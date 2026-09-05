# Paper-first EuroQol research ontology and extraction guide

## Purpose and limits

Use this guide to find EuroQol research papers and to understand their purpose, evidence, methods, products, findings, and author-reported meaning. The paper is the main research record. Deterministic source facts, such as DOI, title, authors, dates, journal, licence, funding, and references, stay in the linked JATS layer.

This guide is not a general research ontology. It is not a fixed form. Record only information that applies. Capture principal findings and decisive values. Do not reproduce each estimate or build a detailed claim graph.

Use four forms of information:

- controlled terms for stable cross-paper categories;
- repeatable structured facts for variable details;
- explicit relations for roles, derivations, comparisons, and dependencies;
- concise narrative for paper-specific rationale, context, and meaning.

Keep `absent`, `not reported`, `unclear`, `conflicting`, and `not applicable` separate.

## Paper and component rule

For each paper, record a concise research aim, contribution, applicable study families, research execution, material topics, and principal outputs.

Create a paper-local component only when it prevents a false paper-level statement about a phase, sample, task, country or language arm, time point, analysis, status, or product. Give the component a short functional name and its own evidence, methods, status, and findings as needed. A condition or arm is subordinate to its component. Do not create components for section headings, tables, ordinary regressions, or each outcome.

Use relations such as `part of`, `precedes`, `informs`, `depends on`, `uses evidence from`, `administers`, `values`, `scores with`, `compares with`, `tests`, `produces`, `derives from`, `reuses`, `updates`, and `supersedes`. State the objects at both ends of a relation.

Record component execution as `planned`, `piloted`, `data collection complete`, `analyzed`, or `reported`, when needed. At paper level, state whether the paper reports planned research, ongoing work, completed primary research, a completed secondary analysis, a completed synthesis, or conceptual or method guidance. Do not store `mixed status`. Derive it from component statuses when a user asks for it.

Protocol has four strict roles:

- A paper can have the purpose `protocol publication` and the research execution `reports planned research`. This is not a study family, and it does not say that the planned components are complete.
- A component can be planned or piloted. This is component status.
- A paper can produce a named, reusable conduct plan or material set. This is a protocol product.
- A component can use a named protocol or technology. This is a method relation.

Do not tag an operating infrastructure as a protocol only because it uses governed procedures.

## Controlled study families

Use one or more purpose-based families. Add a family only when it describes a material purpose, not only a method that the paper uses.

| Final study family | Boundary |
|---|---|
| Health-state valuation | Elicits or models values for health states. It does not require a released value set. |
| Value-set development | Produces or selects a scoring value set. Also tag health-state valuation when the paper collects valuation evidence. |
| Preference-method study | Tests an elicitation, anchoring, or preference-model method as a research target. Name the exact method and purpose. Do not use a broad `methods study` tag. |
| Social-priority weighting | Elicits the relative social value of health gains or beneficiary groups. It does not produce health-state utilities by itself. |
| Instrument development or revision | Creates or changes concepts, items, response labels, forms, or configurations. |
| Translation | Changes wording between languages. |
| Cultural adaptation | Adapts wording or use for a locale or culture, including same-language localization. It can occur with translation. |
| Measurement-property study | Assesses a specific property of an instrument, item, score, reporter form, task, method, or product. |
| Qualitative concept study | Elicits concepts or builds a paper-local framework. Content validity remains an exact assessment target, not a second family by default. |
| Mapping or scoring | Develops, tests, or applies a mapping, crosswalk, or scoring route as a main purpose. For valuation-scale anchoring or transformation, keep the exact task-to-scale path. Do not retrieve it as instrument mapping or economic use unless those separate outputs exist. |
| Population-health study | Describes health or related outcomes in a population. |
| Population-norm study | Produces or updates a dated reference distribution or norm product. |
| Health-equity or inequality | Measures a social gradient, inequality, decomposition, or conditional equity relation. |
| Economic evaluation or decision modeling | Compares alternatives through QALYs, costs, ICERs, or another decision model. |
| Cost-of-illness or burden-of-disease | Estimates non-comparative cost or burden, such as DALYs, years lived with disability, or monetary burden. |
| Implementation study | Studies introduction, workflow, uptake, acceptability, burden, barriers, or routine use. A general feasibility result is not sufficient. |
| Professional-practice or policy survey | Elicits professional views, reported practice, or policy needs. It does not prove agency policy or implementation. |
| Evidence synthesis | Searches for and synthesizes publications, studies, trials, or data sets. |
| Survey-method or data-quality study | Studies survey-process quality, response quality, or a material survey method. |
| Research-infrastructure or data-resource study | Describes or evaluates a reusable project, data collection, or resource. |
| Conceptual or methodological guidance | Develops concepts, uncertainty accounts, reporting guidance, or non-empirical method guidance. |

