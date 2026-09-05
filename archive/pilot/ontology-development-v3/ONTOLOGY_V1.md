# EuroQol research ontology v1

## Purpose

This ontology supports search, comparison, and synthesis of EuroQol-supported
research. It describes what a study did, what it used, what it produced, what
it found, and what limits apply.

It is not a general ontology for all research. It is not a detailed graph of
every claim and coefficient.

## Human model

```text
Project --supports--> Study <--reported by-- Publication
                       |
                       +-- research purpose and study design
                       +-- population, sample, and input data
                       +-- exact instrument and its use
                       +-- administration details
                       +-- exact method, protocol, and task design
                       +-- analysis and statistical model
                       +-- outcome or measurement property
                       +-- research product and its status
                       +-- concepts and themes
                       +-- principal findings, interpretations, and limitations
```

The values are the corner pieces. A researcher can search directly for
`valuation study`, `EQ-5D-5L`, `cTTO`, `DCE`, `Egyptian Arabic`, `hybrid
heteroskedastic Tobit model`, or `states worse than dead`.

## Core records

| Record | What it means | Important content |
|---|---|---|
| `Project` | A funded EuroQol activity | project ID, title |
| `Project-publication link` | Evidence that support applies to an output | accepted or candidate, support type, evidence class, source locator |
| `Publication` | An identifiable output | DOI, title, authors, journal, dates, licence, lifecycle status |
| `Publication relation` | A link between outputs | corrects, retracts, updates, supplements, reports same study |
| `Study` | The investigation that a publication reports | title, completed or planned status, primary publication |
| `Study-publication link` | The role of an output for a study | primary report, protocol, secondary report |
| `Research purpose` | Why the work was done | valuation study, value-set development, implementation research |
| `Study design` | How the work was organized | national valuation survey, longitudinal cohort, systematic review |
| `Population` | The group to which the question applies | Moroccan adults; children with intellectual disability |
| `Sample` | The people or records that supplied data | recruited, completed, analytic, subgroup counts |
| `Input dataset or cohort` | A reused or combined source | register, trial cohort, survey, period, analytic contribution |
| `Instrument` | An exact measure, version, form, or language version | EQ-5D-5L; Chichewa PedsQL child self-report |
| `Instrument use` | What the study did with that instrument | valued, administered, analyzed, mapped, shown, used as predictor |
| `Administration` | How data or responses were collected | respondent, perspective, interaction, channel, setting, language |
| `Measurement time` | What a time expression refers to | report time, reference time, recall period, valuation duration |
| `Research method` | The exact procedure that generated research data | cTTO, DCE, cognitive interview, systematic review |
| `Protocol or task design` | Named protocol and important task detail | EQ-VT 2.6.1; ten cTTO tasks; feedback module |
| `Statistical model` | The exact model and its role | conditional logit; preferred hybrid heteroskedastic Tobit |
| `Derivation step` | A material transformation that changes meaning or uncertainty | median-to-mean conversion before random-effects pooling |
| `Outcome or property` | What was measured or evaluated | utility, responsiveness, content validity, usability |
| `Research product` | A reusable output | value set, instrument version, model, checklist, decision aid |
| `Concept or theme` | A flexible source-grounded discovery topic | states worse than dead; digital health; child health |
| `Finding` | A principal result needed to understand the contribution | pain/discomfort had the largest effect |
| `Interpretation` | What the authors think the result means | recommended for national economic evaluation |
| `Limitation` | A source-reported constraint | rural and low-literacy groups were under-represented |
| `Source conflict` | Two source statements that do not agree | abstract and Results give incompatible significance statements |
| `Review evidence unit` | One underlying unit in an evidence synthesis | source study, instrument, property, result, quality rating |

There is no generic `Component` record. A `Publication` is an output. A
`Study` is the investigation. A correction notice is a publication, but it is
not a second study.

## Controlled corner pieces

Use a preferred label and retain the exact source label. New source terms can
enter a review queue. Do not force an uncertain mapping.

### Research purpose and study design

A study can have several purposes and designs. Keep purpose and design
separate.

Common research purposes include:

- valuation study and value-set development;
- valuation-method or task-design research;
- mapping or crosswalk research;
- instrument or descriptive-system development;
- translation and cultural adaptation;
- measurement-property evaluation;
- content-validity and response-process research;
- population health and population norms;
- longitudinal or clinical outcomes;
- implementation and routine measurement;
- evidence synthesis;
- economic evaluation or utility application;
- qualitative or stakeholder research;
- methodological framework, protocol, or reporting guidance.

Common designs include national valuation survey, DCE experiment,
test-retest study, prospective cohort, retrospective linked-data cohort,
qualitative interview study, systematic review, meta-analysis, Delphi process,
and usability study.

`Valuation study` applies only when the study elicits preferences for health
states, dimensions, or levels. Applying an existing value set does not make a
clinical study a valuation study.

### Instruments and their use

Store the exact family, version, form, and language when reported. Instrument
name alone does not state what the study did.

