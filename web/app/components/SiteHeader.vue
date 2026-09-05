<script setup lang="ts">
type Section = "story" | "explore" | "graph" | "data" | "about";
type Destination = "home" | "story" | "explore";

const props = defineProps<{
  current?: Section;
  onGo?: ((to: Destination) => void) | null;
}>();

const mainItems = [
  { key: "story", label: "Story", href: "/" },
  { key: "explore", label: "Ask", href: "/#chat" },
  { key: "graph", label: "Graph", href: "/graph" },
  { key: "data", label: "Data", href: "/data" },
  { key: "about", label: "About", href: "/about" },
] as const;

function handle(event: MouseEvent, key: Section | "home") {
  if (!props.onGo || key === "about" || key === "data" || key === "graph") return;
  if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) return;
  event.preventDefault();
  props.onGo(key);
}
</script>

<template>
  <header class="site-header">
    <div class="site-header__left">
      <a class="site-wordmark" href="/" aria-label="EQ-Graph home" @click="handle($event, 'home')">
        EQ<span aria-hidden="true">-</span>GRAPH
      </a>
    </div>

    <nav class="site-nav" aria-label="Main navigation">
      <a
        v-for="item in mainItems"
        :key="item.key"
        :href="item.href"
        :class="['site-nav__link', current === item.key && 'is-current']"
        :aria-current="current === item.key ? 'page' : undefined"
        @click="handle($event, item.key)"
      >{{ item.label }}</a>
    </nav>
  </header>
</template>

<style scoped>
.site-header {
  --site-header-pad: var(--pad, 3rem);
  position: fixed;
  inset: 0 0 auto;
  z-index: 30;
  height: 4.8rem;
  padding: 0 var(--site-header-pad);
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 2rem;
  pointer-events: none;
}
.site-header::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(to bottom, var(--surface, var(--paper, #fcfcfb)) 0 68%, transparent 100%);
}
.site-header__left,
.site-nav { pointer-events: auto; }
.site-header__left {
  min-width: 0;
  display: flex;
  align-items: center;
  gap: clamp(1rem, 2vw, 1.55rem);
}
.site-wordmark {
  min-height: 48px;
  display: inline-flex;
  align-items: center;
  color: var(--ink, var(--ink-1, #1a1a17));
  font: 600 1.02rem/1 var(--font-display, "Instrument Sans", sans-serif);
  letter-spacing: -.045em;
  text-decoration: none;
  white-space: nowrap;
}
.site-wordmark span {
  margin: 0 .09em;
  color: var(--teal, var(--accent, #007d6c));
  font-weight: 600;
  transform: scaleX(1.55);
}
.site-nav {
  display: flex;
  align-items: center;
  gap: clamp(1.1rem, 2vw, 1.45rem);
}
.site-nav__link {
  position: relative;
  min-height: 48px;
  display: inline-flex;
  align-items: center;
  color: var(--ink, var(--ink-1, #1a1a17));
  font: 600 .92rem/1 var(--font-body, "Instrument Sans", sans-serif);
  text-decoration: none;
  transition: color .15s ease;
}
.site-nav__link::after {
  content: "";
  position: absolute;
  top: calc(50% + .7rem);
  right: 0;
  left: 0;
  height: 1px;
  background: currentColor;
  opacity: 0;
  transform: scaleX(.4);
  transition: opacity .15s ease, transform .15s ease;
}
.site-wordmark:hover,
.site-nav__link:hover { color: var(--teal, var(--accent, #007d6c)); }
.site-nav__link.is-current {
  color: var(--teal, var(--accent, #007d6c));
}
.site-nav__link.is-current::after {
  opacity: 1;
  transform: scaleX(1);
}
.site-wordmark:focus-visible,
.site-nav__link:focus-visible {
  outline: 2px solid var(--teal, var(--accent, #007d6c));
  outline-offset: 2px;
  border-radius: 2px;
}

@media (max-width: 900px) {
  .site-header { --site-header-pad: var(--pad, 1.5rem); }
}
@media (max-width: 560px) {
  .site-header { --site-header-pad: 1rem; height: 4.2rem; gap: .75rem; }
  .site-header__left { gap: .7rem; }
  .site-wordmark { min-height: 44px; font-size: .88rem; }
  .site-nav { gap: .75rem; }
  .site-nav__link { min-height: 44px; font-size: .76rem; }
}
</style>
