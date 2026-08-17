# EuroQol research interface

## Product idea

The page is one continuous path:

1. The landing view states the purpose.
2. The narrative shows how funded research becomes evidence.
3. The chat lets a person ask questions about that evidence.

The design must feel editorial before it feels technical. The globe is the first data object. The same 944 study dots then change into six narrative views. The chat appears only after the story shows why the data matters.

This implementation keeps the current Nuxt 4 application. It does not use the designer repository as a second application. The approved visual system, globe, story motion, copy, and chat surface now run inside the Nuxt 4 page.

## Visual system

The design uses a visible 12-column grid, large type, warm paper, thin rules, and large areas of empty space. The grid supplies the structure. Effects must not replace structure.

### Type

| Role | Font | Use |
| --- | --- | --- |
| Display and body | Instrument Sans | Headings, narrative, controls, and chat copy |
| Numbers | IBM Plex Mono | Counts, chart values, progress, and technical details |

Large headings use tight line height and negative letter spacing. Small data labels use IBM Plex Mono. Body text stays regular and uses a comfortable line height.

### Core colours

| Token | Value | Use |
| --- | --- | --- |
| Paper | `#f4f3ef` | Landing page and story |
| Surface | `#ffffff` | Chat and chart cards |
| Main ink | `#1a1a17` | Main text |
| Secondary ink | `#5c5c56` | Supporting text |
| Muted ink | `#8e8e86` | Labels and metadata |
| EuroQol green | `#007d6c` | Main action, research reach, and first chart series |
| Amber | `#a8720d` | Second story accent |
| Hairline | `#e6e6e9` | Chat cards and divisions |

The chart topics use the designer palette:

| Topic | Colour |
| --- | --- |
| Working group | `#2a78d6` |
| Instrument | `#eb6834` |
| Researcher or journal | `#1baf7a` |
| Country | `#eda100` |
| Condition | `#e87ba4` |
| Method | `#4a3aa7` |

Text, shape, or a table must also identify a category. Colour must not be the only identifier.

### Grid and spacing

The desktop story has 48 px side padding and 24 px column gaps. The copy uses columns 1 to 5. The data field uses the right side of the fold. The logo sits above the top rule.

The chat shell is 63 rem wide. Its main column is 41 rem wide. Chat cards use a 1 px border and no heavy shadow.

On a phone, side padding is 24 px. The story copy uses the upper part of the fold. The data object uses the lower part. This prevents the chart labels from crossing the narrative text. Main buttons have a minimum touch height of 44 px.

## Landing view

The first fold contains four important parts:

- The official EuroQol logo.
- The statement “Shaping how the world measures health.”
- The “Explore studies” and “View impact” actions.
- A real orthographic globe.

The globe uses D3 geographic projection and Natural Earth country geometry. Countries with funded research use a fill that follows the study count. The globe turns slowly. A person can drag it. Hover gives a country label and count. The key explains what the light and dark areas mean.

The globe is a data view. It must not be replaced with a decorative circle or a generic particle sphere.

## Narrative

The desktop story has a 913 vh scroll runway. Mobile uses 1,039 vh because the copy wraps to more lines. The opening statement uses its own intro range. Six settled views follow.

| Step | Main statement | Data view |
| --- | --- | --- |
| 1 | 944 funded studies | Full research field |
| 2 | 2012–2025, year by year | Study years and evidence years |
| 3 | 117 countries | Geographic distribution |
| 4 | 9 working groups | Working groups by year |
| 5 | 30 accepted publication links | Confirmed links and the wider publication corpus |
| 6 | It all connects | Research network and transition to chat |

Vertical scroll moves one horizontal track. The stage stays fixed. The same 944 dots change position between views. This continuity is essential. It shows that each view describes the same portfolio.

Each scene is stable for about 78% of its scene range. The change to the next scene uses about 22%. A scene is not one exact scroll point. Its copy, chart marks, labels, and furniture remain fully settled while the user reads. The six progress controls jump to the middle of these hold ranges. Reduced-motion mode snaps between settled scenes.

Each step has a number, a heading, an explanation, and a consequence. The green rule marks the consequence. The copy comes from the approved designer narrative and uses the temporary reference fixture.

The last story view and the first chat view share one fold. The final scene first gets a complete hold range. A separate 100 vh range then controls the cross-fade. At the end of that range, the interface changes mode: the story leaves the document layout, the window scroll resets, and the chat becomes a full-height workbench. Only the transcript can scroll. Upward scrolling cannot reopen the story.

“Skip story” enters the same chat mode from the opening view. “Back to story” restores the exact settled story position from which the user entered. A return after the full narrative lands on the sixth scene, not inside its transition.

## Chat

The chat uses the original application architecture: a compact identity and data-status header, a transcript that owns the available vertical space, optional example questions inside the empty transcript, and a fixed composer. The transcript scroll layer spans the viewport, so its scroll rail stays at the window edge. Its content stays in the 50 rem reading column. There is no second greeting, KPI strip, or onboarding page after the narrative.

A response has these parts:

1. The question from the user.
2. The live SQL activity from the AI agent.
3. A direct answer.
4. A chart from the shared renderer when a chart helps.
5. A control that shows the read query.
6. Follow-up questions from the agent and chart marks.

Tool activity stays inline. Charts anchor at the top of the transcript when they arrive, so later streamed text cannot push the chart past the reader. The anchor releases when the user scrolls or asks the next question. Follow-up questions stay directly above the composer.

The chat uses the real Anthropic streaming agent through `POST /api/chat`. The agent has one `query_sql` tool. It writes a read query and can include an optional stat, bar, line, donut, or table specification in the same call. The server loads the temporary JSON fixture into SQLite. SQLite authorizer rules allow reads and SQL functions and reject all write, schema, and PRAGMA actions.

The AI is real. The data is temporary. The interface says “reference dataset” so that a temporary count cannot appear to be a production count.

Chart bars and donut legend rows are keyboard controls. Selecting a mark opens related questions about that value. Each non-table chart also contains an accessible data table.

## Chart system

The Observable Plot gallery remains at `/widgets`. It is the review surface for chart patterns. It contains 11 figure templates:

- Sorted bar
- Emphasis bar
- Grouped bar
- Stacked bar
- Multiple time lines
- Cumulative area
- Scatter plot
- Histogram
- Heat map
- Diverging bar
- Many-row bar

The gallery also covers number tiles, empty data, one row, negative values, long labels, light mode, and dark mode.

The chat uses `GraphWidget.vue`. It supports stat, bar, line, donut, and table specifications. It uses the same type, colour, and rule system as the story and gallery. A new runtime mark must first have a fixed example in `/widgets`.

The gallery and the chat renderer have different jobs. The gallery contains the full design library. The chat renderer contains the mark types that the application can call from a response specification.

`/chat-lab` uses the same chat workbench with fixed test states. It lets a designer review empty, working, answer, chart, table and error layouts without waiting for a model response. It is a design harness, not a second chat implementation.

The gallery also renders one fixed example for each live agent mark. This makes the connection visible: 11 broader Observable Plot patterns and five callable agent specifications share one review route.

## Application structure

| File | Responsibility |
| --- | --- |
| `web/app/pages/index.vue` | Loads the interface data and sets the page order |
| `web/app/components/StoryHorizontal.vue` | Mounts the landing view, globe, and six-step story |
| `web/app/lib/globe.js` | Draws and controls the orthographic globe |
| `web/app/lib/storyHorizontal.js` | Builds the narrative, dot layouts, and scroll state |
| `web/app/lib/beatArt.js` | Draws the background objects for each narrative step |
| `web/app/components/EvidenceChat.vue` | Runs the streaming AI chat and displays tool activity, answers, and charts |
| `web/app/components/ChatWorkbench.vue` | Displays the shared production and test chat surface |
| `web/app/components/ChatAnswer.vue` | Safely formats streamed prose, lists, links, and tables |
| `web/app/components/GraphWidget.vue` | Draws charts in chat answers |
| `web/app/pages/chat-lab.vue` | Provides fixed chat states for interface work |
| `web/app/pages/widgets.vue` | Shows the full Observable Plot gallery |
| `web/app/viz/theme.ts` | Holds chart tokens |
| `web/server/utils/mockResearch.ts` | Maps temporary fixtures to stable interface data |
| `web/server/utils/referenceSqlite.ts` | Loads reference JSON into SQLite and enforces the read-only query boundary |
| `web/server/utils/tools.ts` | Defines the one `query_sql` AI tool |
| `web/server/middleware/remote-api.ts` | Proxies local designer API calls to the shared preview |

The Nuxt 3 shell, Cloudflare target, and direct browser reads from static JSON are not part of the application. Nitro owns the data boundary. The production build uses the Node server output and can run with SQLite on one EC2 instance.

## Temporary data and replacement seam

Two temporary JSON files support interface work:

- `web/server/data/reference-graph.json` supplies the 944-project portfolio and narrative relations.
- `web/server/data/reference-live.json` supplies publications, findings, links, and evidence facets.

These files reproduce the approved interface state. They are not the new ontology and they are not the future source of truth.

The narrative replacement point is `web/server/utils/mockResearch.ts`. It has a `TODO(data)` comment. The agent replacement point is `web/server/utils/referenceSqlite.ts`. When the new ontology and SQLite database are ready, replace the fixture loader and update the schema prompt. The chat transport, one-tool model, and frontend response shapes can stay stable.

There is no Neo4j migration task. The new database starts from the new ontology.

The model already gets one SQL query tool. The tool accepts model-written SQL. The SQLite connection uses query-only mode and an authorizer that rejects actions other than reads. The application does not need a separate tool for each research subject.

## Quality rules

- Desktop and mobile must have no horizontal overflow.
- The first fold must use the official logo and the real globe renderer.
- All six narrative states must settle at their correct scroll positions.
- Reduced-motion mode stops automatic globe rotation and animated transitions.
- Main controls must be native buttons or links.
- Chat status uses a live region.
- Charts must have a name and a data equivalent.
- Runtime errors, hydration errors, and console errors are release blockers.
- The Node production build and Nuxt type check must pass.
