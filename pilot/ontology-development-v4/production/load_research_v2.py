#!/usr/bin/env python3
"""Load validated version-4 records into a separate research SQLite database."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sqlite3
import tempfile
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any

from validate import read_registry, resolve_record_path, validate_record, validate_registry


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SCHEMA = HERE / "research_schema_v2.sql"
USE_TYPE = {
    "InstrumentUse": "Instrument",
    "MethodUse": "Method",
    "ProtocolUse": "Protocol",
    "ModelUse": "Model",
    "SoftwareUse": "Software",
    "ProductUse": "Product",
}
ITEM_TYPES = (
    "Purpose",
    "StudyPart",
    "Design",
    "Population",
    "Sample",
    "DataUse",
    "InstrumentUse",
    "MethodUse",
    "ProtocolUse",
    "ModelUse",
    "SoftwareUse",
    "ProductUse",
    "ScoringUse",
    "TaskDesign",
    "StudyFactor",
    "Administration",
    "StakeholderInvolvement",
    "Outcome",
    "Finding",
    "Interpretation",
    "Limitation",
    "Product",
    "ProductStateAssertion",
    "Concept",
    "Gap",
    "SourceConflict",
    "PublicationStatusAssertion",
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def normalized_doi(value: str | None) -> str | None:
    if not value:
        return None
    text = value.strip().casefold()
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text)
    text = re.sub(r"^doi:\s*", "", text)
    return text.rstrip(". ,;") or None


def normalize_person_name(value: str | None) -> str:
    text = unicodedata.normalize("NFKD", value or "")
    text = "".join(character for character in text if not unicodedata.combining(character))
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.casefold()).split())


def publication_year(dates: list[dict[str, str]]) -> int | None:
    priority = ("ppub", "epub", "published", "accepted", "received")
    for date_type in priority:
        for row in dates:
            if row.get("type") == date_type:
                match = re.search(r"(?:19|20)\d{2}", row.get("value", ""))
                if match:
                    return int(match.group())
    years = [
        int(match.group())
        for row in dates
        if (match := re.search(r"(?:19|20)\d{2}", row.get("value", "")))
    ]
    return min(years) if years else None


def global_study(record_id: str, local_id: str) -> str:
    return f"{record_id}:{local_id}"


def global_item(record_id: str, local_id: str) -> str:
    return f"{record_id}:{local_id}"


def add_sources(
    connection: sqlite3.Connection,
    table: str,
    owner_column: str,
    owner_id: str,
    sources: list[str],
) -> None:
    connection.executemany(
        f"INSERT INTO {table}({owner_column}, ordinal, locator) VALUES (?, ?, ?)",
        [(owner_id, index, locator) for index, locator in enumerate(sources, 1)],
    )


def add_item_terms(
    connection: sqlite3.Connection,
    item_id: str,
    value_type: str,
    values: list[str],
) -> None:
    connection.executemany(
        "INSERT INTO item_text_value(item_id, value_type, ordinal, value) VALUES (?, ?, ?, ?)",
        [(item_id, value_type, index, value) for index, value in enumerate(values, 1)],
    )


def add_relation(
    connection: sqlite3.Connection,
    record_id: str,
    source_id: str,
    predicate: str,
    target_local_ids: list[str],
) -> None:
    seen: set[str] = set()
    for ordinal, target_local_id in enumerate(target_local_ids, 1):
        if target_local_id in seen:
            raise ValueError(f"duplicate relation target: {source_id} {predicate} {target_local_id}")
        seen.add(target_local_id)
        connection.execute(
            "INSERT INTO item_relation(source_item_id, predicate, target_item_id, ordinal) VALUES (?, ?, ?, ?)",
            (source_id, predicate, global_item(record_id, target_local_id), ordinal),
        )


def insert_relation_rules(connection: sqlite3.Connection) -> None:
    rules: set[tuple[str, str, str]] = {
        ("Sample", "SAMPLE_OF", "Population"),
        ("ScoringUse", "SCORES", "InstrumentUse"),
        ("ScoringUse", "USES_PRODUCT", "Product"),
        ("Interpretation", "INTERPRETS", "Finding"),
        ("ProductStateAssertion", "ASSERTS_STATE_OF", "Product"),
    }
    for source in ("TaskDesign", "Administration"):
        for target in ("InstrumentUse", "MethodUse", "ProtocolUse", "SoftwareUse"):
            rules.add((source, "APPLIES_TO", target))
    rules.add(("Administration", "APPLIES_TO", "TaskDesign"))
    rules.add(("Outcome", "MEASURED_WITH", "InstrumentUse"))
    for source in ("Finding", "Limitation", "Concept", "Gap"):
        for target in ITEM_TYPES:
            rules.add((source, "ABOUT" if source != "Gap" else "AFFECTS", target))
    connection.executemany(
        "INSERT INTO relation_rule(source_type, predicate, target_type) VALUES (?, ?, ?)",
        sorted(rules),
    )


def load_registry(
    connection: sqlite3.Connection,
    registry_path: Path,
    aliases_path: Path,
) -> None:
    rows = read_tsv(registry_path)
    registry = {row["registry_id"]: row for row in rows}
    errors = validate_registry(registry)
    if errors:
        raise ValueError("invalid registry: " + "; ".join(errors))
    connection.executemany(
        """
        INSERT INTO registry_identity(
            registry_id, entity_type, canonical_label, parent_registry_id,
            applies_to_registry_id, variant_kind, language_code, jurisdiction,
            version, respondent_form, source_identifier, scope
        ) VALUES (?, ?, ?, NULL, NULL, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                row["registry_id"],
                row["entity_type"],
                row["canonical_label"],
                row["variant_kind"] or None,
                row["language_code"] or None,
                row["jurisdiction"] or None,
                row["version"] or None,
                row["respondent_form"] or None,
                row["source_identifier"] or None,
                row["scope"] or None,
            )
            for row in rows
        ],
    )
    for row in rows:
        connection.execute(
            "UPDATE registry_identity SET parent_registry_id=?, applies_to_registry_id=? WHERE registry_id=?",
            (
                row["parent_registry_id"] or None,
                row["applies_to_registry_id"] or None,
                row["registry_id"],
            ),
        )
    entity_types = {row["registry_id"]: row["entity_type"] for row in rows}
    aliases: list[tuple[str, str, str]] = []
    for row in read_tsv(aliases_path):
        registry_id = row["registry_id"]
        explicit_type = row.get("use_type", "")
        if explicit_type:
            allowed_types = (
                ("Product", "Scoring")
                if entity_types[registry_id] == "Product"
                else (entity_types[registry_id],)
            )
            if explicit_type not in allowed_types:
                raise ValueError(
                    f"alias {row['alias']}: invalid use_type {explicit_type}"
                )
            use_types = (explicit_type,)
        elif entity_types[registry_id] == "Product":
            use_types = ("Product", "Scoring")
        else:
            use_types = (entity_types[registry_id],)
        aliases.extend((registry_id, row["alias"], use_type) for use_type in use_types)
    connection.executemany(
        "INSERT INTO registry_alias(registry_id, alias, use_type) VALUES (?, ?, ?)",
        aliases,
    )


