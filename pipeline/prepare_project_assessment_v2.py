#!/usr/bin/env python3
"""Prepare a complete-candidate audit of truncated pilot project assessments."""

import argparse
import csv
import hashlib
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v3")
    return parser.parse_args()


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def complete_candidates(work, text, project_by_id, projects_by_person):
    exact = {
        project_id
        for project_id in project_by_id
        if project_id.upper() in text.upper()
    }
    linked = set()
    for person in work["authors"]:
        linked.update(projects_by_person.get(person, []))
    project_ids = sorted(exact) + sorted(linked - exact)
    return [{
        "project_id": project_id,
        "exact_id_in_text": project_id in exact,
        "title": project_by_id[project_id]["Title"],
        "abstract": project_by_id[project_id]["Abstract"],
        "pi": project_by_id[project_id]["Project PI / Applicant Name"],
        "working_group": project_by_id[project_id]["Working Group"],
        "start_year": project_by_id[project_id]["Start Year"],
        "end_year": project_by_id[project_id]["End Year"],
    } for project_id in project_ids]


def render(system, work, text, candidates, prior):
    return "\n".join([
        system,
        "",
        "# Article",
        "",
        f"- Record ID: {work['record_id']}",
        f"- Title: {work['title']}",
        f"- Year: {work.get('year') or '[missing]'}",
        f"- Linked people: {', '.join(work['authors'])}",
        f"- Prior incomplete-candidate decision: {prior['project_link']}",
        f"- Prior selected project IDs: {prior['project_ids'] or 'none'}",
        "",
        "## Complete project candidate set",
        "",
        json.dumps(candidates, ensure_ascii=False, indent=2),
        "",
        "## Full article text",
        "",
        text,
        "",
    ])


def main():
    args = parse_args()
    output = PILOT / f"project-assessment-{args.version}"
    selection_path = output / "selection.json"
    if selection_path.exists():
        raise SystemExit(f"selection already exists: {selection_path}")
    system = (output / "SYSTEM.md").read_text()
    prompt_hash = hashlib.sha256(system.encode()).hexdigest()
    works = {
        work["record_id"]: work
        for work in json.loads((PILOT / "derived" / "works.json").read_text())
    }
    manifest = {
        row["record_id"]: row
        for row in read_csv(PILOT / "fulltext" / "manifest.csv")
        if row["status"] == "available"
    }
    prior = {
        row["record_id"]: row
        for row in read_csv(PILOT / "fulltext-assessment-v1-final" / "results.csv")
    }
    projects = read_csv(ROOT / "data" / "funded-projects-canonical.csv")
    project_by_id = {row["Project Id"]: row for row in projects}
    projects_by_person = {
        row["name"]: [value for value in row["project_ids"].split(";") if value]
        for row in read_csv(ROOT / "artefacts" / "01_people.csv")
    }
    supplied = {}
    for batch_path in sorted((PILOT / "fulltext-assessment-v1-final").glob("batch-*/batch.json")):
        for row in json.loads(batch_path.read_text())["records"]:
            supplied[row["record_id"]] = set(row["candidate_project_ids"])

    output.mkdir(parents=True, exist_ok=True)
    batches = []
    audited = []
    for record_id in sorted(manifest):
        text = (ROOT / manifest[record_id]["text_path"]).read_text(errors="replace")
        candidates = complete_candidates(
            works[record_id], text, project_by_id, projects_by_person
        )
        candidate_ids = {row["project_id"] for row in candidates}
        omitted = sorted(candidate_ids - supplied[record_id])
        if not omitted:
            continue
        batch_id = f"batch-{len(batches) + 1:02d}"
        folder = output / batch_id
        folder.mkdir(exist_ok=True)
        payload = {
            "batch_id": batch_id,
            "prompt_sha256": prompt_hash,
            "records": [{
                "record_id": record_id,
                "title": works[record_id]["title"],
                "candidate_project_ids": [row["project_id"] for row in candidates],
                "prior_candidate_project_ids": sorted(supplied[record_id]),
                "previously_omitted_project_ids": omitted,
            }],
        }
        (folder / "batch.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        )
        (folder / "input.md").write_text(
            render(system, works[record_id], text, candidates, prior[record_id])
        )
        wrapper = folder / "submit_project"
        wrapper.write_text(
            "#!/bin/sh\nexec python3 "
            + str(ROOT / "pipeline" / "submit_project_assessment_v2.py")
            + ' "$@"\n'
        )
        wrapper.chmod(0o755)
        batches.append({"batch_id": batch_id, "record_ids": [record_id]})
        audited.append({
            "record_id": record_id,
            "prior_candidates": len(supplied[record_id]),
            "complete_candidates": len(candidate_ids),
            "omitted_candidates": len(omitted),
        })
    selection_path.write_text(json.dumps({
        "prompt_sha256": prompt_hash,
        "method": (
            "Audit every pilot article for which the prior 12-project cap omitted "
            "one or more rule-based candidates."
        ),
        "candidate_rule": (
            "All projects linked to known article people, plus every canonical project "
            "ID found in the full text. No score and no cap."
        ),
        "records": len(audited),
        "audit": audited,
        "batches": batches,
    }, indent=2) + "\n")
    print(json.dumps({
        "records": len(audited),
        "batches": len(batches),
        "prompt_sha256": prompt_hash,
    }, indent=2))


if __name__ == "__main__":
    main()
