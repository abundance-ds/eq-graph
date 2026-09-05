<script setup lang="ts">
import { KIND, KIND_HUE, paletteFor } from "../lib/graphScene.js";

useHead({
  title: "EQ-Graph — Explore the graph",
  meta: [{
    name: "description",
    content: "An interactive three-dimensional view of the EuroQol research knowledge graph: people, projects, papers, products, and instruments.",
  }],
});

type SceneNode = {
  id: string; k: number; l: string; s: number;
  papers?: number; led?: number; member?: number; coauthors?: number; c?: number;
  year?: number | null; g?: number[]; pi?: string; budget?: number | null;
  journal?: string; cites?: number; doi?: string | null;
  type?: string; uses?: number; i?: number[];
};
type SceneLens = { key: string; label: string; count: number; links: number; present: number[]; pos: number[] };
type SceneData = {
  groups: string[]; instruments: string[]; kinds: string[]; communities?: string[];
  nodes: SceneNode[]; lenses: SceneLens[]; edges: Record<string, number[][]>;
};
type Chip = { type: "kind" | "group" | "instrument" | "member"; value: number; label: string };
type Result = { kind: "node"; index: number } | { kind: "chip"; chip: Chip };
type Stage = {
  setLens: (key: string, opts?: { instant?: boolean }) => void;
  select: (index: number | null, opts?: { silent?: boolean; move?: boolean }) => void;
  setFilter: (fn: ((node: SceneNode, index: number) => boolean) | null) => void;
  hover: (index: number | null) => void;
  neighbours: (index: number) => number[];
  edgeCount: () => number;
  resetView: () => void;
  destroy: () => void;
};

const KIND_LABEL = ["Person", "Project", "Paper", "Product", "Instrument"];
const KIND_PLURAL = ["People", "Projects", "Papers", "Products", "Instruments"];
const KIND_RANK = [1, 2, 3, 4, 0];
const DEFAULT_LENS = "people";

const stageHost = ref<HTMLElement | null>(null);
const searchInput = ref<HTMLInputElement | null>(null);
const scene = shallowRef<SceneData | null>(null);
const stage = shallowRef<Stage | null>(null);
const loadError = ref("");
const ready = ref(false);

const lens = ref(DEFAULT_LENS);
const query = ref("");
const chips = ref<Chip[]>([]);
const selected = ref<number | null>(null);
const hovered = ref<number | null>(null);
const activeResult = ref(0);
const searchOpen = ref(false);
const linkCount = ref(0);
let pendingSelect: number | null = null;
let haystack: string[] = [];

const lenses = computed(() => scene.value?.lenses ?? []);
const currentLens = computed(() => lenses.value.find((l) => l.key === lens.value));
const palette = computed(() => (scene.value ? paletteFor(lens.value, scene.value) : []));
const visibleCount = computed(() => {
  const data = scene.value;
  const current = currentLens.value;
  if (!data || !current) return 0;
  if (!chips.value.length) return current.count;
  return current.present.filter((i) => passes(data.nodes[i]!)).length;
});

const fmt = (n: number) => new Intl.NumberFormat("en-GB").format(n);
const euro = (n: number) => (n >= 1e6 ? `€${(n / 1e6).toFixed(1)}m` : n >= 1e3 ? `€${Math.round(n / 1e3)}k` : `€${n}`);

function passes(node: SceneNode): boolean {
  const data = scene.value!;
  return chips.value.every((chip) => {
    if (chip.type === "kind") return node.k === chip.value;
    if (chip.type === "group") return Boolean(node.g?.includes(chip.value));
    if (chip.type === "member") return node.member === 1;
    if (node.k === KIND.instrument) return node.l === data.instruments[chip.value];
    return Boolean(node.i?.includes(chip.value));
  });
}

const facets = computed<Chip[]>(() => {
  const data = scene.value;
  if (!data) return [];
  return [
    ...KIND_PLURAL.map((label, value) => ({ type: "kind" as const, value, label })),
    { type: "member" as const, value: 1, label: "EuroQol members" },
    ...data.groups.map((label, value) => ({ type: "group" as const, value, label })),
    ...data.instruments.map((label, value) => ({ type: "instrument" as const, value, label })),
  ];
});

