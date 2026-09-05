#!/usr/bin/env python3
"""Build the public EQ-Graph SQLite database from the audited graph database."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import tempfile
from pathlib import Path
from typing import Any, Iterable


SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
) STRICT;

CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    abstract TEXT,
    principal_investigator TEXT,
    working_group TEXT,
    start_year INTEGER,
    end_year INTEGER,
    status TEXT,
    approved_budget_eur REAL
) STRICT;

CREATE TABLE publications (
    publication_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    doi TEXT,
    pmid TEXT,
    pmcid TEXT,
    publication_year INTEGER,
    publication_date TEXT,
    journal TEXT,
    publisher TEXT,
    volume TEXT,
    issue TEXT,
    article_number TEXT,
    article_type TEXT,
    language TEXT,
    keywords TEXT,
    funding_statement TEXT,
    abstract TEXT,
    canonical_url TEXT,
    licence_url TEXT,
    open_access INTEGER,
    assessment_disposition TEXT,
    euroqol_connection TEXT,
    euroqol_support TEXT,
    support_scope TEXT,
    full_text_format TEXT
) STRICT;

CREATE TABLE studies (
    study_id TEXT PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publications(publication_id),
    label TEXT NOT NULL,
    study_ordinal INTEGER,
    execution_status TEXT,
    source_status TEXT
) STRICT;

CREATE TABLE project_publications (
    project_id TEXT NOT NULL REFERENCES projects(project_id),
    publication_id TEXT NOT NULL REFERENCES publications(publication_id),
    project_output TEXT,
    support_target TEXT,
    support_scope TEXT,
    PRIMARY KEY (project_id, publication_id)
) STRICT;

CREATE TABLE people (
    person_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    family_name TEXT,
    given_names TEXT,
    orcid TEXT,
    openalex_id TEXT,
    entity_kind TEXT NOT NULL,
    identity_status TEXT NOT NULL
) STRICT;

CREATE TABLE person_names (
    person_id TEXT NOT NULL REFERENCES people(person_id),
    name TEXT NOT NULL,
    name_type TEXT NOT NULL,
    PRIMARY KEY (person_id, name, name_type)
) STRICT;

CREATE TABLE person_identifiers (
    person_id TEXT NOT NULL REFERENCES people(person_id),
    scheme TEXT NOT NULL,
    value TEXT NOT NULL,
    PRIMARY KEY (person_id, scheme, value),
    UNIQUE (scheme, value)
) STRICT;

CREATE TABLE euroqol_memberships (
    person_id TEXT PRIMARY KEY REFERENCES people(person_id),
    member_id TEXT NOT NULL UNIQUE,
    affiliation TEXT,
    profile_url TEXT,
    observed_date TEXT NOT NULL,
    status TEXT NOT NULL
) STRICT;

CREATE TABLE project_people (
    project_id TEXT NOT NULL REFERENCES projects(project_id),
    person_id TEXT NOT NULL REFERENCES people(person_id),
    role TEXT NOT NULL,
    PRIMARY KEY (project_id, person_id, role)
) STRICT;

CREATE TABLE publication_authors (
    publication_id TEXT NOT NULL REFERENCES publications(publication_id),
    person_id TEXT NOT NULL REFERENCES people(person_id),
    author_name TEXT NOT NULL,
    author_order INTEGER,
    corresponding INTEGER,
    orcid TEXT,
    resolution_method TEXT NOT NULL,
    resolution_status TEXT NOT NULL,
    PRIMARY KEY (publication_id, person_id)
) STRICT;

CREATE TABLE publication_citations (
    publication_id TEXT PRIMARY KEY REFERENCES publications(publication_id),
    source TEXT NOT NULL,
    source_work_id TEXT UNIQUE,
    cited_by_count INTEGER,
    retrieved_at TEXT NOT NULL,
    source_updated_at TEXT,
    match_status TEXT NOT NULL
) STRICT;

CREATE TABLE publication_citation_years (
    publication_id TEXT NOT NULL REFERENCES publication_citations(publication_id),
    source TEXT NOT NULL,
    year INTEGER NOT NULL,
    cited_by_count INTEGER NOT NULL,
    PRIMARY KEY (publication_id, source, year)
) STRICT;

CREATE TABLE author_affiliations (
    publication_id TEXT NOT NULL REFERENCES publications(publication_id),
    person_id TEXT NOT NULL,
    affiliation TEXT NOT NULL,
    PRIMARY KEY (publication_id, person_id, affiliation)
) STRICT;

CREATE TABLE study_types (
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    study_type TEXT NOT NULL,
    status TEXT,
    PRIMARY KEY (study_id, study_type)
) STRICT;

CREATE TABLE study_designs (
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    study_design TEXT NOT NULL,
    PRIMARY KEY (study_id, study_design)
) STRICT;

CREATE TABLE research_purposes (
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    purpose TEXT NOT NULL,
    PRIMARY KEY (study_id, purpose)
) STRICT;

CREATE TABLE populations (
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    population TEXT NOT NULL,
    role TEXT,
    geography TEXT,
    size TEXT,
    details_json TEXT NOT NULL DEFAULT '{}',
    PRIMARY KEY (study_id, population, role)
) STRICT;

CREATE TABLE samples (
    sample_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    label TEXT NOT NULL,
    sample_size INTEGER,
    role TEXT,
    geography TEXT,
    details_json TEXT NOT NULL DEFAULT '{}'
) STRICT;

CREATE TABLE study_countries (
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    country TEXT NOT NULL,
    PRIMARY KEY (study_id, country)
) STRICT;

CREATE TABLE instrument_uses (
    instrument_use_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    instrument TEXT NOT NULL,
    role TEXT,
    language TEXT,
    version TEXT,
    administration TEXT,
    respondent TEXT,
    perspective TEXT,
    recall_period TEXT,
    channel TEXT,
    setting TEXT,
    details_json TEXT NOT NULL DEFAULT '{}'
) STRICT;

CREATE TABLE method_uses (
    method_use_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    method TEXT NOT NULL,
    role TEXT,
    purpose TEXT,
    protocol TEXT,
    administration TEXT,
    software TEXT,
    details_json TEXT NOT NULL DEFAULT '{}'
) STRICT;

CREATE TABLE model_uses (
    model_use_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    model TEXT NOT NULL,
    role TEXT,
    outcome TEXT,
    inputs TEXT,
    software TEXT,
    details_json TEXT NOT NULL DEFAULT '{}'
) STRICT;

CREATE TABLE concepts (
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    concept TEXT NOT NULL,
    PRIMARY KEY (study_id, concept)
) STRICT;

CREATE TABLE outcomes (
    outcome_id TEXT NOT NULL,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    outcome TEXT NOT NULL,
    PRIMARY KEY (study_id, outcome_id)
) STRICT;

CREATE TABLE findings (
    finding_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    publication_id TEXT NOT NULL REFERENCES publications(publication_id),
    statement TEXT NOT NULL,
    outcome TEXT,
    details_json TEXT NOT NULL DEFAULT '{}'
) STRICT;

CREATE TABLE limitations (
    limitation_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    publication_id TEXT NOT NULL REFERENCES publications(publication_id),
    statement TEXT NOT NULL,
    impact TEXT,
    scope TEXT,
    details_json TEXT NOT NULL DEFAULT '{}'
) STRICT;

CREATE TABLE research_products (
    product_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    product TEXT NOT NULL,
    product_type TEXT,
    status TEXT,
    details_json TEXT NOT NULL DEFAULT '{}'
) STRICT;

CREATE TABLE dataset_uses (
    dataset_use_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    dataset TEXT NOT NULL,
    role TEXT,
    details_json TEXT NOT NULL DEFAULT '{}'
) STRICT;

CREATE TABLE protocols (
    protocol_id TEXT NOT NULL,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    protocol TEXT NOT NULL,
    details_json TEXT NOT NULL DEFAULT '{}',
    PRIMARY KEY (study_id, protocol_id)
) STRICT;

CREATE TABLE source_conflicts (
    conflict_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    statement TEXT NOT NULL,
    details_json TEXT NOT NULL DEFAULT '{}'
) STRICT;

CREATE INDEX publications_year_index ON publications(publication_year);
CREATE INDEX studies_publication_index ON studies(publication_id);
CREATE INDEX project_publications_publication_index ON project_publications(publication_id);
CREATE INDEX publication_authors_name_index ON publication_authors(author_name);
CREATE INDEX publication_authors_person_index ON publication_authors(person_id);
CREATE INDEX person_names_name_index ON person_names(name);
CREATE INDEX project_people_person_index ON project_people(person_id);
CREATE INDEX publication_citations_count_index ON publication_citations(cited_by_count);
CREATE INDEX study_types_type_index ON study_types(study_type);
CREATE INDEX study_countries_country_index ON study_countries(country);
CREATE INDEX instrument_uses_instrument_index ON instrument_uses(instrument);
CREATE INDEX method_uses_method_index ON method_uses(method);
CREATE INDEX model_uses_model_index ON model_uses(model);
CREATE INDEX concepts_concept_index ON concepts(concept);
CREATE INDEX findings_publication_index ON findings(publication_id);
CREATE INDEX findings_study_index ON findings(study_id);
CREATE INDEX limitations_publication_index ON limitations(publication_id);
"""


