# Typed ontology development

This experiment converts the descriptive EuroQol ontology into a typed
extraction vocabulary. It keeps the present graph unchanged.

The ontology is derived from papers. The 100 user questions test whether the
result can support useful analysis. They do not define one field per question.

Markdown is the human-readable experiment record. It lets independent agents
show how they applied and revised the ontology. Production extraction will not
load these Markdown applications. One Opus call returns a compact draft record
for each paper. A fresh second Opus call checks the full source and returns the
complete corrected record. Deterministic code then validates controlled values,
normalizes registry identities, and loads the SQL graph.
Unknown information will enter the review queue through an explicit gap state;
it will not become an invented official value.

## Round 1

- Evidence set: 15 deliberately diverse papers.
- Two independent builders propose and apply a typed vocabulary.
- One independent reviewer compares the proposals and checks disputed cases
  against the papers.
- The final synthesis keeps a small stable structure, controlled scientific
  values, open concepts, and explicit routes for gaps.
- Round 2 will retain these papers and add 15 new papers.

## Round 2

- Two fresh agents applied version 0.1 to 15 new papers.
- They agreed on all 15 primary-family assignments and found the same two
  missing family mappings.
- A fresh reviewer checked material differences against the papers.
- Version 0.2 adds one primary family, three bounded structures, one method
  function, and one product-state relation.
- No round-1 primary family changed. The cumulative family partition covers
  30 studies.
- One more 15-paper confirmation round is required before a larger batch.

## Round 3

- A blind version-0.2 regression reclassified 3 of the first 30 studies and
  found one part-level design gap.
- Two fresh agents independently applied version 0.2 to 15 new papers and
  agreed on every primary-family assignment.
- A fresh reviewer checked material differences against 19 articles.
- Version 0.3 adds empirical preference research, economic-burden research,
  part-level participatory design, publication status, and health behavior.
- The reviewed exact-one partition covers 45 studies.
- One final 15-paper confirmation round is required before a freeze decision.

## Round 4

- A blind version-0.3 regression mapped all 45 earlier studies but changed four
  reviewed families.
- Source checks accepted two corrections: S058 is methods research and C011
  is health-preference research. They rejected the S084 and C004 changes.
- Two fresh agents applied version 0.3 to 15 new papers. The review resolved
  two family disagreements and found no new record, key, or controlled value.
- Version 0.4 added only short family-boundary rules. Its blind 60-paper
  regression still disagreed on six families.
- A source audit accepted one change: C008 is a planned preference study, not
  a protocol publication classified as a methods study. It rejected the other
  five changes.
- Version 0.5 makes the Study the classification unit and replaces loose
  boundary prose with one ordered 12-family decision table.
- A blind version-0.5 reapplication matched 59 of 60 source-adjudicated
  families and found no new record, key, controlled value, or gap.
- The remaining C011 methods-versus-preference choice is a genuine close
  classification case. No paper-specific rule was added.
- The structure is ready for production-format calibration on unseen papers.
  Primary family remains a governed field before aggregate use.

## Production calibration

- One shallow JSON record now carries the assessment, studies, and typed items.
- The first 20-paper unseen run needed one governed value and general prompt
  corrections. Final repaired records pass 20/20 deterministic checks; final
  source review passed all 16 affected records.
- Registry identity is a separate governed layer. The AI preserves exact
  labels and deterministic code applies reviewed identities after extraction.
- A fresh second 20-paper test produced 20/20 valid repaired records. A later
  independent cross-audit found one repeated structural omission: software
  used for collection or analysis had no exact entity.
- Versions 0.6 to 0.8 added `SoftwareUse`, removed forced placeholder parts,
  allowed whole-study relations, and added exact review-flow stages and an
  experimental-design software function. Version 0.9 adds the matching
  experimental-design method function. The family partition did not change.
