# Workplan

Scope of the whole project, in four work packages. Method for WP1–WP3 is in
[`protocol-2.0.md`](../protocol-2.0.md). This file adds the work-package frame
and the WP4 application design.

## The four work packages

| WP | Name | Output | State |
|---|---|---|---|
| 1 | Paper identification | The set of papers for full-text processing | Paused: main screen complete; human check and held identity tranche pending |
| 2 | Full-text retrieval | The full texts on disk | Pilot: 123/201 retrieved; scale not started or authorized |
| 3 | Full-text processing | Graph-ready evidence: read, filter, link, extract | Pilot complete; scale not started |
| 4 | Application | Graph + backend + two frontend pillars | The chat runs end to end on an invented graph. See the state below. |

### The state of WP4, on 2026-08-05

The application runs. Start it with the four commands in
[`../web/README.md`](../web/README.md).

Done:

- Neo4j 5 Community in a container, through OrbStack. `V001__layer_a.cypher`
  holds 17 constraints, 8 indexes and 4 full-text indexes.
- An invented graph: 2,263 nodes and 4,805 relationships. Real vocabularies,
  invented rows.
- The Nitro backend with the three tools, the query guards and the result store.
- The chat, with streamed text, tool calls, charts and follow-up questions. One
  question answered end to end: the model wrote the Cypher, read 8 rows, drew a
  bar chart and offered three follow-up questions.
- An activity trail in the chat that shows each step while it runs.
- The chart templates on `/widgets`, drawn with Observable Plot, with a
  validated palette and a light and a dark mode. A copy is published at
  <https://shoulders-ai.github.io/eq-test-viz-1/>.

Not done: the real layer A loader, the map and the relation marks, thread
storage, authentication, and the narrative story.

### WP1 — Paper identification

Find every journal article that EuroQol-funded research plausibly produced.
Steps 1–8 of `protocol-2.0.md`. The output is the screened set of candidate
articles.

### WP2 — Full-text retrieval

Get the full text of each retained paper. Step 9 of `protocol-2.0.md`. Record
the licence, the source and the retrieval method for each file. Flag papers
with no available full text. Do not infer content.

### WP3 — Full-text processing

Four operations on each full text:

1. **Read** — parse the document into sections and chunks.
2. **Filter** — assess the EuroQol connection from the content, the authors,
   the acknowledgements and the funding data.
3. **Link** — compare the supported paper with the project portfolio. Allow no
   project, one project or more than one project. Record the confidence and the
   evidence.
4. **Extract** — get the entities and the findings for the graph.

Steps 10–12 of `protocol-2.0.md`. Every extracted value must have a quotation
from the source text.

### WP4 — Application

Three layers:

- **Graph** — the data in Neo4j.
- **Backend** — an API and an agent.
- **Frontend** — two pillars:
  - **(a) The story.** A scrolling narrative that shows the key findings. Each
    step of the story is a data visualization.
  - **(b) The chat.** A chat interface like Claude or ChatGPT. The user asks a
    question. An agent in the backend queries the graph and answers.

## WP4 — design

### Repositories

| Repository | Role |
|---|---|
| `shoulders-ai/eq-graph` | The canonical project repository. It contains both pipelines, the ontology, the application, and compact validated evidence. |
| `shoulders-ai/amnog-graph` | The source of the chat pattern. Take the chat only. |

**Decision:** the application lives in `web/` in this repository.

Historical documents use “Paul's pipeline” and “Kazik's pipeline” to identify their independent origins.
Both pipelines now live in this repository.

**What Kazik has.** `graph/schema.cypher` gives 30 constraints and the indexes.
`graph/graph-type.cypher` gives the closed relationship model with the property
types. 33 node labels and about 45 relationship types. The design also has a
catalog subgraph (`_NodeType`, `_RelType`, `_PropertyDef`, `_QueryTemplate`)
and two vector indexes.

**What Kazik does not have.** No Neo4j instance. No loader. No extraction. The
graph is empty. All of WP4 waits for the loader.

**What amnog-graph has.** Nuxt 4, the Anthropic SDK, a hand-written SSE
transport, and a manual agent loop with a 64-round cap. The loop is good and it
transfers. The chat has **no generative UI**: the model only emits text. A side
panel shows evidence, but the *server* builds that panel from the tool results.
The model never decides what to show. We must build that part.

