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


def no_publication_report(conn, log=print) -> int:
    """List every project no source could link to any publication at all.

    Kept separate from the coverage summary because this is a worklist: these are the
    projects to chase with the funder, not a statistic to read once.
    """
    linked = {row[0] for row in conn.execute("SELECT DISTINCT project_id FROM candidate")}
    missing = [p for p in load_projects() if p.project_id not in linked]

    def tally(attr) -> list[tuple[str, int]]:
        counts: dict[str, int] = {}
        for project in missing:
            for key in attr(project):
                counts[key] = counts.get(key, 0) + 1
        return sorted(counts.items(), key=lambda kv: -kv[1])

    raw = {
        p.project_id: json.loads(
            (PROJECTS_DIR / p.project_id / "project.json").read_text(encoding="utf-8")
        )
        for p in missing
    }
    total_budget = sum(raw[p.project_id]["approved_budget_eur"] or 0 for p in missing)

    bands = dict(
        conn.execute(
            f"""SELECT CASE WHEN best >= {ACCEPT_THRESHOLD} THEN 'accepted'
                            WHEN best >= {REVIEW_THRESHOLD} THEN 'review'
                            ELSE 'weak' END, COUNT(*)
                FROM (SELECT project_id, MAX(score) AS best FROM candidate
                      GROUP BY project_id) GROUP BY 1"""
        ).fetchall()
    )

    lines = [
        "# Projects with no publication found",
        "",
        f"{len(missing)} of 1024 funded projects could not be linked to a single "
        "publication by any source (Europe PMC, CORE, Crossref, OpenAlex, Unpaywall, "
        "and full-text grant-id mining). Regenerated by "
        "`python3 scripts/scrape.py report`.",
        "",
        "> **Absence from this list does not mean a project is resolved.** A project "
        f"drops off it as soon as *any* rule fires, including the weakest one. "
        f"{bands.get('weak', 0)} projects are absent from this list while having only "
        "name-only evidence, which is a review pool rather than an attribution. Only "
        f"**{bands.get('accepted', 0)}** projects have a publication established at "
        "accepted confidence. Read this file as the subset where even the weak rule "
        "found nothing, not as the complement of what has been solved.",
        "",
        "A blank here means *no evidence was found*, not that no paper exists. Read "
        "the status table first: a large share of these are **Ongoing** projects that "
        "simply have not published yet, which is an expected absence rather than a "
        "gap in the search. For the completed ones the likely causes are: the grant "
        "funded something other than a paper (travel, translation, outreach, tooling); "
        "the paper exists but names no grant id and shares no PI surname we could "
        "match; or it sits outside the indexes these free sources cover.",
        "",
        f"Combined approved budget of the projects below: **{total_budget:,} EUR**.",
        "",
        "## By grant type",
        "",
        "| Grant type | Projects |",
        "| --- | ---: |",
    ]
    for code, count in tally(lambda p: [raw[p.project_id]["grant_type"] or "unknown (older id scheme)"]):
        lines.append(f"| {code} | {count} |")

    lines += ["", "## By status", "", "| Status | Projects |", "| --- | ---: |"]
    for status, count in tally(lambda p: [raw[p.project_id]["status"]]):
        lines.append(f"| {status} | {count} |")

    lines += ["", "## By working group", "", "| Working group | Projects |", "| --- | ---: |"]
    for group, count in tally(lambda p: raw[p.project_id]["working_groups"]):
        lines.append(f"| {group} | {count} |")

    lines += [
        "",
        "## The projects",
        "",
        "| Project | Title | PI | Type | Status | Years | Budget (EUR) |",
        "| --- | --- | --- | --- | --- | --- | ---: |",
    ]
    for project in sorted(missing, key=lambda p: p.project_id):
        r = raw[project.project_id]
        title = r["title"].replace("|", "\\|")
        years = "–".join(str(y) for y in (r["start_year"], r["end_year"]) if y) or "—"
        lines.append(
            f"| `{r['project_id']}` | {title} | {r['pi_name_raw'].replace('|', '')} "
            f"| {r['grant_type_code'] or '—'} | {r['status']} | {years} "
            f"| {r['approved_budget_eur']:,} |"
        )
    lines.append("")

    REPORTS_DIR.mkdir(exist_ok=True)
    (REPORTS_DIR / "no-publications.md").write_text("\n".join(lines), encoding="utf-8")
    log(f"{len(missing)} projects with no publication -> reports/no-publications.md")
    return len(missing)


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
