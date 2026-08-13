#!/usr/bin/env python3
"""Prepare scale screening or its validation set with full abstract text."""

import argparse
import csv
import hashlib
import json
import pathlib
import random


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
SCALE = ROOT / "scale" / "protocol-2.0"
BATCH_SIZE = 20
SEED = 20260804


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v1")
    parser.add_argument("--validation", action="store_true")
    return parser.parse_args()


def scale_prompt():
    system = (PILOT / "screening-v3" / "SYSTEM.md").read_text()
    old_rule = (
        "- Every record must contain a real abstract. If one does not, stop and report an\n"
        "  invalid input. Do not decide from the title alone."
    )
    new_rule = (
        "- If the supplied text is not a usable article abstract, exclude it with E5. "
        "Examples include an author list, citation list, database placeholder, publisher "
        "boilerplate, or incomplete fragment. Do not infer relevance from the title alone."
    )
    if system.count(old_rule) != 1:
        raise RuntimeError("frozen v3 abstract rule not found exactly once")
    system = system.replace(
        "# EuroQol title and abstract screen v3",
        "# EuroQol title and abstract screen scale v1",
        1,
    ).replace(old_rule, new_rule, 1)
    system = system.replace(
        "- `[E5]`: The publication format is ineligible.",
        "- `[E5]`: The publication format or supplied abstract field is ineligible.",
        1,
    )
    return system


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def validation_records():
    works = {
        record["record_id"]: record
        for record in json.loads((PILOT / "derived" / "works.json").read_text())
    }
    references = []
    for name in ["screening-v3", "screening-v3-boundary"]:
        references.extend(read_csv(PILOT / name / "reference.csv"))
    invalid = read_csv(PILOT / "abstract-invalid.csv")
    for row in invalid:
        references.append({
            "batch_id": "",
            "record_id": row["record_id"],
            "human_outcome": "exclude",
            "human_code": "E5",
            "human_reason": "The supplied field is not a usable article abstract.",
            "notes": row["reason"],
        })
    records = []
    for reference in references:
        work = works[reference["record_id"]]
        records.append({
            "record_id": work["record_id"],
            "title": work["title"],
            "year": work.get("year"),
            "linked_people": work.get("authors") or [],
            "abstract": work.get("abstract") or "",
            "reference": reference,
        })
    random.Random(SEED).shuffle(records)
    return records


def production_records(version):
    evaluation = SCALE / f"screening-{version}-validation" / "evaluation.json"
    if not evaluation.exists():
        raise SystemExit("scale screening validation is not complete")
    result = json.loads(evaluation.read_text())
    if not result.get("pilot_gate", {}).get("passed"):
        raise SystemExit("scale screening validation did not pass")
    if result.get("false_exclusions") or result.get("false_inclusions"):
        raise SystemExit("scale screening validation has outcome errors")
    records = [json.loads(line) for line in (SCALE / "article-corpus.jsonl").open()]
    return [record for record in records if record["abstract_length_gate"]]


def render(system, records):
    parts = [system, "", "# Batch records", ""]
    for record in records:
        abstract = record["abstract"].strip()
        if len(abstract) < 80:
            raise ValueError(f"record lacks 80 abstract characters: {record['record_id']}")
        parts.extend([
            f"## {record['record_id']}",
            "",
            f"- Year: {record.get('year') or '[missing]'}",
            f"- Linked people: {', '.join(record['linked_people'])}",
            f"- Title: {record['title']}",
            "",
            "Abstract:",
            "",
            abstract,
            "",
        ])
    return "\n".join(parts)


def main():
    args = parse_args()
    suffix = "-validation" if args.validation else ""
    screen = SCALE / f"screening-{args.version}{suffix}"
    selection_path = screen / "selection.json"
    if selection_path.exists():
        raise SystemExit(f"selection already exists: {selection_path}")
    records = validation_records() if args.validation else production_records(args.version)
    system = scale_prompt()
    prompt_hash = hashlib.sha256(system.encode()).hexdigest()
    screen.mkdir(parents=True, exist_ok=False)
    (screen / "SYSTEM.md").write_text(system)

    selections = []
    reference_rows = []
    for start in range(0, len(records), BATCH_SIZE):
        batch_records = records[start:start + BATCH_SIZE]
        batch_id = f"batch-{start // BATCH_SIZE + 1:04d}"
        folder = screen / batch_id
        folder.mkdir()
        batch = {
            "batch_id": batch_id,
            "version": args.version,
            "prompt_sha256": prompt_hash,
            "records": [{
                "record_id": record["record_id"],
                "title": record["title"],
                "year": record.get("year"),
                "linked_people": record["linked_people"],
            } for record in batch_records],
        }
        (folder / "batch.json").write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n")
        (folder / "input.md").write_text(render(system, batch_records))
        wrapper = folder / "submit_screening"
        wrapper.write_text(
            "#!/bin/sh\nexec python3 "
            + str(ROOT / "pipeline" / "submit_screening.py")
            + ' "$@"\n'
        )
        wrapper.chmod(0o755)
        selections.append({
            "batch_id": batch_id,
            "record_ids": [record["record_id"] for record in batch_records],
        })
        for record in batch_records:
            if "reference" in record:
                reference_rows.append({
                    **record["reference"],
                    "batch_id": batch_id,
                })

    selection = {
        "version": args.version,
        "validation": args.validation,
        "source_prompt": "pilot/protocol-2.0/screening-v3/SYSTEM.md",
        "prompt_sha256": prompt_hash,
        "seed": SEED if args.validation else None,
        "batch_size": BATCH_SIZE,
        "records": len(records),
        "abstract_rule": "Full stored text; minimum 80 characters; no truncation.",
        "batches": selections,
    }
    selection_path.write_text(json.dumps(selection, indent=2) + "\n")
    if args.validation:
        fields = [
            "batch_id", "record_id", "human_outcome", "human_code",
            "human_reason", "notes",
        ]
        with (screen / "reference.csv").open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows({field: row.get(field, "") for field in fields} for row in reference_rows)
    print(json.dumps({
        "screen": str(screen.relative_to(ROOT)),
        "records": len(records),
        "batches": len(selections),
        "prompt_sha256": prompt_hash,
    }, indent=2))


if __name__ == "__main__":
    main()
