use clap::Parser;
use nucliadb_core::tracing;
use nucliadb_vectors::data_point::{self, DataPointPin, Elem, LabelDictionary, Similarity};
use nucliadb_vectors::data_point_provider::garbage_collector;
use nucliadb_vectors::data_point_provider::reader::Reader;
use nucliadb_vectors::data_point_provider::writer::Writer;
use nucliadb_vectors::data_point_provider::*;
use nucliadb_vectors::formula::*;
use rand::seq::SliceRandom;
use rand::Rng;
use serde_json::json;
use std::io::Write;
use std::path::Path;
use std::sync::{Arc, RwLock};
use std::time::Duration;
use std::time::SystemTime;
use vectors_benchmark::json_writer::write_json;
use vectors_benchmark::random_vectors::RandomVectors;
use vectors_benchmark::stats::Stats;

const BATCH_SIZE: usize = 5000;
const NO_NEIGHBOURS: usize = 5;
const INDEX_SIZE: usize = 1_000_000;
const VECTOR_DIM: usize = 128;
const LABELS: [&str; 5] = [
    "nucliad_db_has_label_1",
    "nucliad_db_has_label_2",
    "nucliad_db_has_label_3",
    "nucliad_db_has_label_4",
    "nucliad_db_has_label_5",
];
const CYCLES: usize = 25;

macro_rules! measure_time {
    ( seconds $code:block ) => {{
        let start_time = std::time::Instant::now();
        let result = $code;
        let elapsed_time = start_time.elapsed().as_secs_f64();
        (result, elapsed_time)
    }};
    ( milliseconds $code:block ) => {{
        let start_time = std::time::Instant::now();
        let result = $code;
        let elapsed_time = start_time.elapsed().as_millis() as f64;
        (result, elapsed_time)
    }};
    ( microseconds $code:block ) => {{
        let start_time = std::time::Instant::now();
        let result = $code;
        let elapsed_time = start_time.elapsed().as_micros() as f64;
        (result, elapsed_time)
    }};
}

#[derive(Parser, Debug)]
#[clap(author, version, about, long_about = None)]
pub struct Args {
    /// Size of index
    #[clap(short, long, default_value_t = INDEX_SIZE)]
    index_size: usize,
    /// Size of batch
    #[clap(short, long, default_value_t = BATCH_SIZE)]
    batch_size: usize,
    /// Number of search cycles
    #[clap(short, long, default_value_t = CYCLES)]
    cycles: usize,
    /// Path of the json output file
    #[clap(short, long, default_value_t = String::from("./benchmark.json"))]
    json_output: String,
    /// Merge results if json output file exists
    #[clap(short, long, action)]
    merge: bool,
}

impl Default for Args {
    fn default() -> Self {
        Args::new()
    }
}
impl Args {
    pub fn new() -> Args {
        Args::parse()
    }
}

struct Request {
    vector: Vec<f32>,
    filter: Formula,
}
impl SearchRequest for Request {
    fn with_duplicates(&self) -> bool {
        true
    }
    fn get_query(&self) -> &[f32] {
        &self.vector
    }

    fn get_filter(&self) -> &Formula {
        &self.filter
    }

    fn no_results(&self) -> usize {
        NO_NEIGHBOURS
    }
    fn min_score(&self) -> f32 {
        -1.0
    }
}

fn random_labels(batch_no: usize, key: String, index_size: usize) -> LabelDictionary {
    let index = key.parse::<usize>().unwrap() + batch_no;

    let seventy_percent = (index_size as f64 * 0.7) as usize;
    let mut labels: Vec<String> = vec![];

    // the first 70% gets label 1, the remaining 30% label 2
    if index < seventy_percent {
        labels.push(LABELS[0].to_string());
    } else {
        labels.push(LABELS[1].to_string());
    }

    // and we randomly pick more labels
    let mut rng = rand::thread_rng();
    let num_elements = rng.gen_range(0..=3);

    for _ in 0..num_elements {
        let random_index = rng.gen_range(2..LABELS.len());
        labels.push(LABELS[random_index].to_string());
    }

    LabelDictionary::new(labels)
}

