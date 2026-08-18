<script setup lang="ts">
import type { ChatWidgetSpec } from "../types/chat";

/**
 * Draws one widget from a resolved specification.
 *
 * Both frontend pillars use this component. In the chat, the model writes the
 * specification. In the narrative story, a person writes it. The renderer is
 * the same, so build it once.
 */
const props = defineProps<{
  reference?: boolean;
  spec: ChatWidgetSpec;
  /** Labels currently picked out on this chart. Selection is the comparison —
      there is no separate "add" step, so this is the whole interaction state. */
  selected?: string[];
}>();

const emit = defineEmits<{
  select: [value: { label: string; value: number }];
}>();

const titleId = useId();

const num = (v: unknown) => (typeof v === "number" ? v : Number(v) || 0);
const text = (v: unknown) => (v === null || v === undefined ? "" : String(v));
const isNumeric = (v: unknown) => {
  if (typeof v === "number") return Number.isFinite(v);
  return typeof v === "string" && v.trim() !== "" && Number.isFinite(Number(v));
};

const categoryValueKeys = computed(() => {
  const x = props.spec.encoding.x!;
  const y = props.spec.encoding.y!;
  const rows = props.spec.rows;
  const ratio = (key: string) => {
    const values = rows.map((row) => row[key]).filter((value) => value !== null && value !== undefined && value !== "");
    return values.length ? values.filter(isNumeric).length / values.length : 0;
  };
  return ratio(x) > ratio(y) ? { label: y, value: x } : { label: x, value: y };
});

const fmt = (v: unknown) => {
  const n = num(v);
  if (!Number.isFinite(n)) return text(v);
  if (Math.abs(n) >= 1_000_000) return (n / 1_000_000).toFixed(1) + "M";
  if (Math.abs(n) >= 1_000) return (n / 1_000).toFixed(1) + "k";
  return Number.isInteger(n) ? String(n) : n.toFixed(2);
};

// --- stat ---
const statValue = computed(() => {
  const key = props.spec.encoding.value!;
  return props.spec.rows[0]?.[key];
});

// --- bar ---
const horizontal = computed(() => props.spec.options?.orientation === "horizontal");
const bars = computed(() => {
  const { label, value } = categoryValueKeys.value;
  const rows = props.spec.rows;
  const max = Math.max(1, ...rows.map((row) => num(row[value])));
  return rows.map((r) => ({
    label: text(r[label]),
    value: num(r[value]),
    pct: (num(r[value]) / max) * 100,
  }));
});

// --- donut ---
const SERIES = computed(() => [props.spec.options?.color ?? "#007d6c", "#2a78d6", "#eb6834", "#eda100", "#e87ba4", "#4a3aa7"]);
const donut = computed(() => {
  const { label, value } = categoryValueKeys.value;
  const rows = props.spec.rows.map((row, index) => ({
    label: text(row[label]),
    value: num(row[value]),
    color: SERIES.value[index % SERIES.value.length]!,
  }));
  const total = rows.reduce((sum, row) => sum + row.value, 0) || 1;
  let cursor = 0;
  const stops = rows.map((row) => {
    const start = cursor;
    cursor += (row.value / total) * 100;
    return `${row.color} ${start.toFixed(2)}% ${cursor.toFixed(2)}%`;
  });
  return { rows, total, background: `conic-gradient(${stops.join(", ")})` };
});

// --- line ---
const linePath = computed(() => {
  const { x, y } = props.spec.encoding;
  const rows = [...props.spec.rows].sort((a, b) => num(a[x!]) - num(b[x!]));
  if (rows.length === 0) return { d: "", area: "", points: [], min: 0, max: 0, first: "", last: "" };
  const values = rows.map((r) => num(r[y!]));
  const max = Math.max(...values);
  const min = Math.min(0, ...values);
  const W = 640, H = 180, PAD = 8;
  const step = rows.length > 1 ? (W - PAD * 2) / (rows.length - 1) : 0;
  const scale = (v: number) => H - PAD - ((v - min) / (max - min || 1)) * (H - PAD * 2);
  const points = rows.map((r, i) => ({
    cx: PAD + i * step,
    cy: scale(num(r[y!])),
    label: text(r[x!]),
    value: num(r[y!]),
  }));
  const d = points.map((p, i) => `${i === 0 ? "M" : "L"}${p.cx.toFixed(1)},${p.cy.toFixed(1)}`).join(" ");
  const area = `${d} L${points.at(-1)!.cx.toFixed(1)},${H - PAD} L${points[0]!.cx.toFixed(1)},${H - PAD} Z`;
  return { d, area, points, min, max, first: points[0]!.label, last: points.at(-1)!.label };
});

// --- table ---
const tableColumns = computed(
  () => props.spec.encoding.columns ?? Object.keys(props.spec.rows[0] ?? {}),
);
</script>

