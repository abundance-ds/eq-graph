import * as Plot from "@observablehq/plot";
import type { ChatWidgetSpec } from "../types/chat";
import { fieldLabel, formatNumber, numeric } from "./format";
import type { ChartTokens } from "./theme";

type Row = Record<string, unknown>;

const TYPE_BODY = '"Instrument Sans", "Helvetica Neue", Helvetica, Arial, sans-serif';
const TYPE_NUMBER = '"IBM Plex Mono", "SFMono-Regular", Consolas, Menlo, monospace';

function unique(rows: Row[], key?: string): string[] {
  if (!key) return [];
  return [...new Set(rows.map((row) => String(row[key] ?? "").trim()).filter(Boolean))];
}

function categoricalRows(rows: Row[], keys: (string | undefined)[]): Row[] {
  const fields = keys.filter((key): key is string => Boolean(key));
  if (!fields.length) return rows;
  return rows.map((row) => ({
    ...row,
    ...Object.fromEntries(fields.map((field) => [field, String(row[field] ?? "").trim()])),
  }));
}

function valueExtent(rows: Row[], key?: string): [number, number] {
  const values = key
    ? rows.map((row) => numeric(row[key])).filter((value): value is number => value !== null)
    : [];
  return values.length ? [Math.min(...values), Math.max(...values)] : [0, 0];
}

function labelMargin(labels: string[]): number {
  const longest = Math.max(0, ...labels.map((label) => label.length));
  return Math.min(194, Math.max(92, longest * 6.2 + 18));
}

function xAxis(rows: Row[], key: string) {
  const values = rows.map((row) => numeric(row[key]));
  const years = values.length > 1 && values.every((value) =>
    value !== null && Number.isInteger(value) && value >= 1800 && value <= 2200
  );
  return years
    ? { tickFormat: (value: number) => String(Math.round(value)), ticks: Math.min(8, new Set(values).size) }
    : {};
}

function frame(tokens: ChartTokens, width: number, extra: Record<string, unknown> = {}) {
  return {
    width,
    style: {
      background: "transparent",
      color: tokens.secondary,
      fontFamily: TYPE_BODY,
      fontSize: "11px",
      overflow: "visible",
    },
    marginTop: 18,
    marginRight: 30,
    marginBottom: 30,
    marginLeft: 48,
    ...extra,
  };
}

function axis(tokens: ChartTokens, extra: Record<string, unknown> = {}) {
  return { tickSize: 0, tickPadding: 7, color: tokens.muted, ...extra };
}

function tooltip(spec: ChatWidgetSpec, x: string, y?: string) {
  return (row: Row) => {
    const parts = [String(row[x] ?? "")];
    if (spec.encoding.series) parts.push(String(row[spec.encoding.series] ?? ""));
    if (y) parts.push(formatNumber(row[y], spec.options?.unit));
    return parts.filter(Boolean).join("\n");
  };
}

function colorScale(tokens: ChartTokens, rows: Row[], series?: string) {
  const domain = unique(rows, series);
  return series && domain.length
    ? { domain, range: tokens.series.slice(0, domain.length), legend: true }
    : undefined;
}

