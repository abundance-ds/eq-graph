# Nuxt application

Nuxt is the web application and Nitro is its backend. Nitro reads the real
Neo4j Aura research graph with the JavaScript driver. The ingestion pipeline is
the only component that writes to Aura.

## Start the application

```sh
cd web
pnpm install --frozen-lockfile
cp .env.example .env
# Add the Anthropic and Neo4j Aura values to .env.
pnpm db:check
pnpm dev
```

Open `http://localhost:3000`. The page reads current project, publication, and
finding counts from Aura. It refreshes the status once a minute. The counts are
not part of the application build.

`NUXT_NEO4J_DATABASE` is optional. Leave it empty to use the Aura account's
home database.

## Commands

| Command | Purpose |
| --- | --- |
| `pnpm db:check` | Check the Aura connection and print read-only graph counts. |
| `pnpm dev` | Start Nuxt with hot reload. |
| `pnpm build` | Build the Nitro production output. |
| `pnpm preview` | Run the production output locally. |
| `pnpm db:local:up` | Start the optional local Community database. |
| `pnpm db:local:migrate` | Apply the local Community schema. |
| `pnpm db:local:seed` | Add invented interface-test rows to the local database. |
| `pnpm db:local:reset` | Replace local rows with the invented fixture. |
| `pnpm db:local:down` | Stop the local database. |

The local write commands check the target hostname. They stop before a write
when the URI is not localhost, `127.0.0.1`, or `::1`.

## Application data rules

- The Aura graph contains real records, but the current load is a small pilot.
- Counts describe the loaded graph. They do not describe the full portfolio.
- Project-publication questions use accepted attributions by default.
- Findings and other layer-B records are extracted evidence. Their work and
  text-span provenance must remain visible.
- A missing record means only that the loaded graph has no record.
- Vector indexes exist, but semantic search is not active until embeddings are
  loaded.

The complete ontology is in `graph/graph-type.cypher` at the repository root.
The compact agent form is in `server/utils/schema.ts`.

## Read controls

Every agent query runs through `server/utils/neo4j.ts`. The runner plans the
query first, rejects write operators and procedures outside the allowlist,
uses a read transaction, applies a timeout, and caps returned rows. The status
endpoint uses the same runner.

The demo seed, reset, and Community migration scripts are local-only. Do not
add a second database service to the Nuxt request path.
