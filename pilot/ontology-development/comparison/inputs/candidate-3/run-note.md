# Run notes

## Round 1

- Lineage: B
- Round: 1
- Batch: `batch-01.tsv`
- Task version: 1, frozen 2026-08-16
- Protocol version: 1, frozen 2026-08-16
- Branch: `anonymous/candidate-3`
- Base commit: `45018e8e38dd8ed578847c05274fb2977359411e`
- Agent: Codex, GPT-5 family
- Run time recorded: `2026-08-16T17:45:36+02:00`

All ten article SHA-256 values matched the batch manifest. The run used only the frozen task files, batch manifest, and the ten supplied article files in this sparse worktree. No prior lineage state existed.

The batch was sufficient for an initial paper-level ontology. It supports contribution, design, focal-entity, perspective, comparison, evaluation, output, and limitation concepts. It does not support a stable database schema. The small, related corpus has a strong EuroQol and preference-based measurement focus, so later rounds must test transfer to papers with different instruments and study purposes.

## Round 2

- Lineage: B
- Round: 2
- Batch: `batch-02.tsv`
- Task version: 1, frozen 2026-08-16
- Protocol version: 1, frozen 2026-08-16
- Branch: `anonymous/candidate-3`
- Start commit: `b6b6cd88763e070afbedfcfe5cb201dbc283c018`
- Agent: Codex, GPT-5 family
- Run time recorded: `2026-08-16T17:58:34+02:00`

All ten article SHA-256 values and byte counts matched the batch manifest. The run used only the task files, inherited Candidate 3 record, batch 02 manifest, and the ten supplied batch 02 articles in the sparse worktree.

Round 2 retained the question-and-relation form. It added translation, method evaluation, substantive outcome analysis, and implementation feasibility as contribution roles. It also made study components, evidence-unit roles, data-source compatibility, score derivation, downstream modeled outcomes, and incremental measurement value explicit. No fixed database schema or serialization was added.

The batch extends the ontology beyond instrument development and psychometrics, but it remains concentrated on EuroQol measures. It does not establish general thresholds for method interchangeability, cross-country language transfer, pooled-dataset compatibility, or system-level implementation feasibility.

## Round 3

- Lineage: B
- Round: 3
- Batch: `batch-03.tsv`
- Task version: 1, frozen 2026-08-16
- Protocol version: 1, frozen 2026-08-16
- Branch: `anonymous/candidate-3`
- Start commit: `e33c6181af6accad5f8ddc1c07440c8ff800b9fa`
- Agent: Codex, GPT-5 family
- Run time recorded: `2026-08-16T18:06:14+02:00`

All ten article SHA-256 values and byte counts matched the batch manifest. The run used only the task files, inherited Candidate 3 record, batch 03 manifest, and the ten supplied batch 03 articles in the sparse worktree.

Round 3 retained the question-and-relation form. It added explicit evidence-lineage relations for reused datasets, shared samples, supplied inputs, replications, and extensions. It also added data integrity and sample quality as an evaluation family. Procedure and data-product examples now include direct and indirect costs, DALYs, population norms, inequality indices, and survey quality controls. No fixed database schema or serialization was added.

The batch shows that paper independence cannot be inferred from separate identifiers. Several articles reuse the same oncology, Chinese valuation, Trinidad and Tobago, or EQ-DAPHNIE evidence. The vision-impairment cost study broadens the ontology beyond an instrument-centered use, but the corpus remains concentrated on EuroQol-related research. The round does not resolve general thresholds for online-panel representativeness, pooled-sample compatibility, child-versus-adult valuation transfer, or method interchangeability.