function barPlot(
  spec: ChatWidgetSpec,
  width: number,
  tokens: ChartTokens,
) {
  const { x, y, series } = spec.encoding;
  if (!x || !y) return null;
  const rows = categoricalRows(spec.rows, [x, series]);
  const categories = unique(rows, x);
  const groups = unique(rows, series);
  const horizontal = spec.options?.orientation !== "vertical";
  const layout = series ? spec.options?.layout ?? "grouped" : undefined;
  const unit = spec.options?.unit ?? "";
  const [low, high] = valueExtent(rows, y);
  const totals = new Map<string, number>();
  for (const row of rows) {
    const label = String(row[x] ?? "");
    totals.set(label, (totals.get(label) ?? 0) + (numeric(row[y]) ?? 0));
  }
  const fill = series
    ? series
    : low < 0
      ? (row: Row) => (numeric(row[y]) ?? 0) < 0 ? tokens.negative : tokens.accent
      : tokens.accent;
  const color = colorScale(tokens, rows, series);

  if (horizontal) {
    const grouped = layout === "grouped" && groups.length > 1;
    const height = grouped
      ? Math.max(170, categories.length * Math.max(2, groups.length) * 18 + 50)
      : Math.max(150, categories.length * 31 + 28);
    const shared = {
      x: y,
      fill,
      stroke: tokens.paper,
      strokeWidth: 1.5,
      insetTop: grouped ? 2 : 5,
      insetBottom: grouped ? 2 : 5,
      rx2: 4,
      title: tooltip(spec, x, y),
    };
    const marks: any[] = [];

    if (grouped) {
      marks.push(
        Plot.barX(rows, { ...shared, fy: x, y: series }),
        Plot.text(rows, {
          fy: x,
          y: series,
          x: y,
          text: (row: Row) => formatNumber(row[y], unit),
          textAnchor: "start",
          dx: 6,
          fill: tokens.secondary,
          fontFamily: TYPE_NUMBER,
          fontSize: 10,
        }),
      );
    } else if (layout === "stacked" && series) {
      marks.push(
        Plot.barX(rows, { ...shared, y: x, insetLeft: 1, insetRight: 1 }),
        Plot.text([...totals], {
          y: ([label]: [string, number]) => label,
          x: ([, value]: [string, number]) => value,
          text: ([, value]: [string, number]) => formatNumber(value, unit),
          textAnchor: "start",
          dx: 7,
          fill: tokens.secondary,
          fontFamily: TYPE_NUMBER,
          fontSize: 10,
        }),
      );
    } else {
      marks.push(
        Plot.barX(rows, { ...shared, y: x, x1: 0, x2: y }),
        Plot.text(rows.filter((row) => (numeric(row[y]) ?? 0) >= 0), {
          y: x,
          x: y,
          text: (row: Row) => formatNumber(row[y], unit),
          textAnchor: "start",
          dx: 7,
          fill: tokens.secondary,
          fontFamily: TYPE_NUMBER,
          fontSize: 10,
        }),
        Plot.text(rows.filter((row) => (numeric(row[y]) ?? 0) < 0), {
          y: x,
          x: y,
          text: (row: Row) => formatNumber(row[y], unit),
          textAnchor: "end",
          dx: -7,
          fill: tokens.secondary,
          fontFamily: TYPE_NUMBER,
          fontSize: 10,
        }),
      );
    }
    marks.push(Plot.ruleX([0], { stroke: tokens.axis }));

    return Plot.plot({
      ...frame(tokens, width, {
        height,
        marginLeft: labelMargin(categories),
        marginRight: 54,
        marginTop: color ? 34 : 10,
      }),
      x: {
        axis: null,
        label: null,
        ...(low < 0 ? { domain: [-Math.max(Math.abs(low), Math.abs(high)) * 1.22, Math.max(Math.abs(low), Math.abs(high)) * 1.22] } : {}),
      },
      y: grouped ? { axis: null, label: null } : { domain: categories, label: null, ...axis(tokens) },
      fy: grouped ? { domain: categories, label: null, ...axis(tokens) } : undefined,
      color,
      marks,
    });
  }

  const grouped = layout === "grouped" && groups.length > 1;
  const marks: any[] = [];
  const shared = {
    y,
    fill,
    stroke: tokens.paper,
    strokeWidth: 1.5,
    insetLeft: 4,
    insetRight: 4,
    ry2: 4,
    title: tooltip(spec, x, y),
  };
  if (grouped) marks.push(Plot.barY(rows, { ...shared, fx: x, x: series }));
  else if (layout === "stacked" && series) marks.push(Plot.barY(rows, { ...shared, x }));
  else marks.push(Plot.barY(rows, { ...shared, x, y1: 0, y2: y }));
  marks.push(Plot.ruleY([0], { stroke: tokens.axis }));

  return Plot.plot({
    ...frame(tokens, width, { height: 280, marginTop: color ? 34 : 20 }),
    x: grouped ? { axis: null, label: null } : { domain: categories, label: null, ...axis(tokens) },
    fx: grouped ? { domain: categories, label: null, ...axis(tokens) } : undefined,
    y: { label: unit || null, grid: true, ...axis(tokens) },
    color,
    marks,
  });
}

function linePlot(spec: ChatWidgetSpec, width: number, tokens: ChartTokens, area: boolean) {
  const rows = spec.rows;
  const { x, y, series } = spec.encoding;
  if (!x || !y) return null;
  const groups = unique(rows, series);
  const color = colorScale(tokens, rows, series);
  const last = series
    ? groups.map((group) => rows.filter((row) => String(row[series] ?? "") === group).at(-1)).filter(Boolean) as Row[]
    : rows.length ? [rows.at(-1)!] : [];
  const labelled = series
    ? [...last].sort((a, b) => (numeric(b[y]) ?? 0) - (numeric(a[y]) ?? 0)).slice(0, 1)
    : last;
  const stroke = series || tokens.accent;
  const marks: any[] = [Plot.gridY({ stroke: tokens.grid })];

  if (area) {
    marks.push(Plot.areaY(rows, {
      x,
      y1: 0,
      y2: y,
      z: series,
      fill: series || tokens.accent,
      fillOpacity: series ? 0.1 : 0.13,
      curve: "monotone-x",
    }));
  }
  marks.push(
    Plot.line(rows, { x, y, z: series, stroke, strokeWidth: 2, curve: "monotone-x" }),
    Plot.dot(last, { x, y, fill: series || tokens.accent, r: 4.5, stroke: tokens.paper, strokeWidth: 2 }),
    ...labelled.map((end) => Plot.text([end], {
      x,
      y,
      text: (row: Row) => series
        ? `${String(row[series] ?? "")}  ${formatNumber(row[y], spec.options?.unit)}`
        : formatNumber(row[y], spec.options?.unit),
      textAnchor: "end",
      dy: -12,
      fill: tokens.secondary,
      fontFamily: TYPE_NUMBER,
      fontSize: 10,
    })),
    Plot.tip(rows, Plot.pointerX({
      x,
      y,
      z: series,
      title: tooltip(spec, x, y),
      fill: tokens.paper,
      stroke: tokens.axis,
    })),
    Plot.ruleY([0], { stroke: tokens.axis }),
  );

  return Plot.plot({
    ...frame(tokens, width, { height: 270, marginTop: color ? 38 : 26 }),
    x: { label: null, ...axis(tokens), ...xAxis(rows, x) },
    y: { label: spec.options?.unit || null, ...axis(tokens) },
    color,
    marks,
  });
}

