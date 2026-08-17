# EuroQol research ontology proposal: lineage C

## 1. Purpose and scope

This ontology supports precise search, comparison, and synthesis of EuroQol research. It is based on the 50 supplied paper summaries and the 50 supplied competency questions. The summaries are a design sample. They are not a complete inventory of EuroQol projects or publications.

The ontology gives priority to facts that a researcher can use directly. It represents, for example:

- a valuation study as a study classification;
- EQ-5D-5L as an exact instrument version;
- cTTO, DCE without duration, and DCE with duration as different valuation methods;
- EQ-VT version 1.1, EQ-VT version 2.1, and the EQ-VT 2.1 lite protocol as different protocol specifications;
- a heteroscedastic censored hybrid model, a hybrid heteroskedastic Tobit model, ADD20-I, and a mixed-logit model as exact statistical models;
- a study population, an enrolled sample, an analysed sample, and a retest sample as different groups;
- a native value set and a crosswalk value set as different products;
- an outcome definition, a numerical estimate, and an author finding as different facts;
- a publication, a study, a funded project, and a system-derived analytic as different records.

The ontology must not turn missing data into negative evidence. It can state that S061 did not produce a value set because the summary says this. It cannot state that an unmentioned project produced no value set.

The ontology has three use boundaries:

1. It describes research evidence and the administration data that are needed to find that evidence.
2. It does not contain person-level study data.
3. It does not claim a current global inventory unless an authoritative external source is linked and dated.

## 2. Design principles

### 2.1 Keep four information layers separate

| Layer | Meaning | Example |
|---|---|---|
| Source evidence | What a supplied source states, with its wording and location | S023 uses the source term “heteroscedastic censored hybrid model.” |
| Canonical research record | The normalized entity or fact that supports retrieval | The model is one identified Statistical Model used by the S023 analysis. |
| Controlled classification | A maintained category assigned under a named scheme | S023 is classified as a valuation study and a national value-set study. |
| Derived analytic | A result calculated by the research system from a defined data snapshot | Median time from project start to first accepted linked publication. |

A source term is not overwritten by its canonical term. The source strings “composite Time Trade Off,” “composite time trade-off,” and “cTTO” can all map to the canonical cTTO concept. Each source string remains available for audit and text search.

A classification is also not the entity itself. A Study can have more than one justified classification. For example, S019 is both a valuation-method comparison and an empirical stated-preference study.

A paper finding is not a system-derived analytic. “The authors conclude that 5L has lower ceiling and floor effects” is a Finding reported by S090. A portfolio count of all studies that favour 5L is a Derived Analytic.

### 2.2 Give each fact evidence and context

An Evidence Assertion is the central provenance record. It connects:

- the subject of the assertion;
- the precise relation or measured property;
- the object or literal value;
- the source summary and source location;
- the exact source term when it is useful;
- qualifiers such as sample, country role, timepoint, instrument version, administration, respondent perspective, comparison, unit, and uncertainty;
- the evidence status, such as stated, planned, not produced, not reported, or source-conflicted.

This pattern is necessary for n-ary facts. For example, an ICC of 0.85 has little meaning without the instrument, score, retest sample, interval, ICC specification, and study.

The model keeps both source-reported values when a source conflicts with itself. It marks a conflict group and does not silently select one value. The supplied summaries contain useful test cases:

- S004 reports two different mean ages.
- S041 reports two denominator choices for future willingness.
- S047 reports two different physiotherapy EQ VAS changes.

### 2.3 Use semantic relations

The ontology does not use generic relations such as related to or has. It uses relations such as reports study, evaluates instrument, follows protocol, elicits preference with, selects model, produces value set, maps from value set, and supports project-output link.

Direction has meaning. A Publication reports a Study. A Study evaluates an Instrument Version. A Value Set scores an Instrument Version. A Crosswalk maps responses or values from one specified system to another.

### 2.4 Do not force one study template

A national valuation study, a systematic review, an implementation study, and a qualitative instrument-development study need different facts. All can use the same core concepts, but each concept is optional unless the evidence supports it. Study-family templates are views for quality checks. They are not universal cardinality rules.

## 3. Main concepts

### 3.1 Sources, publications, projects, and people

| Concept | Meaning for a EuroQol researcher | Main identity and scope |
|---|---|---|
| Source Summary | The fixed summary from which an assertion was extracted | Summary ID and verified SHA-256 |
| Evidence Assertion | One sourced claim with qualifiers, provenance, and evidence status | Stable assertion identifier |
| Publication | A public research output, such as a journal article | DOI when supplied; title and publication date |
| Study | A planned or completed investigation reported by one or more publications | Study identifier that is separate from DOI |
| Funded Project | An administrative award or project with its own title, dates, status, budget, and roles | Project ID in its registry namespace |
| Project-Output Link | An evidence-bearing claim that a publication is an output of a project | Project, publication, link status, evidence type, decision, and date |
| Person | A researcher, applicant, author, interviewer, or other identified person | Verified person identifier; ORCID when linked |
| Authorship | A person’s ordered author role on one publication | Publication, person, author position, and role |
| Organization | A university, foundation, HTA body, hospital, company, registry, or care provider | Canonical organization identifier; ROR when linked |
| Affiliation Episode | A person’s affiliation with an organization during a stated period | Person, organization, dates, and source |
| Project Participation | A person or organization role in a project | PI, co-applicant, staff role, dates, and evidence |
| Membership Episode | EuroQol membership during a stated period | Person, membership type, start, end, and source |
| Working-Group Participation | Participation in a named EuroQol working group during a stated period | Person, working group, role, and dates |
| Identity-Resolution Decision | A logged merge, override, split, or skip decision for source profiles | Input profiles, decision, reason, rule or reviewer, and date |
| Citation Link | A citing publication to cited publication relation | Source, target, citation source, and retrieval date |
| Topic Assignment | A topic or field assigned to a publication by a named system | Publication, scheme, topic, score, and retrieval date |
| Access Status | Open-access status under a named source and date | Publication, status, route or licence when known, and date |
| Place and Country | A geographic entity used with an explicit role | Stable geographic identifier and canonical label |

The Project-Output Link is an intermediate record because the relation needs its own evidence. Evidence can include an explicit funding statement, a project ID in the publication record, a project report, or a reviewed administrative link. A year-window rule can help triage a candidate link. It must not by itself prove that the link is accepted.

