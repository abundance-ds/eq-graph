# Protocol 2.0 pilot evaluation

## Decision

The pilot passes with scale conditions. The title and abstract screen is ready for
controlled scale-up. The full workflow is not ready for unattended graph publication.

## Results

- Screened: **1,082**.
- Retained: **201** (18.6%).
- Full text available: **123/201** (61.2%).
- Full text unavailable and not assessed: **78/201**.
- Direct EuroQol research: **81**.
- Adjacent measurement or valuation research: **42**.
- Current-study EuroQol funding: **45/123** assessed articles (36.6%).
- Strong project links: **38/123** assessed articles (30.9%).
- Possible project links: **10** review items.
- Article-project edges: **50** across **27** projects.

All **123** assessed full texts were direct or adjacent measurement or
valuation research. This result supports the recall-focused screen. It does not measure
the relevance of the **78** unavailable full texts.

## Screening validation

The three random batches contained **60** articles. They had
zero false exclusions and zero false inclusions against the operator reference labels.
The separate **20**-article boundary check also had zero
outcome errors. The final production run repeated all 80 records with zero outcome
disagreements. These labels were not an independent second-human validation.

## Full-text validation

The prompt check repeated **12** articles. After manual adjudication, the
connection, project-link, and project-ID decisions were stable. Two raw funding labels
differed. The separate funding-scope audit replaces the raw funding label for reporting.
It distinguishes study funding from related-work funding, publication fees, and
nonfinancial support.

The first project assessment limited each article to 12 candidate projects. A complete
candidate audit supplied all **259**
omitted projects for the **41** affected
articles. It selected no omitted project, so the canonical links did not change. The
current method uses no similarity score and no candidate cap.

## Scale conditions

1. Keep the frozen screening prompt and prompt hash.
2. Complete profile QA before records enter the scaled corpus.
3. Improve lawful full-text retrieval and keep a manual queue. Pilot availability was only **61.2%**.
4. Do not infer funding or project links for unavailable full texts.
5. Add an independent human check before final graph publication.
6. Send possible links to review; do not publish them as confirmed edges.

## Canonical outputs

- `paper-assessment.csv`: one row for every retained article.
- `article-project-links.csv`: one row for every explicit, probable, or possible edge.
- `pilot-evaluation.json`: machine-readable metrics and validation state.
- `fulltext-manual-adjudications.csv`: preserved manual corrections.
- `project-assessment-v3/evaluation.json`: complete project-candidate audit.
