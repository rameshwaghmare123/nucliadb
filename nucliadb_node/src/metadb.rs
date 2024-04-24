use nucliadb_core::NodeResult;
use sqlx::{migrate, sqlite::SqlitePoolOptions, Executor, Pool, Sqlite};

#[derive(Debug)]
pub struct MetaDB {
    conn: Pool<Sqlite>,
}

impl MetaDB {
    pub async fn new() -> NodeResult<Self> {
        let conn = SqlitePoolOptions::new().connect("sqlite:///tmp/meta.sqlite").await?;

        migrate!("./migrations").run(&conn).await?;

        Ok(MetaDB {
            conn,
        })
    }

    pub async fn register_segment(&self, segment_id: String) -> NodeResult<i64> {
        let opstamp = self.next_opstamp().await?;
        sqlx::query!("INSERT INTO segments (segment_id, opstamp) VALUES (?, ?)", segment_id, opstamp)
            .execute(&self.conn)
            .await?;
        Ok(opstamp)
    }

    pub async fn list_segments(&self) -> NodeResult<Vec<(String, i64)>> {
        let segs = sqlx::query!("SELECT segment_id, opstamp FROM segments")
            .fetch_all(&self.conn)
            .await?
            .iter()
            .map(|x| (x.segment_id.clone().unwrap(), x.opstamp.unwrap()))
            .collect();
        Ok(segs)
    }

    pub async fn replace_segments(&self, remove: Vec<String>, add: String, opstamp: i64) -> NodeResult<()> {
        let mut tx = self.conn.begin().await?;
        let params = format!("?{}", ", ?".repeat(remove.len() - 1));
        let query_str = format!("DELETE FROM segments WHERE segment_id IN ( { } )", params);
        let mut q = sqlx::query(&query_str);
        for r in &remove {
            q = q.bind(r);
        }
        let deleted = tx.execute(q).await?.rows_affected();
        if deleted as usize != remove.len() {
            tx.rollback().await?;
            return Err(anyhow::anyhow!("WTF replace segment"));
        }
        tx.execute(sqlx::query!("INSERT INTO segments (segment_id, opstamp) VALUES (?, ?)", add, opstamp)).await?;
        tx.commit().await?;
        Ok(())
    }

    pub async fn record_deletions(&self, opstamp: i64, remove: &Vec<String>) -> NodeResult<()> {
        let mut tx = self.conn.begin().await?;

        for r in remove {
            tx.execute(sqlx::query!("INSERT INTO deletions (opstamp, resource_id) VALUES (?, ?)", opstamp, r)).await?;
        }
        tx.commit().await?;
        Ok(())
    }

    pub async fn record_segment_deletions(&self, segment_id: String, remove: &Vec<String>) -> NodeResult<i64> {
        let opstamp = self.next_opstamp().await?;
        let mut tx = self.conn.begin().await?;
        sqlx::query!("INSERT INTO segments (segment_id, opstamp) VALUES (?, ?)", segment_id, opstamp)
            .execute(&mut *tx)
            .await?;

        for r in remove {
            tx.execute(sqlx::query!("INSERT INTO deletions (opstamp, resource_id) VALUES (?, ?)", opstamp, r)).await?;
        }
        tx.commit().await?;
        Ok(opstamp)
    }

    pub async fn trim_deletions(&self) -> NodeResult<()> {
        sqlx::query!("DELETE FROM deletions WHERE opstamp <= (SELECT min(opstamp) FROM segments)")
            .execute(&self.conn)
            .await?;
        Ok(())
    }

    pub async fn next_opstamp(&self) -> NodeResult<i64> {
        let max = sqlx::query_scalar!("SELECT MAX(opstamp) FROM segments").fetch_one(&self.conn).await?;
        Ok(max.unwrap_or(0) as i64 + 1)
    }

    pub async fn list_deletions(&self) -> NodeResult<Vec<(String, i64)>> {
        let dels = sqlx::query!("SELECT resource_id, MAX(opstamp) AS opstamp FROM deletions GROUP BY resource_id")
            .fetch_all(&self.conn)
            .await?
            .iter()
            .map(|x| (x.resource_id.clone().unwrap(), x.opstamp.unwrap() as i64))
            .collect();
        Ok(dels)
    }

    pub async fn list_segments_and_deletions(&self) -> NodeResult<(Vec<(String, i64)>, Vec<(String, i64)>)> {
        let mut tx = self.conn.begin().await?;
        let segs = sqlx::query!("SELECT segment_id, opstamp FROM segments")
            .fetch_all(&mut *tx)
            .await?
            .iter()
            .map(|x| (x.segment_id.clone().unwrap(), x.opstamp.unwrap()))
            .collect();
        let dels = sqlx::query!("SELECT resource_id, MAX(opstamp) AS opstamp FROM deletions GROUP BY resource_id")
            .fetch_all(&mut *tx)
            .await?
            .iter()
            .map(|x| (x.resource_id.clone().unwrap(), x.opstamp.unwrap() as i64))
            .collect();
        Ok((segs, dels))
    }
}
