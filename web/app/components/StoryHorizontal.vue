<script setup lang="ts">
import type { DemoGraphData } from "../../shared/types/demo";

const props = withDefaults(defineProps<{ active?: boolean }>(), {
  active: true,
});
const emit = defineEmits<{
  "enter-chat": [entry: { source: "skip" | "cta" | "story"; returnY: number; question?: string }];
}>();

const rootEl = ref<HTMLElement | null>(null);
let globe: { destroy?: () => void; setActive?: (active: boolean) => void; clearSelection?: () => void } | undefined;

/* The country card.  */
type CountryFacts = {
  name: string;
  studies: number;
  topInstrument?: string | null;
  anchor?: { x: number; y: number };
};
const picked = ref<CountryFacts | null>(null);
const countryPlacement = computed(() => {
  if (!picked.value?.anchor || !import.meta.client || window.innerWidth <= 640) return {};
  const cardWidth = 272;
  const cardHeight = 184;
  const gap = 18;
  const margin = 16;
  const { x, y } = picked.value.anchor;
  const placeLeft = x + gap + cardWidth > window.innerWidth - margin;
  const left = placeLeft ? x - cardWidth - gap : x + gap;
  const top = Math.max(72, Math.min(window.innerHeight - cardHeight - 64, y - cardHeight / 2));
  return {
    "--country-left": `${Math.max(margin, left)}px`,
    "--country-top": `${top}px`,
    "--country-pin-y": `${Math.max(20, Math.min(cardHeight - 20, y - top))}px`,
    "--country-side": placeLeft ? "left" : "right",
  };
});
const ready = ref(false);
const settled = ref(false);
const loadError = ref(false);
let story: { destroy?: () => void; refresh?: () => void; jumpToExplorer?: () => void } | undefined;
let disposed = false;

function enterDirect(source: "skip" | "cta", question?: string) {
  emit("enter-chat", { source, returnY: window.scrollY, question });
}

function skipTour() {
  const root = rootEl.value as (HTMLElement & { __story?: any }) | null;
  root?.__story?.jumpToExplorer?.();
}

function dismissCountry() {
  picked.value = null;
  globe?.clearSelection?.();
}

/* One fold forward or back.  */
function step(delta: number) {
  const root = rootEl.value as (HTMLElement & { __story?: any }) | null;
  const story = root?.__story;
  if (!story) return;
  const at = story.currentBeat?.() ?? 0;
  story.goToBeat(at + delta);
}

/* Story and Ask are views of this page, so the header switches modes without losing the scroll position. */
/* The mark goes to the opening screen from wherever the reader is.  */
function goHome() {
  const root = rootEl.value as (HTMLElement & { __story?: any }) | null;
  root?.__story?.goHome();
}

function goSection(to: "home" | "story" | "explore") {
  if (to === "home" || to === "story") { goHome(); return; }
  if (to === "explore") { enterDirect("skip"); return; }
}

async function initialise() {
  const root = rootEl.value as (HTMLElement & { __story?: any }) | null;
  if (!root) return;

  loadError.value = false;
  settled.value = false;
  ready.value = false;
  try {
    const [{ initStory }, { initGlobe }, data, topo] = await Promise.all([
      import("../lib/storyHorizontal.js"),
      import("../lib/globe.js"),
      $fetch<DemoGraphData>("/api/graph"),
      $fetch<Record<string, any>>("/data/countries-50m.json"),
    ]);
    if (disposed || !root.isConnected) return;

    story?.destroy?.();
    globe?.destroy?.();
    story = initStory(data, topo, root, {
      coauthors: data.live.coauthorship,
      cites: data.live.citations,
      onEnterChat: (entry: { returnY: number; question?: string }) => {
        emit("enter-chat", { source: "story", returnY: entry.returnY, question: entry.question });
      },
    });

    root.querySelectorAll<HTMLButtonElement>("[data-go]").forEach((button) => {
      button.onclick = () => {
        if (button.dataset.go === "story") {
          root.__story?.goToBeat(0);
          return;
        }
        if (button.dataset.go === "preview") {
          root.__story?.jumpToExplorer?.();
          return;
        }
        enterDirect("cta");
      };
    });

    const canvas = root.querySelector<HTMLCanvasElement>("[data-inst-canvas]");
    if (!canvas) throw new Error("The globe canvas is not available.");
    canvas.parentElement?.classList.add("is-globe");
    globe = initGlobe(canvas, data, topo, {
      onSelect: (facts: CountryFacts | null) => { picked.value = facts; },
    });
    globe.setActive?.(props.active);

    settled.value = true;
    setTimeout(() => { if (!disposed) ready.value = true; }, 450);
  } catch (error) {
    console.error("The research story did not load.", error);
    loadError.value = true;
  }
}

