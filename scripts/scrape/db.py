"""SQLite ledger for the scraping pipeline.

The ledger is *state*, not content: it records what has been attempted, what came
back, and which candidate publications were inferred for each project. Downloaded
bytes live in the HTTP cache; curated verdicts live in `decision` and are never
written by the automated stages.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DB_PATH = REPO / "state" / "scrape.db"

SCHEMA_VERSION = 3

# A task is one (project or corpus) x source x operation unit of work.
#   pending  - never attempted, or explicitly reset for a retry
#   ok       - completed, results found
#   empty    - completed, source genuinely has nothing (NOT an error, do not retry)
#   failed   - transient failure; eligible for retry
#   skipped  - deliberately excluded (e.g. no usable query could be built)
SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS task (
    project_id   TEXT NOT NULL,
    source       TEXT NOT NULL,
    op           TEXT NOT NULL,
    status       TEXT NOT NULL
                 CHECK (status IN ('pending','ok','empty','failed','skipped')),
    attempts     INTEGER NOT NULL DEFAULT 0,
    result_count INTEGER,
    http_status  INTEGER,
    last_error   TEXT,
    -- The exact query that produced this result. When a query is refined the stored
    -- one no longer matches, so the task un-settles itself and is re-run.
    query        TEXT,
    updated_at   TEXT NOT NULL,
    PRIMARY KEY (project_id, source, op)
);
CREATE INDEX IF NOT EXISTS task_status ON task(status, source, op);

CREATE TABLE IF NOT EXISTS fetch (
    url         TEXT PRIMARY KEY,
    cache_key   TEXT NOT NULL,
    http_status INTEGER,
    bytes       INTEGER,
    fetched_at  TEXT NOT NULL
);

-- Every work seen from any source, keyed by a normalized identifier.
CREATE TABLE IF NOT EXISTS work (
    work_id    TEXT PRIMARY KEY,
    doi        TEXT,
    pmid       TEXT,
    pmcid      TEXT,
    title      TEXT,
    journal    TEXT,
    year       INTEGER,
    authors    TEXT,
    is_oa      INTEGER,
    oa_url     TEXT,
    licence    TEXT,
    pdf_url    TEXT,
    sources    TEXT,
    raw_ref    TEXT,
    updated_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS work_doi ON work(doi);

-- Automated project -> work links. Rewritten wholesale by the match stage;
-- `extractor_version` lets a newer matcher invalidate older rows selectively.
CREATE TABLE IF NOT EXISTS candidate (
    project_id        TEXT NOT NULL,
    work_id           TEXT NOT NULL,
    score             REAL NOT NULL,
    evidence          TEXT NOT NULL,
    extractor_version INTEGER NOT NULL,
    updated_at        TEXT NOT NULL,
    PRIMARY KEY (project_id, work_id)
);
CREATE INDEX IF NOT EXISTS candidate_project ON candidate(project_id, score DESC);

-- Project ids found printed inside a work's own full text, near a EuroQol mention.
-- The strongest evidence available: the paper itself names the grant.
CREATE TABLE IF NOT EXISTS fulltext_mention (
    work_id    TEXT NOT NULL,
    project_id TEXT NOT NULL,
    snippet    TEXT,
    updated_at TEXT NOT NULL,
    PRIMARY KEY (work_id, project_id)
);

-- Human curation. The automated stages only ever READ this table.
CREATE TABLE IF NOT EXISTS decision (
    project_id TEXT NOT NULL,
    work_id    TEXT NOT NULL,
    verdict    TEXT NOT NULL CHECK (verdict IN ('accept','reject')),
    note       TEXT,
    decided_by TEXT,
    decided_at TEXT NOT NULL,
    PRIMARY KEY (project_id, work_id)
);
"""


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def connect(path: Path = DB_PATH) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript(SCHEMA)
    conn.execute(
        "INSERT OR IGNORE INTO meta(key, value) VALUES ('schema_version', ?)",
        (str(SCHEMA_VERSION),),
    )
    conn.commit()
    return conn


def set_task(
    conn: sqlite3.Connection,
    project_id: str,
    source: str,
    op: str,
    status: str,
    *,
    result_count: int | None = None,
    http_status: int | None = None,
    error: str | None = None,
    query: str | None = None,
) -> None:
    conn.execute(
        """
        INSERT INTO task(project_id, source, op, status, attempts,
                         result_count, http_status, last_error, query, updated_at)
        VALUES (?,?,?,?,1,?,?,?,?,?)
        ON CONFLICT(project_id, source, op) DO UPDATE SET
            status       = excluded.status,
            attempts     = task.attempts + 1,
            result_count = excluded.result_count,
            http_status  = excluded.http_status,
            last_error   = excluded.last_error,
            query        = excluded.query,
            updated_at   = excluded.updated_at
        """,
        (project_id, source, op, status, result_count, http_status, error, query, now()),
    )


def task_row(conn: sqlite3.Connection, project_id: str, source: str, op: str):
    return conn.execute(
        "SELECT status, query, last_error, http_status, result_count "
        "FROM task WHERE project_id=? AND source=? AND op=?",
        (project_id, source, op),
    ).fetchone()


def is_settled(row, retry_failed: bool = False, query: str | None = None) -> bool:
    """Whether a task needs no further work on this run.

    A stored query that differs from the one we would issue now means the heuristic
    has been refined since; the task is not settled, whatever its status says.
    """
    if row is None:
        return False
    if query is not None and row["query"] != query:
        return False
    if row["status"] in ("ok", "empty", "skipped"):
        return True
    return row["status"] == "failed" and not retry_failed
