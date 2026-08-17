#!/usr/bin/env python3
"""Load deterministic metadata and one-pass records into a small SQLite database."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import unicodedata
from pathlib import Path

from evaluate import CALIBRATION, extract_source_locator, first_class, parse_labels, VALID
from index_terms import parse_record


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalized_value(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).strip().rstrip(".")
    aliases = {
        "eq-vas": "EQ VAS",
        "eq vas": "EQ VAS",
        "eq-5d-5l vas": "EQ VAS",
        "eq-5d-5l visual analogue scale": "EQ VAS",
        "eq-5d visual analogue scale": "EQ VAS",
        "euroqol visual analogue scale": "EQ VAS",
        "composite time trade-off": "cTTO",
        "composite time tradeoff": "cTTO",
        "discrete choice experiment": "DCE",
        "discrete-choice experiment": "DCE",
        "eq-vt version 2.0": "EQ-VT 2.0",
        "eq-vt version 2.1": "EQ-VT 2.1",
        "eq-vt-2.0": "EQ-VT 2.0",
        "eq-vt-2.1": "EQ-VT 2.1",
    }
    return aliases.get(value.casefold(), value)


def normalized_type(term_type: str, value: str) -> str:
    lowered = value.casefold()
    if value == "DCE":
        return "Method"
    if value.startswith("EQ-VT "):
        return "Protocol"
    if term_type == "Method" and any(
        word in lowered
        for word in (
            "validity",
            "reliability",
            "responsiveness",
            "agreement",
        )
    ):
        return "Outcome"
    if term_type in {"Method", "Analysis"} and "regression" in lowered:
        return "Model"
    if term_type == "Method" and any(
        word in lowered
        for word in (
            "analysis",
            "correlation",
            "bootstrap",
            "anova",
            "mann-whitney",
            "kruskal-wallis",
        )
    ):
        return "Analysis"
    return term_type


def section_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", text, flags=re.MULTILINE))
    blocks: list[tuple[str, str]] = []
    for position, match in enumerate(matches):
        start = match.end()
        end = matches[position + 1].start() if position + 1 < len(matches) else len(text)
        blocks.append((match.group(1).strip(), text[start:end].strip()))
    return blocks


def bullet_blocks(content: str) -> list[tuple[str, str | None]]:
    bullets: list[str] = []
    current = ""
    for raw in content.splitlines():
        if re.match(r"^\s*-\s+", raw):
            if current:
                bullets.append(current)
            current = re.sub(r"^\s*-\s+", "", raw).strip()
        elif current and raw.strip():
            current += " " + raw.strip()
    if current:
        bullets.append(current)
    output: list[tuple[str, str | None]] = []
    for bullet in bullets:
        output.append((bullet, extract_source_locator(bullet)))
    return output


SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE publication (
    record_id TEXT PRIMARY KEY,
    publication_id TEXT NOT NULL,
    doi TEXT NOT NULL UNIQUE,
    pmid TEXT,
    pmcid TEXT,
    title TEXT NOT NULL,
    abstract TEXT,
    journal TEXT,
    publisher TEXT,
    article_type TEXT,
    language TEXT,
    volume TEXT,
    issue TEXT,
    article_number TEXT,
    licence_url TEXT,
    open_access INTEGER,
    canonical_url TEXT,
    article_path TEXT NOT NULL,
    article_sha256 TEXT NOT NULL,
    xml_path TEXT NOT NULL,
    xml_sha256 TEXT NOT NULL,
    metadata_json TEXT NOT NULL
) STRICT;
CREATE TABLE author (
    author_id TEXT PRIMARY KEY,
    orcid TEXT,
    given_names TEXT,
    family_name TEXT,
    collective_name TEXT
) STRICT;
CREATE TABLE publication_author (
    record_id TEXT NOT NULL REFERENCES publication(record_id),
    author_id TEXT NOT NULL REFERENCES author(author_id),
    author_order INTEGER NOT NULL,
    corresponding INTEGER,
    PRIMARY KEY (record_id, author_order)
) STRICT;
CREATE TABLE affiliation (
    affiliation_id TEXT PRIMARY KEY,
    record_id TEXT NOT NULL REFERENCES publication(record_id),
    source_id TEXT,
    text TEXT NOT NULL
) STRICT;
CREATE TABLE publication_funding (
    funding_id INTEGER PRIMARY KEY,
    record_id TEXT NOT NULL REFERENCES publication(record_id),
    funder TEXT,
    award_id TEXT,
    recipient TEXT,
    source_text TEXT,
    source_locator TEXT
) STRICT;
CREATE TABLE publication_keyword (
    record_id TEXT NOT NULL REFERENCES publication(record_id),
    keyword TEXT NOT NULL,
    PRIMARY KEY (record_id, keyword)
) STRICT;
CREATE TABLE project_candidate (
    record_id TEXT NOT NULL REFERENCES publication(record_id),
    project_id TEXT NOT NULL,
    PRIMARY KEY (record_id, project_id)
) STRICT;
CREATE TABLE extraction_record (
    record_id TEXT PRIMARY KEY REFERENCES publication(record_id),
    disposition TEXT NOT NULL,
    connection TEXT NOT NULL,
    euroqol_support TEXT NOT NULL,
    support_scope TEXT NOT NULL,
    project_link TEXT NOT NULL,
    publication_status TEXT NOT NULL,
    evidence TEXT NOT NULL,
    markdown TEXT NOT NULL
) STRICT;
CREATE TABLE record_section (
    record_id TEXT NOT NULL REFERENCES extraction_record(record_id),
    section_order INTEGER NOT NULL,
    heading TEXT NOT NULL,
    content TEXT NOT NULL,
    PRIMARY KEY (record_id, section_order)
) STRICT;
CREATE TABLE record_fact (
    record_id TEXT NOT NULL REFERENCES extraction_record(record_id),
    section_order INTEGER NOT NULL,
    fact_order INTEGER NOT NULL,
    heading TEXT NOT NULL,
    text TEXT NOT NULL,
    source_locator TEXT,
    PRIMARY KEY (record_id, section_order, fact_order)
) STRICT;
CREATE TABLE term (
    term_id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    normalized_value TEXT NOT NULL,
    UNIQUE (type, normalized_value)
) STRICT;
CREATE TABLE record_term (
    record_id TEXT NOT NULL REFERENCES extraction_record(record_id),
    term_id INTEGER NOT NULL REFERENCES term(term_id),
    source_value TEXT NOT NULL,
    PRIMARY KEY (record_id, term_id)
) STRICT;
CREATE VIRTUAL TABLE record_fts USING fts5(
    record_id UNINDEXED,
    title,
    abstract,
    markdown,
    index_terms
);
CREATE INDEX publication_doi_index ON publication(doi);
CREATE INDEX term_type_value_index ON term(type, normalized_value);
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--overlay-run", action="append", default=[])
    parser.add_argument("--append", action="store_true")
    parser.add_argument("--record-prefix", default="")
    args = parser.parse_args()
    manifest_path = (CALIBRATION / args.manifest).resolve()
    output_path = (CALIBRATION / args.output).resolve()
    if CALIBRATION.resolve() not in manifest_path.parents:
        raise ValueError("manifest must be inside the calibration directory")
    if CALIBRATION.resolve() not in output_path.parents:
        raise ValueError("output must be inside the calibration directory")
    if output_path.exists() and not args.append:
        raise FileExistsError(output_path)
    if args.append and not output_path.exists():
        raise FileNotFoundError(output_path)
    if not re.fullmatch(r"[A-Za-z0-9_-]*", args.record_prefix):
        raise ValueError("record prefix can contain only letters, numbers, underscore, and hyphen")

    run_dir = CALIBRATION / args.run
    overlay_dirs = [CALIBRATION / value for value in args.overlay_run]
    connection = sqlite3.connect(output_path)
    if not args.append:
        connection.executescript(SCHEMA)
    loaded = 0
    with connection:
        for item in read_manifest(manifest_path):
            source_record_id = item["record_id"]
            record_id = f"{args.record_prefix}{source_record_id}"
            record_path = run_dir / "records" / f"{source_record_id}.md"
            for overlay_dir in overlay_dirs:
                candidate = overlay_dir / "records" / f"{source_record_id}.md"
                if candidate.is_file():
                    record_path = candidate
            if not record_path.is_file():
                raise FileNotFoundError(record_path)
            metadata_path = CALIBRATION.parents[2] / item["metadata_path"]
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            publication = metadata["publication"]
            connection.execute(
                "INSERT INTO publication VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    record_id,
                    publication["publication_id"],
                    publication["doi"],
                    publication.get("pmid"),
                    publication.get("pmcid"),
                    publication["title"],
                    publication.get("abstract"),
                    publication.get("journal"),
                    publication.get("publisher"),
                    publication.get("article_type"),
                    publication.get("language"),
                    publication.get("volume"),
                    publication.get("issue"),
                    publication.get("article_number"),
                    publication.get("licence_url"),
                    publication.get("open_access"),
                    publication.get("canonical_url"),
                    item["article_path"],
                    item["article_sha256"],
                    item["xml_path"],
                    item["xml_sha256"],
                    json.dumps(metadata, ensure_ascii=False),
                ),
            )
            for order, author in enumerate(metadata.get("authors", []), 1):
                author_id = f"{record_id}:author:{order}"
                connection.execute(
                    "INSERT INTO author VALUES (?,?,?,?,?)",
                    (
                        author_id,
                        author.get("orcid"),
                        author.get("given_names"),
                        author.get("family_name"),
                        author.get("collective_name"),
                    ),
                )
                connection.execute(
                    "INSERT INTO publication_author VALUES (?,?,?,?)",
                    (record_id, author_id, order, int(bool(author.get("corresponding")))),
                )
            for order, affiliation in enumerate(metadata.get("affiliations", []), 1):
                connection.execute(
                    "INSERT INTO affiliation VALUES (?,?,?,?)",
                    (
                        f"{record_id}:affiliation:{order}",
                        record_id,
                        affiliation.get("id"),
                        affiliation["name"],
                    ),
                )
            for funding in metadata.get("funding", []):
                connection.execute(
                    "INSERT INTO publication_funding "
                    "(record_id,funder,award_id,recipient,source_text,source_locator) VALUES (?,?,?,?,?,?)",
                    (
                        record_id,
                        funding.get("funder"),
                        funding.get("award_id"),
                        funding.get("recipient"),
                        funding.get("source_text"),
                        funding.get("source_locator"),
                    ),
                )
            for keyword in metadata.get("keywords", []):
                connection.execute(
                    "INSERT OR IGNORE INTO publication_keyword VALUES (?,?)", (record_id, keyword)
                )
            for project_id in item["candidate_project_ids"].split(";"):
                if project_id:
                    connection.execute(
                        "INSERT INTO project_candidate VALUES (?,?)", (record_id, project_id)
                    )

            text = record_path.read_text(encoding="utf-8")
            labels = parse_labels(text)
            classes = {key: first_class(labels.get(key, ""), allowed) for key, allowed in VALID.items()}
            connection.execute(
                "INSERT INTO extraction_record VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    record_id,
                    classes["disposition"],
                    classes["connection"],
                    classes["euroqol support"],
                    labels["support scope"],
                    classes["project link"],
                    labels["publication status"],
                    labels["evidence"],
                    text,
                ),
            )
            for order, (heading, content) in enumerate(section_blocks(text), 1):
                connection.execute(
                    "INSERT INTO record_section VALUES (?,?,?,?)",
                    (record_id, order, heading, content),
                )
                for fact_order, (fact, locator) in enumerate(bullet_blocks(content), 1):
                    connection.execute(
                        "INSERT INTO record_fact VALUES (?,?,?,?,?,?)",
                        (record_id, order, fact_order, heading, fact, locator),
                    )
            index_rows, errors = parse_record(record_path)
            if errors:
                raise ValueError("; ".join(errors))
            index_text: list[str] = []
            for row in index_rows:
                normalized = normalized_value(row["value"])
                term_type = normalized_type(row["type"], normalized)
                if term_type == "Outcome" and normalized == "EQ VAS":
                    normalized = "EQ VAS score"
                connection.execute(
                    "INSERT OR IGNORE INTO term (type,normalized_value) VALUES (?,?)",
                    (term_type, normalized),
                )
                term_id = connection.execute(
                    "SELECT term_id FROM term WHERE type=? AND normalized_value=?",
                    (term_type, normalized),
                ).fetchone()[0]
                connection.execute(
                    "INSERT OR IGNORE INTO record_term VALUES (?,?,?)",
                    (record_id, term_id, row["value"]),
                )
                index_text.append(f"{term_type}: {normalized}")
            connection.execute(
                "INSERT INTO record_fts VALUES (?,?,?,?,?)",
                (
                    record_id,
                    publication["title"],
                    publication.get("abstract") or "",
                    text,
                    "\n".join(index_text),
                ),
            )
            loaded += 1
    connection.execute("PRAGMA optimize")
    print(f"loaded={loaded}")
    print(f"terms={connection.execute('SELECT COUNT(*) FROM term').fetchone()[0]}")
    print(f"record_terms={connection.execute('SELECT COUNT(*) FROM record_term').fetchone()[0]}")
    print(f"output={output_path}")
    connection.close()


if __name__ == "__main__":
    main()
