# Version-2 defect classification

Date: 2026-08-21

## Executive finding

Do not rebuild the paper ontology.

The 74 testable questions contain 15 semantic failures. These failures cluster
in a small number of areas. Most are outside the paper ontology.

| Main cause | Non-pass questions | Interpretation |
|---|---:|---|
| Missing evidence | 36 | Required membership, external citation, host-institution, proposal, complete-literature, or provenance data is absent. |
| Extraction or identity | 19 | Project status, project subject, people, PIs, and institutions are not normalized or are incomplete. |
| Query or serving view | 7 | The private data can help, but the public database or aggregate rule does not expose it safely. |
| Paper ontology | 7 | Seven questions show four possible structural issues; only two justify focused ontology tests. |
| Scientific registry | 5 | Exact method, protocol, product, or bolt-on identities remain unresolved. |

## The 15 failures

| Failure group | Questions | Repair direction |
|---|---|---|
| Stale or invalid project data | Q4, Q40 | Keep source status, add a derived current-state check, remove the test row from analytical views, and type project subjects. |
| PI, author, and collaboration identity | Q14, Q38, Q44, Q74, Q77, Q81, Q84, Q93, Q94 | Resolve people and PIs before person-level aggregation. Do not use publication-local IDs or raw names as people. |
| Unsupported budget allocation | Q10 | Do not allocate a full project budget to every paper instrument. Add an explicit project target or allocation relation before instrument-family funding totals. |
| Unsupported negative funding claim | Q43 | Keep unknown separate from no support. Do not infer no funding from silence. |
| Sample aggregation | Q45 | Add a safe sample-count contract. Distinguish respondent or participant counts from interviewers, evidence units, excluded units, tasks, and model inputs. |
| Population aggregation | Q95 | Keep population labels open, but add a controlled relation for the population’s study role and a governed trait layer for age group and relevant clinical characteristics. |

## Ontology decision

The seven questions marked `Ontology` do not support a ground-up change.

1. **Project research scope: Q10, Q13, Q23.** This is a project-enrichment
   layer, not a change to the paper ontology. Projects need explicit targets,
   intended outputs, and topic assignments with provenance.
2. **Population grouping: Q39 and Q95.** This is a real paper-ontology
   candidate. Open population prose is source-faithful but unsafe for counts.
   Test a small controlled population-role and population-trait addition
   against diverse papers before any version change.
3. **Sample counting: Q45.** This is a real aggregation-contract candidate.
   First test whether a controlled sample unit plus an explicit principal
   denominator relation is sufficient. Do not replace the current exact flow
   stages.
4. **Milestones: Q61.** Do not add a milestone ontology only to answer one
   editorial question. Use a documented editorial selection rule or a view.

No current evidence supports changing primary research family, ranked purpose,
design axes, scientific-use context or function, ProductUse, Finding,
Interpretation, Limitation, or Product.

## Release gates

1. Keep the current ontology at version 0.13 during registry review.
2. Apply only exact registry identities. Leave uncertain labels unmapped.
3. Add aggregate views only when their unit, denominator, overlap rule,
   missingness rule, and relation role are explicit.
4. Do focused source tests for population and sample changes before version
   0.14.
5. Re-run the 100 questions after identity and project-data work. An empty or
   not-testable answer remains valid; a misleading aggregate does not.
