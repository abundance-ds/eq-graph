# Production decision

## Decision

The ontology, typed SQLite model, and audited 209-paper JATS graph are approved for application integration and researcher review.

- Use one AI call per paper for full-text inclusion and conditional semantic extraction.
- Treat that output as a draft.
- Require a separate strong-model, full-source verification before trusted graph loading.
- Parse JATS publication metadata with deterministic code before semantic extraction.
- Keep extraction output as readable Markdown with a flat typed fact index.
- Normalize clear aliases and load the graph with deterministic code.
- Keep project linkage separate from paper extraction.
- Keep citations as a secondary provenance layer. Resolve shared cited works
  only with DOI or PMID evidence. Keep unidentified entries paper-scoped.
- Do not make the semantic extraction model reproduce PDF bibliographies.
- Compare each paper with all date-eligible projects.
- Apply project year as a hard rule. Use author overlap as review evidence only.
- Materialize only accepted project links. Keep possible links as assessments.
- Do not use separate routine AI agents for filtering, extraction, and normalization.
- Use SQLite for this stage. The application does not need Neo4j to answer the tested questions.

## Evidence

| Test | Result |
| --- | --- |
| Ontology development | 100 design papers, 100 competency questions, three independent proposals, synthesis, and ten-paper holdout |
| Current JATS corpus | 209 publications; 207 included studies; one exclusion; one correction notice |
| Independent semantic audit | 207/207 included records checked; 121 passed unchanged; 86 corrected; zero unresolved issues |
| Semantic index | 7,030 facts; 871 findings; 602 limitations; 191 source conflicts |
| Linkage audit | 260 pairs checked; 242 accepted; 14 possible; zero unresolved graph targets |
| Typed SQLite graph | 17,650 nodes and 26,143 relationships |
| Final checks | Structure, exact-domain, linkage, integrity, and foreign-key checks pass |
| PDF parser comparison | `pdf-inspector` failed: 304 meaningful signs corrupted in five of six papers |

## Model decision

Do not approve `gpt-5.6-luna` or another low-cost model for unattended publication use. The first pass is useful for drafting, but 86 of 207 included records needed at least one material correction during strong source verification.

This is a strict record-level result. It is not a statement that 42% of all facts were wrong. A single material issue fails a record. It does show that selective repair after automatic structure checks is not enough.

## Input decision

- JATS is the preferred source because it gives structured metadata and clean full text.
- PDF input must use the retained converter until another engine passes text and symbol checks.
- The 60 local PDF-only papers need the same semantic audit before graph loading.

## Scope

This decision applies to the current 209-paper local JATS set. It does not claim that the graph covers all 3,148 retained abstracts or answers all 100 questions completely.

No ontology decision is required before application integration or PDF processing. Stop for user review only if a new paper cannot fit the graph without a structural change, if project-link evidence requires a policy choice, or if a retrieval decision changes legal or cost constraints.
