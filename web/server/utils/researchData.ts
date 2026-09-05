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

const studyFamilyLabels: Record<string, string> = {
  APPLIED_USE_RESEARCH: "Applied use",
  CONCEPTUAL_FRAMEWORK_DEVELOPMENT: "Conceptual frameworks",
  ECONOMIC_BURDEN_RESEARCH: "Economic burden",
  EVIDENCE_SYNTHESIS: "Evidence synthesis",
  HEALTH_ECONOMIC_EVALUATION: "Economic evaluation",
  HEALTH_OUTCOME_RESEARCH: "Health outcomes",
  HEALTH_PREFERENCE_RESEARCH: "Health preferences",
  INSTRUMENT_VERSION_DEVELOPMENT: "Instrument development",
  MEASUREMENT_PROPERTY_EVALUATION: "Measurement properties",
  METHODS_RESEARCH: "Methods research",
  POPULATION_REFERENCE_DESCRIPTION: "Population reference",
  VALUE_SET_DEVELOPMENT: "Value-set development",
};

const researchQuestions = [
  "Which countries in Europe have an EQ-5D-5L value set?",
  "How have participant sample sizes changed over time?",
  "How have EuroQol project budgets changed over time?",
  "Who is asked to value child health states?",
  "How long does funded research take to reach publication?",
  "How many psychometric studies are published each year?",
  "Which psychometric properties are studied most often?",
  "What EQ-5D bolt-on dimensions have been studied?",
  "How has EQ-HWB research expanded over time?",
];

function coauthorshipData(): DemoGraphData["live"]["coauthorship"] {
  const nodes = queryServingRows(`
    WITH paper_counts AS (
      SELECT pa.person_id, COUNT(DISTINCT pa.publication_id) AS paper_count
      FROM publication_authors pa
      JOIN people pe USING(person_id)
      WHERE pa.resolution_status='ACCEPTED' AND pe.entity_kind='PERSON'
      GROUP BY pa.person_id
    ), top_people AS (
      SELECT person_id, paper_count
      FROM paper_counts
      ORDER BY paper_count DESC, person_id
      LIMIT 220
    )
    SELECT t.person_id, pe.display_name AS name, t.paper_count,
           (SELECT COUNT(DISTINCT project_id) FROM project_people pp WHERE pp.person_id=t.person_id) AS project_count,
           (SELECT COUNT(DISTINCT project_id) FROM project_people pp WHERE pp.person_id=t.person_id AND pp.role='PRINCIPAL_INVESTIGATOR') AS led_project_count,
           (SELECT COUNT(DISTINCT pa2.person_id)
            FROM publication_authors pa1
            JOIN publication_authors pa2
              ON pa2.publication_id=pa1.publication_id AND pa2.person_id<>pa1.person_id
            JOIN people pe2 ON pe2.person_id=pa2.person_id AND pe2.entity_kind='PERSON'
            WHERE pa1.person_id=t.person_id
              AND pa1.resolution_status='ACCEPTED'
              AND pa2.resolution_status='ACCEPTED') AS coauthor_count,
           EXISTS(SELECT 1 FROM euroqol_memberships em WHERE em.person_id=t.person_id) AS euroqol_member,
           EXISTS(SELECT 1 FROM project_people pp WHERE pp.person_id=t.person_id AND pp.role='PRINCIPAL_INVESTIGATOR') AS project_leader
    FROM top_people t JOIN people pe USING(person_id)
    ORDER BY t.paper_count DESC, pe.display_name, t.person_id
  `).map((row) => ({
    person_id: String(row.person_id),
    name: String(row.name),
    paper_count: Number(row.paper_count),
    project_count: Number(row.project_count),
    led_project_count: Number(row.led_project_count),
    coauthor_count: Number(row.coauthor_count),
    euroqol_member: Boolean(row.euroqol_member),
    project_leader: Boolean(row.project_leader),
  }));
  const edges = queryServingRows(`
    WITH paper_counts AS (
      SELECT pa.person_id, COUNT(DISTINCT pa.publication_id) AS paper_count
      FROM publication_authors pa
      JOIN people pe USING(person_id)
      WHERE pa.resolution_status='ACCEPTED' AND pe.entity_kind='PERSON'
      GROUP BY pa.person_id
    ), top_people AS (
      SELECT person_id FROM paper_counts ORDER BY paper_count DESC, person_id LIMIT 220
    ), authorship AS (
      SELECT DISTINCT pa.publication_id, pa.person_id
      FROM publication_authors pa JOIN top_people tp USING(person_id)
      WHERE pa.resolution_status='ACCEPTED'
    )
    SELECT a.person_id AS source, b.person_id AS target,
           COUNT(DISTINCT a.publication_id) AS coauthored_paper_count
    FROM authorship a
    JOIN authorship b ON b.publication_id=a.publication_id AND b.person_id>a.person_id
    GROUP BY a.person_id, b.person_id
    ORDER BY coauthored_paper_count DESC, source, target
  `).map((row) => {
    const count = Number(row.coauthored_paper_count);
    return {
      source: String(row.source), target: String(row.target),
      coauthored_paper_count: count,
    };
  });
  const total = queryServingRows(`
    SELECT COUNT(DISTINCT pa.person_id) AS total
    FROM publication_authors pa JOIN people pe USING(person_id)
    WHERE pa.resolution_status='ACCEPTED' AND pe.entity_kind='PERSON'
  `)[0]!;
  return { totalResearchers: Number(total.total), nodes, edges };
}

