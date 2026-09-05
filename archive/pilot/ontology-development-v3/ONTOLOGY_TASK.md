# Independent ontology-proposal task

## Objective

Propose an ontology for EuroQol research. It must represent the important facts in the supplied paper summaries and support the supplied user questions.

Write one self-contained Markdown document. Do not write JSON, RDF, SQL, or implementation code.

## Design priority

Center the proposal on exact facts that users need to find and compare. Examples include:

- `valuation study` as a study type;
- `cTTO` as a valuation method;
- an exact statistical or valuation model;
- `EQ-5D-5L` as an instrument and version;
- a defined population and sample;
- an administration mode and language;
- a value set or other research product;
- a principal finding and its context.

Generic containers are useful only when their contents have clear meaning. Do not hide important distinctions under terms such as `component`, `method`, or `outcome` without a usable classification.

These examples are seed requirements, not a closed vocabulary. Create a class, relation, or controlled value only when the supplied summaries or questions support it. Otherwise, mark it as a proposed extension. Preserve source terms, aliases, provenance, and canonical labels as different information.

## Inputs

- 50 fixed paper summaries.
- 50 competency questions.
- Project purpose and experiment notes.

Do not read earlier ontology experiments, graph models, extraction schemas, or another agent's proposal.

## Required content

Explain, in plain language:

1. The purpose and scope of the ontology.
2. The main concepts and what each concept means to a EuroQol researcher.
3. The important relations between concepts.
4. The controlled classifications or exact value families that make search useful.
5. How the ontology represents populations, instruments, methods, analyses, products, outcomes, and findings at useful granularity.
6. How it separates a publication, a study, a funded project, and derived analytics.
7. How it supports the supplied questions, including questions that need data outside a paper. Classify each question as answerable from the supplied summaries, requiring external linked data, or unsupported by the available evidence. Do not invent missing facts.
8. Two or more complete example records from the supplied papers. Use only supplied facts, do not infer missing fields, and identify the source summary.
9. Important facts that remain free text, derived, optional, or outside scope.
10. Unresolved design choices and risks.

The proposal can use tables, lists, or small diagrams. Keep it readable. Do not force every paper into one study pattern. Study-family templates are optional views. Do not impose a template, class, or cardinality where the paper does not support it.

You can reuse terms from an established standard if they help. The use case controls the design. Identify reused terms and explain their benefit. Do not adopt a standard only because it exists.
