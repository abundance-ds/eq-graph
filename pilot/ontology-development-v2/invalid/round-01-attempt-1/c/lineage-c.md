# Lineage C: paper-first EuroQol ontology

Round 1 record. This record covers batch 01 only.

## Current ontology and extraction guide

### Scope and organizing rule

The paper is the main research record. Link deterministic source metadata from the JATS layer. Do not reconstruct authors, journal data, dates, identifiers, affiliations, funding, licences, or references in the semantic record.

Create a paper-local component only when a phase, sample, task, administration route, analysis, or comparison has different semantic details. Keep each component subordinate to its paper. Do not create a component for each table, coefficient, questionnaire item, or result.

Record an assertion with its scope and source status. Use these source-status terms:

- **author reported**: the paper states the interpretation, implication, limitation, or gap;
- **extractor observation**: a scoped statement needed to explain the extraction;
- **source conflict**: two parts of the same paper give incompatible facts;
- **not reported**: the paper does not give the needed detail.

### Main record units

| Unit | What it represents | Minimum useful content and relations |
|---|---|---|
| **Paper** | The main EuroQol research record | Objective, contribution, study-family tags, design tags, concepts, geographic and temporal scope, principal findings, and author-reported interpretation. |
| **Study component** | A paper-local phase, sample, task, analysis, or comparison with distinct semantics | Component type, purpose, order, and relations to its evidence sources, instruments, tasks, methods, products, and findings. |
| **Evidence-source group** | The people, records, studies, or other units that supply evidence | Source type, selection and recruitment, eligibility and exclusion, stage-specific counts, geography, age, condition and setting. Keep the **respondent or evidence supplier**, the **referent described by the response**, and the **target population or decision context** separate. |
| **Instrument use** | One exact use of an instrument or instrument part | Instrument family, version, variant, language version, self or proxy form, recall period when material, role, component, administration, data form, scoring route or value set, and whether it was administered, developed, evaluated, compared, or only discussed. |
| **Task and protocol use** | A task done by a respondent, researcher, or evidence reviewer | Exact task type, protocol and version, framing or perspective, design, number of states or choices, blocking, sequence, randomization, quality controls, and deviations or extensions. |
| **Administration** | How an instrument or task reached a respondent | Use separate axes for interaction, interface, encounter, report relationship, setting, language, and timing. For example, `interviewer-administered` + `computer-assisted` + `in person` is not the same as `self-administered` + `web`. |
| **Method use** | A method applied for a stated purpose | Exact method or model family, input or target, purpose, important model features, repeated or single time point, adjustment or anchoring role, comparison status, selection criteria, and whether it was selected. Software is optional supporting text, not a main concept. |
| **Measurement evaluation** | An assessment of an instrument, scale, item, or score | Target, property, method, comparator or anchor, subgroup, time interval, a priori criterion, and concise result. Keep properties such as test-retest reliability, content validity, construct validity, known-group validity, responsiveness, informativity, and differential item functioning distinct. |
| **Comparison** | An explicit comparison that affects interpretation | Compared objects, outcome or property, and material condition differences. Conditions can include population, language, mode, recall period, time point, task, scoring route, or value set. |
| **Research product** | An output that can be found and reused | Product type, exact target instrument or context, geography and language, derivation, reported maturity, availability or access statement when material, and remaining work. |
| **Finding** | A concise principal empirical or methodological result | Finding type, scope, direction, target, supporting component and, only when useful, one or more anchor values. Do not reproduce each estimate. |
| **Interpretive statement** | Meaning assigned to findings | Keep author interpretation, contribution, implication, limitation, future work, and stated gap as separate statement types. Link each statement to the paper, component, finding, instrument, method, or product that it concerns. |
| **Evidence reuse** | Dependence on prior evidence or artifacts | Relation type such as `secondary analysis of`, `reuses sample`, `extends protocol`, `uses value set`, `uses mapping function`, `compares with`, or `derived from`. Identify the reused object or cited study when the paper gives enough detail. |
| **Extraction uncertainty** | A limit in the semantic record | Missing detail, source conflict, unclear version, unclear denominator, or transfer limit. State the effect on retrieval or interpretation. |

### Controlled terms and structured values

Use controlled terms when they support retrieval across papers. Use an open extension list. Do not force a paper into one exclusive family.

**Study-family terms observed in this batch**

- value-set development;
- instrument development or response-level refinement;
- measurement-property evaluation;
- content-validity or conceptual-framework comparison;
- population-health data-resource or study-protocol description;
- HTA practice and research-needs survey;
- measurement-property evidence synthesis;
- statistical-practice evidence synthesis.

Use design tags separately. Current design terms include primary empirical study, secondary data analysis, systematic review, meta-analysis, cross-sectional survey, qualitative interview study, multi-phase development study, test-retest study, and protocol or resource description.

**Instrument roles**

- target under development;
- target under evaluation;
- administered evidence measure;
- comparator or reference measure;
- health-state object valued;
- preference-elicitation or valuation vehicle;
- scoring instrument;
- source framework or source instrument;
- object of reported practice or opinion;
- mentioned background instrument.

This distinction prevents a paper that asks practitioners about EQ-5D use from appearing to have administered EQ-5D to those practitioners. It also prevents a review that names many measures from appearing as a primary instrument study for each measure.

**Evidence-source terms**

Use person, dyad, publication, trial, registry record, or other source type. For people, record respondent role such as general-public adult, child or adolescent, patient, informal caregiver, care recipient, clinician, researcher, or HTA practitioner. Record health-condition ascertainment as diagnosed, self-reported, instrument-defined, registry-defined, or not reported.

**Administration axes**

- interaction: self-administered, interviewer-administered, assisted, or not reported;
- interface: web, app, computer-assisted, paper and pencil, telephone, or not reported;
- encounter: in person, remote, classroom, clinic, home, or not reported;
- report relationship: self-report, proxy report, paired or dyadic report, or valuation of a hypothetical referent;
- timing: recall period, assessment time point, and test-retest interval;
- sequence: fixed, randomized, conditional, adaptive, or not reported.

**Product terms and maturity**

