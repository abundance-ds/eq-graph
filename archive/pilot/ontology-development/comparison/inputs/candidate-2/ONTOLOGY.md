# Candidate 2 ontology after round 3

## Purpose and boundary

This ontology describes how a paper studies a health or quality-of-life measure. It supports comparison of research purpose, research objects, populations, methods, evaluation criteria, outputs, and limits.

The ontology does not copy bibliographic data from the structured paper record. It does not represent each numerical result or each claim and citation. It records only the result level that a researcher needs to understand what the study contributes and when that contribution applies.

The elements below form an open research description. They are not a fixed form. A paper can use an element more than once. An element can be omitted when it does not apply.

## Core elements

### 1. Study contribution

Record one or more research roles.

- **Instrument development:** develops or revises an instrument, item, label, response scale, or descriptive system.
- **Translation and cultural adaptation:** produces or tests a language or cultural version of an instrument.
- **Valuation:** elicits preferences and produces or tests a value set.
- **Measurement-property evaluation:** evaluates how a measure performs.
- **Conceptual or content evaluation:** develops a construct framework or tests content coverage.
- **Method evaluation:** compares valuation, scoring, mapping, analysis, or other research methods and tests their effect on estimates.
- **Outcome or decision application:** uses a measure or score to study health, groups, interventions, costs, or decisions.
- **Population or burden estimation:** uses measures and other inputs to estimate population norms, inequality, disease burden, resource use, or societal cost.
- **Implementation or feasibility study:** tests how a measure or data-collection process works in routine practice or a pilot service.
- **Use or practice study:** studies how people or organizations use measures, data, or methods.
- **Evidence synthesis:** reviews and combines evidence from earlier studies or trials.
- **Resource or protocol description:** describes planned or active data infrastructure and its methods.

Also record the **evidence status**. Useful values are completed primary study, secondary analysis, decision-model analysis, evidence synthesis, and protocol or resource description. A paper can have more than one status when it joins data or methods with different origins. Do not treat a protocol as a completed outcome study.

### 2. Focal research object

Identify the exact object under study and its role in the paper.

Possible object types are:

- an instrument family or named version;
- a language, country, proxy, or administration version of an instrument;
- a descriptive system, bolt-on, dimension, item, response scale, recall period, visual analogue scale, or utility index;
- a value set and its valuation model;
- a conceptual framework;
- a valuation task, scoring rule, mapping function, analysis method, or evidence-use practice;
- a dataset, survey infrastructure, collection workflow, or implementation strategy;
- a population norm, inequality measure, disability weight, burden measure, cost category, or economic-burden model;
- a study-defined outcome, group, model input, intervention, decision model, or decision output when its definition is material to the paper.

For each object, record **focal**, **comparator**, **reference measure**, **input**, **output**, or **context only**. Record an origin or transformation relation when one object revises or derives from another. Examples are `EQ-5D-Y-5L revises EQ-5D-Y-3L`, `an Arabic version is translated and adapted from a UK English source`, `a mapping function predicts EQ-5D values from SF-12`, and `a value set assigns preference weights to health states from a descriptive system`.

Do not merge a descriptive system with its value set. A paper can evaluate item responses without evaluating utility scores. A different paper can value the same descriptive system without testing its measurement properties.

### 3. Research question and intended use

Record the practical question in one short statement. Then record the intended use or decision context. Examples are health status measurement, quality-adjusted life-year estimation, health technology assessment, population monitoring, clinical trials, clinical care, routine data collection, and health or social care evaluation.

Keep intended use separate from observed use and pilot use. A survey of health technology assessment staff describes current practice. An instrument development paper proposes a future use. A single-site implementation pilot tests a process but does not establish system-wide feasibility.

### 4. People, evidence units, and context

Separate these parts:

- **Sampled evidence source:** the people, documents, trials, or records that directly supply data.
- **Source role:** self-report respondent, proxy, caregiver, care recipient, preference respondent, practitioner, expert stakeholder, implementation participant, qualitative informant, study, or trial.
- **Target population or system:** the people, decisions, or settings to which the paper intends to apply the output.
- **Valuation or reporting perspective:** whose health is described and whose preferences or report are used.
- **Context:** age, health or care status, geography, language, culture, care setting, and relevant time period.
- **Sampling and recruitment:** probability, quota, purposive, convenience, panel, network, or evidence-search method.
- **Representativeness status:** design target, author claim, demonstrated comparison, or clear limit.
- **Participation flow:** eligible, approached, consented, completed, followed up, included, or excluded, with the correct denominator when this affects interpretation.
- **Analysis population:** the observations retained after study-specific quality controls, missing-data rules, and analytic exclusions.

This separation is necessary when adults value a hypothetical child's health, when staff give personal views about agencies, when a dyadic sample is analyzed at the individual level, or when trials rather than participants are the evidence units.

### 5. Study design and data generation

Record:

- primary data, secondary data, literature or registry records, or a planned resource;
- quantitative, qualitative, or combined methods;
- cross-sectional, repeated measure, longitudinal, multi-phase, or evidence-synthesis design;
- administration mode and report type when these affect interpretation;
- focal tasks, measures, comparators, and data outputs;
- allocation, order randomization, blocking, or quality-control procedures when they are important to the study question;
- routine workflow, collection schedule, and implementation setting when these are under evaluation;
- data-quality gates, data-editing rules, missing-data handling, and the stage at which each rule changes the analysis population.

Use a **study component** when one paper contains samples, phases, datasets, tasks, or models with different evidence sources, targets, timing, or outputs. Keep the components under one paper application. Do not split a paper only because it reports many analyses. Record which component supplies each result.

Also record **evidence provenance and overlap**. Name the source study, resource, or component when a paper reuses, filters, pools, or extends earlier data. State whether samples are mutually exclusive, partly overlapping, or the same people when the paper supplies this information. A new analysis of the same respondents is a new contribution, but it is not independent evidence from a new sample.

### 6. Derivation and compatibility

Record the shortest derivation chain that explains the research object or result. The chain can include:

- source instrument to translated or adapted version;
- item responses to a utility score through a named value set;
- source measure to mapped responses or scores through a mapping function;
- utility inputs to quality-adjusted life-years, incremental estimates, or decision outputs through a decision model;
- one or more datasets to a pooled analysis;
- survey responses to an analysis set through quality-control and exclusion rules;
- prevalence, use, cost, disability-weight, or preference inputs to a burden or cost estimate.

At each material step, record compatibility conditions. These can include population, country, language, instrument version, recall period, value-set source, administration mode, time period, task framing, anchor definition, and the assumed form of time preference. Do not treat a derived score as directly observed data. Do not treat agreement at one step as proof of interchangeability in all settings.

### 7. Evaluation and analysis

Record the evaluation focus before the analysis method.

Measurement-property terms in this batch include:

- feasibility and missing response;
- floor and ceiling effects;
- reliability, agreement, and measurement error;
- content, construct, convergent, and known-group validity;
- responsiveness;
- informativity or use of response categories;
- item discrimination and thresholds;
- differential item functioning;
- ceiling reduction or added discriminatory value after an instrument extension;
- response burden, acceptability, retention, and collection feasibility.

Other evaluation focuses include:

- label comprehension, severity ordering, and preference between versions;
- model coefficient significance and monotonicity;
- logical consistency, prediction error, fit, agreement, and sensitivity analysis;
- translation equivalence, severity ordering, comprehension, and cultural suitability;
- agreement between methods and the downstream effect of a method or score choice;
- conceptual coverage and framework alignment;
- patterns in use, data quality concerns, and research priorities;
- frequency and suitability of analysis methods;
- population-norm comparability, inequality, reporting heterogeneity, and residual content coverage;
- survey data integrity, quota achievement, missingness, duplicate or bot detection, and response consistency;
- cost coverage, burden attribution, and sensitivity to disability weights or monetary valuation assumptions.

