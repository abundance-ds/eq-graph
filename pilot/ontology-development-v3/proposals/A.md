# EuroQol research ontology proposal A

## 1. Purpose and scope

This ontology supports precise search and synthesis of EuroQol research. It represents facts about publications, studies, funded projects, people, populations, instruments, methods, analyses, products, outcomes, and findings. It also supports portfolio questions about funding, outputs, collaboration, citation, and change over time.

The central unit is an evidence-backed research assertion. Each assertion keeps its source, source location, source wording, canonical term, and classification. The ontology does not treat a paper title, a project identifier, or a broad topic label as a substitute for an exact research fact.

The ontology uses an open-world rule. Missing information means unknown unless the source gives an explicit negative statement. For example, a paper that does not mention EuroQol funding is not evidence of no EuroQol funding.

The supplied summaries support a detailed publication and study layer. Many portfolio questions also need linked project, identity, membership, citation, journal, and workflow data. The ontology includes places for these records, but it does not invent them.

The ontology does not store raw respondent-level data as research facts. It can identify and describe a dataset, sample, or analysis. It can also link to governed raw data when this is permitted.

## 2. Design rules

1. Keep a publication, a study, a project, and an analytic result as separate objects.
2. Keep the exact source term and the canonical term. Do not replace one with the other.
3. Classify an instrument by its role in a study. A cited instrument is not necessarily administered, evaluated, valued, or developed.
4. Record the exact method and model variant. Do not reduce `hybrid heteroskedastic Tobit censored at -1` to only `model`.
5. Give every number its metric, unit, population, timepoint, and analysis context when the summary supplies them.
6. Keep planned analyses, hypotheses, observed results, author interpretations, recommendations, and limitations separate.
7. Make a project-to-publication link only when evidence supports the link. A nearby project identifier is not sufficient by itself to prove funding or output status.
8. Keep source disagreement. Do not select one value without a documented resolution.
9. Compute counts, shares, trends, similarity, and network measures in the analytics layer. Do not store these values as if a paper reported them.
10. Permit more than one study type, population, method, instrument role, analysis, or product for one study. Do not force all papers into one template.

## 3. Conceptual structure

The main research path is:

- A `Publication` reports one or more `Study` records.
- A `Study` can be conducted under a `FundedProject` when an explicit link supports this relation.
- A `Study` uses defined `Population`, `Sample`, `InstrumentUse`, `MethodUse`, and `Analysis` records.
- A `Study` can produce a `ResearchProduct` and report `Result` and `Finding` records.
- A `SourceSummary` supports each extracted `Assertion`.
- A `DerivedAnalytic` uses selected assertions and external linked records. It is not a reported study result.

People, organizations, working groups, citations, and project records connect to this path. These connections need their own evidence and dates.

## 4. Main concepts

### 4.1 Evidence and terminology concepts

| Concept | Meaning |
|---|---|
| `SourceSummary` | One supplied fixed summary. It has a summary identifier, file identity, hash, and source-paper reference. |
| `SourceLocation` | The section, table, figure, abstract, or other location named in a summary. |
| `Assertion` | One claim about an object, relation, category, or literal value. It carries provenance and evidence status. |
| `SourceTermOccurrence` | The exact word or phrase used by a source, such as `C-TTO`, `tele-TTO`, or `5L > 3L crosswalk`. |
| `CanonicalTerm` | The stable preferred term used for retrieval, such as `composite time trade-off (cTTO)`. |
| `TerminologyMapping` | A reviewed link from a source term to a canonical term. Its mapping type can be exact synonym, abbreviation, narrower, broader, close, ambiguous, or not mapped. |
| `ClassificationAssignment` | A dated, sourced assignment of an object to a controlled class. It is separate from the source wording. |
| `ConflictSet` | Two or more source-backed assertions that cannot all be one resolved value. |

An assertion has these minimum fields:

- subject;
- relation or measured property;
- object or literal value;
- evidence status;
- source summary identifier;
- source location when supplied;
- source term or source wording when terminology matters;
- extraction or review status;
- valid time or observation time when supplied.

The ontology can expose simple relations for search. The assertion record remains the source of provenance. This design makes it possible to search for `cTTO` and still show whether the paper used `C-TTO`, `c-TTO`, or `composite time trade-off`.

### 4.2 Research administration concepts

| Concept | Meaning and boundary |
|---|---|
| `Publication` | A published or planned scholarly output. DOI, title, journal, publication date, and access status belong here. A publication is not a study. |
| `Study` | A defined research activity with an aim, design, population, data collection, and analysis. One publication can report more than one study. One study can have more than one publication. |
| `FundedProject` | A managed project or grant with its own identifier, title, dates, status, award class, applicants, host, approved budget, and funder. These fields do not belong to a publication. |
| `FundingContribution` | A documented contribution from a funder to a project, study, publication, or open-access charge. Research funding and open-access funding are different values. |
| `Researcher` | A resolved person identity. A display name is not sufficient for resolution. |
| `IdentityProfile` | A source-specific person record, such as an author string, grant applicant record, member record, or ORCID profile. |
| `IdentityResolutionDecision` | A merge, override, skip, or non-match decision with reason, actor, time, and evidence. |
| `ProjectParticipation` | A dated role that connects a researcher to a project, such as applicant, PI, co-investigator, or collaborator. |
| `Organization` | A university, hospital, research institute, company, funder, or other organization. |
| `WorkingGroup` | A named EuroQol or research working group. Membership and project association need dates. |
| `Membership` | A time-bounded member relation between a researcher and an organization or group. |
| `Authorship` | A relation between a researcher profile and a publication, with source order and corresponding-author status when supplied. |
| `Affiliation` | A time-bounded relation between a researcher and an organization. Publication affiliation and current employment are different relations. |
| `Journal` | A publication venue. Venue metrics attach to the journal for a named metric year and source. |
| `AccessStatus` | A dated, sourced open-access classification for a publication. |
| `MetadataQualityFlag` | A source-record problem such as a truncated author list or missing abstract, with detection rule and resolution status. |
| `CorpusDecision` | A dated inclusion or exclusion decision with a reason and rule version. |
| `Topic` | A controlled research subject, instrument subject, method subject, or application subject. |
| `TopicAssignment` | A sourced or derived assignment of a topic to a study, project, publication, or proposal, with method and confidence. |
| `Proposal` | A query-time or managed proposal record. Its abstract and reference list are inputs for similarity and overlap questions. |
| `ReferenceListEntry` | One parsed proposal or publication reference, with its source text and match status. |
| `Citation` | A directed relation from one publication to another, with the citation source and retrieval date. |

### 4.3 Study context concepts

