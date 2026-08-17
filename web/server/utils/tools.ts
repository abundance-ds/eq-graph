import { tool } from "ai";
import { z } from "zod";
import { queryReferenceSql, SqlReadRejected } from "./referenceSqlite";

const encoding = z.object({
  x: z.string().optional().describe("Category, date, or horizontal-axis column. For bar and donut charts, use the label column."),
  y: z.string().optional().describe("Numeric measure or vertical-axis column. For bar and donut charts, use the numeric value column."),
  value: z.string().optional(),
  columns: z.array(z.string()).optional(),
});

const visualization = z.object({
  mark: z.enum(["stat", "bar", "line", "donut", "table"]),
  title: z.string(),
  caption: z.string().optional(),
  encoding,
  options: z.object({
    orientation: z.enum(["vertical", "horizontal"]).optional(),
    sort: z.enum(["asc", "desc", "none"]).optional(),
    limit: z.number().int().positive().max(50).optional(),
    unit: z.string().optional(),
    color: z.enum(["#007d6c", "#2a78d6", "#eb6834", "#eda100", "#e87ba4", "#1baf7a", "#4a3aa7"]).optional(),
    hint: z.string().optional(),
  }).optional(),
}).optional();

export const querySql = tool({
  description:
    "Runs one read-only SQLite query against the temporary EuroQol reference dataset. " +
    "The database rejects writes. Add a visualization when a chart or table makes the result easier to read.",
  inputSchema: z.object({
    sql: z.string().describe("One SQLite SELECT or WITH query. Name each returned column."),
    purpose: z.string().describe("One short sentence that states what the query answers."),
    visualization,
  }),
  execute: async ({ sql, visualization }) => {
    try {
      const result = queryReferenceSql(sql);
      let widget: Record<string, unknown> | undefined;

      if (visualization) {
        const named = new Set(result.columns);
        const requested = [
          visualization.encoding.x,
          visualization.encoding.y,
          visualization.encoding.value,
          ...(visualization.encoding.columns ?? []),
        ].filter(Boolean) as string[];
        const missing = requested.filter((column) => !named.has(column));
        if (missing.length) {
          return { ok: false as const, error: `The query did not return: ${missing.join(", ")}.` };
        }
        const required = visualization.mark === "stat"
          ? [visualization.encoding.value]
          : visualization.mark === "table"
            ? []
            : [visualization.encoding.x, visualization.encoding.y];
        if (required.some((field) => !field)) {
          return { ok: false as const, error: `The ${visualization.mark} visualization has an incomplete encoding.` };
        }
        const options = {
          ...visualization.options,
          ...(visualization.mark === "bar" && !visualization.options?.orientation ? { orientation: "horizontal" as const } : {}),
        };
        const requestedLimit = visualization.options?.limit ?? result.rows.length;
        const displayLimit = visualization.mark === "bar" || visualization.mark === "donut"
          ? Math.min(requestedLimit, 12)
          : visualization.mark === "stat"
            ? 1
            : requestedLimit;
        widget = {
          ...visualization,
          options,
          rows: result.rows.slice(0, displayLimit),
          rowCount: result.rowCount,
        };
      }

      return { ok: true as const, ...result, ...(widget ? { widget } : {}) };
    } catch (error) {
      return {
        ok: false as const,
        error: error instanceof SqlReadRejected ? error.message : error instanceof Error ? error.message : String(error),
        hint: "Correct the read query and use query_sql again.",
      };
    }
  },
});

// The model receives one data tool. Chart instructions are an optional part
// of the same query call, so a chart does not add another agent tool.
export const agentTools = { query_sql: querySql };
