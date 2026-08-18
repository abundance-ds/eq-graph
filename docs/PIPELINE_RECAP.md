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
project. DOI grouping reduced 220 JATS files to 209 publications. One AI call
per paper then made the full-text inclusion decision and drafted the semantic
record. The result was 207 studies, one exclusion, and one correction notice.

The earlier project-folder match was not trusted as the final project link. A
separate strong-model linkage pass received each paper and every project that
passed the hard year rule. It could use authorship as evidence, but not as a
rule. An independent audit checked the 260 nominated paper-project pairs. The
trusted graph contains 242 accepted links. Fourteen possible links remain as
review records and do not create support or output relationships.

## Model and source roles

- Deterministic code parses JATS metadata and loads the graph. No AI model is
  used for these steps.
- The low-cost model produced the first semantic draft.
- A strong full-source audit passed 121 study records unchanged and corrected
  86. A low-cost result is therefore not trusted final evidence.
- Current safe policy: use a strong model for final semantic ingestion or keep
  a mandatory strong-model verification pass. A direct comparison of these two
  strong-model workflows has not yet been run.
- PDF bibliography extraction is separate from semantic paper extraction. The
  evidence agent must not reconstruct a long reference list.

## Current boundary

- The 209-paper graph is the audited project-first JATS corpus.
- The 3,148-paper retained set is the next large retrieval and assessment set.
- The web application is complete enough for data integration, but it still
  uses temporary reference fixtures.
- The public application must use a sanitized serving database. Source files,
  filesystem paths, and unresolved references stay private.
