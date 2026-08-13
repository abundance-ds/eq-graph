#!/usr/bin/env python3
"""Protocol 2.0 reproducible 10-author pilot.

Stages are intentionally separate because AI outputs are immutable inputs to the
next stage: sources -> profile_input -> aggregate -> broad_input -> fulltext ->
assessment_input -> report.
"""

import argparse
import csv
import datetime as dt
import hashlib
import html
import json
import math
import pathlib
import random
import re
import subprocess
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
RAW = PILOT / "raw"
DERIVED = PILOT / "derived"
INPUTS = PILOT / "ai" / "inputs"
OUTPUTS = PILOT / "ai" / "outputs"
SEED = 20260801
RETRIEVED = dt.date.today().isoformat()
USER_AGENT = "eq-graph-protocol-2.0/0.1 (research pilot)"

SCHOLAR = {
    "Ben Van Hout": "n0m3GAIAAAAJ",
    "Gerard De Pouvourville": "w_ysIu8AAAAJ",
    "Fredrick Purba": "7X9G8WgAAAAJ",
}

PUBMED_QUERY_VERSION = "v2"
PUBMED_TOPIC = (
    '("EQ-5D"[Title/Abstract] OR EQ5D[Title/Abstract] OR EuroQol[Title/Abstract] OR '
    '"EQ-VT"[Title/Abstract] OR "EQ-HWB"[Title/Abstract] OR "EQ-TIPS"[Title/Abstract] OR '
    '"EQ-TANDI"[Title/Abstract] OR "health-related quality of life"[Title/Abstract] OR '
    'HRQoL[Title/Abstract] OR "quality of life"[Title/Abstract] OR '
    'psychometric*[Title/Abstract] OR validation[Title/Abstract] OR mapping[Title/Abstract] OR '
    '"health utility"[Title/Abstract] OR "health state"[Title/Abstract] OR '
    '"value set"[Title/Abstract] OR tariff[Title/Abstract] OR valuation[Title/Abstract] OR '
    '"time trade-off"[Title/Abstract] OR "discrete choice"[Title/Abstract] OR '
    '"patient-reported outcome"[Title/Abstract] OR PROM[Title/Abstract] OR '
    'QALY[Title/Abstract] OR "preference-based"[Title/Abstract] OR cost-utility[Title/Abstract])'
)

POSITIVE = re.compile(
    r"\b(eq[- ]?5d(?:[- ]?(?:3l|5l))?|eq[- ]?vt|eq[- ]?hwb|euroqol|"
    r"health[- ]related quality of life|hrqol|quality of life|qaly|qalys|"
    r"health utilit|utility value|health state|value set|tariff|"
    r"time trade[- ]?off|\btto\b|standard gamble|discrete choice|\bdce\b|"
    r"preference elicitation|patient preference|psychometric|validation|"
    r"responsiveness|content validity|construct validity|mapping|"
    r"patient[- ]reported outcome|\bproms?\b|\bprems?\b|"
    r"outcome measure|descriptive system|health valuation)", re.I,
)

JUNK = re.compile(
    r"^(erratum|correction|corrigendum|retraction|editorial|commentary|"
    r"letter(?: to the editor)?|reply|response|news|foreword|preface|"
    r"introduction to|peer review|referee report|additional file|"
    r"supplementary (?:file|material)|visual abstract)\b", re.I,
)

STOPWORDS = {
    "about", "after", "again", "against", "also", "among", "and", "are", "because", "been", "before",
    "being", "between", "both", "but", "can", "could", "did", "does", "during", "each", "for", "from",
    "had", "has", "have", "how", "into", "its", "may", "more", "most", "not", "our", "out", "over",
    "same", "should", "such", "than", "that", "the", "their", "then", "there", "these", "they", "this",
    "those", "through", "under", "using", "was", "were", "what", "when", "where", "which", "while", "who",
    "will", "with", "within", "would", "year", "years", "study", "project", "research", "results", "methods",
}


def ensure_dirs():
    for path in [RAW / "pubmed", RAW / "scholar", DERIVED, INPUTS, OUTPUTS]:
        path.mkdir(parents=True, exist_ok=True)


def slug(value):
    text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.casefold()).strip("-")


def norm_doi(value):
    text = html.unescape(value or "").replace("\u200b", "").strip()
    text = re.sub(
        r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)",
        "",
        text,
        flags=re.I,
    )
    match = re.search(r"10\.\d{4,9}/\S+", text, flags=re.I)
    if match:
        text = match.group(0)
    return text.rstrip(".,;").casefold()


