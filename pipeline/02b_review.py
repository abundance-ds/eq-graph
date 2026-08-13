#!/usr/bin/env python3
"""Step 02b: 02_author_ids.json (+01_people.csv) -> artefacts/02_review.csv

Human-review sheet for person -> OpenAlex identity links. Flagged rows first,
then by number of projects (high-stakes authors up top).

The human edits ONLY the `override_id` column:
  - empty        = accept `chosen_id`
  - A....        = use this OpenAlex author id instead
  - SKIP         = exclude this author from downstream steps

Re-running this script preserves existing override_id and manual_note values.
"""
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
IDS = ROOT / "artefacts" / "02_author_ids.json"
PEOPLE = ROOT / "artefacts" / "01_people.csv"
OUT = ROOT / "artefacts" / "02_review.csv"

FLAGGED = {"ambiguous", "weak_via_works", "unresolved", "not_found", "error"}
KNOWN_FLAGS = {
    "yaling yang": "Common-name OpenAlex profile appears contaminated",
    "richard xu": "High-work-count profile: verify identity",
    "jeffrey johnson": "High-work-count profile: verify identity",
}


def main():
    r = json.load(open(IDS))
    people = {row["name"]: row for row in csv.DictReader(open(PEOPLE))}

    old_edits = {}
    if OUT.exists():
        for row in csv.DictReader(open(OUT)):
            old_edits[row["name"]] = {
                "override_id": row.get("override_id", "").strip(),
                "manual_note": row.get("manual_note", "").strip(),
            }

    chosen_names = {}
    for name in people:
        chosen = r[name].get("chosen")
        if chosen:
            chosen_names.setdefault(chosen, []).append(name)

    rows = []
    for name, person in people.items():
        v = r[name]
        chosen = v.get("chosen")
        info = {}
        for c in v.get("candidates", []) + v.get("fallback_candidates", []):
            if c["id"] == chosen:
                info = c
                break
        alts = []
        for c in v.get("candidates", []) + v.get("fallback_candidates", []):
            if c["id"] != chosen and c.get("eq_works", 0) > 0:
                alts.append(f"{c['id']}={c['display_name']}({c['eq_works']} eq)")
        reasons = []
        if v["status"] in FLAGGED:
            reasons.append(v["status"])
        if chosen and len(chosen_names.get(chosen, [])) > 1:
            others = [n for n in chosen_names[chosen] if n != name]
            reasons.append("OpenAlex profile also assigned to " + "; ".join(others))
        if name.casefold() in KNOWN_FLAGS:
            reasons.append(KNOWN_FLAGS[name.casefold()])
        edit = old_edits.get(name, {})
        orcid = (info.get("orcid") or "").replace("https://orcid.org/", "")
        rows.append({
            "review_required": "1" if reasons else "0",
            "review_reason": "; ".join(reasons),
            "status": v["status"],
            "name": name,
            "is_project_leader": person["is_project_leader"],
            "is_member": person["is_member"],
            "n_projects": int(person["n_projects"]),
            "project_ids": person["project_ids"],
            "member_id": person["member_id"],
            "member_affiliation": person["member_affiliation"],
            "member_profile_url": person["member_profile_url"],
            "chosen_id": chosen or "",
            "openalex_url": f"https://openalex.org/{chosen}" if chosen else "",
            "chosen_name": info.get("display_name", ""),
            "orcid": orcid,
            "orcid_url": f"https://orcid.org/{orcid}" if orcid else "",
            "openalex_affiliation": info.get("affiliation") or "",
            "eq_works": info.get("eq_works", ""),
            "total_works": info.get("works_count", ""),
            "alternatives": "; ".join(alts),
            "override_id": edit.get("override_id", ""),
            "manual_note": edit.get("manual_note", ""),
        })

    rows.sort(key=lambda x: (x["review_required"] != "1", -x["n_projects"], x["name"]))
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    flagged = sum(x["review_required"] == "1" for x in rows)
    print(f"{len(rows)} rows ({flagged} flagged for review) -> {OUT}")


if __name__ == "__main__":
    main()
