# Candidate 1: paper-first EuroQol ontology

Rounds 1 to 4, batches 01 to 04. Round 4 extends the earlier record with the granularity-calibration papers.

## Current ontology and extraction guide

### Record boundary

The **Paper** is the main research record. A paper can have one or more **Study Components** when samples, phases, tasks, country modules, time points, or analyses have different semantic facts. A component is always part of one paper. Do not make a component into an independent main record.

The ontology is a concept model and an extraction guide. It is not a fixed set of mandatory fields. Use only the concepts that apply to a paper. Use controlled terms for stable retrieval distinctions, repeatable structured statements for facts that can occur more than once, relations for connections, and short narrative for context that does not have a stable category.

### Paper purpose and scope

For each paper, record:

- one concise **Research Aim** in the authors' scope;
- one or more **Study Family** tags when the paper has more than one purpose;
- the principal **Topic or Construct** tags;
- the paper's **Contribution** and any product that it creates, tests, compares, or documents.

Use these controlled Study Family terms in the current guide:

- valuation and value-set development;
- preference-elicitation method study;
- instrument development or revision;
- measurement-property study;
- content-validity or concept-elicitation study;
- population-health description;
- population-norm or reference study;
- health-equity or inequality study;
- mapping or scoring study;
- translation or cultural-adaptation study;
- economic-evaluation or decision-model study;
- implementation study;
- reported-use, policy, or practice study;
- evidence synthesis;
- protocol or study-design paper;
- research-infrastructure or data-resource description;
- survey-method or data-quality study;
- cost-of-illness or health-burden study;
- social-value or priority-preference study;
- conceptual or reporting-guidance paper.

Use more than one family when purposes are material. Do not add a family only because the paper uses a statistical model. Record the model under Method Use. For example, papers 12 and 26 are preference-elicitation method studies because they empirically compare valuation specifications. Paper 9 is an evidence synthesis whose topic is statistical analysis practice. Paper 39 is a conceptual and reporting-guidance paper because it develops an uncertainty account without a new empirical method comparison. Treat `psychometric study` as a search synonym for measurement-property study, not as a second controlled term.

Study Family and **Study Design** are different. For example, an evidence synthesis can study measurement-property evidence or statistical practice. A cross-sectional survey can support a population resource or a policy-practice study. Record the design with terms such as cross-sectional survey, prospective cohort, qualitative interview study, systematic review, randomized factorial experiment, or secondary analysis. Add a short design description when the controlled term is not sufficient.

### Study components and relations

Create a Study Component only when it prevents a false paper-level statement. Give it a short paper-local name and a component type, such as phase, sample, task, country or language arm, analysis, or review workstream.

Record **Component Status** when a paper combines completed and planned work. Use planned, piloted, data collection complete, analyzed, or reported as applicable. A completed pilot can inform a planned main study, but it does not make the planned sample, analysis, or product an observed result.

Useful relations are:

- **part of** Paper;
- **precedes** or **informs** another component;
- **uses evidence from** a sample, data set, instrument, protocol, value set, or earlier study;
- **administers**, **values**, **scores with**, **compares with**, or **evaluates** an instrument or product;
- **produces** a product;
- **tests** a measurement property or hypothesis;
- **supports** a finding.

Do not create a component for each table, regression, subgroup, or outcome. Use an Analysis component only when its input, purpose, or interpretation differs from the other analyses.

For a factorial or multi-condition experiment, use a paper-local **Study Condition** when participants or tasks are allocated to conditions and the conclusion depends on one factor or an interaction. Record the factor, levels, allocation method, crossed or nested structure, and linked comparison. Do not turn each observational covariate into a Study Condition.

### People, evidence, and intended use

Keep these three roles separate:

- **Evidence Supplier**: the person or source that supplies data, preferences, judgments, documents, or study-level evidence.
- **Referent**: the person or thing that an answer describes. This can be the respondent, a care recipient, a hypothetical child, a vignette character, a health state, a trial, or an HTA practice.
- **Intended Population or Decision Context**: the population, setting, or decision for which the result or product is intended.

For human samples, record applicable age group, country or region, language, health condition or clinical area, care setting, policy setting, and respondent role. Record self-report and proxy-report separately. State the relationship between respondent and referent when it affects interpretation.

For selection and flow, use repeatable **Sample Stage** statements. A stage includes its label, count when reported, and link to the applicable component. Useful stage labels include approached, eligible, recruited, completed, excluded, clinically stable, and analyzed. Record the sampling method, recruitment source, inclusion and exclusion rules, quota variables, and important non-response or attrition in structured terms plus short narrative. Do not reduce representativeness to a yes-or-no flag.

### Instruments and products

An **Instrument Involvement** statement identifies:

- instrument family;
- exact version, level form, long or short form, experimental status, youth or adult variant, and self or proxy form when reported;
- language version when reported;
- the instrument's role in this paper;
- the applicable component and population.

For a language form, record the language and the locale or language variety separately. A UK English to Singapore English process is an intralingual cultural adaptation even though the language is English in both forms. Do not reduce it to “no translation.”

Use these instrument-role terms:

- target or evaluand;
- administered measure;
- preference-elicitation health-state system;
- comparator or convergent measure;
- anchor or external criterion;
- source of candidate concepts, items, or labels;
- scoring or value-set source;
- experience-based valuation input;
- product created or revised;
- object of instrument-structure preference assessment;
- object of a review, survey question, or reported practice.

Do not use the broad label “used” when a more exact role is known. Treat the descriptive system, EQ VAS, and derived utility or index as instrument components. Record the component when the method or finding applies to only one of them.

A **Product** can be a value set, descriptive system, language version, conceptual framework, protocol, data resource, mapping or scoring function, implementation program, or guidance contribution. Record product type, target instrument or context, country and language scope, and maturity without forcing unlike facts into one stage. Use the following structured dimensions when the paper supports them:

- **Product Status**: planned, proposed, draft, candidate, or final reported product;
- **Evaluation or Review Evidence**: expert reviewed, co-designed, tested for comprehension, tested for measurement properties, or tested in a simulated workflow;
- **Governance or Endorsement**: version-management approved or author-recommended;
- **Derivation Status**: estimated, mapped, or otherwise derived, with its provenance;
- a link to **Documented Use or Effect** for a pilot or routine implementation in the reported setting.

These dimensions can occur together. They are not one universal sequence. Do not use `established` as a controlled maturity term because authors can use it to mean estimated, final in the paper, recommended, available, or adopted. State the supported fact. Do not infer adoption from an author recommendation, a co-designed prototype, a simulation, or a final estimate.

A population norm or reference resource must also identify its reference period, source samples, instrument and outcome form, scoring or value-set route, reported strata, and intended comparison population. A cost or burden estimate must identify its reference year and population. These facts can make an estimate obsolete or unsuitable without changing what the source paper produced.

### Administration and task protocol

An **Administration Event** connects an instrument or task to a component, evidence supplier, and referent. Record applicable mode, reporter, recall period, setting, order or randomization, and software or platform version when it changes comparison or reproducibility.

Use specific mode terms such as web self-completion, paper self-completion, computer-assisted personal interview, face-to-face interview, telephone interview, or proxy completion. Keep mode and reporter separate.

Also keep the participant response mode separate from later data entry, storage, or survey management. State whether a mode was offered, selected, or used when the paper gives this information. A paper questionnaire that staff enter into REDCap is not web self-completion.

Record **Administration Support** separately from mode: interviewer supervised or assisted, unsupervised self-completion, automated tutorial or prompting, live clarification, and feedback or review module. Also record recruitment source separately. An online-panel, unsupervised task and a recruited-in-person, interviewer-assisted task differ on more than a digital-versus-face-to-face axis.

For proxy administration, record the exact **Proxy Perspective**. Distinguish the proxy's own assessment of the referent from the proxy's estimate of how the referent would assess themself. Keep the proxy-referent relationship and independent or joint completion as separate facts.

For valuation work, create a repeatable **Valuation Task Use** for each task. Record:

- exact task, such as cTTO, conventional TTO, lead-time TTO, lag-time TTO, DCE, DCE with duration, PTO, standard gamble, or VAS;
- the task purpose, such as direct anchoring, relative preference estimation, or sensitivity analysis;
- respondent and referent perspective;
- state system, duration and worse-than-dead framing when material;
- experimental design, blocks, states or pairs, and tasks per respondent when material;
- protocol and technology version;
- administration mode and quality-control process.

This detail is specific to valuation. It must not become a broad paper-level method list.

For compositional or multi-step elicitation, record **Preference Elicitation Architecture**: compositional, decompositional, or semi-compositional; the ordered task steps and their intermediate outputs; the anchoring step; the final derivation; and whether the intended product is an individual or aggregate utility function. A dimension rank, swing weight, level rating, dead-versus-worst choice, and anchoring factor are linked steps, not interchangeable valuation tasks.

Use **Distributional Preference Task Use** when PTO, gain trade-off, willingness to pay, or a priority DCE estimates the relative social value of health gains rather than the value of health states. Record the beneficiary groups and ages, decision-maker perspective, health-gain type and duration, counterfactual and later life course, group sizes, matching or iteration rule, equivalence or opt-out option, forced-choice condition, task order, and output weight. Do not classify a PTO age weight as an EQ-5D value set.

When a choice experiment assesses the structure of an instrument, record **Instrument-Structure Preference Assessment**. State the target attributes and levels, exact task form, such as paired profile, partial profile, kaizen or other adaptive sequence, goods or bads framing, referent scenario, property tested, and planned model. Preference-order concordance, non-zero main effects, and agreement between task forms can inform instrument revision without producing a QALY-anchored value set.

For an analysis of valuation scale construction, also record the **Valuation Model Specification**: input task data, latent or cardinal starting scale, operational anchor basis, time-preference form, preference-heterogeneity treatment, and resulting scale. Keep immediate death, a zero-duration life, and externally observed cTTO means as different anchor bases. A conceptual statement that dead equals zero in the QALY model does not show how a fitted latent scale was normalized.

Use **Task Feasibility Assessment** when a study assesses whether respondents can complete a valuation or other research task. Record completion time or burden, number of moves or choices, non-trading or other task behavior, reported understanding, ability to distinguish options, decision difficulty, and the comparison source. Keep task feasibility separate from psychometric missingness and from implementation feasibility.

### Method use

A **Method Use** is a repeatable statement that connects a method to its component, input, purpose, and output. Keep the stable method family controlled. Keep the exact named method in a controlled or normalized text value. Add a short narrative only for unusual specifications. The specialized method concepts below, such as Valuation Task Use, Measurement Property Assessment, Implementation Assessment, and Survey Data Quality Control, are profiles of Method Use. Create one method statement with the applicable specialized detail. Do not create a broad Method Use and a second duplicate specialized record for the same act.

Method families in the current guide are:

- sampling and recruitment;
- valuation task and experimental design;
- statistical model or estimator;
- scoring, anchoring, mapping, or prediction;
- measurement-property assessment;
- qualitative data collection and analysis;
- translation and cultural adaptation;
- evidence search, screening, extraction, and synthesis;
- survey response analysis;
- implementation and workflow assessment;
- economic evaluation and decision modeling;
- cost-of-illness and health-burden estimation;
- population norm, health-equity, and inequality analysis;
- data-quality control;
- missing-data handling;
- sensitivity or robustness analysis.

For statistical methods, state the outcome or input form and the method purpose. For repeated observations, state whether the method handles within-person correlation. For model comparisons, record the candidate model, selection criteria, and selected model. Do not make each software command or parameter an ontology class.

For evidence syntheses, record search sources and end date, main eligibility boundaries, screening and extraction process, included paper or trial count, duplicate-data handling, and synthesis type. Distinguish a pooled meta-analysis from a narrative or descriptive synthesis.

For a translation or cultural-adaptation process, record the adaptation type, source instrument form, source language and locale, target language and locale, intended geography, source and target administration forms, forward and back translation when applicable, reconciliation and review, respondent testing, revision cycles, and approval state when reported. Keep a linguistic product for one target setting separate from an author claim that it can transfer to other settings.

For an economic evaluation, record the decision-model type, alternatives, population, perspective, time horizon, outcome and discounting when these facts change interpretation. Link each utility input to its derivation route. Do not reproduce a complete decision model.

For a **Cost-of-Illness or Health-Burden Assessment**, record the condition and case definition, prevalence- or incidence-based approach, population and reference year, perspective, cost or burden categories, bearer or payer, unit-cost and valuation route, price year and currency, main assumptions, and sensitivity analysis. Keep direct medical cost, direct non-medical cost, productivity or other indirect cost, non-monetary DALY or QALY loss, and monetized wellbeing loss separate. This is not a comparative economic evaluation unless the paper evaluates alternatives.

For **Survey Data Quality Control**, record the threat or indicator, the rule and threshold, its timing, the unit to which it applies, the action taken, and the affected count with its denominator. Distinguish prevention, real-time monitoring, flagging, exclusion, interviewer action, and later survey redesign. Also distinguish researcher controls from panel-provider controls. A bot score, speed rule, duplicate check, consistency check, missing-data rate, and quota result are not one interchangeable quality flag.

For a **Population Norm or Equity Analysis**, record the socioeconomic or demographic construct and its operational measure, its analysis role, the outcome representation and derivation, the metric or model, reference or ranking group, adjustment set, applicable country or subgroup, and result direction. Useful roles include norm stratum, socioeconomic indicator, predictor or exposure, adjustment covariate, rank variable, and decomposition factor. Keep an observed gradient, an inequality index, its decomposition, and a residual within-profile association separate. Do not infer causation from a cross-sectional association.

### Outcome representation and derivation

An **Outcome Specification** states which instrument component is analyzed and in which form. Distinguish item or dimension responses, health profiles, an unweighted level sum score, EQ VAS, and a preference-weighted index or utility. Record a scale transformation when it changes comparison.

Use a repeatable **Outcome Derivation** when a result depends on a scoring or mapping route. Record:

- source instrument and response form;
- direct scoring, response mapping, direct utility mapping, crosswalk, or other transformation;
- target instrument and version;
- mapping function or value set and its preference country when material;
- derived outcome and the component or analysis that uses it.

This structure must show, for example, that a directly collected EQ-5D-5L profile scored with a value set differs from an SF-12 score mapped to an EQ-5D-3L utility. Do not store each coefficient as an ontology concept.

For a derived value-set product, also preserve the **Product Provenance Chain**: source descriptive system and value set, source preference population and period, mapping or crosswalk algorithm and its bridge population, target descriptive system, and later data to which the product is applied. A same-country crosswalk can still inherit preferences and response relationships from different populations and periods.

### Measurement properties

Use **Measurement Property Assessment** as a specialized Method Use. Record the target, which can be an instrument component, reporter form, elicitation task or method, score, or value-set product; the property; exact analytic method; comparator or anchor; prespecified criterion when reported; population; analysis level; and result direction.

Use these property terms when applicable:

- feasibility or missingness;
- response distribution, ceiling, or floor;
- test-retest reliability;
- measurement error;
- content validity, with the aspect comprehensiveness, relevance, or comprehensibility;
- construct validity, with convergent, structural, or known-groups subtype;
- responsiveness or sensitivity to change;
- informativity or response-category use;
- item discrimination or information;
- differential item functioning;
- inter-rater or self-proxy agreement.

Do not use one broad “validity” label when the paper tests a specific property. Do not record internal consistency for a preference-based descriptive system unless the paper gives a reason that makes it relevant.

Record the direction or subgroup for responsiveness. Also record the stability definition or change anchor and time interval. An instrument can respond to worsening but not improvement in the same study.

Use **Cross-Instrument Agreement** when the paper tests whether scores from two instruments or derivation routes agree. Record it as one Measurement Property Assessment linked to the applicable Comparison. Correlation alone does not show agreement.

Use **Cross-Informant Agreement** when the same referent is assessed by self-report and proxy report or by two rater types. Record it as one Measurement Property Assessment linked to the applicable Comparison. Record the reporter pair, proxy perspective, paired dyad, instrument form, time point, dimension or score, agreement statistic, and result. Do not treat self-proxy agreement as instrument test-retest reliability.

### Implementation assessment

An **Implementation Assessment** is a specialized Method Use for the introduction or routine collection of an instrument or practice. Record the implementation object, site and maturity, actor perspective, method, and outcome. Use controlled outcome terms for uptake or reach, follow-up or retention, acceptability, respondent burden, workflow burden, mode or timing preference, and barrier or facilitator. Keep these outcomes separate from psychometric feasibility or missingness.

Record a pilot use as **Documented Use or Effect** only for the site and period that the paper documents. Record a proposed scale-up as planned future work, not as implemented use.

Use **Implementation Workflow Specification** for a designed or tested delivery pathway. Record the trigger and timing, eligible respondent and proxy fallback, offered and used response modes, result representation, data recipient, review responsibility, patient or clinician flag rule, discussion step, clinical action or escalation route, training and support, information-system integration, and workflow maturity. A co-designed or mock-tested pathway is a product, but it is not documented routine use.

### Analytic and decision uncertainty

Keep **Analytic or Decision Uncertainty** separate from Extraction Uncertainty. Record the object whose value is uncertain, uncertainty type, source stage, whether the uncertainty is introduced or inherited, method used to quantify or explore it, information reported, downstream use, and handling method.

Use these uncertainty types when supported: intrinsic variability, observed or latent heterogeneity, statistical uncertainty, and methodological variation. Source stages can include descriptive-system response collection, valuation study design, preference elicitation, valuation modeling, mapping, disease-state estimation, meta-analysis, and economic modeling. Preserve a chain when uncertainty passes through several stages. A coefficient standard error is not the same as uncertainty for each derived health-state value, and source-text ambiguity is not analytic uncertainty.

### Comparisons

A **Comparison** states what is compared and which condition differs. Record:

- objects or groups being compared;
- the contrast axis;
- the component and method;
- the outcome or property;
- the principal result.

Controlled contrast axes in the current guide are instrument or version, response-scale construct, population or health group, country or culture, language wording, administration mode, time or follow-up structure, scoring or value set, preference source, valuation task, and statistical model. This prevents a finding from appearing to be a general instrument difference when it is conditional on population, timing, language, or scoring.

Add outcome representation or derivation route, implementation condition, and socioeconomic group when one of these defines the contrast. When evidence comes from independent samples, record that fact and any material difference in recruitment, mode, or collection period.

### Findings, interpretation, and research use

Capture only principal results. A **Finding Summary** states the result, its object, the applicable component or comparison, and any decisive number. Keep detailed estimates in source tables.

Keep these narrative types separate:

- **Author Interpretation**: how the authors explain the findings;
- **Author-Reported Implication**: a scientific, practical, policy, implementation, or instrument-development consequence stated by the authors;
- **Documented Use or Effect**: actual use or effect reported in the paper;
- **Author-Reported Limitation**;
- **Author-Reported Future Work or Gap**;
- **Extractor Observation**: a narrow source ambiguity or application issue. Label it as an extractor observation.

An implication is not documented impact. Do not infer use, adoption, or a corpus gap. Preserve transfer limits, such as a country, language, age, condition, or valuation perspective. Use Extractor Observation for a scoped interpretation or application note. Use Extraction Uncertainty below for incompatible, missing, or unclear source facts. Do not duplicate the same issue in both forms.

### Evidence reuse and uncertainty

Use **Evidence Reuse** when a paper reuses or extends a sample, dyad data set, protocol, value set, mapping, model, trial corpus, or survey infrastructure. Record the reused object, its role, and whether the paper analyzes it again, extends it, or uses it as a comparator. A standard method citation alone is not evidence reuse.

When a paper combines reused data sets, also record the contributing sample from each source, the compatibility basis, and material differences in variable definitions, order, mode, or collection period. Do not turn the combined data into an apparently new independent sample.

Use **Extraction Uncertainty** for conflicting statements, missing version details, unclear sample roles, uncertain product maturity, or a transfer limit that cannot be normalized safely. Preserve both source statements. Do not silently choose one.

## Applications to batch 01

### 1. `10.1007/s40258-021-00639-3`

**Aim and family.** Valuation and value-set development. The paper aimed to establish the first Danish EQ-5D-5L value set from adult general-population preferences and to select a model from cTTO-only, DCE-only, and combined approaches. It also addressed Danish health-care priority setting and QALY estimation.

**Components and evidence roles.** One valuation study had linked cTTO and DCE task components for the same respondents and separate model-comparison and value-set-comparison analyses. Danish adults older than 18 years supplied preferences for hypothetical EQ-5D-5L health states. The intended preference population was the Danish adult general population. The intended decision context was Danish health-care prioritization, including hospital-dispensed medicines.

**Selection and flow.** Statistics Denmark supplied a random sample stratified for age, gender, education, and region. A market-research panel later supplemented recruitment under the same representativeness targets. Of 1,052 interviews, 1,014 entered analysis after interviewer, software, withdrawal, health, and incomplete-task exclusions. The source reports slight under-representation of people aged 18–24 years and people with the lowest education.

**Instrument and administration.** EQ-5D-5L was the target health-state system. Respondents also self-reported current health with its descriptive system and EQ VAS. EQ-VT 2.1 was administered in computer-assisted personal interviews. Each analyzed respondent valued ten states by cTTO and seven pairs by DCE. The cTTO task combined conventional TTO for states better than dead with lead-time TTO for states worse than dead. The DCE pairs had no duration. A cTTO feedback module allowed respondents to reject an ordering. Interviewer training and the EQ-VT quality-control tool monitored protocol compliance and face validity.

**Methods and comparisons.** The cTTO design covered 86 states in balanced blocks. The DCE design covered 196 pairs in 28 blocks. Candidate models included generalized least-squares random-intercept and random-effects Tobit models for cTTO, conditional and heteroscedastic conditional logit models for DCE, and two hybrid models. Logical consistency was the main selection criterion. A sensitivity analysis restored 712 cTTO observations that respondents had marked as incorrectly ordered. The final product was compared with the Danish EQ-5D-3L value set and the Danish 3L-to-5L crosswalk. The comparison therefore differs in instrument version, valuation method, source period, and direct versus mapped scoring route.

**Product and principal findings.** The paper produced a final reported and estimated Danish EQ-5D-5L value set for all 3,125 health states, which the authors recommend for Danish decision makers. The authors selected the heteroscedastic censored hybrid cTTO-DCE model because it removed logical inconsistencies in the separate models. Its predicted range was -0.757 to 1. Anxiety/depression had the largest decrement, followed by pain/discomfort. The 5L value set had 22% of states below zero, compared with 20% for the 3L set and 11% for the crosswalk.

