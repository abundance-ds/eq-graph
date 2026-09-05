# Version-2 freeze record

Frozen: 2026-08-16, before the first lineage run.

## Scope

- Source content commit: `9d369b0`.
- Three lineages use the same paper order, task, purpose, questions and model configuration.
- Four development rounds contain 40 unique papers from 30 project groups.
- Rounds one to three are byte-for-byte copies of the version-1 manifests.
- The ten-paper holdout uses ten unique project groups.
- Holdout DOI and project-group sets are disjoint from development and calibration.
- Every manifest path, SHA-256 value and byte count passed validation.
- Two independent read-only reviews checked the purpose, task, questions and protocol before freeze.
- Version-1 ontology work, hidden selection labels, frozen probes and legacy extractions are excluded from development agent contexts.

The JATS handling decision remains in [`../ontology-development/XML_AUDIT.md`](../ontology-development/XML_AUDIT.md).
Raw JATS is canonical for deterministic metadata.
The version-2 experiment tests semantic granularity from normalized full text.

## Frozen file hashes

| File | SHA-256 |
| --- | --- |
| `PURPOSE.md` | `ec7738dc2b843fcffb00d834bfece34a376bbf82232b160d01335eb4abe731fe` |
| `USER_QUESTIONS.md` | `0280105481f1d068b76ae564e1d84c0b92cf4d31fb8f9a8eb0d64ec763bc0c1c` |
| `TASK.md` | `a468afcdfbdb2fc4109a01104cccd670ca65466e40a451288a3944232101a337` |
| `PROTOCOL.md` | `a7fd41f6cbdd5607e54ee8fb3e0eea71e1b7ca1a289eb7fba1304a652eba81e2` |
| `PROBES.md` | `40e385db5975a044d2d6ebffde6ef666071a9e2da5cc9cd89415d134745b3099` |
| `batches/batch-01.tsv` | `d19416ccf006379628d53f049f00f1d4e106b37e786da4706db9fda45908a204` |
| `batches/batch-02.tsv` | `439ec5bf65e914a23ce1a3e560ecfea1284392264dc6443169ce7bce754ef410` |
| `batches/batch-03.tsv` | `194792375b317e320a0a6e7258f092c8ce6c3f13dd2149c6e42e55f2fe61b834` |
| `batches/batch-04.tsv` | `c89a50f7e08394aec3a2aec2f39bd2d3db253647cdb53a420533f3dd9028cccc` |
| `batches/holdout.tsv` | `918398ed3539485406f6d020a60664b5e1ad5b16efd7745cfd632b08ee98bfb5` |

Do not change these files during development.
If a material change is required, invalidate affected runs and freeze a new experiment version.