def norm_title(value):
    text = unicodedata.normalize("NFKD", html.unescape(value or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", text.casefold()).strip()


def text_of(node):
    return " ".join("".join(node.itertext()).split()) if node is not None else ""


def http_get(url, path, accept="application/json"):
    if path.exists():
        return path.read_bytes()
    request = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read()
            path.write_bytes(body)
            return body
        except (urllib.error.URLError, TimeoutError):
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)


def sample_authors():
    source = json.loads((ROOT / "artefacts" / "orcid_openalex_check.json").read_text())
    ids = json.loads((ROOT / "artefacts" / "02_author_ids.json").read_text())
    people = {r["name"]: r for r in csv.DictReader(open(ROOT / "artefacts" / "01_people.csv"))}
    authors = []
    for item in source["authors"]:
        name = item["name"]
        resolved = ids[name]
        person = people[name]
        authors.append({
            "name": name,
            "openalex_id": item["openalex_id"],
            "openalex_url": f"https://openalex.org/{item['openalex_id']}",
            "orcid": item["orcid"],
            "orcid_url": f"https://orcid.org/{item['orcid']}",
            "scholar_id": SCHOLAR.get(name, ""),
            "scholar_url": (
                f"https://scholar.google.com/citations?user={SCHOLAR[name]}&hl=en"
                if name in SCHOLAR else ""
            ),
            "affiliation": (resolved.get("candidates") or [{}])[0].get("affiliation") or "",
            "member_affiliation": person.get("member_affiliation", ""),
            "project_ids": [x for x in person.get("project_ids", "").split(";") if x],
            "is_member": person.get("is_member") == "1",
            "is_project_leader": person.get("is_project_leader") == "1",
        })
    return source, authors


def pubmed_author_query(name, orcid=""):
    """PubMed indexes authors mainly as surname + initials."""
    parts = name.split()
    first_initial = parts[0][0]
    surname = " ".join(parts[1:])
    # Do not quote: quotes disable PubMed's automatic expansion E -> EA/EB/etc.
    variants = {f'{surname} {first_initial}[Author]'}
    # Particle handling differs across indexed records.
    if len(parts) > 2 and parts[1].casefold() in {"de", "van", "von"}:
        variants.add(f'{" ".join(parts[2:])} {first_initial}[Author]')
    if "'" in surname:
        variants.add(f'{surname.replace(chr(39), "")} {first_initial}[Author]')
    if orcid:
        variants.add(f'orcid {orcid}[Author Identifier]')
    return "(" + " OR ".join(sorted(variants)) + ")"


def parse_pubmed(xml_bytes):
    root = ET.fromstring(xml_bytes)
    records = []
    for citation in root.findall(".//PubmedArticle"):
        article = citation.find("./MedlineCitation/Article")
        journal_issue = article.find("./Journal/JournalIssue") if article is not None else None
        pmid = text_of(citation.find("./MedlineCitation/PMID"))
        title = text_of(article.find("ArticleTitle")) if article is not None else ""
        abstract = "\n".join(filter(None, [text_of(x) for x in article.findall("./Abstract/AbstractText")])) if article is not None else ""
        year = text_of(journal_issue.find("./PubDate/Year")) if journal_issue is not None else ""
        if not year:
            date_text = text_of(journal_issue.find("./PubDate/MedlineDate")) if journal_issue is not None else ""
            match = re.search(r"\b(19|20)\d{2}\b", date_text)
            year = match.group(0) if match else ""
        ids = {x.attrib.get("IdType", ""): text_of(x) for x in citation.findall("./PubmedData/ArticleIdList/ArticleId")}
        authors = []
        for author in article.findall("./AuthorList/Author") if article is not None else []:
            name = " ".join(filter(None, [text_of(author.find("ForeName")), text_of(author.find("LastName"))]))
            if name:
                authors.append(name)
        records.append({
            "source_id": pmid,
            "pmid": pmid,
            "pmcid": ids.get("pmc", ""),
            "doi": norm_doi(ids.get("doi", "")),
            "title": title,
            "year": int(year) if year.isdigit() else None,
            "abstract": abstract,
            "document_type": "; ".join(text_of(x) for x in article.findall("./PublicationTypeList/PublicationType")) if article is not None else "",
            "authors": authors,
        })
    for citation in root.findall(".//PubmedBookArticle"):
        document = citation.find("./BookDocument")
        if document is None:
            continue
        pmid = text_of(document.find("./PMID"))
        title = text_of(document.find("./ArticleTitle"))
        abstract = "\n".join(filter(None, [text_of(x) for x in document.findall("./Abstract/AbstractText")]))
        year = text_of(document.find("./Book/PubDate/Year")) or text_of(document.find("./ContributionDate/Year"))
        ids = {x.attrib.get("IdType", ""): text_of(x) for x in document.findall("./ArticleIdList/ArticleId")}
        authors = []
        for author in document.findall("./AuthorList[@Type='authors']/Author"):
            name = " ".join(filter(None, [text_of(author.find("ForeName")), text_of(author.find("LastName"))]))
            if name:
                authors.append(name)
        publication_type = text_of(document.find("./PublicationType"))
        records.append({
            "source_id": pmid, "pmid": pmid, "pmcid": "", "doi": norm_doi(ids.get("doi", "")),
            "title": title, "year": int(year) if year.isdigit() else None, "abstract": abstract,
            "document_type": "; ".join(filter(None, ["PubmedBookArticle", publication_type])),
            "authors": authors,
        })
    return records


def fetch_pubmed(author, version=PUBMED_QUERY_VERSION):
    name, name_slug = author["name"], slug(author["name"])
    term = f'{pubmed_author_query(name, author["orcid"])} AND {PUBMED_TOPIC}'
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed", "term": term, "retmode": "json", "retmax": 1000,
    })
    search_path = RAW / "pubmed" / f"{name_slug}-{version}-search.json"
    search = json.loads(http_get(search_url, search_path))
    pmids = search.get("esearchresult", {}).get("idlist", [])
    xml_path = RAW / "pubmed" / f"{name_slug}-{version}-records.xml"
    if pmids:
        fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + urllib.parse.urlencode({
            "db": "pubmed", "id": ",".join(pmids), "retmode": "xml",
        })
        records = parse_pubmed(http_get(fetch_url, xml_path, "application/xml"))
    else:
        xml_path.write_text("<PubmedArticleSet/>")
        records = []
    derived_path = DERIVED / f"pubmed-{version}-{name_slug}.json"
    derived_path.write_text(json.dumps(records, indent=2))
    return {
        "name": name, "version": version, "orcid": author["orcid"], "query": term,
        "query_translation": search.get("esearchresult", {}).get("querytranslation", ""),
        "search_url": search_url, "raw_search": str(search_path.relative_to(ROOT)),
        "raw_records": str(xml_path.relative_to(ROOT)), "esearch_n": len(pmids),
        "parsed_n": len(records), "derived": str(derived_path.relative_to(ROOT)),
    }


