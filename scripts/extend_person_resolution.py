#!/usr/bin/env python3
"""Extend reviewed person files with authors from a new publication manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any


FILES = (
    "PERSONS.tsv",
    "PERSON_NAMES.tsv",
    "PERSON_IDENTIFIERS.tsv",
    "PROJECT_PERSONS.tsv",
    "PUBLICATION_AUTHORS.tsv",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-directory", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--openalex", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_name(value: str | None) -> str:
    text = unicodedata.normalize("NFKD", value or "")
    text = "".join(character for character in text if not unicodedata.combining(character))
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.casefold()).split())


def normalize_orcid(value: str | None) -> str | None:
    text = (value or "").strip().casefold().replace("https://orcid.org/", "")
    return text or None


def openalex_id(value: str | None) -> str | None:
    text = (value or "").strip().rsplit("/", 1)[-1]
    return text or None


def is_group(value: str) -> bool:
    key = normalize_name(value)
    return any(
        marker in key
        for marker in (
            "collaboration",
            "consortium",
            "project team",
            "research group",
            "study group",
            "working group",
            "quokka",
        )
    )


def align_authors(
    source_authors: list[dict[str, Any]],
    authorships: list[dict[str, Any]],
) -> dict[int, dict[str, Any]]:
    remaining = set(range(len(authorships)))
    aligned: dict[int, dict[str, Any]] = {}
    for source in source_authors:
        source_orcid = normalize_orcid(source.get("orcid"))
        matches = [
            index
            for index in remaining
            if source_orcid
            and normalize_orcid((authorships[index].get("author") or {}).get("orcid"))
            == source_orcid
        ]
        if len(matches) == 1:
            index = matches[0]
            aligned[int(source["order"])] = authorships[index]
            remaining.remove(index)

    for source in source_authors:
        order = int(source["order"])
        if order in aligned:
            continue
        source_name = normalize_name(source.get("display_name"))
        source_family = normalize_name(source.get("family_name"))
        exact = []
        family = []
        for index in remaining:
            authorship = authorships[index]
            author = authorship.get("author") or {}
            names = {
                normalize_name(author.get("display_name")),
                normalize_name(authorship.get("raw_author_name")),
            }
            if source_name and source_name in names:
                exact.append(index)
            if source_family and any(source_family in name for name in names):
                family.append(index)
        matches = exact if len(exact) == 1 else family if len(family) == 1 else []
        if len(matches) == 1:
            index = matches[0]
            aligned[order] = authorships[index]
            remaining.remove(index)
    return aligned


def person_id_for(
    publication_id: str,
    order: int,
    name: str,
    oa_id: str | None,
    orcid: str | None,
    group: bool,
) -> str:
    if group:
        prefix = "group"
    else:
        prefix = "person"
    if oa_id:
        return f"{prefix}:openalex:{oa_id}"
    if orcid:
        return f"{prefix}:orcid:{orcid}"
    key = f"{publication_id}|{order}|{normalize_name(name)}"
    return f"{prefix}:author:{hashlib.sha256(key.encode()).hexdigest()[:16]}"


def main() -> None:
    args = parse_args()
    base = args.base_directory.resolve()
    output = args.output_directory.resolve()
    output.mkdir(parents=True, exist_ok=True)

    tables = {name: read_tsv(base / name) for name in FILES}
    fields = {name: list(tables[name][0]) for name in FILES}
    people = tables["PERSONS.tsv"]
    names = tables["PERSON_NAMES.tsv"]
    identifiers = tables["PERSON_IDENTIFIERS.tsv"]
    authors = tables["PUBLICATION_AUTHORS.tsv"]

    by_openalex: dict[str, set[str]] = defaultdict(set)
    by_orcid: dict[str, set[str]] = defaultdict(set)
    by_exact_name: dict[str, set[str]] = defaultdict(set)
    for person in people:
        by_exact_name[normalize_name(person.get("display_name"))].add(person["person_id"])
        if value := openalex_id(person.get("openalex_id")):
            by_openalex[value].add(person["person_id"])
        if value := normalize_orcid(person.get("orcid")):
            by_orcid[value].add(person["person_id"])
    for row in identifiers:
        if row["scheme"] == "OPENALEX":
            by_openalex[openalex_id(row["value"]) or ""].add(row["person_id"])
        elif row["scheme"] == "ORCID":
            by_orcid[normalize_orcid(row["value"]) or ""].add(row["person_id"])

    openalex_rows = {
        row["publication_id"]: row
        for row in (
            json.loads(line)
            for line in args.openalex.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    }
    manifest = read_tsv(args.manifest.resolve())
    new_people: dict[str, dict[str, Any]] = {}
    new_names: set[tuple[str, str, str, str]] = set()
    new_identifiers: set[tuple[str, str, str, str]] = set()
    new_authors: list[dict[str, Any]] = []
    unresolved = 0
    ambiguous = 0

    for manifest_row in manifest:
        metadata_path = Path(manifest_row["metadata_path"])
        if not metadata_path.is_absolute():
            metadata_path = Path.cwd() / metadata_path
        if digest(metadata_path) != manifest_row["metadata_sha256"]:
            raise ValueError(f"metadata hash mismatch: {manifest_row['record_id']}")
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        publication_id = metadata["publication"]["publication_id"]
        oa_row = openalex_rows.get(publication_id, {})
        aligned = align_authors(metadata["authors"], oa_row.get("authorships") or [])
        for source in metadata["authors"]:
            order = int(source["order"])
            authorship = aligned.get(order) or {}
            oa_author = authorship.get("author") or {}
            oa_id = openalex_id(oa_author.get("id") or source.get("openalex_id"))
            orcid = normalize_orcid(source.get("orcid") or oa_author.get("orcid"))
            display_name = oa_author.get("display_name") or source["display_name"]
            group = is_group(display_name)
            candidates = set()
            if oa_id:
                candidates.update(by_openalex.get(oa_id, set()))
            if orcid:
                candidates.update(by_orcid.get(orcid, set()))
            matched_by_external = bool(candidates)
            name_candidates = by_exact_name.get(normalize_name(display_name), set())
            if not candidates and len(normalize_name(display_name).split()) >= 2:
                candidates.update(name_candidates)
            if not candidates and group and "quokka" in normalize_name(display_name):
                candidates.add("group:quokka-project-team")
            if len(candidates) == 1:
                person_id = next(iter(candidates))
                method = "EXTERNAL_IDENTIFIER" if matched_by_external else "EXACT_CANONICAL_NAME"
                status = "ACCEPTED"
            elif len(candidates) > 1:
                person_id = person_id_for(publication_id, order, display_name, oa_id, orcid, group)
                method = "AMBIGUOUS_EXTERNAL_IDENTIFIER"
                status = "UNRESOLVED"
                ambiguous += 1
            else:
                person_id = person_id_for(publication_id, order, display_name, oa_id, orcid, group)
                method = "NEW_EXTERNAL_IDENTITY" if oa_id or orcid else "PUBLICATION_LOCAL"
                status = "ACCEPTED" if oa_id or orcid or group else "UNRESOLVED"
                if status == "UNRESOLVED":
                    unresolved += 1

            if person_id not in {row["person_id"] for row in people} and person_id not in new_people:
                family_name = source.get("family_name") or display_name.split()[-1]
                given_names = source.get("given_names") or " ".join(display_name.split()[:-1])
                new_people[person_id] = {
                    "person_id": person_id,
                    "display_name": display_name,
                    "family_name": family_name,
                    "given_names": given_names,
                    "orcid": orcid or "",
                    "openalex_id": oa_id or "",
                    "euroqol_member_id": "",
                    "member_affiliation": "",
                    "member_profile_url": "",
                    "membership_observed_date": "",
                    "is_project_leader": "0",
                    "is_euroqol_member": "0",
                    "identity_status": method,
                    "candidate_openalex_id": "",
                    "entity_kind": "GROUP" if group else "PERSON",
                }
            source_id = f"author:{publication_id}:{order}"
            new_authors.append(
                {
                    "publication_id": publication_id,
                    "author_order": order,
                    "source_person_id": source_id,
                    "resolved_person_id": person_id,
                    "source_name": source["display_name"],
                    "source_orcid": normalize_orcid(source.get("orcid")) or "",
                    "openalex_id": oa_id or "",
                    "openalex_name": oa_author.get("display_name") or "",
                    "openalex_orcid": normalize_orcid(oa_author.get("orcid")) or "",
                    "resolution_method": method,
                    "resolution_status": status,
                    "note": "" if order in aligned else "no unique OpenAlex authorship alignment",
                }
            )
            new_names.add((person_id, source["display_name"], "PUBLICATION_NAME", publication_id))
            if oa_author.get("display_name"):
                new_names.add((person_id, oa_author["display_name"], "OPENALEX_NAME", publication_id))
            if oa_id:
                new_identifiers.add((person_id, "OPENALEX", oa_id, publication_id))
                by_openalex[oa_id].add(person_id)
            if orcid:
                new_identifiers.add((person_id, "ORCID", orcid, publication_id))
                by_orcid[orcid].add(person_id)
            by_exact_name[normalize_name(display_name)].add(person_id)

    base_person_ids = {row["person_id"] for row in people}
    identifier_owners: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in identifiers:
        identifier_owners[(row["scheme"], row["value"])].add(row["person_id"])
    for person_id, scheme, value, _ in new_identifiers:
        identifier_owners[(scheme, value)].add(person_id)
    remap: dict[str, str] = {}
    for owners in identifier_owners.values():
        if len(owners) < 2:
            continue
        base_owners = sorted(owners & base_person_ids)
        target = base_owners[0] if len(base_owners) == 1 else sorted(owners)[0]
        for person_id in owners:
            if person_id != target:
                remap[person_id] = target

    def final_person_id(person_id: str) -> str:
        seen: set[str] = set()
        while person_id in remap and person_id not in seen:
            seen.add(person_id)
            person_id = remap[person_id]
        return person_id

    for row in new_authors:
        target = final_person_id(row["resolved_person_id"])
        if target != row["resolved_person_id"]:
            row["resolved_person_id"] = target
            row["resolution_method"] = "EXTERNAL_IDENTIFIER_CONSOLIDATION"
            row["resolution_status"] = "ACCEPTED"
            row["note"] = "merged by a shared OpenAlex or ORCID identifier"
    new_names = {
        (final_person_id(person_id), name, name_type, source)
        for person_id, name, name_type, source in new_names
    }
    consolidated_identifiers: dict[tuple[str, str, str], str] = {}
    for person_id, scheme, value, source in new_identifiers:
        key = (final_person_id(person_id), scheme, value)
        consolidated_identifiers[key] = min(
            source,
            consolidated_identifiers.get(key, source),
        )
    new_identifiers = {
        (person_id, scheme, value, source)
        for (person_id, scheme, value), source in consolidated_identifiers.items()
    }
    new_people = {
        person_id: row
        for person_id, row in new_people.items()
        if final_person_id(person_id) == person_id
    }

    existing_author_keys = {(row["publication_id"], row["author_order"]) for row in authors}
    if any((row["publication_id"], str(row["author_order"])) in existing_author_keys for row in new_authors):
        raise ValueError("new publication authors overlap the base authorship table")

    people.extend(sorted(new_people.values(), key=lambda row: row["person_id"]))
    unique_names: dict[tuple[str, str, str], str] = {}
    for person_id, name, name_type, source in new_names:
        key = (person_id, name, source)
        if key not in unique_names or name_type == "PUBLICATION_NAME":
            unique_names[key] = name_type
    existing_name_keys = {
        (row["person_id"], row["name"], row["source"]) for row in names
    }
    names.extend(
        {
            "person_id": person_id,
            "name": name,
            "name_type": name_type,
            "source": source,
        }
        for (person_id, name, source), name_type in sorted(unique_names.items())
        if (person_id, name, source) not in existing_name_keys
    )
    identifiers.extend(
        {"person_id": person_id, "scheme": scheme, "value": value, "source": source}
        for person_id, scheme, value, source in sorted(new_identifiers)
        if not any(
            row["person_id"] == person_id and row["scheme"] == scheme and row["value"] == value
            for row in identifiers
        )
    )
    authors.extend(new_authors)

    for name in FILES:
        write_tsv(output / name, tables[name], fields[name])
    person_details = {row["person_id"]: row for row in people}
    review_rows = [
        {
            "publication_id": row["publication_id"],
            "author_order": row["author_order"],
            "source_name": row["source_name"],
            "candidate_person_id": row["resolved_person_id"],
            "canonical_name": person_details[row["resolved_person_id"]]["display_name"],
            "resolution_method": row["resolution_method"],
            "resolution_status": row["resolution_status"],
            "note": row["note"],
        }
        for row in new_authors
        if row["resolution_method"]
        in {"EXACT_CANONICAL_NAME", "AMBIGUOUS_EXTERNAL_IDENTIFIER", "PUBLICATION_LOCAL"}
    ]
    review_path = output / "IDENTITY_REVIEW.tsv"
    write_tsv(
        review_path,
        review_rows,
        [
            "publication_id",
            "author_order",
            "source_name",
            "candidate_person_id",
            "canonical_name",
            "resolution_method",
            "resolution_status",
            "note",
        ],
    )
    summary = {
        "base_people": len(tables["PERSONS.tsv"]) - len(new_people),
        "new_people": len(new_people),
        "total_people": len(tables["PERSONS.tsv"]),
        "new_authorships": len(new_authors),
        "unresolved_new_authorships": sum(
            row["resolution_status"] == "UNRESOLVED" for row in new_authors
        ),
        "ambiguous_external_identifiers": sum(
            row["resolution_method"] == "AMBIGUOUS_EXTERNAL_IDENTIFIER"
            for row in new_authors
        ),
        "consolidated_external_identities": len(remap),
        "identity_review_rows": len(review_rows),
        "output_hashes": {name: digest(output / name) for name in FILES},
    }
    (output / "SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
