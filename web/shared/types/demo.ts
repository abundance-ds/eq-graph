export type DemoSource = {
  id: string;
  title: string;
  journal: string;
  year: number;
  url?: string;
};

export type DemoSeries = {
  label: string;
  value: number;
};

export type DemoTimelineRow = {
  year: number;
  projects: number;
  works: number;
};

export type DemoTopic = "instruments" | "countries" | "journals" | "conditions" | "methods" | "groups" | "overview";

export type DemoResearchData = {
  meta: {
    label: string;
    note: string;
    updated: string;
  };
  portfolio: {
    projects: number;
    works: number;
    linkedWorks: number;
    linkedWorksDelta: number | null;
    acceptedLinks: number;
    linkedProjects: number;
    meanLinksPerProject: number;
    findings: number;
    countries: number;
    groups: number;
    authors: number;
    journals: number;
    conditions: number;
    methods: number;
    valueSets: number;
    valueSetsDelta: number | null;
    datedProjects: number;
    projectsSince2012: number;
    firstYear: number;
    lastYear: number;
    firstWorkYear: number;
    busiestWorkYear: number;
    participants: number;
    findingsWithSampleSize: number;
  };
  timeline: DemoTimelineRow[];
  coverage: Record<Exclude<DemoTopic, "overview">, number>;
  countries: DemoSeries[];
  groups: DemoSeries[];
  instruments: DemoSeries[];
  journals: DemoSeries[];
  conditions: DemoSeries[];
  methods: DemoSeries[];
  sources: DemoSource[];
  questions: string[];
};

export type DemoGraphData = {
  nodes: Record<string, any>[];
  edges: Record<string, any>[];
  metadata: Record<string, any>;
  live: Record<string, any>;
};
