# EuroQol research ontology proposal C

## 1. Purpose and scope

This ontology supports search, comparison, and synthesis of EuroQol research. It centers on exact research facts. It does not treat a publication title or a broad topic as a substitute for those facts.

The evidence base for this proposal is the 50 supplied summaries. All 50 summary SHA-256 values matched the packet manifest. A summary is the immediate evidence source for this proposal. The underlying paper is not treated as reviewed evidence.

The ontology must support these tasks:

- find a study by its exact study purpose, instrument version, population, country, method, model, product, outcome, or finding;
- compare studies without merging facts that have different contexts;
- show the evidence for a project-to-output link;
- keep a publication, a study, a funded project, and a calculated corpus statistic separate;
- state when a requested answer needs linked data that is not in the summaries;
- preserve missing, conflicting, planned, and not-applicable values without invention.

The scope includes research management facts when they are necessary for the competency questions. Examples are projects, awards, people, organizations, memberships, working groups, output links, citations, and identity-resolution decisions. Most of these facts need linked data outside the supplied summaries.

This proposal does not impose one record shape on all papers. A national valuation study, a psychometric comparison, a systematic review, a qualitative instrument-development study, and a routine-outcome study have different fact patterns.

## 2. Four semantic layers

The ontology uses four layers. Each layer has a different purpose.

| Layer | Main record | Meaning | Rule |
|---|---|---|---|
| Source layer | `SourceSummary`, `SourceAssertion`, `SourceTerm` | What a supplied summary reports, with its wording and location | Do not silently correct, complete, or normalize the report |
| Canonical layer | `CanonicalEntity` and its typed subtypes | The stable research entity that multiple source expressions can identify | Keep identity separate from labels and classifications |
| Classification layer | `ClassificationAssignment` | A controlled interpretation, such as `valuation study` or `test-retest reliability` | Record the scheme, scope, reason, and evidence |
| Analytic layer | `DerivedAnalytic` | A calculated result, such as a median, count, rank, timeline, share, or similarity score | Record the input set, rule, time cut-off, and calculation version |

This separation is mandatory. For example:

- “composite time trade-off” in a summary is a `SourceTerm`.
- `composite time trade-off` is the canonical method label.
- `preference elicitation method` is its controlled method family.
- “cTTO is the most frequent method” is a `DerivedAnalytic`, not a source fact.

### 2.1 Source assertions and provenance

A `SourceAssertion` is the smallest evidence-bearing unit. It contains:

- the summary ID and summary path;
- the summary SHA-256 value;
- the subject, relation, and object or literal value;
- the source section or locator when the summary supplies one;
- the source term and a canonical term, if normalization occurs;
- an evidence status: `reported`, `explicitly not reported`, `planned`, `not produced`, or `source conflict`;
- a value quality: `exact`, `approximate`, `range`, or `unclear`;
- the agent and date for a curator classification or calculation.

The ontology does not use one unqualified null. It distinguishes these cases:

- `not reported`: the summary does not give the fact;
- `not applicable`: the fact does not apply to the record;
- `not produced`: the study explicitly did not make the product;
- `planned`: the product or work was a stated future action;
- `unknown`: the available evidence cannot establish the value;
- `conflicting source assertions`: the supplied summary reports two incompatible source values.

### 2.2 Terms, aliases, and canonical labels

Each term record can have:

- the exact source form;
- one canonical label;
- an abbreviation;
- an alias;
- the language;
- the instrument or method context;
- the evidence source for the mapping.

For example, `EQ VAS` and `EQ-VAS` can map to one canonical concept. Both source forms remain available. `Pain/Discomfort` in adult EQ-5D and `having pain or discomfort` in EQ-5D-Y remain different instrument-bound labels, even when a broader comparison class links them.

No external ontology or classification standard is adopted in this proposal. The controlled terms come from the supplied summaries and competency questions. DOI strings and source project IDs are retained as identifiers, not as evidence that two records are the same type of thing.

## 3. Research identity and management concepts

### 3.1 Core entities

| Concept | Meaning for a EuroQol researcher | Important boundary |
|---|---|---|
| `Publication` | A published or accepted research output with a title and identifier | It is not the study that it reports |
| `Study` | A planned and executed research activity with an aim, design, population, methods, and results | One publication can report more than one study; one study can have more than one publication |
| `FundedProject` | A managed body of work identified by a project ID, with an aim and period | It is not inferred only from a shared topic or author |
| `FundingAward` | The funding decision, approved amount, currency, dates, and recipient facts | It is separate from the project and from a publication funding statement |
| `ResearchOutput` | A publication, dataset, instrument version, value set, protocol, program, or other project product | A project-output relation needs evidence |
| `ProjectOutputLink` | A claim that a project produced or supported an output | It stores link status, evidence type, evidence source, and decision history |
| `Proposal` | A proposal abstract and its target concepts, supplied at query time | It is not a past project unless a source says so |
| `Person` | A resolved researcher identity | Names, author strings, ORCID values, and member status are separate facts |
| `Organization` | A university, funder, health service, facility, company, or other body | An organization name is not an institution-country fact without a location assertion |
| `Affiliation` | A person-organization relation for a stated time | Do not treat present affiliation as affiliation at publication time |
| `RoleAssignment` | A time-bound role, such as author, PI, applicant, interviewer, or working-group member | The role must name its project, output, group, or study context |
| `Membership` | A time-bound EuroQol membership assertion | It is needed before classifying an author as a member or non-member |
| `IdentityResolutionEvent` | A merge, override, skip, split, or manual decision about person identity | Keep before and after identities, reason, evidence, actor, and date |
| `CorpusMembership` | Inclusion or exclusion of an output in a defined corpus snapshot | Store the rule and reason, including `pure application` when used |
| `Citation` | A directed publication-to-publication citation assertion | It needs a source and a data snapshot |
| `TopicAssignment` | A source or analytic topic assigned to a publication or project | Preserve the topic source, score, and model or scheme version |

