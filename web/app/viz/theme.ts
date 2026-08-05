/**
 * The chart theme.
 *
 * One file holds every colour, every size and every format rule. The chat
 * widgets and the narrative story both read it, so the two look like one
 * product.
 *
 * The categorical colours are validated. The check covers the lightness band,
 * the chroma floor, the separation for colour blindness of each neighbour pair,
 * the separation for normal sight, and the contrast against the surface. Both
 * sets pass. Run the check again after any change of a value:
 *
 *   node scripts/validate_palette.js "<hex,hex,…>" --mode light --surface "#faf8f4"
 *
 * Results on 2026-08-04:
 *   light, neighbour pairs — worst colour blindness ΔE 9.1, worst normal 19.6
 *   dark,  neighbour pairs — worst colour blindness ΔE 8.4, worst normal 19.3
 *   light, first three, all pairs — 11.6 / 24.0 (safe for a scatter plot)
 *   dark,  first three, all pairs — 6.6 (needs a second channel: a symbol)
 *
 * Three light colours stay below a contrast of 3:1 against the cream surface
 * (aqua, yellow, magenta). Every chart that uses them must also carry a direct
 * label or the table behind it.
 */

/** The eight series colours, in a fixed order. Never a ninth, never a cycle. */
export const SERIES_LIGHT = [
  "#b4552d", // 1 terracotta — the colour of the product
  "#2a78d6", // 2 blue
  "#1baf7a", // 3 aqua
  "#eda100", // 4 yellow
  "#e87ba4", // 5 magenta
  "#008300", // 6 green
  "#4a3aa7", // 7 violet
  "#e34948", // 8 red
];

export const SERIES_DARK = [
  "#d2734a",
  "#3987e5",
  "#199e70",
  "#c98500",
  "#d55181",
  "#008300",
  "#9085e9",
  "#e66767",
];

/**
 * One hue for a size. Heat maps and maps read this.
 *
 * Each ramp starts beside the paper and moves away from it: pale on the cream
 * paper, and near black on the dark paper. So a small value always recedes and
 * a large value always stands out, in both modes.
 */
export const RAMP_LIGHT = ["#f9e6da", "#f0c6ac", "#e2a17c", "#cf7a4f", "#b4552d", "#8f4021", "#672d17"];
export const RAMP_DARK = ["#33241b", "#4d2f1f", "#6b3e23", "#8c4f28", "#ab6031", "#c76f3e", "#dd8a5c"];

/** Two hues that read as opposite, with a grey middle for "no change". */
export const DIVERGING = { low: "#2a78d6", mid: "#eee9e0", high: "#b4552d" };
export const DIVERGING_DARK = { low: "#3987e5", mid: "#33302a", high: "#d2734a" };

/** The ink and the paper. */
export const INK = {
  light: {
    surface: "#faf8f4",
    raised: "#ffffff",
    primary: "#1c1a17",
    secondary: "#57524a",
    muted: "#8a847a",
    grid: "#e7e2d8",
    axis: "#cfc9bf",
    accent: "#b4552d",
    /** A mark that carries no story, beside the one that does. */
    mute: "#e2dbcd",
  },
  dark: {
    surface: "#1c1a17",
    raised: "#24211d",
    primary: "#f7f4ee",
    secondary: "#c9c2b6",
    muted: "#8a847a",
    grid: "#302c26",
    axis: "#423d35",
    accent: "#d2734a",
    mute: "#403a31",
  },
};

/** The sizes that every mark holds to. */
export const MARK = {
  /** A bar never fills its band. The rest of the band is air. */
  barMax: 24,
  /** White does the separating, and not a stroke. */
  gap: 2,
  lineWidth: 2,
  dotRadius: 4.5,
  areaOpacity: 0.1,
  /** A figure is wide, and not tall. */
  aspect: 1.9,
};

export const TYPE = {
  family: 'system-ui, -apple-system, "Segoe UI", sans-serif',
  mono: 'ui-monospace, SFMono-Regular, "SF Mono", monospace',
  tick: 11,
  label: 12,
  title: 14,
};

/** True when the page draws on a dark background. */
export function isDark(): boolean {
  if (typeof document === "undefined") return false;
  const stamp = document.documentElement.dataset.theme;
  if (stamp === "dark") return true;
  if (stamp === "light") return false;
  return window.matchMedia?.("(prefers-color-scheme: dark)").matches ?? false;
}

/** Every token for the mode that the page shows now. */
export function tokens(dark = isDark()) {
  return {
    dark,
    ink: dark ? INK.dark : INK.light,
    series: dark ? SERIES_DARK : SERIES_LIGHT,
    ramp: dark ? RAMP_DARK : RAMP_LIGHT,
    diverging: dark ? DIVERGING_DARK : DIVERGING,
    mark: MARK,
    type: TYPE,
  };
}
