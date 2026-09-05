export const CHART_SERIES = [
  "#007d6c",
  "#2a78d6",
  "#eb6834",
  "#a8720d",
  "#d65f8d",
  "#5c4fb3",
  "#1b8f6a",
];

export const CHART_RAMP = [
  "#edf7f4",
  "#cce9e2",
  "#94d1c4",
  "#4aaf9b",
  "#007d6c",
  "#005a4e",
];

export type ChartTokens = {
  paper: string;
  ink: string;
  secondary: string;
  muted: string;
  grid: string;
  axis: string;
  accent: string;
  negative: string;
  neutral: string;
  series: string[];
  ramp: string[];
};

function cssValue(style: CSSStyleDeclaration | undefined, name: string, fallback: string): string {
  return style?.getPropertyValue(name).trim() || fallback;
}

export function chartTokens(host?: Element): ChartTokens {
  const style = host ? getComputedStyle(host) : undefined;
  return {
    paper: cssValue(style, "--surface", "#ffffff"),
    ink: cssValue(style, "--ink-1", "#1a1a17"),
    secondary: cssValue(style, "--ink-2", "#5c5c56"),
    muted: cssValue(style, "--ink-3", "#8e8e86"),
    grid: cssValue(style, "--hairline", "#e5e4df"),
    axis: cssValue(style, "--hairline-strong", "#cbc9c1"),
    accent: cssValue(style, "--accent", CHART_SERIES[0]!),
    negative: "#2a78d6",
    neutral: "#d9d9d3",
    series: CHART_SERIES,
    ramp: CHART_RAMP,
  };
}
