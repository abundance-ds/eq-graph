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
    "name": "Tomos Robinson",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2196-RA",
        "title": "Measuring and decomposing socioeconomic inequalities in the EQ-5D-3L and EQ-5D-5L in the UK using the concentration index based indices.",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5048830550",
      "display_name": "Tomos Robinson",
      "orcid": "0000-0001-8695-9738",
      "reported_affiliation": "St Nicholas Hospital",
      "works_count": 63,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 13
        },
        {
          "topic": "Glioma Diagnosis and Treatment",
          "works": 11
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 6
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 4
        },
        {
          "topic": "Brain Metastases and Treatment",
          "works": 4
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 4
        },
        {
          "topic": "Career Development and Diversity",
          "works": 4
        },
        {
          "topic": "Doctoral Education Challenges and Solutions",
          "works": 4
        },
        {
          "topic": "scientometrics and bibliometrics research",
          "works": 4
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 3
        },
        {
          "topic": "Statistical Methods in Clinical Trials",
          "works": 3
        },
        {
          "topic": "Employment and Welfare Studies",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Luke Vale",
          "works": 22
        },
        {
          "name": "Ashleigh Kernohan",
          "works": 16
        },
        {
          "name": "Helen Bulbeck",
          "works": 7
        },
        {
          "name": "Yemi Oluboyede",
          "works": 7
        },
        {
          "name": "Robin Grant",
          "works": 6
        },
        {
          "name": "Clare Bambra",
          "works": 6
        },
        {
          "name": "Laura Ternent",
          "works": 6
        },
        {
          "name": "Stephen Rice",
          "works": 6
        },
        {
          "name": "Sarah Jefferies",
          "works": 5
        },
        {
          "name": "Heather Brown",
          "works": 5
        },
        {
          "name": "Katie Thomson",
          "works": 5
        },
        {
          "name": "Giovany Orozco-Leal",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164906800",
          "year": 2026,
          "title": "Acceptability and Implementation of a Primary Care Health Check for Autistic People: Findings From Evaluation Questionnaires and Interviews",
          "type": "article",
          "venue": "Autism",
          "cited_by_count": 0,
          "topics": [
            "Health Promotion and Cardiovascular Prevention",
            "Autism Spectrum Disorder Research",
            "Down syndrome and intellectual disability research"
          ]
        },
        {
          "openalex_id": "W7160234779",
          "year": 2026,
          "title": "An investigation of a novel public health campaign to improve understanding of persistent pain",
          "type": "article",
          "venue": "Musculoskeletal Science and Practice",
          "cited_by_count": 0,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Health Literacy and Information Accessibility",
            "Pain Management and Opioid Use"
          ]
        },
        {
          "openalex_id": "W7154663184",
          "year": 2026,
          "title": "Designing policy-relevant measures of academic job preferences: A mixed-methods study of UK early career researchers",
          "type": "preprint",
          "venue": "MetArXiv (OSF Preprints)",
          "cited_by_count": 0,
          "topics": [
            "Career Development and Diversity",
            "Doctoral Education Challenges and Solutions",
            "scientometrics and bibliometrics research"
          ]
        },
        {
          "openalex_id": "W7148223632",
          "year": 2026,
          "title": "Patient-reported outcome measures in children and adolescents with malocclusion: a systematic review using COSMIN guidelines",
          "type": "review",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": [
            "Orthodontics and Dentofacial Orthopedics",
            "Temporomandibular Joint Disorders",
            "Facial Rejuvenation and Surgery Techniques"
          ]
        },
        {
          "openalex_id": "W7160610613",
          "year": 2026,
          "title": "Understanding patient preferences, experiences and engagement with ambulatory heart rhythm monitoring: a scoping review",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Technology and Patient Monitoring",
            "ECG Monitoring and Analysis",
            "Cardiac pacing and defibrillation studies"
          ]
        },
        {
          "openalex_id": "W7154235825",
          "year": 2026,
          "title": "What do early career researchers value in academic jobs? Evidence from a mixed-methods study in the UK",
          "type": "preprint",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Career Development and Diversity",
            "Doctoral Education Challenges and Solutions",
            "scientometrics and bibliometrics research"
          ]
        },
        {
          "openalex_id": "W2505755376",
          "year": 1970,
          "title": "Population Growth and Structure",
          "type": "book-chapter",
          "venue": "Palgrave Macmillan UK eBooks",
          "cited_by_count": 6,
          "topics": [
            "Economic Growth and Productivity"
          ]
        },
        {
          "openalex_id": "W2307196619",
          "year": 2008,
          "title": "Estimating Uncertainty in Wildlife Population Estimates",
          "type": "other",
          "venue": "University of Canterbury Research Repository (University of Canterbury)",
          "cited_by_count": 0,
          "topics": [
            "Species Distribution and Climate Change"
          ]
        },
        {
          "openalex_id": "W2895137659",
          "year": 2018,
          "title": "Estimating CHU-9D Utility Scores from the WAItE: A Mapping Algorithm for Economic Evaluation",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2956002388",
          "year": 2018,
          "title": "Exploring inequalities in child cognitive ability, psychological well-being and risky health behaviours",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Early Childhood Education and Development",
            "Poverty, Education, and Child Welfare"
          ]
        },
        {
          "openalex_id": "W3012937109",
          "year": 2020,
          "title": "Treatment of newly diagnosed glioblastoma in the elderly: a network meta-analysis",
          "type": "article",
          "venue": "Cochrane Database of Systematic Reviews",
          "cited_by_count": 78,
          "topics": [
            "Glioma Diagnosis and Treatment",
            "Meta-analysis and systematic reviews",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W2924492801",
          "year": 2019,
          "title": "The impact of New Labour’s English health inequalities strategy on geographical inequalities in infant mortality: a time-trend analysis",
          "type": "article",
          "venue": "Journal of Epidemiology & Community Health",
          "cited_by_count": 69,
          "topics": [
            "Health disparities and outcomes",
            "Employment and Welfare Studies",
            "Healthcare Systems and Challenges"
          ]
        },
        {
          "openalex_id": "W2943139789",
          "year": 2021,
          "title": "Prognostic value of test(s) for O6-methylguanine–DNA methyltransferase (MGMT) promoter methylation for predicting overall survival in people with glioblastoma treated with temozolomide",
          "type": "article",
          "venue": "Cochrane Database of Systematic Reviews",
          "cited_by_count": 51,
          "topics": [
            "Glioma Diagnosis and Treatment",
            "Epigenetics and DNA Methylation",
            "Cutaneous Melanoma Detection and Management"
          ]
        },
        {
          "openalex_id": "W3041321794",
          "year": 2020,
          "title": "An examination of trends in antibiotic prescribing in primary care and the association with area-level deprivation in England",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 46,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pharmaceutical Practices and Patient Outcomes",
            "Antibiotics Pharmacokinetics and Efficacy"
          ]
        },
        {
          "openalex_id": "W4200182341",
          "year": 2021,
          "title": "Diagnostic accuracy of 1p/19q codeletion tests in oligodendroglioma: A comprehensive meta‐analysis based on a Cochrane systematic review",
          "type": "review",
          "venue": "Neuropathology and Applied Neurobiology",
          "cited_by_count": 24,
          "topics": [
            "Glioma Diagnosis and Treatment",
            "Chromatin Remodeling and Cancer",
            "Cancer Genomics and Diagnostics"
          ]
        },
        {
          "openalex_id": "W4311152304",
          "year": 2022,
          "title": "Photobiomodulation in the management of oral mucositis for adult head and neck cancer patients receiving irradiation: the LiTEFORM RCT",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 20,
          "topics": [
            "Oral health in cancer treatment",
            "Laser Applications in Dentistry and Medicine",
            "Oral Health Pathology and Treatment"
          ]
        },
        {
          "openalex_id": "W4220717886",
          "year": 2022,
          "title": "Diagnostic test accuracy and cost-effectiveness of tests for codeletion of chromosomal arms 1p and 19q in people with glioma",
          "type": "article",
          "venue": "Cochrane Database of Systematic Reviews",
          "cited_by_count": 19,
          "topics": [
            "Glioma Diagnosis and Treatment",
            "Cancer Genomics and Diagnostics",
            "Brain Metastases and Treatment"
          ]
        },
        {
          "openalex_id": "W2946720497",
          "year": 2018,
          "title": "Health for Wealth : Building a Healthier Northern Powerhouse for UK Productivity",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 15,
          "topics": [
            "Global Health Care Issues",
            "Health disparities and outcomes",
            "Employment and Welfare Studies"
          ]
        }
      ]
    }
  },
  {
    "name": "Trudy Sullivan",
    "member_affiliation": "University of Otago",
    "is_member": true,
    "projects": [
      {
        "project_id": "20180470",
        "title": "Chronic disease, co-morbidities and health-related quality of life in a representative sample of the New Zealand population",
        "working_group": "Valuation"
      },
      {
        "project_id": "441-RA",
        "title": "Using the EQ-5D to value the health-related quality of life of older adolescents: A feasibility and qualitative study",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5022698267",
      "display_name": "Trudy Sullivan",
      "orcid": "0000-0001-8452-2591",
      "reported_affiliation": "University of Otago",
      "works_count": 82,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 13
        },
        {
          "topic": "Experimental Behavioral Economics Studies",
          "works": 10
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 8
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 6
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 6
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 6
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 6
        },
        {
          "topic": "Orthopaedic implants and arthroplasty",
          "works": 4
        },
        {
          "topic": "Hip and Femur Fractures",
          "works": 4
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 4
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 4
        },
        {
          "topic": "Diabetes, Cardiovascular Risks, and Lipoproteins",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sarah Derrett",
          "works": 15
        },
        {
          "name": "Andrew Gray",
          "works": 11
        },
        {
          "name": "Stephen Knowles",
          "works": 10
        },
        {
          "name": "Emma Wyeth",
          "works": 9
        },
        {
          "name": "Paul Hansen",
          "works": 8
        },
        {
          "name": "Tim Stokes",
          "works": 8
        },
        {
          "name": "Yvonne C. Anderson",
          "works": 6
        },
        {
          "name": "Fiona Doolan‐Noble",
          "works": 6
        },
        {
          "name": "Kirsten J. Coppell",
          "works": 6
        },
        {
          "name": "Franz Ombler",
          "works": 5
        },
        {
          "name": "Robin Turner",
          "works": 5
        },
        {
          "name": "Murat Genç",
          "works": 5
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
          "openalex_id": "W4408566995",
          "year": 2025,
          "title": "Can Adolescents Value the EQ-5D-Y-5L and EQ-5D-5L, and How Do the Values Compare? A Feasibility Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W4414612421",
          "year": 2025,
          "title": "Cost-effectiveness of as-needed budesonide-formoterol in adults with mild asthma: the Novel START trial",
          "type": "article",
          "venue": "ERJ Open Research",
          "cited_by_count": 0,
          "topics": [
            "Asthma and respiratory diseases",
            "Pharmacological Effects and Assays",
            "Chronic Obstructive Pulmonary Disease (COPD) Research"
          ]
        },
        {
          "openalex_id": "W4415949840",
          "year": 2025,
          "title": "Delivering optimal weight gain advice to pregnant women by lead maternity carer midwives in a real-world setting to optimise health outcomes (DOT study): a case study protocol",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 0,
          "topics": [
            "Gestational Diabetes Research and Management",
            "Breastfeeding Practices and Influences",
            "Obesity and Health Practices"
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
          "openalex_id": "W376467333",
          "year": 2003,
          "title": "Cognitive behaviour therapy (CBT) with intensive dietetic treatment results in sustained weight loss at 12 months of the FBI trial",
          "type": "conference-paper",
          "venue": "Queensland's institutional digital repository (The University of Queensland)",
          "cited_by_count": 0,
          "topics": [
            "Eating Disorders and Behaviors"
          ]
        },
        {
          "openalex_id": "W2171515718",
          "year": 2012,
          "title": "Using MCDA (Multi-Criteria Decision Analysis) to prioritise publicly-funded health care",
          "type": "dissertation",
          "venue": "Otago University Research Archive (University of Otago)",
          "cited_by_count": 13,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2416882180",
          "year": 2014,
          "title": "Expectations and reality: What you want is not always what you get",
          "type": "article",
          "venue": "Australian Journal of Adult Learning",
          "cited_by_count": 7,
          "topics": [
            "Innovations in Educational Methods",
            "Higher Education Research Studies",
            "Financial Markets and Investment Strategies"
          ]
        },
        {
          "openalex_id": "W2272439292",
          "year": 2015,
          "title": "A Practical Approach to Well-being Based Policy Development: What Do New Zealanders Want from Their Retirement Income Policies?",
          "type": "report",
          "venue": "Econstor (Econstor)",
          "cited_by_count": 1,
          "topics": [
            "New Zealand Economic and Social Studies",
            "demographic modeling and climate adaptation",
            "Fiscal Policy and Economic Growth"
          ]
        },
        {
          "openalex_id": "W2938447163",
          "year": 2019,
          "title": "A new tool for creating personal and social EQ-5D-5L value sets, including valuing ‘dead’",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 56,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality Function Deployment in Product Design",
            "Product Development and Customization"
          ]
        },
        {
          "openalex_id": "W3174141534",
          "year": 2021,
          "title": "New Zealand Population Norms for the EQ-5D-5L Constructed From the Personal Value Sets of Participants in a National Survey",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 50,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare innovation and challenges"
          ]
        },
        {
          "openalex_id": "W2267950689",
          "year": 2015,
          "title": "The impact of an increase in excise tax on the retail price of tobacco in New Zealand",
          "type": "article",
          "venue": "Tobacco Control",
          "cited_by_count": 45,
          "topics": [
            "Smoking Behavior and Cessation",
            "Global Public Health Policies and Epidemiology",
            "Economics of Agriculture and Food Markets"
          ]
        },
        {
          "openalex_id": "W2944537310",
          "year": 2020,
          "title": "In search of effective altruists",
          "type": "article",
          "venue": "Applied Economics",
          "cited_by_count": 35,
          "topics": [
            "Experimental Behavioral Economics Studies",
            "Religion, Society, and Development",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2948603290",
          "year": 2019,
          "title": "The hidden costs of employee drinking: A quantitative analysis",
          "type": "article",
          "venue": "Drug and Alcohol Review",
          "cited_by_count": 35,
          "topics": [
            "Workplace Health and Well-being",
            "Substance Abuse Treatment and Outcomes",
            "Sleep and Work-Related Fatigue"
          ]
        },
        {
          "openalex_id": "W637651589",
          "year": 2017,
          "title": "Does Charity Begin at Home or Overseas?",
          "type": "article",
          "venue": "Nonprofit and Voluntary Sector Quarterly",
          "cited_by_count": 32,
          "topics": [
            "Nonprofit Sector and Volunteering",
            "Experimental Behavioral Economics Studies",
            "Religion, Society, and Development"
          ]
        },
        {
          "openalex_id": "W3121557478",
          "year": 2021,
          "title": "Total Hip and Knee Arthroplasties Are Highly Cost-Effective Procedures: The Importance of Duration of Follow-Up",
          "type": "article",
          "venue": "The Journal of Arthroplasty",
          "cited_by_count": 32,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Orthopaedic implants and arthroplasty",
            "Hip and Femur Fractures"
          ]
        },
        {
          "openalex_id": "W3028575551",
          "year": 2020,
          "title": "The Relationship Between Preoperative Oxford Hip and Knee Score and Change in Health-Related Quality of Life After Total Hip and Total Knee Arthroplasty: Can It Help Inform Rationing Decisions?",
          "type": "article",
          "venue": "Arthroplasty Today",
          "cited_by_count": 31,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Orthopaedic implants and arthroplasty",
            "Hip and Femur Fractures"
          ]
        }
      ]
    }
  },
  {
    "name": "Ulrike Ravens-Sieberer",
    "member_affiliation": "University Medical Center Hamburg-Eppendorf",
    "is_member": true,
    "projects": [
      {
        "project_id": "2016270",
        "title": "The EQ-5D-Y in a clinical sample of children and adolescents with asthma, diabetes and rheumatoid arthritis: convergent validity, agreement between self-and parent-reports as well as sensitivity to change",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5049804622",
      "display_name": "Ulrike Ravens‐Sieberer",
      "orcid": "0000-0002-2031-095X",
      "reported_affiliation": "Universität Hamburg",
      "works_count": 459,
      "top_topics": [
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 145
        },
        {
          "topic": "Child and Adolescent Psychosocial and Emotional Development",
          "works": 145
        },
        {
          "topic": "Health and Medical Studies",
          "works": 96
        },
        {
          "topic": "Child and Adolescent Health",
          "works": 69
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 49
        },
        {
          "topic": "Adolescent and Pediatric Healthcare",
          "works": 48
        },
        {
          "topic": "School Health and Nursing Education",
          "works": 35
        },
        {
          "topic": "Attention Deficit Hyperactivity Disorder",
          "works": 33
        },
        {
          "topic": "Family Support in Illness",
          "works": 30
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 30
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 26
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 25
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Michael Erhart",
          "works": 131
        },
        {
          "name": "Anne Kaman",
          "works": 96
        },
        {
          "name": "Christiane Otto",
          "works": 60
        },
        {
          "name": "Janine Devine",
          "works": 58
        },
        {
          "name": "Monika Bullinger",
          "works": 54
        },
        {
          "name": "Robert Schlack",
          "works": 50
        },
        {
          "name": "Fionna Klasen",
          "works": 50
        },
        {
          "name": "Franziska Reiß",
          "works": 49
        },
        {
          "name": "Heike Hölling",
          "works": 48
        },
        {
          "name": "Ann-Kathrin Napp",
          "works": 34
        },
        {
          "name": "Nora Wille",
          "works": 33
        },
        {
          "name": "Luís Rajmil",
          "works": 32
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167457554",
          "year": 2026,
          "title": "A cross-cultural adaptation and content validity assessment of the Czech Version Kiddy-KINDL Questionnaire",
          "type": "article",
          "venue": "Acta Psychologica",
          "cited_by_count": 0,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Stuttering Research and Treatment",
            "Reading and Literacy Development"
          ]
        },
        {
          "openalex_id": "W7164406381",
          "year": 2026,
          "title": "Adapting a peer-support intervention for parents of children with rare liver diseases: Study protocol of the Q.RARE.LI PARENTS project",
          "type": "article",
          "venue": "Journal of Psychosomatic Research",
          "cited_by_count": 0,
          "topics": [
            "Adolescent and Pediatric Healthcare",
            "Childhood Cancer Survivors' Quality of Life",
            "Family and Disability Support Research"
          ]
        },
        {
          "openalex_id": "W7171523105",
          "year": 2026,
          "title": "Additional file 1 of Higher severity of infant RSV infections is associated with lower parental quality of life – a European observational study",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Respiratory viral infections research",
            "Viral gastroenteritis research and epidemiology",
            "Viral Infections and Immunology Research"
          ]
        },
        {
          "openalex_id": "W7171528227",
          "year": 2026,
          "title": "Additional file 1 of Higher severity of infant RSV infections is associated with lower parental quality of life – a European observational study",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Respiratory viral infections research",
            "Viral gastroenteritis research and epidemiology",
            "Viral Infections and Immunology Research"
          ]
        },
        {
          "openalex_id": "W7165776696",
          "year": 2026,
          "title": "Congenital Heart Defects and Mental Health: Stress, Psychological Treatment Use, and COVID-19-Related Burden in Young Patients—Lessons from the P-BAHn Study",
          "type": "article",
          "venue": "Repository KITopen (Karlsruhe Institute of Technology)",
          "cited_by_count": 0,
          "topics": [
            "Congenital Heart Disease Studies",
            "Childhood Cancer Survivors' Quality of Life",
            "Congenital heart defects research"
          ]
        },
        {
          "openalex_id": "W7171664309",
          "year": 2026,
          "title": "Gesundheitsbezogene Lebensqualität",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Health, psychology, and well-being",
            "Psychosomatic Disorders and Their Treatments",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W1627553912",
          "year": 1995,
          "title": "Grundlagen, Methoden und Anwendungsgebiete der Lebensqualitätsforschung bei Kindern",
          "type": "article",
          "venue": "PsyDok Dokumentenserver für die Psychologie (Leibniz-Zentrum für Psychologische Information und Dokumentation)",
          "cited_by_count": 17,
          "topics": [
            "Health and Medical Studies"
          ]
        },
        {
          "openalex_id": "W2397047843",
          "year": 1995,
          "title": "[General principles, methods and areas of application of quality of life research in children].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 40,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Child and Adolescent Health"
          ]
        },
        {
          "openalex_id": "W1990430577",
          "year": 1997,
          "title": "Kann man Lebensqualität bei Kindern messen?",
          "type": "article",
          "venue": "Aktuelle Urologie",
          "cited_by_count": 5,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Ethics and Legal Issues in Pediatric Healthcare",
            "Family Support in Illness"
          ]
        },
        {
          "openalex_id": "W2007706875",
          "year": 1998,
          "title": "Assessing health-related quality of life in chronically ill children with the German KINDL: first psychometric and content analytical results",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1123,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Adolescent and Pediatric Healthcare",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W3122397547",
          "year": 2021,
          "title": "Impact of the COVID-19 pandemic on quality of life and mental health in children and adolescents in Germany",
          "type": "article",
          "venue": "European Child & Adolescent Psychiatry",
          "cited_by_count": 1073,
          "topics": [
            "COVID-19 and Mental Health",
            "Child and Adolescent Psychosocial and Emotional Development",
            "Family Support in Illness"
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
          "openalex_id": "W1984556055",
          "year": 2005,
          "title": "KIDSCREEN-52 quality-of-life measure for children and adolescents",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 829,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Family Support in Illness"
          ]
        },
        {
          "openalex_id": "W2047032381",
          "year": 2008,
          "title": "The KIDSCREEN-52 Quality of Life Measure for Children and Adolescents: Psychometric Results from a Cross-Cultural Survey in 13 European Countries",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 808,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Adolescent and Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W2016047472",
          "year": 2007,
          "title": "The KIDSCREEN-27 quality of life measure for children and adolescents: psychometric results from a cross-cultural survey in 13 European countries",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 759,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        },
        {
          "openalex_id": "W2016860569",
          "year": 2010,
          "title": "Reliability, construct and criterion validity of the KIDSCREEN-10 score: a short measure for children and adolescents’ well-being and health-related quality of life",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 733,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Child and Adolescent Psychosocial and Emotional Development",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W2054053084",
          "year": 2013,
          "title": "The European KIDSCREEN approach to measure quality of life and well-being in children: development, current application, and future advances",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 622,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing"
          ]
        }
      ]
    }
  },
  {
    "name": "Valentina Prevolnik Rupel",
    "member_affiliation": "Institute for Economic Research",
    "is_member": true,
    "projects": [
      {
        "project_id": "1687-RA",
        "title": "Content validity of the EQ-HWB among elderly social care users in Slovenia and Hungary",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2013160",
        "title": "Use of EQ-5D in elderly populations (Call for proposal 1)",
        "working_group": "Others"
      },
      {
        "project_id": "2013210",
        "title": "HTA and quality of life measurement in patients",
        "working_group": "Others"
      },
      {
        "project_id": "20170280",
        "title": "Revisiting EQ-5D-3L tariffs – An international collaboration between Slovenia end Portugal",
        "working_group": "Valuation"
      },
      {
        "project_id": "377-VS",
        "title": "EQ-5D-5L Slovenia national value set",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5091343801",
      "display_name": "Valentina Prevolnik Rupel",
      "orcid": "0000-0002-1238-7156",
      "reported_affiliation": "",
      "works_count": 104,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 49
        },
        {
          "topic": "Global Health Care Issues",
          "works": 19
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 11
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 10
        },
        {
          "topic": "Quality and Safety in Healthcare",
          "works": 8
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 7
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 6
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 6
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 5
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 4
        },
        {
          "topic": "Cardiac pacing and defibrillation studies",
          "works": 4
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Marko Ogorevc",
          "works": 26
        },
        {
          "name": "Dominik Golicki",
          "works": 22
        },
        {
          "name": "László Gulàcsi",
          "works": 21
        },
        {
          "name": "Márta Péntek",
          "works": 21
        },
        {
          "name": "Zsombor Zrubka",
          "works": 19
        },
        {
          "name": "Petra Baji",
          "works": 18
        },
        {
          "name": "Valentin Brodszky",
          "works": 15
        },
        {
          "name": "Fanni Rencz",
          "works": 13
        },
        {
          "name": "Eva Turk",
          "works": 10
        },
        {
          "name": "Marko Divjak",
          "works": 10
        },
        {
          "name": "Judit Simon",
          "works": 8
        },
        {
          "name": "Jakub Závada",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7126136010",
          "year": 2026,
          "title": "Dejavniki dostopnosti zobozdravstvenih storitev",
          "type": "article",
          "venue": "DiRROS repository (University of Maribor)",
          "cited_by_count": 0,
          "topics": [
            "Religious, Philosophical, and Educational Studies",
            "Eastern European Communism and Reforms",
            "Hearing Impairment and Communication"
          ]
        },
        {
          "openalex_id": "W4402382542",
          "year": 2024,
          "title": "Accessing dental services in Slovenia: A quantitative study",
          "type": "article",
          "venue": "Journal of Infrastructure Policy and Development",
          "cited_by_count": 0,
          "topics": [
            "Dental Education, Practice, Research",
            "Dental Health and Care Utilization"
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
          "openalex_id": "W4381469959",
          "year": 2023,
          "title": "EQ-5D-5L Value Set for Slovenia",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W4392197176",
          "year": 2023,
          "title": "Estimating the Share of Sickness Absence Costs in Europe's GDP – A Country, Gender and Time Perspective",
          "type": "article",
          "venue": "Finanse i Prawo Finansowe",
          "cited_by_count": 4,
          "topics": [
            "Global Health Care Issues",
            "Employment and Welfare Studies",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4324353450",
          "year": 2023,
          "title": "Is Value-Based Health Care Just the Latest Fad or can it Transform the Slovenian Health Care System?",
          "type": "article",
          "venue": "Slovenian Journal of Public Health",
          "cited_by_count": 5,
          "topics": [
            "Healthcare Policy and Management",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2522197851",
          "year": 2000,
          "title": "Meddržavne selitve prebivalcev Slovenije ter obseg emigrantov in tujcev v Sloveniji - devetdeseta leta",
          "type": "article",
          "venue": "DOAJ (DOAJ: Directory of Open Access Journals)",
          "cited_by_count": 0,
          "topics": [
            "Urbanization and City Planning",
            "Eastern European Communism and Reforms",
            "Balkans: History, Politics, Society"
          ]
        },
        {
          "openalex_id": "W2059891792",
          "year": 2001,
          "title": "Quality of life and treatment costs in schizophrenic outpatients, treated with depot neuroleptics",
          "type": "article",
          "venue": "European Psychiatry",
          "cited_by_count": 27,
          "topics": [
            "Schizophrenia research and treatment",
            "Bipolar Disorder and Treatment",
            "Obsessive-Compulsive Spectrum Disorders"
          ]
        },
        {
          "openalex_id": "W2776436830",
          "year": 2001,
          "title": "The Slovenian vas tariff based on valuations of EQ-5D health states from the general population",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 23,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W3024032380",
          "year": 2002,
          "title": "Calidad de vida y costes de tratamiento en pacientes ambulatorios esquizofrénicos tratados con neurolépticos depot",
          "type": "article",
          "venue": "European psychiatry (Ed Española)",
          "cited_by_count": 0,
          "topics": [
            "Schizophrenia research and treatment",
            "Parkinson's Disease Mechanisms and Treatments",
            "Mental Health and Psychiatry"
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
          "openalex_id": "W2104025691",
          "year": 2015,
          "title": "Is There a European View on Health Economic Evaluations? Results from a Synopsis of Methodological Guidelines Used in the EUnetHTA Partner Countries",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 87,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2585764475",
          "year": 2017,
          "title": "Improving the Methods for the Economic Evaluation of Medical Devices",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 85,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cardiac pacing and defibrillation studies",
            "Innovation Policy and R&D"
          ]
        },
        {
          "openalex_id": "W4286921195",
          "year": 2021,
          "title": "Slovenia: Health System Review.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 73,
          "topics": [
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W3126333616",
          "year": 2021,
          "title": "EQ-5D-Y Value Set for Slovenia",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 71,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2955830860",
          "year": 2019,
          "title": "Cultural Values: Can They Explain Differences in Health Utilities between Countries?",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 69,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2264262604",
          "year": 2015,
          "title": "HEALTH TECHNOLOGY ASSESSMENT OF MEDICAL DEVICES: A SURVEY OF NON-EUROPEAN UNION AGENCIES",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 68,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Biomedical Ethics and Regulation",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W3091973921",
          "year": 2020,
          "title": "EQ-5D-5L Slovenian population norms",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 64,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Healthcare Systems and Reforms"
          ]
        }
      ]
    }
  },
  {
    "name": "victor zarate",
    "member_affiliation": "MSD",
    "is_member": true,
    "projects": [
      {
        "project_id": "2015370",
        "title": "EQ-5D: the ABC approach to measuring and valuing health in Latin America (W15 workshop: 5th ISPOR Latin America meeting/Chile 2015",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2016380",
        "title": "Analyzing health inequities using the EQ-5D in the Chilean general population",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2016390",
        "title": "Analyzing self-perceive health status using the EQ-5D in Latin America: 1st approach to the Gallup 2007 World Survey (19 countries)",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20170470",
        "title": "Recent experiences using the EuroQol EQ-5D instrument In Latin America: The 3L & 5L; Public Health And Economic Evaluations; Newer Time Trade Off Variants And Discrete ChoiceExperiments",
        "working_group": "Others"
      },
      {
        "project_id": "20170630",
        "title": "Understanding Self-perceived Health in Latin America",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "462-RA",
        "title": "EQ-5D 3L in the 2017 National Health Survey for Chile",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5074565937",
      "display_name": "V Zárate",
      "orcid": "0000-0001-9145-3694",
      "reported_affiliation": "Merck & Co., Inc., Rahway, NJ, USA (United States)",
      "works_count": 43,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 21
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 8
        },
        {
          "topic": "Health and Lifestyle Studies",
          "works": 5
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 5
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 4
        },
        {
          "topic": "Global Health Care Issues",
          "works": 4
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 4
        },
        {
          "topic": "Aging, Health, and Disability",
          "works": 4
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 3
        },
        {
          "topic": "Public Health and Social Inequalities",
          "works": 2
        },
        {
          "topic": "History, Culture, and Diplomacy",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Paul Kind",
          "works": 11
        },
        {
          "name": "Federico Augustovski",
          "works": 7
        },
        {
          "name": "P Kind",
          "works": 6
        },
        {
          "name": "Pedro Olivares-Tirado",
          "works": 5
        },
        {
          "name": "Gabriel Bastías",
          "works": 4
        },
        {
          "name": "Thomas Leisewitz",
          "works": 4
        },
        {
          "name": "A Vignau",
          "works": 4
        },
        {
          "name": "Ling‐Hsiang Chuang",
          "works": 4
        },
        {
          "name": "P Valenzuela",
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
          "name": "Hilary Short",
          "works": 3
        }
      ],
      "work_examples": [
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
          "openalex_id": "W2980482484",
          "year": 2019,
          "title": "EP4 HOW IS SELF-PERCEIVED HEALTH STATUS (EQ-5D) ASSOCIATED WITH SOCIOECONOMIC CONDITIONS IN 22 LATIN AMERICAN COUNTRIES?",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes",
            "Food Security and Health in Diverse Populations"
          ]
        },
        {
          "openalex_id": "W2980322025",
          "year": 2019,
          "title": "PNS18 HOW IS SELF-PERCEIVED HEALTH STATUS (EQ-5D) ASSOCIATED WITH PSYCHOSOCIAL FACTORS IN 22 LATIN AMERICAN COUNTRIES?",
          "type": "conference-abstract",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2799597000",
          "year": 2018,
          "title": "Systematic review of Latin American national oral health surveys in adults",
          "type": "review",
          "venue": "Community Dentistry And Oral Epidemiology",
          "cited_by_count": 11,
          "topics": [
            "Dental Health and Care Utilization",
            "Oral microbiology and periodontitis research",
            "HIV/AIDS oral health manifestations"
          ]
        },
        {
          "openalex_id": "W2766034681",
          "year": 2017,
          "title": "Impacto Del Índice De Masa Corporal En La Salud Autopercibida: Resultados De La Encuesta Nacional De Salud De Chile 2016-2017",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 6,
          "topics": [
            "Health and Lifestyle Studies"
          ]
        },
        {
          "openalex_id": "W4234168163",
          "year": 1931,
          "title": "Spanish sketches",
          "type": "article",
          "venue": "Notes and Queries",
          "cited_by_count": 0,
          "topics": [
            "History, Culture, and Diplomacy",
            "Sephardic Jews and Inquisition Studies",
            "Translation Studies and Practices"
          ]
        },
        {
          "openalex_id": "W4247404605",
          "year": 1931,
          "title": "Spanish sketches",
          "type": "article",
          "venue": "Notes and Queries",
          "cited_by_count": 0,
          "topics": [
            "History, Culture, and Diplomacy",
            "Sephardic Jews and Inquisition Studies",
            "Translation Studies and Practices"
          ]
        },
        {
          "openalex_id": "W2018917169",
          "year": 2007,
          "title": "Coronary heart disease in Chile",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 1,
          "topics": [
            "Acute Myocardial Infarction Research",
            "Cardiovascular Function and Risk Factors",
            "Health and Lifestyle Studies"
          ]
        },
        {
          "openalex_id": "W2015768131",
          "year": 2007,
          "title": "DALYs And QALYs In Developing Countries",
          "type": "article",
          "venue": "Health Affairs",
          "cited_by_count": 9,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W1977515230",
          "year": 2008,
          "title": "Health care reform in Chile",
          "type": "article",
          "venue": "Canadian Medical Association Journal",
          "cited_by_count": 104,
          "topics": [
            "Healthcare Policy and Management",
            "Public Health and Social Inequalities",
            "Public Health in Brazil"
          ]
        },
        {
          "openalex_id": "W2014314115",
          "year": 2011,
          "title": "Social Valuation of EQ-5D Health States: The Chilean Case",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 85,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2162937108",
          "year": 2008,
          "title": "Hispanic Valuation of the EQ-5D Health States: A Social Value Set for Latin Americans",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 66,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2614059409",
          "year": 2017,
          "title": "Measuring the Benefits of Healthcare: DALYs and QALYs – Does the Choice of Measure Matter? A Case Study of Two Preventive Interventions",
          "type": "article",
          "venue": "International Journal of Health Policy and Management",
          "cited_by_count": 56,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2123998905",
          "year": 2010,
          "title": "Evaluaciones económicas en salud: Conceptos básicos y clasificación",
          "type": "article",
          "venue": "Revista médica de Chile",
          "cited_by_count": 27,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2118362451",
          "year": 2010,
          "title": "[Methodology for evaluating cost-effectiveness in primary health care centers in Chile].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 10,
          "topics": []
        }
      ]
    }
  }
]
