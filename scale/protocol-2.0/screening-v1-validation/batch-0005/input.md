# EuroQol title and abstract screen scale v1

## Purpose

You are screening journal articles for an impact study of research funded by the
EuroQol Research Foundation.

The input corpus contains publications by verified funded-project leaders and
EuroQol members. A linked person is retrieval provenance only. It is not evidence
that an article is relevant or funded.

This is a recall-focused title and abstract screen. Its purpose is to remove articles
that are clearly outside EuroQol measurement and valuation research before full-text
retrieval. A later stage will assess full text, funding evidence, and project links.
Do not infer funding or match an article to a project.

## Central-object test

Retain an article only when at least one of these statements is true:

1. An EQ instrument or EuroQol method is a primary object of the research. Examples
   include development, valuation, value sets, descriptive systems, bolt-ons,
   psychometrics, translations, mapping, comparisons, population norms, and
   implementation research about the instrument itself.
2. Health or wellbeing measurement is the primary object of the research. The work
   develops or evaluates an instrument, descriptive system, preference-based score,
   mapping method, or other measurement method that could require a EuroQol funding
   check at full text.
3. Health-state valuation is the primary object of the research. The work develops,
   evaluates, or compares TTO, standard-gamble, DCE, utility-elicitation, value-set,
   or QALY methods rather than merely using their outputs.

The central object is what the article tries to learn or change. A measure that is
only used to learn about a disease, treatment, service, population, or policy is not
the central object.

## Exclusion rules

Exclude the article when any of these statements describes its main contribution:

- It reports clinical outcomes, disease burden, population differences, or treatment
  effects. EQ, HRQoL, QoL, a PROM, or a utility is only an outcome or covariate.
- It is a cost-effectiveness, cost-utility, budget-impact, reimbursement, resource-use,
  or policy study. Utilities or QALYs are only model inputs or results.
- It uses a DCE, willingness-to-pay task, or other preference method to study treatment,
  service, product, or policy preferences. It does not study measurement or
  health-state valuation.
- It evaluates a generic statistical or econometric method without a direct health
  measurement or health-state valuation purpose.
- It is about patient experience, satisfaction, decision-making, or shared decisions
  without developing or evaluating a health measurement instrument.
- It is clinically, economically, or topically unrelated to measurement and valuation.
- The record shows an ineligible format such as a conference abstract, editorial,
  letter, protocol-only conference item, correction, or retraction.

Mere mention or use of EQ-5D, EuroQol, HRQoL, QoL, a PROM, a utility, a QALY, a DCE,
TTO, mapping, validation, or preference is insufficient. Judge the aim and methods,
not keywords.

## Boundary rules

- Absence of `EuroQol` or `EQ-5D` is not by itself a reason to exclude an article.
- A non-EQ instrument-development or measurement-method article can qualify only when
  measurement is the central research contribution.
- A TTO or DCE article can qualify only when it values health states or studies the
  valuation method. Treatment and service preferences do not qualify.
- A QALY article can qualify when it studies the QALY concept or method. An economic
  evaluation that only calculates QALYs does not qualify.
- If the supplied abstract leaves genuine uncertainty about the central object, retain
  the article for full-text review.
- If the supplied text is not a usable article abstract, exclude it with E5. Examples include an author list, citation list, database placeholder, publisher boilerplate, or incomplete fragment. Do not infer relevance from the title alone.
- Use only the supplied metadata. Do not search the web or inspect other files.

## Decision codes

Start every reason with exactly one code:

- `[R1]`: An EQ instrument or EuroQol method is the primary research object.
- `[R2]`: Health measurement or health-state valuation is the primary research object.
- `[RU]`: The abstract is genuinely ambiguous, so full text is necessary.
- `[E1]`: EQ, HRQoL, QoL, a PROM, or a utility is only an outcome or covariate.
- `[E2]`: Utilities or QALYs are only inputs or results in an economic or policy study.
- `[E3]`: A DCE or preference method concerns a treatment, service, product, or policy.
- `[E4]`: The article is clinical, economic, statistical, or otherwise outside scope.
- `[E5]`: The publication format or supplied abstract field is ineligible.