### 3.2 Instruments and forms

| Concept | Meaning |
|---|---|
| Instrument Family | A broad family, such as EQ-5D, EQ-5D-Y, EQ-TIPS, or EQ-HWB |
| Instrument Version | An exact descriptive system, such as EQ-5D-3L, EQ-5D-5L, EQ-5D-Y-3L, EQ-5D-Y-5L, EQ-TIPS V2.0, or EQ-HWB-S experimental version 1.0 |
| Instrument Form | A self-report, proxy, interviewer-administered, or other named form of an Instrument Version |
| Language Adaptation | A version in a specified language and locale, with an adaptation status and process when reported |
| Dimension | A named instrument domain, such as mobility, pain/discomfort, cognition, or exhaustion |
| Response Level | A level with its order and exact wording for one dimension and version |
| Recall Period | The time reference in a form, such as today, the last 24 hours, or the past seven days |
| Bolt-On Specification | A candidate or implemented dimension that extends a named base Instrument Version |
| Health-State Definition | A profile in a named descriptive system, such as EQ-5D-5L 55555 |

Instrument version identity must include meaningful release information. EQ-TIPS V2.0 and the label EQ-TIPS-3L can be co-designations only when a source explicitly connects them, as S061 does. The ontology must not infer that an unnamed five-level experimental form is EQ-TIPS V5.0.

A bolt-on is not only a keyword. It links a base Instrument Version, the added Dimension, its wording and levels when reported, its development status, and the study activity. A study can test bolt-on psychometric performance, preference impact, wording, or implementation. These are different roles.

### 3.3 Populations, samples, and administration

| Concept | Meaning |
|---|---|
| Population Definition | The group to which a study intends to apply, with age, condition, geography, and social role |
| Eligibility Criterion | A stated inclusion or exclusion rule |
| Sample or Cohort | A concrete group at one stage of a study |
| Sample Derivation | The inclusion, exclusion, split, or follow-up relation between samples |
| Condition | A canonical health condition with preserved source aliases |
| Life Stage | A controlled age or life-stage concept, such as infant, child, adolescent, adult, older adult, pregnancy, or postpartum |
| Reporter Role | Child self-report, adult self-report, caregiver proxy, staff proxy, family proxy, expert, stakeholder, or general-public valuer |
| Preference Perspective | Own adult health, another adult, a 4-year-old child, a 10-year-old child, an unspecified child, or another explicit perspective |
| Administration Event | Use of one form with one sample at a timepoint, language, mode, setting, and reporter role |
| Study Timepoint | Baseline, retest, follow-up, pregnancy month, postpartum month, heatwave wave, or another named time |

Target population and observed sample are separate. “Nationally representative adult population” is a target or sampling aim. “1,014 analysed respondents” is a sample. The ontology records whether representativeness was designed, assessed, limited, or only claimed.

Each sample size needs a count type. Useful values include invited, eligible, registered, completed, included, analysed, retested, stable at retest, and retained at follow-up. This prevents a target sample size from being confused with an analysed sample.

Country relations also need roles. The following facts are not interchangeable:

- study conducted in a country;
- respondent residence;
- sampled preference population;
- target country for a value set;
- language or locale of an instrument form;
- organization location;
- author affiliation country.

### 3.4 Study activities, methods, and analyses

| Concept | Meaning |
|---|---|
| Study Classification | One controlled study-purpose assignment |
| Study Activity | A bounded activity, such as data collection, translation, valuation, psychometric assessment, or qualitative consultation |
| Valuation Study | A Study classification for eliciting or modelling preferences to estimate health-state values |
| Valuation Protocol | A named specification and version, such as EQ-VT 2.1 or the lite protocol |
| Elicitation Task | The exact task used to obtain preference evidence |
| Health-State Design | The states, pairs, blocks, overlap, severity coverage, randomization, and hold-outs used in tasks |
| Quality-Control Procedure | A stated training, flag, exclusion, feedback, bot, speeding, duplicate, or monitoring rule |
| Dataset | The observations used by an analysis, with the sample and observation count |
| Statistical Analysis | One analysis with inputs, purpose, software when useful, and outputs |
| Statistical Model | An exact model specification, not only a broad model family |
| Model Selection Decision | A decision that compares candidate models and selects one, with stated criteria |
| Comparison | A defined contrast between instruments, methods, samples, timepoints, products, or groups |

The ontology records instrument use through exact roles:

- develops Instrument Version;
- translates or adapts Instrument Version;
- administers Instrument Form;
- evaluates measurement properties of Instrument Version;
- values health states of Instrument Version;
- uses Instrument Version as a comparator;
- scores observations with Value Set;
- maps observations from one instrument to another;
- implements Instrument Version in a service;
- tests Bolt-On Specification for a base version.

This role model prevents a paper that only uses an Indonesian EQ-5D-5L value set to score outcomes from being returned as an Indonesian value-set development study.

### 3.5 Products, outcomes, estimates, and findings

| Concept | Meaning |
|---|---|
| Research Product | A separately identified output of a study or project |
| Value Set | A rule or set of values that assigns preference weights to states from one exact Instrument Version |
| Native Value Set | A Value Set based on direct valuation evidence for the target country or population, under a stated operational definition |
| Crosswalk Value Set | A derived scoring product that maps responses or values through another descriptive system or value set |
| Scoring Rule | A formula, coefficient set, table, or algorithm used to calculate a score |
| Dataset Product | A released or governed dataset, with access conditions |
| Implementation Product | A workflow, display, training package, or decision-support resource |
| Outcome Definition | The measured construct and metric, such as test-retest reliability by ICC or full-health ceiling proportion |
| Estimate | A numerical or categorical result for one Outcome Definition in its full context |
| Finding | A source-stated interpretation, conclusion, or qualitative theme |
| Limitation | A source-stated constraint on interpretation |
| Recommendation | A source-stated proposed action or future research need |

A Value Set must link to:

- its exact Instrument Version;
- target country or population;
- preference source and perspective;
- protocol and version when reported;
- elicitation tasks;
- analysed samples and data;
- selected Statistical Model;
- anchor and scale;
- scoring rule or coefficient product;
- publication and study that report it;
- release or publication date and status.

A Crosswalk Value Set must also state the source descriptive system or value set, the target descriptive system, the mapping algorithm, and the population in which the mapping was developed when known. “Native” and “crosswalk” are controlled product classifications. They are not aliases.

