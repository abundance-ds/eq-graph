# Deterministic JATS metadata audit

Date: 2026-08-17

## Method

- Parse all 220 `input/projects/*/papers/*.xml` files twice.
- Compare a canonical JSON hash for each repeated parse.
- Check required field counts and source-file hashes.
- Use article metadata only. Do not treat data from cited references as
  metadata for the current article.

## Result

- 220 files parsed; 209 unique DOIs; 11 duplicate file copies.
- DOI, PMID, PMCID, title, and journal: 220 files each.
- Abstract: 219 files.
- Publisher: 80 files, as supplied in article metadata.
- Usable licence URL: 211 files.
- Authors: 1,337; files with an ORCID: 102.
- Author roles: 233 values.
- Affiliations: 1,053.
- Correspondence records: 30; files with a corresponding-author email: 95.
- Keywords: 475 values in 88 files.
- Article categories: 460 values in 122 files.
- Funding: 220 normalized records; 118 files have non-empty funding text.
- Dates: 999 records; every file supplies more than one date type.
- References: 9,890; reference DOIs: 8,242; reference PMIDs: 4,411.
- Parse failures: 0.
- Nondeterministic outputs: 0.

## Corrections made during the audit

- Preserve consortium and other group authors from `<collab>`.
- Recover licence URLs from nested licence links.
- Recover reference DOIs from structured identifiers, DOI links, and citation
  text, in that order.
- Preserve publication-specific author keys when an ORCID is absent. Do not
  merge authors by name alone.
- Keep publisher names from cited references separate from the article
  publisher.
- Keep editor roles separate from author roles.

## Decision

JATS XML is the primary source for publication metadata in this repository.
Semantic extraction must receive this metadata as prior context and must not
spend model work on reconstructing it. Missing source fields remain null; the
pipeline does not invent them.