def stage_pubmed_v2():
    ensure_dirs()
    _, authors = sample_authors()
    queries = [fetch_pubmed(author) for author in authors]
    (DERIVED / "pubmed-v2-queries.json").write_text(json.dumps({
        "version": PUBMED_QUERY_VERSION, "retrieval_date": RETRIEVED,
        "topic_block": PUBMED_TOPIC, "authors": queries,
    }, indent=2))
    print(json.dumps([{k: x[k] for k in ["name", "esearch_n", "parsed_n"]} for x in queries], indent=2))


def parse_scholar(raw):
    lines = [x.strip() for x in raw.splitlines()]
    try:
        start = lines.index("YEAR") + 1
    except ValueError:
        return {"profile": lines[:8], "works": []}
    lines = [x for x in lines[start:] if x]
    blocks, block = [], []
    for line in lines:
        if line.startswith("Articles 1–") or line.startswith("Show more"):
            break
        block.append(line)
        if re.fullmatch(r"(?:\d+\s+)?(?:19|20)\d{2}", line):
            blocks.append(block)
            block = []
    works = []
    for i, values in enumerate(blocks):
        if len(values) < 2:
            continue
        last = values[-1].split()
        works.append({
            "source_id": str(i + 1), "title": values[0],
            "authors_text": values[1] if len(values) > 1 else "",
            "venue_text": " ".join(values[2:-1]),
            "year": int(last[-1]), "citations": int(last[0]) if len(last) == 2 else 0,
            "doi": "", "abstract": "", "document_type": "",
        })
    return {"profile": lines[:8], "works": works}


