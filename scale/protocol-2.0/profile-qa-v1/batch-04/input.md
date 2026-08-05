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
    "name": "Andrea L. Monteiro",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "161-RA",
        "title": "PhD dissertation funding request for a novel valuation method: Feasibility and application of the single profile preference elicitation (SPP) method to value bolt-on items. (Revised application)",
        "working_group": "Descriptive Systems, Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5024494805",
      "display_name": "A Monteiro",
      "orcid": "0000-0001-9763-3485",
      "reported_affiliation": "Clinton College",
      "works_count": 52,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 19
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 11
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 4
        },
        {
          "topic": "Cardiac pacing and defibrillation studies",
          "works": 4
        },
        {
          "topic": "Cardiac Arrhythmias and Treatments",
          "works": 4
        },
        {
          "topic": "Acute Myocardial Infarction Research",
          "works": 4
        },
        {
          "topic": "Health Education and Validation",
          "works": 3
        },
        {
          "topic": "Coronary Interventions and Diagnostics",
          "works": 3
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 3
        },
        {
          "topic": "Innovations in Medical Education",
          "works": 3
        },
        {
          "topic": "Heart Rate Variability and Autonomic Control",
          "works": 3
        },
        {
          "topic": "Non-Invasive Vital Sign Monitoring",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "A. Simon Pickard",
          "works": 15
        },
        {
          "name": "Maja Kuharić",
          "works": 10
        },
        {
          "name": "Marisa Santos",
          "works": 10
        },
        {
          "name": "R Dourado",
          "works": 10
        },
        {
          "name": "Fabiana Duarte",
          "works": 9
        },
        {
          "name": "Luís Oliveira",
          "works": 9
        },
        {
          "name": "D Martins",
          "works": 9
        },
        {
          "name": "A Fontes",
          "works": 8
        },
        {
          "name": "C Machado",
          "works": 8
        },
        {
          "name": "E Santos",
          "works": 8
        },
        {
          "name": "Nuno Pelicano",
          "works": 8
        },
        {
          "name": "A Tavares",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4416021299",
          "year": 2025,
          "title": "Assessing the Impact of a Social Program Using EQ-HWB-9 and EQ-5D-5L: The Dara Project",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W4412443035",
          "year": 2025,
          "title": "HTA44 Reimbursement Outcomes for EMA Conditionally Authorized Orphan Drugs (2022-2023): Implications for Joint Clinical Assessment Requirements",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W4405748797",
          "year": 2024,
          "title": "CO109 Evaluating the Psychometric Properties of the Brazilian Portuguese EQ Health and Well-Being Short Form (EQ-HWB-S)",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health and Wellbeing Research",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4391542822",
          "year": 2024,
          "title": "Care recipient self-perceived burden: Perspectives of individuals with chronic health conditions or personal experiences with caregiving on caregiver burden in the US",
          "type": "article",
          "venue": "SSM - Qualitative Research in Health",
          "cited_by_count": 10,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Palliative Care and End-of-Life Issues",
            "Family and Patient Care in Intensive Care Units"
          ]
        },
        {
          "openalex_id": "W4403503984",
          "year": 2024,
          "title": "Comparing the measurement properties of the EQ-5D-5 L, SF-6Dv2, QLU-C10D and FACT-8D among survivors of classical Hodgkin’s lymphoma",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 7,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Lymphoma Diagnosis and Treatment",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4399322759",
          "year": 2024,
          "title": "The role of shared decision-making in cancer pain management: Insights from a systematic review.",
          "type": "conference-abstract",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 0,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Patient-Provider Communication in Healthcare",
            "Ethics in medical practice"
          ]
        },
        {
          "openalex_id": "W2434424988",
          "year": 1970,
          "title": "[Our experience with Ketalar in neuro-radiology].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Anatomy and Medical Technology",
            "Trigeminal Neuralgia and Treatments",
            "History of Medical Practice"
          ]
        },
        {
          "openalex_id": "W4406720447",
          "year": 2004,
          "title": "METODOLOGIA DE GESTÃO DE CUSTO DO AÇO LÍQUIDO E TARUGO NA BELGO – USINA DE MONLEVADE",
          "type": "conference-paper",
          "venue": "ABM Proceedings",
          "cited_by_count": 0,
          "topics": [
            "Business and Management Studies"
          ]
        },
        {
          "openalex_id": "W4384853529",
          "year": 2007,
          "title": "Heart Rate Variability Analysis in Revascularized Individuals Submitted to an Anaerobic Potency Test",
          "type": "article",
          "venue": "DOAJ (DOAJ: Directory of Open Access Journals)",
          "cited_by_count": 1,
          "topics": [
            "Heart Rate Variability and Autonomic Control",
            "Non-Invasive Vital Sign Monitoring",
            "Cardiovascular and exercise physiology"
          ]
        },
        {
          "openalex_id": "W2219998342",
          "year": 2007,
          "title": "Heart rate variability analysis in revascularized individuals submitted to an anaerobic potency test.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Heart Rate Variability and Autonomic Control",
            "Non-Invasive Vital Sign Monitoring",
            "Cardiovascular and exercise physiology"
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
          "openalex_id": "W2173668850",
          "year": 2015,
          "title": "Brazilian Valuation of EQ-5D-3L Health States",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 139,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4205569690",
          "year": 2022,
          "title": "Developing a New Generic Health and Wellbeing Measure: Psychometric Survey Results for the EQ-HWB",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 81,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Health Education and Validation",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W3166961211",
          "year": 2021,
          "title": "EQ-5D Brazilian population norms",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W4214702737",
          "year": 2022,
          "title": "Generation, Selection, and Face Validation of Items for a New Generic Measure of Quality of Life: The EQ-HWB",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 38,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4220657799",
          "year": 2022,
          "title": "A Comparison of a Preliminary Version of the EQ-HWB Short and the 5-Level Version EQ-5D",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 31,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2905645650",
          "year": 2018,
          "title": "Patients&amp;rsquo; preferences for coronary revascularization: a systematic review",
          "type": "review",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 17,
          "topics": [
            "Coronary Interventions and Diagnostics",
            "Economic and Environmental Valuation",
            "Pain Management and Treatment"
          ]
        },
        {
          "openalex_id": "W2612363317",
          "year": 2017,
          "title": "Further evidence on EQ-5D-5L preference inversion: a Brazil/U.S. collaboration",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 14,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        }
      ]
    }
  },
  {
    "name": "Andrew Lenny",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "239-RA",
        "title": "A review of the methodologies implemented in the valuation of generic and condition-specific measures of child and adolescent health states",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5029564514",
      "display_name": "Andrew Lenny",
      "orcid": "0000-0002-9325-0062",
      "reported_affiliation": "People's History Museum",
      "works_count": 10,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 5
        },
        {
          "topic": "Lysosomal Storage Disorders Research",
          "works": 4
        },
        {
          "topic": "Statistical Methods in Clinical Trials",
          "works": 2
        },
        {
          "topic": "Parkinson's Disease Mechanisms and Treatments",
          "works": 2
        },
        {
          "topic": "Trypanosoma species research and implications",
          "works": 1
        },
        {
          "topic": "Hereditary Neurological Disorders",
          "works": 1
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 1
        },
        {
          "topic": "Social Policies and Family",
          "works": 1
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 1
        },
        {
          "topic": "Global Health Care Issues",
          "works": 1
        },
        {
          "topic": "Human-Animal Interaction Studies",
          "works": 1
        },
        {
          "topic": "Ethics and Legal Issues in Pediatric Healthcare",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Louise Longworth",
          "works": 9
        },
        {
          "name": "Koonal Shah",
          "works": 7
        },
        {
          "name": "Derralynn Hughes",
          "works": 5
        },
        {
          "name": "Giovanna Devercelli",
          "works": 3
        },
        {
          "name": "Olulade Ayodele",
          "works": 3
        },
        {
          "name": "Deborah Elstein",
          "works": 2
        },
        {
          "name": "Donna Fountain",
          "works": 2
        },
        {
          "name": "Rachael Miller",
          "works": 2
        },
        {
          "name": "Rohini Sen",
          "works": 2
        },
        {
          "name": "Bryan Bennett",
          "works": 2
        },
        {
          "name": "John Brazier",
          "works": 2
        },
        {
          "name": "Mark Oppe",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4362737154",
          "year": 2023,
          "title": "Estimation of Health State Utility Values in Fabry Disease Using Vignette Development and Valuation",
          "type": "book-chapter",
          "venue": "Journal of health economics and outcomes research",
          "cited_by_count": 3,
          "topics": [
            "Lysosomal Storage Disorders Research",
            "Parkinson's Disease Mechanisms and Treatments",
            "Social Policies and Family"
          ]
        },
        {
          "openalex_id": "W4363673082",
          "year": 2023,
          "title": "Estimation of Health State Utility Values in Fabry Disease Using Vignette Development and Valuation",
          "type": "article",
          "venue": "Journal of health economics and outcomes research",
          "cited_by_count": 1,
          "topics": [
            "Lysosomal Storage Disorders Research",
            "Parkinson's Disease Mechanisms and Treatments"
          ]
        },
        {
          "openalex_id": "W4205236753",
          "year": 2022,
          "title": "Development and validation of Gaucher disease type 1 (GD1)-specific patient-reported outcome measures (PROMs) for clinical monitoring and for clinical trials",
          "type": "article",
          "venue": "Orphanet Journal of Rare Diseases",
          "cited_by_count": 34,
          "topics": [
            "Lysosomal Storage Disorders Research",
            "Trypanosoma species research and implications",
            "Hereditary Neurological Disorders"
          ]
        },
        {
          "openalex_id": "W4210593812",
          "year": 2022,
          "title": "Estimation of health state utility values in Fabry disease using vignette construction and valuation",
          "type": "article",
          "venue": "Molecular Genetics and Metabolism",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3169554342",
          "year": 2021,
          "title": "Adapting preference-based utility measures to capture the impact of cancer treatment-related symptoms",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 8,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Statistical Methods in Clinical Trials",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W3126531089",
          "year": 2021,
          "title": "Psychometric validation of the Gaucher Disease Questionnaire (GDQ) to assess quality of life in patients with Gaucher disease",
          "type": "article",
          "venue": "Molecular Genetics and Metabolism",
          "cited_by_count": 0,
          "topics": [
            "Lysosomal Storage Disorders Research",
            "Autism Spectrum Disorder Research"
          ]
        },
        {
          "openalex_id": "W2994840957",
          "year": 2019,
          "title": "PNS203 USE OF DISCRETE CHOICE EXPERIMENTS TO INFORM HTA DECISION MAKING.",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W3113324866",
          "year": 2020,
          "title": "PCN48 Adapting Preference-Based Utility Measures to Capture the Impact of Cancer Treatment-Related Symptoms",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Statistical Methods in Clinical Trials",
            "Cancer Treatment and Pharmacology"
          ]
        },
        {
          "openalex_id": "W3112447031",
          "year": 2020,
          "title": "PIH21 A Targeted Review of Studies on Canine Animal Assisted Therapy in Paediatric Oncology Patients",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Human-Animal Interaction Studies",
            "Ethics and Legal Issues in Pediatric Healthcare",
            "Pediatric Pain Management Techniques"
          ]
        },
        {
          "openalex_id": "W3111097994",
          "year": 2020,
          "title": "PNS208 A Review of the Methods Used in Valuation Studies of Child/Adolescent Health-Related Quality of Life Using EQ-5D-Y and CHU-9D",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        }
      ]
    }
  },
  {
    "name": "Andrew Lloyd",
    "member_affiliation": "Acaster Lloyd",
    "is_member": true,
    "projects": [
      {
        "project_id": "1475-RA",
        "title": "Exploring the content validity of the EQ-PSO bolt-ons in chronic skin conditions other than psoriasis",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1806-RA",
        "title": "Exploring the construct validity of the EQ-HWB and EQ-HWB-S as a measure of spillover among carers and wider family members",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "20190510",
        "title": "Design and Analysis Considerations when using the EQ-5D alongside clinical trials or observational studies for economic evaluation: PhD studentship and development of tools for analysts and researchers",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5031114648",
      "display_name": "Andrew Lloyd",
      "orcid": "0000-0002-7597-6556",
      "reported_affiliation": "Lloyd's",
      "works_count": 235,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 79
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 20
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 16
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 12
        },
        {
          "topic": "Global Health Care Issues",
          "works": 11
        },
        {
          "topic": "Multiple Sclerosis Research Studies",
          "works": 9
        },
        {
          "topic": "Neurogenetic and Muscular Disorders Research",
          "works": 8
        },
        {
          "topic": "Liver Disease Diagnosis and Treatment",
          "works": 8
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 7
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 7
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 7
        },
        {
          "topic": "Prostate Cancer Treatment and Research",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Beenish Nafees",
          "works": 18
        },
        {
          "name": "Katy Gallop",
          "works": 15
        },
        {
          "name": "Sarah Dewilde",
          "works": 12
        },
        {
          "name": "John Brazier",
          "works": 12
        },
        {
          "name": "Paul Swinburn",
          "works": 12
        },
        {
          "name": "Daniel Aggio",
          "works": 12
        },
        {
          "name": "Siu Hing Lo",
          "works": 11
        },
        {
          "name": "Cicely Kerr",
          "works": 11
        },
        {
          "name": "Karissa Johnston",
          "works": 10
        },
        {
          "name": "Andrew Briggs",
          "works": 9
        },
        {
          "name": "S.L. Shingler",
          "works": 8
        },
        {
          "name": "Michael Herdman",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164860903",
          "year": 2026,
          "title": "Preference-based scoring algorithm to estimate societal utilities based on the patient-reported experience of cognitive impairment in schizophrenia (PRECIS) instrument",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Schizophrenia research and treatment",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4407741846",
          "year": 2025,
          "title": "A Vignette Study to Derive Health-Related Quality-of-Life Weights for Individuals with Steroid Refractory Chronic Graft-versus-Host Disease Receiving Third-Line Therapy in the United Kingdom",
          "type": "article",
          "venue": "Journal of health economics and outcomes research",
          "cited_by_count": 0,
          "topics": [
            "Hematopoietic Stem Cell Transplantation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Acute Lymphoblastic Leukemia research"
          ]
        },
        {
          "openalex_id": "W4417479837",
          "year": 2025,
          "title": "CO131 Health-Related Quality of Life (HRQoL) in Duchenne Muscular Dystrophy (DMD): Insights From the DMD-QoL Instrument in the United States (US)",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Muscle Physiology and Disorders",
            "Nutrition and Health in Aging",
            "Prosthetics and Rehabilitation Robotics"
          ]
        },
        {
          "openalex_id": "W4406767414",
          "year": 2025,
          "title": "Estimating health state utilities for aromatic L-amino acid decarboxylase deficiency (AADCd) in the United States",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Metabolism and Genetic Disorders",
            "Genetic Neurodegenerative Diseases",
            "Autoimmune Neurological Disorders and Treatments"
          ]
        },
        {
          "openalex_id": "W4416291388",
          "year": 2025,
          "title": "Estimation of Health Utility Values for Eosinophilic Granulomatosis With Polyangiitis",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 0,
          "topics": [
            "Vasculitis and related conditions",
            "Eosinophilic Esophagitis",
            "Eosinophilic Disorders and Syndromes"
          ]
        },
        {
          "openalex_id": "W4414963885",
          "year": 2025,
          "title": "P174 Patient-reported outcomes measuring an individuals overall self-rated health after long-term treatment with bulevirtide 2 mg for chronic hepatitis delta in the phase 3 MYR301 trial",
          "type": "conference-abstract",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis C virus research",
            "Liver Disease Diagnosis and Treatment",
            "Hepatitis B Virus Studies"
          ]
        },
        {
          "openalex_id": "W2037615010",
          "year": 1999,
          "title": "Comprehension of Prosody in Parkinson's Disease",
          "type": "article",
          "venue": "Cortex",
          "cited_by_count": 57,
          "topics": [
            "Language Development and Disorders",
            "Voice and Speech Disorders",
            "Neurobiology of Language and Bilingualism"
          ]
        },
        {
          "openalex_id": "W2413217770",
          "year": 1999,
          "title": "Correspondence",
          "type": "letter",
          "venue": "European Journal of Vascular and Endovascular Surgery",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W1978332098",
          "year": 1999,
          "title": "Impact of spontaneous embolization on cognitive function",
          "type": "article",
          "venue": "British journal of surgery",
          "cited_by_count": 7,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Intracerebral and Subarachnoid Hemorrhage Research",
            "Intracranial Aneurysms: Treatment and Complications"
          ]
        },
        {
          "openalex_id": "W2130976421",
          "year": 1999,
          "title": "Prevalence of true vein graft aneurysms: Implications for aneurysm pathogenesis",
          "type": "article",
          "venue": "Journal of Vascular Surgery",
          "cited_by_count": 53,
          "topics": [
            "Vascular Procedures and Complications",
            "Peripheral Artery Disease Management",
            "Infectious Aortic and Vascular Conditions"
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
          "openalex_id": "W2121619367",
          "year": 2011,
          "title": "Conjoint Analysis Applications in Health—a Checklist: A Report of the ISPOR Good Research Practices for Conjoint Analysis Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2056,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Statistical Methods and Bayesian Inference"
          ]
        },
        {
          "openalex_id": "W2020677481",
          "year": 2006,
          "title": "Health state utilities for metastatic breast cancer",
          "type": "article",
          "venue": "British Journal of Cancer",
          "cited_by_count": 365,
          "topics": [
            "Cancer Treatment and Pharmacology",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2296800272",
          "year": 2016,
          "title": "Health state utilities in non–small cell lung cancer: An international study",
          "type": "article",
          "venue": "Asia-Pacific Journal of Clinical Oncology",
          "cited_by_count": 309,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Neutropenia and Cancer Infections"
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
          "openalex_id": "W2918342502",
          "year": 2019,
          "title": "Identification, Review, and Use of Health State Utilities in Cost-Effectiveness Models: An ISPOR Good Practices for Outcomes Research Task Force Report",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 168,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2527943338",
          "year": 2016,
          "title": "Estimating Health-State Utility for Economic Models in Clinical Studies: An ISPOR Good Research Practices Task Force Report",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 161,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        }
      ]
    }
  },
  {
    "name": "Ann Charlotte Egmar",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2013060",
        "title": "Testing feasibility, reliability and validity of the health-related quality of life instrument EQ-5D-Y in children and adolescents with asthma- a cross-sectional pilot study",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5037683865",
      "display_name": "Ann‐Charlotte Egmar",
      "orcid": "0000-0003-2504-343X",
      "reported_affiliation": "Röda Korsets Högskola",
      "works_count": 32,
      "top_topics": [
        {
          "topic": "Allergic Rhinitis and Sensitization",
          "works": 9
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 8
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 7
        },
        {
          "topic": "Human-Animal Interaction Studies",
          "works": 5
        },
        {
          "topic": "Food Allergy and Anaphylaxis Research",
          "works": 4
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 4
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 3
        },
        {
          "topic": "Pediatric health and respiratory diseases",
          "works": 3
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 2
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 2
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 2
        },
        {
          "topic": "Adolescent and Pediatric Healthcare",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kristina Burström",
          "works": 11
        },
        {
          "name": "Magnus Wickman",
          "works": 10
        },
        {
          "name": "Wolfgang Greiner",
          "works": 6
        },
        {
          "name": "Narcís Gusi",
          "works": 6
        },
        {
          "name": "Michael Herdman",
          "works": 6
        },
        {
          "name": "Catarina Almqvist",
          "works": 6
        },
        {
          "name": "Magnus Svartengren",
          "works": 6
        },
        {
          "name": "Paul Kind",
          "works": 5
        },
        {
          "name": "Marina Jonsson",
          "works": 5
        },
        {
          "name": "Inger Kull",
          "works": 5
        },
        {
          "name": "Gunnel Emenius",
          "works": 5
        },
        {
          "name": "Ann Gardulf",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W3086972873",
          "year": 2019,
          "title": "EQ-5D-Y-5L",
          "type": "dataset",
          "venue": "PsycTESTS Dataset",
          "cited_by_count": 2,
          "topics": [
            "RNA regulation and disease"
          ]
        },
        {
          "openalex_id": "W2912408218",
          "year": 2019,
          "title": "EQ-5D-Y-5L: developing a revised EQ-5D-Y with increased response categories",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 127,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W2788561295",
          "year": 2018,
          "title": "Patient-reported improvements of pain, disability, and health-related quality of life following chiropractic care for back pain – A national observational study in Sweden",
          "type": "article",
          "venue": "Journal of Bodywork and Movement Therapies",
          "cited_by_count": 15,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Fibromyalgia and Chronic Fatigue Syndrome Research"
          ]
        },
        {
          "openalex_id": "W2591926165",
          "year": 2017,
          "title": "Experiences of Daily Life Among Adolescents With Asthma – A Struggle With Ambivalence",
          "type": "article",
          "venue": "Journal of Pediatric Nursing",
          "cited_by_count": 16,
          "topics": [
            "Asthma and respiratory diseases",
            "Delphi Technique in Research",
            "Adolescent and Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W2540585829",
          "year": 2016,
          "title": "Extension Of The Labels Within The Eq-5d-Y",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Control Systems in Engineering",
            "Advanced Control Systems Optimization",
            "Advanced Numerical Analysis Techniques"
          ]
        },
        {
          "openalex_id": "W1773251129",
          "year": 2015,
          "title": "Asthma during adolescence impairs health-related quality of life",
          "type": "article",
          "venue": "The Journal of Allergy and Clinical Immunology In Practice",
          "cited_by_count": 32,
          "topics": [
            "Asthma and respiratory diseases",
            "Adolescent and Pediatric Healthcare",
            "Inhalation and Respiratory Drug Delivery"
          ]
        },
        {
          "openalex_id": "W2014018505",
          "year": 1994,
          "title": "Reduced mite allergen levels in dwellings with mechanical exhaust and supply ventilation",
          "type": "article",
          "venue": "Clinical & Experimental Allergy",
          "cited_by_count": 74,
          "topics": [
            "Allergic Rhinitis and Sensitization",
            "Insects and Parasite Interactions",
            "Indoor Air Quality and Microbial Exposure"
          ]
        },
        {
          "openalex_id": "W2059158516",
          "year": 1996,
          "title": "130 Indoor air quality in special daycare centres for atopic children",
          "type": "article",
          "venue": "Journal of Allergy and Clinical Immunology",
          "cited_by_count": 0,
          "topics": [
            "Pediatric health and respiratory diseases",
            "School Health and Nursing Education"
          ]
        },
        {
          "openalex_id": "W2099854259",
          "year": 1996,
          "title": "956 Concentrations of airborne Fel d I in special daycare centres for atopic children",
          "type": "article",
          "venue": "Journal of Allergy and Clinical Immunology",
          "cited_by_count": 8,
          "topics": [
            "Asthma and respiratory diseases",
            "Pediatric health and respiratory diseases"
          ]
        },
        {
          "openalex_id": "W2086256842",
          "year": 1998,
          "title": "Cat and dog allergen in mattresses and textile‐covered floors of homes which do or do not have pets, either in the past or currently",
          "type": "article",
          "venue": "Pediatric Allergy and Immunology",
          "cited_by_count": 32,
          "topics": [
            "Allergic Rhinitis and Sensitization",
            "Contact Dermatitis and Allergies",
            "Dermatology and Skin Diseases"
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
          "openalex_id": "W2078516818",
          "year": 1999,
          "title": "School as a risk environment for children allergic to cats and a site for transfer of cat allergen to homes",
          "type": "article",
          "venue": "Journal of Allergy and Clinical Immunology",
          "cited_by_count": 243,
          "topics": [
            "Allergic Rhinitis and Sensitization",
            "Human-Animal Interaction Studies",
            "Rabies epidemiology and control"
          ]
        },
        {
          "openalex_id": "W1984308938",
          "year": 2013,
          "title": "Development and validation of a new tool measuring nurses self-reported professional competence—The nurse professional competence (NPC) Scale",
          "type": "article",
          "venue": "Nurse Education Today",
          "cited_by_count": 165,
          "topics": [
            "Nursing education and management",
            "Innovations in Medical Education",
            "Interprofessional Education and Collaboration"
          ]
        },
        {
          "openalex_id": "W2049343501",
          "year": 2003,
          "title": "Direct and indirect exposure to pets – risk of sensitization and asthma at 4 years in a birth cohort",
          "type": "article",
          "venue": "Clinical & Experimental Allergy",
          "cited_by_count": 161,
          "topics": [
            "Allergic Rhinitis and Sensitization",
            "Human-Animal Interaction Studies",
            "Veterinary Oncology Research"
          ]
        },
        {
          "openalex_id": "W1487892095",
          "year": 2008,
          "title": "The impact of food hypersensitivity reported in 9‐year‐old children by their parents on health‐related quality of life",
          "type": "article",
          "venue": "Allergy",
          "cited_by_count": 108,
          "topics": [
            "Food Allergy and Anaphylaxis Research",
            "Eosinophilic Esophagitis",
            "Biochemical Analysis and Sensing Techniques"
          ]
        },
        {
          "openalex_id": "W1981190604",
          "year": 2003,
          "title": "Heredity, pet ownership, and confounding control in a population-based birth cohort",
          "type": "article",
          "venue": "Journal of Allergy and Clinical Immunology",
          "cited_by_count": 89,
          "topics": [
            "Human-Animal Interaction Studies",
            "Dermatology and Skin Diseases",
            "Allergic Rhinitis and Sensitization"
          ]
        }
      ]
    }
  },
  {
    "name": "Anna Krabbe-Lugner",
    "member_affiliation": "Ministry of Infrastructure and Water Management, the Netherlands",
    "is_member": true,
    "projects": [
      {
        "project_id": "2015010",
        "title": "Revisiting TTO",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5047866823",
      "display_name": "Anna K. Lugnér",
      "orcid": "",
      "reported_affiliation": "",
      "works_count": 36,
      "top_topics": [
        {
          "topic": "COVID-19 epidemiological studies",
          "works": 8
        },
        {
          "topic": "Influenza Virus Research Studies",
          "works": 7
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 5
        },
        {
          "topic": "Reproductive tract infections research",
          "works": 5
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 5
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 4
        },
        {
          "topic": "Respiratory viral infections research",
          "works": 4
        },
        {
          "topic": "Syphilis Diagnosis and Treatment",
          "works": 4
        },
        {
          "topic": "HIV, Drug Use, Sexual Risk",
          "works": 4
        },
        {
          "topic": "Vector-borne infectious diseases",
          "works": 3
        },
        {
          "topic": "Viral gastroenteritis research and epidemiology",
          "works": 3
        },
        {
          "topic": "Virology and Viral Diseases",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Anita Suijkerbuijk",
          "works": 11
        },
        {
          "name": "Jacco Wallinga",
          "works": 10
        },
        {
          "name": "Hester E. de Melker",
          "works": 7
        },
        {
          "name": "Marianne A. B. van der Sande",
          "works": 5
        },
        {
          "name": "Maarten J. Postma",
          "works": 5
        },
        {
          "name": "Birgit van Benthem",
          "works": 5
        },
        {
          "name": "G. Ardine de Wit",
          "works": 4
        },
        {
          "name": "Wilfrid van Pelt",
          "works": 4
        },
        {
          "name": "Maria Xiridou",
          "works": 4
        },
        {
          "name": "Michiel van Boven",
          "works": 4
        },
        {
          "name": "Hannelore M Götz",
          "works": 4
        },
        {
          "name": "Eelco A. B. Over",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W3036633288",
          "year": 2020,
          "title": "An overview of the time trade-off method: concept, foundation, and the evaluation of distorting factors in putting a value on health",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 94,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4300571144",
          "year": 2018,
          "title": "Consequences of restricted STI testing for young heterosexuals in the Netherlands on test costs and QALY losses.",
          "type": "article",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 0,
          "topics": [
            "LGBTQ Health, Identity, and Policy"
          ]
        },
        {
          "openalex_id": "W2771210142",
          "year": 2017,
          "title": "Consequences of restricted STI testing for young heterosexuals in the Netherlands on test costs and QALY losses",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 7,
          "topics": [
            "Reproductive tract infections research",
            "HIV/AIDS Research and Interventions",
            "HIV, Drug Use, Sexual Risk"
          ]
        },
        {
          "openalex_id": "W2616998218",
          "year": 2017,
          "title": "The cost of Lyme borreliosis",
          "type": "article",
          "venue": "European Journal of Public Health",
          "cited_by_count": 46,
          "topics": [
            "Vector-borne infectious diseases",
            "Viral Infections and Vectors",
            "Dermatological diseases and infestations"
          ]
        },
        {
          "openalex_id": "W2782576727",
          "year": 2017,
          "title": "VP35 Economic Consequences Of A Restricted Dutch Sexually Transmitted Infection-Testing Policy",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "Syphilis Diagnosis and Treatment",
            "HIV, Drug Use, Sexual Risk"
          ]
        },
        {
          "openalex_id": "W2511372377",
          "year": 2016,
          "title": "Cost-Effectiveness of Dual Antimicrobial Therapy for Gonococcal Infections Among Men Who Have Sex With Men in the Netherlands",
          "type": "article",
          "venue": "Sexually Transmitted Diseases",
          "cited_by_count": 9,
          "topics": [
            "Reproductive tract infections research",
            "Syphilis Diagnosis and Treatment",
            "HIV, Drug Use, Sexual Risk"
          ]
        },
        {
          "openalex_id": "W2799531120",
          "year": 2006,
          "title": "Costs and effects of therapeutic use of antiviral drugs during an influenza pandemic",
          "type": "book",
          "venue": "Socio-Environmental Systems Modeling",
          "cited_by_count": 0,
          "topics": [
            "Hermeneutics and Narrative Identity",
            "Aging, Elder Care, and Social Issues",
            "Health, Medicine and Society"
          ]
        },
        {
          "openalex_id": "W66573623",
          "year": 2007,
          "title": "The Impact of Model Choice on Cost-Effectiveness of Interventions Against Infectious Diseases: The Case of Pandemic Influenza",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "COVID-19 epidemiological studies",
            "Influenza Virus Research Studies"
          ]
        },
        {
          "openalex_id": "W2163737296",
          "year": 2008,
          "title": "Optimal allocation of pandemic influenza vaccine depends on age, risk and timing",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 116,
          "topics": [
            "Influenza Virus Research Studies",
            "COVID-19 epidemiological studies",
            "Vaccine Coverage and Hesitancy"
          ]
        },
        {
          "openalex_id": "W2141092194",
          "year": 2009,
          "title": "A cost-utility analysis of antenatal screening to prevent congenital rubella syndrome",
          "type": "article",
          "venue": "Epidemiology and Infection",
          "cited_by_count": 16,
          "topics": [
            "Virology and Viral Diseases",
            "Respiratory viral infections research",
            "Syphilis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2114127072",
          "year": 2015,
          "title": "The burden of Lyme borreliosis expressed in disability-adjusted life years",
          "type": "article",
          "venue": "European Journal of Public Health",
          "cited_by_count": 62,
          "topics": [
            "Vector-borne infectious diseases",
            "Parasitic Diseases Research and Treatment",
            "Zoonotic diseases and public health"
          ]
        },
        {
          "openalex_id": "W2005608328",
          "year": 2009,
          "title": "Dynamic versus static models in cost‐effectiveness analyses of anti‐viral drug therapy to mitigate an influenza pandemic",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 53,
          "topics": [
            "Influenza Virus Research Studies",
            "COVID-19 epidemiological studies",
            "SARS-CoV-2 and COVID-19 Research"
          ]
        },
        {
          "openalex_id": "W2094605944",
          "year": 2014,
          "title": "Gastrointestinal and Respiratory Illness in Children That Do and Do Not Attend Child Day Care Centers: A Cost-of-Illness Study",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 53,
          "topics": [
            "Pediatric health and respiratory diseases",
            "Respiratory viral infections research",
            "Viral gastroenteritis research and epidemiology"
          ]
        },
        {
          "openalex_id": "W1985248712",
          "year": 2010,
          "title": "A Swedish child-friendly pilot version of the EQ-5D instrument--the development process",
          "type": "article",
          "venue": "European Journal of Public Health",
          "cited_by_count": 42,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W2110062524",
          "year": 2012,
          "title": "Cost effectiveness of vaccination against pandemic influenza in European countries: mathematical modelling analysis",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 42,
          "topics": [
            "Influenza Virus Research Studies",
            "COVID-19 epidemiological studies",
            "Respiratory viral infections research"
          ]
        }
      ]
    }
  }
]
