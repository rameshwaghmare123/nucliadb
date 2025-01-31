// Copyright (C) 2021 Bosutech XXI S.L.
//
// nucliadb is offered under the AGPL v3.0 and as commercial software.
// For commercial licensing, contact us at info@nuclia.com.
//
// AGPL:
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.

use std::collections::{HashMap, HashSet};
use std::hash::Hash;
use std::num::NonZeroUsize;
use std::sync::{Arc, Weak};

use anyhow::anyhow;
use lru::LruCache;
use nidx_vector::config::VectorConfig;
use nidx_vector::VectorSearcher;
use tokio::sync::{Mutex, Semaphore};

use crate::metadata::{IndexId, Segment, SegmentId};
use crate::NidxMetadata;

use super::sync::SyncMetadata;

pub enum IndexSearcher {
    Vector(VectorSearcher),
}

pub struct IndexCache {
    cache: Mutex<ResourceCache<IndexId, IndexSearcher>>,
    sync_metadata: Arc<SyncMetadata>,
    metadb: NidxMetadata,
}

impl IndexCache {
    pub fn new(metadata: Arc<SyncMetadata>, metadb: NidxMetadata) -> Self {
        IndexCache {
            cache: ResourceCache::new_unbounded().into(),
            sync_metadata: metadata,
            metadb,
        }
    }

    pub async fn get(&self, id: &IndexId) -> anyhow::Result<Arc<IndexSearcher>> {
        loop {
            let cached = { self.cache.lock().await.get(id) };
            match cached {
                CacheResult::Cached(shard) => return Ok(shard),
                CacheResult::Wait(waiter) => waiter.wait().await,
                CacheResult::Load(guard) => {
                    let loaded = self.load(id).await?;
                    self.cache.lock().await.loaded(guard, &loaded);
                    return Ok(loaded);
                }
            }
        }
    }

    pub async fn remove(&self, id: &IndexId) {
        self.cache.lock().await.remove(id);
    }

    pub async fn load(&self, id: &IndexId) -> anyhow::Result<Arc<IndexSearcher>> {
        let read = self.sync_metadata.get(id).await;
        let read2 = read.get().await;
        let Some(meta) = read2 else {
            return Err(anyhow!("Index not found"));
        };

        // TODO: Cleaner mapping from sync metadata to IndexSeacher metadata
        // We might also want to make this granular, so diff updates can be applied, e.g:
        // list of new segments to open + list of new deletions to apply
        let segments = sqlx::query_as!(
            Segment,
            "SELECT * FROM segments WHERE id = ANY($1)",
            meta.operations.segments().collect::<Vec<_>>() as Vec<SegmentId>
        )
        .fetch_all(&self.metadb.pool)
        .await?
        .into_iter()
        .map(|s| (s.id, s))
        .collect::<HashMap<SegmentId, Segment>>();

        let operations = meta
            .operations
            .0
            .iter()
            .map(|op| {
                (
                    op.seq,
                    op.segment_ids
                        .iter()
                        .map(|sid| nidx_types::SegmentMetadata {
                            path: self.sync_metadata.segment_location(id, sid),
                            records: segments[sid].records.unwrap() as usize,
                            tags: HashSet::new(),
                        })
                        .collect::<Vec<_>>(),
                    op.deleted_keys.clone(),
                )
            })
            .collect();

        Ok(Arc::new(IndexSearcher::Vector(VectorSearcher::open(VectorConfig::default(), operations)?)))
    }
}

// Used to track when an entry is being loaded. Once this is dropped,
// we know the entry finished loading or failed to do so, and we can
// unlock other clients waiting for it.
struct ResourceLoadGuard<K> {
    waiter: Arc<Semaphore>,
    key: K,
}

impl<K> Drop for ResourceLoadGuard<K> {
    fn drop(&mut self) {
        self.waiter.close();
    }
}

// Use to wait until an entry is ready to be used
struct ResourceWaiter(Arc<Semaphore>);
impl ResourceWaiter {
    pub async fn wait(self) {
        let _ = self.0.acquire().await;
    }
}

enum CacheResult<K, V> {
    Cached(Arc<V>),
    Load(ResourceLoadGuard<K>),
    Wait(ResourceWaiter),
}

struct ResourceCache<K, V> {
    live: LruCache<K, Arc<V>>,
    eviction: HashMap<K, Weak<V>>,
    capacity: Option<NonZeroUsize>,
    loading: HashMap<K, Arc<Semaphore>>,
}

