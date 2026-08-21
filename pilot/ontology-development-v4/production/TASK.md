# One-pass EuroQol paper assessment and extraction

Read the structured metadata and the full article once. Return JSON that
matches the supplied output schema. Do not return Markdown.

## Filter

Set `connection` to:

- `direct_eq` when EuroQol measurement, an EQ instrument, an EQ value set, or
  an EQ valuation or measurement method is a primary research object;
- `adjacent_measurement` when health or well-being measurement or health-state
  valuation is primary without a direct EQ focus;
- `application_only` when a measure or utility is only an outcome, covariate,
  or model input;
- `unrelated` or `unclear` when applicable.

Set EuroQol support to `explicit` only when a funding or acknowledgement
statement links EuroQol support to this work or to an author's work on this
paper. Keep the exact scope. Include `direct_eq`, `adjacent_measurement`, and
explicitly supported work. Use `publication-context` for a correction or
retraction notice that reports no new study. Otherwise, exclude unsupported
`application_only` and `unrelated` work.

For an excluded or context-only publication, return empty `studies` and
`items` arrays. For a correction or retraction notice, give the target DOI and
the `CORRECTS` or `RETRACTS` relation in `publication_relation`.

## Extraction

- Classify the Study, not the Publication. For a protocol article, classify
  the planned study aim and intended main result.
- If the authors report multiple studies, create one `Study` record for each.
  Use `StudyPart` only for a component within one study.
- Give each study one primary family and ranked purposes. A purpose must be a
  stated scientific aim or principal output. Do not promote a procedure,
  model choice, discussion topic, or operational context to a purpose.
- Use the smallest purpose set supported by the stated aims and principal
  outputs. Do not add a broader purpose that restates a narrower one.
- Create a `StudyPart` only for a separable sample, data source, method, or
  state. A simple study can have no parts. Keep parts flat and set a
  `StudyPart` item's own `part_id` to `null`.
- Use separate parts for pilot and formal stages, or for a methodological
  add-on whose data are reported elsewhere. Do not combine their samples or
  assign pilot data to the formal study results.
- A protocol article can report completed pilot or development work before the
  main study. Extract that work and its influence, but keep the main planned
  study status and result state unchanged.
- Use exact controlled values from the supplied vocabulary. Use a `Gap` when
  a value, key, or relation does not fit. Do not create an official value.
- Preserve the exact source label for instruments, methods, protocols,
  models, software, existing products, and scoring products. Set `registry_id`
  to `null` in the AI draft. Deterministic normalization adds only reviewed
  exact identities afterward. Do not add a `Gap` only because a registry
  identity is absent.
- Separate direct, observed, source-study, input-provenance, planned, and
  discussion-only uses. Give each use one context and one function.
- Set a scientific use's `part_id` to `null` when it governs the whole Study
  or spans all parts. Use a part ID only when the use is confined to that
  part. Do not duplicate a study-wide use across parts.
- Create another InstrumentUse when the same instrument has another function,
  such as both HEALTH_STATE_DESCRIPTION and VALUATION_TARGET.
- A `DataUse`, `Sample`, or `TaskDesign` can have `part_id=null` when it applies
  to the whole Study. Use a part ID when the fact is confined to that part.
- Link a Sample to a Population only when its units are people or population
  units. Leave `population_id` null for response, task, record, or observation
  counts.
- Create one scientific-use item for one instrument, method, protocol, model,
  software, existing product, or scoring product identity. Split a list of
  tests, models, software products, or other products into separate items
  unless the source names one combined identity.
- Use EXPERIMENTAL_DESIGN for a method or software implementation that creates
  choice sets, task blocks, randomization schedules, or another experimental
  design. Keep the design algorithm and its software implementation separate.
- Use `SoftwareUse` for a named program, package, command, or computational
  platform that the study uses. Keep it separate from the method, protocol,
  model, or reusable Product that it implements. Do not turn software into one
  of those types only because the study used it.
- Extract software that delivers participant data collection, scientific
  analysis, modeling, data management, or reported output. Do not extract an
  incidental communication tool that has no material scientific role.
- Use `ProductUse` for an exact existing reusable product that the current
  study examines, compares, or synthesizes. This includes an existing value
  set studied for validity, properties, or obsolescence. Do not represent a
  value set or another product as an `InstrumentUse`.