def stage_sources():
    ensure_dirs()
    source, authors = sample_authors()
    (DERIVED / "authors.json").write_text(json.dumps({
        "seed": source["seed"], "sample_size": source["sample_size"],
        "retrieval_date": RETRIEVED, "authors": authors,
    }, indent=2))
    summary, queries = [], []
    for author in authors:
        name, name_slug = author["name"], slug(author["name"])
        pubmed_info = fetch_pubmed(author)
        queries.append(pubmed_info)
        pubmed = json.loads((ROOT / pubmed_info["derived"]).read_text())

        scholar = {"profile": [], "works": []}
        if author["scholar_url"]:
            url = author["scholar_url"] + "&cstart=0&pagesize=100"
            raw_path = RAW / "scholar" / f"{name_slug}.txt"
            if not raw_path.exists():
                result = subprocess.run(["fetchpage", url, "4000"], text=True, capture_output=True, check=True)
                raw_path.write_text(result.stdout)
            scholar = parse_scholar(raw_path.read_text())
            (DERIVED / f"scholar-{name_slug}.json").write_text(json.dumps(scholar, indent=2))
        summary.append({"name": name, "pubmed": len(pubmed), "scholar": len(scholar["works"])})
    (DERIVED / "source_counts-v2.json").write_text(json.dumps(summary, indent=2))
    (DERIVED / "pubmed-v2-queries.json").write_text(json.dumps({
        "version": PUBMED_QUERY_VERSION, "retrieval_date": RETRIEVED,
        "topic_block": PUBMED_TOPIC, "authors": queries,
    }, indent=2))
    print(json.dumps(summary, indent=2))


def oa_abstract(work):
    inverted = work.get("abstract_inverted_index") or {}
    positions = [(pos, word) for word, values in inverted.items() for pos in values]
    return " ".join(word for _, word in sorted(positions))


def source_records(author):
    name_slug = slug(author["name"])
    check = json.loads((ROOT / "artefacts" / "orcid_openalex_check.json").read_text())
    check_author = next(x for x in check["authors"] if x["name"] == author["name"])
    orcid = []
    for i, work in enumerate(check_author["orcid_works"]):
        orcid.append({
            "source_id": str(i + 1), "title": work["title"], "year": int(work["year"]) if str(work["year"]).isdigit() else None,
            "doi": work["dois"][0] if work["dois"] else "", "abstract": "", "document_type": "",
        })
    oa_raw = json.loads((ROOT / "artefacts" / "03_works" / f"{author['openalex_id']}.json").read_text())
    openalex = []
    for work in oa_raw["works"]:
        openalex.append({
            "source_id": (work.get("id") or "").rsplit("/", 1)[-1], "title": work.get("title") or "",
            "year": work.get("publication_year"), "doi": norm_doi(work.get("doi") or ""),
            "abstract": oa_abstract(work), "document_type": work.get("type") or "",
            "authorships": [x.get("author", {}).get("display_name", "") for x in work.get("authorships", [])],
            "openalex": work,
        })
    pubmed_v2 = DERIVED / f"pubmed-v2-{name_slug}.json"
    pubmed = json.loads((pubmed_v2 if pubmed_v2.exists() else DERIVED / f"pubmed-{name_slug}.json").read_text())
    scholar_path = DERIVED / f"scholar-{name_slug}.json"
    scholar = json.loads(scholar_path.read_text())["works"] if scholar_path.exists() else []
    return {"orcid": orcid, "openalex": openalex, "pubmed": pubmed, "scholar": scholar}


def representative(records, seed_text, n=18):
    if len(records) <= n:
        chosen = records
    else:
        rng = random.Random(int(hashlib.sha256(seed_text.encode()).hexdigest()[:16], 16))
        recent = sorted(records, key=lambda x: (x.get("year") or 0, x.get("title") or ""), reverse=True)[:6]
        pool = [x for x in records if x not in recent]
        chosen = recent + rng.sample(pool, n - len(recent))
    return [{k: x.get(k, "") for k in ["title", "year", "document_type", "authors_text", "venue_text"]} for x in chosen]


def stage_profile_input():
    authors = json.loads((DERIVED / "authors.json").read_text())["authors"]
    items = []
    for author in authors:
        for source_name, records in source_records(author).items():
            if not records:
                continue
            items.append({
                "author_name": author["name"], "source": source_name,
                "source_id": author.get(f"{source_name}_id", ""),
                "source_url": author.get(f"{source_name}_url", ""),
                "expected_affiliation": author["member_affiliation"] or author["affiliation"],
                "work_count": len(records),
                "works": [{k: x.get(k, "") for k in ["title", "year", "document_type", "authors_text", "venue_text"]} for x in records],
            })
    (DERIVED / "profile_evidence.json").write_text(json.dumps(items, indent=2))
    template = (PILOT / "ai" / "prompts" / "profile-verification.md").read_text()
    (INPUTS / "profile-verification.txt").write_text(template + "\n\nSOURCE PROFILES\n" + json.dumps(items, ensure_ascii=False, indent=2))
    print(f"profiles={len(items)} -> {INPUTS / 'profile-verification.txt'}")


