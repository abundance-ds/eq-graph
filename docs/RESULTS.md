# Pipeline results

Release `beta-2026-08-29`.
Method: [METHOD.md](METHOD.md).
Release contents and validation: [DATA_RELEASE.md](DATA_RELEASE.md).

## Funnel

| Stage | Input | Output | Decision rule | Tool / model | Closed |
|---|---:|---|---|---|---|
| Discovery | 44,583 raw | 28,600 distinct | Merge by DOI, PMID, title+year | OpenAlex, ORCID, PubMed | 2026-08-24 |
| Article gate | 28,600 | 18,348 | Article or review with 80+ char abstract | Deterministic | 2026-08-24 |
| Abstract screen | 18,348 | 1,679 retrieve / 16,669 exclude | Could have EuroQol support or be a funded-project output | gpt-5.6-terra via Codex | 2026-08-24 |
| Full-text retrieval | 1,679 | 1,607 verified / 72 not retrieved | File matches publication identity | Europe PMC, OA PDF, OpenAlex, Unpaywall; manual | 2026-08-26 |
| Full-text preparation | 1,607 | 1,607 prepared (885 JATS, 722 PDF) | Extraction-ready Markdown with deterministic metadata | pymupdf4llm + pikepdf; pandoc | 2026-08-26 |
| Full-text processing | 1,607 | 797 included / 810 excluded | Explicit EuroQol support or accepted project link | Claude Opus + Sol (Codex) | 2026-08-27 |
| Load and release | 797 | `beta-2026-08-29` | Integrity, identity, and privacy checks | export_public_release.py | 2026-08-29 |

## Discovery and deduplication

44,583 raw source records from three routes: OpenAlex 27,371, ORCID 14,102, PubMed 3,110.
15,983 duplicate records removed by DOI, then PMID, then normalized title and year.
28,600 distinct publication records remained.

10,252 records removed at the article gate before AI screening: 5,425 other document types and 4,827 missing or short abstracts.
18,348 records entered the abstract screen.

Tracked summaries: [`identifier-source-summary.json`](../scale/protocol-2.0/identifier-source-summary.json), [`openalex-discovery-summary.json`](../scale/protocol-2.0/openalex-discovery-summary.json), [`source-union-summary.json`](../scale/protocol-2.0/source-union-summary.json), [`abstract-enrichment-summary.json`](../scale/protocol-2.0/abstract-enrichment-summary.json).

## Abstract screen

| Metric | Value |
|---|---:|
| Input records | 18,348 |
| RETRIEVE_FULL_TEXT | 1,679 |
| EXCLUDE | 16,669 |
| Validation sample correct | 9 / 10 |

Model: `gpt-5.6-terra`, medium reasoning, Codex subscription, one publication per call.
The first 17,789 completed records received every qualifying project; the remaining 559 received only projects that started within the previous 10 years.

A stratified random check (seed `20260824`, five retrievals and five exclusions including four from the 10-year tail) found nine correct decisions.
One eye-care paper was over-routed because an author led a different EuroQol project, a precision error, not a false exclusion.

- Frozen prompt SHA-256: `2bc59f11b92c0aaf1823bb1b97457dd51721f0fd94b4684faade1e3fef928aef`
- Compiled result SHA-256: `e2db4c7a6166c9805a69d5692c44b9431ff83c45abed4ee66aba5d74f427239b`

## Full-text retrieval

| Metric | Value |
|---|---:|
| Routed to retrieval | 1,679 |
| Verified full text | 1,607 |
| — XML | 885 |
| — PDF | 722 |
| Not retrieved | 72 |

"Verified" means the file matches the expected publication, not that the publication is eligible.

**Automated pass (2026-08-24).** A resumable runner tried Europe PMC JATS, indexed open-access PDFs, OpenAlex, and Unpaywall.
It verified 1,153 records (885 XML, 268 PDF) and referred 526 to manual retrieval.
Luna reviewed eight unclear first-page cases.

**Manual pass (2026-08-25 to 2026-08-26).** An operator worked the 526 through an institutional entitlement; a colleague contributed two files.
This added 454 records.
The identity check rejected six misfiled PDFs.
Routes are per publisher; they are documented in [MANUAL_FULLTEXT_DOWNLOAD.md](../pipeline/MANUAL_FULLTEXT_DOWNLOAD.md).

