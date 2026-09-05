# Nuxt application

This directory contains the Nuxt 4 frontend and Nitro backend.

Use Node 24.11 or later.
The SQLite adapter uses the built-in `node:sqlite` authorizer API.

The default page is an interface prototype with three parts:

1. A landing page
2. A six-view research narrative
3. A streaming AI chat with read-only SQL and shared charts

"Ask" enters the chat directly. The end of the story lets users ask a question or browse the graph. "Back to story" restores the prior narrative position.

The chat saves sessions in browser local storage (History, New chat, Clear history). Sessions do not sync to the server.

The narrative and chat use the same sanitized SQLite serving database. The chat also needs `NUXT_ANTHROPIC_API_KEY` in `.env`.
The server accepts at most 100 questions per hour, 500 per day, and eight concurrent.

The application records unlinked usage activity in a separate SQLite database: page views, visible time, scroll depth, narrative reach, device class, API status, and chat outcomes.
No IP addresses, full user-agent strings, account identifiers, or AI tool traces.
Question text expires after 30 days. Activity rows expire after 90 days.

## Serving data

The build and check commands are in [scripts/README.md](../scripts/README.md).
The private database keeps source locators, reference occurrences, source conflicts, and audit material.
The public database excludes full text, local paths, reference lists, possible project links, and audit reasoning.
It includes accepted project links, resolved people, observed membership, dated OpenAlex citation counts, and reviewed scientific identities.
Aggregate categories use only global canonical identities.
The narrative API keeps only fields its visuals use and is built once per process with cache headers.
The chat SQL runtime returns at most 200 rows per query.

See [docs/DATA_RELEASE.md](../docs/DATA_RELEASE.md) for database counts and hashes.

## Start the application

### Designer setup

Shared preview: [eq-graph.abundanceds.com](https://eq-graph.abundanceds.com)

`pnpm dev:remote` proxies `/api/*` to the shared preview. No database or API key needed.
`pnpm dev:local` (the default `pnpm dev`) needs `server/data/serving.sqlite`.
Add `NUXT_ANTHROPIC_API_KEY` to `.env` only for local chat.
Push design work to `design/anuja` and open a pull request.

### Production build

`pnpm build` produces a Node server at `.output/server/index.mjs` for one EC2 instance.

Set `NUXT_CHAT_USAGE_PATH` and `NUXT_ANALYTICS_DATABASE_PATH` to writable paths outside the release directory so state survives deployment.
Set `NUXT_ADMIN_TOKEN` (32+ chars). The admin page at `https://eq-graph.abundanceds.com/admin#ADMIN_TOKEN` exchanges the fragment for an HTTP-only session cookie.
All admin endpoints require this cookie or `Authorization: Bearer ADMIN_TOKEN`.

## Routes

| Route | Purpose |
| --- | --- |
| `/` | Landing page, narrative, and AI chat |
| `/about` | Project, method, ontology, team, and contact page |
| `/graph` | Interactive three-dimensional graph with four lenses |
| `/data` | Download links for the frozen public data release |
| `/admin` | Token-gated usage activity page |
| `GET /api/story` | Narrative totals, timeline, and topic series |
| `GET /api/graph` | Slim narrative data, co-authorship, and citation views |
| `GET /api/graph/status` | Serving-database totals |
| `POST /api/chat` | Streaming AI answer, SQL activity, and chart data |
| `POST /api/analytics` | Write one validated, unlinked activity event |
| `POST /api/admin/session` | Exchange the admin token for a signed session |
| `DELETE /api/admin/session` | End the current admin session |
| `GET /api/admin/summary` | Page, story, device, chat, and API totals |
| `GET /api/admin/chats` | Final chat questions, answers, and outcomes |
| `GET /api/admin/health` | Release, data, usage-limit, and error state |
| `GET /api/admin/export` | Date-range activity export in JSON Lines format |

## Graph page

`/graph` draws the graph-shaped part of the release as a print-like scene on the site's paper: people, projects, papers, products, and the instruments used in at least eight papers.
Four lenses re-project the same nodes: People (co-authorship, coloured by community; the default), Instruments (papers by year, tied to instrument hubs), Funding (project, lead, and linked papers, coloured by working group), and Everything.
The free lenses tumble without a pole and keep momentum after a flick; the Instruments lens stays upright so the year axis reads left to right.
Search finds a node or adds a filter chip.
Selecting a node mutes the rest, lights its neighbours, and offers a prefilled chat question through `/?ask=…#chat`.
The URL carries lens, focus, and filters.

The scene is static.
`pnpm build:graph` reads `server/data/serving.sqlite`, runs one seeded three-dimensional force layout per lens, and writes `public/graph-scene.json` (about 1.4 MB, precompressed at build time).
The output is deterministic, so rerunning it on the same database changes no bytes.
Rebuild it only for a new data release.
The renderer is `app/lib/graphScene.js` on three.js; the page is client-only.

The story's last fold offers the graph next to the chat.
Its card draws a real excerpt of the People lens (one co-author community, `app/lib/graphTeaser.json`, also written by `pnpm build:graph`) on a 2-D canvas in `app/lib/graphTeaser.js`, so the invitation shows the graph rather than an illustration of one.

## Chart system

Chat answers use `app/components/GraphWidget.vue`.
Observable Plot and the shared files in `app/viz/` render these marks:

- Stat
- Bar
- Line
- Area
- Scatter
- Histogram
- Heat map
- Donut
- Network
- Table

Bars support one, grouped, stacked, or signed series. Lines support one or more series.
Each chart includes its source rows in an expandable table.
Networks support at most 30 nodes and 60 links; the browser owns the force layout.
Charts do not create chat questions or comparison controls.

## AI and SQL

`server/api/chat.ts` runs the Anthropic agent with two tools: `query_sql` (returns rows and a result id) and `show_visualization` (renders a chart from that result).
The read-only runtime exposes a `coauthor_edges` view for compact network queries.
The SQLite authorizer rejects writes, schema changes, and PRAGMA actions.

## Local chat history

The browser stores sessions under `eq-graph.chat-history.v1` (at most 20, oldest dropped at the storage limit).
`server/utils/prompt.ts` defines the agent behavior; `server/utils/schema.ts` holds the SQL schema.

## Checks

```sh
pnpm test
pnpm exec nuxi typecheck
pnpm build
```

`pnpm build:graph` regenerates the static graph scene from the serving database; run it after a data release, not as part of the ordinary build.

`web/scripts/check-story-numbers.mjs` re-derives every number the story page shows from the API and fails on drift.
It needs a running dev server: `node web/scripts/check-story-numbers.mjs [origin]`.

The repository includes `tsconfig.json`, which extends the Nuxt-generated type configuration.
