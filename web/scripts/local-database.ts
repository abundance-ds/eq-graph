const LOCAL_HOSTS = new Set(["localhost", "127.0.0.1", "[::1]", "::1"]);

export function localDatabaseConnection(action: string) {
  const uri = process.env.NUXT_NEO4J_URI ?? "bolt://localhost:7687";
  const user = process.env.NUXT_NEO4J_USER ?? "neo4j";
  const password = process.env.NUXT_NEO4J_PASSWORD ?? "eqgraphdev";

  let hostname: string;
  try {
    hostname = new URL(uri).hostname;
  } catch {
    throw new Error(`NUXT_NEO4J_URI is not a valid URI: ${uri}`);
  }

  if (!LOCAL_HOSTS.has(hostname)) {
    throw new Error(
      `${action} is local-only. Refusing to write to the Neo4j host ${hostname}.`,
    );
  }

  return { uri, user, password };
}