If none fits, state the exact purpose in narrative and flag the need for later vocabulary review. Do not add an `other` tag during routine extraction.

## Evidence, people, and context

Keep these roles separate for each applicable component:

- **Evidence provider:** a respondent, expert, document, publication, trial, data set, record, organization, or other source of evidence.
- **Respondent:** the person who answers an instrument, interview, survey, or preference task.
- **Referent:** the person, health state, practice, or object that the answer describes.
- **Reporting perspective:** self-report, proxy perspective 1, proxy perspective 2, expert or professional opinion, or another stated perspective.
- **Target population:** the population to which the result or product is intended to apply.
- **Decision context:** the clinical, economic, policy, social-care, research, or instrument-development use.

Use `proxy perspective 1` only when the proxy gives their own assessment of the referent's health. Use `proxy perspective 2` only when the proxy estimates how the referent would report their own health. Keep the exact form identity, author wording, requested perspective, and observed response behavior separate. If the source does not state the requested perspective, record `not reported`.

For proxy evidence, record the proxy relationship, referent, exact form, requested perspective, time point, and independent or joint completion. Keep cross-informant agreement separate from test-retest reliability.

Record country and subnational region, instrument or task language, age, health condition, clinical area, care or community setting, policy setting, sampling frame, selection, recruitment, main inclusion and exclusion rules, and transfer limits when they change use or interpretation.

Use repeatable evidence-stage counts for the material flow. Examples are frame or invited, opened, consented, eligible, enrolled, completed, quality flagged, excluded, retained, weighted, and analyzed. Give the denominator for a rate. Do not reduce representativeness to one flag.

## Instruments, versions, language, and roles

For each material instrument involvement, record:

- family and exact version;
- adult or youth form, level count, long or short form, variant, experimental status, and base-plus-bolt-on configuration;
- self or proxy form and proxy perspective when reported;
- language and locale or language variety as separate facts;
- instrument component, such as descriptive system, item, response label, EQ VAS, or derived index;
- linked component, population, and role.

Use exact roles. The useful roles are target of development, target of valuation, target of measurement-property assessment, administered measure, comparator or convergent measure, criterion or anchor, source of health-state descriptions, source of concepts or labels, source version for translation, reference version for language decisions, target or product of translation or adaptation, scoring or value-set source, mapping source or target, experience-based valuation input, object of structure-preference testing, and object of a review or practice survey.

Do not use a broad `used` role when the source gives a precise role. Do not turn a background mention into instrument involvement.

## Administration and task context

An administration statement links an instrument or task to its component, respondent, referent, and time point. Keep these axes independent:

- reporting perspective;
- human contact, such as none, remote, telephone, or face-to-face;
- support, such as unsupervised, available for questions, guided, or full interviewer administration;
- medium or channel, such as web, app, other digital form, paper, or spoken response;
- setting, such as home, school, clinic, public place, or panel session;
- named platform, protocol technology, tutorial, feedback, or quality review;
- mode offered, selected, used, and later data-entry route;
- order, randomization, timing, recall period, and recruitment source when material.

A web platform does not prove unsupervised self-completion. Staff entry of a paper response into a digital system does not make the response a web response. When administration features vary together, record a bundled comparison. Do not assign the result to one feature without an identifying contrast.

For factorial or multi-condition work, record factors, levels, allocation, crossed or nested structure, interactions, and linked comparisons. Do not treat an observational covariate as an assigned condition.

