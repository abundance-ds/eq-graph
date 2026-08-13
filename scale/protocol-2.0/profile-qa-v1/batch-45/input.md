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
    "name": "Rosalie Viney",
    "member_affiliation": "University of Technology Sydney",
    "is_member": true,
    "projects": [
      {
        "project_id": "148-RA",
        "title": "Combining health and social outcomes using the EQ-5D-5L and the ASCOT – development of a pilot value set",
        "working_group": "Descriptive Systems, Valuation"
      },
      {
        "project_id": "2015360",
        "title": "Using DCE with duration to value EQ-5D-5L: Simplifying the task completion process",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016280",
        "title": "Valuing EQ-5D-5L in Australia: A comparison of the EQ-VT protocol and DCE with duration",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5076742980",
      "display_name": "Rosalie Viney",
      "orcid": "0000-0002-0039-9635",
      "reported_affiliation": "University of Technology Sydney",
      "works_count": 318,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 144
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 83
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 40
        },
        {
          "topic": "Global Health Care Issues",
          "works": 27
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 27
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 19
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 16
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 15
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 14
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 14
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 13
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 12
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Richard Norman",
          "works": 76
        },
        {
          "name": "Marion Haas",
          "works": 70
        },
        {
          "name": "Deborah J. Street",
          "works": 54
        },
        {
          "name": "Brendan Mulhern",
          "works": 47
        },
        {
          "name": "Madeleine King",
          "works": 39
        },
        {
          "name": "Stephen Goodall",
          "works": 27
        },
        {
          "name": "Jane Hall",
          "works": 26
        },
        {
          "name": "Nancy Devlin",
          "works": 23
        },
        {
          "name": "Kees Van Gool",
          "works": 22
        },
        {
          "name": "Denzil G. Fiebig",
          "works": 22
        },
        {
          "name": "John Brazier",
          "works": 21
        },
        {
          "name": "Julie Ratcliffe",
          "works": 20
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
          "openalex_id": "W7135188390",
          "year": 2026,
          "title": "Understanding how adults and adolescents value children's health states: a qualitative exploration using Discrete Choice Experiments (DCEs) with and without duration",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
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
          "openalex_id": "W4417443866",
          "year": 2025,
          "title": "Author Reply",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4416297506",
          "year": 2025,
          "title": "Design and implementation of data quality controls in the EQ-DAPHNIE study: insights from the pilot phase and 15-country analysis",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 3,
          "topics": [
            "Survey Methodology and Nonresponse",
            "Census and Population Estimation",
            "Data Quality and Management"
          ]
        },
        {
          "openalex_id": "W4238052759",
          "year": 1977,
          "title": "Whither private health insurance?",
          "type": "article",
          "venue": "Australian and New Zealand Journal of Public Health",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4256388239",
          "year": 1988,
          "title": "Book Reviews",
          "type": "book-review",
          "venue": "Journal of Industrial Relations",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W2007174926",
          "year": 1988,
          "title": "Book Reviews : A MATTER OF HOURS: WOMEN, PART-TIME WORK AND THE LABOUR MARKET By Veronica Beechey and Tessa Perkins. Polity Press, 1987, 212 pp., $29.95 (paperback)",
          "type": "book-review",
          "venue": "Journal of Industrial Relations",
          "cited_by_count": 0,
          "topics": [
            "Labor Movements and Unions",
            "Digital Economy and Work Transformation"
          ]
        },
        {
          "openalex_id": "W2596895977",
          "year": 1989,
          "title": "Sex discrimination in wages in the Tasmanian labour market",
          "type": "dissertation",
          "venue": "UTAS Research Repository",
          "cited_by_count": 0,
          "topics": [
            "Labor Movements and Unions",
            "Labor market dynamics and wage inequality",
            "Digital Economy and Work Transformation"
          ]
        },
        {
          "openalex_id": "W2762997972",
          "year": 2017,
          "title": "Incidence and severity of self-reported chemotherapy side effects in routine care: A prospective cohort study",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 533,
          "topics": [
            "Nausea and vomiting management",
            "Cancer Treatment and Pharmacology",
            "Pain Management and Opioid Use"
          ]
        },
        {
          "openalex_id": "W1993655814",
          "year": 2011,
          "title": "Time Trade-Off Derived EQ-5D Weights for Australia",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 267,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2065207814",
          "year": 2002,
          "title": "Discrete choice experiments to measure consumer preferences for health and healthcare",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 266,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2025330974",
          "year": 2013,
          "title": "A Pilot Discrete Choice Experiment to Explore Preferences for EQ-5D-5L Health States",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 211,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W1990045668",
          "year": 2004,
          "title": "Randomized Controlled Trial of the Role of Positron Emission Tomography in the Management of Stage I and II Non-Small-Cell Lung Cancer",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 198,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Lung Cancer Research Studies",
            "Radiomics and Machine Learning in Medical Imaging"
          ]
        },
        {
          "openalex_id": "W2147489204",
          "year": 2007,
          "title": "Quality of Life and Survival in the 2 Years After Surgery for Non–Small-Cell Lung Cancer",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 190,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Cancer survivorship and care",
            "Lung Cancer Treatments and Mutations"
          ]
        },
        {
          "openalex_id": "W2126411471",
          "year": 2002,
          "title": "Using stated preference discrete choice modelling to evaluate the introduction of varicella vaccination",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 189,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2041731719",
          "year": 2009,
          "title": "International Comparisons in Valuing EQ-5D Health States: A Review and Analysis",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 176,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        }
      ]
    }
  },
  {
    "name": "Ruixuan Jiang",
    "member_affiliation": "Merck & Co., Inc.,",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5049026946",
      "display_name": "Ruixuan Jiang",
      "orcid": "0000-0003-1737-2989",
      "reported_affiliation": "Merck & Co., Inc., Rahway, NJ, USA (United States)",
      "works_count": 60,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 23
        },
        {
          "topic": "Cutaneous Melanoma Detection and Management",
          "works": 16
        },
        {
          "topic": "Cancer Immunotherapy and Biomarkers",
          "works": 12
        },
        {
          "topic": "Melanoma and MAPK Pathways",
          "works": 7
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 5
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 5
        },
        {
          "topic": "CAR-T cell therapy research",
          "works": 5
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 3
        },
        {
          "topic": "Chronic Myeloid Leukemia Treatments",
          "works": 3
        },
        {
          "topic": "Brain Metastases and Treatment",
          "works": 3
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 3
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "A. Simon Pickard",
          "works": 17
        },
        {
          "name": "Clemens Krepler",
          "works": 11
        },
        {
          "name": "Mizuho Fukunaga‐Kalabis",
          "works": 7
        },
        {
          "name": "Shujing Zhang",
          "works": 6
        },
        {
          "name": "Todd A. Lee",
          "works": 6
        },
        {
          "name": "Emilie Scherrer",
          "works": 6
        },
        {
          "name": "Thomas Kohlmann",
          "works": 5
        },
        {
          "name": "Irene M. Shui",
          "works": 5
        },
        {
          "name": "Ernest H. Law",
          "works": 4
        },
        {
          "name": "James W. Shaw",
          "works": 4
        },
        {
          "name": "Axel Mühlbacher",
          "works": 4
        },
        {
          "name": "Xiang‐Lin Tan",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7170136085",
          "year": 2026,
          "title": "Real-world treatment patterns in stage III and IV melanoma patients: insights from a global multi-center chart review study",
          "type": "article",
          "venue": "Frontiers in Immunology",
          "cited_by_count": 0,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Cutaneous Melanoma Detection and Management",
            "Melanoma and MAPK Pathways"
          ]
        },
        {
          "openalex_id": "W7133675335",
          "year": 2026,
          "title": "Resistance to anti-PD-1 immunotherapy for stage III and IV melanoma: a global chart review study",
          "type": "article",
          "venue": "Journal for ImmunoTherapy of Cancer",
          "cited_by_count": 2,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Cutaneous Melanoma Detection and Management",
            "Immunotherapy and Immune Responses"
          ]
        },
        {
          "openalex_id": "W7171934061",
          "year": 2026,
          "title": "Subglacial Radar Reflectivity Estimation Considering Volumetric Scattering Loss from Englacial Dielectric Inhomogeneities",
          "type": "dataset",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7171968016",
          "year": 2026,
          "title": "Subglacial Radar Reflectivity Estimation Considering Volumetric Scattering Loss from Englacial Dielectric Inhomogeneities",
          "type": "dataset",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4409624676",
          "year": 2025,
          "title": "Abstract 2302: Overall survival and treatment patterns in elderly patients with stage IV colorectal cancer in the United States: SEER-medicare analysis, 2007-2020",
          "type": "conference-abstract",
          "venue": "Cancer Research",
          "cited_by_count": 0,
          "topics": [
            "Colorectal Cancer Treatments and Studies",
            "Colorectal Cancer Surgical Treatments"
          ]
        },
        {
          "openalex_id": "W4412442993",
          "year": 2025,
          "title": "EE389 Cost-Effectiveness of Pembrolizumab as First-Line Treatment for Patients with Microsatellite Instability High (MSI-H) or Mismatch Repair Deficient (dMMR) Unresectable or Metastatic Colorectal Cancer (CRC) from Public Payer Perspective in Brazil",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2471541538",
          "year": 2000,
          "title": "[Treatment of acute lymphoblastic leukemia by autologous stem cell transplantation: an analysis of 30 cases].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": []
        },
        {
          "openalex_id": "W2161452781",
          "year": 2004,
          "title": "Selenium and Colorectal Adenoma: Results of a Pooled Analysis",
          "type": "article",
          "venue": "JNCI Journal of the National Cancer Institute",
          "cited_by_count": 157,
          "topics": [
            "Selenium in Biological Systems",
            "Colorectal Cancer Screening and Detection",
            "Heavy Metals in Plants"
          ]
        },
        {
          "openalex_id": "W2588523631",
          "year": 2006,
          "title": "Aspirin Use and Gender Difference in Adenoma Recurrence",
          "type": "conference-abstract",
          "venue": "American Journal of Epidemiology",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory mediators and NSAID effects",
            "Helicobacter pylori-related gastroenterology studies",
            "Estrogen and related hormone effects"
          ]
        },
        {
          "openalex_id": "W2589023494",
          "year": 2006,
          "title": "Interactions Between PPAR-GAMMA Genotypes and Traits of Metabolic Syndrome on Risk of Recurrence for Colorectal Adenomatous Polyps",
          "type": "conference-abstract",
          "venue": "American Journal of Epidemiology",
          "cited_by_count": 0,
          "topics": [
            "Digestive system and related health",
            "Genetic factors in colorectal cancer",
            "Metabolism, Diabetes, and Cancer"
          ]
        },
        {
          "openalex_id": "W2945409099",
          "year": 2019,
          "title": "United States Valuation of EQ-5D-5L Health States Using an International Protocol",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 399,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W3092636925",
          "year": 2020,
          "title": "US population norms for the EQ-5D-5L and comparison of norms from face-to-face and online samples",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 233,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2617153145",
          "year": 2017,
          "title": "The societal cost of heroin use disorder in the United States",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 66,
          "topics": [
            "Opioid Use Disorder Treatment",
            "HIV, Drug Use, Sexual Risk",
            "Prenatal Substance Exposure Effects"
          ]
        },
        {
          "openalex_id": "W3182459736",
          "year": 2021,
          "title": "Combining EQ-5D-5L items into a level summary score: demonstrating feasibility using non-parametric item response theory using an international dataset",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 46,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W2325381503",
          "year": 2016,
          "title": "Using Patient-reported Outcomes to Compare Relative Burden of Cancer: EQ-5D and Functional Assessment of Cancer Therapy-General in Eleven Types of Cancer",
          "type": "article",
          "venue": "Clinical Therapeutics",
          "cited_by_count": 44,
          "topics": [
            "Cancer survivorship and care",
            "Economic and Financial Impacts of Cancer",
            "Cancer Treatment and Pharmacology"
          ]
        },
        {
          "openalex_id": "W2599491691",
          "year": 2017,
          "title": "Healthcare Resource Use, Costs, and Disease Progression Associated with Diabetic Nephropathy in Adults with Type 2 Diabetes: A Retrospective Observational Study",
          "type": "article",
          "venue": "Diabetes Therapy",
          "cited_by_count": 41,
          "topics": [
            "Chronic Kidney Disease and Diabetes",
            "Diabetes Treatment and Management",
            "Acute Kidney Injury Research"
          ]
        },
        {
          "openalex_id": "W3108716902",
          "year": 2020,
          "title": "Comparison of online and face-to-face valuation of the EQ-5D-5L using composite time trade-off",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 38,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Frailty in Older Adults",
            "Patient-Provider Communication in Healthcare"
          ]
        }
      ]
    }
  },
  {
    "name": "Sander van Kuijk",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1569-RA",
        "title": "The long CORona Follow-Up Study (long CORFU): long-term outcomes and health-related quality of life of long COVID patients",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "1983-PHD",
        "title": "Retrospective measurement of EQ-5D-5L and bolt-ons: a study on recall bias among patients with post COVID-19 condition.",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "2368-RA",
        "title": "Dutch translation of breathing, sleep, fatigue and cognition EQ-5D Bolt-on Toolbox items",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5087173002",
      "display_name": "Sander M. J. van Kuijk",
      "orcid": "0000-0003-2796-729X",
      "reported_affiliation": "Maastricht University Medical Centre",
      "works_count": 666,
      "top_topics": [
        {
          "topic": "Pregnancy and preeclampsia studies",
          "works": 69
        },
        {
          "topic": "Breast Implant and Reconstruction",
          "works": 43
        },
        {
          "topic": "Reconstructive Surgery and Microvascular Techniques",
          "works": 42
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 27
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 26
        },
        {
          "topic": "Pelvic floor disorders treatments",
          "works": 26
        },
        {
          "topic": "Pain Mechanisms and Treatments",
          "works": 24
        },
        {
          "topic": "Cardiovascular Issues in Pregnancy",
          "works": 24
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 24
        },
        {
          "topic": "Gestational Diabetes Research and Management",
          "works": 23
        },
        {
          "topic": "Maternal and Perinatal Health Interventions",
          "works": 23
        },
        {
          "topic": "Sepsis Diagnosis and Treatment",
          "works": 23
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Marc E. A. Spaanderman",
          "works": 52
        },
        {
          "name": "Chahinda Ghossein‐Doha",
          "works": 51
        },
        {
          "name": "Luc Smits",
          "works": 41
        },
        {
          "name": "René R. W. J. van der Hulst",
          "works": 37
        },
        {
          "name": "Iwan C.C. van der Horst",
          "works": 32
        },
        {
          "name": "Bas C. T. van Bussel",
          "works": 31
        },
        {
          "name": "Geerard L. Beets",
          "works": 24
        },
        {
          "name": "Carmen D. Dirksen",
          "works": 24
        },
        {
          "name": "Hubertina Scheepers",
          "works": 24
        },
        {
          "name": "Wolfgang Bühre",
          "works": 24
        },
        {
          "name": "Stéphanie O. Breukink",
          "works": 23
        },
        {
          "name": "Kevin Vernooy",
          "works": 22
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7160058866",
          "year": 2026,
          "title": "Comparing the performance of three software programmes for manual and (semi-)automatic liver volumetry",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Organ Transplantation Techniques and Outcomes",
            "Amoebic Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W7138197763",
          "year": 2026,
          "title": "Improving Health Care with Clinical Prediction Models",
          "type": "book",
          "venue": "Maastricht University Press eBooks",
          "cited_by_count": 0,
          "topics": [
            "Machine Learning in Healthcare",
            "Artificial Intelligence in Healthcare and Education",
            "Artificial Intelligence in Healthcare"
          ]
        },
        {
          "openalex_id": "W7164872688",
          "year": 2026,
          "title": "Intravenous thrombolysis for ischemic stroke in the posterior circulation",
          "type": "article",
          "venue": "DiRROS repository (University of Maribor)",
          "cited_by_count": 0,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Intracerebral and Subarachnoid Hemorrhage Research",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W7169621165",
          "year": 2026,
          "title": "Multicentre prospective randomised controlled non-inferiority trial on the efficacy and safety of minimally invasive SAIF vertebral reconstruction technique versus spinal fixation in unstable osteoporotic vertebral compression fractures: a protocol",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Spinal Fractures and Fixation Techniques",
            "Bone health and osteoporosis research",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W7167514518",
          "year": 2026,
          "title": "Pain prevalence and intensity in advanced pancreatic cancer: a nationwide cohort study",
          "type": "article",
          "venue": "Pain",
          "cited_by_count": 0,
          "topics": [
            "Pain Management and Opioid Use",
            "Pancreatic and Hepatic Oncology Research",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W7168021786",
          "year": 2026,
          "title": "Perceived cognitive load among emergency department code blue teams: distribution, correlates and relationship with team performance",
          "type": "article",
          "venue": "Resuscitation",
          "cited_by_count": 0,
          "topics": [
            "Simulation-Based Education in Healthcare",
            "Cardiac Arrest and Resuscitation",
            "Patient Safety and Medication Errors"
          ]
        },
        {
          "openalex_id": "W3127385318",
          "year": 1986,
          "title": "Development of a PACS system at the University Hospital Brussels",
          "type": "article",
          "venue": "VUBIR (Vrije Universiteit Brussel)",
          "cited_by_count": 0,
          "topics": [
            "Digital Radiography and Breast Imaging",
            "Advanced X-ray and CT Imaging",
            "Dental Radiography and Imaging"
          ]
        },
        {
          "openalex_id": "W2127438621",
          "year": 2010,
          "title": "Cost-effectiveness of recurrence risk guided care versus care as usual in women who suffered from early-onset preeclampsia including HELLP syndrome in their previous pregnancy (the PreCare study)",
          "type": "article",
          "venue": "BMC Pregnancy and Childbirth",
          "cited_by_count": 9,
          "topics": [
            "Pregnancy and preeclampsia studies",
            "Birth, Development, and Health",
            "Cardiovascular Issues in Pregnancy"
          ]
        },
        {
          "openalex_id": "W1577004062",
          "year": 2010,
          "title": "How long do preconception risk prediction models hold? Influence of selective fertility on model performance",
          "type": "article",
          "venue": "Paediatric and Perinatal Epidemiology",
          "cited_by_count": 4,
          "topics": [
            "Pregnancy and preeclampsia studies",
            "Birth, Development, and Health",
            "Assisted Reproductive Technology and Twin Pregnancy"
          ]
        },
        {
          "openalex_id": "W1983955975",
          "year": 2011,
          "title": "326: Mode of delivery after previous cesarean section in the Netherlands",
          "type": "article",
          "venue": "American Journal of Obstetrics and Gynecology",
          "cited_by_count": 1,
          "topics": [
            "Pregnancy-related medical research",
            "Maternal and Perinatal Health Interventions",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W3014524604",
          "year": 2020,
          "title": "Prediction models for diagnosis and prognosis of covid-19: systematic review and critical appraisal",
          "type": "review",
          "venue": "BMJ",
          "cited_by_count": 3262,
          "topics": [
            "COVID-19 Clinical Research Studies",
            "COVID-19 diagnosis using AI",
            "SARS-CoV-2 detection and testing"
          ]
        },
        {
          "openalex_id": "W2673483870",
          "year": 2017,
          "title": "Transforaminal lumbar interbody fusion (TLIF) versus posterior lumbar interbody fusion (PLIF) in lumbar spondylolisthesis: a systematic review and meta-analysis",
          "type": "review",
          "venue": "The Spine Journal",
          "cited_by_count": 306,
          "topics": [
            "Spine and Intervertebral Disc Pathology",
            "Cervical and Thoracic Myelopathy",
            "Spondyloarthritis Studies and Treatments"
          ]
        },
        {
          "openalex_id": "W2549778034",
          "year": 2016,
          "title": "Physiological adaptation of maternal plasma volume during pregnancy: a systematic review and meta-analysis",
          "type": "review",
          "venue": "Ultrasound in Obstetrics and Gynecology",
          "cited_by_count": 271,
          "topics": [
            "Pregnancy and preeclampsia studies",
            "Gestational Diabetes Research and Management",
            "Maternal and fetal healthcare"
          ]
        },
        {
          "openalex_id": "W3195714029",
          "year": 2021,
          "title": "Targeting Autoregulation-Guided Cerebral Perfusion Pressure after Traumatic Brain Injury (COGiTATE): A Feasibility Randomized Controlled Clinical Trial",
          "type": "article",
          "venue": "Journal of Neurotrauma",
          "cited_by_count": 226,
          "topics": [
            "Traumatic Brain Injury and Neurovascular Disturbances",
            "Cerebrospinal fluid and hydrocephalus",
            "Cardiac Arrest and Resuscitation"
          ]
        },
        {
          "openalex_id": "W2945447987",
          "year": 2019,
          "title": "Does three‐dimensional anatomy improve student understanding?",
          "type": "article",
          "venue": "Clinical Anatomy",
          "cited_by_count": 199,
          "topics": [
            "Anatomy and Medical Technology",
            "Surgical Simulation and Training",
            "Innovations in Medical Education"
          ]
        },
        {
          "openalex_id": "W4401598369",
          "year": 2024,
          "title": "Effect of high versus standard protein provision on functional recovery in people with critical illness (PRECISe): an investigator-initiated, double-blinded, multicentre, parallel-group, randomised controlled trial in Belgium and the Netherlands",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 136,
          "topics": [
            "Clinical Nutrition and Gastroenterology",
            "Nutrition and Health in Aging",
            "Enhanced Recovery After Surgery"
          ]
        },
        {
          "openalex_id": "W4361285058",
          "year": 2023,
          "title": "Long-term Quality of Life and Functional Outcome of Patients With Rectal Cancer Following a Watch-and-Wait Approach",
          "type": "article",
          "venue": "JAMA Surgery",
          "cited_by_count": 134,
          "topics": [
            "Colorectal Cancer Surgical Treatments",
            "Prostate Cancer Diagnosis and Treatment",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2895299813",
          "year": 2018,
          "title": "Maternal kidney function during pregnancy: systematic review and meta‐analysis",
          "type": "review",
          "venue": "Ultrasound in Obstetrics and Gynecology",
          "cited_by_count": 130,
          "topics": [
            "Pregnancy and Medication Impact",
            "Pregnancy and preeclampsia studies",
            "Birth, Development, and Health"
          ]
        }
      ]
    }
  },
  {
    "name": "Sarah Derrett",
    "member_affiliation": "University of Otago",
    "is_member": true,
    "projects": [
      {
        "project_id": "1543-RA",
        "title": "VMC proposal for developmental work to support development of gender neutral language in the EuroQol suite of measures",
        "working_group": "Others"
      },
      {
        "project_id": "1812-PHD",
        "title": "Assessing the health-related quality of life of adolescents in Ethiopia: Mixed method study (quantitative and qualitative)",
        "working_group": "Populations and Health Systems, Youth"
      },
      {
        "project_id": "2014190",
        "title": "Understanding relationships between the EQ-5D and Personal Well-being",
        "working_group": "Others"
      },
      {
        "project_id": "2015170",
        "title": "Monitoring neurotrauma patient outcomes in Bandung, Indonesia: A feasibility study",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2229-TR",
        "title": "Seeking an Improved Modular Layout for EuroQol Instruments (SIMPLE): Streamlining and future-proofing version management",
        "working_group": "Others"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5021576811",
      "display_name": "Sarah Derrett",
      "orcid": "0000-0003-2867-0498",
      "reported_affiliation": "University of Otago",
      "works_count": 237,
      "top_topics": [
        {
          "topic": "Trauma and Emergency Care Studies",
          "works": 73
        },
        {
          "topic": "Injury Epidemiology and Prevention",
          "works": 66
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 35
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 27
        },
        {
          "topic": "Traumatic Brain Injury Research",
          "works": 24
        },
        {
          "topic": "Occupational Health and Safety Research",
          "works": 18
        },
        {
          "topic": "Traffic and Road Safety",
          "works": 16
        },
        {
          "topic": "Spinal Cord Injury Research",
          "works": 15
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 15
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 12
        },
        {
          "topic": "Mental Health and Patient Involvement",
          "works": 11
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 10
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Emma Wyeth",
          "works": 82
        },
        {
          "name": "Ari Samaranayaka",
          "works": 48
        },
        {
          "name": "Gabrielle Davie",
          "works": 46
        },
        {
          "name": "Helen Harcombe",
          "works": 37
        },
        {
          "name": "Shanthi Ameratunga",
          "works": 28
        },
        {
          "name": "Rebbecca Lilley",
          "works": 21
        },
        {
          "name": "David McBride",
          "works": 18
        },
        {
          "name": "Peter Herbison",
          "works": 18
        },
        {
          "name": "Amy Richardson",
          "works": 18
        },
        {
          "name": "John Langley",
          "works": 16
        },
        {
          "name": "Belinda J. Gabbe",
          "works": 15
        },
        {
          "name": "Trudy Sullivan",
          "works": 15
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7128304736",
          "year": 2026,
          "title": "<b>Protocol for Assessing Content Validity in Generic Preference-weighted Measures: A Scoping Review</b>",
          "type": "other",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7128313152",
          "year": 2026,
          "title": "<b>Protocol for Assessing Content Validity in Generic Preference-weighted Measures: A Scoping Review</b>",
          "type": "other",
          "venue": "ORDA - The University of Sheffield Research Data Catalogue and Repository",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7127951922",
          "year": 2026,
          "title": "Experiences of Racial Discrimination: Qualitative Findings from Injured New Zealand Migrants",
          "type": "article",
          "venue": "Journal of Immigrant and Minority Health",
          "cited_by_count": 0,
          "topics": [
            "Athletic Training and Education",
            "Migration, Health and Trauma",
            "Indigenous Health, Education, and Rights"
          ]
        },
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
          "openalex_id": "W7153209181",
          "year": 2026,
          "title": "Integrated Care Within New Zealand’s Specialist Mental Health and Addiction Services: Qualitative Research to Inform a New Model",
          "type": "article",
          "venue": "Community Mental Health Journal",
          "cited_by_count": 0,
          "topics": [
            "Mental Health and Patient Involvement",
            "Mental Health Treatment and Access",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W7133136805",
          "year": 2026,
          "title": "Transcultural translation and adaptation of EuroQol’s EQ-5D-5L for Nepal: process description and recommendations for an interpretation guide",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W2159020201",
          "year": 1999,
          "title": "Waiting for elective surgery: effects on health-related quality of life",
          "type": "article",
          "venue": "International Journal for Quality in Health Care",
          "cited_by_count": 140,
          "topics": [
            "Healthcare Operations and Scheduling Optimization",
            "Patient Satisfaction in Healthcare",
            "Prostate Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2089479510",
          "year": 2000,
          "title": "Solving the surgical waiting list problem? New Zealand's ‘booking system’",
          "type": "article",
          "venue": "The International Journal of Health Planning and Management",
          "cited_by_count": 60,
          "topics": [
            "Healthcare Policy and Management",
            "Healthcare Operations and Scheduling Optimization",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W123392214",
          "year": 2001,
          "title": "Prospective evaluation of the effects of prostatectomy on symptoms and quality of life.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Urinary Bladder and Prostate Research",
            "Prostate Cancer Diagnosis and Treatment",
            "Urinary Tract Infections Management"
          ]
        },
        {
          "openalex_id": "W2421174704",
          "year": 2001,
          "title": "Surgical prioritisation and rationing: some recent changes.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 7,
          "topics": [
            "Medical Malpractice and Liability Issues"
          ]
        },
        {
          "openalex_id": "W2097950056",
          "year": 2012,
          "title": "Disability-adjusted life years (DALYs) for 291 diseases and injuries in 21 regions, 1990–2010: a systematic analysis for the Global Burden of Disease Study 2010",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 9025,
          "topics": [
            "Health disparities and outcomes",
            "Cerebral Palsy and Movement Disorders",
            "Injury Epidemiology and Prevention"
          ]
        },
        {
          "openalex_id": "W2108344016",
          "year": 2012,
          "title": "Years lived with disability (YLDs) for 1160 sequelae of 289 diseases and injuries 1990–2010: a systematic analysis for the Global Burden of Disease Study 2010",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 8424,
          "topics": [
            "Frailty in Older Adults",
            "Chronic Disease Management Strategies",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2527824850",
          "year": 2016,
          "title": "Global, regional, and national incidence, prevalence, and years lived with disability for 310 diseases and injuries, 1990–2015: a systematic analysis for the Global Burden of Disease Study 2015",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 7421,
          "topics": [
            "Injury Epidemiology and Prevention",
            "Global Public Health Policies and Epidemiology",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2098082628",
          "year": 2015,
          "title": "Global, regional, and national incidence, prevalence, and years lived with disability for 301 acute and chronic diseases and injuries in 188 countries, 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 6527,
          "topics": [
            "Chronic Disease Management Strategies",
            "Health disparities and outcomes",
            "Injury Epidemiology and Prevention"
          ]
        },
        {
          "openalex_id": "W3143437408",
          "year": 2015,
          "title": "Global, regional, and national comparative risk assessment of 79 behavioural, environmental and occupational, and metabolic risks or clusters of risks in 188 countries, 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 2758,
          "topics": [
            "Health, Environment, Cognitive Aging",
            "Air Quality and Health Impacts",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2142472354",
          "year": 2015,
          "title": "Global, regional, and national disability-adjusted life years (DALYs) for 306 diseases and injuries and healthy life expectancy (HALE) for 188 countries, 1990–2013: quantifying the epidemiological transition",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 2021,
          "topics": [
            "Health disparities and outcomes",
            "Insurance, Mortality, Demography, Risk Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2221016424",
          "year": 2015,
          "title": "The global burden of injury: incidence, mortality, disability-adjusted life years and time trends from the Global Burden of Disease study 2013",
          "type": "article",
          "venue": "Injury Prevention",
          "cited_by_count": 1342,
          "topics": [
            "Injury Epidemiology and Prevention",
            "Trauma and Emergency Care Studies",
            "Autopsy Techniques and Outcomes"
          ]
        },
        {
          "openalex_id": "W2508424442",
          "year": 2016,
          "title": "Measuring the health-related Sustainable Development Goals in 188 countries: a baseline analysis from the Global Burden of Disease Study 2015",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 628,
          "topics": [
            "Global Maternal and Child Health",
            "Human Rights and Development",
            "Child Nutrition and Water Access"
          ]
        }
      ]
    }
  },
  {
    "name": "Sarah Dewilde",
    "member_affiliation": "SHE",
    "is_member": true,
    "projects": [
      {
        "project_id": "124-VS",
        "title": "**Valuing the EQ-5D-Y-3L in Belgium using the new protocol**",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1601-RA",
        "title": "Testing the performance and psychometric properties of six bolt-ons in general population and patients with myasthenia gravis",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20180640",
        "title": "Insight into the higher health state valuation for children compared to adults: effect of 3 valuation methods",
        "working_group": "Youth"
      },
      {
        "project_id": "20180641",
        "title": "Insight into the higher health state valuation for children compared to adults: effect of 3 valuation methods. Request for budget extension",
        "working_group": "Youth"
      },
      {
        "project_id": "2167-RA",
        "title": "Comparing the psychometric performance of five energy- and sleep-related EQ-5D-5L bolt-ons in a multinational, longitudinal general population setting and their association with validated fatigue scales",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5043932217",
      "display_name": "Sarah Dewilde",
      "orcid": "0000-0002-7315-3230",
      "reported_affiliation": "Department of Health Services",
      "works_count": 85,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 19
        },
        {
          "topic": "Myasthenia Gravis and Thymoma",
          "works": 15
        },
        {
          "topic": "Acute Ischemic Stroke Management",
          "works": 12
        },
        {
          "topic": "Stroke Rehabilitation and Recovery",
          "works": 10
        },
        {
          "topic": "Adrenal Hormones and Disorders",
          "works": 9
        },
        {
          "topic": "Parkinson's Disease and Spinal Disorders",
          "works": 8
        },
        {
          "topic": "Fibromyalgia and Chronic Fatigue Syndrome Research",
          "works": 5
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 5
        },
        {
          "topic": "Peripheral Neuropathies and Disorders",
          "works": 5
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 3
        },
        {
          "topic": "Chemotherapy-induced cardiotoxicity and mitigation",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sandra Paci",
          "works": 17
        },
        {
          "name": "Glenn Phillips",
          "works": 15
        },
        {
          "name": "Andrew Lloyd",
          "works": 12
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 12
        },
        {
          "name": "Febe Brackx",
          "works": 12
        },
        {
          "name": "Vincent Thijs",
          "works": 11
        },
        {
          "name": "Lieven Annemans",
          "works": 10
        },
        {
          "name": "C. Arvin-Berod",
          "works": 10
        },
        {
          "name": "Nafthali Hananja Tollenaar",
          "works": 9
        },
        {
          "name": "Lucas Van de Veire",
          "works": 9
        },
        {
          "name": "Renato Mantegazza",
          "works": 6
        },
        {
          "name": "Jack Wright",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164206509",
          "year": 2026,
          "title": "Beyond Disability: The Burden of Fatigue in CIDP (P1-9.007)",
          "type": "article",
          "venue": "Neurology",
          "cited_by_count": 0,
          "topics": [
            "Adrenal Hormones and Disorders",
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Lower Extremity Biomechanics and Pathologies"
          ]
        },
        {
          "openalex_id": "W7135245548",
          "year": 2026,
          "title": "Estimating the minimal clinically important difference for the Myasthenia Gravis Quality of Life revised scale (MG-QOL15R)",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Myasthenia Gravis and Thymoma",
            "Adrenal Hormones and Disorders",
            "Parkinson's Disease and Spinal Disorders"
          ]
        },
        {
          "openalex_id": "W4409824929",
          "year": 2025,
          "title": "A cost analysis of reductions in work productivity for MG patients and their caregivers by symptom severity",
          "type": "article",
          "venue": "Frontiers in Public Health",
          "cited_by_count": 5,
          "topics": [
            "Myasthenia Gravis and Thymoma",
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Adrenal Hormones and Disorders"
          ]
        },
        {
          "openalex_id": "W4417482170",
          "year": 2025,
          "title": "CO80 Early Life Hypoglycemia and Neurological Sequalae in Children With Congenital Hyperinsulinism",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes Management and Research",
            "Growth Hormone and Insulin-like Growth Factors"
          ]
        },
        {
          "openalex_id": "W4411457731",
          "year": 2025,
          "title": "Caregiving burden among caregivers of people with myasthenia gravis",
          "type": "article",
          "venue": "Orphanet Journal of Rare Diseases",
          "cited_by_count": 5,
          "topics": [
            "Myasthenia Gravis and Thymoma",
            "Parkinson's Disease and Spinal Disorders",
            "Coagulation, Bradykinin, Polyphosphates, and Angioedema"
          ]
        },
        {
          "openalex_id": "W4414480137",
          "year": 2025,
          "title": "Comparing Psychometric Properties of 6 of the 5-Level and 3-Level EQ-5D Bolt-Ons in a Large, Multinational, Longitudinal General Population Sample",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Assistive Technology in Communication and Mobility",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Urban Green Space and Health"
          ]
        },
        {
          "openalex_id": "W2398000892",
          "year": 2000,
          "title": "Een leefbaarheidsbarometer voor Leuven. Bewoners beoordelen leven en wonen in hun wijk",
          "type": "book",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Dutch Social and Cultural Studies",
            "Urban Transport and Accessibility"
          ]
        },
        {
          "openalex_id": "W2044951461",
          "year": 2003,
          "title": "Continuous retrograde blood cardioplegia is associated with lower hospital mortality after heart valve surgery",
          "type": "article",
          "venue": "Journal of Thoracic and Cardiovascular Surgery",
          "cited_by_count": 13,
          "topics": [
            "Cardiac Ischemia and Reperfusion",
            "Cardiac and Coronary Surgery Techniques",
            "Aortic Disease and Treatment Approaches"
          ]
        },
        {
          "openalex_id": "W2050822403",
          "year": 2003,
          "title": "PMD20 THE COST-EFFECTIVENESS OF SCREENING PROGRAMS USING SINGLE AND MULTIPLE BIRTH COHORT SIMULATIONS: A COMPARISON USING A MODEL OF CERVICAL CANCER",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Delphi Technique in Research",
            "Nursing Roles and Practices",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W2031796548",
          "year": 2004,
          "title": "PMH19 THE PERCEIVED BENEFITS OF DOSING SCHEDULES FOR CHILDREN WITH ADHD",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Attention Deficit Hyperactivity Disorder"
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
          "openalex_id": "W2767725047",
          "year": 2017,
          "title": "What Impact Does Venous Thromboembolism and Bleeding Have on Cancer Patients’ Quality of Life?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 94,
          "topics": [
            "Venous Thromboembolism Diagnosis and Management",
            "Chemotherapy-induced cardiotoxicity and mitigation",
            "Erythropoietin and Anemia Treatment"
          ]
        },
        {
          "openalex_id": "W2054060007",
          "year": 2006,
          "title": "The economic value of anti-IgE in severe persistent, IgE-mediated (allergic) asthma patients:adaptation of INNOVATE to Sweden",
          "type": "article",
          "venue": "Current Medical Research and Opinion",
          "cited_by_count": 90,
          "topics": [
            "Asthma and respiratory diseases",
            "Allergic Rhinitis and Sensitization",
            "IL-33, ST2, and ILC Pathways"
          ]
        },
        {
          "openalex_id": "W2085270509",
          "year": 2009,
          "title": "Cost-effectiveness of warfarin: Trial versus “real-world” stroke prevention in atrial fibrillation",
          "type": "article",
          "venue": "American Heart Journal",
          "cited_by_count": 82,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Acute Ischemic Stroke Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2919920923",
          "year": 2019,
          "title": "The combined impact of dependency on caregivers, disability, and coping strategy on quality of life after ischemic stroke",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 79,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Dementia and Cognitive Impairment Research",
            "Traumatic Brain Injury Research"
          ]
        },
        {
          "openalex_id": "W2587732585",
          "year": 2017,
          "title": "Modified Rankin scale as a determinant of direct medical costs after stroke",
          "type": "article",
          "venue": "International Journal of Stroke",
          "cited_by_count": 61,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W4318754420",
          "year": 2023,
          "title": "Patient-reported burden of myasthenia gravis: baseline results of the international prospective, observational, longitudinal real-world digital study MyRealWorld-MG",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 51,
          "topics": [
            "Myasthenia Gravis and Thymoma",
            "Adrenal Hormones and Disorders",
            "Autoimmune Neurological Disorders and Treatments"
          ]
        }
      ]
    }
  }
]
