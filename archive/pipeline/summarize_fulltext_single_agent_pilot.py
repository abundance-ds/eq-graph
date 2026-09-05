#!/usr/bin/env python3
"""Compare the single-agent pilot with the fixed two-agent baseline."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PRODUCTION = ROOT / "pilot" / "ontology-development-v4" / "production"
BASELINE = PRODUCTION / "scale-pilot-01"


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected one JSON object: {path}")
    return value


def counts(value: dict) -> tuple[int, int]:
    record = value.get("record")
    if not isinstance(record, dict):
        return 0, 0
    return len(record.get("studies", [])), len(record.get("items", []))


def projects(value: dict) -> str:
    return ";".join(value.get("eligibility", {}).get("project_ids", []))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    args = parser.parse_args()
    run = args.run.resolve()
    manifest = list(
        csv.DictReader((BASELINE / "MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t")
    )

    rows: list[dict[str, str | int]] = []
    for source in manifest:
        record_id = source["record_id"]
        old = read_json(BASELINE / "records" / f"{record_id}.json")
        new = read_json(run / "records" / f"{record_id}.json")
        old_studies, old_items = counts(old)
        new_studies, new_items = counts(new)
        rows.append(
            {
                "record_id": record_id,
                "sample_group": source["sample_group"],
                "title": source["title"],
                "old_decision": old["eligibility"]["decision"],
                "new_decision": new["eligibility"]["decision"],
                "old_basis": old["eligibility"]["basis"],
                "new_basis": new["eligibility"]["basis"],
                "old_projects": projects(old),
                "new_projects": projects(new),
                "old_studies": old_studies,
                "new_studies": new_studies,
                "old_items": old_items,
                "new_items": new_items,
            }
        )

    csv_path = run / "COMPARISON.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    changed = [row for row in rows if row["old_decision"] != row["new_decision"]]
    project_changed = [row for row in rows if row["old_projects"] != row["new_projects"]]
    included = [row for row in rows if row["new_decision"] == "INCLUDE"]
    run_results = [
        read_json(path)
        for row in rows
        if (path := run / "traces" / f"{row['record_id']}.run.json").is_file()
    ]
    extension_path = run / "extensions.jsonl"
    extension_count = (
        sum(1 for line in extension_path.read_text(encoding="utf-8").splitlines() if line)
        if extension_path.is_file()
        else 0
    )
    summary = {
        "papers": len(rows),
        "successful": sum(row.get("status") == "ok" for row in run_results),
        "included": len(included),
        "excluded": len(rows) - len(included),
        "studies": sum(int(row["new_studies"]) for row in rows),
        "items": sum(int(row["new_items"]) for row in rows),
        "eligibility_changes": len(changed),
        "project_link_changes": len(project_changed),
        "registry_extensions": extension_count,
    }
    (run / "SUMMARY.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Single-agent comparison pilot",
        "",
        f"- Papers: {len(rows)}",
        f"- Eligibility decisions changed: {len(changed)}",
        f"- Project links changed: {len(project_changed)}",
        "",
        "| Paper | Group | Old | New | Old items | New items |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['record_id']} | {row['sample_group']} | {row['old_decision']} | "
            f"{row['new_decision']} | {row['old_items']} | {row['new_items']} |"
        )
    (run / "COMPARISON.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"papers={len(rows)}")
    print(f"eligibility_changes={len(changed)}")
    print(f"project_link_changes={len(project_changed)}")
    print(f"report={run / 'COMPARISON.md'}")


if __name__ == "__main__":
    main()