| Concept | Meaning |
|---|---|
| `Aim` | A source-reported research objective. It remains available as text and can have controlled topic assignments. |
| `PopulationDefinition` | The intended population, including participant role, age, condition, geography, and eligibility. |
| `Sample` | A set of participants used at a stated stage. Examples are invited, enrolled, completed, analytic, retest, or follow-up samples. |
| `Group` | An arm, cohort, subgroup, comparator, qualitative stakeholder group, or disease-status group. |
| `WaveOrTimepoint` | A named data-collection wave or observation time, such as pre-heatwave, heatwave 1, T1, T2, baseline, or one-year follow-up. |
| `Setting` | A hospital, community, online panel, care home, registry, country, city, or other study setting. |
| `Condition` | A health condition or health-status category used to define or compare a population. |
| `SamplingMethod` | A controlled sampling design, such as quota, purposive, convenience, stratified, panel, registry, or snowball sampling. |
| `RecruitmentMethod` | The operational recruitment channel. Examples include public places, patient organizations, local groups, social media, and clinical referral. |
| `EligibilityCriterion` | An inclusion or exclusion rule. It keeps its exact source text when detail is important. |
| `DataCollectionPeriod` | A start date, end date, date precision, and source. |

One study can have several samples. Each sample-size assertion must state the sample stage. Thus, `1,145 interviewed`, `140 practice interviews excluded`, and `1,005 included` are three facts, not three values for one generic sample-size field.

### 4.4 Instrument concepts

| Concept | Meaning |
|---|---|
| `InstrumentFamily` | A broad lineage, such as EQ-5D, EQ-5D-Y, EQ-HWB, or EQ-TIPS. |
| `InstrumentVersion` | An exact version or form, such as EQ-5D-5L, EQ-5D-Y-3L, EQ-HWB-S, or EQ-TIPS V2.0. |
| `LanguageVersion` | An instrument version in a stated language and locale, with translation or validation status. |
| `InstrumentComponent` | A descriptive system, EQ VAS, instruction set, or other named component. |
| `Dimension` | A named construct in an instrument, such as mobility, pain/discomfort, sleep, or Social Interaction. |
| `ResponseLevel` | A version-specific level with an order and exact wording. |
| `HealthState` | A profile in one exact instrument version. The code `55555` is not meaningful without its instrument version. |
| `BoltOnDimension` | A dimension added to a base instrument for a study or candidate version. |
| `InstrumentUse` | The role of an instrument version in one study. |
| `Administration` | A use event with mode, respondent, perspective, language, device, interviewer status, recall period, and timepoint. |

The following family and version distinctions are source-supported:

| Family | Exact versions or forms in the summaries | Rule |
|---|---|---|
| EQ-5D | EQ-5D-3L; EQ-5D-5L | Keep 3L and 5L separate. Keep their dimensions, level wording, state spaces, and value sets version-specific. |
| EQ-5D-Y | EQ-5D-Y-3L; EQ-5D-Y-5L | Keep youth versions separate from adult versions and from each other. |
| EQ-HWB | experimental 25-item EQ-HWB; EQ-HWB-S; derived EQ-HWB-9 | Do not treat EQ-HWB-S and EQ-HWB-9 as synonyms without evidence. |
| EQ-TIPS | experimental EQ-TIPS V2.0, described as EQ-TIPS-3L | Preserve experimental status, version, age range, six dimensions, and proxy design. |
| EQ VAS | EQ VAS used with several instrument versions | Treat it as a named measure or component. Do not assume that a study of the descriptive system also studied EQ VAS. |
| EQ-5D extensions | breathing, cognition, dining, gastrointestinal problems, sleep, tiredness, skin irritation, self-confidence, and social relationships bolt-ons | Record each bolt-on, base version, wording version, order, and evidence type. |

Other measures, such as WHOQOL-BREF, WHOQOL-OLD, SF-6Dv2, PROPr, PROMIS-29 + 2, MSIS-8D, POSAS 2.0, WHODAS-12, QOL-ACC, ASCOT, CarerQol, WHO-5, PHQ-9, and GAD-7, use the same instrument registry. Their source names remain available. This registry is necessary for comparison and future crosswalk queries.

The controlled `InstrumentUseRole` values are:

- administered;
- self-report descriptor;
- proxy report;
- preference object valued;
- developed;
- translated or culturally adapted;
- content validated;
- psychometrically evaluated;
- scored with;
- compared with;
- source for a crosswalk;
- target of a crosswalk;
- cited as background only.

These roles prevent false search results. For example, a paper that discusses EQ-5D-Y-5L in an interview is not automatically an EQ-5D-Y-5L valuation study.

### 4.5 Method and analysis concepts

| Concept | Meaning |
|---|---|
| `MethodUse` | One use of a research, elicitation, qualitative, psychometric, or synthesis method in a study. |
| `PreferenceElicitationTask` | A task type, framing, comparator, duration, perspective, and number of tasks. |
| `ValuationProtocol` | A named protocol and exact version, such as EQ-VT 2.0 or EQ-VT 2.1. |
| `QualityControlRule` | A defined check, threshold, flag, exclusion, retraining action, or feedback process. |
| `Analysis` | A defined analysis with inputs, population, outcome, covariates, method, and software when supplied. |
| `StatisticalModel` | The exact model specification used by an analysis. |
| `ModelRole` | Candidate, preferred, final, sensitivity, validation, or rejected. |
| `Scale` | The interpretation and anchors of a measure or estimated value. |

#### Preference and valuation method family

| Canonical value | Required distinction |
|---|---|
| conventional TTO | Better-than-dead TTO task. Do not use it as a synonym for all cTTO. |
| lead-time TTO | Worse-than-dead TTO task with lead time. |
| composite time trade-off, or cTTO | Protocol that combines conventional and lead-time TTO. Source aliases include `C-TTO` and `c-TTO`. |
| duration-free DCE | Choice between health states without a duration attribute. |
| DCE with duration, or DCEd | Choice design that includes duration. `DCE-duration` is a source alias when the design matches. |
| DCE-death | DCE design with immediate death as a comparator. |
| split-triplet DCEd | The specific A/B and B/full-health sequence in S019. It is narrower than DCEd. |
| paired comparison | A direct choice between two profiles. Keep its scale and duration design. |
| best-worst scaling case 2 | Selection of the best and worst attribute level in one profile. |
| Kaizen task | Sequential selection of improvements that creates a preference path. |
| personal utility function elicitation | Direct dimension, level, dead-location, and interaction tasks used to form a PUF. |
| standard gamble | Preference elicitation used for PROPr in the supplied comparison. |
| EQ VAS rating | Rating on the stated 0-to-100 visual scale. It is not a TTO or DCE method. |

`Hybrid` is a model class, not an elicitation method. A hybrid value set must separately state the input methods and the final model.

The protocol registry has exact versions. `EQ-VT`, `EQ-VT 2.0`, and `EQ-VT 2.1` are different controlled values until a source gives a version. The source term `EuroQol Portable Valuation Technology` in S007 remains exact and is not silently changed to a numbered EQ-VT version.

#### Administration and perspective family

Administration mode has separate fields for interaction and delivery:

