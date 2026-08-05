#!/usr/bin/env python3
"""Step 05: 04_papers.jsonl + funded-projects.csv (+02_author_ids.json)
             -> artefacts/05_matches.jsonl

Links papers to funded projects. Candidate pairs are gated, never all x all:
  tier "award"  paper's EuroQol award_id matches a Project Id (normalized)
  tier "pi"     paper author is the project's PI (via resolved identities)
  tier "funder" paper acknowledges EuroQol funding but has no resolved PI
                author -> compared against all projects

Signals per pair (all kept, threshold later):
  cos        TF-IDF cosine of title+abstract vs project title+abstract
  dt         paper year - project start year (start known only for
             year-prefixed Project Ids; None otherwise)
  eq_funded  paper formally acknowledges EuroQol funding
  score      0-1 combination; tier "award" pins 1.0

Hard filter for pi/funder tiers when both years known: -1 <= dt <= 8.
Replayable: pure function of prior artefacts, no network.
"""
import csv
import json
import math
import pathlib
import re
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPERS = ROOT / "artefacts" / "04_papers.jsonl"
IDS = ROOT / "artefacts" / "02_author_ids.json"
PROJECTS = ROOT / "data" / "funded-projects.csv"
OUT = ROOT / "artefacts" / "05_matches.jsonl"

STOP = set("""a an the and or of in on for with to from by at as is are was were be been
this that these those we our it its their his her have has had not no than then into
using use used based study studies results result method methods aim aims objective
objectives background conclusion conclusions patients patient health quality life
""".split())

WORD = re.compile(r"[a-z0-9]+")
PID_PAT = re.compile(r"\b(\d{1,4}-[A-Z]{1,5}|(?:19|20)\d{5})\b")


def toks(text):
    return [t for t in WORD.findall((text or "").lower()) if t not in STOP and len(t) > 2]


def tfidf(tokens, df, n_docs):
    tf = Counter(tokens)
    v = {t: (1 + math.log(c)) * math.log(n_docs / (1 + df[t])) for t, c in tf.items()}
    norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return {t: x / norm for t, x in v.items()}


def cos(a, b):
    if len(b) < len(a):
        a, b = b, a
    return sum(x * b.get(t, 0.0) for t, x in a.items())


def main():
    projects = {}
    for r in csv.DictReader(open(PROJECTS)):
        pid = r["Project Id"]
        m = re.match(r"^(19|20)\d{2}", pid)
        projects[pid] = {
            "pid": pid,
            "year": int(m.group(0)) if m else None,
            "text": toks(r["Title"] + " " + r["Abstract"]),
            "pi": r["Project PI / Applicant Name"].strip(),
        }

    pi_projects = {}  # resolved PI name -> [project ids]
    for name, v in json.load(open(IDS)).items():
        pi_projects[name] = v.get("project_ids", [])

    papers = []
    with open(PAPERS) as f:
        for line in f:
            p = json.loads(line)
            papers.append(p)

    # document frequencies over projects + papers (title+abstract)
    df = Counter()
    n_docs = len(projects) + len(papers)
    paper_toks = {}
    for pr in projects.values():
        df.update(set(pr["text"]))
    for p in papers:
        t = toks((p["title"] or "") + " " + (p["abstract"] or ""))
        paper_toks[p["id"]] = t
        df.update(set(t))

    proj_vecs = {pid: tfidf(pr["text"], df, n_docs) for pid, pr in projects.items()}

    def pair(p, pid, tier):
        pr = projects[pid]
        dt = (p["year"] - pr["year"]) if (p["year"] and pr["year"]) else None
        if tier != "award" and dt is not None and not (-1 <= dt <= 8):
            return None
        c = cos(tfidf(paper_toks[p["id"]], df, n_docs), proj_vecs[pid])
        if tier == "award":
            score = 1.0
        else:
            timing = 1.0 if (dt is not None and 0 <= dt <= 5) else (0.5 if dt is not None else 0.6)
            score = 0.65 * c + 0.15 * timing + 0.20 * (1.0 if p["euroqol_funded"] else 0.0)
        return {"paper_id": p["id"], "project_id": pid, "tier": tier,
                "cos": round(c, 4), "dt": dt, "eq_funded": p["euroqol_funded"],
                "score": round(score, 4)}

    n_award = n_pi = n_funder = 0
    with open(OUT, "w") as out:
        for p in papers:
            seen = set()
            # tier: award id match
            for a in p["awards"]:
                for tok in PID_PAT.findall((a["award_id"] or "").upper()):
                    if tok in projects and tok not in seen:
                        m = pair(p, tok, "award")
                        if m:
                            out.write(json.dumps(m) + "\n")
                            seen.add(tok)
                            n_award += 1
            # tier: PI-authored
            for name in p["pi_authors"]:
                for pid in pi_projects.get(name, []):
                    if pid in seen or pid not in projects:
                        continue
                    m = pair(p, pid, "pi")
                    if m:
                        out.write(json.dumps(m) + "\n")
                        seen.add(pid)
                        n_pi += 1
            # tier: euroqol-funded without any PI-author link
            if p["euroqol_funded"] and not p["pi_authors"] and not seen:
                for pid in projects:
                    m = pair(p, pid, "funder")
                    if m and m["cos"] >= 0.15:  # keep only lexically plausible
                        out.write(json.dumps(m) + "\n")
                        n_funder += 1

    print(f"pairs written: award={n_award} pi={n_pi} funder={n_funder} -> {OUT}")


if __name__ == "__main__":
    main()
