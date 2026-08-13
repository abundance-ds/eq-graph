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
    "name": "Jessica Roydhouse",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1557-RA",
        "title": "Addressing the challenge of recall periods for the proxy version of the EQ-HWB in dementia",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2134-RA",
        "title": "Evaluating respondent burden for the EQ-HWB and EQ-HWB-S in prostate cancer",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5010221662",
      "display_name": "Jessica Roydhouse",
      "orcid": "0000-0002-8025-5841",
      "reported_affiliation": "University of Tasmania",
      "works_count": 123,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 32
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 26
        },
        {
          "topic": "Statistical Methods in Clinical Trials",
          "works": 21
        },
        {
          "topic": "Advanced Causal Inference Techniques",
          "works": 11
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 11
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 11
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 9
        },
        {
          "topic": "Cancer Treatment and Pharmacology",
          "works": 9
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 8
        },
        {
          "topic": "Ethics in Clinical Research",
          "works": 8
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 7
        },
        {
          "topic": "Mental Health and Patient Involvement",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Paul G. Kluetz",
          "works": 13
        },
        {
          "name": "John Devin Peipert",
          "works": 12
        },
        {
          "name": "Smita Shah",
          "works": 12
        },
        {
          "name": "Melanie Calvert",
          "works": 11
        },
        {
          "name": "Roee Gutman",
          "works": 11
        },
        {
          "name": "Kate White",
          "works": 9
        },
        {
          "name": "Bellinda L. King‐Kallimanis",
          "works": 9
        },
        {
          "name": "Susan M. Sawyer",
          "works": 9
        },
        {
          "name": "David Cella",
          "works": 8
        },
        {
          "name": "Rebecca Mercieca‐Bebber",
          "works": 8
        },
        {
          "name": "Ira B. Wilson",
          "works": 8
        },
        {
          "name": "Claudia Rutherford",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7147679594",
          "year": 2026,
          "title": "127MO A practical toolkit with recommendations for analysing and visualising patient-reported outcomes in early phase dose-finding oncology trials: OPTIMISE-AR",
          "type": "article",
          "venue": "ESMO Open",
          "cited_by_count": 0,
          "topics": [
            "Statistical Methods in Clinical Trials",
            "Radiopharmaceutical Chemistry and Applications",
            "Prostate Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W7138367746",
          "year": 2026,
          "title": "A practical toolkit with recommendations for analysing and visualising patient-reported outcomes in early phase dose-finding oncology trials (OPTIMISE-AR)",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 1,
          "topics": [
            "Statistical Methods in Clinical Trials",
            "Prostate Cancer Diagnosis and Treatment",
            "Advanced Radiotherapy Techniques"
          ]
        },
        {
          "openalex_id": "W7119009460",
          "year": 2026,
          "title": "A single item for overall side effect impact: Association with clinician-reported adverse events and global health",
          "type": "article",
          "venue": "Clinical Trials",
          "cited_by_count": 0,
          "topics": [
            "Pain Management and Placebo Effect",
            "Pharmacovigilance and Adverse Drug Reactions",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W7147077407",
          "year": 2026,
          "title": "Carers’ interpretation of the recall period and perspective-taking when completing the EQ health and wellbeing instrument (EQ-HWB)-9 as proxies for people with dementia: a think-aloud study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Mental Health and Patient Involvement",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W7138945340",
          "year": 2026,
          "title": "Designing and Implementing Real-World Patient-Reported Outcomes—Emerging Recommendations: A Good Practices Report of an ISPOR Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Primary Care and Health Outcomes",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W7166809580",
          "year": 2026,
          "title": "Developing a Set of Core Patient‐Reported Outcomes for Kidney Replacement Therapy: A Modified Delphi Study",
          "type": "article",
          "venue": "Journal of Renal Care",
          "cited_by_count": 0,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Delphi Technique in Research",
            "Acute Kidney Injury Research"
          ]
        },
        {
          "openalex_id": "W2058742453",
          "year": 2008,
          "title": "Asthma education in primary healthcare settings",
          "type": "article",
          "venue": "Current Opinion in Pediatrics",
          "cited_by_count": 19,
          "topics": [
            "Asthma and respiratory diseases",
            "Medication Adherence and Compliance",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W209325835",
          "year": 2008,
          "title": "Medical students go back to school--the Triple A journey.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 9,
          "topics": [
            "Child and Adolescent Health",
            "Empathy and Medical Education"
          ]
        },
        {
          "openalex_id": "W1994933637",
          "year": 2009,
          "title": "Becoming Australian? Two different approaches to health care reform in the United States",
          "type": "article",
          "venue": "Australian Health Review",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Primary Care and Health Outcomes",
            "Health Services Management and Policy"
          ]
        },
        {
          "openalex_id": "W2322626251",
          "year": 2009,
          "title": "Evaluation of Asthma Education and Communication Skills Workshops for General Practitioners.",
          "type": "conference-abstract",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "School Health and Nursing Education"
          ]
        },
        {
          "openalex_id": "W4304731581",
          "year": 2022,
          "title": "Key considerations to reduce or address respondent burden in patient-reported outcome (PRO) data collection",
          "type": "article",
          "venue": "Nature Communications",
          "cited_by_count": 179,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2124291048",
          "year": 2011,
          "title": "Strategies for Piloting a Breast Health Promotion Program in the Chinese-Australian Population",
          "type": "article",
          "venue": "Preventing Chronic Disease",
          "cited_by_count": 125,
          "topics": [
            "Global Cancer Incidence and Screening",
            "Health Promotion and Cardiovascular Prevention",
            "Cultural Competency in Health Care"
          ]
        },
        {
          "openalex_id": "W4392294166",
          "year": 2024,
          "title": "Recommendations to address respondent burden associated with patient-reported outcome assessment",
          "type": "article",
          "venue": "Nature Medicine",
          "cited_by_count": 124,
          "topics": [
            "Delphi Technique in Research",
            "Cancer survivorship and care",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4280537076",
          "year": 2022,
          "title": "Ethical Considerations for the Inclusion of Patient-Reported Outcomes in Clinical Research",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 89,
          "topics": [
            "Cancer survivorship and care",
            "Delphi Technique in Research",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W2910830708",
          "year": 2019,
          "title": "Investigating Potential Bias in Patient-Reported Outcomes in Open-label Cancer Trials",
          "type": "article",
          "venue": "JAMA Oncology",
          "cited_by_count": 68,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W2054631690",
          "year": 2011,
          "title": "Chinese-Australian Women’s Knowledge, Facilitators and Barriers Related to Cervical Cancer Screening: A Qualitative Study",
          "type": "article",
          "venue": "Journal of Immigrant and Minority Health",
          "cited_by_count": 64,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Global Cancer Incidence and Screening",
            "Cultural Competency in Health Care"
          ]
        },
        {
          "openalex_id": "W2782235902",
          "year": 2018,
          "title": "Proxy and patient reports of health-related quality of life in a national cancer survey",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 55,
          "topics": [
            "Cancer survivorship and care",
            "Patient Satisfaction in Healthcare",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W2978416960",
          "year": 2019,
          "title": "US Food and Drug Administration review of statistical analysis of patient-reported outcomes in lung cancer clinical trials approved between January, 2008, and December, 2017",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 48,
          "topics": [
            "Cancer survivorship and care",
            "Statistical Methods in Clinical Trials",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        }
      ]
    }
  },
  {
    "name": "Jia Jia Lee",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1971-EO",
        "title": "Travel scholarship request to attend ISPOR Europe 2024 for findings dissemination.",
        "working_group": "Dissemination, OA fee"
      },
      {
        "project_id": "2125-RA",
        "title": "Assessing added values and psychometric performance of breathing, sleep, fatigue, EQ-HWB-25 and EQ-HWB-9 among obese individuals receiving weight-loss intervention",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2179-RA",
        "title": "Developing a localized electronic version of EQ-5D-Y-5L and evaluating its measurement properties for use in clinical settings: the case of Paediatric and Adolescent Wellness Service (PAWS)",
        "working_group": "Populations and Health Systems, Youth"
      },
      {
        "project_id": "2299-EO",
        "title": "Travel scholarship request to attend ISPOR Europe 2025 for findings dissemination",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5050544932",
      "display_name": "Jia Jia Lee",
      "orcid": "0000-0001-7821-9131",
      "reported_affiliation": "",
      "works_count": 29,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 5
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 5
        },
        {
          "topic": "Eating Disorders and Behaviors",
          "works": 4
        },
        {
          "topic": "Bariatric Surgery and Outcomes",
          "works": 4
        },
        {
          "topic": "Dialysis and Renal Disease Management",
          "works": 3
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 3
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 3
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 3
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 3
        },
        {
          "topic": "Behavioral Health and Interventions",
          "works": 3
        },
        {
          "topic": "Chronic Kidney Disease and Diabetes",
          "works": 2
        },
        {
          "topic": "Physical Activity and Health",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Semra Özdemir",
          "works": 15
        },
        {
          "name": "Nan Luo",
          "works": 9
        },
        {
          "name": "Eric Finkelstein",
          "works": 8
        },
        {
          "name": "Irene Teo",
          "works": 8
        },
        {
          "name": "Chetna Malhotra",
          "works": 5
        },
        {
          "name": "Nivedita Nadkarni",
          "works": 5
        },
        {
          "name": "Yiyun Shou",
          "works": 4
        },
        {
          "name": "Priscilla How",
          "works": 3
        },
        {
          "name": "Khung Keong Yeo",
          "works": 3
        },
        {
          "name": "Kheng Leng David Sim",
          "works": 3
        },
        {
          "name": "Asim Shabbir",
          "works": 3
        },
        {
          "name": "Hwee Lin Wee",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7163769664",
          "year": 2026,
          "title": "EQ-5D-5L population norms for Singapore: a household survey-based analysis",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W7155003756",
          "year": 2026,
          "title": "Experiential learning to advocacy: A peer-led approach to safe medication disposal in pharmacy education",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical and Antibiotic Environmental Impacts",
            "Healthcare and Environmental Waste Management",
            "Fecal contamination and water quality"
          ]
        },
        {
          "openalex_id": "W7128543601",
          "year": 2026,
          "title": "Exploring the psychological well-being construct and validating the Comprehensive Inventory of Thriving in Singapore",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Grit, Self-Efficacy, and Motivation",
            "Aging and Gerontology Research"
          ]
        },
        {
          "openalex_id": "W7164829811",
          "year": 2026,
          "title": "Health-related quality of life of people with obesity who have and have not received metabolic bariatric surgery: a qualitative study in Singapore",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Bariatric Surgery and Outcomes",
            "Body Contouring and Surgery",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W7127120964",
          "year": 2026,
          "title": "Identifying Symptom Burden Phenotypes and Building a Classification Model in Adults with Overweight/Obesity: A Latent Profile Analysis and Machine Learning Approach",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Mental Health via Writing",
            "Bariatric Surgery and Outcomes",
            "Mental Health Research Topics"
          ]
        },
        {
          "openalex_id": "W4412555489",
          "year": 2025,
          "title": "Assessing the Health-Related Quality of Life of Children With Asthma or Eczema by a Proxy: Does Assessment Perspective Matter?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Dermatology and Skin Diseases",
            "Asthma and respiratory diseases",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2317746282",
          "year": 2012,
          "title": "Multidisciplinary clinic for patients with newly diagnosed chronic kidney disease",
          "type": "article",
          "venue": "American Journal of Health-System Pharmacy",
          "cited_by_count": 1,
          "topics": [
            "Chronic Kidney Disease and Diabetes",
            "Dialysis and Renal Disease Management",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2587822040",
          "year": 2015,
          "title": "SP697PATIENT-REPORTED OUTCOMES BETWEEN HEMODIALYSIS AND PERITONEAL DIALYSIS PATIENTS IN A MULTI-ETHNIC ASIAN POPULATION",
          "type": "conference-abstract",
          "venue": "Nephrology Dialysis Transplantation",
          "cited_by_count": 0,
          "topics": [
            "Dialysis and Renal Disease Management"
          ]
        },
        {
          "openalex_id": "W2473021009",
          "year": 2016,
          "title": "Association of anemia and mineral and bone disorder with health-related quality of life in Asian pre-dialysis patients",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 38,
          "topics": [
            "Parathyroid Disorders and Treatments",
            "Dialysis and Renal Disease Management",
            "Chronic Kidney Disease and Diabetes"
          ]
        },
        {
          "openalex_id": "W3119883719",
          "year": 2020,
          "title": "The Effect of Social Norm-based Intervention on Physical Activity among Adolescents: A Randomized Controlled Trial",
          "type": "preprint",
          "venue": "Research Square (Research Square)",
          "cited_by_count": 0,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Eating Disorders and Behaviors",
            "Physical Activity and Health"
          ]
        },
        {
          "openalex_id": "W4291019303",
          "year": 2022,
          "title": "Understanding patient preferences in anti-VEGF treatment options for age-related macular degeneration",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 28,
          "topics": [
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W3164521827",
          "year": 2021,
          "title": "A Systematic Review of Discrete Choice Experiments and Conjoint Analysis on Genetic Testing",
          "type": "review",
          "venue": "Patient",
          "cited_by_count": 26,
          "topics": [
            "BRCA gene mutations in cancer",
            "Pharmacogenetics and Drug Metabolism",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4282571926",
          "year": 2022,
          "title": "Awareness and Utilization of Palliative Care Among Advanced Cancer Patients in Asia",
          "type": "article",
          "venue": "Journal of Pain and Symptom Management",
          "cited_by_count": 16,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Pain Management and Opioid Use",
            "Palliative and Oncologic Care"
          ]
        },
        {
          "openalex_id": "W3178298966",
          "year": 2021,
          "title": "The prevalence of perceived stigma and self-blame and their associations with depression, emotional well-being and social well-being among advanced cancer patients: evidence from the APPROACH cross-sectional study in Vietnam",
          "type": "article",
          "venue": "BMC Palliative Care",
          "cited_by_count": 16,
          "topics": [
            "Cancer survivorship and care",
            "Mental Health Treatment and Access",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W4282821813",
          "year": 2022,
          "title": "Patient Medication Preferences for Managing Dry Eye Disease: The Importance of Medication Side Effects",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 14,
          "topics": [
            "Ocular Surface and Contact Lens",
            "Allergic Rhinitis and Sensitization",
            "Ocular Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W3205594654",
          "year": 2021,
          "title": "Associations Between Prognostic Awareness, Acceptance of Illness, and Psychological and Spiritual Well-being Among Patients With Heart Failure",
          "type": "article",
          "venue": "Journal of Cardiac Failure",
          "cited_by_count": 12,
          "topics": [
            "Religion, Spirituality, and Psychology",
            "Heart Failure Treatment and Management",
            "Optimism, Hope, and Well-being"
          ]
        },
        {
          "openalex_id": "W4296328290",
          "year": 2022,
          "title": "Preferences for a non‐invasive prenatal test as first‐line screening for Down Syndrome: A discrete choice experiment",
          "type": "article",
          "venue": "Prenatal Diagnosis",
          "cited_by_count": 6,
          "topics": [
            "Prenatal Screening and Diagnostics",
            "Pregnancy and Medication Impact",
            "HIV/AIDS Research and Interventions"
          ]
        }
      ]
    }
  },
  {
    "name": "Jiabi Wen",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2288-EO",
        "title": "Applying for travel scholarship to attend the 2025 ISPOR Europe Meeting: Country-related differential item functioning in the EQ-5D-5L: Insights from the EuroQol Data Assessment of Population Health Needs and Instrument Evaluation (EQ-DAPHNIE)",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5001767251",
      "display_name": "Jiabi Wen",
      "orcid": "0000-0001-9579-9625",
      "reported_affiliation": "University of Alberta",
      "works_count": 13,
      "top_topics": [
        {
          "topic": "SARS-CoV-2 detection and testing",
          "works": 6
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 3
        },
        {
          "topic": "Healthcare and Environmental Waste Management",
          "works": 3
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 2
        },
        {
          "topic": "Autoimmune and Inflammatory Disorders Research",
          "works": 2
        },
        {
          "topic": "Adolescent and Pediatric Healthcare",
          "works": 2
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 2
        },
        {
          "topic": "Infection Control and Ventilation",
          "works": 2
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 1
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 1
        },
        {
          "topic": "Diabetic Foot Ulcer Assessment and Management",
          "works": 1
        },
        {
          "topic": "Wound Healing and Treatments",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Arto Öhinmaa",
          "works": 8
        },
        {
          "name": "Xiaoli Pang",
          "works": 5
        },
        {
          "name": "Bonita E. Lee",
          "works": 5
        },
        {
          "name": "Judy Qiu",
          "works": 5
        },
        {
          "name": "Eleanor Risling",
          "works": 5
        },
        {
          "name": "Lorie A Little",
          "works": 5
        },
        {
          "name": "Fatima Al Sayah",
          "works": 4
        },
        {
          "name": "Jeffrey Johnson",
          "works": 4
        },
        {
          "name": "Tiejun Gao",
          "works": 4
        },
        {
          "name": "Rhonda J. Rosychuk",
          "works": 4
        },
        {
          "name": "Christopher Sikora",
          "works": 4
        },
        {
          "name": "Michael Y. Li",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164048008",
          "year": 2026,
          "title": "Responsiveness of the EQ-5D-Y-5L Parent-Proxy Version Among Children with Juvenile Idiopathic Arthritis",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 0,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Rheumatoid Arthritis Research and Therapies",
            "Adolescent and Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W7154031915",
          "year": 2026,
          "title": "Site-specific wastewater-based surveillance in early detection of COVID-19 new cases and prediction of mass testing outcomes in long-term care facilities",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 0,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "COVID-19 epidemiological studies",
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W4417480396",
          "year": 2025,
          "title": "EE671 Stakeholder Engagement in the Economic Evaluation of Site-Specific Wastewater-Based Surveillance for Preventing COVID-19 Outbreaks in Long-Term Care Facilities",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Infection Control and Ventilation",
            "SARS-CoV-2 detection and testing",
            "Healthcare and Environmental Waste Management"
          ]
        },
        {
          "openalex_id": "W4417481598",
          "year": 2025,
          "title": "EE695 The Cost-Effectiveness of Using Site-Specific Wastewater-Based Surveillance to Monitor COVID-19 in Long-Term Care Facilities",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "Infection Control and Ventilation",
            "Healthcare and Environmental Waste Management"
          ]
        },
        {
          "openalex_id": "W4417480164",
          "year": 2025,
          "title": "EPH215 Site-Specific Wastewater-Based Surveillance in Early Detection of COVID-19 New Cases and Prediction of Mass Testing Outcomes in Long-Term Care Facilities",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "Wastewater Treatment and Reuse",
            "COVID-19 impact on air quality"
          ]
        },
        {
          "openalex_id": "W4417480899",
          "year": 2025,
          "title": "MSR64 Country-Related Differential Item Functioning in the EQ-5D-5L: Insights From the EuroQol Data Assessment of Population Health Needs and Instrument Evaluation (EQ-DAPHNIE)",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W3124214428",
          "year": 2020,
          "title": "Mapping for the EQ-5D-5L for Use in Cost-Utility Analysis",
          "type": "dissertation",
          "venue": "University of Alberta Library",
          "cited_by_count": 0,
          "topics": [
            "Manufacturing Process and Optimization"
          ]
        },
        {
          "openalex_id": "W3180441084",
          "year": 2021,
          "title": "Economic Evaluation of Sucrose Octasulfate Dressing for Treatment of Diabetic Foot Ulcers in Patients with Type 2 Diabetes",
          "type": "article",
          "venue": "Canadian Journal of Diabetes",
          "cited_by_count": 17,
          "topics": [
            "Diabetic Foot Ulcer Assessment and Management",
            "Wound Healing and Treatments",
            "Peripheral Artery Disease Management"
          ]
        },
        {
          "openalex_id": "W3186024635",
          "year": 2021,
          "title": "Mapping the Edmonton Symptom Assessment System-Revised: Renal to the EQ-5D-5L in patients with chronic kidney disease",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 9,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dialysis and Renal Disease Management",
            "Chronic Kidney Disease and Diabetes"
          ]
        },
        {
          "openalex_id": "W4304807336",
          "year": 2022,
          "title": "Self-reported health-related quality of life of the general population in Alberta, Canada during the COVID-19 pandemic",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 19,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "COVID-19 and Mental Health",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4401798793",
          "year": 2024,
          "title": "Early warning COVID-19 outbreak in long-term care facilities using wastewater surveillance: correlation, prediction, and interaction with clinical and serological statuses",
          "type": "article",
          "venue": "The Lancet Microbe",
          "cited_by_count": 11,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "COVID-19 Clinical Research Studies",
            "Healthcare and Environmental Waste Management"
          ]
        },
        {
          "openalex_id": "W4401579976",
          "year": 2024,
          "title": "Validation of the EQ-5D-Y-5L parent-proxy version among children with juvenile idiopathic arthritis",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 3,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Adolescent and Pediatric Healthcare",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        }
      ]
    }
  },
  {
    "name": "Jill Carlton",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1988-RA",
        "title": "Assessing Content Validity in Generic Adult and Paediatric Preference-Weighted Measures: A Scoping Review to Identify Current Practice",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2148-RA",
        "title": "Developing guidance for best practice in collaborative involvement (CI) in health state valuation studies: An extension to CREATE (CREATE-CI)",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5051490866",
      "display_name": "Jill Carlton",
      "orcid": "0000-0002-9373-7663",
      "reported_affiliation": "University of Sheffield",
      "works_count": 170,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 49
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 38
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 18
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 15
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 12
        },
        {
          "topic": "Retinal Diseases and Treatments",
          "works": 11
        },
        {
          "topic": "Muscle Physiology and Disorders",
          "works": 11
        },
        {
          "topic": "Mental Health and Patient Involvement",
          "works": 9
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 9
        },
        {
          "topic": "Retinopathy of Prematurity Studies",
          "works": 7
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 7
        },
        {
          "topic": "Visual perception and processing mechanisms",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "John Brazier",
          "works": 51
        },
        {
          "name": "Donna Rowen",
          "works": 41
        },
        {
          "name": "Philip A. Powell",
          "works": 37
        },
        {
          "name": "Tessa Peasgood",
          "works": 21
        },
        {
          "name": "Janice Connell",
          "works": 16
        },
        {
          "name": "Anju Keetharuth",
          "works": 15
        },
        {
          "name": "Clara Mukuria",
          "works": 15
        },
        {
          "name": "Frans Pouwer",
          "works": 13
        },
        {
          "name": "Jan Henrik Terheyden",
          "works": 12
        },
        {
          "name": "Robert P. Finger",
          "works": 11
        },
        {
          "name": "Frank G. Holz",
          "works": 11
        },
        {
          "name": "Melanie Broadley",
          "works": 11
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7128304736",
          "year": 2026,
          "title": "<b>Protocol for Assessing Content Validity in Generic Preference-weighted Measures: A Scoping Review</b>",
          "type": "other",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7128313152",
          "year": 2026,
          "title": "<b>Protocol for Assessing Content Validity in Generic Preference-weighted Measures: A Scoping Review</b>",
          "type": "other",
          "venue": "ORDA - The University of Sheffield Research Data Catalogue and Repository",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7140369020",
          "year": 2026,
          "title": "Measuring health-related quality of life in facioscapulohumeral muscular dystrophy: a COSMIN systematic review and conceptual framework",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Muscle Physiology and Disorders",
            "Cardiomyopathy and Myosin Studies",
            "Muscle activation and electromyography studies"
          ]
        },
        {
          "openalex_id": "W7125405142",
          "year": 2026,
          "title": "Patient-Led Collaboration for HTA Tools and Evidence Development: Project HERCULES",
          "type": "book-chapter",
          "venue": "Health informatics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Genomics and Rare Diseases",
            "Biomedical Ethics and Regulation"
          ]
        },
        {
          "openalex_id": "W7167574748",
          "year": 2026,
          "title": "Qualitative testing of potential modifications to the EQ-HWB-9 v1.2 in adults with mobility problems in the United Kingdom",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W7133568900",
          "year": 2026,
          "title": "Understanding decision-making strategies in discrete choice experiment tasks when valuing health states that include duration, a cognitive interview study with Australian adults",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2796689598",
          "year": 1984,
          "title": "The Genesis of Il barone rampante",
          "type": "article",
          "venue": "Italica",
          "cited_by_count": 4,
          "topics": [
            "Renaissance and Early Modern Studies"
          ]
        },
        {
          "openalex_id": "W2052708802",
          "year": 2005,
          "title": "The Impact of Age-Related Macular Degeneration on Health Status Utility Values",
          "type": "article",
          "venue": "Investigative Ophthalmology & Visual Science",
          "cited_by_count": 154,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Retinal Diseases and Treatments",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2094597306",
          "year": 2006,
          "title": "Determinants of health related quality of life and health state utility in patients with age related macular degeneration: the association of contrast sensitivity and visual acuity",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 84,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Retinal Diseases and Treatments",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W167446065",
          "year": 2007,
          "title": "Health State Valuation for Armd Visual Impairment States Using Simulation Lenses",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Older Adults Driving Studies",
            "Tactile and Sensory Interactions"
          ]
        },
        {
          "openalex_id": "W2802639520",
          "year": 2018,
          "title": "The importance of content and face validity in instrument development: lessons learnt from service users when developing the Recovering Quality of Life measure (ReQoL)",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 311,
          "topics": [
            "Mental Health and Patient Involvement",
            "Down syndrome and intellectual disability research",
            "Occupational Therapy Practice and Research"
          ]
        },
        {
          "openalex_id": "W2745578526",
          "year": 2018,
          "title": "Recovering Quality of Life (ReQoL): a new generic self-reported outcome measure for use with people experiencing mental health difficulties",
          "type": "article",
          "venue": "The British Journal of Psychiatry",
          "cited_by_count": 272,
          "topics": [
            "Mental Health and Patient Involvement",
            "Digital Mental Health Interventions",
            "Down syndrome and intellectual disability research"
          ]
        },
        {
          "openalex_id": "W1985046976",
          "year": 2008,
          "title": "The clinical effectiveness and cost-effectiveness of screening programmes for amblyopia and strabismus in children up to the age of 4-5 years: a systematic review and economic evaluation",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 177,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Retinopathy of Prematurity Studies",
            "Visual perception and processing mechanisms"
          ]
        },
        {
          "openalex_id": "W4220774050",
          "year": 2022,
          "title": "The EQ-HWB: Overview of the Development of a Measure of Health and Wellbeing and Key Results",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 175,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychological Well-being and Life Satisfaction",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2530421404",
          "year": 2016,
          "title": "Proceedings of Patient Reported Outcome Measure’s (PROMs) Conference Sheffield 2016: advances in patient reported outcomes research",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 152,
          "topics": [
            "Primary Care and Health Outcomes",
            "Chronic Disease Management Strategies",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2085804494",
          "year": 2011,
          "title": "Amblyopia and quality of life: a systematic review",
          "type": "review",
          "venue": "Eye",
          "cited_by_count": 149,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Retinal Diseases and Treatments",
            "Visual perception and processing mechanisms"
          ]
        },
        {
          "openalex_id": "W2904047048",
          "year": 2018,
          "title": "A review of quality of life themes in Duchenne muscular dystrophy for patients and carers",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 97,
          "topics": [
            "Muscle Physiology and Disorders",
            "Transcranial Magnetic Stimulation Studies",
            "Fibromyalgia and Chronic Fatigue Syndrome Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Jiyoung Park",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2450-RA",
        "title": "Psychometric Evaluation of the EQ-5D-Y-3L and EQ-5D-Y-5L in Vulnerable Child Populations: Implications for Assessing Health-Related Quality of Life",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5100409602",
      "display_name": "Jiyoung Park",
      "orcid": "0000-0003-1374-9187",
      "reported_affiliation": "",
      "works_count": 261,
      "top_topics": [
        {
          "topic": "Health and Wellbeing Research",
          "works": 19
        },
        {
          "topic": "Healthcare Education and Workforce Issues",
          "works": 19
        },
        {
          "topic": "Diverse Approaches in Healthcare and Education Studies",
          "works": 19
        },
        {
          "topic": "Psychosocial Factors Impacting Youth",
          "works": 18
        },
        {
          "topic": "Education and Learning Interventions",
          "works": 17
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 16
        },
        {
          "topic": "Nutrition, Health and Food Behavior",
          "works": 16
        },
        {
          "topic": "Photonic Crystal and Fiber Optics",
          "works": 15
        },
        {
          "topic": "Educational Systems and Policies",
          "works": 15
        },
        {
          "topic": "Advanced Fiber Optic Sensors",
          "works": 11
        },
        {
          "topic": "Optical Network Technologies",
          "works": 11
        },
        {
          "topic": "Consumer Perception and Purchasing Behavior",
          "works": 11
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kyunghwan Oh",
          "works": 21
        },
        {
          "name": "Jiyoon Lee",
          "works": 10
        },
        {
          "name": "Hee Soon Kim",
          "works": 10
        },
        {
          "name": "Gahui Hwang",
          "works": 10
        },
        {
          "name": "Gill A. ten Hoor",
          "works": 9
        },
        {
          "name": "Sejin Lee",
          "works": 7
        },
        {
          "name": "Soan Kim",
          "works": 7
        },
        {
          "name": "Chongwon Park",
          "works": 7
        },
        {
          "name": "Taeho Hong",
          "works": 7
        },
        {
          "name": "Jong-Myoung Lim",
          "works": 6
        },
        {
          "name": "Mihae Im",
          "works": 5
        },
        {
          "name": "Jeonghyun Cho",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4411076175",
          "year": 2025,
          "title": "A Proposal for Strengthening Music Education in Grades 1–2 of Elementary School: Focusing on t he I mprovement o f the Current I ntegrated Curriculum T extbooks",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Educational Systems and Policies",
            "Educational Research and Pedagogy",
            "Education, Safety, and Science Studies"
          ]
        },
        {
          "openalex_id": "W4407265110",
          "year": 2025,
          "title": "Associations Between Ecological Determinants and Weight Status Changes Among Children from Vulnerable Populations: Empirical Findings from a National Panel Survey in South Korea",
          "type": "article",
          "venue": "Western Journal of Nursing Research",
          "cited_by_count": 0,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Child Nutrition and Water Access",
            "Sleep and related disorders"
          ]
        },
        {
          "openalex_id": "W4413303910",
          "year": 2025,
          "title": "Current Status and Practical Strategies of Music Education in Lower Elementary Grades through 2022 Revised Integrated Curriculum ‘Pleasant Life’",
          "type": "article",
          "venue": "The Korean Society of Music Education Technology",
          "cited_by_count": 0,
          "topics": [
            "Educational Systems and Policies",
            "Education, Safety, and Science Studies",
            "Education and Learning Interventions"
          ]
        },
        {
          "openalex_id": "W4408361654",
          "year": 2025,
          "title": "Effect of chewing gum on clinical outcomes and postoperative recovery in adult patients after gastrointestinal surgery: an umbrella review",
          "type": "article",
          "venue": "International Journal of Surgery",
          "cited_by_count": 4,
          "topics": [
            "Enhanced Recovery After Surgery",
            "Gastrointestinal motility and disorders",
            "Clinical Nutrition and Gastroenterology"
          ]
        },
        {
          "openalex_id": "W4412136686",
          "year": 2025,
          "title": "Efficacy and Safety of GLP-1 Receptor Agonist for Adults with Overweight and Obesity: A Systematic Review and Bayesian Network Meta-Analysis of Randomized Controlled Trials",
          "type": "review",
          "venue": "Yakhak Hoeji",
          "cited_by_count": 0,
          "topics": [
            "Pharmacology and Obesity Treatment",
            "Diabetes Treatment and Management",
            "Diet and metabolism studies"
          ]
        },
        {
          "openalex_id": "W4413408872",
          "year": 2025,
          "title": "State-level political environments and executive compensation in the United States: evidence on pay inequality",
          "type": "article",
          "venue": "Economics of Governance",
          "cited_by_count": 0,
          "topics": [
            "Political Influence and Corporate Strategies",
            "Gender Diversity and Inequality",
            "Social Policy and Reform Studies"
          ]
        },
        {
          "openalex_id": "W2899439705",
          "year": 2000,
          "title": "Effects of Rifampin on Cyclosporine Disposition in Kidney Recipients with Tuberculosis",
          "type": "article",
          "venue": "Journal of Korean Society for Clinical Pharmacology and Therapeutics",
          "cited_by_count": 7,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "Diagnosis and treatment of tuberculosis",
            "Pharmacological Effects and Toxicity Studies"
          ]
        },
        {
          "openalex_id": "W2938643206",
          "year": 2000,
          "title": "Population Pharmacokinetics of Amikacin in Korean Neonates",
          "type": "article",
          "venue": "Journal of Korean Society for Clinical Pharmacology and Therapeutics",
          "cited_by_count": 0,
          "topics": [
            "Antibiotics Pharmacokinetics and Efficacy",
            "Neonatal Health and Biochemistry",
            "Drug Transport and Resistance Mechanisms"
          ]
        },
        {
          "openalex_id": "W2064458586",
          "year": 2003,
          "title": "Suppressive Effects of Genistein on Oxidative Stress and NFκB Activation in RAW 264.7 Macrophages",
          "type": "article",
          "venue": "Bioscience Biotechnology and Biochemistry",
          "cited_by_count": 77,
          "topics": [
            "Phytoestrogen effects and research",
            "Stress Responses and Cortisol",
            "Diet, Metabolism, and Disease"
          ]
        },
        {
          "openalex_id": "W2587337977",
          "year": 2004,
          "title": "A Study on the Emotional Responses of 119 Rescue/Emergency Personnels in Korea and their Families : With Regard to Linkage between Mental Health Services and Occupational Social Work",
          "type": "article",
          "venue": "Mental Health & Social Work",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Education and Workforce Issues"
          ]
        },
        {
          "openalex_id": "W2341279356",
          "year": 2016,
          "title": "When perceptions defy reality: The relationships between depression and actual and perceived Facebook social support",
          "type": "article",
          "venue": "Journal of Affective Disorders",
          "cited_by_count": 113,
          "topics": [
            "Impact of Technology on Adolescents",
            "Mental Health via Writing",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W1970544557",
          "year": 2011,
          "title": "Enhancement of chemical sensing capability  in a photonic crystal fiber  with a hollow high index ring defect at the center",
          "type": "article",
          "venue": "Optics Express",
          "cited_by_count": 81,
          "topics": [
            "Photonic Crystal and Fiber Optics",
            "Advanced Fiber Optic Sensors",
            "Advanced Fiber Laser Technologies"
          ]
        },
        {
          "openalex_id": "W2145728259",
          "year": 2005,
          "title": "Considering Risk-Taking Behavior in Travel Time Reliability",
          "type": "article",
          "venue": "eScholarship (California Digital Library)",
          "cited_by_count": 63,
          "topics": [
            "Transportation Planning and Optimization",
            "Economic and Environmental Valuation",
            "Urban Transport and Accessibility"
          ]
        },
        {
          "openalex_id": "W2790247415",
          "year": 2018,
          "title": "Behavioral Adjustment Moderates the Link Between Neuroticism and Biological Health Risk: A U.S.–Japan Comparison Study",
          "type": "article",
          "venue": "Personality and Social Psychology Bulletin",
          "cited_by_count": 60,
          "topics": [
            "Personality Traits and Psychology",
            "Optimism, Hope, and Well-being",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W2891552057",
          "year": 2018,
          "title": "Optimism and the conserved transcriptional response to adversity.",
          "type": "article",
          "venue": "Health Psychology",
          "cited_by_count": 60,
          "topics": [
            "Optimism, Hope, and Well-being",
            "Resilience and Mental Health",
            "Psychological and Temporal Perspectives Research"
          ]
        },
        {
          "openalex_id": "W2515188070",
          "year": 2016,
          "title": "Culture and Healthy Eating",
          "type": "article",
          "venue": "Personality and Social Psychology Bulletin",
          "cited_by_count": 50,
          "topics": [
            "Cultural Differences and Values",
            "Culinary Culture and Tourism",
            "Behavioral Health and Interventions"
          ]
        },
        {
          "openalex_id": "W4362734922",
          "year": 2023,
          "title": "Corporate governance, compensation mechanisms, and voluntary disclosure of carbon emissions: Evidence from Korea",
          "type": "article",
          "venue": "Journal of Contemporary Accounting & Economics",
          "cited_by_count": 45,
          "topics": [
            "Corporate Social Responsibility Reporting",
            "Environmental Sustainability in Business",
            "Energy, Environment, Economic Growth"
          ]
        }
      ]
    }
  }
]