Current product types include value set, instrument version, language version, conceptual framework, study infrastructure, population dataset, survey or protocol, and evidence synthesis. Record the reported stage as planned, draft, field-tested candidate, developed or estimated, evaluated in the reported study, available, or documented in use. A product can have more than one stage statement. Do not convert one positive study into a universal `validated` status.

Use structured values for counts, dates, durations, age ranges, task counts, health-state counts, block sizes, assessment intervals, thresholds, model inputs, and product value ranges. Always give a count a denominator or stage label. For example, `1,052 interviews conducted`, `1,014 analyzed`, and `712 cTTO state valuations removed after feedback` are different facts.

### Method and comparison granularity

Do not use a single `statistical analysis` label. Record a named method when it changes retrieval or interpretation. Each method use must say what it did. Examples from this batch include:

- random-effects meta-analysis for pooled ceiling, index, or correlation results;
- random-intercept generalized least squares, random-effects Tobit, conditional logit, and heteroscedastic censored hybrid models for value-set estimation;
- mixed logit plus mapping and joint hybrid modeling as alternative anchoring paths;
- Kappa and intraclass correlation for different test-retest targets;
- a graded-response item response theory model for item discrimination and thresholds;
- logistic ordinal regression or item response theory for differential item functioning;
- a priori hypothesis testing for construct validity;
- framework and thematic analysis for qualitative concept generation;
- descriptive, bivariate, fixed-effect, mixed-effect, generalized estimating equation, survival, and missing-data method classes in a methods-use review.

Keep model features that affect meaning. Examples are censoring, heteroscedasticity, random effects, correlation between coefficients, an added worst-state term, baseline adjustment, repeated measures, and the missing-data assumption. Do not make each coefficient, package, or software version an ontology concept.

Create a comparison record when the compared objects or conditions are central. Examples include cTTO-only, DCE-only, and hybrid model paths; EQ-5D-Y-4L and EQ-5D-Y-5L; frequency and severity response scales; local and foreign preference sources; single and multiple postbaseline analyses; and instruments tested in pain and no-pain groups.

### Family-specific extraction overlays

#### Valuation and value-set work

Record the exact target instrument, valued referent, respondent population, perspective, valuation task, task protocol, state or choice design, task counts, data role, modeling path, anchoring method, model-selection criteria, selected model, product geography, value range, and intended decision use. `DCE` is not enough when duration, perspective, blocking, or anchoring role differs. Keep cTTO, conventional TTO, lead-time TTO, lag-time TTO, DCE without duration, and DCE with duration distinct when reported.

#### Instrument development

Represent the development sequence. Link source material and target-group input to candidate content, testing, harmonization, and the resulting version. Record the target language for each language version. Separate comprehensibility, feasibility, preference, psychometric performance, valuation feasibility, and proxy-version development as different stages.

#### Measurement-property studies

For each evaluation, record the property, target instrument or item, data form, comparison or anchor, subgroup, method, a priori threshold, and finding. Do not combine item-level reliability with index or VAS reliability. Do not combine construct validity, content validity, known-group validity, and responsiveness under one broad `validity` result.

#### Qualitative content-validity studies

Record the target part of content validity. Keep comprehensiveness, relevance, and comprehensibility separate. Record sampling frame, interview mode and language, concept-elicitation task, coding approach, coder process, code filter, framework-generation process, comparison framework, added or missing concepts, saturation basis, and translation uncertainty.

#### Systematic reviews and evidence syntheses

The direct evidence sources are publications, trials, or registry records. Record databases, coverage dates, language limits, eligibility, duplicate-data handling, screening stages, included-unit count, synthesis method, review target, and the property or method taxonomy. Link findings to the reviewed evidence base. Do not treat every population in an included study as a direct participant sample of the review.

#### Practice surveys and data-resource protocols

For a practice survey, record the respondents' professional role, authority level, decision context, recruitment network, question domains, response scale, regional aggregation, and qualitative analysis. For a data-resource protocol, distinguish planned targets from completed collection. Link each country to the instrument battery and language when the battery varies by country.

### Findings, interpretation, impact, and gaps

Capture principal findings only. Keep these statement types separate:

- empirical finding;
- author interpretation;
- author-reported contribution;
- author-reported implication or recommendation;
- author-reported limitation;
- author-stated future work or evidence gap;
- documented use or effect;
- extractor observation or unresolved transfer limit.

Use `documented use` only when the paper reports actual use. Use `intended use`, `expected use`, or `recommended use` for prospective statements. Do not infer scientific, policy, or social impact.

## Applications to batch 01

### 1. 10.1007/s40258-021-00639-3

**Family and purpose.** Value-set development. The paper aimed to produce the first Danish EQ-5D-5L value set from adult general-population preferences. It also compared cTTO-only, DCE-only, and hybrid modeling paths. Main concepts are health-state valuation, health utility, QALY, anchoring, logical consistency, heteroscedasticity, censoring, and national priority setting.

**Components and evidence.** One Danish adult sample supplied evidence. Statistics Denmark selected a probability-based representative sample by age, gender, education, and region. A market-research panel later supplemented recruitment under the same representation targets. The paper reports 1,052 interviews conducted. Five interviewer-associated interviews, 12 interviews with software, withdrawal, or cognitive or emotional issues, and 21 interviews without both task types were removed. The analysis used 1,014 respondents. The final sample was close to the national population, with small age and education differences.

Two valuation-task components used the same respondents. Each respondent valued ten states with cTTO and seven pairs with DCE. The cTTO design covered 86 states in balanced blocks. The DCE design covered 196 pairs in 28 blocks. State order, pair order, and left-right position were randomized. The DCE did not include duration. The referent was an EQ-5D-5L health state. The response supplier was an adult member of the Danish general public.

**Instruments, administration, and protocol.** EQ-5D-5L was the health-state object valued and an administered self-health measure. EQ VAS was also administered. EQ-VT version 2.1 was the exact valuation platform and protocol. Interviews were interviewer-administered, computer-assisted, and in person. The article does not give an explicit instrument-language label. Interviewer training, the EQ-VT quality-control tool, protocol checks, feedback review, and a cTTO feedback module were material protocol details.