An Outcome Definition supplies meaning. An Estimate supplies value. For example, test-retest reliability is an Outcome Definition; ICC 0.85 for the EQ-5D-5L utility score in the S090 retest sample is an Estimate. A Finding can then state the authors’ interpretation of that estimate.

## 4. Controlled classifications and exact value families

### 4.1 Study-purpose classification

The classification is multi-valued. It includes:

- valuation study;
- national value-set development;
- valuation protocol or task evaluation;
- statistical or valuation model development;
- value-set or scoring-product comparison;
- instrument or descriptive-system development;
- translation or language adaptation;
- content-validity study;
- psychometric or measurement-property study;
- qualitative stakeholder study;
- systematic review or evidence synthesis;
- population-health or health-status study;
- routine PROM or registry study;
- implementation or feasibility study;
- economic evaluation or cost-utility model;
- survey-method and data-quality study;
- methodological, policy, or taxonomy paper.

Publication type is separate. “Peer-reviewed research article” describes a Publication. “Valuation study” describes a Study.

### 4.2 Instrument status and role

Status values include official, experimental, pilot, in development, planned, and not available for the reported study. Status needs a date and source.

Instrument roles include target of development, target of valuation, instrument under psychometric evaluation, primary outcome instrument, comparator instrument, scoring source, mapped source, mapped target, base instrument for a bolt-on, and implementation instrument.

### 4.3 Valuation method family

The controlled method family preserves these exact distinctions:

| Family | Exact methods supported by the summaries |
|---|---|
| Time trade-off | TTO, conventional TTO, lead-time TTO, composite time trade-off or cTTO, lag-time TTO |
| Discrete choice | DCE without duration, DCE with duration or DCEd, DCE-death, split-triplet DCEd |
| Pairwise or sequential choice | Pairwise choice, pick-one task, Kaizen task |
| Rating and weighting | VAS anchor, dimension ranking, swing weighting, level rating, location of dead, OPUF, personal utility function |
| Other preference methods | Standard gamble and best-worst scaling when a study reports them |

The model must not treat all uses of “hybrid” as the same fact:

- a hybrid statistical model can combine cTTO and DCE likelihoods;
- a study can use more than one elicitation method without selecting a hybrid statistical model;
- DCE with duration is one elicitation method and is not cTTO plus DCE;
- a crosswalk is a mapping product and is not a native hybrid value set.

The protocol family includes the exact protocol name, version, and local variant. It includes EQ-VT version 1.1, EQ-VT version 2.1, the EQ-VT 2.1 lite protocol, the EQ-5D-Y-3L International Valuation Protocol, and study-specific modifications. A method can be used without a reported protocol version.

### 4.4 Statistical model family and exact specification

Broad families support recall, but the exact specification supports comparison. Supported families include:

- conditional logit;
- mixed logit;
- Zermelo-Bradley-Terry;
- random-intercept generalized least squares;
- random-effects or random-intercept Tobit;
- heteroscedastic regression;
- heteroscedastic Tobit censored at minus one;
- hybrid cTTO and DCE models;
- hybrid heteroscedastic Tobit;
- heteroscedastic censored hybrid;
- ADD20, ADD20-I, ADD20-P, CALE, CALE-I, and CALE-P;
- Bayesian heteroscedastic Tobit;
- linear, power, and power-without-constant mapping;
- ANOVA, regression, quantile regression, random-intercept longitudinal models, and meta-regression;
- random-effects evidence synthesis.

Model attributes include intercept handling, censoring point, heteroscedasticity, random effects, interaction terms, time-preference form, scale parameter, link function, and selected-model status. The exact source label remains attached.

### 4.5 Measurement-property and finding families

Controlled Outcome Definition families include:

- feasibility and completion;
- ceiling and floor effects;
- distribution and informativity;
- test-retest reliability;
- convergent validity;
- known-groups or discriminant validity;
- responsiveness;
- content validity, relevance, understanding, and comprehensiveness;
- preference value, dimension importance, and worse-than-dead proportion;
- model fit, prediction, and logical consistency;
- health-status, utility, EQ VAS, and wellbeing outcomes;
- change classification, including PCHC;
- cost, QALY, and ICER outcomes;
- implementation feasibility and acceptability;
- survey quality, bot, speeding, duplicate, missingness, and quota outcomes.

Finding direction is controlled only when the comparison is explicit. Values include favours first comparator, favours second comparator, no clear difference, mixed, supports feasibility, identifies limitation, and proposes future work. The full finding text remains available.

### 4.6 Product classification

Research Product types include:

- native value set;
- crosswalk value set;
- mapping function;
- scoring rule or coefficient table;
- instrument version or form;
- translation or language adaptation;
- dataset;
- survey protocol;
- taxonomy or selection criteria;
- implementation programme, display, training, or decision-support tool.

Planned output and produced output are different statuses. S061 can link EQ-TIPS to a planned future preference-weighted score and to an explicit “not produced in this study” assertion. It must not link S061 to a produced EQ-TIPS value set.

### 4.7 Term and identifier management

Each controlled concept has a preferred label, source labels, aliases, definition, scheme version, and broader or narrower concepts when useful. Examples include:

- preferred label cTTO; source labels “composite Time Trade Off” and “composite time trade-off”;
- preferred label value set; alias tariff;
- preferred label EQ VAS; source labels “EQ-VAS” and “visual analog scale” where the source identifies the EuroQol scale;
- separate canonical concepts for anxiety/depression and worried, sad, or unhappy because they belong to different instrument versions.

DOIs identify Publications. ORCID and ROR can identify people and organizations after verification. ISO language and country codes can normalize language and geography. A SKOS-like label pattern can manage preferred and alternative terms. A PROV-like pattern can manage source, extraction, and derivation. These are limited alignments. They do not control the domain design.

## 5. Important relations

