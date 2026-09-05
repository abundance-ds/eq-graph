# Coverage map for Q1-Q100

## Meaning of the dependency labels

- `Content`: EuroQol study content from the ontology core.
- `Portfolio`: projects, awards, working groups, and accepted project-output links.
- `People`: resolved people, roles, memberships, authorship, and affiliations.
- `Corpus`: publication metadata, inclusion decisions, source lineage, and corpus snapshots.
- `Scholarly`: references, citations, open access, venues, and external topics with dated sources.
- `Registry`: a complete current instrument or value-set registry.
- `Analytic`: a declared calculation over one data snapshot.
- `Rule`: a human-approved meaning for an evaluative term or classification.

The ontology can represent each dependency below. A reliable answer also needs a complete input set. The 100-paper experiment is not a complete project, person, citation, or global value-set registry.

| Q | Primary records and relations | Dependencies |
|---|---|---|
| Q1 | Projects, approved awards, currencies, deduplication, total | Portfolio, Analytic |
| Q2 | Project funding date and yearly count | Portfolio, Analytic |
| Q3 | Approved award amount and currency rule; median, IQR, maximum | Portfolio, Analytic |
| Q4 | Project status at a named date | Portfolio |
| Q5 | Project-working-group links, award amounts, rank | Portfolio, Analytic |
| Q6 | Completed projects, accepted output links, proportion | Portfolio, Analytic |
| Q7 | Project start, accepted publication dates, first-output rule, median | Portfolio, Corpus, Analytic |
| Q8 | Accepted project-publication links, distinct publication count, rank | Portfolio, Corpus, Analytic |
| Q9 | Completion date, accepted output search, cut-off, anti-join | Portfolio, Corpus, Analytic |
| Q10 | Project target instrument and award amount by instrument family | Portfolio, Content, Analytic |
| Q11 | Award recipient organization, organization country, approved amount | Portfolio, People, Analytic |
| Q12 | Accepted funded publication, citation count and snapshot, rank | Portfolio, Scholarly, Analytic |
| Q13 | Dated project topics or study types and time trend | Portfolio, Content, Analytic |
| Q14 | PI role, projects, approved amount, person resolution, rank | Portfolio, People, Analytic |
| Q15 | Funding acknowledgement, project ID, link-review status | Portfolio, Corpus |
| Q16 | Project country role, EQ-5D-5L, valuation-study type, historical status | Portfolio, Content |
| Q17 | Applicant identity, prior grants, accepted publications, study summaries | Portfolio, People, Content |
| Q18 | Proposal text, past-project aims, versioned similarity method and rank | Portfolio, Analytic |
| Q19 | Cognition bolt-on, project aims, status, outputs, overlap rule | Portfolio, Content, Rule |
| Q20 | Proposal aims, ongoing project aims, population, condition, instrument, method | Portfolio, Content, Rule, Analytic |
| Q21 | Applicant identity, dated membership, co-authorship | People, Corpus |
| Q22 | Applicant, previous grant date, first accepted publication, interval | Portfolio, People, Analytic |
| Q23 | Completed projects, promised product, accepted value-set outputs, anti-join | Portfolio, Content, Rule |
| Q24 | Funded valuation studies, exact valuation methods, region role | Portfolio, Content |
| Q25 | Student-grant class, completed projects, accepted outputs, proportion | Portfolio, Rule, Analytic |
| Q26 | Proposal condition and instrument, past project aims, conjunctive match | Portfolio, Content |
| Q27 | Approved budget band, proposal amount, accepted output count, productivity rule | Portfolio, Analytic, Rule |
| Q28 | Proposal references, publication identity, corpus membership, funded-output links | Portfolio, Corpus, Scholarly |
| Q29 | Published native EQ-5D-5L value sets and jurisdiction | Content, Registry |
| Q30 | Value-set products, EQ-VT protocol and exact version | Content |
| Q31 | Current people and project roles, EQ-HWB, valuation-study type | Portfolio, People, Content |
| Q32 | Working-group projects, accepted publications, five-year cut-off | Portfolio, Corpus |
| Q33 | Shared population or sample, 3L and 5L value sets, direct comparison | Content |
| Q34 | EQ-5D-5L population-norm study, country, publication | Content, Registry |
| Q35 | Mapping or crosswalk study, source measure, target EQ-5D version | Content |
| Q36 | EQ-5D-Y version, self and proxy forms, agreement property and statistic | Content |
| Q37 | Valuation study, DCE method, data-collection or target country | Content |
| Q38 | Resolved researcher, corpus co-authors, frequency and tie rule | People, Corpus, Analytic |
| Q39 | Bolt-on product or supplementary dimension, condition, base instrument | Content |
| Q40 | Ongoing project or study, EQ-5D-5L target, valuation-study type, as-of date | Portfolio, Content |
| Q41 | EQ-VT protocol product, introduction or validation role, publication | Content, Rule |
| Q42 | DCE-with-duration and related exact method terms, studies, products | Content |
| Q43 | Value-set product, funding link search, explicit non-funding rule | Content, Portfolio, Rule |
| Q44 | Researcher identity, publications or projects, dated working-group links | People, Portfolio |
| Q45 | EQ-5D-5L valuation studies, analytic sample counts, inclusion rule, median/range | Content, Analytic |
| Q46 | Canonical 1997 UK MVH publication, corpus references and citations | Corpus, Scholarly |
| Q47 | Resolved researcher, dated member status, funded outputs, co-authorship | People, Portfolio, Corpus |
| Q48 | Ongoing projects, exact target instruments, project aim or planned product | Portfolio, Content |
| Q49 | EQ-5D-Y version, retest design, interval, reliability property and statistic | Content |
| Q50 | Same value-set study, TTO method and DCE method | Content |
| Q51 | Complete EQ-TIPS project, publication, version, product, and study-purpose record | Content, Portfolio, Registry |
| Q52 | EQ-HWB translation or adaptation product, language, validation status, publication | Content, Registry |
| Q53 | Valuation-method study type, citation snapshot, top-ten rank | Content, Scholarly, Analytic |
| Q54 | Native value set versus crosswalk basis, source and target versions, key publications | Content |
| Q55 | Funded projects or studies, host organization and country, rank rule | Portfolio, People, Analytic |
| Q56 | Student grants, supervisor role, host institution | Portfolio, People |
| Q57 | Funded valuation projects, exact methods, project deduplication, frequency | Portfolio, Content, Analytic |
| Q58 | Exact EQ-5D-Y-5L version, study types, publications, current snapshot | Content, Registry |
| Q59 | EQ-HWB introduction role, publication and open-access snapshot | Content, Scholarly, Rule |
| Q60 | Dated topic or study-type assignments, three-year window, growth rule | Content, Corpus, Analytic |
| Q61 | Dated instrument-version, translation, validation, launch, and value-set events | Content, Registry, Analytic |
| Q62 | Resolved people, organization identity, dated affiliation, EQ topics | People, Content |
| Q63 | Country universe minus published native EQ-5D-5L jurisdictions | Registry, Analytic |
| Q64 | Systematic-review study type, citation snapshot, rank | Content, Scholarly, Analytic |
| Q65 | Youth instrument family, journal identity, frequency and tie rule | Content, Corpus, Analytic |
| Q66 | Student grants, accepted publications, principal findings | Portfolio, Content |
| Q67 | Child valuation study types and methods, key findings, reading-list rule | Content, Scholarly, Rule |
| Q68 | EQ-5D methodological corpus, funding acknowledgements, fraction | Content, Portfolio, Corpus, Analytic |
| Q69 | Included corpus publications, publication year, yearly count | Corpus, Analytic |
| Q70 | Resolved members, co-authorship network, community method and version | People, Corpus, Analytic |
| Q71 | Funded publications, open-access status and date, time trend | Portfolio, Scholarly, Analytic |
| Q72 | Researcher identity, funded link status, citation snapshot, comparison rule | People, Portfolio, Scholarly, Analytic |
| Q73 | Publication-time affiliation countries, paper-level country count, time trend | People, Corpus, Analytic |
| Q74 | Resolved author, first observed corpus publication, three-year cut-off | People, Corpus, Analytic |
| Q75 | Accepted links, project-period reference dates, publication dates, window rule | Portfolio, Corpus, Analytic |
| Q76 | Publication identity, accepted links to distinct projects | Portfolio, Corpus |
| Q77 | PI roles, accepted outputs, top-decile rounding and concentration share | Portfolio, People, Analytic |
| Q78 | Dated member status, non-members, co-authorship counts | People, Corpus, Analytic |
| Q79 | Corpus citation graph, component and hub definitions, method version | Scholarly, Analytic |
| Q80 | Accepted project-output links and citations between outputs | Portfolio, Scholarly, Analytic |
| Q81 | Resolved-person universe, ORCID assertion and verification, fraction | People, Analytic |
| Q82 | Publication metadata-quality flags, flag definition and source | Corpus, Rule |
| Q83 | Working-group projects, accepted output counts, comparison rule | Portfolio, Analytic |
| Q84 | Resolved-person universe and dated membership status | People, Analytic |
| Q85 | Funded outputs, citing works, dated OpenAlex topics, rank | Portfolio, Scholarly, Analytic |
| Q86 | Corpus citations, citing and cited dates, lag distribution | Scholarly, Analytic |
| Q87 | Identity-resolution events, before and after identities, action, evidence and reason | People, Corpus |
| Q88 | Funded publications, venue metric and snapshot, impact rule | Portfolio, Scholarly, Rule, Analytic |
| Q89 | Project, outputs, citations, collaborators, findings and impact summary rule | Portfolio, People, Content, Scholarly, Rule |
| Q90 | Value-set product projects and later corpus references to the product | Portfolio, Content, Scholarly |
| Q91 | Recent completed projects, citations, success and high-citation rules | Portfolio, Scholarly, Rule, Analytic |
| Q92 | Project universe, projects with outputs, distinct outputs, citations | Portfolio, Scholarly, Analytic |
| Q93 | First PI role, first grant, accepted publication, cut-off rule | Portfolio, People, Rule |
| Q94 | Dated co-authorship graph, decade buckets, network-size and growth measures | People, Corpus, Analytic |
| Q95 | Project study populations, under-representation categories, status | Portfolio, Content, Rule |
| Q96 | Complete corpus, bolt-on study or product, one-line principal finding | Content, Corpus |
| Q97 | Funded publications, publication-time author affiliations, distinct countries | Portfolio, People, Analytic |
| Q98 | DOI, accepted project-output link, link evidence and review status | Portfolio, Corpus |
| Q99 | Dated member authorship, corpus exclusion decision, pure-application rule, fraction | People, Corpus, Rule, Analytic |
| Q100 | Corpus-ingestion event, extraction source, full-text or structured-metadata route | Corpus |

## Coverage result

- Q29-Q67 test the scientific ontology most directly. The proposed core contains the required exact study, instrument, population, method, model, product, outcome, and finding concepts.
- Q1-Q28 depend mainly on project, funding, proposal, and project-output data. These records belong in the portfolio module.
- Q68-Q100 depend mainly on people, corpus history, citations, external metadata, and declared analytics.
- Many questions combine two or three modules. The links between modules are therefore part of the model.
- Questions that use terms such as `success`, `impact`, `starter reading list`, `overlap`, `high impact`, `under-represented`, or `pure application` need a human-approved rule before calculation.
