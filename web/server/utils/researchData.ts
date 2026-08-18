import type { DemoGraphData, DemoResearchData, DemoSeries } from "../../shared/types/demo";
import { queryServingRows } from "./servingSqlite";

function series(sql: string): DemoSeries[] {
  return queryServingRows(sql).map((row) => ({ label: String(row.label), value: Number(row.value) }));
}

function listsByPublication(sql: string): Map<string, string[]> {
  const output = new Map<string, string[]>();
  for (const row of queryServingRows(sql)) {
    const publicationId = String(row.publication_id);
    const values = String(row.joined_values ?? "").split("\u001f").filter(Boolean);
    output.set(publicationId, [...new Set(values)]);
  }
  return output;
}

function slug(value: string): string {
  return value.toLowerCase().normalize("NFKD").replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

export function getResearchStory(): DemoResearchData {
  const totals = queryServingRows(`
    SELECT
      (SELECT COUNT(*) FROM projects) AS projects,
      (SELECT COUNT(*) FROM publications) AS works,
      (SELECT COUNT(*) FROM studies) AS studies,
      (SELECT COUNT(DISTINCT publication_id) FROM project_publications) AS linked_works,
      (SELECT COUNT(*) FROM project_publications) AS accepted_links,
      (SELECT COUNT(DISTINCT project_id) FROM project_publications) AS linked_projects,
      (SELECT COUNT(*) FROM findings) AS findings,
      (SELECT COUNT(DISTINCT country) FROM study_countries) AS countries,
      (SELECT COUNT(DISTINCT working_group) FROM projects WHERE working_group IS NOT NULL) AS groups,
      (SELECT COUNT(DISTINCT person_id) FROM publication_authors) AS authors,
      (SELECT COUNT(DISTINCT journal) FROM publications WHERE journal IS NOT NULL) AS journals,
      (SELECT COUNT(DISTINCT concept) FROM concepts) AS concepts,
      (SELECT COUNT(DISTINCT method) FROM method_uses) AS methods,
      (SELECT COUNT(*) FROM research_products WHERE lower(COALESCE(product_type,'')) LIKE '%value set%' OR lower(product) LIKE '%value set%') AS value_sets,
      (SELECT COUNT(*) FROM projects WHERE start_year IS NOT NULL) AS dated_projects,
      (SELECT COUNT(*) FROM projects WHERE start_year >= 2012) AS projects_since_2012,
      (SELECT MIN(start_year) FROM projects) AS first_year,
      (SELECT MAX(start_year) FROM projects) AS last_year,
      (SELECT MIN(publication_year) FROM publications) AS first_work_year,
      (SELECT publication_year FROM publications WHERE publication_year IS NOT NULL GROUP BY publication_year ORDER BY COUNT(*) DESC, publication_year DESC LIMIT 1) AS busiest_work_year,
      (SELECT COUNT(*) FROM samples WHERE sample_size IS NOT NULL) AS samples_with_size
  `)[0]!;

  const timeline = queryServingRows(`
    WITH years AS (
      SELECT start_year AS year, COUNT(*) AS projects, 0 AS works
      FROM projects WHERE start_year IS NOT NULL GROUP BY start_year
      UNION ALL
      SELECT publication_year AS year, 0 AS projects, COUNT(*) AS works
      FROM publications WHERE publication_year IS NOT NULL GROUP BY publication_year
    )
    SELECT year, SUM(projects) AS projects, SUM(works) AS works
    FROM years GROUP BY year ORDER BY year
  `).map((row) => ({ year: Number(row.year), projects: Number(row.projects), works: Number(row.works) }));

  const countries = series("SELECT country AS label, COUNT(DISTINCT study_id) AS value FROM study_countries GROUP BY country ORDER BY value DESC, label LIMIT 50");
  const groups = series("SELECT working_group AS label, COUNT(*) AS value FROM projects WHERE working_group IS NOT NULL GROUP BY working_group ORDER BY value DESC, label");
  const instruments = series("SELECT instrument AS label, COUNT(DISTINCT study_id) AS value FROM instrument_uses GROUP BY instrument ORDER BY value DESC, label LIMIT 50");
  const journals = series("SELECT journal AS label, COUNT(*) AS value FROM publications WHERE journal IS NOT NULL GROUP BY journal ORDER BY value DESC, label LIMIT 50");
  const concepts = series("SELECT concept AS label, COUNT(DISTINCT study_id) AS value FROM concepts GROUP BY concept ORDER BY value DESC, label LIMIT 50");
  const methods = series("SELECT method AS label, COUNT(DISTINCT study_id) AS value FROM method_uses GROUP BY method ORDER BY value DESC, label LIMIT 50");
  const coverage = queryServingRows(`
    SELECT
      (SELECT COUNT(DISTINCT study_id) FROM study_countries) AS countries,
      (SELECT COUNT(DISTINCT study_id) FROM instrument_uses) AS instruments,
      (SELECT COUNT(DISTINCT study_id) FROM concepts) AS concepts,
      (SELECT COUNT(DISTINCT study_id) FROM method_uses) AS methods,
      (SELECT COUNT(DISTINCT publication_id) FROM publications WHERE journal IS NOT NULL) AS journals,
      (SELECT COUNT(DISTINCT pp.publication_id) FROM project_publications pp JOIN projects p ON p.project_id=pp.project_id WHERE p.working_group IS NOT NULL) AS groups
  `)[0]!;
  const sources = queryServingRows(`
    SELECT publication_id AS id, title, COALESCE(journal,'Journal not recorded') AS journal,
           COALESCE(publication_year,0) AS year, canonical_url AS url
    FROM publications ORDER BY publication_year DESC, title LIMIT 16
  `).map((row) => ({
    id: String(row.id), title: String(row.title), journal: String(row.journal), year: Number(row.year),
    ...(row.url ? { url: String(row.url) } : {}),
  }));

  return {
    meta: {
      label: "Data-backed preview",
      note: "The portfolio has 1,024 projects. The current evidence layer contains 209 assessed publications and 207 study records.",
      updated: "2026-08-18",
    },
    portfolio: {
      projects: Number(totals.projects),
      works: Number(totals.works),
      studies: Number(totals.studies),
      linkedWorks: Number(totals.linked_works),
      linkedWorksDelta: null,
      acceptedLinks: Number(totals.accepted_links),
      linkedProjects: Number(totals.linked_projects),
      meanLinksPerProject: Number(totals.accepted_links) / Math.max(1, Number(totals.linked_projects)),
      findings: Number(totals.findings),
      countries: Number(totals.countries),
      groups: Number(totals.groups),
      authors: Number(totals.authors),
      journals: Number(totals.journals),
      concepts: Number(totals.concepts),
      methods: Number(totals.methods),
      valueSets: Number(totals.value_sets),
      valueSetsDelta: null,
      datedProjects: Number(totals.dated_projects),
      projectsSince2012: Number(totals.projects_since_2012),
      firstYear: Number(totals.first_year),
      lastYear: Number(totals.last_year),
      firstWorkYear: Number(totals.first_work_year),
      busiestWorkYear: Number(totals.busiest_work_year),
      participants: null,
      samplesWithSize: Number(totals.samples_with_size),
    },
    timeline,
    coverage: {
      countries: Number(coverage.countries), groups: Number(coverage.groups), instruments: Number(coverage.instruments),
      journals: Number(coverage.journals), concepts: Number(coverage.concepts), methods: Number(coverage.methods),
    },
    countries,
    groups,
    instruments,
    journals,
    concepts,
    methods,
    sources,
    questions: [
      "Which study types and valuation methods appear most often?",
      "Which instruments, versions, and administration modes were used?",
      "What populations and countries have been studied?",
      "What are the main findings and limitations?",
      "Which projects have accepted publication links?",
      "Where are the main evidence gaps?",
    ],
  };
}

export function getResearchGraph(): DemoGraphData {
  const projectRows = queryServingRows("SELECT * FROM projects ORDER BY project_id");
  const projectCountries = queryServingRows(`
    SELECT DISTINCT pp.project_id, sc.country
    FROM project_publications pp
    JOIN studies s ON s.publication_id=pp.publication_id
    JOIN study_countries sc ON sc.study_id=s.study_id
    ORDER BY pp.project_id, sc.country
  `);
  const countryNames = [...new Set(projectCountries.map((row) => String(row.country)))];
  const nodes: Record<string, unknown>[] = [
    ...projectRows.map((row) => ({
      id: `project:${row.project_id}`, type: "project", project_id: row.project_id, label: row.title, title: row.title,
      pi: row.principal_investigator, wg: row.working_group, start_year: row.start_year, status: row.status,
    })),
    ...countryNames.map((country) => ({ id: `country:${slug(country)}`, type: "country", label: country })),
  ];
  const edges = projectCountries.map((row) => ({
    source: `project:${row.project_id}`, target: `country:${slug(String(row.country))}`, type: "CONDUCTED_IN",
  }));

  const authors = listsByPublication(`
    SELECT publication_id, group_concat(author_name, char(31)) AS joined_values
    FROM (SELECT publication_id, author_name FROM publication_authors ORDER BY publication_id, author_order)
    GROUP BY publication_id
  `);
  const instruments = listsByPublication(`
    SELECT s.publication_id, group_concat(i.instrument, char(31)) AS joined_values
    FROM (SELECT DISTINCT study_id, instrument FROM instrument_uses ORDER BY instrument) i
    JOIN studies s ON s.study_id=i.study_id GROUP BY s.publication_id
  `);
  const methods = listsByPublication(`
    SELECT s.publication_id, group_concat(m.method, char(31)) AS joined_values
    FROM (SELECT DISTINCT study_id, method FROM method_uses ORDER BY method) m
    JOIN studies s ON s.study_id=m.study_id GROUP BY s.publication_id
  `);
  const countries = listsByPublication(`
    SELECT s.publication_id, group_concat(c.country, char(31)) AS joined_values
    FROM study_countries c JOIN studies s ON s.study_id=c.study_id GROUP BY s.publication_id
  `);
  const concepts = listsByPublication(`
    SELECT s.publication_id, group_concat(c.concept, char(31)) AS joined_values
    FROM concepts c JOIN studies s ON s.study_id=c.study_id GROUP BY s.publication_id
  `);
  const projectIds = listsByPublication(`
    SELECT publication_id, group_concat(project_id, char(31)) AS joined_values
    FROM project_publications GROUP BY publication_id
  `);

  const works = queryServingRows(`
    SELECT p.publication_id, p.title, p.publication_year, p.journal, p.doi,
           COUNT(DISTINCT f.finding_id) AS finding_count
    FROM publications p LEFT JOIN findings f ON f.publication_id=p.publication_id
    GROUP BY p.publication_id ORDER BY p.publication_year, p.title
  `).map((row) => {
    const id = String(row.publication_id);
    return {
      id, title: row.title, year: row.publication_year, journal: row.journal, doi: row.doi,
      findingCount: Number(row.finding_count), authors: authors.get(id) ?? [], instruments: instruments.get(id) ?? [],
      methods: methods.get(id) ?? [], countries: countries.get(id) ?? [], concepts: concepts.get(id) ?? [],
      projectIds: projectIds.get(id) ?? [],
    };
  });
  const attributions = queryServingRows("SELECT project_id, publication_id FROM project_publications ORDER BY project_id, publication_id")
    .map((row, index) => ({ id: `accepted:${index + 1}`, projectId: row.project_id, workId: row.publication_id, confidence: "accepted" }));
  const valueSets = queryServingRows(`
    SELECT rp.product_id AS id, rp.product AS label, p.publication_year AS year
    FROM research_products rp JOIN studies s ON s.study_id=rp.study_id JOIN publications p ON p.publication_id=s.publication_id
    WHERE lower(COALESCE(rp.product_type,'')) LIKE '%value set%' OR lower(rp.product) LIKE '%value set%'
    ORDER BY p.publication_year, rp.product
  `);
  const meta = queryServingRows(`
    SELECT
      (SELECT COUNT(DISTINCT concept) FROM concepts) AS concepts,
      (SELECT COUNT(DISTINCT method) FROM method_uses) AS methods,
      (SELECT COUNT(DISTINCT study_type) FROM study_types) AS study_types,
      (SELECT COUNT(*) FROM findings) AS findings
  `)[0]!;

  return {
    nodes,
    edges,
    metadata: {
      node_counts: {
        project: projectRows.length, country: countryNames.length, concept: Number(meta.concepts),
        method: Number(meta.methods), study_type: Number(meta.study_types),
      },
      scope: "Countries shown in the graph come from studies in accepted project-publication links.",
    },
    live: { works, findings: Array(Number(meta.findings)).fill(null), attributions, valueSets, coefficients: [] },
  };
}