### Stack

**Nuxt 4 is the full-stack application.** Nitro is the backend. Nitro connects
to Neo4j with the JavaScript driver over the Bolt protocol. The agent runs in
Nitro. No other server is in the request path.

The reasons:

- The agent must run somewhere, and Nitro is that place.
- The frontend needs Nitro for the pages. A second server removes nothing.
- Paul writes the application, and Paul writes TypeScript.

Separate the two paths, and the language question disappears:

| Path | What it does | Server | Language |
|---|---|---|---|
| Write | The pipeline loads the graph | A batch job | Any |
| Read | The application answers questions | Nitro | TypeScript |

The pipeline writes to Neo4j and then stops. The application reads from Neo4j.
The two never meet inside a request. Kazik therefore writes the pipeline in the
language he prefers. Python works now. Kotlin works too.

**SDK: the Vercel AI SDK**, with the Anthropic provider today. See "The SDK
decision" below for the reasoning and for the measurement that still has to
happen.

Use **Zod** for the tool schemas.

### The SDK decision

**Settled: the Vercel AI SDK.** The reason is provider portability, which is a
goal here: a cheap open model such as Kimi or DeepSeek must be one line away.
The SDK also carries the chat transport and the Vue chat class, so the widget
channel needs no protocol of our own — a chart arrives in the browser as an
ordinary tool result.

The model is not settled. Measure it, as described below.

The comparison that led to the decision:

| | Anthropic SDK | Vercel AI SDK |
|---|---|---|
| Model choice | Anthropic only | Any provider, one line to change |
| Cheap open models (Kimi, DeepSeek) | Needs a second adapter | Supported |
| Widget channel | We build it | Data parts, already there |
| Chat composable for Vue | We build it | `useChat` |
| amnog code | Transfers as it is | We drop it (about 250 lines) |
| Anthropic-only controls | Direct | Through `providerOptions`, and later |
| Version risk | Low | Higher. Version 4 to version 5 broke the API. |

**The cost question is really a quality question.** A cheap model is only cheap
if it writes correct Cypher. Our schema has 33 node labels and a closed
relationship model. Text-to-Cypher is hard on a schema of that size. The failure
modes are invented labels, a reversed relationship direction, a missing
`confidence = 'accepted'` filter, and cartesian products. Compare a model that answers 40 percent of the questions
correctly with a model that answers 90 percent. The first model costs more,
because a wrong answer to a funder is worse than an expensive answer.

**We can measure this.** `docs/COMPETENCY_QUESTIONS.md` already holds 100
questions across 6 personas, plus 20 negative questions with the expected
refusal. That file is an evaluation set. When layer A is loaded, run 20 to 30
questions against each candidate model and record:

- the share of queries that run at all,
- the share of answers that are correct,
- the share of negative questions that get the correct refusal.

Then choose the model from the numbers, not from the price list.

**Keep the decision reversible.** The agent loop is the thin part. These parts
are durable and they must not import an SDK:

- the tool bodies (`search_graph`, `run_cypher`, `render`) — plain functions
  over the Neo4j driver,
- the Zod schemas,
- the event envelope,
- the widget renderer.

Write those four first. Then either SDK can drive them, and a later change costs
a day.

### The wire protocol

One event stream from the server to the browser. This envelope is the contract
between the backend and **both** frontend pillars.

```jsonc
{"t":"status",   "text":"Reading the graph…"}
{"t":"text",     "delta":"Sweden and "}
{"t":"cypher",   "id":"q1", "query":"MATCH …", "rows":42, "ms":180}
{"t":"widget",   "id":"w1", "spec":{ … }}
{"t":"followups","items":["…","…","…"]}
{"t":"error",    "message":"…"}
{"t":"done",     "threadId":"…"}
```

The client keeps an array of blocks. Text deltas go into the last text block. A
`widget` event appends a widget block. The transcript then holds prose and
widgets in the correct order.

### The agent loop

