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
    "name": "Jan Heijdra Suasnabar",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2265-EO",
        "title": "Travel grant for ISPOR Europe 2025 to give an oral presentation of work for SG-1792.",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2301-RA",
        "title": "Exploring the measurement strengths and gaps of the EQ-5D-5L in older populations",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5050459768",
      "display_name": "Jan M. Heijdra Suasnabar",
      "orcid": "0000-0002-8057-1318",
      "reported_affiliation": "Leiden University Medical Center",
      "works_count": 7,
      "top_topics": [
        {
          "topic": "Health disparities and outcomes",
          "works": 2
        },
        {
          "topic": "Substance Abuse Treatment and Outcomes",
          "works": 2
        },
        {
          "topic": "Cervical and Thoracic Myelopathy",
          "works": 2
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 2
        },
        {
          "topic": "Spinal Fractures and Fixation Techniques",
          "works": 2
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 1
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 1
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 1
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 1
        },
        {
          "topic": "Prenatal Substance Exposure Effects",
          "works": 1
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 1
        },
        {
          "topic": "Osteoarthritis Treatment and Mechanisms",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "M. Elske van den Akker‐van Marle",
          "works": 4
        },
        {
          "name": "Carmen Vleggeert‐Lankamp",
          "works": 2
        },
        {
          "name": "Aureliano Paolo Finch",
          "works": 1
        },
        {
          "name": "Brendan Mulhern",
          "works": 1
        },
        {
          "name": "Bethany Hipple Walters",
          "works": 1
        },
        {
          "name": "Caroline M.W. Goedmakers",
          "works": 1
        },
        {
          "name": "Floor de Vries",
          "works": 1
        },
        {
          "name": "Mark P. Arts",
          "works": 1
        },
        {
          "name": "Abhijit Nadkarni",
          "works": 1
        },
        {
          "name": "Benjamin Palafox",
          "works": 1
        },
        {
          "name": "Maaike G. J. Gademan",
          "works": 1
        },
        {
          "name": "Liza N. van Steenbergen",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4407852129",
          "year": 2025,
          "title": "Explanatory factors for the survival benefit among hip and knee arthroplasty patients with osteoarthritis",
          "type": "article",
          "venue": "Osteoarthritis and Cartilage Open",
          "cited_by_count": 0,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Osteoarthritis Treatment and Mechanisms",
            "Orthopaedic implants and arthroplasty"
          ]
        },
        {
          "openalex_id": "W4417500811",
          "year": 2025,
          "title": "Quality of Life and Societal Costs Related to Celiac Disease Before and After Diagnosis",
          "type": "article",
          "venue": "Clinical and Translational Gastroenterology",
          "cited_by_count": 0,
          "topics": [
            "Celiac Disease Research and Management",
            "Microscopic Colitis",
            "Gastrointestinal motility and disorders"
          ]
        },
        {
          "openalex_id": "W4392247404",
          "year": 2024,
          "title": "Exploring the measurement of health related quality of life and broader instruments: A dimensionality analysis",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 14,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4319869035",
          "year": 2023,
          "title": "Cost effectiveness of implanting a prosthesis after anterior cervical discectomy for radiculopathy: results of the NECK randomized controlled trial",
          "type": "article",
          "venue": "The Spine Journal",
          "cited_by_count": 12,
          "topics": [
            "Cervical and Thoracic Myelopathy",
            "Spine and Intervertebral Disc Pathology",
            "Spinal Fractures and Fixation Techniques"
          ]
        },
        {
          "openalex_id": "W4382358292",
          "year": 2023,
          "title": "Determinants of alcohol use among young males in two Indian states: A population‐based study",
          "type": "article",
          "venue": "Tropical Medicine & International Health",
          "cited_by_count": 3,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Prenatal Substance Exposure Effects",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4387017603",
          "year": 2023,
          "title": "Reply to letter to the editor regarding “Cost-effectiveness of implanting a prosthesis after anterior cervical discectomy for radiculopathy: results of the NECK randomized controlled trial”",
          "type": "letter",
          "venue": "The Spine Journal",
          "cited_by_count": 0,
          "topics": [
            "Cervical and Thoracic Myelopathy",
            "Spine and Intervertebral Disc Pathology",
            "Spinal Fractures and Fixation Techniques"
          ]
        },
        {
          "openalex_id": "W3092158397",
          "year": 2020,
          "title": "Community-based psychosocial substance use disorder interventions in low-and-middle-income countries: a narrative literature review",
          "type": "article",
          "venue": "International Journal of Mental Health Systems",
          "cited_by_count": 44,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Mental Health Treatment and Access",
            "Health Policy Implementation Science"
          ]
        }
      ]
    }
  },
  {
    "name": "Jan Henrik Terheyden",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2357-BT",
        "title": "Repeatability and validity of instructed and non-instructed EQ-5D-5L vision bolt-ons in age-related macular degeneration and diabetic eye disease",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5069023369",
      "display_name": "Jan Henrik Terheyden",
      "orcid": "0000-0002-0174-4066",
      "reported_affiliation": "University of Bonn",
      "works_count": 93,
      "top_topics": [
        {
          "topic": "Retinal Diseases and Treatments",
          "works": 49
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 34
        },
        {
          "topic": "Retinal Imaging and Analysis",
          "works": 23
        },
        {
          "topic": "Retinal and Optic Conditions",
          "works": 20
        },
        {
          "topic": "Ocular Diseases and Behçet’s Syndrome",
          "works": 18
        },
        {
          "topic": "Glaucoma and retinal disorders",
          "works": 12
        },
        {
          "topic": "Vasculitis and related conditions",
          "works": 9
        },
        {
          "topic": "Antioxidant Activity and Oxidative Stress",
          "works": 5
        },
        {
          "topic": "Otitis Media and Relapsing Polychondritis",
          "works": 4
        },
        {
          "topic": "Scoliosis diagnosis and treatment",
          "works": 4
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 4
        },
        {
          "topic": "Machine Learning in Healthcare",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Robert P. Finger",
          "works": 78
        },
        {
          "name": "Frank G. Holz",
          "works": 63
        },
        {
          "name": "Maximilian W. M. Wintergerst",
          "works": 31
        },
        {
          "name": "Charlotte Behning",
          "works": 31
        },
        {
          "name": "Matthias Schmid",
          "works": 25
        },
        {
          "name": "David P. Crabb",
          "works": 24
        },
        {
          "name": "Adnan Tufail",
          "works": 23
        },
        {
          "name": "Moritz Berger",
          "works": 21
        },
        {
          "name": "Ulrich F. O. Luhmann",
          "works": 21
        },
        {
          "name": "Steffen Schmitz-Valckenberg",
          "works": 18
        },
        {
          "name": "Sérgio Leal",
          "works": 17
        },
        {
          "name": "Marlene Saßmannshausen",
          "works": 16
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7160890159",
          "year": 2026,
          "title": "Determinants of vision-related quality of life in recessive Stargardt disease",
          "type": "article",
          "venue": "British Journal of Ophthalmology",
          "cited_by_count": 0,
          "topics": [
            "Retinal Development and Disorders",
            "Ophthalmology and Visual Impairment Studies",
            "Connexins and lens biology"
          ]
        },
        {
          "openalex_id": "W7140148162",
          "year": 2026,
          "title": "Hyperreflective Foci Contiguous With the Retinal Pigment Epithelium Associated With Visual Function in Aging, Early, and Intermediate Age-Related Macular Degeneration: MACUSTAR Study Report",
          "type": "article",
          "venue": "American Journal of Ophthalmology",
          "cited_by_count": 0,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Ophthalmology and Visual Impairment Studies",
            "Visual perception and processing mechanisms"
          ]
        },
        {
          "openalex_id": "W4408768619",
          "year": 2025,
          "title": "A new generation of patient-reported outcome measures with large language models",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 12,
          "topics": [
            "Cancer survivorship and care",
            "Artificial Intelligence in Healthcare and Education",
            "Machine Learning in Healthcare"
          ]
        },
        {
          "openalex_id": "W4411405260",
          "year": 2025,
          "title": "Advances in diagnosing and treating giant cell arteritis: New hope for arteritic anterior ischemic optic neuropathy",
          "type": "article",
          "venue": "Survey of Ophthalmology",
          "cited_by_count": 6,
          "topics": [
            "Vasculitis and related conditions",
            "Intraoperative Neuromonitoring and Anesthetic Effects",
            "Ocular Diseases and Behçet’s Syndrome"
          ]
        },
        {
          "openalex_id": "W4414564142",
          "year": 2025,
          "title": "Associations Between Structural Phenotype and Polygenic Risk Scores in Intermediate Age-Related Macular Degeneration – A MACUSTAR Report",
          "type": "article",
          "venue": "Translational Vision Science & Technology",
          "cited_by_count": 4,
          "topics": [
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies",
            "Retinal Imaging and Analysis"
          ]
        },
        {
          "openalex_id": "W4414537869",
          "year": 2025,
          "title": "Associations between patient-reported vision impairment in low luminance and vision-related quality of life in intermediate age-related macular degeneration",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 1,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Urban Green Space and Health",
            "Retinal Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W2558020255",
          "year": 2016,
          "title": "German validation of the BIDQ-S questionnaire on body image disturbance in idiopathic scoliosis",
          "type": "article",
          "venue": "European Spine Journal",
          "cited_by_count": 18,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Musculoskeletal pain and rehabilitation",
            "Myofascial pain diagnosis and treatment"
          ]
        },
        {
          "openalex_id": "W2754879837",
          "year": 2017,
          "title": "German validation of the quality of life profile for spinal disorders (QLPSD)",
          "type": "article",
          "venue": "European Spine Journal",
          "cited_by_count": 10,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Spine and Intervertebral Disc Pathology",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2769796042",
          "year": 2017,
          "title": "Menschliche Reproduktion in Schöne Neue Welt von Aldous Huxley",
          "type": "article",
          "venue": "Der Gynäkologe",
          "cited_by_count": 0,
          "topics": [
            "Historical Studies on Reproduction, Gender, Health, and Societal Changes",
            "Reproductive Health and Technologies"
          ]
        },
        {
          "openalex_id": "W2733595362",
          "year": 2017,
          "title": "Predictors of shoulder level after spinal fusion in adolescent idiopathic scoliosis",
          "type": "article",
          "venue": "European Spine Journal",
          "cited_by_count": 24,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Shoulder Injury and Treatment",
            "Spinal Fractures and Fixation Techniques"
          ]
        },
        {
          "openalex_id": "W2981975467",
          "year": 2019,
          "title": "Association of Vision-related Quality of Life with Visual Function in Age-Related Macular Degeneration",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 74,
          "topics": [
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies",
            "Retinal Imaging and Analysis"
          ]
        },
        {
          "openalex_id": "W3011628045",
          "year": 2020,
          "title": "Automated thresholding algorithms outperform manual thresholding in macular optical coherence tomography angiography image analysis",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 48,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Optical Coherence Tomography Applications"
          ]
        },
        {
          "openalex_id": "W3043154550",
          "year": 2020,
          "title": "Clinical study protocol for a low-interventional study in intermediate age-related macular degeneration developing novel clinical endpoints for interventional clinical trials with a regulatory and patient access intention—MACUSTAR",
          "type": "article",
          "venue": "Trials",
          "cited_by_count": 37,
          "topics": [
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies",
            "Glaucoma and retinal disorders"
          ]
        },
        {
          "openalex_id": "W4312083317",
          "year": 2022,
          "title": "Characteristics and Spatial Distribution of Structural Features in Age-Related Macular Degeneration",
          "type": "article",
          "venue": "Ophthalmology Retina",
          "cited_by_count": 36,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W2903046687",
          "year": 2018,
          "title": "Prevalence of Retinal Vein Occlusion in Europe: A Systematic Review and Meta-Analysis",
          "type": "review",
          "venue": "Ophthalmologica",
          "cited_by_count": 29,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal and Optic Conditions",
            "Retinal and Macular Surgery"
          ]
        },
        {
          "openalex_id": "W4294243474",
          "year": 2022,
          "title": "Relative ellipsoid zone reflectivity and its association with disease severity in age-related macular degeneration: a MACUSTAR study report",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 29,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Glaucoma and retinal disorders"
          ]
        },
        {
          "openalex_id": "W4220746090",
          "year": 2022,
          "title": "Changes of the retinal and choroidal vasculature in cerebral small vessel disease",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 28,
          "topics": [
            "Retinal Imaging and Analysis",
            "Glaucoma and retinal disorders",
            "Retinal Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W3120919313",
          "year": 2021,
          "title": "Development of the Vision Impairment in Low Luminance Questionnaire",
          "type": "article",
          "venue": "Translational Vision Science & Technology",
          "cited_by_count": 27,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Retinal Diseases and Treatments",
            "Balance, Gait, and Falls Prevention"
          ]
        }
      ]
    }
  },
  {
    "name": "Jan Verhaar",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "200-RA",
        "title": "EQ-5D health inequalities in orthopaedic patients. A Dutch registry-based study.",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5035697100",
      "display_name": "Jan A.N. Verhaar",
      "orcid": "0000-0003-3016-9600",
      "reported_affiliation": "Erasmus MC",
      "works_count": 573,
      "top_topics": [
        {
          "topic": "Osteoarthritis Treatment and Mechanisms",
          "works": 189
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 132
        },
        {
          "topic": "Knee injuries and reconstruction techniques",
          "works": 78
        },
        {
          "topic": "Shoulder Injury and Treatment",
          "works": 75
        },
        {
          "topic": "Tendon Structure and Treatment",
          "works": 74
        },
        {
          "topic": "Orthopaedic implants and arthroplasty",
          "works": 67
        },
        {
          "topic": "Orthopedic Surgery and Rehabilitation",
          "works": 60
        },
        {
          "topic": "Hip disorders and treatments",
          "works": 59
        },
        {
          "topic": "Sports injuries and prevention",
          "works": 55
        },
        {
          "topic": "Lower Extremity Biomechanics and Pathologies",
          "works": 54
        },
        {
          "topic": "Bone fractures and treatments",
          "works": 36
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 28
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sita Bierma‐Zeinstra",
          "works": 136
        },
        {
          "name": "Harrie Weinans",
          "works": 118
        },
        {
          "name": "Max Reijman",
          "works": 113
        },
        {
          "name": "Bart W. Koes",
          "works": 77
        },
        {
          "name": "J.H. Waarsing",
          "works": 62
        },
        {
          "name": "P.K. Bos",
          "works": 57
        },
        {
          "name": "Y.M. Bastiaansen-Jenniskens",
          "works": 48
        },
        {
          "name": "Gerjo J.V.M. van Osch",
          "works": 44
        },
        {
          "name": "Holger Jahr",
          "works": 37
        },
        {
          "name": "Robert‐Jan de Vos",
          "works": 36
        },
        {
          "name": "Gerjo J. V. M. van Osch",
          "works": 35
        },
        {
          "name": "Nicole Kops",
          "works": 34
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4406958353",
          "year": 2025,
          "title": "A head-to-head comparison of the adult EQ-5D-5L and youth EQ-5D-Y-5L in adolescents with idiopathic scoliosis",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Hip disorders and treatments",
            "Foot and Ankle Surgery"
          ]
        },
        {
          "openalex_id": "W4408220701",
          "year": 2025,
          "title": "Can we avoid casting for suspected scaphoid fractures? A multicenter randomized controlled trial",
          "type": "article",
          "venue": "Journal of Orthopaedics and Traumatology",
          "cited_by_count": 1,
          "topics": [
            "Orthopedic Surgery and Rehabilitation",
            "Facial Trauma and Fracture Management",
            "Traumatic Ocular and Foreign Body Injuries"
          ]
        },
        {
          "openalex_id": "W4415040832",
          "year": 2025,
          "title": "Correction: The influence of casting techniques on the redisplacement risk of reduced distal radius fractures in adults",
          "type": "erratum",
          "venue": "Archives of Orthopaedic and Trauma Surgery",
          "cited_by_count": 0,
          "topics": [
            "Orthopedic Surgery and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W4409497743",
          "year": 2025,
          "title": "Diagnostic domains, differential diagnosis and conditions requiring further medical attention that are considered important in the assessment for Achilles tendinopathy: a Delphi consensus study",
          "type": "article",
          "venue": "British Journal of Sports Medicine",
          "cited_by_count": 13,
          "topics": [
            "Tendon Structure and Treatment",
            "Sports injuries and prevention",
            "Foot and Ankle Surgery"
          ]
        },
        {
          "openalex_id": "W4410630560",
          "year": 2025,
          "title": "Socioeconomic inequalities in patient-reported outcome measures among total hip and knee arthroplasty patients: a comprehensive analysis of instruments and domains",
          "type": "article",
          "venue": "International Journal for Equity in Health",
          "cited_by_count": 6,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Patient Satisfaction in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4410923174",
          "year": 2025,
          "title": "The influence of casting techniques on the redisplacement risk of reduced distal radius fractures in adults",
          "type": "article",
          "venue": "Archives of Orthopaedic and Trauma Surgery",
          "cited_by_count": 3,
          "topics": [
            "Orthopedic Surgery and Rehabilitation",
            "Bone fractures and treatments",
            "Foot and Ankle Surgery"
          ]
        },
        {
          "openalex_id": "W2831828310",
          "year": 1969,
          "title": "SOME NOTES ON LANGUAGE AND THEOLOGY",
          "type": "article",
          "venue": "Bijdragen",
          "cited_by_count": 1,
          "topics": [
            "Behavioral and Psychological Studies"
          ]
        },
        {
          "openalex_id": "W2418897514",
          "year": 1982,
          "title": "[A patient with an isolated pancreatic injury followed by a pancreatic pseudocyst].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Autopsy Techniques and Outcomes",
            "Pancreatitis Pathology and Treatment"
          ]
        },
        {
          "openalex_id": "W2413486211",
          "year": 1984,
          "title": "[Handlebars in the belly, dust in the eyes? Pancreatic pseudocyst in children caused by trauma].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Pancreatitis Pathology and Treatment",
            "Pancreatic and Hepatic Oncology Research"
          ]
        },
        {
          "openalex_id": "W2412558427",
          "year": 1985,
          "title": "[The value of herniography in inexplicable inguinal pain].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 2,
          "topics": [
            "Hernia repair and management"
          ]
        },
        {
          "openalex_id": "W2063095747",
          "year": 2004,
          "title": "Prevalence and incidence of shoulder pain in the general population; a systematic review",
          "type": "review",
          "venue": "Scandinavian Journal of Rheumatology",
          "cited_by_count": 1356,
          "topics": [
            "Shoulder Injury and Treatment",
            "Nerve Injury and Rehabilitation",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2158175963",
          "year": 2010,
          "title": "Platelet-Rich Plasma Injection for Chronic Achilles Tendinopathy",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 841,
          "topics": [
            "Tendon Structure and Treatment",
            "Periodontal Regeneration and Treatments",
            "Shoulder Injury and Treatment"
          ]
        },
        {
          "openalex_id": "W2131971817",
          "year": 2012,
          "title": "Cam impingement causes osteoarthritis of the hip: a nationwide prospective cohort study (CHECK)",
          "type": "article",
          "venue": "Annals of the Rheumatic Diseases",
          "cited_by_count": 485,
          "topics": [
            "Hip disorders and treatments",
            "Osteoarthritis Treatment and Mechanisms",
            "Orthopaedic implants and arthroplasty"
          ]
        },
        {
          "openalex_id": "W2157131809",
          "year": 2011,
          "title": "Incidence of midportion Achilles tendinopathy in the general population",
          "type": "article",
          "venue": "British Journal of Sports Medicine",
          "cited_by_count": 483,
          "topics": [
            "Tendon Structure and Treatment",
            "Shoulder Injury and Treatment",
            "Sports injuries and prevention"
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
          "openalex_id": "W1990895739",
          "year": 2010,
          "title": "The infrapatellar fat pad should be considered as an active osteoarthritic joint tissue: a narrative review",
          "type": "review",
          "venue": "Osteoarthritis and Cartilage",
          "cited_by_count": 434,
          "topics": [
            "Osteoarthritis Treatment and Mechanisms",
            "Knee injuries and reconstruction techniques",
            "Lower Extremity Biomechanics and Pathologies"
          ]
        },
        {
          "openalex_id": "W2121620043",
          "year": 2008,
          "title": "Can Platelet-Rich Plasma Enhance Tendon Repair?",
          "type": "article",
          "venue": "The American Journal of Sports Medicine",
          "cited_by_count": 425,
          "topics": [
            "Tendon Structure and Treatment",
            "Periodontal Regeneration and Treatments",
            "Shoulder Injury and Treatment"
          ]
        },
        {
          "openalex_id": "W2099204150",
          "year": 2011,
          "title": "Platelet-Rich Plasma Releasate Inhibits Inflammatory Processes in Osteoarthritic Chondrocytes",
          "type": "article",
          "venue": "The American Journal of Sports Medicine",
          "cited_by_count": 408,
          "topics": [
            "Periodontal Regeneration and Treatments",
            "Osteoarthritis Treatment and Mechanisms",
            "Platelet Disorders and Treatments"
          ]
        }
      ]
    }
  },
  {
    "name": "Janine van Til",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "285-PHD",
        "title": "To capitalize on the clinical value of EQ-5D - communicating and predicting patient outcomes on the individual patient level",
        "working_group": "Descriptive Systems, Valuation, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5070605387",
      "display_name": "Janine A. van Til",
      "orcid": "0000-0002-5416-5893",
      "reported_affiliation": "University of Twente",
      "works_count": 135,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 42
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 36
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 19
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 10
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 8
        },
        {
          "topic": "Multi-Criteria Decision Making",
          "works": 7
        },
        {
          "topic": "Child and Adolescent Health",
          "works": 7
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 6
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 6
        },
        {
          "topic": "Cardiac Arrest and Resuscitation",
          "works": 5
        },
        {
          "topic": "Breast Cancer Treatment Studies",
          "works": 5
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Maarten J. IJzerman",
          "works": 49
        },
        {
          "name": "Karin Groothuis‐Oudshoorn",
          "works": 44
        },
        {
          "name": "Marieke G.M. Weernink",
          "works": 17
        },
        {
          "name": "Jorien Veldwijk",
          "works": 12
        },
        {
          "name": "Clemens von Birgelen",
          "works": 10
        },
        {
          "name": "Magda M. Boere‐Boonekamp",
          "works": 10
        },
        {
          "name": "Mattijs Lambooij",
          "works": 9
        },
        {
          "name": "Sabine Siesling",
          "works": 7
        },
        {
          "name": "Domino Determann",
          "works": 7
        },
        {
          "name": "Ida J. Korfage",
          "works": 7
        },
        {
          "name": "Mireille Goetghebeur",
          "works": 6
        },
        {
          "name": "Irina Cleemput",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7147080508",
          "year": 2026,
          "title": "Comprehension of and preferences for visualization of patient-reported outcome data to support clinical decision making: A systematic review",
          "type": "review",
          "venue": "Patient Education and Counseling",
          "cited_by_count": 0,
          "topics": [
            "Data Visualization and Analytics",
            "Nursing Diagnosis and Documentation",
            "Electronic Health Records Systems"
          ]
        },
        {
          "openalex_id": "W7124701132",
          "year": 2026,
          "title": "Mapping fatigue attributes in patient preference studies to existing fatigue-specific PROs",
          "type": "other",
          "venue": "Open Science Framework",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7148600958",
          "year": 2026,
          "title": "Putting Patient Voices at the Heart of Healthcare Decisions: The UNIFIED Public-Private Project",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 0,
          "topics": [
            "Global Healthcare and Medical Tourism",
            "Mental Health and Patient Involvement",
            "Global Health and Surgery"
          ]
        },
        {
          "openalex_id": "W7143425472",
          "year": 2026,
          "title": "Toward Data-Driven Profiles to Support Shared Decision-Making, for Patients with COPD: A Latent Class Analysis",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W7143457659",
          "year": 2026,
          "title": "Toward Data-Driven Profiles to Support Shared Decision-Making, for Patients with COPD: A Latent Class Analysis",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W7143503835",
          "year": 2026,
          "title": "Toward Data-Driven Profiles to Support Shared Decision-Making, for Patients with COPD: A Latent Class Analysis",
          "type": "article",
          "venue": "International Journal of Human-Computer Interaction",
          "cited_by_count": 0,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Chronic Disease Management Strategies",
            "Cardiovascular Health and Risk Factors"
          ]
        },
        {
          "openalex_id": "W1586072584",
          "year": 2003,
          "title": "Evaluating rehabilitation technology with the analytic hierarchy process",
          "type": "conference-paper",
          "venue": "University of Twente Research Information",
          "cited_by_count": 0,
          "topics": [
            "Advanced Scientific Research Methods",
            "Advanced Research in Systems and Signal Processing",
            "Engineering Diagnostics and Reliability"
          ]
        },
        {
          "openalex_id": "W2171629514",
          "year": 2003,
          "title": "Gezamenlijke besluitvorming (shared decision making): patiënt- en behandelaarsbehoeften in balans",
          "type": "article",
          "venue": "University of Twente Research Information",
          "cited_by_count": 1,
          "topics": [
            "Clinical practice guidelines implementation",
            "Dutch Social and Cultural Studies",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W1676226417",
          "year": 2003,
          "title": "Preferences for health staes as an alternative for descriptive quality of life measurement: the valuation of treatment outcomes in spinal cord injury",
          "type": "article",
          "venue": "University of Twente Research Information",
          "cited_by_count": 0,
          "topics": [
            "Hermeneutics and Narrative Identity",
            "Aging, Elder Care, and Social Issues",
            "Health, Medicine and Society"
          ]
        },
        {
          "openalex_id": "W2121713767",
          "year": 2005,
          "title": "A multicriteria decision analysis of augmentative treatment of upper limbs in persons with tetraplegia",
          "type": "article",
          "venue": "The Journal of Rehabilitation Research and Development",
          "cited_by_count": 40,
          "topics": [
            "Nerve Injury and Rehabilitation",
            "Spinal Cord Injury Research",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W2170621602",
          "year": 2012,
          "title": "From efficacy to equity: Literature review of decision criteria for resource allocation and healthcare decisionmaking",
          "type": "article",
          "venue": "Cost Effectiveness and Resource Allocation",
          "cited_by_count": 229,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2954640182",
          "year": 2019,
          "title": "Multicriteria Decision Analysis to Support Health Technology Assessment Agencies: Benefits, Limitations, and the Way Forward",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 167,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W2169449290",
          "year": 2015,
          "title": "A Review and Classification of Approaches for Dealing with Uncertainty in Multi-Criteria Decision Analysis for Healthcare Decisions",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 137,
          "topics": [
            "Multi-Criteria Decision Making",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2614295913",
          "year": 2017,
          "title": "Early EEG for outcome prediction of postanoxic coma: prospective cohort study with cost-minimization analysis",
          "type": "article",
          "venue": "Critical Care",
          "cited_by_count": 102,
          "topics": [
            "Cardiac Arrest and Resuscitation",
            "Traumatic Brain Injury and Neurovascular Disturbances",
            "Traumatic Brain Injury Research"
          ]
        },
        {
          "openalex_id": "W2610867018",
          "year": 2017,
          "title": "Patient preference for radial versus femoral vascular access for elective coronary procedures: The PREVAS study",
          "type": "article",
          "venue": "Catheterization and Cardiovascular Interventions",
          "cited_by_count": 100,
          "topics": [
            "Vascular Procedures and Complications",
            "Central Venous Catheters and Hemodialysis",
            "Peripheral Artery Disease Management"
          ]
        },
        {
          "openalex_id": "W3109936636",
          "year": 2013,
          "title": "WHICH CRITERIA ARE CONSIDERED IN HEALTHCARE DECISIONS? INSIGHTS FROM AN INTERNATIONAL SURVEY OF POLICY AND CLINICAL DECISION MAKERS",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 99,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2101813937",
          "year": 2014,
          "title": "MEDICAL DEVICES EARLY ASSESSMENT METHODS: SYSTEMATIC LITERATURE REVIEW",
          "type": "review",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 88,
          "topics": [
            "Quality and Safety in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Biomedical and Engineering Education"
          ]
        },
        {
          "openalex_id": "W2005489709",
          "year": 2014,
          "title": "A Systematic Review to Identify the Use of Preference Elicitation Methods in Healthcare Decision Making",
          "type": "review",
          "venue": "Pharmaceutical Medicine",
          "cited_by_count": 68,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare"
          ]
        }
      ]
    }
  },
  {
    "name": "Janine Verstraete",
    "member_affiliation": "University of Cape Town",
    "is_member": true,
    "projects": [
      {
        "project_id": "142-RA",
        "title": "Performance of the EQ-5D-Y Interviewer Administered Version in young children aged 5-8 years",
        "working_group": "Youth"
      },
      {
        "project_id": "147-RA",
        "title": "Exploring the EQ-5D adult and youth descriptive systems",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "1681-RA",
        "title": "Health-Related Quality of Life in children attending specialist health services",
        "working_group": "Youth"
      },
      {
        "project_id": "1859-TVG",
        "title": "Travel Grant to visit the University of Sheffield for Qualitative analysis of EQ-TIPS qualitative data on content validity.",
        "working_group": "Youth, Education and Outreach"
      },
      {
        "project_id": "1928-RA",
        "title": "Psychometric Testing of the EuroQol Toddler and Infant Populations (EQ-TIPS) Measure of Health Related Quality of Life",
        "working_group": "Youth"
      },
      {
        "project_id": "20180730",
        "title": "Validation of the UK English version of EQ-5D-Y-5L in South Africa",
        "working_group": "Youth"
      },
      {
        "project_id": "20190200",
        "title": "Validation of the Chichewa versions of the EQ-5D-Y-3L and the EQ-5D-Y-5L in Malawi",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20190670",
        "title": "Cross-cultural Validity and Reliability Testing of the Toddler and Infant (TANDI) Health Related Quality of Life Measure, an experimental version of the EQ-5D-Y Proxy",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "2226-TR",
        "title": "Translation of EQ-TIPS into 10 most requested language versions",
        "working_group": "Youth"
      },
      {
        "project_id": "2633-TVG",
        "title": "Travel Grant to support speakers of two EuroQol symposia focused on the Experimental Instruments (EQ-HWB-9, EQ-TIPS and ToolboxTM)",
        "working_group": "Others"
      },
      {
        "project_id": "365-RA",
        "title": "Measuring Health-Related Quality of Life (HRQoL) in the Youngest Population",
        "working_group": "Youth"
      },
      {
        "project_id": "425-RA",
        "title": "Health-Related Quality of Life in children living with cystic fibrosis (CF)",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "426-RA",
        "title": "Health-Related Quality of Life in children dependent on technology for breathing",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5006452129",
      "display_name": "Janine Verstraete",
      "orcid": "0000-0002-1148-4747",
      "reported_affiliation": "University of Cape Town",
      "works_count": 88,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 25
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 14
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 12
        },
        {
          "topic": "Cystic Fibrosis Research Advances",
          "works": 9
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 8
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 7
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 6
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 5
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 5
        },
        {
          "topic": "Health Education and Validation",
          "works": 5
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 4
        },
        {
          "topic": "Pharmaceutical studies and practices",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "E Tritsmans",
          "works": 18
        },
        {
          "name": "J Vanslype",
          "works": 17
        },
        {
          "name": "Marco Zampoli",
          "works": 15
        },
        {
          "name": "Des Scott",
          "works": 11
        },
        {
          "name": "Jennifer Jelsma",
          "works": 9
        },
        {
          "name": "Michael Herdman",
          "works": 8
        },
        {
          "name": "Nancy Devlin",
          "works": 6
        },
        {
          "name": "Heather J. Zar",
          "works": 6
        },
        {
          "name": "Razia Amien",
          "works": 6
        },
        {
          "name": "Samar Farid",
          "works": 6
        },
        {
          "name": "Lasse Herdien",
          "works": 5
        },
        {
          "name": "Nan Luo",
          "works": 5
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
          "openalex_id": "W7131850503",
          "year": 2026,
          "title": "Additional file 1 of Translation and cultural adaptation of the EQ-5D-Y-5L into Modern Standard Arabic for use in Egypt",
          "type": "article",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": [
            "Natural Language Processing Techniques",
            "Speech Recognition and Synthesis",
            "Linguistic Studies and Language Acquisition"
          ]
        },
        {
          "openalex_id": "W7131889548",
          "year": 2026,
          "title": "Additional file 1 of Translation and cultural adaptation of the EQ-5D-Y-5L into Modern Standard Arabic for use in Egypt",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Natural Language Processing Techniques",
            "Speech Recognition and Synthesis",
            "Linguistic Studies and Language Acquisition"
          ]
        },
        {
          "openalex_id": "W7140301642",
          "year": 2026,
          "title": "Agreement and measurement properties of the interviewer-administered, self-completed and proxy‐reported versions of the Tigrinya EQ-5D-Y-5L in Ethiopia",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Genomics and Rare Diseases",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W7166657717",
          "year": 2026,
          "title": "DEVELOPMENT OF A HEALTH-RELATED QUALITY OF LIFE (HRQOL) INSTRUMENT FOR VERY YOUNG CHILDREN, DERIVED FROM THE EQ-5D-Y, FOR PROXY COMPLETION",
          "type": "conference-paper",
          "venue": "World Physiotherapy Congress Archive",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W3089395788",
          "year": 1948,
          "title": "Hemorrhage, blood transfusion and air pressure homeostasis.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 2,
          "topics": [
            "Trauma, Hemostasis, Coagulopathy, Resuscitation",
            "Respiratory Support and Mechanisms",
            "Traumatic Brain Injury and Neurovascular Disturbances"
          ]
        },
        {
          "openalex_id": "W3090977804",
          "year": 1948,
          "title": "Hemorrhage, blood transfusion, and homeostasis of blood pressure.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Trauma, Hemostasis, Coagulopathy, Resuscitation",
            "Traumatic Brain Injury and Neurovascular Disturbances"
          ]
        },
        {
          "openalex_id": "W2404216738",
          "year": 1957,
          "title": "[Factors influencing favorably formation of chlamydospores in Candida albicans in Nickerson-Mankowski's medium].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Antifungal resistance and susceptibility",
            "Autoimmune Bullous Skin Diseases",
            "Autoimmune and Inflammatory Disorders"
          ]
        },
        {
          "openalex_id": "W2328719592",
          "year": 1958,
          "title": "Factors promoting the formation of chlamydospores in Candida albicans on the Nickerson-Mankowski medium.",
          "type": "article",
          "venue": "Compte rendu des seances de la Societe de biologie",
          "cited_by_count": 0,
          "topics": [
            "Autoimmune Bullous Skin Diseases",
            "Antifungal resistance and susceptibility",
            "Reproductive tract infections research"
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
          "openalex_id": "W3103882586",
          "year": 2020,
          "title": "Validity and reliability testing of the Toddler and Infant (TANDI) Health Related Quality of Life instrument for very young children",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 56,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Pediatric Pain Management Techniques",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W3003049071",
          "year": 2020,
          "title": "Item generation for a proxy health related quality of life measure in very young children",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 51,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Delphi Technique in Research",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4284892570",
          "year": 2022,
          "title": "Valuing EQ-5D-Y: the current state of play",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 50,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Early Childhood Education and Development",
            "Child and Animal Learning Development"
          ]
        },
        {
          "openalex_id": "W4211054812",
          "year": 2022,
          "title": "Why Do Adults Value EQ-5D-Y-3L Health States Differently for Themselves Than for Children and Adolescents: A Think-Aloud Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 47,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2024374861",
          "year": 2009,
          "title": "The Effect of Sustained Phonation at High and Low Pitch on Vocal Jitter and Shimmer",
          "type": "article",
          "venue": "Folia Phoniatrica et Logopaedica",
          "cited_by_count": 39,
          "topics": [
            "Voice and Speech Disorders",
            "Speech Recognition and Synthesis"
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
        }
      ]
    }
  }
]
