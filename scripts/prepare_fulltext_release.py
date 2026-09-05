#!/usr/bin/env python3
"""Prepare the completed full-text results for the typed database loader."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parent.parent
PRODUCTION = ROOT / "pilot/ontology-development-v4/production"
ONTOLOGY = ROOT / "pilot/ontology-development-v4"
SCALE = ROOT / "scale/protocol-2.0"

RESULT_RUNS = (
    PRODUCTION / "single-agent-pilot/native-opus-clean-check-01",
    SCALE / "fulltext-single-agent-v1/run-01",
    SCALE / "fulltext-sql-scale-v1/run-01",
)
EXTENSION_LOGS = tuple(path / "extensions.jsonl" for path in RESULT_RUNS)
PREPARATION_MANIFEST = SCALE / "fulltext-preparation-v2/MANIFEST.tsv"
PACKAGES = SCALE / "fulltext-paper-packages-v2/packages"
SOURCE_UNION = SCALE / "source-union.jsonl"
OPENALEX_DISCOVERY = SCALE / "openalex-discovery.jsonl"
BASE_PEOPLE = PRODUCTION / "person-citation-sprint-v2"

REGISTRY_FIELDS = (
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
ALIAS_FIELDS = ("registry_id", "alias", "use_type")
MANIFEST_FIELDS = (
    "record_id",
    "paper_id",
    "article_path",
    "article_sha256",
    "article_bytes",
    "xml_path",
    "xml_sha256",
    "xml_bytes",
    "pdf_path",
    "pdf_sha256",
    "pdf_bytes",
    "metadata_path",
    "metadata_sha256",
    "project_ids",
)
REGISTRY_ITEM_TYPES = {
    "InstrumentUse": "Instrument",
    "MethodUse": "Method",
    "ProtocolUse": "Protocol",
    "ModelUse": "Model",
    "SoftwareUse": "Software",
    "ProductUse": "Product",
    "ScoringUse": "Product",
}
DASHES = str.maketrans({"‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "−": "-"})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=SCALE / "fulltext-release-v1",
    )
    return parser.parse_args()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path.resolve())


def normalized_label(value: str) -> str:
    text = unicodedata.normalize("NFKC", value).translate(DASHES)
    return re.sub(r"\s+", " ", text).strip().casefold()


def compact_label(value: str) -> str:
    text = unicodedata.normalize("NFKD", normalized_label(value))
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "", text)


def normalized_doi(value: str | None) -> str:
    text = (value or "").strip().casefold()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:)", "", text).rstrip("/")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(
    path: Path,
    rows: Iterable[dict[str, Any]],
    fields: Iterable[str],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(fields),
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


class Components:
    def __init__(self) -> None:
        self.parent: dict[tuple[str, str], tuple[str, str]] = {}

    def add(self, value: tuple[str, str]) -> None:
        self.parent.setdefault(value, value)

    def find(self, value: tuple[str, str]) -> tuple[str, str]:
        self.add(value)
        parent = self.parent[value]
        if parent != value:
            self.parent[value] = self.find(parent)
        return self.parent[value]

    def union(self, left: tuple[str, str], right: tuple[str, str]) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def registry_id_for(entity_type: str, label: str, used: set[str]) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", normalized_label(label)).strip("-") or "entity"
    candidate = f"{entity_type.casefold()}:{slug}"
    if candidate not in used:
        return candidate
    suffix = hashlib.sha256(f"{entity_type}\0{label}".encode()).hexdigest()[:8]
    return f"{candidate}-{suffix}"


def load_results() -> tuple[dict[str, dict[str, Any]], dict[str, Path]]:
    results: dict[str, dict[str, Any]] = {}
    source_runs: dict[str, Path] = {}
    for run in RESULT_RUNS:
        for path in sorted((run / "records").glob("*.json")):
            value = json.loads(path.read_text(encoding="utf-8"))
            record_id = value["record_id"]
            if record_id in results:
                raise ValueError(f"Duplicate result: {record_id}")
            results[record_id] = value
            source_runs[record_id] = run
    return results, source_runs


def all_extensions() -> tuple[list[dict[str, Any]], dict[Path, list[dict[str, Any]]]]:
    combined: list[dict[str, Any]] = []
    by_run: dict[Path, list[dict[str, Any]]] = {}
    for run, path in zip(RESULT_RUNS, EXTENSION_LOGS, strict=True):
        rows = read_jsonl(path)
        by_run[run] = rows
        combined.extend(rows)
    return combined, by_run


def build_registry(
    extensions: list[dict[str, Any]],
) -> tuple[
    list[dict[str, str]],
    list[dict[str, str]],
    dict[tuple[str, str], str],
    dict[str, Any],
]:
    source_registry = read_tsv(PRODUCTION / "REGISTRY.tsv")
    base = [row for row in source_registry if row["scope"] == "GLOBAL"]
    scoped = [row for row in source_registry if row["scope"] != "GLOBAL"]
    base_ids = {row["registry_id"] for row in base}
    source_by_id = {row["registry_id"]: row for row in source_registry}
    source_aliases = read_tsv(PRODUCTION / "REGISTRY_ALIASES.tsv")
    base_aliases = [
        row
        for row in source_aliases
        if row["registry_id"] in base_ids
    ]
    scoped_aliases = [
        row for row in source_aliases if row["registry_id"] not in base_ids
    ]
    concepts = read_tsv(PRODUCTION / "CONCEPT_MAP.tsv")
    components = Components()
    labels: dict[tuple[str, str], list[str]] = defaultdict(list)
    base_by_key: dict[tuple[str, str], dict[str, str]] = {}
    preferred: list[tuple[str, str]] = []

    for row in base:
        key = (row["entity_type"], normalized_label(row["canonical_label"]))
        components.add(key)
        labels[key].append(row["canonical_label"])
        base_by_key[key] = row
    for row in concepts:
        key = ("Concept", normalized_label(row["canonical_label"]))
        components.add(key)
        labels[key].append(row["canonical_label"])
        preferred.append(key)
    for row in scoped:
        key = (row["entity_type"], normalized_label(row["canonical_label"]))
        components.add(key)
        if row["canonical_label"] not in labels[key]:
            labels[key].append(row["canonical_label"])
    entity_rows = [row for row in extensions if row["action"] == "ADD_REGISTRY_ENTITY"]
    for row in entity_rows:
        key = (row["entity_type"], normalized_label(row["name"]))
        components.add(key)
        if row["name"] not in labels[key]:
            labels[key].append(row["name"])

    compact_groups: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    for key in components.parent:
        compact_groups[(key[0], compact_label(key[1]))].append(key)
    compact_merges: list[list[str]] = []
    for keys in compact_groups.values():
        if len(keys) < 2:
            continue
        anchor = keys[0]
        for key in keys[1:]:
            components.union(anchor, key)
        compact_merges.append([labels[key][0] for key in keys])

    explicit_aliases = [
        row for row in extensions if row["action"] == "ADD_REGISTRY_ALIAS"
    ]
    for row in explicit_aliases:
        canonical = (row["entity_type"], normalized_label(row["canonical_name"]))
        if canonical not in components.parent:
            raise ValueError(
                f"Unknown alias target {row['entity_type']}: {row['canonical_name']}"
            )
        preferred.append(canonical)

    alias_targets: dict[tuple[str, str], set[tuple[str, str]]] = defaultdict(set)
    for row in explicit_aliases:
        alias_key = (row["entity_type"], normalized_label(row["alias"]))
        canonical = (row["entity_type"], normalized_label(row["canonical_name"]))
        alias_targets[alias_key].add(components.find(canonical))
    conflicting_aliases = {
        key: targets for key, targets in alias_targets.items() if len(targets) > 1
    }
    for row in explicit_aliases:
        alias_key = (row["entity_type"], normalized_label(row["alias"]))
        if alias_key in conflicting_aliases or alias_key not in components.parent:
            continue
        canonical = (row["entity_type"], normalized_label(row["canonical_name"]))
        components.union(alias_key, canonical)

    members: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    for key in components.parent:
        members[components.find(key)].append(key)

    preferred_rank = {key: index for index, key in enumerate(preferred)}
    used_ids = {row["registry_id"] for row in base}
    final_rows: list[dict[str, str]] = []
    final_for_key: dict[tuple[str, str], str] = {}
    canonical_for_root: dict[tuple[str, str], tuple[str, str]] = {}
    for root, keys in sorted(members.items()):
        base_keys = [key for key in keys if key in base_by_key]
        if len(base_keys) > 1:
            ids = [base_by_key[key]["registry_id"] for key in base_keys]
            raise ValueError(f"Registry merge joins base identities: {ids}")
        if base_keys:
            canonical_key = base_keys[0]
            row = {field: base_by_key[canonical_key].get(field, "") for field in REGISTRY_FIELDS}
        else:
            canonical_key = min(
                keys,
                key=lambda key: (
                    preferred_rank.get(key, 10**9),
                    len(labels[key][0]),
                    labels[key][0].casefold(),
                ),
            )
            canonical_label = labels[canonical_key][0]
            registry_id = registry_id_for(canonical_key[0], canonical_label, used_ids)
            used_ids.add(registry_id)
            row = {
                "entity_type": canonical_key[0],
                "registry_id": registry_id,
                "canonical_label": canonical_label,
                "parent_registry_id": "",
                "applies_to_registry_id": "",
                "variant_kind": "",
                "language_code": "",
                "jurisdiction": "",
                "version": "",
                "respondent_form": "",
                "source_identifier": "",
                "scope": "GLOBAL",
            }
        final_rows.append(row)
        canonical_for_root[root] = canonical_key
        for key in keys:
            final_for_key[key] = row["registry_id"]

    alias_values: set[tuple[str, str, str]] = set()
    for row in base_aliases:
        alias_values.add((row["registry_id"], row["alias"], row["use_type"]))
    for row in scoped_aliases:
        source = source_by_id[row["registry_id"]]
        key = (source["entity_type"], normalized_label(source["canonical_label"]))
        alias_values.add((final_for_key[key], row["alias"], row["use_type"]))
    for row in concepts:
        key = ("Concept", normalized_label(row["canonical_label"]))
        registry_id = final_for_key[key]
        if normalized_label(row["alias"]) != normalized_label(row["canonical_label"]):
            alias_values.add((registry_id, row["alias"], "Concept"))
    for root, keys in members.items():
        canonical_key = canonical_for_root[root]
        registry_id = final_for_key[canonical_key]
        canonical_label = next(
            row["canonical_label"] for row in final_rows if row["registry_id"] == registry_id
        )
        for key in keys:
            for label in labels[key]:
                if normalized_label(label) == normalized_label(canonical_label):
                    continue
                use_types = ("Product", "Scoring") if key[0] == "Product" else (key[0],)
                for use_type in use_types:
                    alias_values.add((registry_id, label, use_type))
    accepted_explicit_aliases = 0
    for row in explicit_aliases:
        alias_key = (row["entity_type"], normalized_label(row["alias"]))
        if alias_key in conflicting_aliases:
            continue
        canonical = (row["entity_type"], normalized_label(row["canonical_name"]))
        registry_id = final_for_key[canonical]
        use_types = (
            ("Product", "Scoring")
            if row["entity_type"] == "Product"
            else (row["entity_type"],)
        )
        for use_type in use_types:
            alias_values.add((registry_id, row["alias"], use_type))
        accepted_explicit_aliases += 1

    aliases = [
        {"registry_id": registry_id, "alias": alias, "use_type": use_type}
        for registry_id, alias, use_type in sorted(
            alias_values,
            key=lambda value: (value[0], value[2], normalized_label(value[1])),
        )
    ]
    database_rows = [row for row in final_rows if row["entity_type"] != "Concept"]
    database_ids = {row["registry_id"] for row in database_rows}
    database_aliases = [row for row in aliases if row["registry_id"] in database_ids]
    report = {
        "base_registry_entities": len(base),
        "omitted_source_scoped_base_entities": len(source_registry) - len(base),
        "promoted_source_scoped_identity_labels": len(
            {(row["entity_type"], normalized_label(row["canonical_label"])) for row in scoped}
        ),
        "proposed_registry_entity_rows": len(entity_rows),
        "unique_proposed_registry_entities": len(
            {(row["entity_type"], normalized_label(row["name"])) for row in entity_rows}
        ),
        "final_registry_entities": len(database_rows),
        "final_aliases": len(database_aliases),
        "canonical_concept_labels": sum(
            row["entity_type"] == "Concept" for row in final_rows
        ),
        "compact_identity_merges": compact_merges,
        "accepted_explicit_aliases": accepted_explicit_aliases,
        "skipped_ambiguous_aliases": [
            {"entity_type": key[0], "alias": key[1]}
            for key in sorted(conflicting_aliases)
        ],
    }
    return (
        sorted(database_rows, key=lambda row: row["registry_id"]),
        database_aliases,
        final_for_key,
        report,
    )


def build_vocabulary(
    extensions: list[dict[str, Any]],
) -> tuple[list[dict[str, str]], dict[str, str], dict[str, Any]]:
    rows = read_tsv(ONTOLOGY / "VOCABULARY.tsv")
    additions = [row for row in extensions if row["action"] == "ADD_ENUM_VALUE"]
    rewrite = {"MIXED_METHODS_INTEGRATION": "MIXED_METHOD_INTEGRATION"}
    seen = {(row["key"], row["value"]) for row in rows}
    added: list[dict[str, str]] = []
    for row in additions:
        value = rewrite.get(row["value"], row["value"])
        key = (row["key"], value)
        if key in seen:
            continue
        value_row = {
            "group": "fulltext_extension",
            "key": row["key"],
            "value": value,
            "definition": row["definition"],
        }
        rows.append(value_row)
        added.append(value_row)
        seen.add(key)
    return rows, rewrite, {"proposals": len(additions), "added": added, "rewrite": rewrite}


def run_registry(
    extensions: list[dict[str, Any]],
) -> dict[str, dict[str, str]]:
    """Reproduce each run registry so old IDs resolve to canonical labels."""
    identities = read_tsv(PRODUCTION / "REGISTRY.tsv")
    used = {row["registry_id"] for row in identities}
    for row in read_tsv(PRODUCTION / "CONCEPT_MAP.tsv"):
        label = row["canonical_label"]
        if any(
            value["entity_type"] == "Concept"
            and normalized_label(value["canonical_label"]) == normalized_label(label)
            for value in identities
        ):
            continue
        registry_id = registry_id_for("Concept", label, used)
        used.add(registry_id)
        identities.append(
            {
                "entity_type": "Concept",
                "registry_id": registry_id,
                "canonical_label": label,
            }
        )
    for row in extensions:
        if row["action"] != "ADD_REGISTRY_ENTITY":
            continue
        if any(
            value["entity_type"] == row["entity_type"]
            and normalized_label(value["canonical_label"]) == normalized_label(row["name"])
            for value in identities
        ):
            continue
        registry_id = registry_id_for(row["entity_type"], row["name"], used)
        used.add(registry_id)
        identities.append(
            {
                "entity_type": row["entity_type"],
                "registry_id": registry_id,
                "canonical_label": row["name"],
            }
        )
    return {row["registry_id"]: row for row in identities}


def adapt_metadata(
    record_id: str,
    metadata: dict[str, Any],
    package: dict[str, Any],
) -> dict[str, Any]:
    if "dates" in metadata:
        result = metadata
        result["publication"]["record_id"] = record_id
        unique_authors = []
        seen_authors: set[str] = set()
        for author in result["authors"]:
            key = normalized_label(author["display_name"])
            if key in seen_authors:
                continue
            seen_authors.add(key)
            author["order"] = len(unique_authors) + 1
            unique_authors.append(author)
        result["authors"] = unique_authors
        return result
    source = package["publication"]
    publication = dict(metadata["publication"])
    publication.update(
        {
            "record_id": record_id,
            "abstract": source.get("abstract"),
            "journal": publication.get("journal") or source.get("venue"),
            "publisher": None,
            "article_type": (source.get("document_types") or ["article"])[0],
            "language": None,
            "volume": None,
            "issue": None,
            "article_number": None,
            "licence_url": None,
            "open_access": False,
        }
    )
    year = publication.pop("year", None) or source.get("year")
    author_names = metadata.get("authors") or source.get("authors") or []
    authors = []
    seen_author_names: set[str] = set()
    for order, value in enumerate(author_names, 1):
        name = value if isinstance(value, str) else value.get("name") or value.get("display_name")
        if not name:
            continue
        name_key = normalized_label(name)
        if name_key in seen_author_names:
            continue
        seen_author_names.add(name_key)
        parts = name.split()
        authors.append(
            {
                "id": str(len(authors) + 1),
                "order": len(authors) + 1,
                "display_name": name,
                "family_name": parts[-1],
                "given_names": " ".join(parts[:-1]),
                "orcid": value.get("orcid") if isinstance(value, dict) else None,
                "corresponding": False,
                "email": None,
                "roles": [],
                "affiliation_ids": [],
            }
        )
    funding = [
        {
            "funder": funder,
            "award_id": None,
            "recipient": None,
            "source_text": None,
            "source_locator": "OpenAlex funding metadata",
        }
        for funder in metadata.get("funders", [])
    ]
    return {
        "publication": publication,
        "dates": [{"type": "published", "value": str(year)}] if year else [],
        "urls": [
            {"type": "canonical", "url": publication["canonical_url"]}
        ] if publication.get("canonical_url") else [],
        "affiliations": [],
        "authors": authors,
        "correspondence": [],
        "keywords": [],
        "categories": [
            {"type": "document_type", "value": value}
            for value in source.get("document_types") or []
        ],
        "funding": funding,
        "references": metadata.get("references", []),
    }


def build_openalex_rows(
    manifest_rows: list[dict[str, str]],
    metadata_by_record: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    source_union = {row["record_id"]: row for row in read_jsonl(SOURCE_UNION)}
    by_id: dict[str, dict[str, Any]] = {}
    by_doi: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in read_jsonl(OPENALEX_DISCOVERY):
        if row.get("openalex_id"):
            by_id[row["openalex_id"]] = row
        if doi := normalized_doi(row.get("doi")):
            by_doi[doi].append(row)
    output = []
    for manifest_row in manifest_rows:
        record_id = manifest_row["record_id"]
        metadata = metadata_by_record[record_id]
        publication = metadata["publication"]
        source = source_union.get(record_id, {})
        match = None
        for openalex_id in source.get("openalex_ids") or []:
            if openalex_id in by_id:
                match = by_id[openalex_id]
                break
        doi = normalized_doi(publication.get("doi"))
        if match is None and doi and by_doi.get(doi):
            match = by_doi[doi][0]
        authorships = []
        for author in (match or {}).get("authors") or []:
            authorships.append(
                {
                    "author": {
                        "id": f"https://openalex.org/{author.get('openalex_id')}"
                        if author.get("openalex_id") else None,
                        "display_name": author.get("name"),
                        "orcid": f"https://orcid.org/{author.get('orcid')}"
                        if author.get("orcid") else None,
                    },
                    "raw_author_name": author.get("name"),
                }
            )
        title = publication["title"]
        year = next(
            (int(row["value"][:4]) for row in metadata["dates"] if row.get("value", "")[:4].isdigit()),
            None,
        )
        output.append(
            {
                "publication_id": publication["publication_id"],
                "requested_doi": doi or None,
                "source_title": title,
                "source_year": year,
                "match_status": "EXACT" if match else "NOT_FOUND",
                "openalex_id": (match or {}).get("openalex_id"),
                "openalex_doi": normalized_doi((match or {}).get("doi")) or None,
                "openalex_title": (match or {}).get("title"),
                "openalex_year": (match or {}).get("year"),
                "title_similarity": 1.0 if match else None,
                "year_difference": abs(year - match["year"])
                if match and year and isinstance(match.get("year"), int) else None,
                "cited_by_count": int((match or {}).get("cited_by_count") or 0),
                "counts_by_year": [],
                "openalex_updated_date": None,
                "retrieved_at": "2026-08-27T00:00:00Z",
                "google_scholar_url": "https://scholar.google.com/scholar?q=" + quote_plus(doi or title),
                "authorships": authorships,
            }
        )
    return output


def prepare_people_base(output: Path, publication_ids: set[str]) -> None:
    rows = {
        name: read_tsv(BASE_PEOPLE / name)
        for name in (
            "PERSONS.tsv",
            "PERSON_NAMES.tsv",
            "PERSON_IDENTIFIERS.tsv",
            "PROJECT_PERSONS.tsv",
            "PUBLICATION_AUTHORS.tsv",
        )
    }
    keep_ids = {
        row["person_id"] for row in rows["PROJECT_PERSONS.tsv"]
    } | {
        row["person_id"]
        for row in rows["PERSONS.tsv"]
        if row["is_euroqol_member"] == "1"
    }
    rows["PERSONS.tsv"] = [
        row for row in rows["PERSONS.tsv"] if row["person_id"] in keep_ids
    ]
    rows["PERSON_NAMES.tsv"] = [
        row for row in rows["PERSON_NAMES.tsv"] if row["person_id"] in keep_ids
    ]
    rows["PERSON_IDENTIFIERS.tsv"] = [
        row for row in rows["PERSON_IDENTIFIERS.tsv"] if row["person_id"] in keep_ids
    ]
    rows["PUBLICATION_AUTHORS.tsv"] = [
        row
        for row in rows["PUBLICATION_AUTHORS.tsv"]
        if row["publication_id"] not in publication_ids
        and row["resolved_person_id"] in keep_ids
    ]
    for name, values in rows.items():
        fields = list(read_tsv(BASE_PEOPLE / name)[0])
        write_tsv(output / name, values, fields)


def main() -> None:
    args = parse_args()
    output = args.output.resolve()
    if output == ROOT or not output.is_relative_to(ROOT):
        raise ValueError("The release output must be a subdirectory of the repository.")
    if output.exists():
        shutil.rmtree(output)
    (output / "records").mkdir(parents=True)
    (output / "metadata").mkdir(parents=True)

    results, source_runs = load_results()
    if len(results) != 1607:
        raise ValueError(f"Expected 1,607 results, found {len(results)}")
    included = {
        record_id: value
        for record_id, value in results.items()
        if value["eligibility"]["decision"] == "INCLUDE"
    }
    if len(included) != 797:
        raise ValueError(f"Expected 797 included results, found {len(included)}")

    extensions, extensions_by_run = all_extensions()
    registry_rows, alias_rows, final_registry, registry_report = build_registry(extensions)
    vocabulary_rows, enum_rewrite, vocabulary_report = build_vocabulary(extensions)
    write_tsv(output / "REGISTRY.tsv", registry_rows, REGISTRY_FIELDS)
    write_tsv(output / "REGISTRY_ALIASES.tsv", alias_rows, ALIAS_FIELDS)
    write_tsv(
        output / "VOCABULARY.tsv",
        vocabulary_rows,
        ("group", "key", "value", "definition"),
    )

    old_registries = {
        run: run_registry(extensions_by_run[run]) for run in RESULT_RUNS
    }
    rewritten_registry_ids = 0
    rewritten_enums = 0
    for record_id, wrapper in included.items():
        record = json.loads(json.dumps(wrapper["record"]))
        old_registry = old_registries[source_runs[record_id]]
        for item in record["items"]:
            entity_type = REGISTRY_ITEM_TYPES.get(item["type"])
            if entity_type:
                old_id = item.get("registry_id")
                if old_id not in old_registry:
                    raise ValueError(f"{record_id}/{item['id']}: unknown old registry ID {old_id}")
                canonical = old_registry[old_id]["canonical_label"]
                key = (entity_type, normalized_label(canonical))
                if key not in final_registry:
                    raise ValueError(f"{record_id}/{item['id']}: no final registry identity for {canonical}")
                new_id = final_registry[key]
                if new_id != old_id:
                    item["registry_id"] = new_id
                    rewritten_registry_ids += 1
        encoded = json.dumps(record, ensure_ascii=False)
        for old, new in enum_rewrite.items():
            count = encoded.count(f'"{old}"')
            if count:
                encoded = encoded.replace(f'"{old}"', f'"{new}"')
                rewritten_enums += count
        (output / "records" / f"{record_id}.json").write_text(
            json.dumps(json.loads(encoded), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    preparation = {
        row["record_id"]: row for row in read_tsv(PREPARATION_MANIFEST)
    }
    manifest_rows: list[dict[str, str]] = []
    metadata_by_record: dict[str, dict[str, Any]] = {}
    project_links: list[dict[str, str]] = []
    for record_id in sorted(included):
        source = preparation[record_id]
        package = json.loads((PACKAGES / f"{record_id}.json").read_text(encoding="utf-8"))
        metadata_source = ROOT / source["metadata_path"]
        metadata = adapt_metadata(
            record_id,
            json.loads(metadata_source.read_text(encoding="utf-8")),
            package,
        )
        metadata_path = output / "metadata" / f"{record_id}.json"
        metadata_path.write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        metadata_by_record[record_id] = metadata
        publication = metadata["publication"]
        source_format = source["source_format"].casefold()
        row = {
            "record_id": record_id,
            "paper_id": publication["publication_id"],
            "article_path": source["markdown_path"],
            "article_sha256": source["markdown_sha256"],
            "article_bytes": source["markdown_bytes"],
            "xml_path": source["source_path"] if source_format == "xml" else "",
            "xml_sha256": source["source_sha256"] if source_format == "xml" else "",
            "xml_bytes": source["source_bytes"] if source_format == "xml" else "",
            "pdf_path": source["source_path"] if source_format == "pdf" else "",
            "pdf_sha256": source["source_sha256"] if source_format == "pdf" else "",
            "pdf_bytes": source["source_bytes"] if source_format == "pdf" else "",
            "metadata_path": relative(metadata_path),
            "metadata_sha256": digest(metadata_path),
            "project_ids": ";".join(included[record_id]["eligibility"]["project_ids"]),
        }
        manifest_rows.append(row)
        for project_id in included[record_id]["eligibility"]["project_ids"]:
            project_links.append(
                {
                    "project_id": project_id,
                    "publication_id": publication["publication_id"],
                    "project_output": "YES",
                    "support_target": "PUBLICATION",
                    "support_scope": "",
                    "evidence_status": "FULL_TEXT_CONFIRMED_V1",
                }
            )
    write_tsv(output / "MANIFEST.tsv", manifest_rows, MANIFEST_FIELDS)
    write_tsv(
        output / "PROJECT_LINKS.tsv",
        project_links,
        (
            "project_id",
            "publication_id",
            "project_output",
            "support_target",
            "support_scope",
            "evidence_status",
        ),
    )

    openalex_rows = build_openalex_rows(manifest_rows, metadata_by_record)
    openalex_path = output / "openalex-publications.jsonl"
    with openalex_path.open("w", encoding="utf-8") as handle:
        for row in openalex_rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    prepare_people_base(
        output / "person-base",
        {row["publication_id"] for row in openalex_rows},
    )

    report = {
        "results": len(results),
        "included": len(included),
        "excluded": len(results) - len(included),
        "project_links": len(project_links),
        "records_with_project_links": sum(
            bool(value["eligibility"]["project_ids"]) for value in included.values()
        ),
        "registry": registry_report,
        "vocabulary": vocabulary_report,
        "rewritten_registry_ids": rewritten_registry_ids,
        "rewritten_enum_values": rewritten_enums,
        "openalex_exact": sum(row["match_status"] == "EXACT" for row in openalex_rows),
        "openalex_not_found": sum(row["match_status"] == "NOT_FOUND" for row in openalex_rows),
        "hashes": {
            name: digest(output / name)
            for name in (
                "MANIFEST.tsv",
                "PROJECT_LINKS.tsv",
                "REGISTRY.tsv",
                "REGISTRY_ALIASES.tsv",
                "VOCABULARY.tsv",
                "openalex-publications.jsonl",
            )
        },
    }
    (output / "SUMMARY.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
