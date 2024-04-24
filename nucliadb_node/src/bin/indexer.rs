use std::collections::HashMap;
use std::fs::File;
use std::io::Write;
use std::path::Path;
use std::sync::Arc;

use std::thread;
use std::time::{Duration, Instant, SystemTime};

use nucliadb_core::protos::*;
use nucliadb_node::shards::metadata::ShardMetadata;
use nucliadb_node::shards::writer::ShardWriter;

use rand::{random, Rng};

fn random_key() -> String {
    format!("{:032x?}", rand::random::<u128>())
}

fn resource(id: usize, seq: u32) -> Resource {
    let mut paragraphs = HashMap::new();

    let mut vector = [0.0; 50].to_vec();
    vector[id] = 1.0;

    let key = format!("r{id}");
    paragraphs.insert(
        format!("{key}p{seq}"),
        IndexParagraph {
            start: 0,
            end: 100,
            sentences: [(
                format!("{key}ps{seq}"),
                VectorSentence {
                    vector: vector.clone(),
                    ..Default::default()
                },
            )]
            .into_iter()
            .collect(),
            ..Default::default()
        },
    );

    Resource {
        metadata: Some(IndexMetadata {
            modified: Some(SystemTime::now().into()),
            created: Some(SystemTime::now().into()),
        }),
        resource: Some(ResourceId {
            shard_id: seq.to_string(),
            uuid: key.clone(),
        }),
        paragraphs: [(
            "f/text".into(),
            IndexParagraphs {
                paragraphs,
            },
        )]
        .into_iter()
        .collect(),
        sentences_to_delete: vec![key],
        ..Default::default()
    }
}

fn main() -> anyhow::Result<()> {
    let tmp_dir = Path::new("/tmp/shards");
    let metadata = ShardMetadata::new(
        tmp_dir.join("shard"),
        "patata".into(),
        None,
        nucliadb_node::shards::metadata::Similarity::Dot,
        None,
        false,
    );
    let metadata2 = ShardMetadata::new(
        tmp_dir.join("shard"),
        "patata".into(),
        None,
        nucliadb_node::shards::metadata::Similarity::Dot,
        None,
        false,
    );

    let sw = match ShardWriter::open(Arc::new(metadata)) {
        Ok(s) => s,
        Err(_) => ShardWriter::new(Arc::new(metadata2)).unwrap(),
    };

    let mut seq = 1;
    loop {
        let t = Instant::now();
        let mut batch = vec![];
        for _ in 0..100 {
            batch.push((resource(rand::thread_rng().gen_range(0..10), seq), seq));
            println!("Resource {} seq={seq}", batch.last().unwrap().0.resource.as_ref().unwrap().uuid);
            seq += 1;
        }
        batch.sort_by_cached_key(|_| random::<u32>());
        while let Some((resource, _)) = batch.pop() {
            let oldest_pending = batch.iter().chain(vec![(resource.clone(), seq)].iter()).map(|r| r.1).min().unwrap();
            std::fs::write("/tmp/oldest_ack", (oldest_pending - 1).to_ne_bytes())?;

            // Passing seq number as resource.shard_id 🙈
            sw.set_resource(resource)?;
            thread::sleep(Duration::from_millis(10));
        }
        println!("Indexing batch took {:?}", t.elapsed());
        thread::sleep(Duration::from_millis(200));
    }

    Ok(())
}
