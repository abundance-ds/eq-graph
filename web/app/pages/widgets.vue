<script setup lang="ts">
/**
 * The gallery.
 *
 * Every mark, against fixed data, in one place. This page exists so a person
 * can judge the look of a chart without asking the agent for one. Build a mark
 * here first, and give it to the agent afterwards.
 */
import * as Plot from "@observablehq/plot";
import { axis, baseX, baseY, barInset, endLabel, fmt, frame, gridX, gridY, type Tokens } from "../viz/plot";
import {
  CORPUS,
  HEADLINE,
  LINK_QUALITY,
  MANY_ROWS,
  NO_ROWS,
  ONE_ROW,
  PUBLICATIONS,
  SCORES,
  STUDIES,
  VALUE_SETS,
  WITH_NEGATIVE,
  WORKING_GROUPS,
} from "../viz/fixtures";

// --- the light and the dark mode -------------------------------------------

const mode = ref<"light" | "dark">("light");

function setMode(next: "light" | "dark") {
  mode.value = next;
  if (import.meta.client) document.documentElement.dataset.theme = next;
}

onMounted(() => setMode("light"));
onBeforeUnmount(() => {
  if (import.meta.client) delete document.documentElement.dataset.theme;
});

// --- the shared shapes ------------------------------------------------------

const GROUP_ORDER = WORKING_GROUPS.map((row) => row.group);
const LABEL_WIDTH = 168;

/** The height of a chart with a band for each row. */
function bandHeight(rows: number, top = 8, bottom = 26) {
  return rows * 30 + top + bottom;
}

// 1. A bar chart, one series, sorted, with the value at the tip. The axis and
//    the grid then carry nothing, so both go away.
function barSorted(t: Tokens) {
  const inset = barInset(WORKING_GROUPS.length, bandHeight(WORKING_GROUPS.length) - 34);
  return {
    ...frame(t, { marginLeft: LABEL_WIDTH, marginTop: 8, marginBottom: 26, marginRight: 42 }),
    height: bandHeight(WORKING_GROUPS.length),
    x: { axis: null },
    y: { label: null, domain: GROUP_ORDER, ...axis(t) },
    marks: [
      Plot.barX(WORKING_GROUPS, {
        y: "group",
        x: "projects",
        fill: t.series[0],
        rx2: 4,
        insetTop: inset,
        insetBottom: inset,
      }),
      Plot.text(WORKING_GROUPS, {
        y: "group",
        x: "projects",
        text: (d: any) => fmt.int(d.projects),
        textAnchor: "start",
        dx: 7,
        ...endLabel(t),
      }),
      baseX(t),
    ],
  };
}

// 2. The same numbers, when the story is one row. Colour marks the point, and
//    the rest of the bars fall back to grey.
function barEmphasis(t: Tokens) {
  const inset = barInset(WORKING_GROUPS.length, bandHeight(WORKING_GROUPS.length) - 34);
  return {
    ...frame(t, { marginLeft: LABEL_WIDTH, marginTop: 8, marginBottom: 26, marginRight: 42 }),
    height: bandHeight(WORKING_GROUPS.length),
    x: { axis: null },
    y: { label: null, domain: GROUP_ORDER, ...axis(t) },
    marks: [
      Plot.barX(WORKING_GROUPS, {
        y: "group",
        x: "projects",
        fill: (d: any) => (d.group === "EQ-HWB" ? t.ink.accent : t.ink.mute),
        rx2: 4,
        insetTop: inset,
        insetBottom: inset,
      }),
      Plot.text(WORKING_GROUPS, {
        y: "group",
        x: "projects",
        text: (d: any) => fmt.int(d.projects),
        textAnchor: "start",
        dx: 7,
        ...endLabel(t, {
          fill: (d: any) => (d.group === "EQ-HWB" ? t.ink.primary : t.ink.muted),
        }),
      }),
      baseX(t),
    ],
  };
}

