# Competency questions for the EuroQol research knowledge graph

This file contains 100 competency questions and 20 negative (bad) questions.
The release test result is in [aggregate-validity-v5/RESULT.md](aggregate-validity-v5/RESULT.md).
The questions were generated from six user personas crossed with ten query capabilities and seven output modalities.
Paper-level ontology requirements are in [USER_QUESTIONS.md](../../archive/pilot/ontology-development-v2/USER_QUESTIONS.md).

Each good question scores pass, partial, fail, or not testable.
Each bad question tests whether the system refuses, caveats, or corrects the premise.

**Columns.** Output: text, number, list, links, table, viz, profile.
Needs: `core` (projects+publications+authors+links), `extract` (typed evidence items), `cites` (citation edges), `member` (membership), `budget` (budget/status), `sim` (embeddings), `fulltext` (harvested text), `class` (relevance labels).
Pilot: ✓ answerable with the pilot load; ✗ needs the full graph or later enrichment.

---

## A. Portfolio & funding overview (foundation staff, board) — Q1–Q15

| # | Question | Output | Needs | Pilot |
|---|---|---|---|---|
| Q1 | How many projects has EuroQol funded in total, and what is the combined approved budget? | number | core, budget | ✓ |
| Q2 | How many projects were funded each year since 2012? | viz (bar) | core | ✓ |
| Q3 | What is the distribution of approved budgets (median, IQR, largest grants)? | number/viz | budget | ✓ |
| Q4 | How many projects are ongoing vs completed vs closed? | number | core | ✓ |
| Q5 | Which working group accounts for the most projects, and the most budget? | table | core, budget | ✓ |
| Q6 | What proportion of completed projects have at least one linked publication? | number + viz (funnel) | core | ✓ |
| Q7 | What is the median time from project start to first linked publication? | number/viz | core | ✓ |
| Q8 | Which five projects produced the most publications? | list + links | core | ✓ |
| Q9 | Which projects completed three or more years ago still have no linked publication? | list | core | ✓ |
| Q10 | How does funding split across instrument families (EQ-5D-3L/5L, EQ-5D-Y, EQ-HWB, EQ-TIPS)? | viz | extract, budget | ✓ |
| Q11 | Which countries' institutions have received the most EuroQol funding? | viz (map)/table | core, budget | ✗ (needs institution→country) |
| Q12 | Which funded publication is the most cited, and which project produced it? | text + link | core, cites | ✓ |
| Q13 | How has the topical mix of the portfolio shifted over time? | viz (trend) | extract | ✓ |
| Q14 | Which PIs hold the most grants, by count and by total budget? | table | core, budget | ✓ |
| Q15 | Which publications acknowledge EuroQol funding but cannot be tied to any project id? | list | core, class | ✗ |

## B. Grant reviewers — Q16–Q28

| # | Question | Output | Needs | Pilot |
|---|---|---|---|---|
| Q16 | Has EuroQol funded an EQ-5D-5L valuation study in country X before? | text + list | extract | ✓ |
| Q17 | What did applicant X publish from their previous EuroQol grants? | list | core | ✓ |
| Q18 | Which past funded projects are topically most similar to this proposal abstract? | list (ranked) | sim | ✗ |
| Q19 | Is a cognition bolt-on already covered by past or ongoing projects? | list | extract | ✓ |
| Q20 | Which ongoing projects overlap with this proposal's aims? | list | core, sim | ✗ |
| Q21 | Has applicant X co-authored with EuroQol members before, and with whom? | list/viz (network) | core, member | ✓ |
| Q22 | How long after their previous grant did applicant X first publish from it? | number | core | ✓ |
| Q23 | Which completed projects promised a value set in their abstract but have no linked value-set publication? | list | core, extract | ✓ |
| Q24 | Which valuation methods (TTO, DCE, hybrid) have funded projects in region Y used? | table | extract | ✓ |
| Q25 | What share of student grants produced at least one publication? | number | core | ✓ |
| Q26 | Which past projects share both this proposal's target condition and instrument? | list | extract | ✓ |
| Q27 | How productive were past projects in the same budget band as this proposal? | viz/table | core, budget | ✓ |
| Q28 | Given a proposal's reference list, which cited works are already in the corpus, and which are EuroQol-funded? | list (annotated) | core, class | ✗ |

