# Typed EuroQol research ontology

Version 0.13, adopted for release `beta-2026-08-29` after 60 development studies and two 20-publication calibration batches.
It governs the 797-publication graph.

This is the compact domain reference, not the system prompt. Exact controlled
values are in [`VOCABULARY.tsv`](VOCABULARY.tsv). Decision evidence is in the
round review files.

## Domain map

```text
Project ──supports──> Study <──reports── Publication
                         │
                         ├── StudyPart ──uses──> DataAsset
                         ├── Population ──has──> Sample
                         ├── InstrumentUse ──of──> Instrument
                         ├── MethodUse ─────of──> Method
                         ├── ProtocolUse ───of──> Protocol
                         ├── ModelUse ──────of──> Model
                         ├── SoftwareUse ───of──> Software
                         ├── ProductUse ────of──> Product
                         ├── ScoringUse ───uses─> Product
                         ├── TaskDesign
                         ├── StudyFactor
                         ├── Administration
                         ├── StakeholderInvolvement
                         ├── Outcome ──has──> Finding ──supports──> Interpretation
                         ├── Limitation
                         ├── Product ──has──> ProductStateAssertion
                         ├── Concept
                         ├── Gap
                         └── SourceConflict

Publication ──has──> PublicationStatusAssertion
Publication ──corrects/retracts──> Publication
```

## Information types

| Type | Rule |
|---|---|
| Controlled | Use one exact value from `VOCABULARY.tsv` or a gap state. |
| Registry | Preserve the exact source label; map aliases to one reviewed identity. |
| Open | Preserve source-faithful text for populations, concepts, findings, interpretations, and limitations. |
| Provenance | Give a source file and section, table, figure, or paragraph locator. |

The paper-level extraction call queries the current registry and maps an exact
identity when one exists. If a source contains a genuinely new identity, the
call must add it explicitly after it checks the existing identities. A new key
or controlled value remains a `Gap`. The frozen release does not accept silent
schema or vocabulary changes.

A registry match is an exact identity match. A base instrument is not an alias
for a language, respondent, level, or experimental version. Reviewed variant
identities can link to a parent identity.

The `submit` validator checks registry use, controlled values, relations, and
required fields. It returns specific errors to the same extraction call for
correction. Deterministic release validation then checks the complete database.

## Core rules

- Each mapped `Study` has exactly one `primary_research_family`.
- Purposes are ranked and can be multiple. A purpose must be a stated
  scientific aim or principal output, not a procedure or discussion topic.
- Design, time, allocation, data origin, publication form, and status are
  separate axes.
- Create a `StudyPart` only for a separable sample, data source, method, or
  state. A simple study can have no parts. Keep parts flat. Do not create one
  for every analysis.
- Create one `DataUse` for each data source. Never use a mixed-origin value.
- A study-wide `DataUse` can have no part link. Keep it part-scoped when its
  origin, level, or analytic use differs by part.
- Use `Sample` for source-reported counts at exact flow stages. Use
  `IDENTIFIED`, `SCREENED`, and `ELIGIBLE` for general flow. Evidence reviews
  can use the more exact `IDENTIFIED_RECORDS`, `FULL_TEXT_ASSESSED`, and
  `INCLUDED_EVIDENCE` stages.
- Registry names for instruments, methods, protocols, models, software,
  products, languages, and places are not schema enums.
- Each scientific use has one context and one type-specific function. Use a
  part link when the use is confined to that part. Leave the part link empty
  when the use governs the whole study or spans all parts. Create another use
  when the context or function changes.
- Keep task randomization in `TaskDesign`. Use study allocation only for
  assignment of people or study units.
- Use `StudyFactor` only for an analysed condition, determinant, comparator,
  stratifier, modifier, or stage. Keep its exact name and levels open.
- Keep task profiles, health-state descriptions, and reference points in
  `TaskDesign`, not `StudyFactor`.
- Use `StakeholderInvolvement` only when the source reports an activity and its
  influence. Ordinary participation is not involvement.
- Use part-level `PARTICIPATORY_DESIGN` when joint creation or refinement is
  the defining process. Keep collection and analysis methods separate.
- Publication, study, result, and product states are separate and source-dated.
- Extract selected principal findings, not every coefficient or table cell.
- Extract only source-reported limitations.
- Concepts support discovery. They do not replace exact instruments, methods,
  populations, factors, or purposes.

## Primary-family boundaries

The family classifies the `Study`, not the `Publication`. For a protocol
article, use the planned study aim and intended main result. Keep publication
form and study status on their separate axes.

Select the first row that describes the study's principal scientific
contribution. A mentioned method, product, or secondary analysis is not enough.

| Order | Principal contribution | Family |
|---:|---|---|
| 1 | Systematic identification and combination of prior evidence | `EVIDENCE_SYNTHESIS` |
| 2 | Comparison of costs and health consequences for a decision | `HEALTH_ECONOMIC_EVALUATION` |
| 3 | Attributable economic burden without decision alternatives | `ECONOMIC_BURDEN_RESEARCH` |
| 4 | Taxonomy, definition, framework, or conceptual classification | `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` |
| 5 | New or revised value set or scoring system | `VALUE_SET_DEVELOPMENT` |
| 6 | New, revised, translated, or adapted instrument content | `INSTRUMENT_VERSION_DEVELOPMENT` |
| 7 | Norms or reference data stated as a main aim or output | `POPULATION_REFERENCE_DESCRIPTION` |
| 8 | Use, provision, workflow, implementation, prediction support, or decision support | `APPLIED_USE_RESEARCH` |
| 9 | Measurement performance without new instrument content as a principal output | `MEASUREMENT_PROPERTY_EVALUATION` |
| 10 | Approach, method, or protocol selection, reliability, assumptions, performance, feasibility, or quality | `METHODS_RESEARCH` |
| 11 | Empirical health-preference patterns or differences | `HEALTH_PREFERENCE_RESEARCH` |
| 12 | Health, HRQoL, well-being, or health-behavior outcomes | `HEALTH_OUTCOME_RESEARCH` |

