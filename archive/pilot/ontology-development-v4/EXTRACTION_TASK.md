# Pilot ontology application task

This task creates a human-readable research record for ontology development.
It is not the production extraction prompt or production data format.

Read the supplied publication metadata, `ONTOLOGY.md`, `VOCABULARY.tsv`, and
full text. Assess the paper and apply the ontology. Do not create a new
ontology key, controlled value, or canonical identity.

Publication metadata has already been parsed from JATS or another structured
source. Use it as context. Do not reconstruct authors, DOI, journal, licence,
dates, affiliations, funding fields, or references from article prose.

## Rules

- Use exact canonical codes from the ontology for controlled fields.
- Keep the exact source label for each instrument, method, protocol, and model.
- Separate direct, observed, source-study, planned, and discussion-only uses.
- Separate purpose, design, time, data origin, publication form, and status.
- Create a `StudyPart` only when a part has its own sample, data source,
  methods, or status.
- Extract principal findings at the study-dependent depth in the ontology.
- Extract source-reported limitations. Do not invent limitations.
- Give a section, table, figure, or paragraph locator for each extracted item.
- Do not assess project linkage in this task.

## Gaps

If a controlled value does not fit, write `UNMAPPED_VALUE`. If an important
fact has no key, write `UNMODELED_ASPECT`. If two mappings are plausible, write
`UNCERTAIN_MAPPING`. If a required fact is absent, write `NOT_REPORTED`.

For each gap, state the affected key, source evidence, why it matters, and a
proposed resolution. Do not force a value.

## Pilot Markdown output

Use these headings:

1. `Assessment and classification`
2. `Study structure and typed uses`
3. `Findings, limitations, products, and concepts`
4. `Gaps and source conflicts`
5. `High-value canonical terms`

Do not fill a heading with `none`. State only supported facts or a required
gap.
