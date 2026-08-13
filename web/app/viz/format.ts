/**
 * The number formats.
 *
 * The file holds no chart code, so a component that shows only a number does
 * not pull the whole plot library into the bundle.
 */
import { format } from "d3-format";

export const fmt = {
  int: format(",.0f"),
  one: format(",.1f"),
  two: format(",.2f"),
  pct: format(".0%"),
  pct1: format(".1%"),
  /** 1284 becomes 1,284. 12900 becomes 12.9k. 4200000 becomes 4.2M. */
  compact(value: number): string {
    const size = Math.abs(value);
    if (size >= 1e6) return `${format(".1f")(value / 1e6)}M`;
    if (size >= 1e4) return `${format(".1f")(value / 1e3)}k`;
    return format(",.0f")(value);
  },
};
