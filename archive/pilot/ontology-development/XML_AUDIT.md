# JATS XML audit

Date: 2026-08-16.

Scope: 220 XML files, 209 unique DOIs.
Eleven files are copies under more than one project.

## Coverage

| Data | Files |
| --- | ---: |
| DOI, PMID, PMCID, title, journal, authors, licence, references | 220 |
| Abstract, affiliations, body sections | 219 |
| Tables | 207 |
| Figures | 172 |
| Supplementary material | 135 |
| Funding | 116 |
| Article history | 115 |
| ORCID | 102 |
| Keywords | 88 |

The XML contains 1,337 authors, 1,053 affiliations, 9,890 references, 5,290 sections, 872 tables, 218 funding-source elements and 202 award identifiers.

## Current conversion

`scripts/to_markdown.py` already extracts identifiers, title, journal, one publication date, volume, issue, authors, ORCIDs, affiliation links, flattened affiliations, keywords, manifest licence and source provenance.
It also restores the abstract and reference list after Pandoc conversion.

Important structured data does not survive fully:

- Funding is not a structured Markdown field.
- Licence URLs occur in only 6 Markdown files, although XML URL forms occur in at least 206 files.
- Multiple publication and article-history dates become one selected date.
- Author roles, correspondence details and structured affiliation identifiers are omitted.
- Affiliations lose 199 ROR, 334 GRID and 320 ISNI identifiers when flattened.
- References become strings, although XML holds 8,179 reference DOIs and 4,411 reference PMIDs.
- Section IDs and types are not explicit in Markdown.
- Reference lists add substantial text when a task does not need them.

JATS variants need deterministic parser rules for dates, licences, contributor types, citations, journal-name normalization and other source differences.
They do not need AI judgment.

## Decision

- Keep raw JATS XML as the canonical structured source.
- Deduplicate papers by work identity before batching.
- Extract available metadata before AI work; preserve missing values and source provenance.
- Give agents a compact source-derived metadata record and section-aware article text.
- Include tables or references only when the task needs them.
- Tell agents not to re-extract supplied metadata and to flag conflicts or gaps.
- Use AI only for information that requires interpretation.
