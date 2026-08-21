# Current research work plan

Status date: 2026-08-21.

This file states the current work-package status and ordered research tasks.
It does not specify website design. Application implementation is recorded in
`web/README.md` and the repository log.

## Research boundary

Two discovery routes supply different stages of evidence:

```text
PROJECT-FIRST LOCAL CORPUS                 LITERATURE-FIRST SCALE CORPUS
1,024 funded projects                      author and funder searches
  -> 305 discovery matches                   -> 18,348 screened abstracts
  -> 287 held full texts                     -> 3,148 retained records
  -> 209 unique JATS papers                  -> full-text retrieval not started
  -> 207 audited studies
```

The 209-paper project-first corpus is not the full 3,148-record scale corpus.
The 305 project-first matches were discovery results, not full-text inclusion
decisions.

## Work-package status

| WP | Output | Current state | Next gate |
|---|---|---|---|
| 1. Paper identification | Final records for full-text retrieval | The frozen screen retained 3,148 of 18,348 records. | Independent human sample check and held identity queue. |
| 2. Full-text retrieval | Lawfully obtained full texts with source and licence records | The project-first route holds 287 full texts. Scale retrieval is zero. | Process the local PDF set, then approve a scale retrieval plan. |
| 3. Full-text processing | Source-verified study evidence and project links | Complete for 209 local JATS publications: 207 studies, one exclusion, one correction notice. | Add 60 local PDF-only papers with the same audit gates. |
| 4. Research data service | Audited graph and safe research-query derivative | The version-0.13 corrected-record run, version-2 database, and shared preview are complete for all 209 records. | Run the full 100-question aggregate-validity test and focused version-0.14 gap work. |

## Completed research foundation

- Ontology version 3 used 100 design papers and 100 questions. Its 209-paper
  graph remains the source-audited version-1 baseline, not the final analytical
  model.
- The typed reset used four rounds and 60 diverse papers. Version 0.5 matched
  59 of 60 source-adjudicated families in a blind run and found no missing
  record, key, controlled value, or gap.
- The first typed production calibration used 20 unseen publications. Final
  records pass 20/20 deterministic checks, and the source-checked repairs pass
  16/16. Registry normalization resolves 220 uses and keeps five ambiguous
  labels unmapped.
- A second test used 20 different publications and 21 studies. Final records
  pass 20/20 deterministic checks and all repaired records pass source review.
  Corrected normalization resolves 287 uses and keeps two vague labels unmapped.
- A later cross-audit found that software use was absent. The first rebuild was
  stopped and invalidated. Versions 0.6 to 0.8 add software use, optional parts
  for simple studies, whole-study relations, exact review-flow stages, and one
  experimental-design software function.
- A live audit then found that experimental-design algorithms had no exact
  method role. The version-0.8 restart was stopped after five records. Version
  0.9 adds that role. Four difficult DCE-design papers then had zero MAJOR
  source defects and no new ontology gap.
- The version-0.9 rebuild stopped after 48 records when independent one-paper
  audits found repeated sample-flow gaps. Version 0.10 added three general
  stages. Version 0.11 added general clinical-event and health-service-use
  outcome families after corpus-wide evidence and direct source tests.
- Two fresh eight-paper tests checked the correction. The first raw set had
  three MAJOR errors that focused repair removed. The second raw set had zero
  MAJOR, two PASS, and six MINOR source verdicts.
- The completed version-0.13 run has 209 valid corrected records: 207 studies,
  one correction notice, and one excluded paper. The records contain 15,430
  typed items, 1,951 findings, 939 limitations, 96 products, 188 source
  conflicts, and 210 explicit gaps.
- Each paper used one Opus draft and one fresh Opus source review. Draft review
  returned 7 PASS, 202 MINOR, 0 MAJOR, and 846 corrections. Deterministic code
  validates each corrected record before normalization or loading.
- The version-1 full-source audit checked all 207 included records. It passed 121
  unchanged, corrected 86, and left no unresolved material issue.
- Project linkage compared each paper with all date-eligible projects. The
  final result has 242 accepted links. Fourteen possible links remain
  non-materialized assessments.
- The version-1 local graph contains 17,650 nodes, 26,143 relationships, 7,030
  semantic facts, 871 findings, 602 limitations, and 191 source conflicts.
