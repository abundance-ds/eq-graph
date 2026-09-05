# Historical build record

This record summarizes the main development stages. Newest entries appear first.
The current method, results, and release records govern the project. See
[HISTORY.md](../docs/HISTORY.md) for the concise project timeline.

## 2026-08-31 — Chat visualization system

- Integrated statistical charts into the research chat interface.
- Added stat, bar, line, area, scatter, histogram, heat-map, donut, network, and table views.
- Centralized chart validation, presentation, responsive layout, and result limits.

## 2026-08-29 — First public data release

- Froze ontology 0.13 and the 797-publication research database.
- Built and validated the sanitized public database.
- Recorded release counts, file hashes, and validation results in
  [DATA_RELEASE.md](../docs/DATA_RELEASE.md).
- Added the technical ontology view to the project website.

## 2026-08-27 — Full-text processing and graph build

- Completed assessment of 1,607 verified full texts: 797 included and 810 excluded.
- Loaded 798 studies, 54,002 typed evidence items, 642 confirmed project links,
  5,845 findings, 3,666 limitations, and 489 products.
- Built the private research database and its sanitized public derivative.
- Validated integrity, foreign keys, controlled values, project years, identities,
  and public-field exclusions.
- Tested 100 competency questions: 54 passed, 36 were partial, 6 failed, and 4
  were not testable with the available data.

See [FULLTEXT_PROCESSING_RESULT.md](docs/results/FULLTEXT_PROCESSING_RESULT.md).

## 2026-08-26 — Full-text retrieval and scope review

- Completed the manual review stage for the full-text retrieval queue.
- Verified 1,607 full texts and recorded 72 unavailable or excluded records.
- Applied a bounded title-based scope check to 36 clearly unrelated records whose
  screening evidence did not establish a funding link.
- Prepared all verified sources for full-text assessment.
- Recorded PDF repair, fallback conversion, and source-verification results.

See [FULLTEXT_RETRIEVAL_RESULT.md](docs/results/FULLTEXT_RETRIEVAL_RESULT.md),
[FULLTEXT_PREPARATION_RESULT.md](docs/results/FULLTEXT_PREPARATION_RESULT.md), and
[SCOPE_SCREEN_RESULT.md](docs/results/SCOPE_SCREEN_RESULT.md).

## 2026-08-24 — Corrected abstract screen

- Assessed 18,348 usable abstracts against the funded-project scope.
- Routed 1,679 publications to full-text retrieval and excluded 16,669.
- Applied a 10-year project lookback to the final 559 records.
- Completed a 20-paper full-text calibration with no eligibility changes after review.
- Rebuilt the reviewed identity registry and prepared 1,153 verified sources available
  at that stage.

See [ABSTRACT_SCREEN_RESULT.md](docs/results/ABSTRACT_SCREEN_RESULT.md).

## 2026-08-23 — Scope correction

- Required verified full-text evidence of EuroQol support or an accepted funded-project
  link for final inclusion.
- Retained the earlier topic screen only as historical evidence.
- Validated the corrected abstract screen on a 50-record calibration set.
- Excluded three corrupt source records with incorrect DOI assignments.

See [2026-08-24-scope-repair-plan.md](docs/2026-08-24-scope-repair-plan.md).

## 2026-08-22 — Scale eligibility pilot

- Completed a 40-paper full-text eligibility pilot with retained, boundary, and exclusion
  cases.
- Added 64 source-reviewed PDF publications without changing ontology 0.13.
- Rebuilt the research and serving databases with 273 publications and 271 studies.
- Repeated the 100-question competency assessment.

See [fulltext-pilot-v1](scale/protocol-2.0/fulltext-pilot-v1/).

## 2026-08-21 — Release validation

- Tested all competency questions against the version-2 release.
- Identified limits in identity, study-type, method-role, working-group, affiliation,
  and product aggregation.
- Completed source review for 209 JATS publications and corrected all recorded issues.
- Confirmed ontology 0.13 for the next production stage.

## 2026-08-20 — Ontology 0.13 development

- Replaced the earlier analytical classification with a typed research ontology.
- Used four development rounds, source review, and independent calibration sets.
- Added explicit sample-flow stages and general outcome families after repeated evidence
  gaps appeared.
- Completed two 20-publication production calibrations and corrected all major findings.

See [production decision](pilot/ontology-development-v4/production/DECISION.md).

## 2026-08-18 — Integrated graph and interface

- Replaced interface fixtures with a deterministic SQLite serving database.
- Connected the narrative, graph, and query interface to the serving data.
- Completed source review for 207 included records and corrected 86 records.
- Confirmed 242 accepted project links and retained 14 possible links outside the trusted
  graph.

See [pipeline recap](docs/2026-08-27-pipeline-recap.md).

## 2026-08-17 — Web research interface

- Added the shared website preview workflow.
- Integrated the research narrative, read-only query interface, and graph views.
- Added query authorization, streamed-answer formatting, and chart interactions.

## 2026-08-16 — Comparative ontology development

- Completed three independent ontology lineages over shared development papers.
- Compared the proposals anonymously and selected the paper-first architecture.
- Tested method granularity and applied the combined model to an unseen holdout set.
- Retained the complete experiment records under the archived ontology directories.

See [ontology version 1](pilot/ontology-development/) and
[ontology version 2](pilot/ontology-development-v2/).

## 2026-08-05 — Scale screening and audits

- Completed the initial 18,348-record topic screen.
- Performed two blinded 100-record exclusion audits with no confirmed false exclusion.
- Recorded the limits of the topic-based scope before full-text retrieval.

See [topic-screen results](docs/2026-08-05-topic-screen-and-pilot-results.md) and
[archived scale records](scale/protocol-2.0/).

## 2026-08-04 — Source integration

- Added provenance records for source data, transformations, prompts, validation, and
  known limits.
- Replaced lexical project ranking with complete time-eligible project comparison.
- Added binary identity review for selected author profiles.
- Combined OpenAlex, ORCID, PubMed, and funding sources into 28,600 deduplicated records.
- Prepared the 18,348-record screening input.

## 2026-08-03 — Protocol 2.0 pilot

- Completed the 10-person discovery and screening pilot.
- Evaluated abstract availability, full-text retrieval, funding evidence, and project links.
- Confirmed that final funding decisions require full-text evidence.
- Defined the scale conditions for profile review, retrieval coverage, and independent
  validation.

## 2026-07-30 — Pipeline integration

- Combined the project-first and literature-first discovery routes.
- Defined a shared typed-evidence model and a staged screening method.
- Added the canonical 1,024-project table with project years and approved budgets.
- Tested a broad pre-filter against known project-publication links.

See [method draft](docs/2026-07-30-method-draft.md).

## 2026-07-29 — Publication discovery

- Completed author and funder publication retrieval.
- Built a 46,620-publication discovery set.
- Added grant-identifier, funder, title, and author evidence for project matching.
- Recorded identity cases that required manual review.

See [pipeline assessment](docs/2026-07-29-grant-mining-pipeline-assessment.md) and
[pipeline architecture](docs/2026-07-29-scrape-pipeline.md).

## 2026-07-28 — Project setup

- Reviewed the initial project and graph data.
- Normalized project-leader names and current EuroQol member records.
- Established reproducible discovery stages and one recorded output per stage.
- Added identity safeguards for ambiguous names and incomplete author identifiers.
