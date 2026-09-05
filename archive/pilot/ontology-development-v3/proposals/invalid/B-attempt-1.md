# EuroQol research ontology proposal: packet B

## 1. Purpose and evidence boundary

This ontology is for search, comparison, and synthesis of EuroQol research. Its central unit is an exact research fact in a stated context. It must let a researcher find facts such as these:

- a study is a **valuation study**;
- the study valued **EQ-5D-5L**;
- it used **cTTO** and a duration-free DCE under a specified EQ-VT version;
- its preferred model was a **hybrid heteroskedastic Tobit model censored at -1**;
- its sample was a defined national adult population;
- it produced a native value set for a stated country; and
- a reported health-state value, model comparison, psychometric result, or limitation applies only in its stated context.

The evidence for this proposal is the 50 fixed summaries in packet B and the 50 supplied competency questions. A summary is an evidence record about a publication. It is not the publication itself. The examples below use only facts stated in the summaries and identify the applicable summary.

The ontology has two linked scopes:

1. The research-evidence scope represents publications, studies, samples, instruments, methods, analyses, products, outcomes, and findings.
2. The research-administration scope represents funded projects, applications, people, organizations, working groups, budgets, membership, citations, access status, identity resolution, and graph-ingestion provenance. Most of this second scope needs linked data that is not in the summaries.

The ontology does not assume that each publication reports one study, that each study produces one product, or that each project has one publication. It does not force a sample, model, or value set onto conceptual papers, reviews, or protocols.

## 2. Design principles

### 2.1 Keep four kinds of information separate

| Kind | Meaning | Example from the packet | Rule |
|---|---|---|---|
| Source term | Wording used in a summary or its reported source | “heteroscedastic censored hybrid model”; “tariff”; “misery score/index” | Store the text, source summary, and local context without silent rewriting. |
| Canonical term | The preferred concept used for retrieval | composite time trade-off; EQ-5D-5L; native value set | Link source terms to it with a typed and reviewable mapping. |
| Classification | An assignment of a record to a controlled class | valuation study; population-norms study; experimental instrument version | Store who or what made the assignment and whether it was source-stated or curated. |
| Derived analytic | A result calculated over records | median publication lag; top-decile output share; co-authorship community | Store the rule, inputs, query boundary, parameters, and calculation date. Do not present it as a source claim. |

These kinds can agree, but they are not interchangeable. For example, a source can call a product a “tariff”; the canonical product class can be `ValueSet`; and `NativeValueSet` can be its classification. A later count of native value sets by country is a derived analytic.

### 2.2 Keep direct facts and evidence together

Each important fact has a semantic relation and an evidence record. The evidence record contains:

- the source summary identifier;
- the publication identifier when given;
- the summary section or other locator when given;
- the exact source wording when it is important;
- whether the statement is reported, planned, recommended, not produced, not reported, unclear, or conflicting;
- the extraction or curation agent and date; and
- confidence in the mapping, not confidence in the scientific result.

This prevents these errors:

- treating a planned method in a protocol as a completed method;
- treating “not reported” as “no”;
- treating a project identifier in packet metadata as proof of an explicit funding acknowledgement;
- treating an author interpretation as a measured cause; and
- treating two similar instrument names as the same version without evidence.

### 2.3 Use semantic relations, not vague links

The ontology uses relations such as `REPORTS_STUDY`, `USES_ELICITATION_METHOD`, `PRODUCES_VALUE_SET`, `USES_VALUE_SET_FOR_SCORING`, `COMPARES_WITH_VALUE_SET`, and `ACKNOWLEDGES_FUNDER`. It does not use one undifferentiated “related to” or “has” relation.

### 2.4 Make time and scope explicit

Publication date, study fieldwork, follow-up, project period, membership period, affiliation period, access observation, citation count, and project status are different temporal facts. A claim that a study is “ongoing right now” must be evaluated against a dated status observation. A citation count or open-access status also needs a provider and an as-of date.

## 3. Main concepts

### 3.1 Evidence and research activity

| Concept | Meaning to a EuroQol researcher | Important fields or distinctions |
|---|---|---|
| `SummaryRecord` | The fixed secondary evidence record supplied to this ontology task | Summary ID, summary hash, title, source path as reported, source hash as reported. |
| `Publication` | A citable research output, such as an article, review, or protocol paper | DOI or other identifier, title, publication type, date, journal, access observations. |
| `Study` | A research activity with an aim and design | Study type, status, setting, dates, samples, data collections, methods, analyses. |
| `StudyProtocol` | A plan for a study or study phase | Planned sample, methods, analyses, ethics status, and explicit absence of results. It can be reported by a protocol publication. |
| `Dataset` | A reusable body of data | Name, origin, collection period, population, access conditions. It is separate from the study that first collected it. |
| `DataCollectionWave` | One collection period or time point in a dataset or study | Date range, sample stage, instrument administration, mode, and follow-up relation. |
| `EvidenceAssertion` | Provenance for one domain fact | Subject, semantic relation, object or literal value, evidence locator, assertion status. |

A publication can report multiple studies or samples. S019 reports a direct comparison that uses two Trinidad and Tobago samples. A project can support multiple publications: project 341-RA appears on S019 and S070. A protocol publication such as S065 describes planned data collection and does not become a completed study merely because it has a DOI.

### 3.2 Projects, awards, and research administration

| Concept | Meaning | Important distinctions |
|---|---|---|
| `GrantApplication` | An application or proposal before an award decision | Applicant roles, submission date, abstract, requested budget, decision. |
| `FundingAward` | The formal award that provides approved funding | Award identifier, approved amount, currency, approval date, funder, award status. “Grant” is retained as a source term and is not automatically made a synonym of project. |
| `FundedProject` | The research activity supported by one or more awards | Project identifier, title, abstract, start/end dates, status observations, working group. |
| `ProjectOutputLink` | A qualified claim that a publication or product is an output of a project | Evidence basis, confidence, link date, and curator. |
| `ProjectRole` | A dated role held by a person on an application or project | Applicant, PI, co-investigator, supervisor, student recipient, or another exact source role. |
| `WorkingGroup` | An administrative or topical EuroQol group | Name, validity period, projects, and dated person membership when available. |
| `BudgetAmount` | One monetary fact | Amount, currency, approved/requested/actual status, and date. Currency conversion is a derived step. |

An acknowledgement, a project-output link, and a funding award are separate facts. `ACKNOWLEDGES_FUNDER` does not by itself mean `OUTPUT_OF_PROJECT`. A packet project ID is evidence of an association in the packet, but an explicit funding statement is stronger evidence for funding.

### 3.3 People and organizations

| Concept | Meaning | Important distinctions |
|---|---|---|
| `Person` | A resolved researcher or other contributor | Stable local identity, source names, external identifiers when linked. |
| `Authorship` | A person's ordered contribution as an author of a publication | Author position and source name. It is not membership or a project role. |
| `MembershipEpisode` | A person's membership during a stated period | Organization or working group, start/end, evidence. This supports time-correct member questions. |
| `AffiliationEpisode` | A person's relationship with an organization during a stated period | Organization, role or department when stated, dates, source. |
| `Organization` | University, hospital, funder, company, agency, or other body | Canonical name, source names, organization type, location. |
| `IdentityResolutionEvent` | An auditable merge, override, split, or skip decision | Input profiles, output identity, action, rule, evidence, operator, date, reason. |

