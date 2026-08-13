#!/usr/bin/env python3
"""Merge unique project leaders and current EuroQol members.

Inputs:
  artefacts/01_authors.csv
  artefacts/00_euroqol_members.csv
Output:
  artefacts/01_people.csv
"""

import csv
import difflib
import pathlib
import unicodedata

from name_utils import key, norm


ROOT = pathlib.Path(__file__).resolve().parent.parent
AUTHORS = ROOT / "artefacts" / "01_authors.csv"
MEMBERS = ROOT / "artefacts" / "00_euroqol_members.csv"
OVERRIDES = ROOT / "data" / "person-name-overrides.csv"
OUT = ROOT / "artefacts" / "01_people.csv"


def plain(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).casefold()


def surname(s: str) -> str:
    return plain(norm(s).split()[-1]).strip(".-")


def semicolon_union(*values: str) -> str:
    items = {x.strip() for value in values for x in value.split(";") if x.strip()}
    return ";".join(sorted(items))


def main():
    aliases = {key(r["alias"]): norm(r["canonical_name"])
               for r in csv.DictReader(open(OVERRIDES))}

    def canonical(name):
        return aliases.get(key(name), norm(name))

    people = {}
    for r in csv.DictReader(open(AUTHORS)):
        name = canonical(r["name"])
        k = key(name)
        p = people.setdefault(k, {
            "name": name,
            "raw_names": "",
            "is_project_leader": "1",
            "is_member": "0",
            "n_projects": "0",
            "project_ids": "",
            "member_id": "",
            "member_affiliation": "",
            "member_profile_url": "",
            "possible_same_person": "",
        })
        p["raw_names"] = semicolon_union(p["raw_names"], r["raw_names"], r["name"])
        p["project_ids"] = semicolon_union(p["project_ids"], r["project_ids"])
        p["n_projects"] = str(len([x for x in p["project_ids"].split(";") if x]))

    seen_member_ids = set()
    for r in csv.DictReader(open(MEMBERS)):
        if r["member_id"] in seen_member_ids:
            raise ValueError(f"duplicate member_id: {r['member_id']}")
        seen_member_ids.add(r["member_id"])
        name = canonical(r["name"])
        k = key(name)
        p = people.setdefault(k, {
            "name": name,
            "raw_names": r["name"],
            "is_project_leader": "0",
            "is_member": "0",
            "n_projects": "0",
            "project_ids": "",
            "member_id": "",
            "member_affiliation": "",
            "member_profile_url": "",
            "possible_same_person": "",
        })
        p["is_member"] = "1"
        p["member_id"] = r["member_id"]
        p["member_affiliation"] = r["institute"]
        p["member_profile_url"] = r["profile_url"]
        p["raw_names"] = semicolon_union(p["raw_names"], r["name"])

    # Do not auto-merge non-identical names. Flag plausible cross-list pairs for review.
    pi_only = [p for p in people.values() if p["is_project_leader"] == "1" and p["is_member"] == "0"]
    member_only = [p for p in people.values() if p["is_project_leader"] == "0" and p["is_member"] == "1"]
    for a in pi_only:
        suggestions = []
        for b in member_only:
            if surname(a["name"]) != surname(b["name"]):
                continue
            ratio = difflib.SequenceMatcher(None, plain(a["name"]), plain(b["name"])).ratio()
            if ratio >= 0.68:
                suggestions.append((ratio, b["name"]))
                b["possible_same_person"] = a["name"]
        if suggestions:
            a["possible_same_person"] = max(suggestions)[1]

    rows = sorted(people.values(), key=lambda p: plain(p["name"]))
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    overlap = sum(p["is_project_leader"] == "1" and p["is_member"] == "1" for p in rows)
    flagged = sum(bool(p["possible_same_person"]) for p in rows)
    print(f"{len(rows)} people; {overlap} project leader+member; {flagged} rows flagged -> {OUT}")


if __name__ == "__main__":
    main()
