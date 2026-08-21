#!/usr/bin/env python3
"""Build reviewed registry and alias candidates from proposal decisions."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from normalize_registry import normalized_label


HERE = Path(__file__).resolve().parent
REGISTRY_COLUMNS = (
    "entity_type",
    "registry_id",
    "canonical_label",
    "parent_registry_id",
    "applies_to_registry_id",
    "variant_kind",
    "language_code",
    "jurisdiction",
    "version",
    "respondent_form",
    "source_identifier",
    "scope",
)
ALIAS_COLUMNS = ("registry_id", "alias")
CREATE_DECISIONS = {
    "ADD_GLOBAL",
    "ADD_SOURCE_SCOPED",
    "KEEP_COMPOUND",
    "TYPE_REPAIR",
}
LINK_DECISIONS = {"KEEP_EXISTING", "ALIAS_EXISTING", *CREATE_DECISIONS}


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], columns: tuple[str, ...]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=columns,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def target_type_and_id(row: dict[str, str]) -> tuple[str, str] | None:
    registry_id = row["proposed_registry_id"]
    if not registry_id:
        return None
    entity_type = row["entity_type"]
    if row["decision"] == "TYPE_REPAIR":
        prefix = registry_id.split(":", 1)[0]
        if prefix == "model":
            entity_type = "Model"
        elif prefix == "scoring":
            entity_type = "Product"
        elif prefix == "software":
            entity_type = "Software"
        else:
            return None
    elif entity_type == "Scoring":
        entity_type = "Product"
    if registry_id.startswith("scoring:"):
        registry_id = "product:" + registry_id.split(":", 1)[1]
    return entity_type, registry_id


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposals", type=Path, required=True)
    parser.add_argument("--registry", type=Path, default=HERE / "REGISTRY.tsv")
    parser.add_argument("--aliases", type=Path, default=HERE / "REGISTRY_ALIASES.tsv")
    parser.add_argument("--output-registry", type=Path, required=True)
    parser.add_argument("--output-aliases", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    identities: dict[str, dict[str, str]] = {}
    alias_pairs: set[tuple[str, str]] = set()
    for row in read_tsv(args.registry):
        registry_id = row["registry_id"]
        if registry_id in identities:
            raise ValueError(f"duplicate registry_id: {registry_id}")
        identities[registry_id] = {
            column: row.get(column, "") or "" for column in REGISTRY_COLUMNS
        }
        for alias in (row.get("aliases", "") or "").split(";"):
            if alias:
                alias_pairs.add((registry_id, alias))
    for row in read_tsv(args.aliases):
        alias_pairs.add((row["registry_id"], row["alias"]))

    proposals = read_tsv(args.proposals)
    creatable_ids = {
        target[1]
        for proposal in proposals
        if proposal["decision"] in CREATE_DECISIONS
        and (target := target_type_and_id(proposal)) is not None
    }
    skipped: list[dict[str, str]] = []
    conflicts: list[str] = []
    decisions: Counter[str] = Counter()
    for proposal in proposals:
        decision = proposal["decision"]
        decisions[decision] += 1
        target = target_type_and_id(proposal)
        if decision not in LINK_DECISIONS or target is None:
            skipped.append(
                {
                    "entity_type": proposal["entity_type"],
                    "source_label": proposal["source_label"],
                    "decision": decision,
                    "note": proposal["note"],
                }
            )
            continue
        entity_type, registry_id = target
        parent_id = proposal["parent_registry_id"]
        if parent_id.startswith("scoring:"):
            parent_id = "product:" + parent_id.split(":", 1)[1]
        applies_to_id = ""
        if entity_type == "Product" and parent_id.startswith("instrument:"):
            applies_to_id = parent_id
            parent_id = ""
        variant_kind = proposal["variant_kind"]
        if entity_type == "Instrument" and variant_kind == "PRODUCT_VERSION":
            variant_kind = "FORM_VERSION"
        candidate = {
            "entity_type": entity_type,
            "registry_id": registry_id,
            "canonical_label": proposal["canonical_label"],
            "parent_registry_id": parent_id,
            "applies_to_registry_id": applies_to_id,
            "variant_kind": variant_kind,
            "language_code": proposal["language_code"],
            "jurisdiction": proposal["jurisdiction"],
            "version": proposal["version"],
            "respondent_form": "PROXY"
            if "proxy" in proposal["canonical_label"].casefold()
            else "",
            "source_identifier": proposal["source_identifier"],
            "scope": proposal["scope"],
        }
        current = identities.get(registry_id)
        if current is None:
            if decision not in CREATE_DECISIONS and registry_id not in creatable_ids:
                conflicts.append(f"{registry_id}: alias target is not created")
                continue
            identities[registry_id] = candidate
        else:
            if current["entity_type"] != entity_type:
                conflicts.append(f"{registry_id}: entity type conflict")
                continue
            for field in REGISTRY_COLUMNS:
                if field in {"registry_id", "entity_type"}:
                    continue
                incoming = candidate[field]
                if not current[field] and incoming:
                    current[field] = incoming
                elif incoming and current[field] != incoming:
                    conflicts.append(
                        f"{registry_id}: {field} is {current[field]!r} and {incoming!r}"
                    )
        canonical = identities[registry_id]["canonical_label"]
        if normalized_label(proposal["source_label"]) != normalized_label(canonical):
            alias_pairs.add((registry_id, proposal["source_label"]))

    for registry_id, alias in alias_pairs:
        if registry_id not in identities:
            conflicts.append(f"{registry_id}: alias has no identity")
    if conflicts:
        raise ValueError("\n".join(sorted(set(conflicts))))

    identity_rows = sorted(identities.values(), key=lambda row: row["registry_id"])
    alias_rows = [
        {"registry_id": registry_id, "alias": alias}
        for registry_id, alias in sorted(
            alias_pairs,
            key=lambda pair: (pair[0], normalized_label(pair[1]), pair[1]),
        )
        if normalized_label(alias)
        != normalized_label(identities[registry_id]["canonical_label"])
    ]
    write_tsv(args.output_registry, identity_rows, REGISTRY_COLUMNS)
    write_tsv(args.output_aliases, alias_rows, ALIAS_COLUMNS)
    report = {
        "identities": len(identity_rows),
        "aliases": len(alias_rows),
        "decisions": dict(decisions),
        "skipped": skipped,
    }
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({key: value for key, value in report.items() if key != "skipped"}, indent=2))
    print(f"skipped={len(skipped)}")


if __name__ == "__main__":
    main()