`Member`, `PI`, `author`, `applicant`, and `supervisor` are roles with context and often time. They are not permanent person types.

### 3.4 Population, sample, and setting

| Concept | Meaning | Important fields or distinctions |
|---|---|---|
| `PopulationDefinition` | The group to which a study aims to apply | Geography, age bounds, life stage, condition, inclusion/exclusion criteria, general-population or patient status. |
| `Sample` | The people who took part in a study or wave | Recruitment method, setting, respondent role, and links to staged counts. |
| `SampleStage` | One count in the flow from recruitment to analysis | Invited, recruited, interviewed, completed, excluded, retained, paired, or another exact stage; count and reason. |
| `SampleGroup` | A subgroup, arm, cohort, or comparison group | Group definition, membership rule, sample stage, time point. |
| `Condition` | A health condition or condition family studied, excluded, or used as a known group | Exact source label, canonical label, relation type, and evidence. |
| `LifeStage` | A controlled age or developmental category | Infant/toddler, child, adolescent, adult, older adult, plus exact numeric age bounds when stated. |
| `GeographicArea` | Country, region, city, or study location | Geographic level and role, such as sample residence, fieldwork site, or product jurisdiction. |

The ontology must not replace exact age bounds with only a life-stage label. It must also distinguish `STUDIES_CONDITION`, `EXCLUDES_CONDITION`, `RECRUITS_FROM_SETTING`, and `MENTIONS_CONDITION`.

### 3.5 Instruments and versions

| Concept | Meaning | Important fields or distinctions |
|---|---|---|
| `InstrumentFamily` | A durable measure family | EQ-5D, EQ-5D-Y, EQ-TIPS, EQ-HWB, or a comparator instrument. |
| `InstrumentVersion` | A version that researchers can administer, develop, value, or compare | Target population, level count, revision number, official or experimental status, release status. |
| `LanguageVersion` | A stated language form of an instrument version | Language, country adaptation when stated, validation status only when stated. |
| `ReporterVersion` | A self-report or proxy form | Self-report, proxy version 1, proxy version 2, or another exact form. |
| `Dimension` | A named descriptive-system dimension in a specified version | Source label, canonical construct mapping, order, examples, and version scope. |
| `ResponseLevel` | One ordered response option in a version and language | Level number, exact label, order, and anchor role. |
| `InstrumentComponent` | A component that is not a descriptive-system dimension | EQ VAS is represented here and not confused with a VAS preference-elicitation method. |
| `InstrumentExtension` | A bolt-on dimension or other extension to a base instrument | Base version, added dimension, development/test status, target condition. This concept is required by Q39, but the packet does not supply a condition-specific bolt-on instance. |

Version identity is composite. `EQ-5D-Y-5L`, experimental Indonesian proxy version 1, and a self-report EQ-5D-Y-5L are not one interchangeable object. Likewise, the source terms `EQ-HWB-S` in S033 and `EQ-HWB-9` in S078 remain separate until evidence establishes their relationship.

### 3.6 Instrument use and reporter perspective

`InstrumentAdministration` is an independently queryable context. It links:

- one study or wave;
- one exact instrument, language, and reporter version;
- one sample or sample group;
- an administration mode, such as face-to-face interviewer administration, online self-completion, paper self-completion, or computer-assisted personal interview;
- a reporter role, such as child self-report or parent/caregiver proxy report;
- a proxy perspective, such as proxy-person or proxy-proxy;
- a recall period;
- an instrument order when it can affect results; and
- planned or completed status.

This context is needed because S021 finds material differences between online unsupervised and face-to-face cTTO, S042 uses proxy version 2 with a proxy-person perspective, and S085 uses proxy version 1 and explicitly distinguishes it from version 2.

### 3.7 Methods and analyses

| Concept | Meaning | Examples supported by the packet |
|---|---|---|
| `StudyDesign` | The overall design classification | valuation study, longitudinal observational study, qualitative study, systematic review, protocol, cross-sectional survey. |
| `SamplingMethod` | How participants were selected | quota sampling, probability sampling, online panel, convenience sampling, purposive sampling. |
| `PreferenceElicitationMethod` | The exact task used to elicit preferences | cTTO, duration-free DCE, DCE with duration, DCE-death, DCE-duration, split-triplet DCEd, kaizen task, paired comparison, standard gamble, person trade-off, personal utility function elicitation. |
| `ValuationProtocol` | A named procedure and version that organizes valuation tasks | MVH protocol, Paris protocol, EQ-VT, EQ-VT 2.0, EQ-VT 2.1, EQ-VT 2.6.1. An unversioned EQ-VT fact stays unversioned. |
| `QualitativeMethod` | A qualitative collection or analysis method | focus group, cognitive interview, think-aloud interview, framework analysis, thematic analysis. |
| `MeasurementProperty` | The property that a study evaluates | content validity, construct validity, convergent validity, known-groups validity, reliability, responsiveness, agreement, feasibility, ceiling/floor, informativity. |
| `QualityControlProcedure` | A rule or process used to inspect data collection | interviewer training, task-time flag, 55555 inconsistency flag, feedback module, bot or duplicate check. |
| `StatisticalModelSpecification` | The exact model fitted to stated data for a stated purpose | conditional logit; mixed logit; random-intercept model; heteroskedastic Tobit; hybrid heteroskedastic Tobit censored at -1. |
| `ModelFit` | One application of a model specification to data | Input data, estimand, software when reported, sensitivity sample, fit criteria, result, and selected/not-selected role. |

#### Exact cTTO representation

`cTTO` is a canonical preference-elicitation method, with “composite time trade-off” as its preferred label and `cTTO` as an alias. It has two stated parts when the source supports them:

- conventional TTO for better-than-dead states; and
- lead-time TTO for worse-than-dead states.

The ontology records task horizon, state design, iteration rule, administration mode, feedback, and censoring separately. It does not treat conventional TTO, lead-time TTO, and cTTO as synonyms.

#### Exact hybrid-model representation

`HybridModel` is a controlled model family, but “hybrid model” alone is not an adequate record. A model specification can state:

- the data sources combined, such as cTTO and DCE;
- the component likelihood or model families;
- the scale-link parameter;
- main effects or interactions;
- random effects;
- heteroskedasticity;
- censoring and its bound;
- constraints;
- time-preference form; and
- whether the model was preferred, a sensitivity model, or rejected.

Thus the preferred UAE model in S004 is represented as a hybrid model that combines cTTO and DCE, is heteroskedastic, uses a Tobit component, and is censored at -1. The exact source label is also retained.

### 3.8 Products

`ResearchProduct` is an abstract parent only. Each product must have a useful subtype.

