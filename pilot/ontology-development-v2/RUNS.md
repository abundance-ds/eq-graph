# Version-2 development run record

The valid lineages use the same frozen inputs, paper order, model configuration and explicit no-external-modeling-guidance control.
Each round uses a fresh agent context.

| Round | Batch | Lineage A commit | Lineage B commit | Lineage C commit |
| ---: | --- | --- | --- | --- |
| 1 | `batch-01.tsv` | `84f60d9` | `d5e75b8` | `5ccc284` |

Branches are `experiment/ontology-v2-a`, `experiment/ontology-v2-b` and `experiment/ontology-v2-c`.
Each valid round verifies source hashes, byte counts, paper coverage, allowed inputs and Markdown integrity before commit.

The first round-one attempt was invalidated as a complete three-lineage set because one agent used external Neo4j modeling guidance.
Its outputs and cause are preserved under `invalid/round-01-attempt-1/` and are not part of development evidence.