Keep the amnog loop. Send the message to the Anthropic API with `stream: true`.
Forward each text delta as a `text` event. Read the `tool_use` blocks from the
final message, run the tools, push the results, and repeat. Stop when
`stop_reason` is not `tool_use`. Keep the round cap and the second system
prompt that removes the tools on the last round.

**Model:** `claude-opus-5` for the agent. `claude-haiku-4-5` for the follow-up
questions. Put the schema in the system prompt with `cache_control` on the last
block. The prompt-cache minimum on Opus 5 is 512 tokens, so the schema caches.

### The tools

Four tools. Three for the first version.

**1. `search_graph({ q, kinds?, limit? })`**

Resolves a name to an identifier. Uses the full-text indexes that
`schema.cypher` already declares: `project_text_ft`, `work_text_ft`,
`person_name_ft`, `concept_label_ft`. Without this tool the agent guesses exact
strings in the `WHERE` clause and finds nothing.

**2. `run_cypher({ cypher, params?, purpose })`**

Runs a read query. Returns the columns, a capped preview of the rows, the row
count, and a `result_id`. The server keeps the full result set in memory under
that `result_id` for the length of the turn.

Guards. Neo4j Community Edition has no roles and no users, so a read-only
database user is not available. Use these instead:

- A **read transaction** (`session.executeRead`). The server refuses a write
  inside one. Smoke-test this on the instance before you trust it.
- **Inspect the `EXPLAIN` plan**, not the query text. Reject a plan that has a
  write operator: `CreateNode`, `MergeNode`, `SetProperty`, `DeleteRelationship`,
  `RemoveLabel`. A regular expression on the text loses to comments, to string
  literals and to Unicode.
- An allowlist for procedures. Deny `CALL apoc.*`, `CALL dbms.*` and `CALL db.*`
  unless the procedure is on the list.
- One statement per call.
- A transaction timeout and a row cap. The driver sets the timeout, so this
  works on Community Edition.

**3. `render({ spec })`**

This is the answer to the widget problem. The tool result is only
`{ "ok": true, "widget_id": "w1" }`. The server sends the widget to the browser
as a `widget` event.

The `spec` carries the *encoding*, not the data:

```jsonc
{
  "mark": "bar",                 // stat | bar | line | map | graph | table
  "title": "EQ-5D-5L value sets by country",
  "caption": "Accepted attributions only.",
  "source": { "result_id": "r3" },   // or { "rows": [ … ] } for small data
  "encoding": { "x": "country", "y": "n", "series": "technique" },
  "options": { "orientation": "horizontal", "sort": "desc", "limit": 15 }
}
```

Use **one** tool with a `mark` field. Do not use one tool per chart type. One
schema is easier to maintain, and the model chooses the mark as a field.

The `result_id` matters. The model does not copy the data. That saves tokens and
it removes transcription errors. Validate the spec on the server. If the spec is
invalid, return a tool result with `is_error: true`. The model then corrects
itself.

**4. `compute({ result_id, ops })` — later**

Do not add a code sandbox. Cypher does the aggregation. If the pilot shows a
gap, add a small declarative operation set: `sum`, `mean`, `median`, `pct`,
`groupby`, `sort`, `topk`. This is deterministic and it needs no sandbox.

### Why "respond to user" must not be a tool

The model can put text blocks and `tool_use` blocks in the **same** assistant
turn. So the model writes prose, calls `render`, and then writes more prose. The
prose streams token by token. The widget appears at the correct position. A
"respond to user" tool would break the streaming and it would give no benefit.

### The widget set

**Observable Plot draws the marks.** It is Bostock's own chart library, and its
grammar is the grammar the widget specification already uses, so `resolveWidget`
translates and does not draw. The theme lives in `web/app/viz/theme.ts`, and its
categorical colours are validated for the lightness band, the chroma floor, the
separation under colour blindness and the contrast against the paper.

| Mark | Use | State |
|---|---|---|
| `stat` | One number with its context. Cheap and it has a strong effect. | On `/widgets` |
| `bar` | Counts by country, working group, grant type or instrument. | On `/widgets`, in four forms |
| `line` | Publications per year. Cumulative funding. | On `/widgets`, with the area form |
| `table` | Ranked rows. It is also the twin behind every figure. | On `/widgets` |
| scatter, histogram, heat map | Relation and distribution. | On `/widgets` |
| `map` | Value sets by country. This mark suits the EuroQol domain very well. | Not built. It needs country shapes. |
| `graph` | A node-link subgraph: project → attribution → work → person. | Not built. Prefer an arc diagram or a matrix over a dense ball of nodes. |

