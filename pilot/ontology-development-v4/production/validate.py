#!/usr/bin/env python3
"""Validate production JSON records with structural and semantic rules."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from schema import GAP_VALUES, HERE, VOCABULARY, build_schema, read_vocabulary


DESIGN_KEYS = {
    "component_approach",
    "temporal_structure",
    "comparison_structure",
    "allocation_structure",
    "mixed_method_integration",
    "synthesis_design",
}
REGISTRY_TYPE = {
    "InstrumentUse": "Instrument",
    "MethodUse": "Method",
    "ProtocolUse": "Protocol",
    "ModelUse": "Model",
    "SoftwareUse": "Software",
    "ProductUse": "Product",
    "ScoringUse": "Product",
}
VARIANT_KINDS = {
    "LEVEL_VERSION",
    "LANGUAGE_EDITION",
    "RESPONDENT_VERSION",
    "PROTOCOL_VERSION",
    "STUDY_ADAPTATION",
    "EXPERIMENTAL_VERSION",
    "PRODUCT_VERSION",
    "FORM_VERSION",
    "METHOD_VARIANT",
    "LOCAL_INSTRUMENT",
    "INTEGRATED_WORKFLOW",
    "MODEL_VARIANT",
    "SOFTWARE_VERSION",
    "FACTOR_MODEL",
    "SUBSCALE",
}
STUDY_REQUIRED = {
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
}
def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_registry(path: Path) -> dict[str, dict[str, str]]:
    return {row["registry_id"]: row for row in read_tsv(path)}


def validate_registry(registry: dict[str, dict[str, str]]) -> list[str]:
    """Validate identity parent relations and controlled variant kinds."""
    errors: list[str] = []
    for registry_id, row in registry.items():
        parent_id = row.get("parent_registry_id", "")
        applies_to_id = row.get("applies_to_registry_id", "")
        variant_kind = row.get("variant_kind", "")
        if variant_kind and variant_kind not in VARIANT_KINDS:
            errors.append(f"{registry_id}: unknown variant_kind {variant_kind}")
        if parent_id and not variant_kind:
            errors.append(f"{registry_id}: a parent requires variant_kind")
        if parent_id:
            parent = registry.get(parent_id)
            if parent is None:
                errors.append(f"{registry_id}: unknown parent_registry_id {parent_id}")
            elif parent["entity_type"] != row["entity_type"]:
                errors.append(f"{registry_id}: parent {parent_id} has a different type")
        if applies_to_id:
            target = registry.get(applies_to_id)
            if target is None:
                errors.append(
                    f"{registry_id}: unknown applies_to_registry_id {applies_to_id}"
                )
            elif row["entity_type"] == "Product" and target["entity_type"] != "Instrument":
                errors.append(
                    f"{registry_id}: a Product applies_to target must be an Instrument"
                )

    for registry_id in registry:
        seen: set[str] = set()
        current = registry_id
        while current:
            if current in seen:
                errors.append(f"{registry_id}: registry parent cycle")
                break
            seen.add(current)
            row = registry.get(current)
            current = row.get("parent_registry_id", "") if row else ""
    return sorted(set(errors))


def resolve_record_path(
    record_id: str,
    run: Path,
    fallback_runs: list[Path],
) -> tuple[Path, Path] | None:
    """Return the first record path and its source run in precedence order."""
    for candidate_run in (run, *fallback_runs):
        path = candidate_run / "records" / f"{record_id}.json"
        if path.is_file():
            return path, candidate_run
    return None


def path_text(error: Any) -> str:
    path = ".".join(str(value) for value in error.absolute_path)
    return f"{path}: {error.message}" if path else error.message


def validate_semantics(
    record: dict[str, Any],
    expected_record_id: str | None,
    registry: dict[str, dict[str, str]],
    require_null_registry: bool = False,
    skip_filter_rule: bool = False,
    vocabulary: dict[str, list[str]] | None = None,
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if expected_record_id and record["record_id"] != expected_record_id:
        errors.append(
            f"record_id is {record['record_id']}; expected {expected_record_id}"
        )

    assessment = record["assessment"]
    disposition = assessment["disposition"]
    connection = assessment["connection"]
    support = assessment["euroqol_support"]
    publication_form = assessment["publication_form"]
    publication_relation = assessment["publication_relation"]
    expected = (
        "include-study"
        if connection in {"direct_eq", "adjacent_measurement"} or support == "explicit"
        else "exclude"
        if connection in {"application_only", "unrelated"} and support != "explicit"
        else "unclear"
    )
    if not skip_filter_rule and disposition != "publication-context" and disposition != expected:
        errors.append(f"filter rule gives {expected}; record gives {disposition}")
    notice_relation = {
        "CORRECTION_NOTICE": "CORRECTS",
        "RETRACTION_NOTICE": "RETRACTS",
    }
    if publication_form in notice_relation:
        if disposition != "publication-context":
            errors.append(f"{publication_form} must use publication-context")
        if not publication_relation:
            errors.append(f"{publication_form} requires publication_relation")
        elif publication_relation["type"] != notice_relation[publication_form]:
            errors.append(
                f"{publication_form} requires relation {notice_relation[publication_form]}"
            )
    elif publication_relation:
        errors.append("publication_relation is allowed only for a notice")
    if disposition in {"exclude", "publication-context"}:
        if record["studies"] or record["items"]:
            errors.append(f"{disposition} record must not contain studies or items")
        return errors, warnings
    if disposition != "include-study":
        if record["studies"] or record["items"]:
            errors.append("unclear record must not contain studies or items")
        return errors, warnings
    if not record["studies"]:
        errors.append("included record has no study")

    studies = {study["id"]: study for study in record["studies"]}
    if len(studies) != len(record["studies"]):
        errors.append("study IDs are not unique")
    items = record["items"]
    item_by_id = {item["id"]: item for item in items}
    if len(item_by_id) != len(items):
        errors.append("item IDs are not unique")
    overlap = sorted(set(studies) & set(item_by_id))
    if overlap:
        errors.append("study and item IDs overlap: " + ", ".join(overlap))

    parts = {item["id"] for item in items if item["type"] == "StudyPart"}
    item_types = {item["id"]: item["type"] for item in items}
    for item in items:
        item_type = item["type"]
        study_id = item["study_id"]
        part_id = item["part_id"]
        if item_type in STUDY_REQUIRED and not study_id:
            errors.append(f"{item['id']}: {item_type} requires study_id")
        if study_id and study_id not in studies:
            errors.append(f"{item['id']}: unknown study_id {study_id}")
        if part_id and part_id not in parts:
            errors.append(f"{item['id']}: unknown part_id {part_id}")
        if item_type == "StudyPart" and part_id is not None:
            errors.append(f"{item['id']}: StudyPart part_id must be null")

    for study_id in studies:
        study_parts = [
            item for item in items if item["type"] == "StudyPart" and item["study_id"] == study_id
        ]
        purposes = sorted(
            (
                item for item in items if item["type"] == "Purpose" and item["study_id"] == study_id
            ),
            key=lambda item: item["rank"],
        )
        ranks = [item["rank"] for item in purposes]
        if not purposes:
            errors.append(f"{study_id}: no Purpose")
        elif ranks != list(range(1, len(ranks) + 1)):
            errors.append(f"{study_id}: purpose ranks must start at 1 and have no gaps")
        if studies[study_id]["result_state"] == "RESULTS_REPORTED":
            if not any(item["type"] == "Finding" and item["study_id"] == study_id for item in items):
                errors.append(f"{study_id}: results are reported but no Finding is present")

    vocabulary = vocabulary or read_vocabulary()
    designs_by_scope: dict[tuple[str, str | None], dict[str, list[str]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for item in items:
        if item["type"] != "Design":
            continue
        axis = item["axis"]
        value = item["value"]
        if axis not in DESIGN_KEYS:
            errors.append(f"{item['id']}: unknown design axis {axis}")
        elif value not in vocabulary[axis] and value not in GAP_VALUES:
            errors.append(f"{item['id']}: {value} is not valid for {axis}")
        designs_by_scope[(item["study_id"], item["part_id"])][axis].append(value)
    def validate_design_axes(scope: str, axes: dict[str, list[str]]) -> None:
        if not axes["component_approach"]:
            errors.append(f"{scope}: no component_approach")
        for axis in ("temporal_structure", "allocation_structure"):
            if len(axes[axis]) != 1:
                errors.append(f"{scope}: {axis} must occur exactly once")
        if not axes["comparison_structure"]:
            errors.append(f"{scope}: no comparison_structure")

    for study_id in studies:
        study_parts = [
            item["id"]
            for item in items
            if item["type"] == "StudyPart" and item["study_id"] == study_id
        ]
        defaults = designs_by_scope[(study_id, None)]
        if not study_parts:
            validate_design_axes(study_id, defaults)
            continue
        for part_id in study_parts:
            local = designs_by_scope[(study_id, part_id)]
            axes = {
                axis: local[axis] if local[axis] else defaults[axis]
                for axis in DESIGN_KEYS
            }
            validate_design_axes(part_id, axes)

    for item in items:
        item_type = item["type"]
        if item_type in REGISTRY_TYPE:
            registry_id = item["registry_id"]
            if require_null_registry and registry_id is not None:
                errors.append(f"{item['id']}: AI draft registry_id must be null")
                continue
            if registry_id is None:
                warnings.append(
                    f"{item['id']}: unmapped {REGISTRY_TYPE[item_type]} registry label {item['source_label']}"
                )
            elif registry_id not in registry:
                errors.append(f"{item['id']}: unknown registry_id {registry_id}")
            elif registry[registry_id]["entity_type"] != REGISTRY_TYPE[item_type]:
                errors.append(
                    f"{item['id']}: {registry_id} is not a {REGISTRY_TYPE[item_type]} identity"
                )

    def require_type(reference: str, allowed: set[str], owner: str) -> None:
        actual = item_types.get(reference)
        if actual not in allowed:
            errors.append(
                f"{owner}: {reference} must refer to {', '.join(sorted(allowed))}; got {actual or 'missing'}"
            )

    for item in items:
        item_type = item["type"]
        owner = item["id"]
        if item_type == "Sample" and item["population_id"]:
            require_type(item["population_id"], {"Population"}, owner)
        elif item_type == "ScoringUse":
            require_type(item["instrument_use_id"], {"InstrumentUse"}, owner)
            if item["product_id"]:
                require_type(item["product_id"], {"Product"}, owner)
        elif item_type == "TaskDesign":
            for reference in item["applies_to"]:
                require_type(
                    reference,
                    {"InstrumentUse", "MethodUse", "ProtocolUse", "SoftwareUse"},
                    owner,
                )
        elif item_type == "Administration":
            for reference in item["applies_to"]:
                require_type(
                    reference,
                    {
                        "InstrumentUse",
                        "MethodUse",
                        "ProtocolUse",
                        "SoftwareUse",
                        "TaskDesign",
                    },
                    owner,
                )
        elif item_type == "Outcome":
            for reference in item["instrument_use_ids"]:
                require_type(reference, {"InstrumentUse"}, owner)
        elif item_type in {"Finding", "Limitation", "Concept"}:
            for reference in item["about"]:
                if reference not in item_by_id and reference not in studies:
                    errors.append(f"{owner}: unknown about reference {reference}")
        elif item_type == "Interpretation":
            for reference in item["finding_ids"]:
                require_type(reference, {"Finding"}, owner)
        elif item_type == "ProductStateAssertion":
            require_type(item["product_id"], {"Product"}, owner)
        elif item_type == "Gap" and item["affected_item_id"]:
            if item["affected_item_id"] not in item_by_id and item["affected_item_id"] not in studies:
                errors.append(f"{owner}: unknown affected_item_id {item['affected_item_id']}")

    for item in items:
        if item["type"] == "Sample" and item["size"] is None and item["size_text"] is None:
            warnings.append(f"{item['id']}: sample has no size or size_text")
    return errors, warnings


def validate_record(
    record: dict[str, Any],
    expected_record_id: str | None = None,
    registry_path: Path = HERE / "REGISTRY.tsv",
    require_null_registry: bool = False,
    vocabulary_path: Path = VOCABULARY,
) -> tuple[list[str], list[str]]:
    structural = sorted(
        Draft202012Validator(build_schema(vocabulary_path)).iter_errors(record),
        key=lambda error: list(error.absolute_path),
    )
    errors = [path_text(error) for error in structural]
    if errors:
        return errors, []
    registry = read_registry(registry_path)
    registry_errors = validate_registry(registry)
    if registry_errors:
        return [f"registry: {error}" for error in registry_errors], []
    return validate_semantics(
        record,
        expected_record_id,
        registry,
        require_null_registry=require_null_registry,
        vocabulary=read_vocabulary(vocabulary_path),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument(
        "--fallback-run",
        type=Path,
        action="append",
        default=[],
        help="use records from this run when the primary run has no record",
    )
    parser.add_argument("--manifest", type=Path, default=HERE / "CALIBRATION.tsv")
    parser.add_argument("--registry", type=Path, default=HERE / "REGISTRY.tsv")
    parser.add_argument(
        "--draft",
        action="store_true",
        help="require the AI draft to leave all registry IDs null",
    )
    args = parser.parse_args()
    rows = read_tsv(args.manifest)
    results: list[dict[str, Any]] = []
    for row in rows:
        resolved = resolve_record_path(row["record_id"], args.run, args.fallback_run)
        if resolved is None:
            results.append(
                {
                    "record_id": row["record_id"],
                    "source_run": None,
                    "disposition": None,
                    "errors": ["missing output"],
                    "warnings": [],
                }
            )
            continue
        path, source_run = resolved
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            results.append(
                {
                    "record_id": row["record_id"],
                    "source_run": str(source_run),
                    "disposition": None,
                    "errors": [f"invalid JSON: {error}"],
                    "warnings": [],
                }
            )
            continue
        errors, warnings = validate_record(
            record,
            row["record_id"],
            args.registry,
            require_null_registry=args.draft,
        )
        results.append(
            {
                "record_id": row["record_id"],
                "source_run": str(source_run),
                "disposition": record["assessment"]["disposition"],
                "errors": errors,
                "warnings": warnings,
            }
        )
    summary = {
        "expected": len(rows),
        "present": sum("missing output" not in result["errors"] for result in results),
        "valid": sum(not result["errors"] for result in results),
        "errors": sum(len(result["errors"]) for result in results),
        "warnings": sum(len(result["warnings"]) for result in results),
        "dispositions": dict(
            Counter(result["disposition"] for result in results if result["disposition"])
        ),
    }
    output = {"summary": summary, "records": results}
    args.run.mkdir(parents=True, exist_ok=True)
    (args.run / "VALIDATION.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))
    if summary["valid"] != summary["expected"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