| Product subtype | Meaning | Required distinctions |
|---|---|---|
| `ValueSet` | A rule or set of values used to assign preference-based values to health states | Native, crosswalk, mapped/anchored, or other stated derivation; exact instrument version; preference population; jurisdiction; model; scale and range. |
| `InstrumentRelease` | A defined instrument version or revision | Experimental/official status, dimensions, levels, target population, reporter and language forms. |
| `ValuationProtocol` | A reusable valuation procedure | Protocol family, version, intended instrument, task components. |
| `PopulationNormSet` | Reference distributions or scores for a defined population | Instrument/version, country, period, population, sample, scoring value set, stratifiers. |
| `ScoringAlgorithm` | A formula or algorithm that produces a score | Inputs, output scale, parameters, source study, validation status. |
| `Dataset` | A reusable research data product | Collection scope, waves, access conditions, provenance. |
| `GuidanceOrCriteriaSet` | A structured methodological recommendation | Intended use, criteria, evidence basis, status. |

#### Native value set versus crosswalk

A native value set is estimated from preferences elicited for the target descriptive system. A crosswalk applies a mapping to values from another descriptive system. A mapped or anchored value set uses an explicit mapping or anchoring function and must name both source and target scales.

The ontology uses separate relations:

- `PRODUCES_VALUE_SET` for a study that creates a product;
- `USES_VALUE_SET_FOR_SCORING` for a study that scores observations;
- `COMPARES_WITH_VALUE_SET` for a methodological comparison;
- `REFERENCES_VALUE_SET` for a textual or bibliographic reference; and
- `SUPERSEDES_VALUE_SET` only when a source explicitly states replacement or succession.

This prevents a paper that uses or compares a value set from being classified as its producer.

### 3.9 Outcomes, observations, comparisons, and findings

| Concept | Meaning | Important fields |
|---|---|---|
| `OutcomeConcept` | What was measured or estimated | EQ-5D index, EQ VAS, dimension response, LSS, QALY, agreement, responsiveness, utility for state 55555. |
| `OutcomeObservation` | One value of an outcome in context | Numeric value or category, unit, statistic type, denominator, time point, sample group, instrument/version, scoring product. |
| `Comparison` | A structured contrast | Compared entities, same/different sample, outcome, direction, effect estimate, uncertainty, time point. |
| `Finding` | One atomic reported conclusion or result | Finding type, subject, relation, object/value, population, method, time, evidence, assertion status. |
| `Limitation` | A source-reported limit on interpretation | Target study or finding, exact text or canonical category, evidence. |
| `EvidenceGap` | A source-reported absence of evidence or planned future need | Target concept, scope, source, and whether it means not studied, not reported, or not produced. |

Useful finding subtypes are estimate, association, comparison, measurement-property result, qualitative theme, recommendation, interpretation, and evidence gap. A finding must not be only an unclassified free-text “outcome”.

Health-state codes such as 55555 are always linked to an exact instrument version. The same string is not globally meaningful without that context. A statistic also keeps its type: mean, median, proportion, correlation, ICC, kappa, coefficient, utility, effect size, SRM, AUC, confidence interval, or another exact source type.

## 4. Important relations

| Relation | From | To | Meaning |
|---|---|---|---|
| `REPORTS_STUDY` | Publication | Study | The publication reports the study. |
| `DESCRIBES_PLANNED_STUDY` | StudyProtocol | Study | The protocol describes a study that is planned at the cited time. |
| `USES_DATASET` | Study | Dataset | The study analyzes the dataset. |
| `HAS_WAVE` | Study or Dataset | DataCollectionWave | The wave belongs to that activity or dataset. |
| `HAS_SAMPLE` | Study or Wave | Sample | The sample took part in that context. |
| `HAS_SAMPLE_STAGE` | Sample | SampleStage | The count applies at one flow stage. |
| `ADMINISTERS_INSTRUMENT` | InstrumentAdministration | InstrumentVersion | The exact version was administered. |
| `ADMINISTERED_TO` | InstrumentAdministration | Sample or SampleGroup | The recipient group. |
| `USES_LANGUAGE_VERSION` | InstrumentAdministration | LanguageVersion | The stated language form. |
| `USES_REPORTER_VERSION` | InstrumentAdministration | ReporterVersion | The stated self/proxy form. |
| `USES_ELICITATION_METHOD` | ValuationExercise | PreferenceElicitationMethod | The exact task used. |
| `USES_PROTOCOL_VERSION` | ValuationExercise | ValuationProtocol | The named protocol version, when stated. |
| `ELICITS_PREFERENCES_FROM` | ValuationExercise | PopulationDefinition or Sample | The preference source. |
| `VALUES_INSTRUMENT_VERSION` | ValuationExercise | InstrumentVersion | The health-state system being valued. |
| `USES_PERSPECTIVE` | ValuationExercise | Perspective | Self, another adult, a child of stated age, or another exact frame. |
| `FITS_MODEL` | Analysis | ModelFit | The analysis applies the model. |
| `USES_INPUT_DATA` | ModelFit | ValuationExercise or Dataset | The observations fitted by the model. |
| `SELECTS_PREFERRED_MODEL` | Study | ModelFit | The source selects this fit, with stated criteria. |
| `PRODUCES_PRODUCT` | Study or Project | ResearchProduct | The evidence supports product creation. A typed subrelation is preferred. |
| `USES_PRODUCT_FOR_SCORING` | Study | ValueSet or ScoringAlgorithm | The product generates study scores. |
| `EVALUATES_PROPERTY` | Study | MeasurementProperty | The study evaluates the property. |
| `REPORTS_FINDING` | Study or Publication | Finding | The source reports the atomic finding. |
| `APPLIES_TO_POPULATION` | Finding or Product | PopulationDefinition | The stated applicability context. |
| `SUPPORTED_BY_AWARD` | FundedProject | FundingAward | The award supports the project. |
| `HAS_PROJECT_ROLE` | Person | ProjectRole | The person has the dated role. |
| `OUTPUT_OF_PROJECT` | Publication or Product | FundedProject | A qualified output link supports the relation. |
| `ACKNOWLEDGES_FUNDER` | Publication | Organization | The publication explicitly acknowledges the funder. |
| `AUTHORED_BY` | Publication | Authorship | Links the work to ordered authorship. |
| `AFFILIATED_DURING` | Person | AffiliationEpisode | The person has a dated organization link. |
| `MEMBER_DURING` | Person | MembershipEpisode | The person has a dated membership link. |
| `CITES` | Publication | Publication | A direct citation edge from a defined citation source. |
| `REFERENCES_PRODUCT` | Publication | ResearchProduct | The text or citation identifies the product. |
| `ENTERED_GRAPH_BY` | Record | IngestionEvent | Records the graph entry route and source. |
| `SUPPORTED_BY_ASSERTION` | Domain fact | EvidenceAssertion | Connects a fact to its provenance. |

All of these relations are optional and can be many-to-many. Their absence does not prove a negative.

## 5. Controlled classifications and exact value families

