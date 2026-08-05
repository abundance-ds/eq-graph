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
    "name": "Kristina Burström",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2016480",
        "title": "Analysis of EQ-5D profile data and EQ VAS scores across patient groups in the Swedish National Quality Registers and use in developing alternative ways of summarizing EQ-5D data.",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5005862614",
      "display_name": "Kristina Burström",
      "orcid": "0000-0001-9996-4317",
      "reported_affiliation": "Karolinska Institutet",
      "works_count": 89,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 47
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 20
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 8
        },
        {
          "topic": "Global Health Care Issues",
          "works": 8
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 8
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 7
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 7
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 7
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 6
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 5
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 5
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bo Bur­ström",
          "works": 23
        },
        {
          "name": "Ola Rolfson",
          "works": 15
        },
        {
          "name": "Jiaying Chen",
          "works": 13
        },
        {
          "name": "Mimmi Åström",
          "works": 13
        },
        {
          "name": "Sun Sun",
          "works": 12
        },
        {
          "name": "Ann‐Charlotte Egmar",
          "works": 11
        },
        {
          "name": "Magnus Johannesson",
          "works": 10
        },
        {
          "name": "Fitsum Sebsibe Teni",
          "works": 10
        },
        {
          "name": "Paul Kind",
          "works": 9
        },
        {
          "name": "Nancy Devlin",
          "works": 7
        },
        {
          "name": "Ulf‐G. Gerdtham",
          "works": 7
        },
        {
          "name": "Wolfgang Greiner",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4411957459",
          "year": 2025,
          "title": "Studying an educational intervention and its impact on health-related quality of life and fasting blood glucose levels among patients with type 2 diabetes mellitus in rural China",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 1,
          "topics": [
            "Diabetes Management and Education",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4363677835",
          "year": 2023,
          "title": "Experience-based health state valuation using the EQ VAS: a register-based study of the EQ-5D-3L among nine patient groups in Sweden",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 26,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4313625145",
          "year": 2023,
          "title": "Socio-demographic indicators of self-reported health based on EQ-5D-3L: A cross-country analysis of population surveys from 18 countries",
          "type": "article",
          "venue": "Frontiers in Public Health",
          "cited_by_count": 13,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, psychology, and well-being",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W4362706230",
          "year": 2023,
          "title": "Use of the visual analogue scale for health state valuation: a scoping review",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 151,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4210399103",
          "year": 2022,
          "title": "Exploring EQ-5D-Y-3L Experience-Based VAS Values Derived Among Adolescents",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 9,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4205823567",
          "year": 2022,
          "title": "Longitudinal study of patients’ health-related quality of life using EQ-5D-3L in 11 Swedish National Quality Registers",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 16,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W110549433",
          "year": 1998,
          "title": "Price Setting for Doctors",
          "type": "book-chapter",
          "venue": "Developments in health economics and public policy",
          "cited_by_count": 3,
          "topics": [
            "Healthcare Policy and Management",
            "Global Health Care Issues",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1972739397",
          "year": 2001,
          "title": "Health-related quality of life by disease and socio-economic group in the general population in Sweden",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 249,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1539664312",
          "year": 2001,
          "title": "Swedish population health-related quality of life results using the EQ-5D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 664,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W2154390046",
          "year": 2002,
          "title": "Cross-national comparability of burden of disease estimates: the European Disability Weights Project.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 72,
          "topics": [
            "Cerebral Palsy and Movement Disorders",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes"
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
          "openalex_id": "W2064869088",
          "year": 2010,
          "title": "Feasibility, reliability, and validity of the EQ-5D-Y: results from a multinational study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 475,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W2130267399",
          "year": 2013,
          "title": "Swedish experience-based value sets for EQ-5D health states",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 352,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2043007588",
          "year": 2010,
          "title": "Population health status in China: EQ-5D results, by age, sex and socio-economic status, from the National Health Services Survey 2008",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 235,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2804874827",
          "year": 2018,
          "title": "Time Trade-Off Value Set for EQ-5D-3L Based on a Nationally Representative Chinese Population Survey",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 177,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Quality Function Deployment in Product Design"
          ]
        },
        {
          "openalex_id": "W1970182218",
          "year": 2015,
          "title": "Subjective Well-Being and Its Association with Subjective Health Status, Age, Sex, Region, and Socio-economic Characteristics in a Chinese Population Study",
          "type": "article",
          "venue": "Journal of Happiness Studies",
          "cited_by_count": 166,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Health disparities and outcomes",
            "Mental Health Research Topics"
          ]
        }
      ]
    }
  },
  {
    "name": "Kristina Ludwig",
    "member_affiliation": "(1) Department of Health Economics & Health Care Management, School of Public Health, Bielefeld University, Germany; (2) EuroQol Research Foundation",
    "is_member": true,
    "projects": [
      {
        "project_id": "1762-RA",
        "title": "The impact of medical diagnosis on German EQ-5D values using the DCE with duration protocol",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5035184665",
      "display_name": "Kristina Ludwig",
      "orcid": "0000-0002-4306-4667",
      "reported_affiliation": "Bielefeld University",
      "works_count": 46,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 26
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 6
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 5
        },
        {
          "topic": "Health and Medical Studies",
          "works": 5
        },
        {
          "topic": "Transplantation: Methods and Outcomes",
          "works": 4
        },
        {
          "topic": "Renal Transplantation Outcomes and Treatments",
          "works": 4
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 3
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 2
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 2
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 2
        },
        {
          "topic": "Traumatic Brain Injury and Neurovascular Disturbances",
          "works": 2
        },
        {
          "topic": "Organ Transplantation Techniques and Outcomes",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Wolfgang Greiner",
          "works": 22
        },
        {
          "name": "Simone Kreimeier",
          "works": 16
        },
        {
          "name": "Tessa Peasgood",
          "works": 7
        },
        {
          "name": "Ole Marten",
          "works": 7
        },
        {
          "name": "Juan Manuel Ramos-Goñi",
          "works": 6
        },
        {
          "name": "Clara Mukuria",
          "works": 6
        },
        {
          "name": "Nancy Devlin",
          "works": 6
        },
        {
          "name": "María Belizán",
          "works": 5
        },
        {
          "name": "Jill Carlton",
          "works": 5
        },
        {
          "name": "Jasper Iske",
          "works": 5
        },
        {
          "name": "Bettina Wiegmann",
          "works": 5
        },
        {
          "name": "F. Ius",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4409974057",
          "year": 2025,
          "title": "Assessing the effectiveness and cost-effectiveness of a smart home emergency call system: study protocol for a randomised controlled trial in Germany",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 2,
          "topics": [
            "Emergency and Acute Care Studies",
            "Healthcare Technology and Patient Monitoring",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W4407819653",
          "year": 2025,
          "title": "Gender-based variations in surgical management of colorectal liver metastases: comprehensive analysis",
          "type": "article",
          "venue": "BMC Cancer",
          "cited_by_count": 2,
          "topics": [
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Colorectal Cancer Treatments and Studies",
            "Gastric Cancer Management and Outcomes"
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
          "openalex_id": "W4417481846",
          "year": 2025,
          "title": "PCR162 Multinational Qualitative Testing of the Experimental EuroQol Toddler and Infant Populations (EQ-TIPS) Instrument",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W4395028994",
          "year": 2024,
          "title": "From morbidity reduction to cost-effectiveness: Enhanced recovery after surgery (ERAS) society recommendations in minimal invasive liver surgery",
          "type": "article",
          "venue": "Langenbeck s Archives of Surgery",
          "cited_by_count": 8,
          "topics": [
            "Enhanced Recovery After Surgery",
            "Nutrition and Health in Aging",
            "Cardiac, Anesthesia and Surgical Outcomes"
          ]
        },
        {
          "openalex_id": "W4400538585",
          "year": 2024,
          "title": "Using the OPUF approach to create a value set for the EQ-HWB-S: An exploratory feasibility study",
          "type": "article",
          "venue": "Wellcome Open Research",
          "cited_by_count": 5,
          "topics": [
            "Advanced Statistical Process Monitoring"
          ]
        },
        {
          "openalex_id": "W2072654417",
          "year": 1965,
          "title": "Emulgatoren in Nahrungsmitteln",
          "type": "article",
          "venue": "Fette Seifen Anstrichmittel",
          "cited_by_count": 5,
          "topics": [
            "Biopolymer Synthesis and Applications",
            "Freezing and Crystallization Processes",
            "Polyamine Metabolism and Applications"
          ]
        },
        {
          "openalex_id": "W1979772559",
          "year": 1967,
          "title": "Moderne Emulgatoren: Die Grundlage verbesserter Formbeständigkeit von Eiskrem",
          "type": "article",
          "venue": "Fette Seifen Anstrichmittel",
          "cited_by_count": 2,
          "topics": [
            "biodegradable polymer synthesis and properties",
            "Surface Modification and Superhydrophobicity",
            "Textile materials and evaluations"
          ]
        },
        {
          "openalex_id": "W2050194648",
          "year": 1968,
          "title": "Moderne Emulgatoren als Backhilfsmittel",
          "type": "article",
          "venue": "Fette Seifen Anstrichmittel",
          "cited_by_count": 4,
          "topics": [
            "Food Industry and Aquatic Biology"
          ]
        },
        {
          "openalex_id": "W2029929763",
          "year": 1969,
          "title": "Moderne Emulgatoren zur Verzögerung der Fettreifbildung bei Schokolade",
          "type": "article",
          "venue": "Fette Seifen Anstrichmittel",
          "cited_by_count": 14,
          "topics": [
            "Food Chemistry and Fat Analysis",
            "biodegradable polymer synthesis and properties",
            "Material Properties and Processing"
          ]
        },
        {
          "openalex_id": "W2788008365",
          "year": 2018,
          "title": "German Value Set for the EQ-5D-5L",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 614,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
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
          "openalex_id": "W3000338306",
          "year": 2020,
          "title": "A French Value Set for the EQ-5D-5L",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 164,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
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
          "openalex_id": "W1975999506",
          "year": 2002,
          "title": "Brain stem lesions after head injury",
          "type": "article",
          "venue": "Neurological Research",
          "cited_by_count": 63,
          "topics": [
            "Traumatic Brain Injury and Neurovascular Disturbances",
            "Traumatic Brain Injury Research",
            "Cardiac Arrest and Resuscitation"
          ]
        },
        {
          "openalex_id": "W4281285777",
          "year": 2022,
          "title": "EQ-5D-Y Value Set for Germany",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 43,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W4214702737",
          "year": 2022,
          "title": "Generation, Selection, and Face Validation of Items for a New Generic Measure of Quality of Life: The EQ-HWB",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 38,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "Patient Satisfaction in Healthcare"
          ]
        }
      ]
    }
  },
  {
    "name": "Kristina Secnik Boye",
    "member_affiliation": "Eli Lilly and Company",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5039006946",
      "display_name": "Kristina S. Boye",
      "orcid": "0000-0002-5953-5929",
      "reported_affiliation": "Eli Lilly (United States)",
      "works_count": 243,
      "top_topics": [
        {
          "topic": "Diabetes Treatment and Management",
          "works": 145
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 76
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 47
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 46
        },
        {
          "topic": "Diabetes, Cardiovascular Risks, and Lipoproteins",
          "works": 43
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 39
        },
        {
          "topic": "Bariatric Surgery and Outcomes",
          "works": 39
        },
        {
          "topic": "Metabolism, Diabetes, and Cancer",
          "works": 23
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 17
        },
        {
          "topic": "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
          "works": 17
        },
        {
          "topic": "Obesity and Health Practices",
          "works": 14
        },
        {
          "topic": "Pharmacology and Obesity Treatment",
          "works": 14
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Louis S. Matza",
          "works": 45
        },
        {
          "name": "Maureen J. Lage",
          "works": 29
        },
        {
          "name": "Kirsi Norrbacka",
          "works": 27
        },
        {
          "name": "Hélène Sapin",
          "works": 26
        },
        {
          "name": "Katie D. Stewart",
          "works": 25
        },
        {
          "name": "Vivian T. Thieu",
          "works": 21
        },
        {
          "name": "Luis‐Emilio García‐Pérez",
          "works": 21
        },
        {
          "name": "Bruno Guerci",
          "works": 20
        },
        {
          "name": "Jay Bae",
          "works": 19
        },
        {
          "name": "Francesco Giorgino",
          "works": 19
        },
        {
          "name": "Elke Heitmann",
          "works": 19
        },
        {
          "name": "Marco Orsini Federici",
          "works": 17
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7155704510",
          "year": 2026,
          "title": "Differences in Perspectives of Weight Management Among People in the US and Canada with Type 2 Diabetes by Body Mass Index",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 0,
          "topics": [
            "Bariatric Surgery and Outcomes",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Obesity and Health Practices"
          ]
        },
        {
          "openalex_id": "W7166049043",
          "year": 2026,
          "title": "EPH226 VALUE SETS FOR AQOL, EQ-5D, HUI, QWB AND SF-6D: A SYSTEMATIC REVIEW OF THEIR AVAILABILITY AND CHARACTERISTICS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Free Radicals and Antioxidants",
            "Chemical and Physical Properties in Aqueous Solutions",
            "Chemistry and Chemical Engineering"
          ]
        },
        {
          "openalex_id": "W7166188896",
          "year": 2026,
          "title": "MSR230 A METHODOLOGICAL REVIEW OF VALUATION STUDIES FOR THE EQ-5D-5L: EVOLVING PRACTICES AND LESSONS FROM THE EQ-5D-3L",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Nuclear Engineering Thermal-Hydraulics",
            "Technology Assessment and Management"
          ]
        },
        {
          "openalex_id": "W4411287785",
          "year": 2025,
          "title": "1160-P: Development of the Pediatric Type 2 Diabetes Impact Measure (P-TIM)",
          "type": "article",
          "venue": "Diabetes",
          "cited_by_count": 0,
          "topics": [
            "Diabetes and associated disorders",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes Management and Research"
          ]
        },
        {
          "openalex_id": "W4414078401",
          "year": 2025,
          "title": "Appetite, eating attitudes, and eating behaviours during treatment with retatrutide in adults with type 2 diabetes: Results of a phase 2 study",
          "type": "article",
          "venue": "Diabetes Obesity and Metabolism",
          "cited_by_count": 2,
          "topics": [
            "Diabetes Treatment and Management",
            "Bariatric Surgery and Outcomes",
            "Eating Disorders and Behaviors"
          ]
        },
        {
          "openalex_id": "W4412760284",
          "year": 2025,
          "title": "Association between patient‐reported eating behaviours and weight change: Secondary analyses of a randomized, double‐blind trial comparing retatrutide and placebo in people with obesity or overweight",
          "type": "article",
          "venue": "Diabetes Obesity and Metabolism",
          "cited_by_count": 2,
          "topics": [
            "Eating Disorders and Behaviors",
            "Obesity, Physical Activity, Diet",
            "Obesity and Health Practices"
          ]
        },
        {
          "openalex_id": "W2134376988",
          "year": 2006,
          "title": "Patient-reported outcomes in a trial of exenatide and insulin glargine for the treatment of type 2 diabetes",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 68,
          "topics": [
            "Diabetes Treatment and Management",
            "Diabetes Management and Education",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W1992074003",
          "year": 2007,
          "title": "A Modeled Economic Evaluation Comparing Atomoxetine with Stimulant Therapy in the Treatment of Children with Attention-Deficit/Hyperactivity Disorder in the United Kingdom",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 34,
          "topics": [
            "Attention Deficit Hyperactivity Disorder",
            "Neuroethics, Human Enhancement, Biomedical Innovations",
            "Bipolar Disorder and Treatment"
          ]
        },
        {
          "openalex_id": "W2075288946",
          "year": 2007,
          "title": "Exenatide versus insulin glargine in patients with type 2 diabetes in the UK: a model of long-term clinical and cost outcomes",
          "type": "article",
          "venue": "Current Medical Research and Opinion",
          "cited_by_count": 56,
          "topics": [
            "Diabetes Treatment and Management",
            "Antiplatelet Therapy and Cardiovascular Diseases",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W2119957760",
          "year": 2007,
          "title": "Health-related quality of life of patients with type 2 diabetes mellitus in primary care in Spain: self-reported and proxy assessment using the EQ-5D",
          "type": "article",
          "venue": "Journal of Medical Economics",
          "cited_by_count": 6,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Parkinson's Disease Mechanisms and Treatments",
            "Clinical practice guidelines implementation"
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
          "openalex_id": "W3033327429",
          "year": 2020,
          "title": "Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 309,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2097132878",
          "year": 2009,
          "title": "Diabetes in Japan: a review of disease burden and approaches to treatment",
          "type": "article",
          "venue": "Diabetes/Metabolism Research and Reviews",
          "cited_by_count": 156,
          "topics": [
            "Diabetes Treatment and Management",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Diabetes Management and Research"
          ]
        },
        {
          "openalex_id": "W2023738827",
          "year": 2015,
          "title": "Multi‐country retrospective observational study of the management and outcomes of patients with Type 2 diabetes during Ramadan in 2010 (<scp>CREED</scp>)",
          "type": "article",
          "venue": "Diabetic Medicine",
          "cited_by_count": 155,
          "topics": [
            "Dietary Effects on Health",
            "Diet and metabolism studies",
            "Berberine and alkaloids research"
          ]
        },
        {
          "openalex_id": "W2076583826",
          "year": 2010,
          "title": "Utilities and disutilities for attributes of injectable treatments for type 2 diabetes",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 140,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Medication Adherence and Compliance",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2002529638",
          "year": 2015,
          "title": "Economic impact of severe and non-severe hypoglycemia in patients with Type 1 and Type 2 diabetes in the United States",
          "type": "article",
          "venue": "Journal of Medical Economics",
          "cited_by_count": 119,
          "topics": [
            "Diabetes Management and Research",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes and associated disorders"
          ]
        },
        {
          "openalex_id": "W2067626357",
          "year": 2007,
          "title": "Utilities and disutilities for type 2 diabetes treatment-related attributes",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 115,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2730168622",
          "year": 2017,
          "title": "Cost of medication adherence and persistence in type 2 diabetes mellitus: a literature review",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 110,
          "topics": [
            "Medication Adherence and Compliance",
            "Diabetes Management and Education",
            "Diabetes Treatment and Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Lan Gao",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1771-RA",
        "title": "Validation of the EQ-HWB-S for measuring the health and wellbeing of informal carers",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "198-RA",
        "title": "Going beyond life expectancy– Examining health inequalities in quality adjusted life expectancy (QALE) in Australia",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2141-RA",
        "title": "Comparative analysis of the EQ-HWB-S, CarerQoL, ASCOT, ICECAP-A, WIX and EQ-5D-5L among informal caregivers",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2363-BT",
        "title": "Comparison of patient and proxy reported global cognition, fatigue, and sleep bolt-ons in stroke",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5043687438",
      "display_name": "Lan Gao",
      "orcid": "0000-0001-9734-1140",
      "reported_affiliation": "Deakin University",
      "works_count": 211,
      "top_topics": [
        {
          "topic": "Acute Ischemic Stroke Management",
          "works": 44
        },
        {
          "topic": "Stroke Rehabilitation and Recovery",
          "works": 32
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 27
        },
        {
          "topic": "Cardiac Health and Mental Health",
          "works": 15
        },
        {
          "topic": "Physical Activity and Health",
          "works": 12
        },
        {
          "topic": "Peripheral Artery Disease Management",
          "works": 11
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 11
        },
        {
          "topic": "Epilepsy research and treatment",
          "works": 9
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 8
        },
        {
          "topic": "Workplace Health and Well-being",
          "works": 8
        },
        {
          "topic": "Cerebrovascular and Carotid Artery Diseases",
          "works": 8
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 8
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Marj Moodie",
          "works": 54
        },
        {
          "name": "Theresa Sevilis",
          "works": 19
        },
        {
          "name": "Shu‐Chuen Li",
          "works": 18
        },
        {
          "name": "Thomas Devlin",
          "works": 14
        },
        {
          "name": "Dieu Nguyen",
          "works": 13
        },
        {
          "name": "Amanda Avila",
          "works": 13
        },
        {
          "name": "Suzanne Robinson",
          "works": 12
        },
        {
          "name": "Peter Lee",
          "works": 12
        },
        {
          "name": "Elise Tan",
          "works": 12
        },
        {
          "name": "Ralph Maddison",
          "works": 10
        },
        {
          "name": "Phuong Nguyen",
          "works": 10
        },
        {
          "name": "Caitlyn Boyd",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7171246309",
          "year": 2026,
          "title": "An interpretable artificial intelligence model for real-time leukemia screening via routine blood tests across multicenter cohorts",
          "type": "article",
          "venue": "npj Digital Medicine",
          "cited_by_count": 0,
          "topics": [
            "Digital Imaging for Blood Diseases",
            "Acute Myeloid Leukemia Research",
            "Clinical Laboratory Practices and Quality Control"
          ]
        },
        {
          "openalex_id": "W7161405201",
          "year": 2026,
          "title": "Cost‐Effectiveness Analysis of Transoral Robotic Surgery Versus Radiotherapy Alone for Early‐Stage <scp>HPV</scp> ‐Associated Oropharynx Squamous Cell Carcinoma in Australia",
          "type": "article",
          "venue": "Journal of Medical Imaging and Radiation Oncology",
          "cited_by_count": 0,
          "topics": [
            "Head and Neck Cancer Studies",
            "Esophageal Cancer Research and Treatment",
            "Advanced Radiotherapy Techniques"
          ]
        },
        {
          "openalex_id": "W7155219205",
          "year": 2026,
          "title": "Cost‐Effectiveness of Donanemab for Early Alzheimer Disease in Australia",
          "type": "article",
          "venue": "The Medical Journal of Australia",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Healthcare Decision-Making and Restraints"
          ]
        },
        {
          "openalex_id": "W7169865971",
          "year": 2026,
          "title": "Estimating the Lifetime Informal Care Costs in Stroke: A Model-Based Analysis",
          "type": "article",
          "venue": "European Journal of Cardiovascular Nursing",
          "cited_by_count": 0,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W7170554998",
          "year": 2026,
          "title": "Estimating the Lifetime Informal Care Costs in Stroke: A Model-Based Analysis",
          "type": "article",
          "venue": "Deakin Research Online (Deakin University)",
          "cited_by_count": 0,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Stroke Rehabilitation and Recovery",
            "Intergenerational Family Dynamics and Caregiving"
          ]
        },
        {
          "openalex_id": "W7164132771",
          "year": 2026,
          "title": "Evaluating Race and Ethnicity Differences in Acute Stroke Treatments in the TeleSpecialists Telestroke RegistryTM (P10-4.017)",
          "type": "article",
          "venue": "Neurology",
          "cited_by_count": 0,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Telemedicine and Telehealth Implementation",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W4249195114",
          "year": 2004,
          "title": "Abstract",
          "type": "conference-abstract",
          "venue": "Canadian Journal of Anesthesia/Journal canadien d anesthésie",
          "cited_by_count": 2,
          "topics": [
            "Hemophilia Treatment and Research",
            "Cardiac and Coronary Surgery Techniques",
            "Hemostasis and retained surgical items"
          ]
        },
        {
          "openalex_id": "W2160978993",
          "year": 2005,
          "title": "Postoperative Cognitive Dysfunction After Cardiac Surgery",
          "type": "article",
          "venue": "CHEST Journal",
          "cited_by_count": 188,
          "topics": [
            "Intensive Care Unit Cognitive Disorders",
            "Cardiac, Anesthesia and Surgical Outcomes",
            "Cardiac and Coronary Surgery Techniques"
          ]
        },
        {
          "openalex_id": "W2382858340",
          "year": 2007,
          "title": "[Study on composing mechanism by effect of disassembled compositions of Yiqi Huoxue decoction on platelet aggregation of health adults].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Traditional Chinese Medicine Analysis",
            "Andrographolide Research and Applications",
            "Lipid metabolism and disorders"
          ]
        },
        {
          "openalex_id": "W2156557282",
          "year": 2012,
          "title": "COST-UTILITY ANALYSIS OF LIRAGLUTIDE VERSUS GLIMEPIRIDE AS ADD-ON TO METFORMIN IN TYPE 2 DIABETES PATIENTS IN CHINA",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 37,
          "topics": [
            "Diabetes Treatment and Management",
            "Metabolism, Diabetes, and Cancer",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W2889374857",
          "year": 2018,
          "title": "Effects and costs of real-time cardiac telerehabilitation: randomised controlled non-inferiority trial",
          "type": "article",
          "venue": "Heart",
          "cited_by_count": 336,
          "topics": [
            "Cardiac Health and Mental Health",
            "Stroke Rehabilitation and Recovery",
            "Cardiovascular and exercise physiology"
          ]
        },
        {
          "openalex_id": "W2507703924",
          "year": 2016,
          "title": "Scaling-up an efficacious school-based physical activity intervention: Study protocol for the ‘Internet-based Professional Learning to help teachers support Activity in Youth’ (iPLAY) cluster randomized controlled trial and scale-up implementation evaluation",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 294,
          "topics": [
            "Children's Physical and Motor Development",
            "Physical Education and Pedagogy",
            "Obesity, Physical Activity, Diet"
          ]
        },
        {
          "openalex_id": "W3087558248",
          "year": 2020,
          "title": "The effectiveness of sedentary behaviour interventions on sitting time and screen time in children and adults: an umbrella review of systematic reviews",
          "type": "review",
          "venue": "International Journal of Behavioral Nutrition and Physical Activity",
          "cited_by_count": 141,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Physical Activity and Health",
            "Ergonomics and Musculoskeletal Disorders"
          ]
        },
        {
          "openalex_id": "W3042328429",
          "year": 2020,
          "title": "Implementation of Telerehabilitation Interventions for the Self-Management of Cardiovascular Disease: Systematic Review",
          "type": "review",
          "venue": "JMIR mhealth and uhealth",
          "cited_by_count": 134,
          "topics": [
            "Cardiac Health and Mental Health",
            "Stroke Rehabilitation and Recovery",
            "Telemedicine and Telehealth Implementation"
          ]
        },
        {
          "openalex_id": "W2104825304",
          "year": 2014,
          "title": "Burden of epilepsy: A prevalence-based cost of illness study of direct, indirect and intangible costs for epilepsy",
          "type": "article",
          "venue": "Epilepsy Research",
          "cited_by_count": 61,
          "topics": [
            "Epilepsy research and treatment",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmacological Effects and Toxicity Studies"
          ]
        },
        {
          "openalex_id": "W2023498059",
          "year": 2012,
          "title": "Statin is a Reasonable Treatment Option for Patients with Polycystic Ovary Syndrome: a Meta-analysis of Randomized Controlled Trials",
          "type": "review",
          "venue": "Experimental and Clinical Endocrinology & Diabetes",
          "cited_by_count": 56,
          "topics": [
            "Ovarian function and disorders",
            "Hormonal and reproductive studies",
            "Healthcare and Venom Research"
          ]
        },
        {
          "openalex_id": "W3092208674",
          "year": 2020,
          "title": "Cost-Effectiveness of Tenecteplase Before Thrombectomy for Ischemic Stroke",
          "type": "article",
          "venue": "Stroke",
          "cited_by_count": 55,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Stroke Rehabilitation and Recovery",
            "Spatial Neglect and Hemispheric Dysfunction"
          ]
        }
      ]
    }
  },
  {
    "name": "Lars Ehlers",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20170401",
        "title": "Deriving EQ-5D-5L preference weights for Denmark - request for budget extension",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5054828864",
      "display_name": "Lars Holger Ehlers",
      "orcid": "0000-0001-6512-5566",
      "reported_affiliation": "Nordic School of Public Health",
      "works_count": 309,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 45
        },
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 19
        },
        {
          "topic": "Education, Healthcare and Sociology Research",
          "works": 19
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 15
        },
        {
          "topic": "Cardiac, Anesthesia and Surgical Outcomes",
          "works": 15
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 13
        },
        {
          "topic": "Telemedicine and Telehealth Implementation",
          "works": 13
        },
        {
          "topic": "Global Health Care Issues",
          "works": 13
        },
        {
          "topic": "Healthcare Quality and Management",
          "works": 12
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 12
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 12
        },
        {
          "topic": "Acute Ischemic Stroke Management",
          "works": 11
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Ole Hejlesen",
          "works": 23
        },
        {
          "name": "Mette Kjølby",
          "works": 20
        },
        {
          "name": "Morten Berg Jensen",
          "works": 17
        },
        {
          "name": "Søren Paaske Johnsen",
          "works": 15
        },
        {
          "name": "Sabrina Storgaard Sørensen",
          "works": 14
        },
        {
          "name": "Kjeld Møller Pedersen",
          "works": 12
        },
        {
          "name": "Lisa Korsbakke Emtekær Hæsum",
          "works": 12
        },
        {
          "name": "Merete Bech",
          "works": 11
        },
        {
          "name": "Martin Bach Jensen",
          "works": 11
        },
        {
          "name": "Claus Løvschall",
          "works": 11
        },
        {
          "name": "Michael Falk Hvidberg",
          "works": 10
        },
        {
          "name": "Karin Dam Petersen",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7150784370",
          "year": 2026,
          "title": "Early health economic assessment of eLi <sub>12</sub> , a new method to estimate 12-h lithium levels when blood sampling deviates from 12 h",
          "type": "article",
          "venue": "Acta Neuropsychiatrica",
          "cited_by_count": 0,
          "topics": [
            "Bipolar Disorder and Treatment",
            "Extraction and Separation Processes",
            "Coordination Chemistry and Organometallics"
          ]
        },
        {
          "openalex_id": "W7165499115",
          "year": 2026,
          "title": "Her er tre simple greb, der kan reducere antallet af patienter, der udvikler nyresvigt og får behov for dialyse",
          "type": "other",
          "venue": "University of Southern Denmark Research Portal (University of Southern Denmark)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4408308807",
          "year": 2025,
          "title": "Bioterroristische Gefahrenlagen – Die Stärkung von Strukturen und Fähigkeiten des ÖGD am Beispiel Hamburg",
          "type": "conference-paper",
          "venue": "Das Gesundheitswesen",
          "cited_by_count": 0,
          "topics": [
            "Bacillus and Francisella bacterial research"
          ]
        },
        {
          "openalex_id": "W4409567804",
          "year": 2025,
          "title": "Cost-Effectiveness of Hospital-at-Home and Fecal Microbiota Transplantation in Treating Older Patients With <i>Clostridioides difficile</i>",
          "type": "article",
          "venue": "Clinical Infectious Diseases",
          "cited_by_count": 1,
          "topics": [
            "Clostridium difficile and Clostridium perfringens research",
            "Gut microbiota and health",
            "Gastrointestinal motility and disorders"
          ]
        },
        {
          "openalex_id": "W4417479795",
          "year": 2025,
          "title": "EE22 A Model-Based Analysis of the Impact on Labor Market Supply From Enhanced Tobacco Control Strategies in Denmark",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Employment and Welfare Studies",
            "Workplace Health and Well-being",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4417480775",
          "year": 2025,
          "title": "EE442 Evaluating the Economic Impact of Worksite Physical Activity Interventions in Denmark: An Employer’s Perspective",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Physical Activity and Health",
            "Workplace Health and Well-being",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W3021774029",
          "year": 1997,
          "title": "Alternative organisationsformer i sygevæsenet: en komparativ efficiensanalyse af private virksomheder og udvalgte sygehusafdelinger i Danmark, Sverige og Holland",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Organizational Learning and Leadership",
            "Complex Systems and Decision Making"
          ]
        },
        {
          "openalex_id": "W2263628237",
          "year": 1997,
          "title": "[A clinic for the study of dementia--110 consecutive patients].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Health, Medicine and Society"
          ]
        },
        {
          "openalex_id": "W2520919147",
          "year": 1999,
          "title": "Internet - Technologie und Historie",
          "type": "article",
          "venue": "",
          "cited_by_count": 6,
          "topics": [
            "Libraries and Information Services",
            "Historical Influence and Diplomacy"
          ]
        },
        {
          "openalex_id": "W4230159032",
          "year": 2000,
          "title": "Ein Vorgehensmodell für Konzeption, Implementierung und Einsatz einer Internet-Präsenz — Erfahrungen aus einem Intranet-Projekt",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Corporate Governance and Management",
            "Digital Innovation in Industries",
            "Business Process Modeling and Analysis"
          ]
        },
        {
          "openalex_id": "W2978392027",
          "year": 2019,
          "title": "Can quality improvement improve the quality of care? A systematic review of reported effects and methodological rigor in plan-do-study-act projects",
          "type": "review",
          "venue": "BMC Health Services Research",
          "cited_by_count": 227,
          "topics": [
            "Health Policy Implementation Science",
            "Primary Care and Health Outcomes",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2157236448",
          "year": 2015,
          "title": "The Health-Related Quality of Life for Patients with Myalgic Encephalomyelitis / Chronic Fatigue Syndrome (ME/CFS)",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 226,
          "topics": [
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Genetic Neurodegenerative Diseases",
            "Psychosomatic Disorders and Their Treatments"
          ]
        },
        {
          "openalex_id": "W3126420006",
          "year": 2021,
          "title": "The Danish EQ-5D-5L Value Set: A Hybrid Model Using cTTO and DCE Data",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 197,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W1983702267",
          "year": 2012,
          "title": "Using preventive home monitoring to reduce hospital admission rates and reduce costs: a case study of telehealth among chronic obstructive pulmonary disease patients",
          "type": "article",
          "venue": "Journal of Telemedicine and Telecare",
          "cited_by_count": 123,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Respiratory Support and Mechanisms",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W3043482046",
          "year": 2020,
          "title": "Rate and impact of duodenoscope contamination: A systematic review and meta-analysis",
          "type": "review",
          "venue": "EClinicalMedicine",
          "cited_by_count": 107,
          "topics": [
            "Medical Device Sterilization and Disinfection",
            "Infection Control in Healthcare",
            "Cardiac pacing and defibrillation studies"
          ]
        },
        {
          "openalex_id": "W3216946134",
          "year": 2021,
          "title": "Danish population health measured by the EQ-5D-5L",
          "type": "article",
          "venue": "Scandinavian Journal of Public Health",
          "cited_by_count": 105,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W2980885831",
          "year": 2019,
          "title": "A systematic review and cost effectiveness analysis of reusable vs. single‐use flexible bronchoscopes",
          "type": "review",
          "venue": "Anaesthesia",
          "cited_by_count": 102,
          "topics": [
            "Medical Device Sterilization and Disinfection",
            "Airway Management and Intubation Techniques",
            "Foreign Body Medical Cases"
          ]
        },
        {
          "openalex_id": "W2027656984",
          "year": 2015,
          "title": "Person-centred care for patients with chronic heart failure – a cost–utility analysis",
          "type": "article",
          "venue": "European Journal of Cardiovascular Nursing",
          "cited_by_count": 91,
          "topics": [
            "Chronic Disease Management Strategies",
            "Heart Failure Treatment and Management",
            "Patient-Provider Communication in Healthcare"
          ]
        }
      ]
    }
  }
]