- Queue SHA-256: `4628d6e86486d6b540a26dfe766bb071aade8c7e9d1943bba642ee1f91c009bf`
- Result SHA-256: `950162a7dbbe8fe37fbf3bf4ea4a878782060ab479cbcdb51f9f1a7c07c6cfb4`

**Reversal.** Delete the row from `data/fulltext-not-retrieved.csv`, place the file in the manual directory, and rerun the retrieval runner with `--retry --record-id`.

### Disposition of the 72 not retrieved

| Disposition | Records | Revisit |
|---|---:|---|
| outside_scope | 36 | no |
| not_accessible | 20 | yes |
| not_found | 12 | yes |
| supplement_only | 2 | no |
| abstract_only | 1 | no |
| duplicate | 1 | no |

The 32 records flagged `revisit = yes` are the reacquisition list.
Each row is registered in [`data/fulltext-not-retrieved.csv`](../data/fulltext-not-retrieved.csv).

### Operator scope screen

An operator scope screen removed 36 records from the retrieval queue on 2026-08-26.
The criterion: the title is clearly off-topic, and the abstract screen's reason rests on author or PI-name plausibility rather than funding evidence.
The screen was applied once, by hand, to the manual queue only.

Diagnostic counts across the 1,679 routed records:

| Routing basis | Records |
|---|---:|
| Reason contains a hedge | 424 |
| No project nominated | 217 |
| Reason cites funder metadata or acknowledgement | 416 |

The 36-row register is in [SCOPE_SCREEN_RESULT.md](../archive/docs/results/SCOPE_SCREEN_RESULT.md) and in [`data/fulltext-not-retrieved.csv`](../data/fulltext-not-retrieved.csv) (rows with `outside_scope`).

## Full-text preparation

| Metric | Value |
|---|---:|
| Sources prepared | 1,607 |
| — JATS | 885 |
| — PDF | 722 |
| Paper packages | 1,607 |
| — with nominated project rows | 1,397 |
| — without | 210 |
| Failures | 0 |

315 PDFs needed font-map repair, covering 1,208 character codes.
Publisher PDFs draw mathematical symbols from fonts with no usable `/ToUnicode` map; an unrepaired extractor silently corrupts numbers.
Repair uses verified font and glyph identity in a temporary copy.

163 PDFs fell back to a bounded Poppler layout pass with 4,861 explicit unreadable-glyph markers.
33 repository cover-sheet pages were dropped where the leading page carried known repository branding.

Markdown is the reading copy; the verified PDF or JATS file is the source of record.
Converter decision: [PDF_PARSING.md](../pipeline/PDF_PARSING.md).

## Full-text processing

| Metric | Value |
|---|---:|
| Assessed | 1,607 |
| Included | 797 |
| Excluded | 810 |
| Included with project links | 603 |
| — JATS sources among included | 452 |
| — PDF sources among included | 345 |

The 20-paper comparison set and the first 332 single-agent records used the same governing eligibility and evidence rules.
The final 1,255-paper run used 275 Opus calls (Claude Code) and 980 Sol calls (Codex).
Saved records are authoritative for resume; no paper was repeated across the switch.

Registry consolidation retained 3,311 global instrument, method, protocol, model, software, and product identities.
It merged 31 punctuation-only duplicates and withheld two ambiguous acronym aliases.

Release counts (studies, evidence items, links, findings, people, citations) and the aggregate validity test: [DATA_RELEASE.md](DATA_RELEASE.md).

## Records

- [Abstract screen result](../archive/docs/results/ABSTRACT_SCREEN_RESULT.md) (verbatim original)
- [Full-text retrieval result](../archive/docs/results/FULLTEXT_RETRIEVAL_RESULT.md) (verbatim original)
- [Full-text preparation result](../archive/docs/results/FULLTEXT_PREPARATION_RESULT.md) (verbatim original)
- [Full-text processing result](../archive/docs/results/FULLTEXT_PROCESSING_RESULT.md) (verbatim original)
- [Scope screen result](../archive/docs/results/SCOPE_SCREEN_RESULT.md) (verbatim original)

Local run folders are listed in [scale/README.md](../scale/README.md).
