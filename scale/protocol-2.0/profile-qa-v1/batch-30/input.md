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
    "name": "Klas Goran Sahlen",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20180770",
        "title": "An EQ-5D-5L value set for the Swedish population",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5069574274",
      "display_name": "Klas-Göran Sahlèn",
      "orcid": "0000-0002-3975-4868",
      "reported_affiliation": "",
      "works_count": 71,
      "top_topics": [
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 12
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Global Health Care Issues",
          "works": 5
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 4
        },
        {
          "topic": "Frailty in Older Adults",
          "works": 4
        },
        {
          "topic": "Workplace Health and Well-being",
          "works": 4
        },
        {
          "topic": "Disability Rights and Representation",
          "works": 4
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 4
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 4
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 3
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 3
        },
        {
          "topic": "Mobile Health and mHealth Applications",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Lars Lindholm",
          "works": 22
        },
        {
          "name": "Haleluya Moshi",
          "works": 11
        },
        {
          "name": "Fredrik Norström",
          "works": 10
        },
        {
          "name": "Gunnevi Sundelin",
          "works": 9
        },
        {
          "name": "Ann Sörlin",
          "works": 9
        },
        {
          "name": "Sun Sun",
          "works": 8
        },
        {
          "name": "Kim Bảo Giang",
          "works": 8
        },
        {
          "name": "Hoàng Văn Minh",
          "works": 7
        },
        {
          "name": "Curt Löfgren",
          "works": 7
        },
        {
          "name": "Magnus Zingmark",
          "works": 6
        },
        {
          "name": "Vu Quynh",
          "works": 5
        },
        {
          "name": "Anita Pettersson-Strömbäck",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166783566",
          "year": 2026,
          "title": "CHALLENGES IN REHABILITATION AND PREVENTION OF TRAUMATIC SPINAL CORD INJURY INCIDENTS IN TANZANIA RURAL AREA",
          "type": "conference-paper",
          "venue": "World Physiotherapy Congress Archive",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7166733708",
          "year": 2026,
          "title": "MAKING LIFE POSSIBLE WITH SPINAL CORD INJURY IN POOR RURAL SETTINGS OF LOW-INCOME COUNTRIES: THE CASE OF KILIMANJARO - TANZANIA",
          "type": "conference-paper",
          "venue": "World Physiotherapy Congress Archive",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7166741158",
          "year": 2026,
          "title": "OCCURRENCE AND CLINICAL OUTCOMES OF TRAUMATIC SPINAL CORD INJURY IN RURAL KILIMANJARO, TANZANIA: A ONE-YEAR PROSPECTIVE STUDY",
          "type": "conference-paper",
          "venue": "World Physiotherapy Congress Archive",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4413445802",
          "year": 2025,
          "title": "Expanded and unclear responsibilities: the evolving role of home care workers as a lifeline during the COVID-19 pandemic -a focus group interview study",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 0,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "COVID-19 and Mental Health",
            "Healthcare professionals’ stress and burnout"
          ]
        },
        {
          "openalex_id": "W4406782345",
          "year": 2025,
          "title": "In-home work environment for home care workers in Northern Sweden before and during the Covid-19 pandemic",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 1,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Infection Control and Ventilation",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W4410872046",
          "year": 2025,
          "title": "KAMSO – ett hälsoekonomiskt kalkylverktyg när evidens saknas",
          "type": "article",
          "venue": "Socialmedicinsk tidskrift",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2076807719",
          "year": 1995,
          "title": "Distance from the Primary Health Center: A GIS method to study geographical access to health care",
          "type": "article",
          "venue": "Journal of Medical Systems",
          "cited_by_count": 47,
          "topics": [
            "Public Health Policies and Education",
            "Data-Driven Disease Surveillance",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W1965757126",
          "year": 1997,
          "title": "Individuals living in areas with high background radon: a GIS method to identify populations at risk",
          "type": "article",
          "venue": "Computer Methods and Programs in Biomedicine",
          "cited_by_count": 16,
          "topics": [
            "Radioactivity and Radon Measurements",
            "Radioactive contamination and transfer",
            "Data-Driven Disease Surveillance"
          ]
        },
        {
          "openalex_id": "W221703584",
          "year": 2002,
          "title": "Hälsa På-projektet : Effekter av förebyggande hembesök hos pigga pensionärer i Nordmaling",
          "type": "report",
          "venue": "KTH Publication Database DiVA (KTH Royal Institute of Technology)",
          "cited_by_count": 1,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Research in Social Sciences"
          ]
        },
        {
          "openalex_id": "W574886231",
          "year": 2005,
          "title": "Implementering av verksamhet med förebyggande hembesök: : Nordmalings kommun - primärvården i Nordmaling",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Research in Social Sciences"
          ]
        },
        {
          "openalex_id": "W2947893598",
          "year": 2019,
          "title": "Does unemployment contribute to poorer health-related quality of life among Swedish adults?",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 169,
          "topics": [
            "Employment and Welfare Studies",
            "Health disparities and outcomes",
            "Occupational and environmental lung diseases"
          ]
        },
        {
          "openalex_id": "W2180327715",
          "year": 2015,
          "title": "A cost-effectiveness study of person-centered integrated heart failure and palliative home care: Based on a randomized controlled trial",
          "type": "article",
          "venue": "Palliative Medicine",
          "cited_by_count": 133,
          "topics": [
            "Heart Failure Treatment and Management",
            "Palliative Care and End-of-Life Issues",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W3013295362",
          "year": 2020,
          "title": "An EQ-5D-5L Value Set for Vietnam",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 112,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2169087111",
          "year": 2014,
          "title": "Primary healthcare system capacities for responding to storm and flood-related health problems: a case study from a rural district in central Vietnam",
          "type": "article",
          "venue": "Global Health Action",
          "cited_by_count": 71,
          "topics": [
            "Disaster Response and Management",
            "Disaster Management and Resilience",
            "Facility Location and Emergency Management"
          ]
        },
        {
          "openalex_id": "W2751535768",
          "year": 2017,
          "title": "Traumatic spinal cord injury in the north-east Tanzania – describing incidence, etiology and clinical outcomes retrospectively",
          "type": "article",
          "venue": "Global Health Action",
          "cited_by_count": 60,
          "topics": [
            "Spinal Cord Injury Research",
            "Spinal Dysraphism and Malformations",
            "Disability Rights and Representation"
          ]
        },
        {
          "openalex_id": "W3010625789",
          "year": 2020,
          "title": "The burden of high workload on the health-related quality of life among home care workers in Northern Sweden",
          "type": "article",
          "venue": "International Archives of Occupational and Environmental Health",
          "cited_by_count": 58,
          "topics": [
            "Workplace Health and Well-being",
            "Geriatric Care and Nursing Homes",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W1506048853",
          "year": 2006,
          "title": "Preventive home visits postpone mortality – a controlled trial with time-limited results",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 46,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Frailty in Older Adults",
            "Health disparities and outcomes"
          ]
        }
      ]
    }
  },
  {
    "name": "KM Vermeulen",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2016700",
        "title": "Selecting health attributes; the patients perspective",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5110324582",
      "display_name": "KM Vermeulen",
      "orcid": "",
      "reported_affiliation": "University Medical Center Groningen",
      "works_count": 4,
      "top_topics": [
        {
          "topic": "Pelvic floor disorders treatments",
          "works": 2
        },
        {
          "topic": "Endometriosis Research and Treatment",
          "works": 1
        },
        {
          "topic": "Menopause: Health Impacts and Treatments",
          "works": 1
        },
        {
          "topic": "Urinary Tract Infections Management",
          "works": 1
        },
        {
          "topic": "Pressure Ulcer Prevention and Management",
          "works": 1
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 1
        },
        {
          "topic": "Nutrition and Health in Aging",
          "works": 1
        },
        {
          "topic": "Transplantation: Methods and Outcomes",
          "works": 1
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 1
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 1
        },
        {
          "topic": "Child and Adolescent Psychosocial and Emotional Development",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "MY Berger",
          "works": 2
        },
        {
          "name": "Janny H. Dekker",
          "works": 2
        },
        {
          "name": "Cmcr Panman",
          "works": 1
        },
        {
          "name": "Marian Wiegersma",
          "works": 1
        },
        {
          "name": "BJ Kollen",
          "works": 1
        },
        {
          "name": "Yvonne Lisman‐van Leeuwen",
          "works": 1
        },
        {
          "name": "Ellen Visser",
          "works": 1
        },
        {
          "name": "E.J. Messelink",
          "works": 1
        },
        {
          "name": "AJ Schram",
          "works": 1
        },
        {
          "name": "Geertruida H. de Bock",
          "works": 1
        },
        {
          "name": "Wendy Post",
          "works": 1
        },
        {
          "name": "Wim van der Bij",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W2767149438",
          "year": 2017,
          "title": "Value Health With A Mobile APP: The Infant Health-Related Quality Of Life Instrument",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Infant Development and Preterm Care",
            "Delphi Technique in Research",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        },
        {
          "openalex_id": "W2271532185",
          "year": 2016,
          "title": "Cost‐effectiveness of a pro‐active approach of urinary incontinence in women",
          "type": "article",
          "venue": "BJOG An International Journal of Obstetrics & Gynaecology",
          "cited_by_count": 13,
          "topics": [
            "Pelvic floor disorders treatments",
            "Urinary Tract Infections Management",
            "Pressure Ulcer Prevention and Management"
          ]
        },
        {
          "openalex_id": "W2300062853",
          "year": 2016,
          "title": "Two‐year effects and cost‐effectiveness of pelvic floor muscle training in mild pelvic organ prolapse: a randomised controlled trial in primary care",
          "type": "article",
          "venue": "BJOG An International Journal of Obstetrics & Gynaecology",
          "cited_by_count": 58,
          "topics": [
            "Pelvic floor disorders treatments",
            "Endometriosis Research and Treatment",
            "Menopause: Health Impacts and Treatments"
          ]
        },
        {
          "openalex_id": "W1975911778",
          "year": 2003,
          "title": "PRP18 ANALYSIS OF LONGITUDINAL CHANGES IN QUALITY OF LIFE BEFORE AND AFTER LUNG TRANSPLANTATION USING A MULTI-LEVEL MODEL",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Nutrition and Health in Aging",
            "Transplantation: Methods and Outcomes"
          ]
        }
      ]
    }
  },
  {
    "name": "Knut Stavem",
    "member_affiliation": "Akershus University Hospital",
    "is_member": true,
    "projects": [
      {
        "project_id": "1816-RA",
        "title": "Validity of breathing and cognition bolt-ons for the EQ-5D instrument in non-hospitalized patients after COVID-19",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5033845511",
      "display_name": "Knut Stavem",
      "orcid": "0000-0003-4512-8000",
      "reported_affiliation": "University of Oslo",
      "works_count": 287,
      "top_topics": [
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 40
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 36
        },
        {
          "topic": "Long-Term Effects of COVID-19",
          "works": 23
        },
        {
          "topic": "Venous Thromboembolism Diagnosis and Management",
          "works": 19
        },
        {
          "topic": "Epilepsy research and treatment",
          "works": 17
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 16
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 15
        },
        {
          "topic": "Pharmacological Effects and Toxicity Studies",
          "works": 14
        },
        {
          "topic": "Respiratory Support and Mechanisms",
          "works": 13
        },
        {
          "topic": "Cardiovascular and exercise physiology",
          "works": 11
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 10
        },
        {
          "topic": "Cardiac Health and Mental Health",
          "works": 9
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Waleed Ghanima",
          "works": 25
        },
        {
          "name": "Gunnar Einvik",
          "works": 21
        },
        {
          "name": "Øyvind Jervan",
          "works": 16
        },
        {
          "name": "Jan Erikssen",
          "works": 15
        },
        {
          "name": "Jostein Gleditsch",
          "works": 15
        },
        {
          "name": "Kjetil Steine",
          "works": 15
        },
        {
          "name": "Mazdak Tavoly",
          "works": 12
        },
        {
          "name": "Amund Gulsvik",
          "works": 12
        },
        {
          "name": "Stein Erik Utvåg",
          "works": 11
        },
        {
          "name": "Ole Geir Solberg",
          "works": 11
        },
        {
          "name": "Ole Morten Rønning",
          "works": 11
        },
        {
          "name": "Liv Ariane Augestad",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7131349142",
          "year": 2026,
          "title": "Correction: Validity of EQ-5D-5L breathing and cognition bolt-ons in non-hospitalized patients after COVID-19",
          "type": "erratum",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Long-Term Effects of COVID-19",
            "Intensive Care Unit Cognitive Disorders",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W7165558492",
          "year": 2026,
          "title": "Long-term chest CT abnormalities up to 4.5 years after COVID-19 hospitalization and their association with dyspnea and fatigue: a prospective cohort study",
          "type": "article",
          "venue": "Respiratory Research",
          "cited_by_count": 0,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 Clinical Research Studies",
            "Pneumothorax, Barotrauma, Emphysema"
          ]
        },
        {
          "openalex_id": "W7125939843",
          "year": 2026,
          "title": "Stress Echocardiography to Detect Exercise Pulmonary Hypertension in Patients With Chronic Thromboembolic Pulmonary Disease",
          "type": "article",
          "venue": "Pulmonary Medicine",
          "cited_by_count": 0,
          "topics": [
            "Pulmonary Hypertension Research and Treatments",
            "Cardiovascular and exercise physiology",
            "Cardiac Valve Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W7119518577",
          "year": 2026,
          "title": "Validity of EQ-5D-5L breathing and cognition bolt-ons in non-hospitalized patients after COVID-19",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4407906910",
          "year": 2025,
          "title": "Bjørn Mikael Hokland",
          "type": "article",
          "venue": "Tidsskrift for Den norske legeforening",
          "cited_by_count": 0,
          "topics": [
            "European and International Law Studies",
            "History and advancements in chemistry"
          ]
        },
        {
          "openalex_id": "W4407132274",
          "year": 2025,
          "title": "Cardiac events and procedures following COVID-19 compared with other pneumonias: a national register study",
          "type": "article",
          "venue": "Open Heart",
          "cited_by_count": 3,
          "topics": [
            "COVID-19 Clinical Research Studies",
            "Long-Term Effects of COVID-19",
            "Pericarditis and Cardiac Tamponade"
          ]
        },
        {
          "openalex_id": "W2415941892",
          "year": 1988,
          "title": "[Retrospective diagnosis of epidemic nephropathy].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis Viruses Studies and Epidemiology",
            "Parvovirus B19 Infection Studies"
          ]
        },
        {
          "openalex_id": "W187201068",
          "year": 1989,
          "title": "[Information technology in health care. A new industrial policy program].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Electronic Health Records Systems"
          ]
        },
        {
          "openalex_id": "W2413788617",
          "year": 1989,
          "title": "[Medical expert systems. What are they and how should we organize our efforts?].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Electronic Health Records Systems",
            "Medical Coding and Health Information",
            "Machine Learning in Healthcare"
          ]
        },
        {
          "openalex_id": "W3151215443",
          "year": 1990,
          "title": "Prepaid financing of primary health care in Guinea-Bissau: an assessment of 18 village health posts",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 3,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "HIV/AIDS Impact and Responses"
          ]
        },
        {
          "openalex_id": "W2047564829",
          "year": 2010,
          "title": "Health-related quality of life in diabetes: The associations of complications with EQ-5D scores",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 385,
          "topics": [
            "Diabetes Management and Education",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Research"
          ]
        },
        {
          "openalex_id": "W3112559917",
          "year": 2020,
          "title": "Dyspnoea, lung function and CT findings 3 months after hospital admission for COVID-19",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 354,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 Clinical Research Studies",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W3107877162",
          "year": 2020,
          "title": "Persistent symptoms 1.5–6 months after COVID-19 in non-hospitalised subjects: a population-based cohort study",
          "type": "article",
          "venue": "Thorax",
          "cited_by_count": 295,
          "topics": [
            "Long-Term Effects of COVID-19",
            "Psychosomatic Disorders and Their Treatments",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W2053720649",
          "year": 2007,
          "title": "Consequences of antiepileptic drug withdrawal: A randomized, double‐blind study (Akershus Study)",
          "type": "article",
          "venue": "Epilepsia",
          "cited_by_count": 208,
          "topics": [
            "Epilepsy research and treatment",
            "Pharmacological Effects and Toxicity Studies",
            "Alcoholism and Thiamine Deficiency"
          ]
        },
        {
          "openalex_id": "W2595294727",
          "year": 2017,
          "title": "Measurement properties and normative data for the Norwegian SF-36: results from a general population survey",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 204,
          "topics": [
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W3174941847",
          "year": 2021,
          "title": "Cardiopulmonary exercise capacity and limitations 3 months after COVID-19 hospitalisation",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 183,
          "topics": [
            "Long-Term Effects of COVID-19",
            "Cardiovascular and exercise physiology",
            "Chronic Obstructive Pulmonary Disease (COPD) Research"
          ]
        },
        {
          "openalex_id": "W2622468719",
          "year": 2017,
          "title": "Charlson comorbidity index derived from chart review or administrative data: agreement and prediction of mortality in intensive care patients",
          "type": "article",
          "venue": "Clinical Epidemiology",
          "cited_by_count": 173,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Frailty in Older Adults",
            "Cardiac, Anesthesia and Surgical Outcomes"
          ]
        },
        {
          "openalex_id": "W2076370391",
          "year": 2008,
          "title": "Cutpoints for mild, moderate and severe pain in patients with osteoarthritis of the hip or knee ready for joint replacement surgery",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 164,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Pain Management and Opioid Use",
            "Anesthesia and Pain Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Kompal Sinha",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "430-RA",
        "title": "Socioeconomic disadvantage, COVID symptom persistence and health-related quality of life EQ-5D: An analysis for India",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5026880787",
      "display_name": "Kompal Sinha",
      "orcid": "0000-0003-4318-6100",
      "reported_affiliation": "International Labour Organization",
      "works_count": 93,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 15
        },
        {
          "topic": "Income, Poverty, and Inequality",
          "works": 15
        },
        {
          "topic": "Economics of Agriculture and Food Markets",
          "works": 14
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 11
        },
        {
          "topic": "Poverty, Education, and Child Welfare",
          "works": 11
        },
        {
          "topic": "Gender, Labor, and Family Dynamics",
          "works": 10
        },
        {
          "topic": "Hearing Loss and Rehabilitation",
          "works": 10
        },
        {
          "topic": "Hearing Impairment and Communication",
          "works": 8
        },
        {
          "topic": "Social and Economic Development in India",
          "works": 7
        },
        {
          "topic": "Agricultural risk and resilience",
          "works": 7
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 6
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Ranjan Ray",
          "works": 20
        },
        {
          "name": "Jeff Richardson",
          "works": 13
        },
        {
          "name": "Angelo Iezzi",
          "works": 12
        },
        {
          "name": "Yuanyuan Gu",
          "works": 12
        },
        {
          "name": "Amita Majumder",
          "works": 10
        },
        {
          "name": "Bonny Parkinson",
          "works": 9
        },
        {
          "name": "Henry Cutler",
          "works": 9
        },
        {
          "name": "Nyamdavaa Byambadorj",
          "works": 8
        },
        {
          "name": "Munir Khan",
          "works": 7
        },
        {
          "name": "Anam Bilgrami",
          "works": 7
        },
        {
          "name": "Anurag Sharma",
          "works": 6
        },
        {
          "name": "John McKie",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7163742387",
          "year": 2026,
          "title": "<p>Final manuscript 20 May Tex.</p>",
          "type": "dataset",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7163741934",
          "year": 2026,
          "title": "<p>Structure of resilience.</p>",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7163745384",
          "year": 2026,
          "title": "<p>This is the supporting file for Appendix Tables.</p>",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Delphi Technique in Research",
            "Survey Methodology and Nonresponse",
            "Focus Groups and Qualitative Methods"
          ]
        },
        {
          "openalex_id": "W7123360420",
          "year": 2026,
          "title": "Disability onset, earnings and income dynamics: examining the role of hearing loss in working-age adults",
          "type": "article",
          "venue": "Applied Economics",
          "cited_by_count": 0,
          "topics": [
            "Retirement, Disability, and Employment",
            "Hearing Impairment and Communication",
            "Hearing Loss and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W7164826134",
          "year": 2026,
          "title": "Expanding Access to Oral Contraceptive Pills: Do Consumers Prefer Over-the-Counter Availability?",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 0,
          "topics": [
            "Reproductive Health and Contraception",
            "Reproductive Health and Technologies",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W7127434385",
          "year": 2026,
          "title": "From entry to persistence: Socio-emotional skills and entrepreneurial profiles",
          "type": "article",
          "venue": "Journal of Behavioral and Experimental Economics",
          "cited_by_count": 0,
          "topics": [
            "Entrepreneurship Studies and Influences",
            "Migration, Ethnicity, and Economy",
            "Family Business Performance and Succession"
          ]
        },
        {
          "openalex_id": "W631880384",
          "year": 2000,
          "title": "NGOs and Socio- Economic Development Opportunities",
          "type": "book",
          "venue": "Medical Entomology and Zoology",
          "cited_by_count": 10,
          "topics": [
            "International Development and Aid",
            "Religion, Society, and Development"
          ]
        },
        {
          "openalex_id": "W1485848884",
          "year": 2005,
          "title": "Household characteristics and calorie intake in rural India: a quantile regression approach",
          "type": "report",
          "venue": "ANU Open Research (Australian National University)",
          "cited_by_count": 11,
          "topics": [
            "Economics of Agriculture and Food Markets",
            "Income, Poverty, and Inequality",
            "Agricultural risk and resilience"
          ]
        },
        {
          "openalex_id": "W840252781",
          "year": 2006,
          "title": "Opening the Black Box of Household Labour Supply: Is Household Behaviour Unitary or Collective? [PhD Thesis]",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Employment and Welfare Studies",
            "Labor market dynamics and wage inequality",
            "Gender, Labor, and Family Dynamics"
          ]
        },
        {
          "openalex_id": "W2269718095",
          "year": 2006,
          "title": "Opening the Black Box of Individual Labour Supply: Is Individual Behaviour Asymmetric for Rural India? [PhD Thesis]",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Gender, Labor, and Family Dynamics",
            "Income, Poverty, and Inequality",
            "Fiscal Policy and Economic Growth"
          ]
        },
        {
          "openalex_id": "W1983572683",
          "year": 2014,
          "title": "Modelling utility weights for the Assessment of Quality of Life (AQoL)-8D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 130,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W1995616067",
          "year": 2010,
          "title": "Predicting Time Trade-Off Health State Valuations of Adolescents in Four Pacific Countries Using the Assessment of Quality-of-Life (AQoL-6D) Instrument",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 96,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Obesity, Physical Activity, Diet"
          ]
        },
        {
          "openalex_id": "W2550290040",
          "year": 2014,
          "title": "Rangarajan Committee Report on Poverty Measurement Another Lost Opportunity",
          "type": "article",
          "venue": "",
          "cited_by_count": 94,
          "topics": [
            "Income, Poverty, and Inequality",
            "Social and Economic Development in India",
            "Agricultural risk and resilience"
          ]
        },
        {
          "openalex_id": "W2734697286",
          "year": 2017,
          "title": "Pricing as a means of controlling alcohol consumption",
          "type": "article",
          "venue": "British Medical Bulletin",
          "cited_by_count": 71,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Gambling Behavior and Treatments",
            "Smoking Behavior and Cessation"
          ]
        },
        {
          "openalex_id": "W2129881175",
          "year": 2012,
          "title": "Calculating Rural‐Urban Food Price Differentials from Unit Values in Household Expenditure Surveys: A Comparison with Existing Methods and A New Procedure",
          "type": "article",
          "venue": "American Journal of Agricultural Economics",
          "cited_by_count": 62,
          "topics": [
            "Economics of Agriculture and Food Markets",
            "Agricultural Economics and Policy",
            "Gender, Labor, and Family Dynamics"
          ]
        },
        {
          "openalex_id": "W2318070225",
          "year": 2016,
          "title": "A longitudinal study of the cost of food in Victoria influenced by geography and nutritional quality",
          "type": "article",
          "venue": "Australian and New Zealand Journal of Public Health",
          "cited_by_count": 49,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Food Security and Health in Diverse Populations",
            "Social Issues and Policies"
          ]
        },
        {
          "openalex_id": "W3133756306",
          "year": 2021,
          "title": "Fuel poverty policy: Go big or go home insulation",
          "type": "article",
          "venue": "Energy Economics",
          "cited_by_count": 48,
          "topics": [
            "Energy and Environment Impacts",
            "Energy, Environment, and Transportation Policies",
            "Energy, Environment, Economic Growth"
          ]
        },
        {
          "openalex_id": "W2128144867",
          "year": 2015,
          "title": "A lifecycle perspective of stock market performance and wellbeing",
          "type": "article",
          "venue": "Journal of Economic Behavior & Organization",
          "cited_by_count": 37,
          "topics": [
            "Health disparities and outcomes",
            "Psychological Well-being and Life Satisfaction",
            "Employment and Welfare Studies"
          ]
        }
      ]
    }
  },
  {
    "name": "Koonal Shah",
    "member_affiliation": "NICE",
    "is_member": true,
    "projects": [
      {
        "project_id": "117-RA",
        "title": "Conceptual challenges in the valuation of health in children and adolescents",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2015050",
        "title": "Important aspects of (full) health not captured by EQ-5D",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015440",
        "title": "Valuing health states 'in context'",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016150",
        "title": "Two MSc student project placements on EuroQol-related topics",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016370",
        "title": "A qualitative approach to understanding what aspects of health are important to people",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20190490",
        "title": "ISPOR Issue Panel on child health valuation",
        "working_group": "Youth, Education and Outreach"
      },
      {
        "project_id": "20190660",
        "title": "Funding application: Early Career Researcher Meeting",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "82-RA",
        "title": "Valuing health in children: an examination of age, perspective and methodological effects (REVISED)",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5083575745",
      "display_name": "Koonal Shah",
      "orcid": "0000-0002-4927-7858",
      "reported_affiliation": "National Institute for Health and Care Excellence",
      "works_count": 150,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 124
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 49
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 32
        },
        {
          "topic": "Global Health Care Issues",
          "works": 26
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 17
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 10
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 9
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 8
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 5
        },
        {
          "topic": "Climate Change and Health Impacts",
          "works": 5
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 5
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nancy Devlin",
          "works": 48
        },
        {
          "name": "Brendan Mulhern",
          "works": 21
        },
        {
          "name": "Ben van Hout",
          "works": 14
        },
        {
          "name": "Louise Longworth",
          "works": 14
        },
        {
          "name": "David Mott",
          "works": 12
        },
        {
          "name": "Adrian Towse",
          "works": 11
        },
        {
          "name": "Yan Feng",
          "works": 10
        },
        {
          "name": "Aki Tsuchiya",
          "works": 10
        },
        {
          "name": "Jon Sussex",
          "works": 10
        },
        {
          "name": "Mark Oppe",
          "works": 9
        },
        {
          "name": "Martina Garau",
          "works": 9
        },
        {
          "name": "Juan Manuel Ramos-Goñi",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7128209919",
          "year": 2026,
          "title": "Are Health Gains to Children and Adolescents More Important Than Health Gains to Adults? A Person Trade-Off Study",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 1,
          "topics": [
            "Pediatric Pain Management Techniques",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W7125606515",
          "year": 2026,
          "title": "Valuing Child and Adolescent Health States to Derive Utilities for Use in Economic Evaluation: A Good Practices Report of an ISPOR Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4413138927",
          "year": 2025,
          "title": "Distributional Cost-Effectiveness Analysis and Health Technology Assessment at NICE",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4417482087",
          "year": 2025,
          "title": "EE422 Estimating Quality-Adjusted Life Expectancy by Ethnicity for Application in Distributional Cost-Effectiveness Analysis",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Insurance, Mortality, Demography, Risk Management"
          ]
        },
        {
          "openalex_id": "W4410463015",
          "year": 2025,
          "title": "How well do participants understand the questions asked in the Online Personal Utility Functions (OPUF) approach? A cognitive debrief of the EQ-HWB-S (EQ Health and Wellbeing Short version) valuation",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4414841370",
          "year": 2025,
          "title": "The Influence of Perspective on the Valuation of the EQ-5D-Y-3L: A Comparison Using the OPUF Tool and a Discrete Choice Experiment",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2800990164",
          "year": 2009,
          "title": "Assessment and Appraisal of Oncology Medicines: NICE's Approach and International HTA Experience",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W1981360761",
          "year": 2009,
          "title": "Severity of illness and priority setting in healthcare: A review of the literature",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 224,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W3123132299",
          "year": 2010,
          "title": "A Comparison of Alternative Variants of the Lead and Lag Time TTO",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W3123136406",
          "year": 2010,
          "title": "A Comparison of Alternative Variants of the Lead and Lag Time TTO",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2343426002",
          "year": 2017,
          "title": "Valuing health-related quality of life: An EQ-5D-5L value set for England",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 1416,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2337676734",
          "year": 2016,
          "title": "EuroQol Protocols for Time Trade-Off Valuation of Health Outcomes",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 246,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W3017192319",
          "year": 2020,
          "title": "International Valuation Protocol for the EQ-5D-Y-3L",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 161,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2883512800",
          "year": 2018,
          "title": "Utility Values for Health States in Ireland: A Value Set for the EQ-5D-5L",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 136,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2885527383",
          "year": 2018,
          "title": "Valuation of EuroQol Five-Dimensional Questionnaire, Youth Version (EQ-5D-Y) and EuroQol Five-Dimensional Questionnaire, Three-Level Version (EQ-5D-3L) Health States: The Impact of Wording and Perspective",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 115,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2788887762",
          "year": 2018,
          "title": "Comparing the UK EQ-5D-3L and English EQ-5D-5L Value Sets",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 109,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W1977877370",
          "year": 2014,
          "title": "Valuing health at the end of life: A stated preference discrete choice experiment",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 101,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        }
      ]
    }
  }
]
