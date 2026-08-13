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
    "name": "Barbara Spady",
    "member_affiliation": "University of Calgary",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5032609556",
      "display_name": "Barbara Conner‐Spady",
      "orcid": "0000-0001-5674-4795",
      "reported_affiliation": "University of Calgary",
      "works_count": 63,
      "top_topics": [
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 20
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 16
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 14
        },
        {
          "topic": "Healthcare Operations and Scheduling Optimization",
          "works": 13
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 9
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 9
        },
        {
          "topic": "Osteoarthritis Treatment and Mechanisms",
          "works": 9
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 9
        },
        {
          "topic": "Orthopaedic implants and arthroplasty",
          "works": 8
        },
        {
          "topic": "Bone and Joint Diseases",
          "works": 4
        },
        {
          "topic": "Healthcare Systems and Technology",
          "works": 4
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Tom Noseworthy",
          "works": 29
        },
        {
          "name": "Deborah A. Marshall",
          "works": 19
        },
        {
          "name": "Walter P. Maksymowych",
          "works": 18
        },
        {
          "name": "Éric Bohm",
          "works": 17
        },
        {
          "name": "Michael Dunbar",
          "works": 14
        },
        {
          "name": "John McGurran",
          "works": 13
        },
        {
          "name": "Gillian Hawker",
          "works": 11
        },
        {
          "name": "Claudia Sanmartin",
          "works": 11
        },
        {
          "name": "R. Lambert",
          "works": 9
        },
        {
          "name": "Lynda Loucks",
          "works": 8
        },
        {
          "name": "Anthony S. Russell",
          "works": 7
        },
        {
          "name": "Geoffrey Johnston",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4308767355",
          "year": 2022,
          "title": "Patient acceptable symptom state (PASS): thresholds for the EQ-5D-5L and Oxford hip and knee scores for patients with total hip and knee replacement",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 17,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Total Knee Arthroplasty Outcomes",
            "Patient Safety and Medication Errors"
          ]
        },
        {
          "openalex_id": "W3121556767",
          "year": 2021,
          "title": "Relationship Between <scp>Patient‐Reported</scp> Readiness for Total Knee Arthroplasty and Likelihood of a Good Outcome at One‐Year <scp>Follow‐Up</scp>",
          "type": "article",
          "venue": "Arthritis Care & Research",
          "cited_by_count": 15,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Osteoarthritis Treatment and Mechanisms",
            "Orthopaedic implants and arthroplasty"
          ]
        },
        {
          "openalex_id": "W3153843187",
          "year": 2021,
          "title": "Reply",
          "type": "letter",
          "venue": "Arthritis & Rheumatology",
          "cited_by_count": 0,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies",
            "Systemic Lupus Erythematosus Research",
            "Autoimmune and Inflammatory Disorders Research"
          ]
        },
        {
          "openalex_id": "W3083468782",
          "year": 2020,
          "title": "Patients’ Preoperative Expectations of Total Knee Arthroplasty and Satisfaction With Outcomes at One Year: A Prospective Cohort Study",
          "type": "article",
          "venue": "Arthritis & Rheumatology",
          "cited_by_count": 59,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Osteoarthritis Treatment and Mechanisms",
            "Orthopaedic implants and arthroplasty"
          ]
        },
        {
          "openalex_id": "W2988350570",
          "year": 2019,
          "title": "Patient expectations and satisfaction 6 and 12 months following total hip and knee replacement",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 109,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Orthopaedic implants and arthroplasty",
            "Hip and Femur Fractures"
          ]
        },
        {
          "openalex_id": "W2792766369",
          "year": 2018,
          "title": "Comparing the validity and responsiveness of the EQ-5D-5L to the Oxford hip and knee scores and SF-12 in osteoarthritis patients 1 year following total joint replacement",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 81,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Total Knee Arthroplasty Outcomes",
            "Osteoarthritis Treatment and Mechanisms"
          ]
        },
        {
          "openalex_id": "W2780466179",
          "year": 2001,
          "title": "Health-related quality of life as a predictor of future physician visits and hospitalization",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 0,
          "topics": [
            "Healthcare professionals’ stress and burnout"
          ]
        },
        {
          "openalex_id": "W2052111658",
          "year": 2001,
          "title": "Lack of Congruence in the Ratings of Patients' Health Status by Patients and Their Physicians",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 147,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical Reasoning and Diagnostic Skills"
          ]
        },
        {
          "openalex_id": "W4235426257",
          "year": 2001,
          "title": "Lack of Congruence in the Ratings of Patients' Health Status by Patients and Their Physicians",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 135,
          "topics": [
            "Health and Wellbeing Research"
          ]
        },
        {
          "openalex_id": "W2780201340",
          "year": 2001,
          "title": "Longitudinal changes in health-related quality of life of people with diabetes compared to those without chronic conditions",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 4,
          "topics": [
            "Health and Wellbeing Research",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2079392881",
          "year": 2005,
          "title": "Spondyloarthritis research Consortium of Canada magnetic resonance imaging index for assessment of sacroiliac joint inflammation in ankylosing spondylitis",
          "type": "article",
          "venue": "Arthritis Care & Research",
          "cited_by_count": 537,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Spine and Intervertebral Disc Pathology",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W2119067278",
          "year": 2008,
          "title": "Development and validation of the Spondyloarthritis Research Consortium of Canada (SPARCC) Enthesitis Index",
          "type": "article",
          "venue": "Annals of the Rheumatic Diseases",
          "cited_by_count": 285,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Autoimmune and Inflammatory Disorders Research"
          ]
        },
        {
          "openalex_id": "W4255613904",
          "year": 2005,
          "title": "Spondyloarthritis research consortium of canada magnetic resonance imaging index for assessment of spinal inflammation in ankylosing spondylitis",
          "type": "article",
          "venue": "Arthritis & Rheumatism",
          "cited_by_count": 238,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W2123235923",
          "year": 2012,
          "title": "Suppression of inflammation and effects on new bone formation in ankylosing spondylitis: evidence for a window of opportunity in disease modification",
          "type": "article",
          "venue": "Annals of the Rheumatic Diseases",
          "cited_by_count": 237,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Infectious Diseases and Tuberculosis"
          ]
        },
        {
          "openalex_id": "W2048805333",
          "year": 2011,
          "title": "Focal fat lesions at vertebral corners on magnetic resonance imaging predict the development of new syndesmophytes in ankylosing spondylitis",
          "type": "article",
          "venue": "Arthritis & Rheumatism",
          "cited_by_count": 199,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Infectious Diseases and Tuberculosis",
            "Bone and Joint Diseases"
          ]
        },
        {
          "openalex_id": "W2010040768",
          "year": 2015,
          "title": "Reliability and validity of the EQ-5D-5L compared to the EQ-5D-3L in patients with osteoarthritis referred for hip and knee replacement",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 192,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Total Knee Arthroplasty Outcomes",
            "Osteoarthritis Treatment and Mechanisms"
          ]
        },
        {
          "openalex_id": "W1965690582",
          "year": 2007,
          "title": "Serum matrix metalloproteinase 3 is an independent predictor of structural damage progression in patients with ankylosing spondylitis",
          "type": "article",
          "venue": "Arthritis & Rheumatism",
          "cited_by_count": 164,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W2054036955",
          "year": 2007,
          "title": "Steroid injection for osteoarthritis of the hip: A randomized, double‐blind, placebo‐controlled trial",
          "type": "article",
          "venue": "Arthritis & Rheumatism",
          "cited_by_count": 157,
          "topics": [
            "Osteoarthritis Treatment and Mechanisms",
            "Bone and Joint Diseases",
            "Spine and Intervertebral Disc Pathology"
          ]
        }
      ]
    }
  },
  {
    "name": "Bas Janssen",
    "member_affiliation": "",
    "is_member": true,
    "projects": [
      {
        "project_id": "155-RA",
        "title": "Performance of the EQ-5D in the European aging population – A study on measurement properties, population norms, health inequalities and determinants of health in a large representative sample of European adults aged 55+ using the SHARE-data",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "157-RA",
        "title": "Towards a patient-reported summary score for EQ-5D - revision (20190210)",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2012040",
        "title": "Bolt-on proposal",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2015450",
        "title": "A head-to-head comparison of nine country-specific EQ-5D-3L and EQ-5D-5L value sets in eight patient groups and a student cohort",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2016620",
        "title": "A head-to-head comparison of eight country-specific EQ-5D-3L and EQ-5D-5L value sets in eight patient groups and a student cohort - Why discriminatory power varies with versions, value sets and subgroups?",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20170600",
        "title": "Comparatively investigating sensitivity to change of the EQ-5D-3L and the EQ-5D-5L descriptive systems and seven country-specific value sets using different methodological approaches",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "240-RA",
        "title": "Revisiting the descriptor ‘discomfort’ and comparing measurement properties of the EQ-5D-5L to PROMIS measures",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2594-RA",
        "title": "Comparing the representativeness of population health surveys in Norway: a comparison of random probability sampling and online panel quota sampling (EQ-DAPHNIE)",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "458-RA",
        "title": "Testing the psychometric properties of 9 bolt-ons for the EQ-5D",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "461-RA",
        "title": "As if there were (no) tomorrow: the association between time perspective profile and self-reported health on the EQ-5D",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5020933378",
      "display_name": "Mathieu F. Janssen",
      "orcid": "0000-0001-6602-6949",
      "reported_affiliation": "Erasmus MC",
      "works_count": 116,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 77
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 11
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 8
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 8
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 7
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 6
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 6
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 6
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 6
        },
        {
          "topic": "Myasthenia Gravis and Thymoma",
          "works": 6
        },
        {
          "topic": "Traumatic Brain Injury Research",
          "works": 6
        },
        {
          "topic": "Long-Term Effects of COVID-19",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Gouke J. Bonsel",
          "works": 32
        },
        {
          "name": "Juanita A. Haagsma",
          "works": 19
        },
        {
          "name": "Fanni Rencz",
          "works": 16
        },
        {
          "name": "Brendan Mulhern",
          "works": 13
        },
        {
          "name": "Erica I. Lubetkin",
          "works": 12
        },
        {
          "name": "Sarah Dewilde",
          "works": 12
        },
        {
          "name": "A. Simon Pickard",
          "works": 11
        },
        {
          "name": "Henry Bailey",
          "works": 11
        },
        {
          "name": "Dominik Golicki",
          "works": 8
        },
        {
          "name": "Suzanne Polinder",
          "works": 8
        },
        {
          "name": "Glenn Phillips",
          "works": 8
        },
        {
          "name": "Althea La Foucade",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166433823",
          "year": 2026,
          "title": "Comparative performance of EQ-5D-5L bolt-ons in China and the Netherlands: results from the EQ-DAPHNIE project",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Ophthalmology and Visual Impairment Studies",
            "Psychometric Methodologies and Testing"
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
          "openalex_id": "W4411119891",
          "year": 2025,
          "title": "Development and Use of Cognition Bolt-Ons for the EQ-5D-3L and EQ-5D-5L: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Traumatic Brain Injury Research"
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
          "openalex_id": "W4413045171",
          "year": 2025,
          "title": "Health-related quality of life and QALY loss under COVID-19 lockdown: The case of Spain",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and Mental Health",
            "COVID-19 and healthcare impacts",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W2403348271",
          "year": 1991,
          "title": "Lower Xanthine Oxidoreductase Activity in Isolated Perfused Hearts if Xanthine Replaces Hypoxanthine as Substrate",
          "type": "book-chapter",
          "venue": "Advances in experimental medicine and biology",
          "cited_by_count": 1,
          "topics": [
            "Gout, Hyperuricemia, Uric Acid",
            "Metabolism and Genetic Disorders",
            "Biochemical and Molecular Research"
          ]
        },
        {
          "openalex_id": "W2049038631",
          "year": 1991,
          "title": "Relationship between glutathione status and xanthine oxidoreductase activity",
          "type": "article",
          "venue": "Journal of Molecular and Cellular Cardiology",
          "cited_by_count": 0,
          "topics": [
            "Gout, Hyperuricemia, Uric Acid"
          ]
        },
        {
          "openalex_id": "W2223339715",
          "year": 1991,
          "title": "Uridine and Purine Nucleoside Phosphorylase Activity in Human and Rat Heart",
          "type": "book-chapter",
          "venue": "Advances in experimental medicine and biology",
          "cited_by_count": 2,
          "topics": [
            "Biochemical and Molecular Research",
            "HIV/AIDS drug development and treatment",
            "Metabolism and Genetic Disorders"
          ]
        },
        {
          "openalex_id": "W1981692114",
          "year": 1993,
          "title": "Antioxidant defences in rat, pig, guinea pig, and human hearts: comparison with xanthine oxidoreductase activity",
          "type": "article",
          "venue": "Cardiovascular Research",
          "cited_by_count": 45,
          "topics": [
            "Gout, Hyperuricemia, Uric Acid",
            "Kidney Stones and Urolithiasis Treatments",
            "Thyroid Disorders and Treatments"
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
          "openalex_id": "W3111512677",
          "year": 2020,
          "title": "Psychometric properties of the EQ-5D-5L: a systematic review of the literature",
          "type": "review",
          "venue": "Quality of Life Research",
          "cited_by_count": 940,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W2788315630",
          "year": 2018,
          "title": "Is EQ-5D-5L Better Than EQ-5D-3L? A Head-to-Head Comparison of Descriptive Systems and Value Sets from Seven Countries",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 400,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2794316606",
          "year": 2018,
          "title": "A Systematic Review of Studies Comparing the Measurement Properties of the Three-Level and Five-Level Versions of the EQ-5D",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 375,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2791479921",
          "year": 2018,
          "title": "Population norms for the EQ-5D-3L: a cross-country analysis of population surveys for 20 countries",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 346,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2071701167",
          "year": 2007,
          "title": "Comparing the Standard EQ-5D Three-Level System with a Five-Level Version",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 282,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Reliability and Agreement in Measurement",
            "Psychometric Methodologies and Testing"
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
        }
      ]
    }
  },
  {
    "name": "Beata Koń",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "91-RA",
        "title": "EQ-5D-5L in productivity assessment according to the type of occupation",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5070682056",
      "display_name": "Beata Koń",
      "orcid": "0000-0003-2190-4546",
      "reported_affiliation": "National Health Insurance Fund",
      "works_count": 34,
      "top_topics": [
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 6
        },
        {
          "topic": "Viral Infections and Immunology Research",
          "works": 4
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 4
        },
        {
          "topic": "Diabetes and associated disorders",
          "works": 3
        },
        {
          "topic": "Blood Pressure and Hypertension Studies",
          "works": 3
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 3
        },
        {
          "topic": "Lung Cancer Diagnosis and Treatment",
          "works": 3
        },
        {
          "topic": "Radiomics and Machine Learning in Medical Imaging",
          "works": 3
        },
        {
          "topic": "Viral gastroenteritis research and epidemiology",
          "works": 2
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 2
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 2
        },
        {
          "topic": "Acute Myocardial Infarction Research",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Marcin Kruk",
          "works": 7
        },
        {
          "name": "Filip Urbański",
          "works": 7
        },
        {
          "name": "Barbara Więckowska",
          "works": 7
        },
        {
          "name": "Michał Jakubczyk",
          "works": 6
        },
        {
          "name": "Milena Kozioł",
          "works": 5
        },
        {
          "name": "Krzysztof Ozierański",
          "works": 4
        },
        {
          "name": "Agata Tymińska",
          "works": 4
        },
        {
          "name": "Marcin Grabowski",
          "works": 4
        },
        {
          "name": "Piotr Dobrowolski",
          "works": 4
        },
        {
          "name": "Aleksander Prejbisz",
          "works": 4
        },
        {
          "name": "Maciej Miłkowski",
          "works": 4
        },
        {
          "name": "Artur Myśliwiec",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7140309852",
          "year": 2026,
          "title": "Low-dose Computed Tomography Lung Cancer Screening Participants Show Improved 10-year Survival Compared With Matched Controls: A Case–Control Study",
          "type": "article",
          "venue": "Archivos de Bronconeumología",
          "cited_by_count": 0,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Radiomics and Machine Learning in Medical Imaging",
            "Effects of Radiation Exposure"
          ]
        },
        {
          "openalex_id": "W4414824084",
          "year": 2025,
          "title": "475PHigher risk of fractures in myasthenia gravis patients in comparison with general population – national healthcare database study",
          "type": "article",
          "venue": "Neuromuscular Disorders",
          "cited_by_count": 0,
          "topics": [
            "Myasthenia Gravis and Thymoma"
          ]
        },
        {
          "openalex_id": "W4413048043",
          "year": 2025,
          "title": "Diagnostic trends in patients hospitalized with suspected myocarditis: 10-year data from the nationwide MYO-PL database",
          "type": "article",
          "venue": "Cardiology Journal",
          "cited_by_count": 0,
          "topics": [
            "Viral Infections and Immunology Research",
            "Cardiac Imaging and Diagnostics",
            "Acute Myocardial Infarction Research"
          ]
        },
        {
          "openalex_id": "W4415656848",
          "year": 2025,
          "title": "Endoscopic Retrograde Cholangiopancreatography and Post Endoscopy Cholecystectomies in Pediatric Population—Longitudinal, Nationwide Data from Poland",
          "type": "article",
          "venue": "Journal of Clinical Medicine",
          "cited_by_count": 1,
          "topics": [
            "Gallbladder and Bile Duct Disorders",
            "Pediatric Hepatobiliary Diseases and Treatments",
            "Medical Device Sterilization and Disinfection"
          ]
        },
        {
          "openalex_id": "W7127957187",
          "year": 2025,
          "title": "Long-term survival of heFH or ACS patients on PCSK9 targeted therapy based on the real-life data from poland",
          "type": "article",
          "venue": "European Heart Journal",
          "cited_by_count": 0,
          "topics": [
            "Lipoproteins and Cardiovascular Health",
            "Pharmacovigilance and Adverse Drug Reactions",
            "Cholesterol and Lipid Metabolism"
          ]
        },
        {
          "openalex_id": "W4414491192",
          "year": 2025,
          "title": "Patterns of prescription of antihypertensive medications in Poland: a one-year assessment of initiation and persistence of therapy in a nationwide population cohort",
          "type": "article",
          "venue": "Journal of Hypertension",
          "cited_by_count": 1,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Medication Adherence and Compliance",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W2351619003",
          "year": 2016,
          "title": "The impact of firms' expectations & adjustments on the productivity cost of illness",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Workplace Health and Well-being"
          ]
        },
        {
          "openalex_id": "W7138304053",
          "year": 2016,
          "title": "The impact of firms' expectations &amp; adjustments on the productivity cost of illness",
          "type": "report",
          "venue": "",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W2583573735",
          "year": 2017,
          "title": "The impact of firms’ adjustments on the indirect cost of illness",
          "type": "article",
          "venue": "International Journal of Health Economics and Management",
          "cited_by_count": 2,
          "topics": [
            "Healthcare Policy and Management",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Workplace Health and Well-being"
          ]
        },
        {
          "openalex_id": "W2910405527",
          "year": 2018,
          "title": "Accessibility to personal insulin pumps among children with diabetes mellitus in Poland in 2014",
          "type": "article",
          "venue": "Clinical Diabetology",
          "cited_by_count": 1,
          "topics": [
            "Diabetes Management and Research",
            "Diabetes and associated disorders"
          ]
        },
        {
          "openalex_id": "W3206129070",
          "year": 2021,
          "title": "Occurrence, Trends, Management and Outcomes of Patients Hospitalized with Clinically Suspected Myocarditis—Ten-Year Perspectives from the MYO-PL Nationwide Database",
          "type": "article",
          "venue": "Journal of Clinical Medicine",
          "cited_by_count": 22,
          "topics": [
            "Viral Infections and Immunology Research",
            "Viral gastroenteritis research and epidemiology",
            "Cardiomyopathy and Myosin Studies"
          ]
        },
        {
          "openalex_id": "W3217281904",
          "year": 2021,
          "title": "Sex Differences in Incidence, Clinical Characteristics and Outcomes in Children and Young Adults Hospitalized for Clinically Suspected Myocarditis in the Last Ten Years—Data from the MYO-PL Nationwide Database",
          "type": "article",
          "venue": "Journal of Clinical Medicine",
          "cited_by_count": 19,
          "topics": [
            "Viral Infections and Immunology Research",
            "Viral gastroenteritis research and epidemiology",
            "Cardiovascular Effects of Exercise"
          ]
        },
        {
          "openalex_id": "W3094318041",
          "year": 2020,
          "title": "10 year Trends in Hospitalization Rates Due to Heart Failure and Related in-Hospital Mortality in Poland (2010–2019)",
          "type": "article",
          "venue": "ESC Heart Failure",
          "cited_by_count": 11,
          "topics": [
            "Heart Failure Treatment and Management",
            "Acute Myocardial Infarction Research",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2972064473",
          "year": 2019,
          "title": "Is the literature on the WTP-WTA disparity biased?",
          "type": "article",
          "venue": "Journal of Behavioral and Experimental Economics",
          "cited_by_count": 8,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Customer Service Quality and Loyalty"
          ]
        },
        {
          "openalex_id": "W4378078333",
          "year": 2023,
          "title": "Real World Evidence on the Effectiveness of Nusinersen within the National Program to Treat Spinal Muscular Atrophy in Poland",
          "type": "article",
          "venue": "Healthcare",
          "cited_by_count": 8,
          "topics": [
            "Neurogenetic and Muscular Disorders Research",
            "Muscle Physiology and Disorders",
            "Amyotrophic Lateral Sclerosis Research"
          ]
        },
        {
          "openalex_id": "W4210664535",
          "year": 2022,
          "title": "Sex differences in incidence, management, and outcomes in adult patients aged over 20 years with clinically diagnosed myocarditis in the last ten years: data from the MYO-PL nationwide database",
          "type": "article",
          "venue": "Polskie Archiwum Medycyny Wewnętrznej",
          "cited_by_count": 8,
          "topics": [
            "Viral Infections and Immunology Research",
            "Eosinophilic Disorders and Syndromes",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W2973217582",
          "year": 2019,
          "title": "Organisational units providing psychiatric services for adults – an analysis based on National Health Fund data for 2010–2016",
          "type": "article",
          "venue": "Psychiatria Polska",
          "cited_by_count": 7,
          "topics": [
            "Psychiatric care and mental health services",
            "Mental Health Treatment and Access",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2890538040",
          "year": 2018,
          "title": "An analysis of psychiatric services provided to adults in 2010–2014 based on the National Health Fund data",
          "type": "article",
          "venue": "Psychiatria Polska",
          "cited_by_count": 6,
          "topics": [
            "Mental Health Treatment and Access",
            "Schizophrenia research and treatment",
            "Family Caregiving in Mental Illness"
          ]
        }
      ]
    }
  },
  {
    "name": "Begashaw Melaku Gebresillassie",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1591-RA",
        "title": "A Systematic Scoping Review to Sythesise Evidence on Health-Related Quality of Life Measures in Africa",
        "working_group": "Populations and Health Systems, Education and Outreach"
      },
      {
        "project_id": "436-RA",
        "title": "Comparison of the psychometric properties of self-complete and proxy version of the EQ-5D-Y-3L in Ethiopian children with prevalent acute illnesses",
        "working_group": "Descriptive Systems, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5013305477",
      "display_name": "Begashaw Melaku Gebresillassie",
      "orcid": "0000-0003-0071-732X",
      "reported_affiliation": "Hunter Medical Research Institute",
      "works_count": 58,
      "top_topics": [
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 14
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 13
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 8
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 7
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 5
        },
        {
          "topic": "Complementary and Alternative Medicine Studies",
          "works": 5
        },
        {
          "topic": "Pregnancy and Medication Impact",
          "works": 5
        },
        {
          "topic": "Ethnobotanical and Medicinal Plants Studies",
          "works": 4
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 4
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 4
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 4
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Daniel Erku",
          "works": 23
        },
        {
          "name": "Abebe Basazn Mekuria",
          "works": 16
        },
        {
          "name": "Sewunet Admasu Belachew",
          "works": 15
        },
        {
          "name": "Asnakew Achaw Ayele",
          "works": 14
        },
        {
          "name": "Yonas Getaye Tefera",
          "works": 12
        },
        {
          "name": "Tadesse Melaku Abegaz",
          "works": 8
        },
        {
          "name": "Eyob Alemayehu Gebreyohannes",
          "works": 8
        },
        {
          "name": "Amanual Getnet Mersha",
          "works": 7
        },
        {
          "name": "Tamrat Befekadu Abebe",
          "works": 7
        },
        {
          "name": "Eshetie Melese Birru",
          "works": 6
        },
        {
          "name": "Henok Getachew Tegegn",
          "works": 6
        },
        {
          "name": "Yohannes Kelifa Emiru",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7165427543",
          "year": 2026,
          "title": "Leveraging linked healthcare data to facilitate early identification of end‑of‑life and support proactive palliative care decisions",
          "type": "dissertation",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Chronic Disease Management Strategies",
            "Insurance, Mortality, Demography, Risk Management",
            "Machine Learning in Healthcare"
          ]
        },
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
          "openalex_id": "W7125402310",
          "year": 2026,
          "title": "Predicting end-of-life in older women with heart failure: development and internal validation of clinically actionable prognostic models using routinely collected national data",
          "type": "article",
          "venue": "BMC Geriatrics",
          "cited_by_count": 0,
          "topics": [
            "Heart Failure Treatment and Management",
            "Chronic Disease Management Strategies",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W7167019382",
          "year": 2026,
          "title": "Subcutaneous Levetiracetam Use in Adult Palliative Care in Australia: A Cross-Sectional Survey",
          "type": "article",
          "venue": "Journal of Palliative Medicine",
          "cited_by_count": 0,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Patient Safety and Medication Errors",
            "Pain Management and Opioid Use"
          ]
        },
        {
          "openalex_id": "W4407613619",
          "year": 2025,
          "title": "Development and Validation of a Risk Prediction Model to Identify Women With Chronic Obstructive Pulmonary Disease for Proactive Palliative Care",
          "type": "article",
          "venue": "Respirology",
          "cited_by_count": 3,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Delphi Technique in Research",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4409266697",
          "year": 2025,
          "title": "Development, validation, and clinical utility of a risk prediction model to identify older women with dementia for proactive palliative care",
          "type": "article",
          "venue": "Archives of Gerontology and Geriatrics",
          "cited_by_count": 0,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Dementia and Cognitive Impairment Research",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W2461984944",
          "year": 2016,
          "title": "Evaluation of cotrimoxazole use as a preventive therapy among patients living with HIV/AIDS in Gondar University Referral Hospital, northwestern Ethiopia: a retrospective cross-sectional study",
          "type": "article",
          "venue": "HIV/AIDS - Research and Palliative Care",
          "cited_by_count": 10,
          "topics": [
            "Pneumocystis jirovecii pneumonia detection and treatment",
            "HIV/AIDS Research and Interventions",
            "Syphilis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2528987193",
          "year": 2016,
          "title": "Expectation and satisfaction of HIV/AIDS patients toward the pharmaceutical care provided at Gondar University Referral Hospital, Northwestern Ethiopia: a cross-sectional study",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 37,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Medication Adherence and Compliance",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W2467502157",
          "year": 2016,
          "title": "Extent of dispensing prescription-only medications without a prescription in community drug retail outlets in Addis Ababa, Ethiopia: a simulated-patient study",
          "type": "article",
          "venue": "Drug Healthcare and Patient Safety",
          "cited_by_count": 73,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pharmaceutical Quality and Counterfeiting",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2522410648",
          "year": 2016,
          "title": "Knowledge and Self-Reported Practice of Insulin Injection Device Disposal among Diabetes Patients in Gondar Town, Ethiopia: A Cross-Sectional Study",
          "type": "article",
          "venue": "Journal of Diabetes Research",
          "cited_by_count": 39,
          "topics": [
            "Antibiotic Use and Resistance",
            "Diabetes Management and Research",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W3005957464",
          "year": 2020,
          "title": "Global, regional, and national burden of chronic kidney disease, 1990–2017: a systematic analysis for the Global Burden of Disease Study 2017",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 6694,
          "topics": [
            "Chronic Kidney Disease and Diabetes",
            "Gout, Hyperuricemia, Uric Acid",
            "Acute Kidney Injury Research"
          ]
        },
        {
          "openalex_id": "W3093350281",
          "year": 2020,
          "title": "Five insights from the Global Burden of Disease Study 2019",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 690,
          "topics": [
            "Healthcare cost, quality, practices",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2980624194",
          "year": 2020,
          "title": "The global, regional, and national burden of oesophageal cancer and its attributable risk factors in 195 countries and territories, 1990–2017: a systematic analysis for the Global Burden of Disease Study 2017",
          "type": "article",
          "venue": "The Lancet. Gastroenterology & hepatology",
          "cited_by_count": 652,
          "topics": [
            "Esophageal Cancer Research and Treatment",
            "Esophageal and GI Pathology",
            "Head and Neck Cancer Studies"
          ]
        },
        {
          "openalex_id": "W2613139975",
          "year": 2017,
          "title": "Prevalence, Impact, and Management Practice of Dysmenorrhea among University of Gondar Students, Northwestern Ethiopia: A Cross-Sectional Study",
          "type": "article",
          "venue": "International Journal of Reproductive Medicine",
          "cited_by_count": 131,
          "topics": [
            "Menstrual Health and Disorders",
            "Child Nutrition and Water Access",
            "Therapeutic Uses of Natural Elements"
          ]
        },
        {
          "openalex_id": "W3014657877",
          "year": 2020,
          "title": "Diabetic health literacy and its association with glycemic control among adult patients with type 2 diabetes mellitus attending the outpatient clinic of a university hospital in Ethiopia",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 120,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Mobile Health and mHealth Applications",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2585881448",
          "year": 2017,
          "title": "Prevalence and associated factors of herbal medicine use among pregnant women on antenatal care follow-up at University of Gondar referral and teaching hospital, Ethiopia: a cross-sectional study",
          "type": "article",
          "venue": "BMC Complementary and Alternative Medicine",
          "cited_by_count": 106,
          "topics": [
            "Complementary and Alternative Medicine Studies",
            "Pregnancy and Medication Impact",
            "Ethnobotanical and Medicinal Plants Studies"
          ]
        },
        {
          "openalex_id": "W2797339351",
          "year": 2018,
          "title": "Health Related Quality of Life of Cancer Patients in Ethiopia",
          "type": "article",
          "venue": "Journal of Oncology",
          "cited_by_count": 62,
          "topics": [
            "Cancer survivorship and care",
            "Global Cancer Incidence and Screening",
            "Economic and Financial Impacts of Cancer"
          ]
        }
      ]
    }
  },
  {
    "name": "Ben Van Hout",
    "member_affiliation": "Open Health/University of Sheffield",
    "is_member": true,
    "projects": [
      {
        "project_id": "2014025",
        "title": "Supplementary funding 5L value set study England: Sheffield",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190940",
        "title": "Health state utility rescaling and interpersonal comparisons",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5032690231",
      "display_name": "Ben van Hout",
      "orcid": "0000-0001-9698-6094",
      "reported_affiliation": "The Open Group",
      "works_count": 120,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 56
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 21
        },
        {
          "topic": "Venous Thromboembolism Diagnosis and Management",
          "works": 15
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 12
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 11
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 10
        },
        {
          "topic": "Lipoproteins and Cardiovascular Health",
          "works": 10
        },
        {
          "topic": "Coronary Interventions and Diagnostics",
          "works": 9
        },
        {
          "topic": "Global Health Care Issues",
          "works": 6
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 5
        },
        {
          "topic": "Sepsis Diagnosis and Treatment",
          "works": 5
        },
        {
          "topic": "Schizophrenia research and treatment",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nancy Devlin",
          "works": 19
        },
        {
          "name": "Sonja Kroep",
          "works": 16
        },
        {
          "name": "Koonal Shah",
          "works": 14
        },
        {
          "name": "John Brazier",
          "works": 13
        },
        {
          "name": "Giancarlo Agnelli",
          "works": 13
        },
        {
          "name": "Ling‐Hsiang Chuang",
          "works": 13
        },
        {
          "name": "Peter Lindgren",
          "works": 11
        },
        {
          "name": "Rupert Bauersachs",
          "works": 11
        },
        {
          "name": "Brendan Mulhern",
          "works": 10
        },
        {
          "name": "Bart Heeg",
          "works": 10
        },
        {
          "name": "Guillermo Villa",
          "works": 9
        },
        {
          "name": "Elly Stolk",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4401435928",
          "year": 2024,
          "title": "691 - Understanding patient and physician preferences when choosing between biologic and oral systemic treatment options for moderate-to-severe atopic dermatitis: a discrete choice experiment",
          "type": "article",
          "venue": "British Journal of Dermatology",
          "cited_by_count": 0,
          "topics": [
            "Dermatology and Skin Diseases",
            "Allergic Rhinitis and Sensitization",
            "Health and Medical Studies"
          ]
        },
        {
          "openalex_id": "W4403800478",
          "year": 2024,
          "title": "Biologics and oral systemic treatment preferences in patients and physicians for moderate-to-severe atopic dermatitis: a discrete choice experiment in the United Kingdom and Germany",
          "type": "article",
          "venue": "Journal of Dermatological Treatment",
          "cited_by_count": 4,
          "topics": [
            "Dermatology and Skin Diseases",
            "Allergic Rhinitis and Sensitization",
            "Psoriasis: Treatment and Pathogenesis"
          ]
        },
        {
          "openalex_id": "W4391044434",
          "year": 2024,
          "title": "Exploring health preference heterogeneity in the UK: Using the online elicitation of personal utility functions approach to construct EQ‐5D‐5L value functions on societal, group and individual level",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4380150767",
          "year": 2023,
          "title": "CO77 Relationships between Heterotopic Ossification Volume and Functional and Quality of Life Endpoints in Fibrodysplasia Ossificans Progressiva (FOP)",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Heterotopic Ossification and Related Conditions",
            "Medical Imaging and Pathology Studies"
          ]
        },
        {
          "openalex_id": "W4380149239",
          "year": 2023,
          "title": "MSR58 Relating Heterotopic Ossification Volume to Joint Function And Quality of Life: A Simulation Study in Fibrodysplasia Ossificans Progressiva (FOP)",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Heterotopic Ossification and Related Conditions"
          ]
        },
        {
          "openalex_id": "W4390246256",
          "year": 2023,
          "title": "Using the Online Elicitation of Personal Utility Functions Approach to Derive a Patient-Based 5-Level Version of EQ-5D Value Set: A Study in 122 Patients With Rheumatic Diseases From Germany",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 5,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Multi-Criteria Decision Making"
          ]
        },
        {
          "openalex_id": "W1965327159",
          "year": 1993,
          "title": "Heart transplantation in the Netherlands; costs, effects and scenarios",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 60,
          "topics": [
            "Transplantation: Methods and Outcomes",
            "Renal Transplantation Outcomes and Treatments",
            "Viral Infections and Immunology Research"
          ]
        },
        {
          "openalex_id": "W2043741802",
          "year": 1996,
          "title": "Cost-effectiveness of fracture prevention: Time of intervention",
          "type": "conference-abstract",
          "venue": "Osteoporosis International",
          "cited_by_count": 0,
          "topics": [
            "Hip and Femur Fractures",
            "Bone health and osteoporosis research"
          ]
        },
        {
          "openalex_id": "W1779177804",
          "year": 1996,
          "title": "Osteoporosis in the Netherlands; A burden of illness study commissioned by Merck Sharp & Dohme",
          "type": "article",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "Bone health and osteoporosis research",
            "Hip and Femur Fractures",
            "Pelvic and Acetabular Injuries"
          ]
        },
        {
          "openalex_id": "W1965394645",
          "year": 1996,
          "title": "The cost of osteoporosis related fractures in the netherlands",
          "type": "conference-abstract",
          "venue": "Osteoporosis International",
          "cited_by_count": 0,
          "topics": [
            "Bone health and osteoporosis research",
            "Hip and Femur Fractures"
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
          "openalex_id": "W2163674015",
          "year": 2008,
          "title": "Transcatheter valve implantation for patients with aortic stenosis: a position statement from the European Association of Cardio-Thoracic Surgery (EACTS) and the European Society of Cardiology (ESC), in collaboration with the European Association of Percutaneous Cardiovascular Interventions (EAPCI)",
          "type": "article",
          "venue": "European Heart Journal",
          "cited_by_count": 721,
          "topics": [
            "Cardiac Valve Diseases and Treatments",
            "Aortic Disease and Treatment Approaches",
            "Cardiovascular Function and Risk Factors"
          ]
        },
        {
          "openalex_id": "W2145189434",
          "year": 1998,
          "title": "Randomised comparison of implantation of heparin-coated stents with balloon angioplasty in selected patients with coronary artery disease (Benestent II)",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 656,
          "topics": [
            "Coronary Interventions and Diagnostics",
            "Cardiac Imaging and Diagnostics",
            "Cerebrovascular and Carotid Artery Diseases"
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
          "openalex_id": "W2907128483",
          "year": 2019,
          "title": "Overview, Update, and Lessons Learned From the International EQ-5D-5L Valuation Work: Version 2 of the EQ-5D-5L Valuation Protocol",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 365,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2051686671",
          "year": 2001,
          "title": "Clinical and Economic Impact of Diabetes Mellitus on Percutaneous and Surgical Treatment of Multivessel Coronary Disease Patients",
          "type": "article",
          "venue": "Circulation",
          "cited_by_count": 340,
          "topics": [
            "Peripheral Artery Disease Management",
            "Coronary Interventions and Diagnostics",
            "Cardiac and Coronary Surgery Techniques"
          ]
        },
        {
          "openalex_id": "W2037785736",
          "year": 2008,
          "title": "Transcatheter valve implantation for patients with aortic stenosis: a position statement from the European Association of Cardio-Thoracic Surgery (EACTS) and the European Society of Cardiology (ESC), in collaboration with the European Association of Percutaneous Cardiovascular Interventions (EAPCI)",
          "type": "article",
          "venue": "European Journal of Cardio-Thoracic Surgery",
          "cited_by_count": 309,
          "topics": [
            "Cardiac Valve Diseases and Treatments",
            "Aortic Disease and Treatment Approaches",
            "Cardiovascular Function and Risk Factors"
          ]
        }
      ]
    }
  }
]
