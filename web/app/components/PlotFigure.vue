<script setup lang="ts">
/**
 * One figure: a title, a subtitle, the plot, a note, and the same data as a
 * table behind a control.
 *
 * The component draws in the browser only, because Plot needs a document. It
 * draws again when the column changes width and when the page changes between
 * the light and the dark mode.
 */
import { nextTick, onBeforeUnmount, onMounted, ref, shallowRef, watch } from "vue";
import * as Plot from "@observablehq/plot";
import { tokens } from "../viz/theme";
import type { Tokens } from "../viz/plot";

const props = defineProps<{
  title: string;
  subtitle?: string;
  note?: string;
  /** What a person who cannot see the figure must be told. */
  alt: string;
  /** Builds the Plot options. It gets the tokens and the width it may use. */
  build: (t: Tokens, width: number) => any;
  /** The same numbers as a table. Every value stays reachable. */
  table?: { columns: string[]; rows: Record<string, unknown>[] };
  /** A figure is wide, not tall. Give a height only when the mark needs one. */
  height?: number;
}>();

const host = ref<HTMLElement | null>(null);
const width = ref(0);
const dark = ref(false);
const open = ref(false);
const node = shallowRef<HTMLElement | SVGElement | null>(null);

let frame = 0;

function draw() {
  const target = host.value;
  if (!target || width.value < 120) return;
  cancelAnimationFrame(frame);
  frame = requestAnimationFrame(() => {
    const figure = Plot.plot({
      width: width.value,
      ...props.build(tokens(dark.value), width.value),
    });
    node.value?.remove();
    node.value = figure;
    target.append(figure);
  });
}

// --- what makes the figure draw again ---------------------------------------

let observer: ResizeObserver | undefined;
let media: MediaQueryList | undefined;
let themeWatcher: MutationObserver | undefined;

function readMode() {
  const stamp = document.documentElement.dataset.theme;
  dark.value = stamp === "dark" ? true : stamp === "light" ? false : Boolean(media?.matches);
}

onMounted(async () => {
  media = window.matchMedia("(prefers-color-scheme: dark)");
  media.addEventListener("change", readMode);
  themeWatcher = new MutationObserver(readMode);
  themeWatcher.observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
  readMode();

  // The element must exist before the observer takes it.
  await nextTick();
  if (!host.value) return;
  observer = new ResizeObserver(([entry]) => {
    width.value = Math.round(entry!.contentRect.width);
  });
  observer.observe(host.value);
});

onBeforeUnmount(() => {
  cancelAnimationFrame(frame);
  observer?.disconnect();
  themeWatcher?.disconnect();
  media?.removeEventListener("change", readMode);
});

watch([width, dark, () => props.build], draw);
</script>

<template>
  <figure class="fig">
    <figcaption class="cap">
      <h3>{{ title }}</h3>
      <p v-if="subtitle">{{ subtitle }}</p>
    </figcaption>

    <div ref="host" class="plot" role="img" :aria-label="alt" :style="height ? { minHeight: `${height}px` } : undefined" />

    <p v-if="note" class="note">{{ note }}</p>

    <details v-if="table" class="table">
      <summary>Table</summary>
      <div class="scroll">
        <table>
          <thead>
            <tr><th v-for="column in table.columns" :key="column" scope="col">{{ column }}</th></tr>
          </thead>
          <tbody>
            <tr v-for="(row, i) in table.rows" :key="i">
              <td v-for="column in table.columns" :key="column">{{ row[column] }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </details>
  </figure>
</template>

<style scoped>
.fig { margin: 0; }
.cap h3 { margin: 0; font-size: 0.9rem; font-weight: 600; letter-spacing: -0.01em; color: var(--ink-primary); }
.cap p { margin: 0.15rem 0 0.55rem; font-size: 0.78rem; line-height: 1.45; color: var(--ink-muted); }
.plot { width: 100%; }
.note { margin: 0.45rem 0 0; font-size: 0.7rem; color: var(--ink-muted); }

.table { margin-top: 0.5rem; }
.table summary { font-size: 0.7rem; color: var(--ink-muted); cursor: pointer; width: max-content; }
.table summary:hover { color: var(--accent); }
.scroll { overflow-x: auto; margin-top: 0.4rem; }
table { border-collapse: collapse; font-size: 0.72rem; width: 100%; }
th, td { text-align: left; padding: 0.28rem 0.7rem 0.28rem 0; border-bottom: 1px solid var(--grid); white-space: nowrap; }
th { font-weight: 600; color: var(--ink-secondary); }
td { color: var(--ink-secondary); font-variant-numeric: tabular-nums; }
</style>
