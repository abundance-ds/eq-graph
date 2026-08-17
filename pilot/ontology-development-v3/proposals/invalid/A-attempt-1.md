# EuroQol research ontology proposal

## 1. Evidence basis

This proposal uses 50 fixed paper summaries and 50 competency questions from input packet A. The input audit found 50 matching SHA-256 hashes and no mismatches. The proposal did not use the source papers. Thus, each example identifies its immediate evidence by summary ID.

The ontology supports research search, comparison, synthesis, portfolio analysis, and evidence audit. It gives priority to exact EuroQol research facts. It does not treat a title, a project identifier, or a keyword as a sufficient substitute for a study fact.

The scope includes:

- publications, studies, projects, awards, people, organizations, and working groups;
- populations, samples, settings, timepoints, and administration;
- instrument families, exact versions, localized forms, dimensions, response levels, bolt-ons, and health states;
- valuation studies, valuation protocols, elicitation methods, task designs, scales, statistical models, and value sets;
- other study purposes, such as measurement-property assessment, content validity, translation, feasibility, population norms, instrument development, and evidence synthesis;
- outcomes, estimates, findings, limitations, recommendations, and research products;
- citations, corpus decisions, identity resolution, topics, and derived portfolio or network analytics when linked data is available.

Participant-level observations, copyrighted full text, and executable scoring algorithms are outside the core ontology. The ontology can point to these resources when access and governance permit.

## 2. Design principles

### 2.1 Keep four layers separate

The ontology has four layers.

1. **Source evidence** records what a supplied summary states, where it states it, and which source spelling it uses.
2. **Canonical research facts** identify the publication, study, population, method, model, product, and finding that the statement concerns.
3. **Controlled classifications** assign exact canonical categories under a named and versioned scheme.
4. **Derived analytics** contain computed counts, shares, trends, similarities, rankings, and network measures. Each analytic result identifies its inputs and calculation date.

No layer replaces another. For example, the source strings “composite TTO”, “C-TTO”, and “c-TTO” can all map to the canonical term **composite time trade-off (cTTO)**. The original strings remain available. A curator classification that calls the study a **valuation study** remains separate from the source wording. A later count of valuation studies is a derived result.

### 2.2 Use exact typed concepts

Important facts do not sit only in broad fields named “method”, “component”, or “outcome”.

- **Valuation study** is an explicit study-purpose category.
- **Composite time trade-off (cTTO)** is an elicitation method.
- **Conventional TTO** and **lead-time TTO** are distinct method parts of cTTO.
- **Discrete choice experiment (DCE)**, **DCE with duration**, and **DCE-death** are distinct elicitation methods or task formats.
- **Hybrid model** is a statistical model that combines evidence from more than one elicitation source. It is not an elicitation method.
- **Hybrid heteroskedastic Tobit model censored at −1** is an exact model specification, not only “hybrid”.
- **EQ-5D-5L** is an instrument version, not only an instrument keyword.
- **Value set**, **crosswalk**, and **mapping function** are different research products.

### 2.3 Preserve an open world

No recorded fact means “not reported”, not “no”. A value set without a recorded EuroQol award is not a value set produced without EuroQol funding. A negative answer needs one of these forms of evidence:

- an explicit negative source statement;
- a complete and dated external register that permits the negative conclusion;
- a derived result with a documented completeness rule.

Unknown, not applicable, conflicting, planned, and not yet measured are distinct states. A study protocol has planned analyses and hypotheses. It does not have completed findings unless a later source supplies them.

### 2.4 Do not force one study pattern

A publication can report one study, several studies, a protocol, a systematic review, a theoretical comparison, or a methodological argument. A study can use several samples, instruments, methods, and models. A product can arise from several analyses. A publication can link to more than one project. The ontology therefore uses qualified links where the connection has a role, date, basis, or provenance.

## 3. Core concepts

### 3.1 Evidence and terminology concepts

| Concept | Meaning and minimum useful content |
|---|---|
| **Summary document** | The immediate evidence object. It has a summary ID, title, file hash, paper identifier, and source location. |
| **Source assertion** | One proposition reported by a summary. It records the summary section, the reported wording, the assertion status, and any stated uncertainty or conflict. |
| **Source term occurrence** | An exact word or phrase in the source evidence, including spelling, capitalization, abbreviation, and language. |
| **Canonical concept** | The stable research meaning to which one or more source terms map. It has a preferred label, definition, aliases, and concept-scheme version. |
| **Classification assignment** | A qualified decision that assigns a study, method, product, finding, or other entity to a controlled category. It records whether the source stated the category or a curator assigned it. |
| **Metadata-quality flag** | A dated flag for a source or canonical record. Examples include conflicting values, a missing abstract, a truncated author list, or an unresolved identifier. The flag includes evidence and resolution status. |

Each canonical fact must point to at least one source assertion, an external linked record, or a derivation record. A fact can have more than one supporting assertion. Conflicting assertions remain separate. For example, summary S004 reports two different mean ages in the abstract and Results. The ontology keeps both values with their locations and adds a conflict flag. It does not silently select one.

### 3.2 Research lifecycle concepts

| Concept | Meaning and useful detail |
|---|---|
| **Publication** | A dissemination object, such as a journal article or protocol paper. Identity uses DOI when available. Title, journal, publication date, open-access status, and bibliographic metadata belong here. |
| **Study** | The research activity or analysis that has an aim, design, population, data, methods, and findings. A publication reports a study; it is not the study itself. |
| **Project** | An administrative research activity with a project identifier, title, dates, status, project type, people, organizations, and possible working-group ownership. A suffix in an identifier does not prove the project type. |
| **Award** | A funding decision with funder, approved amount, currency, award date, recipient, and conditions. An award funds a project. This is the required evidence for a “funded project” classification unless the source gives an equivalent explicit statement. |
| **Research product** | A typed output with its own identity and version. The type is mandatory. Supported types include value set, crosswalk, mapping function, localized instrument form, conceptual framework, study protocol, population-norm set, and quality-control framework. |
| **Working group** | A named organizational group that manages, sponsors, reviews, or is associated with projects or products. The exact role and dates are required. |
| **Researcher** | A resolved person identity. It has name variants and optional external identifiers. A name string alone is not a resolved researcher. |
| **Organization** | An institution, funder, journal publisher, care provider, panel provider, or other named body. Its role is stated on each link. |
| **Authorship** | A qualified publication-to-researcher link with author order and, when known, corresponding-author status and source name string. |
| **Affiliation** | A qualified researcher-to-organization link with publication or date context and organization country. It is not a permanent property of the researcher. |
| **Project role** | A researcher or organization role in a project, such as applicant, principal investigator, collaborator, host, or funder. It has dates and evidence. |
| **Project-output link** | A qualified assertion that a publication or product is an output of a project. It records the link basis, source, verification status, and link date. |
| **Citation** | A directed publication-to-publication reference. It has a source, date of ingestion, and match quality. |
| **Corpus decision** | A versioned inclusion or exclusion decision for a publication, with reason such as “pure application” when the corpus policy defines that term. |
| **Identity-resolution decision** | A merge, override, skip, or split decision for person profiles. It records candidate profiles, rule, evidence, actor, time, and reason. |

A reported project ID is a source fact. It is not, by itself, proof of an award, project type, working-group ownership, or output status. These are separate facts.

### 3.3 Study, population, and data concepts