Record only analysis families that explain the design or model choice. Examples are thematic framework analysis, random-effects evidence pooling, item response theory, mixed logit, hybrid valuation model, Markov decision model, cost-of-illness analysis, inequality decomposition, and descriptive regional comparison. Record prespecified hypotheses, anchors, thresholds, known-group definitions, and selection rules when they materially affect interpretation.

Do not use one generic positive or negative result for all measurement properties. A measure can have good known-group validity and poor test-retest reliability in the same study.

### 8. Output and conclusion scope

Record the main research product. Examples are a new instrument version, a translated version, a value set, a conceptual framework, a measurement-property profile, a method-comparison profile, population norms, an inequality or burden profile, a decision-impact estimate, implementation guidance, an evidence map, a research-priority landscape, or a reusable dataset design.

Then record a short conclusion with its scope. The conclusion can state a comparative direction or an important qualification. It must not become a detailed claim-evidence graph.

For an artifact, record whether it is a candidate, final product in the paper, external protocol, or future product that still needs validation. A study-final translation is not automatically a psychometrically validated measure. A pilot result is not automatically evidence of full-scale implementation.

### 9. Rigor, applicability, and transparency

Record features that change confidence or transferability:

- interviewer training, data-quality checks, duplicate review, a priori hypotheses, or saturation procedures;
- sample and setting limits;
- method assumptions and omitted properties;
- mismatch of recall periods, respondent perspectives, instruments, health states, samples, or value sets;
- attrition, exclusions, missing denominators, pooled-data differences, and model-input uncertainty;
- whether a quality-control or exclusion rule uses the focal outcome, can remove the phenomenon under study, or lacks a sensitivity analysis;
- data and code access conditions;
- a reported relationship between the research team or funder and the research object, when this is relevant to meta-research.

Do not infer bias from a disclosed relationship. Record the relationship and any reported safeguard, such as a statement that the funder had no role.

### 10. Uncertainty and source conflict

For each uncertain item, record its type:

- not reported;
- not applicable;
- author interpretation;
- ontology curator interpretation;
- conflict within the supplied paper;
- limit caused by the supplied material.

Do not silently resolve an internal conflict. Preserve both reported values and identify the location of the conflict.

## Main relations

The ontology uses plain-language relations. These relations are useful for future graph design, but they do not prescribe a database schema.

- A paper **has research role**.
- A paper **studies**, **develops**, **revises**, **values**, **evaluates**, **compares**, **reviews**, or **describes** an object.
- An object **derives from**, **is translated or adapted from**, **is a component of**, **is added to**, **maps to**, **produces**, **supplies an input to**, or **is scored by** another object.
- A study **draws evidence from** a source and **targets** a population, setting, or decision.
- A study **reuses**, **filters**, **pools**, **extends**, or **overlaps with** an earlier study component or dataset.
- A respondent **reports own health**, **reports another person's health**, or **values a hypothetical health state**.
- A study or study component **uses task or measure**, **assesses property or criterion**, and **uses analysis family**.
- A study **produces output**, **supports intended use**, and **has applicability limit**.
- A workflow **collects measure at** a setting and time, and **has participation flow**.
- An analysis set **results from** stated quality-control, exclusion, and missing-data rules.
- An uncertainty **concerns** an element and **is supported by** a stated part of the paper.

## Comparison procedure

For two papers, compare in this order:

1. Compare research role and evidence status.
2. Compare the exact research objects and their roles.
3. Compare the practical question and intended use.
4. Compare sampled evidence sources, target populations, and perspectives.
5. Compare evidence provenance, sample overlap, and analysis populations.
6. Compare study components, design, tasks, and data outputs.
7. Compare derivation chains and compatibility conditions.
8. Compare the properties or criteria assessed.
9. Compare the main output and its maturity.
10. Compare applicability limits and unresolved uncertainty.

This order prevents false comparisons. For example, a value-set study and a descriptive-system reliability study both concern EQ-5D, but they answer different questions.