const results = computed<Result[]>(() => {
  const data = scene.value;
  const q = query.value.trim().toLowerCase();
  if (!data || q.length < 2) return [];
  const terms = q.split(/\s+/);
  const active = new Set(chips.value.map((c) => `${c.type}:${c.value}`));
  const chipHits = facets.value
    .filter((chip) => !active.has(`${chip.type}:${chip.value}`) && chip.label.toLowerCase().includes(q))
    .slice(0, 3)
    .map((chip): Result => ({ kind: "chip", chip }));
  const scored: { index: number; score: number }[] = [];
  for (let i = 0; i < data.nodes.length; i++) {
    const hay = haystack[i]!;
    if (!terms.every((t) => hay.includes(t))) continue;
    const node = data.nodes[i]!;
    const prefix = hay.startsWith(q) ? 0 : 1;
    scored.push({ index: i, score: prefix * 10 + KIND_RANK[node.k]! * 2 - node.s });
  }
  scored.sort((a, b) => a.score - b.score);
  return [...chipHits, ...scored.slice(0, 8).map((s): Result => ({ kind: "node", index: s.index }))];
});

const selectedNode = computed(() => (selected.value != null ? scene.value?.nodes[selected.value] ?? null : null));
const hoveredNode = computed(() => (hovered.value != null ? scene.value?.nodes[hovered.value] ?? null : null));

function factsFor(node: SceneNode): string[] {
  const data = scene.value!;
  if (node.k === KIND.person) {
    const parts = [`${fmt(node.papers ?? 0)} papers`, `${fmt(node.coauthors ?? 0)} co-authors`];
    if (node.led) parts.push(`${node.led} project${node.led === 1 ? "" : "s"} led`);
    if (node.member) parts.push("EuroQol member");
    return parts;
  }
  if (node.k === KIND.project) {
    const parts = [node.id];
    if (node.year) parts.push(String(node.year));
    if (node.g?.length) parts.push(node.g.map((g) => data.groups[g]!).join(" · "));
    if (node.pi) parts.push(node.pi);
    if (node.budget) parts.push(euro(node.budget));
    return parts;
  }
  if (node.k === KIND.paper) {
    const parts = [];
    if (node.year) parts.push(String(node.year));
    if (node.journal) parts.push(node.journal);
    parts.push(`${fmt(node.cites ?? 0)} citations`);
    return parts;
  }
  if (node.k === KIND.product) return [node.type || "research product"];
  return [`used in ${fmt(node.uses ?? 0)} papers`];
}

function askUrl(node: SceneNode): string {
  const question = node.k === KIND.person
    ? `What has ${node.l} published with EuroQol support, and with whom?`
    : node.k === KIND.project
      ? `What did EuroQol project ${node.id}, "${node.l}", produce?`
      : node.k === KIND.paper
        ? `Summarise the findings and limitations of "${node.l}".`
        : node.k === KIND.instrument
          ? `Which studies used ${node.l}, and in which populations?`
          : `Tell me about the research product "${node.l}".`;
  return `/?ask=${encodeURIComponent(question)}#chat`;
}

function chooseResult(result: Result) {
  if (result.kind === "chip") {
    chips.value = [...chips.value, result.chip];
    query.value = "";
    activeResult.value = 0;
    applyFilter();
    return;
  }
  query.value = "";
  searchOpen.value = false;
  searchInput.value?.blur();
  focusNode(result.index);
}

function focusNode(index: number) {
  const current = currentLens.value;
  if (!scene.value || !current || !stage.value) return;
  if (!current.present.includes(index)) {
    pendingSelect = index;
    setLens("everything");
    return;
  }
  stage.value.select(index);
}

function removeChip(chip: Chip) {
  chips.value = chips.value.filter((c) => c !== chip);
  applyFilter();
}

function applyFilter() {
  if (!stage.value) return;
  stage.value.setFilter(chips.value.length ? (node) => passes(node) : null);
}

function setLens(key: string) {
  if (!stage.value || key === lens.value) return;
  stage.value.setLens(key);
}

function clearSelection() {
  stage.value?.select(null);
}

