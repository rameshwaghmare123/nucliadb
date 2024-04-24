use std::collections::{HashMap, HashSet};
use std::path::{Path, PathBuf};
use std::sync::{Arc, Mutex};

use std::time::Duration;
use std::{fs, thread};

use nucliadb_node::metadb::MetaDB;
use nucliadb_vectors::data_point_provider::reader::Reader;
use nucliadb_vectors::data_point_provider::SearchRequest;
use nucliadb_vectors::formula::Formula;
use object_store::local::LocalFileSystem;
use object_store::ObjectStore;
use tempfile::tempdir;
use tokio::task::JoinSet;
use tokio_tar::Archive;

struct Search {
    vector: Vec<f32>,
    formula: Formula,
}

impl SearchRequest for Search {
    fn get_query(&self) -> &[f32] {
        &self.vector
    }

    fn get_filter(&self) -> &Formula {
        &self.formula
    }

    fn no_results(&self) -> usize {
        10
    }

    fn with_duplicates(&self) -> bool {
        true
    }

    fn min_score(&self) -> f32 {
        0.9
    }
}

fn update_thread(working_path: PathBuf, reader: Arc<Mutex<Reader>>) {
    let storage = Arc::new(LocalFileSystem::new_with_prefix(Path::new("/tmp/shards/shard/objects")).unwrap());
    let rt = tokio::runtime::Builder::new_current_thread().enable_time().build().unwrap();
    let meta = rt.block_on(MetaDB::new()).unwrap();
    let mut last_segments = HashSet::new();
    loop {
        thread::sleep(Duration::from_millis(100));
        let (segments, deletions) = rt.block_on(meta.list_segments_and_deletions()).unwrap();
        println!(
            "Max seg = {}, Max deletion = {}",
            segments.iter().map(|x| x.1).max().unwrap(),
            deletions.iter().map(|x| x.1).max().unwrap()
        );
        assert_eq!(segments.iter().map(|x| x.1).max().unwrap(), deletions.iter().map(|x| x.1).max().unwrap());
        let segment_set: HashSet<_> = segments.iter().map(|x| x.0.clone()).collect();
        if segment_set == last_segments {
            continue;
        }
        // To download
        for s in segment_set.difference(&last_segments) {
            let wp = working_path.clone();
            let storage = storage.clone();
            rt.block_on(async move {
                let stream = storage.get(&object_store::path::Path::from(s.as_str())).await.unwrap().into_stream();
                let reader = tokio_util::io::StreamReader::new(stream);
                let mut unarchiver = Archive::new(reader);
                unarchiver.unpack(wp.join(s)).await.unwrap();
            });
        }

        // To remove
        for s in last_segments.difference(&segment_set) {
            let segment_dir = working_path.join(s);
            fs::remove_dir_all(segment_dir).unwrap();
        }

        println!("Updating! to {} segments", segments.len());
        reader.lock().unwrap().update(&segments, &deletions).unwrap();
        println!("Updated!");

        last_segments = segment_set;
    }
}

fn main() -> anyhow::Result<()> {
    let tmp = tempdir()?;
    let working_path = tmp.path().to_owned();

    let reader = Arc::new(Mutex::new(Reader::open(&working_path)?));

    let wp = working_path.clone();
    let r = reader.clone();
    std::thread::spawn(|| update_thread(wp, r));

    let mut latest: HashMap<usize, u32> = HashMap::new();
    thread::sleep(Duration::from_secs(2));
    loop {
        let vector = [0.0; 50].to_vec();
        for resource in 0..10 {
            let mut v = vector.clone();
            v[resource] = 1.0;
            // Do queries
            let s = Search {
                vector: v,
                formula: Formula::new(),
            };
            let lr = reader.lock().unwrap();
            let results = lr.search(&s).unwrap();
            let keys: Vec<_> = results.iter().map(|x| String::from_utf8(x.id().to_vec()).unwrap()).collect();
            if keys.is_empty() {
                println!("No results found for {resource}");
                let mut keys = lr.keys()?;
                keys.sort();
                println!("Available keys = {:?}", keys);
                continue;
            } else if keys.len() > 1 {
                panic!("Multiple results for {resource}: {keys:?}");
            }
            let v = keys[0].split("ps").nth(1).unwrap().parse::<u32>().unwrap();
            let old_v = *latest.get(&resource).unwrap_or(&0);
            assert!(old_v <= v, "not {old_v} <= {v}");
            latest.insert(resource, v);
        }
        thread::sleep(Duration::from_millis(10));
    }

    Ok(())
}
