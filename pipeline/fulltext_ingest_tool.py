#!/usr/bin/env python3
"""Validate one worker record and save an accepted extraction draft."""

from __future__ import annotations

import argparse
import copy
import csv
import difflib
import fcntl
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent.parent
PRODUCTION = ROOT / "pilot" / "ontology-development-v4" / "production"
ONTOLOGY = PRODUCTION.parent
sys.path.insert(0, str(PRODUCTION))

from normalize_registry import normalized_label, registry_lookup  # noqa: E402
from schema import GAP_VALUES, build_schema, read_vocabulary  # noqa: E402
from validate import REGISTRY_TYPE, path_text, validate_semantics  # noqa: E402


REGISTRY_PATH = PRODUCTION / "REGISTRY.tsv"
ALIASES_PATH = PRODUCTION / "REGISTRY_ALIASES.tsv"
CONCEPT_MAP_PATH = PRODUCTION / "CONCEPT_MAP.tsv"
VOCABULARY_PATH = ONTOLOGY / "VOCABULARY.tsv"
WORKER_REGISTRY_TYPE = {**REGISTRY_TYPE, "Concept": "Concept"}
REGISTRY_ITEMS = set(WORKER_REGISTRY_TYPE)
EXTENSION_ACTIONS = {
    "ADD_ENUM_VALUE",
    "ADD_REGISTRY_ENTITY",
    "ADD_REGISTRY_ALIAS",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected one JSON object")
    return value


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def extension_path(context_path: Path, context: dict[str, Any]) -> Path:
    value = context.get("extension_log_path", "extensions.jsonl")
    path = Path(value)
    return path if path.is_absolute() else context_path.parent / path


def accepted_path(context_path: Path, context: dict[str, Any]) -> Path:
    value = context.get("accepted_record_path", "accepted.json")
    path = Path(value)
    return path if path.is_absolute() else context_path.parent / path


def read_extensions(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    with path.open("r", encoding="utf-8") as handle:
        fcntl.flock(handle, fcntl.LOCK_SH)
        rows = [json.loads(line) for line in handle if line.strip()]
        fcntl.flock(handle, fcntl.LOCK_UN)
    return rows


def append_extensions(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        handle.seek(0)
        existing = {
            json.dumps(json.loads(line), ensure_ascii=False, sort_keys=True)
            for line in handle
            if line.strip()
        }
        handle.seek(0, os.SEEK_END)
        for row in rows:
            encoded = json.dumps(row, ensure_ascii=False, sort_keys=True)
            if encoded not in existing:
                handle.write(encoded + "\n")
                existing.add(encoded)
        handle.flush()
        os.fsync(handle.fileno())
        fcntl.flock(handle, fcntl.LOCK_UN)


def extension_schema() -> dict[str, Any]:
    enum_addition = {
        "type": "object",
        "properties": {
            "action": {"const": "ADD_ENUM_VALUE"},
            "key": {"type": "string", "minLength": 1},
            "value": {"type": "string", "minLength": 1},
            "definition": {"type": "string", "minLength": 1},
        },
        "required": ["action", "key", "value", "definition"],
        "additionalProperties": False,
    }
    entity_addition = {
        "type": "object",
        "properties": {
            "action": {"const": "ADD_REGISTRY_ENTITY"},
            "entity_type": {
                "type": "string",
                "enum": [
                    "Instrument", "Method", "Protocol", "Model", "Software",
                    "Product", "Concept",
                ],
            },
            "name": {"type": "string", "minLength": 1},
        },
        "required": ["action", "entity_type", "name"],
        "additionalProperties": False,
    }
    alias_addition = {
        "type": "object",
        "properties": {
            "action": {"const": "ADD_REGISTRY_ALIAS"},
            "entity_type": {
                "type": "string",
                "enum": [
                    "Instrument", "Method", "Protocol", "Model", "Software",
                    "Product", "Concept",
                ],
            },
            "alias": {"type": "string", "minLength": 1},
            "canonical_name": {"type": "string", "minLength": 1},
        },
        "required": ["action", "entity_type", "alias", "canonical_name"],
        "additionalProperties": False,
    }
    return {"anyOf": [enum_addition, entity_addition, alias_addition]}


def remove_property(schema: dict[str, Any], name: str) -> None:
    schema.get("properties", {}).pop(name, None)
    if name in schema.get("required", []):
        schema["required"].remove(name)


def worker_record_schema(vocabulary_path: Path) -> dict[str, Any]:
    source = build_schema(vocabulary_path)
    studies = copy.deepcopy(source["properties"]["studies"])
    remove_property(studies["items"], "source")

    items = copy.deepcopy(source["properties"]["items"])
    for variant in items["items"]["anyOf"]:
        item_type = variant["properties"]["type"]["const"]
        remove_property(variant, "source")
        if item_type == "Concept":
            remove_property(variant, "label")
            variant["properties"]["name"] = {"type": "string", "minLength": 1}
            variant["required"].append("name")
        elif item_type in REGISTRY_ITEMS:
            remove_property(variant, "source_label")
            remove_property(variant, "registry_id")
            variant["properties"]["name"] = {"type": "string", "minLength": 1}
            variant["required"].append("name")
        elif item_type == "DataUse":
            remove_property(variant, "source_label")
            variant["properties"]["name"] = {"type": "string", "minLength": 1}
            variant["required"].append("name")
        if item_type == "SourceConflict":
            statement = variant["properties"]["statements"]["items"]
            remove_property(statement, "source")

    return {
        "type": "object",
        "properties": {
            "studies": studies,
            "items": items,
        },
        "required": ["studies", "items"],
        "additionalProperties": False,
    }


def build_submit_schema(vocabulary_path: Path = VOCABULARY_PATH) -> dict[str, Any]:
    nullable_string = {
        "anyOf": [
            {"type": "string", "minLength": 1},
            {"type": "null"},
        ]
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Funded-project paper submission",
        "type": "object",
        "properties": {
            "basis": {
                "type": "string",
                "enum": ["EXPLICIT_SUPPORT", "PROJECT_OUTPUT", "BOTH"],
            },
            "project_ids": {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
                "uniqueItems": True,
            },
            "reason": {"type": "string", "minLength": 1},
            "support_scope": nullable_string,
            "record": worker_record_schema(vocabulary_path),
            "extensions": {
                "type": "array",
                "items": extension_schema(),
                "default": [],
            },
        },
        "required": ["basis", "project_ids", "reason", "support_scope", "record"],
        "additionalProperties": False,
    }


def merged_vocabulary(
    prior: list[dict[str, Any]],
    current: list[dict[str, Any]],
) -> tuple[dict[str, list[str]], Path]:
    additions = [
        row
        for row in [*prior, *current]
        if row.get("action") == "ADD_ENUM_VALUE"
    ]
    base = read_tsv(VOCABULARY_PATH)
    keys = {row["key"] for row in base}
    for row in additions:
        if row["key"] not in keys:
            raise ValueError(f"unknown controlled-vocabulary key: {row['key']}")
    descriptor, name = tempfile.mkstemp(suffix=".tsv")
    os.close(descriptor)
    path = Path(name)
    fields = ["group", "key", "value", "definition"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(base)
        seen = {(row["key"], row["value"]) for row in base}
        for row in additions:
            key = (row["key"], row["value"])
            if key in seen:
                continue
            writer.writerow(
                {
                    "group": "agent_extension",
                    "key": row["key"],
                    "value": row["value"],
                    "definition": row["definition"],
                }
            )
            seen.add(key)
    return read_vocabulary(path), path


def registry_id_for(entity_type: str, name: str, used: set[str]) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", normalized_label(name)).strip("-") or "entity"
    prefix = entity_type.casefold()
    candidate = f"{prefix}:{slug}"
    if candidate not in used:
        return candidate
    suffix = hashlib.sha256(f"{entity_type}\0{name}".encode()).hexdigest()[:8]
    return f"{candidate}-{suffix}"


def merged_registry(
    prior: list[dict[str, Any]],
    current: list[dict[str, Any]],
) -> tuple[
    dict[str, dict[str, str]],
    dict[tuple[str, str], set[str]],
]:
    identities = read_tsv(REGISTRY_PATH)
    aliases = read_tsv(ALIASES_PATH)
    concept_ids: dict[str, str] = {}
    for row in read_tsv(CONCEPT_MAP_PATH):
        canonical = row["canonical_label"]
        registry_id = concept_ids.get(canonical)
        if not registry_id:
            registry_id = registry_id_for(
                "Concept",
                canonical,
                {value["registry_id"] for value in identities},
            )
            concept_ids[canonical] = registry_id
            identities.append(
                {
                    "entity_type": "Concept",
                    "registry_id": registry_id,
                    "canonical_label": canonical,
                    "parent_registry_id": "",
                    "applies_to_registry_id": "",
                    "variant_kind": "",
                    "language_code": "",
                    "jurisdiction": "",
                    "version": "",
                    "respondent_form": "",
                    "source_identifier": "",
                    "scope": "GLOBAL",
                }
            )
        aliases.append(
            {
                "registry_id": registry_id,
                "alias": row["alias"],
                "use_type": "Concept",
            }
        )
    used = {row["registry_id"] for row in identities}
    additions = [*prior, *current]
    for row in additions:
        if row.get("action") != "ADD_REGISTRY_ENTITY":
            continue
        existing = [
            value
            for value in identities
            if value["entity_type"] == row["entity_type"]
            and normalized_label(value["canonical_label"]) == normalized_label(row["name"])
        ]
        if existing:
            continue
        registry_id = registry_id_for(row["entity_type"], row["name"], used)
        used.add(registry_id)
        identities.append(
            {
                "entity_type": row["entity_type"],
                "registry_id": registry_id,
                "canonical_label": row["name"],
                "parent_registry_id": "",
                "applies_to_registry_id": "",
                "variant_kind": "",
                "language_code": "",
                "jurisdiction": "",
                "version": "",
                "respondent_form": "",
                "source_identifier": "",
                "scope": "GLOBAL",
            }
        )
    registry, lookup = registry_lookup(identities, aliases)
    canonical = {
        (row["entity_type"], normalized_label(row["canonical_label"])): row["registry_id"]
        for row in identities
    }
    for row in additions:
        if row.get("action") != "ADD_REGISTRY_ALIAS":
            continue
        key = (row["entity_type"], normalized_label(row["canonical_name"]))
        registry_id = canonical.get(key)
        if not registry_id:
            raise ValueError(
                f"unknown canonical {row['entity_type']}: {row['canonical_name']}"
            )
        use_types = (
            ("Product", "Scoring")
            if row["entity_type"] == "Product"
            else (row["entity_type"],)
        )
        for use_type in use_types:
            lookup[(use_type, normalized_label(row["alias"]))].add(registry_id)
    return registry, lookup


def structural_errors(
    payload: dict[str, Any],
    schema: dict[str, Any],
    vocabulary: dict[str, list[str]],
) -> list[str]:
    variants = {
        value["properties"]["type"]["const"]: value
        for value in schema["properties"]["record"]["properties"]["items"]["items"]["anyOf"]
    }
    raw_errors = sorted(
        Draft202012Validator(schema).iter_errors(payload),
        key=lambda value: list(value.absolute_path),
    )
    selected_item_errors: list[tuple[Any, list[Any]]] = []
    for index, item in enumerate(payload.get("record", {}).get("items", [])):
        variant = variants.get(item.get("type")) if isinstance(item, dict) else None
        if not variant:
            continue
        for error in Draft202012Validator(variant).iter_errors(item):
            selected_item_errors.append((error, ["record", "items", index]))

    errors: list[str] = []
    selected_indexes = {
        index
        for index, item in enumerate(payload.get("record", {}).get("items", []))
        if isinstance(item, dict) and item.get("type") in variants
    }
    combined: list[tuple[Any, list[Any]]] = []
    for error in raw_errors:
        path_values = list(error.absolute_path)
        if (
            len(path_values) >= 3
            and path_values[:2] == ["record", "items"]
            and path_values[2] in selected_indexes
        ):
            continue
        combined.append((error, []))
    combined.extend(selected_item_errors)

    for error, prefix in combined:
        complete_path = [*prefix, *error.absolute_path]
        path = ".".join(str(value) for value in complete_path)
        if error.validator != "enum":
            message = f"{path}: {error.message}" if path else error.message
            errors.append(message)
            continue
        choices = list(error.validator_value)
        vocabulary_key = next(
            (
                key
                for key, values in vocabulary.items()
                if set(choices) == set(values) | set(GAP_VALUES)
            ),
            None,
        )
        if path.endswith(".value") and ".items." in f".{path}":
            try:
                index = int(path.split(".items.", 1)[1].split(".", 1)[0])
                item = payload["record"]["items"][index]
                if item.get("type") == "Design":
                    vocabulary_key = item.get("axis")
                    choices = vocabulary.get(vocabulary_key, choices)
            except (KeyError, IndexError, TypeError, ValueError):
                pass
        if vocabulary_key:
            errors.append(
                f'{path}: "{error.instance}" is not an existing value for '
                f"{vocabulary_key}. Use one of: {json.dumps(choices, ensure_ascii=False)}. "
                "If none fits and the value is genuinely new, resubmit with "
                f'{{"action":"ADD_ENUM_VALUE","key":"{vocabulary_key}",'
                f'"value":{json.dumps(error.instance, ensure_ascii=False)},'
                '"definition":"[short definition]"}} in extensions.'
            )
        else:
            errors.append(path_text(error))
    return errors


def possible_registry_matches(
    entity_type: str,
    name: str,
    registry: dict[str, dict[str, str]],
    limit: int = 8,
) -> list[str]:
    labels = {
        row["canonical_label"]
        for row in registry.values()
        if row["entity_type"] == entity_type
    }
    normalized = {normalized_label(label): label for label in labels}
    keys = difflib.get_close_matches(normalized_label(name), normalized, n=limit, cutoff=0.35)
    return [normalized[key] for key in keys]


def resolve_registry_items(
    payload: dict[str, Any],
    registry: dict[str, dict[str, str]],
    lookup: dict[tuple[str, str], set[str]],
) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    resolved: dict[str, str] = {}
    for index, item in enumerate(payload["record"]["items"]):
        item_type = item["type"]
        entity_type = WORKER_REGISTRY_TYPE.get(item_type)
        if not entity_type:
            continue
        use_type = "Scoring" if item_type == "ScoringUse" else entity_type
        name = item["name"]
        matches = sorted(lookup.get((use_type, normalized_label(name)), set()))
        if len(matches) == 1:
            resolved[item["id"]] = matches[0]
            continue
        if len(matches) > 1:
            labels = [registry[value]["canonical_label"] for value in matches]
            errors.append(
                f"record.items.{index}.name: {name!r} matches more than one "
                f"{entity_type}: {json.dumps(labels, ensure_ascii=False)}. "
                "Resubmit with the exact canonical name."
            )
            continue
        candidates = possible_registry_matches(entity_type, name, registry)
        alias_example = {
            "action": "ADD_REGISTRY_ALIAS",
            "entity_type": entity_type,
            "alias": name,
            "canonical_name": "[existing canonical name]",
        }
        entity_example = {
            "action": "ADD_REGISTRY_ENTITY",
            "entity_type": entity_type,
            "name": name,
        }
        errors.append(
            f"record.items.{index}.name: {name!r} is not a known {entity_type}. "
            f"Check these possible existing identities: {json.dumps(candidates, ensure_ascii=False)}. "
            "If one is the same identity, use its canonical name or add this "
            f"alias extension: {json.dumps(alias_example, ensure_ascii=False)}. "
            "Only use this new-entity extension when the identity is genuinely "
            f"new: {json.dumps(entity_example, ensure_ascii=False)}."
        )
    return errors, resolved


def internal_record(
    context: dict[str, Any],
    payload: dict[str, Any],
    resolved: dict[str, str],
    registry: dict[str, dict[str, str]],
) -> dict[str, Any]:
    marker = context["source_marker"]
    record = {
        "schema_version": "eq-record-0.1",
        "record_id": context["record_id"],
        "assessment": {
            "disposition": "include-study",
            "connection": "direct_eq",
            "euroqol_support": (
                "explicit"
                if payload["basis"] in {"EXPLICIT_SUPPORT", "BOTH"}
                else "none-stated"
            ),
            "support_scope": payload["support_scope"],
            "publication_form": context["publication_form"],
            "publication_relation": context.get("publication_relation"),
            "reason": payload["reason"],
            "source": [marker],
        },
        "studies": copy.deepcopy(payload["record"]["studies"]),
        "items": copy.deepcopy(payload["record"]["items"]),
    }
    for study in record["studies"]:
        study["source"] = [marker]
    for item in record["items"]:
        item["source"] = [marker]
        if item["type"] == "Concept":
            item["label"] = registry[resolved[item["id"]]]["canonical_label"]
            item.pop("name")
        elif item["type"] in REGISTRY_ITEMS:
            item["source_label"] = item.pop("name")
            item["registry_id"] = resolved[item["id"]]
        elif item["type"] == "DataUse":
            item["source_label"] = item.pop("name")
        if item["type"] == "SourceConflict":
            for statement in item["statements"]:
                statement["source"] = [marker]
    return record


def validate_context(context: dict[str, Any]) -> None:
    required = {
        "record_id",
        "candidate_project_ids",
        "publication_form",
        "source_marker",
    }
    missing = sorted(required - set(context))
    if missing:
        raise ValueError("context is missing: " + ", ".join(missing))
    if not isinstance(context["candidate_project_ids"], list):
        raise ValueError("candidate_project_ids must be a list")


def validate_extensions(
    payload: dict[str, Any],
    base_vocabulary: dict[str, list[str]],
) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["submission must be one JSON object"]
    additions = payload.get("extensions", [])
    if not isinstance(additions, list):
        return ["extensions must be a list"]
    for index, row in enumerate(additions):
        if not isinstance(row, dict):
            errors.append(f"extensions.{index}: expected one object")
            continue
        shape_errors = list(Draft202012Validator(extension_schema()).iter_errors(row))
        if shape_errors:
            errors.append(f"extensions.{index}: invalid extension object")
            continue
        action = row.get("action")
        if action not in EXTENSION_ACTIONS:
            continue
        if action == "ADD_ENUM_VALUE":
            if row["key"] not in base_vocabulary:
                errors.append(f"extensions.{index}.key: unknown enum key {row['key']!r}")
            elif row["value"] in base_vocabulary[row["key"]]:
                errors.append(
                    f"extensions.{index}: {row['value']!r} already exists in {row['key']}"
                )
    return errors


def submit(context_path: Path, payload: dict[str, Any]) -> tuple[bool, str]:
    context = read_json(context_path)
    validate_context(context)
    prior = read_extensions(extension_path(context_path, context))
    current = payload.get("extensions", []) if isinstance(payload, dict) else []
    base_vocabulary = read_vocabulary()
    errors = validate_extensions(payload, base_vocabulary)
    if errors:
        return False, "CORRECT_AND_RESUBMIT\n- " + "\n- ".join(errors)
    try:
        vocabulary, temporary_vocabulary = merged_vocabulary(prior, current)
    except (KeyError, ValueError) as error:
        return False, f"CORRECT_AND_RESUBMIT\n- extensions: {error}"
    try:
        schema = build_submit_schema(temporary_vocabulary)
        errors.extend(structural_errors(payload, schema, vocabulary))
        if errors:
            return False, "CORRECT_AND_RESUBMIT\n- " + "\n- ".join(errors)

        basis = payload["basis"]
        project_ids = set(payload["project_ids"])
        candidates = set(context["candidate_project_ids"])
        unknown = sorted(project_ids - candidates)
        if unknown:
            errors.append("unknown candidate project IDs: " + ", ".join(unknown))
        if basis in {"PROJECT_OUTPUT", "BOTH"} and not project_ids:
            errors.append(f"{basis} requires at least one candidate project ID")
        if basis == "EXPLICIT_SUPPORT" and project_ids:
            errors.append("Use BOTH when explicit support and a project link are present")
        if basis in {"EXPLICIT_SUPPORT", "BOTH"} and not payload["support_scope"]:
            errors.append(f"{basis} requires a short support_scope")
        if basis == "PROJECT_OUTPUT" and payload["support_scope"] is not None:
            errors.append("PROJECT_OUTPUT requires support_scope=null")
        if errors:
            return False, "CORRECT_AND_RESUBMIT\n- " + "\n- ".join(errors)

        try:
            registry, lookup = merged_registry(prior, current)
        except (KeyError, ValueError) as error:
            return False, f"CORRECT_AND_RESUBMIT\n- extensions: {error}"
        registry_errors, resolved = resolve_registry_items(payload, registry, lookup)
        if registry_errors:
            return False, "CORRECT_AND_RESUBMIT\n- " + "\n- ".join(registry_errors)

        record = internal_record(context, payload, resolved, registry)
        semantic_errors, warnings = validate_semantics(
            record,
            context["record_id"],
            registry,
            skip_filter_rule=True,
            vocabulary=vocabulary,
        )
        if semantic_errors:
            return False, "CORRECT_AND_RESUBMIT\n- " + "\n- ".join(semantic_errors)

        result = {
            "record_id": context["record_id"],
            "eligibility": {
                "decision": "INCLUDE",
                "basis": basis,
                "project_ids": payload["project_ids"],
                "reason": payload["reason"],
                "source": [context["source_marker"]],
            },
            "record": record,
        }
        append_extensions(
            extension_path(context_path, context),
            [{**row, "record_id": context["record_id"]} for row in current],
        )
        write_json_atomic(accepted_path(context_path, context), result)
        note = "SAVED"
        if warnings:
            note += "\n" + "\n".join(f"NOTE: {value}" for value in warnings)
        return True, note
    finally:
        temporary_vocabulary.unlink(missing_ok=True)


def reject(context_path: Path, comment: str) -> tuple[bool, str]:
    context = read_json(context_path)
    validate_context(context)
    comment = comment.strip()
    if not comment:
        return False, "REJECTED: comment must not be empty"
    result = {
        "record_id": context["record_id"],
        "eligibility": {
            "decision": "EXCLUDE",
            "basis": "NONE",
            "project_ids": [],
            "reason": comment,
            "source": [context["source_marker"]],
        },
        "record": None,
    }
    write_json_atomic(accepted_path(context_path, context), result)
    return True, "SAVED"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--context", type=Path)
    subparsers = parser.add_subparsers(dest="command", required=True)

    schema_parser = subparsers.add_parser("schema")
    schema_parser.add_argument("--output", type=Path)

    reject_parser = subparsers.add_parser("reject")
    reject_parser.add_argument("comment")

    submit_parser = subparsers.add_parser("submit")
    submit_parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="JSON file, or '-' to read JSON from standard input",
    )

    args = parser.parse_args()
    if args.command == "schema":
        content = json.dumps(build_submit_schema(), ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(content, encoding="utf-8")
        else:
            print(content, end="")
        return
    if not args.context:
        parser.error("--context is required for reject and submit")
    if args.command == "reject":
        success, message = reject(args.context, args.comment)
    else:
        if args.input == "-":
            payload = json.load(sys.stdin)
            if not isinstance(payload, dict):
                raise ValueError("standard input must contain one JSON object")
        else:
            payload = read_json(Path(args.input))
        success, message = submit(args.context, payload)
    print(message)
    if not success:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
