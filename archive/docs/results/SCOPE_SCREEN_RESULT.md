# Scope screen result

This file records an **operator scope screen** applied to the full-text retrieval
queue. It is a stage of the governing method
([`METHOD_SIMPLE.md`](../../../docs/METHOD.md)), not a side note, and it sits between the
abstract screen and full-text assessment:

```text
abstract screen            -> 1,679 routed to retrieval   ABSTRACT_SCREEN_RESULT.md
  operator scope screen    -> removes off-topic records    this file
    full-text retrieval    -> file obtained and verified   FULLTEXT_RETRIEVAL_RESULT.md
      full-text assessment -> eligibility decided          FULLTEXT_PREPARATION_RESULT.md
```

## Why this stage exists

[`ABSTRACT_SCREEN_RESULT.md`](ABSTRACT_SCREEN_RESULT.md) defines a deliberately
high-recall screen: it routes a publication when it *could* have EuroQol support
or be an output of a listed project, and states that retrieval is not final
inclusion. Its own validation sample found an over-routed paper and concluded
that "the full-text gate must reject such weak links".

Reading the retrieval queue showed the same failure at scale. Most over-routed
records entered on **author or PI name plus plausibility**, which cannot
establish that a paper is a project output — 344 PIs hold 1,024 grants, so a
name match yields a review pool, not an attribution. The screen's own reasons
say as much, in wording such as:

- "no concrete match to the supplied projects"
- "not a clear project-product match"
- "Author link alone is weak, but retrieval is warranted for verification"

Measured across the 1,679 routed records:

| routing basis | records |
|---|---|
| reason contains a hedge (`plausible`, `weak`, `not a clear`, `no concrete`) | 424 |
| no project id nominated at all | 217 |
| reason cites funder metadata or an acknowledgement | 416 |

Retrieving these costs institutional access effort and publisher goodwill on
papers that full-text assessment would reject anyway. This stage removes the
clearest cases before that cost is paid.

## Criterion applied

A record is excluded when an operator reads its title and judges the topic to
have no relation to EuroQol instrument work or to any listed funded project, and
the abstract screen's own reason rests on an author or name link rather than on
funding evidence.

The criterion is topical and human. It is **not** applied by code, it is not
applied to any record whose reason cites explicit funding evidence, and it is
not a substitute for full-text assessment on records that stay in the queue.

## Standing method question

[`METHOD_SIMPLE.md`](../../../docs/METHOD.md) assigns the eligibility decision to
full-text assessment: "The abstract screen does not establish eligibility" and
"The full-text assessment, not retrieval or the abstract screen, makes the
eligibility decision." An operator screen at the retrieval stage decides,
on title alone, that some records never reach that gate.

That tension is deliberate but undocumented in the governing method. **The method
file has not been changed for it.** Resolve it before the methods review, either
by adding this stage to `METHOD_SIMPLE.md` with the criterion above, or by
reclassifying these records as screen corrections rather than a new stage.

## Status when excluded

All records below were `MANUAL_REQUIRED` when excluded. None had been retrieved,
so no full text was discarded and the exclusion costs nothing to reverse: delete
the row and rerun

```sh
.venv/bin/python pipeline/run_scale_fulltext_retrieval.py \
  --execute --retry --record-id <record_id>
```

## Coverage

This is a partial pass. The operator reviewed the manual retrieval queue only,
and stopped before the end. The 424 hedged and 217 project-less records named
above have **not** been reviewed as a population; more records of this kind
remain in the queue.

## Register

Decided on 2026-08-26.

These 36 records also appear in
[`../data/fulltext-not-retrieved.csv`](../../../data/fulltext-not-retrieved.csv) with
`disposition = outside_scope`. That file is the machine-readable register of
every routed record without a full text, whatever the reason; this file holds
the criterion and the reasoning behind these particular rows.

