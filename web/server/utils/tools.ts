import { tool } from "ai";
import { z } from "zod";
import { queryServingSql, SqlReadRejected } from "./servingSqlite";

const title = z.string().min(1).max(100)
  .describe("Short reader-facing title that names the measure and comparison.");
const caption = z.string().max(180).optional()
  .describe("Optional note about scope, denominator, unit, or ranking.");
const unit = z.string().max(20).optional()
  .describe("Short display unit such as %, years, or €. Do not repeat it in the title.");
const chartEncoding = z.object({
  category: z.string().optional().describe("Bar or donut category column."),
  measure: z.string().optional().describe("Bar or donut numeric measure column."),
  x: z.string().optional().describe("Line, area, or scatter horizontal column."),
  y: z.string().optional().describe("Line, area, or scatter numeric vertical column."),
  row: z.string().optional().describe("Heat-map row-category column."),
  column: z.string().optional().describe("Heat-map column-category column."),
  value: z.string().optional().describe("Stat, histogram, or heat-map numeric column."),
  source: z.string().optional().describe("Network source-node label column."),
  target: z.string().optional().describe("Network target-node label column."),
  weight: z.string().optional().describe("Optional network link-weight column; one per row by default."),
  series: z.string().optional().describe("Optional chart grouping column; at most seven groups."),
  columns: z.array(z.string()).optional().describe("Table columns; all result columns by default."),
});

const visualization = z.object({
  mark: z.enum(["stat", "bar", "line", "area", "scatter", "histogram", "heatmap", "donut", "network", "table"])
    .describe("Fields: stat(value); bar(category,measure); line/area/scatter(x,y); histogram(value); heatmap(column,row,value); donut(category,measure); network(source,target,weight?); table(columns)."),
  title,
  caption,
  encoding: chartEncoding,
  options: z.object({
    orientation: z.enum(["vertical", "horizontal"]).optional().describe("Bar direction; horizontal by default."),
    layout: z.enum(["grouped", "stacked"]).optional().describe("Bar layout when series is present."),
    unit,
  }).optional(),
});

type QueryResult = ReturnType<typeof queryServingSql>;
type Visualization = z.infer<typeof visualization>;
type VisualizationMark = Visualization["mark"];
type WidgetEncoding = {
  x?: string;
  y?: string;
  series?: string;
  value?: string;
  source?: string;
  target?: string;
  weight?: string;
  columns?: string[];
};
type WidgetSpec = {
  mark: VisualizationMark;
  title: string;
  caption?: string;
  encoding: WidgetEncoding;
  options?: { orientation?: "vertical" | "horizontal"; layout?: "grouped" | "stacked"; unit?: string };
};

function normalizeVisualization(spec: Visualization): WidgetSpec {
  const common = { mark: spec.mark, title: spec.title, caption: spec.caption };
  if (spec.mark === "bar") {
    return {
      ...common,
      encoding: { x: spec.encoding.category, y: spec.encoding.measure, series: spec.encoding.series },
      options: { ...spec.options, orientation: spec.options?.orientation ?? "horizontal" },
    };
  }
  if (spec.mark === "donut") {
    return { ...common, encoding: { x: spec.encoding.category, y: spec.encoding.measure }, options: spec.options };
  }
  if (spec.mark === "stat") {
    return { ...common, encoding: { value: spec.encoding.value }, options: spec.options };
  }
  if (spec.mark === "histogram") {
    return { ...common, encoding: { x: spec.encoding.value }, options: spec.options };
  }
  if (spec.mark === "heatmap") {
    return {
      ...common,
      encoding: { x: spec.encoding.column, y: spec.encoding.row, value: spec.encoding.value },
      options: spec.options,
    };
  }
  if (spec.mark === "network") {
    return {
      ...common,
      encoding: {
        source: spec.encoding.source,
        target: spec.encoding.target,
        weight: spec.encoding.weight,
      },
      options: spec.options,
    };
  }
  if (spec.mark === "table") {
    return { ...common, encoding: { columns: spec.encoding.columns } };
  }
  return {
    ...common,
    encoding: { x: spec.encoding.x, y: spec.encoding.y, series: spec.encoding.series },
    options: spec.options,
  };
}

function requiredColumns(mark: VisualizationMark, fields: WidgetEncoding): (string | undefined)[] {
  if (mark === "stat") return [fields.value];
  if (mark === "table") return [];
  if (mark === "histogram") return [fields.x];
  if (mark === "heatmap") return [fields.x, fields.y, fields.value];
  if (mark === "network") return [fields.source, fields.target];
  return [fields.x, fields.y];
}

function numericColumns(mark: VisualizationMark, fields: WidgetEncoding): (string | undefined)[] {
  if (mark === "stat" || mark === "heatmap") return [fields.value];
  if (mark === "histogram") return [fields.x];
  if (mark === "network") return fields.weight ? [fields.weight] : [];
  if (mark === "scatter") return [fields.x, fields.y];
  if (mark === "table") return [];
  return [fields.y];
}

function numericValue(value: unknown): number | null {
  if (typeof value === "number") return Number.isFinite(value) ? value : null;
  if (typeof value !== "string" || !value.trim()) return null;
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : null;
}

function uniqueCount(rows: Record<string, unknown>[], field?: string): number {
  return field ? new Set(rows.map((row) => String(row[field] ?? ""))).size : 0;
}

