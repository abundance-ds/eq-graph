import graph from "../data/reference-graph.json";
import live from "../data/reference-live.json";
import type {
  DemoGraphData,
  DemoResearchData,
  DemoSeries,
} from "../../shared/types/demo";

/**
 * TODO(data): Replace these reference fixtures when the new ontology and
 * SQLite schema are ready. Keep both API response shapes stable.
 */
export function getMockGraph(): DemoGraphData {
  return { ...graph, live } as DemoGraphData;
}

function tally(values: string[]): DemoSeries[] {
  const counts = new Map<string, number>();
  for (const value of values.filter(Boolean)) counts.set(value, (counts.get(value) ?? 0) + 1);
  return [...counts].map(([label, value]) => ({ label, value })).sort((a, b) => b.value - a.value);
}

function valuesOf(record: Record<string, any>, field: string): string[] {
  const value = record[field];
  if (value === null || value === undefined) return [];
  return [...new Set((Array.isArray(value) ? value : [value]).map(String).filter(Boolean))];
}

function deltaOf(series: [number, number][]): number | null {
  if (series.length < 2) return null;
  const previous = series.at(-2)![1];
  return previous ? Math.round(((series.at(-1)![1] - previous) / previous) * 100) : null;
}

function yearSeries(records: Record<string, any>[]): [number, number][] {
  const counts = new Map<number, number>();
  for (const record of records) {
    const year = Number(record.year);
    if (year) counts.set(year, (counts.get(year) ?? 0) + 1);
  }
  return [...counts].sort((a, b) => a[0] - b[0]);
}

function projectYear(project: Record<string, any>): number | null {
  const match = String(project.project_id ?? "").match(/^(20\d{2})/);
  const year = match ? Number(match[1]) : 0;
  return year >= 2012 && year <= 2026 ? year : null;
}

export function getMockResearch(): DemoResearchData {
  const nodes = graph.nodes as Record<string, any>[];
  const projects = nodes.filter((node) => node.type === "project");
  const works = live.works as Record<string, any>[];
  const findings = live.findings as Record<string, any>[];
  const liveProjects = new Map((live.projects as Record<string, any>[]).map((project) => [String(project.id), project]));
  const accepted = (live.attributions as Record<string, any>[]).filter((item) => item.confidence === "accepted");

  const groupValues = projects.flatMap((project) =>
    String(project.wg || "Unassigned").split(",").map((value) => value.trim()).filter(Boolean),
  );

  const worksWithGroups: Record<string, any>[] = works.map((work) => ({
    ...work,
    workingGroups: [...new Set((work.projectIds ?? []).flatMap((id: string) => liveProjects.get(String(id))?.workingGroups ?? []))],
  }));

  const years = projects.map(projectYear).filter((year): year is number => year !== null);
  const yearCounts = new Map<number, number>();
  for (const year of years) yearCounts.set(year, (yearCounts.get(year) ?? 0) + 1);
  const workYearCounts = new Map<number, number>();
  for (const work of works) if (work.year) workYearCounts.set(work.year, (workYearCounts.get(work.year) ?? 0) + 1);
  const timeline = [...new Set([...yearCounts.keys(), ...workYearCounts.keys()])]
    .sort((a, b) => a - b)
    .map((year) => ({ year, projects: yearCounts.get(year) ?? 0, works: workYearCounts.get(year) ?? 0 }));

  const participants = findings.reduce((sum, finding) => sum + (typeof finding.n === "number" ? finding.n : 0), 0);
  const linkedWorkIds = new Set(accepted.map((item) => item.workId));
  const linkedWorks = works.filter((work) => linkedWorkIds.has(work.id));
  const valueSets = live.valueSets as Record<string, any>[];
  const evidence = {
    instruments: tally(worksWithGroups.flatMap((work) => valuesOf(work, "instruments"))),
    countries: tally(worksWithGroups.flatMap((work) => valuesOf(work, "countries"))),
    journals: tally(worksWithGroups.flatMap((work) => valuesOf(work, "journal"))),
    conditions: tally(worksWithGroups.flatMap((work) => valuesOf(work, "conditions"))),
    methods: tally(worksWithGroups.flatMap((work) => valuesOf(work, "methods"))),
    groups: tally(worksWithGroups.flatMap((work) => valuesOf(work, "workingGroups"))),
  };
  const coverage = {
    instruments: worksWithGroups.filter((work) => valuesOf(work, "instruments").length).length,
    countries: worksWithGroups.filter((work) => valuesOf(work, "countries").length).length,
    journals: worksWithGroups.filter((work) => valuesOf(work, "journal").length).length,
    conditions: worksWithGroups.filter((work) => valuesOf(work, "conditions").length).length,
    methods: worksWithGroups.filter((work) => valuesOf(work, "methods").length).length,
    groups: worksWithGroups.filter((work) => valuesOf(work, "workingGroups").length).length,
  };

  return {
    meta: {
      label: "Reference fixture",
      note: "Interface reference data. These figures are temporary and will be rebuilt from the new ontology.",
      updated: "2026-08-16",
    },
    portfolio: {
      projects: projects.length,
      works: works.length,
      linkedWorks: linkedWorkIds.size,
      linkedWorksDelta: deltaOf(yearSeries(linkedWorks)),
      acceptedLinks: accepted.length,
      linkedProjects: new Set(accepted.map((item) => String(item.projectId))).size,
      meanLinksPerProject: accepted.length / Math.max(1, new Set(accepted.map((item) => String(item.projectId))).size),
      findings: findings.length,
      countries: Number(graph.metadata.node_counts.country ?? 0),
      groups: tally(groupValues).length,
      authors: new Set(works.flatMap((work) => work.authors ?? [])).size,
      journals: new Set(works.map((work) => work.journal).filter(Boolean)).size,
      conditions: Number(graph.metadata.node_counts.condition ?? 0),
      methods: Number(graph.metadata.node_counts.method ?? 0),
      valueSets: valueSets.length,
      valueSetsDelta: deltaOf(yearSeries(valueSets)),
      datedProjects: years.length,
      projectsSince2012: years.filter((year) => year >= 2012).length,
      firstYear: Math.min(...years),
      lastYear: Math.max(...years),
      firstWorkYear: Math.min(...works.map((work) => work.year).filter(Boolean)),
      busiestWorkYear: [...workYearCounts].sort((a, b) => b[1] - a[1])[0]?.[0] ?? 0,
      participants,
      findingsWithSampleSize: findings.filter((finding) => typeof finding.n === "number").length,
    },
    timeline,
    coverage,
    countries: evidence.countries,
    groups: evidence.groups,
    instruments: evidence.instruments,
    journals: evidence.journals,
    conditions: evidence.conditions,
    methods: evidence.methods,
    sources: works.slice(0, 16).map((work, index) => ({
      id: String(work.id ?? `REF-${index + 1}`),
      title: String(work.title ?? work.id),
      journal: String(work.journal ?? "Journal not recorded"),
      year: Number(work.year ?? 0),
      url: work.doi ? `https://doi.org/${work.doi}` : undefined,
    })),
    questions: [
      "Which instruments show up most in the findings?",
      "Where were these studies run?",
      "Which journals published this work?",
      "Which conditions have been studied?",
      "Which methods were applied?",
      "How does the evidence split by working group?",
    ],
  };
}
