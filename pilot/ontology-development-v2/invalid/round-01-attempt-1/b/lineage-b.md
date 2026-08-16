# Lineage B paper-first EuroQol ontology

Status: round 1 complete for batch 01, 2026-08-16.

This record contains the current ontology, the extraction guide, and the ten paper applications. It is an ontology for a paper-first research record. It is not a fixed data form. An element is optional or repeatable when the paper requires it.

## Source verification

All assigned files matched the frozen manifest before semantic work started.

| Order | Paper ID | Bytes | SHA-256 check | Byte-count check |
|---:|---|---:|---|---|
| 1 | `10.1007/s40258-021-00639-3` | 77,402 | pass | pass |
| 2 | `10.1007/s11136-020-02688-y` | 121,988 | pass | pass |
| 3 | `10.1007/s11136-025-03983-2` | 73,694 | pass | pass |
| 4 | `10.1017/s0266462326103602` | 101,826 | pass | pass |
| 5 | `10.1007/s11136-019-02115-x` | 69,271 | pass | pass |
| 6 | `10.1007/s40273-022-01216-9` | 55,701 | pass | pass |
| 7 | `10.1007/s11136-025-04003-z` | 58,977 | pass | pass |
| 8 | `10.1007/s11136-025-04038-2` | 76,716 | pass | pass |
| 9 | `10.1016/j.jval.2025.02.001` | 50,386 | pass | pass |
| 10 | `10.1007/s10198-025-01770-x` | 173,513 | pass | pass |

## Current ontology and extraction guide

### 1. Record boundary and representation choices

The paper is the main record. Use a paper-local study component only when a difference in phase, evidence group, task, administration, timing, or analysis changes retrieval or interpretation. Keep all components subordinate to the paper.

Use four representation forms.

| Form | Use |
|---|---|
| Controlled tag | Use for stable distinctions that support filtering, such as study family, instrument role, psychometric property, valuation task, administration channel, and product type or stage. Keep lists open when the current papers do not support a closed vocabulary. |
| Structured value | Use for an exact name, version, language, country, condition, count with stage, time point, recall period, sample rule, model name, or protocol version. |
| Relation | Use when the connection carries the meaning. Examples are a component that uses a sample, an instrument that has a role in a component, an analysis that tests a property, and a paper that reuses a data set. |
| Concise narrative | Use for purpose, contribution, principal findings, interpretation, limitations, implications, future work, uncertain source statements, and detail that does not support stable retrieval. |

Do not force a paper to use all ontology concepts. Do not copy all reported detail. Preserve the exact paper term with a normalized tag when normalization is useful.

### 2. Paper-level research description

For each paper, capture:

- a concise aim and the research questions that the authors address;
- one or more study-family tags;
- the main concepts, constructs, theories, frameworks, and practical topics;
- author-stated contributions;
- the component structure, if it is material;
- the products and evidence that the paper creates.

The current controlled study-family tags are:

- `valuation and value-set development`;
- `instrument development or adaptation`;
- `measurement-property or psychometric study`;
- `qualitative concept or content-validity study`;
- `population-health or population-norm infrastructure`;
- `practice, policy, or methods survey`;
- `systematic evidence or methods review`.

A paper can have more than one tag. Mapping, translation, implementation, and population-norm studies remain required by the user questions. This batch does not yet give enough evidence to define their full method modules.

Purpose tags can include `develop`, `estimate`, `test`, `compare`, `describe practice`, `synthesize`, and `build research infrastructure`. Record the aim in narrative as well. A tag does not replace the exact purpose.

### 3. Study component

A study component is a paper-local unit with a distinct purpose or method path. Give it a clear local name, such as `phase 1 label development`, `DCE sample`, `7-day retest`, or `review meta-analysis`.

For each material component, capture these relations as applicable:

- purpose and sequence or dependency;
- evidence-source group;
- instrument and its role;
- task, protocol, and administration;
- analysis and the reason for that analysis;
- comparison;
- product or finding;
- data reuse or extension.

Do not create a component only because a paper has a section heading. Create it when the split answers user question 5 or prevents a false combination of methods, samples, or findings.

### 4. Evidence, population, and context

Keep these three roles separate:

1. **Evidence supplier:** the person, document, trial, or other source that supplies the evidence.
2. **Referent:** the person, group, health state, or practice that an answer describes.
3. **Intended population or decision context:** the population or decision for which the result or product is intended.

This distinction is required. An adult can value a hypothetical child's health. An HTA practitioner can report individual views about agency practice. A caregiver can report their own health and not the care recipient's health.

For participant or evidence-source groups, use structured values for:

- source type and role;
- country, region, language, age group, condition, care setting, and policy setting;
- study period, data-collection period, and material follow-up interval;
- sampling frame and method;
- recruitment, inclusion, and exclusion rules;
- counts with explicit stages, such as invited, screened, completed, included, analyzed, or stable at retest;
- important weighting, quotas, and representativeness claims;
- report role: self-report, proxy report, professional report, hypothetical-person valuation, or document evidence.

Do not store a count without its stage and component. Keep author claims of representativeness separate from the sampling method.

### 5. Instrument identity and role

Identify each instrument with the most exact information that the paper supplies:

- family;
- version or level system;
- variant, long or short form, youth or adult form, and official or experimental status;
- language version;
- component, such as descriptive system, index utility, EQ VAS, dimension, item, or response scale, when that level changes interpretation.

An instrument can have one or more roles in a component:

- target of development or adaptation;
- target of valuation;
- target of measurement-property or content-validity testing;
- respondent health measure;
- health-state descriptive system or preference-task stimulus;
- comparator;
- anchor, external criterion, or known-group classifier;
- outcome or data type under review;
- screening or eligibility instrument;
- scoring or value-set source;
- survey topic, when practitioners report use of an instrument;
- product created by the work.

Do not treat an instrument that is only a survey topic as if participants completed it. Do not treat an instrument mention in the background as study use.

### 6. Method path

Record the method path at the component level. The path connects design, task or data collection, administration, protocol, quality control, and analysis. Use the study-family modules below.

#### Valuation module

Capture:

- exact task, such as cTTO, another TTO form, DCE, DCE with duration, PTO, VAS, or SG;
- valued instrument and health states;
- evidence supplier and valuation referent;
- perspective, duration, worse-than-dead framing, choice format, and anchoring route when reported;
- experimental design, including states or pairs, blocks, task count per person, overlap, randomization, and feedback task when material;
- protocol and technology, such as an EQ-VT version;
- administration and interviewer training or quality control;
- model family and exact model form;
- model purpose, anchoring method, model-selection criteria, and sensitivity analysis.

