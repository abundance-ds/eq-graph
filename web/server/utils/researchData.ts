import type { DemoGraphData, DemoResearchData, DemoSeries } from "../../shared/types/demo";
import { queryServingRows } from "./servingSqlite";

function series(sql: string): DemoSeries[] {
  return queryServingRows(sql).map((row) => ({ label: String(row.label), value: Number(row.value) }));
}

function listsByStudy(sql: string): Map<string, string[]> {
  const output = new Map<string, string[]>();
  for (const row of queryServingRows(sql)) {
    const studyId = String(row.study_id);
    const values = String(row.joined_values ?? "").split("\u001f").filter(Boolean);
    output.set(studyId, [...new Set(values)]);
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
      (SELECT COUNT(DISTINCT COALESCE(canonical_label,source_label)) FROM scientific_uses WHERE use_type='Method' AND context='DIRECT_CURRENT_ACTIVITY') AS methods,
      (SELECT COUNT(*) FROM research_products WHERE product_type='VALUE_SET' OR lower(product) LIKE '%value set%') AS value_sets,
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
  const instruments = series("SELECT COALESCE(canonical_label,source_label) AS label, COUNT(DISTINCT study_id) AS value FROM scientific_uses WHERE use_type='Instrument' AND context IN ('DIRECT_CURRENT_ACTIVITY','CURRENT_STUDY_OBJECT') GROUP BY label ORDER BY value DESC, label LIMIT 50");
  const journals = series("SELECT journal AS label, COUNT(*) AS value FROM publications WHERE journal IS NOT NULL GROUP BY journal ORDER BY value DESC, label LIMIT 50");
  const concepts = series("SELECT concept AS label, COUNT(DISTINCT study_id) AS value FROM concepts GROUP BY concept ORDER BY value DESC, label LIMIT 50");
  const methods = series("SELECT COALESCE(canonical_label,source_label) AS label, COUNT(DISTINCT study_id) AS value FROM scientific_uses WHERE use_type='Method' AND context='DIRECT_CURRENT_ACTIVITY' GROUP BY label ORDER BY value DESC, label LIMIT 50");
  const coverage = queryServingRows(`
    SELECT
      (SELECT COUNT(DISTINCT study_id) FROM study_countries) AS countries,
      (SELECT COUNT(DISTINCT study_id) FROM scientific_uses WHERE use_type='Instrument' AND context IN ('DIRECT_CURRENT_ACTIVITY','CURRENT_STUDY_OBJECT')) AS instruments,
      (SELECT COUNT(DISTINCT study_id) FROM concepts) AS concepts,
      (SELECT COUNT(DISTINCT study_id) FROM scientific_uses WHERE use_type='Method' AND context='DIRECT_CURRENT_ACTIVITY') AS methods,
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
      label: "EuroQol research",
      note: `${Number(totals.projects).toLocaleString()} funded projects and ${Number(totals.studies).toLocaleString()} studies shape the EuroQol research evidence base.`,
      updated: "2026-08-21",
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
      "Which valuation studies used both cTTO and DCE?",
      "Which EQ-5D-Y studies compare self-report and proxy report?",
      "What does the research say about states worse than dead?",
      "Which instruments, versions, and languages were studied?",
      "What are the main findings and limitations?",
      "Where are the main gaps by population, country, and method?",
    ],
  };
}

export function getResearchGraph(): DemoGraphData {
  const projectRows = queryServingRows(`
    SELECT project_id, title, principal_investigator, working_group, start_year, status
    FROM projects ORDER BY project_id
  `);
  const projectsWithPublications = new Set(queryServingRows("SELECT DISTINCT project_id FROM project_publications")
    .map((row) => String(row.project_id)));
  const projectCountries = queryServingRows(`
    SELECT DISTINCT pp.project_id, sc.country
    FROM project_publications pp
    JOIN studies s ON s.publication_id=pp.publication_id
    JOIN study_countries sc ON sc.study_id=s.study_id
    ORDER BY pp.project_id, sc.country
  `);
  const studyCountryRows = queryServingRows(`
    SELECT study_id, country FROM study_countries ORDER BY study_id, country
  `);
  const countryNames = [...new Set([
    ...projectCountries.map((row) => String(row.country)),
    ...studyCountryRows.map((row) => String(row.country)),
  ])];

  const studyTypes = listsByStudy(`
    SELECT study_id, group_concat(study_type, char(31)) AS joined_values
    FROM (SELECT study_id, study_type FROM study_types ORDER BY study_id, study_type)
    GROUP BY study_id
  `);
  const instrumentsByStudy = listsByStudy(`
    SELECT study_id, group_concat(instrument, char(31)) AS joined_values
    FROM (
      SELECT DISTINCT study_id, COALESCE(canonical_label,source_label) AS instrument
      FROM scientific_uses
      WHERE use_type='Instrument' AND context IN ('DIRECT_CURRENT_ACTIVITY','CURRENT_STUDY_OBJECT')
      ORDER BY study_id, instrument
    )
    GROUP BY study_id
  `);
  const methodsByStudy = listsByStudy(`
    SELECT study_id, group_concat(method, char(31)) AS joined_values
    FROM (
      SELECT DISTINCT study_id, COALESCE(canonical_label,source_label) AS method
      FROM scientific_uses
      WHERE use_type='Method' AND context='DIRECT_CURRENT_ACTIVITY'
      ORDER BY study_id, method
    )
    GROUP BY study_id
  `);
  const conceptsByStudy = listsByStudy(`
    SELECT study_id, group_concat(concept, char(31)) AS joined_values
    FROM (SELECT DISTINCT study_id, concept FROM concepts ORDER BY study_id, concept)
    GROUP BY study_id
  `);
  const countriesByStudy = listsByStudy(`
    SELECT study_id, group_concat(country, char(31)) AS joined_values
    FROM (SELECT DISTINCT study_id, country FROM study_countries ORDER BY study_id, country)
    GROUP BY study_id
  `);
  const studiesWithProducts = new Set(queryServingRows("SELECT DISTINCT study_id FROM research_products")
    .map((row) => String(row.study_id)));
  const studiesWithValueSets = new Set(queryServingRows(`
    SELECT DISTINCT study_id FROM research_products
    WHERE product_type='VALUE_SET' OR lower(product) LIKE '%value set%'
  `).map((row) => String(row.study_id)));
  const productTypesByStudy = listsByStudy(`
    SELECT study_id, group_concat(product_type, char(31)) AS joined_values
    FROM (SELECT DISTINCT study_id, product_type FROM research_products ORDER BY study_id, product_type)
    GROUP BY study_id
  `);

  const studyRows = queryServingRows(`
    SELECT s.study_id, s.publication_id, s.label, p.title AS publication_title,
           p.publication_year, p.doi,
           (SELECT COUNT(*) FROM findings f WHERE f.study_id=s.study_id) AS finding_count,
           (SELECT COUNT(*) FROM limitations l WHERE l.study_id=s.study_id) AS limitation_count
    FROM studies s JOIN publications p ON p.publication_id=s.publication_id
    ORDER BY p.publication_year, p.title, s.study_ordinal
  `);
  const nodes: Record<string, unknown>[] = [
    ...projectRows.map((row) => ({
      id: `project:${row.project_id}`, type: "project", project_id: row.project_id, label: row.title, title: row.title,
      pi: row.principal_investigator, wg: row.working_group, start_year: row.start_year, status: row.status,
      hasPublication: projectsWithPublications.has(String(row.project_id)),
    })),
    ...studyRows.map((row) => {
      const id = String(row.study_id);
      return {
        id: `study:${id}`, study_id: id, type: "study", label: row.label,
        publication_id: row.publication_id, publication_title: row.publication_title,
        year: row.publication_year, doi: row.doi,
        studyTypes: studyTypes.get(id) ?? [], instruments: instrumentsByStudy.get(id) ?? [],
        methods: methodsByStudy.get(id) ?? [], concepts: conceptsByStudy.get(id) ?? [],
        countries: countriesByStudy.get(id) ?? [], findingCount: Number(row.finding_count),
        limitationCount: Number(row.limitation_count), hasProduct: studiesWithProducts.has(id),
        hasValueSet: studiesWithValueSets.has(id), productTypes: productTypesByStudy.get(id) ?? [],
      };
    }),
    ...countryNames.map((country) => ({ id: `country:${slug(country)}`, type: "country", label: country })),
  ];
  const edges = [
    ...projectCountries.map((row) => ({
      source: `project:${row.project_id}`, target: `country:${slug(String(row.country))}`, type: "SUPPORTED_EVIDENCE_IN",
    })),
    ...studyCountryRows.map((row) => ({
      source: `study:${row.study_id}`, target: `country:${slug(String(row.country))}`, type: "CONDUCTED_IN",
    })),
  ];
  const meta = queryServingRows(`
    SELECT
      (SELECT COUNT(DISTINCT concept) FROM concepts) AS concepts,
      (SELECT COUNT(DISTINCT COALESCE(canonical_label,source_label)) FROM scientific_uses WHERE use_type='Method' AND context='DIRECT_CURRENT_ACTIVITY') AS methods,
      (SELECT COUNT(DISTINCT study_type) FROM study_types) AS study_types,
      (SELECT COUNT(DISTINCT COALESCE(canonical_label,source_label)) FROM scientific_uses WHERE use_type='Instrument' AND context IN ('DIRECT_CURRENT_ACTIVITY','CURRENT_STUDY_OBJECT')) AS instruments,
      (SELECT COUNT(*) FROM publications) AS publications,
      (SELECT COUNT(*) FROM findings) AS findings,
      (SELECT COUNT(*) FROM limitations) AS limitations,
      (SELECT COUNT(*) FROM research_products) AS products,
      (SELECT COUNT(*) FROM research_products WHERE product_type='VALUE_SET' OR lower(product) LIKE '%value set%') AS value_set_products,
      (SELECT COUNT(DISTINCT project_id) FROM project_publications) AS projects_with_publications,
      (SELECT COUNT(DISTINCT publication_id) FROM project_publications) AS publications_with_projects,
      (SELECT COUNT(*) FROM project_publications) AS project_publication_links
  `)[0]!;

  return {
    nodes,
    edges,
    metadata: {
      node_counts: {
        project: projectRows.length, study: studyRows.length, country: countryNames.length,
        concept: Number(meta.concepts), method: Number(meta.methods),
        instrument: Number(meta.instruments), study_type: Number(meta.study_types),
      },
      evidence: {
        publications: Number(meta.publications), findings: Number(meta.findings),
        limitations: Number(meta.limitations), products: Number(meta.products),
        valueSetProducts: Number(meta.value_set_products), studiesWithProducts: studiesWithProducts.size,
        studiesWithValueSets: studiesWithValueSets.size,
      },
      projectEvidence: {
        projectsWithPublications: Number(meta.projects_with_publications),
        publicationsWithProjects: Number(meta.publications_with_projects),
        links: Number(meta.project_publication_links),
      },
      series: {
        studyTypes: series("SELECT study_type AS label, COUNT(DISTINCT study_id) AS value FROM study_types GROUP BY study_type ORDER BY value DESC, label LIMIT 12"),
        instruments: series("SELECT COALESCE(canonical_label,source_label) AS label, COUNT(DISTINCT study_id) AS value FROM scientific_uses WHERE use_type='Instrument' AND context IN ('DIRECT_CURRENT_ACTIVITY','CURRENT_STUDY_OBJECT') GROUP BY label ORDER BY value DESC, label LIMIT 12"),
        methods: series("SELECT COALESCE(canonical_label,source_label) AS label, COUNT(DISTINCT study_id) AS value FROM scientific_uses WHERE use_type='Method' AND context='DIRECT_CURRENT_ACTIVITY' GROUP BY label ORDER BY value DESC, label LIMIT 12"),
        countries: series("SELECT country AS label, COUNT(DISTINCT study_id) AS value FROM study_countries GROUP BY country ORDER BY value DESC, label LIMIT 12"),
      },
      scope: "The story moves from funded projects to the studies, methods, findings, and products that shape EuroQol research.",
    },
    live: {},
  };
}