**The two pillars share the renderer.** The story is a sequence of specs that a
human writes. The chat is a sequence of specs that the model writes. One
`<Widget :spec="…">` component set serves both. Build the renderer once.

### The follow-up questions

Do not use a tool. A tool adds a round trip and it puts the questions in the
wrong position.

Do not use a second model call either. The agent knows what it searched and what
the graph holds. A second model only sees the transcript, so its questions are
worse. The cost is the same.

**Use a sentinel block at the end of the answer.** The agent writes:

```
<followups>
Which countries have the most EQ-5D-5L value sets?
Who are the most prolific EQ-HWB researchers?
Show me the funding trend since 2015.
</followups>
```

The server removes the block from the stream and sends a `followups` event.

Three rules make this safe:

1. **Hold back a suffix.** The text streams token by token. Keep the last
   `len("<followups>")` characters in a buffer. Send them only when the tail of
   the buffer cannot start the opening tag. Without this, the user sees `<`,
   `<f` and `<fol` in the transcript.
2. **One block for each turn.** After the opening tag, stop all `text` events
   for the rest of the turn. Ignore a second block.
3. **Remove the block before you save the turn.** If the block stays in the
   thread history, the agent reads its own questions on the next turn.

Use one block with symmetric tags. Do not use numbered tags such as `<|FU1|>`,
because the scanner must then match many tags.

### The graph schema on Community Edition

We use Neo4j Community Edition. Three of Kazik's constraints do not apply.

| Feature | Community Edition | What we do |
|---|---|---|
| `IS NODE KEY` | Not available | Use `IS UNIQUE` for each one |
| Existence and property-type constraints (section 4) | Not available | Remove the section. The loader validates instead. |
| Roles and users | Not available | See the guards under `run_cypher` |
| Indexes, full-text indexes, vector indexes | Available | No change |

Kazik's `schema.cypher` header already gives the first two substitutions.

Write `graph/schema.community.cypher` from his file. Keep the constraint names,
because the names are stable identifiers that the tests can assert.

**Use versioned migrations, not one DDL file.** Kazik uses this pattern in
`xemantic/xemantic-neo4j-demo`: numbered Cypher files under a `migrations`
directory, applied in order, with the applied version recorded in the database.

```
graph/migrations/V001__constraints_layer_a.cypher
graph/migrations/V002__indexes_layer_a.cypher
graph/migrations/V003__fulltext_indexes.cypher
```

The tool is `neo4j-migrations`. It has a command-line version, so we can run it
from CI or from the pipeline. We need no Kotlin, no Gradle and no JVM for this.

This matters because the schema will change. Layer B and layer C arrive in WP3,
and the first loader run will find errors in layer A.

**The loader becomes the validation layer.** Section 4 would have enforced
non-null keys, integer years and float scores. The loader must check these
before each `MERGE`.

**Keep `graph-type.cypher`, but do not run it.** It needs Neo4j 2026.02 or
later. It stays useful as the single source of truth. Generate three things from
it:

1. The schema text for the agent system prompt.
2. The TypeScript types.
3. The `_NodeType` and `_RelType` catalog rows.

### Persistence, authentication and limits

amnog has no persistence. The browser returns the full history on each turn.
That is not sufficient here, because a Cypher result set is large.

- Keep the threads on the server. The client sends a `thread_id` and the new
  message only.
- Truncate the old tool results in the history.
- Add a per-address rate limit and a per-thread rate limit.
- Add at least a shared password. This application faces a funder.

## Decisions made

1. **The application lives in `web/` in this repository.**
2. **Nuxt is the full-stack application, and Nitro is the backend.** Nitro
   connects to Neo4j directly. No second server is in the request path. This is
   settled, and it is not open for discussion with Kazik.
3. **Neo4j Community Edition.** No Enterprise. No version 2026.02 preview.
4. **Zod for the tool schemas.** Both SDKs accept Zod.
5. **A sentinel block for the follow-up questions.** No tool, no second call.
   But see the warning under the open decisions.