- interaction: self-complete, interviewer-administered, interviewer-assisted, or proxy-complete;
- delivery: face-to-face, paper, web, tablet, telephone, videoconference, or mixed;
- proxy perspective: proxy-person or proxy-proxy;
- preference respondent: adult general public, child, adolescent, patient, caregiver, or other stated role;
- described person: self, another adult, a child of a stated age, own child, generic child, or other stated person;
- valuation perspective: self, other-person, societal, or source-specific perspective;
- recall or reference period: today, seven days, two weeks, one-week episode, or exact source text.

The source codes `SA_A`, `OA_A`, `SC_A`, `OC_A`, `SC_C`, and `OC_C` from S032 remain source aliases. Their expanded respondent and perspective fields are the canonical representation.

#### Scale family

The ontology distinguishes these source-supported scales:

- full health 1 and dead 0 QALY scale, with possible values below 0;
- latent DCE scale without a dead anchor;
- pits scale, with `55555 = 0` and `11111 = 1`;
- experience scale, with coma 0 and one week in full health 1;
- EQ VAS 0-to-100 scale;
- unweighted level sum score;
- instrument-specific value-set scale with exact anchors and range.

A value on one scale must not be compared with a value on another scale without an explicit transformation or analytic decision.

#### Model and analysis family

The ontology stores the exact source label and a controlled model family. Source-supported families include:

| Family | Exact variants that must remain available |
|---|---|
| linear regression | OLS, GLS, censored linear regression, logistic regression, and models with robust or random effects |
| Tobit | random-effects Tobit, Tobit censored at -1, heteroskedastic Tobit, and heteroskedastic no-constant Tobit |
| choice model | conditional logit, heteroskedastic conditional logit, mixed logit, and nonlinear-time mixed logit |
| hybrid valuation model | standard hybrid, hybrid Tobit, heteroskedastic hybrid, heteroskedastic censored hybrid, and Bayesian hybrid |
| latent class | scale-adjusted latent class model with separate taste and scale classes |
| evidence synthesis | random-effects meta-analysis and multi-level meta-regression |
| psychometric analysis | correlation, reliability, known-groups validity, responsiveness, informativity, factor analysis, and ceiling or floor analysis |
| qualitative analysis | thematic, framework, content, conversational, and qualitative interpretive analysis |
| change classification | Paretian Classification of Health Change and its stated categories |

Each model has a `ModelRole`. A paper can test ten candidate models and select one final model. Search for a produced value set must use the final model, not all tested models.

### 4.6 Product, outcome, result, and finding concepts

| Concept | Meaning |
|---|---|
| `ResearchProduct` | A durable output from a study. It can be a value set, crosswalk, instrument version, language adaptation, protocol, framework, population-norm set, item criteria, or quality-control scheme. |
| `ValueSet` | A function or coefficient set that assigns values to states of one exact instrument version. |
| `Crosswalk` | A rule that predicts a target measure or value from a different source measure or version. |
| `ScaleAnchoringMap` | A transformation from a latent preference scale to an anchored scale. It is not an instrument crosswalk. |
| `Outcome` | A measured or analyzed variable, such as EQ-5D index, EQ VAS, completion, ceiling, utility, or a qualitative content-validity construct. |
| `Result` | A source-reported observation, estimate, comparison, test result, theme, or model output. |
| `Finding` | A bounded claim that interprets one or more results in a stated context. |
| `Limitation` | A source-reported boundary, risk, or evidence gap. |
| `PlannedAnalysis` | An analysis in a protocol that has not yet produced a result. |
| `DerivedAnalytic` | A value computed across ontology records for a portfolio question. |

A `ValueSet` has these useful fields:

- exact instrument version;
- jurisdiction or target population;
- value perspective and preference respondent population;
- elicitation methods;
- protocol and version;
- sample or samples;
- final statistical model;
- anchors, scale, and range;
- coefficient or scoring-rule reference;
- product status, such as source-reported national, experimental, pilot, or not stated;
- producing study and reporting publication;
- funding evidence, if supplied.

The ontology uses three different mapping classes:

1. An `InstrumentCrosswalk` converts one instrument or version to another target score. The US EQ-5D-5L-to-EQ-5D-3L crosswalk in S073 is in this class.
2. A `ScaleAnchoringMap` places latent DCE values on a TTO or dead/full-health scale. The power mapping in S007 is in this class.
3. A `ConditionSpecificToGenericMapping` predicts EQ-5D from a condition-specific instrument. No supplied summary reports such a study.

This distinction is necessary for Q35 and Q54.

### 4.7 Exact result structure

A numeric result has, when applicable:

- metric name;
- point value;
- unit;
- numerator and denominator;
- dispersion or interval;
- p value or other uncertainty;
- observed, predicted, adjusted, or derived status;
- sample and subgroup;
- instrument and value set;
- health state;
- wave or timepoint;
- comparator;
- analysis and model;
- source location.

A qualitative result has a theme or category, participant group, method, source location, and exact source label. A finding then states what the authors concluded from that result. The ontology does not convert an author explanation into a tested causal result.

For example, S029 reports that cultural concerns about burden on family and friends can be a possible explanation for negative values. The ontology stores this as an author interpretation, not as a causal finding.

## 5. Controlled study classifications

Study classification uses independent facets. A record can have more than one value in each facet when the evidence supports this.

### 5.1 Research-purpose facet

The source-supported values are:

- national valuation and value-set production;
- valuation method development or comparison;
- preference-task or experimental-design study;
- instrument or conceptual-framework development;
- translation and cultural adaptation;
- content-validity study;
- psychometric or measurement-property study;
- feasibility or implementation study;
- data-quality or interviewer-quality study;
- population-norm study;
- descriptive HRQoL or outcome-monitoring study;
- equity or inequality analysis;
- systematic review or evidence synthesis;
- study protocol;
- comparative value-set analysis.

`Pure application` is a question-required corpus inclusion class. The summaries do not supply the project's inclusion rule or exclusion decisions. Store this value only with a separate curation assertion.

### 5.2 Design facet

The source-supported values include qualitative, quantitative, mixed-methods, cross-sectional, longitudinal, observational cohort, registry study, online-panel study, experimental preference study, secondary analysis, theoretical state-space analysis, systematic review, meta-analysis, pilot, and protocol.

These values are not mutually exclusive. For example, S098 is longitudinal, descriptive, registry-based, and quantitative.

### 5.3 Sample-role and stage facet

Participant role values include general-population adult, child, adolescent, patient, caregiver, informal carer, expert, clinician, staff proxy, family proxy, registry member, and stakeholder.

Sample-stage values include target, invited, approached, consented, started, completed, eligible, excluded, analytic, retest, follow-up, pilot, and model-specific. The ontology also stores the reason for each transition when supplied.

### 5.4 Project and portfolio values

The following values are required by the competency questions but need linked project or workflow data:

- project status: ongoing, completed, closed, cancelled, or unknown;
- grant class: student grant, research award, value-set award, doctoral award, or source-specific class;
- project role: applicant, principal investigator, co-investigator, collaborator, host, or working-group sponsor;
- output-link status: asserted, verified, disputed, candidate, or rejected;
- researcher membership status: member, non-member, former member, or unknown, with dates;
- identity decision: merged, overridden, skipped, split, or unresolved;
- publication inclusion class: included, excluded as pure application, excluded for another reason, or unreviewed;
- access status: open access, closed, hybrid, or unknown, with date and source;
- venue metric: named metric, source, metric year, value, and coverage.

