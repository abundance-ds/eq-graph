"""Source adapters: query construction and normalization into `work` records.

Each adapter turns a source-specific payload into the same dict shape so the match
stage never needs to know where a work came from.
"""

from __future__ import annotations

import json
import os
import re
from typing import Iterator

from .http import CONTACT_EMAIL, Fetcher

EPMC_SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
CROSSREF_WORKS = "https://api.crossref.org/works"
UNPAYWALL = "https://api.unpaywall.org/v2/"

# Registered identifiers for the funder, confirmed against both registries.
CROSSREF_FUNDER_ID = "501100006419"
OPENALEX_FUNDER_ID = "F4320323856"

PAGE_SIZE = 100
MAX_PAGES = 40  # hard stop so a runaway query cannot page forever


def normalize_doi(doi: str | None) -> str | None:
    if not doi:
        return None
    doi = doi.strip().lower()
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", doi)
    return doi or None


def make_work_id(doi: str | None, pmid: str | None, pmcid: str | None) -> str | None:
    if doi:
        return f"doi:{doi}"
    if pmid:
        return f"pmid:{pmid}"
    if pmcid:
        return f"pmcid:{pmcid}"
    return None


# --------------------------------------------------------------------------- EPMC


def epmc_search(fetcher: Fetcher, query: str, max_pages: int = MAX_PAGES,
                strict: bool = False) -> Iterator[dict]:
    """Yield core-format results, following cursorMark pagination.

    `strict` turns silent truncation at the page cap into an error; use it for sweeps
    meant to be exhaustive, and leave it off for per-project probes that are
    deliberately capped.
    """
    cursor = "*"
    for _ in range(max_pages):
        resp = fetcher.get(
            EPMC_SEARCH,
            {
                "query": query,
                "format": "json",
                "pageSize": PAGE_SIZE,
                "resultType": "core",
                "cursorMark": cursor,
            },
        )
        payload = resp.json()
        results = payload.get("resultList", {}).get("result", [])
        yield from results
        next_cursor = payload.get("nextCursorMark")
        if not next_cursor or next_cursor == cursor or len(results) < PAGE_SIZE:
            return
        cursor = next_cursor
    if strict:
        raise RuntimeError(f"europepmc sweep hit the {max_pages}-page cap: {query}")


def epmc_to_work(item: dict) -> dict | None:
    doi = normalize_doi(item.get("doi"))
    pmid = (item.get("pmid") or "").strip() or None
    pmcid = (item.get("pmcid") or "").strip() or None
    work_id = make_work_id(doi, pmid, pmcid)
    if not work_id:
        return None

    authors = [
        {
            "full_name": a.get("fullName"),
            "last_name": a.get("lastName"),
            "orcid": (a.get("authorId") or {}).get("value")
            if (a.get("authorId") or {}).get("type") == "ORCID"
            else None,
        }
        for a in (item.get("authorList") or {}).get("author", [])
    ]

    pdf_url = oa_url = None
    for entry in (item.get("fullTextUrlList") or {}).get("fullTextUrl", []):
        if entry.get("availability") in ("Open access", "Free"):
            if entry.get("documentStyle") == "pdf" and not pdf_url:
                pdf_url = entry.get("url")
            elif not oa_url:
                oa_url = entry.get("url")

    grants = [
        {"grant_id": g.get("grantId"), "agency": g.get("agency")}
        for g in (item.get("grantsList") or {}).get("grant", [])
    ]

    year = item.get("pubYear") or (item.get("journalInfo") or {}).get("yearOfPublication")
    return {
        "work_id": work_id,
        "doi": doi,
        "pmid": pmid,
        "pmcid": pmcid,
        "title": (item.get("title") or "").strip().rstrip("."),
        "journal": ((item.get("journalInfo") or {}).get("journal") or {}).get("title"),
        "year": int(year) if str(year).isdigit() else None,
        "authors": authors,
        "is_oa": 1 if item.get("isOpenAccess") == "Y" else 0,
        "oa_url": oa_url,
        "licence": item.get("license"),
        "pdf_url": pdf_url,
        "source": "europepmc",
        "grants": grants,
        "abstract": item.get("abstractText"),
    }


def epmc_ack_query() -> str:
    return 'ACK_FUND:"EuroQol" OR ACK_FUND:"EuroQol Research Foundation"'


def epmc_phrase_query() -> str:
    """Free-text phrase sweep.

    The ACK_FUND index only holds what Europe PMC managed to parse out of the funding
    statement; searching the phrase across the whole text finds ~1147 works against
    626 for the index. The extra hits are exactly the ones whose funding statement was
    never structured -- which is where full-text grant-id mining pays off.
    """
    return '"EuroQol Research Foundation"'


# Only the 8-digit scheme is distinctive enough for free-text search. Suffix ids like
# "100-RA" tokenize apart and collide with prose ("100 RA patients" - RA is also
# rheumatoid arthritis), which returned materials-chemistry papers in testing.
UNAMBIGUOUS_ID_RE = re.compile(r"^\d{7,}(R\d+)?$")

