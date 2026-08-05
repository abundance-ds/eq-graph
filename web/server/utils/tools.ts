/**
 * The agent tools.
 *
 * Keep this file free of any AI SDK import except `tool`. The bodies are plain
 * functions over the Neo4j driver. A change of SDK must not touch them.
 */
import { tool } from "ai";
import { z } from "zod";
import { runReadCypher, CypherRejected } from "./neo4j";
import { putResult } from "./results";
import { widgetSpec, resolveWidget } from "./widget";

/** The full-text index that serves each kind of thing. */
const SEARCH_INDEX = {
  project: { index: "project_text_ft", cypher: "node.projectId AS id, node.title AS label, node.status AS detail" },
  person: { index: "person_name_ft", cypher: "node.personId AS id, node.fullName AS label, node.orcid AS detail" },
  work: { index: "work_text_ft", cypher: "node.workId AS id, node.title AS label, node.journalName AS detail" },
  instrument: { index: "instrument_name_ft", cypher: "node.instrumentId AS id, node.name AS label, node.family AS detail" },
} as const;

export const searchGraph = tool({
  description:
    "Finds the identifier of a project, a person, a work or an instrument by " +
    "name or by topic. Call this before you write a WHERE clause that " +
    "compares a name. An exact string that you guess will not match.",
  inputSchema: z.object({
    query: z.string().describe("The words to search for. Two or three words work best."),
    kinds: z
      .array(z.enum(["project", "person", "work", "instrument"]))
      .optional()
      .describe("Which kinds to search. The default searches all of them."),
    limit: z.number().int().min(1).max(25).optional(),
  }),
  execute: async ({ query, kinds, limit }) => {
    const wanted = kinds ?? (["project", "person", "work", "instrument"] as const);
    const perKind = limit ?? 5;
    const hits: Record<string, unknown>[] = [];

    for (const kind of wanted) {
      const config = SEARCH_INDEX[kind];
      try {
        const result = await runReadCypher(
          `CALL db.index.fulltext.queryNodes($index, $query, {limit: $limit})
           YIELD node, score
           RETURN ${config.cypher}, score, '${kind}' AS kind`,
          { index: config.index, query, limit: perKind },
        );
        hits.push(...result.rows);
      } catch {
        // An index may be absent while the graph is still small. Skip it.
      }
    }

    hits.sort((a, b) => Number(b.score ?? 0) - Number(a.score ?? 0));
    if (hits.length === 0) {
      return { hits: [], note: "Nothing matched. Try fewer words, or other words." };
    }
    return { hits: hits.slice(0, 15) };
  },
});

export const runCypher = tool({
  description:
    "Runs one read query against the graph. Returns the column names, the " +
    "number of rows, a preview of the rows, and a resultId. Give that " +
    "resultId to the render tool to draw a chart.",
  inputSchema: z.object({
    cypher: z.string().describe("One Cypher read statement. Name every column with AS."),
    params: z
      .record(z.string(), z.unknown())
      .optional()
      .describe("The query parameters. Use a parameter instead of a value inside the string."),
    purpose: z.string().describe("One short sentence. What does this query answer?"),
  }),
  execute: async ({ cypher, params }) => {
    try {
      const result = await runReadCypher(cypher, params ?? {});
      const resultId = putResult(result);
      return {
        ok: true as const,
        resultId,
        columns: result.columns,
        rowCount: result.rowCount,
        truncated: result.truncated,
        elapsedMs: result.elapsedMs,
        warnings: result.warnings,
        // The model reads a preview only. The render tool reads the whole set.
        preview: result.rows.slice(0, 20),
      };
    } catch (error) {
      const message =
        error instanceof CypherRejected
          ? error.message
          : error instanceof Error
            ? error.message
            : String(error);
      return {
        ok: false as const,
        error: message,
        hint: "Read the schema again. Correct the query, then call this tool once more.",
      };
    }
  },
});

export const render = tool({
  description:
    "Draws a chart in the chat for the user. Call this after run_cypher when " +
    "the result holds more than two rows, or when one number deserves " +
    "emphasis. Pass the resultId. Never copy the data into this call.",
  inputSchema: widgetSpec,
  execute: async (spec) => {
    const resolved = resolveWidget(spec);
    if ("error" in resolved) {
      return { ok: false as const, error: resolved.error };
    }
    // The tool result is small on purpose. The browser reads the rows from
    // this output and draws the chart. The model needs no copy of the rows.
    return { ok: true as const, widget: resolved };
  },
});

export const agentTools = {
  search_graph: searchGraph,
  run_cypher: runCypher,
  render,
};