def load_people(
    connection: sqlite3.Connection,
    people_path: Path,
    names_path: Path,
    identifiers_path: Path,
) -> None:
    people = read_tsv(people_path)
    connection.executemany(
        "INSERT INTO person VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                row["person_id"],
                row["display_name"],
                row["family_name"] or None,
                row["given_names"] or None,
                row["orcid"] or None,
                row["openalex_id"] or None,
                row["entity_kind"],
                row["identity_status"],
            )
            for row in people
        ],
    )
    connection.executemany(
        "INSERT INTO person_name VALUES (?, ?, ?, ?)",
        [
            (row["person_id"], row["name"], row["name_type"], row["source"])
            for row in read_tsv(names_path)
        ],
    )
    connection.executemany(
        "INSERT INTO person_identifier VALUES (?, ?, ?, ?)",
        [
            (row["person_id"], row["scheme"], row["value"], row["source"])
            for row in read_tsv(identifiers_path)
        ],
    )
    connection.executemany(
        "INSERT INTO euroqol_membership VALUES (?, ?, ?, ?, ?, 'OBSERVED_MEMBER')",
        [
            (
                row["person_id"],
                row["euroqol_member_id"],
                row["member_affiliation"] or None,
                row["member_profile_url"] or None,
                row["membership_observed_date"],
            )
            for row in people
            if row["is_euroqol_member"] == "1"
        ],
    )


