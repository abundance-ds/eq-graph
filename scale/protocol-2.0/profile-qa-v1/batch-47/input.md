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
    "name": "Shunya Ikeda",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2013140",
        "title": "A Japanese valuation study for the EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014040",
        "title": "Japanese participation in the MAT-endorsed ranking task",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5064794823",
      "display_name": "Shunya Ikeda",
      "orcid": "0000-0002-1866-2155",
      "reported_affiliation": "Hiroshima University",
      "works_count": 300,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 74
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 30
        },
        {
          "topic": "Pharmacy and Medical Practices",
          "works": 28
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 13
        },
        {
          "topic": "Global Health Care Issues",
          "works": 12
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 12
        },
        {
          "topic": "CAR-T cell therapy research",
          "works": 12
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 11
        },
        {
          "topic": "Vestibular and auditory disorders",
          "works": 11
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 10
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 9
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 9
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Takeru Shiroiwa",
          "works": 31
        },
        {
          "name": "Naoki Ikegami",
          "works": 30
        },
        {
          "name": "Takashi Fukuda",
          "works": 28
        },
        {
          "name": "Koji Wada",
          "works": 20
        },
        {
          "name": "Ataru Igarashi",
          "works": 20
        },
        {
          "name": "Jin Kanzaki",
          "works": 20
        },
        {
          "name": "Kojiro Shimozuma",
          "works": 17
        },
        {
          "name": "Shinichi Noto",
          "works": 16
        },
        {
          "name": "Hiroyuki Sakamaki",
          "works": 16
        },
        {
          "name": "Kaoru Ogawa",
          "works": 15
        },
        {
          "name": "Basilua André Muzembo",
          "works": 14
        },
        {
          "name": "Nlandu Roger Ngatu",
          "works": 14
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7168021990",
          "year": 2026,
          "title": "<p>Kernel density plots of transportation time for each group before and after the COVID-19 pandemic.</p>",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 epidemiological studies",
            "Advanced Queuing Theory Analysis",
            "Point processes and geometric inequalities"
          ]
        },
        {
          "openalex_id": "W7156013677",
          "year": 2026,
          "title": "A small proportion of CD8 T cells expand robustly when stimulated with BCMAxCD3 bispecific T-cell engagers in vitro",
          "type": "article",
          "venue": "Leukemia",
          "cited_by_count": 0,
          "topics": [
            "Monoclonal and Polyclonal Antibodies Research",
            "CAR-T cell therapy research",
            "T-cell and B-cell Immunology"
          ]
        },
        {
          "openalex_id": "W4413481138",
          "year": 2026,
          "title": "Beyond the freedom to refuse patient: A retrospective comparative study of emergency transportation during the COVID-19 pandemic in Japan",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 0,
          "topics": [
            "Disaster Response and Management",
            "Geriatric Care and Nursing Homes",
            "Healthcare Systems and Practices"
          ]
        },
        {
          "openalex_id": "W7133230545",
          "year": 2026,
          "title": "CAR T cells derived from a novel, high-affinity anti-CLL-1 monoclonal antibody exhibit a significant anti-AML effect",
          "type": "article",
          "venue": "Cancer Immunology Immunotherapy",
          "cited_by_count": 0,
          "topics": [
            "CAR-T cell therapy research",
            "CRISPR and Genetic Engineering",
            "Cutaneous lymphoproliferative disorders research"
          ]
        },
        {
          "openalex_id": "W7162695288",
          "year": 2026,
          "title": "Day 7 clinical indicators for predicting discharge destination in patients with prolonged ICU stays: implications for time-limited trials",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Frailty in Older Adults",
            "Acute Kidney Injury Research"
          ]
        },
        {
          "openalex_id": "W7163823425",
          "year": 2026,
          "title": "Effects of multiple tongue conditions on the diversity and composition of the oral microbiota",
          "type": "article",
          "venue": "Journal of Oral Microbiology",
          "cited_by_count": 0,
          "topics": [
            "Traditional Chinese Medicine Studies",
            "Oral microbiology and periodontitis research",
            "Salivary Gland Disorders and Functions"
          ]
        },
        {
          "openalex_id": "W2463238063",
          "year": 1973,
          "title": "[Group discussion: Anxiety of preoperative patients shown in the survey].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Cardiac, Anesthesia and Surgical Outcomes",
            "Music Therapy and Health"
          ]
        },
        {
          "openalex_id": "W2460500058",
          "year": 1975,
          "title": "[Ms. Ida Jean Orlando's nursing theory and my own concepts].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "School Health and Nursing Education"
          ]
        },
        {
          "openalex_id": "W588000130",
          "year": 1989,
          "title": "25 Basic studies on application of two kinds of monoclonal antibodies against endometrial cancer to treatment of cancer.",
          "type": "article",
          "venue": "日本産科婦人科學會雜誌",
          "cited_by_count": 0,
          "topics": [
            "RNA Research and Splicing",
            "Reproductive System and Pregnancy"
          ]
        },
        {
          "openalex_id": "W2333329685",
          "year": 1990,
          "title": "Acute profound deafness related to immunological impairments.",
          "type": "article",
          "venue": "AUDIOLOGY JAPAN",
          "cited_by_count": 0,
          "topics": [
            "Vestibular and auditory disorders"
          ]
        },
        {
          "openalex_id": "W2966611464",
          "year": 2019,
          "title": "The Japanese Society of Hypertension Guidelines for the Management of Hypertension (JSH 2019)",
          "type": "article",
          "venue": "Hypertension Research",
          "cited_by_count": 1875,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Sodium Intake and Health",
            "Nutritional Studies and Diet"
          ]
        },
        {
          "openalex_id": "W2137428285",
          "year": 2011,
          "title": "What has made the population of Japan healthy?",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 677,
          "topics": [
            "Health disparities and outcomes",
            "Global Health Care Issues",
            "Insurance, Mortality, Demography, Risk Management"
          ]
        },
        {
          "openalex_id": "W2153141951",
          "year": 2002,
          "title": "Estimating an EQ‐5D population value set: the case of Japan",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 585,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2086197387",
          "year": 2010,
          "title": "Development of a Database of Health Insurance Claims: Standardization of Disease Classifications and Anonymous Record Linkage",
          "type": "article",
          "venue": "Journal of Epidemiology",
          "cited_by_count": 352,
          "topics": [
            "Medical Coding and Health Information",
            "Data-Driven Disease Surveillance",
            "Machine Learning in Healthcare"
          ]
        },
        {
          "openalex_id": "W1936620973",
          "year": 2015,
          "title": "Japanese population norms for preference-based measures: EQ-5D-3L, EQ-5D-5L, and SF-6D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 341,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W2343671706",
          "year": 2016,
          "title": "Comparison of Value Set Based on DCE and/or TTO Data: Scoring for EQ-5D-5L Health States in Japan",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 320,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W1973443484",
          "year": 2012,
          "title": "Adult Mortality Attributable to Preventable Risk Factors for Non-Communicable Diseases and Injuries in Japan: A Comparative Risk Assessment",
          "type": "article",
          "venue": "PLoS Medicine",
          "cited_by_count": 249,
          "topics": [
            "Health Promotion and Cardiovascular Prevention",
            "Sodium Intake and Health",
            "Blood Pressure and Hypertension Studies"
          ]
        },
        {
          "openalex_id": "W2561287536",
          "year": 2015,
          "title": "Developing a Japanese version of the EQ-5D-5L value set",
          "type": "article",
          "venue": "Hoken iryou kagaku",
          "cited_by_count": 162,
          "topics": [
            "Risk and Safety Analysis",
            "Quality Function Deployment in Product Design",
            "Technology Assessment and Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Simon Pickard",
    "member_affiliation": "University of Illinois - Chicago",
    "is_member": true,
    "projects": [
      {
        "project_id": "2014130",
        "title": "Understanding the relationship between health behaviors, attitudes and perceptions of HRQL using the EQ-5D",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015190",
        "title": "No kidding: the validity of discrete choice experiments in children - a pilot study",
        "working_group": "Youth"
      },
      {
        "project_id": "2016090",
        "title": "Developments in preference-based measures of health: scoring approaches and guidance",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2016210",
        "title": "Measuring concordance between patient and proxy raters of EQ-5D using fuzzy set theory",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016470",
        "title": "US valuation study of the EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180080",
        "title": "Extending the QALY project in the United States – testing the face and content validity of a preliminary list of items",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "20180520",
        "title": "Psychometric assessment of the E-QALY item pool in the United States",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "20190360",
        "title": "Comparison of EQ-5D-3L and 5L value sets/scoring for US users",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190410",
        "title": "US population norms for the EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190800",
        "title": "Measuring and Valuing Patient-Reported Outcomes in Economic Evaluations of Health Care Workshop",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5058888906",
      "display_name": "A. Simon Pickard",
      "orcid": "0000-0001-5645-7091",
      "reported_affiliation": "University of Illinois Chicago",
      "works_count": 304,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 139
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 38
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 30
        },
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 20
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 20
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 18
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 16
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 16
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 14
        },
        {
          "topic": "Opioid Use Disorder Treatment",
          "works": 13
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 11
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 11
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Todd A. Lee",
          "works": 52
        },
        {
          "name": "David Cella",
          "works": 37
        },
        {
          "name": "Maja Kuharić",
          "works": 29
        },
        {
          "name": "Glen T. Schumock",
          "works": 27
        },
        {
          "name": "John Brazier",
          "works": 24
        },
        {
          "name": "Richard Norman",
          "works": 21
        },
        {
          "name": "Rosalie Viney",
          "works": 20
        },
        {
          "name": "Madeleine King",
          "works": 18
        },
        {
          "name": "Lisa K. Sharp",
          "works": 18
        },
        {
          "name": "Ruixuan Jiang",
          "works": 17
        },
        {
          "name": "James W. Shaw",
          "works": 15
        },
        {
          "name": "Feng Xie",
          "works": 15
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166508976",
          "year": 2026,
          "title": "A randomised equivalence study of the EQ-5D-5L Shona versions: evaluation of measurement equivalence between digital and paper formats",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W4413903274",
          "year": 2025,
          "title": "A Randomised Equivalency Study of the EQ-5D-5L Shona Versions - Evaluation of Measurement Equivalency Between Digital and Paper Formats",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4407456299",
          "year": 2025,
          "title": "An Acquired Taste: Latent Class Analysis to Compare Adolescent and Adult Preferences for EQ-5D-Y-3L Health States",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W7116654208",
          "year": 2025,
          "title": "An Eight-Item PROMIS Profile for screen-to-CAT use in clinical practice",
          "type": "article",
          "venue": "Advances in Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Digital Mental Health Interventions",
            "Mobile Health and mHealth Applications",
            "Autism Spectrum Disorder Research"
          ]
        },
        {
          "openalex_id": "W4408418484",
          "year": 2025,
          "title": "Diabetes Screening in the Emergency Department: Development of a Predictive Model for Elevated Hemoglobin A1c",
          "type": "article",
          "venue": "Journal of Diabetes Research",
          "cited_by_count": 0,
          "topics": [
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes Management and Research",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W4412432163",
          "year": 2025,
          "title": "EE496 Long-Term Cost-Effectiveness of a Mobile Health Intervention Delivered by Clinical Pharmacists and Community Health Workers for Type 2 Diabetes Management",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W1965927342",
          "year": 1999,
          "title": "Drug utilization reviews of oral quinolone, cephalosporin, and macrolide use in nonacute care: A systematic review",
          "type": "review",
          "venue": "Clinical Therapeutics",
          "cited_by_count": 7,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pharmaceutical Practices and Patient Outcomes",
            "Healthcare Systems and Technology"
          ]
        },
        {
          "openalex_id": "W56406119",
          "year": 1999,
          "title": "Health status and satisfaction with pharmacy services.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 31,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Pharmaceutical Practices and Patient Outcomes",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W2141821653",
          "year": 1999,
          "title": "Replicability of SF-36 Summary Scores by the SF-12 in Stroke Patients",
          "type": "article",
          "venue": "Stroke",
          "cited_by_count": 121,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2114200373",
          "year": 1999,
          "title": "The Impact of Pharmacist Interventions on Health-Related Quality of Life",
          "type": "article",
          "venue": "Annals of Pharmacotherapy",
          "cited_by_count": 52,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Medication Adherence and Compliance",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2013564592",
          "year": 2012,
          "title": "Interim Scoring for the EQ-5D-5L: Mapping the EQ-5D-5L to EQ-5D-3L Value Sets",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2231,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W2089165963",
          "year": 2012,
          "title": "Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1652,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Education",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2098428600",
          "year": 2007,
          "title": "Estimation of minimally important differences in EQ-5D utility and VAS scores in cancer",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 934,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Lung Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2945409099",
          "year": 2019,
          "title": "United States Valuation of EQ-5D-5L Health States Using an International Protocol",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 399,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2101713088",
          "year": 2007,
          "title": "Health Utilities Using the EQ-5D in Studies of Cancer",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 295,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W2087756930",
          "year": 2000,
          "title": "Comparison of the EQ-5D and SF-12 Health Surveys in a General Population Survey in Alberta, Canada",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 273,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Schizophrenia research and treatment"
          ]
        },
        {
          "openalex_id": "W1970256118",
          "year": 2007,
          "title": "Psychometric Comparison of the Standard EQ-5D to a 5 Level Version in Cancer Patients",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 269,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2021768440",
          "year": 2014,
          "title": "Validity of EQ-5D-5L in stroke",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 267,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Simone Schieskow",
    "member_affiliation": "Bielefeld University, School of Public Health, Department of Health Economics and Health Care Management",
    "is_member": true,
    "projects": [
      {
        "project_id": "20180450",
        "title": "Extending the QALY – Psychometric testing of the items in Germany to support the item selection for the new measure",
        "working_group": "Descriptive Systems, EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5117152200",
      "display_name": "Simone Schieskow",
      "orcid": "",
      "reported_affiliation": "Bielefeld University",
      "works_count": 4,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 3
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 2
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 1
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 1
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 1
        },
        {
          "topic": "Early Childhood Education and Development",
          "works": 1
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 1
        },
        {
          "topic": "Mental Health and Patient Involvement",
          "works": 1
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Michael Herdman",
          "works": 3
        },
        {
          "name": "Janine Verstraete",
          "works": 3
        },
        {
          "name": "Philip A. Powell",
          "works": 2
        },
        {
          "name": "Ling Jie Cheng",
          "works": 1
        },
        {
          "name": "Le Ann Chen",
          "works": 1
        },
        {
          "name": "Jing Ying Cheng",
          "works": 1
        },
        {
          "name": "Nan Luo",
          "works": 1
        },
        {
          "name": "Jennifer Jelsma",
          "works": 1
        },
        {
          "name": "Kim Dalziel",
          "works": 1
        },
        {
          "name": "E. Bidgood",
          "works": 1
        },
        {
          "name": "Fanni Rencz",
          "works": 1
        },
        {
          "name": "J. Carlton",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7147252400",
          "year": 2026,
          "title": "Measuring health-related quality of life in infants and toddlers: conceptual challenges and proposed recommendations",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Infant Development and Preterm Care",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4409450625",
          "year": 2025,
          "title": "Head-to-Head Comparisons of the Distributional Characteristics and Measurement Properties of the 3-Level and 5-Level Versions of the EQ-5D-Y: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 6,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W4416068433",
          "year": 2025,
          "title": "Improving Collaborative Engagement in Health State Valuation: A Scoping Review of Current Practices and Emerging Recommendations",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Mental Health and Patient Involvement",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W4416337963",
          "year": 2025,
          "title": "Multinational stakeholder engagement to inform future development and refinement of the EuroQol toddler and infant populations (EQ-TIPS)",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 2,
          "topics": [
            "Infant Development and Preterm Care",
            "Delphi Technique in Research",
            "Early Childhood Education and Development"
          ]
        }
      ]
    }
  },
  {
    "name": "Soumana Chamoun Nasser",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2585-RA",
        "title": "EQ-HWB-9 and EQ-5D-5L Proxy Assessment in Neuropsychiatric Populations: Validating Patient-Proxy Agreement, Perspective Discordance, and the Role of Caregiver Burden",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5029600163",
      "display_name": "Soumana C. Nasser",
      "orcid": "0000-0003-4202-7116",
      "reported_affiliation": "Lebanese American University",
      "works_count": 38,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 9
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 8
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 6
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 4
        },
        {
          "topic": "Innovations in Medical Education",
          "works": 4
        },
        {
          "topic": "Interprofessional Education and Collaboration",
          "works": 3
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 3
        },
        {
          "topic": "Child Nutrition and Water Access",
          "works": 3
        },
        {
          "topic": "Posttraumatic Stress Disorder Research",
          "works": 2
        },
        {
          "topic": "Anesthesia and Pain Management",
          "works": 2
        },
        {
          "topic": "Pain Management and Opioid Use",
          "works": 2
        },
        {
          "topic": "Pediatric Pain Management Techniques",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Hani Dimassi",
          "works": 8
        },
        {
          "name": "Zeina Mneimneh",
          "works": 4
        },
        {
          "name": "Aimée Karam",
          "works": 4
        },
        {
          "name": "John A. Fayyad",
          "works": 4
        },
        {
          "name": "Elie G. Karam",
          "works": 3
        },
        {
          "name": "Somnath Chatterji",
          "works": 3
        },
        {
          "name": "Ronald C. Kessler",
          "works": 3
        },
        {
          "name": "Nancy Hoffart",
          "works": 3
        },
        {
          "name": "Aline Saad",
          "works": 3
        },
        {
          "name": "Jeanette G. Nassif",
          "works": 3
        },
        {
          "name": "Hanine Mansour",
          "works": 3
        },
        {
          "name": "Hanadi Nahas",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7155100205",
          "year": 2026,
          "title": "Item-Level Convergent and Structural Validity of the EQ-HWB-9 in US Informal Caregivers Compared With ASCOT-Carer, CarerQoL, and EQ-5D-5L",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health and Wellbeing Research",
            "Cancer survivorship and care",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W7117295520",
          "year": 2025,
          "title": "Extent and causes of the collapse in the registration of innovative medications in Lebanon: A mixed-methods analysis",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 1,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Biomedical Ethics and Regulation"
          ]
        },
        {
          "openalex_id": "W4413220821",
          "year": 2025,
          "title": "Extent and causes of the collapse in the registration of innovative medications in Lebanon: A mixed-methods analysis",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W4411179987",
          "year": 2025,
          "title": "Frequency and severity response scales for pain and discomfort: psychometric insights from EQ-HWB",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4417480666",
          "year": 2025,
          "title": "HPR212 Extent and Causes of the Collapse in the Registration of Innovative Medications in Lebanon: A Mixed-Methods Analysis",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W4407881969",
          "year": 2025,
          "title": "Impact of health literacy on healthcare outcomes in hospitalized patients in Lebanon including quality of life and antibiotic knowledge",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 0,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Mobile Health and mHealth Applications",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W1971465143",
          "year": 1988,
          "title": "The Clinical Epidemiology of Acute Diarrhoeal Disease in Egyptian Children",
          "type": "article",
          "venue": "Journal of Tropical Pediatrics",
          "cited_by_count": 5,
          "topics": [
            "Child Nutrition and Water Access",
            "Viral gastroenteritis research and epidemiology"
          ]
        },
        {
          "openalex_id": "W2317040495",
          "year": 1990,
          "title": "Effect of Diarrheal Disease Control on Infant and Childhood Mortality in Egypt",
          "type": "article",
          "venue": "Studies in Family Planning",
          "cited_by_count": 8,
          "topics": [
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W2112689951",
          "year": 1990,
          "title": "Effect of diarrhoeal disease control on infant and childhood mortality in Egypt",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 55,
          "topics": [
            "Child Nutrition and Water Access",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2133680877",
          "year": 2006,
          "title": "Prevalence and treatment of mental disorders in Lebanon: a national epidemiological survey",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 293,
          "topics": [
            "Mental Health Treatment and Access",
            "Posttraumatic Stress Disorder Research",
            "Migration, Health and Trauma"
          ]
        },
        {
          "openalex_id": "W2146637767",
          "year": 2008,
          "title": "Lifetime Prevalence of Mental Disorders in Lebanon: First Onset, Treatment, and Exposure to War",
          "type": "article",
          "venue": "PLoS Medicine",
          "cited_by_count": 278,
          "topics": [
            "Mental Health Treatment and Access",
            "Posttraumatic Stress Disorder Research",
            "Personality Disorders and Psychopathology"
          ]
        },
        {
          "openalex_id": "W2020050705",
          "year": 2010,
          "title": "Clinical and cost impact of intravenous proton pump inhibitor use in non-ICU patients",
          "type": "article",
          "venue": "World Journal of Gastroenterology",
          "cited_by_count": 58,
          "topics": [
            "Nosocomial Infections in ICU",
            "Pressure Ulcer Prevention and Management",
            "Stoma care and complications"
          ]
        },
        {
          "openalex_id": "W2329166502",
          "year": 2016,
          "title": "Student perceptions towards interprofessional education: Findings from a longitudinal study based in a Middle Eastern university",
          "type": "article",
          "venue": "Journal of Interprofessional Care",
          "cited_by_count": 44,
          "topics": [
            "Interprofessional Education and Collaboration",
            "Social Work Education and Practice",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2601899893",
          "year": 2017,
          "title": "Patient Perception of Acute Pain Management: Data from Three Tertiary Care Hospitals",
          "type": "article",
          "venue": "Pain Research and Management",
          "cited_by_count": 39,
          "topics": [
            "Anesthesia and Pain Management",
            "Pain Management and Opioid Use",
            "Pediatric Pain Management Techniques"
          ]
        },
        {
          "openalex_id": "W2808910719",
          "year": 2018,
          "title": "Managed Entry Agreements for Pharmaceutical Products in Middle East and North African Countries: Payer and Manufacturer Experience and Outlook",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 29,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Quality and Counterfeiting"
          ]
        },
        {
          "openalex_id": "W2399162796",
          "year": 2015,
          "title": "Influence of proton pump inhibitors on gastritis diagnosis and pathologic gastric changes",
          "type": "article",
          "venue": "World Journal of Gastroenterology",
          "cited_by_count": 27,
          "topics": [
            "Helicobacter pylori-related gastroenterology studies",
            "Gastroesophageal reflux and treatments",
            "Esophageal Cancer Research and Treatment"
          ]
        }
      ]
    }
  },
  {
    "name": "Stefan Lipman",
    "member_affiliation": "Erasmus School of Health Policy & Management (ESHPM), Erasmus University Rotterdam",
    "is_member": true,
    "projects": [
      {
        "project_id": "120-RA",
        "title": "The role of time and lexicographic preferences in valuation of EQ-5D-Y for health states better and worse than dead.",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1783-RA",
        "title": "Paving the way towards a (potential) pluralistic EQ-5D-Y-5L valuation protocol: mapping out the questions and (lack of) answers",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1992-RA",
        "title": "Whose Health Is It Anyway? Critically considering the role adults take in EQ-5D-Y valuation",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "20190080R1",
        "title": "Correcting bias in time trade-off within the EuroQol Valuation Technology",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190860",
        "title": "Think of the children: rationale for and implications of the perspective in EQ-5D-Y-3L health state valuation",
        "working_group": "Youth"
      },
      {
        "project_id": "20190890",
        "title": "Individual vs. proxy, child vs. adult – A systematic study of different perspectives applied in TTO valuation for EQ-5D-Y",
        "working_group": "Youth"
      },
      {
        "project_id": "205-RA",
        "title": "The role of attention allocation in health state valuation with time trade-off: an exploration of the decision processes underlying correction for prospect theory.",
        "working_group": "Valuation"
      },
      {
        "project_id": "2404-RA",
        "title": "Walk the talk: Would you let your child take part in health state valuation research?",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "245-RA",
        "title": "The search for a task to measure time preference in EQ-5D valuation: systematic review, experiment and application to stand-alone DCE",
        "working_group": "Valuation"
      },
      {
        "project_id": "416-RA",
        "title": "Mind the gap. Psychological distance in EQ-5D-Y valuation",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "417-RA",
        "title": "Comparing (heuristic) valuation processes between EQ-5D valuation from adult and child perspectives",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5078862538",
      "display_name": "Stefan A. Lipman",
      "orcid": "0000-0002-8784-9650",
      "reported_affiliation": "National Institute for Public Health and the Environment",
      "works_count": 57,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 39
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 28
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 20
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 10
        },
        {
          "topic": "Global Health Care Issues",
          "works": 9
        },
        {
          "topic": "Behavioral Health and Interventions",
          "works": 8
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 3
        },
        {
          "topic": "Experimental Behavioral Economics Studies",
          "works": 3
        },
        {
          "topic": "Physical Activity and Health",
          "works": 2
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 2
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 2
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Arthur E. Attema",
          "works": 21
        },
        {
          "name": "Werner Brouwer",
          "works": 7
        },
        {
          "name": "Vivian Reckers‐Droog",
          "works": 6
        },
        {
          "name": "Bram Roudijk",
          "works": 6
        },
        {
          "name": "Zhongyu Lang",
          "works": 6
        },
        {
          "name": "Michał Jakubczyk",
          "works": 5
        },
        {
          "name": "Peep F. M. Stalmeier",
          "works": 4
        },
        {
          "name": "Liying Zhang",
          "works": 4
        },
        {
          "name": "Koonal Shah",
          "works": 3
        },
        {
          "name": "David R. de Buisonjé",
          "works": 3
        },
        {
          "name": "Lisa Tholen",
          "works": 3
        },
        {
          "name": "Ayesha Sajjad",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7127108532",
          "year": 2026,
          "title": "EQ-5D(-Y) Valuation from Adult and Child Perspectives: Where Does the Empirical Evidence Leave Us and How Should We Proceed?",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W7171458555",
          "year": 2026,
          "title": "Employing Psychological Distance to Explain Perspective-Specific EQ-5D-Y-3L Health State Valuation: A Bayesian Hierarchical Analysis",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Behavioral Health and Interventions",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W7127155301",
          "year": 2026,
          "title": "Promoting healthy behaviour with financial incentives: three challenges and solutions for large scale implementation",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Behavioral Health and Interventions",
            "Smoking Behavior and Cessation",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W7141458160",
          "year": 2026,
          "title": "Tailoring through choice: comparing the effect of randomly assigned and self-selected behavioural interventions in promoting healthier snack choice",
          "type": "article",
          "venue": "Behavioural Public Policy",
          "cited_by_count": 0,
          "topics": [
            "Consumer Attitudes and Food Labeling",
            "Behavioral Health and Interventions",
            "Obesity, Physical Activity, Diet"
          ]
        },
        {
          "openalex_id": "W7126028790",
          "year": 2026,
          "title": "Understanding consumption of animal- and plant-based protein sources in the Netherlands: A stakeholder-driven causal loop diagram",
          "type": "article",
          "venue": "Appetite",
          "cited_by_count": 0,
          "topics": [
            "Agriculture Sustainability and Environmental Impact",
            "Organic Food and Agriculture",
            "Food Waste Reduction and Sustainability"
          ]
        },
        {
          "openalex_id": "W4412572730",
          "year": 2025,
          "title": "Assessing a dire fate: Standard gamble and time trade-off utilities for states worse than dead",
          "type": "article",
          "venue": "Theory and Decision",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2508936053",
          "year": 2016,
          "title": "Nudge vs. Habit - Moderating effects of habit strength on nudges’ effectiveness in reducing unhealthy snacking",
          "type": "dissertation",
          "venue": "Utrecht University Repository (Utrecht University)",
          "cited_by_count": 0,
          "topics": [
            "Consumer Retail Behavior Studies",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W2780267256",
          "year": 2017,
          "title": "Lipman Burt (2017) Pest prevalence HBM",
          "type": "preprint",
          "venue": "OSF Preprints (OSF Preprints)",
          "cited_by_count": 0,
          "topics": [
            "Mosquito-borne diseases and control"
          ]
        },
        {
          "openalex_id": "W2966796747",
          "year": 2017,
          "title": "QALYs Without Bias? Non-Parametric Correction of Time Trade-Off and Standard Gamble Weights Based on Prospect Theory",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 5,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2776948689",
          "year": 2017,
          "title": "Self-reported prevalence of pests in Dutch households and the use of the health belief model to explore householders’ intentions to engage in pest control",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 10,
          "topics": [
            "Behavioral Health and Interventions",
            "Urban Green Space and Health",
            "Environmental Education and Sustainability"
          ]
        },
        {
          "openalex_id": "W3155891196",
          "year": 2021,
          "title": "Think of the Children: A Discussion of the Rationale for and Implications of the Perspective Used for EQ-5D-Y Health State Valuation",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W3116333528",
          "year": 2020,
          "title": "Time for Tele-TTO? Lessons Learned From Digital Interviewer-Assisted Time Trade-Off Data Collection",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 53,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Housing Market and Economics"
          ]
        },
        {
          "openalex_id": "W4304080516",
          "year": 2022,
          "title": "A Value Set for the EQ-5D-Y-3L in the Netherlands",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W4367669495",
          "year": 2023,
          "title": "Taking the Shortcut: Simplifying Heuristics in Discrete Choice Experiments",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 47,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4211054812",
          "year": 2022,
          "title": "Why Do Adults Value EQ-5D-Y-3L Health States Differently for Themselves Than for Children and Adolescents: A Think-Aloud Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 47,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W3202443669",
          "year": 2021,
          "title": "Self vs. other, child vs. adult. An experimental comparison of valuation perspectives for valuation of EQ-5D-Y-3L health states",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 46,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4281255993",
          "year": 2022,
          "title": "Time and lexicographic preferences in the valuation of EQ-5D-Y with time trade-off methodology",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 21,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W3036143002",
          "year": 2020,
          "title": "One size fits all? Designing financial incentives tailored to individual economic preferences",
          "type": "article",
          "venue": "Behavioural Public Policy",
          "cited_by_count": 20,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Behavioral Health and Interventions",
            "Experimental Behavioral Economics Studies"
          ]
        }
      ]
    }
  }
]
