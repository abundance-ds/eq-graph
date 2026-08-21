# Application data adapter

## Flow

```text
audited version-2 records and structured publication metadata
  -> load_research_v2.py
  -> private typed SQLite database
  -> build_serving_database_v2.py
  -> sanitized read-only SQLite database
  -> Nitro story, graph-status, and chat endpoints
  -> browser interface
```

`load_research_v2.py` loads the audited records into the private typed database.
This database keeps source locators, citation occurrences and edges, source
conflicts, and audit material. `scripts/build_serving_database_v2.py` copies
only the data that the application can query.

The public serving database excludes full text, local paths, citations,
possible project links, and audit reasoning. It contains accepted project links
only. The private corpus and typed database remain the evidence and audit layer.

## Runtime

`web/server/utils/servingSqlite.ts` opens the database in read-only and defensive
mode. Its authorizer accepts reads and SQL functions only. The AI has one SQL
tool. Query results stop at 200 rows.

The main data routes are:

- `GET /api/story`: narrative totals and series
- `GET /api/graph`: project, study, and country layout data
- `GET /api/graph/status`: live database totals
- `POST /api/chat`: AI answers through the same read-only database

The shared preview has 1,024 projects, 209 publications, 207 studies, 1,951
findings, 939 limitations, 96 products, and 242 accepted project-publication
links. These counts describe the completed local corpus, not all EuroQol
literature. The full 100-question aggregate-validity rerun remains before a
final research release.

## Build and check

From the repository root:

```sh
python3 pilot/ontology-development-v4/production/load_research_v2.py \
  --run pilot/ontology-development-v4/production/rebuild-v2-v013-normalized-02 \
  --manifest pilot/ontology-development-v4/production/prepared-rebuild-v2-v013/MANIFEST.tsv \
  --projects "input/Funded projects – Table for Download - EuroQol.csv" \
  --project-links web/server/data/serving.sqlite \
  --output pilot/ontology-development-v4/production/research-v2-v013.sqlite \
  --expect-studies 207 \
  --expect-items 15430 \
  --expect-mapped 1022 \
  --expect-unresolved 3457
python3 scripts/build_serving_database_v2.py \
  --source pilot/ontology-development-v4/production/research-v2-v013.sqlite \
  --output web/server/data/serving.sqlite
python3 scripts/check_serving_database_v2.py \
  --expect-projects 1024 \
  --expect-publications 209 \
  web/server/data/serving.sqlite
```

The generated databases are not in Git. `--project-links` carries the 242
accepted links from the current serving artifact into a fresh private build.
