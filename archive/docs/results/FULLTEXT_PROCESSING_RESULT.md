# Full-text processing result

## Result

All **1,607 verified full texts** now have a saved eligibility decision. The
complete result contains:

- **797 included publications** and **810 excluded publications**;
- **603 included publications** linked to one or more funded projects, with
  **642 paper-project links** in total;
- **798 study records** and **54,002 typed evidence items** for the included
  publications.

The final 1,255-paper run added 652 inclusions and 603 exclusions. It used 275
Opus calls through Claude Code and 980 Sol calls through the isolated Codex
subscription. All 1,255 calls saved a record. No runner or validation failure
remains.

## Method

Each call received one verified paper text, deterministic publication metadata,
the abstract-screen result, and only the projects nominated during abstract
screening. The model used an isolated SQLite workspace with three flat tools:
`sql`, `submit`, and `reject`. `submit` checked the schema, controlled values,
scientific identities, relations, and project rules. The same call corrected
reported errors before the record was saved.

The 20-paper reviewed comparison set and the first 332 scale records used the
same governing eligibility and evidence rules. The final 1,255 papers used the
flat SQL interface. Saved records are authoritative for resume, so a switch
between Opus and Sol did not repeat completed papers.

## Evidence trail and limits

- Prepared manifest SHA-256:
  `336bed1accca17aa00ff49361435ffdd75229026d00daf301952d04a1e606ff3`
- Final run summary SHA-256:
  `017147bed861d75d88c78d4ac829118a29ba81b7668f34a9825f30db3b4969be`
- Extension log SHA-256:
  `de2873fe2763c322bd964e13693dae2c77434e77eebe3c2fc7458bc8c710b74c`
- Local run folder:
  `scale/protocol-2.0/fulltext-sql-scale-v1/run-01/`
- The complete records passed the tool's deterministic checks. The current
  top-level test set passes 60 tests.
- Registry consolidation retained 3,311 global Instrument, Method, Protocol,
  Model, Software, and Product identities. It merged 31 punctuation-only
  duplicates and withheld two ambiguous acronym aliases instead of forcing a
  false merge.
- All 797 included records pass the final schema and semantic checks. The
  private and public databases pass integrity, foreign-key, controlled-value,
  project-year, identity, and privacy checks.

## Loaded graph

- 797 publications: 452 JATS and 345 PDF sources;
- 798 studies and 54,002 typed evidence items;
- 13,581 public scientific uses, all mapped to canonical identities;
- 5,845 findings, 3,666 limitations, and 489 research products;
- 642 confirmed paper-project links across 603 publications;
- 4,919 authorships, including 90 explicitly unresolved identities;
- 791 exact OpenAlex matches and six manual lookup routes.

The 100-question validity test is complete: 54 pass, 36 partial, 6 fail, and 4
are not testable. The failures need external data and do not justify an ontology
change.
- The 72 papers without verified full text remain unassessed.
