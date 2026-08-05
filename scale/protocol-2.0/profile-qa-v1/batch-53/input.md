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
    "name": "Xin Zhang",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1972-RA",
        "title": "Assessing Validity, Test-retest Reliability and Responsiveness of EQ-5D-5L with Bolt-ons in Patients with Atopic Dermatitis in China: A Mixed-methods study",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2649-EO",
        "title": "Travel scholarship application to present EQ-5D-5L and EQ-HWB-9 study findings at ISOQOL 33rd Annual Conference 2026",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5100427821",
      "display_name": "Lixin Zhang",
      "orcid": "0000-0003-0894-9520",
      "reported_affiliation": "University of Science and Technology Liaoning",
      "works_count": 1119,
      "top_topics": [
        {
          "topic": "Microbial Natural Products and Biosynthesis",
          "works": 148
        },
        {
          "topic": "Photosynthetic Processes and Mechanisms",
          "works": 64
        },
        {
          "topic": "Genomics and Phylogenetic Studies",
          "works": 53
        },
        {
          "topic": "Plant biochemistry and biosynthesis",
          "works": 40
        },
        {
          "topic": "Plant Stress Responses and Tolerance",
          "works": 37
        },
        {
          "topic": "Fungal Biology and Applications",
          "works": 34
        },
        {
          "topic": "Ovarian cancer diagnosis and treatment",
          "works": 32
        },
        {
          "topic": "Marine Sponges and Natural Products",
          "works": 31
        },
        {
          "topic": "Mitochondrial Function and Pathology",
          "works": 30
        },
        {
          "topic": "Microbial Metabolic Engineering and Bioproduction",
          "works": 30
        },
        {
          "topic": "RNA and protein synthesis mechanisms",
          "works": 28
        },
        {
          "topic": "CRISPR and Genetic Engineering",
          "works": 26
        }
      ],
      "frequent_coauthors": [
        {
          "name": "David Padua",
          "works": 243
        },
        {
          "name": "Xueting Liu",
          "works": 93
        },
        {
          "name": "Huanqin Dai",
          "works": 93
        },
        {
          "name": "Fuhang Song",
          "works": 61
        },
        {
          "name": "Biao Ren",
          "works": 57
        },
        {
          "name": "Michael Gerndt",
          "works": 54
        },
        {
          "name": "Davide Sangiorgi",
          "works": 54
        },
        {
          "name": "Anda Vlad",
          "works": 51
        },
        {
          "name": "Robert P. Edwards",
          "works": 46
        },
        {
          "name": "George C. Tseng",
          "works": 41
        },
        {
          "name": "Jingyu Zhang",
          "works": 40
        },
        {
          "name": "Esther Elishaev",
          "works": 39
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7154730567",
          "year": 2026,
          "title": "<i>Diaporthe</i> species associated with postharvest fruit rot of kiwifruit in Anhui province, China",
          "type": "article",
          "venue": "Plant Disease",
          "cited_by_count": 0,
          "topics": [
            "Plant Pathogens and Fungal Diseases",
            "Phytochemistry and biological activity of medicinal plants",
            "Essential Oils and Antimicrobial Activity"
          ]
        },
        {
          "openalex_id": "W4406840771",
          "year": 2026,
          "title": "A benchmark of expert-level academic questions to assess AI capabilities",
          "type": "article",
          "venue": "Nature",
          "cited_by_count": 15,
          "topics": [
            "Topic Modeling",
            "Natural Language Processing Techniques",
            "Explainable Artificial Intelligence (XAI)"
          ]
        },
        {
          "openalex_id": "W7170038325",
          "year": 2026,
          "title": "Comparative evaluation of tobacco germplasm reveals distinct lead accumulation and translocation patterns associated with stomatal responses, oxidative stress, cell death, and antioxidative defense",
          "type": "article",
          "venue": "Industrial Crops and Products",
          "cited_by_count": 0,
          "topics": [
            "Plant Stress Responses and Tolerance",
            "Heavy Metal Exposure and Toxicity",
            "Aluminum toxicity and tolerance in plants and animals"
          ]
        },
        {
          "openalex_id": "W7165204207",
          "year": 2026,
          "title": "CsWRKY33 Integrates Immune Signalling and Metabolic Reprogramming to Enhance Tea Plant Resistance Against <i>Colletotrichum camelliae</i>",
          "type": "article",
          "venue": "Plant Cell & Environment",
          "cited_by_count": 0,
          "topics": [
            "Plant Gene Expression Analysis",
            "Plant-Microbe Interactions and Immunity",
            "Plant biochemistry and biosynthesis"
          ]
        },
        {
          "openalex_id": "W4403556367",
          "year": 2026,
          "title": "Error Bounds of Median-of-Means Estimators with VC-Dimension",
          "type": "article",
          "venue": "Communications in Mathematics and Statistics",
          "cited_by_count": 0,
          "topics": [
            "Statistical Methods and Inference",
            "Control Systems and Identification",
            "Advanced Statistical Methods and Models"
          ]
        },
        {
          "openalex_id": "W7162083766",
          "year": 2026,
          "title": "From Discovery to Manufacturing: A Quantitative Review of Phosphonates and Strategies for High-Titer Production",
          "type": "article",
          "venue": "Microorganisms",
          "cited_by_count": 0,
          "topics": [
            "Organophosphorus compounds synthesis",
            "Enzyme Catalysis and Immobilization",
            "Biochemical and Molecular Research"
          ]
        },
        {
          "openalex_id": "W2013247420",
          "year": 1991,
          "title": "Carotenoids enhance gap junctional communication and inhibit lipid peroxidation in C3H/10T1/2 cells: relationship to their cancer chemopreventive action",
          "type": "article",
          "venue": "Carcinogenesis",
          "cited_by_count": 513,
          "topics": [
            "Antioxidant Activity and Oxidative Stress",
            "Free Radicals and Antioxidants",
            "Metal-Catalyzed Oxygenation Mechanisms"
          ]
        },
        {
          "openalex_id": "W1536077708",
          "year": 1992,
          "title": "Carotenoids up-regulate connexin43 gene expression independent of their provitamin A or antioxidant properties.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 329,
          "topics": [
            "Antioxidant Activity and Oxidative Stress",
            "Retinoids in leukemia and cellular processes",
            "Glutathione Transferases and Polymorphisms"
          ]
        },
        {
          "openalex_id": "W2146881541",
          "year": 1992,
          "title": "Inhibition of cellular transformation by triphenylmethane: a novel chemopreventive agent",
          "type": "article",
          "venue": "Carcinogenesis",
          "cited_by_count": 10,
          "topics": [
            "Synthesis of Organic Compounds",
            "Retinoids in leukemia and cellular processes",
            "Antioxidant Activity and Oxidative Stress"
          ]
        },
        {
          "openalex_id": "W2245488421",
          "year": 1992,
          "title": "Mechanistic studies of carotenoid cancer chemopreventive action in mammalian cell cultures : involvement of gap junctional communication and connexin43 gene expression",
          "type": "dissertation",
          "venue": "ScholarSpace (University of Hawaii at Manoa)",
          "cited_by_count": 0,
          "topics": [
            "Connexins and lens biology"
          ]
        },
        {
          "openalex_id": "W2504691963",
          "year": 2016,
          "title": "Sharing and community curation of mass spectrometry data with Global Natural Products Social Molecular Networking",
          "type": "article",
          "venue": "Nature Biotechnology",
          "cited_by_count": 4660,
          "topics": [
            "Metabolomics and Mass Spectrometry Studies",
            "Species Distribution and Climate Change",
            "Microbial Community Ecology and Physiology"
          ]
        },
        {
          "openalex_id": "W3023986730",
          "year": 2020,
          "title": "SARS-CoV-2 infection of the liver directly contributes to hepatic impairment in patients with COVID-19",
          "type": "article",
          "venue": "Journal of Hepatology",
          "cited_by_count": 637,
          "topics": [
            "COVID-19 Clinical Research Studies",
            "Dermatological and COVID-19 studies",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W2144591886",
          "year": 2004,
          "title": "Superconductivity Modulated by Quantum Size Effects",
          "type": "article",
          "venue": "Science",
          "cited_by_count": 614,
          "topics": [
            "Surface and Thin Film Phenomena",
            "Physics of Superconductivity and Magnetism",
            "Semiconductor materials and devices"
          ]
        },
        {
          "openalex_id": "W1966156878",
          "year": 2013,
          "title": "Molecular Networking as a Dereplication Strategy",
          "type": "article",
          "venue": "Journal of Natural Products",
          "cited_by_count": 584,
          "topics": [
            "Metabolomics and Mass Spectrometry Studies",
            "Mass Spectrometry Techniques and Applications",
            "Analytical Chemistry and Chromatography"
          ]
        },
        {
          "openalex_id": "W2097849024",
          "year": 2013,
          "title": "The Identification and Characterization of Breast Cancer CTCs Competent for Brain Metastasis",
          "type": "article",
          "venue": "Science Translational Medicine",
          "cited_by_count": 517,
          "topics": [
            "Cancer Cells and Metastasis",
            "Brain Metastases and Treatment",
            "Cancer Genomics and Diagnostics"
          ]
        },
        {
          "openalex_id": "W2091614177",
          "year": 2013,
          "title": "Effects of actinobacteria on plant disease suppression and growth promotion",
          "type": "article",
          "venue": "Applied Microbiology and Biotechnology",
          "cited_by_count": 464,
          "topics": [
            "Plant-Microbe Interactions and Immunity",
            "Mycorrhizal Fungi and Plant Interactions",
            "Plant Pathogens and Fungal Diseases"
          ]
        },
        {
          "openalex_id": "W4238526656",
          "year": 2015,
          "title": "CRISPR-Cas9 Based Engineering of Actinomycetal Genomes",
          "type": "article",
          "venue": "ACS Synthetic Biology",
          "cited_by_count": 440,
          "topics": [
            "CRISPR and Genetic Engineering",
            "RNA and protein synthesis mechanisms",
            "Genomics and Phylogenetic Studies"
          ]
        }
      ]
    }
  },
  {
    "name": "Xuejing Jin",
    "member_affiliation": "Beijing University of Chinese Medicine",
    "is_member": true,
    "projects": [
      {
        "project_id": "217-EO",
        "title": "Promoting and Supporting the use of EQ-5D instruments in China",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "318-RA",
        "title": "Measurement properties of the EQ-5D-5L among non-small cell lung cancer patients on active treatments in China",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5008581679",
      "display_name": "Xuejing Jin",
      "orcid": "0000-0003-3513-2364",
      "reported_affiliation": "Beijing University of Chinese Medicine",
      "works_count": 61,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 22
        },
        {
          "topic": "Acute Ischemic Stroke Management",
          "works": 7
        },
        {
          "topic": "Stroke Rehabilitation and Recovery",
          "works": 7
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 6
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 6
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 5
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 4
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 4
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 4
        },
        {
          "topic": "Ovarian function and disorders",
          "works": 4
        },
        {
          "topic": "Neurofibromatosis and Schwannoma Cases",
          "works": 4
        },
        {
          "topic": "Intensive Care Unit Cognitive Disorders",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Feng Xie",
          "works": 15
        },
        {
          "name": "Hongchao Li",
          "works": 10
        },
        {
          "name": "Weiping Sun",
          "works": 9
        },
        {
          "name": "Lehana Thabane",
          "works": 8
        },
        {
          "name": "Luying Wang",
          "works": 8
        },
        {
          "name": "Pingping Li",
          "works": 8
        },
        {
          "name": "Min Zhao",
          "works": 8
        },
        {
          "name": "Yining Huang",
          "works": 8
        },
        {
          "name": "Haijing Guan",
          "works": 7
        },
        {
          "name": "Gordon Guyatt",
          "works": 7
        },
        {
          "name": "Fatima Al Sayah",
          "works": 6
        },
        {
          "name": "Jeffrey Johnson",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7158728065",
          "year": 2026,
          "title": "Additional file 1 of Interpreting patient-reported outcomes after ischemic stroke: defining minimal important difference in EQ-5D across recovery phases",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W7158741860",
          "year": 2026,
          "title": "Additional file 1 of Interpreting patient-reported outcomes after ischemic stroke: defining minimal important difference in EQ-5D across recovery phases",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W7158689349",
          "year": 2026,
          "title": "Additional file 2 of Interpreting patient-reported outcomes after ischemic stroke: defining minimal important difference in EQ-5D across recovery phases",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W7159071154",
          "year": 2026,
          "title": "Additional file 2 of Interpreting patient-reported outcomes after ischemic stroke: defining minimal important difference in EQ-5D across recovery phases",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W7139983302",
          "year": 2026,
          "title": "Interpreting patient-reported outcomes after ischemic stroke: defining minimal important difference in EQ-5D across recovery phases",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Acute Ischemic Stroke Management",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W7158479359",
          "year": 2026,
          "title": "Interpreting patient-reported outcomes after ischemic stroke: defining minimal important difference in EQ-5D across recovery phases",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W2106259262",
          "year": 2015,
          "title": "Is bad living better than good death? Impact of demographic and cultural factors on health state preference",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 37,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2465326294",
          "year": 2016,
          "title": "Economic and Humanistic Burden of Osteoarthritis: A Systematic Review of Large Sample Studies",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 201,
          "topics": [
            "Osteoarthritis Treatment and Mechanisms",
            "Total Knee Arthroplasty Outcomes",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2550958125",
          "year": 2016,
          "title": "SELF-REPORTED HEALTH STATUS AMONG TYPE 2 DIABETIC PATIENTS: A COMMUNITY-BASED SURVEY IN CHINA",
          "type": "article",
          "venue": "38th Annual North American Meeting of the Society for Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Cardiovascular Health and Risk Factors",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W4210720738",
          "year": 2017,
          "title": "A Computer-Assisted Personal Interview App in Research Electronic Data Capture for Administering Time Trade-off Surveys (REDCap): Development and Pretest (Preprint)",
          "type": "preprint",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2587471491",
          "year": 2017,
          "title": "Estimating an EQ-5D-5L Value Set for China",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 737,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W3033943032",
          "year": 2020,
          "title": "Evaluating the credibility of anchor based estimates of minimal important differences for patient reported outcomes: instrument development and reliability study",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 273,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Total Knee Arthroplasty Outcomes",
            "Meta-analysis and systematic reviews"
          ]
        },
        {
          "openalex_id": "W2894738161",
          "year": 2018,
          "title": "Evaluating Progression-Free Survival as a Surrogate Outcome for Health-Related Quality of Life in Oncology",
          "type": "article",
          "venue": "JAMA Internal Medicine",
          "cited_by_count": 144,
          "topics": [
            "Cancer survivorship and care",
            "Cancer Treatment and Pharmacology",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W3111011457",
          "year": 2020,
          "title": "Minimal important difference estimates for patient-reported outcomes: A systematic survey",
          "type": "article",
          "venue": "Journal of Clinical Epidemiology",
          "cited_by_count": 125,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Meta-analysis and systematic reviews"
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
        },
        {
          "openalex_id": "W4309264997",
          "year": 2022,
          "title": "Estimating an EQ-5D-Y-3L Value Set for China",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 65,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W3094596778",
          "year": 2020,
          "title": "Berberine for diarrhea in children and adults: a systematic review and meta-analysis",
          "type": "review",
          "venue": "Therapeutic Advances in Gastroenterology",
          "cited_by_count": 50,
          "topics": [
            "Berberine and alkaloids research",
            "Vibrio bacteria research studies",
            "Diphtheria, Corynebacterium, and Tetanus"
          ]
        }
      ]
    }
  },
  {
    "name": "Yan Feng",
    "member_affiliation": "Queen Mary University of London",
    "is_member": true,
    "projects": [
      {
        "project_id": "1650-RA",
        "title": "Developing a function to map EQ-5D-Y-5L to EQ-5D-Y-3L",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2015090",
        "title": "Revisiting the MVH study: new methods for modelling UK valuations for the EQ-5D-3L",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015330",
        "title": "Exploring the inconsistent ordering of levels of the EQ-5D-5L value set - Are England and China different?",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016330",
        "title": "Understanding the relationship between clinical quality of primary care and patient self-reported health on the EQ-5D in England",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20180740",
        "title": "What contributes to variations in self-reported health for the general population and for ten condition-specific patient groups in England? - An empirical analysis using repeated cross-sectional general practice data with 2.9 million patient records.",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5053760337",
      "display_name": "Feng Yan",
      "orcid": "0000-0001-8663-6859",
      "reported_affiliation": "State Key Laboratory of Hydrology-Water Resources and Hydraulic Engineering",
      "works_count": 544,
      "top_topics": [
        {
          "topic": "Neuroinflammation and Neurodegeneration Mechanisms",
          "works": 51
        },
        {
          "topic": "Intracerebral and Subarachnoid Hemorrhage Research",
          "works": 47
        },
        {
          "topic": "Helicobacter pylori-related gastroenterology studies",
          "works": 37
        },
        {
          "topic": "Acute Ischemic Stroke Management",
          "works": 29
        },
        {
          "topic": "Intracranial Aneurysms: Treatment and Complications",
          "works": 23
        },
        {
          "topic": "MicroRNA in disease regulation",
          "works": 21
        },
        {
          "topic": "Neurological Disease Mechanisms and Treatments",
          "works": 19
        },
        {
          "topic": "Cancer Immunotherapy and Biomarkers",
          "works": 19
        },
        {
          "topic": "Traumatic Brain Injury and Neurovascular Disturbances",
          "works": 16
        },
        {
          "topic": "Immune cells in cancer",
          "works": 14
        },
        {
          "topic": "Cancer-related molecular mechanisms research",
          "works": 14
        },
        {
          "topic": "Epigenetics and DNA Methylation",
          "works": 13
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Xunming Ji",
          "works": 62
        },
        {
          "name": "Gao Chen",
          "works": 58
        },
        {
          "name": "Jianru Li",
          "works": 46
        },
        {
          "name": "James G. Fox",
          "works": 44
        },
        {
          "name": "Yumin Luo",
          "works": 43
        },
        {
          "name": "Zhongming Ge",
          "works": 28
        },
        {
          "name": "Haiping Zhao",
          "works": 28
        },
        {
          "name": "Rongliang Wang",
          "works": 28
        },
        {
          "name": "Hang Zhou",
          "works": 27
        },
        {
          "name": "Yucong Peng",
          "works": 25
        },
        {
          "name": "Lin Wang",
          "works": 25
        },
        {
          "name": "Chi Gu",
          "works": 25
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7127348560",
          "year": 2026,
          "title": "An agentic framework turns patient-sourced records into a multimodal map of ALS heterogeneity",
          "type": "preprint",
          "venue": "bioRxiv (Cold Spring Harbor Laboratory)",
          "cited_by_count": 0,
          "topics": [
            "Amyotrophic Lateral Sclerosis Research",
            "Genomics and Rare Diseases",
            "Epigenetics and DNA Methylation"
          ]
        },
        {
          "openalex_id": "W7127071873",
          "year": 2026,
          "title": "Climate change intensifies carbon emissions from the Earth's Third Pole: Projected trajectories of soil and ecosystem respiration",
          "type": "article",
          "venue": "Global and Planetary Change",
          "cited_by_count": 2,
          "topics": [
            "Climate change and permafrost",
            "Soil Carbon and Nitrogen Dynamics",
            "Cryospheric studies and observations"
          ]
        },
        {
          "openalex_id": "W7134173435",
          "year": 2026,
          "title": "Retraction Notice to “ErbB4 protects against neuronal apoptosis via activation of YAP/PIK3CB signaling pathway in a rat model of subarachnoid hemorrhage” [Experimental Neurology 297 (2017) 92–100].",
          "type": "retraction",
          "venue": "Experimental Neurology",
          "cited_by_count": 0,
          "topics": [
            "Hippo pathway signaling and YAP/TAZ",
            "Axon Guidance and Neuronal Signaling",
            "14-3-3 protein interactions"
          ]
        },
        {
          "openalex_id": "W4408796507",
          "year": 2025,
          "title": "1426 Tucatinib (HER2 Tyrosine Kinase Inhibitor)-Induced Liver Injury",
          "type": "article",
          "venue": "Laboratory Investigation",
          "cited_by_count": 1,
          "topics": [
            "Lung Cancer Treatments and Mutations",
            "Melanoma and MAPK Pathways",
            "PI3K/AKT/mTOR signaling in cancer"
          ]
        },
        {
          "openalex_id": "W4408089818",
          "year": 2025,
          "title": "A Preliminary Study of Effect of Melatonin on Inflammation and Hypoxia‐Related Factors in a Mouse Model of Elastase‐Induced Intracranial Aneurysm",
          "type": "article",
          "venue": "Brain and Behavior",
          "cited_by_count": 0,
          "topics": [
            "Neuroinflammation and Neurodegeneration Mechanisms",
            "Kruppel-like factors research",
            "Cerebrovascular and genetic disorders"
          ]
        },
        {
          "openalex_id": "W4415950162",
          "year": 2025,
          "title": "Aberrant 5-Methylcytosine tRNA Modification Disrupts Proteostasis and Exacerbates Age-Related Osteoporosis",
          "type": "preprint",
          "venue": "bioRxiv (Cold Spring Harbor Laboratory)",
          "cited_by_count": 0,
          "topics": [
            "RNA modifications and cancer",
            "Ubiquitin and proteasome pathways",
            "Cancer-related gene regulation"
          ]
        },
        {
          "openalex_id": "W2738295680",
          "year": 1989,
          "title": "Studies on The Calypterate flies in West Sichuan,China.IV.Preliminary observation on The Diurnal and Nocturnal Activity of Musca domestica Linnaeus in Yaan",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Insect and Arachnid Ecology and Behavior",
            "Orthoptera Research and Taxonomy",
            "Botany and Plant Ecology Studies"
          ]
        },
        {
          "openalex_id": "W2380925904",
          "year": 1994,
          "title": "The effects of adenosine on cellular immunity",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Pediatric health and respiratory diseases",
            "Adenosine and Purinergic Signaling",
            "Immune Cell Function and Interaction"
          ]
        },
        {
          "openalex_id": "W2356316330",
          "year": 1995,
          "title": "Effects of dipyridamole on murine immunity",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Nanoparticle-Based Drug Delivery",
            "Neuropeptides and Animal Physiology",
            "Advanced Drug Delivery Systems"
          ]
        },
        {
          "openalex_id": "W2051274297",
          "year": 1997,
          "title": "Inhibition of LPS-induced TNF-α production by calcitonin gene-related peptide (CGRP) in cultured mouse peritoneal macrophages",
          "type": "article",
          "venue": "Life Sciences",
          "cited_by_count": 60,
          "topics": [
            "Neuropeptides and Animal Physiology",
            "Hypothalamic control of reproductive hormones",
            "Hormonal Regulation and Hypertension"
          ]
        },
        {
          "openalex_id": "W4384820644",
          "year": 2023,
          "title": "China stroke surveillance report 2021",
          "type": "article",
          "venue": "Military Medical Research",
          "cited_by_count": 546,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Neurological Disease Mechanisms and Treatments",
            "Healthcare Systems and Practices"
          ]
        },
        {
          "openalex_id": "W2143626786",
          "year": 1998,
          "title": "Hepatic Helicobacter species identified in bile and gallbladder tissue from chileans with chronic cholecystitis",
          "type": "article",
          "venue": "Gastroenterology",
          "cited_by_count": 505,
          "topics": [
            "Helicobacter pylori-related gastroenterology studies",
            "Gastric Cancer Management and Outcomes",
            "Phytochemistry and biological activities of Ficus species"
          ]
        },
        {
          "openalex_id": "W3031532038",
          "year": 2020,
          "title": "TREM2 activation attenuates neuroinflammation and neuronal apoptosis via PI3K/Akt pathway after intracerebral hemorrhage in mice",
          "type": "article",
          "venue": "Journal of Neuroinflammation",
          "cited_by_count": 374,
          "topics": [
            "Neuroinflammation and Neurodegeneration Mechanisms",
            "Inflammation biomarkers and pathways",
            "Intracerebral and Subarachnoid Hemorrhage Research"
          ]
        },
        {
          "openalex_id": "W2106136875",
          "year": 2013,
          "title": "Gastric colonisation with a restricted commensal microbiota replicates the promotion of neoplastic lesions by diverse intestinal microbiota in the <i>Helicobacter pylori</i> INS-GAS mouse model of gastric carcinogenesis",
          "type": "article",
          "venue": "Gut",
          "cited_by_count": 288,
          "topics": [
            "Helicobacter pylori-related gastroenterology studies",
            "Gut microbiota and health",
            "Immune cells in cancer"
          ]
        },
        {
          "openalex_id": "W1993391636",
          "year": 2013,
          "title": "Global chromatin profiling reveals NSD2 mutations in pediatric acute lymphoblastic leukemia",
          "type": "article",
          "venue": "Nature Genetics",
          "cited_by_count": 285,
          "topics": [
            "Acute Lymphoblastic Leukemia research",
            "Epigenetics and DNA Methylation",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W2794292604",
          "year": 2018,
          "title": "An overview of graphene-based hydroxyapatite composites for orthopedic applications",
          "type": "article",
          "venue": "Bioactive Materials",
          "cited_by_count": 240,
          "topics": [
            "Graphene and Nanomaterials Applications",
            "Bone Tissue Engineering Materials",
            "Nanoparticles: synthesis and applications"
          ]
        },
        {
          "openalex_id": "W2183144139",
          "year": 2016,
          "title": "Nivolumab dose selection: challenges, opportunities, and lessons learned for cancer immunotherapy",
          "type": "article",
          "venue": "Journal for ImmunoTherapy of Cancer",
          "cited_by_count": 214,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Immunotherapy and Immune Responses",
            "CAR-T cell therapy research"
          ]
        },
        {
          "openalex_id": "W2988708112",
          "year": 2019,
          "title": "Prevalence and risk factors for dyslipidemia among adults in rural and urban China: findings from the China National Stroke Screening and prevention project (CNSSPP)",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 211,
          "topics": [
            "Lipoproteins and Cardiovascular Health",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Adipokines, Inflammation, and Metabolic Diseases"
          ]
        }
      ]
    }
  },
  {
    "name": "Yap Xin Yi",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2290-EO",
        "title": "Evaluating Performance of the Experimental EQ-TIPS (V3) for Assessing Infants and Toddlers with Acute Infections: A Mixed-Methods Approach of Cognitive Debriefing and Psychometric Testing",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5058382403",
      "display_name": "Yajun Yi",
      "orcid": "0000-0002-7135-6325",
      "reported_affiliation": "Beijing Children’s Hospital",
      "works_count": 79,
      "top_topics": [
        {
          "topic": "Prostate Cancer Treatment and Research",
          "works": 20
        },
        {
          "topic": "Cancer-related molecular mechanisms research",
          "works": 17
        },
        {
          "topic": "NF-κB Signaling Pathways",
          "works": 12
        },
        {
          "topic": "Head and Neck Cancer Studies",
          "works": 12
        },
        {
          "topic": "Cancer, Lipids, and Metabolism",
          "works": 10
        },
        {
          "topic": "Gene expression and cancer classification",
          "works": 9
        },
        {
          "topic": "Bioinformatics and Genomic Networks",
          "works": 7
        },
        {
          "topic": "Molecular Biology Techniques and Applications",
          "works": 6
        },
        {
          "topic": "Hormonal and reproductive studies",
          "works": 4
        },
        {
          "topic": "Peptidase Inhibition and Analysis",
          "works": 4
        },
        {
          "topic": "Breast Cancer Treatment Studies",
          "works": 3
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Robert J. Matusik",
          "works": 24
        },
        {
          "name": "Peter E. Clark",
          "works": 16
        },
        {
          "name": "Robbert J.C. Slebos",
          "works": 15
        },
        {
          "name": "Kim Ely",
          "works": 15
        },
        {
          "name": "Yu Shyr",
          "works": 15
        },
        {
          "name": "Wendell G. Yarbrough",
          "works": 15
        },
        {
          "name": "Christine H. Chung",
          "works": 15
        },
        {
          "name": "Jesse Carter",
          "works": 14
        },
        {
          "name": "Anthony J. Cmelak",
          "works": 14
        },
        {
          "name": "Shawn Levy",
          "works": 14
        },
        {
          "name": "Renjie Jin",
          "works": 14
        },
        {
          "name": "Magdalena M. Grabowska",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7168158751",
          "year": 2026,
          "title": "Novel <i>NPR2</i> heterozygous variant in a familial short stature and the therapeutic response to rhGH: a case report",
          "type": "article",
          "venue": "Journal of Pediatric Endocrinology and Metabolism",
          "cited_by_count": 0,
          "topics": [
            "Connective tissue disorders research",
            "Genetic Syndromes and Imprinting",
            "Growth Hormone and Insulin-like Growth Factors"
          ]
        },
        {
          "openalex_id": "W4415257910",
          "year": 2025,
          "title": "Development of a polyclonal antibody against the protein encoded by the metabolic syndrome-associated gene for dissecting its function and underlying mechanism",
          "type": "article",
          "venue": "Biochimica et Biophysica Acta (BBA) - General Subjects",
          "cited_by_count": 0,
          "topics": [
            "Microbial Metabolic Engineering and Bioproduction",
            "Endoplasmic Reticulum Stress and Disease",
            "Pancreatic function and diabetes"
          ]
        },
        {
          "openalex_id": "W4417479813",
          "year": 2025,
          "title": "EPH92 Evaluating Performance of the Experimental EQ-TIPS (V3) for Assessing Infants and Toddlers With Acute Infections: A Mixed-Methods Approach of Cognitive Debriefing and Psychometric Testing",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Infant Development and Preterm Care",
            "Childhood Cancer Survivors' Quality of Life",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        },
        {
          "openalex_id": "W4410866236",
          "year": 2025,
          "title": "Epidemiology of Overweight and Obesity in Early Childhood in China and Associated Factors",
          "type": "article",
          "venue": "Diabetes Metabolic Syndrome and Obesity",
          "cited_by_count": 2,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Cancer Research and Treatment",
            "Child Nutrition and Feeding Issues"
          ]
        },
        {
          "openalex_id": "W4415072916",
          "year": 2025,
          "title": "Hospital readmission disparity measure for evaluating hospital performance and penalties",
          "type": "article",
          "venue": "Archives of Public Health",
          "cited_by_count": 0,
          "topics": [
            "Heart Failure Treatment and Management",
            "Frailty in Older Adults",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4415085636",
          "year": 2025,
          "title": "[Study of the effect of self-perceived hearing status on depression in middle-aged and older people in the community].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Health and Well-being Studies"
          ]
        },
        {
          "openalex_id": "W2170129784",
          "year": 2000,
          "title": "Regulatory Defects in Cbl and Mitogen-Activated Protein Kinase (Extracellular Signal-Related Kinase) Pathways Cause Persistent Hyperexpression of CD40 Ligand in Human Lupus T Cells",
          "type": "article",
          "venue": "The Journal of Immunology",
          "cited_by_count": 92,
          "topics": [
            "T-cell and B-cell Immunology",
            "Immune Cell Function and Interaction",
            "Signaling Pathways in Disease"
          ]
        },
        {
          "openalex_id": "W2022768816",
          "year": 2002,
          "title": "A Novel Gene Encoding a TIG Multiple Domain Protein Is a Positional Candidate for Autosomal Recessive Polycystic Kidney Disease",
          "type": "article",
          "venue": "Genomics",
          "cited_by_count": 73,
          "topics": [
            "Genetic and Kidney Cyst Diseases",
            "Renal and related cancers",
            "Renal Diseases and Glomerulopathies"
          ]
        },
        {
          "openalex_id": "W2049121222",
          "year": 2004,
          "title": "Comparative Sequence and X-Inactivation Analyses of a Domain of Escape in Human Xp11.2 and the Conserved Segment in Mouse",
          "type": "preprint",
          "venue": "Genome Research",
          "cited_by_count": 58,
          "topics": [
            "Genetic and Clinical Aspects of Sex Determination and Chromosomal Abnormalities",
            "RNA and protein synthesis mechanisms",
            "Immune Cell Function and Interaction"
          ]
        },
        {
          "openalex_id": "W2010720008",
          "year": 2004,
          "title": "Human lupus T cells resist inactivation and escape death by upregulating COX-2",
          "type": "article",
          "venue": "Nature Medicine",
          "cited_by_count": 139,
          "topics": [
            "Bioactive Compounds and Antitumor Agents",
            "Inflammatory mediators and NSAID effects",
            "Cytokine Signaling Pathways and Interactions"
          ]
        },
        {
          "openalex_id": "W2139376220",
          "year": 2006,
          "title": "Gene Expression Differences Associated with Human Papillomavirus Status in Head and Neck Squamous Cell Carcinoma",
          "type": "article",
          "venue": "Clinical Cancer Research",
          "cited_by_count": 316,
          "topics": [
            "Molecular Biology Techniques and Applications",
            "Cancer-related Molecular Pathways",
            "Genomics and Chromatin Dynamics"
          ]
        },
        {
          "openalex_id": "W2101965347",
          "year": 2006,
          "title": "Gene Expression Profiles Identify Epithelial-to-Mesenchymal Transition and Activation of Nuclear Factor-κB Signaling as Characteristics of a High-risk Head and Neck Squamous Cell Carcinoma",
          "type": "article",
          "venue": "Cancer Research",
          "cited_by_count": 249,
          "topics": [
            "NF-κB Signaling Pathways",
            "Cancer-related molecular mechanisms research",
            "Cancer-related gene regulation"
          ]
        },
        {
          "openalex_id": "W2168850532",
          "year": 2005,
          "title": "Molecular Alterations in Primary Prostate Cancer after Androgen Ablation Therapy",
          "type": "article",
          "venue": "Clinical Cancer Research",
          "cited_by_count": 186,
          "topics": [
            "Prostate Cancer Treatment and Research",
            "Prostate Cancer Diagnosis and Treatment",
            "Breast Cancer Treatment Studies"
          ]
        },
        {
          "openalex_id": "W2071593083",
          "year": 2012,
          "title": "Altered microRNA expression associated with chromosomal changes contributes to cervical carcinogenesis",
          "type": "article",
          "venue": "Oncogene",
          "cited_by_count": 185,
          "topics": [
            "MicroRNA in disease regulation",
            "Cancer-related molecular mechanisms research",
            "Circular RNAs in diseases"
          ]
        },
        {
          "openalex_id": "W2015009117",
          "year": 2014,
          "title": "NF-κB Gene Signature Predicts Prostate Cancer Progression",
          "type": "article",
          "venue": "Cancer Research",
          "cited_by_count": 116,
          "topics": [
            "NF-κB Signaling Pathways",
            "Cancer-related molecular mechanisms research",
            "Prostate Cancer Treatment and Research"
          ]
        },
        {
          "openalex_id": "W1900346306",
          "year": 2012,
          "title": "Integrin-Associated CD151 Drives ErbB2-Evoked Mammary Tumor Onset and Metastasis",
          "type": "article",
          "venue": "Neoplasia",
          "cited_by_count": 97,
          "topics": [
            "Cell Adhesion Molecules Research",
            "Platelet Disorders and Treatments",
            "Caveolin-1 and cellular processes"
          ]
        }
      ]
    }
  },
  {
    "name": "Yared Belete Belay",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1846-EO",
        "title": "Travel Grant Application for the 2024 ISPOR Meeting in Atlanta GA, USA-Yared Belete Belay",
        "working_group": "Dissemination, OA fee, Others"
      },
      {
        "project_id": "229-RA",
        "title": "Examining the psychometric properties of a split version of the EQ-5D-5L anxiety/depression dimension in patients with anxiety and/or depression",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "323-RA",
        "title": "Disabled people and other stakeholders’ perspectives on the feasibility, acceptability and content validity of EQ-5D-5L. A qualitative study in low-income setting",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "327-RA",
        "title": "A qualitative study on respondent’s interpretation of the EQ-VAS in Ethiopia",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "79-RA",
        "title": "The psychometric properties, feasibility and usefulness of the EQ-5D-5L in Ethiopian stroke patients- A mixed-methods longitudinal study",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5086002810",
      "display_name": "Yared Belete Belay",
      "orcid": "0000-0001-5473-3857",
      "reported_affiliation": "Monash Health",
      "works_count": 33,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 5
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 4
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 3
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 3
        },
        {
          "topic": "Schizophrenia research and treatment",
          "works": 3
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 3
        },
        {
          "topic": "HIV-related health complications and treatments",
          "works": 2
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 2
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 2
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 2
        },
        {
          "topic": "Bipolar Disorder and Treatment",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Lidia Engel",
          "works": 8
        },
        {
          "name": "Cathrine Mihalopoulos",
          "works": 6
        },
        {
          "name": "Hedayat Abbastabar",
          "works": 4
        },
        {
          "name": "Vahid Alipour",
          "works": 4
        },
        {
          "name": "Nelson Alvis‐Guzmán",
          "works": 4
        },
        {
          "name": "Mina Anjomshoa",
          "works": 4
        },
        {
          "name": "Jalal Arabloo",
          "works": 4
        },
        {
          "name": "Olatunde Aremu",
          "works": 4
        },
        {
          "name": "Martin Amogre Ayanore",
          "works": 4
        },
        {
          "name": "Mojtaba Bagherzadeh",
          "works": 4
        },
        {
          "name": "Ali Bijani",
          "works": 4
        },
        {
          "name": "Terefe Teshome Kassa",
          "works": 4
        }
      ],
      "work_examples": [
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
          "openalex_id": "W7167727387",
          "year": 2026,
          "title": "The Cost Effectiveness of Treatment Strategies for Depression in Ethiopia: A Multiple Cohort Markov Model Analysis",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Mental Health Treatment and Access",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Treatment of Major Depression"
          ]
        },
        {
          "openalex_id": "W7161954143",
          "year": 2026,
          "title": "Updated trends in the global prevalence and burden of mental disorders, 1990–2023: a systematic analysis for the Global Burden of Disease Study 2023",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 12,
          "topics": [
            "Mental Health Treatment and Access",
            "Bipolar Disorder and Treatment",
            "Schizophrenia research and treatment"
          ]
        },
        {
          "openalex_id": "W7163215745",
          "year": 2026,
          "title": "Updated trends in the global prevalence and burden of mental disorders, 1990–2023: a systematic analysis for the Global Burden of Disease Study 2023",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Schizophrenia research and treatment",
            "Bipolar Disorder and Treatment",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W4413111549",
          "year": 2025,
          "title": "Psychometric evaluation of the EQ-5D-Y-3L in Ethiopian pediatric inpatients: comparing self and proxy reports",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W4411746668",
          "year": 2025,
          "title": "The Psychometric Performance of Generic Preference-Based Measures in Informal Carers: A Systematic Review of Validation Studies",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Intergenerational Family Dynamics and Caregiving",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W2431674130",
          "year": 2016,
          "title": "Influence of Medical Representatives on Prescribing Practices in Mekelle, Northern Ethiopia",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 47,
          "topics": [
            "Pharmaceutical industry and healthcare",
            "Antibiotic Use and Resistance",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2521129886",
          "year": 2016,
          "title": "Job satisfaction among community pharmacy professionals in Mekelle city, Northern Ethiopia",
          "type": "article",
          "venue": "Advances in Medical Education and Practice",
          "cited_by_count": 19,
          "topics": [
            "Nursing education and management",
            "Global and Cross-Cultural Management",
            "Educational Management and Quality"
          ]
        },
        {
          "openalex_id": "W2766003591",
          "year": 2017,
          "title": "A study of personality disorders among patients with somatization disorder",
          "type": "article",
          "venue": "Egyptian Journal of Psychiatry",
          "cited_by_count": 0,
          "topics": [
            "Personality Disorders and Psychopathology",
            "Psychotherapy Techniques and Applications",
            "Psychosomatic Disorders and Their Treatments"
          ]
        },
        {
          "openalex_id": "W2767529661",
          "year": 2017,
          "title": "Assessment of Drug-Drug Interaction in Ayder Comprehensive Specialized Hospital, Mekelle, Northern Ethiopia: A Retrospective Study",
          "type": "article",
          "venue": "BioMed Research International",
          "cited_by_count": 18,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Antibiotic Use and Resistance",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W3211488171",
          "year": 2019,
          "title": "Global, Regional, and National Cancer Incidence, Mortality, Years of Life Lost, Years Lived With Disability, and Disability-Adjusted Life-Years for 29 Cancer Groups, 1990 to 2017",
          "type": "article",
          "venue": "JAMA Oncology",
          "cited_by_count": 2680,
          "topics": [
            "Global Cancer Incidence and Screening",
            "COVID-19 and healthcare impacts",
            "Hematological disorders and diagnostics"
          ]
        },
        {
          "openalex_id": "W2969635519",
          "year": 2019,
          "title": "Global, regional, and national incidence, prevalence, and mortality of HIV, 1980–2017, and forecasts to 2030, for 195 countries and territories: a systematic analysis for the Global Burden of Diseases, Injuries, and Risk Factors Study 2017",
          "type": "article",
          "venue": "The Lancet HIV",
          "cited_by_count": 587,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV Research and Treatment",
            "HIV-related health complications and treatments"
          ]
        },
        {
          "openalex_id": "W2941926021",
          "year": 2019,
          "title": "Past, present, and future of global health financing: a review of development assistance, government, out-of-pocket, and other private spending on health for 195 countries, 1995–2050",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 534,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Public Health Policies and Epidemiology",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2980608708",
          "year": 2019,
          "title": "Mapping 123 million neonatal, infant and child deaths between 2000 and 2017",
          "type": "article",
          "venue": "Nature",
          "cited_by_count": 278,
          "topics": [
            "Global Maternal and Child Health",
            "Maternal and Neonatal Healthcare",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W3124039690",
          "year": 2021,
          "title": "Health-related quality of life of patients with HIV/AIDS at a tertiary care teaching hospital in Ethiopia",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 26,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "HIV/AIDS Research and Interventions",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4362734318",
          "year": 2023,
          "title": "Health-related quality of life in children, adolescents and young adults with self-harm or suicidality: A systematic review",
          "type": "review",
          "venue": "Australian & New Zealand Journal of Psychiatry",
          "cited_by_count": 24,
          "topics": [
            "Suicide and Self-Harm Studies",
            "Child and Adolescent Psychosocial and Emotional Development",
            "COVID-19 and Mental Health"
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
        }
      ]
    }
  }
]