function onSearchKey(ev: KeyboardEvent) {
  const list = results.value;
  if (ev.key === "ArrowDown") { ev.preventDefault(); activeResult.value = Math.min(list.length - 1, activeResult.value + 1); return; }
  if (ev.key === "ArrowUp") { ev.preventDefault(); activeResult.value = Math.max(0, activeResult.value - 1); return; }
  if (ev.key === "Enter") { ev.preventDefault(); const hit = list[activeResult.value]; if (hit) chooseResult(hit); return; }
  if (ev.key === "Escape") { query.value = ""; searchInput.value?.blur(); }
}

function onWindowKey(ev: KeyboardEvent) {
  const inField = (ev.target as HTMLElement | null)?.tagName === "INPUT";
  if (ev.key === "Escape" && !inField) { clearSelection(); return; }
  if (ev.key === "/" && !inField) { ev.preventDefault(); searchInput.value?.focus(); return; }
  if (!inField && ["1", "2", "3", "4"].includes(ev.key)) {
    const target = lenses.value[Number(ev.key) - 1];
    if (target) setLens(target.key);
  }
}

function syncUrl() {
  if (!import.meta.client) return;
  const params = new URLSearchParams();
  if (lens.value !== DEFAULT_LENS) params.set("lens", lens.value);
  if (selectedNode.value) params.set("focus", selectedNode.value.id);
  for (const chip of chips.value) params.append(chip.type, chip.type === "kind" ? KIND_PLURAL[chip.value]!.toLowerCase() : chip.label);
  const search = params.toString();
  history.replaceState(history.state, "", `${location.pathname}${search ? `?${search}` : ""}`);
}

function readUrl(data: SceneData): { lens: string; focus: number | null; chips: Chip[] } {
  const params = new URLSearchParams(location.search);
  const wanted = params.get("lens") ?? DEFAULT_LENS;
  const focusId = params.get("focus");
  const focus = focusId ? data.nodes.findIndex((n) => n.id === focusId) : -1;
  const found: Chip[] = [];
  for (const [type, label] of params) {
    if (type === "kind") { const value = KIND_PLURAL.findIndex((k) => k.toLowerCase() === label); if (value >= 0) found.push({ type, value, label: KIND_PLURAL[value]! }); }
    else if (type === "group") { const value = data.groups.indexOf(label); if (value >= 0) found.push({ type, value, label }); }
    else if (type === "instrument") { const value = data.instruments.indexOf(label); if (value >= 0) found.push({ type, value, label }); }
    else if (type === "member") found.push({ type, value: 1, label: "EuroQol members" });
  }
  return { lens: data.lenses.some((l) => l.key === wanted) ? wanted : DEFAULT_LENS, focus: focus >= 0 ? focus : null, chips: found };
}

watch([lens, selected, chips], syncUrl);

onMounted(async () => {
  window.addEventListener("keydown", onWindowKey);
  try {
    const response = await fetch("/graph-scene.json");
    if (!response.ok) throw new Error(`scene ${response.status}`);
    const data = (await response.json()) as SceneData;
    haystack = data.nodes.map((n) => `${n.l} ${n.id}`.toLowerCase());
    scene.value = data;
    const initial = readUrl(data);
    chips.value = initial.chips;
    const { createGraphScene } = await import("../lib/graphScene.js");
    const coarse = matchMedia("(pointer: coarse)").matches;
    const lite = coarse || window.innerWidth < 760 || (navigator.hardwareConcurrency || 8) <= 4;
    stage.value = createGraphScene(stageHost.value!, data, {
      quality: lite ? "lite" : "full",
      onHover: (index: number | null) => { hovered.value = index; },
      onSelect: (index: number | null) => { selected.value = index; },
      onLens: (key: string) => {
        lens.value = key;
        linkCount.value = stage.value?.edgeCount() ?? 0;
      },
      onSettle: () => {
        linkCount.value = stage.value?.edgeCount() ?? 0;
        if (pendingSelect != null) { const index = pendingSelect; pendingSelect = null; stage.value?.select(index); }
      },
    });
    stage.value.setLens(initial.lens);
    applyFilter();
    if (initial.focus != null) pendingSelect = initial.focus;
    ready.value = true;
  } catch (error) {
    loadError.value = error instanceof Error ? error.message : String(error);
  }
});

