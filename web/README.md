# Nuxt application

This directory contains the Nuxt 4 frontend and Nitro backend.

Use Node 24.11 or later. The SQLite adapter uses the built-in
`node:sqlite` authorizer API.

The default page is an interface prototype with three parts:

1. A landing page
2. A six-view research narrative
3. A streaming AI chat with read-only SQL and shared charts

The narrative and chat are separate interaction modes. “Skip story” enters the
chat directly. Completing the story also enters chat. In chat mode, only the
transcript scrolls. “Back to story” restores the prior narrative position.

The narrative and chat use the same sanitized SQLite serving database. The chat
also needs `NUXT_ANTHROPIC_API_KEY` in `.env`.

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

Use `pnpm dev:local` when `server/data/serving.sqlite` exists on the local
computer. The narrative, data APIs and chart gallery need no key. Add
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
| `GET /api/story` | Narrative totals, timeline, and topic series |
| `GET /api/graph` | Globe and project dot-layout data |
| `GET /api/graph/status` | Serving-database totals |
| `POST /api/chat` | Streaming AI answer, SQL activity, and chart data |

The old `/api/mock/story` and `/api/mock/graph` routes remain as temporary
aliases for a designer branch that still uses them.

## Serving data

`server/data/serving.sqlite` is a generated deployment artifact. It is not in
Git. Build and check it from the repository root:

```sh
python3 scripts/build_serving_database.py \
  --source pilot/ontology-development-v3/production-calibration/graph-neutral-209-run-02/euroqol-research-graph-citation-safe.sqlite \
  --output web/server/data/serving.sqlite
python3 scripts/check_serving_database.py web/server/data/serving.sqlite
```

The public database excludes full text, local paths, unresolved citations,
possible project links, and audit reasoning. See
[`docs/APP_DATA_ADAPTER.md`](../docs/APP_DATA_ADAPTER.md).

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

The agent receives one concise schema and one read-only SQL tool. The SQLite
authorizer rejects writes, schema changes, and PRAGMA actions.

## Checks

```sh
pnpm exec nuxi typecheck
pnpm build
```

The repository includes `tsconfig.json`, which extends the Nuxt-generated type
configuration.
