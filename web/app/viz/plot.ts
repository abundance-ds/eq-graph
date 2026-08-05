/**
 * The shared parts of every figure.
 *
 * Observable Plot draws the marks. This file holds the decisions that must be
 * the same in each figure: the margins, the quiet grid, the tick size, the
 * number formats and the thickness of a bar.
 */
import * as Plot from "@observablehq/plot";
import { MARK, TYPE, tokens } from "./theme";

export { fmt } from "./format";

export type Tokens = ReturnType<typeof tokens>;

/** The frame: transparent paper, one type family, room for the labels. */
export function frame(t: Tokens, extra: Record<string, unknown> = {}) {
  return {
    style: {
      background: "transparent",
      color: t.ink.secondary,
      fontFamily: TYPE.family,
      fontSize: `${TYPE.tick}px`,
      overflow: "visible",
    },
    marginTop: 24,
    marginRight: 18,
    marginBottom: 32,
    marginLeft: 46,
    ...extra,
  };
}

/** A hairline grid, solid, one step off the paper, behind the data. */
export function gridY(t: Tokens) {
  return Plot.gridY({ stroke: t.ink.grid, strokeOpacity: 1, strokeWidth: 1 });
}

export function gridX(t: Tokens) {
  return Plot.gridX({ stroke: t.ink.grid, strokeOpacity: 1, strokeWidth: 1 });
}

/** The one baseline that every bar grows from. */
export function baseY(t: Tokens) {
  return Plot.ruleY([0], { stroke: t.ink.axis, strokeWidth: 1 });
}

export function baseX(t: Tokens) {
  return Plot.ruleX([0], { stroke: t.ink.axis, strokeWidth: 1 });
}

/** No tick marks. The label alone is enough. */
export function axis(t: Tokens, extra: Record<string, unknown> = {}) {
  return { tickSize: 0, tickPadding: 6, color: t.ink.muted, ...extra };
}

/**
 * The thickness of a bar. A bar never fills its band: the rest is air, and it
 * never grows past 24 px. The inset gives that air, and it also gives the 2 px
 * that separates two bars that touch.
 */
export function barInset(count: number, extent: number): number {
  const band = extent / Math.max(count, 1);
  const air = Math.max(band - MARK.barMax, band * 0.3);
  return Math.max(air / 2, 1);
}

/** The value that a direct label shows, and only where it fits. */
export function endLabel(t: Tokens, options: Record<string, unknown> = {}) {
  return {
    fill: t.ink.secondary,
    fontSize: TYPE.label,
    fontVariant: "tabular-nums",
    ...options,
  };
}

export { Plot, MARK, TYPE };