| record_id | year | doi | title |
|---|---|---|---|
| `P94e1c2d512e0` | 2012 | 10.3109/17518423.2012.711781 | The effect of the Nintendo Wii Fit on balance control and gross motor function of children with spastic hemiplegic cerebral palsy |
| `P306cf92b0950` | 2013 | 10.3109/02770903.2013.853080 | Experiences of living with asthma – a focus group study with adolescents and parents of children with asthma |
| `P036826a75189` | 2015 | 10.2519/jospt.2015.6015 | The Incremental Effects of Manual Therapy or Booster Sessions in Addition to Exercise Therapy for Knee Osteoarthritis: A Randomized Clinical Trial |
| `Pb5b2b8080910` | 2017 | 10.1136/annrheumdis-2016-042193 | Subsequent Injury Study (SInS): Improving outcomes for injured New Zealanders. |
| `P10b5b110d6d5` | 2017 | 10.1055/s-0037-1598413 | Wirksamkeit des „Assessment of Burden of COPD“ (ABC) Instruments bezüglich gezundheitsbezogener Lebensqualität bei COPD Patienten: eine Cluster-randomisierte, kontrollierte Studie |
| `Pa9a6b5d71b39` | 2018 | 10.1089/neu.2017.5257 | Divergent Classification Methods of Post-Concussion Syndrome after Mild Traumatic Brain Injury: Prevalence Rates, Risk Factors, and Functional Outcome |
| `P9741cbbef775` | 2018 | 10.1001/jamainternmed.2018.4710 | Evaluating Progression-Free Survival as a Surrogate Outcome for Health-Related Quality of Life in Oncology |
| `Pe1bedb4b598e` | 2018 | 10.1210/jc.2018-01787 | Pre-Conception Characteristics Predict Obstetrical and Neonatal Outcomes in Women With Polycystic Ovary Syndrome |
| `P6f651b9db598` | 2019 | 10.37532/2041-6792.2019.9(2).152 | Binge eating disorder among obese/overweight in Pakistan: Under-diagnosed, undertreated and misunderstood |
| `Pb83e60aaab21` | 2019 | 10.1001/jamaneurol.2018.4561 | Prediction Tools for Psychiatric Adverse Effects After Levetiracetam Prescription |
| `Pf246baab0a8f` | 2019 | 10.7454/msk.v23i1.10147 | Quality of Life of Primary Brain Tumor Patients Before and 3 Months After Discharge from a Hospital in Bandung, Indonesia |
| `P7db87ac9c8a9` | 2019 | 10.1183/13993003.01568-2018 | Surgery or radiotherapy for stage I lung cancer? An intention-to-treat analysis. |
| `Pf766fd75ca35` | 2019 | 10.1089/neu.2019.6764 | Toward a New Multi-Dimensional Classification of Traumatic Brain Injury: A Collaborative European NeuroTrauma Effectiveness Research for Traumatic Brain Injury Study |
| `Pc9504a7a0426` | 2019 | 10.1302/0301-620x.101b11.bjj-2019-0515.r1 | Underarm bracing for adolescent idiopathic scoliosis leads to flatback deformity |
| `Pb2df4df860c6` | 2020 | 10.1515/sjpain-2020-0050 | A cost-utility analysis of multimodal pain rehabilitation in primary healthcare |
| `P5fb9fbe8e76a` | 2020 | 10.1302/0301-620x.102b7.bjj-2019-1766.r2 | Comparative study of the use of Paediatric Quality Of Life Inventory 4.0 generic core scales in paediatric patients with spine and limb pathologies |
| `P634a9fe45d3a` | 2020 | 10.1089/neu.2020.7228 | Differences between Men and Women in Treatment and Outcome after Traumatic Brain Injury |
| `Pd008a92c93d4` | 2020 | 10.21037/aol-20-21 | Effectiveness and safety of pembrolizumab as bridging to hematopoietic stem cell transplantation in relapsed and refractory classical Hodgkin’s lymphoma: a retrospective observational study |
| `P4fb1c805bd41` | 2020 | 10.26452/ijrps.v11i3.2421 | Evaluation of prescribing pattern at basic health care facilities of Islamabad Pakistan |
| `Pc5d8eaabeac4` | 2020 | 10.37532/2041-6792.2020.10(3).170 | Healthy Behaviours and Depression among Overweight and Obese: A Social Taboo in Pakistan |
| `P91799ae88e45` | 2020 | 10.5588/ijtld.19.0652 | Modeling the likely economic cost of non-adherence to TB medicines in the Philippines |
| `P94e87d3717fb` | 2020 | 10.1136/oemed-2020-106597 | Predictors of subsequent injury at work: findings from a prospective cohort of injured workers in New Zealand. |
| `Pb7ffb9b71f03` | 2021 | 10.1017/s0266462321000647 | A framework for action to improve patient and public involvement in health technology assessment. |
| `P379c6813a76b` | 2021 | 10.7196/samj.2021.v111i5.15351 | HIV care coverage among HIV-positive adolescent girls and young women in South Africa: Results from the HERStory Study |
| `Pf0bb1572b33a` | 2021 | 10.1002/14651858.cd014428 | Telerehabilitation for neck pain |
| `Pabd5b13f0afe` | 2021 | 10.5694/mja2.51242 | What price quality in aged care? Findings from a national survey of more than 6500 income taxpayers. |
| `P2a7c7f3a1b36` | 2022 | 10.2337/db22-1152-p | 1152-P: Achieving Diabetic Management Targets in People with Type 1 Diabetes |
| `Pb1aa8a43bd54` | 2022 | 10.2215/cjn.05940522 | How the Routine Use of Patient-Reported Outcome Measures for Hemodialysis Care Influences Patient-Clinician Communication |
| `P1f0f736b19f1` | 2022 | 10.1017/s0266462322002203 | PP93 The Impact Of Using Different EQ-5D Scoring Methods On Cost-Utility Outcomes: A Simulation Study |
| `Pf03b949976d8` | 2022 | 10.1056/evidoa2200105 | Parenteral Vitamin C in Patients with Severe Infection: A Systematic Review |
| `P4a3c6ae9b8ac` | 2022 | 10.2106/jbjs.21.00597 | The Effect of Patient Age and Surgical Appropriateness and Their Influence on Surgeon Recommendations for Primary TKA: A Cross-Sectional Study of 2,037 Patients. |
| `P8e9ebb761be3` | 2022 | 10.23889/ijpds.v7i3.1862 | The Registry of Senior Australians: Informing Aged Care Policy Reforms. |
| `P4995de2db688` | 2022 | 10.3233/jad-220219 | Understanding the Quality of Life Impacts of Providing Informal Care to People with Dementia: A Systematic Review of Qualitative Studies |
| `Pd0ad756e0694` | 2023 | 10.1017/ice.2023.126 | Estimating the cost of inappropriate antibiotic prophylaxis prior to dental procedures. |
| `P85b7b883cf1c` | 2023 | 10.1155/2023/5839776 | Measuring Quality of Life in Residential Aged Care Using the EQ-5D-5L: A Cross-Sectional Study on the Impact of Cognition Level and Proxy Perspective on Interrater Agreement |
| `P25f89e60f0c5` | 2023 | 10.1542/hpeds.2023-007332 | Patient and Family Experience With Discharge Directly Home From the Pediatric ICU |

## Related

- [`METHOD_SIMPLE.md`](../../../docs/METHOD.md) — governing method and fixed evidence rules
- [`ABSTRACT_SCREEN_RESULT.md`](ABSTRACT_SCREEN_RESULT.md) — the screen that produced the queue
- [`FULLTEXT_RETRIEVAL_RESULT.md`](FULLTEXT_RETRIEVAL_RESULT.md) — retrieval status
- [`MANUAL_FULLTEXT_DOWNLOAD.md`](../../../pipeline/MANUAL_FULLTEXT_DOWNLOAD.md) — the queue this screen was applied to
- [`PROVENANCE.md`](../../../docs/PROVENANCE.md) — evidence and audit trail
- [`../LOG.md`](../../LOG.md) — chronological record
