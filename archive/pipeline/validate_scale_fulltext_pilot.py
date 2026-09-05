#!/usr/bin/env python3
"""Validate the complete full-text eligibility pilot."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parent.parent
PILOT = ROOT / "scale" / "protocol-2.0" / "fulltext-pilot-v1"
SUPPORT_INCLUDE = {"CURRENT_WORK", "DATA_OR_PRIOR_COMPONENT", "AUTHOR_SUPPORT"}


def read_tsv(name: str) -> list[dict[str, str]]:
    with (PILOT / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_unique(rows: list[dict[str, str]], key: str, count: int) -> None:
    if len(rows) != count or len({row[key] for row in rows}) != count:
        raise ValueError(f"Expected {count} unique {key} values.")


def main() -> None:
    availability = read_tsv("AVAILABILITY.tsv")
    require_unique(availability, "record_id", 3148)
    queue = read_tsv("CANDIDATE_QUEUE.tsv")
    require_unique(queue, "record_id", 80)
    queue_groups = Counter(row["sample_group"] for row in queue)
    expected_queue = {
        "boundary-retained": 40,
        "clear-retained": 20,
        "excluded-e1": 6,
        "excluded-e2": 6,
        "excluded-e3": 4,
        "excluded-e4": 4,
    }
    if dict(queue_groups) != expected_queue:
        raise ValueError("Candidate queue strata do not match the frozen design.")
    if any(row["current_graph_overlap"] != "0" for row in queue):
        raise ValueError("The candidate queue contains a current graph record.")

    manifest = read_tsv("MANIFEST.tsv")
    require_unique(manifest, "record_id", 40)
    final_groups = Counter(row["sample_group"] for row in manifest)
    expected_final = {
        "boundary-retained": 20,
        "clear-retained": 10,
        "excluded-e1": 3,
        "excluded-e2": 3,
        "excluded-e3": 2,
        "excluded-e4": 2,
    }
    if dict(final_groups) != expected_final:
        raise ValueError("Final sample strata do not match the frozen design.")
    for row in manifest:
        source = ROOT / row["raw_path"]
        if source.stat().st_size != int(row["bytes"]) or digest(source) != row["sha256"]:
            raise ValueError(f"Source mismatch for {row['record_id']}.")

    parser_failures = read_tsv("PARSER_FAILURES.tsv")
    if len(parser_failures) != len({row["record_id"] for row in parser_failures}):
        raise ValueError("The parser-failure ledger contains a duplicate record ID.")
    failed_ids = {row["record_id"] for row in parser_failures}
    if failed_ids & {row["record_id"] for row in manifest}:
        raise ValueError("A parser failure remains in the final sample.")
    source_exclusions = read_tsv("SOURCE_EXCLUSIONS.tsv")
    require_unique(source_exclusions, "record_id", 1)
    source_exclusion_ids = {row["record_id"] for row in source_exclusions}
    if source_exclusion_ids & {row["record_id"] for row in manifest}:
        raise ValueError("A source exclusion remains in the final sample.")

    preprocess = read_tsv("PREPROCESS.tsv")
    require_unique(preprocess, "record_id", 40)
    if {row["record_id"] for row in preprocess} != {
        row["record_id"] for row in manifest
    }:
        raise ValueError("Preprocess and retrieval record sets differ.")
    for row in preprocess:
        markdown = ROOT / row["markdown_path"]
        if markdown.stat().st_size != int(row["markdown_bytes"]):
            raise ValueError(f"Markdown size mismatch for {row['record_id']}.")
        if digest(markdown) != row["markdown_sha256"]:
            raise ValueError(f"Markdown hash mismatch for {row['record_id']}.")

    eligibility = read_tsv("eligibility/MANIFEST.tsv")
    require_unique(eligibility, "record_id", 40)
    schema = json.loads((PILOT / "ELIGIBILITY_SCHEMA.json").read_text())
    recommendations = Counter()
    connections = Counter()
    support = Counter()
    for row in eligibility:
        input_path = ROOT / row["input_path"]
        if input_path.stat().st_size != int(row["input_bytes"]):
            raise ValueError(f"AI input size mismatch for {row['record_id']}.")
        if digest(input_path) != row["input_sha256"]:
            raise ValueError(f"AI input hash mismatch for {row['record_id']}.")
        record_path = PILOT / "eligibility" / "run-01" / "records" / f"{row['record_id']}.json"
        record = json.loads(record_path.read_text())
        jsonschema.validate(record, schema)
        expected = (
            "INCLUDE"
            if record["connection"] == "DIRECT_EQ"
            or record["euroqol_support"] in SUPPORT_INCLUDE
            else "HUMAN_REVIEW"
            if record["connection"] == "UNCLEAR"
            or record["euroqol_support"] == "UNCLEAR"
            else "EXCLUDE"
        )
        if record["recommendation"] != expected:
            raise ValueError(f"Rule mismatch for {row['record_id']}.")
        recommendations[record["recommendation"]] += 1
        connections[record["connection"]] += 1
        support[record["euroqol_support"]] += 1

    run = json.loads((PILOT / "eligibility" / "run-01" / "SUMMARY.json").read_text())
    if run["valid"] != 40 or not run["api_key_absent_for_all_started_calls"]:
        raise ValueError("The AI run is incomplete or an API key entered a child process.")
    human = read_tsv("HUMAN_REVIEW.tsv")
    require_unique(human, "record_id", 40)
    if any(row["human_verdict"] != "PENDING" for row in human):
        raise ValueError("The initial human-review packet must remain pending.")

    validation = {
        "status": "PASS",
        "availability_records": 3148,
        "candidate_queue": 80,
        "final_sample": 40,
        "final_groups": dict(final_groups),
        "source_formats": dict(Counter(row["format"] for row in manifest)),
        "parser_failures_replaced": len(parser_failures),
        "source_exclusions_replaced": len(source_exclusions),
        "preprocessed": 40,
        "ai_records": 40,
        "api_key_absent_for_all_ai_calls": True,
        "recommendations": dict(recommendations),
        "connections": dict(connections),
        "support": dict(support),
        "human_pending": 40,
    }
    output = PILOT / "VALIDATION.json"
    output.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