| Concept | Meaning and useful detail |
|---|---|
| **Study aim** | A stated research objective or question. It remains distinct from a later finding. |
| **Study design profile** | A multi-axis classification of evidence stage, data origin, time structure, method family, and study purpose. |
| **Population specification** | The intended group. It combines role, age bounds, condition, geography, residence, language, and other eligibility criteria without turning the full description into one opaque string. |
| **Sample or cohort** | The recruited or observed people or records. It has a sample role, size, recruitment route, inclusion and exclusion rules, dates, and relationship to the target population. |
| **Analysis set** | The records or respondents used for one analysis after exclusions. It keeps the denominator and exclusion logic close to each result. |
| **Subgroup** | A defined part of a sample, such as people with a chronic condition, a country group, or an age band. |
| **Setting** | The care, community, registry, online-panel, laboratory, home, or other context in which research occurs. |
| **Place** | A country, region, city, or facility. Separate relations identify study location, target geography, recruitment geography, institution country, and product jurisdiction. |
| **Timepoint** | A named observation time, wave, baseline, follow-up, or recall anchor. It can carry an exact date, interval, or relative definition. |
| **Dataset** | A study data resource with data origin, coverage, collection period, access state, and relationship to samples and analyses. |
| **Administration** | The qualified event in which a specified instrument form is given to a sample at a timepoint. It records mode, respondent, perspective, language, platform, interviewer support, recall period, and setting. |

Target population, recruited sample, completed sample, final analysis set, and retest sample are not interchangeable. For example, summary S029 reports at least 1,000 targeted adults, 1,054 completed interviews, and separate final counts for cTTO and DCE observations. Each denominator belongs to a different concept.

### 3.4 Instrument and measurement concepts

| Concept | Meaning and useful detail |
|---|---|
| **Instrument family** | A stable family such as EQ-5D, EQ-5D-Y, EQ-HWB, or EQ-TIPS. |
| **Instrument version** | An exact form such as EQ-5D-3L, EQ-5D-5L, EQ-5D-Y-3L, EQ-5D-Y-5L, EQ-HWB, EQ-HWB-S, EQ-HWB-9, or experimental EQ-TIPS V2.0 / EQ-TIPS-3L. |
| **Localized form** | A language, country, respondent, or mode-specific form of an instrument version. Examples include the official Bahasa Indonesia EQ-5D-5L, Singapore English EQ-5D-Y forms, and Modern Standard Arabic EQ-5D-Y-5L. |
| **Instrument component** | A named part, such as the EQ-5D descriptive system or EQ VAS. A component type is required. |
| **Dimension** | A named construct in a specified instrument version. The link to the version prevents an adult “self-care” dimension from being treated as identical to a youth wording without review. |
| **Response level** | An ordered level with exact wording, ordinal position, language, and instrument version. |
| **Bolt-on dimension** | A dimension that extends a base instrument version. It records whether it is proposed, experimental, tested, or adopted. |
| **Health state** | A profile under one exact descriptive system. The same digit string under 3L and 5L is not the same state. |
| **Outcome definition** | The variable or construct that a study measures, such as EQ VAS, index value, ceiling effect, completion rate, construct validity, or responsiveness. |
| **Scoring system or value set use** | The qualified use of a named value set to score an instrument in a study. It identifies the value set, target version, jurisdiction, and sensitivity role. |

Comparator instruments such as WHOQOL-BREF, WHOQOL-OLD, SF-6Dv2, PROPr, MSIS-8D, WHODAS-12, POSAS, PHQ-9, GAD-7, and WHO-5 use the same instrument concepts. They remain outside EuroQol instrument families.

### 3.5 Valuation, task, and analysis concepts

| Concept | Meaning and useful detail |
|---|---|
| **Valuation exercise** | A study part that elicits preferences for described states. It links a sample, target instrument version, perspective, protocol, task design, elicitation method, scale, and resulting data. |
| **Valuation protocol version** | An exact protocol or software-supported procedure, such as EQ-VT 2.0 or EQ-VT 2.1. Protocol version is distinct from administration mode and software platform. |
| **Elicitation method** | A controlled exact method, such as cTTO, conventional TTO, lead-time TTO, DCE, DCE with duration, DCE-death, paired comparison, best–worst scaling case 2, standard gamble, or direct personal utility function elicitation. |
| **Task design** | The operational choice design. It includes blocks, task count, state design, duration, comparator, overlap, randomization, perspective, feedback module, and quality checks. |
| **Valuation perspective** | Who values whose health. It separates respondent population from target person, such as an adult valuing own health, an adult valuing a 10-year-old child, or a child using own perspective. |
| **Value scale and anchors** | The meaning of scores and anchors. Supported examples are a QALY scale with full health and dead, a latent DCE scale, a pits scale with 55555 and 11111 anchors, and an experience scale with coma and one week of full health. |
| **Analysis** | A defined analytic activity that uses one or more datasets and produces estimates. Its purpose and analysis family are explicit. |
| **Statistical model specification** | The exact model fitted in one analysis. It has a source label, base model family, modifiers, censoring rule, scale rule, error distribution, covariates, interactions, and tested or selected status. |
| **Model-selection decision** | The stated decision that selects a model for a product, with criteria and alternatives. |

The model specification can represent both a canonical family and an exact source form. Examples from the summaries include:

- Tobit cTTO model censored at −1;
- conditional-logit DCE model with rescaled coefficients;
- hybrid regression;
- hybrid heteroskedastic Tobit model censored at −1;
- heteroscedastic censored hybrid model;
- Bayesian hybrid model with random parameters, a generalized t-Student error, a Cauchy DCE distribution, religion scaling, and cTTO censoring at −1;
- mixed logit with nonlinear time preferences;
- heteroskedastic conditional logit;
- scale-adjusted latent class model;
- random-effects meta-analysis;
- multi-level meta-regression.

The ontology does not replace these specifications with the word “model”.

### 3.6 Product, result, and interpretation concepts

| Concept | Meaning and useful detail |
|---|---|
| **Value set** | A versioned scoring product that assigns values to health states for one exact instrument version and use context. It identifies preference population, target population or perspective, geography, elicitation evidence, anchors, model, and value range. |
| **Native value set** | A value set estimated from preferences elicited for the target descriptive system. “Native” does not require one fixed elicitation method. |
| **Mapped or anchored value set** | A value set made by transforming latent or other values onto an anchored scale. The source and target scales and fitted mapping are explicit. |
| **Crosswalk** | A transformation that predicts scores under one instrument or tariff from responses under another version or instrument. A 5L-to-3L crosswalk is not a native 5L value set. |
| **Mapping function** | A mathematical research product that links one score, latent utility, or instrument to another. Its source and target are mandatory. |
| **Population-norm set** | Reference distributions for a defined population, instrument, value set, and period. |
| **Estimate** | A numeric or categorical result with statistic type, value, unit, denominator, uncertainty, population, timepoint, instrument, method, and analysis context. |
| **Comparison result** | A qualified result that states the compared entities, common outcome, direction, effect measure, and analysis context. |
| **Finding** | A source-supported claim or interpretation. It links to supporting estimates when available and records whether it is empirical, interpretive, causal, null, or uncertain. |
| **Limitation** | A stated constraint on design, data, inference, or generalization. |
| **Recommendation** | A stated proposed use or next action. It is not an empirical finding. |
| **Planned result** | A hypothesis, planned analysis, or intended product in a protocol. It cannot satisfy a query for a completed result. |

An estimate does not stand alone. The value −0.865 is useful only when linked to health state 55555, the Indonesian EQ-5D-5L value set, its final hybrid main-effects model, and summary S029.

### 3.7 Portfolio and analytic concepts

