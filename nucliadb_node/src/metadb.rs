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

    pub async fn register_segment(&self, segment_id: String) -> NodeResult<()> {
        sqlx::query!("INSERT INTO segments (segment_id) VALUES (?)", segment_id).execute(&self.conn).await?;
        Ok(())
    }

    pub async fn list_segments(&self) -> NodeResult<Vec<String>> {
        let segs = sqlx::query_scalar!("SELECT segment_id AS \"a!\" FROM segments").fetch_all(&self.conn).await?;
        Ok(segs)
    }

    pub async fn replace_segments(&self, remove: Vec<String>, add: String) -> NodeResult<()> {
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
        tx.execute(sqlx::query!("INSERT INTO segments (segment_id) VALUES (?)", add)).await?;
        tx.commit().await?;
        Ok(())
    }
}