Keep a valuation task, an experimental design, an administration mode, and a statistical model as separate concepts. Papers 1 and 6 show that their combinations affect the product.

#### Measurement-property module

Use controlled property tags, with the exact paper term when needed:

- feasibility or missing responses;
- distribution, ceiling, and floor;
- test-retest reliability and measurement error;
- content validity, construct validity, convergent validity, and known-group validity;
- responsiveness;
- informativity and discrimination;
- differential item functioning.

For each test, connect the property to the target instrument component, population, comparator or anchor, time points, analytic method, and decision rule. The unit can be item, dimension, profile, index, or EQ VAS. Do not combine these units into one generic validity result.

#### Instrument-development and adaptation module

Capture material development stages, such as:

- concept or label elicitation;
- candidate generation;
- sorting or response scaling;
- item or label selection;
- cognitive interview or debriefing;
- language-specific development;
- translation, review, cultural adaptation, and harmonization;
- psychometric testing and valuation, if done.

Record the evidence population at each stage. Record whether a version is draft, selected, tested for comprehension, validated, valued, licensed, or in routine use. Do not call a comprehensible draft a validated instrument.

#### Qualitative module

Capture interview or group format, topic-guide source and language, sampling logic, interviewer and respondent mode, coding approach, coder process, framework or theory, comparison framework, and saturation claim. Connect a content-validity conclusion to the tested aspect, such as comprehensiveness. Do not generalize one tested aspect to all content-validity aspects.

#### Survey and population-data module

Capture cross-sectional or longitudinal design, sampling frame, quota or probability method, survey channel, language, country modules, instrument order, quality checks, and analysis of closed and open responses. Separate a general-population health survey from a survey of professional practice.

#### Systematic-review module

Capture source databases or registries, search period, report-language limits, eligibility, evidence unit, duplicate or shared-data handling, selection and extraction process, synthesis method, subgroup logic, and quality-appraisal decision. The review corpus is the evidence-source group. The populations in included studies are the referents of the synthesized evidence.

#### Analysis description

For all families, record the exact important analytic method and its purpose. Use a controlled purpose tag such as `estimate value set`, `test association`, `test group difference`, `test reliability`, `test measurement information`, `synthesize studies`, or `describe practice`. Record the inference type as descriptive, association, prediction, comparison, measurement, causal treatment effect, or qualitative interpretation when it matters.

### 7. Administration

Describe administration with separate values for:

- respondent or report role;
- interaction mode, such as interviewer-administered or self-completed;
- channel, such as face-to-face, telephone, web, app, or paper;
- technology, such as computer-assisted personal interview;
- setting;
- recall period;
- instrument or task order and randomization.

For example, `face-to-face`, `computer-assisted`, and `interviewer-administered` are three compatible facts. They are not synonyms.

### 8. Comparison and condition

Represent a material comparison as a relation between named objects. Add the condition that makes the comparison interpretable. Comparison objects can be instruments, versions, language labels, response scales, models, value sets, populations, regions, time points, or evidence formats.

Use structured conditions for differences in:

- population or evidence source;
- language or cultural setting;
- timing and recall period;
- administration or report role;
- task or valuation perspective;
- scoring route or value set;
- analytic unit or property;
- country or policy context.

Keep the comparison result concise. Paper 10 shows that a difference in recall period can explain an apparent instrument difference. Paper 6 shows that DCE and cTTO can change dimension ranks.

### 9. Product and maturity

Link a product to the paper and to the component that creates it. Current product types include:

- value set;
- instrument version or language version;
- conceptual framework;
- survey instrument, data infrastructure, or reference data set;
- evidence synthesis;
- methods or research-priority evidence.

Capture the author-reported stage and the evidence for it. Useful stage tags are `draft`, `selected`, `comprehension-tested`, `measurement-tested`, `valued`, `established`, `published`, `operational`, and `planned extension`. More than one stage can apply. Add a concise future-step narrative.

Do not infer adoption, policy effect, or scientific impact from publication or author expectation.

### 10. Findings, interpretation, and impact boundary

Keep these statement types separate and label their source:

| Statement type | Extraction rule |
|---|---|
| Principal finding | Capture the result that answers the main aim. Include only key estimates or counts that are needed for interpretation. |
| Author interpretation | Capture how the authors explain or qualify the findings. Mark it as author-reported. |
| Author-stated contribution | Capture what the authors say the work adds. |
| Reported implication or recommendation | Capture the proposed scientific, clinical, policy, implementation, or instrument-development consequence. Do not treat it as actual use. |
| Documented use or effect | Capture only use or effect that the paper documents. State the actor and context. |
| Reported limitation | Keep the limitation with the affected component or conclusion. |
| Author-stated gap or future work | Keep this separate from a later corpus-level gap. |
| Extractor uncertainty or transfer limit | Use for source conflicts, unclear versions, unclear provenance, or a limit that is needed to prevent a false comparison. |

Do not create an estimate-level claim graph. Do not extract every coefficient, confidence interval, or table cell.

### 11. Reuse and provenance

Record explicit reuse of a sample, data set, protocol, value set, mapping function, or model. Use relations such as `reuses`, `extends`, `applies`, `compares with`, or `deduplicates shared evidence`. Identify the reused object as exactly as the paper permits.

Following a standard protocol is not sample reuse. Comparing with a prior value set is not the same as applying it for scoring. If a review finds several papers from one data set, record the shared-data handling because it changes the evidence count.

### 12. Corpus-derived questions

The paper record supplies structured inputs for later corpus queries. Publication date comes from the deterministic source layer. Semantic time, such as data-collection period, instrument generation, protocol version, and product stage, comes from this extraction. A later layer can use these values to describe change over time.

Do not state a corpus gap from one paper. A later corpus process can test combinations of instrument, version, language, population, country, condition, method, setting, and purpose. It can then label absent or weak coverage and retain the papers that support the conclusion.

## Applications to batch 01

### Paper 1 — `10.1007/s40258-021-00639-3`

**Family and purpose.** Valuation and value-set development. The paper develops the first Danish EQ-5D-5L value set from Danish adult general-population preferences. It also selects a model for the combined cTTO and DCE evidence. Main topics are health-state utility, QALYs, national priority setting, cTTO, DCE, anchoring, hybrid modeling, representativeness, and valuation quality control.

