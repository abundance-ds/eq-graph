#!/usr/bin/env python3
"""Create and operate one paper-scoped SQL extraction workspace."""

from __future__ import annotations

import csv
import json
import re
import sqlite3
from pathlib import Path
from typing import Any

from fulltext_ingest_tool import reject as save_rejection
from fulltext_ingest_tool import submit as save_submission


ROOT = Path(__file__).resolve().parent.parent
PRODUCTION = ROOT / "pilot" / "ontology-development-v4" / "production"
PILOT = PRODUCTION / "sql-agent-pilot"
SCHEMA_PATH = PILOT / "WORKSPACE_SCHEMA.sql"
VOCABULARY_PATH = PRODUCTION.parent / "VOCABULARY.tsv"
REGISTRY_PATH = PRODUCTION / "REGISTRY.tsv"
ALIASES_PATH = PRODUCTION / "REGISTRY_ALIASES.tsv"
CONCEPT_MAP_PATH = PRODUCTION / "CONCEPT_MAP.tsv"

READ_ONLY_TABLES = {
    "paper_context",
    "candidate_project",
    "controlled_value",
    "registry_identity",
    "registry_alias",
}

ITEM_TABLES = (
    "purpose",
    "study_part",
    "design",
    "population",
    "sample",
    "data_use",
    "instrument_use",
    "method_use",
    "protocol_use",
    "model_use",
    "software_use",
    "product_use",
    "scoring_use",
    "task_design",
    "study_factor",
    "administration",
    "stakeholder_involvement",
    "outcome",
    "finding",
    "interpretation",
    "limitation",
    "product",
    "product_state",
    "concept",
    "gap",
    "source_conflict",
    "publication_status",
)

ITEM_ID_COLUMNS = {
    "purpose": "purpose_id",
    "study_part": "part_id",
    "design": "design_id",
    "population": "population_id",
    "sample": "sample_id",
    "data_use": "data_use_id",
    "instrument_use": "use_id",
    "method_use": "use_id",
    "protocol_use": "use_id",
    "model_use": "use_id",
    "software_use": "use_id",
    "product_use": "use_id",
    "scoring_use": "use_id",
    "task_design": "task_id",
    "study_factor": "factor_id",
    "administration": "administration_id",
    "stakeholder_involvement": "involvement_id",
    "outcome": "outcome_id",
    "finding": "finding_id",
    "interpretation": "interpretation_id",
    "limitation": "limitation_id",
    "product": "product_id",
    "product_state": "state_id",
    "concept": "concept_id",
    "gap": "gap_id",
    "source_conflict": "conflict_id",
    "publication_status": "status_id",
}

ITEM_TYPE_NAMES = {
    "purpose": "Purpose",
    "study_part": "StudyPart",
    "design": "Design",
    "population": "Population",
    "sample": "Sample",
    "data_use": "DataUse",
    "instrument_use": "InstrumentUse",
    "method_use": "MethodUse",
    "protocol_use": "ProtocolUse",
    "model_use": "ModelUse",
    "software_use": "SoftwareUse",
    "product_use": "ProductUse",
    "scoring_use": "ScoringUse",
    "task_design": "TaskDesign",
    "study_factor": "StudyFactor",
    "administration": "Administration",
    "stakeholder_involvement": "StakeholderInvolvement",
    "outcome": "Outcome",
    "finding": "Finding",
    "interpretation": "Interpretation",
    "limitation": "Limitation",
    "product": "Product",
    "product_state": "ProductStateAssertion",
    "concept": "Concept",
    "gap": "Gap",
    "source_conflict": "SourceConflict",
    "publication_status": "PublicationStatusAssertion",
}


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected one JSON object")
    return value


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def context_path_value(context_path: Path, key: str) -> Path:
    context = read_json(context_path)
    value = context.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"context is missing {key}")
    path = Path(value)
    return path if path.is_absolute() else context_path.parent / path


def workspace_path(context_path: Path) -> Path:
    return context_path_value(context_path, "workspace_path")


