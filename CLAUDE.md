# CLAUDE.md

This file captures only what cannot be inferred from the codebase itself.

## Rules for editing this file

Both developers and AI agents are expected to add entries as they encounter surprises.

- **Add an entry** when you encounter something unexpected: a build quirk, a non-obvious constraint, a dependency gotcha, or any behavior that would surprise the next agent or developer.
- **Add an entry** when a developer flags an anti-pattern produced by AI — describe the anti-pattern and the preferred alternative.
- **Do not** add codebase overviews, directory listings, or anything discoverable by reading the source.
- Keep entries concise: one line per lesson, grouped under a heading if a theme emerges.

## Known gotchas

- `Working Group` in the EuroQol CSV is multi-value joined with `", "`, but one of the
  groups is itself named `Dissemination, OA fee` — splitting on `", "` silently
  invents two groups for those 5 rows. Match against the closed vocabulary instead.
- Crossref cursor paging returns the **same** `next-cursor` token on every page, so
  consecutive page URLs are byte-identical. Behind any URL-keyed cache this replays
  page 2 forever (it silently inflated a 513-result sweep to "4000"). Use `offset`
  paging for Crossref; Europe PMC's `cursorMark` does advance and is fine.
- Grant numbers are **not** globally unique across funders: Europe PMC
  `GRANT_ID:"2013010"` returns awards from the Norwegian South East Health Authority
  and a Chinese biofuel lab. Always confirm the matching grant's `agency` before
  treating a grant-id hit as evidence.
- Free-text searching a EuroQol project id only works for the 8-digit scheme. Suffix
  ids tokenize apart, and `-RA` collides with "RA" for rheumatoid arthritis — a search
  for `"100-RA"` returned a materials-chemistry paper on ZnO heterojunctions.
- OpenAlex is now **metered** and the free daily allowance is a fraction of a cent; a
  single funders query exhausted it. Do not assume it is a free bulk source.
- Anything whose output lands in git must iterate `set`s in sorted order. Python
  randomizes string hashing per process, so unsorted set iteration silently reordered
  exported evidence and rewrote ~540 tracked files on every identical rerun.
- Publishers 403 automated PDF fetches even for CC-licensed articles (Elsevier, BMJ,
  MDPI, Wiley all did). Treat 401/403 as terminal, not as a retryable failure.
- Europe PMC's `ACK_FUND:"EuroQol"` finds 626 works; the free-text phrase
  `"EuroQol Research Foundation"` finds 1147. The index only holds funding statements
  EPMC managed to parse, so never treat it as the full funder corpus.
- The grant id is printed in the article's acknowledgement text far more reliably than
  it is indexed. Harvesting OA full text and reading ids out of it (within ~300 chars
  of a EuroQol mention, else reused grant numbers produce false hits) is the
  highest-yield attribution route available without paid sources.
- OpenAIRE holds no EuroQol funder records (`funder=EuroQol` returns 0). Do not spend
  time on it for this corpus.

## Anti-patterns to avoid

- Do not attribute a paper to a specific grant on PI-name evidence alone. 344 PIs hold
  1024 grants, so name matching cannot tell which of a PI's grants a paper belongs to;
  it yields a review pool, not an attribution.

## Anti-patterns to avoid

- Do not add content to this file that is already discoverable by reading the source or build scripts — that inflates context without adding signal, reducing AI agent task success rates (see [arxiv 2602.11988](https://arxiv.org/abs/2602.11988)).