function citationData(): DemoGraphData["live"]["citations"] {
  const totals = queryServingRows(`
    SELECT COUNT(*) AS publications, COALESCE(SUM(cited_by_count),0) AS citations,
           substr(MAX(retrieved_at),1,10) AS retrieved
    FROM publication_citations WHERE match_status='EXACT'
  `)[0]!;
  const papers = queryServingRows(`
    SELECT p.title, COALESCE(p.publication_year,0) AS year, c.cited_by_count AS citations,
           p.doi, p.canonical_url, p.journal, c.source_work_id,
           COALESCE((
             SELECT group_concat(author_name, char(31))
             FROM (
               SELECT pa.author_name
               FROM publication_authors pa
               WHERE pa.publication_id=p.publication_id
               ORDER BY pa.author_order
             )
           ), '') AS authors,
           COALESCE((
             SELECT st.study_type
             FROM studies s JOIN study_types st USING(study_id)
             WHERE s.publication_id=p.publication_id
             ORDER BY s.study_ordinal, st.study_type LIMIT 1
           ), 'OTHER') AS family
    FROM publications p JOIN publication_citations c USING(publication_id)
    WHERE c.match_status='EXACT'
    ORDER BY c.cited_by_count DESC, p.title LIMIT 12
  `).map((row) => ({
    title: String(row.title), year: Number(row.year), citations: Number(row.citations),
    group: studyFamilyLabels[String(row.family)] ?? "Other research",
    authors: String(row.authors).split("\u001f").filter(Boolean),
    journal: String(row.journal ?? ""),
    doi: String(row.doi ?? ""),
    url: String(row.canonical_url || (row.doi ? `https://doi.org/${row.doi}` : `https://openalex.org/${row.source_work_id}`)),
  }));
  return {
    source: "OpenAlex",
    retrieved: String(totals.retrieved),
    totalCitations: Number(totals.citations),
    totalPublications: Number(totals.publications),
    papers,
  };
}

function buildResearchStory(): DemoResearchData {
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
      (SELECT COUNT(DISTINCT pa.person_id) FROM publication_authors pa JOIN people pe USING(person_id) WHERE pa.resolution_status='ACCEPTED' AND pe.entity_kind='PERSON') AS authors,
      (SELECT COUNT(DISTINCT journal) FROM publications WHERE journal IS NOT NULL) AS journals,
      (SELECT COUNT(DISTINCT concept) FROM concepts) AS concepts,
      (SELECT COUNT(DISTINCT u.registry_id) FROM scientific_uses u JOIN registry_entities r USING(registry_id) WHERE u.use_type='Method' AND u.context='DIRECT_CURRENT_ACTIVITY' AND r.scope='GLOBAL') AS methods,
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
  const instruments = series("SELECT r.canonical_label AS label, COUNT(DISTINCT u.study_id) AS value FROM scientific_uses u JOIN registry_entities r USING(registry_id) WHERE u.use_type='Instrument' AND u.context IN ('DIRECT_CURRENT_ACTIVITY','CURRENT_STUDY_OBJECT') AND r.scope='GLOBAL' GROUP BY u.registry_id, r.canonical_label ORDER BY value DESC, label LIMIT 50");
  const journals = series("SELECT journal AS label, COUNT(*) AS value FROM publications WHERE journal IS NOT NULL GROUP BY journal ORDER BY value DESC, label LIMIT 50");
  const concepts = series("SELECT concept AS label, COUNT(DISTINCT study_id) AS value FROM concepts GROUP BY concept ORDER BY value DESC, label LIMIT 50");
  const methods = series("SELECT r.canonical_label AS label, COUNT(DISTINCT u.study_id) AS value FROM scientific_uses u JOIN registry_entities r USING(registry_id) WHERE u.use_type='Method' AND u.context='DIRECT_CURRENT_ACTIVITY' AND r.scope='GLOBAL' GROUP BY u.registry_id, r.canonical_label ORDER BY value DESC, label LIMIT 50");
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
      note: `The dataset contains ${Number(totals.projects).toLocaleString()} funded projects and ${Number(totals.studies).toLocaleString()} studies.`,
      updated: String(queryServingRows("SELECT substr(MAX(retrieved_at),1,10) AS updated FROM publication_citations")[0]!.updated),
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
    questions: researchQuestions,
  };
}