**Interpretation, implications, limits, and gaps.** The authors linked data quality to the standardized protocol, interviewer training, and active quality control. They recommended the new value set for Danish decision-makers. They treated the recruitment-source change and remaining education and age imbalance as limits. They also stated that statistical fit is not sufficient to justify a hybrid model and called for more work on its utility-theory foundation. Cross-country value differences and dimension rankings limit transfer of foreign value sets. These are author-reported interpretations and implications, not documented policy effects.

**Reuse.** The paper used the standard EQ-VT design and compared existing Danish 3L and crosswalk products. It did not report reuse of the present participant sample.

### 2. `10.1007/s11136-020-02688-y`

**Aim and family.** Evidence synthesis with a measurement-property focus. The paper summarized evidence on EQ-5D-5L psychometric properties and sought evidence gaps.

**Review component.** The authors searched PubMed/MEDLINE, PsycINFO, EMBASE, and the EuroQol website through January 2019. Two reviewers independently screened records with consensus and senior adjudication. Eligibility was limited to humans aged 18 years or older, English or German reports, official EQ-5D-5L versions, and studies that evaluated measurement properties. The review included 99 publications from 32 countries after screening 889 identified publications. It excluded experimental 5L versions and ordinary application studies without an explicit psychometric aim.

**Instrument role and scope.** The official adult EQ-5D-5L descriptive system was the review target. EQ VAS was outside the main scope because source studies did not always identify its version. The review treated EQ-5D-5L index values and individual dimensions as separate components. Other generic, condition-specific, clinical, and global measures served as comparators or anchors in included studies.

**Property and synthesis methods.** Extracted properties were missingness, response distributions, ceiling and floor, test-retest reliability, content validity, construct validity, known-groups validity, convergent validity, and responsiveness. Internal consistency was excluded as not relevant to the preference-based EQ-5D structure. The authors pooled full-health proportions, mean index values, and correlations with random-effects models. Other results received structured narrative synthesis. When multiple papers used one underlying data set, the authors extracted the data once.

**Principal findings.** Missingness and worst-response floor effects were generally not problematic. Eight of nine reliability papers reported excellent index agreement, but individual dimensions were less stable, especially pain/discomfort in some studies. Index values had the strongest pooled correlations with other multi-attribute utility, physical or functional, and pain measures. Correlations were weak with life satisfaction and cognition or communication measures. Known-groups evidence generally distinguished disease, severity, symptoms, age, and education. Fifteen studies assessed responsiveness; moderate effects occurred mainly in groups expected to improve, but methods and anchors were heterogeneous. General-population ceiling effects remained large.

**Interpretation, implications, limits, and gaps.** The authors concluded that the instrument was reliable and valid across many populations and settings. They advised use of condition-specific measures with EQ-5D-5L where the five dimensions have weak relevance. They called for rigorous responsiveness work, suitable anchors and minimally important differences, assessment in less-studied regions and uses, and study of how value-set choice changes responsiveness. The review did not assess valuation methods, experimental versions, or psychometric information in application-only studies. Those exclusions limit the conclusion.

**Reuse.** The review identified linked publications from the Multi-Instrument Comparison data set and a 3L-to-5L mapping data set and prevented duplicate extraction. This is evidence reuse inside the review corpus.

### 3. `10.1007/s11136-025-03983-2`

**Aim and family.** Research-infrastructure and data-resource description, with population-health and instrument-comparison purposes. EQ-DAPHNIE aimed to create comparable general-population data across countries and to support population-health assessment and comparison of health and wellbeing measures.

**Components.** The paper describes a United Kingdom pilot, round 1 in Australia, Canada, New Zealand, the United Kingdom, and the United States, and round 2 in Argentina, Brazil, Chile, China, France, Germany, Japan, Mexico, the Netherlands, and Spain. Each country is a component because language, sample, bolt-ons, and the non-EQ instrument set vary. The pilot collected 3,012 completed surveys. Round-1 country samples ranged from 4,505 to 5,040. Round-2 samples ranged from 4,502 to 4,537. Later regions and longitudinal or serial follow-up were planned.

**Evidence roles and sampling.** Adults aged 18 years or older in Dynata online panels supplied self-reported evidence. Quotas used age, sex, income, urban or rural residence, and language where applicable. Enrollment was first come, first served within quotas. The target was 4,500 complete responses per country, with at least 85% adherence to each quota after possible relaxation at week five. Post-stratification weights were planned. The self-report referent was the respondent. In the response-scale heterogeneity vignette, the referent was the hypothetical person Alex, imagined with the respondent's age and background.

**Administration and survey design.** The cross-sectional survey used LimeSurvey 5+ and Dynata panels. It took about 20 minutes and had about 50 screens. The core sections covered social determinants, health and wellbeing, health behaviors, and health-service and insurance use. EQ-5D-5L came before the Alex vignette. Other health measures were randomized. Age and marital status were repeated as consistency checks. Questions were optional, and conditional display reduced burden. The team used a 250-response soft launch, usability tests, attention and consistency checks, and other quality controls.

**Instrument involvement.** EQ-5D-5L was administered in all countries. Country components then used different combinations of EQ-5D-5L bolt-ons; EQ-HWB long or short form; PROMIS-10; ASCOT-SCT4 or ICECAP-A; WHO-5; OPQOL-brief for people aged 65 years or older; PHQ-2; and GAD-2. The pilot used EQ-HWB long form and 9-item PHQ and 7-item GAD versions rather than the later two-item forms. The exact core-measure combinations were:

| Component | EQ-HWB | PROMIS-10 | ASCOT | ICECAP-A | WHO-5 | OPQOL-brief | PHQ/GAD |
|---|---|---|---|---|---|---|---|
| UK pilot | Long | No | No | No | No | No | 9-item/7-item |
| Australia, Canada, United States | Short | Yes | Yes | No | Yes | Yes | PHQ-2/GAD-2 |
| New Zealand, United Kingdom round 1 | Long | Yes | Yes | No | No | Yes | PHQ-2/GAD-2 |
| Argentina, Chile, China, Mexico, Spain | Long | Yes | No | Yes | Yes | Yes | PHQ-2/GAD-2 |
| Brazil, France | No | Yes | No | Yes | Yes | Yes | PHQ-2/GAD-2 |
| Germany | Long | Yes | Yes | No | Yes | Yes | PHQ-2/GAD-2 |
| Japan | Long | No | Yes | No | Yes | Yes | PHQ-2/GAD-2 |
| Netherlands | No | Yes | Yes | No | Yes | Yes | PHQ-2/GAD-2 |

Bolt-ons were absent in round 1 and varied in round 2: skin irritation and self-confidence in Argentina, Chile, Mexico, and Spain; vision, hearing, breathing, sleep, tiredness, social relationships, self-confidence, and cognition in China; social relationships, skin irritation, and self-confidence in Germany; cognition in Japan; and those eight China bolt-ons plus skin irritation in the Netherlands. The instrument-country relation is necessary for correct retrieval.

**Languages.** The survey was available in English and translated into Spanish, French, Portuguese, Japanese, Simplified Chinese, Dutch, and German. Standardized translations came from instrument developers when available. Native speakers reviewed local wording. Country-specific questions could be adapted while the team sought cross-country comparability.

**Product and interpretation.** The product is an operational multi-country survey infrastructure and a set of collected cross-sectional data resources. It is not a value set or a report of instrument performance. The authors expected the resource to support population-health norms, cross-country comparison, instrument evaluation, and public-health decisions. They identified online-panel coverage, cultural response differences, and one-time cross-sectional measurement as limits. They proposed other sampling modes, longitudinal subsets, and repeated panels as future work.

**Reuse.** The paper reports a reusable infrastructure and shared core protocol. It also reuses official instrument language versions. It does not report reuse of one participant sample across countries.

### 4. `10.1017/s0266462326103602`

**Aim and family.** Reported-use, policy, and practice study. The paper surveyed HTA practitioners about current use of HRQoL instruments, preference-elicitation methods, preference sources, data-quality problems, and research needs for QALY evidence.

**Evidence roles and design.** The evidence suppliers were 238 HTA practitioners from 65 agencies in 45 countries. The referents were the respondents' own work experience and views, not patient health. The intended context was national-level HTA and cost-effectiveness analysis. The sample covered six regions. Purposive, network-based recruitment targeted personnel involved in reviewing, producing, or using QALY evidence. Respondents were not official agency representatives, and the survey did not retain an agency identifier for analysis.

**Administration and analysis.** The cross-sectional Qualtrics survey was in English, with open responses allowed in another language. It ran from April 2023 to January 2024 and was designed for completion in no more than 20 minutes. Questions covered utility instruments, elicitation methods, preference data sources, data quality, and research topics. Four-point frequency responses were summarized first at country level and then by region. Research-priority scores were also aggregated through country and region levels. Open responses received translated, iterative content analysis.

**Instrument and method roles.** EQ-5D, EQ-5D-Y, SF-6D, AQoL, HUI, CHU9D, EQ-HWB, QLU-C10D, FACT-8D, PROPr, and bolt-ons were objects of reported use or opinion. They were not administered as patient outcome measures. TTO, VAS, standard gamble, DCE, best-worst scaling, and PTO were also objects of reported practice. This role distinction prevents false retrieval as a valuation study.

**Comparisons and findings.** The main comparisons were between six regions, elicitation methods, instrument types, and local versus foreign or patient versus general-public preference sources. EQ-5D was reported “very often” and was the most frequent utility instrument. SF-6D and EQ-5D-Y followed. TTO, VAS, and standard gamble were the most frequent elicitation methods. Respondents used another country's general-public preferences more often overall than local public preferences, but Western Europe and Commonwealth countries more often used local preferences. Poor sample representativeness, small samples, mismatched data, and mixing data from different instruments or methods were frequent quality concerns. The global priority order was newer tariffs, child and adolescent instruments, and instruments that cover both health and social care. Regional priorities differed.

**Interpretation, implications, limits, and gaps.** The authors interpreted the results as evidence of data scarcity and uneven local preference resources. They recommended sustained engagement between instrument developers and HTA agencies, more local and recent utility evidence, child measures, and public utility-data repositories. Network recruitment through EuroQol members can over-represent familiarity with EuroQol. Some countries had very few responses. Individual views cannot be treated as formal agency policy, respondent eligibility was not independently verified, and the study was not powered for fine subgroup comparisons. The paper reports research priorities, not adoption or policy effects.

### 5. `10.1007/s11136-019-02115-x`

**Aim and family.** Instrument development or revision, with multilingual label development and comprehension testing. The aim was to extend the EQ-5D-Y-3L descriptive system, compare four-level and five-level candidate forms, and produce an understandable youth instrument for ages 8–15 years.

**Components.** Phase 1 contained a review of child HRQoL instruments, two age-specific focus groups per country, and individual sorting or response-scaling interviews. Phase 2 tested draft 4L and 5L instruments by cognitive interview. A final harmonization component compared the German, Spanish, Swedish, and UK English forms. Phase relations are important: candidate sources informed label pools; child judgments informed draft instruments; cognitive tests informed wording; harmonization produced the final language forms.

**Participants and evidence roles.** Children and adolescents aged 8–15 years supplied wording, severity, comprehension, and form-preference evidence. Phase-1 participants came from schools, sports clubs, and the general population. Sorting used children aged 8–10 years and response scaling used those aged 11–15 years. There were 255 sorting or scaling interviews across Germany, Spain, Sweden, and the United Kingdom. Phase 2 included 120 participants: Germany 33, Spain 35, Sweden 32, and United Kingdom 20. Germany, Spain, and Sweden included both healthy children and children receiving care for a condition. The UK component used school pupils only and tested only the 5L candidate.

**Instrument roles, methods, and administration.** EQ-5D-Y-3L was the source instrument. Existing generic and condition-specific measures, dictionaries, thesauruses, and focus-group language supplied candidate labels. Younger children sorted labels on a five-face scale. Older children used a VAS, with country-specific scale direction or range documented in the source. Labels were selected with severity location, agreement, dispersion, comprehension, and everyday-language criteria. Phase 2 used self-completion, paraphrasing, probing, and thematic content analysis. Draft 4L and 5L forms were compared in randomized order in Germany, Spain, and Sweden. The UK used group discussion and written comprehension tasks.

**Product and findings.** The paper produced self-report EQ-5D-Y-5L descriptive systems in German, Spanish, Swedish, and UK English. The UK English form was proposed as the source for later translations. The product was tested for comprehension and feasibility, but it was not yet tested for measurement properties or valuation. Children generally found both candidates easy. The reported preference for 5L was Germany 88%, Spain 68%, and Sweden 66%. Children valued its precision, extra severe-health options, and middle category. The UK replaced “terrible” with “extreme” after comprehension problems and a small confirmation exercise. Harmonization retained some non-literal language differences when child evidence supported them.

**Interpretation, implications, limits, and gaps.** The authors concluded that direct child involvement and language-specific development were necessary and that inserting two translated labels mechanically would not have been sufficient. Convenience samples were not nationally representative. The UK and Spain procedures differed in small ways from the common protocol, and recruitment of children with health conditions was difficult. Required future work included measurement-property testing, validation in health-condition groups, proxy forms, more language versions, and valuation feasibility.

**Extraction uncertainty.** The abstract reports a country preference range of 68% to 88%, while the result text reports Sweden at 66%. Preserve the country values and flag the abstract range as inconsistent.

### 6. `10.1007/s40273-022-01216-9`

**Aim and family.** Valuation and value-set development for EQ-5D-Y-3L in China, with a statistical-model comparison. The study expanded the international cTTO design to test how cTTO data and a worst-state gap affect value-set estimation.

**Components and evidence roles.** Independent DCE and cTTO samples supplied two preference data types. Adult Chinese general-population respondents valued health for a hypothetical 10-year-old child. The relationship to the child was not specified. The intended result population was Chinese children and adolescents, and the intended use was pediatric economic evaluation and HTA.

**Selection and flow.** Quotas covered gender, age, education, and rural or urban registered residence. Non-probability snowball and purposive recruitment occurred in 14 provinces or cities across five geographic parts of China. Eligibility required Chinese citizenship, at least five recent years in China, consent, quota fit, and no earlier EQ-5D valuation participation. The study analyzed 1,476 participants: 1,058 DCE and 418 cTTO. cTTO data came from eight recruitment regions, while DCE data had wider coverage.

**Tasks and administration.** EQ-5D-Y-3L was the preference-elicitation health-state system and product target. EQ-VT supported face-to-face, one-to-one, computer-assisted interviews. DCE was the main source for relative dimension and level preferences. Its Bayesian efficient design had 150 pairs in ten blocks, two-dimension overlap, level balance, and no dominance or retest pair. Each respondent completed 15 pairs. cTTO provided QALY anchoring. Its expanded design had 28 states in three ten-state blocks, with 33333 in every block. Each respondent completed five practice states before the formal states. Adult respondents valued an unspecified hypothetical 10-year-old. cTTO interviewers received two-day training and repeated quality feedback; DCE interviewers received two-hour online training without the same quality-control process.

**Models and comparisons.** One route fitted a correlated mixed logit model to DCE data and mapped its latent values to observed cTTO means with ordinary least squares. The other jointly fitted DCE and cTTO in a heteroscedastic hybrid model. The paper compared main-effects models with a hybrid that added an `A3` term for state 33333. Selection criteria were coefficient significance, monotonicity, and mean absolute prediction error for observed cTTO state means.

**Product and findings.** The paper produced an estimated and author-recommended Chinese EQ-5D-Y-3L value set. The hybrid model with `A3` was selected because all main coefficients were significant and monotonic, prediction error was lowest, and it reproduced a negative value for 33333. Observed cTTO means ranged from 0.924 for 11112 to -0.088 for 33333. The authors found a marked gap between 33333 and the next-worst observed state. DCE and cTTO models also produced different rankings for some dimensions, which suggests task-dependent preference emphasis.

**Interpretation, implications, limits, and gaps.** The authors stated that the value set can support pediatric economic evaluation in China. They cautioned that lead-time TTO places the impaired child state at adult ages and proposed research on lag-time TTO. Other gaps were the cause of the 33333 discontinuity, effects of child age and respondent-child relationship, adolescent preferences, and consequences of switching between youth and adult value sets. Limits include cTTO coverage in only eight sites and an unspecified relationship to the imagined child. The latter produced varied respondent interpretations.

**Extraction uncertainty.** A key-point statement says that the sample represented four regions. The methods give 14 provinces or cities across five geographic parts, with cTTO in eight sites. Preserve the detailed methods statement and flag the key-point count as inconsistent.

### 7. `10.1007/s11136-025-04003-z`

**Aim and family.** Measurement-property study and response-scale method study. It compared frequency and severity scales for physical pain and discomfort in experimental EQ-HWB data.

**Evidence reuse and population.** This was a secondary analysis of an existing cross-sectional dyadic survey. The data contained 504 unpaid adult caregivers and their 504 linked adult care recipients. Both members self-reported their own health. The dyad structure described data provenance, but the analysis treated people as individuals and did not compare caregiver with recipient outcomes. Recruitment used a Qualtrics caregiver panel and sequential same-session completion without discussion.

**Instrument roles and administration.** Experimental EQ-HWB/EQ-HWB-S pain-frequency, pain-severity, discomfort-frequency, and discomfort-severity items were the targets. Their recall period was the last seven days. EQ-5D-5L pain/discomfort, with a “today” recall period, was a convergent comparator. EQ-5D-5L and EQ-HWB were web self-completed in randomized instrument order. Other caregiver measures were collected but were outside the focused analysis. Self-reported chronic conditions defined clinical subgroups.

**Property methods.** Spearman correlation tested association among the five pain and discomfort items. Shannon evenness assessed response-category informativity. A graded-response item-response model estimated discrimination and thresholds on a common trait. Ordinal logistic regression plus item-response estimates tested differential item functioning between frequency and severity scale forms. Separate ordinal logistic models related scale responses to age, gender, and condition. This combination distinguishes association, information spread, trait precision, differential response behavior, and condition association.

**Comparisons and findings.** Frequency versus severity was the main response-scale contrast. Pain versus discomfort and EQ-HWB versus the EQ-5D composite item were secondary contrasts. Pain frequency and severity correlated strongly. Frequency scales used response categories more evenly and gave more information at mild to moderate trait levels. Severity scales discriminated better at higher trait levels. Differential functioning was substantial for pain but negligible for discomfort. The EQ-5D composite item related more strongly to EQ-HWB pain than to discomfort. Some conditions showed different response patterns.

**Interpretation, implications, limits, and gaps.** The authors concluded that frequency and severity are complementary. They suggested both for a long instrument and frequency for a short instrument when broad informativity is the priority. They did not propose condition-specific scale forms because that would require multiple value sets and reduce cross-condition comparability. They called for research on recall-period effects and replication across clinical, cultural, and linguistic populations. Cross-sectional data, self-reported diagnoses, and limited cultural coverage were reported limits. The recommendation is not a documented change to EQ-HWB licensing or content.

### 8. `10.1007/s11136-025-04038-2`

**Aim and family.** Content-validity and concept-elicitation study with instrument-framework comparison. It elicited a Chinese lay concept of quality of life and tested the comprehensiveness aspect of EQ-HWB content validity.

**Components and evidence roles.** Thirty Chinese adults took part: ten healthy people, ten patients, and ten informal caregivers. Quotas sought diversity in age, gender, education, medical condition, and rural or urban registration. Participants came from two regions. They supplied their own concepts and examples of quality of life. The study did not ask caregivers to proxy-report another person's quality of life.

**Qualitative methods.** One trained interviewer conducted face-to-face, semi-structured interviews in Chinese. The topic guide used open concept elicitation, self-rating, poor-quality-of-life examples, and participant confirmation of an interview summary. Two coders analyzed verbatim Chinese transcripts in NVivo with a thematic framework method. The initial deductive codebook came from 96 EQ-HWB candidate items, and inductive codes captured new outcomes. Codes were filtered with explicit present, person-level, outcome-focused criteria. The team then grouped codes into subthemes and themes and compared the result with the EQ-HWB framework. Data saturation was judged subjectively after repeated content in the final interviews.

**Instrument role and content-validity scope.** The EQ-HWB conceptual framework was the comparator and source for deductive codes. The EQ-HWB questionnaire was also completed as part of eligibility, but this paper did not test its score or measurement properties. The content-validity aspect was comprehensiveness only. Relevance and comprehensibility were reserved for later work.

**Product and findings.** The paper produced a Chinese lay quality-of-life framework from 187 retained codes, 57 subthemes, and eight themes: feeling and emotion, cognition, self-identity, coping, physical sensation, relationship, activity, and mindset. Seven of eight themes aligned with EQ-HWB. Mindset was an additional theme. Several additional subthemes included regret, boredom, stress, emotion management, cognitive impairment, self-assessment, adaptation, weakness, appetite, appearance, relationship formation, judgment, and betrayal. Sleep and boredom were assigned to different parent themes in the two frameworks. The authors judged these differences insufficient to undermine EQ-HWB comprehensiveness in China.

**Interpretation, implications, limits, and gaps.** The authors linked mindset and some wording differences to Chinese cultural concepts and warned that translation and cultural adaptation must address differences in connotation. The Harbin part of the sample was young, healthy, and educated. Patients mainly had community-managed chronic conditions. No formal saturation criterion was set, and some Chinese concepts lacked direct English equivalents. Future work should include more severe and hospitalized populations and should address relevance and comprehensibility.

**Extraction uncertainty.** The source states a 68% subtheme alignment and writes “18/57.” Those values do not agree arithmetically. The source also describes the framework as almost fully represented in EQ-HWB while it lists several extra subthemes. Preserve the qualitative conclusion and flag the numeric alignment as unresolved.

### 9. `10.1016/j.jval.2025.02.001`

**Aim and family.** Evidence synthesis. The review topic was statistical method use in randomized clinical trials that analyzed treatment effects on EQ-5D outcomes.

**Review methods and scope.** MEDLINE and EMBASE were searched from inception through 15 November 2021. ClinicalTrials.gov was searched on 16 August 2023, and linked publications were sought in PubMed. Eligible records were English-language RCT reports or HTA reports with postbaseline EQ-5D analyses by treatment group. Pilot studies, feasibility studies, reviews, editorials, and conference abstracts were excluded. QALYs and quality-adjusted time outcomes were excluded because they combine time and quality of life. Screening was duplicate and independent. Multiple reports were linked to one trial by registration number, indication, treatment, and sample size. The final review contained 2,125 unique trials.

**Instrument-component roles.** EQ-5D dimension responses, EQ VAS, and derived utilities were separate review targets. Utilities were classified as numerical or categorical. EQ VAS was treated the same way. Dimension responses could be multilevel, binary, or incorrectly treated as numerical in source trials. The review did not administer an instrument and did not estimate clinical treatment effects.

