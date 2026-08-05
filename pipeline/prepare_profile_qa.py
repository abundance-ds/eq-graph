#!/usr/bin/env python3
"""Prepare simple binary QA batches for unflagged chosen author profiles."""

import csv
import hashlib
import json
import pathlib
from collections import Counter


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
OUT = SCALE / "profile-qa-v1"
BATCH_SIZE = 5


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def suffix(value):
    return (value or "").rsplit("/", 1)[-1]


def work_examples(works):
    def key_recent(work):
        return (-(work.get("publication_year") or 0), work.get("title") or "")

    def key_old(work):
        return (work.get("publication_year") or 9999, work.get("title") or "")

    def key_cited(work):
        return (-(work.get("cited_by_count") or 0), work.get("title") or "")

    chosen = []
    for group in [
        sorted(works, key=key_recent)[:6],
        sorted(works, key=key_old)[:4],
        sorted(works, key=key_cited)[:8],
    ]:
        for work in group:
            work_id = suffix(work.get("id"))
            if work_id and all(item["openalex_id"] != work_id for item in chosen):
                location = work.get("primary_location") or {}
                source = location.get("source") or {}
                chosen.append({
                    "openalex_id": work_id,
                    "year": work.get("publication_year"),
                    "title": work.get("title") or "",
                    "type": work.get("type") or "",
                    "venue": source.get("display_name") or "",
                    "cited_by_count": work.get("cited_by_count") or 0,
                    "topics": [
                        topic.get("display_name") or ""
                        for topic in (work.get("topics") or [])[:3]
                    ],
                })
    return chosen


def profile_evidence(row, projects_by_id):
    path = ROOT / row["cached_profile_path"]
    payload = json.loads(path.read_text())
    works = payload["works"]
    topics = Counter(
        topic.get("display_name") or ""
        for work in works
        for topic in (work.get("topics") or [])[:3]
        if topic.get("display_name")
    )
    coauthors = Counter()
    for work in works:
        for authorship in work.get("authorships") or []:
            author = authorship.get("author") or {}
            author_id = suffix(author.get("id"))
            if author_id and author_id != row["chosen_id"] and author.get("display_name"):
                coauthors[author["display_name"]] += 1
    projects = []
    for project_id in [value for value in row["project_ids"].split(";") if value]:
        project = projects_by_id[project_id]
        projects.append({
            "project_id": project_id,
            "title": project["Title"],
            "working_group": project["Working Group"],
        })
    return {
        "name": row["name"],
        "member_affiliation": row["member_affiliation"],
        "is_member": row["is_member"] == "1",
        "projects": projects,
        "chosen_profile": {
            "openalex_id": row["chosen_id"],
            "display_name": row["chosen_name"],
            "orcid": row["orcid"],
            "reported_affiliation": row["affiliation"],
            "works_count": len(works),
            "top_topics": [
                {"topic": topic, "works": count}
                for topic, count in topics.most_common(12)
            ],
            "frequent_coauthors": [
                {"name": name, "works": count}
                for name, count in coauthors.most_common(12)
            ],
            "work_examples": work_examples(works),
        },
    }


def render(system, records):
    return "\n".join([
        system,
        "",
        "# Profiles",
        "",
        f"Assess all {len(records)} people.",
        "",
        json.dumps(records, ensure_ascii=False, indent=2),
        "",
    ])


def main():
    selection_path = OUT / "selection.json"
    if selection_path.exists():
        raise SystemExit(f"selection already exists: {selection_path}")
    system = (OUT / "SYSTEM.md").read_text()
    prompt_hash = hashlib.sha256(system.encode()).hexdigest()
    readiness = [
        row for row in read_csv(SCALE / "profile-scale-readiness.csv")
        if row["scale_status"] == "ready"
    ]
    projects_by_id = {
        row["Project Id"]: row
        for row in read_csv(ROOT / "data" / "funded-projects-canonical.csv")
    }
    records = [profile_evidence(row, projects_by_id) for row in readiness]
    records.sort(key=lambda row: row["name"].casefold())
    OUT.mkdir(parents=True, exist_ok=True)
    batches = []
    for index in range(0, len(records), BATCH_SIZE):
        batch_records = records[index:index + BATCH_SIZE]
        batch_id = f"batch-{index // BATCH_SIZE + 1:02d}"
        folder = OUT / batch_id
        folder.mkdir()
        payload = {
            "batch_id": batch_id,
            "prompt_sha256": prompt_hash,
            "records": [{
                "name": row["name"],
                "openalex_id": row["chosen_profile"]["openalex_id"],
            } for row in batch_records],
        }
        (folder / "batch.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        )
        (folder / "input.md").write_text(render(system, batch_records))
        wrapper = folder / "submit_profile"
        wrapper.write_text(
            "#!/bin/sh\nexec python3 "
            + str(ROOT / "pipeline" / "submit_profile_qa.py")
            + ' "$@"\n'
        )
        wrapper.chmod(0o755)
        batches.append({
            "batch_id": batch_id,
            "names": [row["name"] for row in batch_records],
        })
    selection_path.write_text(json.dumps({
        "prompt_sha256": prompt_hash,
        "method": "Binary identity QA for every unflagged chosen profile.",
        "records": len(records),
        "batches": batches,
    }, indent=2) + "\n")
    print(json.dumps({
        "records": len(records),
        "batches": len(batches),
        "prompt_sha256": prompt_hash,
    }, indent=2))


if __name__ == "__main__":
    main()
