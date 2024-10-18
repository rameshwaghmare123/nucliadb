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

use nidx::{indexer, maintenance};
use std::collections::HashSet;
use tokio::{main, task::JoinSet};

#[main]
async fn main() -> anyhow::Result<()> {
    let args: HashSet<_> = std::env::args().skip(1).collect();

    tracing_subscriber::fmt::init();

    let mut tasks = JoinSet::new();
    args.iter().for_each(|arg| {
        match arg.as_str() {
            "indexer" => tasks.spawn(indexer::run()),
            "worker" => tasks.spawn(maintenance::worker::run()),
            "scheduler" => tasks.spawn(maintenance::scheduler::run()),
            other => panic!("Unknown component: {other}"),
        };
    });

    while let Some(join_result) = tasks.join_next().await {
        let task_result = join_result?;
        if let Err(e) = task_result {
            panic!("Task finished with error, stopping: {e:?}");
        }
    }

    Ok(())
}