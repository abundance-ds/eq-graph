#!/usr/bin/env python3
"""Check a typed EQ-Graph public serving database."""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
VOCABULARY = REPO / "pilot/ontology-development-v4/VOCABULARY.tsv"

FORBIDDEN_TEXT = (
    "/Users/",
    "/private/",
    "input/projects/",
    "pilot/ontology-development",
    "source_path",
    "record_path",
    ".xml",
    ".md",
)

REQUIRED_TABLES = {
    "projects",
    "publications",
    "studies",
    "project_publications",
    "people",
    "person_names",
    "project_people",
    "euroqol_memberships",
    "publication_authors",
    "publication_citations",
    "registry_entities",
    "study_types",
    "design_axes",
    "scientific_uses",
    "administrations",
    "task_designs",
    "outcomes",
    "findings",
    "finding_values",
    "interpretations",
    "limitations",
    "research_products",
    "product_uses",
    "extraction_gaps",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database", type=Path)
    parser.add_argument("--expect-projects", type=int)
    parser.add_argument("--expect-publications", type=int)
    parser.add_argument("--expect-pdf-publications", type=int)
    parser.add_argument("--expect-project-leaders", type=int)
    parser.add_argument("--expect-members", type=int)
    parser.add_argument("--expect-leaders-and-members", type=int)
    return parser.parse_args()


def scalar(connection: sqlite3.Connection, sql: str) -> int:
    return int(connection.execute(sql).fetchone()[0])


def controlled_values(key: str) -> set[str]:
    with VOCABULARY.open(encoding="utf-8", newline="") as handle:
        return {
            row["value"]
            for row in csv.DictReader(handle, delimiter="\t")
            if row["key"] == key
        }


def unexpected_values(
    connection: sqlite3.Connection,
    table: str,
    column: str,
    allowed: set[str],
) -> list[str]:
    return [
        str(row[0])
        for row in connection.execute(
            f"SELECT DISTINCT {column} FROM {table} ORDER BY {column}"
        )
        if row[0] not in allowed
    ]


def main() -> None:
    args = parse_args()
    uri = f"file:{args.database.resolve()}?mode=ro"
    connection = sqlite3.connect(uri, uri=True)
    connection.execute("PRAGMA query_only = ON")

    foreign_keys = connection.execute("PRAGMA foreign_key_check").fetchall()
    if foreign_keys:
        raise SystemExit(f"Foreign-key check failed: {foreign_keys[:5]}")
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    if integrity != "ok":
        raise SystemExit(f"Integrity check failed: {integrity}")

    tables = {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        )
    }
    missing = REQUIRED_TABLES - tables
    if missing:
        raise SystemExit(f"Required tables are missing: {sorted(missing)}")
    forbidden_tables = {"source_record", "item_source", "assessment_source"} & tables
    if forbidden_tables:
        raise SystemExit(f"Private tables are present: {sorted(forbidden_tables)}")

    counts = {
        table: scalar(connection, f"SELECT COUNT(*) FROM {table}")
        for table in (
            "projects",
            "publications",
            "studies",
            "project_publications",
            "people",
            "project_people",
            "euroqol_memberships",
            "publication_authors",
            "publication_citations",
            "scientific_uses",
            "findings",
            "limitations",
            "research_products",
        )
    }
    if args.expect_projects is not None and counts["projects"] != args.expect_projects:
        raise SystemExit(
            f"projects: expected {args.expect_projects}, found {counts['projects']}"
        )
    if (
        args.expect_publications is not None
        and counts["publications"] != args.expect_publications
    ):
        raise SystemExit(
            "publications: expected "
            f"{args.expect_publications}, found {counts['publications']}"
        )
    bad_formats = unexpected_values(
        connection,
        "publications",
        "full_text_format",
        {"JATS", "PDF"},
    )
    if bad_formats:
        raise SystemExit(f"Full-text formats are invalid: {bad_formats}")
    pdf_publications = scalar(
        connection,
        "SELECT COUNT(*) FROM publications WHERE full_text_format='PDF'",
    )
    if (
        args.expect_pdf_publications is not None
        and pdf_publications != args.expect_pdf_publications
    ):
        raise SystemExit(
            "PDF publications: expected "
            f"{args.expect_pdf_publications}, found {pdf_publications}"
        )
    if counts["studies"] < counts["publications"]:
        no_study_expected = scalar(
            connection,
            "SELECT COUNT(*) FROM publications WHERE assessment_disposition IN ('publication-context','exclude')",
        )
        if counts["studies"] + no_study_expected < counts["publications"]:
            raise SystemExit("One or more study publications have no Study.")
    project_leaders = scalar(
        connection,
        "SELECT COUNT(DISTINCT person_id) FROM project_people WHERE role='PRINCIPAL_INVESTIGATOR'",
    )
    members = counts["euroqol_memberships"]
    leaders_and_members = scalar(
        connection,
        """
        SELECT COUNT(DISTINCT pp.person_id)
        FROM project_people AS pp
        JOIN euroqol_memberships AS em USING (person_id)
        WHERE pp.role='PRINCIPAL_INVESTIGATOR'
        """,
    )
    for label, expected, actual in (
        ("project leaders", args.expect_project_leaders, project_leaders),
        ("EuroQol members", args.expect_members, members),
        ("leaders and members", args.expect_leaders_and_members, leaders_and_members),
    ):
        if expected is not None and expected != actual:
            raise SystemExit(f"{label}: expected {expected}, found {actual}")
    bad_project_people = connection.execute(
        """
        SELECT p.project_id
        FROM projects AS p
        LEFT JOIN project_people AS pp
          ON pp.project_id=p.project_id AND pp.role='PRINCIPAL_INVESTIGATOR'
        GROUP BY p.project_id HAVING COUNT(pp.person_id) <> 1
        LIMIT 5
        """
    ).fetchall()
    if bad_project_people:
        raise SystemExit(f"Projects do not have one project leader: {bad_project_people}")
    if counts["publication_citations"] != counts["publications"]:
        raise SystemExit("One or more publications have no citation snapshot.")
    bad_author_status = connection.execute(
        """
        SELECT publication_id, person_id FROM publication_authors
        WHERE resolution_status NOT IN ('ACCEPTED','UNRESOLVED') LIMIT 5
        """
    ).fetchall()
    if bad_author_status:
        raise SystemExit(f"Publication authors have invalid status: {bad_author_status}")

    bad_family_counts = connection.execute(
        """
        SELECT s.study_id, COUNT(t.study_type)
        FROM studies AS s LEFT JOIN study_types AS t USING (study_id)
        GROUP BY s.study_id HAVING COUNT(t.study_type) <> 1
        LIMIT 5
        """
    ).fetchall()
    if bad_family_counts:
        raise SystemExit(f"Studies must have one primary family: {bad_family_counts}")
    bad_families = unexpected_values(
        connection,
        "study_types",
        "study_type",
        controlled_values("primary_research_family"),
    )
    if bad_families:
        raise SystemExit(f"Primary research families are invalid: {bad_families}")
    studies_without_purpose = connection.execute(
        """
        SELECT s.study_id
        FROM studies AS s LEFT JOIN research_purposes AS p USING (study_id)
        GROUP BY s.study_id HAVING COUNT(p.purpose) = 0
        LIMIT 5
        """
    ).fetchall()
    if studies_without_purpose:
        raise SystemExit(f"Studies have no research purpose: {studies_without_purpose}")
    bad_purposes = unexpected_values(
        connection,
        "research_purposes",
        "purpose",
        controlled_values("research_purpose"),
    )
    if bad_purposes:
        raise SystemExit(f"Research purposes are invalid: {bad_purposes}")
    bad_contexts = unexpected_values(
        connection,
        "scientific_uses",
        "context",
        controlled_values("use_context"),
    )
    if bad_contexts:
        raise SystemExit(f"Scientific-use contexts are invalid: {bad_contexts}")
    blank_labels = scalar(
        connection,
        """
        SELECT COUNT(*) FROM scientific_uses
        WHERE trim(source_label) = ''
           OR canonical_label IS NOT NULL AND trim(canonical_label) = ''
        """,
    )
    if blank_labels:
        raise SystemExit(f"Scientific uses have {blank_labels} blank labels.")
    unknown_registry_ids = scalar(
        connection,
        """
        SELECT COUNT(*) FROM scientific_uses AS u
        LEFT JOIN registry_entities AS r USING (registry_id)
        WHERE u.registry_id IS NOT NULL AND r.registry_id IS NULL
        """,
    )
    if unknown_registry_ids:
        raise SystemExit(
            f"Scientific uses have {unknown_registry_ids} unknown registry IDs."
        )
    raw_aggregate_labels = scalar(
        connection,
        """
        SELECT
          (SELECT COUNT(*) FROM instrument_uses AS x
           LEFT JOIN scientific_uses AS u ON u.use_id=x.instrument_use_id
           LEFT JOIN registry_entities AS r USING (registry_id)
           WHERE u.registry_id IS NULL OR r.scope <> 'GLOBAL')
          +
          (SELECT COUNT(*) FROM method_uses AS x
           LEFT JOIN scientific_uses AS u ON u.use_id=x.method_use_id
           LEFT JOIN registry_entities AS r USING (registry_id)
           WHERE u.registry_id IS NULL OR r.scope <> 'GLOBAL')
          +
          (SELECT COUNT(*) FROM model_uses AS x
           LEFT JOIN scientific_uses AS u ON u.use_id=x.model_use_id
           LEFT JOIN registry_entities AS r USING (registry_id)
           WHERE u.registry_id IS NULL OR r.scope <> 'GLOBAL')
          +
          (SELECT COUNT(*) FROM protocols AS x
           LEFT JOIN scientific_uses AS u ON u.use_id=x.protocol_id
           LEFT JOIN registry_entities AS r USING (registry_id)
           WHERE u.registry_id IS NULL OR r.scope <> 'GLOBAL')
          +
          (SELECT COUNT(*) FROM product_uses AS x
           LEFT JOIN scientific_uses AS u ON u.use_id=x.product_use_id
           LEFT JOIN registry_entities AS r USING (registry_id)
           WHERE u.registry_id IS NULL OR r.scope <> 'GLOBAL')
        """,
    )
    if raw_aggregate_labels:
        raise SystemExit(
            "An aggregate category table contains raw or source-scoped labels."
        )
    inconsistent_findings = connection.execute(
        """
        SELECT f.finding_id
        FROM findings AS f JOIN studies AS s USING (study_id)
        WHERE f.publication_id <> s.publication_id
        LIMIT 5
        """
    ).fetchall()
    if inconsistent_findings:
        raise SystemExit(f"Findings have inconsistent owners: {inconsistent_findings}")
    inconsistent_limitations = connection.execute(
        """
        SELECT l.limitation_id
        FROM limitations AS l JOIN studies AS s USING (study_id)
        WHERE l.publication_id <> s.publication_id
        LIMIT 5
        """
    ).fetchall()
    if inconsistent_limitations:
        raise SystemExit(
            f"Limitations have inconsistent owners: {inconsistent_limitations}"
        )
    invalid_administration_targets = connection.execute(
        """
        SELECT t.administration_id, t.target_use_id
        FROM administration_targets AS t
        LEFT JOIN scientific_uses AS u ON u.use_id=t.target_use_id
        LEFT JOIN task_designs AS d ON d.task_id=t.target_use_id
        WHERE u.use_id IS NULL AND d.task_id IS NULL
        LIMIT 5
        """
    ).fetchall()
    if invalid_administration_targets:
        raise SystemExit(
            "Administration targets do not exist: "
            f"{invalid_administration_targets}"
        )
    if scalar(
        connection,
        "SELECT COUNT(*) FROM project_publications WHERE project_output IS NULL",
    ):
        raise SystemExit("An accepted project link has no output decision.")
    bad_year_links = connection.execute(
        """
        SELECT pp.project_id, pp.publication_id, p.start_year, w.publication_year
        FROM project_publications AS pp
        JOIN projects AS p USING (project_id)
        JOIN publications AS w USING (publication_id)
        WHERE p.start_year IS NOT NULL AND w.publication_year IS NOT NULL
          AND p.start_year > w.publication_year
        LIMIT 5
        """
    ).fetchall()
    if bad_year_links:
        raise SystemExit(f"Project links violate the year rule: {bad_year_links}")

    for table in sorted(tables):
        columns = [
            row[1]
            for row in connection.execute(f"PRAGMA table_info({table})")
            if row[2].upper() == "TEXT"
        ]
        for column in columns:
            for forbidden in FORBIDDEN_TEXT:
                row = connection.execute(
                    f"SELECT rowid FROM {table} "
                    f"WHERE instr(COALESCE({column},''), ?) > 0 LIMIT 1",
                    (forbidden,),
                ).fetchone()
                if row:
                    raise SystemExit(f"Unsafe text in {table}.{column}: {forbidden}")

    result = {
        **counts,
        "study_families": scalar(
            connection, "SELECT COUNT(DISTINCT study_type) FROM study_types"
        ),
        "mapped_scientific_uses": scalar(
            connection,
            "SELECT COUNT(*) FROM scientific_uses WHERE registry_id IS NOT NULL",
        ),
        "unmapped_scientific_uses": scalar(
            connection,
            "SELECT COUNT(*) FROM scientific_uses WHERE registry_id IS NULL",
        ),
        "project_leaders": project_leaders,
        "euroqol_members": members,
        "leaders_and_members": leaders_and_members,
        "openalex_citations": scalar(
            connection, "SELECT COALESCE(SUM(cited_by_count),0) FROM publication_citations"
        ),
        "status": "pass",
    }
    connection.close()
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
