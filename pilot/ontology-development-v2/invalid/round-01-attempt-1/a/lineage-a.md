# Lineage A: paper-first EuroQol ontology

Status: round 1, batch 01, 2026-08-16.

This record gives the current ontology, the extraction guide, and its application to all ten papers in batch 01. It does not define a JSON contract. The paper is always the main record. Paper-local components hold detail only when samples, phases, tasks, comparisons, or analyses differ.

## 1. Required questions and model boundary

The ontology must support these actions:

1. Find papers by exact instrument, version, language, population, country, condition, method, mode, purpose, or product.
2. Explain what a paper tried to do, which evidence it used, and what it produced.
3. Separate the person who supplied an answer from the person or health state that the answer describes.
4. Compare methods within and across valuation, psychometric, instrument-development, population-health, qualitative, review, and implementation research.
5. Explain which population, timing, mode, scoring route, or other condition makes a comparison valid or limited.
6. Retrieve principal findings and keep them separate from author interpretation, implications, limitations, and future work.
7. Find products and their reported stage. Distinguish a completed product from a proposed, experimental, or planned product.
8. Trace sample, data-set, protocol, model, value-set, or other research-object reuse.

The ontology does not copy deterministic bibliographic data. It links to the paper identifier that the source layer supplies. It also does not model researchers, citations, funding, affiliations, or portfolio statistics. Corpus trends and corpus gaps are later derived results.

## 2. Current ontology and extraction guide

### 2.1 Main semantic units

| Unit | Meaning and use | Minimum useful content |
|---|---|---|
| **Paper record** | The main semantic record. | Paper identifier; concise objective; one or more study-family tags; contribution summary; links to components, products, findings, and reuse. |
| **Study component** | A subordinate part that has its own sample, phase, task, comparison, analysis, or result. Create it only when the distinction changes retrieval or interpretation. | Component type; local purpose; sequence or parent; evidence source; methods; outputs; relation to other components. |
| **Evidence group** | A set of people, papers, trials, agencies, records, or other sources that supply evidence. | Source type; selection and recruitment; inclusion and exclusion; country and setting; population facets; important stage counts. |
| **Population role** | A role in an evidence statement. The same person can have more than one role. | `respondent`, `referent`, `target population`, or `decision population`. |
| **Instrument identity** | A reusable identity for an instrument family, exact version, variant, language form, and report form. | Family; exact version or variant when stated; language; self/proxy form; experimental or official status when stated. |
| **Instrument participation** | A paper-local relation between an instrument and a component. This avoids the false statement that every named instrument was administered. | Role; instrument identity; component; respondent and referent; mode; recall period; scoring or value-set route when material. |
| **Method application** | A method used for a stated purpose on stated data. A method name alone is not sufficient. | Method family and exact method; purpose; input or target; output or inference type; protocol or software when it changes comparability. |
| **Comparison** | A paper-local comparison that can include more than two conditions. | Objects compared; comparison basis; material differences in population, time, language, mode, task, scoring, or analysis. |
| **Product** | A research output with identity and maturity. | Product type; target instrument or context; country/language; stage; evidence of reported use, if any; next required step. |
| **Reuse statement** | An explicit or strongly supported link to earlier evidence or methods. | Reused object type; source if stated; purpose; whether the paper reanalyzes, extends, anchors to, or only cites it. |
| **Outcome summary** | A concise paper- or component-level statement. Do not make a detailed claim graph. | Statement type; scope; subject; direction or conclusion; selected decisive value if needed; source section; attribution. |
| **Extraction uncertainty** | A source conflict, unclear boundary, transfer limit, or extractor caution. | Exact issue; affected element; retained representation; source locations. |

The main relations are:

```text
Paper
  -> contains -> Study component
  -> addresses -> Concept, construct, framework, or practical topic
  -> produces -> Product
  -> reports -> Outcome summary
  -> reuses or extends -> Research object

Study component
  -> draws evidence from -> Evidence group
  -> uses, assesses, values, adapts, compares, or produces -> Instrument participation
  -> applies -> Method application
  -> makes -> Comparison
  -> supports -> Product or outcome summary

Evidence group
  -> has -> Respondent
  -> supplies answers about -> Referent
  -> is intended to represent -> Target population
  -> informs -> Decision population or decision context
```

These relations are conceptual. They do not require a graph database or a fixed storage schema.

### 2.2 Controlled terms, repeatable values, relations, and narrative

Use a small controlled vocabulary for stable retrieval facets. Keep exact source wording as a display value when it is useful.

| Information | Representation | Current guidance |
|---|---|---|
| Study family | Controlled, multi-valued tag | Seed terms: `valuation/value-set development`, `psychometric or measurement-property study`, `instrument development`, `translation or cultural adaptation`, `mapping`, `population norm or surveillance`, `implementation or practice study`, `systematic evidence synthesis`, `qualitative concept or content-validity study`, `study protocol or infrastructure`, and `clinical or economic application`. Do not force one exclusive family. |
| Purpose | Controlled action plus concise narrative | Actions include develop, adapt, value, evaluate, compare, describe, synthesize, validate, monitor, and identify needs. Preserve the exact study objective in one short statement. |
| Topic, concept, construct, theory, or framework | Typed repeatable term | Distinguish a measured construct from an analytic framework and from a practical topic. Keep paper-local theme hierarchies subordinate to the paper unless later reuse proves that a corpus term is stable. |
| Instrument role | Controlled relation | `administered measure`, `valuation target`, `development target`, `evaluation target`, `comparator`, `sample classifier or anchor`, `scored output`, `value set applied`, `survey topic`, `product`, or `background mention`. Do not promote a background mention into an instrument use. |
| Country and language | Repeatable structured value | State the role: evidence location, target population, value-set jurisdiction, survey language, instrument language, or decision context. These roles are not interchangeable. |
| Administration mode | Controlled value plus detail | Examples in this batch are web self-completion, paper self-completion, computer-assisted personal interview, face-to-face qualitative interview, and focus group. Record assistance and proxy status separately. |
| Study design | Controlled value | Examples are cross-sectional survey, repeated-measure measurement study, systematic review, qualitative interview study, and multi-phase instrument-development study. |
| Method | Method application relation | Record the exact method and its purpose. For example, `mixed logit` estimates DCE preferences, while `OLS mapping` anchors latent values. |
| Psychometric property | Controlled value | Use `feasibility/missingness`, `distribution`, `ceiling`, `floor`, `test-retest reliability`, `measurement error`, `construct validity`, `convergent validity`, `known-group validity`, `content validity`, `responsiveness`, `informativity`, `discrimination`, and `differential item functioning`. Link each property to its target instrument, outcome level, comparator or anchor, subgroup, and method. |
| Valuation task | Controlled value with structured qualifiers | Distinguish cTTO, other TTO forms, DCE, DCE with duration, VAS, standard gamble, PTO, and other tasks. Record perspective or referent, protocol, design, task count, worse-than-dead handling, anchoring role, and administration when material. |
| Statistical analysis | Method application relation | Record outcome type, data format, single or repeated time points, model family, baseline adjustment, missing-data handling, assumption checks, and inference purpose when these affect interpretation. |
| Selection and sample flow | Repeatable stage values | Keep invited, screened, consented, completed, excluded, analyzed, and stable-retest counts when they explain evidence strength. Do not copy every demographic cell. |
| Product type and stage | Controlled value plus narrative | Product types in this batch include value set, instrument version, conceptual framework, data infrastructure or data set, and evidence synthesis. Stage values are proposed, draft, experimental, developed, tested, operational, published, and reported in use. Use only stages that the paper supports. |
| Principal finding | Concise narrative with structured scope | State the target, population or subgroup, comparison, and direction. Keep only decisive numbers. |
| Interpretation, limitation, implication, documented use, and future work | Separate concise narratives | Mark each as author-reported. Keep actual documented use separate from expected, recommended, or possible use. |
| Extractor observation | Explicitly marked narrative | Use only for a source conflict, unclear boundary, or narrow scope note. Do not infer impact. |