| From | Relation | To | Important qualifiers |
|---|---|---|---|
| Publication | reports | Study | report role and source |
| Publication | has authorship | Authorship | order and corresponding role |
| Authorship | identifies author | Person | identity confidence |
| Study | is supported by | Funded Project | through Project-Output Link evidence |
| Project-Output Link | links project output | Publication and Funded Project | accepted, candidate, rejected, evidence, reviewer, date |
| Person | participates in | Funded Project | PI or other role and dates |
| Person | affiliated with | Organization | through dated Affiliation Episode |
| Person | holds membership in | EuroQol or Working Group | role and dates |
| Study | has target population | Population Definition | intended scope |
| Study | has sample | Sample | sample stage and count type |
| Sample | is derived from | Sample | exclusion, split, follow-up, or stable subset |
| Study | takes place in | Place | site-country role |
| Study | performs | Study Activity | dates and sequence |
| Administration Event | administers | Instrument Form | mode, language, reporter, recall, and timepoint |
| Study | develops, evaluates, values, compares, or implements | Instrument Version | explicit instrument role |
| Instrument Version | belongs to | Instrument Family | version identity |
| Instrument Version | contains | Dimension and Response Level | order and wording |
| Language Adaptation | adapts | Instrument Version | language, locale, process, and status |
| Bolt-On Specification | extends | Instrument Version | added dimension and development status |
| Valuation Study | follows | Valuation Protocol | exact version |
| Valuation Study | elicits preferences with | Elicitation Task | perspective, duration, health-state design |
| Statistical Analysis | analyses | Dataset | sample, task, and observation count |
| Statistical Analysis | fits | Statistical Model | exact specification |
| Model Selection Decision | selects | Statistical Model | alternatives and criteria |
| Study | produces | Research Product | product status |
| Value Set | scores states from | Instrument Version | scale and anchor |
| Value Set | represents preferences of | Population Definition | country and preference source |
| Value Set | is estimated from | Elicitation Task, Dataset, and Statistical Model | complete method chain |
| Crosswalk Value Set | maps from and maps to | Named systems or value sets | algorithm and development population |
| Estimate | quantifies | Outcome Definition | sample, instrument, time, unit, uncertainty |
| Finding | interprets | Estimate, Comparison, or qualitative evidence | scope and source |
| Finding | is limited by | Limitation | source-stated only |
| Publication | cites | Publication | source and retrieval date |
| Publication | receives topic assignment | Topic | scheme, score, and date |
| Derived Analytic | is computed from | Versioned input set | rule, date, and missing-data policy |

An Instrument Version and a Country can have high degree because many studies use them. These are valid domain hubs. Queries should start from a bounded Study, Publication, Project, or Sample and use the role-specific relations. An Administration Event and a Project-Output Link also prevent one overloaded edge from carrying many unrelated qualifiers.

## 6. Representation of required research detail

### 6.1 Populations and samples

A population description is built from explicit facets:

- geography and the role of that geography;
- age limits, age groups, or life stage;
- condition and diagnostic basis;
- general population, patient, caregiver, expert, stakeholder, or professional role;
- reporter role and preference-source role;
- recruitment frame and sampling method;
- language ability and other eligibility criteria.

The facets remain optional. The system must not create an age limit, diagnosis, or national-representativeness claim when the source does not state it.

Sample derivation records all reported denominators. For S023, target sample 1,200, conducted interviews 1,052, and analysed interviews 1,014 are different Sample facts. For S090, baseline sample 117 and retest sample 110 are different cohorts. For S063, the 52 second administrations and the 46 stable children used for reliability are also different cohorts.

### 6.2 Instruments

The ontology represents the instrument at the version, form, language, and administration levels. It can therefore distinguish:

- EQ-5D-5L from EQ-5D-3L;
- EQ-5D-Y-5L from adult EQ-5D-5L;
- EQ-TIPS V2.0 or EQ-TIPS-3L from a five-level version not available in S061;
- EQ-HWB, EQ-HWB-S, and EQ-HWB-9;
- self-report from proxy version 1 or proxy version 2;
- Australian English, UAE Arabic, UK English, Bahasa Indonesia, isiXhosa, and Simplified Chinese forms;
- use as a measure from development or valuation of the measure.

Dimensions and response levels belong to the exact version. This avoids a false merge of adult anxiety/depression with the youth wording worried, sad, or unhappy.

### 6.3 Methods and valuation

A valuation record follows a traceable chain:

Valuation Study → target Instrument Version → Valuation Protocol and version → Elicitation Task → perspective and preference source → health-state design → sample and observations → quality-control rules → Statistical Analysis → candidate models → selected model → Value Set.

Each link can be absent when it is not reported. For example, S023 reports EQ-VT 2.1 but does not report the EQ-5D-5L interview language. The language field stays unasserted.

The model distinguishes cTTO task details from the later statistical model. It also records whether DCE excludes duration, includes duration, compares with death, or uses a split-triplet design.

### 6.4 Analyses and exact models

An Analysis has a purpose, input dataset, model, transformations, comparison set, and output estimates. Model selection is a separate decision. This permits questions such as:

- Which studies fitted both cTTO-only and hybrid models?
- Which selected models handled censoring at minus one?
- Which DCE-with-duration analyses used nonlinear time preference?
- Which value sets used interaction terms?

The exact selected model remains visible. The ontology must not reduce the S023 model to “regression” or the S018 model to “hybrid.”

### 6.5 Products

A study can produce no product, one product, or several products. A publication can report a product that was created by a larger project. The ontology separates:

- a value set from the study that estimated it;
- a value set from the publication that reports it;
- a scoring formula from the value-set identity;
- a direct value set from a crosswalk;
- a released product from a planned product;
- a dataset from an article that describes the dataset;
- an implementation programme from the instrument that it implements.

Product lineage makes Q54 possible. It can show that a native EQ-5D-5L value set uses direct preference evidence for EQ-5D-5L states. A crosswalk instead derives 5L scores through another system or value set. S024 supplies comparative evidence that the two product types are not interchangeable.

### 6.6 Outcomes, estimates, and findings

An Outcome Definition specifies:

- the construct;
- the metric;
- its direction;
- its unit;
- its threshold or interpretation rule when the study states one;
- the instrument, dimension, or score to which it applies.

An Estimate adds the sample, timepoint, comparator, value, uncertainty, and analysis. A Finding adds the authors’ interpretation. A Limitation bounds that interpretation.

This model supports both quantitative and qualitative evidence. A qualitative theme can be a Finding with a participant group and analysis method. It does not need a numerical Estimate.

## 7. Publication, study, project, link, and analytic separation