## Common method-use pattern

Represent each material method use as:

`component -> evidence or input -> exact task or method -> purpose or exact assessment target -> inference or output`

Record the stable method family and the exact named method. Link the method to its component, input, population, comparison, and product. For a model, record its input outcome, inferential purpose, material specification, candidate-versus-selected role, and output. Do not create a second generic method statement when a specialized profile below describes the same act.

Do not store an extra assessment-class value. Derive broad groupings from the exact method purpose and target. For example, a bot score is survey-process quality, preference-order concordance is an instrument-development criterion, prediction error is method performance, and responsiveness is a measurement property.

## Family-specific profiles

### Valuation, preference methods, and social priority

For each task, record its exact form, such as cTTO, conventional TTO, lead-time or lag-time TTO, DCE, DCE with duration, DCE with immediate death, PTO, VAS, or a compositional task. Record its purpose separately: health-state cardinal valuation, relative preference estimation, anchoring, social-priority weighting, instrument-structure preference testing, task feasibility, or sensitivity analysis.

Record respondent and referent, hypothetical or experienced-own-health perspective, state or gain framing, duration and worse-than-dead framing, experimental design and blocks, task count, order, protocol and technology version, administration, training, quality rules, and analyzed evidence when material.

For scale construction, keep task, operational anchor basis, mathematical scale transformation, time-preference form, preference heterogeneity, model, and resulting scale separate. Immediate death, zero duration, and observed cTTO means are different anchor bases. A time-preference parameter in DCE with duration is not an economic discount rate.

For compositional methods, record ordered steps and intermediate outputs, the anchoring step, final derivation, and individual or aggregate target. For PTO and related social-priority tasks, record beneficiary groups, decision-maker perspective, gain and duration, counterfactual, group sizes, iteration rule, forced choice or equivalence option, and output weight. Do not call this output a value set.

### Instrument development, language work, qualitative work, and properties

For development, translation, or adaptation, preserve each material stage and output: concept or item generation, wording or label work, sorting or response scaling, forward and back translation, reconciliation, cognitive interview, comprehension test, harmonization, revision, proofread, governance review, psychometric test, and valuation. Record source, reference, and target versions; source and target language and locale; administration forms; participant role; revision cycle; and approval when reported. Keep an author claim about wider transfer separate from evidence in the tested locale.

For qualitative concept work, record the conceptual starting point, sampling, interview or group method, language, coding method, coder process, inductive and deductive inputs, comparison framework, saturation statement, output concepts, and scoped inference. Keep a paper-local framework local.

For each measurement-property assessment, record the exact target, property, subtype, population or subgroup, comparator or anchor, interval, analytic method, prespecified criterion, assessment level, direction, and result. Supported properties include feasibility or missingness; distribution, ceiling, and floor; test-retest reliability; measurement error; content validity with relevance, comprehensibility, or comprehensiveness; construct validity with convergent, structural, discriminative, or known-groups evidence; responsiveness and minimal important difference; informativity; item discrimination and information; differential item functioning; cross-informant agreement; and cross-instrument agreement. This list is not exhaustive. Response-process behavior, recall-period interpretation, and instruction or perspective adherence can be exact assessment targets. Do not equate them automatically with content-validity comprehensibility. Record response-level preference ordering and attribute decision relevance as development criteria, not generic validity.

### Scoring, mapping, comparison, and economic use

For each score path, record:

`instrument and version -> response or profile -> scoring, mapping, crosswalk, or aggregation -> value set or algorithm -> output`

For mapping, record source variables and instrument, direct utility mapping or response mapping, target version, algorithm, development population, validation, application population, and output. For an economic evaluation, add alternatives, population, model, perspective, horizon, utility source for each state, QALY route, cost route, ICER or decision output, and uncertainty handling. Do not reproduce the full model.

### Population health, norms, equity, cost, and burden

For population norms, record the reference period, source samples, instrument and language form, outcomes, scoring route, strata, intended comparison population, and update relation. Rescoring old profiles is reuse and harmonization, not new response collection.

