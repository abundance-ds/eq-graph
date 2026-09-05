#!/usr/bin/env python3
"""Validated submission tool for one screening batch."""

import json
import os
import pathlib
import re
import sys


ROOT = pathlib.Path.cwd()
MANIFEST = ROOT / "batch.json"
OUTPUT = ROOT / "decisions.jsonl"
CODE_PATTERN = re.compile(r"^\[(R1|R2|RU|E1|E2|E3|E4|E5)\]")
RETAIN_CODES = {"R1", "R2", "RU"}
EXCLUDE_CODES = {"E1", "E2", "E3", "E4", "E5"}


def load_manifest():
    if not MANIFEST.exists():
        raise SystemExit("batch.json not found in current directory")
    return json.loads(MANIFEST.read_text())


def load_decisions():
    if not OUTPUT.exists():
        return []
    return [json.loads(line) for line in OUTPUT.read_text().splitlines() if line.strip()]


def status():
    manifest = load_manifest()
    decisions = load_decisions()
    expected = {x["record_id"] for x in manifest["records"]}
    received = {x["record_id"] for x in decisions}
    missing = sorted(expected - received)
    print(f"submitted={len(received)}/{len(expected)}")
    if missing:
        print("missing=" + ",".join(missing))
    raise SystemExit(0 if not missing and len(decisions) == len(expected) else 1)


def submit(record_id, outcome, reason):
    manifest = load_manifest()
    valid_ids = {x["record_id"] for x in manifest["records"]}
    if record_id not in valid_ids:
        raise SystemExit(f"unknown record_id: {record_id}")
    if outcome not in {"retain", "exclude"}:
        raise SystemExit("outcome must be retain or exclude")
    reason = " ".join(reason.split())
    if not reason or len(reason) > 240:
        raise SystemExit("reason must contain 1-240 characters")
    code_match = CODE_PATTERN.match(reason)
    if not code_match:
        raise SystemExit("reason must start with a valid decision code")
    code = code_match.group(1)
    if outcome == "retain" and code not in RETAIN_CODES:
        raise SystemExit("retain requires R1, R2, or RU")
    if outcome == "exclude" and code not in EXCLUDE_CODES:
        raise SystemExit("exclude requires E1, E2, E3, E4, or E5")
    existing = load_decisions()
    if any(x["record_id"] == record_id for x in existing):
        raise SystemExit(f"decision already submitted: {record_id}")
    item = {"record_id": record_id, "outcome": outcome, "reason": reason}
    fd = os.open(OUTPUT, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    with os.fdopen(fd, "a") as handle:
        handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"accepted {record_id} ({len(existing) + 1}/{len(valid_ids)})")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "status":
        status()
    if len(sys.argv) != 4:
        raise SystemExit("usage: submit_screening RECORD_ID retain|exclude 'SHORT REASON'")
    submit(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
