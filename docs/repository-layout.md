# Repository layout

This repository covers the full path from project records to the graph application.

```text
project and member records
  -> author and paper discovery
  -> screening
  -> full-text retrieval
  -> evidence extraction
  -> graph loading
  -> Nuxt application
```

## Directory roles

| Path | Role |
| --- | --- |
| `input/` | Authoritative project records and the current per-project publication records |
| `scripts/` | Existing project-to-publication discovery and full-text pipeline |
| `pipeline/` | Protocol 2.0 discovery, screening, assessment, extraction, and graph-load stages |
| `corpus/` | Full text that the extraction stages can read |
| `graph/` | Historical Neo4j pilot schema and queries |
| `pilot/ontology-development-v3/` | Current ontology, production method, source audit, linkage audit, and graph result |
| `web/` | Nuxt server, graph tools, chat, and visual output |
| `docs/` | Protocol, method, provenance, architecture, decisions, and status |

The `pipeline/` directory entered the repository after the scale screen reached its validated pause point.
The existing `input/` and `scripts/` paths stay unchanged during the first integration stage.
This rule keeps the project-first pipeline usable while the integrated structure settles.

## Working data

Secrets, caches, dependencies, build output, and active run output do not belong in Git.
The repository tracks source code, authoritative small inputs, prompts, compact validation evidence, and result summaries.
Large or mutable working data stays in a separate work directory and uses checksummed manifests for provenance.
The tracked `WORKSPACE_MANIFEST.tsv` files record the complete local `artefacts/`, pilot, and scale trees at the import checkpoint.