| Concept | Meaning and useful detail |
|---|---|
| **Research topic** | A controlled, versioned concept such as valuation, youth instruments, EQ-HWB, EQ-TIPS, bolt-ons, feasibility, or measurement properties. Topics can form a hierarchy. |
| **Topic assignment** | A source-stated, curator-assigned, or algorithm-assigned link from a project, study, publication, or proposal to a topic. It has a method, confidence, and taxonomy version. |
| **Proposal record** | A proposal abstract and reference list supplied for comparison. It is not a publication or funded project unless an external record states this. |
| **Derived metric definition** | A named calculation with numerator, denominator, filters, date rules, grouping, weighting, and completeness requirements. |
| **Derived metric observation** | The result of one calculation against a dated source snapshot. |
| **Similarity result** | A derived comparison between a proposal and projects or publications. It records representation method, model or taxonomy version, score, rank, and snapshot. |
| **Network snapshot** | A dated graph projection, such as co-authorship, citation, or inter-project knowledge flow. It defines nodes, edges, filters, and identity-resolution version. |
| **External metric observation** | A provider-specific citation count, journal metric, open-access status, or other time-varying external fact with an as-of date. |

Co-authorship is normally derived from shared authorship of a publication. Collaboration is not asserted only because two people are in the same project. Citation hubs, components, top-decile shares, and citation lag are derived analytics, not properties of a publication.

## 4. Important relations

| Source concept | Relation | Target concept | Required qualification |
|---|---|---|---|
| Publication | reports | Study | Evidence source; report role; one publication can report several studies. |
| Publication | has authorship | Researcher | Source name, author order, and resolution status. |
| Researcher | has affiliation | Organization | Publication or date context, role, and organization country. |
| Study | conducted within | Project | Evidence and verification status. |
| Award | funds | Project | Funder, amount, currency, award date, and recipient when known. |
| Project | has project role | Researcher or organization | Role type and date interval. |
| Project | associated with | Working group | Exact association type, date, and evidence. |
| Publication or product | is output of | Project | Qualified project-output link and link basis. |
| Publication | cites | Publication | Citation source, matched identifier, and ingestion date. |
| Study | has target population | Population specification | Eligibility and geography. |
| Study | has sample | Sample or cohort | Sample role and recruitment stage. |
| Sample | has analysis set | Analysis set | Exclusions and denominator. |
| Sample | has subgroup | Subgroup | Definition and overlap rule. |
| Study | has setting | Setting or place | Setting role and time. |
| Study | has administration | Administration | Instrument form, sample, mode, language, perspective, support, and timepoint. |
| Instrument version | version of | Instrument family | Version identity. |
| Localized form | localizes | Instrument version | Language, jurisdiction, respondent form, and approval state. |
| Instrument version | has dimension | Dimension | Order and exact wording source. |
| Bolt-on dimension | extends | Instrument version | Development state and tested population. |
| Health state | defined under | Instrument version | State code and dimension order. |
| Study | has valuation exercise | Valuation exercise | Sample and study part. |
| Valuation exercise | uses elicitation method | Elicitation method | Method role and order. |
| Valuation exercise | follows protocol | Valuation protocol version | Adaptation status and version certainty. |
| Valuation exercise | uses task design | Task design | Blocks, states, durations, comparators, and randomization. |
| Valuation exercise | uses perspective | Valuation perspective | Respondent and target person. |
| Valuation exercise | produces | Dataset | Observation type and exclusions. |
| Analysis | analyzes | Dataset | Analysis-set version. |
| Analysis | fits | Statistical model specification | Tested or selected role. |
| Analysis | estimates | Outcome definition | Estimand and unit. |
| Study | produces | Research product | Product type and version. |
| Value set | targets | Instrument version | Required exact version. |
| Value set | applies to | Place or population | Jurisdiction, preference source, and intended use. |
| Value set | based on | Valuation exercise and model | Elicitation data, anchors, selected model, and transformation. |
| Estimate | estimates | Outcome definition | Population, timepoint, method, model, statistic, and unit. |
| Finding | supported by | Estimate or source assertion | Evidence role and qualification. |
| Finding | applies to | Population, instrument, method, model, or product | Context needed to prevent over-generalization. |
| Project, study, publication, or proposal | has topic assignment | Research topic | Assignment source and taxonomy version. |
| Derived metric observation | derived from | Source snapshot | Metric definition, input set, and as-of date. |

## 5. Controlled classifications

### 5.1 Study classification uses several axes

A study can have more than one value on each open axis. The ontology must not compress these into one publication-type string.

| Axis | Values supported by the supplied summaries |
|---|---|
| Evidence stage | protocol; completed empirical study; evidence synthesis; conceptual or methodological paper; secondary analysis; theoretical-state analysis |
| Time structure | cross-sectional; longitudinal; repeated cross-sectional; cohort; registry; test–retest; retrospective; prospective |
| Method family | quantitative; qualitative; mixed methods; systematic review; simulation or theoretical comparison |
| Main purpose | valuation study; value-set development; valuation-method comparison; valuation-design study; measurement-property study; content-validity study; translation and cultural adaptation; feasibility or acceptability; population norms; instrument development; data-quality or process evaluation; routine outcome measurement; stakeholder-preference study; health-status association study |
| Population scope | general population; patient population; caregivers; children or adolescents; older adults; experts; mixed stakeholders |

“National EQ-5D-5L valuation study” is a useful compound classification. It combines valuation-study purpose, national jurisdiction, the exact instrument version, and general-population preference source. These parts remain independently queryable.

### 5.2 Instrument and form classification

The controlled hierarchy must include these distinctions:

- EQ-5D family: EQ-5D-3L and EQ-5D-5L;
- EQ-5D-Y family: EQ-5D-Y-3L and EQ-5D-Y-5L;
- EQ-HWB family: experimental 25-item EQ-HWB, EQ-HWB-S, and EQ-HWB-9;
- EQ-TIPS family: experimental EQ-TIPS V2.0 / EQ-TIPS-3L;
- instrument component: descriptive system and EQ VAS;
- respondent form: self-report, interviewer-administered, proxy version 2, proxy-person perspective, and proxy-proxy perspective;
- localization state: source language form, translated form, culturally adapted form, approved form, experimental form, and version not reported.

Instrument family, level version, item count, experimental version, language, country adaptation, and respondent form are different attributes. For example, “Modern Standard Arabic EQ-5D-Y-5L for use in Egypt” is a localized form of EQ-5D-Y-5L, not a new instrument family.

### 5.3 Elicitation method, protocol, task, and model classification

The elicitation-method scheme contains at least:

- time trade-off;
- conventional TTO for better-than-dead states;
- lead-time TTO for worse-than-dead states;
- composite time trade-off (cTTO);
- discrete choice experiment without duration;
- discrete choice experiment with duration, including DCEd;
- DCE-death;
- paired comparison;
- Kaizen task;
- best–worst scaling case 2;
- standard gamble;
- direct personal utility function elicitation;
- swing weighting;
- location-of-dead task.

The task-design scheme separately records feedback modules, wheelchair examples, practice states, block designs, severity stratification, health-state overlap, immediate-death comparisons, full-health duration comparisons, and split-triplet designs.

The protocol scheme records EQ-VT 2.0, EQ-VT 2.1, EuroQol Portable Valuation Technology, adapted or translated EQ-VT, and EQ-VT with version not reported. “Computer-assisted”, “face-to-face”, “Zoom”, and “online” are administration facts, not protocol versions.

The statistical-model scheme records the base model and its modifiers. It keeps all of these features queryable:

- linear, generalized least squares, ordinary least squares, Tobit, conditional logit, mixed logit, random effects, latent class, meta-analysis, and meta-regression;
- hybrid combination of cTTO and DCE;
- heteroskedastic or homoskedastic;
- censoring point;
- constant or no constant;
- main effects or interactions;
- random parameters and scale classes;
- linear or nonlinear time preference;
- error distribution;
- frequentist or Bayesian estimation;
- selected, rejected, sensitivity, or comparator role.

