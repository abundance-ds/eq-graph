# Production decision

Status update, 2026-08-20: the source-verification and linkage decisions remain
current. Approval for broad researcher-facing aggregation is withdrawn until
the analytical and serving layers pass the 100-question aggregate-validity
test.

The version-3 analytical classification is superseded by
`pilot/ontology-development-v4/`. Keep this file for the source, audit,
linkage, citation, and version-1 database decisions.

## Decision

The audited source facts and project links remain approved. The current
normalized categories and serving database are not approved for broad
aggregate claims.

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
| Aggregate validity | 150 reviewer-question runs: 37 pass, 36 partial, 26 fail, 51 not testable |
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

Repair the analytical classification and serving projection before PDF graph
loading or broad aggregate release. Keep source extraction and parser work
separate from this gate.