// 3. Two series over the same rows. The bars sit side by side inside a facet,
//    and the legend carries the identity.
function barGrouped(t: Tokens) {
  return {
    ...frame(t, { marginLeft: LABEL_WIDTH, marginTop: 8, marginBottom: 30, marginRight: 30 }),
    // Two thin bars for each row, and air between the rows.
    height: WORKING_GROUPS.length * 40 + 38,
    x: { label: null, ...axis(t), tickFormat: fmt.int },
    y: { axis: null },
    fy: { label: null, domain: GROUP_ORDER, ...axis(t) },
    color: { domain: ["Accepted", "For review"], range: [t.series[0], t.series[1]], legend: true },
    marks: [
      gridX(t),
      Plot.barX(LINK_QUALITY, {
        fy: "group",
        y: "state",
        x: "links",
        fill: "state",
        rx2: 3,
        insetTop: 2,
        insetBottom: 2,
      }),
      baseX(t),
    ],
  };
}

// 4. The same two series as parts of one whole. A 2 px inset makes the gap, so
//    no stroke is needed to separate the parts.
function barStacked(t: Tokens) {
  const inset = barInset(WORKING_GROUPS.length, bandHeight(WORKING_GROUPS.length) - 34);
  return {
    ...frame(t, { marginLeft: LABEL_WIDTH, marginTop: 8, marginBottom: 30, marginRight: 18 }),
    height: bandHeight(WORKING_GROUPS.length),
    x: { label: null, ...axis(t), tickFormat: fmt.int },
    y: { label: null, domain: GROUP_ORDER, ...axis(t) },
    color: { domain: ["Accepted", "For review"], range: [t.series[0], t.series[1]], legend: true },
    marks: [
      gridX(t),
      Plot.barX(LINK_QUALITY, {
        y: "group",
        x: "links",
        fill: "state",
        insetLeft: 1,
        insetRight: 1,
        insetTop: inset,
        insetBottom: inset,
      }),
      baseX(t),
    ],
  };
}

// 5. A trend. Three series, a legend, a label at the end of each line, and a
//    gap where the data is missing. EQ-HWB starts in 2019, and the line must
//    not fall to zero before that.
function lines(t: Tokens) {
  const ends = ["EQ-5D-5L", "EQ-5D-3L", "EQ-HWB"].map((family) => {
    const rows = PUBLICATIONS.filter((row) => row.family === family && row.works != null);
    return rows[rows.length - 1]!;
  });

  return {
    ...frame(t, { marginRight: 88, marginTop: 26 }),
    height: 300,
    x: { label: null, ...axis(t) },
    y: { label: "↑ Works", grid: false, ...axis(t), tickFormat: fmt.int },
    color: { domain: ["EQ-5D-5L", "EQ-5D-3L", "EQ-HWB"], range: t.series.slice(0, 3), legend: true },
    marks: [
      gridY(t),
      Plot.line(PUBLICATIONS, {
        x: "year",
        y: "works",
        stroke: "family",
        strokeWidth: 2,
        strokeLinejoin: "round",
        strokeLinecap: "round",
        curve: "monotone-x",
      }),
      Plot.dot(ends, {
        x: "year",
        y: "works",
        fill: "family",
        r: 4.5,
        stroke: t.ink.surface,
        strokeWidth: 2,
      }),
      // Two of the three lines meet at the foot of the chart, and two labels
      // there would touch. Only the line that carries the story gets a label.
      // The legend holds the identity of the other two.
      Plot.text(ends.slice(0, 1), {
        x: "year",
        y: "works",
        text: "family",
        textAnchor: "start",
        dx: 10,
        ...endLabel(t, { fontVariant: "normal" }),
      }),
      Plot.tip(
        PUBLICATIONS.filter((row) => row.works != null),
        Plot.pointer({
          x: "year",
          y: "works",
          title: (d: any) => `${d.family}\n${d.year.getUTCFullYear()}: ${fmt.int(d.works)} works`,
          fill: t.ink.raised,
          stroke: t.ink.axis,
        }),
      ),
      baseY(t),
    ],
  };
}

