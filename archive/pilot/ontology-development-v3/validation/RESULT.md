# Holdout pilot result

## Assessment

The proposed ontology now produces useful and natural EuroQol research records. It is ready for human review through concrete outputs. It is not yet time to design the database tables.

The central design passed:

- exact study type, instrument, method, model, product, and finding values remained visible;
- instrument versions, roles, language, administration, respondent, and perspective remained distinct;
- methods did not collapse into statistical models;
- products did not collapse into publications or findings;
- principal findings remained useful without participant-level data or full result tables;
- missing facts and source conflicts remained visible;
- no universal claim-evidence structure was necessary.

## Process

1. Selected ten papers not used in the 100-paper ontology design set.
2. Covered ten different research patterns.
3. Used the compact Markdown extraction instruction in `EXTRACTION_TASK.md`.
4. Lower-cost agents produced one record per paper.
5. Different agents checked each record against the full source.
6. The primary agent reviewed all records, source abstracts, methods, results, and conclusions.
7. Corrected minor factual and terminology issues.
8. Tested twelve questions against the records and source text.

All ten source hashes and byte counts match the frozen manifest.

## Record results

| Record | Research pattern | Source-QA result | Main ontology observation |
|---|---|---|---|
| H01 | German EQ-5D-5L value set | Pass | Exact valuation methods, model roles, and product fit well |
| H02 | DCE design and attribute non-attendance | Pass after minor wording correction | DCE design details need searchable task-design fields |
| H03 | OPUF test-retest reliability | Pass | One method can produce individual and aggregate products with different reliability |
| H04 | QID-12 instrument development | Pass after cohort correction | Reused source datasets need explicit cohort lineage |
| H05 | EQ-HWB proxy use in aged care | Pass after minor corrections | Proxy type, perspective, and response process are essential |
| H06 | Swedish adolescent population health | Pass after minor corrections | Sample stages and population-reference products fit well |
| H07 | Asian measurement-property review | Pass after minor corrections | Review publications and source-defined evidence units must stay separate |
| H08 | Chichewa EQ-5D-Y psychometrics | Pass after source-conflict additions | Scoring value set is not a fitted study model |
| H09 | Vision-impairment economic burden | Pass as extraction; project link unverified | Boundary test only; no EQ instrument was reported |
| H10 | EQ-5D-5L decision-aid visualization | Pass after instrument-use clarification | Displaying historical instrument data is not instrument administration |

## Question-test result

- Pass: 10.
- Partial: 1.
- Boundary test: 1.
- Fail: 0.

The partial result is structural, not an extraction error:

- H07 needs a review evidence unit.

H09 showed a possible economic-analysis profile, but its EuroQol project link is not verified. Defer that profile until an accepted portfolio paper or a user question needs it.

The complete tested answers are in [QUESTION_TEST.md](QUESTION_TEST.md).

## Important correction from the pilot

The initial H09 selection note said that the study used EQ-5D-5L. The full paper does not report any EQ instrument. The extractor did not copy this incorrect selection assumption into the research record.

A later audit also found that the article does not connect EuroQol funding to the study. Its Funding section names other funders. EuroQol project IDs occur only in one author's competing-interest statement. H09 is now an unverified project-link candidate and a boundary test, not a confirmed funded output.

This is a useful safety result. Extraction must use the article as evidence. Project labels, filenames, selection notes, and expected topics are context only.

## Required ontology changes

1. Separate research purpose from study design.
2. Add input dataset or cohort lineage.
3. Add a review evidence unit.
4. Defer the economic analysis profile until accepted portfolio evidence requires it.
5. Add instrument-use roles for reuse, visualization, and decision support.
6. Add family-specific controlled fields within task design, administration, sample, and product status.

These changes are specified in [PILOT_REVISIONS.md](PILOT_REVISIONS.md). They extend the evidence-backed core. They do not create a new general research ontology.

## Concrete review set

The most useful records for human review are:

- [H01](records/H01.md): valuation study, methods, model, and value-set product.
- [H05](records/H05.md): proxy perspective, qualitative findings, and instrument problems.
- [H07](records/H07.md): systematic-review evidence structure.
- [H09](records/H09.md): economic-burden boundary case with no EQ instrument and an unverified funding link.
- [H10](records/H10.md): reuse and visualization of EQ-5D-5L data in decision support.

## Recommendation

Accept the ontology core with the six holdout revisions. Then run one small relational implementation with these ten records. Do not build the full database or extraction pipeline yet.

The next implementation must show:

- exact filters for study type, instrument, method, and model;
- principal-finding retrieval;
- source and conflict inspection;
- correct separation of administered, scored, reused, and visualized instrument data;
- the H07 review-unit extension and the H09 funding boundary.