### 5.1 Study type

Use multiple study-type assignments when the evidence supports them. The initial controlled family is:

- valuation study;
- instrument-development study;
- content-validity study;
- psychometric or measurement-property study;
- population-norms or reference-value study;
- method-development study;
- method-comparison study;
- systematic review or evidence synthesis;
- qualitative stakeholder or preference study;
- observational HRQoL study;
- implementation or feasibility study;
- study protocol; and
- randomized-trial methods review.

Publication type remains separate. A systematic review is both a publication type and a study design only when the evidence supports both assignments. A protocol publication reports a planned study and is not classified as a completed valuation study.

### 5.2 Instrument status and form

Controlled axes include:

- status: official, experimental, planned, superseded, or not reported;
- target: adult, youth, infant/toddler, caregiver, or broader health and wellbeing;
- level structure: 3L, 4L, 5L, or exact item count when levels do not apply;
- reporter: self-report, proxy version 1, proxy version 2, or unspecified proxy;
- language: exact source language label; and
- revision: exact version string, such as EQ-TIPS V2.0 or V3.0.

The source controls each assignment. For example, S061 states that EQ-TIPS V2.0 was the experimental EQ-TIPS-3L and that a five-level version was not available for testing. S065 describes experimental EQ-TIPS-5L V3.0. These are distinct instrument versions.

### 5.3 Preference-elicitation method

The hierarchy keeps exact methods visible:

- time trade-off
  - conventional TTO;
  - lead-time TTO;
  - composite time trade-off, or cTTO;
- discrete choice experiment
  - duration-free DCE;
  - DCE with duration, or DCEd;
  - DCE-death;
  - DCE-duration;
  - split-triplet task;
  - kaizen task;
  - paired comparison;
- standard gamble;
- person trade-off;
- personal utility function elicitation;
- best-worst scaling; and
- visual analogue scale valuation.

EQ VAS is an outcome component, not automatically a visual analogue scale valuation method.

### 5.4 Statistical model

Do not use a single list that loses model structure. Use a model-family classification plus facets:

- family: linear regression, random-intercept model, Tobit, conditional logit, mixed logit, ordered logit, hybrid model, mapping model, item-response model, factor analysis, or another exact family;
- data source: cTTO, DCE, DCEd, outcomes over time, item responses, or another stated input;
- variance: homoskedastic or heteroskedastic;
- censoring: none reported, left-censored, or another exact rule and bound;
- effects: fixed, random, main effects, interactions, or another stated structure;
- transformation or link: linear, power, scale link, nonlinear time preference, or another exact function;
- constraints and anchoring; and
- study role: candidate, preferred, sensitivity, rejected, or not reported.

### 5.5 Product type

For value sets, control these derivation types:

- native value set;
- crosswalk value set;
- mapped or anchored value set;
- experience-based value set; and
- derivation not reported.

The ontology also records whether a value set is national, which population supplied preferences, which instrument it values, and whether the paper produced, used, or only compared it.

### 5.6 Reporter and perspective

Separate these values:

- respondent role: adult general-public respondent, patient, child/adolescent, caregiver, expert, stakeholder, or another exact role;
- report source: self-report or proxy report;
- proxy form: proxy version 1, proxy version 2, or source-unspecified;
- proxy perspective: how the proxy rates the subject, how the proxy thinks the subject would rate themselves, or source-unspecified;
- valuation perspective: adult self, adult considering another adult, adult imagining self as a child, adult considering a child, child self, child considering another child, or exact source wording; and
- hypothetical subject age.

This detail is necessary for child valuation and self-proxy agreement research.

### 5.7 Assertion and evidence status

Use these controlled statuses:

- observed or completed;
- planned;
- source-reported recommendation;
- explicitly not produced or not tested;
- explicitly absent;
- not reported;
- unclear or conflicting; and
- curator-derived.

For S004, the age reported in the abstract conflicts with the age reported in Results. Both values stay as evidence assertions with `conflicting` status; one is not silently selected.

## 6. Modular study views

These are query views, not mandatory templates.

### 6.1 Valuation-study view

A valuation-study view can join:

`ValuationStudy` -> target `InstrumentVersion` -> `ValuationExercise` -> exact elicitation method and protocol -> preference-source `Sample` -> `ModelFit` -> preferred model -> produced `ValueSet` -> reported state values and range.

Optional detail includes perspective, hypothetical age, language, administration mode, experimental design, interviewer training, quality-control flags, exclusions, anchoring, and sensitivity analyses.

### 6.2 Measurement-property view

A measurement-property view can join:

study -> instrument administration -> population/sample -> property evaluated -> comparator or anchor -> statistic -> finding.

It supports content validity, construct validity, reliability, responsiveness, self-proxy agreement, feasibility, ceiling/floor, and informativity without treating them as one vague outcome.

### 6.3 Instrument-development view

An instrument-development view joins a study to the version developed or tested, its dimensions and response labels, target population, languages, qualitative and quantitative methods, stakeholder groups, proposed changes, and release status. Proposed dimensions and adopted dimensions are different relations.

### 6.4 Population-norms view

A norms view joins a study and `PopulationNormSet` to the exact instrument, scoring value set, country, collection period, target population, achieved sample, weighting, strata, dimension distributions, index/EQ VAS summaries, and comparison periods.

### 6.5 Review view

A review view records databases, search date, eligibility, review registration, included-study count, synthesis method, target instruments, populations, properties, and evidence conclusions. It does not pretend that the review's included studies are direct samples of the review itself.

## 7. Source language, canonicalization, and provenance

### 7.1 Term records

Each `SourceTerm` includes text, language when known, summary, section, entity mentioned, and local meaning. A `TermMapping` connects it to a `CanonicalTerm` and has one of these mapping types:

- exact;
- narrower than;
- broader than;
- related but not equivalent;
- spelling or abbreviation variant; or
- unresolved.

Examples supported by the packet include:

- `cTTO` as an abbreviation of composite time trade-off;
- `DCEd` as an abbreviation of discrete choice with duration in S019;
- `LSS`, “level summary score”, “equally weighted score”, and “misery score/index” as contextual names reported in S054; and
- “tariff” as source wording for a value set in S013 and S022.

Mappings can be scope-specific. A language version can use wording that is conceptually comparable but not a literal lexical equivalent, as S064 reports for EQ-5D-Y-5L labels.

### 7.2 Classification assignments

A `ClassificationAssignment` states:

- the classified record;
- the controlled class;
- whether the class was source-stated, rule-derived, or manually curated;
- evidence and date; and
- rule version when applicable.

This is important for classes such as `methodological literature`, `pure application`, `under-represented population`, and `first-time PI`. These classes drive denominators and must be auditable.

### 7.3 Project-output evidence

Each `ProjectOutputLink` records one evidence basis:

- explicit project identifier in the publication or summary;
- explicit funding acknowledgement;
- structured funder metadata;
- full-text grant mining;
- manual curation; or
- another stated route.

It also records positive, rejected, or unresolved status. Q15 and Q100 depend on this provenance.