### 2.3 Component rule

Create a component when at least one of these conditions is true:

- A phase has a different purpose or produces an input for a later phase.
- A sample has a different respondent or referent, recruitment path, or analysis.
- A task supplies a different evidence type, such as cTTO and DCE.
- An analysis has a different target, comparison, or inference purpose.
- A review has separate search, screening, extraction, and synthesis parts that are needed to explain the result.

Do not create a component only because the paper has a section heading. Keep a component subordinate to its paper. In a dyadic study, model the dyad design and the two participant roles. Do not create a node for every participant or dyad.

### 2.4 Study-family paths

#### Valuation and value-set development

Record the valued instrument and jurisdiction, respondent population, valuation referent, task, protocol, experimental design, health states or choice sets, administration, quality control, exclusion rules, model candidates, anchoring or hybrid relation, model-selection criteria, final model, value-set stage, and main transfer limits.

Do not merge cTTO and DCE under `preference elicitation`. In papers 1 and 6, they supply different data and have different modeling roles. Also keep a task separate from a statistical model.

#### Psychometric and measurement-property studies

For each property, record the target instrument and outcome level. Also record the comparator or anchor, subgroup, timing, analytic method, decision rule, and result. `Validity` alone is too broad. A result for an index score must not be applied to item or dimension results.

#### Instrument development and cultural adaptation

Record the product under development, each phase, participant involvement, candidate content, selection rule, cognitive testing, language-specific decisions, harmonization, rejected candidate, resulting version, and next validation step. Keep a language-specific wording decision distinct from literal translation equivalence.

#### Systematic evidence synthesis

Record databases and coverage dates, eligible evidence type, target instrument or outcome, selection rules, duplicate-data handling, number and scope of included sources, extraction categories, synthesis method, whether quality appraisal occurred, main evidence gaps, and transfer limits.

#### Population data, protocols, and infrastructure

Record planned versus completed work. Keep country rounds, samples, instruments, translations, data-quality procedures, conditional modules, and product maturity. A protocol can report an operational infrastructure without reporting the later substantive analyses.

#### Stakeholder practice and implementation surveys

Record who answers, whether answers are personal or official agency positions, recruitment frame, survey topics, aggregation unit, qualitative analysis, current practices, quality problems, and priorities. Instruments that respondents rate are `survey topics`, not administered health measures.

#### Qualitative concept and content-validity work

Record participant groups, sampling, setting, interview or focus-group format, coding approach, starting framework, inductive additions, consensus method, theme hierarchy, comparison basis, saturation method, and content-validity aspect. Do not convert every paper-local code into a global ontology concept.

### 2.5 Outcome and evidence rule

Each outcome summary must have one of these types:

- `principal finding`;
- `author interpretation`;
- `author-reported limitation`;
- `author-reported implication`;
- `documented use or effect`;
- `author-stated future work or gap`;
- `extractor uncertainty`.

Give the paper section that supports the statement. A short section reference is sufficient. Do not build a claim-to-sentence graph. Use exact numbers only when they define the sample, task, product range, decision rule, or principal result. Do not copy full coefficient tables or all confidence intervals.

## 3. Applications to batch 01

### Paper 1 — 10.1007/s40258-021-00639-3

Source: `corpus/20170400/doi_10.1007_s40258-021-00639-3.md`.

**Study family and purpose.** Valuation and value-set development, with a model-comparison component. The paper aimed to create the first Danish EQ-5D-5L value set from Danish adult general-population preferences and to select a model that could use cTTO alone or cTTO with DCE. Central topics were QALY weights, Danish priority setting, worse-than-dead values, representativeness, and hybrid modeling. Evidence: Abstract; Introduction.

**Component map.**

1. `P1-C1 sample and recruitment`: Adults older than 18 in Denmark. Statistics Denmark supplied a random population frame and monitored age, gender, education, and region. A market-research panel became a second recruitment source when recruitment was slow. The study completed 1,052 interviews and analyzed 1,014 after stated exclusions. The intended target was the Danish adult general population. Evidence: Participant Recruitment; Results, The Sample.
2. `P1-C2 valuation interview`: Computer-assisted personal interviews used EQ-VT 2.1. Each respondent reported own health with EQ-5D-5L and EQ VAS, valued ten EQ-5D-5L states by cTTO, and completed seven paired DCE choices. The cTTO task used conventional TTO for better-than-dead states and lead-time TTO for worse-than-dead states. DCE did not include duration. Evidence: The Valuation Interview; Techniques for Eliciting Preferences; Health States Valued.
3. `P1-C3 quality control`: The study used interviewer training, the EQ-VT quality-control tool, protocol checks, feedback, and rules to remove poorly performed interviews. Feedback-module reversals were excluded from the main cTTO model and restored in sensitivity analysis. Evidence: Data Quality; Statistical Analyses; Sensitivity Analyses.
4. `P1-C4 model comparison`: cTTO candidates were a GLS random-intercept model and a random-effects Tobit model. DCE candidates included conditional logit variants. Hybrid candidates combined DCE with the cTTO models. Logical consistency was the decisive model criterion. Evidence: Data Modelling.
5. `P1-C5 external comparison`: The final Danish EQ-5D-5L value set was compared with the Danish EQ-5D-3L value set and the Danish 5L crosswalk value set. Evidence: Comparison of Value Sets.

