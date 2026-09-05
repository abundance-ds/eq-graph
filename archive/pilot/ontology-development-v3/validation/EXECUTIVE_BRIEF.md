# Executive decision brief: EuroQol research ontology

> **Historical validation gate.** The SQLite pilot requested here was completed
> and followed by the 209-paper production pass. Current decisions are in
> [`../production-calibration/DECISION.md`](../production-calibration/DECISION.md).

**Reading time:** four minutes

**Mission status:** the ontology direction is approved. Three policy additions are now fixed. The relational pilot has not started.

## 1. Situation

The project needs a research ontology and extraction system that helps users find and understand EuroQol research.

Earlier attempts failed because they started with abstract structures such as `Paper`, `Component`, and evidence assertions. They did not center the terms that researchers search for, such as:

- `valuation study`;
- `EQ-5D-5L`;
- `cTTO` and `DCE`;
- exact administration mode and language;
- exact statistical model;
- value set, mapping function, translation, or other product;
- principal findings, interpretations, and gaps.

We reset the work and built the ontology from evidence and user questions.

## 2. What we did

1. Selected 100 varied EuroQol-related papers.
2. Used lower-cost agents to produce fixed, dense summaries.
3. Gave three independent Sol agents different controlled sets of 50 papers and 50 user questions, with 50% overlap.
4. Compared the three ontology proposals.
5. Rejected their shared tendency to make an evidence-assertion graph central.
6. Produced a compact, EuroQol-specific proposal.
7. Tested it on ten new papers that were not used to design it.
8. Different agents checked all ten extractions against the full articles.
9. Tested twelve realistic questions against the extracted records.

Results:

- Ten of ten records passed source review after minor corrections.
- Ten question tests passed.
- One question test was partial because the ontology lacked a review evidence unit.
- One funding-boundary test passed: it caught an unverified project link. Its possible economic-analysis profile is deferred.
- No question test failed.

## 3. What the proposed system now captures

For each study, the system captures:

- research purpose and study design;
- flexible, source-grounded concepts and themes;
- target population, recruitment source, samples, and subgroups;
- exact instrument, version, form, language, and role;
- administration channel, interaction, respondent, perspective, setting, and recall period;
- exact research or valuation methods;
- protocol and important task design;
- analysis and exact statistical models, including candidate and preferred roles;
- research products and their status;
- measured outcomes or properties;
- the study-level findings needed to explain the paper's contribution;
- interpretations, limitations, data-quality caveats, and research gaps;
- source location and conflicts.

It does not capture participant-level data or every coefficient and result table.

Example: the German value-set record makes all of these direct search values:

```text
Research purpose: value-set development
Study design: national valuation survey
Population: German adults
Instrument: EQ-5D-5L
Protocol: EQ-VT 2.0
Valuation methods: cTTO; DCE
Preferred model: hybrid model 3b with censoring and heteroskedasticity
Product: German EQ-5D-5L value set
Finding: predicted range -0.661 to 1; pain/discomfort had the largest effect
```

This is the intended unit of usefulness.

## 4. What the holdout taught us

The core works. Six narrow revisions are justified by the evidence:

1. Separate `research purpose` from `study design`.
2. Add lineage for reused input datasets and cohorts.
3. Add a review evidence unit so publications and review-level observations are not confused.
4. Defer an economic-analysis profile until accepted portfolio evidence requires it.
5. Distinguish instrument administration from reuse or visualization of historical instrument data.
6. Keep family-specific detail inside existing concepts, such as DCE design, proxy perspective, sample stage, and product status.

These are controlled extensions. They do not turn the model into a general research ontology.

## 5. Strategic assessment

This is no longer a dead end. The model is now useful enough for a small relational implementation.

The strongest evidence is not agent agreement. It is the unseen-paper test:

- A national valuation study retained exact methods, models, and product details.
- A proxy study retained respondent type, proxy perspective, qualitative findings, and instrument problems.
- A systematic review exposed the need for review evidence units.
- An economic-burden boundary case exposed a possible family-specific profile, but its project link did not pass the funding rule.
- A decision-aid study correctly distinguished displaying EQ-5D-5L data from administering EQ-5D-5L.