**Method taxonomy and comparisons.** The authors grouped analysis into descriptive, bivariate, and multivariable methods. Linear and logistic models were split into fixed and mixed effects. Generalized estimating equations and survival analysis were separate. Results were stratified by EQ-5D component, variable format, and one versus multiple postbaseline measurements. Baseline adjustment, model-assumption checks, missing-data assessment, imputation, and use of a minimally important difference were recorded.

**Principal findings.** EQ-5D was a primary endpoint in only 131 trials, a secondary endpoint in 1,219, and exploratory in 775. Utility was analyzed in 1,592 trials, EQ VAS in 1,197, and dimensions in 385. Numerical utility and EQ VAS dominated. Linear fixed-effect models were most frequent for one postbaseline utility observation. Linear mixed-effect models were most frequent for multiple postbaseline observations. Only 221 of 2,054 trials with numerical EQ-5D reported assumption checks, and 438 adjusted for baseline EQ-5D. Missing data were explicitly assessed in 661 trials. Of these, 347 imputed, most often with multiple imputation or last observation carried forward. Dimension-level analysis was uncommon.

**Interpretation, implications, limits, and gaps.** The authors concluded that method choice varied and that many reports lacked baseline adjustment and suitable missing-data work. They noted that utility distributions can be skewed, discrete, and bounded, which can violate linear-model assumptions. They also noted that utility combines a health profile with a value set, while dimension responses can reveal different treatment effects. They called for method comparison, estimand-based analysis choices, and analysis guidance. Sparse reporting can cause undercounting of covariates, assumptions, and missing-data methods. The long search period combines changing practice over time. No trial quality appraisal was done because the review target was method use, not treatment-effect evidence.

**Reuse.** Multiple publications and registry results were linked to unique trials to prevent double counting. This is explicit review-level evidence reuse handling.

### 10. `10.1007/s10198-025-01770-x`

**Aim and family.** Measurement-property study. It compared EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D in Brazilian children and adolescents with and without self-reported musculoskeletal pain.

**Population and components.** Schools in urban São Paulo supplied 356 participants aged 8–18 years. Of these, 181 met the paper's PIP-Kids definition of musculoskeletal pain that affected activities or school, and 175 reported no musculoskeletal pain. Participants with pain from trauma, sports injury, surgery, or specified disease causes were excluded. Baseline and seven-day retest were separate components. The retest reliability analysis included 231 children whose PIP-Kids pain classification was stable: 96 with pain and 135 without pain.

**Instrument involvement and administration.** Official Brazilian-Portuguese self-complete EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D were target instruments. EQ VAS was analyzed as a separate component of each EQ-5D-Y form. PedsQL 4.0 was a convergent comparator. PIP-Kids defined pain groups and stability. A 0-to-10 numerical pain rating supported pain-severity groups. All were paper self-completed in classrooms. The order of the two EQ-5D-Y versions was randomized, but they remained consecutive. EQ-5D-Y and CHU9D referred to “today”; PIP-Kids and PedsQL used the last month.

**Property methods.** Missingness and completion assessed feasibility. Full-health profiles and item distributions assessed ceiling and floor. Seven-day kappa and agreement assessed descriptive-system reliability and error. Intraclass correlation, standard error of measurement, and smallest detectable change assessed EQ VAS reliability and error. Prespecified correlation hypotheses with PedsQL and CHU9D tested construct validity under COSMIN criteria. Pain versus no-pain and pain-severity comparisons tested known-groups validity.

**Principal findings.** Missingness was generally low, but EQ-5D-Y-5L usual activities had 12.7% missing data. Completion was highest for EQ-5D-Y-3L and lowest for PedsQL. In the pain group, full-health ceiling was 18.2% for EQ-5D-Y-3L and 16.0% for EQ-5D-Y-5L; CHU9D had 5.5% at its full-health profile. Descriptive-system test-retest reliability was poor to moderate. EQ VAS reliability was substantial in the pain group and moderate in the no-pain group. In the pain group, both EQ-5D-Y versions met the prespecified construct-validity criterion against PedsQL. EQ-5D-Y-5L met the criterion against CHU9D in both groups. All three instruments distinguished pain from no pain. Most EQ-5D-Y dimensions and some CHU9D dimensions distinguished pain severity.

**Interpretation, implications, limits, and gaps.** The authors stated that all three measures can support research and clinical assessment, especially for musculoskeletal pain, and linked EQ-5D-Y-3L utilities to Brazilian economic evaluation. Reliability and construct validity were better in children with pain. The pain definition was self-reported and heterogeneous, not a clinical diagnosis. Different recall periods can explain why 36% of the pain group reported no current pain on the target instruments. The study did not test comprehension time, responsiveness, utility-score properties, or children younger than eight. Consecutive EQ forms can cause recall or confusion. There is no gold-standard HRQoL measure for this context. The authors called for other conditions, settings, younger ages, proxy forms, utility-based analysis, and responsiveness work.

**Extraction caution.** The conclusion's broad statement that all instruments had good feasibility and validity must be read with the specific results: descriptive-system reliability was poor to moderate, and several construct-hypothesis comparisons did not reach the prespecified threshold.

## Applications to batch 02

### 11. `10.1016/j.jval.2025.01.003`

**Aim and family.** Valuation and value-set development. The paper developed an EQ-5D-5L value set from preferences of the adult general population of the United Arab Emirates. It also compared cTTO-only, DCE-only, and hybrid statistical models.

**Components and evidence roles.** Adult residents supplied preferences for hypothetical EQ-5D-5L health states. They also self-reported their own health. The intended preference population was the UAE adult general population, including nationals and expatriates. The intended decision context was UAE cost-utility analysis, HTA, population-health assessment, and health-system use. Language and interview-mode checks were subordinate comparisons, not independent samples.

**Selection and flow.** Recruitment used emirate, age, and sex quotas, then interviewer networks, snowball recruitment, public locations, posters, and social media. Eligibility required age 18 years or older and either UAE nationality or at least five years of UAE residence. Interviews could be in Arabic or English. The target was 1,150 people. The team conducted 1,145 interviews and excluded 140 practice interviews from the first six weeks. The analysis used 1,005 respondents, 10,050 cTTO responses, and 7,035 DCE responses. Nationals were 11.4% of the analyzed sample and expatriates were 88.6%.

**Instrument, tasks, and administration.** EQ-5D-5L was the health-state system and product target. Respondents first self-reported their health with the descriptive system and EQ VAS. The study used the UAE Arabic EQ-5D-5L and the UK English form because no UAE English form was available. EQ-VT supported interviewer-administered computer tasks in face-to-face or online interviews. Each respondent completed ten cTTO states and seven duration-free DCE pairs. cTTO used conventional TTO for states better than dead and lead-time TTO for states worse than dead. A feedback module, interviewer training, practice rounds, weekly or biweekly review, and three interim pauses supported quality control. The study combined languages and modes after its checks found small quality differences.

**Models and product.** Ten candidate models covered random-intercept, Tobit, heteroskedastic, DCE conditional-logit, and hybrid specifications. Sensitivity analyses excluded values with `55555` inconsistencies, feedback flags, or both. Leave-one-state and leave-one-block cross-validation tested prediction. The authors selected a heteroskedastic hybrid Tobit model censored at -1 because it used both data types, treated cTTO censoring, remained logically consistent, and performed well on the stated fit measures. The product was a final reported, estimated, and author-recommended UAE EQ-5D-5L value set.

**Principal findings.** Predicted values ranged from 1 for full health to -0.654 for `55555`; 15.3% of predicted states were below zero. Mobility had the largest decrement, followed by pain/discomfort and anxiety/depression. Sensitivity exclusions did not materially change the result. Online and face-to-face data also gave similar quality results in the paper's checks.

**Interpretation, limits, and gaps.** The authors stated that the value set can support local economic evaluation and resource-allocation decisions. They did not document adoption or a policy effect. The use of UK English health-state wording in the UAE and the untested five-year residence rule limit interpretation. Language can also mark different nationality and lived experience rather than cause a language effect. The paper calls for work on expatriate experience, the definition of a general population in a mobile country, value-set update timing, and broadly usable language forms.

**Extraction uncertainty.** The abstract reports mean age 39 years with SD 10.8. The results report mean age 32.1 years with SD 11.4. Preserve both statements. The authors call the sample representative by age, sex, and geography, but the table shows material differences from the population values for sex and several emirates. Preserve the selection method and distributions instead of a binary representativeness label.

### 12. `10.1016/j.jval.2024.05.016`

**Aim and family.** Preference-elicitation method study. It directly compared EQ-VT cTTO and duration-free DCE estimates with split-triplet DCE with duration, or DCEd, for EQ-5D-5L in Trinidad and Tobago. It also tested linear against nonlinear time-preference specifications for DCEd.

**Components and evidence roles.** Two independent adult general-population samples supplied preferences for the same EQ-5D-5L health-state system. The EQ-VT sample and DCEd sample were not the same people. EQ-VT data were collected from June to September 2022. DCEd data were collected from November 2022 to June 2023. The intended use was a less costly valuation method that can produce QALY-scale values.

**EQ-VT component.** A panel company sampled people to represent age, sex, and geography. Eleven trained interviewers completed in-home face-to-face interviews with 1,079 respondents. Each respondent completed ten cTTO states from the standard 86-state design and 12 DCE pairs without duration. The DCE design used two-dimension overlap. The study used interviewer training and the EQ-VT quality-control protocol. Analyses used a heteroskedastic cTTO Tobit model, a rescaled mixed-logit DCE model, and a heteroskedastic hybrid Tobit model.

**DCEd component.** Of 1,581 completers, 611 were excluded and 970 entered analysis. Each analyzed respondent completed 18 split-triplet tasks. The first choice compared two EQ-5D-5L states at equal duration. The next choice compared one of those lives with a shorter life in full health; three tasks used immediate death instead. The durations included six months and positive integer years up to 15. A near-orthogonal design supplied initial estimates. The team then updated the Bayesian efficient design three times after batches of 200 respondents. Respondents self-completed the LimeSurvey task after examples and warm-up tasks. Online panel participation remained in the analysis. Public-place laptop collection stopped after high speeding and flatlining, and all data from that route were removed. The primary speed rule was a mean below 12.5 seconds per split triplet, with 10- and 15-second sensitivity checks.

**Comparison and findings.** Linear and nonlinear mixed-logit DCEd models differed materially. The linear model predicted `55555` at -1.214. The nonlinear model, which estimated a 23.5% time-discount rate, predicted it at -0.543. The EQ-VT models predicted `55555` from -0.611 to -0.563. The nonlinear DCEd estimates correlated from 0.954 to 0.973 with EQ-VT model estimates across all 3,125 states. Mean absolute differences were 0.083 against cTTO, 0.051 against rescaled DCE, and 0.060 against the hybrid model. DCEd gave slightly higher values in the middle of the scale. It predicted observed cTTO state means less closely than the EQ-VT models.

**Interpretation, limits, and gaps.** The authors interpreted nonlinear DCEd as a possible cheaper substitute for EQ-VT. This is a conditional method implication, not evidence of interchangeability in routine valuation. The evidence comes from one country, independent samples, different modes, a collection-time gap, and different education and ethnicity distributions. The DCEd method cannot easily distinguish strong duration preferences from inattentive flatlining. More comparisons across cultural, language, and sampling settings are required. The estimated discount rate is a correction for the valuation model, not a recommended HTA discount rate.

### 13. `10.1186/s12955-023-02177-z`

**Aim and family.** Prospective measurement-property study. It assessed EQ-5D-5L convergent validity, test-retest reliability, response distributions, and responsiveness in adults with relapsed Graves' disease in Hong Kong.

**Population, flow, and components.** A convenience sample was recruited from endocrinology and surgical outpatient clinics at three public hospitals. Adults had relapsed Graves' disease and could read Chinese or English. Pregnancy and cognitive impairment were exclusions. Of 125 baseline participants, 101 completed one month and 100 completed six months. The reliability component used 64 people who reported unchanged health at one month. The responsiveness component used 21 people who reported worsened health, 38 unchanged, and 41 improved at six months. These analysis stages must not be replaced by the baseline count.

**Instrument roles and administration.** Participants self-completed EQ-5D-5L and ThyPRO-39 at baseline. They completed online follow-up questionnaires at one and six months. The EQ-5D-5L descriptive system, Hong Kong value-set index, and EQ VAS were separate targets. ThyPRO-39 overall quality-of-life impact and composite scores were convergent comparators. A self-reported global change question at six months was the responsiveness anchor. Mandatory online questions prevented item missingness among follow-up completers.

**Property methods and findings.** Baseline best-health profiles tested ceiling: 28.0% reported `11111`, while 5.6% reported EQ VAS 100. Prespecified Spearman correlations tested convergent validity and were moderate to strong between EQ-5D index or EQ VAS and ThyPRO-39 summary scores. One-month dimension agreement used weighted Gwet AC2 and percentage agreement. Index and EQ VAS reliability used a two-way random-effects, absolute-agreement ICC. Dimension agreement was substantial to almost perfect, while index and EQ VAS ICCs were about 0.70 and classified as moderate. Six-month Wilcoxon tests, standardized effect size, and standardized response mean tested change. EQ VAS showed large worsening effects, and the index showed small-to-moderate or moderate worsening effects by the two statistics. Neither outcome showed clear responsiveness to reported improvement.

**Interpretation, limits, and gaps.** The authors support use of EQ-5D-5L with a disease-specific measure in Graves' disease. The result is conditional by component and direction: responsiveness was present for worsening but not improvement. Baseline ceiling, small change groups, one-month stability defined only by self-report, 20% attrition, and recruitment from three public-hospital clinics limit transfer. The authors call for larger studies of improvement and the meaningful size of score change.

**Extraction caution.** The discussion calls the index and EQ VAS worsening effects large. Under the paper's stated thresholds, the index standardized effect size of 0.66 is moderate and its standardized response mean of 0.42 is small. Preserve the two method-specific values instead of the broad label.

### 14. `10.1007/s11136-025-04150-3`

**Aim and family.** Instrument development and content-validity study. Three expert consultation groups reviewed experimental EQ-TIPS-3L version 2.0 wording and content. They also discussed intended uses and conceptual problems for HRQoL measurement in children aged zero to three years.

**Components and evidence roles.** The components were EuroQol measurement experts, pediatric health and development experts, and pediatric outcome-measure developers. The groups supplied expert judgments. They did not proxy-report the health of a child and did not supply caregiver or child comprehension evidence. The instrument target was the child. Anticipated respondents were parents or other proxies with sufficient knowledge of the child. Of 44 experts reported as invited, 33 participated: 17, 11, and 5 in the three groups. Fifteen countries were represented.

**Instrument and method.** The evaluand was the generic English experimental EQ-TIPS-3L version 2.0. It had six dimensions, three response levels, a `Today` recall period, and a proxy EQ VAS. The later five-level form was not available for this study. Three semi-structured Zoom consultations ran from December 2022 to February 2023. The groups used different topic guides because their expertise differed. Some used breakout rooms and participant checks. Two analysts applied deductive and inductive thematic analysis to de-identified verbatim transcripts. Facilitators and the wider team checked the analysis.

**Content findings and product stage.** Experts generally found the short instrument and its current wording understandable and relevant. They supported the six dimensions but recommended tests of sleep and emotion. They questioned overlap between communication and social interaction. They proposed observable, age-specific examples instead of the phrase `age-appropriate behavior`. They also discussed construct definition, response levels, recall period, child age and development, premature birth, cultural norms, translation, and proxy familiarity. The paper supplied expert-review evidence and recommendations for a future revision. It did not produce a revised EQ-TIPS form, establish content validity with intended proxies, or establish psychometric performance.

**Proxy and construct interpretation.** Experts wanted answers to describe the child's HRQoL, not caregiver burden or family spillover. They stated that proxy suitability depends on context. A clinician can be a possible proxy for a hospitalized child. Proxy characteristics and familiarity can affect answers and should be recorded. Most experts preferred the current `Today` recall for acute care or repeated measurement, but some wanted a longer period for chronic or fluctuating health.

**Limits and gaps.** Expert recruitment used researcher networks. Expertise and prior knowledge varied. Breakout rooms limited whole-group consensus. The instrument-developer group was small and concentrated in Europe and Canada. The study did not collect caregiving experience systematically. Future work must test revisions with parents and caregivers, people with lower literacy, different socioeconomic and cultural settings, varied health conditions, and the full intended age range.

**Extraction uncertainty.** The paper reports 44 invitees, but the three invited-group counts are 21, 13, and 9, which total 43. Eleven nonattenders and 33 participants agree with the overall count of 44. Preserve both source statements.

### 15. `10.1186/s41687-025-00985-z`

**Aim and family.** Translation and cultural-adaptation study with comprehension testing. It translated EQ-5D-Y-5L into Modern Standard Arabic for use in Egypt.

**Process components and relations.** The source form was UK English EQ-5D-Y-5L. The existing Egyptian Arabic EQ-5D-Y-3L supplied compatible wording where suitable. Two independent native-Arabic translators produced forward translations for paper and digital forms. The team reconciled them, and the EuroQol Version Management Committee reviewed the draft. Two independent native-English translators who had not seen the source made back translations. Comparison and committee review informed a second Arabic form. Cognitive work with children then informed revisions, three confirmation interviews, proofreading, and the final approved form.

**Participants and tasks.** Eleven Egyptian children aged 8 to 15 years supplied language and comprehension evidence. Six were girls, six were healthy, and five had chronic conditions. Recruitment was by convenience in Cairo and Menoufia and covered low-to-middle socioeconomic settings. Eight children ranked four sets of five severity labels before they saw the questionnaire. They then self-completed it and took part in detailed face-to-face debriefing. Three additional children tested revised pain wording, a digital prompt term, and EQ VAS instructions. Parents were present, but the paper does not identify them as evidence suppliers.

**Administration and findings.** The product tests covered paper and digital forms, but the cognitive task itself was face-to-face self-completion with an interviewer available. Of 160 ranked cards, ten were out of intended order. Later examples showed that the children understood the severity order. All 11 described the questionnaire as clear and easy. Six needed confirmation of the general or EQ VAS instructions. Mean completion time was 5.2 minutes. Psychological interpretations of the first pain wording caused a revision to a term that more clearly meant physical pain. All three confirmation participants understood the revised terms.

**Product and maturity.** The paper produced a final, committee-approved, comprehension-tested Modern Standard Arabic EQ-5D-Y-5L for Egypt in paper and digital forms. It did not report measurement-property results or a value set. The authors recommend an interviewer-based form for ages 8 to 10 because some younger children needed instruction support.

**Interpretation, transfer, and gaps.** The authors state that the form can be used in Egypt and possibly other Arabic-speaking countries. The discussion also states that dialect and culture differ and that other countries require local validation. Record Egypt as the tested setting and the wider Arabic region as an author-proposed transfer, not as established validation. The paper says that psychometric testing has occurred in other work, but those results are not evidence in this paper.

### 16. `10.1016/j.jval.2024.03.2195`

**Aim and family.** Measurement-property and instrument-development study. It assessed nine existing EQ-5D-5L bolt-ons and their incremental performance in a Hungarian adult general-population sample.

**Population, instruments, and administration.** An online cross-sectional survey recruited 1,700 adults with soft quotas for age, gender, residence, and region. After 113 inconsistency exclusions, 1,587 remained. Respondents self-completed fixed-order Hungarian forms. The evaluands were the EQ-5D-5L core plus cognition, sleep, social relationships, breathing, hearing, tiredness, vision, skin irritation, and self-confidence bolt-ons. All bolt-ons had five levels and a `Today` recall. PROMIS-29 v2.1, SF-6D derived from SF-36, PROMIS Global Health, and Satisfaction With Life Scale items supplied construct comparators and analysis outcomes. Physician-diagnosed conditions defined known groups.

**Property methods.** Distribution and best-health profiles assessed category use and ceiling. Spearman correlations tested overlap with EQ-5D items and convergence with similar external items. Principal-component analysis and confirmatory-factor analysis tested structural grouping. Transformed level sum scores and bootstrapped relative-efficiency ratios tested known-group discrimination. Linear models tested added explanation of EQ VAS, PROMIS Global Health, and life-satisfaction variance. Each bolt-on was tested alone and selected combinations were built stepwise. The study therefore assessed item performance and the incremental performance of an expanded descriptive system. It did not test a scored bolt-on utility.

**Principal findings.** EQ-5D-5L full-health ceiling was 41%; 77% of those at `11111` reported at least one bolt-on problem. Sleep, tiredness, vision, and self-confidence produced the largest individual ceiling reductions. Seven bolt-ons loaded on factors apart from the EQ-5D core; cognition and self-confidence loaded with anxiety/depression. Relevant bolt-ons improved group discrimination for several self-reported conditions. Sleep added discrimination in nine of 13 condition groups. Tiredness explained the most EQ VAS variance in eight of 13 groups. One or two bolt-ons usually supplied most of the gain, but no single bolt-on was best for all constructs or groups.

**Interpretation, limits, and gaps.** The authors propose the evidence for candidate selection in population or patient studies and for continued bolt-on development. It is not an author decision to add all nine items to EQ-5D-5L. Severe responses were sparse. Fixed order, a question block between core and bolt-ons, level-sum scoring, self-reported condition severity, and limited external items for some constructs restrict the findings. Valuation feasibility, resulting utilities, and comparability with existing national value sets remain unresolved. The authors call for clinical-population and item-response work.

### 17. `10.1007/s10198-018-0987-x`

**Aim and family.** Mapping and economic-evaluation method study. It tested how five SF-12-to-EQ-5D mapping functions and SF-6D utilities changed incremental QALYs and cost-effectiveness ratios relative to directly collected EQ-5D-5L in dialysis models.

**Evidence reuse and components.** This secondary analysis reran two earlier Singapore Markov models: one for people without diabetes and one for people with diabetes. It reused a cross-sectional survey of 75 people receiving hemodialysis and 75 receiving peritoneal dialysis for at least three months. Participants supplied EQ-5D-5L responses for health that day and SF-12 responses for the prior four weeks. The paper reused published transition inputs, a transplantation utility, five mapping functions, and value sets. It did not develop a new mapping function or collect a new sample.

**Outcome derivation routes.** The direct route scored observed EQ-5D-5L profiles with the England EQ-5D-5L value set. Three direct mappings used SF-12 physical and mental summary scores to predict EQ-5D-3L utilities with ordinary least squares. Two response mappings used summary scores or item responses to predict EQ-5D-3L responses, then applied the UK 3L value set. A separate route derived SF-6D from seven SF-12 items and used UK standard-gamble weights. The mapping-development samples differed from the Singapore dialysis sample. This route information is necessary because mapped and direct outcomes differ in source instrument, recall period, EQ-5D version, modeling method, and preference source.