**Components and evidence.**

- Recruitment and interview component: adults older than 18 years in Denmark. Data collection ran from October 2018 through November 2019. Statistics Denmark supplied a random representative sample frame for age, sex, education, and region. A market-research panel later supplemented recruitment under the same targets. There were 1,052 completed interviews and 1,014 analyzed interviews after exclusions. Respondents supplied preferences. The referents were hypothetical EQ-5D-5L health states. The intended context was Danish healthcare priority setting and QALY estimation.
- cTTO component: each respondent valued 10 EQ-5D-5L states. The full blocked design contained 86 states. It included mild, moderate, and state 55555. It used conventional TTO for states better than dead and lead-time TTO for states worse than dead. Respondents used a feedback module to flag unwanted rankings.
- DCE component: each respondent valued seven pairs without duration. The full design contained 196 pairs in 28 blocks. The order and left-right position were randomized.
- Modeling component: the paper tested cTTO-only GLS random-intercept and random-effects Tobit models, a DCE conditional logit model, and hybrid models. The selected model was a heteroscedastic censored Tobit hybrid that combined cTTO and DCE. Logical consistency was the main selection criterion. A sensitivity analysis restored cTTO observations that respondents had removed in feedback.
- Comparison component: the new value set was compared with the Danish EQ-5D-3L value set and the Danish 5L crosswalk value set.

**Instruments, protocol, and administration.** EQ-5D-5L was a respondent health measure, a health-state descriptive system, the target of valuation, and the product basis. EQ VAS measured respondent health. EQ-5D-3L and the 5L crosswalk were value-set comparators. Interviews were face-to-face, interviewer-administered, and computer-assisted. They used EQ-VT 2.1. Interviewers received 2.5 days of training. The EQ-VT quality-control tool supported repeated protocol and data checks.

**Product and maturity.** An established and published Danish EQ-5D-5L value set. The selected model predicts all 3,125 states. The paper presents it as ready for Danish decision use.

**Principal findings and interpretation.** The analyzed sample was close to the Danish adult population, with some excess higher education and under-representation of ages 18 to 24 and the lowest education group. Only the heteroscedastic censored hybrid model was logically consistent. Predicted values ranged from -0.757 to 1. Anxiety/depression had the largest decrement. The authors interpret the data quality as a result of the detailed protocol, training, monitoring, and recruitment support. They recommend the new value set for Danish QALY estimation.

**Limits, implications, and gaps.** The authors report a recruitment-source change, recruitment difficulty, and small representation differences. They state that DCE anchoring and the utility-theory basis of hybrid models remain unresolved. They also warn that country differences and translation can limit value-set transfer. The expected role in Danish decisions is an author-reported implication. The paper does not document a later policy effect.

**Reuse.** The paper applies EQ-VT 2.1 and compares prior Danish value sets. It does not report sample reuse.

### Paper 2 — `10.1007/s11136-020-02688-y`

**Family and purpose.** Systematic psychometric evidence review. The paper synthesizes evidence for the measurement properties of the official EQ-5D-5L and identifies gaps. Main constructs are feasibility, distribution, test-retest reliability, validity, responsiveness, ceiling and floor effects, and value-set effects on index scores.

**Review evidence and methods.** MEDLINE, PsycINFO, EMBASE, and the EuroQol website were searched for publications from 2011 through January 2019. Reports had to be in English or German. The review excluded experimental 5L versions and work that did not assess measurement properties. Two reviewers screened independently, with consensus and senior review. Of 889 identified publications, 99 were included. They represented 32 countries and included general-population and patient studies. The review recognized repeated use of the same underlying data set and extracted the shared data only once when applicable.

**Instrument roles and property units.** EQ-5D-5L was the target instrument. The review focused on its descriptive system because the EQ VAS version was not always clear in source papers. It separated missingness, profile and dimension distributions, index and item test-retest reliability, content and construct validity, convergent validity, known-group validity, and responsiveness. It also distinguished index, dimension, and full-profile results. Comparators included EQ-5D-3L, other multi-attribute utility instruments, global-health measures, physical and functional measures, pain measures, clinical measures, satisfaction, and cognition or communication measures.

**Synthesis.** The paper used narrative synthesis across all properties. It used random-effects meta-analysis for the proportion at full health, index means, and correlations. It used subgroup analysis only when at least three studies supported a subgroup. It estimated missing means and standard deviations when source data permitted this. It did not review valuation methods as a main topic.

**Product and maturity.** A published evidence synthesis of EQ-5D-5L measurement properties. It is not a new instrument or value set.

**Principal findings and interpretation.** All 17 studies that reported missing values found acceptable levels. Most of 48 studies found no important floor effect. Nine studies supported index test-retest reliability, but several showed less stable dimensions. Convergent evidence was strongest for other utility instruments, physical or functional health, and pain. Evidence was weak for life satisfaction and cognition or communication. Fifteen studies assessed responsiveness. The authors judge overall validity and reliability to be strong, but they identify responsiveness as less settled. They interpret general-population ceilings as partly consistent with an instrument that measures health problems rather than positive health.

**Limits, implications, and gaps.** The review excluded experimental versions and many application studies. It did not assess valuation methods, although a value-set choice can change index results and responsiveness. The evidence was concentrated in western Europe, OECD countries, and parts of East Asia. The authors call for stronger responsiveness work, suitable anchors and minimally important differences, and evidence from more regions and uses. These are author-stated gaps, not corpus-level gaps.

**Reuse.** The review explicitly handles publications that use the same underlying data. This is a `deduplicates shared evidence` relation.

### Paper 3 — `10.1007/s11136-025-03983-2`

**Family and purpose.** Population-health and instrument-evaluation infrastructure. The paper describes the rationale, design, and data-collection methods of EQ-DAPHNIE. Its aims are comparable national population-health data, evaluation of health and wellbeing instruments, and research infrastructure for later analyses.

**Components, countries, and counts.**

- Pilot: United Kingdom, 2023, 3,012 completed responses.
- Round 1: Australia, Canada, New Zealand, the United Kingdom, and the United States. Data collection occurred in 2024. Each country targeted about 4,500 complete responses. Reported completed samples ranged from 4,505 to 5,040.
- Round 2: Argentina, Brazil, Chile, China, France, Germany, Japan, Mexico, the Netherlands, and Spain. Data collection occurred in 2024. Reported completed samples ranged from 4,502 to 4,537.
- Future rounds: planned expansion to other regions.