function buildResearchGraph(): DemoGraphData {
  const projectRows = queryServingRows(`
    SELECT project_id, working_group, start_year
    FROM projects ORDER BY project_id
  `);
  const countryNames = queryServingRows("SELECT DISTINCT country FROM study_countries ORDER BY country")
    .map((row) => String(row.country));

  const studyTypes = listsByStudy(`
    SELECT study_id, group_concat(study_type, char(31)) AS joined_values
    FROM (SELECT study_id, study_type FROM study_types ORDER BY study_id, study_type)
    GROUP BY study_id
  `);
  const instrumentsByStudy = listsByStudy(`
    SELECT study_id, group_concat(instrument, char(31)) AS joined_values
    FROM (
      SELECT DISTINCT u.study_id, r.canonical_label AS instrument
      FROM scientific_uses u JOIN registry_entities r USING(registry_id)
      WHERE u.use_type='Instrument' AND u.context IN ('DIRECT_CURRENT_ACTIVITY','CURRENT_STUDY_OBJECT') AND r.scope='GLOBAL'
      ORDER BY study_id, instrument
    )
    GROUP BY study_id
  `);
  const countriesByStudy = listsByStudy(`
    SELECT study_id, group_concat(country, char(31)) AS joined_values
    FROM (SELECT DISTINCT study_id, country FROM study_countries ORDER BY study_id, country)
    GROUP BY study_id
  `);
  const studyRows = queryServingRows(`
    SELECT s.study_id, p.publication_year,
           (SELECT COUNT(*) FROM findings f WHERE f.study_id=s.study_id) AS finding_count
    FROM studies s JOIN publications p ON p.publication_id=s.publication_id
    ORDER BY p.publication_year, s.study_id
  `);
  const nodes: Record<string, unknown>[] = [
    ...projectRows.map((row) => ({
      id: `project:${row.project_id}`, type: "project", wg: row.working_group, start_year: row.start_year,
    })),
    ...studyRows.map((row) => {
      const id = String(row.study_id);
      return {
        id: `study:${id}`, type: "study", year: row.publication_year,
        studyTypes: studyTypes.get(id) ?? [], instruments: instrumentsByStudy.get(id) ?? [],
        countries: countriesByStudy.get(id) ?? [], findingCount: Number(row.finding_count),
      };
    }),
    ...countryNames.map((country) => ({ id: `country:${slug(country)}`, type: "country", label: country })),
  ];
  const edges: Record<string, unknown>[] = [];
  const meta = queryServingRows(`
    SELECT
      (SELECT COUNT(DISTINCT concept) FROM concepts) AS concepts,
      (SELECT COUNT(DISTINCT u.registry_id) FROM scientific_uses u JOIN registry_entities r USING(registry_id) WHERE u.use_type='Method' AND u.context='DIRECT_CURRENT_ACTIVITY' AND r.scope='GLOBAL') AS methods,
      (SELECT COUNT(DISTINCT study_type) FROM study_types) AS study_types,
      (SELECT COUNT(DISTINCT u.registry_id) FROM scientific_uses u JOIN registry_entities r USING(registry_id) WHERE u.use_type='Instrument' AND u.context IN ('DIRECT_CURRENT_ACTIVITY','CURRENT_STUDY_OBJECT') AND r.scope='GLOBAL') AS instruments,
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
        valueSetProducts: Number(meta.value_set_products),
      },
      projectEvidence: {
        projectsWithPublications: Number(meta.projects_with_publications),
        publicationsWithProjects: Number(meta.publications_with_projects),
        links: Number(meta.project_publication_links),
      },
      series: {
        studyTypes: series("SELECT study_type AS label, COUNT(DISTINCT study_id) AS value FROM study_types GROUP BY study_type ORDER BY value DESC, label LIMIT 12"),
        instruments: series("SELECT r.canonical_label AS label, COUNT(DISTINCT u.study_id) AS value FROM scientific_uses u JOIN registry_entities r USING(registry_id) WHERE u.use_type='Instrument' AND u.context IN ('DIRECT_CURRENT_ACTIVITY','CURRENT_STUDY_OBJECT') AND r.scope='GLOBAL' GROUP BY u.registry_id, r.canonical_label ORDER BY value DESC, label LIMIT 12"),
        methods: series("SELECT r.canonical_label AS label, COUNT(DISTINCT u.study_id) AS value FROM scientific_uses u JOIN registry_entities r USING(registry_id) WHERE u.use_type='Method' AND u.context='DIRECT_CURRENT_ACTIVITY' AND r.scope='GLOBAL' GROUP BY u.registry_id, r.canonical_label ORDER BY value DESC, label LIMIT 12"),
        countries: series("SELECT country AS label, COUNT(DISTINCT study_id) AS value FROM study_countries GROUP BY country ORDER BY value DESC, label LIMIT 12"),
      },
      scope: "The story moves from funded projects to the studies, methods, findings, and products that shape EuroQol research.",
      questions: researchQuestions,
    },
    live: {
      coauthorship: coauthorshipData(),
      citations: citationData(),
    },
  };
}

let storyCache: DemoResearchData | undefined;
let graphCache: DemoGraphData | undefined;

export function getResearchStory(): DemoResearchData {
  storyCache ??= buildResearchStory();
  return storyCache;
}

export function getResearchGraph(): DemoGraphData {
  graphCache ??= buildResearchGraph();
  return graphCache;
}
