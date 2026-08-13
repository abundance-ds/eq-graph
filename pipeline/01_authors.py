#!/usr/bin/env python3
"""Step 01: data/funded-projects-canonical.csv -> artefacts/01_authors.csv

One row per unique PI name (after normalization), with the projects they lead.
Replayable: pure function of the input CSV.
"""
import csv
import pathlib

from name_utils import key, norm

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "funded-projects-canonical.csv"
OUT = ROOT / "artefacts" / "01_authors.csv"
OVERRIDES = ROOT / "data" / "person-name-overrides.csv"


def main():
    rows = list(csv.DictReader(open(SRC)))
    aliases = {key(r["alias"]): norm(r["canonical_name"])
               for r in csv.DictReader(open(OVERRIDES))}
    authors = {}
    for r in rows:
        raw = r["Project PI / Applicant Name"].strip()
        if not raw:
            continue
        name = aliases.get(key(raw), norm(raw))
        a = authors.setdefault(name.casefold(), {"name": name, "raw": set(), "projects": []})
        a["raw"].add(raw)
        a["projects"].append(r["Project Id"])

    OUT.parent.mkdir(exist_ok=True)
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "raw_names", "n_projects", "project_ids"])
        for k in sorted(authors):
            a = authors[k]
            w.writerow([
                a["name"],
                "; ".join(sorted(a["raw"])),
                len(a["projects"]),
                ";".join(a["projects"]),
            ])
    print(f"{len(authors)} unique authors from {len(rows)} projects -> {OUT}")


if __name__ == "__main__":
    main()
