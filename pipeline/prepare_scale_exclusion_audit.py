#!/usr/bin/env python3
"""Prepare a blinded random audit of completed scale-screening exclusions."""

import argparse
import csv
import hashlib
import json
import pathlib
import random


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
SCREEN = SCALE / "screening-v1"
BATCH_SIZE = 20
PRIOR_CHECK_BATCHES = {"batch-0001", "batch-0002", "batch-0003"}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--sample-size", type=int, default=100)
    return parser.parse_args()


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


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
    out = SCALE / f"exclusion-audit-{args.version}"
    if out.exists():
        raise SystemExit(f"audit already exists: {out}")
    progress = json.loads((SCREEN / "progress.json").read_text())
    if not progress.get("ok") or progress.get("submitted_records", 0) < args.sample_size:
        raise SystemExit("current scale-screening checkpoint is not valid")

    previously_audited = set()
    for path in sorted(SCALE.glob("exclusion-audit-*/selection.json")):
        prior = json.loads(path.read_text())
        previously_audited.update(
            record_id for batch in prior["batches"] for record_id in batch["record_ids"]
        )
    results = read_csv(SCREEN / "results.csv")
    pool = [
        row for row in results
        if row["outcome"] == "exclude" and row["batch_id"] not in PRIOR_CHECK_BATCHES
        and row["record_id"] not in previously_audited
    ]
    if len(pool) < args.sample_size:
        raise SystemExit("too few fresh exclusions for the requested audit")
    selected_rows = random.Random(args.seed).sample(
        sorted(pool, key=lambda row: row["record_id"]), args.sample_size
    )
    selected_ids = {row["record_id"] for row in selected_rows}
    corpus = {
        record["record_id"]: record
        for line in (SCALE / "article-corpus.jsonl").open()
        if (record := json.loads(line))["record_id"] in selected_ids
    }
    if set(corpus) != selected_ids:
        raise SystemExit("sample records are missing from the article corpus")

    system = (SCREEN / "SYSTEM.md").read_text()
    prompt_hash = hashlib.sha256(system.encode()).hexdigest()
    records = [corpus[row["record_id"]] for row in selected_rows]
    out.mkdir()
    (out / "SYSTEM.md").write_text(system)
    (out / "TASK.md").write_text(
        "# Independent exclusion audit\n\n"
        "Review only the five batch inputs in this directory. The prior screening "
        "decisions are withheld. Apply `SYSTEM.md` independently and act as a skeptical "
        "false-negative reviewer. Use only the supplied title, metadata, and full stored "
        "abstract. Do not inspect `screening-v1`, other project files, or the web. Submit "
        "one decision for every record with each batch's `submit_screening` command.\n"
    )

    batches = []
    for start in range(0, len(records), BATCH_SIZE):
        batch_records = records[start:start + BATCH_SIZE]
        batch_id = f"batch-{start // BATCH_SIZE + 1:04d}"
        folder = out / batch_id
        folder.mkdir()
        manifest_records = [{
            "record_id": record["record_id"],
            "title": record["title"],
            "year": record.get("year"),
            "linked_people": record["linked_people"],
        } for record in batch_records]
        (folder / "batch.json").write_text(json.dumps({
            "batch_id": batch_id,
            "version": f"exclusion-audit-{args.version}",
            "prompt_sha256": prompt_hash,
            "records": manifest_records,
        }, ensure_ascii=False, indent=2) + "\n")
        (folder / "input.md").write_text(render(system, batch_records))
        wrapper = folder / "submit_screening"
        wrapper.write_text(
            "#!/bin/sh\nexec python3 "
            + str(ROOT / "pipeline" / "submit_screening.py")
            + ' "$@"\n'
        )
        wrapper.chmod(0o755)
        batches.append({
            "batch_id": batch_id,
            "record_ids": [record["record_id"] for record in batch_records],
        })

    selection = {
        "version": f"exclusion-audit-{args.version}",
        "method": "Simple random sample without replacement from completed exclusions.",
        "blinding": "Prior outcomes, codes, and reasons withheld from the reviewer.",
        "seed": args.seed,
        "sample_size": args.sample_size,
        "batch_size": BATCH_SIZE,
        "sampling_frame_exclusions": len(pool),
        "previous_audit_record_ids_excluded": len(previously_audited),
        "excluded_prior_operator_check_batches": sorted(PRIOR_CHECK_BATCHES),
        "production_checkpoint_records": progress["submitted_records"],
        "production_checkpoint_exclusions": progress["excluded"],
        "prompt_sha256": prompt_hash,
        "batches": batches,
    }
    (out / "selection.json").write_text(json.dumps(selection, indent=2) + "\n")
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "sample_size": args.sample_size,
        "sampling_frame_exclusions": len(pool),
        "previous_audit_record_ids_excluded": len(previously_audited),
        "seed": args.seed,
        "prompt_sha256": prompt_hash,
    }, indent=2))


if __name__ == "__main__":
    main()