**Instrument participation.** EQ-5D-5L was the valuation target, an administered self-report measure, and the target of the produced value set. EQ VAS was an administered self-rating. EQ-5D-3L and the 5L crosswalk were comparison scoring routes, not administered study measures.

**Product and principal findings.** The product was a published Danish EQ-5D-5L value set. The selected model was a heteroscedastic censored hybrid model that combined cTTO and DCE. Predicted values ranged from -0.757 to 1. Anxiety/depression had the largest utility decrement. Evidence: Results, The Final Model; Abstract.

**Author interpretation and implication.** The authors described the standardized protocol, training, quality control, and population-frame support as reasons for high-quality data. They recommended the new EQ-5D-5L value set for Danish decision makers who estimate QALYs. This is a recommendation and expected use. The paper does not document later policy use or effect. Evidence: Discussion; Conclusions.

**Limits and gaps.** The recruitment source changed. Young adults and people with the lowest education remained slightly under-represented. The paper also stated that hybrid-model choice needs stronger utility-theory foundations and that DCE anchoring remains unresolved. Evidence: Discussion.

### Paper 2 — 10.1007/s11136-020-02688-y

Source: `corpus/2016170/doi_10.1007_s11136-020-02688-y.md`.

**Study family and purpose.** Systematic evidence synthesis and psychometric review. The paper aimed to summarize evidence for EQ-5D-5L measurement properties and identify gaps. Evidence: Abstract; Background.

**Component map.**

1. `P2-C1 search and selection`: MEDLINE, PsycINFO, EMBASE, and the EuroQol website were searched for publications from 2011 through January 2019. The review accepted German- and English-language studies of the official EQ-5D-5L in humans aged 18 or older. It excluded experimental 5L versions and sources that did not assess measurement properties. Two reviewers screened independently, with escalation for disagreement. Evidence: Literature search.
2. `P2-C2 extraction`: The review extracted study context, distribution, missingness, floor and ceiling results, test-retest reliability, validity types, and responsiveness. It did not treat internal consistency as relevant to EQ-5D. Reused underlying data were extracted once. Evidence: Data extraction.
3. `P2-C3 synthesis`: Random-effects models pooled full-health proportions, index means, and correlations when comparable. Heterogeneous results were summarized narratively by property, outcome level, population, and comparator. Evidence: Analysis.

**Evidence group.** The final evidence group contained 99 publications from 32 countries. It included general-population and patient studies. Musculoskeletal or orthopedic conditions and cancer were the most common condition groups. Evidence: Results.

**Instrument participation.** Official EQ-5D-5L was the evaluation target. The review focused on its descriptive system because the EQ VAS version was often unclear. Other HRQoL, clinical, functional, pain, cognition, satisfaction, and anchor measures were comparators in included studies. They were not administered by this review.

**Property findings.** Missingness and floor effects were generally not problematic. Index test-retest reliability was good, but some dimensions were unstable. The index and dimensions had moderate-to-strong relations with global health, other multi-attribute utility instruments, physical or functional health, pain, daily activities, and clinical measures. Relations with life satisfaction and cognition or communication were weak. Responsiveness evidence came from 15 heterogeneous studies and was less conclusive. Evidence: Distribution properties; Reliability; Validity; Responsiveness.

**Product and interpretation.** The product was a systematic synthesis of EQ-5D-5L psychometric evidence. The authors concluded that EQ-5D-5L was reliable and valid across many populations and settings. They did not claim equal performance for each dimension, property, population, or context. Evidence: Discussion; Conclusions.

**Limits and gaps.** The review excluded experimental versions, many application studies, and valuation-method evidence. Much evidence came from Western Europe, OECD countries, and East Asia. The authors requested more rigorous responsiveness studies, work in other regions and settings, and study of how the chosen value set affects responsiveness. Evidence: Study limitations; Discussion.

### Paper 3 — 10.1007/s11136-025-03983-2

Source: `corpus/367-RA/doi_10.1007_s11136-025-03983-2.md`.

**Study family and purpose.** Study protocol and data infrastructure, with population-health and instrument-comparison purposes. The paper described the rationale, design, and data-collection methods of EQ-DAPHNIE. It did not report the planned substantive instrument comparisons or population norms. Evidence: Abstract; Background.

**Component map.**

1. `P3-C1 pilot`: A United Kingdom pilot occurred in 2023. A 250-response soft launch in each country supported technical and data-quality checks before full launch. Evidence: Sampling Strategy; Study Timelines.
2. `P3-C2 round 1`: Cross-sectional online surveys ran from February through May 2024 in Australia, Canada, New Zealand, the United Kingdom, and the United States. Evidence: Setting and Population; Study Timelines.
3. `P3-C3 round 2`: Surveys ran from May through December 2024 in Argentina, Brazil, Chile, China, France, Germany, Japan, Mexico, the Netherlands, and Spain. Evidence: Setting and Population; Study Timelines.
4. `P3-C4 future rounds`: Further expansion to Africa, the Middle East, and East Asia was planned for 2025 and later. This is planned work, not completed evidence. Evidence: Setting and Population; Study Timelines.

**Evidence groups and sampling.** The target in each country was 4,500 completed adult responses. Participants came from Dynata online panels and completed a LimeSurvey web survey. Quotas used age, sex, income, region, urban or rural residence, and language where applicable. Enrollment within strata was first come, first served. Quotas could be relaxed after five weeks. Post-stratification weights were planned. Evidence: Country Selection and Sample Size; Sampling Strategy.

**Respondent and referent.** Respondents first described their own health. They then completed an EQ-5D-5L response-scale heterogeneity vignette for a hypothetical person called Alex, who had the respondent's age and background. Thus, the respondent stayed the same, but the referent changed from self to a hypothetical person. Evidence: EQ-5D-5L Response-Scale Heterogeneity Vignette.

**Instrument participation.** Administered measures included EQ-5D-5L and EQ VAS; selected EQ-5D-5L bolt-ons; EQ-HWB and EQ-HWB-S; PROMIS-10; ASCOT SCT4; ICECAP-A; WHO-5; OPQOL-brief for respondents aged 65 or older; PHQ-2; and GAD-2. The exact set varied by availability, burden, and country. The EQ-5D-5L and vignette had a fixed early order. Other standardized measures were randomized. Instrument recall periods and conditional administration must stay attached to each participation record. Evidence: Study Survey; Survey Features.

