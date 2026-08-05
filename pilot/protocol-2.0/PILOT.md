# Protocol 2.0 pilot audit

Canonical method/status: `../../protocol-2.0.md`.

This file records the completed pilot. The scale screen is now complete and paused
before scale full-text retrieval. See `../../scale/protocol-2.0/PAUSE_2026-08-05.md`.

## Scope

- People: 10.
- Seed: `20260801`.
- PubMed query: v2.
- Retrieval: 2026-08-01 to 2026-08-03.

## Final funnel

- Accepted source records: 3,032.
- Deduplicated records: 1,729.
- Excluded: 21 document junk; 307 non-journal outputs.
- Article records: 1,401.
- Abstracts: 896 valid source abstracts + 186 recovered.
- No valid abstract: 319 excluded, including 6 invalid pseudo-abstracts.
- Ready for title and abstract screen: 1,082.
- Screen retained: 201; excluded: 881.
- Machine-readable full text: 123 available; 78 unavailable.
- Full-text assessment: 81 direct EuroQol; 42 adjacent measurement or valuation.
- Current-study EuroQol funding: 45.
- Project links: 29 explicit; 9 probable; 10 possible; 75 none.
- Article-project edges: 50 across 27 projects.
- Identifier duplicates found during enrichment: 4 merged; 0 remain.
- Validation: passed with scale conditions.

## QA findings

- PubMed v1 missed indexed papers; v2: 262 → 578 records; 65/69 known misses recovered.
- One common-name PubMed profile rejected; its ORCID/OpenAlex sources retained.
- OpenAlex added six eligible journal articles in this pilot; most non-PubMed additions were excluded formats or duplicate versions.
- Scholar counts of 100 are first-page limits, not total publication counts.
- Previous 40-paper AI screen invalid: nine inputs lacked abstracts; scope was too broad.
- Six stored abstract fields were author, citation, publisher, or truncated text. They
  were removed before the final screen. No title-only decision was used.
- Three random 20-record batches and one 20-record boundary check had zero outcome
  errors against operator reference labels.
- The final screen repeated all 80 calibration records with zero outcome differences.
- The calibration was not an independent second-human assessment.
- Full-text retrieval found 123/201 articles. The other 78 have no funding or project
  assessment.
- A separate funding audit prevents publication fees, related-work funding, and
  nonfinancial help from being reported as funding of the current study.
- Two full-text labels have documented manual adjudication.

## Outputs

- `derived/works.json`: screening corpus + exclusions.
- `derived/abstract-enrichment.json`: sources, attempts, duplicate lineage.
- `abstract-unavailable.csv`: excluded missing-abstract records.
- `person-funnel.csv`: per-person counts.
- `screening-corpus-validation.json`: gate validation.
- `screening-final/validation.json`: final screen validation.
- `fulltext/manifest.csv`: full-text retrieval status and paths.
- `paper-assessment.csv`: integrated result for all 201 retained articles.
- `article-project-links.csv`: explicit, probable, and possible candidate edges.
- `fulltext-assessment-validation.json`: full-text and funding validation.
- `PILOT_EVALUATION.md`: pilot decision and scale conditions.