# Grant numbers are reused across funders: GRANT_ID:"2013010" matches awards from the
# Norwegian South East Health Authority and a Chinese biofuel lab. Any grant-id hit
# must therefore be confirmed against the agency name before it counts as evidence.
EUROQOL_AGENCY_RE = re.compile(r"euroqol", re.IGNORECASE)


def epmc_grant_queries(project_id: str) -> list[tuple[str, str]]:
    """(evidence_kind, query) pairs targeting one project's grant id."""
    queries = [("grant_id_structured", f'GRANT_ID:"{project_id}"')]
    if UNAMBIGUOUS_ID_RE.match(project_id):
        # Anchored to the acknowledgement index; the bare phrase is far too loose.
        queries.append(("grant_id_fulltext", f'ACK_FUND:"EuroQol" AND "{project_id}"'))
    return queries


def is_euroqol_grant(work: dict, project_id: str) -> bool:
    """True when the work credits *this* project id to EuroQol specifically."""
    target = project_id.strip().lower()
    for grant in work.get("grants") or []:
        grant_id = str(grant.get("grant_id") or "").strip().lower()
        if grant_id == target and EUROQOL_AGENCY_RE.search(grant.get("agency") or ""):
            return True
    return False


def epmc_title_query(title: str, pi_names: list[tuple[str, str]]) -> str | None:
    """Title-led lookup, widened by a PI surname when we have one."""
    cleaned = re.sub(r'["\\]', " ", title).strip()
    if len(cleaned) < 15:
        return None
    query = f'TITLE:"{cleaned}"'
    if pi_names:
        query += f' OR (TITLE:"{cleaned}" AND AUTH:"{pi_names[0][0]}")'
    return query


# ----------------------------------------------------------------------- Crossref


def crossref_funder_works(fetcher: Fetcher, max_pages: int = MAX_PAGES) -> Iterator[dict]:
    """Page the funder's works by offset.

    Crossref's cursor paging is unusable behind a URL-keyed cache: it returns the
    *same* `next-cursor` token on every page, so consecutive requests are byte
    identical and the cache replays page 2 forever. Offset paging gives each page a
    distinct URL. The result set (~513) is far below Crossref's deep-paging limit.
    """
    for page in range(max_pages):
        resp = fetcher.get(
            CROSSREF_WORKS,
            {
                "filter": f"funder:{CROSSREF_FUNDER_ID}",
                "rows": PAGE_SIZE,
                "offset": page * PAGE_SIZE,
                "mailto": CONTACT_EMAIL,
            },
        )
        message = resp.json().get("message", {})
        items = message.get("items", [])
        yield from items
        if len(items) < PAGE_SIZE:
            return
    raise RuntimeError(
        f"crossref funder sweep hit the {max_pages}-page cap; results were truncated"
    )


def crossref_to_work(item: dict) -> dict | None:
    doi = normalize_doi(item.get("DOI"))
    if not doi:
        return None
    titles = item.get("title") or []
    containers = item.get("container-title") or []
    year = None
    for field in ("issued", "published-print", "published-online"):
        parts = (item.get(field) or {}).get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            year = parts[0][0]
            break

    authors = [
        {
            "full_name": " ".join(filter(None, [a.get("given"), a.get("family")])),
            "last_name": a.get("family"),
            "orcid": normalize_doi(a.get("ORCID")) if a.get("ORCID") else None,
        }
        for a in item.get("author", [])
    ]

    grants = []
    for funder in item.get("funder", []):
        for award in funder.get("award", []) or []:
            grants.append({"grant_id": award, "agency": funder.get("name")})

    licences = [lic.get("URL") for lic in item.get("license", []) if lic.get("URL")]
    return {
        "work_id": f"doi:{doi}",
        "doi": doi,
        "pmid": None,
        "pmcid": None,
        "title": (titles[0].strip().rstrip(".") if titles else ""),
        "journal": containers[0] if containers else None,
        "year": year,
        "authors": authors,
        "is_oa": 0,
        "oa_url": None,
        "licence": licences[0] if licences else None,
        "pdf_url": None,
        "source": "crossref",
        "grants": grants,
        "abstract": item.get("abstract"),
    }


# ---------------------------------------------------------------------- Unpaywall


def unpaywall_lookup(fetcher: Fetcher, doi: str) -> dict | None:
    """OA status and best free location for a DOI; None when Unpaywall has no record."""
    from .http import FetchError

    try:
        payload = fetcher.get(f"{UNPAYWALL}{doi}", {"email": CONTACT_EMAIL}).json()
    except FetchError as exc:
        if exc.status == 404:
            return None
        raise
    best = payload.get("best_oa_location") or {}
    return {
        "is_oa": 1 if payload.get("is_oa") else 0,
        "oa_url": best.get("url_for_landing_page") or best.get("url"),
        "pdf_url": best.get("url_for_pdf"),
        "licence": best.get("license"),
        "host_type": best.get("host_type"),
        "oa_status": payload.get("oa_status"),
    }


def dumps(value) -> str:
    return json.dumps(value, ensure_ascii=False)