Do not derive these values from a project identifier, author name, DOI prefix, or missing field.

## 6. Important relations

| Relation | From | To | Meaning and rule |
|---|---|---|---|
| `reports` | Publication | Study | The publication reports the study. Do not assume one-to-one cardinality. |
| `supportedBy` | Assertion | SourceSummary | The summary supports the assertion. |
| `hasSourceLocation` | Assertion | SourceLocation | The summary identifies the relevant source section, table, or figure. |
| `usesSourceTerm` | Assertion or mention | SourceTermOccurrence | Keeps exact source wording. |
| `mapsToCanonicalTerm` | SourceTermOccurrence | CanonicalTerm | Gives a reviewed terminology mapping. |
| `classifiedAs` | Entity | Controlled class | Uses a separate classification assignment with provenance. |
| `conductedUnderProject` | Study | FundedProject | Use only for an explicit study-to-project assertion. |
| `outputOfProject` | Publication or Product | FundedProject | Use only for an explicit output link. |
| `fundedBy` | Project, Study, or Publication | FundingContribution | States the exact funding target and contribution type. |
| `reportsProjectReference` | Publication or Summary | Project identifier | Records a source project identifier without making a stronger funding claim. |
| `authoredBy` | Publication | Researcher or profile | Keeps author order and source profile. |
| `affiliatedWithAtPublication` | Authorship | Organization | Does not imply current employment. |
| `memberOfDuring` | Researcher | Organization or WorkingGroup | Requires a time interval or observation date. |
| `hasIdentityProfile` | Researcher | IdentityProfile | Connects the resolved person to a source profile through a resolution decision. |
| `participatesInProject` | Researcher | ProjectParticipation | Keeps project role and dates. |
| `participationFor` | ProjectParticipation | FundedProject | Connects the role record to the project. |
| `associatedWithProject` | WorkingGroup | FundedProject | Requires a source and, when applicable, a time interval. |
| `hostedBy` | FundedProject | Organization | Identifies the project host. |
| `hasTopicAssignment` | Project, Study, Publication, or Proposal | TopicAssignment | Keeps the topic scheme, assignment method, and evidence. |
| `assignsTopic` | TopicAssignment | Topic | Identifies the controlled topic. |
| `publishedIn` | Publication | Journal | Identifies the publication venue. |
| `hasAccessStatus` | Publication | AccessStatus | Keeps access source and observation date. |
| `hasMetadataFlag` | Publication record | MetadataQualityFlag | Keeps the flag rule, status, and audit source. |
| `hasCorpusDecision` | Publication | CorpusDecision | Keeps the inclusion rule and reason. |
| `hasReferenceEntry` | Proposal or Publication | ReferenceListEntry | Keeps the source citation string before matching. |
| `matchesPublication` | ReferenceListEntry | Publication | Requires an identifier or reviewed bibliographic match. |
| `hasPopulation` | Study | PopulationDefinition | States the intended population. |
| `hasSample` | Study | Sample | Links a study to a sample at a stated stage. |
| `subsampleOf` | Sample | Sample | Supports arms, retest samples, and analytic subsets. |
| `observedAt` | Sample, Administration, or Result | WaveOrTimepoint | Keeps longitudinal context. |
| `locatedIn` | Setting, Organization, or Sample | Place | Uses an explicit place hierarchy. |
| `administers` | Study | InstrumentUse | States actual administration. |
| `evaluates` | Study | InstrumentUse | States the object of evaluation. |
| `develops` | Study | InstrumentVersion or Product | States development, not only mention. |
| `adaptsFrom` | LanguageVersion | InstrumentVersion or LanguageVersion | Keeps source and target versions. |
| `values` | Study | InstrumentVersion | States that its health states are valuation objects. |
| `usesMethod` | Study or Analysis | MethodUse | Keeps method role and variant. |
| `usesProtocol` | MethodUse | ValuationProtocol | Keeps exact protocol version. |
| `usesAdministration` | InstrumentUse or MethodUse | Administration | Keeps mode, perspective, and language. |
| `appliesModel` | Analysis | StatisticalModel | Keeps the full model specification and role. |
| `measures` | Analysis or Result | Outcome | Identifies the exact outcome. |
| `comparesWith` | Analysis | Instrument, group, result, or product | Keeps comparator type and direction. |
| `produces` | Study | ResearchProduct | Identifies a study output. |
| `scoredWith` | InstrumentUse or Result | ValueSet | Identifies the scoring algorithm, not only the descriptive system. |
| `hasResult` | Study or Analysis | Result | Links exact evidence to its context. |
| `supportsFinding` | Result | Finding | Keeps the evidence for a bounded claim. |
| `cites` | Publication | Publication | Requires citation evidence from a named source. |
| `derivedFrom` | DerivedAnalytic | Assertion, entity set, or analytic | Makes computation lineage explicit. |

Inverse relations can be shown in the user interface. The stored semantic direction must remain stable.

## 7. Representation of key research facts

### 7.1 Populations and samples

Represent the target population separately from each observed sample. Store age thresholds, participant role, condition, geography, language ability, and eligibility as structured values when the source is exact. Keep complex quota rules and exclusion reasons as both structured facts and source text.

Represent waves and groups explicitly. This is necessary for S078, which has four heatwave-related waves, and S091, which has T1 and T2 plus four mutually exclusive T2 health groups. It also prevents a retest sample from being confused with the full sample.

### 7.2 Instruments and versions

Use the exact version as the primary search object. Link it to its family for broad search. Give each instrument use a role. Keep language, locale, mode, perspective, recall period, and value-set scoring separate.

For a translation study, record the reference version, forward and back translation, cognitive debriefing, target language version, and approval or review body only when the summary reports them. For a bolt-on study, record each bolt-on as a candidate dimension and keep its evidence type. Content-validity support does not equal a scored or valued extension.

### 7.3 Methods and protocols

Record a method at task level when the design affects interpretation. For cTTO, keep conventional and lead-time components, duration, health-state design, feedback module, and exclusion or censoring rules. For DCE, keep duration, death comparator, task structure, blocking, and scale.

Record protocol version independently from method. A study can use cTTO without a reported numbered EQ-VT version. Unknown version stays unknown.

### 7.4 Analyses and models

Create one `Analysis` for each materially different outcome, sample, or model comparison. Link candidate and final models to their roles. Store adjustment variables, censoring point, constants, scale parameters, and sensitivity exclusions when supplied.

An exact final model is part of a value-set identity. For example, `hybrid model` alone is not sufficient to distinguish the UAE preferred hybrid heteroskedastic Tobit model censored at -1 from the Danish heteroscedastic censored hybrid model or the Polish Bayesian hybrid model.

### 7.5 Products