**Languages and adaptation.** The survey used English and translated forms in Spanish, French, Portuguese, Japanese, Simplified Chinese, Dutch, and German. Standardized measures used developer-supplied translations when available. Native speakers and local researchers reviewed the survey, and some questions changed for local context. Evidence: Study Survey.

**Product stage.** The paper supports `operational infrastructure` and `round 1 and round 2 data collected`. It does not support a completed cross-country norm set or completed instrument-performance result. Future rounds and longitudinal follow-up were proposed. Evidence: Study Timelines; Discussion.

**Limits and gaps.** Online panels can exclude people without internet access and can introduce panel-selection bias. Cultural response differences can affect cross-country comparability. The cross-sectional design cannot estimate individual change or reliability over time. The authors proposed alternative sampling, longitudinal follow-up, and repeated panels. Evidence: Limitations.

### Paper 4 — 10.1017/s0266462326103602

Source: `corpus/1505-RA/doi_10.1017_s0266462326103602.md`.

**Study family and purpose.** Cross-sectional stakeholder practice and needs survey, with an HTA implementation and policy context. The paper aimed to describe HTA practitioners' current use and views of HRQoL measurement, valuation, preference data, data quality, and research priorities. Evidence: Abstract; Introduction.

**Evidence group and role.** The evidence came from 238 individual respondents in 45 countries, 65 HTA agencies, and six regions. Respondents were agency employees, contractors, consultants, or advisers. Most had QALY-related work. Their answers were personal practitioner views, not official agency positions. Evidence: Participants; Results, Sample Characteristics; Limitations.

**Selection and administration.** The team used purposive, network-based recruitment from April 2023 through January 2024. Country recruiters invited personnel from identified HTA agencies. Eligible people completed an anonymous English Qualtrics survey. Evidence: Sampling and Recruitment Design; Participants; Survey Form.

**Survey modules.** The six sections covered utility instruments, preference-elicitation methods, health-preference data sources, data quality and appropriateness, and research priorities. Four-point frequency responses produced closed data. Open responses supplied qualitative explanations. Evidence: Survey Form.

**Instrument and method roles.** EQ-5D, SF-6D, EQ-5D-Y, EQ-HWB, bolt-ons, and other instruments were survey topics. TTO, VAS, standard gamble, DCE, best-worst scaling, and PTO were also survey topics. The paper did not administer these as health or valuation tasks to respondents.

**Analysis.** Closed responses were summarized by country and region. The analysis used a country summary and then a median across countries for frequency items. Research-priority scores were averaged first within countries and then within regions and globally. Open responses underwent translated, structured content analysis. Evidence: Statistical Analysis.

**Principal findings.** EQ-5D, SF-6D, and EQ-5D-Y were the most frequently encountered utility instruments. TTO, VAS, and standard gamble were the most frequently used elicitation methods. Foreign general-public preferences were used more often overall than local public preferences, although the pattern differed by region. Common problems were poor sample representativeness, small utility samples, mismatched evidence, and mixed instruments or methods in one model. Recent tariffs, child instruments, and combined health and social-care measurement were leading global priorities. Evidence: Results sections.

**Author interpretation and implications.** The authors linked use of foreign preferences and weak data to evidence scarcity. They called for more local and recent utility data, child-focused instruments, stakeholder involvement in instrument development, and public utility-data resources. These are reported priorities and recommendations. They are not documented changes in HTA policy. Evidence: Discussion.

**Limits.** Some countries had fewer than three respondents. The network recruitment can over-represent people familiar with EuroQol. Respondent eligibility could not be verified. The source did not preserve an agency identifier, and the study was not powered for detailed subgroup comparisons. Evidence: Discussion, limitations paragraph.

### Paper 5 — 10.1007/s11136-019-02115-x

Source: `corpus/2014160/doi_10.1007_s11136-019-02115-x.md`.

**Study family and purpose.** Multi-phase instrument development and multilingual wording development. The study aimed to make an EQ-5D-Y descriptive system with more response levels and to test 4-level and 5-level candidates for comprehension, feasibility, and preference. Evidence: Abstract; Introduction.

**Component map.**

1. `P5-C1 candidate-label generation`: Reviews of child HRQoL instruments, dictionaries, and thesauruses supplied candidate severity words. Two focus groups in each country included children aged 8-10 and 11-15. The groups elicited child-friendly language and judged candidate terms. The four countries and languages were Germany/German, Spain/Spanish, Sweden/Swedish, and United Kingdom/English. Evidence: Phase 1, Identifying a Pool of Labels.
2. `P5-C2 sorting and response scaling`: A convenience sample of 255 schoolchildren rated 7-16 labels per dimension and language. Children aged 8-10 used a five-face sorting scale. Children aged 11-15 used a VAS response-scaling task. Median, mode, spread, daily-language use, and comprehension informed selection. Evidence: Sorting and Response Scaling Interviews; Results, Phase 1.
3. `P5-C3 cognitive testing`: Germany, Spain, and Sweden tested draft EQ-5D-Y-4L and EQ-5D-Y-5L forms with healthy children and children in treatment. The United Kingdom tested only the 5L candidate and did not recruit a health-condition sample. The table reports 33, 35, 32, and 20 participants by country, for 120 total. Paraphrasing and probing assessed comprehension. Evidence: Phase 2; Results, Cognitive Interviews.
4. `P5-C4 harmonization`: Teams translated the German, Spanish, and Swedish forms into English and compared meanings with the UK form. They retained justified language-specific differences rather than require literal equivalence. Evidence: Harmonization.

**Products and rejected candidate.** The selected product was a self-report EQ-5D-Y-5L in the four study languages. UK English was proposed as the source for later translations. EQ-5D-Y-4L was a tested candidate but was not selected. The product was developed and tested for initial comprehension and feasibility. It was not yet fully psychometrically validated or valued. Evidence: Discussion; Conclusion.

**Principal findings.** Both candidates were generally understandable. Participants in Germany, Spain, and Sweden preferred the 5L form because it gave more precise response choices. The reported preferences were Germany 88%, Spain 68%, and Sweden 66%. UK participants tested only 5L. Several Spanish and UK words changed after cognitive testing. Evidence: Results, Cognitive Interviews.

**Author interpretation.** The authors stated that direct child participation, language-specific development, and staged testing were necessary. They rejected the simple insertion of two labels into the earlier 3L form. Evidence: Discussion.

**Limits and future work.** Both phases used convenience samples. Recruitment of children with health conditions was difficult. The UK and Spain had small protocol differences. Future work must compare psychometric performance with EQ-5D-Y-3L, validate more languages and conditions, develop proxy forms, and test valuation feasibility. Evidence: Discussion; Conclusion.

