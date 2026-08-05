export default defineNuxtConfig({
  compatibilityDate: "2025-01-01",
  devtools: { enabled: true },

  runtimeConfig: {
    // Filled from NUXT_-prefixed environment variables. Never hard code a key.
    anthropicApiKey: "",
    neo4jUri: "bolt://localhost:7687",
    neo4jUser: "neo4j",
    neo4jPassword: "",
    // The model that drives the agent. Change the provider in one place:
    // server/utils/model.ts
    agentModel: "claude-opus-5",
    // Guards for run_cypher.
    cypherTimeoutMs: 10_000,
    cypherRowCap: 2000,
  },

  nitro: {
    experimental: { asyncContext: true },
  },
});
