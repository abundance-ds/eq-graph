#!/usr/bin/env python3
"""Check the public EQ-Graph SQLite database."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


EXPECTED_COUNTS = {
    "projects": 1024,
    "publications": 209,
    "studies": 207,
    "project_publications": 242,
    "findings": 871,
    "limitations": 602,
}

FORBIDDEN_TEXT = (
    "/Users/",
    "/private/",
    "input/projects/",
    "source_path",
    "record_path",
    ".xml",
    ".md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database", type=Path)
    return parser.parse_args()


def main() -> None:
    path = parse_args().database
    uri = f"file:{path.resolve()}?mode=ro"
    connection = sqlite3.connect(uri, uri=True)
    connection.execute("PRAGMA query_only = ON")

    errors = connection.execute("PRAGMA foreign_key_check").fetchall()
    if errors:
        raise SystemExit(f"Foreign-key check failed: {errors[:5]}")
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    if integrity != "ok":
        raise SystemExit(f"Integrity check failed: {integrity}")

    for table, expected in EXPECTED_COUNTS.items():
        actual = connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        if actual != expected:
            raise SystemExit(f"{table}: expected {expected}, found {actual}")

    if connection.execute("SELECT COUNT(*) FROM project_publications WHERE project_output IS NULL").fetchone()[0] > 0:
        raise SystemExit("An accepted project link has no output decision.")

    tables = [row[0] for row in connection.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
    for table in tables:
        columns = [row[1] for row in connection.execute(f"PRAGMA table_info({table})") if row[2].upper() == "TEXT"]
        for column in columns:
            for forbidden in FORBIDDEN_TEXT:
                row = connection.execute(
                    f"SELECT rowid FROM {table} WHERE instr(COALESCE({column},''), ?) > 0 LIMIT 1",
                    (forbidden,),
                ).fetchone()
                if row:
                    raise SystemExit(f"Unsafe text in {table}.{column}: {forbidden}")

    connection.close()
    print("Serving database checks passed.")


if __name__ == "__main__":
    main()
