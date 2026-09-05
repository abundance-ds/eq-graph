#!/usr/bin/env python3
"""Build canonical people and cautious project/publication identity links."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


AFFILIATION_STOPWORDS = {
    "and", "centre", "center", "college", "department", "faculty", "for",
    "health", "hospital", "institute", "institution", "of", "research",
    "school", "the", "university",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--people-source", type=Path, required=True)
    parser.add_argument("--profile-review", type=Path, required=True)
    parser.add_argument("--profile-accepted", type=Path, required=True)
    parser.add_argument("--name-overrides", type=Path, required=True)
    parser.add_argument("--authorship-overrides", type=Path, required=True)
    parser.add_argument("--openalex", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--membership-observed-date", required=True)
    return parser.parse_args()


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def normalize_name(value: str | None) -> str:
    text = unicodedata.normalize("NFKD", value or "")
    text = "".join(character for character in text if not unicodedata.combining(character))
    text = text.casefold()
    text = re.sub(r"\b(?:professor|prof|doctor|dr|phd|msc|md)\b", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def normalize_orcid(value: str | None) -> str | None:
    text = (value or "").strip().casefold().replace("https://orcid.org/", "")
    return text or None


def short_hash(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()[:12]


def affiliation_tokens(value: str | None) -> set[str]:
    tokens = normalize_name(value).split()
    return {
        token[:-1] if token.endswith("s") and len(token) > 5 else token
        for token in tokens
        if len(token) > 3 and token not in AFFILIATION_STOPWORDS
    }


def is_collective_author(value: str) -> bool:
    key = normalize_name(value)
    return key.endswith(" group") or any(
        marker in key
        for marker in (
            "study group", "project team", "research group", "collaboration",
            "collaborative group", "consortium", "working group",
        )
    )


def collective_key(value: str) -> str:
    key = normalize_name(value)
    for marker, canonical in (
        ("quokka", "quokka-project-team"),
        ("eurosca", "eurosca-study-group"),
        ("esmi", "esmi-study-group"),
        ("impact hta hrqol", "impact-hta-hrqol-group"),
        ("swedish quality register", "swedish-quality-register-study-group"),
        ("eq daphnie", "eq-daphnie-project-team"),
    ):
        if marker in key:
            return canonical
    return short_hash(key)


def canonical_person_id(row: dict[str, str]) -> str:
    if row["member_id"]:
        return f"person:eqmember:{row['member_id']}"
    return f"person:leader:{short_hash(normalize_name(row['name']))}"


def oa_author_values(authorship: dict[str, Any]) -> tuple[str | None, str, str | None]:
    author = authorship.get("author") or {}
    openalex_id = (author.get("id") or "").rsplit("/", 1)[-1] or None
    display_name = author.get("display_name") or authorship.get("raw_author_name") or ""
    orcid = normalize_orcid(author.get("orcid"))
    return openalex_id, display_name, orcid


def align_openalex_author(
    author_name: str,
    author_orcid: str | None,
    authorships: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str, str]:
    if author_orcid:
        matches = [row for row in authorships if oa_author_values(row)[2] == author_orcid]
        if len(matches) == 1:
            return matches[0], "OPENALEX_ORCID", ""
        if len(matches) > 1:
            return None, "", "multiple OpenAlex authorships share the JATS ORCID"
    key = normalize_name(author_name)
    matches = []
    for row in authorships:
        _, display_name, _ = oa_author_values(row)
        raw_name = row.get("raw_author_name") or ""
        if key and key in {normalize_name(display_name), normalize_name(raw_name)}:
            matches.append(row)
    if len(matches) == 1:
        return matches[0], "OPENALEX_EXACT_NAME", ""
    if len(matches) > 1:
        return None, "", "multiple OpenAlex authorships share the normalized name"
    return None, "", "no exact OpenAlex authorship match"


def write_tsv(path: Path, fields: tuple[str, ...], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    source_people = read_csv(args.people_source)
    profile_review = {row["name"]: row for row in read_csv(args.profile_review)}
    profile_accepted = {row["name"]: row for row in read_csv(args.profile_accepted)}
    override_rows = read_csv(args.name_overrides)
    authorship_overrides = {
        (row["publication_id"], int(row["author_order"])): row
        for row in read_csv(args.authorship_overrides)
    }
    openalex_rows = {
        row["publication_id"]: row
        for row in (
            json.loads(line)
            for line in args.openalex.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    }

    connection = sqlite3.connect(f"file:{args.database.resolve()}?mode=ro", uri=True)
    projects = {
        row[0]: {"title": row[1], "principal_investigator": row[2]}
        for row in connection.execute(
            "SELECT project_id, title, principal_investigator FROM project"
        )
    }
    publications = {
        row[0]: {"doi": row[1], "title": row[2]}
        for row in connection.execute("SELECT publication_id, doi, title FROM publication")
    }
    source_authors = [
        {
            "publication_id": row[0],
            "source_person_id": row[1],
            "display_name": row[2],
            "author_order": row[3],
            "orcid": normalize_orcid(row[4]),
            "family_name": row[5],
            "given_names": row[6],
        }
        for row in connection.execute(
            """
            SELECT pa.publication_id, pa.person_id, pa.display_name, pa.author_order,
                   p.orcid, p.family_name, p.given_names
            FROM publication_author AS pa
            JOIN person AS p USING (person_id)
            ORDER BY pa.publication_id, pa.author_order
            """
        )
    ]
    project_publications: dict[str, set[str]] = defaultdict(set)
    for project_id, publication_id in connection.execute(
        "SELECT project_id, publication_id FROM project_publication"
    ):
        project_publications[publication_id].add(project_id)
    author_affiliations: dict[tuple[str, str], list[str]] = defaultdict(list)
    for publication_id, person_id, affiliation in connection.execute(
        """
        SELECT aa.publication_id, aa.person_id, a.name
        FROM author_affiliation AS aa
        JOIN affiliation AS a USING (affiliation_id)
        """
    ):
        author_affiliations[(publication_id, person_id)].append(affiliation)
    connection.close()

    canonical_rows: list[dict[str, Any]] = []
    canonical_by_name: dict[str, set[str]] = defaultdict(set)
    canonical_by_openalex: dict[str, set[str]] = defaultdict(set)
    canonical_by_orcid: dict[str, set[str]] = defaultdict(set)
    person_alias_rows: list[dict[str, Any]] = []
    project_person_rows: list[dict[str, Any]] = []
    canonical_by_display: dict[str, str] = {}
    canonical_details: dict[str, dict[str, Any]] = {}
    person_projects: dict[str, set[str]] = defaultdict(set)
    for row in source_people:
        person_id = canonical_person_id(row)
        canonical_by_display[row["name"]] = person_id
        accepted = profile_accepted.get(row["name"])
        reviewed = profile_review.get(row["name"], {})
        openalex_id = accepted["openalex_id"] if accepted else ""
        reviewed_orcid = (
            normalize_orcid(reviewed.get("orcid"))
            if reviewed.get("status") in {"ok", "ok_via_works", "weak_via_works"}
            and reviewed.get("review_required") == "0"
            else None
        )
        orcid = normalize_orcid(accepted.get("orcid")) if accepted else reviewed_orcid
        if accepted:
            identity_status = "PROFILE_ACCEPTED"
        elif reviewed.get("chosen_id"):
            identity_status = "PROFILE_NOT_ACCEPTED_FOR_DISCOVERY"
        else:
            identity_status = "NO_EXTERNAL_PROFILE"
        canonical_rows.append(
            {
                "person_id": person_id,
                "display_name": row["name"],
                "family_name": row["name"].split()[-1] if row["name"] else "",
                "given_names": " ".join(row["name"].split()[:-1]),
                "orcid": orcid or "",
                "openalex_id": openalex_id,
                "euroqol_member_id": row["member_id"],
                "member_affiliation": row["member_affiliation"],
                "member_profile_url": row["member_profile_url"],
                "membership_observed_date": args.membership_observed_date if row["is_member"] == "1" else "",
                "is_project_leader": row["is_project_leader"],
                "is_euroqol_member": row["is_member"],
                "identity_status": identity_status,
                "candidate_openalex_id": reviewed.get("chosen_id", "") if not accepted else "",
                "entity_kind": "PERSON",
            }
        )
        canonical_details[person_id] = {
            "reviewed_openalex_id": reviewed.get("chosen_id", ""),
            "review_required": reviewed.get("review_required", "1"),
            "affiliations": " | ".join(
                value
                for value in (
                    row["member_affiliation"],
                    accepted.get("affiliation", "") if accepted else "",
                    reviewed.get("openalex_affiliation", ""),
                )
                if value
            ),
        }
        names = {row["name"]}
        names.update(value.strip() for value in row["raw_names"].split(";") if value.strip())
        if reviewed.get("chosen_name"):
            names.add(reviewed["chosen_name"])
        if accepted and accepted.get("chosen_name"):
            names.add(accepted["chosen_name"])
        for name in sorted(names):
            canonical_by_name[normalize_name(name)].add(person_id)
            person_alias_rows.append(
                {
                    "person_id": person_id,
                    "name": name,
                    "name_type": "CANONICAL" if name == row["name"] else "SOURCE_ALIAS",
                    "source": "artefacts/01_people.csv",
                }
            )
        if openalex_id:
            canonical_by_openalex[openalex_id].add(person_id)
        if orcid:
            canonical_by_orcid[orcid].add(person_id)
        for project_id in [value for value in row["project_ids"].split(";") if value]:
            if project_id not in projects:
                raise ValueError(f"Unknown project in people source: {project_id}")
            project_person_rows.append(
                {
                    "project_id": project_id,
                    "person_id": person_id,
                    "role": "PRINCIPAL_INVESTIGATOR",
                    "source_name": projects[project_id]["principal_investigator"],
                    "resolution_method": "CANONICAL_PROJECT_SOURCE",
                    "resolution_status": "ACCEPTED",
                }
            )
            person_projects[person_id].add(project_id)

    for row in override_rows:
        person_id = canonical_by_display.get(row["canonical_name"])
        if person_id:
            canonical_by_name[normalize_name(row["alias"])].add(person_id)
            person_alias_rows.append(
                {
                    "person_id": person_id,
                    "name": row["alias"],
                    "name_type": "REVIEWED_ALIAS",
                    "source": "data/person-name-overrides.csv",
                }
            )

    if len(project_person_rows) != len(projects):
        covered = Counter(row["project_id"] for row in project_person_rows)
        missing = sorted(set(projects) - set(covered))
        duplicates = sorted(key for key, count in covered.items() if count != 1)
        raise ValueError(f"Project-person coverage failure: missing={missing}, duplicates={duplicates}")
    for mapping in (canonical_by_openalex, canonical_by_orcid):
        conflicts = {key: value for key, value in mapping.items() if len(value) > 1}
        if conflicts:
            raise ValueError(f"Canonical external identifier conflicts: {conflicts}")

    aligned_rows: list[dict[str, Any]] = []
    for source in source_authors:
        oa_record = openalex_rows.get(source["publication_id"], {})
        authorship, oa_method, oa_note = align_openalex_author(
            source["display_name"], source["orcid"], oa_record.get("authorships") or []
        )
        if authorship:
            oa_id, oa_name, oa_orcid = oa_author_values(authorship)
        else:
            oa_id, oa_name, oa_orcid = None, "", None
        aligned_rows.append(
            {
                **source,
                "openalex_id": oa_id or "",
                "openalex_name": oa_name,
                "openalex_orcid": oa_orcid or "",
                "openalex_alignment": oa_method,
                "openalex_note": oa_note,
            }
        )

    orcid_to_openalex: dict[str, set[str]] = defaultdict(set)
    for row in aligned_rows:
        orcid = row["orcid"] or row["openalex_orcid"]
        if orcid and row["openalex_id"]:
            orcid_to_openalex[orcid].add(row["openalex_id"])

    author_person_rows: dict[str, dict[str, Any]] = {}
    author_link_rows: list[dict[str, Any]] = []
    review_rows: list[dict[str, Any]] = []
    repeated_names = Counter(normalize_name(row["display_name"]) for row in aligned_rows)
    for row in aligned_rows:
        candidates: set[str] = set()
        method = ""
        if is_collective_author(row["display_name"]):
            person_id = f"group:{collective_key(row['display_name'])}"
            method = "COLLECTIVE_AUTHOR"
            status = "ACCEPTED"
            note = ""
            candidates = set()
            name_candidates = set()
        else:
            person_id = ""
            status = ""
            note = ""
        if not person_id and row["openalex_id"] and row["openalex_id"] in canonical_by_openalex:
            candidates.update(canonical_by_openalex[row["openalex_id"]])
            method = "CANONICAL_OPENALEX_ID"
        external_orcid = row["orcid"] or row["openalex_orcid"]
        if not person_id and external_orcid and external_orcid in canonical_by_orcid:
            candidates.update(canonical_by_orcid[external_orcid])
            method = "CANONICAL_ORCID"
        name_candidates = (
            canonical_by_name.get(normalize_name(row["display_name"]), set())
            if not person_id else set()
        )
        if not person_id and not candidates and len(name_candidates) == 1:
            candidate_id = next(iter(name_candidates))
            candidate = next(item for item in canonical_rows if item["person_id"] == candidate_id)
            detail = canonical_details[candidate_id]
            source_affiliation_text = " | ".join(
                author_affiliations[(row["publication_id"], row["source_person_id"])]
            )
            affiliation_match = bool(
                affiliation_tokens(source_affiliation_text)
                & affiliation_tokens(detail["affiliations"])
            )
            direct_project_match = bool(
                person_projects[candidate_id] & project_publications[row["publication_id"]]
            )
            if candidate["openalex_id"] and row["openalex_id"] == candidate["openalex_id"]:
                candidates.add(candidate_id)
                method = "CANONICAL_NAME_AND_OPENALEX"
            elif candidate["orcid"] and external_orcid == candidate["orcid"]:
                candidates.add(candidate_id)
                method = "CANONICAL_NAME_AND_ORCID"
            elif direct_project_match:
                candidates.add(candidate_id)
                method = "CANONICAL_NAME_AND_LINKED_PROJECT"
            elif affiliation_match:
                candidates.add(candidate_id)
                method = "CANONICAL_NAME_AND_AFFILIATION"
            elif (
                detail["review_required"] == "0"
                and row["openalex_id"]
                and row["openalex_id"] == detail["reviewed_openalex_id"]
            ):
                candidates.add(candidate_id)
                method = "CANONICAL_NAME_AND_REVIEWED_OPENALEX"
        if person_id:
            pass
        elif len(candidates) == 1:
            person_id = next(iter(candidates))
            status = "ACCEPTED"
            note = ""
        elif len(candidates) > 1:
            person_id = f"person:author:{row['publication_id']}:{row['author_order']}"
            status = "REVIEW_REQUIRED"
            method = "CANONICAL_IDENTITY_CONFLICT"
            note = "multiple canonical people match the external identifiers"
        else:
            if external_orcid:
                person_id = f"person:orcid:{external_orcid}"
                method = "AUTHOR_ORCID"
            elif row["openalex_id"]:
                person_id = f"person:openalex:{row['openalex_id']}"
                method = "AUTHOR_OPENALEX_ID"
            else:
                person_id = f"person:author:{row['publication_id']}:{row['author_order']}"
                method = "PUBLICATION_LOCAL"
            status = "ACCEPTED" if method != "PUBLICATION_LOCAL" else "UNRESOLVED"
            note = row["openalex_note"]

        if person_id not in {item["person_id"] for item in canonical_rows}:
            current = author_person_rows.get(person_id)
            candidate_person = {
                "person_id": person_id,
                "display_name": row["openalex_name"] or row["display_name"],
                "family_name": row["family_name"] or "",
                "given_names": row["given_names"] or "",
                "orcid": external_orcid or "",
                "openalex_id": row["openalex_id"],
                "euroqol_member_id": "",
                "member_affiliation": "",
                "member_profile_url": "",
                "membership_observed_date": "",
                "is_project_leader": "0",
                "is_euroqol_member": "0",
                "identity_status": "AUTHOR_EXTERNAL_ID" if status == "ACCEPTED" else "AUTHOR_LOCAL",
                "candidate_openalex_id": "",
                "entity_kind": "GROUP" if method == "COLLECTIVE_AUTHOR" else "PERSON",
            }
            if current and current["orcid"] and candidate_person["orcid"] and current["orcid"] != candidate_person["orcid"]:
                raise ValueError(f"Conflicting ORCIDs for {person_id}")
            author_person_rows.setdefault(person_id, candidate_person)

        author_link = {
            "publication_id": row["publication_id"],
            "author_order": row["author_order"],
            "source_person_id": row["source_person_id"],
            "resolved_person_id": person_id,
            "source_name": row["display_name"],
            "source_orcid": row["orcid"] or "",
            "openalex_id": row["openalex_id"],
            "openalex_name": row["openalex_name"],
            "openalex_orcid": row["openalex_orcid"],
            "resolution_method": method,
            "resolution_status": status,
            "note": note,
        }
        author_link_rows.append(author_link)
        potential_canonical = bool(name_candidates) and not candidates
        repeated_unresolved = status == "UNRESOLVED" and repeated_names[normalize_name(row["display_name"])] > 1
        if status == "REVIEW_REQUIRED" or potential_canonical or repeated_unresolved:
            review_rows.append(
                {
                    **author_link,
                    "doi": publications[row["publication_id"]]["doi"],
                    "publication_title": publications[row["publication_id"]]["title"],
                    "canonical_candidates": ";".join(sorted(name_candidates)),
                    "review_reason": (
                        "CANONICAL_NAME_WITHOUT_CONFIRMED_EXTERNAL_ID"
                        if potential_canonical
                        else "REPEATED_UNRESOLVED_AUTHOR_NAME"
                        if repeated_unresolved
                        else "IDENTITY_CONFLICT"
                    ),
                }
            )

    canonical_ids = {row["person_id"] for row in canonical_rows}
    trusted_openalex: dict[str, set[str]] = defaultdict(set)
    trusted_names: dict[str, set[str]] = defaultdict(set)
    for link in author_link_rows:
        if link["resolved_person_id"] not in canonical_ids:
            continue
        if link["openalex_id"]:
            trusted_openalex[link["openalex_id"]].add(link["resolved_person_id"])
        trusted_names[normalize_name(link["source_name"])].add(link["resolved_person_id"])
    for link in author_link_rows:
        if link["resolved_person_id"] in canonical_ids:
            continue
        name_candidates = canonical_by_name.get(normalize_name(link["source_name"]), set())
        if len(name_candidates) != 1:
            continue
        candidate_id = next(iter(name_candidates))
        oa_candidates = trusted_openalex.get(link["openalex_id"], set())
        name_evidence = trusted_names.get(normalize_name(link["source_name"]), set())
        if link["openalex_id"] and oa_candidates == {candidate_id}:
            link["resolved_person_id"] = candidate_id
            link["resolution_method"] = "CANONICAL_PROPAGATED_OPENALEX"
            link["resolution_status"] = "ACCEPTED"
            link["note"] = "same OpenAlex author occurs in a source-confirmed canonical paper"
        elif name_evidence == {candidate_id}:
            link["resolved_person_id"] = candidate_id
            link["resolution_method"] = "CANONICAL_PROPAGATED_EXACT_NAME"
            link["resolution_status"] = "ACCEPTED"
            link["note"] = "exact name recurs after source-confirmed canonical linkage"

    author_links_by_key = {
        (row["publication_id"], int(row["author_order"])): row
        for row in author_link_rows
    }
    missing_override_keys = sorted(set(authorship_overrides) - set(author_links_by_key))
    if missing_override_keys:
        raise ValueError(f"Unknown authorship override keys: {missing_override_keys}")
    for key, override in authorship_overrides.items():
        link = author_links_by_key[key]
        action = override["action"]
        if action == "MERGE":
            target = override["target_person_id"]
            if not target:
                raise ValueError(f"MERGE override has no target: {key}")
            link["resolved_person_id"] = target
            link["resolution_method"] = "REVIEWED_AUTHORSHIP_MERGE"
            link["resolution_status"] = "ACCEPTED"
        elif action == "ACCEPT_DISTINCT":
            if override["target_person_id"]:
                raise ValueError(f"ACCEPT_DISTINCT override has a target: {key}")
            link["resolution_method"] = "SOURCE_DISTINCT_SAME_NAME"
            link["resolution_status"] = "ACCEPTED"
        else:
            raise ValueError(f"Unknown authorship override action {action}: {key}")
        link["note"] = override["reason"]
        if override["display_name"]:
            link["resolved_display_name"] = override["display_name"]

    all_known_ids = canonical_ids | set(author_person_rows)
    unknown_override_targets = sorted(
        {
            row["resolved_person_id"]
            for row in author_link_rows
            if row["resolved_person_id"] not in all_known_ids
        }
    )
    if unknown_override_targets:
        raise ValueError(f"Authorship overrides use unknown people: {unknown_override_targets}")

    # Apply reviewed display names and external identifiers to the retained identity.
    person_rows_by_id = {
        row["person_id"]: row for row in canonical_rows
    } | author_person_rows
    identifiers: dict[tuple[str, str, str], dict[str, str]] = {}
    for link in author_link_rows:
        person_id = link["resolved_person_id"]
        person_row = person_rows_by_id[person_id]
        if link.get("resolved_display_name"):
            person_row["display_name"] = link["resolved_display_name"]
            person_row["given_names"] = " ".join(link["resolved_display_name"].split()[:-1])
            person_row["family_name"] = link["resolved_display_name"].split()[-1]
        for scheme, value in (
            ("ORCID", link["source_orcid"] or link["openalex_orcid"]),
            ("OPENALEX", link["openalex_id"]),
        ):
            if not value:
                continue
            identifiers[(person_id, scheme, value)] = {
                "person_id": person_id,
                "scheme": scheme,
                "value": value,
                "source": link["publication_id"],
            }
        orcids = {
            value for pid, scheme, value in identifiers if pid == person_id and scheme == "ORCID"
        }
        if len(orcids) == 1 and not person_row["orcid"]:
            person_row["orcid"] = next(iter(orcids))
        openalex_ids = {
            value for pid, scheme, value in identifiers if pid == person_id and scheme == "OPENALEX"
        }
        if len(openalex_ids) == 1 and not person_row["openalex_id"]:
            person_row["openalex_id"] = next(iter(openalex_ids))

    review_rows = []
    for link in author_link_rows:
        name_candidates = canonical_by_name.get(normalize_name(link["source_name"]), set())
        potential_canonical = bool(name_candidates) and link["resolved_person_id"] not in canonical_ids
        repeated_unresolved = (
            link["resolution_status"] == "UNRESOLVED"
            and repeated_names[normalize_name(link["source_name"])] > 1
        )
        if link["resolution_status"] == "REVIEW_REQUIRED" or potential_canonical or repeated_unresolved:
            review_rows.append(
                {
                    **link,
                    "doi": publications[link["publication_id"]]["doi"],
                    "publication_title": publications[link["publication_id"]]["title"],
                    "canonical_candidates": ";".join(sorted(name_candidates)),
                    "review_reason": (
                        "CANONICAL_NAME_WITHOUT_CONFIRMED_EXTERNAL_ID"
                        if potential_canonical
                        else "REPEATED_UNRESOLVED_AUTHOR_NAME"
                        if repeated_unresolved
                        else "IDENTITY_CONFLICT"
                    ),
                }
            )

    used_author_person_ids = {
        row["resolved_person_id"] for row in author_link_rows if row["resolved_person_id"] not in canonical_ids
    }
    author_person_rows = {
        person_id: row
        for person_id, row in author_person_rows.items()
        if person_id in used_author_person_ids
    }
    all_person_rows = canonical_rows + sorted(author_person_rows.values(), key=lambda row: row["person_id"])
    person_alias_rows.extend(
        {
            "person_id": row["resolved_person_id"],
            "name": row["source_name"],
            "name_type": "PUBLICATION_NAME",
            "source": row["publication_id"],
        }
        for row in author_link_rows
    )
    person_alias_rows = list(
        {
            (row["person_id"], row["name"], row["source"]): row
            for row in person_alias_rows
        }.values()
    )
    if len({row["person_id"] for row in all_person_rows}) != len(all_person_rows):
        raise ValueError("Duplicate resolved person_id")
    authorship_keys = {(row["publication_id"], row["author_order"]) for row in author_link_rows}
    if len(authorship_keys) != len(source_authors):
        raise ValueError("Authorship mapping is not one-to-one")
    duplicate_publication_people = [
        key
        for key, count in Counter(
            (row["publication_id"], row["resolved_person_id"]) for row in author_link_rows
        ).items()
        if count > 1
    ]
    if duplicate_publication_people:
        raise ValueError(f"A publication maps two authors to one person: {duplicate_publication_people}")

    output = args.output_directory
    write_tsv(
        output / "PERSONS.tsv",
        (
            "person_id", "display_name", "family_name", "given_names", "orcid",
            "openalex_id", "euroqol_member_id", "member_affiliation",
            "member_profile_url", "membership_observed_date", "is_project_leader",
            "is_euroqol_member", "identity_status", "candidate_openalex_id", "entity_kind",
        ),
        all_person_rows,
    )
    write_tsv(
        output / "PERSON_NAMES.tsv",
        ("person_id", "name", "name_type", "source"),
        sorted(person_alias_rows, key=lambda row: (row["person_id"], row["name"], row["source"])),
    )
    write_tsv(
        output / "PERSON_IDENTIFIERS.tsv",
        ("person_id", "scheme", "value", "source"),
        sorted(identifiers.values(), key=lambda row: (row["person_id"], row["scheme"], row["value"])),
    )
    write_tsv(
        output / "PROJECT_PERSONS.tsv",
        ("project_id", "person_id", "role", "source_name", "resolution_method", "resolution_status"),
        sorted(project_person_rows, key=lambda row: row["project_id"]),
    )
    write_tsv(
        output / "PUBLICATION_AUTHORS.tsv",
        (
            "publication_id", "author_order", "source_person_id", "resolved_person_id",
            "source_name", "source_orcid", "openalex_id", "openalex_name",
            "openalex_orcid", "resolution_method", "resolution_status", "note",
        ),
        author_link_rows,
    )
    write_tsv(
        output / "IDENTITY_REVIEW.tsv",
        (
            "publication_id", "doi", "publication_title", "author_order", "source_name",
            "source_orcid", "openalex_id", "openalex_name", "openalex_orcid",
            "resolved_person_id", "canonical_candidates", "resolution_method",
            "resolution_status", "review_reason", "note",
        ),
        review_rows,
    )
    leader_ids = {row["person_id"] for row in canonical_rows if row["is_project_leader"] == "1"}
    member_ids = {row["person_id"] for row in canonical_rows if row["is_euroqol_member"] == "1"}
    summary = {
        "projects": len(projects),
        "project_person_links": len(project_person_rows),
        "project_leaders": len(leader_ids),
        "euroqol_members": len(member_ids),
        "leaders_and_members": len(leader_ids & member_ids),
        "publication_authorships": len(author_link_rows),
        "resolved_people": len(all_person_rows),
        "authorship_resolution": dict(sorted(Counter(row["resolution_method"] for row in author_link_rows).items())),
        "authorship_status": dict(sorted(Counter(row["resolution_status"] for row in author_link_rows).items())),
        "identity_review_rows": len(review_rows),
        "openalex_publications": dict(sorted(Counter(row["match_status"] for row in openalex_rows.values()).items())),
    }
    (output / "SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