### 3.2 Required separation

The main research lineage is:

`FundedProject` supports `Study`; `Study` is reported by `Publication`; `Study` can create `ResearchProduct`.

These are separate relations. They are not one generic `related to` link.

A `ProjectOutputLink` connects a project to a publication or another output. Its evidence can be:

- an explicit project ID in the supplied summary;
- an explicit funding statement in the supplied summary;
- an external project output list;
- a manual decision with a recorded reason;
- a rejected candidate link.

Shared authors, similar dates, or similar topics can generate a candidate link. They do not by themselves prove the link.

## 4. Research-content concepts

### 4.1 Study, population, and sample

| Concept | Meaning | Required detail when reported |
|---|---|---|
| `StudyAim` | The question that the study addresses | Preserve the source wording and add controlled purpose assignments |
| `StudyDesign` | The overall design | Cross-sectional, longitudinal, qualitative, experimental, review, model, or mixed-method details |
| `TargetPopulation` | The population to which the study intends to apply | Age, condition, country, and respondent role are separate qualifiers |
| `RecruitmentPopulation` | The population from which participants were approached | Panel, registry, facility, community, or sampling frame |
| `Sample` | A defined set of participants or records | Sample-size type, count, dates, and inclusion rules |
| `SampleGroup` | A subgroup, study arm, cohort, or comparator | The grouping rule and parent sample |
| `ParticipantRole` | The role in the research | Patient, general-public valuer, caregiver, child, proxy, expert, stakeholder, or record |
| `Condition` | A health condition or study-defined status | Keep exact source term, canonical term, and aliases separate |
| `Setting` | The research or care setting | Country, region, facility, service, community, or online panel |
| `ObservationPeriod` | The time covered by data or follow-up | Separate data-collection dates, recall period, retest interval, and follow-up point |

Sample size is not one field. The controlled `SampleSizeType` family includes:

- `targeted`;
- `invited`;
- `eligible`;
- `consented`;
- `completed`;
- `analytic`;
- `retest`;
- `follow-up`;
- `stable retest subset`;
- `records`;
- `task observations`.

This distinction is necessary for questions about typical valuation-study sample sizes. It also prevents a task-observation count from being treated as a participant count.

### 4.2 Instruments and forms

| Concept | Meaning | Example distinctions from the summaries |
|---|---|---|
| `InstrumentFamily` | A broad instrument lineage | EQ-5D, EQ-5D-Y, EQ-TIPS, EQ-HWB |
| `InstrumentVersion` | A named descriptive-system version | EQ-5D-3L, EQ-5D-5L, EQ-5D-Y-3L, EQ-5D-Y-5L, EQ-TIPS V2.0 |
| `InstrumentForm` | A reporter, length, or administration form | Self-report, proxy version 1, proxy version 2, EQ-HWB-S, EQ-HWB-9 |
| `DescriptiveSystem` | The set of dimensions and response levels | Five dimensions with three or five levels; six EQ-TIPS dimensions with three levels |
| `Dimension` | An instrument-bound health or wellbeing dimension | Mobility, self-care, pain/discomfort, play, communication, exhaustion |
| `ResponseLevel` | A version-bound response option | “some problems” and “a little bit of problems” are not interchangeable |
| `HealthStateProfile` | A profile in one exact descriptive system | 11111 for five-dimension systems; 111223 for six-dimension EQ-TIPS |
| `SupplementaryDimension` | A candidate or used bolt-on | Fatigue, hearing, sleep, cognition, energy, relationships |
| `TranslationOrAdaptation` | A language or cultural form and its development activity | isiXhosa EQ-TIPS; Simplified Chinese EQ-HWB v1.1 |
| `InstrumentStatusAssertion` | Status in a specified source and time | Experimental, in development, officially launched, planned, or not reported |

An instrument family is not sufficient for search when a study uses an exact version. A study that uses EQ-5D-Y-3L must not be returned as an EQ-5D-Y-5L study unless the query asks for the family.

A bolt-on record contains the base instrument version, added dimension, wording version, response levels, use status, and study role. The controlled use status is `candidate`, `tested as added item`, `included in survey`, or `proposed for future work`. These statuses must not be merged.

### 4.3 Administration, language, reporter, and perspective

An `Administration` connects a sample, an instrument form, and a time point. It can contain these independent axes:

- interaction: `self-completed`, `interviewer-administered`, or `assisted self-completion`;
- reporter: patient, child, caregiver, staff, relative, clinician, or general-public valuer;
- perspective: self, proxy-person, proxy-proxy, another adult, own child, child of a stated age, or child of unspecified age;
- channel: paper, web, tablet, REDCap, video interview, Zoom, telephone, or face-to-face;
- setting: home, hospital, community, care facility, public place, or remote;
- instrument language;
- interview language;
- recall period;
- task framing.

These axes must stay separate. For example, a caregiver can complete a proxy form on paper from a proxy-person perspective. “Proxy” alone does not give all three facts.

### 4.4 Methods, protocols, and task designs

| Concept | Meaning |
|---|---|
| `MethodFamily` | A controlled broad method, such as preference elicitation, psychometric testing, qualitative analysis, or evidence synthesis |
| `MethodImplementation` | The method as used in one study, with sample, framing, duration, task count, and administration |
| `Protocol` | A named procedure and version |
| `TaskDesign` | The states, pairs, blocks, durations, order, overlap, and randomization used in a task |
| `QualityControlRule` | A stated flag, exclusion, retraining, or monitoring rule |
| `Analysis` | A defined analysis of specified data |
| `StatisticalModelSpecification` | The exact model, not only a broad model family |
| `ModelSelectionDecision` | A decision that marks a model as preferred, rejected, or used for sensitivity analysis, with a reason |

The preference-elicitation controlled family includes these supplied methods:

- time trade-off;
- conventional TTO for better-than-dead states;
- lead-time TTO for worse-than-dead states;
- composite time trade-off (`cTTO`);
- duration-free discrete choice experiment (`DCE`);
- discrete choice experiment with duration (`DCEd`);
- DCE-death;
- DCE-duration;
- lag-time TTO;
- visual analogue scale anchoring;
- location of dead (`LOD`);
- standard gamble;
- Online elicitation of Personal Utility Functions (`OPUF`);
- direct personal utility function tasks, including dimension ranking, swing weighting, level rating, and dead anchoring;
- pairwise choice;
- Kaizen preference-path tasks.

`Hybrid` is not a sufficient method label. The ontology separates:

- a hybrid statistical model that combines cTTO and DCE data;
- a DCE task that contains duration;
- a study that compares multiple elicitation methods.

Named protocol records supported by the summaries include `EQ-VT version 1.1`, `EQ-VT version 2.1`, and the `lite EQ-5D-5L valuation protocol` used with EQ-VT version 2.1. If a summary says only `EQ-VT`, its version remains `not reported`.

An exact model specification can use these controlled facets:

- response source: cTTO, DCE, DCEd, or combined data;
- estimator family: GLS, Tobit, conditional logit, mixed logit, OLS, power mapping, or Bayesian model;
- intercept form: fixed, random, or no constant;
- censoring and censoring point;
- variance form: constant or heteroskedastic;
- scale parameter;
- time-preference form: linear or nonlinear;
- main effects and interactions;
- weighting or reweighting;
- preferred, rejected, comparator, or sensitivity status.

Thus `hybrid heteroskedastic Tobit censored at −1` is a more useful fact than `regression model`.

### 4.5 Products and value sets

`ResearchProduct` has controlled subtypes:

- instrument version or form;
- translation or language adaptation;
- native value set or tariff;
- crosswalk;
- mapped utility function;
- scoring algorithm;
- valuation or administration protocol;
- dataset;
- survey infrastructure;
- implementation program or package;
- taxonomy or decision guidance.

A `ValueSet` record contains, when supplied:

- the target instrument version;
- the preference population and jurisdiction;
- adult or child perspective and hypothetical age;
- elicitation methods;
- protocol and exact version;
- task design;
- analytic sample sizes by type;
- preferred model specification;
- anchoring and worse-than-dead treatment;
- value range and selected state values;
- dimension ranking;
- publication and study that report it;
- product status and intended use.

The `ValueSetBasis` classification uses these controlled values:

- `native direct valuation`: preferences were elicited for the target descriptive system;
- `crosswalk`: values for one descriptive system were inferred from another descriptive system by response mapping;
- `mapped utility`: utilities were inferred from a different measure, such as SF-12; this is not called a native value set;
- `reanalysis or reweighting`: an existing preference dataset was analyzed again;
- `theoretical comparator`: a value set was used only in a theoretical comparison.

A native value set must have a jurisdiction and a target instrument version. Study country alone is not sufficient. A value set can use a hybrid cTTO-DCE model and still be native. `Crosswalk` describes the derivation basis, not the target instrument label.

### 4.6 Outcomes, estimates, comparisons, and findings

| Concept | Meaning |
|---|---|
| `OutcomeDefinition` | What was measured, with instrument, score, time, group, and direction |
| `ResultEstimate` | One numerical result in one context |
| `QualitativeTheme` | A reported theme, view, or recommendation with its participant and analysis context |
| `Comparison` | A defined contrast between two or more estimates, groups, instruments, methods, or products |
| `Finding` | A source-supported interpretation tied to estimates, themes, or comparisons |
| `Limitation` | A reported limit on design, data, interpretation, or generalization |

A `ResultEstimate` can contain:

- statistic type;
- value and unit;
- numerator and denominator;
- sample or subgroup;
- instrument version and score type;
- value set used for scoring;
- time point or interval;
- comparator;
- confidence interval, standard error, test statistic, and p value when reported;
- direction, where higher or lower has an explicit meaning;
- source assertion.

The measurement-property controlled family includes:

- feasibility and acceptability;
- missingness and completion;
- ceiling and floor effects;
- informativity;
- content validity;
- convergent validity;
- known-groups or discriminant validity;
- test-retest reliability;
- agreement;
- responsiveness;
- redistribution consistency;
- explanatory power.

A principal finding is not a bare text field. It links to its population, instrument, method, outcome, comparison, and evidence. A short source-faithful text statement can remain as its label.

## 5. Important relations

