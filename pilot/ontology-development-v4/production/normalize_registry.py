#!/usr/bin/env python3
"""Apply reviewed exact registry aliases to extraction records."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
REGISTRY_TYPE = {
    "InstrumentUse": "Instrument",
    "MethodUse": "Method",
    "ProtocolUse": "Protocol",
    "ModelUse": "Model",
    "SoftwareUse": "Software",
    "ProductUse": "Product",
    "ScoringUse": "Product",
}
DASHES = str.maketrans({"‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "−": "-"})


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalized_label(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).translate(DASHES)
    return re.sub(r"\s+", " ", value).strip().casefold()


def identity_in_scope(
    identity: dict[str, str], record_id: str, paper_id: str
) -> bool:
    """Accept a global identity or the same source publication."""
    if identity.get("scope", "") in {"GLOBAL", record_id}:
        return True
    source_identifier = identity.get("source_identifier", "").strip().casefold()
    return bool(paper_id and source_identifier == paper_id.strip().casefold())


def registry_lookup(
    rows: list[dict[str, str]],
    alias_rows: list[dict[str, str]] | None = None,
) -> tuple[dict[str, dict[str, str]], dict[tuple[str, str], set[str]]]:
    registry: dict[str, dict[str, str]] = {}
    lookup: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in rows:
        registry_id = row["registry_id"]
        if registry_id in registry:
            raise ValueError(f"duplicate registry_id: {registry_id}")
        registry[registry_id] = row
        labels = [row["canonical_label"], *(row.get("aliases", "") or "").split(";")]
        for label in labels:
            if label:
                use_types = (
                    ("Product", "Scoring")
                    if row["entity_type"] == "Product"
                    else (row["entity_type"],)
                )
                for use_type in use_types:
                    lookup[(use_type, normalized_label(label))].add(registry_id)
    for row in alias_rows or []:
        registry_id = row["registry_id"]
        if registry_id not in registry:
            raise ValueError(f"alias has unknown registry_id: {registry_id}")
        entity_type = registry[registry_id]["entity_type"]
        allowed_types = (
            ("Product", "Scoring") if entity_type == "Product" else (entity_type,)
        )
        use_type = row.get("use_type", "")
        if use_type and use_type not in allowed_types:
            raise ValueError(f"alias {row['alias']}: invalid use_type {use_type}")
        for target_type in (use_type,) if use_type else allowed_types:
            lookup[(target_type, normalized_label(row["alias"]))].add(registry_id)
    return registry, lookup


def resolve_record_path(
    record_id: str,
    run: Path,
    fallback_runs: list[Path],
) -> tuple[Path, Path] | None:
    for candidate_run in (run, *fallback_runs):
        path = candidate_run / "records" / f"{record_id}.json"
        if path.is_file():
            return path, candidate_run
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--fallback-run", type=Path, action="append", default=[])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, default=HERE / "CALIBRATION.tsv")
    parser.add_argument("--registry", type=Path, default=HERE / "REGISTRY.tsv")
    parser.add_argument(
        "--aliases", type=Path, default=HERE / "REGISTRY_ALIASES.tsv"
    )
    parser.add_argument(
        "--blocklist",
        type=Path,
        help="TSV with entity_type and source_label values that must stay unmapped",
    )
    parser.add_argument(
        "--reset-existing",
        action="store_true",
        help="clear prior registry IDs before exact reviewed normalization",
    )
    args = parser.parse_args()

    run = args.run.resolve()
    fallback_runs = [path.resolve() for path in args.fallback_run]
    output = args.output.resolve()
    records_dir = output / "records"
    records_dir.mkdir(parents=True, exist_ok=True)
    registry, lookup = registry_lookup(
        read_tsv(args.registry),
        read_tsv(args.aliases) if args.aliases.is_file() else [],
    )
    blocked = {
        (row["entity_type"], normalized_label(row["source_label"]))
        for row in read_tsv(args.blocklist)
    } if args.blocklist else set()
    mapped: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []
    collisions: list[dict[str, Any]] = []
    unverified_existing: list[dict[str, str]] = []
    reset_existing = 0
    source_runs: Counter[str] = Counter()

    for row in read_tsv(args.manifest):
        record_id = row["record_id"]
        resolved = resolve_record_path(record_id, run, fallback_runs)
        if resolved is None:
            raise ValueError(f"missing record: {record_id}")
        source_path, source_run = resolved
        source_runs[str(source_run.relative_to(REPO))] += 1
        record = json.loads(source_path.read_text(encoding="utf-8"))
        for item in record["items"]:
            entity_type = REGISTRY_TYPE.get(item["type"])
            if not entity_type:
                continue
            review_type = "Scoring" if item["type"] == "ScoringUse" else entity_type
            key = (review_type, normalized_label(item["source_label"]))
            registry_id = item["registry_id"]
            if args.reset_existing and registry_id is not None:
                item["registry_id"] = None
                registry_id = None
                reset_existing += 1
            review_key = (review_type, key[1])
            paper_id = row.get("paper_id", "")
            matches = [] if review_key in blocked else sorted(
                registry_id
                for registry_id in lookup.get(key, set())
                if identity_in_scope(registry[registry_id], record_id, paper_id)
            )
            if registry_id is None:
                if len(matches) == 1:
                    item["registry_id"] = matches[0]
                    mapped.append(
                        {
                            "record_id": record_id,
                            "item_id": item["id"],
                            "registry_id": matches[0],
                        }
                    )
                elif len(matches) > 1:
                    collisions.append(
                        {
                            "record_id": record_id,
                            "item_id": item["id"],
                            "source_label": item["source_label"],
                            "matches": matches,
                        }
                    )
                else:
                    unresolved.append(
                        {
                            "record_id": record_id,
                            "item_id": item["id"],
                            "entity_type": entity_type,
                            "source_label": item["source_label"],
                        }
                    )
            elif registry_id not in registry:
                raise ValueError(f"{record_id}/{item['id']}: unknown {registry_id}")
            elif registry_id not in matches:
                unverified_existing.append(
                    {
                        "record_id": record_id,
                        "item_id": item["id"],
                        "registry_id": registry_id,
                        "source_label": item["source_label"],
                    }
                )
        output_path = records_dir / f"{record_id}.json"
        output_path.write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    summary = {
        "records": sum(source_runs.values()),
        "source_runs": dict(source_runs),
        "mapped": len(mapped),
        "unresolved": len(unresolved),
        "collisions": len(collisions),
        "unverified_existing": len(unverified_existing),
        "reset_existing": reset_existing,
        "registry_sha256": digest(args.registry),
        "aliases_sha256": digest(args.aliases) if args.aliases.is_file() else None,
    }
    result = {
        "summary": summary,
        "mapped": mapped,
        "unresolved": unresolved,
        "collisions": collisions,
        "unverified_existing": unverified_existing,
    }
    (output / "NORMALIZATION.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))
    if collisions:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