## 8. External linked data and derived analytics

### 8.1 External observations

The following records are necessary but are not reliably available in the 50 summaries:

- `ProjectStatusObservation`, with status and as-of date;
- `OpenAccessObservation`, with status, provider, evidence, and date;
- `CitationMetricObservation`, with count, index/provider, and date;
- direct `CitationEdge` records;
- complete grant applications, awards, budgets, roles, working groups, and project periods;
- complete authorship, membership, affiliation, and ORCID links;
- `IdentityResolutionEvent` audit records; and
- `IngestionEvent` records with graph-entry route.

These observations can change. They must not overwrite earlier snapshots.

### 8.2 Derived-analytic record

Every `DerivedAnalytic` contains:

- a named analytic type;
- an exact corpus or project boundary;
- inclusion and exclusion rules;
- denominator definition;
- input record versions and observation dates;
- parameters, such as top-decile rounding or budget band;
- currency and normalization rule when money is involved;
- computation date; and
- output value plus uncertainty when applicable.

Examples include:

- total funded projects and combined approved budget;
- median, IQR, and maximum approved budget;
- share of completed projects with a linked publication;
- time from project start to first linked publication;
- open-access share and trend;
- top-decile PI output concentration;
- co-authorship communities;
- citation comparison between funded and other work;
- inter-project citation flow; and
- topical similarity between a proposal abstract and past projects.

The analytic result links to its input projects, publications, people, and observations. It is never stored as a reported paper finding.

## 9. Competency-question coverage

### 9.1 Answerability categories

- **S — Answerable from supplied summaries:** The packet contains enough evidence for a packet-bounded answer. A transparent calculation over extracted summary facts is allowed.
- **X — Requires external linked data:** The research ontology can answer after it links administrative, bibliographic, identity, access, citation, status, or graph-provenance data that the summaries do not contain completely.
- **U — Unsupported by available evidence:** The packet does not contain the research evidence needed for an answer. Answering from it would invent facts. Additional research publications or equivalent evidence are necessary, not only metadata linkage.

“Answerable” below means answerable within the supplied 50-summary boundary. It does not claim that the packet is the complete EuroQol corpus.

