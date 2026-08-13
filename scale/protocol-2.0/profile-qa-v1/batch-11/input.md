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
    "name": "Ciaran O'Neill",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2013280",
        "title": "An Irish valuation study for the EQ-5D-5L",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5016414995",
      "display_name": "Ciarán O’Neill",
      "orcid": "0000-0001-7668-3934",
      "reported_affiliation": "Queen's University Belfast",
      "works_count": 306,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 48
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 37
        },
        {
          "topic": "Global Health Care Issues",
          "works": 31
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 29
        },
        {
          "topic": "Dental Health and Care Utilization",
          "works": 25
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 20
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 19
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 17
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 13
        },
        {
          "topic": "Health Promotion and Cardiovascular Prevention",
          "works": 11
        },
        {
          "topic": "Chronic Kidney Disease and Diabetes",
          "works": 10
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 10
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Michael Donnelly",
          "works": 43
        },
        {
          "name": "Luke E. Barry",
          "works": 24
        },
        {
          "name": "Linda Sharp",
          "works": 23
        },
        {
          "name": "Frank Kee",
          "works": 19
        },
        {
          "name": "Tran Thu Ngan",
          "works": 19
        },
        {
          "name": "Edel Doherty",
          "works": 19
        },
        {
          "name": "Alexander P. Maxwell",
          "works": 18
        },
        {
          "name": "Gerald McKenna",
          "works": 16
        },
        {
          "name": "Liam G. Heaney",
          "works": 13
        },
        {
          "name": "Chris R. Cardwell",
          "works": 12
        },
        {
          "name": "Paul Brocklehurst",
          "works": 12
        },
        {
          "name": "Michael Donaldson",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7170090265",
          "year": 2026,
          "title": "Using Role Substitution to Improve Oral Health of Dependent Older People Residing in Care Homes and Assisted Living Settings in the United Kingdom",
          "type": "article",
          "venue": "Community Dentistry And Oral Epidemiology",
          "cited_by_count": 0,
          "topics": [
            "Dental Health and Care Utilization",
            "Fluoride Effects and Removal",
            "Oral microbiology and periodontitis research"
          ]
        },
        {
          "openalex_id": "W4412639186",
          "year": 2025,
          "title": "1The Radical Potential of Public History in Global Perspective",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Digital Humanities and Scholarship",
            "Libraries and Information Services"
          ]
        },
        {
          "openalex_id": "W4417236853",
          "year": 2025,
          "title": "3. Trinity’s Colonial Legacies: Transparency, Instrumentality and Agency in an Engaged Research Project",
          "type": "book-chapter",
          "venue": "Edinburgh University Press eBooks",
          "cited_by_count": 1,
          "topics": [
            "Christian Theology and Mission",
            "Theological Perspectives and Practices",
            "Pentecostalism and Christianity Studies"
          ]
        },
        {
          "openalex_id": "W4407630154",
          "year": 2025,
          "title": "A Taxonomy for Assessing Whether HRQoL Value Sets Are Obsolete",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4406480886",
          "year": 2025,
          "title": "A Theoretically Informed Process Evaluation in Parallel to a Feasibility Study of a Complex Oral Health Intervention Using <scp>NICE</scp> Guidelines in a Care Home Setting",
          "type": "article",
          "venue": "Community Dentistry And Oral Epidemiology",
          "cited_by_count": 7,
          "topics": [
            "Dental Health and Care Utilization",
            "Health Policy Implementation Science",
            "Interprofessional Education and Collaboration"
          ]
        },
        {
          "openalex_id": "W4411956929",
          "year": 2025,
          "title": "A feasibility study of the costs and consequences of improving the oral health of older people in care homes: findings from the TOPIC study",
          "type": "article",
          "venue": "BMC Oral Health",
          "cited_by_count": 3,
          "topics": [
            "Dental Health and Care Utilization",
            "Geriatric Care and Nursing Homes",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W2080562996",
          "year": 1991,
          "title": "ALTERNATIVE DEFINITIONS OF DEMAND FOR RECREATIONAL ANGLING IN NORTHERN IRELAND",
          "type": "article",
          "venue": "Journal of Agricultural Economics",
          "cited_by_count": 13,
          "topics": [
            "Economic and Environmental Valuation",
            "Urban Transport and Accessibility",
            "Transportation Planning and Optimization"
          ]
        },
        {
          "openalex_id": "W2108233326",
          "year": 1992,
          "title": "DISCRETE‐CHOICE VALUATION OF RECREATIONAL ANGLING IN NORTHERN IRELAND",
          "type": "article",
          "venue": "Journal of Agricultural Economics",
          "cited_by_count": 16,
          "topics": [
            "Economic and Environmental Valuation",
            "Recreation, Leisure, Wilderness Management",
            "Forest Management and Policy"
          ]
        },
        {
          "openalex_id": "W2079468443",
          "year": 1995,
          "title": "Strategies for reducing coronary risk factors in primary care: which is most cost effective?",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 89,
          "topics": [
            "Health Promotion and Cardiovascular Prevention",
            "Lipoproteins and Cardiovascular Health",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W2072999437",
          "year": 1996,
          "title": "A comparison of three measures of perceived distress: results from a study of angina patients in general practice in Northern Ireland.",
          "type": "article",
          "venue": "Journal of Epidemiology & Community Health",
          "cited_by_count": 7,
          "topics": [
            "Cardiac Health and Mental Health",
            "Diabetes Management and Education",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W2077024838",
          "year": 2014,
          "title": "The direct and indirect costs of both overweight and obesity: a systematic review",
          "type": "review",
          "venue": "BMC Research Notes",
          "cited_by_count": 319,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Obesity, Physical Activity, Diet",
            "Obesity and Health Practices"
          ]
        },
        {
          "openalex_id": "W3012813218",
          "year": 2020,
          "title": "The impact of chronic kidney disease on developed countries from a health economics perspective: A systematic scoping review",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 240,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Chronic Kidney Disease and Diabetes",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2171124311",
          "year": 2014,
          "title": "The cost of treating severe refractory asthma in the UK: an economic analysis from the British Thoracic Society Difficult Asthma Registry",
          "type": "article",
          "venue": "Thorax",
          "cited_by_count": 184,
          "topics": [
            "Asthma and respiratory diseases",
            "Eosinophilic Esophagitis"
          ]
        },
        {
          "openalex_id": "W2111319723",
          "year": 2004,
          "title": "Comparison of five antimicrobial regimens for treatment of mild to moderate inflammatory facial acne vulgaris in the community: randomised controlled trial",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 168,
          "topics": [
            "Acne and Rosacea Treatments and Effects",
            "Dermatology and Skin Diseases",
            "Dermatologic Treatments and Research"
          ]
        },
        {
          "openalex_id": "W3158039857",
          "year": 2021,
          "title": "Securing a sustainable and fit-for-purpose UK health and care workforce",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 154,
          "topics": [
            "Global Health Workforce Issues",
            "Primary Care and Health Outcomes",
            "Healthcare Systems and Challenges"
          ]
        },
        {
          "openalex_id": "W2990409567",
          "year": 2019,
          "title": "Dental caries following radiotherapy for head and neck cancer: A systematic review",
          "type": "review",
          "venue": "Oral Oncology",
          "cited_by_count": 148,
          "topics": [
            "Oral health in cancer treatment",
            "Head and Neck Cancer Studies",
            "Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2883323624",
          "year": 2018,
          "title": "Effect of providing near glasses on productivity among rural Indian tea workers with presbyopia (PROSPER): a randomised trial",
          "type": "article",
          "venue": "The Lancet Global Health",
          "cited_by_count": 144,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Ergonomics and Musculoskeletal Disorders",
            "Spatial Neglect and Hemispheric Dysfunction"
          ]
        },
        {
          "openalex_id": "W2339371375",
          "year": 2015,
          "title": "United Kingdom: Health System Review.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 143,
          "topics": [
            "Global Health Care Issues",
            "Healthcare Policy and Management",
            "Health Services Management and Policy"
          ]
        }
      ]
    }
  },
  {
    "name": "Claire Gudex",
    "member_affiliation": "University of Southern Denmark",
    "is_member": true,
    "projects": [
      {
        "project_id": "20170400",
        "title": "Deriving EQ-5D-5L preference weights for Denmark",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5047944478",
      "display_name": "Claire Gudex",
      "orcid": "0000-0003-3881-9890",
      "reported_affiliation": "University of Southern Denmark",
      "works_count": 125,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 35
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 15
        },
        {
          "topic": "Global Health Care Issues",
          "works": 12
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 12
        },
        {
          "topic": "Eating Disorders and Behaviors",
          "works": 9
        },
        {
          "topic": "Education, Healthcare and Sociology Research",
          "works": 8
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 6
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 5
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 4
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
          "topic": "Bariatric Surgery and Outcomes",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Paul Kind",
          "works": 13
        },
        {
          "name": "Jan Sørensen",
          "works": 10
        },
        {
          "name": "Kjeld Møller Pedersen",
          "works": 10
        },
        {
          "name": "René Klinkby Støving",
          "works": 9
        },
        {
          "name": "Mia Beck Lichtenstein",
          "works": 8
        },
        {
          "name": "Paul Dolan",
          "works": 7
        },
        {
          "name": "Charlotte P. Horsted",
          "works": 7
        },
        {
          "name": "Fuad Lechín",
          "works": 7
        },
        {
          "name": "Alan Williams",
          "works": 6
        },
        {
          "name": "Per Bech",
          "works": 6
        },
        {
          "name": "Jørgen T. Lauridsen",
          "works": 6
        },
        {
          "name": "Cathrine Elgaard Jensen",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7153616249",
          "year": 2026,
          "title": "Translation and pilot-testing of the ReSPECT (Recommended Summary Plan for Emergency Care and Treatment) form into Danish",
          "type": "article",
          "venue": "Resuscitation Plus",
          "cited_by_count": 0,
          "topics": [
            "Trauma and Emergency Care Studies",
            "Cardiac Arrest and Resuscitation",
            "Interpreting and Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4411316975",
          "year": 2025,
          "title": "Optimal DCE design for modelling nonlinear time preferences in EQ-5D-5L valuation studies: exploration of data from Denmark and Peru",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 2,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4412386832",
          "year": 2025,
          "title": "Patients’ Assessment of Transitions in Healthcare Settings: Development and Psychometric Analysis of the PATH questionnaire",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Adolescent and Pediatric Healthcare",
            "Primary Care and Health Outcomes",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4411050688",
          "year": 2025,
          "title": "Stability of Danish Population Health Preferences Over Time",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4409785404",
          "year": 2025,
          "title": "Translation and cultural adaptation of the DE-STRESS survey into Danish – Measuring stress, coping, and intention to leave among Emergency department Nurses, Nurse Assistants, and Physicians",
          "type": "article",
          "venue": "International Emergency Nursing",
          "cited_by_count": 0,
          "topics": [
            "Healthcare professionals’ stress and burnout",
            "Nursing education and management",
            "Occupational Health and Burnout"
          ]
        },
        {
          "openalex_id": "W4396915390",
          "year": 2024,
          "title": "Academic English course for the health sciences: evolution towards a flipped classroom",
          "type": "article",
          "venue": "Tidsskriftet Læring og Medier (LOM)",
          "cited_by_count": 0,
          "topics": [
            "Innovative Teaching Methods",
            "Online and Blended Learning",
            "E-Learning and Knowledge Management"
          ]
        },
        {
          "openalex_id": "W1563723520",
          "year": 1986,
          "title": "QALYs and their use by the health service",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 59,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1506592244",
          "year": 1988,
          "title": "The QALY toolkit",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 78,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2416015604",
          "year": 1990,
          "title": "Prioritising waiting lists.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 29,
          "topics": [
            "Healthcare Policy and Management",
            "Cardiac, Anesthesia and Surgical Outcomes"
          ]
        },
        {
          "openalex_id": "W2031427653",
          "year": 1991,
          "title": "Adverse effects of Benzodiazepines",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 54,
          "topics": [
            "Sleep and related disorders",
            "Epilepsy research and treatment",
            "Alcoholism and Thiamine Deficiency"
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
          "openalex_id": "W2081557449",
          "year": 1998,
          "title": "Variations in population health status: results from a United Kingdom national questionnaire survey",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 1069,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W2021402729",
          "year": 1996,
          "title": "The time trade-off method: Results from a general population study",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 700,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W1480287350",
          "year": 1995,
          "title": "A social tariff for EuroQol: results from a UK general population survey",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 614,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1988299889",
          "year": 2010,
          "title": "The WHO (Ten) Well-Being Index: Validation in Diabetes",
          "type": "article",
          "venue": "Psychotherapy and Psychosomatics",
          "cited_by_count": 534,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Diabetes Management and Education",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W2045166904",
          "year": 1996,
          "title": "Valuing health states: A comparison of methods",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 337,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2032763021",
          "year": 2014,
          "title": "From Translation to Version Management: A History and Review of Methods for the Cultural Adaptation of the EuroQol Five-Dimensional Questionnaire",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 283,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Meta-analysis and systematic reviews"
          ]
        }
      ]
    }
  },
  {
    "name": "Clara Mukuria",
    "member_affiliation": "University of Sheffield",
    "is_member": true,
    "projects": [
      {
        "project_id": "1892-RA",
        "title": "Testing the EQ-HWB modifications in a mixed patient population: developing a protocol and generating evidence",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2016240",
        "title": "Assessment of the EQ-5D-5L compared to EQ-5D-3L and generation of population norms in England",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20190310",
        "title": "Extending the QALY Valuation Study in England",
        "working_group": "Valuation"
      },
      {
        "project_id": "2217-TR",
        "title": "Translation of EQ-HWB-9 10 most commonly requested languages",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2234-TVG",
        "title": "EQ-5D-5L UK Valuation Educational Session - HESG Summer 2025",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "326-RA",
        "title": "A feasibility study of applying PAPRIKA to the EQ-HWB",
        "working_group": "Valuation, EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5043083823",
      "display_name": "Clara Mukuria",
      "orcid": "0000-0003-4318-1481",
      "reported_affiliation": "University of Sheffield",
      "works_count": 128,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 90
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 30
        },
        {
          "topic": "Global Health Care Issues",
          "works": 12
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 11
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 9
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 9
        },
        {
          "topic": "Health Education and Validation",
          "works": 7
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 7
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 7
        },
        {
          "topic": "Cystic Fibrosis Research Advances",
          "works": 7
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 6
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "John Brazier",
          "works": 76
        },
        {
          "name": "Donna Rowen",
          "works": 57
        },
        {
          "name": "Brendan Mulhern",
          "works": 38
        },
        {
          "name": "Tessa Peasgood",
          "works": 30
        },
        {
          "name": "Anju Keetharuth",
          "works": 28
        },
        {
          "name": "Aki Tsuchiya",
          "works": 25
        },
        {
          "name": "Janice Connell",
          "works": 25
        },
        {
          "name": "Louise Longworth",
          "works": 21
        },
        {
          "name": "Yaling Yang",
          "works": 21
        },
        {
          "name": "Tracey Young",
          "works": 20
        },
        {
          "name": "Mónica Hernández Alava",
          "works": 19
        },
        {
          "name": "Michael Barkham",
          "works": 19
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167275189",
          "year": 2026,
          "title": "Content validity of the modified EQ-HWB-9 in a sample of Argentinean patients, informal caregivers, and members of the general public",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W7166114740",
          "year": 2026,
          "title": "PCR9 CONTENT VALIDITY OF THE EQ-HWB-9 IN PATIENTS WITH ADVANCED ILLNESSES: A COGNITIVE DEBRIEFING STUDY",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory Myopathies and Dermatomyositis",
            "Interstitial Lung Diseases and Idiopathic Pulmonary Fibrosis",
            "Lung Cancer Treatments and Mutations"
          ]
        },
        {
          "openalex_id": "W4407944051",
          "year": 2025,
          "title": "Associations between financial toxicity, health-related quality of life, and well-being in Indonesian patients with breast cancer",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 6,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W4413103268",
          "year": 2025,
          "title": "EQ Health and Wellbeing (EQ-HWB): A Psychometric Assessment Across 6 Conditions and the General Population in the United Kingdom",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychological Well-being and Life Satisfaction",
            "Health, psychology, and well-being"
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
          "openalex_id": "W4408218600",
          "year": 2025,
          "title": "Test-retest reliability of the Online Elicitation of Personal Utility Functions (OPUF) approach for valuing the EQ-HWB-S",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W1505724240",
          "year": 2011,
          "title": "An evaluation of a new service model Improving Access to Psychological Therapies",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Digital Mental Health Interventions",
            "Mental Health Treatment and Access",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W7139818085",
          "year": 2011,
          "title": "An evaluation of a new service model Improving Access to Psychological Therapies",
          "type": "report",
          "venue": "Research Explorer (The University of Manchester)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W2184401650",
          "year": 2011,
          "title": "An evaluation of a new service model: Improving Access to Psychological Therapies demonstration sites 2006-2009",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 29,
          "topics": [
            "Mental Health and Patient Involvement",
            "Mental Health Treatment and Access",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W177661295",
          "year": 2011,
          "title": "An evaluation of a new service model: Improving Access to Psychological Therapies demonstration sites 2006-2009, Final Report.",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 25,
          "topics": [
            "Healthcare innovation and challenges"
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
          "openalex_id": "W2065524809",
          "year": 2014,
          "title": "A systematic review, psychometric analysis and qualitative assessment of generic preference-based measures of health in mental health populations and the estimation of mapping functions from widely used specific measures",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 279,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Schizophrenia research and treatment"
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
          "openalex_id": "W2076023694",
          "year": 2014,
          "title": "Using generic preference-based measures in mental health: psychometric validity of the EQ-5D and SF-6D",
          "type": "article",
          "venue": "The British Journal of Psychiatry",
          "cited_by_count": 135,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Schizophrenia research and treatment",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2928936747",
          "year": 2019,
          "title": "An Updated Systematic Review of Studies Mapping (or Cross-Walking) Measures of Health-Related Quality of Life to Generic Preference-Based Measures to Generate Utility Values",
          "type": "review",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 130,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2618633361",
          "year": 2017,
          "title": "What is the evidence for the performance of generic preference-based measures? A systematic overview of reviews",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 123,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Behavioral and Psychological Studies"
          ]
        },
        {
          "openalex_id": "W3093662954",
          "year": 2020,
          "title": "Impact of social prescribing to address loneliness: A mixed methods evaluation of a national social prescribing programme",
          "type": "article",
          "venue": "Health & Social Care in the Community",
          "cited_by_count": 112,
          "topics": [
            "Art Therapy and Mental Health",
            "Health, psychology, and well-being",
            "Community Health and Development"
          ]
        },
        {
          "openalex_id": "W2905944219",
          "year": 2019,
          "title": "Valuing Health State: An EQ-5D-5L Value Set for Ethiopians",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 100,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Delphi Technique in Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Corneliu Bolbocean",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1869-SG",
        "title": "Evaluating the Sensitivity and Validity of EQ-5D-Y-5L in Measuring HRQoL Among Obese and Non-Obese US Children: Insights from the Little Rock Green Schoolyard Initiative",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5018646670",
      "display_name": "Corneliu Bolbocean",
      "orcid": "0000-0001-5782-1844",
      "reported_affiliation": "John Radcliffe Hospital",
      "works_count": 44,
      "top_topics": [
        {
          "topic": "Infant Development and Preterm Care",
          "works": 8
        },
        {
          "topic": "Birth, Development, and Health",
          "works": 8
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 6
        },
        {
          "topic": "Genetics and Neurodevelopmental Disorders",
          "works": 4
        },
        {
          "topic": "Neonatal Respiratory Health Research",
          "works": 4
        },
        {
          "topic": "Autism Spectrum Disorder Research",
          "works": 4
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 4
        },
        {
          "topic": "Early Childhood Education and Development",
          "works": 4
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 3
        },
        {
          "topic": "Child Nutrition and Feeding Issues",
          "works": 3
        },
        {
          "topic": "Neonatal and fetal brain pathology",
          "works": 3
        },
        {
          "topic": "Poverty, Education, and Child Welfare",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Stavros Petrou",
          "works": 8
        },
        {
          "name": "Shelin Adam",
          "works": 5
        },
        {
          "name": "Tanya N. Nelson",
          "works": 5
        },
        {
          "name": "Maria McCormack",
          "works": 5
        },
        {
          "name": "J. Lloyd Holder",
          "works": 5
        },
        {
          "name": "Ilaria Guella",
          "works": 4
        },
        {
          "name": "Marna B. McKenzie",
          "works": 4
        },
        {
          "name": "Mary Connolly",
          "works": 4
        },
        {
          "name": "Matthew J. Farrer",
          "works": 4
        },
        {
          "name": "Michelle Demos",
          "works": 4
        },
        {
          "name": "Clara van Karnebeek",
          "works": 4
        },
        {
          "name": "Cyrus Boelman",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166251231",
          "year": 2026,
          "title": "EE26 PRODUCTIVITY LOSSES AFTER MISCARRIAGE: A PROSPECTIVE COHORT ANALYSIS USING THE IMTA PRODUCTIVITY COST QUESTIONNAIRE",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W7167517344",
          "year": 2026,
          "title": "Latent Class Profiles of Telehealth Modality, Motivation, and Experience: A Cross-Sectional Analysis on Nationally Representative US Survey (Preprint)",
          "type": "preprint",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Mobile Health and mHealth Applications",
            "Literature Analysis and Criticism"
          ]
        },
        {
          "openalex_id": "W7164511826",
          "year": 2026,
          "title": "Miscarriage, self-harm, and psychiatric disorders in first-time pregnant women: Evidence from a linkage study",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 0,
          "topics": [
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Menstrual Health and Disorders",
            "Neuroendocrine regulation and behavior"
          ]
        },
        {
          "openalex_id": "W7166031535",
          "year": 2026,
          "title": "PCR42 ASSOCIATION OF MARIJUANA USE AND HEALTH-RELATED QUALITY OF LIFE AMONG CARDIOVASCULAR DISEASE PATIENTS. EVIDENCE FROM THE BEHAVIORAL RISK FACTOR SURVEILLANCE SYSTEM",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Heart rate and cardiovascular health",
            "Biological Research and Disease Studies",
            "Medical Case Reports and Studies"
          ]
        },
        {
          "openalex_id": "W7126188551",
          "year": 2026,
          "title": "Telehealth Use and Modality Choice Among US Adults: Shorrocks-Shapley Decomposition of a 2022 Cross-Sectional National Survey",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 2,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Mobile Health and mHealth Applications",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4410252785",
          "year": 2025,
          "title": "A heterogeneity analysis of health-related quality of life in early adults born very preterm or very low birthweight across the sociodemographic spectrum",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 4,
          "topics": [
            "Health disparities and outcomes",
            "Infant Development and Preterm Care",
            "Birth, Development, and Health"
          ]
        },
        {
          "openalex_id": "W2274087684",
          "year": 2007,
          "title": "Poverty in Moldova",
          "type": "article",
          "venue": "",
          "cited_by_count": 2,
          "topics": [
            "Global Socioeconomic and Political Dynamics",
            "Russia and Soviet political economy"
          ]
        },
        {
          "openalex_id": "W1570018115",
          "year": 2008,
          "title": "Regional distribution of poverty in Moldova",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Sustainable Development and Environmental Policy",
            "Economic Growth and Productivity",
            "Income, Poverty, and Inequality"
          ]
        },
        {
          "openalex_id": "W45037370",
          "year": 2009,
          "title": "Visible minorities` educational choices in Canada",
          "type": "dissertation",
          "venue": "Summit (Simon Fraser University)",
          "cited_by_count": 0,
          "topics": [
            "Global Educational Policies and Reforms",
            "Education Systems and Policy",
            "School Choice and Performance"
          ]
        },
        {
          "openalex_id": "W2028043880",
          "year": 2012,
          "title": "Cost–effectiveness of rituximab in follicular lymphoma",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 10,
          "topics": [
            "Lymphoma Diagnosis and Treatment",
            "CNS Lymphoma Diagnosis and Treatment",
            "Viral-associated cancers and disorders"
          ]
        },
        {
          "openalex_id": "W2734085560",
          "year": 2017,
          "title": "Loss-of-Function and Gain-of-Function Mutations in KCNQ5 Cause Intellectual Disability or Epileptic Encephalopathy",
          "type": "article",
          "venue": "The American Journal of Human Genetics",
          "cited_by_count": 129,
          "topics": [
            "Cardiac electrophysiology and arrhythmias",
            "Ion channel regulation and function",
            "Neuroscience and Neuropharmacology Research"
          ]
        },
        {
          "openalex_id": "W2952564037",
          "year": 2019,
          "title": "Diagnostic Yield and Treatment Impact of Targeted Exome Sequencing in Early-Onset Epilepsy",
          "type": "article",
          "venue": "Frontiers in Neurology",
          "cited_by_count": 101,
          "topics": [
            "Genomics and Rare Diseases",
            "Genetics and Neurodevelopmental Disorders",
            "Epilepsy research and treatment"
          ]
        },
        {
          "openalex_id": "W2745067258",
          "year": 2017,
          "title": "De Novo Mutations in YWHAG Cause Early-Onset Epilepsy",
          "type": "article",
          "venue": "The American Journal of Human Genetics",
          "cited_by_count": 86,
          "topics": [
            "14-3-3 protein interactions",
            "Macrophage Migration Inhibitory Factor",
            "Ubiquitin and proteasome pathways"
          ]
        },
        {
          "openalex_id": "W2020297058",
          "year": 2014,
          "title": "Resource Utilization and Costs during the Initial Years of Lung Cancer Screening with Computed Tomography in Canada",
          "type": "article",
          "venue": "Journal of Thoracic Oncology",
          "cited_by_count": 51,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Lung Cancer Treatments and Mutations",
            "Lung Cancer Research Studies"
          ]
        },
        {
          "openalex_id": "W4307337073",
          "year": 2022,
          "title": "Health-Related Quality-of-Life Outcomes of Very Preterm or Very Low Birth Weight Adults: Evidence From an Individual Participant Data Meta-Analysis",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 28,
          "topics": [
            "Infant Development and Preterm Care",
            "Neonatal Respiratory Health Research",
            "Birth, Development, and Health"
          ]
        },
        {
          "openalex_id": "W3159261299",
          "year": 2021,
          "title": "Health-Related Quality of Life in Pediatric Patients with Syndromic Autism and their Caregivers",
          "type": "article",
          "venue": "Journal of Autism and Developmental Disorders",
          "cited_by_count": 23,
          "topics": [
            "Autism Spectrum Disorder Research",
            "Genetics and Neurodevelopmental Disorders",
            "Genomic variations and chromosomal abnormalities"
          ]
        },
        {
          "openalex_id": "W2792790836",
          "year": 2018,
          "title": "Wellbeing Indices: A Comprehensive Inventory of Standards and a Review of Current Comparative Measures",
          "type": "article",
          "venue": "Ecological Economics",
          "cited_by_count": 19,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Health disparities and outcomes",
            "Income, Poverty, and Inequality"
          ]
        },
        {
          "openalex_id": "W2616009121",
          "year": 2017,
          "title": "Diagnostic Yield and Treatment Impact of Targeted Exome Sequencing in Early-onset Epilepsy",
          "type": "preprint",
          "venue": "bioRxiv (Cold Spring Harbor Laboratory)",
          "cited_by_count": 18,
          "topics": [
            "Genomics and Rare Diseases",
            "Epilepsy research and treatment",
            "Genetics and Neurodevelopmental Disorders"
          ]
        }
      ]
    }
  },
  {
    "name": "Cynthia L. Gong",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "328-RA",
        "title": "Assessing the Impact of Transitioning from Pediatric to Adult Care on the HRQoL of Adolescents with Complex Health Conditions: A 5-Year Longitudinal Registry Study in Los Angeles County Using the EQ-5D-5L",
        "working_group": "Populations and Health Systems, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5101451604",
      "display_name": "Cynthia L. Gong",
      "orcid": "0000-0003-0159-1335",
      "reported_affiliation": "Children's Hospital of Los Angeles",
      "works_count": 83,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 13
        },
        {
          "topic": "Neonatal Respiratory Health Research",
          "works": 6
        },
        {
          "topic": "Adolescent and Pediatric Healthcare",
          "works": 5
        },
        {
          "topic": "Prostate Cancer Treatment and Research",
          "works": 5
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 5
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 5
        },
        {
          "topic": "Antibiotics Pharmacokinetics and Efficacy",
          "works": 4
        },
        {
          "topic": "Pediatric Pain Management Techniques",
          "works": 4
        },
        {
          "topic": "Mechanical Circulatory Support Devices",
          "works": 4
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 3
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 3
        },
        {
          "topic": "Congenital Heart Disease Studies",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Joel W. Hay",
          "works": 19
        },
        {
          "name": "Leah Yieh",
          "works": 17
        },
        {
          "name": "Ashwini Lakshmanan",
          "works": 12
        },
        {
          "name": "Ashley Song",
          "works": 11
        },
        {
          "name": "Philippe Friedlich",
          "works": 11
        },
        {
          "name": "Ning Yan Gu",
          "works": 8
        },
        {
          "name": "Nadine Zawadzki",
          "works": 6
        },
        {
          "name": "Sandy Srinivas",
          "works": 6
        },
        {
          "name": "Feng Xie",
          "works": 5
        },
        {
          "name": "Xiayu Jiao",
          "works": 5
        },
        {
          "name": "Roy S. Zawadzki",
          "works": 5
        },
        {
          "name": "Kenneth M. Zangwill",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166185332",
          "year": 2026,
          "title": "CO56 BASELINE (UNTREATED) RISK OF HOSPITALIZATION AND MORTALITY IN PATIENTS WITH SPECIFIC COMORBID HIGH-RISK CONDITIONS WHO ARE ELIGIBLE FOR NIRMATRELVIR/RITONAVIR TREATMENT: A SYSTEMATIC LITERATURE REVIEW EXPANSION STUDY",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis C virus research",
            "COVID-19 Clinical Research Studies",
            "Respiratory viral infections research"
          ]
        },
        {
          "openalex_id": "W7165530247",
          "year": 2026,
          "title": "Implementation of an antimicrobial stewardship program in a multicenter neonatal intensive care unit collaborative: a mixed-methods staff resource needs evaluation",
          "type": "article",
          "venue": "Journal of Perinatology",
          "cited_by_count": 0,
          "topics": [
            "Neonatal and Maternal Infections",
            "Antibiotic Use and Resistance",
            "Antibiotics Pharmacokinetics and Efficacy"
          ]
        },
        {
          "openalex_id": "W7163538549",
          "year": 2026,
          "title": "The value of innovation in breast cancer treatment: real option value of olaparib for first-line treatment of gBRCA-mutated HER2 negative metastatic breast cancer",
          "type": "article",
          "venue": "Breast Cancer Research and Treatment",
          "cited_by_count": 0,
          "topics": [
            "PARP inhibition in cancer therapy",
            "Economic and Financial Impacts of Cancer",
            "Biosimilars and Bioanalytical Methods"
          ]
        },
        {
          "openalex_id": "W4406221853",
          "year": 2025,
          "title": "Budget Impact Analysis of Integrative Medicine Practices for Pediatric Patients With Chronic Pain",
          "type": "article",
          "venue": "Clinical Journal of Pain",
          "cited_by_count": 1,
          "topics": [
            "Complementary and Alternative Medicine Studies",
            "Musculoskeletal pain and rehabilitation",
            "Acupuncture Treatment Research Studies"
          ]
        },
        {
          "openalex_id": "W4412443149",
          "year": 2025,
          "title": "EPH173 Baseline Risk of Hospitalization and Mortality in High-Risk Subgroups of a Nirmatrelvir/Ritonavir Treatment-Eligible Population With Mild-to-Moderate COVID-19 in the United States: A Systematic Literature Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W4412042054",
          "year": 2025,
          "title": "Economic Analysis of Pharmacogenomics",
          "type": "article",
          "venue": "Advances in Molecular Pathology",
          "cited_by_count": 0,
          "topics": [
            "Pharmacogenetics and Drug Metabolism",
            "Drug Transport and Resistance Mechanisms",
            "Steroid Chemistry and Biochemistry"
          ]
        },
        {
          "openalex_id": "W2023025417",
          "year": 2012,
          "title": "PCN72 Cost Effectiveness Analysis of New Treatments for Metastatic Castration-Resistant Prostate Cancer: Does Severity Matter?",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Prostate Cancer Treatment and Research",
            "Radiopharmaceutical Chemistry and Applications",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2246090340",
          "year": 2012,
          "title": "Therapeutic options in metastatic castration-resistant prostate cancer (mCRPC): A cost-effectiveness analysis.",
          "type": "conference-abstract",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 2,
          "topics": [
            "Prostate Cancer Treatment and Research",
            "Cancer Treatment and Pharmacology",
            "Radiopharmaceutical Chemistry and Applications"
          ]
        },
        {
          "openalex_id": "W2054917262",
          "year": 2013,
          "title": "Therapeutic Options in Docetaxel-Refractory Metastatic Castration-Resistant Prostate Cancer: A Cost-Effectiveness Analysis",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 32,
          "topics": [
            "Prostate Cancer Treatment and Research",
            "Prostate Cancer Diagnosis and Treatment",
            "Management of metastatic bone disease"
          ]
        },
        {
          "openalex_id": "W2292137525",
          "year": 2014,
          "title": "Cost-Effectiveness Analysis of Abiraterone and Sipuleucel-T in Asymptomatic Metastatic Castration-Resistant Prostate Cancer",
          "type": "article",
          "venue": "Journal of the National Comprehensive Cancer Network",
          "cited_by_count": 34,
          "topics": [
            "Prostate Cancer Treatment and Research",
            "Radiopharmaceutical Chemistry and Applications",
            "Statistical Methods in Clinical Trials"
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
          "openalex_id": "W3112593009",
          "year": 2021,
          "title": "A US Population Health Survey on the Impact of COVID-19 Using the EQ-5D-5L",
          "type": "article",
          "venue": "Journal of General Internal Medicine",
          "cited_by_count": 77,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Efficiency Analysis Using DEA",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W3201456923",
          "year": 2021,
          "title": "The financial burden experienced by families of preterm infants after NICU discharge",
          "type": "article",
          "venue": "Journal of Perinatology",
          "cited_by_count": 59,
          "topics": [
            "Infant Development and Preterm Care",
            "Neonatal Respiratory Health Research",
            "Adolescent and Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W3041851110",
          "year": 2020,
          "title": "Lifetime Burden of Adult Congenital Heart Disease in the USA Using a Microsimulation Model",
          "type": "article",
          "venue": "Pediatric Cardiology",
          "cited_by_count": 53,
          "topics": [
            "Congenital Heart Disease Studies",
            "Retirement, Disability, and Employment",
            "Cardiovascular Function and Risk Factors"
          ]
        },
        {
          "openalex_id": "W3119281346",
          "year": 2021,
          "title": "Maternal post-traumatic stress and depression symptoms and outcomes after NICU discharge in a low-income sample: a cross-sectional study",
          "type": "article",
          "venue": "BMC Pregnancy and Childbirth",
          "cited_by_count": 51,
          "topics": [
            "Infant Development and Preterm Care",
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Neonatal Respiratory Health Research"
          ]
        },
        {
          "openalex_id": "W3100311432",
          "year": 2020,
          "title": "Cost–benefit analysis comparing trough, two-level AUC and Bayesian AUC dosing for vancomycin",
          "type": "article",
          "venue": "Clinical Microbiology and Infection",
          "cited_by_count": 46,
          "topics": [
            "Antimicrobial Resistance in Staphylococcus",
            "Antibiotics Pharmacokinetics and Efficacy",
            "Acute Kidney Injury Research"
          ]
        },
        {
          "openalex_id": "W3200589463",
          "year": 2021,
          "title": "Early transplantation maximizes survival in severe acute-on-chronic liver failure: Results of a Markov decision process model",
          "type": "article",
          "venue": "JHEP Reports",
          "cited_by_count": 44,
          "topics": [
            "Liver Disease and Transplantation",
            "Liver Disease Diagnosis and Treatment",
            "Organ Transplantation Techniques and Outcomes"
          ]
        },
        {
          "openalex_id": "W2187626044",
          "year": 2015,
          "title": "Association between use of warfarin with common sulfonylureas and serious hypoglycemic events: retrospective cohort analysis",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 42,
          "topics": [
            "Pharmacogenetics and Drug Metabolism",
            "Pharmaceutical Practices and Patient Outcomes",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients"
          ]
        }
      ]
    }
  }
]
