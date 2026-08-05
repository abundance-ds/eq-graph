<script setup lang="ts">
/**
 * A number that leads a view.
 *
 * A single number is not a chart. One bar in a bar chart says less than the
 * number itself, so a count on its own belongs here.
 */
import { computed } from "vue";
import { fmt } from "../viz/format";

const props = defineProps<{
  label: string;
  value: number;
  /** The change against a named period. Give the period in `since`. */
  delta?: number | null;
  since?: string;
  /** True when a rise is good. It decides the colour of the change. */
  upIsGood?: boolean;
  /** Twelve points at most. The last one carries the accent. */
  spark?: { value: number }[];
  hero?: boolean;
}>();

const shown = computed(() =>
  Number.isInteger(props.value) ? fmt.compact(props.value) : fmt.one(props.value),
);

const direction = computed(() => {
  if (props.delta == null || props.delta === 0) return "flat";
  const good = props.upIsGood ?? true;
  return props.delta > 0 === good ? "good" : "bad";
});

/** The path of the sparkline, in a box of 100 by 28. */
const path = computed(() => {
  const points = props.spark ?? [];
  if (points.length < 2) return "";
  const values = points.map((p) => p.value);
  const low = Math.min(...values);
  const high = Math.max(...values);
  const span = high - low || 1;
  return points
    .map((p, i) => {
      const x = (i / (points.length - 1)) * 100;
      const y = 26 - ((p.value - low) / span) * 24;
      return `${i === 0 ? "M" : "L"}${x.toFixed(1)},${y.toFixed(1)}`;
    })
    .join(" ");
});

const lastPoint = computed(() => {
  const points = props.spark ?? [];
  if (points.length < 2) return null;
  const values = points.map((p) => p.value);
  const low = Math.min(...values);
  const span = Math.max(...values) - low || 1;
  return { x: 100, y: 26 - ((values.at(-1)! - low) / span) * 24 };
});
</script>

<template>
  <div :class="['tile', hero && 'tile--hero']">
    <p class="label">{{ label }}</p>
    <p class="value">{{ shown }}</p>

    <p v-if="delta != null" :class="['delta', `delta--${direction}`]">
      <span aria-hidden="true">{{ delta > 0 ? "↑" : delta < 0 ? "↓" : "→" }}</span>
      {{ fmt.pct(Math.abs(delta)) }}
      <span v-if="since" class="since">{{ since }}</span>
    </p>

    <svg v-if="path" class="spark" viewBox="0 0 100 28" preserveAspectRatio="none" aria-hidden="true">
      <path :d="path" fill="none" :stroke="'var(--ink-axis)'" stroke-width="1.5" vector-effect="non-scaling-stroke" />
      <circle v-if="lastPoint" :cx="lastPoint.x" :cy="lastPoint.y" r="2.5" fill="var(--accent)" />
    </svg>
  </div>
</template>

<style scoped>
.tile { min-width: 0; }
.label { margin: 0; font-size: 0.75rem; color: var(--ink-muted); }
.value {
  margin: 0.1rem 0 0;
  font-size: 1.55rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.1;
  color: var(--ink-primary);
}
.tile--hero .value { font-size: 3rem; letter-spacing: -0.03em; }
.tile--hero .label { font-size: 0.8rem; }

.delta { margin: 0.2rem 0 0; font-size: 0.72rem; font-variant-numeric: tabular-nums; }
.delta--good { color: var(--good); }
.delta--bad { color: var(--accent); }
.delta--flat { color: var(--ink-muted); }
.since { color: var(--ink-muted); }

.spark { display: block; width: 100%; height: 28px; margin-top: 0.45rem; overflow: visible; }
</style>