| Question | Required concepts and relations | Category and reason |
|---|---|---|
| **Q41 — Which publications introduced or validated the EQ-VT protocol?** | Publication, Study, ValuationProtocol, protocol version, `INTRODUCES_PROTOCOL`, `EVALUATES_PROTOCOL`, evidence type, finding. | **S.** S002 explicitly introduces and critiques EQ-VT with MVH and Paris. Other summaries report empirical uses and method comparisons. The answer must state that no supplied summary labels a paper as a formal validation unless that exact claim is present. |
| **Q22 — How long after their previous grant did applicant X first publish from it?** | Person, GrantApplication, FundingAward, ProjectRole, prior-award order, ProjectOutputLink, Publication date, derived duration. | **X.** Complete grant history, resolved identity, project dates, output links, and publication dates are external. |
| **Q90 — Which projects produced value sets that later corpus works reference?** | FundedProject, ValueSet, `PRODUCES_VALUE_SET`, Publication, `REFERENCES_PRODUCT` or citation edge, publication date. | **X.** The summaries identify several value sets, but they do not give a complete, resolved product-reference graph. |
| **Q68 — What share of the EQ-5D methodological literature acknowledges EuroQol funding?** | Corpus boundary, methodological-study classification, Publication, `ACKNOWLEDGES_FUNDER`, denominator and share analytic. | **X.** A complete corpus classification and complete acknowledgement extraction are not in the packet. |
| **Q47 — Which members co-authored with researcher X on funded outputs?** | Resolved Person, Authorship, dated MembershipEpisode, ProjectOutputLink, co-authorship relation. | **X.** Complete authorship, identity, membership, and funded-output links are external. |
| **Q40 — Which EQ-5D-5L valuation studies are ongoing right now?** | ValuationStudy, `VALUES_INSTRUMENT_VERSION` EQ-5D-5L, FundedProject, dated ProjectStatusObservation, study dates. | **X.** “Right now” needs current project or study status that the fixed summaries cannot provide. |
| **Q39 — Which conditions have bolt-on dimensions been developed or tested for?** | InstrumentExtension, BoltOnDimension, base InstrumentVersion, Condition, `DEVELOPED_FOR`, `TESTED_IN`, development status. | **U.** S065 says that 13 EQ-5D bolt-ons were administered but does not name them or their conditions. S078 suggests climate-related or psychosocial bolt-ons but does not report their development or testing. |
| **Q77 — How concentrated is output among PIs (share held by the top decile)?** | Resolved PI roles, ProjectOutputLink, output-count rule, PI population, top-decile rule, concentration analytic. | **X.** Complete PI and output data are external. |
| **Q36 — Has proxy-vs-self-report agreement been studied for EQ-5D-Y?** | InstrumentVersion and ReporterVersion, Sample dyad, proxy perspective, self/proxy Comparison, agreement statistic, Finding. | **S.** S069 and S085 directly report self-proxy agreement for EQ-5D-Y forms in stated populations. |
| **Q93 — Which first-time PIs published from their first grant?** | Person, dated PI roles, ordered awards, first-time classification, ProjectOutputLink, Publication. | **X.** It needs complete grant histories, identities, and outputs. |
| **Q21 — Has applicant X co-authored with EuroQol members before, and with whom?** | Applicant identity, Authorship, dated MembershipEpisode, publication date, prior-to-application filter. | **X.** Identity, membership, and complete authorship history are external. |
| **Q56 — Which supervisors and institutions ran student grants?** | Student-grant classification, ProjectRole for supervisor and student, AffiliationEpisode, Organization, Project. | **X.** The summaries do not provide complete student-grant roles or institutions. |
| **Q1 — How many projects has EuroQol funded in total, and what is the combined approved budget?** | Funder, FundingAward, FundedProject, approved BudgetAmount, project de-duplication, currency rule, totals. | **X.** A complete award ledger and budget data are external. |
| **Q59 — Which open-access papers introduce EQ-HWB?** | Publication, InstrumentVersion/Product, `INTRODUCES_PRODUCT`, dated OpenAccessObservation. | **X.** The packet contains EQ-HWB development work, but open-access status is not complete or consistently stated. |
| **Q12 — Which funded publication is the most cited, and which project produced it?** | Publication, ProjectOutputLink, CitationMetricObservation with provider/date, maximum analytic, Project. | **X.** Citation snapshots and complete project-output links are external. |
| **Q67 — What is a good starter reading list on health-state valuation for children?** | Publication, child-valuation topic, StudyType, elicitation method, evidence-synthesis relation, curated-list analytic with selection rule. | **S.** The packet has a systematic review and empirical or qualitative child-valuation studies. “Good” must be a declared curation rule, not a source fact. |
| **Q33 — Which studies compare EQ-5D-5L and EQ-5D-3L value sets in the same population?** | Study, Sample, two InstrumentVersions, two ValueSets, `COMPARES_WITH_VALUE_SET`, same-sample flag, outcomes. | **S.** S068 and S073 provide direct comparative evidence, with sample and value-set context; other summaries provide related country comparisons that must not be mislabeled as same-sample comparisons. |
| **Q71 — What is the open-access share of funded publications, and its trend?** | ProjectOutputLink, Publication date, OpenAccessObservation, denominator, time-series analytic. | **X.** Complete funded-output and dated access data are external. |
| **Q99 — What share of member-authored corpus papers are excluded as pure applications?** | Authorship, dated MembershipEpisode, corpus inclusion decision, `PureApplication` classification, exclusion reason, share analytic. | **X.** Membership and corpus-screening decisions are external. |
| **Q81 — What share of resolved researchers have an ORCID?** | Resolved Person, external ORCID identifier, identity status, denominator and share analytic. | **X.** Resolved profiles and ORCID links are not in the summaries. |
| **Q3 — What is the distribution of approved budgets (median, IQR, largest grants)?** | FundingAward, approved BudgetAmount, currency, normalization rule, median/IQR/maximum analytic. | **X.** The packet has no complete budget ledger. |
| **Q6 — What proportion of completed projects have at least one linked publication?** | Dated ProjectStatusObservation, ProjectOutputLink, Publication, completion and link-quality rules, proportion analytic. | **X.** Complete status and output links are external. |
| **Q78 — Which non-members co-author most frequently with members?** | Resolved Person, Authorship, dated MembershipEpisode, non-member rule, co-author counts. | **X.** Complete identity, authorship, and membership data are external. |
| **Q80 — Which projects' outputs cite other projects' outputs (inter-grant knowledge flow)?** | ProjectOutputLink, direct CitationEdge, citing and cited Publication, source and target Project, derived project-flow edge. | **X.** Direct citation and complete output data are external. |
| **Q7 — What is the median time from project start to first linked publication?** | Project start date, ProjectOutputLink, Publication date, earliest-publication rule, median duration analytic. | **X.** Complete project dates and output links are external. |
| **Q83 — How do papers-per-project compare across working groups?** | WorkingGroup, FundedProject, ProjectOutputLink, Publication, group assignment period, ratio analytic. | **X.** Working-group assignments and complete outputs are external. |
| **Q100 — Which papers entered the graph via full-text grant mining vs structured funder metadata?** | Publication record, IngestionEvent, route classification, source, date, run identifier. | **X.** This is graph-process provenance, not a paper fact. |
| **Q30 — Which value sets used the EQ-VT protocol, and which version?** | ValueSet, producing ValuationStudy, ValuationExercise, `USES_PROTOCOL_VERSION`, exact protocol version, unknown-version status. | **S.** S023, S013, S022, and S008 state EQ-VT versions for Danish, French, Egyptian, and Moroccan value-set studies. S004 states EQ-VT without a version and must remain unversioned. |
| **Q15 — Which publications acknowledge EuroQol funding but cannot be tied to any project id?** | Publication, `ACKNOWLEDGES_FUNDER`, ProjectOutputLink attempts, project identifier, unresolved-link status and reason. | **X.** It needs full acknowledgements and an audited project-linking process across the corpus. |
| **Q64 — Which are the most-cited systematic reviews in the corpus?** | Publication, SystematicReview classification, CitationMetricObservation, provider/date, ranking. | **X.** The summaries identify reviews but do not provide comparable citation counts. |
| **Q62 — Who works at institution X on EQ topics?** | Resolved Person, dated AffiliationEpisode, Organization, Publication or Project topic assignment, time scope. | **X.** Complete affiliations, identities, and topic records are external. |
| **Q70 — What co-authorship communities exist among EuroQol members?** | Resolved Person, Authorship, dated MembershipEpisode, co-authorship network, community-detection analytic and parameters. | **X.** Full authorship and membership data are external, and the communities are derived. |
| **Q53 — What are the ten most-cited papers on EQ-5D valuation methodology?** | Publication, EQ-5D valuation-methodology classification, CitationMetricObservation, ranking and tie rule. | **X.** Complete classification and current citation data are external. |
| **Q54 — What is the difference between a crosswalk and a native 5L value set — with key references?** | ValueSet derivation type, source and target InstrumentVersion, ValuationStudy, MappingModel, `PRODUCES_VALUE_SET`, `COMPARES_WITH_VALUE_SET`, Publication. | **S.** S023, S013, S071, and S073 provide explicit native/crosswalk comparisons and methodological context. |
| **Q58 — What has been published on EQ-5D-Y-5L so far?** | InstrumentVersion, status and reporter form, Publication, `DEVELOPS`, `TESTS`, `VALUES`, or `USES`, StudyType and findings. | **S.** S064 reports development of self-report EQ-5D-Y-5L; S039 studies stakeholder views; S085 tests an experimental proxy 5L. The answer must keep these forms and statuses separate. |
| **Q11 — Which countries' institutions have received the most EuroQol funding?** | FundingAward, recipient Organization, organization country, approved BudgetAmount, currency rule, aggregation. | **X.** Award recipients, countries, and budgets require an external grant ledger and organization resolution. |
| **Q18 — Which past funded projects are topically most similar to this proposal abstract?** | Proposal abstract, Project abstract, Project status/date, topic representation, similarity analytic, model/version and score. | **X.** The current proposal text and complete project abstracts are external; similarity is derived. |
| **Q44 — Which working groups does researcher X's work span?** | Resolved Person, Authorship or ProjectRole, FundedProject, WorkingGroup assignment, dates. | **X.** Researcher identity and working-group data are external. |
| **Q95 — Which projects studied under-represented populations (children, cognitive impairment)?** | FundedProject, Study, PopulationDefinition, LifeStage, Condition, inclusion/exclusion relation, under-represented classification with rule. | **S.** The packet supports a packet-bounded list for children through several project-linked summaries. It does not support a positive cognitive-impairment instance; studies that exclude cognitive impairment must not be counted as studying it. |
| **Q31 — Who is currently working on EQ-HWB valuation?** | Person, ProjectRole, active ProjectStatusObservation, ValuationStudy, target InstrumentVersion/Product, as-of date. | **X.** Current people and active-project status need external project and identity data. |
| **Q74 — Which researchers newly entered the corpus in the last three years?** | Resolved Person, Authorship, Publication date, corpus-entry date rule, observation window, first-entry analytic. | **X.** Complete identities and corpus history are external. |
| **Q87 — Which author profiles were merged, overridden, or skipped during identity resolution, and why?** | IdentityResolutionEvent, input/output profiles, action, rule, reason, operator, date. | **X.** This is graph-process audit data, not paper evidence. |
| **Q14 — Which PIs hold the most grants, by count and by total budget?** | Resolved Person, PI ProjectRole, FundingAward, approved BudgetAmount, currency rule, two rankings. | **X.** Complete roles and award budgets are external. |
| **Q57 — Which methods appear most often in funded valuation projects (what should I learn)?** | ProjectOutputLink, ValuationStudy classification, PreferenceElicitationMethod, ValuationProtocol, ModelSpecification, method-count analytic, learning-list curation. | **X.** The packet shows many methods, but complete funded-project membership and project-level de-duplication require external project data. “What should I learn” is a separate curated recommendation. |
| **Q5 — Which working group accounts for the most projects, and the most budget?** | WorkingGroup, Project assignment, FundingAward, approved BudgetAmount, count and sum analytics. | **X.** Working-group and budget ledgers are external. |
| **Q20 — Which ongoing projects overlap with this proposal's aims?** | Proposal aim or abstract, FundedProject aim/abstract, dated ProjectStatusObservation, overlap analytic and threshold. | **X.** Current project data and proposal content are external; overlap is derived. |
| **Q72 — How do citations of researchers' EuroQol-funded papers compare with their other corpus papers?** | Resolved Person, Authorship, ProjectOutputLink or funding relation, CitationMetricObservation, funded/non-funded partition, comparison analytic. | **X.** Complete identities, funding links, and citation snapshots are external. |
| **Q27 — How productive were past projects in the same budget band as this proposal?** | Proposal requested/approved budget, BudgetBand definition, past Project, ProjectOutputLink, productivity metric, observation period. | **X.** Budgets, proposal data, complete outputs, and a declared productivity rule are external. |
| **Q51 — What EQ-TIPS work exists so far?** | InstrumentFamily and exact versions, Publication, StudyType, `DEVELOPS`, `TESTS`, `VALUES`, status, finding. | **S.** S061, S065, and S060 cover qualitative development, a planned DCE protocol, and comparative psychometric work. The answer must preserve V2.0/V3.0 and 3L/5L distinctions. |
| **Q34 — What population norms have been published for EQ-5D-5L, by country?** | PopulationNormSet, Publication, country, collection period, PopulationDefinition, InstrumentVersion, scoring ValueSet, sample and strata. | **S.** S070 reports Trinidad and Tobago norms, S027 Romanian 3L/5L norms, and S077 German elderly 5L reference values. Their populations and periods must remain explicit. |

