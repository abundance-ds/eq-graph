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
    "name": "Liv Ariane Augestad",
    "member_affiliation": "University of Oslo",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5054297438",
      "display_name": "Liv Ariane Augestad",
      "orcid": "0000-0003-3330-5081",
      "reported_affiliation": "University of Oslo",
      "works_count": 31,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 23
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 11
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 9
        },
        {
          "topic": "Frailty in Older Adults",
          "works": 4
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 2
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 2
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 2
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 2
        },
        {
          "topic": "European and International Law Studies",
          "works": 2
        },
        {
          "topic": "Ethics and Legal Issues in Pediatric Healthcare",
          "works": 2
        },
        {
          "topic": "Global Health Care Issues",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kim Rand",
          "works": 12
        },
        {
          "name": "Knut Stavem",
          "works": 10
        },
        {
          "name": "Mathias Barra",
          "works": 10
        },
        {
          "name": "Ivar Sønbø Kristiansen",
          "works": 7
        },
        {
          "name": "Yvonne Michel",
          "works": 4
        },
        {
          "name": "David G. T. Whitehurst",
          "works": 4
        },
        {
          "name": "Andrew Garratt",
          "works": 3
        },
        {
          "name": "T. Hansen",
          "works": 3
        },
        {
          "name": "Nan Luo",
          "works": 3
        },
        {
          "name": "Fredrik A. Dahl",
          "works": 2
        },
        {
          "name": "Tilde Østborg",
          "works": 2
        },
        {
          "name": "Samantha S. Adams",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4399173182",
          "year": 2024,
          "title": "Healthcare use and costs in the last six months of life by level of care and cause of death",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 7,
          "topics": [
            "Frailty in Older Adults",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W7117510648",
          "year": 2023,
          "title": "Evaluering av handlingsplan for allmennlegetjenesten 2020-2024",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "European and International Law Studies",
            "Education, Healthcare and Sociology Research",
            "Government, Law, and Information Management"
          ]
        },
        {
          "openalex_id": "W4281381746",
          "year": 2022,
          "title": "194:oral Severity and EQ-5D: when health state value and moral value differ",
          "type": "conference-abstract",
          "venue": "Abstracts",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W4250176567",
          "year": 2021,
          "title": "Norwegian Population Norms for the EQ-5D-5L: Results From a General Population Survey",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 8,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W3139504198",
          "year": 2021,
          "title": "Norwegian population norms for the EQ-5D-5L: results from a general population survey",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 128,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W3034926783",
          "year": 2020,
          "title": "Elicitation of Norwegian EQ-5D-5L values for hypothetical and experience-based health states based on the EuroQol Valuation Technology (EQ-VT) protocol",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 27,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W1985215603",
          "year": 2011,
          "title": "Comparison of hypothetical and experienced EQ-5D valuations: relative weights of the five dimensions",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 44,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2118069093",
          "year": 2012,
          "title": "A Shortcut to Mean-Based Time Tradeoff Tariffs for the EQ-5D?",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 15,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2136043900",
          "year": 2012,
          "title": "A critical re-evaluation of the regression model specification in the US D1 EQ-5D value function",
          "type": "article",
          "venue": "Population Health Metrics",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2148968274",
          "year": 2012,
          "title": "Impact of Transformation of Negative Values and Regression Models on Differences Between the UK and US EQ-5D Time Trade-Off Value Sets",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 12,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Primary Care and Health Outcomes",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2897465631",
          "year": 2018,
          "title": "General population norms for the EQ-5D-3 L in Norway: comparison of postal and web surveys",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 73,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2613980321",
          "year": 2017,
          "title": "Less Is More: Cross-Validation Testing of Simplified Nonlinear Regression Model Specifications for EQ-5D-5L Health State Values",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 36,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W3022784450",
          "year": 2020,
          "title": "The association of stroke severity with health-related quality of life in survivors of acute cerebrovascular disease and their informal caregivers during the first year post stroke: a survey study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 26,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management",
            "Intracerebral and Subarachnoid Hemorrhage Research"
          ]
        },
        {
          "openalex_id": "W2077287416",
          "year": 2012,
          "title": "Time trade-off and attitudes toward euthanasia: implications of using ‘death’ as an anchor in health state valuation",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 24,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Palliative Care and End-of-Life Issues",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2163857207",
          "year": 2012,
          "title": "Learning Effects in Time Trade-Off Based Valuation of EQ-5D Health States",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 23,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Quality and Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Louise Longworth",
    "member_affiliation": "Arrow Health Economics",
    "is_member": true,
    "projects": [
      {
        "project_id": "2013190",
        "title": "Overview of psychometric properties of EQ-5D in a range of conditions",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016300",
        "title": "Methods for development of a generic descriptive system",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20200020",
        "title": "Establishment of a UK EuroQol Group and initial 1 day meeting",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2115-EOI",
        "title": "Meeting of EQ-5D researchers in the UK and Ireland",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5046647690",
      "display_name": "Louise Longworth",
      "orcid": "0000-0003-2512-4862",
      "reported_affiliation": "Arrow International (United States)",
      "works_count": 216,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 108
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 30
        },
        {
          "topic": "Liver Disease Diagnosis and Treatment",
          "works": 19
        },
        {
          "topic": "Liver Disease and Transplantation",
          "works": 15
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 14
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 14
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 13
        },
        {
          "topic": "Hepatitis C virus research",
          "works": 9
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 7
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 7
        },
        {
          "topic": "Global Health Care Issues",
          "works": 6
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "John Brazier",
          "works": 50
        },
        {
          "name": "Donna Rowen",
          "works": 47
        },
        {
          "name": "Brendan Mulhern",
          "works": 45
        },
        {
          "name": "Aki Tsuchiya",
          "works": 40
        },
        {
          "name": "Tracey Young",
          "works": 27
        },
        {
          "name": "Emmanuel Tsochatzis",
          "works": 26
        },
        {
          "name": "Catriona Crossan",
          "works": 25
        },
        {
          "name": "Kurinchi Selvan Gurusamy",
          "works": 25
        },
        {
          "name": "Nick Bansback",
          "works": 25
        },
        {
          "name": "Nancy Devlin",
          "works": 24
        },
        {
          "name": "Yaling Yang",
          "works": 23
        },
        {
          "name": "Manuel Rodríguez‐Perálvarez",
          "works": 22
        }
      ],
      "work_examples": [
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
          "openalex_id": "W4411748481",
          "year": 2025,
          "title": "The Economic Burden of Anti-Vascular Endothelial Growth Factor on Patients and Caregivers in the UK, Europe, and North America",
          "type": "article",
          "venue": "Ophthalmology and Therapy",
          "cited_by_count": 9,
          "topics": [
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies",
            "Ocular Diseases and Behçet’s Syndrome"
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
          "openalex_id": "W4401544475",
          "year": 2024,
          "title": "A scoping review of the use of minimally important difference of EQ-5D utility index and EQ-VAS scores in health technology assessment",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 12,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4392506596",
          "year": 2024,
          "title": "A time trade-off study to determine health-state utilities of transplant recipients with refractory cytomegalovirus infection with or without resistance",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 3,
          "topics": [
            "Cytomegalovirus and herpesvirus research",
            "Viral Infections and Immunology Research",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4393350116",
          "year": 2024,
          "title": "An eye on equity: faricimab-driven health equity improvements in diabetic macular oedema using a distributional cost-effectiveness analysis from a UK societal perspective",
          "type": "article",
          "venue": "Eye",
          "cited_by_count": 9,
          "topics": [
            "Retinal Diseases and Treatments",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W1967344541",
          "year": 1999,
          "title": "SD1: USING CONJOINT ANALYSIS TO ASSESS WOMEN'S PREFERENCES FOR MATERNITY CARE SERVICES DURING THE INTRAPARTUM STAGE",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1966467748",
          "year": 2001,
          "title": "A comparison of survival, with and in the absence of, liver transplantation in the absence of a non-transplant cohort: the case of alcoholic cirrhosis",
          "type": "article",
          "venue": "Journal of Hepatology",
          "cited_by_count": 0,
          "topics": [
            "Liver Disease Diagnosis and Treatment",
            "Liver Disease and Transplantation",
            "Alcohol Consumption and Health Effects"
          ]
        },
        {
          "openalex_id": "W1988562518",
          "year": 2001,
          "title": "Assessing the health-related quality of life of liver transplant recipients in England and Wales",
          "type": "article",
          "venue": "Journal of Hepatology",
          "cited_by_count": 0,
          "topics": [
            "Liver Disease and Transplantation",
            "Organ Transplantation Techniques and Outcomes",
            "Hepatitis C virus research"
          ]
        },
        {
          "openalex_id": "W2026514473",
          "year": 2001,
          "title": "Investigating women’s preferences for intrapartum care: home versus hospital births",
          "type": "article",
          "venue": "Health & Social Care in the Community",
          "cited_by_count": 90,
          "topics": [
            "Maternal and Perinatal Health Interventions",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2133275424",
          "year": 2014,
          "title": "Addressing liver disease in the UK: a blueprint for attaining excellence in health care and reducing premature mortality from lifestyle issues of excess consumption of alcohol, obesity, and viral hepatitis",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 604,
          "topics": [
            "Liver Disease Diagnosis and Treatment",
            "Alcohol Consumption and Health Effects",
            "Liver Disease and Transplantation"
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
          "openalex_id": "W2320150092",
          "year": 2016,
          "title": "The EQ-5D-5L health status questionnaire in COPD: validity, responsiveness and minimum important difference",
          "type": "article",
          "venue": "Thorax",
          "cited_by_count": 318,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Delphi Technique in Research"
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
          "openalex_id": "W1979971995",
          "year": 2003,
          "title": "An empirical comparison of EQ‐5D and SF‐6D in liver transplant patients",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 184,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2055475477",
          "year": 2015,
          "title": "Cost-effectiveness of non-invasive methods for assessment and monitoring of liver fibrosis and cirrhosis in patients with chronic liver disease: systematic review and economic evaluation",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 166,
          "topics": [
            "Liver Disease Diagnosis and Treatment",
            "Liver Disease and Transplantation",
            "Alcohol Consumption and Health Effects"
          ]
        },
        {
          "openalex_id": "W2530421404",
          "year": 2016,
          "title": "Proceedings of Patient Reported Outcome Measure’s (PROMs) Conference Sheffield 2016: advances in patient reported outcomes research",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 152,
          "topics": [
            "Primary Care and Health Outcomes",
            "Chronic Disease Management Strategies",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2029389948",
          "year": 2011,
          "title": "A Review of Generic Preference-Based Measures of Health-Related Quality of Life in Visual Disorders",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 144,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Retinal Diseases and Treatments"
          ]
        }
      ]
    }
  },
  {
    "name": "Lucila Rey Ares",
    "member_affiliation": "",
    "is_member": true,
    "projects": [
      {
        "project_id": "2015340",
        "title": "EQ-5D for monitoring population health: a comparison of general population survey data in Argentina, Brazil, Chile and Uruguay",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2016340",
        "title": "Uses and applications of EQ-5D in Latin America & the Caribbean - Systematic Review and bibliometric study",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5045433583",
      "display_name": "Lucila Rey Ares",
      "orcid": "",
      "reported_affiliation": "Pfizer (United States)",
      "works_count": 25,
      "top_topics": [
        {
          "topic": "Trypanosoma species research and implications",
          "works": 3
        },
        {
          "topic": "Respiratory viral infections research",
          "works": 3
        },
        {
          "topic": "Syphilis Diagnosis and Treatment",
          "works": 3
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 3
        },
        {
          "topic": "Hepatitis C virus research",
          "works": 3
        },
        {
          "topic": "Effects and risks of endocrine disrupting chemicals",
          "works": 3
        },
        {
          "topic": "Public Health and Environmental Issues",
          "works": 3
        },
        {
          "topic": "Viral Infections and Immunology Research",
          "works": 2
        },
        {
          "topic": "Viral gastroenteritis research and epidemiology",
          "works": 2
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 2
        },
        {
          "topic": "Pneumocystis jirovecii pneumonia detection and treatment",
          "works": 2
        },
        {
          "topic": "HIV/AIDS drug development and treatment",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sebastián García Martí",
          "works": 9
        },
        {
          "name": "Andrea Alcaraz",
          "works": 6
        },
        {
          "name": "Agustín Ciapponi",
          "works": 5
        },
        {
          "name": "Ariel Bardach",
          "works": 5
        },
        {
          "name": "Demián Glujovsky",
          "works": 4
        },
        {
          "name": "Karen Klein",
          "works": 4
        },
        {
          "name": "Federico Augustovski",
          "works": 4
        },
        {
          "name": "Joaquín Caporale",
          "works": 4
        },
        {
          "name": "María Soledad Burrone",
          "works": 3
        },
        {
          "name": "Juan Pedro Alonso",
          "works": 3
        },
        {
          "name": "Antonia Lavenia",
          "works": 3
        },
        {
          "name": "Vanessa Elías",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4417481106",
          "year": 2025,
          "title": "EPH53 Cost-Effectiveness Analysis of the 13-Valent Pneumococcal Conjugate Vaccine Compared With Higher-Valent Alternatives in the Pediatric Population of Paraguay",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Pneumonia and Respiratory Infections",
            "Respiratory viral infections research",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W4403865393",
          "year": 2024,
          "title": "Clinical evolution and medical resource utilization in adult patients with respiratory syncytial virus infection at a community hospital in Argentina",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Respiratory viral infections research",
            "Public Health and Environmental Issues"
          ]
        },
        {
          "openalex_id": "W4405748233",
          "year": 2024,
          "title": "EE276 Budget Impact Analysis of RSVpreF Vaccine for Prevention of Respiratory Syncytial Virus (RSV) Disease Among Older Adults in Argentina",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Public Health and Environmental Issues",
            "Vaccine Coverage and Hesitancy"
          ]
        },
        {
          "openalex_id": "W4405752082",
          "year": 2024,
          "title": "EE683 Clinical Evolution and Medical Resource Utilization in Adults With Respiratory Syncytial Virus Infection at a Community Hospital in Argentina",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Public Health and Environmental Issues"
          ]
        },
        {
          "openalex_id": "W4405749949",
          "year": 2024,
          "title": "OP8 What Do HTA Agencies Across the Globe Need for Generating Health-Related Quality of Life Evidence? Findings From a Global Survey",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4390126294",
          "year": 2023,
          "title": "EE380 Budget-Impact Analysis of Encorafenib with Binimetinib for Unresectable or Metastatic Melanoma in BRAFV600-Mutated Patients in an Argentinian Social Security Payer Setting",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "CAR-T cell therapy research",
            "Biosimilars and Bioanalytical Methods",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3188180436",
          "year": 2012,
          "title": "Quirófano con flujo laminar para prevenir infecciones en artroplastías de cadera y rodilla",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Orthopedic Infections and Treatments",
            "Orthopaedic implants and arthroplasty",
            "Total Knee Arthroplasty Outcomes"
          ]
        },
        {
          "openalex_id": "W2023955832",
          "year": 2013,
          "title": "Calibration of a Cost-Effectiveness Model to Evaluate the Incorporation of a Quadrivalent HPV Types 6, 11, 16, 18 Vaccine in Argentina: Disease Burden Component",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Vaccine Coverage and Hesitancy",
            "Livestock Management and Performance Improvement"
          ]
        },
        {
          "openalex_id": "W2171587828",
          "year": 2013,
          "title": "Cost-Effectiveness of Telaprevir in Genotype 1 Chronic Hepatitis C Virus (HCV) Infection in Argentina",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis C virus research",
            "Pharmaceutical Economics and Policy",
            "HIV/AIDS drug development and treatment"
          ]
        },
        {
          "openalex_id": "W4251546597",
          "year": 2013,
          "title": "Cost-Effectiveness of Telaprevir in Genotype 1 Chronic Hepatitis C Virus (HCV) Infection in Colombia",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis C virus research",
            "Pharmaceutical Economics and Policy",
            "Pneumocystis jirovecii pneumonia detection and treatment"
          ]
        },
        {
          "openalex_id": "W1910947906",
          "year": 2019,
          "title": "Sequential inactivated (IPV) and live oral (OPV) poliovirus vaccines for preventing poliomyelitis",
          "type": "article",
          "venue": "Cochrane Database of Systematic Reviews",
          "cited_by_count": 35,
          "topics": [
            "Viral Infections and Immunology Research",
            "SARS-CoV-2 and COVID-19 Research",
            "Viral gastroenteritis research and epidemiology"
          ]
        },
        {
          "openalex_id": "W2740066531",
          "year": 2017,
          "title": "[Strategy to improve access to etiological treatment of Chagas disease at the first level of care in Argentina].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 11,
          "topics": [
            "Trypanosoma species research and implications",
            "Parasites and Host Interactions",
            "Research on Leishmaniasis Studies"
          ]
        },
        {
          "openalex_id": "W2612751175",
          "year": 2017,
          "title": "Estrategia para mejorar el acceso al tratamiento etiológico para la enfermedad de Chagas en el primer nivel de atención en Argentina",
          "type": "article",
          "venue": "DOAJ (DOAJ: Directory of Open Access Journals)",
          "cited_by_count": 7,
          "topics": [
            "Trypanosoma species research and implications"
          ]
        },
        {
          "openalex_id": "W4253145815",
          "year": 2014,
          "title": "Sequential inactivated (IPV) and live oral (OPV) poliovirus vaccines for preventing poliomyelitis",
          "type": "article",
          "venue": "Cochrane Database of Systematic Reviews",
          "cited_by_count": 5,
          "topics": [
            "Viral Infections and Immunology Research",
            "Viral gastroenteritis research and epidemiology",
            "Respiratory viral infections research"
          ]
        },
        {
          "openalex_id": "W2626949144",
          "year": 2017,
          "title": "[Health-worker barriers to syphilis screening in pregnant women in Bolivia's Los Andes network].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 3,
          "topics": [
            "Syphilis Diagnosis and Treatment",
            "HIV/AIDS oral health manifestations",
            "Maternal and Neonatal Healthcare"
          ]
        },
        {
          "openalex_id": "W2612627711",
          "year": 2017,
          "title": "Barreras del personal de salud para el tamizaje de sífilis en mujeres embarazadas de la Red Los Andes, Bolivia",
          "type": "article",
          "venue": "DOAJ (DOAJ: Directory of Open Access Journals)",
          "cited_by_count": 1,
          "topics": [
            "Syphilis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4250086957",
          "year": 2014,
          "title": "Combined therapy with statins and fibrates for people with dyslipidaemia",
          "type": "reference-entry",
          "venue": "Cochrane Database of Systematic Reviews",
          "cited_by_count": 1,
          "topics": [
            "Lipoproteins and Cardiovascular Health",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "HIV-related health complications and treatments"
          ]
        },
        {
          "openalex_id": "W2007012482",
          "year": 2013,
          "title": "Self-Reported Health Status and EQ-5D-3L Values of the Argentine Population: Comparing 2005 Versus 2009 National Risk Factor Surveys",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Public Health Policies and Epidemiology",
            "Global Health Care Issues"
          ]
        }
      ]
    }
  },
  {
    "name": "Lucky Ngwira",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1734-TVG",
        "title": "‘Decolonizing health’: Perception and development of a conceptual health framework among children and adolescents in sub-Saharan Africa and its content comparison with the EQ-5D-Y",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1943-EO",
        "title": "’Decolonizing health’: Perception and development of a conceptual health framework among children and adolescents in sub-Saharan Africa and its content comparison with the EQ-5D-Y",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20200030",
        "title": "travel scholarship Lucky Ngwira",
        "working_group": "Others"
      },
      {
        "project_id": "2025-RA",
        "title": "Adaptation and Psychometric Validation of the Chichewa (Malawi) EuroQol Toddler and Infant Populations (EQ-TIPS) Measure of Health Related Quality of Life",
        "working_group": "Youth"
      },
      {
        "project_id": "2252-EO",
        "title": "Cross-cultural adaptation of the EQ-TIPS into Chichewa (Malawi): preliminary findings",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5063482306",
      "display_name": "Lucky G. Ngwira",
      "orcid": "0000-0002-2695-8917",
      "reported_affiliation": "Kamuzu Central Hospital",
      "works_count": 41,
      "top_topics": [
        {
          "topic": "Pneumocystis jirovecii pneumonia detection and treatment",
          "works": 15
        },
        {
          "topic": "Tuberculosis Research and Epidemiology",
          "works": 11
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 11
        },
        {
          "topic": "Pneumonia and Respiratory Infections",
          "works": 9
        },
        {
          "topic": "SARS-CoV-2 and COVID-19 Research",
          "works": 6
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 5
        },
        {
          "topic": "SARS-CoV-2 detection and testing",
          "works": 5
        },
        {
          "topic": "Respiratory viral infections research",
          "works": 5
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 4
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 3
        },
        {
          "topic": "COVID-19 epidemiological studies",
          "works": 2
        },
        {
          "topic": "Diagnosis and treatment of tuberculosis",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Elizabeth L. Corbett",
          "works": 14
        },
        {
          "name": "Andrea M. Rehman",
          "works": 14
        },
        {
          "name": "Victoria Simms",
          "works": 14
        },
        {
          "name": "Rashida A. Ferrand",
          "works": 14
        },
        {
          "name": "Grace McHugh",
          "works": 13
        },
        {
          "name": "Tsitsi Bandason",
          "works": 8
        },
        {
          "name": "Mark P. Nicol",
          "works": 8
        },
        {
          "name": "Richard E. Chaisson",
          "works": 7
        },
        {
          "name": "David W. Dowdy",
          "works": 7
        },
        {
          "name": "Regina E. Abotsi",
          "works": 7
        },
        {
          "name": "Felix S. Dube",
          "works": 7
        },
        {
          "name": "McEwen Khundi",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7163050445",
          "year": 2026,
          "title": "Mapping health-related quality of life measurement tools in Africa: a scoping review",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W7170168179",
          "year": 2026,
          "title": "Uncertainty in Economic Evaluation: A Pragmatic Guide for Health Technology Assessment (HTA) Agencies in Resource-Constrained Settings",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4417405339",
          "year": 2025,
          "title": "COVID-19 diagnosis within five days of symptoms onset among healthcare workers in Malawi; Non-randomized control trial of self-testing using Ag-RDTs",
          "type": "article",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 0,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W4409760382",
          "year": 2025,
          "title": "Cost-effectiveness of wastewater-based environmental surveillance for SARS-CoV-2 in Blantyre, Malawi and Kathmandu, Nepal: A model-based study",
          "type": "article",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 1,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "COVID-19 epidemiological studies",
            "SARS-CoV-2 and COVID-19 Research"
          ]
        },
        {
          "openalex_id": "W4414941215",
          "year": 2025,
          "title": "Provider costs of professional COVID-19 rapid antigen testing in low-income settings",
          "type": "article",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 0,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W4400053974",
          "year": 2024,
          "title": "Characterization of bacterial and viral pathogens in the respiratory tract of children with HIV-associated chronic lung disease: a case–control study",
          "type": "article",
          "venue": "BMC Infectious Diseases",
          "cited_by_count": 3,
          "topics": [
            "Pneumocystis jirovecii pneumonia detection and treatment",
            "Respiratory viral infections research",
            "Pneumonia and Respiratory Infections"
          ]
        },
        {
          "openalex_id": "W2169000358",
          "year": 2012,
          "title": "The Ethics of Testing a Test: Randomized Trials of the Health Impact of Diagnostic Tests for Infectious Diseases",
          "type": "article",
          "venue": "Clinical Infectious Diseases",
          "cited_by_count": 17,
          "topics": [
            "Ethics in Clinical Research",
            "Healthcare cost, quality, practices",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W644943277",
          "year": 2015,
          "title": "Screening for Tuberculosis Among Adults Newly Diagnosed With HIV in Sub-Saharan Africa",
          "type": "article",
          "venue": "JAIDS Journal of Acquired Immune Deficiency Syndromes",
          "cited_by_count": 21,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "Immune responses and vaccinations",
            "Malaria Research and Control"
          ]
        },
        {
          "openalex_id": "W2805527338",
          "year": 2018,
          "title": "Assessment of the quality of SOBO industrial wastewater and its impact on water quality in Nankhaka River",
          "type": "article",
          "venue": "Physics and Chemistry of the Earth Parts A/B/C",
          "cited_by_count": 8,
          "topics": [
            "Water Quality and Pollution Assessment",
            "Water Quality Monitoring Technologies"
          ]
        },
        {
          "openalex_id": "W2790229085",
          "year": 2018,
          "title": "Completion of isoniazid preventive therapy among human immunodeficiency virus positive adults in urban Malawi",
          "type": "article",
          "venue": "The International Journal of Tuberculosis and Lung Disease",
          "cited_by_count": 34,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "HIV/AIDS Research and Interventions",
            "HIV Research and Treatment"
          ]
        },
        {
          "openalex_id": "W4320856122",
          "year": 2023,
          "title": "A systematic review of economic evaluations of whole-genome sequencing for the surveillance of bacterial pathogens",
          "type": "review",
          "venue": "Microbial Genomics",
          "cited_by_count": 56,
          "topics": [
            "Salmonella and Campylobacter epidemiology",
            "Bacterial Identification and Susceptibility Testing",
            "Antibiotic Resistance in Bacteria"
          ]
        },
        {
          "openalex_id": "W4323316013",
          "year": 2023,
          "title": "COVID-19 vaccine inequity in African low-income countries",
          "type": "article",
          "venue": "Frontiers in Public Health",
          "cited_by_count": 50,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 epidemiological studies"
          ]
        },
        {
          "openalex_id": "W4281289476",
          "year": 2022,
          "title": "TB morbidity estimates overlook the contribution of post-TB disability: evidence from urban Malawi",
          "type": "article",
          "venue": "BMJ Global Health",
          "cited_by_count": 39,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "Diagnosis and treatment of tuberculosis",
            "Healthcare Facilities Design and Sustainability"
          ]
        },
        {
          "openalex_id": "W4312208037",
          "year": 2022,
          "title": "Cost of wastewater-based environmental surveillance for SARS-CoV-2: Evidence from pilot sites in Blantyre, Malawi and Kathmandu, Nepal",
          "type": "article",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 30,
          "topics": [
            "SARS-CoV-2 detection and testing",
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W2759439196",
          "year": 2018,
          "title": "Screening for Tuberculosis With Xpert MTB/RIF Assay Versus Fluorescent Microscopy Among Adults Newly Diagnosed With Human Immunodeficiency Virus in Rural Malawi: A Cluster Randomized Trial (Chepetsa)",
          "type": "article",
          "venue": "Clinical Infectious Diseases",
          "cited_by_count": 30,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "Immune responses and vaccinations",
            "Image Processing Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W2793576616",
          "year": 2018,
          "title": "Predictors of isoniazid preventive therapy completion among adults newly diagnosed with HIV in rural Malawi",
          "type": "article",
          "venue": "The International Journal of Tuberculosis and Lung Disease",
          "cited_by_count": 20,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "HIV/AIDS Research and Interventions",
            "Pneumocystis jirovecii pneumonia detection and treatment"
          ]
        }
      ]
    }
  },
  {
    "name": "Luis Rajmil",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2016490",
        "title": "Statistical analysis and preparation of a manuscript describing the responsiveness, and impact on outcomes of administering the EQ‐5D‐Y via internet to children/youths with Type I Diabetes Mellitus in clinical practice.",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5000326162",
      "display_name": "Luís Rajmil",
      "orcid": "0000-0002-6625-0649",
      "reported_affiliation": "Agencia de Salud Pública de Barcelona",
      "works_count": 210,
      "top_topics": [
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 56
        },
        {
          "topic": "Child and Adolescent Health",
          "works": 31
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 24
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 19
        },
        {
          "topic": "Child and Adolescent Psychosocial and Emotional Development",
          "works": 19
        },
        {
          "topic": "Health and Lifestyle Studies",
          "works": 18
        },
        {
          "topic": "Employment and Welfare Studies",
          "works": 16
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 15
        },
        {
          "topic": "Global Health Care Issues",
          "works": 14
        },
        {
          "topic": "Adolescent and Pediatric Healthcare",
          "works": 10
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 10
        },
        {
          "topic": "Aging, Health, and Disability",
          "works": 10
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jordi Alonso",
          "works": 46
        },
        {
          "name": "Michael Herdman",
          "works": 37
        },
        {
          "name": "Ulrike Ravens‐Sieberer",
          "works": 32
        },
        {
          "name": "Silvina Berra",
          "works": 31
        },
        {
          "name": "Montse Ferrer",
          "works": 27
        },
        {
          "name": "José M Valderas",
          "works": 19
        },
        {
          "name": "Vicky Serra‐Sutton",
          "works": 19
        },
        {
          "name": "Bárbara Starfield",
          "works": 18
        },
        {
          "name": "Michael Erhart",
          "works": 16
        },
        {
          "name": "Pascal Auquier",
          "works": 16
        },
        {
          "name": "Anders Hjern",
          "works": 12
        },
        {
          "name": "Esteve Fernández",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4417270026",
          "year": 2025,
          "title": "783 - MALADAPTIVE EATING BEHAVIORS AND HEALTH-RELATED QUALITY OF LIFE IN SPANISH CHILDREN",
          "type": "article",
          "venue": "Gaceta Sanitaria",
          "cited_by_count": 0,
          "topics": [
            "Health and Well-being Studies",
            "Child Nutrition and Feeding Issues",
            "Human Health and Disease"
          ]
        },
        {
          "openalex_id": "W4417291577",
          "year": 2025,
          "title": "Behavioural and Emotional Symptoms Did not Increase During the COVID‐19 Pandemic in Swedish Preschool Children",
          "type": "article",
          "venue": "Acta Paediatrica",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and Mental Health",
            "Child and Adolescent Psychosocial and Emotional Development",
            "Early Childhood Education and Development"
          ]
        },
        {
          "openalex_id": "W4403965068",
          "year": 2024,
          "title": "Impact of School Closures and other Lockdown Measures during the COVID-19 Pandemic: Effects on Social Inequalities in Child Health",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and Mental Health",
            "Early Childhood Education and Development",
            "Youth Substance Use and School Attendance"
          ]
        },
        {
          "openalex_id": "W4403144409",
          "year": 2024,
          "title": "Maladaptive eating behaviors and health-related quality of life in Spanish children",
          "type": "article",
          "venue": "Appetite",
          "cited_by_count": 1,
          "topics": [
            "Eating Disorders and Behaviors",
            "Obesity, Physical Activity, Diet",
            "Health and Lifestyle Studies"
          ]
        },
        {
          "openalex_id": "W4386945094",
          "year": 2023,
          "title": "Gender differences in trajectories of health-related quality of life from childhood to adolescence in a 7-year follow-up study in a urban socially disadvantaged sample from Argentina",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 7,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "COVID-19 and Mental Health",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        },
        {
          "openalex_id": "W4390169496",
          "year": 2023,
          "title": "Impact of lockdown and school closure on children during the COVID-19 pandemic",
          "type": "article",
          "venue": "Global Pediatrics",
          "cited_by_count": 1,
          "topics": [
            "COVID-19 and Mental Health",
            "COVID-19 and healthcare impacts"
          ]
        },
        {
          "openalex_id": "W4290690362",
          "year": 1981,
          "title": "[Harlequin fetus].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Psychoanalysis and Psychopathology Research",
            "Sympathectomy and Hyperhidrosis Treatments",
            "Assisted Reproductive Technology and Twin Pregnancy"
          ]
        },
        {
          "openalex_id": "W2623201024",
          "year": 1983,
          "title": "Ús de la PGE 1 als 36 dies de vida en un cas de cardiopatia congènita ductus-dependent",
          "type": "article",
          "venue": "Pediatria catalana: butlletí de la Societat Catalana de Pediatria",
          "cited_by_count": 0,
          "topics": [
            "Cardiovascular Conditions and Treatments",
            "Congenital Heart Disease Studies",
            "Tracheal and airway disorders"
          ]
        },
        {
          "openalex_id": "W2418713416",
          "year": 1991,
          "title": "[Prolonged erections after diagnostic injection of papaverine chlorhydrate].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Sexual function and dysfunction studies",
            "Hormonal and reproductive studies",
            "Genital Health and Disease"
          ]
        },
        {
          "openalex_id": "W2954569644",
          "year": 1993,
          "title": "Repetitividad del uso de las clasificaciones de las causas de defunción en el contexto de una encuesta de mortalidad perinatal",
          "type": "article",
          "venue": "Anales de Pediatría",
          "cited_by_count": 0,
          "topics": [
            "Autopsy Techniques and Outcomes",
            "Insurance, Mortality, Demography, Risk Management",
            "Maternal and Neonatal Healthcare"
          ]
        },
        {
          "openalex_id": "W2022995084",
          "year": 2005,
          "title": "El Cuestionario de Salud SF-36 español: una década de experiencia y nuevos desarrollos",
          "type": "article",
          "venue": "Gaceta Sanitaria",
          "cited_by_count": 841,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Nursing care and research",
            "Dialysis and Renal Disease Management"
          ]
        },
        {
          "openalex_id": "W1984556055",
          "year": 2005,
          "title": "KIDSCREEN-52 quality-of-life measure for children and adolescents",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 827,
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
          "cited_by_count": 807,
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
          "cited_by_count": 758,
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
          "cited_by_count": 732,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Child and Adolescent Psychosocial and Emotional Development",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W2111818224",
          "year": 2008,
          "title": "Health-Related Quality of Life Measurement in Children and Adolescents: A Systematic Review of Generic and Disease-Specific Instruments",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 670,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Adolescent and Pediatric Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1914452183",
          "year": 2005,
          "title": "Health measurement scales. A practical guide to their development and use, 3rd ed",
          "type": "article",
          "venue": "Europe PMC (PubMed Central)",
          "cited_by_count": 567,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Reliability and Agreement in Measurement",
            "Health and Wellbeing Research"
          ]
        },
        {
          "openalex_id": "W1969958843",
          "year": 2013,
          "title": "Pediatric Patient-Reported Outcome Instruments for Research to Support Medical Product Labeling: Report of the ISPOR PRO Good Research Practices for the Assessment of Children and Adolescents Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 486,
          "topics": [
            "Pharmaceutical studies and practices",
            "Childhood Cancer Survivors' Quality of Life",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        }
      ]
    }
  }
]
