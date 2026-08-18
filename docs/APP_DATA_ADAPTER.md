# Application data adapter

## Flow

```text
audited private graph database
  -> deterministic serving-database builder
  -> sanitized read-only SQLite database
  -> Nitro story, graph-status, and chat endpoints
  -> browser interface
```

The builder is `scripts/build_serving_database.py`. It copies the 1,024 project
records and the assessed 209-publication evidence layer into simple research
tables. These tables cover publications, studies, accepted project links,
authors, study types, designs, populations, samples, countries, instruments,
methods, models, concepts, outcomes, findings, limitations, products, datasets,
protocols, and source conflicts.

The serving database does not contain full text, source file paths, extraction
paths, unresolved references, external citations, possible project links, or
project-link audit reasoning. The full text stays in the private corpus. The
audited database keeps its own source record and hash. The serving database has
only a `full_text_format` flag, so it cannot expose a local file.

## Runtime

`web/server/utils/servingSqlite.ts` opens the database in read-only and defensive
mode. Its authorizer accepts reads and SQL functions only. The AI has one SQL
tool. Query results stop at 200 rows.

The main data routes are:

- `GET /api/story`: narrative totals and series
- `GET /api/graph`: project, study, and country layout data
- `GET /api/graph/status`: live database totals
- `POST /api/chat`: AI answers through the same read-only database

The current build has 1,024 projects, 209 assessed publications, 207 studies,
242 accepted project-publication links, 871 findings, and 602 limitations.
These publication counts describe the assessed local corpus, not all EuroQol
literature.

## Build and check

From the repository root:

```sh
python3 scripts/build_serving_database.py \
  --source pilot/ontology-development-v3/production-calibration/graph-neutral-209-run-02/euroqol-research-graph-citation-safe.sqlite \
  --output web/server/data/serving.sqlite
python3 scripts/check_serving_database.py web/server/data/serving.sqlite
```

The generated database is not in Git. The checked build has SHA-256
`f05816073d92288d717af1e16cc0f5bcb152d38fffb2d2a41e23382790c5c473`.
Its audited input has SHA-256
`69eb1c76fa71ec4c7a51588cf9cc29a38438c77a5d9d3111d6d97348434dbf32`.
