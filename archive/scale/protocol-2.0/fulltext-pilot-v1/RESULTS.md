# Full-text eligibility pilot: current result

## Gate

The retrieval, conversion, and AI assessment stages are complete. The result is not
final until the human review is complete.

## Pilot

- 40 papers: 20 boundary retained, 10 clear retained, and 10 exclusion controls.
- 31 PDF sources and 9 JATS sources in the final sample.
- 10 PDF candidates failed the strict text check and were replaced within the same
  sample group. The failures remain in `PARSER_FAILURES.tsv`.
- 1 retrieved exclusion control was a conference-abstract supplement and was replaced
  within the same group. The decision remains in `SOURCE_EXCLUSIONS.tsv`.
- 40/40 isolated Claude Sonnet 5 assessments returned valid records. The child
  processes did not receive `ANTHROPIC_API_KEY`.

## AI result, before human review

- Recommendation: 17 include, 23 exclude, and 0 human review.
- Connection: 17 direct EQ, 12 adjacent measurement, 4 application only, 7 unrelated, and 0 unclear.
- EuroQol support: 5 current work, 0 data or prior component, 1 author support, 7 disclosure only, 18 other funder only, 9 none stated, and 0 unclear.

| Sample group | Include | Exclude | Human review |
|---|---:|---:|---:|
| boundary-retained | 7 | 13 | 0 |
| clear-retained | 10 | 0 | 0 |
| excluded-e1 | 0 | 3 | 0 |
| excluded-e2 | 0 | 3 | 0 |
| excluded-e3 | 0 | 2 | 0 |
| excluded-e4 | 0 | 2 | 0 |

## Human action

The human review packet was never completed and was removed on 2026-09-03; Git history keeps it.
