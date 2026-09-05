# Pipeline recap

## Two separate discovery routes

```text
PROJECT-FIRST ROUTE                         LITERATURE-FIRST ROUTE
1,024 EuroQol projects                     author and funder searches
  -> candidate project-output matches        -> 28,600 distinct records
  -> 305 works above the match threshold      -> 18,348 usable abstracts
  -> 287 held full texts                      -> 1,679 routed to full text
  -> 220 JATS + 67 PDF files                  -> 16,669 abstract exclusions
  -> 273 audited publications
```

The **305** means that an automated project-work match had strong discovery
evidence. It does not mean that a full-text inclusion assessment occurred.
Evidence included an explicit EuroQol grant identifier, a near-exact title
match, or another strong combination of acknowledgement, title, investigator,
and date evidence. This route supplied the first available full-text corpus.

The former topic screen retained **3,148** papers from the broader author and
funder searches. That result is historical because the screen did not test the
funded-project scope. The corrected Terra screen assessed all 18,348 usable
abstracts. It routed 1,679 publications to full-text retrieval and excluded
16,669 from that queue. Retrieval verified 1,607 full texts and closed with 72
unavailable records.

## What happened to the local papers

Eleven papers had two XML copies because each copy was filed under a different
project. DOI grouping reduced 220 JATS files to 209 publications. One Opus call
per paper made the full-text inclusion decision and drafted the semantic
record. A fresh second Opus call checked the full source and returned the
complete corrected record. All 209 corrected records pass deterministic
validation. The result is 207 studies, one excluded paper, and one correction
notice.

The PDF stage converted 67 local files. Identity checks excluded one earlier
article version and one preprint duplicate, which left 64 new publications.
All 64 corrected records pass the same source-review and deterministic gates.
The ontology did not change.

The combined graph contains 273 publications, 271 studies, 20,493 typed items,
2,617 findings, 1,201 limitations, and 124 products.

The earlier project-folder match was not trusted as the final project link. A
separate strong-model linkage pass received each paper and every project that
passed the hard year rule. It could use authorship as evidence, but not as a
rule. An independent audit checked the 260 nominated paper-project pairs. The
trusted graph contains 307 accepted links. This total includes 65 direct grant,
acknowledgement, or exact-title links for the PDF publications. Fourteen
historical possible links remain outside the trusted graph.

## Model and source roles

- Deterministic code parses JATS metadata and loads the graph. No AI model is
  used for these steps.
- One isolated Opus call produced each version-0.13 draft.
- A fresh isolated Opus call reviewed the full source and returned each complete
  corrected record. Review returned 7 PASS, 202 MINOR, 0 MAJOR, and 846
  corrections for JATS. The PDF tranche returned 2 PASS, 62 MINOR, 0 MAJOR,
  and 261 corrections.
- Deterministic validation rejects an invalid corrected record before
  normalization or loading.
- PDF bibliography extraction is separate from semantic paper extraction. The
  evidence agent must not reconstruct a long reference list.

## Current boundary

- The completed 273-publication version-0.13 result remains the audited
  development baseline.
- The current local database uses the strict funded-project scope. It contains
  797 publications and 798 studies. Direct EQ relevance alone is not
  sufficient.
- The person and project-leader layer has 297 leaders, 125 observed members,
  and 106 people in both groups. Unsafe aggregates remain unavailable; they do
  not trigger ontology growth.
- OpenAlex matched 791 of 797 publications exactly. Six records retain manual
  lookup routes. Citation counts are dated snapshots.
- PDF reference lists remain outside the graph. Their parsing and
  deduplication are a separate deterministic task, not an AI extraction task.
- The 3,148-paper set is historical and does not control retrieval. The
  corrected 1,679-record queue controlled scale full-text assessment. Of 1,607
  verified papers, 797 are included and 810 are excluded. The 72 papers without
  verified full text remain unassessed.
- The 20-paper single-agent pilot matched every reviewed eligibility decision
  and project link. The final SQL-interface pilot then saved five valid Opus
  records and five valid Sol records. New scale tranches use one model call and
  an isolated SQLite workspace with `sql`, `submit`, and `reject`.
- Full-text processing and database loading are complete. The expanded graph
  contains 797 publications, 798 studies, 54,002 typed evidence items, and 642
  confirmed paper-project links. The private and public databases pass the
  release checks.
- The held identity queue can add a separate deduplicated discovery tranche.
- The application reads a deterministic, sanitized SQLite database built from
  the audited graph. Source files, filesystem paths, unresolved references,
  possible project links, and audit reasoning stay private.
- The release registry maps all 13,581 public scientific uses to 3,311 global
  canonical identities. Exact source labels remain paper-level evidence.
