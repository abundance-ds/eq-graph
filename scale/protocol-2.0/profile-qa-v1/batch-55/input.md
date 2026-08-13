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

Assess all 1 people.

[
  {
    "name": "Zhuxin Mao",
    "member_affiliation": "University of Antwerp",
    "is_member": true,
    "projects": [
      {
        "project_id": "103-RA",
        "title": "Using EQ-5D to measure health status in Chinese populations during the COVID-19 pandemic",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1580-RA",
        "title": "Exploring subjective constructions of quality of life as defined by EQ-HWB in patients, carers and the healthy general publics: a Q-methodological study",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1588-RA",
        "title": "An exploratory study on the constructs of health-related quality of life and mental well-being: results from a Belgian population survey",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20190990",
        "title": "Regional differences in health-related quality of life in England: EQ-5D in national surveys of the general population",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20191000",
        "title": "Testing the appropriateness of EQ-5D in a socioeconomically disadvantaged population",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2084-RA",
        "title": "Vision and Hearing Bolt-ons for the EQ-5D-3L and EQ-5D- 5L: A Systematic Review",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2422-RA",
        "title": "Exploring the measurement properties of EQ-5D-5L and the breathing bolt-on in older adults at risk of influenza-like illness: a multi-country cohort analysis",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "398-RA",
        "title": "To what extent does EQ-5D reflect the health concepts of Chinese: a scoping review",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5002022038",
      "display_name": "Zhuxin Mao",
      "orcid": "0000-0002-7444-1584",
      "reported_affiliation": "University of Antwerp",
      "works_count": 68,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 24
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 6
        },
        {
          "topic": "Respiratory viral infections research",
          "works": 6
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 6
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 5
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 5
        },
        {
          "topic": "Microbial Community Ecology and Physiology",
          "works": 5
        },
        {
          "topic": "Soil Carbon and Nitrogen Dynamics",
          "works": 5
        },
        {
          "topic": "Gut microbiota and health",
          "works": 4
        },
        {
          "topic": "Global Health Care Issues",
          "works": 4
        },
        {
          "topic": "Agricultural pest management studies",
          "works": 3
        },
        {
          "topic": "Genetic and Environmental Crop Studies",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Zhihao Yang",
          "works": 15
        },
        {
          "name": "Philippe Beutels",
          "works": 14
        },
        {
          "name": "Shunping Li",
          "works": 14
        },
        {
          "name": "Joke Bilcke",
          "works": 9
        },
        {
          "name": "Pei Wang",
          "works": 8
        },
        {
          "name": "Xiao Li",
          "works": 7
        },
        {
          "name": "Lander Willem",
          "works": 7
        },
        {
          "name": "Gang Chen",
          "works": 7
        },
        {
          "name": "Nan Luo",
          "works": 7
        },
        {
          "name": "Ming Yue",
          "works": 7
        },
        {
          "name": "Paul Kind",
          "works": 6
        },
        {
          "name": "Yifan Ding",
          "works": 6
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
          "openalex_id": "W4417064109",
          "year": 2025,
          "title": "Changes in health-related quality of life and its influencing factors of patients after percutaneous coronary intervention in China: A single-center longitudinal study",
          "type": "article",
          "venue": "Medicine",
          "cited_by_count": 0,
          "topics": [
            "Cardiac Health and Mental Health",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pain Management and Treatment"
          ]
        },
        {
          "openalex_id": "W4409110356",
          "year": 2025,
          "title": "Correction to: Evaluating the content validity of the EQ-5D-Y for Chinese children and adolescents",
          "type": "erratum",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Technology Assessment and Management"
          ]
        },
        {
          "openalex_id": "W4411817531",
          "year": 2025,
          "title": "Cost-effectiveness of Abrysvo® and Beyfortus® against RSV infections in Belgian infants",
          "type": "book",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Pediatric health and respiratory diseases",
            "Infant Health and Development",
            "Herpesvirus Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W4415783829",
          "year": 2025,
          "title": "Cost-effectiveness of maternal vaccine and/or monoclonal antibody strategies against respiratory syncytial virus in Belgian infants",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Respiratory viral infections research",
            "Virology and Viral Diseases",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4414531471",
          "year": 2025,
          "title": "Design and selection of items for a new health-related quality of life instrument with infertility patients (Infertility-QoL): a national multicenter, four-phase, mixed-methods study",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Reproductive Health and Technologies",
            "Ovarian function and disorders",
            "Family Dynamics and Relationships"
          ]
        },
        {
          "openalex_id": "W1987818008",
          "year": 2012,
          "title": "Effect of temperature on fatty acid content in Vicia sativa",
          "type": "article",
          "venue": "Journal of Consumer Protection and Food Safety",
          "cited_by_count": 4,
          "topics": [
            "Agricultural pest management studies",
            "Genetic and Environmental Crop Studies",
            "Botanical Research and Chemistry"
          ]
        },
        {
          "openalex_id": "W2001910671",
          "year": 2012,
          "title": "Fatty acid content of common vetch (Vicia sativa L.) in different regions of Northwest China",
          "type": "article",
          "venue": "Biochemical Systematics and Ecology",
          "cited_by_count": 24,
          "topics": [
            "Agronomic Practices and Intercropping Systems",
            "Genetic and Environmental Crop Studies",
            "Agricultural pest management studies"
          ]
        },
        {
          "openalex_id": "W2376549888",
          "year": 2013,
          "title": "A study on forage nutritional quality of Elymus nutans from different populations in the Qinghai-Tibet Plateau",
          "type": "article",
          "venue": "Acta Pratacultural Science",
          "cited_by_count": 4,
          "topics": [
            "Medicinal Plant Studies",
            "Mycotoxins in Agriculture and Food"
          ]
        },
        {
          "openalex_id": "W1987119343",
          "year": 2014,
          "title": "Fatty acid, amino acid, and mineral composition of four common vetch seeds on Qinghai-Tibetan plateau",
          "type": "article",
          "venue": "Food Chemistry",
          "cited_by_count": 49,
          "topics": [
            "Agricultural pest management studies",
            "Botanical Research and Chemistry",
            "Genetic and Environmental Crop Studies"
          ]
        },
        {
          "openalex_id": "W3128794245",
          "year": 2021,
          "title": "Similarities and Differences in Health-Related Quality-of-Life Concepts Between the East and the West: A Qualitative Analysis of the Content of Health-Related Quality-of-Life Measures",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 61,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychological Well-being and Life Satisfaction",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4318766800",
          "year": 2023,
          "title": "Cost-effectiveness of monoclonal antibody and maternal immunization against respiratory syncytial virus (RSV) in infants: Evaluation for six European countries",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 54,
          "topics": [
            "Respiratory viral infections research",
            "Immunodeficiency and Autoimmune Disorders",
            "COVID-19 Impact on Reproduction"
          ]
        },
        {
          "openalex_id": "W4328047899",
          "year": 2023,
          "title": "Economic burden and health-related quality-of-life among infants with respiratory syncytial virus infection: A multi-country prospective cohort study in Europe",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 54,
          "topics": [
            "Respiratory viral infections research",
            "Delphi Technique in Research",
            "Neonatal Respiratory Health Research"
          ]
        },
        {
          "openalex_id": "W4213417758",
          "year": 2022,
          "title": "Economic Burden and Health-Related Quality of Life of Respiratory Syncytial Virus and Influenza Infection in European Community-Dwelling Older Adults",
          "type": "article",
          "venue": "The Journal of Infectious Diseases",
          "cited_by_count": 45,
          "topics": [
            "Respiratory viral infections research",
            "Influenza Virus Research Studies",
            "Pneumonia and Respiratory Infections"
          ]
        },
        {
          "openalex_id": "W3032394243",
          "year": 2020,
          "title": "Exploring subjective constructions of health in China: a Q-methodological investigation",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 24,
          "topics": [
            "Q Methodology Applications",
            "Cardiovascular Health and Risk Factors",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4392468086",
          "year": 2024,
          "title": "A Head-to-Head Comparison of EQ-HWB and EQ-5D-5L in Patients, Carers, and General Public in China",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 23,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Mental Health and Patient Involvement",
            "Diabetes Management and Education"
          ]
        }
      ]
    }
  }
]
