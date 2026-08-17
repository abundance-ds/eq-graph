#!/usr/bin/env python3
"""Parse the flat index from one-pass Markdown records."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ALLOWED = {
    "Study type",
    "Design",
    "Population",
    "Dataset",
    "Instrument",
    "Language",
    "Administration",
    "Method",
    "Protocol",
    "Analysis",
    "Model",
    "Product",
    "Outcome",
    "Concept",
    "Condition",
    "Setting",
    "Geography",
}


def assessment_value(text: str, label: str) -> str:
    match = re.search(rf"^- {re.escape(label)}:\s*`?([^.`\s]+)", text, flags=re.MULTILINE)
    return match.group(1) if match else ""


def parse_record(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    text = path.read_text(encoding="utf-8")
    record_id = path.stem
    disposition = assessment_value(text, "Disposition")
    if disposition != "include-study":
        return [], []
    if "### High-value terms" not in text:
        return [], [f"{record_id}: missing High-value terms heading"]

    block = text.split("### High-value terms", 1)[1]
    block = re.split(r"^###\s", block, maxsplit=1, flags=re.MULTILINE)[0]
    rows: list[dict[str, str]] = []
    errors: list[str] = []
    seen: set[tuple[str, str]] = set()
    for raw in block.splitlines():
        line = raw.strip()
        if not line:
            continue
        match = re.fullmatch(r"- ([^:]+):\s*(.+)", line)
        if not match:
            errors.append(f"{record_id}: invalid index line: {line}")
            continue
        term_type, value = match.groups()
        if term_type not in ALLOWED:
            errors.append(f"{record_id}: invalid index type: {term_type}")
            continue
        value = value.strip().rstrip(".")
        key = (term_type.casefold(), value.casefold())
        if key in seen:
            errors.append(f"{record_id}: duplicate index term: {term_type}: {value}")
            continue
        seen.add(key)
        rows.append({"record_id": record_id, "type": term_type, "value": value})
    if len(rows) < 4:
        errors.append(f"{record_id}: only {len(rows)} valid index terms")
    return rows, errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("records_dir", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows: list[dict[str, str]] = []
    errors: list[str] = []
    for path in sorted(args.records_dir.glob("*.md")):
        record_rows, record_errors = parse_record(path)
        rows.extend(record_rows)
        errors.extend(record_errors)

    output = args.output or args.records_dir.parent / "INDEX_TERMS.tsv"
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["record_id", "type", "value"],
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"records={len({row['record_id'] for row in rows})}")
    print(f"terms={len(rows)}")
    print(f"errors={len(errors)}")
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
