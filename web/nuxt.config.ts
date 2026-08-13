export default defineNuxtConfig({
  compatibilityDate: "2025-01-01",
  devtools: { enabled: true },

  runtimeConfig: {
    // Filled from NUXT_-prefixed environment variables. Never hard code a key.
    anthropicApiKey: "",
    neo4jUri: "",
    neo4jUser: "",
    neo4jPassword: "",
    // Leave this empty to use the account's Neo4j home database.
    neo4jDatabase: "",
    // The model that drives the agent. Change the provider in one place:
    // server/utils/model.ts
    agentModel: "claude-sonnet-5",
    // Guards for run_cypher.
    cypherTimeoutMs: 10_000,
    cypherRowCap: 2000,
  },

  nitro: {
    experimental: { asyncContext: true },
  },
});
