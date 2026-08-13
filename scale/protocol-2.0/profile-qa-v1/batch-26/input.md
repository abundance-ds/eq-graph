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
    "name": "John Brazier",
    "member_affiliation": "University of Sheffield",
    "is_member": true,
    "projects": [
      {
        "project_id": "2014080",
        "title": "Comparison of the EQ-5D-5L to measures of well-being and capability in an older population",
        "working_group": "Others"
      },
      {
        "project_id": "2016660",
        "title": "How to capture fluctuating health impairments: Testing intensive longitudinal assessment of the EQ-5D-5L in multiple sclerosis",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2016710",
        "title": "Going beyond health related quality of life – towards a broader QALY measure for use across sectors",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5007276743",
      "display_name": "John Brazier",
      "orcid": "0000-0001-8645-4780",
      "reported_affiliation": "Novartis (Switzerland)",
      "works_count": 858,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 448
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 183
        },
        {
          "topic": "Global Health Care Issues",
          "works": 121
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 100
        },
        {
          "topic": "Clostridium difficile and Clostridium perfringens research",
          "works": 61
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 41
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 33
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 33
        },
        {
          "topic": "Viral gastroenteritis research and epidemiology",
          "works": 27
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 23
        },
        {
          "topic": "Microscopic Colitis",
          "works": 22
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 22
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Donna Rowen",
          "works": 174
        },
        {
          "name": "Aki Tsuchiya",
          "works": 118
        },
        {
          "name": "Brendan Mulhern",
          "works": 98
        },
        {
          "name": "Clara Mukuria",
          "works": 75
        },
        {
          "name": "Tracey Young",
          "works": 60
        },
        {
          "name": "Julie Ratcliffe",
          "works": 58
        },
        {
          "name": "Jill Carlton",
          "works": 51
        },
        {
          "name": "Louise Longworth",
          "works": 49
        },
        {
          "name": "Anju Keetharuth",
          "works": 43
        },
        {
          "name": "Nancy Devlin",
          "works": 39
        },
        {
          "name": "Janice Connell",
          "works": 37
        },
        {
          "name": "Michael Barkham",
          "works": 35
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4413636468",
          "year": 2025,
          "title": "Meeting reports",
          "type": "article",
          "venue": "The Biochemist",
          "cited_by_count": 0,
          "topics": [
            "Advanced biosensing and bioanalysis techniques",
            "DNA and Nucleic Acid Chemistry",
            "Supramolecular Chemistry and Complexes"
          ]
        },
        {
          "openalex_id": "W4414983129",
          "year": 2025,
          "title": "Patient-reported vision impairment in low luminance relates to visual function in age-related macular degeneration: A MACUSTAR study report",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 2,
          "topics": [
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies",
            "Retinal Imaging and Analysis"
          ]
        },
        {
          "openalex_id": "W4407157728",
          "year": 2025,
          "title": "Validating candidate endpoints for intermediate age-related macular degeneration trials in a multi-centre setting—lessons from the MACUSTAR study",
          "type": "article",
          "venue": "Eye",
          "cited_by_count": 4,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W2406467814",
          "year": 2024,
          "title": "A conceptual comparison of well-being measures used in the UK",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 12,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Health disparities and outcomes",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W2474113531",
          "year": 2024,
          "title": "An empirical comparison of wellbeing measures used in UK",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 13,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Global Health Care Issues",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2395807849",
          "year": 2024,
          "title": "Case-mix methodology for the NHS outcomes framework GP patient survey questionnaire data",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W4313051536",
          "year": 1874,
          "title": "Description of Eleven New Species of Terrestrial and Marine Shells, from North-East Australia",
          "type": "article",
          "venue": "Transactions of the Royal Society of New South Wales",
          "cited_by_count": 0,
          "topics": [
            "Maritime and Coastal Archaeology",
            "Paleontology and Evolutionary Biology",
            "Geotourism and Geoheritage Conservation"
          ]
        },
        {
          "openalex_id": "W2596143702",
          "year": 1876,
          "title": "A list of the Pleurotomidae collected during the Chevert Expedition, with the description of the new species",
          "type": "article",
          "venue": "Proceedings of the Linnean Society of New South Wales",
          "cited_by_count": 4,
          "topics": [
            "Subterranean biodiversity and taxonomy",
            "Invertebrate Taxonomy and Ecology",
            "Collembola Taxonomy and Ecology Studies"
          ]
        },
        {
          "openalex_id": "W2414419406",
          "year": 1877,
          "title": "Continuation of the Mollusca of the Chevert Expedition",
          "type": "article",
          "venue": "Proceedings of the Linnean Society of New South Wales",
          "cited_by_count": 2,
          "topics": [
            "Marine Biology and Ecology Research",
            "Space Exploration and Technology",
            "Polar Research and Ecology"
          ]
        },
        {
          "openalex_id": "W2281458289",
          "year": 1877,
          "title": "Continuation of the Mollusca of the Chevert Expedition, with new species",
          "type": "article",
          "venue": "Proceedings of the Linnean Society of New South Wales",
          "cited_by_count": 1,
          "topics": [
            "Marine Biology and Ecology Research",
            "Aquatic Invertebrate Ecology and Behavior",
            "Marine Ecology and Invasive Species"
          ]
        },
        {
          "openalex_id": "W2113750014",
          "year": 1992,
          "title": "Validating the SF-36 health survey questionnaire: new outcome measure for primary care.",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 4703,
          "topics": [
            "Survey Methodology and Nonresponse",
            "Health disparities and outcomes",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2092052931",
          "year": 2002,
          "title": "The estimation of a preference-based measure of health from the SF-36",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 3050,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2050302634",
          "year": 1998,
          "title": "Cross-Validation of Item Selection and Scoring for the SF-12 Health Survey in Nine Countries",
          "type": "article",
          "venue": "Journal of Clinical Epidemiology",
          "cited_by_count": 2913,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Health disparities and outcomes",
            "Behavioral Health and Interventions"
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
          "openalex_id": "W2163423623",
          "year": 2005,
          "title": "Toxin production by an emerging strain of Clostridium difficile associated with outbreaks of severe disease in North America and Europe",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 1441,
          "topics": [
            "Clostridium difficile and Clostridium perfringens research",
            "Bacillus and Francisella bacterial research",
            "Antimicrobial Resistance in Staphylococcus"
          ]
        },
        {
          "openalex_id": "W2094993869",
          "year": 2005,
          "title": "Comparison of the minimally important difference for two health state utility measures: EQ-5D and SF-6D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1342,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1965742808",
          "year": 2004,
          "title": "The Estimation of a Preference-Based Measure of Health From the SF-12",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 1317,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W1486826346",
          "year": 2016,
          "title": "Measuring and Valuing Health Benefits for Economic Evaluation",
          "type": "book",
          "venue": "Oxford University Press eBooks",
          "cited_by_count": 1063,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        }
      ]
    }
  },
  {
    "name": "John Hartman",
    "member_affiliation": "GSK",
    "is_member": true,
    "projects": [
      {
        "project_id": "2016680",
        "title": "Screen size & data quality",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016690",
        "title": "DCE Learning curves",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180560",
        "title": "Non-Linear Time Preferences in Discrete Choice Experiments",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5108501222",
      "display_name": "Karen Hartman",
      "orcid": "",
      "reported_affiliation": "",
      "works_count": 239,
      "top_topics": [
        {
          "topic": "Social Work Education and Practice",
          "works": 56
        },
        {
          "topic": "Social Policy and Reform Studies",
          "works": 38
        },
        {
          "topic": "Research in Social Sciences",
          "works": 18
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 15
        },
        {
          "topic": "Homelessness and Social Issues",
          "works": 15
        },
        {
          "topic": "Public Policy and Administration Research",
          "works": 15
        },
        {
          "topic": "Policy Transfer and Learning",
          "works": 15
        },
        {
          "topic": "Aging, Elder Care, and Social Issues",
          "works": 9
        },
        {
          "topic": "Web and Library Services",
          "works": 8
        },
        {
          "topic": "Healthcare innovation and challenges",
          "works": 8
        },
        {
          "topic": "Cardiovascular Function and Risk Factors",
          "works": 7
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Wayne L. Miller",
          "works": 15
        },
        {
          "name": "Allan S. Jaffe",
          "works": 14
        },
        {
          "name": "Ernest C. Ackermann",
          "works": 10
        },
        {
          "name": "John C. Burnett",
          "works": 9
        },
        {
          "name": "Richard R. Lau",
          "works": 8
        },
        {
          "name": "Mary F. Burritt",
          "works": 8
        },
        {
          "name": "Stephen A. Stumpf",
          "works": 7
        },
        {
          "name": "Diane E. Grill",
          "works": 6
        },
        {
          "name": "Stephen M. Colarelli",
          "works": 3
        },
        {
          "name": "Joachim Struck",
          "works": 3
        },
        {
          "name": "Andreas Bergmann",
          "works": 3
        },
        {
          "name": "John E. Ware",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W3156784511",
          "year": 2021,
          "title": "Research Guides: After Graduation-Resources for Social Work Alumni: Open Access Social Work Journals",
          "type": "libguides",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Research in Social Sciences",
            "Social Work Education and Practice",
            "Adolescent and Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W3160732077",
          "year": 2021,
          "title": "Research Guides: After Graduation-Resources for Social Work Alumni: Open Access Tools",
          "type": "libguides",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W3143643549",
          "year": 2021,
          "title": "Research Guides: Women and Health (10:832:415:01): Useful Websites...A Sampling",
          "type": "libguides",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Mobile Health and mHealth Applications",
            "Focus Groups and Qualitative Methods"
          ]
        },
        {
          "openalex_id": "W3200418488",
          "year": 2020,
          "title": "Research Guides: Social Work Practice II-Intensive Weekend Program (19:910:501): Getting Started",
          "type": "libguides",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Homelessness and Social Issues"
          ]
        },
        {
          "openalex_id": "W3044471096",
          "year": 2020,
          "title": "Research Guides: Social Work Practice II-Intensive Weekend Program (19:910:501): Government Reports",
          "type": "libguides",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Homelessness and Social Issues"
          ]
        },
        {
          "openalex_id": "W2969472648",
          "year": 2019,
          "title": "Research Guides: Social Welfare Policy and Services I (19:910:504): Home",
          "type": "libguides",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Social Policy and Reform Studies",
            "Healthcare innovation and challenges"
          ]
        },
        {
          "openalex_id": "W2386425682",
          "year": 1971,
          "title": "Lipoprotein Phenotyping—The “Mail-In Lesion”",
          "type": "article",
          "venue": "Laboratory Medicine",
          "cited_by_count": 3,
          "topics": [
            "Cerebrovascular and Carotid Artery Diseases",
            "Lipoproteins and Cardiovascular Health"
          ]
        },
        {
          "openalex_id": "W2793220377",
          "year": 1976,
          "title": "An annotated bibliography on proton affinities",
          "type": "report",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Solar and Space Plasma Dynamics",
            "Dark Matter and Cosmic Phenomena",
            "Atomic and Molecular Physics"
          ]
        },
        {
          "openalex_id": "W1997889746",
          "year": 1976,
          "title": "Social Processes and Psychiatric Symptom Pattern Change: Wallace Revisited",
          "type": "article",
          "venue": "Human Organization",
          "cited_by_count": 1,
          "topics": [
            "Mental Health and Psychiatry",
            "Mental Health Treatment and Access",
            "Community Health and Development"
          ]
        },
        {
          "openalex_id": "W251173677",
          "year": 1977,
          "title": "How Do I Teach in a Future-Shocked World?.",
          "type": "article",
          "venue": "Young children",
          "cited_by_count": 0,
          "topics": [
            "Education and Critical Thinking Development"
          ]
        },
        {
          "openalex_id": "W1978698499",
          "year": 1983,
          "title": "Development of the Career Exploration Survey (CES)",
          "type": "article",
          "venue": "Journal of Vocational Behavior",
          "cited_by_count": 619,
          "topics": [
            "Cognitive and psychological constructs research",
            "Retirement, Disability, and Employment",
            "Career Development and Diversity"
          ]
        },
        {
          "openalex_id": "W1989490528",
          "year": 1990,
          "title": "Development and Change of Young Adults' Preventive Health Beliefs and Behavior: Influence from Parents and Peers",
          "type": "article",
          "venue": "Journal of Health and Social Behavior",
          "cited_by_count": 515,
          "topics": [
            "Behavioral Health and Interventions",
            "Environmental Education and Sustainability",
            "Youth Development and Social Support"
          ]
        },
        {
          "openalex_id": "W2099135990",
          "year": 1983,
          "title": "Common sense representations of common illnesses.",
          "type": "article",
          "venue": "Health Psychology",
          "cited_by_count": 308,
          "topics": [
            "Mental Health Research Topics",
            "Mental Health and Psychiatry",
            "Behavioral Health and Interventions"
          ]
        },
        {
          "openalex_id": "W2074187643",
          "year": 1986,
          "title": "Health as a value: Methodological and theoretical considerations.",
          "type": "article",
          "venue": "Health Psychology",
          "cited_by_count": 254,
          "topics": [
            "Mental Health and Psychiatry",
            "Behavioral Health and Interventions",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W2031710720",
          "year": 1984,
          "title": "Individual Exploration to Organizational Commitment or Withdrawal.",
          "type": "article",
          "venue": "Academy of Management Journal",
          "cited_by_count": 252,
          "topics": [
            "Job Satisfaction and Organizational Behavior",
            "Psychological Well-being and Life Satisfaction",
            "Career Development and Diversity"
          ]
        },
        {
          "openalex_id": "W2031592890",
          "year": 1987,
          "title": "Self-efficacy expectations and coping with career-related events",
          "type": "article",
          "venue": "Journal of Vocational Behavior",
          "cited_by_count": 220,
          "topics": [
            "Career Development and Diversity",
            "Job Satisfaction and Organizational Behavior",
            "Higher Education Research Studies"
          ]
        },
        {
          "openalex_id": "W4234213313",
          "year": 1986,
          "title": "Health as a value: Methodological and theoretical considerations.",
          "type": "article",
          "venue": "Health Psychology",
          "cited_by_count": 215,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2090218977",
          "year": 1989,
          "title": "Further explorations of common-sense representations of common illnesses.",
          "type": "article",
          "venue": "Health Psychology",
          "cited_by_count": 192,
          "topics": [
            "Behavioral Health and Interventions",
            "Social and Intergroup Psychology",
            "Psychology of Moral and Emotional Judgment"
          ]
        }
      ]
    }
  },
  {
    "name": "John Yfantopoulos",
    "member_affiliation": "University of Athens",
    "is_member": true,
    "projects": [
      {
        "project_id": "1710-VS",
        "title": "Valuation of the EQ-5D-5L in Greece",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5050078092",
      "display_name": "John Yfantopoulos",
      "orcid": "0000-0003-0424-6887",
      "reported_affiliation": "National and Kapodistrian University of Athens",
      "works_count": 125,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 41
        },
        {
          "topic": "Global Health Care Issues",
          "works": 22
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 18
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 15
        },
        {
          "topic": "Employment and Welfare Studies",
          "works": 12
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 12
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 9
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 7
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 7
        },
        {
          "topic": "Dental Health and Care Utilization",
          "works": 6
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 5
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Athanasios Chantzaras",
          "works": 26
        },
        {
          "name": "Guenka Petrova",
          "works": 7
        },
        {
          "name": "Dimitris Niakas",
          "works": 6
        },
        {
          "name": "Steven Simoens",
          "works": 6
        },
        {
          "name": "Constantine Oulis",
          "works": 6
        },
        {
          "name": "A. Constantopoulos",
          "works": 6
        },
        {
          "name": "Dimitra Latsou",
          "works": 6
        },
        {
          "name": "Nick Kontodimopoulos",
          "works": 5
        },
        {
          "name": "Brian Godman",
          "works": 5
        },
        {
          "name": "Patricia Vella Bonanno",
          "works": 5
        },
        {
          "name": "Antony P. Martin",
          "works": 5
        },
        {
          "name": "Jolanta Gulbinovič",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4417050793",
          "year": 2025,
          "title": "Cost-Effectiveness of Positron Emission Tomography/Computed Tomography (PET/CT) in the Initial N-Staging of Head–Neck Cancer and Comparison with CT and Magnetic Resonance Imaging (MRI)",
          "type": "article",
          "venue": "Current Oncology",
          "cited_by_count": 0,
          "topics": [
            "Head and Neck Cancer Studies",
            "Lung Cancer Diagnosis and Treatment",
            "Advances in Oncology and Radiotherapy"
          ]
        },
        {
          "openalex_id": "W4407729211",
          "year": 2025,
          "title": "Determinants of medication adherence in patients with diabetes, hypertension, and hyperlipidemia",
          "type": "article",
          "venue": "HORMONES",
          "cited_by_count": 13,
          "topics": [
            "Medication Adherence and Compliance",
            "Mobile Health and mHealth Applications",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W4409886001",
          "year": 2025,
          "title": "Expert review of pharmacoeconomics and outcomes research: high impact articles from 2024",
          "type": "editorial",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W4408996630",
          "year": 2025,
          "title": "Sustainability of Public Social Spending: Asymmetric Effects and Financialization",
          "type": "article",
          "venue": "Sustainability",
          "cited_by_count": 0,
          "topics": [
            "Fiscal Policy and Economic Growth",
            "Fiscal Policies and Political Economy",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4412750238",
          "year": 2025,
          "title": "The economics of prevention and quality of care: policy insights from the EU’s COVID-19 response",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Public Health Policies and Education",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4411864908",
          "year": 2025,
          "title": "Unmet healthcare needs among older Europeans: trends, determinants, and the role of public health expenditure",
          "type": "article",
          "venue": "Journal of Public Health",
          "cited_by_count": 0,
          "topics": [
            "Global Health Care Issues",
            "Health disparities and outcomes",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W2091702793",
          "year": 1980,
          "title": "Fixed proportion production models for hospitals",
          "type": "article",
          "venue": "Socio-Economic Planning Sciences",
          "cited_by_count": 3,
          "topics": [
            "Operations Management Techniques"
          ]
        },
        {
          "openalex_id": "W2411029767",
          "year": 1984,
          "title": "Socio-economic factors and school health education in Greece.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 3,
          "topics": [
            "School Health and Nursing Education"
          ]
        },
        {
          "openalex_id": "W54916207",
          "year": 1986,
          "title": "Visual Impairment in Greece: Health Service Organization",
          "type": "book-chapter",
          "venue": "Documenta ophthalmologica. Proceedings series",
          "cited_by_count": 0,
          "topics": [
            "Global Health Care Issues",
            "Ergonomics and Musculoskeletal Disorders",
            "Global Healthcare and Medical Tourism"
          ]
        },
        {
          "openalex_id": "W2406002245",
          "year": 1988,
          "title": "Kirlian photography--a tool in the diagnosing of psychopathology.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Mental Health and Psychiatry",
            "Psychotherapy Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W2113197765",
          "year": 2008,
          "title": "Validity of the EuroQoL (EQ-5D) Instrument in a Greek General Population",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 172,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W2899026268",
          "year": 2018,
          "title": "Barriers for Access to New Medicines: Searching for the Balance Between Rising Costs and Limited Budgets",
          "type": "article",
          "venue": "Frontiers in Public Health",
          "cited_by_count": 163,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2419656437",
          "year": 2016,
          "title": "Validation and comparison of the psychometric properties of the EQ-5D-3L and EQ-5D-5L instruments in Greece",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 79,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W3128444525",
          "year": 2021,
          "title": "Potential approaches for the pricing of cancer medicines across Europe to enhance the sustainability of healthcare systems and the implications",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 74,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W3198651120",
          "year": 2021,
          "title": "Health-related quality of life and mental well-being of healthy and diseased persons in 8 countries: Does stringency of government response against early COVID-19 matter?",
          "type": "article",
          "venue": "SSM - Population Health",
          "cited_by_count": 66,
          "topics": [
            "COVID-19 and Mental Health",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W2608039316",
          "year": 2017,
          "title": "Efficiency and productivity assessment of public hospitals in Greece during the crisis period 2009–2012",
          "type": "article",
          "venue": "Cost Effectiveness and Resource Allocation",
          "cited_by_count": 59,
          "topics": [
            "Efficiency Analysis Using DEA",
            "Healthcare Policy and Management",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W2154772807",
          "year": 2012,
          "title": "Validation of a Greek version of the oral health impact profile (OHIP-14) for use among adults",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 56,
          "topics": [
            "Dental Health and Care Utilization",
            "Health, psychology, and well-being",
            "Oral microbiology and periodontitis research"
          ]
        },
        {
          "openalex_id": "W2615103550",
          "year": 2017,
          "title": "Assessment of the psychometric properties of the EQ-5D-3L and EQ-5D-5L instruments in psoriasis",
          "type": "article",
          "venue": "Archives of Dermatological Research",
          "cited_by_count": 53,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical industry and healthcare",
            "Psoriasis: Treatment and Pathogenesis"
          ]
        }
      ]
    }
  },
  {
    "name": "Jose Luis Pinto-Prades",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2015210",
        "title": "Reducing biases in adaptive Time Trade-Off using non-transparent methods",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5017788431",
      "display_name": "José Luis Pinto Prades",
      "orcid": "0000-0002-9684-3410",
      "reported_affiliation": "Universidad de Navarra",
      "works_count": 171,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 121
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 78
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 41
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 40
        },
        {
          "topic": "Global Health Care Issues",
          "works": 31
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 10
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 8
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 4
        },
        {
          "topic": "Traffic and Road Safety",
          "works": 4
        },
        {
          "topic": "Experimental Behavioral Economics Studies",
          "works": 4
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 3
        },
        {
          "topic": "Housing Market and Economics",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Han Bleichrodt",
          "works": 20
        },
        {
          "name": "José‐María Abellán‐Perpiñán",
          "works": 20
        },
        {
          "name": "Eva Rodríguez",
          "works": 14
        },
        {
          "name": "Fernando Ignacio Sánchez Martínez",
          "works": 12
        },
        {
          "name": "José María Abellán Perpiñán",
          "works": 12
        },
        {
          "name": "Werner Brouwer",
          "works": 11
        },
        {
          "name": "Graham Loomes",
          "works": 10
        },
        {
          "name": "Arthur E. Attema",
          "works": 10
        },
        {
          "name": "Jaume Puig‐Junoy",
          "works": 9
        },
        {
          "name": "José Antonio Sacristán",
          "works": 8
        },
        {
          "name": "Jorge Eduardo Martínez Pérez",
          "works": 8
        },
        {
          "name": "Fernando Antoñanzas",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4411119925",
          "year": 2025,
          "title": "Can reference-dependent loss aversion explain choice behaviour?",
          "type": "article",
          "venue": "Journal of Behavioral and Experimental Economics",
          "cited_by_count": 1,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Economic and Environmental Valuation",
            "Forecasting Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W4398248688",
          "year": 2024,
          "title": "A Feasible Estimation of a “Corrected” EQ-5D Social Tariff",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4388569323",
          "year": 2023,
          "title": "Testing Nonmonotonicity in Health Preferences",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 2,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Genetics, Aging, and Longevity in Model Organisms"
          ]
        },
        {
          "openalex_id": "W4290612537",
          "year": 2022,
          "title": "Editorial: Behavioral and experimental health economics",
          "type": "editorial",
          "venue": "Frontiers in Health Services",
          "cited_by_count": 0,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4304891067",
          "year": 2022,
          "title": "QALY Maximization and the Social Optimum",
          "type": "article",
          "venue": "Revista Hacienda Pública Española",
          "cited_by_count": 1,
          "topics": [
            "Global Health Care Issues",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4294558865",
          "year": 2022,
          "title": "Reference‐dependent age weighting of quality‐adjusted life years",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 9,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Optimism, Hope, and Well-being",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2157536439",
          "year": 1980,
          "title": "Medicare utilization in the United States: PSRO and regional impacts.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 10,
          "topics": [
            "Healthcare Policy and Management",
            "Global Health Care Issues",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W78364117",
          "year": 1988,
          "title": "Evolución del coste de la educación en España 1954-1980",
          "type": "article",
          "venue": "Estadística española/Estadística española",
          "cited_by_count": 0,
          "topics": [
            "History of Education in Spain"
          ]
        },
        {
          "openalex_id": "W179277927",
          "year": 1988,
          "title": "Un índice del coste de la educación española",
          "type": "article",
          "venue": "Revista Española de Pedagogía",
          "cited_by_count": 0,
          "topics": [
            "Educational Practices and Policies"
          ]
        },
        {
          "openalex_id": "W194293591",
          "year": 1990,
          "title": "Medida de la contribución de la educación al crecimiento en España: 1964-86",
          "type": "article",
          "venue": "Información Comercial Española, ICE: Revista de economía",
          "cited_by_count": 0,
          "topics": [
            "Intergenerational and Educational Inequality Studies"
          ]
        },
        {
          "openalex_id": "W1980339486",
          "year": 2000,
          "title": "A Parameter-Free Elicitation of the Probability Weighting Function in Medical Decision Analysis",
          "type": "article",
          "venue": "Management Science",
          "cited_by_count": 498,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2115094990",
          "year": 1999,
          "title": "Incorporating societal concerns for fairness in numerical valuations of health programmes",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 402,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2129087050",
          "year": 2001,
          "title": "Making Descriptive Use of Prospect Theory to Improve the Prescriptive Use of Expected Utility",
          "type": "article",
          "venue": "Management Science",
          "cited_by_count": 329,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2155540139",
          "year": 2010,
          "title": "Weighting and valuing quality-adjusted life-years using stated preference methods: preliminary results from the Social Value of a QALY Project",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 277,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2772302443",
          "year": 2017,
          "title": "Handling Data Quality Issues to Estimate the Spanish EQ-5D-5L Value Set Using a Hybrid Interval Regression Approach",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 246,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2326661655",
          "year": 2015,
          "title": "Valuation and Modeling of EQ-5D-5L Health States Using a Hybrid Approach",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 154,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W1985075012",
          "year": 1999,
          "title": "Toward a Broader View of Values in Cost-Effectiveness Analysis of Health",
          "type": "article",
          "venue": "The Hastings Center Report",
          "cited_by_count": 125,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2153652510",
          "year": 2009,
          "title": "Trying to estimate a monetary value for the QALY",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 107,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics",
            "Economic and Environmental Valuation"
          ]
        }
      ]
    }
  },
  {
    "name": "Josephine Walker",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1732-VS",
        "title": "EQ-5D-3L valuation study with crosswalk to EQ-5D-5L in Georgia",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5038317615",
      "display_name": "Josephine G. Walker",
      "orcid": "0000-0002-9732-5738",
      "reported_affiliation": "At Bristol",
      "works_count": 164,
      "top_topics": [
        {
          "topic": "Hepatitis C virus research",
          "works": 63
        },
        {
          "topic": "Hepatitis B Virus Studies",
          "works": 43
        },
        {
          "topic": "HIV, Drug Use, Sexual Risk",
          "works": 38
        },
        {
          "topic": "Liver Disease Diagnosis and Treatment",
          "works": 18
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 15
        },
        {
          "topic": "Sex work and related issues",
          "works": 13
        },
        {
          "topic": "COVID-19 epidemiological studies",
          "works": 10
        },
        {
          "topic": "Parasite Biology and Host Interactions",
          "works": 9
        },
        {
          "topic": "Liver Diseases and Immunity",
          "works": 9
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 8
        },
        {
          "topic": "Hepatitis Viruses Studies and Epidemiology",
          "works": 8
        },
        {
          "topic": "Homelessness and Social Issues",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Peter Vickerman",
          "works": 92
        },
        {
          "name": "Aaron G. Lim",
          "works": 38
        },
        {
          "name": "Adam Trickey",
          "works": 31
        },
        {
          "name": "Jack Stone",
          "works": 25
        },
        {
          "name": "Hannah Fraser",
          "works": 24
        },
        {
          "name": "Matthew Hickman",
          "works": 24
        },
        {
          "name": "Natasha K. Martin",
          "works": 16
        },
        {
          "name": "Niklas Luhmann",
          "works": 13
        },
        {
          "name": "Nyashadzaishe Mafirakureva",
          "works": 13
        },
        {
          "name": "Matthew J. Akiyama",
          "works": 13
        },
        {
          "name": "Lucy Platt",
          "works": 12
        },
        {
          "name": "Eric R. Morgan",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7130628950",
          "year": 2026,
          "title": "A non-randomised trial of a hepatitis C same-day test and treat model using antibody test only for people who inject drugs in Armenia, Georgia, and Tanzania:a CUTTS HepC study protocol",
          "type": "article",
          "venue": "Bristol Research (University of Bristol)",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis C virus research",
            "Hepatitis B Virus Studies",
            "Biosimilars and Bioanalytical Methods"
          ]
        },
        {
          "openalex_id": "W7150970641",
          "year": 2026,
          "title": "Correction: Hepatitis C virus cascade of care among adults in Sindh province, Pakistan: Findings from 2019–2020 household sero-survey",
          "type": "erratum",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis C virus research",
            "Hepatitis B Virus Studies",
            "Blood donation and transfusion practices"
          ]
        },
        {
          "openalex_id": "W7160806872",
          "year": 2026,
          "title": "Cost-effectiveness of emergency department opt-out testing for HIV in England: a modelling study",
          "type": "article",
          "venue": "Bristol Research (University of Bristol)",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "Pneumocystis jirovecii pneumonia detection and treatment",
            "HIV Research and Treatment"
          ]
        },
        {
          "openalex_id": "W7165899638",
          "year": 2026,
          "title": "Cost-effectiveness of emergency department opt-out testing for HIV in England: a modelling study",
          "type": "article",
          "venue": "The Lancet HIV",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV/AIDS Impact and Responses",
            "Tuberculosis Research and Epidemiology"
          ]
        },
        {
          "openalex_id": "W7135014305",
          "year": 2026,
          "title": "Delivering Effective Hepatitis C Virus Treatment in an Embedded Primary Care Setting Within a Tertiary Care Hospital in Karachi, Pakistan",
          "type": "article",
          "venue": "Journal of Viral Hepatitis",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis C virus research",
            "Diabetes Management and Education",
            "Hepatitis B Virus Studies"
          ]
        },
        {
          "openalex_id": "W7131323627",
          "year": 2026,
          "title": "Delivering effective hepatitis C virus treatment in an embedded primary care setting within a tertiary care hospital in Karachi, Pakistan",
          "type": "article",
          "venue": "Bristol Research (University of Bristol)",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis C virus research",
            "Hepatitis B Virus Studies",
            "Hepatitis Viruses Studies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W1548662200",
          "year": 1925,
          "title": "Bibliography of science teaching in secondary schools",
          "type": "paratext",
          "venue": "Medical Entomology and Zoology",
          "cited_by_count": 2,
          "topics": [
            "Science Education and Pedagogy"
          ]
        },
        {
          "openalex_id": "W2007256851",
          "year": 1962,
          "title": "The use of Haemodialysis in Acute Renal Failure and Overhydration in Children",
          "type": "article",
          "venue": "Archives of Disease in Childhood",
          "cited_by_count": 9,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Muscle and Compartmental Disorders",
            "Central Venous Catheters and Hemodialysis"
          ]
        },
        {
          "openalex_id": "W2330378284",
          "year": 1963,
          "title": "Measurement of Renal Red Cell and Plasma Transit Times in Acute Renal Failure",
          "type": "article",
          "venue": "Experimental Biology and Medicine",
          "cited_by_count": 18,
          "topics": [
            "Acute Kidney Injury Research",
            "Chronic Kidney Disease and Diabetes",
            "Dialysis and Renal Disease Management"
          ]
        },
        {
          "openalex_id": "W2116539314",
          "year": 1963,
          "title": "Renal Blood Flow in Acute Renal Failure Measured by Renal Arterial Infusion of Indocyanine Green",
          "type": "article",
          "venue": "Experimental Biology and Medicine",
          "cited_by_count": 25,
          "topics": [
            "Acute Kidney Injury Research",
            "Renal and Vascular Pathologies",
            "Hemodynamic Monitoring and Therapy"
          ]
        },
        {
          "openalex_id": "W3857228",
          "year": 1966,
          "title": "Tissue antibodies in primary biliary cirrhosis, active chronic (lupoid) hepatitis, cryptogenic cirrhosis and other liver diseases and their clinical implications.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 414,
          "topics": [
            "Liver Disease Diagnosis and Treatment",
            "Liver Diseases and Immunity",
            "Drug-Induced Hepatotoxicity and Protection"
          ]
        },
        {
          "openalex_id": "W2341020717",
          "year": 1966,
          "title": "Arterial Changes in the Lungs in Cirrhosis of the Liver — Lung Spider Nevi",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 356,
          "topics": [
            "Medical Imaging and Pathology Studies",
            "Hypertrophic osteoarthropathy and related conditions",
            "Genetic and Kidney Cyst Diseases"
          ]
        },
        {
          "openalex_id": "W2940255242",
          "year": 2019,
          "title": "The contribution of injection drug use to hepatitis C virus transmission globally, regionally, and at country level: a modelling study",
          "type": "article",
          "venue": "The Lancet. Gastroenterology & hepatology",
          "cited_by_count": 249,
          "topics": [
            "Hepatitis C virus research",
            "HIV, Drug Use, Sexual Risk",
            "Hepatitis B Virus Studies"
          ]
        },
        {
          "openalex_id": "W2884203623",
          "year": 2018,
          "title": "Incarceration history and risk of HIV and hepatitis C virus acquisition among people who inject drugs: a systematic review and meta-analysis",
          "type": "review",
          "venue": "The Lancet Infectious Diseases",
          "cited_by_count": 229,
          "topics": [
            "HIV, Drug Use, Sexual Risk",
            "Criminal Justice and Corrections Analysis",
            "Hepatitis C virus research"
          ]
        },
        {
          "openalex_id": "W3119473535",
          "year": 2021,
          "title": "Homelessness, unstable housing, and risk of HIV and hepatitis C virus acquisition among people who inject drugs: a systematic review and meta-analysis",
          "type": "review",
          "venue": "The Lancet Public Health",
          "cited_by_count": 212,
          "topics": [
            "HIV, Drug Use, Sexual Risk",
            "Homelessness and Social Issues",
            "Hepatitis C virus research"
          ]
        },
        {
          "openalex_id": "W2159270737",
          "year": 1968,
          "title": "STUDIES ON THE CONTROL OF ANTIBODY SYNTHESIS",
          "type": "article",
          "venue": "The Journal of Experimental Medicine",
          "cited_by_count": 159,
          "topics": [
            "Monoclonal and Polyclonal Antibodies Research",
            "Viral Infectious Diseases and Gene Expression in Insects",
            "Protein purification and stability"
          ]
        },
        {
          "openalex_id": "W2014877638",
          "year": 1966,
          "title": "COMPLICATIONS OF DIURETIC THERAPY IN HEPATIC CIRRHOSIS",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 154,
          "topics": [
            "Liver Disease Diagnosis and Treatment",
            "Liver Disease and Transplantation",
            "Drug-Induced Hepatotoxicity and Protection"
          ]
        },
        {
          "openalex_id": "W1964469575",
          "year": 1969,
          "title": "A UNIFIED CONCEPT OF AUTOIMMUNE HEPATITIS",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 150,
          "topics": [
            "Liver Diseases and Immunity",
            "Liver Disease Diagnosis and Treatment",
            "Liver physiology and pathology"
          ]
        }
      ]
    }
  }
]