| Relation | From → to | Meaning and constraint |
|---|---|---|
| `reportsStudy` | Publication → Study | The publication reports the study |
| `reportedBy` | Study → Publication | Inverse of `reportsStudy` |
| `supportedByProject` | Study → FundedProject | The supplied or linked evidence states project support |
| `hasOutputLink` | FundedProject → ProjectOutputLink | The project has an evidence-bearing candidate or accepted output link |
| `linksToOutput` | ProjectOutputLink → ResearchOutput | The output at the other end of the link |
| `hasFundingAward` | FundedProject → FundingAward | Connects project activity to a funding decision |
| `hasAim` | Study or FundedProject → StudyAim | Keeps publication topic separate from aim |
| `hasDesign` | Study → StudyDesign | Records the study design |
| `hasPopulation` | Study → TargetPopulation | Records intended population |
| `hasSample` | Study → Sample | Records an actual participant or record set |
| `hasSubgroup` | Sample → SampleGroup | Records an arm, cohort, or subgroup |
| `hasCondition` | Population or SampleGroup → Condition | Gives the condition context |
| `locatedIn` | Study, Sample, Organization, or ValueSet → Place | The place role must also be stated |
| `usesInstrumentVersion` | Study or Administration → InstrumentVersion | Requires the exact version when reported |
| `usesInstrumentForm` | Administration → InstrumentForm | Records self or proxy form and length variant |
| `hasAdministration` | Study → Administration | Connects mode, reporter, perspective, language, and time |
| `hasDimension` | DescriptiveSystem → Dimension | The dimension is version-bound |
| `hasResponseLevel` | Dimension → ResponseLevel | The response wording is version-bound |
| `addsDimensionTo` | SupplementaryDimension → InstrumentVersion | Defines a bolt-on relation |
| `hasTranslation` | InstrumentVersion → TranslationOrAdaptation | Does not imply psychometric validation |
| `usesMethod` | Study or Analysis → MethodImplementation | Records the method as applied |
| `followsProtocol` | MethodImplementation → Protocol | Records the named protocol and version |
| `usesTaskDesign` | MethodImplementation → TaskDesign | Records blocks, states, tasks, duration, and framing |
| `appliesModel` | Analysis → StatisticalModelSpecification | Records the exact model |
| `selectedModel` | Analysis → ModelSelectionDecision | Records the preferred model and selection reason |
| `producedProduct` | Study → ResearchProduct | Requires a supplied assertion; planned products use `plansProduct` |
| `plansProduct` | Study or FundedProject → ResearchProduct | Does not mean the product exists |
| `targetsInstrument` | ValueSet or Crosswalk → InstrumentVersion | Records the scored descriptive system |
| `nativeFor` | ValueSet → PreferencePopulation | Used only for direct target-version valuation |
| `mapsFrom` | Crosswalk or MappedUtilityFunction → Instrument or Measure | Records the source measure |
| `hasOutcome` | Study → OutcomeDefinition | Records the measured outcome |
| `hasEstimate` | OutcomeDefinition → ResultEstimate | Connects outcome definition to a contextual result |
| `compares` | Comparison → entity or estimate | Each comparison has named sides and a direction |
| `supportsFinding` | ResultEstimate, Comparison, or QualitativeTheme → Finding | Gives a finding its evidence |
| `hasLimitation` | Study or Finding → Limitation | Keeps reported limits queryable |
| `authoredBy` | Publication → Person | Uses a resolved person only after identity resolution |
| `hasAuthorString` | Publication → source name literal | Preserves the unmerged source name |
| `affiliatedWith` | Person → Affiliation | Requires an organization and time scope |
| `hasMembership` | Person → Membership | Requires status and time scope |
| `cites` | Publication → Citation | Requires a citation source and snapshot |
| `hasTopicAssignment` | Publication or Project → TopicAssignment | Distinguishes source topics from calculated topics |
| `hasDerivedAnalytic` | corpus snapshot or query → DerivedAnalytic | Prevents a calculation from becoming a paper assertion |

## 6. Controlled classifications

### 6.1 Study-purpose family

One study can have more than one purpose assignment. Each assignment has a primary or secondary role.

1. `national valuation and value-set study`
2. `preference-method development or comparison`
3. `DCE or task-design experiment`
4. `measurement-property evaluation`
5. `instrument development or content-validity study`
6. `translation or cultural-adaptation study`
7. `implementation or routine-measurement feasibility study`
8. `population-health or routine-outcome study`
9. `systematic review or evidence synthesis`
10. `stakeholder or normative consultation`
11. `economic evaluation or utility-mapping impact study`
12. `methodological, conceptual, taxonomy, or policy paper`
13. `survey infrastructure or data-quality study`

`Valuation study` is assigned only when preferences for health states, dimensions, or levels are elicited or a value set is estimated. A paper that only applies a value set is not a valuation study.

### 6.2 Publication and evidence form

The publication-form family includes peer-reviewed research article, systematic review, methodological paper, qualitative study, observational study, experimental study, mixed-methods study, and policy or opinion paper. This classification describes the output. It does not replace the study-purpose classification.

### 6.3 Product and lifecycle status

Product status uses source-bound assertions:

- `experimental`;
- `in development`;
- `officially launched`, only when the summary explicitly says this;
- `validated for stated language and population`;
- `published product`;
- `planned`;
- `not produced by this study`;
- `status not reported`.

An isiXhosa validation result does not make every EQ-TIPS language form validated. A planned value set is not a published value set.

### 6.4 Geography roles

The controlled geography-role family includes:

- data-collection country;
- target population country;
- value-set jurisdiction;
- respondent residence country;
- institution country;
- author-affiliation country;
- fund-recipient country;
- language community.

These roles are necessary for country questions. They prevent a multi-country author list from becoming a study-country list.

### 6.5 Project and output link status

Project status, output status, and link status are different families.

- Project status: proposed, approved, ongoing, completed, paused, or unknown.
- Output status: planned, submitted, accepted, published, or unknown.
- Link status: candidate, accepted, rejected, overridden, or superseded.
- Link evidence: explicit project ID, explicit funding statement, project registry, author/date/topic heuristic, or manual review.

Only an accepted link contributes to project-output counts. The ontology keeps candidate and rejected links for audit.

### 6.6 Corpus and application status

A `CorpusMembership` classification contains:

- corpus name and snapshot date;
- inclusion status;
- inclusion or exclusion rule;
- reason;
- reviewer or process;
- evidence.

`Pure application` must have an explicit rule. For example, applying an EQ-5D instrument only as an outcome can differ from work on measurement, valuation, instrument development, implementation, or methods. The ontology does not infer this status from the presence of patient data.

## 7. Study-family views

These views help users. They are not mandatory templates.

### 7.1 Valuation-study view

Show the target instrument, jurisdiction, preference population, respondent perspective, elicitation method, protocol version, administration, task design, sample-size types, quality controls, model candidates, preferred model, anchoring, range, selected state values, and value-set product.

### 7.2 Measurement-property view

Show instrument versions, forms, language, target population, reporter, administration, comparator measures, property definitions, statistics, time points, subgroup results, and principal findings.

### 7.3 Instrument-development view

Show the instrument lifecycle stage, conceptual target, dimensions and levels, candidate wording, participant or expert groups, qualitative method, themes, requested changes, planned products, and unresolved issues.

### 7.4 Systematic-review view

