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
    "name": "Katy Gallop",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1884-RA",
        "title": "A systematic literature review of the measurement properties of the EQ-5D-5L in conditions with itch to support the IP dossier of the ‘psoriasis bolt-ons’",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2011-RA",
        "title": "Exploring the content validity of the self-confidence and skin irritation bolt-ons in alopecia areata and vitiligo",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2014-RA",
        "title": "Psychometric testing of the EQ-5D-5L and four bolt-ons in chronic urticaria in the US",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2432-BT",
        "title": "Experimental Bolt-on Toolbox - Cognitive debriefing of the UK English source version",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5091811569",
      "display_name": "Katy Gallop",
      "orcid": "0000-0002-6826-3865",
      "reported_affiliation": "Lloyd's",
      "works_count": 77,
      "top_topics": [
        {
          "topic": "Food Allergy and Anaphylaxis Research",
          "works": 11
        },
        {
          "topic": "Allergic Rhinitis and Sensitization",
          "works": 11
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 6
        },
        {
          "topic": "Lysosomal Storage Disorders Research",
          "works": 6
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 5
        },
        {
          "topic": "Parkinson's Disease Mechanisms and Treatments",
          "works": 4
        },
        {
          "topic": "Systemic Lupus Erythematosus Research",
          "works": 3
        },
        {
          "topic": "Epilepsy research and treatment",
          "works": 3
        },
        {
          "topic": "Botulinum Toxin and Related Neurological Disorders",
          "works": 3
        },
        {
          "topic": "Microscopic Colitis",
          "works": 3
        },
        {
          "topic": "Neurogenetic and Muscular Disorders Research",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sarah Acaster",
          "works": 25
        },
        {
          "name": "Andrew Lloyd",
          "works": 18
        },
        {
          "name": "Alasdair MacCulloch",
          "works": 9
        },
        {
          "name": "Annabel Nixon",
          "works": 8
        },
        {
          "name": "Robert Ryan",
          "works": 8
        },
        {
          "name": "Andrea Vereda",
          "works": 8
        },
        {
          "name": "Lena Hubig",
          "works": 7
        },
        {
          "name": "D Wild",
          "works": 7
        },
        {
          "name": "Cicely Kerr",
          "works": 6
        },
        {
          "name": "AJ Lloyd",
          "works": 6
        },
        {
          "name": "Paul Swinburn",
          "works": 5
        },
        {
          "name": "Anna-Katrine Sussex",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7128498687",
          "year": 2026,
          "title": "Complexity of Severity Classification in Hereditary Angioedema",
          "type": "article",
          "venue": "Journal of Allergy and Clinical Immunology",
          "cited_by_count": 0,
          "topics": [
            "Coagulation, Bradykinin, Polyphosphates, and Angioedema",
            "Complement system in diseases",
            "Hemophilia Treatment and Research"
          ]
        },
        {
          "openalex_id": "W7128490038",
          "year": 2026,
          "title": "Perspectives of Healthcare Professionals on the Treatment Landscape of Ocular Redness",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 0,
          "topics": [
            "Ocular Infections and Treatments",
            "Corneal Surgery and Treatments",
            "Ocular Surface and Contact Lens"
          ]
        },
        {
          "openalex_id": "W4415925600",
          "year": 2025,
          "title": "A QUALITATIVE STUDY AND CONCEPTUAL MODEL OF PATIENT EXPERIENCES DURING AND BETWEEN HEREDITARY ANGIOEDEMA ATTACKS.",
          "type": "article",
          "venue": "Annals of Allergy Asthma & Immunology",
          "cited_by_count": 0,
          "topics": [
            "Peripheral Artery Disease Management",
            "Electronic Health Records Systems",
            "Healthcare Technology and Patient Monitoring"
          ]
        },
        {
          "openalex_id": "W4412442851",
          "year": 2025,
          "title": "PCR157 Estimated Impact of Pre-Exposure Prophylaxis for COVID-19 on Quality of Life and Physical Distancing Among Immunocompromised Individuals and Caregivers",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W4406981823",
          "year": 2025,
          "title": "Validation of quality-of-life states in late-infantile and early-juvenile metachromatic leukodystrophy",
          "type": "article",
          "venue": "Molecular Genetics and Metabolism",
          "cited_by_count": 0,
          "topics": [
            "Neuroinflammation and Neurodegeneration Mechanisms",
            "RNA regulation and disease",
            "Neutrophil, Myeloperoxidase and Oxidative Mechanisms"
          ]
        },
        {
          "openalex_id": "W4402275464",
          "year": 2024,
          "title": "Caring for patients with Alagille syndrome: a multinational survey investigating the mental health and financial burden on caregivers",
          "type": "article",
          "venue": "Future Rare Diseases",
          "cited_by_count": 1,
          "topics": [
            "Pediatric Hepatobiliary Diseases and Treatments",
            "Intestinal Malrotation and Obstruction Disorders",
            "Gallbladder and Bile Duct Disorders"
          ]
        },
        {
          "openalex_id": "W1970123263",
          "year": 2008,
          "title": "PMC18 CONCEPTUALISING DISEASE: BUILDING UNIFYING MODELS TO SUPPORT THE DEVELOPMENT OF PROS AND COST-EFFECTIVENESS ANALYSES. A CASE STUDY IN ALZHEIMER—S DISEASE (AD)",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Folate and B Vitamins Research",
            "Liver Disease Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2079682587",
          "year": 2009,
          "title": "Impact of Lennox-Gastaut Syndrome (LGS) on health-related quality of life (HRQL) of patients and caregivers: Literature review",
          "type": "article",
          "venue": "Seizure",
          "cited_by_count": 62,
          "topics": [
            "Epilepsy research and treatment",
            "Neonatal and fetal brain pathology",
            "Hemoglobinopathies and Related Disorders"
          ]
        },
        {
          "openalex_id": "W2162288300",
          "year": 2009,
          "title": "Lennox-Gastaut Syndrome (LGS): Development of conceptual models of health-related quality of life (HRQL) for caregivers and children",
          "type": "article",
          "venue": "Seizure",
          "cited_by_count": 63,
          "topics": [
            "Epilepsy research and treatment",
            "Genetics and Neurodevelopmental Disorders",
            "Pharmacological Effects and Toxicity Studies"
          ]
        },
        {
          "openalex_id": "W2089324806",
          "year": 2009,
          "title": "PND25 THE IMPACT OF LENNOX-GASTAUT SYNDROME (LGS) ON HEALTH RELATED QUALITY OF LIFE – A CONCEPTUAL MODEL",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Fibromyalgia and Chronic Fatigue Syndrome Research"
          ]
        },
        {
          "openalex_id": "W2512716401",
          "year": 2016,
          "title": "Is Pain Perception Altered in People With Depression? A Systematic Review and Meta-Analysis of Experimental Pain Research",
          "type": "review",
          "venue": "Journal of Pain",
          "cited_by_count": 190,
          "topics": [
            "Pain Mechanisms and Treatments",
            "Pain Management and Placebo Effect",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2129634723",
          "year": 2012,
          "title": "Development of a conceptual model of health-related quality of life for systemic lupus erythematosus from the patient's perspective",
          "type": "article",
          "venue": "Lupus",
          "cited_by_count": 83,
          "topics": [
            "Systemic Lupus Erythematosus Research",
            "Rheumatoid Arthritis Research and Therapies",
            "Spondyloarthritis Studies and Treatments"
          ]
        },
        {
          "openalex_id": "W1980438718",
          "year": 2014,
          "title": "A Qualitative Investigation of Patients’ and Caregivers’ Experiences of Severe Sepsis*",
          "type": "article",
          "venue": "Critical Care Medicine",
          "cited_by_count": 72,
          "topics": [
            "Family and Patient Care in Intensive Care Units",
            "Sepsis Diagnosis and Treatment",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W3202938209",
          "year": 2021,
          "title": "Impact of developmental and epileptic encephalopathies on caregivers: A literature review",
          "type": "article",
          "venue": "Epilepsy & Behavior",
          "cited_by_count": 70,
          "topics": [
            "Epilepsy research and treatment",
            "Pharmacological Effects and Toxicity Studies",
            "Neonatal and fetal brain pathology"
          ]
        },
        {
          "openalex_id": "W2067876771",
          "year": 2015,
          "title": "Development of a conceptual model to illustrate the impact of multiple myeloma and its treatment on health-related quality of life",
          "type": "article",
          "venue": "Supportive Care in Cancer",
          "cited_by_count": 67,
          "topics": [
            "Multiple Myeloma Research and Treatments",
            "Cancer survivorship and care",
            "Cancer-related cognitive impairment studies"
          ]
        },
        {
          "openalex_id": "W2101867353",
          "year": 2013,
          "title": "Patient-reported fatigue and its impact on patients with systemic lupus erythematosus",
          "type": "article",
          "venue": "Lupus",
          "cited_by_count": 60,
          "topics": [
            "Systemic Lupus Erythematosus Research",
            "Psoriasis: Treatment and Pathogenesis",
            "T-cell and B-cell Immunology"
          ]
        }
      ]
    }
  },
  {
    "name": "Kelly de Ligt",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2317-RA",
        "title": "One Question Away: Using the EQ-5D-5L to Screen for Emotional Distress in Advanced Melanoma Care",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5000687889",
      "display_name": "Kelly M. de Ligt",
      "orcid": "0000-0001-9218-617X",
      "reported_affiliation": "Tilburg University",
      "works_count": 68,
      "top_topics": [
        {
          "topic": "Cancer survivorship and care",
          "works": 33
        },
        {
          "topic": "Breast Cancer Treatment Studies",
          "works": 21
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 12
        },
        {
          "topic": "Cancer-related cognitive impairment studies",
          "works": 10
        },
        {
          "topic": "Breast Implant and Reconstruction",
          "works": 9
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 9
        },
        {
          "topic": "Cancer Treatment and Pharmacology",
          "works": 8
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 5
        },
        {
          "topic": "Brain Metastases and Treatment",
          "works": 5
        },
        {
          "topic": "Cancer Risks and Factors",
          "works": 4
        },
        {
          "topic": "Reconstructive Surgery and Microvascular Techniques",
          "works": 4
        },
        {
          "topic": "Lymphatic System and Diseases",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sabine Siesling",
          "works": 29
        },
        {
          "name": "Lonneke V. van de Poll‐Franse",
          "works": 28
        },
        {
          "name": "M. Heins",
          "works": 12
        },
        {
          "name": "Joke C. Korevaar",
          "works": 12
        },
        {
          "name": "Belle H. de Rooij",
          "works": 12
        },
        {
          "name": "Janneke Verloop",
          "works": 10
        },
        {
          "name": "Sanne B. Schagen",
          "works": 9
        },
        {
          "name": "Iris Walraven",
          "works": 8
        },
        {
          "name": "Linetta B. Koppert",
          "works": 8
        },
        {
          "name": "E A C Albers",
          "works": 7
        },
        {
          "name": "Iris M. C. van der Ploeg",
          "works": 7
        },
        {
          "name": "Bernhard Holzner",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4410455598",
          "year": 2025,
          "title": "421P Predicting health related quality of life in breast cancer: The EORTC BALANCE study",
          "type": "article",
          "venue": "ESMO Open",
          "cited_by_count": 0,
          "topics": [
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W4407349352",
          "year": 2025,
          "title": "Adverse health effects after breast cancer up to 14 years after diagnosis",
          "type": "article",
          "venue": "The Breast",
          "cited_by_count": 6,
          "topics": [
            "Cancer Risks and Factors",
            "Global Cancer Incidence and Screening",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W4406090011",
          "year": 2025,
          "title": "Corrigendum to ‘Adverse health effects after breast cancer up to 14 years after diagnosis’ [The Breast 61 (2022) 22–28]",
          "type": "erratum",
          "venue": "The Breast",
          "cited_by_count": 0,
          "topics": [
            "Cancer Risks and Factors",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W4414307776",
          "year": 2025,
          "title": "Cross-sectional study of long-term Health-Related Quality of Life in stage III melanoma patients receiving neo-adjuvant versus adjuvant immune checkpoint inhibitors",
          "type": "article",
          "venue": "European Journal of Cancer",
          "cited_by_count": 2,
          "topics": [
            "Cutaneous Melanoma Detection and Management",
            "Cancer Immunotherapy and Biomarkers",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W4408076532",
          "year": 2025,
          "title": "Exploring the integration of patient-reported outcome measures in clinical practice: A cross-sectional survey of EORTC healthcare professionals",
          "type": "article",
          "venue": "European Journal of Cancer",
          "cited_by_count": 8,
          "topics": [
            "Cancer survivorship and care",
            "Global Cancer Incidence and Screening",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4407159803",
          "year": 2025,
          "title": "Improving the Implementation of Patient-Reported Outcome Measure in Clinical Practice: Tackling Current Challenges With Innovative Digital Communication Technologies",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 14,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Cancer survivorship and care",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W195138548",
          "year": 2014,
          "title": "Cost-effectiveness analysis of an alternative follow-up strategy for breast cancer patients that have received breast conserving treatment: referral to the National Screening Programme after one year of regular hospital follow-up compared to regular five-year follow-up at the hospital.",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Global Cancer Incidence and Screening",
            "Economic and Financial Impacts of Cancer",
            "Breast Cancer Treatment Studies"
          ]
        },
        {
          "openalex_id": "W2617534172",
          "year": 2017,
          "title": "Hospital organizational factors affect the use of immediate breast reconstruction after mastectomy for breast cancer in the Netherlands",
          "type": "article",
          "venue": "The Breast",
          "cited_by_count": 35,
          "topics": [
            "Breast Implant and Reconstruction",
            "Breast Cancer Treatment Studies",
            "Reconstructive Surgery and Microvascular Techniques"
          ]
        },
        {
          "openalex_id": "W2767791692",
          "year": 2017,
          "title": "Patients' experiences with decisions on timing of chemotherapy for breast cancer",
          "type": "article",
          "venue": "The Breast",
          "cited_by_count": 10,
          "topics": [
            "Breast Cancer Treatment Studies",
            "Global Cancer Incidence and Screening",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2884673058",
          "year": 2018,
          "title": "Current decisions on neoadjuvant chemotherapy for early breast cancer: Experts’ experiences in the Netherlands",
          "type": "article",
          "venue": "Patient Education and Counseling",
          "cited_by_count": 8,
          "topics": [
            "Breast Cancer Treatment Studies",
            "Breast Lesions and Carcinomas",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W3187456071",
          "year": 2021,
          "title": "Symptom clusters in 1330 survivors of 7 cancer types from the PROFILES registry: A network analysis",
          "type": "article",
          "venue": "Cancer",
          "cited_by_count": 90,
          "topics": [
            "Mental Health Research Topics",
            "Cancer survivorship and care",
            "Cancer-related cognitive impairment studies"
          ]
        },
        {
          "openalex_id": "W2973049984",
          "year": 2019,
          "title": "The impact of health symptoms on health-related quality of life in early-stage breast cancer survivors",
          "type": "article",
          "venue": "Breast Cancer Research and Treatment",
          "cited_by_count": 90,
          "topics": [
            "Cancer survivorship and care",
            "Cancer-related cognitive impairment studies",
            "Lymphatic System and Diseases"
          ]
        },
        {
          "openalex_id": "W3037389741",
          "year": 2020,
          "title": "Long-Term Health-Related Quality of Life after Four Common Surgical Treatment Options for Breast Cancer and the Effect of Complications: A Retrospective Patient-Reported Survey among 1871 Patients",
          "type": "article",
          "venue": "Plastic & Reconstructive Surgery",
          "cited_by_count": 85,
          "topics": [
            "Breast Implant and Reconstruction",
            "Breast Cancer Treatment Studies",
            "Lymphatic System and Diseases"
          ]
        },
        {
          "openalex_id": "W2793065143",
          "year": 2018,
          "title": "Surgical resection versus systemic therapy for breast cancer liver metastases: Results of a European case matched comparison",
          "type": "article",
          "venue": "European Journal of Cancer",
          "cited_by_count": 85,
          "topics": [
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Cancer Cells and Metastasis",
            "Cancer Research and Treatment"
          ]
        },
        {
          "openalex_id": "W4200446586",
          "year": 2021,
          "title": "Adverse health effects after breast cancer up to 14 years after diagnosis",
          "type": "article",
          "venue": "The Breast",
          "cited_by_count": 63,
          "topics": [
            "Cancer survivorship and care",
            "Cancer Risks and Factors",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W4214861727",
          "year": 2022,
          "title": "Visualization formats of patient-reported outcome measures in clinical practice: a systematic review about preferences and interpretation accuracy",
          "type": "review",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 50,
          "topics": [
            "Data Visualization and Analytics",
            "Nursing Diagnosis and Documentation",
            "Art Therapy and Mental Health"
          ]
        },
        {
          "openalex_id": "W3034501693",
          "year": 2020,
          "title": "The added value of immediate breast reconstruction to health-related quality of life of breast cancer patients",
          "type": "article",
          "venue": "European Journal of Surgical Oncology",
          "cited_by_count": 49,
          "topics": [
            "Breast Implant and Reconstruction",
            "Breast Cancer Treatment Studies",
            "Lymphatic System and Diseases"
          ]
        },
        {
          "openalex_id": "W2931660014",
          "year": 2019,
          "title": "Patient-reported health problems and healthcare use after treatment for early-stage breast cancer",
          "type": "article",
          "venue": "The Breast",
          "cited_by_count": 47,
          "topics": [
            "Cancer survivorship and care",
            "Cancer Treatment and Pharmacology",
            "Cancer-related cognitive impairment studies"
          ]
        }
      ]
    }
  },
  {
    "name": "Kidu Gidey",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1627-RA",
        "title": "Health-related quality of life in patients with COVID-19: a protocol for systematic review and meta-analysis of EQ-5D studies",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5040157120",
      "display_name": "Kidu Gidey",
      "orcid": "0000-0002-7363-1327",
      "reported_affiliation": "Mekelle University",
      "works_count": 40,
      "top_topics": [
        {
          "topic": "Epilepsy research and treatment",
          "works": 8
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 7
        },
        {
          "topic": "Pharmacological Effects and Toxicity Studies",
          "works": 6
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 4
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 4
        },
        {
          "topic": "Blood Pressure and Hypertension Studies",
          "works": 3
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 3
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 2
        },
        {
          "topic": "Nosocomial Infections in ICU",
          "works": 2
        },
        {
          "topic": "Surgical site infection prevention",
          "works": 2
        },
        {
          "topic": "Pharmacovigilance and Adverse Drug Reactions",
          "works": 2
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Yirga Legesse Niriayo",
          "works": 20
        },
        {
          "name": "Solomon Weldegebreal Asgedom",
          "works": 15
        },
        {
          "name": "Berhane Yohannes Hailu",
          "works": 9
        },
        {
          "name": "Gebre Teklemariam Demoz",
          "works": 8
        },
        {
          "name": "Tesfay Mehari Atey",
          "works": 6
        },
        {
          "name": "Tesfaye Kassa",
          "works": 4
        },
        {
          "name": "Legese Chelkeba",
          "works": 4
        },
        {
          "name": "Yirga Legesse Nirayo",
          "works": 3
        },
        {
          "name": "Esayas Kebede Gudina",
          "works": 3
        },
        {
          "name": "Nigusse Tesfay",
          "works": 3
        },
        {
          "name": "Meles Tekie Gidey",
          "works": 2
        },
        {
          "name": "Abraham Mamo",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7127295955",
          "year": 2026,
          "title": "Health-related quality of life and associated factors among patients living with epilepsy of Mekelle City Hospitals, Northern Ethiopia: a multicenter observational study",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Epilepsy research and treatment",
            "Psychosomatic Disorders and Their Treatments",
            "Pharmacological Effects and Toxicity Studies"
          ]
        },
        {
          "openalex_id": "W4414751286",
          "year": 2025,
          "title": "Effect of Self‐Care Activities on Blood Pressure Control Among Patients With Hypertension",
          "type": "article",
          "venue": "BioMed Research International",
          "cited_by_count": 1,
          "topics": [
            "Health and Well-being Studies"
          ]
        },
        {
          "openalex_id": "W4414898827",
          "year": 2025,
          "title": "Health-related quality of life in COVID-19 patients: a systematic review and meta-analysis of EQ-5D studies",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 8,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W4411593008",
          "year": 2025,
          "title": "Treatment outcomes, medication adherence and predictors among patients with epilepsy in Mekelle City Hospitals, Ethiopia: a multicentre observational cross-sectional study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 1,
          "topics": [
            "Epilepsy research and treatment",
            "Malaria Research and Control",
            "Hemoglobinopathies and Related Disorders"
          ]
        },
        {
          "openalex_id": "W4390753002",
          "year": 2024,
          "title": "Antimicrobial Use-Related Problems Among Hospitalized Pediatric Patients: A Prospective Observational Study",
          "type": "article",
          "venue": "Infection and Drug Resistance",
          "cited_by_count": 7,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pharmaceutical studies and practices",
            "Antibiotics Pharmacokinetics and Efficacy"
          ]
        },
        {
          "openalex_id": "W4390863498",
          "year": 2024,
          "title": "Drug therapy problems among hospitalized patients with cardiovascular disease",
          "type": "article",
          "venue": "BMC Cardiovascular Disorders",
          "cited_by_count": 12,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Potassium and Related Disorders",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W2186800498",
          "year": 2015,
          "title": "Drug Dose Adjustment Practices in Patients with Renal Impairment at Ayder Referral Hospital, Mekelle, Northern Ethiopia",
          "type": "article",
          "venue": "",
          "cited_by_count": 2,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical Practices and Patient Outcomes",
            "Chronic Kidney Disease and Diabetes"
          ]
        },
        {
          "openalex_id": "W2562435058",
          "year": 2015,
          "title": "Households willingness to pay for improved water services in urban areas: A case study from Nebelet town, Ethiopia",
          "type": "article",
          "venue": "Journal of Development and Agricultural Economics",
          "cited_by_count": 45,
          "topics": [
            "Economic and Environmental Valuation",
            "Water resources management and optimization",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W2598945222",
          "year": 2017,
          "title": "Olanzapine for chemotherapy-induced nausea and vomiting: systematic review and meta-analysis",
          "type": "article",
          "venue": "Pharmacy Practice",
          "cited_by_count": 27,
          "topics": [
            "Nausea and vomiting management",
            "Chemotherapy-induced organ toxicity mitigation",
            "Chemotherapy-related skin toxicity"
          ]
        },
        {
          "openalex_id": "W2601967111",
          "year": 2017,
          "title": "Olanzapine for chemotherapy-induced nausea and vomiting: systematic review and meta-analysis [online appendix]",
          "type": "article",
          "venue": "Pharmacy Practice",
          "cited_by_count": 0,
          "topics": [
            "Nausea and vomiting management",
            "Anesthesia and Sedative Agents",
            "Pathogenesis and Treatment of Hiccups"
          ]
        },
        {
          "openalex_id": "W2943277367",
          "year": 2019,
          "title": "Diseases, Injuries, and Risk Factors in Child and Adolescent Health, 1990 to 2017",
          "type": "article",
          "venue": "Archives of Pediatrics and Adolescent Medicine",
          "cited_by_count": 267,
          "topics": [
            "Child and Adolescent Health",
            "Injury Epidemiology and Prevention",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W4321607915",
          "year": 2023,
          "title": "Clinical and economic burden of healthcare-associated infections: A prospective cohort study",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 160,
          "topics": [
            "Nosocomial Infections in ICU",
            "Infection Control in Healthcare",
            "Surgical site infection prevention"
          ]
        },
        {
          "openalex_id": "W2998952322",
          "year": 2020,
          "title": "Drug related problems in admitted geriatric patients: the impact of clinical pharmacist interventions",
          "type": "article",
          "venue": "BMC Geriatrics",
          "cited_by_count": 120,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Pharmacovigilance and Adverse Drug Reactions",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2900970314",
          "year": 2018,
          "title": "Treatment outcome and associated factors among patients with epilepsy",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 73,
          "topics": [
            "Epilepsy research and treatment",
            "Pharmacological Effects and Toxicity Studies",
            "Hemoglobinopathies and Related Disorders"
          ]
        },
        {
          "openalex_id": "W2942174024",
          "year": 2019,
          "title": "Medication Belief and Adherence among Patients with Epilepsy",
          "type": "article",
          "venue": "Behavioural Neurology",
          "cited_by_count": 69,
          "topics": [
            "Epilepsy research and treatment",
            "Medication Adherence and Compliance",
            "Pharmacological Effects and Toxicity Studies"
          ]
        },
        {
          "openalex_id": "W2953649359",
          "year": 2019,
          "title": "Practice and predictors of self-care behaviors among ambulatory patients with hypertension in Ethiopia",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 64,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Medication Adherence and Compliance",
            "Sodium Intake and Health"
          ]
        },
        {
          "openalex_id": "W3006921218",
          "year": 2020,
          "title": "Healthcare professionals knowledge, attitude and practice of adverse drug reactions reporting in Ethiopia: a cross-sectional study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 49,
          "topics": [
            "Pharmacovigilance and Adverse Drug Reactions",
            "Patient Safety and Medication Errors",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        }
      ]
    }
  },
  {
    "name": "Kim Dalziel",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "111-RA",
        "title": "Developing and testing a version of EQ-5D-Y for use in children aged 2-5 years using a mixed methods approach",
        "working_group": "Youth"
      },
      {
        "project_id": "2017-RA",
        "title": "QUALITATIVE EXPLORATION OF THE NEED FOR A STRENGTHS-BASED FOCUS WITHIN THE EQ-5D-Y-5L: UNDERSTANDING MARKET THREATS AND POSITIONING",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "330-PHD",
        "title": "Evaluation of the EQ-5D-Y as a child PROM in tertiary hospitals for high impact childhood conditions",
        "working_group": "Youth"
      },
      {
        "project_id": "361-RA",
        "title": "Multi instrument comparison study extension: focus on EuroQol instruments, psychometric protocols, psychometric analysis and view to international replication",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5078953009",
      "display_name": "Kim Dalziel",
      "orcid": "0000-0003-4972-8871",
      "reported_affiliation": "The University of Melbourne",
      "works_count": 237,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 68
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 37
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 28
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 16
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
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 13
        },
        {
          "topic": "Congenital Heart Disease Studies",
          "works": 11
        },
        {
          "topic": "Food Allergy and Anaphylaxis Research",
          "works": 11
        },
        {
          "topic": "Global Health Care Issues",
          "works": 10
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 10
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 9
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nancy Devlin",
          "works": 45
        },
        {
          "name": "Harriet Hiscock",
          "works": 43
        },
        {
          "name": "Li Huang",
          "works": 40
        },
        {
          "name": "Leonie Segal",
          "works": 29
        },
        {
          "name": "Philip Clarke",
          "works": 23
        },
        {
          "name": "Renee Jones",
          "works": 21
        },
        {
          "name": "Brendan Mulhern",
          "works": 19
        },
        {
          "name": "Franz E Babl",
          "works": 18
        },
        {
          "name": "Michelle Tew",
          "works": 16
        },
        {
          "name": "Cate Bailey",
          "works": 14
        },
        {
          "name": "Gang Chen",
          "works": 13
        },
        {
          "name": "Rachel O’Loughlin",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7118349013",
          "year": 2026,
          "title": "Avoiding routine gastric residual volume measurement in neonatal critical care (the neoGASTRIC trial): study protocol for a multi-centre, unblinded, randomised, controlled trial",
          "type": "article",
          "venue": "Trials",
          "cited_by_count": 4,
          "topics": [
            "Infant Nutrition and Health",
            "Infant Development and Preterm Care",
            "Clinical Nutrition and Gastroenterology"
          ]
        },
        {
          "openalex_id": "W7140307574",
          "year": 2026,
          "title": "Comparative performance of common paediatric patient-reported outcome measures (P-PROMs) across health conditions",
          "type": "article",
          "venue": "Archives of Disease in Childhood",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W7139963877",
          "year": 2026,
          "title": "Cost-Effectiveness of Oral Immunotherapy Treatments vs No Treatment for Peanut Allergy in Children",
          "type": "article",
          "venue": "JAMA Network Open",
          "cited_by_count": 0,
          "topics": [
            "Food Allergy and Anaphylaxis Research",
            "Allergic Rhinitis and Sensitization",
            "Pediatric health and respiratory diseases"
          ]
        },
        {
          "openalex_id": "W7138071919",
          "year": 2026,
          "title": "Health Economic Evaluations Alongside Adaptive Platform Trials: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W7135178833",
          "year": 2026,
          "title": "Qualitative insights from patient/caregivers, and clinicians on routine use of the EQ-5D-Y-5L in clinical paediatric care—results from a pilot feasibility and acceptability trial",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W7155508205",
          "year": 2026,
          "title": "Trends in out-of-hospital healthcare use and costs in adolescents with complex conditions transitioning from pediatric care",
          "type": "article",
          "venue": "Pediatric Research",
          "cited_by_count": 0,
          "topics": [
            "Adolescent and Pediatric Healthcare",
            "Healthcare Policy and Management",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W2401205380",
          "year": 2002,
          "title": "Screening for hepatitis C among injecting drug users and in genitourinary medicine (GUM) clinics: systematic reviews of effectiveness, modelling study and national survey of current practice",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 103,
          "topics": [
            "Hepatitis C virus research",
            "Hepatitis B Virus Studies",
            "Hepatitis Viruses Studies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2315329255",
          "year": 2002,
          "title": "The effectiveness and cost-effectiveness of imatinib in chronic myeloid leukaemia: a systematic review",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 42,
          "topics": [
            "Chronic Myeloid Leukemia Treatments"
          ]
        },
        {
          "openalex_id": "W2049105581",
          "year": 2003,
          "title": "Development of an evidence‐based guideline for imaging in cervical spine trauma",
          "type": "article",
          "venue": "Australasian Radiology",
          "cited_by_count": 9,
          "topics": [
            "Spinal Fractures and Fixation Techniques",
            "Pelvic and Acetabular Injuries",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W2159291632",
          "year": 2003,
          "title": "Screening for hepatitis C in genito-urinary medicine clinics: a cost utility analysis",
          "type": "article",
          "venue": "Journal of Hepatology",
          "cited_by_count": 23,
          "topics": [
            "Hepatitis C virus research",
            "Hepatitis B Virus Studies",
            "HIV, Drug Use, Sexual Risk"
          ]
        },
        {
          "openalex_id": "W2466586463",
          "year": 2016,
          "title": "Nasal High-Flow Therapy for Primary Respiratory Support in Preterm Infants",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 219,
          "topics": [
            "Neonatal Respiratory Health Research",
            "Respiratory Support and Mechanisms",
            "Tracheal and airway disorders"
          ]
        },
        {
          "openalex_id": "W2386738609",
          "year": 2016,
          "title": "The Fontan epidemic: Population projections from the Australia and New Zealand Fontan Registry",
          "type": "article",
          "venue": "International Journal of Cardiology",
          "cited_by_count": 187,
          "topics": [
            "Congenital Heart Disease Studies",
            "Cardiovascular Issues in Pregnancy",
            "Transplantation: Methods and Outcomes"
          ]
        },
        {
          "openalex_id": "W2006906070",
          "year": 2006,
          "title": "Endoscopic Sinus Surgery for the Excision of Nasal Polyps: A Systematic Review of Safety and Effectiveness",
          "type": "review",
          "venue": "American Journal of Rhinology",
          "cited_by_count": 160,
          "topics": [
            "Sinusitis and nasal conditions",
            "Head and Neck Surgical Oncology",
            "Nasal Surgery and Airway Studies"
          ]
        },
        {
          "openalex_id": "W2038426359",
          "year": 2003,
          "title": "Systematic review of endoscopic sinus surgery for nasal polyps",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 149,
          "topics": [
            "Sinusitis and nasal conditions",
            "Nasal Surgery and Airway Studies",
            "Head and Neck Surgical Oncology"
          ]
        },
        {
          "openalex_id": "W1992254924",
          "year": 2004,
          "title": "Effectiveness and cost-effectiveness of imatinib for first-line treatment of chronic myeloid leukaemia in chronic phase: a systematic review and economic analysis",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 127,
          "topics": [
            "Chronic Myeloid Leukemia Treatments",
            "Acute Myeloid Leukemia Research",
            "Myeloproliferative Neoplasms: Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2800239415",
          "year": 2018,
          "title": "A population‐based cost‐effectiveness study of early genetic testing in severe epilepsies of infancy",
          "type": "article",
          "venue": "Epilepsia",
          "cited_by_count": 117,
          "topics": [
            "Epilepsy research and treatment",
            "Genomics and Rare Diseases",
            "Neonatal and fetal brain pathology"
          ]
        },
        {
          "openalex_id": "W1926783858",
          "year": 2012,
          "title": "Theory! The Missing Link in Understanding the Performance of Neonate/Infant Home‐Visiting Programs to Prevent Child Maltreatment: A Systematic Review",
          "type": "review",
          "venue": "Milbank Quarterly",
          "cited_by_count": 98,
          "topics": [
            "Child Abuse and Trauma",
            "Child Welfare and Adoption",
            "Homicide, Infanticide, and Child Abuse"
          ]
        }
      ]
    }
  },
  {
    "name": "Kim Rand",
    "member_affiliation": "Maths in Health and the Health Services Research Centre, Akershus University Hospital",
    "is_member": true,
    "projects": [
      {
        "project_id": "1507-VS",
        "title": "Completion of the Covid-stranded Norwegian EQ-5D-5L valuation study",
        "working_group": "Valuation"
      },
      {
        "project_id": "1854-EO",
        "title": "Travel support for the SEVQoL PhD student to the Priorities 2024 conference",
        "working_group": "Descriptive Systems, Valuation, Populations and Health Systems"
      },
      {
        "project_id": "2014070",
        "title": "EQVT iteration experiment",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015070",
        "title": "Comparing the predictive accuracy of different main-effects regression models on left-out EQ-5D-5L health states: 20-parameter additive model vs. 8, 9, and 11 parameter multiplicative models.",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015250",
        "title": "Intercept investigation: Does the value drop from full health to any EQ-5D problems reflect preferences, or is it an artefact of the valuation method?",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015260",
        "title": "Hybrid model in R",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015270",
        "title": "HRQoL among patients seeking treatment for abuse of illicit substances",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190580",
        "title": "Severity and EQ-5D (SEVQ). How can EQ5D-utilitites capture notions of severity for priority setting in health care.",
        "working_group": "Valuation"
      },
      {
        "project_id": "20191190",
        "title": "HRQoL and Health Literacy among informal caregivers to persons with dementia",
        "working_group": "Others"
      },
      {
        "project_id": "209-RA",
        "title": "Building in latent class support to xreg R package – simplifying access to linear and non-linear, latent class, random effects, censored/interval, and hybrid regression methods",
        "working_group": "Valuation"
      },
      {
        "project_id": "2471-RA",
        "title": "Developing and validating a copula-based method to transport aggregated EQ-5D utility values between value sets",
        "working_group": "Valuation"
      },
      {
        "project_id": "2540-EO",
        "title": "Panel debate on QALY-based HTA and the EQ-5D at the Society for Medical Decision Making 48th Annual Meeting in Oslo",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2626-RA",
        "title": "AI Preferences for Health? Characterizing LLM Responses to DCE-Based Valuation Tasks and Evaluating Strategies for Detecting Automated Survey Respondents",
        "working_group": "Valuation"
      },
      {
        "project_id": "309-RA",
        "title": "Illustrating the empirical impact of applying different value sets: easy-to-read graphs and tables for stakeholders",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5041551368",
      "display_name": "Kim Rand",
      "orcid": "0000-0001-7692-4099",
      "reported_affiliation": "Akershus University Hospital",
      "works_count": 66,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 34
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 18
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 10
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 3
        },
        {
          "topic": "Social and Cultural Dynamics",
          "works": 3
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 3
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 3
        },
        {
          "topic": "Global Health Care Issues",
          "works": 3
        },
        {
          "topic": "Social and Educational Sciences",
          "works": 3
        },
        {
          "topic": "Simulation Techniques and Applications",
          "works": 3
        },
        {
          "topic": "Complex Systems and Decision Making",
          "works": 3
        },
        {
          "topic": "Business Process Modeling and Analysis",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Liv Ariane Augestad",
          "works": 12
        },
        {
          "name": "Nan Luo",
          "works": 11
        },
        {
          "name": "Knut Stavem",
          "works": 10
        },
        {
          "name": "Fredrik A. Dahl",
          "works": 10
        },
        {
          "name": "Mathias Barra",
          "works": 8
        },
        {
          "name": "Juan Manuel Ramos-Goñi",
          "works": 7
        },
        {
          "name": "Joe Viana",
          "works": 7
        },
        {
          "name": "Ivar Sønbø Kristiansen",
          "works": 6
        },
        {
          "name": "Hilde Eileen Nafstad",
          "works": 5
        },
        {
          "name": "Rolv Mikkel Blakar",
          "works": 5
        },
        {
          "name": "Hanne H. Brorson",
          "works": 4
        },
        {
          "name": "Zhihao Yang",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7134953055",
          "year": 2026,
          "title": "Valuation of EQ-5D-5L With 2 Bolt-On Items: Further Evaluation of the Scaling Factor Model",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W7131776276",
          "year": 2026,
          "title": "What do HTA agencies need for generating health-related quality of life evidence? Findings from a global survey",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, psychology, and well-being",
            "Public Health Policies and Education"
          ]
        },
        {
          "openalex_id": "W7159612649",
          "year": 2026,
          "title": "xreg2: Flexible Maximum Likelihood Regression with Gradient-Based Optimisation",
          "type": "dataset",
          "venue": "",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4413827585",
          "year": 2025,
          "title": "Developing an EQ-5D-5L Value Set for Singapore",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 15,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W7117457750",
          "year": 2025,
          "title": "Letter to the Editor Regarding “Dupilumab Versus Lebrikizumab Demonstrates Greater Likelihood of Achieving and Maintaining Improvements in Efficacy Outcomes Using a Placebo Adjusted Indirect Treatment Comparison”",
          "type": "letter",
          "venue": "Dermatology and Therapy",
          "cited_by_count": 2,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Psoriasis: Treatment and Pathogenesis",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W7155154592",
          "year": 2025,
          "title": "Mental health INtervention with Digital APPlications (MIND-APP): Protocol for a Randomized Controlled Researcher Blinded Trial Evaluating the Effectiveness of the Tankevirus and Grubl Mental Health Apps Compared to a Placebo App (Preprint)",
          "type": "article",
          "venue": "JMIR Research Protocols",
          "cited_by_count": 0,
          "topics": [
            "Digital Mental Health Interventions",
            "Mobile Health and mHealth Applications",
            "Social Media in Health Education"
          ]
        },
        {
          "openalex_id": "W2108046163",
          "year": 2007,
          "title": "Ideology and power: the influence of current neo‐liberalism in society",
          "type": "article",
          "venue": "Journal of Community & Applied Social Psychology",
          "cited_by_count": 101,
          "topics": [
            "Social and Cultural Dynamics",
            "Social Media and Politics",
            "Populism, Right-Wing Movements"
          ]
        },
        {
          "openalex_id": "W2464947075",
          "year": 2008,
          "title": "Ideological changes measured through changes in language : development, description and preliminary validation of a new archival method",
          "type": "dissertation",
          "venue": "Duo Research Archive (University of Oslo)",
          "cited_by_count": 8,
          "topics": [
            "Interpreting and Communication in Healthcare",
            "Discourse Analysis in Language Studies",
            "Social and Educational Sciences"
          ]
        },
        {
          "openalex_id": "W2035866490",
          "year": 2009,
          "title": "Globalization, Neo‐Liberalism and Community Psychology",
          "type": "article",
          "venue": "American Journal of Community Psychology",
          "cited_by_count": 55,
          "topics": [
            "Community Health and Development",
            "Social Representations and Identity",
            "Language, Discourse, Communication Strategies"
          ]
        },
        {
          "openalex_id": "W2083814201",
          "year": 2009,
          "title": "Globalization, ideologies and well-being: a study of a West African and a North European society",
          "type": "article",
          "venue": "The Journal of Positive Psychology",
          "cited_by_count": 14,
          "topics": [
            "Social and Cultural Dynamics",
            "Cultural Differences and Values",
            "Social and Intergroup Psychology"
          ]
        },
        {
          "openalex_id": "W2587471491",
          "year": 2017,
          "title": "Estimating an EQ-5D-5L Value Set for China",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 737,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2009786630",
          "year": 2013,
          "title": "Drop-out from addiction treatment: A systematic review of risk factors",
          "type": "review",
          "venue": "Clinical Psychology Review",
          "cited_by_count": 658,
          "topics": [
            "Mental Health Research Topics",
            "Schizophrenia research and treatment",
            "Treatment of Major Depression"
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
          "openalex_id": "W2903723251",
          "year": 2018,
          "title": "EQ-5D-5L Valuation for the Malaysian Population",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 91,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W1985215603",
          "year": 2011,
          "title": "Comparison of hypothetical and experienced EQ-5D valuations: relative weights of the five dimensions",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 44,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2613980321",
          "year": 2017,
          "title": "Less Is More: Cross-Validation Testing of Simplified Nonlinear Regression Model Specifications for EQ-5D-5L Health State Values",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 36,
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
