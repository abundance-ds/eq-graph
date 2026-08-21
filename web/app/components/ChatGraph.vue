<script setup lang="ts">
/**
 * The answer, drawn as a graph.
 *
 * A chart answers "how much" — one thing, measured. A graph answers "what
 * connects to what". So this only ever appears for an answer whose rows carry
 * TWO entity columns, because that is the only case where there is a
 * relationship to draw. A graph of one entity with counts beside it is a bar
 * chart with extra steps and worse legibility.
 *
 * Two columns of nodes with links between them, rather than a force-directed
 * cloud. In a chat the reader has a narrow strip of page and a question in
 * mind; a hairball makes them hunt. Two ranked columns can be read left to
 * right in the order the sentence above already put them.
 */
import type { ChatWidgetSpec } from "../types/chat";

const props = defineProps<{ spec: ChatWidgetSpec; from: string; to: string }>();
const emit = defineEmits<{ ask: [question: string] }>();

const MAX_NODES = 8;   // per side — past this the links cross into noise

type Node = { label: string; weight: number; y: number };

const model = computed(() => {
  const rows = props.spec.rows ?? [];
  const valueKey = props.spec.encoding?.value;

  const weigh = (key: string) => {
    const totals = new Map<string, number>();
    for (const row of rows) {
      const label = String(row[key] ?? "").trim();
      if (!label) continue;
      const amount = valueKey && Number(row[valueKey]) ? Number(row[valueKey]) : 1;
      totals.set(label, (totals.get(label) ?? 0) + amount);
    }
    return [...totals.entries()].sort((a, b) => b[1] - a[1]).slice(0, MAX_NODES);
  };

  const left = weigh(props.from);
  const right = weigh(props.to);
  const leftIndex = new Map(left.map(([label], i) => [label, i]));
  const rightIndex = new Map(right.map(([label], i) => [label, i]));

  const place = (list: [string, number][]): Node[] => {
    const step = list.length > 1 ? 100 / (list.length - 1) : 0;
    return list.map(([label, weight], i) => ({
      label, weight,
      y: list.length > 1 ? 6 + (step * i) * 0.88 : 50,
    }));
  };

  const leftNodes = place(left);
  const rightNodes = place(right);

  // One link per row that lands on two nodes we kept. Weight sets the stroke,
  // so a thick line means many studies, not many rows.
  const links = new Map<string, { a: Node; b: Node; weight: number }>();
  for (const row of rows) {
    const a = String(row[props.from] ?? "").trim();
    const b = String(row[props.to] ?? "").trim();
    if (!leftIndex.has(a) || !rightIndex.has(b)) continue;
    const key = `${a}→${b}`;
    const amount = valueKey && Number(row[valueKey]) ? Number(row[valueKey]) : 1;
    const found = links.get(key);
    if (found) found.weight += amount;
    else links.set(key, { a: leftNodes[leftIndex.get(a)!]!, b: rightNodes[rightIndex.get(b)!]!, weight: amount });
  }

  const heaviest = Math.max(1, ...[...links.values()].map((l) => l.weight));
  return { leftNodes, rightNodes, links: [...links.values()], heaviest };
});

const picked = ref<string | null>(null);
function choose(label: string) {
  picked.value = picked.value === label ? null : label;
}
</script>

