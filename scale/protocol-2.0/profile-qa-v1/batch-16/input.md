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
    "name": "Erwin Birnie",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20200060",
        "title": "Grant to develop the outcomes-research component of the intended Capacity-2 study",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5023843843",
      "display_name": "Erwin Birnie",
      "orcid": "0000-0002-4534-4857",
      "reported_affiliation": "University Medical Center Groningen",
      "works_count": 338,
      "top_topics": [
        {
          "topic": "Prenatal Screening and Diagnostics",
          "works": 28
        },
        {
          "topic": "Maternal and Perinatal Health Interventions",
          "works": 25
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 19
        },
        {
          "topic": "Breast Cancer Treatment Studies",
          "works": 18
        },
        {
          "topic": "Uterine Myomas and Treatments",
          "works": 17
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 17
        },
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 17
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 17
        },
        {
          "topic": "Cardiomyopathy and Myosin Studies",
          "works": 16
        },
        {
          "topic": "Gynecological conditions and treatments",
          "works": 14
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 14
        },
        {
          "topic": "Breast Implant and Reconstruction",
          "works": 14
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Gouke J. Bonsel",
          "works": 81
        },
        {
          "name": "Manuel Castro Cabezas",
          "works": 51
        },
        {
          "name": "Irene M. van Langen",
          "works": 44
        },
        {
          "name": "Eric A.P. Steegers",
          "works": 29
        },
        {
          "name": "Boudewijn Klop",
          "works": 27
        },
        {
          "name": "T.M.A.L. Klem",
          "works": 25
        },
        {
          "name": "Adelita V. Ranchor",
          "works": 24
        },
        {
          "name": "Gerson M. Struik",
          "works": 23
        },
        {
          "name": "Mirjam Plantinga",
          "works": 22
        },
        {
          "name": "Semiha Denktaş",
          "works": 19
        },
        {
          "name": "Gert‐Jan M. van de Geijn",
          "works": 19
        },
        {
          "name": "Henk‐Jan Aanstoot",
          "works": 19
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7129006891",
          "year": 2026,
          "title": "Exploring feasible ways of person-reported outcome measurement in routine type 1 diabetes care: a protocol for the Diabeter-PROM study",
          "type": "article",
          "venue": "Frontiers in Clinical Diabetes and Healthcare",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Education",
            "Diabetes Management and Research",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W7163922442",
          "year": 2026,
          "title": "Meta-analysis of adverse events in clinical studies with antisense oligonucleotide therapies",
          "type": "review",
          "venue": "Molecular Therapy — Nucleic Acids",
          "cited_by_count": 0,
          "topics": [
            "DNA and Nucleic Acid Chemistry",
            "Hemoglobinopathies and Related Disorders",
            "PARP inhibition in cancer therapy"
          ]
        },
        {
          "openalex_id": "W7135101514",
          "year": 2026,
          "title": "Psychometric Properties of the EQ-5D-5L in Post-COVID-19 Condition: Results From the Long CORFU Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and Mental Health",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Traumatic Brain Injury Research"
          ]
        },
        {
          "openalex_id": "W7136651262",
          "year": 2026,
          "title": "The Ability of Serum Amyloid A to Discriminate Coronavirus Disease 2019 ( <scp>COVID</scp> ‐19) Patients Who Stay Moderately Ill Versus Patients Who Become Severely Ill",
          "type": "article",
          "venue": "Journal of Clinical Laboratory Analysis",
          "cited_by_count": 0,
          "topics": [
            "Amyloidosis: Diagnosis, Treatment, Outcomes",
            "COVID-19 Clinical Research Studies",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W7130520739",
          "year": 2026,
          "title": "Towards responsible genome-wide screening",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "BRCA gene mutations in cancer",
            "Genomics and Rare Diseases",
            "Prenatal Screening and Diagnostics"
          ]
        },
        {
          "openalex_id": "W7161994325",
          "year": 2026,
          "title": "Towards responsible genome-wide screening: normative and stakeholder considerations",
          "type": "article",
          "venue": "European Journal of Human Genetics",
          "cited_by_count": 0,
          "topics": [
            "BRCA gene mutations in cancer",
            "Genomics and Rare Diseases",
            "Prenatal Screening and Diagnostics"
          ]
        },
        {
          "openalex_id": "W2117110200",
          "year": 1992,
          "title": "Experimental pathology of intravenous Polyurethane cannulae containing disinfectant",
          "type": "article",
          "venue": "Journal of Hospital Infection",
          "cited_by_count": 9,
          "topics": [
            "Antimicrobial agents and applications",
            "Anesthesia and Sedative Agents",
            "Airway Management and Intubation Techniques"
          ]
        },
        {
          "openalex_id": "W2464519062",
          "year": 1994,
          "title": "Cost-effectiveness of HA-1A treatment for patients with sepsis.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 3,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cardiac, Anesthesia and Surgical Outcomes"
          ]
        },
        {
          "openalex_id": "W2509082238",
          "year": 1997,
          "title": "Cost-Minimization Analvsis of Domiciliarv Antenatal Fetal Monitor& in High-Risk J Pregnancies",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Neonatal Respiratory Health Research",
            "Global Maternal and Child Health",
            "Maternal and Perinatal Health Interventions"
          ]
        },
        {
          "openalex_id": "W2091994458",
          "year": 1997,
          "title": "Cost-minimization analysis of domiciliary antenatal fetal monitoring in high-risk pregnancies",
          "type": "article",
          "venue": "Obstetrics and Gynecology",
          "cited_by_count": 17,
          "topics": [
            "Neonatal and fetal brain pathology",
            "Neonatal Respiratory Health Research",
            "Healthcare Technology and Patient Monitoring"
          ]
        },
        {
          "openalex_id": "W2113313274",
          "year": 2016,
          "title": "Uterine artery embolization vs hysterectomy in the treatment of symptomatic uterine fibroids: 10-year outcomes from the randomized EMMY trial",
          "type": "article",
          "venue": "American Journal of Obstetrics and Gynecology",
          "cited_by_count": 388,
          "topics": [
            "Uterine Myomas and Treatments",
            "Gynecological conditions and treatments",
            "Maternal and fetal healthcare"
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
          "openalex_id": "W2146309723",
          "year": 2007,
          "title": "Loss of ovarian reserve after uterine artery embolization: a randomized comparison with hysterectomy",
          "type": "article",
          "venue": "Human Reproduction",
          "cited_by_count": 263,
          "topics": [
            "Uterine Myomas and Treatments",
            "Gynecological conditions and treatments",
            "Thyroid and Parathyroid Surgery"
          ]
        },
        {
          "openalex_id": "W2132458770",
          "year": 2005,
          "title": "Uterine artery embolization versus hysterectomy in the treatment of symptomatic uterine fibroids (EMMY trial): Peri- and postprocedural results from a randomized controlled trial",
          "type": "article",
          "venue": "American Journal of Obstetrics and Gynecology",
          "cited_by_count": 194,
          "topics": [
            "Uterine Myomas and Treatments",
            "Gynecological conditions and treatments",
            "Thyroid and Parathyroid Surgery"
          ]
        },
        {
          "openalex_id": "W2120813609",
          "year": 2010,
          "title": "Risk stratification for sudden cardiac death in hypertrophic cardiomyopathy: systematic review of clinical risk markers",
          "type": "review",
          "venue": "EP Europace",
          "cited_by_count": 176,
          "topics": [
            "Cardiomyopathy and Myosin Studies",
            "Viral Infections and Immunology Research",
            "Cardiovascular Effects of Exercise"
          ]
        },
        {
          "openalex_id": "W2033952229",
          "year": 2008,
          "title": "Symptomatic Uterine Fibroids: Treatment with Uterine Artery Embolization or Hysterectomy—Results from the Randomized Clinical Embolisation versus Hysterectomy (EMMY) Trial",
          "type": "article",
          "venue": "Radiology",
          "cited_by_count": 176,
          "topics": [
            "Uterine Myomas and Treatments",
            "Gynecological conditions and treatments",
            "Maternal and fetal healthcare"
          ]
        },
        {
          "openalex_id": "W2108252565",
          "year": 2004,
          "title": "CT Colonography and Colonoscopy: Assessment of Patient Preference in a 5-week Follow-up Study",
          "type": "article",
          "venue": "Radiology",
          "cited_by_count": 159,
          "topics": [
            "Colorectal Cancer Screening and Detection",
            "Radiology practices and education",
            "Microscopic Colitis"
          ]
        },
        {
          "openalex_id": "W4253890724",
          "year": 2010,
          "title": "Uterine artery embolization vs hysterectomy in the treatment of symptomatic uterine fibroids: 5-year outcome from the randomized EMMY trial",
          "type": "article",
          "venue": "American Journal of Obstetrics and Gynecology",
          "cited_by_count": 150,
          "topics": [
            "Uterine Myomas and Treatments",
            "Gynecological conditions and treatments",
            "Endometriosis Research and Treatment"
          ]
        }
      ]
    }
  },
  {
    "name": "Eszter Szlávicz",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2400-RA",
        "title": "Understanding caregiver perspectives: qualitative testing of EQ-TIPS among caregiver dyads for children with moderate and severe chronic skin disease",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5086041403",
      "display_name": "Eszter Szlávicz",
      "orcid": "0000-0002-1083-0994",
      "reported_affiliation": "Veszprémi Érseki Hittudományi Fõiskola",
      "works_count": 33,
      "top_topics": [
        {
          "topic": "Body Image and Dysmorphia Studies",
          "works": 8
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 6
        },
        {
          "topic": "Psoriasis: Treatment and Pathogenesis",
          "works": 6
        },
        {
          "topic": "RNA Research and Splicing",
          "works": 6
        },
        {
          "topic": "Nail Diseases and Treatments",
          "works": 6
        },
        {
          "topic": "Cytokine Signaling Pathways and Interactions",
          "works": 5
        },
        {
          "topic": "Tattoo and Body Piercing Complications",
          "works": 3
        },
        {
          "topic": "Cell Adhesion Molecules Research",
          "works": 3
        },
        {
          "topic": "Skin and Cellular Biology Research",
          "works": 2
        },
        {
          "topic": "Neuropeptides and Animal Physiology",
          "works": 2
        },
        {
          "topic": "Neuroendocrine regulation and behavior",
          "works": 2
        },
        {
          "topic": "Fungal Infections and Studies",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Rolland Gyulai",
          "works": 14
        },
        {
          "name": "Zsuzsanna Lengyel",
          "works": 11
        },
        {
          "name": "Márta Széll",
          "works": 7
        },
        {
          "name": "Kornélia Szabó",
          "works": 6
        },
        {
          "name": "Zsuzsanna Bata‐Csörgõ",
          "works": 6
        },
        {
          "name": "Lajos Kemény",
          "works": 6
        },
        {
          "name": "Tamás Bancsók",
          "works": 5
        },
        {
          "name": "Péter Osváth",
          "works": 5
        },
        {
          "name": "Gergely Groma",
          "works": 4
        },
        {
          "name": "Péter Oláh",
          "works": 4
        },
        {
          "name": "Jutta Major",
          "works": 4
        },
        {
          "name": "Éva Szepes",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7135057139",
          "year": 2026,
          "title": "Narcissistic Traits and Narcissistic Personality Disorder in Dermatology With a Focus on Body‐Dysmorphic Disorder",
          "type": "article",
          "venue": "International Journal of Dermatology",
          "cited_by_count": 0,
          "topics": [
            "Body Image and Dysmorphia Studies",
            "Facial Rejuvenation and Surgery Techniques",
            "Genetic and rare skin diseases."
          ]
        },
        {
          "openalex_id": "W7166097239",
          "year": 2026,
          "title": "PS09 Building an integrated psychodermatology service in central Europe: clinical implementation and research experience from Pécs, Hungary",
          "type": "conference-abstract",
          "venue": "British Journal of Dermatology",
          "cited_by_count": 0,
          "topics": [
            "Body Image and Dysmorphia Studies",
            "Psoriasis: Treatment and Pathogenesis",
            "Dermatology and Skin Diseases"
          ]
        },
        {
          "openalex_id": "W4417311992",
          "year": 2025,
          "title": "Addiction and chronic skin diseases: A Pan‐European study on prevalence, associations and patient impact",
          "type": "article",
          "venue": "Journal of the European Academy of Dermatology and Venereology",
          "cited_by_count": 4,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Psoriasis: Treatment and Pathogenesis",
            "Skin Protection and Aging"
          ]
        },
        {
          "openalex_id": "W4410092631",
          "year": 2025,
          "title": "Body Dysmorphic Disorder, Social Media Use, Borderline and Narcissistic Pathologies",
          "type": "article",
          "venue": "International Journal of Dermatology",
          "cited_by_count": 4,
          "topics": [
            "Body Image and Dysmorphia Studies",
            "Tattoo and Body Piercing Complications",
            "Evolutionary Psychology and Human Behavior"
          ]
        },
        {
          "openalex_id": "W4408032509",
          "year": 2024,
          "title": "Diagnosis of mycotic skin infections and principles of antimycotic therapy",
          "type": "article",
          "venue": "Bőrgyógyászati és Venerológiai Szemle",
          "cited_by_count": 0,
          "topics": [
            "Nail Diseases and Treatments",
            "Plant Pathogens and Fungal Diseases",
            "Antifungal resistance and susceptibility"
          ]
        },
        {
          "openalex_id": "W4394750209",
          "year": 2024,
          "title": "History, structure and international practice of psychodermatology care",
          "type": "article",
          "venue": "Bőrgyógyászati és Venerológiai Szemle",
          "cited_by_count": 3,
          "topics": [
            "Body Image and Dysmorphia Studies"
          ]
        },
        {
          "openalex_id": "W2120848160",
          "year": 2014,
          "title": "Inhibition of Opioid Receptor Mediated G-Protein Activity After Chronic Administration of Kynurenic Acid and its Derivative without Direct Binding to Opioid Receptors",
          "type": "article",
          "venue": "CNS & Neurological Disorders - Drug Targets",
          "cited_by_count": 18,
          "topics": [
            "Neuropeptides and Animal Physiology",
            "Neuroendocrine regulation and behavior",
            "Pharmacological Receptor Mechanisms and Effects"
          ]
        },
        {
          "openalex_id": "W2737623142",
          "year": 2014,
          "title": "PPIG, SFRS-18 és LUC7L3 Splicing regulárok vizsgálata szinkronizált, immortalizált sejtvonalakban és pikkelysömörben",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "RNA Research and Splicing",
            "Sarcoma Diagnosis and Treatment",
            "Virus-based gene therapy research"
          ]
        },
        {
          "openalex_id": "W2740145100",
          "year": 2014,
          "title": "Splicing regulation disturbances in psoriasis pathogenesis",
          "type": "article",
          "venue": "Repository of the Academy's Library (Library of the Hungarian Academy of Sciences)",
          "cited_by_count": 0,
          "topics": [
            "Cell Adhesion Molecules Research",
            "RNA Research and Splicing",
            "Skin and Cellular Biology Research"
          ]
        },
        {
          "openalex_id": "W2324771434",
          "year": 2014,
          "title": "What have we learned about non-involved psoriatic skin from large-scale gene expression studies?",
          "type": "article",
          "venue": "World Journal of Dermatology",
          "cited_by_count": 0,
          "topics": [
            "Psoriasis: Treatment and Pathogenesis",
            "Cytokine Signaling Pathways and Interactions",
            "Nuclear Receptors and Signaling"
          ]
        },
        {
          "openalex_id": "W2622214567",
          "year": 2017,
          "title": "Splicing factors differentially expressed in psoriasis alter mRNA maturation of disease-associated EDA+ fibronectin",
          "type": "article",
          "venue": "Molecular and Cellular Biochemistry",
          "cited_by_count": 24,
          "topics": [
            "Cell Adhesion Molecules Research",
            "Skin and Cellular Biology Research",
            "Cellular Mechanics and Interactions"
          ]
        },
        {
          "openalex_id": "W4387296137",
          "year": 2023,
          "title": "Content validity of the EQ-5D-5L with skin irritation and self-confidence bolt-ons in patients with atopic dermatitis: a qualitative think-aloud study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 18,
          "topics": [
            "Dermatology and Skin Diseases",
            "Psoriasis: Treatment and Pathogenesis",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2796054054",
          "year": 2018,
          "title": "The rs13388259 Intergenic Polymorphism in the Genomic Context of the<i>BCYRN1</i>Gene Is Associated with Parkinson’s Disease in the Hungarian Population",
          "type": "article",
          "venue": "Parkinson s Disease",
          "cited_by_count": 17,
          "topics": [
            "Cancer-related molecular mechanisms research",
            "RNA modifications and cancer",
            "RNA regulation and disease"
          ]
        },
        {
          "openalex_id": "W2790854129",
          "year": 2018,
          "title": "Analysis of psoriasis‐relevant gene expression and exon usage alterations after silencing of <scp>SR</scp>‐rich splicing regulators",
          "type": "article",
          "venue": "Experimental Dermatology",
          "cited_by_count": 12,
          "topics": [
            "Cytokine Signaling Pathways and Interactions",
            "Immune Response and Inflammation",
            "RNA Research and Splicing"
          ]
        },
        {
          "openalex_id": "W2281773954",
          "year": 2015,
          "title": "Further Characterization of Hemopressin Peptide Fragments in the Opioid and Cannabinoid Systems",
          "type": "article",
          "venue": "Anesthesia & Analgesia",
          "cited_by_count": 11,
          "topics": [
            "Neuroendocrine regulation and behavior",
            "Neuropeptides and Animal Physiology",
            "Renin-Angiotensin System Studies"
          ]
        },
        {
          "openalex_id": "W3030560090",
          "year": 2020,
          "title": "Congenital ichthyosis associated with Trichophyton rubrum tinea, imitating drug hypersensitivity reaction",
          "type": "article",
          "venue": "Medical Mycology Case Reports",
          "cited_by_count": 8,
          "topics": [
            "Nail Diseases and Treatments",
            "Fungal Infections and Studies",
            "Plant Pathogens and Fungal Diseases"
          ]
        }
      ]
    }
  },
  {
    "name": "Fan Yang",
    "member_affiliation": "Analysis Group",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5056976700",
      "display_name": "Fan Yang",
      "orcid": "0000-0003-4689-265X",
      "reported_affiliation": "",
      "works_count": 106,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 24
        },
        {
          "topic": "Dialysis and Renal Disease Management",
          "works": 11
        },
        {
          "topic": "Cardiac, Anesthesia and Surgical Outcomes",
          "works": 6
        },
        {
          "topic": "Chronic Kidney Disease and Diabetes",
          "works": 6
        },
        {
          "topic": "Physical Activity and Health",
          "works": 6
        },
        {
          "topic": "Balance, Gait, and Falls Prevention",
          "works": 5
        },
        {
          "topic": "Acute Ischemic Stroke Management",
          "works": 5
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 5
        },
        {
          "topic": "Gastric Cancer Management and Outcomes",
          "works": 5
        },
        {
          "topic": "Stroke Rehabilitation and Recovery",
          "works": 4
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 4
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nan Luo",
          "works": 12
        },
        {
          "name": "Simon Walker",
          "works": 9
        },
        {
          "name": "Brenda Gannon",
          "works": 7
        },
        {
          "name": "Susan Griffin",
          "works": 7
        },
        {
          "name": "Hongwei Sun",
          "works": 7
        },
        {
          "name": "Anantharaman Vathsala",
          "works": 6
        },
        {
          "name": "Tim Stephens",
          "works": 5
        },
        {
          "name": "Gerry Richardson",
          "works": 5
        },
        {
          "name": "Rupert M. Pearse",
          "works": 5
        },
        {
          "name": "Konstadina Griva",
          "works": 5
        },
        {
          "name": "Graham Martin",
          "works": 4
        },
        {
          "name": "Mandeep Phull",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4411725898",
          "year": 2025,
          "title": "A Novel Memristor-Based Majority Logic and Efficient Approximate Full Adder for Image Processing",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "Advanced Memory and Neural Computing",
            "CCD and CMOS Imaging Sensors",
            "Neural Networks and Applications"
          ]
        },
        {
          "openalex_id": "W4406379692",
          "year": 2025,
          "title": "Advancing presurgical non-invasive spread through air spaces prediction in clinical stage IA lung adenocarcinoma using artificial intelligence and CT signatures",
          "type": "article",
          "venue": "Frontiers in Surgery",
          "cited_by_count": 6,
          "topics": [
            "Radiomics and Machine Learning in Medical Imaging",
            "Lung Cancer Diagnosis and Treatment",
            "Advanced Radiotherapy Techniques"
          ]
        },
        {
          "openalex_id": "W4407099007",
          "year": 2025,
          "title": "Analysis of factors associated with intercostal neuralgia after osteoporotic thoracic spine fracture and construction of a prediction model",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 0,
          "topics": [
            "Spinal Fractures and Fixation Techniques",
            "Cervical and Thoracic Myelopathy",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W4410908795",
          "year": 2025,
          "title": "Asymptomatic intramural esophageal dissection: A case report and literature review",
          "type": "article",
          "venue": "Medicine",
          "cited_by_count": 2,
          "topics": [
            "Esophageal and GI Pathology",
            "Esophageal Cancer Research and Treatment",
            "Dysphagia Assessment and Management"
          ]
        },
        {
          "openalex_id": "W4411255048",
          "year": 2025,
          "title": "Clinical features of Kawasaki disease and analysis of risk factors for coronary damage",
          "type": "article",
          "venue": "AIMS Medical Science",
          "cited_by_count": 1,
          "topics": [
            "Kawasaki Disease and Coronary Complications",
            "Coronary Artery Anomalies",
            "Liver Disease and Transplantation"
          ]
        },
        {
          "openalex_id": "W4406748085",
          "year": 2025,
          "title": "Combining pelvic floor ultrasonography with deep learning to diagnose anterior compartment organ prolapse",
          "type": "article",
          "venue": "Quantitative Imaging in Medicine and Surgery",
          "cited_by_count": 6,
          "topics": [
            "Pelvic floor disorders treatments",
            "Endometriosis Research and Treatment",
            "Preterm Birth and Chorioamnionitis"
          ]
        },
        {
          "openalex_id": "W2327907720",
          "year": 2012,
          "title": "ME2 Validation of the Kidney Disease and Quality of Life Questionnaire (KDQOL-36) in Haemodialysis Patients in Singapore",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3030544684",
          "year": 2012,
          "title": "The behavioral improvements and mechanisms by ziprasidone early intervention in a rat model of posttraumatic stress disorder",
          "type": "article",
          "venue": "Zhonghua xingwei yixue yu naokexue zazhi",
          "cited_by_count": 0,
          "topics": [
            "Traumatic Brain Injury and Neurovascular Disturbances",
            "Neurological Disorders and Treatments"
          ]
        },
        {
          "openalex_id": "W2130825154",
          "year": 2013,
          "title": "Prevalence of infarct and villous clumps, and the expression of α-smooth muscle actin in the placental basal plate in severe preeclampsia",
          "type": "article",
          "venue": "Molecular Medicine Reports",
          "cited_by_count": 5,
          "topics": [
            "Pregnancy and preeclampsia studies",
            "Prenatal Screening and Diagnostics",
            "Birth, Development, and Health"
          ]
        },
        {
          "openalex_id": "W2074847568",
          "year": 2013,
          "title": "Validation of the English Version of the Kidney Disease Quality of Life Questionnaire (KDQOL-36) in Haemodialysis Patients in Singapore",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 32,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Chronic Kidney Disease and Diabetes",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2911929705",
          "year": 2019,
          "title": "Effectiveness of a national quality improvement programme to improve survival after emergency abdominal surgery (EPOCH): a stepped-wedge cluster-randomised trial",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 189,
          "topics": [
            "Cardiac, Anesthesia and Surgical Outcomes",
            "Trauma and Emergency Care Studies",
            "Enhanced Recovery After Surgery"
          ]
        },
        {
          "openalex_id": "W1994196649",
          "year": 2015,
          "title": "Health-related quality of life of Asian patients with end-stage renal disease (ESRD) in Singapore",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 115,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Chronic Kidney Disease and Diabetes",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2031064002",
          "year": 2014,
          "title": "Comparison of the preference-based EQ-5D-5L and SF-6D in patients with end-stage renal disease (ESRD)",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 80,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dialysis and Renal Disease Management",
            "Chronic Kidney Disease and Diabetes"
          ]
        },
        {
          "openalex_id": "W2883633486",
          "year": 2018,
          "title": "Tai Chi for Stroke Rehabilitation: A Systematic Review and Meta-Analysis of Randomized Controlled Trials",
          "type": "review",
          "venue": "Frontiers in Physiology",
          "cited_by_count": 77,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Balance, Gait, and Falls Prevention",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W1883503528",
          "year": 2015,
          "title": "Responding to Young People’s Health Risks in Primary Care: A Cluster Randomised Trial of Training Clinicians in Screening and Motivational Interviewing",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 76,
          "topics": [
            "Adolescent Sexual and Reproductive Health",
            "Substance Abuse Treatment and Outcomes",
            "Child Abuse and Trauma"
          ]
        },
        {
          "openalex_id": "W2744647264",
          "year": 2017,
          "title": "Measurement tools of resource use and quality of life in clinical trials for dementia or cognitive impairment interventions: A systematically conducted narrative review",
          "type": "review",
          "venue": "International Journal of Geriatric Psychiatry",
          "cited_by_count": 69,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2746961250",
          "year": 2017,
          "title": "Referral for Expert Physical Activity Counseling: A Pragmatic RCT",
          "type": "article",
          "venue": "American Journal of Preventive Medicine",
          "cited_by_count": 69,
          "topics": [
            "Physical Activity and Health",
            "Cardiovascular and exercise physiology",
            "Behavioral Health and Interventions"
          ]
        },
        {
          "openalex_id": "W2172819197",
          "year": 2015,
          "title": "Cost‐effectiveness of haemodialysis and peritoneal dialysis for patients with end‐stage renal disease in Singapore",
          "type": "article",
          "venue": "Nephrology",
          "cited_by_count": 55,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Chronic Kidney Disease and Diabetes",
            "Acute Kidney Injury Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Fanni Rencz",
    "member_affiliation": "Corvinus University of Budapest, Department of Health Policy",
    "is_member": true,
    "projects": [
      {
        "project_id": "119-RA",
        "title": "A qualitative study on the content validity of the EQ-5D-5L and EQ-PSO bolt-on in patients with psoriasis in Hungary",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1700-RA",
        "title": "Cognition bolt-ons for the EQ-5D-5L and EQ-5D-3L: a systematic review",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1800-RA",
        "title": "Social and temporal comparisons on the EQ-5D",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "192-VS",
        "title": "Valuation of the EQ-5D-Y in Hungary",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2000-RA",
        "title": "Developing a consensus-based reporting checklist for EuroQol instruments based on EQUATOR guidance",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20170500",
        "title": "Hungarian EQ-5D-5L valuation study",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5024021740",
      "display_name": "Fanni Rencz",
      "orcid": "0000-0001-9674-620X",
      "reported_affiliation": "Semmelweis University",
      "works_count": 245,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 114
        },
        {
          "topic": "Psoriasis: Treatment and Pathogenesis",
          "works": 47
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 36
        },
        {
          "topic": "Biosimilars and Bioanalytical Methods",
          "works": 19
        },
        {
          "topic": "Inflammatory Bowel Disease",
          "works": 16
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 14
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 14
        },
        {
          "topic": "Autoimmune Bullous Skin Diseases",
          "works": 14
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 11
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 9
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 9
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 8
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Valentin Brodszky",
          "works": 187
        },
        {
          "name": "László Gulàcsi",
          "works": 120
        },
        {
          "name": "Márta Péntek",
          "works": 117
        },
        {
          "name": "Petra Baji",
          "works": 58
        },
        {
          "name": "Andrea Szegedi",
          "works": 39
        },
        {
          "name": "Miklós Sárdy",
          "works": 35
        },
        {
          "name": "Zsombor Zrubka",
          "works": 33
        },
        {
          "name": "Péter Holló",
          "works": 32
        },
        {
          "name": "Zsuzsanna Beretzky",
          "works": 28
        },
        {
          "name": "Sarolta Kárpáti",
          "works": 25
        },
        {
          "name": "Éva Remenyik",
          "works": 22
        },
        {
          "name": "K. Hajdu",
          "works": 22
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164732578",
          "year": 2026,
          "title": "1st EuroQol Central and Eastern Europe Regional Meeting: Book of Abstracts",
          "type": "other",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7164751425",
          "year": 2026,
          "title": "1st EuroQol Central and Eastern Europe Regional Meeting: Book of Abstracts",
          "type": "other",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7166799494",
          "year": 2026,
          "title": "Comparative exploration of EQ-5D-5L bolt-on variants for fatigue, sleep, and vision in a general population sample",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Ergonomics and Musculoskeletal Disorders",
            "Safety Warnings and Signage"
          ]
        },
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
          "openalex_id": "W7166145415",
          "year": 2026,
          "title": "PCR125 PATIENTS’ VIEWS ON PUBLIC SUPPORT MECHANISMS IN COELIAC DISEASE IN HUNGARY",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Celiac Disease Research and Management",
            "Microscopic Colitis",
            "Inflammatory Bowel Disease"
          ]
        },
        {
          "openalex_id": "W7164842455",
          "year": 2026,
          "title": "Psychometric properties of four FACE-Q Aesthetics scales in patients planning and undergoing minimally invasive facial cosmetic procedures",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Facial Rejuvenation and Surgery Techniques",
            "Body Image and Dysmorphia Studies",
            "Botulinum Toxin and Related Neurological Disorders"
          ]
        },
        {
          "openalex_id": "W2040895099",
          "year": 2013,
          "title": "Frequency of Lower Urinary Tract Symptoms in Men and Women in Hungary – Results of an Open Label Questionnaire Study from 2012",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Pelvic floor disorders treatments"
          ]
        },
        {
          "openalex_id": "W2012813142",
          "year": 2014,
          "title": "A Comaprative Cross-Sectional Study On Health-Related Quality Of Life In Psoriasis From Hungary And Iran",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W2077942718",
          "year": 2014,
          "title": "Budget Impact Analysis Of Biosimilar Infliximab For The Treatment Of Crohn's Disease In Six Central Eastern European Countries",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 5,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1939757787",
          "year": 2014,
          "title": "Disease burden of psoriasis associated with psoriatic arthritis in Hungary",
          "type": "article",
          "venue": "Orvosi Hetilap",
          "cited_by_count": 13,
          "topics": [
            "Psoriasis: Treatment and Pathogenesis",
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W2279527004",
          "year": 2016,
          "title": "Alopecia areata and health-related quality of life: a systematic review and meta-analysis",
          "type": "review",
          "venue": "British Journal of Dermatology",
          "cited_by_count": 240,
          "topics": [
            "Hair Growth and Disorders",
            "Facial Rejuvenation and Surgery Techniques",
            "Skin and Cellular Biology Research"
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
          "openalex_id": "W3048694137",
          "year": 2020,
          "title": "Parallel Valuation of the EQ-5D-3L and EQ-5D-5L by Time Trade-Off in Hungary",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 119,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W2057699446",
          "year": 2014,
          "title": "Exploring the relationship between EQ-5D, DLQI and PASI, and mapping EQ-5D utilities: a cross-sectional study in psoriasis from Hungary",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 98,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psoriasis: Treatment and Pathogenesis",
            "Spondyloarthritis Studies and Treatments"
          ]
        },
        {
          "openalex_id": "W2946470017",
          "year": 2019,
          "title": "Psychometric properties of the Hungarian version of the eHealth Literacy Scale",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 93,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Mobile Health and mHealth Applications",
            "Electronic Health Records Systems"
          ]
        },
        {
          "openalex_id": "W1973791399",
          "year": 2014,
          "title": "Health technology assessment in Poland, the Czech Republic, Hungary, Romania and Bulgaria",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 85,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W2751008784",
          "year": 2017,
          "title": "Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L in psoriasis patients",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 78,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psoriasis: Treatment and Pathogenesis",
            "Dermatology and Skin Diseases"
          ]
        },
        {
          "openalex_id": "W2606245581",
          "year": 2017,
          "title": "The Rituximab Biosimilar CT-P10 in Rheumatology and Cancer: A Budget Impact Analysis in 28 European Countries",
          "type": "article",
          "venue": "Advances in Therapy",
          "cited_by_count": 78,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "CAR-T cell therapy research",
            "Monoclonal and Polyclonal Antibodies Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Fatima Al Sayah",
    "member_affiliation": "University of Alberta (Canada), Centre for Clinical, Health Economics, and Outcomes Research, CCHO (Lebanon, UAE, KSA)",
    "is_member": true,
    "projects": [
      {
        "project_id": "102-RA",
        "title": "The impact of COVID-19 on health status, based on the EQ-5D-5L, of adults visiting emergency departments and primary care clinics in Alberta, Canada",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1465-VS",
        "title": "Developing a value set for the EQ-5D-5L in United Arab Emirates",
        "working_group": "Valuation, Populations and Health Systems"
      },
      {
        "project_id": "1696-RA",
        "title": "Measuring health-related quality of life using the EQ-5D-5L in the general population in Lebanon during the third worst socio-economic crisis in history",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1931-RA",
        "title": "Exploring the development, methodological quality, and applications of the EQ-5D population norms - Extending the EQ-POPs",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1974-VS",
        "title": "Comparative Study of TTO-based, Hybrid, and DCE with duration Value Sets for EQ-5D-5L in Qatar",
        "working_group": "Valuation"
      },
      {
        "project_id": "1984-RA",
        "title": "Examining the content validity of the EQ-HWB-Short, the EQ-5D-5L and five bolt-ons in older adults",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "20190050",
        "title": "panel presentation titled \"Putting Patients at the Centre of Health Care: The use of patient-reported outcome measures (PROMs) in the Healthcare System” for CAHSPR annual conference",
        "working_group": "Populations and Health Systems, Education and Outreach"
      },
      {
        "project_id": "2116-EOI",
        "title": "Joint North American EuroQol Regional meeting and 10th Annual APERSU End-user meeting",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2413-RA",
        "title": "Exploring differential item functioning in EQ-5D-5L, EQ-HWB, and PROMIS-10 using EQ-DAPHNIE data",
        "working_group": "Descriptive Systems, Populations and Health Systems, EQ-HWB"
      },
      {
        "project_id": "2487-TVG",
        "title": "Advancing EuroQol Research and Collaboration in Saudi Arabia: A Visit to King Saud University (KSU)",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2490-EO",
        "title": "Introduction to EuroQol Instruments and their various applications at the ISPOR UAE Chapter Annual conference",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2560-RA",
        "title": "Translation and cultural adaptation of 18 EQ-5D-5L bolt-ons into standard Arabic Language for the Kingdom of Saudi Arabia (KSA)",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "96-EO",
        "title": "Knowledge translation for the use of EQ-5D as a PROM for routine outcome measurement in health systems",
        "working_group": "Populations and Health Systems, Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5026033494",
      "display_name": "Fatima Al Sayah",
      "orcid": "0000-0003-3891-5452",
      "reported_affiliation": "University of Alberta",
      "works_count": 102,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 50
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 31
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 17
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 11
        },
        {
          "topic": "Health Literacy and Information Accessibility",
          "works": 10
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 9
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 6
        },
        {
          "topic": "Mobile Health and mHealth Applications",
          "works": 6
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 6
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 6
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 6
        },
        {
          "topic": "Mental Health and Patient Involvement",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jeffrey Johnson",
          "works": 67
        },
        {
          "name": "Arto Öhinmaa",
          "works": 30
        },
        {
          "name": "Sumit R. Majumdar",
          "works": 18
        },
        {
          "name": "Hilary Short",
          "works": 13
        },
        {
          "name": "Allison Soprovich",
          "works": 12
        },
        {
          "name": "Weiyu Qiu",
          "works": 11
        },
        {
          "name": "Sandra Rees",
          "works": 9
        },
        {
          "name": "Steven T. Johnson",
          "works": 8
        },
        {
          "name": "Markus Lahtinen",
          "works": 8
        },
        {
          "name": "Lisa Wozniak",
          "works": 7
        },
        {
          "name": "Xuejing Jin",
          "works": 6
        },
        {
          "name": "Beverly Williams",
          "works": 5
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
          "openalex_id": "W7159935463",
          "year": 2026,
          "title": "Factors associated with health state valuations: a secondary analysis of an EQ-5D-3L valuation study from Jordan",
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
          "openalex_id": "W7159974947",
          "year": 2026,
          "title": "The association of food insecurity with psychological distress and health-related quality of life in the general adult population of Lebanon",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Food Security and Health in Diverse Populations",
            "COVID-19 Pandemic Impacts",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W4406863862",
          "year": 2025,
          "title": "A Value Set for EQ-5D-5L in the United Arab Emirates",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 6,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
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
          "openalex_id": "W1994476685",
          "year": 2011,
          "title": "Arts-based methods in health research: A systematic review of the literature",
          "type": "review",
          "venue": "Arts & Health",
          "cited_by_count": 275,
          "topics": [
            "Art Therapy and Mental Health",
            "Participatory Visual Research Methods",
            "Empathy and Medical Education"
          ]
        },
        {
          "openalex_id": "W2071510397",
          "year": 2011,
          "title": "Population-level response shift: novel implications for research",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 7,
          "topics": [
            "Health disparities and outcomes",
            "Posttraumatic Stress Disorder Research",
            "Smoking Behavior and Cessation"
          ]
        },
        {
          "openalex_id": "W2264963030",
          "year": 2011,
          "title": "The Relationship between Health Promotion Counseling and Health Outcomes in Individuals with Chronic Conditions: Does Anxiety or Depression have a Role?",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Health and Wellbeing Research",
            "Health and Well-being Studies",
            "Education and Learning Interventions"
          ]
        },
        {
          "openalex_id": "W2037848969",
          "year": 2012,
          "title": "An Integrated Model of Health Literacy Using Diabetes as an Exemplar",
          "type": "article",
          "venue": "Canadian Journal of Diabetes",
          "cited_by_count": 33,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Mobile Health and mHealth Applications",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2030334027",
          "year": 2012,
          "title": "Health Literacy and Health Outcomes in Diabetes: A Systematic Review",
          "type": "review",
          "venue": "Journal of General Internal Medicine",
          "cited_by_count": 400,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Diabetes Management and Education",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2568974466",
          "year": 2017,
          "title": "Instrument-Defined Estimates of the Minimally Important Difference for EQ-5D-5L Index Scores",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 351,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2039295555",
          "year": 2014,
          "title": "Nursing perspectives on factors influencing interdisciplinary teamwork in the <scp>C</scp>anadian primary care setting",
          "type": "article",
          "venue": "Journal of Clinical Nursing",
          "cited_by_count": 124,
          "topics": [
            "Interprofessional Education and Collaboration",
            "Primary Care and Health Outcomes",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2164950742",
          "year": 2012,
          "title": "Health related quality of life measures in Arabic speaking populations: A systematic review on cross-cultural adaptation and measurement properties",
          "type": "review",
          "venue": "Quality of Life Research",
          "cited_by_count": 112,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2122141875",
          "year": 2012,
          "title": "Measuring Health Literacy in Individuals With Diabetes",
          "type": "article",
          "venue": "Health Education & Behavior",
          "cited_by_count": 105,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Diabetes Management and Education",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2795706072",
          "year": 2018,
          "title": "Minimally Important Difference of the EQ-5D-5L Index Score in Adults with Type 2 Diabetes",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 99,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Education",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W3205389994",
          "year": 2021,
          "title": "Selection of patient-reported outcome measures (PROMs) for use in health systems",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 91,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care"
          ]
        }
      ]
    }
  }
]
