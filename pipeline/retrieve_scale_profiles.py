#!/usr/bin/env python3
"""Retrieve missing OpenAlex works for scale-ready author profiles only."""

import csv
import json
import pathlib

from oa import api_all


ROOT = pathlib.Path(__file__).resolve().parent.parent
READINESS = ROOT / "scale" / "protocol-2.0" / "profile-scale-readiness.csv"
OUT = ROOT / "artefacts" / "03_works"
SELECT = ",".join([
    "id", "doi", "title", "publication_year", "publication_date", "type",
    "authorships", "cited_by_count", "referenced_works", "awards", "funders",
    "primary_location", "topics", "abstract_inverted_index",
])


def main():
    ready = {}
    with READINESS.open(newline="") as handle:
        for row in csv.DictReader(handle):
            if row["scale_status"] == "ready":
                ready.setdefault(row["chosen_id"], []).append(row["name"])
    OUT.mkdir(parents=True, exist_ok=True)
    missing = [author_id for author_id in sorted(ready) if not (OUT / f"{author_id}.json").exists()]
    print(f"scale-ready profiles: {len(ready)}; missing: {len(missing)}", flush=True)
    failures = []
    for index, author_id in enumerate(missing, 1):
        try:
            works = api_all(
                "works", filter=f"author.id:{author_id}", select=SELECT
            )
        except Exception as error:
            failures.append({"author_id": author_id, "error": str(error)})
            print(f"FAIL {author_id}: {error}", flush=True)
            continue
        path = OUT / f"{author_id}.json"
        path.write_text(json.dumps({
            "author_id": author_id,
            "pi_names": ready[author_id],
            "works": works,
        }))
        print(f"{index}/{len(missing)} {author_id}: {len(works)} works", flush=True)
    result = {
        "scale_ready_profiles": len(ready),
        "missing_before_run": len(missing),
        "retrieved": len(missing) - len(failures),
        "failures": failures,
    }
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
