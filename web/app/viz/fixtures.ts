/**
 * The data for the gallery.
 *
 * The numbers are invented, and they hold to the shape of the graph. They are
 * fixed on purpose: a change of the seed must never change a picture in the
 * gallery, because the gallery is where the look of a mark gets judged.
 *
 * Each set also carries the hard cases: one row, forty rows, a very long name,
 * a missing value, and a negative value.
 */

export const WORKING_GROUPS = [
  { group: "EQ-HWB", projects: 24 },
  { group: "Valuation", projects: 20 },
  { group: "Descriptive Systems", projects: 20 },
  { group: "Youth instruments", projects: 18 },
  { group: "Psychometrics", projects: 16 },
  { group: "Methods and Modelling", projects: 14 },
  { group: "Populations and Health Systems", projects: 12 },
  { group: "Dissemination and open-access fee", projects: 12 },
];

/** Two series over the same categories. A legend is needed. */
export const LINK_QUALITY = WORKING_GROUPS.flatMap(({ group, projects }, i) => [
  { group, state: "Accepted", links: Math.round(projects * (0.5 + (i % 3) * 0.08)) },
  { group, state: "For review", links: Math.round(projects * (0.22 + (i % 4) * 0.05)) },
]);

/** A trend, three series, over sixteen years. */
const FAMILIES = ["EQ-5D-5L", "EQ-5D-3L", "EQ-HWB"] as const;
export const PUBLICATIONS = FAMILIES.flatMap((family, f) =>
  Array.from({ length: 16 }, (_, i) => {
    const year = new Date(Date.UTC(2010 + i, 0, 1));
    const base = [3, 26, 0][f]!;
    const growth = [1.42, 0.86, 1.9][f]!;
    const start = [4, 0, 9][f]!;
    // EQ-HWB starts in 2019. Before that the value is missing, and a missing
    // value must be a gap in the line, and never a zero.
    const value = i < start ? null : Math.round(base * Math.pow(growth, i - start) + (i % 3) * 2);
    return { family, year, works: value };
  }),
);

/** One series, cumulative. An area suits it. */
export const CORPUS = Array.from({ length: 16 }, (_, i) => {
  const year = new Date(Date.UTC(2010 + i, 0, 1));
  return { year, works: Math.round(320 * Math.pow(1.28, i)) };
});

/** Two measures for each study, and a third field for identity. */
const TECHNIQUES = ["cTTO", "DCE", "TTO"] as const;
/** A repeatable spread. Math.sin gives the same numbers on every run. */
function spread(i: number, salt: number): number {
  return (Math.sin((i + 1) * salt) + 1) / 2;
}
export const STUDIES = Array.from({ length: 96 }, (_, i) => {
  const technique = TECHNIQUES[i % 3]!;
  const year = 2010 + Math.floor(spread(i, 12.9898) * 16);
  const base = [1.0, 0.62, 0.44][i % 3]!;
  const size = Math.round(200 + Math.pow(spread(i, 78.233), 1.7) * 2400 * base);
  return { study: `S${String(i + 1).padStart(3, "0")}`, technique, year, size };
});

/** A distribution. The bins carry the story, and not the single values. */
export const SCORES = Array.from({ length: 640 }, (_, i) => {
  const noise = ((i * 2654435761) % 1000) / 1000;
  const shape = 0.18 + 0.62 * Math.pow(noise, 1.7);
  return { pair: i, score: Math.round(shape * 100) / 100 };
});

/** Two names against one another. A heat map reads it. */
const COUNTRIES = ["United Kingdom", "Netherlands", "China", "Spain", "Germany", "Australia", "Japan", "Canada"];
export const VALUE_SETS = COUNTRIES.flatMap((country, c) =>
  TECHNIQUES.map((technique, t) => ({
    country,
    technique,
    sets: Math.max(0, Math.round(9 - c * 0.9 + (t === 0 ? 3 : t === 1 ? 1 : -1) + ((c + t) % 3))),
  })),
);

/** The hard cases, for the states at the end of the gallery. */
export const ONE_ROW = [{ group: "Valuation", projects: 20 }];
export const NO_ROWS: { group: string; projects: number }[] = [];
export const MANY_ROWS = Array.from({ length: 40 }, (_, i) => ({
  group: `Project ${String(i + 1).padStart(2, "0")}`,
  projects: Math.round(48 * Math.pow(0.94, i)) + (i % 5),
}));
export const WITH_NEGATIVE = [
  { group: "EQ-HWB", change: 6 },
  { group: "Valuation", change: 3 },
  { group: "Descriptive Systems", change: -2 },
  { group: "Youth instruments", change: -5 },
  { group: "Psychometrics", change: 1 },
];

/** The numbers that lead a view. */
export const HEADLINE = {
  hero: { label: "Publications linked to a funded project", value: 1284 },
  tiles: [
    { label: "Funded projects", value: 944, delta: null, unit: "" },
    { label: "Accepted links", value: 318, delta: 0.24, unit: "" },
    { label: "Value sets published", value: 59, delta: 0.08, unit: "" },
    { label: "Mean links for each project", value: 1.4, delta: -0.03, unit: "" },
  ],
  spark: Array.from({ length: 12 }, (_, i) => ({ i, value: Math.round(60 * Math.pow(1.14, i) + (i % 4) * 9) })),
};
