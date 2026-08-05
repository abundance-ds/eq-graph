# Author profile QA v1

## Purpose

Decide whether each supplied OpenAlex profile belongs to the named EuroQol researcher.
Use only the supplied names, affiliations, projects, topics, coauthors, and work examples.
Do not search the web or inspect other files.

Choose one decision:

- `accept`: The name and research record form one coherent identity that is consistent
  with the supplied EuroQol person evidence.
- `hold`: The profile is the wrong person, is mixed, is ambiguous, or lacks enough
  evidence for safe inclusion.

Use `hold` when the given name is incompatible, the field is unrelated, or the profile
contains substantial name-collision contamination. A broad clinical portfolio is not by
itself contamination when the field, affiliations, and coauthors remain coherent.

The only task tool is:

`./submit_profile "PERSON_NAME" DECISION "REASON"`

Call it once for every supplied person. The reason must be factual, record-specific, and
no more than 400 characters. Then run `./submit_profile status` and finish.


# Profiles

Assess all 5 people.

[
  {
    "name": "Carlos Wong",
    "member_affiliation": "London School Hygiene & Tropical Medicine",
    "is_member": true,
    "projects": [
      {
        "project_id": "2012030",
        "title": "EQ-5D-5L valuation study in Hong Kong",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014050",
        "title": "Hong Kong participation BTD-WTD split experiment",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180530",
        "title": "Agreement between proxy EQ‐5D‐Y and self‐reported EQ‐5D‐Y in a paediatric patient group",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "20190250",
        "title": "Psychometric testing of proxy EQ-5D-5L-Y in caregivers of paediatric patients with idiopathic scoliosis",
        "working_group": "Youth"
      },
      {
        "project_id": "2421-RA",
        "title": "Psychometric performance of interviewer-administered EQ‑5D‑Y‑5L in comparison with EQ‑5D‑Y‑3L in orthopaedic paediatric patients aged 6-10 years",
        "working_group": "Youth"
      },
      {
        "project_id": "333-RA",
        "title": "Psychometric properties of EQ-5D-5L for use in patients with autoimmune Graves’ disease",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5041610413",
      "display_name": "Carlos King Ho Wong",
      "orcid": "0000-0002-6895-6071",
      "reported_affiliation": "University of Leicester",
      "works_count": 485,
      "top_topics": [
        {
          "topic": "SARS-CoV-2 and COVID-19 Research",
          "works": 82
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 65
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 44
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 43
        },
        {
          "topic": "Diabetes, Cardiovascular Risks, and Lipoproteins",
          "works": 36
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 34
        },
        {
          "topic": "Thyroid Cancer Diagnosis and Treatment",
          "works": 30
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 30
        },
        {
          "topic": "Thyroid and Parathyroid Surgery",
          "works": 24
        },
        {
          "topic": "Long-Term Effects of COVID-19",
          "works": 22
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 21
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 19
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Eric Yuk Fai Wan",
          "works": 125
        },
        {
          "name": "Cindy Lo Kuen Lam",
          "works": 125
        },
        {
          "name": "Ian Chi Kei Wong",
          "works": 91
        },
        {
          "name": "Esther W. Chan",
          "works": 88
        },
        {
          "name": "Xue Li",
          "works": 83
        },
        {
          "name": "Francisco Tsz Tsun Lai",
          "works": 81
        },
        {
          "name": "Celine Sze Ling Chui",
          "works": 79
        },
        {
          "name": "Ivan Chi Ho Au",
          "works": 53
        },
        {
          "name": "Brian Hung‐Hin Lang",
          "works": 44
        },
        {
          "name": "Eric Ho Man Tang",
          "works": 43
        },
        {
          "name": "Esther Yee Tak Yu",
          "works": 42
        },
        {
          "name": "Vincent Ka Chun Yan",
          "works": 41
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167958771",
          "year": 2026,
          "title": "Automated Disease Activity Assessment in Systemic Lupus Erythematosus Using Privacy-Preserving Large Language Models",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Systemic Lupus Erythematosus Research",
            "Machine Learning in Healthcare",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W7162498249",
          "year": 2026,
          "title": "FRI-230 Impact of palliative care on end-of-life healthcare utilization among Asian patients with hepatocellular carcinoma",
          "type": "conference-abstract",
          "venue": "Journal of Hepatology",
          "cited_by_count": 0,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Economic and Financial Impacts of Cancer",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W7170137461",
          "year": 2026,
          "title": "Pembrolizumab in advanced acral lentiginous melanoma: final results of a single-centre, open-label, phase II trial in an East Asian population",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Cutaneous Melanoma Detection and Management",
            "Melanoma and MAPK Pathways",
            "Cancer Immunotherapy and Biomarkers"
          ]
        },
        {
          "openalex_id": "W7164903781",
          "year": 2026,
          "title": "Self-administered acupressure training for depression in community-dwelling individuals: a randomized controlled trial and cost-effectiveness analysis",
          "type": "article",
          "venue": "EClinicalMedicine",
          "cited_by_count": 0,
          "topics": [
            "Acupuncture Treatment Research Studies",
            "Mindfulness and Compassion Interventions",
            "Pain Management and Placebo Effect"
          ]
        },
        {
          "openalex_id": "W7162492411",
          "year": 2026,
          "title": "THU-364 Intensive care admission patterns and outcomes in hepatocellular carcinoma patients on systemic therapy",
          "type": "conference-abstract",
          "venue": "Journal of Hepatology",
          "cited_by_count": 0,
          "topics": [
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Sepsis Diagnosis and Treatment",
            "Liver Disease and Transplantation"
          ]
        },
        {
          "openalex_id": "W7164914313",
          "year": 2026,
          "title": "Type 2 Diabetes Is Associated With Increased Complications and Mortality After Hip Fracture in Older Adults Aged 60 Years or Older",
          "type": "article",
          "venue": "Diabetes Obesity and Metabolism",
          "cited_by_count": 0,
          "topics": [
            "Hip and Femur Fractures",
            "Bone health and osteoporosis research",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients"
          ]
        },
        {
          "openalex_id": "W3183875574",
          "year": 1985,
          "title": "Tracoma en una comunidad Shipiba de la selva del Perú",
          "type": "article",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "Public Health and Social Inequalities"
          ]
        },
        {
          "openalex_id": "W3217125570",
          "year": 1986,
          "title": "Afecciones oculares y causas de ceguera en la selva peruana",
          "type": "article",
          "venue": "",
          "cited_by_count": 2,
          "topics": [
            "Psychedelics and Drug Studies",
            "Historical and Scientific Studies"
          ]
        },
        {
          "openalex_id": "W2071255385",
          "year": 1988,
          "title": "The Rutter Parent Scale A2 and Teacher Scale B2 in Chinese",
          "type": "article",
          "venue": "Acta Psychiatrica Scandinavica",
          "cited_by_count": 17,
          "topics": [
            "Reliability and Agreement in Measurement",
            "Respiratory viral infections research",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        },
        {
          "openalex_id": "W1988004746",
          "year": 1988,
          "title": "The Rutter Parent Scale A2 and Teacher Scale B2 in Chinese II. Clinical validity among Chinese children",
          "type": "article",
          "venue": "Acta Psychiatrica Scandinavica",
          "cited_by_count": 27,
          "topics": [
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        },
        {
          "openalex_id": "W4303423758",
          "year": 2022,
          "title": "Real-world effectiveness of molnupiravir and nirmatrelvir plus ritonavir against mortality, hospitalisation, and in-hospital outcomes among community-dwelling, ambulatory patients with confirmed SARS-CoV-2 infection during the omicron wave in Hong Kong: an observational study",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 304,
          "topics": [
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 Clinical Research Studies",
            "SARS-CoV-2 detection and testing"
          ]
        },
        {
          "openalex_id": "W4293280590",
          "year": 2022,
          "title": "Real-world effectiveness of early molnupiravir or nirmatrelvir–ritonavir in hospitalised patients with COVID-19 without supplemental oxygen requirement on admission during Hong Kong's omicron BA.2 wave: a retrospective cohort study",
          "type": "article",
          "venue": "The Lancet Infectious Diseases",
          "cited_by_count": 273,
          "topics": [
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 Clinical Research Studies",
            "SARS-CoV-2 detection and testing"
          ]
        },
        {
          "openalex_id": "W1668227175",
          "year": 2015,
          "title": "The Psychometric Properties of the Center for Epidemiologic Studies Depression Scale in Chinese Primary Care Patients: Factor Structure, Construct Validity, Reliability, Sensitivity and Responsiveness",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 237,
          "topics": [
            "Mental Health Treatment and Access",
            "Treatment of Major Depression",
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes"
          ]
        },
        {
          "openalex_id": "W2807736175",
          "year": 2018,
          "title": "Saliva as a diagnostic specimen for testing respiratory virus by a point-of-care molecular assay: a diagnostic validity study",
          "type": "article",
          "venue": "Clinical Microbiology and Infection",
          "cited_by_count": 229,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "Respiratory viral infections research",
            "Dental Research and COVID-19"
          ]
        },
        {
          "openalex_id": "W4316014100",
          "year": 2023,
          "title": "Estimating the transmission dynamics of SARS-CoV-2 Omicron BF.7 in Beijing after adjustment of the zero-COVID policy in November–December 2022",
          "type": "article",
          "venue": "Nature Medicine",
          "cited_by_count": 175,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 epidemiological studies"
          ]
        },
        {
          "openalex_id": "W4385871686",
          "year": 2023,
          "title": "Risk of autoimmune diseases following COVID-19 and the potential protective effect from vaccination: a population-based cohort study",
          "type": "article",
          "venue": "EClinicalMedicine",
          "cited_by_count": 158,
          "topics": [
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 Clinical Research Studies",
            "Spondyloarthritis Studies and Treatments"
          ]
        },
        {
          "openalex_id": "W2564998229",
          "year": 2016,
          "title": "Systematic review and meta-analysis on intra-operative neuro-monitoring in high-risk thyroidectomy",
          "type": "review",
          "venue": "International Journal of Surgery",
          "cited_by_count": 150,
          "topics": [
            "Thyroid and Parathyroid Surgery",
            "Intraoperative Neuromonitoring and Anesthetic Effects",
            "Anesthesia and Pain Management"
          ]
        },
        {
          "openalex_id": "W4317480700",
          "year": 2023,
          "title": "Association of COVID-19 with short- and long-term risk of cardiovascular disease and mortality: a prospective cohort in UK Biobank",
          "type": "article",
          "venue": "Cardiovascular Research",
          "cited_by_count": 133,
          "topics": [
            "COVID-19 Clinical Research Studies",
            "COVID-19 and healthcare impacts",
            "Long-Term Effects of COVID-19"
          ]
        }
      ]
    }
  },
  {
    "name": "Cate Bailey",
    "member_affiliation": "University of Melbourne",
    "is_member": true,
    "projects": [
      {
        "project_id": "1559-RA",
        "title": "Testing the validity of the EQ-HWB-s in caregivers of children with health conditions",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1566-RA",
        "title": "Examining the psychometric performance of the EQ-HWB in caregivers of persons living with dementia.",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1772-RA",
        "title": "The psychometric performance of the EQ-HWB-S in two Nationally Representative Samples - Australia and New Zealand",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1872-RA",
        "title": "Testing the validity and responsiveness to change of the EQ-HWB-S in a 4-week online study evaluating the effects of mindfulness training for meditation app users with a range of mental health statuses; The Medito Study.",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2032-RA",
        "title": "Investigating validity and responsiveness to change of the EQ-HWB-S in a sample of people living with dementia with mild cognitive decline; the I-CHARD study",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2096-RA",
        "title": "Understanding the effects of preference-weights on the psychometric performance of the EQ-HWB short form through comparing sum- and preference-based scores.",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2439-RA",
        "title": "Testing the validity and responsiveness to change of the EQ-HWB-9 in a population of young adults with chronic health conditions transitioning from paediatric to adult medical care - the Transition Compass Trial. ",
        "working_group": "Youth, EQ-HWB"
      },
      {
        "project_id": "2440-RA",
        "title": "Comparing the performance of the modified and experimental versions of the EQ-HWB Hopelessness item; a psychometric study using IRT and DIF using data from the Meditation Engagement Study ",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "295-RA",
        "title": "The feasibility, acceptability and validity of the EQ-HWB for use in a hard-to-reach population of carers of children experiencing adversity.",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5020867003",
      "display_name": "Cate Bailey",
      "orcid": "0000-0001-5030-430X",
      "reported_affiliation": "The University of Melbourne",
      "works_count": 88,
      "top_topics": [
        {
          "topic": "Maternal Mental Health During Pregnancy and Postpartum",
          "works": 19
        },
        {
          "topic": "Gestational Diabetes Research and Management",
          "works": 17
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 17
        },
        {
          "topic": "Breastfeeding Practices and Influences",
          "works": 9
        },
        {
          "topic": "Child Abuse and Trauma",
          "works": 8
        },
        {
          "topic": "Birth, Development, and Health",
          "works": 7
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 6
        },
        {
          "topic": "Indigenous Health, Education, and Rights",
          "works": 6
        },
        {
          "topic": "Pregnancy and preeclampsia studies",
          "works": 4
        },
        {
          "topic": "Physical Activity and Health",
          "works": 4
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 4
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Helen Skouteris",
          "works": 33
        },
        {
          "name": "Briony Hill",
          "works": 22
        },
        {
          "name": "Helena Teede",
          "works": 20
        },
        {
          "name": "Nancy Devlin",
          "works": 12
        },
        {
          "name": "Kim Dalziel",
          "works": 12
        },
        {
          "name": "Cheryce L. Harrison",
          "works": 11
        },
        {
          "name": "Tessa Peasgood",
          "works": 11
        },
        {
          "name": "Shakila Thangaratinam",
          "works": 10
        },
        {
          "name": "Ruth Walker",
          "works": 9
        },
        {
          "name": "Jacqueline Boyle",
          "works": 8
        },
        {
          "name": "Heidi Bergmeier",
          "works": 8
        },
        {
          "name": "Zanfina Ademi",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7169580014",
          "year": 2026,
          "title": "The Effectiveness and Exploratory Cost-Effectiveness of Regular Meditation for Improving Quality of Life: Protocol for a Prospective Longitudinal Cohort Study",
          "type": "article",
          "venue": "JMIR Research Protocols",
          "cited_by_count": 0,
          "topics": [
            "Mindfulness and Compassion Interventions",
            "Religion, Spirituality, and Psychology",
            "Workplace Spirituality and Leadership"
          ]
        },
        {
          "openalex_id": "W7166745655",
          "year": 2026,
          "title": "Validation of the EQ-HWB-9 in a mental health sample and an investigation of modifications to items",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Mindfulness and Compassion Interventions",
            "Digital Mental Health Interventions",
            "Behavioral Health and Interventions"
          ]
        },
        {
          "openalex_id": "W4415746872",
          "year": 2025,
          "title": "A qualitative study to understand public views on the relative value of health gains for children and young people in Australia compared to adults",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "demographic modeling and climate adaptation"
          ]
        },
        {
          "openalex_id": "W4415387627",
          "year": 2025,
          "title": "Contemplative Practices as Complementary Mental Health Strategies: Insights from a Nationally Representative Sample in Australia and New Zealand",
          "type": "preprint",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Religion, Spirituality, and Psychology"
          ]
        },
        {
          "openalex_id": "W4411415124",
          "year": 2025,
          "title": "Content Validity of the EQ-HWB in Caregivers of Children with Health Conditions",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 1,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Health Education and Validation",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W4407249761",
          "year": 2025,
          "title": "Do you really want to see a 2-year-old suffer? Understanding people’s views on the relative value of health gains by age",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W268304340",
          "year": 1968,
          "title": "Educational Communications Handbook.",
          "type": "article",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "Online and Blended Learning",
            "Education and Technology Integration"
          ]
        },
        {
          "openalex_id": "W2037905533",
          "year": 1993,
          "title": "Bone lead content assessed by L-line x-ray fluorescence in lead-exposed and non-lead-exposed suburban populations in the United States.",
          "type": "article",
          "venue": "Proceedings of the National Academy of Sciences",
          "cited_by_count": 29,
          "topics": [
            "Heavy Metal Exposure and Toxicity",
            "Heavy metals in environment",
            "Radioactivity and Radon Measurements"
          ]
        },
        {
          "openalex_id": "W125891128",
          "year": 2001,
          "title": "Lead poisoning: Experience of chelation therapy proceedings of Ascept",
          "type": "conference-paper",
          "venue": "Queensland's institutional digital repository (The University of Queensland)",
          "cited_by_count": 0,
          "topics": [
            "Heavy Metal Exposure and Toxicity"
          ]
        },
        {
          "openalex_id": "W2082297407",
          "year": 2003,
          "title": "Serious lead poisoning in childhood: Still a problem after a century",
          "type": "article",
          "venue": "Journal of Paediatrics and Child Health",
          "cited_by_count": 5,
          "topics": [
            "Heavy Metal Exposure and Toxicity",
            "Occupational exposure and asthma",
            "Burn Injury Management and Outcomes"
          ]
        },
        {
          "openalex_id": "W4200619051",
          "year": 2021,
          "title": "Association of Antenatal Diet and Physical Activity–Based Interventions With Gestational Weight Gain and Pregnancy Outcomes",
          "type": "article",
          "venue": "JAMA Internal Medicine",
          "cited_by_count": 329,
          "topics": [
            "Gestational Diabetes Research and Management",
            "Pregnancy and preeclampsia studies",
            "Birth, Development, and Health"
          ]
        },
        {
          "openalex_id": "W2972891424",
          "year": 2017,
          "title": "Interventions Designed to Promote Exclusive Breastfeeding in High-Income Countries: A Systematic Review Update",
          "type": "review",
          "venue": "Breastfeeding Medicine",
          "cited_by_count": 127,
          "topics": [
            "Breastfeeding Practices and Influences",
            "Child Nutrition and Water Access",
            "Gestational Diabetes Research and Management"
          ]
        },
        {
          "openalex_id": "W2883086777",
          "year": 2018,
          "title": "Systematic review of organisation‐wide, trauma‐informed care models in out‐of‐home care (Oo<scp>HC</scp>) settings",
          "type": "review",
          "venue": "Health & Social Care in the Community",
          "cited_by_count": 93,
          "topics": [
            "Child Abuse and Trauma",
            "Child Welfare and Adoption",
            "Psychiatric care and mental health services"
          ]
        },
        {
          "openalex_id": "W4293250912",
          "year": 2022,
          "title": "Are We Agreed? Self- Versus Proxy-Reporting of Paediatric Health-Related Quality of Life (HRQoL) Using Generic Preference-Based Measures: A Systematic Review and Meta-Analysis",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 79,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W4206911976",
          "year": 2022,
          "title": "Systematic Review of Conceptual, Age, Measurement and Valuation Considerations for Generic Multidimensional Childhood Patient-Reported Outcome Measures",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 78,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W3092022449",
          "year": 2020,
          "title": "Bridging the research–practice gap in healthcare: a rapid review of research translation centres in England and Australia",
          "type": "article",
          "venue": "Health Research Policy and Systems",
          "cited_by_count": 73,
          "topics": [
            "Health and Medical Research Impacts",
            "Health Policy Implementation Science",
            "Health Sciences Research and Education"
          ]
        },
        {
          "openalex_id": "W2990651847",
          "year": 2019,
          "title": "Health in Preconception, Pregnancy and Postpartum Global Alliance: International Network Preconception Research Priorities for the Prevention of Maternal Obesity and Related Pregnancy and Long-Term Complications",
          "type": "article",
          "venue": "Journal of Clinical Medicine",
          "cited_by_count": 65,
          "topics": [
            "Gestational Diabetes Research and Management",
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Birth, Development, and Health"
          ]
        },
        {
          "openalex_id": "W2935152672",
          "year": 2019,
          "title": "A systematic mapping review of the associations between pregnancy intentions and health-related lifestyle behaviours or psychological wellbeing",
          "type": "article",
          "venue": "Preventive Medicine Reports",
          "cited_by_count": 51,
          "topics": [
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Maternal and Perinatal Health Interventions",
            "Reproductive Health and Contraception"
          ]
        }
      ]
    }
  },
  {
    "name": "Cathrine Elgaard Jensen",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1606-RA",
        "title": "Examining whether the covid-19 pandemic has affected the Danish general population’s preferences for health",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5102727513",
      "display_name": "Cathrine Elgaard Jensen",
      "orcid": "0000-0001-7300-254X",
      "reported_affiliation": "Aalborg University",
      "works_count": 12,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 6
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 2
        },
        {
          "topic": "Insurance, Mortality, Demography, Risk Management",
          "works": 2
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 2
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 2
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 2
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 1
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 1
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 1
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 1
        },
        {
          "topic": "Cervical Cancer and HPV Research",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sabrina Storgaard Sørensen",
          "works": 6
        },
        {
          "name": "Claire Gudex",
          "works": 6
        },
        {
          "name": "Lars Holger Ehlers",
          "works": 5
        },
        {
          "name": "Morten Berg Jensen",
          "works": 4
        },
        {
          "name": "Kjeld Møller Pedersen",
          "works": 3
        },
        {
          "name": "Allan Riis",
          "works": 2
        },
        {
          "name": "Flemming Bro",
          "works": 2
        },
        {
          "name": "Helle Maindal",
          "works": 2
        },
        {
          "name": "Karin Petersen",
          "works": 2
        },
        {
          "name": "Mette Dahl Bendtsen",
          "works": 2
        },
        {
          "name": "Martin Jensen",
          "works": 2
        },
        {
          "name": "Andreas Westh Vilsbøll",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4411316975",
          "year": 2025,
          "title": "Optimal DCE design for modelling nonlinear time preferences in EQ-5D-5L valuation studies: exploration of data from Denmark and Peru",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 2,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4411050688",
          "year": 2025,
          "title": "Stability of Danish Population Health Preferences Over Time",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4404897175",
          "year": 2024,
          "title": "Geographical variation in quality-adjusted life expectancy in the North Denmark Region",
          "type": "article",
          "venue": "Scandinavian Journal of Public Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Insurance, Mortality, Demography, Risk Management"
          ]
        },
        {
          "openalex_id": "W4281479515",
          "year": 2022,
          "title": "Public versus patient health preferences: protocol for a study to elicit EQ-5D-5L health state valuations for patients who have survived a stay in intensive care",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W3216946134",
          "year": 2021,
          "title": "Danish population health measured by the EQ-5D-5L",
          "type": "article",
          "venue": "Scandinavian Journal of Public Health",
          "cited_by_count": 105,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W3126420006",
          "year": 2021,
          "title": "The Danish EQ-5D-5L Value Set: A Hybrid Model Using cTTO and DCE Data",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 197,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W7136239662",
          "year": 2016,
          "title": "Additional file 1: of A multifaceted implementation strategy versus passive implementation of low back pain guidelines in general practice: a cluster randomised controlled trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Clinical practice guidelines implementation",
            "Health Policy Implementation Science",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W7136678174",
          "year": 2016,
          "title": "Additional file 1: of A multifaceted implementation strategy versus passive implementation of low back pain guidelines in general practice: a cluster randomised controlled trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Clinical practice guidelines implementation",
            "Health Policy Implementation Science",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2994980668",
          "year": 2019,
          "title": "PCN199 COST-UTILITY ANALYSIS OF THE BI-, QUADRI-, AND NONA-VALENT HPV-VACCINE: A DECISION ANALYTIC MODEL",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Vaccine Coverage and Hesitancy",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W2995465809",
          "year": 2019,
          "title": "PNS8 IDENTIFYING MECHANISMS IN PARTICIPANT RECRUITMENT IN THE DANSIH EQ-5D-5L VALUATION STUDY",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Insurance, Mortality, Demography, Risk Management",
            "Aging and Gerontology Research"
          ]
        },
        {
          "openalex_id": "W3016551864",
          "year": 2020,
          "title": "Mapping Dermatology Life Quality Index (DLQI) scores to EQ-5D utility scores using data of patients with atopic dermatitis from the National Health and Wellness Study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 61,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dermatology and Skin Diseases",
            "Economic and Environmental Valuation"
          ]
        }
      ]
    }
  },
  {
    "name": "Chris Sampson",
    "member_affiliation": "Office of Health Economics",
    "is_member": true,
    "projects": [
      {
        "project_id": "116-RA",
        "title": "Development and testing of EQ-5D-5L bolt-on descriptors for hearing",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2112-EOI",
        "title": "UK value set HESG summer 2025 event",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "427-RA",
        "title": "Conceptualising bolt-ons: identifying key questions",
        "working_group": "Descriptive Systems, Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5002636040",
      "display_name": "Chris Sampson",
      "orcid": "0000-0001-9470-2369",
      "reported_affiliation": "Office Of Health Economics",
      "works_count": 98,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 46
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 11
        },
        {
          "topic": "Global Health Care Issues",
          "works": 9
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 9
        },
        {
          "topic": "Retinal Diseases and Treatments",
          "works": 7
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 5
        },
        {
          "topic": "Stroke Rehabilitation and Recovery",
          "works": 4
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 4
        },
        {
          "topic": "Diabetes, Cardiovascular Risks, and Lipoproteins",
          "works": 4
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 4
        },
        {
          "topic": "Personality Disorders and Psychopathology",
          "works": 4
        },
        {
          "topic": "Sleep and related disorders",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Marilyn James",
          "works": 23
        },
        {
          "name": "Simon Harding",
          "works": 10
        },
        {
          "name": "Deborah Broadbent",
          "works": 7
        },
        {
          "name": "Boliang Guo",
          "works": 6
        },
        {
          "name": "Christopher P. Cheyne",
          "works": 5
        },
        {
          "name": "Amu Wang",
          "works": 4
        },
        {
          "name": "Nick Huband",
          "works": 4
        },
        {
          "name": "Steve Geelan",
          "works": 4
        },
        {
          "name": "David K. Whynes",
          "works": 4
        },
        {
          "name": "Brendan Mulhern",
          "works": 3
        },
        {
          "name": "Richard Morriss",
          "works": 3
        },
        {
          "name": "Dyfrig Hughes",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4416180089",
          "year": 2025,
          "title": "Cost Savings Associated With Fully Automated Digital Cognitive Behavioral Therapy for Insomnia Disorder (SleepioRx): A Matched Control Study of US Patients",
          "type": "article",
          "venue": "Journal of health economics and outcomes research",
          "cited_by_count": 1,
          "topics": [
            "Sleep and related disorders",
            "Digital Mental Health Interventions",
            "Sleep and Wakefulness Research"
          ]
        },
        {
          "openalex_id": "W4416182906",
          "year": 2025,
          "title": "Cost Savings Associated With Fully Automated Digital Cognitive Behavioral Therapy for Insomnia Disorder (SleepioRx): A Matched Control Study of US Patients",
          "type": "article",
          "venue": "Journal of health economics and outcomes research",
          "cited_by_count": 0,
          "topics": [
            "Sleep and related disorders",
            "Digital Mental Health Interventions",
            "Obstructive Sleep Apnea Research"
          ]
        },
        {
          "openalex_id": "W4417176003",
          "year": 2025,
          "title": "Health economic considerations for pharmacogenomic services in the United Kingdom: The Centre for Excellence in Regulatory Science and Innovation in Pharmacogenomics",
          "type": "article",
          "venue": "British Journal of Clinical Pharmacology",
          "cited_by_count": 1,
          "topics": [
            "Pharmacogenetics and Drug Metabolism",
            "Genomics and Rare Diseases",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W4404643703",
          "year": 2024,
          "title": "A qualitative systematic review of the impact of hearing on quality of life",
          "type": "review",
          "venue": "Quality of Life Research",
          "cited_by_count": 27,
          "topics": [
            "Hearing Loss and Rehabilitation",
            "Hearing Impairment and Communication",
            "Hearing, Cochlea, Tinnitus, Genetics"
          ]
        },
        {
          "openalex_id": "W4394858765",
          "year": 2024,
          "title": "Author Reply",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W4399327403",
          "year": 2024,
          "title": "Is anchoring at ‘dead’ a theoretical requirement for health state valuation?",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 14,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2319835360",
          "year": 1981,
          "title": "Assessing Long-Stay Psychiatric Patients in Occupational Therapy",
          "type": "article",
          "venue": "British Journal of Occupational Therapy",
          "cited_by_count": 0,
          "topics": [
            "Occupational Therapy Practice and Research"
          ]
        },
        {
          "openalex_id": "W2430050857",
          "year": 1995,
          "title": "Use of a nurse in an orthopaedic foot and ankle practice.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Nursing Roles and Practices",
            "Musculoskeletal Disorders and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W2013027399",
          "year": 2003,
          "title": "Maternal Diabetes Mellitus is Associated with Altered Deposition of Fibrin-type Fibrinoid at the Villous Surface in Term Placentae",
          "type": "article",
          "venue": "Placenta",
          "cited_by_count": 23,
          "topics": [
            "Gestational Diabetes Research and Management",
            "Pregnancy and preeclampsia studies",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W1966487547",
          "year": 2010,
          "title": "Is routine dental prophylaxis effective?",
          "type": "article",
          "venue": "Evidence-Based Dentistry",
          "cited_by_count": 1,
          "topics": [
            "Dental Health and Care Utilization",
            "Oral microbiology and periodontitis research",
            "Fluoride Effects and Removal"
          ]
        },
        {
          "openalex_id": "W2955784899",
          "year": 2019,
          "title": "Transparency in Decision Modelling: What, Why, Who and How?",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 62,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Meta-analysis and systematic reviews",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W2178574726",
          "year": 2015,
          "title": "Clinical characteristics of persistent frequent attenders in primary care: case–control study",
          "type": "article",
          "venue": "Family Practice",
          "cited_by_count": 56,
          "topics": [
            "Psychosomatic Disorders and Their Treatments",
            "Mental Health Treatment and Access",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2108414379",
          "year": 2012,
          "title": "Occupational therapy predischarge home visits for patients with a stroke (HOVIS): results of a feasibility randomized controlled trial",
          "type": "article",
          "venue": "Clinical Rehabilitation",
          "cited_by_count": 49,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Occupational Therapy Practice and Research",
            "Acute Ischemic Stroke Management"
          ]
        },
        {
          "openalex_id": "W3049136724",
          "year": 2020,
          "title": "Rapid Lentiviral Vector Producer Cell Line Generation Using a Single DNA Construct",
          "type": "article",
          "venue": "Molecular Therapy — Methods & Clinical Development",
          "cited_by_count": 45,
          "topics": [
            "Virus-based gene therapy research",
            "Viral gastroenteritis research and epidemiology",
            "Viral Infectious Diseases and Gene Expression in Insects"
          ]
        },
        {
          "openalex_id": "W2501021498",
          "year": 2016,
          "title": "Efficacy and cost-effectiveness of a specialist depression service versus usual specialist mental health care to manage persistent depression: a randomised controlled trial",
          "type": "article",
          "venue": "The Lancet Psychiatry",
          "cited_by_count": 41,
          "topics": [
            "Treatment of Major Depression",
            "Mental Health Treatment and Access",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W4225135404",
          "year": 2022,
          "title": "Criteria for developing, assessing and selecting candidate EQ-5D bolt-ons",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 37,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4281646039",
          "year": 2022,
          "title": "Supply-Side Cost-Effectiveness Thresholds: Questions for Evidence-Based Policy",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 34,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4221031157",
          "year": 2022,
          "title": "Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) statement: updated reporting guidance for health economic evaluations",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 31,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Christine Mpundu-Kaambwa",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1709-RA",
        "title": "Can pictorial enhancements extend the self-report age of the EQ-5D-Y? An exploratory study in 4 to 7-year-olds",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "2129-RA",
        "title": "Mapping EQ-TIPS-3L and EQ-TIPS-5L to EQ-5D-Y-5L in Young Children to Enable Preference-Weighting EQ-TIPS Using EQ-5D-Y Value Sets",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5020619329",
      "display_name": "Christine Mpundu‐Kaambwa",
      "orcid": "0000-0002-8152-6068",
      "reported_affiliation": "The University of Melbourne",
      "works_count": 48,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 18
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 16
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 6
        },
        {
          "topic": "COVID-19 and healthcare impacts",
          "works": 4
        },
        {
          "topic": "Heart Rate Variability and Autonomic Control",
          "works": 3
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 3
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 3
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 3
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 3
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 3
        },
        {
          "topic": "Insurance, Mortality, Demography, Risk Management",
          "works": 2
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Julie Ratcliffe",
          "works": 23
        },
        {
          "name": "Gang Chen",
          "works": 15
        },
        {
          "name": "Billingsley Kaambwa",
          "works": 10
        },
        {
          "name": "Norma B. Bulamu",
          "works": 9
        },
        {
          "name": "Hanadi Al Hamad",
          "works": 8
        },
        {
          "name": "Hassan Abolhassani",
          "works": 7
        },
        {
          "name": "Bright Opoku Ahinkorah",
          "works": 7
        },
        {
          "name": "Fahad Alanezi",
          "works": 7
        },
        {
          "name": "Jyoti Khadka",
          "works": 7
        },
        {
          "name": "Remo Russo",
          "works": 7
        },
        {
          "name": "Michael Abdelmasseh",
          "works": 6
        },
        {
          "name": "Aidin Abedi",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4413364008",
          "year": 2025,
          "title": "Implications of Value Set Choice on EQ-5D-Y-3L Child and Proxy Health-Related Quality of Life Ratings: What to Do When a Country-Specific “Y” Value Set Is Unavailable?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4413005429",
          "year": 2025,
          "title": "Investigating older people’s preferences for an urgent care service: a discrete choice experiment",
          "type": "article",
          "venue": "BMC Geriatrics",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Geriatric Care and Nursing Homes",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4391277444",
          "year": 2024,
          "title": "An Investigation of Inter-Rater and Intra-Proxy Agreement in Measuring Quality of Life of Children in the Community Using the EQ-5D-Y-3L",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Reliability and Agreement in Measurement"
          ]
        },
        {
          "openalex_id": "W4391723498",
          "year": 2024,
          "title": "Content Comparison of Quality-of-Life Instruments Used in Economic Evaluations of Sleep Disorder Interventions: A Systematic Review",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 3,
          "topics": [
            "Sleep and related disorders",
            "Parkinson's Disease Mechanisms and Treatments",
            "Restless Legs Syndrome Research"
          ]
        },
        {
          "openalex_id": "W4391786302",
          "year": 2024,
          "title": "Exploring the Use of Pictorial Approaches in the Development of Paediatric Patient-Reported Outcome Instruments: A Systematic Review",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 13,
          "topics": [
            "Pediatric Pain Management Techniques",
            "Childhood Cancer Survivors' Quality of Life",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W4392663706",
          "year": 2024,
          "title": "Global age-sex-specific mortality, life expectancy, and population estimates in 204 countries and territories and 811 subnational locations, 1950–2021, and the impact of the COVID-19 pandemic: a comprehensive demographic analysis for the Global Burden of Disease Study 2021",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 989,
          "topics": [
            "COVID-19 epidemiological studies",
            "Insurance, Mortality, Demography, Risk Management",
            "Immune responses and vaccinations"
          ]
        },
        {
          "openalex_id": "W1998708390",
          "year": 2014,
          "title": "An equivalence evaluation of a nurse-moderated group-based internet support program for new mothers versus standard care: a pragmatic preference randomised controlled trial",
          "type": "article",
          "venue": "BMC Pediatrics",
          "cited_by_count": 9,
          "topics": [
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Infant Development and Preterm Care",
            "Telemedicine and Telehealth Implementation"
          ]
        },
        {
          "openalex_id": "W2023626961",
          "year": 2014,
          "title": "The Spectrum of Children's Palliative Care Needs: a classification framework for children with life-limiting or life-threatening conditions",
          "type": "article",
          "venue": "BMJ Supportive & Palliative Care",
          "cited_by_count": 21,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Ethics and Legal Issues in Pediatric Healthcare",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2054870672",
          "year": 2015,
          "title": "Gastric Emptying Is More Rapid in Adolescents With Type 1 Diabetes and Impacts on Postprandial Glycemia",
          "type": "article",
          "venue": "The Journal of Clinical Endocrinology & Metabolism",
          "cited_by_count": 54,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Diabetes Management and Research",
            "Heart Rate Variability and Autonomic Control"
          ]
        },
        {
          "openalex_id": "W1506007981",
          "year": 2015,
          "title": "Gastric emptying is rapid in adolescents with type 1 diabetes and relates to gastrointestinal symptoms",
          "type": "article",
          "venue": "International Journal of Pediatric Endocrinology",
          "cited_by_count": 0,
          "topics": [
            "Heart Rate Variability and Autonomic Control",
            "Cardiovascular Syncope and Autonomic Disorders",
            "Heart rate and cardiovascular health"
          ]
        },
        {
          "openalex_id": "W4293276539",
          "year": 2022,
          "title": "The global burden of cancer attributable to risk factors, 2010–19: a systematic analysis for the Global Burden of Disease Study 2019",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 949,
          "topics": [
            "Global Cancer Incidence and Screening",
            "Cancer Risks and Factors",
            "COVID-19 and healthcare impacts"
          ]
        },
        {
          "openalex_id": "W4366977264",
          "year": 2023,
          "title": "Global burden of chronic respiratory diseases and risk factors, 1990–2019: an update from the Global Burden of Disease Study 2019",
          "type": "article",
          "venue": "EClinicalMedicine",
          "cited_by_count": 777,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Asthma and respiratory diseases",
            "Interstitial Lung Diseases and Idiopathic Pulmonary Fibrosis"
          ]
        },
        {
          "openalex_id": "W4394019396",
          "year": 2024,
          "title": "Global fertility in 204 countries and territories, 1950–2021, with forecasts to 2100: a comprehensive demographic analysis for the Global Burden of Disease Study 2021",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 591,
          "topics": [
            "Global Maternal and Child Health",
            "Insurance, Mortality, Demography, Risk Management",
            "Family Dynamics and Relationships"
          ]
        },
        {
          "openalex_id": "W4200359149",
          "year": 2021,
          "title": "The global burden of adolescent and young adult cancer in 2019: a systematic analysis for the Global Burden of Disease Study 2019",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 283,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Acute Lymphoblastic Leukemia research",
            "COVID-19 and healthcare impacts"
          ]
        },
        {
          "openalex_id": "W4318393808",
          "year": 2023,
          "title": "Global investments in pandemic preparedness and COVID-19: development assistance and domestic spending on health between 1990 and 2026",
          "type": "article",
          "venue": "The Lancet Global Health",
          "cited_by_count": 230,
          "topics": [
            "Viral Infections and Outbreaks Research",
            "Healthcare Systems and Reforms",
            "Global Security and Public Health"
          ]
        },
        {
          "openalex_id": "W3199493325",
          "year": 2021,
          "title": "Tracking development assistance for health and for COVID-19: a review of development assistance, government, out-of-pocket, and other private spending on health for 204 countries and territories, 1990–2050",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 159,
          "topics": [
            "Viral Infections and Outbreaks Research",
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W3202618816",
          "year": 2021,
          "title": "Global, regional, and national sex-specific burden and control of the HIV epidemic, 1990–2019, for 204 countries and territories: the Global Burden of Diseases Study 2019",
          "type": "article",
          "venue": "The Lancet HIV",
          "cited_by_count": 132,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "Adolescent Sexual and Reproductive Health",
            "HIV Research and Treatment"
          ]
        }
      ]
    }
  }
]