## C. Active EQ researchers & members — Q29–Q52

| # | Question | Output | Needs | Pilot |
|---|---|---|---|---|
| Q29 | Which countries have a published EQ-5D-5L value set? | viz (map)/table | extract, class | ✗ (needs full included set) |
| Q30 | Which value sets used the EQ-VT protocol, and which version? | table | fulltext | ✗ |
| Q31 | Who is currently working on EQ-HWB valuation? | list | core, extract | ✓ |
| Q32 | Which publications came out of working group X's projects in the last five years? | list | core | ✓ |
| Q33 | Which studies compare EQ-5D-5L and EQ-5D-3L value sets in the same population? | list | class, extract | ✗ |
| Q34 | What population norms have been published for EQ-5D-5L, by country? | table | class, extract | ✗ |
| Q35 | Which mapping/crosswalk studies link condition-specific instruments to EQ-5D? | list | class, extract | ✗ |
| Q36 | Has proxy-vs-self-report agreement been studied for EQ-5D-Y? | list | class | ✗ |
| Q37 | Which papers used DCE for valuation, and in which countries? | list + viz (map) | extract | ✓ |
| Q38 | Who are researcher X's most frequent co-authors within the corpus? | viz (network) | core | ✓ |
| Q39 | Which conditions have bolt-on dimensions been developed or tested for? | list | extract | ✓ |
| Q40 | Which EQ-5D-5L valuation studies are ongoing right now? | list | core, extract | ✓ |
| Q41 | Which publications introduced or validated the EQ-VT protocol? | links | class | ✗ |
| Q42 | What work exists on DCE-with-duration hybrids? | list | extract, class | ✗ |
| Q43 | Which value sets were produced *without* EuroQol funding? | list | class | ✗ (tests negation) |
| Q44 | Which working groups does researcher X's work span? | text/traversal | core | ✓ |
| Q45 | What sample sizes are typical for 5L valuation studies? | number/viz | extract | ✓ |
| Q46 | Which corpus papers cite the 1997 UK MVH value-set paper? | list | cites | ✗ |
| Q47 | Which members co-authored with researcher X on funded outputs? | list | core, member | ✓ |
| Q48 | Which instruments does each ongoing project target? | table | extract | ✓ |
| Q49 | Which studies examined test–retest reliability of EQ-5D-Y? | list | class | ✗ |
| Q50 | Which papers report both TTO and DCE data for the same value set? | list | extract, fulltext | ✗ |
| Q51 | What EQ-TIPS work exists so far? | list | extract, class | ✓ |
| Q52 | Which translations or language adaptations of EQ-HWB have been published? | list | class | ✗ |

## D. PhD students & newcomers — Q53–Q67

| # | Question | Output | Needs | Pilot |
|---|---|---|---|---|
| Q53 | What are the ten most-cited papers on EQ-5D valuation methodology? | list (reading list) | cites, class | ✗ |
| Q54 | What is the difference between a crosswalk and a native 5L value set — with key references? | text + links | class | ✗ |
| Q55 | Which institutions host the most EuroQol-funded research? | table | core | ✓ |
| Q56 | Which supervisors and institutions ran student grants? | list | core | ✓ |
| Q57 | Which methods appear most often in funded valuation projects (what should I learn)? | table (ranked) | extract | ✓ |
| Q58 | What has been published on EQ-5D-Y-5L so far? | list | class | ✗ |
| Q59 | Which open-access papers introduce EQ-HWB? | links | core, class | ✓ |
| Q60 | Which topics show growing publication activity in the last three years? | viz (trend) | class, extract | ✗ |
| Q61 | Give a timeline of instrument-development milestones as reflected in the corpus. | viz (timeline) | class | ✗ |
| Q62 | Who works at institution X on EQ topics? | list | core | ✓ |
| Q63 | Which countries still lack a native EQ-5D-5L value set? | viz (gap map) | class, extract | ✗ (tests negation) |
| Q64 | Which are the most-cited systematic reviews in the corpus? | list | cites, class | ✗ |
| Q65 | In which journals do youth-instrument papers usually appear? | table | class | ✗ |
| Q66 | Which student-grant projects led to publications, and what did they find? | list (annotated) | core, extract | ✓ |
| Q67 | What is a good starter reading list on health-state valuation for children? | list | class, cites | ✗ |