**Decision models and comparison.** Each Markov model compared hemodialysis with peritoneal dialysis from a societal perspective over ten years in 2015 Singapore dollars. Costs and QALYs were discounted at 3% per year. Regression-adjusted mean utilities supplied dialysis-state inputs. A hypothetical cohort of 10,000 people generated incremental QALYs and ICERs. A 1,000-replicate nonparametric bootstrap represented utility-input uncertainty.

**Findings and interpretation.** Against the direct EQ-5D-5L route, mapped routes produced 14.9% to 33.2% fewer incremental QALYs and 17.5% to 49.7% higher ICERs. SF-6D also produced lower incremental QALYs and higher ICERs. The authors linked the differences to instrument content, recall, mapping-sample mismatch, prediction bias, and the 5L-versus-3L route. They recommend direct EQ-5D collection and one jurisdictional reference measure when possible. This is an author-reported decision implication, not evidence that reimbursement changed.

**Limits and gaps.** The result comes from one Singapore dialysis analysis. Direct EQ-5D-3L observations were unavailable, so the study cannot isolate mapping error from the change in EQ-5D version and value set. UK or England preferences were applied to Singapore data. Utility was treated as constant through the model horizon. The outcome direction must not be generalized to all mapping functions or populations.

### 18. `10.3389/fpubh.2021.744405`

**Aim and family.** Population-health description and health-equity study. It tested whether an EQ-5D-5L level sum score added discrimination over EQ VAS in education-related health-inequality analysis in Italy, the Netherlands, and the United Kingdom.

**Components and population.** Country components used general-population internet panels of adults aged 18 to 75 years. The samples were selected for age, gender, and education distributions. Only full questionnaire completers entered analysis. The total was 10,172: Italy 3,026, Netherlands 3,027, and UK 4,119. Participants self-reported their own health, education, income, work status, and chronic conditions. Education, classified with ISCED-97, was the study's proxy for socioeconomic status. The intended context was public-health inequality measurement.

**Instrument, outcome forms, and methods.** EQ-5D-5L and EQ VAS were web self-completed. The main comparison was not between two instruments: it was between the unweighted five-item level sum score and the single EQ VAS item. The level sum score was reversed and transformed to 0 to 100 for comparison; it was not a preference-weighted utility. ANOVA and Kruskal-Wallis tests compared education and country groups. Stratified analyses used presence and type of chronic condition. Country-specific backward-elimination regression models used education, work, income, chronic-condition count, age, and sex.

**Principal findings.** In the UK and Netherlands, lower education was associated with worse level-sum and EQ VAS outcomes. Italy did not show the same ordered pattern. Unadjusted education differences were usually slightly larger for the level sum score. Adjusted models explained 31.6% to 54.3% of level-sum variance and 17.9% to 30.6% of EQ VAS variance. Chronic-condition count and inability to work were strong predictors. Education largely lost its association after adjustment, although a small UK association remained. Condition-specific stratification did not give one consistent advantage for the level sum score.

**Interpretation, limits, and gaps.** The authors concluded that the multi-item level sum score can add some discrimination for inequality analysis. They also noted extra respondent burden. Web-panel coverage can omit people without access or sufficient literacy, and nonresponse could not be analyzed. Education is only one socioeconomic proxy. Country differences can reflect sampling, reporting, and health conditions as well as inequality. The authors used a level sum score because Italy had no 5L value set; this avoids an arbitrary foreign preference source but does not produce utility evidence.

### 19. `10.3390/curroncol32060308`

**Aim and family.** Implementation study with mixed methods. It assessed patient-perspective feasibility of routine EQ-5D-3L collection during systemic cancer treatment at one Ontario oncology center. It was a pilot for possible province-wide collection.

**Components, population, and flow.** Adults starting publicly reimbursed systemic therapy for a confirmed solid or hematologic malignancy formed a prospective convenience cohort. Staff recruited during chemotherapy visits from May to November 2024 and followed participants through February 2025. All 170 eligible and consenting participants completed an initial EQ-5D-3L. Of these, 160 completed the optional feasibility and demographic questionnaire, and 103 completed at least one EQ-5D follow-up. Fifty-seven agreed to interview contact, and nine completed an interview. Baseline, follow-up, feasibility survey, and qualitative interview are different components.

**Instrument, reporter, and administration.** English self-report EQ-5D-3L and EQ VAS were the routine-collection targets. English proxy version 1 was available for a caregiver to rate the patient's health in the caregiver's opinion, but the paper does not state how often it was used. The study offered paper and REDCap forms, and staff entered all responses into REDCap. Do not infer web self-completion from REDCap storage. A separate feasibility questionnaire asked about willingness, understanding, ease, acceptability, and length. Two-person semi-structured Zoom interviews supplied deeper patient feedback; three researchers used content analysis.

**Implementation outcomes and findings.** Follow-up retention was 60.6% of the 170 initial completers. Of 160 feasibility respondents, 115, or 71.9%, said they would definitely continue at each visit, and 35, or 21.9%, said very likely. Most respondents found the questionnaire understandable, easy, acceptable, and short. Interviews found that chemotherapy visits can provide available time but can also give a poor or rapidly changing health snapshot. Patients differed on paper against electronic collection and on preferred frequency. Small font, coordinator burden, short infusion appointments, missed contact, English-language barriers, and limited HRQoL content were barriers.

**Documented use, product stage, and implications.** The study documents pilot implementation at one oncology center. The authors provide a pilot workflow and patient-informed recommendations for timing, mode options, and scale-up. Province-wide EQ-5D collection and use of the `Your Symptoms Matter` platform remained planned. The authors recommend EQ-5D-5L for wider implementation despite testing EQ-5D-3L in this pilot. That is a future instrument choice, not documented 5L implementation.

**Limits and uncertainty.** The single-site convenience sample and high staff burden limit transfer. Only nine interviews were completed, and English barriers affected recruitment. The abstract gives willingness as 115, or 67.3%, and 35, or 20.5%, using 170 as the denominator. The results give 71.9% and 21.9% using 160 feasibility respondents. Preserve counts and denominators. The actual number of proxy completions and the actual response-mode distribution are not reported.

### 20. `10.1016/j.jval.2024.05.007`

**Aim and family.** Measurement-property study with instrument and utility-score comparison. It assessed experimental EQ-HWB-S version 1.0 against EQ-5D-5L in a UK general-population sample.

**Evidence reuse and components.** The paper combined two existing valuation-stage data sets. The E-QALY valuation source contributed 429 of 521 people who had both instruments. It used age, sex, and ethnicity quotas, EQ-HWB-S before EQ-5D-5L, and online valuation interviews from May to November 2021. The UK EQ-5D-5L pilot source contributed 248 people with both instruments. It used EQ-5D-5L before EQ-HWB-S, 81% online and 19% face-to-face interviews from October 2022 to February 2023. The combined analysis had 677 people. The source data were compatible in instrument forms and valuation-interview setting, but order, mode, period, recruitment, and some background questions differed.

**Instruments and outcome derivation.** Experimental EQ-HWB-S version 1.0 was the evaluand. EQ-5D-5L was the comparator. The study compared individual dimensions, full profiles, and utilities. EQ-HWB-S utility used its UK feasibility value set, estimated directly with TTO and DCE preferences. EQ-5D-5L utility used the NICE-recommended mapping to the UK EQ-5D-3L value set. Thus, utility agreement compares both instrument content and scoring route. Health and life satisfaction and EQ VAS defined known groups. The long-term-condition question differed between source data sets. Carer status and satisfaction were available only in the E-QALY source.

**Property methods and findings.** Best and worst response proportions assessed distributions. Spearman correlations tested convergence of dimensions, and Pearson correlations tested utilities. Conceptually overlapping mobility, activity, anxiety or depression, and pain dimensions correlated strongly. EQ-HWB-S had a 9.45% full-profile ceiling, compared with 36% for EQ-5D-5L. Bland-Altman analysis and Lin concordance tested agreement, not only association. Concordance was high overall, but individual utility differences ranged from -0.61 to 0.31 and outliers occurred across the EQ-HWB-S scale. Both utility routes distinguished health, long-term-condition, satisfaction, and employment groups. Carer and age effects were smaller.

**Interpretation, limits, and gaps.** The authors state that EQ-HWB-S performed favorably and covered loneliness, cognition, and control beyond EQ-5D-5L. They do not establish equivalence of the instruments. The combined sources differed in order, mode, data period, variable definitions, and availability. One source was collected during the COVID-19 pandemic. The EQ-5D mapping route compressed its score range. Future work should repeat utility comparisons with a new UK EQ-5D-5L value set and in clinical populations.

## Applications to batch 03

### 21. `10.3390/curroncol32110645`

**Aim and family.** Health-equity study within a real-world cancer cohort. It examined whether age, sex, education, marital status, employment, family income, ethnicity, and cancer site were associated with EQ-5D-3L utilities in Ontario. The intended decision context was equity-informed HTA and later distributional cost-effectiveness analysis.

**Evidence reuse, population, and components.** This paper is a cross-sectional secondary analysis of the initial responses from the 170-person oncology implementation pilot in paper 19. Adults were starting publicly reimbursed systemic therapy for a solid or hematological malignancy at one Toronto oncology center from May to November 2024. Patients supplied self-reports about their own health. The analysis used a full sample of 170 without birth sex as a covariate and a restricted sample of 111 that excluded breast, gynecological, and prostate cancers so that birth sex could enter the model. The earlier pilot reports 160 optional demographic-questionnaire completers. The present paper does not explain how all covariates were available for the 170-person model.

**Instrument, administration, and derivation.** EQ-5D-3L descriptive responses and EQ VAS were collected during chemotherapy appointments. The utility outcome was derived from EQ-5D-3L profiles with the Canadian TTO value set through the `eq5d` software package. The earlier pilot offered paper and REDCap response routes but did not report the route used by each participant. Do not infer web self-completion or one uniform mode. EQ VAS was administered but was not the outcome in the reported association models.

**Equity variables and methods.** Family income was an ordinal socioeconomic indicator with CAD 150,000 or more as the privileged reference. The other demographic and clinical variables were predictors or adjustment covariates, not separate populations. Ordinary least-squares multivariable models estimated associations with utility. ANOVA tested age-category-by-birth-sex interaction terms, and BIC compared nested models. Spearman correlations related reported income categories to individual dimension severity. The two sample specifications are sensitivity or scope conditions and must remain linked to their different eligibility rules.

**Principal findings.** Income below CAD 30,000 and undisclosed income were associated with lower utility in both main models. Low income also correlated with more pain or discomfort and anxiety or depression. Colorectal cancer was associated with higher utility than the head-and-neck reference group. The age-by-birth-sex interaction was not significant. These are adjusted cross-sectional associations, not causal effects of income or proof that trial utilities are biased.

**Interpretation, implications, limits, and gaps.** The authors argue that trial-based utilities can overstate the health of socioeconomically disadvantaged real-world patients and recommend consideration of real-world utilities and equity factors in HTA. They do not estimate the effect on incremental QALYs or document an HTA decision. Income was undisclosed by 79 participants, the sample was small and from one urban site, and cancer stage and comorbidities were not measured. EQ-5D-3L ceiling, model uncertainty, and the cross-sectional design further limit transfer. The authors propose longitudinal collection from diagnosis and application to distributional cost-effectiveness analysis.

### 22. `10.1016/j.jval.2018.05.002`

**Aim and family.** Preference-elicitation method and instrument-comparison study. It used a randomized 2-by-2 design to test the joint effects of descriptive-system wording, EQ-5D-3L against EQ-5D-Y-3L, and valuation perspective, the respondent's own adult health against the health of a hypothetical 10-year-old child.

**Conditions, population, and flow.** Adult general-population convenience samples in England, Germany, the Netherlands, and Spain completed computer-assisted personal interviews from May to July 2015. Recruitment was monitored for age and sex. The 805 respondents were randomly assigned to EQ-5D-3L adult perspective (205), EQ-5D-3L child perspective (195), EQ-5D-Y-3L adult perspective (194), or EQ-5D-Y-3L child perspective (211). Country collection sites differed: England used homes, while the other countries used central sites. The evidence suppliers were adults. The referent was either the respondent or an unspecified hypothetical 10-year-old, according to condition.

**Tasks and protocol.** An adapted EQ-VT protocol used a dimension-level ranking task, nine cTTO health-state tasks after examples and practice, a feedback module, and DCE comparisons that also placed health states against immediate death. cTTO used conventional TTO for better-than-dead states and lead-time TTO for worse-than-dead states. The design used 17 cTTO states in two blocks, with `33333` in both. Intensive interviewer training and the EQ-VT quality-control tool supported protocol adherence. Descriptive-system wording, referent perspective, and death framing are separate task specifications.

**Factorial analysis and findings.** Two-way MANOVA tested the wording-by-perspective interaction for cTTO values. Hotelling tests and corrected state-level tests compared arms. Chi-square tests compared DCE choices. The interaction was significant, so wording and perspective could not be interpreted as independent main effects. Perspective differences appeared for EQ-5D-3L but not clearly for EQ-5D-Y-3L, and wording differences appeared under the adult perspective. Overall, child-perspective cTTO values were higher and immediate death was selected less often. State `33333` did not differ significantly by arm. The main conclusion concerns conditional wording and perspective effects, not a universal child-versus-adult value difference.

**Contribution, interpretation, and implications.** The paper supplied method evidence that adult EQ-5D-3L value sets should not be applied to EQ-5D-Y health states. The authors propose separate youth value sets and further work on death anchoring and child perspective. They suggest that adult and child QALY comparisons can be difficult because respondents can interpret the death anchor differently. This is an author-reported decision implication, not a new value set or a changed cost-per-QALY threshold.

**Limits and uncertainty.** A technical implementation error left only one planned DCE block and prevented DCE model estimation. Pooled country analysis could not control all recruitment and cultural differences, and the adult condition used self-perspective while the child condition used another-person perspective. The exact instrument language used in each country is not stated in the available text. The protocol text and table indicate nine health-state pairs, while the design paragraph says ten pairs were implemented. Preserve the task-count conflict.

### 23. `10.1007/s40273-018-0642-5`

**Aim and family.** Evidence synthesis with a measurement-property and version-comparison focus. It consolidated adult evidence that directly or indirectly compared the official EQ-5D-3L and EQ-5D-5L descriptive systems.

**Review process and scope.** PubMed, EMBASE, PsycINFO, and the EuroQol website were searched for English or German reports from 2007 through May 2016, then updated through January 2018. Eligible primary studies and conference papers used final adult 3L and 5L forms and reported a comparative measurement property. Two reviewers independently screened titles and abstracts. One extracted full texts and another checked them. When reports used the same data, the review retained the report with more relevant information or retained both when they supplied different evidence. An adapted nine-item appraisal rated reports as poor, fair, good, or excellent.

**Evidence corpus and instrument roles.** The final synthesis contained 24 articles from 18 countries: eight general-population studies and 16 patient studies. All but two used head-to-head responses from the same people. Some studies randomized instrument order. EQ-5D-3L and EQ-5D-5L descriptive systems and their index routes were the review targets. Crosswalk-derived 5L utilities in source studies remained mapped outcomes and were not treated as directly valued 5L utilities.

**Property and synthesis methods.** The review structured missingness, dimension and profile endpoints, full-health ceiling, worst-health floor, response redistribution inconsistency, Shannon information richness and evenness, responsiveness, and test-retest reliability. It pooled full-health proportions with random-effects logit models and synthesized other results descriptively. Reliability methods included ICC, kappa, weighted kappa, and agreement. Responsiveness evidence was separated by dimension or index outcome, external change criterion, method, interval, and value-set route.

**Principal findings.** Missingness and worst-health profiles were usually below 5% for both forms. Nineteen of 22 reports with profile ceiling results found a lower ceiling for 5L. Pooled full-health proportions were 0.23 for 3L against 0.18 for 5L in patient samples and 0.53 against 0.43 in population samples. Shannon information richness was always higher for 5L, while normalized evenness gains were small. Inconsistencies were usually below 5% and were most frequent for usual activities. Index ICCs favored 5L in several studies, but dimension-level reliability had no clear winner. Only three studies supplied responsiveness evidence, and results were mixed. Crosswalk scoring affected two index-level responsiveness comparisons.

**Interpretation, limits, and gaps.** The authors conclude that 5L usually has similar or better measurement performance, with clearer gains for ceiling and informativity. They support both forms and recommend 5L when discrimination among mild states is important. Differences in populations, languages, order, intervening questionnaires, design, value sets, and analytic methods limit synthesis. Evidence remained insufficient for responsiveness and test-retest reliability. The authors call for comparative research, better reporting standards, and attention to setting, respondent, language form, and local value-set availability when a form is selected.

**Extraction uncertainty.** The flow text reports 215 full texts and 190 exclusions but then says 20 articles remained; the arithmetic would leave 25. A later update added four and the final count of 24 agrees with the abstract. Preserve the stated stages instead of repairing the flow.

### 24. `10.1016/j.jval.2023.03.003`

**Aim and family.** Preference-elicitation method and task-feasibility study. It tested whether cTTO data alone could support an EQ-5D-Y-3L value set, contrary to the international youth protocol's primary reliance on DCE with cTTO anchoring.

**Evidence reuse and population.** This is a secondary analysis of the 418-person Chinese cTTO component from paper 6. Adult Chinese general-population respondents in eight provinces or cities valued health for a hypothetical 10-year-old child in face-to-face, one-to-one computer-assisted interviews from November 2019 to June 2020. The 28-state design had three blocks of ten, with `33333` in every block. Each respondent valued ten states after warm-up and practice. Eight trained interviewers received two-day training and continuing EQ-VT quality review.

**Task-feasibility assessment.** Feasibility was represented by interview time, moves between the two lives, self-reported understanding, ability to distinguish states, decision difficulty, and non-trading. The mean interview time was 35.70 minutes and the mean number of moves per cTTO task was 13.21. Of participants, 74.16% reported easy understanding, 59.33% reported easy state differentiation, and 11.48% reported difficulty selecting an indifference point. One participant did not trade. The comparison with a Chinese adult EQ-5D-5L valuation used an independent sample, self-perspective rather than child perspective, and a protocol without the same active quality controls. It is contextual evidence, not a randomized feasibility comparison.

**Models and candidate product.** The paper compared ordinary least-squares, heteroskedastic, and random-effects models under main effects and main-effects-plus-`A3` specifications. Logical consistency, coefficient significance, uncertainty, and leave-one-state-out prediction error guided evaluation. The `A3` random-effects model performed best by the stated criteria. It is a candidate cTTO-only scoring model and a guidance contribution. The paper did not replace the Chinese hybrid EQ-5D-Y-3L value set selected in paper 6 or document official adoption.

**Principal findings and interpretation.** About 21.9% of cTTO observations were negative. Observed means ranged from 0.924 for `11112` to -0.088 for `33333`, with a marked gap above the next-worst observed state. The authors judged the distribution smooth enough and the coefficients sufficiently differentiated to support cTTO-only estimation. They argue that cTTO directly reflects quality-duration trade-offs and can avoid uncertain hybrid modeling. They also infer that higher youth values can make lifesaving child interventions more likely to appear cost-effective. That latter statement is an author implication, not an evaluated economic result.

**Limits, gaps, and uncertainty.** The sample slightly overrepresented higher education and the task comparison combined several design differences. The study tested one country, one child age, and one protocol. The participant table gives 216 males as 48.33% and 202 females as 51.67%, but those percentages match the opposite counts. The result text repeats 51.67% female. Preserve the conflicting count and percentage.

### 25. `10.1038/s41433-023-02860-x`

**Aim and family.** Cost-of-illness, health-burden, and population-health description. It estimated the 2014 prevalent societal economic impact of presenting vision impairment in adults aged 40 years or older in Trinidad and Tobago.

**Evidence sources, population, and flow.** The main source was the 2014 National Eye Survey of Trinidad and Tobago, a multistage probability cluster survey. It sampled 9,913 eligible people aged five years or older in 3,556 households and included 4,263 adults aged 40 years or older. Vision was measured in 3,589. Medical and ophthalmic utilization evidence was available for 2,792, and socioeconomic cost evidence for 2,516. A contemporaneous national eye-care system survey supplied provider services, volumes, tariffs, and unit costs. Population counts, disability weights, labor values, exchange rates, and other external sources supplied model inputs. These are linked evidence sources, not one participant sample.

**Measures and roles.** Clinical vision measurements defined normal vision, near vision impairment, mild impairment, moderate or severe impairment, and blindness in the better-seeing eye. Participants reported care use, costs, employment, informal care, transport, aids, and socioeconomic circumstances. No EQ-5D form was administered in this paper. DALYs and disability weights represented non-fatal wellbeing burden. They must not be retrieved as EQ-5D utilities or QALYs.

**Burden-estimation methods.** The prevalence-based, mainly bottom-up assessment used a societal perspective and 2014 Trinidad and Tobago dollars. It separated direct medical costs, direct non-medical costs, indirect productivity and informal-care costs, and intangible wellbeing loss. Years lived with disability were prevalent cases multiplied by WHO disability weights; years of life lost were set to zero. The authors then monetized lost wellbeing through an external value-of-statistical-life route and reported totals with and without this component. Survey weights, post-stratification, cluster corrections, age- and sex-adjusted multilevel models, unit-cost conversion, allocation to bearers, and one-way sensitivity analyses supported the estimates.

**Principal findings.** The estimated total societal impact was TT$3.842 billion, or UK£365.7 million. Monetized wellbeing loss was 73.3%. Without it, economic cost was TT$1.025 billion, of which indirect costs were 70.5%, direct medical costs 17.9%, and direct non-medical costs 11.6%. Individuals and families bore an estimated 97.6% of total cost. The authors estimated 64,431 adults with distance vision impairment, of whom 86.1% had potentially avoidable impairment. Lower vision was also associated with lower employment, income, education, insurance, and eye-care access.

**Interpretation, implications, limits, and gaps.** The authors present the estimates as a national baseline for research and later cost-effectiveness analysis and identify investment needs in prevention, treatment, low-vision services, and work enablement. They do not compare intervention alternatives. Results exclude people younger than 40 years, institutional care, several downstream medical effects, transfers, deadweight loss, and caregiver opportunity cost. Recall and overall questionnaire nonresponse of 34.5% to 41.0% can bias estimates. Only 41.9% of eligible blind participants supplied the medical and ophthalmic questionnaire evidence. Alternative disability weights changed monetized wellbeing costs about fourfold. The authors describe monetization of DALYs as conceptually and ethically uncertain and call for international cost-of-vision study standards.

### 26. `10.1177/0272989x251325828`

**Aim and family.** Preference-elicitation method study. It tested whether DCE-with-duration utilities align with cTTO when the model varies both time preference, linear against nonlinear, and operational anchor, immediate death against zero duration.