Adults aged at least 18 years supplied self-reported evidence about their own health, wellbeing, social conditions, behaviors, and healthcare use. Dynata online panel members were eligible. The intended uses were national population-health assessment, cross-country comparison, and instrument evaluation.

**Sampling and administration.** The study used a cross-sectional web survey in LimeSurvey. It used an online panel and first-come enrollment within quotas. Quotas covered age, sex, income, region, urban or rural residence, and language where applicable. Post-stratification weighting was planned. A soft launch of 250 responses per country supported review before the full launch. Surveys were self-completed online. The standard survey took about 20 minutes and about 50 screens. Participants could skip questions.

**Instruments and roles.** EQ-5D-5L and EQ VAS were respondent health measures. Country-specific bolt-ons included vision, hearing, breathing, sleep, tiredness, social relationships, cognition, skin irritation, and self-confidence. Other respondent measures included EQ-HWB, including long and short forms as applicable, PROMIS-10, ASCOT SCT4, ICECAP-A, WHO-5, OPQOL-brief for respondents aged at least 65 years, PHQ-2, and GAD-2. The instrument set varied by country. The survey also used an `Alex's health` vignette. Respondents completed EQ-5D-5L for a hypothetical person to support study of response-scale heterogeneity. This was a hypothetical-person report, not the respondent's own health report.

**Language and survey process.** Survey languages included English, Spanish, French, Portuguese, Japanese, Simplified Chinese, Dutch, and German. Standard measure translations came from developers when available. Native speakers reviewed translations and country adaptations. EQ-5D-5L preceded the vignette. Other health measures were randomized. Duplicate age and marital-status questions, technical tests, soft launch review, and response checks supported quality control.

**Product and maturity.** The product is an operational multi-country data-collection infrastructure and a set of completed cross-sectional national data sets. The paper does not report the later instrument-comparison or population-norm findings. Expansion, longitudinal follow-up, and serial panels are planned.

**Principal contribution and interpretation.** The authors present EQ-DAPHNIE as a way to generate large, comparable population-health evidence and to test several health and wellbeing instruments. They interpret the standardized core, quotas, pretests, and quality checks as strengths for cross-country comparison.

**Limits, implications, and gaps.** The authors report exclusion of people without adequate internet access, possible online-panel bias, cultural differences in how measures work, and a one-time cross-sectional design. The paper calls for tests of other sampling methods, longitudinal follow-up, and repeated panels. The paper calls its samples representative, but the extraction must retain the nonprobability online-panel frame and quota method with that claim.

**Reuse.** The project applies established instruments and translation resources. This paper does not state that the project reuses a prior participant sample.

### Paper 4 — `10.1017/s0266462326103602`

**Family and purpose.** Practice, policy, and methods survey. The paper describes how HTA practitioners use HRQoL and health-state utility evidence. It also records their views about instruments, valuation methods, evidence sources, data quality, and research priorities.

**Evidence suppliers, referent, and context.** The evidence suppliers were HTA agency personnel and contracted professionals. Their answers described their own practices and views. They did not provide formal agency positions. The intended context was QALY-based cost-effectiveness work and future HRQoL research. The survey was distributed in 49 countries. It received 238 complete responses from 45 countries and 65 agencies across six regions. Of these respondents, 213 had QALY-related work.

**Sampling and administration.** The cross-sectional survey ran from April 2023 through January 2024. The study used purposive recruitment through the international team's professional and EuroQol networks. Recruiters and agency contacts sent country-specific links and reminders. Eligible participants worked on national HTA or advised such organizations. The survey was anonymous, self-completed, and web-based in Qualtrics. Participants needed to understand the English form. They could answer open questions in a language of their choice. Non-English text received forward and backward translation.

**Survey topics and instrument roles.** The listed utility instruments were topics of professional-practice questions, not HRQoL measures that respondents completed. They included AQoL, EQ-5D, EQ-5D-Y, EQ-HWB, EQ-5D bolt-ons, HUI, PROPr, QWB, and SF-6D. Elicitation-method topics included TTO, DCE, VAS, SG, BWS, and PTO. Other topics were general-public or patient preference sources, local or foreign evidence, data-quality problems, and research priorities.

**Analysis.** Closed responses received descriptive analysis. Country summaries used a mode, or a median when needed. Regional results used medians of country summaries. Research priorities used country, regional, and global importance scores. Open responses received structured content analysis after translation.

**Product and maturity.** A published global practice and needs assessment. It produces methods-priority evidence. It does not create or validate a utility instrument.

**Principal findings and interpretation.** The three most frequently used instruments were EQ-5D, SF-6D, and EQ-5D-Y. TTO, VAS, and SG were the most frequently used elicitation methods. Foreign general-public preference evidence was used more often overall than local general-public evidence, although most respondents preferred local evidence. Common problems were poor sample representation, small utility samples, mismatch with decision models, and mixing instruments or methods. Global priorities included recent tariffs, child and adolescent instruments, and instruments that cover health and social care. The authors interpret data scarcity and limited fit as important causes of suboptimal evidence use.

**Limits, implications, and gaps.** Some countries had very few respondents. The network recruitment could over-represent people who know or favor EuroQol instruments. The study could not verify eligibility, link respondents reliably to a specific agency, or treat an agency as the unit of analysis. The authors recommend sustained HTA engagement in instrument development, more pediatric and social-care measurement work, recent local values, and more accessible HSU data. These are reported priorities and implications. The paper does not document that agencies adopted a new method because of the survey.

**Reuse.** The recruitment reused professional networks. It did not reuse a study sample or health data set.

### Paper 5 — `10.1007/s11136-019-02115-x`

**Family and purpose.** Instrument development and multilingual adaptation. The study ran from May 2014 through June 2018. The paper develops an EQ-5D-Y descriptive system with more response levels. It compares draft four-level and five-level forms for comprehension, feasibility, and child preference.

**Components and evidence.**

