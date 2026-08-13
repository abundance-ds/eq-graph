import neo4j from "neo4j-driver";

const uri = process.env.NUXT_NEO4J_URI;
const user = process.env.NUXT_NEO4J_USER;
const password = process.env.NUXT_NEO4J_PASSWORD;
const database = process.env.NUXT_NEO4J_DATABASE?.trim();

if (!uri || !user || !password) {
  throw new Error(
    "Set NUXT_NEO4J_URI, NUXT_NEO4J_USER, and NUXT_NEO4J_PASSWORD in web/.env.",
  );
}

const driver = neo4j.driver(uri, neo4j.auth.basic(user, password), {
  disableLosslessIntegers: true,
});

async function main() {
  const server = await driver.getServerInfo();
  const session = driver.session({
    defaultAccessMode: neo4j.session.READ,
    ...(database ? { database } : {}),
  });

  try {
    const result = await session.run(`
      RETURN
        COUNT { MATCH (n) } AS nodes,
        COUNT { MATCH ()-[r]->() } AS relationships,
        COUNT { MATCH (:Project) } AS projects,
        COUNT { MATCH (:Work) } AS works,
        COUNT { MATCH (:Attribution {confidence: 'accepted'}) } AS acceptedAttributions,
        COUNT { MATCH (:Finding) } AS findings
    `);
    const counts = result.records[0]?.toObject();
    if (!counts) throw new Error("Neo4j returned no status row.");

    console.log(`Neo4j connection: OK (${server.agent})`);
    console.log(`Nodes: ${counts.nodes}`);
    console.log(`Relationships: ${counts.relationships}`);
    console.log(`Projects: ${counts.projects}`);
    console.log(`Works: ${counts.works}`);
    console.log(`Accepted attributions: ${counts.acceptedAttributions}`);
    console.log(`Findings: ${counts.findings}`);
  } finally {
    await session.close();
    await driver.close();
  }
}

main().catch(async (error) => {
  await driver.close();
  console.error(error instanceof Error ? error.message : error);
  process.exit(1);
});
