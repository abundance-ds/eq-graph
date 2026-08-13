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
    "name": "Gerkens Sophie",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20170491",
        "title": "Valuing Health-Related Quality of Life: An EQ-5D-5L Value Set for Belgium: Request for budget extention",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5063513647",
      "display_name": "Sophie Gerkens",
      "orcid": "0000-0001-6211-3471",
      "reported_affiliation": "Belgian Health Care Knowledge Centre (KCE)",
      "works_count": 154,
      "top_topics": [
        {
          "topic": "Healthcare Policy and Management",
          "works": 17
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 14
        },
        {
          "topic": "Healthcare Systems and Practices",
          "works": 12
        },
        {
          "topic": "Hepatitis C virus research",
          "works": 11
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 10
        },
        {
          "topic": "Cardiovascular Effects of Exercise",
          "works": 8
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 7
        },
        {
          "topic": "Biosimilars and Bioanalytical Methods",
          "works": 7
        },
        {
          "topic": "Global Health Care Issues",
          "works": 6
        },
        {
          "topic": "Hepatitis B Virus Studies",
          "works": 6
        },
        {
          "topic": "Liver Disease Diagnosis and Treatment",
          "works": 6
        },
        {
          "topic": "Cardiac pacing and defibrillation studies",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nicolas Bouckaert",
          "works": 34
        },
        {
          "name": "Irina Cleemput",
          "works": 24
        },
        {
          "name": "Mélanie Lefèvre",
          "works": 24
        },
        {
          "name": "Carl Devos",
          "works": 23
        },
        {
          "name": "Caroline Obyn",
          "works": 22
        },
        {
          "name": "Nancy Thiry",
          "works": 22
        },
        {
          "name": "Chris De Laet",
          "works": 22
        },
        {
          "name": "Claire Beguin",
          "works": 21
        },
        {
          "name": "Imgard Vinck",
          "works": 21
        },
        {
          "name": "Lorena San Miguel",
          "works": 18
        },
        {
          "name": "Charline Maertens de Noordhout",
          "works": 17
        },
        {
          "name": "Hans Van Brabandt",
          "works": 17
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7155171870",
          "year": 2026,
          "title": "Health system performance assessment (HSPA): A first step in the assessment of environmental sustainability",
          "type": "book",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Environmental and Social Impact Assessments",
            "Healthcare Facilities Design and Sustainability",
            "Sustainable Development and Environmental Policy"
          ]
        },
        {
          "openalex_id": "W7155172154",
          "year": 2026,
          "title": "Health system performance assessment (HSPA): A first step in the assessment of environmental sustainability",
          "type": "book",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Environmental and Social Impact Assessments",
            "Healthcare Facilities Design and Sustainability",
            "Sustainable Development and Environmental Policy"
          ]
        },
        {
          "openalex_id": "W7155173810",
          "year": 2026,
          "title": "Health system performance assessment (HSPA): A first step in the assessment of environmental sustainability",
          "type": "book",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Environmental and Social Impact Assessments",
            "Healthcare Facilities Design and Sustainability",
            "Sustainable Development and Environmental Policy"
          ]
        },
        {
          "openalex_id": "W7168153724",
          "year": 2026,
          "title": "Le paiement à la performance",
          "type": "book",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Primary Care and Health Outcomes",
            "Healthcare Systems and Practices",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W7168192967",
          "year": 2026,
          "title": "Pay-for-performance",
          "type": "book",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Community Development and Social Impact",
            "Healthcare innovation and challenges",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W7168211879",
          "year": 2026,
          "title": "Pay-for-performance",
          "type": "book",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Primary Care and Health Outcomes",
            "Patient Satisfaction in Healthcare",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4406863182",
          "year": 2006,
          "title": "Farmacologische en chirurgische behandeling van obesitas",
          "type": "book",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "Pharmacology and Obesity Treatment",
            "Diet and metabolism studies",
            "Obesity and Health Practices"
          ]
        },
        {
          "openalex_id": "W4406861475",
          "year": 2006,
          "title": "Pharmacological and surgical treatment of obesity",
          "type": "book",
          "venue": "",
          "cited_by_count": 4,
          "topics": [
            "Pharmacology and Obesity Treatment"
          ]
        },
        {
          "openalex_id": "W4406865193",
          "year": 2006,
          "title": "Traitement pharmacologique et chirurgical de l'obésité",
          "type": "book",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "Pharmacology and Obesity Treatment"
          ]
        },
        {
          "openalex_id": "W1728209451",
          "year": 2007,
          "title": "A health economic model to assess the cost-effectiveness of pegylated interferon alpha-2a and ribavirin in patients with moderate chronic hepatitis C and persistently normal alanine aminotransferase levels.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 14,
          "topics": [
            "Hepatitis C virus research",
            "Hepatitis B Virus Studies",
            "Hemophilia Treatment and Research"
          ]
        },
        {
          "openalex_id": "W2255890739",
          "year": 2010,
          "title": "Belgium: Health System Review.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 197,
          "topics": [
            "Healthcare Policy and Management",
            "Healthcare innovation and challenges",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W2565587258",
          "year": 2016,
          "title": "Pharmaceutical regulation in 15 European countries review.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 105,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical industry and healthcare",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2112066550",
          "year": 2008,
          "title": "Comparison of three instruments assessing the quality of economic evaluations: A practical exercise on economic evaluations of the surgical treatment of obesity",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 81,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Bariatric Surgery and Outcomes",
            "Obesity and Health Practices"
          ]
        },
        {
          "openalex_id": "W2111250144",
          "year": 2008,
          "title": "Steroid-Free, Tacrolimus-Basiliximab Immunosuppression in Pediatric Liver Transplantation: Clinical and Pharmacoeconomic Study in 50 Children",
          "type": "article",
          "venue": "Liver Transplantation",
          "cited_by_count": 77,
          "topics": [
            "Organ Transplantation Techniques and Outcomes",
            "Renal Transplantation Outcomes and Treatments",
            "Liver Disease and Transplantation"
          ]
        },
        {
          "openalex_id": "W3159695207",
          "year": 2021,
          "title": "In the wake of the pandemic: Preparing for Long COVID",
          "type": "book",
          "venue": "ePrints Soton (University of Southampton)",
          "cited_by_count": 67,
          "topics": [
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W2080261918",
          "year": 2013,
          "title": "Are biosimilars the next tool to guarantee cost-containment for pharmaceutical expenditures?",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 64,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W4289835526",
          "year": 2022,
          "title": "An EQ-5D-5L Value Set for Belgium",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 56,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2341947744",
          "year": 2016,
          "title": "Harms and benefits of screening young people to prevent sudden cardiac death",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 55,
          "topics": [
            "Cardiovascular Effects of Exercise",
            "Sports injuries and prevention",
            "Cardiac electrophysiology and arrhythmias"
          ]
        }
      ]
    }
  },
  {
    "name": "Girma Tekle Gebremariam",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "343-RA",
        "title": "The Psychometric Properties of the EQ-5D-5L among Ethiopian Cervical Cancer Patients: A Longitudinal Study",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5008650274",
      "display_name": "Girma Tekle Gebremariam",
      "orcid": "0000-0002-2747-7955",
      "reported_affiliation": "Addis Ababa University",
      "works_count": 22,
      "top_topics": [
        {
          "topic": "Cancer survivorship and care",
          "works": 5
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 4
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 3
        },
        {
          "topic": "Endometrial and Cervical Cancer Treatments",
          "works": 3
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 2
        },
        {
          "topic": "Cancer-related cognitive impairment studies",
          "works": 2
        },
        {
          "topic": "Cervical Cancer and HPV Research",
          "works": 2
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 2
        },
        {
          "topic": "Neutropenia and Cancer Infections",
          "works": 2
        },
        {
          "topic": "Health Education and Validation",
          "works": 2
        },
        {
          "topic": "Antifungal resistance and susceptibility",
          "works": 2
        },
        {
          "topic": "Parasitic Diseases Research and Treatment",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Gebremedhin Beedemariam Gebretekle",
          "works": 12
        },
        {
          "name": "Beate Sander",
          "works": 7
        },
        {
          "name": "Atalay Mulu Fentie",
          "works": 6
        },
        {
          "name": "Kebede Beyene",
          "works": 4
        },
        {
          "name": "Teferi Gedif Fenta",
          "works": 4
        },
        {
          "name": "Eskinder Eshetu Ali",
          "works": 4
        },
        {
          "name": "Liya Teklu Araya",
          "works": 3
        },
        {
          "name": "Dessale Abate Beyene",
          "works": 3
        },
        {
          "name": "Tamrat Assefa Tadesse",
          "works": 3
        },
        {
          "name": "Abraham Gebregziabiher Welie",
          "works": 2
        },
        {
          "name": "Abel Tesfaye Anshabo",
          "works": 2
        },
        {
          "name": "Wondemagegnhu Tigeneh",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7162318366",
          "year": 2026,
          "title": "Health-related quality of life and associated factors among patients with chronic obstructive pulmonary disease in Addis Ababa, Ethiopia: a multicentre cross-sectional study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Chronic Disease Management Strategies",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W7163050445",
          "year": 2026,
          "title": "Mapping health-related quality of life measurement tools in Africa: a scoping review",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W7154848528",
          "year": 2025,
          "title": "Reliability of the Amharic Version of the Medication Adherence Report Scale and Beliefs about Medicines Questionnaire in Patients with Asthma in Ethiopia.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Medication Adherence and Compliance",
            "Asthma and respiratory diseases",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W4390499811",
          "year": 2024,
          "title": "Health-related quality of life and its associated factors among hemophilia patients: experience from Ethiopian Hemophilia Treatment Centre",
          "type": "article",
          "venue": "Journal of Pharmaceutical Health Care and Sciences",
          "cited_by_count": 8,
          "topics": [
            "Hemophilia Treatment and Research",
            "Blood donation and transfusion practices",
            "Blood transfusion and management"
          ]
        },
        {
          "openalex_id": "W4391825226",
          "year": 2024,
          "title": "Impact of pharmacist-led interventions on medication-related problems among patients treated for cancer: A systematic review and meta-analysis of randomized control trials",
          "type": "review",
          "venue": "Research in Social and Administrative Pharmacy",
          "cited_by_count": 23,
          "topics": [
            "Medication Adherence and Compliance",
            "Pharmaceutical Practices and Patient Outcomes",
            "Cancer-related cognitive impairment studies"
          ]
        },
        {
          "openalex_id": "W4394980355",
          "year": 2024,
          "title": "Prevalence, Characteristics, and Treatment Pattern of Menstrual-Related Headache Among Undergraduate Health Sciences Students at Addis Ababa University, Ethiopia",
          "type": "article",
          "venue": "International Journal of Women s Health",
          "cited_by_count": 0,
          "topics": [
            "Menstrual Health and Disorders",
            "Migraine and Headache Studies",
            "Menopause: Health Impacts and Treatments"
          ]
        },
        {
          "openalex_id": "W2980843729",
          "year": 2018,
          "title": "Brief Fatigue Inventory--Amharic Version",
          "type": "dataset",
          "venue": "PsycTESTS Dataset",
          "cited_by_count": 0,
          "topics": [
            "Effects of Vibration on Health"
          ]
        },
        {
          "openalex_id": "W2799505404",
          "year": 2018,
          "title": "Validation of the Amharic Version of the Brief Fatigue Inventory for Assessment of Cancer-Related Fatigue in Ethiopian Cancer Patients",
          "type": "article",
          "venue": "Journal of Pain and Symptom Management",
          "cited_by_count": 17,
          "topics": [
            "Cancer survivorship and care",
            "Economic and Financial Impacts of Cancer",
            "Cancer-related cognitive impairment studies"
          ]
        },
        {
          "openalex_id": "W2951328609",
          "year": 2019,
          "title": "European Organization for Research and Treatment of Cancer--Cervical Cancer Specific Quality of Life Module; Amharic Version",
          "type": "dataset",
          "venue": "PsycTESTS Dataset",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2917316172",
          "year": 2019,
          "title": "Reliability and validity of the Amharic version of European Organization for Research and Treatment of cervical Cancer module for the assessment of health related quality of life in women with cervical cancer in Addis Ababa, Ethiopia",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 18,
          "topics": [
            "Cancer survivorship and care",
            "Endometrial and Cervical Cancer Treatments",
            "Cervical Cancer and HPV Research"
          ]
        },
        {
          "openalex_id": "W3011126225",
          "year": 2020,
          "title": "Health-related quality of life and associated factors among cervical cancer patients at Tikur Anbessa specialized hospital, Addis Ababa, Ethiopia",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 49,
          "topics": [
            "Cancer survivorship and care",
            "Endometrial and Cervical Cancer Treatments",
            "Cervical Cancer and HPV Research"
          ]
        },
        {
          "openalex_id": "W4212772886",
          "year": 2022,
          "title": "Health-related quality of life of patients with type 2 diabetes mellitus at a tertiary care hospital in Ethiopia",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 47,
          "topics": [
            "Diabetes Management and Education",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W4303961709",
          "year": 2022,
          "title": "Health-related quality of life and treatment satisfaction of patients with cardiovascular disease in Ethiopia",
          "type": "article",
          "venue": "Frontiers in Public Health",
          "cited_by_count": 20,
          "topics": [
            "Cardiac Health and Mental Health",
            "Cardiovascular Health and Risk Factors",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W3027022519",
          "year": 2020,
          "title": "&lt;p&gt;Assessment of Quality of Care Using Information on Patient Satisfaction at Adult Oncology Center of Tikur Anbessa Specialized Hospital, Ethiopia: A Cross-Sectional Study&lt;/p&gt;",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 12,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Primary Care and Health Outcomes",
            "Healthcare Quality and Satisfaction"
          ]
        },
        {
          "openalex_id": "W4313454989",
          "year": 2022,
          "title": "Cost-effectiveness of pegfilgrastim versus filgrastim for prevention of chemotherapy-induced febrile neutropenia in patients with lymphoma: a systematic review",
          "type": "review",
          "venue": "BMC Health Services Research",
          "cited_by_count": 8,
          "topics": [
            "Neutropenia and Cancer Infections",
            "Sepsis Diagnosis and Treatment",
            "Bacterial Identification and Susceptibility Testing"
          ]
        }
      ]
    }
  },
  {
    "name": "Gisela Cristiane Miyamoto",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2308-VS",
        "title": "The development of the national value set for the EQ-5D-5L in Brazil",
        "working_group": "Valuation"
      },
      {
        "project_id": "2410-RA",
        "title": "Cross-Cultural Adaptation and Psychometric Properties Testing of the EuroQol Toddler and Infant Populations (EQ-TIPS) Health-Related Quality of Life Measure in Brazilian Children",
        "working_group": "Youth"
      },
      {
        "project_id": "2468-RA",
        "title": "Psychometric properties of the EQ-HWB-9 in Brazilian frail and non-frail older adults",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2482-EO",
        "title": "Estimating an EQ-5D-Y-3L value set for Brazil and comparing the measurement properties of the EQ-5D-Y-3L, EQ-5D-Y- 5L and CHU9D in children and adolescents ",
        "working_group": "Dissemination, OA fee"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5024629360",
      "display_name": "Gisela Cristiane Miyamoto",
      "orcid": "0000-0002-6826-4278",
      "reported_affiliation": "Universidade Cidade de São Paulo",
      "works_count": 61,
      "top_topics": [
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 36
        },
        {
          "topic": "Sports injuries and prevention",
          "works": 16
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 9
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 9
        },
        {
          "topic": "Fibromyalgia and Chronic Fatigue Syndrome Research",
          "works": 8
        },
        {
          "topic": "Occupational Health and Performance",
          "works": 8
        },
        {
          "topic": "Myofascial pain diagnosis and treatment",
          "works": 5
        },
        {
          "topic": "Telemedicine and Telehealth Implementation",
          "works": 4
        },
        {
          "topic": "Sports Performance and Training",
          "works": 4
        },
        {
          "topic": "Lower Extremity Biomechanics and Pathologies",
          "works": 4
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 3
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Cristina Maria Nunes Cabral",
          "works": 37
        },
        {
          "name": "Katherinne Ferro Moura Franco",
          "works": 20
        },
        {
          "name": "Tiê Parma Yamato",
          "works": 11
        },
        {
          "name": "Leonardo Oliveira Pena Costa",
          "works": 10
        },
        {
          "name": "Verônica Souza Santos",
          "works": 8
        },
        {
          "name": "Naiane Teixeira Bastos de Oliveira",
          "works": 7
        },
        {
          "name": "Felipe José Jandre dos Reis",
          "works": 7
        },
        {
          "name": "Bruno Tirotti Saragiotto",
          "works": 7
        },
        {
          "name": "Caique de Melo do Espírito Santo",
          "works": 7
        },
        {
          "name": "Iuri Fioratti",
          "works": 5
        },
        {
          "name": "Junior Vitorino Fandim",
          "works": 5
        },
        {
          "name": "Christopher G. Maher",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7162040796",
          "year": 2026,
          "title": "Is telerehabilitation inferior to face-to-face rehabilitation at improving adherence and pain in patients with chronic low back pain? Protocol for a non-inferiority randomized clinical trial with economic evaluation",
          "type": "article",
          "venue": "Trials",
          "cited_by_count": 0,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Telemedicine and Telehealth Implementation",
            "Spinal Cord Injury Research"
          ]
        },
        {
          "openalex_id": "W4415699911",
          "year": 2025,
          "title": "COMPARISON OF RESISTANCE VERSUS AEROBIC EXERCISE DURING HEMODIALYSIS IN CHRONIC RENAL PATIENTS: A RANDOMIZED CONTROLLED TRIAL",
          "type": "article",
          "venue": "Brazilian Journal of Physical Therapy",
          "cited_by_count": 0,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Parathyroid Disorders and Treatments",
            "Nutrition and Health in Aging"
          ]
        },
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
          "openalex_id": "W4415699750",
          "year": 2025,
          "title": "HEALTHCARE COSTS DURING PREGNANCY CONSIDERING WOMEN'S HEALTH: A SYSTEMATIC REVIEW",
          "type": "article",
          "venue": "Brazilian Journal of Physical Therapy",
          "cited_by_count": 1,
          "topics": [
            "Gestational Diabetes Research and Management",
            "Global Maternal and Child Health",
            "Pregnancy and Medication Impact"
          ]
        },
        {
          "openalex_id": "W4415699824",
          "year": 2025,
          "title": "HEALTHCARE COSTS OF NECK PAIN: A SYSTEMATIC REVIEW",
          "type": "article",
          "venue": "Brazilian Journal of Physical Therapy",
          "cited_by_count": 0,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Medical Practices and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W2049694586",
          "year": 2010,
          "title": "Alongamento muscular segmentar melhora função e alinhamento do joelho de indivíduos com síndrome femoropatelar: estudo preliminar",
          "type": "article",
          "venue": "Revista Brasileira de Medicina do Esporte",
          "cited_by_count": 4,
          "topics": [
            "Lower Extremity Biomechanics and Pathologies",
            "Shoulder Injury and Treatment",
            "Sports injuries and prevention"
          ]
        },
        {
          "openalex_id": "W2105059445",
          "year": 2011,
          "title": "The efficacy of the addition of the Pilates method over a minimal intervention in the treatment of chronic nonspecific low back pain: a study protocol of a randomized controlled trial",
          "type": "article",
          "venue": "Journal of Chiropractic Medicine",
          "cited_by_count": 15,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Myofascial pain diagnosis and treatment",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W2119356381",
          "year": 2012,
          "title": "Efficacy of the Addition of Modified Pilates Exercises to a Minimal Intervention in Patients With Chronic Low Back Pain: A Randomized Controlled Trial",
          "type": "article",
          "venue": "Physical Therapy",
          "cited_by_count": 136,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Myofascial pain diagnosis and treatment",
            "Sports injuries and prevention"
          ]
        },
        {
          "openalex_id": "W2134341230",
          "year": 2013,
          "title": "Efficacy of the Pilates method for pain and disability in patients with chronic nonspecific low back pain: a systematic review with meta-analysis",
          "type": "review",
          "venue": "Brazilian Journal of Physical Therapy",
          "cited_by_count": 84,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Occupational Health and Performance",
            "Myofascial pain diagnosis and treatment"
          ]
        },
        {
          "openalex_id": "W2802922258",
          "year": 2018,
          "title": "Cost-effectiveness of exercise therapy in the treatment of non-specific neck pain and low back pain: a systematic review with meta-analysis",
          "type": "review",
          "venue": "British Journal of Sports Medicine",
          "cited_by_count": 162,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W2793871331",
          "year": 2018,
          "title": "Different doses of Pilates-based exercise therapy for chronic low back pain: a randomised controlled trial with economic evaluation",
          "type": "article",
          "venue": "British Journal of Sports Medicine",
          "cited_by_count": 128,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Sports injuries and prevention",
            "Scoliosis diagnosis and treatment"
          ]
        },
        {
          "openalex_id": "W4379260467",
          "year": 2023,
          "title": "Pain catastrophising and kinesiophobia mediate pain and physical function improvements with Pilates exercise in chronic low back pain: a mediation analysis of a randomised controlled trial",
          "type": "article",
          "venue": "Journal of physiotherapy",
          "cited_by_count": 56,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Fibromyalgia and Chronic Fatigue Syndrome Research"
          ]
        },
        {
          "openalex_id": "W2047971917",
          "year": 2014,
          "title": "Efficacy of the addition of interferential current to Pilates method in patients with low back pain: a protocol of a randomized controlled trial",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 31,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Myofascial pain diagnosis and treatment",
            "Sports injuries and prevention"
          ]
        },
        {
          "openalex_id": "W3183416685",
          "year": 2021,
          "title": "Interpretation of trial-based economic evaluations of musculoskeletal physical therapy interventions",
          "type": "article",
          "venue": "Brazilian Journal of Physical Therapy",
          "cited_by_count": 25,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cerebral Palsy and Movement Disorders",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2536895331",
          "year": 2016,
          "title": "Is Interferential Current Before Pilates Exercises More Effective Than Placebo in Patients With Chronic Nonspecific Low Back Pain?",
          "type": "article",
          "venue": "Archives of Physical Medicine and Rehabilitation",
          "cited_by_count": 25,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Sports injuries and prevention",
            "Occupational Health and Performance"
          ]
        }
      ]
    }
  },
  {
    "name": "Goitom Molalign Takele",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1735-RA",
        "title": "Exploring the content validity and acceptability of the EQ-5D-Y-3L and the EQ-5D-Y-5L among children and adolescents with Type 1 diabetes in Ethiopia A qualitative-study",
        "working_group": "Youth"
      },
      {
        "project_id": "227-RA",
        "title": "Comparison of the Afaan-Oromo language version of the EQ-5D-Y-3L and the EQ-5D-Y-5L performance among children and adolescents in Ethiopia",
        "working_group": "Youth"
      },
      {
        "project_id": "317-RA",
        "title": "Investigating the aspects of HRQoL covered by the descriptive system and the added value of the respiratory bolt-ons (EQ-5D-5L+R): breathing problem and limitations in physical activities due to shortness of breath among patients suffering from asthma in Ethiopia: A mixed method study",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "449-RA",
        "title": "Assessing the health of Ethiopian Adolescents using the EQ-5D-Y-3L: A cross-sectional study",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5009462612",
      "display_name": "Goitom Molalign Takele",
      "orcid": "0000-0002-9344-3390",
      "reported_affiliation": "Mekelle University",
      "works_count": 8,
      "top_topics": [
        {
          "topic": "Diabetes Management and Education",
          "works": 2
        },
        {
          "topic": "Trauma and Emergency Care Studies",
          "works": 2
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 2
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 2
        },
        {
          "topic": "Emergency and Acute Care Studies",
          "works": 2
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 2
        },
        {
          "topic": "Nursing care and research",
          "works": 1
        },
        {
          "topic": "Mobile Health and mHealth Applications",
          "works": 1
        },
        {
          "topic": "Global Health and Surgery",
          "works": 1
        },
        {
          "topic": "Nosocomial Infections in ICU",
          "works": 1
        },
        {
          "topic": "Infection Control in Healthcare",
          "works": 1
        },
        {
          "topic": "Surgical site infection prevention",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Birhan Gebresillassie Gebregiorgis",
          "works": 5
        },
        {
          "name": "Kahsu Gebrekirstos Gebrekidan",
          "works": 2
        },
        {
          "name": "Negash Abreha Weldesenbet",
          "works": 2
        },
        {
          "name": "Trudy Sullivan",
          "works": 2
        },
        {
          "name": "Ari Samaranayaka",
          "works": 2
        },
        {
          "name": "Mimmi Åström",
          "works": 2
        },
        {
          "name": "Gashaw Arega",
          "works": 2
        },
        {
          "name": "Sarah Derrett",
          "works": 2
        },
        {
          "name": "Medina Abdulkadir Weharei",
          "works": 1
        },
        {
          "name": "Hiyab T Michael Kidanu",
          "works": 1
        },
        {
          "name": "Tsegalem Hailemariam Ballo",
          "works": 1
        },
        {
          "name": "Kiros Belay Gebrekidan",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7124434023",
          "year": 2026,
          "title": "Generic health-related quality of life instruments among children and adolescents in low- and middle-income countries: a scoping review",
          "type": "article",
          "venue": "Systematic Reviews",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Maternal and Child Health",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W4415370550",
          "year": 2025,
          "title": "The use of generic health-related quality of life instruments among children and adolescents in low- and middle-income countries: a scoping review",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical studies and practices",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Ethics and Legal Issues in Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W3119194455",
          "year": 2021,
          "title": "Assessment patient satisfaction towards emergency medical care and its determinants at Ayder comprehensive specialized hospital, Mekelle, Northern Ethiopia",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 18,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Emergency and Acute Care Studies",
            "Trauma and Emergency Care Studies"
          ]
        },
        {
          "openalex_id": "W3154940998",
          "year": 2021,
          "title": "Diabetes self-care practice and associated factors among type 2 diabetic patients in public hospitals of Tigray regional state, Ethiopia: A multicenter study",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 43,
          "topics": [
            "Diabetes Management and Education",
            "Nursing care and research",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W3185386402",
          "year": 2021,
          "title": "Utilization, Barriers and Determinants of Emergency Medical Services in Mekelle City, Tigray, Ethiopia: A Community-Based Cross-Sectional Study",
          "type": "article",
          "venue": "Open Access Emergency Medicine",
          "cited_by_count": 13,
          "topics": [
            "Trauma and Emergency Care Studies",
            "Global Health and Surgery",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W3118924651",
          "year": 2020,
          "title": "Client’s satisfaction towards emergency medical care at Ayder comprehensive specialized hospital, Mekelle, Ethiopia",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Emergency and Acute Care Studies",
            "Patient Satisfaction in Healthcare",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W3205518323",
          "year": 2020,
          "title": "Diabetes Self-Care Practice, and Associated Factors Among Type 2 Diabetic Patients in Public Hospitals of Tigray Region, Ethiopia",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Education",
            "Chronic Disease Management Strategies",
            "Health, Medicine and Society"
          ]
        },
        {
          "openalex_id": "W3115077389",
          "year": 2020,
          "title": "Prevalence of hospital-acquired infections (HAIs) and associated factors in Ethiopia: a systematic review and meta-analysis protocol",
          "type": "review",
          "venue": "BMJ Open",
          "cited_by_count": 11,
          "topics": [
            "Nosocomial Infections in ICU",
            "Infection Control in Healthcare",
            "Surgical site infection prevention"
          ]
        }
      ]
    }
  },
  {
    "name": "Gouke Bonsel",
    "member_affiliation": "EuroQol Research Foundation",
    "is_member": true,
    "projects": [
      {
        "project_id": "2013150",
        "title": "Non-additive impact of dimensions on the index values of health states: an analysis of interaction effects to avoid misspecification of the value function with unsaturated valuation datasets",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014090",
        "title": "Prevention of misspecification of the EuroQol tariff through optimal choices on design and analysis. An empirical and simulation based analysis using existing datasets.",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016160",
        "title": "Conventional and perceived change in health-related quality of life of trauma patients: what role does recall bias play?",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2016670",
        "title": "Measuring health-related quality of life in trauma patients: what is the added value of extending the EQ-5D3L and the EQ-5D5L with a cognitive domain?",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2016750",
        "title": "EQ-5D-5L in pregnancy. Antenatal and postnatal HRQOL, the impact of poor out",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20170360",
        "title": "PROMs and PREMs, their interaction: bias or added value? On the dependency between EQ5D5L (stand alone PROM), and validated PREMs in a large sample of recently delivering women, ranging from healthy to severely affected",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "238-RA",
        "title": "Population health impact of the COVID-19 pandemic (POPCORN): longitudinal effects of the COVID-19 pandemic on individual's health-related quality of life",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "512-RA",
        "title": "Implementation of a digital survey, and development of an EQ-based patient platform (dashboard) in 2 Dutch longcovid studies focussing on cardiovascular sequelae (Capacity2, Defence)",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "645-RA",
        "title": "Implementation of a digital survey, and development of an EQ-based patient platform (dashboard) in national longcovid study (CORFU) focussing on quality of life",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5047977076",
      "display_name": "Gouke J. Bonsel",
      "orcid": "0000-0002-8364-1086",
      "reported_affiliation": "",
      "works_count": 362,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 71
        },
        {
          "topic": "Maternal and Perinatal Health Interventions",
          "works": 45
        },
        {
          "topic": "Maternal Mental Health During Pregnancy and Postpartum",
          "works": 40
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 33
        },
        {
          "topic": "Pregnancy and preeclampsia studies",
          "works": 29
        },
        {
          "topic": "Gestational Diabetes Research and Management",
          "works": 25
        },
        {
          "topic": "Birth, Development, and Health",
          "works": 25
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 23
        },
        {
          "topic": "Prenatal Screening and Diagnostics",
          "works": 17
        },
        {
          "topic": "Child and Adolescent Health",
          "works": 16
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 15
        },
        {
          "topic": "Maternal and fetal healthcare",
          "works": 15
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Erwin Birnie",
          "works": 81
        },
        {
          "name": "Eric A.P. Steegers",
          "works": 58
        },
        {
          "name": "Juanita A. Haagsma",
          "works": 37
        },
        {
          "name": "Semiha Denktaş",
          "works": 35
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 32
        },
        {
          "name": "Marie‐Louise Essink‐Bot",
          "works": 20
        },
        {
          "name": "Jashvant Poeran",
          "works": 20
        },
        {
          "name": "Suzanne Polinder",
          "works": 19
        },
        {
          "name": "Marcel F. van der Wal",
          "works": 18
        },
        {
          "name": "Otto P. Bleker",
          "works": 17
        },
        {
          "name": "Tanja G. M. Vrijkotte",
          "works": 16
        },
        {
          "name": "Johannes B. Reitsma",
          "works": 14
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7135101514",
          "year": 2026,
          "title": "Psychometric Properties of the EQ-5D-5L in Post-COVID-19 Condition: Results From the Long CORFU Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and Mental Health",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Traumatic Brain Injury Research"
          ]
        },
        {
          "openalex_id": "W4406958353",
          "year": 2025,
          "title": "A head-to-head comparison of the adult EQ-5D-5L and youth EQ-5D-Y-5L in adolescents with idiopathic scoliosis",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Hip disorders and treatments",
            "Foot and Ankle Surgery"
          ]
        },
        {
          "openalex_id": "W4413865180",
          "year": 2025,
          "title": "Development and internal validation of a prediction model for post-COVID-19 condition 2 years after infection—results of the CORFU study",
          "type": "article",
          "venue": "Diagnostic and Prognostic Research",
          "cited_by_count": 1,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 Clinical Research Studies",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W4415299974",
          "year": 2025,
          "title": "Health-related quality of life of adult post COVID-19 condition patients three years after infection and patient characteristics associated with change over time: a longitudinal analysis from the CORFU study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W4410630560",
          "year": 2025,
          "title": "Socioeconomic inequalities in patient-reported outcome measures among total hip and knee arthroplasty patients: a comprehensive analysis of instruments and domains",
          "type": "article",
          "venue": "International Journal for Equity in Health",
          "cited_by_count": 6,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Patient Satisfaction in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4414146329",
          "year": 2025,
          "title": "Two years and counting: a prospective cohort study on the scope and severity of post-COVID symptoms across diverse patient groups in the Netherlands—insights from the CORFU study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 2,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health",
            "Pharmacological Receptor Mechanisms and Effects"
          ]
        },
        {
          "openalex_id": "W2028600951",
          "year": 1990,
          "title": "Orthotopic liver transplantation in The Netherlands. The results and impact of a medical technology assessment",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 12,
          "topics": [
            "Liver Disease and Transplantation",
            "Organ Transplantation Techniques and Outcomes",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2060897967",
          "year": 1990,
          "title": "Valuation of health states by the general public: Feasibility of a standardized measurement procedure",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 45,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W417268899",
          "year": 1991,
          "title": "Methods of medical technology assessment with an application to liver transplantation.",
          "type": "dissertation",
          "venue": "RePub (Erasmus University Rotterdam)",
          "cited_by_count": 8,
          "topics": [
            "Organizational Management and Leadership",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2070566838",
          "year": 1992,
          "title": "ASSESSMENT OF THE QUALITY OF LIFE BEFORE AND FOLLOWING LIVER TRANSPLANTATION",
          "type": "article",
          "venue": "Transplantation",
          "cited_by_count": 81,
          "topics": [
            "Liver Disease and Transplantation",
            "Organ Transplantation Techniques and Outcomes",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W1990166011",
          "year": 2011,
          "title": "Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L)",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 10156,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, psychology, and well-being",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W2092926517",
          "year": 2003,
          "title": "The diagnostic odds ratio: a single indicator of test performance",
          "type": "article",
          "venue": "Journal of Clinical Epidemiology",
          "cited_by_count": 2308,
          "topics": [
            "Meta-analysis and systematic reviews",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W2050436219",
          "year": 2000,
          "title": "A Comparison of Continuous Thalamic Stimulation and Thalamotomy for Suppression of Severe Tremor",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 1045,
          "topics": [
            "Neurological disorders and treatments",
            "Neuroscience and Neural Engineering",
            "Botulinum Toxin and Related Neurological Disorders"
          ]
        },
        {
          "openalex_id": "W4304014077",
          "year": 2022,
          "title": "Estimated Global Proportions of Individuals With Persistent Fatigue, Cognitive, and Respiratory Symptom Clusters Following Symptomatic COVID-19 in 2020 and 2021",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 925,
          "topics": [
            "Long-Term Effects of COVID-19",
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W2029997282",
          "year": 2010,
          "title": "Development of the EQ-5D-Y: a child-friendly version of the EQ-5D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 901,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W2064869088",
          "year": 2010,
          "title": "Feasibility, reliability, and validity of the EQ-5D-Y: results from a multinational study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 475,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W2141882750",
          "year": 2012,
          "title": "Posttraumatic stress symptoms and health-related quality of life: a two year follow up study of injury treated at the emergency department",
          "type": "article",
          "venue": "BMC Psychiatry",
          "cited_by_count": 421,
          "topics": [
            "Trauma and Emergency Care Studies",
            "Posttraumatic Stress Disorder Research",
            "Pediatric Pain Management Techniques"
          ]
        },
        {
          "openalex_id": "W2788315630",
          "year": 2018,
          "title": "Is EQ-5D-5L Better Than EQ-5D-3L? A Head-to-Head Comparison of Descriptive Systems and Value Sets from Seven Countries",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 400,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        }
      ]
    }
  }
]