**Extractor uncertainty.** The abstract reports a preference range of 68-88%, but the results report Sweden at 66%. Preserve the country results and flag the abstract range as internally inconsistent.

### Paper 6 — 10.1007/s40273-022-01216-9

Source: `corpus/20191020/doi_10.1007_s40273-022-01216-9.md`.

**Study family and purpose.** EQ-5D-Y-3L valuation and value-set development, with an experimental design and model-strategy comparison. The study aimed to produce a Chinese EQ-5D-Y-3L value set under the international protocol and test whether an expanded cTTO design supported hybrid modeling better than DCE plus mapping. Evidence: Abstract; Introduction.

**Evidence groups and population roles.** Two independent adult Chinese general-public samples supplied preferences. Adults valued the health of a hypothetical 10-year-old child. Thus, the adult was the respondent, the hypothetical child was the referent, and Chinese children and adolescents were the intended instrument population. The DCE group had 1,058 respondents and the cTTO group had 418, for 1,476 total. Evidence: Experimental Design; Data Collection Procedures; Results.

**Sampling.** The study recruited from 14 provinces or cities across five geographical parts of China. Quotas covered gender, age, education, and rural or urban hukou. Recruitment used non-probability snowball and purposive methods. cTTO collection occurred in eight locations, while DCE had the wider location coverage. Evidence: Sampling Strategy and Participant Recruitment; Discussion, limitations.

**Component map.**

1. `P6-C1 DCE`: The design had 150 choice sets in ten blocks of 15. It used two-dimension overlap, level spread, and utility balance. DCE was the main source for relative dimension and level preferences. Evidence: Experimental Design.
2. `P6-C2 cTTO`: The expanded design had 28 states: ten standard protocol states and 18 orthogonal-design states. Three blocks each contained ten states, and 33333 occurred in each block. cTTO supplied QALY-scale information and enabled direct main-effects modeling. Evidence: Experimental Design.
3. `P6-C3 administration and quality`: EQ-VT supported one-to-one, face-to-face computer-assisted interviews. cTTO interviewers had two days of training, practice rounds, and protocol quality control. DCE interviewers had a two-hour online session and no equivalent DCE quality-control process. Evidence: Data Collection Procedures.
4. `P6-C4 DCE plus mapping`: A correlated mixed logit estimated latent DCE values. OLS mapping of latent values to observed cTTO values supplied the scale. Evidence: Data Analysis and Model Evaluation.
5. `P6-C5 hybrid modeling`: A heteroscedastic hybrid model jointly used DCE and cTTO. The study tested a main-effects form and a form with an `A3` term for the discontinuity at state 33333. Model selection used coefficient significance and monotonicity plus mean absolute error against observed cTTO means. Evidence: Data Analysis and Model Evaluation.

**Product and finding.** The published product was the Chinese EQ-5D-Y-3L value set. The hybrid model with the A3 term was selected. It had consistent significant coefficients, the lowest reported prediction error, and a negative prediction for 33333. The observed cTTO mean ranged from 0.924 for 11112 to -0.088 for 33333. Evidence: Value Set Modelling; Conclusion.

**Interpretation and implication.** The authors said that the larger cTTO design made better use of both evidence types and handled the large gap between 33333 and the next state. They stated that the value set can support pediatric economic evaluation in China. This is an intended use, not a documented later decision effect. Evidence: Discussion.

**Limits and future work.** cTTO covered only eight locations. The relationship between respondent and imagined child was not standardized. The authors proposed study of lag-time TTO, the 33333 gap, DCE inclusion of 33333, age effects, cultural differences, and an updated youth valuation protocol. Evidence: Discussion.

**Extractor uncertainty.** The key-points box says the sample came from four regions. The abstract says 14 regions, and Methods names 14 provinces or cities across five geographical parts. Keep the named Methods detail and flag the key-points statement as a source conflict.

### Paper 7 — 10.1007/s11136-025-04003-z

Source: `corpus/1811-RA/doi_10.1007_s11136-025-04003-z.md`.

**Study family and purpose.** Secondary psychometric analysis and response-scale comparison. The study compared frequency and severity scales for EQ-HWB pain and discomfort items and tested their distinct measurement contribution across self-reported conditions. Evidence: Abstract; Background.

**Reused evidence.** The paper reused a cross-sectional CARE-2B dyadic data set that earlier papers had described. It did not collect a new sample for this analysis. The evidence group had 504 unpaid adult caregivers and 504 linked adult care recipients. The analysis used the 1,008 individual responses and did not compare dyad agreement. Evidence: Study Design and Participants; Data Collection.

**Respondent and referent.** Caregivers and recipients each reported their own health for the analyzed pain and discomfort items. The study design linked them as dyads, but the analyzed referent was self. Clinical groups came from self-reported conditions, not verified diagnoses. Evidence: Study Design and Participants; Data Collection.

**Instrument participation.** EQ-HWB/EQ-HWB-S was the main evaluation target. Its four target items measured pain frequency, pain severity, discomfort frequency, and discomfort severity over seven days. EQ-5D-5L pain/discomfort was an administered comparator with a `today` recall period. CarerQoL, CARE-2B, and other burden measures were administered in the parent survey but were not targets in this analysis. Evidence: Measures; Data Collection.

**Method applications.** Spearman correlations tested overlap. Shannon indices tested category informativity. A graded-response IRT model estimated discrimination and thresholds across the latent trait. Ordinal logistic regression with an IRT term tested differential item functioning between frequency and severity forms. Separate ordinal logistic models tested associations with demographic factors and condition groups. Evidence: Analysis.

**Principal findings.** Pain and discomfort measures were strongly related, but the response forms were not interchangeable. Frequency scales spread information more evenly and were more sensitive at lower trait levels. Severity scales discriminated better at high intensity. Differential item functioning was material for pain but negligible for discomfort. Evidence: Abstract; Discussion.

**Author interpretation and implication.** The authors recommended both forms when a longer instrument can support them. They said a frequency form can be preferable for a short instrument because of its wider informative range. They also cautioned that one scale across conditions can preserve value-set feasibility and comparability. Evidence: Discussion; Conclusion.

**Limits and gaps.** The cross-sectional analysis cannot show causation. Conditions were self-reported. Cultural and language transfer needs replication. Recall-period effects need direct study. Evidence: Discussion.

**Extractor uncertainty.** The current paper does not clearly state the country of data collection. Affiliations and a cited parent-paper title suggest a United States context, but that is not sufficient to assign an evidence country. Keep country as `not explicit in this paper` until the linked data-source record supplies it.

