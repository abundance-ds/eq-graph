"""Full-text acquisition, restricted to openly licensed copies.

Policy, in order of preference:

1. **Europe PMC full-text XML** for anything with a PMCID. Europe PMC only serves
   `fullTextXML` for its open-access subset, so a 200 here *is* the licence check,
   and the result is structured text rather than a PDF to re-parse later.
2. **Repository-hosted PDFs** (green OA: PMC mirrors, institutional repositories)
   as recorded by Unpaywall.
3. **Publisher PDFs only under an explicit Creative Commons licence.**

Anything else is skipped with a reason and its landing page, for separate retrieval
through institutional access. Publisher sites are not scraped speculatively: an
Elsevier "TDM user licence" is not a redistribution licence, and a paywalled PDF
endpoint typically answers with an HTML interstitial anyway.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from . import sources
from .db import is_settled, set_task, task_row
from .http import FetchError, Fetcher
from .match import ACCEPT_THRESHOLD

REPO = Path(__file__).resolve().parents[2]
PROJECTS_DIR = REPO / "input" / "projects"

EPMC_FULLTEXT = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"

CC_LICENCE_RE = re.compile(r"\bcc[-\s]?(by|0|zero)", re.IGNORECASE)
OPEN_HOST_TYPES = {"repository"}

# Signatures used to reject an HTML interstitial saved under a .pdf name.
PDF_MAGIC = b"%PDF"
MAX_BYTES = 80 * 1024 * 1024


def safe_name(work_id: str) -> str:
    """Filesystem-safe stem derived from the work id (DOIs contain slashes)."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", work_id)


def unpaywall_from_cache(fetcher: Fetcher, doi: str) -> list[dict]:
    """Every free location Unpaywall knows for a DOI, not just the best one.

    `best_oa_location` is Unpaywall's single pick and is frequently the publisher's
    own copy -- exactly the one that answers 403. The `oa_locations` array usually
    also lists a repository deposit of the same article, which is both openly
    licensed and happy to be fetched.
    """
    try:
        payload = fetcher.get(
            f"{sources.UNPAYWALL}{doi}", {"email": sources.CONTACT_EMAIL}
        ).json()
    except FetchError:
        return []
    locations = list(payload.get("oa_locations") or [])
    best = payload.get("best_oa_location")
    if best and best not in locations:
        locations.insert(0, best)
    return [loc for loc in locations if loc]


def candidate_sources(work, locations: list[dict]) -> list[tuple[str, str, str]]:
    """Ordered (method, url, reason) candidates to try for one work.

    Repositories come before publishers: a green-OA deposit is redistributable and
    rarely blocks automated fetching, whereas the publisher copy often does both the
    opposite. Within each tier, order is stable so the ledger key is deterministic.
    """
    out: list[tuple[str, str, str]] = []
    if work["pmcid"]:
        out.append(("epmc_xml", EPMC_FULLTEXT.format(pmcid=work["pmcid"]), "PMCID present"))

    tiers: dict[str, list[tuple[str, str, str]]] = {"repo": [], "cc": []}
    for loc in locations:
        url = loc.get("url_for_pdf")
        if not url:
            continue
        licence = loc.get("license") or ""
        host = loc.get("host_type")
        if host in OPEN_HOST_TYPES:
            tiers["repo"].append(
                ("repository_pdf", url, f"repository copy, licence {licence or 'unstated'}")
            )
        elif CC_LICENCE_RE.search(licence):
            tiers["cc"].append(("publisher_pdf", url, f"explicit {licence}"))

    seen: set[str] = set()
    for tier in ("repo", "cc"):
        for method, url, reason in tiers[tier]:
            if url not in seen:
                seen.add(url)
                out.append((method, url, reason))

    # Last resort: a pointer recorded on the work itself, from OpenAlex or Europe PMC.
    # These mostly duplicate Unpaywall, but a handful of locations are known only to
    # those sources. Same licence bar as above -- an unstated licence does not qualify.
    own = work["pdf_url"]
    if own and own not in seen and work["is_oa"] and CC_LICENCE_RE.search(work["licence"] or ""):
        out.append(("indexed_pdf", own, f"location from work metadata, {work['licence']}"))
    return out


def skip_reason(work, locations: list[dict]) -> str:
    if any(loc.get("url_for_pdf") for loc in locations):
        return "open access, but no location with a clearly redistributable licence"
    if work["is_oa"]:
        return "flagged OA but no usable free location recorded"
    return "no open-access copy; use the landing page"


def verify(method: str, data: bytes) -> str | None:
    """Reject responses that are not actually the document we asked for."""
    if not data:
        return "empty response"
    head = data.lstrip()[:512].lower()
    if method.endswith("pdf"):
        if not data.lstrip().startswith(PDF_MAGIC):
            return "response is not a PDF (likely an HTML interstitial)"
    elif b"<html" in head and b"<article" not in head:
        return "response is HTML, not full-text XML"
    return None