## E. Meta-researchers & bibliometricians — Q68–Q87

| # | Question | Output | Needs | Pilot |
|---|---|---|---|---|
| Q68 | What share of the EQ-5D methodological literature acknowledges EuroQol funding? | number | class | ✗ |
| Q69 | How has annual publication output of the included corpus evolved since 1990? | viz (trend) | class | ✗ |
| Q70 | What co-authorship communities exist among EuroQol members? | viz (network) | core, member | ✓ |
| Q71 | What is the open-access share of funded publications, and its trend? | viz (trend) | core | ✓ |
| Q72 | How do citations of researchers' EuroQol-funded papers compare with their other corpus papers? | viz/number | core, cites, class | ✗ |
| Q73 | Has international co-authorship (countries per paper) increased over time? | viz (trend) | core | ✗ (needs affiliation→country) |
| Q74 | Which researchers newly entered the corpus in the last three years? | list | class | ✗ |
| Q75 | What fraction of accepted links fall in the −1..+8-year window around the project period? | number | core | ✓ (method diagnostic) |
| Q76 | Which publications are linked to more than one funded project? | list | core | ✓ |
| Q77 | How concentrated is output among PIs (share held by the top decile)? | number/viz | core | ✓ |
| Q78 | Which non-members co-author most frequently with members? | table | core, member | ✓ |
| Q79 | What is the structure of the within-corpus citation network (components, hubs)? | viz/number | cites | ✗ |
| Q80 | Which projects' outputs cite other projects' outputs (inter-grant knowledge flow)? | viz (network) | core, cites | ✗ |
| Q81 | What share of resolved researchers have an ORCID? | number | core | ✓ (QA) |
| Q82 | Which papers carry metadata-quality flags (truncated author list, missing abstract)? | list | core | ✓ (QA) |
| Q83 | How do papers-per-project compare across working groups? | table/viz | core | ✓ |
| Q84 | How many distinct researchers appear in the graph, and how many are members? | number | core, member | ✓ |
| Q85 | Which OpenAlex topics/fields cite EuroQol-funded work the most? | table | cites (+topics) | ✗ |
| Q86 | What is the distribution of in-corpus citation lag (years between citing and cited paper)? | viz | cites | ✗ |
| Q87 | Which author profiles were merged, overridden, or skipped during identity resolution, and why? | list | core (provenance) | ✓ |

## F. Impact, communications & provenance — Q88–Q100

| # | Question | Output | Needs | Pilot |
|---|---|---|---|---|
| Q88 | Which funded papers appeared in the highest-impact venues? | list | core | ✓ |
| Q89 | Give a one-paragraph impact profile of project X: outputs, citations, collaborators. | profile | core, cites | ✓ |
| Q90 | Which projects produced value sets that later corpus works reference? | list | cites, extract | ✗ |
| Q91 | Name five recent success stories: projects completed in the last three years with highly cited outputs. | list | core, cites | ✓ |
| Q92 | Show the overall funnel: projects → projects with outputs → outputs → citations. | viz (funnel) | core, cites | ✓ |
| Q93 | Which first-time PIs published from their first grant? | list | core | ✓ |
| Q94 | Show the growth of the collaboration network decade by decade. | viz (small multiples) | core | ✗ |
| Q95 | Which projects studied under-represented populations (children, cognitive impairment)? | list | extract | ✓ |
| Q96 | List all corpus papers about bolt-ons, with a one-line summary each. | list (annotated) | class, extract | ✗ |
| Q97 | How many countries' researchers have participated in funded publications? | number + viz (map) | core | ✗ (affiliation→country) |
| Q98 | For DOI X: which project produced it, and what evidence supports that link? | text (provenance) | core | ✓ |
| Q99 | What share of member-authored corpus papers are excluded as pure applications? | number | class, member | ✗ (tests relevance layer) |
| Q100 | Which papers entered the graph via full-text grant mining vs structured funder metadata? | table (provenance) | core | ✓ |

