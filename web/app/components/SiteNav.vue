<script setup lang="ts">
/**
 * The three places this site goes, in the same corner on every screen.
 *
 * Impact and Research explorer are two views of one page rather than two
 * routes, so from the story they are handled in place and from anywhere else
 * they are ordinary links that the page reads on arrival. Either way the reader
 * meets the same three words in the same position, which is the point.
 */
const props = defineProps<{
  /** 'impact' | 'explore' | 'about' — the one you are already on. */
  current?: string;
  /** Present on the story page, where these are views and not navigations. */
  onGo?: ((to: "impact" | "explore") => void) | null;
}>();

const items = [
  { key: "impact",  label: "Impact",            href: "/" },
  { key: "explore", label: "Research explorer", href: "/#chat" },
  { key: "about",   label: "About",             href: "/about" },
];

function handle(event: MouseEvent, key: string) {
  // Only intercept what this page can do without a navigation.
  if (!props.onGo || key === "about") return;
  event.preventDefault();
  props.onGo(key as "impact" | "explore");
}
</script>

<template>
  <nav class="nav" aria-label="Sections">
    <a
      v-for="item in items"
      :key="item.key"
      :href="item.href"
      :class="['nav-link', current === item.key && 'is-here']"
      :aria-current="current === item.key ? 'page' : undefined"
      @click="handle($event, item.key)"
    >{{ item.label }}</a>
  </nav>
</template>

<style scoped>
.nav {
  position: absolute;
  right: var(--pad, 3rem);
  top: 0.75rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 1.6rem;
}
.nav-link {
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  color: var(--ink, #1a1a17);
  font: 600 0.95rem var(--font-body, "Instrument Sans", sans-serif);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: color 0.15s ease, border-color 0.15s ease;
}
.nav-link:hover { color: var(--teal, #007d6c); }
/* The page you are on is stated, not just implied by removing the link. */
.nav-link.is-here { color: var(--teal, #007d6c); border-bottom-color: currentColor; }
.nav-link:focus-visible { outline: 2px solid var(--teal, #007d6c); outline-offset: 3px; border-radius: 2px; }

@media (max-width: 720px) {
  .nav { gap: 1rem; }
  .nav-link { font-size: 0.86rem; }
}
</style>