Show the review question, search sources and dates, eligibility rules, included-study count, populations and countries, synthesis method, property or method classifications, pooled estimates, heterogeneity, and evidence gaps.

### 7.5 Implementation and routine-outcome view

Show service setting, workflow, administration, reporter, completion, support or action rules, repeated time points, scoring product, change classification, feasibility findings, and implementation barriers.

## 8. Derived analytics

A `DerivedAnalytic` is an immutable result for one declared input snapshot. It contains:

- analytic type;
- question or purpose;
- input universe and snapshot date;
- filters and controlled classifications;
- inclusion and missing-data rules;
- calculation definition;
- result and unit;
- ties and rounding rule;
- method or model version;
- creation time;
- links to every input record.

Supported analytic types include:

- count and sum;
- yearly count;
- median, range, and distribution;
- frequency and rank;
- timeline;
- top-decile share;
- fraction in a date window;
- time-to-first-output;
- growth trend;
- project-output-citation funnel;
- coauthor frequency;
- country participation count;
- topic or proposal similarity.

For a similarity result, the ontology must retain the proposal text supplied at query time, the compared project text, feature source, method version, score, rank, and threshold. Similarity is not a source classification.

For a timeline, the ontology must distinguish event types. A publication date, instrument launch, translation, first validation, and value-set publication are different milestones.

For any fraction, the numerator and denominator sets must be queryable. Missing dates or unresolved people cannot silently leave the denominator.

## 9. Complete example records

The following examples use only facts in the named supplied summaries. Each example marks absent facts instead of inferring them.

### 9.1 Example A: Danish EQ-5D-5L valuation and value set

Immediate evidence:

- Source summary: `S023`, `summaries/S023.md`.
- Verified summary SHA-256: `4008222b93f49f632e67a2c95a2c0588e8088b560ffbb577ba065dd4c13f7f6f`.

Publication:

- Title: “The Danish EQ-5D-5L Value Set: A Hybrid Model Using cTTO and DCE Data”.
- DOI: `10.1007/s40258-021-00639-3`.
- Publication date reported in the summary: 2021-02-02.
- Publication form: national value-set report.

Study:

- Primary purpose: national valuation and value-set study.
- Target product: the first Danish EQ-5D-5L value set.
- Target population: Danish adults.
- Data-collection period: October 2018 to November 2019.
- Completed interviews: 1,052.
- Analytic sample: 1,014.
- Sampling aim: national representation by age, gender, education, and region.
- Instrument version: EQ-5D-5L.
- Administration: computer-assisted personal interview.
- Protocol: EQ-VT version 2.1.
- Elicitation methods: ten cTTO tasks and seven duration-free DCE pairs per respondent.
- cTTO design: 86 states in total.
- DCE design: 196 pairs in 28 blocks of seven.
- Analysis candidates: cTTO-only, DCE-only, and combined hybrid models.
- Preferred model: heteroscedastic censored hybrid model.

Product and findings:

- Product basis: native direct valuation.
- Jurisdiction: Denmark.
- Target descriptive system: all 3,125 EQ-5D-5L states.
- Full health state 11111: 1.
- Worst state 55555: −0.757.
- States worse than dead: about 22%.
- Dimension ranking: anxiety/depression, pain/discomfort, mobility, self-care, usual activities.
- Intended use: Danish QALYs and health-care decision-making.
- Instrument interview language: not reported in the summary.

Project lineage:

- Source project ID: `20170401`.
- The summary reports that funding included EuroQol Research Foundation project `20170401`.
- The project-publication link is therefore an accepted link with `explicit project ID` and `explicit funding statement` evidence from `S023`.
- Award amount, project start date, project end date, and project status: not reported.

### 9.2 Example B: EQ-TIPS V2.0 expert consultation

Immediate evidence:

- Source summary: `S061`, `summaries/S061.md`.
- Verified summary SHA-256: `19e062b813b6014b8d70f92eda57e18e430a7bc53053b0faa94666bca8ff31f3`.

Publication:

- Title: “Developing the EuroQol toddler and infant populations (EQ-TIPS) instrument: qualitative analysis of expert views on content validity and conceptual challenges”.
- DOI: `10.1007/s11136-025-04150-3`.
- Publication form: qualitative peer-reviewed research article.

Study:

- Primary purpose: instrument development and content-validity study.
- Instrument: experimental EQ-TIPS V2.0, also described as EQ-TIPS-3L.
- Intended age range discussed: 0–3 years.
- Dimensions: Movement, Play, Social Interaction, Communication, Eating, and Pain.
- Response levels: no, some, and a lot of problems.
- Supplementary component: EQ VAS from 0 to 100.
- Participant role: invited experts.
- Invited: 44.
- Participated: 33.
- Countries represented: 15.
- Collection: three online semi-structured focus-group consultations on Zoom.
- Collection period: December 2022 to February 2023.
- Analysis: mainly deductive thematic analysis with inductive themes permitted; NVivo Version 14; Braun and Clarke six-phase approach.

Findings and product status:

- Most experts found the measure short and easy to complete.
- Experts asked for a clearer construct definition.
- Experts preferred observable examples to “age-appropriate behaviour”.
- Sleep was widely proposed as an additional dimension.
- The best proxy depends on study context, and proxy characteristics should be recorded.
- EQ-TIPS V5.0 was not tested.
- No psychometric evidence, preference evidence, or value set was produced.
- Preference-weighted scores and value sets were planned.

Project lineage:

- Source project ID: `365-RA`.
- Award amount and project dates: not reported.

### 9.3 Example C: measurement properties in late-onset Pompe disease

Immediate evidence:

- Source summary: `S090`, `summaries/S090.md`.
- Verified summary SHA-256: `fa3bb4f6d401e2bed4c6a5b4852699521c8a496380af32f1cfe813789cbe36a5`.

Publication and study:

