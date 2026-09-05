# Practical ontology for health measurement meta-research

## Purpose

This ontology helps a researcher describe and compare studies about health and quality-of-life measurement. It covers instrument concepts, development, translation, psychometric evaluation, preference valuation, outcome derivation, statistical and decision-model use, survey-data quality, implementation, population norms and inequalities, burden and cost estimation, population data resources, and decision-maker needs.

The ontology is a set of linked concepts and comparison facets. It is not a fixed form. A paper can have more than one study activity, method, comparison, or output.

## Main organizing view: the measurement chain

The papers show that the word *measurement* can refer to different layers. These layers must stay separate.

```text
intended construct
  -> conceptual framework
  -> instrument and version
  -> dimension, item, label, or response scale
  -> response, profile, or self-rated score
  -> preference elicitation and valuation model
  -> value set, mapping, scoring, or aggregation rule
  -> scored, mapped, or aggregated outcome
  -> analyzed outcome or population summary
  -> inequality, burden, cost, or decision-model outcome
  -> evidence used for policy, care, or population assessment
```

| Layer | Meaning | Typical comparison question |
|---|---|---|
| Intended construct | The broad object to measure, such as health status, HRQoL, QoL, wellbeing, capability, or social-care-related QoL. | Does the instrument cover the intended construct? |
| Conceptual framework | The organized domains and subdomains that define the construct for an instrument or a population. | Does a lay framework contain domains that the instrument framework does not contain? |
| Instrument | A named measure and its version, target group, respondent form, dimensions, recall period, and scoring options. | How do EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D differ? |
| Component | A dimension, item, severity label, response scale, or visual analogue scale within an instrument. | Does a frequency scale behave differently from a severity scale? |
| Observation | A response, health profile, dimension response, VAS score, or other value produced by a respondent. | Are there missing responses, ceiling effects, or stable retest responses? |
| Preference evidence | Values from tasks such as TTO, cTTO, DCE, SG, or VAS, with a stated respondent and valuation perspective. | Do cTTO and DCE give compatible relative preferences? |
| Scoring or transformation artifact | A value set, tariff, crosswalk, mapping model, or aggregation rule that converts source observations to another representation. | Was a utility scored from the reported profile or predicted from a different instrument? |
| Derived or analyzed outcome | A direct response, scored value, mapped value, unweighted summary, change score, population norm, inequality index, DALY, monetized burden, QALY, ICER, or other representation used in an analysis. | Does a change in source, scoring, aggregation, or modeling change the downstream result? |
| Use context | The clinical, economic, population-health, or HTA purpose for which the evidence is produced or used. | Is the evidence suitable for cost-utility analysis or population comparison? |

An instrument can span several layers. Record the layer that a study directly examines. For example, a paper that compares utility models does not directly test the descriptive system, even if the model uses responses from that system.

## Core entities

### 1. Research report

A **research report** is the paper-level record. It can report one or more study activities. Keep supplied identifiers and bibliographic data outside the semantic description unless a conflict or gap requires a note.

Useful report facets are:

- contribution type;
- completion stage;
- main research purpose;
- reported output;
- linked study activities;
- source study, dataset, or collection wave;
- known evidence overlap with other reports.

Suggested contribution types are primary empirical study, secondary analysis, systematic review, study protocol or resource description, and practice or needs assessment. More than one type can apply.

### 2. Study activity

A **study activity** is a coherent piece of research within a report. It has a purpose, evidence basis, design, methods, comparison, and output. This concept prevents a multi-phase instrument-development paper from being forced into one design label.

Useful activity purposes include:

- define a construct or framework;
- develop or revise an instrument;
- translate or culturally adapt an instrument;
- test content, comprehension, or feasibility;
- evaluate measurement properties;
- elicit health preferences;
- estimate or compare valuation models;
- develop a value set;
- assess the effect of scoring, mapping, or aggregation choices;
- estimate population distributions, associations, or inequalities;
- produce or compare population norms;
- estimate disease burden, resource use, or societal cost;
- describe analytic practice;
- assess collection implementation or acceptability;
- design or assess response-data quality controls;
- assess stakeholder practice, needs, or priorities;
- create or describe a comparable data resource.

When it changes interpretation, record the inferential aim as description, association, prediction, causal effect, measurement-property evaluation, or method performance. Do not interpret an adjusted association as a causal effect unless the design supports that inference.

### 3. Evidence source and research-data lineage

An **evidence source** is the material from which a study activity draws evidence.

Record:

- source unit: person, dyad, paper, trial, registry record, or existing dataset;
- source role: general-public respondent, patient, child or adolescent, caregiver, care recipient, professional stakeholder, expert, translator, or study report;
- target population and sampled population;
- age or other eligibility limits when they affect interpretation;
- country or region;
- recruitment and sampling method;
- sample size;
- data-collection mode;
- timing: cross-sectional, test-retest, longitudinal, or literature-search period;
- whether the data are primary or reused.

Also record the data lineage when a report reuses or combines evidence:

- named source study, survey, trial, registry, or dataset;
- collection wave and source dates;
- source sample, eligible sample, and final analysis cohort;
- exclusions, quality filters, and transformations that create the analysis cohort;
- overlap with other reports or datasets in the lineage record.

Two reports that analyze the same people are not independent evidence, even when they answer different questions. Record overlap only when the supplied papers establish it. Do not infer overlap from similar authors or settings alone.

Keep the evidence actor and the measurement referent separate. Record, when relevant:

- who gives the response;
- whose health, wellbeing, experience, or preferences the response describes;
- the requested perspective, such as self-report, proxy opinion, or proxy estimate of the person's view;
- whose preferences a value set is intended to represent;
- the proxy's relationship, familiarity, and instructions;
- possible spillover from the described person to the proxy.

Do not encode **representative** as a simple fact. Record the target, quota or probability method, coverage, recruitment source, and important departures. The paper's representativeness claim can then be assessed.

### 4. Measurement artifact

A **measurement artifact** is an object in the measurement chain. Its main subtypes are conceptual framework, instrument, instrument version, language or cultural version, respondent form, bolt-on or other extension, dimension or item, response label or scale, health profile, health-state vignette, value set, tariff, crosswalk, mapping model, disability weight, aggregation rule, and scoring algorithm.

Record only the characteristics that matter to the study:

- instrument family and exact version;
- language and intended jurisdiction when these affect use;
- intended construct;
- intended age or population;
- self-report, proxy, or other perspective;
- dimensions or components under study;
- response levels and scale type;
- recall period;
- preference-weighted or profile-only status;
- development or authorization status, such as experimental, draft, revised, or established.

### Cross-cutting facet: outcome derivation and provenance

The same outcome name can refer to quantities with different origins. Distinguish:

- a response or profile reported directly with the named instrument;
- a score calculated from that instrument's responses with a stated value set or rule;
- a mapped or predicted score derived from another source measure;
- an unweighted aggregate, such as a level-sum score;
- a population summary, such as an age-sex norm or profile ceiling;
- an inequality summary or decomposition derived from responses or scores;
- a burden or cost outcome, such as YLD, DALY, monetized wellbeing loss, or total societal cost;
- a decision-model endpoint, such as a QALY or ICER, that uses a measurement output as an input.

Record the source observation or instrument, source dataset and wave, transformation artifact and version, target representation, population scaling or weighting, perspective, cost bearer when relevant, and downstream analysis. For a temporal comparison, record whether both periods use the same instrument and scoring rule. Do not call a mapped EQ-5D value an observed EQ-5D response. Do not call an unweighted profile summary a preference-weighted utility. Do not treat a monetized DALY as a directly observed cost.

### 5. Artifact role in a study