- Phase 1a, candidate labels: reviews of child HRQoL instruments, dictionaries, thesauruses, and two focus groups per country generated child-friendly severity labels. Participants were ages 8 to 15 in Germany, Spain, Sweden, and the United Kingdom. The home language had to be the local study language.
- Phase 1b, sorting and response scaling: school samples rated label severity. Ages 8 to 10 used a five-face sorting scale. Ages 11 to 15 used a VAS response-scaling task. The article reports 255 interviews, but the country counts in its table sum to 254. Candidate selection used location on the severity continuum, agreement, dispersion, and participant comments.
- Phase 2, cognitive testing: 120 participants took part: Germany 33, Spain 35, Sweden 32, and United Kingdom 20. Germany, Spain, and Sweden included healthy participants and children in treatment. The United Kingdom included school participants only and tested only the 5L draft. Other countries compared 4L and 5L drafts. Paraphrasing and probing tested comprehension and response reasons.
- Harmonization: national teams compared the German, Spanish, Swedish, and United Kingdom English forms. They retained language differences when participant evidence supported them.

**Instrument identities and roles.** EQ-5D-Y-3L was the source instrument and comparator. Draft EQ-5D-Y-4L and EQ-5D-Y-5L systems were target forms. The final products were self-report EQ-5D-Y-5L forms in German, Spanish, Swedish, and United Kingdom English. Language forms were developed from local evidence, rather than as literal copies of one label set. The paper proposes United Kingdom English as a source for later translations.

**Administration and analysis.** Focus groups and individual interviews were face-to-face. Sorting and response-scaling order was randomized. Phase 1 used descriptive statistics and thematic content analysis. Phase 2 used recorded cognitive interviews and thematic content analysis. The order of 4L and 5L completion varied to reduce order effects.

**Product and maturity.** A selected and comprehension-tested self-report EQ-5D-Y-5L descriptive system in four languages. It had not yet completed broad measurement-property testing or valuation. No proxy form was produced.

**Principal findings and interpretation.** The development process generated 233 candidate labels. The 5L form was preferred by 68% to 88% of participants in countries that made the direct comparison. Children found it more precise and liked the middle option. The final forms were understandable and feasible in the study samples. The authors conclude that the 5L form is a suitable result of this development stage.

**Limits, implications, and gaps.** All samples were convenience samples. Children with health conditions were difficult to recruit. The United Kingdom and Spain had small protocol differences. The authors call for measurement-property tests, comparisons with EQ-5D-Y-3L, valuation, testing in health conditions, more language versions, and proxy forms. The paper does not claim that these steps were complete.

**Reuse.** The work extends EQ-5D-Y-3L and reviews existing instrument labels. It does not reuse a prior participant data set.

### Paper 6 — `10.1007/s40273-022-01216-9`

**Family and purpose.** Valuation and value-set development. The paper estimates a Chinese EQ-5D-Y-3L value set. It also tests whether an expanded cTTO design and hybrid model improve estimation under the international youth valuation protocol.

**Evidence roles and components.** Adults in the Chinese general population supplied preferences. The referent was a hypothetical 10-year-old child's health, with no stated relationship to the adult. The intended use was health-utility estimation for children and adolescents in Chinese HTA and economic evaluation.

- DCE component: an independent sample of 1,058 adults completed DCE interviews. The design had 150 choice sets in 10 blocks of 15. It used two-dimension overlap and did not include duration, a dominant pair, or a test-retest pair.
- cTTO component: an independent sample of 418 adults completed cTTO interviews. The expanded design had 28 health states in three blocks of 10. State 33333 occurred in each block. The component covered eight recruitment regions.
- Sampling component: quota targets covered sex, age, education, and urban or rural registered residence. Recruitment used snowball and purposive methods in 14 provinces or cities across five geographical parts of China.
- Model comparison: one path used a correlated mixed-logit DCE model and OLS mapping to observed cTTO means for anchoring. A second path jointly modeled DCE and cTTO in a heteroscedastic hybrid model. The authors added an `A3` term for the extra decrement in state 33333. Selection used coefficient significance, monotonicity, and prediction error against observed cTTO means.

**Instruments, protocol, and administration.** EQ-5D-Y-3L was the respondent health measure, health-state stimulus, valuation target, and value-set product basis. Interviews were face-to-face, one-to-one, interviewer-administered, and computer-assisted in EQ-VT. cTTO interviewers received two days of training, practice interviews, and repeated quality-control feedback. DCE interviewers received a two-hour online training, without the same quality-control process. The study followed the international EQ-5D-Y-3L valuation protocol but expanded its cTTO design.

**Product and maturity.** An established and published Chinese EQ-5D-Y-3L value set. The selected product uses the hybrid model with the A3 term.

**Principal findings and interpretation.** Data collection ran from January 2020 through October 2021. Of 1,476 respondents, 1,058 supplied DCE evidence and 418 supplied cTTO evidence. The observed cTTO means ranged from 0.924 for state 11112 to -0.088 for state 33333. The A3 hybrid had the lowest reported mean absolute error, no inconsistent or nonsignificant coefficients, and reproduced a negative value for 33333. The authors interpret the expanded cTTO design as useful for the large gap between 33333 and the next-worst state. They recommend the model as the Chinese youth value set.

**Limits, implications, and gaps.** cTTO data covered only eight regions, while DCE covered more regions. The imagined child's relationship to the respondent was not standardized. cTTO for states worse than dead can place impaired health at ages 20 to 30 for a child who starts at age 10. The authors propose tests of lag-time TTO, richer DCE designs, reasons for the 33333 gap, the effect of child age and respondent perspective, and an updated protocol. The authors state that the value set can support Chinese pediatric economic evaluation. The paper does not document a later reimbursement effect.

**Source uncertainty.** The abstract states 14 regions. A key-points box states four regions. The method identifies 14 provinces or cities across five geographical parts, and it states that cTTO occurred in eight regions. Preserve these statements at their exact level. Do not normalize them to one region count.

**Reuse.** The study applies and extends the international youth valuation protocol. It does not report participant reuse.

### Paper 7 — `10.1007/s11136-025-04003-z`

**Family and purpose.** Secondary measurement-property study. It compares frequency and severity response scales for pain and discomfort. It asks whether the scales supply distinct measurement information and whether results differ by health condition.

**Evidence and reuse.** The paper reuses a cross-sectional dyadic survey data set collected from August 2022 through February 2023. The sample contained 504 unpaid caregivers and their 504 care recipients, for 1,008 adults. Caregiver-care recipient dyads completed linked surveys in one session without discussing answers. The analysis treats respondents as individuals and studies their own responses. Conditions were self-reported. The country is not stated in the supplied article text.

**Instrument identities and roles.** The experimental EQ-HWB 25-item profile, with the nine-item EQ-HWB-S embedded, was the main target. The analysis focused on four items: pain frequency, pain severity, discomfort frequency, and discomfort severity. EQ-5D-5L pain/discomfort was a comparator. EQ-HWB used a seven-day recall period. EQ-5D-5L used `today`. Other survey measures included CarerQoL, CARE-2B, and caregiver-burden measures, but they were not targets of this analysis.

