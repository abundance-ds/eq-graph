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

.landing-v2-root:not(.is-chat-mode) .xp-root {
  visibility: hidden;
  opacity: 0;
  pointer-events: none;
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
  visibility: visible;
  height: 100dvh;
  min-height: 0;
  margin-top: 0;
  opacity: 1 !important;
  transform: none !important;
  pointer-events: auto !important;
}

.landing-v2-root:not(.is-chat-mode) .sh-handoff-form {
  view-transition-name: research-composer;
}
.landing-v2-root.is-chat-mode .chat-composer {
  view-transition-name: research-composer;
}
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 260ms;
  animation-timing-function: ease;
}
::view-transition-group(research-composer) {
  animation-duration: 450ms;
  animation-timing-function: cubic-bezier(.2,.9,.3,1);
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
.load-error { max-width: 32rem; color: #a23c2a; line-height: 1.6; }
.xp-error { color: #a23c2a; font-size: 0.8rem; text-align: center; }

@media (prefers-reduced-motion: reduce) {
  .landing-v2-root .xp-root {
    transition: none !important;
  }
}
</style>
