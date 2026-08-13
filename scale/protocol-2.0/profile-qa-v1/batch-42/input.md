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
    "name": "Patricia Cubi-Molla",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2016460",
        "title": "TTO valuation sets for EQ-5D-3L – country comparison",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180190",
        "title": "MSc student project placements on a EuroQol-related topic",
        "working_group": "Valuation, Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5087726711",
      "display_name": "Patricia Cubí‐Mollá",
      "orcid": "0000-0002-2803-7337",
      "reported_affiliation": "Office Of Health Economics",
      "works_count": 53,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 30
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 11
        },
        {
          "topic": "Global Health Care Issues",
          "works": 11
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 8
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 6
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 6
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 5
        },
        {
          "topic": "Parkinson's Disease Mechanisms and Treatments",
          "works": 5
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 4
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 4
        },
        {
          "topic": "Mindfulness and Compassion Interventions",
          "works": 3
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nancy Devlin",
          "works": 9
        },
        {
          "name": "Mireia Jofre‐Bonet",
          "works": 9
        },
        {
          "name": "Martina Garau",
          "works": 8
        },
        {
          "name": "Paula Lorgelly",
          "works": 6
        },
        {
          "name": "Angeliki Bogosian",
          "works": 5
        },
        {
          "name": "Catherine S. Hurt",
          "works": 5
        },
        {
          "name": "Lance M. McCracken",
          "works": 5
        },
        {
          "name": "Adrian Towse",
          "works": 5
        },
        {
          "name": "Amanda Cole",
          "works": 5
        },
        {
          "name": "Duncan Sim",
          "works": 5
        },
        {
          "name": "Jon Sussex",
          "works": 5
        },
        {
          "name": "David Mott",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4408635332",
          "year": 2025,
          "title": "Acceptability and feasibility randomised controlled trial of a digital mental health intervention for people with Parkinson’s (PACT): trial protocol",
          "type": "article",
          "venue": "Pilot and Feasibility Studies",
          "cited_by_count": 3,
          "topics": [
            "Digital Mental Health Interventions",
            "Parkinson's Disease Mechanisms and Treatments",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W4412490688",
          "year": 2025,
          "title": "Effect of caregiver burden on the quality of life of informal caregivers of people with cystic fibrosis in the United Kingdom: a cross-sectional study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Cystic Fibrosis Research Advances",
            "Family and Disability Support Research",
            "Family Caregiving in Mental Illness"
          ]
        },
        {
          "openalex_id": "W4408885123",
          "year": 2025,
          "title": "Evaluating a digital mental health intervention for people with Parkinson’s (PACT): acceptability and feasibility randomised controlled trial",
          "type": "article",
          "venue": "Aging & Mental Health",
          "cited_by_count": 1,
          "topics": [
            "Digital Mental Health Interventions",
            "Parkinson's Disease Mechanisms and Treatments",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W4412587737",
          "year": 2025,
          "title": "Guidance on the economic evaluation of the health impacts of climate action: a literature review protocol.",
          "type": "article",
          "venue": "Wellcome Open Research",
          "cited_by_count": 1,
          "topics": [
            "Climate Change and Health Impacts",
            "Global Health Care Issues",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W4417480707",
          "year": 2025,
          "title": "HPR180 Science at PACE? A Multi-Stakeholder Developed Framework for Accelerated Patient Access to Cancer Care",
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
          "openalex_id": "W4408461078",
          "year": 2025,
          "title": "Navigating change: a comparative analysis of health technology assessment reforms across agencies – processes, drivers, and interdependencies",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Biomedical Ethics and Regulation"
          ]
        },
        {
          "openalex_id": "W2163303525",
          "year": 2008,
          "title": "Estimating health effects in quality-of-life terms: health losses following road crashes",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2805270120",
          "year": 2009,
          "title": "Métodos de escalamiento para medidas categóricas de salud auto-percibida: Resumen del trabajo premiado en las XXIX Jornadas de Economía de la Salud como mejor presentación oral",
          "type": "article",
          "venue": "Economía y salud: boletín informativo",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Systems and Technology"
          ]
        },
        {
          "openalex_id": "W3124179940",
          "year": 2011,
          "title": "Quality of Life Lost Due to Non-Fatal Road Crashes",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2050652103",
          "year": 2011,
          "title": "Quality of life lost due to non‐fatal road traffic injuries",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 15,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W3125659738",
          "year": 2021,
          "title": "Acceptability and Feasibility of a Mindfulness Intervention Delivered via Videoconferencing for People With Parkinson’s",
          "type": "article",
          "venue": "Journal of Geriatric Psychiatry and Neurology",
          "cited_by_count": 55,
          "topics": [
            "Mindfulness and Compassion Interventions",
            "Restless Legs Syndrome Research",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W2003304941",
          "year": 2014,
          "title": "A Study of the Relationship between Health and Subjective Well-Being in Parkinson’s Disease Patients",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 36,
          "topics": [
            "Parkinson's Disease Mechanisms and Treatments",
            "Psychological Well-being and Life Satisfaction",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4281646039",
          "year": 2022,
          "title": "Supply-Side Cost-Effectiveness Thresholds: Questions for Evidence-Based Policy",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 34,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W3190941324",
          "year": 2021,
          "title": "Approaches to Measure Efficiency in Primary Care: A Systematic Literature Review",
          "type": "review",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 27,
          "topics": [
            "Primary Care and Health Outcomes",
            "Healthcare Policy and Management",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2781816100",
          "year": 2018,
          "title": "Experience-Based Values: A Framework for Classifying Different Types of Experience in Health Valuation Research",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 27,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W3014071279",
          "year": 2020,
          "title": "Testing the validity and responsiveness of a new cancer-specific health utility measure (FACT-8D) in relapsed/refractory mantle cell lymphoma, and comparison to EQ-5D-5L",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 21,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W3099808323",
          "year": 2020,
          "title": "Accreditation as a quality-improving policy tool: family planning, maternal health, and child health in Egypt",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 20,
          "topics": [
            "Healthcare Quality and Management",
            "Healthcare Systems and Reforms",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2601396669",
          "year": 2017,
          "title": "Adaptation to health states: Sick yet better off?",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 19,
          "topics": [
            "Global Health Care Issues",
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        }
      ]
    }
  },
  {
    "name": "Paul Kind",
    "member_affiliation": "Health Economics Policy Lab (HEPL), University College London",
    "is_member": true,
    "projects": [
      {
        "project_id": "1583-RA",
        "title": "Testing the ordinal relationship between TTO utilities and the ranking of EQ-5D health states : examining the commensurability of preferences in the MVH dataset",
        "working_group": "Valuation"
      },
      {
        "project_id": "1786-RA",
        "title": "An empirical analysis of the EQ-5D Anxiety/Depression dimension : investigating the Humpty Dumpty phenomenon using general population data",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2009018",
        "title": "measuring population health status using a web-based implementation of EQ-5D",
        "working_group": "Others"
      },
      {
        "project_id": "2010011",
        "title": "exploration of differences between EQ-5D-3L and EQ-5D-Y",
        "working_group": "Youth"
      },
      {
        "project_id": "2014120",
        "title": "LSHA Workshop",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2014220",
        "title": "Temporal variation in population health in England",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2015350",
        "title": "Demonstrating the feasibility and operational value of the routine measurement of health status in community mental health services: exploring the use of EQ-5D in an operational NHS setting",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2015420",
        "title": "A City-wide survey of HrQoL in children using EQ-5D-Y",
        "working_group": "Youth"
      },
      {
        "project_id": "2016050",
        "title": "2-day entry level course describing development and current status of EQ-5D ”technologies” for Russia",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2016200",
        "title": "Clik 2016",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20191040",
        "title": "Learning from 5L valuation studies : Investigating differences in preference structures",
        "working_group": "Valuation"
      },
      {
        "project_id": "20191050",
        "title": "Using EQ-5D to inform real-world decision making : a cross-sectoral perspective",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "78-RA",
        "title": "Measuring population health status at a time of national crisis",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5013594779",
      "display_name": "Paul Kind",
      "orcid": "0000-0003-2377-1652",
      "reported_affiliation": "University of Leeds",
      "works_count": 240,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 140
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 40
        },
        {
          "topic": "Global Health Care Issues",
          "works": 33
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 31
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 14
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 13
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 9
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 9
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 8
        },
        {
          "topic": "Prostate Cancer Diagnosis and Treatment",
          "works": 8
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 7
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Penny Wright",
          "works": 21
        },
        {
          "name": "Amy Downing",
          "works": 14
        },
        {
          "name": "Claire Gudex",
          "works": 13
        },
        {
          "name": "Richard Wagland",
          "works": 13
        },
        {
          "name": "Adam Glaser",
          "works": 13
        },
        {
          "name": "Xavier Badı́a",
          "works": 12
        },
        {
          "name": "Ling‐Hsiang Chuang",
          "works": 12
        },
        {
          "name": "Paul Dolan",
          "works": 11
        },
        {
          "name": "V Zárate",
          "works": 11
        },
        {
          "name": "Luke Hounsome",
          "works": 10
        },
        {
          "name": "Hugh Butcher",
          "works": 10
        },
        {
          "name": "Kristina Burström",
          "works": 9
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4409834181",
          "year": 2025,
          "title": "Exploring the origin and conceptual framework of the EQ VAS",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4417482296",
          "year": 2025,
          "title": "P1 Predicting EQ-5D Index Scores: A Comparison Study of Machine Learning and Statistical Methods on Health Survey for England Data",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W4414663954",
          "year": 2025,
          "title": "Self-reported health status in the general population over 2 decades: variation in EQ-5D-3L in Health Survey for England",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W4391311525",
          "year": 2024,
          "title": "A Comparison of Items and Constructs of Standardized Health-Related Quality of Life and Mental Well-Being Measures",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 5,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychological Well-being and Life Satisfaction",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W4396217404",
          "year": 2024,
          "title": "Adapting the EQ-5D-3L for adults with mild to moderate learning disabilities",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 5,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Down syndrome and intellectual disability research",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W4405749743",
          "year": 2024,
          "title": "PCR281 Assessing Internal Structure, Psychometric Properties, and Explanatory Power of Self-Complete EQ-5D-Y and CHU-9D in Children With Specific Phobia",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Attention Deficit Hyperactivity Disorder"
          ]
        },
        {
          "openalex_id": "W2087141923",
          "year": 1968,
          "title": "Dermatofibroma of the Eyelid",
          "type": "article",
          "venue": "American Journal of Ophthalmology",
          "cited_by_count": 6,
          "topics": [
            "Soft tissue tumor case studies",
            "Cancer and Skin Lesions",
            "Sarcoma Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2137292463",
          "year": 1978,
          "title": "A Scale of Valuations of States of Illness: is there a Social Consensus?",
          "type": "article",
          "venue": "International Journal of Epidemiology",
          "cited_by_count": 465,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W169295556",
          "year": 1979,
          "title": "Death and Dying: Scaling of Death for Health Status Indices",
          "type": "book-chapter",
          "venue": "Lecture notes in medical informatics",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2044818801",
          "year": 1982,
          "title": "A Comparison of Two Models for Scaling Health Indicators",
          "type": "article",
          "venue": "International Journal of Epidemiology",
          "cited_by_count": 29,
          "topics": [
            "Health disparities and outcomes"
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
          "openalex_id": "W2164024605",
          "year": 1997,
          "title": "Measuring health-related quality of life in rheumatoid arthritis: validity, responsiveness and reliability of EuroQol (EQ-5D)",
          "type": "article",
          "venue": "Lara D. Veeken",
          "cited_by_count": 852,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Rheumatoid Arthritis Research and Therapies",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W2028873098",
          "year": 1993,
          "title": "Testing the validity of the Euroqol and comparing it with the SF-36 health survey questionnaire",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 709,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Global Health Care Issues"
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
        }
      ]
    }
  },
  {
    "name": "Paul Krabbe",
    "member_affiliation": "University Medical Center Groningen",
    "is_member": true,
    "projects": [
      {
        "project_id": "2014150",
        "title": "Discrete choice modeling from a different angle",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5061371202",
      "display_name": "Paul F. M. Krabbe",
      "orcid": "0000-0001-6042-1243",
      "reported_affiliation": "University Medical Center Groningen",
      "works_count": 266,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 100
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 31
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 16
        },
        {
          "topic": "Hepatocellular Carcinoma Treatment and Prognosis",
          "works": 16
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 16
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 14
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 13
        },
        {
          "topic": "Medical Imaging Techniques and Applications",
          "works": 12
        },
        {
          "topic": "Radiomics and Machine Learning in Medical Imaging",
          "works": 11
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 11
        },
        {
          "topic": "Head and Neck Cancer Studies",
          "works": 10
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 10
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Wim J.G. Oyen",
          "works": 29
        },
        {
          "name": "Maarten J. Postma",
          "works": 23
        },
        {
          "name": "Karin M. Vermeulen",
          "works": 21
        },
        {
          "name": "Theo J. M. Ruers",
          "works": 19
        },
        {
          "name": "Marcel G. M. Olde Rikkert",
          "works": 17
        },
        {
          "name": "C.A.J. de Jong",
          "works": 15
        },
        {
          "name": "Eddy Adang",
          "works": 12
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 11
        },
        {
          "name": "Marie‐Louise Essink‐Bot",
          "works": 11
        },
        {
          "name": "Lioe‐Fee de Geus‐Oei",
          "works": 11
        },
        {
          "name": "B. Wiering",
          "works": 10
        },
        {
          "name": "Jennifer E. Lutomski",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4408537979",
          "year": 2025,
          "title": "Parent-Reported Health-Related Quality of Life (HRQoL) of NICU Graduates in Their First Year: A Prospective Cohort Study",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W4394573787",
          "year": 2024,
          "title": "Early stress during NICU stay and parent-reported health-related quality of life after extremely preterm birth: an exploratory study with possible targets for early intervention",
          "type": "article",
          "venue": "Frontiers in Pediatrics",
          "cited_by_count": 5,
          "topics": [
            "Infant Development and Preterm Care",
            "Neonatal Respiratory Health Research",
            "Maternal Mental Health During Pregnancy and Postpartum"
          ]
        },
        {
          "openalex_id": "W4400381115",
          "year": 2024,
          "title": "Generating Utilities for the Château-Santé Base: A Novel, Generic, and Patient-Centered Health-Outcome Measure",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W4404795475",
          "year": 2024,
          "title": "Lifestyle factors and incident multimorbidity related to chronic disease: a population-based cohort study",
          "type": "article",
          "venue": "European Journal of Ageing",
          "cited_by_count": 25,
          "topics": [
            "Chronic Disease Management Strategies",
            "Diabetes Management and Education",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W4405259863",
          "year": 2024,
          "title": "Measuring health-related quality of life in cardiovascular disease using a novel patient-centred and disease-specific patient-reported outcome measure",
          "type": "article",
          "venue": "International Journal of Cardiology Cardiovascular Risk and Prevention",
          "cited_by_count": 0,
          "topics": [
            "Cardiac Health and Mental Health",
            "Cardiovascular Health and Risk Factors",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4389832895",
          "year": 2023,
          "title": "Correction to: Different Frameworks, Similar Results? Head-to-Head Comparison of the Generic Preference-Based Health-Outcome Measures CS-Base and EQ-5D-5L",
          "type": "erratum",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2038526368",
          "year": 1993,
          "title": "The paradoxical nature of sexuality in anorexia nervosa",
          "type": "article",
          "venue": "Journal of Sex & Marital Therapy",
          "cited_by_count": 43,
          "topics": [
            "Eating Disorders and Behaviors",
            "Sexuality, Behavior, and Technology",
            "Obsessive-Compulsive Spectrum Disorders"
          ]
        },
        {
          "openalex_id": "W1973560164",
          "year": 1994,
          "title": "Test-retest reliability of health state valuations collected with the EuroQol questionnaire",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 348,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Advanced Causal Inference Techniques",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W787899159",
          "year": 1995,
          "title": "De vergelijking van 4 methoden voor de waardering van gezondheidstoestanden (abstract)",
          "type": "article",
          "venue": "Radboud Repository (Radboud University)",
          "cited_by_count": 0,
          "topics": [
            "Dutch Social and Cultural Studies",
            "Health Policy Implementation Science",
            "Health Promotion and Cardiovascular Prevention"
          ]
        },
        {
          "openalex_id": "W2043866079",
          "year": 1995,
          "title": "The Impact of Migraine on Health Status",
          "type": "article",
          "venue": "Headache The Journal of Head and Face Pain",
          "cited_by_count": 71,
          "topics": [
            "Migraine and Headache Studies",
            "Traumatic Brain Injury Research",
            "Neurological Complications and Syndromes"
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
          "openalex_id": "W2133094593",
          "year": 2006,
          "title": "Prostate Cancer Localization with Dynamic Contrast-enhanced MR Imaging and Proton MR Spectroscopic Imaging",
          "type": "article",
          "venue": "Radiology",
          "cited_by_count": 520,
          "topics": [
            "MRI in cancer diagnosis",
            "Prostate Cancer Diagnosis and Treatment",
            "Radiomics and Machine Learning in Medical Imaging"
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
          "openalex_id": "W2123969858",
          "year": 2014,
          "title": "A Program of Methodological Research to Arrive at the New International EQ-5D-5L Valuation Protocol",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 439,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Quality and Management",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2040248981",
          "year": 2007,
          "title": "A Prospective Multicenter Study on Fever of Unknown Origin",
          "type": "article",
          "venue": "Medicine",
          "cited_by_count": 404,
          "topics": [
            "Hematological disorders and diagnostics",
            "Streptococcal Infections and Treatments",
            "Orthopedic Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W2013864512",
          "year": 2001,
          "title": "Effect of folic or folinic acid supplementation on the toxicity and efficacy of methotrexate in rheumatoid arthritis: A forty-eight-week, multicenter, randomized, double-blind, placebo-controlled study",
          "type": "article",
          "venue": "Arthritis & Rheumatism",
          "cited_by_count": 399,
          "topics": [
            "Folate and B Vitamins Research",
            "Rheumatoid Arthritis Research and Therapies",
            "Acute Lymphoblastic Leukemia research"
          ]
        },
        {
          "openalex_id": "W2166606788",
          "year": 2000,
          "title": "Development and application of a health‐related quality‐of‐life instrument for adults with cochlear implants: The Nijmegen Cochlear Implant Questionnaire",
          "type": "article",
          "venue": "Otolaryngology",
          "cited_by_count": 393,
          "topics": [
            "Hearing Loss and Rehabilitation",
            "Hearing Impairment and Communication",
            "Hearing, Cochlea, Tinnitus, Genetics"
          ]
        }
      ]
    }
  },
  {
    "name": "Paula Lorgelly",
    "member_affiliation": "University of Auckland | Waipapa Taumata Rau",
    "is_member": true,
    "projects": [
      {
        "project_id": "1573-RA",
        "title": "Exploring inequalities in HRQoL in long COVID in Aotearoa New Zealand",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1655-EO",
        "title": "IHEA Pre-congress session on EQ-5D as a measure of population health, plus sponsorship of 7 LMIC ECR delegates to attend IHEA",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1680-RA",
        "title": "System-level PROM collection and EQ instruments: the current state of play",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1881-RA",
        "title": "From Routine Collection to Routine Care: Understanding the Barriers and Facilitators to Greater Adoption of PROMs in Clinical Practice",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20191030",
        "title": "Investigating response heterogeneity in the EQ-5D",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2053-EO",
        "title": "IHEA Pre-congress session on EQ-5D in the Indo-Pacific Region",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2443-BT",
        "title": "Psychometric testing of cognition, fatigue and breathing bolt-ons in a cohort with long COVID",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "291-RA",
        "title": "HRQoL in Post-COVID syndrome patients in the UK: exploring EQ-5D in a new and emerging chronic condition",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5027424571",
      "display_name": "Paula Lorgelly",
      "orcid": "0000-0002-8990-9514",
      "reported_affiliation": "University of Auckland",
      "works_count": 203,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 64
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 25
        },
        {
          "topic": "Global Health Care Issues",
          "works": 20
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 13
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 13
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 12
        },
        {
          "topic": "Long-Term Effects of COVID-19",
          "works": 12
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 11
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 10
        },
        {
          "topic": "Cancer Genomics and Diagnostics",
          "works": 10
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 9
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 9
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Amitava Banerjee",
          "works": 13
        },
        {
          "name": "Miranda Mugford",
          "works": 12
        },
        {
          "name": "Andrew Briggs",
          "works": 11
        },
        {
          "name": "Brett Doble",
          "works": 10
        },
        {
          "name": "Vageesh Jain",
          "works": 9
        },
        {
          "name": "Bruce Hollingsworth",
          "works": 8
        },
        {
          "name": "David M. Ashley",
          "works": 8
        },
        {
          "name": "Stephen B. Fox",
          "works": 8
        },
        {
          "name": "Melissa Heightman",
          "works": 8
        },
        {
          "name": "Amanda Cole",
          "works": 8
        },
        {
          "name": "Richard Norman",
          "works": 7
        },
        {
          "name": "David M. Thomas",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7140039069",
          "year": 2026,
          "title": "In the next pandemic, NZ doesn’t need to choose between health and the economy",
          "type": "other",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Systems and Challenges",
            "Global Public Health Policies and Epidemiology",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W4411540033",
          "year": 2025,
          "title": "Does pay for performance affect socioeconomic inequalities in access? Evidence from hospital specialised care in England",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Primary Care and Health Outcomes",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W4408731374",
          "year": 2025,
          "title": "Equity in health care and health: Contributions from health economics",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 2,
          "topics": [
            "Healthcare Policy and Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4417480899",
          "year": 2025,
          "title": "MSR64 Country-Related Differential Item Functioning in the EQ-5D-5L: Insights From the EuroQol Data Assessment of Population Health Needs and Instrument Evaluation (EQ-DAPHNIE)",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4412442858",
          "year": 2025,
          "title": "PCR141 Estimating the HRQoL Shortfall of Long COVID: Meta Analysis of Cohort Studies Relative to Population Norms",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W4412443369",
          "year": 2025,
          "title": "PT36 Psychometric Evidence Supporting the Use of the EQ-5D in Long COVID: A Systematic Review",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Long-Term Effects of COVID-19",
            "Mosquito-borne diseases and control",
            "Multiple Sclerosis Research Studies"
          ]
        },
        {
          "openalex_id": "W2036161518",
          "year": 1999,
          "title": "The effect of female and male schooling on economic growth in the Barro-Lee model",
          "type": "article",
          "venue": "Empirical Economics",
          "cited_by_count": 68,
          "topics": [
            "Fiscal Policy and Economic Growth",
            "Economic Growth and Productivity",
            "Gender, Labor, and Family Dynamics"
          ]
        },
        {
          "openalex_id": "W3123620150",
          "year": 2000,
          "title": "The Effect of Female and Male Schooling on Economic Growth in the Barro-Lee Model",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 2,
          "topics": [
            "Fiscal Policy and Economic Growth"
          ]
        },
        {
          "openalex_id": "W2010842593",
          "year": 2001,
          "title": "Barro's fertility equations: the robustness of the role of female education and income",
          "type": "article",
          "venue": "Applied Economics",
          "cited_by_count": 5,
          "topics": [
            "Economic Growth and Productivity",
            "Fiscal Policy and Economic Growth",
            "Income, Poverty, and Inequality"
          ]
        },
        {
          "openalex_id": "W3125640814",
          "year": 2001,
          "title": "Barro's fertility equations: the robustness of the role of female education and income",
          "type": "article",
          "venue": "Applied Economics",
          "cited_by_count": 1,
          "topics": [
            "Economic Growth and Productivity",
            "Gender, Labor, and Family Dynamics",
            "Fiscal Policy and Economic Growth"
          ]
        },
        {
          "openalex_id": "W1997284773",
          "year": 2008,
          "title": "Welfarism, extra-welfarism and capability: The spread of ideas in health economics",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 168,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W4318624517",
          "year": 2023,
          "title": "The Use of a Discrete Choice Experiment Including Both Duration and Dead for the Development of an EQ-5D-5L Value Set for Australia",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 163,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2025430995",
          "year": 2008,
          "title": "Should the capability approach be applied in Health Economics?",
          "type": "editorial",
          "venue": "Health Economics",
          "cited_by_count": 142,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4317499944",
          "year": 2023,
          "title": "The impact of the COVID-19 pandemic on cardiovascular disease prevention and management",
          "type": "article",
          "venue": "Nature Medicine",
          "cited_by_count": 139,
          "topics": [
            "COVID-19 and healthcare impacts",
            "COVID-19 Clinical Research Studies",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2013817492",
          "year": 2010,
          "title": "Outcome Measurement in Economic Evaluations of Public Health Interventions: a Role for the Capability Approach?",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 137,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2006959783",
          "year": 2007,
          "title": "What is the relationship between income inequality and health? Evidence from the BHPS",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 122,
          "topics": [
            "Health disparities and outcomes",
            "Global Health Care Issues",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W2012479964",
          "year": 2013,
          "title": "A Qualitative Assessment of the Content Validity of the ICECAP-A and EQ-5D-5L and Their Appropriateness for Use in Health Research",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 97,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W2118056731",
          "year": 2015,
          "title": "Operationalising the capability approach as an outcome measure in public health: The development of the OCAP-18",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 91,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Health disparities and outcomes"
          ]
        }
      ]
    }
  },
  {
    "name": "Pedro Ferreira",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2015110",
        "title": "Estimation of the EQ-5D-5L value set for Portugal",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5048178253",
      "display_name": "Pedro Lopes Ferreira",
      "orcid": "0000-0002-9448-9542",
      "reported_affiliation": "University of Lisbon",
      "works_count": 347,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 48
        },
        {
          "topic": "Health, Nursing, Elderly Care",
          "works": 35
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 31
        },
        {
          "topic": "Global Health Care Issues",
          "works": 23
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 22
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 15
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 14
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 14
        },
        {
          "topic": "Palliative and Oncologic Care",
          "works": 14
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 13
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 13
        },
        {
          "topic": "Public Health in Brazil",
          "works": 13
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Lara Noronha Ferreira",
          "works": 38
        },
        {
          "name": "Luís Nobre Pereira",
          "works": 24
        },
        {
          "name": "Irene J Higginson",
          "works": 22
        },
        {
          "name": "Bárbara Gomes",
          "works": 15
        },
        {
          "name": "Rui Soles Gonçalves",
          "works": 15
        },
        {
          "name": "Bárbara Antunes",
          "works": 14
        },
        {
          "name": "Rui Pimenta",
          "works": 14
        },
        {
          "name": "Luís Manuel Cavalheiro",
          "works": 14
        },
        {
          "name": "Aida Isabel Tavares",
          "works": 13
        },
        {
          "name": "Luc Deliëns",
          "works": 10
        },
        {
          "name": "Barbara A Daveson",
          "works": 10
        },
        {
          "name": "Claudia Bausewein",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4413278172",
          "year": 2025,
          "title": "CGD-MAE: Clip Distillation-Driven Pre-Training Framework for Vehicle Re-Identification",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Fault Detection and Control Systems",
            "Hydraulic and Pneumatic Systems",
            "Control Systems and Identification"
          ]
        },
        {
          "openalex_id": "W4414926175",
          "year": 2025,
          "title": "Conflict in the North of Mozambique",
          "type": "article",
          "venue": "BULLETIN OF CAROL I NATIONAL DEFENCE UNIVERSITY",
          "cited_by_count": 2,
          "topics": [
            "African history and culture analysis"
          ]
        },
        {
          "openalex_id": "W4407354962",
          "year": 2025,
          "title": "Corrigendum: A meta-analysis on the role of sonication in the diagnosis of cardiac implantable electronic device-related infections",
          "type": "erratum",
          "venue": "Frontiers in Microbiology",
          "cited_by_count": 0,
          "topics": [
            "Cardiac pacing and defibrillation studies"
          ]
        },
        {
          "openalex_id": "W4408246708",
          "year": 2025,
          "title": "Cross-Cultural Adaptation and Validation of the Portuguese Version of the “Australian Pelvic Floor Questionnaire”",
          "type": "article",
          "venue": "International Urogynecology Journal",
          "cited_by_count": 0,
          "topics": [
            "Pelvic floor disorders treatments",
            "Gastrointestinal motility and disorders",
            "Anorectal Disease Treatments and Outcomes"
          ]
        },
        {
          "openalex_id": "W4408350891",
          "year": 2025,
          "title": "Cuidados paliativos na atenção básica: uma investigação sobre o conhecimento público em Imperatriz – MA",
          "type": "article",
          "venue": "Brazilian Journal of Health Review",
          "cited_by_count": 0,
          "topics": [
            "Palliative and Oncologic Care",
            "Psychology and Mental Health",
            "Health, Nursing, Elderly Care"
          ]
        },
        {
          "openalex_id": "W4406268337",
          "year": 2025,
          "title": "Digital health in Portugal: Exploring perceptions, barriers, and experiences through a focus group study",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Digital Mental Health Interventions",
            "Mobile Health and mHealth Applications",
            "Telemedicine and Telehealth Implementation"
          ]
        },
        {
          "openalex_id": "W2604538575",
          "year": 1985,
          "title": "Sistema de informação clínica automatizado do Hospital Pediátrico de Coimbra",
          "type": "article",
          "venue": "Estudo Geral (Universidade de Coimbra)",
          "cited_by_count": 0,
          "topics": [
            "Electronic Health Records Systems",
            "Context-Aware Activity Recognition Systems",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W4416326005",
          "year": 1990,
          "title": "Estudo da transformação ordem-desordem na liga FeCo-2%V encruada",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Magnetic Properties and Applications",
            "Magnetic properties of thin films",
            "Metallic Glasses and Amorphous Alloys"
          ]
        },
        {
          "openalex_id": "W2602912087",
          "year": 1990,
          "title": "Structure-process-outcome: a causal model for quality in nursing homes",
          "type": "other",
          "venue": "Portuguese National Funding Agency for Science, Research and Technology (RCAAP Project by FCT)",
          "cited_by_count": 1,
          "topics": [
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W2306116434",
          "year": 1991,
          "title": "Definir e Medir a Qualidade de Cuidados de Saúde",
          "type": "article",
          "venue": "Portuguese National Funding Agency for Science, Research and Technology (RCAAP Project by FCT)",
          "cited_by_count": 3,
          "topics": [
            "Health, Nursing, Elderly Care"
          ]
        },
        {
          "openalex_id": "W2100910330",
          "year": 2012,
          "title": "Preferences for place of death if faced with advanced cancer: a population survey in England, Flanders, Germany, Italy, the Netherlands, Portugal and Spain",
          "type": "article",
          "venue": "Annals of Oncology",
          "cited_by_count": 559,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Cancer survivorship and care",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W3007172259",
          "year": 2016,
          "title": "Proceedings of the 3rd IPLeiria’s International Health Congress",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 462,
          "topics": [
            "Digital Mental Health Interventions",
            "Child and Adolescent Health"
          ]
        },
        {
          "openalex_id": "W4380204422",
          "year": 2023,
          "title": "Sociodemographic determinants of digital health literacy: A systematic review and meta-analysis",
          "type": "review",
          "venue": "International Journal of Medical Informatics",
          "cited_by_count": 367,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Mobile Health and mHealth Applications",
            "Social Media in Health Education"
          ]
        },
        {
          "openalex_id": "W1906671210",
          "year": 2000,
          "title": "Patients in Europe evaluate general practice care: an international comparison.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 296,
          "topics": [
            "Primary Care and Health Outcomes",
            "Patient Satisfaction in Healthcare",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2170953792",
          "year": 1999,
          "title": "Patients' priorities with respect to general practice care: an international comparison",
          "type": "article",
          "venue": "Family Practice",
          "cited_by_count": 295,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Primary Care and Health Outcomes",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W1756291139",
          "year": 2015,
          "title": "EAPC White Paper on outcome measurement in palliative care: Improving practice, attaining outcomes and delivering quality services – Recommendations from the European Association for Palliative Care (EAPC) Task Force on Outcome Measurement",
          "type": "article",
          "venue": "Palliative Medicine",
          "cited_by_count": 254,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Cancer survivorship and care",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W1561653992",
          "year": 2008,
          "title": "[Measuring quality of life in palliative care].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 254,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Palliative and Oncologic Care",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2116817969",
          "year": 2015,
          "title": "Reliability and validity of the Portuguese version of the Generalized Anxiety Disorder (GAD-7) scale",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 240,
          "topics": [
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes",
            "Mental Health Treatment and Access",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        }
      ]
    }
  }
]
