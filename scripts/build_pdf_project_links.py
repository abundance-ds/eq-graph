#!/usr/bin/env python3
"""Build audited project links for the local PDF tranche."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--projects", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--review-output", type=Path, required=True)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def publication_year(metadata: dict[str, Any]) -> int | None:
    years = [
        int(match.group())
        for row in metadata.get("dates", [])
        if (match := re.search(r"(?:19|20)\d{2}", row.get("value", "")))
    ]
    return min(years) if years else None


def main() -> None:
    args = parse_args()
    with args.projects.open(encoding="utf-8-sig", newline="") as handle:
        projects = {row["Project Id"].strip(): row for row in csv.DictReader(handle)}

    accepted: list[dict[str, Any]] = []
    review: list[dict[str, Any]] = []
    for row in read_tsv(args.manifest.resolve()):
        metadata_path = Path(row["metadata_path"])
        if not metadata_path.is_absolute():
            metadata_path = Path.cwd() / metadata_path
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        publication = metadata["publication"]
        year = publication_year(metadata)
        for source_path in row["metadata_source_paths"].split(";"):
            discovery = json.loads(Path(source_path).read_text(encoding="utf-8"))
            project_id = discovery["project_id"]
            project = projects.get(project_id)
            matches = [
                item
                for item in discovery.get("accepted", [])
                if item.get("work_id") == row["work_id"]
            ]
            reasons: list[str] = []
            if project is None:
                reasons.append("project is absent from the project register")
            if len(matches) != 1:
                reasons.append(f"accepted discovery matches={len(matches)}")
            start_year = int(project["Start Year"]) if project and project["Start Year"] else None
            if year is None:
                reasons.append("publication year is absent")
            elif start_year is not None and start_year > year:
                reasons.append(f"project starts in {start_year} after publication year {year}")
            evidence = matches[0].get("evidence", []) if len(matches) == 1 else []
            strong_kinds = {
                "grant_id_structured",
                "grant_id_acknowledged",
                "grant_id_fulltext",
                "title_exact",
            }
            if not any(item.get("kind") in strong_kinds for item in evidence):
                reasons.append("no accepted direct grant or exact-title evidence")
            evidence_text = "; ".join(
                item.get("detail") or item.get("kind") or "unspecified evidence"
                for item in evidence
            )
            output_row = {
                "project_id": project_id,
                "publication_id": publication["publication_id"],
                "project_output": "yes",
                "support_target": "study",
                "support_scope": evidence_text,
                "evidence_status": "project-discovery-direct-v1",
                "publication_year": year or "",
                "project_start_year": start_year or "",
                "review_reason": " | ".join(reasons),
            }
            (review if reasons else accepted).append(output_row)

    fields = [
        "project_id",
        "publication_id",
        "project_output",
        "support_target",
        "support_scope",
        "evidence_status",
        "publication_year",
        "project_start_year",
        "review_reason",
    ]
    for path, rows in ((args.output, accepted), (args.review_output, review)):
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=fields,
                delimiter="\t",
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps({"accepted": len(accepted), "review": len(review)}, indent=2))


if __name__ == "__main__":
    main()