<template>
  <figure
    :class="['widget', reference && 'widget--reference xp-figure']"
    :aria-labelledby="titleId"
    :style="{ '--widget-accent': spec.options?.color ?? '#007d6c' }"
  >
    <figcaption class="widget__head xp-figure-head">
      <span :id="titleId" class="widget__title xp-figure-title">{{ spec.title }}</span>
      <span v-if="spec.rowCount > spec.rows.length" class="widget__meta xp-figure-note">
        showing {{ spec.rows.length }} of {{ spec.rowCount }}
      </span>
    </figcaption>

    <!-- stat -->
    <div v-if="spec.mark === 'stat'" class="stat">
      <span class="stat__value">{{ fmt(statValue) }}</span>
      <span v-if="spec.options?.unit" class="stat__unit">{{ spec.options.unit }}</span>
    </div>

    <!-- bar -->
    <div v-else-if="spec.mark === 'bar'" :class="horizontal ? 'bars bars--h' : 'bars bars--v'">
      <button
        v-for="(bar, i) in bars"
        :key="i"
        type="button"
        :class="['bar', (selected ?? []).includes(bar.label) && 'is-picked']"
        :aria-pressed="(selected ?? []).includes(bar.label)"
        :aria-label="`${bar.label}: ${fmt(bar.value)}`"
        @click="emit('select', { label: bar.label, value: bar.value })"
      >
        <span class="bar__label" :title="bar.label">{{ bar.label }}</span>
        <span class="bar__track">
          <span class="bar__fill" :style="{ [horizontal ? 'width' : 'height']: bar.pct + '%' }" />
        </span>
        <span class="bar__value">{{ fmt(bar.value) }}{{ spec.options?.unit ?? "" }}</span>
      </button>
    </div>

    <!-- line -->
    <div v-else-if="spec.mark === 'line'" class="line">
      <svg viewBox="0 0 640 180" preserveAspectRatio="none" class="line__svg" role="img" :aria-label="spec.title">
        <path :d="linePath.area" class="line__area" />
        <path :d="linePath.d" class="line__stroke" />
        <circle v-for="(p, i) in linePath.points" :key="i" :cx="p.cx" :cy="p.cy" r="3" class="line__dot">
          <title>{{ p.label }}: {{ fmt(p.value) }}</title>
        </circle>
      </svg>
      <div class="line__axis">
        <span>{{ linePath.first }}</span>
        <span>{{ linePath.last }}</span>
      </div>
    </div>

    <!-- donut -->
    <div v-else-if="spec.mark === 'donut'" class="donut">
      <div class="donut__plot" :style="{ background: donut.background }">
        <span><strong>{{ fmt(donut.total) }}</strong><small>total</small></span>
      </div>
      <ul class="donut__legend">
        <li v-for="row in donut.rows" :key="row.label">
          <button type="button" :aria-label="`${row.label}: ${fmt(row.value)}`" @click="emit('select', { label: row.label, value: row.value })">
            <i :style="{ background: row.color }" aria-hidden="true" />
            <span>{{ row.label }}</span>
            <strong>{{ fmt(row.value) }}</strong>
          </button>
        </li>
      </ul>
    </div>

    <!-- table -->
    <div v-else class="tablewrap">
      <table class="table">
        <thead>
          <tr><th v-for="c in tableColumns" :key="c">{{ c }}</th></tr>
        </thead>
        <tbody>
          <tr v-for="(row, i) in spec.rows" :key="i">
            <td v-for="c in tableColumns" :key="c">{{ text(row[c]) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p v-if="spec.options?.hint" class="widget__hint">{{ spec.options.hint }}</p>
    <p v-if="spec.caption" class="widget__caption">{{ spec.caption }}</p>

    <div v-if="spec.mark !== 'table'" class="sr-only">
      <table>
        <caption>{{ spec.title }} data</caption>
        <thead><tr><th>Label</th><th>Value</th></tr></thead>
        <tbody>
          <tr v-for="(row, index) in spec.rows" :key="index">
            <td>{{ text(row[spec.encoding.x ?? spec.encoding.value ?? '']) }}</td>
            <td>{{ text(row[spec.encoding.y ?? spec.encoding.value ?? '']) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </figure>
</template>

<style scoped>
.widget { margin: 1rem 0; border: 1px solid #e6e6e9; border-radius: 0; padding: 1.15rem 1.2rem; background: #fff; }
.widget--reference { margin: 0; border-radius: 16px; padding: 1rem 1.1rem 1.1rem; }
.widget__head { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; margin-bottom: 0.7rem; }
.widget__title { font-weight: 600; font-size: 0.9rem; color: #1a1a17; }
.widget__meta { font: 0.65rem var(--font-mono, monospace); color: #8e8e86; font-variant-numeric: tabular-nums; }
.widget__caption { margin: 0.8rem 0 0; font-size: 0.72rem; line-height: 1.5; color: #5b6068; }
.widget__hint { margin: 0.7rem 0 0; font-size: 0.72rem; line-height: 1.45; color: #8e939b; }

.stat { display: flex; align-items: baseline; gap: 0.35rem; }
.stat__value { font-size: 2.4rem; font-weight: 600; letter-spacing: -0.04em; color: #1a1a17; font-variant-numeric: tabular-nums; }
.stat__unit { font-size: 1rem; color: #8a847a; }

.bars--h .bar { display: grid; grid-template-columns: minmax(6rem, 11rem) 1fr auto; align-items: center; gap: 0.6rem; margin-bottom: 0.3rem; }
.bars--h .bar__track { height: 0.75rem; background: #f0f1f1; border-radius: 2px; overflow: hidden; }
.bar { appearance: none; border: 0; padding: 0; width: 100%; background: transparent; color: inherit; font: inherit; text-align: left; cursor: pointer; }
.bar:focus-visible { outline: 2px solid var(--widget-accent); outline-offset: 3px; border-radius: 3px; }
/* A picked row is outlined, not recoloured. The bar's colour already carries
   its category, so tinting it to show selection would overwrite meaning with
   state. An outline sits on top of the encoding instead of replacing it. */
.bar.is-picked { outline: 1.5px solid var(--ink-1, #1c1a17); outline-offset: 4px; border-radius: 4px; }
.bar:not(.is-picked):hover .bar__fill { filter: brightness(0.94); }
.bars--h .bar__fill { display: block; height: 100%; background: var(--widget-accent); border-radius: 2px; }
.bars--v { display: flex; align-items: flex-end; gap: 0.4rem; height: 190px; }
.bars--v .bar { display: flex; flex-direction: column-reverse; align-items: center; gap: 0.3rem; flex: 1; height: 100%; }
.bars--v .bar__track { width: 100%; flex: 1; display: flex; align-items: flex-end; background: none; }
.bars--v .bar__fill { display: block; width: 100%; background: var(--widget-accent); border-radius: 2px 2px 0 0; }
.bars--v .bar__label { font-size: 0.65rem; text-align: center; }
.bar__label { font-size: 0.75rem; color: #4a453e; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.bar__value { font-size: 0.75rem; color: #1c1a17; font-variant-numeric: tabular-nums; }

.line__svg { width: 100%; height: 180px; display: block; }
.line__area { fill: var(--widget-accent); opacity: 0.1; }
.line__stroke { fill: none; stroke: var(--widget-accent); stroke-width: 2; vector-effect: non-scaling-stroke; }
.line__dot { fill: var(--widget-accent); }
.line__axis { display: flex; justify-content: space-between; font-size: 0.7rem; color: #8a847a; }

.donut { display: grid; grid-template-columns: minmax(9rem, 12rem) 1fr; align-items: center; gap: 2rem; }
.donut__plot { position: relative; aspect-ratio: 1; border-radius: 50%; }
.donut__plot::after { content: ""; position: absolute; inset: 25%; border-radius: 50%; background: #fff; }
.donut__plot > span { position: absolute; z-index: 1; inset: 30%; display: grid; place-content: center; text-align: center; }
.donut__plot strong { font: 600 1.25rem var(--font-mono, monospace); }
.donut__plot small { color: #8e8e86; font-size: 0.62rem; }
.donut__legend { margin: 0; padding: 0; list-style: none; }
.donut__legend li { border-bottom: 1px solid #f0f0f1; }
.donut__legend button { display: grid; grid-template-columns: 0.55rem minmax(0, 1fr) auto; align-items: center; gap: 0.55rem; width: 100%; padding: 0.38rem 0; border: 0; background: transparent; color: inherit; font: inherit; font-size: 0.72rem; text-align: left; cursor: pointer; }
.donut__legend i { width: 0.48rem; height: 0.48rem; border-radius: 50%; }
.donut__legend strong { font-family: var(--font-mono, monospace); font-weight: 500; }

.tablewrap { overflow-x: auto; }
.table { width: 100%; border-collapse: collapse; font-size: 0.78rem; }
.table th { text-align: left; font-weight: 600; color: #7a746a; border-bottom: 1px solid #e4e1da; padding: 0.35rem 0.6rem 0.35rem 0; white-space: nowrap; }
.table td { padding: 0.35rem 0.6rem 0.35rem 0; border-bottom: 1px solid #f4f2ee; color: #29261f; }
.table tr:last-child td { border-bottom: none; }

.widget--reference .bars--h .bar { grid-template-columns: minmax(7.5rem, 11.9rem) 1fr auto; min-height: 1.85rem; margin: 0; }
.widget--reference .bars--h .bar__track { height: 1rem; background: transparent; }
.widget--reference .bars--h .bar__fill { border-radius: 3px; }
.widget--reference .bar__label { color: #14171a; font-size: 0.75rem; }
.widget--reference .bar__value { color: #5b6068; font: 0.72rem var(--font-num, monospace); }
.widget--reference .widget__caption { color: #8e939b; font-size: 0.72rem; }

@media (max-width: 520px) {
  .bars--h .bar { grid-template-columns: minmax(5rem, 8rem) 1fr auto; }
  .widget--reference .bars--h .bar { min-height: 2.75rem; }
  .donut__legend button { min-height: 2.75rem; }
  .donut { grid-template-columns: 1fr; }
  .donut__plot { width: min(70%, 12rem); margin: 0 auto; }
}
</style>
