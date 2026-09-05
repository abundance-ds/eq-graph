# Production workspace

Registry files and loader code for ontology 0.13. The pipeline imports from this directory.

## Code

- `load_research_v2.py`: loads release records into the typed SQLite database. Run it as shown in [scripts/README.md](../../../scripts/README.md).
- `validate.py`, `schema.py`, `normalize_registry.py`: structural checks, JSON Schema, and exact alias resolution. Imported by `pipeline/fulltext_ingest_tool.py`.
- `research_schema_v2.sql`: the typed schema.

## Registry files

- `REGISTRY.tsv`: reviewed identities.
- `REGISTRY_ALIASES.tsv`: one exact alias and use type per row.
- `CONCEPT_MAP.tsv`: concept-to-identity mapping.

The release build copies these under `scale/protocol-2.0/fulltext-release-v1/`.

## Release inputs

- `release-inputs-v2/`: publication manifests and OpenAlex metadata.
- `person-citation-sprint-v2/`: resolved person, authorship, citation, and co-authorship files.
- `single-agent-pilot/native-opus-clean-check-01/`: 20 extraction records that form part of the 1,607 release results ([RESULTS.md](single-agent-pilot/RESULTS.md)).
- `sql-agent-pilot/`: workspace schema and prompt template of the SQL extraction ([RESULTS.md](sql-agent-pilot/RESULTS.md)).

The interim-database working files and the other pilot results are in [`archive/pilot/ontology-development-v4/`](../../../archive/pilot/ontology-development-v4/).
