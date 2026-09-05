# Local JATS production result

## Outcome

The approved one-pass pipeline processed all 209 unique papers that have JATS
full text in the repository.

- 209/209 records are present and structurally valid.
- 206 records are included studies.
- Two records are excluded.
- One record is a correction notice and is kept as publication context.
- The corpus has 182 direct EQ papers, 16 application-only papers, and 11
  adjacent measurement papers.
- Explicit EuroQol support occurs in 201 records. Eight records state no such
  support.
- SQLite contains 3,731 normalized terms, 5,786 record-term links, and 16,471
  fact bullets.
- All nine database, metadata, search, and integrity checks pass.

## Process

```text
JATS XML
  -> deterministic publication metadata and clean article text
  -> one AI call: assess inclusion and, when included, extract the record
  -> deterministic structure, source, and term checks
  -> targeted repair only for a failed or audited record
  -> light normalization and SQLite load
```

The first pass used `gpt-5.6-luna`. The process used a stronger model only for
two final calibration repairs. It did not use separate routine agents for
filtering, extraction, and normalization.

## Evidence by partition

| Partition | Final result | Repair or audit |
| --- | --- | --- |
| Source-checked calibration, 30 papers | 30/30 expected dispositions; 30/30 clean; 22/22 safety checks | Two targeted final repairs; 84.6% exact reference-term recall |
| Random production sample, 50 papers | 50/50 clean | Three formatting repairs |
| Remaining JATS set, 129 papers | 129/129 clean | Three structural repairs; eight connection-label reviews; stratified source audit |

The source audit found no sampled substantive fact that needed correction. It
confirmed one important corpus rule: use of EQ only as a health outcome is
`application_only`; research about an EQ instrument, valuation, mapping,
reference norms, or measurement implementation is `direct_eq`.

## Known limits

- The first 50 records use varied source-locator syntax. Automatic locator
  recognition is 87.2% there and at least 99.8% in later records. Combined
  recognition is 96.7%.
- The flat index has reasonable term and type variation. The loader applies
  only low-risk aliases and keeps source terms.
- This result tests JATS input. PDF text needs a separate calibration before
  scale retrieval.
- The SQLite database and full record trees are local ignored artefacts. Their
  tracked manifests preserve file names, sizes, and SHA-256 hashes.

## Next gate

Calibrate the same one-pass process on the 60 local PDF-only files. Compare PDF
text quality and extraction quality with the JATS baseline. Start lawful scale
retrieval for the 3,148 retained abstracts only after this gate passes.

No new ontology decision is required now. Stop for human review only if PDF
quality causes a repeated extraction failure, a new study type does not fit,
or the corpus policy needs a change.