impl<K, V> ResourceCache<K, V>
where
    K: Eq + Hash + Clone + std::fmt::Debug,
{
    #[allow(dead_code)]
    pub fn new_with_capacity(capacity: NonZeroUsize) -> Self {
        ResourceCache {
            capacity: Some(capacity),
            live: LruCache::unbounded(),
            eviction: HashMap::new(),
            loading: HashMap::new(),
        }
    }

    pub fn new_unbounded() -> Self {
        ResourceCache {
            capacity: None,
            live: LruCache::unbounded(),
            eviction: HashMap::new(),
            loading: HashMap::new(),
        }
    }

    // Try to get an entry from the cache
    // 1. If it's present, we return Cached(entry). Consumer can use it.
    // 2. If it's not in the cache, we return Load(guard). Consumer should load it and call
    //    cache.loaded with the guard.
    // 3. If it's being loaded concurrently, we return Wait(waiter). Consumer should wait using the
    //    waiter and then retry the get.
    pub fn get(&mut self, id: &K) -> CacheResult<K, V> {
        if let Some(v) = self.get_cached(id) {
            return CacheResult::Cached(v);
        }

        if let Some(wait) = self.loading.get(id) {
            if wait.is_closed() {
                // The loading process finished but is still in the loading tree
                // This happens when the guard was dropped without saving an object
                // This is an error loading, we can retry by returning a load object
                self.loading.remove(id);
            } else {
                return CacheResult::Wait(ResourceWaiter(wait.clone()));
            }
        }

        let waiter = Arc::new(Semaphore::new(0));
        self.loading.insert(id.clone(), waiter.clone());
        CacheResult::Load(ResourceLoadGuard {
            waiter,
            key: id.clone(),
        })
    }

    pub fn loaded(&mut self, guard: ResourceLoadGuard<K>, v: &Arc<V>) {
        self.loading.remove(&guard.key);
        self.insert(&guard.key, v);
        drop(guard);
    }

    pub fn remove(&mut self, k: &K) {
        self.live.pop(k);
    }

    pub fn get_cached(&mut self, id: &K) -> Option<Arc<V>> {
        if let Some(v) = self.eviction.get(id).and_then(Weak::upgrade) {
            self.insert(id, &v);
            return Some(v);
        }
        self.live.get(id).cloned()
    }

    pub fn insert(&mut self, k: &K, v: &Arc<V>) {
        if self.live.len() >= self.capacity.unwrap_or(NonZeroUsize::MAX).into() {
            self.evict();
        }
        self.live.push(k.clone(), Arc::clone(v));
    }

    fn evict(&mut self) {
        if let Some((evicted_k, evicted_v)) = self.live.pop_lru() {
            self.eviction.insert(evicted_k, Arc::downgrade(&evicted_v));
        }
    }
}

#[cfg(test)]
mod tests {
    use std::num::NonZeroUsize;
    use std::sync::atomic::AtomicU8;
    use std::sync::mpsc::channel;
    use std::sync::{Arc, Mutex};
    use std::time::Duration;

    use anyhow::anyhow;
    use rand::Rng;
    use tokio::task::JoinSet;

    use super::{CacheResult, ResourceCache};

    static OBJCOUNTER: [AtomicU8; 8] = [
        AtomicU8::new(0),
        AtomicU8::new(0),
        AtomicU8::new(0),
        AtomicU8::new(0),
        AtomicU8::new(0),
        AtomicU8::new(0),
        AtomicU8::new(0),
        AtomicU8::new(0),
    ];

    #[derive(Debug)]
    struct CacheItem(usize);

    impl CacheItem {
        async fn new(k: usize) -> anyhow::Result<Self> {
            tokio::time::sleep(Duration::from_millis(50)).await;
            if rand::thread_rng().gen_ratio(1, 10) {
                return Err(anyhow!("patata"));
            }
            let old = OBJCOUNTER[k].fetch_add(1, std::sync::atomic::Ordering::SeqCst);
            if old >= 1 {
                panic!("A resource was opened more than once simultaneously");
            }
            Ok(Self(k))
        }
    }

    impl Drop for CacheItem {
        fn drop(&mut self) {
            OBJCOUNTER[self.0].fetch_sub(1, std::sync::atomic::Ordering::SeqCst);
        }
    }

    #[tokio::test]
    async fn test_cache_rng() {
        let cache: ResourceCache<usize, CacheItem> = ResourceCache::new_with_capacity(NonZeroUsize::new(3).unwrap());
        let cache = Arc::new(Mutex::new(cache));

        let mut tasks = JoinSet::new();
        for _ in 0..16 {
            let cc = cache.clone();
            tasks.spawn(async move {
                for _i in 0..50 {
                    // Wait for next request
                    let t = Duration::from_millis(rand::thread_rng().gen_range(0..5));
                    tokio::time::sleep(t).await;

                    // Get a shard
                    let k = rand::thread_rng().gen_range(0..8);
                    let shard = {
                        loop {
                            let cached = { cc.lock().unwrap().get(&k) };
                            match cached {
                                CacheResult::Cached(shard) => break shard,
                                CacheResult::Wait(waiter) => waiter.wait().await,
                                CacheResult::Load(guard) => {
                                    if let Ok(loaded) = CacheItem::new(k).await {
                                        let loaded = Arc::new(loaded);
                                        cc.lock().unwrap().loaded(guard, &loaded);
                                        break loaded;
                                    }
                                }
                            }
                        }
                    };

                    // Do something
                    let t = Duration::from_millis(rand::thread_rng().gen_range(1..20));
                    tokio::time::sleep(t).await;
                    drop(shard);
                }
            });
        }
        tasks.join_all().await;
    }

