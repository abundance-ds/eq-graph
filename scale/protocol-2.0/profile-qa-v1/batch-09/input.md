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
    "name": "Bram Roudijk",
    "member_affiliation": "EuroQol Research Foundation",
    "is_member": true,
    "projects": [
      {
        "project_id": "100-RA",
        "title": "Valuation of the EQ-5D-3L-Y in the Netherlands and an investigation on different proxy perspectives",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "169-RA",
        "title": "Value sets for EQ-5D-5L: A compendium, comparative review & user guide",
        "working_group": "Valuation"
      },
      {
        "project_id": "1694-RA",
        "title": "Better understanding of the transition between Y and adult instruments: taking both measurement and valuation differences into account",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1923-RA",
        "title": "Comparison of DCE duration and EQ-VT in EQ-5D-Y-5L in the Netherlands",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "20180340R1",
        "title": "Trickling down to explain the valuation of worse than dead states: towards more valid values.",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190780",
        "title": "Valuation of the EQ-5D-5L in the Kingdom of Saudi Arabia (KSA)",
        "working_group": "Valuation"
      },
      {
        "project_id": "2647-RA",
        "title": "Impact of EQ-5D-5L Arabic level 4 changes on preferences. Are corrections needed for value sets?",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5028508726",
      "display_name": "Bram Roudijk",
      "orcid": "0000-0001-5000-0875",
      "reported_affiliation": "Erasmus MC",
      "works_count": 58,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 51
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 37
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 12
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 7
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 5
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 4
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 4
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 4
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 3
        },
        {
          "topic": "Global Health Care Issues",
          "works": 3
        },
        {
          "topic": "Quality and Safety in Healthcare",
          "works": 2
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Peep F. M. Stalmeier",
          "works": 12
        },
        {
          "name": "Nancy Devlin",
          "works": 11
        },
        {
          "name": "Fredrick Dermawan Purba",
          "works": 10
        },
        {
          "name": "Elly Stolk",
          "works": 8
        },
        {
          "name": "Marcel F. Jonker",
          "works": 8
        },
        {
          "name": "Fanni Rencz",
          "works": 7
        },
        {
          "name": "Aureliano Paolo Finch",
          "works": 6
        },
        {
          "name": "Stefan A. Lipman",
          "works": 6
        },
        {
          "name": "Henry Bailey",
          "works": 6
        },
        {
          "name": "Richard Norman",
          "works": 6
        },
        {
          "name": "Eleanor Pullenayegum",
          "works": 5
        },
        {
          "name": "A. Kooli",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7162664709",
          "year": 2026,
          "title": "Exploring Perceived Interactions between EQ-5D-5L and Bolt-ons Using Composite Time-Tradeoff Valuations: A Qualitative Study",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W7122436979",
          "year": 2026,
          "title": "Revisiting health state preferences after 20 years: A new EQ-5D-3L value set for the Netherlands",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Public Health Policies and Education"
          ]
        },
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
        },
        {
          "openalex_id": "W7127301341",
          "year": 2026,
          "title": "Unconscious death thoughts: Do they play a role in time trade-off and visual analogue scale scores for health?",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Death Anxiety and Social Exclusion",
            "Grief, Bereavement, and Mental Health",
            "Palliative Care and End-of-Life Issues"
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
          "openalex_id": "W4408305971",
          "year": 2025,
          "title": "A Head-On Comparison of EQ-VT- and Crosswalk-Based EQ-5D-5L Value Sets",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2587013309",
          "year": 2017,
          "title": "Cultural values: can they explain self-reported health?",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 34,
          "topics": [
            "Cultural Differences and Values",
            "Health disparities and outcomes",
            "Social Representations and Identity"
          ]
        },
        {
          "openalex_id": "W2796512612",
          "year": 2018,
          "title": "Setting Dead at Zero: Applying Scale Properties to the QALY Model",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 26,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2996741948",
          "year": 2019,
          "title": "A Head-On Ordinal Comparison of the Composite Time Trade-Off and the Better-Than-Dead Method",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 5,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
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
          "openalex_id": "W3211171162",
          "year": 2021,
          "title": "An EQ-5D-5L value set for Italy using videoconferencing interviews and feasibility of a new mode of administration",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 91,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4301142577",
          "year": 2022,
          "title": "Value Sets for EQ-5D-5L",
          "type": "book",
          "venue": "",
          "cited_by_count": 86,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Manufacturing Process and Optimization",
            "Product Development and Customization"
          ]
        },
        {
          "openalex_id": "W4304080516",
          "year": 2022,
          "title": "A Value Set for the EQ-5D-Y-3L in the Netherlands",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W3217092198",
          "year": 2021,
          "title": "Developing the EQ-5D-5L Value Set for Uganda Using the ‘Lite’ Protocol",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W4228998400",
          "year": 2022,
          "title": "The Sensitivity and Specificity of Repeated and Dominant Choice Tasks in Discrete Choice Experiments",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 36,
          "topics": [
            "Economic and Environmental Valuation",
            "Agriculture Sustainability and Environmental Impact",
            "Sensory Analysis and Statistical Methods"
          ]
        },
        {
          "openalex_id": "W4206834014",
          "year": 2021,
          "title": "The EQ-5D-5L Valuation Study in Egypt",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 34,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Quality and Supply Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Brendan Mulhern",
    "member_affiliation": "University of Technology Sydney",
    "is_member": true,
    "projects": [
      {
        "project_id": "1903-RA",
        "title": "Testing the development of a Dimension Specific Module using cognition – Extending the Deep Dive pilot study",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1926-RA",
        "title": "Developing a EuroQol guidance for testing psychometric evidence for generic preference based instruments",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1976-TVG",
        "title": "Brendan Mulhern - Study visit to Canada (hosted by Simon Fraser University, and the University of British Columbia)",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2014010",
        "title": "Valuing EQ-5D-5L health states using EQ-VT: Does the Life A health description and/or the ordering of dimensions matter?",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015460",
        "title": "The Relative Value of Social Outcomes in Health Technology Assessment",
        "working_group": "Others"
      },
      {
        "project_id": "2016260",
        "title": "Comparing DCE designs that can be used to value EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016650",
        "title": "A qualitative approach to understanding what aspects of health are important to people Ð Australian extension",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20170670",
        "title": "Extending the QALY project – testing the face and content validity of candidate items within the Australian context",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "20180300",
        "title": "Development and psychometric testing of EQ-5D-5L bolt-on descriptors for vision and cognition: A study in the UK and Australia",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20180460",
        "title": "Psychometric assessment of the eQALY item pool in Australia",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "234-VS",
        "title": "Valuing Health-Related Quality of Life: Developing an EQ-5D-5L Value Set for Ghana",
        "working_group": "Valuation"
      },
      {
        "project_id": "322-RA",
        "title": "Investigating the development of a multi layered “Deep Dive” measure of health-related quality of life based on the EQ-5D: A pilot study",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "99-RA",
        "title": "How much do the EQ-5D-5L and bolt-on dimensions contribute to the overall measurement of quality of life? A psychometric investigation",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5090013218",
      "display_name": "Brendan Mulhern",
      "orcid": "0000-0003-3656-8063",
      "reported_affiliation": "University of Technology Sydney",
      "works_count": 294,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 188
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 77
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 18
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 17
        },
        {
          "topic": "Global Health Care Issues",
          "works": 15
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 15
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 13
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 12
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 11
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 10
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 9
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 8
        }
      ],
      "frequent_coauthors": [
        {
          "name": "John Brazier",
          "works": 97
        },
        {
          "name": "Donna Rowen",
          "works": 79
        },
        {
          "name": "Nancy Devlin",
          "works": 69
        },
        {
          "name": "Aki Tsuchiya",
          "works": 48
        },
        {
          "name": "Rosalie Viney",
          "works": 46
        },
        {
          "name": "Louise Longworth",
          "works": 45
        },
        {
          "name": "Richard Norman",
          "works": 41
        },
        {
          "name": "Clara Mukuria",
          "works": 37
        },
        {
          "name": "Nick Bansback",
          "works": 31
        },
        {
          "name": "Tracey Young",
          "works": 23
        },
        {
          "name": "Lidia Engel",
          "works": 23
        },
        {
          "name": "Arne Risa Hole",
          "works": 22
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7165174612",
          "year": 2026,
          "title": "<i>What Matters 2 Kids:</i> a mixed-methods protocol for developing a culturally-responsive illustrated well-being measure for Aboriginal and Torres Strait Islander children",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Indigenous Health, Education, and Rights",
            "Participatory Visual Research Methods",
            "Child Abuse and Trauma"
          ]
        },
        {
          "openalex_id": "W7140273325",
          "year": 2026,
          "title": "A qualitative study of cancer clinical trial network consumers’ acceptability of the modular approach to patient-reported outcome measurement: how much of it is “common sense”?",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Cancer survivorship and care",
            "Economic and Financial Impacts of Cancer",
            "Mental Health and Patient Involvement"
          ]
        },
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
          "openalex_id": "W7147077407",
          "year": 2026,
          "title": "Carers’ interpretation of the recall period and perspective-taking when completing the EQ health and wellbeing instrument (EQ-HWB)-9 as proxies for people with dementia: a think-aloud study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Mental Health and Patient Involvement",
            "Geriatric Care and Nursing Homes"
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
          "openalex_id": "W4417022934",
          "year": 2025,
          "title": "A cross-country comparison of the psychometric performance of SF-6Dv2 and EQ-5D-5L",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W5590851",
          "year": 1980,
          "title": "Foetal warfarin syndrome.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 7,
          "topics": [
            "Cardiovascular Issues in Pregnancy"
          ]
        },
        {
          "openalex_id": "W2414665093",
          "year": 1982,
          "title": "A double blind placebo controlled study on the use of ketotifen in childhood asthma.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 5,
          "topics": [
            "Asthma and respiratory diseases",
            "Adrenal Hormones and Disorders",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W1969211327",
          "year": 1984,
          "title": "Failure of cord serum cholesterol and betalipoprotein as screening tests for familial hyperlipoproteinaemia",
          "type": "article",
          "venue": "Irish Journal of Medical Science (1971 -)",
          "cited_by_count": 4,
          "topics": [
            "Lipoproteins and Cardiovascular Health",
            "Lipid metabolism and disorders",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W2419607965",
          "year": 1988,
          "title": "Rehabilitation--easing the transition from hospital to home.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Telemedicine and Telehealth Implementation",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W2343426002",
          "year": 2017,
          "title": "Valuing health-related quality of life: An EQ-5D-5L value set for England",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 1416,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Delphi Technique in Research"
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
          "openalex_id": "W2070375179",
          "year": 2008,
          "title": "The effectiveness of web-based interventions designed to decrease alcohol consumption — A systematic review",
          "type": "review",
          "venue": "Preventive Medicine",
          "cited_by_count": 235,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Digital Mental Health Interventions",
            "Health Policy Implementation Science"
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
          "openalex_id": "W2049658617",
          "year": 2008,
          "title": "The feasibility and effectiveness of a web-based personalised feedback and social norms alcohol intervention in UK university students: A randomised control trial",
          "type": "article",
          "venue": "Addictive Behaviors",
          "cited_by_count": 161,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Alcohol Consumption and Health Effects",
            "Neurotransmitter Receptor Influence on Behavior"
          ]
        }
      ]
    }
  },
  {
    "name": "Brigitte Essers",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2016740",
        "title": "A Dutch tariff for the Euroqol-5D-Youth",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5056962219",
      "display_name": "Brigitte A.B. Essers",
      "orcid": "0000-0002-7703-7114",
      "reported_affiliation": "Maastricht University Medical Centre",
      "works_count": 112,
      "top_topics": [
        {
          "topic": "Nonmelanoma Skin Cancer Studies",
          "works": 33
        },
        {
          "topic": "Cutaneous Melanoma Detection and Management",
          "works": 14
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 14
        },
        {
          "topic": "Reconstructive Facial Surgery Techniques",
          "works": 11
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 10
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 9
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 8
        },
        {
          "topic": "Gastrointestinal motility and disorders",
          "works": 7
        },
        {
          "topic": "Cardiac Arrest and Resuscitation",
          "works": 6
        },
        {
          "topic": "Mechanical Circulatory Support Devices",
          "works": 5
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 5
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Klara Mosterd",
          "works": 23
        },
        {
          "name": "Nicole W.J. Kelleners-Smeets",
          "works": 18
        },
        {
          "name": "Carmen D. Dirksen",
          "works": 14
        },
        {
          "name": "Patty J. Nelemans",
          "works": 13
        },
        {
          "name": "Björn Winkens",
          "works": 12
        },
        {
          "name": "Jos G. Maessen",
          "works": 11
        },
        {
          "name": "Martje M. Suverein",
          "works": 10
        },
        {
          "name": "Roberto Lorusso",
          "works": 10
        },
        {
          "name": "Martin H. Prins",
          "works": 10
        },
        {
          "name": "Erik Scholten",
          "works": 9
        },
        {
          "name": "Marcel C.G. van de Poll",
          "works": 9
        },
        {
          "name": "A.H.M.M. Arits",
          "works": 9
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7125184376",
          "year": 2026,
          "title": "Attitudes of patients and family members towards deferred and waived consent in ECPR research, an ancillary study of the INCEPTION trial",
          "type": "article",
          "venue": "Resuscitation Plus",
          "cited_by_count": 0,
          "topics": [
            "Ethics in Clinical Research",
            "Patient-Provider Communication in Healthcare",
            "Healthcare Decision-Making and Restraints"
          ]
        },
        {
          "openalex_id": "W7164960474",
          "year": 2026,
          "title": "Measuring health-related quality of life and well-being in adults with fecal incontinence: a comparative psychometric evaluation",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Pelvic floor disorders treatments",
            "Pressure Ulcer Prevention and Management",
            "Gastrointestinal motility and disorders"
          ]
        },
        {
          "openalex_id": "W4411982669",
          "year": 2025,
          "title": "254: CONTROLLING FAECAL INCONTINENCE WITH A NOVEL ANAL DEVICE (CONFIDENCE): A MULTICENTER RANDOMIZED CONTROLLED TRIAL",
          "type": "article",
          "venue": "Gastroenterology",
          "cited_by_count": 0,
          "topics": [
            "Anorectal Disease Treatments and Outcomes",
            "Pelvic floor disorders treatments",
            "Diverticular Disease and Complications"
          ]
        },
        {
          "openalex_id": "W4415549737",
          "year": 2025,
          "title": "Attitudes of patients and family members towards deferred and waived consent in ECPR research, a post-hoc analysis of the INCEPTION trial",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Patient Dignity and Privacy",
            "Healthcare Decision-Making and Restraints"
          ]
        },
        {
          "openalex_id": "W4414121469",
          "year": 2025,
          "title": "Cost-Effectiveness of Photodynamic Therapy and 5-Fluorouracil Cream versus Surgical Excision in Treatment of Bowen’s Disease: A Trial-Based Economic Evaluation",
          "type": "article",
          "venue": "Dermatology",
          "cited_by_count": 1,
          "topics": [
            "Nonmelanoma Skin Cancer Studies",
            "Photodynamic Therapy Research Studies",
            "Cutaneous Melanoma Detection and Management"
          ]
        },
        {
          "openalex_id": "W4417067378",
          "year": 2025,
          "title": "Psychological Factors: The Defining Features of Quality of Life in Disorders of Gut-Brain Interaction: A Comparative Exploratory Analysis",
          "type": "article",
          "venue": "Clinical Gastroenterology and Hepatology",
          "cited_by_count": 0,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Gastroesophageal reflux and treatments",
            "Celiac Disease Research and Management"
          ]
        },
        {
          "openalex_id": "W2155930895",
          "year": 2004,
          "title": "Surgical excision vs Mohs' micrographic surgery for basal-cell carcinoma of the face: randomised controlled trial",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 369,
          "topics": [
            "Nonmelanoma Skin Cancer Studies",
            "Reconstructive Facial Surgery Techniques",
            "Head and Neck Surgical Oncology"
          ]
        },
        {
          "openalex_id": "W2015009700",
          "year": 2005,
          "title": "Determinants of satisfaction with the health state of the facial skin in patients undergoing surgery for facial basal cell carcinoma",
          "type": "article",
          "venue": "Patient Education and Counseling",
          "cited_by_count": 20,
          "topics": [
            "Nonmelanoma Skin Cancer Studies",
            "Reconstructive Facial Surgery Techniques",
            "Facial Rejuvenation and Surgery Techniques"
          ]
        },
        {
          "openalex_id": "W2912808391",
          "year": 2006,
          "title": "Basal Cell Carcinoma Questionnaire",
          "type": "dataset",
          "venue": "PsycTESTS Dataset",
          "cited_by_count": 0,
          "topics": [
            "Nonmelanoma Skin Cancer Studies",
            "Cancer and Skin Lesions",
            "Polyomavirus and related diseases"
          ]
        },
        {
          "openalex_id": "W2097067989",
          "year": 2006,
          "title": "Cost-effectiveness of Mohs Micrographic Surgery vs Surgical Excision for Basal Cell Carcinoma of the Face",
          "type": "article",
          "venue": "Archives of Dermatology",
          "cited_by_count": 131,
          "topics": [
            "Nonmelanoma Skin Cancer Studies",
            "Reconstructive Facial Surgery Techniques",
            "Cutaneous Melanoma Detection and Management"
          ]
        },
        {
          "openalex_id": "W4318016874",
          "year": 2023,
          "title": "Early Extracorporeal CPR for Refractory Out-of-Hospital Cardiac Arrest",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 539,
          "topics": [
            "Mechanical Circulatory Support Devices",
            "Cardiac Arrest and Resuscitation",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W2589882013",
          "year": 2017,
          "title": "Prophylactic hydration to protect renal function from intravascular iodinated contrast material in patients at high risk of contrast-induced nephropathy (AMACING): a prospective, randomised, phase 3, controlled, open-label, non-inferiority trial",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 479,
          "topics": [
            "Acute Kidney Injury Research",
            "Chronic Kidney Disease and Diabetes",
            "Ultrasound and Hyperthermia Applications"
          ]
        },
        {
          "openalex_id": "W2131131624",
          "year": 2008,
          "title": "Surgical excision versus Mohs' micrographic surgery for primary and recurrent basal-cell carcinoma of the face: a prospective randomised controlled trial with 5-years' follow-up",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 462,
          "topics": [
            "Nonmelanoma Skin Cancer Studies",
            "Reconstructive Facial Surgery Techniques",
            "Cancer and Skin Lesions"
          ]
        },
        {
          "openalex_id": "W2122888213",
          "year": 2013,
          "title": "Photodynamic therapy versus topical imiquimod versus topical fluorouracil for treatment of superficial basal-cell carcinoma: a single blind, non-inferiority, randomised controlled trial",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 311,
          "topics": [
            "Nonmelanoma Skin Cancer Studies",
            "Photodynamic Therapy Research Studies",
            "Reconstructive Facial Surgery Techniques"
          ]
        },
        {
          "openalex_id": "W2921125836",
          "year": 2019,
          "title": "Randomized Trial of Four Treatment Approaches for Actinic Keratosis",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 245,
          "topics": [
            "Nonmelanoma Skin Cancer Studies",
            "Cutaneous Melanoma Detection and Management",
            "Reconstructive Facial Surgery Techniques"
          ]
        },
        {
          "openalex_id": "W2921522488",
          "year": 2019,
          "title": "Early or Delayed Cardioversion in Recent-Onset Atrial Fibrillation",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 205,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Cardiac electrophysiology and arrhythmias",
            "Cardiac Arrhythmias and Treatments"
          ]
        },
        {
          "openalex_id": "W2767005502",
          "year": 2017,
          "title": "Five-Year Results of a Randomized Controlled Trial Comparing Effectiveness of Photodynamic Therapy, Topical Imiquimod, and Topical 5-Fluorouracil in Patients with Superficial Basal Cell Carcinoma",
          "type": "article",
          "venue": "Journal of Investigative Dermatology",
          "cited_by_count": 150,
          "topics": [
            "Nonmelanoma Skin Cancer Studies",
            "Cancer and Skin Lesions",
            "Cutaneous lymphoproliferative disorders research"
          ]
        }
      ]
    }
  },
  {
    "name": "Caitlyn Solem",
    "member_affiliation": "GSK",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5090387330",
      "display_name": "Caitlyn T. Solem",
      "orcid": "",
      "reported_affiliation": "GlaxoSmithKline (United States)",
      "works_count": 121,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 18
        },
        {
          "topic": "Antimicrobial Resistance in Staphylococcus",
          "works": 16
        },
        {
          "topic": "Lung Cancer Treatments and Mutations",
          "works": 13
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 12
        },
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 9
        },
        {
          "topic": "Lung Cancer Diagnosis and Treatment",
          "works": 9
        },
        {
          "topic": "CAR-T cell therapy research",
          "works": 8
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 8
        },
        {
          "topic": "Respiratory and Cough-Related Research",
          "works": 7
        },
        {
          "topic": "Lymphoma Diagnosis and Treatment",
          "works": 6
        },
        {
          "topic": "Cystic Fibrosis Research Advances",
          "works": 6
        },
        {
          "topic": "Pancreatic and Hepatic Oncology Research",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Cynthia Macahilig",
          "works": 30
        },
        {
          "name": "Jennifer Stephens",
          "works": 24
        },
        {
          "name": "Marc Botteman",
          "works": 19
        },
        {
          "name": "Shelby Corman",
          "works": 10
        },
        {
          "name": "Sajjad Haider",
          "works": 9
        },
        {
          "name": "Shawn X. Sun",
          "works": 9
        },
        {
          "name": "Seema Haider",
          "works": 9
        },
        {
          "name": "Claudie Charbonneau",
          "works": 8
        },
        {
          "name": "Xin Gao",
          "works": 8
        },
        {
          "name": "Richard Chambers",
          "works": 8
        },
        {
          "name": "Vijay R. Nadipelli",
          "works": 8
        },
        {
          "name": "Yin Wan",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W2279127602",
          "year": 2025,
          "title": "Challenges and consequences of medication exposure definitions in comparative effectiveness research.",
          "type": "dissertation",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W4413804058",
          "year": 2025,
          "title": "Patient and Physician Preferences for Maintenance Treatment in Advanced Non-Small Cell Lung Cancer: Insights into Treatment Selection",
          "type": "article",
          "venue": "Advances in Therapy",
          "cited_by_count": 0,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Lung Cancer Treatments and Mutations",
            "Lung Cancer Research Studies"
          ]
        },
        {
          "openalex_id": "W4409457141",
          "year": 2025,
          "title": "Real-World Maintenance Treatment Patterns Among Patients with Advanced Non-Small Cell Lung Cancer",
          "type": "article",
          "venue": "Advances in Therapy",
          "cited_by_count": 1,
          "topics": [
            "Lung Cancer Treatments and Mutations",
            "Cancer Immunotherapy and Biomarkers",
            "Lung Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4406870067",
          "year": 2025,
          "title": "Real-world treatment patterns, healthcare resource utilization (HCRU), and costs in newly diagnosed patients with rectal cancer (RC) in the United States (US).",
          "type": "conference-abstract",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Colorectal Cancer Screening and Detection"
          ]
        },
        {
          "openalex_id": "W4414893551",
          "year": 2025,
          "title": "Real-world treatment patterns, healthcare resource utilization (HCRU), and costs in newly diagnosed patients with rectal cancer (RC) in the United States (US).",
          "type": "conference-abstract",
          "venue": "JCO Oncology Practice",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Colorectal Cancer Screening and Detection"
          ]
        },
        {
          "openalex_id": "W4411369722",
          "year": 2025,
          "title": "Treatments and Outcomes After Platinum-Based Chemotherapy and Anti–PD-(L)1 in NSCLC",
          "type": "article",
          "venue": "JAMA Network Open",
          "cited_by_count": 5,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Lung Cancer Treatments and Mutations",
            "Lung Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2006188285",
          "year": 2011,
          "title": "A brief assessment tool for body image in systemic lupus erythematosus",
          "type": "article",
          "venue": "Body Image",
          "cited_by_count": 24,
          "topics": [
            "Systemic Lupus Erythematosus Research",
            "Systemic Sclerosis and Related Diseases",
            "Fibromyalgia and Chronic Fatigue Syndrome Research"
          ]
        },
        {
          "openalex_id": "W2144743167",
          "year": 2011,
          "title": "Assessing the impact of age, race, ethnicity and inhibitor status on functional limitations of patients with severe and moderately severe haemophilia A",
          "type": "article",
          "venue": "Haemophilia",
          "cited_by_count": 37,
          "topics": [
            "Hemophilia Treatment and Research",
            "Blood Coagulation and Thrombosis Mechanisms"
          ]
        },
        {
          "openalex_id": "W2273652410",
          "year": 2011,
          "title": "Incidence of events common with corticosteroid use among individuals with noninfectious uveitis",
          "type": "article",
          "venue": "European Journal of Ophthalmology",
          "cited_by_count": 0,
          "topics": [
            "Ocular Diseases and Behçet’s Syndrome",
            "Systemic Lupus Erythematosus Research",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W2025907550",
          "year": 2011,
          "title": "PRM39 Identification of Diseases for EQ-5D Bolt-on Item Development: An Empirical Approach",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Design Education and Practice",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1841279730",
          "year": 2015,
          "title": "Pathophysiology and burden of infection in patients with diabetes mellitus and peripheral vascular disease: focus on skin and soft-tissue infections",
          "type": "article",
          "venue": "Clinical Microbiology and Infection",
          "cited_by_count": 192,
          "topics": [
            "Diabetic Foot Ulcer Assessment and Management",
            "Infective Endocarditis Diagnosis and Management",
            "Peripheral Artery Disease Management"
          ]
        },
        {
          "openalex_id": "W4285492548",
          "year": 2022,
          "title": "Patient-reported outcomes in ZUMA-7, a phase 3 study of axicabtagene ciloleucel in second-line large B-cell lymphoma",
          "type": "article",
          "venue": "Blood",
          "cited_by_count": 76,
          "topics": [
            "CAR-T cell therapy research",
            "Lymphoma Diagnosis and Treatment",
            "Integrated Circuits and Semiconductor Failure Analysis"
          ]
        },
        {
          "openalex_id": "W1830468797",
          "year": 2015,
          "title": "Implementing criteria-based early switch/early discharge programmes: a European perspective",
          "type": "article",
          "venue": "Clinical Microbiology and Infection",
          "cited_by_count": 69,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pneumonia and Respiratory Infections",
            "Nosocomial Infections in ICU"
          ]
        },
        {
          "openalex_id": "W2336531854",
          "year": 2016,
          "title": "Impact of pulmonary exacerbations and lung function on generic health-related quality of life in patients with cystic fibrosis",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 67,
          "topics": [
            "Cystic Fibrosis Research Advances",
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Interstitial Lung Diseases and Idiopathic Pulmonary Fibrosis"
          ]
        },
        {
          "openalex_id": "W2008099224",
          "year": 2012,
          "title": "Effect of Acute Bleeding on Daily Quality of Life Assessments in Patients with Congenital Hemophilia with Inhibitors and Their Families: Observations from the Dosing Observational Study in Hemophilia",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 63,
          "topics": [
            "Hemophilia Treatment and Research",
            "Blood transfusion and management",
            "Platelet Disorders and Treatments"
          ]
        },
        {
          "openalex_id": "W2067470530",
          "year": 2013,
          "title": "Exacerbation-related impairment of quality of life and work productivity in severe and very severe chronic obstructive pulmonary disease",
          "type": "article",
          "venue": "International Journal of COPD",
          "cited_by_count": 61,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Respiratory and Cough-Related Research",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W1967215347",
          "year": 2014,
          "title": "Antibiotic treatment patterns across Europe in patients with complicated skin and soft-tissue infections due to meticillin-resistant Staphylococcus aureus: A plea for implementation of early switch and early discharge criteria",
          "type": "article",
          "venue": "International Journal of Antimicrobial Agents",
          "cited_by_count": 60,
          "topics": [
            "Antimicrobial Resistance in Staphylococcus",
            "Antibiotics Pharmacokinetics and Efficacy",
            "Bacterial Identification and Susceptibility Testing"
          ]
        },
        {
          "openalex_id": "W2982849442",
          "year": 2019,
          "title": "Effects of monthly buprenorphine extended-release injections on patient-centered outcomes: A long-term study",
          "type": "article",
          "venue": "Journal of Substance Abuse Treatment",
          "cited_by_count": 57,
          "topics": [
            "Opioid Use Disorder Treatment",
            "HIV, Drug Use, Sexual Risk",
            "Substance Abuse Treatment and Outcomes"
          ]
        }
      ]
    }
  },
  {
    "name": "Camilla Falivena",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "354-RA",
        "title": "Content and face validity of the EQ-HWB and EQ-HWB-S in a sample of patients, members of the general public and social care users in Italy",
        "working_group": "Descriptive Systems, EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5014952669",
      "display_name": "Camilla Falivena",
      "orcid": "0000-0003-3259-095X",
      "reported_affiliation": "Libera Università Maria SS. Assunta",
      "works_count": 21,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Corporate Social Responsibility Reporting",
          "works": 5
        },
        {
          "topic": "Environmental Sustainability in Business",
          "works": 4
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 3
        },
        {
          "topic": "Public Policy and Administration Research",
          "works": 3
        },
        {
          "topic": "Corporate Finance and Governance",
          "works": 2
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 2
        },
        {
          "topic": "Accounting and Organizational Management",
          "works": 2
        },
        {
          "topic": "Public-Private Partnership Projects",
          "works": 2
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 2
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 2
        },
        {
          "topic": "Auditing, Earnings Management, Governance",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sandro Brunelli",
          "works": 10
        },
        {
          "name": "Gabriele Palozzi",
          "works": 4
        },
        {
          "name": "Constance Stegbauer",
          "works": 3
        },
        {
          "name": "Ariadna Moreno",
          "works": 3
        },
        {
          "name": "Anna Hentschel",
          "works": 3
        },
        {
          "name": "Magda Rosenmöller",
          "works": 3
        },
        {
          "name": "Tim Heise",
          "works": 3
        },
        {
          "name": "Joachim Szécsényi",
          "works": 3
        },
        {
          "name": "Freimut Schliess",
          "works": 3
        },
        {
          "name": "Francesco Venuti",
          "works": 2
        },
        {
          "name": "Berit Adam",
          "works": 2
        },
        {
          "name": "Jens Heiling",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7136338790",
          "year": 2026,
          "title": "Local government and political turbulences: evidence from municipality commissionership in Italy",
          "type": "article",
          "venue": "Meditari Accountancy Research",
          "cited_by_count": 0,
          "topics": [
            "Public Policy and Administration Research",
            "Fiscal Policies and Political Economy",
            "Local Government Finance and Decentralization"
          ]
        },
        {
          "openalex_id": "W4411287937",
          "year": 2025,
          "title": "Public Sector Accountability Challenges in Emerging Climate Governance: Seeking Consequentiality Through a Theoretical Common Ground",
          "type": "article",
          "venue": "Business Strategy and the Environment",
          "cited_by_count": 1,
          "topics": [
            "Corporate Social Responsibility Reporting",
            "Public Policy and Administration Research",
            "Sustainability and Climate Change Governance"
          ]
        },
        {
          "openalex_id": "W4409833014",
          "year": 2025,
          "title": "The coverage of public sector financial management in MPA and MPM programs: evidence from Europe",
          "type": "article",
          "venue": "International Journal of Public Sector Management",
          "cited_by_count": 1,
          "topics": [
            "Public-Private Partnership Projects"
          ]
        },
        {
          "openalex_id": "W4394764853",
          "year": 2024,
          "title": "Content validity of the EQ-HWB and EQ-HWB-S in a sample of Italian patients, informal caregivers and members of the general public",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 16,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, psychology, and well-being",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W4400101850",
          "year": 2024,
          "title": "ESG and impact litigation: identifying and governing the causes through strategic accountability patterns",
          "type": "article",
          "venue": "Management Decision",
          "cited_by_count": 11,
          "topics": [
            "Community Development and Social Impact",
            "Public-Private Partnership Projects",
            "Legal Education and Practice Innovations"
          ]
        },
        {
          "openalex_id": "W4317567006",
          "year": 2023,
          "title": "Cost-Utility Analysis of Esketamine for Patients with Treatment-Resistant Depression in Italy",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 11,
          "topics": [
            "Treatment of Major Depression",
            "Neurotransmitter Receptor Influence on Behavior",
            "Anesthesia and Sedative Agents"
          ]
        },
        {
          "openalex_id": "W2904635818",
          "year": 2016,
          "title": "PMSs and Health Policy Choices. The need for a Health Technology Assessment Framework",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2907842134",
          "year": 2018,
          "title": "Designing the Function of Health Technology Assessment as a Support for Hospital Management",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W2894737121",
          "year": 2018,
          "title": "Higher Sustainability and Lower Opportunistic Behaviour in Healthcare: A New Framework for Performing Hospital-Based Health Technology Assessment",
          "type": "article",
          "venue": "Sustainability",
          "cited_by_count": 20,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2972255427",
          "year": 2019,
          "title": "Corporate social responsibility and firm value: Do firm size and age matter? Empirical evidence from European listed companies",
          "type": "article",
          "venue": "Corporate Social Responsibility and Environmental Management",
          "cited_by_count": 334,
          "topics": [
            "Corporate Social Responsibility Reporting",
            "Corporate Finance and Governance",
            "Environmental Sustainability in Business"
          ]
        },
        {
          "openalex_id": "W3104754673",
          "year": 2020,
          "title": "Costs and its drivers for diabetes mellitus type 2 patients in France and Germany: a systematic review of economic studies",
          "type": "review",
          "venue": "BMC Health Services Research",
          "cited_by_count": 34,
          "topics": [
            "Diabetes Management and Research",
            "Diabetes Treatment and Management",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W3131477414",
          "year": 2021,
          "title": "Accountability for climate change: a research synthesis through the lenses of the integrated thinking approach",
          "type": "article",
          "venue": "Meditari Accountancy Research",
          "cited_by_count": 17,
          "topics": [
            "Corporate Social Responsibility Reporting",
            "Environmental Sustainability in Business",
            "Accounting and Organizational Management"
          ]
        },
        {
          "openalex_id": "W4309315304",
          "year": 2022,
          "title": "Environmental Auditing in Rural Areas: Current Patterns and Future Challenges in Central Asia",
          "type": "article",
          "venue": "Sustainability",
          "cited_by_count": 10,
          "topics": [
            "Regulation and Compliance Studies",
            "Environmental Sustainability in Business",
            "Corporate Social Responsibility Reporting"
          ]
        }
      ]
    }
  }
]