### 5.4 Product and value-set classification

Every product has a mandatory exact product type.

| Product type | Definition |
|---|---|
| Native value set | Preference evidence was elicited for the target descriptive system and used to estimate its state values. |
| Mapped or anchored value set | Values for the target descriptive system were transformed from a latent or other source scale to a stated anchor. Summary S007 is an example: EQ-5D-Y-3L DCE values were mapped onto cTTO values with a power function. |
| Crosswalk | Responses or values for one instrument or level version are converted to predicted values under another instrument or tariff. |
| Experience-based value set | Values reflect experienced health, as reported for Swedish EQ-5D-3L context in summaries S001 and S098. |
| Hypothetical social value set | A general-public preference product for hypothetical states, such as the Swedish EQ-5D-5L product in S001. |
| Population-norm set | Reference distributions for a population, instrument, scoring system, and period. |
| Localized instrument form | A translated or culturally adapted questionnaire form. |
| Conceptual framework | A structured set of domains or themes, such as the Chinese quality-of-life framework in S067. |
| Protocol | A planned design and analysis specification, such as S016. |

A native value set can still use a hybrid model. A hybrid model does not make a product a crosswalk. A mapped youth value set is also not a 5L-to-3L crosswalk. These distinctions are necessary for questions Q30, Q33, Q50, and Q54.

### 5.5 Outcome and finding classification

Outcome definitions use an open controlled scheme with precise families:

- utility or index value;
- EQ VAS score;
- dimension response or problem prevalence;
- health-state frequency;
- value-set coefficient, state value, range, and worse-than-dead count;
- missingness, completion, completion time, and need for support;
- ceiling, floor, and informativity;
- reliability;
- content, convergent, known-groups, discriminant, and construct validity;
- responsiveness and minimally important difference;
- model fit, prediction error, correlation, agreement, or concordance;
- data-quality indicator;
- qualitative theme, relevance, comprehensibility, or comprehensiveness;
- preference ranking, method preference, or ethical concern.

Finding types include association, group difference, longitudinal change, method comparison, equivalence or no detected difference, ranking, validation support, feasibility judgment, limitation, and recommendation. A causal finding requires explicit causal evidence. The ontology must not convert an association or an author explanation into a causal claim.

## 6. Representation rules for key research facts

### 6.1 Population and sample

A population record uses composable criteria:

- human role: adult, child, adolescent, caregiver, proxy, patient, general-public respondent, expert, or stakeholder;
- health condition and disease stage when reported;
- age rule and hypothetical target age;
- country, region, city, care setting, and residence rule;
- language and literacy rule;
- recruitment source;
- inclusion and exclusion criteria;
- quota or stratification variables.

Each sample records its stage. Useful stage values are invited, eligible, recruited, completed, retained after quality control, analytic, retest, and subgroup. This design supports both a 68,411-person multi-country survey and a 15-person qualitative stakeholder study without treating their sample counts as comparable.

### 6.2 Administration

Administration is a qualified event because mode, language, respondent, and perspective can vary within one study. It records:

- exact instrument or localized form;
- self, proxy, interviewer, or mixed administration;
- face-to-face, paper, web, tablet, telephone, or videoconference mode;
- interviewer assistance and shared-screen use;
- respondent and target-person perspective;
- language;
- recall period;
- place and timepoint.

This supports comparisons such as personal TTO versus tele-TTO in S026 and self-report versus staff or family proxy in S042.

### 6.3 Valuation and analysis

A valuation exercise must state the exact elicitation method and its role. It can state that cTTO contains conventional TTO for better-than-dead states and lead-time TTO for worse-than-dead states. DCE data can be duration-free and remain on a latent scale unless an explicit anchor or transformation is supplied.

The ontology records each tested model and the model-selection decision. It does not store only the selected label. This permits queries about studies that tested a hybrid model but selected a cTTO-only model, as in S001.

### 6.4 Products

A value set record includes:

- product name and version;
- target instrument version;
- target jurisdiction;
- preference-source population;
- perspective and hypothetical target person;
- elicitation methods and protocol version;
- scale and anchors;
- selected model;
- source datasets and exclusions;
- state coverage;
- minimum, maximum, and worse-than-dead information;
- intended use;
- supersession or comparison links;
- publication and project provenance.

Large coefficient tables and all health-state values can be a linked product table. The ontology keeps key summary estimates and the location of the complete product.

### 6.5 Outcomes, estimates, and findings

Each estimate states:

- what was estimated;
- the statistic and value;
- unit and direction;
- denominator;
- sample or subgroup;
- timepoint;
- instrument and scoring system;
- method and model;
- comparator;
- uncertainty and significance when reported;
- evidence source.

Each finding states its scope. For example, “the cognition bolt-on did not add to the five-item-plus-breathing EQ VAS model” in S053 applies to one non-hospitalized Norwegian post-COVID cohort and one regression specification. It is not a universal statement about cognition.

## 7. Publication, study, project, and analytics separation

| Object | Question that it answers | Facts that must not be moved into it |
|---|---|---|
| Publication | What was disseminated, by whom, where, and when? | Recruitment, analysis, and findings belong to the reported study. Funding is not proved by a project-like source path. |
| Study | What research was done, on which data, with which methods, and what did it find? | Approved budget, administrative status, and working-group ownership belong to project or award records. |
| Project | What administrative research activity was approved and managed? | DOI, journal, and author order belong to publications. A publication is an output only through a qualified link. |
| Award | Who funded what, for how much, and when? | Acknowledgment text alone does not supply a complete project budget. |
| Research product | What reusable product resulted, and which version is it? | A value set is not identical to the publication that reports it or the model that estimates it. |
| Derived analytic result | What was calculated from a defined snapshot? | A count, share, network hub, topic trend, or similarity score is not a source statement. |

The basic flow is:

- a funder makes an award;
- an award funds a project;
- a project contains or supports studies;
- a publication reports one or more studies;
- a publication or research product can be a verified project output;
- studies use instruments and methods and produce estimates, findings, and products;
- analytics derive new results from dated sets of these facts.

The flow is not a mandatory chain. A theoretical paper can have no participant sample. A protocol can have no completed findings. A publication can have no verified project link.

## 8. Query and derivation rules

### 8.1 Time and completeness

Terms such as “current”, “last five years”, “first”, “most”, and “since 1990” require an as-of date and a date rule. Project start, award date, study start, online publication date, issue date, and corpus-ingestion date are different dates.

A share or median requires:

- a defined denominator;
- inclusion and exclusion rules;
- a source snapshot;
- treatment of unresolved and missing records;
- a calculation method.

The system must decline a portfolio-wide negative or share when source completeness is not known.

### 8.2 Funding

“EuroQol funded” requires an explicit award or an equivalent verified funding assertion. “Without EuroQol funding” requires positive evidence about all relevant funding or a complete award register. The absence of a EuroQol link does not satisfy Q43.

### 8.3 Same population

“Same population” needs a comparison level:

- same respondents;
- different samples from the same sampling frame;
- same target population in one country;
- only the same broad population type.

The query must state the accepted level or return the level with each result.

### 8.4 Topics and similarity

Topic counts use a versioned topic scheme. A proposal-similarity result identifies whether it used controlled-topic overlap, text similarity, or a combined method. It also identifies the source text and model version. The similarity score is derived and does not become a source topic.

### 8.5 Networks and impact