Use `retain` with R1, R2, or RU. Use `exclude` with E1, E2, E3, E4, or E5.

## Boundary examples

- Retain `[R1]`: A study derives an EQ-5D-5L value set with TTO data.
- Retain `[R1]`: A study maps a cancer measure to EQ-5D utilities.
- Retain `[R1]`: A study tests responsiveness or content validity of EQ-HWB.
- Retain `[R2]`: A study develops a preference-based measure and its scoring system.
- Retain `[R2]`: A study compares TTO and DCE methods for valuing health states.
- Exclude `[E1]`: A cancer cohort compares EQ-5D scores between patient groups.
- Exclude `[E2]`: A treatment model reports cost per QALY with published utilities.
- Exclude `[E3]`: A DCE elicits preferred attributes of a clinical service.
- Exclude `[E4]`: A simulation studies mixed-logit estimation without a health-state
  valuation or measurement application.
- Exclude `[E4]`: A paper discusses reimbursement policy without studying a health
  measure or valuation method.

## Submission tool

The only task tool is:

`./submit_screening RECORD_ID retain|exclude "[CODE] SHORT EVIDENCE-BASED REASON"`

Call it exactly once for every supplied record. Each reason must be one concise
record-specific sentence of at most 240 characters. After all records are submitted,
run `./submit_screening status` and finish.


# Batch records

## P4516ff9b63f6

- Year: 2006
- Linked people: Ben Van Hout
- Title: Cost-effectiveness of the unrestricted use of sirolimus-eluting stents vs. bare metal stents at 1 and 2-year follow-up: results from the RESEARCH Registry

Abstract:

Aims To assess the cost-effectiveness of sirolimus-eluting stents (SESs) compared with bare metal stents (BMSs) as the default strategy in unselected patients treated in the Rapamycin Eluting Stent Evaluated At Rotterdam Cardiology Hospital (RESEARCH) Registry at 1 and 2-years following the procedure. Methods and results A total of 508 consecutive patients with de novo lesions exclusively treated with SES were compared with 450 patients treated with BMS from the immediate preceding period. Resource use and costs of the index procedure, and clinical outcomes were prospectively recorded over a 2-year follow-up period. Follow-up costs were measured as unit costs per patient based on the incidence of clinically driven target vessel revascularization (TVR), to obtain cumulative costs at 1 and 2-years. Cost-effectiveness was measured as the incremental cost-effectiveness ratio (ICER) per TVR avoided. The use of SES cost euro 3,036 more per patient at the index procedure, driven by the price of SES. Follow-up costs after 1-year were euro 1,089 less with SES when compared with BMS, due to less TVR, resulting in a net excess cost of euro 1,968 per patient in the SES group, and reduced by a further euro 100 per patient in the second year. The incidence of death or myocardial infarction between groups was similar at 1 and 2 years. Rates of TVR in the SES and BMS groups were 3.7% vs. 10.4%, P Conclusion The use of SES, while significantly beneficial in reducing the need for repeat revascularization, was more expensive and not cost-effective in the RESEARCH registry at either 1 or 2-years when compared with BMS. On the basis of these results, in an unselected population with 1 year of follow-up, the unit price of SES would have to be euro 1,023 in order to be cost-neutral.

## P21f5d5b086b5

- Year: 2021
- Linked people: Margreet Franken
- Title: Early discontinuation of PD-1 blockade upon achieving a complete or partial response in patients with advanced melanoma: the multicentre prospective Safe Stop trial.

Abstract:

BACKGROUND: The introduction of programmed cell death protein 1 (PD-1) blockers (i.e. nivolumab and pembrolizumab) has significantly improved the prognosis of patients with advanced melanoma. However, the long treatment duration (i.e. two years or longer) has a high impact on patients and healthcare systems in terms of (severe) toxicity, health-related quality of life (HRQoL), resource use, and healthcare costs. While durable tumour responses have been observed and PD-1 blockade is discontinued on an individual basis, no consensus has been reached on the optimal treatment duration. The objective of the Safe Stop trial is to evaluate whether early discontinuation of first-line PD-1 blockade is safe in patients with advanced and metastatic melanoma who achieve a radiological response. METHODS: The Safe Stop trial is a nationwide, multicentre, prospective, single-arm, interventional study in the Netherlands. A total of 200 patients with advanced and metastatic cutaneous melanoma and a confirmed complete response (CR) or partial response (PR) according to response evaluation criteria in solid tumours (RECIST) v1.1 will be included to early discontinue first-line monotherapy with nivolumab or pembrolizumab. The primary objective is the rate of ongoing responses at 24 months after discontinuation of PD-1 blockade. Secondary objectives include best overall and duration of response, need and outcome of rechallenge with PD-1 blockade, and changes in (serious) adverse events and HRQoL. The impact of treatment discontinuation on healthcare resource use, productivity losses, and hours of informal care will also be assessed. Results will be compared to those from patients with CR or PR who completed 24 months of treatment with PD-1 blockade and had an ongoing response at treatment discontinuation. It is hypothesised that it is safe to early stop first-line nivolumab or pembrolizumab at confirmed tumour response while improving HRQoL and reducing costs. DISCUSSION: From a patient, healthcare, and economic perspective, shorter treatment duration is preferred and overtreatment should be prevented. If early discontinuation of first-line PD-1 blockade appears to be safe, early discontinuation of PD-1 blockade may be implemented as the standard of care in a selected group of patients. TRIAL REGISTRATION: The Safe Stop trial has been registered in the Netherlands Trial Register (NTR), Trial NL7293 (old NTR ID: 7502), https://www.trialregister.nl/trial/7293 . Date of registration September 30, 2018.

## P8113220293c0

- Year: 2018
- Linked people: Philip Powell
- Title: Individual differences in emotion regulation moderate the associations between empathy and affective distress

Abstract:

Individual differences in empathy can have positive and negative psychological outcomes. Yet, individual differences in the processing and regulation of empathy-induced emotion have not been fully explored within this dynamic. This study was designed to explore whether individual differences in emotion regulation strategies moderated the effects of empathy on common forms of affective distress. Eight hundred and forty four participants completed survey measures of trait empathy, emotion regulation strategies, and symptoms of depression, anxiety, and stress. Affective empathy typically predicted greater affective distress, but the effects on depression and anxiety were offset when people were effective at reappraising their emotions. Cognitive empathy predicted lower distress on average, but this beneficial effect on anxiety and stress was absent in those who typically suppressed their emotions. Finally, suppression unexpectedly reduced the depression and stress reported for people high in affective empathy. Individual differences in emotion regulation are an important moderator between empathy and psychological health, and thus a useful target for intervention.

## Pb11b3b47ee24

- Year: 2024
- Linked people: Margreet Franken
- Title: Relationship between Sleep Bruxism Determined by Non-Instrumental and Instrumental Approaches and Psychometric Variables.

Abstract:

Sleep bruxism (SB) can be determined with different diagnostic procedures. The relationship between psychometric variables and SB varies depending on the diagnostic method. The aim of the study was to compare the association between SB and oral health-related quality of life (OHRQoL; measured by the Oral Health Impact Profile, OHIP), anxiety (measured by the State-Trait anxiety inventory, STAI), and stress (single scale variable) depending on the diagnostic method in the same sample. N = 45 participants were examined by non-instrumental (possible/probable SB) and instrumental methods (definite SB). The OHIP differed significantly between possible SB (median = 4) and non-SB (median = 0) with W = 115, p = 0.01, and probable SB (median = 6) and non-SB (median = 0) with W = 101, p = 0.01). There was no significant difference in the OHIP score between definite SB and non-SB. For the other psychometric variables, the analyses revealed no significant differences between SB and non-SB in all diagnostic procedures. The results suggest that there is a difference between possible/probable and definite SB with respect to the association with OHRQoL. Certain aspects of possible/probable SB might be responsible for the poor OHRQoL, which are not measured in definite SB.

## P5193b8ead600