| Record | What it answers | What it must not imply |
|---|---|---|
| Publication | What public document exists and what does it report? | One publication is not necessarily one study or one project. |
| Study | What investigation was done, in which samples, with which methods? | A study is not an administrative grant. |
| Funded Project | What work did an award authorize, fund, and schedule? | A project ID in a summary does not prove project status, budget, or all outputs. |
| Project-Output Link | Why is one publication treated as one project’s output? | A date window alone does not prove production. |
| Derived Analytic | What did the system calculate across records? | The result is not a source-paper finding and is not timeless. |

A Derived Analytic must state:

- metric definition and version;
- input record set and snapshot date;
- scope, such as accepted project-output links only;
- time window;
- handling of missing values, ties, and duplicate identities;
- formula or procedure in plain language;
- result and calculation date.

This is necessary for project counts, approved-budget totals, publication counts, citation rankings, median publication lag, link-window fractions, top-decile concentration, topic growth, topical similarity, ORCID coverage, country participation, and the projects-to-citations funnel.

## 8. Support for all supplied competency questions

The categories in the table mean:

- **Answerable from supplied summaries**: the 50 summaries contain the needed facts for a packet-scoped answer. A global claim is not permitted.
- **Requires external linked data**: the ontology supports the question, but a registry, citation source, identity source, membership source, access-status source, or complete corpus must be linked.
- **Unsupported by available evidence**: a required query input or evidence base is absent, so the current data cannot support an answer.

| ID | Required concepts and relations | Answerability category and reason |
|---|---|---|
| Q63 | Country universe; EQ-5D-5L; Native Value Set; targets country; publication status; as-of date | **Requires external linked data.** The summaries give examples, not a complete current country inventory or its complement. |
| Q1 | Funded Project; approved budget and currency; award status; unique project count; currency policy; Derived Analytic | **Requires external linked data.** Project budgets and the complete project register are absent. |
| Q57 | Funded Project; valuation-study classification; exact Valuation Method; project-method relation; frequency analytic | **Requires external linked data.** Paper methods are present, but the complete funded-project portfolio is not. |
| Q37 | Publication; Study; valuation-study classification; DCE exact method; target Country; values Instrument Version | **Answerable from supplied summaries.** The answer must remain scoped to the 50 summaries and must separate DCE variants. |
| Q61 | Instrument Version; development milestone; produced, launched, experimental, translated, or evaluated status; event date; Publication | **Answerable from supplied summaries.** The result is a corpus-reflected timeline, not a complete EuroQol history. |
| Q78 | Person; Authorship; Membership Episode at publication date; co-author pair; identity resolution; frequency analytic | **Requires external linked data.** Full author lists, resolved people, and dated membership are not supplied for all papers. |
| Q85 | Funded Publication; Citation Link; OpenAlex Topic or Field Assignment; citing publication; count analytic and snapshot | **Requires external linked data.** OpenAlex citation and topic data are absent. |
| Q96 | Publication; Bolt-On Specification; base Instrument Version; added Dimension; Study classification; one-line Finding | **Answerable from supplied summaries.** S084, S087, S094, and other explicit bolt-on evidence can be retrieved within packet scope. |
| Q91 | Funded Project; completion date; accepted Project-Output Link; Publication; citation count; “highly cited” rule; last-three-years window | **Requires external linked data.** Project completion and citation snapshots are absent. |
| Q80 | Project-Output Link; Publication; Citation Link; source and target Funded Project; accepted-link status | **Requires external linked data.** Reference lists and a complete project-output graph are absent. |
| Q87 | Source person profile; canonical Person; Identity-Resolution Decision; merge, override, or skip action; reason and audit date | **Requires external linked data.** Identity-resolution audit logs are not paper facts. |
| Q29 | Country; published Native Value Set for EQ-5D-5L; publication date; product status; current inventory | **Requires external linked data.** The summaries name some value sets but do not list all countries. |
| Q2 | Funded Project; award or start year; funded status; project count by year; date coverage since 2012 | **Requires external linked data.** A complete dated project register is absent. |
| Q48 | Funded Project; ongoing status and as-of date; target Instrument Version; project objective or abstract assertion | **Requires external linked data.** Current project status and complete project aims are absent. |
| Q18 | Proposal Abstract; project abstracts; Topic Assignment or semantic representation; similarity method and score; past-project status | **Unsupported by available evidence.** No proposal abstract is supplied, and no complete project-abstract set is present. |
| Q44 | Person parameter; Publication and Project Participation; Working-Group Participation; topic or instrument span; dates | **Requires external linked data.** Dated working-group membership and a resolved person record are absent. |
| Q19 | Cognition Bolt-On Specification; base Instrument Version; Funded Project; project status; project aims; related Publication | **Requires external linked data.** S084 supplies published cognition bolt-on work, but portfolio coverage and ongoing status need project data. |
| Q33 | Study; same Sample or source population; EQ-5D-3L Value Set; EQ-5D-5L Value Set; comparison relation; Publication | **Answerable from supplied summaries.** The model must distinguish same respondents from only the same country. |
| Q42 | Publication; Study; DCE with duration or DCEd; duration model; anchoring; target Instrument Version; Finding | **Answerable from supplied summaries.** S011, S019, S020, and related method evidence support a packet-scoped synthesis. |
| Q11 | Funded Project; approved amount; recipient Organization; organization Country; project role; currency conversion rule; aggregate | **Requires external linked data.** Award amounts and recipient records are absent. |
| Q8 | Funded Project; accepted Project-Output Link; unique Publication; count and tie rule | **Requires external linked data.** The summaries do not give a complete output set for each project. |
| Q31 | Person; current Project Participation; ongoing project status; EQ-HWB target; role; as-of date | **Requires external linked data.** Current project staff and status are absent. |
| Q45 | Valuation Study; EQ-5D-5L target; analysed Sample size; protocol type; country; distribution summary | **Answerable from supplied summaries.** “Typical” must be defined and reported only for the supplied valuation studies. |
| Q98 | DOI-identified Publication; Funded Project; Project-Output Link; supporting Evidence Assertion; link status | **Answerable from supplied summaries** when DOI X is one of the 50 supplied publications. An arbitrary DOI needs external data. |
| Q49 | Study; EQ-5D-Y Instrument Version; test-retest Outcome Definition; retest Sample; interval; reliability method; Publication | **Answerable from supplied summaries.** S059 and S096 contain direct evidence, with different versions and cohorts. |
| Q59 | Publication; EQ-HWB introduction or development classification; Access Status; licence or route; as-of date | **Requires external linked data.** The summaries do not provide systematic open-access status. |
| Q23 | completed Funded Project; abstract promise assertion; promised Value Set; accepted output links; published product; closed-world audit rule | **Requires external linked data.** Project abstracts, completion status, and complete output links are absent. |
| Q75 | Project-Output Link; accepted status; publication date; project start and end; year offset; numerator, denominator, and window analytic | **Requires external linked data.** Link decisions and project periods are absent. |
| Q7 | Funded Project; start date; accepted linked Publication dates; first-output rule; duration; median analytic | **Requires external linked data.** Complete link and project-date data are absent. |
| Q74 | canonical Person; first Authorship date in the complete corpus; identity-resolution version; last-three-years window | **Requires external linked data.** Full authorship and identity history are absent. |
| Q60 | Publication; date; Topic Assignment under a fixed scheme; yearly counts; growth rule; corpus snapshot | **Requires external linked data.** A selected 50-paper packet cannot support a corpus activity trend. |
| Q26 | Proposal target Condition and Instrument Version; past Project; project aims; shared-condition and shared-instrument match | **Unsupported by available evidence.** The proposal and a complete project-aim set are not supplied. |
| Q17 | Applicant Person; prior Project Participation; previous grants; accepted Project-Output Links; Publications | **Requires external linked data.** Applicant identity, grant roles, and complete links are absent. |
| Q46 | canonical 1997 UK MVH Publication; Citation Link; citing corpus Publication; reference evidence | **Requires external linked data.** Reference lists and citation links are absent from the summaries. |
| Q22 | Applicant Person; previous Funded Project; project date; first accepted linked Publication date; elapsed time | **Requires external linked data.** Applicant, project dates, and complete links are absent. |
| Q38 | Person parameter; Authorship; co-author Person; canonical publication set; pair counts and identity resolution | **Requires external linked data.** Full author lists and resolved identities are absent. |
| Q77 | PI role; Funded Project; accepted outputs; output count by PI; top-decile definition; concentration share | **Requires external linked data.** PI assignments and complete output links are absent. |
| Q47 | Person parameter; co-authorship; Membership Episode at relevant date; funded-output link; Publication | **Requires external linked data.** Dated membership and complete authorship are absent. |
| Q97 | Person; funded Publication; Affiliation Episode; Country; participation rule; distinct-country count | **Requires external linked data.** Complete author affiliations are absent. |
| Q51 | Publication; Study; EQ-TIPS Instrument Version; development, translation, psychometric, or valuation role; Finding | **Answerable from supplied summaries.** S061 and S063 support a packet-scoped account and show different study roles. |
| Q54 | Native Value Set; Crosswalk Value Set; direct valuation evidence; mapping lineage; target Instrument Version; key Publication | **Answerable from supplied summaries.** S018, S024, and S073 give definitions, comparisons, and DOI-identified references. |
| Q12 | Funded Publication; citation count and source; snapshot date; accepted Project-Output Link; maximum rule | **Requires external linked data.** Citation counts are absent. |
| Q92 | unique Funded Projects; projects with accepted outputs; unique output Publications; citation totals; funnel definitions and snapshot | **Requires external linked data.** A full project, link, and citation dataset is absent. |
| Q99 | Authorship; Membership Episode; corpus inclusion or exclusion decision; pure-application classification; share and denominator | **Requires external linked data.** Membership and corpus-screening decisions are absent. |
| Q62 | Organization parameter; Affiliation Episode; Person; EQ Topic Assignment or relevant Study; date | **Requires external linked data.** Current and historical affiliation data are absent. |
| Q52 | EQ-HWB Instrument Version; Language Adaptation; target language and locale; adaptation process; reporting Publication; publication status | **Requires external linked data.** S078 shows use of Simplified Chinese EQ-HWB v1.1, but the packet is not a complete translation bibliography. |
| Q20 | Proposal aims; ongoing Funded Project; current status; project objectives; overlap dimensions and method | **Unsupported by available evidence.** The proposal and current project portfolio are not supplied. |
| Q81 | canonical Person; resolved-profile population; verified ORCID identifier; resolution version; numerator and denominator | **Requires external linked data.** ORCID and resolved-person data are absent. |
| Q58 | Publication; EQ-5D-Y-5L Instrument Version; study role; population; product and main Finding | **Answerable from supplied summaries.** S059, S057, and S096 support a packet-scoped account; “all published work worldwide” would need external data. |
| Q30 | Value Set; EQ-VT Valuation Protocol; exact version or lite variant; target country; Publication; protocol-not-reported state | **Answerable from supplied summaries.** S023, S018, S028, and S004 contain direct value-set evidence with reported protocol detail. |