onMounted(initialise);

watch(
  () => props.active,
  async (active) => {
    if (!active) {
      globe?.setActive?.(false);
      return;
    }
    await nextTick();
    globe?.setActive?.(true);
    story?.refresh?.();
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

defineExpose({ goHome, restoreAt });

/* Anything opened by a click is temporary and closes when the reader moves on.  */
function dismissOnScroll() {
  if (picked.value) dismissCountry();
}
onMounted(() => window.addEventListener("scroll", dismissOnScroll, { passive: true }));

onBeforeUnmount(() => {
  window.removeEventListener("scroll", dismissOnScroll);
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
    <SiteHeader current="story" :on-go="goSection" />

    <div class="sh-scroll" data-scroll>
      <!-- Sits inside the pinned stage so it covers the story and nothing else, and fades rather than cutting, so the arrival is not its own jolt. -->
      <div v-if="!ready" :class="['sh-loading', settled && !loadError && 'is-done']">
        <div v-if="loadError" class="sh-load-error" role="alert">
          <p>The research map did not load.</p>
          <button type="button" @click="initialise">Try again</button>
        </div>
        <BrandLoader v-else label="Loading the research map" />
      </div>

      <div class="sh-stage" data-stage>
        <h1 class="sr-only">A knowledge graph of EuroQol-funded research.</h1>
        <p class="sr-only">A research knowledge graph connecting funded projects to publications, researchers, measures, methods, and findings.</p>

        <div class="sh-glow" data-glow aria-hidden="true"><i class="a" /><i class="b" /></div>

        <!-- Step, then skip.  -->
        <div class="sh-controls">
          <div class="sh-step">
            <button type="button" @click="step(-1)" aria-label="Previous fold">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" /></svg>
            </button>
            <button type="button" @click="step(1)" aria-label="Next fold">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" /></svg>
            </button>
          </div>
          <button type="button" class="sh-skip" @click="skipTour">
            Skip Tour <span aria-hidden="true">→</span>
          </button>
        </div>

        <div class="sh-grid" aria-hidden="true">
          <span v-for="n in 12" :key="n" />
        </div>

        <div class="sh-instrument" data-instrument aria-hidden="true">
          <canvas data-inst-canvas />
        </div>

        <!-- The globe stays simple. A click adds only two facts. -->
        <transition name="sh-card">
          <aside
            v-if="picked"
            :class="['sh-country', countryPlacement['--country-side'] === 'left' ? 'is-left' : 'is-right']"
            :style="countryPlacement"
            role="group"
            :aria-label="picked.name"
          >
            <button type="button" class="sh-country-x" aria-label="Close" @click="dismissCountry">×</button>
            <h3>{{ picked.name }}</h3>
            <dl>
              <div><dt>{{ picked.studies.toLocaleString('en') }}</dt><dd>studies linked to this country</dd></div>
              <div v-if="picked.topInstrument"><dt>{{ picked.topInstrument }}</dt><dd>most used measure</dd></div>
            </dl>
          </aside>
        </transition>

        <div class="sh-field" aria-hidden="true"><canvas data-canvas /></div>
        <div class="sh-charts" data-charts />
        <output class="sh-data-tip" data-data-tip hidden />

        <p class="sh-hero-kicker" data-hero-kicker>EQ–GRAPH / RESEARCH KNOWLEDGE GRAPH</p>
        <p class="sh-sub" data-sub>
          Projects, publications, people, and findings, linked and ready to&nbsp;query.
        </p>
        <p class="sh-scope" data-scope>1,024 funded projects | 797 publications</p>

        <div class="sh-cta" data-cta>
          <button class="sh-btn is-primary" data-go="story">
            <i class="sh-ray" aria-hidden="true"><b /></i>
            <span>Start</span>
          </button>
          <button class="sh-tour-link" data-go="preview">Ask a question</button>
          <a class="sh-tour-link" href="/graph">Explore the graph</a>
        </div>

        <div class="sh-dots" data-dots />
      </div>

      <div class="sh-steps" data-steps />
    </div>
  </div>
</template>
