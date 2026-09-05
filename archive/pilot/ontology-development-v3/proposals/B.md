# Proposal B: evidence-centered ontology for EuroQol research

## 1. Purpose and scope

This ontology supports precise search, comparison, and synthesis of EuroQol research. It represents what a publication reports, what a study did, which population it studied, which instrument version it used, how it administered and scored the instrument, which methods and models it applied, which product it produced, and which findings it reported.

The ontology has two equal requirements:

- It must preserve exact source facts.
- It must make comparable facts available through controlled concepts and value families.

The ontology does not treat a publication, a study, a funded project, or a computed corpus statistic as the same object. It also does not treat all uses of a short name as the same concept. For example, `EQ-5D-5L`, `EQ-5D-Y-5L`, and `EQ-TIPS-5L V3.0` are different instrument versions. A native EQ-5D-5L value set and a 5L-to-3L crosswalk are different products. A level sum score and a preference-weighted utility are different outcomes.

The proposal covers the supplied 50 summaries and the supplied 50 competency questions. An answer from these summaries is packet-bounded. It does not claim that the packet is a complete bibliography. Facts about grant administration, current project status, citations, open-access status, researcher identity, membership, and ingestion history need linked data when the summaries do not supply them.

This proposal does not import an external ontology or standard. The supplied evidence does not give a sufficient basis to select one. A later implementation can map the local concepts to an external vocabulary without changing the evidence model.

## 2. Design rules

1. **Keep the evidence unit small.** Store each exact assertion with its own provenance and context.
2. **Keep source wording.** Preserve a source label even when it maps to a canonical term.
3. **Use controlled values for search.** Classify study types, instruments, methods, models, populations, products, outcomes, and findings with explicit value families.
4. **Keep versions explicit.** Do not infer an instrument version, protocol version, language version, proxy version, value set, or model specification.
5. **Keep applications separate from definitions.** An instrument has a definition. A study has an instrument application with a language, mode, respondent role, perspective, recall period, time point, and scoring context.
6. **Keep estimates contextual.** A number must identify its statistic, unit, population or subgroup, time point, instrument application, and analysis context.
7. **Keep absence explicit.** Distinguish `not reported`, `not applicable`, `planned but not produced`, `not available`, `conflicting source statements`, and `not extracted`.
8. **Keep time explicit.** Current status, membership, affiliation, and instrument status need an evidence date or an interval.
9. **Do not force one study template.** A protocol, a systematic review, a qualitative study, a value-set study, and a population-norms study can use different sets of concepts.
10. **Do not convert interpretation into observation.** Store an author interpretation, recommendation, limitation, and future-work statement as distinct finding types.

## 3. Four information layers

The ontology separates four layers. This separation prevents a source phrase or a computed result from becoming an unqualified research fact.

| Layer | Meaning | Example from the supplied summaries |
|---|---|---|
| Source record and source term | The supplied summary, its section locator, and the wording that it uses. | S019 uses `DCEd`, `discrete choice with duration`, and `split-triplet` in specific contexts. |
| Evidence assertion | One claim extracted from one source, with a subject, relation, object or literal, and qualifiers. | S019 reports that the final DCEd analytic sample had 970 respondents. |
| Canonical concept and classification | A stable concept used to find equivalent or related evidence. | The source terms `DCEd`, `DCE-duration`, and `DCE with Duration` can map to the canonical method `discrete choice experiment with duration`. Their original forms remain available. |
| Derived analytic | A result computed from selected assertions under a declared rule and snapshot. | The share of funded valuation projects that use cTTO, or the top decile of PIs by output count. |

A canonical mapping does not change a source assertion. It adds a search path. A classification also does not state identity. For example, `hybrid heteroskedastic Tobit model censored at −1` can be classified under `hybrid valuation model`, `Tobit model`, and `heteroskedastic model`. The exact model name remains the value used for a precise query.

## 4. Main concepts

### 4.1 Evidence and terminology concepts

| Concept | Meaning for EuroQol research |
|---|---|
| **Summary source** | One supplied fixed summary. It has a summary ID, file path, verified hash, and optional section locator. |
| **Evidence assertion** | One source-supported statement. It records the subject, relation, value, source summary, locator, source wording, and evidence status. |
| **Source term occurrence** | An exact word or phrase as used in a source. It has language, capitalization, abbreviation form, and local context. |
| **Canonical term** | The preferred search label for one concept. It has a definition and a controlled concept type. |
| **Term mapping** | A qualified link from a source term to a canonical term. Mapping values are exact synonym, abbreviation, spelling variant, narrower term, broader term, related term, and unresolved. |
| **Classification assignment** | A link from an entity to a controlled category. It records who or what supplied the classification and whether it is direct or curated. |
| **Evidence conflict** | A set of assertions that cannot all be used as one value. The source values remain intact. |
| **Missingness statement** | An explicit reason that a field has no value. It prevents `not reported` from becoming `no`. |

### 4.2 Research administration concepts

| Concept | Meaning for EuroQol research |
|---|---|
| **Publication** | A document or registered report. It can have a title, DOI, publication date, publication form, authorship, access status, and citations. |
| **Study** | The research activity reported by a publication. It has an aim, design, status, dates, setting, populations, samples, methods, analyses, products, and findings. |
| **Study part** | A named wave, phase, arm, cohort, survey, task block, review stage, or analysis within a study. It lets one study contain different samples and methods. |
| **Funded project** | An administrative award or project. It has a project identifier, title, dates, status, approved budget, working group, and project roles when linked data supply them. |
| **Output-project link** | An evidence-qualified link between a publication or study and a project. Its basis can be a supplied project ID, an explicit funding statement, a grant acknowledgement, or a curated external match. |
| **Funding statement** | The exact funding or support statement reported for a publication or study. It can name a funder and grant identifier without proving a complete project match. |
| **Person** | A resolved researcher, author, applicant, PI, supervisor, or other contributor. Person identity is separate from each printed author name. |
| **Organization** | A university, hospital, funder, research group, care provider, panel vendor, or other organization. |
| **Researcher role** | A time-qualified role such as author, applicant, PI, supervisor, interviewer, or project member. |
| **Membership** | A time-qualified relation between a person and the EuroQol Group or another body. |
| **Affiliation** | A time-qualified relation between a person and an organization, usually linked to a publication or project. |
| **Working group** | A controlled organizational topic or governance group. It is not inferred only from a paper topic. |
| **Citation** | A directed relation from one publication to another. It has a source, date or snapshot, and match quality. |
| **Open-access status** | A time-qualified access and licence fact for a publication. A funding statement about open-access costs is not sufficient by itself. |
| **Ingestion event** | A record of how a publication entered a corpus, such as structured funder metadata or full-text grant mining. |
| **Identity-resolution decision** | A merge, override, split, or skip action for person records, with reason, evidence, actor, and time. |

### 4.3 Research-content concepts

