"""Export stage: per-project publication files plus the coverage gap report."""

from __future__ import annotations

import json
from pathlib import Path

from .match import ACCEPT_THRESHOLD, REVIEW_THRESHOLD, load_projects

REPO = Path(__file__).resolve().parents[2]
PROJECTS_DIR = REPO / "input" / "projects"
REPORTS_DIR = REPO / "reports"

# Weak-band entries kept per project in the export; the rest stay queryable in the
# ledger. Ordered by score then recency, so the cap keeps the most plausible ones.
WEAK_EXPORT_LIMIT = 15


def _work_row(row) -> dict:
    """Shape one candidate for the on-disk export."""
    is_oa = bool(row["is_oa"])
    return {
        "work_id": row["work_id"],
        "doi": row["doi"],
        "pmid": row["pmid"],
        "pmcid": row["pmcid"],
        "title": row["title"],
        "journal": row["journal"],
        "year": row["year"],
        "authors": json.loads(row["authors"] or "[]"),
        "score": round(row["score"], 3),
        "confidence": (
            "accepted" if row["score"] >= ACCEPT_THRESHOLD
            else "review" if row["score"] >= REVIEW_THRESHOLD
            else "weak"
        ),
        "curated": row["verdict"],
        "evidence": json.loads(row["evidence"] or "[]"),
        "sources": json.loads(row["sources"] or "[]"),
        "access": {
            "is_oa": is_oa,
            "licence": row["licence"],
            "oa_url": row["oa_url"],
            "pdf_url": row["pdf_url"],
            # For closed works we record where the text lives so it can be
            # retrieved separately through institutional access.
            "landing_page": f"https://doi.org/{row['doi']}" if row["doi"] else None,
            "retrieval": "open" if is_oa else "requires_subscription",
        },
    }


def export(conn, log=print) -> dict:
    rows = conn.execute(
        """SELECT c.project_id, c.work_id, c.score, c.evidence,
                  w.doi, w.pmid, w.pmcid, w.title, w.journal, w.year, w.authors,
                  w.is_oa, w.oa_url, w.licence, w.pdf_url, w.sources,
                  d.verdict
           FROM candidate c
           JOIN work w USING (work_id)
           LEFT JOIN decision d
                  ON d.project_id = c.project_id AND d.work_id = c.work_id
           ORDER BY c.project_id, c.score DESC, c.work_id"""
    ).fetchall()

    by_project: dict[str, list[dict]] = {}
    for row in rows:
        if row["verdict"] == "reject":
            continue  # curation wins over the matcher
        by_project.setdefault(row["project_id"], []).append(_work_row(row))

    written = 0
    for project in load_projects():
        path = PROJECTS_DIR / project.project_id / "publications.json"
        entries = by_project.get(project.project_id, [])
        if not entries:
            path.unlink(missing_ok=True)
            continue
        weak = [e for e in entries if e["confidence"] == "weak" and e["curated"] != "accept"]
        payload = {
            "project_id": project.project_id,
            "accepted": [e for e in entries if e["confidence"] == "accepted"
                         or e["curated"] == "accept"],
            "review": [e for e in entries if e["confidence"] == "review"
                       and e["curated"] != "accept"],
            # Name-only evidence cannot say *which* of a PI's grants a paper belongs
            # to, so this band is a review pool, not an attribution. Capped, with the
            # dropped count kept so the truncation is never silent.
            "weak": weak[:WEAK_EXPORT_LIMIT],
            "weak_omitted": max(0, len(weak) - WEAK_EXPORT_LIMIT),
        }
        content = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
            written += 1

    log(f"exported publications for {len(by_project)} projects ({written} files changed)")
    return {"projects_with_candidates": len(by_project), "files_written": written}


