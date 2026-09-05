#!/usr/bin/env python3
"""Prepare the fixed 20-paper funded-project extraction pilot."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PRODUCTION = ROOT / "pilot" / "ontology-development-v4" / "production"
PACKAGES = ROOT / "scale" / "protocol-2.0" / "fulltext-paper-packages-v2" / "packages"
sys.path.insert(0, str(PRODUCTION))

from scale_validate import validate_scale_result  # noqa: E402


SAMPLE = {
    "strong-support": (
        "Pd44d1f7862a2",
        "P331a66a51c5a",
        "P43731963824d",
        "P9cd3ec6c2594",
        "P9b4818f6b5e2",
    ),
    "likely-project-output": (
        "P94878b957eaf",
        "P26c157c2cc87",
        "P56e05d5f936e",
        "Pf53a5ee15eef",
        "P42480dcbbafa",
    ),
    "negative-control": (
        "P0d5ba8d5bb2c",
        "P3113dc9b9673",
        "P3a0c65aeea63",
        "Pd5c85ad12f19",
        "P4f23b7238f3e",
    ),
    "ambiguous": (
        "P0e37117d0b49",
        "Pac4f1e0ea5c5",
        "Pcf3f881673e1",
        "Pdf30fc100f6d",
        "P958d821a1250",
    ),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_manifest(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def slim_screen(value: dict) -> dict:
    return {
        "decision": value.get("decision"),
        "project_ids": value.get("project_ids", []),
        "reason": value.get("reason"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("extract", "review"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--draft-run", type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    inputs = output / "inputs"
    inputs.mkdir(parents=True, exist_ok=True)
    if args.stage == "review" and not args.draft_run:
        raise ValueError("--draft-run is required for review preparation")

    scale_task = (PRODUCTION / "SCALE_TASK.md").read_text(encoding="utf-8").rstrip()
    core_task = (PRODUCTION / "TASK.md").read_text(encoding="utf-8").rstrip()
    ontology = (PRODUCTION.parent / "ONTOLOGY.md").read_text(encoding="utf-8").rstrip()
    vocabulary = (PRODUCTION.parent / "VOCABULARY.tsv").read_text(encoding="utf-8").rstrip()
    prefix_parts = [
        scale_task,
        "# Typed extraction rules\n\n" + core_task,
        "# Ontology reference\n\n" + ontology,
        "# Controlled vocabulary\n\n```tsv\n" + vocabulary + "\n```",
    ]
    if args.stage == "review":
        prefix_parts.insert(
            0,
            (PRODUCTION / "SCALE_REVIEW_TASK.md").read_text(encoding="utf-8").rstrip(),
        )
        prefix_parts.insert(
            1,
            (PRODUCTION / "REVIEW_AND_CORRECT_TASK.md").read_text(encoding="utf-8").rstrip(),
        )

    rows: list[dict[str, str]] = []
    for group, record_ids in SAMPLE.items():
        for record_id in record_ids:
            package_path = PACKAGES / f"{record_id}.json"
            package = json.loads(package_path.read_text(encoding="utf-8"))
            if package["record_id"] != record_id:
                raise ValueError(f"package record mismatch: {record_id}")
            source_path = ROOT / package["full_text"]["path"]
            if digest(source_path) != package["full_text"]["sha256"]:
                raise ValueError(f"source hash mismatch: {record_id}")
            candidate_ids = {row["project_id"] for row in package["candidate_projects"]}
            draft = None
            validation_errors: list[str] = []
            if args.stage == "review":
                draft_path = args.draft_run.resolve() / "records" / f"{record_id}.json"
                draft = json.loads(draft_path.read_text(encoding="utf-8"))
                validation_errors, _ = validate_scale_result(draft, record_id, candidate_ids)

            paper_parts = [
                "# Paper package",
                "## Identity\n\n"
                f"- Record ID: `{record_id}`\n"
                f"- Package SHA-256: `{digest(package_path)}`\n"
                f"- Reading-copy SHA-256: `{package['full_text']['sha256']}`",
                "## Publication and discovery metadata\n\n```json\n"
                + json.dumps(package["publication"], ensure_ascii=False, indent=2)
                + "\n```",
                "## Abstract-screen result\n\nThis result nominated possible projects. It did not decide final eligibility.\n\n```json\n"
                + json.dumps(slim_screen(package["abstract_screen"]), ensure_ascii=False, indent=2)
                + "\n```",
                "## Nominated funded projects\n\n```json\n"
                + json.dumps(package["candidate_projects"], ensure_ascii=False, indent=2)
                + "\n```",
                "## Deterministic publication metadata\n\n```json\n"
                + json.dumps(package["deterministic_metadata"], ensure_ascii=False, indent=2)
                + "\n```",
                "## Full article\n\n" + source_path.read_text(encoding="utf-8").rstrip(),
            ]
            if draft is not None:
                paper_parts.extend(
                    [
                        "## Deterministic draft errors\n\n```json\n"
                        + json.dumps(validation_errors, ensure_ascii=False, indent=2)
                        + "\n```",
                        "## Draft result\n\n```json\n"
                        + json.dumps(draft, ensure_ascii=False, indent=2)
                        + "\n```",
                    ]
                )
            prompt = "\n\n".join([*prefix_parts, *paper_parts]) + "\n"
            input_path = inputs / f"{record_id}.md"
            input_path.write_text(prompt, encoding="utf-8")
            rows.append(
                {
                    "record_id": record_id,
                    "sample_group": group,
                    "title": package["publication"]["title"],
                    "year": str(package["publication"].get("year") or ""),
                    "doi": package["publication"].get("doi") or "",
                    "source_format": package["full_text"]["format"],
                    "candidate_project_ids": ";".join(sorted(candidate_ids)),
                    "package_path": str(package_path.relative_to(ROOT)),
                    "package_sha256": digest(package_path),
                    "source_path": str(source_path.relative_to(ROOT)),
                    "source_sha256": digest(source_path),
                    "input_path": str(input_path.relative_to(ROOT)),
                    "input_sha256": digest(input_path),
                    "input_bytes": str(input_path.stat().st_size),
                }
            )
    write_manifest(output / "MANIFEST.tsv", rows)
    print(f"stage={args.stage}")
    print(f"records={len(rows)}")
    print(f"manifest={output / 'MANIFEST.tsv'}")
    print(f"manifest_sha256={digest(output / 'MANIFEST.tsv')}")


if __name__ == "__main__":
    main()