BLOCKED_PROPERTY_KEYS = {
    "citationtext",
    "counterevidence",
    "evidence",
    "papersources",
    "projectsources",
    "recordpath",
    "sourcelocator",
    "sourcepath",
    "sourcesha256",
}


COUNTRY_PATTERNS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("Australia", (r"\bAustralia\b",)),
    ("Belgium", (r"\bBelgium\b",)),
    ("Brazil", (r"\bBrazil\b",)),
    ("Canada", (r"\bCanada\b",)),
    ("China", (r"\bChina\b", r"\bFuzhou\b", r"\bShanghai\b")),
    ("Denmark", (r"\bDenmark\b", r"\bDanish\b")),
    ("Egypt", (r"\bEgypt\b",)),
    ("Estonia", (r"\bEstonia\b",)),
    ("Ethiopia", (r"\bEthiopia\b",)),
    ("France", (r"\bFrance\b",)),
    ("Germany", (r"\bGermany\b",)),
    ("Hungary", (r"\bHungary\b",)),
    ("Indonesia", (r"\bIndonesia\b", r"\bJava\b")),
    ("Italy", (r"\bItaly\b",)),
    ("Japan", (r"\bJapan\b",)),
    ("Malawi", (r"\bMalawi\b", r"\bBlantyre\b")),
    ("Malaysia", (r"\bMalaysia\b",)),
    ("Morocco", (r"\bMorocco\b", r"\bMoroccan\b")),
    ("Netherlands", (r"\bNetherlands\b", r"\bDutch\b")),
    ("Norway", (r"\bNorway\b",)),
    ("Pakistan", (r"\bPakistan\b",)),
    ("Philippines", (r"\bPhilippines\b",)),
    ("Poland", (r"\bPoland\b",)),
    ("Romania", (r"\bRomania\b",)),
    ("Singapore", (r"\bSingapore\b",)),
    ("Slovenia", (r"\bSlovenia\b",)),
    ("South Africa", (r"\bSouth Africa\b", r"\bCape Town\b")),
    ("South Korea", (r"\bSouth Korea\b", r"\bRepublic of Korea\b", r"\bKorea\b")),
    ("Spain", (r"\bSpain\b",)),
    ("Sweden", (r"\bSweden\b", r"\bSwedish\b", r"\bScania\b")),
    ("Taiwan", (r"\bTaiwan\b",)),
    ("Thailand", (r"\bThailand\b",)),
    ("United Kingdom", (r"\bUnited Kingdom\b", r"\bUK\b", r"\bU\.K\.\b", r"\bEngland\b", r"\bScotland\b", r"\bWales\b")),
    ("United States", (r"\bUnited States\b", r"\bUSA\b", r"\bU\.S\.A?\.?\b")),
    ("Vietnam", (r"\bVietnam\b",)),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(value: str | None) -> dict[str, Any]:
    if not value:
        return {}
    data = json.loads(value)
    return data if isinstance(data, dict) else {}


