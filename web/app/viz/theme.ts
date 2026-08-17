/**
 * The chart theme.
 *
 * One file holds every colour, every size and every format rule. The chat
 * widgets and the narrative story both read it, so the two look like one
 * product.
 *
 * The categorical colours use the designer palette. Direct labels and the
 * source table must carry identity when colour is not sufficient. Review the
 * light and dark variants in the chart gallery after a token changes.
 */

/** The eight series colours, in a fixed order. Never a ninth, never a cycle. */
export const SERIES_LIGHT = [
  "#007d6c", // 1 EuroQol green — the colour of the product
  "#2a78d6", // 2 blue
  "#eb6834", // 3 orange
  "#eda100", // 4 yellow
  "#e87ba4", // 5 magenta
  "#1baf7a", // 6 aqua
  "#4a3aa7", // 7 violet
  "#e34948", // 8 red
];

export const SERIES_DARK = [
  "#20a894",
  "#3987e5",
  "#f17d50",
  "#c98500",
  "#d55181",
  "#42bd91",
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
export const RAMP_LIGHT = ["#dff1ed", "#b8ded6", "#7fc6b8", "#42a895", "#007d6c", "#006052", "#003f36"];
export const RAMP_DARK = ["#12332e", "#164a41", "#196456", "#1b7f6b", "#239b83", "#42b79e", "#75cfbb"];

/** Two hues that read as opposite, with a grey middle for "no change". */
export const DIVERGING = { low: "#2a78d6", mid: "#e8e7e2", high: "#a8720d" };
export const DIVERGING_DARK = { low: "#3987e5", mid: "#343633", high: "#d6a33c" };

/** The ink and the paper. */
export const INK = {
  light: {
    surface: "#f4f3ef",
    raised: "#ffffff",
    primary: "#1a1a17",
    secondary: "#5c5c56",
    muted: "#8e8e86",
    grid: "#e1e0db",
    axis: "#c4c4bb",
    accent: "#007d6c",
    /** A mark that carries no story, beside the one that does. */
    mute: "#dcdcd5",
  },
  dark: {
    surface: "#1c1a17",
    raised: "#24211d",
    primary: "#f7f4ee",
    secondary: "#c9c2b6",
    muted: "#8a847a",
    grid: "#302c26",
    axis: "#423d35",
    accent: "#20a894",
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
  family: '"Instrument Sans", "Helvetica Neue", Helvetica, Arial, sans-serif',
  mono: '"IBM Plex Mono", ui-monospace, SFMono-Regular, "SF Mono", monospace',
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
