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
    "name": "Thao Thai",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1797-RA",
        "title": "Head-to-Head Comparison of the Psychometric Performance of the EQ-HWB, EQ-5D-5L, and Re-QoL in the general population and people with mental health problems",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1887-RA",
        "title": "Testing a modified version of the EQ-HWB-S among the general public in Australia",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "1896-RA",
        "title": "Psychometric Performance of the EQ-HWB in Individual with Culturally and Linguistically Diverse Background",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5050171927",
      "display_name": "Thao Phuong Thi Thai",
      "orcid": "",
      "reported_affiliation": "",
      "works_count": 8,
      "top_topics": [
        {
          "topic": "Global Maternal and Child Health",
          "works": 2
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 2
        },
        {
          "topic": "HIV/AIDS drug development and treatment",
          "works": 2
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 2
        },
        {
          "topic": "Mosquito-borne diseases and control",
          "works": 1
        },
        {
          "topic": "Dengue and Mosquito Control Research",
          "works": 1
        },
        {
          "topic": "HIV Research and Treatment",
          "works": 1
        },
        {
          "topic": "Cardiac Health and Mental Health",
          "works": 1
        },
        {
          "topic": "Cardiovascular Health and Risk Factors",
          "works": 1
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 1
        },
        {
          "topic": "Mobile Health and mHealth Applications",
          "works": 1
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bach Xuan Tran",
          "works": 6
        },
        {
          "name": "Carl A. Latkin",
          "works": 6
        },
        {
          "name": "Cyrus S. H. Ho",
          "works": 5
        },
        {
          "name": "Roger Ho",
          "works": 5
        },
        {
          "name": "Long Hoang Nguyen",
          "works": 4
        },
        {
          "name": "Cuong Tat Nguyen",
          "works": 3
        },
        {
          "name": "Giang Thu Vu",
          "works": 2
        },
        {
          "name": "Tung Thanh Tran",
          "works": 2
        },
        {
          "name": "Nu Thi Truong",
          "works": 2
        },
        {
          "name": "Thu Hong Thi Nguyen",
          "works": 2
        },
        {
          "name": "Trang Huyen Thi Nguyen",
          "works": 2
        },
        {
          "name": "Anh Tuan Nguyen",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W3031634496",
          "year": 2020,
          "title": "Impacts of Media Multitasking on Advertising Effectiveness - The moderating role of Sexual Advertising Appeal",
          "type": "dissertation",
          "venue": "Aaltodoc (Aalto University)",
          "cited_by_count": 0,
          "topics": [
            "Consumer Perception and Purchasing Behavior",
            "Diverse Topics in Contemporary Research",
            "Asian Culture and Media Studies"
          ]
        },
        {
          "openalex_id": "W2914220456",
          "year": 2019,
          "title": "&lt;p&gt;Catastrophic health expenditure of Vietnamese patients with gallstone diseases &amp;ndash; a case for health insurance policy revaluation&lt;/p&gt;",
          "type": "article",
          "venue": "ClinicoEconomics and Outcomes Research",
          "cited_by_count": 8,
          "topics": [
            "Gallbladder and Bile Duct Disorders",
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2984878246",
          "year": 2019,
          "title": "Predictors of Self-Efficacy and Health-Related Outcomes in Community-Dwelling Stroke Survivors",
          "type": "conference-abstract",
          "venue": "American Journal of Occupational Therapy",
          "cited_by_count": 2,
          "topics": [
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W2914110704",
          "year": 2019,
          "title": "Stigma against patients with HIV/AIDS in the rapid expansion of antiretroviral treatment in large drug injection-driven HIV epidemics of Vietnam",
          "type": "article",
          "venue": "Harm Reduction Journal",
          "cited_by_count": 41,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV Research and Treatment",
            "HIV/AIDS drug development and treatment"
          ]
        },
        {
          "openalex_id": "W2896600966",
          "year": 2018,
          "title": "Adherence to antiretroviral therapy among HIV/AIDS patients in the context of early treatment initiation in Vietnam",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 23,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV/AIDS drug development and treatment",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W2807293003",
          "year": 2018,
          "title": "Cost-of-Illness and the Health-Related Quality of Life of Patients in the Dengue Fever Outbreak in Hanoi in 2017",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 45,
          "topics": [
            "Mosquito-borne diseases and control",
            "Global Maternal and Child Health",
            "Dengue and Mosquito Control Research"
          ]
        },
        {
          "openalex_id": "W2898266166",
          "year": 2018,
          "title": "Demand and willingness to pay for different treatment and care services among patients with heart diseases in Hanoi, Vietnam",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 10,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2894511580",
          "year": 2018,
          "title": "Socioeconomic Inequalities in Health-Related Quality of Life among Patients with Cardiovascular Diseases in Vietnam",
          "type": "article",
          "venue": "BioMed Research International",
          "cited_by_count": 34,
          "topics": [
            "Cardiac Health and Mental Health",
            "Cardiovascular Health and Risk Factors",
            "Diabetes Management and Education"
          ]
        }
      ]
    }
  },
  {
    "name": "thomas kohlmann",
    "member_affiliation": "University of Greifswald",
    "is_member": true,
    "projects": [
      {
        "project_id": "20170130",
        "title": "Scoring Methods for the EQ-5D instrument: theoretical background and empirical analyses (revised application)",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5031953969",
      "display_name": "Thomas Kohlmann",
      "orcid": "0000-0002-5956-8309",
      "reported_affiliation": "Universitätsmedizin Greifswald",
      "works_count": 427,
      "top_topics": [
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 66
        },
        {
          "topic": "Health and Medical Studies",
          "works": 53
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 44
        },
        {
          "topic": "Medical Practices and Rehabilitation",
          "works": 41
        },
        {
          "topic": "Fibromyalgia and Chronic Fatigue Syndrome Research",
          "works": 26
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 24
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 13
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 12
        },
        {
          "topic": "Biomedical and Chemical Research",
          "works": 12
        },
        {
          "topic": "Infection Control in Healthcare",
          "works": 12
        },
        {
          "topic": "Growth Hormone and Insulin-like Growth Factors",
          "works": 11
        },
        {
          "topic": "Pancreatitis Pathology and Treatment",
          "works": 11
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jörn Moock",
          "works": 35
        },
        {
          "name": "Axel Krämer",
          "works": 26
        },
        {
          "name": "Carsten Oliver Schmidt",
          "works": 25
        },
        {
          "name": "Markus M. Lerch",
          "works": 25
        },
        {
          "name": "You‐Shan Feng",
          "works": 24
        },
        {
          "name": "Julia Mayerle",
          "works": 24
        },
        {
          "name": "Georg Beyer",
          "works": 24
        },
        {
          "name": "Henry Völzke",
          "works": 23
        },
        {
          "name": "Ralf Ohlinger",
          "works": 23
        },
        {
          "name": "Matthias Nauck",
          "works": 22
        },
        {
          "name": "Gabriele Lindena",
          "works": 22
        },
        {
          "name": "Marek Zygmunt",
          "works": 22
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7119515457",
          "year": 2026,
          "title": "Konzepte der elterlichen Entscheidungsfindung zur Inanspruchnahme von Impfungen – eine qualitative Interviewstudie",
          "type": "article",
          "venue": "Prävention und Gesundheitsförderung",
          "cited_by_count": 0,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "Virology and Viral Diseases",
            "Diphtheria, Corynebacterium, and Tetanus"
          ]
        },
        {
          "openalex_id": "W7153847944",
          "year": 2026,
          "title": "Understanding Preference Heterogeneity in Digital Neurorehabilitation: Results of a Discrete Choice Experiment",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Spatial Neglect and Hemispheric Dysfunction",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W7140043310",
          "year": 2026,
          "title": "Unraveling acceptance of healthcare innovations in neurorehabilitation: results from a discrete choice experiment",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 2,
          "topics": [
            "Economic and Environmental Valuation",
            "Assistive Technology in Communication and Mobility",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4415940515",
          "year": 2025,
          "title": "2366P Patient-relevance of the endpoint time to subsequent therapy (TTST): Development of a standardised checklist for documentation in clinical trials",
          "type": "article",
          "venue": "Annals of Oncology",
          "cited_by_count": 0,
          "topics": [
            "Clinical practice guidelines implementation",
            "Psychiatric care and mental health services",
            "Meta-analysis and systematic reviews"
          ]
        },
        {
          "openalex_id": "W7125978971",
          "year": 2025,
          "title": "Effect of proton pump inhibitors on occlusion of lumen-apposing metal stents and rate of endoscopic necrosectomies: a Europe-wide multicenter cohort study",
          "type": "article",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": [
            "Esophageal and GI Pathology",
            "Gastrointestinal Bleeding Diagnosis and Treatment",
            "Gallbladder and Bile Duct Disorders"
          ]
        },
        {
          "openalex_id": "W4409458530",
          "year": 2025,
          "title": "Evaluating an early Interdisciplinary Multimodal Assessment for Patients at Risk of Developing Chronic Pain: Results of a Multicentre RCT in Germany",
          "type": "article",
          "venue": "Pain and Therapy",
          "cited_by_count": 5,
          "topics": [
            "Pediatric Pain Management Techniques",
            "Musculoskeletal pain and rehabilitation",
            "Pain Management and Opioid Use"
          ]
        },
        {
          "openalex_id": "W2464178211",
          "year": 1952,
          "title": "[Studies of psychological function in dementia].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Psychosomatic Disorders and Their Treatments"
          ]
        },
        {
          "openalex_id": "W2444480673",
          "year": 1954,
          "title": "[Clinical and ergopsychological examination of the effect of lecithin in biomalz with reference to the increase of individual activity].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Neurological Disorders and Treatments",
            "Myofascial pain diagnosis and treatment",
            "Medical and Biological Ozone Research"
          ]
        },
        {
          "openalex_id": "W573963166",
          "year": 1975,
          "title": "DER FUNKTIONELL-PSYCHOTISCHE INTELLIGENZABBAU DER SCHIZOPHRENIE UND DAS PROBLEM DER REHABILITATION DIESER",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Psychoanalysis and Social Critique",
            "Psychiatric care and mental health services",
            "Psychology, Coaching, and Therapy"
          ]
        },
        {
          "openalex_id": "W2555444216",
          "year": 1988,
          "title": "Health Lifestyles: A Comparative Approach to the Culture of Health Concept",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 6,
          "topics": [
            "Nutrition, Genetics, and Disease"
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
          "openalex_id": "W2131014997",
          "year": 2010,
          "title": "Cohort Profile: The Study of Health in Pomerania",
          "type": "article",
          "venue": "International Journal of Epidemiology",
          "cited_by_count": 1015,
          "topics": [
            "Health and Medical Studies",
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W3111512677",
          "year": 2020,
          "title": "Psychometric properties of the EQ-5D-5L: a systematic review of the literature",
          "type": "review",
          "venue": "Quality of Life Research",
          "cited_by_count": 940,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W2119408292",
          "year": 2014,
          "title": "Systematic literature review and validity evaluation of the Expanded Disability Status Scale (EDSS) and the Multiple Sclerosis Functional Composite (MSFC) in patients with multiple sclerosis",
          "type": "review",
          "venue": "BMC Neurology",
          "cited_by_count": 634,
          "topics": [
            "Multiple Sclerosis Research Studies",
            "Amyotrophic Lateral Sclerosis Research",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W2105241989",
          "year": 2008,
          "title": "Costs of back pain in Germany",
          "type": "article",
          "venue": "European Journal of Pain",
          "cited_by_count": 440,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Fibromyalgia and Chronic Fatigue Syndrome Research"
          ]
        },
        {
          "openalex_id": "W2054317102",
          "year": 2008,
          "title": "When to use the odds ratio or the relative risk?",
          "type": "article",
          "venue": "Sozial- und Präventivmedizin",
          "cited_by_count": 440,
          "topics": [
            "Advanced Causal Inference Techniques",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W1981336961",
          "year": 2007,
          "title": "Back Pain in the German Adult Population",
          "type": "article",
          "venue": "Spine",
          "cited_by_count": 384,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Occupational Health and Performance",
            "Health and Medical Studies"
          ]
        },
        {
          "openalex_id": "W2109103145",
          "year": 2005,
          "title": "Clinical features of heparin-induced thrombocytopenia including risk factors for thrombosis",
          "type": "article",
          "venue": "Thrombosis and Haemostasis",
          "cited_by_count": 380,
          "topics": [
            "Heparin-Induced Thrombocytopenia and Thrombosis",
            "Venous Thromboembolism Diagnosis and Management",
            "Case Reports on Hematomas"
          ]
        }
      ]
    }
  },
  {
    "name": "Tianxin Pan",
    "member_affiliation": "",
    "is_member": true,
    "projects": [
      {
        "project_id": "1472-PD",
        "title": "Understanding the transition between EuroQol instruments for use in children and adolescents",
        "working_group": "Youth"
      },
      {
        "project_id": "2284-BT",
        "title": "Validation of multiple EQ-5D Bolt-on Toolbox bolt-ons in older adults in China",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "233-RA",
        "title": "Exploring the use of EQ-5D-3L in measuring population health and studying health inequalities in China: evidence from National Health Services Surveys (2008, 2013 and 2018)",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2347-RA",
        "title": "A systematic review of social relationships bolt-on",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "428-RA",
        "title": "Understanding the ceiling effects phenomenon of EQ-5D instruments: a systematic investigation into possible reasons, existing evidence, and future research directions and priorities",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5044860561",
      "display_name": "Tianxin Pan",
      "orcid": "0000-0002-2243-8818",
      "reported_affiliation": "The University of Melbourne",
      "works_count": 50,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 20
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 9
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 7
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 7
        },
        {
          "topic": "Global Health Care Issues",
          "works": 7
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 5
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 5
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 5
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 4
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 3
        },
        {
          "topic": "Employment and Welfare Studies",
          "works": 3
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nancy Devlin",
          "works": 20
        },
        {
          "name": "Richard Norman",
          "works": 13
        },
        {
          "name": "Barbara McPake",
          "works": 10
        },
        {
          "name": "Brendan Mulhern",
          "works": 9
        },
        {
          "name": "John Tayu Lee",
          "works": 8
        },
        {
          "name": "Yang Zhao",
          "works": 7
        },
        {
          "name": "Ilias Goranitis",
          "works": 7
        },
        {
          "name": "Rifat Atun",
          "works": 6
        },
        {
          "name": "Kim Dalziel",
          "works": 5
        },
        {
          "name": "Rosalie Viney",
          "works": 5
        },
        {
          "name": "Tiara Marthias",
          "works": 4
        },
        {
          "name": "Kanya Anindya",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7155180776",
          "year": 2026,
          "title": "Correction: Public Preferences and Willingness to Pay for a Multidisciplinary Colorectal and Pelvic Reconstruction Service",
          "type": "erratum",
          "venue": "Patient",
          "cited_by_count": 0,
          "topics": [
            "Pelvic floor disorders treatments",
            "Congenital gastrointestinal and neural anomalies",
            "Ureteral procedures and complications"
          ]
        },
        {
          "openalex_id": "W7128772625",
          "year": 2026,
          "title": "Health-related quality of life of children born with very low birth weight and their caregivers in China: a cross-sectional survey",
          "type": "article",
          "venue": "Translational Pediatrics",
          "cited_by_count": 0,
          "topics": [
            "Infant Development and Preterm Care",
            "Neonatal Respiratory Health Research",
            "Birth, Development, and Health"
          ]
        },
        {
          "openalex_id": "W7125701987",
          "year": 2026,
          "title": "Proxy-reported health-related quality of life in children with omphalocele: a cross-sectional study in China",
          "type": "article",
          "venue": "Translational Pediatrics",
          "cited_by_count": 0,
          "topics": [
            "Congenital Anomalies and Fetal Surgery",
            "Urological Disorders and Treatments",
            "Urinary and Genital Oncology Studies"
          ]
        },
        {
          "openalex_id": "W7159985003",
          "year": 2026,
          "title": "The validation of the CarerQol instrument and factors associated with quality of life among informal caregivers of disabled older adults in China",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Intergenerational Family Dynamics and Caregiving",
            "Health and Wellbeing Research",
            "Family and Disability Support Research"
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
          "openalex_id": "W4412410621",
          "year": 2025,
          "title": "An Australian Value Set for the EQ-5D-Y-3L",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2587256744",
          "year": 2017,
          "title": "Risk Factors and NCDs in China: A Longitudinal Study",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Energy and Environment Impacts"
          ]
        },
        {
          "openalex_id": "W2796448844",
          "year": 2018,
          "title": "Risk factors and non-communicable disease diagnosis in China",
          "type": "article",
          "venue": "China Economic Review",
          "cited_by_count": 4,
          "topics": [
            "Energy and Environment Impacts",
            "Global Public Health Policies and Epidemiology",
            "Obesity, Physical Activity, Diet"
          ]
        },
        {
          "openalex_id": "W2914543834",
          "year": 2018,
          "title": "Risk factors and non-communicable disease diagnosis in China",
          "type": "report",
          "venue": "Munich Personal RePEc Archive (Ludwig Maximilian University of Munich)",
          "cited_by_count": 0,
          "topics": [
            "Energy and Environment Impacts",
            "Energy, Environment, Economic Growth",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W3093902339",
          "year": 2019,
          "title": "The Economic Impact of Non-communicable Diseases on Household Welfare in China",
          "type": "dissertation",
          "venue": "Minerva Access (University of Melbourne)",
          "cited_by_count": 0,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Global Health Care Issues",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W3132327386",
          "year": 2021,
          "title": "Impact of non-communicable disease multimorbidity on health service use, catastrophic health expenditure and productivity loss in Indonesia: a population-based panel data analysis study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 76,
          "topics": [
            "Chronic Disease Management Strategies",
            "Healthcare Systems and Reforms",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W3130230332",
          "year": 2021,
          "title": "Medical costs and out-of-pocket expenditures associated with multimorbidity in China: quantile regression analysis",
          "type": "article",
          "venue": "BMJ Global Health",
          "cited_by_count": 57,
          "topics": [
            "Chronic Disease Management Strategies",
            "Healthcare Systems and Reforms",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W3158519958",
          "year": 2021,
          "title": "Effect of multimorbidity on utilisation and out-of-pocket expenditure in Indonesia: quantile regression analysis",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 51,
          "topics": [
            "Chronic Disease Management Strategies",
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W4284892570",
          "year": 2022,
          "title": "Valuing EQ-5D-Y: the current state of play",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 50,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Early Childhood Education and Development",
            "Child and Animal Learning Development"
          ]
        },
        {
          "openalex_id": "W4392764911",
          "year": 2024,
          "title": "The Ceiling Effects of EQ-5D-3L and 5L in General Population Health Surveys: A Systematic Review and Meta-Analysis",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W3214654466",
          "year": 2021,
          "title": "Plasma neurofilament light chain protein is not increased in treatment-resistant schizophrenia and first-degree relatives",
          "type": "article",
          "venue": "Australian & New Zealand Journal of Psychiatry",
          "cited_by_count": 36,
          "topics": [
            "Alzheimer's disease research and treatments",
            "Neurogenesis and neuroplasticity mechanisms",
            "Tryptophan and brain disorders"
          ]
        },
        {
          "openalex_id": "W4210634802",
          "year": 2022,
          "title": "The relationship between physical and mental health multimorbidity and children’s health-related quality of life",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 35,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Child and Adolescent Psychosocial and Emotional Development",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W3106700432",
          "year": 2020,
          "title": "The clinical utility of exome sequencing and extended bioinformatic analyses in adolescents and adults with a broad range of neurological phenotypes: an Australian perspective",
          "type": "article",
          "venue": "Journal of the Neurological Sciences",
          "cited_by_count": 32,
          "topics": [
            "Genomics and Rare Diseases",
            "Genetic Neurodegenerative Diseases",
            "Genetics and Neurodevelopmental Disorders"
          ]
        }
      ]
    }
  },
  {
    "name": "Tie Parma Yamato",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "218-RA",
        "title": "Analysis of the measurement properties of the Brazilian-Portuguese version of the health-related quality of life instruments EQ-5D-Y-3L and EQ-5D-Y-5L in children and adolescents",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "220-VS",
        "title": "The development of the national value set for the EQ-5D-Y-3L in Brazil",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5034831401",
      "display_name": "Tiê Parma Yamato",
      "orcid": "0000-0002-5228-1292",
      "reported_affiliation": "The University of Sydney",
      "works_count": 112,
      "top_topics": [
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 44
        },
        {
          "topic": "Occupational Health and Performance",
          "works": 29
        },
        {
          "topic": "Sports injuries and prevention",
          "works": 20
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 20
        },
        {
          "topic": "Pediatric Pain Management Techniques",
          "works": 20
        },
        {
          "topic": "Lower Extremity Biomechanics and Pathologies",
          "works": 12
        },
        {
          "topic": "Injury Epidemiology and Prevention",
          "works": 11
        },
        {
          "topic": "Health Sciences Research and Education",
          "works": 8
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 7
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 6
        },
        {
          "topic": "Pain Management and Placebo Effect",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bruno Tirotti Saragiotto",
          "works": 65
        },
        {
          "name": "Christopher G. Maher",
          "works": 47
        },
        {
          "name": "Steven J. Kamper",
          "works": 28
        },
        {
          "name": "Leonardo Oliveira Pena Costa",
          "works": 23
        },
        {
          "name": "Anne M. Moseley",
          "works": 21
        },
        {
          "name": "Tammy Hoffmann",
          "works": 18
        },
        {
          "name": "Verônica Souza Santos",
          "works": 18
        },
        {
          "name": "Mark R. Elkins",
          "works": 17
        },
        {
          "name": "Christopher Williams",
          "works": 14
        },
        {
          "name": "Mariana Nascimento Leite",
          "works": 13
        },
        {
          "name": "Alexandre Días Lópes",
          "works": 12
        },
        {
          "name": "Gisela Cristiane Miyamoto",
          "works": 11
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4409388160",
          "year": 2025,
          "title": "Comparing the measurement properties of the EQ-5D-Y-3L, EQ-5D-Y-5L and CHU9D in children and adolescents: a measurement property study",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cerebral Palsy and Movement Disorders",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W4415706092",
          "year": 2025,
          "title": "Effectiveness and Cost-effectiveness of an Internet-Based Self-management Program for People With Chronic Pain: A Randomized Controlled Trial With Economic Evaluation (the ReabilitaDOR Trial)",
          "type": "article",
          "venue": "Journal of Orthopaedic and Sports Physical Therapy",
          "cited_by_count": 0,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Diabetes Management and Education",
            "Total Knee Arthroplasty Outcomes"
          ]
        },
        {
          "openalex_id": "W4409591589",
          "year": 2025,
          "title": "Measurement Properties of the EQ-5D Instruments in Children and Adolescents: A Systematic Review",
          "type": "review",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W7165117714",
          "year": 2025,
          "title": "Pain Concept Questionnaire for adolescents: comprehensibility and measurement properties",
          "type": "other",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4413108556",
          "year": 2025,
          "title": "Telerehabilitation for neck pain",
          "type": "article",
          "venue": "Cochrane Database of Systematic Reviews",
          "cited_by_count": 2,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Musculoskeletal pain and rehabilitation",
            "Pain Management and Treatment"
          ]
        },
        {
          "openalex_id": "W4404721350",
          "year": 2024,
          "title": "Adolescents' understanding of pain and their preferences for learning about pain at school: a cross-sectional survey.",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 1,
          "topics": [
            "Pediatric Pain Management Techniques",
            "Empathy and Medical Education",
            "Pain Management and Placebo Effect"
          ]
        },
        {
          "openalex_id": "W2401953938",
          "year": 1978,
          "title": "[Survey on the living conditions and attitudes of pregnant women].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Ethics in medical practice"
          ]
        },
        {
          "openalex_id": "W2094510669",
          "year": 2009,
          "title": "MP-05.11: Strategy to Interest Women Medical Students in Urology: Proposal of the Society of Female Urologists in Japan (SFUJ)",
          "type": "conference-abstract",
          "venue": "Urology",
          "cited_by_count": 0,
          "topics": [
            "Global Health Workforce Issues",
            "Diversity and Career in Medicine"
          ]
        },
        {
          "openalex_id": "W2107598256",
          "year": 2011,
          "title": "Musculoskeletal pain in recreational runners prior to race participation: a cross-sectional survey in 1049 runners",
          "type": "article",
          "venue": "British Journal of Sports Medicine",
          "cited_by_count": 0,
          "topics": [
            "Sports injuries and prevention",
            "Occupational Health and Performance",
            "Sports Performance and Training"
          ]
        },
        {
          "openalex_id": "W2148249748",
          "year": 2011,
          "title": "Musculoskeletal pain is prevalent among recreational runners who are about to compete: an observational study of 1049 runners",
          "type": "article",
          "venue": "Journal of physiotherapy",
          "cited_by_count": 40,
          "topics": [
            "Lower Extremity Biomechanics and Pathologies",
            "Occupational Health and Performance",
            "Sports injuries and prevention"
          ]
        },
        {
          "openalex_id": "W2227323785",
          "year": 2016,
          "title": "Motor control exercise for chronic non-specific low-back pain",
          "type": "article",
          "venue": "Cochrane Database of Systematic Reviews",
          "cited_by_count": 421,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Ergonomics and Musculoskeletal Disorders",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W2745599707",
          "year": 2017,
          "title": "Knee osteoarthritis phenotypes and their relevance for outcomes: a systematic review",
          "type": "review",
          "venue": "Osteoarthritis and Cartilage",
          "cited_by_count": 330,
          "topics": [
            "Osteoarthritis Treatment and Mechanisms",
            "Total Knee Arthroplasty Outcomes",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W3199777986",
          "year": 2021,
          "title": "Some types of exercise are more effective than others in people with chronic low back pain: a network meta-analysis",
          "type": "article",
          "venue": "Journal of physiotherapy",
          "cited_by_count": 322,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Myofascial pain diagnosis and treatment"
          ]
        },
        {
          "openalex_id": "W2047122567",
          "year": 2014,
          "title": "What are the Main Risk Factors for Running-Related Injuries?",
          "type": "article",
          "venue": "Sports Medicine",
          "cited_by_count": 281,
          "topics": [
            "Lower Extremity Biomechanics and Pathologies",
            "Occupational Health and Performance",
            "Injury Epidemiology and Prevention"
          ]
        },
        {
          "openalex_id": "W2049024707",
          "year": 2015,
          "title": "A Consensus Definition of Running-Related Injury in Recreational Runners: A Modified Delphi Approach",
          "type": "article",
          "venue": "Journal of Orthopaedic and Sports Physical Therapy",
          "cited_by_count": 261,
          "topics": [
            "Lower Extremity Biomechanics and Pathologies",
            "Sports injuries and prevention",
            "Foot and Ankle Surgery"
          ]
        },
        {
          "openalex_id": "W2344966246",
          "year": 2016,
          "title": "Motor Control Exercise for Nonspecific Low Back Pain",
          "type": "article",
          "venue": "Spine",
          "cited_by_count": 177,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Occupational Health and Performance",
            "Sports injuries and prevention"
          ]
        },
        {
          "openalex_id": "W2593715723",
          "year": 2017,
          "title": "The PEDro scale had acceptably high convergent validity, construct validity, and interrater reliability in evaluating methodological quality of pharmaceutical trials",
          "type": "article",
          "venue": "Journal of Clinical Epidemiology",
          "cited_by_count": 174,
          "topics": [
            "Meta-analysis and systematic reviews",
            "Advanced Causal Inference Techniques",
            "Reliability and Agreement in Measurement"
          ]
        },
        {
          "openalex_id": "W2623384351",
          "year": 2016,
          "title": "The prevalence, risk factors, prognosis and treatment for back pain in children and adolescents: An overview of systematic reviews",
          "type": "review",
          "venue": "Best Practice & Research Clinical Rheumatology",
          "cited_by_count": 154,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Occupational Health and Performance",
            "School Health and Nursing Education"
          ]
        }
      ]
    }
  },
  {
    "name": "Titi Fitriana",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20180490",
        "title": "Test of the minimal number of C-TTO states in the valuation protocol of the EQ-5D-3L-Y",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "20200010",
        "title": "Describing the Worse than Dead in Youth Valuation",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2444-RA",
        "title": "Extending the use of EQ-5D-Y-5L to Younger Children: Testing Comprehensibility and Interviewer-Assisted Administration in Indonesia",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5049547434",
      "display_name": "Titi Sahidah Fitriana",
      "orcid": "0000-0001-5062-6886",
      "reported_affiliation": "Yarsi University",
      "works_count": 18,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 9
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 3
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 2
        },
        {
          "topic": "Behavioral and Psychological Studies",
          "works": 2
        },
        {
          "topic": "Educational Methods and Impacts",
          "works": 2
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 1
        },
        {
          "topic": "HER2/EGFR in Cancer Research",
          "works": 1
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 1
        },
        {
          "topic": "Health Education and Validation",
          "works": 1
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 1
        },
        {
          "topic": "Intergenerational Family Dynamics and Caregiving",
          "works": 1
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Fredrick Dermawan Purba",
          "works": 11
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 10
        },
        {
          "name": "Joke A. M. Hunfeld",
          "works": 5
        },
        {
          "name": "Aulia Iskandarsyah",
          "works": 5
        },
        {
          "name": "Sawitri S. Sadarjoen",
          "works": 5
        },
        {
          "name": "Jan Passchier",
          "works": 5
        },
        {
          "name": "Elly Stolk",
          "works": 5
        },
        {
          "name": "Rina Rahmatika",
          "works": 2
        },
        {
          "name": "Juan Manuel Ramos-Goñi",
          "works": 1
        },
        {
          "name": "Riski Muhaimin",
          "works": 1
        },
        {
          "name": "Nur Melani Sari",
          "works": 1
        },
        {
          "name": "Gouke J. Bonsel",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4410230033",
          "year": 2025,
          "title": "Adaptation of the Experimental Version of EQ-5D-Y-5L Into Bahasa Indonesia",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Behavioral and Psychological Studies",
            "Simulation-Based Education in Healthcare"
          ]
        },
        {
          "openalex_id": "W7169715303",
          "year": 2025,
          "title": "Psychometric Test of the Routine Exercise Intention Measurement Tool",
          "type": "conference-paper",
          "venue": "Proceedings of The International Conference on Psychology and Education",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4407180061",
          "year": 2024,
          "title": "THE RELATIONSHIP BETWEEN SOCIO-ECONOMIC AND MEDIA LITERACY LEVELS WITH THE LEVEL OF PARENT PARTICIPATION IN PREVENTING STUNTING IN RURAL AREAS",
          "type": "article",
          "venue": "Sosiohumaniora",
          "cited_by_count": 3,
          "topics": [
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W4382812608",
          "year": 2023,
          "title": "Hypocenter Relocation of Local Earthquake using Double Difference Method in Central Sulawesi from BMKG Network Data: Time Periods of July 26 - August 18, 2021",
          "type": "conference-paper",
          "venue": "IOP Conference Series Earth and Environmental Science",
          "cited_by_count": 3,
          "topics": [
            "earthquake and tectonic studies",
            "High-pressure geophysics and materials",
            "Earthquake Detection and Analysis"
          ]
        },
        {
          "openalex_id": "W4380422518",
          "year": 2023,
          "title": "Indonesia youth population norms for EQ-5D-Y-3 L, EQ-5D-Y-5 L and the PedsQL generic core scale: lower health related quality of life relates to high economic status and stress",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 8,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4281702460",
          "year": 2022,
          "title": "EQ-5D-Y-3L and EQ-5D-Y-5L proxy report: psychometric performance and agreement with self-report",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 27,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W4247020886",
          "year": 2013,
          "title": "Understanding prostitutes life in Indonesia",
          "type": "dataset",
          "venue": "PsycEXTRA Dataset",
          "cited_by_count": 0,
          "topics": [
            "Asian Studies and History",
            "Sex work and related issues"
          ]
        },
        {
          "openalex_id": "W2460279540",
          "year": 2015,
          "title": "INTERVENSI DENGAN PENDEKATAN EKLEKTIK YANG BERFOKUS PADA SOLUSI UNTUK MENINGKATKAN KUALITAS HUBUNGAN ROMANTIS PADA DEWASA MUDA DARI KELUARGA DENGAN ORANGTUA BERCERAI",
          "type": "article",
          "venue": "Journal Psikogenesis",
          "cited_by_count": 1,
          "topics": [
            "Marriage and Family Dynamics",
            "Islamic Finance and Communication",
            "Educational Methods and Impacts"
          ]
        },
        {
          "openalex_id": "W2922111088",
          "year": 2015,
          "title": "Pendekatan Berbasis Pola Asuh Orang Tua dalam Mengatasi Social Withdrawal Pada Anak",
          "type": "article",
          "venue": "Jurnal Psikologi Tabularasa",
          "cited_by_count": 1,
          "topics": [
            "Child Development and Education",
            "Educational Methods and Impacts",
            "Education and Character Development"
          ]
        },
        {
          "openalex_id": "W2542743269",
          "year": 2016,
          "title": "Employing quality control and feedback to the EQ-5D-5L valuation protocol to improve the quality of data collection",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 29,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Healthcare Quality and Management"
          ]
        },
        {
          "openalex_id": "W2735686076",
          "year": 2017,
          "title": "The Indonesian EQ-5D-5L Value Set",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 205,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2800059521",
          "year": 2018,
          "title": "Quality of life of the Indonesian general population: Test-retest reliability and population norms of the EQ-5D-5L and WHOQOL-BREF",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 179,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W3212036572",
          "year": 2021,
          "title": "Comparing measurement properties of EQ-5D-Y-3L and EQ-5D-Y-5L in paediatric patients",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Behavioral and Psychological Studies",
            "HER2/EGFR in Cancer Research"
          ]
        },
        {
          "openalex_id": "W4308558743",
          "year": 2022,
          "title": "Estimating an EQ-5D-Y-3L Value Set for Indonesia by Mapping the DCE onto TTO Values",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 28,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W2808780612",
          "year": 2018,
          "title": "Living in uncertainty due to floods and pollution: the health status and quality of life of people living on an unhealthy riverbank",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 26,
          "topics": [
            "Flood Risk Assessment and Management",
            "Disaster Management and Resilience",
            "Climate Change, Adaptation, Migration"
          ]
        },
        {
          "openalex_id": "W2942641401",
          "year": 2019,
          "title": "Sociodemographic determinants of self-reporting mental health problems in Indonesian urban population",
          "type": "article",
          "venue": "Psychological Research on Urban Society",
          "cited_by_count": 23,
          "topics": [
            "Intergenerational Family Dynamics and Caregiving",
            "Mental Health Treatment and Access"
          ]
        }
      ]
    }
  }
]