Controlled use roles include:

- developed;
- translated or culturally adapted;
- administered to measure participant health;
- administered to describe the sample;
- valued;
- psychometrically evaluated;
- used as a comparator;
- used as a mapping source or target;
- scored with a named value set;
- used as a prediction input;
- used in a methodological example;
- shown for content or implementation evaluation;
- historical data reused, visualized, or displayed in decision support;
- evidence synthesized;
- discussed only.

The same instrument can have several roles. A role must not imply another
role. For example, `EQ-5D displayed in a decision aid` does not mean that the
study administered EQ-5D.

### Administration

Store these as independent facts:

- respondent;
- perspective;
- self-completed, interviewer-assisted, or interviewer-administered;
- paper, web, app, telephone, video, or face-to-face channel;
- setting;
- instrument and interview language;
- recall period;
- report time and repeated-measure schedule.

`cTTO` is a valuation method. `Video` is an administration channel. Do not
combine them into a new method label.

### Methods, protocols, and models

Store exact methods such as cTTO, conventional TTO, DCE, DCE with duration,
person trade-off, visual analogue scale, cognitive interview, think-aloud,
psychometric assessment, systematic review, and meta-analysis.

Store a named protocol and version when reported. Store task details only when
they distinguish the work or answer a user question.

Store each statistical model with its role: candidate, comparator, preferred,
final, or sensitivity analysis. Keep material qualifiers such as censoring,
heteroskedasticity, random effects, link function, mapping form, and anchor.

`Hybrid` is normally a statistical model or analysis that combines data. It is
not a valuation method.

### Concepts and themes

This is a flexible, multi-value discovery layer. Examples include:

- states worse than dead;
- child and adolescent health;
- proxy reporting and proxy perspective;
- digital health and remote measurement;
- respondent engagement;
- attribute non-attendance;
- health inequality;
- cultural adaptation and cross-cultural comparability;
- caregiver spillover;
- routine PROM implementation and clinical decision support.

A concept can overlap a structured fact when the overlap improves discovery.
It must not replace exact facts such as instrument, method, population, or
study type. Keep the source term when a preferred mapping is uncertain.

### Findings, interpretations, and limitations

Use study-dependent depth. Extract enough to explain the paper's contribution
and answer likely user questions. Do not use a fixed finding count.

For a valuation study, this usually includes:

- utility range or anchors;
- lowest and highest states when relevant;
- dimension order or relative importance;
- selected model and selection reason;
- important subgroup, null, or conflicting results;
- other findings that the authors emphasize.

For other study families, use the equivalent decision-relevant depth. Include
important aggregate estimates. Do not copy complete result tables or
participant-level values.

Keep direct results, author interpretations, and limitations distinct. Attach
a source section, table, figure, or paragraph locator. Keep source conflicts
visible.

## State and safety rules

- Mark a study as planned, in progress, completed, or not applicable.
- Mark products with their source-grounded state. Examples are proposed,
  developed, tested, internally validated, implemented, superseded, or
  retracted.
- Mark publication lifecycle separately from product state.
- Keep retracted outputs searchable, but exclude them from default operational
  evidence and product recommendations.
- Apply a correction to its parent publication. Do not create another study.
- Do not present a planned product as a completed product.

## Funding and inclusion

Include all verified EuroQol-supported outputs, even when a paper reports no EQ
instrument.

Accept a project-publication link when the paper directly links EuroQol to the
work or data, or when an authoritative portfolio record lists the output. Keep
the exact support type, such as study funding, data-collection funding, author
grant, or travel grant.

Folder placement, author overlap, and topic similarity are not sufficient.
Keep an unresolved link as `candidate`; do not count it as verified funding.

## Deterministic metadata

Parse publication metadata from JATS or another structured source before AI
semantic extraction. This includes identifiers, title, abstract, authors,
ORCID, affiliations, correspondence, journal, publisher, article type,
language, date roles, volume, issue, URLs, licence, keywords, funding fields,
references, and source provenance.

The AI receives this parsed record as context. It extracts the research
semantics that structured metadata does not supply. Missing metadata remains
missing. Conflicts remain explicit.

## Analytics layer

Counts, trends, rankings, networks, similarity scores, and research-gap results
are derived analytics. Each analytic result states its data snapshot, filters,
and rule. Do not present a calculated portfolio result as a study finding.

## Implementation choice

Use a relational database for the first production system. The ontology maps
naturally to typed tables and join tables. SQLite answered all pilot questions.
Move to another database only when measured access or scale needs require it.

## Evidence for v1

- 100 papers and 100 user questions informed three independent ontology
  proposals.
- Ten unseen papers tested the first proposal and caused evidence-based
  revisions.
- A source-checked ten-study SQLite pilot passed 15 executable queries.
- All 220 repository JATS files parsed twice with zero failure and identical
  output.
- A second, non-overlapping 20-paper batch passed source, manifest, ontology,
  database, and 23 executable query checks.

The 100 user questions remain the design requirements in `questions.tsv`.
