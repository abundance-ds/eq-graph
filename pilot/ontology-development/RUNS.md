# Development run record

All development runs used protocol version 1, the same short task, the same paper order and the same Codex model configuration.
Each round used a fresh agent context.
The agent could see only its lineage state and the papers available through the current round.

| Round | Batch | Lineage A commit | Lineage B commit | Lineage C commit |
| ---: | --- | --- | --- | --- |
| 1 | `batch-01.tsv` | `92f51c8` | `b6b6cd8` | `8fba6e8` |
| 2 | `batch-02.tsv` | `e3e440c` | `e33c618` | `7f50cfd` |
| 3 | `batch-03.tsv` | `53a1f79` | `cbad9d1` | `d5ef649` |

Branches are `experiment/ontology-a`, `experiment/ontology-b` and `experiment/ontology-c`.
Each run verified the assigned file hashes and byte counts.
Mechanical checks confirmed paper coverage and lineage-only changes before each commit.
No agent saw another lineage or a comparison result during development.