// 6. One series over time, as a size. The wash sits at ten per cent, so it
//    never becomes a block.
function area(t: Tokens) {
  return {
    ...frame(t, { marginTop: 26 }),
    height: 240,
    x: { label: null, ...axis(t) },
    y: { label: "↑ Works in the corpus", ...axis(t), tickFormat: fmt.int },
    marks: [
      gridY(t),
      Plot.areaY(CORPUS, { x: "year", y: "works", fill: t.series[0], fillOpacity: 0.1, curve: "monotone-x" }),
      Plot.line(CORPUS, { x: "year", y: "works", stroke: t.series[0], strokeWidth: 2, curve: "monotone-x" }),
      Plot.dot(CORPUS.slice(-1), {
        x: "year",
        y: "works",
        fill: t.series[0],
        r: 4.5,
        stroke: t.ink.surface,
        strokeWidth: 2,
      }),
      Plot.text(CORPUS.slice(-1), {
        x: "year",
        y: "works",
        text: (d: any) => fmt.int(d.works),
        textAnchor: "end",
        dy: -12,
        ...endLabel(t),
      }),
      baseY(t),
    ],
  };
}

// 7. Two measures against one another. Three series only, because a scatter
//    compares every pair of colours and not only the neighbours. The symbol is
//    the second channel, so colour never carries the identity alone.
function scatter(t: Tokens) {
  return {
    ...frame(t, { marginTop: 26, marginLeft: 52 }),
    height: 300,
    x: { label: null, ...axis(t), tickFormat: (d: number) => String(d) },
    y: { label: "↑ People in the study", ...axis(t), tickFormat: fmt.int },
    color: { domain: ["cTTO", "DCE", "TTO"], range: t.series.slice(0, 3), legend: true },
    symbol: { domain: ["cTTO", "DCE", "TTO"], range: ["circle", "square", "triangle"] },
    marks: [
      gridY(t),
      Plot.dot(STUDIES, {
        x: "year",
        y: "size",
        fill: "technique",
        symbol: "technique",
        r: 4.5,
        stroke: t.ink.surface,
        strokeWidth: 2,
      }),
      Plot.tip(
        STUDIES,
        Plot.pointer({
          x: "year",
          y: "size",
          title: (d: any) => `${d.study}\n${d.technique}\n${fmt.int(d.size)} people, ${d.year}`,
          fill: t.ink.raised,
          stroke: t.ink.axis,
        }),
      ),
      baseY(t),
    ],
  };
}

// 8. A distribution. The bins carry the shape, and no single value is labelled.
function histogram(t: Tokens) {
  return {
    ...frame(t, { marginTop: 26 }),
    height: 220,
    x: { label: "Match score →", ...axis(t), tickFormat: fmt.one },
    y: { label: "↑ Pairs", ...axis(t), tickFormat: fmt.int },
    marks: [
      gridY(t),
      Plot.rectY(SCORES, {
        ...Plot.binX({ y: "count" }, { x: "score", thresholds: 26 }),
        fill: t.series[0],
        insetLeft: 1,
        insetRight: 1,
        ry2: 3,
      }),
      Plot.ruleX([0.5], { stroke: t.ink.primary, strokeWidth: 1 }),
      Plot.text([0.5], {
        x: (d: number) => d,
        text: () => "accept above 0.50",
        frameAnchor: "top",
        textAnchor: "start",
        dx: 6,
        ...endLabel(t, { fontVariant: "normal", fill: t.ink.muted }),
      }),
      baseY(t),
    ],
  };
}

// 9. Two names against one another. One hue, light to dark, with a legend,
//    and the number written in each cell.
function heatmap(t: Tokens) {
  const top = VALUE_SETS.reduce((max, row) => Math.max(max, row.sets), 0);
  return {
    ...frame(t, { marginLeft: LABEL_WIDTH, marginTop: 30, marginBottom: 8 }),
    height: 8 * 34 + 38,
    padding: 0,
    x: { axis: "top", label: null, ...axis(t) },
    y: { label: null, ...axis(t) },
    color: { type: "linear", domain: [0, top], range: [t.ramp[0], t.ramp[6]], legend: true, label: "Value sets" },
    marks: [
      Plot.cell(VALUE_SETS, { x: "technique", y: "country", fill: "sets", inset: 1, rx: 3 }),
      Plot.text(VALUE_SETS, {
        x: "technique",
        y: "country",
        text: (d: any) => fmt.int(d.sets),
        // The label sits inside the fill, so it takes its colour from the
        // darkness of that fill, and never from the colour of the series.
        fill: (d: any) => {
          const strong = d.sets > top * 0.55;
          if (t.dark) return strong ? "#241f1a" : t.ink.secondary;
          return strong ? "#ffffff" : t.ink.primary;
        },
        fontSize: 11,
        fontVariant: "tabular-nums",
      }),
    ],
  };
}

