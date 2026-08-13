#!/usr/bin/env python3
"""Step 04: artefacts/03_works/*.json + 03_funder_works.json
             -> artefacts/04_papers.jsonl (full records, one per line)
             -> artefacts/04_papers.csv   (slim browsing view)

Dedupes works across all fetched authors, reconstructs abstracts from
OpenAlex inverted indexes, links each paper to the resolved PI(s) appearing
in its byline, and flags EuroQol funding acknowledgments (+ award ids).

Replayable: pure function of the step-03 artefacts. No network.
"""
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS_DIR = ROOT / "artefacts" / "03_works"
FUNDER_IN = ROOT / "artefacts" / "03_funder_works.json"
OUT_JSONL = ROOT / "artefacts" / "04_papers.jsonl"
OUT_CSV = ROOT / "artefacts" / "04_papers.csv"
EUROQOL_FUNDER = "F4320323856"


def abstract_text(inv):
    if not inv:
        return None
    pos = [(p, w) for w, ps in inv.items() for p in ps]
    return " ".join(w for _, w in sorted(pos))


def slim(work, pi_map):
    wid = work["id"].rsplit("/", 1)[-1]
    authors, pi_authors = [], []
    for a in work.get("authorships", []):
        au = a.get("author") or {}
        if not au.get("id"):
            continue
        aid = au["id"].rsplit("/", 1)[-1]
        authors.append({"id": aid, "name": au.get("display_name")})
        for pi in pi_map.get(aid, []):
            if pi not in pi_authors:
                pi_authors.append(pi)
    funders = [f["id"].rsplit("/", 1)[-1] for f in work.get("funders") or [] if f.get("id")]
    awards = [{"funder_id": (a.get("funder_id") or "").rsplit("/", 1)[-1] or None,
               "award_id": a.get("funder_award_id"),
               "funder_name": a.get("funder_display_name")}
              for a in work.get("awards") or []]
    eq_funded = EUROQOL_FUNDER in funders
    loc = work.get("primary_location") or {}
    src = loc.get("source") or {}
    return {
        "id": wid,
        "doi": (work.get("doi") or "").replace("https://doi.org/", "") or None,
        "title": work.get("title"),
        "year": work.get("publication_year"),
        "date": work.get("publication_date"),
        "type": work.get("type"),
        "venue": src.get("display_name"),
        "cited_by_count": work.get("cited_by_count"),
        "authors": authors,
        "pi_authors": pi_authors,
        "euroqol_funded": eq_funded,
        "funders": funders,
        "awards": awards,
        "topics": [t["display_name"] for t in (work.get("topics") or [])[:3]],
        "referenced_works": [r.rsplit("/", 1)[-1] for r in work.get("referenced_works") or []],
        "abstract": abstract_text(work.get("abstract_inverted_index")),
    }


def main():
    # author_id -> PI names, straight from the step-03 files (single source of truth)
    pi_map, raw = {}, {}
    for p in sorted(WORKS_DIR.glob("*.json")):
        d = json.loads(p.read_text())
        pi_map[d["author_id"]] = d["pi_names"]
    for p in sorted(WORKS_DIR.glob("*.json")):
        d = json.loads(p.read_text())
        for w in d["works"]:
            raw.setdefault(w["id"], w)
    n_author_works = len(raw)
    if FUNDER_IN.exists():
        for w in json.loads(FUNDER_IN.read_text()):
            raw.setdefault(w["id"], w)

    papers = [slim(w, pi_map) for w in raw.values()]
    papers.sort(key=lambda x: (-(x["year"] or 0), x["id"]))

    with open(OUT_JSONL, "w") as f:
        for p in papers:
            f.write(json.dumps(p) + "\n")
    with open(OUT_CSV, "w", newline="") as f:
        cols = ["year", "title", "venue", "pi_authors", "euroqol_funded",
                "cited_by_count", "doi", "id"]
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for p in papers:
            w.writerow({**{c: p[c] for c in cols if c != "pi_authors"},
                        "pi_authors": "; ".join(p["pi_authors"])})

    eq = sum(1 for p in papers if p["euroqol_funded"])
    with_pi = sum(1 for p in papers if p["pi_authors"])
    print(f"{len(papers)} unique papers ({n_author_works} via authors, "
          f"{len(papers) - n_author_works} funder-only)")
    print(f"  euroqol_funded: {eq}, with >=1 PI author: {with_pi}, "
          f"with abstract: {sum(1 for p in papers if p['abstract'])}")
    print(f"-> {OUT_JSONL}\n-> {OUT_CSV}")


if __name__ == "__main__":
    main()