Co-authorship networks derive edges from resolved authorship records. Citation networks derive edges from matched reference records. Inter-project knowledge flow requires both citation edges and verified project-output links. Citation counts and journal-impact measures require provider and as-of date because they change.

### 8.6 Identity

Counts of researchers, ORCID coverage, member status, institutional rankings, and collaboration measures use one version of the identity-resolution graph. Unresolved profiles remain outside the resolved denominator unless the metric definition says otherwise.

## 9. Competency-question coverage

The categories in this section have these meanings:

- **Answerable from supplied summaries**: the packet contains enough evidence for a packet-scoped answer. This category does not claim that the packet is a complete world bibliography.
- **Requires external linked data**: the question needs project administration, membership, bibliographic references, citation metrics, journal metrics, open-access records, identity-resolution logs, proposal content, or another record that is not in the summaries.
- **Unsupported by available evidence**: the supplied summaries contain no qualifying instance or fact. The ontology can represent the question, but it must return unknown until new evidence is added.

| Question | Required concepts and relations | Answerability and reason |
|---|---|---|
| **Q32 — Which publications came out of working group X's projects in the last five years?** | Working group identity; working-group-to-project role; verified project-output link; publication date; five-year window and as-of date. | **Requires external linked data.** The summaries do not give working-group ownership or a complete project-output register. |
| **Q81 — What share of resolved researchers have an ORCID?** | Resolved researcher; identity-resolution state; ORCID identifier; denominator rule; derived share. | **Requires external linked data.** Author identity records and ORCID links are absent. |
| **Q13 — How has the topical mix of the portfolio shifted over time?** | Portfolio inclusion; project or publication topic assignments; topic taxonomy version; date; period bins; derived proportions. | **Requires external linked data.** The 50-paper packet is not a complete portfolio and project dates are incomplete. |
| **Q18 — Which past funded projects are topically most similar to this proposal abstract?** | Proposal record and abstract; past funded project; project abstract or aims; topic assignments; similarity result; funding and status. | **Requires external linked data.** The proposal and complete project records are not supplied. |
| **Q66 — Which student-grant projects led to publications, and what did they find?** | Project-type assignment for student grant; award; project-output link; publication reports study; study has finding. | **Requires external linked data.** An identifier suffix such as “PHD” cannot prove student-grant status, and output coverage is incomplete. |
| **Q51 — What EQ-TIPS work exists so far?** | EQ-TIPS instrument family and exact version; publication reports study; study uses or develops instrument; products, planned products, and findings. | **Answerable from supplied summaries, within packet scope.** S061 reports qualitative expert consultation for experimental EQ-TIPS V2.0 / EQ-TIPS-3L and states that preference-weighted scores and value sets were planned but not produced. |
| **Q43 — Which value sets were produced without EuroQol funding?** | Value set; producing study; project-output link; award and funder; explicit negative funding evidence or complete funding register. | **Requires external linked data.** Silence about funding cannot prove no EuroQol funding. |
| **Q7 — What is the median time from project start to first linked publication?** | Project start date; verified outputs; publication date rule; first-output selection; duration; metric definition and median. | **Requires external linked data.** Project start dates and complete output links are absent. |
| **Q82 — Which papers carry metadata-quality flags (truncated author list, missing abstract)?** | Publication metadata record; metadata-quality flag; flag type, evidence, status, and ingestion source. | **Requires external linked data.** The summaries do not provide ingestion flags for author-list truncation or missing abstracts. |
| **Q89 — Give a one-paragraph impact profile of project X: outputs, citations, collaborators.** | Project; verified outputs; time-stamped citation observations; resolved authorship; collaboration network; derived narrative with snapshot. | **Requires external linked data.** Citation and resolved collaborator data are absent. |
| **Q31 — Who is currently working on EQ-HWB valuation?** | Researcher; current project role; project status and dates; EQ-HWB topic; valuation-study purpose; as-of date. | **Requires external linked data.** Publications show past work, not current project staffing. |
| **Q35 — Which mapping/crosswalk studies link condition-specific instruments to EQ-5D?** | Mapping or crosswalk product; condition-specific source instrument; EQ-5D target instrument; producing study and publication. | **Unsupported by available evidence.** No supplied summary reports this exact source-to-target mapping. S073 has a 5L-to-3L crosswalk, and S007 maps DCE values to cTTO anchors, but neither is a condition-specific instrument-to-EQ-5D mapping. |
| **Q47 — Which members co-authored with researcher X on funded outputs?** | Researcher identity; dated member status; authorship; co-authorship derivation; funded project; verified output link. | **Requires external linked data.** Member status and complete funded-output links are absent. |
| **Q79 — What is the structure of the within-corpus citation network (components, hubs)?** | Corpus decision; citation edges; matched publication identities; network snapshot; component and hub metric definitions. | **Requires external linked data.** Reference lists and citation edges are absent. |
| **Q74 — Which researchers newly entered the corpus in the last three years?** | Resolved authorship; publication inclusion date rule; first corpus appearance; three-year window and as-of date. | **Requires external linked data.** Full author lists and resolved identities are not supplied. |
| **Q59 — Which open-access papers introduce EQ-HWB?** | Publication; open-access status with date/source; study-purpose classification for EQ-HWB introduction or development; instrument version. | **Requires external linked data.** S058 supplies EQ-HWB development evidence, but the packet does not give complete open-access status. |
| **Q80 — Which projects' outputs cite other projects' outputs (inter-grant knowledge flow)?** | Citation edge; two verified project-output links; project identities; derived inter-project edge and snapshot. | **Requires external linked data.** Both reference data and complete output links are absent. |
| **Q76 — Which publications are linked to more than one funded project?** | Publication; multiple verified project-output links; awards and funders; link count. | **Requires external linked data.** One reported project ID per summary does not establish complete linkage. |
| **Q57 — Which methods appear most often in funded valuation projects (what should I learn)?** | Funded project; valuation-study classification; exact elicitation methods; exact model specifications; count rule and portfolio snapshot. | **Requires external linked data.** The packet is a selected sample and does not contain a complete funded-project inventory. |
| **Q20 — Which ongoing projects overlap with this proposal's aims?** | Ongoing project status; project aims or abstract; proposal aims; topic assignment; similarity result; as-of date. | **Requires external linked data.** Current project records and the proposal text are absent. |
| **Q16 — Has EuroQol funded an EQ-5D-5L valuation study in country X before?** | EuroQol award; funded project; valuation-study classification; EQ-5D-5L; target jurisdiction; award and study dates; completeness rule. | **Requires external linked data.** Several summaries report national value sets, but a complete award history is required for “before”. |
| **Q1 — How many projects has EuroQol funded in total, and what is the combined approved budget?** | Complete project and award inventory; approved amount; currency; status; deduplication; currency aggregation rule; derived count and sum. | **Requires external linked data.** Budgets and the complete award ledger are absent. |
| **Q99 — What share of member-authored corpus papers are excluded as pure applications?** | Dated member status; resolved authorship; corpus decision; controlled exclusion reason “pure application”; denominator and derived share. | **Requires external linked data.** Membership and corpus decision logs are absent. |
| **Q24 — Which valuation methods (TTO, DCE, hybrid) have funded projects in region Y used?** | Funded projects; project geography; valuation exercise; cTTO/TTO and DCE methods; hybrid model classification; region mapping. | **Requires external linked data.** The summaries support the method vocabulary, but not a complete funded regional portfolio. The query must treat hybrid as a model, not an elicitation method. |
| **Q58 — What has been published on EQ-5D-Y-5L so far?** | EQ-5D-Y-5L instrument version; publication reports study; study purpose, population, localized form, product, and finding. | **Answerable from supplied summaries, within packet scope.** S051 reports Modern Standard Arabic translation and adaptation, S062 reports Singapore English adaptation and content validation, and S039 reports stakeholder comparison with EQ-5D-Y-3L. |
| **Q55 — Which institutions host the most EuroQol-funded research?** | Project host role; organization identity; EuroQol award; project; host attribution rule; derived ranking. | **Requires external linked data.** Publication affiliations do not prove project-host status. |
| **Q12 — Which funded publication is the most cited, and which project produced it?** | Verified funded output; external citation count with provider and date; project-output link; ranking rule. | **Requires external linked data.** Citation observations are absent and time-varying. |
| **Q9 — Which projects completed three or more years ago still have no linked publication?** | Project completion date and status; complete output register; publication link; as-of date; explicit no-output derivation. | **Requires external linked data.** Project status and completeness evidence are absent. |
| **Q73 — Has international co-authorship (countries per paper) increased over time?** | Resolved authorship; publication-context affiliation; institution country; publication date; countries-per-paper metric; trend method. | **Requires external linked data.** Complete authors and affiliations are absent. |
| **Q4 — How many projects are ongoing vs completed vs closed?** | Project; controlled status; status effective date; portfolio snapshot; derived counts. | **Requires external linked data.** A project ID in a summary does not state administrative status. |
| **Q94 — Show the growth of the collaboration network decade by decade.** | Resolved authorship; publication dates; co-authorship derivation; decade bins; network snapshots and growth metrics. | **Requires external linked data.** Full authorship and identity resolution are absent. |
| **Q22 — How long after their previous grant did applicant X first publish from it?** | Researcher identity; applicant project role; award or project date rule; verified first output; publication date; duration. | **Requires external linked data.** Applicant roles, grant dates, and full output links are absent. |
| **Q33 — Which studies compare EQ-5D-5L and EQ-5D-3L value sets in the same population?** | Comparative study; native and crosswalk value-set products; exact instrument versions; population-equivalence level; comparison result. | **Answerable from supplied summaries.** S073 directly compares US 3L, native 5L, and 5L-to-3L crosswalk scoring with data sources in which respondents completed both descriptive systems. S023 provides a related Danish 5L, 3L, and crosswalk comparison, with different population-equivalence detail. |
| **Q65 — In which journals do youth-instrument papers usually appear?** | Youth-instrument topic; publication; journal identity; corpus scope; frequency and “usually” rule. | **Requires external linked data.** A representative or complete youth-publication corpus is needed. |
| **Q30 — Which value sets used the EQ-VT protocol, and which version?** | Value set; producing valuation exercise; follows protocol; exact EQ-VT version; version-not-reported state. | **Answerable from supplied summaries.** Explicit examples include S029 and S005 with EQ-VT 2.0, S001 and S023 with EQ-VT 2.1, and S003 with EQ-VT 2.0. S004 reports EQ-VT use but does not state a version in the summary. |
| **Q87 — Which author profiles were merged, overridden, or skipped during identity resolution, and why?** | Identity-resolution decision; candidate profiles; action type; rule; evidence; reason; actor and date. | **Requires external linked data.** Resolution logs are absent. |
| **Q11 — Which countries' institutions have received the most EuroQol funding?** | Award; recipient or host organization; organization country; approved amount and currency; aggregation and ranking rule. | **Requires external linked data.** Funding amounts and recipient records are absent. |
| **Q88 — Which funded papers appeared in the highest-impact venues?** | Verified funded output; journal; external venue-impact metric, provider, year, and field rule; ranking. | **Requires external linked data.** Journal-impact measures are absent and time-dependent. |
| **Q77 — How concentrated is output among PIs (share held by the top decile)?** | Principal-investigator project role; verified project outputs; output-attribution rule; researcher resolution; top-decile and share definition. | **Requires external linked data.** PI roles and complete outputs are absent. |
| **Q86 — What is the distribution of in-corpus citation lag (years between citing and cited paper)?** | Corpus publications; directed citations; citing and cited publication dates; date precision rule; lag observations and distribution. | **Requires external linked data.** Reference edges are absent. |
| **Q28 — Given a proposal's reference list, which cited works are already in the corpus, and which are EuroQol-funded?** | Proposal reference; identifier resolution; publication identity; corpus decision; award and verified project-output link. | **Requires external linked data.** The proposal reference list, corpus index, and funding links are not supplied. |
| **Q84 — How many distinct researchers appear in the graph, and how many are members?** | Resolved researcher; identity-resolution version; dated membership; two denominator rules; derived counts. | **Requires external linked data.** Full authors and membership records are absent. |
| **Q78 — Which non-members co-author most frequently with members?** | Dated membership; resolved authorship; co-authorship derivation; non-member definition; frequency and tie rule. | **Requires external linked data.** Membership and resolved author data are absent. |
| **Q62 — Who works at institution X on EQ topics?** | Organization identity; dated affiliation or project role; researcher; EQ topic assignment; evidence period. | **Requires external linked data.** The summaries do not give complete affiliations or current employment. |
| **Q44 — Which working groups does researcher X's work span?** | Researcher; authorship or project role; publication or project; verified working-group association; span derivation. | **Requires external linked data.** Working-group links are absent. |
| **Q54 — What is the difference between a crosswalk and a native 5L value set — with key references?** | Product type; source and target instruments; native valuation evidence; crosswalk transformation; key publication links. | **Answerable from supplied summaries.** S073 gives the direct US comparison: the native US 5L tariff values EQ-5D-5L directly, while the crosswalk converts 5L responses to 3L tariff values. S023 supplies a related Danish comparison of native 5L, 3L, and crosswalk values. |
| **Q50 — Which papers report both TTO and DCE data for the same value set?** | Publication reports valuation study; value-set product; valuation exercises; cTTO or TTO dataset; DCE dataset; both datasets contribute to or are reported for that product. | **Answerable from supplied summaries.** Examples include S029, S004, S005, S023, and S003. S001 reports both datasets but selects a cTTO-only product; this role distinction must be visible. S007 uses DCE plus separate cTTO anchoring data. |
| **Q25 — What share of student grants produced at least one publication?** | Student-grant project type; complete project denominator; verified output links; at-least-one rule; derived share. | **Requires external linked data.** Grant type and complete output coverage are absent. |
| **Q69 — How has annual publication output of the included corpus evolved since 1990?** | Corpus inclusion decision; publication date rule; annual bins; complete corpus snapshot; derived counts. | **Requires external linked data.** The packet is a 50-paper experimental sample, not a complete corpus since 1990. |
| **Q10 — How does funding split across instrument families (EQ-5D-3L/5L, EQ-5D-Y, EQ-HWB, EQ-TIPS)?** | Award amounts and currency; project; project-to-instrument-family topic assignments; allocation rule for multi-family projects; derived totals and shares. | **Requires external linked data.** Approved budgets and a complete project portfolio are absent. |