For equity work, record the construct, exact operational measure, individual, household, or area level, categories or cut points, analytic role, reference or rank group, adjustment set, conditioning rule, metric, and result direction. Keep observed gradients, inequality indices, decompositions, and residual within-profile associations separate. Do not infer causation.

For cost or burden work, record condition and case definition, prevalence or incidence basis, population, perspective, reference year, cost categories and bearer, resource and unit-cost route, productivity method, price year and currency, health-loss outcome, monetization, assumptions, exclusions, and sensitivity analysis. Keep costs, utilities, QALYs, DALYs, and years lived with disability separate.

### Evidence syntheses

Keep review methods in a paper-local review component. Record databases and other sources, final search date, main eligibility logic, screening and extraction roles, evidence-unit type and count, duplicate or shared-data handling, synthesis type, and appraisal or stated reason for its absence. Keep publications, studies, trials, data sets, and participants distinct. Detailed search strings and per-database yields stay in the source or concise narrative unless they decide a reported conflict or a user query.

### Implementation, practice, infrastructure, and survey quality

For implementation, record the object, site, stage, actor perspective, eligible and participating counts, workflow position, collection schedule, uptake, repeat completion, acceptability, respondent and staff burden, barriers, facilitators, tested changes, and planned scale. For a clinical workflow, preserve the path from trigger through self or proxy form, medium, displayed result, recipient, review duty, flag rule, discussion or action route, training, and system integration.

For practice surveys and infrastructure, record survey target, frame, sections or battery, mode bundle, quota or representativeness method, language adaptation, order, quality checks, open- and closed-response analysis, operating periods, geographic scope, and resource access.

For each survey-quality rule, record `indicator -> threshold -> timing -> unit -> action -> affected count and denominator`. Keep prevention, live monitoring, flagging, exclusion, interviewer action, and redesign separate. State whether the rule came from a protocol, pilot, external precedent, or author judgment.

### Conceptual and methodological guidance

Record the named concept or framework, its scope, inputs, distinctions, intended use, limitations, and any proposed handling or research priorities. Use structured uncertainty only when uncertainty is a study object, a quantified result, or a dependency in a method chain. Ordinary limitations remain attributed narrative.

## Outcomes, comparisons, and evidence lineage

Distinguish item or dimension response, health profile, unweighted level sum score, EQ VAS, directly scored utility, mapped response, mapped utility, change score, category, QALY, DALY, years lived with disability, cost, inequality index, modeled estimate, and decision result. Link each derived outcome to its source response, transformation, value set or algorithm, model, and applicable population and time.

For a comparison, record the objects, purpose, exact contrast axes, component, paired or independent evidence, conditioning rule, method, outcome or property, principal result, and transfer limit. Useful axes include instrument, version, configuration, response wording, language, population, condition, country, time, administration bundle, task, preference source, scoring or value set, mapping route, model, and implementation condition.

Record reuse only when the paper identifies or describes a reused sample, data set, protocol, design, value set, mapping function, model, product, trial corpus, or infrastructure. State whether the paper reanalyzes, extends, updates, harmonizes, scores with, or compares the object. A method citation alone is not reuse.

For evidence relation status, record the object and one supported value: `documented same evidence`, `documented partial overlap`, `documented independent`, `possible overlap`, or `not reported or unclear`. Add the source basis and relevant differences in period, recruitment, mode, order, or definitions. Do not assign a subjective numeric confidence and do not store one paper-level independence flag.

For harmonization or calibration, name the source variables, response labels, value set, time period, and transformation. State the common output and the information that the operation preserves or removes.

## Products and independent states

Create a product record only for an output that a researcher can identify or seek. Product kinds include value set, instrument or version, language version, mapping or scoring function, conceptual framework, protocol, data set or infrastructure, population norms, implementation workflow or resource package, and reporting or method guidance.

Record product identity, author wording, kind, output role, version or date, instrument, country, language, population basis, producing component, intended use, and provenance. Keep these state dimensions independent:

- **Development fact:** proposed concept, draft, prototype, completed named output, ongoing resource, or superseded.
- **Supporting evidence:** state the exact evidence, such as technical pilot, cognitive interview, content-validity work, psychometric test, valuation, external validation, or mock workflow test.
- **Governance:** experimental, reviewed, endorsed, or approved, with the named body when supplied.
- **Availability and access:** available, restricted, licensed, unavailable, planned, or not reported.
- **Author recommendation:** what the authors recommend and for which scope.
- **Documented use:** actual research, pilot, limited routine, or scaled routine use in the reported setting and period.
- **Documented effect:** the observed effect and its evidence.
- **Implementation state:** proposal, pre-implementation prototype, pilot, local routine use, multi-site scale-up, or established system use, when this axis applies.

Do not use `tested`, `validated`, `established`, or `final` alone. State the exact evidence and scope. A completed language version can lack psychometric evidence. A restricted infrastructure can operate. A comparison-only value set can be an analysis derivative without being a released scoring product. A mock-tested workflow is not routine use.

## Findings, meaning, limits, and gaps

Keep these statement types separate and attribute them:

- **Principal finding:** the main empirical or methodological result, linked to its component, comparison, method, property, or product.
- **Author interpretation:** the authors' explanation or synthesis.
- **Author-reported limitation:** an important limit that the authors state.
- **Author-reported implication:** a scientific, practical, policy, implementation, or development consequence that the authors propose.
- **Documented use:** actual use reported in the paper.
- **Documented effect:** an observed effect reported in the paper.
- **Author-reported future work or gap:** a need or plan that the authors state.
- **Extractor observation:** a narrow, labeled scope or application note.
- **Corpus-derived gap:** a later result from defined corpus filters, with corpus version, date, and boundaries.

For a documented effect, record the evidence provider and outcome level. Keep a staff-reported practice response, an observed workflow change, and a measured participant or service outcome separate.

Do not turn an implication into impact. Do not turn a proposed scale-up into use. Keep competing author explanations when the design cannot distinguish them.

## Source uncertainty and extraction quality

Keep analytic uncertainty separate from extraction uncertainty. For analytic uncertainty, record the object, author-named type, source stage, generated or inherited status, quantification or exploration, downstream use, and handling. Supported top-level types are variability, observed or latent heterogeneity, statistical uncertainty, and methodological variation. They can overlap.

Use extraction issue records for `source conflict`, `unclear procedure`, `not reported`, and `transfer limit`. For a source conflict, add a subtype when useful: count or arithmetic, scope or geography, definition or denominator, or summary versus main text. Preserve each competing statement, value, denominator, and location. Record the extractor's normalized choice and reason, or state that the issue remains unresolved. Do not silently repair the source or merge the issue into an author conclusion.

Apply these quality checks:

1. Read the abstract, methods, results, tables, and supplied supplements for each material component.
2. Build an evidence-stage ledger and test reported arithmetic and denominators.
3. Compare each repeated key fact across sections. Check counts, versions, languages, dates, ranges, thresholds, group definitions, modes, and product states.
4. Trace each principal finding to the correct component, evidence, method, and outcome.
5. Trace each derived outcome and product state to its stated source.
6. Run a second pass only for conflicts and unclear procedures. Preserve disjoint conflicts even when another candidate record did not detect them.
7. Separate author statements, extractor normalization, and corpus derivation.

## Extraction workflow

1. State the paper aim, contribution, study families, and research execution.
2. Identify material components and their relations. Remove any component that does not prevent a false statement.
3. Record evidence roles, context, flow, instruments, and administration for each component.
4. Record each material method through the common method-use pattern. Apply only the needed family profile.
5. Record outcomes, derivations, comparisons, products, reuse, and evidence relations.
6. Summarize principal findings and keep interpretation, limits, implications, use, effect, and future work separate.
7. Complete the conflict and provenance checks.
8. Test the record against likely combined filters. Mark any unsupported value as not reported, unclear, conflicting, or not applicable as appropriate.

Structure a detail when it recurs across papers and changes retrieval, comparison, or interpretation. Use a relation when the meaning depends on another object. Keep exact names as normalized values under a stable method or product category. Use concise narrative for rationale, unusual procedures, competing explanations, and local frameworks. Do not create mandatory empty fields.