| Concept | Meaning for EuroQol research |
|---|---|
| **Research aim** | The question or purpose of a study, in source text and optional controlled topic form. |
| **Study family** | A broad research purpose, such as valuation, instrument development, psychometric evaluation, population norms, health inequality, routine outcome use, or methods research. |
| **Study design** | The design that produced evidence, such as qualitative interviews, a cross-sectional survey, a longitudinal cohort, a comparative experiment, or a systematic review. |
| **Population definition** | The intended group, with age, geography, condition, care setting, residence, language, respondent role, and inclusion or exclusion criteria. |
| **Sample** | A realized set of units in a study or study part. The unit can be a person, dyad, interview, publication, trial, or health-state response. |
| **Sample count** | A count tied to a stage and unit, such as invited, screened, recruited, completed, excluded, included, paired, or analysed. |
| **Subgroup** | A defined part of a sample, such as an age band, country, condition, report perspective, or change group. |
| **Setting** | A hospital, community, home, online panel, care facility, registry, or other research environment. |
| **Time point or period** | A collection wave, baseline, follow-up, admission, discharge, survey period, recall period, or hypothetical duration. |
| **Instrument family** | A related group of measures, such as EQ-5D, EQ-5D-Y, EQ-TIPS, or EQ-HWB. |
| **Instrument version** | A specific descriptive system or form, such as EQ-5D-5L, EQ-5D-Y-3L, experimental EQ-TIPS-5L V3.0, or experimental EQ-HWB v1.1. |
| **Language version** | A named language and localization of one instrument version. It can have official, translated, adapted, or experimental status as reported. |
| **Dimension or item** | A component of one instrument version. It retains its exact label and order for that version and language. |
| **Response level** | A response category tied to a dimension, instrument version, and language. Do not store one global meaning for level 5. |
| **Health state** | An ordered profile under one descriptive system, such as EQ-5D-5L state 55555. The profile is invalid without its instrument version. |
| **Instrument application** | One use of an instrument version in a study part. It records language, administration mode, respondent role, perspective, recall period, time point, and scoring method. |
| **Administration event** | The collection procedure for an instrument application, including self-complete, interviewer-administered, proxy, paper, computer-assisted, web, face-to-face, or mixed mode. |
| **Method** | A reusable research procedure, such as cTTO, DCE with duration, framework analysis, Mokken scaling, or Paretian Classification of Health Change. |
| **Protocol** | A named and versioned set of procedures, such as EQ-VT 2.1. A protocol is not the same as cTTO, one component of the protocol. |
| **Method application** | A study-specific use of a method or protocol, with task design, comparator, duration, perspective, software, and quality-control details. |
| **Statistical model** | An exact model specification, such as `hybrid heteroskedastic Tobit model censored at −1` or `main-effects conditional logit model estimated by maximum likelihood`. |
| **Analysis application** | A model or analytic procedure applied to a data set, outcome, study part, and sensitivity set. |
| **Research product** | A reusable output, such as a value set, crosswalk, scoring rule, instrument version, protocol, population-norm set, reference-value set, experimental design, or evidence synthesis. |
| **Outcome measure** | What is measured, such as EQ VAS, index utility, level sum score, ceiling, agreement, responsiveness, or a dimension problem rate. |
| **Estimate** | A result with a statistic, value, unit, denominator, sample or subgroup, time point, and analysis context. |
| **Comparison** | A structured contrast between two or more estimates, methods, instruments, versions, modes, time points, or groups. |
| **Finding** | A source-reported conclusion or interpretation, linked to its supporting estimates and scope. |
| **Limitation or evidence gap** | A stated restriction, source uncertainty, absent test, or future research need. |
| **Derived analytic** | A computed corpus result with a definition, input set, filters, formula description, time snapshot, and provenance. |

## 5. Important relations

The relation labels below state semantics. They do not set universal cardinalities.

| Relation | From → to | Meaning and required qualification |
|---|---|---|
| `reports` | Publication → Study | The document reports the study. A publication can report more than one study, and a study can have more than one publication. |
| `has study part` | Study → Study part | The part is a wave, arm, phase, cohort, or distinct analysis in that study. |
| `has project link` | Publication or Study → Output-project link | Connects research evidence to a project without hiding the match basis. |
| `links to project` | Output-project link → Funded project | Identifies the administrative project. |
| `has link basis` | Output-project link → Link-basis value | Records whether the source is a project ID, explicit funding text, acknowledgement, or curated match. |
| `contains funding statement` | Publication → Funding statement | Preserves the funding statement as evidence. |
| `names funder` | Funding statement → Organization | Names a funder without automatically asserting a project match. |
| `has author occurrence` | Publication → printed author name | Preserves the name as printed or summarized. |
| `resolves to person` | printed author name → Person | Adds a qualified identity match. |
| `has role` | Person → Researcher role | Records applicant, PI, supervisor, author, or other role with a project or publication and time. |
| `affiliated with` | Person → Organization | Requires a time or publication context when available. |
| `member of` | Person → organization or group | Requires evidence date or interval. |
| `assigned to working group` | Project → Working group | Uses administrative evidence. A topic match alone does not prove assignment. |
| `cites` | Publication → Publication | Records a directed citation and bibliometric snapshot. |
| `entered corpus through` | Publication → Ingestion event | Supports provenance audits for corpus entry. |
| `has aim` | Study → Research aim | Preserves the source aim and optional controlled topics. |
| `classified as` | entity → controlled category | Applies one or more categories without replacing exact labels. |
| `targets population` | Study → Population definition | States the intended group. |
| `has sample` | Study or Study part → Sample | States a realized group or unit set. |
| `has sample count` | Sample → Sample count | Keeps counts for different stages and units separate. |
| `has subgroup` | Sample → Subgroup | Identifies a defined analytic or descriptive group. |
| `conducted in setting` | Study or Study part → Setting | Records the care, community, online, registry, or other environment. |
| `conducted at place` | Study or Study part → Place | Records a study location. This is not the same as preference jurisdiction or recipient country. |
| `uses instrument` | Instrument application → Instrument version | Identifies the exact form used. |
| `version of` | Instrument version → Instrument family | Places a version in its family. |
| `has language version` | Instrument application → Language version | Identifies the exact language or localization. |
| `has dimension` | Instrument version → Dimension or item | Records version-specific content and order. |
| `has response level` | Dimension or item → Response level | Records exact response wording and ordinal position. |
| `administered to` | Instrument application → Sample or Subgroup | Identifies who supplied or received the measure. |
| `has respondent role` | Instrument application → respondent-role value | Distinguishes adult, child, caregiver, clinician, expert, or other respondent. |
| `uses perspective` | Instrument application or Method application → perspective value | Distinguishes self, proxy version 1, proxy-person version 2, own-child, hypothetical child, and other perspectives. |
| `uses administration mode` | Administration event → mode value | Keeps web, paper, face-to-face, telephone, CAPI, and mixed mode explicit. |
| `uses recall period` | Instrument application → Time period | Stores `today`, seven days, one month, or another exact period. |
| `applies method` | Study part → Method application | Connects a study part to a concrete method use. |
| `implements protocol` | Method application → Protocol | Records the exact protocol version or `version not reported`. |
| `uses method` | Method application → Method | Records cTTO, DCE, thematic analysis, or another exact method. |
| `uses task frame` | Method application → task-frame description | Records the compared alternatives, duration, subject, and decision perspective. |
| `analysed by` | Study part or Method application → Analysis application | Connects evidence generation to its analysis. |
| `uses model` | Analysis application → Statistical model | Identifies the exact model specification. |
| `produces` | Study → Research product | States a reported product. A plan for a future product uses `plans to produce`. |
| `applies value set` | Instrument application → Value set | Identifies the scoring product used for a specific application. |
| `value set for` | Value set → Instrument version | Identifies the descriptive system that the value set scores. |
| `has preference jurisdiction` | Value set → Place | Identifies the country or population whose preferences the value set represents. |
| `derived by mapping from` | Crosswalk → Value set or descriptive system | Separates a crosswalk from a native value set. |
| `has outcome` | Study or Study part → Outcome measure | Identifies the measured construct. |
| `has estimate` | Study or Analysis application → Estimate | Stores one contextual result. |
| `estimates` | Estimate → Outcome measure | Identifies what the number represents. |
| `for population or subgroup` | Estimate → Sample, Population, or Subgroup | Identifies the denominator and scope. |
| `at time point` | Estimate → Time point | Prevents baseline and follow-up values from merging. |
| `uses scoring context` | Estimate → Value set or Scoring rule | Prevents values from different tariffs or LSS rules from merging. |
| `compares` | Comparison → two or more comparison members | Records the exact items in a contrast. |
| `reports comparison result` | Comparison → Estimate or Finding | Stores direction, magnitude, uncertainty, and test result when supplied. |
| `supports finding` | Estimate or Comparison → Finding | Links a conclusion to its evidence. |
| `qualified by` | Finding or Estimate → Limitation or evidence gap | Keeps scope and uncertainty next to the result. |
| `computed from` | Derived analytic → Evidence assertions or linked data snapshot | Makes a corpus statistic reproducible. |