All 50 questions are in scope. Q35 has no qualifying supplied instance. The remaining non-summary questions become answerable only when the named external records are linked and their completeness is known.

## 10. Optional study-family views

These views help a researcher read records. They do not impose a class or cardinality on all studies.

### 10.1 Valuation-study view

Show the target instrument, jurisdiction, preference population, sample, perspective, protocol version, administration mode, elicitation methods, task design, datasets, exclusions, tested models, selected model, scale, value-set product, key state values, and limitations.

### 10.2 Measurement-property view

Show the instrument and scoring system, population, comparator measures, property tested, hypothesis, statistic, threshold, result, subgroup, timepoint, and conclusion. Keep reliability, validity, responsiveness, feasibility, and content validity as separate outcomes.

### 10.3 Translation and content-validity view

Show the source form, target language and jurisdiction, translation stages, review or approval body, cognitive-debrief sample, wording decisions, relevance, comprehensiveness, comprehensibility, and final or experimental status.

### 10.4 Protocol and evidence-synthesis view

For a protocol, show planned sample, tasks, analyses, hypotheses, ethics, and planned products. Mark all results as planned. For a systematic review, show search coverage, eligibility, included-study count, synthesis method, outcomes, gaps, and review limitations.

## 11. Complete example records

“Complete” in this section means complete for facts that the summary supports. An unsupported field is shown as not reported. No value is inferred from the project identifier or source path.