- Keep a product that the current study develops or reports as a `Product`.
  Do not create a `ProductUse` only because the current paper creates that
  output.
- Use `ScoringUse` only when the study applies a value set or scoring product
  to instrument responses. Do not replace that application with `ProductUse`.
  A value set that the study develops or reports is a `Product`, not a scoring
  use unless it is also applied.
- Record ordinary reverse scoring, level sums, and score transformations as a
  MethodUse with MAPPING_OR_DERIVATION unless the source identifies an exact
  reusable value set or scoring product.
- Use source-study context only for activity from a separate prior study. Work
  reported as part of the current study remains current activity.
- When the current paper performs a secondary analysis of a prior study, set
  reused participant data to PRIOR_RESEARCH_COLLECTION. Give the source
  study's collection, sampling, instrument, and administration uses
  SOURCE_STUDY_ACTIVITY or INPUT_DATA_PROVENANCE context as applicable.
- Bind administration details to applicable instrument, method, protocol, and
  software uses, and to applicable tasks, when they share those details. Split
  the Administration when channel, language, respondent, perspective,
  assistance, setting, recall, or time differs, even for a small subgroup.
- A `TaskDesign` can apply to a method, protocol, or an instrument whose
  content or health states the task directly uses or changes. It can also
  apply to software that delivers the task. Do not link an instrument or
  software product only because it occurs elsewhere in the study.
- A study-level `Design` value describes a study with no parts and is a default
  for all parts. A part value replaces that axis. The study or every
  substantive part must resolve component, time, comparison, and allocation
  values.
- Use BETWEEN_INSTRUMENT only for a planned instrument comparison. An inventory
  or description of several instruments is NONCOMPARATIVE.
- Use PARTICIPATORY_DESIGN only when participants or stakeholders jointly
  create, refine, or select an output. Pilot testing or user feedback alone is
  not participatory design.
- Extract principal findings at the depth needed to explain the contribution.
  Keep selected aggregate values, not participant values or complete tables.
- Keep important recruitment, exclusion, completion, and analysis counts.
- Use IDENTIFIED, SCREENED, and ELIGIBLE for general sample flow when the
  source gives those counts.
- For evidence synthesis, use IDENTIFIED_RECORDS for search results,
  SCREENED for an initial screening count, FULL_TEXT_ASSESSED for full-text
  eligibility assessment, and INCLUDED_EVIDENCE for the final included
  evidence. Do not use APPROACHED for documents or search records.
- Split `DataUse` records when data components differ in origin, level, or
  analytic purpose, even when the study collected them in one session.
- Record each distinct data-collection component that defines the reported
  methods, including open-ended and closed-ended components. Do not omit a
  component only because the paper gives no separate result for it.
- When a principal finding depends on a comparator procedure, record the
  instruments, mapping model, and scoring product that create the comparator.
- Create one StudyFactor for one analysed variable or randomized task
  condition. Do not combine unrelated respondent characteristics, display
  position, order, or other conditions as levels of one factor.
- Record a named review framework or methodological refinement as a
  ProtocolUse when it governs the current review. Keep reporting guidance
  separate.
- Include important negative or null findings that qualify the conclusion.
- Keep author interpretations separate. Extract only source-reported
  limitations.
- Do not use `StudyFactor` for task profiles, health-state descriptions, or
  reference points. Keep these in `TaskDesign`.
- Use open `Concept` items for useful EuroQol themes that do not replace exact
  instruments, methods, populations, factors, or purposes.
- A `Finding`, `Limitation`, or `Concept` can refer to the Study ID when the
  statement applies to the whole study and no narrower item is correct.
- Record incompatible repeated facts as `SourceConflict`. Do not repair them.
- If the text describes a cited source study but the cited reference identifies
  a different work, create a `SourceConflict` with both locators.
- Give a section, table, figure, or paragraph locator for every item.
- Do not extract project links. That is a separate task.
- Do not reconstruct bibliographic metadata that the structured input gives.

Use short local IDs such as `s1`, `part1`, `iu1`, and `f1`. Fixed ID fields
define relations. Do not emit generic graph triples or free-form properties.