## 6. Controlled classifications and exact value families

### 6.1 Publication, study, and status values

Publication form and study design are separate value families. A `systematic review` is both a publication form and an evidence-synthesis design. A `study protocol` reports planned work and does not supply completed results.

| Value family | Controlled values supported by the packet | Notes |
|---|---|---|
| Publication form | peer-reviewed research article; study protocol; systematic review; methodological or conceptual paper; methods report | Keep the exact source publication type as a source term. |
| Study family | health-state valuation; value-set development; valuation-method development; valuation-method comparison; instrument development; content-validity research; psychometric evaluation; instrument comparison; population norms or reference values; population health; health inequality; routine PROM implementation; data-quality research; statistical-methods review; item-selection methods; evidence synthesis | A study can have more than one family. |
| Design | qualitative interview or focus group; cross-sectional survey; longitudinal or repeated-measures study; observational cohort; comparative experiment; mixed-methods study; secondary analysis; systematic review; protocol; theoretical-state analysis | Do not infer randomization when the summary does not report it. |
| Evidence status | observed; planned; source-reported interpretation; recommendation; limitation; future work; no result produced | This family applies to assertions and findings. |
| Study status | planned in protocol; data collection completed; analysis completed; publication reported; current status unknown | `Planned in protocol` does not mean `ongoing now`. |

### 6.2 Instrument and descriptive-system values

The instrument registry must use full version identities. It must not search only on the token `5L`.

| Instrument family | Versions or forms in the packet | Important distinction |
|---|---|---|
| EQ-5D | EQ-5D-3L; EQ-5D-5L; EQ VAS | EQ VAS is an associated measure, not one of the five descriptive-system dimensions. |
| EQ-5D-Y | EQ-5D-Y-3L self-report; EQ-5D-Y-5L self-report; EQ-5D-Y-3L proxy; experimental EQ-5D-Y-5L proxy version 1; proxy version 2 where reported | Youth and adult forms are not interchangeable. Proxy version 1 and proxy-person version 2 have different perspectives. |
| EQ-TIPS | experimental EQ-TIPS V2.0 or EQ-TIPS-3L; experimental EQ-TIPS-5L V3.0; EQ-TIPS EQ VAS | V2.0 and V3.0 have different dimension sets. The five-level version was not available for the S061 test. |
| EQ-HWB | experimental 25-item EQ-HWB; experimental EQ-HWB v1.1; EQ-HWB-S; EQ-HWB-9 | Do not equate EQ-HWB-S and EQ-HWB-9 only because each has nine items. The packet does not state full identity across all studies. |
| Comparator measures | PedsQL; PROMIS-16; PROMIS-29 + 2 and PROPr; WHOQOL-OLD; SF-6Dv2; ASCOT; CarerQol; QOL-ACC; EORTC QLQ-C30; WHODAS-12; WHO-5; PHQ-9; GAD-7; Brief Inventory of Thriving | These concepts support comparison but remain outside the EuroQol instrument families. |

Dimensions belong to an instrument version. The adult EQ-5D versions use Mobility, Self-Care, Usual Activities, Pain/Discomfort, and Anxiety/Depression. EQ-5D-Y uses child wording such as Looking After Myself and Feeling Worried, Sad, or Unhappy. EQ-TIPS V2.0 uses Movement, Play, Social Interaction, Communication, Eating, and Pain. EQ-TIPS-5L V3.0 uses Movement, Eating or Drinking, Sleep, Pain, Managing Emotions, Interacting with Others, and Play. These labels must remain version-specific.

Response levels also belong to a version, dimension, and language. For example, adult EQ-5D-5L can use `extreme problems` for one dimension and `unable to` for another. EQ-5D-Y-3L uses `no problems`, `some problems`, and `a lot of problems`. A numeric level is not sufficient without its response wording.

Instrument-status values are time-qualified. Supported source states include `experimental`, `in-progress source version`, `final product of the reported development study`, `official translation`, `not available for this study`, and `status not reported`. The ontology must not convert these values into a single permanent status.

### 6.3 Population and administration values

| Value family | Controlled values and fields |
|---|---|
| Unit of observation | person; child-caregiver dyad; expert; interview; publication; trial; health-state valuation; choice task; registry record |
| Respondent role | adult general-population respondent; patient; child or adolescent; parent or caregiver; staff proxy; family proxy; expert; stakeholder; publication reviewer |
| Report perspective | self-report; assisted self-report; proxy version 1; proxy-person version 2; adult own health; adult imagining a child; adult valuing for a child; child own perspective; other-adult perspective; unspecified proxy |
| Age representation | exact age; lower and upper age bound; age band; mean or median age; hypothetical age; age unit |
| Condition role | inclusion condition; comparator condition; self-reported chronic condition; clinical diagnosis; excluded condition; hypothetical condition |
| Geography role | study site; recruitment place; residence criterion; target population; preference jurisdiction; norm jurisdiction; institution location; fund recipient country |
| Setting | general population; hospital inpatient; outpatient; primary care; residential aged care; registry; school; home; community; online panel; public place |
| Administration mode | self-complete; interviewer-administered; assisted; face-to-face; online; paper; CAPI; tablet; telephone; mixed mode |
| Time role | data-collection period; baseline; follow-up; admission; discharge; recall period; hypothetical episode; health-state duration; publication date; evidence snapshot |

Population definitions use composable fields. They also preserve a source-text definition. This is necessary for groups such as `Emirati national or non-national resident for at least five years`, `Ethiopian pediatric inpatient aged 4–18 years with prevalent acute illness`, and `German general population aged 65 years and older`. A condition mention is not sufficient to classify a condition as the study population.

Sample counts use a stage and a unit. For example, 1,145 interviews, 140 practice interviews, and 1,005 included respondents in S004 are three different counts. The ontology must not store only `sample size = 1,005` and discard the flow.

### 6.4 Method and protocol values

The method registry has a broad family and an exact method. Important preference-elicitation values in the packet are:

- conventional time trade-off;
- lead-time time trade-off;
- composite time trade-off, or cTTO;
- duration-free discrete choice experiment;
- discrete choice experiment with duration, also reported as DCEd or DCE-duration;
- discrete choice experiment with death;
- split-triplet task;
- kaizen task and its `aku` bad change;
- person trade-off;
- standard gamble;
- personal utility function elicitation, including dimension ranking, swing rating, location of dead, and interaction tasks;
- visual analogue scale valuation where the source uses it as a valuation method.