- SQLite integrity, foreign-key, graph-structure, exact-domain, and linkage
  checks pass.

## Ordered next work

### 1. Package and validate the version-2 preview

1. Keep the current 209-paper database unchanged as version 1.
2. Package the 209 valid version-0.13 corrected records in a separate version-2
   SQLite database and shared preview.
3. Run integrity, provenance, registry, and corpus checks on the packaged data.
4. Rerun all 100 aggregate questions. Do not infer a pass from record validity.
5. Complete focused version-0.14 work on recurrent explicit gaps.
6. Treat the shared preview as a review release. Approve the final analytical
   release only after the aggregate-validity and gap gates.

### 2. Local PDF input

1. Use `scripts/pdf_markdown.py` version 3 for canonical PDF Markdown. It repairs
   verified font maps before one PyMuPDF4LLM structural pass.
2. Do not run a second table parser. Tables, headings, prose, formula text, and
   source-page markers are in the same output.
3. Convert the 60 pending PDF-only papers in small tranches.
4. Run the same assessment, extraction, source audit, project linkage, graph
   loading, and integrity checks used for the JATS corpus.

### 3. Scale-retrieval readiness

1. Complete an independent human sample check of retained and excluded
   screening decisions.
2. Resolve the 94 held people and 76 additional profile suggestions.
3. Add and screen only genuinely new records from newly accepted profiles. Do
   not rerun the frozen 18,348-record screen.
4. Freeze the final retained set.

### 4. Lawful scale retrieval

Before retrieval, record:

- source order and lawful access method;
- licence and storage rules;
- DOI and PMID identity checks;
- PDF and JATS handling;
- unavailable-paper status;
- expected cost, rate limits, and tranche size.

Keep unavailable papers unassessed. Do not infer full-text evidence from an
abstract.

### 5. Processing each new tranche

```text
source file
  -> deterministic identity, metadata, and text preparation
  -> one Opus full-text assessment and conditional draft extraction
  -> one fresh Opus full-source review and correction
  -> separate project-link assessment across all date-eligible projects
  -> deterministic normalization and graph loading
  -> integrity, provenance, and competency-question tests
```

Project year is a hard exclusion rule. Author overlap is evidence for the AI
reviewer, not a deterministic link rule. Only accepted links create trusted
support or output relationships.

## Change rules

- Do not redesign the ontology for one unusual paper.
- Add a distinction only after repeated structural failure or a clear user
  question that the current model cannot represent.
- Preserve exact source terms before normalization.
- Keep findings aggregate and source-faithful. Record limitations, data-quality
  caveats, and source conflicts.
- Keep possible project links outside the trusted graph.
- Keep citation identity separate from study evidence. Share a cited
  publication only when a DOI or PMID identifies it.
- Do not make the semantic extraction call reconstruct a PDF bibliography.

## Decision points

Aggregate validity and focused version-0.14 gap work are the active graph gates.
Human input is required if:

- the six-paper PDF extraction pilot finds a material source error;
- a repeated paper type cannot fit the current ontology;
- project-link evidence requires a new policy;
- retrieval changes legal, access, or material cost constraints;
- the independent human screening check finds a material scope problem.

## Governing records

- Method: [`METHOD_SIMPLE.md`](METHOD_SIMPLE.md)
- Discovery-route boundary: [`PIPELINE_RECAP.md`](PIPELINE_RECAP.md)
- Provenance: [`PROVENANCE.md`](PROVENANCE.md)
- Scale pause and restart order:
  [`../scale/protocol-2.0/PAUSE_2026-08-05.md`](../scale/protocol-2.0/PAUSE_2026-08-05.md)
- Current ontology candidate:
  [`../pilot/ontology-development-v4/ONTOLOGY.md`](../pilot/ontology-development-v4/ONTOLOGY.md)
- Current production decision:
  [`../pilot/ontology-development-v4/production/DECISION.md`](../pilot/ontology-development-v4/production/DECISION.md)
- Historical version-1 production decision:
  [`../pilot/ontology-development-v3/production-calibration/DECISION.md`](../pilot/ontology-development-v3/production-calibration/DECISION.md)
- Audited corpus result:
  [`../pilot/ontology-development-v3/production-calibration/GRAPH_CORPUS_REPORT.md`](../pilot/ontology-development-v3/production-calibration/GRAPH_CORPUS_REPORT.md)