// 10. A change with a sign. Two hues that read as opposite, and a grey rule at
//     zero.
function diverging(t: Tokens) {
  const inset = barInset(WITH_NEGATIVE.length, bandHeight(WITH_NEGATIVE.length) - 34);
  const span = Math.max(...WITH_NEGATIVE.map((row) => Math.abs(row.change))) * 1.45;
  return {
    ...frame(t, { marginLeft: LABEL_WIDTH, marginTop: 8, marginBottom: 26, marginRight: 42 }),
    height: bandHeight(WITH_NEGATIVE.length),
    // The bars run both ways. A symmetric scale with room to spare keeps the
    // longest bar, and its label, clear of the names on the left.
    x: { axis: null, domain: [-span, span] },
    y: { label: null, domain: WITH_NEGATIVE.map((row) => row.group), ...axis(t) },
    marks: [
      Plot.barX(WITH_NEGATIVE, {
        y: "group",
        x: "change",
        fill: (d: any) => (d.change >= 0 ? t.diverging.high : t.diverging.low),
        rx2: 4,
        insetTop: inset,
        insetBottom: inset,
      }),
      // The anchor of a label is a fixed value and not a channel, so the two
      // sides need two marks.
      Plot.text(
        WITH_NEGATIVE.filter((row) => row.change >= 0),
        { y: "group", x: "change", text: (d: any) => `+${d.change}`, textAnchor: "start", dx: 7, ...endLabel(t) },
      ),
      Plot.text(
        WITH_NEGATIVE.filter((row) => row.change < 0),
        { y: "group", x: "change", text: (d: any) => String(d.change), textAnchor: "end", dx: -7, ...endLabel(t) },
      ),
      Plot.ruleX([0], { stroke: t.ink.axis, strokeWidth: 1 }),
    ],
  };
}

// 11. Forty rows. The chart shows the twelve that matter, and it says out loud
//     what it left out. A silent cut reads as "this is all of it".
const TOP_ROWS = 12;
const shown = MANY_ROWS.slice(0, TOP_ROWS);
const rest = MANY_ROWS.slice(TOP_ROWS);
const withOther = [
  ...shown,
  { group: `Other (${rest.length})`, projects: rest.reduce((sum, row) => sum + row.projects, 0) },
];

function barMany(t: Tokens) {
  const inset = barInset(withOther.length, bandHeight(withOther.length) - 34);
  return {
    ...frame(t, { marginLeft: 120, marginTop: 8, marginBottom: 26, marginRight: 42 }),
    height: bandHeight(withOther.length),
    x: { axis: null },
    y: { label: null, domain: withOther.map((row) => row.group), ...axis(t) },
    marks: [
      Plot.barX(withOther, {
        y: "group",
        x: "projects",
        fill: (d: any) => (d.group.startsWith("Other") ? t.ink.mute : t.series[0]),
        rx2: 4,
        insetTop: inset,
        insetBottom: inset,
      }),
      Plot.text(withOther, {
        y: "group",
        x: "projects",
        text: (d: any) => fmt.int(d.projects),
        textAnchor: "start",
        dx: 7,
        ...endLabel(t, { fill: (d: any) => (d.group.startsWith("Other") ? t.ink.muted : t.ink.secondary) }),
      }),
      baseX(t),
    ],
  };
}

// --- the tables behind the figures ------------------------------------------

const groupTable = {
  columns: ["Working group", "Projects"],
  rows: WORKING_GROUPS.map((row) => ({ "Working group": row.group, Projects: row.projects })),
};

const linkTable = {
  columns: ["Working group", "State", "Links"],
  rows: LINK_QUALITY.map((row) => ({ "Working group": row.group, State: row.state, Links: row.links })),
};

