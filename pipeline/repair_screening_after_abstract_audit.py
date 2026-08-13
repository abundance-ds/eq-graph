#!/usr/bin/env python3
"""Remove invalid-abstract records from a partial production screen and prepare resume inputs."""

import csv
import hashlib
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
SCREEN = PILOT / "screening-final"
SYSTEM = (PILOT / "screening-v3" / "SYSTEM.md").read_text()

sys.path.insert(0, str(ROOT / "pipeline"))
from prepare_screening_pilot import render_records  # noqa: E402


def main():
    invalid = {
        row["record_id"]
        for row in csv.DictReader((PILOT / "abstract-invalid.csv").open())
    }
    works = {
        work["record_id"]: work
        for work in json.loads((PILOT / "derived" / "works.json").read_text())
    }
    selection_path = SCREEN / "selection.json"
    selection = json.loads(selection_path.read_text())
    removed = []
    resume = {}
    for batch in selection["batches"]:
        batch_id = batch["batch_id"]
        folder = SCREEN / batch_id
        manifest_path = folder / "batch.json"
        manifest = json.loads(manifest_path.read_text())
        original_ids = [item["record_id"] for item in manifest["records"]]
        revised_records = [
            item for item in manifest["records"] if item["record_id"] not in invalid
        ]
        removed.extend(record_id for record_id in original_ids if record_id in invalid)
        manifest["records"] = revised_records
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        batch["record_ids"] = [item["record_id"] for item in revised_records]

        output = folder / "decisions.jsonl"
        received = {
            json.loads(line)["record_id"]
            for line in output.read_text().splitlines() if line.strip()
        } if output.exists() else set()
        expected = set(batch["record_ids"])
        if not received <= expected:
            raise SystemExit(f"{batch_id} has decisions for removed or unknown records")
        missing = [record_id for record_id in batch["record_ids"] if record_id not in received]
        if missing:
            original_input = folder / "input.md"
            preserved_input = folder / "input-attempt-01.md"
            if not preserved_input.exists():
                original_input.rename(preserved_input)
            original_input.write_text(
                SYSTEM + "\n\n" + render_records([works[record_id] for record_id in missing])
            )
            resume[batch_id] = len(missing)

    selection["abstract_quality_exclusions"] = sorted(set(removed))
    selection["records_after_abstract_quality_gate"] = sum(
        len(batch["record_ids"]) for batch in selection["batches"]
    )
    selection["prompt_sha256"] = hashlib.sha256(SYSTEM.encode()).hexdigest()
    selection_path.write_text(json.dumps(selection, indent=2) + "\n")
    print(json.dumps({
        "removed": sorted(set(removed)),
        "records_after_gate": selection["records_after_abstract_quality_gate"],
        "resume_batches": resume,
    }, indent=2))


if __name__ == "__main__":
    main()