def connect(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_workspace(context_path: Path, reset: bool = False) -> Path:
    context = read_json(context_path)
    path = workspace_path(context_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if reset:
        path.unlink(missing_ok=True)
    if path.exists():
        return path

    connection = connect(path)
    try:
        connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        connection.execute(
            "INSERT INTO paper_context VALUES (?, ?, ?)",
            (
                context["record_id"],
                context["publication_form"],
                context["source_marker"],
            ),
        )
        projects = context.get("candidate_projects", [])
        connection.executemany(
            """
            INSERT INTO candidate_project(
                project_id,title,abstract,principal_investigator,working_group,
                start_year,end_year,status
            ) VALUES (?,?,?,?,?,?,?,?)
            """,
            [
                (
                    row["project_id"],
                    row.get("title") or "[untitled project]",
                    row.get("abstract"),
                    row.get("principal_investigator"),
                    row.get("working_group"),
                    row.get("start_year"),
                    row.get("end_year"),
                    row.get("status"),
                )
                for row in projects
            ],
        )
        connection.executemany(
            "INSERT INTO controlled_value(key,value,definition) VALUES (?,?,?)",
            [
                (row["key"], row["value"], row["definition"])
                for row in read_tsv(VOCABULARY_PATH)
            ],
        )
        registry_rows = read_tsv(REGISTRY_PATH)
        identity_type = {
            row["registry_id"]: row["entity_type"] for row in registry_rows
        }
        identity_name = {
            row["registry_id"]: row["canonical_label"] for row in registry_rows
        }
        identities = {
            (row["entity_type"], row["canonical_label"]) for row in registry_rows
        }
        aliases = {
            (
                row.get("use_type") or identity_type[row["registry_id"]],
                row["alias"],
                identity_name[row["registry_id"]],
            )
            for row in read_tsv(ALIASES_PATH)
        }
        for row in read_tsv(CONCEPT_MAP_PATH):
            identities.add(("Concept", row["canonical_label"]))
            aliases.add(("Concept", row["alias"], row["canonical_label"]))
        connection.executemany(
            "INSERT INTO registry_identity(entity_type,canonical_name) VALUES (?,?)",
            sorted(identities),
        )
        connection.executemany(
            "INSERT INTO registry_alias(entity_type,alias,canonical_name) VALUES (?,?,?)",
            sorted(aliases),
        )
        connection.commit()
    finally:
        connection.close()
    return path


def authorizer(
    action: int,
    argument_1: str | None,
    argument_2: str | None,
    database: str | None,
    trigger: str | None,
) -> int:
    del argument_2, database, trigger
    denied_actions = {
        sqlite3.SQLITE_ALTER_TABLE,
        sqlite3.SQLITE_ATTACH,
        sqlite3.SQLITE_CREATE_INDEX,
        sqlite3.SQLITE_CREATE_TABLE,
        sqlite3.SQLITE_CREATE_TEMP_INDEX,
        sqlite3.SQLITE_CREATE_TEMP_TABLE,
        sqlite3.SQLITE_CREATE_TEMP_TRIGGER,
        sqlite3.SQLITE_CREATE_TEMP_VIEW,
        sqlite3.SQLITE_CREATE_TRIGGER,
        sqlite3.SQLITE_CREATE_VIEW,
        sqlite3.SQLITE_DELETE,
        sqlite3.SQLITE_DETACH,
        sqlite3.SQLITE_DROP_INDEX,
        sqlite3.SQLITE_DROP_TABLE,
        sqlite3.SQLITE_DROP_TEMP_INDEX,
        sqlite3.SQLITE_DROP_TEMP_TABLE,
        sqlite3.SQLITE_DROP_TEMP_TRIGGER,
        sqlite3.SQLITE_DROP_TEMP_VIEW,
        sqlite3.SQLITE_DROP_TRIGGER,
        sqlite3.SQLITE_DROP_VIEW,
        sqlite3.SQLITE_PRAGMA,
        sqlite3.SQLITE_REINDEX,
    }
    if action in denied_actions and action != sqlite3.SQLITE_DELETE:
        return sqlite3.SQLITE_DENY
    if action in {sqlite3.SQLITE_INSERT, sqlite3.SQLITE_UPDATE, sqlite3.SQLITE_DELETE}:
        if argument_1 in READ_ONLY_TABLES or (argument_1 or "").startswith("sqlite_"):
            return sqlite3.SQLITE_DENY
    return sqlite3.SQLITE_OK


def run_sql(context_path: Path, statement: str) -> tuple[bool, str]:
    statement = statement.strip()
    if not statement:
        return False, "SQL_ERROR: statement is empty"
    first_word = re.match(r"(?:--[^\n]*\n|/\*.*?\*/\s*)*([A-Za-z]+)", statement, re.DOTALL)
    if not first_word or first_word.group(1).upper() not in {
        "SELECT",
        "WITH",
        "INSERT",
        "UPDATE",
        "DELETE",
    }:
        return False, "SQL_ERROR: use SELECT, INSERT, UPDATE, or DELETE"
    path = initialize_workspace(context_path)
    connection = connect(path)
    connection.set_authorizer(authorizer)
    try:
        cursor = connection.execute(statement)
        if cursor.description:
            names = [value[0] for value in cursor.description]
            rows = [dict(zip(names, row)) for row in cursor.fetchmany(201)]
            truncated = len(rows) > 200
            rows = rows[:200]
            result = json.dumps(rows, ensure_ascii=False, separators=(",", ":"))
            if truncated:
                result += "\nTRUNCATED: more than 200 rows"
            return True, result
        connection.commit()
        return True, f"OK: {cursor.rowcount} row(s) changed"
    except sqlite3.Error as error:
        connection.rollback()
        return False, f"SQL_ERROR: {error}"
    finally:
        connection.close()


def rows(connection: sqlite3.Connection, table: str, order: str) -> list[dict[str, Any]]:
    return [dict(row) for row in connection.execute(f"SELECT * FROM {table} ORDER BY {order}")]


def term_values(connection: sqlite3.Connection, item_id: str, field: str) -> list[str]:
    return [
        row[0]
        for row in connection.execute(
            "SELECT value FROM item_term WHERE item_id=? AND field=? ORDER BY ordinal",
            (item_id, field),
        )
    ]


def relation_targets(
    connection: sqlite3.Connection,
    item_id: str,
    predicate: str,
) -> list[str]:
    return [
        row[0]
        for row in connection.execute(
            """
            SELECT target_item_id FROM item_relation
            WHERE source_item_id=? AND predicate=? ORDER BY ordinal,target_item_id
            """,
            (item_id, predicate),
        )
    ]


def base_item(item_type: str, row: dict[str, Any], id_column: str) -> dict[str, Any]:
    return {
        "type": item_type,
        "id": row[id_column],
        "study_id": row.get("study_id"),
        "part_id": row.get("part_id"),
    }


def registry_item(
    item_type: str,
    row: dict[str, Any],
    analytic_role: bool = False,
) -> dict[str, Any]:
    value = {
        **base_item(item_type, row, "use_id"),
        "name": row["name"],
        "context": row["context"],
        "function": row["function"],
    }
    if analytic_role:
        value["analytic_role"] = row["analytic_role"]
    return value


def item_identity_map(connection: sqlite3.Connection) -> tuple[dict[str, str], list[str]]:
    identities: dict[str, str] = {}
    errors: list[str] = []
    for table in ITEM_TABLES:
        column = ITEM_ID_COLUMNS[table]
        for row in connection.execute(f"SELECT {column} FROM {table}"):
            item_id = row[0]
            if item_id in identities:
                errors.append(
                    f"duplicate item ID {item_id!r} in {identities[item_id]} and {table}"
                )
            else:
                identities[item_id] = table
    return identities, errors


def workspace_errors(connection: sqlite3.Connection) -> list[str]:
    errors: list[str] = []
    identities, duplicate_errors = item_identity_map(connection)
    errors.extend(duplicate_errors)
    for row in connection.execute(
        "SELECT item_id,field FROM item_term ORDER BY item_id,field,ordinal"
    ):
        if row["item_id"] not in identities:
            errors.append(
                f"item_term[{row['item_id']},{row['field']}]: unknown item_id"
            )
    for row in connection.execute(
        "SELECT source_item_id,predicate,target_item_id FROM item_relation ORDER BY source_item_id,ordinal"
    ):
        if row["source_item_id"] not in identities:
            errors.append(
                f"item_relation[{row['source_item_id']}]: unknown source_item_id"
            )
        if row["target_item_id"] not in identities:
            errors.append(
                f"item_relation[{row['source_item_id']}]: unknown target_item_id {row['target_item_id']!r}"
            )
    foreign_keys = connection.execute("PRAGMA foreign_key_check").fetchall()
    for row in foreign_keys:
        errors.append(f"foreign key error in {row[0]} row {row[1]}")
    decision_count = connection.execute("SELECT COUNT(*) FROM eligibility").fetchone()[0]
    if decision_count != 1:
        errors.append("eligibility: insert exactly one row before submit")
    if not connection.execute("SELECT 1 FROM study LIMIT 1").fetchone():
        errors.append("study: insert at least one study before submit")
    return errors


def build_payload(connection: sqlite3.Connection) -> tuple[dict[str, Any], list[tuple[str, str]]]:
    decision = dict(connection.execute("SELECT * FROM eligibility").fetchone())
    studies = [
        {
            "id": row["study_id"],
            "label": row["label"],
            "primary_research_family": row["primary_research_family"],
            "execution_state": row["execution_state"],
            "result_state": row["result_state"],
            "family_rationale": row["family_rationale"],
        }
        for row in rows(connection, "study", "study_id")
    ]
    items: list[dict[str, Any]] = []
    item_locations: list[tuple[str, str]] = []

    def add(table: str, item: dict[str, Any]) -> None:
        items.append(item)
        item_locations.append((table, item["id"]))

    for row in rows(connection, "purpose", "purpose_id"):
        add("purpose", {**base_item("Purpose", row, "purpose_id"), "value": row["value"], "rank": row["rank"]})
    for row in rows(connection, "study_part", "part_id"):
        add(
            "study_part",
            {
                "type": "StudyPart",
                "id": row["part_id"],
                "study_id": row["study_id"],
                "part_id": None,
                "label": row["label"],
            },
        )
    for row in rows(connection, "design", "design_id"):
        add("design", {**base_item("Design", row, "design_id"), "axis": row["axis"], "value": row["value"]})
    for row in rows(connection, "population", "population_id"):
        item_id = row["population_id"]
        add(
            "population",
            {
                **base_item("Population", row, "population_id"),
                "label": row["label"],
                "role": row["role"],
                "geographies": term_values(connection, item_id, "GEOGRAPHY"),
                "conditions": term_values(connection, item_id, "CONDITION"),
                "age_description": row["age_description"],
                "inclusion_description": row["inclusion_description"],
            },
        )
    for row in rows(connection, "sample", "sample_id"):
        add(
            "sample",
            {
                **base_item("Sample", row, "sample_id"),
                "population_id": row["population_id"],
                "stage": row["stage"],
                "size": row["size"],
                "size_text": row["size_text"],
                "unit": row["unit"],
                "description": row["description"],
            },
        )
    for row in rows(connection, "data_use", "data_use_id"):
        add(
            "data_use",
            {
                **base_item("DataUse", row, "data_use_id"),
                "name": row["name"],
                "origin": row["origin"],
                "level": row["level"],
                "purpose": row["purpose"],
            },
        )
    for table, item_type in (
        ("instrument_use", "InstrumentUse"),
        ("method_use", "MethodUse"),
        ("protocol_use", "ProtocolUse"),
        ("software_use", "SoftwareUse"),
        ("product_use", "ProductUse"),
    ):
        for row in rows(connection, table, "use_id"):
            add(table, registry_item(item_type, row))
    for row in rows(connection, "model_use", "use_id"):
        add("model_use", registry_item("ModelUse", row, analytic_role=True))
    for row in rows(connection, "scoring_use", "use_id"):
        add(
            "scoring_use",
            {
                **base_item("ScoringUse", row, "use_id"),
                "instrument_use_id": row["instrument_use_id"],
                "name": row["name"],
                "product_id": row["product_id"],
                "context": row["context"],
            },
        )
    for row in rows(connection, "task_design", "task_id"):
        item_id = row["task_id"]
        add(
            "task_design",
            {
                **base_item("TaskDesign", row, "task_id"),
                "applies_to": relation_targets(connection, item_id, "APPLIES_TO"),
                "label": row["label"],
                "profiles": term_values(connection, item_id, "PROFILE"),
                "attributes": term_values(connection, item_id, "ATTRIBUTE"),
                "levels": term_values(connection, item_id, "LEVEL"),
                "duration": row["duration"],
                "alternatives": row["alternatives"],
                "task_count": row["task_count"],
                "block": row["block"],
                "order": row["task_order"],
                "randomization_unit": row["randomization_unit"],
                "stopping_rule": row["stopping_rule"],
            },
        )
    for row in rows(connection, "study_factor", "factor_id"):
        item_id = row["factor_id"]
        add(
            "study_factor",
            {
                **base_item("StudyFactor", row, "factor_id"),
                "label": row["label"],
                "levels": term_values(connection, item_id, "FACTOR_LEVEL"),
                "role": row["role"],
            },
        )
    for row in rows(connection, "administration", "administration_id"):
        item_id = row["administration_id"]
        add(
            "administration",
            {
                **base_item("Administration", row, "administration_id"),
                "applies_to": relation_targets(connection, item_id, "APPLIES_TO"),
                **{
                    key: row[key]
                    for key in (
                        "respondent",
                        "perspective",
                        "completion",
                        "assistance",
                        "channel",
                        "setting",
                        "instrument_language",
                        "interview_language",
                        "recall_period",
                        "time_point",
                    )
                },
            },
        )
    for row in rows(connection, "stakeholder_involvement", "involvement_id"):
        add(
            "stakeholder_involvement",
            {
                **base_item("StakeholderInvolvement", row, "involvement_id"),
                "group": row["stakeholder_group"],
                "activity": row["activity"],
                "stage": row["stage"],
                "role": row["role"],
                "influence": row["influence"],
            },
        )
    for row in rows(connection, "outcome", "outcome_id"):
        item_id = row["outcome_id"]
        add(
            "outcome",
            {
                **base_item("Outcome", row, "outcome_id"),
                "family": row["family"],
                "label": row["label"],
                "instrument_use_ids": relation_targets(connection, item_id, "MEASURED_WITH"),
            },
        )
    for row in rows(connection, "finding", "finding_id"):
        item_id = row["finding_id"]
        values = [
            {key: value for key, value in dict(value_row).items() if key not in {"finding_id", "ordinal"}}
            for value_row in connection.execute(
                "SELECT * FROM finding_value WHERE finding_id=? ORDER BY ordinal",
                (item_id,),
            )
        ]
        add(
            "finding",
            {
                **base_item("Finding", row, "finding_id"),
                "statement": row["statement"],
                "about": relation_targets(connection, item_id, "ABOUT"),
                "values": values,
            },
        )
    for row in rows(connection, "interpretation", "interpretation_id"):
        item_id = row["interpretation_id"]
        add(
            "interpretation",
            {
                **base_item("Interpretation", row, "interpretation_id"),
                "statement": row["statement"],
                "finding_ids": relation_targets(connection, item_id, "INTERPRETS"),
            },
        )
    for row in rows(connection, "limitation", "limitation_id"):
        item_id = row["limitation_id"]
        add(
            "limitation",
            {
                **base_item("Limitation", row, "limitation_id"),
                "statement": row["statement"],
                "about": relation_targets(connection, item_id, "ABOUT"),
            },
        )
    for row in rows(connection, "product", "product_id"):
        add(
            "product",
            {
                **base_item("Product", row, "product_id"),
                "label": row["label"],
                "product_type": row["product_type"],
            },
        )
    for row in rows(connection, "product_state", "state_id"):
        add(
            "product_state",
            {
                **base_item("ProductStateAssertion", row, "state_id"),
                "product_id": row["product_id"],
                "axis": row["axis"],
                "exact_state": row["exact_state"],
                "assertion_date": row["assertion_date"],
                "asserted_by": row["asserted_by"],
            },
        )
    for row in rows(connection, "concept", "concept_id"):
        item_id = row["concept_id"]
        add(
            "concept",
            {
                **base_item("Concept", row, "concept_id"),
                "name": row["name"],
                "description": row["description"],
                "about": relation_targets(connection, item_id, "ABOUT"),
            },
        )
    for row in rows(connection, "gap", "gap_id"):
        add(
            "gap",
            {
                **base_item("Gap", row, "gap_id"),
                **{
                    key: row[key]
                    for key in (
                        "state",
                        "affected_item_id",
                        "affected_type",
                        "affected_key",
                        "evidence",
                        "importance",
                        "proposed_resolution",
                    )
                },
            },
        )
    for row in rows(connection, "source_conflict", "conflict_id"):
        item_id = row["conflict_id"]
        statements = [
            {"statement": value[0]}
            for value in connection.execute(
                "SELECT statement FROM conflict_statement WHERE conflict_id=? ORDER BY ordinal",
                (item_id,),
            )
        ]
        add(
            "source_conflict",
            {
                **base_item("SourceConflict", row, "conflict_id"),
                "scope": row["scope"],
                "statements": statements,
            },
        )
    for row in rows(connection, "publication_status", "status_id"):
        add(
            "publication_status",
            {
                **base_item("PublicationStatusAssertion", row, "status_id"),
                **{
                    key: row[key]
                    for key in (
                        "status",
                        "exact_term",
                        "assertion_date",
                        "asserted_by",
                        "reason",
                        "notice_doi",
                    )
                },
            },
        )

    extensions: list[dict[str, str]] = []
    extensions.extend(
        {
            "action": "ADD_ENUM_VALUE",
            "key": row["key"],
            "value": row["value"],
            "definition": row["definition"],
        }
        for row in rows(connection, "enum_extension", "key,value")
    )
    extensions.extend(
        {
            "action": "ADD_REGISTRY_ENTITY",
            "entity_type": row["entity_type"],
            "name": row["name"],
        }
        for row in rows(connection, "registry_extension", "entity_type,name")
    )
    extensions.extend(
        {
            "action": "ADD_REGISTRY_ALIAS",
            "entity_type": row["entity_type"],
            "alias": row["alias"],
            "canonical_name": row["canonical_name"],
        }
        for row in rows(connection, "registry_alias_extension", "entity_type,alias")
    )
    project_ids = [row[0] for row in connection.execute("SELECT project_id FROM project_link ORDER BY project_id")]
    payload = {
        "basis": decision["basis"],
        "project_ids": project_ids,
        "reason": decision["reason"],
        "support_scope": decision["support_scope"],
        "record": {"studies": studies, "items": items},
        "extensions": extensions,
    }
    return payload, item_locations


def friendly_errors(
    message: str,
    item_locations: list[tuple[str, str]],
    studies: list[dict[str, Any]],
) -> str:
    def item_replacement(match: re.Match[str]) -> str:
        index = int(match.group(1))
        if index >= len(item_locations):
            return match.group(0)
        table, item_id = item_locations[index]
        return f"{table}[{item_id}]"

    message = re.sub(r"record\.items\.(\d+)", item_replacement, message)
    for index, study in enumerate(studies):
        message = message.replace(
            f"record.studies.{index}", f"study[{study['id']}]"
        )
    message = re.sub(
        r"Resubmit with the exact canonical name\.",
        "Update the named row with the exact canonical name.",
        message,
    )
    message = re.sub(
        r"or add this alias extension: \{.*?\}\. Only use this new-entity "
        r"extension when the identity is genuinely new: \{.*?\}\.",
        (
            "or insert the alias in registry_alias_extension. Only insert the "
            "name in registry_extension when the identity is genuinely new."
        ),
        message,
    )
    message = re.sub(
        r"If none fits and the value is genuinely new, resubmit with "
        r"\{.*?\} in extensions\.",
        (
            "If none fits and the value is genuinely new, insert it in "
            "enum_extension and submit again."
        ),
        message,
    )
    return message


def submit_workspace(context_path: Path) -> tuple[bool, str]:
    path = initialize_workspace(context_path)
    connection = connect(path)
    try:
        errors = workspace_errors(connection)
        if errors:
            return False, "CORRECT_AND_RESUBMIT\n- " + "\n- ".join(errors)
        payload, item_locations = build_payload(connection)
        studies = payload["record"]["studies"]
    finally:
        connection.close()
    success, message = save_submission(context_path, payload)
    return success, friendly_errors(message, item_locations, studies)


def reject_workspace(context_path: Path, reason: str) -> tuple[bool, str]:
    return save_rejection(context_path, reason)