Named protocol values include MVH, Paris, EQ-VT, EQ-VT 2.0, EQ-VT 2.1, and EQ-VT 2.6.1. `EQ-VT version not reported` is an explicit missingness value, not a protocol version. A study can use EQ-VT and also adapt a training example, as the Egyptian study replaced the wheelchair example with a migraine example. Store the protocol implementation and the adaptation as separate facts.

Other controlled method families include qualitative analysis, psychometric analysis, evidence synthesis, survey quality control, sampling, and change classification. Exact methods include framework analysis, thematic analysis, content analysis, Mokken scaling, exploratory factor analysis, Paretian Classification of Health Change, COSMIN risk-of-bias assessment as source-reported, and modified GRADE as source-reported. These are methods, not generic `components`.

### 6.5 Statistical-model values

Store the complete source model label. Also assign broader model classes for recall. The packet supports exact values such as:

- main-effects conditional logit model estimated by maximum likelihood;
- mixed logit with linear time preference;
- mixed logit with nonlinear time preference and an immediate-death parameter;
- random-intercept cTTO model;
- random-effects Tobit model;
- heteroskedastic Tobit model;
- hybrid heteroskedastic Tobit model censored at −1;
- constrained heteroskedastic cTTO model;
- random-intercept linear regression;
- ordered logit;
- linear fixed-effect model;
- linear mixed-effect model;
- multilevel meta-regression;
- non-parametric item response theory with the monotone homogeneity and double monotonicity models.

Model qualifiers are first-class facts. They include censoring point, heteroskedasticity, random intercept, fixed or random effect, main effects, interaction terms, scaling parameter, time-preference form, covariate adjustment, weighting, bootstrap method, exclusion set, and sensitivity set. `Tobit` alone cannot answer a query for the preferred UAE value-set model.

### 6.6 Measurement-property and outcome values

| Family | Controlled values |
|---|---|
| Distribution and feasibility | missingness; completion; ceiling; floor; health-state frequency; completion time; help required; bot flag; speeding; duplicate; logical inconsistency |
| Reliability and agreement | test-retest reliability; dimension agreement; index agreement; self-proxy agreement; weighted kappa; Gwet's agreement coefficient; intraclass correlation coefficient |
| Validity | content validity; comprehensiveness; relevance; comprehensibility; convergent validity; divergent validity; known-groups validity; discriminant validity; structural validity |
| Responsiveness and change | responsiveness; standardized response mean; standardized effect size; anchor-defined change; Paretian change class; minimally important difference; minimal clinically important difference; minimal detectable change |
| Informativity and structure | Shannon index; Shannon evenness; factor loading; Loevinger coefficient; invariant item ordering |
| Health outcome | dimension response; health-state profile; EQ VAS; utility or index value; level sum score; transformed level sum score; QALY-related utility scale |
| Valuation quality | worse-than-dead rate; feedback flag; non-trader; speeding; flatlining; parameter ordering; model fit; state-value range |

The outcome registry keeps `MID` and `MCID` as distinct source terms unless a source explicitly equates them. It also keeps a Paretian category separate from an index change. A Paretian result describes the direction of profile changes but does not give their preference-weighted magnitude.

### 6.7 Product values

| Product type | Required content |
|---|---|
| Native value set or tariff | Target instrument version, preference jurisdiction, preference-source population, elicitation methods, protocol and version, model, anchors, scoring rule, range, worst-state value, production status, and source study. |
| Crosswalk | Source descriptive system, target value system, mapping method, population or data basis, version, and limitations. It must not be classified as a native value set. |
| Mapping function | Input scale, output scale, functional form, coefficients, model-selection basis, and validation results. |
| Instrument version | Family, version label, status at a date, dimensions, item wording, response levels, recall, intended age, respondent form, and language versions. |
| Protocol | Name, version, target instrument, component tasks, administration requirements, training, quality control, and supported adaptations. |
| Population norms or reference values | Instrument version, country, target population, data period, sample, weights, scoring value set, dimension distributions, index and EQ VAS summaries, and subgroup strata. |
| Evidence synthesis | Review question, eligibility, search dates, included-study count, appraisal method, outcomes, synthesis method, and conclusions. |
| Experimental design or quality-control specification | Task universe, exclusions, blocking or stratification, quotas, checks, thresholds, and intended use. |

`Plans to produce` and `produces` are different relations. S065 plans evidence to refine EQ-TIPS-5L. It reports no completed DCE result, value set, or final recommendation. The ontology must not create those products.

## 7. Representation at useful granularity

### 7.1 Populations and samples

A population record contains structured facets and the exact source definition. The minimum useful facets are:

- human role and respondent role;
- age bounds and units;
- country or region with its geography role;
- condition, condition status, and whether it is an inclusion, exclusion, or comparator condition;
- care or recruitment setting;
- residence, nationality, language, and other eligibility rules;
- proxy or self-report relation;
- study dates.

A sample is not a population definition. It records actual units, sample-flow stages, and subgroups. A study with baseline, retest, and follow-up samples needs separate counts. A review sample uses publications or studies as its units. A valuation study can also record counts of respondents, cTTO observations, and DCE responses without merging them.

### 7.2 Instrument use

An instrument application is the central link between a sample and an instrument. It records:

- instrument family and exact version;
- experimental or official status at the study date;
- language or localization;
- self, assisted-self, or proxy form;
- respondent role and requested perspective;
- mode and setting;
- recall period;
- time point;
- scoring rule or value set;
- whether EQ VAS was included.

This pattern supports the Amharic EQ-5D-Y-3L self and proxy applications in S069, the proxy-person perspective in S042, and the use of a Zimbabwe youth value set in Ethiopia. It does not attach the Zimbabwe value set to all EQ-5D-Y-3L uses.

### 7.3 Methods and analyses

A method application records the task actually used. For valuation, it includes the health-state instrument, task alternatives, durations, better-than-dead and worse-than-dead handling, hypothetical subject, respondent perspective, block design, administration mode, protocol version, adaptations, interviewer training, and quality control.

An analysis application records the exact model, data part, exclusions, outcome, parameters, uncertainty method, weighting, and sensitivity set. Preferred, candidate, and rejected models remain separate. This supports queries for all models tested and for only the model selected for a product.

### 7.4 Products

A product has its own identity and provenance. A value set is linked to, but is not identical to, its study or publication. A population-norm set records both the descriptive results and the value set used to calculate its index. An instrument version records content and status. A protocol records procedures. A systematic review produces an evidence synthesis, not a new value set unless the source says that it does.

### 7.5 Outcomes, estimates, comparisons, and findings

An estimate must contain:

- the outcome measure;
- statistic type, such as mean, median, proportion, coefficient, correlation, or count;
- value and unit;
- numerator and denominator when relevant;
- sample or subgroup;
- time point;
- instrument application;
- scoring value set or rule;
- method or model context;
- uncertainty, test statistic, and threshold when reported;
- source assertion and locator.

A comparison points to its members and gives the comparison basis. For example, S019 compares values for all 3,125 states across nonlinear DCEd and three EQ-VT models. S021 compares online and face-to-face cTTO. S068 compares responsiveness of 3L and 5L descriptive systems and nine pairs of country value sets. These are three different comparison designs.

A finding has a controlled finding type and a free-text statement. Useful types are observed association, difference, equivalence or similarity, superiority, no clear difference, feasibility conclusion, validity conclusion, recommendation, interpretation, limitation, and research gap. The finding records its subject, object, direction, population, context, supporting estimates, and evidence status.

## 8. Publication, study, project, and analytic separation