def stage_pubmed_v2_profile_input():
    authors = json.loads((DERIVED / "authors.json").read_text())["authors"]
    items = []
    for author in authors:
        records = source_records(author)["pubmed"]
        items.append({
            "author_name": author["name"], "source": "pubmed",
            "source_id": "", "source_url": "",
            "expected_affiliation": author["member_affiliation"] or author["affiliation"],
            "work_count": len(records),
            "works": [{k: x.get(k, "") for k in ["title", "year", "document_type"]} for x in records],
        })
    (DERIVED / "pubmed-v2-profile-evidence.json").write_text(json.dumps(items, indent=2))
    template = (PILOT / "ai" / "prompts" / "profile-verification.md").read_text()
    target = INPUTS / "pubmed-v2-profile-verification.txt"
    target.write_text(template + "\n\nPUBMED V2 SEARCH RESULTS\n" + json.dumps(items, ensure_ascii=False, indent=2))
    print(f"profiles={len(items)} -> {target}")


def profile_statuses():
    path = OUTPUTS / "profile-verification.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text())
    out = {(x["author_name"], x["source"]): x for x in data["decisions"]}
    v2 = OUTPUTS / "pubmed-v2-profile-verification.json"
    if v2.exists():
        for item in json.loads(v2.read_text())["decisions"]:
            out[(item["author_name"], item["source"])] = item
    return out


def record_key(record):
    if record.get("doi"):
        return "doi:" + norm_doi(record["doi"])
    if record.get("pmid"):
        return "pmid:" + record["pmid"]
    return "title:" + norm_title(record.get("title", "")) + ":" + str(record.get("year") or "")


def eligibility(record):
    """Apply the protocol's publication-output rule; leave missing types unresolved."""
    if JUNK.search(record.get("title", "")):
        return "exclude_document", "title identifies document junk"
    kind = (record.get("document_type") or "").strip().lower()
    if not kind:
        return "uncertain", "publication type missing"
    if kind in {"article", "review"} or "journal article" in kind:
        return "candidate_full_journal_article", "source labels journal article"
    return "exclude_non_journal", f"source type: {kind}"


def stage_aggregate():
    authors = json.loads((DERIVED / "authors.json").read_text())["authors"]
    statuses = profile_statuses()
    merged = {}
    by_doi, by_pmid, by_title_year = {}, {}, {}
    source_counts = {}
    for author in authors:
        for source_name, records in source_records(author).items():
            decision = statuses.get((author["name"], source_name), {"status": "caution"})
            if decision["status"] == "reject":
                continue
            source_counts[f"{author['name']}|{source_name}"] = len(records)
            for raw in records:
                record = {k: v for k, v in raw.items() if k != "openalex"}
                record["doi"] = norm_doi(record.get("doi", ""))
                doi = record.get("doi", "")
                pmid = record.get("pmid", "")
                title_year = norm_title(record.get("title", "")) + ":" + str(record.get("year") or "")
                key = (by_doi.get(doi) if doi else None) or (by_pmid.get(pmid) if pmid else None) or by_title_year.get(title_year)
                key = key or record_key(record)
                if key not in merged:
                    merged[key] = {
                        "record_id": "P" + hashlib.sha1(key.encode()).hexdigest()[:12],
                        "title": record.get("title", ""), "year": record.get("year"),
                        "doi": record.get("doi", ""), "pmid": record.get("pmid", ""),
                        "pmcid": record.get("pmcid", ""), "abstract": record.get("abstract", ""),
                        "document_type": record.get("document_type", ""),
                        "authors": [], "sources": [], "profile_flags": [],
                    }
                target = merged[key]
                if len(record.get("abstract", "")) > len(target["abstract"]):
                    target["abstract"] = record["abstract"]
                for field in ["doi", "pmid", "pmcid", "document_type"]:
                    if not target.get(field) and record.get(field):
                        target[field] = record[field]
                if author["name"] not in target["authors"]:
                    target["authors"].append(author["name"])
                target["sources"].append({"author": author["name"], "source": source_name, "source_id": record.get("source_id", "")})
                if decision["status"] == "caution":
                    target["profile_flags"].append(f"{author['name']}:{source_name}")
                if doi:
                    by_doi[doi] = key
                if pmid:
                    by_pmid[pmid] = key
                if title_year:
                    by_title_year[title_year] = key
    records = sorted(merged.values(), key=lambda x: (x["authors"], -(x["year"] or 0), x["title"]))
    for record in records:
        record["document_filter"] = "exclude" if JUNK.search(record["title"]) else "keep"
        record["eligibility_status"], record["eligibility_reason"] = eligibility(record)
        record["positive_signal"] = bool(POSITIVE.search(record["title"] + " " + record["abstract"]))
    (DERIVED / "works.json").write_text(json.dumps(records, ensure_ascii=False, indent=2))
    counts = {
        "source_records_used": sum(source_counts.values()), "deduplicated_works": len(records),
        "document_excluded": sum(x["document_filter"] == "exclude" for x in records),
        "non_journal_excluded": sum(x["eligibility_status"] == "exclude_non_journal" for x in records),
        "publication_type_uncertain": sum(x["eligibility_status"] == "uncertain" for x in records),
        "full_journal_article_candidates": sum(
            x["eligibility_status"] == "candidate_full_journal_article" for x in records
        ),
        "positive_signal": sum(x["positive_signal"] for x in records),
    }
    (DERIVED / "aggregate_counts.json").write_text(json.dumps(counts, indent=2))
    print(json.dumps(counts, indent=2))