const valueSetTable = {
  columns: ["Country", "Technique", "Value sets"],
  rows: VALUE_SETS.map((row) => ({ Country: row.country, Technique: row.technique, "Value sets": row.sets })),
};
</script>

<template>
  <div class="viz-root">
    <header class="top">
      <div>
        <h1>Chart templates</h1>
        <p>
          Every mark, against fixed data. The colours are validated for the lightness band, the
          chroma floor, the separation under colour blindness and the contrast against the paper.
        </p>
      </div>
      <div class="modes" role="group" aria-label="Mode">
        <button :class="mode === 'light' && 'on'" @click="setMode('light')">Light</button>
        <button :class="mode === 'dark' && 'on'" @click="setMode('dark')">Dark</button>
      </div>
    </header>

    <!-- Numbers first. A single number is not a chart. -->
    <section class="block">
      <h2>Numbers</h2>
      <div class="hero">
        <StatTile
          hero
          :label="HEADLINE.hero.label"
          :value="HEADLINE.hero.value"
          :delta="0.19"
          since="against last year"
          :spark="HEADLINE.spark"
        />
      </div>
      <div class="tiles">
        <StatTile
          v-for="tile in HEADLINE.tiles"
          :key="tile.label"
          :label="tile.label"
          :value="tile.value"
          :delta="tile.delta"
          since="against last year"
        />
      </div>
    </section>

    <section class="block">
      <h2>Bars</h2>
      <div class="grid">
        <PlotFigure
          title="Projects for each working group"
          subtitle="One series. Sorted. The value rides the tip of the bar, so the axis and the grid carry nothing and both go away."
          alt="A horizontal bar chart of eight working groups. EQ-HWB leads with 24 projects, and the smallest two hold 12 each."
          note="Invented data."
          :build="barSorted"
          :table="groupTable"
        />
        <PlotFigure
          title="Projects for each working group, with one group named"
          subtitle="When the story is one row, colour marks that row and the rest fall back to grey."
          alt="The same eight bars. Only EQ-HWB carries colour."
          :build="barEmphasis"
          :table="groupTable"
        />
        <PlotFigure
          title="Article links, by state"
          subtitle="Two series side by side. The legend carries the identity."
          alt="Two bars for each working group: accepted links and links that wait for review."
          :build="barGrouped"
          :table="linkTable"
        />
        <PlotFigure
          title="Article links, as parts of one whole"
          subtitle="The same two series, stacked. A 2 px inset makes the gap, so no stroke is needed."
          alt="One stacked bar for each working group, split into accepted links and links for review."
          :build="barStacked"
          :table="linkTable"
        />
      </div>
    </section>

    <section class="block">
      <h2>Time</h2>
      <div class="grid">
        <PlotFigure
          title="Works for each year, by instrument"
          subtitle="Three series. A label rides the end of each line. EQ-HWB starts in 2019, and the line breaks before that, because a missing value is not a zero."
          alt="Three lines from 2010 to 2025. EQ-5D-5L rises steeply, EQ-5D-3L falls, and EQ-HWB starts in 2019."
          :build="lines"
        />
        <PlotFigure
          title="The corpus, cumulative"
          subtitle="One series. The wash sits at ten per cent, so it never becomes a block."
          alt="An area that rises from about 320 works in 2010 to about 15,000 in 2025."
          :build="area"
        />
      </div>
    </section>

    <section class="block">
      <h2>Distribution and relation</h2>
      <div class="grid">
        <PlotFigure
          title="Study size against year"
          subtitle="Three series at most. A scatter compares every pair of colours, and not only the neighbours, so the symbol carries the identity beside the colour."
          alt="A scatter of 84 studies. Size runs from about 200 to about 2,200 people, with no clear trend against the year."
          :build="scatter"
        />
        <PlotFigure
          title="Match scores"
          subtitle="A distribution. The bins carry the shape, and no single bar gets a number."
          alt="A histogram of 640 match scores. Most sit between 0.2 and 0.5, and the tail reaches 0.8."
          :build="histogram"
        />
        <PlotFigure
          title="Value sets, by country and technique"
          subtitle="One hue, light to dark, with a legend and the number inside each cell."
          alt="A grid of eight countries against three techniques. The United Kingdom and cTTO hold the largest counts."
          :build="heatmap"
          :table="valueSetTable"
        />
        <PlotFigure
          title="Change in accepted links"
          subtitle="A signed change. Two hues that read as opposite, and a grey rule at zero."
          alt="Five working groups. Three rose, and two fell, the largest fall being five links."
          :build="diverging"
        />
      </div>
    </section>

    <section class="block">
      <h2>The hard states</h2>
      <div class="grid">
        <div class="state">
          <h3>One row</h3>
          <p class="hint">A chart with one bar says less than the number. The tile takes over.</p>
          <StatTile :label="`Projects · ${ONE_ROW[0]!.group}`" :value="ONE_ROW[0]!.projects" />
        </div>

        <div class="state">
          <h3>No rows</h3>
          <p class="hint">The query ran, and it matched nothing. Say that, and say what to change.</p>
          <p class="blank">
            Nothing matched. {{ NO_ROWS.length }} rows came back.
            Widen the years, or drop one condition.
          </p>
        </div>

        <PlotFigure
          title="Forty rows"
          subtitle="The chart draws twelve, and it groups the rest. A silent cut reads as “this is all of it”."
          alt="Twelve bars, and a thirteenth grey bar that holds the other twenty-eight rows."
          note="28 rows are grouped as Other."
          :build="barMany"
        />
      </div>
    </section>
  </div>