| Object | What it is | What it is not |
|---|---|---|
| Publication | A report with a DOI or other document identity. | It is not automatically one study or one funded project. |
| Study | A research activity with a design, samples, methods, and findings. | It is not the document that reports it and is not the grant that supported it. |
| Funded project | An administrative award with roles, dates, status, and budget. | It is not a publication count, a paper acknowledgement, or a study method. |
| Derived analytic | A computed view over selected evidence and linked data. | It is not a source-reported fact and must not be cited as if a paper reported it. |

The packet shows why this distinction is necessary. Project 341-RA links S019, a valuation-method comparison, and S070, a population-norms and inequality study. Project 2015200 links S097, S077, and S075, which report different studies. A project can therefore have multiple outputs and research families. The ontology also permits more than one publication for one study, but it requires evidence before it asserts that identity.

Every derived analytic records:

- a plain-language definition;
- the counting unit;
- numerator and denominator rules;
- inclusion and exclusion filters;
- treatment of unresolved links and missing values;
- input source snapshots;
- computation date;
- result and uncertainty where applicable.

This structure supports shares, medians, trends, citation ranks, time-to-publication, top-decile concentration, network communities, and topic similarity without mixing them with paper findings.

## 9. Provenance, conflict, and uncertainty

Each evidence assertion must record the summary ID and summary path. It should also record the summary hash, section locator, exact source term or compact source excerpt when needed, extraction date, and extraction status. The source paths and source hashes named inside summaries remain metadata from the summaries; they are not evidence that this proposal inspected the source papers.

The 50 packet summary hashes were checked against `B-papers.tsv`; all 50 matched.

Use these evidence states:

- **directly reported**: the summary states the fact;
- **normalized from a source term**: a canonical term was added, while source wording remains;
- **curated classification**: a reviewer assigned a controlled category;
- **derived**: a declared computation produced the value;
- **conflicting**: the source gives incompatible values;
- **unclear in source**: the summary reports unresolved ambiguity;
- **not reported**: the summary does not give the value;
- **planned but not produced**: a protocol or discussion names future work;
- **requires linked data**: the fact belongs to an external registry or corpus service.

Do not select one value silently when sources conflict. S004 reports a mean UAE sample age of 32.1 years in the Results and 39 years in the abstract. Store both estimates with their locators and place them in one evidence-conflict record. S074 reports unclear MDC row labels. Store the displayed values and the ambiguity statement. Do not resolve the labels without more evidence.

## 10. Complete example records

These records show the conceptual fields. They are not implementation syntax.

### 10.1 Example record: UAE EQ-5D-5L value set

**Source summary:** S004, `summaries/S004.md`, summary SHA-256 `87695bcc8b50df4ea0fa171636b70080f2f5a270643801a6076e456ffaf77be8`.

**Publication**

- Title: *A Value Set for EQ-5D-5L in the United Arab Emirates*.
- DOI: 10.1016/j.jval.2025.01.003.
- Publication form: national value-set research article.
- Output-project link: project ID 1465-VS, with the supplied project ID as the link basis.

**Study**

- Study families: health-state valuation and value-set development.
- Design: national valuation survey with two-stage quota sampling by emirate, age, and sex.
- Main collection period: January–August 2023. Practice interviews occurred in November–December 2022.
- Target population: adults aged 18 years or older who were Emirati nationals, or non-nationals resident in the UAE for at least five years, and who could complete an interview in Arabic or English.
- Sample flow: 1,145 interviews; 140 practice interviews excluded; 1,005 respondents included.
- Sample facts: 44.4% female and 11.4% nationals in the Results.
- Evidence conflict: mean age 32.1 years with SD 11.4 in the Results; average age 39 years with SD 10.8 in the abstract. Status: unresolved source discrepancy.

**Instrument applications**

- UAE Arabic EQ-5D-5L for Arabic-speaking participants.
- UK-validated English EQ-5D-5L for English-speaking participants because a UAE-specific English version was not available.
- EQ VAS was included.
- Administration mode: interviewer-administered, face-to-face or online.

**Method applications**

- Protocol: EQ-VT; exact version not reported in the summary.
- cTTO: conventional TTO for better-than-dead states and lead-time TTO for worse-than-dead states, followed by feedback.
- DCE: seven paired comparisons from 196 pairs in 28 blocks.
- Quality control: 14 interviewers received two-day training, five practice interviews, and online review; data collection paused at 25%, 50%, and 75% for interim review.

**Analysis and product**

- Ten candidate models were compared.
- Preferred model: hybrid heteroskedastic Tobit model censored at −1.
- Product: native UAE EQ-5D-5L value set.
- Product range: −0.654 for state 55555 to 1 for state 11111.
- Example product estimate: state 11211 has predicted utility 0.962.
- Dimension ranking: Mobility, Pain/Discomfort, Anxiety/Depression, Self-Care, Usual Activities.
- Intended uses: local cost-effectiveness analysis, population health assessment, and PROM applications.

**Findings and qualifications**

- The study combined Arabic and English and face-to-face and online data after reported quality parameters showed minimal differences.
- Illiterate, rural, and low-literacy participants were under-represented.
- The UK English version and the five-year expatriate criterion are reported limitations.

This record supports exact searches for a UAE native value set, cTTO plus DCE, a preferred censored hybrid model, mixed administration, and an unreported EQ-VT version. It does not fill the missing protocol version from another study.

### 10.2 Example record: Ethiopian EQ-5D-Y self and proxy agreement

**Source summary:** S069, `summaries/S069.md`, summary SHA-256 `cb60fac273ab808f24500c021999f9bcc6554b09e6396a8c88e032d2cb447778`.

**Publication**

- Title: *Psychometric evaluation of the EQ-5D-Y-3L in Ethiopian pediatric inpatients: comparing self and proxy reports*.
- DOI: 10.1186/s41687-025-00928-8.
- Publication form: repeated-measures psychometric research article.
- Output-project link: project ID 436-RA, with the supplied project ID as the link basis.

**Study and population**

- Study families: psychometric evaluation, responsiveness, and self-proxy agreement.
- Setting: University of Gondar Comprehensive Specialized Hospital, Ethiopia.
- Data period: 1 June–31 October 2023.
- Target population: patients aged 4–18 years with prevalent acute illness.
- Exclusions: low consciousness, disorientation, or visual impairment.
- Unit: child or adolescent and parent or caregiver dyad.
- Sample flow: 985 dyads recruited; 28 excluded for incomplete descriptive-system or EQ VAS data; 957 dyads analysed.
- Sample facts: mean child age 10.7 years with SD 4.3; 52.7% boys; 81.3% rural residents.
- Time points: admission and discharge.

**Instrument applications**

- Modified Amharic EQ-5D-Y-3L self-report with EQ VAS.
- Children aged 8–18 self-completed.
- Children aged 4–7 completed with trained data collectors who read instructions and questions and gave simple clarification without changing meaning.
- Parents or caregivers completed the proxy version.
- Scoring context: Zimbabwe EQ-5D-Y-3L value set. The source gives geographic proximity, socioeconomic similarities, and shared regional health challenges as the selection reasons.

**Analysis applications**

- Dimension agreement: weighted Cohen's kappa.
- Index and EQ VAS agreement: intraclass correlation coefficient.
- Index and EQ VAS convergence: Spearman rank correlation.
- Responsiveness: paired changes, percentage reduction in problems, and Paretian Classification of Health Change.
- External responsiveness anchor: physician-recorded clinical improvement.