def load_publication(
    connection: sqlite3.Connection,
    manifest_row: dict[str, str],
    record: dict[str, Any],
    record_path: Path,
    source_run: Path,
    metadata: dict[str, Any],
    author_resolution: dict[tuple[str, int], dict[str, str]],
) -> tuple[str, list[dict[str, Any]]]:
    publication = metadata["publication"]
    assessment = record["assessment"]
    publication_id = publication["publication_id"]
    if manifest_row.get("xml_path"):
        source_format = "JATS_XML"
        source_path = manifest_row["xml_path"]
        source_sha256 = manifest_row["xml_sha256"]
        source_bytes = manifest_row["xml_bytes"]
    elif manifest_row.get("pdf_path"):
        source_format = "PDF"
        source_path = manifest_row["pdf_path"]
        source_sha256 = manifest_row["pdf_sha256"]
        source_bytes = manifest_row["pdf_bytes"]
    else:
        raise ValueError(f"No source artifact for {record['record_id']}")
    connection.execute(
        """
        INSERT INTO publication(
            publication_id, record_id, doi, pmid, pmcid, title, abstract,
            publication_year, journal, publisher, jats_article_type,
            publication_form, language, volume, issue, article_number,
            licence_url, open_access, canonical_url, assessment_disposition,
            euroqol_connection, euroqol_support, support_scope,
            assessment_reason, schema_version
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            publication_id,
            record["record_id"],
            normalized_doi(publication.get("doi")),
            publication.get("pmid"),
            publication.get("pmcid"),
            publication["title"],
            publication.get("abstract"),
            publication_year(metadata["dates"]),
            publication.get("journal"),
            publication.get("publisher"),
            publication.get("article_type"),
            assessment["publication_form"],
            publication.get("language"),
            publication.get("volume"),
            publication.get("issue"),
            publication.get("article_number"),
            publication.get("licence_url"),
            int(bool(publication.get("open_access"))),
            publication.get("canonical_url"),
            assessment["disposition"],
            assessment["connection"],
            assessment["euroqol_support"],
            assessment.get("support_scope"),
            assessment["reason"],
            record["schema_version"],
        ),
    )
    connection.execute(
        """
        INSERT INTO source_record(
            record_id, article_path, article_sha256, article_bytes, source_format,
            source_path, source_sha256, source_bytes, extraction_record_path,
            extraction_record_sha256, extraction_source_run
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            record["record_id"],
            manifest_row["article_path"],
            manifest_row["article_sha256"],
            int(manifest_row["article_bytes"]),
            source_format,
            source_path,
            source_sha256,
            int(source_bytes),
            str(record_path.relative_to(REPO)),
            digest(record_path),
            str(source_run.relative_to(REPO)) if source_run.is_relative_to(REPO) else str(source_run),
        ),
    )
    add_sources(
        connection,
        "assessment_source",
        "publication_id",
        publication_id,
        assessment["source"],
    )
    connection.executemany(
        "INSERT OR IGNORE INTO publication_date(publication_id, date_type, date_value) VALUES (?, ?, ?)",
        [(publication_id, row["type"], row["value"]) for row in metadata["dates"]],
    )
    connection.executemany(
        "INSERT OR IGNORE INTO publication_url(publication_id, url_type, url) VALUES (?, ?, ?)",
        [(publication_id, row["type"], row["url"]) for row in metadata["urls"]],
    )
    affiliations: dict[str, str] = {}
    for row in metadata["affiliations"]:
        affiliation_id = f"{publication_id}:aff:{row['id']}"
        affiliations[row["id"]] = affiliation_id
        connection.execute(
            "INSERT INTO affiliation VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                affiliation_id,
                publication_id,
                row["id"],
                row["name"],
                row.get("ror"),
                row.get("grid"),
                row.get("isni"),
            ),
        )
    for author in metadata["authors"]:
        order = int(author["order"])
        mapping = author_resolution.get((publication_id, order))
        if not mapping:
            raise ValueError(f"Missing person resolution for {publication_id} author {order}")
        if normalize_person_name(mapping["source_name"]) != normalize_person_name(author["display_name"]):
            raise ValueError(
                f"Person resolution name mismatch for {publication_id} author {order}: "
                f"{mapping['source_name']} != {author['display_name']}"
            )
        person_id = mapping["resolved_person_id"]
        connection.execute(
            "INSERT INTO publication_author VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                publication_id,
                person_id,
                author.get("id"),
                author["display_name"],
                order,
                int(bool(author.get("corresponding"))),
                author.get("email"),
                json_text(author.get("roles", [])),
                mapping["resolution_method"],
                mapping["resolution_status"],
            ),
        )
        for source_affiliation_id in author.get("affiliation_ids", []):
            if source_affiliation_id not in affiliations:
                raise ValueError(
                    f"{record['record_id']}: unknown affiliation {source_affiliation_id}"
                )
            connection.execute(
                "INSERT OR IGNORE INTO author_affiliation VALUES (?, ?, ?)",
                (publication_id, person_id, affiliations[source_affiliation_id]),
            )
    for row in metadata["correspondence"]:
        connection.execute(
            "INSERT INTO publication_correspondence(publication_id, label, correspondence_text, email) VALUES (?, ?, ?, ?)",
            (publication_id, row.get("label"), row["text"], row.get("email")),
        )
    connection.executemany(
        "INSERT OR IGNORE INTO publication_keyword VALUES (?, ?)",
        [(publication_id, value) for value in metadata["keywords"]],
    )
    connection.executemany(
        "INSERT OR IGNORE INTO publication_category VALUES (?, ?, ?)",
        [(publication_id, row["type"], row["value"]) for row in metadata["categories"]],
    )
    for row in metadata["funding"]:
        connection.execute(
            """
            INSERT INTO publication_funding(
                publication_id, funder, award_id, recipient, source_text, source_locator
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                publication_id,
                row.get("funder"),
                row.get("award_id"),
                row.get("recipient"),
                row.get("source_text"),
                row["source_locator"],
            ),
        )
    relation = assessment.get("publication_relation")
    if relation:
        connection.execute(
            "INSERT INTO publication_relation VALUES (?, ?, ?, ?)",
            (
                publication_id,
                relation["type"],
                normalized_doi(relation["target_doi"]),
                json_text(relation["source"]),
            ),
        )
    return publication_id, metadata["references"]


def load_studies_and_items(
    connection: sqlite3.Connection,
    publication_id: str,
    record: dict[str, Any],
) -> tuple[Counter[str], Counter[str]]:
    record_id = record["record_id"]
    for study in record["studies"]:
        study_id = global_study(record_id, study["id"])
        connection.execute(
            "INSERT INTO study VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                study_id,
                publication_id,
                study["id"],
                study["label"],
                study["primary_research_family"],
                study["execution_state"],
                study["result_state"],
                study["family_rationale"],
            ),
        )
        add_sources(connection, "study_source", "study_id", study_id, study["source"])

    items = record["items"]
    source_counts = Counter(item["type"] for item in items)
    ordered = [item for item in items if item["type"] == "StudyPart"] + [
        item for item in items if item["type"] != "StudyPart"
    ]
    for value in ordered:
        item_id = global_item(record_id, value["id"])
        connection.execute(
            "INSERT INTO item VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                item_id,
                publication_id,
                record_id,
                value["id"],
                global_study(record_id, value["study_id"]) if value["study_id"] else None,
                global_item(record_id, value["part_id"]) if value["part_id"] else None,
                value["type"],
                json_text(value),
            ),
        )
        add_sources(connection, "item_source", "item_id", item_id, value["source"])

    by_type: dict[str, list[dict[str, Any]]] = {
        item_type: [item for item in items if item["type"] == item_type]
        for item_type in ITEM_TYPES
    }
    loaded: Counter[str] = Counter()

    def ids(value: dict[str, Any]) -> tuple[str, str | None, str | None]:
        return (
            global_item(record_id, value["id"]),
            global_study(record_id, value["study_id"]) if value["study_id"] else None,
            global_item(record_id, value["part_id"]) if value["part_id"] else None,
        )

    item_local_ids = {item["id"] for item in items}
    study_local_ids = {study["id"] for study in record["studies"]}

    def add_about_relations(item_id: str, references: list[str]) -> None:
        item_references = [value for value in references if value in item_local_ids]
        study_references = [value for value in references if value in study_local_ids]
        if len(item_references) + len(study_references) != len(references):
            raise ValueError(f"{item_id}: unknown ABOUT target")
        add_relation(connection, record_id, item_id, "ABOUT", item_references)
        connection.executemany(
            "INSERT INTO item_study_relation VALUES (?, 'ABOUT', ?)",
            [
                (item_id, global_study(record_id, study_local_id))
                for study_local_id in study_references
            ],
        )

    for value in by_type["Purpose"]:
        item_id, study_id, _ = ids(value)
        connection.execute("INSERT INTO purpose VALUES (?, ?, ?, ?)", (item_id, study_id, value["value"], value["rank"]))
        loaded["Purpose"] += 1
    for value in by_type["StudyPart"]:
        item_id, study_id, _ = ids(value)
        connection.execute("INSERT INTO study_part VALUES (?, ?, ?)", (item_id, study_id, value["label"]))
        loaded["StudyPart"] += 1
    for value in by_type["Design"]:
        item_id, study_id, part_id = ids(value)
        connection.execute("INSERT INTO design VALUES (?, ?, ?, ?, ?)", (item_id, study_id, part_id, value["axis"], value["value"]))
        loaded["Design"] += 1
    for value in by_type["Population"]:
        item_id, _, _ = ids(value)
        connection.execute(
            "INSERT INTO population VALUES (?, ?, ?, ?, ?)",
            (item_id, value["label"], value.get("role"), value.get("age_description"), value.get("inclusion_description")),
        )
        add_item_terms(connection, item_id, "POPULATION_GEOGRAPHY", value["geographies"])
        add_item_terms(connection, item_id, "POPULATION_CONDITION", value["conditions"])
        loaded["Population"] += 1
    for value in by_type["Sample"]:
        item_id, _, _ = ids(value)
        population_id = global_item(record_id, value["population_id"]) if value["population_id"] else None
        connection.execute(
            "INSERT INTO sample VALUES (?, ?, ?, ?, ?, ?, ?)",
            (item_id, population_id, value["stage"], value.get("size"), value.get("size_text"), value.get("unit"), value.get("description")),
        )
        if value["population_id"]:
            add_relation(connection, record_id, item_id, "SAMPLE_OF", [value["population_id"]])
        loaded["Sample"] += 1
    for value in by_type["DataUse"]:
        item_id, _, _ = ids(value)
        connection.execute(
            "INSERT INTO data_use VALUES (?, ?, ?, ?, ?)",
            (item_id, value["source_label"], value["origin"], value["level"], value.get("purpose")),
        )
        loaded["DataUse"] += 1
    for item_type in USE_TYPE:
        for value in by_type[item_type]:
            item_id, _, _ = ids(value)
            connection.execute(
                "INSERT INTO registry_use VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    item_id,
                    USE_TYPE[item_type],
                    value["source_label"],
                    value.get("registry_id"),
                    value["context"],
                    value["function"],
                    value.get("analytic_role"),
                ),
            )
            loaded[item_type] += 1
    for value in by_type["Product"]:
        item_id, _, _ = ids(value)
        connection.execute("INSERT INTO product VALUES (?, ?, ?)", (item_id, value["label"], value["product_type"]))
        loaded["Product"] += 1
    for value in by_type["ScoringUse"]:
        item_id, _, _ = ids(value)
        instrument_id = global_item(record_id, value["instrument_use_id"])
        product_id = global_item(record_id, value["product_id"]) if value["product_id"] else None
        connection.execute(
            "INSERT INTO scoring_use VALUES (?, ?, ?, ?, ?, ?)",
            (item_id, value["source_label"], value.get("registry_id"), value["context"], instrument_id, product_id),
        )
        add_relation(connection, record_id, item_id, "SCORES", [value["instrument_use_id"]])
        if value["product_id"]:
            add_relation(connection, record_id, item_id, "USES_PRODUCT", [value["product_id"]])
        loaded["ScoringUse"] += 1
    for value in by_type["TaskDesign"]:
        item_id, _, _ = ids(value)
        connection.execute(
            "INSERT INTO task_design VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (item_id, value["label"], value.get("duration"), value.get("alternatives"), value.get("task_count"), value.get("block"), value.get("order"), value.get("randomization_unit"), value.get("stopping_rule")),
        )
        add_item_terms(connection, item_id, "TASK_PROFILE", value["profiles"])
        add_item_terms(connection, item_id, "TASK_ATTRIBUTE", value["attributes"])
        add_item_terms(connection, item_id, "TASK_LEVEL", value["levels"])
        add_relation(connection, record_id, item_id, "APPLIES_TO", value["applies_to"])
        loaded["TaskDesign"] += 1
    for value in by_type["StudyFactor"]:
        item_id, _, _ = ids(value)
        connection.execute("INSERT INTO study_factor VALUES (?, ?, ?)", (item_id, value["label"], value["role"]))
        add_item_terms(connection, item_id, "FACTOR_LEVEL", value["levels"])
        loaded["StudyFactor"] += 1
    for value in by_type["Administration"]:
        item_id, _, _ = ids(value)
        connection.execute(
            "INSERT INTO administration VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (item_id, value.get("respondent"), value.get("perspective"), value.get("completion"), value.get("assistance"), value.get("channel"), value.get("setting"), value.get("instrument_language"), value.get("interview_language"), value.get("recall_period"), value.get("time_point")),
        )
        add_relation(connection, record_id, item_id, "APPLIES_TO", value["applies_to"])
        loaded["Administration"] += 1
    for value in by_type["StakeholderInvolvement"]:
        item_id, _, _ = ids(value)
        connection.execute(
            "INSERT INTO stakeholder_involvement VALUES (?, ?, ?, ?, ?, ?)",
            (item_id, value["group"], value["activity"], value.get("stage"), value.get("role"), value["influence"]),
        )
        loaded["StakeholderInvolvement"] += 1
    for value in by_type["Outcome"]:
        item_id, _, _ = ids(value)
        connection.execute("INSERT INTO outcome VALUES (?, ?, ?)", (item_id, value["family"], value["label"]))
        add_relation(connection, record_id, item_id, "MEASURED_WITH", value["instrument_use_ids"])
        loaded["Outcome"] += 1
    for value in by_type["Finding"]:
        item_id, _, _ = ids(value)
        connection.execute("INSERT INTO finding VALUES (?, ?)", (item_id, value["statement"]))
        connection.executemany(
            "INSERT INTO finding_value VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                (
                    item_id,
                    index,
                    row["reported_value"],
                    row.get("unit"),
                    row.get("denominator"),
                    row.get("time"),
                    row.get("subgroup"),
                    row.get("comparator"),
                    row.get("direction"),
                    row.get("uncertainty"),
                )
                for index, row in enumerate(value["values"], 1)
            ],
        )
        add_about_relations(item_id, value["about"])
        loaded["Finding"] += 1
    for value in by_type["Interpretation"]:
        item_id, _, _ = ids(value)
        connection.execute("INSERT INTO interpretation VALUES (?, ?)", (item_id, value["statement"]))
        add_relation(connection, record_id, item_id, "INTERPRETS", value["finding_ids"])
        loaded["Interpretation"] += 1
    for value in by_type["Limitation"]:
        item_id, _, _ = ids(value)
        connection.execute("INSERT INTO limitation VALUES (?, ?)", (item_id, value["statement"]))
        add_about_relations(item_id, value["about"])
        loaded["Limitation"] += 1
    for value in by_type["ProductStateAssertion"]:
        item_id, _, _ = ids(value)
        product_id = global_item(record_id, value["product_id"])
        connection.execute(
            "INSERT INTO product_state_assertion VALUES (?, ?, ?, ?, ?, ?)",
            (item_id, product_id, value["axis"], value["exact_state"], value.get("assertion_date"), value.get("asserted_by")),
        )
        add_relation(connection, record_id, item_id, "ASSERTS_STATE_OF", [value["product_id"]])
        loaded["ProductStateAssertion"] += 1
    for value in by_type["Concept"]:
        item_id, _, _ = ids(value)
        connection.execute("INSERT INTO concept VALUES (?, ?, ?)", (item_id, value["label"], value.get("description")))
        add_about_relations(item_id, value["about"])
        loaded["Concept"] += 1
    for value in by_type["Gap"]:
        item_id, _, _ = ids(value)
        connection.execute(
            "INSERT INTO gap VALUES (?, ?, ?, ?, ?, ?, ?)",
            (item_id, value["state"], value["affected_type"], value["affected_key"], value["evidence"], value["importance"], value["proposed_resolution"]),
        )
        affected = value.get("affected_item_id")
        if affected in item_local_ids:
            add_relation(connection, record_id, item_id, "AFFECTS", [affected])
        elif affected in study_local_ids:
            connection.execute(
                "INSERT INTO item_study_relation VALUES (?, 'AFFECTS', ?)",
                (item_id, global_study(record_id, affected)),
            )
        loaded["Gap"] += 1
    for value in by_type["SourceConflict"]:
        item_id, _, _ = ids(value)
        connection.execute("INSERT INTO source_conflict VALUES (?, ?)", (item_id, value["scope"]))
        connection.executemany(
            "INSERT INTO source_conflict_statement VALUES (?, ?, ?, ?)",
            [(item_id, index, row["statement"], json_text(row["source"])) for index, row in enumerate(value["statements"], 1)],
        )
        loaded["SourceConflict"] += 1
    for value in by_type["PublicationStatusAssertion"]:
        item_id, _, _ = ids(value)
        connection.execute(
            "INSERT INTO publication_status_assertion VALUES (?, ?, ?, ?, ?, ?, ?)",
            (item_id, value["status"], value["exact_term"], value.get("assertion_date"), value.get("asserted_by"), value.get("reason"), value.get("notice_doi")),
        )
        loaded["PublicationStatusAssertion"] += 1
    return source_counts, loaded


def load_projects(connection: sqlite3.Connection, path: Path | None) -> None:
    if not path:
        return
    for row in read_tsv(path) if path.suffix == ".tsv" else []:
        raise AssertionError(row)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        budget_text = (row.get("Approved Budget (EUR)") or "").replace(",", "").strip()
        connection.execute(
            "INSERT INTO project VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                row["Project Id"].strip(),
                row["Title"].strip(),
                row.get("Abstract") or None,
                row.get("Project PI / Applicant Name") or None,
                row.get("Working Group") or None,
                float(budget_text) if budget_text else None,
                row.get("Status") or None,
                int(row["Start Year"]) if row.get("Start Year") else None,
                int(row["End Year"]) if row.get("End Year") else None,
            ),
        )


def insert_project_link_rows(
    connection: sqlite3.Connection,
    rows: list[dict[str, str]],
) -> None:
    connection.executemany(
        "INSERT INTO project_publication VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                row["project_id"],
                row["publication_id"],
                row.get("project_output") or None,
                row.get("support_target") or None,
                row.get("support_scope") or None,
                row["evidence_status"],
            )
            for row in rows
        ],
    )


def load_project_links(connection: sqlite3.Connection, path: Path | None) -> None:
    if not path:
        return
    if path.suffix.casefold() == ".tsv":
        insert_project_link_rows(connection, read_tsv(path))
        return
    source = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        rows = source.execute(
            """
            SELECT pp.project_id, pub.doi, pp.project_output,
                   pp.support_target, pp.support_scope
            FROM project_publications AS pp
            JOIN publications AS pub USING (publication_id)
            """
        ).fetchall()
    finally:
        source.close()
    doi_to_publication = {
        normalized_doi(doi): publication_id
        for publication_id, doi in connection.execute(
            "SELECT publication_id, doi FROM publication WHERE doi IS NOT NULL"
        )
    }
    missing: list[str] = []
    for project_id, doi, project_output, support_target, support_scope in rows:
        publication_id = doi_to_publication.get(normalized_doi(doi))
        if not publication_id:
            missing.append(str(doi))
            continue
        connection.execute(
            "INSERT INTO project_publication VALUES (?, ?, ?, ?, ?, 'audited-accepted-v1')",
            (
                project_id,
                publication_id,
                project_output,
                support_target,
                support_scope,
            ),
        )
    if missing:
        raise ValueError(f"project links have {len(missing)} unknown publication DOIs")


def load_additional_project_links(
    connection: sqlite3.Connection,
    path: Path | None,
) -> None:
    if not path:
        return
    insert_project_link_rows(connection, read_tsv(path))


def load_project_people(connection: sqlite3.Connection, path: Path) -> None:
    connection.executemany(
        "INSERT INTO project_person VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                row["project_id"],
                row["person_id"],
                row["role"],
                row["source_name"],
                row["resolution_method"],
                row["resolution_status"],
            )
            for row in read_tsv(path)
        ],
    )


def load_openalex_publications(connection: sqlite3.Connection, path: Path) -> None:
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    for row in rows:
        connection.execute(
            """
            INSERT INTO publication_openalex VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                row["publication_id"],
                row.get("openalex_id"),
                row.get("openalex_doi"),
                row["source_title"],
                row.get("source_year"),
                row.get("openalex_title"),
                row.get("openalex_year"),
                row.get("title_similarity"),
                row.get("year_difference"),
                row["match_status"],
                row.get("cited_by_count"),
                row.get("openalex_updated_date"),
                row["retrieved_at"],
                row.get("google_scholar_url"),
            ),
        )
        connection.executemany(
            "INSERT INTO publication_openalex_year VALUES (?, ?, ?)",
            [
                (row["publication_id"], value["year"], value["cited_by_count"])
                for value in row.get("counts_by_year", [])
            ],
        )


