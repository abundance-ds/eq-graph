#!/usr/bin/env python3
"""Create a build manifest with corrected top-level JATS author metadata."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parent
PARSER_DIRECTORY = REPO / "pipeline"
sys.path.insert(0, str(PARSER_DIRECTORY))

from jats_metadata import parse_jats  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with args.manifest.open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source, delimiter="\t"))
    output = args.output_directory.resolve()
    metadata_directory = output / "metadata"
    metadata_directory.mkdir(parents=True, exist_ok=True)
    output_rows: list[dict[str, str]] = []
    changed: list[dict[str, object]] = []
    for row in rows:
        old_path = REPO / row["metadata_path"]
        old = json.loads(old_path.read_text(encoding="utf-8"))
        new = parse_jats(REPO / row["xml_path"])
        old_without_authors = {key: value for key, value in old.items() if key != "authors"}
        new_without_authors = {key: value for key, value in new.items() if key != "authors"}
        if old_without_authors != new_without_authors:
            raise ValueError(f"Non-author metadata changed for {row['record_id']}")
        if old["authors"] != new["authors"]:
            changed.append(
                {
                    "record_id": row["record_id"],
                    "doi": row["paper_id"],
                    "old_authors": len(old["authors"]),
                    "new_authors": len(new["authors"]),
                }
            )
        metadata_path = metadata_directory / f"{row['record_id']}.json"
        metadata_path.write_text(
            json.dumps(new, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        output_rows.append(
            {
                **row,
                "metadata_path": str(metadata_path.relative_to(REPO)),
                "metadata_sha256": digest(metadata_path),
                "metadata_repair": "TOP_LEVEL_JATS_CONTRIBUTORS_ONLY",
            }
        )
    manifest_path = output / "MANIFEST.tsv"
    with manifest_path.open("w", encoding="utf-8", newline="") as destination:
        writer = csv.DictWriter(
            destination, fieldnames=list(output_rows[0]), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(output_rows)
    report = {
        "records": len(rows),
        "records_with_author_repairs": len(changed),
        "repairs": changed,
        "source_manifest": str(args.manifest),
        "source_manifest_sha256": digest(args.manifest),
        "output_manifest_sha256": digest(manifest_path),
        "parser_sha256": digest(PARSER_DIRECTORY / "jats_metadata.py"),
    }
    (output / "REPORT.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
