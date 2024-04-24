use std::path::Path;
use std::sync::Arc;

use std::time::{Duration, Instant, SystemTime};

use nucliadb_node::metadb::MetaDB;
use nucliadb_vectors::data_point::{self, merge, open, DataPointPin};
use object_store::local::LocalFileSystem;
use object_store::{path, ObjectStore};
use tempfile::tempdir;
use tokio::io::AsyncWriteExt;
use tokio::task::JoinSet;
use tokio_tar::Archive;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let meta = MetaDB::new().await?;

    loop {
        let working_path = tempdir()?;
        let segments = meta.list_segments().await?;

        if segments.len() <= 1 {
            println!("Not enough to merge");
            tokio::time::sleep(Duration::from_millis(1000)).await;
            continue;
        }

        let t = Instant::now();
        println!("Merging {} segments", segments.len());
        let mut tasks = JoinSet::new();
        let storage = Arc::new(LocalFileSystem::new_with_prefix(Path::new("/tmp/shards/shard/objects"))?);
        for s in segments.clone() {
            let wp = working_path.path().to_owned();
            let storage = storage.clone();
            tasks.spawn(async move {
                let stream = storage.get(&object_store::path::Path::from(s.as_str())).await.unwrap().into_stream();
                let reader = tokio_util::io::StreamReader::new(stream);
                let mut unarchiver = Archive::new(reader);
                unarchiver.unpack(wp.join(s)).await.unwrap();
            });
        }
        while tasks.join_next().await.is_some() {}

        let inputs: Vec<_> = segments
            .iter()
            .map(|sid| {
                let pin = DataPointPin::open_pin(working_path.path(), uuid::Uuid::parse_str(sid).unwrap()).unwrap();
                (data_point::NoDLog, open(&pin).unwrap())
            })
            .collect();
        let ii: Vec<_> = inputs.iter().map(|(d, dp)| (d, dp)).collect();
        let output = DataPointPin::create_pin(working_path.path())?;
        let out = output.id();

        merge(&output, ii.as_slice(), nucliadb_vectors::data_point::Similarity::Dot, SystemTime::now())?;

        // Archive & upload
        let uploader = object_store::buffered::BufWriter::new(storage.clone(), out.to_string().into());
        let mut archive = tokio_tar::Builder::new(uploader);
        archive.append_dir_all(".", working_path.path().join(out.to_string())).await?;
        archive.finish().await?;
        let mut x = archive.into_inner().await?;
        x.shutdown().await?;

        meta.replace_segments(segments.clone(), out.to_string()).await?;

        for s in segments {
            storage.delete(&path::Path::from(s)).await?;
        }
        println!("Took {:?}", t.elapsed());
    }

    Ok(())
}