def gap_report(conn, log=print) -> dict:
    projects = load_projects()
    total = len(projects)

    # Bucket each project by its BEST candidate, so the outcomes are mutually
    # exclusive and actually sum to the portfolio size.
    counts = dict(
        conn.execute(
            f"""SELECT CASE WHEN best >= {ACCEPT_THRESHOLD} THEN 'accepted'
                            WHEN best >= {REVIEW_THRESHOLD} THEN 'review'
                            ELSE 'weak' END AS band,
                       COUNT(*)
                FROM (SELECT project_id, MAX(score) AS best FROM candidate
                      GROUP BY project_id)
                GROUP BY band"""
        ).fetchall()
    )
    resolved = counts.get("accepted", 0)
    any_candidate = conn.execute("SELECT COUNT(DISTINCT project_id) FROM candidate").fetchone()[0]

    works = conn.execute("SELECT COUNT(*) FROM work").fetchone()[0]
    linked_works = conn.execute(
        f"""SELECT COUNT(DISTINCT work_id) FROM candidate WHERE score >= {ACCEPT_THRESHOLD}"""
    ).fetchone()[0]
    oa = conn.execute(
        f"""SELECT COUNT(DISTINCT w.work_id) FROM work w JOIN candidate c USING (work_id)
            WHERE c.score >= {ACCEPT_THRESHOLD} AND w.is_oa = 1"""
    ).fetchone()[0]

    task_rows = conn.execute(
        "SELECT source, op, status, COUNT(*) n FROM task GROUP BY source, op, status"
    ).fetchall()

    unresolved = [
        p.project_id
        for p in projects
        if not conn.execute(
            f"SELECT 1 FROM candidate WHERE project_id=? AND score >= {ACCEPT_THRESHOLD}",
            (p.project_id,),
        ).fetchone()
    ]

    lines = [
        "# Coverage gap report",
        "",
        "Generated by `python3 scripts/scrape.py report`. Free sources only "
        "(Europe PMC, Crossref, Unpaywall) — OpenAlex is metered and was not used.",
        "",
        "## Projects",
        "",
        "| Outcome | Projects | Share |",
        "| --- | ---: | ---: |",
        f"| Resolved (>= {ACCEPT_THRESHOLD} confidence) | {resolved} | {resolved/total:.1%} |",
        f"| Best candidate is review-band | {counts.get('review', 0)} | "
        f"{counts.get('review', 0)/total:.1%} |",
        f"| Only weak (name-only) candidates | {counts.get('weak', 0)} | "
        f"{counts.get('weak', 0)/total:.1%} |",
        f"| No candidate at all | {total - any_candidate} | {(total-any_candidate)/total:.1%} |",
        f"| **Total** | **{total}** | |",
        "",
        "## Works",
        "",
        f"- {works} distinct works in the pool",
        f"- {linked_works} linked to a project at accepted confidence",
        f"- {oa} of those are open access with a retrievable free copy "
        f"({oa/linked_works:.1%} of linked works)" if linked_works else "- no linked works",
        "",
        "## Full text",
        "",
    ]

    # Counted from the manifests, not the task ledger: items skipped by licence
    # policy are never requested, so they have no ledger row at all.
    methods: dict[str, int] = {}
    ft = {"ok": 0, "unavailable": 0, "skipped": 0}
    ft_bytes = 0
    for path in PROJECTS_DIR.glob("*/papers/manifest.json"):
        for entry in json.loads(path.read_text(encoding="utf-8"))["entries"]:
            ft[entry["status"]] = ft.get(entry["status"], 0) + 1
            methods[entry["method"]] = methods.get(entry["method"], 0) + 1
            ft_bytes += entry.get("bytes") or 0

    if any(ft.values()):
        total_ft = sum(ft.values())
        lines += [
            f"- **{ft['ok']} of {total_ft}** accepted-confidence links have a full "
            f"text on disk ({ft_bytes/1e6:.0f} MB)",
            "- by method: "
            + ", ".join(f"{k} {v}" for k, v in sorted(methods.items(), key=lambda kv: -kv[1])),
            f"- {ft['skipped']} skipped before any request: no open copy, or a licence "
            "that is not clearly redistributable",
            f"- {ft['unavailable']} requested but not obtained, nearly all publishers "
            "refusing automated download (HTTP 403)",
            "",
            "Nothing is lost silently: every non-`ok` entry keeps its reason and DOI "
            "landing page in the project's `papers/manifest.json`, ready for retrieval "
            "through institutional access.",
            "",
        ]
    else:
        lines += ["- not run yet (`python3 scripts/scrape.py fulltext`)", ""]

    lines += [
        "## Task ledger",
        "",
        "| Source | Operation | Status | Count |",
        "| --- | --- | --- | ---: |",
    ]
    for row in task_rows:
        lines.append(f"| {row['source']} | {row['op']} | {row['status']} | {row['n']} |")

    lines += [
        "",
        "## What OpenAlex would add",
        "",
        f"{len(unresolved)} projects have no accepted-confidence publication from free "
        "sources. OpenAlex indexes 757 works for funder `F4320323856` and additionally "
        "carries author ORCIDs, institutional affiliations and citation edges that "
        "Europe PMC and Crossref do not expose together. Deciding whether to buy credits "
        "is a question of whether those unresolved projects and the citation graph matter "
        "more than the cost.",
        "",
        "Unresolved project ids are listed in `reports/unresolved.txt`.",
        "",
    ]

    REPORTS_DIR.mkdir(exist_ok=True)
    (REPORTS_DIR / "coverage.md").write_text("\n".join(lines), encoding="utf-8")
    (REPORTS_DIR / "unresolved.txt").write_text(
        "\n".join(unresolved) + ("\n" if unresolved else ""), encoding="utf-8"
    )
    log(f"resolved {resolved}/{total} projects; report in reports/coverage.md")
    return {"total": total, "resolved": resolved, "unresolved": len(unresolved),
            "works": works, "oa": oa}