**Evidence reuse and comparison basis.** This secondary analysis reused the 970 retained respondents from the Trinidad and Tobago DCE-with-duration study described in paper 12. Each person completed 18 split-triplet tasks, including 15 shorter-full-health comparisons and three immediate-death comparisons. The 1,079-person EQ-VT cTTO study in paper 27 supplied an independent population benchmark. No respondent completed both protocols, so the paper tests population-level tariff correspondence, not individual agreement. The secondary paper mentions both online-panel and public-place recruitment, while the primary report states that all public-place records were removed for quality problems.

**Task and model specifications.** Each triplet first compared two EQ-5D-5L states at equal duration and then compared the selected state with shorter full health or immediate death. Durations ranged from six months to 15 years. Bayesian design updates followed successive respondent batches. Mixed-logit models included respondent-specific coefficients. One model fixed linear time preference. The other estimated exponential discounting. Each model was normalized once on immediate death and once on full health at zero duration. These four scale constructions are distinct outcome-derivation routes.

**Principal findings.** The nonlinear discount parameter was about 23.4%. With linear time preference, immediate death had estimated utility -2.1 when the scale was anchored on duration; with nonlinear time preference it was -0.28. Worst-state values ranged from 0.34 under linear time and immediate-death anchoring to -1.03 under linear time and duration anchoring. Nonlinear time plus duration anchoring gave -0.54, close to the cTTO benchmark near -0.61. Immediate-death anchoring compressed decrements, and linear duration anchoring expanded them excessively.

**Interpretation, implications, limits, and gaps.** The authors conclude that immediate death is empirically below a zero-duration life and that DCE-with-duration designs must identify nonlinear time preference. They recommend duration anchoring and suggest removal of immediate-death tasks. This is method guidance, not an established replacement protocol. The study is limited to EQ-5D-5L in one country. It had no participant debrief for DCE engagement, less mature quality control than EQ-VT, and independent comparison samples. The article states that one selected construction aligned with cTTO but then refers to the “other 4 choices,” although only three other combinations remain.

### 27. `10.1186/s12955-024-02266-7`

**Aim and family.** Valuation and value-set development. The study directly elicited an EQ-5D-5L value set for Trinidad and Tobago under EQ-VT 2.1 and compared it with the earlier 3L-to-5L crosswalk.

**Population, sampling, and flow.** A market-research company recruited adults through randomly selected streets, one in four households, and the most-recent-birthday method. Quotas used age, sex, 14 Trinidad regions, and the combined Tobago parishes. Fourteen interviewers entered training and ten remained after pilot or continuing quality review. The response rate was 34%. A total of 1,079 adults completed interviews from July to September 2022. Participants supplied preferences for hypothetical EQ-5D-5L states and also reported their own health.

**Tasks, administration, and quality control.** Face-to-face computer-assisted interviews used self-report EQ-5D-5L and EQ VAS, wheelchair examples, three cTTO practice states, ten formal cTTO states, a cTTO feedback module, and 12 duration-free DCE pairs. cTTO used conventional and lead-time branches. The cTTO design had 86 states in ten blocks. The expanded DCE design had 20 blocks. Batch-level quality rules covered explanation of worse-than-dead tasks, example time, formal-task speed, and serious `55555` ordering problems. Of 1,079 interviews, 164 were flagged, but the final analysis retained the respondents under the paper's quality procedure.

**Models and selection.** Candidate routes included random-intercept and censored Tobit cTTO models, heteroskedastic variants, conditional and mixed-logit DCE models, and hybrid models. Selection considered censoring, heteroskedasticity, logical consistency, significance, in-sample error, leave-one-state-out prediction, and leave-one-block-out prediction. The hybrid heteroskedastic Tobit model was selected because all coefficients were monotonic and significant and single-state prediction was best. A cTTO-only model predicted whole omitted blocks slightly better, so no one fit measure decided selection.

**Product and findings.** The paper produced a final reported, estimated, and author-recommended Trinidad and Tobago EQ-5D-5L value set with range -0.563 to 1. Pain or discomfort had the largest decrements and usual activities the smallest. Compared with the crosswalk, the direct value set had lower mean values, a wider range, a mean absolute difference of 0.157, and correlation 0.879. It is the national product recommended for local QALY calculation.

**Comparison interpretation, transfer, and reuse.** The direct value set and crosswalk differ in instrument version, health-state wording, valuation protocol, source period, direct against mapped derivation, and underlying preference populations. The authors link some difference to better quality control and possible social change, but the comparison cannot isolate these causes. The paper proposes use as a reference in similar Caribbean settings; it does not establish regional validity. Its cTTO data supply the benchmark in papers 12 and 26, and its self-reported health responses supply one component of paper 28.

**Limits and uncertainty.** Some age-sex and education groups were imbalanced, and interviewer compliance and distribution differences remained. The abstract reports 236 negative states, or 7.6%. The result text reports 275 negative states, or 8.8%. Preserve both. The comparison statement that the 2022 study represents preferences “as of 2022” is supported by the collection dates, although one discussion sentence calls it the 2023 study.

### 28. `10.1186/s12955-024-02323-1`

**Aim and family.** Population-norm or reference study and health-equity or inequality study. It produced updated Trinidad and Tobago EQ-5D-5L reference values for 2022–2023, assessed inequality, and compared health with the 2012 norms.

**Components, evidence reuse, and modes.** The combined sample of 2,989 contained three components. Survey 1 reused the 1,079 face-to-face computer-assisted valuation respondents from paper 27. Survey 2 reused the 970 retained online DCE-with-duration respondents from paper 12. Survey 3 added 940 online panel respondents who supplied only EQ-5D-5L and demographic data. All used the Trinidad and Tobago English self-complete computer or tablet form. The paper describes the samples as mutually exclusive, but it also states that overlap between the non-panel first survey and later panels could not be ruled out.

**Norm product and outcome derivation.** The paper supplies index, EQ VAS, full-profile ceiling, dimension, state, age-sex, and demographic reference values. Current profiles were scored with the directly elicited 2024 Trinidad and Tobago EQ-5D-5L value set from paper 27. The same value set was applied to stored 2012 profiles so that the temporal index comparison did not confound time with scoring route. The reference period, three source samples, mixed modes, and value set are necessary parts of the population-norm product.

**Inequality and temporal methods.** Demographic strata included age, sex, income, education, ethnicity, employment, marital status, insurance, and self-employment. Welch tests and ANOVA compared norm means. Ordered-logit models estimated odds of levels 3 to 5 for dichotomized disadvantaged groups. A modified Kakwani index quantified inequality in EQ VAS and index values and decomposed the association by sex, income, age, and education. The temporal comparison reused a 2012 sample of 2,036 and common subgroup definitions. These methods represent different inequality questions and should not be collapsed into one score.

**Principal findings and product stage.** In 2022–2023, mean index was 0.921, mean EQ VAS was 79.6, and full-profile ceiling was 31.5%. Pain or discomfort problems occurred in 43% and anxiety or depression problems in 39%. The Kakwani index was 0.113 for EQ VAS and 0.058 for index; only small reported shares were decomposed through the included demographics, with sex the largest relative contributor. Index, EQ VAS, and ceiling were lower across demographic groups than in 2012. The EQ VAS Kakwani index rose from 0.103 to 0.113. The authors recommend these estimated norms as the current national reference until they are updated.

**Interpretation, limits, and gaps.** The authors interpret the change as worse reported population health and more inequality and propose periodic norm updates. They also discuss changed perceptions and the post-pandemic context, but the observational design cannot separate health change, reporting change, source-sample differences, mode, or panel coverage. The combined sample uses incentives and two panel surveys, response rates were unavailable for the online components, some duplicates could remain, and demographic variables were coarsened for 2012 comparison. Future work should use older age groups with more detail.

**Extraction uncertainty.** The abstract says three studies, while the method introduction says two studies and then describes three surveys. The abstract and discussion give the collection end as May 2023, while the survey-3 method states March to August 2023. Preserve the three survey components and conflicting end dates.

### 29. `10.1007/s11136-025-04074-y`

**Aim and family.** Survey-method and data-quality study within a research infrastructure and data resource. It documented how the EQ-DAPHNIE UK pilot changed survey design and reported quality indicators for the later 15-country online data resource. It did not estimate population norms or instrument performance.

**Components and evidence reuse.** The UK pilot had 3,012 completers and six randomized survey versions. It belongs to the same EQ-DAPHNIE infrastructure described in paper 3. The main component contained 68,411 completed surveys from 15 countries, with about 4,500 adults per country. Dynata non-probability panels supplied respondents under quotas for age, sex, income, community setting, and language where applicable. LimeSurvey hosted the response events. Paper 30 later reuses an eight-country subset.

**Pilot conditions and documented redesign.** Pilot factors varied EQ-HWB length, the number and form of EQ-5D-5L response-heterogeneity vignettes, and mandatory against optional questions with a `prefer not to answer` option. Repeated education and self-rated-health questions assessed consistency. Pilot findings led to one gender-neutral moderate-health vignette, country-specific EQ-HWB long or short forms, two-item PHQ and GAD forms, optional questions without a refusal option, earlier demographic questions, bounded selection lists instead of open numeric fields, sensitivity explanations, and removal of political affiliation. These are documented survey-design effects, not only recommendations.

**Quality-control structure.** Researcher controls included four reCAPTCHA interactions, a five-minute speed rule, duplicate checks, repeated-item agreement, missingness and outlier review, soft launches, real-time quota monitoring, and post-stratification. Panel-provider controls included IP checks, identity validation, and proprietary fraud screening. Each rule had a different unit and action. Bot and speed rules excluded records. Quota monitoring changed recruitment thresholds. Pilot missingness and feedback changed later question design. Link clicks, consent, completion, exclusion, and final records are distinct sample stages.

**Principal results.** The pilot sent 4,538 invitations, recorded 96.6% link clicks, 75.1% consent, and 3,012 completions. In the main data, link-click rates were 80.1% to 100%, while completion rates were 22.9% to 60.8%, with mean 42.4%. Mean completion time was 18.3 to 31.4 minutes by country. Bot exclusions averaged 3.0% and reached 11.7% in China. Speeding averaged 0.3%, and duplicates were rare. Repeated marital-status agreement was 92.8% to 98.9% and age agreement was 92.3% to 98.7%. Variable missingness ranged up to 48.7%, and proportional quota achievement ranged from 68.7% to 98.6%.

**Interpretation, implications, and limits.** The authors judge the controls effective and the data generally high quality. They also warn that missingness, quota gaps, internet coverage, and non-probability selection affect norm and cross-country analyses. Weighting cannot remove unobserved panel-selection differences. Suggested actions include adaptive recruitment, other panels or offline modes, sensitivity analyses, and triangulation with probability samples. The abstract calls the 80.1% to 100% link-click measure a response rate. Store it as a link-click stage to avoid confusing it with consent or completion.

**Extraction uncertainty.** One method passage flags a bot when any score is below 0.5; another excludes scores of 0.5 or less. The same boundary conflict appears for speeders as under five minutes against five minutes or less. Preserve the operational ambiguity at the threshold.

### 30. `10.1007/s11136-026-04294-w`

**Aim and family.** Population-health description and health-equity or inequality study with a measurement-coverage topic. It tested whether education and subjective income gradients remain in EQ VAS among people who report the same EQ-5D-5L profile.

**Evidence reuse, population, and selection.** This secondary analysis reused EQ-DAPHNIE data from Australia, Canada, France, Germany, the Netherlands, New Zealand, the United Kingdom, and the United States. The final sample contained 32,327 online-panel respondents reported as aged 25 to 79 years. Ten selected mild EQ-5D-5L profiles covered 61% of the sample. The analysis excluded younger and oldest respondents, BMI at or below 15, and profile-specific low EQ VAS values. It inherited quota sampling, survey weights, and data-quality controls from the parent resource.

**Instrument and variable roles.** EQ-5D-5L profiles defined within-profile analysis strata. EQ VAS was the dependent outcome. This paper did not analyze preference-weighted index values. Education was harmonized as low, medium, or tertiary. Subjective household-income adequacy was comfortable, coping, or difficult, after the two lowest categories were combined. Age, sex, and country were adjustment variables. Education and perceived income are socioeconomic indicators, not dimensions of the EQ-5D-5L instrument.

**Methods and data handling.** Each profile received separate weighted linear models for education and income, adjusted for age, sex, and country. Country-specific models were possible only for profiles `11111` and `11121`. Full-information maximum likelihood handled missing data under a missing-at-random assumption. The study removed EQ VAS below 50 for `11111` and below 30 for the other mild profiles as logical-consistency exclusions, affecting 0.6% to 3.1% by profile. The rule is an analysis-specific eligibility choice and must remain visible.

**Principal findings.** Higher education was associated with higher EQ VAS in all ten profiles, with evidence at the paper's 0.10 threshold in seven. Subjective income showed a stronger gradient in nine profiles. For `11121`, high against low education differed by 2.135 EQ VAS points, while comfortable against difficult income differed by 4.969. In country-specific analyses, the comfortable-income coefficient was positive and significant at 0.05 for `11111` in all eight countries. For `11121`, it was positive in all eight, significant at 0.05 in six, marginal in Canada, and not significant in the Netherlands.

**Interpretation and implications.** The authors give two non-exclusive explanations: EQ-5D-5L profiles can omit health aspects that influence EQ VAS, or socioeconomic groups can use the VAS scale differently. The data cannot distinguish these mechanisms. They argue that EQ-5D-5L values alone can understate inequality relative to EQ VAS and recommend complementary EQ VAS, bolt-on, or direct socioeconomic information when equity is central to monitoring or HTA. The study does not show that the descriptive system fails its intended construct or that equity-weighted QALYs changed a decision.

**Limits and uncertainty.** The cross-sectional online-panel design does not support causal inference and covers only high-income countries. Subjective income and EQ VAS can share response-style or psychological determinants. Country-specific precision was limited. The low-EQ-VAS exclusion can remove true extra-domain poor health or response heterogeneity, which are mechanisms discussed by the paper; treat the resulting gradient as conditional on that rule. The abstract reports ages 25 to 79, but methods say respondents older than 80 were excluded, which would retain age 80. The exact upper boundary is unresolved.

## Applications to batch 04

### 31. `10.1371/journal.pone.0302886`

**Aim and family.** Protocol or study-design paper, social-value or priority-preference study, and preference-elicitation method study. It specifies a mixed-methods Australian study that will estimate the relative social value of otherwise identical health gains for children and young people against adults. It will also test whether a PTO task that permits an equivalence response gives different results from a forced-choice task.

**Components and status.** The main 2,000-person online PTO survey, about 40 think-aloud interviews, and about four focus groups are planned components. Completed design work included Consumer Advisory Group input, survey pilots with at least 14 convenience participants in addition to three advisory-group testers, two initial interview pilots, and protocol refinement. A 50-person soft launch and six further interview pilots were planned. The completed pilots inform the protocol, but the paper reports no main-sample preference results or age weights.

**Evidence roles and planned selection.** Australian people aged 16 years or older will supply social-priority preferences. The beneficiaries in the PTO scenarios are patient groups at 13 ages from 1 month to 24 years and adult comparator groups aged 40 or 55 years. The survey will use an Online Research Unit panel with age-gender, education, and loose geography quotas. The qualitative recruitment will purposively cover adolescents and young adults, parents of younger and older children, parents or carers of children with health problems, and adults without children. The intended decision context is Australian HTA and possible weighting of health gains by recipient age.

**Distributional preference tasks and conditions.** This PTO is not an EQ-5D health-state valuation. Respondents will compare programs that give identical gains to different age groups while patient-group size changes from a 100-versus-100 start. The preferred group's size is reduced by bisection toward equivalence, with an inferred midpoint when exact equivalence is not reached. Health-gain contexts cover 2- or 5-year life extension and temporary improvement in pain, mobility, or distress and low mood or anxiety. Life-extension gains end in death. Quality-of-life gains last 2 years and then return to full health. Randomized factors include forced choice against an equivalence option, younger group on the left or right, and life-extension against quality-of-life question order. Chaining questions test cardinal consistency. Attitudinal questions and qualitative probes examine reasoning and apparent conflicts between principles and numerical choices.

**Planned methods and quality controls.** The survey will report ratio of means and median of individual ratios by age and context, bootstrap uncertainty, extreme and non-trading preferences, preference classes, chaining performance, and regression associations. The qualitative work will use framework-guided thematic analysis and prospective saturation checks. Pre-specified record controls cover speed, an attention item, repeated age, unique panel identifier, nonsensical text, and a bot honeypot. Comprehension, PTO-attitude inconsistency, and rapid completion are sensitivity indicators rather than interchangeable exclusion rules.

**Contribution, implications, limits, and gaps.** The product is a detailed, piloted protocol and planned mixed-method resource, not observed age weights. The authors expect it to inform Australian decision makers and PTO design. They identify online engagement, commercial-panel coverage, PTO focusing and aggregation assumptions, extreme preferences, and Australia-only transfer as limits. The study is designed to investigate whether equivalence responses reflect genuine equality, avoidance, difficulty, or low understanding. That question remains unresolved until the planned data are analyzed.

### 32. `10.1186/s12955-023-02115-z`

**Aim and family.** Preference-elicitation method study using experience-based health-state valuation and secondary register analysis. It examined how patients in nine Swedish clinical groups rated their own EQ-5D-3L states on EQ VAS at baseline and 1-year follow-up and compared these patterns with a general-population sample.

**Evidence sources, components, and flow.** The patient evidence contained 172,070 complete records with EQ VAS from nine National Quality Registers: spine surgery, hip replacement, knee replacement, ankle replacement, cruciate-ligament treatment, first-line osteoarthritis treatment, heart failure, respiratory failure, and bipolar disorder. A separate 41,761-person general-population component reused 2004 Scania and 2006 Stockholm survey data. Baseline, 1-year follow-up, patient group, and general population are analysis components because health experience, timing, and collection source differ. Register availability, follow-up availability, and willingness to participate affected register selection. The exact administration procedures varied between registers and were not harmonized in this paper.

**Instrument and valuation roles.** EQ-5D-3L profiles described experienced health. EQ VAS was both the self-rated overall-health outcome and the input from which the authors interpreted experience-based state values. This differs from VAS valuation of several hypothetical states. The EQ-5D-3L index was derived with the Swedish experience-based VAS value set and served as a comparison outcome. Supplemental checks used EQ-5D-5L data from only the osteoarthritis and hip registers. The paper did not anchor the present EQ VAS responses on dead and did not produce a complete national value set.

**Methods and comparisons.** Mean EQ VAS was summarized for nine selected profiles. Spearman correlation compared EQ VAS with the experience-based index and compared their changes. Ordinary least-squares and two-level random-intercept and random-slope models related EQ-5D dimension levels to EQ VAS, with age and sex adjustments and pooled patient-group models. A decrement was called inconsistent when a more severe level had a smaller decrement than a milder level. The comparisons therefore concern time, clinical group, general population, profile severity, and model form.

**Principal findings.** EQ VAS generally decreased as profile severity increased. Correlations with the index were moderate at baseline and became stronger at follow-up, but correlations between changes were low to moderate. Most models showed ordered decrements. Severe self-care was the most frequent inconsistency. Anxiety or depression had the largest decrement in most patient groups and the general population, with pain, mobility, or usual activities leading in a few groups. Values for the same profiles differed by group and time.

**Interpretation, implications, limits, and reuse.** The authors interpret the variation as evidence that EQ VAS covers health beyond the five descriptive dimensions and that patient experience and timing can affect valuation. They propose patient EQ VAS data as possible input for patient-perspective value sets and clinical or resource-allocation work, but they do not document such use. Different register collection procedures, lack of a dead anchor, VAS end avoidance, lack of a choice or trade-off, and remaining EQ VAS-index discrepancy limit economic use. The study explicitly reuses register, population-survey, and Swedish value-set evidence from earlier work.

### 33. `10.1007/s11136-020-02712-1`

**Aim and family.** Preference-elicitation method and data-quality study with an administration-mode comparison. It tested whether an unsupervised online implementation could reproduce interviewer-assisted face-to-face US EQ-5D-5L cTTO evidence.

**Samples, reuse, and comparison bundle.** The paper reused two independent US valuation sources. The face-to-face source contained 1,134 completers and 11,340 cTTO observations. Interviewers judged 72 respondents unable to understand cTTO. The remaining 1,062 respondents withdrew 1,234 values through the feedback module, leaving 9,386 observations in the face-to-face valid analysis. The experimental online-panel source contained 501 completers and 5,010 observations. Both used age, gender, race, and ethnicity quotas, but they differed in recruitment, incentives, supervision, platform, tutorials, live clarification, feedback, and sample period. The contrast is therefore an implementation bundle, not a clean estimate of mode alone.

**Task and administration.** Both sources used the same 86-state, ten-block EQ-5D-5L design, with ten formal cTTO states per person, conventional TTO for better-than-dead responses, and lead-time TTO for worse-than-dead responses. Face-to-face respondents completed one-to-one computer-assisted interviews in six metropolitan areas, read states aloud, received live clarification, completed five practice states, and used a final feedback module. Online respondents completed an automated panel survey with spoken state presentation, interactive tutorials, the same practice sequence, and a prompt after a task under 15 seconds, but no interviewer or feedback module.

**Quality and model methods.** Task time, number of trade-offs, non-trading, better-than-dead-only patterns, self-reported understanding, dominated-state inconsistencies, and `55555` inconsistencies assessed engagement and validity at task or respondent level. Random-intercept linear models produced research value sets for each sample. The comparison also used coefficient significance, level inversions, range, worst-state value, dimension rank, and mode-adjusted models. These modeled sets are analytic outputs, not recommended US scoring products.

**Principal findings.** Online respondents reported poorer understanding and used fewer trade-offs. They were more often non-traders or better-than-dead-only traders. A `55555` inconsistency occurred in 41.3% online against 12.2% in the full face-to-face sample. Online values were higher for most severity groups and only 2.8% were negative, against about 23% face to face. The online model had eight non-significant decrements, two inversions, a range of 0.600, and a `55555` value of 0.400. The face-to-face range was 1.307.

**Interpretation, limitations, and uncertainty.** The authors conclude that this online cTTO implementation did not overcome engagement and comprehension problems and should not be the first choice for general-population valuation. They do not conclude that every online TTO design is invalid. Recruitment source and interviewer presence cannot be separated, sample sizes differed, unmeasured respondent traits remain, and the online platform may not represent other implementations. The online sample is described as an adult general-population sample, but its reported age range starts at 17 years. Preserve that conflict.

### 34. `10.1186/s12955-022-01996-w`