onBeforeUnmount(() => {
  window.removeEventListener("keydown", onWindowKey);
  stage.value?.destroy();
});
</script>

<template>
  <main class="gx-root">
    <SiteHeader current="graph" />

    <div ref="stageHost" class="gx-stage" />
    <div class="gx-glow" aria-hidden="true"><i class="a" /><i class="b" /></div>

    <p v-if="!ready && !loadError" class="gx-loading"><span>Loading the graph</span></p>
    <p v-if="loadError" class="gx-loading is-error">The graph could not be loaded. {{ loadError }}</p>

    <!-- controls: lens, then search, then whatever is selected -->
    <div class="gx-panel">
      <nav class="gx-lenses" aria-label="Graph lenses">
        <button
          v-for="(entry, i) in lenses"
          :key="entry.key"
          type="button"
          :class="{ 'is-on': entry.key === lens }"
          :aria-pressed="entry.key === lens"
          @click="setLens(entry.key)"
        ><i aria-hidden="true">{{ i + 1 }}</i>{{ entry.label }}</button>
      </nav>

      <div class="gx-search" :class="{ 'is-open': searchOpen && results.length }">
        <div class="gx-search-field">
          <svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="8.5" cy="8.5" r="5.5" /><path d="m13 13 4.5 4.5" /></svg>
          <input
            ref="searchInput"
            v-model="query"
            type="search"
            autocomplete="off"
            spellcheck="false"
            placeholder="Find a person, project, paper, or instrument"
            aria-label="Search the graph"
            @focus="searchOpen = true"
            @blur="searchOpen = false"
            @input="activeResult = 0"
            @keydown="onSearchKey"
          >
          <kbd v-if="!query" aria-hidden="true">/</kbd>
        </div>
        <ul v-if="chips.length" class="gx-chips">
          <li v-for="chip in chips" :key="`${chip.type}:${chip.value}`">
            <button type="button" @click="removeChip(chip)">
              <span>{{ chip.label }}</span><i aria-hidden="true">×</i>
            </button>
          </li>
        </ul>
        <ul v-if="searchOpen && results.length" class="gx-results">
          <li
            v-for="(result, i) in results"
            :key="result.kind === 'chip' ? `chip-${result.chip.type}-${result.chip.value}` : `node-${result.index}`"
            :class="{ 'is-active': i === activeResult }"
            @mousedown.prevent="chooseResult(result)"
            @mouseenter="activeResult = i"
          >
            <template v-if="result.kind === 'chip'">
              <em>filter</em><span>{{ result.chip.label }}</span>
            </template>
            <template v-else>
              <em :style="{ color: KIND_HUE[scene!.nodes[result.index]!.k] }">{{ KIND_LABEL[scene!.nodes[result.index]!.k] }}</em>
              <span>{{ scene!.nodes[result.index]!.l }}</span>
            </template>
          </li>
        </ul>
      </div>

      <transition name="gx-fade">
        <aside v-if="selectedNode" class="gx-card" :style="{ '--kind': KIND_HUE[selectedNode.k] }">
          <button type="button" class="gx-card-close" aria-label="Clear selection" @click="clearSelection">×</button>
          <em class="gx-kind">{{ KIND_LABEL[selectedNode.k] }}</em>
          <h2>{{ selectedNode.l }}</h2>
          <p class="gx-facts"><span v-for="fact in factsFor(selectedNode)" :key="fact">{{ fact }}</span></p>
          <p class="gx-links">
            <a :href="askUrl(selectedNode)">Ask about this</a>
            <a v-if="selectedNode.doi" :href="`https://doi.org/${selectedNode.doi}`" target="_blank" rel="noopener noreferrer">Open paper</a>
            <button type="button" @click="stage?.resetView()">Reset view</button>
          </p>
        </aside>
      </transition>
    </div>

    <!-- colour key for the current lens -->
    <ul :key="lens" class="gx-legend" aria-label="Colour key">
      <li v-for="entry in palette" :key="entry.label">
        <i :style="{ background: entry.colour }" aria-hidden="true" /><span>{{ entry.label }}</span>
      </li>
    </ul>

    <!-- readout -->
    <div class="gx-hud" aria-live="polite">
      <p v-if="hoveredNode" class="gx-hud-hover">
        <em :style="{ color: KIND_HUE[hoveredNode.k] }">{{ KIND_LABEL[hoveredNode.k] }}</em>{{ hoveredNode.l }}
      </p>
      <p v-if="currentLens" class="gx-hud-count">{{ fmt(visibleCount) }} nodes · {{ fmt(linkCount) }} links</p>
      <button v-if="ready" type="button" class="gx-hud-reset" @click="stage?.resetView()">Reset view</button>
    </div>
  </main>
