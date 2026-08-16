# Independent harmonization task

## Objective

Create one concise, paper-first EuroQol research ontology and extraction guide from the three anonymous development records and their independent comparison.

The result must help researchers find relevant studies and understand what the studies did and found.
It must preserve useful EuroQol-specific detail without turning every reported fact into a field.

Do not concatenate the three candidates.
Resolve duplicate terms, broad labels, inconsistent boundaries, and redundant concepts.
Do not choose content by candidate count, document length, nesting depth, or a numerical score.
Use paper evidence and the effect on the focused user questions.

## Inputs

Read these files in full:

- `context/PURPOSE.md`
- `context/USER_QUESTIONS.md`
- `context/PROTOCOL.md`
- `context/PROBES.md`
- `comparison/COMPARISON.md`
- `candidates/candidate-1.md`
- `candidates/candidate-2.md`
- `candidates/candidate-3.md`
- `batches/batch-01.tsv` through `batches/batch-04.tsv`

The 40 manifest article files are available under `corpus/` for focused source checks.
Use them when a material decision needs paper evidence or when the comparison identifies a source conflict.

Do not use holdout papers, the Internet, Git history, external ontology guidance, a graph or database model, or a database-modeling skill.

## Decision rules

1. Keep the paper as the main record.
2. Add a paper-local component only when it prevents a false paper-level statement about a phase, sample, task, analysis, status, or product.
3. Keep a distinction structured when it changes useful retrieval, comparison, or interpretation and agents can extract it consistently.
4. Use controlled terms for stable cross-paper categories, repeatable structured facts for variable details, explicit relations for dependencies, and concise narrative for paper-specific context.
5. Keep exact named methods and instrument details when they matter. Do not replace them with labels such as `quantitative`, `psychometric`, or `regression`.
6. Do not make each named detail a class or a mandatory field.
7. Keep absent, not reported, unclear, conflicting, and not applicable separate.
8. Keep author statements, documented use or effect, and extractor inference separate.
9. Keep an author-reported gap separate from a corpus-derived gap.
10. Keep source conflicts and unclear procedures as extraction records with the competing statements. Do not silently repair them.

Resolve the comparison's open boundaries. In particular, decide:

- which study-family values remain separate and how broad method work is tagged;
- the strict roles of protocol as paper purpose, component status, and reusable product;
- whether paper-level mixed status is stored or derived;
- whether assessment class is explicit or derived from exact property and method purpose;
- how product development, evidence, governance, access, recommendation, use, effect, and implementation state remain independent;
- how evidence-overlap confidence is represented;
- where review search and screening details belong;
- how extraction quality checks improve source-conflict capture.

For each decision, state the paper or user-query consequence.
If the 40 papers do not decide an issue, use the simplest provisional choice that preserves information and state what future evidence could change it.
Leave a material alternative unresolved only when either choice changes user answers and no safe provisional choice exists.

## Candidate document

Write `output/CANDIDATE.md` as the proposed ontology and extraction guide.
It must be usable by a researcher and by a capable extraction agent without a large prompt or a fixed JSON schema.

Include:

- purpose and boundaries;
- the paper and paper-local component rule;
- the stable core distinctions and relations;
- controlled study-family terms with short boundary notes;
- instruments, versions, language, roles, administration, people and population roles;
- a common method-use pattern and only the family-specific profiles that the 40 papers justify;
- outcomes, derivation, comparisons, reuse and evidence lineage;
- products and independent state dimensions;
- principal findings, interpretation, limits, implications, documented use or effect, future work and gaps;
- source uncertainty and extraction quality rules;
- a short extraction workflow and the rule for structured detail versus narrative.

Use Markdown.
Do not provide JSON, a database schema, graph labels, SQL tables, a class hierarchy, or mandatory empty fields.
Avoid duplicate concepts and repeated guidance.

## Decision and validation record

Write `output/HARMONIZATION.md` with:

- a short result summary;
- a terminology crosswalk from all three candidates to the final terms;
- each material harmonization decision and its evidence;
- rejected or derived distinctions;
- a compact 40-paper backward-fit table, one row per manifest paper;
- a check of all 27 focused user questions;
- a check of all 14 frozen probes against the final candidate;
- unresolved or provisional decisions and their concrete consequence;
- focused source checks and comparison limitations;
- a run note with every input read and each mechanical issue.

The backward-fit table is a validation record, not a new full extraction.
For each paper, state whether the candidate fits naturally and name only the decisive specialized distinctions or any remaining ambiguity.

## Stop condition

Write both output files only after the candidate supports all 40 applications and the frozen probes without an unrecorded forced fit.
If a material alternative cannot receive a safe provisional decision, record it clearly in `HARMONIZATION.md`; do not hide it in general prose.
Make no commit.
