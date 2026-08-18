<script setup lang="ts">
import type { DemoGraphData } from "../../shared/types/demo";

const props = withDefaults(defineProps<{ active?: boolean }>(), { active: true });
const emit = defineEmits<{
  "enter-chat": [entry: { source: "skip" | "cta" | "story"; returnY: number }];
}>();

const rootEl = ref<HTMLElement | null>(null);
let globe: { destroy?: () => void; setActive?: (active: boolean) => void } | undefined;
let story: { destroy?: () => void; refresh?: () => void } | undefined;
let disposed = false;

function enterDirect(source: "skip" | "cta") {
  emit("enter-chat", { source, returnY: window.scrollY });
}

onMounted(async () => {
  const root = rootEl.value as (HTMLElement & { __story?: any }) | null;
  if (!root) return;

  const [{ initStory }, { initGlobe }, data, topo] = await Promise.all([
    import("../lib/storyHorizontal.js"),
    import("../lib/globe.js"),
    $fetch<DemoGraphData>("/api/graph"),
    $fetch<Record<string, any>>("/data/countries-50m.json"),
  ]);
  if (disposed || !root.isConnected) return;

  story = initStory(data, topo, root, {
    onEnterChat: (entry: { returnY: number }) => {
      emit("enter-chat", { source: "story", returnY: entry.returnY });
    },
  });

  root.querySelectorAll<HTMLButtonElement>("[data-go]").forEach((button) => {
    button.onclick = () => {
      if (button.dataset.go === "impact") {
        root.__story?.goToBeat(0);
        return;
      }
      enterDirect("cta");
    };
  });

  const canvas = root.querySelector<HTMLCanvasElement>("[data-inst-canvas]");
  if (!canvas) return;
  canvas.parentElement?.classList.add("is-globe");
  globe = initGlobe(canvas, data, topo);
  globe.setActive?.(props.active);

  const facts = (globe as any).facts();
  const key = root.querySelector<HTMLElement>("[data-key-body]");
  if (key) {
    key.innerHTML =
      `<b>Research locations represented — ${facts.countries}.</b>`
      + ` A country lights in proportion to its study count. `
      + `${facts.top?.[0]} is brightest with ${facts.top?.[1]} studies.`;
  }

  const keyButton = root.querySelector<HTMLButtonElement>("[data-key-toggle]");
  if (keyButton && key) {
    keyButton.onclick = () => {
      const open = key.hasAttribute("hidden");
      key.toggleAttribute("hidden", !open);
      keyButton.setAttribute("aria-expanded", String(open));
    };
  }
});

watch(
  () => props.active,
  async (active) => {
    globe?.setActive?.(active);
    if (active) {
      await nextTick();
      story?.refresh?.();
    }
  },
);

async function restoreAt(top: number) {
  await nextTick();
  window.scrollTo(0, Math.max(0, top));
  story?.refresh?.();
  globe?.setActive?.(true);
  await nextTick();
  rootEl.value?.querySelector<HTMLButtonElement>("[data-dots] button[aria-current='step']")?.focus({ preventScroll: true });
}

defineExpose({ restoreAt });

onBeforeUnmount(() => {
  disposed = true;
  story?.destroy?.();
  globe?.destroy?.();
});
</script>

<template>
  <div
    ref="rootEl"
    class="sh-root"
    :aria-hidden="active ? undefined : 'true'"
    :inert="!active"
  >
    <div class="sh-scroll" data-scroll>
      <div class="sh-stage" data-stage>
        <h1 class="sr-only">Shaping how the world measures health.</h1>
        <p class="sr-only">Explore EuroQol studies, instruments, methods, populations, findings, and research gaps.</p>

        <div class="sh-glow" data-glow aria-hidden="true"><i class="a" /><i class="b" /></div>

        <img class="sh-logo" src="/brand/euroqol-logo.svg" alt="EuroQol" width="300" height="49">

        <button type="button" class="sh-skip" @click="enterDirect('skip')">
          Skip story <span aria-hidden="true">→</span>
        </button>

        <div class="sh-grid" aria-hidden="true">
          <span v-for="n in 12" :key="n" />
        </div>

        <div class="sh-instrument" data-instrument aria-hidden="true">
          <canvas data-inst-canvas />
        </div>

        <div class="sh-key" data-key>
          <button class="sh-key-toggle" data-key-toggle aria-expanded="false">Key</button>
          <p class="sh-key-body" data-key-body hidden />
        </div>

        <div class="sh-field" aria-hidden="true"><canvas data-canvas /></div>

        <div class="sh-cta" data-cta>
          <button class="sh-btn is-primary" data-go="chat">
            <i class="sh-ray" aria-hidden="true"><b /></i>
            <span>Explore studies</span>
          </button>
          <button class="sh-btn is-secondary" data-go="impact">
            <i class="sh-ray" aria-hidden="true"><b /></i>
            <span>View impact</span>
          </button>
        </div>

        <div class="sh-track" data-track />

        <div class="sh-frame" aria-hidden="true">
          <span class="rule-t" />
          <span class="rule-b" />
        </div>

        <div class="sh-dots" data-dots />
      </div>
    </div>
  </div>
</template>
