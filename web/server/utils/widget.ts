/**
 * The widget specification.
 *
 * One tool draws every chart. The mark field selects the chart. One schema is
 * easier to maintain than one tool for each chart, and the model chooses the
 * mark as a field.
 *
 * The specification carries the encoding, and it never carries the data. The
 * rows arrive from the result store through resultId.
 */
import { z } from "zod";
import { getResult } from "./results";

export const widgetSpec = z.object({
  mark: z
    .enum(["stat", "bar", "line", "table"])
    .describe(
      "stat for one number. bar for a comparison between categories. " +
        "line for a value over time. table for ranked rows.",
    ),
  title: z.string().describe("A short title. Say what the reader sees."),
  caption: z
    .string()
    .optional()
    .describe("One sentence under the chart. State a filter or a caveat here."),
  resultId: z.string().describe("The resultId that run_cypher returned."),
  encoding: z.object({
    x: z.string().optional().describe("The column for the category or the time axis. bar and line need this."),
    y: z.string().optional().describe("The column for the numeric value. bar and line need this."),
    series: z.string().optional().describe("The column that splits the data into groups."),
    value: z.string().optional().describe("The column that holds the number. stat needs this."),
    columns: z.array(z.string()).optional().describe("The columns to show. table uses this."),
  }),
  options: z
    .object({
      orientation: z.enum(["vertical", "horizontal"]).optional()
        .describe("Use horizontal when the labels are long."),
      sort: z.enum(["asc", "desc", "none"]).optional(),
      limit: z.number().int().positive().max(50).optional(),
      unit: z.string().optional().describe("A suffix, for example % or EUR."),
    })
    .optional(),
});

export type WidgetSpec = z.infer<typeof widgetSpec>;

export type ResolvedWidget = WidgetSpec & {
  rows: Record<string, unknown>[];
  rowCount: number;
};

/**
 * Checks the specification against the real result, then attaches the rows.
 * Returns a message when the specification is wrong. The caller sends that
 * message back to the model, and the model corrects itself.
 */
export function resolveWidget(spec: WidgetSpec): ResolvedWidget | { error: string } {
  const result = getResult(spec.resultId);
  if (!result) {
    return { error: `No result has the id ${spec.resultId}. Run run_cypher first.` };
  }

  const columns = new Set(result.columns);
  const missing: string[] = [];
  const need = (name: string | undefined) => {
    if (name && !columns.has(name)) missing.push(name);
  };

  need(spec.encoding.x);
  need(spec.encoding.y);
  need(spec.encoding.series);
  need(spec.encoding.value);
  for (const column of spec.encoding.columns ?? []) need(column);

  if (missing.length > 0) {
    return {
      error:
        `The result ${spec.resultId} has no column named ${missing.join(", ")}. ` +
        `It has these columns: ${result.columns.join(", ")}.`,
    };
  }

  const required: Record<WidgetSpec["mark"], string[]> = {
    stat: ["value"],
    bar: ["x", "y"],
    line: ["x", "y"],
    table: [],
  };
  for (const field of required[spec.mark]) {
    if (!spec.encoding[field as keyof typeof spec.encoding]) {
      return { error: `The mark ${spec.mark} needs encoding.${field}.` };
    }
  }

  let rows = [...result.rows];
  const sort = spec.options?.sort ?? "none";
  const sortKey = spec.mark === "line" ? spec.encoding.x : spec.encoding.y;
  if (sort !== "none" && sortKey) {
    rows.sort((a, b) => {
      const left = Number(a[sortKey]) || 0;
      const right = Number(b[sortKey]) || 0;
      return sort === "asc" ? left - right : right - left;
    });
  }
  if (spec.options?.limit) rows = rows.slice(0, spec.options.limit);

  return { ...spec, rows, rowCount: result.rowCount };
}