function scatterPlot(spec: ChatWidgetSpec, width: number, tokens: ChartTokens) {
  const { x, y, series } = spec.encoding;
  if (!x || !y) return null;
  const color = colorScale(tokens, spec.rows, series);
  return Plot.plot({
    ...frame(tokens, width, { height: 290, marginTop: color ? 38 : 24 }),
    x: { label: fieldLabel(x), grid: true, ...axis(tokens), ...xAxis(spec.rows, x) },
    y: { label: fieldLabel(y), grid: true, ...axis(tokens) },
    color,
    symbol: series ? { legend: false } : undefined,
    marks: [
      Plot.dot(spec.rows, {
        x,
        y,
        fill: series || tokens.accent,
        symbol: series,
        r: 4.7,
        stroke: tokens.paper,
        strokeWidth: 1.5,
        tip: true,
        title: tooltip(spec, x, y),
      }),
      Plot.ruleY([0], { stroke: tokens.axis }),
    ],
  });
}

function histogramPlot(spec: ChatWidgetSpec, width: number, tokens: ChartTokens) {
  const x = spec.encoding.x;
  if (!x) return null;
  return Plot.plot({
    ...frame(tokens, width, { height: 245, marginTop: 24 }),
    x: { label: fieldLabel(x), ...axis(tokens) },
    y: { label: "Count", grid: true, ...axis(tokens) },
    marks: [
      Plot.rectY(spec.rows, {
        ...Plot.binX({ y: "count" }, { x }),
        fill: tokens.accent,
        insetLeft: 1,
        insetRight: 1,
        ry2: 3,
        tip: true,
      }),
      Plot.ruleY([0], { stroke: tokens.axis }),
    ],
  });
}

function heatmapPlot(spec: ChatWidgetSpec, width: number, tokens: ChartTokens) {
  const { x, y, value } = spec.encoding;
  if (!x || !y || !value) return null;
  const rows = categoricalRows(spec.rows, [x, y]);
  const [, high] = valueExtent(rows, value);
  const yDomain = unique(rows, y);
  return Plot.plot({
    ...frame(tokens, width, {
      height: Math.max(190, yDomain.length * 34 + 70),
      marginLeft: labelMargin(yDomain),
      marginTop: 46,
      marginBottom: 12,
    }),
    x: { axis: "top", label: null, ...axis(tokens) },
    y: { domain: yDomain, label: null, ...axis(tokens) },
    color: {
      type: "linear",
      domain: [0, high || 1],
      range: tokens.ramp,
      label: fieldLabel(value),
      legend: true,
    },
    marks: [
      Plot.cell(rows, { x, y, fill: value, inset: 1, rx: 3, tip: true, title: tooltip(spec, x, value) }),
      Plot.text(rows, {
        x,
        y,
        text: (row: Row) => formatNumber(row[value], spec.options?.unit),
        fill: (row: Row) => (numeric(row[value]) ?? 0) > high * 0.55 ? "#ffffff" : tokens.ink,
        fontFamily: TYPE_NUMBER,
        fontSize: 10,
      }),
    ],
  });
}

export function createChatPlot(
  spec: ChatWidgetSpec,
  width: number,
  tokens: ChartTokens,
): HTMLElement | SVGSVGElement | null {
  if (spec.mark === "bar") return barPlot(spec, width, tokens);
  if (spec.mark === "line") return linePlot(spec, width, tokens, false);
  if (spec.mark === "area") return linePlot(spec, width, tokens, true);
  if (spec.mark === "scatter") return scatterPlot(spec, width, tokens);
  if (spec.mark === "histogram") return histogramPlot(spec, width, tokens);
  if (spec.mark === "heatmap") return heatmapPlot(spec, width, tokens);
  return null;
}
