#!/usr/bin/env python3
"""Reproducible 10-author ORCID vs OpenAlex works comparison."""

import csv
import json
import pathlib
import random
import re
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parent.parent
REVIEW = ROOT / "artefacts" / "02_review.csv"
OA_DIR = ROOT / "artefacts" / "03_works"
ORCID_CACHE = ROOT / "cache" / "orcid"
OUT_JSON = ROOT / "artefacts" / "orcid_openalex_check.json"
OUT_CSV = ROOT / "artefacts" / "orcid_openalex_check.csv"
SEED = 20260801
N = 10


def norm_doi(value):
    if not value:
        return ""
    return value.lower().replace("https://doi.org/", "").replace("http://doi.org/", "").strip()


def norm_title(value):
    return re.sub(r"[^a-z0-9]+", " ", (value or "").casefold()).strip()


def orcid_record(orcid):
    ORCID_CACHE.mkdir(parents=True, exist_ok=True)
    path = ORCID_CACHE / f"{orcid}-works.json"
    if not path.exists():
        request = urllib.request.Request(
            f"https://pub.orcid.org/v3.0/{orcid}/works",
            headers={"Accept": "application/json", "User-Agent": "eq-graph/1.0"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            path.write_bytes(response.read())
    return json.loads(path.read_text())


def orcid_works(record):
    works = []
    for group in record.get("group", []):
        summaries = group.get("work-summary", [])
        summary = next((x for x in summaries if x.get("source", {}).get("source-orcid")), None)
        summary = summary or (summaries[0] if summaries else {})
        title = (((summary.get("title") or {}).get("title") or {}).get("value")) or ""
        year = (((summary.get("publication-date") or {}).get("year") or {}).get("value")) or ""
        dois = []
        for ext in (group.get("external-ids") or {}).get("external-id", []):
            if (ext.get("external-id-type") or "").casefold() == "doi":
                dois.append(norm_doi(ext.get("external-id-value")))
        works.append({"title": title, "year": year, "dois": sorted(set(filter(None, dois)))})
    return works


def openalex_works(author_id):
    data = json.loads((OA_DIR / f"{author_id}.json").read_text())
    return [{
        "id": (w.get("id") or "").rsplit("/", 1)[-1],
        "title": w.get("title") or "",
        "year": w.get("publication_year") or "",
        "doi": norm_doi(w.get("doi")),
    } for w in data.get("works", [])]


def main():
    rows = list(csv.DictReader(open(REVIEW)))
    eligible = [r for r in rows if r["chosen_id"] and r["orcid"]
                and r["review_required"] == "0" and (OA_DIR / f"{r['chosen_id']}.json").exists()]
    sample = random.Random(SEED).sample(sorted(eligible, key=lambda r: r["name"]), N)
    details = []
    summary = []
    for row in sample:
        ow = orcid_works(orcid_record(row["orcid"]))
        aw = openalex_works(row["chosen_id"])
        o_dois = {d for w in ow for d in w["dois"]}
        a_dois = {w["doi"] for w in aw if w["doi"]}
        o_titles = {norm_title(w["title"]) for w in ow if w["title"]}
        a_titles = {norm_title(w["title"]) for w in aw if w["title"]}
        item = {
            "name": row["name"], "openalex_id": row["chosen_id"], "orcid": row["orcid"],
            "openalex_works": aw, "orcid_works": ow,
            "openalex_count": len(aw), "orcid_count": len(ow),
            "count_difference": len(aw) - len(ow),
            "doi_overlap": len(a_dois & o_dois), "title_overlap": len(a_titles & o_titles),
            "openalex_only_dois": sorted(a_dois - o_dois), "orcid_only_dois": sorted(o_dois - a_dois),
        }
        details.append(item)
        summary.append({k: item[k] for k in (
            "name", "openalex_id", "orcid", "openalex_count", "orcid_count",
            "count_difference", "doi_overlap", "title_overlap")})
        print(summary[-1])

    OUT_JSON.write_text(json.dumps({"seed": SEED, "sample_size": N, "authors": details}, indent=1))
    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary[0]))
        writer.writeheader()
        writer.writerows(summary)
    print(f"-> {OUT_CSV}\n-> {OUT_JSON}")


if __name__ == "__main__":
    main()
