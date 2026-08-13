#!/usr/bin/env python3
"""Prepare a focused audit of records with reported EuroQol support."""

import csv
import hashlib
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
OUT = PILOT / "funding-audit-v1"
BATCH_SIZE = 8


def extracts(text):
    intervals = []
    for match in re.finditer(r"euroqol", text, re.I):
        intervals.append((max(0, match.start() - 1800), min(len(text), match.end() + 2200)))
    if not intervals:
        return text[-12000:]
    intervals.sort()
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))
    return "\n\n".join(text[start:end] for start, end in merged[:12])


def main():
    selection = OUT / "selection.json"
    if selection.exists():
        raise SystemExit("funding audit selection already exists")
    system = (OUT / "SYSTEM.md").read_text()
    prompt_hash = hashlib.sha256(system.encode()).hexdigest()
    assessment = [
        row for row in csv.DictReader((PILOT / "fulltext-assessment-v1-final" / "results.csv").open(newline=""))
        if row["funding"] == "explicit_euroqol"
    ]
    manifest = {
        row["record_id"]: row
        for row in csv.DictReader((PILOT / "fulltext" / "manifest.csv").open(newline=""))
    }
    OUT.mkdir(parents=True, exist_ok=True)
    batches = []
    for index in range(0, len(assessment), BATCH_SIZE):
        records = assessment[index:index + BATCH_SIZE]
        batch_id = f"batch-{index // BATCH_SIZE + 1:02d}"
        folder = OUT / batch_id
        folder.mkdir()
        payload = {
            "batch_id": batch_id,
            "prompt_sha256": prompt_hash,
            "records": [{"record_id": row["record_id"], "title": row["title"]} for row in records],
        }
        (folder / "batch.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        parts = [system, "", "# Articles", ""]
        for row in records:
            text = (ROOT / manifest[row["record_id"]]["text_path"]).read_text(errors="replace")
            parts.extend([
                f"## {row['record_id']}", "",
                f"- Title: {row['title']}",
                f"- Prior funding evidence: {row['funding_evidence']}", "",
                "Relevant full-text extracts:", "", extracts(text), "",
            ])
        (folder / "input.md").write_text("\n".join(parts))
        wrapper = folder / "submit_funding"
        wrapper.write_text("#!/bin/sh\nexec python3 " + str(ROOT / "pipeline" / "submit_funding_audit.py") + ' "$@"\n')
        wrapper.chmod(0o755)
        batches.append({"batch_id": batch_id, "record_ids": [row["record_id"] for row in records]})
    selection.write_text(json.dumps({
        "prompt_sha256": prompt_hash,
        "records": len(assessment),
        "batches": batches,
    }, indent=2) + "\n")
    print(json.dumps({"records": len(assessment), "batches": len(batches), "prompt_sha256": prompt_hash}, indent=2))


if __name__ == "__main__":
    main()