The pilot also caught two false assumptions. A selection note said that one paper used EQ-5D-5L, but the article reported no EQ instrument. A later funding audit found that the article did not connect EuroQol support to the study. Its Funding section named other funders; EuroQol grants occurred only in one author's competing-interest statement. The paper is now an unverified candidate, not a confirmed EuroQol output.

## 6. Decisions fixed

### Decision A — Ontology direction and concepts

**Decision:** Accepted, with a flexible `Concepts and themes` layer.

Exact EuroQol research facts remain central, with optional family-specific profiles. `Concepts and themes` adds cross-cutting discovery terms, such as states worse than dead, child and adolescent health, proxy reporting, digital health, respondent engagement, attribute non-attendance, health inequality, cultural adaptation, caregiver spillover, and routine PROM implementation.

Concepts do not replace exact population, instrument, method, model, product, or finding values.

**Trade-off:** A compact core is easier to maintain, but some study families need optional detail. A single universal schema would look cleaner but would lose important distinctions or become too large.

### Decision B — Funded work with no EQ instrument

**Decision:** Keep all verified EuroQol-supported outputs. Mark `EQ instrument use: none reported` when applicable. Include their scientific content, but do not return them for queries that require an EQ instrument.

For a no-EQ paper, require a direct article statement that EuroQol supported the work or data, or an authoritative EuroQol project-output record. An author grant disclosure alone is not enough. Record the exact support type.

**Trade-off:** Excluding them gives a purer instrument corpus but creates an incomplete account of funded work and impact. Including them without a clear module boundary pollutes instrument searches.

### Decision C — Findings depth

**Decision:** Do not set a default count. Explain the required level and trust the agent to apply it to the paper.

For a valuation study, this normally includes the utility range or anchors, lowest and highest states when relevant, dimension order or importance, the selected model and why it was selected, and notable author-emphasized findings. A commentary can need only one or two main arguments.

**Control:** Keep participant-level values and complete result tables outside the ontology. Capture author-reported limitations, data-quality caveats, scope limits, research gaps, and source conflicts. Do not invent them.

### Table stakes — Publication metadata

Parse official metadata from JATS XML or another structured source before AI extraction. This includes identifiers, authorship, affiliations, journal data, date roles, URLs, licence, abstract, keywords, funding data, references, and provenance. Give the result to the AI as context. Do not spend AI work on reconstructing it.

### Decision D — Authorize the relational pilot

**Status:** Paused until the decisions above are confirmed. The next action is a small SQLite implementation using only checked records.

The pilot must demonstrate:

- exact filters for study type, instrument, method, model, population, and product;
- retrieval of principal findings and gaps;
- source and conflict inspection;
- correct instrument-use roles;
- the systematic-review extension and the funding-link gate.

Do not build the full database or automated pipeline yet.

## 7. Decision principles

Use these principles when changing the recommendation:

1. **Retrieval value before theoretical completeness.** Structure a fact when it improves a real search, comparison, or synthesis task.
2. **Exact source meaning before generic normalization.** Keep source terms and map them to preferred labels without erasing them.
3. **High detail for corner pieces.** Instruments, methods, administration, models, products, populations, and findings need precision.
4. **Text for low-value detail.** Do not structure every coefficient, task pair, quotation, or protocol sentence.
5. **Separate reported facts from calculated answers.** Counts, ranks, trends, networks, and similarity are derived analytics.
6. **Absence is not evidence unless checked.** `No instrument reported` is different from `instrument not extracted`.
7. **Database choice follows meaning.** Use relational storage now. Add graph views later only if they solve a proven problem.

## 8. Requested response

If this brief now reflects the intended policy, reply:

> **Start D.**

Supporting evidence:

- `records/H01.md`: valuation study.
- `records/H05.md`: proxy and qualitative study.
- `FUNDING_EVIDENCE_AUDIT.md`: checked no-EQ funding cases.
- `METADATA_POLICY.md`: deterministic publication metadata.
