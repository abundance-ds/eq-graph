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


def unpaywall_from_cache(fetcher: Fetcher, doi: str) -> dict | None:
    """Re-read the cached Unpaywall record for licence and host type."""
    try:
        payload = fetcher.get(f"{sources.UNPAYWALL}{doi}", {"email": sources.CONTACT_EMAIL})
    except FetchError:
        return None
    best = (payload.json().get("best_oa_location") or {})
    return {
        "host_type": best.get("host_type"),
        "licence": best.get("license"),
        "pdf_url": best.get("url_for_pdf"),
        "landing": best.get("url_for_landing_page"),
    }


def choose_source(work, oa: dict | None) -> tuple[str, str | None, str]:
    """Return (method, url, reason)."""
    if work["pmcid"]:
        return "epmc_xml", EPMC_FULLTEXT.format(pmcid=work["pmcid"]), "PMCID present"
    if oa:
        licence = oa.get("licence") or ""
        if oa.get("pdf_url") and oa.get("host_type") in OPEN_HOST_TYPES:
            return "repository_pdf", oa["pdf_url"], f"repository copy, licence {licence or 'unstated'}"
        if oa.get("pdf_url") and CC_LICENCE_RE.search(licence):
            return "publisher_pdf", oa["pdf_url"], f"explicit {licence}"
        if oa.get("pdf_url"):
            return "skip", None, f"OA but licence '{licence or 'unstated'}' is not clearly redistributable"
    if work["is_oa"]:
        return "skip", None, "flagged OA but no usable free location recorded"
    return "skip", None, "no open-access copy; use the landing page"


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
        oa = unpaywall_from_cache(offline, row["doi"]) if row["doi"] else None
        method, url, reason = choose_source(row, oa)
        entry = {
            "work_id": work_id,
            "doi": row["doi"],
            "title": row["title"],
            "method": method,
            "source_url": url,
            "licence": (oa or {}).get("licence") or row["licence"],
            "landing_page": f"https://doi.org/{row['doi']}" if row["doi"] else row["oa_url"],
        }

        if method == "skip":
            entry.update(status="skipped", reason=reason)
            manifests.setdefault(project_id, []).append(entry)
            stats["skipped"] += 1
            continue

        papers_dir = PROJECTS_DIR / project_id / "papers"
        suffix = ".xml" if method == "epmc_xml" else ".pdf"
        dest = papers_dir / f"{safe_name(work_id)}{suffix}"

        ledger_key = f"{project_id}|{work_id}"
        prior = task_row(conn, ledger_key, "fulltext", "download")
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
        try:
            if work_id in blobs:
                data = blobs[work_id].read_bytes()
                stats["reused"] += 1
            else:
                data = fetcher.get_bytes(url, max_bytes=MAX_BYTES)
                problem = verify(method, data)
                if problem:
                    raise FetchError(problem)
                stats["downloaded"] += 1
        except FetchError as exc:
            status_code = getattr(exc, "status", None)
            # 401/403 is a publisher deliberately refusing automated download. That is
            # a terminal answer, not a transient fault: retrying cannot succeed and
            # re-hammering the endpoint would be rude. 404 means simply not there.
            if status_code in (401, 403):
                ledger_status = "skipped"
                reason = (f"publisher refuses automated download (HTTP {status_code}); "
                          "use the landing page")
            elif status_code == 404:
                ledger_status, reason = "empty", "no copy at the recorded location"
            else:
                ledger_status, reason = "failed", str(exc)[:200]
            set_task(conn, ledger_key, "fulltext", "download", ledger_status,
                     query=url, http_status=status_code, error=reason)
            entry.update(status="unavailable", reason=reason)
            manifests.setdefault(project_id, []).append(entry)
            stats["failed" if ledger_status == "failed" else "skipped"] += 1
            continue

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
