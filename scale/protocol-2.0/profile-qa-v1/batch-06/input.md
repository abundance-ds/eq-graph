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
    "name": "Arto Ohinmaa",
    "member_affiliation": "School of Public Health, University of Alberta, Edmonton, Canada",
    "is_member": true,
    "projects": [
      {
        "project_id": "1744-EO",
        "title": "ISOQOL Annual Conference, Calgary, October 18 - 21; Symposium 7: Measuring and valuing health in children using EuroQol instruments – Challenges and Opportunities",
        "working_group": "Youth, Education and Outreach"
      },
      {
        "project_id": "2015380",
        "title": "Alberta EQ-5D end-user conference and APERSU Scientific Advisory Committee meeting fall 2015",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5087246819",
      "display_name": "Arto Öhinmaa",
      "orcid": "0000-0002-7094-1573",
      "reported_affiliation": "University of Alberta",
      "works_count": 317,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 80
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 35
        },
        {
          "topic": "Telemedicine and Telehealth Implementation",
          "works": 31
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 21
        },
        {
          "topic": "Healthcare Systems and Technology",
          "works": 15
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 14
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 14
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 14
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 14
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 14
        },
        {
          "topic": "Mobile Health and mHealth Applications",
          "works": 13
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 13
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Paul J. Veugelers",
          "works": 52
        },
        {
          "name": "Philip Jacobs",
          "works": 40
        },
        {
          "name": "Jeffrey Johnson",
          "works": 39
        },
        {
          "name": "Fatima Al Sayah",
          "works": 30
        },
        {
          "name": "Nguyễn Xuân Thành",
          "works": 22
        },
        {
          "name": "Padma Kaul",
          "works": 20
        },
        {
          "name": "Vincent I. O. Agyapong",
          "works": 19
        },
        {
          "name": "David Hailey",
          "works": 17
        },
        {
          "name": "Andrew J. Greenshaw",
          "works": 17
        },
        {
          "name": "Bach Xuan Tran",
          "works": 16
        },
        {
          "name": "Risto P. Roine",
          "works": 13
        },
        {
          "name": "Xiuyun Wu",
          "works": 13
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7128794725",
          "year": 2026,
          "title": "Exploring the Feasibility of Using Discrete Choice Experiments With Duration to Elicit Health State Preferences Among Canadian Youth: A Convergent Parallel Mixed Methods Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W7123851798",
          "year": 2026,
          "title": "Healthcare Cost Associated with an Acute Mental Healthcare Bundle in Pediatric Emergency Departments",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 0,
          "topics": [
            "Emergency and Acute Care Studies",
            "Healthcare Decision-Making and Restraints",
            "Psychiatric care and mental health services"
          ]
        },
        {
          "openalex_id": "W7126210739",
          "year": 2026,
          "title": "Patients as partners in a research advisory council role: describing the APERSU Patient Engagement Network",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Mental Health and Patient Involvement",
            "Patient-Provider Communication in Healthcare",
            "Social Media in Health Education"
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
          "openalex_id": "W7133132736",
          "year": 2026,
          "title": "The impact of testing positive versus negative for COVID-19 on health-related quality of life: cross-sectional evidence from the Alberta post-COVID-19 follow-up survey",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W4414379279",
          "year": 2025,
          "title": "Aligning Indigenous and Western Concepts of Health Resource Decision Making in a Western Canadian First Nations Context",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Indigenous Health, Education, and Rights",
            "Indigenous Studies and Ecology",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W4406454496",
          "year": 1992,
          "title": "NHP - koetun terveydentilan mittari terveydenhuollon arviointitutkimuksiin",
          "type": "article",
          "venue": "Sosiaalilääketieteellinen Aikakauslehti",
          "cited_by_count": 0,
          "topics": [
            "Primary Care and Health Outcomes",
            "Healthcare Systems and Technology",
            "Health Promotion and Cardiovascular Prevention"
          ]
        },
        {
          "openalex_id": "W4406454511",
          "year": 1993,
          "title": "Terveyteen liittyvän elämänlaadun mittaaminen aivokasvainpotilailla",
          "type": "article",
          "venue": "Sosiaalilääketieteellinen Aikakauslehti",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W4406282512",
          "year": 1994,
          "title": "Aikuisdiabeetikkojen elämänlaatu NHP-mittarilla mitattuna",
          "type": "article",
          "venue": "Sosiaalilääketieteellinen Aikakauslehti",
          "cited_by_count": 1,
          "topics": [
            "Research in Social Sciences"
          ]
        },
        {
          "openalex_id": "W1446678671",
          "year": 1995,
          "title": "Nottingham Health Profilen (NHP) suomalainen versio",
          "type": "other",
          "venue": "STM:n Hallinnonalan avoin julkaisuarkisto (Julkari)",
          "cited_by_count": 7,
          "topics": [
            "Research in Social Sciences"
          ]
        },
        {
          "openalex_id": "W2405193268",
          "year": 2015,
          "title": "A Time Trade-off-derived Value Set of the EQ-5D-5L for Canada",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 490,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2154795762",
          "year": 2003,
          "title": "A single European currency for EQ-5D health states",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 465,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2156739230",
          "year": 2003,
          "title": "The socio-economic impact of telehealth: A systematic review",
          "type": "review",
          "venue": "Journal of Telemedicine and Telecare",
          "cited_by_count": 411,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Patient Satisfaction in Healthcare",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W1999093857",
          "year": 2001,
          "title": "Periradicular Infiltration for Sciatica",
          "type": "article",
          "venue": "Spine",
          "cited_by_count": 409,
          "topics": [
            "Spine and Intervertebral Disc Pathology",
            "Anesthesia and Pain Management",
            "Pain Management and Treatment"
          ]
        },
        {
          "openalex_id": "W2048955953",
          "year": 2002,
          "title": "Systematic review of evidence for the benefits of telemedicine",
          "type": "article",
          "venue": "Journal of Telemedicine and Telecare",
          "cited_by_count": 405,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Radiology practices and education"
          ]
        },
        {
          "openalex_id": "W2137881942",
          "year": 2002,
          "title": "Endovenous obliteration versus conventional stripping operation in the treatment of primary varicose veins: A randomized controlled trial with comparison of the costs",
          "type": "article",
          "venue": "Journal of Vascular Surgery",
          "cited_by_count": 340,
          "topics": [
            "Diagnosis and Treatment of Venous Diseases",
            "Central Venous Catheters and Hemodialysis",
            "Body Contouring and Surgery"
          ]
        },
        {
          "openalex_id": "W2143263600",
          "year": 2008,
          "title": "A new population-based measure of the economic burden of mental illness in Canada",
          "type": "article",
          "venue": "Chronic diseases in Canada",
          "cited_by_count": 274,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W2157839242",
          "year": 2012,
          "title": "Quality of life profile and psychometric properties of the EQ-5D-5L in HIV/AIDS patients",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 214,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "HIV/AIDS Research and Interventions",
            "Diabetes Management and Education"
          ]
        }
      ]
    }
  },
  {
    "name": "Asrul Shafie",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2016100",
        "title": "Valuation of EQ-5D-5L for the Malaysian population",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016190",
        "title": "National EQ-5D Symposium and Valuation Workshop",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190290",
        "title": "Malaysian EQ‐5D‐5L Value Set Symposium and Workshop",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5089160643",
      "display_name": "Asrul Akmal Shafie",
      "orcid": "0000-0002-5629-9270",
      "reported_affiliation": "Universiti Sains Malaysia",
      "works_count": 413,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 84
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 66
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 60
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 38
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 25
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 23
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 21
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 21
        },
        {
          "topic": "Pharmaceutical studies and practices",
          "works": 21
        },
        {
          "topic": "Blood Pressure and Hypertension Studies",
          "works": 18
        },
        {
          "topic": "Tuberculosis Research and Epidemiology",
          "works": 18
        },
        {
          "topic": "Diabetes, Cardiovascular Risks, and Lipoproteins",
          "works": 17
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Mohamed Azmi Hassali",
          "works": 212
        },
        {
          "name": "Fahad Saleem",
          "works": 86
        },
        {
          "name": "Muhammad Atif",
          "works": 38
        },
        {
          "name": "N. Haq",
          "works": 35
        },
        {
          "name": "Mohamed Izham Mohamed Ibrahim",
          "works": 32
        },
        {
          "name": "Syed Azhar Syed Sulaiman",
          "works": 31
        },
        {
          "name": "Hisham Aljadhey",
          "works": 30
        },
        {
          "name": "Ahmed Awaisu",
          "works": 25
        },
        {
          "name": "Maryam Farooqui",
          "works": 25
        },
        {
          "name": "Gin Nie Chua",
          "works": 18
        },
        {
          "name": "Noor Syahireen Mohammed",
          "works": 17
        },
        {
          "name": "Muhammad Asif",
          "works": 15
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7141757682",
          "year": 2026,
          "title": "Cost-effectiveness analysis of interprofessional collaboration in management of blood pressure in hemodialysis outpatients with end-stage renal disease",
          "type": "article",
          "venue": "Pharmacia",
          "cited_by_count": 0,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Pharmaceutical Practices and Patient Outcomes",
            "Interprofessional Education and Collaboration"
          ]
        },
        {
          "openalex_id": "W7116774680",
          "year": 2025,
          "title": "ASSESSING THE DISTRIBUTION OF SELF-PAYING INNOVATIVE ONCOLOGY MEDICINES AMONG CANCER PATIENTS",
          "type": "article",
          "venue": "Jurnal Administrasi Kesehatan Indonesia",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Pharmaceutical Economics and Policy",
            "Advanced Breast Cancer Therapies"
          ]
        },
        {
          "openalex_id": "W4407758642",
          "year": 2025,
          "title": "Cost-Effectiveness Analysis of Idursulfase for the Long-Term Treatment of Hunter Syndrome Using a Partitioned-Survival Model Approach in R",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 1,
          "topics": [
            "Lysosomal Storage Disorders Research",
            "Autoimmune and Inflammatory Disorders Research",
            "Leprosy Research and Treatment"
          ]
        },
        {
          "openalex_id": "W4416994380",
          "year": 2025,
          "title": "Cost-Utility Analyses of Hemodialysis, Peritoneal Dialysis, and Kidney Transplantation in Patients with End-Stage Kidney Disease: A Systematic Review",
          "type": "review",
          "venue": "ClinicoEconomics and Outcomes Research",
          "cited_by_count": 3,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Renal Transplantation Outcomes and Treatments",
            "Chronic Kidney Disease and Diabetes"
          ]
        },
        {
          "openalex_id": "W4412136183",
          "year": 2025,
          "title": "Development of a Youth-Centred Online Mental Health Education Module Based on Intervention Mapping",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Social and Behavioral Studies",
            "Digital Mental Health Interventions",
            "Psychology of Development and Education"
          ]
        },
        {
          "openalex_id": "W4417479990",
          "year": 2025,
          "title": "EE267 Cost-Effectiveness of Peripheral Neuropathy Screening in Malaysian Adults With Thalassemia: An Integrated Modeling Approach",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Hemoglobinopathies and Related Disorders",
            "Myeloproliferative Neoplasms: Diagnosis and Treatment",
            "Hereditary Neurological Disorders"
          ]
        },
        {
          "openalex_id": "W267761703",
          "year": 2000,
          "title": "10.51847/RhjgufdHI3",
          "type": "article",
          "venue": "Time to knit",
          "cited_by_count": 9,
          "topics": [
            "Mosquito-borne diseases and control",
            "Viral Infections and Vectors",
            "Dengue and Mosquito Control Research"
          ]
        },
        {
          "openalex_id": "W1529283086",
          "year": 2005,
          "title": "PIN21 SELF ASSESSED HEALTH-RELATED QUALITY OF LIFE AMONG HIV PATIENT IN UK",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Impact and Responses",
            "Chronic Disease Management Strategies",
            "HIV-related health complications and treatments"
          ]
        },
        {
          "openalex_id": "W1723401856",
          "year": 2007,
          "title": "Can systematic assessment of patients' quality of life influence optimisation of HIV treatment?",
          "type": "article",
          "venue": "ORCA Online Research @Cardiff (Cardiff University)",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV/AIDS Impact and Responses",
            "HIV-related health complications and treatments"
          ]
        },
        {
          "openalex_id": "W593870421",
          "year": 2007,
          "title": "Economic evaluation of initial HAART regimen for HIV patients",
          "type": "dissertation",
          "venue": "ORCA Online Research @Cardiff (Cardiff University)",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV/AIDS drug development and treatment",
            "HIV-related health complications and treatments"
          ]
        },
        {
          "openalex_id": "W2124575324",
          "year": 2009,
          "title": "The role of pharmacists in developing countries: the current scenario in Pakistan",
          "type": "article",
          "venue": "Human Resources for Health",
          "cited_by_count": 264,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Antibiotic Use and Resistance",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W2096828556",
          "year": 2010,
          "title": "Public knowledge and attitudes towards antibiotic usage: a cross-sectional study among the general public in the state of Penang, Malaysia",
          "type": "article",
          "venue": "The Journal of Infection in Developing Countries",
          "cited_by_count": 245,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pharmaceutical and Antibiotic Environmental Impacts",
            "Bacterial Identification and Susceptibility Testing"
          ]
        },
        {
          "openalex_id": "W2159339457",
          "year": 2010,
          "title": "The eight-item Morisky Medication Adherence Scale MMAS: Translation and validation of the Malaysian version",
          "type": "article",
          "venue": "Diabetes Research and Clinical Practice",
          "cited_by_count": 232,
          "topics": [
            "Medication Adherence and Compliance",
            "Diabetes Management and Education",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W2068377285",
          "year": 2012,
          "title": "A cross sectional assessment of knowledge, attitude and practice towards Hepatitis B among healthy population of Quetta, Pakistan",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 224,
          "topics": [
            "Hepatitis B Virus Studies",
            "Hepatitis C virus research",
            "Blood donation and transfusion practices"
          ]
        },
        {
          "openalex_id": "W2036339171",
          "year": 2011,
          "title": "Diabetes knowledge, medication adherence and glycemic control among patients with type 2 diabetes",
          "type": "article",
          "venue": "International Journal of Clinical Pharmacy",
          "cited_by_count": 224,
          "topics": [
            "Medication Adherence and Compliance",
            "Pharmacology and Nanomedicine Research",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2767473732",
          "year": 2017,
          "title": "Systematic review of economic burden of heart failure",
          "type": "review",
          "venue": "Heart Failure Reviews",
          "cited_by_count": 154,
          "topics": [
            "Heart Failure Treatment and Management",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1980904706",
          "year": 2009,
          "title": "A survey exploring knowledge and perceptions of general practitioners towards the use of generic medicines in the northern state of Malaysia",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 128,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Quality and Counterfeiting"
          ]
        },
        {
          "openalex_id": "W4235967645",
          "year": 2009,
          "title": "Consumers’ views on generic medicines: a review of the literature",
          "type": "article",
          "venue": "International Journal of Pharmacy Practice",
          "cited_by_count": 108,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical industry and healthcare",
            "Intellectual Property and Patents"
          ]
        }
      ]
    }
  },
  {
    "name": "Ataru Igarashi",
    "member_affiliation": "The University of Tokyo",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5071771037",
      "display_name": "Ataru Igarashi",
      "orcid": "0000-0001-6307-6916",
      "reported_affiliation": "University of Tokyo Health Sciences",
      "works_count": 371,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 81
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 23
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 22
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 21
        },
        {
          "topic": "Pharmacy and Medical Practices",
          "works": 18
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 17
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 15
        },
        {
          "topic": "SARS-CoV-2 and COVID-19 Research",
          "works": 14
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 13
        },
        {
          "topic": "Respiratory viral infections research",
          "works": 12
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 12
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 11
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kiichiro Tsutani",
          "works": 31
        },
        {
          "name": "Ayako Shoji",
          "works": 26
        },
        {
          "name": "Takashi Fukuda",
          "works": 22
        },
        {
          "name": "Lida Teng",
          "works": 22
        },
        {
          "name": "Kosuke Iwasaki",
          "works": 22
        },
        {
          "name": "Shunya Ikeda",
          "works": 21
        },
        {
          "name": "Tomomi Takeshima",
          "works": 18
        },
        {
          "name": "Takeru Shiroiwa",
          "works": 15
        },
        {
          "name": "Yusuke Kajimoto",
          "works": 13
        },
        {
          "name": "Takeo Nakayama",
          "works": 12
        },
        {
          "name": "Hiroshi Yoshihara",
          "works": 12
        },
        {
          "name": "Shigeyuki Nakaji",
          "works": 11
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7143285394",
          "year": 2026,
          "title": "Author’s reply to ‘Trends in Usage and Drug Costs of Immune-Checkpoint Inhibitors in Japan’",
          "type": "article",
          "venue": "Japanese Journal of Clinical Oncology",
          "cited_by_count": 0,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Economic and Financial Impacts of Cancer",
            "CAR-T cell therapy research"
          ]
        },
        {
          "openalex_id": "W7166137959",
          "year": 2026,
          "title": "CO136 THE ASSOCIATION BETWEEN PNEUMOCOCCAL VACCINATION HISTORY AND THE INCIDENCE OF PNEUMONIA AND HEALTHCARE RESOURSE USE IN RURAL RESIDENTS IN JAPAN",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Pneumonia and Respiratory Infections",
            "Nosocomial Infections in ICU",
            "Medicine and Dermatology Studies History"
          ]
        },
        {
          "openalex_id": "W7161064886",
          "year": 2026,
          "title": "Correction: Association of health literacy with quality of life and health outcomes among school-age children in Japan: A cross-sectional study",
          "type": "erratum",
          "venue": "PLoS ONE",
          "cited_by_count": 0,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Childhood Cancer Survivors' Quality of Life",
            "School Health and Nursing Education"
          ]
        },
        {
          "openalex_id": "W7170174232",
          "year": 2026,
          "title": "Diet-related quality of life is associated with health-related quality of life: a nationwide online cohort study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Nutritional Studies and Diet",
            "Nutrition and Health in Aging",
            "Food Security and Health in Diverse Populations"
          ]
        },
        {
          "openalex_id": "W7166155732",
          "year": 2026,
          "title": "EE196 ANALYSIS OF THE RELATIONSHIP BETWEEN PHYSICIAN DENSITY AND HEALTHCARE EXPENDITURE IN JAPAN:USING LARGE-SCALE REAL-WORLD DATA OF EMPLOYMENT-BASED HEALTH INSURANCE CLAIMS (WELLNESS STAR DATABASE)",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Workplace Health and Well-being",
            "Medical Coding and Health Information",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W7166132637",
          "year": 2026,
          "title": "EE301 COST EFFECTIVENESS ANALYSIS OF ADULT PNEUMOCOCCAL VACCINES INCLUDING PCV21 AND PCV20 TO OPTIMIZE NATIONAL IMMUNIZATION PROGRAM IN JAPAN",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Pneumonia and Respiratory Infections",
            "Respiratory viral infections research",
            "Influenza Virus Research Studies"
          ]
        },
        {
          "openalex_id": "W2404919518",
          "year": 1969,
          "title": "A respiratory adaptation of the Ama.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 9,
          "topics": [
            "Animal Vocal Communication and Behavior",
            "Avian ecology and behavior"
          ]
        },
        {
          "openalex_id": "W2430897734",
          "year": 1981,
          "title": "[The dental folk remedies in the folklore of Shinetsu district (author's transl)].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Pediatric health and respiratory diseases"
          ]
        },
        {
          "openalex_id": "W2395869607",
          "year": 1984,
          "title": "[Clinical efficacy of cefpimizole in inflammatory diseases in the field of gynecology].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Reproductive System and Pregnancy",
            "Pregnancy and Medication Impact",
            "Endometriosis Research and Treatment"
          ]
        },
        {
          "openalex_id": "W2416897364",
          "year": 1985,
          "title": "[Use of cefminox in infections in the field of obstetrics and gynecology].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Pregnancy and Medication Impact",
            "Drug-Induced Adverse Reactions"
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
          "openalex_id": "W2163142498",
          "year": 2013,
          "title": "The 14-item health literacy scale for Japanese adults (HLS-14)",
          "type": "article",
          "venue": "Environmental Health and Preventive Medicine",
          "cited_by_count": 251,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Text Readability and Simplification",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2035511549",
          "year": 2015,
          "title": "Relationship between health literacy, health information access, health behavior, and health status in Japanese people",
          "type": "article",
          "venue": "Patient Education and Counseling",
          "cited_by_count": 212,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Health Sciences Research and Education",
            "School Health and Nursing Education"
          ]
        },
        {
          "openalex_id": "W2090602898",
          "year": 2010,
          "title": "Potentially inappropriate medication use in elderly Japanese patients",
          "type": "article",
          "venue": "The American journal of geriatric pharmacotherapy",
          "cited_by_count": 175,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Medication Adherence and Compliance",
            "Pharmacy and Medical Practices"
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
        },
        {
          "openalex_id": "W2172023244",
          "year": 2013,
          "title": "WTP for a QALY and health states: More money for severer health states?",
          "type": "article",
          "venue": "Cost Effectiveness and Resource Allocation",
          "cited_by_count": 139,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2980531114",
          "year": 2019,
          "title": "Epidemiological characteristics of rheumatoid arthritis in Japan: Prevalence estimates using a nationwide population-based questionnaire survey",
          "type": "article",
          "venue": "Modern Rheumatology",
          "cited_by_count": 95,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies",
            "Traditional Chinese Medicine Studies",
            "Mycobacterium research and diagnosis"
          ]
        }
      ]
    }
  },
  {
    "name": "Aureliano Finch",
    "member_affiliation": "EuroQol Office, EuroQol Research Foundation",
    "is_member": true,
    "projects": [
      {
        "project_id": "122-RA",
        "title": "An exploratory study on the use of the recall period and the impact of different formats in two fluctuating conditions",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1927-RA",
        "title": "Testing the EQ-HWB-S modifications in a multi-country mixed population",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "20170210",
        "title": "Testing the impact of potential bolt-ons on preferences using pairwise choices: A pilot study.",
        "working_group": "Descriptive Systems, Valuation"
      },
      {
        "project_id": "20190460",
        "title": "Valuation of the EQ-5D-5L in Italy",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5055927783",
      "display_name": "Aureliano Paolo Finch",
      "orcid": "0000-0003-1438-321X",
      "reported_affiliation": "EuroQol Research Foundation",
      "works_count": 47,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 37
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 15
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 5
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 4
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 4
        },
        {
          "topic": "Health Education and Validation",
          "works": 4
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 3
        },
        {
          "topic": "Traumatic Brain Injury Research",
          "works": 3
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 2
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 2
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 2
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Clara Mukuria",
          "works": 8
        },
        {
          "name": "Bram Roudijk",
          "works": 6
        },
        {
          "name": "Claudio Jommi",
          "works": 6
        },
        {
          "name": "Fanni Rencz",
          "works": 6
        },
        {
          "name": "John Brazier",
          "works": 5
        },
        {
          "name": "Brendan Mulhern",
          "works": 5
        },
        {
          "name": "Samar Farid",
          "works": 5
        },
        {
          "name": "Sahar Al Shabasy",
          "works": 4
        },
        {
          "name": "Maggie Abbassi",
          "works": 4
        },
        {
          "name": "Janine Verstraete",
          "works": 4
        },
        {
          "name": "Michela Meregaglia",
          "works": 3
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 3
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
          "openalex_id": "W4410553486",
          "year": 2025,
          "title": "Developing and testing a patient-reported outcome measure for patients with sleep disturbances using EQ-5D and condition-specific bolt-ons: a mixed method study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4411119891",
          "year": 2025,
          "title": "Development and Use of Cognition Bolt-Ons for the EQ-5D-3L and EQ-5D-5L: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Traumatic Brain Injury Research"
          ]
        },
        {
          "openalex_id": "W4417479813",
          "year": 2025,
          "title": "EPH92 Evaluating Performance of the Experimental EQ-TIPS (V3) for Assessing Infants and Toddlers With Acute Infections: A Mixed-Methods Approach of Cognitive Debriefing and Psychometric Testing",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Infant Development and Preterm Care",
            "Childhood Cancer Survivors' Quality of Life",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        },
        {
          "openalex_id": "W4413354774",
          "year": 2025,
          "title": "Exploring subjective constructions of quality of life in patients, carers and the healthy general public: a Q-methodological study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Q Methodology Applications",
            "Psychological Well-being and Life Satisfaction",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4417481846",
          "year": 2025,
          "title": "PCR162 Multinational Qualitative Testing of the Experimental EuroQol Toddler and Infant Populations (EQ-TIPS) Instrument",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W2411115121",
          "year": 1997,
          "title": "Therapeutic Touch and wound healing",
          "type": "article",
          "venue": "Journal of Wound Care",
          "cited_by_count": 11,
          "topics": [
            "Wound Healing and Treatments",
            "Surgical Sutures and Adhesives"
          ]
        },
        {
          "openalex_id": "W1992125252",
          "year": 2014,
          "title": "BRICS’ role in global health and the promotion of universal health coverage: the debate continues",
          "type": "article",
          "venue": "Bulletin of the World Health Organization",
          "cited_by_count": 15,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Healthcare Systems and Reforms",
            "Global Health Workforce Issues"
          ]
        },
        {
          "openalex_id": "W2336860564",
          "year": 2015,
          "title": "BRICS countries and the global movement for universal health coverage",
          "type": "article",
          "venue": "Health Policy and Planning",
          "cited_by_count": 36,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W1596038392",
          "year": 2015,
          "title": "Comparative effectiveness of Mitraclip plus medical therapy versus medical therapy alone in high-risk surgical patients: a comprehensive review",
          "type": "article",
          "venue": "Expert Review of Medical Devices",
          "cited_by_count": 3,
          "topics": [
            "Cardiac Valve Diseases and Treatments",
            "Heart Failure Treatment and Management",
            "Cardiac pacing and defibrillation studies"
          ]
        },
        {
          "openalex_id": "W4205139067",
          "year": 2022,
          "title": "Development of an EQ-5D Value Set for India Using an Extended Design (DEVINE) Study: The Indian 5-Level Version EQ-5D Value Set",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 131,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Quality and Management"
          ]
        },
        {
          "openalex_id": "W2618633361",
          "year": 2017,
          "title": "What is the evidence for the performance of generic preference-based measures? A systematic overview of reviews",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 123,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Behavioral and Psychological Studies"
          ]
        },
        {
          "openalex_id": "W3211171162",
          "year": 2021,
          "title": "An EQ-5D-5L value set for Italy using videoconferencing interviews and feasibility of a new mode of administration",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 91,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2735037954",
          "year": 2017,
          "title": "An Exploratory Study on Using Principal-Component Analysis and Confirmatory Factor Analysis to Identify Bolt-On Dimensions: The EQ-5D Case Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 90,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Sensory Analysis and Statistical Methods",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2887050320",
          "year": 2018,
          "title": "Selecting Bolt-On Dimensions for the EQ-5D: Examining Their Contribution to Health-Related Quality of Life",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 52,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W3138121773",
          "year": 2021,
          "title": "Methods Used to Identify, Test, and Assess Impact on Preferences of Bolt-Ons: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 51,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Safety Warnings and Signage",
            "Quality and Management Systems"
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
          "openalex_id": "W3106837058",
          "year": 2020,
          "title": "Selecting Bolt-on Dimensions for the EQ-5D: Testing the Impact of Hearing, Sleep, Cognition, Energy, and Relationships on Preferences Using Pairwise Choices",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 44,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health, psychology, and well-being"
          ]
        }
      ]
    }
  },
  {
    "name": "Ava Hoogenboom",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1934-TVG",
        "title": "Research visit Melbourne School of Population and Global Health of the University of Melbourne.",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5117116214",
      "display_name": "Ava F H Hoogenboom",
      "orcid": "0009-0004-2252-454X",
      "reported_affiliation": "Erasmus University Rotterdam",
      "works_count": 2,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 2
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 2
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 1
        },
        {
          "topic": "Global Health Care Issues",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Stefan A. Lipman",
          "works": 2
        },
        {
          "name": "Vivian Reckers‐Droog",
          "works": 1
        },
        {
          "name": "Werner Brouwer",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4409377800",
          "year": 2025,
          "title": "Loss aversion in EQ-5D-Y-3L: does it explain differences in willingness to trade-off life years in adults and children?",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4412755063",
          "year": 2025,
          "title": "Nothing about us, without us? A reflection on and call for involving children in the process of valuing child health",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Delphi Technique in Research"
          ]
        }
      ]
    }
  }
]