### Paper 8 — 10.1007/s11136-025-04038-2

Source: `corpus/1485-RA/doi_10.1007_s11136-025-04038-2.md`.

**Study family and purpose.** Qualitative concept elicitation, conceptual-framework development, and content-validity comparison. The study developed a Chinese lay quality-of-life framework and compared it with the EQ-HWB framework. It assessed only the comprehensiveness part of content validity. Evidence: Abstract; Introduction.

**Evidence group.** Quota sampling recruited 30 people: ten healthy participants, ten patients, and ten informal caregivers. Twenty-two came from Guangzhou and eight from Harbin. Quotas covered age, gender, education, health condition, caregiver experience, and urban or rural hukou. Interviews were face to face in quiet public places from March through June 2023. Evidence: Participant Selection and Setting; Participants.

**Component map.**

1. `P8-C1 guide pilot`: Two pilot rounds with three people each tested and revised the translated interview guide. The team replaced the difficult Chinese expression for `poor well-being` with `quality of life`. Evidence: Research Team and Reflexivity; Data Collection.
2. `P8-C2 concept elicitation`: Semi-structured interviews started with open questions, asked for a 1-10 quality-of-life rating and explanation, and asked for examples of poor quality of life. The interviewer summarized the answer for participant confirmation. Evidence: Data Collection.
3. `P8-C3 coding and framework development`: Two coders used 96 EQ-HWB candidate items as a deductive starting codebook and added inductive codes. Consensus and supervisor review resolved differences. Five criteria removed codes outside the selected current, individual, holistic outcome boundary. Of 221 codes, 187 remained and formed 57 subthemes and eight themes. Evidence: Analysis; Results, QoL Framework.
4. `P8-C4 framework comparison`: The team compared the new hierarchy with the EQ-HWB conceptual framework at theme and subtheme levels. Evidence: Compare with EQ-HWB; Comparison with EQ-HWB.

**Product.** The paper produced a Chinese lay quality-of-life conceptual framework with eight themes: feeling and emotion, cognition, self-identity, coping, physical sensation, relationship, activity, and mindset. This is a paper-local analytical product. It is not a new licensed instrument or a new EQ-HWB version.

**Principal findings.** Seven of eight high-level themes aligned with EQ-HWB. `Mindset` was the additional theme. The paper also found new or differently placed subthemes and broader negative and positive meanings for autonomy. The authors judged these differences too small to defeat the comprehensiveness of EQ-HWB in this sample. Evidence: Comparison with EQ-HWB; Discussion; Conclusion.

**Interpretation boundary.** The paper supports content validity for comprehensiveness in a Chinese lay sample. It does not test the relevance or comprehensibility of the final EQ-HWB items, a measurement model, responsiveness, or utility valuation. Evidence: Introduction; Conclusion.

**Limits and future work.** Harbin participants were young, healthy, and highly educated. Patients were community-based and mainly had chronic disease. Some Chinese concepts were difficult to translate. Saturation had no preset rule and was judged subjectively. Relevance and comprehensibility were reserved for later work. Evidence: Limitation; Introduction.

**Extractor uncertainty.** The source reports `68% (18/57)` subtheme alignment. The fraction is not 68%. Do not normalize it. Keep the narrative statement that there was substantial overlap, retain both reported values in an uncertainty note, and do not use the percentage for comparison.

### Paper 9 — 10.1016/j.jval.2025.02.001

Source: `corpus/345-PHD/doi_10.1016_j.jval.2025.02.001.md`.

**Study family and purpose.** Systematic review of analysis practice in randomized clinical trials. The paper aimed to describe how trials estimated treatment effects on EQ-5D dimensions, EQ VAS, and utility. Evidence: Abstract; Introduction.

**Component map.**

1. `P9-C1 identification`: MEDLINE and EMBASE were searched from inception through 15 November 2021. ClinicalTrials.gov was searched on 16 August 2023, and linked publications were sought in PubMed. Evidence: Trial Identification.
2. `P9-C2 eligibility and trial identity`: Eligible RCTs analyzed postbaseline EQ-5D by treatment group. The review excluded QALYs and other time-plus-quality outcomes, pilot studies, reviews, abstracts, and non-English reports. Multiple publications were mapped to one trial. Evidence: Trial Eligibility; Trial Selection.
3. `P9-C3 method extraction`: The review separated EQ-5D dimension responses, utility, and EQ VAS; numerical and categorical formats; single and multiple postbaseline collections; descriptive, bivariate, multivariable, and survival methods; baseline adjustment; assumptions; and missing-data handling. Evidence: Data Extraction and Categorization.
4. `P9-C4 descriptive synthesis`: The review summarized use counts and method patterns. It did not estimate treatment effect and did not perform risk-of-bias or GRADE appraisal. Evidence: Data Synthesis; Quality Appraisal.

**Evidence group.** The final unit was 2,125 unique RCTs. Most used a parallel design. EQ-5D was usually a secondary or exploratory endpoint. Baseline EQ-5D existed in most trials, and 1,270 trials had more than one postbaseline collection. Evidence: Characteristics of the Trials.

**Instrument participation.** EQ-5D was the review target, not an instrument that the review administered. Version detail was not the main synthesis facet. Outcome-level detail was central: utility, EQ VAS, and dimension response.

**Principal findings.** Utility was analyzed most often, followed by EQ VAS; dimension responses were much less common. Fixed-effect linear models were most common for one postbaseline utility, and mixed-effect linear models were most common for repeated postbaseline utility. Only 10.8% of trials that analyzed numerical EQ-5D reported assumption checks, and 21.3% reported baseline-score adjustment. Missing EQ-5D data were explicitly assessed in 661 trials; about half of those used imputation. Multiple imputation and last observation carried forward were most common. Evidence: Statistical Methods; Missing Data.

**Author interpretation and implication.** The authors said method variation, limited assumption checks, weak baseline adjustment, and incomplete missing-data methods reduce confidence and cross-study comparability. They proposed that the review can support analysis and reporting guidance. Evidence: Discussion; Conclusion.

**Limits and gaps.** The long time window combines changing practice. Reports often had little space for secondary EQ-5D methods, so extracted baseline and missing-data practices can be undercounts. Future work must compare model performance for EQ-5D distributions and connect method choice to a prespecified estimand. Evidence: Discussion.

### Paper 10 — 10.1007/s10198-025-01770-x

Source: `corpus/218-RA/doi_10.1007_s10198-025-01770-x.md`.