The same instrument can have different roles. Link each artifact to its role in each activity.

- **development target**: the activity changes or creates it;
- **evaluation target**: the activity tests its properties;
- **source artifact**: the activity translates, maps, or derives another artifact from it;
- **comparator**: it provides one object in a comparison;
- **reference or anchor**: it supports validity, interpretation, or scale anchoring;
- **data generator**: it produces the responses under analysis;
- **context measure**: it supplies covariates, group definitions, or descriptive context;
- **reported option**: stakeholders report whether they use or value it.

### 6. Method

A **method** is a procedure for collection, elicitation, analysis, or synthesis. Record a method family first. Add the exact named method when it changes interpretation or supports comparison.

Method families in the three rounds include:

- qualitative elicitation and thematic framework analysis;
- cognitive interviewing, sorting, and response scaling;
- translation and cultural adaptation, including forward translation, back translation, reconciliation, and proofreading;
- survey administration and quota sampling;
- survey-data quality control, including soft launch, bot and duplicate detection, response-time rules, consistency checks, outlier review, and quota monitoring;
- workflow implementation, mixed-mode collection, and acceptability assessment;
- test-retest and hypothesis-based psychometric testing;
- preference elicitation with TTO, cTTO, DCE, DCE with duration, SG, or VAS;
- valuation models, including conditional logit, mixed logit, Tobit, hybrid models, and temporal-preference corrections;
- score mapping, response mapping, unweighted aggregation, and decision-analytic modeling;
- population norms, survey weighting, inequality indexes, decomposition, and temporal population comparison;
- prevalence-based burden estimation, resource-use costing, DALY estimation, monetization, cost allocation, and sensitivity analysis;
- item and scale analysis, including correlation, Shannon indices, IRT, DIF, and ordinal regression;
- systematic search, study selection, descriptive synthesis, and meta-analysis;
- statistical treatment-effect models for numerical, categorical, repeated, and time-to-event outcomes.

For a review of methods, distinguish the review's own synthesis method from the methods found in its source studies.

For preference valuation, record the task frame and scale assumptions when they affect the output. These can include the described person's age, self-versus-other perspective, task wording, definition of death or full health, anchor choice, duration, and linear or nonlinear time preference.

### 7. Evaluation

An **evaluation** links a target to a property, method, population, and interpretation. Record the level of the target because an index can perform differently from an item.

Main property families are:

| Family | Examples |
|---|---|
| Content and concept | relevance, comprehensiveness, comprehensibility, cultural fit, domain coverage |
| Response and distribution | missing responses, completion time, ceiling, floor, response-category use |
| Implementation and acceptability | reach, enrollment, retention, repeat completion, willingness, burden, accessibility, timing, mode, workflow fit |
| Reliability and error | test-retest agreement, ICC, Kappa, measurement error |
| Validity | construct, convergent, known-groups, discriminant, criterion, structural validity |
| Responsiveness | change detection, effect size, anchor-based change, MID |
| Scale functioning | informativity, discrimination, thresholds, DIF, incremental discrimination from added components |
| Valuation-model performance | monotonicity, logical consistency, coefficient significance, anchoring, fit or prediction error, censoring and heterogeneity treatment |
| Response-data integrity | likely human response, attention or speed, duplicate status, repeated-item consistency, outlier plausibility, missingness, and effect of exclusion rules |
| Data fitness and inference | coverage, sampling evidence, quota attainment, weighting, sample size, comparability, temporal alignment, match to target population or decision model |
| Analytic adequacy | baseline adjustment, assumption checks, missing-data handling, repeated-measure handling, alignment with estimand |

Use a short interpretation such as supported, mixed, limited, problematic, or not assessed. Add the paper's stated threshold or criterion when it materially affects that interpretation. Do not convert all results into detailed claim records.

### 8. Comparison