- DOI: `10.1007/s10198-024-01682-2`.
- Publication date: 2024-03-12.
- Primary purpose: measurement-property evaluation.
- Country and sample: 117 Chinese patients with late-onset Pompe disease.
- Administration: web survey.
- Baseline collection period: January to April 2023.
- Retest: 110 patients after one week.
- Instrument versions: EQ-5D-3L, EQ-5D-5L, and SF-6Dv2.
- Comparator measure: WHODAS-12.
- Scoring products: Chinese value sets for the two EQ-5D versions and SF-6Dv2.

Analyses and findings:

- Properties: ceiling and floor effects, convergent validity, known-group validity, and test-retest reliability.
- Dimension reliability statistic: Gwet’s agreement coefficient.
- Utility reliability statistic: two-way mixed-effects, single-measure, absolute-agreement ICC.
- Utility ICC: 0.87 for EQ-5D-3L, 0.85 for EQ-5D-5L, and 0.85 for SF-6Dv2.
- EQ VAS ICC: 0.71.
- Full-health profile: 6.8% for EQ-5D-3L, 0.9% for EQ-5D-5L, and 0% for SF-6Dv2.
- Principal finding: EQ-5D-5L had lower ceiling and floor effects, stronger convergent validity, and greater discriminant ability; EQ-5D-3L had better test-retest agreement.
- Limitation: WHODAS-12 lacks pain, so pain/discomfort validity was not sufficiently assessed.

Project lineage:

- Source project ID: `444-RA`.
- The summary reports EuroQol Research Foundation support under `444-RA`.

### 9.4 Conflict-preservation examples

The ontology must not choose one value without evidence when the summary reports a conflict.

- `S004` reports two different mean ages for the UAE sample. Store both source assertions and mark the publication-level age summary as conflicting.
- `S041` reports different denominators for future-completion willingness. Store each numerator, denominator context, and source section.
- `S047` reports a physiotherapy EQ VAS change of 1.2 in one location and 12.2 in another. Store both and mark the comparison as unresolved.

## 10. Competency-question support

The answerability classes are:

- `A — answerable from supplied summaries`: the 50 summaries contain the necessary facts for a packet-scoped answer or calculation.
- `E — external linked data required`: the ontology can answer only after the named external records are linked. The packet alone must return `not answerable from supplied summaries`.
- `U — unsupported as worded`: a decision rule or evidence concept is missing. The ontology must not invent it.

An `A` result is complete only for the supplied 50-summary universe. It must not be presented as a complete result for all EuroQol research.

