/**
 * The agent tools.
 *
 * Keep this file free of any AI SDK import except tool. The bodies are plain
 * functions over the Neo4j driver.
 */
import { tool } from "ai";
import { z } from "zod";
import { runReadCypher, CypherRejected } from "./neo4j";
import { putResult } from "./results";
import { widgetSpec, resolveWidget } from "./widget";

const searchKind = z.enum([
  "project",
  "person",
  "work",
  "instrument",
  "concept",
  "method",
  "condition",
  "property",
  "country",
  "working_group",
  "journal",
  "value_set",
]);

type SearchKind = z.infer<typeof searchKind>;

const DEFAULT_SEARCH_KINDS: SearchKind[] = [
  "project",
  "person",
  "work",
  "instrument",
  "concept",
  "country",
  "working_group",
  "value_set",
];

/** Escapes text for the Lucene query parser used by Neo4j full-text indexes. */
function luceneText(value: string): string {
  return value.replace(/([+\-&|!(){}\[\]^"~*?:\\/])/g, "\\$1");
}

const PROJECT_SEARCH = `
CALL {
  MATCH (node:Project {projectId: $exact})
  RETURN node, 1000.0 AS score
  UNION ALL
  CALL db.index.fulltext.queryNodes('project_text_ft', $lucene, {limit: $limit})
  YIELD node, score
  RETURN node, score
}
WITH node, max(score) AS score
RETURN node.projectId AS id, node.title AS label, node.status AS detail,
       score, 'project' AS kind
ORDER BY score DESC LIMIT $limit
`;

const PERSON_SEARCH = `
CALL {
  MATCH (node:Person)
  WHERE node.personId = $exact OR node.orcid = $exact
  RETURN node, 1000.0 AS score
  UNION ALL
  CALL db.index.fulltext.queryNodes('person_name_ft', $lucene, {limit: $limit})
  YIELD node, score
  RETURN node, score
}
WITH node, max(score) AS score
RETURN node.personId AS id, node.fullName AS label, node.orcid AS detail,
       score, 'person' AS kind
ORDER BY score DESC LIMIT $limit
`;

const WORK_SEARCH = `
CALL {
  MATCH (node:Work)
  WHERE node.workId = $exact OR node.doi = $exact OR node.pmid = $exact OR node.pmcid = $exact
  RETURN node, 1000.0 AS score
  UNION ALL
  CALL db.index.fulltext.queryNodes('work_text_ft', $lucene, {limit: $limit})
  YIELD node, score
  RETURN node, score
}
WITH node, max(score) AS score
RETURN node.workId AS id, node.title AS label,
       coalesce(node.journalName, toString(node.year)) AS detail,
       score, 'work' AS kind
ORDER BY score DESC LIMIT $limit
`;

function ontologySearch(label: "Concept" | "Method" | "Condition" | "Property"): string {
  const labelFilter = label === "Concept" ? "node:Concept" : `node:${label}`;
  return `
CALL {
  MATCH (node:Concept)
  WHERE ${labelFilter}
    AND (node.conceptId = $exact OR node.code = $exact OR node.methodId = $exact)
  RETURN node, 1000.0 AS score
  UNION ALL
  CALL db.index.fulltext.queryNodes('concept_label_ft', $lucene, {limit: $limit})
  YIELD node, score
  WHERE ${labelFilter}
  RETURN node, score
  UNION ALL
  CALL db.index.fulltext.queryNodes('term_text_ft', $lucene, {limit: $limit})
  YIELD node AS term, score
  MATCH (term)-[:DENOTES]->(node:Concept)
  WHERE ${labelFilter}
  RETURN node, score * 0.9 AS score
}
WITH node, max(score) AS score
RETURN node.conceptId AS id, coalesce(node.prefLabel, node.name) AS label,
       coalesce(node.kind, node.scheme, node.status) AS detail,
       score,
       CASE
         WHEN node:Condition THEN 'condition'
         WHEN node:Method THEN 'method'
         WHEN node:Property THEN 'property'
         ELSE 'concept'
       END AS kind
ORDER BY score DESC LIMIT $limit
`;
}

const SCAN_SEARCH: Partial<Record<SearchKind, string>> = {
  instrument: `
    MATCH (node:Instrument)
    WHERE node.instrumentId = $exact
       OR toLower(node.name) CONTAINS toLower($exact)
       OR toLower(coalesce(node.family, '')) CONTAINS toLower($exact)
    RETURN node.instrumentId AS id, node.name AS label, node.family AS detail,
           CASE WHEN node.instrumentId = $exact OR toLower(node.name) = toLower($exact)
                THEN 1000.0 ELSE 25.0 END AS score,
           'instrument' AS kind
    ORDER BY score DESC, label LIMIT $limit
  `,
  country: `
    MATCH (node:Country)
    WHERE node.iso2 = toUpper($exact)
       OR toLower(node.name) CONTAINS toLower($exact)
    RETURN node.iso2 AS id, node.name AS label, node.m49Region AS detail,
           CASE WHEN node.iso2 = toUpper($exact) OR toLower(node.name) = toLower($exact)
                THEN 1000.0 ELSE 25.0 END AS score,
           'country' AS kind
    ORDER BY score DESC, label LIMIT $limit
  `,
  working_group: `
    MATCH (node:WorkingGroup)
    WHERE toLower(node.name) CONTAINS toLower($exact)
    RETURN node.name AS id, node.name AS label, null AS detail,
           CASE WHEN toLower(node.name) = toLower($exact) THEN 1000.0 ELSE 25.0 END AS score,
           'working_group' AS kind
    ORDER BY score DESC, label LIMIT $limit
  `,
  journal: `
    MATCH (node:Journal)
    WHERE toLower(node.name) CONTAINS toLower($exact)
    RETURN node.name AS id, node.name AS label, null AS detail,
           CASE WHEN toLower(node.name) = toLower($exact) THEN 1000.0 ELSE 25.0 END AS score,
           'journal' AS kind
    ORDER BY score DESC, label LIMIT $limit
  `,
  value_set: `
    MATCH (node:ValueSet)
    WHERE node.valueSetId = $exact
       OR toLower(coalesce(node.label, '')) CONTAINS toLower($exact)
       OR toLower(coalesce(node.technique, '')) = toLower($exact)
    RETURN node.valueSetId AS id, coalesce(node.label, node.valueSetId) AS label,
           coalesce(node.technique, toString(node.year)) AS detail,
           CASE WHEN node.valueSetId = $exact OR toLower(coalesce(node.label, '')) = toLower($exact)
                THEN 1000.0 ELSE 25.0 END AS score,
           'value_set' AS kind
    ORDER BY score DESC, label LIMIT $limit
  `,
};

function searchQuery(kind: SearchKind): string {
  if (kind === "project") return PROJECT_SEARCH;
  if (kind === "person") return PERSON_SEARCH;
  if (kind === "work") return WORK_SEARCH;
  if (kind === "concept") return ontologySearch("Concept");
  if (kind === "method") return ontologySearch("Method");
  if (kind === "condition") return ontologySearch("Condition");
  if (kind === "property") return ontologySearch("Property");
  return SCAN_SEARCH[kind]!;
}

export const searchGraph = tool({
  description:
    "Resolves a graph name or identifier before a Cypher query. It searches " +
    "projects, people, works, instruments, concepts, methods, conditions, " +
    "measurement properties, countries, working groups, journals, and value sets.",
  inputSchema: z.object({
    query: z.string().trim().min(1).describe("A name, identifier, or short topic phrase."),
    kinds: z
      .array(searchKind)
      .min(1)
      .optional()
      .describe("The graph types to search. Omit this to search the common entry points."),
    limit: z.number().int().min(1).max(25).optional()
      .describe("The maximum hits for each requested type. The default is 5."),
  }),
  execute: async ({ query, kinds, limit }) => {
    const wanted = [...new Set(kinds ?? DEFAULT_SEARCH_KINDS)];
    const perKind = limit ?? 5;
    const params = {
      exact: query,
      lucene: luceneText(query),
      limit: perKind,
    };

    const attempts = await Promise.all(
      wanted.map(async (kind) => {
        try {
          const result = await runReadCypher(searchQuery(kind), params);
          return { kind, rows: result.rows };
        } catch {
          return { kind, rows: [] as Record<string, unknown>[], unavailable: true };
        }
      }),
    );

    const unavailableKinds = attempts
      .filter((attempt) => attempt.unavailable)
      .map((attempt) => attempt.kind);
    const unique = new Map<string, Record<string, unknown>>();

    for (const hit of attempts.flatMap((attempt) => attempt.rows)) {
      const key = `${String(hit.kind)}:${String(hit.id)}`;
      const previous = unique.get(key);
      if (!previous || Number(hit.score ?? 0) > Number(previous.score ?? 0)) {
        unique.set(key, hit);
      }
    }

    const hits = [...unique.values()]
      .sort((left, right) => Number(right.score ?? 0) - Number(left.score ?? 0))
      .slice(0, 25);

    if (hits.length === 0) {
      return {
        hits: [],
        note: "The loaded graph has no match. Try fewer words or another graph type.",
        ...(unavailableKinds.length > 0 ? { unavailableKinds } : {}),
      };
    }
    return {
      hits,
      ...(unavailableKinds.length > 0 ? { unavailableKinds } : {}),
    };
  },
});

export const runCypher = tool({
  description:
    "Runs one read query against the graph. Returns the columns, row count, " +
    "a preview, and a resultId for render.",
  inputSchema: z.object({
    cypher: z.string().describe("One Cypher read statement. Name every returned column."),
    params: z
      .record(z.string(), z.unknown())
      .optional()
      .describe("Query parameters. Use these instead of values inside the statement."),
    purpose: z.string().describe("One short sentence that states what the query answers."),
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
        hint: "Check the schema, correct the read query, and call this tool again.",
      };
    }
  },
});

export const render = tool({
  description:
    "Draws a chart in the chat from a run_cypher result. Pass the resultId. " +
    "Do not copy result rows into this call.",
  inputSchema: widgetSpec,
  execute: async (spec) => {
    const resolved = resolveWidget(spec);
    if ("error" in resolved) {
      return { ok: false as const, error: resolved.error };
    }
    return { ok: true as const, widget: resolved };
  },
});

export const agentTools = {
  search_graph: searchGraph,
  run_cypher: runCypher,
  render,
};
