<script setup lang="ts">
import type { DemoGraphData } from "../../shared/types/demo";

const props = withDefaults(defineProps<{ active?: boolean }>(), { active: true });
const emit = defineEmits<{
  "enter-chat": [entry: { source: "skip" | "cta" | "story"; returnY: number }];
}>();

const rootEl = ref<HTMLElement | null>(null);
let globe: { destroy?: () => void; setActive?: (active: boolean) => void } | undefined;

/* The country card. The globe reports what was clicked; this holds it, so the
   card can be a real element — focusable, closable, and styled with the rest
   of the page rather than drawn into the canvas. */
type CountryFacts = {
  name: string; projects: number; studies: number; findings: number;
  family?: { short: string; has: boolean }[] | null;
};
const picked = ref<CountryFacts | null>(null);
let story: { destroy?: () => void; refresh?: () => void } | undefined;
let disposed = false;

function enterDirect(source: "skip" | "cta") {
  emit("enter-chat", { source, returnY: window.scrollY });
}

/* One fold forward or back. It reads the beat the story is actually on rather
   than counting clicks, so the arrows stay right however the reader got here —
   by scrolling, by a dot, or by an arrow. */
function step(delta: number) {
  const root = rootEl.value as (HTMLElement & { __story?: any }) | null;
  const story = root?.__story;
  if (!story) return;
  const at = story.currentBeat?.() ?? 0;
  story.goToBeat(at + delta);
}

/* Impact and Research explorer are views of this page, not other pages, so the
   nav asks us to switch rather than navigating away and losing the scroll. */
function goSection(to: "impact" | "explore") {
  if (to === "explore") { enterDirect("cta"); return; }
  const root = rootEl.value as (HTMLElement & { __story?: any }) | null;
  root?.__story?.goToBeat(0);
}

onMounted(async () => {
  const root = rootEl.value as (HTMLElement & { __story?: any }) | null;
  if (!root) return;

  const [{ initStory }, { initGlobe }, data, topo, coauthors] = await Promise.all([
    import("../lib/storyHorizontal.js"),
    import("../lib/globe.js"),
    $fetch<DemoGraphData>("/api/graph"),
    $fetch<Record<string, any>>("/data/countries-50m.json"),
    // The co-authorship network is a separate artefact from Paul's pipeline,
    // not part of the research graph, so it loads on its own.
    $fetch<Record<string, any>>("/data/coauthorship.json").catch(() => null),
  ]);
  if (disposed || !root.isConnected) return;

  story = initStory(data, topo, root, {
    coauthors,
    onEnterChat: (entry: { returnY: number }) => {
      emit("enter-chat", { source: "story", returnY: entry.returnY });
    },
    // The map beat reports the country under a click; the card is the same one
    // the globe used, so a reader meets one object however they got to it.
    onSelectCountry: (facts: CountryFacts | null) => { picked.value = facts; },
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
  globe = initGlobe(canvas, data, topo, {
    onSelect: (facts: CountryFacts | null) => { picked.value = facts; },
  });
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

/* Anything opened by a click is temporary and closes when the reader moves on.
   The card is pinned to a country on a map that scrolls away underneath it, so
   left open it ends up floating over a different fold entirely. */
function dismissOnScroll() {
  if (picked.value) picked.value = null;
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
    <div class="sh-scroll" data-scroll>
      <div class="sh-stage" data-stage>
        <h1 class="sr-only">Shaping how the world measures health.</h1>
        <p class="sr-only">Explore EuroQol studies, instruments, methods, populations, findings, and research gaps.</p>

        <div class="sh-glow" data-glow aria-hidden="true"><i class="a" /><i class="b" /></div>

        <img class="sh-logo" src="/brand/euroqol-logo.svg" alt="EuroQol" width="300" height="49">

        <SiteNav current="impact" :on-go="goSection" />

        <!-- Step, then skip. The arrows move one fold at a time and Skip leaves
             the story altogether, so the smaller action sits first and the one
             that ends things sits last. No labels on the arrows: a left and a
             right chevron beside a row of fold dots need no explaining. -->
        <div class="sh-controls">
          <div class="sh-step">
            <button type="button" @click="step(-1)" aria-label="Previous fold">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" /></svg>
            </button>
            <button type="button" @click="step(1)" aria-label="Next fold">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" /></svg>
            </button>
          </div>
          <button type="button" class="sh-skip" @click="enterDirect('skip')">
            Skip impact <span aria-hidden="true">→</span>
          </button>
        </div>

        <div class="sh-grid" aria-hidden="true">
          <span v-for="n in 12" :key="n" />
        </div>

        <div class="sh-instrument" data-instrument aria-hidden="true">
          <canvas data-inst-canvas />
        </div>

        <!-- Click a country, and its three numbers arrive here. Projects and
             studies are deliberately both shown: the distance between them is
             how much of the funded work has actually been read.

             A sibling of the globe, not a child of it. Inside, it inherited the
             container's opacity, which the story drives to 0 as soon as it
             starts, so a click on the map fold set the country but the card was
             invisible. It also inherited pointer-events:none, which killed its
             own close button. -->
        <transition name="sh-card">
          <aside v-if="picked" class="sh-country" role="dialog" :aria-label="picked.name">
            <button type="button" class="sh-country-x" aria-label="Close" @click="picked = null">×</button>
            <h3>{{ picked.name }}</h3>
            <dl>
              <div><dt>{{ picked.projects.toLocaleString('en') }}</dt><dd>projects funded</dd></div>
              <div><dt>{{ picked.studies.toLocaleString('en') }}</dt><dd>studies read</dd></div>
              <div><dt>{{ picked.findings.toLocaleString('en') }}</dt><dd>findings extracted</dd></div>
            </dl>
            <!-- Which of the five have actually been used here. A version with
                 no study is shown greyed rather than dropped: the absence is
                 the useful half of the answer. -->
            <ul v-if="picked.family" class="sh-family">
              <li v-for="f in picked.family" :key="f.short" :class="f.has && 'is-on'">
                <i aria-hidden="true" />{{ f.short }}
              </li>
            </ul>
          </aside>
        </transition>

        <div class="sh-key" data-key>
          <button class="sh-key-toggle" data-key-toggle aria-expanded="false">Key</button>
          <p class="sh-key-body" data-key-body hidden />
        </div>

        <div class="sh-field" aria-hidden="true"><canvas data-canvas /></div>
        <div class="sh-charts" data-charts aria-hidden="true" />

        <div class="sh-cta" data-cta>
          <button class="sh-btn is-primary" data-go="chat">
            <i class="sh-ray" aria-hidden="true"><b /></i>
            <span>Explore research</span>
          </button>
          <button class="sh-btn is-secondary" data-go="impact">
            <i class="sh-ray" aria-hidden="true"><b /></i>
            <span>View impact</span>
          </button>
        </div>

        <div class="sh-track" data-track />

        <!-- Both frame rules are gone. They ran the full width and underlined
             nothing: the fold is already bounded by its own edges. -->

        <div class="sh-dots" data-dots />
      </div>
    </div>
  </div>
</template>
