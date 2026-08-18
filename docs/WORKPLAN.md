# Current research work plan

Status date: 2026-08-18.

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

The 209-paper graph is not the full 3,148-record corpus. The 305 project-first
matches were discovery results, not full-text inclusion decisions.

## Work-package status

| WP | Output | Current state | Next gate |
|---|---|---|---|
| 1. Paper identification | Final records for full-text retrieval | The frozen screen retained 3,148 of 18,348 records. | Independent human sample check and held identity queue. |
| 2. Full-text retrieval | Lawfully obtained full texts with source and licence records | The project-first route holds 287 full texts. Scale retrieval is zero. | Process the local PDF set, then approve a scale retrieval plan. |
| 3. Full-text processing | Source-verified study evidence and project links | Complete for 209 local JATS publications: 207 studies, one exclusion, one correction notice. | Add 60 local PDF-only papers with the same audit gates. |
| 4. Research data service | Audited graph and safe research-query derivative | Typed SQLite graph and sanitized serving database are complete for the JATS corpus. | Rebuild after each accepted tranche and test question coverage. |

## Completed research foundation

- Ontology version 3 used 100 design papers, 100 competency questions, three
  independent proposals, synthesis, and an unseen holdout.
- One paper call combines full-text assessment and conditional draft
  extraction. Deterministic code handles structured metadata, validation,
  normalization, and graph loading.
- A strong full-source audit checked all 207 included records. It passed 121
  unchanged, corrected 86, and left no unresolved material issue.
- Project linkage compared each paper with all date-eligible projects. The
  final result has 242 accepted links. Fourteen possible links remain
  non-materialized assessments.
- The final local graph contains 17,650 nodes, 26,143 relationships, 7,030
  semantic facts, 871 findings, 602 limitations, and 191 source conflicts.
- SQLite integrity, foreign-key, graph-structure, exact-domain, and linkage
  checks pass.

## Ordered next work

### 1. Local PDF input

1. Select an established PDF parser only after it passes the six-paper text,
   symbol, section, and table checks.
2. Do not use `pdf-inspector` 1.15.0 as the default. It corrupted 304 meaningful
   minus or inequality signs in five of six test papers.
3. Convert the 60 local PDF-only papers.
4. Run the same assessment, extraction, source audit, project linkage, graph
   loading, and integrity checks used for the JATS corpus.

### 2. Scale-retrieval readiness

1. Complete an independent human sample check of retained and excluded
   screening decisions.
2. Resolve the 94 held people and 76 additional profile suggestions.
3. Add and screen only genuinely new records from newly accepted profiles. Do
   not rerun the frozen 18,348-record screen.
4. Freeze the final retained set.

### 3. Lawful scale retrieval

Before retrieval, record:

- source order and lawful access method;
- licence and storage rules;
- DOI and PMID identity checks;
- PDF and JATS handling;
- unavailable-paper status;
- expected cost, rate limits, and tranche size.

Keep unavailable papers unassessed. Do not infer full-text evidence from an
abstract.

### 4. Processing each new tranche

```text
source file
  -> deterministic identity, metadata, and text preparation
  -> one AI full-text assessment and conditional draft extraction
  -> mandatory strong full-source verification
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

No ontology decision is open now. Human input is required if:

- an established PDF parser does not pass the calibration;
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
- Current ontology and production decision:
  [`../pilot/ontology-development-v3/production-calibration/DECISION.md`](../pilot/ontology-development-v3/production-calibration/DECISION.md)
- Audited corpus result:
  [`../pilot/ontology-development-v3/production-calibration/GRAPH_CORPUS_REPORT.md`](../pilot/ontology-development-v3/production-calibration/GRAPH_CORPUS_REPORT.md)
