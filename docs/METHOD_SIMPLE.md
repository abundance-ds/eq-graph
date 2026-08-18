# Protocol 2.0 method in simple form

This file states the current method without implementation detail.

**Current state, 2026-08-18:** the scale title-and-abstract screen is complete and the
project is paused before scale full-text retrieval. The independent human check and
held identity queue remain. The separate 209-paper local JATS corpus has completed
full-text extraction, source verification, project linkage, and graph loading. It does
not remove the scale-retrieval gates. See
`../scale/protocol-2.0/PAUSE_2026-08-05.md`.

## Method

1. Make one list of EuroQol project leaders and current members.
2. Accept a profile only when its identity is coherent. Hold every wrong, mixed,
   ambiguous, or insufficient profile. Retrieve papers from accepted profiles and from
   EuroQol funding metadata. ORCID and PubMed can add papers only through an ORCID ID
   from an accepted profile. Do not use name-only PubMed discovery.
3. Merge duplicate records by DOI, PMID, then normalized title and year.
4. Keep journal articles and reviews. Exclude records with fewer than 80 abstract
   characters. During AI screening, exclude any longer field that is not a usable
   article abstract. Do not infer relevance from the title.
5. Retain direct EuroQol research and central measurement or valuation research. Exclude
   generic HRQoL, clinical, treatment-preference, and economic-model applications.
6. Retrieve full text for retained papers. Mark unavailable papers as unassessed.
7. Read the full text once to classify EuroQol connection and funding scope.
8. Compare the paper with every project linked to its known people and every canonical
   project ID stated in the full text. Use no similarity score and no candidate cap.
9. Publish only evidence-backed results. Send uncertainty and possible links to review.

## Fixed evidence rules

- Funding metadata is a discovery route, not proof of funding.
- Full text must state the funding scope.
- Authorship or topic similarity alone does not prove a project link.
- An explicit project ID is an explicit link when the ID is canonical and the article
  identifies it as funding or project evidence.
- A probable link needs strong combined evidence from distinctive aims, methods or data,
  authorship, funding, and timing.
- A possible link is a review item, not a confirmed graph edge.
- No full text means no funding or project-link decision.

## Mechanical operations

The following operations do not make research judgments:

- Source retrieval and caching.
- DOI and PMID normalization.
- Exact identifier matching.
- Exact normalized title-and-year matching. Alternate identifiers remain in the merged
  record and audit table. A title prefix is accepted only when the source title
  explicitly ends with an ellipsis during abstract enrichment.
- Random selection for calibration.
- File validation and count checks.
- Full-text format and size safety checks.

## Recorded exceptions

- Six pilot records contained pseudo-abstracts. The audit file records their exclusion.
- Two full-text labels received documented manual adjudication.
- A blinded separate-AI audit sampled 100 fresh scale exclusions. It raised six for
  adjudication. All six concerned clinical use, outcome selection, endpoint methods,
  preference surveys, or result presentation rather than health-measure or valuation
  research. The frozen prompt did not change.
- A second blinded separate-AI audit sampled 100 different exclusions at the
  6,000-record checkpoint. It raised two for adjudication. Both were outside scope, so
  the frozen prompt was approved for completion.
- The first project assessment used a 12-project shortlist. A complete-candidate audit
  supplied 259 omitted candidates across 41 articles and found no additional link. The
  current method has no score and no cap.
