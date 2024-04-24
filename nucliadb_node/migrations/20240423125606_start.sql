-- Add migration script here
CREATE TABLE segments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    segment_id TEXT,
    opstamp INTEGER
);

CREATE TABLE deletions(
    opstamp INTEGER,
    resource_id TEXT
)