**Methods and comparisons.** The paper compared a random-intercept GLS cTTO model, random-effects Tobit cTTO model, conditional-logit DCE models, and hybrid combinations. The selected model was a heteroscedastic censored hybrid that joined cTTO and DCE data. Logical consistency was the main selection criterion. A sensitivity analysis restored 712 cTTO state valuations that respondents had marked as incorrectly ranked. The product was also compared with the Danish EQ-5D-3L value set and the Danish 5L crosswalk value set. These are direct-valuation versus mapped-score comparisons, not three equivalent products.

**Product and findings.** The product is a developed Danish EQ-5D-5L value set. The selected model removed the inconsistencies seen in separate task models. Predicted values ranged from -0.757 to 1. Anxiety or depression had the largest decrement, followed by pain or discomfort. The direct 5L set had 22% of states worse than dead, compared with 20% for the direct 3L set and 11% for the crosswalk set.

**Interpretation and boundaries.** The authors interpreted the hybrid model as the best approach for these data. They recommended use of the 5L value set for Danish QALY estimation and priority setting. This is a recommendation and expected use, not documented adoption or effect. Reported strengths were protocol adherence, training, quality monitoring, and representative recruitment. Reported limits included the recruitment-source change, small under-representation of young adults and people with lower education, uncertainty about cross-national preference differences, unresolved DCE anchoring theory, and the need for more work on the theoretical basis of hybrid models. No sample reuse was reported.

### 2. 10.1007/s11136-020-02688-y

**Family and purpose.** Measurement-property evidence synthesis with meta-analysis. The paper summarized psychometric evidence for the official EQ-5D-5L descriptive system and sought evidence gaps. The review target excluded clear analysis of EQ VAS because source papers did not always identify its version.

**Evidence sources and selection.** The evidence suppliers were publications, not direct study participants. PubMed or MEDLINE, PsycINFO, EMBASE, and the EuroQol website were searched for material published from 2011 through January 2019. Screening was independent and in duplicate, with senior adjudication. Eligible evidence concerned people aged 18 years or older, German or English reports, and the official EQ-5D-5L. Experimental 5L forms were excluded. The review included 99 papers from 32 countries. It recorded general-population and patient evidence across many clinical areas. When publications used the same dataset, the reviewers extracted that evidence once.

**Properties and methods.** Separate measurement evaluations covered missing responses, floor and ceiling distributions, test-retest reliability, construct, content, convergent and known-group validity, and responsiveness. Internal consistency was explicitly out of scope because the EQ-5D index has a preference-based measurement model. Kappa and ICC were kept distinct for item and index stability. Responsiveness methods included standardized effect size, standardized response mean, anchors, and minimally important difference. Random-effects models pooled the proportion in state 11111, mean index values, and transformed correlations.

**Findings.** The paper found acceptable missingness in 17 of 17 papers and acceptable floor results in 43 of 48. Index reliability was adequate in nine of nine papers, but individual dimensions had lower stability. Pooled correlations were strongest with other multi-attribute utility measures, physical or functional health, and pain. Correlations were weak for life satisfaction and cognition or communication. Fifteen studies addressed responsiveness. Effects were usually moderate in subgroups that improved, but the evidence base was heterogeneous. Large ceilings persisted in general-population samples.

**Interpretation and boundaries.** The authors interpreted the EQ-5D-5L as reliable and valid across a broad range of settings. They identified responsiveness as a main research gap. They also called for evidence from more regions and for specific clinical, health-service, and surveillance uses. Limitations included exclusion of experimental versions and application studies, no review of valuation methods, heterogeneous methods, and restricted regional coverage. No actual use or effect of the review was documented.

**Source conflict.** The abstract states that 889 publications were identified. The results state 496 initial records plus 397 update records, which totals 893. Keep both source statements. Do not select one count without source correction.

### 3. 10.1007/s11136-025-03983-2

**Family and purpose.** Population-health data-resource and study-protocol description. The paper describes the rationale, survey design, completed early rounds, governance, and future expansion of EQ-DAPHNIE. Its joint purposes are comparable population-health assessment and evaluation of health, wellbeing, and social-care instruments.

**Components and evidence.** A United Kingdom pilot preceded two country rounds. The target was 4,500 completed adult responses per country. Dynata recruited adult panel members. The study used quota sampling for age, sex, income, urban or rural area, and, where relevant, language. Enrollment was first come within a quota. Non-completers did not enter the final count. A 250-response soft launch in each country supported checks before full launch. Respondents supplied self-reported data about their own health. A separate anchoring-vignette task asked each respondent to rate a hypothetical person, Alex, who had the same age and background.

The paper reports these completed counts: pilot UK 3,012; round 1 UK 4,505, New Zealand 4,514, Australia 5,040, Canada 4,707, and US 4,523; round 2 France 4,502, Brazil 4,513, Japan 4,502, Netherlands 4,506, China 4,519, Spain 4,526, Mexico 4,508, Chile 4,503, Argentina 4,506, and Germany 4,537. The paper therefore describes completed data collection as well as future plans.

**Administration and languages.** The survey was self-administered on the LimeSurvey web platform. The core survey took about 20 minutes and about 50 screens. EQ-5D-5L came first, followed by its response-scale heterogeneity vignette. Other standardized measures were randomized. Some questions were conditional. No answer was mandatory. Age and marital status were repeated as consistency checks. The project translated survey content into Spanish, French, Portuguese, Japanese, Simplified Chinese, Dutch, and German, with other languages as required. Standardized language versions came from instrument developers when available.

**Country-specific instrument use.** All round 1 and round 2 countries received EQ-5D-5L. The remaining battery differed by country:

