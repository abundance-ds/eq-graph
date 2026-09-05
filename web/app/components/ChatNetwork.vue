<script setup lang="ts">
import { nextTick, onBeforeUnmount, onMounted, shallowRef } from "vue";
import type { ChatWidgetSpec } from "../types/chat";
import { numeric } from "../viz/format";
import { CHART_RAMP } from "../viz/theme";

const props = defineProps<{ spec: ChatWidgetSpec }>();

type NetworkNode = {
  id: string;
  label: string;
  weight: number;
  degree: number;
  x: number;
  y: number;
  r: number;
  named: boolean;
  labelSide: "left" | "right" | "below";
  color: string;
};

type NetworkLink = {
  id: string;
  source: string;
  target: string;
  weight: number;
  width: number;
};

const host = shallowRef<HTMLElement | null>(null);
const width = ref(0);
const focused = ref<string | null>(null);
let observer: ResizeObserver | undefined;

const height = computed(() => width.value && width.value < 520 ? 250 : 310);
const picked = computed(() => new Set(focused.value ? [focused.value] : []));

function label(value: unknown): string {
  return String(value ?? "").trim();
}

function hash(value: string): number {
  let output = 2166136261;
  for (let index = 0; index < value.length; index += 1) {
    output ^= value.charCodeAt(index);
    output = Math.imul(output, 16777619);
  }
  return output >>> 0;
}

const model = computed(() => {
  const sourceKey = props.spec.encoding.source;
  const targetKey = props.spec.encoding.target;
  const weightKey = props.spec.encoding.weight;
  const canvasWidth = Math.max(300, width.value || 680);
  const canvasHeight = height.value;
  if (!sourceKey || !targetKey) return { nodes: [] as NetworkNode[], links: [] as NetworkLink[] };

  const merged = new Map<string, NetworkLink>();
  for (const row of props.spec.rows) {
    const source = label(row[sourceKey]);
    const target = label(row[targetKey]);
    if (!source || !target || source === target) continue;
    const weight = weightKey ? Math.max(0, numeric(row[weightKey]) ?? 0) : 1;
    const [left, right] = source.localeCompare(target) <= 0 ? [source, target] : [target, source];
    const id = `${left}\u001f${right}`;
    const found = merged.get(id);
    if (found) found.weight += weight;
    else merged.set(id, { id, source: left, target: right, weight, width: 1 });
  }

  const links = [...merged.values()];
  const nodeMap = new Map<string, NetworkNode>();
  for (const link of links) {
    for (const nodeLabel of [link.source, link.target]) {
      if (!nodeMap.has(nodeLabel)) {
        nodeMap.set(nodeLabel, {
          id: nodeLabel,
          label: nodeLabel,
          weight: 0,
          degree: 0,
          x: 0,
          y: 0,
          r: 6,
          named: false,
          labelSide: "below",
          color: CHART_RAMP[2]!,
        });
      }
      const node = nodeMap.get(nodeLabel)!;
      node.weight += link.weight;
      node.degree += 1;
    }
  }

  const nodes = [...nodeMap.values()].sort((a, b) => a.label.localeCompare(b.label));
  const byId = new Map(nodes.map((node) => [node.id, node]));
  const maxNodeWeight = Math.max(1, ...nodes.map((node) => node.weight));
  const maxLinkWeight = Math.max(1, ...links.map((link) => link.weight));
  const span = Math.min(canvasWidth, canvasHeight);
  const centerX = canvasWidth / 2;
  const centerY = (canvasHeight - 20) / 2;

  for (const node of nodes) {
    const amount = Math.sqrt(node.weight / maxNodeWeight);
    node.r = 5.5 + amount * 9.5;
    node.color = CHART_RAMP[Math.min(CHART_RAMP.length - 1, 1 + Math.floor(amount * 4))]!;
    const seed = hash(node.label) / 0xffffffff;
    const angle = seed * Math.PI * 2;
    const radius = span * (.12 + (hash(`${node.label}:radius`) % 1000) / 1000 * .22);
    node.x = centerX + Math.cos(angle) * radius;
    node.y = centerY + Math.sin(angle) * radius;
  }

  const velocity = new Map(nodes.map((node) => [node.id, { x: 0, y: 0 }]));
  for (let step = 0; step < 220; step += 1) {
    const cool = 1 - step / 250;
    for (let aIndex = 0; aIndex < nodes.length; aIndex += 1) {
      const a = nodes[aIndex]!;
      const aVelocity = velocity.get(a.id)!;
      for (let bIndex = aIndex + 1; bIndex < nodes.length; bIndex += 1) {
        const b = nodes[bIndex]!;
        const bVelocity = velocity.get(b.id)!;
        let dx = b.x - a.x;
        let dy = b.y - a.y;
        const distance = Math.max(1, Math.hypot(dx, dy));
        dx /= distance;
        dy /= distance;
        const charge = Math.min(2.2, (1350 / (distance * distance)) * cool);
        aVelocity.x -= dx * charge;
        aVelocity.y -= dy * charge;
        bVelocity.x += dx * charge;
        bVelocity.y += dy * charge;
        const minimum = a.r + b.r + 7;
        if (distance < minimum) {
          const push = (minimum - distance) * .16;
          aVelocity.x -= dx * push;
          aVelocity.y -= dy * push;
          bVelocity.x += dx * push;
          bVelocity.y += dy * push;
        }
      }
      aVelocity.x += (centerX - a.x) * .0018 * cool;
      aVelocity.y += (centerY - a.y) * .0018 * cool;
    }

    for (const link of links) {
      const source = byId.get(link.source)!;
      const target = byId.get(link.target)!;
      const sourceVelocity = velocity.get(source.id)!;
      const targetVelocity = velocity.get(target.id)!;
      let dx = target.x - source.x;
      let dy = target.y - source.y;
      const distance = Math.max(1, Math.hypot(dx, dy));
      dx /= distance;
      dy /= distance;
      const strength = Math.sqrt(link.weight / maxLinkWeight);
      const rest = span * (.28 - strength * .12);
      const force = (distance - rest) * (.009 + strength * .012) * cool;
      sourceVelocity.x += dx * force;
      sourceVelocity.y += dy * force;
      targetVelocity.x -= dx * force;
      targetVelocity.y -= dy * force;
    }

    for (const node of nodes) {
      const speed = velocity.get(node.id)!;
      node.x += speed.x;
      node.y += speed.y;
      speed.x *= .72;
      speed.y *= .72;
    }
  }

  if (nodes.length) {
    const minX = Math.min(...nodes.map((node) => node.x - node.r));
    const maxX = Math.max(...nodes.map((node) => node.x + node.r));
    const minY = Math.min(...nodes.map((node) => node.y - node.r));
    const maxY = Math.max(...nodes.map((node) => node.y + node.r));
    const padX = Math.min(58, canvasWidth * .12);
    const padY = 24;
    const scale = Math.min(
      (canvasWidth - padX * 2) / Math.max(1, maxX - minX),
      (canvasHeight - padY * 2 - 20) / Math.max(1, maxY - minY),
      1.7,
    );
    for (const node of nodes) {
      node.x = padX + (node.x - minX) * scale;
      node.y = padY + (node.y - minY) * scale;
      node.r = Math.max(5.5, node.r * Math.min(scale, 1.15));
    }
  }

  const named = new Set(
    [...nodes]
      .sort((a, b) => b.weight - a.weight || b.degree - a.degree || a.label.localeCompare(b.label))
      .slice(0, canvasWidth < 520 ? 7 : 11)
      .map((node) => node.id),
  );
  for (const node of nodes) {
    node.named = named.has(node.id) || picked.value.has(node.id);
    node.labelSide = node.x < canvasWidth * .32 ? "right" : node.x > canvasWidth * .68 ? "left" : "below";
  }
  for (const link of links) {
    link.width = .65 + Math.sqrt(link.weight / maxLinkWeight) * 2.7;
  }

  return { nodes, links };
});

