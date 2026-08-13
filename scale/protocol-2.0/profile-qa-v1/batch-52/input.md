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
    "name": "Vincent Lau",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "299-RA",
        "title": "Validation of EQ-5D-5L in critical care (EuroQoL Working Groups Project Request for Proposal)",
        "working_group": "Descriptive Systems, Valuation, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5022213392",
      "display_name": "Vincent Lau",
      "orcid": "0000-0002-9939-7348",
      "reported_affiliation": "Alberta Health Services",
      "works_count": 73,
      "top_topics": [
        {
          "topic": "Sepsis Diagnosis and Treatment",
          "works": 18
        },
        {
          "topic": "Intensive Care Unit Cognitive Disorders",
          "works": 18
        },
        {
          "topic": "Family and Patient Care in Intensive Care Units",
          "works": 11
        },
        {
          "topic": "Nosocomial Infections in ICU",
          "works": 10
        },
        {
          "topic": "Respiratory Support and Mechanisms",
          "works": 10
        },
        {
          "topic": "Frailty in Older Adults",
          "works": 9
        },
        {
          "topic": "Ultrasound in Clinical Applications",
          "works": 7
        },
        {
          "topic": "Hemodynamic Monitoring and Therapy",
          "works": 7
        },
        {
          "topic": "Acute Kidney Injury Research",
          "works": 5
        },
        {
          "topic": "Cardiac Arrest and Resuscitation",
          "works": 5
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 4
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sean M. Bagshaw",
          "works": 27
        },
        {
          "name": "John Basmaji",
          "works": 24
        },
        {
          "name": "Bram Rochwerg",
          "works": 21
        },
        {
          "name": "Oleksa Rewa",
          "works": 20
        },
        {
          "name": "Kirsten M. Fiest",
          "works": 17
        },
        {
          "name": "Dawn Opgenorth",
          "works": 15
        },
        {
          "name": "Wendy Sligl",
          "works": 15
        },
        {
          "name": "Ian Ball",
          "works": 14
        },
        {
          "name": "Kimberley Lewis",
          "works": 14
        },
        {
          "name": "Janek Senaratne",
          "works": 12
        },
        {
          "name": "Sebastian Kilcommons",
          "works": 11
        },
        {
          "name": "Constantine Karvellas",
          "works": 11
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4414575168",
          "year": 2026,
          "title": "Intensive Care Unit and Hospital Mortality for non-COVID Critically ill Patients Before, and During the COVID-19 Pandemic in Alberta Hospitals: Retrospective, Observational Cohort Study",
          "type": "article",
          "venue": "Journal of Intensive Care Medicine",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and healthcare impacts",
            "COVID-19 Clinical Research Studies",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W4416867459",
          "year": 2025,
          "title": "Cost-Effectiveness of Pantoprazole to Prevent Upper Gastrointestinal Bleeding in Mechanically Ventilated Patients",
          "type": "article",
          "venue": "JAMA Network Open",
          "cited_by_count": 0,
          "topics": [
            "Nosocomial Infections in ICU",
            "Respiratory Support and Mechanisms",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4417019563",
          "year": 2025,
          "title": "Exploring the factors affecting ICU nurse retention during and post-COVID-19: A qualitative descriptive interview study",
          "type": "article",
          "venue": "Intensive and Critical Care Nursing",
          "cited_by_count": 2,
          "topics": [
            "Nursing education and management",
            "Family and Patient Care in Intensive Care Units",
            "Nursing Roles and Practices"
          ]
        },
        {
          "openalex_id": "W4406308314",
          "year": 2025,
          "title": "Five-Year Results With Patisiran for Hereditary Transthyretin Amyloidosis With Polyneuropathy",
          "type": "article",
          "venue": "JAMA Neurology",
          "cited_by_count": 33,
          "topics": [
            "Amyloidosis: Diagnosis, Treatment, Outcomes",
            "Alzheimer's disease research and treatments",
            "Parathyroid Disorders and Treatments"
          ]
        },
        {
          "openalex_id": "W4406087320",
          "year": 2025,
          "title": "Limitation of life-sustaining treatments in Asian ICUs: theory versus practice",
          "type": "article",
          "venue": "Critical Care",
          "cited_by_count": 0,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Family and Patient Care in Intensive Care Units",
            "Ethics in medical practice"
          ]
        },
        {
          "openalex_id": "W4411615121",
          "year": 2025,
          "title": "Protocol for an Economic Evaluation Alongside the Re-Evaluating the Inhibition of Stress Erosions (E-REVISE) Trial",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 1,
          "topics": [
            "Sexual function and dysfunction studies",
            "Dermatologic Treatments and Research",
            "Pain Management and Treatment"
          ]
        },
        {
          "openalex_id": "W2211811380",
          "year": 2015,
          "title": "Extracorporeal membrane oxygenation rescue for extrinsic airway compression and cardiac tamponade with multiple transports for mediastinal Burkitt’s lymphoma radiation and chemotherapy: case report and review",
          "type": "article",
          "venue": "Case Studies in Surgery",
          "cited_by_count": 1,
          "topics": [
            "Cardiac tumors and thrombi",
            "Mechanical Circulatory Support Devices",
            "Cardiac Structural Anomalies and Repair"
          ]
        },
        {
          "openalex_id": "W1812302601",
          "year": 2015,
          "title": "Heart transplantation from a dermatomyositis donor: Case report and review",
          "type": "article",
          "venue": "Case Reports in Internal Medicine",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory Myopathies and Dermatomyositis",
            "Eosinophilic Disorders and Syndromes",
            "Neurogenetic and Muscular Disorders Research"
          ]
        },
        {
          "openalex_id": "W2504739926",
          "year": 2016,
          "title": "Factors Associated With the Increasing Rates of Discharges Directly Home From Intensive Care Units—A Direct From ICU Sent Home Study",
          "type": "article",
          "venue": "Journal of Intensive Care Medicine",
          "cited_by_count": 28,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Intensive Care Unit Cognitive Disorders",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W2757577280",
          "year": 2017,
          "title": "Patient, Family, and Physician Satisfaction With Planning for Direct Discharge to Home From Intensive Care Units: Direct From ICU Sent Home Study",
          "type": "article",
          "venue": "Journal of Intensive Care Medicine",
          "cited_by_count": 19,
          "topics": [
            "Intensive Care Unit Cognitive Disorders",
            "Frailty in Older Adults",
            "Heart Failure Treatment and Management"
          ]
        },
        {
          "openalex_id": "W4399671024",
          "year": 2024,
          "title": "Stress Ulcer Prophylaxis during Invasive Mechanical Ventilation",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 90,
          "topics": [
            "Nosocomial Infections in ICU",
            "Sepsis Diagnosis and Treatment",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W2764226479",
          "year": 2017,
          "title": "Point-of-care transcranial Doppler by intensivists",
          "type": "article",
          "venue": "The Ultrasound Journal",
          "cited_by_count": 81,
          "topics": [
            "Traumatic Brain Injury and Neurovascular Disturbances",
            "Cerebrospinal fluid and hydrocephalus",
            "Intracranial Aneurysms: Treatment and Complications"
          ]
        },
        {
          "openalex_id": "W4282915158",
          "year": 2022,
          "title": "Probiotics in Critical Illness: A Systematic Review and Meta-Analysis of Randomized Controlled Trials",
          "type": "review",
          "venue": "Critical Care Medicine",
          "cited_by_count": 63,
          "topics": [
            "Probiotics and Fermented Foods",
            "Nosocomial Infections in ICU",
            "Gut microbiota and health"
          ]
        },
        {
          "openalex_id": "W2890127880",
          "year": 2018,
          "title": "Impact of Critical Care Transesophageal Echocardiography in Medical–Surgical ICU Patients: Characteristics and Results From 274 Consecutive Examinations",
          "type": "article",
          "venue": "Journal of Intensive Care Medicine",
          "cited_by_count": 51,
          "topics": [
            "Ultrasound in Clinical Applications",
            "Hemodynamic Monitoring and Therapy",
            "Cardiac Valve Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W4282965815",
          "year": 2022,
          "title": "Parenteral Vitamin C in Patients with Severe Infection: A Systematic Review",
          "type": "review",
          "venue": "NEJM Evidence",
          "cited_by_count": 44,
          "topics": [
            "Vitamin C and Antioxidants Research",
            "Vitamin K Research Studies",
            "Climate Change and Health Impacts"
          ]
        },
        {
          "openalex_id": "W4283391837",
          "year": 2022,
          "title": "Non-COVID outcomes associated with the coronavirus disease-2019 (COVID-19) pandemic effects study (COPES): A systematic review and meta-analysis",
          "type": "review",
          "venue": "PLoS ONE",
          "cited_by_count": 41,
          "topics": [
            "COVID-19 and healthcare impacts",
            "COVID-19 Clinical Research Studies",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W4390414367",
          "year": 2023,
          "title": "Prospective Study of Ultrasound Markers of Organ Congestion in Critically Ill Patients With Acute Kidney Injury",
          "type": "article",
          "venue": "Kidney International Reports",
          "cited_by_count": 39,
          "topics": [
            "Acute Kidney Injury Research",
            "Renal and Vascular Pathologies",
            "Liver Disease and Transplantation"
          ]
        },
        {
          "openalex_id": "W2977559213",
          "year": 2019,
          "title": "Better With Ultrasound",
          "type": "article",
          "venue": "CHEST Journal",
          "cited_by_count": 36,
          "topics": [
            "Traumatic Brain Injury and Neurovascular Disturbances",
            "Ultrasound in Clinical Applications",
            "Cardiac, Anesthesia and Surgical Outcomes"
          ]
        }
      ]
    }
  },
  {
    "name": "Vivian Reckers-Droog",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1462-PHD",
        "title": "Examining the desirability, feasibility, and impact of involving children in the valuation of EQ-5D-Y health states",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "20190920",
        "title": "Understanding adult preferences in the valuation of child and adolescent health states measured with the EQ-5D-Y: A qualitative approach.",
        "working_group": "Youth"
      },
      {
        "project_id": "2154-RA",
        "title": "Improving the way we ask children and young people to participate in paediatric valuation tasks – co-designing improvements to the EQ-5D-Y valuation and interview protocol with young people and experts",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5121459836",
      "display_name": "Vivian Reckers-droog",
      "orcid": "",
      "reported_affiliation": "Erasmus University Rotterdam",
      "works_count": 9,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 5
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 2
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 1
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 1
        },
        {
          "topic": "COVID-19 and healthcare impacts",
          "works": 1
        },
        {
          "topic": "Healthcare innovation and challenges",
          "works": 1
        },
        {
          "topic": "Intergenerational Family Dynamics and Caregiving",
          "works": 1
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 1
        },
        {
          "topic": "Accounting and Organizational Management",
          "works": 1
        },
        {
          "topic": "Evaluation and Performance Assessment",
          "works": 1
        },
        {
          "topic": "Healthcare Operations and Scheduling Optimization",
          "works": 1
        },
        {
          "topic": "Sepsis Diagnosis and Treatment",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Philipa Mos",
          "works": 5
        },
        {
          "name": "Saskia Knies",
          "works": 4
        },
        {
          "name": "Werner Brouwer",
          "works": 4
        },
        {
          "name": "Anouk M.I.A. van Alphen",
          "works": 1
        },
        {
          "name": "Robert Baatenburg de Jong",
          "works": 1
        },
        {
          "name": "Thomas Reindersma",
          "works": 1
        },
        {
          "name": "Stijn B. Peeters",
          "works": 1
        },
        {
          "name": "Silvia Evers",
          "works": 1
        },
        {
          "name": "B. Wijnen",
          "works": 1
        },
        {
          "name": "Leonie M Huis In 't Veld",
          "works": 1
        },
        {
          "name": "Frederick W. Thielen",
          "works": 1
        },
        {
          "name": "Tim A. Kanters",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7129066604",
          "year": 2026,
          "title": "From Paper to Platform: Updating the Dutch Costing Manual and Launching a Web Application",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 0,
          "topics": [
            "Accounting and Organizational Management",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Evaluation and Performance Assessment"
          ]
        },
        {
          "openalex_id": "W7118370527",
          "year": 2026,
          "title": "Resource allocation in social care and the consequences for equitable access: findings from a secondary analysis of a systematic review",
          "type": "review",
          "venue": "Health Economics Policy and Law",
          "cited_by_count": 0,
          "topics": [
            "Healthcare innovation and challenges",
            "Intergenerational Family Dynamics and Caregiving",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W7155038768",
          "year": 2026,
          "title": "Understanding public opposition to negative reimbursement decisions in healthcare: A systematic review",
          "type": "review",
          "venue": "Social Science & Medicine",
          "cited_by_count": 0,
          "topics": [
            "Healthcare cost, quality, practices",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W7162076829",
          "year": 2026,
          "title": "Using Proportional and Absolute Shortfall in Reimbursement Decision-Making in the Netherlands: Implications for Oncology Drugs for Older Patients",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W7130872283",
          "year": 2026,
          "title": "“They Are Not Going to Be Happy”: An Ethnographic Study of the Prioritization of Patients Awaiting Elective Surgery in an Academic Hospital in the Netherlands",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Operations and Scheduling Optimization",
            "Sepsis Diagnosis and Treatment",
            "Emergency and Acute Care Studies"
          ]
        },
        {
          "openalex_id": "W7117459312",
          "year": 2025,
          "title": "OP05 Societal Preferences For Prioritizing Patients Suffering From Breast Cancer, Deafness, Or Knee Arthrosis For Scarce Surgical Capacity",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "COVID-19 and healthcare impacts"
          ]
        },
        {
          "openalex_id": "W7155455552",
          "year": 2024,
          "title": "<b>Kostenhandleiding </b>voor economische evaluaties in de gezondheidszorg::Methodologie en Referentieprijzen",
          "type": "report",
          "venue": "EUR Research Repository (Erasmus University Rotterdam)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7117449857",
          "year": 2025,
          "title": "OP06 The Specifics Of Public Opposition To Negative Reimbursement Decisions In Health Care: A Systematic Review",
          "type": "review",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W7161272770",
          "year": 2025,
          "title": "Understanding public opposition to negative reimbursement decisions in healthcare: Dataset underlying the systematic review",
          "type": "dataset",
          "venue": "DataverseNL",
          "cited_by_count": 0,
          "topics": []
        }
      ]
    }
  },
  {
    "name": "Wenjing Zhou",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1654-TVG",
        "title": "The impact of COVID-19 on EQ-5D-Y-3L, EQ-TIPS, EQ-5D-5L and EQ-HWB-S in Chinese children and their parent carers",
        "working_group": "Youth"
      },
      {
        "project_id": "1742-EO",
        "title": "Applying for travel scholarship to attend the 2023 ISPOR Europe Meeting: Testing the Psychometric Properties of Several EuroQol Instruments for Measuring the Impact of COVID-19 in a Large Sample of Chinese Children and their Parent Carers",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1874-TVG",
        "title": "A travel grant to support a clinical application of PROMs in pediatrics with a focus on EQ-5D-Y-5L and PedsQL",
        "working_group": "Youth, Education and Outreach"
      },
      {
        "project_id": "2152-RA",
        "title": "A comprehensive Psychometric Validation of EQ Instruments for Early Childhood Health-Related Quality of Life and Caregiver Spillover, including EQ-TIPS, EQ-5D-Y-5L, EQ-5D-5L with Sleep and Fatigue Bolt-ons, and the EQ-HWB-S",
        "working_group": "Descriptive Systems, Youth, EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5080372262",
      "display_name": "Wenjing Zhou",
      "orcid": "0000-0003-0770-4564",
      "reported_affiliation": "",
      "works_count": 10,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 5
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 3
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 2
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 2
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 2
        },
        {
          "topic": "School Health and Nursing Education",
          "works": 2
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 1
        },
        {
          "topic": "Respiratory viral infections research",
          "works": 1
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 1
        },
        {
          "topic": "Restless Legs Syndrome Research",
          "works": 1
        },
        {
          "topic": "Complementary and Alternative Medicine Studies",
          "works": 1
        },
        {
          "topic": "Pathogenesis and Treatment of Hiccups",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jan J.V. Busschbach",
          "works": 7
        },
        {
          "name": "Zhihao Yang",
          "works": 7
        },
        {
          "name": "Michael Herdman",
          "works": 6
        },
        {
          "name": "Yanming Lu",
          "works": 4
        },
        {
          "name": "Pei Wang",
          "works": 4
        },
        {
          "name": "Bin Wu",
          "works": 4
        },
        {
          "name": "Nan Luo",
          "works": 4
        },
        {
          "name": "Bo Ding",
          "works": 3
        },
        {
          "name": "Yaqin Li",
          "works": 1
        },
        {
          "name": "Y. Lu",
          "works": 1
        },
        {
          "name": "Anle Shen",
          "works": 1
        },
        {
          "name": "Min Xia",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4408246071",
          "year": 2025,
          "title": "Are EQ‐5D‐Y‐3L and EQ‐5D‐Y‐5L Useful Tools to Assess Health Outcomes in Children With Asthma? An Analysis of Child and Parental Carer Reporting",
          "type": "article",
          "venue": "Pediatric Pulmonology",
          "cited_by_count": 2,
          "topics": [
            "Asthma and respiratory diseases",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4407161902",
          "year": 2025,
          "title": "EQ-5D-5L or EQ-HWB-S: Which is the Better Instrument for Capturing Spillover Effects in Parental Carers of Children with COVID-19?",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 9,
          "topics": [
            "COVID-19 and Mental Health",
            "Family and Disability Support Research",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W4411428313",
          "year": 2025,
          "title": "Validation of EuroQol instruments in paediatric patients and their caregivers in China: protocol for a prospective observational study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4401053400",
          "year": 2024,
          "title": "Psychometric validation of the Chinese versions of EQ-5D-Y-3L and the experimental EQ-TIPS in children and adolescents with COVID-19",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 8,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Respiratory viral infections research",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W4391824173",
          "year": 2024,
          "title": "Validity and responsiveness of EQ-5D-Y in children with haematological malignancies and their caregivers",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 5,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W4313521872",
          "year": 2023,
          "title": "Early intravenous administration of tirofiban is recommended in patients with acute ischemic stroke treated with alteplase: a meta-analysis",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Venous Thromboembolism Diagnosis and Management",
            "Traumatic Brain Injury and Neurovascular Disturbances"
          ]
        },
        {
          "openalex_id": "W2891305108",
          "year": 2018,
          "title": "Association between storage age of transfused red blood cells and clinical outcomes in critically ill adults: A meta-analysis of randomized controlled trials",
          "type": "review",
          "venue": "Medicina Intensiva",
          "cited_by_count": 6,
          "topics": [
            "Blood transfusion and management",
            "Trauma, Hemostasis, Coagulopathy, Resuscitation",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4223587990",
          "year": 2022,
          "title": "Clinical Efficacy and Safety of Massage for the Treatment of Restless Leg Syndrome in Hemodialysis Patients: A Meta-Analysis of 5 Randomized Controlled Trials",
          "type": "review",
          "venue": "Frontiers in Psychiatry",
          "cited_by_count": 10,
          "topics": [
            "Restless Legs Syndrome Research",
            "Complementary and Alternative Medicine Studies",
            "Pathogenesis and Treatment of Hiccups"
          ]
        },
        {
          "openalex_id": "W4388303835",
          "year": 2023,
          "title": "Is EQ-5D-Y a useful tool to assess health outcomes in children with asthma? An analysis of child and caregiver reporting.",
          "type": "preprint",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Pharmaceutical studies and practices",
            "School Health and Nursing Education"
          ]
        }
      ]
    }
  },
  {
    "name": "Willem van Veghel",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1584-SG",
        "title": "Exploring the added value of the EQ-5D-5L in a VBHC setting: implementing and prediction",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5003208889",
      "display_name": "Willem H. P. van Veghel",
      "orcid": "",
      "reported_affiliation": "Sint Franciscus Gasthuis",
      "works_count": 2,
      "top_topics": [
        {
          "topic": "Burn Injury Management and Outcomes",
          "works": 1
        },
        {
          "topic": "Wound Healing and Treatments",
          "works": 1
        },
        {
          "topic": "Injury Epidemiology and Prevention",
          "works": 1
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 1
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 1
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "A. Weel",
          "works": 2
        },
        {
          "name": "Raaba S. M. Thambithurai",
          "works": 1
        },
        {
          "name": "Denise van Uden",
          "works": 1
        },
        {
          "name": "Jean-Bart Bügel",
          "works": 1
        },
        {
          "name": "Anouk Pijpe",
          "works": 1
        },
        {
          "name": "M.K. Nieuwenhuis",
          "works": 1
        },
        {
          "name": "Cornelis H. van der Vlies",
          "works": 1
        },
        {
          "name": "Margriet E. van Baar",
          "works": 1
        },
        {
          "name": "S. Boon",
          "works": 1
        },
        {
          "name": "T.M.A.L. Klem",
          "works": 1
        },
        {
          "name": "JB Bugel",
          "works": 1
        },
        {
          "name": "Erwin Birnie",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4414941195",
          "year": 2025,
          "title": "Outcomes and costs in specialized burn care: Adapting the Quality Cost Indicator (QCI) model for burn care",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 1,
          "topics": [
            "Burn Injury Management and Outcomes",
            "Wound Healing and Treatments",
            "Injury Epidemiology and Prevention"
          ]
        },
        {
          "openalex_id": "W4297019871",
          "year": 2022,
          "title": "Quality cost indicator: Reassessing the effects of health outcomes on healthcare expenditure. A retrospective cohort study",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Clinical practice guidelines implementation"
          ]
        }
      ]
    }
  },
  {
    "name": "Wolfgang Greiner",
    "member_affiliation": "Bielefeld University",
    "is_member": true,
    "projects": [
      {
        "project_id": "1603-RA",
        "title": "Evaluation of different methods for handling missing EQ-5D-5L data – an explorative simulation study and empirical application",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2012020",
        "title": "German tariff for EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "2013200",
        "title": "Extension of the labels within the EQ-5D-Y",
        "working_group": "Youth"
      },
      {
        "project_id": "2014030",
        "title": "A German Tariff for the EQ-5D-5L - an explorative pre-study",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014160",
        "title": "Comparing valuation of the EQ-5D-Y and the EQ-5D-3L: The impact of wording and perspective",
        "working_group": "Youth"
      },
      {
        "project_id": "2015200",
        "title": "Feasibility and application of the EQ-5D in elderly",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2016530",
        "title": "Application study of the EQ-5D-5L in oncology: linking self-reported quality of life of patients with metastatic colorectal cancer to clinical data of a German tumor registry",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20170020",
        "title": "Comparison of different model specifications for the frequentist estimation of random effect hybrid",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180010",
        "title": "Extending the QALY - Testing face and content validity with patients, social-care users and carers in Germany",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "20180260",
        "title": "Testing the robustness of the German EQ-5D-5L value set for people with health impairments",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180510",
        "title": "Valuing the EQ-5D-Y-3L in Germany, Spain and Slovenia",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2433-RA",
        "title": "Psychometric Evaluation of the EQ-5D-5L in Sepsis Patients",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5001823062",
      "display_name": "Wolfgang Greiner",
      "orcid": "0000-0001-9552-6969",
      "reported_affiliation": "Bielefeld University",
      "works_count": 570,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 145
        },
        {
          "topic": "Health and Medical Studies",
          "works": 133
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 35
        },
        {
          "topic": "Medical and Health Sciences Research",
          "works": 31
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 27
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 24
        },
        {
          "topic": "Cervical Cancer and HPV Research",
          "works": 24
        },
        {
          "topic": "Social and Demographic Issues in Germany",
          "works": 23
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 21
        },
        {
          "topic": "Global Health Care Issues",
          "works": 19
        },
        {
          "topic": "Corporate Governance and Management",
          "works": 18
        },
        {
          "topic": "Medical Practices and Rehabilitation",
          "works": 18
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Oliver Damm",
          "works": 48
        },
        {
          "name": "Julian Witte",
          "works": 45
        },
        {
          "name": "Simone Kreimeier",
          "works": 33
        },
        {
          "name": "Stefan Scholz",
          "works": 31
        },
        {
          "name": "Stefan N. Willich",
          "works": 28
        },
        {
          "name": "Thomas Mittendorf",
          "works": 26
        },
        {
          "name": "B. Ultsch",
          "works": 25
        },
        {
          "name": "Christoph Vauth",
          "works": 23
        },
        {
          "name": "Christian Jacob",
          "works": 23
        },
        {
          "name": "Sebastian Braun",
          "works": 23
        },
        {
          "name": "Kristina Ludwig",
          "works": 21
        },
        {
          "name": "Bastian Surmann",
          "works": 21
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7160997629",
          "year": 2026,
          "title": "Development Process of a Clinical Decision Support System for Empiric Antibiotic Therapies in Patients With Sepsis: Case Study",
          "type": "article",
          "venue": "JMIR Medical Informatics",
          "cited_by_count": 0,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Machine Learning in Healthcare",
            "Bacterial Identification and Susceptibility Testing"
          ]
        },
        {
          "openalex_id": "W7140315339",
          "year": 2026,
          "title": "Epidemiology and economic burden of medically attended influenza and influenza-like illness in Germany, 2016–2019",
          "type": "article",
          "venue": "Journal of Medical Economics",
          "cited_by_count": 0,
          "topics": [
            "Influenza Virus Research Studies",
            "Respiratory viral infections research",
            "COVID-19 epidemiological studies"
          ]
        },
        {
          "openalex_id": "W4415942776",
          "year": 2025,
          "title": "2339P Financial considerations and the treatment interval of pembrolizumab: Evidence from a claims data analysis in the outpatient sector in Germany",
          "type": "article",
          "venue": "Annals of Oncology",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer Immunotherapy and Biomarkers"
          ]
        },
        {
          "openalex_id": "W4415941872",
          "year": 2025,
          "title": "2572P Financial distress among cancer patients in Germany: Results from a quantitative study with the new Financial Distress of Cancer Assessment Tool (FIAT)",
          "type": "article",
          "venue": "Annals of Oncology",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Cancer survivorship and care",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4416531557",
          "year": 2025,
          "title": "Acceptance of telemedicine among care personnel in inpatient and outpatient elderly care: a systematic review",
          "type": "review",
          "venue": "BMC Geriatrics",
          "cited_by_count": 1,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Mobile Health and mHealth Applications",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W4410852197",
          "year": 2025,
          "title": "Development Process of a Clinical Decision Support System for Empiric Antibiotic Therapies in Sepsis Patients",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 3,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Pharmaceutical Practices and Patient Outcomes",
            "Antibiotic Use and Resistance"
          ]
        },
        {
          "openalex_id": "W208367388",
          "year": 1960,
          "title": "Hardwood sawdust for cold caustic pulp appears feasible.",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Materials Engineering and Processing",
            "Lignin and Wood Chemistry"
          ]
        },
        {
          "openalex_id": "W2588130663",
          "year": 1985,
          "title": "Gefährdet die Ausgabe eigener Schuldverschreibungen durch Kreditgenossenschaften die Zusammenarbeit im genossenschaftlichen Bankenverbund?",
          "type": "article",
          "venue": "Zeitschrift für das gesamte Genossenschaftswesen",
          "cited_by_count": 2,
          "topics": [
            "Corporate Governance and Law"
          ]
        },
        {
          "openalex_id": "W12583483",
          "year": 1990,
          "title": "Ammonia barging risk assessment.",
          "type": "article",
          "venue": "",
          "cited_by_count": 2,
          "topics": [
            "Recycling and Waste Management Techniques"
          ]
        },
        {
          "openalex_id": "W2414297191",
          "year": 1995,
          "title": "[Socioeconomic evaluation of the effect of rhDNase on the cost of treating infections of the respiratory tract in patients with cystic fibrosis].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 12,
          "topics": [
            "Cystic Fibrosis Research Advances",
            "Pediatric health and respiratory diseases",
            "Respiratory viral infections research"
          ]
        },
        {
          "openalex_id": "W2466926363",
          "year": 2016,
          "title": "Barriers and Strategies in Guideline Implementation—A Scoping Review",
          "type": "article",
          "venue": "Healthcare",
          "cited_by_count": 944,
          "topics": [
            "Clinical practice guidelines implementation",
            "Health Policy Implementation Science",
            "Primary Care and Health Outcomes"
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
          "openalex_id": "W2788008365",
          "year": 2018,
          "title": "German Value Set for the EQ-5D-5L",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 614,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
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
          "openalex_id": "W2165758480",
          "year": 2007,
          "title": "Health Technology Assessment (HTA)",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 461,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2081845389",
          "year": 2004,
          "title": "Validating the EQ-5D with time trade off for the German population",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 390,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Health and Medical Studies"
          ]
        },
        {
          "openalex_id": "W3033327429",
          "year": 2020,
          "title": "Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 307,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        }
      ]
    }
  }
]
