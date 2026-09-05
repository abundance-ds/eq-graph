#!/usr/bin/env python3
"""Parse publication metadata from JATS XML without AI."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


XLINK = "{http://www.w3.org/1999/xlink}href"
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"


def clean_text(element: ET.Element | None) -> str | None:
    if element is None:
        return None
    value = " ".join("".join(element.itertext()).split())
    return value or None


def first_text(parent: ET.Element, path: str) -> str | None:
    return clean_text(parent.find(path))


def date_value(element: ET.Element) -> str | None:
    year = first_text(element, "year")
    month = first_text(element, "month")
    day = first_text(element, "day")
    if not year:
        iso = element.get("iso-8601-date")
        return iso[:10] if iso else None
    parts = [year]
    if month:
        try:
            parts.append(f"{int(month):02d}")
        except ValueError:
            parts.append(month)
    if day:
        try:
            parts.append(f"{int(day):02d}")
        except ValueError:
            parts.append(day)
    return "-".join(parts)


def normalized_orcid(value: str | None) -> str | None:
    if not value:
        return None
    match = re.search(r"(\d{4}-\d{4}-\d{4}-[\dXx]{4})", value)
    return match.group(1).upper() if match else value.strip()


def normalized_doi(value: str | None) -> str | None:
    if not value:
        return None
    match = re.search(r"10\.\d{4,9}/[^\s<>\"\]]+", value, re.IGNORECASE)
    if not match:
        return None
    return match.group(0).rstrip(".,;:)]}").lower()


def author_id(name: str, orcid: str | None, publication_id: str, order: int) -> str:
    if orcid:
        return f"orcid:{orcid}"
    identity_basis = f"{publication_id}\t{order}\t{name.casefold()}"
    digest = hashlib.sha1(identity_basis.encode("utf-8")).hexdigest()[:16]
    return f"contrib:{digest}"


def parse_jats(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    root = ET.fromstring(raw)
    article_meta = root.find("./front/article-meta")
    journal_meta = root.find("./front/journal-meta")
    if article_meta is None or journal_meta is None:
        raise ValueError(f"Missing JATS front matter: {path}")

    identifiers: dict[str, str] = {}
    for element in article_meta.findall("article-id"):
        kind = element.get("pub-id-type")
        value = clean_text(element)
        if kind and value and kind not in identifiers:
            identifiers[kind] = value
    doi = identifiers.get("doi")
    if not doi:
        raise ValueError(f"Missing DOI: {path}")
    publication_id = f"doi:{doi.lower()}"

    dates: list[dict[str, str]] = []
    for element in article_meta.findall("pub-date"):
        value = date_value(element)
        kind = element.get("pub-type") or "publication"
        if value:
            dates.append({"type": kind, "value": value})
    for element in article_meta.findall("./history/date"):
        value = date_value(element)
        kind = element.get("date-type") or "history"
        if value:
            dates.append({"type": kind, "value": value})
    for event in article_meta.findall("./pub-history/event"):
        date = event.find("date")
        value = date_value(date) if date is not None else None
        kind = event.get("event-type") or "event"
        if value:
            dates.append({"type": kind, "value": value})

    urls: list[dict[str, str]] = []
    for element in article_meta.findall("self-uri"):
        href = element.get(XLINK)
        if href:
            urls.append({"type": element.get("content-type") or "self", "url": href})

    licence_url = None
    for element in article_meta.iter():
        if element.tag.endswith("license_ref"):
            licence_url = clean_text(element)
            if licence_url:
                break
    if not licence_url:
        for license_element in article_meta.findall(".//license"):
            for link in license_element.findall(".//ext-link"):
                candidate = link.get(XLINK) or clean_text(link)
                if candidate and candidate.startswith(("http://", "https://")):
                    licence_url = candidate
                    break
            if licence_url:
                break

    affiliations: list[dict[str, str | None]] = []
    affiliation_by_id: dict[str, dict[str, str | None]] = {}
    for index, element in enumerate(article_meta.findall(".//aff"), start=1):
        source_id = element.get("id") or f"aff-{index}"
        ids: dict[str, str] = {}
        for id_element in element.findall(".//institution-id"):
            kind = (id_element.get("institution-id-type") or "").lower()
            value = clean_text(id_element)
            if kind and value:
                ids[kind] = value
        record = {
            "id": source_id,
            "name": clean_text(element) or source_id,
            "ror": ids.get("ror"),
            "grid": ids.get("grid"),
            "isni": ids.get("isni"),
        }
        if source_id not in affiliation_by_id:
            affiliation_by_id[source_id] = record
            affiliations.append(record)

    authors: list[dict[str, Any]] = []
    order = 0
    parent_by_element = {
        child: parent for parent in article_meta.iter() for child in parent
    }
    author_contribs = []
    for contrib in article_meta.findall(".//contrib"):
        ancestor = parent_by_element.get(contrib)
        nested_in_contrib = False
        while ancestor is not None and ancestor is not article_meta:
            if ancestor.tag == "contrib":
                nested_in_contrib = True
                break
            ancestor = parent_by_element.get(ancestor)
        if not nested_in_contrib:
            author_contribs.append(contrib)
    for contrib in author_contribs:
        if contrib.get("contrib-type", "author") != "author":
            continue
        name_element = contrib.find("name")
        if name_element is None:
            family = None
            given = None
            display = clean_text(contrib.find("collab")) or "Unknown group author"
        else:
            family = first_text(name_element, "surname")
            given = first_text(name_element, "given-names")
            display = " ".join(value for value in (given, family) if value)
            if not display:
                display = clean_text(name_element) or "Unknown author"
        orcid = normalized_orcid(first_text(contrib, "contrib-id[@contrib-id-type='orcid']"))
        order += 1
        affiliations_for_author = [
            xref.get("rid")
            for xref in contrib.findall("xref[@ref-type='aff']")
            if xref.get("rid")
        ]
        authors.append(
            {
                "id": author_id(display, orcid, publication_id, order),
                "display_name": display,
                "family_name": family,
                "given_names": given,
                "orcid": orcid,
                "order": order,
                "corresponding": contrib.get("corresp") in {"yes", "true", "1"},
                "email": first_text(contrib, ".//email"),
                "roles": [value for value in (clean_text(role) for role in contrib.findall("role")) if value],
                "affiliation_ids": affiliations_for_author,
            }
        )

    keywords = [
        value
        for value in (clean_text(element) for element in article_meta.findall(".//kwd"))
        if value
    ]

    categories: list[dict[str, str | None]] = []
    for group in article_meta.findall("./article-categories//subj-group"):
        category_type = group.get("subj-group-type") or "unspecified"
        for subject in group.findall("subject"):
            value = clean_text(subject)
            if value:
                categories.append({"type": category_type, "value": value})

    correspondence: list[dict[str, str | None]] = []
    for element in article_meta.findall(".//corresp"):
        value = clean_text(element)
        if not value:
            continue
        correspondence.append(
            {
                "label": first_text(element, "label"),
                "text": value,
                "email": first_text(element, ".//email"),
            }
        )

    funding: list[dict[str, str | None]] = []
    seen_funding: set[tuple[str | None, str | None, str | None]] = set()
    for group in article_meta.findall(".//funding-group"):
        statements = [
            value
            for value in (clean_text(element) for element in group.findall(".//funding-statement"))
            if value
        ]
        for award in group.findall(".//award-group"):
            funder = first_text(award, ".//funding-source")
            award_value = first_text(award, ".//award-id")
            recipient = first_text(award, ".//principal-award-recipient")
            key = (funder, award_value, recipient)
            if key in seen_funding:
                continue
            seen_funding.add(key)
            funding.append(
                {
                    "funder": funder,
                    "award_id": award_value,
                    "recipient": recipient,
                    "source_text": " ".join(statements) or clean_text(award),
                    "source_locator": "JATS article-meta/funding-group",
                }
            )
    for notes in root.findall(".//notes[@notes-type='funding-information']"):
        source_text = clean_text(notes)
        if source_text and not funding:
            funding.append(
                {
                    "funder": None,
                    "award_id": None,
                    "recipient": None,
                    "source_text": source_text,
                    "source_locator": "JATS back/notes funding-information",
                }
            )

    references: list[dict[str, str | None]] = []
    for ref in root.findall(".//ref-list/ref"):
        doi_value = None
        pmid_value = None
        for pub_id in ref.findall(".//pub-id"):
            kind = pub_id.get("pub-id-type")
            value = clean_text(pub_id)
            if kind == "doi" and value and not doi_value:
                doi_value = normalized_doi(value)
            if kind == "pmid" and value and not pmid_value:
                pmid_value = value
        if not doi_value:
            for link in ref.findall(".//ext-link"):
                if link.get("ext-link-type") != "doi":
                    continue
                doi_value = normalized_doi(link.get(XLINK) or clean_text(link))
                if doi_value:
                    break
        citation_text = clean_text(ref)
        if not doi_value:
            doi_value = normalized_doi(citation_text)
        references.append(
            {
                "source_reference_id": ref.get("id"),
                "citation_text": citation_text,
                "doi": doi_value,
                "pmid": pmid_value,
            }
        )

    abstract_element = article_meta.find("abstract")
    issue = first_text(article_meta, "issue") or first_text(article_meta, "issue-id")
    article_number = first_text(article_meta, "elocation-id")
    if not article_number:
        first_page = first_text(article_meta, "fpage")
        last_page = first_text(article_meta, "lpage")
        if first_page:
            article_number = first_page if not last_page else f"{first_page}-{last_page}"

    return {
        "publication": {
            "publication_id": publication_id,
            "doi": doi.lower(),
            "pmid": identifiers.get("pmid"),
            "pmcid": identifiers.get("pmcid"),
            "title": first_text(article_meta, "./title-group/article-title") or doi,
            "abstract": clean_text(abstract_element),
            "journal": first_text(journal_meta, ".//journal-title"),
            "publisher": first_text(journal_meta, ".//publisher-name"),
            "article_type": root.get("article-type"),
            "language": root.get(XML_LANG),
            "volume": first_text(article_meta, "volume"),
            "issue": issue,
            "article_number": article_number,
            "licence_url": licence_url,
            "open_access": int(bool(licence_url)),
            "canonical_url": f"https://doi.org/{doi}",
            "source_path": str(path),
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "source_bytes": len(raw),
            "metadata_status": "parsed",
        },
        "dates": dates,
        "urls": urls,
        "authors": authors,
        "affiliations": affiliations,
        "correspondence": correspondence,
        "keywords": sorted(set(keywords)),
        "categories": categories,
        "funding": funding,
        "references": references,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("xml_path", type=Path)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    result = parse_jats(args.xml_path)
    print(json.dumps(result, ensure_ascii=False, indent=None if args.compact else 2))


if __name__ == "__main__":
    main()