Do not assume that every valuation paper produces a value set. A method-comparison paper can estimate values for comparison without issuing a national product. Also, a study can collect both cTTO and DCE but select a cTTO-only final value set, as in S001.

Crosswalk direction is mandatory. `EQ-5D-5L to EQ-5D-3L crosswalk` is different from a native EQ-5D-5L value set and from mapping DCE latent values to TTO values.

### 7.6 Outcomes and findings

Keep observations, model estimates, and interpretations separate. A result such as `adjusted R-squared increased from 0.542 to 0.565 after adding breathing` is a model result. The conclusion that a breathing bolt-on adds explanatory value is a finding. The conclusion must retain its sample of non-hospitalized patients after COVID-19.

Store negative and null results. Store `not tested` as scope metadata only when the source explicitly states it. S061, for example, did not produce psychometric or preference evidence. This fact prevents a search for an EQ-TIPS value set from returning the paper as if it produced one.

## 8. Publication, study, project, and analytic separation

| Object | Identity | Dates | Typical relations | Must not be used as |
|---|---|---|---|---|
| Publication | DOI or publication-local identity | publication, online, accepted, or issue date, with date type | reports study; has authors; cites publication | study identifier, project identifier, or grant |
| Study | local study identity | data-collection and follow-up dates | has population, sample, instrument use, method, analysis, result, product | publication or funded award |
| Funded project | project or award identifier | start, end, decision, and status dates | funded by; hosted by; has applicants; supports study; has outputs | proof that all nearby publications are outputs |
| Derived analytic | analytic identity and version | computation and data-cutoff dates | derived from a defined entity set and method | source-reported fact or paper finding |

A paper can report a secondary analysis of a larger project. A project can generate several studies and publications. Several projects can support one publication. One study can use data from another study or dataset. The ontology permits all these patterns.

The source summaries contain project identifiers. The ontology records them first as `reportsProjectReference`. It promotes a reference to `conductedUnderProject`, `outputOfProject`, or `fundedBy` only when an explicit statement supports the stronger relation.

## 9. Derived analytics

Each `DerivedAnalytic` has:

- a question or analytic type;
- an input entity set and inclusion rule;
- data sources and version identifiers;
- an as-of date;
- a formula or documented method;
- numerator and denominator for a share;
- deduplication and identity-resolution rules;
- treatment of unknown values;
- output value and uncertainty when relevant;
- computation status and provenance.

Question-supported analytic types include:

| Analytic type | Required computation rule |
|---|---|
| count or status distribution | State the counted entity type and use distinct identifiers. Do not count publications as projects. |
| share | Store numerator, denominator, exclusions, and unknowns. |
| publication lag | Select project start and first verified output date; state treatment of censored projects. |
| topic mix over time | State the topic scheme, unit of analysis, time bin, and multi-topic weighting. |
| semantic similarity | Store the query text, compared text field, method version, score, and cutoff. |
| citation impact | Store citation source, retrieval date, coverage, and self-citation rule. |
| citation network | Store nodes, directed edges, components, hub metric, and data cutoff. |
| collaboration network | Store author identity rules, edge definition, time window, and counting method. |
| citation lag | Use the cited and citing publication dates with defined date types. |
| output concentration | Define PI set, output attribution, top-decile rule, ties, and fractional or full counting. |
| funding split | Use approved award amounts, currencies, exchange-date rule if combined, and project-to-instrument assignments. |
| impact profile | Assemble outputs, citations, and collaborators as separate sections. Do not convert them into one unexplained score. |

An analytic result changes when source coverage or identity resolution changes. Keep each version instead of overwriting the earlier result.

## 10. External linked data needed for portfolio questions

The following linked records are within ontology scope but are not supplied by the paper summaries:

- project title, abstract, start and end dates, status, award class, approved budget, currency, applicants, PI, host, and working group;
- verified project-to-study, project-to-product, and project-to-publication links;
- complete bibliographic author lists, publication dates, journals, reference lists, and open-access status;
- researcher profiles, ORCID identifiers, membership history, and affiliations;
- identity-resolution decisions and their audit log;
- citation edges and citation counts with a dated source;
- venue metrics with metric name and year;
- corpus inclusion and exclusion decisions;
- proposal abstracts and proposal reference lists supplied at query time;
- a controlled place hierarchy for country-to-region queries.

Each external record needs a source-system identifier, retrieval date, and link assertion. The ontology must show external facts separately from paper-derived facts.

## 11. Competency-question coverage

The status values in this section are:

- **S — Summary-answerable:** The supplied 50 summaries contain the facts for an answer limited to this supplied set.
- **L — Linked data required:** The ontology supports the question, but a complete answer needs external project, bibliographic, identity, membership, citation, journal, workflow, geographic, or query-time data.
- **U — Unsupported:** The supplied evidence does not support a positive or exhaustive answer. The ontology must not infer one from absence.

All **S** answers have a fixed-set limit. They do not claim that the 50 summaries are a complete world bibliography.