fn add_batch(batch_no: usize, writer: &mut Writer, elems: Vec<(String, Vec<f32>)>, index_size: usize) {
    let new_data_point_pin = DataPointPin::create_pin(writer.location()).unwrap();
    let temporal_mark = SystemTime::now();
    let similarity = Similarity::Cosine;
    let elems = elems
        .into_iter()
        .map(|(key, vector)| Elem::new(key.clone(), vector, random_labels(batch_no, key.clone(), index_size), None))
        .collect();

    data_point::create(&new_data_point_pin, elems, Some(temporal_mark), similarity).unwrap();

    writer.add_data_point(new_data_point_pin).unwrap();
    writer.commit().unwrap();
}

fn vector_random_subset<T: Clone>(vector: Vec<T>) -> Vec<T> {
    let mut rng = rand::thread_rng();
    let size = vector.len();
    let subset_size = rng.gen_range(1..=size);
    let mut random_indices: Vec<usize> = (0..size).collect();
    random_indices.shuffle(&mut rng);
    random_indices.truncate(subset_size);
    random_indices.iter().map(|&index| vector[index].clone()).collect()
}

fn generate_vecs(count: usize) -> Vec<RandomVectors> {
    let mut res = vec![];
    for _ in 0..count {
        res.push(RandomVectors::new(VECTOR_DIM));
    }
    res
}

fn create_db(db_location: &Path, index_size: usize, batch_size: usize, vecs: &[RandomVectors]) -> f64 {
    println!("Writing starts..");
    let mut writer = Writer::new(db_location, IndexMetadata::default()).unwrap();
    let mut writing_time: f64 = 0.0;
    for (i, vec) in vecs.iter().enumerate().take(index_size / batch_size) {
        let elems = vec.take(batch_size).enumerate().map(|(i, q)| (i.to_string(), q)).collect();

        let (_, elapsed_time) = measure_time!(milliseconds {
            add_batch(i, &mut writer, elems, index_size);
        });

        writing_time += elapsed_time;
        print!("{} vectors included       \r", batch_size * i);
        let _ = std::io::stdout().flush();
    }
    println!("\nCleaning garbage..");

    garbage_collector::collect_garbage(writer.location()).unwrap();

    println!("Garbage cleaned");
    writing_time
}

fn create_filtered_request() -> Request {
    let random_subset = vector_random_subset(LABELS.to_vec().clone());

    let formula = random_subset.clone().into_iter().fold(Formula::new(), |mut acc, i| {
        acc.extend(AtomClause::label(i.to_string()));
        acc
    });

    Request {
        filter: formula,
        vector: RandomVectors::new(VECTOR_DIM).next().unwrap(),
    }
}

fn test_datapoint(
    index_size: usize,
    batch_size: usize,
    cycles: usize,
    unfiltered_request: &Request,
    filtered_requests: &[Request],
    vecs: &[RandomVectors],
) -> Stats {
    let mut stats = Stats {
        writing_time: 0,
        read_time: 0,
        tagged_time: 0,
    };

    let at = tempfile::TempDir::new().unwrap();
    let db_location = at.path().join("vectors");

    stats.writing_time = create_db(&db_location, index_size, batch_size, vecs) as u128;

    let reader = Reader::open(&db_location).unwrap();

    for cycle in 0..cycles {
        print!("Unfiltered Search => cycle {} of {}      \r", (cycle + 1), cycles);
        let _ = std::io::stdout().flush();

        let (_, elapsed_time) = measure_time!(microseconds {
            reader.search(unfiltered_request).unwrap();
        });
        stats.read_time += elapsed_time as u128;
    }

    stats.read_time /= cycles as u128;
    println!();

    for (cycle, filtered_request) in filtered_requests.iter().enumerate().take(cycles) {
        print!("Filtered Search => cycle {} of {}      \r", (cycle + 1), cycles);
        let _ = std::io::stdout().flush();

        let (_, elapsed_time) = measure_time!(microseconds {
            reader.search(filtered_request).unwrap();
        });
        stats.tagged_time += elapsed_time as u128;
    }

    println!();
    stats.tagged_time /= cycles as u128;
    stats
}

pub fn search(reader: Arc<RwLock<Reader>>, request: Request) {
    loop {
        std::thread::sleep(Duration::from_millis(100));
        let read_guard = reader.read().unwrap();
        let (_, elapsed_time) = measure_time!(microseconds {
            read_guard.search(&request).unwrap()
        });
        println!("SEARCH: {elapsed_time} µs");
    }
}

