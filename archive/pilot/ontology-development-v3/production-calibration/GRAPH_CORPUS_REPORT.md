# EuroQol research graph: audited corpus result

## Decision

The source-linked SQLite graph is complete and audited for the current
209-paper local JATS set. It is not approved for broad researcher-facing
aggregation. A later 100-question test found repeated defects in identity,
classification, relationship roles, missingness, and the serving projection.
The superseded 100-question test synthesis remains in Git history at `pilot/ontology-development-v3/aggregate-validity/SYNTHESIS.md`.

The low-cost first AI pass is not approved for unattended production. Every included record needs a strong source-verification pass before trusted graph loading.

## Process in one view

```text
100 questions + 100 diverse papers
  -> three independent ontology proposals
  -> comparison and synthesis
  -> ten-paper holdout
  -> concise typed graph

JATS metadata --------------------------> deterministic graph facts
full text -> one AI filter/extract call -> draft semantic facts
draft + full text ----------------------> independent source verification
paper + all date-eligible projects ----> separate project-link assessment
audited facts and accepted links ------> typed SQLite graph
```

The process started with real EuroQol questions and papers. It did not start with a general paper standard or a large fixed JSON schema.

## Graph center

```text
Person --AUTHORED--> Publication --REPORTS_STUDY--> Study
Project --HAS_OUTPUT------------------------------> Publication
Project --SUPPORTS_STUDY--------------------------> Study
Project --SUPPORTS_PUBLICATION--------------------> Publication
Project --SUPPORTS_PERSON-------------------------> Person
Project --SUPPORTS_DATASET------------------------> Dataset use

Study --HAS_STUDY_TYPE--> valuation study
      --USES_INSTRUMENT--> Instrument use --OF_INSTRUMENT--> EQ-5D-5L
      --USES_METHOD------> Method use -----OF_METHOD-------> cTTO
      --ANALYZED_WITH----> Model use ------OF_MODEL-------> hybrid model
      --PRODUCES---------> Research product
      --REPORTS_FINDING--> Finding
      --HAS_LIMITATION---> Limitation
      --CONCERNS---------> Concept
```

Shared nodes keep exact query values. Bound use nodes keep paper-specific roles, languages, versions, administration, perspectives, inputs, and qualifiers. Findings can link to outcomes, instruments, methods, models, and populations. Only aggregate study results enter the graph.

## Final corpus result

- Source publications: 209 unique local JATS papers.
- Included studies: 207.
- Excluded papers: 1.
- Publication-context notices: 1 correction.
- Flat semantic facts: 7,030.
- Controlled study types: 34.
- Instruments: 256.
- Methods: 472.
- Statistical models: 319.
- Principal findings: 871.
- Limitations: 602.
- Source conflicts: 191.
- Final graph: 17,650 nodes and 26,143 typed relationships.
- Deterministic JATS citation occurrences: 9,340. A total of 7,813 resolve by
  DOI, 95 resolve by PMID, and 1,432 remain paper-scoped and unresolved.
- Author edges: 1,250.
- Affiliation edges: 1,533.
- Relationships without a source locator: 0.

Database: `graph-neutral-209-run-02/euroqol-research-graph-citation-safe.sqlite`

SHA-256: `69eb1c76fa71ec4c7a51588cf9cc29a38438c77a5d9d3111d6d97348434dbf32`

SQLite integrity, foreign-key, graph-structure, exact-domain, and linkage tests pass.

## Semantic source audit

All 207 included study records received an independent full-article audit with `gpt-5.6-sol` at `xhigh` reasoning effort.

- Passed without a material change: 121.
- Records with at least one material issue: 86.
- Corrected: 86.
- Unresolved material issues: 0.

This is a record-level gate, not a fact-level error rate. One wrong stage label, value direction, denominator, administration detail, or omitted source conflict causes the full record to fail. The correction log contains one entry for each affected paper.

The result is clear: the first-pass model is useful for drafting but is not publication-safe without strong source verification.

## Project linkage audit

Each paper was compared with all date-eligible projects. Project year was a hard rule. Author and project-lead overlap was evidence for the AI reviewer, not a deterministic rule.

- Candidate pairs independently audited: 260.
- Final accepted links: 242.
- Final possible links: 14.
- Unresolved graph targets: 0.
- Accepted project-output edges: 209.
- Accepted support edges: 185 study, 34 dataset, 18 person, and 3 publication.
- Accepted output-only links without a support target: 2.

Only accepted judgments create trusted support or output edges. Possible judgments remain reviewable assessment nodes.

## Exact-domain check

The Moroccan EQ-5D-5L value-set paper resolves to:

- study type: valuation study;
- instruments: EQ-5D-5L and EQ VAS;
- methods: cTTO and DCE;
- models: conditional logit, heteroskedastic censored Tobit, and hybrid heteroskedastic Tobit;
- products: Moroccan EQ-5D-5L value set and scoring algorithm.

The graph also resolves flexible concepts such as `states worse than dead` to one shared query node.

## Input decisions

JATS remains the canonical source for bibliographic metadata, authors, affiliations, correspondence, funding, dates, and references. Deterministic code loads these fields before AI semantic extraction.

Citations are not part of the trusted study-evidence layer. The graph shares a
cited publication only when a DOI or PMID supports that identity. It does not
merge unidentified references by title. The `corpus_publication` view keeps
external cited works out of corpus counts.

Do not use `pdf-inspector` 1.15.0 as the default PDF parser. In the six-paper test, it silently corrupted 304 meaningful minus or inequality signs in five papers. The current converter remains the default.

## Question coverage

All 100 competency questions shaped the ontology and validation probes. The current graph can represent their paper, study, method, instrument, result, concept, person, project, and provenance dependencies.

The database cannot yet answer every question completely. Corpus-wide, portfolio-wide, external citation, registry, and identity questions need inputs beyond the current 209 local papers.

## Known limits

- The graph covers 209 current local JATS publications, not all 3,148 retained screen records.
- Lawful scale full-text retrieval has not started.
- Sixty local PDF-only papers remain to process with the retained converter and the same audit gate.
- Names without ORCID are not merged across publications.
- Ninety project leads remain unresolved, and five projects lack a start year.
- Affiliations keep exact JATS strings and are not fully institution-normalized.
- Possible project links do not enter the trusted support or output graph.
- PDF reference lists are not an AI semantic-extraction task. Citation coverage
  for PDF-only papers remains pending a dedicated parser decision.
- A false-negative project link remains possible when the paper and project record do not give enough evidence.

## Next actions

The public service uses a deterministic, sanitized SQLite derivative of this
audited graph. Broad aggregate answers remain paused until the analytical and
serving layers pass the 100-question test.

1. Repair the repeated aggregate-validity failures and rerun all 100 questions.
2. Process the 60 local PDF-only papers only after the repaired analytical
   model is stable.
3. Complete the independent human screening check and resolve the held identity
   queue before scale retrieval.
4. Plan lawful full-text retrieval for the final retained set.
5. Repeat extraction, source audit, project linkage, deterministic loading, and
   integrity tests for each new full-text tranche.