**Administration and methods.** Participants self-completed a Qualtrics web survey. Instrument order was randomized. Attention checks and minimum completion time supported quality control. Analyses included Spearman correlation, Shannon information and evenness indices, graded-response item response theory, ordinal-regression and IRT differential item functioning, and ordinal logistic regression of conditions and item responses. Each method had a measurement purpose. Correlation tested overlap. Shannon indices tested response-category information. IRT tested discrimination and trait coverage. DIF tested response-scale functioning. Regression described condition associations.

**Product and maturity.** Psychometric design evidence for response-scale selection. The paper does not create a new EQ-HWB version. It states that EQ-HWB was experimental during data collection.

**Principal findings and interpretation.** Pain frequency and severity correlated strongly. All pain and discomfort items also correlated strongly, but the scales were not interchangeable. Frequency scales used response categories more evenly and were more informative across the trait range. Severity scales discriminated more at high trait levels. Pain showed material DIF between frequency and severity. Discomfort did not. The authors interpret both scales as complementary for a long instrument. They prefer frequency when a short instrument needs broad information coverage.

**Limits, implications, and gaps.** Cross-sectional evidence cannot support causal interpretation. Conditions were self-reported. Generalization to other cultures and languages requires testing. Recall period and clinical severity can change which response scale is useful. The authors call for tests across populations, conditions, measurement contexts, and recall periods.

**Reuse.** This is explicit secondary analysis of a previously reported dyadic study data set.

### Paper 8 — `10.1007/s11136-025-04038-2`

**Family and purpose.** Qualitative concept and content-validity study. It develops a Chinese lay conceptual framework for quality of life and compares it with the EQ-HWB conceptual framework. The tested content-validity aspect is comprehensiveness. Relevance and comprehensibility were outside this paper.

**Evidence suppliers and context.** Thirty Chinese adults took part: 10 healthy people, 10 patients, and 10 informal caregivers. Twenty-two were from Guangzhou and eight were from Harbin. Quotas covered age, sex, education, health group, and urban or rural household registration. Respondents described their own understanding of quality of life. The intended context was use of EQ-HWB in China.

**Collection and language.** Data collection ran from March through June 2023. Interviews were individual, semi-structured, face-to-face, and usually longer than one hour. The topic guide was developed in English, translated to Chinese, reviewed, and tested in two pilot rounds with six people. Formal interviews occurred in Chinese. Transcripts and analyses used Simplified Chinese. Respondents discussed quality of life, gave a 1-to-10 rating, explained poor quality of life, and confirmed the interviewer's summary.

**Analysis and framework comparison.** Two coders used thematic framework analysis with deductive and inductive coding. The 96 EQ-HWB candidate items supplied a starting codebook. Coders met after each transcript and used supervisor consensus for disagreements. The analysis generated 221 codes and retained 187 after stated outcome-focused exclusion criteria. It grouped them into 57 subthemes and eight themes. The new framework was then compared with the EQ-HWB framework at theme and subtheme levels. Reported saturation was based on repeated views in later interviews and was a subjective judgment.

**Instrument and theory roles.** EQ-HWB was the target of conceptual comparison and content-validity inference. The paper does not establish that EQ-HWB was administered as the source of the qualitative evidence. Wilson and Cleary's quality-of-life framework, COSMIN content-validity guidance, and Chinese cultural concepts informed the study and interpretation.

**Product and maturity.** A published Chinese lay quality-of-life conceptual framework and evidence about the comprehensiveness of EQ-HWB. This is not a new scored instrument.

**Principal findings and interpretation.** Seven of eight themes aligned with EQ-HWB. The Chinese framework also contained `mindset`. It had broader meanings for some subthemes and different placement for sleep and boredom. The authors judge the EQ-HWB framework to be well represented and interpret the omissions as unlikely to remove content validity. They also state that language and cultural adaptation need care because some Chinese terms have no direct English equivalent.

**Limits, implications, and gaps.** The regional samples differed. Harbin participants were younger, healthier, and more educated. Patients were community participants, mainly with chronic illness. Some concepts were difficult to translate. Saturation had no prespecified rule. The authors suggest work with severe or hospitalized patients and later tests of relevance and comprehensibility.

**Reuse.** The study closely follows a prior Italian study protocol for international comparison. It does not reuse the Italian participant data.

### Paper 9 — `10.1016/j.jval.2025.02.001`

**Family and purpose.** Systematic methods review. It describes how randomized clinical trials analyze postbaseline EQ-5D treatment effects. Main distinctions are EQ-5D output type, numerical or categorical format, one or several follow-ups, statistical model, baseline adjustment, assumptions, and missing-data method.

**Review corpus and selection.** MEDLINE and EMBASE were searched from inception through November 15, 2021. ClinicalTrials.gov was searched in August 2023. Eligible evidence was an RCT that compared postbaseline EQ-5D results by treatment group. Publications and HTA reports in English were eligible. Registry results were used when no publication was found. The review found 11,633 records and included 2,125 unique RCTs. It mapped several publications to one trial by registration number, condition, treatment, and sample size.

**Instrument identities and data roles.** The target was EQ-5D trial data. The review separated dimension responses, utility, and EQ VAS. It also separated numerical and categorical use. The source trials could involve EQ-5D-3L or EQ-5D-5L, but exact version, instrument language, and value set were not consistent review strata in the reported synthesis. QALYs and other time-integrated outcomes were excluded.

**Review components and analysis.** Eight reviewers screened titles and abstracts in duplicate. Paired reviewers screened full text. Four reviewer pairs extracted with a pilot-tested form. Methods were normalized into descriptive, bivariate, and multivariable families. Linear and logistic models were split into fixed and mixed effects. Results were separated by one or several postbaseline points. The review did not appraise RCT risk of bias because it described method use and did not estimate a treatment effect.

**Product and maturity.** A published methods synthesis. The authors present it as a basis for future analysis guidance. It is not itself a guideline.

**Principal findings and interpretation.** Utility was analyzed in 1,592 trials, EQ VAS in 1,197, and dimension responses in 385. Most trials treated EQ-5D as secondary or exploratory. Linear fixed-effect models were most frequent for one postbaseline utility measure. Linear mixed-effect models were most frequent for repeated postbaseline utility measures. Only 10.8% of trials with numerical EQ-5D reported checks of model assumptions. Only 21.3% adjusted for baseline EQ-5D. Missing data were explicitly assessed in 661 trials. Of those, 347 used imputation, most often multiple imputation or last observation carried forward. The authors interpret the variation and omissions as evidence that practice lacks consistent, well-reported guidance.