def resolve_citations(
    connection: sqlite3.Connection,
    references: list[tuple[str, list[dict[str, Any]]]],
) -> None:
    doi_map: dict[str, set[str]] = {}
    pmid_map: dict[str, set[str]] = {}
    for publication_id, doi, pmid in connection.execute(
        "SELECT publication_id, doi, pmid FROM publication"
    ):
        if doi:
            doi_map.setdefault(normalized_doi(doi) or "", set()).add(publication_id)
        if pmid:
            pmid_map.setdefault(str(pmid), set()).add(publication_id)
    for publication_id, rows in references:
        for index, row in enumerate(rows, 1):
            targets: set[str] = set()
            doi = normalized_doi(row.get("doi"))
            pmid = str(row.get("pmid")) if row.get("pmid") else None
            if doi:
                targets.update(doi_map.get(doi, set()))
            if pmid:
                targets.update(pmid_map.get(pmid, set()))
            if len(targets) == 1:
                status = "resolved"
                target = next(iter(targets))
            elif len(targets) > 1:
                status = "identifier-conflict"
                target = None
            else:
                status = "external-or-unresolved"
                target = None
            connection.execute(
                "INSERT INTO citation_occurrence VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    f"{publication_id}:ref:{index}",
                    publication_id,
                    row.get("source_reference_id"),
                    row.get("citation_text"),
                    doi,
                    pmid,
                    target,
                    status,
                ),
            )