- Year: 2023
- Linked people: Nyantara Wickramasekera
- Title: Can electronic assessment tools improve the process of shared decision-making? A systematic review

Abstract:

BACKGROUND: Patient involvement in decision-making plays a prominent role in improving the quality of healthcare. Despite this, shared decision-making is not routinely implemented. However, electronic assessment tools that capture patients' history, symptoms, opinions and values prior to their medical appointment are used by healthcare professionals during patient consultations to facilitate shared decision-making. OBJECTIVE: To assess the effectiveness of electronic assessment tools to improve the shared decision-making process. METHOD: A systematic review was conducted following PRISMA guidelines. Published literature was searched on MEDLINE, EMBASE and PsycINFO to identify potentially relevant studies. Data were extracted and analysed narratively. RESULTS: Seventeen articles, representing 4004 participants, were included in this review. The main findings were significant improvement in patient-provider communication and provider management of patient condition in the intervention group compared to the control group. In contrast, patient-provider satisfaction and time efficiency were assessed by relatively few included studies, and the effects of these outcomes were inconclusive. CONCLUSION: This review found that communication and healthcare professional's management of a patient's condition improves because of the use of electronic questionnaires. This is encouraging because the process of shared decision-making is reliant on high-quality communication between healthcare professionals and patients. IMPLICATIONS: We found that this intervention is especially important for people with chronic diseases, as they need to establish a long-term relationship with their healthcare provider and agree to a treatment plan that aligns with their values. More rigorous research with validated instruments is required.

## P39548ebd9f63

- Year: 2018
- Linked people: Ben Van Hout
- Title: P1699Characteristics of patients prescribed Evolocumab in Europe. Does clinical use match clinical guidelines?

Abstract:

Background: Randomized trials have studied evolocumab in patients at high/very high cardiovascular (CV) risk with an average LDL-C of 2.4 mmol/L (92 mg/dl) despite maximally tolerated statins. In contrast, the 2016 ESC/EAS guidelines recommend PCSK9 inhibitors (PCSK9i) be considered for patients with clinical atherosclerotic CV disease (ASCVD) and LDL-C >3.6 mmol/L despite maximum tolerated statins, or >2.6 mmol/L where there is rapid progression of CVD. Purpose: This interim analysis of an observational study describes a cohort of patients initiating evolocumab in clinical practice across Europe. Methods: Patients are followed from initiation of evolocumab (i.e. baseline); demographic/clinical characteristics, lipid modifying medication(s) and lipid values are collected from routine medical records (6 months prior to evolocumab initiation through 12 months post initiation). We report data from patients initiating evolocumab from August 2015 with follow-up through October 2017, across 10 EU countries. Results: 476 patients initiating evolocumab were included in this interim analysis (median follow-up, 3.1 months). Mean (SD) age was 60.8 (11.2) years; 89% of patients had a history of CV disease (CVD), 46% had a diagnosis of familial hypercholesterolemia (FH), 21% had diabetes, 67% were hypertensive, 10% had renal impairment and half were prior or current smokers. Approximately two-thirds (63%) of patients reported statin intolerance; 40% were receiving ezetimibe. Of the 216 patients receiving statins at baseline, more than 90% were on a moderate/high intensity (22%, moderate; 69%, high intensity). Mean (SE) baseline lipids were: LDL-C, 4.19 (1.62) mmol/L; total cholesterol, 6.26 (1.89) mmol/L; HDL-C, 1.32 (0.37) mmol/L; triglycerides, 2.11 (1.99) mmol/L. Use of evolocumab resulted in LDL-C reductions which were maintained over time (Figure). In general, statin use remained stable with no clear patterns of withdrawals or changes (data not shown). The most common evolocumab regimen (95%) was 140mg subcutaneous every 2 weeks. Seventeen (3.6%) patients reported at least one Adverse Drug Reaction (ADR); no serious ADRs were reported. Four patients discontinued evolocumab due to an ADR (arthralgia, nasopharyngitis and cognitive disorder reported by one patient each; one patient reported multiple ADRs of arthralgia, vertigo and type 2 diabetes mellitus).