6. **The Vercel AI SDK**, with the Anthropic provider today. The reason is
   provider portability. The model itself is still open.
7. **Observable Plot for every chart**, with one theme file, a validated
   palette, and a gallery on `/widgets` that carries the hard states.
8. **The renderer decides how a chart looks, and the model decides what it
   shows.** The model names the fields and the intent. The renderer picks the
   orientation, the sort, the ticks and the number format. Fewer choices for the
   model means fewer bad charts. This is not built yet; see the next steps.

## Open decisions

1. **Which model?** The SDK is settled. Do not decide the model from the price
   list. Measure the candidates against `COMPETENCY_QUESTIONS.md` on the real
   layer A graph, and count three things: the share of queries that run, the
   share of answers that are correct, and the share of negative questions that
   get the correct refusal.
2. **Does the sentinel survive a weak model?** A small model can forget the
   `<followups>` block or write it incorrectly. If we move to a cheap model,
   test this. The alternative is a second call to the same cheap model, which
   costs almost nothing.
3. **Which embedding model?** Both vector indexes use 1024 dimensions as a
   placeholder. A change needs an index rebuild and a new embedding run. This
   blocks nothing until WP3.
4. **Where does the database run in production?** The container answers for
   development. For production the plan is a plain Ubuntu instance on EC2, with
   Neo4j bound to the local address and Caddy in front for the certificate. Not
   started, and it does not block the work.
5. **Does the invented seed stay?** The pilot produced real rows: 50 candidate
   article-project links in `pilot/protocol-2.0/`. A loader over those would
   make every answer real, and it would make the competency questions a true
   measurement. The seed keeps one advantage: 140 projects and 260 works fill a
   chart, and the pilot set is smaller.

## Coordination with Kazik

The application server is decided. Tell him the decision. Do not ask him.

His repository `xemantic/xemantic-neo4j-demo` shows his default structure:
Kotlin, Ktor, Netty and the Neo4j driver, with no frontend. His Gradle files in
`eq-graph` may mean the same structure, or they may only run the schema
migrations. Either answer is acceptable now, because the pipeline is a batch job
and its language is free.

Two items need his agreement:

1. **The schema on Community Edition.** He must accept `IS UNIQUE` in place of
   `IS NODE KEY`, and the loss of section 4. See the section above.
2. **The migrations.** Agree one set of versioned Cypher files, and agree who
   owns them.

## Next steps, in order

Steps 1 to 4 of the earlier plan are done. What follows is the work that starts
tomorrow. Nothing here waits for WP3.

1. **Move the chat onto Plot.** `app/pages/index.vue` still draws with
   `GraphWidget.vue`. Replace it with `PlotFigure.vue`, and hold the interface
   of `resolveWidget` still, so the tool contract does not move. Half a day.
2. **Send the column types from the server.** `runReadCypher` already knows
   whether a column holds an integer, a name or a date, and it then throws that
   knowledge away. Keep it, and the renderer picks the scale and the number
   format without asking the model. This is the cheapest large gain.
3. **Narrow the model contract.** The model gives the fields and the intent:
   compare, trend, part of a whole, distribution, rank, relation, one number.
   The renderer decides the rest. Grow `widgetSpec` for the new marks, and grow
   the check in `resolveWidget` with it, so a wrong specification returns a
   plain sentence and the model corrects itself.
4. **Write the real layer A loader.** The data is on disk and the work is
   mechanical: the project files, the publication files, the manifests and the
   Markdown with front matter. This replaces the invented seed and it turns
   `COMPETENCY_QUESTIONS.md` into a real measurement.
5. **Measure the models.** 20 to 30 questions against each candidate. Then
   choose from the numbers.
6. **Add the thread store.** A reload clears the chat today.
7. **Add `map` and the relation mark.** The map needs country shapes. The
   relation mark needs a layout that a person can read.
8. **Build the narrative story** with the same components as the chat.
9. **Deploy.** A plain Ubuntu instance on EC2: Node 22, a systemd unit for
   `.output/server/index.mjs`, Caddy for the certificate, and Neo4j bound to
   `127.0.0.1`.