| Question | Required concepts and relations | Class and evidence decision |
|---|---|---|
| Q63 — countries without a native EQ-5D-5L value set | Country universe; `ValueSet`; `ValueSetBasis=native direct valuation`; `targetsInstrument`; jurisdiction; publication status; current snapshot; set difference | **E.** The summaries give some national sets, but not a complete current country or value-set registry |
| Q1 — total funded projects and approved budget | `FundedProject`; `FundingAward`; approved amount; currency; exchange rule; project deduplication; sum analytic | **E.** Project award and budget records are not in the summaries |
| Q57 — frequent methods in funded valuation projects | Project-purpose classification; accepted project-study links; `MethodImplementation`; project-level deduplication; frequency analytic | **E.** Summary methods can describe publications, but a complete funded-project universe and project aims are absent; “what should I learn” also needs a separate recommendation rule |
| Q37 — papers that used DCE for valuation and countries | `Publication`; `Study`; valuation-purpose assignment; DCE method subtype; geography role; `reportedBy` | **A.** The summaries identify DCE use and country for supplied studies, including national and youth valuation work |
| Q61 — instrument-development timeline in the corpus | Instrument version; product status; development, translation, validation, launch, and value-set events; event date; timeline analytic | **A.** A packet-scoped timeline can use facts such as EQ-HWB development, EQ-TIPS V2.0 work, and the stated EQ-5D-Y-5L launch |
| Q78 — non-members who co-author most with members | Resolved `Person`; dated `Membership`; authorship; coauthor pair; frequency analytic | **E.** Complete authorship, member history, and identity resolution are absent |
| Q85 — OpenAlex topics or fields that cite funded work most | Accepted funded-output links; citation records; citing-work topic assignments; source snapshot; rank analytic | **E.** Citation and OpenAlex topic records are not in the summaries |
| Q96 — all corpus bolt-on papers with one-line summaries | Full `CorpusMembership`; `SupplementaryDimension`; `addsDimensionTo`; bolt-on study role; source-grounded synopsis | **E.** The packet has bolt-on examples, but it is not the full corpus inventory |
| Q91 — five recent success stories | Project completion date; output links; publication date; citation snapshot; rank; explicit definitions of “success story” and “highly cited” | **U.** “Success story” and “highly cited” have no supplied decision rule. After rules are approved, project and citation data will also be required |
| Q80 — inter-project output citation flow | Projects; accepted output links; publication citations; source and target project; directed network analytic | **E.** Project-output and citation graphs are not supplied |
| Q87 — identity merges, overrides, and skips | `IdentityResolutionEvent`; action; before and after profiles; reason; evidence; actor; date | **E.** Resolution audit logs are not in the summaries |
| Q29 — countries with a published native EQ-5D-5L value set | Published `ValueSet`; native basis; target version; jurisdiction; publication date; current registry snapshot | **E.** Supplied national examples are not an exhaustive global list |
| Q2 — funded projects by year since 2012 | Project identity; funding decision date; year; status; yearly count analytic | **E.** The project registry is absent |
| Q48 — instruments targeted by each ongoing project | Project status and period; project aim; `targetsInstrument`; instrument version | **E.** Ongoing status and complete project aims are absent |
| Q18 — past projects most similar to a proposal abstract | Query-time `Proposal`; project abstracts; project status; topic or text features; versioned similarity analytic | **E.** The proposal text and full past-project abstracts must be linked at query time |
| Q44 — working groups spanned by researcher X | Resolved person; dated working-group membership; publications or projects; topic assignments; span analytic | **E.** Working-group and person records are absent |
| Q19 — cognition bolt-on coverage in projects | Cognition `SupplementaryDimension`; base instrument; project aims and status; accepted outputs; overlap rule | **E.** `S084` supplies one paper-level cognition example, but past and ongoing project coverage is not complete |
| Q33 — studies comparing 5L and 3L value sets in the same population | Study; paired instrument versions; value sets; shared sample assertion; comparison | **A.** `S073` and the parallel-study analysis in `S024` supply packet evidence; the shared-population relation must be explicit |
| Q42 — work on DCE-with-duration hybrids | DCEd, DCE-duration, DCE-death, split-triplet, duration and nonlinear-time specifications; publication and study links | **A.** `S011`, `S019`, `S020`, and `S039` provide method and stakeholder evidence in the packet |
| Q11 — institution countries receiving most funding | Award recipient; organization; institution-country relation; approved amount; currency conversion; rank analytic | **E.** Award, recipient, and complete institution data are absent |
| Q8 — five projects with most publications | Complete project universe; accepted output links; publication deduplication; count and rank | **E.** The summaries are a selected publication sample, not a complete output register |
| Q31 — people currently working on EQ-HWB valuation | Person; current project role; current project status; EQ-HWB target; valuation-purpose assignment; as-of date | **E.** Current role and ongoing-project data are absent |
| Q45 — typical sample sizes for 5L valuation studies | National valuation classification; exact target version; analytic participant count; summary statistics with inclusion rule | **A.** The packet has analytic samples of 1,014, 1,079, 500, and 1,005 for four national EQ-5D-5L value-set studies; “typical” must name this filter |
| Q98 — project for DOI X and link evidence | DOI identity; publication; `ProjectOutputLink`; project ID; link status; evidence type and source | **A.** For a DOI among the supplied 50, the summary and its project or funding assertion support the answer; another DOI requires external data |
| Q49 — EQ-5D-Y test-retest studies | Instrument family and version; measurement-property classification; retest interval; stable subset; reliability statistic; publication | **A.** `S059` and `S096` contain packet evidence for EQ-5D-Y versions |
| Q59 — open-access papers that introduce EQ-HWB | Publication access status; introduction-role classification; instrument-development lineage; publication date | **E.** Open-access status and an exhaustive, evidence-based “introduces” role are not in the summaries |
| Q23 — completed projects that promised a value set but have no linked publication | Project completion; abstract promise; planned product; accepted outputs; value-set publication classification; anti-join | **E.** Project abstracts, completion status, and complete output links are absent |
| Q75 — fraction of accepted links in the −1 to +8 year window | Accepted output links; project start/end rule; publication date; date offset; numerator and denominator; missing-date rule | **E.** Link decisions and project periods are absent |
| Q7 — median project start to first publication | Project start; accepted outputs; first publication date; censoring and missing rules; median analytic | **E.** Project dates and complete outputs are absent |
| Q74 — researchers newly entering the corpus in three years | Resolved person; authorship; corpus snapshot; first observed publication date; three-year cut-off | **E.** Complete authorship history and identity records are absent |
| Q60 — topics with growing activity in three years | Full corpus snapshot; dated publications; versioned topic assignments; time buckets; growth rule | **E.** The selected summaries do not give a complete publication time series or topic scheme |
| Q26 — past projects sharing proposal condition and instrument | Query-time proposal targets; project abstracts; controlled condition; instrument version; project status; conjunctive match | **E.** Proposal and project records are absent |
| Q17 — applicant X outputs from previous grants | Resolved applicant; PI or applicant role; prior awards; accepted output links; publications | **E.** Applicant, award, and output-link data are absent |
| Q46 — corpus papers citing the 1997 UK MVH paper | Canonical target publication; complete corpus publications; reference-level citations; citation source | **E.** Reference lists and citation data are absent |
| Q22 — lag from previous grant to applicant X's first output | Resolved applicant; prior grant; grant end or award reference date; accepted outputs; first publication; interval | **E.** Person, grant-period, and output data are absent |
| Q38 — researcher X's frequent corpus coauthors | Resolved people; complete corpus authorship; coauthor counts; tie rule | **E.** Full author lists and identity resolution are absent |
| Q77 — output concentration among PIs | PI role; project universe; accepted outputs; person deduplication; top-decile and rounding rule; share analytic | **E.** PI assignments and complete output links are absent |
| Q47 — members who coauthored with researcher X on funded outputs | Resolved people; dated member status; authorship; accepted funded-output link; coauthor relation | **E.** Membership, authorship, and full funded-output links are absent |
| Q97 — countries represented by researchers on funded publications | Accepted funded outputs; resolved authors; publication-time affiliation; institution country; distinct-country analytic | **E.** Complete authorship and affiliation data are absent |
| Q51 — EQ-TIPS work so far | EQ-TIPS family and versions; publication; study purpose; translation; validation; development events; current corpus snapshot | **E.** `S061` and `S063` give packet examples, but “so far” needs a complete current publication and project inventory |
| Q54 — crosswalk versus native 5L value set | Value-set basis; `mapsFrom`; `targetsInstrument`; direct elicitation; preference population; protocol; comparison; key publications | **A.** `S018`, `S024`, `S036`, and `S073` directly support the distinction and its consequences |
| Q12 — most cited funded publication and project | Accepted funded-output links; citation count source and snapshot; rank; project link evidence | **E.** Citation counts and complete links are absent |
| Q92 — projects-to-citations funnel | Projects; projects with accepted outputs; distinct outputs; citations; deduplication; four-stage count analytic | **E.** The project registry, output graph, and citation data are absent |
| Q99 — share of member-authored papers excluded as pure applications | Dated membership; resolved authorship; corpus inclusion decisions; pure-application rule; numerator and denominator | **E.** Membership and exclusion-decision data are absent, and the classification rule must be recorded |
| Q62 — researchers at institution X on EQ topics | Query-time organization; publication-time or current affiliation; resolved people; EQ topic assignment; as-of rule | **E.** Person and affiliation records are absent |
| Q52 — published EQ-HWB translations or language adaptations | EQ-HWB version; translation/adaptation product; language; publication; validation status; complete corpus snapshot | **E.** `S078` gives a Simplified Chinese use case, but the summaries do not provide a complete published-adaptation register |
| Q20 — ongoing projects that overlap proposal aims | Proposal aims; ongoing projects; project aims; condition, instrument, method, and population facets; overlap score and rule | **E.** Query-time proposal and current project data are absent |
| Q81 — share of resolved researchers with ORCID | Resolved person universe; ORCID assertion and verification status; numerator and denominator; snapshot | **E.** ORCID and resolved-person records are absent |
| Q58 — EQ-5D-Y-5L work published so far | Exact instrument version; publication; study purpose; launch and development events; current corpus snapshot | **E.** `S057`, `S059`, and `S096` give packet evidence, but “so far” requires a complete current inventory |
| Q30 — value sets that used EQ-VT and its version | `ValueSet`; `followsProtocol`; protocol version; target instrument; jurisdiction; source assertion | **A.** `S023`, `S018`, and `S028` report version 2.1; `S004` reports EQ-VT without a version; `S009` reports version 1.1 but explicitly did not produce a national value set |

