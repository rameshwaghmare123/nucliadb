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
//

use std::collections::HashSet;

use nidx_vector::config::VectorType;
use nidx_vector::data_point_provider::{DTrie, SearchRequest};
use nidx_vector::formula::Formula;
use nidx_vector::{
    config::{Similarity, VectorConfig},
    data_point::{self, Elem, LabelDictionary},
    data_point_provider::reader::Reader,
};
use rstest::rstest;
use tempfile::tempdir;

fn elem(index: usize) -> Elem {
    let mut vector: Vec<f32> = [0.0; DIMENSION].into();
    vector[index] = 1.0;

    Elem::new(format!("key_{index}"), vector, LabelDictionary::default(), None)
}

#[derive(Clone, Debug, PartialEq)]
struct Request {
    vector: Vec<f32>,
    formula: Formula,
}

impl SearchRequest for Request {
    fn with_duplicates(&self) -> bool {
        false
    }
    fn get_query(&self) -> &[f32] {
        &self.vector
    }

    fn get_filter(&self) -> &Formula {
        &self.formula
    }

    fn no_results(&self) -> usize {
        10
    }
    fn min_score(&self) -> f32 {
        -1.0
    }
}

const DIMENSION: usize = 128;

#[rstest]
fn test_basic_search(
    #[values(Similarity::Dot, Similarity::Cosine)] similarity: Similarity,
    #[values(VectorType::DenseF32Unaligned, VectorType::DenseF32 { dimension: DIMENSION })] vector_type: VectorType,
) -> anyhow::Result<()> {
    let workdir = tempdir()?;
    let segment_path = workdir.path();
    let config = VectorConfig {
        similarity,
        vector_type,
        ..Default::default()
    };

    // Write some data
    let segment = data_point::create(segment_path, (0..DIMENSION).map(elem).collect(), &config, HashSet::new())?;

    // Search for a specific element
    let reader = Reader::open(vec![(segment.into_metadata(), 0i64.into())], config, DTrie::new())?;
    let search_for = elem(5);
    let results = reader._search(
        &Request {
            vector: search_for.vector,
            formula: Formula::new(),
        },
        &None,
    )?;
    assert_eq!(results.len(), 10);
    assert_eq!(results[0].id(), search_for.key);
    assert_eq!(results[0].score(), 1.0);
    assert_eq!(results[1].score(), 0.0);

    // Search near a few elements
    let mut vector: Vec<f32> = [0.0; DIMENSION].into();
    vector[42] = 0.7;
    vector[43] = 0.6;
    vector[44] = 0.5;
    vector[45] = 0.4;
    let results = reader._search(
        &Request {
            vector,
            formula: Formula::new(),
        },
        &None,
    )?;
    assert_eq!(results.len(), 10);
    assert_eq!(results[0].id(), elem(42).key);
    assert!(results[0].score() > 0.2);
    assert_eq!(results[1].id(), elem(43).key);
    assert!(results[1].score() > 0.2);
    assert_eq!(results[2].id(), elem(44).key);
    assert!(results[2].score() > 0.2);
    assert_eq!(results[3].id(), elem(45).key);
    assert!(results[3].score() > 0.2);
    assert_eq!(results[5].score(), 0.0);

    Ok(())
}
