#!/usr/bin/env python3
"""Step 03: resolved authors -> artefacts/03_works/<author_id>.json
             + artefacts/03_funder_works.json

Fetches every work for every resolved author (chosen + also_plausible split
profiles), and separately all works that acknowledge EuroQol Research
Foundation funding. Applies human overrides from artefacts/02_review.csv
(`override_id` column: empty=accept, A...=replace, SKIP=exclude).

Replayable: per-author output files are skipped if present; underlying HTTP
pages are cached in cache/http/. Delete a file in 03_works/ to refetch one
author; delete cache entries to force network refetch.
"""
import csv
import json
import pathlib

from oa import api_all, EUROQOL_FUNDER

ROOT = pathlib.Path(__file__).resolve().parent.parent
IDS = ROOT / "artefacts" / "02_author_ids.json"
REVIEW = ROOT / "artefacts" / "02_review.csv"
OUT_DIR = ROOT / "artefacts" / "03_works"
FUNDER_OUT = ROOT / "artefacts" / "03_funder_works.json"

# keep works lean; abstract_inverted_index is needed for step-05 topic matching
# NB: OpenAlex renamed grants -> awards/funders (filter: funders.id, not grants.funder)
SELECT = ",".join([
    "id", "doi", "title", "publication_year", "publication_date", "type",
    "authorships", "cited_by_count", "referenced_works", "awards", "funders",
    "primary_location", "topics", "abstract_inverted_index",
])


def author_ids_to_fetch() -> dict:
    """author_id -> list of PI names it belongs to (post-override)."""
    r = json.load(open(IDS))
    overrides = {}
    if REVIEW.exists():
        for row in csv.DictReader(open(REVIEW)):
            if row.get("override_id", "").strip():
                overrides[row["name"]] = row["override_id"].strip()

    out = {}
    for name, v in r.items():
        ov = overrides.get(name, "")
        if ov.upper() == "SKIP":
            continue
        ids = [ov] if ov else ([v["chosen"]] if v.get("chosen") else [])
        ids += [i for i in v.get("also_plausible", []) if i not in ids]
        for aid in ids:
            out.setdefault(aid, []).append(name)
    return out


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    todo = author_ids_to_fetch()
    print(f"{len(todo)} author profiles to fetch")

    done = failed = 0
    for aid, names in sorted(todo.items()):
        p = OUT_DIR / f"{aid}.json"
        if p.exists():
            done += 1
            continue
        try:
            works = api_all("works", **{"filter": f"author.id:{aid}", "select": SELECT})
        except Exception as e:
            print(f"  FAIL {aid} ({'; '.join(names)}): {e}", flush=True)
            failed += 1
            continue
        p.write_text(json.dumps({"author_id": aid, "pi_names": names, "works": works}))
        done += 1
        if done % 20 == 0:
            print(f"  {done}/{len(todo)} authors fetched", flush=True)

    print(f"authors: {done} done, {failed} failed -> {OUT_DIR}")

    if not FUNDER_OUT.exists():
        works = api_all("works", **{"filter": f"funders.id:{EUROQOL_FUNDER}", "select": SELECT})
        FUNDER_OUT.write_text(json.dumps(works))
        print(f"{len(works)} EuroQol-funded works -> {FUNDER_OUT}")

    if failed:
        import sys
        sys.exit(1)  # rerun to pick up the failed authors (done ones are skipped)


if __name__ == "__main__":
    main()
