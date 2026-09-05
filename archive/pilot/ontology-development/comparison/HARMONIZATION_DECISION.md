# Decision: how should the ontology be organized?

Status: option A approved, 2026-08-16.

## Context

Three independent agent lineages developed ontologies from the same 30 papers.
They largely agree about the information that matters.
They disagree about the main structure used to organize that information.

For example, all three can describe a paper as:

- a validation study of EQ-5D-5L;
- adults with Graves' disease;
- longitudinal data;
- reliability and responsiveness assessment;
- stronger evidence for detecting deterioration than improvement;
- uncertainty about how one retest subgroup was defined.

The decision is how to organize information of this type across all papers.

## Option A: paper-first tags and short descriptions — recommended

Each paper is the main record.
It receives practical tags and short descriptions for its purpose, population, methods, concepts, outputs, results and limitations.
A complex paper can have a small number of paper-local components for different samples or analyses.

Benefits:

- closest to the intended meta-research use;
- easy for researchers to read;
- suitable for a relational database;
- less risk of an over-specific or deeply nested ontology.

Trade-off: some technical provenance is less explicit unless it is important for interpreting a result.

## Option B: measurement-pathway structure

The main structure follows information through a measurement process, for example:

`questionnaire answers -> score -> mapped utility -> QALYs -> cost-effectiveness result`

Benefits: very precise when a paper transforms one type of measurement into another.

Trade-off: it is more complex, is specific to measurement and health economics, and can make ordinary meta-research descriptions cumbersome.

## Option C: relationship-first structure

The main structure is a set of statements such as:

`paper evaluates instrument`, `paper compares methods`, or `paper reuses dataset`.

Benefits: flexible and good for connected evidence.

Trade-off: it can become graph-like, verbose and difficult to keep consistent across agents and papers.

## Recommendation

Choose option A.
Use a measurement path or evidence-reuse link only when it changes how a researcher must interpret the result.

For example, if a paper converts SF-12 answers into EQ-5D utilities and then uses those utilities to calculate QALYs, record only:

`SF-12 answers -> mapped EQ-5D utility -> QALYs`

This is what “the shortest material derivation chain” meant.
It does not mean that we record every analysis step or create claim-evidence triplets.

## Specific ask

Reply with **“Approve option A”** if you want the recommended paper-first approach.
Alternatively, select option B or C.

I will make the remaining detailed harmonization decisions from the paper evidence and bring the tested candidate back for review.

## Human record

Decision: option A, paper-first tags and short descriptions.

Amendment: paper-first does not mean shallow or generic.
The ontology is for EuroQol research discovery and synthesis, not for general research.
It must test useful domain detail for populations, instruments, versions, languages, administration, study-family-specific methods, statistical methods, findings, interpretation, implications and gaps.

Outcome: do not harmonize the version-1 lineages into a final ontology.
Run a controlled version-2 experiment with option A fixed and the clarified purpose frozen before development.
