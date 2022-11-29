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

use std::collections::HashMap;

use nucliadb_protos::resource::ResourceStatus;
use nucliadb_protos::{DeleteGraphNodes, JoinGraph, Resource, ResourceId};
use nucliadb_service_interface::prelude::*;
use tracing::*;

use super::utils::*;
use crate::relations::errors::RelationsErr as InnerErr;
use crate::relations::index::*;

pub struct RelationsWriterService {
    wmode: WMode,
    index: Index,
}
impl RelationsWriterService {
    fn delete_node(&self, writer: &mut GraphWriter, id: Entity) -> InternalResult<()> {
        let affects = writer.delete_node(&self.wmode, id)?;
        for affected in affects {
            let affected_value = writer.get_node(affected)?;
            let no_in = writer.get_inedges(affected)?.count();
            let no_out = writer.get_outedges(affected)?.count();
            if no_in == 0 && no_out == 0 && !affected_value.defined_by_user() {
                writer.delete_node(&self.wmode, affected)?;
            }
        }
        Ok(())
    }
}
impl RelationWriter for RelationsWriterService {
    fn delete_nodes(&mut self, graph: &DeleteGraphNodes) -> InternalResult<()> {
        let mut writer = self.index.start_writing()?;
        for node in graph.nodes.iter() {
            let name = node.value.clone();
            let (xtype, subtype) = node_type_parsing(node.ntype(), &node.subtype);
            let node = IoNode::new(name, xtype.to_string(), subtype.map(|s| s.to_string()));
            if let Some(id) = writer.get_node_id(node.hash())? {
                self.delete_node(&mut writer, id)?;
            }
        }
        Ok(writer.commit(&mut self.wmode)?)
    }
    fn join_graph(&mut self, graph: &JoinGraph) -> InternalResult<()> {
        let mut writer = self.index.start_writing()?;
        let nodes: HashMap<_, _> = graph
            .nodes
            .iter()
            .map(|(k, v)| (k, v.value.clone(), node_type_parsing(v.ntype(), &v.subtype)))
            .map(|(key, value, (xtype, subtype))| (key, value, xtype, subtype))
            .map(|(key, value, xtype, subtype)| (key, value, xtype.to_string(), subtype))
            .map(|(key, value, xtype, subtype)| (key, value, xtype, subtype.map(|s| s.to_string())))
            .map(|(&key, value, xtype, subtype)| (key, IoNode::user_node(value, xtype, subtype)))
            .collect();

        let ubehaviour = || Err(InnerErr::UBehaviour);
        for edge in graph.edges.iter() {
            let from = nodes.get(&edge.source).map_or_else(ubehaviour, Ok)?;
            let to = nodes.get(&edge.target).map_or_else(ubehaviour, Ok)?;
            let edge = rtype_parsing(edge.rtype(), &edge.rsubtype);
            let edge = IoEdge::new(edge.0.to_string(), edge.1.map(|s| s.to_string()));
            writer.connect(&self.wmode, from, to, &edge)?;
        }
        Ok(writer.commit(&mut self.wmode)?)
    }
}
impl std::fmt::Debug for RelationsWriterService {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("RelationWriterService").finish()
    }
}

impl WriterChild for RelationsWriterService {
    fn stop(&mut self) -> InternalResult<()> {
        info!("Stopping relation writer Service");
        Ok(())
    }
    fn count(&self) -> usize {
        let mut count = 0;
        match self
            .index
            .start_reading()
            .and_then(|reader| reader.no_nodes())
        {
            Err(err) => error!("{err:?}"),
            Ok(v) => count = v as usize,
        }
        count
    }
    fn delete_resource(&mut self, x: &ResourceId) -> InternalResult<()> {
        let node = IoNode::new(x.uuid.clone(), dictionary::ENTITY.to_string(), None);
        let mut writer = self.index.start_writing()?;
        if let Some(id) = writer.get_node_id(node.hash())? {
            self.delete_node(&mut writer, id)?;
        }
        Ok(())
    }
    fn set_resource(&mut self, resource: &Resource) -> InternalResult<()> {
        if resource.status != ResourceStatus::Delete as i32 {
            let mut writer = self.index.start_writing()?;
            let iter = resource
                .relations
                .iter()
                .filter(|rel| rel.to.is_some() || rel.source.is_some());
            for rel in iter {
                let edge = rtype_parsing(rel.relation(), &rel.relation_label);
                let from = rel.source.as_ref().unwrap();
                let from_type = node_type_parsing(from.ntype(), &from.subtype);
                let to = rel.to.as_ref().unwrap();
                let to_type = node_type_parsing(to.ntype(), &to.subtype);
                let from = IoNode::system_node(
                    from.value.clone(),
                    from_type.0.to_string(),
                    from_type.1.map(|s| s.to_string()),
                );
                let to = IoNode::system_node(
                    to.value.clone(),
                    to_type.0.to_string(),
                    to_type.1.map(|s| s.to_string()),
                );
                let edge = IoEdge::new(edge.0.to_string(), edge.1.map(|s| s.to_string()));
                writer.connect(&self.wmode, &from, &to, &edge)?;
            }
            writer.commit(&mut self.wmode)?;
        }
        Ok(())
    }
    fn garbage_collection(&mut self) {}
}

impl RelationsWriterService {
    pub fn start(config: &RelationConfig) -> InternalResult<Self> {
        let path = std::path::Path::new(&config.path);
        let (index, wmode) = Index::new_writer(path)?;
        Ok(RelationsWriterService { index, wmode })
    }
    pub fn new(config: &RelationConfig) -> InternalResult<Self> {
        let path = std::path::Path::new(&config.path);
        if path.exists() {
            Err(Box::new("Shard already created".to_string()))
        } else {
            std::fs::create_dir_all(path).unwrap();
            let (index, wmode) = Index::new_writer(path)?;
            Ok(RelationsWriterService { index, wmode })
        }
    }

    pub fn open(config: &RelationConfig) -> InternalResult<Self> {
        let path = std::path::Path::new(&config.path);
        if !path.exists() {
            Err(Box::new("Shard does not exist".to_string()))
        } else {
            let (index, wmode) = Index::new_writer(path)?;
            Ok(RelationsWriterService { index, wmode })
        }
    }
}