**Limits, implications, and gaps.** Sparse reporting of secondary outcomes can cause undercounting of covariates, assumptions, and missing-data methods. The wide time span can hide change over time. The review did not establish that one model is best. The authors call for model comparisons, estimand-led selection, baseline adjustment, suitable missing-data sensitivity analysis, and reporting guidance.

**Reuse.** The review uses trial publications, HTA reports, and registry results. It deduplicates multiple reports of the same RCT.

### Paper 10 — `10.1007/s10198-025-01770-x`

**Family and purpose.** Measurement-property and psychometric comparison. The paper compares EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D in Brazilian children and adolescents with and without self-reported musculoskeletal pain.

**Evidence and components.** The sample contained 356 students ages 8 to 18 from public and private schools in urban Sao Paulo state. There were 181 with qualifying musculoskeletal pain and 175 without pain. Pain status came from PIP-Kids. It required pain in the last month plus interference, recreation impact, or school absence. Trauma, surgery, and specified conditions were excluded. A 7-day retest identified 231 clinically stable participants: 96 with pain and 135 without pain.

**Instruments and roles.** Official Brazilian-Portuguese self-complete EQ-5D-Y-3L and EQ-5D-Y-5L were target instruments. Their descriptive systems and EQ VAS were separate property units. CHU9D was a target and comparator. PedsQL 4.0 was a construct-validity comparator. PIP-Kids classified known groups and stability. A 0-to-10 pain rating measured pain intensity. The paper used descriptive-system results, not youth utility scores, for the main measurement comparisons.

**Administration and timing.** Students self-completed paper-and-pencil forms in classrooms. Teachers and researchers could explain interpretation. EQ-5D-Y form order was randomized, but the two forms were consecutive. EQ-5D-Y and CHU9D used a `today` recall. PIP-Kids, the pain rating, and PedsQL used longer recall periods. This timing difference affects comparison.

**Properties and methods.** Feasibility used missing responses and completion. Distribution analysis used item responses and profile ceiling or floor. Test-retest reliability used Kappa for dimensions and ICC for EQ VAS, with measurement-error values. Construct validity used prespecified hypotheses and correlations with PedsQL and CHU9D. Known-group validity compared pain and no-pain groups and pain-severity groups. The paper followed COSMIN guidance and kept results separate for the two pain groups.

**Product and maturity.** Brazilian measurement-property evidence for three child HRQoL instruments. The study does not create a new version or value set.

**Principal findings and interpretation.** All three instruments had high completion but important ceiling effects. Descriptive-system test-retest reliability ranged from poor to moderate. EQ VAS reliability was stronger in the pain group than in the no-pain group. Prespecified construct-validity hypotheses were supported more often in participants with pain. EQ-5D-Y-5L met the hypothesis threshold against CHU9D in both groups. All three instruments distinguished participants with and without musculoskeletal pain. The authors state that these instruments can support research and clinical assessment, especially in children with pain.

**Limits, implications, and gaps.** Pain was self-reported and not diagnosed. The pain group was heterogeneous. Recall periods differed. The two EQ-5D-Y forms were consecutive. Feasibility did not include time or comprehension. There was no gold standard for criterion validity. The authors call for tests in other conditions and settings, younger children, proxy forms, utility scores, and responsiveness. The stated policy role of the existing Brazilian EQ-5D-Y-3L value set is an implication, not a documented reimbursement effect.

**Reuse.** The study applies published Brazilian-Portuguese forms and an existing Brazilian EQ-5D-Y-3L value set as context. It does not report reuse of a participant sample.

## Granularity decisions and evidence

| Decision | Paper evidence | User-question consequence |
|---|---|---|
| Keep evidence supplier, referent, and intended context separate. | Paper 6 uses adults to value a hypothetical 10-year-old. Paper 4 asks practitioners about practice. Paper 7 has caregivers and care recipients who report as individuals. | Supports questions 6, 7, 17, and 20. Without the split, a search can falsely return children as respondents or agencies as formal speakers. |
| Use paper-local components when method paths differ. | Paper 5 has label generation, response scaling, cognitive testing, and harmonization. Paper 6 has independent DCE and cTTO samples. Paper 10 has baseline, retest, and pain groups. | Supports questions 5, 8, 9, 12, and 13. It prevents one sample or method from being assigned to the whole paper. |
| Keep exact instrument identity, language, status, component, and role. | Papers 5 and 10 distinguish youth 3L and 5L language forms. Paper 7 tests an experimental EQ-HWB item set. Paper 4 lists instruments only as survey topics. | Supports questions 3, 4, 11, 20, and 23. It prevents a mention from becoming an administration and prevents an experimental form from becoming an official form. |
| Keep valuation task, protocol, experimental design, administration, and model separate. | Papers 1 and 6 both combine cTTO and DCE but use different referents, designs, anchoring paths, model choices, and quality controls. | Supports questions 9, 10, 11, 12, and 21. A broad `valuation` tag cannot distinguish these studies. |
| Structure psychometric property, unit, comparator, population, and decision rule. | Paper 2 separates index reliability from dimension stability. Paper 7 separates informativity from high-trait discrimination. Paper 10 separates dimension Kappa, EQ VAS ICC, hypotheses, and known groups. | Supports questions 12, 13, 20, 21, and 22. A broad `validity` label would hide material disagreements. |
| Keep administration interaction, channel, technology, report role, order, and recall as separate values. | Paper 1 is interviewer-administered, face-to-face, and computer-assisted. Paper 3 is a web self-survey. Paper 10 is a paper self-survey with classroom help and mismatched recall periods. | Supports questions 11, 13, 20, and 24. It enables searches for mode effects without collapsing compatible facts. |
| Store sample counts with stage and component. | Paper 1 reports completed and analyzed interviews. Paper 2 reports records and included papers. Paper 4 reports countries, people, agencies, and a QALY-work subset. Paper 10 reports baseline groups and stable retest groups. | Supports question 8 and helps users judge selection and attrition. A bare sample size is ambiguous. |
| Represent comparisons as relations with conditions. | Paper 1 compares direct and crosswalk value sets. Paper 5 compares 4L and 5L by language. Paper 7 compares scale formats and recall periods. Paper 8 compares frameworks. Paper 10 compares instruments and pain groups. | Supports questions 13, 20, 21, and 22. It prevents comparison results from losing the population, language, timing, or scoring condition. |
| Give products an evidence-based maturity stage and future steps. | Papers 1 and 6 produce established value sets. Paper 5 produces comprehension-tested forms that still need psychometrics and valuation. Paper 3 has operational data collection with planned expansion. | Supports questions 14, 17, 18, and 23. It prevents a draft or expectation from being reported as adopted practice. |
| Separate principal finding, author interpretation, implication, limitation, documented use, and gap. | Paper 1 expects decision use but does not show later effect. Paper 4 reports priorities but no adoption. Papers 2, 7, and 10 qualify findings by property and population. | Supports questions 15 to 18 and 22. It prevents recommendation from becoming impact and prevents an author gap from becoming a corpus gap. |
| Record reuse as a typed relation. | Paper 7 is secondary analysis. Papers 2 and 9 deduplicate papers that share data or trials. Papers 1 and 6 apply protocols but use new samples. | Supports questions 19 and 25. It distinguishes data dependence from protocol similarity. |
| Treat review evidence as a corpus, not as one participant sample. | Paper 2 reviews 99 publications and paper 9 reviews 2,125 RCTs. Each review also has rules for shared data or multiple reports. | Supports questions 8, 19, 21, 22, and 25. It preserves the correct evidence unit. |
| Keep an extensible exact method value with a normalized purpose. | Papers 1, 6, 7, 9, and 10 use many methods for different purposes. The same model family can support different inference. | Supports questions 9, 12, 20, and 21. Exact names remain searchable without requiring one ontology class for every software procedure. |
| Structure language and cultural adaptation only when it affects the study or product. | Paper 5 develops four language forms. Paper 3 uses country survey translations. Paper 8 analyzes in Chinese and finds translation-sensitive concepts. Paper 10 tests official Brazilian-Portuguese forms. | Supports questions 4, 7, 13, 20, and 24. It avoids assigning a paper language to an instrument language. |