**Estimates and findings**

- Total index ICC was 0.582 at admission and 0.498 at discharge.
- EQ VAS ICC was 0.671 at admission and 0.676 at discharge.
- Dimension agreement was fair to moderate at admission. Agreement for Worried, Sad, or Unhappy was lower at discharge, with kappa 0.15.
- Both perspectives showed significant index and EQ VAS improvement after treatment, with p below 0.001.
- Most participants were classified as improved under Paretian Classification of Health Change.
- The source concludes that the instrument was responsive during inpatient treatment and that self-proxy agreement was moderate.

**Qualifications**

- The hospital population was expected to improve and can overstate responsiveness.
- Children with developmental disabilities were excluded.
- The Zimbabwe value set might not represent Ethiopian preferences.
- The findings might not apply to outpatient or healthy populations.

This record supports a direct answer about EQ-5D-Y self versus proxy evidence. It keeps age-assisted self-report, proxy reporting, agreement estimates, responsiveness, and an externally sourced scoring value set as different facts.

### 10.3 Example record: planned EQ-TIPS-5L DCE waves

**Source summary:** S065, `summaries/S065.md`, summary SHA-256 `fa20613afcef0f358ca405b244a2701dcc7a5df5b7349f7312c744ea2ede224a`.

**Publication**

- Title: *Assessing the experimental EuroQol toddler and infant populations (EQ-TIPS) descriptive system: a protocol integrating discrete choice experiment (DCE) surveys in instrument development*.
- DOI: 10.1136/bmjopen-2025-100897.
- Publication form: study protocol.
- Output-project link: project ID 1850-RA, with the supplied project ID as the link basis.

**Planned study**

- Study families: instrument development and preference-method evaluation.
- Evidence status: planned in the protocol. Current operational status is unknown.
- Decision context: a one-month acute health episode for a one-year-old child, followed by recovery.
- Respondents: Australian adults from the general community.
- Wave 1 planned sample: 400 adults, 14 kaizen tasks per respondent.
- Wave 2 planned sample: 1,000 adults, 28 paired comparisons per respondent.
- Planned total: 1,400 adults.

**Instrument and methods**

- Instrument: experimental EQ-TIPS-5L V3.0.
- Dimensions: Movement, Eating or Drinking, Sleep, Pain, Managing Emotions, Interacting with Others, and Play.
- Response structure: five ordered problem or pain levels.
- Wave 1 method: kaizen choice tasks with four improvements and one `aku` bad change.
- Wave 2 method: paired comparisons between two EQ-TIPS profiles.
- Planned primary model: main-effects conditional logit estimated by maximum likelihood.
- Planned uncertainty method: 1,000-iteration cluster bootstrap with block-specific strata.

**Products and evidence gaps**

- Planned product: preference evidence to inform refinement of EQ-TIPS-5L.
- No completed DCE result is reported.
- No value set is reported.
- No final instrument recommendation is reported.
- Ethics approval was granted on 19 February 2025.

This record prevents a protocol from appearing as a completed valuation study or as evidence that a study is ongoing now.

## 11. Support for the 50 competency questions

### 11.1 Answerability classes

- **Answerable from supplied summaries:** Direct assertions or a declared packet-bounded derivation can answer the question. The result is not claimed to be complete outside this packet.
- **Requires external linked data:** The ontology has the concepts and relations, but one or more required facts are absent from the summaries. The table names the needed data.
- **Unsupported by available evidence:** The supplied summaries do not contain the exact evidence needed for the requested relation. The system must return an evidence gap and must not infer an answer from nearby concepts.

### 11.2 Question-by-question coverage

