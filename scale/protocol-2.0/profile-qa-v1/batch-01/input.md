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
    "name": "Aaron Winn",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2349-BT",
        "title": "Validation of the EQ-5D-5L Breathing Bolt-On: Longitudinal Evidence from a Large Randomized Controlled Trial",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5066367734",
      "display_name": "Aaron N. Winn",
      "orcid": "0000-0003-2906-3913",
      "reported_affiliation": "University of Illinois Chicago",
      "works_count": 177,
      "top_topics": [
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 38
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 27
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 27
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 17
        },
        {
          "topic": "Chronic Myeloid Leukemia Treatments",
          "works": 14
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 11
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 11
        },
        {
          "topic": "Pharmaceutical industry and healthcare",
          "works": 10
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 9
        },
        {
          "topic": "Opioid Use Disorder Treatment",
          "works": 9
        },
        {
          "topic": "Pain Management and Opioid Use",
          "works": 9
        },
        {
          "topic": "Chronic Lymphocytic Leukemia Research",
          "works": 8
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Stacie B. Dusetzina",
          "works": 30
        },
        {
          "name": "Joan Neuner",
          "works": 22
        },
        {
          "name": "Joshua T. Cohen",
          "works": 18
        },
        {
          "name": "Nicole Fergestrom",
          "works": 18
        },
        {
          "name": "Pei‐Jung Lin",
          "works": 17
        },
        {
          "name": "Peter J. Neumann",
          "works": 16
        },
        {
          "name": "Aaron Philip Mitchell",
          "works": 16
        },
        {
          "name": "Elbert S. Huang",
          "works": 15
        },
        {
          "name": "Susan K. Parsons",
          "works": 15
        },
        {
          "name": "Neda Laiteerapong",
          "works": 12
        },
        {
          "name": "Gunjan L. Shah",
          "works": 12
        },
        {
          "name": "Purushottam W. Laud",
          "works": 11
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7162579464",
          "year": 2026,
          "title": "Association of drug industry payments to oncologists and use of guideline-preferred cancer treatments.",
          "type": "conference-abstract",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Medication Adherence and Compliance",
            "Advanced Breast Cancer Therapies"
          ]
        },
        {
          "openalex_id": "W7154030794",
          "year": 2026,
          "title": "Follow-Up Patterns at a Low-Threshold Mobile Medical Unit Providing Opioid Use Disorder Care in an Urban Setting: A Group-Based Trajectory Modeling Approach",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Opioid Use Disorder Treatment",
            "Substance Abuse Treatment and Outcomes",
            "HIV, Drug Use, Sexual Risk"
          ]
        },
        {
          "openalex_id": "W7166160794",
          "year": 2026,
          "title": "P11 TRENDS IN OUT-OF-POCKET SPENDINGFOR MEDICATIONAMONG INDIVIDUALS WITH DIABETES: EVIDENCE FROM MEPS, 2013-2023",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Education",
            "Diabetes Management and Research",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W7166078781",
          "year": 2026,
          "title": "P59 GROWTH IN PRIVATE-PAYER MARKUPS FOR INFUSED CHEMOTHERAPY RELATIVE TO MEDICARE AVERAGE SALES PRICE BY SITE OF CARE, 2015-2023",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Advances in Oncology and Radiotherapy",
            "Neutropenia and Cancer Infections"
          ]
        },
        {
          "openalex_id": "W7166153614",
          "year": 2026,
          "title": "PCR156 IS HEALTH LITERACY ASSOCIATED WITH DIFFICULTY UNDERSTANDING AND COMPLETING HEALTH STATE VALUATION TASKS?",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "BRCA gene mutations in cancer",
            "Molecular Biology Techniques and Applications",
            "Forensic and Genetic Research"
          ]
        },
        {
          "openalex_id": "W7166028689",
          "year": 2026,
          "title": "PCR203 COMPARING HEALTH, HEALTH AND WELLBEING (HWB), AND QUALITY OF LIFE (QOL) VISUAL ANALOGUE SCALE (VAS) CONSTRUCTS WITH THE EQ-HWB-9 IN THE UNITED STATES (US), UNITED KINGDOM (UK), AND GERMANY",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Molecular Biology Techniques and Applications",
            "Forensic and Genetic Research",
            "Gene expression and cancer classification"
          ]
        },
        {
          "openalex_id": "W2061129666",
          "year": 2010,
          "title": "A fat lot of good. An 8 year longitudinal investigation of fat intakes in a paediatric CF population",
          "type": "article",
          "venue": "Journal of Cystic Fibrosis",
          "cited_by_count": 0,
          "topics": [
            "Child Nutrition and Feeding Issues",
            "Child and Adolescent Health",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W2116215834",
          "year": 2010,
          "title": "The Cost-Effectiveness of Continuous Glucose Monitoring in Type 1 Diabetes",
          "type": "article",
          "venue": "Diabetes Care",
          "cited_by_count": 119,
          "topics": [
            "Diabetes Management and Research",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes and associated disorders"
          ]
        },
        {
          "openalex_id": "W2171799035",
          "year": 2011,
          "title": "A fat lot of good: Balance and trends in fat intake in children with cystic fibrosis",
          "type": "article",
          "venue": "Journal of Cystic Fibrosis",
          "cited_by_count": 38,
          "topics": [
            "Cystic Fibrosis Research Advances",
            "Child Nutrition and Feeding Issues",
            "Lymphatic Disorders and Treatments"
          ]
        },
        {
          "openalex_id": "W2004627960",
          "year": 2011,
          "title": "Health Utilities for Children and Adults With Type 1 Diabetes",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 43,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Research",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2140974115",
          "year": 2013,
          "title": "Cost Sharing and Adherence to Tyrosine Kinase Inhibitors for Patients With Chronic Myeloid Leukemia",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 499,
          "topics": [
            "Chronic Myeloid Leukemia Treatments",
            "Medication Adherence and Compliance",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2115659841",
          "year": 2013,
          "title": "Cost-Effectiveness of MODY Genetic Testing: Translating Genomic Advances Into Practical Health Applications",
          "type": "article",
          "venue": "Diabetes Care",
          "cited_by_count": 137,
          "topics": [
            "Diabetes Treatment and Management",
            "Genomics and Rare Diseases",
            "Pancreatic function and diabetes"
          ]
        },
        {
          "openalex_id": "W2798025593",
          "year": 2018,
          "title": "Cost-effectiveness of Continuous Glucose Monitoring for Adults With Type 1 Diabetes Compared With Self-Monitoring of Blood Glucose: The DIAMOND Randomized Trial",
          "type": "article",
          "venue": "Diabetes Care",
          "cited_by_count": 120,
          "topics": [
            "Diabetes Management and Research",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Pancreatic function and diabetes"
          ]
        },
        {
          "openalex_id": "W2529061634",
          "year": 2016,
          "title": "Factors Associated With Tyrosine Kinase Inhibitor Initiation and Adherence Among Medicare Beneficiaries With Chronic Myeloid Leukemia",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 118,
          "topics": [
            "Chronic Myeloid Leukemia Treatments",
            "Chronic Lymphocytic Leukemia Research",
            "Acute Lymphoblastic Leukemia research"
          ]
        },
        {
          "openalex_id": "W177304803",
          "year": 2015,
          "title": "Multiple chronic conditions in type 2 diabetes mellitus: prevalence and consequences.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 98,
          "topics": [
            "Chronic Disease Management Strategies",
            "Diabetes Management and Education",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W2103285808",
          "year": 2011,
          "title": "The Cost-Effectiveness of Personalized Genetic Medicine",
          "type": "article",
          "venue": "Diabetes Care",
          "cited_by_count": 86,
          "topics": [
            "Pancreatic function and diabetes",
            "Diabetes Management and Research",
            "Adolescent and Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W4300773139",
          "year": 2022,
          "title": "First-Line Therapy for Type 2 Diabetes With Sodium–Glucose Cotransporter-2 Inhibitors and Glucagon-Like Peptide-1 Receptor Agonists",
          "type": "article",
          "venue": "Annals of Internal Medicine",
          "cited_by_count": 82,
          "topics": [
            "Diabetes Treatment and Management",
            "Diabetes Management and Research",
            "Pancreatic function and diabetes"
          ]
        }
      ]
    }
  },
  {
    "name": "Abdelghafour MARFAK",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1411-VS",
        "title": "Valuing health‐related quality of life: An EQ‐5D‐5L value set for Morocco",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5024805890",
      "display_name": "Abdelghafour Marfak",
      "orcid": "0000-0002-4212-8438",
      "reported_affiliation": "National School of Architecture",
      "works_count": 78,
      "top_topics": [
        {
          "topic": "Simulation-Based Education in Healthcare",
          "works": 11
        },
        {
          "topic": "Phytochemicals and Antioxidant Activities",
          "works": 7
        },
        {
          "topic": "Free Radicals and Antioxidants",
          "works": 7
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 7
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 6
        },
        {
          "topic": "Artificial Intelligence in Healthcare and Education",
          "works": 5
        },
        {
          "topic": "Quality Function Deployment in Product Design",
          "works": 5
        },
        {
          "topic": "Maternal Mental Health During Pregnancy and Postpartum",
          "works": 4
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 4
        },
        {
          "topic": "Lymphoma Diagnosis and Treatment",
          "works": 3
        },
        {
          "topic": "Clinical Reasoning and Diagnostic Skills",
          "works": 3
        },
        {
          "topic": "Antioxidant Activity and Oxidative Stress",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Ibtissam Youlyouz‐Marfak",
          "works": 33
        },
        {
          "name": "Abderraouf Hilali",
          "works": 31
        },
        {
          "name": "Chakib Nejjari",
          "works": 30
        },
        {
          "name": "Elmadani Saad",
          "works": 27
        },
        {
          "name": "Amal Boutib",
          "works": 20
        },
        {
          "name": "Asmaa Azizi",
          "works": 20
        },
        {
          "name": "Mohamed Benfatah",
          "works": 12
        },
        {
          "name": "Doha Achak",
          "works": 12
        },
        {
          "name": "Samia Chergaoui",
          "works": 9
        },
        {
          "name": "Mohamed Taiebine",
          "works": 9
        },
        {
          "name": "Patrick Trouillas",
          "works": 7
        },
        {
          "name": "Claude-Alain Calliste",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7161786130",
          "year": 2026,
          "title": "A narrative review of literature on the neuropsychological screening and assessment of acquired neurogenic and cognitive-communication disorders in Moroccan adults",
          "type": "review",
          "venue": "Applied Neuropsychology Adult",
          "cited_by_count": 0,
          "topics": [
            "Language Development and Disorders",
            "Genomics and Rare Diseases",
            "Epilepsy research and treatment"
          ]
        },
        {
          "openalex_id": "W7164312926",
          "year": 2026,
          "title": "Alternatives Africaines : Analyse et Prospective",
          "type": "other",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7164378903",
          "year": 2026,
          "title": "Alternatives Africaines : Analyse et Prospective",
          "type": "other",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7161567025",
          "year": 2026,
          "title": "Assessing Health-Related Quality of Life (HRQoL) in Moroccan Infants and Young Children: Insights from the EQ-TIPS Instrument",
          "type": "article",
          "venue": "Journal of Child and Family Studies",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Infant Development and Preterm Care",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W7134841022",
          "year": 2026,
          "title": "Bridging the nutritional care gap: nurse-led education for potassium control in hemodialysis patients",
          "type": "article",
          "venue": "Frontiers in Nutrition",
          "cited_by_count": 0,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Potassium and Related Disorders",
            "Parathyroid Disorders and Treatments"
          ]
        },
        {
          "openalex_id": "W7164335596",
          "year": 2026,
          "title": "Enhancing clinical competencies through AI-assisted simulation: an african perspective",
          "type": "article",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": [
            "Simulation-Based Education in Healthcare",
            "Global Health and Surgery",
            "Artificial Intelligence in Healthcare and Education"
          ]
        },
        {
          "openalex_id": "W2072379206",
          "year": 2002,
          "title": "Antioxidant, anti-inflammatory and antiproliferative properties of sixteen water plant extracts used in the Limousin countryside as herbal teas",
          "type": "article",
          "venue": "Food Chemistry",
          "cited_by_count": 267,
          "topics": [
            "Phytochemicals and Antioxidant Activities",
            "Essential Oils and Antimicrobial Activity",
            "Natural product bioactivities and synthesis"
          ]
        },
        {
          "openalex_id": "W1994076068",
          "year": 2002,
          "title": "Radiolysis of Quercetin in Methanol Solution:  Observation of Depside Formation",
          "type": "article",
          "venue": "Journal of Agricultural and Food Chemistry",
          "cited_by_count": 33,
          "topics": [
            "Free Radicals and Antioxidants",
            "Phytochemicals and Antioxidant Activities",
            "Plant biochemistry and biosynthesis"
          ]
        },
        {
          "openalex_id": "W2038986354",
          "year": 2003,
          "title": "Mechanisms of Transformation of the Antioxidant Kaempferol into Depsides. Gamma-Radiolysis Study in Methanol and Ethanol",
          "type": "article",
          "venue": "Radiation Research",
          "cited_by_count": 15,
          "topics": [
            "Free Radicals and Antioxidants",
            "Phytochemicals and Antioxidant Activities",
            "Computational Drug Discovery Methods"
          ]
        },
        {
          "openalex_id": "W1559058370",
          "year": 2003,
          "title": "Radiolyse gamma des flavonoïdes : étude de leur réactivité avec les radicaux issus des alcools : formation de depsides",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 9,
          "topics": [
            "Phytochemicals and Antioxidant Activities",
            "Food Quality and Safety Studies",
            "Free Radicals and Antioxidants"
          ]
        },
        {
          "openalex_id": "W2115093629",
          "year": 2012,
          "title": "IGHV gene features and MYD88 L265P mutation separate the three marginal zone lymphoma entities and Waldenström macroglobulinemia/lymphoplasmacytic lymphomas",
          "type": "article",
          "venue": "Leukemia",
          "cited_by_count": 174,
          "topics": [
            "Chronic Lymphocytic Leukemia Research",
            "Lymphoma Diagnosis and Treatment",
            "Viral-associated cancers and disorders"
          ]
        },
        {
          "openalex_id": "W4289528274",
          "year": 2022,
          "title": "Quality of Life During Pregnancy from 2011 to 2021: Systematic Review",
          "type": "review",
          "venue": "International Journal of Women s Health",
          "cited_by_count": 72,
          "topics": [
            "Pregnancy-related medical research",
            "Pregnancy and Medication Impact",
            "Maternal Mental Health During Pregnancy and Postpartum"
          ]
        },
        {
          "openalex_id": "W3080777887",
          "year": 2020,
          "title": "Health-related quality of life and behavior-related lifestyle changes due to the COVID-19 home confinement: Dataset from a Moroccan sample",
          "type": "data-paper",
          "venue": "Data in Brief",
          "cited_by_count": 69,
          "topics": [
            "COVID-19 and Mental Health",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W2094191439",
          "year": 2004,
          "title": "A theoretical study of the conformational behavior and electronic structure of taxifolin correlated with the free radical-scavenging activity",
          "type": "article",
          "venue": "Food Chemistry",
          "cited_by_count": 66,
          "topics": [
            "Free Radicals and Antioxidants",
            "Antioxidant Activity and Oxidative Stress",
            "Phytochemicals and Antioxidant Activities"
          ]
        },
        {
          "openalex_id": "W4392246232",
          "year": 2024,
          "title": "Assessing the efficacy of ChatGPT as a virtual patient in nursing simulation training: A study on nursing students' experience",
          "type": "article",
          "venue": "Teaching and learning in nursing",
          "cited_by_count": 62,
          "topics": [
            "Artificial Intelligence in Healthcare and Education",
            "Simulation-Based Education in Healthcare",
            "COVID-19 diagnosis using AI"
          ]
        },
        {
          "openalex_id": "W4396708987",
          "year": 2024,
          "title": "Impact of artificial intelligence-enhanced debriefing on clinical skills development in nursing students: A comparative study",
          "type": "article",
          "venue": "Teaching and learning in nursing",
          "cited_by_count": 56,
          "topics": [
            "Simulation-Based Education in Healthcare",
            "Artificial Intelligence in Healthcare and Education",
            "Clinical Reasoning and Diagnostic Skills"
          ]
        },
        {
          "openalex_id": "W2068985535",
          "year": 2003,
          "title": "Reactivity of flavonoids with 1-hydroxyethyl radical: a γ-radiolysis study",
          "type": "article",
          "venue": "Biochimica et Biophysica Acta (BBA) - General Subjects",
          "cited_by_count": 43,
          "topics": [
            "Free Radicals and Antioxidants",
            "Phytochemicals and Antioxidant Activities",
            "Radiation Effects and Dosimetry"
          ]
        }
      ]
    }
  },
  {
    "name": "Abdulmuminu Isah",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2236-VS",
        "title": "Developing Quality Adjusted Life Years Value Set for Nigerian Youth Population",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5024575926",
      "display_name": "Abdulmuminu Isah",
      "orcid": "0000-0002-1349-6434",
      "reported_affiliation": "University of Nigeria",
      "works_count": 102,
      "top_topics": [
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 18
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 15
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 10
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 9
        },
        {
          "topic": "HIV/AIDS drug development and treatment",
          "works": 8
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Blood Pressure and Hypertension Studies",
          "works": 7
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 7
        },
        {
          "topic": "Mobile Health and mHealth Applications",
          "works": 6
        },
        {
          "topic": "Pharmaceutical studies and practices",
          "works": 6
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 6
        },
        {
          "topic": "Diverse Scientific Research Studies",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Blessing Onyinye Ukoha-Kalu",
          "works": 21
        },
        {
          "name": "Maxwell Ogochukwu Adibe",
          "works": 20
        },
        {
          "name": "Ezinwanne Jane Ugochukwu",
          "works": 14
        },
        {
          "name": "Chukwuemeka Michael Ubaka",
          "works": 13
        },
        {
          "name": "Chibueze Anosike",
          "works": 12
        },
        {
          "name": "Deborah Oyine Aluh",
          "works": 12
        },
        {
          "name": "Chukwuemeka Augustine Nwachuya",
          "works": 11
        },
        {
          "name": "Chinwe Victoria Ukwe",
          "works": 9
        },
        {
          "name": "Chinonyelum Emmanuel Agbo",
          "works": 8
        },
        {
          "name": "Uzochukwu Emmanuel Chima",
          "works": 8
        },
        {
          "name": "Mustapha Muhammed Abubakar",
          "works": 8
        },
        {
          "name": "Chigozie Gloria Anene‐Okeke",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7160717663",
          "year": 2026,
          "title": "Efficacy and Mechanisms of Tribulus terrestris in the Management of Erectile Dysfunction: A Systematic Review of Preclinical Studies",
          "type": "article",
          "venue": "Pharmacology and Toxicology of Natural Medicines (ISSN 2756-6838)",
          "cited_by_count": 0,
          "topics": [
            "Phytochemical Studies and Bioactivities",
            "Sexual function and dysfunction studies",
            "Medicinal Plant Extracts Effects"
          ]
        },
        {
          "openalex_id": "W7163892138",
          "year": 2026,
          "title": "Impact of Dolutegravir-based regimens on patient satisfaction and quality of life among people living with HIV: a systematic review and meta-analysis",
          "type": "article",
          "venue": "BMC Infectious Diseases",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV-related health complications and treatments",
            "HIV/AIDS drug development and treatment"
          ]
        },
        {
          "openalex_id": "W7160556141",
          "year": 2026,
          "title": "Leaving no child behind? developing zero-dose and under-immunized child archetypes to improve vaccine uptake in Nigeria",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 0,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "Immune responses and vaccinations",
            "Bacterial Infections and Vaccines"
          ]
        },
        {
          "openalex_id": "W7118411712",
          "year": 2026,
          "title": "Measuring health-related quality of life in Africa: a systematic review of validated disease-specific and generic measurement tools",
          "type": "review",
          "venue": "Frontiers in Psychology",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W4416057345",
          "year": 2025,
          "title": "(ID: 51) Barriers and facilitators to the provision of telemedicine in Nigeria: a systematic review",
          "type": "review",
          "venue": "International Journal of Pharmacy Practice",
          "cited_by_count": 0,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Mobile Health and mHealth Applications",
            "Global Health and Surgery"
          ]
        },
        {
          "openalex_id": "W7117469492",
          "year": 2025,
          "title": "A scoping review of mobile health for ART adherence in pregnant and breastfeeding women with HIV in sub-Saharan Africa: preferences, acceptability, and privacy concerns",
          "type": "article",
          "venue": "BMC Infectious Diseases",
          "cited_by_count": 2,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "Mobile Health and mHealth Applications",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W3141375544",
          "year": 2016,
          "title": "Evaluation of drug therapy problems among patients receiving care in National Orthopedic Hospital in Nigeria",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W2752205775",
          "year": 2017,
          "title": "Evaluation of Health Status of Type 2 Diabetes Outpatients Receiving Care in a Tertiary Hospital in Nigeria",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 14,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Primary Care and Health Outcomes",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2726974357",
          "year": 2017,
          "title": "Knowledge, Attitudes and Perceptions of Prostate Cancer among Male Staff of the University of Nigeria",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 23,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Prostate Cancer Diagnosis and Treatment",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W2891049722",
          "year": 2018,
          "title": "CLINICAL INTERVENTIONS UNDERTAKEN BY FINAL YEAR STUDENT PHARMACISTS ON ROUNDING TEAMS IN NIGERIA: A 3-YEAR CROSS-SECTIONAL EVALUATION",
          "type": "article",
          "venue": "International Journal of Pharmacy and Pharmaceutical Sciences",
          "cited_by_count": 2,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Pharmaceutical studies and practices",
            "Antibiotic Use and Resistance"
          ]
        },
        {
          "openalex_id": "W2792864849",
          "year": 2018,
          "title": "Prescribing pattern and antibiotic use for hospitalized children in a Northern Nigerian Teaching Hospital",
          "type": "article",
          "venue": "Annals of African Medicine",
          "cited_by_count": 49,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pharmaceutical studies and practices",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W4387136943",
          "year": 2023,
          "title": "Assessment of public knowledge and attitude toward antibiotics use and resistance: a community pharmacy-based survey",
          "type": "article",
          "venue": "Journal of Pharmaceutical Policy and Practice",
          "cited_by_count": 18,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pharmaceutical and Antibiotic Environmental Impacts",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W4411038165",
          "year": 2025,
          "title": "Students’ acceptance and use of generative AI in pharmacy education: international cross-sectional survey based on the extended unified theory of acceptance and use of technology",
          "type": "article",
          "venue": "International Journal of Clinical Pharmacy",
          "cited_by_count": 18,
          "topics": [
            "Artificial Intelligence in Healthcare and Education",
            "AI in Service Interactions",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W4385982503",
          "year": 2023,
          "title": "Effectiveness of Telepharmacy in Rural Communities in Africa: A Scoping Review",
          "type": "article",
          "venue": "Journal of Pharmacy Technology",
          "cited_by_count": 16,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Mobile Health and mHealth Applications",
            "Healthcare Systems and Technology"
          ]
        },
        {
          "openalex_id": "W4393547240",
          "year": 2024,
          "title": "Assessment of Academic Resilience and Its Associated Factors Among Pharmacy Students in Twelve Countries",
          "type": "article",
          "venue": "American Journal of Pharmaceutical Education",
          "cited_by_count": 15,
          "topics": [
            "Resilience and Mental Health",
            "Healthcare professionals’ stress and burnout",
            "Perfectionism, Procrastination, Anxiety Studies"
          ]
        },
        {
          "openalex_id": "W3027831507",
          "year": 2020,
          "title": "Development and validation of a questionnaire for evaluating knowledge of risk factors for teen depression among health care trainees of a Nigerian university",
          "type": "article",
          "venue": "Asia-Pacific Psychiatry",
          "cited_by_count": 15,
          "topics": [
            "Mental Health Treatment and Access",
            "Child and Adolescent Psychosocial and Emotional Development",
            "Problem Solving Skills Development"
          ]
        },
        {
          "openalex_id": "W2792608569",
          "year": 2018,
          "title": "Knowledge and practice of malaria prevention and management among non-medical students of university of Nigeria, Nsukka",
          "type": "article",
          "venue": "International Journal of Community Medicine and Public Health",
          "cited_by_count": 15,
          "topics": [
            "Malaria Research and Control",
            "Digital Imaging for Blood Diseases"
          ]
        }
      ]
    }
  },
  {
    "name": "Abdulrasheed Hassan Yusuf",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1731-VS",
        "title": "Valuing Health-related quality of life of Nigerians: A Value Set for the EQ-5D-5L.",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5138651068",
      "display_name": "Abdulrasheed Hassan Yusuf",
      "orcid": "",
      "reported_affiliation": "Mahidol University",
      "works_count": 1,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 1
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 1
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bello Usman Ardo",
          "works": 1
        },
        {
          "name": "Montarat Thavorncharoensap",
          "works": 1
        },
        {
          "name": "Bram Roudijk",
          "works": 1
        },
        {
          "name": "Fredrick Dermawan Purba",
          "works": 1
        },
        {
          "name": "Zhihao Yang",
          "works": 1
        },
        {
          "name": "Meixia Liao",
          "works": 1
        },
        {
          "name": "Usa Chaikledkaew",
          "works": 1
        },
        {
          "name": "Sitaporn Youngkong",
          "works": 1
        },
        {
          "name": "Ammarin Thakkinstian",
          "works": 1
        },
        {
          "name": "Yakubu Adole Agada-Amade",
          "works": 1
        },
        {
          "name": "Taiwo Gboluwaga Amole",
          "works": 1
        },
        {
          "name": "Mohammed Nasir Sambo",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164819429",
          "year": 2026,
          "title": "The EQ-5D-5L valuation study in Nigeria",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        }
      ]
    }
  },
  {
    "name": "Abeer Al Rabayah",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "60-VS",
        "title": "Generating an EQ-5D-3L value set for the Hashemite kingdom of Jordan",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5058964513",
      "display_name": "Abeer Al Rabayah",
      "orcid": "0000-0003-2952-9103",
      "reported_affiliation": "King Hussein Cancer Center",
      "works_count": 28,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 15
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 9
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 5
        },
        {
          "topic": "Biosimilars and Bioanalytical Methods",
          "works": 4
        },
        {
          "topic": "Quality and Safety in Healthcare",
          "works": 3
        },
        {
          "topic": "Neutropenia and Cancer Infections",
          "works": 3
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 3
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 2
        },
        {
          "topic": "Blood disorders and treatments",
          "works": 2
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 2
        },
        {
          "topic": "Global Health Workforce Issues",
          "works": 2
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Saad Jaddoua",
          "works": 10
        },
        {
          "name": "Razan Sawalha",
          "works": 7
        },
        {
          "name": "Lama Nazer",
          "works": 6
        },
        {
          "name": "Uwe Siebert",
          "works": 5
        },
        {
          "name": "Rawan Fawzi Al Froukh",
          "works": 5
        },
        {
          "name": "Sewar Salmany",
          "works": 4
        },
        {
          "name": "Suzan Hammoudeh",
          "works": 3
        },
        {
          "name": "Manal Rayyan",
          "works": 3
        },
        {
          "name": "Rawan Al Froukh",
          "works": 3
        },
        {
          "name": "Khader Al-Habash",
          "works": 3
        },
        {
          "name": "Ahmad Nader Fasseeh",
          "works": 2
        },
        {
          "name": "Rita Karam",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4414162443",
          "year": 2025,
          "title": "Description and outcomes of a hospital-based pharmacovigilance system at a comprehensive cancer centre in Jordan",
          "type": "article",
          "venue": "Journal of Oncology Pharmacy Practice",
          "cited_by_count": 0,
          "topics": [
            "Pharmacovigilance and Adverse Drug Reactions",
            "Biosimilars and Bioanalytical Methods",
            "Drug-Induced Adverse Reactions"
          ]
        },
        {
          "openalex_id": "W4412444138",
          "year": 2025,
          "title": "EE213 Cost-Utility analysis of Dinutuximab Beta in Treating High-Risk Neuroblastoma: A Partitioned Survival Model Using R programming Language",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "Neuroblastoma Research and Treatments",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W4417481679",
          "year": 2025,
          "title": "EE338 Do Public Preferences Matter? Health-Economic Evaluation of Antineoplastic Medication Considering EQ-5D Value Sets From Several Countries",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Medication Adherence and Compliance",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4415871571",
          "year": 2025,
          "title": "Measuring health-related quality of life of patients with metastatic colorectal cancer using the Jordanian EQ-5D-3L value set: a cross-sectional observational study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 1,
          "topics": [
            "Colorectal Cancer Treatments and Studies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4412443539",
          "year": 2025,
          "title": "PCR1 Health-Related Quality of Life Research in Jordan: A Systematic Review of Published Studies",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Health Workforce Issues",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4412443791",
          "year": 2025,
          "title": "PT1 Developing a Budget Impact R Shiney Application to Assess the Financial Implications of Implementing Organized Cancer Screening Programs in Countries with Limited Resources: Breast Cancer as an Example",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2083801308",
          "year": 2012,
          "title": "PHP58 Data Disclosure an Ongoing Process Towards More Transparency",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical Quality and Counterfeiting"
          ]
        },
        {
          "openalex_id": "W2050884118",
          "year": 2013,
          "title": "Health Technology Assessment: Is It the Right Piece for the Jordanian Health Care Puzzle?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W2884081963",
          "year": 2018,
          "title": "A capacity-building programme in health technology assessment for hospital pharmacists in a low- to middle-income country",
          "type": "article",
          "venue": "Journal of Pharmaceutical Health Services Research",
          "cited_by_count": 6,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2905956412",
          "year": 2018,
          "title": "PCN32 - THE EFFECTIVENESS AND SAFETY OF SWITCHING FROM ORGINAL FILGRASTIM TO BIOSIMILAR FILGRASTIM IN PRIMARY PROPHYLAXIS OF CHEMOTHERAPY INDUCED FEBRILE NEUTROPENIA: A RETROSPECTIVE COHORT STUDY",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "Neutropenia and Cancer Infections",
            "Blood disorders and treatments"
          ]
        },
        {
          "openalex_id": "W3008935926",
          "year": 2020,
          "title": "Implementation of Health Technology Assessment in the Middle East and North Africa: Comparison Between the Current and Preferred Status",
          "type": "article",
          "venue": "Frontiers in Pharmacology",
          "cited_by_count": 73,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W3152879723",
          "year": 2021,
          "title": "Establishment and implementation of hospital-based health technology assessment at King Hussein Cancer Center: can our model be an example?",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 9,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W4402187925",
          "year": 2024,
          "title": "Valuation of the EQ-5D-3L in Jordan",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 9,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W3213561351",
          "year": 2021,
          "title": "Impact of a New Cost-Effectiveness Threshold Implementation on Cancer Formulary Decisions in Jordan",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4207073047",
          "year": 2022,
          "title": "Quality of Life of Family Caregivers of Critically Ill Patients With Cancer Before and After Intensive Care Unit Admission Measured by EQ-5D 3-Level: A Longitudinal Prospective Cohort Study",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 6,
          "topics": [
            "Family and Patient Care in Intensive Care Units",
            "Palliative Care and End-of-Life Issues",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W3144348297",
          "year": 2021,
          "title": "Oncology pharmacists’ response to COVID-19 pandemic in Jordan: The King Hussein Cancer Center experience",
          "type": "article",
          "venue": "Journal of Global Health",
          "cited_by_count": 5,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "COVID-19 Clinical Research Studies",
            "Antibiotic Use and Resistance"
          ]
        },
        {
          "openalex_id": "W4294919321",
          "year": 2022,
          "title": "Effectiveness and Safety of Filgrastim (Neupogen™) versus Filgrastim-aafi (Nivestim™) in Primary Prophylaxis of Chemotherapy-Induced Febrile Neutropenia: An Observational Cohort Study",
          "type": "article",
          "venue": "Drugs - Real World Outcomes",
          "cited_by_count": 4,
          "topics": [
            "Neutropenia and Cancer Infections",
            "Biosimilars and Bioanalytical Methods",
            "Blood disorders and treatments"
          ]
        }
      ]
    }
  }
]
