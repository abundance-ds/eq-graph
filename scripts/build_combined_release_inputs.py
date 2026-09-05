#!/usr/bin/env python3
"""Combine the frozen JATS inputs with one validated expansion tranche."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-manifest", type=Path, required=True)
    parser.add_argument("--added-manifest", type=Path, required=True)
    parser.add_argument("--base-openalex", type=Path, required=True)
    parser.add_argument("--added-openalex", type=Path, required=True)
    parser.add_argument("--exclude-record-id", action="append", default=[])
    parser.add_argument("--output-directory", type=Path, required=True)
    return parser.parse_args()


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    args = parse_args()
    output = args.output_directory.resolve()
    output.mkdir(parents=True, exist_ok=True)

    base_fields, base_rows = read_tsv(args.base_manifest.resolve())
    added_fields, added_rows = read_tsv(args.added_manifest.resolve())
    excluded = set(args.exclude_record_id)
    known_added_ids = {row["record_id"] for row in added_rows}
    if not excluded <= known_added_ids:
        raise ValueError(f"unknown excluded record IDs: {sorted(excluded - known_added_ids)}")
    added_rows = [row for row in added_rows if row["record_id"] not in excluded]
    fields = [*base_fields, *(field for field in added_fields if field not in base_fields)]
    manifest_rows = [*base_rows, *added_rows]
    record_ids = [row["record_id"] for row in manifest_rows]
    if len(record_ids) != len(set(record_ids)):
        raise ValueError("combined manifest has duplicate record IDs")
    paper_ids = [row["paper_id"].casefold() for row in manifest_rows]
    if len(paper_ids) != len(set(paper_ids)):
        raise ValueError("combined manifest has duplicate paper IDs")

    manifest = output / "MANIFEST.tsv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            delimiter="\t",
            lineterminator="\n",
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(manifest_rows)

    added_manifest = output / "ADDED_MANIFEST.tsv"
    with added_manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=added_fields,
            delimiter="\t",
            lineterminator="\n",
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(added_rows)

    added_publication_ids = set()
    for row in added_rows:
        metadata = json.loads(Path(row["metadata_path"]).read_text(encoding="utf-8"))
        added_publication_ids.add(metadata["publication"]["publication_id"])

    openalex_rows = [
        *read_jsonl(args.base_openalex.resolve()),
        *(
            row
            for row in read_jsonl(args.added_openalex.resolve())
            if row["publication_id"] in added_publication_ids
        ),
    ]
    publication_ids = [row["publication_id"] for row in openalex_rows]
    if len(publication_ids) != len(set(publication_ids)):
        raise ValueError("combined OpenAlex file has duplicate publication IDs")
    openalex = output / "openalex-publications.jsonl"
    with openalex.open("w", encoding="utf-8") as handle:
        for row in openalex_rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")

    summary = {
        "base_records": len(base_rows),
        "added_records": len(added_rows),
        "excluded_added_records": sorted(excluded),
        "combined_records": len(manifest_rows),
        "openalex_rows": len(openalex_rows),
        "manifest_sha256": digest(manifest),
        "openalex_sha256": digest(openalex),
    }
    (output / "SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