const neighbors = computed(() => {
  const output = new Set<string>();
  for (const link of model.value.links) {
    if (picked.value.has(link.source)) output.add(link.target);
    if (picked.value.has(link.target)) output.add(link.source);
  }
  return output;
});

function nodeClass(node: NetworkNode) {
  return {
    "is-picked": picked.value.has(node.id),
    "is-neighbor": neighbors.value.has(node.id),
    "is-dim": picked.value.size > 0 && !picked.value.has(node.id) && !neighbors.value.has(node.id),
  };
}

function linkClass(link: NetworkLink) {
  const active = picked.value.has(link.source) || picked.value.has(link.target);
  return { "is-active": active, "is-dim": picked.value.size > 0 && !active };
}

function choose(node: NetworkNode) {
  focused.value = focused.value === node.id ? null : node.id;
}

onMounted(async () => {
  await nextTick();
  if (!host.value) return;
  observer = new ResizeObserver(([entry]) => {
    width.value = Math.round(entry?.contentRect.width ?? 0);
  });
  observer.observe(host.value);
});

onBeforeUnmount(() => observer?.disconnect());
</script>

<template>
  <div ref="host" class="network">
    <div
      class="network__canvas"
      :style="{ height: `${height}px` }"
      role="group"
      :aria-label="`${spec.title}. ${model.nodes.length} nodes and ${model.links.length} links.`"
    >
      <svg
        class="network__links"
        :viewBox="`0 0 ${Math.max(300, width || 680)} ${height}`"
        preserveAspectRatio="none"
        aria-hidden="true"
      >
        <line
          v-for="link in model.links"
          :key="link.id"
          :class="linkClass(link)"
          :x1="model.nodes.find((node) => node.id === link.source)?.x"
          :y1="model.nodes.find((node) => node.id === link.source)?.y"
          :x2="model.nodes.find((node) => node.id === link.target)?.x"
          :y2="model.nodes.find((node) => node.id === link.target)?.y"
          :style="{ strokeWidth: link.width }"
        />
      </svg>

      <button
        v-for="node in model.nodes"
        :key="node.id"
        type="button"
        :class="['network__node', nodeClass(node)]"
        :style="{ left: `${node.x}px`, top: `${node.y}px` }"
        :aria-pressed="picked.has(node.id)"
        :aria-label="`${node.label}: total connection weight ${node.weight}, ${node.degree} ${node.degree === 1 ? 'link' : 'links'}`"
        @click="choose(node)"
      >
        <i
          :style="{ width: `${node.r * 2}px`, height: `${node.r * 2}px`, backgroundColor: node.color }"
          aria-hidden="true"
        />
        <span v-if="node.named" :class="`is-${node.labelSide}`">{{ node.label }}</span>
      </button>
    </div>

    <div class="network__key" aria-hidden="true">
      <span><i class="is-node" />Node size · total link weight</span>
      <span><i class="is-link" />Line width · link weight</span>
    </div>
  </div>