def run(conn, fetcher: Fetcher, retry_failed: bool = False,
        min_score: float = ACCEPT_THRESHOLD, log=print) -> dict:
    offline = Fetcher(conn, offline=True)
    rows = conn.execute(
        """SELECT DISTINCT c.project_id, w.work_id, w.doi, w.pmcid, w.title,
                  w.is_oa, w.licence, w.pdf_url, w.oa_url, c.score
           FROM candidate c JOIN work w USING (work_id)
           LEFT JOIN decision d
                  ON d.project_id = c.project_id AND d.work_id = c.work_id
           WHERE (c.score >= ? OR d.verdict = 'accept')
             AND COALESCE(d.verdict, '') != 'reject'
           ORDER BY c.project_id, c.score DESC""",
        (min_score,),
    ).fetchall()

    stats = {"downloaded": 0, "reused": 0, "skipped": 0, "failed": 0, "settled": 0}
    manifests: dict[str, list[dict]] = {}
    # A work linked to several projects is fetched once and copied.
    blobs: dict[str, Path] = {}

    for row in rows:
        project_id, work_id = row["project_id"], row["work_id"]
        locations = unpaywall_from_cache(offline, row["doi"]) if row["doi"] else []
        candidates = candidate_sources(row, locations)
        entry = {
            "work_id": work_id,
            "doi": row["doi"],
            "title": row["title"],
            "licence": next((loc.get("license") for loc in locations if loc.get("license")),
                            row["licence"]),
            "landing_page": f"https://doi.org/{row['doi']}" if row["doi"] else row["oa_url"],
        }

        if not candidates:
            entry.update(method="skip", source_url=None, status="skipped",
                         reason=skip_reason(row, locations))
            manifests.setdefault(project_id, []).append(entry)
            stats["skipped"] += 1
            continue

        method, url, reason = candidates[0]
        entry.update(method=method, source_url=url,
                     alternates=max(0, len(candidates) - 1))

        papers_dir = PROJECTS_DIR / project_id / "papers"
        suffix = ".xml" if method == "epmc_xml" else ".pdf"
        dest = papers_dir / f"{safe_name(work_id)}{suffix}"

        ledger_key = f"{project_id}|{work_id}"
        # Key the ledger on the whole candidate list: if a new alternate location
        # appears, the task un-settles and the extra copy gets tried.
        url = "|".join(c[1] for c in candidates)
        prior = task_row(conn, ledger_key, "fulltext", "download")
        # An already-downloaded file stays put even when the candidate list grows:
        # discovering more mirrors is no reason to re-fetch something we hold. The
        # query comparison therefore only un-settles tasks that did NOT succeed.
        if prior is not None and prior["status"] == "ok" and dest.exists():
            stats["settled"] += 1
            entry.update(status="ok", file=str(dest.relative_to(REPO)),
                         bytes=dest.stat().st_size,
                         sha256=hashlib.sha256(dest.read_bytes()).hexdigest())
            manifests.setdefault(project_id, []).append(entry)
            continue

        # A settled *failure* leaves no file behind, so the ledger alone decides;
        # requiring dest.exists() here would silently re-attempt it on every run.
        if is_settled(prior, retry_failed, url) and (
            prior["status"] != "ok" or dest.exists()
        ):
            stats["settled"] += 1
            if prior["status"] == "ok":
                entry.update(status="ok", file=str(dest.relative_to(REPO)),
                             bytes=dest.stat().st_size,
                             sha256=hashlib.sha256(dest.read_bytes()).hexdigest())
            else:
                entry.update(status="unavailable", reason=prior["last_error"])
            manifests.setdefault(project_id, []).append(entry)
            continue

        papers_dir.mkdir(parents=True, exist_ok=True)
        data = None
        attempts: list[str] = []

        if work_id in blobs:
            data = blobs[work_id].read_bytes()
            stats["reused"] += 1
        else:
            # Walk the candidates: a publisher 403 is terminal for *that URL*, not for
            # the article, so fall through to the repository deposit behind it.
            for cand_method, cand_url, _reason in candidates:
                try:
                    payload = fetcher.get_bytes(cand_url, max_bytes=MAX_BYTES)
                    problem = verify(cand_method, payload)
                    if problem:
                        raise FetchError(problem)
                except FetchError as exc:
                    code = getattr(exc, "status", None)
                    attempts.append(f"{cand_url} -> {code or str(exc)[:60]}")
                    continue
                data = payload
                method, dest = cand_method, papers_dir / (
                    safe_name(work_id) + (".xml" if cand_method == "epmc_xml" else ".pdf")
                )
                entry["method"] = cand_method
                entry["source_url"] = cand_url
                stats["downloaded"] += 1
                break

        if data is None:
            blocked = any("403" in a or "401" in a for a in attempts)
            reason = (
                f"no candidate location yielded the document ({len(candidates)} tried); "
                + ("publisher refuses automated download" if blocked else "see attempts")
            )
            set_task(conn, ledger_key, "fulltext", "download",
                     "skipped" if blocked else "failed",
                     query=url, error=reason + " :: " + "; ".join(attempts)[:300])
            entry.update(status="unavailable", reason=reason, attempts=attempts)
            manifests.setdefault(project_id, []).append(entry)
            stats["skipped" if blocked else "failed"] += 1
            continue

        if entry.get("attempts_failed") is None and attempts:
            entry["attempts_failed"] = attempts

        dest.write_bytes(data)
        blobs.setdefault(work_id, dest)
        digest = hashlib.sha256(data).hexdigest()
        set_task(conn, ledger_key, "fulltext", "download", "ok",
                 query=url, result_count=len(data))
        entry.update(status="ok", file=str(dest.relative_to(REPO)),
                     bytes=len(data), sha256=digest)
        manifests.setdefault(project_id, []).append(entry)

        if (stats["downloaded"] + stats["reused"]) % 25 == 0:
            conn.commit()
            log(f"  {stats}")

    conn.commit()
    for project_id, entries in manifests.items():
        path = PROJECTS_DIR / project_id / "papers" / "manifest.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "project_id": project_id,
            "policy": "open-access only; see scripts/scrape/fulltext.py",
            "entries": sorted(entries, key=lambda e: e["work_id"]),
        }
        # No timestamp in the payload: it would churn every run for no information
        # the ledger does not already hold.
        content = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
    log(f"full text: {stats} across {len(manifests)} projects")
    return stats
