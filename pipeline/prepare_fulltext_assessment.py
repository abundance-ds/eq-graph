#!/usr/bin/env python3
"""Prepare full-text batches with a complete rule-based project candidate set."""

import argparse
import csv
import hashlib
import json
import pathlib
import random
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
BATCH_SIZE = 1
SEED = 20260806


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-version", default="v1-sample")
    parser.add_argument("--prompt-version", default="v1")
    parser.add_argument("--sample", type=int, default=12, help="0 means all available full texts")
    parser.add_argument("--seed", type=int, default=SEED)
    return parser.parse_args()


def project_candidates(work, text, projects, project_by_id, people):
    exact = {
        project_id
        for project_id in project_by_id
        if project_id.upper() in text.upper()
    }
    person_ids = set()
    for person in work["authors"]:
        person_ids.update(people.get(person, []))
    selected = sorted(exact) + sorted(person_ids - exact)
    return [{
        "project_id": project_id,
        "exact_id_in_text": project_id in exact,
        "title": project_by_id[project_id]["Title"],
        "abstract": project_by_id[project_id]["Abstract"],
        "pi": project_by_id[project_id]["Project PI / Applicant Name"],
        "working_group": project_by_id[project_id]["Working Group"],
        "start_year": project_by_id[project_id]["Start Year"],
        "end_year": project_by_id[project_id]["End Year"],
    } for project_id in selected]


def evidence_text(value):
    limit = 120_000
    if len(value) <= limit:
        return value
    intervals = [(0, 50_000), (len(value) - 30_000, len(value))]
    pattern = re.compile(r"euroqol|fund(?:ed|ing)?|grant|acknowledg|project\s+(?:id|number|no\.)", re.I)
    for match in list(pattern.finditer(value))[:12]:
        intervals.append((max(0, match.start() - 2500), min(len(value), match.end() + 3500)))
    intervals.sort()
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))
    parts = [
        f"[FULL-TEXT EXCERPT {start}:{end} OF {len(value)} CHARACTERS]\n{value[start:end]}"
        for start, end in merged
    ]
    return "\n\n".join(parts)


def render(system, records):
    parts = [system, "", "# Articles", "", f"Assess all {len(records)} articles below.", ""]
    for item in records:
        work = item["work"]
        parts.extend([
            f"## {work['record_id']}", "",
            f"- Title: {work['title']}",
            f"- Year: {work.get('year') or '[missing]'}",
            f"- DOI: {work.get('doi') or '[missing]'}",
            f"- Linked people: {', '.join(work['authors'])}",
            f"- Title/abstract screen code: {item['screen_code']}", "",
            "### Candidate funded projects", "",
            json.dumps(item["candidates"], ensure_ascii=False, indent=2), "",
            "### Article full text", "",
            item["text"], "",
        ])
    return "\n".join(parts)


def main():
    args = parse_args()
    output = PILOT / f"fulltext-assessment-{args.output_version}"
    prompt_path = PILOT / f"fulltext-assessment-{args.prompt_version}" / "SYSTEM.md"
    selection_path = output / "selection.json"
    if selection_path.exists():
        raise SystemExit(f"selection already exists and will not be overwritten: {selection_path}")
    system = prompt_path.read_text()
    prompt_hash = hashlib.sha256(system.encode()).hexdigest()
    manifest = {
        row["record_id"]: row
        for row in csv.DictReader((PILOT / "fulltext" / "manifest.csv").open(newline=""))
        if row["status"] == "available"
    }
    works = {
        work["record_id"]: work
        for work in json.loads((PILOT / "derived" / "works.json").read_text())
    }
    projects = list(csv.DictReader((ROOT / "data" / "funded-projects-canonical.csv").open(newline="")))
    project_by_id = {project["Project Id"]: project for project in projects}
    people = {}
    for row in csv.DictReader((ROOT / "artefacts" / "01_people.csv").open(newline="")):
        people[row["name"]] = [value for value in row["project_ids"].split(";") if value]

    ids = sorted(manifest)
    if args.sample:
        rng = random.Random(args.seed)
        by_code = {}
        for record_id in ids:
            by_code.setdefault(manifest[record_id]["screen_code"], []).append(record_id)
        chosen = []
        for code in sorted(by_code):
            rng.shuffle(by_code[code])
            chosen.extend(by_code[code][:min(4, len(by_code[code]))])
        remaining = [record_id for record_id in ids if record_id not in chosen]
        rng.shuffle(remaining)
        ids = (chosen + remaining)[:args.sample]

    prepared = []
    for record_id in ids:
        work = works[record_id]
        text_path = ROOT / manifest[record_id]["text_path"]
        full_text = text_path.read_text(errors="replace")
        candidates = project_candidates(work, full_text, projects, project_by_id, people)
        prepared.append({
            "work": work,
            "screen_code": manifest[record_id]["screen_code"],
            "candidates": candidates,
            "text": evidence_text(full_text),
        })

    output.mkdir(parents=True, exist_ok=True)
    selection = {
        "output_version": args.output_version,
        "prompt_version": args.prompt_version,
        "prompt_sha256": prompt_hash,
        "seed": args.seed,
        "method": "Stratified prompt check" if args.sample else "All available full texts",
        "available_full_texts": len(manifest),
        "selected": len(prepared),
        "batches": [],
    }
    for index in range(0, len(prepared), BATCH_SIZE):
        records = prepared[index:index + BATCH_SIZE]
        batch_id = f"batch-{index // BATCH_SIZE + 1:02d}"
        folder = output / batch_id
        folder.mkdir()
        payload = {
            "batch_id": batch_id,
            "prompt_sha256": prompt_hash,
            "records": [{
                "record_id": item["work"]["record_id"],
                "title": item["work"]["title"],
                "candidate_project_ids": [project["project_id"] for project in item["candidates"]],
            } for item in records],
        }
        (folder / "batch.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        (folder / "input.md").write_text(render(system, records))
        wrapper = folder / "submit_assessment"
        wrapper.write_text(
            "#!/bin/sh\nexec python3 " + str(ROOT / "pipeline" / "submit_fulltext_assessment.py") + ' "$@"\n'
        )
        wrapper.chmod(0o755)
        selection["batches"].append({
            "batch_id": batch_id,
            "record_ids": [item["work"]["record_id"] for item in records],
        })
    selection_path.write_text(json.dumps(selection, indent=2) + "\n")
    print(json.dumps({
        "selected": len(prepared),
        "batches": len(selection["batches"]),
        "prompt_sha256": prompt_hash,
    }, indent=2))


if __name__ == "__main__":
    main()