### 11.1 Example A: Indonesian EQ-5D-5L value set

**Immediate evidence:** summary S029, verified summary SHA-256 b059ef6dbad0475276b0acbd0ebece29de7cd02855a2b2d1cdedf629429cb402.

**Publication**

- Title: *The Indonesian EQ-5D-5L Value Set*.
- DOI: 10.1007/s40273-017-0538-9.
- Reported project identifier: 2013240.
- Verified award, budget, project status, working group, and project start date: not reported in S029.

**Study**

- Purpose: national EQ-5D-5L valuation study and value-set development.
- Aim: derive a societal Indonesian EQ-5D-5L value set for QALY-based economic evaluation.
- Target population: Indonesian general population aged 17 years or older.
- Sampling: multistage stratified quota design for residence, sex, age, education, religion, and ethnicity.
- Recruitment geography: six cities and surrounding areas—Jakarta, Bandung, Jogjakarta, Surabaya, Medan, and Makassar.
- Completed sample: 1,054 interviews.
- Data-collection period: 9 March 2015 to 24 January 2016.

**Instrument administration**

- Localized form: official Bahasa Indonesia EQ-5D-5L.
- Components: five-dimension descriptive system and EQ VAS.
- Administration: computer-assisted, interviewer-led, face-to-face.
- Protocol: EQ-VT version 2.0.

**Valuation exercises**

- cTTO: ten states per respondent. Conventional TTO valued better-than-dead states. Lead-time TTO valued worse-than-dead states.
- cTTO design: 86 unique states across blocks, with 55555 in every block.
- DCE: seven forced-pair comparisons per respondent from 196 pairs in 28 blocks.
- Quality process: interviewer training, pilot interviews, retraining, feedback flags, and stated exclusion rules.
- Final observation sets: 9,462 cTTO observations and 7,378 DCE observations.

**Analyses and models**

- Tested cTTO model: Tobit censored at −1.
- Tested DCE model: conditional logit with rescaled coefficients.
- Combined model: hybrid regression.
- Selected product model: final hybrid main-effects model, reported as logically consistent.

**Product**

- Product type: native national EQ-5D-5L value set.
- Preference source: Indonesian general population.
- Intended use: QALY-based economic evaluation, HTA, PROM research, clinical trials, and hospital-care research.
- Health-state coverage: all 3,125 EQ-5D-5L states.

**Estimates and findings**

- Utility for 11111: 1.000.
- Utility for 11112: 0.921.
- Utility for 55555: −0.865.
- Negative predicted states: 1,108 of 3,125, or 35.46%.
- Example utility: state 12345 has value 0.240.
- Model comparison: predicted values correlated at 0.995 for hybrid versus cTTO and 0.997 for hybrid versus DCE.
- Dimension finding: mobility had the greatest effect and pain/discomfort the least in the final model.

**Limits**

- Quota and personal-network recruitment.
- Concentration on Java.
- No weighting for small demographic deviations.
- Uncertainty about island-specific preferences.

This record keeps cTTO and DCE as elicitation methods, Tobit and conditional logit as separate tested models, hybrid regression as the combined model, and the value set as the product.

### 11.2 Example B: EQ-TIPS expert consultation

**Immediate evidence:** summary S061, verified summary SHA-256 19e062b813b6014b8d70f92eda57e18e430a7bc53053b0faa94666bca8ff31f3.

**Publication**

- Title: *Developing the EuroQol toddler and infant populations (EQ-TIPS) instrument: qualitative analysis of expert views on content validity and conceptual challenges*.
- DOI: 10.1007/s11136-025-04150-3.
- Reported project identifier: 365-RA.
- Verified award, budget, project status, and working group: not reported in S061.

**Study**

- Purpose: qualitative instrument-development and content-validity consultation.
- Evidence stage: completed empirical qualitative study.
- Aim: review EQ-TIPS V2.0 wording and content and examine possible uses and development challenges.
- Participants: 33 experts from 15 countries.
- Groups: EuroQol experts; pediatric health and development experts; pediatric HRQoL instrument developers.
- Administration: three online semi-structured focus groups through Zoom.
- Data-collection period: December 2022 to February 2023.
- Analysis: Braun and Clarke six-phase thematic analysis in NVivo Version 14, mainly deductive with permitted inductive themes.

**Instrument under study**

- Family: EQ-TIPS.
- Exact form: experimental EQ-TIPS V2.0 / EQ-TIPS-3L.
- Intended population: infants and toddlers, with a proposed age range of 0–3 years.
- Dimensions: Movement, Play, Social Interaction, Communication, Eating, and Pain.
- Response levels: no, some, and a lot of problems.
- Proxy component: EQ-TIPS Visual Analogue Scale from 0 to 100.
- Five-level form: not available for testing in this study.

**Findings**

- Most experts found the measure short, easy to complete, and suitable for clinical trials and research.
- Experts were not always clear whether the construct was health, health status, HRQoL, or development.
- Most experts gave priority to age-relevant content over direct dimension mapping to EQ-5D-Y.
- Proxy subjectivity, proxy selection, and caregiver spillover need explicit treatment.
- “Today” was generally preferred for acute conditions. A longer recall period could help with chronic or fluctuating conditions.
- Sleep was widely proposed as an additional dimension. Emotions were also proposed.
- Communication and Social Interaction can overlap.

**Product and result status**

- Produced evidence: expert content-validity evidence and development recommendations.
- Preference-weighted score: planned, not produced.
- Value set: planned, not produced.
- Psychometric evidence: not produced by this study.
- Direct caregiver or child testing: not done.

This record shows why an instrument-development paper must not be forced into a valuation-study template. It also prevents a planned value set from appearing as a completed product.

### 11.3 Example C: native 5L value set versus crosswalk

**Immediate evidence:** summary S073, verified summary SHA-256 e22a331a0bb5d8202b25eb3bb4b06eb3f631f78a4a13871bd2c477a128e83e1a.

**Publication**

- Title: *EQ-5D-5L measurement properties are superior to EQ-5D-3L across the continuum of health using US value sets*.
- DOI: 10.1186/s12955-022-02031-8.
- Publication date: 9 September 2022.
- Project identifier: 20190360.
- Funding assertion: the EuroQol Research Foundation funded the study and had no role in conduct or interpretation.

**Study**

- Purpose: comparative measurement and value-set study.
- Data source 1: 2017 US EQ-5D-5L valuation study, 1,133 respondents.
- Data source 2: international parallel 3L/5L fielding dataset, 3,790 respondents from healthy and disease populations.
- Instruments: EQ-5D-3L, EQ-5D-5L, and EQ VAS.
- Products compared: US 3L tariff, native US 5L tariff, and US 5L-to-3L crosswalk.
- Analyses: theoretical range and transition comparisons, empirical discriminative ability, and an EQ VAS-weighted responsiveness simulation.

**Product semantics**

- Native US 5L tariff: values EQ-5D-5L health states on its own 5L value-set scale.
- 5L-to-3L crosswalk: converts 5L responses to predicted 3L tariff values.
- These products share an input descriptive system in use, but they have different value-generation routes.

