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
    "name": "Jahangir Khan",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1669-VS",
        "title": "Establishing value sets for EQ-5D-3L and EQ-5D-5L in Bangladesh",
        "working_group": "Valuation"
      },
      {
        "project_id": "2480-EO",
        "title": "Dissemination seminar on Bangladesh value sets for EQ-5D-3L and EQ-5D-5L study and piloting of EQ-5D-Y",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5052565475",
      "display_name": "Jahangir Khan",
      "orcid": "0000-0002-6151-764X",
      "reported_affiliation": "Liverpool School of Tropical Medicine",
      "works_count": 125,
      "top_topics": [
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 42
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 40
        },
        {
          "topic": "Global Health Care Issues",
          "works": 24
        },
        {
          "topic": "Child Nutrition and Water Access",
          "works": 14
        },
        {
          "topic": "Global Health and Epidemiology",
          "works": 11
        },
        {
          "topic": "Employment and Welfare Studies",
          "works": 9
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 7
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 7
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 6
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 6
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 6
        },
        {
          "topic": "Vibrio bacteria research studies",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sayem Ahmed",
          "works": 41
        },
        {
          "name": "Abdur Razzaque Sarker",
          "works": 24
        },
        {
          "name": "Marufa Sultana",
          "works": 23
        },
        {
          "name": "Louis Niessen",
          "works": 21
        },
        {
          "name": "Zia Ul Islam",
          "works": 20
        },
        {
          "name": "Rashidul Alam Mahumud",
          "works": 15
        },
        {
          "name": "Mohammad Wahid Ahmed",
          "works": 14
        },
        {
          "name": "Md. Zahid Hasan",
          "works": 13
        },
        {
          "name": "Andrew J. Mirelman",
          "works": 9
        },
        {
          "name": "Clas Rehnberg",
          "works": 8
        },
        {
          "name": "Tracey Pérez Koehlmoos",
          "works": 7
        },
        {
          "name": "Firdausi Qadri",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4414655439",
          "year": 2025,
          "title": "An intelligent deep representation learning with enhanced feature selection approach for cyberattack detection in internet of things enabled cloud environment",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 2,
          "topics": [
            "Network Security and Intrusion Detection",
            "Advanced Malware Detection Techniques",
            "Internet Traffic Analysis and Secure E-voting"
          ]
        },
        {
          "openalex_id": "W4408986962",
          "year": 2025,
          "title": "Determinants of care-seeking for ARI/Pneumonia-like symptoms among under-2 children in urban slums in and around Dhaka City, Bangladesh",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 3,
          "topics": [
            "Pneumonia and Respiratory Infections",
            "Child Nutrition and Water Access",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W4417461664",
          "year": 2025,
          "title": "Ensemble deep learning with advanced feature engineering for embryo evaluation on in-vitro fertilisation procedures using biomedical images",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 1,
          "topics": [
            "Reproductive Biology and Fertility",
            "Ovarian function and disorders",
            "Reproductive Health and Technologies"
          ]
        },
        {
          "openalex_id": "W4417009576",
          "year": 2025,
          "title": "Epidemiological and molecular analysis of thalassemia (Beta Globin Gene) in the heterogeneous population of gwadar, Pakistan",
          "type": "conference-abstract",
          "venue": "Blood",
          "cited_by_count": 0,
          "topics": [
            "Hemoglobinopathies and Related Disorders",
            "Iron Metabolism and Disorders",
            "Blood groups and transfusion"
          ]
        },
        {
          "openalex_id": "W4414778722",
          "year": 2025,
          "title": "Exploiting deep transfer learning based precise classification and grading of renal cell carcinoma using histopathological images",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 0,
          "topics": [
            "AI in cancer detection",
            "Radiomics and Machine Learning in Medical Imaging",
            "Colorectal Cancer Screening and Detection"
          ]
        },
        {
          "openalex_id": "W4414856529",
          "year": 2025,
          "title": "Modeling of Explainable Artificial Intelligence With a Filter-Based Attribute Selection Framework for Smart Consumer Healthcare Electronics",
          "type": "article",
          "venue": "IEEE Transactions on Consumer Electronics",
          "cited_by_count": 0,
          "topics": [
            "Artificial Intelligence in Healthcare",
            "Brain Tumor Detection and Classification",
            "Machine Learning in Healthcare"
          ]
        },
        {
          "openalex_id": "W249436255",
          "year": 1973,
          "title": "Causal paths in elaboration of organizational structure: a case of hospital services.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Complex Systems and Decision Making"
          ]
        },
        {
          "openalex_id": "W2921078315",
          "year": 1981,
          "title": "Multiple forms of glucosaminidase in mammalian skeletal muscle",
          "type": "article",
          "venue": "Biochemical Society Transactions",
          "cited_by_count": 0,
          "topics": [
            "Muscle metabolism and nutrition",
            "Protein Hydrolysis and Bioactive Peptides"
          ]
        },
        {
          "openalex_id": "W2914617064",
          "year": 1989,
          "title": "SERUM PROTEIN AND ALBUMIN, LIPID AND CHOLESTEROL CONCENTRATION IN NORMAL ADULT POPULATION OF DISTRICT ABBOTTABAD",
          "type": "article",
          "venue": "Journal of Ayub Medical College Abbottabad",
          "cited_by_count": 0,
          "topics": [
            "Muscle metabolism and nutrition",
            "Meat and Animal Product Quality",
            "Adipose Tissue and Metabolism"
          ]
        },
        {
          "openalex_id": "W1502050869",
          "year": 1990,
          "title": "Acute respiratory infections in children: a case management intervention in Abbottabad District, Pakistan.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 70,
          "topics": [
            "Child and Adolescent Health",
            "Vaccine Coverage and Hesitancy",
            "Pneumonia and Respiratory Infections"
          ]
        },
        {
          "openalex_id": "W2795707819",
          "year": 2018,
          "title": "Tackling socioeconomic inequalities and non-communicable diseases in low-income and middle-income countries under the Sustainable Development agenda",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 405,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Health disparities and outcomes",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2618177743",
          "year": 2017,
          "title": "Catastrophic healthcare expenditure and poverty related to out-of-pocket payments for healthcare in Bangladesh—an estimation of financial risk protection of universal health coverage",
          "type": "article",
          "venue": "Health Policy and Planning",
          "cited_by_count": 205,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2271241286",
          "year": 2016,
          "title": "Willingness-to-Pay for Community-Based Health Insurance among Informal Workers in Urban Bangladesh",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 152,
          "topics": [
            "Healthcare Systems and Reforms",
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2923875968",
          "year": 2019,
          "title": "Measuring the efficiency of health systems in Asia: a data envelopment analysis",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 148,
          "topics": [
            "Efficiency Analysis Using DEA",
            "Global Health Care Issues",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W1897470778",
          "year": 2015,
          "title": "Feasibility and effectiveness of oral cholera vaccine in an urban endemic setting in Bangladesh: a cluster randomised open-label trial",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 137,
          "topics": [
            "Vibrio bacteria research studies",
            "Viral Infections and Outbreaks Research",
            "Bacillus and Francisella bacterial research"
          ]
        },
        {
          "openalex_id": "W2077561632",
          "year": 2015,
          "title": "Trends and Inequities in Use of Maternal Health Care Services in Bangladesh, 1991-2011",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 99,
          "topics": [
            "Global Maternal and Child Health",
            "Healthcare Systems and Reforms",
            "Global Health and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2598319394",
          "year": 2017,
          "title": "Distribution and Determinants of Out-of-pocket Healthcare Expenditures in Bangladesh",
          "type": "article",
          "venue": "Journal of Preventive Medicine and Public Health",
          "cited_by_count": 90,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4229079298",
          "year": 2021,
          "title": "Assessing the incidence of catastrophic health expenditure and impoverishment from out-of-pocket payments and their determinants in Bangladesh: evidence from the nationwide Household Income and Expenditure Survey 2016",
          "type": "article",
          "venue": "International Health",
          "cited_by_count": 89,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "Global Health Care Issues"
          ]
        }
      ]
    }
  },
  {
    "name": "James Shaw",
    "member_affiliation": "Takeda Pharmaceuticals",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5055862397",
      "display_name": "James W. Shaw",
      "orcid": "0000-0002-7019-3720",
      "reported_affiliation": "Bristol-Myers Squibb (United States)",
      "works_count": 156,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 52
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 23
        },
        {
          "topic": "Cancer Immunotherapy and Biomarkers",
          "works": 15
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 14
        },
        {
          "topic": "Criminal Justice and Corrections Analysis",
          "works": 12
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 11
        },
        {
          "topic": "Head and Neck Cancer Studies",
          "works": 8
        },
        {
          "topic": "Migraine and Headache Studies",
          "works": 7
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 7
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 7
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 6
        },
        {
          "topic": "Crime Patterns and Interventions",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "A. Simon Pickard",
          "works": 15
        },
        {
          "name": "Bryan Bennett",
          "works": 13
        },
        {
          "name": "Doris Layton MacKenzie",
          "works": 13
        },
        {
          "name": "Stephen Joel Coons",
          "works": 12
        },
        {
          "name": "Kevin J. Harrington",
          "works": 10
        },
        {
          "name": "David Cella",
          "works": 10
        },
        {
          "name": "Robert I. Haddad",
          "works": 8
        },
        {
          "name": "Fiona Taylor",
          "works": 8
        },
        {
          "name": "Kim Cocks",
          "works": 8
        },
        {
          "name": "Robert L. Ferris",
          "works": 7
        },
        {
          "name": "J. Guigay",
          "works": 7
        },
        {
          "name": "Maura L. Gillison",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7165526123",
          "year": 2026,
          "title": "Reliability, validity, and measurement invariance of 7-day recall and no-recall versions of the Patient-Reported Outcomes Measurement Information System (PROMIS®) Short Form v2.0 – Physical Function 8c",
          "type": "article",
          "venue": "Advances in Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Cancer survivorship and care",
            "Medication Adherence and Compliance",
            "Nutrition and Health in Aging"
          ]
        },
        {
          "openalex_id": "W4411491812",
          "year": 2025,
          "title": "No Differential Item Functioning between \"No Recall\" and \"7-Day Recall\" of PROMIS Physical Function items",
          "type": "article",
          "venue": "Advances in Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Education, Safety, and Science Studies",
            "Education and Learning Interventions",
            "Diverse Approaches in Healthcare and Education Studies"
          ]
        },
        {
          "openalex_id": "W4407853101",
          "year": 2025,
          "title": "Predicting Danish EQ-5D-5L Utilities Based on United Kingdom EQ-5D-3L Utilities for Use in Health Economic Models",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W4414932993",
          "year": 2025,
          "title": "United Kingdom value set for the functional assessment of cancer therapy eight dimension (FACT-8D) preference-based quality of life instrument",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4409417639",
          "year": 2025,
          "title": "Using patient-reported outcomes and health-related quality of life data in regulatory decisions on cancer treatment: highlights from an EMA-EORTC workshop",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 22,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W4392820132",
          "year": 2024,
          "title": "A Methodological Study to Compare Alternative Modes of Administration to Value EQ-5D Using Preference-Elicitation Techniques",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 6,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2606630936",
          "year": 1926,
          "title": "REGENERATION OF PANCREATIC TISSUE FROM THE TRANSPLANTED PANCREATIC DUCT IN THE DOG",
          "type": "article",
          "venue": "American Journal of Physiology-Legacy Content",
          "cited_by_count": 31,
          "topics": [
            "Pancreatic function and diabetes",
            "Renal and related cancers",
            "Pediatric Hepatobiliary Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W2010211634",
          "year": 1974,
          "title": "Parathyroid Hormone (PTH)-Mediated Rise in Urinary Cyclic AMP (UcAMP) During Acute Extracellular Fluid (ECF) Expansion Natriuresis in Man*",
          "type": "article",
          "venue": "The Journal of Clinical Endocrinology & Metabolism",
          "cited_by_count": 16,
          "topics": [
            "Thyroid and Parathyroid Surgery",
            "Parathyroid Disorders and Treatments",
            "Genetic Syndromes and Imprinting"
          ]
        },
        {
          "openalex_id": "W2038686698",
          "year": 1975,
          "title": "Epinephrine-Induced Alterations in Urinary Cyclic AMP in Hyper- and Hypothyroidism",
          "type": "article",
          "venue": "The Journal of Clinical Endocrinology & Metabolism",
          "cited_by_count": 41,
          "topics": [
            "Thyroid Disorders and Treatments",
            "Ion channel regulation and function",
            "Nitric Oxide and Endothelin Effects"
          ]
        },
        {
          "openalex_id": "W2046379754",
          "year": 1977,
          "title": "Urinary cyclic AMP analyzed as a function of the serum calcium and parathyroid hormone in the idfferential diagnosis of hypercalcemia.",
          "type": "article",
          "venue": "Journal of Clinical Investigation",
          "cited_by_count": 63,
          "topics": [
            "Bone health and treatments",
            "Bone health and osteoporosis research",
            "Hormonal and reproductive studies"
          ]
        },
        {
          "openalex_id": "W2529484692",
          "year": 2016,
          "title": "Nivolumab for Recurrent Squamous-Cell Carcinoma of the Head and Neck",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 5121,
          "topics": [
            "Head and Neck Cancer Studies",
            "Cancer Immunotherapy and Biomarkers",
            "Nonmelanoma Skin Cancer Studies"
          ]
        },
        {
          "openalex_id": "W2096782143",
          "year": 2005,
          "title": "US Valuation of the EQ-5D Health States",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 1298,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2711613673",
          "year": 2017,
          "title": "Nivolumab versus standard, single-agent therapy of investigator's choice in recurrent or metastatic squamous cell carcinoma of the head and neck (CheckMate 141): health-related quality-of-life results from a randomised, phase 3 trial",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 431,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Head and Neck Cancer Studies",
            "CAR-T cell therapy research"
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
          "openalex_id": "W2088673482",
          "year": 2005,
          "title": "Self-Reported Health Status of the General Adult U.S. Population as Assessed by the EQ-5D and Health Utilities Index",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 392,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4248486935",
          "year": 2005,
          "title": "The Determinants of Life Expectancy: An Analysis of the OECD Health Data",
          "type": "article",
          "venue": "Southern Economic Journal",
          "cited_by_count": 227,
          "topics": [
            "Global Health Care Issues",
            "Insurance, Mortality, Demography, Risk Management",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2142427202",
          "year": 2005,
          "title": "Valuations of EQ-5D Health States",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 226,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2162131595",
          "year": 2007,
          "title": "Greater occipital nerve block using local anaesthetics alone or with triamcinolone for transformed migraine: a randomised comparative study",
          "type": "article",
          "venue": "Journal of Neurology Neurosurgery & Psychiatry",
          "cited_by_count": 167,
          "topics": [
            "Migraine and Headache Studies",
            "Myofascial pain diagnosis and treatment",
            "Pain Management and Treatment"
          ]
        }
      ]
    }
  },
  {
    "name": "Jan Abel Olsen",
    "member_affiliation": "Department of Community Medicine, UiT The Arctic University of Norway",
    "is_member": true,
    "projects": [
      {
        "project_id": "1830-RA",
        "title": "Response heterogeneities in EQ-VAS within identical EQ-5D-5L profiles: Investigating potential underestimation of the education-health gradient",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1973-TVG",
        "title": "Three weeks research visit to University of Melbourne, Monash University and University Technology Sydney to: facilitate collaborative work on two RFPs; present EQ-based papers at various seminars, and; revise a grant application investigating relevant bolt-ons for older adults.",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2295-RA",
        "title": "Exploring older people's understanding of the  EQ-5D-5L: a qualitative study",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5052181611",
      "display_name": "Jan Abel Olsen",
      "orcid": "0000-0001-9472-2669",
      "reported_affiliation": "UiT The Arctic University of Norway",
      "works_count": 191,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 91
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 69
        },
        {
          "topic": "Global Health Care Issues",
          "works": 44
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 37
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 26
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 17
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 13
        },
        {
          "topic": "Employment and Welfare Studies",
          "works": 11
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 7
        },
        {
          "topic": "Intergenerational and Educational Inequality Studies",
          "works": 5
        },
        {
          "topic": "Breast Cancer Treatment Studies",
          "works": 5
        },
        {
          "topic": "Child Abuse and Trauma",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Paul Dolan",
          "works": 18
        },
        {
          "name": "Birgit Abelsen",
          "works": 18
        },
        {
          "name": "Gang Chen",
          "works": 15
        },
        {
          "name": "Jeff Richardson",
          "works": 14
        },
        {
          "name": "Admassu N. Lamu",
          "works": 14
        },
        {
          "name": "Jan Norum",
          "works": 11
        },
        {
          "name": "Ivar Sønbø Kristiansen",
          "works": 8
        },
        {
          "name": "Richard Smith",
          "works": 7
        },
        {
          "name": "Cam Donaldson",
          "works": 7
        },
        {
          "name": "Dorte Gyrd‐Hansen",
          "works": 5
        },
        {
          "name": "Thor Gamst-Klaussen",
          "works": 5
        },
        {
          "name": "Anthony Harris",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7151896784",
          "year": 2026,
          "title": "Beyond the education-health gradient: the importance of early-life and lifestyle factors for health-related quality of life: A Norwegian cohort study",
          "type": "article",
          "venue": "Scandinavian Journal of Public Health",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes",
            "Intergenerational and Educational Inequality Studies",
            "Early Childhood Education and Development"
          ]
        },
        {
          "openalex_id": "W7166440507",
          "year": 2026,
          "title": "Explaining inequalities in quality of life: a longitudinal study of health disparities in Norway",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W7164854844",
          "year": 2026,
          "title": "Measuring inequality in quality of life: further evidence that the EQ-5D-5L may underestimate it",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W7151895683",
          "year": 2026,
          "title": "Psychometric Performance of Preference-Weighted Instruments in Older Adults: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Nutrition and Health in Aging",
            "Physical Activity and Health",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W7151851807",
          "year": 2026,
          "title": "The impact of acute hearth attack, stroke, and cancer on labour market participation: A panel data study from Norway",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Employment and Welfare Studies",
            "Workplace Health and Well-being",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4415098579",
          "year": 2025,
          "title": "Common Method Variance: Statistical Detection and Control",
          "type": "article",
          "venue": "UNC Libraries",
          "cited_by_count": 0,
          "topics": [
            "Advanced Statistical Methods and Models",
            "Advanced Statistical Process Monitoring"
          ]
        },
        {
          "openalex_id": "W318125307",
          "year": 1976,
          "title": "Case reports. Customized reconstruction of the breast after radical and modified radical mastectomies.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Breast Implant and Reconstruction",
            "Breast Cancer Treatment Studies",
            "Reconstructive Surgery and Microvascular Techniques"
          ]
        },
        {
          "openalex_id": "W2474328985",
          "year": 1983,
          "title": "IV therapy nurse upgraded at Hale.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Nursing Roles and Practices"
          ]
        },
        {
          "openalex_id": "W2418736378",
          "year": 1988,
          "title": "[Primary health centers].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 4,
          "topics": [
            "Health and Medical Studies"
          ]
        },
        {
          "openalex_id": "W2470494609",
          "year": 1990,
          "title": "[Consumption of alcohol and tobacco during pregnancy by health advisors. An investigation of nurses, nurses' aides, physicians and school teachers].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "School Health and Nursing Education"
          ]
        },
        {
          "openalex_id": "W2014943738",
          "year": 2001,
          "title": "Theory versuspractice: a review of ?willingness-to-pay? in health and health care",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 423,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2903602806",
          "year": 2018,
          "title": "Cost-Effectiveness of Telemedicine in Remote Orthopedic Consultations: Randomized Controlled Trial",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 309,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Mobile Health and mHealth Applications",
            "Healthcare Systems and Technology"
          ]
        },
        {
          "openalex_id": "W2016972410",
          "year": 2002,
          "title": "The role of adaptation to disability and disease in health state valuation: a preliminary normative analysis",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 223,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2015368967",
          "year": 2014,
          "title": "Estimating QALY Gains in Applied Studies: A Review of Cost-Utility Analyses Published in 2010",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 203,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W1963662183",
          "year": 1998,
          "title": "Helicopters, hearts and hips: Using willingness to pay to set priorities for public sector health care programmes",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 199,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2032497249",
          "year": 2002,
          "title": "An inquiry into the different perspectives that can be used when eliciting preferences in health",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 144,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2047269660",
          "year": 1997,
          "title": "Theories of justice and their implications for priority setting in health care",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 141,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2349423311",
          "year": 2016,
          "title": "Clarifying Associations between Childhood Adversity, Social Support, Behavioral Factors, and Mental Health, Health, and Well-Being in Adulthood: A Population-Based Study",
          "type": "article",
          "venue": "Frontiers in Psychology",
          "cited_by_count": 122,
          "topics": [
            "Child Abuse and Trauma",
            "Resilience and Mental Health",
            "Migration, Health and Trauma"
          ]
        }
      ]
    }
  },
  {
    "name": "Jan Busschbach",
    "member_affiliation": "Erasmus MC",
    "is_member": true,
    "projects": [
      {
        "project_id": "2013240",
        "title": "Indonesian valuation and validation study of the EQ-5D-5L and its application in families living in unhealthy circumstances and in breast cancer patients",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015230",
        "title": "Funding proposal for an scholarship for international travel and cooperation",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2016040",
        "title": "Assessing the validity of the 86 health state selection for EQ-5D-5L VT studies: are we using the most efficient and valid set of health states to predict health states that exist in practice?",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016421",
        "title": "The follow up meeting with Indonesian Ministry of Health and HTA Committee: EQ-5D inHTA and non-HTA research and the EQ-5D-5L value set",
        "working_group": "Others"
      },
      {
        "project_id": "20170160",
        "title": "Can we use a 25 health states to estimate a EQ-5D-5L value set instead of “EQ-VT standard” 86?",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5020122364",
      "display_name": "Jan J.V. Busschbach",
      "orcid": "0000-0002-8602-0381",
      "reported_affiliation": "Erasmus MC",
      "works_count": 522,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 117
        },
        {
          "topic": "Organ Donation and Transplantation",
          "works": 58
        },
        {
          "topic": "Personality Disorders and Psychopathology",
          "works": 57
        },
        {
          "topic": "Psychotherapy Techniques and Applications",
          "works": 45
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 34
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 32
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 31
        },
        {
          "topic": "Renal Transplantation Outcomes and Treatments",
          "works": 27
        },
        {
          "topic": "Mental Health and Psychiatry",
          "works": 20
        },
        {
          "topic": "Dialysis and Renal Disease Management",
          "works": 20
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 19
        },
        {
          "topic": "Ovarian function and disorders",
          "works": 17
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Reinier Timman",
          "works": 86
        },
        {
          "name": "Leonieke W. Kranenburg",
          "works": 61
        },
        {
          "name": "Willem Weimar",
          "works": 56
        },
        {
          "name": "Roel Verheul",
          "works": 46
        },
        {
          "name": "Jan Passchier",
          "works": 42
        },
        {
          "name": "Emma K. Massey",
          "works": 38
        },
        {
          "name": "Zhihao Yang",
          "works": 31
        },
        {
          "name": "Willij C. Zuidema",
          "works": 31
        },
        {
          "name": "Sohal Y. Ismail",
          "works": 30
        },
        {
          "name": "Elly Stolk",
          "works": 28
        },
        {
          "name": "Nan Luo",
          "works": 27
        },
        {
          "name": "Jan N.M. IJzermans",
          "works": 26
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7131354028",
          "year": 2026,
          "title": "Anxiety and depression may amplify self-reported physical health problems: evidence from EQ-5D-5L data",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Workplace Health and Well-being"
          ]
        },
        {
          "openalex_id": "W7124149006",
          "year": 2026,
          "title": "Clinical and Cost-Effectiveness of Blended Cognitive Behavioral Therapy or Psychodynamic Therapy Versus Face-to-Face Psychotherapy for Depression (BLENDED Study): Protocol for a Pragmatic, Multicenter, Assessor-Blinded Randomized Controlled Noninferiority Trial",
          "type": "article",
          "venue": "JMIR Research Protocols",
          "cited_by_count": 0,
          "topics": [
            "Digital Mental Health Interventions",
            "Treatment of Major Depression",
            "Psychotherapy Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W7165048388",
          "year": 2026,
          "title": "Data from A Multicenter Phase II Randomized Controlled Trial Comparing &lt;sup&gt;177&lt;/sup&gt;Lu-Dotatate/Capecitabine Combination Treatment with &lt;sup&gt;177&lt;/sup&gt;Lu-Dotatate Monotherapy in Patients with Neuroendocrine Tumors",
          "type": "other",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Neuroendocrine Tumor Research Advances",
            "Lung Cancer Research Studies",
            "Esophageal Cancer Research and Treatment"
          ]
        },
        {
          "openalex_id": "W7125735193",
          "year": 2026,
          "title": "HRQoL in adolescents with idiopathic isolated GHD: rhGH (dis)continuation in mid-puberty",
          "type": "article",
          "venue": "Endocrine Connections",
          "cited_by_count": 0,
          "topics": [
            "Growth Hormone and Insulin-like Growth Factors",
            "Pituitary Gland Disorders and Treatments",
            "Genetic Syndromes and Imprinting"
          ]
        },
        {
          "openalex_id": "W7165062566",
          "year": 2026,
          "title": "Supplementary Data 1 from A Multicenter Phase II Randomized Controlled Trial Comparing &lt;sup&gt;177&lt;/sup&gt;Lu-Dotatate/Capecitabine Combination Treatment with &lt;sup&gt;177&lt;/sup&gt;Lu-Dotatate Monotherapy in Patients with Neuroendocrine Tumors",
          "type": "supplementary-materials",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Neuroendocrine Tumor Research Advances",
            "Thyroid Cancer Diagnosis and Treatment",
            "Breast Lesions and Carcinomas"
          ]
        },
        {
          "openalex_id": "W7160554533",
          "year": 2026,
          "title": "Using patient input to develop item banks to measure quality-of-life impact of vitreous floaters",
          "type": "article",
          "venue": "BMJ Open Ophthalmology",
          "cited_by_count": 0,
          "topics": [
            "Retinal and Macular Surgery",
            "Ophthalmology and Visual Impairment Studies",
            "Intraocular Surgery and Lenses"
          ]
        },
        {
          "openalex_id": "W2094486394",
          "year": 1993,
          "title": "The utility of health at different stages in life: A quantitative approach",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 105,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2127482479",
          "year": 1994,
          "title": "Measuring the Quality of Life Before and After Bilateral Lung Transplantation in Patients With Cystic Fibrosis",
          "type": "article",
          "venue": "CHEST Journal",
          "cited_by_count": 100,
          "topics": [
            "Transplantation: Methods and Outcomes",
            "Renal Transplantation Outcomes and Treatments",
            "Interstitial Lung Diseases and Idiopathic Pulmonary Fibrosis"
          ]
        },
        {
          "openalex_id": "W2147850448",
          "year": 1995,
          "title": "Experiencing the life cycle",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 3,
          "topics": [
            "Bioinformatics and Genomic Networks",
            "Lipoproteins and Cardiovascular Health",
            "Genetic Associations and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2045216225",
          "year": 1995,
          "title": "Impaired social status of growth hormone deficient adults as compared to controls with short or normal stature",
          "type": "article",
          "venue": "Clinical Endocrinology",
          "cited_by_count": 53,
          "topics": [
            "Growth Hormone and Insulin-like Growth Factors",
            "Pituitary Gland Disorders and Treatments",
            "Stress Responses and Cortisol"
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
          "openalex_id": "W2089165963",
          "year": 2012,
          "title": "Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1652,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Education",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2110682994",
          "year": 2004,
          "title": "A comparison of the EQ‐5D and SF‐6D across seven patient groups",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 806,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2096463904",
          "year": 2006,
          "title": "The Dutch tariff: results and arguments for an effective design for national EQ‐5D valuation studies",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 636,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2118332255",
          "year": 2005,
          "title": "[Measuring the quality of life in economic evaluations: the Dutch EQ-5D tariff].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 581,
          "topics": []
        },
        {
          "openalex_id": "W1978010209",
          "year": 2015,
          "title": "Standardised Mindfulness-Based Interventions in Healthcare: An Overview of Systematic Reviews and Meta-Analyses of RCTs",
          "type": "review",
          "venue": "PLoS ONE",
          "cited_by_count": 546,
          "topics": [
            "Mindfulness and Compassion Interventions",
            "Acupuncture Treatment Research Studies",
            "Pain Management and Placebo Effect"
          ]
        },
        {
          "openalex_id": "W2092394859",
          "year": 2011,
          "title": "Psychological Factors Affecting the Outcome of Total Hip and Knee Arthroplasty: A Systematic Review",
          "type": "review",
          "venue": "Seminars in Arthritis and Rheumatism",
          "cited_by_count": 474,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Orthopaedic implants and arthroplasty",
            "Hip and Femur Fractures"
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
        }
      ]
    }
  },
  {
    "name": "Jan Faller",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1851-TVG",
        "title": "Travel scholarship request to attend the EuHEA conference 2024 in Vienna, Austria - Jan Faller",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2197-EO",
        "title": "Travel scholarship request to attend and present at the IHEA Congress 2025 in Bali, Indonesia.",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5043601549",
      "display_name": "Jan Faller",
      "orcid": "0000-0001-7645-2079",
      "reported_affiliation": "Monash Health",
      "works_count": 14,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 6
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 4
        },
        {
          "topic": "Substance Abuse Treatment and Outcomes",
          "works": 3
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 3
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 3
        },
        {
          "topic": "Schizophrenia research and treatment",
          "works": 2
        },
        {
          "topic": "Mental Health and Patient Involvement",
          "works": 2
        },
        {
          "topic": "Alcohol Consumption and Health Effects",
          "works": 2
        },
        {
          "topic": "Intergenerational Family Dynamics and Caregiving",
          "works": 2
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 1
        },
        {
          "topic": "Global Health Care Issues",
          "works": 1
        },
        {
          "topic": "Smoking Behavior and Cessation",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Cathrine Mihalopoulos",
          "works": 11
        },
        {
          "name": "Lidia Engel",
          "works": 8
        },
        {
          "name": "Mary Lou Chatterton",
          "works": 8
        },
        {
          "name": "Long Khanh‐Dao Le",
          "works": 6
        },
        {
          "name": "Joahna Kevin Perez",
          "works": 4
        },
        {
          "name": "Yong Yi Lee",
          "works": 4
        },
        {
          "name": "Cath Chapman",
          "works": 3
        },
        {
          "name": "Nicola C. Newton",
          "works": 3
        },
        {
          "name": "Tim Slade",
          "works": 3
        },
        {
          "name": "Maree Teesson",
          "works": 3
        },
        {
          "name": "Mario Álvarez‐Jiménez",
          "works": 2
        },
        {
          "name": "Daniela Cagliarini",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4411339835",
          "year": 2025,
          "title": "An Updated Systematic Literature Review of the Economic Costs of Loneliness and Social Isolation and the Cost Effectiveness of Interventions",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 10,
          "topics": [
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4412534852",
          "year": 2025,
          "title": "Are Generic Preference-Based Measures Valid for Use in Informal Carers? A Psychometric Investigation",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Intergenerational Family Dynamics and Caregiving",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W4410835888",
          "year": 2025,
          "title": "Economic evaluation of subcutaneous ketamine injections for treatment resistant depression: A randomised, double-blind, active-controlled trial – The KADS study",
          "type": "article",
          "venue": "Journal of Affective Disorders",
          "cited_by_count": 2,
          "topics": [
            "Treatment of Major Depression",
            "Mental Health Treatment and Access",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W4416453874",
          "year": 2025,
          "title": "The Cost-Effectiveness of a Novel Online Social Therapy to Maintain Treatment Effects From First-Episode Psychosis Services: Results From the Horyzons Randomized Controlled Trial",
          "type": "article",
          "venue": "UNC Libraries",
          "cited_by_count": 0,
          "topics": [
            "Digital Mental Health Interventions",
            "Schizophrenia research and treatment",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W4411746668",
          "year": 2025,
          "title": "The Psychometric Performance of Generic Preference-Based Measures in Informal Carers: A Systematic Review of Validation Studies",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Intergenerational Family Dynamics and Caregiving",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W4391850733",
          "year": 2024,
          "title": "Age at first drink and its influence on alcohol use behaviours in young adulthood: Evidence from an Australian household-based panel study",
          "type": "article",
          "venue": "Preventive Medicine",
          "cited_by_count": 8,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Alcohol Consumption and Health Effects",
            "Smoking Behavior and Cessation"
          ]
        },
        {
          "openalex_id": "W3186293304",
          "year": 2021,
          "title": "Are interventions to improve cardiovascular disease risk factors in premenopausal women effective? A systematic review and meta-analysis",
          "type": "review",
          "venue": "BMJ Open",
          "cited_by_count": 7,
          "topics": [
            "Cardiovascular Health and Risk Factors",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Nutritional Studies and Diet"
          ]
        },
        {
          "openalex_id": "W4296027775",
          "year": 2022,
          "title": "Economic evaluation of a Decision Support Tool to guide intensity of mental health care in general practice: the Link-me pragmatic randomised controlled trial",
          "type": "article",
          "venue": "BMC Family Practice",
          "cited_by_count": 8,
          "topics": [
            "Mental Health Treatment and Access",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W4385663686",
          "year": 2023,
          "title": "A systematic review of economic evaluations for opioid misuse, cannabis and illicit drug use prevention",
          "type": "review",
          "venue": "BJPsych Open",
          "cited_by_count": 6,
          "topics": [
            "Opioid Use Disorder Treatment",
            "Prenatal Substance Exposure Effects",
            "Substance Abuse Treatment and Outcomes"
          ]
        },
        {
          "openalex_id": "W4389951582",
          "year": 2023,
          "title": "Economic evidence for prevention and treatment of eating disorders: An updated systematic review",
          "type": "review",
          "venue": "International Journal of Eating Disorders",
          "cited_by_count": 8,
          "topics": [
            "Eating Disorders and Behaviors",
            "Body Image and Dysmorphia Studies",
            "Sexuality, Behavior, and Technology"
          ]
        },
        {
          "openalex_id": "W4378953860",
          "year": 2023,
          "title": "The Cost-Effectiveness of a Novel Online Social Therapy to Maintain Treatment Effects From First-Episode Psychosis Services: Results From the Horyzons Randomized Controlled Trial",
          "type": "article",
          "venue": "Schizophrenia Bulletin",
          "cited_by_count": 32,
          "topics": [
            "Schizophrenia research and treatment",
            "Digital Mental Health Interventions",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W4382182522",
          "year": 2023,
          "title": "Interventions to prevent alcohol use: systematic review of economic evaluations",
          "type": "review",
          "venue": "BJPsych Open",
          "cited_by_count": 15,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Alcohol Consumption and Health Effects"
          ]
        }
      ]
    }
  }
]
