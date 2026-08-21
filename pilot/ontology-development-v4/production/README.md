# Typed production extraction

This stage applied ontology version 0.13 to 209 JATS papers. It packages a new
version-2 database and does not change the version-1 database.

Each paper gets two isolated `claude-opus-5` calls. The first call returns a
draft JSON record. A fresh second call compares the draft with the full source
and returns the complete corrected record. Deterministic code then checks the
record shape, controlled values, IDs, relations, registry use, and evidence
locators. Markdown views and search terms are derived from valid JSON. The AI
does not write graph triples.

The AI preserves exact scientific labels and leaves registry IDs empty. The
full registry is not in the prompt. Deterministic code applies reviewed exact
aliases after extraction and leaves ambiguous labels unmapped.

Two unseen 20-paper tests passed after focused repair. A later cross-audit
found missing software structure, so the first rebuild was stopped and
invalidated. Two fresh eight-paper tests then checked the correction. A live
audit of the version-0.8 restart found one missing experimental-design method
role, so that run was also stopped. Version 0.9 adds the bounded role. Four
difficult DCE-design papers then had zero MAJOR source defects and no new
ontology gap. The version-0.9 rebuild stopped after 48 records when one-paper
audits found repeated sample-flow gaps. Version 0.10 added three general flow
stages. Version 0.11 added two general outcome families after a focused test.
Version 0.12 added translation and adaptation methods. Version 0.13 added
`ProductUse` for existing products that are analysed, compared, or synthesized.
A 20-paper Opus test found no MAJOR scientific error. Its corrected records
pass 20/20 deterministic checks. The uniform version-0.13 run loads into a
separate version-2 database.

## Completed run

- All 209 corrected records pass deterministic validation: 207 studies, one
  correction notice, and one excluded paper.
- The records contain 15,430 typed items, 1,951 findings, 939 limitations, 96
  products, 188 source conflicts, and 210 explicit gaps.
- Each paper used one Opus draft and one fresh Opus source review. Draft review
  returned 7 PASS, 202 MINOR, 0 MAJOR, and 846 corrections.
- The private version-2 SQLite database passes its count, relation, and integrity
  checks. It contains 1,024 projects, 242 accepted project-publication links,
  9,363 citation occurrences, and 573 resolved internal citation edges.
- Conservative registry normalization maps 1,022 uses and leaves 3,457
  unresolved. It has no collision or unverified match. The registry contains
  331 identities and 395 exact aliases.
- A 436-row expansion candidate failed semantic review because it over-merged
  distinct versions and products. It remains a review queue and was not
  applied. Uncertain labels stay unmapped.
- The shared preview is not the final analytical release. The full
  aggregate-validity rerun against all 100 questions and focused version-0.14
  gap work remain. Record validity does not show that the 100 questions pass.

## Files

- `TASK.md`: short extraction instructions.
- `REGISTRY.tsv`: reviewed identities used by deterministic normalization.
- `REGISTRY_ALIASES.tsv`: one exact alias per row.
- `CALIBRATION.tsv`: 20 unseen papers and source hashes.
- `CONFIRMATION.tsv`: 20 fresh confirmation papers and source hashes.
- `REBUILD_V2.tsv`: frozen 209-paper rebuild manifest.
- `schema.py`: generated JSON Schema for model output.
- `validate.py`: deterministic structural and semantic checks.
- `prepare.py`: verified prompt and metadata preparation.
- `prepare_repair.py`: full-record repair prompts from reviewed feedback.
- `run.py`: one isolated model call per paper.
- `run_claude.py`: parallel isolated Claude extraction and review calls.
- `REVIEW_AND_CORRECT_TASK.md`: second-call source-review rules.
- `prepare_review.py`: one review-and-correction prompt per paper.
- `review_schema.py`: review summary and corrected-record output contract.
- `normalize_registry.py`: exact reviewed alias resolution without AI edits.
- `DECISION.md`: production approval and rebuild controls.
- `rebuild-v2-v013-gap-audit-01.md`: governed recurrent-gap proposals and
  release implications.

The corrected record does not overwrite the first extraction. The draft,
review summary, corrected record, source hashes, prompt hashes, and run data
remain separate. Only a corrected record that passes deterministic validation
can enter normalization and database loading.
