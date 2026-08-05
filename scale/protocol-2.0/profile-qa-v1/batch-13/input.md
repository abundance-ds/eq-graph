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
    "name": "Deborah Street",
    "member_affiliation": "University of Technology Sydney",
    "is_member": true,
    "projects": [
      {
        "project_id": "20190350",
        "title": "A comparison of DCEs with choice sets of size 2 and DCEs with various choice set sizes for the valuation of the EQ-5D",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5053497885",
      "display_name": "Deborah J. Street",
      "orcid": "0000-0002-4476-0656",
      "reported_affiliation": "University of Technology Sydney",
      "works_count": 187,
      "top_topics": [
        {
          "topic": "Economic and Environmental Valuation",
          "works": 84
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 43
        },
        {
          "topic": "Optimal Experimental Design Methods",
          "works": 37
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 24
        },
        {
          "topic": "graph theory and CDMA systems",
          "works": 17
        },
        {
          "topic": "Consumer Market Behavior and Pricing",
          "works": 11
        },
        {
          "topic": "Reproductive Health and Contraception",
          "works": 10
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 8
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 7
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 6
        },
        {
          "topic": "Advanced Multi-Objective Optimization Algorithms",
          "works": 6
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Rosalie Viney",
          "works": 56
        },
        {
          "name": "Leonie Burgess",
          "works": 37
        },
        {
          "name": "Richard Norman",
          "works": 34
        },
        {
          "name": "Marion Haas",
          "works": 16
        },
        {
          "name": "Madeleine King",
          "works": 14
        },
        {
          "name": "Brendan Mulhern",
          "works": 14
        },
        {
          "name": "Stephen Goodall",
          "works": 14
        },
        {
          "name": "Richard De Abreu Lourenço",
          "works": 14
        },
        {
          "name": "John Brazier",
          "works": 12
        },
        {
          "name": "Stephanie Knox",
          "works": 11
        },
        {
          "name": "Julie Ratcliffe",
          "works": 11
        },
        {
          "name": "Jordan J. Louviere",
          "works": 10
        }
      ],
      "work_examples": [
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
          "openalex_id": "W7162515809",
          "year": 2026,
          "title": "Societal Preferences for Assessment Pathways of Rare Disease Drugs: A Discrete Choice Experiment",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Genomics and Rare Diseases",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W7129637247",
          "year": 2026,
          "title": "Understanding Preferences for Preconception Care in Australia: Insights From a Discrete Choice Experiment",
          "type": "article",
          "venue": "Health Expectations",
          "cited_by_count": 1,
          "topics": [
            "Reproductive Health and Contraception",
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Global Maternal and Child Health"
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
          "openalex_id": "W7123351017",
          "year": 2026,
          "title": "Valuation of the EQ-5D-Y-5L Using DCE Methods That Account for Nonlinear Time Preferences",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W7153305065",
          "year": 2026,
          "title": "Women’s experiences with diagnosis and management of vaginal symptoms of menopause: a mixed-methods study",
          "type": "article",
          "venue": "BMC Women s Health",
          "cited_by_count": 0,
          "topics": [
            "Menopause: Health Impacts and Treatments",
            "Sexual function and dysfunction studies",
            "Pelvic floor disorders treatments"
          ]
        },
        {
          "openalex_id": "W2335212321",
          "year": 1967,
          "title": "PRINCIPLES OF ORGANIZATION. By Theodore Caplow. New York: Harcourt, Brace &amp; World, 1964. 397 pp. $6.95",
          "type": "article",
          "venue": "Social Forces",
          "cited_by_count": 0,
          "topics": [
            "Management Theory and Practice",
            "Global and Cross-Cultural Management",
            "Management and Organizational Studies"
          ]
        },
        {
          "openalex_id": "W619333439",
          "year": 1977,
          "title": "Solution manual to Combinatorial theory : an introduction by A.P. Street, William H. Wilson",
          "type": "book",
          "venue": "Medical Entomology and Zoology",
          "cited_by_count": 0,
          "topics": [
            "Advanced Mathematical Theories",
            "Mathematics and Applications",
            "Graph Labeling and Dimension Problems"
          ]
        },
        {
          "openalex_id": "W1587915809",
          "year": 1980,
          "title": "All DBIBDs with block size four exist",
          "type": "article",
          "venue": "Research Online (University of Wollongong)",
          "cited_by_count": 28,
          "topics": [
            "graph theory and CDMA systems",
            "Optimal Experimental Design Methods",
            "Rings, Modules, and Algebras"
          ]
        },
        {
          "openalex_id": "W1996508231",
          "year": 1980,
          "title": "Bhaskar Rao designs from cyclotomy",
          "type": "article",
          "venue": "Journal of the Australian Mathematical Society",
          "cited_by_count": 10,
          "topics": [
            "Optimal Experimental Design Methods",
            "graph theory and CDMA systems"
          ]
        },
        {
          "openalex_id": "W2088186114",
          "year": 2005,
          "title": "Quick and easy choice sets: Constructing optimal and nearly optimal stated choice experiments",
          "type": "article",
          "venue": "International Journal of Research in Marketing",
          "cited_by_count": 552,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Consumer Market Behavior and Pricing"
          ]
        },
        {
          "openalex_id": "W2492807224",
          "year": 2007,
          "title": "The Construction of Optimal Stated Choice Experiments",
          "type": "book",
          "venue": "Wiley series in probability and statistics",
          "cited_by_count": 402,
          "topics": [
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W630074859",
          "year": 2007,
          "title": "The Construction of Optimal Stated Choice Experiments: Theory and Methods",
          "type": "article",
          "venue": "",
          "cited_by_count": 319,
          "topics": [
            "Economic and Environmental Valuation"
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
          "openalex_id": "W2132095645",
          "year": 2008,
          "title": "Designing Discrete Choice Experiments: Do Optimal Designs Come at a Price?",
          "type": "article",
          "venue": "Journal of Consumer Research",
          "cited_by_count": 250,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Consumer Market Behavior and Pricing"
          ]
        },
        {
          "openalex_id": "W2009237207",
          "year": 1989,
          "title": "Combinatorics of Experimental Design.",
          "type": "article",
          "venue": "Journal of the American Statistical Association",
          "cited_by_count": 244,
          "topics": [
            "Design Education and Practice"
          ]
        },
        {
          "openalex_id": "W1985136372",
          "year": 2008,
          "title": "Modeling the choices of individual decision-makers by combining efficient choice experiment designs with extra preference information",
          "type": "article",
          "venue": "Journal of Choice Modelling",
          "cited_by_count": 241,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Consumer Market Behavior and Pricing"
          ]
        },
        {
          "openalex_id": "W1859778715",
          "year": 2002,
          "title": "Dissecting the Random Component of Utility",
          "type": "article",
          "venue": "Marketing Letters",
          "cited_by_count": 216,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Consumer Market Behavior and Pricing"
          ]
        }
      ]
    }
  },
  {
    "name": "Des Scott",
    "member_affiliation": "University of Cape Town",
    "is_member": true,
    "projects": [
      {
        "project_id": "2248-TR",
        "title": "Formatting the EQ Health and Wellbeing 9 (EQ-HWB-9): Qualitative assessment of acceptability of the digital version",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5038664789",
      "display_name": "Des Scott",
      "orcid": "0000-0003-3943-7392",
      "reported_affiliation": "University of Cape Town",
      "works_count": 20,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 12
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 5
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 4
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 4
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 3
        },
        {
          "topic": "Occupational Therapy Practice and Research",
          "works": 2
        },
        {
          "topic": "Clinical Nutrition and Gastroenterology",
          "works": 2
        },
        {
          "topic": "Nutrition and Health in Aging",
          "works": 2
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 1
        },
        {
          "topic": "Autoimmune and Inflammatory Disorders Research",
          "works": 1
        },
        {
          "topic": "Adolescent and Pediatric Healthcare",
          "works": 1
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Janine Verstraete",
          "works": 10
        },
        {
          "name": "Jennifer Jelsma",
          "works": 5
        },
        {
          "name": "Razia Amien",
          "works": 4
        },
        {
          "name": "Hilary Short",
          "works": 4
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 3
        },
        {
          "name": "Fatima Al Sayah",
          "works": 3
        },
        {
          "name": "Henry Bailey",
          "works": 3
        },
        {
          "name": "Dominik Golicki",
          "works": 3
        },
        {
          "name": "Fredrick Dermawan Purba",
          "works": 3
        },
        {
          "name": "Jeffrey Johnson",
          "works": 2
        },
        {
          "name": "Nils Gutacker",
          "works": 2
        },
        {
          "name": "Erica I. Lubetkin",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7161802675",
          "year": 2026,
          "title": "EQ-5D-5L population health and cross-country comparison across 15 countries (the EQ-DAPHNIE project)",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Health, psychology, and well-being"
          ]
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
          "openalex_id": "W4410056786",
          "year": 2025,
          "title": "EuroQol data for assessment of population health needs and instrument evaluation (EQ-DAPHNIE): a study for enhancing population health assessment",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 6,
          "topics": [
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, Environment, Cognitive Aging"
          ]
        },
        {
          "openalex_id": "W4401993913",
          "year": 2024,
          "title": "He/She/They - gender inclusivity in developing and using health-related questionnaires: a scoping review",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 7,
          "topics": [
            "Sex and Gender in Healthcare",
            "Rheumatoid Arthritis Research and Therapies",
            "LGBTQ Health, Identity, and Policy"
          ]
        },
        {
          "openalex_id": "W4321491034",
          "year": 2023,
          "title": "The validity and reliability of the interviewer-administered EQ-5D-Y-3L version in young children",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 10,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cerebral Palsy and Movement Disorders",
            "Pediatric Pain Management Techniques"
          ]
        },
        {
          "openalex_id": "W4223946477",
          "year": 2022,
          "title": "Comparing Measurement Properties of the English EQ-5D-Y 3-Level Version With the 5-Level Version in South Africa",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 18,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W2156973736",
          "year": 2001,
          "title": "Home artificial nutritional support: the value of the British Artificial Nutrition Survey",
          "type": "article",
          "venue": "Clinical Nutrition",
          "cited_by_count": 31,
          "topics": [
            "Clinical Nutrition and Gastroenterology",
            "Child Nutrition and Feeding Issues",
            "Nutrition and Health in Aging"
          ]
        },
        {
          "openalex_id": "W2025296916",
          "year": 2001,
          "title": "Home enteral tube feeding following cerebrovascular accident",
          "type": "article",
          "venue": "Clinical Nutrition",
          "cited_by_count": 30,
          "topics": [
            "Clinical Nutrition and Gastroenterology",
            "Dysphagia Assessment and Management",
            "Nutrition and Health in Aging"
          ]
        },
        {
          "openalex_id": "W2142458785",
          "year": 2010,
          "title": "Impact of using the ICF framework as an assessment tool for students in paediatric physiotherapy: a preliminary study",
          "type": "article",
          "venue": "Physiotherapy",
          "cited_by_count": 35,
          "topics": [
            "Cerebral Palsy and Movement Disorders",
            "Occupational Therapy Practice and Research",
            "Clinical Reasoning and Diagnostic Skills"
          ]
        },
        {
          "openalex_id": "W2141314705",
          "year": 2014,
          "title": "Do physiotherapy students perceive that they are adequately prepared to enter clinical practice? An empirical study",
          "type": "article",
          "venue": "African Journal of Health Professions Education",
          "cited_by_count": 7,
          "topics": [
            "Occupational Therapy Practice and Research",
            "Innovations in Medical Education",
            "Nursing Roles and Practices"
          ]
        },
        {
          "openalex_id": "W2573222080",
          "year": 2017,
          "title": "The use of the EQ-5D-Y health related quality of life outcome measure in children in the Western Cape, South Africa: psychometric properties, feasibility and usefulness - a longitudinal, analytical study",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 91,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W3026280548",
          "year": 2020,
          "title": "How does the EQ-5D-Y Proxy version 1 perform in 3, 4 and 5-year-old children?",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 59,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W4283020880",
          "year": 2022,
          "title": "Comparison of the EQ-5D-Y-5L, EQ-5D-Y-3L and PedsQL in children and adolescents",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 31,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W2965257181",
          "year": 2019,
          "title": "Validity and feasibility of the self-report EQ-5D-Y as a generic Health-Related Quality of Life outcome measure in children and adolescents with Juvenile Idiopathic Arthritis in Western Cape, South Africa",
          "type": "article",
          "venue": "South African Journal of Physiotherapy",
          "cited_by_count": 31,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Adolescent and Pediatric Healthcare",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W4212905107",
          "year": 2022,
          "title": "Measurement properties and responsiveness of the EQ-5D-Y-5L compared to the EQ-5D-Y-3L in children and adolescents receiving acute orthopaedic care",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 29,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Health Policy Implementation Science"
          ]
        }
      ]
    }
  },
  {
    "name": "Dominik Golicki",
    "member_affiliation": "Medical Univeristy of Warsaw",
    "is_member": true,
    "projects": [
      {
        "project_id": "1575-VS",
        "title": "Valuation of the EQ-5D-Y-3L in Poland",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2015240",
        "title": "EQ-5D-5L VALUATION IN POLAND",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015280",
        "title": "EQ-5D-3L in Hematologic Malignant Neoplasms: a Systematic Review of Health State Utility Values",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2016110",
        "title": "EQ-5D-5L valuation in Poland: a methodological extension",
        "working_group": "Valuation"
      },
      {
        "project_id": "2038-RA",
        "title": "Comparison of DCE duration and EQ-VT in EQ-5D-Y-5L in Poland",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2100-EOI",
        "title": "1st EuroQol Central and Eastern Europe Regional Meeting",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "214-RA",
        "title": "Measurement properties of the EQ-5D-Y: a systematic review",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "2479-RA",
        "title": "Translating the EQ-5D Bolt-on Toolbox  (Best Available, EV1.0 & Exploratory set of items, EV1.5) into Polish (for Poland)",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "337-RA",
        "title": "Measurement properties of the EQ-5D in diseases of the upper respiratory tract: a systematic review",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "339-RA",
        "title": "Systematic Review of Measurement Properties of the EQ-5D in Hematologic Cancers",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5035126117",
      "display_name": "Dominik Golicki",
      "orcid": "0000-0001-7741-4760",
      "reported_affiliation": "Medical University of Warsaw",
      "works_count": 162,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 67
        },
        {
          "topic": "Global Health Care Issues",
          "works": 18
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 9
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 9
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 8
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 8
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 7
        },
        {
          "topic": "Cardiac Arrhythmias and Treatments",
          "works": 7
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 7
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 6
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 6
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Maciej Niewada",
          "works": 51
        },
        {
          "name": "Michał Jakubczyk",
          "works": 28
        },
        {
          "name": "László Gulàcsi",
          "works": 26
        },
        {
          "name": "Márta Péntek",
          "works": 26
        },
        {
          "name": "Zsombor Zrubka",
          "works": 23
        },
        {
          "name": "Valentina Prevolnik Rupel",
          "works": 22
        },
        {
          "name": "Petra Baji",
          "works": 22
        },
        {
          "name": "Tomasz Hermanowski",
          "works": 19
        },
        {
          "name": "Fanni Rencz",
          "works": 18
        },
        {
          "name": "Valentin Brodszky",
          "works": 18
        },
        {
          "name": "Witold Wrona",
          "works": 17
        },
        {
          "name": "T Macioch",
          "works": 15
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164732578",
          "year": 2026,
          "title": "1st EuroQol Central and Eastern Europe Regional Meeting: Book of Abstracts",
          "type": "other",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7164751425",
          "year": 2026,
          "title": "1st EuroQol Central and Eastern Europe Regional Meeting: Book of Abstracts",
          "type": "other",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7161802675",
          "year": 2026,
          "title": "EQ-5D-5L population health and cross-country comparison across 15 countries (the EQ-DAPHNIE project)",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W7135058486",
          "year": 2026,
          "title": "The value of social robots supporting informal care: a discrete choice experiment among informal caregivers",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Social Robot Interaction and HRI",
            "Assistive Technology in Communication and Mobility",
            "AI in Service Interactions"
          ]
        },
        {
          "openalex_id": "W7154140943",
          "year": 2026,
          "title": "Validity, Reliability, and Responsiveness of the EQ-5D in Hematological Cancers: A Systematic Review of Measurement Properties",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Breast Cancer Treatment Studies",
            "Economic and Financial Impacts of Cancer"
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
          "openalex_id": "W2408960641",
          "year": 2003,
          "title": "Shoulder arthroscopy in the net.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Intellectual Property Rights and Media",
            "Health, Work, and Social Studies in Poland",
            "Leadership and Management in Organizations"
          ]
        },
        {
          "openalex_id": "W2430750298",
          "year": 2003,
          "title": "The review of outcome measures in the shoulder surgery.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Shoulder Injury and Treatment",
            "Shoulder and Clavicle Injuries"
          ]
        },
        {
          "openalex_id": "W48833690",
          "year": 2004,
          "title": "Application of clindamycin in therapy of orthopaedic infections with special regard to applicability in outpatients practice.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Orthopedic Infections and Treatments",
            "Historical Medical Research and Treatments",
            "Musculoskeletal Disorders and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W1972836530",
          "year": 2005,
          "title": "PCN5 THE COST OF SECOND-LINE TREATMENT OF OVARIAN CANCER IN POLISH SETTINGS",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Multiple and Secondary Primary Cancers",
            "Cancer Risks and Factors"
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
          "openalex_id": "W2021768440",
          "year": 2014,
          "title": "Validity of EQ-5D-5L in stroke",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 267,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management"
          ]
        },
        {
          "openalex_id": "W2118976763",
          "year": 2014,
          "title": "Comparing responsiveness of the EQ-5D-5L, EQ-5D-3L and EQ VAS in stroke patients",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 153,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Stroke Rehabilitation and Recovery",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W2484016290",
          "year": 2016,
          "title": "EQ-5D in Central and Eastern Europe: 2000–2015",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 152,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2335411225",
          "year": 2015,
          "title": "EQ-5D-5L Polish population norms",
          "type": "article",
          "venue": "Archives of Medical Science",
          "cited_by_count": 144,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W3048694137",
          "year": 2020,
          "title": "Parallel Valuation of the EQ-5D-3L and EQ-5D-5L by Time Trade-Off in Hungary",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 119,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W1978393391",
          "year": 2009,
          "title": "Valuation of EQ-5D Health States in Poland: First TTO-Based Social Value Set in Central and Eastern Europe",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 115,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Quality and Management",
            "Patient Satisfaction in Healthcare"
          ]
        }
      ]
    }
  },
  {
    "name": "Donna Rowen",
    "member_affiliation": "University of Sheffield",
    "is_member": true,
    "projects": [
      {
        "project_id": "134-RA",
        "title": "Valuing well-being alongside health: What can and should be done? Project number 20190750 (Revised)",
        "working_group": "Valuation"
      },
      {
        "project_id": "1524-VS",
        "title": "UK valuation of the EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190140",
        "title": "Valuing health benefits for children and adolescents: Qualitative research examining the impact of perspective and respondents’ priorities around adult and child health",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2201-RA",
        "title": "Exploration and assessment of potential methods for generating consistent utilities and QALYs across the life-course",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "222-RA",
        "title": "Pilot of the UK EQ-5D-5L TTO valuation to assess equivalence and feasibility of online interviews and face-to-face interviews during the COVID-19 pandemic",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5067226056",
      "display_name": "Donna Rowen",
      "orcid": "0000-0003-3018-5109",
      "reported_affiliation": "",
      "works_count": 273,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 195
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 84
        },
        {
          "topic": "Global Health Care Issues",
          "works": 34
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 28
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 21
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 12
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 10
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 10
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 10
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 9
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 9
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 8
        }
      ],
      "frequent_coauthors": [
        {
          "name": "John Brazier",
          "works": 175
        },
        {
          "name": "Brendan Mulhern",
          "works": 79
        },
        {
          "name": "Aki Tsuchiya",
          "works": 66
        },
        {
          "name": "Clara Mukuria",
          "works": 55
        },
        {
          "name": "Tracey Young",
          "works": 49
        },
        {
          "name": "Louise Longworth",
          "works": 47
        },
        {
          "name": "Jill Carlton",
          "works": 41
        },
        {
          "name": "Anju Keetharuth",
          "works": 35
        },
        {
          "name": "Nancy Devlin",
          "works": 31
        },
        {
          "name": "Yaling Yang",
          "works": 27
        },
        {
          "name": "Richard Norman",
          "works": 23
        },
        {
          "name": "Philip A. Powell",
          "works": 23
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7116635480",
          "year": 2026,
          "title": "Valuing child and adolescent health states for use in economic evaluation: A good practices report of an ISPOR task force",
          "type": "article",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4410618796",
          "year": 2025,
          "title": "A Systematic Review of Attributes Influencing Preferences for Treatments and Interventions in People With Amyotrophic Lateral Sclerosis (<scp>ALS</scp>)",
          "type": "review",
          "venue": "Muscle & Nerve",
          "cited_by_count": 1,
          "topics": [
            "Amyotrophic Lateral Sclerosis Research",
            "Neurogenetic and Muscular Disorders Research"
          ]
        },
        {
          "openalex_id": "W4416069460",
          "year": 2025,
          "title": "Comparative Assessment of Short Form 6-Dimension Health State Preferences Among Lebanese Population Pre- and Post-COVID-19 Pandemic",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4410449495",
          "year": 2025,
          "title": "Determining the Content Validity of the EQ-5D-5L, EQ-5D-Y-3L, and CHU9D Instruments for Assessing Generic Child and Adolescent Health-Related Quality of Life: A Qualitative Study",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W4406688629",
          "year": 2025,
          "title": "Embedding a Choice Experiment in an Online Decision Aid or Tool: Scoping Review",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 3,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4408343264",
          "year": 2025,
          "title": "Enhancing HRQoL assessment for economic evaluation in dementia populations",
          "type": "article",
          "venue": "Alzheimer s & Dementia Translational Research & Clinical Interventions",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W1489389606",
          "year": 2004,
          "title": "Incorporating Ethics into Economics: Problems and Possibilities",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 2,
          "topics": [
            "Experimental Behavioral Economics Studies",
            "Economic Theory and Institutions",
            "Income, Poverty, and Inequality"
          ]
        },
        {
          "openalex_id": "W2589071536",
          "year": 2005,
          "title": "Ethical Principles and Economic Analysis",
          "type": "article",
          "venue": "Journal of Interdisciplinary Economics",
          "cited_by_count": 3,
          "topics": [
            "Experimental Behavioral Economics Studies",
            "Economic Theory and Institutions",
            "Ethics in Business and Education"
          ]
        },
        {
          "openalex_id": "W1508594088",
          "year": 2007,
          "title": "Are people ethical? An experimental approach",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 0,
          "topics": [
            "Experimental Behavioral Economics Studies",
            "Ethics in Business and Education",
            "Psychology of Moral and Emotional Judgment"
          ]
        },
        {
          "openalex_id": "W1503702285",
          "year": 2007,
          "title": "Attitudes and motivations of Economics students: Some recent evidence",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 1,
          "topics": [
            "Experimental Behavioral Economics Studies",
            "Innovations in Educational Methods",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2087604552",
          "year": 2009,
          "title": "A review of studies mapping (or cross walking) non-preference based measures of health to generic preference-based measures",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 533,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W1970908877",
          "year": 2014,
          "title": "Use of generic and condition-specific measures of health-related quality of life in NICE decision-making: a systematic review, statistical modelling and survey",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 419,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W2150637118",
          "year": 2013,
          "title": "Mapping to Obtain EQ-5D Utility Values for Use in NICE Health Technology Assessments",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 265,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W1972932269",
          "year": 2009,
          "title": "Mapping SF-36 onto the EQ-5D index: how reliable is the relationship?",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 203,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2006310627",
          "year": 2012,
          "title": "Developing and testing methods for deriving preference-based measures of health from condition-specific measures (and other patient-based measures of outcome).",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 191,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2104766485",
          "year": 2013,
          "title": "Development of DEMQOL-U and DEMQOL-PROXY-U: generation of preference-based indices from DEMQOL and DEMQOL-PROXY for use in economic evaluation",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 177,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cerebral Palsy and Movement Disorders",
            "Economic and Environmental Valuation"
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
          "openalex_id": "W2737575630",
          "year": 2017,
          "title": "International Regulations and Recommendations for Utility Data for Health Technology Assessment",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 164,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Pharmaceutical Economics and Policy"
          ]
        }
      ]
    }
  },
  {
    "name": "Edward Webb",
    "member_affiliation": "University of Leeds",
    "is_member": true,
    "projects": [
      {
        "project_id": "2316-RA",
        "title": "Quantitative evidence supporting the adoption of a visual analogue scale for the EQ-HWB-9 using hypothetical vignettes",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "289-RA",
        "title": "COVID-19 and EQ-5D-5L health state valuation",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5011344482",
      "display_name": "Edward Webb",
      "orcid": "0000-0001-7918-839X",
      "reported_affiliation": "University of Leeds",
      "works_count": 60,
      "top_topics": [
        {
          "topic": "Economic and Environmental Valuation",
          "works": 9
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Assistive Technology in Communication and Mobility",
          "works": 7
        },
        {
          "topic": "Multiple Sclerosis Research Studies",
          "works": 6
        },
        {
          "topic": "Consumer Market Behavior and Pricing",
          "works": 5
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 4
        },
        {
          "topic": "Family Support in Illness",
          "works": 4
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 3
        },
        {
          "topic": "Hearing Impairment and Communication",
          "works": 3
        },
        {
          "topic": "Intergenerational Family Dynamics and Caregiving",
          "works": 3
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 3
        },
        {
          "topic": "Child and Adolescent Health",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "David Meads",
          "works": 21
        },
        {
          "name": "Stephane Hess",
          "works": 9
        },
        {
          "name": "Yvonne Lynch",
          "works": 8
        },
        {
          "name": "Simon Judge",
          "works": 8
        },
        {
          "name": "Juliet Goldbart",
          "works": 8
        },
        {
          "name": "Stuart Meredith",
          "works": 8
        },
        {
          "name": "Liz Moulam",
          "works": 8
        },
        {
          "name": "Janice Murray",
          "works": 8
        },
        {
          "name": "Nicola Randall",
          "works": 7
        },
        {
          "name": "Ieva Eskytė",
          "works": 6
        },
        {
          "name": "Jeremy Chataway",
          "works": 6
        },
        {
          "name": "Helen Ford",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7165558310",
          "year": 2026,
          "title": "<b>E</b> quitable <b>P</b> alliative care <b>I</b> n the <b>C</b> ommunity through <b>P</b> rimary <b>C</b> are (EPIC-PC) study protocol: a realist study to propose a new integrated neighbourhood team approach to palliative care",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Mental Health and Patient Involvement",
            "Interprofessional Education and Collaboration"
          ]
        },
        {
          "openalex_id": "W4414073683",
          "year": 2025,
          "title": "Characteristics and population estimates of unpaid end of life carers: An observational study",
          "type": "article",
          "venue": "Palliative Medicine",
          "cited_by_count": 0,
          "topics": [
            "Grief, Bereavement, and Mental Health",
            "Family Support in Illness",
            "Intergenerational Family Dynamics and Caregiving"
          ]
        },
        {
          "openalex_id": "W4410061702",
          "year": 2025,
          "title": "My husband is my responsibility:” motivations and activities of informal caregiving for patients with chronic diseases in Uganda",
          "type": "article",
          "venue": "Discover Public Health",
          "cited_by_count": 0,
          "topics": [
            "Global Maternal and Child Health",
            "HIV/AIDS Impact and Responses",
            "Family Support in Illness"
          ]
        },
        {
          "openalex_id": "W4416130650",
          "year": 2025,
          "title": "Procalcitonin evaluation of antibiotic use in COVID-19 hospitalised patients: The PEACH mixed methods study",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 1,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Antibiotic Use and Resistance",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W4404619731",
          "year": 2024,
          "title": "Choice of primary healthcare providers among population in urban areas of low- and middle-income countries—a protocol for systematic review of literature",
          "type": "review",
          "venue": "Systematic Reviews",
          "cited_by_count": 0,
          "topics": [
            "Global Maternal and Child Health",
            "Economic and Environmental Valuation",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W4405940762",
          "year": 2024,
          "title": "Health and economic impact of caregiving on informal caregivers of people with chronic diseases in sub-Saharan Africa: A systematic review",
          "type": "review",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 12,
          "topics": [
            "Family Support in Illness",
            "Intergenerational Family Dynamics and Caregiving",
            "Family Caregiving in Mental Illness"
          ]
        },
        {
          "openalex_id": "W2318317046",
          "year": 1897,
          "title": "Postgate's <i>Silva Maniliana</i> - Silva Maniliana. Congessit Joh. P. Postgate. Cantabrigiae, MDCCCLXXXXVII. <i>3S.</i> net.",
          "type": "article",
          "venue": "The Classical Review",
          "cited_by_count": 0,
          "topics": [
            "Cuban History and Society"
          ]
        },
        {
          "openalex_id": "W2319974089",
          "year": 1898,
          "title": "Manitius' Edition of Hipparchus - ‘Hipparchi in Arati et Eudoxi Phaenomena Commentariorum Libri Tres’ ad Codicum Fidem recensuit Germanica Interpretatione et Commentariis instruxit Carolus Manitius. Lipsiae, in Aedihus B. G. Teubneri. 1894. 4 M.",
          "type": "article",
          "venue": "The Classical Review",
          "cited_by_count": 8,
          "topics": [
            "Historical Astronomy and Related Studies",
            "Historical, Religious, and Philosophical Studies",
            "Historical and Linguistic Studies"
          ]
        },
        {
          "openalex_id": "W2047157341",
          "year": 1899,
          "title": "Thiele's <i>Antike Himmelsbilder</i> - Antike Himmelsbilder, von Geoeg Thiele. Mit 7 Tafeln und 72 in den Text gedruckten Abbildungen. (Berlin : Weidmannsche Buchhandlung. 1898.) 20 M.",
          "type": "article",
          "venue": "The Classical Review",
          "cited_by_count": 0,
          "topics": [
            "Historical Geography and Cartography"
          ]
        },
        {
          "openalex_id": "W4400191896",
          "year": 1958,
          "title": "The use of complex growth functions in sales and economic forecasting",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Economic Development and Digital Transformation",
            "Economic and Technological Developments in Russia"
          ]
        },
        {
          "openalex_id": "W2782724327",
          "year": 2018,
          "title": "A Systematic Review of Discrete-Choice Experiments and Conjoint Analysis Studies in People with Multiple Sclerosis",
          "type": "review",
          "venue": "Patient",
          "cited_by_count": 49,
          "topics": [
            "Multiple Sclerosis Research Studies",
            "Economic and Environmental Valuation",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W4213075636",
          "year": 2022,
          "title": "The path towards herd immunity: Predicting COVID-19 vaccination uptake through results from a stated choice study across six continents",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 45,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 epidemiological studies"
          ]
        },
        {
          "openalex_id": "W2050110137",
          "year": 2011,
          "title": "Resisting Anamnesis: A Nietzschean Analysis of Turkey's National History Education",
          "type": "article",
          "venue": "Journal of Contemporary European Studies",
          "cited_by_count": 38,
          "topics": [
            "Religious Education and Schools",
            "Jewish Identity and Society",
            "Educator Training and Historical Pedagogy"
          ]
        },
        {
          "openalex_id": "W2901314543",
          "year": 2018,
          "title": "Understanding treatment decisions from the perspective of people with relapsing remitting multiple Sclerosis: A critical interpretive synthesis",
          "type": "article",
          "venue": "Multiple Sclerosis and Related Disorders",
          "cited_by_count": 34,
          "topics": [
            "Multiple Sclerosis Research Studies",
            "Healthcare Decision-Making and Restraints",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W3011344686",
          "year": 2020,
          "title": "Transforming discrete choice experiment latent scale values for EQ-5D-3L using the visual analogue scale",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 31,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2912352762",
          "year": 2019,
          "title": "What’s important in AAC decision making for children? Evidence from a best–worst scaling survey",
          "type": "article",
          "venue": "Augmentative and Alternative Communication",
          "cited_by_count": 24,
          "topics": [
            "Assistive Technology in Communication and Mobility",
            "Tracheal and airway disorders",
            "Hearing Impairment and Communication"
          ]
        },
        {
          "openalex_id": "W2990191139",
          "year": 2019,
          "title": "Finding the best fit: examining the decision-making of augmentative and alternative communication professionals in the UK using a discrete choice experiment",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 22,
          "topics": [
            "Assistive Technology in Communication and Mobility",
            "Cerebral Palsy and Movement Disorders",
            "Autism Spectrum Disorder Research"
          ]
        },
        {
          "openalex_id": "W3183414539",
          "year": 2021,
          "title": "Does a health crisis change how we value health?",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 21,
          "topics": [
            "Global Health Care Issues",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Climate Change and Health Impacts"
          ]
        }
      ]
    }
  }
]
