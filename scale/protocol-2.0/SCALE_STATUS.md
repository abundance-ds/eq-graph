# Protocol 2.0 scale status

**Paused 2026-08-05:** screening is complete and validated. No scale full text has
been downloaded. Resume from `PAUSE_2026-08-05.md`.

## Current result

The controlled source union is complete for 222 profiles accepted by binary identity
QA. A total of 94 people remain outside the author route: 45 original profile flags and
49 profiles held by the new QA.

- People in the author route: 222.
- People held for review: 94.
- Additional plausible profile assignments held for review: 76. None are included.
- Final review queue: 137 people. This combines 94 primary holds with people who have
  additional proposed profile IDs.
The OpenAlex and funding-only stage produced these intermediate counts:

- Unique works from accepted author profiles: 27,244.
- EuroQol funding-metadata works: 739.
- Funding-only additions: 127.
- Union: 27,371 works.
- Articles and reviews: 22,022.
- Candidate articles with reconstructed abstract text: 14,836.
- Candidate articles without an abstract: 7,186.
- DOI duplicate groups before bibliographic QA: 27.

The accepted identifier routes added 14,102 ORCID records and 3,110 PubMed records.
PubMed used exact accepted ORCID IDs. It did not use author names. The complete input
contained 44,583 source records. Exact DOI, PMID, and normalized title/year matching
produced 28,600 unique records.

- Article or review candidates after the union: 23,175.
- Candidates with nonempty abstract text: 14,853.
- Candidates with at least 80 abstract characters: 14,780.
- Candidates with no abstract text: 8,322.
- Exact title/year groups with alternate identifiers: 667. The merge retained every
  alternate DOI and PMID in the record and audit table.

Exact DOI or PMID enrichment from Europe PMC recovered 3,568 abstracts in 314 batch
requests. The current screening input contains 18,348 records with at least 80 abstract
characters. A total of 4,827 records remain unavailable or too short.

Scale prompt v1 keeps all relevance rules from validated pilot prompt v3. It adds one
rule: exclude an unusable abstract field as E5 instead of stopping the batch. The
validation set contained the prior 80 reference records and all six known invalid
abstract fields. The prompt had zero outcome errors. It correctly excluded all six
invalid fields. The operator also inspected the first 60 production decisions and
found zero outcome errors. Neither check is independent validation.

The production screen is complete. All 918 batches and all 18,348 records were
submitted. A total of 3,148 are retained and 15,200 are excluded. All record IDs,
decision codes, and outcome-code pairs validate. There are no remaining batches.

The final retention rate is 17.16%.

## Blinded exclusion audit

A separate AI subagent independently reviewed a simple random sample of 100 exclusions
from the 1,527 fresh exclusions outside the prior operator check. The seed was
`20260805`. The reviewer saw the frozen prompt, titles, metadata, and full stored
abstracts. It did not see the production decisions, codes, or reasons.

- Independent AI agreement: 94/100.
- Records sent to adjudication: 6/100.
- Confirmed false exclusions after direct scope adjudication: 0/100.
- Decision: continue scale prompt v1 without a rule or prompt change.

The six disagreements concerned clinical dashboard effects, stated-preference survey
guidance, core outcome-set adoption, surrogate clinical endpoints, a QOL dashboard
trial, and PROM-result visualization. None developed or evaluated a health measure or
health-state valuation method. This check is not independent human validation.

At the 6,000-record checkpoint, a fresh separate AI subagent reviewed 100 different
exclusions sampled from a 4,707-record frame with seed `2026080502`. It agreed on 98
and retained two for adjudication. One measured the clinical utility of genetic testing;
the other designed dashboards that present PROM data. Neither measured health or
wellbeing or evaluated a health measure. Audit v2 therefore found 100 true negatives
and no confirmed false exclusion. The frozen prompt is approved for completion.

The funding route contains 686 articles or reviews. Of these, 547 have an abstract and
139 do not. A total of 377 funding-route works include a EuroQol award ID.

## Funding-route pilot check

The metadata route matched 67 of the 201 retained pilot articles. Full text was
available for 49 of these matched articles.

- Current-study funding: 33/49 metadata matches (67.3%).
- Current-study funding found by metadata: 33/45 assessed funded studies (73.3%).
- Any explicit EuroQol support: 42/49 metadata matches (85.7%).
- Explicit EuroQol support found by metadata: 42/59 assessed support statements
  (71.2%).

These results confirm that the route adds useful records. They also confirm that it is
not a final funding label. It misses supported articles and includes records where
EuroQol did not fund the current study.

## Evidence rules

- OpenAlex funder metadata is a discovery signal. It is not final proof that EuroQol
  funded the current study.
- Full text must confirm the funding scope.
- Only profiles with a binary `accept` decision are in the author route.
- The author route uses only the chosen profile ID. It does not add unreviewed split
  profiles. Some split IDs overlap another person's chosen ID.
- All retrieved abstract text is present without truncation in the screening inputs.
- The prompt excludes a longer pseudo-abstract as E5. It does not infer relevance from
  the title.

## Next work

1. Complete an independent human sample check before scale full-text processing.
2. Review or resolve the 94 held people and 76 additional profile assignments in
   `profile-review-queue-final.csv` as a separate identity work queue.
3. After those gates, retrieve full texts for the retained set. Keep unavailable texts
   unassessed.

## Outputs

- `profile-scale-readiness.csv`: all 316 people and their scale status.
- `profile-review-queue-final.csv`: all primary holds and extra profile assignments.
- `profile-qa-v1/accepted.csv`: 222 profiles in the current author route.
- `profile-qa-v1/held.csv`: 49 profiles added to the review queue by binary QA.
- `profile-qa-v1/inspection-set.csv`: all holds and the accepted-profile check sample.
- `funding-metadata-discovery.csv`: the independent funding route.
- `openalex-discovery.jsonl`: accepted author-route and funding-route union.
- `openalex-discovery-summary.json`: counts and validation state.
- `identifier-sources/`: one normalized ORCID and PubMed source file per accepted
  profile.
- `identifier-source-summary.json`: identifier-route counts and validation state.
- `source-union.jsonl`: deduplicated source union with full abstract text.
- `source-union-title-year-identifier-variants.csv`: alternate identifiers merged by
  exact title and year.
- `source-union-summary.json`: source-union funnel counts.
- `source-union-validation.json`: duplicate and completeness checks.
- `article-corpus.jsonl`: 23,175 article or review candidates after exact-identifier
  abstract enrichment.
- `abstract-enrichment-summary.json`: exact Europe PMC enrichment counts.
- `abstract-unavailable-or-short.csv`: 4,827 records outside the screening input.
- `screening-v1-validation/`: 86-record prompt validation with zero outcome errors.
- `screening-v1/`: frozen 18,348-record production input and current decisions.
- `screening-v1/progress.json`: cumulative validated production progress.
- `screening-v1/retained.csv`: 3,148 records retained for the next gate.
- `screening-v1/excluded.csv`: 15,200 screened exclusions.
- `screening-v1/FINAL_SCREEN.md`: final funnel, codes, checks, and limitations.
- `exclusion-audit-v1/`: blinded sample, independent decisions, comparison, six
  adjudications, and evaluation.
- `exclusion-audit-v2/`: second nonoverlapping blinded sample, independent decisions,
  comparison, two adjudications, and evaluation.
- `funding-metadata-pilot-evaluation.json`: comparison with pilot full-text evidence.
- `../../docs/PROVENANCE.md`: source-to-result evidence trail and known provenance
  limits.
- `PAUSE_2026-08-05.md`: dated state and ordered restart instructions.