---

## Negative (bad) questions — B1–B20

Each has a category and an expected behavior: `refuse` (say the graph does not hold this), `caveat` (answer the answerable part, state the boundary), `premise` (correct the false premise), `no-judgment` (decline normative/subjective verdicts, offer the factual substrate).
Hallucinating a fluent answer is a test failure.

| # | Question | Why it is bad | Expected behavior |
|---|---|---|---|
| B1 | What were the peer-review scores for project 2014030? | Review data is not in the graph | refuse |
| B2 | Why was my grant application rejected? | Rejected applications are absent; decision rationale unknowable | refuse |
| B3 | Which projects will EuroQol fund next year? | Future, unknowable | refuse |
| B4 | What is the licensing fee for commercial use of EQ-5D-5L? | Licensing/business data out of scope | refuse (point to EuroQol office) |
| B5 | What is researcher X's personal email address? | Not stored; privacy | refuse (offer public profile URL) |
| B6 | Give me the full text of [paywalled paper]. | Copyright; graph stores metadata (and some OA text) | caveat (metadata + OA link if any) |
| B7 | What is the gender distribution of funded PIs? | Not recorded; name-based inference unreliable and inappropriate | refuse |
| B8 | Is EQ-5D better than SF-36? | Normative verdict; graph holds literature, not judgments | no-judgment (offer comparison studies) |
| B9 | Which value set should I use for my trial in France? | Recommendation/advice; authority lies with official guidance | no-judgment (list existing French value sets + caveat) |
| B10 | What were the patient-level utility scores in study Y? | Micro-data not in the graph | refuse |
| B11 | What did the EuroQol board discuss at its last meeting? | Internal minutes absent | refuse |
| B12 | How many people worldwide have ever completed an EQ-5D questionnaire? | Unknowable from any source here | refuse |
| B13 | When did EuroQol fund the development of the SF-36? | False premise (it did not) | premise |
| B14 | What is PI X's overall h-index across all their fields? | Corpus is EQ-scoped; a cross-field metric computed from it would be silently wrong | caveat (in-corpus metrics only, clearly labeled) |
| B15 | Which paper in the corpus contains fraudulent data? | Accusation/judgment not derivable from metadata | refuse |
| B16 | How many citations did paper X get this week? | Graph is a dated snapshot; no real-time data | caveat (snapshot value + snapshot date) |
| B17 | What is the salary of EuroQol's executive director? | Private, out of scope | refuse |
| B18 | Translate the EQ-5D-5L descriptive system into Swahili. | Instrument content is licensed; a task, not a graph query | refuse (point to EuroQol translation process) |
| B19 | Which unpublished plenary abstracts exist for project X? | Grey literature is a known coverage gap | caveat (state the gap explicitly) |
| B20 | Did project 343-RA achieve its stated aims? | Goal attainment is a judgment; graph shows outputs, not success | no-judgment (show aims vs outputs, no verdict) |

---

## Coverage summary

- **Personas**: foundation/board 15, reviewers 13, researchers/members 24, PhD/newcomers 15, meta-researchers 20, impact/provenance 13.
- **Capabilities**: lookup, aggregation, ranking, trends, traversal, network, similarity, negation/gap-finding, provenance, data-quality introspection.