| Country or phase | Distinct battery details |
|---|---|
| UK pilot | EQ-HWB long form, PHQ-9, and GAD-7; no listed bolt-on or other standard measure. |
| Australia, Canada, US | EQ-HWB short form, PROMIS-10, ASCOT, WHO-5, OPQOL-brief, PHQ-2, and GAD-2. |
| New Zealand, UK round 1 | EQ-HWB long form, PROMIS-10, ASCOT, OPQOL-brief, PHQ-2, and GAD-2; no WHO-5. |
| Argentina, Chile, Mexico, Spain | Skin-irritation and self-confidence bolt-ons; EQ-HWB long form, PROMIS-10, ICECAP-A, WHO-5, OPQOL-brief, PHQ-2, and GAD-2. |
| Brazil, France | PROMIS-10, ICECAP-A, WHO-5, OPQOL-brief, PHQ-2, and GAD-2; no listed EQ-HWB or bolt-on. |
| China | Vision, hearing, breathing, sleep, tiredness, social-relationships, self-confidence, and cognition bolt-ons; EQ-HWB long form, PROMIS-10, ICECAP-A, WHO-5, OPQOL-brief, PHQ-2, and GAD-2. |
| Germany | Social-relationships, skin-irritation, and self-confidence bolt-ons; EQ-HWB long form, PROMIS-10, ASCOT, WHO-5, OPQOL-brief, PHQ-2, and GAD-2. |
| Japan | Cognition bolt-on; EQ-HWB long form, ASCOT, WHO-5, OPQOL-brief, PHQ-2, and GAD-2; no PROMIS-10. |
| Netherlands | All nine listed bolt-ons; PROMIS-10, ASCOT, WHO-5, OPQOL-brief, PHQ-2, and GAD-2; no listed EQ-HWB. |

EQ-HWB long means the experimental 25-item profile. Short means the 9-item short form. ASCOT is the SCT4 self-complete four-level form. OPQOL-brief was conditional on age 65 years or older. The nine possible EQ-5D-5L bolt-ons were vision, hearing, breathing, sleep, tiredness, social relationships, cognition, skin irritation, and self-confidence.

**Product, interpretation, and boundaries.** The products are a multinational survey infrastructure, completed country datasets, a common survey and collection protocol, and a platform for later population-health and instrument-comparison work. The paper does not report health outcomes or instrument-performance results. The authors expected the resource to support cross-country assessment and policy research. This is intended use, not documented effect. Reported limits were exclusion of people without adequate internet access, panel and representativeness bias, cultural differences in instrument function, and a cross-sectional design. Future work includes more regions, other sampling or collection methods, longitudinal follow-up, and serial panels. No external sample reuse was reported.

### 4. 10.1017/s0266462326103602

**Family and purpose.** HTA practice and research-needs survey. The paper asked HTA practitioners about current HRQoL and health-state utility practice, method and instrument views, data sources, data-quality problems, and research priorities for QALY-based evidence.

**Evidence sources and setting.** Respondents were individual HTA practitioners, advisors, contractors, and personnel involved in national listing, reimbursement, or pricing work. They did not respond as official agency representatives. The survey used purposive, network-based, two-stage recruitment through EuroQol members and professional contacts. Sixty countries were approached at the planning stage. The survey was distributed in 49 and received completed responses from 45. The final evidence base had 238 respondents from 65 HTA agencies. Region totals were Asia 95, Central or Eastern Europe 25, Western Europe 31, Latin America 38, Middle East or Africa 15, and Commonwealth countries 34. Of all respondents, 213 had QALY-related work.

**Administration and tasks.** The anonymous survey was self-administered on Qualtrics. The main form was in English. Respondents could answer open questions in a language of their choice. The form used six sections and four-point frequency scales. It asked about utility instruments, elicitation methods, data sources, data quality or appropriateness, and research priorities. Instrument names such as EQ-5D, SF-6D, and EQ-5D-Y were objects of reported practice. They were not administered as health measures to respondents.

**Methods.** Closed responses received descriptive analysis. Country-level modes, or medians when needed, fed regional medians. Research-priority scores were averaged first within country and then within region and globally. Open responses underwent translation by a forward-backward approach and structured content analysis. The main comparisons were across six regions, local versus foreign preference sources, general-public versus patient preferences, and different instruments and elicitation methods.

**Findings.** EQ-5D, SF-6D, and EQ-5D-Y were the three most frequently used utility instruments. TTO, VAS, and standard gamble were the three most frequently used elicitation methods. DCE use was less frequent and varied by region. Preferences from a foreign general population were used more often overall than local public preferences, although local public values were more common in Western Europe and Commonwealth settings. Common quality problems were poor representativeness, small samples, poor fit to cost-effectiveness model needs, and mixed methods or instruments in one model. The top global priorities were recent tariffs, child or adolescent instruments, and instruments that cover health and social care.

**Interpretation and boundaries.** The authors saw a wide shortage of suitable HRQoL and utility data. They recommended stakeholder engagement in instrument development, pediatric work, newer value sets, and better data resources. Current practice is documented through respondent reports, but the paper does not document a downstream policy change caused by the survey. Reported limits were small country samples, uncertain respondent authority, network and EuroQol-familiarity bias, no agency identifier, no agency-level analysis, no eligibility verification, and no reliable therapeutic-area subgroup analysis. The results describe practitioner views, not official national policy.

### 5. 10.1007/s11136-019-02115-x

**Family and purpose.** Multi-phase instrument development and response-level refinement. The paper developed and tested a five-level EQ-5D-Y descriptive system for ages 8 to 15. It did not set four or five levels in advance.

**Components and evidence.** Phase 1 first generated candidate severity labels from child HRQoL instruments, dictionaries, thesauruses, and two focus groups per country. The focus groups separated ages 8 to 10 and 11 to 15. A second phase-1 component used 255 individual sorting or response-scaling interviews across Germany, Spain, Sweden, and the UK. Younger children used a five-face sorting scale. Older children used a VAS. Participants came from school convenience samples, and the task order was randomized.

Phase 2 tested draft 4L and 5L forms through cognitive interviews. The phase-2 counts were Germany 33, Spain 35, Sweden 32, and UK 20, for a total of 120. Germany, Spain, and Sweden included healthy participants and participants receiving care for a health condition. The UK included school pupils only and tested the 5L form, not both forms. A harmonization component compared translated German, Spanish, and Swedish labels with UK English while it retained supported language-specific differences.

**Instruments, languages, and methods.** EQ-5D-Y-3L was the source instrument. Draft EQ-5D-Y-4L and EQ-5D-Y-5L forms were targets under development. The study produced German, Spanish, Swedish, and UK English self-report language versions. Methods included review, focus groups, thematic content analysis, label sorting, response scaling, quantitative label-selection criteria, cognitive paraphrasing and probing, and cross-language harmonization.