- The corrected confirmation has 21 studies, 1,205 typed items, 287 mapped
  registry uses, and two intentional unresolved labels. Its SQLite fixture is
  deterministic and passes all integrity checks.
- The first fresh eight-paper test had three MAJOR raw records; focused repairs
  removed all major defects. A second fresh eight-paper test had zero MAJOR,
  two PASS, and six MINOR raw records.
- The first rebuild was stopped after 23 records because software had no exact
  entity. The version-0.8 restart was stopped after five records because its
  method vocabulary lacked experimental design. A four-paper version-0.9 test
  had zero MAJOR source defects and no new ontology gap.
- The version-0.9 rebuild stopped after 48 records when one-paper audits found
  repeated sample-flow gaps. Version 0.10 added three general stages. Its
  focused test then exposed forced clinical-event and service-use outcome
  mappings. Version 0.11 adds two general outcome families. Version 0.12 adds
  translation and adaptation methods. Version 0.13 adds existing-product uses.
  A 20-paper Opus test found no MAJOR scientific error, and its corrected
  records pass 20/20 deterministic checks. The version-0.13 run covers all 209
  papers.
- All 209 version-0.13 corrected records pass deterministic validation. They
  represent 207 studies, one correction notice, and one excluded paper, with
  15,430 typed items, 1,951 findings, 939 limitations, 96 products, 188 source
  conflicts, and 210 explicit gaps.
- Fresh Opus source review returned 7 PASS, 202 MINOR, 0 MAJOR, and 846
  corrections across the drafts. Version 1 remains unchanged. The version-2
  database and shared preview are in packaging.
- The shared preview is not the final analytical release. The full aggregate-
  validity rerun against all 100 questions and focused version-0.14 gap work
  remain. Record validity does not show that the 100 questions pass.

## Files

- `PROTOCOL.md`: iteration and acceptance rules.
- `BUILDER_TASK.md`: independent proposal task.
- `REVIEW_TASK.md`: independent comparison task.
- `round-01.tsv`: controlled paper manifest.
- `round-01/candidate-a.md` and `round-01/candidate-b.md`: independent work.
- `round-01/review.md`: independent comparison.
- `ONTOLOGY.md`: ultra-short current domain map and rules.
- `VOCABULARY.tsv`: exact controlled keys, values, and one-line definitions.
- `EXTRACTION_TASK.md`: short pilot application task; not production output.
- `round-01/applications.md`: backward-fit application to all 15 papers.
- `round-01/gaps.md`: unresolved vocabulary and schema gaps.
- `round-02.tsv`: second controlled paper manifest.
- `round-02/application-a.md` and `round-02/application-b.md`: independent
  version-0.1 applications.
- `round-02/review.md`: source-checked independent adjudication.
- `round-02/DECISIONS.md`: concise accepted changes and next gate.
- `regression-v0.2.md`: blind reapplication to the first 30 papers.
- `round-03.tsv`: confirmation paper manifest.
- `round-03/application-a.md` and `round-03/application-b.md`: independent
  version-0.2 applications.
- `round-03/review.md`: source-checked confirmation review.
- `round-03/DECISIONS.md`: concise version-0.3 changes and next gate.
- `regression-v0.3.md`: blind reapplication to the first 45 papers.
- `round-04.tsv`: final confirmation manifest.
- `round-04/application-a.md` and `round-04/application-b.md`: independent
  version-0.3 applications.
- `round-04/review.md`: source-checked final confirmation review.
- `round-04/DECISIONS.md`: concise version-0.4 changes and next gate.
- `regression-v0.4.md`: blind 60-paper application of version 0.4.
- `regression-v0.4-audit.md`: source-checked unit and boundary correction.
- `regression-v0.5.md`: blind 60-paper application of the ordered family table.
- `regression-v0.5-audit.md`: final fit and governance decision.
- `production/rebuild-v2-v013-gap-audit-01.md`: recurrent gap governance and
  release implications after the full corrected-record run.
