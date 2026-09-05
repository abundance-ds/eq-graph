#!/usr/bin/env python3
"""Build the compact JSON Schema for one production extraction record."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
VOCABULARY = HERE.parent / "VOCABULARY.tsv"
GAP_VALUES = ("UNMAPPED_VALUE", "UNCERTAIN_MAPPING", "NOT_REPORTED")


def read_vocabulary(path: Path = VOCABULARY) -> dict[str, list[str]]:
    values: dict[str, list[str]] = defaultdict(list)
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            values[row["key"]].append(row["value"])
    return dict(values)


def object_schema(properties: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties),
        "additionalProperties": False,
    }


def nullable(schema: dict[str, Any]) -> dict[str, Any]:
    return {"anyOf": [schema, {"type": "null"}]}


def string(min_length: int = 1) -> dict[str, Any]:
    return {"type": "string", "minLength": min_length}


def string_list(min_items: int = 0) -> dict[str, Any]:
    return {
        "type": "array",
        "items": string(),
        "minItems": min_items,
    }


def enum(values: list[str] | tuple[str, ...]) -> dict[str, Any]:
    return {"type": "string", "enum": list(values)}


def controlled(vocabulary: dict[str, list[str]], key: str) -> dict[str, Any]:
    return enum(vocabulary[key] + [value for value in GAP_VALUES if value not in vocabulary[key]])


def local_id(nullable_value: bool = False) -> dict[str, Any]:
    value = {"type": "string", "pattern": "^[A-Za-z][A-Za-z0-9_-]{0,63}$"}
    return nullable(value) if nullable_value else value


def source() -> dict[str, Any]:
    return string_list(min_items=1)


def base_item(item_type: str, fields: dict[str, Any]) -> dict[str, Any]:
    return object_schema(
        {
            "type": {"type": "string", "const": item_type},
            "id": local_id(),
            "study_id": local_id(nullable_value=True),
            "part_id": local_id(nullable_value=True),
            **fields,
            "source": source(),
        }
    )


def registry_fields(vocabulary: dict[str, list[str]], function_key: str) -> dict[str, Any]:
    return {
        "source_label": string(),
        "registry_id": nullable(string()),
        "context": controlled(vocabulary, "use_context"),
        "function": controlled(vocabulary, function_key),
    }


def item_schemas(vocabulary: dict[str, list[str]]) -> list[dict[str, Any]]:
    value_record = object_schema(
        {
            "reported_value": string(),
            "unit": nullable(string()),
            "denominator": nullable(string()),
            "time": nullable(string()),
            "subgroup": nullable(string()),
            "comparator": nullable(string()),
            "direction": nullable(string()),
            "uncertainty": nullable(string()),
        }
    )
    conflict_statement = object_schema(
        {
            "statement": string(),
            "source": source(),
        }
    )
    return [
        base_item(
            "Purpose",
            {
                "value": controlled(vocabulary, "research_purpose"),
                "rank": {"type": "integer", "minimum": 1},
            },
        ),
        base_item("StudyPart", {"label": string()}),
        base_item(
            "Design",
            {
                "axis": enum(
                    (
                        "component_approach",
                        "temporal_structure",
                        "comparison_structure",
                        "allocation_structure",
                        "mixed_method_integration",
                        "synthesis_design",
                    )
                ),
                "value": enum(
                    sorted(
                        {
                            *GAP_VALUES,
                            *vocabulary["component_approach"],
                            *vocabulary["temporal_structure"],
                            *vocabulary["comparison_structure"],
                            *vocabulary["allocation_structure"],
                            *vocabulary["mixed_method_integration"],
                            *vocabulary["synthesis_design"],
                        }
                    )
                ),
            },
        ),
        base_item(
            "Population",
            {
                "label": string(),
                "role": nullable(string()),
                "geographies": string_list(),
                "conditions": string_list(),
                "age_description": nullable(string()),
                "inclusion_description": nullable(string()),
            },
        ),
        base_item(
            "Sample",
            {
                "population_id": local_id(nullable_value=True),
                "stage": controlled(vocabulary, "sample_stage"),
                "size": nullable({"type": "integer", "minimum": 0}),
                "size_text": nullable(string()),
                "unit": nullable(string()),
                "description": nullable(string()),
            },
        ),
        base_item(
            "DataUse",
            {
                "source_label": string(),
                "origin": controlled(vocabulary, "data_origin"),
                "level": controlled(vocabulary, "data_level"),
                "purpose": nullable(string()),
            },
        ),
        base_item("InstrumentUse", registry_fields(vocabulary, "instrument_function")),
        base_item("MethodUse", registry_fields(vocabulary, "method_function")),
        base_item("ProtocolUse", registry_fields(vocabulary, "protocol_function")),
        base_item("SoftwareUse", registry_fields(vocabulary, "software_function")),
        base_item(
            "ModelUse",
            {
                **registry_fields(vocabulary, "model_function"),
                "analytic_role": controlled(vocabulary, "analytic_role"),
            },
        ),
        base_item("ProductUse", registry_fields(vocabulary, "product_function")),
        base_item(
            "ScoringUse",
            {
                "instrument_use_id": local_id(),
                "source_label": string(),
                "registry_id": nullable(string()),
                "product_id": local_id(nullable_value=True),
                "context": controlled(vocabulary, "use_context"),
            },
        ),
        base_item(
            "TaskDesign",
            {
                "applies_to": string_list(min_items=1),
                "label": string(),
                "profiles": string_list(),
                "attributes": string_list(),
                "levels": string_list(),
                "duration": nullable(string()),
                "alternatives": nullable(string()),
                "task_count": nullable(string()),
                "block": nullable(string()),
                "order": nullable(string()),
                "randomization_unit": nullable(string()),
                "stopping_rule": nullable(string()),
            },
        ),
        base_item(
            "StudyFactor",
            {
                "label": string(),
                "levels": string_list(),
                "role": controlled(vocabulary, "factor_role"),
            },
        ),
        base_item(
            "Administration",
            {
                "applies_to": string_list(min_items=1),
                "respondent": nullable(string()),
                "perspective": nullable(string()),
                "completion": nullable(string()),
                "assistance": nullable(string()),
                "channel": nullable(string()),
                "setting": nullable(string()),
                "instrument_language": nullable(string()),
                "interview_language": nullable(string()),
                "recall_period": nullable(string()),
                "time_point": nullable(string()),
            },
        ),
        base_item(
            "StakeholderInvolvement",
            {
                "group": string(),
                "activity": string(),
                "stage": nullable(string()),
                "role": nullable(string()),
                "influence": string(),
            },
        ),
        base_item(
            "Outcome",
            {
                "family": controlled(vocabulary, "outcome_family"),
                "label": string(),
                "instrument_use_ids": string_list(),
            },
        ),
        base_item(
            "Finding",
            {
                "statement": string(),
                "about": string_list(),
                "values": {"type": "array", "items": value_record},
            },
        ),
        base_item(
            "Interpretation",
            {
                "statement": string(),
                "finding_ids": string_list(min_items=1),
            },
        ),
        base_item(
            "Limitation",
            {
                "statement": string(),
                "about": string_list(),
            },
        ),
        base_item(
            "Product",
            {
                "label": string(),
                "product_type": controlled(vocabulary, "product_type"),
            },
        ),
        base_item(
            "ProductStateAssertion",
            {
                "product_id": local_id(),
                "axis": enum(("DEVELOPMENT", "APPROVAL", "VALIDATION", "DEPLOYMENT", "WITHDRAWAL")),
                "exact_state": string(),
                "assertion_date": nullable(string()),
                "asserted_by": nullable(string()),
            },
        ),
        base_item(
            "Concept",
            {
                "label": string(),
                "description": nullable(string()),
                "about": string_list(),
            },
        ),
        base_item(
            "Gap",
            {
                "state": enum(vocabulary["gap_state"]),
                "affected_item_id": local_id(nullable_value=True),
                "affected_type": string(),
                "affected_key": string(),
                "evidence": string(),
                "importance": string(),
                "proposed_resolution": string(),
            },
        ),
        base_item(
            "SourceConflict",
            {
                "scope": string(),
                "statements": {
                    "type": "array",
                    "items": conflict_statement,
                    "minItems": 2,
                },
            },
        ),
        base_item(
            "PublicationStatusAssertion",
            {
                "status": controlled(vocabulary, "publication_status"),
                "exact_term": string(),
                "assertion_date": nullable(string()),
                "asserted_by": nullable(string()),
                "reason": nullable(string()),
                "notice_doi": nullable(string()),
            },
        ),
    ]


def build_schema(vocabulary_path: Path = VOCABULARY) -> dict[str, Any]:
    vocabulary = read_vocabulary(vocabulary_path)
    publication_relation = object_schema(
        {
            "type": enum(("CORRECTS", "RETRACTS")),
            "target_doi": string(),
            "source": source(),
        }
    )
    assessment = object_schema(
        {
            "disposition": enum(("include-study", "publication-context", "exclude", "unclear")),
            "connection": enum(
                ("direct_eq", "adjacent_measurement", "application_only", "unrelated", "unclear")
            ),
            "euroqol_support": enum(("explicit", "other-funding-only", "none-stated", "unclear")),
            "support_scope": nullable(string()),
            "publication_form": controlled(vocabulary, "publication_form"),
            "publication_relation": nullable(publication_relation),
            "reason": string(),
            "source": source(),
        }
    )
    study = object_schema(
        {
            "id": local_id(),
            "label": string(),
            "primary_research_family": controlled(vocabulary, "primary_research_family"),
            "execution_state": controlled(vocabulary, "execution_state"),
            "result_state": controlled(vocabulary, "result_state"),
            "family_rationale": string(),
            "source": source(),
        }
    )
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "EuroQol paper extraction record 0.1",
        "type": "object",
        "properties": {
            "schema_version": {"type": "string", "const": "eq-record-0.1"},
            "record_id": local_id(),
            "assessment": assessment,
            "studies": {"type": "array", "items": study},
            "items": {"type": "array", "items": {"anyOf": item_schemas(vocabulary)}},
        },
        "required": ["schema_version", "record_id", "assessment", "studies", "items"],
        "additionalProperties": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = json.dumps(build_schema(), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