## 9. Complete example records

These examples use only facts in the supplied summaries. They show the proposed record structure. They do not fill fields that the summaries do not report.

### 9.1 Example A: Danish EQ-5D-5L value set

**Source and publication**

- Source Summary: S023, verified packet summary.
- Publication: “The Danish EQ-5D-5L Value Set: A Hybrid Model Using cTTO and DCE Data.”
- DOI: 10.1007/s40258-021-00639-3.
- Publication date: 2 February 2021.
- Publication type: national EQ-5D-5L valuation and value-set report.

**Project and link evidence**

- Funded Project identifier: 20170401.
- The summary reports EuroQol Research Foundation project 20170401 among the funding sources.
- The Project-Output Link is supported by the reported project identifier and funding statement.
- Project start, end, status, approved budget, and PI are not reported in S023.

**Study**

- Classifications: valuation study; national value-set development.
- Target product: the first Danish EQ-5D-5L value set for QALYs and hospital-medicine priority setting.
- Target population: Danish adults.
- Sampling aim: national representation by age, gender, education, and region with Statistics Denmark data.
- Target Sample count: 1,200.
- Conducted-interview Sample count: 1,052.
- Analysed Sample count: 1,014.
- Data-collection period: October 2018 to November 2019.
- The sample underrepresented people aged 18–24 and the lowest education level.

**Instrument, protocol, and tasks**

