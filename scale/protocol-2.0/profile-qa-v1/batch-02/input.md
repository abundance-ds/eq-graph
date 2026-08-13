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
    "name": "Abraham Gebregziabiher",
    "member_affiliation": "1School of Pharmacy, College of Health Science, Mekelle University.",
    "is_member": true,
    "projects": [
      {
        "project_id": "133-RA",
        "title": "Assessment and comparison of the feasibility and measurement properties of the EQ-5D-Y-3L, EQ-5D-Y-5L and EQ-5D-5L self-complete versions in the Tigrinya language",
        "working_group": "Youth"
      },
      {
        "project_id": "1798-RA",
        "title": "Impact of mode of administration on responses and measurement properties of the EQ-5D-Y-3L/-5L and other pediatric preference weight measures: a systematic review",
        "working_group": "Youth"
      },
      {
        "project_id": "20170480",
        "title": "Valuing Health-State: An EQ-5D-5L Value Set for Ethiopians",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180500",
        "title": "Reliability and validity of using EQ-5D-5L among healthy and adolescents with major mental disorders in Ethiopia",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20191010",
        "title": "Psychometric properties, feasibility and usefulness of the extended EQ-5D-Y-5L in children with prevalent disease conditions in Ethiopia",
        "working_group": "Youth"
      },
      {
        "project_id": "2124-RA",
        "title": "Exploring experience and perception of valuation tasks for valuing EQ-5D-Y-5L health states: a qualitative study of adults and adolescents",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "225-RA",
        "title": "Assessing and comparing psychometric properties of both 3L/5L of EQ-5D-Y and adult EQ-5D versions in adolescents with prevalent disease conditions in Ethiopia",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "313-PHD",
        "title": "Measuring and valuing health for children and adolescents in Ethiopia",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "340-RA",
        "title": "Agreement of the Amharic EQ‐5D‐Y-3L and Y-5L self-report (by interview-administration and self-complete) and proxy‐report",
        "working_group": "Youth"
      },
      {
        "project_id": "89-RA",
        "title": "Investigating the aspects of HRQoL covered by pain/discomfort and the added value of the psoriasis bolt-ons (EQ-PSO) among patients suffering from skin diseases (Revised).",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5061701004",
      "display_name": "Abraham Gebregziabiher Welie",
      "orcid": "0000-0003-4661-7287",
      "reported_affiliation": "Mekelle University",
      "works_count": 6,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 3
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 1
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 1
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 1
        },
        {
          "topic": "Diabetes, Cardiovascular Risks, and Lipoproteins",
          "works": 1
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 1
        },
        {
          "topic": "Schizophrenia research and treatment",
          "works": 1
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 1
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 1
        },
        {
          "topic": "Pharmaceutical Quality and Counterfeiting",
          "works": 1
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 1
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Gebremedhin Beedemariam Gebretekle",
          "works": 4
        },
        {
          "name": "Yared Belete Belay",
          "works": 3
        },
        {
          "name": "Elly Stolk",
          "works": 2
        },
        {
          "name": "Clara Mukuria",
          "works": 2
        },
        {
          "name": "Murray Krahn",
          "works": 2
        },
        {
          "name": "Girma Tekle Gebremariam",
          "works": 2
        },
        {
          "name": "Beate Sander",
          "works": 2
        },
        {
          "name": "Terefe Teshome Kassa",
          "works": 2
        },
        {
          "name": "Fantaye Teka Dinkashe",
          "works": 2
        },
        {
          "name": "Fikre Enquoselassie",
          "works": 1
        },
        {
          "name": "Teferi Gedif Fenta",
          "works": 1
        },
        {
          "name": "Selam Biratu",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4404314514",
          "year": 2024,
          "title": "The psychometric properties of the amharic version of EuroQoL five-dimensions-five level among Ethiopian cervical cancer patients",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Cancer survivorship and care",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Endometrial and Cervical Cancer Treatments"
          ]
        },
        {
          "openalex_id": "W4212772886",
          "year": 2022,
          "title": "Health-related quality of life of patients with type 2 diabetes mellitus at a tertiary care hospital in Ethiopia",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 47,
          "topics": [
            "Diabetes Management and Education",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W4206672650",
          "year": 2022,
          "title": "Reliability and validity of using EQ-5D-5L among healthy and adolescents with major mental health disorders in Ethiopia",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 23,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Schizophrenia research and treatment",
            "Mental Health Treatment and Access"
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
        },
        {
          "openalex_id": "W2774126125",
          "year": 2017,
          "title": "Assessment of Knowledge, Attitude and Practice of Pharmacy Professionals Toward Generic Medicines, Northern Ethiopia, Mekelle: A Cross Sectional Study",
          "type": "article",
          "venue": "Journal of Basic and Clinical Pharmacy",
          "cited_by_count": 11,
          "topics": [
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2744018567",
          "year": 2017,
          "title": "Assessment of counseling practice in medicine retail outlets in Mekelle City, Northern Ethiopia",
          "type": "article",
          "venue": "Risk Management and Healthcare Policy",
          "cited_by_count": 8,
          "topics": [
            "Pharmaceutical Quality and Counterfeiting",
            "Pharmaceutical Practices and Patient Outcomes",
            "Antibiotic Use and Resistance"
          ]
        }
      ]
    }
  },
  {
    "name": "Ademola Itiola",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1753-PHD",
        "title": "Exploring response shift in EQ-5D and its implications for healthcare decision making in knee arthroplasty",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5093433205",
      "display_name": "Ademola Itiola",
      "orcid": "",
      "reported_affiliation": "University of Alberta",
      "works_count": 2,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 2
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 2
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 1
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jeffrey Johnson",
          "works": 2
        },
        {
          "name": "Shakib Rahman",
          "works": 2
        },
        {
          "name": "Christopher Smith",
          "works": 2
        },
        {
          "name": "Allison Soprovich",
          "works": 2
        },
        {
          "name": "Lisa Wozniak",
          "works": 2
        },
        {
          "name": "Deborah A. Marshall",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4392286701",
          "year": 2024,
          "title": "Exploring patient perspectives on EQ-5D-5L data visualization within an individualized decision aid for total knee arthroplasty (TKA) in Alberta, Canada",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 5,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4389398334",
          "year": 2023,
          "title": "Exploring Patient Perspectives on EQ-5D-5L Data Visualization within an Individualized Decision Aid for Total Knee Arthroplasty (TKA) in Alberta, Canada",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Patient Satisfaction in Healthcare"
          ]
        }
      ]
    }
  },
  {
    "name": "Agota Szende",
    "member_affiliation": "Covance Health Economics & Outcomes Services",
    "is_member": true,
    "projects": [
      {
        "project_id": "2015470",
        "title": "International Analysis of Income-related Inequity in Self-assessed Health Using the EQ-5D",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20191120",
        "title": "Population norms and inequalities based on EQ-5D-5L general population surveys (POPS 2 Project)",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5002095623",
      "display_name": "Ágota Szende",
      "orcid": "0000-0002-5880-3354",
      "reported_affiliation": "Genesis Research Trust",
      "works_count": 113,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 36
        },
        {
          "topic": "Global Health Care Issues",
          "works": 13
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 9
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 8
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 6
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 5
        },
        {
          "topic": "Acute Myeloid Leukemia Research",
          "works": 5
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 5
        },
        {
          "topic": "Chronic Lymphocytic Leukemia Research",
          "works": 5
        },
        {
          "topic": "Inflammatory Bowel Disease",
          "works": 4
        },
        {
          "topic": "Advanced Breast Cancer Therapies",
          "works": 4
        },
        {
          "topic": "Multiple and Secondary Primary Cancers",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bas Janssen",
          "works": 16
        },
        {
          "name": "Sam Colman",
          "works": 16
        },
        {
          "name": "Caroline Schaefer",
          "works": 13
        },
        {
          "name": "Emilija Veljanoska",
          "works": 9
        },
        {
          "name": "Diego Novick",
          "works": 8
        },
        {
          "name": "Alan F. List",
          "works": 7
        },
        {
          "name": "Sofia Gomes",
          "works": 6
        },
        {
          "name": "Juan Manuel Ramos-Goñi",
          "works": 5
        },
        {
          "name": "Thomas F. Goss",
          "works": 5
        },
        {
          "name": "Barbara Deschler-Baier",
          "works": 4
        },
        {
          "name": "Pierre Fenaux",
          "works": 4
        },
        {
          "name": "Sally Killick",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7126051336",
          "year": 2026,
          "title": "Cost implications of introducing the BIOFIRE FILMARRAY meningitis/encephalitis panel vs. real-time PCR in adult and pediatric populations in the UK",
          "type": "article",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": [
            "Bacterial Infections and Vaccines",
            "Multiple Sclerosis Research Studies",
            "Herpesvirus Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W7126058135",
          "year": 2026,
          "title": "Cost implications of introducing the BIOFIRE FILMARRAY meningitis/encephalitis panel vs. real-time PCR in adult and pediatric populations in the UK",
          "type": "article",
          "venue": "Journal of Medical Economics",
          "cited_by_count": 0,
          "topics": [
            "Bacterial Infections and Vaccines",
            "Antibiotic Use and Resistance",
            "Herpesvirus Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W7126083841",
          "year": 2026,
          "title": "Cost implications of introducing the BIOFIRE FILMARRAY meningitis/encephalitis panel vs. real-time PCR in adult and pediatric populations in the UK",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Bacterial Infections and Vaccines",
            "Multiple Sclerosis Research Studies",
            "Herpesvirus Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W7166186053",
          "year": 2026,
          "title": "MSR11 US ICER ASSESSMENT APPROACHES TO SURVIVAL EXTRAPOLATION: A REVIEW AND CASE STUDY",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Transplantation: Methods and Outcomes",
            "Hematopoietic Stem Cell Transplantation"
          ]
        },
        {
          "openalex_id": "W7166071487",
          "year": 2026,
          "title": "MSR214 A MODULAR ONCOLOGY REFERENCE MODEL FOR EARLY ECONOMIC EVALUATION: A CASE STUDY IN EGFR-MUTATED NSCLC",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Lung Cancer Treatments and Mutations",
            "Gastric Cancer Management and Outcomes"
          ]
        },
        {
          "openalex_id": "W4410232680",
          "year": 2025,
          "title": "Author’s Reply to Perera et al.: A Commentary on “An Early Cost–Utility Model of mRNA-Based Therapies for the Treatment of Methylmalonic and Propionic Acidemia in the United Kingdom”",
          "type": "article",
          "venue": "Clinical Drug Investigation",
          "cited_by_count": 0,
          "topics": [
            "Metabolism and Genetic Disorders",
            "Folate and B Vitamins Research",
            "Diet and metabolism studies"
          ]
        },
        {
          "openalex_id": "W1995469411",
          "year": 1999,
          "title": "TPC1: COST-EFFECTIVENESS ANALYSIS OF BUDESONIDE VERSUS DISODIUM CROMOGLYCATE THERAPY IN CHILDREN WITH MODERATE BRONCHIAL ASTHMA",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Asthma and respiratory diseases"
          ]
        },
        {
          "openalex_id": "W2043944029",
          "year": 2000,
          "title": "AO2: GENERIC AND DISEASE-SPECIFIC HEALTH RELATED QUALITY OF LIFE MEASUREMENTS IN 127 RHEUMATOID ARTHRITIS AND 167 OSTEOARTHRITIS PATIENTS IN HUNGARY",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Systems and Public Health",
            "Infrared Thermography in Medicine",
            "Medical and Biological Ozone Research"
          ]
        },
        {
          "openalex_id": "W2109518591",
          "year": 2000,
          "title": "NR2: QUALITY OF LIFE AFTER SUBARACHNOID HEMORRHAGE IN RELATION TO RISK ESTIMATION BEFORE SURGERY",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Traumatic Brain Injury and Neurovascular Disturbances"
          ]
        },
        {
          "openalex_id": "W2033369280",
          "year": 2000,
          "title": "PMDQ1: GENERAL POPULATION-BASED QUALITY OF LIFE MEASUREMENTS USING THE EQ-5D QUESTIONNAIRE",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Pharmacy and Medical Practices",
            "Mental Health Research Topics",
            "Healthcare Systems and Public Health"
          ]
        },
        {
          "openalex_id": "W2100770509",
          "year": 2013,
          "title": "Self-Reported Population Health: An International Perspective based on EQ-5D",
          "type": "book",
          "venue": "",
          "cited_by_count": 801,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Public Health Policies and Education"
          ]
        },
        {
          "openalex_id": "W1466167365",
          "year": 2007,
          "title": "EQ-5D value sets : inventory, comparative review, and user guide",
          "type": "other",
          "venue": "",
          "cited_by_count": 499,
          "topics": [
            "Product Development and Customization",
            "Manufacturing Process and Optimization"
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
          "openalex_id": "W102833839",
          "year": 2013,
          "title": "Population Norms for the EQ-5D",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 256,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W4253882148",
          "year": 2013,
          "title": "Self-Reported Population Health: An International Perspective Based on EQ-5D",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 196,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2076706228",
          "year": 2005,
          "title": "The inequity of informal payments for health care: The case of Hungary",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 121,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Health Care Issues",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2090432028",
          "year": 2005,
          "title": "Health-Related Quality of Life and Other Patient-Reported Outcomes in the European Centralized Drug Regulatory Process: A Review of Guidance Documents and Performed Authorizations of Medicinal Products 1995 to 2003",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmacovigilance and Adverse Drug Reactions",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W193643119",
          "year": 2003,
          "title": "[Health-related quality of life of the Hungarian population].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 58,
          "topics": []
        }
      ]
    }
  },
  {
    "name": "Akanksha Akanksha",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1799-RA",
        "title": "Assessment of psychometric properties of EQ-HWB and Comparative Analysis with EQ-5D-5L, ASCOT, and QOL-ACC in the Australian context.",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2511-RA",
        "title": "Psychometric comparison of experimental and experimental modified versions of the EQ-HWB-9 in the Netherlands and the USA",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5101596594",
      "display_name": "Akanksha Akanksha",
      "orcid": "",
      "reported_affiliation": "University of Technology Sydney",
      "works_count": 135,
      "top_topics": [
        {
          "topic": "Phytochemicals and Medicinal Plants",
          "works": 10
        },
        {
          "topic": "Genetics and Plant Breeding",
          "works": 6
        },
        {
          "topic": "Natural Antidiabetic Agents Studies",
          "works": 5
        },
        {
          "topic": "Coal and Its By-products",
          "works": 5
        },
        {
          "topic": "Coal Properties and Utilization",
          "works": 5
        },
        {
          "topic": "Hydrocarbon exploration and reservoir analysis",
          "works": 5
        },
        {
          "topic": "Food Science and Nutritional Studies",
          "works": 5
        },
        {
          "topic": "Drug-Induced Hepatotoxicity and Protection",
          "works": 5
        },
        {
          "topic": "Sulfur-Based Synthesis Techniques",
          "works": 4
        },
        {
          "topic": "Medicinal Plants and Neuroprotection",
          "works": 4
        },
        {
          "topic": "Agricultural Practices and Plant Genetics",
          "works": 4
        },
        {
          "topic": "Essential Oils and Antimicrobial Activity",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Rakesh Maurya",
          "works": 8
        },
        {
          "name": "Arvind K. Srivastava",
          "works": 5
        },
        {
          "name": "Deepak Singh Panwar",
          "works": 5
        },
        {
          "name": "Rajveer Sason",
          "works": 5
        },
        {
          "name": "Ajay Singh",
          "works": 4
        },
        {
          "name": "Ram Chandra Chaurasia",
          "works": 4
        },
        {
          "name": "Munna Lal Prajapati",
          "works": 4
        },
        {
          "name": "Debabrata Maiti",
          "works": 3
        },
        {
          "name": "Amar Singh",
          "works": 3
        },
        {
          "name": "Atul Kumar",
          "works": 3
        },
        {
          "name": "Himanshu Chaudhary",
          "works": 3
        },
        {
          "name": "Ayushi Srivastava",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167921318",
          "year": 2026,
          "title": "Do wording and response option modifications to the EQ-HWB-9 affect measurement performance? Evidence from the Netherlands and the USA",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Digital Mental Health Interventions",
            "Psychometric Methodologies and Testing",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W4406212652",
          "year": 2025,
          "title": "A REVIEW ARTICLE ON TOXICOLOGY IN AYURVEDA",
          "type": "article",
          "venue": "EPRA International Journal of Research & Development (IJRD)",
          "cited_by_count": 0,
          "topics": [
            "Plant-based Medicinal Research",
            "Drug-Induced Hepatotoxicity and Protection",
            "Phytochemicals and Medicinal Plants"
          ]
        },
        {
          "openalex_id": "W4417080197",
          "year": 2025,
          "title": "A Review of Tundikeri with Special Reference to Tonsillitis: An Ayurvedic and Modern Perspective",
          "type": "article",
          "venue": "International Journal For Multidisciplinary Research",
          "cited_by_count": 0,
          "topics": [
            "Medical Case Reports and Studies",
            "Therapeutic Uses of Natural Elements",
            "Complementary and Alternative Medicine Studies"
          ]
        },
        {
          "openalex_id": "W4408782453",
          "year": 2025,
          "title": "A framework for extending the health-related quality adjusted life year by combining instruments",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W4412405434",
          "year": 2025,
          "title": "Analysis and Design of Reliable Node Routing Mechanism for MANET using Fuzzy Logic",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Mobile Ad Hoc Networks",
            "Vehicular Ad Hoc Networks (VANETs)",
            "Security in Wireless Sensor Networks"
          ]
        },
        {
          "openalex_id": "W4407141965",
          "year": 2025,
          "title": "Antimicrobial Efficacy of Prepared Herbal Denture Cleansers and Their Impact on Physical Properties of Denture Base Material: An Invitro Study",
          "type": "article",
          "venue": "European Journal of Medicinal Plants",
          "cited_by_count": 0,
          "topics": [
            "Pharmacology and Nanomedicine Research",
            "Medicinal Plants and Neuroprotection",
            "Essential Oils and Antimicrobial Activity"
          ]
        },
        {
          "openalex_id": "W2951488966",
          "year": 2007,
          "title": "Amino acid catalyzed thio-Michael addition reactions",
          "type": "article",
          "venue": "Tetrahedron",
          "cited_by_count": 48,
          "topics": [
            "Sulfur-Based Synthesis Techniques",
            "Chemical Synthesis and Reactions",
            "Synthesis of heterocyclic compounds"
          ]
        },
        {
          "openalex_id": "W1968422972",
          "year": 2007,
          "title": "Anti-stress Constituents of Evolvulus alsinoides: An Ayurvedic Crude Drug",
          "type": "article",
          "venue": "Chemical and Pharmaceutical Bulletin",
          "cited_by_count": 54,
          "topics": [
            "Medicinal Plants and Neuroprotection",
            "Phytochemicals and Medicinal Plants",
            "Pharmacological Effects of Natural Compounds"
          ]
        },
        {
          "openalex_id": "W2949298580",
          "year": 2007,
          "title": "HbA/H2O2: an efficient biomimetic catalytic system for the oxidation of sulfides to sulfoxides",
          "type": "article",
          "venue": "Tetrahedron Letters",
          "cited_by_count": 23,
          "topics": [
            "Chemical Synthesis and Reactions",
            "Sulfur-Based Synthesis Techniques",
            "Synthesis and Catalytic Reactions"
          ]
        },
        {
          "openalex_id": "W2069364931",
          "year": 2007,
          "title": "Mass transport correlation for CO2 absorption in aqueous monoethanolamine in a continuous film contactor",
          "type": "article",
          "venue": "Chemical Engineering and Processing - Process Intensification",
          "cited_by_count": 28,
          "topics": [
            "Carbon Dioxide Capture Technologies",
            "Phase Equilibria and Thermodynamics",
            "Adsorption and Cooling Systems"
          ]
        },
        {
          "openalex_id": "W2233456439",
          "year": 2016,
          "title": "UAVs as remote sensing platform in glaciology: Present applications and future prospects",
          "type": "article",
          "venue": "Remote Sensing of Environment",
          "cited_by_count": 381,
          "topics": [
            "Cryospheric studies and observations",
            "UAV Applications and Optimization",
            "Species Distribution and Climate Change"
          ]
        },
        {
          "openalex_id": "W2119158627",
          "year": 2012,
          "title": "Nickel-catalyzed decyanation of inert carbon–cyano bonds",
          "type": "article",
          "venue": "Chemical Communications",
          "cited_by_count": 68,
          "topics": [
            "Sulfur-Based Synthesis Techniques",
            "Catalytic C–H Functionalization Methods",
            "Catalytic Cross-Coupling Reactions"
          ]
        },
        {
          "openalex_id": "W2162171771",
          "year": 2012,
          "title": "Microwave-assisted palladium mediated decarbonylation reaction: synthesis of eulatachromene",
          "type": "article",
          "venue": "Green Chemistry",
          "cited_by_count": 66,
          "topics": [
            "Catalytic Cross-Coupling Reactions",
            "Microwave-Assisted Synthesis and Applications",
            "Multicomponent Synthesis of Heterocycles"
          ]
        },
        {
          "openalex_id": "W2123327337",
          "year": 2009,
          "title": "Anti-hyperglycaemic, lipid lowering and anti-oxidant properties of (6)-gingerol in db/db mice",
          "type": "article",
          "venue": "International Journal of Medicine and Medical Sciences",
          "cited_by_count": 59,
          "topics": [
            "Ginger and Zingiberaceae research",
            "Mangiferin and Mango Extracts",
            "Peroxisome Proliferator-Activated Receptors"
          ]
        },
        {
          "openalex_id": "W4239450470",
          "year": 2014,
          "title": "Synthesis of Bis(heteroaryl) Ketones by Removal of Benzylic CHR and CO Groups",
          "type": "article",
          "venue": "Angewandte Chemie",
          "cited_by_count": 40,
          "topics": [
            "Catalytic C–H Functionalization Methods",
            "Synthesis and Catalytic Reactions",
            "Cyclopropane Reaction Mechanisms"
          ]
        },
        {
          "openalex_id": "W1984775340",
          "year": 2011,
          "title": "Design and synthesis of 1,3-biarylsulfanyl derivatives as new anti-breast cancer agents",
          "type": "article",
          "venue": "Bioorganic & Medicinal Chemistry",
          "cited_by_count": 36,
          "topics": [
            "Estrogen and related hormone effects",
            "Inflammatory mediators and NSAID effects",
            "Synthesis and biological activity"
          ]
        }
      ]
    }
  },
  {
    "name": "Aki Tsuchiya",
    "member_affiliation": "University of Sheffield",
    "is_member": true,
    "projects": [
      {
        "project_id": "2013170",
        "title": "Further Exploration into using DCE for EQ5D-5L Valuations (FEDEV)",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015180",
        "title": "Exploring non-iterative TTO (ENITTO)",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190840",
        "title": "Aversion to inequalities in health by EQ-5D domain",
        "working_group": "Others"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5015417862",
      "display_name": "Aki Tsuchiya",
      "orcid": "0000-0003-4245-5399",
      "reported_affiliation": "University of Sheffield",
      "works_count": 272,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 183
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 85
        },
        {
          "topic": "Global Health Care Issues",
          "works": 76
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 41
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 23
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 20
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 9
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 8
        },
        {
          "topic": "Income, Poverty, and Inequality",
          "works": 7
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 7
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 6
        },
        {
          "topic": "Employment and Welfare Studies",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "John Brazier",
          "works": 118
        },
        {
          "name": "Donna Rowen",
          "works": 66
        },
        {
          "name": "Brendan Mulhern",
          "works": 48
        },
        {
          "name": "Paul Dolan",
          "works": 42
        },
        {
          "name": "Louise Longworth",
          "works": 40
        },
        {
          "name": "Nancy Devlin",
          "works": 35
        },
        {
          "name": "Nick Bansback",
          "works": 31
        },
        {
          "name": "Yaling Yang",
          "works": 29
        },
        {
          "name": "Ken Buckingham",
          "works": 29
        },
        {
          "name": "Tracey Young",
          "works": 27
        },
        {
          "name": "Clara Mukuria",
          "works": 25
        },
        {
          "name": "Arne Risa Hole",
          "works": 25
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7148826297",
          "year": 2026,
          "title": "A Systematic Review of Elicitation Methods for Distributional Preferences in Healthcare Regarding the Concentration and Dispersion of Health Benefits",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Systems and Reforms",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W7134232681",
          "year": 2026,
          "title": "Eliciting Public Preferences Across Health and Wellbeing Dimensions: An Equivalent Income Value Set for SIPHER-7, 2020-2021",
          "type": "other",
          "venue": "VocBench (University of Rome Tor Vergata)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7132837468",
          "year": 2026,
          "title": "Evaluating the Validity of the EQ Health and Wellbeing (EQ-HWB-9) in a Large United Kingdom General Population Sample",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cardiac Imaging and Diagnostics",
            "Liver Disease Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W7131384634",
          "year": 2026,
          "title": "Why Object to Inequalities in Health and Well-Being? A Mixed-Methods Exploration of Inequality Aversion With Members of the General Public",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Income, Poverty, and Inequality"
          ]
        },
        {
          "openalex_id": "W4414983851",
          "year": 2025,
          "title": "A Large Scale Population Survey of Health and Wellbeing to Allow Comparisons Between Outcome Measures: the SIPHER-HWMIC Dataset",
          "type": "article",
          "venue": "Social Indicators Research",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4407053703",
          "year": 2025,
          "title": "Corrigendum to ‘Does the UK-public's aversion to inequalities in health differ by group-labelling and health-gain type? A choice-experiment’ [Soc. Sci. Med. Volume 269, January 2021, 113573]",
          "type": "erratum",
          "venue": "Social Science & Medicine",
          "cited_by_count": 0,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Global Health Care Issues",
            "Healthcare Systems and Challenges"
          ]
        },
        {
          "openalex_id": "W2417707054",
          "year": 1992,
          "title": "[Suppression of breast cancer cells by cardiac glycosides].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 3,
          "topics": [
            "Glycosylation and Glycoproteins Research",
            "ATP Synthase and ATPases Research",
            "Coenzyme Q10 studies and effects"
          ]
        },
        {
          "openalex_id": "W7146132011",
          "year": 1994,
          "title": "医療資源の配分の倫理 (<研究報告> 医療の倫理学)",
          "type": "article",
          "venue": "Institutional Repositories DataBase (IRDB)",
          "cited_by_count": 0,
          "topics": [
            "Military Technology and Strategies",
            "Legal and Regulatory Analysis",
            "Linguistic, Cultural, and Literary Studies"
          ]
        },
        {
          "openalex_id": "W3024503005",
          "year": 1996,
          "title": "The Value of Health at Different Ages",
          "type": "article",
          "venue": "Iryo To Shakai",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2321357659",
          "year": 1998,
          "title": "A Validity Study of the Japanese EuroQol Instrument",
          "type": "article",
          "venue": "Iryo To Shakai",
          "cited_by_count": 6,
          "topics": [
            "Global Health Care Issues"
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
        },
        {
          "openalex_id": "W2110682994",
          "year": 2004,
          "title": "A comparison of the EQ‐5D and SF‐6D across seven patient groups",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 806,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2153141951",
          "year": 2002,
          "title": "Estimating an EQ‐5D population value set: the case of Japan",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 585,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2087604552",
          "year": 2009,
          "title": "A review of studies mapping (or cross walking) non-preference based measures of health to generic preference-based measures",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 533,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare cost, quality, practices"
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
          "openalex_id": "W3145434052",
          "year": 2007,
          "title": "Measuring and Valuing Health Benefits for Economic Evaluation",
          "type": "article",
          "venue": "OUP Catalogue",
          "cited_by_count": 439,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2038273794",
          "year": 2004,
          "title": "QALY maximisation and people's preferences: a methodological review of the literature",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 430,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
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
        }
      ]
    }
  }
]
