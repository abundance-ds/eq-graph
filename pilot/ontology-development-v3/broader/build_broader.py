#!/usr/bin/env python3
"""Build the SQLite database for the 20-paper broader test."""

from __future__ import annotations

import argparse
import csv
import hashlib
import sqlite3
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
SQLITE_DIR = SCRIPT_DIR.parent / "sqlite"
sys.path.append(str(SQLITE_DIR))

from build_pilot import insert_metadata  # noqa: E402
from jats_metadata import parse_jats  # noqa: E402
from semantic_seed import load_semantic  # noqa: E402


PARENT_XML = "input/projects/2016440/papers/doi_10.1371_journal.pone.0209344.xml"
PARENT_XML_SHA256 = "576ccfe6e6a590363456b1ef92ec86601157ee5876d837c8175301d9288532ec"
PARENT_XML_BYTES = 122371


def read_batch() -> dict[str, dict[str, str]]:
    with (SCRIPT_DIR / "BATCH.tsv").open(encoding="utf-8", newline="") as handle:
        return {row["record_id"]: row for row in csv.DictReader(handle, delimiter="\t")}


def verify(path: Path, expected_hash: str, expected_bytes: int) -> None:
    if path.stat().st_size != expected_bytes:
        raise ValueError(f"Byte-count mismatch: {path}")
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected_hash:
        raise ValueError(f"SHA-256 mismatch: {path}")


def validate(connection: sqlite3.Connection) -> dict[str, int]:
    foreign_key_errors = connection.execute("PRAGMA foreign_key_check").fetchall()
    if foreign_key_errors:
        raise ValueError(f"Foreign-key errors: {foreign_key_errors}")
    checks = {
        "publications": connection.execute("SELECT count(*) FROM publication").fetchone()[0],
        "studies": connection.execute("SELECT count(*) FROM study").fetchone()[0],
        "accepted_project_links": connection.execute(
            "SELECT count(*) FROM project_publication WHERE link_status = 'accepted'"
        ).fetchone()[0],
        "candidate_project_links": connection.execute(
            "SELECT count(*) FROM project_publication WHERE link_status = 'candidate'"
        ).fetchone()[0],
        "instruments": connection.execute("SELECT count(*) FROM instrument").fetchone()[0],
        "instrument_uses": connection.execute("SELECT count(*) FROM instrument_use").fetchone()[0],
        "methods": connection.execute("SELECT count(*) FROM research_method").fetchone()[0],
        "models": connection.execute("SELECT count(*) FROM statistical_model").fetchone()[0],
        "products": connection.execute("SELECT count(*) FROM research_product").fetchone()[0],
        "findings": connection.execute("SELECT count(*) FROM finding").fetchone()[0],
        "limitations": connection.execute("SELECT count(*) FROM limitation").fetchone()[0],
    }
    expected = {
        "publications": 21,
        "studies": 19,
        "accepted_project_links": 18,
        "candidate_project_links": 2,
    }
    for name, value in expected.items():
        if checks[name] != value:
            raise ValueError(f"Expected {name}={value}; got {checks[name]}")

    lifecycle = connection.execute(
        "SELECT doi, lifecycle_status FROM publication WHERE lifecycle_status != 'active' ORDER BY doi"
    ).fetchall()
    if lifecycle != [
        ("10.1007/s40273-021-01002-z", "retracted"),
        ("10.1371/journal.pone.0305983", "correction-notice"),
    ]:
        raise ValueError(f"Publication lifecycle invariant failed: {lifecycle}")
    relation = connection.execute(
        "SELECT s.doi, r.relation_type, t.doi "
        "FROM publication_relation AS r "
        "JOIN publication AS s ON s.publication_id = r.source_publication_id "
        "JOIN publication AS t ON t.publication_id = r.target_publication_id"
    ).fetchall()
    if relation != [
        ("10.1371/journal.pone.0305983", "corrects", "10.1371/journal.pone.0209344")
    ]:
        raise ValueError(f"Publication relation invariant failed: {relation}")
    if connection.execute("SELECT execution_status FROM study WHERE study_id = 'B10'").fetchone() != ("planned",):
        raise ValueError("The protocol paper is not marked as planned")
    if connection.execute("SELECT count(*) FROM study WHERE study_id = 'B17'").fetchone()[0]:
        raise ValueError("The correction notice became a study")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=SCRIPT_DIR / "broader-test.sqlite")
    args = parser.parse_args()
    output_path = args.db.resolve()
    if output_path.suffix != ".sqlite" or REPO_ROOT not in output_path.parents:
        raise ValueError("Database output must be a .sqlite file inside the repository")
    if output_path.exists():
        output_path.unlink()

    batch = read_batch()
    if len(batch) != 20:
        raise ValueError("The broader manifest must contain 20 rows")
    connection = sqlite3.connect(output_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript((SQLITE_DIR / "schema.sql").read_text(encoding="utf-8"))
        for record_id, row in batch.items():
            xml_path = REPO_ROOT / row["xml_path"]
            verify(xml_path, row["xml_sha256"], int(row["xml_bytes"]))
            parsed = parse_jats(xml_path)
            if parsed["publication"]["doi"] != row["doi"].lower():
                raise ValueError(f"{record_id}: DOI mismatch")
            insert_metadata(connection, parsed)

        parent_path = REPO_ROOT / PARENT_XML
        verify(parent_path, PARENT_XML_SHA256, PARENT_XML_BYTES)
        parent = parse_jats(parent_path)
        if parent["publication"]["doi"] != "10.1371/journal.pone.0209344":
            raise ValueError("Correction-parent DOI mismatch")
        insert_metadata(connection, parent)

        connection.execute(
            "UPDATE publication SET lifecycle_status = 'retracted' WHERE doi = '10.1007/s40273-021-01002-z'"
        )
        connection.execute(
            "UPDATE publication SET lifecycle_status = 'correction-notice' WHERE doi = '10.1371/journal.pone.0305983'"
        )
        connection.execute(
            "INSERT INTO publication_relation "
            "(source_publication_id, target_publication_id, relation_type, source_locator) "
            "VALUES ('doi:10.1371/journal.pone.0305983', 'doi:10.1371/journal.pone.0209344', "
            "'corrects', 'correction notice body')"
        )
        load_semantic(connection, REPO_ROOT, batch)
        checks = validate(connection)
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()

    print(f"Built {output_path}")
    for name, value in checks.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