**Study family and purpose.** Comparative measurement-property study. The paper compared EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D in Brazilian children and adolescents with and without self-reported musculoskeletal pain. Evidence: Abstract; Introduction.

**Evidence groups and sample flow.** The study distributed 1,760 school consent packs. It received 540 signed consents and included 356 participants. Of these, 181 met the paper's self-reported musculoskeletal-pain rule and 175 did not report pain. For the seven-day retest, 231 were classified as stable: 96 with pain and 135 without pain. Participants were aged 8-18 and attended public or private schools in urban São Paulo state. Evidence: Participants and Setting; Results; Test-Retest Reliability.

**Condition definition.** PIP-Kids classified pain from self-reported back, neck, arm, or leg pain in the prior month plus school absence or interference with usual or recreational activity. The study excluded pain attributed to specified trauma, surgery, or diagnosed conditions. This was not a clinical diagnosis. Evidence: PIP-Kids; Participants and Setting.

**Administration and timing.** Participants self-completed Brazilian-Portuguese paper forms in classrooms. Teachers and researchers could help with interpretation. Baseline administration included PIP-Kids, a numerical pain rating, the two EQ-5D-Y forms, CHU9D, and PedsQL. The order of the two EQ-5D-Y forms was randomized, but they remained consecutive. Stable participants repeated the main instruments after seven days. Evidence: Procedure.

**Instrument roles.** EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D were evaluation targets. PedsQL was a construct-validity comparator. PIP-Kids classified known groups and retest stability. The numerical pain scale classified pain intensity. The study used official Brazilian-Portuguese self-report forms. It assessed descriptive responses and EQ VAS, not utility scores. Evidence: Instruments; Data Management and Analysis.

**Property applications.**

- Feasibility used missing response and completion rates.
- Distribution used item response, full-health ceiling, and floor results.
- Test-retest reliability used Kappa for dimensions and ICC for EQ VAS.
- Measurement error used response agreement, standard error of measurement, and smallest detectable change.
- Construct validity used prespecified correlations with PedsQL and CHU9D, with a 75% hypothesis-confirmation rule.
- Known-group validity compared pain versus no pain and pain-intensity groups.

Evidence: Item Response Distribution; Measurement Properties.

**Principal findings.** The instruments were generally feasible, but EQ-5D-Y-5L usual activities had 12.7% missing data. The pain-group full-health ceiling was 18.2% for EQ-5D-Y-3L and 16.0% for EQ-5D-Y-5L. Dimension test-retest reliability was poor to moderate. EQ VAS reliability was higher in the pain group than in the no-pain group. EQ-5D-Y-3L and EQ-5D-Y-5L met the paper's construct-validity rule against PedsQL in the pain group. EQ-5D-Y-5L met it against CHU9D in both groups. All three target instruments distinguished pain from no pain. Evidence: Results; Main Findings.

**Interpretation limits.** The one-month PIP-Kids pain window differed from the `today` window of EQ-5D-Y and CHU9D. This explains why some participants classified with pain reported no pain on the study day. A failed prespecified correlation rule means that the observed results did not match the hypotheses; the authors cautioned that it does not by itself prove invalidity. Evidence: Comparison with Other Studies; Strengths and Limitations.

**Implication and gaps.** The authors supported use of the instruments, especially in Brazilian young people with musculoskeletal pain, and noted the available Brazilian EQ-5D-Y-3L value set for economic evaluation. Future work should cover other conditions and settings, children younger than eight with self or proxy forms, utility-score properties, and responsiveness. Evidence: Implications; Unanswered Questions and Future Research.

**Limits.** Pain was heterogeneous and self-reported. Feasibility did not test completion time or comprehension. Consecutive EQ-5D-Y forms can cause recall or confusion. Recall periods and response forms differed across comparators. There was no gold standard, and the study did not test Shannon informativity or responsiveness. Evidence: Strengths and Limitations.

## 4. Granularity decisions and evidence

| Decision | Why it changes retrieval or interpretation | Paper and user-question evidence |
|---|---|---|
| Keep the paper as the main record and add selective local components. | Papers 5 and 8 have phases that produce inputs for later phases. Papers 1 and 6 have separate valuation tasks and model paths. A flat record would mix samples and purposes. | Papers 1, 5, 6, 8, and 10; questions 5, 9, 12, and 13. |
| Model instrument participation, not only instrument identity. | EQ-5D-5L is administered in paper 1, a review target in paper 2, a vignette form in paper 3, and a survey topic in paper 4. A single `uses EQ-5D` flag creates false matches. | Papers 1-4 and 9; questions 3, 4, 11, 20, and 21. |
| Keep family, version, variant, language, report form, and development status separate. | EQ-5D-Y-3L and EQ-5D-Y-5L differ in papers 5, 6, and 10. Paper 5 has four language forms and a selected self-report product. Paper 3 includes experimental EQ-HWB forms and optional bolt-ons. | Papers 3, 5, 6, 7, and 10; questions 3, 4, 14, 20, and 23. |
| Separate respondent, referent, target population, and decision population. | Adults value a hypothetical child in paper 6. Paper 3 changes from self to Alex. Paper 7 has linked caregivers and recipients. Paper 1 uses adult preferences for Danish policy. | Papers 1, 3, 6, and 7; questions 6, 13, and 20. |
| Keep evidence-source type and evidence count. | A person survey, a systematic review of publications, and a review of unique trials support different inferences. Counts must refer to the correct unit. | Papers 2, 4, 7, and 9; questions 6, 8, 16, and 25. |
| Distinguish valuation task, protocol, design, and statistical model. | cTTO and DCE have different roles. EQ-VT 2.1, youth framing, lead-time TTO, health-state blocks, mapping, hybrid modeling, and model criteria can change the value set. | Papers 1 and 6; questions 9, 10, 12, 13, 20, and 21. |
| Represent a method as an application with purpose and target. | `Mixed model` can analyze repeated EQ-5D outcomes in paper 9 or combine preference data in papers 1 and 6. The name alone does not explain the inference. | Papers 1, 6, 7, 9, and 10; questions 12, 13, and 21. |
| Structure psychometric property, outcome level, comparator, subgroup, timing, and decision rule. | Index reliability differs from dimension reliability in paper 2. Frequency and severity differ by trait level in paper 7. Pain and no-pain groups differ in paper 10. | Papers 2, 7, and 10; questions 9, 12, 13, 15, 20, and 22. |
| Structure administration mode and recall period. | Face-to-face computer tasks, web surveys, paper classroom forms, and qualitative interviews are not equivalent. The one-month versus today mismatch materially affects paper 10. | Papers 1, 3, 5, 6, 8, and 10; questions 11, 13, 20, and 24. |
| Structure sample stages only when they explain evidence. | Attrition and analyzed counts matter in papers 1 and 10. Paper 9 must count unique RCTs, not publications. Full demographic tables do not need ontology fields. | Papers 1, 2, 9, and 10; questions 8, 16, 20, and 25. |
| Keep planned, experimental, developed, operational, published, and reported-in-use stages separate. | Paper 3 describes operational collection but pending analyses. Paper 5 produces an instrument that still needs validation. Papers 1 and 6 publish value sets. No paper documents later effect. | Papers 1, 3, 5, and 6; questions 14, 17, and 23. |
| Keep principal finding, interpretation, implication, limitation, documented use, and future gap separate. | Recommendations to use a value set are not actual policy effects. A paper-specific future-work statement is not a corpus gap. | All papers; questions 15-18 and 27. |
| Record reuse by object type and reuse action. | Paper 7 reanalyzes CARE-2B data. Paper 2 avoids duplicate extraction from one underlying data set. Paper 6 extends a standard protocol. These have different independence consequences. | Papers 2, 6, and 7; questions 19 and 25. |
| Keep qualitative theme hierarchies paper-local until stable reuse exists. | `Mindset` is a product finding in paper 8. It must be findable, but it is not yet a required domain of every EuroQol record. | Paper 8; questions 2, 15, 16, and 22. |
| Keep only decisive numerical results. | Model choice, sample size, task count, sample flow, and key property results aid interpretation. Full model coefficients and every pooled estimate do not answer the fixed questions better. | Papers 1, 2, 4, 6, 7, 9, and 10; purpose boundary on findings. |

