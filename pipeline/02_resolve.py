#!/usr/bin/env python3
"""Step 02: artefacts/01_people.csv -> artefacts/02_author_ids.json

Resolve each PI name to an OpenAlex author ID (which carries ORCID when known).
Disambiguation: a candidate counts as a match if they have >=1 work whose
title/abstract mentions EQ-5D / EuroQol / HRQoL / EQ-HWB.

Replayable: every HTTP response is cached in cache/http/ keyed by URL hash,
and the output is rewritten incrementally. Rerunning is near-instant and
idempotent; delete cache files to force a refetch.

Usage: 02_resolve.py [--limit N]
"""
import csv
import copy
import json
import pathlib
import sys
import unicodedata

from oa import api, EQ_SEARCH

ROOT = pathlib.Path(__file__).resolve().parent.parent
IN = ROOT / "artefacts" / "01_people.csv"
OUT = ROOT / "artefacts" / "02_author_ids.json"
MAX_CANDIDATES = 5


def tokens(name: str) -> set:
    n = unicodedata.normalize("NFKD", name)
    n = "".join(ch for ch in n if not unicodedata.combining(ch)).casefold()
    for dash in "‐‑‒–—−":
        n = n.replace(dash, "-")
    return {t.strip(".") for t in n.replace("-", " ").split() if len(t.strip(".")) > 1}


def name_compat(query: str, candidate: str) -> bool:
    """Surname of one must appear among the other's tokens (diacritics-insensitive)."""
    q, c = tokens(query), tokens(candidate)
    if not q or not c:
        return False
    q_last = tokens(query.split()[-1])
    c_last = tokens(candidate.split()[-1])
    return bool((q_last & c) or (c_last & q))


def eq_works_count(author_id: str) -> int:
    d = api("works", **{
        "filter": f"author.id:{author_id},title_and_abstract.search:{EQ_SEARCH}",
        "per-page": 1,
    })
    return d["meta"]["count"]


def resolve_via_works(name: str) -> list:
    """Fallback: find EQ-related works whose raw author name matches, and
    collect the author IDs OpenAlex assigned to those authorships."""
    try:
        d = api("works", **{
            "filter": f"raw_author_name.search:{name},title_and_abstract.search:{EQ_SEARCH}",
            "per-page": 25,
        })
    except Exception:
        return []
    hits = {}
    for w in d["results"]:
        for a in w.get("authorships", []):
            if not (a.get("author") or {}).get("id"):
                continue
            disp = a.get("author", {}).get("display_name") or ""
            raw = a.get("raw_author_name") or disp
            if name_compat(name, raw) or name_compat(name, disp):
                aid = a["author"]["id"].rsplit("/", 1)[-1]
                h = hits.setdefault(aid, {"id": aid, "display_name": disp,
                                          "orcid": a["author"].get("orcid"), "eq_works": 0})
                h["eq_works"] += 1
    return sorted(hits.values(), key=lambda h: -h["eq_works"])


def resolve(name: str) -> dict:
    out = {"name": name, "candidates": [], "chosen": None, "orcid": None, "status": "not_found"}
    d = api("authors", **{"search": name, "per-page": MAX_CANDIDATES})
    for c in d["results"][:MAX_CANDIDATES]:
        cid = c["id"].rsplit("/", 1)[-1]
        insts = c.get("last_known_institutions") or []
        out["candidates"].append({
            "id": cid,
            "display_name": c["display_name"],
            "orcid": c.get("orcid"),
            "works_count": c["works_count"],
            "cited_by_count": c.get("cited_by_count"),
            "affiliation": insts[0]["display_name"] if insts else None,
            "name_compat": name_compat(name, c["display_name"]),
            "eq_works": eq_works_count(cid),
        })
    matched = sorted((c for c in out["candidates"] if c["eq_works"] > 0 and c["name_compat"]),
                     key=lambda c: -c["eq_works"])
    if matched:
        out["chosen"] = matched[0]["id"]
        out["orcid"] = matched[0]["orcid"]
        # multiple strong candidates usually = split OpenAlex profiles of the same person
        runner_up = matched[1]["eq_works"] if len(matched) > 1 else 0
        out["status"] = "ambiguous" if runner_up >= max(2, matched[0]["eq_works"] // 2) else "ok"
        out["also_plausible"] = [c["id"] for c in matched[1:] if c["eq_works"] >= 2]
        return out

    # author search failed us -> try via works
    fb = resolve_via_works(name)
    if fb:
        out["fallback_candidates"] = fb
        out["chosen"] = fb[0]["id"]
        out["orcid"] = fb[0]["orcid"]
        out["status"] = "ok_via_works" if fb[0]["eq_works"] >= 2 else "weak_via_works"
        out["also_plausible"] = [h["id"] for h in fb[1:] if h["eq_works"] >= 2]
    else:
        out["status"] = "unresolved" if out["candidates"] else "not_found"
    return out


def main():
    limit = None
    force_name = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    if "--force-name" in sys.argv:
        force_name = sys.argv[sys.argv.index("--force-name") + 1]

    authors = list(csv.DictReader(open(IN)))
    if force_name:
        authors = [a for a in authors if a["name"] == force_name]
        if not authors:
            raise SystemExit(f"person not found: {force_name}")
    if limit:
        authors = authors[:limit]

    results = {}
    if OUT.exists():
        results = json.load(open(OUT))

    def add_context(result, person):
        result["project_ids"] = [x for x in person.get("project_ids", "").split(";") if x]
        result["is_project_leader"] = person.get("is_project_leader") == "1"
        result["is_member"] = person.get("is_member") == "1"
        result["member_id"] = person.get("member_id", "")
        result["member_affiliation"] = person.get("member_affiliation", "")
        result["member_profile_url"] = person.get("member_profile_url", "")

    for i, a in enumerate(authors):
        name = a["name"]
        if name not in results:
            # Reuse an existing resolution when manually merged aliases agree.
            old = [results[n] for n in (x.strip() for x in a.get("raw_names", "").split(";"))
                   if n in results and results[n].get("status") != "error"]
            chosen = {r.get("chosen") for r in old if r.get("chosen")}
            if old and len(chosen) <= 1:
                results[name] = copy.deepcopy(max(old, key=lambda r: r.get("status") in {"ok", "ok_via_works"}))
                results[name]["name"] = name
                results[name]["reused_from"] = sorted({r.get("name", "") for r in old})
        if name in results and results[name].get("status") != "error" and name != force_name:
            add_context(results[name], a)
            continue
        try:
            results[name] = resolve(name)
        except Exception as e:
            results[name] = {"name": name, "status": "error", "error": str(e)}
        add_context(results[name], a)
        if (i + 1) % 10 == 0 or i == len(authors) - 1:
            OUT.write_text(json.dumps(results, indent=1))
            done = len([n for n in results if n in {x['name'] for x in authors}])
            print(f"{done}/{len(authors)} resolved", flush=True)

    OUT.write_text(json.dumps(results, indent=1))
    from collections import Counter
    names = {a["name"] for a in authors}
    print(Counter(r["status"] for n, r in results.items() if n in names))


if __name__ == "__main__":
    main()
