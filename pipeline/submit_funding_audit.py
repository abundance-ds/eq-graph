#!/usr/bin/env python3
"""Submission tool for the EuroQol funding-scope audit."""

import json
import os
import pathlib
import sys


ROOT = pathlib.Path.cwd()
MANIFEST = ROOT / "batch.json"
OUTPUT = ROOT / "funding.jsonl"
SCOPES = {
    "study_funding", "related_work_funding", "publication_support_only",
    "nonfinancial_support_only", "no_euroqol_support", "unclear",
}


def load(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []


def status():
    expected = {item["record_id"] for item in json.loads(MANIFEST.read_text())["records"]}
    values = load(OUTPUT)
    received = {item["record_id"] for item in values}
    print(f"submitted={len(received)}/{len(expected)}")
    raise SystemExit(0 if received == expected and len(values) == len(expected) else 1)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "status":
        status()
    if len(sys.argv) != 4:
        raise SystemExit("usage: submit_funding RECORD_ID SCOPE EVIDENCE")
    record_id, scope, evidence = sys.argv[1:]
    manifest = json.loads(MANIFEST.read_text())
    valid = {item["record_id"] for item in manifest["records"]}
    if record_id not in valid:
        raise SystemExit("unknown record_id")
    if scope not in SCOPES:
        raise SystemExit("invalid funding scope")
    evidence = " ".join(evidence.split())
    if not evidence or len(evidence) > 600:
        raise SystemExit("evidence must contain 1-600 characters")
    values = load(OUTPUT)
    if any(item["record_id"] == record_id for item in values):
        raise SystemExit("record already submitted")
    descriptor = os.open(OUTPUT, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    with os.fdopen(descriptor, "a") as handle:
        handle.write(json.dumps({"record_id": record_id, "funding_scope": scope, "funding_scope_evidence": evidence}, ensure_ascii=False) + "\n")
    print(f"accepted {record_id} ({len(values) + 1}/{len(valid)})")


if __name__ == "__main__":
    main()