**Product and findings.** The product is a field-tested candidate EQ-5D-Y-5L descriptive system with five severity levels in each of five dimensions and 3,125 possible states. The initial work generated 233 labels. Seven to 16 labels per dimension and language reached rating. In direct 4L versus 5L testing, 5L preference was Germany 88%, Spain 68%, and Sweden 66%. UK participants did not make this comparison. Participants valued the additional precision and middle category. The study revised several Spanish labels after comprehension problems. In the UK, `extreme` replaced `terrible` for the highest pain and emotion levels after follow-up testing.

**Interpretation and boundaries.** The authors interpreted the new 5L form as comprehensible and feasible. They expected improved sensitivity and lifetime comparability with adult 5L, but they did not test these claims. The product was not yet psychometrically established or valued. No actual use was documented. Reported limits were convenience samples, low national representativeness, recruitment difficulty for children with health conditions, and small protocol differences in the UK and Spain. Future work includes psychometric testing, comparison with Y-3L, language-version validation, proxy versions, and valuation research.

**Source conflict.** The abstract says the country preference range was 68% to 88%. The detailed results report Sweden at 66%, Spain at 68%, and Germany at 88%. Use the detailed country values and retain the abstract range as a source conflict.

### 6. 10.1007/s40273-022-01216-9

**Family and purpose.** Value-set development for the Chinese EQ-5D-Y-3L. The paper followed the international youth valuation protocol but expanded its cTTO design. It compared mapping after DCE modeling with joint hybrid modeling.

**Components and evidence.** Two independent adult general-population samples supplied preferences. The DCE sample had 1,058 respondents. The cTTO sample had 418. The total was 1,476. Quotas covered gender, age, education, and rural or urban registered residence. Recruitment used purposive and snowball methods across 14 provinces or cities in five broad Chinese regions. The cTTO sample came from eight sites. Adults valued health for a hypothetical 10-year-old child. The child's relationship to the adult was not fixed.

**Tasks, administration, and protocol.** Both tasks used EQ-VT and face-to-face, one-to-one, computer-assisted personal interviews. DCE was the main source for relative dimension and level preferences. The design had 150 pairs in ten blocks of 15, with two-dimension overlap and no duration. cTTO provided QALY anchors. The expanded cTTO design had 28 states in three blocks of ten, with state 33333 in each block. cTTO respondents completed practice states. The study used interviewer training and cTTO quality control. The exact administered language-version label is not stated in the article.

**Model paths and comparison.** Path 1 used a correlated-coefficient mixed logit for DCE, then OLS mapping of latent DCE values to observed cTTO means. Path 2 used a heteroscedastic hybrid model that fitted DCE and cTTO jointly. A hybrid variant added an `A3` term for the extra decrement in state 33333. Selection used coefficient significance, monotonicity, and mean absolute prediction error for the observed cTTO states. The selected model was the hybrid with A3.

**Product and findings.** The product is an estimated Chinese EQ-5D-Y-3L value set. Mean observed cTTO values ranged from 0.924 for 11112 to -0.088 for 33333. The selected hybrid predicted 33333 at -0.089, had no insignificant or inconsistent coefficients, and had the lowest prediction error among the main candidate paths. It captured a large gap between 33333 and the next-worst observed state.

**Interpretation and boundaries.** The authors said the expanded cTTO design and hybrid model made fuller use of the evidence and could support pediatric economic evaluation in China. This is intended use, not documented HTA use. Reported limits were cTTO collection in only eight sites, an unspecified relationship to the hypothetical child, possible cTTO sensitivity and ethical problems, task-specific preference differences, and uncertain transfer across adult and youth value sets. Future work includes lag-time TTO, a DCE design that includes 33333, reasons for the worst-state gap, age effects, adolescent preferences, and an updated valuation protocol.

**Source conflict.** The key-points box says the sample came from four regions. The methods name 14 provinces or cities across five broad geographic regions and eight cTTO sites. Keep these three geographic levels separate. Treat `four regions` as a source conflict.

### 7. 10.1007/s11136-025-04003-z

**Family and purpose.** Secondary measurement-property analysis. The paper compared frequency and severity response scales for pain and discomfort in the experimental EQ-HWB and used the EQ-5D-5L pain or discomfort item as a reference measure.

**Evidence reuse, sources, and administration.** The study is a secondary analysis of a previously collected dyadic survey. It reused 1,008 records: 504 informal caregivers and their 504 adult care recipients. Caregivers had supplied unpaid care to an adult relative or friend for at least six months. The Qualtrics caregiver panel supported recruitment and web administration. A sequential linking process let both members complete the survey in one session without discussion. Measures were randomized. Attention checks and minimum completion times supported quality control. Analysis was at the individual level, not the dyad level. Conditions were self-reported. The article body does not clearly state the sample country, so the country remains not reported in this extraction.

**Instrument uses and comparisons.** EQ-HWB was an experimental 25-item profile. EQ-HWB-S was a 9-item classifier embedded in it. Both used a seven-day recall period. Four distinct five-level items assessed pain frequency, pain severity, discomfort frequency, and discomfort severity. EQ-5D-5L used a combined pain or discomfort severity item with a `today` recall period. Other measures, including CarerQoL and CARE-2B, were in the source survey but were not targets of this analysis.

**Measurement evaluations and methods.** The paper used Spearman correlations for overlap, Shannon H' and J' for informativity, a graded-response IRT model for item discrimination and thresholds, ordinal logistic regression or IRT for uniform and non-uniform differential item functioning, and four ordinal logistic models for condition associations. These methods answer different property questions and must not be combined as one generic psychometric result.

**Findings.** Pain frequency and severity correlated at 0.81. All pain and discomfort item correlations exceeded 0.5. Frequency scales had higher informativity for pain and discomfort. Severity items had greater discrimination at high trait levels, while frequency items were more sensitive at lower levels. Total DIF was large for pain and negligible for discomfort. Immunologic and musculoskeletal conditions had the strongest associations with pain frequency.

**Interpretation and boundaries.** The authors interpreted frequency and severity as complementary for pain and discomfort. They suggested both for a longer instrument and frequency for a shorter instrument when broad-range informativity is the goal. This is a design implication, not a documented instrument change. Limits were cross-sectional data, self-reported conditions, and uncertain cultural and language transfer. Future research should test recall periods and replicate across clinical, cultural, and linguistic contexts. The different recall periods of EQ-HWB and EQ-5D-5L are a material comparison condition.

