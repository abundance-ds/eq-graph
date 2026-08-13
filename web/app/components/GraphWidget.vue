<script setup lang="ts">
/**
 * Draws one widget from a resolved specification.
 *
 * Both frontend pillars use this component. In the chat, the model writes the
 * specification. In the narrative story, a person writes it. The renderer is
 * the same, so build it once.
 */
const props = defineProps<{
  spec: {
    mark: "stat" | "bar" | "line" | "table";
    title: string;
    caption?: string;
    encoding: {
      x?: string; y?: string; series?: string; value?: string; columns?: string[];
    };
    options?: { orientation?: "vertical" | "horizontal"; unit?: string };
    rows: Record<string, unknown>[];
    rowCount: number;
  };
}>();

const num = (v: unknown) => (typeof v === "number" ? v : Number(v) || 0);
const text = (v: unknown) => (v === null || v === undefined ? "" : String(v));

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
  const { x, y } = props.spec.encoding;
  const rows = props.spec.rows;
  const max = Math.max(1, ...rows.map((r) => num(r[y!])));
  return rows.map((r) => ({
    label: text(r[x!]),
    value: num(r[y!]),
    pct: (num(r[y!]) / max) * 100,
  }));
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
  <figure class="widget">
    <figcaption class="widget__head">
      <span class="widget__title">{{ spec.title }}</span>
      <span v-if="spec.rowCount > spec.rows.length" class="widget__meta">
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
      <div v-for="(bar, i) in bars" :key="i" class="bar">
        <span class="bar__label" :title="bar.label">{{ bar.label }}</span>
        <span class="bar__track">
          <span class="bar__fill" :style="{ [horizontal ? 'width' : 'height']: bar.pct + '%' }" />
        </span>
        <span class="bar__value">{{ fmt(bar.value) }}{{ spec.options?.unit ?? "" }}</span>
      </div>
    </div>

    <!-- line -->
    <div v-else-if="spec.mark === 'line'" class="line">
      <svg viewBox="0 0 640 180" preserveAspectRatio="none" class="line__svg">
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

    <p v-if="spec.caption" class="widget__caption">{{ spec.caption }}</p>
  </figure>
</template>

<style scoped>
.widget { margin: 0.75rem 0; border: 1px solid #e4e1da; border-radius: 10px; padding: 0.9rem 1rem; background: #fff; }
.widget__head { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; margin-bottom: 0.7rem; }
.widget__title { font-weight: 600; font-size: 0.9rem; color: #1c1a17; }
.widget__meta { font-size: 0.7rem; color: #8a847a; font-variant-numeric: tabular-nums; }
.widget__caption { margin: 0.7rem 0 0; font-size: 0.75rem; color: #7a746a; }

.stat { display: flex; align-items: baseline; gap: 0.35rem; }
.stat__value { font-size: 2.4rem; font-weight: 650; letter-spacing: -0.02em; color: #1c1a17; font-variant-numeric: tabular-nums; }
.stat__unit { font-size: 1rem; color: #8a847a; }

.bars--h .bar { display: grid; grid-template-columns: minmax(6rem, 11rem) 1fr auto; align-items: center; gap: 0.6rem; margin-bottom: 0.3rem; }
.bars--h .bar__track { height: 0.85rem; background: #f1efea; border-radius: 3px; overflow: hidden; }
.bars--h .bar__fill { display: block; height: 100%; background: #b4552d; border-radius: 3px; }
.bars--v { display: flex; align-items: flex-end; gap: 0.4rem; height: 190px; }
.bars--v .bar { display: flex; flex-direction: column-reverse; align-items: center; gap: 0.3rem; flex: 1; height: 100%; }
.bars--v .bar__track { width: 100%; flex: 1; display: flex; align-items: flex-end; background: none; }
.bars--v .bar__fill { display: block; width: 100%; background: #b4552d; border-radius: 3px 3px 0 0; }
.bars--v .bar__label { font-size: 0.65rem; text-align: center; }
.bar__label { font-size: 0.75rem; color: #4a453e; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.bar__value { font-size: 0.75rem; color: #1c1a17; font-variant-numeric: tabular-nums; }

.line__svg { width: 100%; height: 180px; display: block; }
.line__area { fill: #b4552d; opacity: 0.1; }
.line__stroke { fill: none; stroke: #b4552d; stroke-width: 2; vector-effect: non-scaling-stroke; }
.line__dot { fill: #b4552d; }
.line__axis { display: flex; justify-content: space-between; font-size: 0.7rem; color: #8a847a; }

.tablewrap { overflow-x: auto; }
.table { width: 100%; border-collapse: collapse; font-size: 0.78rem; }
.table th { text-align: left; font-weight: 600; color: #7a746a; border-bottom: 1px solid #e4e1da; padding: 0.35rem 0.6rem 0.35rem 0; white-space: nowrap; }
.table td { padding: 0.35rem 0.6rem 0.35rem 0; border-bottom: 1px solid #f4f2ee; color: #29261f; }
.table tr:last-child td { border-bottom: none; }
</style>
