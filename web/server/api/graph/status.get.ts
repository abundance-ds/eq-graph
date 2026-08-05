import { runReadCypher } from "../../utils/neo4j";

const STATUS_QUERY = `
RETURN
  COUNT { MATCH (n) } AS nodes,
  COUNT { MATCH ()-[r]->() } AS relationships,
  COUNT { MATCH (:Project) } AS projects,
  COUNT { MATCH (:Work) } AS works,
  COUNT { MATCH (:Attribution {confidence: 'accepted'}) } AS acceptedAttributions,
  COUNT { MATCH (:FullText) } AS fullTexts,
  COUNT { MATCH (:Study) } AS studies,
  COUNT { MATCH (:Finding) } AS findings
`;

export default defineEventHandler(async (event) => {
  setHeader(event, "Cache-Control", "no-store");

  try {
    const result = await runReadCypher(STATUS_QUERY);
    const counts = result.rows[0];
    if (!counts) throw new Error("Neo4j returned no status row.");

    return {
      ok: true as const,
      checkedAt: new Date().toISOString(),
      counts,
    };
  } catch (error) {
    console.error("[graph status]", error);
    throw createError({
      statusCode: 503,
      statusMessage: "The research graph is not available.",
    });
  }
});