A **comparison** has a basis and at least two comparison objects. Common objects are instrument versions, instruments, response-scale types, valuation methods, models, value sets, frameworks, populations, countries, regions, and health groups.

Record:

- the objects;
- the comparison basis;
- whether the comparison is direct, indirect, or descriptive;
- whether it is within-person, within-sample, between parallel samples, or across reused sources;
- alignment of population, respondent, instrument, language, calendar period, mode, source study, data, scoring or transformation, design, and criteria;
- important asymmetries or confounding factors.

This entity is necessary because a statement such as "5L performed better" is not meaningful without the property, population, and comparison design.

### 9. Output

An **output** is what the activity adds for later research or use.

Output types include:

- conceptual framework;
- instrument or version;
- translated or culturally adapted version;
- preferred label or response-scale design;
- measurement-property evidence;
- value set or tariff;
- model recommendation;
- evidence about the downstream effect of scoring or mapping;
- population norm, inequality estimate, or temporal population comparison;
- burden, resource-use, cost, or cost-bearer estimate;
- evidence inventory or pooled summary;
- data-collection infrastructure or dataset;
- data-quality rule, survey-design change, or data-fitness warning;
- implementation finding or collection guidance;
- practice inventory, quality concern, or research priority;
- guidance need or unresolved methodological question.

Record status separately from output type. Status can be proposed, draft, experimental, selected by the study, established for a jurisdiction, planned, collected but not yet analyzed in the report, or recommended for more testing.

### 10. Interpretation and limitation

An **interpretation** is a concise report-level synthesis. It can contain:

- the authors' main conclusion;
- a qualifier from the methods or results;
- the population and context to which it applies;
- a stated limitation or unresolved question.

Also record competing explanations when the design cannot distinguish them. For example, a difference between EQ VAS scores within one reported profile can reflect omitted health content, response-scale heterogeneity, or both. State the identification limit. Do not choose one mechanism without evidence.

Keep author interpretation separate from an ontology curator's uncertainty. This separation is important when a paper uses strong terms such as *valid*, *representative*, or *best* but also reports scope limits.

## Main relations

The following relations are sufficient after three rounds:

```text
research report REPORTS study activity
research report ANALYZES source dataset or analysis cohort
analysis cohort DERIVED_FROM source dataset or collection wave
research report SHARES_EVIDENCE_WITH research report
study activity HAS_PURPOSE purpose
study activity DRAWS_ON evidence source
study activity USES method
study activity TARGETS measurement artifact
study activity USES measurement artifact AS artifact role
instrument version VERSION_OF instrument family
instrument HAS_COMPONENT component
observation PRODUCED_BY instrument or component
observation DESCRIBES person or referent
derived outcome DERIVED_FROM source observation or outcome
derived outcome USES transformation artifact
population summary SUMMARIZES source dataset or analysis cohort
burden or cost outcome USES population scaling, weights, assumptions, and perspective
value set SCORES profiles from an instrument version
value set BASED_ON preference evidence
evaluation ASSESSES target
evaluation ASSESSES_PROPERTY property
comparison COMPARES objects ON comparison basis
study activity PRODUCES output
interpretation QUALIFIES study activity, evaluation, comparison, or output
```

These relations are conceptual guidance. They do not require a graph database or a fixed serialization.

## Minimum useful paper application

For each new paper, record these items in clear prose or a small table:

1. contribution and completion stage;
2. purpose and measurement-chain layer;
3. evidence source, population, place, timing, and perspective;
4. source study, dataset, analysis cohort, and overlap with other reports when known;
5. measurement artifacts and their study roles;
6. outcome derivation and provenance when it affects interpretation;
7. main methods and comparisons;
8. evaluation properties;
9. output and short interpretation;
10. main limits, competing explanations, uncertainty, or metadata issue.

Use **not applicable** when a facet does not apply. Use **not reported in the supplied paper** when the information should exist but is absent. Do not infer facts from the journal, author affiliation, or cited literature.