## 10. Complete example records

### 10.1 Example A: Danish EQ-5D-5L valuation and native value set

**Evidence:** summary S023, “The Danish EQ-5D-5L Value Set: A Hybrid Model Using cTTO and DCE Data”.

**Publication**

- DOI: 10.1007/s40258-021-00639-3.
- Published: 2021-02-02.
- Publication type: national EQ-5D-5L valuation study and value-set report.
- Authors as listed in S023: Jensen CE, Sørensen SS, Gudex C, Jensen MB, Pedersen KM, and Ehlers LH.

**Project and funding evidence**

- Project identifier: 20170401.
- The summary states that funding included EuroQol Research Foundation project 20170401 and other named funders.
- This supports an explicit funded-project relation. It is stronger than a project ID alone.

**Study**

- Study classification: national valuation study.
- Jurisdiction and target population: Denmark; adult general population.
- Recruitment basis: Statistics Denmark data on age, gender, education, and region.
- Fieldwork: October 2018 to November 2019.
- Sample stages: target 1,200; interviewed 1,052; retained for analysis 1,014 after stated exclusions.
- Administration: EQ-VT 2.1 computer-assisted personal interviews.
- Instrument valued: EQ-5D-5L.
- Interview-language status: not reported for EQ-5D-5L; the summary reports a Danish translation of training material. The ontology must not fill this gap.

**Valuation exercises**

- cTTO: ten states per respondent; design of 86 states; conventional TTO for better-than-dead states and lead-time TTO for worse-than-dead states.
- Duration-free DCE: seven pairs per respondent; 196 pairs in 28 blocks.
- Quality-control facts include task-time, explanation, and 55555 inconsistency flags, plus interviewer retraining rules.

**Analyses and model selection**

- cTTO candidates included GLS random-intercept and random-effects Tobit models.
- DCE used conditional logit, with a heteroscedastic robustness model.
- Hybrid candidates combined cTTO and DCE with a multiplicative scale parameter.
- Preferred exact model: heteroscedastic censored hybrid model.
- Selection context: it removed logical inconsistencies in the combined estimates; some adjacent increments were not statistically different.

**Product**

- Product type: native Danish EQ-5D-5L value set.
- Coverage: all 3,125 EQ-5D-5L health states.
- Full health 11111: 1.
- Worst state 55555: -0.757.
- Reported dimension ranking: anxiety/depression, pain/discomfort, mobility, self-care, usual activities.
- Intended use: Danish QALYs and health-care decision-making.

**Structured findings and comparisons**

- Twenty-two percent of observed cTTO states were worse than dead.
- The study compares its native 5L product with Danish 3L and crosswalk sets. This is a `COMPARES_WITH_VALUE_SET` relation, not a claim that the study produced those comparison sets.

### 10.2 Example B: Ethiopian EQ-5D-Y-3L self-proxy agreement

**Evidence:** summary S069, “Psychometric evaluation of the EQ-5D-Y-3L in Ethiopian pediatric inpatients: comparing self and proxy reports”.

**Publication**

- DOI: 10.1186/s41687-025-00928-8.
- Publication type: repeated-measures psychometric evaluation of self and proxy reports.
- Project identifier in the packet: 436-RA.
- The summary does not give an explicit funding statement. The project identifier is retained as packet association evidence and is not silently promoted to an explicit funding acknowledgement.

**Study and population**

- Setting: University of Gondar Comprehensive Specialized Hospital, Ethiopia.
- Collection period: 1 June to 31 October 2023.
- Population: pediatric inpatients aged 4-18 years with prevalent acute illness.
- Exclusions included low consciousness, disorientation, or visual impairment.
- Sample stages: 985 recruited dyads; 28 excluded for incomplete descriptive-system or EQ VAS data; 957 dyads analyzed.
- Time points: admission and discharge.

**Instrument administration**

- Instrument: modified Amharic EQ-5D-Y-3L plus EQ VAS.
- Dimensions: mobility, looking after myself, doing usual activity, pain/discomfort, and worried, sad or unhappy.
- Children aged 8-18 self-completed.
- Children aged 4-7 also self-completed, with trained data collectors reading and giving simple clarification.
- Parents or caregivers completed the proxy version.
- The exact proxy version number or proxy perspective is not stated in the summary and remains not reported.

**Scoring and analysis**

- The Zimbabwe EQ-5D-Y-3L value set was used because an Ethiopian value set was not available.
- This is `USES_VALUE_SET_FOR_SCORING`; the study did not produce a Zimbabwe or Ethiopian value set.
- Dimension agreement used weighted Cohen's kappa.
- Index and EQ VAS agreement used ICC.
- Responsiveness used physician-recorded clinical improvement, paired changes, and Paretian Classification of Health Change.

**Findings**

- Dimension agreement was fair to moderate at admission, with weighted kappa from 0.28 to 0.38.
- Agreement for worried, sad or unhappy was lower at discharge, with kappa 0.15.
- Index ICC was 0.582 at admission and 0.498 at discharge.
- EQ VAS ICC was 0.671 at admission and 0.676 at discharge.
- Both perspectives showed substantial improvement after treatment.
- The source interpretation is that emotional dimensions can have poorer agreement because they are less observable to proxies.

