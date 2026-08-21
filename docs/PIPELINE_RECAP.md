# Pipeline recap

## Two separate discovery routes

```text
PROJECT-FIRST ROUTE                         LITERATURE-FIRST ROUTE
1,024 EuroQol projects                     author and funder searches
  -> candidate project-output matches        -> 28,600 distinct records
  -> 305 works above the match threshold      -> 18,348 usable abstracts
  -> 287 held full texts                      -> title-and-abstract screening
  -> 220 JATS copies                          -> 3,148 retained records
  -> 209 unique DOI papers                    -> full-text retrieval not started
```

The **305** means that an automated project-work match had strong discovery
evidence. It does not mean that a full-text inclusion assessment occurred.
Evidence included an explicit EuroQol grant identifier, a near-exact title
match, or another strong combination of acknowledgement, title, investigator,
and date evidence. This route supplied the first available full-text corpus.

The **3,148** papers came from the much broader author and funder searches.
They passed title-and-abstract screening, but their full texts have not been
retrieved or assessed. They are not part of the 209-paper graph.

## What happened to the 209 papers

Eleven papers had two XML copies because each copy was filed under a different
project. DOI grouping reduced 220 JATS files to 209 publications. One Opus call
per paper made the full-text inclusion decision and drafted the semantic
record. A fresh second Opus call checked the full source and returned the
complete corrected record. All 209 corrected records pass deterministic
validation. The result is 207 studies, one excluded paper, and one correction
notice.

The corrected records contain 15,430 typed items, including 1,951 findings,
939 limitations, 96 products, 188 source conflicts, and 210 explicit gaps.

The earlier project-folder match was not trusted as the final project link. A
separate strong-model linkage pass received each paper and every project that
passed the hard year rule. It could use authorship as evidence, but not as a
rule. An independent audit checked the 260 nominated paper-project pairs. The
trusted graph contains 242 accepted links. Fourteen possible links remain as
review records and do not create support or output relationships.

## Model and source roles

- Deterministic code parses JATS metadata and loads the graph. No AI model is
  used for these steps.
- One isolated Opus call produced each version-0.13 draft.
- A fresh isolated Opus call reviewed the full source and returned each complete
  corrected record. Review returned 7 PASS, 202 MINOR, 0 MAJOR, and 846
  corrections.
- Deterministic validation rejects an invalid corrected record before
  normalization or loading.
- PDF bibliography extraction is separate from semantic paper extraction. The
  evidence agent must not reconstruct a long reference list.

## Current boundary

- The completed 209-paper version-0.13 result is the audited project-first JATS
  corpus. It is separate from the 3,148 screened scale records.
- The version-2 database and shared preview are live. The preview is not the
  final analytical release. The full 100-question aggregate-validity
  rerun and focused version-0.14 gap work remain. No 100-question pass is
  claimed.
- Sixty local PDF-only papers remain outside the audited graph. The validated
  converter repairs their PDF font maps, then creates prose, headings, tables,
  and formula text in one structural pass. PDF-derived facts keep the same
  source-page verification gate as other extracted facts.
- The 3,148-paper retained set is the next large retrieval and assessment set.
- Scale retrieval remains behind the independent human-screening check and the
  held identity queue.
- The application reads a deterministic, sanitized SQLite database built from
  the audited graph. Source files, filesystem paths, unresolved references,
  possible project links, and audit reasoning stay private.
