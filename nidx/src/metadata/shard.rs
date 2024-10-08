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
use super::{index::*, NidxMetadata};
use sqlx;
use uuid::Uuid;

pub struct Shard {
    pub id: Uuid,
    pub kbid: Uuid,
}

impl Shard {
    pub async fn create(meta: &NidxMetadata, kbid: Uuid) -> Result<Shard, sqlx::Error> {
        sqlx::query_as!(Shard, "INSERT INTO shards (kbid) VALUES ($1) RETURNING *", kbid).fetch_one(&meta.pool).await
    }

    pub async fn indexes(&self, meta: &NidxMetadata) -> sqlx::Result<Vec<Index>> {
        sqlx::query_as!(
            Index,
            r#"SELECT id, shard_id, kind as "kind: IndexKind", name, configuration FROM indexes where shard_id = $1"#,
            self.id
        )
        .fetch_all(&meta.pool)
        .await
    }
}