**Estimates and findings**

- Scale range: 1.573 for native 5L; 1.109 for 3L and crosswalk.
- Worse-than-dead states: 620 of 3,125 for native 5L; 10 of 243 for 3L; 39 of 3,125 for crosswalk.
- Gap from 11111 to the next-best state: 0.057 for native 5L, 0.140 for 3L, and 0.112 for crosswalk.
- Mean single-level transition: 0.078 for native 5L, 0.111 for 3L, and 0.061 for crosswalk.
- Interpretation: the authors report better interval properties, precision, discrimination, and responsiveness for native 5L.

**Limits**

- Few paired datasets were available.
- No trial or longitudinal data were used.
- Evidence was sparse for very poor health.
- Responsiveness used EQ VAS as the only anchor.
- Results can depend on disease and geography.

This record supplies a direct answer pattern for Q54 and makes product generation queryable instead of relying on the word “value set”.

## 12. Free text, derived data, optional detail, and boundaries

### 12.1 Keep as source-linked free text

The following facts should remain source-linked narrative unless a clear use case supports further structure:

- detailed aims and author interpretations;
- cultural explanations, such as possible family-burden concerns;
- participant quotations and interviewer dialogue;
- nuanced translation decisions;
- full limitation narratives;
- model-selection rationale;
- qualitative themes below the controlled topic level;
- open-text respondent feedback;
- recommendations and ethical concerns.

A short controlled finding can point to this narrative. It must not replace it.

### 12.2 Derived only

The following results are derived and must include a metric definition and snapshot:

- project and publication counts;
- shares, medians, top-decile concentration, and annual trends;
- first publication and time-to-publication;
- topical mix and proposal similarity;
- co-authorship growth, components, and hubs;
- international country count per paper;
- citation count, citation lag, and inter-project knowledge flow;
- institution, country, journal, or method rankings;
- one-paragraph impact profiles.

### 12.3 Optional structured detail

These details are useful but can remain optional in an initial implementation:

- every health-state coefficient and all 3,125 state values;
- every task block, state pair, and randomization rule;
- every quota cell;
- software package and version;
- detailed quality-control thresholds;
- every survey item and translated wording;
- ethics approval identifiers;
- conflict-of-interest roles;
- data-access conditions.

When present, these details need evidence and version context.

### 12.4 Outside the core scope

The following items remain outside the core ontology:

- participant-level response data and direct identifiers;
- executable scoring code;
- legal rights to instruments or data;
- causal claims that the study did not make;
- a claim that one culture caused a valuation pattern;
- live project budgets, member rosters, citation counts, journal metrics, and open-access states until they are linked from authoritative records;
- full article text.

## 13. Reuse of established identifiers and patterns

The ontology should reuse a small set of established patterns when they improve linking:

- **DOI** for publication identity. It reduces title-based duplicates.
- **ORCID** for researcher identifiers. It supports Q81, but an ORCID does not replace local identity-resolution evidence.
- **ROR** for organization identifiers as a proposed external extension. It helps to merge institution name variants and countries.
- **ISO country and language codes** as a proposed external extension. They support region, language, and international-collaboration queries.
- A **SKOS-like concept pattern** for preferred labels, alternative labels, broader and narrower concepts, and exact matches. This keeps source terms and canonical terms separate without requiring the full standard.
- A **PROV-like provenance pattern** for source, extraction or curation activity, and derivation. This makes summary evidence, external facts, and analytic results auditable without requiring the full standard.

EuroQol-specific meanings remain primary. These reused patterns do not define valuation study, cTTO, EQ-5D-5L, hybrid model, or value set.

## 14. Unresolved choices and risks

### 14.1 Study boundaries

One publication can contain a main study, secondary analysis, validation exercise, and sensitivity analyses. A practical rule is needed for when an analysis becomes a separate study. The recommended rule is to create a separate study when the aim, population, or data source can stand alone. Otherwise, create a separate analysis under the study.

### 14.2 Summary evidence versus paper evidence

The immediate evidence is a fixed summary, not the source paper. A future ingestion process must keep both provenance levels. It must not state that a source-paper detail was checked when only the summary was checked.

### 14.3 Conflicting reported values

Summaries can preserve source conflicts, as S004 does for mean age and S076 does for the count of 5L feasibility studies. The model needs parallel assertions and a quality flag. A single scalar field would lose this evidence.

### 14.4 Project identifiers and funding

Project identifiers appear in all summaries, but their administrative meaning is not always stated. The system must not derive funder, award type, student-grant status, host, or working group from an identifier pattern.

### 14.5 Product taxonomy

The boundary between native, mapped, anchored, and crosswalk products needs a curator guide. S007 is a useful test: it is an EQ-5D-Y-3L value set that maps DCE values onto cTTO values. It is not a crosswalk from a condition-specific instrument and not a 5L-to-3L crosswalk.

### 14.6 Hybrid terminology

Users can call hybrid a “method”, as in Q24. The ontology should accept this search term but return two typed results: the elicitation methods that supplied data and the hybrid statistical model that combined them.

### 14.7 Instrument change and experimental status

EQ-HWB and EQ-TIPS forms can change. Version, item count, experimental status, language, and date must be part of identity. “EQ-HWB” without a version can be a family search but not an exact administration fact.

### 14.8 Population equivalence

“Same population” can mean the same respondents or only the same national population. The query interface must expose this distinction. It must not silently combine the levels.

### 14.9 Scale comparability

QALY, latent DCE, pits, and experience scales are not interchangeable. An anchored value of zero can mean death, 55555, or coma. The scale and anchors must travel with every estimate and product.

### 14.10 Topic classification

Topic assignments can be source-stated, curator-assigned, or algorithmic. The system needs a versioned topic scheme and rules for multi-topic studies. Otherwise, portfolio-shift and similarity results will not be reproducible.

### 14.11 Person and organization identity

Name collision, name change, affiliation change, and group authorship create error risks. Identity-resolution decisions must be reversible and auditable. Institution rankings need time-specific affiliation or project-host facts, not current organization names only.

### 14.12 Negative and complete answers

Queries about no funding, no publication, or no prior study are high risk in an open graph. The system must require a completeness declaration before it returns a negative portfolio answer.

### 14.13 Time-varying analytics

Citations, open-access status, project status, membership, and journal metrics change. Each observation needs a provider and as-of date. A derived narrative must cite its snapshot.

### 14.14 Classification overlap

Many studies have several valid purpose classes. S029 is both a valuation study and a value-set development study. S014 is a process evaluation nested in a valuation study. Multi-axis classification prevents false exclusivity.

### 14.15 Granularity and graph size

Full state-value tables, item wording, and task pairs can be large. Store them as linked typed tables or resources when needed. Keep product and study identity in the core graph. Do not reduce exact values to unsearchable attachments when a stated query needs them.

## 15. Minimum acceptance criteria

An implementation of this proposal is acceptable only if it can:

- distinguish publication, study, project, award, product, and derived result;
- preserve each source term while it maps to a canonical term;
- represent valuation study, cTTO, DCE, hybrid model, and EQ-5D-5L as different exact concepts;
- distinguish native value set, mapped value set, and crosswalk;
- attach population, sample stage, administration, language, mode, and perspective to the correct study part;
- store an exact statistical model with its modifiers;
- bind every estimate and finding to population, timepoint, instrument, method or model, and evidence;
- keep planned products separate from completed products;
- maintain unknown and explicit negative states;
- record external and derived facts with provider, method, snapshot, and provenance;
- support the 50 question patterns in Section 9 without inventing missing facts.