</template>

<style scoped>
.gx-root {
  --paper: #fcfcfb;
  --surface: #fff;
  --ink-1: #1a1a17;
  --ink-2: #5c5c56;
  --ink-3: #8e8e86;
  --hairline: #e5e4df;
  --hairline-strong: #cbc9c1;
  --teal: #007d6c;
  --mono: var(--font-num, "IBM Plex Mono", monospace);
  --pad: clamp(1.25rem, 3vw, 3rem);
  position: fixed;
  inset: 0;
  overflow: hidden;
  background: var(--paper);
  color: var(--ink-1);
  user-select: none;
}
.gx-stage {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 1.4s ease;
}
.gx-stage.is-ready { opacity: 1; }
.gx-stage :deep(canvas) { display: block; width: 100%; height: 100%; touch-action: none; }
.gx-stage :deep(.gx-labels) {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
}
.gx-stage :deep(.gx-label) {
  position: absolute;
  top: 0;
  left: 0;
  max-width: 24ch;
  overflow: hidden;
  color: var(--ink-1);
  font: 500 11px/16px var(--font-body, "Instrument Sans", sans-serif);
  letter-spacing: .005em;
  white-space: nowrap;
  text-overflow: ellipsis;
  text-shadow: 0 0 5px var(--paper), 0 0 2px var(--paper), 0 0 1px var(--paper);
  will-change: transform, opacity;
}
.gx-stage :deep(.gx-label.is-hub) {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.gx-stage :deep(.gx-label.is-axis) {
  color: var(--ink-3);
  font: 400 10px/14px var(--mono);
  letter-spacing: .12em;
  transition: opacity .3s ease;
}
.gx-stage :deep(.gx-label.is-lit) {
  color: var(--ink-1);
  font-weight: 600;
}
/* The story's paper glow, multiplied over the drawing so both pages share a ground. */
.gx-glow {
  position: absolute;
  inset: 0;
  pointer-events: none;
  mix-blend-mode: multiply;
}
.gx-glow i {
  position: absolute;
  border-radius: 50%;
}
.gx-glow i.a { top: -18vw; left: -14vw; width: 52vw; height: 52vw; background: radial-gradient(circle, rgba(214, 163, 60, .10), rgba(214, 163, 60, 0) 70%); }
.gx-glow i.b { right: -12vw; bottom: -16vw; width: 46vw; height: 46vw; background: radial-gradient(circle, rgba(0, 125, 108, .09), rgba(0, 125, 108, 0) 70%); }

.gx-loading {
  position: absolute;
  inset: 0;
  display: grid;
  place-content: center;
  margin: 0;
  color: var(--ink-3);
  font: 400 11px/1 var(--mono);
  letter-spacing: .16em;
  text-transform: uppercase;
}
.gx-loading span { animation: gx-pulse 1.6s ease-in-out infinite; }
.gx-loading.is-error { color: #a23c2a; letter-spacing: 0; text-transform: none; font: 400 .9rem/1.5 var(--font-body); }
@keyframes gx-pulse { 0%, 100% { opacity: .4; } 50% { opacity: 1; } }

/* control column ---------------------------------------------------- */
.gx-panel {
  position: absolute;
  top: 5.6rem;
  left: var(--pad);
  z-index: 5;
  width: min(23rem, calc(100vw - 2 * var(--pad)));
}
.gx-lenses {
  display: flex;
  gap: clamp(.9rem, 1.6vw, 1.4rem);
  margin-bottom: .75rem;
}
.gx-lenses button {
  position: relative;
  display: inline-flex;
  align-items: baseline;
  gap: .4rem;
  min-height: 40px;
  padding: 0;
  border: 0;
  background: none;
  color: var(--ink-2);
  font: 600 .95rem/1 var(--font-body);
  letter-spacing: -.01em;
  cursor: pointer;
  transition: color .15s ease;
}
.gx-lenses button i {
  color: var(--ink-3);
  font: 400 10px/1 var(--mono);
  font-style: normal;
}
.gx-lenses button::after {
  content: "";
  position: absolute;
  right: 0;
  bottom: 8px;
  left: 0;
  height: 1px;
  background: currentColor;
  opacity: 0;
  transform: scaleX(.4);
  transition: opacity .15s ease, transform .15s ease;
}
.gx-lenses button:hover { color: var(--ink-1); }
.gx-lenses button.is-on { color: var(--teal); }
.gx-lenses button.is-on i { color: var(--teal); }
.gx-lenses button.is-on::after { opacity: 1; transform: scaleX(1); }

/* search ------------------------------------------------------------ */
.gx-search-field {
  position: relative;
  display: flex;
  align-items: center;
  gap: .55rem;
  border-bottom: 1px solid var(--hairline-strong);
  transition: border-color .2s ease;
}
.gx-search-field:focus-within { border-color: var(--teal); }
.gx-search-field svg {
  flex: none;
  width: 15px;
  height: 15px;
  fill: none;
  stroke: var(--ink-3);
  stroke-width: 1.5;
  stroke-linecap: round;
}
.gx-search-field input {
  flex: 1;
  min-width: 0;
  padding: .55rem 0;
  border: 0;
  background: transparent;
  color: var(--ink-1);
  font: 500 .9rem/1.2 var(--font-body);
  outline: none;
  appearance: none;
}
.gx-search-field input::placeholder { color: var(--ink-3); }
.gx-search-field input::-webkit-search-cancel-button { display: none; }
.gx-search-field kbd {
  flex: none;
  padding: .1rem .38rem;
  border: 1px solid var(--hairline);
  border-radius: 3px;
  color: var(--ink-3);
  font: 400 10px/1.3 var(--mono);
}
.gx-chips {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
  margin: .6rem 0 0;
  padding: 0;
  list-style: none;
}
.gx-chips button {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding: .3rem .55rem .3rem .65rem;
  border: 1px solid rgba(0, 125, 108, .35);
  border-radius: 999px;
  background: rgba(0, 125, 108, .07);
  color: var(--teal);
  font: 500 11px/1 var(--mono);
  letter-spacing: .02em;
  cursor: pointer;
  transition: background .15s ease, border-color .15s ease;
}
.gx-chips button:hover { background: rgba(0, 125, 108, .14); border-color: var(--teal); }
.gx-chips button i { font-style: normal; opacity: .7; }
.gx-results {
  margin: .5rem 0 0;
  padding: .3rem 0;
  list-style: none;
  border: 1px solid var(--hairline);
  border-radius: 6px;
  background: var(--surface);
  box-shadow: 0 12px 32px rgba(26, 26, 23, .08);
}
.gx-results li {
  display: grid;
  grid-template-columns: 5.4rem 1fr;
  align-items: baseline;
  gap: .6rem;
  padding: .5rem .8rem;
  cursor: pointer;
}
.gx-results li.is-active { background: #f4f4f1; }
.gx-results em {
  color: var(--ink-3);
  font: 500 10px/1.4 var(--mono);
  font-style: normal;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.gx-results span {
  overflow: hidden;
  color: var(--ink-1);
  font: 500 .84rem/1.35 var(--font-body);
  white-space: nowrap;
  text-overflow: ellipsis;
}

/* card -------------------------------------------------------------- */
.gx-card {
  position: relative;
  margin-top: 1rem;
  padding: 1rem 1.1rem 1rem;
  border: 1px solid var(--hairline);
  border-radius: 6px;
  background: var(--surface);
  box-shadow: 0 12px 32px rgba(26, 26, 23, .08);
}
.gx-card-close {
  position: absolute;
  top: .45rem;
  right: .5rem;
  width: 28px;
  height: 28px;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--ink-3);
  font: 400 18px/1 var(--font-body);
  cursor: pointer;
}
.gx-card-close:hover { color: var(--ink-1); background: #f4f4f1; }
.gx-kind {
  display: flex;
  align-items: center;
  gap: .45rem;
  margin-bottom: .45rem;
  color: var(--kind, var(--teal));
  font: 500 10px/1 var(--mono);
  font-style: normal;
  letter-spacing: .14em;
  text-transform: uppercase;
}
.gx-kind::before {
  content: "";
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: currentColor;
}
.gx-card h2 {
  margin: 0 1.2rem .5rem 0;
  color: var(--ink-1);
  font: 500 1rem/1.3 var(--font-body);
  letter-spacing: -.01em;
}
.gx-facts {
  display: flex;
  flex-wrap: wrap;
  gap: .2rem .55rem;
  margin: 0 0 .8rem;
  color: var(--ink-2);
  font: 400 11px/1.5 var(--mono);
}
.gx-facts span + span::before { content: "·"; margin-right: .55rem; color: var(--ink-3); }
.gx-links {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem 1rem;
  margin: 0;
}
.gx-links a, .gx-links button {
  padding: 0;
  border: 0;
  background: none;
  color: var(--teal);
  font: 500 .8rem/1.4 var(--font-body);
  text-decoration: none;
  cursor: pointer;
}
.gx-links button { color: var(--ink-2); }
.gx-links a:hover, .gx-links button:hover { text-decoration: underline; text-underline-offset: .2em; }

/* legend and readout ------------------------------------------------ */
.gx-legend {
  position: absolute;
  left: var(--pad);
  bottom: calc(var(--pad) * .8);
  z-index: 4;
  display: flex;
  flex-wrap: wrap;
  gap: .3rem 1rem;
  max-width: 36rem;
  margin: 0;
  padding: 0;
  list-style: none;
  animation: gx-rise .5s ease both;
}
.gx-legend li {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  color: var(--ink-2);
  font: 400 10.5px/1.6 var(--mono);
  letter-spacing: .03em;
}
.gx-legend i { width: 7px; height: 7px; border-radius: 50%; }
@keyframes gx-rise { from { opacity: 0; transform: translateY(4px); } }

.gx-hud {
  position: absolute;
  right: var(--pad);
  bottom: calc(var(--pad) * .8);
  z-index: 4;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: .25rem;
  max-width: min(26rem, 50vw);
  pointer-events: none;
  text-align: right;
}
.gx-hud p {
  margin: 0;
  color: var(--ink-3);
  font: 400 10.5px/1.5 var(--mono);
  letter-spacing: .08em;
  text-transform: uppercase;
}
.gx-hud-reset {
  margin-top: .2rem;
  padding: .2rem 0;
  border: 0;
  background: none;
  color: var(--ink-3);
  font: 400 10.5px/1.5 var(--mono);
  letter-spacing: .08em;
  text-transform: uppercase;
  cursor: pointer;
  pointer-events: auto;
  transition: color .15s ease;
}
.gx-hud-reset:hover { color: var(--teal); }
.gx-hud-hover {
  overflow: hidden;
  max-width: 100%;
  color: var(--ink-1) !important;
  letter-spacing: .01em !important;
  text-transform: none !important;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.gx-hud-hover em {
  margin-right: .6rem;
  font-style: normal;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.gx-fade-enter-active, .gx-fade-leave-active { transition: opacity .25s ease, transform .25s ease; }
.gx-fade-enter-from, .gx-fade-leave-to { opacity: 0; transform: translateY(4px); }

@media (max-width: 760px) {
  .gx-panel { top: 4.8rem; width: calc(100vw - 2 * var(--pad)); }
  .gx-lenses { gap: .8rem; }
  .gx-lenses button { min-height: 36px; font-size: .84rem; }
  .gx-card {
    position: fixed;
    right: var(--pad);
    bottom: 3.6rem;
    left: var(--pad);
    margin: 0;
    padding: .85rem .95rem;
  }
  .gx-legend { display: none; }
  .gx-hud { max-width: 60vw; }
}
</style>