### 8. 10.1007/s11136-025-04038-2

**Family and purpose.** Qualitative content-validity and conceptual-framework comparison. The paper developed a Chinese lay QoL framework and compared it with the EQ-HWB framework. It tested comprehensiveness only. Relevance and comprehensibility were reserved for later work.

**Components and evidence.** Two pilot rounds with six people refined the topic guide. The formal sample had 30 respondents: ten healthy people, ten patients, and ten informal caregivers. Quotas covered age, gender, education, medical condition, and rural or urban Hukou. Twenty-two respondents came from Guangzhou and eight from Harbin. Interviews were face to face in quiet public settings from March through June 2023. The topic guide started in English, was translated into Chinese, and changed `poor well-being` to `poor QoL` after pilot comprehension problems. Interviews, transcription, and analysis were in Chinese; transcripts used Simplified Chinese.

**Tasks and methods.** Respondents described QoL, rated their own QoL from 1 to 10, explained poor QoL, and gave examples. The interviewer summarized answers for respondent confirmation. Two coders used inductive and deductive thematic framework analysis. Ninety-six EQ-HWB candidate items formed the deductive codebook. The team generated 221 codes, removed 34 by five explicit filters, retained 187, and organized them into 57 subthemes and eight themes. The filters excluded external or economic causes, time-dependent outcomes, concepts that did not distinguish good from poor QoL, organ-level concepts, and future outcomes. The resulting framework was compared with the seven-domain EQ-HWB conceptual framework.

**Product and findings.** The product is a Chinese lay QoL conceptual framework with feeling and emotion, cognition, self-identity, coping, physical sensation, relationship, activity, and mindset. Seven of eight themes aligned with EQ-HWB. Eighteen of 57 subthemes aligned under the paper's stated comparison. `Mindset` was the added theme. The study also found added subthemes and different placement for boredom and sleep. Autonomy had a broader dependence-related meaning. EQ-HWB contained hearing, which these respondents did not produce.

**Interpretation and boundaries.** The authors interpreted the framework as support for EQ-HWB comprehensiveness in China. They did not consider the missing concepts large enough to invalidate the instrument. This is content-validity evidence, not a complete validation or documented use. Limits were the young, healthy, educated Harbin subgroup, community patients with mostly chronic disease, no hospitalized severe-disease group, difficult translation of `mindset` and positive or negative energy, and subjective saturation. The abstract says saturation occurred in the last three interviews, while the limitations say views repeated in the last ten and no formal saturation rule was set. Keep this qualification with the saturation statement. Future work covers relevance, comprehensibility, more diverse samples, and cultural adaptation.

### 9. 10.1016/j.jval.2025.02.001

**Family and purpose.** Statistical-practice evidence synthesis. The paper reviewed how randomized clinical trials analyzed postbaseline EQ-5D treatment effects.

**Evidence sources and selection.** MEDLINE and EMBASE were searched from inception through 15 November 2021. ClinicalTrials.gov was searched on 16 August 2023, with publication follow-up in PubMed. Eligible units were randomized trials that analyzed postbaseline EQ-5D by treatment group. English journal articles, HTA reports, and registry results were eligible. Pilot or feasibility studies, reviews, editorials, conference abstracts, and non-English reports were excluded. QALYs and quality-adjusted time were excluded because they combine time and quality of life. The review mapped multiple publications to one trial to prevent duplicate counting. It screened 9,030 titles or abstracts, assessed 7,056 full texts, and included 2,125 unique trials.

**Instrument data and method taxonomy.** The review distinguished EQ-5D dimension responses, EQ VAS, and utility. It also distinguished numerical and categorical formats and single versus multiple postbaseline collection. Method classes were descriptive, bivariate, multivariable, and survival analysis. Regression subtypes included fixed-effect, mixed-effect, generalized estimating equation, and less common specialized models. Separate fields covered model-assumption checks, baseline adjustment, minimally important difference, explicit missing-data assessment, and imputation method.

**Findings.** Utility was analyzed in 1,592 trials, EQ VAS in 1,197, and dimension responses in 385. EQ-5D was mainly a secondary or exploratory endpoint. A linear fixed-effect model was most common for one postbaseline utility measure. A linear mixed-effect model was most common for multiple postbaseline measures. Among 2,054 trials with numerical EQ-5D analysis, 10.8% reported assumption checks and 21.3% adjusted for baseline. Missing data were explicitly assessed in 661 trials. Of these, 347 used imputation, most often multiple imputation or last observation carried forward.

**Interpretation and boundaries.** The authors found large method variation, sparse analysis of dimensions, and weak reporting of assumptions, baseline adjustment, and missing-data handling. They called for method comparisons and analysis guidance that starts with the estimand. They noted that utilities combine profile responses with a value set, so a value-set choice can alter treatment effects. No guidance product or practice change was documented. Reported limits were the long search period, changing practice over time, sparse reporting of secondary outcomes, and possible undercounting of adjustment and imputation. No trial quality or risk-of-bias appraisal was done because the review target was method use, not treatment-effect synthesis.

### 10. 10.1007/s10198-025-01770-x

**Family and purpose.** Comparative measurement-property study with a seven-day test-retest component. It compared the Brazilian-Portuguese self-complete EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D in children and adolescents with and without self-reported musculoskeletal pain.

**Evidence sources and components.** Schools in urban Sao Paulo state supplied 356 children and adolescents aged 8 to 18. Of these, 181 met the paper's PIP-Kids definition of musculoskeletal pain and 175 did not report pain. The pain definition required pain in the last month plus interference with normal or recreational activity or school attendance. It was self-reported and not a medical diagnosis. Pain caused by trauma, sports injury, surgery, cancer, infection, fracture, inflammatory disease, or diagnosed traumatic soft-tissue injury was excluded. A retest after seven days included 231 children classified as stable: 96 with pain and 135 without pain.

