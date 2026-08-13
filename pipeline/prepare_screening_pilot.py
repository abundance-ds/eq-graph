#!/usr/bin/env python3
"""Prepare fresh deterministic random batches for prompt calibration."""

import argparse
import hashlib
import json
import pathlib
import random
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
DEFAULT_SEED = 20260804
BATCH_SIZE = 20
EQ_TERM = re.compile(
    r"\b(?:eq[- ]?5d(?:[- ]?(?:3l|5l|y))?|euroqol|eq[- ]?vt|eq[- ]?hwb|"
    r"eq[- ]?tips|eq[- ]?tandi)\b", re.I,
)
METHOD_TERM = re.compile(
    r"\b(?:value set|tariff|time trade[- ]?off|standard gamble|health[- ]state "
    r"valu|preference[- ]based|mapping|crosswalk|psychometric|content validity|"
    r"construct validity|responsiveness|discrete choice|dce)\b", re.I,
)
FALSE_FRIEND = re.compile(
    r"\b(?:quality of life|hrqol|qaly|qalys|utilit|prom|preference|valuation|"
    r"cost[- ]effectiveness|budget impact)\b", re.I,
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v3")
    parser.add_argument("--prompt-version")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--batches", type=int, default=3)
    parser.add_argument(
        "--sample", choices=["random", "boundary", "full"], default="random"
    )
    return parser.parse_args()


def historical_ids(current_screen):
    record_ids = set()
    for path in sorted(PILOT.glob("screening-v*/selection.json")):
        if path.parent == current_screen:
            continue
        data = json.loads(path.read_text())
        for batch in data.get("batches", []):
            record_ids.update(batch.get("record_ids", []))
    return record_ids


def choose_batches(works, excluded, seed, batch_count):
    pool = [work for work in works if work["record_id"] not in excluded]
    required = BATCH_SIZE * batch_count
    if len(pool) < required:
        raise SystemExit(f"need {required} fresh records; found {len(pool)}")
    rng = random.Random(seed)
    selected = rng.sample(pool, required)
    return [selected[i:i + BATCH_SIZE] for i in range(0, required, BATCH_SIZE)]


def choose_boundary_batches(works, excluded, seed, batch_count):
    available = [work for work in works if work["record_id"] not in excluded]
    strata = {name: [] for name in ["eq_method", "eq_other", "method_no_eq", "false_friend"]}
    for work in available:
        text = work["title"] + " " + work["abstract"]
        has_eq = bool(EQ_TERM.search(text))
        has_method = bool(METHOD_TERM.search(text))
        if has_eq and has_method:
            strata["eq_method"].append(work)
        elif has_eq:
            strata["eq_other"].append(work)
        elif has_method:
            strata["method_no_eq"].append(work)
        elif FALSE_FRIEND.search(text):
            strata["false_friend"].append(work)
    rng = random.Random(seed)
    for pool in strata.values():
        rng.shuffle(pool)
    batches = []
    for _ in range(batch_count):
        batch = []
        for name, pool in strata.items():
            if len(pool) < 5:
                raise SystemExit(f"boundary stratum {name} has fewer than 5 fresh records")
            for work in pool[:5]:
                item = dict(work)
                item["sampling_stratum"] = name
                batch.append(item)
            del pool[:5]
        rng.shuffle(batch)
        batches.append(batch)
    return batches


def render_records(records):
    parts = [
        "# Batch records", "",
        f"Screen all {len(records)} records below using `./submit_screening`.", "",
    ]
    for record in records:
        abstract = record["abstract"].strip()
        if len(abstract) < 80:
            raise ValueError(f"screening record lacks a usable abstract: {record['record_id']}")
        parts.extend([
            f"## {record['record_id']}", "",
            f"- Year: {record.get('year') or '[missing]'}",
            f"- Linked people: {', '.join(record['authors'])}",
            f"- Title: {record['title']}", "",
            "Abstract:", "", abstract, "",
        ])
    return "\n".join(parts)


def main():
    args = parse_args()
    screen = PILOT / f"screening-{args.version}"
    prompt_version = args.prompt_version or args.version
    system_path = PILOT / f"screening-{prompt_version}" / "SYSTEM.md"
    selection_path = screen / "selection.json"
    if not system_path.exists():
        raise SystemExit(f"prompt not found: {system_path}")
    if selection_path.exists():
        raise SystemExit(f"selection already exists and will not be overwritten: {selection_path}")

    system = system_path.read_text()
    prompt_hash = hashlib.sha256(system.encode()).hexdigest()
    works = [
        work for work in json.loads((PILOT / "derived" / "works.json").read_text())
        if work.get("eligibility_status") == "candidate_full_journal_article"
        and work.get("screening_ready")
    ]
    invalid = [
        work["record_id"] for work in works
        if len((work.get("abstract") or "").strip()) < 80
    ]
    if invalid:
        raise SystemExit(f"invalid screening corpus: {len(invalid)} records lack abstracts")

    excluded = historical_ids(screen)
    excluded_count = 0 if args.sample == "full" else len(excluded)
    if args.sample == "full":
        batches = [
            works[index:index + BATCH_SIZE]
            for index in range(0, len(works), BATCH_SIZE)
        ]
        sample_method = "Complete screening-ready corpus in stable corpus order."
    elif args.sample == "boundary":
        batches = choose_boundary_batches(works, excluded, args.seed, args.batches)
        sample_method = (
            "Random sample within four boundary strata: EQ plus method term, EQ without "
            "method term, method term without EQ, and other false-friend term."
        )
    else:
        batches = choose_batches(works, excluded, args.seed, args.batches)
        sample_method = "Simple random sample without replacement from all screening-ready articles."
    selection = {
        "version": args.version,
        "prompt_version": prompt_version,
        "prompt_sha256": prompt_hash,
        "seed": args.seed,
        "batch_size": BATCH_SIZE,
        "method": sample_method,
        "historical_records_excluded": excluded_count,
        "eligible_records": len(works),
        "batches": [],
    }
    for number, records in enumerate(batches, 1):
        batch_id = f"batch-{number:02d}"
        folder = screen / batch_id
        folder.mkdir(parents=True, exist_ok=False)
        payload = {
            "batch_id": batch_id,
            "version": args.version,
            "seed": args.seed,
            "prompt_sha256": prompt_hash,
            "records": [{
                "record_id": work["record_id"],
                "title": work["title"],
                "year": work["year"],
                "linked_people": work["authors"],
                "sampling_stratum": work.get("sampling_stratum", "random"),
            } for work in records],
        }
        (folder / "batch.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        )
        (folder / "input.md").write_text(system + "\n\n" + render_records(records))
        wrapper = folder / "submit_screening"
        wrapper.write_text(
            "#!/bin/sh\nexec python3 "
            + str(ROOT / "pipeline" / "submit_screening.py") + ' "$@"\n'
        )
        wrapper.chmod(0o755)
        selection["batches"].append({
            "batch_id": batch_id,
            "record_ids": [work["record_id"] for work in records],
        })

    selection_path.write_text(json.dumps(selection, indent=2) + "\n")
    print(json.dumps({
        "version": args.version,
        "prompt_sha256": prompt_hash,
        "historical_records_excluded": excluded_count,
        "batches": {
            batch["batch_id"]: len(batch["record_ids"])
            for batch in selection["batches"]
        },
    }, indent=2))


if __name__ == "__main__":
    main()