function validateVisualization(result: QueryResult, spec: WidgetSpec): string | undefined {
  const named = new Set(result.columns);
  const requested = [
    spec.encoding.x,
    spec.encoding.y,
    spec.encoding.series,
    spec.encoding.value,
    spec.encoding.source,
    spec.encoding.target,
    spec.encoding.weight,
    ...(spec.encoding.columns ?? []),
  ].filter(Boolean) as string[];
  const missing = requested.filter((column) => !named.has(column));
  if (missing.length) return `The query did not return: ${missing.join(", ")}.`;

  if (requiredColumns(spec.mark, spec.encoding).some((field) => !field)) {
    return `The ${spec.mark} visualization has an incomplete encoding.`;
  }

  if (!result.rows.length) return "The query returned no rows. Answer without a visualization or run a different query.";
  if (result.truncated) return `The query returned ${result.rowCount} rows. Refine it to at most 200 rows before visualizing.`;

  const rowCount = result.rows.length;
  const categories = uniqueCount(result.rows, spec.encoding.x);
  if (spec.mark === "stat" && rowCount !== 1) return "A stat requires exactly one result row.";
  if (spec.mark === "donut" && (rowCount < 2 || rowCount > 6)) return "A donut requires 2–6 exhaustive result rows.";
  if (spec.mark === "bar" && categories > 15) return "A bar chart supports at most 15 categories. Rank and limit the query first.";
  if (spec.mark === "table" && rowCount > 20) return "An inline table supports at most 20 rows. Rank and limit the query first.";
  if (spec.mark === "heatmap" && rowCount > 80) return "A heat map supports at most 80 cells. Aggregate or filter the query first.";
  if (spec.mark === "network") {
    const source = spec.encoding.source!;
    const target = spec.encoding.target!;
    const nodes = new Set(result.rows.flatMap((row) => [String(row[source]), String(row[target])]));
    if (rowCount > 60) return "A network supports at most 60 links. Rank and limit the query first.";
    if (nodes.size > 30) return "A network supports at most 30 nodes. Filter the query to a focused subgraph.";
    if (result.rows.some((row) => String(row[source]) === String(row[target]))) {
      return "A network cannot show self-links. Remove rows where source equals target.";
    }
  }
  if (spec.encoding.series && uniqueCount(result.rows, spec.encoding.series) > 7) {
    return "A chart supports at most seven series. Aggregate or filter the query first.";
  }

  const encoded = [...requiredColumns(spec.mark, spec.encoding), spec.encoding.series].filter(Boolean) as string[];
  for (const field of encoded) {
    if (result.rows.some((row) => row[field] === null || row[field] === undefined || row[field] === "")) {
      return `The ${field} column contains missing values. Filter or label them before visualizing.`;
    }
  }

  for (const field of numericColumns(spec.mark, spec.encoding).filter(Boolean) as string[]) {
    const values = result.rows.map((row) => row[field]);
    if (values.some((value) => numericValue(value) === null)) {
      return `The ${field} column must contain numeric values for a ${spec.mark} visualization.`;
    }
  }

  if (spec.mark === "donut") {
    const values = result.rows.map((row) => numericValue(row[spec.encoding.y!]) ?? 0);
    if (values.some((value) => value < 0) || values.reduce((sum, value) => sum + value, 0) <= 0) {
      return "A donut requires non-negative values with a positive total.";
    }
  }
  if (spec.mark === "heatmap") {
    const values = result.rows.map((row) => numericValue(row[spec.encoding.value!]) ?? 0);
    if (values.some((value) => value < 0)) return "This heat map requires non-negative values.";
  }
  if (spec.mark === "network" && spec.encoding.weight) {
    const values = result.rows.map((row) => numericValue(row[spec.encoding.weight!]) ?? -1);
    if (values.some((value) => value < 0)) return "Network weights must be non-negative.";
  }
}

export function createAgentTools() {
  const results = new Map<string, QueryResult>();
  let resultNumber = 0;

  const querySql = tool({
    description:
      "Query the read-only EQ-Graph SQLite release. Use it before every claim about the evidence base. " +
      "It returns a result_id, columns, rows, and total row count. Aggregate in SQL; add LIMIT 200 to row-level queries.",
    inputSchema: z.object({
      sql: z.string().min(1)
        .describe("One SQLite SELECT or WITH query with short result aliases. For what a study used, filter scientific_uses.context='DIRECT_CURRENT_ACTIVITY'."),
      purpose: z.string().min(3).max(80)
        .describe("User-visible 3–10 word action label, such as 'Count publications by year'."),
    }),
    execute: async ({ sql }) => {
      try {
        const result = queryServingSql(sql);
        const resultId = `result_${++resultNumber}`;
        results.set(resultId, result);
        return { ok: true as const, result_id: resultId, ...result };
      } catch (error) {
        return {
          ok: false as const,
          error: error instanceof SqlReadRejected ? error.message : error instanceof Error ? error.message : String(error),
          hint: "Correct the query and call query_sql again.",
        };
      }
    },
  });

  const showVisualization = tool({
    description:
      "Render one inline visualization after inspecting a query result. Omit it when prose is clearer. " +
      "Limits: stat=1 row; donut=2–6 exhaustive shares; bar=15 categories; table=20 rows; " +
      "heatmap=80 cells; network=30 nodes/60 links; any series=7 groups. Results must not be truncated. " +
      "Order rankings and time series in SQL; aggregate repeated network links in SQL.",
    inputSchema: z.object({
      result_id: z.string().describe("The result_id returned by query_sql in this response."),
      visualization,
    }),
    execute: async ({ result_id: resultId, visualization: requested }) => {
      const result = results.get(resultId);
      if (!result) return { ok: false as const, error: "That query result is not available. Run query_sql again." };

      const spec = normalizeVisualization(requested);
      const error = validateVisualization(result, spec);
      if (error) return { ok: false as const, error };

      const widget = { ...spec, rows: result.rows, rowCount: result.rowCount };
      return {
        ok: true as const,
        result_id: resultId,
        mark: spec.mark,
        rowCount: result.rowCount,
        widget,
      };
    },
  });

  return { query_sql: querySql, show_visualization: showVisualization };
}
