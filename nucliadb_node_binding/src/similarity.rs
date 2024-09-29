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
use pyo3::prelude::*;
use pyo3::types::PyList;
use pyo3::exceptions::PyTypeError;
#[pyclass]
pub struct Similarity {}

#[pymethods]
impl Similarity {
    #[new]
    pub fn new() -> PyResult<Self> {
        Ok(Self {})
    }

    pub fn cosine<'p>(&self, a: &PyList, b: &PyList, py: Python<'p>) -> PyResult<f32> {
        let a: Vec<f32> = a.extract()?;
        let b: Vec<f32> = b.extract()?;
        
        if a.len() != b.len() {
            return Err(PyTypeError::new_err("Vectors must be of the same length"));
        }

        let dot_product = a.iter().zip(b.iter()).map(|(a, b)| a * b).sum::<f32>();
        let norm_a = a.iter().map(|a| a.powi(2)).sum::<f32>().sqrt();
        let norm_b = b.iter().map(|b| b.powi(2)).sum::<f32>().sqrt();
        Ok(dot_product / (norm_a * norm_b))
    }

    pub fn dot_product<'p>(&self, a: &PyList, b: &PyList, py: Python<'p>) -> PyResult<f32> {
        let a: Vec<f32> = a.extract()?;
        let b: Vec<f32> = b.extract()?;
        
        if a.len() != b.len() {
            return Err(PyTypeError::new_err("Vectors must be of the same length"));
        }

        Ok(a.iter().zip(b.iter()).map(|(a, b)| a * b).sum())
    }
}