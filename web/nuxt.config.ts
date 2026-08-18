export default defineNuxtConfig({
  compatibilityDate: "2025-01-01",
  devtools: { enabled: true },

  css: [
    "@fontsource/instrument-sans/400.css",
    "@fontsource/instrument-sans/500.css",
    "@fontsource/instrument-sans/600.css",
    "@fontsource/ibm-plex-mono/400.css",
    "@fontsource/ibm-plex-mono/500.css",
    "@fontsource/ibm-plex-mono/600.css",
    "~/assets/css/story-h.css",
    "~/assets/css/explore.css",
  ],

  runtimeConfig: {
    // Filled from NUXT_-prefixed environment variables. Never hard code a key.
    anthropicApiKey: "",
    // The model that drives the agent.
    agentModel: "claude-sonnet-5",
  },

  nitro: {
    experimental: { asyncContext: true },
  },

  // Let the dev server be reached through a Cloudflare quick tunnel
  // (….trycloudflare.com), so a branch can be shown to someone who is not on
  // this machine. Without this, Vite's dev host check rejects the tunnelled
  // request before it ever reaches the app. Dev only — it has no effect on a
  // build, and it opens nothing by itself; a tunnel still has to be started.
  vite: {
    server: {
      allowedHosts: [".trycloudflare.com"],
    },
  },
});
