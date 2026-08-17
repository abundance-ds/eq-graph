#!/usr/bin/env python3
"""Validate a production one-pass run with deterministic rules."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

from evaluate import (
    CALIBRATION,
    INCLUDE_HEADINGS,
    VALID,
    first_class,
    parse_labels,
    read_usage,
    source_locator_coverage,
)
from index_terms import parse_record


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalization_flags(rows: list[dict[str, str]]) -> list[str]:
    flags: list[str] = []
    term_types: dict[tuple[str, str], set[str]] = {}
    analysis_words = (
        "regression",
        "correlation",
        "test",
        "analysis",
        "anova",
        "bootstrap",
        "cronbach",
        "coefficient",
    )
    for row in rows:
        value = row["value"].casefold()
        term_types.setdefault((row["record_id"], value), set()).add(row["type"])
        if row["type"] == "Model" and any(word in value for word in (" test", "correlation", "cronbach")):
            flags.append(f"{row['record_id']}: possible Analysis typed as Model: {row['value']}")
        if row["type"] == "Method" and any(word in value for word in analysis_words):
            flags.append(f"{row['record_id']}: possible Analysis typed as Method: {row['value']}")
        if row["type"] == "Setting" and "population" in value:
            flags.append(f"{row['record_id']}: possible Population typed as Setting: {row['value']}")
        if row["type"] == "Condition" and any(word in value for word in ("arthroplasty", "surgery", "procedure")):
            flags.append(f"{row['record_id']}: possible Concept typed as Condition: {row['value']}")
    for (record_id, value), types in term_types.items():
        if len(types) > 1:
            flags.append(
                f"{record_id}: same term has multiple types ({', '.join(sorted(types))}): {value}"
            )
    return flags


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--overlay-run", action="append", default=[])
    args = parser.parse_args()
    run_dir = CALIBRATION / args.run
    overlay_dirs = [CALIBRATION / value for value in args.overlay_run]
    manifest_path = (CALIBRATION / args.manifest).resolve()
    if CALIBRATION.resolve() not in manifest_path.parents:
        raise ValueError("manifest must be inside the calibration directory")

    records: list[dict[str, object]] = []
    all_index_rows: list[dict[str, str]] = []
    for item in read_manifest(manifest_path):
        record_id = item["record_id"]
        path = run_dir / "records" / f"{record_id}.md"
        for overlay_dir in overlay_dirs:
            candidate = overlay_dir / "records" / f"{record_id}.md"
            if candidate.is_file():
                path = candidate
        errors: list[str] = []
        if not path.is_file():
            records.append({"record_id": record_id, "exists": False, "errors": ["missing output"]})
            continue
        text = path.read_text(encoding="utf-8")
        labels = parse_labels(text)
        classes = {key: first_class(labels.get(key, ""), allowed) for key, allowed in VALID.items()}
        for label in ("disposition", "connection", "euroqol support", "support scope", "project link", "publication status", "evidence"):
            if label not in labels:
                errors.append(f"missing label: {label}")
        for label in VALID:
            if label in labels and not classes[label]:
                errors.append(f"invalid class: {label}")

        disposition = classes["disposition"]
        connection = classes["connection"]
        support = classes["euroqol support"]
        expected = (
            "include-study"
            if connection in {"direct_eq", "adjacent_measurement"} or support == "explicit"
            else "exclude"
            if connection in {"application_only", "unrelated"} and support != "explicit"
            else "unclear"
        )
        if disposition == "publication-context":
            expected = "publication-context"
        if disposition != expected:
            errors.append(f"decision rule gives {expected}, output gives {disposition}")

        present = [heading for heading in INCLUDE_HEADINGS if heading in text]
        if disposition == "include-study":
            for heading in INCLUDE_HEADINGS:
                if heading not in text:
                    errors.append(f"missing heading: {heading}")
                    continue
                if heading != "### High-value terms":
                    block = text.split(heading, 1)[1]
                    block = re.split(r"^###\s", block, maxsplit=1, flags=re.MULTILINE)[0]
                    if not re.search(r"^\s*-\s+", block, flags=re.MULTILINE):
                        errors.append(f"heading has no bullets: {heading}")
        elif disposition in {"exclude", "publication-context"} and present:
            errors.append("excluded or context record contains full extraction")
        status_text = labels.get("publication status", "").strip().lstrip("`").casefold()
        if status_text.startswith("retracted") and disposition == "include-study":
            if not any(word in text.casefold() for word in ("unsafe", "must not", "do not use", "not approved")):
                errors.append("retracted study lacks an unsafe-use warning")

        index_rows, index_errors = parse_record(path)
        errors.extend(index_errors)
        all_index_rows.extend(index_rows)
        located, bullets = source_locator_coverage(text)
        records.append(
            {
                "record_id": record_id,
                "doi": item["doi"],
                "exists": True,
                "classes": classes,
                "errors": errors,
                "word_count": len(text.split()),
                "located_bullets": located,
                "substantive_bullets": bullets,
                "index_terms": len(index_rows),
                "usage": read_usage(path.parents[1] / "traces" / f"{record_id}.jsonl"),
            }
        )

    present = [row for row in records if row.get("exists")]
    located = sum(int(row.get("located_bullets", 0)) for row in present)
    bullets = sum(int(row.get("substantive_bullets", 0)) for row in present)
    usage_keys = ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens")
    summary = {
        "records_expected": len(records),
        "records_present": len(present),
        "records_clean": sum(not row.get("errors") for row in present),
        "dispositions": dict(Counter(row["classes"]["disposition"] for row in present)),
        "connections": dict(Counter(row["classes"]["connection"] for row in present)),
        "support": dict(Counter(row["classes"]["euroqol support"] for row in present)),
        "index_terms": len(all_index_rows),
        "index_types": dict(Counter(row["type"] for row in all_index_rows)),
        "normalization_flags": normalization_flags(all_index_rows),
        "source_locator_rate": round(located / bullets, 4) if bullets else None,
        "mean_output_words": round(sum(int(row.get("word_count", 0)) for row in present) / len(present), 1)
        if present
        else None,
        "usage": {
            key: sum(int(row.get("usage", {}).get(key, 0)) for row in present)
            for key in usage_keys
        },
    }
    result = {"summary": summary, "records": records}
    (run_dir / "VALIDATION.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    flagged = [row for row in records if row.get("errors")]
    lines = [
        "# Production-run validation",
        "",
        f"- Records present: {summary['records_present']}/{summary['records_expected']}.",
        f"- Clean records: {summary['records_clean']}/{summary['records_present']}.",
        f"- Parsed index terms: {summary['index_terms']}.",
        f"- Source-locator rate: {summary['source_locator_rate']:.1%}.",
        f"- Mean record length: {summary['mean_output_words']:,.0f} words.",
        f"- Normalization flags: {len(summary['normalization_flags'])}.",
        "",
        "## Dispositions",
        "",
    ]
    lines.extend(f"- {key}: {value}." for key, value in sorted(summary["dispositions"].items()))
    lines += ["", "## Records for targeted repair", ""]
    if not flagged:
        lines.append("None.")
    for row in flagged:
        lines.append(f"- {row['record_id']}: {'; '.join(row['errors'])}.")
    lines += ["", "## Deterministic normalization review", ""]
    if not summary["normalization_flags"]:
        lines.append("No type-rule flags.")
    else:
        lines.extend(f"- {value}." for value in summary["normalization_flags"])
    (run_dir / "VALIDATION.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