| Question | Required concepts and relations | Status and answerability |
|---|---|---|
| Q32 | WorkingGroup `associatedWith` FundedProject; Project `outputOfProject` Publication; project and publication dates | **L.** Working-group links, verified project outputs, and project dates are not in the summaries. |
| Q81 | Researcher; resolved IdentityProfile; ORCID identifier; identity status; share analytic | **L.** A resolved researcher set and ORCID coverage data are required. |
| Q13 | TopicAssignment on projects or publications; dates; topic-mix analytic | **L.** The summaries support topics for this set, but a portfolio trend needs the full portfolio, stable topic scheme, and dates. |
| Q18 | Proposal abstract; Project abstract; funding status; semantic-similarity analytic | **L.** The proposal abstract and project abstracts are query-time or project-system data. |
| Q66 | student-grant class; Project-to-Publication link; Study; Finding | **L.** Findings can come from summaries after outputs are linked, but student-grant and output records are absent. |
| Q51 | InstrumentFamily EQ-TIPS; develops/evaluates roles; Publication; Study; Product and evidence status | **S.** S061 is the supplied EQ-TIPS record. It reports expert consultation on experimental EQ-TIPS V2.0/EQ-TIPS-3L. It reports no value set and no psychometric or preference evidence. |
| Q43 | ValueSet; producing Study; explicit FundingContribution or explicit no-funding assertion | **L.** Missing funding text is not evidence of no funding. Verified funding records or explicit declarations are required. |
| Q7 | Project start date; verified first Publication output date; median-lag analytic | **L.** Project dates and complete output links are absent. |
| Q82 | Publication metadata record; metadata-quality flag; flag type and audit source | **L.** The summaries are not the metadata-quality audit log. |
| Q89 | FundedProject; outputs; Citation; authors/collaborators; impact-profile analytic | **L.** Project output, citation, and identity data are required. |
| Q31 | active Project status; TopicAssignment for EQ-HWB valuation; current Researcher role | **L.** `Currently` needs a dated project and personnel source. Publication authorship is not proof of current work. |
| Q35 | Study classification `condition-specific-to-generic mapping`; source and target InstrumentVersion; Crosswalk | **U.** No supplied summary reports a study that maps a condition-specific instrument to EQ-5D. S073 is a 5L-to-3L crosswalk, and S007 is DCE-to-TTO scale anchoring. Neither satisfies this question. |
| Q47 | Researcher; dated Membership; Authorship; verified funded output | **L.** Full authorship, membership, identity, and output-link data are required. |
| Q79 | Publication; directed Citation edges; components and hub analytic | **L.** Citation edges are absent. |
| Q74 | Researcher identity; first corpus-authorship date; rolling time window | **L.** Complete authorship history and resolved identities are required. |
| Q59 | EQ-HWB introduction classification; Publication; access status | **L.** S058 supplies development context, but open-access status and an agreed `introduces` rule need linked bibliographic curation. |
| Q80 | Project `outputOfProject` Publication; Publication `cites` Publication; inter-project flow analytic | **L.** Both citation edges and verified output links are absent. |
| Q76 | Publication with two or more verified `outputOfProject` relations | **L.** One project reference in a summary does not establish complete project linkage. |
| Q57 | Project type valuation; FundingContribution; MethodUse; distinct-project frequency analytic | **L.** The summaries supply exact methods, but complete funded-project membership and project deduplication need linked project data. |
| Q20 | active Project; project aims; Proposal aims; similarity/overlap analytic | **L.** Current status, project aims, and proposal text are not all supplied. |
| Q16 | funded Project; national EQ-5D-5L valuation Study; country; project date | **L.** The summaries supply several country valuation studies, but an exhaustive prior-funding answer needs the full project register and explicit funding links. |
| Q1 | distinct FundedProject; approved budget; currency; status; sum analytic | **L.** Budgets and the complete project register are absent. |
| Q99 | Authorship; dated Membership; corpus inclusion decision; pure-application exclusion class; share analytic | **L.** Membership and exclusion decisions are absent. |
| Q24 | funded valuation Project; country-to-region relation; exact MethodUse; distinct-project counts | **L.** Methods are in the summaries, but funding links and a controlled region assignment are required. |
| Q58 | EQ-5D-Y-5L InstrumentUseRole; Publication; Study purpose | **S.** The supplied direct records are S039 for Canadian stakeholder views on Y-3L versus Y-5L, S051 for Modern Standard Arabic translation and adaptation, and S062 for Singapore English adaptation of Y-3L and Y-5L plus Y-3L content validity. |
| Q55 | funded Project; host Organization; verified host relation; ranking analytic | **L.** Project hosts are not supplied. Author affiliations must not substitute for hosts. |
| Q12 | funded output link; Citation count with date/source; Project | **L.** Citation counts and verified project outputs are absent. |
| Q9 | Project completion date/status; verified output links; as-of date | **L.** Project status, completion dates, and complete output links are absent. |
| Q73 | Publication date; resolved Authorship; publication-time affiliation country; country-count trend | **L.** Full authorship and affiliation histories are absent. |
| Q4 | Project status with effective date; distinct-project count | **L.** Project status records are absent. |
| Q94 | resolved co-authorship edges; publication dates; decade bins; network-growth analytic | **L.** Complete authorship and identity data are required. |
| Q22 | Applicant role; successive grants; project start; first verified output date | **L.** Applicant roles, grant history, and output dates are absent. |
| Q33 | same Sample administered 3L and 5L; `scoredWith` value sets; comparison Analysis | **S.** S073 directly compares US 3L, native US 5L, and 5L-to-3L crosswalk scoring in datasets whose respondents completed both systems. S090 compares 3L and 5L in the same late-onset Pompe disease sample. S097 administers both versions to the same older German care sample. S071 is a systematic review, not one same-population primary study. |
| Q65 | youth-instrument TopicAssignment; Publication journal; distribution analytic | **L.** The supplied set does not give complete journal metadata or a complete youth-paper denominator. |
| Q30 | ValueSet; `usesProtocol`; exact protocol version; producing Study | **S.** Source-reported records are S029 Indonesia, EQ-VT 2.0; S004 UAE, EQ-VT with version not stated; S001 Sweden, EQ-VT 2.1; S005 Taiwan, EQ-VT 2.0; S023 Denmark, EQ-VT 2.1; and S003 Poland, EQ-VT 2.0. S007 reports EuroQol Portable Valuation Technology for cTTO but gives no numbered EQ-VT version, so the ontology keeps that source term separate. |
| Q87 | IdentityProfile; IdentityResolutionDecision; decision reason, actor, time, and input profiles | **L.** The required workflow audit is not in paper summaries. |
| Q11 | funded Project; approved budget; host country; currency treatment; ranking analytic | **L.** Award budgets, hosts, and complete country links are absent. |
| Q88 | funded output; Journal; venue metric name/year/source; ranking analytic | **L.** Funding links and venue metrics are absent. |
| Q77 | Project PI role; project outputs; resolved identities; top-decile concentration analytic | **L.** PI roles and verified project outputs are absent. |
| Q86 | directed Citation; citing and cited publication dates; citation-lag analytic | **L.** Citation edges are absent. |
| Q28 | Proposal reference list; Publication identifiers; corpus inclusion; funded-output link | **L.** The reference list is a query-time input, and funded-output links need external records. |
| Q84 | resolved Researcher; dated Membership; distinct counts and unknowns | **L.** Complete authorship, identity, and membership data are absent. |
| Q78 | resolved co-authorship; dated Membership; member/non-member classification; frequency analytic | **L.** Identity, authorship, and membership data are required. |
| Q62 | current or publication-time Affiliation; Organization; TopicAssignment; Researcher | **L.** The question must state which affiliation time it means. Complete affiliations are absent. |
| Q44 | Researcher work output; WorkingGroup; dated group-project or group-topic relation | **L.** Working-group assignments and resolved identities are absent. |
| Q54 | InstrumentCrosswalk; native ValueSet; source and target version; comparison Publication | **S.** A native 5L value set directly estimates values for 5L states from 5L valuation data. A 5L-to-3L crosswalk predicts 3L-value-set scores from 5L descriptions. S073 is the key direct comparison. S001, S003, S004, S005, S023, and S029 are supplied native 5L value-set references. S007 is scale anchoring, not an instrument crosswalk. |
| Q50 | valuation Study; TTO MethodUse; DCE MethodUse; ValueSet; method contribution to final product | **S.** S029, S004, S005, S023, and S003 report both inputs and select hybrid final value sets. S007 combines DCE with separate cTTO data through power scale anchoring for the Indonesian Y-3L value set. S001 reports both methods but selects a cTTO-only final value set. S019 is a method-comparison study and is not identified as a produced national value set. |
| Q25 | student-grant Project; verified Publication output; share analytic | **L.** Student-grant classification and complete output links are absent. |
| Q69 | Publication inclusion record; publication date; annual count with date rules | **L.** The 50-summary packet is not the complete included corpus since 1990. |
| Q10 | FundedProject; approved budget; Project-to-InstrumentFamily assignment; currency rule; split analytic | **L.** The summaries support instrument-family assignments for studies, but not the complete award amounts or project portfolio. |

