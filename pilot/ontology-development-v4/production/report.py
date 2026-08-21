#!/usr/bin/env python3
"""Create a concise deterministic report for one production calibration run."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def resolve_record_path(
    record_id: str,
    run: Path,
    fallback_runs: list[Path],
) -> tuple[Path, Path] | None:
    """Return the first record path and its source run in precedence order."""
    for candidate_run in (run, *fallback_runs):
        path = candidate_run / "records" / f"{record_id}.json"
        if path.is_file():
            return path, candidate_run
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument(
        "--fallback-run",
        type=Path,
        action="append",
        default=[],
        help="use records from this run when the primary run has no record",
    )
    parser.add_argument("--manifest", type=Path, default=HERE / "CALIBRATION.tsv")
    args = parser.parse_args()
    manifest = read_tsv(args.manifest)
    records: list[dict[str, Any]] = []
    record_sources: Counter[str] = Counter()
    for row in manifest:
        resolved = resolve_record_path(row["record_id"], args.run, args.fallback_run)
        if resolved:
            path, source_run = resolved
            records.append(json.loads(path.read_text(encoding="utf-8")))
            record_sources[str(source_run)] += 1
    validation_path = args.run / "VALIDATION.json"
    validation = (
        json.loads(validation_path.read_text(encoding="utf-8"))
        if validation_path.is_file()
        else None
    )
    run_summary_path = args.run / "SUMMARY.json"
    run_summary = (
        json.loads(run_summary_path.read_text(encoding="utf-8"))
        if run_summary_path.is_file()
        else None
    )
    studies = [study for record in records for study in record["studies"]]
    items = [item for record in records for item in record["items"]]
    unmapped_registry = [
        {
            "record_id": record["record_id"],
            "type": item["type"],
            "source_label": item["source_label"],
        }
        for record in records
        for item in record["items"]
        if item["type"]
        in {
            "InstrumentUse",
            "MethodUse",
            "ProtocolUse",
            "ModelUse",
            "ProductUse",
            "ScoringUse",
        }
        and item["registry_id"] is None
    ]
    gaps = [item for item in items if item["type"] == "Gap"]
    conflicts = [item for item in items if item["type"] == "SourceConflict"]
    summary = {
        "records": len(records),
        "record_sources": dict(record_sources),
        "dispositions": dict(Counter(record["assessment"]["disposition"] for record in records)),
        "studies": len(studies),
        "primary_families": dict(Counter(study["primary_research_family"] for study in studies)),
        "item_types": dict(Counter(item["type"] for item in items)),
        "unmapped_registry": len(unmapped_registry),
        "gaps": len(gaps),
        "source_conflicts": len(conflicts),
        "validation": validation["summary"] if validation else None,
        "run": {
            key: run_summary.get(key)
            for key in (
                "model",
                "reasoning_effort",
                "records",
                "successful",
                "failed",
                "elapsed_agent_seconds",
                "usage",
            )
        }
        if run_summary
        else None,
    }
    output = {
        "summary": summary,
        "unmapped_registry": unmapped_registry,
        "gaps": gaps,
        "source_conflicts": conflicts,
    }
    (args.run / "REPORT.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# Production calibration report",
        "",
        f"- Records: {len(records)}/{len(manifest)}.",
        f"- Studies: {len(studies)}.",
        f"- Unmapped registry labels: {len(unmapped_registry)}.",
        f"- Ontology gaps: {len(gaps)}.",
        f"- Source conflicts: {len(conflicts)}.",
    ]
    if validation:
        valid = validation["summary"]["valid"]
        expected = validation["summary"]["expected"]
        lines.append(f"- Deterministically valid records: {valid}/{expected}.")
    lines += ["", "## Dispositions", ""]
    lines.extend(
        f"- `{key}`: {value}."
        for key, value in sorted(summary["dispositions"].items())
    )
    lines += ["", "## Primary research families", ""]
    lines.extend(
        f"- `{key}`: {value}."
        for key, value in sorted(summary["primary_families"].items())
    )
    lines += ["", "## Ontology gaps", ""]
    if not gaps:
        lines.append("None.")
    else:
        for item in gaps:
            lines.append(
                f"- `{item['state']}` `{item['affected_key']}`: {item['evidence']}"
            )
    lines += ["", "## Source conflicts", ""]
    if not conflicts:
        lines.append("None.")
    else:
        for item in conflicts:
            lines.append(f"- {item['scope']}")
    lines += ["", "## Registry review queue", ""]
    if not unmapped_registry:
        lines.append("None.")
    else:
        for row in unmapped_registry:
            lines.append(
                f"- `{row['record_id']}` `{row['type']}`: {row['source_label']}"
            )
    (args.run / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
