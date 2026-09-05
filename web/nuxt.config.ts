export default defineNuxtConfig({
  compatibilityDate: "2025-01-01",
  devtools: { enabled: true },

  app: {
    head: {
      link: [
        // SVG first for browsers that take it; PNG and ICO for the rest.
        { rel: "icon", type: "image/svg+xml", href: "/favicon.svg" },
        { rel: "icon", type: "image/png", sizes: "32x32", href: "/favicon-32.png" },
        { rel: "icon", sizes: "any", href: "/favicon.ico" },
        { rel: "apple-touch-icon", sizes: "180x180", href: "/apple-touch-icon.png" },
      ],
      meta: [{ name: "theme-color", content: "#007d6c" }],
    },
  },

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
    adminToken: "",
    // The model that drives the agent.
    agentModel: "claude-sonnet-5",
  },

  nitro: {
    experimental: { asyncContext: true },
    // public/graph-scene.json is 1.4 MB of layout; ship it precompressed.
    compressPublicAssets: true,
  },

  routeRules: {
    // The graph page is a WebGL stage with no server-renderable content.
    "/graph": { ssr: false },
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