## 12. Complete example records

The examples show the proposed semantic record. They do not add facts beyond the named summaries. Unstated fields remain unknown.

### 12.1 Example 1: Indonesian EQ-5D-5L value set

**Evidence source**

- Source summary: S029.
- Summary title: *The Indonesian EQ-5D-5L Value Set*.
- Summary SHA-256: `b059ef6dbad0475276b0acbd0ebece29de7cd02855a2b2d1cdedf629429cb402`.
- The summary identifies DOI `10.1007/s40273-017-0538-9` and project reference `2013240`.

**Publication and study**

- Publication: Indonesian national EQ-5D-5L valuation and value-set report.
- Study classifications: national valuation; value-set production; quantitative preference study.
- Aim: derive a societal Indonesian EQ-5D-5L value set for QALY-based economic evaluation.
- Target population: Indonesian general population aged 17 years or older.
- Sampling: multi-stage stratified quota design for residence, sex, age, education, religion, and ethnicity.
- Setting: six cities and surrounding areas: Jakarta, Bandung, Jogjakarta, Surabaya, Medan, and Makassar.
- Analytic sample: 1,054 completed interviews.
- Language version administered: official Bahasa Indonesia EQ-5D-5L.
- Administration: computer-assisted, interviewer-administered, face-to-face.
- Data collection: 9 March 2015 to 24 January 2016.

**Instrument and method use**

- Valued instrument version: EQ-5D-5L.
- Components administered: descriptive system and EQ VAS.
- Protocol: EQ-VT 2.0.
- Preference methods: cTTO and duration-free DCE.
- cTTO components: conventional TTO for better-than-dead states and lead-time TTO for worse-than-dead states.
- Per respondent: 10 cTTO states and seven forced-pair DCE comparisons.
- Design: 86 cTTO states and 196 DCE pairs in 28 blocks.
- Quality process: 102 early interviews were treated as pilot interviews and excluded after quality review and interviewer retraining.
- Modelled observations: 9,462 cTTO observations after stated removals and 7,378 DCE observations.

**Analysis and product**

- Candidate analyses: Tobit cTTO censored at -1, conditional-logistic DCE with rescaling, and hybrid regression.
- Final product: Indonesian EQ-5D-5L value set.
- Final model: hybrid main-effects model.
- Scale: 11111 equals 1.000; values below zero represent states worse than dead.
- Selected values: 11112 equals 0.921; 55555 equals -0.865; example state 12345 equals 0.240.
- Negative state count: 1,108 of 3,125 states, or 35.46%.
- Intended uses reported by the source include HTA, economic evaluation, PROM research, clinical trials, and hospital-care research.

**Results and findings**

- Observed cTTO means ranged from -0.719 for 55555 to 0.909 for 12111.
- The source reports high correlations between cTTO, rescaled DCE, and hybrid predicted values.
- The final model ranks mobility as the dimension with the greatest effect and pain/discomfort as the least.
- The source reports Java concentration and quota-recruitment limits. It does not establish island-specific preferences.

Every fact above has `supportedBy S029`. The project reference stays a project-reference assertion unless separate evidence verifies the output or funding relation.

### 12.2 Example 2: EQ-TIPS expert consultation

**Evidence source**

- Source summary: S061.
- Summary title: *Developing the EuroQol toddler and infant populations (EQ-TIPS) instrument: qualitative analysis of expert views on content validity and conceptual challenges*.
- Summary SHA-256: `19e062b813b6014b8d70f92eda57e18e430a7bc53053b0faa94666bca8ff31f3`.
- The summary identifies DOI `10.1007/s11136-025-04150-3` and project reference `365-RA`.

**Publication and study**

- Publication type: qualitative peer-reviewed research article.
- Study classifications: instrument development; qualitative content-validity consultation; conceptual study.
- Aim: review EQ-TIPS V2.0 wording and content and examine uses and development challenges.
- Data collection: three online semi-structured focus-group consultations on Zoom from December 2022 to February 2023.
- Sample: 33 experts from 15 countries.
- Groups: EuroQol experts, paediatric health and development experts, and paediatric HRQoL instrument developers.
- Sampling: purposive expert selection.
- Analysis: Braun and Clarke six-phase thematic analysis, mainly deductive with permitted inductive themes, using NVivo Version 14.

**Instrument under development**

- Instrument family: EQ-TIPS.
- Exact version: experimental EQ-TIPS V2.0, described as EQ-TIPS-3L.
- Intended population: infants and toddlers, with a proposed age range of 0 to 3 years.
- Dimensions: Movement, Play, Social Interaction, Communication, Eating, and Pain.
- Response levels: no, some, and a lot of problems.
- Proxy measure: yes.
- EQ VAS: proxy rating of the child's overall health from 0 to 100.
- Value-set status: planned, not produced in this study.
- Five-level version status: not available for testing in this study.

**Results and findings**

- Most experts found the instrument short and easy to complete and suitable for trials and research.
- The source reports uncertainty about whether the construct is health, health status, HRQoL, or development.
- Experts generally preferred age-relevant content over direct mapping to later-life EQ-5D dimensions.
- Sleep was widely proposed as an additional dimension. Emotions were also proposed. Bowel habits had little support.
- Communication and Social Interaction can overlap.
- Proxy characteristics, caregiver HRQoL, and spillover can affect proxy reports and should be recorded.
- The study did not test caregivers or children directly and did not produce psychometric or preference evidence.

This record can answer what EQ-TIPS work exists in the supplied set. It cannot answer whether a valued or validated EQ-TIPS product exists outside the supplied set.

### 12.3 Example 3: native 5L value set versus crosswalk

**Evidence source**

- Source summary: S073.
- Summary title: *EQ-5D-5L measurement properties are superior to EQ-5D-3L across the continuum of health using US value sets*.
- Summary SHA-256: `e22a331a0bb5d8202b25eb3bb4b06eb3f631f78a4a13871bd2c477a128e83e1a`.
- The summary identifies DOI `10.1186/s12955-022-02031-8` and project reference `20190360`.

**Study and inputs**

- Study classifications: comparative measurement study; comparative value-set analysis; theoretical and empirical analysis.
- Compared products: US EQ-5D-3L value set, native US EQ-5D-5L value set, and EQ-5D-5L-to-EQ-5D-3L crosswalk value set.
- Data source 1: 1,133 respondents in the 2017 US 5L valuation study.
- Data source 2: 3,790 respondents in an international 3L/5L parallel-fielding dataset.
- Same-population property: respondents in both data sources completed both descriptive systems and EQ VAS.
- Analyses: theoretical range and transition comparisons, ANOVA F-statistic ratios, bootstrap resampling, and a VAS-weighted responsiveness simulation.

**Exact product roles**

- The native US 5L value set directly scores EQ-5D-5L states.
- The crosswalk predicts 3L-value-set scores from 5L descriptions.
- The US 3L value set directly scores EQ-5D-3L states.
- None of these relations is a condition-specific-to-EQ-5D mapping.