</template>

<style scoped>
.network { width: 100%; }
.network__canvas {
  position: relative;
  width: 100%;
  overflow: hidden;
  border-block: 1px solid var(--hairline, #e5e4df);
  background:
    radial-gradient(circle at center, color-mix(in srgb, var(--accent, #007d6c) 4%, transparent), transparent 62%);
}
.network__links { position: absolute; inset: 0; width: 100%; height: 100%; overflow: visible; }
.network__links line {
  stroke: var(--accent, #007d6c);
  stroke-linecap: round;
  stroke-opacity: .21;
  vector-effect: non-scaling-stroke;
  transition: stroke-opacity .18s ease;
}
.network__links line.is-active { stroke-opacity: .7; }
.network__links line.is-dim { stroke-opacity: .035; }
.network__node {
  position: absolute;
  z-index: 1;
  display: grid;
  width: 34px;
  height: 34px;
  padding: 0;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--ink-2, #5c5c56);
  font: inherit;
  cursor: pointer;
  place-items: center;
  transform: translate(-50%, -50%);
  transition: opacity .18s ease, transform .18s ease;
}
.network__node i {
  display: block;
  border: 1px solid color-mix(in srgb, var(--ink-1, #1a1a17) 22%, transparent);
  border-radius: 50%;
  box-shadow: 0 0 0 2px color-mix(in srgb, var(--surface, #fff) 78%, transparent);
  transition: box-shadow .18s ease, transform .18s ease;
}
.network__node:hover,
.network__node:focus-visible,
.network__node.is-picked { z-index: 3; }
.network__node:hover i,
.network__node:focus-visible i { transform: scale(1.16); }
.network__node.is-picked i {
  box-shadow: 0 0 0 3px var(--surface, #fff), 0 0 0 5px var(--accent, #007d6c);
}
.network__node.is-neighbor i { box-shadow: 0 0 0 2px var(--surface, #fff), 0 0 0 3px var(--accent, #007d6c); }
.network__node.is-dim { opacity: .18; }
.network__node:focus-visible { outline: 2px solid var(--accent, #007d6c); outline-offset: 2px; }
.network__node span {
  position: absolute;
  max-width: 10rem;
  padding: .12rem .28rem;
  border-radius: 2px;
  background: color-mix(in srgb, var(--surface, #fff) 92%, transparent);
  color: var(--ink-1, #1a1a17);
  font-size: .68rem;
  font-weight: 520;
  line-height: 1.2;
  overflow: hidden;
  pointer-events: none;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.network__node span.is-right { left: calc(50% + 14px); top: 50%; transform: translateY(-50%); }
.network__node span.is-left { right: calc(50% + 14px); top: 50%; transform: translateY(-50%); }
.network__node span.is-below { left: 50%; top: calc(50% + 13px); transform: translateX(-50%); }
.network__key {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem 1rem;
  padding-top: .45rem;
  color: var(--ink-3, #8e8e86);
  font: .65rem var(--font-num, ui-monospace, monospace);
}
.network__key span { display: inline-flex; align-items: center; gap: .35rem; }
.network__key i { display: inline-block; flex: none; }
.network__key .is-node { width: .55rem; height: .55rem; border-radius: 50%; background: var(--accent, #007d6c); }
.network__key .is-link { width: .8rem; height: 2px; border-radius: 2px; background: var(--accent, #007d6c); }

@media (max-width: 520px) {
  .network__node span { max-width: 7.5rem; font-size: .64rem; }
  .network__key { gap: .3rem .75rem; }
}

@media (prefers-reduced-motion: reduce) {
  .network__links line,
  .network__node,
  .network__node i { transition: none; }
}
</style>