**Instruments and administration.** Participants self-completed paper-and-pencil measures in classrooms. Researchers and teachers could help with interpretation. Exact forms were Brazilian-Portuguese EQ-5D-Y-3L and EQ-5D-Y-5L, CHU9D, PedsQL version 4.0 child or adolescent self-report, PIP-Kids, and a numerical pain rating scale. EQ-5D-Y instruments and CHU9D used `today`; PedsQL and PIP-Kids used the last month. The EQ-5D-Y order was randomized, although the two descriptive systems were consecutive. A Brazilian EQ-5D-Y-3L value set existed, but the study analyzed profiles and EQ VAS rather than youth utility scores. No Brazilian CHU9D value set was available.

**Measurement evaluations and methods.** Feasibility used missing responses and completion. Floor and ceiling analyses used items and full profiles. Test-retest reliability used Kappa for dimensions and ICC for EQ VAS, with agreement, standard error of measurement, and smallest detectable change. Construct validity used a priori correlation hypotheses and a 75% COSMIN criterion. Known-group validity compared pain and no-pain groups and pain-intensity groups.

**Findings.** Missingness was low for Y-3L but reached 12.7% for the Y-5L usual-activities item. Completion was 96% or higher for the three preference-based instruments. The full-profile ceiling in the pain group was 18.2% for Y-3L and 16.0% for Y-5L. Kappa ranges were fair to moderate for both youth EQ-5D versions and poor to moderate for CHU9D. EQ VAS ICC was substantial in the pain group and moderate in the no-pain group. For participants with pain, Y-3L and Y-5L met the a priori construct-validity criterion against PedsQL. Y-5L met it against CHU9D in both groups. All three instruments distinguished pain from no pain, with an exception for the youth EQ-5D self-care dimension. Pain-severity discrimination also varied by dimension.

**Interpretation and boundaries.** The authors supported use of all three instruments, especially in Brazilian children and adolescents with musculoskeletal pain. They described potential clinical and economic-evaluation use, but documented no actual adoption or effect. Limits were self-reported and heterogeneous pain, no diagnostic confirmation, no gold standard, no timing or comprehension measure for feasibility, consecutive EQ-5D-Y forms, differing recall periods and response scales, and no utility, redistribution, Shannon, or responsiveness analysis. The last-month pain definition versus `today` instrument recall explains why 36% of the pain group reported no current pain problem. Future work includes other conditions and settings, children younger than eight, proxy forms, utility-score properties, and responsiveness.

## Granularity decision log

1. **Keep respondent, referent, and target population separate.** Adults valued a hypothetical ten-year-old in paper 6, practitioners described HTA practice in paper 4, and respondents rated a hypothetical Alex in paper 3. One `population` field would give false retrieval results for user questions 6, 7, 20, and 25.

2. **Make exact instrument version, variant, language, and role independently searchable.** Papers 5, 6, and 10 show that Y-3L, candidate Y-4L, and Y-5L are not interchangeable. Papers 3 and 7 show that EQ-HWB long and short forms can occur in the same project. This supports user questions 3, 4, 14, 20, and 23.

3. **Do not treat an instrument that is discussed as an administered instrument.** Paper 4 measures practitioner reports about EQ-5D, SF-6D, and EQ-5D-Y. Paper 9 reviews EQ-5D analyses in trials. This distinction prevents false matches for user questions 3, 11, and 20.

4. **Decompose administration mode.** Papers 1 and 6 used in-person, interviewer-administered, computer-assisted interviews. Papers 3, 4, and 7 used web surveys. Paper 10 used classroom paper forms. These differences can change selection, task burden, and interpretation. They support user questions 11, 13, 20, and 24.

5. **Represent task design below the paper level.** cTTO and DCE have different roles in papers 1 and 6. Phase-specific child tasks differ in paper 5. A broad paper-level method label would hide blocking, counts, framing, and anchoring. This supports user questions 5, 9, 10, 12, and 21.

6. **Keep valuation data role separate from task name.** DCE estimated relative importance and cTTO anchored the youth scale in paper 6, while paper 1 modeled both alone and jointly. This distinction changes comparison and interpretation for user questions 10, 12, 13, 21, and 23.

7. **Use a purpose-bearing method-use record.** A hybrid value-set model, a random-effects meta-analysis, an IRT model, and a linear mixed model do different work. The record needs target, input, role, and key features, not only a method name. Papers 1, 2, 6, 7, 9, and 10 support user questions 9, 12, 13, 21, and 22.

8. **Keep measurement properties distinct.** Paper 2 found good index reliability but item instability and weak responsiveness evidence. Paper 10 found different reliability and validity patterns by score and group. Paper 8 tested only comprehensiveness. A broad `psychometric validation` tag would conceal these differences. This supports user questions 9, 12, 15, 16, 21, and 22.

9. **Make comparison conditions explicit.** Recall period explains part of the pain discrepancy in paper 10. Frequency and severity plus recall period affect paper 7. Direct and crosswalk value sets differ in paper 1. This supports user questions 13, 20, 21, and 22.

10. **Use labeled stage counts.** Papers 1, 2, 4, 9, and 10 have important recruitment, screening, completion, exclusion, and analysis counts. One sample-size value cannot answer user question 8 and can misstate denominators.

11. **Represent products with evidence-based maturity.** Paper 5 produced a field-tested candidate instrument that still needed psychometric and valuation work. Paper 6 estimated a value set. Paper 3 produced infrastructure and completed datasets but no outcome results. This supports user questions 14 and 23 without an unsupported maturity score.

12. **Link country to the applicable instrument battery and language.** Paper 3 used different EQ-HWB variants, bolt-ons, and comparator instruments by country. Paper-level lists alone would create false instrument-country combinations for user questions 4, 20, and 24.

13. **Represent evidence reuse.** Paper 7 is a secondary analysis of an earlier dyadic dataset. Papers 2 and 9 removed duplicate evidence from related publications. Paper 6 extends a standard protocol. These are different dependency relations for user questions 19 and 25.

14. **Keep finding, interpretation, implication, limitation, and gap separate.** Each paper contains positive findings plus transfer limits or future work. This separation supports user questions 15 to 18 and prevents an author recommendation from appearing as an observed effect.

15. **Preserve source conflicts as extraction uncertainty.** Papers 2, 5, and 6 contain internal count conflicts. These conflicts affect paper understanding and user question 16. Silent normalization would hide source quality.