# ---------------------------------------------------- keyed / metered sources
#
# All three need credentials this machine does not have yet, so each is inert
# until its environment variable is set. They are wired but UNVERIFIED: no live
# response has been seen from them, unlike Europe PMC, Crossref and Unpaywall.
#
#   CORE_API_KEY              https://core.ac.uk/services/api  (free)
#   SEMANTIC_SCHOLAR_API_KEY  https://www.semanticscholar.org/product/api  (free)
#   OPENALEX_API_KEY          https://openalex.org/settings/api  (free, $1/day)

CORE_API_KEY = os.environ.get("CORE_API_KEY")
S2_API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
OPENALEX_API_KEY = os.environ.get("OPENALEX_API_KEY")

CORE_SEARCH = "https://api.core.ac.uk/v3/search/works"
S2_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
OPENALEX_WORKS = "https://api.openalex.org/works"


def core_works(fetcher: Fetcher, max_pages: int = MAX_PAGES) -> Iterator[dict]:
    """CORE aggregates open-access repository deposits, including full text."""
    if not CORE_API_KEY:
        return
    for page in range(max_pages):
        resp = fetcher.get(
            CORE_SEARCH,
            {"q": '"EuroQol Research Foundation"', "limit": PAGE_SIZE,
             "offset": page * PAGE_SIZE},
            headers={"Authorization": f"Bearer {CORE_API_KEY}"},
        )
        results = resp.json().get("results", [])
        yield from results
        if len(results) < PAGE_SIZE:
            return


def core_to_work(item: dict) -> dict | None:
    doi = normalize_doi(item.get("doi"))
    work_id = make_work_id(doi, None, None) or (
        f"core:{item['id']}" if item.get("id") else None
    )
    if not work_id:
        return None
    authors = [{"full_name": a.get("name"), "last_name": (a.get("name") or "").split()[-1]
                if a.get("name") else None, "orcid": None}
               for a in item.get("authors", [])]
    return {
        "work_id": work_id, "doi": doi, "pmid": None, "pmcid": None,
        "title": (item.get("title") or "").strip().rstrip("."),
        "journal": item.get("publisher"), "year": item.get("yearPublished"),
        "authors": authors, "is_oa": 1, "oa_url": item.get("downloadUrl"),
        "licence": None, "pdf_url": item.get("downloadUrl"),
        "source": "core", "grants": [], "abstract": item.get("abstract"),
    }


def openalex_funder_works(fetcher: Fetcher, max_pages: int = MAX_PAGES) -> Iterator[dict]:
    """OpenAlex works crediting the EuroQol funder.

    A free key carries a $1/day allowance, which at ~$0.0001 per request is ample for
    this corpus; the anonymous tier is what runs out immediately.

    The key travels in the Authorization header only, never as a query parameter:
    the cache is keyed by URL and stores it, so a query-param secret would be written
    into cache files and the ledger's `url` column in plain text.
    """
    if not OPENALEX_API_KEY:
        return
    for page in range(1, max_pages + 1):
        resp = fetcher.get(
            OPENALEX_WORKS,
            {"filter": f"funders.id:{OPENALEX_FUNDER_ID}", "per-page": PAGE_SIZE,
             "page": page, "mailto": CONTACT_EMAIL},
            headers={"Authorization": f"Bearer {OPENALEX_API_KEY}"},
        )
        results = resp.json().get("results", [])
        yield from results
        if len(results) < PAGE_SIZE:
            return


def openalex_to_work(item: dict) -> dict | None:
    doi = normalize_doi(item.get("doi"))
    ids = item.get("ids") or {}
    pmid = (ids.get("pmid") or "").rsplit("/", 1)[-1] or None
    pmcid = (ids.get("pmcid") or "").rsplit("/", 1)[-1] or None
    work_id = make_work_id(doi, pmid, pmcid)
    if not work_id:
        return None
    authors = []
    for a in item.get("authorships", []):
        name = (a.get("author") or {}).get("display_name") or ""
        authors.append({
            "full_name": name, "last_name": name.split()[-1] if name else None,
            "orcid": normalize_doi((a.get("author") or {}).get("orcid")),
        })
    # The API moved from `grants` to `awards`; accept either so an older cached
    # response still parses.
    grants = [
        {"grant_id": g.get("funder_award_id") or g.get("award_id"),
         "agency": g.get("funder_display_name") or ""}
        for g in (item.get("awards") or item.get("grants") or [])
        if g.get("funder_award_id") or g.get("award_id")
    ]
    oa = item.get("open_access") or {}
    return {
        "work_id": work_id, "doi": doi, "pmid": pmid, "pmcid": pmcid,
        "title": (item.get("title") or "").strip().rstrip("."),
        "journal": ((item.get("primary_location") or {}).get("source") or {}).get("display_name"),
        "year": item.get("publication_year"), "authors": authors,
        "is_oa": 1 if oa.get("is_oa") else 0, "oa_url": oa.get("oa_url"),
        "licence": ((item.get("best_oa_location") or {}).get("license")
                    or (item.get("primary_location") or {}).get("license")),
        "pdf_url": (item.get("best_oa_location") or {}).get("pdf_url"),
        "source": "openalex", "grants": grants, "abstract": None,
    }