## Rejected distinctions and details

- **A fixed universal field set.** Rejected because the papers use different evidence units and method paths. The ontology gives optional concepts and relations.
- **One broad `method` value.** Rejected because cTTO, DCE, cognitive interviewing, thematic framework analysis, test-retest analysis, and review synthesis answer different queries.
- **One broad `psychometric validation` result.** Rejected because property, instrument unit, comparator, population, and timing change interpretation.
- **One `participant` role.** Rejected because supplier, referent, and intended population differ in papers 4, 6, and 7.
- **One administration-mode string.** Rejected because interview role, channel, technology, report role, order, and recall can vary independently.
- **A component for every section, table, or statistical test.** Rejected. Create a component only for a material purpose, sample, phase, task, administration, or analysis split.
- **A globally closed list of all statistical models.** Rejected at this round. Preserve exact named methods as repeatable values and normalize their purpose. Add stable controlled distinctions only after repeated evidence supports them.
- **A separate ontology entity for every survey variable, instrument item, health state, coefficient, estimate, or confidence interval.** Rejected because it adds detail without improving the fixed retrieval and interpretation questions.
- **An exhaustive instrument-dimension ontology.** Rejected. Structure a dimension or item only when it is an analytic unit, comparison object, task stimulus, or principal finding.
- **A detailed claim-evidence graph.** Rejected by the fixed purpose. Keep concise principal findings and their component or comparison link.
- **Generic `impact` inferred from a value set, framework, or survey.** Rejected. Expected use and recommendation remain implications unless the paper documents use or effect.
- **Bibliographic reconstruction.** Rejected because JATS supplies canonical source metadata.
- **Paper language as instrument language.** Rejected. Record an instrument language only from study evidence.
- **Protocol use as data reuse.** Rejected. Protocol application, sample reuse, model reuse, scoring application, and value-set comparison are distinct relations.
- **All social and clinical variables as controlled population classes.** Rejected. Use structured paper terms for conditions and contexts. Normalize them only when cross-paper retrieval requires it.

## Unresolved cases

1. **Paper 5 interview total.** The abstract and results text report 255 sorting and response-scaling interviews. The country counts 64, 72, 60, and 58 sum to 254. Preserve the conflict until the source or supplement resolves it.
2. **Paper 6 region count.** The abstract reports 14 regions. The key-points box reports four regions. Methods report 14 provinces or cities across five geographical parts, with cTTO in eight regions. These can refer to different levels, but `four regions` does not align with the method description. Do not select one normalized count.
3. **Paper 7 study country.** The supplied article describes the sample, platform, ethics body, and conditions, but it does not state the country in the study-method text. Do not infer a country from institutions or demographic categories.
4. **Paper 3 product stage.** The paper is written as a design and infrastructure description, but it also gives completed 2023 and 2024 country samples. Mark the infrastructure operational and the described rounds collected. Do not infer that all planned norm, comparison, access, or longitudinal products are available.
5. **Paper 4 agency voice.** Respondents report as individuals. The recruitment and anonymous form do not support a formal agency-level position. Country or region summaries must not be labeled agency policy.
6. **Paper 9 instrument detail.** The synthesis does not consistently stratify trial results by EQ-5D version, language, or value set. These details remain unknown for corpus-level comparisons, even when a source trial may report them.
7. **Paper 2 EQ VAS version.** The review explicitly focuses on the descriptive system because source reports did not always identify the EQ VAS version. Do not extend its findings to one exact EQ VAS form without source evidence.
8. **Product use versus expected use.** Papers 1, 6, and 10 describe decision uses. This batch does not document later adoption or effects. Keep these statements as reported implications.

## Run note

- Lineage: B.
- Round: 1.
- Batch: `batch-01.tsv`, ten papers.
- Task version: version 2 frozen 2026-08-16.
- Branch: `experiment/ontology-v2-b`.
- Base commit: `858adec5d930fdbb80af94aaa8388c476ec7f14f`.
- Agent: fresh isolated round-1 Codex agent.
- Input check: all ten hashes and byte counts passed.
- Method: read the fixed purpose, user questions, common task, protocol, manifest, and all ten assigned full texts. Developed the ontology from paper applications. Did not inspect version-1 work, other lineages, later batches, probes, holdouts, legacy graph or extraction files, or Git history.
- Mechanical issues: none. Source-level inconsistencies are listed under unresolved cases.