def text_value(value: Any) -> str | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, list):
        values = [text_value(item) for item in value]
        return "; ".join(item for item in values if item) or None
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return str(value)


def integer_value(value: Any) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        match = re.fullmatch(r"\s*(\d[\d,]*)\s*", value)
        if match:
            return int(match.group(1).replace(",", ""))
    return None


def pick(properties: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = text_value(properties.get(key))
        if value:
            return value
    return None


def safe_properties(properties: dict[str, Any], excluded: Iterable[str] = ()) -> str:
    excluded_keys = {key.casefold() for key in excluded}
    clean: dict[str, Any] = {}
    for key, value in properties.items():
        folded = key.casefold().replace("_", "")
        if key.casefold() in excluded_keys:
            continue
        if folded in BLOCKED_PROPERTY_KEYS:
            continue
        clean[key] = value
    return json.dumps(clean, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def publication_date(properties: dict[str, Any]) -> tuple[str | None, int | None]:
    dates = properties.get("dates")
    values: list[tuple[str, str]] = []
    if isinstance(dates, list):
        for item in dates:
            if not isinstance(item, dict):
                continue
            value = text_value(item.get("value"))
            kind = text_value(item.get("type")) or ""
            if value:
                values.append((kind.casefold(), value))
    priorities = ("epub", "publication", "ppub", "published", "pmc-release")
    selected = next((value for kind in priorities for item_kind, value in values if item_kind == kind), None)
    if selected is None and values:
        selected = values[0][1]
    match = re.search(r"(?:19|20)\d{2}", selected or "")
    return selected, int(match.group()) if match else None


def publication_funding(properties: dict[str, Any]) -> str | None:
    funding = properties.get("funding")
    if not isinstance(funding, list):
        return None
    statements: list[str] = []
    for item in funding:
        if not isinstance(item, dict):
            continue
        parts = [
            text_value(item.get("funder")),
            text_value(item.get("award_id")),
            text_value(item.get("recipient")),
            text_value(item.get("source_text")),
        ]
        statement = "; ".join(dict.fromkeys(part for part in parts if part))
        if statement:
            statements.append(statement)
    return " | ".join(dict.fromkeys(statements)) or None


def countries_from(*values: Any) -> set[str]:
    source = " ; ".join(value for item in values if (value := text_value(item)))
    output: set[str] = set()
    for country, patterns in COUNTRY_PATTERNS:
        if any(re.search(pattern, source, re.IGNORECASE) for pattern in patterns):
            output.add(country)
    return output


def rows(connection: sqlite3.Connection, sql: str, parameters: tuple[Any, ...] = ()) -> list[sqlite3.Row]:
    return list(connection.execute(sql, parameters))


def edge_targets(connection: sqlite3.Connection, edge_type: str) -> list[sqlite3.Row]:
    return rows(
        connection,
        """
        SELECT source.node_id AS source_id,
               target.node_id AS target_id,
               target.preferred_label AS target_label,
               target.properties_json AS target_properties,
               edge.properties_json AS edge_properties,
               edge.record_id AS record_id
        FROM graph_edge AS edge
        JOIN graph_node AS source ON source.node_id = edge.source_node_id
        JOIN graph_node AS target ON target.node_id = edge.target_node_id
        WHERE source.node_type = 'Study' AND edge.edge_type = ?
        ORDER BY source.node_id, target.node_id
        """,
        (edge_type,),
    )


def build(source: Path, output: Path) -> dict[str, int]:
    if not source.is_file():
        raise SystemExit(f"Source database does not exist: {source}")
    output.parent.mkdir(parents=True, exist_ok=True)

    source_uri = f"file:{source.resolve()}?mode=ro"
    source_db = sqlite3.connect(source_uri, uri=True)
    source_db.row_factory = sqlite3.Row
    source_db.execute("PRAGMA query_only = ON")

    handle, temporary_name = tempfile.mkstemp(prefix=f".{output.name}.", suffix=".tmp", dir=output.parent)
    os.close(handle)
    temporary = Path(temporary_name)
    try:
        target = sqlite3.connect(temporary)
        target.execute("PRAGMA foreign_keys = ON")
        target.executescript(SCHEMA)
        target.execute("BEGIN")

        source_digest = sha256(source)
        target.executemany(
            "INSERT INTO metadata(key,value) VALUES (?,?)",
            (
                ("dataset", "EQ-Graph public research serving database"),
                ("scope", "1024 projects and the assessed 209-publication evidence corpus"),
                ("source_database_sha256", source_digest),
                ("project_link_policy", "accepted links only"),
                ("citation_policy", "citations are not included in this serving database"),
                ("full_text_policy", "full text remains outside the serving database"),
            ),
        )

        project_rows = rows(source_db, "SELECT node_id, preferred_label, properties_json FROM graph_node WHERE node_type='Project' ORDER BY node_id")
        for row in project_rows:
            props = load_json(row["properties_json"])
            target.execute(
                "INSERT INTO projects VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    pick(props, "projectId") or row["node_id"].removeprefix("project:"),
                    row["preferred_label"],
                    pick(props, "abstract"),
                    pick(props, "principalInvestigator"),
                    pick(props, "workingGroup"),
                    integer_value(props.get("startYear")),
                    integer_value(props.get("endYear")),
                    pick(props, "status"),
                    props.get("approvedBudgetEur") if isinstance(props.get("approvedBudgetEur"), (int, float)) else None,
                ),
            )

        publication_rows = rows(source_db, "SELECT node_id, preferred_label, properties_json FROM corpus_publication ORDER BY node_id")
        publication_ids: set[str] = set()
        for row in publication_rows:
            props = load_json(row["properties_json"])
            publication_id = pick(props, "publication_id") or row["node_id"].removeprefix("publication:")
            publication_ids.add(row["node_id"])
            assessment = props.get("assessment") if isinstance(props.get("assessment"), dict) else {}
            date, year = publication_date(props)
            source_path = pick(props, "source_path") or ""
            extension = Path(source_path).suffix.removeprefix(".").upper() or None
            target.execute(
                "INSERT INTO publications VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    publication_id,
                    row["preferred_label"],
                    pick(props, "doi"),
                    pick(props, "pmid"),
                    pick(props, "pmcid"),
                    year,
                    date,
                    pick(props, "journal"),
                    pick(props, "publisher"),
                    pick(props, "volume"),
                    pick(props, "issue"),
                    pick(props, "article_number"),
                    pick(props, "article_type"),
                    pick(props, "language"),
                    text_value(props.get("keywords")),
                    publication_funding(props),
                    pick(props, "abstract"),
                    pick(props, "canonical_url"),
                    pick(props, "licence_url"),
                    int(bool(props.get("open_access"))) if props.get("open_access") is not None else None,
                    pick(assessment, "disposition"),
                    pick(assessment, "connection"),
                    pick(assessment, "euroqol-support"),
                    pick(assessment, "support-scope"),
                    extension,
                ),
            )

        study_to_publication: dict[str, str] = {}
        for row in rows(
            source_db,
            """
            SELECT publication.node_id AS publication_node_id,
                   study.node_id AS study_id,
                   study.preferred_label AS label,
                   study.properties_json AS properties_json
            FROM graph_edge AS edge
            JOIN graph_node AS publication ON publication.node_id=edge.source_node_id
            JOIN graph_node AS study ON study.node_id=edge.target_node_id
            WHERE edge.edge_type='REPORTS_STUDY' AND publication.node_id IN (SELECT node_id FROM corpus_publication)
            ORDER BY publication.node_id, study.node_id
            """,
        ):
            props = load_json(row["properties_json"])
            publication_id = row["publication_node_id"].removeprefix("publication:")
            study_to_publication[row["study_id"]] = publication_id
            target.execute(
                "INSERT INTO studies VALUES (?,?,?,?,?,?)",
                (
                    row["study_id"], publication_id, row["label"],
                    integer_value(props.get("studyOrdinal")), pick(props, "executionStatus"), pick(props, "sourceStatus"),
                ),
            )

        for row in rows(
            source_db,
            """
            SELECT project.preferred_label AS project_label,
                   project.properties_json AS project_properties,
                   publication.node_id AS publication_node_id,
                   assessment.properties_json AS assessment_properties
            FROM graph_node AS project
            JOIN graph_edge AS has_assessment
              ON has_assessment.source_node_id=project.node_id AND has_assessment.edge_type='HAS_LINK_ASSESSMENT'
            JOIN graph_node AS assessment ON assessment.node_id=has_assessment.target_node_id
            JOIN graph_edge AS assesses
              ON assesses.source_node_id=assessment.node_id AND assesses.edge_type='ASSESSES_PUBLICATION'
            JOIN graph_node AS publication ON publication.node_id=assesses.target_node_id
            WHERE project.node_type='Project'
              AND json_extract(assessment.properties_json,'$.connectionStatus')='accepted'
              AND publication.node_id IN (SELECT node_id FROM corpus_publication)
            ORDER BY project.node_id, publication.node_id
            """,
        ):
            project_props = load_json(row["project_properties"])
            props = load_json(row["assessment_properties"])
            target.execute(
                "INSERT INTO project_publications VALUES (?,?,?,?,?)",
                (
                    pick(project_props, "projectId"),
                    row["publication_node_id"].removeprefix("publication:"),
                    pick(props, "projectOutput"),
                    pick(props, "supportTarget"),
                    pick(props, "supportScope"),
                ),
            )

        for row in rows(
            source_db,
            """
            SELECT publication.node_id AS publication_node_id,
                   person.node_id AS person_id,
                   person.preferred_label AS person_name,
                   person.properties_json AS person_properties,
                   authored.properties_json AS authored_properties
            FROM graph_edge AS authored
            JOIN graph_node AS person ON person.node_id=authored.source_node_id
            JOIN graph_node AS publication ON publication.node_id=authored.target_node_id
            WHERE authored.edge_type='AUTHORED'
              AND publication.node_id IN (SELECT node_id FROM corpus_publication)
            ORDER BY publication.node_id, CAST(json_extract(authored.properties_json,'$.authorOrder') AS INTEGER), person.node_id
            """,
        ):
            person = load_json(row["person_properties"])
            edge = load_json(row["authored_properties"])
            target.execute(
                "INSERT OR IGNORE INTO people VALUES (?,?,?,?,?,?,?,?)",
                (
                    row["person_id"], row["person_name"], pick(person, "familyName"),
                    pick(person, "givenNames"), pick(person, "orcid"),
                    pick(person, "openalexId"), "PERSON", "LEGACY_GRAPH_ID",
                ),
            )
            target.execute(
                "INSERT OR IGNORE INTO person_names VALUES (?,?,?)",
                (row["person_id"], row["person_name"], "LEGACY_GRAPH_NAME"),
            )
            target.execute(
                "INSERT OR IGNORE INTO publication_authors VALUES (?,?,?,?,?,?,?,?)",
                (
                    row["publication_node_id"].removeprefix("publication:"), row["person_id"], row["person_name"],
                    integer_value(edge.get("authorOrder")), int(bool(edge.get("corresponding"))), pick(person, "orcid"),
                    "LEGACY_GRAPH_ID", "ACCEPTED",
                ),
            )

        for row in rows(
            source_db,
            """
            SELECT publication.node_id AS publication_node_id,
                   person.node_id AS person_id,
                   affiliation.preferred_label AS affiliation
            FROM graph_edge AS authored
            JOIN graph_node AS person ON person.node_id=authored.source_node_id
            JOIN graph_node AS publication ON publication.node_id=authored.target_node_id
            JOIN graph_edge AS affiliated
              ON affiliated.source_node_id=person.node_id
             AND affiliated.edge_type='AFFILIATED_WITH'
             AND affiliated.record_id=authored.record_id
            JOIN graph_node AS affiliation ON affiliation.node_id=affiliated.target_node_id
            WHERE authored.edge_type='AUTHORED'
              AND publication.node_id IN (SELECT node_id FROM corpus_publication)
            ORDER BY publication.node_id, person.node_id, affiliation.preferred_label
            """,
        ):
            target.execute(
                "INSERT OR IGNORE INTO author_affiliations VALUES (?,?,?)",
                (row["publication_node_id"].removeprefix("publication:"), row["person_id"], row["affiliation"]),
            )

        simple_edges = (
            ("HAS_STUDY_TYPE", "study_types", "study_type", ("status",)),
            ("HAS_DESIGN", "study_designs", "study_design", ()),
            ("HAS_PURPOSE", "research_purposes", "purpose", ()),
            ("CONCERNS", "concepts", "concept", ()),
        )
        for edge_type, table, label_column, extra_columns in simple_edges:
            for row in edge_targets(source_db, edge_type):
                if row["source_id"] not in study_to_publication:
                    continue
                props = {**load_json(row["target_properties"]), **load_json(row["edge_properties"])}
                columns = ["study_id", label_column, *extra_columns]
                values: list[Any] = [row["source_id"], row["target_label"]]
                values.extend(pick(props, column) for column in extra_columns)
                target.execute(
                    f"INSERT OR IGNORE INTO {table} ({','.join(columns)}) VALUES ({','.join('?' for _ in values)})",
                    values,
                )

        geography_by_study: dict[str, list[Any]] = {study_id: [] for study_id in study_to_publication}
        for row in edge_targets(source_db, "STUDIES_POPULATION"):
            if row["source_id"] not in study_to_publication:
                continue
            props = {**load_json(row["target_properties"]), **load_json(row["edge_properties"])}
            geography = pick(props, "geography", "countries")
            geography_by_study[row["source_id"]].extend((geography, props.get("countries"), row["target_label"]))
            target.execute(
                "INSERT OR IGNORE INTO populations VALUES (?,?,?,?,?,?)",
                (
                    row["source_id"], row["target_label"], pick(props, "role"), geography,
                    pick(props, "size", "n", "sample size"), safe_properties(props, ("role", "geography", "countries", "size", "n", "sample size")),
                ),
            )

        for row in edge_targets(source_db, "HAS_SAMPLE"):
            if row["source_id"] not in study_to_publication:
                continue
            props = {**load_json(row["target_properties"]), **load_json(row["edge_properties"])}
            geography = pick(props, "geography", "countries")
            geography_by_study[row["source_id"]].extend((geography, props.get("countries"), row["target_label"]))
            target.execute(
                "INSERT INTO samples VALUES (?,?,?,?,?,?,?)",
                (
                    row["target_id"], row["source_id"], row["target_label"],
                    integer_value(props.get("size")) or integer_value(props.get("n")) or integer_value(props.get("N")) or integer_value(props.get("total")),
                    pick(props, "role"), geography,
                    safe_properties(props, ("size", "n", "N", "total", "role", "geography", "countries")),
                ),
            )

        for study_id, values in geography_by_study.items():
            for country in sorted(countries_from(*values)):
                target.execute("INSERT INTO study_countries VALUES (?,?)", (study_id, country))

        for row in edge_targets(source_db, "USES_INSTRUMENT"):
            if row["source_id"] not in study_to_publication:
                continue
            instrument_row = source_db.execute(
                """
                SELECT instrument.preferred_label
                FROM graph_edge AS edge JOIN graph_node AS instrument ON instrument.node_id=edge.target_node_id
                WHERE edge.source_node_id=? AND edge.edge_type='OF_INSTRUMENT'
                ORDER BY instrument.node_id LIMIT 1
                """,
                (row["target_id"],),
            ).fetchone()
            props = {**load_json(row["target_properties"]), **load_json(row["edge_properties"])}
            instrument = instrument_row[0] if instrument_row else row["target_label"]
            excluded = ("role", "language", "version", "administration", "respondent", "perspective", "recall", "recall period", "recall_period", "channel", "setting")
            target.execute(
                "INSERT INTO instrument_uses VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    row["target_id"], row["source_id"], instrument, pick(props, "role"), pick(props, "language"),
                    pick(props, "version"), pick(props, "administration", "administration details"), pick(props, "respondent", "assessor"),
                    pick(props, "perspective"), pick(props, "recall period", "recall_period", "recall"), pick(props, "channel", "format"),
                    pick(props, "setting"), safe_properties(props, excluded),
                ),
            )

        for row in edge_targets(source_db, "USES_METHOD"):
            if row["source_id"] not in study_to_publication:
                continue
            method_row = source_db.execute(
                """
                SELECT method.preferred_label
                FROM graph_edge AS edge JOIN graph_node AS method ON method.node_id=edge.target_node_id
                WHERE edge.source_node_id=? AND edge.edge_type='OF_METHOD'
                ORDER BY method.node_id LIMIT 1
                """,
                (row["target_id"],),
            ).fetchone()
            props = {**load_json(row["target_properties"]), **load_json(row["edge_properties"])}
            method = method_row[0] if method_row else row["target_label"]
            excluded = ("role", "purpose", "protocol", "administration", "software")
            target.execute(
                "INSERT INTO method_uses VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    row["target_id"], row["source_id"], method, pick(props, "role"), pick(props, "purpose", "criterion", "output"),
                    pick(props, "protocol"), pick(props, "administration", "channel"), pick(props, "software", "package"),
                    safe_properties(props, excluded),
                ),
            )

        for row in edge_targets(source_db, "ANALYZED_WITH"):
            if row["source_id"] not in study_to_publication:
                continue
            model_row = source_db.execute(
                """
                SELECT model.preferred_label
                FROM graph_edge AS edge JOIN graph_node AS model ON model.node_id=edge.target_node_id
                WHERE edge.source_node_id=? AND edge.edge_type='OF_MODEL'
                ORDER BY model.node_id LIMIT 1
                """,
                (row["target_id"],),
            ).fetchone()
            props = {**load_json(row["target_properties"]), **load_json(row["edge_properties"])}
            model = model_row[0] if model_row else row["target_label"]
            excluded = ("role", "outcome", "outcomes", "inputs", "input", "software")
            target.execute(
                "INSERT INTO model_uses VALUES (?,?,?,?,?,?,?,?)",
                (
                    row["target_id"], row["source_id"], model, pick(props, "role"), pick(props, "outcome", "outcomes"),
                    pick(props, "inputs", "input", "predictors"), pick(props, "software"), safe_properties(props, excluded),
                ),
            )

        for row in edge_targets(source_db, "MEASURES_OUTCOME"):
            if row["source_id"] in study_to_publication:
                target.execute("INSERT OR IGNORE INTO outcomes VALUES (?,?,?)", (row["target_id"], row["source_id"], row["target_label"]))

        for edge_type, table, id_column, label_column in (
            ("REPORTS_FINDING", "findings", "finding_id", "statement"),
            ("HAS_LIMITATION", "limitations", "limitation_id", "statement"),
        ):
            for row in edge_targets(source_db, edge_type):
                if row["source_id"] not in study_to_publication:
                    continue
                props = {**load_json(row["target_properties"]), **load_json(row["edge_properties"])}
                publication_id = study_to_publication[row["source_id"]]
                if table == "findings":
                    target.execute(
                        "INSERT INTO findings VALUES (?,?,?,?,?,?)",
                        (
                            row["target_id"], row["source_id"], publication_id, row["target_label"], pick(props, "outcome", "outcomes"),
                            safe_properties(props, ("outcome", "outcomes")),
                        ),
                    )
                else:
                    target.execute(
                        "INSERT INTO limitations VALUES (?,?,?,?,?,?,?)",
                        (
                            row["target_id"], row["source_id"], publication_id, row["target_label"], pick(props, "impact", "consequence"),
                            pick(props, "scope"), safe_properties(props, ("impact", "consequence", "scope")),
                        ),
                    )

        for edge_type, table in (
            ("PRODUCES", "research_products"),
            ("USES_DATA", "dataset_uses"),
            ("FOLLOWS_PROTOCOL", "protocols"),
            ("HAS_SOURCE_CONFLICT", "source_conflicts"),
        ):
            for row in edge_targets(source_db, edge_type):
                if row["source_id"] not in study_to_publication:
                    continue
                props = {**load_json(row["target_properties"]), **load_json(row["edge_properties"])}
                if table == "research_products":
                    target.execute(
                        "INSERT INTO research_products VALUES (?,?,?,?,?,?)",
                        (row["target_id"], row["source_id"], row["target_label"], pick(props, "type"), pick(props, "status"), safe_properties(props, ("type", "status"))),
                    )
                elif table == "dataset_uses":
                    target.execute(
                        "INSERT INTO dataset_uses VALUES (?,?,?,?,?)",
                        (row["target_id"], row["source_id"], row["target_label"], pick(props, "role"), safe_properties(props, ("role",))),
                    )
                elif table == "protocols":
                    target.execute(
                        "INSERT INTO protocols VALUES (?,?,?,?)",
                        (row["target_id"], row["source_id"], row["target_label"], safe_properties(props)),
                    )
                else:
                    target.execute(
                        "INSERT INTO source_conflicts VALUES (?,?,?,?)",
                        (row["target_id"], row["source_id"], row["target_label"], safe_properties(props)),
                    )

        counts = {
            table: target.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            for table in (
                "projects", "publications", "studies", "project_publications", "publication_authors",
                "study_types", "study_countries", "instrument_uses", "method_uses", "model_uses",
                "concepts", "outcomes", "findings", "limitations", "research_products",
            )
        }
        target.executemany(
            "INSERT INTO metadata(key,value) VALUES (?,?)",
            ((f"count_{key}", str(value)) for key, value in counts.items()),
        )
        target.commit()
        target.execute("PRAGMA optimize")
        target.execute("VACUUM")
        target.close()
        source_db.close()
        os.replace(temporary, output)
        return counts
    finally:
        source_db.close()
        if temporary.exists():
            temporary.unlink()


def main() -> None:
    args = parse_args()
    counts = build(args.source, args.output)
    print(json.dumps({"output": str(args.output), "sha256": sha256(args.output), "counts": counts}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