**Selected results**

- Range: 1.573 for native 5L and 1.109 for both 3L and crosswalk.
- Worse-than-dead states: 620 of 3,125 for native 5L; 10 of 243 for 3L; 39 of 3,125 for crosswalk.
- Gap from 11111 to the next-best state: 0.057 for native 5L, 0.140 for 3L, and 0.112 for crosswalk.
- Mean single-level transition: 0.078 for native 5L, 0.111 for 3L, and 0.061 for crosswalk.
- Finding: the authors interpret native 5L as having better interval properties, discrimination, and responsiveness in the tested data and simulations.
- Limitation: the study did not use trial or longitudinal data, and evidence was limited for very poor health.

This record supports Q33 and Q54 while preserving the difference between a native value set and a crosswalk.

## 13. Free text, optional facts, derived facts, and outside scope

### 13.1 Facts that remain free text

Keep these facts as source text, with optional controlled tags:

- detailed aims and rationale;
- complex eligibility and exclusion rules;
- qualitative themes, cultural concepts, and participant explanations;
- interviewer problems and proposed solutions;
- limitations and author cautions;
- possible causal explanations that were not tested;
- recommendations and intended uses;
- exact wording disputes in translation and adaptation;
- unusual task instructions or experimental-design details that do not yet justify a controlled value.

For example, `positive/negative energy` and `mindset` in S067 must keep their exact translation context. A broad mental-health tag is not an adequate replacement.

### 13.2 Optional structured facts

Structure these facts when available and useful:

- ethics approval;
- software and version;
- respondent incentive;
- conflict-of-interest statement;
- data and code availability;
- interviewer training;
- quality-control thresholds;
- recruitment channels;
- sensitivity-analysis rules;
- source-reported intended use.

Absence of an optional field means unknown.

### 13.3 Derived facts

Counts, shares, medians, rankings, trends, topic similarity, components, hubs, citation lag, collaboration growth, output concentration, and impact profiles are derived. Store the analytic definition and lineage with each result.

Do not copy a derived portfolio rank into the publication record. The rank changes when the corpus or citation data changes.

### 13.4 Outside scope or linked only

The ontology does not make raw participant data, confidential grant applications, financial transaction records, private reviewer comments, or full identity evidence part of the public research-fact layer. It can keep governed links and access conditions.

The ontology also does not make a normative judgment about the best valuation method, value set, instrument, or funding decision. It represents the evidence and the authors' bounded findings.

## 14. Validation and quality rules

1. A DOI identifies a publication, not a study or project.
2. A project identifier does not prove research funding, project output, or sole funding.
3. A publication date has a date type. Do not mix accepted, online, issue, and data-collection dates.
4. An instrument family search can include versions. An exact-version search cannot use family-only records as exact matches.
5. A health-state code always has an instrument version.
6. A value always has a scale or value set.
7. A sample size always has a sample stage and, when supplied, a timepoint.
8. A percentage has a denominator or a source-reported-value marker.
9. A model has a role. Only a source-selected final model defines the final value-set product.
10. A crosswalk has a source and target. Scale anchoring is not an instrument crosswalk.
11. A funding assertion states the funder, target, contribution type, and source.
12. A negative claim needs explicit negative evidence or a documented closed-world rule.
13. A current-state query has an as-of date.
14. A researcher count uses resolved identities and reports unresolved profiles.
15. A network analytic states its node, edge, time, and counting rules.
16. Conflicting source values remain in a `ConflictSet` until resolution.

S004 gives a useful conflict test. Its abstract reports average age 39 years with SD 10.8, while its Results report mean age 32.1 with SD 11.4. The ontology must keep both source-backed estimates and mark the discrepancy unresolved. It must not average them or select one silently.

## 15. Unresolved design choices and risks

### 15.1 Study boundaries

A publication can contain a main study, a pilot, a secondary analysis, and sensitivity analyses. Curators need a rule for when these become separate `Study` records instead of nested activities. The rule must favor different populations, data collections, or aims as evidence for separation.

### 15.2 Project links

The packet gives project identifiers, but the semantic strength of each identifier can vary. A project registry must verify whether the identifier means funding, administrative grouping, source-corpus folder, or output attribution.

### 15.3 Instrument status and naming

Experimental forms can change. EQ-HWB-S, derived EQ-HWB-9, and future short forms need version histories. EQ-TIPS V2.0 and a future five-level form must remain separate. The registry needs a documented rule for official, experimental, derived, and locally adapted status.

### 15.4 Method aliases

Terms such as `DCE`, `DCEd`, `DCE-duration`, and `paired comparison` can overlap in source use. Terminology mappings need human review and task-level facts. `EuroQol Portable Valuation Technology` also needs review before it is mapped to a numbered EQ-VT protocol.

### 15.5 Mapping ambiguity

The word `mapping` has at least three meanings in this evidence set. The ontology must require source and target objects and a mapping class. Otherwise Q35 and Q54 will return false matches.

### 15.6 Population overlap

Several papers can use the same project, cohort, or valuation dataset. Counts of studies, samples, and participants can be inflated if shared data are not linked. Dataset and cohort identity need evidence-backed resolution.

### 15.7 Finding granularity

Very narrow findings give accurate context but can make synthesis difficult. Very broad findings lose population, instrument, and model conditions. A practical rule is one claim, one direction, one main context, and links to all supporting results.

### 15.8 Topic classification

Portfolio trends and similarity need a stable topic scheme. Multi-topic studies require either fractional weights or clear multiple assignment. The analytic record must state the rule. Instrument mention alone must not define a topic.

### 15.9 Identity and membership

Author-name matching can merge different people or split one person. Membership also changes over time. Researcher and member analytics must retain unresolved profiles and the full identity-resolution audit.

### 15.10 Citation and venue measures

Citation counts and venue metrics change and have source-specific coverage. Every value needs a source, metric date, and retrieval date. `Highest impact` is not meaningful without the named metric and year.

### 15.11 Unknown and negative evidence

Open-world data can answer positive existence questions more safely than exhaustive negative questions. Queries such as no publication, no funding, or no prior study require a documented closed dataset and coverage date.

### 15.12 Source-summary limits

The summaries are dense but are still secondary evidence artifacts. They sometimes state that a fact is missing, ambiguous, or internally inconsistent. The ontology must show this limit and must not reconstruct missing facts from general knowledge.

## 16. Input and validation audit

- The SHA-256 value of each of the 50 listed summary files matched `A-papers.tsv`.
- The proposal used all 50 summaries and all 50 competency questions.
- Packet-allowlist inputs read: `README.md`, `ONTOLOGY_TASK.md`, `packets/A-papers.tsv`, `packets/A-questions.md`, and the 50 summary files listed in `A-papers.tsv`.
- Files or resources read outside the packet allowlist: `AGENTS.md` only.
- No source paper, other packet, other proposal, prior ontology experiment, graph model, extraction schema, Git history, skill, framework, standard, or web source was read or used.