Use a gap when the stated aim, main decision, principal output, and conclusion
do not support one row. Do not add an `OTHER` family.

## Uses and administration

`InstrumentUse`, `MethodUse`, `ProtocolUse`, `ModelUse`, `SoftwareUse`, and
`ProductUse` each link one exact registry identity to one study part, context,
function, and evidence locator. `ModelUse` also has an analytic role. Software
is separate from the method, protocol, model, or product that it implements.

`ProductUse` represents a previously existing reusable product that the
current study examines, compares, or synthesizes. It does not represent an
output that the current study creates. It maps to a registry Product identity,
not to a local current-study Product item. `ScoringUse` links instrument
responses to an exact value-set or scoring product that the study applies.

Administration can record respondent, reporting or valuation perspective,
self/interviewer/assisted completion, assistance type, channel, setting,
instrument language, interview language, recall period, and time point.
Assisted self-completion remains self-report.

An Administration can apply to the instrument, method, protocol, software, or
task that shares those details. A finding, limitation, or concept can refer to
a whole Study when no narrower item is the correct object.

A study-level design value describes a study with no parts and is the default
for any parts. A part-specific value replaces that axis. The study or each
substantive part must have effective component, time, comparison, and
allocation values.

`TaskDesign` can record the exact task label, profiles, attributes, levels,
duration, alternatives, task count, block, order, randomization unit, and
stopping or indifference rule. Do not create one record per response.

## Findings, products, and status

A `Finding` has a short source-faithful statement and can contain selected
aggregate values: value, unit, denominator, time, subgroup, comparator,
direction, and uncertainty. Keep author interpretation separate.

A current-study `Product` is optional and must be an explicit reusable output.
Development, approval, validation, deployment, and withdrawal are independent
assertions. An assertion can identify who made it. Silence does not prove a
negative state.

A `PublicationStatusAssertion` records a reported editorial state. Retraction
does not change study execution, result availability, publication form, or
product validity.

Structured source data supplies DOI, title, abstract, authors, ORCID,
affiliations, dates, journal, licence, language, funding, references, URLs, and
related metadata before semantic extraction.

Use `CORRECTION_NOTICE` or `RETRACTION_NOTICE` only for the editorial notice.
A retracted research article keeps its research publication form and gets a
`RETRACTED` status assertion. Keep the notice-to-target relation separate.

## Gaps and aggregation

- `UNMAPPED_VALUE`: a controlled key exists, but no value fits.
- `UNMODELED_ASPECT`: an important fact has no key or relation.
- `UNCERTAIN_MAPPING`: more than one mapping remains plausible.
- `NOT_REPORTED`: a required fact is absent.

A source contradiction is a `SourceConflict`, not a gap. Keep both statements
and locators; do not repair them silently.

Every aggregate states its counting unit and denominator. Primary-family
counts use distinct studies and form one partition. Multi-value totals can
exceed the study count. Method and instrument counts filter by function and
context. Missing and uncertain values remain outside scientific categories.

## Development record

Four 15-paper rounds used independent applications, blind regression, and
source-checked review. Version 0.5 matched 59 of 60 source-adjudicated primary
families. Two unseen 20-publication batches then tested the production format.
A later independent source audit found that software use was absent even
though it occurs across the corpus. It also found a conflict between the
written part rule and a validator that forced placeholder parts. Version 0.6
added `SoftwareUse` and made `StudyPart` optional for a simple study. A fresh
production test then found that review-flow counts did not fit participant
sample stages. Version 0.7 added exact stages for identified records and full
texts assessed. A second fresh production test supported one software function
for experimental-design construction. Version 0.8 added that function. A live
audit then showed that the design algorithm itself also needs a method
function. Version 0.9 adds that matching function. Early version-0.9 source
audits then found repeated gaps for general sample identification, screening,
and eligibility counts. Version 0.10 adds these three general stages. Its
focused test also showed that clinical endpoints and health-service use were
forced into unrelated outcome families. Version 0.11 adds two general outcome
families. It does not change an entity, relation, research family, or
scientific-use function.

During the version-0.11 rebuild, an independent audit found that forward and
back translation had no exact method function. Five corpus papers directly
report that workflow, and 27 discuss cultural adaptation. Version 0.12 adds
one general instrument-translation-or-adaptation method function. This additive
enum change uses the governed `UNMAPPED_VALUE` repair route; it does not
invalidate unrelated version-0.11 drafts.

A later source audit found studies that examine the validity or obsolescence
of existing value sets. Version 0.13 adds `ProductUse` for an exact existing
product that is an analysis object, comparator, or evidence-synthesis target.
It keeps current-study outputs in `Product` and product application in
`ScoringUse`.
