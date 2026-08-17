#!/usr/bin/env python3
"""Run integrity and search checks on a loaded production pilot database."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from evaluate import CALIBRATION


def scalar(connection: sqlite3.Connection, query: str, parameters: tuple = ()) -> int:
    return int(connection.execute(query, parameters).fetchone()[0])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("database")
    parser.add_argument("--expected", type=int, required=True)
    args = parser.parse_args()
    path = (CALIBRATION / args.database).resolve()
    if CALIBRATION.resolve() not in path.parents:
        raise ValueError("database must be inside the calibration directory")
    connection = sqlite3.connect(path)
    checks: list[tuple[str, bool, object]] = []

    publication_count = scalar(connection, "SELECT COUNT(*) FROM publication")
    checks.append(("publication count", publication_count == args.expected, publication_count))
    checks.append(
        (
            "extraction count",
            scalar(connection, "SELECT COUNT(*) FROM extraction_record") == args.expected,
            scalar(connection, "SELECT COUNT(*) FROM extraction_record"),
        )
    )
    checks.append(
        (
            "unique DOI count",
            scalar(connection, "SELECT COUNT(DISTINCT doi) FROM publication") == args.expected,
            scalar(connection, "SELECT COUNT(DISTINCT doi) FROM publication"),
        )
    )
    missing_terms = scalar(
        connection,
        "SELECT COUNT(*) FROM extraction_record e "
        "WHERE e.disposition='include-study' AND "
        "(SELECT COUNT(*) FROM record_term rt WHERE rt.record_id=e.record_id) < 4",
    )
    checks.append(("included records have index terms", missing_terms == 0, missing_terms))
    excluded_terms = scalar(
        connection,
        "SELECT COUNT(*) FROM extraction_record e JOIN record_term rt USING(record_id) "
        "WHERE e.disposition IN ('exclude','publication-context')",
    )
    checks.append(("excluded records have no index terms", excluded_terms == 0, excluded_terms))
    empty_metadata = scalar(
        connection,
        "SELECT COUNT(*) FROM publication WHERE doi='' OR title='' OR metadata_json=''",
    )
    checks.append(("required metadata present", empty_metadata == 0, empty_metadata))
    fact_count = scalar(connection, "SELECT COUNT(*) FROM record_fact")
    checks.append(("fact bullets loaded", fact_count > publication_count, fact_count))
    fts_count = scalar(connection, "SELECT COUNT(*) FROM record_fts WHERE record_fts MATCH '\"EQ-5D\"'")
    checks.append(("full-text search works", fts_count > 0, fts_count))
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    checks.append(("SQLite integrity", integrity == "ok", integrity))

    failed = 0
    for name, passed, evidence in checks:
        print(f"{'PASS' if passed else 'FAIL'}\t{name}\t{evidence}")
        failed += int(not passed)
    summary = {
        "checks": len(checks),
        "passed": len(checks) - failed,
        "failed": failed,
        "publications": publication_count,
        "terms": scalar(connection, "SELECT COUNT(*) FROM term"),
        "record_terms": scalar(connection, "SELECT COUNT(*) FROM record_term"),
        "facts": fact_count,
    }
    print("SUMMARY\t" + json.dumps(summary, sort_keys=True))
    connection.close()
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
