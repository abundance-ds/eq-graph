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
    "name": "Min-Woo Jo",
    "member_affiliation": "Department of Preventive Medicine, University of Ulsan College of Medicine",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5015763173",
      "display_name": "Min‐Woo Jo",
      "orcid": "0000-0002-4574-1318",
      "reported_affiliation": "Ulsan College",
      "works_count": 231,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 61
        },
        {
          "topic": "Health and Wellbeing Research",
          "works": 33
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 20
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 18
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 17
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 15
        },
        {
          "topic": "Diverse Approaches in Healthcare and Education Studies",
          "works": 15
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 13
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 12
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 11
        },
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 11
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 11
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Minsu Ock",
          "works": 68
        },
        {
          "name": "Seon‐Ha Kim",
          "works": 41
        },
        {
          "name": "Seok‐Jun Yoon",
          "works": 27
        },
        {
          "name": "Sang‐Il Lee",
          "works": 27
        },
        {
          "name": "Jin Yong Lee",
          "works": 26
        },
        {
          "name": "Hyeon‐Jeong Lee",
          "works": 22
        },
        {
          "name": "In‐Hwan Oh",
          "works": 21
        },
        {
          "name": "Jong Won Lee",
          "works": 18
        },
        {
          "name": "Sung‐Cheol Yun",
          "works": 18
        },
        {
          "name": "Hyun Joo Kim",
          "works": 14
        },
        {
          "name": "Sei Won Lee",
          "works": 14
        },
        {
          "name": "Young‐Hak Kim",
          "works": 14
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164401020",
          "year": 2026,
          "title": "Deriving a Korean SF-6Dv2 Value Set Using a Discrete Choice Experiment with Duration",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W7167835396",
          "year": 2026,
          "title": "Governance fragmentation and sociotechnical misalignment in hybrid telemedicine care pathways: A qualitative study",
          "type": "article",
          "venue": "Digital Health",
          "cited_by_count": 0,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Electronic Health Records Systems",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W4410541070",
          "year": 2025,
          "title": "A randomized controlled trial of a digital lifestyle intervention involving postoperative patients with colorectal cancer",
          "type": "article",
          "venue": "npj Digital Medicine",
          "cited_by_count": 4,
          "topics": [
            "Stoma care and complications",
            "Enhanced Recovery After Surgery",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W4411287668",
          "year": 2025,
          "title": "Abstract P2-01-04: Impact of Mobile Healthcare Apps on Patient-Reported Quality of Life after Breast Cancer Surgery: A Randomized Controlled Trial",
          "type": "conference-abstract",
          "venue": "Clinical Cancer Research",
          "cited_by_count": 0,
          "topics": [
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W4411454682",
          "year": 2025,
          "title": "Author Correction: A randomized controlled trial of a digital lifestyle intervention involving postoperative patients with colorectal cancer",
          "type": "erratum",
          "venue": "npj Digital Medicine",
          "cited_by_count": 1,
          "topics": [
            "Stoma care and complications",
            "Cancer survivorship and care",
            "Enhanced Recovery After Surgery"
          ]
        },
        {
          "openalex_id": "W4417497416",
          "year": 2025,
          "title": "Cerebral infarction in red panda (&lt;i&gt;Ailurus fulgens&lt;/i&gt;)",
          "type": "article",
          "venue": "Journal of Veterinary Medical Science",
          "cited_by_count": 0,
          "topics": [
            "Antifungal resistance and susceptibility",
            "Infective Endocarditis Diagnosis and Management",
            "Cardiovascular Conditions and Treatments"
          ]
        },
        {
          "openalex_id": "W2376221739",
          "year": 2003,
          "title": "Efficient DRG Fraud Candidate Detection Method Using Data Mining Techniques",
          "type": "article",
          "venue": "Journal of Preventive Medicine and Public Health",
          "cited_by_count": 0,
          "topics": [
            "Imbalanced Data Classification Techniques"
          ]
        },
        {
          "openalex_id": "W3178966617",
          "year": 2005,
          "title": "Census population vs. registration population",
          "type": "article",
          "venue": "Journal of Preventive Medicine and Public Health",
          "cited_by_count": 0,
          "topics": [
            "Census and Population Estimation",
            "Romani and Gypsy Studies",
            "Migration and Labor Dynamics"
          ]
        },
        {
          "openalex_id": "W2015235346",
          "year": 2005,
          "title": "Rising rates, changing relationships: caesarean section and its correlates in South Korea, 1988–2000",
          "type": "article",
          "venue": "BJOG An International Journal of Obstetrics & Gynaecology",
          "cited_by_count": 38,
          "topics": [
            "Maternal and Perinatal Health Interventions",
            "Global Maternal and Child Health",
            "Maternal Mental Health During Pregnancy and Postpartum"
          ]
        },
        {
          "openalex_id": "W2406963158",
          "year": 2005,
          "title": "[Census population vs. registration population: which population denominator should be used to calculate geographical mortality].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 4,
          "topics": []
        },
        {
          "openalex_id": "W2295298510",
          "year": 2016,
          "title": "The EQ-5D-5L valuation study in Korea",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 396,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2781501523",
          "year": 2018,
          "title": "Socioeconomic status can affect pregnancy outcomes and complications, even with a universal healthcare system",
          "type": "article",
          "venue": "International Journal for Equity in Health",
          "cited_by_count": 256,
          "topics": [
            "Global Maternal and Child Health",
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Maternal and Perinatal Health Interventions"
          ]
        },
        {
          "openalex_id": "W2007061319",
          "year": 2011,
          "title": "Comparing the psychometric properties of the EQ-5D-3L and EQ-5D-5L in cancer patients in Korea",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 164,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W2025096471",
          "year": 2012,
          "title": "Psychometric properties of the EQ-5D-5L in the general population of South Korea",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 151,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W2107915429",
          "year": 2014,
          "title": "Daily Collection of Self-Reporting Sleep Disturbance Data via a Smartphone App in Breast Cancer Patients Receiving Chemotherapy: A Feasibility Study",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 142,
          "topics": [
            "Cancer survivorship and care",
            "Mobile Health and mHealth Applications",
            "Cancer-related cognitive impairment studies"
          ]
        },
        {
          "openalex_id": "W2531252297",
          "year": 2016,
          "title": "High correlation of Middle East respiratory syndrome spread with Google search and Twitter trends in Korea",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 138,
          "topics": [
            "Data-Driven Disease Surveillance",
            "Influenza Virus Research Studies",
            "COVID-19 epidemiological studies"
          ]
        },
        {
          "openalex_id": "W3092249547",
          "year": 2020,
          "title": "Increased prevalence of depression in South Korea from 2002 to 2013",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 135,
          "topics": [
            "Suicide and Self-Harm Studies",
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4405260637",
          "year": 2024,
          "title": "Cancer situation in China: an analysis based on the global epidemiological data released in 2024",
          "type": "article",
          "venue": "癌症：英文版",
          "cited_by_count": 134,
          "topics": [
            "Global Cancer Incidence and Screening",
            "Esophageal Cancer Research and Treatment",
            "Insurance, Mortality, Demography, Risk Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Mina Bahrampour",
    "member_affiliation": "University of Technology Sydney",
    "is_member": true,
    "projects": [
      {
        "project_id": "2075-EOI",
        "title": "EuroQol Meeting in Australia",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2416-BT",
        "title": "Evaluating the EQ-5D Vision, Hearing and Cognition Bolt-Ons in Older Australians: A Qualitative Study",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "466-RA",
        "title": "Testing the validity of EQ-5D-5L respiratory bolt-ons in a large Australian dataset",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5068470091",
      "display_name": "Mina Bahrampour",
      "orcid": "0000-0002-6915-1865",
      "reported_affiliation": "University of Technology Sydney",
      "works_count": 30,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 17
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 7
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 5
        },
        {
          "topic": "Global Health Care Issues",
          "works": 5
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 4
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 4
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 4
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 3
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 2
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 2
        },
        {
          "topic": "Customer Service Quality and Loyalty",
          "works": 2
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Brendan Mulhern",
          "works": 11
        },
        {
          "name": "Richard Norman",
          "works": 8
        },
        {
          "name": "Joshua Byrnes",
          "works": 8
        },
        {
          "name": "Paul Scuffham",
          "works": 8
        },
        {
          "name": "Martin Downes",
          "works": 8
        },
        {
          "name": "Nancy Devlin",
          "works": 7
        },
        {
          "name": "Rosalie Viney",
          "works": 7
        },
        {
          "name": "Kim Dalziel",
          "works": 5
        },
        {
          "name": "Renee Jones",
          "works": 5
        },
        {
          "name": "Deborah J. Street",
          "works": 4
        },
        {
          "name": "Vahid Yazdi‐Feyzabadi",
          "works": 4
        },
        {
          "name": "Harriet Hiscock",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164822486",
          "year": 2026,
          "title": "Assessing the dimensionality of the EQ-HWB-25 alongside EQ-5D-5L, QOL-ACC and ASCOT in an older adult population",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W7150066852",
          "year": 2026,
          "title": "Corrigendum to ‘Understanding how adults and adolescents value children's health states: a qualitative exploration using Discrete Choice Experiments (DCEs) with and without duration’ [Soc. Sci. Med. 398 (2026) 119193]",
          "type": "erratum",
          "venue": "Social Science & Medicine",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W4408782453",
          "year": 2025,
          "title": "A framework for extending the health-related quality adjusted life year by combining instruments",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W4407963059",
          "year": 2025,
          "title": "Exploring the Validity of Measures of Health-Related Quality of Life in Older Adults at Increased Risk of Falls and/or Fractures in Exercise Clinical Trials",
          "type": "article",
          "venue": "Journal of Applied Gerontology",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Musculoskeletal pain and rehabilitation",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4414259738",
          "year": 2025,
          "title": "Impoverishing Health Expenditure in Iran Before and After the COVID-19 Pandemic: A National Cross-sectional Study",
          "type": "article",
          "venue": "Health Technology Assessment in Action",
          "cited_by_count": 0,
          "topics": [
            "Global Health Care Issues",
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W4396921531",
          "year": 2024,
          "title": "A Comparison of the Psychometric Properties of the EQ-5D-Y-3L and EQ-5D-Y-5L Using Paediatric Multi-Instrument Comparison (P-MIC) Study Data",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W2279018603",
          "year": 2002,
          "title": "KNOWLEDGE AND ATTITUDE OF NURSES REGARDING ECT AMONG STAFF AT A PSYCHIATRIC HOSPITAL",
          "type": "article",
          "venue": "Iranian Journal of Psychiatry and Clinical Psychology",
          "cited_by_count": 0,
          "topics": [
            "Organizational and Employee Performance"
          ]
        },
        {
          "openalex_id": "W2277447011",
          "year": 2004,
          "title": "ATTITUDE OF KERMAN UNIVERSITIES MALE STUDENTS TOWAD CIGARETTES",
          "type": "article",
          "venue": "Iranian Journal of Psychiatry and Clinical Psychology",
          "cited_by_count": 6,
          "topics": [
            "Teacher Professional Development and Motivation",
            "Problem Solving Skills Development",
            "Educational Leadership and Administration"
          ]
        },
        {
          "openalex_id": "W2611645546",
          "year": 2013,
          "title": "Determination of Technical Efficiency of Intensive Care Units in Hospitals Afilliated to Kerman University of Medical Sciences by Stochastic Frontier Analysis in 2008",
          "type": "article",
          "venue": "",
          "cited_by_count": 2,
          "topics": [
            "Insurance and Financial Risk Management",
            "Efficiency Analysis Using DEA",
            "Economic Analysis and Policy"
          ]
        },
        {
          "openalex_id": "W2147078423",
          "year": 2013,
          "title": "Patient Preferences for Hospital Quality: Case Study of Iran",
          "type": "article",
          "venue": "Iranian Red Crescent Medical Journal",
          "cited_by_count": 8,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Healthcare Policy and Management",
            "Customer Service Quality and Loyalty"
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
          "openalex_id": "W2803692502",
          "year": 2018,
          "title": "Prevalence and intensity of catastrophic health care expenditures in Iran from 2008 to 2015: a study on Iranian household income and expenditure survey",
          "type": "article",
          "venue": "International Journal for Equity in Health",
          "cited_by_count": 77,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Health Care Issues",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W3021310744",
          "year": 2020,
          "title": "Discrete choice experiments to generate utility values for multi-attribute utility instruments: a systematic review of methods",
          "type": "review",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 46,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4388628817",
          "year": 2023,
          "title": "Comparative Psychometric Performance of Common Generic Paediatric Health-Related Quality of Life Instrument Descriptive Systems: Results from the Australian Paediatric Multi-Instrument Comparison Study",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 28,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2886100760",
          "year": 2018,
          "title": "Hospital service quality – patient preferences – a discrete choice experiment",
          "type": "article",
          "venue": "International Journal of Health Care Quality Assurance",
          "cited_by_count": 20,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Economic and Environmental Valuation",
            "Customer Service Quality and Loyalty"
          ]
        },
        {
          "openalex_id": "W2521911036",
          "year": 2017,
          "title": "Incidence and intensity of catastrophic health expenditures in Iranian provinces; 2008-2014",
          "type": "article",
          "venue": "Griffith Research Online (Griffith University, Queensland, Australia)",
          "cited_by_count": 15,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Health Care Issues",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2612780963",
          "year": 2017,
          "title": "The Trend of Impoverishing Effects of Out-Of-Pocket Health Expenditure in Iranian Provinces in 2008-2014",
          "type": "article",
          "venue": "DOAJ (DOAJ: Directory of Open Access Journals)",
          "cited_by_count": 14,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Health Care Issues",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W3093100734",
          "year": 2020,
          "title": "Utility Values for the CP-6D, a Cerebral Palsy-Specific Multi-Attribute Utility Instrument, Using a Discrete Choice Experiment",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 10,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cerebral Palsy and Movement Disorders",
            "Ophthalmology and Visual Impairment Studies"
          ]
        }
      ]
    }
  },
  {
    "name": "Minghui Li",
    "member_affiliation": "University of Tennessee",
    "is_member": true,
    "projects": [
      {
        "project_id": "2016580",
        "title": "The feasibility of using the EQ-VT program to conduct the EQ-5D-5L valuation study in rural China",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180620",
        "title": "Validation and Comparison of the Psychometric Properties of the EQ-5D-3L-Y and EQ-5D-5L-Y in the United States",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5100400064",
      "display_name": "Minghui Li",
      "orcid": "0000-0003-3673-5925",
      "reported_affiliation": "",
      "works_count": 38,
      "top_topics": [
        {
          "topic": "COVID-19 and Mental Health",
          "works": 7
        },
        {
          "topic": "Mental Health via Writing",
          "works": 5
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 4
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 4
        },
        {
          "topic": "COVID-19 epidemiological studies",
          "works": 3
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 3
        },
        {
          "topic": "Education and Work Dynamics",
          "works": 3
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 2
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 2
        },
        {
          "topic": "SARS-CoV-2 and COVID-19 Research",
          "works": 2
        },
        {
          "topic": "Long-Term Effects of COVID-19",
          "works": 2
        },
        {
          "topic": "Machine Learning in Healthcare",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jie Yang",
          "works": 8
        },
        {
          "name": "Yining Hua",
          "works": 7
        },
        {
          "name": "Li Zhou",
          "works": 6
        },
        {
          "name": "Jiageng Wu",
          "works": 5
        },
        {
          "name": "Nan Luo",
          "works": 4
        },
        {
          "name": "Jing Yuan",
          "works": 3
        },
        {
          "name": "Gang Lv",
          "works": 3
        },
        {
          "name": "Andrew Lloyd",
          "works": 3
        },
        {
          "name": "Michael Herdman",
          "works": 3
        },
        {
          "name": "Shixu Lin",
          "works": 3
        },
        {
          "name": "Yujie Zhang",
          "works": 3
        },
        {
          "name": "Gordon G. Liu",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4406559574",
          "year": 2025,
          "title": "Analysis of longitudinal social media for monitoring symptoms during a pandemic",
          "type": "article",
          "venue": "Journal of Biomedical Informatics",
          "cited_by_count": 1,
          "topics": [
            "Mental Health via Writing",
            "Machine Learning in Healthcare",
            "Data-Driven Disease Surveillance"
          ]
        },
        {
          "openalex_id": "W4417097699",
          "year": 2025,
          "title": "Astra: Toward General-Purpose Mobile Robots via Hierarchical Multimodal Learning",
          "type": "preprint",
          "venue": "arXiv (Cornell University)",
          "cited_by_count": 0,
          "topics": [
            "Robotics and Sensor-Based Localization",
            "Robotic Path Planning Algorithms",
            "Autonomous Vehicle Technology and Safety"
          ]
        },
        {
          "openalex_id": "W4411003153",
          "year": 2025,
          "title": "Hybrid Sequence Augmentation and Optimized Contrastive Loss Recommendation",
          "type": "article",
          "venue": "International Journal of Advanced Computer Science and Applications",
          "cited_by_count": 0,
          "topics": [
            "Speech Recognition and Synthesis",
            "Web Data Mining and Analysis",
            "Advanced Algorithms and Applications"
          ]
        },
        {
          "openalex_id": "W4409361494",
          "year": 2025,
          "title": "Recommendation Model Based on Global Intention Learning and Sequence Augmentation",
          "type": "article",
          "venue": "Symmetry",
          "cited_by_count": 0,
          "topics": [
            "Technology and Data Analysis"
          ]
        },
        {
          "openalex_id": "W4416037132",
          "year": 2025,
          "title": "Transferable Direct Prompt Injection via Activation-Guided MCMC Sampling",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "Markov Chains and Monte Carlo Methods",
            "Functional Brain Connectivity Studies",
            "Advanced MRI Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W4416067361",
          "year": 2025,
          "title": "Transferable Direct Prompt Injection via Activation-Guided MCMC Sampling",
          "type": "preprint",
          "venue": "arXiv (Cornell University)",
          "cited_by_count": 0,
          "topics": [
            "Adversarial Robustness in Machine Learning",
            "Security and Verification in Computing",
            "Advanced Malware Detection Techniques"
          ]
        },
        {
          "openalex_id": "W2524706444",
          "year": 1998,
          "title": "Der Konfuzianismus Ursprünge, Entwicklungen, Perspektiven",
          "type": "article",
          "venue": "",
          "cited_by_count": 4,
          "topics": [
            "Japanese History and Culture",
            "Chinese history and philosophy",
            "Financial Crisis of the 21st Century"
          ]
        },
        {
          "openalex_id": "W2360616401",
          "year": 2003,
          "title": "Tectonic Evolution Since Late Palaeozoic Era in West Yunnan",
          "type": "article",
          "venue": "Journal of Tongji University",
          "cited_by_count": 3,
          "topics": [
            "Geochemistry and Geochronology of Asian Mineral Deposits",
            "Geological and Geophysical Studies",
            "Hydrocarbon exploration and reservoir analysis"
          ]
        },
        {
          "openalex_id": "W2371422551",
          "year": 2005,
          "title": "Theoretical Analysis of the Rising of Legal Responsibility for Misrepresentation in Financial Reporting",
          "type": "article",
          "venue": "Journal of Hebei University",
          "cited_by_count": 0,
          "topics": [
            "Legal Studies and Policies"
          ]
        },
        {
          "openalex_id": "W86618644",
          "year": 2006,
          "title": "Ru Xue, Wen Hua Yu Zong Jiao: Liu Shuxian Xian Sheng Qi Zhi Shou Qing Lun Wen Ji",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Japanese History and Culture",
            "Chinese history and philosophy"
          ]
        },
        {
          "openalex_id": "W3013014385",
          "year": 2020,
          "title": "Monitoring transmissibility and mortality of COVID-19 in Europe",
          "type": "article",
          "venue": "International Journal of Infectious Diseases",
          "cited_by_count": 377,
          "topics": [
            "COVID-19 epidemiological studies",
            "SARS-CoV-2 detection and testing",
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W1970509123",
          "year": 2012,
          "title": "Developing the Chinese version of the new 5-level EQ-5D descriptive system: the response scaling approach",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 126,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W1965170384",
          "year": 2012,
          "title": "A comparison of the scaling properties of the English, Spanish, French, and Chinese EQ-5D descriptive systems",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 53,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W4388892389",
          "year": 2023,
          "title": "Oral VV116 versus placebo in patients with mild-to-moderate COVID-19 in China: a multicentre, double-blind, phase 3, randomised controlled study",
          "type": "article",
          "venue": "The Lancet Infectious Diseases",
          "cited_by_count": 48,
          "topics": [
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 Clinical Research Studies",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W4397003497",
          "year": 2024,
          "title": "Clinical Text Datasets for Medical Artificial Intelligence and Large Language Models — A Systematic Review",
          "type": "review",
          "venue": "NEJM AI",
          "cited_by_count": 45,
          "topics": [
            "Machine Learning in Healthcare",
            "Artificial Intelligence in Healthcare and Education",
            "Artificial Intelligence in Healthcare"
          ]
        },
        {
          "openalex_id": "W2113618863",
          "year": 2013,
          "title": "The effects of lead time and visual aids in TTO valuation: a study of the EQ-VT framework",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 27,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Older Adults Driving Studies",
            "Physical Activity and Health"
          ]
        },
        {
          "openalex_id": "W4301392846",
          "year": 2022,
          "title": "Tracking the Impact of COVID-19 and Lockdown Policies on Public Mental Health Using Social Media: Infoveillance Study",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 26,
          "topics": [
            "Mental Health via Writing",
            "COVID-19 and Mental Health",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W4321484723",
          "year": 2023,
          "title": "Trend and Co-occurrence Network of COVID-19 Symptoms From Large-Scale Social Media Data: Infoveillance Study",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 22,
          "topics": [
            "Mental Health via Writing",
            "Dermatological and COVID-19 studies",
            "Long-Term Effects of COVID-19"
          ]
        }
      ]
    }
  },
  {
    "name": "Minh Pham",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1970-RA",
        "title": "Exploring dimension-specific components and aging (EDCA): a secondary data analysis",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2136-TVG",
        "title": "Summer Research Visit to Singapore: Advancing EuroQol Fatigue/Sleep Bolt-ons among adults living with Obesity",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2305-BT",
        "title": "Qualitative Study for Fatigue Bolt-on (QSFB) in Collaboration with U.S. Adults Living with Multiple Sclerosis",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5077706356",
      "display_name": "Phạm Minh Khuê",
      "orcid": "0000-0003-2974-3484",
      "reported_affiliation": "Hai phong University Of Medicine and Pharmacy",
      "works_count": 129,
      "top_topics": [
        {
          "topic": "Research studies in Vietnam",
          "works": 32
        },
        {
          "topic": "HIV, Drug Use, Sexual Risk",
          "works": 31
        },
        {
          "topic": "Hepatitis C virus research",
          "works": 19
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 17
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 13
        },
        {
          "topic": "Health Literacy and Information Accessibility",
          "works": 12
        },
        {
          "topic": "Hepatitis B Virus Studies",
          "works": 12
        },
        {
          "topic": "Tuberculosis Research and Epidemiology",
          "works": 8
        },
        {
          "topic": "Opioid Use Disorder Treatment",
          "works": 7
        },
        {
          "topic": "Liver Disease Diagnosis and Treatment",
          "works": 6
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 5
        },
        {
          "topic": "Nutritional Studies and Diet",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nicolas Nagot",
          "works": 39
        },
        {
          "name": "Didier Laureillard",
          "works": 38
        },
        {
          "name": "Don C. Des Jarlais",
          "works": 34
        },
        {
          "name": "Catherine Quillet",
          "works": 34
        },
        {
          "name": "Jean‐Pierre Molès",
          "works": 33
        },
        {
          "name": "Roselyne Vallo",
          "works": 33
        },
        {
          "name": "Laurent Michel",
          "works": 33
        },
        {
          "name": "Delphine Rapoud",
          "works": 32
        },
        {
          "name": "Jonathan Feelemyer",
          "works": 29
        },
        {
          "name": "Tuyen Van Duong",
          "works": 25
        },
        {
          "name": "Thao T. P. Nguyen",
          "works": 22
        },
        {
          "name": "Dương Thị Hương",
          "works": 22
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4410587169",
          "year": 2025,
          "title": "44. ĐẶC ĐIỂM CÁC LĨNH VỰC CHỨC NĂNG CHẤT LƯỢNG CUỘC SỐNG CỦA BỆNH NHÂN NỮ UNG THƯ SINH DỤC TẠI BỆNH VIỆN K NĂM 2020-2021",
          "type": "article",
          "venue": "Tạp chí Y học Cộng đồng",
          "cited_by_count": 0,
          "topics": [
            "Regional Development and Environment",
            "Medical Research and Treatments"
          ]
        },
        {
          "openalex_id": "W4406241117",
          "year": 2025,
          "title": "Association between underlying health conditions and long COVID among non-hospitalized and hospitalized individuals as modified by health literacy: A multi-center study",
          "type": "article",
          "venue": "Public Health",
          "cited_by_count": 2,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W4412492340",
          "year": 2025,
          "title": "Hepatitis C virus incidence trend and its risk factors among people who inject drugs in Hai Phong, Vietnam",
          "type": "article",
          "venue": "Hepatology International",
          "cited_by_count": 0,
          "topics": [
            "HIV, Drug Use, Sexual Risk",
            "Hepatitis C virus research",
            "Hepatitis B Virus Studies"
          ]
        },
        {
          "openalex_id": "W4414590049",
          "year": 2025,
          "title": "High Efficiency and Safety of Hepatitis C Treatment Among People Who Inject Drugs in Vietnam",
          "type": "article",
          "venue": "Journal of Viral Hepatitis",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis C virus research",
            "HIV, Drug Use, Sexual Risk",
            "Hepatitis B Virus Studies"
          ]
        },
        {
          "openalex_id": "W4407859398",
          "year": 2025,
          "title": "High prevalence and incidence of HSV-2 among people who inject drugs in Hai Phong, Vietnam, and risk factors associated with seroconversion",
          "type": "article",
          "venue": "European Journal of Clinical Microbiology & Infectious Diseases",
          "cited_by_count": 0,
          "topics": [
            "HIV, Drug Use, Sexual Risk",
            "Hepatitis C virus research",
            "Herpesvirus Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W4411392916",
          "year": 2025,
          "title": "Hành vi sử dụng đa chất và một số yếu tố liên quan ở người tiêm chích heroin tại Hải Phòng",
          "type": "article",
          "venue": "Tạp chí Nghiên cứu Y học",
          "cited_by_count": 0,
          "topics": [
            "Research studies in Vietnam"
          ]
        },
        {
          "openalex_id": "W4239160367",
          "year": 1900,
          "title": "Medical Practice in Australia.",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 0,
          "topics": [
            "Primary Care and Health Outcomes",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2100601928",
          "year": 2007,
          "title": "A 10-year prospective surveillance of<i>Mycobacterium tuberculosis</i>drug resistance in France 1995–2004",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 29,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "Pneumocystis jirovecii pneumonia detection and treatment",
            "Infectious Diseases and Tuberculosis"
          ]
        },
        {
          "openalex_id": "W2082904197",
          "year": 2007,
          "title": "Evaluation of data quality in a laboratory-based surveillance of <i>M. tuberculosis</i> drug resistance and impact on the prevalence of resistance: France, 2004",
          "type": "article",
          "venue": "Epidemiology and Infection",
          "cited_by_count": 2,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "Mycobacterium research and diagnosis",
            "Pneumonia and Respiratory Infections"
          ]
        },
        {
          "openalex_id": "W132185310",
          "year": 2008,
          "title": "Drug resistance and HIV co-infection among pulmonary tuberculosis patients in Haiphong City, Vietnam.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 12,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "HIV, Drug Use, Sexual Risk",
            "Pneumocystis jirovecii pneumonia detection and treatment"
          ]
        },
        {
          "openalex_id": "W3014073980",
          "year": 2020,
          "title": "People with Suspected COVID-19 Symptoms Were More Likely Depressed and Had Lower Health-Related Quality of Life: The Potential Benefit of Health Literacy",
          "type": "article",
          "venue": "Journal of Clinical Medicine",
          "cited_by_count": 581,
          "topics": [
            "COVID-19 and Mental Health",
            "Health Literacy and Information Accessibility",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W3035455574",
          "year": 2020,
          "title": "Fear of COVID-19 Scale—Associations of Its Scores with Health Literacy and Health-Related Behaviors among Medical Students",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 407,
          "topics": [
            "COVID-19 and Mental Health",
            "Health Literacy and Information Accessibility",
            "Family and Patient Care in Intensive Care Units"
          ]
        },
        {
          "openalex_id": "W2575874589",
          "year": 2017,
          "title": "Measuring health literacy in Asia: Validation of the HLS-EU-Q47 survey tool in six Asian countries",
          "type": "article",
          "venue": "Journal of Epidemiology",
          "cited_by_count": 323,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Data-Driven Disease Surveillance",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W2940170181",
          "year": 2019,
          "title": "Development and Validation of a New Short-Form Health Literacy Instrument (HLS-SF12) for the General Public in Six Asian Countries",
          "type": "article",
          "venue": "HLRP Health Literacy Research and Practice",
          "cited_by_count": 200,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Health Education and Validation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2888484774",
          "year": 2018,
          "title": "Musculoskeletal Disorders: Prevalence and Associated Factors among District Hospital Nurses in Haiphong, Vietnam",
          "type": "article",
          "venue": "BioMed Research International",
          "cited_by_count": 127,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Occupational health in dentistry",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W3013528681",
          "year": 2020,
          "title": "Factors Associated with Health Literacy among the Elderly People in Vietnam",
          "type": "article",
          "venue": "BioMed Research International",
          "cited_by_count": 98,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Technology Use by Older Adults",
            "Assistive Technology in Communication and Mobility"
          ]
        },
        {
          "openalex_id": "W3090560984",
          "year": 2020,
          "title": "Digital Healthy Diet Literacy and Self-Perceived Eating Behavior Change during COVID-19 Pandemic among Undergraduate Nursing and Medical Students: A Rapid Online Survey",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 93,
          "topics": [
            "Nutritional Studies and Diet",
            "COVID-19 and Mental Health",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W4391848409",
          "year": 2024,
          "title": "Progress towards elimination of viral hepatitis: a Lancet Gastroenterology &amp; Hepatology Commission update",
          "type": "article",
          "venue": "The Lancet. Gastroenterology & hepatology",
          "cited_by_count": 85,
          "topics": [
            "Hepatitis B Virus Studies",
            "Liver Disease Diagnosis and Treatment",
            "Viral gastroenteritis research and epidemiology"
          ]
        }
      ]
    }
  },
  {
    "name": "Márta Péntek",
    "member_affiliation": "Obuda University",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5064557440",
      "display_name": "Márta Péntek",
      "orcid": "0000-0001-9636-6012",
      "reported_affiliation": "Obuda University",
      "works_count": 349,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 105
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 44
        },
        {
          "topic": "Biosimilars and Bioanalytical Methods",
          "works": 29
        },
        {
          "topic": "Psoriasis: Treatment and Pathogenesis",
          "works": 28
        },
        {
          "topic": "Global Health Care Issues",
          "works": 26
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 18
        },
        {
          "topic": "Mobile Health and mHealth Applications",
          "works": 18
        },
        {
          "topic": "Inflammatory Bowel Disease",
          "works": 16
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 15
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 15
        },
        {
          "topic": "Autoimmune Bullous Skin Diseases",
          "works": 14
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 13
        }
      ],
      "frequent_coauthors": [
        {
          "name": "László Gulàcsi",
          "works": 293
        },
        {
          "name": "Valentin Brodszky",
          "works": 191
        },
        {
          "name": "Petra Baji",
          "works": 130
        },
        {
          "name": "Zsombor Zrubka",
          "works": 125
        },
        {
          "name": "Fanni Rencz",
          "works": 117
        },
        {
          "name": "Levente Kovács",
          "works": 44
        },
        {
          "name": "Áron Hölgyesi",
          "works": 33
        },
        {
          "name": "I Boncz",
          "works": 31
        },
        {
          "name": "Dominik Golicki",
          "works": 26
        },
        {
          "name": "Andrea Szegedi",
          "works": 25
        },
        {
          "name": "Valentina Prevolnik Rupel",
          "works": 21
        },
        {
          "name": "Miklós Sárdy",
          "works": 21
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7156687399",
          "year": 2026,
          "title": "Additional file 1 of Health-related quality of life in adults with epidermolysis bullosa: a cross-sectional study in seven European countries using EQ-5D-5L",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Skin and Cellular Biology Research",
            "Genetic and rare skin diseases.",
            "Dermatology and Skin Diseases"
          ]
        },
        {
          "openalex_id": "W7157019572",
          "year": 2026,
          "title": "Additional file 1 of Health-related quality of life in adults with epidermolysis bullosa: a cross-sectional study in seven European countries using EQ-5D-5L",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Skin and Cellular Biology Research",
            "Genetic and rare skin diseases.",
            "Dermatology and Skin Diseases"
          ]
        },
        {
          "openalex_id": "W7162507392",
          "year": 2026,
          "title": "Automated Classification of EQ-5D Literature in PubMed Using Multi-Phase Learning and LLM-Assisted Co-Training",
          "type": "article",
          "venue": "IEEE Access",
          "cited_by_count": 0,
          "topics": [
            "Biomedical Text Mining and Ontologies",
            "Topic Modeling",
            "Meta-analysis and systematic reviews"
          ]
        },
        {
          "openalex_id": "W7161136881",
          "year": 2026,
          "title": "Ensembles of Large Language Models for Identifying EQ-5D Studies in Pubmed Based on their Abstracts",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Reliability and Agreement in Measurement",
            "Psychometric Methodologies and Testing",
            "Safety Systems Engineering in Autonomy"
          ]
        },
        {
          "openalex_id": "W7139028021",
          "year": 2026,
          "title": "Health-related quality of life in adults with epidermolysis bullosa: a cross-sectional study in seven European countries using EQ-5D-5L",
          "type": "article",
          "venue": "Orphanet Journal of Rare Diseases",
          "cited_by_count": 1,
          "topics": [
            "Skin and Cellular Biology Research",
            "Genetic and rare skin diseases.",
            "Autoimmune Bullous Skin Diseases"
          ]
        },
        {
          "openalex_id": "W7162192503",
          "year": 2026,
          "title": "Optimizing Glycemic Control Using Continuous Glucose Monitoring: An Umbrella Review of Systematic Reviews and Meta-Analysis",
          "type": "review",
          "venue": "Journal of Diabetes Science and Technology",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Research",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Spectroscopy Techniques in Biomedical and Chemical Research"
          ]
        },
        {
          "openalex_id": "W2122771659",
          "year": 2002,
          "title": "Establishing a standard for patient-completed instrument adaptations in Eastern Europe: experience with the Nottingham Health Profile in Hungary",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 14,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Health and Wellbeing Research"
          ]
        },
        {
          "openalex_id": "W2011782558",
          "year": 2005,
          "title": "PAR17 BURDEN OF ILLNESS, COSTS AND OUTCOMES OF RHEUMATOID ARTHRITIS IN HUNGARY",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 4,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W2090680882",
          "year": 2006,
          "title": "PDB41 EFFECT OF COMPLICATIONS ON HEALTH RELATED QUALITY OF LIFE IN HUNGARIAN INSULIN TREATED DIABETIC PATINETS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Nutrition and Health Studies",
            "Nutritional Studies and Diet"
          ]
        },
        {
          "openalex_id": "W2030347234",
          "year": 2006,
          "title": "PHP17 EFFICIENCY OF RHEUMATOLOGY HOSPITAL CARE: CHANGES IN THE AVERAGE LENGTH OF STAY IN RHEUMATOLOGY DEPARTMENTS IN HUNGARY",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2279527004",
          "year": 2016,
          "title": "Alopecia areata and health-related quality of life: a systematic review and meta-analysis",
          "type": "review",
          "venue": "British Journal of Dermatology",
          "cited_by_count": 240,
          "topics": [
            "Hair Growth and Disorders",
            "Facial Rejuvenation and Surgery Techniques",
            "Skin and Cellular Biology Research"
          ]
        },
        {
          "openalex_id": "W2484016290",
          "year": 2016,
          "title": "EQ-5D in Central and Eastern Europe: 2000–2015",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 152,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W1981336058",
          "year": 2014,
          "title": "Budget impact analysis of biosimilar infliximab (CT-P13) for the treatment of rheumatoid arthritis in six Central and Eastern European countries",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 129,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3048694137",
          "year": 2020,
          "title": "Parallel Valuation of the EQ-5D-3L and EQ-5D-5L by Time Trade-Off in Hungary",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 119,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W3043408157",
          "year": 2020,
          "title": "Managing COVID-19 within and across health systems: why we need performance intelligence to coordinate a global response",
          "type": "article",
          "venue": "Health Research Policy and Systems",
          "cited_by_count": 102,
          "topics": [
            "Human Resource Development and Performance Evaluation",
            "Accounting and Organizational Management",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2057699446",
          "year": 2014,
          "title": "Exploring the relationship between EQ-5D, DLQI and PASI, and mapping EQ-5D utilities: a cross-sectional study in psoriasis from Hungary",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 98,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psoriasis: Treatment and Pathogenesis",
            "Spondyloarthritis Studies and Treatments"
          ]
        },
        {
          "openalex_id": "W2096103877",
          "year": 2015,
          "title": "Biosimilars for the management of rheumatoid arthritis: economic considerations",
          "type": "article",
          "venue": "Expert Review of Clinical Immunology",
          "cited_by_count": 95,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W2946470017",
          "year": 2019,
          "title": "Psychometric properties of the Hungarian version of the eHealth Literacy Scale",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 93,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Mobile Health and mHealth Applications",
            "Electronic Health Records Systems"
          ]
        }
      ]
    }
  }
]