**Aim and family.** Measurement-property and instrument-version study. It compared Bahasa Indonesia proxy forms of EQ-5D-Y-3L and experimental EQ-5D-Y-5L version 1 and assessed agreement of each proxy form with the matched child self-report form.

**Population, dyads, and time components.** The study contained 286 Indonesian child-caregiver dyads from five hospitals in Jakarta and Bandung. Children were aged 8 to 16 years and had beta-thalassemia, hemophilia, acute lymphoblastic leukemia, or an acute illness. Proxies were mainly mothers, with fathers, siblings, and other relatives also represented. Baseline, disease-timed test-retest, and post-treatment follow-up were separate components. Of 247 possible retest pairs, only 59 proxy pairs met the proxy-reported no-change rule. Follow-up contained 222 proxy responses, of which 91.4% reported improvement.

**Reporter perspective and administration.** The study used proxy version 1: the caregiver gave their own assessment of the child's health. It did not use proxy version 2, which asks how the caregiver thinks the child would answer. Children and proxies completed paper forms independently, with staff preventing discussion and assisting only with reading or writing. EQ-5D-Y-5L always preceded EQ-5D-Y-3L. The study used in-progress UK English self and proxy forms translated into Bahasa Indonesia with EuroQol version-management collaboration.

**Instrument roles and property methods.** The target descriptive systems were proxy EQ-5D-Y-3L and experimental proxy EQ-5D-Y-5L. PedsQL Generic and condition-specific proxy measures were convergent comparators. Missingness assessed feasibility. Full-profile `11111` frequency assessed response distribution, even though the paper discusses it under content validity. Response redistribution assessed classification refinement. Correlation assessed convergent validity. Gwet's agreement coefficient and percentage agreement assessed stable retest reliability and self-proxy agreement. Responsiveness used proxy-reported change and dimension-level direction because no EQ-5D-Y-5L value set was available.

**Principal findings.** Missingness was 1.0% for 3L and 1.4% for 5L. Baseline full-health frequency was 21.3% for 3L and 16.7% for 5L. The forms had similar convergent patterns and mean retest coefficients of about 0.83 and 0.84. In the large improved subgroup, 5L captured more improvement in four of five dimensions. At baseline, self-proxy agreement was usually higher for 5L. Agreement was weaker for acute illness and rose after recovery.

**Interpretation, limits, and product boundary.** The authors state that five levels can improve proxy classification and change detection without an evident reliability loss. The paper supports further development of a 5L proxy form; it does not itself create an official revision or show that proxy reports can replace self-reports. The fixed instrument order, different recall periods in comparators, only 59 stable pairs, and analysis of responsiveness almost only in improvers limit conclusions. Acute illness also shows that self-proxy agreement is conditional on clinical stability and time.

### 35. `10.1186/s12955-024-02290-7`

**Aim and family.** Intralingual cultural-adaptation and content-validity study. It adapted UK English EQ-5D-Y-3L and EQ-5D-Y-5L to Singapore English and assessed relevance and comprehensiveness of the descriptive system for children in Singapore.

**Components, evidence suppliers, and flow.** An eight-person expert panel, six pediatricians and two primary-school educators, reviewed wording for local use. Cognitive debriefing then included 11 children: six tested Y-3L because one noisy interview was replaced, and five tested Y-5L. A separate content-validity sample contained eight healthy and six chronically ill children aged 8 to 15 years. These samples did not overlap. Children supplied comprehension, severity-order, poor-health concept, relevance, and comprehensiveness evidence. The intended population was English-speaking children and adolescents in Singapore.

**Adaptation and qualitative methods.** This was a UK English to Singapore English cultural adaptation, not translation to a different language. Expert review, developer input, draft revision, verbal probing, paraphrasing, and child cognitive debriefing produced local wording and examples. Y-5L children also ranked randomized severity labels. All proposed modifications were endorsed by the EuroQol Research Foundation. For content validity, one-to-one English interviews first elicited direct and indirect poor-health experiences without an instrument. Children then self-completed Singapore English Y-3L and discussed missing or irrelevant content. Two coders used a prior Singapore framework with inductive additions, consensus, and a three-transcript saturation rule.

**Products and content scope.** The products are developer-endorsed, comprehension-tested Singapore English Y-3L and Y-5L forms. The content-validity component evaluated the common descriptive-system concepts through Y-3L. It did not assess EQ VAS content and did not test Y-5L response levels beyond adaptation comprehension and ranking. Record source and target English locale so that the products remain distinct.

**Principal findings.** Local changes included familiar wording for self-care and examples for discomfort. All Y-5L testers ordered the response levels as intended. The content interviews elicited physical health, mental wellbeing, and social relationships. All five EQ-5D-Y dimensions appeared spontaneously and were judged relevant. Children also identified sleep, appetite, and family or friend relationships, among other concepts. The authors judged the system generally relevant and comprehensive while noting that social relationships and appetite were not covered.

**Interpretation, limitations, and gaps.** The authors recommend study of appetite and social-relationship bolt-ons and psychometric testing in Singapore. They do not report a revised core descriptive system. Young children had limited direct serious-health experience, relative importance of concepts was not studied, and the EQ VAS was outside scope. The broad conclusion about descriptive-system content must not be expanded to EQ VAS or to measurement properties that the paper did not test.

### 36. `10.1007/s10198-025-01769-4`

**Aim and family.** Preference-elicitation method and measurement-property study. It assessed 2-week test-retest reliability of the Online Elicitation of Personal Utility Functions approach for EQ-HWB-S at individual and aggregate levels.

**Population, flow, and components.** A German online panel supplied 330 initial respondents: 110 from the general population, 110 with diabetes, and 110 with rheumatic disease. Of these, 257 completed retest. After exclusions for illogical or unusable unmatched responses, 220 were analyzed: 73 general-population and 147 patient participants. Test and retest, general population and patient, and individual and aggregate outputs are distinct components. The same respondents were matched by identifier.

**Preference elicitation architecture.** EQ-HWB-S, with nine five-level dimensions, was the health-state system. The compositional OPUF sequence first ranked worst-level dimensions and elicited relative swing weights. It then rated intermediate levels between fixed best and worst anchors. A pairwise task compared state `555555555` with dead, after which the preferred state was located on a 0-to-100 scale to generate a QALY anchor. Level ratings, swing weights, and the anchor were combined in an additive model to produce individual and aggregate utility decrements and value sets. Participants also reported their own EQ-HWB-S state and completed an adapted EQ VAS as warm-up tasks. The survey was unsupervised online self-completion.

**Reliability methods and exclusions.** Spearman correlation assessed individual dimension ranks. Agreement percentages, kappa, and intraclass correlation assessed the top rank, swing weights, intermediate levels, dead-versus-worst choice, anchoring factor, and individual decrements. Paired tests, distribution tests, and plots compared aggregate decrements. Participants with more than two illogical responses or anchoring indifference were excluded. The target of reliability is the elicitation method and each derived output, not the EQ-HWB-S descriptive system alone.

**Principal findings.** Only about 42% selected the same top-ranked dimension. Individual swing weights, level ratings, anchoring factors, and utility decrements usually had poor or moderate agreement. The dead-versus-worst choice was more stable, with kappa 0.64, but its continuous anchoring factor had ICC 0.12. Final individual health-state rankings had Spearman rho 0.26. By contrast, aggregate decrements were close: the mean absolute test-retest difference was 0.004, and almost all distribution tests showed no difference.

**Interpretation, product, limits, and gaps.** The authors conclude that OPUF can produce stable group-level research value sets for EQ-HWB-S but does not yet support stable personal utility functions. The test and retest value sets are method-evaluation outputs, not a recommended German national value set. Excluding illogical responses can overstate reliability, online recruitment selects for digital access, and the study cannot separate effects of OPUF, EQ-HWB-S complexity, and online administration. Patient status was also associated with age. The authors call for qualitative task research, design refinement, repeat reliability testing, minimum-sample study, and interviewer-supported comparisons.

### 37. `10.1136/bmjopen-2025-100897`

**Aim and family.** Protocol or study-design paper, instrument-development study, and preference-elicitation method study. It specifies two planned Australian DCE waves that will test whether the levels of experimental EQ-TIPS-5L version 3.0 follow preference severity, influence choices, and give consistent main effects across kaizen and paired-comparison tasks.

**Instrument and product status.** Experimental EQ-TIPS version 3.0 is intended for proxy assessment of health in children aged 0 to 36 months. It has seven attributes and both 3L and 5L forms. The paper targets the 5L descriptive system as an object of instrument-structure preference assessment. It supplies complete wave-1 survey materials, experimental design, and analysis plan. Wave-2 materials will be adapted from wave-1 evidence. The study does not report choice results, psychometric results, a final instrument, or a value set.

**Planned evidence roles and decision context.** The planned evidence suppliers are 1,400 Australian adults recruited from an online panel: 400 in wave 1 and 1,000 in wave 2. In preparatory questions, each adult will describe and assess a real 1-year-old child whom they know. In the main choice tasks, the referent is a hypothetical 1-year-old with an acute 1-month health episode that starts today and ends in recovery. Adults also complete EQ-5D-5L plus 13 bolt-ons about their own health. These administrations have different referents and roles from the EQ-TIPS choice profiles.

**Task forms and designs.** Wave 1 uses 14 kaizen tasks per person in two blocks. Each task starts from one profile and sequentially selects four improvements from a set that also contains one worsening change. The design identifies a bad change selected early and an improvement skipped as two discordance types. Wave 2 will use 28 paired full-profile comparisons per person in five blocks. Kaizen presents improvements or “goods,” while paired comparison selects between two impaired profiles or “bads.” Both waves randomize task sequence and respondent-level attribute order and use conditional-logit main-effects models. Cluster bootstrap methods will compare uncertainty, main effects, task-form agreement, and wave-1 prediction of wave-2 choices.

**Selection, quality, and planned comparisons.** Recruitment uses gender, age, and ancestry quotas. Withdrawal, invalid child description, completion under 10 minutes, or an attempted repeat after exclusion can remove a respondent. The child-description rule requires a child, an object or toy, personalization, and two complete sentences. Sensitivity analyses cover block, task sequence, attribute order, sample size, and removal of respondents with frequent preference-severity discordance.

**Contribution, interpretation, limits, and uncertainty.** The product is a planned two-wave protocol with operational wave-1 materials. Claims that kaizen yields more preference information and lower burden are design rationale and hypotheses here, not findings from the planned study. Online-panel selection, English and internet requirements, and choices about illness in a 1-year-old limit transfer. The paper states age quotas of 18–29, 30–44, 45–64, and 55 years or older. The last two bands overlap, so the implemented age strata cannot be normalized from the text. Preference results and any instrument revision remain future work.

### 38. `10.1007/s40258-025-00954-z`

**Aim and family.** Mapping, scoring, and value-set comparison study. It compared EQ-5D-5L crosswalk value sets derived from national EQ-5D-3L value sets with direct national EQ-VT EQ-5D-5L value sets and examined the role of the changed worst mobility label.

**Products, countries, and provenance.** The authors identified 25 TTO- or DCE-plus-TTO EQ-5D-3L sets and 32 EQ-VT EQ-5D-5L sets, then formed 19 comparable pairs across 18 countries: Canada, China, Denmark, France, Germany, Hungary, Italy, Japan, the Netherlands, Poland, Portugal, Romania, South Korea, Spain, Taiwan, Thailand, Trinidad and Tobago, and the United States. The United States contributed one historical independent pair and one parallel-study pair. For each source 3L set, the Van Hout response-mapping algorithm produced an analysis-specific 5L crosswalk set. This chain inherits the national 3L preferences, the source period and protocol, and the European patient response data used to estimate the crosswalk.

**Evidence dependence and external application.** Sixteen pairs used separately collected historical 3L and 5L studies. Hungary, Romania, and a second US pair used 3L and 5L EQ-VT data from the same respondents and similar models, although respondents valued fewer 3L states. Reverse 5L-to-3L crosswalks were also made for these three comparisons. An independent 7,933-person Multi-Instrument Comparison data set from five countries supplied observed EQ-5D-5L profiles for external scoring comparisons. Same-sample and independent-source comparisons must remain separate.

**Methods and comparison endpoints.** The study compared range, mean, `55555`, percentage negative, severe-state means, dimension ranks, Pearson and Spearman correlation, Lin concordance, mean absolute difference, scatterplots, and Bland-Altman plots. It isolated states with worst mobility and applied both routes to all MIC profiles, severe profiles, and worst-mobility profiles. Publication interval was only a proxy for elapsed collection time. Correlation was treated as association, while concordance, absolute difference, and plots addressed agreement.

**Principal findings.** Spearman correlation ranged from 0.831 to 0.989 and was below 0.9 for 11 pairs. Mean absolute difference across full value sets averaged 0.149 and was under 0.1 for only five pairs. No country preserved the ranking of all five single-worst-level dimension states. Worst-mobility states formed a separate disagreement band in most plots, including the same-respondent and reverse-crosswalk analyses. Scoring the MIC profiles produced significantly different means for all 19 pairs; the direction differed by pair.

**Interpretation, implications, limits, and product stage.** The authors recommend direct EQ-VT 5L values and restrict crosswalk use to cases where direct valuation is not feasible, such as very small populations. The paper creates crosswalk sets for comparison, but it does not recommend them as new national products. Historical pairs combine changes in instrument wording, valuation protocol, quality control, preference population, and period. The parallel pairs reduce these differences but still use the crosswalk algorithm and unequal task coverage. The evidence supports a strong mobility-label explanation, but it cannot quantify the relative effect of wording, method, time, population, and model. Further work should test aligned mobility labels and diagnostic or model effects as more direct sets become available.

### 39. `10.1177/0272989x251380556`

**Aim and family.** Conceptual and reporting-guidance paper. It describes how uncertainty in health-state values arises, accumulates, and enters QALY and cost-effectiveness estimates, with special depth for valuation studies.

**Scope and evidence basis.** The paper is not a new valuation, mapping analysis, or economic evaluation and has no participant sample. It uses published methodological evidence and examples from EQ-5D and other value-based descriptive systems. It provides a conceptual account rather than a systematic evidence synthesis. The intended users are valuation researchers, instrument developers, trial researchers, decision modelers, guideline developers, and HTA decision makers.

**Uncertainty model.** The framework separates intrinsic variability, observed or latent heterogeneity, statistical uncertainty, and methodological variation. It traces uncertainty through descriptive-system profile collection, valuation design, elicitation, value-set modeling, mapping, disease-state studies, meta-analysis, and cost-effectiveness modeling. Each downstream step can inherit uncertainty from its inputs and add uncertainty of its own. Valuation-specific sources include choice of relevant preference population, sampling frame, states and task order, desired scale properties, respondent engagement, elicitation method, administration and interviewer effects, fraud, summary statistic, model specification, interpolation, and misspecification.

**Key distinction and contribution.** Regression coefficient standard errors do not directly give uncertainty for every health-state value used in a decision model. The paper recommends reporting either profile-level health-state-value standard errors or the variance-covariance matrix needed to derive them. It also recommends that cost-effectiveness analyses propagate this uncertainty instead of treating value-set entries as fixed constants. The product is an uncertainty taxonomy, source-flow model, and reporting contribution, not a formally adopted guideline.

**Interpretation, implications, limits, and gaps.** The authors state that current value-set and economic-model reporting gives false precision because it often retains only point estimates. Deterministic sensitivity across alternative value sets is not a complete substitute when within-set and inherited uncertainty are absent. The authors state that the source list is not exhaustive and that evidence on the relative importance of several uncertainty types is limited. They call for valuation reporting guidance, better uncertainty quantification and propagation, and solutions for methodological uncertainty. This analytic uncertainty must remain separate from an extractor's uncertainty about conflicting source text.

### 40. `10.1007/s11136-025-03996-x`

**Aim and family.** Implementation study with co-design. Phase 2 of P-PROM ROCK co-designed an EQ-5D-Y-5L implementation program for routine pediatric outpatient visits at the Royal Children's Hospital in Melbourne and prepared it for a future pilot evaluation.

**Evidence suppliers, components, and reuse.** The results section reports two adolescents aged 14 and 16 years, three caregiver mothers, and 11 service providers across five workshops. Five feedback activities occurred within workshops and four individual feedback meetings followed. Two mock patients and two mock clinicians then took part in two optimization simulations; some were not members of the co-design group. Phase-1 qualitative findings informed workshop topics. P-MIC contacts supported recruitment, but P-MIC health data were not reanalyzed. Participants supplied design judgments from lived or service experience; they did not supply routine EQ-5D-Y-5L outcome data.

**Co-design and optimization methods.** A seven-step public-service co-design framework governed resourcing through building for change. The Double Diamond model governed discover, define, develop, and deliver work inside workshops. Sensitization tasks, vignettes, individual and group creative work, consensus discussion, iterative prototypes, email or interview feedback, and two simulated patient-clinician visits refined the program. Workshops used online, in-person, and hybrid formats and included measures to reduce stakeholder power imbalance.

**Instrument role and outcome representation.** EQ-5D-Y-5L was the implementation object. The designed clinical display uses item wording and longitudinal item-level lines, not a preference-weighted index. The ordinal level direction is reversed for the longitudinal display so that a higher plotted value means better health. Patients or caregivers select which responses to flag for discussion. This result representation is specific to clinical communication and must not be retrieved as utility scoring.

**Co-designed workflow product.** The P-PROM ROCK Program is a co-designed prototype with six linked elements: clinician training; a patient and caregiver information package that calls the instrument a general health tracking questionnaire; item and longitudinal displays; a visit-linked workflow; family resources; and clinician decision support and escalation resources. Planned completion is through Epic MyChart up to 7 days before a visit or on paper on the visit day, with reminders. The assigned clinician is responsible for review. Self-report and caregiver proxy routes receive matched resources. Mild or moderate concerns link to community support, while urgent concerns link to clinician action. The prototype was tested in a simulated workflow, but it was not yet implemented in routine care.

**Interpretation, limitations, and future work.** The authors conclude that collection alone is unlikely to change visits and that review responsibility, discussion, action pathways, training, and patient control are necessary. This is an author interpretation from co-design, not a documented clinical effect. Small stakeholder groups, technology difficulties, possible power imbalance, early-adopter service providers, no non-English-speaking participants, one hospital, and unknown transfer to other ages or settings limit the product. Phase 3 will pilot and evaluate use, decision effects, and patient-care outcomes.

**Extraction uncertainty.** The abstract reports nine service providers, while the results report 11 across the five workshops. Preserve both. The paper also calls this the first clinical-setting use of EQ-5D-Y-5L, but the reported activity is design and mock optimization rather than routine administration. Record the product at co-designed and simulated-workflow stages, not implemented.

## Round 2 ontology changes

- Added translation or cultural adaptation and economic evaluation or decision modeling as Study Family terms and Method Use families.
- Added Outcome Specification and Outcome Derivation to separate profiles, level sum scores, EQ VAS, utilities, scoring, and mapping routes.
- Added Implementation Assessment for uptake, retention, acceptability, burden, workflow, timing, and mode evidence.
- Refined Administration Event to separate participant response mode from an offered mode, later data entry, storage, or survey platform.
- Refined Evidence Reuse for combined data sets and Measurement Property Assessment for directional responsiveness, stability definitions, and cross-instrument agreement.

## Round 3 ontology changes

- Added survey-method or data-quality study and cost-of-illness or health-burden study as Study Family terms.
- Added Study Condition for allocated factorial designs and interactions.
- Added Valuation Model Specification to distinguish anchor basis, time preference, latent scale, and preference heterogeneity.
- Added Task Feasibility Assessment, separate from psychometric and implementation feasibility.
- Added specialized guidance for cost-of-illness or burden assessment, survey data-quality control, and population-norm or equity analysis.
- Refined Product to preserve a norm or burden estimate's reference period, source samples, outcome derivation, and intended comparison scope.

## Round 4 ontology changes

- Added component status so that completed pilots, planned main studies, analyzed components, and reported products do not collapse into one study state.
- Added social-value or priority-preference and methodological or conceptual guidance Study Family terms.
- Added Distributional Preference Task Use for PTO and other tasks that estimate priority weights rather than health-state utilities.
- Added Administration Support, Proxy Perspective, Cross-Informant Agreement, and locale-specific language forms.
- Added Preference Elicitation Architecture and extended property assessment from instruments to tasks, methods, scores, and value-set products at individual or aggregate level.
- Added Instrument-Structure Preference Assessment for choice experiments that test response-level ordering or decision relevance without producing a value set.
- Added Product Provenance Chain for direct, mapped, and crosswalk value sets.
- Added Analytic or Decision Uncertainty, separate from source extraction uncertainty.
- Added Implementation Workflow Specification and finer prototype stages for co-designed and simulated delivery pathways.

## Granularity decisions and evidence

1. **Keep respondent, referent, and intended population separate.** Paper 6 uses adult respondents who value health for an unspecified hypothetical 10-year-old. Paper 3 combines self-report with a proxy-style vignette for Alex. Paper 4 asks practitioners about HTA work. One “population” field would give false answers to user questions 6, 7, 20, and 25.

2. **Use paper-local components, but only for semantic differences.** Papers 3 and 5 need round, country, and phase components. Paper 6 needs independent DCE and cTTO samples. Paper 10 needs pain groups and a stable retest sample. Paper 9 needs one versus multiple postbaseline analysis strata. This supports user questions 5, 8, 9, 12, and 13 without turning tables into records.

3. **Record an instrument role, not only an instrument name.** EQ-5D is a target and scoring system in paper 1, an object of a review in papers 2 and 9, an administered population measure in paper 3, an object of practitioner-reported use in paper 4, a source and new product in paper 5, a health-state system in paper 6, and a comparator in paper 7. This distinction is required for user questions 3, 20, 21, and 23.

4. **Separate instrument family, exact form, language, and component.** Papers 3, 5, and 10 show that long or short form, 3L or 5L, youth or adult form, language, and self or proxy form change meaning and retrieval. Paper 9 shows that the descriptive system, EQ VAS, and utility require different analytic methods. This supports user questions 4, 11, 12, and 20.

5. **Represent each method use with purpose and input.** A label such as “DCE” does not show whether it estimates relative preferences, anchors utility, or is only a surveyed practice. A label such as “linear model” does not show whether it analyzes one follow-up, repeated observations, utility, VAS, or a dimension. Papers 1, 4, 6, and 9 support this choice and user questions 9, 10, 12, and 21.

6. **Give valuation tasks domain-specific depth.** Paper 1 uses adult self-perspective cTTO with conventional and lead-time branches plus duration-free DCE. Paper 6 uses adults valuing an unspecified child and questions lead-time framing. Protocol version, perspective, referent, duration, state design, anchoring role, and quality control can change interpretation. This supports user questions 10, 13, 20, and 21.

