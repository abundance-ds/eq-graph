# Evidence- and review-based ontology revisions

These revisions apply to the pre-pilot proposal in `review/FINAL_PROPOSAL.md`. They come from direct extraction and source QA of H01-H10.

## 1. Separate research purpose from study design

Use two small, multi-value classifications.

`Research purpose` answers why the study was done. Examples are:

- value-set development;
- valuation-method research;
- measurement-property evaluation;
- instrument development;
- content validity;
- population health;
- implementation;
- economic burden;
- evidence synthesis.

`Study design` answers how the study was done. Examples are:

- national valuation survey;
- multi-arm DCE experiment;
- test-retest study;
- qualitative think-aloud study;
- cross-sectional population survey;
- systematic review;
- cost-of-illness study;
- prototype usability study.

This keeps `valuation study` as an exact searchable type. It prevents labels such as `survey/interviewer/data-quality study` from mixing purpose, design, and collection mode.

Evidence: H01-H10, especially H02, H06, H09, and H10.

## 2. Add input dataset and cohort lineage

Add an optional `Input dataset or cohort` record with:

- source dataset name;
- collection period;
- recruitment source;
- source sample count;
- duplicate-removal or harmonization rule;
- analytic contribution count;
- relation to other cohorts or the merged analytic sample;
- source location.

This is necessary when one paper reuses or merges several datasets. A diagnostic subgroup is not the same as an input cohort.

Evidence: H04 combines three source families and several cohorts. H09 combines survey, health-system, population, and unit-cost data.

## 3. Add a review evidence unit

For evidence syntheses, add an optional `Review evidence unit` with:

- source-defined unit type;
- underlying publication;
- instrument;
- population;
- property or outcome;
- result;
- quality rating;
- inclusion in an aggregate review finding.

This prevents a review's publications, primary studies, hypotheses, ICC values, effect sizes, and aggregate ratings from being called the same thing.

Evidence: H07 includes 79 publications and 1,504 source-defined units. Each hypothesis, ICC, or standardized effect-size value can be one review unit.

## 4. Defer the economic analysis profile

H09 showed how an optional profile could describe cost-of-illness, economic-burden, and related studies:

- economic perspective;
- cost and price year;
- currency and conversion;
- costing approach;
- direct medical cost;
- direct non-medical cost;
- indirect or productivity cost;
- informal-care cost;
- intangible wellbeing loss;
- burden measure, such as DALY or QALY;
- population extrapolation method;
- sensitivity-analysis method.

However, the funding audit did not verify H09 as a EuroQol-supported output. Do not add this profile from H09 alone. Add it only when an accepted EuroQol-supported paper or a user question needs it. If added, use exact terms such as `cost-of-illness study` and `economic-burden study`. Do not force these papers into `economic evaluation or utility application`.

Conditional evidence: H09 is a source-faithful boundary case with an unverified project link.

## 5. Extend instrument-use roles

Add these roles:

- historical instrument data reused;
- instrument data visualized;
- instrument data used in decision support.

These roles are different from administering the instrument in the current study.

Evidence: H10 displays historical EQ-5D-5L data. Its participants did not complete EQ-5D-5L.

## 6. Keep family-specific detail inside existing concepts

The following details improve search but do not need new top-level ontology concepts:

- DCE design construction method, prior assumption, overlap structure, software, and focal design subset under `Task design`;
- proxy type, proxy-person or proxy-proxy perspective, and response heuristics under `Administration` and `Finding`;
- scoring value set and scoring source under `Instrument use`;
- existing, prototype, revised, planned, tested, and implemented under `Product status`;
- recruited, screened, completed, analytic, outcome-specific, and population-extrapolation counts under `Sample`.

Evidence: H02, H05, H06, H08, H09, and H10.

## 7. Add flexible concepts and themes

Add a multi-value `Concepts and themes` layer for cross-cutting research topics. Keep exact source terms and add preferred terms when the mapping is clear.

This layer supports discovery and study similarity. It does not replace exact study type, population, instrument, method, model, product, outcome, or finding fields. It is not a closed classification during ontology development.

Examples include states worse than dead, child and adolescent health, proxy reporting, digital health, respondent engagement, attribute non-attendance, health inequality, cultural adaptation, caregiver spillover, and routine PROM implementation.

## 8. Use a finding depth, not a finding count

Do not set a default number of findings or estimates. Extract the study-level findings needed to understand the paper's contribution and answer relevant research questions.

For a valuation study, this normally includes the utility range or anchors, lowest and highest states when relevant, dimension order or relative importance, selected model and selection reason, and notable author-emphasized findings. Other study families need different depths.

Retain the exclusions: no participant-level values, no complete result-table copy, and no assertion record for every coefficient.

## 9. Make limitations explicit

Capture reported limitations, data-quality caveats, scope limits, research gaps, and source conflicts. Preserve their relation to the applicable finding, method, sample, or whole study. Do not invent limitations.

## 10. Treat publication metadata as deterministic table stakes

Parse available identifiers, authorship, affiliations, journal data, date roles, URLs, licence, abstract, keywords, funding data, references, and source provenance from JATS XML or another structured source before AI extraction.

Give the parsed record to the AI as context. Do not ask the AI to reconstruct this metadata from prose. See [METADATA_POLICY.md](METADATA_POLICY.md).

## 11. Require verified funding evidence

Include all verified EuroQol-supported outputs, even when they use no EQ instrument. For a no-EQ paper, accept the project link only when the article directly links EuroQol to this work or its data, or an authoritative project record lists the paper as an output.

Author grant disclosures, folder placement, author overlap, and topic similarity are not enough. Record the exact support type. See [FUNDING_EVIDENCE_AUDIT.md](FUNDING_EVIDENCE_AUDIT.md).

## 12. No change to these decisions

- Exact EuroQol terms remain first-class searchable values.
- Instrument, method, model, product, outcome, and finding remain separate.
- Findings remain at study level, with only the aggregate estimates needed to understand them.
- Participant-level values and complete result tables remain outside the ontology.
- Provenance remains attached to ordinary records. There is no universal assertion graph.
- Portfolio data and derived analytics remain separate modules.
- A relational pilot implementation remains appropriate after human review of the concrete records.