def integrity_report(connection: sqlite3.Connection) -> dict[str, Any]:
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    foreign_keys = connection.execute("PRAGMA foreign_key_check").fetchall()
    lost_items = connection.execute(
        "SELECT record_id, item_type FROM load_audit WHERE source_count <> loaded_count"
    ).fetchall()
    cross_parts = connection.execute(
        """
        SELECT i.item_id
        FROM item AS i
        JOIN item AS p ON p.item_id = i.part_item_id
        WHERE i.study_id <> p.study_id OR p.type <> 'StudyPart'
        """
    ).fetchall()
    bad_registry = connection.execute(
        """
        SELECT u.item_id
        FROM registry_use AS u
        JOIN registry_identity AS r USING (registry_id)
        WHERE u.use_type <> r.entity_type
        UNION ALL
        SELECT s.item_id
        FROM scoring_use AS s
        JOIN registry_identity AS r USING (registry_id)
        WHERE r.entity_type <> 'Product'
        """
    ).fetchall()
    bad_relations = connection.execute(
        """
        SELECT r.source_item_id, r.predicate, r.target_item_id
        FROM item_relation AS r
        JOIN item AS source ON source.item_id = r.source_item_id
        JOIN item AS target ON target.item_id = r.target_item_id
        LEFT JOIN relation_rule AS rule
          ON rule.predicate = r.predicate
         AND rule.source_type = source.type
         AND rule.target_type = target.type
        WHERE rule.predicate IS NULL
        """
    ).fetchall()
    missing_findings = connection.execute(
        """
        SELECT s.study_id
        FROM study AS s
        LEFT JOIN item AS i ON i.study_id = s.study_id AND i.type = 'Finding'
        WHERE s.result_state = 'RESULTS_REPORTED'
        GROUP BY s.study_id
        HAVING COUNT(i.item_id) = 0
        """
    ).fetchall()
    bad_ranks = connection.execute(
        """
        SELECT study_id
        FROM purpose
        GROUP BY study_id
        HAVING MIN(rank) <> 1 OR MAX(rank) <> COUNT(*) OR COUNT(DISTINCT rank) <> COUNT(*)
        """
    ).fetchall()
    duplicate_dois = connection.execute(
        """
        SELECT lower(doi)
        FROM publication
        WHERE doi IS NOT NULL
        GROUP BY lower(doi)
        HAVING COUNT(*) > 1
        """
    ).fetchall()
    project_year_errors = connection.execute(
        """
        SELECT pp.project_id, pp.publication_id
        FROM project_publication AS pp
        JOIN project AS p USING (project_id)
        JOIN publication AS pub USING (publication_id)
        WHERE p.start_year > pub.publication_year
        """
    ).fetchall()
    project_person_errors = connection.execute(
        """
        SELECT p.project_id
        FROM project AS p
        LEFT JOIN project_person AS pp
          ON pp.project_id = p.project_id AND pp.role = 'PRINCIPAL_INVESTIGATOR'
        GROUP BY p.project_id
        HAVING COUNT(pp.person_id) <> 1
        """
    ).fetchall()
    publication_author_errors = connection.execute(
        """
        SELECT publication_id, author_order
        FROM publication_author
        WHERE resolution_status NOT IN ('ACCEPTED', 'UNRESOLVED')
        """
    ).fetchall()
    openalex_errors = connection.execute(
        """
        SELECT p.publication_id
        FROM publication AS p
        LEFT JOIN publication_openalex AS oa USING (publication_id)
        WHERE oa.publication_id IS NULL
        """
    ).fetchall()
    counts = {
        "publications": connection.execute("SELECT COUNT(*) FROM publication").fetchone()[0],
        "studies": connection.execute("SELECT COUNT(*) FROM study").fetchone()[0],
        "items": connection.execute("SELECT COUNT(*) FROM item").fetchone()[0],
        "mapped_registry_uses": connection.execute(
            "SELECT (SELECT COUNT(*) FROM registry_use WHERE registry_id IS NOT NULL) + (SELECT COUNT(*) FROM scoring_use WHERE registry_id IS NOT NULL)"
        ).fetchone()[0],
        "unresolved_registry_uses": connection.execute(
            "SELECT (SELECT COUNT(*) FROM registry_use WHERE registry_id IS NULL) + (SELECT COUNT(*) FROM scoring_use WHERE registry_id IS NULL)"
        ).fetchone()[0],
        "citation_occurrences": connection.execute("SELECT COUNT(*) FROM citation_occurrence").fetchone()[0],
        "resolved_citation_edges": connection.execute("SELECT COUNT(*) FROM citation_edge").fetchone()[0],
        "projects": connection.execute("SELECT COUNT(*) FROM project").fetchone()[0],
        "project_publications": connection.execute(
            "SELECT COUNT(*) FROM project_publication"
        ).fetchone()[0],
        "people": connection.execute("SELECT COUNT(*) FROM person").fetchone()[0],
        "project_leaders": connection.execute(
            "SELECT COUNT(DISTINCT person_id) FROM project_person WHERE role='PRINCIPAL_INVESTIGATOR'"
        ).fetchone()[0],
        "euroqol_members": connection.execute(
            "SELECT COUNT(*) FROM euroqol_membership"
        ).fetchone()[0],
        "leaders_and_members": connection.execute(
            """
            SELECT COUNT(DISTINCT pp.person_id)
            FROM project_person AS pp
            JOIN euroqol_membership AS em USING (person_id)
            WHERE pp.role='PRINCIPAL_INVESTIGATOR'
            """
        ).fetchone()[0],
        "publication_authorships": connection.execute(
            "SELECT COUNT(*) FROM publication_author"
        ).fetchone()[0],
        "unresolved_authorships": connection.execute(
            "SELECT COUNT(*) FROM publication_author WHERE resolution_status='UNRESOLVED'"
        ).fetchone()[0],
        "openalex_publications": connection.execute(
            "SELECT COUNT(*) FROM publication_openalex"
        ).fetchone()[0],
        "openalex_citations": connection.execute(
            "SELECT COALESCE(SUM(cited_by_count),0) FROM publication_openalex"
        ).fetchone()[0],
    }
    failures = {
        "integrity": [] if integrity == "ok" else [integrity],
        "foreign_keys": foreign_keys,
        "lost_items": lost_items,
        "cross_study_parts": cross_parts,
        "registry_type": bad_registry,
        "invalid_relations": bad_relations,
        "missing_findings": missing_findings,
        "purpose_ranks": bad_ranks,
        "duplicate_dois": duplicate_dois,
        "project_year_rule": project_year_errors,
        "project_person_coverage": project_person_errors,
        "publication_author_resolution": publication_author_errors,
        "openalex_coverage": openalex_errors,
    }
    return {
        "counts": counts,
        "failures": {key: value for key, value in failures.items() if value},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--fallback-run", type=Path, action="append", default=[])
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--registry", type=Path, default=HERE / "REGISTRY.tsv")
    parser.add_argument("--aliases", type=Path, default=HERE / "REGISTRY_ALIASES.tsv")
    parser.add_argument("--vocabulary", type=Path, default=HERE.parent / "VOCABULARY.tsv")
    parser.add_argument("--projects", type=Path)
    parser.add_argument("--project-links", type=Path)
    parser.add_argument("--additional-project-links", type=Path)
    parser.add_argument("--persons", type=Path, required=True)
    parser.add_argument("--person-names", type=Path, required=True)
    parser.add_argument("--person-identifiers", type=Path, required=True)
    parser.add_argument("--project-persons", type=Path, required=True)
    parser.add_argument("--publication-authors", type=Path, required=True)
    parser.add_argument("--openalex-publications", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expect-studies", type=int)
    parser.add_argument("--expect-items", type=int)
    parser.add_argument("--expect-mapped", type=int)
    parser.add_argument("--expect-unresolved", type=int)
    args = parser.parse_args()

    run = args.run.resolve()
    fallback_runs = [path.resolve() for path in args.fallback_run]
    manifest_rows = read_tsv(args.manifest.resolve())
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    file_descriptor, temporary_name = tempfile.mkstemp(
        prefix=output.stem + ".", suffix=".sqlite", dir=output.parent
    )
    os.close(file_descriptor)
    temporary = Path(temporary_name)
    references: list[tuple[str, list[dict[str, Any]]]] = []
    try:
        connection = sqlite3.connect(temporary)
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(SCHEMA.read_text(encoding="utf-8"))
        insert_relation_rules(connection)
        load_registry(connection, args.registry.resolve(), args.aliases.resolve())
        load_people(
            connection,
            args.persons.resolve(),
            args.person_names.resolve(),
            args.person_identifiers.resolve(),
        )
        author_resolution_rows = read_tsv(args.publication_authors.resolve())
        author_resolution = {
            (row["publication_id"], int(row["author_order"])): row
            for row in author_resolution_rows
        }
        if len(author_resolution) != len(author_resolution_rows):
            raise ValueError("Publication-author resolution contains duplicate keys")
        for manifest_row in manifest_rows:
            resolved = resolve_record_path(manifest_row["record_id"], run, fallback_runs)
            if resolved is None:
                raise ValueError(f"missing record: {manifest_row['record_id']}")
            record_path, source_run = resolved
            record = json.loads(record_path.read_text(encoding="utf-8"))
            errors, _ = validate_record(
                record,
                manifest_row["record_id"],
                args.registry.resolve(),
                vocabulary_path=args.vocabulary.resolve(),
            )
            if errors:
                raise ValueError(f"{manifest_row['record_id']}: " + "; ".join(errors))
            metadata_path = REPO / manifest_row["metadata_path"]
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            publication_id, publication_references = load_publication(
                connection, manifest_row, record, record_path, source_run, metadata,
                author_resolution,
            )
            references.append((publication_id, publication_references))
            source_counts, loaded_counts = load_studies_and_items(connection, publication_id, record)
            for item_type in sorted(set(source_counts) | set(loaded_counts)):
                connection.execute(
                    "INSERT INTO load_audit VALUES (?, ?, ?, ?)",
                    (
                        record["record_id"],
                        item_type,
                        source_counts[item_type],
                        loaded_counts[item_type],
                    ),
                )
        resolve_citations(connection, references)
        load_projects(connection, args.projects.resolve() if args.projects else None)
        load_project_links(
            connection, args.project_links.resolve() if args.project_links else None
        )
        load_additional_project_links(
            connection,
            args.additional_project_links.resolve()
            if args.additional_project_links
            else None,
        )
        load_project_people(connection, args.project_persons.resolve())
        load_openalex_publications(connection, args.openalex_publications.resolve())
        connection.executemany(
            "INSERT INTO build VALUES (?, ?)",
            [
                ("schema", "research-v2"),
                ("manifest_sha256", digest(args.manifest.resolve())),
                ("registry_sha256", digest(args.registry.resolve())),
                ("aliases_sha256", digest(args.aliases.resolve())),
                ("vocabulary_sha256", digest(args.vocabulary.resolve())),
                ("records", str(len(manifest_rows))),
                ("persons_sha256", digest(args.persons.resolve())),
                ("publication_authors_sha256", digest(args.publication_authors.resolve())),
                ("openalex_publications_sha256", digest(args.openalex_publications.resolve())),
            ],
        )
        connection.commit()
        report = integrity_report(connection)
        expected = {
            "studies": args.expect_studies,
            "items": args.expect_items,
            "mapped_registry_uses": args.expect_mapped,
            "unresolved_registry_uses": args.expect_unresolved,
        }
        expectation_failures = {
            key: {"expected": value, "actual": report["counts"][key]}
            for key, value in expected.items()
            if value is not None and report["counts"][key] != value
        }
        if expectation_failures:
            report["failures"]["expected_counts"] = expectation_failures
        if report["failures"]:
            raise ValueError(json.dumps(report["failures"], ensure_ascii=False, indent=2))
        connection.execute("PRAGMA optimize")
        connection.execute("VACUUM")
        connection.close()
        os.replace(temporary, output)
        report["database_sha256"] = digest(output)
        report["database_bytes"] = output.stat().st_size
        report_path = output.with_suffix(output.suffix + ".build.json")
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
    except Exception:
        if "connection" in locals():
            connection.close()
        temporary.unlink(missing_ok=True)
        raise


if __name__ == "__main__":
    main()
