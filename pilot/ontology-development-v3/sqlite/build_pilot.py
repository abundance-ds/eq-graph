#!/usr/bin/env python3
"""Build the isolated EuroQol ontology SQLite pilot."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sqlite3
from pathlib import Path

from jats_metadata import parse_jats
from semantic_seed import load_semantic


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]


def read_pilot_set() -> dict[str, dict[str, str]]:
    path = SCRIPT_DIR / "PILOT_SET.tsv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = {row["record_id"]: row for row in csv.DictReader(handle, delimiter="\t")}
    if set(rows) != {"H01", "H02", "H03", "H04", "H05", "H06", "H07", "H08", "H09", "H10", "H11"}:
        raise ValueError("PILOT_SET.tsv does not contain the expected eleven records")
    return rows


def verify_inputs(rows: dict[str, dict[str, str]]) -> None:
    for record_id, row in rows.items():
        for field in ("record_path", "article_path", "xml_path"):
            path = REPO_ROOT / row[field]
            if not path.is_file():
                raise FileNotFoundError(f"{record_id}: missing {field}: {path}")
        xml_path = REPO_ROOT / row["xml_path"]
        actual = hashlib.sha256(xml_path.read_bytes()).hexdigest()
        if actual != row["xml_sha256"]:
            raise ValueError(f"{record_id}: XML hash mismatch")


def insert_metadata(connection: sqlite3.Connection, parsed: dict) -> None:
    publication = parsed["publication"]
    connection.execute(
        "INSERT INTO publication "
        "(publication_id, doi, pmid, pmcid, title, abstract, journal, publisher, "
        "article_type, language, volume, issue, article_number, licence_url, open_access, "
        "canonical_url, source_path, source_sha256, source_bytes, metadata_status) VALUES "
        "(:publication_id, :doi, :pmid, :pmcid, :title, :abstract, :journal, :publisher, "
        ":article_type, :language, :volume, :issue, :article_number, :licence_url, :open_access, "
        ":canonical_url, :source_path, :source_sha256, :source_bytes, :metadata_status)",
        publication,
    )
    publication_id = publication["publication_id"]
    connection.executemany(
        "INSERT OR IGNORE INTO publication_date VALUES (?, ?, ?)",
        [(publication_id, item["type"], item["value"]) for item in parsed["dates"]],
    )
    connection.executemany(
        "INSERT OR IGNORE INTO publication_url VALUES (?, ?, ?)",
        [(publication_id, item["type"], item["url"]) for item in parsed["urls"]],
    )
    for author in parsed["authors"]:
        connection.execute(
            "INSERT INTO author (author_id, display_name, family_name, given_names, orcid) "
            "VALUES (?, ?, ?, ?, ?) ON CONFLICT(author_id) DO UPDATE SET "
            "display_name = excluded.display_name, "
            "family_name = COALESCE(author.family_name, excluded.family_name), "
            "given_names = COALESCE(author.given_names, excluded.given_names), "
            "orcid = COALESCE(author.orcid, excluded.orcid)",
            (
                author["id"],
                author["display_name"],
                author["family_name"],
                author["given_names"],
                author["orcid"],
            ),
        )
        connection.execute(
            "INSERT INTO publication_author "
            "(publication_id, author_id, author_order, corresponding, email, roles) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                publication_id,
                author["id"],
                author["order"],
                int(author["corresponding"]),
                author["email"],
                "; ".join(author["roles"]) or None,
            ),
        )
    for affiliation in parsed["affiliations"]:
        connection.execute(
            "INSERT INTO affiliation VALUES (?, ?, ?, ?, ?, ?)",
            (
                publication_id,
                affiliation["id"],
                affiliation["name"],
                affiliation["ror"],
                affiliation["grid"],
                affiliation["isni"],
            ),
        )
    valid_affiliations = {item["id"] for item in parsed["affiliations"]}
    for author in parsed["authors"]:
        for affiliation_id in author["affiliation_ids"]:
            if affiliation_id not in valid_affiliations:
                continue
            connection.execute(
                "INSERT OR IGNORE INTO author_affiliation VALUES (?, ?, ?)",
                (publication_id, author["id"], affiliation_id),
            )
    for item in parsed["correspondence"]:
        connection.execute(
            "INSERT INTO publication_correspondence "
            "(publication_id, label, correspondence_text, email) VALUES (?, ?, ?, ?)",
            (publication_id, item["label"], item["text"], item["email"]),
        )
    connection.executemany(
        "INSERT OR IGNORE INTO publication_keyword VALUES (?, ?)",
        [(publication_id, value) for value in parsed["keywords"]],
    )
    connection.executemany(
        "INSERT OR IGNORE INTO publication_category VALUES (?, ?, ?)",
        [(publication_id, item["type"], item["value"]) for item in parsed["categories"]],
    )
    for item in parsed["funding"]:
        connection.execute(
            "INSERT INTO publication_funding "
            "(publication_id, funder, award_id, recipient, source_text, source_locator) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                publication_id,
                item["funder"],
                item["award_id"],
                item["recipient"],
                item["source_text"],
                item["source_locator"],
            ),
        )
    for item in parsed["references"]:
        connection.execute(
            "INSERT INTO publication_reference "
            "(publication_id, source_reference_id, citation_text, doi, pmid) "
            "VALUES (?, ?, ?, ?, ?)",
            (
                publication_id,
                item["source_reference_id"],
                item["citation_text"],
                item["doi"],
                item["pmid"],
            ),
        )


def load_projects(connection: sqlite3.Connection, rows: dict[str, dict[str, str]]) -> None:
    project_ids = {row["project_id"] for row in rows.values() if row["project_id"]}
    project_ids.update({"341-RA", "357-RA"})
    for project_id in sorted(project_ids):
        path = REPO_ROOT / "input" / "projects" / project_id / "project.json"
        title = None
        if path.is_file():
            title = json.loads(path.read_text(encoding="utf-8")).get("title")
        connection.execute("INSERT INTO project VALUES (?, ?)", (project_id, title))


def validate_database(connection: sqlite3.Connection) -> dict[str, int]:
    foreign_key_errors = connection.execute("PRAGMA foreign_key_check").fetchall()
    if foreign_key_errors:
        raise ValueError(f"Foreign-key errors: {foreign_key_errors}")
    checks = {
        "publications": connection.execute("SELECT count(*) FROM publication").fetchone()[0],
        "studies": connection.execute("SELECT count(*) FROM study").fetchone()[0],
        "accepted_project_links": connection.execute(
            "SELECT count(*) FROM project_publication WHERE link_status = 'accepted'"
        ).fetchone()[0],
        "rejected_project_links": connection.execute(
            "SELECT count(*) FROM project_publication WHERE link_status = 'rejected'"
        ).fetchone()[0],
        "authors": connection.execute("SELECT count(*) FROM author").fetchone()[0],
        "affiliations": connection.execute("SELECT count(*) FROM affiliation").fetchone()[0],
        "references": connection.execute("SELECT count(*) FROM publication_reference").fetchone()[0],
        "concepts": connection.execute("SELECT count(*) FROM study_concept").fetchone()[0],
        "findings": connection.execute("SELECT count(*) FROM finding").fetchone()[0],
        "limitations": connection.execute("SELECT count(*) FROM limitation").fetchone()[0],
    }
    expected = {
        "publications": 11,
        "studies": 10,
        "accepted_project_links": 10,
        "rejected_project_links": 2,
    }
    for name, value in expected.items():
        if checks[name] != value:
            raise ValueError(f"Expected {name}={value}; got {checks[name]}")
    h11 = connection.execute(
        "SELECT s.eq_instrument_status, pp.link_status "
        "FROM study AS s JOIN project_publication AS pp USING (publication_id) "
        "WHERE s.study_id = 'H11'"
    ).fetchone()
    if h11 != ("none-reported", "accepted"):
        raise ValueError(f"H11 boundary invariant failed: {h11}")
    h09_study_count = connection.execute("SELECT count(*) FROM study WHERE study_id = 'H09'").fetchone()[0]
    h09_accepted_count = connection.execute(
        "SELECT count(*) FROM project_publication AS pp "
        "JOIN publication AS p USING (publication_id) "
        "WHERE p.doi = '10.1038/s41433-023-02860-x' AND pp.link_status = 'accepted'"
    ).fetchone()[0]
    if h09_study_count or h09_accepted_count:
        raise ValueError("H09 entered the scientific pilot or accepted funded counts")
    finding_range = connection.execute(
        "SELECT min(n), max(n) FROM (SELECT study_id, count(*) AS n FROM finding GROUP BY study_id)"
    ).fetchone()
    if finding_range[0] == finding_range[1]:
        raise ValueError("Finding counts are fixed instead of study-dependent")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=SCRIPT_DIR / "ontology-pilot.sqlite")
    args = parser.parse_args()
    output_path = args.db.resolve()
    if output_path.suffix != ".sqlite":
        raise ValueError("Database output must use the .sqlite suffix")
    if REPO_ROOT not in output_path.parents:
        raise ValueError("Database output must remain inside the repository")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists():
        output_path.unlink()

    rows = read_pilot_set()
    verify_inputs(rows)
    connection = sqlite3.connect(output_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript((SCRIPT_DIR / "schema.sql").read_text(encoding="utf-8"))
        for row in rows.values():
            parsed = parse_jats(REPO_ROOT / row["xml_path"])
            if parsed["publication"]["doi"] != row["doi"].lower():
                raise ValueError(f"{row['record_id']}: DOI mismatch")
            insert_metadata(connection, parsed)
        load_projects(connection, rows)
        load_semantic(connection, REPO_ROOT, rows)
        checks = validate_database(connection)
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