def stage_broad_input():
    records = [
        x for x in json.loads((DERIVED / "works.json").read_text())
        if x.get("eligibility_status") == "candidate_full_journal_article"
    ]
    authors = [x["name"] for x in json.loads((DERIVED / "authors.json").read_text())["authors"]]
    chosen = []
    for name in authors:
        pool = [x for x in records if name in x["authors"]]
        positive = [x for x in pool if x["positive_signal"]]
        other = [x for x in pool if not x["positive_signal"]]
        rng = random.Random(SEED + authors.index(name))
        selected = rng.sample(positive, min(10, len(positive)))
        selected += rng.sample(other, min(10, len(other)))
        chosen.extend(selected)
    unique = {x["record_id"]: x for x in chosen}
    payload = [{
        "record_id": x["record_id"], "authors_in_people_set": x["authors"],
        "title": x["title"], "year": x["year"], "document_type": x["document_type"],
        "abstract": x["abstract"][:2500], "sources": x["sources"],
    } for x in unique.values()]
    (DERIVED / "broad_sample.json").write_text(json.dumps({"seed": SEED, "records": payload}, ensure_ascii=False, indent=2))
    template = (PILOT / "ai" / "prompts" / "broad-filter.md").read_text()
    (INPUTS / "broad-filter.txt").write_text(template + "\n\nRECORDS\n" + json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"records={len(payload)} -> {INPUTS / 'broad-filter.txt'}")


def epmc_lookup(record):
    query = f'DOI:"{record["doi"]}"' if record.get("doi") else f'EXT_ID:{record.get("pmid", "")}'
    if not query or query == "EXT_ID:":
        return {}
    cache = RAW / "europe-pmc" / f"{record['record_id']}-search.json"
    cache.parent.mkdir(parents=True, exist_ok=True)
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({
        "query": query, "format": "json", "pageSize": 5,
    })
    data = json.loads(http_get(url, cache))
    results = data.get("resultList", {}).get("result", [])
    for result in results:
        if record.get("doi") and norm_doi(result.get("doi", "")) == norm_doi(record["doi"]):
            return result
        if record.get("pmid") and result.get("pmid", "") == record["pmid"]:
            return result
    return {}


def stage_fulltext():
    decisions = {x["record_id"]: x for x in json.loads((OUTPUTS / "broad-filter.json").read_text())["decisions"]}
    records = {x["record_id"]: x for x in json.loads((DERIVED / "works.json").read_text())}
    authors = json.loads((DERIVED / "authors.json").read_text())["authors"]
    selected, used = [], set()
    for author in authors:
        candidates = [records[rid] for rid, d in decisions.items()
                      if rid not in used and d["decision"] in {"keep", "uncertain"} and author["name"] in records[rid]["authors"]]
        candidates.sort(key=lambda x: (not x["positive_signal"], -(x["year"] or 0), x["title"]))
        best = None
        for record in candidates:
            epmc = epmc_lookup(record)
            if best is None:
                best = (record, epmc)
            if epmc.get("pmcid"):
                best = (record, epmc)
                break
        if not best:
            continue
        record, epmc = best
        used.add(record["record_id"])
        item = dict(record)
        item["europe_pmc"] = epmc
        item["fulltext_status"] = "abstract_only"
        item["evidence_text"] = record["abstract"]
        pmcid = epmc.get("pmcid", "")
        if pmcid:
            xml_path = RAW / "europe-pmc" / f"{record['record_id']}-{pmcid}.xml"
            url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
            try:
                xml = http_get(url, xml_path, "application/xml")
                root = ET.fromstring(xml)
                body = text_of(root.find(".//body"))
                back = text_of(root.find(".//back"))
                if body:
                    item["evidence_text"] = body + ("\n\nBACK MATTER\n" + back if back else "")
                    item["fulltext_status"] = "full_text"
            except (urllib.error.URLError, ET.ParseError):
                pass
        selected.append(item)
    (DERIVED / "fulltext_sample.json").write_text(json.dumps(selected, ensure_ascii=False, indent=2))
    print(json.dumps([{"author": x["authors"], "title": x["title"], "status": x["fulltext_status"]} for x in selected], indent=2))


