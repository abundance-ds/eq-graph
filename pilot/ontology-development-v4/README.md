# Ontology 0.13

- `ONTOLOGY.md`: domain map and classification rules (read by code).
- `VOCABULARY.tsv`: controlled keys, values, and definitions (read by code).
- `COMPETENCY_QUESTIONS.md`: the 100-question test bank and 20 negative questions.
- `aggregate-validity-v5/`: the 100-question test of the release ([RESULT.md](aggregate-validity-v5/RESULT.md)).
- `production/`: registry files and loader code the pipeline imports ([README](production/README.md)).

## How the ontology was built

Four 15-paper rounds with two independent builders and one reviewer, then five blind regressions, took the ontology from version 0.1 to 0.5.
Version 0.5 fixed the family partition as one ordered 12-family decision table; a blind 60-paper reapplication matched 59 of 60 adjudicated families.
Production calibration on unseen papers then refined the vocabulary to 0.13: `SoftwareUse` (0.6 to 0.8), experimental-design methods (0.9), sample-flow stages (0.10), general outcome families (0.11), translation and adaptation methods (0.12), existing-product uses (0.13).

The round transcripts, regressions, task prompts, and earlier validity tests are in [`archive/pilot/ontology-development-v4/`](../../archive/pilot/ontology-development-v4/).
