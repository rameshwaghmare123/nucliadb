use std::collections::HashMap;
use std::path::Path;
use std::sync::Arc;

use std::thread;
use std::time::{Duration, Instant, SystemTime};

use nucliadb_core::protos::*;
use nucliadb_node::shards::metadata::ShardMetadata;
use nucliadb_node::shards::writer::ShardWriter;

use rand::Rng;
use tempfile::tempdir;

fn random_key() -> String {
    format!("{:032x?}", rand::random::<u128>())
}

fn resource() -> Resource {
    let mut paragraphs = HashMap::new();
    for i in 0..rand::thread_rng().gen_range(0..1000) {
        paragraphs.insert(
            format!("p{i}"),
            IndexParagraph {
                start: i * 100,
                end: (i + 1) * 100,
                sentences: [(
                    "a".into(),
                    VectorSentence {
                        vector: vec![1.0, 2.0, 3.0],
                        ..Default::default()
                    },
                )]
                .into_iter()
                .collect(),
                ..Default::default()
            },
        );
    }

    Resource {
        metadata: Some(IndexMetadata {
            modified: Some(SystemTime::now().into()),
            created: Some(SystemTime::now().into()),
        }),
        resource: Some(ResourceId {
            shard_id: "patata".into(),
            uuid: random_key(),
        }),
        paragraphs: [(
            "f/text".into(),
            IndexParagraphs {
                paragraphs,
            },
        )]
        .into_iter()
        .collect(),
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
    let sw = ShardWriter::open(Arc::new(metadata))?;

    loop {
        let t = Instant::now();
        sw.set_resource(resource())?;
        println!("Indexing took {:?}", t.elapsed());
        thread::sleep(Duration::from_millis(250));
    }

    Ok(())
}