    #[test]
    fn test_lru() {
        let mut cache: ResourceCache<usize, usize> = ResourceCache::new_with_capacity(NonZeroUsize::new(2).unwrap());

        let items = vec![Arc::new(0), Arc::new(1), Arc::new(2), Arc::new(3)];

        // Keeps the latest inserted ones
        cache.insert(&0, &items[0]);
        cache.insert(&1, &items[1]);
        cache.insert(&2, &items[2]);
        cache.insert(&3, &items[3]);

        assert!(!cache.live.contains(&0));
        assert!(!cache.live.contains(&1));
        assert!(cache.live.contains(&2));
        assert!(cache.live.contains(&3));

        // Keeps the recently used
        cache.get(&2);
        cache.insert(&0, &items[0]);

        assert!(cache.live.contains(&0));
        assert!(!cache.live.contains(&1));
        assert!(cache.live.contains(&2));
        assert!(!cache.live.contains(&3));
    }

    #[test]
    fn test_eviction() {
        let mut cache: ResourceCache<usize, usize> = ResourceCache::new_with_capacity(NonZeroUsize::new(1).unwrap());

        let item0 = Arc::new(0);
        let item1 = Arc::new(1);

        // Fill the cache
        cache.insert(&0, &item0);

        // Insert a new one, 0 is getting evicted
        cache.insert(&1, &item1);

        assert!(!cache.live.contains(&0));
        assert!(cache.eviction.contains_key(&0));

        // 0 should be evicted, but there are still references to it
        // from this test code. Requesting it again should reuse that
        // instance.
        assert!(matches!(cache.get(&0), CacheResult::Cached(_)));
        assert!(cache.live.contains(&0));

        // Currently the cache contains 0. Let's delete the last reference
        // to 1 (from this test) and try to get it, we should be asked to
        // load it, since it'll be out of the cache.
        drop(item1);
        assert!(matches!(cache.get(&1), CacheResult::Load(_)));
    }

    #[tokio::test]
    async fn test_loading() {
        let cache: ResourceCache<usize, usize> = ResourceCache::new_unbounded();
        let cache = Arc::new(Mutex::new(cache));

        // Item not in cache, we are asked to load it
        let CacheResult::Load(load_guard) = cache.lock().unwrap().get(&0) else {
            panic!("Expected a CacheResult::Load")
        };

        // If we try to get it from elsewhere, we wait a waiter
        let CacheResult::Wait(waiter) = cache.lock().unwrap().get(&0) else {
            panic!("Expected a CacheResult::Wait")
        };

        // We start two threads to load and wait, we expect the wait to block
        // until the load is complete
        let mut tasks = JoinSet::new();

        let (tx, rx) = channel();
        let tx_clone = tx.clone();
        let cache_clone = cache.clone();
        tasks.spawn(async move {
            waiter.wait().await;
            assert!(matches!(cache_clone.lock().unwrap().get(&0), CacheResult::Cached(_)));
            tx_clone.send(1).unwrap();
        });
        tasks.spawn(async move {
            // Sleep a little bit to ensure the waiter actually waits
            tokio::time::sleep(Duration::from_millis(5)).await;
            let mut unlocked_cache = cache.lock().unwrap();
            tx.send(0).unwrap();
            unlocked_cache.loaded(load_guard, &Arc::new(0));
        });

        // Both threads finished without panic/failing assert
        tasks.join_all().await;

        // Load thread stores before wait thread waken up
        assert_eq!(rx.recv().unwrap(), 0);
        assert_eq!(rx.recv().unwrap(), 1);
    }

    #[tokio::test]
    async fn test_loading_failed() {
        let cache: ResourceCache<usize, usize> = ResourceCache::new_unbounded();
        let cache = Arc::new(Mutex::new(cache));

        // Item not in cache, we are asked to load it
        let CacheResult::Load(load_guard) = cache.lock().unwrap().get(&0) else {
            panic!("Expected a CacheResult::Load")
        };

        // If we try to get it from elsewhere, we wait a waiter
        let CacheResult::Wait(waiter) = cache.lock().unwrap().get(&0) else {
            panic!("Expected a CacheResult::Wait")
        };

        // We start two threads to load and wait, we expect the wait to block
        // until the load is complete
        let mut tasks = JoinSet::new();

        let (tx, rx) = channel();
        let tx_clone = tx.clone();
        let cache_clone = cache.clone();
        tasks.spawn(async move {
            waiter.wait().await;
            // The load will fail, so we expect to be asked
            // to load it ourselves
            assert!(matches!(cache_clone.lock().unwrap().get(&0), CacheResult::Load(_)));
            tx_clone.send(1).unwrap();
        });
        tasks.spawn(async move {
            // Sleep a little bit to ensure the waiter actually waits
            tokio::time::sleep(Duration::from_millis(5)).await;
            // Fail to call `loaded`. This should drop the load_guard
            // which will mark the load as failed.
            tx.send(0).unwrap();
            drop(load_guard);
        });

        // Both threads finished without panic/failing assert
        tasks.join_all().await;

        // Load thread finished earlier
        assert_eq!(rx.recv().unwrap(), 0);
        assert_eq!(rx.recv().unwrap(), 1);
    }
}