**Limitations**

- The hospital population was expected to improve and can overstate responsiveness.
- No cognitive interviews were done for younger children.
- Children with developmental disabilities were excluded.
- The Zimbabwe value set may not represent Ethiopian preferences.

### 10.3 Example C: planned EQ-TIPS-5L V3.0 preference study

**Evidence:** summary S065, “Assessing the experimental EuroQol toddler and infant populations (EQ-TIPS) descriptive system: a protocol integrating discrete choice experiment (DCE) surveys in instrument development”.

**Publication and status**

- DOI: 10.1136/bmjopen-2025-100897.
- Publication type: study protocol for two online DCE waves.
- Project identifier in the packet: 1850-RA.
- Study status at publication: planned. The summary reports no completed DCE results, value set, or final recommendation.

**Instrument version**

- Experimental EQ-TIPS-5L V3.0.
- Target age of the instrument: 0-36 months.
- Seven attributes: Movement, Eating or drinking, Sleep, Pain, Managing emotions, Interacting with others, and Play.
- Five ordered response levels from no problems/no pain to extreme problems.

**Planned preference context and samples**

- Common scenario: a one-month acute episode for a one-year-old child who recovers after one month.
- Preference source: Australian adults in the general community.
- Wave 1: planned sample 400; 14 kaizen tasks each.
- Wave 2: planned sample 1,000; 28 paired comparisons each.
- Planned total: 1,400.

**Planned analysis**

- Primary model: main-effects conditional logit estimated by maximum likelihood.
- Planned comparisons include non-zero main effects, discordance, Lin's concordance coefficient, and bootstrap uncertainty.
- Scale-adjusted latent-class models are possible future work, not a completed analysis.

This record shows why `planned`, `completed`, and `not produced` are required assertion states.

## 11. Free text, optional facts, derived facts, and exclusions

### 11.1 Keep as free text with optional classification

Keep these items as source text unless a stable controlled need emerges:

- detailed author interpretations of cultural, historical, or behavioral causes;
- long limitation narratives;
- quotations and qualitative examples;
- detailed recruitment narratives;
- unusual task instructions;
- proposed wording changes;
- reasons for model selection beyond controlled criteria; and
- policy-use narratives.

Important free text can also receive topic tags, but the text remains primary evidence. For example, S061 reports expert concerns about “age-appropriate behaviour”; that wording must remain available even if it is classified under proxy subjectivity or cross-cultural interpretation.

### 11.2 Optional facts

Facts are optional when they are not applicable or not reported. Examples include sample size for conceptual papers, a model for qualitative studies, a value set for protocols, interview language, an ORCID, a budget, and an access license. There is no universal minimum record beyond identity and provenance sufficient to distinguish the record.

### 11.3 Derived facts

The following are derived and must have recipes:

- first grant or first publication;
- first-time PI;
- top decile;
- budget band;
- papers per project;
- citation rank;
- open-access trend;
- co-authorship community;
- topic similarity or overlap;
- inter-grant knowledge flow; and
- “starter reading list” ranking.

### 11.4 Outside the core research-evidence scope

The ontology can link but does not define the operational semantics of:

- grant-management accounting;
- currency-exchange services;
- citation providers;
- open-access registries;
- ORCID account management;
- identity-resolution software; and
- graph-ingestion pipelines.

It represents their observations and provenance so that user questions remain auditable.

## 12. Unresolved design choices and risks

1. **Project-link strength.** A project ID in a packet, an explicit publication acknowledgement, and a structured grant-output link have different evidential strength. The final policy for `OUTPUT_OF_PROJECT` needs a reviewed evidence hierarchy.
2. **Study boundaries.** Some publications use multiple datasets, samples, waves, or embedded studies. Curators need rules for when these become separate `Study` records rather than parts of one study.
3. **Instrument identity.** Similar names do not prove equivalence. The relation between EQ-HWB-S and EQ-HWB-9, and between experimental and later official forms, remains unresolved until explicit version evidence is linked.
4. **Model composition.** A facet model preserves exact specifications but can become complex. A controlled set of common complete labels should coexist with facets and source wording.
5. **Proxy semantics.** Many summaries say “proxy” without a version or perspective. These fields must remain unknown rather than inferred from study context.
6. **Language and translation.** A translated training package does not prove the interview language. Comparable language versions are not always literal equivalents, as S064 reports.
7. **Sample counts.** Invited, interviewed, completed, excluded, analyzed, and paired counts are not interchangeable. Count-stage normalization needs careful quality review.
8. **Conflicting source facts.** S004 reports different mean ages in its abstract and Results. The ontology must retain both assertions and the conflict.
9. **Negative evidence.** “Not reported”, “not tested”, “not produced”, and an observed count of zero have different meanings.
10. **Native, crosswalk, and mapped products.** Product classification can be wrong if it is inferred from the word “value set” alone. Derivation evidence is mandatory for the subtype.
11. **Dynamic facts.** Current project status, membership, affiliation, citations, and open access need dated observations. Cached values can give wrong answers to “current” questions.
12. **Denominators.** Shares in Q6, Q68, Q71, Q81, and Q99 depend on explicit corpus, person-resolution, project-status, and classification rules.
13. **Money.** Combining or ranking budgets across currencies requires a declared normalization date and method. Original approved amounts must remain unchanged.
14. **Topic classifications.** “Methodological”, “pure application”, and “under-represented” are useful but contestable. Their assignments need rule versions and human review.
15. **Citation-to-product resolution.** A paper can cite a publication that introduced a value set without naming the product. Product-level reference resolution needs evidence and must not be guessed.
16. **Recommendation questions.** “Good starter reading” and “what should I learn” require a transparent curation objective. Citation rank alone is not a sufficient research recommendation.
17. **Packet coverage.** The 50 summaries support ontology design but are not evidence that no other EuroQol work exists. Packet-bounded negative answers must state their boundary.

## 13. Minimum quality checks for populated records

Before a record becomes searchable:

- every publication, study, project, person, instrument version, product, and finding has a stable local identity;
- each domain fact has evidence or is explicitly marked derived;
- study type and publication type are separate;
- instrument family, version, language, reporter form, and status are not collapsed;
- valuation method, protocol version, model specification, and product type remain exact;
- planned work is not reported as completed;
- sample counts have stages and denominators;
- health-state codes name their instrument version;
- value-set creation, use, comparison, and reference are distinct;
- project output, funding acknowledgement, and packet association are distinct;
- source terms and canonical terms remain linked but separate;
- external observations have provider and as-of date;
- derived analytics state boundary, rule, inputs, and calculation date; and
- unknown, not reported, conflicting, and explicit negative evidence remain distinct.

This structure gives researchers direct access to exact EuroQol research facts while it also supports larger administrative and bibliometric questions through explicit, auditable links.
