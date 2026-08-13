#!/usr/bin/env python3
"""Validated submission tool for a full-text assessment batch."""

import json
import os
import pathlib
import sys


ROOT = pathlib.Path.cwd()
MANIFEST = ROOT / "batch.json"
OUTPUT = ROOT / "assessments.jsonl"
CONNECTIONS = {"direct_eq", "adjacent_measurement", "application_only", "unrelated", "unclear"}
FUNDING = {"explicit_euroqol", "other_funding_only", "no_funding_statement", "unclear"}
LINKS = {"explicit", "probable", "possible", "none", "unclear"}
CONFIDENCE = {"high", "medium", "low"}


def manifest():
    if not MANIFEST.exists():
        raise SystemExit("batch.json not found in current directory")
    return json.loads(MANIFEST.read_text())


def assessments():
    if not OUTPUT.exists():
        return []
    return [json.loads(line) for line in OUTPUT.read_text().splitlines() if line.strip()]


def status():
    expected = {item["record_id"] for item in manifest()["records"]}
    completed = assessments()
    received = {item["record_id"] for item in completed}
    missing = sorted(expected - received)
    print(f"submitted={len(received)}/{len(expected)}")
    if missing:
        print("missing=" + ",".join(missing))
    raise SystemExit(0 if not missing and len(completed) == len(expected) else 1)


def submit(args):
    record_id, connection, funding, link, confidence, project_ids, connection_evidence, funding_evidence, project_evidence = args
    data = manifest()
    records = {item["record_id"]: item for item in data["records"]}
    if record_id not in records:
        raise SystemExit(f"unknown record_id: {record_id}")
    if connection not in CONNECTIONS:
        raise SystemExit("invalid connection class")
    if funding not in FUNDING:
        raise SystemExit("invalid funding class")
    if link not in LINKS:
        raise SystemExit("invalid link class")
    if confidence not in CONFIDENCE:
        raise SystemExit("invalid confidence")
    selected = [] if project_ids == "none" else [value.strip() for value in project_ids.split(";") if value.strip()]
    candidates = set(records[record_id]["candidate_project_ids"])
    if not set(selected) <= candidates:
        raise SystemExit("project_ids must be supplied candidates")
    if link in {"none", "unclear"} and selected:
        raise SystemExit("none or unclear link requires project_ids=none")
    if link in {"explicit", "probable", "possible"} and not selected:
        raise SystemExit("linked assessment requires at least one project_id")
    evidence = [connection_evidence, funding_evidence, project_evidence]
    if any(not value.strip() or len(value) > 600 for value in evidence):
        raise SystemExit("each evidence field must contain 1-600 characters")
    existing = assessments()
    if any(item["record_id"] == record_id for item in existing):
        raise SystemExit(f"assessment already submitted: {record_id}")
    item = {
        "record_id": record_id,
        "connection": connection,
        "funding": funding,
        "project_link": link,
        "confidence": confidence,
        "project_ids": selected,
        "connection_evidence": " ".join(connection_evidence.split()),
        "funding_evidence": " ".join(funding_evidence.split()),
        "project_evidence": " ".join(project_evidence.split()),
    }
    descriptor = os.open(OUTPUT, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    with os.fdopen(descriptor, "a") as handle:
        handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"accepted {record_id} ({len(existing) + 1}/{len(records)})")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "status":
        status()
    if len(sys.argv) != 10:
        raise SystemExit(
            "usage: submit_assessment RECORD_ID CONNECTION FUNDING LINK CONFIDENCE "
            "PROJECT_IDS CONNECTION_EVIDENCE FUNDING_EVIDENCE PROJECT_EVIDENCE"
        )
    submit(sys.argv[1:])


if __name__ == "__main__":
    main()