- Instrument Version valued: EQ-5D-5L.
- Protocol: EQ-VT version 2.1.
- Administration: computer-assisted personal interview.
- Each respondent completed self-reported EQ-5D-5L, EQ VAS, ten cTTO tasks, feedback and debriefing, and seven DCE pairs.
- cTTO contained conventional TTO for better-than-dead states and lead-time TTO for worse-than-dead states.
- DCE compared two non-dominant EQ-5D-5L states without duration.
- The cTTO design contained 86 states.
- The DCE design contained 196 pairs in 28 blocks of seven.
- The EQ-5D-5L interview language is not reported. A Danish translation of training material is reported. The ontology does not infer the interview language.

**Analysis and model selection**

- Candidate cTTO models: generalized least-squares random-intercept and random-effects Tobit.
- Candidate DCE model: conditional logit, with a heteroscedastic robustness model.
- Candidate hybrid models combined cTTO and DCE with a multiplicative scale parameter.
- Selected Statistical Model source term: “heteroscedastic censored hybrid model.”
- Model-selection reasons: it removed logical inconsistencies; the source also considered logical consistency and goodness of fit.

**Product**

- Product type: Native Value Set.
- Canonical label: Danish EQ-5D-5L value set.
- Instrument Version: EQ-5D-5L.
- Target country: Denmark.
- Preference source: adult population sample.
- Inputs: cTTO and DCE observations.
- Anchor: full health 1 and dead 0, with negative values for states worse than dead.
- State range: 11111 equals 1; 55555 equals minus 0.757.
- Coverage: values for all 3,125 EQ-5D-5L states.
- Example scoring fact from the source: state 13224 equals 0.439.

**Estimates and findings**

- Estimate: 22% of valued states were worse than dead in the cTTO data.
- Finding: the selected hybrid removed logical inconsistencies, although some adjacent increments were not statistically different.
- Finding: anxiety/depression had the largest dimension decrement in the preferred model, followed by pain/discomfort, mobility, self-care, and usual activities.
- Comparison Finding: the Danish 5L value set had a lower 55555 value than the Danish 3L and crosswalk sets.
- Limitation: the source reports underrepresentation, long interviews, mixed recruitment sources, and unresolved questions about combining TTO and DCE.

### 9.2 Example B: EQ-TIPS content and instrument development

**Source and publication**

- Source Summary: S061, verified packet summary.
- Publication: “Developing the EuroQol toddler and infant populations (EQ-TIPS) instrument: qualitative analysis of expert views on content validity and conceptual challenges.”
- DOI: 10.1007/s11136-025-04150-3.
- Project identifier: 365-RA.
- Publication type: qualitative peer-reviewed research article.

**Study**

- Classifications: instrument development; qualitative content-validity study; expert consultation.
- Aim: review wording and content of EQ-TIPS V2.0 and examine uses and development challenges.
- Study Activity: three online semi-structured focus-group consultations on Zoom.
- Activity dates: December 2022 to February 2023.
- Invited Sample count: 44 experts.
- Non-attending count: 11.
- Participant Sample count: 33.
- Group counts: EuroQol expert group 17, paediatric health and development expert group 11, and paediatric HRQoL instrument developer group 5.
- Geographic coverage: 15 countries represented.
- Recruitment method: purposive selection for expertise, experience, and geographic spread.

**Instrument**

- Instrument Family: EQ-TIPS.
- Instrument Version source designations: EQ-TIPS V2.0 and experimental EQ-TIPS-3L.
- Target life stage: infants and toddlers, with proposed range 0–3 years.
- Dimensions: Movement, Play, Social Interaction, Communication, Eating, and Pain.
- Response levels: no, some, and a lot of problems.
- EQ-TIPS Visual Analogue Scale: proxy rating of the child’s overall health from 0 to 100.
- Status: experimental.
- The five-level version was not available for testing in this study.

**Method and findings**

- Materials: instrument, short video, and preparatory reading.
- Qualitative Analysis: Braun and Clarke six-phase thematic analysis.
- Software: NVivo version 14.
- Coding: mainly deductive, with inductive themes and sub-themes permitted.
- Finding: most experts found the measure short and easy to complete.
- Finding: experts asked for a clearer construct definition and child-health focus.
- Finding: most experts gave priority to age-relevant content rather than direct mapping to EQ-5D-Y and EQ-5D dimensions.
- Finding: Sleep was widely proposed as an additional dimension; Emotions was also proposed; bowel habits had little support.
- Finding: examples of observable behaviour were preferred to “age-appropriate behaviour.”
- Finding: the best proxy depends on the study context.

**Explicit negative and future-status assertions**

- The study did not test caregivers or children directly.
- It did not test EQ-TIPS V5.0.
- It did not produce psychometric evidence.
- It did not produce preference evidence or a value set.
- Preference-weighted scores and value sets were planned for future work.

These negative assertions are sourced facts. They are not inferred from empty product fields.

### 9.3 Example C: preference testing of EQ-5D-5L bolt-ons

**Source and publication**

- Source Summary: S084, verified packet summary.
- Publication: “Selecting Bolt-on Dimensions for the EQ-5D: Testing the Impact of Hearing, Sleep, Cognition, Energy, and Relationships on Preferences Using Pairwise Choices.”
- DOI: 10.1177/0272989X20969686.
- Project identifier: 20170210.
- Publication date: 30 November 2020.

**Study and sample**

- Classifications: bolt-on study; online pairwise-choice preference experiment.
- Country role: UK general-population sample.
- Data-collection period: May 2017.
- Included Sample count: 1,040, with 520 women and 520 men.
- Administration mode: online panel survey.

**Instrument extension records**

- Base Instrument Version: EQ-5D-5L.
- Candidate Bolt-On Specifications: Hearing, Sleep, Cognition, Energy, and Relationships.
- Tested levels: 1, 3, and 5.
- Three base EQ-5D-5L health-state pairs were used.
- Survey design: 48 pairwise questions across six randomized blocks; each respondent completed eight choices.

**Analysis, estimates, and findings**

- Statistical Analysis: logistic regression with clustered sandwich estimators.
- Outcome Definition: marginal effect of a bolt-on on the choice of the state to which it was added.
- Overall Estimates: Hearing minus 0.16, Cognition minus 0.15, Relationships minus 0.12, Sleep minus 0.09, and Energy minus 0.08.
- Level-3 Finding: Cognition had the largest overall effect.
- Level-5 Finding: Hearing had the largest overall effect.
- Finding: the rank of bolt-ons changed with severity.
- Finding: adding a bolt-on requires revaluation of the extended tariff.
- Limitation: the study used only three base health-state pairs and did not test levels 2 and 4.
- Product status: the study did not report a new extended value set.