pub fn update(reader: Arc<RwLock<Reader>>) {
    let update_cycle = 1000 as f64;
    let mut current_cycle = 0 as f64;
    let mut current_cycle_time = 0.0 as f64;
    loop {
        std::thread::sleep(Duration::from_millis(10));
        let mut write_guard = reader.write().unwrap();
        let (_, elapsed_time) = measure_time!(microseconds {
            write_guard.update().unwrap();
        });
        current_cycle_time += elapsed_time;
        current_cycle += 1.0;
        if current_cycle == update_cycle {
            let cycle_average = (current_cycle_time / update_cycle) as u128;
            println!("UPDATE: {cycle_average} µs");
            current_cycle_time = 0.0;
            current_cycle = 0.0;
        }
    }
}

pub fn ingest(writer: Arc<RwLock<Writer>>, index_size: usize, batch_size: usize, vecs: &[RandomVectors]) {
    let mut writing_time: f64 = 0.0;
    for (i, vec) in vecs.iter().enumerate().take(index_size / batch_size) {
        let mut write_guard = writer.write().unwrap();
        let elems = vec.take(batch_size).enumerate().map(|(i, q)| (i.to_string(), q)).collect();
        let (_, elapsed_time) = measure_time!(milliseconds {
            add_batch(i, &mut write_guard, elems, index_size);
        });

        writing_time += elapsed_time;
        println!("WRITE: {} vectors included", batch_size * i);
        let _ = std::io::stdout().flush();
    }
}

pub fn garbage_collect(writer: Arc<RwLock<Writer>>) {
    loop {
        std::thread::sleep(Duration::from_secs(15));
        let mut write_guard = writer.write().unwrap();
        let (_, elapsed_time) = measure_time!(microseconds {
            write_guard.collect_garbage().unwrap();
        });
        println!("GC: {elapsed_time} µs");
    }
}

fn main() {
    let args = Args::new();

    let at = tempfile::TempDir::new().unwrap();
    let db_location = at.path().join("vectors");
    let vecs = generate_vecs(args.index_size / args.batch_size);
    let writer = Writer::new(&db_location, IndexMetadata::default()).unwrap();
    let reader = Reader::open(&db_location).unwrap();
    let writer = Arc::new(RwLock::new(writer));
    let reader = Arc::new(RwLock::new(reader));

    let request = Request {
        filter: Formula::new(),
        vector: RandomVectors::new(VECTOR_DIM).next().unwrap(),
    };
    let search_reader = Arc::clone(&reader);
    let search_handle = std::thread::spawn(move || search(search_reader, request));

    let update_reader = Arc::clone(&reader);
    let update_handle = std::thread::spawn(move || update(update_reader));

    let ingest_writer = Arc::clone(&writer);
    let index_size = args.index_size;
    let batch_size = args.batch_size;
    let ingest_handle = std::thread::spawn(move || ingest(ingest_writer, index_size, batch_size, &vecs));

    let gc_writer = Arc::clone(&writer);
    let gc_handle = std::thread::spawn(move || garbage_collect(gc_writer));

    search_handle.join().unwrap();

    // let unfiltered_request = Request {
    //     filter: Formula::new(),
    //     vector: RandomVectors::new(VECTOR_DIM).next().unwrap(),
    // };

    // let mut filtered_requests: Vec<Request> = vec![];
    // for _ in 0..args.cycles {
    //     filtered_requests.push(create_filtered_request());
    // }
    // let stats =
    //     test_datapoint(args.index_size, args.batch_size, args.cycles, &unfiltered_request, &filtered_requests, &vecs);

    // json_results.extend(vec![
    //     json!({
    //         "name": format!("Writing Time"),
    //         "unit": "ms",
    //         "value": stats.writing_time,
    //     }),
    //     json!({
    //     "name": format!("Reading Time"),
    //     "unit": "µs",
    //     "value": stats.read_time,

    //     }),
    //     json!({
    //     "name": format!("Reading Time with Labels"),
    //     "unit": "µs",
    //     "value": stats.tagged_time,

    //     }),
    // ]);

    // let pjson = serde_json::to_string_pretty(&json_results).unwrap();
    // println!("{}", pjson);
    // write_json(args.json_output, json_results, args.merge).unwrap();
}