16. **Use concepts at a practical, mid-level depth.** Keep terms such as HRQoL, health utility, QALY, content validity, response-scale heterogeneity, informativity, and HTA. Keep fine qualitative concepts such as `mindset` when they are a principal comparative finding. Do not turn every interview code or EQ-5D response label into a corpus-wide concept. This supports user questions 2, 20, and 22.

## Rejected distinctions and structures

- **A fixed field set for every study family.** It would make valuation fields empty or forced in qualitative and review papers. The common units plus family overlays are clearer.
- **One node for every reported estimate or coefficient.** This would create a detailed claim graph that the purpose excludes. Retain only anchor values that explain a principal result or product.
- **One component for every analysis or table.** Create a component only when scope, sample, task, or interpretation differs. Use repeatable method uses within that component.
- **A single broad `digital` administration term.** Web self-administration and computer-assisted personal interview have different respondent interactions.
- **A single broad `validity` property.** Content, construct, known-group, convergent, and criterion validity are not interchangeable.
- **A single broad `TTO` term.** Preserve composite, conventional, lead-time, and lag-time forms when stated. Do not infer a form when the paper only says TTO.
- **A universal product-maturity score.** Maturity depends on product type and evidence. Use stage statements and remaining work.
- **Country inferred from author affiliation.** An affiliation is deterministic metadata and does not prove sample geography. Paper 7 therefore retains an unresolved country.
- **Software as a main ontology entity.** Record software or platform only when it identifies a protocol, administration route, or reproducibility detail, such as EQ-VT, LimeSurvey, Qualtrics, or a named modeling function.
- **Every cited instrument as an instrument use.** Use `mentioned background instrument` only when needed. It must not retrieve as administered or evaluated.
- **Inferred impact.** Recommendations, intended resources, and expected HTA uses are not documented effects.
- **Corpus-level gaps from one paper.** Record only author-stated gaps in each paper. Derive corpus gaps after extraction.

## Unresolved cases after round 1

1. Paper 2 reports 889 identified publications in the abstract but gives 496 plus 397 in the results. The source needs correction before one count becomes canonical.
2. Paper 5 reports a 68% to 88% preference range in the abstract, but the detailed country result includes Sweden at 66%.
3. Paper 6 says `four regions` in the key-points box, while the methods report 14 provinces or cities in five broad regions and cTTO collection at eight sites.
4. Paper 7 does not clearly state the participant country in its article body. Do not infer it from affiliations or related-paper titles.
5. Some valuation papers do not state the administered language-version label even when the national context suggests a language. Keep language as not reported unless the paper names it.
6. Paper 8 uses a numerical framework-alignment statement that reads `68% (18/57)`. Eighteen of 57 is approximately 32%, not 68%. Retain the stated percentage and fraction as a source conflict until corrected.
7. The current controlled family terms come from ten papers. Translation-only, mapping-only, implementation, population-norm result, and bolt-on development papers can require new overlays in later rounds. Add them only when paper evidence tests their boundaries.
8. Paper 10 authors describe hypotheses below the 75% threshold as inadequate validity in results, but later clarify that this means the a priori hypotheses did not match and does not prove that an instrument itself is invalid. Preserve both the criterion result and this interpretive qualification.

## Run note

- Lineage: C.
- Round and batch: round 1, `batch-01.tsv`, ten papers.
- Task version: version 2, frozen 2026-08-16.
- Agent: fresh Codex round-1 lineage agent; exact service model identifier was not exposed in the task context.
- Branch: `experiment/ontology-v2-c`.
- Base commit: `858adec5d930fdbb80af94aaa8388c476ec7f14f`.
- Run time recorded: 2026-08-16T16:58:13Z.
- Input verification: all ten article files matched the manifest SHA-256 values and byte counts.

| Order | Paper | Bytes | SHA-256 check |
|---:|---|---:|---|
| 1 | 10.1007/s40258-021-00639-3 | 77,402 | matched `0d6462427e64575f7139aaf3e362a742b2aa7c66106ad5f1261e2e2f5cb6c25f` |
| 2 | 10.1007/s11136-020-02688-y | 121,988 | matched `5d7c04ab1bf4b1d87968b8d8cc575c55820c8c1ea3019acf189a876b1f32bb96` |
| 3 | 10.1007/s11136-025-03983-2 | 73,694 | matched `afc648a5368fb945d630b3b9a8cae8a92a9f18b8b489be05f308847bd549dc77` |
| 4 | 10.1017/s0266462326103602 | 101,826 | matched `4f26cab992adb34e099c71814ee81c54b02de2bffc8ad03c5f824627b93901be` |
| 5 | 10.1007/s11136-019-02115-x | 69,271 | matched `04548203cbc5d71bba6264c57524d711ef2883c370edc52006135a39e0eab645` |
| 6 | 10.1007/s40273-022-01216-9 | 55,701 | matched `e86e0424c494875ca381b346f7b1e754e10b3f9912e8bef933efd9c625749b1d` |
| 7 | 10.1007/s11136-025-04003-z | 58,977 | matched `b94ca45ec043a5b7b81d28380e4d24256b09bb60f846c3a8b8ac80a0090ee5a8` |
| 8 | 10.1007/s11136-025-04038-2 | 76,716 | matched `168d53aed9f5436771a17e2560de98f312835ceea2df0b76cf64f31f8de92608` |
| 9 | 10.1016/j.jval.2025.02.001 | 50,386 | matched `45d9c8ae457cb963d4fb0be5882c72526e7fbcff050b234d29f5bbe94719f2ac` |
| 10 | 10.1007/s10198-025-01770-x | 173,513 | matched `087da109d92a3fb7edf1c86e6a127a1b3c8251c03a41e3faaf64d4e43af7e7d9` |

- Mechanical note: the first verification shell loop used zsh's read-only `status` variable and stopped before it produced results. A corrected read-only check used a different variable. It verified all ten inputs. No source file changed.
- Repository note: the root `.gitignore` rule `/pilot/` ignores this lineage path. The record is present in the worktree, but normal `git status` does not show it. This run did not stage or commit the file.
- Scope note: this run used only the supplied version-2 purpose, user questions, task, protocol, batch-01 manifest, and ten batch-01 article texts. It did not use another lineage or prior ontology work.
