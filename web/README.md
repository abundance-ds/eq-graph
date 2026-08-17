# Nuxt application

This directory contains the Nuxt 4 frontend and Nitro backend.

Use Node 24.11 or later. The temporary SQLite adapter uses the built-in
`node:sqlite` authorizer API.

The default page is an interface prototype with three parts:

1. A landing page
2. A six-view research narrative
3. A streaming AI chat with read-only SQL and shared charts

The narrative and chat are separate interaction modes. “Skip story” enters the
chat directly. Completing the story also enters chat. In chat mode, only the
transcript scrolls. “Back to story” restores the prior narrative position.

The narrative does not need a database connection. The chat needs
`NUXT_ANTHROPIC_API_KEY` in `.env`. It uses the temporary reference JSON through
an in-memory SQLite database until the new ontology and database are ready.

## Start the application

### Designer setup

Shared preview: [eq-graph.shoulde.rs](https://eq-graph.shoulde.rs)

The designer can use the shared preview API without a database file or an API
key:

```sh
git clone https://github.com/shoulders-ai/eq-graph.git
cd eq-graph/web
git switch -c design/anuja
nvm use
corepack enable
pnpm install --frozen-lockfile
pnpm dev:remote
```

Open `http://localhost:3000`.

`pnpm dev:remote` runs the Nuxt frontend locally and proxies `/api/*` to
`https://eq-graph.shoulde.rs`. The browser still uses one origin, so no CORS
setup is required. Frontend edits update immediately.

Use `pnpm dev:local` to run the committed fixtures and in-memory SQLite on the
local computer. The narrative, data APIs and chart gallery need no key. Add
`NUXT_ANTHROPIC_API_KEY` to `.env` only when the local chat must call Anthropic.

Open `/chat-lab` for fixed empty, working, answer, chart, table and error
states. Open `/widgets` for the chart template gallery. These routes use the
real interface components without making an AI request. The main application
always uses the live AI transport.

Push design work to `design/anuja` and open a pull request. Do not work directly
on `main`.

The default `pnpm dev` command is the same as `pnpm dev:local`.

### Production build

Use `pnpm build` for a production Node server. The output runs from
`.output/server/index.mjs` and is suitable for one EC2 instance.

## Routes

| Route | Purpose |
| --- | --- |
| `/` | Landing page, narrative, and AI chat |
| `/widgets` | Observable Plot template gallery |
| `/chat-lab` | Deterministic chat states for interface work |
| `GET /api/mock/story` | Prototype narrative data |
| `GET /api/mock/graph` | Prototype globe and dot-layout data |
| `GET /api/graph/status` | Temporary SQLite dataset totals |
| `POST /api/chat` | Streaming AI answer, SQL activity, and chart data |

## Prototype data

`server/data/reference-graph.json` and `server/data/reference-live.json` are
temporary interface fixtures. Both main interface parts read them through
Nitro.

`server/utils/mockResearch.ts` is the narrative replacement seam.
`server/utils/referenceSqlite.ts` is the agent replacement seam. It loads the
fixture into normalized SQLite tables and allows only read actions. Replace that
loader and the schema prompt when the new ontology is ready. The client and chat
transport can stay stable.

The files reproduce the approved reference state. They are not the new
ontology or the future source of truth.

## Chart system

The full template gallery is in `app/pages/widgets.vue`. Shared chart tokens are
in `app/viz/theme.ts`.

Chat answers use `app/components/GraphWidget.vue`. It supports these marks:

- Stat
- Bar
- Line
- Donut
- Table

`/widgets` includes one fixed example for each of these live marks beside the
11-pattern Observable Plot library. Add and review a visual pattern there
before it becomes available to chat.

## AI and SQL

`server/api/chat.ts` runs the Anthropic agent. The agent receives one tool:
`query_sql`. The same call can request a chart from the shared renderer. There
is no tool for each subject and no unrestricted write connection.

The new database is a clean design. No Neo4j-to-SQLite migration is required.
The current temporary adapter already uses the intended one-tool boundary.

## Checks

```sh
pnpm exec nuxi typecheck
pnpm build
```

The repository includes `tsconfig.json`, which extends the Nuxt-generated type
configuration.