</template>

<style scoped>
/* The tokens. The figures read these, and one change swaps the whole mode. */
.viz-root {
  color-scheme: light;
  --surface: #faf8f4;
  --raised: #ffffff;
  --ink-primary: #1c1a17;
  --ink-secondary: #57524a;
  --ink-muted: #8a847a;
  --grid: #e7e2d8;
  --ink-axis: #cfc9bf;
  --accent: #b4552d;
  --good: #006300;

  min-height: 100%;
  padding: 2rem 1.5rem 5rem;
  background: var(--surface);
  color: var(--ink-primary);
}

:root[data-theme="dark"] .viz-root {
  color-scheme: dark;
  --surface: #1c1a17;
  --raised: #24211d;
  --ink-primary: #f7f4ee;
  --ink-secondary: #c9c2b6;
  --ink-muted: #8a847a;
  --grid: #302c26;
  --ink-axis: #423d35;
  --accent: #d2734a;
  --good: #0ca30c;
}

.top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1.5rem;
  max-width: 74rem;
  margin: 0 auto 2.2rem;
}
.top h1 { margin: 0; font-size: 1.15rem; letter-spacing: -0.01em; }
.top p { margin: 0.35rem 0 0; max-width: 42rem; font-size: 0.8rem; line-height: 1.55; color: var(--ink-muted); }

.modes { display: flex; gap: 0.25rem; flex: none; }
.modes button {
  border: 1px solid var(--grid);
  background: transparent;
  color: var(--ink-muted);
  border-radius: 999px;
  padding: 0.3rem 0.8rem;
  font: inherit;
  font-size: 0.75rem;
  cursor: pointer;
}
.modes button.on { border-color: var(--accent); color: var(--accent); }

.block { max-width: 74rem; margin: 0 auto 2.8rem; }
.block h2 {
  margin: 0 0 1rem;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: var(--ink-muted);
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--grid);
}

.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(23rem, 1fr)); gap: 2.2rem 2.4rem; }

.hero { margin-bottom: 1.6rem; max-width: 22rem; }
.tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr)); gap: 1.6rem; }

.state h3 { margin: 0; font-size: 0.9rem; font-weight: 600; }
.state .hint { margin: 0.15rem 0 0.8rem; font-size: 0.78rem; line-height: 1.45; color: var(--ink-muted); }
.blank {
  margin: 0;
  padding: 1.1rem;
  border: 1px dashed var(--grid);
  border-radius: 8px;
  font-size: 0.8rem;
  line-height: 1.5;
  color: var(--ink-muted);
}
</style>
