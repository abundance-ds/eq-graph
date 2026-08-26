<template>
  <NuxtPage />
</template>

<style>
:root {
  color-scheme: light;
  --font-body: "Instrument Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-display: "Instrument Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-num: "IBM Plex Mono", "SFMono-Regular", Consolas, Menlo, monospace;
}

* { box-sizing: border-box; }
html { margin: 0; background: #fcfcfb; }
body, #__nuxt { min-height: 100%; margin: 0; }
body {
  overflow-x: hidden;
  background: #fcfcfb;
  color: #1a1a17;
  font-family: var(--font-body);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}
button, textarea, input { font: inherit; }

html.is-chat-cockpit,
body.is-chat-cockpit,
body.is-chat-cockpit #__nuxt {
  height: 100%;
  overflow: hidden;
}

.landing-v2-root .xp-root {
  position: relative;
  z-index: 3;
  min-height: 100vh;
  margin-top: -100vh;
  transition: none;
}

.landing-v2-root.is-chat-mode {
  height: 100dvh;
  overflow: hidden;
  background: #fff;
}

.landing-v2-root.is-chat-mode .sh-root {
  display: none;
}

.landing-v2-root.is-chat-mode .xp-root {
  height: 100dvh;
  min-height: 0;
  margin-top: 0;
  opacity: 1 !important;
  transform: none !important;
  pointer-events: auto !important;
}

.sr-only {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
}

.load-state {
  position: relative;
  min-height: 100vh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: 2rem;
  text-align: center;
}
/* The same two values the story and the About page pin the mark to. Not the
   page gutter, which is fluid, and so would put it somewhere else at every
   width. */
.load-logo { position: absolute; left: 3rem; top: 1.55rem; display: block; line-height: 0; }
.load-logo img { height: 27px; width: auto; display: block; }
@media (max-width: 900px) { .load-logo { left: 1.5rem; top: 1.2rem; } .load-logo img { height: 22px; } }
.load-error { max-width: 32rem; color: #a23c2a; line-height: 1.6; }
.xp-error { color: #a23c2a; font-size: 0.8rem; text-align: center; }

@media (prefers-reduced-motion: reduce) {
  .landing-v2-root .xp-root {
    margin-top: 0;
    opacity: 1 !important;
    transform: none !important;
  }
}
</style>
