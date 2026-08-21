# Production calibration decision

Status: the version-0.13 corrected-record run, separate version-2 SQLite
database, and shared preview are complete. Keep version 1 unchanged as the
historical baseline.

The first unseen batch contained 20 publications. Independent source review of
the raw records found 10 PASS, nine MINOR, and one MAJOR. General rules and one
new controlled value corrected all affected records. Final source review found
no remaining defect.

The fresh confirmation batch contained 20 different publications and 21
author-defined studies. Raw source review again found 10 PASS, nine MINOR, and
one MAJOR. The MAJOR error merged two author-defined studies. One general rule
now requires a separate `Study` record for each reported study. No primary-
family error occurred. Three one-paper representation gaps remain explicit;
none justified a new controlled value.

Focused repairs produced 20/20 valid confirmation records. Independent review
checked every repaired record and found no remaining defect. Deterministic
normalization maps 287 scientific uses to reviewed identities. Two labels stay
unmapped because the source does not identify an exact model or instrument
version. The calibration registry had 332 identities and 394 exact aliases.

A later independent cross-audit found that the model had no exact software-use
entity. The first rebuild was stopped after 23 saved records and invalidated.
Versions 0.6 to 0.8 add software use, optional parts for simple studies,
whole-study relations, two review-flow sample stages, and an
experimental-design software function. A live audit of the version-0.8
restart then found that the method vocabulary could not identify
experimental-design algorithms. That run was stopped after five records.
Version 0.9 adds the bounded `EXPERIMENTAL_DESIGN` method function. It does not
change the 12 study families.

The corrected confirmation fixture passes all deterministic and SQLite checks.
The first fresh eight-paper test had three MAJOR raw records; focused repairs
removed all major defects. The second fresh eight-paper test had zero MAJOR,
two PASS, and six MINOR raw records. A further four-paper DCE-design test under
version 0.9 had zero MAJOR and four MINOR source verdicts. The version-0.9
rebuild then stopped after 48 records when one-paper audits found repeated
sample-flow gaps. Version 0.10 added general identification, screening, and
eligibility stages. Its focused test exposed forced mappings for clinical
events and health-service use. Version 0.11 adds those two general outcome
families. Version 0.12 adds translation and adaptation methods. Version 0.13
adds `ProductUse` for an existing value set or other reusable product that is
the object of analysis, comparison, or synthesis.

The production process uses two strong calls per paper. Call 1 extracts a
draft. A fresh Call 2 compares that draft with the full source and returns the
complete corrected record. Deterministic validation rejects invalid records;
it is not an AI stage. A 20-paper Opus test found no MAJOR scientific error,
and its corrected records pass 20/20 checks.

The completed run has 209 corrected records, and all 209 pass deterministic
validation. They represent 207 studies, one correction notice, and one excluded
paper. The records contain 15,430 typed items, 1,951 findings, 939 limitations,
96 products, 188 source conflicts, and 210 explicit gaps.

Each paper used one Opus draft and one fresh Opus source review. Review of the
drafts returned 7 PASS, 202 MINOR, 0 MAJOR, and 846 corrections. The explicit
gaps preserve unresolved source or ontology facts without forced mappings.

Version 2 loaded into a new SQLite database. The build has 209 publications,
207 studies, 15,430 items, 1,024 projects, and 242 accepted project-publication
links. Its integrity and expected-count checks pass.

The release registry has 331 identities and 395 exact aliases. Conservative
normalization maps 1,022 uses and leaves 3,457 unresolved, with no collision or
unverified match. A larger 436-row candidate was rejected for this release
because it over-merged distinct versions, dated value sets, bolt-on products,
and related software. It is a review queue, not approved registry data.

The shared preview is not the final analytical release. The full
aggregate-validity rerun against all 100 questions and focused version-0.14 gap
work remain. Do not claim that the 100 questions pass. Final analytical release
needs those gates; KEEP_AS_GAP decisions do not change the version-0.13 schema.
