# Round 1 decisions and gaps

## Accepted corrections

- Replace free-text `study_type` with an exact-one primary family and ranked
  controlled purposes.
- Split approach, time, comparison, allocation, data origin, publication form,
  execution state, and result state.
- Store data origin per `DataUse`; reject `MIXED_ORIGIN`.
- Store an exact registry identity separately from its use context and
  function.
- Split instrument, method, protocol, scoring, and model uses.
- Add completion assistance. Young children can give assisted self-reports
  without becoming proxy respondents.
- Keep product development, approval, validation, and deployment as separate
  dated assertions.
- Restrict products to explicit reusable outputs. Findings are not products.
- Keep source conflicts separate from ontology gaps.
- Keep structured aggregate values inside selected findings. Do not build a
  claim record for every coefficient.
- Store evidence locators on extracted items. Do not build a universal
  assertion graph.

## Paper-level gaps

| Paper | State | Affected fact | Current action |
|---|---|---|---|
| G010 | `UNCERTAIN_MAPPING` | Identity and provenance of historic EQ-5D input | Keep as visualized historical input; do not invent a source study |
| G125 | `UNCERTAIN_MAPPING` plus source conflict | Household-size count exceeds the sample | Keep both source values; exclude the cell from aggregation |
| G131 | `UNCERTAIN_MAPPING` | Present-paper boundary across wider project steps | Attach origin to each data asset; do not force one study-level origin |
| G154 | `UNCERTAIN_MAPPING` | “Redundancy” and “obsolescence” taxonomy wording | Retain both source labels pending domain review |
| G160 | `UNMODELED_ASPECT` | Full construction and weighting of the interviewer score | Keep method and product text; test recurrence before adding keys |
| G168 | `UNMODELED_ASPECT` | Youth co-researcher involvement | Use agent roles for now; test a stakeholder-involvement record in round 2 |
| G014 | Source conflict | Risk-of-bias categories total 188 for 187 studies | Keep reported values and conflict; do not repair silently |
| G015 | Source conflict | Article reverses EQ VAS endpoint wording | Keep source wording and conflict; do not normalize silently |
| G146 | Source conflict | Incompatible cTTO observation counts | Preserve both statements and their locators |

## Open questions for round 2

1. Does the primary-family rule remain stable for papers with several major
   purposes?
2. Is `HEALTH_OUTCOME_RESEARCH` required as another primary family?
3. When does one mixed study require two `StudyPart` records?
4. Which controlled `StudyFactor` roles are stable across conditions,
   interventions, exposures, comparators, and subgroups?
5. Which source terms reliably distinguish approached, recruited, enrolled,
   completed, and analyzed sample stages?
6. Which product-state issuers and evidence sources count as approval,
   validation, or deployment?
7. Does task design require a small reusable structure, or is protocol-linked
   source text sufficient?

## Round-2 gate

Retain all 15 papers as regression cases and add 15 diverse new papers. Two
independent applications must use only the accepted vocabulary. Proposed keys
and values go to the gap log. An independent reviewer adjudicates the deltas.

Round 2 can increase again only if earlier papers still fit, family assignment
is stable, and new gaps are mostly registry additions or open concepts rather
than new structural keys.
