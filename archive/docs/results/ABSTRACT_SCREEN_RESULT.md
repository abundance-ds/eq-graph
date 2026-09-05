# Corrected abstract-screen result

## Method

- Input: 18,348 journal articles or reviews with a usable abstract and a
  resolved publication year.
- Model: `gpt-5.6-terra`, medium reasoning, through the Codex ChatGPT
  subscription. Each call received one publication.
- Task: route a publication to `RETRIEVE_FULL_TEXT` when it could have explicit
  EuroQol support or be an output of a listed funded project. Otherwise, return
  `EXCLUDE`. Retrieval is not final inclusion.
- Output: one validated JSON object with `decision`, `project_ids[]`, and a
  short `reason`.
- Project rule: a project cannot start after the publication year. The first
  17,789 completed records received every project that passed this rule. After
  an operator decision, the remaining 559 records received only projects that
  started within the previous 10 years. No completed record was rerun.
- Execution: records were grouped by publication year to reuse the stable
  instruction and project prefix. Each result was written atomically, so the
  run could stop and resume without repeating completed work.

## Result

- `RETRIEVE_FULL_TEXT`: **1,679** (9.15%).
- `EXCLUDE`: **16,669** (90.85%).
- Completed: **18,348/18,348**.
- Current errors: **0**.

The former topic-based result of 3,148 retained and 15,200 excluded records is
historical. It does not control full-text retrieval or final eligibility.

## Checks

- Every input record has exactly one result; there are no duplicate or unknown
  record IDs.
- All decisions, project IDs, reasons, model fields, and project-year rules
  pass deterministic validation.
- All 559 records after the cutoff have `project_lookback_years=10`; their
  nominated projects satisfy that window.
- A stratified random check used seed `20260824`: five retrievals and five
  exclusions, including four records from the 10-year tail. Nine decisions
  were appropriate. One paper about eye-care services was over-routed because
  an author led a different EuroQol project. The reason itself noted the topic
  mismatch. This is a precision error, not a false exclusion; the full-text
  gate must reject such weak links.

The same precision error was later found at scale in the retrieval queue: 424 of
the 1,679 routed records carry a hedged reason and 217 nominate no project at all.
Records removed on that basis are registered in
[`SCOPE_SCREEN_RESULT.md`](SCOPE_SCREEN_RESULT.md).

## Old-to-new transition check

The corrected screen did not only reduce the queue:

- Old retain, now retrieval: 960.
- Old retain, now exclusion: 2,188.
- Old exclusion, now retrieval: 719.
- Old exclusion, now exclusion: 14,481.

A random sample of ten old-retain/new-exclusion records used seed `20260824`.
All ten exclusions were correct under the funded-project scope. The old screen
had retained unrelated instrument development, psychometric, translation,
utility, and valuation research because those topics matched its former scope.
The corrected screen found no EuroQol support signal or concrete funded-project
link. No sampled case required human adjudication.

## Evidence and next gate

The production record is local and ignored by Git:
`scale/protocol-2.0/abstract-screen-v2-codex-r5/`. It contains the manifest,
frozen prompt, JSON schema, one atomic record per publication, run traces,
compiled results, and final progress summary. Runs r1-r4 are superseded
diagnostic attempts.

- Frozen prompt SHA-256: `2bc59f11b92c0aaf1823bb1b97457dd51721f0fd94b4684faade1e3fef928aef`.
- Compiled result SHA-256: `e2db4c7a6166c9805a69d5692c44b9431ff83c45abed4ee66aba5d74f427239b`.

Full-text retrieval is now complete: 1,607 verified sources and 72 unavailable
records. See
[`FULLTEXT_RETRIEVAL_RESULT.md`](FULLTEXT_RETRIEVAL_RESULT.md). Full text must
confirm explicit EuroQol support or an accepted funded-project link before a
paper can enter the graph.