def terms(text):
    return [x for x in re.findall(r"[a-z0-9]+", (text or "").casefold()) if len(x) >= 3 and x not in STOPWORDS]


def semantic_project_scores(record, projects_by_id):
    projects = list(projects_by_id.values())
    project_terms = {}
    document_frequency = Counter()
    for project in projects:
        tokens = terms((project["Title"] + " ") * 5 + project["Abstract"])
        project_terms[project["Project Id"]] = Counter(tokens)
        document_frequency.update(set(tokens))
    n = len(projects)
    idf = {word: math.log((n + 1) / (count + 1)) + 1 for word, count in document_frequency.items()}

    paper = Counter(terms((record["title"] + " ") * 5 + record["evidence_text"]))
    paper_vector = {word: (1 + math.log(count)) * idf.get(word, 1) for word, count in paper.items()}
    paper_norm = math.sqrt(sum(value * value for value in paper_vector.values())) or 1
    scores = []
    for project_id, counts in project_terms.items():
        vector = {word: (1 + math.log(count)) * idf[word] for word, count in counts.items()}
        norm = math.sqrt(sum(value * value for value in vector.values())) or 1
        dot = sum(paper_vector.get(word, 0) * value for word, value in vector.items())
        scores.append((dot / (paper_norm * norm), project_id))
    return sorted(scores, reverse=True)


def project_candidates(record, projects_by_id):
    people = {r["name"]: r for r in csv.DictReader(open(ROOT / "artefacts" / "01_people.csv"))}
    origins = {}
    for author in record["authors"]:
        for project_id in people[author]["project_ids"].split(";"):
            if project_id in projects_by_id:
                origins.setdefault(project_id, set()).add("author")
    haystack = record["title"] + " " + record["evidence_text"]
    for project_id in projects_by_id:
        if re.search(rf"(?<!\w){re.escape(project_id)}(?!\w)", haystack, re.I):
            origins.setdefault(project_id, set()).add("id_string")
    similarities = dict((project_id, score) for score, project_id in semantic_project_scores(record, projects_by_id))
    for _, project_id in semantic_project_scores(record, projects_by_id)[:10]:
        origins.setdefault(project_id, set()).add("semantic")
    projects = [projects_by_id[x] for x in origins]
    year = record.get("year") or 9999
    projects.sort(key=lambda x: (
        "id_string" not in origins[x["Project Id"]],
        "author" not in origins[x["Project Id"]],
        -similarities.get(x["Project Id"], 0),
        abs((int(x["Start Year"]) if x["Start Year"].isdigit() else year) - year),
        x["Project Id"],
    ))
    return [{
        "project_id": x["Project Id"], "title": x["Title"], "start_year": x["Start Year"],
        "end_year": x["End Year"], "pi": x["Project PI / Applicant Name"],
        "working_group": x["Working Group"], "abstract": x["Abstract"],
        "candidate_source": sorted(origins[x["Project Id"]]),
        "lexical_similarity": round(similarities.get(x["Project Id"], 0), 6),
    } for x in projects]


def stage_assessment_input():
    projects = {r["Project Id"]: r for r in csv.DictReader(open(ROOT / "data" / "funded-projects-canonical.csv"))}
    papers = []
    for record in json.loads((DERIVED / "fulltext_sample.json").read_text()):
        papers.append({
            "record_id": record["record_id"], "title": record["title"], "year": record["year"],
            "doi": record["doi"], "people_set_authors": record["authors"],
            "evidence_source": record["fulltext_status"],
            "paper_text": record["evidence_text"],
            "candidate_projects": project_candidates(record, projects),
        })
    (DERIVED / "assessment_sample.json").write_text(json.dumps(papers, ensure_ascii=False, indent=2))
    template = (PILOT / "ai" / "prompts" / "project-assessment.md").read_text()
    (INPUTS / "project-assessment.txt").write_text(template + "\n\nPAPERS AND CANDIDATE PROJECTS\n" + json.dumps(papers, ensure_ascii=False, indent=2))
    print(f"papers={len(papers)} -> {INPUTS / 'project-assessment.txt'}")


