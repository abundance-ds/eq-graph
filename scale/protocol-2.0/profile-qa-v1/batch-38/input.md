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
    "name": "Mihir Gandhi",
    "member_affiliation": "Duke-NUS Medical School",
    "is_member": true,
    "projects": [
      {
        "project_id": "20170180",
        "title": "An EQ-VT study of heart disease patients",
        "working_group": "Valuation"
      },
      {
        "project_id": "2224-RA",
        "title": "Evaluating content validity and measurement properties of EQ-HWB-S in patients with advanced illnesses receiving end-of-life care: A mixed-methods study",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "389-RA",
        "title": "A head-to-head comparison of measurement properties of EQ-5D-Y-3L and EQ-5D-Y-5L in children and adolescents with heart diseases",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5087601665",
      "display_name": "Mihir Gandhi",
      "orcid": "0000-0002-8902-2710",
      "reported_affiliation": "Duke-NUS Medical School",
      "works_count": 167,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 21
        },
        {
          "topic": "Hepatocellular Carcinoma Treatment and Prognosis",
          "works": 18
        },
        {
          "topic": "Blood Pressure and Hypertension Studies",
          "works": 18
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 11
        },
        {
          "topic": "Health Promotion and Cardiovascular Prevention",
          "works": 10
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 9
        },
        {
          "topic": "Diabetes, Cardiovascular Risks, and Lipoproteins",
          "works": 9
        },
        {
          "topic": "Cholangiocarcinoma and Gallbladder Cancer Studies",
          "works": 8
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 8
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 8
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 7
        },
        {
          "topic": "Cardiac, Anesthesia and Surgical Outcomes",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Eric Finkelstein",
          "works": 41
        },
        {
          "name": "Aliya Naheed",
          "works": 20
        },
        {
          "name": "Nan Luo",
          "works": 20
        },
        {
          "name": "Yin Bun Cheung",
          "works": 19
        },
        {
          "name": "Julian Thumboo",
          "works": 19
        },
        {
          "name": "Tazeen H. Jafar",
          "works": 18
        },
        {
          "name": "Imtiaz Jehan",
          "works": 18
        },
        {
          "name": "Elizabeth L. Turner",
          "works": 17
        },
        {
          "name": "Anuradhani Kasturiratne",
          "works": 17
        },
        {
          "name": "Pryseley Nkouibert Assam",
          "works": 17
        },
        {
          "name": "Shah Ebrahim",
          "works": 16
        },
        {
          "name": "Marcel Bilger",
          "works": 15
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7165143940",
          "year": 2026,
          "title": "Direct Medical Costs Among an Inception Cohort of Patients With Inflammatory Arthritis and Osteoarthritis",
          "type": "article",
          "venue": "International Journal of Rheumatic Diseases",
          "cited_by_count": 0,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies",
            "Spondyloarthritis Studies and Treatments",
            "Osteoarthritis Treatment and Mechanisms"
          ]
        },
        {
          "openalex_id": "W7129347164",
          "year": 2026,
          "title": "Effectiveness of Multicomponent Interventions in Slowing Progression of CKD Stages G3-G4",
          "type": "article",
          "venue": "Clinical Journal of the American Society of Nephrology",
          "cited_by_count": 0,
          "topics": [
            "Chronic Kidney Disease and Diabetes",
            "Dialysis and Renal Disease Management",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4406352766",
          "year": 2025,
          "title": "Aspirin after completion of standard adjuvant therapy for colorectal cancer (ASCOLT): an international, multicentre, phase 3, randomised, double-blind, placebo-controlled trial",
          "type": "article",
          "venue": "The Lancet. Gastroenterology & hepatology",
          "cited_by_count": 31,
          "topics": [
            "Inflammatory mediators and NSAID effects",
            "Antiplatelet Therapy and Cardiovascular Diseases",
            "Cancer, Stress, Anesthesia, and Immune Response"
          ]
        },
        {
          "openalex_id": "W4412752853",
          "year": 2025,
          "title": "Assessment of Dietary Intake of Zinc and its Association with the Immune Status and Gut Health in Children Diagnosed with Autism Spectrum Disorder (ASD) Aged 6-14 Years",
          "type": "article",
          "venue": "International Journal for Research in Applied Science and Engineering Technology",
          "cited_by_count": 0,
          "topics": [
            "Child Nutrition and Water Access",
            "Child Nutrition and Feeding Issues"
          ]
        },
        {
          "openalex_id": "W4406795551",
          "year": 2025,
          "title": "Development of the PRECIOUS Short-Form (PRECIOUS-SF) quality of care measure for children with serious illnesses",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Pediatric Pain Management Techniques",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4413848835",
          "year": 2025,
          "title": "EORTC QLU-C10D was similarly valid and sensitive as EQ-5D-5L but more responsive to cancer patients' health deterioration",
          "type": "article",
          "venue": "Journal of Clinical Epidemiology",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2167330481",
          "year": 1979,
          "title": "Absorption of Xanthine Oxidase from the Instestines of Rats and Rabbits and its Role in initiation of Atherosclerosis",
          "type": "article",
          "venue": "Zentralblatt für Veterinärmedizin Reihe A",
          "cited_by_count": 11,
          "topics": [
            "Gout, Hyperuricemia, Uric Acid",
            "Peroxisome Proliferator-Activated Receptors",
            "Lipid metabolism and disorders"
          ]
        },
        {
          "openalex_id": "W2000100049",
          "year": 1979,
          "title": "Partial Characterization of Xanthine Oxidase (XO) from Buffalo Milk Fat Globules and Variation in the XO content of Milk",
          "type": "article",
          "venue": "Zentralblatt für Veterinärmedizin Reihe A",
          "cited_by_count": 3,
          "topics": [
            "Gout, Hyperuricemia, Uric Acid",
            "Ruminant Nutrition and Digestive Physiology",
            "T-cell and Retrovirus Studies"
          ]
        },
        {
          "openalex_id": "W2252983407",
          "year": 1994,
          "title": "Regulation of mitogenesis, motogenesis, and tubulogenesis by hepatocyte growth factor in renal collecting duct cells",
          "type": "article",
          "venue": "American Journal of Physiology-Renal Physiology",
          "cited_by_count": 121,
          "topics": [
            "Liver physiology and pathology",
            "Organ Transplantation Techniques and Outcomes",
            "Renal and related cancers"
          ]
        },
        {
          "openalex_id": "W1983751403",
          "year": 2007,
          "title": "NATRIURETIC PEPTIDE TESTING AND APACHE II SCORES FOR THE EVALUATION AND PREDICTION OF OUTCOME IN ACUTELY ILL PATIENTS: A PROSPECTIVE COHORT STUDY",
          "type": "conference-abstract",
          "venue": "CHEST Journal",
          "cited_by_count": 0,
          "topics": [
            "Hemodynamic Monitoring and Therapy",
            "Cardiac, Anesthesia and Surgical Outcomes"
          ]
        },
        {
          "openalex_id": "W2791703762",
          "year": 2018,
          "title": "SIRveNIB: Selective Internal Radiation Therapy Versus Sorafenib in Asia-Pacific Patients With Hepatocellular Carcinoma",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 652,
          "topics": [
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Hepatitis B Virus Studies",
            "Cholangiocarcinoma and Gallbladder Cancer Studies"
          ]
        },
        {
          "openalex_id": "W3006880319",
          "year": 2020,
          "title": "A Community-Based Intervention for Managing Hypertension in Rural South Asia",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 311,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Global Maternal and Child Health",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2048316728",
          "year": 2012,
          "title": "Induction Chemoradiation Is Not Superior to Induction Chemotherapy Alone in Stage IIIA Lung Cancer",
          "type": "article",
          "venue": "The Annals of Thoracic Surgery",
          "cited_by_count": 119,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Breast Cancer Treatment Studies"
          ]
        },
        {
          "openalex_id": "W2074820476",
          "year": 2011,
          "title": "Cholecystectomy Concomitant with Laparoscopic Gastric Bypass: A Trend Analysis of the Nationwide Inpatient Sample from 2001 to 2008",
          "type": "article",
          "venue": "Obesity Surgery",
          "cited_by_count": 118,
          "topics": [
            "Bariatric Surgery and Outcomes",
            "Gallbladder and Bile Duct Disorders",
            "Minimally Invasive Surgical Techniques"
          ]
        },
        {
          "openalex_id": "W2901647060",
          "year": 2018,
          "title": "Effectiveness of a Technology-Based Supportive Educational Parenting Program on Parental Outcomes (Part 1): Randomized Controlled Trial",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 108,
          "topics": [
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Infant Development and Preterm Care",
            "Breastfeeding Practices and Influences"
          ]
        },
        {
          "openalex_id": "W2899889607",
          "year": 2018,
          "title": "Art therapy is associated with sustained improvement in cognitive function in the elderly with mild neurocognitive disorder: findings from a pilot randomized controlled trial for art therapy and music reminiscence activity versus usual care",
          "type": "article",
          "venue": "Trials",
          "cited_by_count": 104,
          "topics": [
            "Art Therapy and Mental Health",
            "Dementia and Cognitive Impairment Research",
            "Identity, Memory, and Therapy"
          ]
        },
        {
          "openalex_id": "W1488411822",
          "year": 2014,
          "title": "External Validation of the CRASH and IMPACT Prognostic Models in Severe Traumatic Brain Injury",
          "type": "article",
          "venue": "Journal of Neurotrauma",
          "cited_by_count": 104,
          "topics": [
            "Traumatic Brain Injury and Neurovascular Disturbances",
            "Trauma and Emergency Care Studies",
            "Sepsis Diagnosis and Treatment"
          ]
        }
      ]
    }
  },
  {
    "name": "Mihretab Gebreslassie",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1781-RA",
        "title": "Establishing population norms and assessing the usefulness of EQ-5D in studying health inequalities: a cross-sectional and longitudinal study based on Stockholm public health cohort",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2564-RA",
        "title": "Impact of mode of administration on responses agreement and measurement properties of the EQ-5D and other preference-based outcome measures: a systematic review ",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5085631323",
      "display_name": "Mihretab Gebreslassie",
      "orcid": "0000-0001-9556-0075",
      "reported_affiliation": "Stockholm County Council",
      "works_count": 21,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 5
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 3
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 2
        },
        {
          "topic": "Global Health and Surgery",
          "works": 2
        },
        {
          "topic": "Child Nutrition and Water Access",
          "works": 2
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 2
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 2
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 1
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 1
        },
        {
          "topic": "Gambling Behavior and Treatments",
          "works": 1
        },
        {
          "topic": "Substance Abuse Treatment and Outcomes",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Per Tynelius",
          "works": 7
        },
        {
          "name": "Stefan Fors",
          "works": 7
        },
        {
          "name": "Inna Feldman",
          "works": 6
        },
        {
          "name": "Filipa Sampaio",
          "works": 5
        },
        {
          "name": "Camilla Nystrand",
          "works": 5
        },
        {
          "name": "Richard Ssegonja",
          "works": 5
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 5
        },
        {
          "name": "Sofia Sveréus",
          "works": 5
        },
        {
          "name": "Emelie Heintz",
          "works": 5
        },
        {
          "name": "Anton Lager",
          "works": 4
        },
        {
          "name": "Meresa Berwo Mengesha",
          "works": 3
        },
        {
          "name": "Tesfaye Temesgen Chekole",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7169831773",
          "year": 2026,
          "title": "Additional file 1 of Variations in health-related quality of life across sociodemographic groups, health conditions, and modifiable risk factors: a population-based EQ-5D-3L study",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Geriatric Care and Nursing Homes",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W7169893901",
          "year": 2026,
          "title": "Additional file 1 of Variations in health-related quality of life across sociodemographic groups, health conditions, and modifiable risk factors: a population-based EQ-5D-3L study",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Geriatric Care and Nursing Homes",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W7164026998",
          "year": 2026,
          "title": "Feasibility, acceptability and effectiveness of group antenatal care on maternal health continuum of care and perinatal outcomes in sub-Saharan Africa: a systematic review and meta-analysis",
          "type": "review",
          "venue": "BMJ Global Health",
          "cited_by_count": 0,
          "topics": [
            "Global Maternal and Child Health",
            "Global Health and Surgery",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W7169752373",
          "year": 2026,
          "title": "Variations in health-related quality of life across sociodemographic groups, health conditions, and modifiable risk factors: a population-based EQ-5D-3L study",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W7169839490",
          "year": 2026,
          "title": "Variations in health-related quality of life across sociodemographic groups, health conditions, and modifiable risk factors: a population-based EQ-5D-3L study",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7169875570",
          "year": 2026,
          "title": "Variations in health-related quality of life across sociodemographic groups, health conditions, and modifiable risk factors: a population-based EQ-5D-3L study",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W3088961953",
          "year": 2020,
          "title": "A systematic review of economic evaluations of public health interventions targeting alcohol, tobacco, illicit drug use and problematic gambling: Using a case study to assess transferability",
          "type": "review",
          "venue": "Health Policy",
          "cited_by_count": 21,
          "topics": [
            "Gambling Behavior and Treatments",
            "Substance Abuse Treatment and Outcomes",
            "Opioid Use Disorder Treatment"
          ]
        },
        {
          "openalex_id": "W3015467135",
          "year": 2020,
          "title": "Cost-effectiveness of superabsorbent wound dressing versus standard of care in patients with moderate-to-highly exuding leg ulcers",
          "type": "article",
          "venue": "Journal of Wound Care",
          "cited_by_count": 15,
          "topics": [
            "Diagnosis and Treatment of Venous Diseases",
            "Wound Healing and Treatments",
            "Pressure Ulcer Prevention and Management"
          ]
        },
        {
          "openalex_id": "W3046672200",
          "year": 2020,
          "title": "Economic Evaluations of Public Health Interventions to Improve Mental Health and Prevent Suicidal Thoughts and Behaviours: A Systematic Literature Review",
          "type": "review",
          "venue": "Administration and Policy in Mental Health and Mental Health Services Research",
          "cited_by_count": 25,
          "topics": [
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W3092321875",
          "year": 2020,
          "title": "Economic evaluations of public health interventions for mental health: A systematic literature review",
          "type": "review",
          "venue": "European Journal of Public Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W3020677625",
          "year": 2020,
          "title": "Economic evaluations of public health interventions for physical activity and healthy diet: A systematic review",
          "type": "review",
          "venue": "Preventive Medicine",
          "cited_by_count": 38,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Obesity, Physical Activity, Diet"
          ]
        },
        {
          "openalex_id": "W4285093973",
          "year": 2022,
          "title": "Cohort Profile: The Stockholm Diabetes Prevention Programme (SDPP)",
          "type": "article",
          "venue": "International Journal of Epidemiology",
          "cited_by_count": 12,
          "topics": [
            "Nutritional Studies and Diet",
            "Obesity, Physical Activity, Diet",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W3004579104",
          "year": 2020,
          "title": "Narrative review of interventions suitable for well‐baby clinics to promote infant attachment security and parents’ sensitivity",
          "type": "review",
          "venue": "Acta Paediatrica",
          "cited_by_count": 8,
          "topics": [
            "Attachment and Relationship Dynamics",
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        },
        {
          "openalex_id": "W4390791946",
          "year": 2024,
          "title": "Observational study of selective screening for prediabetes and diabetes in a real-world setting: an interprofessional collaboration method between public dental services and primary health care in Sweden",
          "type": "article",
          "venue": "Scandinavian Journal of Primary Health Care",
          "cited_by_count": 7,
          "topics": [
            "Oral microbiology and periodontitis research",
            "Dental Health and Care Utilization",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W3091978759",
          "year": 2020,
          "title": "Economic evaluations of public health interventions for physical activity and diet: systematic review",
          "type": "article",
          "venue": "European Journal of Public Health",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        }
      ]
    }
  },
  {
    "name": "Milad Karimi",
    "member_affiliation": "",
    "is_member": true,
    "projects": [
      {
        "project_id": "2016560",
        "title": "Investigating the difference between hypothetical and experienced valuations: the case of mistaken expectations",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190550",
        "title": "Public perspectives on patient preferences: an extension to project 2016560",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5076374306",
      "display_name": "Milad Karimi",
      "orcid": "0000-0002-5298-174X",
      "reported_affiliation": "Yazd University",
      "works_count": 56,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 24
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 11
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 8
        },
        {
          "topic": "Global Health Care Issues",
          "works": 6
        },
        {
          "topic": "Interprofessional Education and Collaboration",
          "works": 6
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 5
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 4
        },
        {
          "topic": "Hemophilia Treatment and Research",
          "works": 4
        },
        {
          "topic": "Minerals Flotation and Separation Techniques",
          "works": 4
        },
        {
          "topic": "Metal Extraction and Bioleaching",
          "works": 4
        },
        {
          "topic": "Acute Myeloid Leukemia Research",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Maureen Rutten‐van Mölken",
          "works": 14
        },
        {
          "name": "Maaike Hoedemakers",
          "works": 10
        },
        {
          "name": "John Brazier",
          "works": 9
        },
        {
          "name": "Willemijn Looman",
          "works": 7
        },
        {
          "name": "Apostolos Tsiachristas",
          "works": 5
        },
        {
          "name": "Marc Botteman",
          "works": 5
        },
        {
          "name": "Donna Rowen",
          "works": 4
        },
        {
          "name": "Fenna Leijten",
          "works": 4
        },
        {
          "name": "M. Kamrul Islam",
          "works": 4
        },
        {
          "name": "Flora Peyvandi",
          "works": 4
        },
        {
          "name": "Antonino Cannavò",
          "works": 4
        },
        {
          "name": "Isabella Garagiola",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4417481413",
          "year": 2025,
          "title": "CO157 Investigating the Patient-Relevance of Achieving Blood Phe Thresholds in PKU: Results From an Analysis of the OPAL Study",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Metabolism and Genetic Disorders",
            "Pharmacogenetics and Drug Metabolism",
            "Genomics and Rare Diseases"
          ]
        },
        {
          "openalex_id": "W4406754183",
          "year": 2025,
          "title": "Electrochemical insights into the direct dissolution of impure sphalerites and their partial oxidation in an acidic environment",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 4,
          "topics": [
            "Metal Extraction and Bioleaching",
            "Minerals Flotation and Separation Techniques",
            "Mineral Processing and Grinding"
          ]
        },
        {
          "openalex_id": "W4407196389",
          "year": 2025,
          "title": "How Do Individuals Value Worse-Than-Dead EQ-5D-5L Health States in Composite Time Trade-Off Tasks? A Qualitative Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4402327849",
          "year": 2024,
          "title": "Electrochemical Investigation of Sphalerite Dissolution in an Acidic Environment: Insights on Electrometallurgy",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Metal Extraction and Bioleaching",
            "Minerals Flotation and Separation Techniques",
            "Metallurgical Processes and Thermodynamics"
          ]
        },
        {
          "openalex_id": "W4393962993",
          "year": 2024,
          "title": "The green reductive leaching of manganiferous iron ore and Mn3O4 nanoparticles production: Kinetic modeling and comparison of various reductants",
          "type": "article",
          "venue": "Journal of the Taiwan Institute of Chemical Engineers",
          "cited_by_count": 12,
          "topics": [
            "Extraction and Separation Processes",
            "Minerals Flotation and Separation Techniques",
            "Metal Extraction and Bioleaching"
          ]
        },
        {
          "openalex_id": "W4320002084",
          "year": 2023,
          "title": "Fundamental Electrochemical Insights into the Direct Dissolution of Different Sphalerite and Their Partial Oxidation in Acidic Media",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Minerals Flotation and Separation Techniques",
            "Metal Extraction and Bioleaching",
            "Mineral Processing and Grinding"
          ]
        },
        {
          "openalex_id": "W2329367046",
          "year": 2013,
          "title": "P-110 Evaluation of a high throughput mutation-screening strategy in myelodysplastic syndrome patients and acute myeloid leukemia using Halogenomics™ targeted-gene enrichment technology",
          "type": "conference-abstract",
          "venue": "Leukemia Research",
          "cited_by_count": 0,
          "topics": [
            "Acute Myeloid Leukemia Research",
            "Cancer Genomics and Diagnostics",
            "Molecular Biology Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W2320357242",
          "year": 2015,
          "title": "A mixed methods investigation of methods ofvaluing health: are preferences over healthstates matters of taste, complete, andinformed?",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2149921639",
          "year": 2015,
          "title": "High-throughput mutational screening adds clinically important information in myelodysplastic syndromes and secondary or therapy-related acute myeloid leukemia",
          "type": "article",
          "venue": "Haematologica",
          "cited_by_count": 18,
          "topics": [
            "Acute Myeloid Leukemia Research",
            "Myeloproliferative Neoplasms: Diagnosis and Treatment",
            "Cancer Genomics and Diagnostics"
          ]
        },
        {
          "openalex_id": "W4241099052",
          "year": 2015,
          "title": "Streitfall Erlösung",
          "type": "book",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Religion, Theology, and Education",
            "Biblical Studies and Interpretation",
            "Historical and Linguistic Studies"
          ]
        },
        {
          "openalex_id": "W2279074305",
          "year": 2016,
          "title": "Health, Health-Related Quality of Life, and Quality of Life: What is the Difference?",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 1675,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2906351843",
          "year": 2019,
          "title": "Future Directions in Valuing Benefits for Estimating QALYs: Is Time Up for the EQ-5D?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 87,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2883728347",
          "year": 2018,
          "title": "Strengthening the evidence-base of integrated care for people with multi-morbidity in Europe using Multi-Criteria Decision Analysis (MCDA)",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 70,
          "topics": [
            "Chronic Disease Management Strategies",
            "Interprofessional Education and Collaboration",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2556245455",
          "year": 2016,
          "title": "How do individuals value health states? A qualitative investigation",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2760499076",
          "year": 2017,
          "title": "Experience-based utility and own health state valuation for a health state classification system: why and how to do it",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 54,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2336253832",
          "year": 2016,
          "title": "The Capability Approach: A Critical Review of Its Application in Health Economics",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Systems and Reforms"
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
        }
      ]
    }
  },
  {
    "name": "Mimmi Åström",
    "member_affiliation": "Karolinska Institutet",
    "is_member": true,
    "projects": [
      {
        "project_id": "1776-RA",
        "title": "Psychometric properties of the EQ-5D-Y-3L and EQ-5D-Y-5Lamong children and adolescents with a range of acute and chronic conditions in Bangladesh using cross-sectional and longitudinal study designs",
        "working_group": "Populations and Health Systems, Youth"
      },
      {
        "project_id": "2015400",
        "title": "Development of EQ-5D-Y-3L norms data based on a general population sample of children and adolescents in Sweden",
        "working_group": "Youth"
      },
      {
        "project_id": "20190980",
        "title": "Exploring experiences among adults and adolescents of health state valuation for the EQ-5D-Y-3L - a qualitative study",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5055089597",
      "display_name": "Mimmi Åström",
      "orcid": "0000-0002-6711-5262",
      "reported_affiliation": "Karolinska Institutet",
      "works_count": 17,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 13
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 3
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 2
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 2
        },
        {
          "topic": "Child and Adolescent Psychosocial and Emotional Development",
          "works": 2
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
          "topic": "BRCA gene mutations in cancer",
          "works": 1
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 1
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 1
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 1
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kristina Burström",
          "works": 13
        },
        {
          "name": "Ann‐Charlotte Egmar",
          "works": 4
        },
        {
          "name": "Michael Herdman",
          "works": 4
        },
        {
          "name": "Simone Kreimeier",
          "works": 3
        },
        {
          "name": "Narcís Gusi",
          "works": 3
        },
        {
          "name": "Wolfgang Greiner",
          "works": 3
        },
        {
          "name": "Ola Rolfson",
          "works": 3
        },
        {
          "name": "Fitsum Sebsibe Teni",
          "works": 2
        },
        {
          "name": "Jenny Berg",
          "works": 2
        },
        {
          "name": "Paul Kind",
          "works": 2
        },
        {
          "name": "Miguel Ángel Pérez-Sousa",
          "works": 2
        },
        {
          "name": "Carina Persson",
          "works": 2
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
          "openalex_id": "W4390471965",
          "year": 2023,
          "title": "Did Stress Prevalence Among Adolescents in Scandinavia Change from 2000 to 2019? A literature review",
          "type": "article",
          "venue": "Scandinavian Journal of Child and Adolescent Psychiatry and Psychology",
          "cited_by_count": 3,
          "topics": [
            "Child and Adolescent Psychosocial and Emotional Development",
            "Stress Responses and Cortisol",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W4362706230",
          "year": 2023,
          "title": "Use of the visual analogue scale for health state valuation: a scoping review",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 151,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4210399103",
          "year": 2022,
          "title": "Exploring EQ-5D-Y-3L Experience-Based VAS Values Derived Among Adolescents",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 9,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4213413324",
          "year": 2022,
          "title": "‘Like holding the axe on who should live or not’: adolescents’ and adults’ perceptions of valuing children’s health states using a standardised valuation protocol for the EQ-5D-Y-3L",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 18,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W657527591",
          "year": 2011,
          "title": "A passport to healthcare? : A client perspective on the national health insurance scheme in Ghana",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Systems and Reforms",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1987896463",
          "year": 2014,
          "title": "Measuring health-related quality of life with the EQ-5D-Y instrument in children and adolescents with asthma",
          "type": "article",
          "venue": "Acta Paediatrica",
          "cited_by_count": 63,
          "topics": [
            "Asthma and respiratory diseases",
            "Delphi Technique in Research",
            "Health Systems, Economic Evaluations, Quality of Life"
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
          "openalex_id": "W2765148415",
          "year": 2017,
          "title": "Population Health Status Based On The EQ-5D-3L-Y Among Adolescents In Sweden - Results By Sex, Age And Socio-Economic Status",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
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
          "openalex_id": "W3205826885",
          "year": 2021,
          "title": "Inequality and heterogeneity in health-related quality of life: findings based on a large sample of cross-sectional EQ-5D-5L data from the Swedish general population",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 65,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W3003361186",
          "year": 2020,
          "title": "Whom should we ask? A systematic literature review of the arguments regarding the most accurate source of information for valuation of health states",
          "type": "review",
          "venue": "Quality of Life Research",
          "cited_by_count": 52,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2889649872",
          "year": 2018,
          "title": "Population health status based on the EQ-5D-Y-3L among adolescents in Sweden: Results by sociodemographic factors and self-reported comorbidity",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 45,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cerebral Palsy and Movement Disorders",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W3029204673",
          "year": 2020,
          "title": "EQ-5D-Y-5L as a patient-reported outcome measure in psychiatric inpatient care for children and adolescents – a cross-sectional study",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 32,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Schizophrenia research and treatment",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        }
      ]
    }
  },
  {
    "name": "Min-Joo Woo",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2013020",
        "title": "A Korean valuation study for the EQ-5D-5L",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5028665396",
      "display_name": "Woo‐Jung Song",
      "orcid": "0000-0002-4630-9922",
      "reported_affiliation": "",
      "works_count": 374,
      "top_topics": [
        {
          "topic": "Asthma and respiratory diseases",
          "works": 233
        },
        {
          "topic": "Respiratory and Cough-Related Research",
          "works": 157
        },
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 53
        },
        {
          "topic": "Pediatric health and respiratory diseases",
          "works": 39
        },
        {
          "topic": "Drug-Induced Adverse Reactions",
          "works": 36
        },
        {
          "topic": "Allergic Rhinitis and Sensitization",
          "works": 33
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 24
        },
        {
          "topic": "Inhalation and Respiratory Drug Delivery",
          "works": 20
        },
        {
          "topic": "IL-33, ST2, and ILC Pathways",
          "works": 18
        },
        {
          "topic": "Contact Dermatitis and Allergies",
          "works": 17
        },
        {
          "topic": "Eosinophilic Esophagitis",
          "works": 17
        },
        {
          "topic": "Gastroesophageal reflux and treatments",
          "works": 15
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sang‐Heon Cho",
          "works": 124
        },
        {
          "name": "Yoon‐Seok Chang",
          "works": 102
        },
        {
          "name": "You Sook Cho",
          "works": 82
        },
        {
          "name": "Ji‐Hyang Lee",
          "works": 81
        },
        {
          "name": "Tae‐Bum Kim",
          "works": 79
        },
        {
          "name": "Min‐Hye Kim",
          "works": 77
        },
        {
          "name": "Sae‐Hoon Kim",
          "works": 76
        },
        {
          "name": "Heung‐Woo Park",
          "works": 69
        },
        {
          "name": "So‐Young Park",
          "works": 66
        },
        {
          "name": "Ha‐Kyeong Won",
          "works": 60
        },
        {
          "name": "Hyouk‐Soo Kwon",
          "works": 60
        },
        {
          "name": "Byung‐Jae Lee",
          "works": 58
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7129021053",
          "year": 2026,
          "title": "<i>ERJ Open Research</i> in 2026: progress and future directions",
          "type": "article",
          "venue": "ERJ Open Research",
          "cited_by_count": 0,
          "topics": [
            "Academic Publishing and Open Access",
            "Medical Research and Practices",
            "Meta-analysis and systematic reviews"
          ]
        },
        {
          "openalex_id": "W7165165714",
          "year": 2026,
          "title": "Clinical Features of Cellular Senescence Pathways in Severe Asthma",
          "type": "article",
          "venue": "Allergy",
          "cited_by_count": 0,
          "topics": [
            "Telomeres, Telomerase, and Senescence",
            "Asthma and respiratory diseases",
            "Neutrophil, Myeloperoxidase and Oxidative Mechanisms"
          ]
        },
        {
          "openalex_id": "W7165414270",
          "year": 2026,
          "title": "Exploring cough hypersensitivity patterns across respiratory diseases",
          "type": "article",
          "venue": "Respiratory Medicine",
          "cited_by_count": 0,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Asthma and respiratory diseases",
            "Chronic Obstructive Pulmonary Disease (COPD) Research"
          ]
        },
        {
          "openalex_id": "W7170161398",
          "year": 2026,
          "title": "Interpretive framework for Cough Hypersensitivity Questionnaire scores in chronic cough",
          "type": "article",
          "venue": "ERJ Open Research",
          "cited_by_count": 0,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Asthma and respiratory diseases",
            "Chronic Obstructive Pulmonary Disease (COPD) Research"
          ]
        },
        {
          "openalex_id": "W7169851823",
          "year": 2026,
          "title": "Patient-Anchored Cough Visual Analogue Scale and Leicester Cough Questionnaire Thresholds for Cough Control Classification in Chronic Cough",
          "type": "article",
          "venue": "Lung",
          "cited_by_count": 0,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Dysphagia Assessment and Management",
            "Voice and Speech Disorders"
          ]
        },
        {
          "openalex_id": "W7155401403",
          "year": 2026,
          "title": "Prevalence and associated factors of cough syncope in patients with chronic cough: a multicentre prospective study",
          "type": "article",
          "venue": "ERJ Open Research",
          "cited_by_count": 0,
          "topics": [
            "Cardiovascular Syncope and Autonomic Disorders",
            "Respiratory and Cough-Related Research",
            "Pathogenesis and Treatment of Hiccups"
          ]
        },
        {
          "openalex_id": "W2204649711",
          "year": 2002,
          "title": "A new Proposal of Voltage Variable Solid-state Laser Power Supply Adopted the Cockcroft-Walton circuit",
          "type": "article",
          "venue": "KIEE International Transactions on Electro-Physics and Application",
          "cited_by_count": 0,
          "topics": [
            "solar cell performance optimization",
            "Ocular and Laser Science Research",
            "Laser Material Processing Techniques"
          ]
        },
        {
          "openalex_id": "W1769846281",
          "year": 2004,
          "title": "The Effect of Increasing Blood Flow Rate on Dialysis Adequacy in Hemodialysis Patients with Low Kt/V",
          "type": "article",
          "venue": "Hemodialysis International",
          "cited_by_count": 21,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Central Venous Catheters and Hemodialysis"
          ]
        },
        {
          "openalex_id": "W1925215555",
          "year": 2004,
          "title": "The Microbe Removing Characteristics Caused by Dirty Water Using a Simple Pulsed Power System",
          "type": "article",
          "venue": "KIEE International Transactions on Electro-Physics and Application",
          "cited_by_count": 0,
          "topics": [
            "Microbial Inactivation Methods",
            "Magnetic and Electromagnetic Effects"
          ]
        },
        {
          "openalex_id": "W2095881982",
          "year": 2005,
          "title": "The effect of dialysis needle size on hemodialysis adequacy",
          "type": "article",
          "venue": "Hemodialysis International",
          "cited_by_count": 1,
          "topics": [
            "Central Venous Catheters and Hemodialysis",
            "Dialysis and Renal Disease Management",
            "Vascular Procedures and Complications"
          ]
        },
        {
          "openalex_id": "W2973217118",
          "year": 2019,
          "title": "ERS guidelines on the diagnosis and treatment of chronic cough in adults and children",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 881,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Asthma and respiratory diseases",
            "Gastroesophageal reflux and treatments"
          ]
        },
        {
          "openalex_id": "W1977367528",
          "year": 2015,
          "title": "The global epidemiology of chronic cough in adults: a systematic review and meta-analysis",
          "type": "review",
          "venue": "European Respiratory Journal",
          "cited_by_count": 584,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Asthma and respiratory diseases",
            "Pediatric health and respiratory diseases"
          ]
        },
        {
          "openalex_id": "W3155354002",
          "year": 2021,
          "title": "Confronting COVID-19-associated cough and the post-COVID syndrome: role of viral neurotropism, neuroinflammation, and neuroimmune responses",
          "type": "article",
          "venue": "The Lancet Respiratory Medicine",
          "cited_by_count": 379,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes",
            "Pathogenesis and Treatment of Hiccups"
          ]
        },
        {
          "openalex_id": "W3096206487",
          "year": 2020,
          "title": "Adult chronic rhinosinusitis",
          "type": "article",
          "venue": "Nature Reviews Disease Primers",
          "cited_by_count": 318,
          "topics": [
            "Sinusitis and nasal conditions",
            "Allergic Rhinitis and Sensitization",
            "Nasal Surgery and Airway Studies"
          ]
        },
        {
          "openalex_id": "W4283722066",
          "year": 2022,
          "title": "Cough hypersensitivity and chronic cough",
          "type": "article",
          "venue": "Nature Reviews Disease Primers",
          "cited_by_count": 300,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Asthma and respiratory diseases",
            "Ion Channels and Receptors"
          ]
        },
        {
          "openalex_id": "W2146630627",
          "year": 2014,
          "title": "A worldwide survey of chronic cough: a manifestation of enhanced somatosensory response",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 284,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Asthma and respiratory diseases",
            "Gastroesophageal reflux and treatments"
          ]
        },
        {
          "openalex_id": "W2039049647",
          "year": 2011,
          "title": "Carbamazepine-induced severe cutaneous adverse reactions and HLA genotypes in Koreans",
          "type": "article",
          "venue": "Epilepsy Research",
          "cited_by_count": 260,
          "topics": [
            "Drug-Induced Adverse Reactions",
            "Pharmacovigilance and Adverse Drug Reactions",
            "Contact Dermatitis and Allergies"
          ]
        },
        {
          "openalex_id": "W3127614400",
          "year": 2021,
          "title": "European Respiratory Society guidelines for the management of children and adolescents with bronchiectasis",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 226,
          "topics": [
            "Cystic Fibrosis Research Advances",
            "Tracheal and airway disorders",
            "Neonatal Respiratory Health Research"
          ]
        }
      ]
    }
  }
]
