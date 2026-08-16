# Version-2 development run record

The valid lineages use the same frozen inputs, paper order, model configuration and explicit no-external-modeling-guidance control.
Each round uses a fresh agent context.

| Round | Batch | Lineage A commit | Lineage B commit | Lineage C commit |
| ---: | --- | --- | --- | --- |
| 1 | `batch-01.tsv` | `84f60d9` | `d5e75b8` | `5ccc284` |
| 2 | `batch-02.tsv` | `0977ffc` | `b920143` | `ec3aeda` |
| 3 | `batch-03.tsv` | `145b7c3` | `22f9159` | `984d1b2` |
| 4 | `batch-04.tsv` | `9f928ee` | `ee9b833` | `0fa020f` |

Branches are `experiment/ontology-v2-a`, `experiment/ontology-v2-b` and `experiment/ontology-v2-c`.
Each valid round verifies source hashes, byte counts, paper coverage, allowed inputs and Markdown integrity before commit.

The first round-one attempt was invalidated as a complete three-lineage set because one agent used external Neo4j modeling guidance.
Its outputs and cause are preserved under `invalid/round-01-attempt-1/` and are not part of development evidence.