## 5. Rejected distinctions and detail

1. **One exclusive study-family label.** Rejected because a paper can be both a protocol and an instrument-comparison resource, or both a psychometric study and a response-scale comparison.
2. **One broad `method` field.** Rejected because task, protocol, experimental design, statistical model, and synthesis method have different functions.
3. **One broad `validity` result.** Rejected because content, construct, convergent, and known-group validity use different evidence. The target level and subgroup also matter.
4. **A generic `uses instrument` relation.** Rejected because it merges administered measures, review targets, valuation targets, products, survey topics, and cited background instruments.
5. **Every named instrument as a study instrument.** Rejected. Literature examples and survey answer options must not appear as administered measures.
6. **Every paper section as a component.** Rejected. Components exist only when a local distinction changes retrieval or interpretation.
7. **Every participant, dyad, health state, or included study as an ontology entity.** Rejected for this paper layer. Keep group design, selected task counts, and aggregate evidence. Detailed source records can link from other layers.
8. **Every eligibility rule as a controlled term.** Rejected. Structure major population and selection facets. Keep unusual or complex rules as concise narrative.
9. **Every coefficient, confidence interval, correlation, and table cell.** Rejected. Keep decisive values and the principal direction. The paper remains the detailed source.
10. **Every qualitative code as a global concept.** Rejected. Preserve paper-local theme and subtheme hierarchies. Promote a term only after stable cross-paper use and a retrieval need are clear.
11. **Recommendation as documented impact.** Rejected. `Expected`, `recommended`, `possible`, and `documented in use` are separate states.
12. **Author-stated future work as a corpus gap.** Rejected. Corpus gaps require a later cross-corpus derivation.
13. **A detailed claim-evidence graph.** Rejected by scope. A concise outcome summary with a section source gives sufficient traceability.
14. **A fixed property taxonomy for all methods.** Rejected. Use the common core plus a study-family path. Different families need different depth.
15. **Literal cross-language equivalence as a requirement.** Rejected because paper 5 shows that comprehensible language-specific severity terms can be comparable without literal identity.

## 6. Unresolved cases for later rounds

1. **Paper 5 preference range conflict.** The abstract gives 68-88%, but the country results include Sweden at 66%. Keep the country values and the conflict note.
2. **Paper 6 location conflict.** The key-points box says four regions. The abstract says 14 regions. Methods names 14 provinces or cities in five geographical parts, with cTTO in eight locations. Keep the detailed Methods representation.
3. **Paper 7 evidence country.** The current paper does not state it clearly. Do not infer the country from affiliations or a cited parent-paper title.
4. **Paper 8 subtheme percentage.** The text gives 68% and 18/57 for the same alignment. These values do not agree. Do not calculate a replacement without source clarification.
5. **Paper 3 product maturity.** Rounds 1 and 2 have collection dates and counts, but the paper uses prospective language for later analyses and rounds. Keep infrastructure and collected data separate from unreported analytical products.
6. **Paper 4 organizational meaning.** Respondents came from 65 agencies, but answers cannot be aggregated as official agency positions. Keep the person as the evidence unit.
7. **Paper 10 validity wording.** The conclusion uses broad positive wording, but property-specific results include poor-to-moderate reliability and several failed hypothesis rules. Preserve the property-specific findings and the authors' caution that a failed hypothesis rule does not alone prove invalidity.
8. **Controlled vocabulary growth.** This batch gives strong terms for valuation, measurement properties, instrument development, qualitative content validity, reviews, population infrastructure, and stakeholder surveys. Mapping, translation-only studies, population-norm result papers, and direct implementation evaluations need later paper evidence before deeper family-specific terms are fixed.

## 7. Run note

- Lineage: A, round 1.
- Batch: `pilot/ontology-development-v2/batches/batch-01.tsv`.
- Task version: version 2, frozen 2026-08-16.
- Branch: `experiment/ontology-v2-a`.
- Base commit: `858adec5d930fdbb80af94aaa8388c476ec7f14f`.
- Agent: Codex, fresh round-1 context.
- Run time recorded: 2026-08-16 18:57:37 CEST.
- Source check: all ten article files matched the manifest SHA-256 values and byte counts.
- Mechanical note: the first local verification command used `status`, which zsh reserves as read-only. It stopped before a report was produced and changed no file. A corrected command verified all inputs.
- Storage note: the repository `.gitignore` ignores `/pilot/`. The lineage file exists in the requested path, but it is untracked and does not appear in normal `git status` output. It was not staged or committed.
- Research-input check: only the supplied version-2 purpose, questions, task, protocol, batch-01 manifest, ten assigned article files, `AGENTS.md`, and Git branch or commit identity supplied EuroQol or experiment content. System-required generic modeling guidance was also read. It contained no EuroQol, paper, or experiment content. No version-1 work, legacy extraction, graph schema, later batch, hidden probe, holdout paper, or other lineage was inspected.