## 11. Facts that remain text, optional, derived, or outside scope

### 11.1 Source text

Keep these facts as source-faithful text with controlled tags where useful:

- nuanced qualitative themes and participant concerns;
- authors' explanations of cultural, ethical, or behavioral mechanisms;
- limitations and cautions;
- implementation recommendations;
- exact wording-change proposals;
- model-selection rationale that cannot be reduced to one metric.

### 11.2 Optional structured detail

These details are useful when a question needs them, but they are not mandatory for every study:

- every task block and health-state pair;
- every model coefficient;
- every quality-control flag count;
- software and software version;
- ethics identifiers;
- conflict-of-interest statements;
- recruitment incentive;
- interviewer training detail.

The ontology should store an exact formula as a source expression when it is available. It should also store its target product and model. It must not parse or recalculate the formula unless a separate verified analytic process does this.

### 11.3 Derived facts

Counts, medians, ranks, “most frequent,” growth, similarity, success rankings, citation funnels, top-decile shares, and date-window fractions remain analytic records. They are never copied into the source layer.

### 11.4 Outside scope without linked data

The supplied summaries do not establish:

- complete project budgets, dates, statuses, applicants, PIs, or recipient organizations;
- complete author identities, ORCID values, memberships, working groups, or affiliations;
- complete citation, open-access, reference, or OpenAlex data;
- a complete current value-set registry;
- identity-resolution audit history;
- the complete corpus inclusion and exclusion history;
- current proposal text or current ongoing-project data.

The ontology can link these records later. It must label their source and snapshot.

## 12. Unresolved design choices and risks

1. **Publication-to-study boundaries.** Some papers report one study with several samples. Others synthesize several datasets or prior studies. Curators need a rule for when to create more than one `Study` record.
2. **Project identity.** Project IDs have different formats. A shared project ID across publications is strong evidence of a shared project, but it does not prove that all reported studies have the same award or period.
3. **Native value-set coverage.** “Native” needs an approved rule for multinational populations, expatriate populations, and language versions. Jurisdiction, respondent residence, nationality, and interview language must stay separate.
4. **Instrument status.** `Experimental`, `validated`, and `officially launched` are time- and form-specific. Status must have a date and source.
5. **Study-purpose overlap.** A methods paper can also contain a valuation experiment. Multiple classifications are safer than one forced class, but queries need a stated primary-purpose rule.
6. **Exact model identity.** Short model labels can hide censoring, heteroskedasticity, data source, and time-preference assumptions. A composite model specification is necessary.
7. **Value-set version identity.** A country can have more than one value set or a later reanalysis. Product version and publication identity must not be collapsed.
8. **Sample-size comparisons.** “Typical sample size” changes when pilot, national, youth, DCE-only, cTTO-only, and task-observation counts are mixed. Every analytic must state its filter.
9. **Reporter and perspective.** Self-report, proxy form, proxy-person perspective, and child framing are often confused. Separate axes reduce this risk.
10. **Country analytics.** Study location, value-set jurisdiction, institution country, and author country answer different questions. Queries must select one role.
11. **Output-link inflation.** Topic and author heuristics can create false project-output links. Only accepted, evidence-bearing links can enter counts.
12. **Person identity drift.** Membership, ORCID, affiliation, and working-group status can change. Each assertion needs a time scope and resolution history.
13. **Corpus drift.** “So far,” “recent,” and “all corpus papers” require a named snapshot and cut-off date.
14. **Citation drift.** Citation ranks change. Each citation metric needs a provider, access date, and counting rule.
15. **Undefined evaluative labels.** “Success story,” “highly cited,” “overlap,” and “pure application” need approved rules before calculation.
16. **Source conflict.** The summaries contain explicit internal discrepancies. The ontology must preserve them and must not choose a value without review evidence.
17. **Negative or null evidence.** “No linked publication” is valid only after the project-output search universe and matching process are complete.
18. **Granularity cost.** Full task designs and coefficients can be large. Store them when they answer a question, and keep a source locator otherwise.

## 13. Minimum quality rules

A record is fit for research use only if it meets these rules:

- Every factual assertion has a source.
- Every source term remains available after normalization.
- Every study use of an instrument names the exact version when reported.
- Every value set names its target version, jurisdiction, basis, and evidence.
- Every method names the exact implementation when the summary supplies it.
- Every numerical result has its population, measure, statistic, and time context.
- Every project-output link has a status and evidence type.
- Every derived answer names its universe, snapshot, filters, and rule.
- Conflicts remain visible.
- Missing facts stay missing.

These rules make the ontology useful for the supplied studies and safe for later links to projects, people, institutions, publications, citations, and current registries.
