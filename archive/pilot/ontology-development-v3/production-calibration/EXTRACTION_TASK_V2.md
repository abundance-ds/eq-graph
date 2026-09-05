# One-pass full-text assessment and extraction

## Task

Read the supplied metadata, project candidate, and full article once. Decide
whether the publication enters the research corpus. If it does, write a dense,
source-faithful research record. State each fact once and avoid boilerplate.
Use only the supplied material.

## Assessment

Choose one connection:

- `direct_eq`: an EQ instrument or EuroQol measurement or valuation method is
  a primary research object;
- `adjacent_measurement`: health or wellbeing measurement or health-state
  valuation is primary, without a direct EQ focus;
- `application_only`: a measure or utility is only an outcome, covariate, or
  model input;
- `unrelated` or `unclear`.

A clinical, economic, or epidemiological study is `application_only` when it
only calculates QALYs or DALYs, or uses utility or disability weights as an
input or outcome. This alone is not measurement or valuation research.
Development, translation, adaptation, or psychometric evaluation of a non-EQ
health, wellbeing, or patient-reported measure is `adjacent_measurement`.

Choose EuroQol support for the current output as `explicit`,
`other-funding-only`, `none-stated`, or `unclear`. Use `explicit` only when a
funding or acknowledgement statement links EuroQol support to this work, or to
an author's work on this paper. Keep its exact scope, such as study funding,
data-collection funding, author involvement, travel grant, or publication fee.
A grant listed only in competing interests, an author biography, a folder, or
a candidate project does not show support for the current output.

Disposition:

- `include-study` if connection is `direct_eq` or `adjacent_measurement`, or
  if the current output has explicit EuroQol support;
- `publication-context` for a correction or retraction notice that does not
  report another study;
- `exclude` for unsupported `application_only` or `unrelated` work;
- `unclear` when the source is insufficient.

Keep a retracted research article as `include-study`, but mark it retracted and
unsafe for operational use. Project candidates are possibilities, not proof.

## Output

Write Markdown. Use bullets under each heading. Start with these exact headings
and labels:

### Assessment

- Disposition:
- Connection:
- EuroQol support:
- Support scope:
- Project link: `explicit`, `probable`, `possible`, `none`, or `unclear`; give
  project IDs only when supported.
- Publication status:
- Evidence: concise article-specific support for the decisions.

For `exclude` or `publication-context`, add a short publication-relation note
when relevant and stop.

For `include-study`, continue with:

### Study

Give exact research purposes, study designs, and planned or completed status.

### Population and data

Separate target population, recruitment source, sample stages, subgroups, and
reused datasets or cohorts. Do not use one ambiguous sample size.

### Instruments and administration

For each exact instrument or version, state its role, language, respondent,
perspective, interaction, channel, setting, recall period or time points, and
scoring source when reported. Displaying old instrument data is not
administering the instrument.

### Methods and analysis

Give exact research methods, protocols, important task design, analyses, and
statistical models. Give each model its role. `Hybrid` is normally a model, not
a valuation method. Record a derivation step only when it materially changes
meaning or uncertainty.

### Products and concepts

Give each research product and its status. Add a concise free list of
source-grounded concepts or themes that improves discovery.

### Outcomes and findings

State measured outcomes or properties, principal results, and separate author
interpretations. Use the depth needed to explain the contribution. For a
valuation study, normally include anchors or range, dimension order, selected
model and reason, and notable results. Do not copy complete tables or
participant-level values.

### Limitations and source issues

Give reported limitations, gaps, data-quality caveats, missing facts, and
conflicts between source sections. Before you finish, compare repeated sample
counts, main result values, funding, and publication status across the
abstract, body, and tables. Report contradictions; do not silently choose one.
Do not add a statement that no contradiction was found.
Differences between a project plan and a completed study are not source
contradictions. Different publication date types are also not contradictions.

### High-value terms

List the exact terms that define the paper for a EuroQol researcher. Check the
exact study type, population, instrument and version, method, protocol, model,
product, and important concepts before you finish.

Add a source section, table, figure, or paragraph locator to each substantive
bullet. Do not reconstruct bibliographic metadata that the structured input
already supplies. Do not invent a fact to fill a heading.