| Question | Required concepts and relations | Answerability and evidence |
|---|---|---|
| Q41 — Publications that introduced or validated EQ-VT | Publication `reports` Study; Study family; Protocol; `introduces`, `evaluates`, or `validates`; Finding and evidence status | **Answerable from supplied summaries.** S002 introduces and critiques MVH, Paris, and EQ-VT and recommends EQ-VT for EQ-5D-5L. No supplied summary explicitly reports a formal validation of the full EQ-VT protocol, so the answer must state that limit. |
| Q22 — Time from applicant X's previous grant to first publication | Resolved Person; applicant or PI role; ordered Project awards; project start or award date; Output-project link; Publication date; derived duration | **Requires external linked data.** It needs the grant register, person resolution, complete project-output links, and publication dates. |
| Q90 — Projects that produced later-referenced value sets | Project `has output` Publication or Value set; native product type; Citation from later corpus publication; citation date | **Requires external linked data.** The packet identifies several value-set products, but it does not supply a complete citation graph. |
| Q68 — Share of methodological literature that acknowledges EuroQol funding | Publication classified as EQ-5D methodology; Funding statement `names funder`; corpus inclusion rule; derived numerator and denominator | **Requires external linked data.** It needs complete corpus classification and funding-acknowledgement data. A packet-only share could be computed but would not answer the corpus question. |
| Q47 — Members who co-authored with researcher X on funded outputs | Resolved people; Authorship; time-qualified Membership; Output-project link with funding basis; co-author relation | **Requires external linked data.** Author lists, identity resolution, membership history, and complete funded-output links are not present for all summaries. |
| Q40 — EQ-5D-5L valuation studies that are ongoing now | Study family `value-set development` or `valuation`; `uses instrument` EQ-5D-5L; current Study or Project status; status date | **Requires external linked data.** A protocol publication is not proof of current activity. A current project registry or study-status source is required. |
| Q39 — Conditions for which bolt-on dimensions were developed or tested | Bolt-on dimension; parent Instrument version; `developed for` or `tested in` Condition; Study and Population | **Unsupported by available evidence.** S065 mentions 13 unnamed EQ-5D bolt-ons, and S078 suggests climate-related or psychosocial bolt-ons. Neither gives an exact bolt-on-to-condition development or test relation. |
| Q77 — Top-decile concentration of PI output | Resolved Person; PI role; Project; linked Publication; counting rule; decile rule; derived share | **Requires external linked data.** It needs a complete PI and output registry plus identity resolution. |
| Q36 — Proxy versus self-report agreement for EQ-5D-Y | Study `uses instrument` youth version; Instrument applications with self and proxy perspectives; agreement Outcome and Estimate | **Answerable from supplied summaries.** S069 reports Amharic EQ-5D-Y-3L self-proxy agreement in Ethiopian inpatients. S085 reports Indonesian EQ-5D-Y-3L and experimental 5L proxy agreement with self-report. |
| Q93 — First-time PIs who published from their first grant | Person; ordered PI roles; first Project; Output-project link; Publication date | **Requires external linked data.** It needs grant histories, role dates, and complete output links. |
| Q21 — Applicant X's prior co-authorship with EuroQol members | Applicant resolved to Person; Authorship before application date; time-qualified Membership; co-author relation | **Requires external linked data.** It needs author, membership, identity, and application-date records. |
| Q56 — Supervisors and institutions for student grants | Project classified as student grant; supervisor role; student role; recipient Organization; affiliation interval | **Requires external linked data.** The packet has project IDs but no complete student-grant administration records. |
| Q1 — Total funded projects and combined approved budget | Project identity; funding status; approved Budget with currency; aggregation date; deduplication rule | **Requires external linked data.** A grant registry and currency policy are required. |
| Q59 — Open-access papers that introduce EQ-HWB | Publication `introduces` Instrument version or development concept; Open-access status and licence at a date | **Requires external linked data.** S058 and S034 provide EQ-HWB development evidence, but the summaries do not give sufficient publication-level access and licence data. |
| Q12 — Most-cited funded publication and its project | Publication Citation count at snapshot; Output-project link; funding-link basis; ranking rule | **Requires external linked data.** Citation counts and a complete project-output graph are absent. |
| Q67 — Starter reading list on child health-state valuation | Publication topic; child valuation population or perspective; Study family; evidence type; derived relevance and reading-order rules | **Answerable from supplied summaries as a declared derived view.** A packet-bounded list can start with S032 for the systematic review, then use S007 for an Indonesian youth value set, S039 for Canadian stakeholder choices, S031 for Australian public reasoning, and S002 for TTO protocol context. `Starter` remains an editorial ranking, not a paper fact. |
| Q33 — Studies that compare 5L and 3L value sets in the same population | Study and Sample; Instrument applications for 3L and 5L; Value sets; Comparison; same-sample evidence | **Answerable from supplied summaries.** S073 applies US 3L, native 5L, and crosswalk scoring to paired data sources. S068 applies nine country pairs of 3L and 5L value sets to the same German rehabilitation and Polish stroke samples. |
| Q71 — Open-access share and trend for funded publications | Publication access status and date; Output-project link; year; numerator and denominator; trend definition | **Requires external linked data.** It needs historical access metadata and a complete funded-publication set. |
| Q99 — Share of member-authored corpus papers excluded as pure applications | Resolved author; time-qualified Membership; corpus screening decision; exclusion reason `pure application`; derived share | **Requires external linked data.** It needs the corpus screening audit and membership data. |
| Q81 — Share of resolved researchers with an ORCID | Resolved Person; ORCID identifier; identity confidence; denominator rule | **Requires external linked data.** The summaries do not give an identity registry. |
| Q3 — Approved-budget distribution | Project; approved Budget; currency and conversion date; median, quartiles, IQR, and maximum derivations | **Requires external linked data.** It needs complete grant financial records and a currency rule. |
| Q6 — Proportion of completed projects with a linked publication | Project status; Output-project link; completion date; denominator and unresolved-link policy | **Requires external linked data.** Project completion and complete output linkage are absent. |
| Q78 — Non-members who co-author most often with members | Resolved people; Authorship; time-qualified Membership; co-author edge count; ranking rule | **Requires external linked data.** It needs complete authorship and membership data. |
| Q80 — Inter-grant citation flow | Project-to-output links; Publication `cites` Publication; source and target Project; citation snapshot | **Requires external linked data.** The packet does not contain reference lists or a citation graph. |
| Q7 — Median time from project start to first publication | Project start date; linked Publication dates; first-output rule; median derivation; censoring rule | **Requires external linked data.** Grant dates and complete publication links are required. |
| Q83 — Papers per project by working group | Project `assigned to working group`; linked Publications; counting and multi-group allocation rules | **Requires external linked data.** The packet does not give administrative working-group assignments. |
| Q100 — Entry through full-text mining versus funder metadata | Publication; Ingestion event; route value; run date; evidence and deduplication decision | **Requires external linked data.** This is workflow provenance, not a paper fact. |
| Q30 — Value sets that used EQ-VT and its version | Value set `produced by` Study; Method application `implements protocol`; exact Protocol version; evidence status | **Answerable from supplied summaries.** Danish S023 used EQ-VT 2.1, French S013 used EQ-VT 2.0, Egyptian S022 used EQ-VT 2.1, and Moroccan S008 used EQ-VT 2.6.1. UAE S004 used EQ-VT, but the exact version is not reported in its summary. |
| Q15 — Funding acknowledgements with no project ID match | Publication Funding statement; named EuroQol funder; grant text; Output-project link status and match reason | **Requires external linked data.** A complete acknowledgement extraction and project-match audit are required. A summary project header alone must not replace that audit. |
| Q64 — Most-cited systematic reviews | Publication classified as systematic review; Citation count and snapshot; corpus scope; ranking | **Requires external linked data.** Citation metrics are absent. The packet supplies review classifications that can seed the candidate set. |
| Q62 — People at institution X who work on EQ topics | Resolved Person; time-qualified Affiliation; Publication topics and dates; institution identity | **Requires external linked data.** Complete authorship and affiliation records are absent. |
| Q70 — Co-authorship communities among members | Resolved people; time-qualified Membership; co-author network; edge weighting; community algorithm and snapshot | **Requires external linked data.** This is a derived network analytic over identity and authorship data. |
| Q53 — Ten most-cited papers on EQ-5D valuation methodology | Publication topic and Study family; Citation count at snapshot; ranking and tie rule | **Requires external linked data.** It needs bibliometric data and a complete methodology corpus. |
| Q54 — Difference between a crosswalk and a native 5L value set | Product type; `derived by mapping from`; native preference evidence; target instrument; comparison findings; key Publication links | **Answerable from supplied summaries.** A native 5L value set estimates values from preferences collected for 5L states. A 5L-to-3L crosswalk maps 5L profiles to a 3L value system. S073 directly compares US native 5L, 3L, and crosswalk scoring; S023 and S013 also compare native 5L products with 3L or crosswalk values. |
| Q58 — Published work on EQ-5D-Y-5L | Instrument version; publication date; Study family; self or proxy form; status at study date | **Answerable from supplied summaries in packet scope.** S064 reports development of the self-report 5L. S039 reports Canadian stakeholder views on 3L versus 5L and valuation. S085 evaluates an experimental 5L proxy version against 3L and self-report. A current exhaustive answer needs a complete bibliography. |
| Q11 — Countries whose institutions received most funding | Project recipient Organization; organization country; approved Budget; aggregation and currency rules | **Requires external linked data.** Study location or value-set jurisdiction cannot stand in for fund-recipient country. |
| Q18 — Past projects most similar to a proposal abstract | Project abstract and controlled topics; user Proposal abstract; similarity method; date and status filters | **Requires external linked data.** It needs project abstracts and the proposal text. Similarity is a derived analytic, not a source fact. |
| Q44 — Working groups spanned by researcher X | Resolved Person; authored outputs or Project roles; Project `assigned to working group`; date and span rule | **Requires external linked data.** Topic classification must not be used as proof of formal working-group assignment. |
| Q95 — Projects that studied children or cognitive impairment | Project link; Study `targets population`; age and condition roles; inclusion and exclusion evidence | **Answerable from supplied summaries in packet scope.** Direct child or pediatric samples occur in S066, S069, S064, S031, S060, and S085. S061, S065, S039, S032, and S007 provide child-focused evidence through experts, adult stakeholders, reviews, proxies, or hypothetical-child valuation. The packet mainly reports exclusion or under-representation of cognitive impairment in S017, S097, S042, S090, and S069; these exclusions are not evidence that those projects studied cognitive impairment. |
| Q31 — People currently working on EQ-HWB valuation | Resolved Person; Study or Project topic EQ-HWB valuation; current role and status; evidence date | **Requires external linked data.** Publications show past authorship and instrument work, not current activity. |
| Q74 — Researchers who entered the corpus in the last three years | Resolved Person; first corpus Publication date; corpus snapshot; three-year interval rule | **Requires external linked data.** It needs complete publication history and identity resolution. |
| Q87 — Identity profiles merged, overridden, or skipped | Identity-resolution decision; source and target profiles; action; reason; actor; time; evidence | **Requires external linked data.** This is identity workflow provenance and is absent from paper summaries. |
| Q14 — PIs with most grants by count and budget | Resolved Person; PI role; Project; approved Budget; count, currency, and ranking rules | **Requires external linked data.** The packet does not contain PI and budget records. |
| Q57 — Frequent methods in funded valuation projects | Project link; Study family `valuation`; Method application; exact method and broader family; frequency and learning-order derivation | **Answerable from supplied summaries as a packet-bounded derived view.** cTTO and DCE recur. Exact elicitation variants include DCE with duration, DCE with death, split triplets, and kaizen tasks. Other work uses personal utility function elicitation and DCE-to-TTO mapping. Hybrid is a model family, not an elicitation method. The view must count study-level method applications and keep exact variants visible. `What should I learn` is a recommendation with a declared ranking rule. |
| Q5 — Working group with most projects and budget | Project `assigned to working group`; approved Budget; project count; multi-group and currency rules | **Requires external linked data.** Administrative group and budget records are absent. |
| Q20 — Ongoing projects that overlap with proposal aims | Current Project status; project aim or abstract; user Proposal aim; similarity or concept-overlap analytic | **Requires external linked data.** It needs current project data and the proposal content. |
| Q72 — Citations of funded papers versus other corpus papers | Person; authored Publication; funding-linked versus other classification; Citation counts; matched comparison rule | **Requires external linked data.** Bibliometric, identity, and complete funding-link data are required. |
| Q27 — Productivity of projects in the proposal's budget band | Project Budget; proposal Budget; band definition; linked output counts; project duration and completion; derived comparison | **Requires external linked data.** It needs grant finances, proposal input, status, and output linkage. |
| Q51 — Existing EQ-TIPS work | Instrument family and exact version; Study family; Publication date; Population; Product and evidence status | **Answerable from supplied summaries in packet scope.** S061 reports expert content work on experimental V2.0 or 3L, S060 compares V2.0 with PedsQL in Australian children aged 2–3 by proxy, and S065 reports planned DCE work for experimental 5L V3.0. None reports an EQ-TIPS value set. |
| Q34 — EQ-5D-5L population norms by country | Product classified as population norms or reference values; country as norm jurisdiction; target age; survey period; instrument and scoring value set | **Answerable from supplied summaries in packet scope.** S070 reports Trinidad and Tobago 5L norms for 2022–2023 and comparison with 2012. S027 reports Romanian 3L and 5L norms. S077 reports German 5L reference values for people aged 65 years and older. S089 aims to support norms but reports data-quality results, so it is not itself a norm product. |