7. **Use a property taxonomy below “psychometric.”** Papers 2, 7, 8, and 10 distinguish reliability, responsiveness, comprehensiveness, informativity, item discrimination, differential item functioning, and known-groups validity. A single psychometric label would hide different evidence and gaps. This supports user questions 9, 12, 15, 18, 21, and 22.

8. **Represent comparisons with their contrast condition.** Paper 1 compares direct 5L, direct 3L, and mapped 5L scoring. Paper 5 compares response-level forms within language. Paper 7 compares frequency with severity and pain with discomfort. Paper 10 compares versions and populations. This supports user questions 13, 20, and 22 and prevents unconditional claims.

9. **Use sample stages instead of one sample-size value.** All ten papers need different counts for identified records, respondents, tasks, completed surveys, analyzed people, stable retest samples, or included studies. Paper 1 alone distinguishes 1,052 interviews from 1,014 analyzed. This supports user question 8.

10. **Treat products and product stage as structured concepts.** Paper 1 establishes a value set. Paper 5 produces a comprehension-tested descriptive system that still needs validation and valuation. Paper 3 describes an operational data infrastructure. Paper 8 produces a conceptual framework, not a revised EQ-HWB. Product type and stage support user questions 1, 14, 17, and 23.

11. **Keep principal finding, interpretation, implication, actual use, limitation, and gap separate.** The papers often recommend use without documenting adoption. Paper 1 expects decision use, paper 4 proposes priorities, and paper 10 says measures can support practice. These are not documented effects. This boundary supports user questions 15 to 18.

12. **Record evidence reuse and duplicate-data handling.** Paper 7 is a secondary analysis of dyadic data. Papers 2 and 9 consolidate linked publications. Paper 3 supplies a reusable infrastructure. This supports user questions 19 and 25.

13. **Preserve source conflicts as uncertainty.** Papers 5, 6, and 8 contain incompatible summary counts or percentages. Silent normalization would create false precision and would weaken user question 16.

14. **Make translation and cultural adaptation a study family and a specialized process.** Paper 15 links UK English EQ-5D-Y-5L, Egyptian Arabic EQ-5D-Y-3L wording, Modern Standard Arabic drafts, paper and digital forms, translator roles, child testing, revision, and approval. A generic instrument-development tag cannot answer user questions 4, 9, 14, 20, 21, and 23.

15. **Separate outcome representation from instrument name.** Paper 18 analyzes an unweighted EQ-5D-5L level sum score, not utility. Papers 13 and 20 analyze dimensions, profiles, EQ VAS, and utilities with different results. This distinction supports user questions 12, 13, 20, 21, and 22.

16. **Record the full outcome derivation route when scoring or mapping changes interpretation.** Paper 17 contrasts directly collected 5L profiles scored with an England value set, SF-12 values mapped to EQ-5D-3L by five routes, and SF-6D. Paper 20 compares a directly valued EQ-HWB-S utility with a mapped EQ-5D-5L utility. The route is necessary for user questions 3, 12, 13, 19, 20, and 21.

17. **Keep implementation outcomes separate from psychometric feasibility.** Paper 19 studies uptake, retention, acceptability, respondent burden, staff burden, timing, and collection mode at an oncology pilot. These do not show response missingness or measurement validity. A specialized Implementation Assessment supports user questions 9, 11, 15, 17, 20, and 21.

18. **Distinguish response mode, offered mode, and data-entry platform.** Paper 19 offers paper and REDCap routes but states that all responses were entered in REDCap. Paper 11 uses interviewer-administered online or face-to-face EQ-VT. This prevents false web-self-completion matches under user questions 11 and 20.

19. **Preserve reused-data provenance and harmonization limits.** Paper 20 combines two valuation-stage sources with different order, mode, periods, variable definitions, and available covariates. Paper 17 reruns existing survey and model inputs. A combined analysis is not a new independent sample. This supports user questions 5, 13, 19, and 25.

20. **Condition responsiveness on direction, anchor, interval, and analysis sample.** Paper 13 finds response to worsening but not improvement at six months, using self-reported change groups. Its one-month reliability sample has a different stability definition and count. This supports user questions 5, 8, 12, 15, 18, and 22.

21. **Do not stop at the broad DCE label.** Paper 12 shows that split-triplet DCE with duration and nonlinear time correction gave values close to EQ-VT, while a linear duration model did not. Task structure, duration, death framing, and time-preference form change the conclusion. This extends the valuation depth needed for user questions 10, 12, 13, 20, and 21.

22. **Record whether a method comparison uses the same or independent evidence.** Paper 12 compares independent samples with different collection periods and modes. Paper 20 combines sources, while paper 17 applies several derivation routes to the same dialysis responses. Evidence dependence changes the strength and meaning of comparisons under user questions 13, 19, 22, and 25.

23. **Distinguish expert review, respondent comprehension testing, and a revised product.** Paper 14 supplies expert judgments about EQ-TIPS version 2.0 but does not produce a revised instrument or test intended proxy respondents. Paper 15 revises and confirms wording with children and produces an approved language form. This supports user questions 6, 14, 15, 20, and 23.

24. **Represent allocated study factors and interactions.** Paper 22 crosses descriptive-system wording with adult or child perspective. Its significant interaction means neither factor has one unconditional effect. A Study Condition links allocation, factor level, task, and comparison without turning every covariate into an arm. This supports user questions 5, 10, 13, 20, and 21.

25. **Keep valuation-task feasibility separate from other feasibility concepts.** Paper 24 assesses time, moves, non-trading, understanding, state differentiation, and decision difficulty. Paper 19 assesses routine collection, and papers 13 and 23 assess instrument response properties. One feasibility label would create false method matches under user questions 9, 10, 12, 15, 20, and 21.

26. **Record operational anchoring and time preference in value derivation.** Paper 26 produces four materially different scales from the same DCE data by crossing immediate-death or zero-duration anchoring with linear or nonlinear time preference. Paper 22 also shows that death framing interacts with referent perspective. This supports user questions 10, 12, 13, 20, 21, and 22.

27. **Add cost-of-illness and health-burden depth without treating it as comparative economic evaluation.** Paper 25 needs condition, prevalence population, reference year, societal perspective, cost category, bearer, disability-weight route, monetization route, and sensitivity assumptions. It has no intervention alternatives. This supports user questions 1, 2, 7, 9, 12, 15 to 18, 20, and 21.

28. **Make population norms time- and derivation-specific products.** Paper 28 combines three source samples and supplies 2022–2023 profile, VAS, ceiling, index, and subgroup references scored with a named national value set. Its comparison rescored 2012 profiles by the same route. A country-level “norm available” flag would hide source, time, mode, outcome, and scoring differences needed for user questions 13, 14, 20, 22, and 23.

29. **Structure equity measures by construct, operationalization, role, outcome, and method.** Paper 21 uses family-income categories as predictors of utility. Paper 28 uses demographic strata, ordered logits, and Kakwani indices. Paper 30 tests education and perceived income within fixed profiles. These are not interchangeable “inequality” methods. This supports user questions 2, 7, 9, 12, 13, 15, 20 to 22, and 24.

30. **Represent data-quality controls as rules and actions, not a pass flag.** Paper 29 distinguishes bot, speed, duplicate, consistency, missingness, outlier, and quota indicators. Some exclude records, some change recruitment, and some redesign the later survey. Threshold, timing, unit, action, and denominator support user questions 8, 9, 12, 13, 16, 19, and 25.

31. **Trace nested, reused, and benchmark evidence across papers.** Paper 21 reuses the paper-19 oncology pilot. Paper 24 reuses paper 6. Papers 26 and 28 reuse Trinidad and Tobago valuation samples. Papers 29 and 30 extend EQ-DAPHNIE from paper 3. This reuse changes independence and prevents one cohort from appearing as several samples under user questions 5, 13, 19, 22, and 25.

32. **Do not equate an identical EQ-5D profile with identical underlying health.** Paper 30 deliberately conditions on profile and finds residual EQ VAS gradients. The authors cannot distinguish omitted health content from response-scale heterogeneity. Preserve the profile as an analysis condition and the mechanisms as alternatives. This supports user questions 2, 12, 13, 15, 16, and 22.

33. **Keep survey flow denominators and quality exclusions explicit.** Paper 29 reports invitation, link click, consent, completion, bot, speed, duplicate, and final-data stages. Paper 27 reports response, completion, flags, and interviewer actions. A single response-rate or analyzed-count field would misstate selection under user questions 8, 13, 16, 20, and 25.

34. **Keep property-level synthesis conditional on outcome derivation.** Paper 23 finds clear 5L gains for ceiling and informativity but mixed reliability and responsiveness. Two responsiveness studies use crosswalk-derived 5L indices. A broad “5L better” result would hide property, dimension or index form, and scoring route. This supports user questions 12, 13, 15, 18, 21, and 22.

35. **Record whether each component is planned, piloted, completed, or analyzed.** Papers 31 and 37 report completed development and pilot work inside protocols for larger planned studies. Without component status, a search can falsely return 2,000 observed PTO respondents, 1,400 observed DCE respondents, age weights, or EQ-TIPS preference findings that do not yet exist. This supports user questions 5, 8, 9, 14 to 16, 20, and 23.

36. **Separate social-priority elicitation from health-state valuation.** Paper 31 uses PTO to estimate relative weights for gains to age-defined beneficiary groups. It does not value an EQ-5D state. Beneficiary age, gain type and duration, counterfactual, group-size matching, forced or equivalence response, and output weight determine the method's meaning. This supports user questions 2, 6, 9, 10, 12, 13, 20, and 21.

37. **Distinguish experienced EQ VAS valuation from hypothetical VAS and ordinary overall-health measurement.** In paper 32, patients rate their own current health on EQ VAS, and the authors model those ratings against their observed profiles as experience-based state values. Dead is not anchored and broader health affects the outcome. This distinction changes retrieval and economic interpretation under user questions 3, 6, 10, 12, 13, 16, 20, and 22.

38. **Treat administration mode as separate from support, platform, recruitment, and feedback.** Paper 33 compares an online panel with automated tutorials against recruited face-to-face respondents with an interviewer and feedback module. A simple online-versus-face-to-face label would over-attribute differences to mode. This supports user questions 8, 9, 11 to 13, 16, 20 to 22, and 25.

39. **Record the exact proxy perspective and self-proxy agreement as a separate property.** Paper 34 uses proxy version 1, the caregiver's own assessment of the child, and compares it with independent child self-report. Proxy version 2 would ask a different question. Self-proxy agreement is not test-retest reliability and varies by condition and time. This supports user questions 3, 4, 6, 11 to 13, 15, 20 to 22, and 24.

40. **Represent language locale and intralingual cultural adaptation.** Paper 35 changes UK English to Singapore English while the language remains English. Local phrasing, comprehension tests, examples, endorsement, and intended geography are necessary to retrieve the actual language product. This supports user questions 4, 7, 9, 13, 14, 20, 21, and 23.

41. **Allow measurement properties to target an elicitation method and preserve analysis level.** Paper 36 tests the OPUF task chain, intermediate outputs, and derived utilities. Individual outputs are unstable while aggregate decrements are similar. Calling the whole result “reliable” or assigning it only to EQ-HWB-S would reverse the paper's main conclusion. This supports user questions 5, 9, 10, 12, 13, 15, 16, 20 to 22.

42. **Record preference elicitation architecture and exact choice-task form.** Paper 36 composes ranks, swing weights, level ratings, a dead-versus-worst choice, and an anchoring scale. Paper 37 contrasts sequential kaizen improvements with paired impaired profiles. The task sequence, goods or bads framing, intermediate output, and individual or aggregate target change burden and interpretation. This supports user questions 9, 10, 12, 13, 20, and 21.

43. **Separate instrument-structure preference evidence from value-set development.** Paper 37 will use DCE evidence to test severity-preference concordance and whether level differences influence choice. It does not yet QALY-anchor EQ-TIPS or estimate a scoring algorithm. This supports user questions 1, 3, 9, 10, 12, 14, 20, 21, and 23.

44. **Trace full value-set provenance, including the bridge population in a crosswalk.** Paper 38 shows that a same-country label can hide old 3L preferences, a response-mapping algorithm based on European patients, a target 5L system, and a later application sample. Same-respondent and independent-country comparisons also have different evidence dependence. This supports user questions 3, 4, 12 to 14, 19, 20, 22, 23, and 25.

45. **Keep analytic uncertainty separate from extraction uncertainty and trace inheritance.** Paper 39 distinguishes variability, heterogeneity, statistical uncertainty, and methodological variation across profile collection, valuation, mapping, synthesis, and decision modeling. These are properties of evidence and estimates. They are not conflicts in source wording. This supports user questions 12, 13, 16, 19, 21, and 22.

46. **Represent an implementation workflow and its maturity, not only implementation outcomes.** Paper 40 designs collection timing, self and proxy routes, item display, review ownership, participant-controlled flags, discussion, escalation, training, resources, and electronic-record integration. It is co-designed and mock-tested, not used in routine care. This supports user questions 5, 9, 11 to 17, 20, 21, and 23.

## Distinctions considered and rejected

- **A fixed universal field set.** Rejected because valuation, qualitative concept work, population infrastructure, HTA practice, and evidence synthesis require different depth. The common concepts above remain available without forcing empty fields.
- **One primary method label per paper.** Rejected because papers 1 and 6 connect different tasks to different model roles, while paper 9 compares many methods by outcome format and follow-up structure.
- **One paper-level population.** Rejected because evidence supplier, referent, target population, country component, and analysis subgroup can differ.
- **One generic “EQ-5D used” relation.** Rejected because it would mix administration, health-state valuation, scoring, comparison, review scope, and reported HTA practice.
- **A global class for every named model, coefficient, survey item, or qualitative code.** Rejected because these details do not all improve retrieval. Keep exact method names or local concepts as normalized values under stable method and topic families.
- **A separate finding record for every estimate or table cell.** Rejected by the fixed purpose. Keep decisive numbers in principal finding summaries and leave detailed estimates in source tables.
- **A binary “valid instrument” result.** Rejected because results depend on property, component, population, comparator, and criterion. Papers 2, 7, 8, and 10 show this dependency.
- **A binary “representative sample” result.** Rejected because quota targets, recruitment sources, response, weighting, and coverage limits determine what the claim means.
- **A universal best response scale.** Rejected because paper 7 finds different strengths for frequency and severity by trait level and intended instrument length.
- **A universal hierarchy of quality-of-life concepts.** Rejected because paper 8 assigns sleep and boredom to different parent themes than EQ-HWB. Keep instrument-scoped or study-scoped concept hierarchies and map them explicitly.
- **Author recommendation as impact or adoption.** Rejected. Record actual use only when the paper documents it.
- **Ethics, funding, authorship, and identifiers in the semantic ontology.** Rejected unless they change method interpretation. The fixed purpose assigns deterministic source metadata to other layers.
- **One “translation complete” flag.** Rejected because source form, target language and setting, administration form, review, child or respondent testing, approval, and transfer limits differ. Paper 15 requires these facts.
- **One broad “feasibility” property.** Rejected because paper 13 uses psychometric response feasibility, paper 15 uses comprehension and burden evidence, and paper 19 uses implementation uptake, follow-up, acceptability, and workflow evidence.
- **A new instrument product for each proposed content change.** Rejected because paper 14 reports expert suggestions for sleep, emotion, examples, and wording but does not produce a revised EQ-TIPS form.
- **One utility value without its derivation.** Rejected because papers 17 and 20 show that direct scoring, response mapping, direct utility mapping, crosswalk, target version, and preference source can change values and conclusions.
- **REDCap or LimeSurvey as proof of web self-completion.** Rejected because a platform can support interviewer administration, participant self-completion, later data entry, or storage. Papers 11, 12, and 19 require the actual response event.
- **A complete ontology of every economic-model state and parameter.** Rejected because paper 17 needs the main decision context, alternatives, outcome route, and assumptions, not a reconstruction of the Markov model.
- **A causal ontology for each observational predictor.** Rejected because paper 18 does not establish a full causal model. Preserve the paper's operational definition of education as an SES proxy, the main grouping variables, adjustment role, and author interpretation.
- **Method equivalence from correlation alone.** Rejected because papers 12 and 20 also use absolute differences, Bland-Altman analysis, concordance, or observed-state prediction. Association does not establish agreement.
- **One quality-control pass or fail field.** Rejected because paper 29 applies different rules to records, interviewers, recruitment, and survey design. A flag, exclusion, retraining action, and redesign have different meanings.
- **One response-rate value.** Rejected because paper 29 reports invitation, link click, consent, completion, and exclusion stages with different denominators. Store the exact stage rather than the authors' broad label.
- **One inequality method or result.** Rejected because papers 21, 28, and 30 use covariate association, subgroup norms, ordered response models, inequality indices, decompositions, and within-profile residual gradients.
- **Population norms without a reference period and scoring route.** Rejected because paper 28 rescored 2012 profiles with the later value set and combined three 2022–2023 sources. A norm is not timeless or independent of outcome derivation.
- **Identical profile as proof of identical underlying health.** Rejected because paper 30 cannot distinguish omitted health content from reporting heterogeneity. The profile is an observed classification, not a complete latent-health state.
- **Immediate death and zero duration as interchangeable anchors.** Rejected because paper 26 shows that they produce different scales, and nonlinear time preference changes both. Store conceptual and operational anchors separately.
- **Cost of illness as cost-effectiveness analysis.** Rejected because paper 25 estimates one condition's societal burden without comparing interventions, incremental outcomes, or an ICER.
- **A candidate model as an established national product.** Rejected because paper 24 demonstrates a possible cTTO-only youth model but does not replace the selected Chinese value set in paper 6.
- **Regional validity from author-proposed transfer.** Rejected because paper 27 estimates Trinidad and Tobago preferences. Use in other Caribbean countries remains a proposal, not demonstrated validity.
- **A protocol's target sample as observed evidence.** Rejected because papers 31 and 37 contain completed pilots or materials but no completed main sample or main-study findings.
- **PTO as another name for TTO.** Rejected because paper 31 varies the number of beneficiaries to estimate a social-priority weight, while TTO varies duration to value health.
- **Every EQ VAS response as the same outcome role.** Rejected because paper 32 uses self-rated overall health as experience-based valuation input, without a dead anchor. This differs from hypothetical-state VAS valuation and from ordinary descriptive reporting.
- **A pure mode effect from bundled samples.** Rejected because paper 33's online and face-to-face samples also differ in recruitment, supervision, tutorial, platform, incentives, and feedback.
- **One generic proxy-report form or proxy-validity result.** Rejected because paper 34's proxy version 1 asks for the proxy's view, while version 2 asks the proxy to predict the child's view. Agreement with self-report is a paired reporter comparison, not proof of substitution.
- **Same language as proof that no cultural adaptation occurred.** Rejected because paper 35 produces Singapore English forms from UK English through local review and child testing.
- **Instrument reliability and valuation-method reliability as interchangeable.** Rejected because paper 36 tests OPUF tasks and derived outputs. Its aggregate and individual results differ.
- **Every DCE as value-set development.** Rejected because paper 37 uses choice evidence to test the ordering and decision relevance of EQ-TIPS levels without a QALY anchor or scoring product.
- **A country-matched crosswalk as direct national preference evidence.** Rejected because paper 38's derived set inherits a source 3L value set and the crosswalk algorithm's bridge population.
- **Analytic uncertainty as an Extraction Uncertainty note.** Rejected because paper 39's uncertainty belongs to estimates and methods and can propagate into decisions. Extraction Uncertainty records ambiguity in the source or its normalization.
- **A co-designed implementation prototype as documented clinical use.** Rejected because paper 40 reports workshops and simulated visits. Routine pilot use and clinical effects remain planned.

## Unresolved cases