<template>
  <figure class="cg">
    <svg :viewBox="`0 0 100 ${Math.max(46, Math.max(model.leftNodes.length, model.rightNodes.length) * 11)}`"
         preserveAspectRatio="none" class="cg-plot" role="img"
         :aria-label="`${from} linked to ${to}`">
      <!-- Links first, so a node always sits on top of its own threads. -->
      <path
        v-for="(link, i) in model.links"
        :key="i"
        :class="['cg-link', picked && link.a.label !== picked && link.b.label !== picked && 'is-dim']"
        :d="`M 26 ${link.a.y} C 50 ${link.a.y}, 50 ${link.b.y}, 74 ${link.b.y}`"
        :style="{ strokeWidth: (0.4 + (link.weight / model.heaviest) * 2.4).toFixed(2) }"
      />
      <circle v-for="node in model.leftNodes" :key="`l${node.label}`"
              class="cg-dot is-from" cx="26" :cy="node.y" r="1.1" />
      <circle v-for="node in model.rightNodes" :key="`r${node.label}`"
              class="cg-dot is-to" cx="74" :cy="node.y" r="1.1" />
    </svg>

    <!-- Labels are real buttons in the layer above, not SVG text: they need to
         be clickable, focusable and legible at any zoom. -->
    <div class="cg-names">
      <button
        v-for="node in model.leftNodes" :key="`ln${node.label}`"
        type="button"
        :class="['cg-name', 'is-left', picked === node.label && 'is-picked']"
        :style="{ top: `${node.y}%` }"
        @click="choose(node.label)"
      >{{ node.label }}</button>
      <button
        v-for="node in model.rightNodes" :key="`rn${node.label}`"
        type="button"
        :class="['cg-name', 'is-right', picked === node.label && 'is-picked']"
        :style="{ top: `${node.y}%` }"
        @click="choose(node.label)"
      >{{ node.label }}</button>
    </div>

    <figcaption v-if="picked" class="cg-ask">
      <span>{{ picked }}</span>
      <button type="button" @click="emit('ask', `What research involves ${picked}?`)">Ask about this</button>
      <button type="button" class="cg-clear" @click="picked = null">Clear</button>
    </figcaption>
    <figcaption v-else class="cg-hint">
      Line thickness is the number of studies. Click a name to follow it.
    </figcaption>
  </figure>
</template>

<style scoped>
.cg { position: relative; margin: 0; padding: 0.4rem 0 0; }
.cg-plot { width: 100%; height: auto; overflow: visible; display: block; }

.cg-link {
  fill: none;
  stroke: var(--accent, #007d6c);
  stroke-opacity: 0.26;
  vector-effect: non-scaling-stroke;
  transition: stroke-opacity 0.18s ease;
}
.cg-link.is-dim { stroke-opacity: 0.06; }

.cg-dot { fill: var(--ink-1, #1a1a17); }
.cg-dot.is-to { fill: var(--accent, #007d6c); }

.cg-names { position: absolute; inset: 0; pointer-events: none; }
.cg-name {
  position: absolute;
  transform: translateY(-50%);
  max-width: 24%;
  padding: 0.15rem 0.3rem;
  border: 0;
  border-radius: 5px;
  background: none;
  color: var(--ink-2, #5c5c56);
  font: inherit;
  font-size: 0.78rem;
  line-height: 1.25;
  cursor: pointer;
  pointer-events: auto;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.cg-name.is-left { right: 76%; text-align: right; }
.cg-name.is-right { left: 76%; text-align: left; }
.cg-name:hover { color: var(--ink-1, #1a1a17); background: var(--sunk, #f7f7f5); }
.cg-name.is-picked { color: var(--ink-1, #1a1a17); font-weight: 500; background: var(--sunk, #f7f7f5); }
.cg-name:focus-visible { outline: 2px solid var(--accent, #007d6c); outline-offset: 1px; }

.cg-hint, .cg-ask {
  margin-top: 0.5rem;
  color: var(--ink-3, #8e8e86);
  font-size: 0.74rem;
}
.cg-ask { display: flex; align-items: center; flex-wrap: wrap; gap: 0.45rem; }
.cg-ask > span { color: var(--ink-1, #1a1a17); font-weight: 500; }
.cg-ask button {
  min-height: 30px;
  padding: 0.25rem 0.6rem;
  border: 1px solid var(--hairline, #e5e4df);
  border-radius: 999px;
  background: none;
  color: var(--ink-2, #5c5c56);
  font: inherit;
  font-size: 0.74rem;
  cursor: pointer;
}
.cg-ask button:hover { border-color: var(--accent, #007d6c); color: var(--accent, #007d6c); }
.cg-ask .cg-clear { border: 0; text-decoration: underline; text-underline-offset: 2px; }
</style>
