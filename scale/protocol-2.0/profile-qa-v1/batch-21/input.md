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
    "name": "Ilan Koppen",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1468-RA",
        "title": "Exploring the use of the EQ-5D-Y as an outcome measure in pediatric gastroenterology, a pilot study",
        "working_group": "Descriptive Systems, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5031557006",
      "display_name": "Ilan J.N. Koppen",
      "orcid": "0000-0002-1856-0968",
      "reported_affiliation": "Emma Kinderziekenhuis",
      "works_count": 98,
      "top_topics": [
        {
          "topic": "Gastrointestinal motility and disorders",
          "works": 69
        },
        {
          "topic": "Congenital gastrointestinal and neural anomalies",
          "works": 47
        },
        {
          "topic": "Infant Health and Development",
          "works": 24
        },
        {
          "topic": "Pelvic floor disorders treatments",
          "works": 17
        },
        {
          "topic": "Intestinal Malrotation and Obstruction Disorders",
          "works": 12
        },
        {
          "topic": "Gastroesophageal reflux and treatments",
          "works": 9
        },
        {
          "topic": "Child Nutrition and Feeding Issues",
          "works": 5
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 4
        },
        {
          "topic": "Appendicitis Diagnosis and Management",
          "works": 4
        },
        {
          "topic": "Diet and metabolism studies",
          "works": 3
        },
        {
          "topic": "Celiac Disease Research and Management",
          "works": 3
        },
        {
          "topic": "Neonatal skin health care",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Marc A. Benninga",
          "works": 78
        },
        {
          "name": "Desale Yacob",
          "works": 25
        },
        {
          "name": "Peter L. Lu",
          "works": 21
        },
        {
          "name": "Miguel Saps",
          "works": 19
        },
        {
          "name": "Mana H. Vriesman",
          "works": 15
        },
        {
          "name": "Desiree F. Baaleman",
          "works": 14
        },
        {
          "name": "Merit M. Tabbers",
          "works": 11
        },
        {
          "name": "Marc A. Levitt",
          "works": 8
        },
        {
          "name": "Richard J. Wood",
          "works": 8
        },
        {
          "name": "Carlos Alberto Velasco Benítez",
          "works": 7
        },
        {
          "name": "Katherine J. Deans",
          "works": 7
        },
        {
          "name": "Peter C. Minneci",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4413411267",
          "year": 2025,
          "title": "Bowel habits in preterm infants: Observations from the first 2 weeks of life",
          "type": "article",
          "venue": "Journal of Pediatric Gastroenterology and Nutrition",
          "cited_by_count": 0,
          "topics": [
            "Infant Nutrition and Health",
            "Gastrointestinal motility and disorders",
            "Infant Health and Development"
          ]
        },
        {
          "openalex_id": "W4413027399",
          "year": 2025,
          "title": "Colon Length in Children, Normal Values Based on Magnetic Resonance Imaging",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Congenital gastrointestinal and neural anomalies",
            "Intestinal Malrotation and Obstruction Disorders"
          ]
        },
        {
          "openalex_id": "W4417416639",
          "year": 2025,
          "title": "Long-term gastrointestinal sequelae in patients who underwent surgery for congenital duodenal obstruction",
          "type": "article",
          "venue": "Pediatric Surgery International",
          "cited_by_count": 0,
          "topics": [
            "Intestinal Malrotation and Obstruction Disorders",
            "Esophageal and GI Pathology",
            "Intestinal and Peritoneal Adhesions"
          ]
        },
        {
          "openalex_id": "W4406204608",
          "year": 2025,
          "title": "Outcomes and Complications of Chait Trapdoor Cecostomy in Pediatric Patients with Therapy-Resistant Constipation and Fecal Incontinence: A 14-Year Retrospective Study",
          "type": "article",
          "venue": "European Journal of Pediatric Surgery",
          "cited_by_count": 1,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Congenital gastrointestinal and neural anomalies",
            "Pelvic floor disorders treatments"
          ]
        },
        {
          "openalex_id": "W4411968358",
          "year": 2025,
          "title": "Pediatric Constipation",
          "type": "article",
          "venue": "Gastroenterology Clinics of North America",
          "cited_by_count": 0,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Congenital gastrointestinal and neural anomalies",
            "Gastroesophageal reflux and treatments"
          ]
        },
        {
          "openalex_id": "W4407892134",
          "year": 2025,
          "title": "Pharmacological treatment for children with constipation: present and future",
          "type": "editorial",
          "venue": "Expert Opinion on Pharmacotherapy",
          "cited_by_count": 3,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Congenital gastrointestinal and neural anomalies",
            "Infant Health and Development"
          ]
        },
        {
          "openalex_id": "W2116330166",
          "year": 2009,
          "title": "Folate related gene polymorphisms and susceptibility to develop childhood acute lymphoblastic leukaemia",
          "type": "article",
          "venue": "British Journal of Haematology",
          "cited_by_count": 82,
          "topics": [
            "Acute Lymphoblastic Leukemia research",
            "Childhood Cancer Survivors' Quality of Life",
            "Folate and B Vitamins Research"
          ]
        },
        {
          "openalex_id": "W1834620239",
          "year": 2010,
          "title": "Acute lymphoblastic leukaemia in children – is there a role for MTHFR? – response to Lightfoot <i>et al</i>",
          "type": "article",
          "venue": "British Journal of Haematology",
          "cited_by_count": 0,
          "topics": [
            "Folate and B Vitamins Research",
            "Acute Lymphoblastic Leukemia research",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W2779968684",
          "year": 2014,
          "title": "Liesbreuken bij kinderen: goed kijken, snel handelen.",
          "type": "article",
          "venue": "Data Archiving and Networked Services (DANS)",
          "cited_by_count": 0,
          "topics": [
            "Hernia repair and management",
            "Appendicitis Diagnosis and Management",
            "Pelvic and Acetabular Injuries"
          ]
        },
        {
          "openalex_id": "W2417954006",
          "year": 2014,
          "title": "[Inguinal hernia in children: examine thoroughly, treat rapidly].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Hernia repair and management",
            "Appendicitis Diagnosis and Management"
          ]
        },
        {
          "openalex_id": "W2987715292",
          "year": 2019,
          "title": "Management of functional constipation in children and adults",
          "type": "article",
          "venue": "Nature Reviews Gastroenterology & Hepatology",
          "cited_by_count": 463,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Congenital gastrointestinal and neural anomalies",
            "Pelvic floor disorders treatments"
          ]
        },
        {
          "openalex_id": "W2604393173",
          "year": 2017,
          "title": "The New Rome IV Criteria for Functional Gastrointestinal Disorders in Infants and Toddlers",
          "type": "article",
          "venue": "Pediatric Gastroenterology Hepatology & Nutrition",
          "cited_by_count": 355,
          "topics": [
            "Infant Health and Development",
            "Gastrointestinal motility and disorders",
            "Respiratory and Cough-Related Research"
          ]
        },
        {
          "openalex_id": "W2797285236",
          "year": 2018,
          "title": "Prevalence of Functional Defecation Disorders in Children: A Systematic Review and Meta-Analysis",
          "type": "review",
          "venue": "The Journal of Pediatrics",
          "cited_by_count": 347,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Pelvic floor disorders treatments",
            "Congenital gastrointestinal and neural anomalies"
          ]
        },
        {
          "openalex_id": "W1902828807",
          "year": 2015,
          "title": "Management of Functional Constipation in Children: Therapy in Practice",
          "type": "article",
          "venue": "Pediatric Drugs",
          "cited_by_count": 202,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Diet and metabolism studies",
            "Congenital gastrointestinal and neural anomalies"
          ]
        },
        {
          "openalex_id": "W2579522668",
          "year": 2017,
          "title": "The pediatric Rome IV criteria: what’s new?",
          "type": "article",
          "venue": "Expert Review of Gastroenterology & Hepatology",
          "cited_by_count": 177,
          "topics": [
            "Infant Health and Development",
            "Gastrointestinal motility and disorders",
            "Gastroesophageal reflux and treatments"
          ]
        },
        {
          "openalex_id": "W2529047104",
          "year": 2016,
          "title": "A Population-Based Study on the Epidemiology of Functional Gastrointestinal Disorders in Young Children",
          "type": "article",
          "venue": "The Journal of Pediatrics",
          "cited_by_count": 152,
          "topics": [
            "Infant Health and Development",
            "Gastrointestinal motility and disorders",
            "Digestive system and related health"
          ]
        },
        {
          "openalex_id": "W2966494958",
          "year": 2019,
          "title": "Quality of Life in Children with Functional Constipation: A Systematic Review and Meta-Analysis",
          "type": "review",
          "venue": "The Journal of Pediatrics",
          "cited_by_count": 147,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Congenital gastrointestinal and neural anomalies",
            "Celiac Disease Research and Management"
          ]
        },
        {
          "openalex_id": "W2743849824",
          "year": 2017,
          "title": "Role of Polyethylene Glycol in the Treatment of Functional Constipation in Children",
          "type": "article",
          "venue": "Journal of Pediatric Gastroenterology and Nutrition",
          "cited_by_count": 104,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Gastroesophageal reflux and treatments",
            "Helicobacter pylori-related gastroenterology studies"
          ]
        }
      ]
    }
  },
  {
    "name": "Ilias Goranitis",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "454-RA",
        "title": "Psychometric assessment of EQ-5D-5L, EQ-HWB and EQ-5D-Y-5L in rare genetic diseases: a mixed methods approach",
        "working_group": "Descriptive Systems, Youth, EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5023451391",
      "display_name": "Ilias Goranitis",
      "orcid": "0000-0001-7946-8324",
      "reported_affiliation": "The University of Melbourne",
      "works_count": 153,
      "top_topics": [
        {
          "topic": "Genomics and Rare Diseases",
          "works": 60
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 45
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 35
        },
        {
          "topic": "Prenatal Screening and Diagnostics",
          "works": 10
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 9
        },
        {
          "topic": "Pelvic floor disorders treatments",
          "works": 9
        },
        {
          "topic": "Urinary Bladder and Prostate Research",
          "works": 9
        },
        {
          "topic": "Cancer Genomics and Diagnostics",
          "works": 9
        },
        {
          "topic": "Metabolism and Genetic Disorders",
          "works": 8
        },
        {
          "topic": "Ectopic Pregnancy Diagnosis and Management",
          "works": 6
        },
        {
          "topic": "Reproductive System and Pregnancy",
          "works": 6
        },
        {
          "topic": "Ethics in Clinical Research",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Zornitza Stark",
          "works": 46
        },
        {
          "name": "Stephanie Best",
          "works": 41
        },
        {
          "name": "Lee Middleton",
          "works": 28
        },
        {
          "name": "Tracy Roberts",
          "works": 27
        },
        {
          "name": "Arri Coomarasamy",
          "works": 26
        },
        {
          "name": "Jane Daniels",
          "works": 25
        },
        {
          "name": "Sebastian Lunke",
          "works": 22
        },
        {
          "name": "John Christodoulou",
          "works": 21
        },
        {
          "name": "Clara Gaff",
          "works": 20
        },
        {
          "name": "Pallavi Latthe",
          "works": 17
        },
        {
          "name": "Suneetha Rachaneni",
          "works": 16
        },
        {
          "name": "Shanteela McCooty",
          "works": 16
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166319752",
          "year": 2026,
          "title": "Australian parents’ perspectives on extended genomic screening: what information to return and when?",
          "type": "article",
          "venue": "European Journal of Human Genetics",
          "cited_by_count": 0,
          "topics": [
            "Genomics and Rare Diseases",
            "BRCA gene mutations in cancer",
            "Prenatal Screening and Diagnostics"
          ]
        },
        {
          "openalex_id": "W7169795084",
          "year": 2026,
          "title": "Chat with Ilias Goranitis and Jemimah Ride, Co-authors of the DIRECT checklist",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7169795237",
          "year": 2026,
          "title": "Chat with Ilias Goranitis and Jemimah Ride, Co-authors of the DIRECT checklist",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7169815569",
          "year": 2026,
          "title": "Chat with Ilias Goranitis and Jemimah Ride, Co-authors of the DIRECT checklist",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7169853500",
          "year": 2026,
          "title": "Chat with Ilias Goranitis and Jemimah Ride, Co-authors of the DIRECT checklist",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7124132998",
          "year": 2026,
          "title": "Content validity, face validity and comprehensiveness of generic quality-of-life measures in adults and children with rare genetic conditions and their carers: a think aloud qualitative study",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Genomics and Rare Diseases",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W2024558179",
          "year": 2013,
          "title": "An investigation into the construct validity of the Carer Experience Scale (CES)",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 50,
          "topics": [
            "Family Caregiving in Mental Illness",
            "Intergenerational Family Dynamics and Caregiving",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W108718528",
          "year": 2013,
          "title": "Η επίδραση του θεσμικού, πολιτικού και διοικητικού περιβάλλοντος στη μεταρρύθμιση του τομέα της υγείας στην Ελλάδα, 1950-2005",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2053191341",
          "year": 2014,
          "title": "Health policy making under information constraints: An evaluation of the policy responses to the economic crisis in Greece",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 28,
          "topics": [
            "Employment and Welfare Studies",
            "Global Health Care Issues",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2599120744",
          "year": 2015,
          "title": "Cost-effectiveness of zoledronic acid and strontium-89 as bone protecting treatments in addition to chemotherapy in patients with metastatic castrate-refractory prostate cancer. (ISRCTN 12808747) TRAPEZE.",
          "type": "conference-abstract",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 2,
          "topics": [
            "Prostate Cancer Treatment and Research",
            "Bone health and treatments",
            "Radiopharmaceutical Chemistry and Applications"
          ]
        },
        {
          "openalex_id": "W2944460039",
          "year": 2019,
          "title": "A Randomized Trial of Progesterone in Women with Bleeding in Early Pregnancy",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 192,
          "topics": [
            "Ectopic Pregnancy Diagnosis and Management",
            "Maternal and fetal healthcare",
            "Reproductive System and Pregnancy"
          ]
        },
        {
          "openalex_id": "W2108556356",
          "year": 2015,
          "title": "Health care financing and the sustainability of health systems",
          "type": "article",
          "venue": "International Journal for Equity in Health",
          "cited_by_count": 120,
          "topics": [
            "Global Health Care Issues",
            "Healthcare Policy and Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4402166627",
          "year": 2024,
          "title": "A Reporting Checklist for Discrete Choice Experiments in Health: The DIRECT Checklist",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 103,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2285201826",
          "year": 2016,
          "title": "Clinical Outcomes and Survival Following Treatment of Metastatic Castrate-Refractory Prostate Cancer With Docetaxel Alone or With Strontium-89, Zoledronic Acid, or Both",
          "type": "article",
          "venue": "JAMA Oncology",
          "cited_by_count": 88,
          "topics": [
            "Prostate Cancer Treatment and Research",
            "Bone health and treatments",
            "Prostate Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4322762719",
          "year": 2023,
          "title": "Australian Genomics: Outcomes of a 5-year national program to accelerate the integration of genomics in healthcare",
          "type": "article",
          "venue": "The American Journal of Human Genetics",
          "cited_by_count": 74,
          "topics": [
            "Genomics and Rare Diseases",
            "BRCA gene mutations in cancer",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2951799143",
          "year": 2019,
          "title": "A cost-effectiveness model of genetic testing and periodical clinical screening for the evaluation of families with dilated cardiomyopathy",
          "type": "article",
          "venue": "Genetics in Medicine",
          "cited_by_count": 63,
          "topics": [
            "Cardiomyopathy and Myosin Studies",
            "Cardiac electrophysiology and arrhythmias",
            "Cardiovascular Effects of Exercise"
          ]
        },
        {
          "openalex_id": "W2957038058",
          "year": 2019,
          "title": "A head-to-head evaluation of the diagnostic efficacy and costs of trio versus singleton exome sequencing analysis",
          "type": "article",
          "venue": "European Journal of Human Genetics",
          "cited_by_count": 61,
          "topics": [
            "Genomics and Rare Diseases",
            "Genomic variations and chromosomal abnormalities",
            "Genetic factors in colorectal cancer"
          ]
        },
        {
          "openalex_id": "W3023104365",
          "year": 2020,
          "title": "The personal utility and uptake of genomic sequencing in pediatric and adult conditions: eliciting societal preferences with three discrete choice experiments",
          "type": "article",
          "venue": "Genetics in Medicine",
          "cited_by_count": 58,
          "topics": [
            "Genomics and Rare Diseases",
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        }
      ]
    }
  },
  {
    "name": "Ines Buchholz",
    "member_affiliation": "None",
    "is_member": true,
    "projects": [
      {
        "project_id": "1785-RA",
        "title": "Testing the skin irritation, self-confidence, social relationships, social participation and social connectedness bolt-on items for the EQ-5D-5L in German patients with chronic skin diseases associated with shame",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2016170",
        "title": "A systematic review of the measurement properties of EQ-5D-5L",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5043257626",
      "display_name": "Ines Buchholz",
      "orcid": "0000-0001-9729-6992",
      "reported_affiliation": "Universität Hamburg",
      "works_count": 41,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Health and Medical Studies",
          "works": 8
        },
        {
          "topic": "Medical Practices and Rehabilitation",
          "works": 6
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 4
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 4
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 3
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 3
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 3
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 3
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 3
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 2
        },
        {
          "topic": "Psoriasis: Treatment and Pathogenesis",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Thomas Kohlmann",
          "works": 21
        },
        {
          "name": "You‐Shan Feng",
          "works": 9
        },
        {
          "name": "Ralf Ohlinger",
          "works": 6
        },
        {
          "name": "Stefan Paepke",
          "works": 6
        },
        {
          "name": "Jens‐Uwe Blohmer",
          "works": 6
        },
        {
          "name": "Susanne Grunwald",
          "works": 6
        },
        {
          "name": "Oumar Camara",
          "works": 6
        },
        {
          "name": "U. Deichert",
          "works": 6
        },
        {
          "name": "Uwe Peisker",
          "works": 6
        },
        {
          "name": "Kirsten Utpatel",
          "works": 6
        },
        {
          "name": "Marek Zygmunt",
          "works": 6
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167921683",
          "year": 2026,
          "title": "Originalbeiträge (Originals). Burnout and Personality Structure: A Comparison of Medical, Psychology and Teaching and Other Students / Burnout und Persönlichkeitsstruktur: Ein Vergleich von Medizin-, Psychologie-, Lehramt- und anderen Studierenden",
          "type": "article",
          "venue": "Zeitschrift für psychosomatische Medizin und Psychotherapie",
          "cited_by_count": 0,
          "topics": [
            "Healthcare professionals’ stress and burnout",
            "Medical Education and Admissions",
            "Innovations in Medical Education"
          ]
        },
        {
          "openalex_id": "W7147392611",
          "year": 2026,
          "title": "Psychometric validation of a cognition and social participation bolt-on for the EQ-5D-5L in SARS-CoV-2 infected German healthcare workers",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and Mental Health",
            "Long-Term Effects of COVID-19",
            "Human-Automation Interaction and Safety"
          ]
        },
        {
          "openalex_id": "W4410508995",
          "year": 2025,
          "title": "Determinants of Quality of Life in Patients with Atopic Dermatitis and Psoriasis: A Multivariate Approach",
          "type": "article",
          "venue": "Acta Dermato Venereologica",
          "cited_by_count": 9,
          "topics": [
            "Dermatology and Skin Diseases",
            "Allergic Rhinitis and Sensitization",
            "Psoriasis: Treatment and Pathogenesis"
          ]
        },
        {
          "openalex_id": "W4415743630",
          "year": 2025,
          "title": "Psychometric Performance of Skin, Self-Confidence, and Social Health-Related EQ-5D-5L Bolt-Ons in Patients With Atopic Dermatitis and Psoriasis in Germany",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 4,
          "topics": [
            "Dermatology and Skin Diseases",
            "Contact Dermatitis and Allergies",
            "Psoriasis: Treatment and Pathogenesis"
          ]
        },
        {
          "openalex_id": "W4319078371",
          "year": 2023,
          "title": "Assessment of return to play after an acute shoulder injury: protocol for an explorative prospective observational German multicentre study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 5,
          "topics": [
            "Shoulder Injury and Treatment",
            "Sports injuries and prevention",
            "Traumatic Brain Injury Research"
          ]
        },
        {
          "openalex_id": "W4388405428",
          "year": 2023,
          "title": "Der Zusammenhang von Persönlichkeitsstruktur, Burnout und Prokrastination bei Psychologie- und Medizinstudierenden unter Einbeziehung von sozialer Unterstützung und Entscheidungsspielraum im Studium",
          "type": "article",
          "venue": "PPmP - Psychotherapie · Psychosomatik · Medizinische Psychologie",
          "cited_by_count": 3,
          "topics": [
            "Perfectionism, Procrastination, Anxiety Studies",
            "Healthcare professionals’ stress and burnout",
            "Medical Education and Admissions"
          ]
        },
        {
          "openalex_id": "W2419444757",
          "year": 1991,
          "title": "[Oral premedication in oral surgery].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Dental Anxiety and Anesthesia Techniques",
            "Pharmaceutical studies and practices",
            "Pediatric Pain Management Techniques"
          ]
        },
        {
          "openalex_id": "W1976313727",
          "year": 2000,
          "title": "Pupillomotorik nach Kataraktoperation",
          "type": "article",
          "venue": "Der Ophthalmologe",
          "cited_by_count": 12,
          "topics": [
            "Intraocular Surgery and Lenses",
            "Ophthalmology and Visual Impairment Studies",
            "Retinal and Macular Surgery"
          ]
        },
        {
          "openalex_id": "W7131604379",
          "year": 2007,
          "title": "Problemfelder und Lösungsstrategien in der interkulturellen Kommunikation bei multinationalen Arbeitsgruppen. Dargestellt am Beispiel der Zusammenarbeit der Kuehne + Nagel (AG & Co.) KG, Zweigniederlassung Erfurt und der Kuehne & Nagel Ltd., Representative Office Shanghai.",
          "type": "dissertation",
          "venue": "LIBDOC - Westsächsische Hochschule Zwickau",
          "cited_by_count": 0,
          "topics": [
            "International Student and Expatriate Challenges",
            "Organizational Management and Change",
            "Linguistic Education and Pedagogy"
          ]
        },
        {
          "openalex_id": "W2410150341",
          "year": 2013,
          "title": "Akzeptanz, Nutzen und Praktikabilität eines Fragebogens zur Definition von Reha-Zielen vor Antritt der medizinischen Rehabilitation",
          "type": "article",
          "venue": "Die Rehabilitation",
          "cited_by_count": 2,
          "topics": [
            "Medical Practices and Rehabilitation",
            "Health and Medical Studies",
            "Stroke Rehabilitation and Recovery"
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
          "openalex_id": "W2035768288",
          "year": 2014,
          "title": "Measuring changes in health over time using the EQ-5D 3L and 5L: a head-to-head comparison of measurement properties and sensitivity to change in a German inpatient rehabilitation sample",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 51,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Medical Practices and Rehabilitation",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W3134523367",
          "year": 2021,
          "title": "Facilitators and barriers in anorexia nervosa treatment initiation: a qualitative study on the perspectives of patients, carers and professionals",
          "type": "article",
          "venue": "Journal of Eating Disorders",
          "cited_by_count": 37,
          "topics": [
            "Eating Disorders and Behaviors",
            "Child Nutrition and Feeding Issues",
            "Body Image and Dysmorphia Studies"
          ]
        },
        {
          "openalex_id": "W3158829445",
          "year": 2021,
          "title": "Translation and adaptation of the German version of the Veterans Rand—36/12 Item Health Survey",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 36,
          "topics": [
            "Cancer survivorship and care",
            "Musculoskeletal pain and rehabilitation",
            "Total Knee Arthroplasty Outcomes"
          ]
        },
        {
          "openalex_id": "W1996277752",
          "year": 2014,
          "title": "Ductoscopic Detection of Intraductal Lesions in Cases of Pathologic Nipple Discharge in Comparison with Standard Diagnostics: The German Multicenter Study",
          "type": "article",
          "venue": "Oncology Research and Treatment",
          "cited_by_count": 29,
          "topics": [
            "Breast Lesions and Carcinomas",
            "Breast Implant and Reconstruction",
            "Cancer and Skin Lesions"
          ]
        },
        {
          "openalex_id": "W4289874543",
          "year": 2022,
          "title": "Is EQ-5D-5L Better Than EQ-5D-3L Over Time? A Head-to-Head Comparison of Responsiveness of Descriptive Systems and Value Sets from Nine Countries",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 19,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W3213093900",
          "year": 2021,
          "title": "What difference does multiple imputation make in longitudinal modeling of EQ-5D-5L data? Empirical analyses of simulated and observed missing data patterns",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 19,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Statistical Methods and Bayesian Inference",
            "Meta-analysis and systematic reviews"
          ]
        }
      ]
    }
  },
  {
    "name": "Irina Kinchin",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1676-RA",
        "title": "EQ-HWB, EQ-5D-5L, and ICECAP-A: A Comparative Study of Health and Wellbeing Measures in Ireland",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "1912-RA",
        "title": "Validating the EQ-HWB and its modifications among informal carers of people living with dementia",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "235-RA",
        "title": "Do EQ-5D valuations differ in palliative care settings? A discrete choice experiment",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5054485095",
      "display_name": "Irina Kinchin",
      "orcid": "0000-0003-0133-2763",
      "reported_affiliation": "Trinity College Dublin",
      "works_count": 93,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 19
        },
        {
          "topic": "Indigenous Health, Education, and Rights",
          "works": 17
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 16
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 10
        },
        {
          "topic": "Mental Health and Patient Involvement",
          "works": 9
        },
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 8
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 7
        },
        {
          "topic": "Global Health and Surgery",
          "works": 7
        },
        {
          "topic": "Suicide and Self-Harm Studies",
          "works": 7
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 6
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 5
        },
        {
          "topic": "Indigenous Studies and Ecology",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Iracema Leroi",
          "works": 25
        },
        {
          "name": "Komla Tsey",
          "works": 21
        },
        {
          "name": "Janya McCalman",
          "works": 16
        },
        {
          "name": "Christopher M. Doran",
          "works": 14
        },
        {
          "name": "Roxanne Bainbridge",
          "works": 12
        },
        {
          "name": "David C. Currow",
          "works": 11
        },
        {
          "name": "Slavica Kochovska",
          "works": 11
        },
        {
          "name": "Meera Agar",
          "works": 8
        },
        {
          "name": "Sungwon Chang",
          "works": 8
        },
        {
          "name": "Susan P. Jacups",
          "works": 8
        },
        {
          "name": "Diana Ferreira",
          "works": 7
        },
        {
          "name": "Magnus Ekström",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7119486528",
          "year": 2026,
          "title": "Lived experiences of Lewy body dementia diagnosis and care in Ireland",
          "type": "article",
          "venue": "npj Dementia",
          "cited_by_count": 2,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes",
            "Education, Healthcare and Sociology Research"
          ]
        },
        {
          "openalex_id": "W7130423350",
          "year": 2026,
          "title": "Self-reporting quality of life in mild-to-moderate Alzheimer's disease and Lewy body dementia: Comparing capability and health-focused measures using response process validation",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 0,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W7131625472",
          "year": 2026,
          "title": "The global landscape of online dementia resources",
          "type": "article",
          "venue": "npj Dementia",
          "cited_by_count": 0,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Dementia and Cognitive Impairment Research",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W4410031056",
          "year": 2025,
          "title": "A Comparative Study of Health and Well-Being Measures in Ireland Using EQ Health and Wellbeing (EQ-HWB) and its Short Version, EQ-5D-5L, and ICEpop Capability Measure for Adults (ICECAP-A)",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychological Well-being and Life Satisfaction",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4412355310",
          "year": 2025,
          "title": "A common outcome set for trials in dementia with Lewy bodies (DLB COS)",
          "type": "article",
          "venue": "Alzheimer s & Dementia Translational Research & Clinical Interventions",
          "cited_by_count": 5,
          "topics": [
            "Delphi Technique in Research",
            "Dementia and Cognitive Impairment Research",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4406798841",
          "year": 2025,
          "title": "Addressing Age-Related Complexity in Intellectual Disability (AARC-ID): an economic analysis of different support models. Study protocol.",
          "type": "article",
          "venue": "HRB Open Research",
          "cited_by_count": 0,
          "topics": [
            "Retirement, Disability, and Employment",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W1946029654",
          "year": 2015,
          "title": "An empowerment intervention for Indigenous communities: an outcome assessment",
          "type": "article",
          "venue": "BMC Psychology",
          "cited_by_count": 22,
          "topics": [
            "Indigenous Health, Education, and Rights",
            "Community Health and Development",
            "Community and Sustainable Development"
          ]
        },
        {
          "openalex_id": "W1809728561",
          "year": 2015,
          "title": "No one’s discussing the elephant in the room: contemplating questions of research impact and benefit in Aboriginal and Torres Strait Islander Australian health research",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 276,
          "topics": [
            "Indigenous Health, Education, and Rights",
            "Health Policy Implementation Science",
            "Global Health and Surgery"
          ]
        },
        {
          "openalex_id": "W2329018675",
          "year": 2016,
          "title": "Economic evaluation of ‘Return to Country’: A remote Australian initiative to address indigenous homelessness",
          "type": "article",
          "venue": "Evaluation and Program Planning",
          "cited_by_count": 5,
          "topics": [
            "Homelessness and Social Issues",
            "Indigenous Health, Education, and Rights",
            "Rural development and sustainability"
          ]
        },
        {
          "openalex_id": "W2558335641",
          "year": 2016,
          "title": "Effectiveness of the uptake and implementation of an Aboriginal Australian empowerment program in the context of public health training in Papua New Guinea",
          "type": "article",
          "venue": "Acquire (CQUniversity)",
          "cited_by_count": 3,
          "topics": [
            "Community Health and Development",
            "Community Development and Social Impact",
            "Indigenous Health, Education, and Rights"
          ]
        },
        {
          "openalex_id": "W2767910641",
          "year": 2017,
          "title": "A review of the economic impact of mental illness",
          "type": "article",
          "venue": "Australian Health Review",
          "cited_by_count": 250,
          "topics": [
            "Mental Health Treatment and Access",
            "Health disparities and outcomes",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W3122598258",
          "year": 2021,
          "title": "The economic cost of delirium: A systematic review and quality assessment",
          "type": "review",
          "venue": "Alzheimer s & Dementia",
          "cited_by_count": 125,
          "topics": [
            "Intensive Care Unit Cognitive Disorders",
            "Pain Management and Opioid Use",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2603835732",
          "year": 2017,
          "title": "The Economic Cost of Suicide and Non-Fatal Suicide Behavior in the Australian Workforce and the Potential Impact of a Workplace Suicide Prevention Strategy",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 105,
          "topics": [
            "Suicide and Self-Harm Studies",
            "Mental Health Treatment and Access",
            "Workplace Health and Well-being"
          ]
        },
        {
          "openalex_id": "W2982201588",
          "year": 2019,
          "title": "Breathlessness, Anxiety, Depression, and Function–The BAD-F Study: A Cross-Sectional and Population Prevalence Study in Adults",
          "type": "article",
          "venue": "Journal of Pain and Symptom Management",
          "cited_by_count": 73,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Sleep and related disorders",
            "Cardiac Health and Mental Health"
          ]
        },
        {
          "openalex_id": "W2795573514",
          "year": 2018,
          "title": "The Cost of Youth Suicide in Australia",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 73,
          "topics": [
            "Suicide and Self-Harm Studies",
            "Homicide, Infanticide, and Child Abuse",
            "Gun Ownership and Violence Research"
          ]
        },
        {
          "openalex_id": "W3026605731",
          "year": 2020,
          "title": "Economic and epidemiological impact of youth suicide in countries with the highest human development index",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 64,
          "topics": [
            "Suicide and Self-Harm Studies",
            "Homicide, Infanticide, and Child Abuse"
          ]
        },
        {
          "openalex_id": "W2538502302",
          "year": 2016,
          "title": "The Complexity of Health Service Integration: A Review of Reviews",
          "type": "article",
          "venue": "Frontiers in Public Health",
          "cited_by_count": 62,
          "topics": [
            "Interprofessional Education and Collaboration",
            "Service and Product Innovation",
            "Mental Health and Patient Involvement"
          ]
        }
      ]
    }
  },
  {
    "name": "Iwan van der Horst",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1539-SG",
        "title": "Variability and ease of access in proxy quality of life interviews at the ICU",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5024802434",
      "display_name": "Iwan C.C. van der Horst",
      "orcid": "0000-0003-3891-8522",
      "reported_affiliation": "Cardiovascular Institute Hospital",
      "works_count": 340,
      "top_topics": [
        {
          "topic": "Sepsis Diagnosis and Treatment",
          "works": 80
        },
        {
          "topic": "Acute Myocardial Infarction Research",
          "works": 49
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 42
        },
        {
          "topic": "Hemodynamic Monitoring and Therapy",
          "works": 41
        },
        {
          "topic": "Cardiac Arrest and Resuscitation",
          "works": 37
        },
        {
          "topic": "Cardiovascular Function and Risk Factors",
          "works": 36
        },
        {
          "topic": "Mechanical Circulatory Support Devices",
          "works": 32
        },
        {
          "topic": "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
          "works": 32
        },
        {
          "topic": "Respiratory Support and Mechanisms",
          "works": 29
        },
        {
          "topic": "Cardiac Imaging and Diagnostics",
          "works": 28
        },
        {
          "topic": "Cardiac, Anesthesia and Surgical Outcomes",
          "works": 23
        },
        {
          "topic": "Coronary Interventions and Diagnostics",
          "works": 21
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bas C. T. van Bussel",
          "works": 69
        },
        {
          "name": "Frederik Keus",
          "works": 48
        },
        {
          "name": "Felix Zijlstra",
          "works": 44
        },
        {
          "name": "Pim van der Harst",
          "works": 43
        },
        {
          "name": "Sander M. J. van Kuijk",
          "works": 31
        },
        {
          "name": "Maarten W. Nijsten",
          "works": 30
        },
        {
          "name": "Thijs Delnoij",
          "works": 29
        },
        {
          "name": "Dirk J. van Veldhuisen",
          "works": 28
        },
        {
          "name": "Renske Wiersema",
          "works": 27
        },
        {
          "name": "Dennis C. J. J. Bergmans",
          "works": 27
        },
        {
          "name": "Bart Hiemstra",
          "works": 27
        },
        {
          "name": "Frank van Rosmalen",
          "works": 27
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4292065809",
          "year": 2026,
          "title": "Hemodynamic monitoring during veno-venous extracorporeal membrane oxygenation: A scoping review",
          "type": "article",
          "venue": "Perfusion",
          "cited_by_count": 0,
          "topics": [
            "Mechanical Circulatory Support Devices",
            "Cardiac Arrest and Resuscitation",
            "Advanced battery technologies research"
          ]
        },
        {
          "openalex_id": "W7169881466",
          "year": 2026,
          "title": "Socioeconomic Disparities and the Role of Comorbidity in Hospital Mortality: A Dutch Nationwide Critical Care Cohort Study",
          "type": "article",
          "venue": "Critical Care Medicine",
          "cited_by_count": 0,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Chronic Disease Management Strategies",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W4408747018",
          "year": 2025,
          "title": "Accuracy between ICU admission and discharge diagnoses in non-survivors: A retrospective cohort study",
          "type": "article",
          "venue": "Journal of Critical Care",
          "cited_by_count": 1,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Intensive Care Unit Cognitive Disorders",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W4417185129",
          "year": 2025,
          "title": "Cerebral monitoring responses to bedside physiological challenges in comatose post–cardiac arrest patients",
          "type": "article",
          "venue": "Journal of Clinical Monitoring and Computing",
          "cited_by_count": 0,
          "topics": [
            "Cardiac Arrest and Resuscitation",
            "Optical Imaging and Spectroscopy Techniques",
            "Traumatic Brain Injury and Neurovascular Disturbances"
          ]
        },
        {
          "openalex_id": "W4412891744",
          "year": 2025,
          "title": "Comparison of regional lung mechanics using electrical impedance tomography in mechanically ventilated COVID-19 vs pre-pandemic patients: A retrospective study",
          "type": "article",
          "venue": "Respiratory Medicine",
          "cited_by_count": 2,
          "topics": [
            "Respiratory Support and Mechanisms",
            "Neonatal Respiratory Health Research",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4411069900",
          "year": 2025,
          "title": "Critically ill patients undergoing interhospital transportation: a prospective multicentre cohort study in the Euregio Meuse-Rhine",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Trauma and Emergency Care Studies",
            "Sepsis Diagnosis and Treatment",
            "Emergency and Acute Care Studies"
          ]
        },
        {
          "openalex_id": "W2080104266",
          "year": 2002,
          "title": "Fluid Resuscitation during Active Hemorrhage: Need for a Step Forward",
          "type": "article",
          "venue": "The Journal of Trauma: Injury, Infection, and Critical Care",
          "cited_by_count": 5,
          "topics": [
            "Trauma, Hemostasis, Coagulopathy, Resuscitation",
            "Trauma and Emergency Care Studies",
            "Cardiac Arrest and Resuscitation"
          ]
        },
        {
          "openalex_id": "W2144651860",
          "year": 2003,
          "title": "Beneficial effect of glucose‐insulin‐potassium infusion in noncritically ill patients has to be proven",
          "type": "article",
          "venue": "Journal of Internal Medicine",
          "cited_by_count": 4,
          "topics": [
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes Management and Research",
            "Metabolism, Diabetes, and Cancer"
          ]
        },
        {
          "openalex_id": "W4235684772",
          "year": 2003,
          "title": "Corticosteroids for Patients With Septic Shock",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 0,
          "topics": [
            "Adrenal Hormones and Disorders",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2093290757",
          "year": 2003,
          "title": "Corticosteroids for patients with septic shock. Authors' reply",
          "type": "letter",
          "venue": "JAMA",
          "cited_by_count": 3,
          "topics": [
            "Adrenal Hormones and Disorders",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W3014524604",
          "year": 2020,
          "title": "Prediction models for diagnosis and prognosis of covid-19: systematic review and critical appraisal",
          "type": "review",
          "venue": "BMJ",
          "cited_by_count": 3262,
          "topics": [
            "COVID-19 Clinical Research Studies",
            "COVID-19 diagnosis using AI",
            "SARS-CoV-2 detection and testing"
          ]
        },
        {
          "openalex_id": "W2921375647",
          "year": 2019,
          "title": "Coronary Angiography after Cardiac Arrest without ST-Segment Elevation",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 537,
          "topics": [
            "Cardiac Arrest and Resuscitation",
            "Mechanical Circulatory Support Devices",
            "Acute Myocardial Infarction Research"
          ]
        },
        {
          "openalex_id": "W2898389841",
          "year": 2018,
          "title": "Pantoprazole in Patients at Risk for Gastrointestinal Bleeding in the ICU",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 349,
          "topics": [
            "Nosocomial Infections in ICU",
            "Sepsis Diagnosis and Treatment",
            "Clostridium difficile and Clostridium perfringens research"
          ]
        },
        {
          "openalex_id": "W1796632239",
          "year": 2011,
          "title": "Culprit Vessel Only Versus Multivessel and Staged Percutaneous Coronary Intervention for Multivessel Disease in Patients Presenting With ST-Segment Elevation Myocardial Infarction",
          "type": "article",
          "venue": "Journal of the American College of Cardiology",
          "cited_by_count": 305,
          "topics": [
            "Coronary Interventions and Diagnostics",
            "Acute Myocardial Infarction Research",
            "Mechanical Circulatory Support Devices"
          ]
        },
        {
          "openalex_id": "W2113849464",
          "year": 2003,
          "title": "Glucose-insulin-potassium infusion inpatients treated with primary angioplasty for acute myocardial infarction",
          "type": "article",
          "venue": "Journal of the American College of Cardiology",
          "cited_by_count": 261,
          "topics": [
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Potassium and Related Disorders",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W2970939804",
          "year": 2019,
          "title": "Metabolomics Profile in Depression: A Pooled Analysis of 230 Metabolic Markers in 5283 Cases With Depression and 10,145 Controls",
          "type": "article",
          "venue": "Biological Psychiatry",
          "cited_by_count": 251,
          "topics": [
            "Metabolomics and Mass Spectrometry Studies",
            "Tryptophan and brain disorders",
            "Treatment of Major Depression"
          ]
        },
        {
          "openalex_id": "W2590924093",
          "year": 2017,
          "title": "Incidence, timing and outcome of AKI in critically ill patients varies with the definition used and the addition of urine output criteria",
          "type": "article",
          "venue": "BMC Nephrology",
          "cited_by_count": 242,
          "topics": [
            "Acute Kidney Injury Research",
            "Sepsis Diagnosis and Treatment",
            "Trauma, Hemostasis, Coagulopathy, Resuscitation"
          ]
        },
        {
          "openalex_id": "W2047443422",
          "year": 2011,
          "title": "Prognostic Value of Admission Glycosylated Hemoglobin and Glucose in Nondiabetic Patients With ST-Segment–Elevation Myocardial Infarction Treated With Percutaneous Coronary Intervention",
          "type": "article",
          "venue": "Circulation",
          "cited_by_count": 241,
          "topics": [
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Diabetes Management and Research"
          ]
        }
      ]
    }
  }
]
