use std::collections::{HashMap, HashSet};
use std::path::{Path, PathBuf};
use std::sync::{Arc, Mutex};

use std::time::Duration;
use std::{fs, thread};

use itertools::Itertools;
use nucliadb_node::metadb::MetaDB;
use nucliadb_vectors::data_point_provider::reader::Reader;
use nucliadb_vectors::data_point_provider::SearchRequest;
use nucliadb_vectors::formula::Formula;
use object_store::gcp::GoogleCloudStorageBuilder;
use object_store::local::LocalFileSystem;
use object_store::ObjectStore;
use tantivy::directory::MmapDirectory;
use tantivy::fastfield::AliveBitSet;
use tantivy::postings::SegmentPostings;
use tantivy::query::{EnableScoring, Query, TermQuery};
use tantivy::schema::IndexRecordOption;
use tantivy::{Index, Segment, SegmentId, SegmentMeta, SegmentReader, Term};
use tantivy_common::BitSet;
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
    let storage = Arc::new(LocalFileSystem::new_with_prefix("/tmp/objects").unwrap());
    let rt = tokio::runtime::Builder::new_current_thread().enable_time().enable_io().build().unwrap();
    let meta = rt.block_on(MetaDB::new()).unwrap();
    let mut last_segments = HashSet::new();
    loop {
        thread::sleep(Duration::from_millis(50));
        let (segments, deletions) = rt.block_on(meta.list_segments_and_deletions(1000000000)).unwrap();

        let ms = segments.iter().map(|x| x.1).max().unwrap();
        let ds = deletions.iter().map(|x| x.1).max();

        // if let Some(ds) = ds {
        //     assert_eq!(ms, ds);
        // }

        let segment_set: HashSet<_> = segments.iter().map(|x| x.0.clone()).collect();
        if segment_set == last_segments {
            continue;
        }
        // To download
        for s in segment_set.difference(&last_segments) {
            let wp = working_path.clone();
            let storage = storage.clone();
            if !s.contains("para") {
                continue;
            }
            rt.block_on(async move {
                let stream = storage.get(&object_store::path::Path::from(s.as_str())).await;
                if let Ok(x) = stream {
                    println!("Ok {}", s);
                    let stream = x.into_stream();
                    let reader = tokio_util::io::StreamReader::new(stream);
                    let mut unarchiver = Archive::new(reader);
                    unarchiver.unpack(wp.join(s)).await.unwrap();
                }
            });
        }

        // To remove
        for s in last_segments.difference(&segment_set) {
            let segment_dir = working_path.join(s);
            fs::remove_dir_all(segment_dir).unwrap();
        }

        let (para, vector): (Vec<_>, Vec<_>) = segments.into_iter().partition(|x| x.0.contains("para"));

        println!("{:?}", para.first());

        let index = Index::open_or_create(
            MmapDirectory::open(&working_path).unwrap(),
            nucliadb_paragraphs3::schema::ParagraphSchema::new().schema,
        )
        .unwrap();
        let meta = index.new_segment_meta(SegmentId::from_uuid_string(&para[0].0[5..]).unwrap(), 100);
        let segment = index.segment(meta);
        let reader = SegmentReader::open(&segment).unwrap();
        let del_query = TermQuery::new(
            Term::from_field_text(nucliadb_paragraphs3::schema::ParagraphSchema::new().field_uuid, "patata"),
            IndexRecordOption::Basic,
        );
        let mut bs = BitSet::with_max_value_and_full(100);
        del_query
            .weight(EnableScoring::disabled_from_schema(&index.schema()))
            .unwrap()
            .for_each_no_score(&reader, &mut |x| {
                println!("Deleted set of docs {x:?}");
                for d in x {
                    bs.remove(*d);
                }
            })
            .unwrap();
        //bs.serialize(writer)
        //let ids = reader.doc_ids_alive().collect::<Vec<_>>();

        println!("Updating! to {} segments", para.len());
        reader.lock().unwrap().update(&vector, &deletions).unwrap();
        println!("Updated!");

        last_segments = segment_set;
    }
}

fn main() -> anyhow::Result<()> {
    let tmp = tempdir()?;
    let working_path = tmp.path().to_owned();
    let para_working_path = tmp.path().to_owned();

    let reader = Arc::new(Mutex::new(Reader::open(&working_path)?));
    // let preader = Arc::new(Mutex::new(nucliadb_paragraphs3::reader::ParagraphReaderService))

    let wp = working_path.clone();
    let r = reader.clone();
    std::thread::spawn(|| update_thread(wp, r));

    let mut latest: HashMap<usize, u32> = HashMap::new();
    thread::sleep(Duration::from_secs(20));
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
                println!("SEGMENTS {:#?}", lr.segment_versions);
                println!(
                    "DELETIONS {:#?}",
                    lr.deletions.iter().map(|(x, y)| (String::from_utf8_lossy(x), y)).collect_vec()
                );
                panic!("Multiple results for {resource}: {keys:?}");
            }
            let v = keys[0].split("ps").nth(1).unwrap().parse::<u32>().unwrap();
            let old_v = *latest.get(&resource).unwrap_or(&0);
            assert!(old_v <= v, "not {old_v} <= {v}");
            latest.insert(resource, v);
        }
        println!("Search PASS");
        thread::sleep(Duration::from_millis(10));
    }

    Ok(())
}
