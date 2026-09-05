#!/usr/bin/env python3
"""Prepare papers for the single-agent full-text workflow."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PRODUCTION = ROOT / "pilot" / "ontology-development-v4" / "production"
PILOT = PRODUCTION / "single-agent-pilot"
PACKAGES = ROOT / "scale" / "protocol-2.0" / "fulltext-paper-packages-v2" / "packages"
BASELINE_MANIFEST = PRODUCTION / "scale-pilot-01" / "MANIFEST.tsv"
def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def publication_form(package: dict) -> str:
    publication = package["publication"]
    metadata = package["deterministic_metadata"].get("publication", {})
    terms = " ".join(
        [
            str(metadata.get("article_type") or ""),
            *[str(value) for value in publication.get("document_types", [])],
        ]
    ).casefold()
    if "retraction" in terms:
        return "RETRACTION_NOTICE"
    if "correction" in terms or "erratum" in terms:
        return "CORRECTION_NOTICE"
    if "protocol" in terms:
        return "PROTOCOL_ARTICLE"
    if "systematic review" in terms or "review-article" in terms or " review" in terms:
        return "REVIEW_ARTICLE"
    if "comment" in terms or "editorial" in terms or "opinion" in terms:
        return "OPINION_ARTICLE"
    if "conceptual" in terms or "framework" in terms:
        return "CONCEPTUAL_ARTICLE"
    return "ORIGINAL_RESEARCH_ARTICLE"


def replace_once(text: str, marker: str, value: str) -> str:
    if text.count(marker) != 1:
        raise ValueError(f"expected one prompt marker: {marker}")
    return text.replace(marker, value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--package-manifest",
        type=Path,
        help="prepare all rows in this package manifest instead of the fixed pilot",
    )
    parser.add_argument(
        "--exclude-records-dir",
        type=Path,
        help="exclude record IDs that already have a JSON record in this directory",
    )
    args = parser.parse_args()

    output = args.output.resolve()
    inputs = output / "inputs"
    contexts = output / "contexts"
    inputs.mkdir(parents=True, exist_ok=True)
    contexts.mkdir(parents=True, exist_ok=True)

    template_path = PILOT / "PROMPT_TEMPLATE.md"
    template = template_path.read_text(encoding="utf-8")
    source_rows = read_tsv(
        args.package_manifest.resolve() if args.package_manifest else BASELINE_MANIFEST
    )
    excluded_ids = set()
    if args.exclude_records_dir:
        excluded_ids = {
            path.stem for path in args.exclude_records_dir.resolve().glob("*.json")
        }
    rows: list[dict[str, str]] = []
    for baseline in source_rows:
        record_id = baseline["record_id"]
        if record_id in excluded_ids:
            continue
        package_path = (
            ROOT / baseline["package_path"]
            if baseline.get("package_path")
            else PACKAGES / f"{record_id}.json"
        )
        if (
            baseline.get("package_sha256")
            and digest(package_path) != baseline["package_sha256"]
        ):
            raise ValueError(f"package hash mismatch: {record_id}")
        package = json.loads(package_path.read_text(encoding="utf-8"))
        source_path = ROOT / package["full_text"]["path"]
        if digest(source_path) != package["full_text"]["sha256"]:
            raise ValueError(f"source hash mismatch: {record_id}")

        candidate_projects = package["candidate_projects"]
        candidates_text = (
            json.dumps(candidate_projects, ensure_ascii=False, indent=2)
            if candidate_projects
            else "No candidate projects found."
        )
        metadata = {
            "publication": package["publication"],
            "deterministic_metadata": package["deterministic_metadata"],
            "abstract_screen": {
                "decision": package["abstract_screen"].get("decision"),
                "project_ids": package["abstract_screen"].get("project_ids", []),
                "reason": package["abstract_screen"].get("reason"),
            },
        }
        prompt = replace_once(
            template,
            '[INSERT THE CANDIDATE PROJECTS, OR "No candidate projects found."]',
            candidates_text,
        )
        prompt = replace_once(
            prompt,
            "[INSERT THE DETERMINISTICALLY EXTRACTED METADATA.]",
            "```json\n" + json.dumps(metadata, ensure_ascii=False, indent=2) + "\n```",
        )
        prompt = replace_once(
            prompt,
            "[INSERT THE FULL PAPER TEXT.]",
            source_path.read_text(encoding="utf-8").rstrip(),
        )
        input_path = inputs / f"{record_id}.md"
        input_path.write_text(prompt + "\n", encoding="utf-8")

        candidate_ids = [row["project_id"] for row in candidate_projects]
        context_path = contexts / f"{record_id}.json"
        context_path.write_text(
            json.dumps(
                {
                    "record_id": record_id,
                    "candidate_project_ids": candidate_ids,
                    "publication_form": publication_form(package),
                    "source_marker": package["full_text"]["path"],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        rows.append(
            {
                **baseline,
                "input_path": str(input_path.relative_to(ROOT)),
                "input_sha256": digest(input_path),
                "input_bytes": str(input_path.stat().st_size),
                "context_path": str(context_path.relative_to(ROOT)),
                "context_sha256": digest(context_path),
                "publication_form": publication_form(package),
            }
        )

    manifest_path = output / "MANIFEST.tsv"
    write_tsv(manifest_path, rows)
    print(f"records={len(rows)}")
    print(f"manifest={manifest_path}")
    print(f"manifest_sha256={digest(manifest_path)}")


if __name__ == "__main__":
    main()
