# Scale full-text eligibility pilot

## Purpose

This pilot tests the full-text inclusion rule before bulk retrieval. It does not
extract scientific findings, change the ontology, link projects, or load the graph.

```text
frozen screen
  -> metadata availability inventory
  -> balanced 40-paper sample
  -> verified PDF or JATS source
  -> deterministic Markdown
  -> one blinded eligibility call per paper
  -> blinded human review
```

The sample contains 20 boundary retained papers, 10 clear retained papers, and 10
exclusion controls. The AI does not receive the earlier abstract-screen code or
reason. `ELIGIBILITY_TASK.md` defines the small classification contract.

## Source handling

The inventory uses exact identifiers and records candidates, not confirmed downloads.
It checks Europe PMC and OpenAlex, then uses Unpaywall when neither source gives a
direct file. Retrieval verifies document bytes, source URL, licence label, size, and
SHA-256. It prefers PDFs in this pilot to test the harder parsing path, then uses
Europe PMC JATS when PDF retrieval fails. The verified source remains the source of
record. Markdown is only the AI reading copy.

The strict PDF parser rejects invalid character maps. `PARSER_FAILURES.tsv` retains
each failure. The sample builder replaces a failed paper only with a paper from the
same sample group. Full references remain in canonical Markdown but are removed from
the AI input when a clear final reference heading is present.

An unknown licence label does not permit redistribution. The pilot can use a document
that a public source serves without access control for private analysis, but it keeps
that source private and records the missing label. It never bypasses a paywall.

`SOURCE_EXCLUSIONS.tsv` records a retrieved file that fails the journal-article or
review format gate. The sample builder replaces it within the same group.

## AI and review

Each paper uses one isolated Claude Sonnet 5 call. The runner removes
`ANTHROPIC_API_KEY` from every child process. The output records the EQ connection,
EuroQol support relation, evidence locator, and inclusion recommendation. It does not
extract ontology records. `HUMAN_REVIEW.md` is the next gate.

## Reproduce

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-scale-pilot.txt
.venv/bin/python pipeline/inventory_scale_fulltexts.py
.venv/bin/python pipeline/prepare_scale_fulltext_pilot.py
.venv/bin/python pipeline/retrieve_scale_fulltext_pilot.py
.venv/bin/python pipeline/convert_scale_fulltext_pilot.py
.venv/bin/python pipeline/prepare_scale_eligibility_pilot.py
.venv/bin/python pipeline/run_scale_eligibility_pilot.py
.venv/bin/python pipeline/prepare_scale_eligibility_review.py
.venv/bin/python pipeline/validate_scale_fulltext_pilot.py
```

If conversion records a new parser failure, rerun retrieval and conversion. The
retrieval stage uses the cumulative failure ledger and promotes the next verified
paper from the same group.

Large API caches, source files, Markdown, AI inputs, and raw traces remain local and
ignored. Git retains the compact task, manifests, decisions, validation, and human
review packet.
