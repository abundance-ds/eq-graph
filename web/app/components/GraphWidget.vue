<script setup lang="ts">
import { nextTick, onBeforeUnmount, onMounted, shallowRef, watch } from "vue";
import type { ChatWidgetSpec } from "../types/chat";
import { createChatPlot } from "../viz/chatPlot";
import { fieldLabel, formatNumber, numeric } from "../viz/format";
import { CHART_SERIES, chartTokens } from "../viz/theme";

const props = defineProps<{ spec: ChatWidgetSpec }>();

const titleId = useId();
const plotHost = shallowRef<HTMLElement | null>(null);
const plotNode = shallowRef<HTMLElement | SVGSVGElement | null>(null);
const width = ref(0);
let observer: ResizeObserver | undefined;
let frame = 0;

const text = (value: unknown) => value == null ? "" : String(value);
const plotMark = computed(() => [
  "bar",
  "line",
  "area",
  "scatter",
  "histogram",
  "heatmap",
].includes(props.spec.mark));
const hasRows = computed(() => props.spec.rows.length > 0);

const dataColumns = computed(() => {
  if (props.spec.mark === "table" && props.spec.encoding.columns?.length) {
    return props.spec.encoding.columns;
  }
  const named = [
    props.spec.encoding.x,
    props.spec.encoding.y,
    props.spec.encoding.series,
    props.spec.encoding.value,
    props.spec.encoding.source,
    props.spec.encoding.target,
    props.spec.encoding.weight,
  ].filter((field): field is string => Boolean(field));
  return named.length ? [...new Set(named)] : Object.keys(props.spec.rows[0] ?? {});
});

const statValue = computed(() => {
  const key = props.spec.encoding.value;
  return key ? props.spec.rows[0]?.[key] : undefined;
});

const donut = computed(() => {
  const labelKey = props.spec.encoding.x;
  const valueKey = props.spec.encoding.y;
  if (!labelKey || !valueKey) return { rows: [], total: 0, background: "#e5e4df" };
  const rows = props.spec.rows.map((row, index) => ({
    label: text(row[labelKey]),
    value: Math.max(0, numeric(row[valueKey]) ?? 0),
    color: CHART_SERIES[index % CHART_SERIES.length]!,
  }));
  const total = rows.reduce((sum, row) => sum + row.value, 0);
  if (!total) return { rows, total, background: "#e5e4df" };
  let cursor = 0;
  const stops = rows.map((row) => {
    const start = cursor;
    cursor += (row.value / total) * 100;
    return `${row.color} ${start.toFixed(2)}% ${cursor.toFixed(2)}%`;
  });
  return { rows, total, background: `conic-gradient(${stops.join(", ")})` };
});

function display(value: unknown): string {
  return formatNumber(value, props.spec.options?.unit);
}

function draw() {
  const host = plotHost.value;
  if (!host || !plotMark.value || width.value < 120 || !hasRows.value) return;
  cancelAnimationFrame(frame);
  frame = requestAnimationFrame(() => {
    const next = createChatPlot(
      props.spec,
      width.value,
      chartTokens(host),
    );
    plotNode.value?.remove();
    plotNode.value = next;
    if (next) host.append(next);
  });
}

onMounted(async () => {
  await nextTick();
  if (!plotHost.value) return;
  observer = new ResizeObserver(([entry]) => {
    width.value = Math.round(entry?.contentRect.width ?? 0);
  });
  observer.observe(plotHost.value);
});

onBeforeUnmount(() => {
  cancelAnimationFrame(frame);
  observer?.disconnect();
  plotNode.value?.remove();
});

watch(
  [width, () => props.spec],
  draw,
  { deep: true },
);
</script>