def stage_report():
    authors = json.loads((DERIVED / "authors.json").read_text())["authors"]
    source_counts = json.loads((DERIVED / "source_counts.json").read_text())
    aggregate = json.loads((DERIVED / "aggregate_counts.json").read_text())
    profiles = json.loads((OUTPUTS / "profile-verification.json").read_text())["decisions"]
    broad = json.loads((OUTPUTS / "broad-filter.json").read_text())["decisions"]
    fulltexts = json.loads((DERIVED / "fulltext_sample.json").read_text())
    assessed = json.loads((OUTPUTS / "project-assessment.json").read_text())["assessments"]
    profile_count = {x: sum(y["status"] == x for y in profiles) for x in ["accept", "caution", "reject"]}
    broad_count = {x: sum(y["decision"] == x for y in broad) for x in ["keep", "uncertain", "exclude"]}
    ai_count = {str(x): sum(y["decision"] == x for y in assessed) for x in range(1, 6)}
    works = json.loads((DERIVED / "works.json").read_text())
    route_count = {source: sum(s["source"] == source for x in works for s in x["sources"])
                   for source in ["orcid", "scholar", "pubmed", "openalex"]}
    lines = [
        "# Protocol 2.0 pilot", "", "## Scope", "",
        f"- Seed: `{SEED}`.", f"- Authors: {len(authors)}.", f"- Retrieval date: `{RETRIEVED}`.",
        "- Google Scholar profiles: known public profiles only; no automated profile discovery.", "",
        "## Funnel", "",
        f"- Source records accepted for merging: {aggregate['source_records_used']}.",
        f"- Source records by route: `{json.dumps(route_count, sort_keys=True)}`.",
        f"- Deduplicated works: {aggregate['deduplicated_works']}.",
        f"- Objective document exclusions: {aggregate['document_excluded']}.",
        f"- Broad-filter evaluation sample: {len(broad)}; `{json.dumps(broad_count, sort_keys=True)}`.",
        f"- Full-text assessment sample: {len(fulltexts)}; full text {sum(x['fulltext_status']=='full_text' for x in fulltexts)}; abstract only {sum(x['fulltext_status']!='full_text' for x in fulltexts)}.",
        f"- Final AI decisions: `{json.dumps(ai_count, sort_keys=True)}`.", "",
        "## Profile check", "",
        f"- Decisions: `{json.dumps(profile_count, sort_keys=True)}`.",
        "- Input: every listed work for each source; no title sampling.",
        "- Full-list rerun changed four sources from `accept` to `caution`; reject set unchanged.",
        "- `caution`: source retained; record-level noise remains reviewable.",
        "- `reject`: source omitted before merging.", "",
        "## Filter calibration", "",
        "- Corpus inspected: 2,311 source records; 80-record audit; seed `20260801`.",
        "- Refinements: 12.",
        "- Frozen rule: remove objective document junk; exclude topically only when clearly outside; retain uncertainty.",
        "- Profile contamination is resolved upstream, not with topic rules.", "",
        "## Evaluation", "",
        "- Broad sample: per author, up to 10 positive-signal + 10 other records; deterministic; not prevalence-estimating.",
        "- Full-text sample: one retained paper per author; positive-signal first; newest first; Europe PMC full text preferred.",
        "- Broad result: 183/189 retained; high recall; limited workload reduction.",
        "- Project result: two clear/best links; two direct EQ papers lacked a listed matching project.",
        "- Link evidence: one exact acknowledgement; one semantic methods/date match without project acknowledgement.",
        "- Strength: raw inputs, seeds, prompts, schemas, traces and outputs are retained.",
        "- Strength: full-text AI uses acknowledgements as optional evidence, not a required grant-number match.",
        "- Audit: wrong PubMed descendant-ID XPath produced a title/full-text mismatch; detected; fixed; downstream rerun.",
        "- Limitation: Scholar profile discovery is manual; only verified public profiles enter.",
        "- Limitation: full-text selection is purposive; outputs test workflow, not study prevalence.",
        "- Limitation: abstract fallback exists but was not exercised; all 10 pilot texts were open.", "",
        "## Files", "",
        "- `derived/authors.json`: author/source identifiers.",
        "- `raw/`: immutable downloaded responses.",
        "- `derived/works.json`: deduplicated works.",
        "- `derived/fulltext_sample.json`: assessment evidence.",
        "- `ai/prompts/`: reusable instructions.",
        "- `ai/inputs/`: exact filled prompts.",
        "- `ai/schemas/`: output contracts.",
        "- `ai/outputs/`: final JSON.",
        "- `ai/traces/`: Codex JSONL event logs and run metadata.",
    ]
    (PILOT / "PILOT.md").write_text("\n".join(lines) + "\n")
    print(PILOT / "PILOT.md")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=["sources", "pubmed-v2", "profile-input", "pubmed-v2-profile-input", "aggregate", "broad-input", "fulltext", "assessment-input", "report"])
    args = parser.parse_args()
    ensure_dirs()
    globals()["stage_" + args.stage.replace("-", "_")]()


if __name__ == "__main__":
    main()
