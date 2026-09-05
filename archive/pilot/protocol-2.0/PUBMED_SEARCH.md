# PubMed search v2

## Author block

- `{surname} {first initial}[Author]`.
- Unquoted: PubMed expands additional initials.
- OR `{orcid}[Author Identifier]` when available.
- Compound-surname variants retained.

## Topic block

- Instruments: EQ-5D; EQ5D; EuroQol; EQ-VT; EQ-HWB; EQ-TIPS; EQ-TANDI.
- Concepts: HRQoL; quality of life; psychometrics; validation; mapping; utility; health state; value set; tariff; valuation; TTO; DCE; PROM; QALY; preference-based; cost-utility.
- Fields: title/abstract.

## Records

- Exact expanded query per person: `derived/pubmed-v2-queries.json`.
- Raw ESearch/EFetch: `raw/pubmed/*-v2-*`.
- Parsed output: `derived/pubmed-v2-*.json`.
- `PubmedArticle` and `PubmedBookArticle` retained; type recorded.

## Superseded v1

- Invalid author syntax: quoted single initial, e.g. `"Purba F"[Author]`.
- Effect: disabled automatic initial expansion; major false exclusions.
- Files retained as `*-initial-*` and `derived/pubmed-*.json`.

## Pilot audit

- V1 parsed records: 262.
- V2 parsed records: 578.
- V1 missed 69 confirmed PubMed-indexed explicit-EQ papers found through OpenAlex.
- V2 recovered 65/69 (94.2%).
- Four residual misses: two incomplete PubMed author lists; one author-index defect; one title without a topic-block term.
- Residual control: DOI/title reconciliation with OpenAlex; no further author-query expansion.
- Main cause: quoted single-initial author terms.
- V2 profile check: 7 accept; 2 caution; 1 reject.
- Rejected source: Ciaran O'Neill; common-name contamination; OpenAlex/ORCID retained.