This record shows why Bolt-On Specification, tested severity, base state, Estimate, and Finding must remain separate.

## 10. Free text, derived facts, optional facts, and exclusions

### 10.1 Facts that should remain available as free text

The following information can have controlled tags, but the full source text remains important:

- nuanced qualitative themes and participant reasons;
- limitations and cautions;
- recommendations and future-research proposals;
- explanations for unexpected findings;
- exact value-set formulas when a complete structured coefficient representation is not available;
- complex eligibility, sampling, and quality-control narratives;
- interpretation of normative issues, such as child versus adult perspective;
- source-reported conflicts and unclear denominators.

Free text does not replace structured facts. It complements them.

### 10.2 Derived analytics

The system can derive:

- counts and budgets by year or country;
- publication counts per project;
- citation counts and rankings;
- time from project start to first output;
- project-output link-window fractions;
- co-author frequency and network concentration;
- share of outputs held by the top PI decile;
- topic growth;
- semantic similarity between a proposal and past projects;
- the project-to-output-to-citation funnel;
- ORCID coverage;
- participating-country counts;
- shares of corpus inclusion or exclusion classes.

Each analytic must be reproducible and dated. A source-paper statistic remains an Estimate, not a Derived Analytic of the research system.

### 10.3 Optional but useful facts

Optional facts include:

- software and version;
- ethics approval and registration;
- conflict-of-interest statement;
- funding organization and grant statement;
- interviewer training;
- quality-control thresholds;
- access and licence status;
- supporting code or online-resource availability;
- journal, issue, and page data;
- source quotations where permissions allow them.

These facts become mandatory only for a use case that needs them.

### 10.4 Outside the initial scope

The initial ontology does not represent:

- participant-level responses or clinical records;
- unpublished patient data;
- full bibliographic reference lists unless they are linked as Citation records;
- causal clinical claims that the source does not make;
- a global current value-set inventory without an external dated source;
- confidential award review, applicant, or budget records unless an authorized project system supplies them;
- full statistical code or software implementation.

## 11. Quality rules

1. A Publication DOI is unique after DOI normalization.
2. A project identifier is unique only within its project-registry namespace.
3. A Source Summary identifier and hash identify the fixed input used for extraction.
4. A Value Set cannot exist without one exact target Instrument Version.
5. A Crosswalk Value Set must identify both ends of the mapping.
6. An Estimate cannot exist without an Outcome Definition and evidence source.
7. A sample count must have a count type and, when known, a denominator scope.
8. A country relation must state its geographic role.
9. A project-output claim must use a Project-Output Link with evidence and status.
10. A system-derived metric must have a method version, input snapshot, and calculation date.
11. A source conflict must preserve all conflicting assertions.
12. “Not reported,” “not produced,” “planned,” and “no evidence found under a stated closed-world search” are different statuses.
13. Instrument use, evaluation, development, valuation, and scoring are different relations.
14. cTTO, DCE without duration, DCEd, DCE-death, and a hybrid model are different concepts.
15. No classification can replace the source term from which it was assigned.

## 12. Unresolved design choices and risks

### 12.1 Definition of native value set

The system needs an agreed operational definition. “Native” can mean a local preference sample, a direct valuation of the target descriptive system, or both. The definition must state how multinational samples, residents, nationals, expatriates, and imported protocol components are handled.

### 12.2 Study and sub-study boundaries

Some publications report several surveys, samples, waves, or models. S015 synthesizes three prior online DCE datasets. S019 compares two Trinidad and Tobago samples. A curator rule is needed for when these become separate Studies, Study Activities, or Samples.

### 12.3 Project-output link authority

A project ID in a summary, a funding statement, and an administrative output record provide different evidence strengths. The ontology can store them, but governance must define acceptance rules and reviewer authority.

### 12.4 Instrument version identity

Experimental names can change. A version registry must prevent accidental merge of a working title, a response-level count, and a formal release. Status needs an as-of date.

### 12.5 Method name overlap

“Hybrid,” “mapping,” “anchoring,” and “DCE” are easy to over-normalize. The source term, exact method, protocol, and model must remain separate. In particular, DCE with duration must not be retrieved only through the broad DCE label when the duration feature is material.

### 12.6 Negative evidence

Questions about countries without a value set or projects with no output need a closed and dated reference set. Absence of a relation in an open research graph is not evidence of nonexistence.

### 12.7 Time-dependent people and organizations

Membership, affiliation, working-group role, project status, ORCID coverage, citations, topics, and open-access status can change. Undated current-state properties will produce incorrect historical queries.

### 12.8 Identity-resolution error

Co-author, applicant, PI, and member analytics depend on person resolution. Every merge, split, override, and skip must be auditable. Derived network metrics must cite the identity-resolution version.

### 12.9 Selected-corpus bias

The 50 summaries are suitable for ontology design. They are not suitable for estimates of global prevalence, publication trends, project success, or typical practice without a clear packet scope. The system must display the denominator and corpus snapshot for every aggregate.

### 12.10 Conflicting or incomplete summary detail

Some summaries explicitly report source discrepancies. Other summaries omit language, protocol version, access status, or full author affiliation. The model must accept partial records and conflicts without forced completion.

### 12.11 Controlled vocabulary governance

Canonical labels can drift as instruments and methods develop. Each scheme needs a version, change log, owner, and rules for deprecated labels. Source labels must remain searchable after a canonical change.

### 12.12 Performance and high-degree hubs

EQ-5D-5L and frequently used countries will be high-degree entities. This is expected. Query paths must use Study Instrument Role, Administration Event, Project-Output Link, and country-role relations. This reduces false matches and avoids broad traversals through an undifferentiated hub.

## 13. Acceptance test for the ontology

The ontology is ready for implementation only when a test dataset can:

1. reproduce all sourced facts in the three examples without invented values;
2. retain the exact source terms and source locations;
3. distinguish every valuation method, protocol version, and selected statistical model in the packet;
4. return packet-scoped answers for all questions marked answerable;
5. state the missing external dataset for every question marked external;
6. refuse to answer the three unsupported proposal-matching questions until their required proposal input is supplied;
7. preserve all source conflicts;
8. recompute every Derived Analytic from a named snapshot;
9. distinguish a publication that uses a value set from a study that creates one;
10. distinguish explicit “not produced” evidence from an empty product field.