1. Paper 3 is both a design report and a report of completed fieldwork. The product can be called operational infrastructure with collected data, but the paper does not report full data release or downstream instrument results. Do not assign a stronger maturity stage.
2. Paper 3 has a country-specific instrument matrix. A later implementation must preserve this component relation. A paper-level union of all measures would cause false country matches.
3. Paper 4 cannot distinguish formal agency positions from staff views. It also cannot use the agency as the statistical unit because agency identifiers were not retained.
4. Paper 5 gives a 68% to 88% preference range in the abstract but 66% for Sweden in the result text.
5. Paper 6 describes 14 provinces or cities across five geographic parts and eight cTTO sites, but one key-point statement says four regions.
6. Paper 8 reports “68% (18/57)” subtheme alignment. The percentage and fraction conflict. The intended numerator is not clear from the paper text.
7. Papers use “ceiling” and “floor” inconsistently when they refer to best-health or worst-health responses. Extraction must store the actual endpoint and not rely on the label alone.
8. Paper 10 gives a broad favorable conclusion despite poor-to-moderate descriptive reliability and failed construct hypotheses in some comparisons. Preserve the property-level results and label the broad statement as author interpretation.
9. Paper 11 reports different mean ages in the abstract and results: 39 years with SD 10.8 against 32.1 years with SD 11.4. Its representativeness claim also does not align closely with all sex and emirate values in its table.
10. Paper 12 removed all public-place DCEd collection after high speeding and flatlining. The remaining evidence supports an online panel implementation, not all unattended or mixed-mode DCEd collection.
11. Paper 14 reports 44 invited experts, but its invited-group counts total 43. The reported nonattender and final-participant counts support 44 overall, but the group allocation is unresolved.
12. Paper 15 tested Modern Standard Arabic in Egypt. Its proposed use in other Arabic-speaking countries remains conditional on local validation and dialect or cultural adaptation.
13. Paper 17 cannot isolate mapping error from differences in source instrument, recall period, EQ-5D version, and value set because direct EQ-5D-3L responses were not available.
14. Paper 18 reports that education effects were canceled after adjustment, but a small adjusted UK association remained. Preserve the country-specific model results rather than the broad conclusion alone.
15. Paper 19 gives willingness percentages with two denominators. The abstract uses 170 initial participants. The results use 160 feasibility respondents. The proxy-completion count and response-mode distribution are not reported.
16. Paper 20 combines sources whose long-term-condition question, mode, instrument order, period, and available variables differ. Some known-group analyses apply only to one source. These facts limit any combined-sample result.
17. Paper 13 calls both index and EQ VAS worsening effect sizes large. Its stated interpretation rules classify the index statistics as moderate and small. Store the method-specific estimates and directions.
18. Paper 21 reuses the 170-person paper-19 pilot and reports full-sample regression with demographic covariates, while the earlier paper reports only 160 optional demographic-questionnaire completers. The present paper does not explain the denominator difference. Actual response-mode distribution also remains unknown.
19. Paper 22 states nine DCE health-state pairs in the task description and shows nine in the table, but the design paragraph says ten pairs were implemented. A technical error removed a planned block. The exact implemented pair count is unresolved. The result narrative assigns 205 respondents to Spain and 200 to the Netherlands, while the study-arm table assigns 200 to Spain and 205 to the Netherlands.
20. Paper 23 reports 215 full texts and 190 exclusions but then gives 20 included reports, not the arithmetical remainder of 25. The later update adds four, and the final count of 24 agrees with the abstract.
21. Paper 24 reports 216 males as 48.33% and 202 females as 51.67%, but the counts give the opposite percentages. The narrative supports 51.67% female but not the corresponding count.
22. Paper 26 describes both panel and public-place recruitment for the reused DCE-with-duration study. Paper 12 states that all public-place data were removed. Treat the 970-person final sample as retained panel evidence. Paper 26 also refers to the “other 4 choices” after selecting one of four model-anchor combinations; only three alternatives remain.
23. Paper 27 reports 236 negative predicted states, or 7.6%, in the abstract and 275 states, or 8.8%, in the results. Both statements refer to the direct EQ-VT value set.
24. Paper 28 calls its inputs three studies in the abstract, then two studies and three surveys in the methods. It reports a May 2023 collection end in the abstract and discussion, but survey 3 is stated to run through August 2023. It claims mutually exclusive samples while acknowledging possible overlap between the first non-panel survey and later panels.
25. Paper 29 defines reCAPTCHA exclusion as below 0.5 in one passage and 0.5 or less in another. Its speed threshold similarly changes from under five minutes to five minutes or less. The boundary cases cannot be normalized from the paper.
26. Paper 30 reports ages 25 to 79 in the abstract but says only people older than 80 were excluded in the methods, which would retain age 80. Its low-EQ-VAS exclusion also removes some observations that could represent the extra-domain health or response heterogeneity discussed as explanations. Preserve the age conflict and condition findings on the stated exclusion rule.
27. Paper 31 says that at least 14 convenience respondents piloted the survey in addition to three Consumer Advisory Group members. It later describes the pilot group as 14 people, eight male and six female. The demographic statement appears to describe the convenience group, but its scope is not explicit. Do not add the groups into a single exact pilot count without qualification.
28. Paper 32 combines nine registers with different collection procedures and reports one total of 172,070 patient records. Exact administration mode and important stage counts by register and time point are not available in the paper text. Do not infer one common mode or a uniform longitudinal cohort.
29. Paper 33 describes both samples as US adults quota-matched to the adult general population, but the online sample's reported age range begins at 17. The eligibility status of that respondent is unresolved.
30. Paper 34 used in-progress UK English EQ-5D-Y-5L self and proxy forms translated into Bahasa Indonesia with version-management collaboration. The paper supports experimental-form testing but does not state that it created an officially approved Bahasa Indonesia proxy product.
31. Paper 35 adapted both Y-3L and Y-5L, but its separate content-validity interviews administered only Y-3L because the target was the common descriptive-system concepts. Do not treat this as direct content-validity testing of the Y-5L response levels or EQ VAS.
32. Paper 36 finds stable aggregate but unstable individual OPUF outputs. It cannot determine whether individual instability comes from the OPUF architecture, EQ-HWB-S complexity, online administration, or their interaction. Preserve these as alternative explanations.
33. Paper 37 states planned age quotas of 18–29, 30–44, 45–64, and 55 years or older. The last two categories overlap. The intended implemented boundary is not clear.
34. Paper 38 finds a persistent worst-mobility disagreement in same-sample and reverse-crosswalk analyses. It still cannot quantify the separate effects of label wording, crosswalk response mapping, task coverage, valuation method, source period, preference population, and model. Preserve the mobility explanation as author interpretation rather than an isolated causal estimate.
35. Paper 40 reports nine service providers in the abstract and 11 service providers in the results. It also calls the work clinical-setting use, although the reported evidence is co-design and simulated visits rather than routine collection. Preserve both counts and the prototype maturity boundary.

## Consolidation decision record

### Scope and result

The consolidation reviewed the current ontology and all 40 paper applications against the 40 manifest sources. It also tested each concept added in rounds 2 to 4 against the earlier applications. All 40 applications remain covered. No application needed a new substantive paper fact. Three value-set applications needed clearer product-status wording, and several applications needed only controlled Study Family normalization.

The final ontology remains paper first. Study Components, Study Conditions, methods, products, comparisons, and findings remain subordinate to the Paper. The consolidation did not add a paper, a mandatory field set, or a fixed output schema.

### Consolidated terms and boundaries

1. **Study Family now records research purpose, not every method used.** The former `mapping, scoring, or statistical-method study` term mixed a substantive product family with any paper that used or reviewed statistics. Mapping and scoring remain one family. Preference-elicitation method studies have their own family. Statistical models remain Method Uses or paper topics. Paper 9 is an evidence synthesis about statistical practice, papers 12 and 26 are empirical preference-method studies, and paper 39 is conceptual and reporting guidance.
2. **Implementation is separate from reported use or practice.** Paper 4 reports practitioner use and opinion. Papers 19 and 40 study implementation and workflow. The former combined family could return practitioner surveys as implementation trials. The final terms prevent this false match.
3. **Protocols are separate from data resources.** Papers 31 and 37 describe planned studies with completed design work. Papers 3 and 29 describe a multi-country research infrastructure with collected data. Component Status still records the status of each local part.
4. **`Psychometric` is a search synonym, not a second controlled family.** The controlled family is measurement-property study. The property terms supply the useful retrieval depth.
5. **Product maturity uses separate dimensions.** Status, evaluation evidence, governance or endorsement, derivation, and documented use are not one sequence. Papers 1, 6, 11, and 27 produce estimated value sets that authors recommend. Paper 15 produces a version-management-approved language form. Paper 40 produces a co-designed and simulated prototype. Paper 19 documents a pilot use. The term `established` was removed as a controlled stage because it can imply any of these facts, including adoption that the paper does not show.
6. **Specialized method concepts do not create parallel records.** Valuation Task Use, Measurement Property Assessment, Implementation Assessment, Survey Data Quality Control, and the other specialized concepts are profiles of one Method Use. This resolves an internal duplicate-record risk without removing domain detail.
7. **Agreement is both a property and a comparison, but it is one assessment.** Cross-instrument and cross-informant agreement link one Measurement Property Assessment to its Comparison. Papers 20 and 34 support this boundary. Correlation alone remains association, not agreement.
8. **Data quality, missing-data handling, and sensitivity analysis are separate method families.** Paper 29 uses operational controls that can exclude a record or change recruitment. Paper 9 reviews missing-data handling. Papers 1 and 11 use sensitivity analysis for model robustness. The former combined label was too broad.
9. **Late-round concepts remain optional and evidence led.** A late concept was not added to an earlier application only to make records look uniform. It was applied when it prevented a false statement or enabled a material retrieval distinction.

### Review of all 40 applications

| Paper | Late or consolidated concept tested | Consolidation decision |
|---:|---|---|
| 1 | Product maturity; provenance; analytic model | Replaced `established` with final reported, estimated, and author-recommended. Existing task and crosswalk detail was sufficient. |
| 2 | Specialized measurement-property assessment; evidence reuse | No content change. The application already separates property, outcome, synthesis, and duplicate-data handling. |
| 3 | Component status; research infrastructure; country-level instrument relations | Normalized the family label. Pilot, completed rounds, and planned later work were already distinct. |
| 4 | Reported practice against implementation; instrument object role | Normalized the family label. No implementation claim or instrument administration was added. |
| 5 | Product maturity; locale; component status | No change. Draft, comprehension testing, harmonization, language forms, and future validation were already separate. |
| 6 | Valuation model; referent; product derivation | No change. Independent task samples, child referent, hybrid model, estimated product, and gaps were already explicit. |
| 7 | Property target beyond an instrument; response-scale comparison | No change. The response-scale items, properties, trait regions, and recommendation limit were already explicit. |
| 8 | Content-validity aspect; study-local framework | No change. Comprehensiveness, the comparison framework, culture, and numeric uncertainty were already distinct. |
| 9 | Study Family against statistical method topic; outcome representation | Normalized the family label to evidence synthesis. Existing method-use taxonomy and EQ-5D component detail was sufficient. |
| 10 | Cross-instrument comparison; property-specific result | No change. Reliability, validity, known groups, analysis samples, and broad author conclusion were already separated. |
| 11 | Product maturity; language locale; administration support | Replaced `established` with final reported, estimated, and author-recommended. Existing language, mode, and quality detail was sufficient. |
| 12 | Preference-method family; time preference; data-quality control | Normalized the family label. The independent samples, split-triplet task, exclusions, and nonlinear model were already explicit. |
| 13 | Directional responsiveness; stability sample | No change. Worsening, improvement, interval, anchor, and analysis counts were already distinct. |
| 14 | Product review evidence; intended proxy role | No change. Expert review was not promoted to a revised product or intended-respondent validation. |
| 15 | Locale-specific adaptation; governance approval | No change. Source and target forms, Egypt testing, paper and digital forms, approval, and transfer limit were already explicit. |
| 16 | Measurement property against instrument revision | No change. Bolt-on performance did not become a scored utility or a decision to revise EQ-5D-5L. |
| 17 | Product provenance chain; decision uncertainty | No change. Direct, mapped, response-mapped, and SF-6D routes and the model consequence were already explicit. |
| 18 | Equity family; outcome representation | Normalized the family label. The unweighted level sum score remained distinct from utility and EQ VAS. |
| 19 | Implementation family; workflow maturity; offered against used mode | Normalized the family label. The site pilot, retention, burden, missing route counts, and planned scale-up were already explicit. |
| 20 | Reused-data provenance; cross-instrument agreement | No change. Source differences, score routes, association, agreement, and transfer limits were already explicit. |
| 21 | Equity family; reused sample; covariate role | Normalized the family label. The application already avoids a causal or distributional cost-effectiveness result claim. |
| 22 | Study Condition; interaction; referent and death framing | Normalized the preference-method family label. The factorial interaction and task-count uncertainty were already explicit. |
| 23 | Property-level evidence synthesis; outcome derivation | No change. 3L and 5L results remain conditional on property, sample, and crosswalk route. |
| 24 | Preference-method family; task feasibility; candidate product | Normalized the family label. The cTTO-only model remains a candidate and does not replace paper 6's product. |
| 25 | Burden family; non-EQ outcome; cost bearer | Normalized the population-health label. DALYs, monetized wellbeing, and cost categories remain separate from EQ-5D and cost-effectiveness. |
| 26 | Preference-method family; operational anchor; time preference | Normalized the family label. Four scale constructions and the independent cTTO benchmark were already explicit. |
| 27 | Product maturity; crosswalk provenance | Replaced `established` with final reported, estimated, and author-recommended. Existing direct-versus-mapped comparison detail was sufficient. |
| 28 | Norm and equity families; product reference period; reused sources | Normalized the family labels. The three source samples, common scoring route, time comparison, and overlap uncertainty were already explicit. |
| 29 | Data-quality family; rule, unit, action, and denominator | Normalized the family label. Threshold conflicts and documented redesign effects were already explicit. |
| 30 | Equity family; profile as an analysis condition | Normalized the family label. Alternative mechanisms and the low-EQ-VAS exclusion remained conditional and unresolved. |
| 31 | Component status; distributional preference task | No change. Completed pilots and planned main work remain separate, and PTO does not become health-state valuation. |
| 32 | Experience-based valuation role; administration uncertainty | Normalized the family label. Current self-rated health, lack of a dead anchor, group and time differences, and register-mode limits were already explicit. |
| 33 | Administration support; bundled mode comparison; task quality | Normalized the family label. The application does not infer a pure mode effect or reject all online TTO designs. |
| 34 | Proxy perspective; cross-informant agreement | No change. Proxy version 1, independent completion, stability rule, and self-proxy agreement were already explicit. |
| 35 | Language locale; intralingual adaptation; content-validity scope | No change. Singapore English remains distinct from UK English, and Y-3L content evidence was not extended to Y-5L levels or EQ VAS. |
| 36 | Preference architecture; property target; analysis level | Normalized the family labels. Individual instability and aggregate stability remain separate. |
| 37 | Component status; instrument-structure preference assessment | Normalized the family labels. Planned choice evidence does not become an observed result, final instrument, or value set. |
| 38 | Product provenance chain; same-sample dependence | No change. Crosswalk bridge evidence, direct values, reverse mapping, and external profile application were already explicit. |
| 39 | Analytic uncertainty; conceptual guidance family | Normalized the family label. Analytic uncertainty remains separate from extraction uncertainty. |
| 40 | Implementation workflow; product maturity | Normalized the family label. Co-design and simulated visits remain distinct from routine use and clinical effect. |

### Consolidation unresolved cases

- The 35 source-specific cases in the earlier Unresolved cases section remain unresolved. The source review did not supply a safe basis to choose between the conflicting counts, percentages, thresholds, dates, modes, or maturity claims.
- Paper 3 still does not show full data release or downstream use of the infrastructure.
- Papers 19 and 21 still do not report the response-mode distribution, and paper 19 does not report the proxy-completion count.
- Paper 32 still does not report one harmonized administration mode or detailed flow for all registers and time points.
- No ontology-level term boundary remains unresolved after the controlled-term and product-maturity changes above.

### Consolidation distinctions considered and rejected

- **Keep `statistical-method study` as a universal Study Family.** Rejected because it joins evidence synthesis, empirical preference-method comparisons, equity analyses, and conceptual guidance only because they use or discuss statistics.
- **Keep `established` as a Product Stage.** Rejected because the 40 papers use different evidence for final estimation, recommendation, approval, pilot use, routine use, and adoption.
- **Force every late-round concept into every earlier application.** Rejected because absent or immaterial concepts would add empty detail. The audit records why each earlier application did or did not change.
- **Create both a general Method Use and a specialized method record.** Rejected because it duplicates one method act and can produce double counts.
- **Create a separate agreement result and measurement-property result.** Rejected because agreement is one property assessment linked to a comparison.
- **Treat all completed work inside a protocol as the main study result.** Rejected because papers 31 and 37 contain completed design and pilot work but no completed main sample or main outcome.
- **Use a single ordered maturity ladder for all products.** Rejected because review evidence, governance approval, estimation, recommendation, and documented use are independent dimensions.

## Source verification

### Batch 01

All ten batch-01 article files matched both manifest values.

| Order | Paper | Bytes | SHA-256 status |
|---:|---|---:|---|
| 1 | `10.1007/s40258-021-00639-3` | 77,402 | Match |
| 2 | `10.1007/s11136-020-02688-y` | 121,988 | Match |
| 3 | `10.1007/s11136-025-03983-2` | 73,694 | Match |
| 4 | `10.1017/s0266462326103602` | 101,826 | Match |
| 5 | `10.1007/s11136-019-02115-x` | 69,271 | Match |
| 6 | `10.1007/s40273-022-01216-9` | 55,701 | Match |
| 7 | `10.1007/s11136-025-04003-z` | 58,977 | Match |
| 8 | `10.1007/s11136-025-04038-2` | 76,716 | Match |
| 9 | `10.1016/j.jval.2025.02.001` | 50,386 | Match |
| 10 | `10.1007/s10198-025-01770-x` | 173,513 | Match |

### Batch 02

All ten batch-02 article files matched both manifest values.

| Order | Paper | Bytes | SHA-256 status |
|---:|---|---:|---|
| 1 | `10.1016/j.jval.2025.01.003` | 55,884 | Match |
| 2 | `10.1016/j.jval.2024.05.016` | 48,268 | Match |
| 3 | `10.1186/s12955-023-02177-z` | 44,049 | Match |
| 4 | `10.1007/s11136-025-04150-3` | 101,717 | Match |
| 5 | `10.1186/s41687-025-00985-z` | 49,236 | Match |
| 6 | `10.1016/j.jval.2024.03.2195` | 61,107 | Match |
| 7 | `10.1007/s10198-018-0987-x` | 39,487 | Match |
| 8 | `10.3389/fpubh.2021.744405` | 134,250 | Match |
| 9 | `10.3390/curroncol32060308` | 50,596 | Match |
| 10 | `10.1016/j.jval.2024.05.007` | 47,849 | Match |

### Batch 03

All ten batch-03 article files matched both manifest values.

| Order | Paper | Bytes | SHA-256 status |
|---:|---|---:|---|
| 1 | `10.3390/curroncol32110645` | 58,691 | Match |
| 2 | `10.1016/j.jval.2018.05.002` | 42,129 | Match |
| 3 | `10.1007/s40273-018-0642-5` | 84,553 | Match |
| 4 | `10.1016/j.jval.2023.03.003` | 28,961 | Match |
| 5 | `10.1038/s41433-023-02860-x` | 71,413 | Match |
| 6 | `10.1177/0272989x251325828` | 42,340 | Match |
| 7 | `10.1186/s12955-024-02266-7` | 123,881 | Match |
| 8 | `10.1186/s12955-024-02323-1` | 106,425 | Match |
| 9 | `10.1007/s11136-025-04074-y` | 90,076 | Match |
| 10 | `10.1007/s11136-026-04294-w` | 49,090 | Match |

### Batch 04

All ten batch-04 article files matched both manifest values.

| Order | Paper | Bytes | SHA-256 status |
|---:|---|---:|---|
| 1 | `10.1371/journal.pone.0302886` | 188,611 | Match |
| 2 | `10.1186/s12955-023-02115-z` | 110,575 | Match |
| 3 | `10.1007/s11136-020-02712-1` | 66,890 | Match |
| 4 | `10.1186/s12955-022-01996-w` | 61,492 | Match |
| 5 | `10.1186/s12955-024-02290-7` | 52,978 | Match |
| 6 | `10.1007/s10198-025-01769-4` | 78,866 | Match |
| 7 | `10.1136/bmjopen-2025-100897` | 42,479 | Match |
| 8 | `10.1007/s40258-025-00954-z` | 68,428 | Match |
| 9 | `10.1177/0272989x251380556` | 59,876 | Match |
| 10 | `10.1007/s11136-025-03996-x` | 69,560 | Match |

## Run note

### Round 1

Fresh Candidate 1, round-1 restart on 2026-08-16. The run used only the fixed version-2 purpose, user questions, task, protocol, README, batch-01 manifest, local `AGENTS.md`, and the ten manifest articles. No prior lineage record was present. No version-1, legacy extraction, graph, later-batch, probe, holdout, or other-lineage file was inspected. The paper files and manifest had no mechanical mismatch. The source text itself contains the unresolved statements listed above. The repository ignores the `lineage/` directory, so ordinary Git status does not show this record. The file is present at the required path. No commit was made.

### Round 2

Fresh Candidate 1, round 2 on 2026-08-16. The run used the fixed version-2 purpose, user questions, task, protocol, README, batch-02 manifest, current Candidate 1 record, local `AGENTS.md`, and the ten batch-02 articles. No version-1, legacy extraction, graph, later-batch, probe, holdout, or other-lineage file was inspected. Outside the assigned papers and supplied version-2 files, the only filesystem file read was the worktree-local `AGENTS.md`. All article hashes and byte counts matched. An initial command looked for `batches/batch-02.tsv` at the worktree root and received a file-not-found message; the supplied manifest was then found at `pilot/ontology-development-v2/batches/batch-02.tsv`. This path correction did not change any file. The first final-check command had a shell-quoting error around DOI backticks and tried to run a DOI as a command. A corrected check then passed. The failed check did not change a file. No commit was made.

### Round 3

Fresh Candidate 1, round 3 on 2026-08-16. The run used the fixed version-2 purpose, user questions, task, protocol, README, batch-03 manifest, current Candidate 1 record, local `AGENTS.md`, and the ten batch-03 articles. Outside the assigned papers and supplied version-2 files, the only file whose contents were read was the worktree-local `AGENTS.md`. No version-1, legacy extraction, graph, later-batch, hidden-probe, holdout, Git-history, or other-lineage content was inspected. All article hashes and byte counts matched. An initial discovery command enumerated file names in the sparse worktree and printed names of earlier-batch corpus files. It did not open or read those article contents. This was the only mechanical scope issue. The first final-validation command used zsh's read-only `status` variable and stopped before running its checks. A corrected command used a task-specific variable and passed all coverage, section, hash, and byte checks. Neither issue changed a file. No commit was made.

### Round 4

Fresh Candidate 1, round 4 on 2026-08-16. The run used the fixed version-2 purpose, user questions, task, protocol, README, batch-04 manifest, current Candidate 1 record, local `AGENTS.md`, and the ten batch-04 articles. Outside the assigned papers and supplied version-2 files, the only file whose contents were read was the worktree-local `AGENTS.md`. No version-1, legacy extraction, graph, hidden-selection, hidden-probe, holdout, Git-history, or other-lineage content was inspected. All article hashes and byte counts matched. An initial discovery command looked for a `batches` directory at the worktree root and received a file-not-found message, then enumerated file names under the supplied version-2 directory. This printed the names of the earlier batch manifests but did not open or read their contents. A large initial read of the current lineage record was truncated by the command-output limit, so the record was reread in line ranges. The first final coverage check used unsafe shell quoting around DOI backticks and tried to execute the first DOI as a command. It stopped before completing the coverage loop. A corrected check passed. A later sequence check used a `seq -s` option that this system does not support and stopped without changing the record; a portable sequence check then passed. These mechanical issues did not change a file or expose excluded content. No commit was made.

### Consolidation

Fresh Candidate 1 consolidation on 2026-08-16. The run used only the worktree-local `AGENTS.md`, the fixed version-2 purpose, user questions, task, protocol, README, all four batch manifests, the complete current Candidate 1 record, and all 40 manifest articles. Outside the supplied version-2 files and articles, the only file whose contents were read was `AGENTS.md`. Git status and tracking checks read repository index metadata for this exact lineage path. They did not inspect Git history or another file's contents. No version-1 work, legacy graph or extraction file, hidden selection label, hidden probe, holdout paper, other lineage, skill file, external guidance, or Internet source was inspected.

All 40 article hashes and byte counts matched their manifests. The application audit covered papers 1 through 40. The consolidation changed controlled family labels, product-maturity guidance, duplicate-record guidance, three value-set product descriptions, and the explicit consolidation record. It did not add a paper or infer a new result. Two large read commands reached the command-output limit. The lineage record was reread in smaller complete line ranges, and the paper review continued with bounded and targeted source reads. An initial final check counted all numbered table rows, including source-verification rows, instead of only the 40-row application audit and stopped. The next check stopped because `rg` returned a no-match status for an empty code-fence set. A bounded audit count and an `awk` fence check then passed. These mechanical issues did not change a source or expose excluded content. Final coverage, section, Markdown, hash, and byte checks passed. No commit was made.