<template>
  <figure class="widget" :aria-labelledby="titleId">
    <figcaption class="widget__head">
      <span :id="titleId" class="widget__title">{{ spec.title }}</span>
      <span v-if="spec.rowCount > spec.rows.length" class="widget__meta">
        {{ spec.rows.length }} of {{ spec.rowCount }} rows
      </span>
    </figcaption>

    <p v-if="!hasRows" class="widget__empty">
      No data matched this view.
    </p>

    <div v-else-if="spec.mark === 'stat'" class="stat">
      <strong>{{ display(statValue) }}</strong>
    </div>

    <div
      v-else-if="plotMark"
      ref="plotHost"
      class="widget__plot"
    />

    <ChatNetwork
      v-else-if="spec.mark === 'network'"
      :spec="spec"
    />

    <div v-else-if="spec.mark === 'donut'" class="donut">
      <div class="donut__plot" :style="{ background: donut.background }" aria-hidden="true">
        <span><strong>{{ display(donut.total) }}</strong><small>total</small></span>
      </div>
      <ul class="donut__legend">
        <li v-for="row in donut.rows" :key="row.label">
          <div class="donut__item">
            <i :style="{ background: row.color }" aria-hidden="true" />
            <span>{{ row.label }}</span>
            <strong>{{ display(row.value) }}</strong>
            <small>{{ donut.total ? Math.round(row.value / donut.total * 100) : 0 }}%</small>
          </div>
        </li>
      </ul>
    </div>

    <div v-else class="tablewrap">
      <table class="table">
        <thead>
          <tr><th v-for="column in dataColumns" :key="column" scope="col">{{ fieldLabel(column) }}</th></tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in spec.rows" :key="index">
            <td v-for="column in dataColumns" :key="column">{{ text(row[column]) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p v-if="spec.caption && hasRows" class="widget__caption">{{ spec.caption }}</p>

    <details v-if="hasRows && spec.mark !== 'table'" class="widget__data">
      <summary>View data · {{ spec.rows.length }} {{ spec.rows.length === 1 ? 'row' : 'rows' }}</summary>
      <div class="tablewrap">
        <table class="table">
          <thead>
            <tr><th v-for="column in dataColumns" :key="column" scope="col">{{ fieldLabel(column) }}</th></tr>
          </thead>
          <tbody>
            <tr v-for="(row, index) in spec.rows" :key="index">
              <td v-for="column in dataColumns" :key="column">{{ text(row[column]) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </details>
  </figure>
</template>

<style scoped>
.widget {
  margin: .25rem 0 .85rem;
  padding: .85rem 0 .1rem;
  border-top: 1px solid var(--hairline-strong, #cbc9c1);
  background: transparent;
}
.widget__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: .55rem;
}
.widget__title {
  color: var(--ink-1, #1a1a17);
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: -.01em;
}
.widget__meta {
  flex: none;
  color: var(--ink-3, #8e8e86);
  font: .65rem var(--font-num, monospace);
  font-variant-numeric: tabular-nums;
}
.widget__plot {
  width: 100%;
  min-height: 150px;
}
.widget__plot :deep(svg) { display: block; max-width: 100%; }
.widget__caption {
  max-width: 42rem;
  margin: .55rem 0 0;
  color: var(--ink-2, #5c5c56);
  font-size: .74rem;
  line-height: 1.5;
}
.widget__empty {
  margin: .2rem 0;
  padding: .9rem 0;
  color: var(--ink-3, #8e8e86);
  font-size: .8rem;
}

.stat { padding: .25rem 0 .4rem; }
.stat strong {
  color: var(--ink-1, #1a1a17);
  font: 600 clamp(2.8rem, 7vw, 4.4rem)/.95 var(--font-num, monospace);
  letter-spacing: -.065em;
  font-variant-numeric: tabular-nums;
}

.donut {
  display: grid;
  grid-template-columns: minmax(9rem, 12rem) minmax(0, 1fr);
  align-items: center;
  gap: clamp(1.5rem, 5vw, 3.4rem);
  padding: .4rem 0;
}
.donut__plot { position: relative; aspect-ratio: 1; border-radius: 50%; }
.donut__plot::after {
  position: absolute;
  inset: 27%;
  border-radius: 50%;
  background: var(--surface, #fff);
  content: "";
}
.donut__plot > span {
  position: absolute;
  z-index: 1;
  inset: 31%;
  display: grid;
  place-content: center;
  text-align: center;
}
.donut__plot strong { color: var(--ink-1, #1a1a17); font: 600 1.15rem var(--font-num, monospace); }
.donut__plot small { color: var(--ink-3, #8e8e86); font-size: .6rem; }
.donut__legend { margin: 0; padding: 0; list-style: none; }
.donut__legend li { border-bottom: 1px solid var(--hairline, #e5e4df); }
.donut__item {
  display: grid;
  grid-template-columns: .55rem minmax(0, 1fr) auto 2.3rem;
  align-items: center;
  gap: .55rem;
  width: 100%;
  min-height: 34px;
  padding: .38rem .15rem;
  color: inherit;
  font-size: .73rem;
  text-align: left;
}
.donut__legend i { width: .48rem; height: .48rem; border-radius: 50%; }
.donut__legend strong { font: 500 .7rem var(--font-num, monospace); }
.donut__legend small { color: var(--ink-3, #8e8e86); font: .65rem var(--font-num, monospace); text-align: right; }

.tablewrap { overflow-x: auto; }
.table { width: 100%; border-collapse: collapse; font-size: .76rem; }
.table th {
  padding: .42rem .8rem .42rem 0;
  border-bottom: 1px solid var(--hairline-strong, #cbc9c1);
  color: var(--ink-2, #5c5c56);
  font-weight: 600;
  text-align: left;
  white-space: nowrap;
}
.table td {
  padding: .42rem .8rem .42rem 0;
  border-bottom: 1px solid var(--hairline, #e5e4df);
  color: var(--ink-1, #1a1a17);
  font-variant-numeric: tabular-nums;
}
.table tr:last-child td { border-bottom: 0; }

.widget__data { margin-top: .55rem; width: 100%; }
.widget__data summary {
  width: max-content;
  color: var(--ink-3, #8e8e86);
  font-size: .69rem;
  cursor: pointer;
}
.widget__data summary:hover { color: var(--accent, #007d6c); }
.widget__data .tablewrap { margin-top: .45rem; max-height: 16rem; }
.widget__data .table { font-size: .7rem; }

@media (max-width: 560px) {
  .widget { padding-top: .7rem; }
  .widget__head { align-items: flex-start; }
  .donut { grid-template-columns: 1fr; }
  .donut__plot { width: min(62%, 11rem); margin: 0 auto; }
  .donut__item { min-height: 44px; }
  .stat strong { font-size: clamp(2.65rem, 15vw, 3.6rem); }
}
</style>
