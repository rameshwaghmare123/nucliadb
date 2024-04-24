use std::collections::HashMap;
use std::path::Path;
use std::sync::Arc;

use std::thread;
use std::time::{Duration, Instant, SystemTime};

use nucliadb_core::protos::*;
use nucliadb_node::shards::metadata::ShardMetadata;
use nucliadb_node::shards::writer::ShardWriter;

use rand::Rng;

fn random_key() -> String {
    format!("{:032x?}", rand::random::<u128>())
}

fn resource(id: usize, counter: u32) -> Resource {
    let mut paragraphs = HashMap::new();

    let mut vector = [0.0; 50].to_vec();
    vector[id] = 1.0;

    let key = format!("r{id}");
    paragraphs.insert(
        format!("{key}p{counter}"),
        IndexParagraph {
            start: 0,
            end: 100,
            sentences: [(
                format!("{key}ps{counter}"),
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
            shard_id: "patata".into(),
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

    let mut i = 0;
    loop {
        let t = Instant::now();
        sw.set_resource(resource(rand::thread_rng().gen_range(0..10), i))?;
        println!("Indexing took {:?}", t.elapsed());
        thread::sleep(Duration::from_millis(20));
        i += 1;
    }

    Ok(())
}
