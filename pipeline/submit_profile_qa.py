#!/usr/bin/env python3
"""Validated submission tool for one profile-QA batch."""

import json
import os
import pathlib
import sys


ROOT = pathlib.Path.cwd()
MANIFEST = ROOT / "batch.json"
OUTPUT = ROOT / "decisions.jsonl"
DECISIONS = {"accept", "hold"}


def manifest():
    if not MANIFEST.exists():
        raise SystemExit("batch.json not found in current directory")
    return json.loads(MANIFEST.read_text())


def decisions():
    if not OUTPUT.exists():
        return []
    return [json.loads(line) for line in OUTPUT.read_text().splitlines() if line.strip()]


def status():
    expected = {item["name"] for item in manifest()["records"]}
    completed = decisions()
    received = {item["name"] for item in completed}
    missing = sorted(expected - received)
    print(f"submitted={len(received)}/{len(expected)}")
    if missing:
        print("missing=" + ";".join(missing))
    raise SystemExit(0 if not missing and len(completed) == len(expected) else 1)


def submit(args):
    name, decision, reason = args
    expected = {item["name"] for item in manifest()["records"]}
    if name not in expected:
        raise SystemExit(f"unknown person: {name}")
    if decision not in DECISIONS:
        raise SystemExit("decision must be accept or hold")
    if not reason.strip() or len(reason) > 400:
        raise SystemExit("reason must contain 1-400 characters")
    existing = decisions()
    if any(item["name"] == name for item in existing):
        raise SystemExit(f"decision already submitted: {name}")
    item = {
        "name": name,
        "decision": decision,
        "reason": " ".join(reason.split()),
    }
    descriptor = os.open(OUTPUT, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    with os.fdopen(descriptor, "a") as handle:
        handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"accepted {name}: {decision}")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "status":
        status()
    if len(sys.argv) != 4:
        raise SystemExit('usage: submit_profile "PERSON_NAME" DECISION "REASON"')
    submit(sys.argv[1:])


if __name__ == "__main__":
    main()