## 12. Free text, optional facts, derived facts, and scope limits

### 12.1 Facts that remain free text

Some content loses meaning if it is forced into a short controlled value. Keep these facts as evidence-linked text, with optional controlled tags:

- full research aims and rationales;
- detailed eligibility and exclusion wording;
- interview prompts, item examples, and respondent explanations;
- author interpretations of cultural or behavioural causes;
- limitations and generalizability statements;
- ethical concerns and acceptability comments;
- recommendations and future-work statements;
- exact model-selection rationale;
- unclear or conflicting source passages.

The ontology can add topics such as `cultural context`, `cognitive burden`, or `selection bias`, but the tag does not replace the source statement.

### 12.2 Optional facts

Most fields are optional because study families differ. A methods paper can have no participant sample. A protocol can have planned samples but no estimates. A qualitative study can have no statistical model. A systematic review can have publication counts instead of patient counts. A product can be planned but absent.

Optional details include software, ethics identifier, compensation, interviewer training duration, task blocks, response-quality thresholds, data availability, conflict statements, and exact coefficients. They become important when a query or comparison uses them.

No field should use a false placeholder. Use an explicit missingness statement when absence matters.

### 12.3 Derived analytics

The following requested results are derived and must never appear as paper assertions unless a paper reported that exact result:

- project and publication counts;
- combined budgets, medians, IQRs, and budget bands;
- open-access and funding-acknowledgement shares and trends;
- time from grant to publication;
- citation ranks and comparisons;
- papers per project or working group;
- top-decile PI concentration;
- co-authorship communities and collaborator ranks;
- inter-grant citation flow;
- researcher entry dates;
- topic-similarity rankings and starter reading lists.

### 12.4 Outside the supplied evidence

The ontology can link these data, but the packet does not supply them completely:

- grant titles, approved budgets, award and completion dates, status, PI, applicant, supervisor, recipient institution, and working-group assignment;
- current project and researcher activity;
- complete authorship, affiliation, membership, and ORCID data;
- publication licences, open-access history, and citation counts;
- reference lists and project-to-project citation links;
- corpus screening, ingestion, and identity-resolution logs;
- proposal abstracts and budgets supplied at query time.

## 13. Unresolved design choices and risks

1. **Study identity across publications.** DOI identity is easier than study identity. A later curation rule must decide when two reports describe the same study, related waves, or reused data.
2. **Meaning of a supplied project ID.** The packet links every summary to a project ID, but the ontology should retain the link basis. It must not assume that every project paid for every reported study component.
3. **Instrument status over time.** `Experimental`, `final`, and `official` can change. Status needs a date and source. EQ-5D-Y-5L self and proxy forms show this risk.
4. **Short-form identity.** The packet uses EQ-HWB-S and EQ-HWB-9 in different studies. The ontology should keep them separate until evidence states their exact relation.
5. **Term equivalence across languages.** Literal translation does not prove conceptual identity. Store language-specific labels and validated mappings.
6. **Protocol use versus protocol compliance.** A study can state that it used EQ-VT and still adapt examples, modes, or quality checks. Protocol version, implementation, adaptation, and compliance are separate facts.
7. **Model-name granularity.** Very broad labels make search easy but hide decisive details. The design must keep both the exact model and multiple broader classifications.
8. **Outcome comparability.** EQ VAS, LSS, transformed LSS, a native utility, and a crosswalk utility can all use numeric scales. They must not merge by numeric range alone.
9. **Counting systematic-review evidence.** A review result and each included primary study are different evidence units. A corpus statistic must state whether it counts publications, studies, samples, or estimates.
10. **Current and historical truth.** Membership, affiliation, open access, citations, and project status change. Each needs a snapshot or interval.
11. **Identity-resolution error.** A wrong merge can distort grant counts, collaboration networks, and citation comparisons. All decisions need an audit trail and reversible evidence links.
12. **Topic classification drift.** A paper can concern children without sampling children, as in adult valuation of a hypothetical child. Population role, respondent role, and topic must remain separate.
13. **Evidence quality versus fact provenance.** A well-provenanced result can still have study limitations. Provenance status and methodological quality must be separate dimensions.
14. **Conflicting source summaries.** The system must expose conflicts such as the S004 age values and the S074 MDC labels. An automated search must not choose one silently.
15. **Recommendation questions.** `Good starter reading` and `what should I learn` require declared editorial criteria. They are derived views, not objective source facts.

## 14. Minimum viable ontology and extension order

The first implementation should include the evidence layer, Publication, Study, Study part, Project link, Population, Sample and Sample count, Instrument version, Instrument application, Method application, Statistical model, Product, Outcome, Estimate, Finding, and Limitation. It should also include the exact controlled families for study purpose, instrument version, respondent perspective, administration mode, valuation method, model, measurement property, and product type.

The next extension should add grant administration, people and identity resolution, authorship and membership, working groups, citations, open-access metadata, and ingestion provenance. These extensions are necessary for most funding, people, network, and bibliometric questions. They must use the same assertion-level provenance and time model as the research-content layer.

This order gives useful scientific search before all administrative data are available. It also prevents missing external facts from weakening the exact representation of the supplied EuroQol research evidence.
