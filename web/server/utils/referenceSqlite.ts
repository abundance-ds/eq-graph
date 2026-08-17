import { DatabaseSync, constants as sqlite } from "node:sqlite";
import graph from "../data/reference-graph.json";
import live from "../data/reference-live.json";

export class SqlReadRejected extends Error {}

type Row = Record<string, string | number | null>;

let database: DatabaseSync | undefined;

function yearFromProjectId(value: unknown): number | null {
  const match = String(value ?? "").match(/^(20\d{2})/);
  return match ? Number(match[1]) : null;
}

function openDatabase(): DatabaseSync {
  if (database) return database;

  const db = new DatabaseSync(":memory:");
  db.exec(`
    PRAGMA journal_mode = MEMORY;
    PRAGMA synchronous = OFF;

    CREATE TABLE projects (
      project_id TEXT PRIMARY KEY,
      title TEXT NOT NULL,
      principal_investigator TEXT,
      working_groups TEXT,
      project_type TEXT,
      population_type TEXT,
      sample_size INTEGER,
      key_finding TEXT,
      abstract TEXT,
      start_year INTEGER,
      status TEXT,
      budget_eur REAL
    );

    CREATE TABLE project_topics (
      project_id TEXT NOT NULL,
      topic_type TEXT NOT NULL,
      topic TEXT NOT NULL
    );

    CREATE TABLE works (
      work_id TEXT PRIMARY KEY,
      title TEXT NOT NULL,
      year INTEGER,
      journal TEXT,
      doi TEXT,
      finding_count INTEGER NOT NULL DEFAULT 0
    );

    CREATE TABLE work_topics (
      work_id TEXT NOT NULL,
      topic_type TEXT NOT NULL,
      topic TEXT NOT NULL
    );

    CREATE TABLE attributions (
      attribution_id TEXT PRIMARY KEY,
      project_id TEXT NOT NULL,
      work_id TEXT NOT NULL,
      confidence TEXT NOT NULL,
      score REAL,
      sources TEXT
    );

    CREATE TABLE findings (
      finding_id TEXT PRIMARY KEY,
      work_id TEXT NOT NULL,
      year INTEGER,
      metric TEXT,
      value REAL,
      sample_size INTEGER,
      statement TEXT NOT NULL,
      direction TEXT
    );

    CREATE TABLE finding_topics (
      finding_id TEXT NOT NULL,
      topic_type TEXT NOT NULL,
      topic TEXT NOT NULL
    );

    CREATE TABLE value_sets (
      value_set_id TEXT PRIMARY KEY,
      label TEXT,
      year INTEGER,
      technique TEXT,
      respondent_count INTEGER,
      minimum_value REAL,
      instrument TEXT,
      country TEXT
    );

    CREATE TABLE coefficients (
      value_set_id TEXT NOT NULL,
      dimension TEXT,
      dimension_name TEXT,
      level INTEGER,
      value REAL
    );

    CREATE INDEX project_topics_lookup ON project_topics(topic_type, topic);
    CREATE INDEX work_topics_lookup ON work_topics(topic_type, topic);
    CREATE INDEX attribution_project ON attributions(project_id, confidence);
    CREATE INDEX attribution_work ON attributions(work_id, confidence);
    CREATE INDEX finding_work ON findings(work_id);
    CREATE INDEX finding_topics_lookup ON finding_topics(topic_type, topic);
  `);

  const liveProject = new Map((live.projects as Record<string, any>[]).map((item) => [String(item.id), item]));
  const nodeById = new Map((graph.nodes as Record<string, any>[]).map((node) => [String(node.id), node]));
  const projects = (graph.nodes as Record<string, any>[]).filter((node) => node.type === "project");

  const insertProject = db.prepare(`
    INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);
  const insertProjectTopic = db.prepare("INSERT INTO project_topics VALUES (?, ?, ?)");
  const insertWork = db.prepare("INSERT INTO works VALUES (?, ?, ?, ?, ?, ?)");
  const insertWorkTopic = db.prepare("INSERT INTO work_topics VALUES (?, ?, ?)");
  const insertAttribution = db.prepare("INSERT INTO attributions VALUES (?, ?, ?, ?, ?, ?)");
  const insertFinding = db.prepare("INSERT INTO findings VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
  const insertFindingTopic = db.prepare("INSERT INTO finding_topics VALUES (?, ?, ?)");
  const insertValueSet = db.prepare("INSERT INTO value_sets VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
  const insertCoefficient = db.prepare("INSERT INTO coefficients VALUES (?, ?, ?, ?, ?)");

  db.exec("BEGIN");
  try {
    for (const project of projects) {
      const current = liveProject.get(String(project.project_id));
      insertProject.run(
        String(project.project_id), String(project.title ?? project.label ?? project.project_id),
        String(project.pi ?? current?.pi ?? "") || null, String(project.wg ?? current?.workingGroups?.join(", ") ?? "") || null,
        String(project.project_type ?? current?.researchType ?? "") || null, String(project.population_type ?? "") || null,
        project.sample_size ?? null, project.key_finding ?? null, project.abstract_snippet ?? null,
        current?.startYear ?? yearFromProjectId(project.project_id), current?.status ?? null, current?.budgetEur ?? null,
      );
    }

    const topicTypes: Record<string, string> = {
      USES_INSTRUMENT: "instrument",
      CONDUCTED_IN: "country",
      USES_METHOD: "method",
      BELONGS_TO: "working_group",
      STUDIES_CONDITION: "condition",
      PI_OF: "researcher",
    };
    for (const edge of graph.edges as Record<string, any>[]) {
      const topicType = topicTypes[String(edge.type)];
      const source = nodeById.get(String(edge.source));
      const target = nodeById.get(String(edge.target));
      if (!topicType || source?.type !== "project" || !target?.label) continue;
      insertProjectTopic.run(String(source.project_id), topicType, String(target.label));
    }

    for (const work of live.works as Record<string, any>[]) {
      insertWork.run(String(work.id), String(work.title ?? work.id), work.year ?? null, work.journal ?? null, work.doi ?? null, work.findingCount ?? 0);
      const fields: Record<string, string> = {
        instruments: "instrument", methods: "method", countries: "country",
        conditions: "condition", authors: "author",
      };
      for (const [field, topicType] of Object.entries(fields)) {
        for (const value of new Set<string>((work[field] ?? []).map(String))) insertWorkTopic.run(String(work.id), topicType, value);
      }
    }

    for (const item of live.attributions as Record<string, any>[]) {
      insertAttribution.run(String(item.id), String(item.projectId), String(item.workId), String(item.confidence), item.score ?? null, JSON.stringify(item.sources ?? []));
    }

    for (const finding of live.findings as Record<string, any>[]) {
      insertFinding.run(
        String(finding.id), String(finding.workId), finding.year ?? null, finding.metric ?? null,
        finding.value ?? null, finding.n ?? null, String(finding.statement ?? ""), finding.direction ?? null,
      );
      for (const value of new Set<string>((finding.instruments ?? []).map(String))) insertFindingTopic.run(String(finding.id), "instrument", value);
      for (const value of new Set<string>((finding.methods ?? []).map(String))) insertFindingTopic.run(String(finding.id), "method", value);
    }

    for (const item of live.valueSets as Record<string, any>[]) {
      insertValueSet.run(
        String(item.id), item.label ?? null, item.year ?? null, item.technique ?? null,
        item.nRespondents ?? null, item.minimumValue ?? null, item.instrument ?? null, item.country ?? null,
      );
    }
    for (const item of live.coefficients as Record<string, any>[]) {
      insertCoefficient.run(item.valueSetId, item.dimension ?? null, item.dimensionName ?? null, item.level ?? null, item.value ?? null);
    }
    db.exec("COMMIT");
  } catch (error) {
    db.exec("ROLLBACK");
    db.close();
    throw error;
  }

  // This is the only policy boundary. The connection accepts reads and SQL
  // functions. SQLite rejects every write, schema change, and PRAGMA action.
  db.exec("PRAGMA query_only = ON");
  db.enableDefensive(true);
  const allowed = new Set([
    sqlite.SQLITE_SELECT,
    sqlite.SQLITE_READ,
    sqlite.SQLITE_FUNCTION,
    sqlite.SQLITE_RECURSIVE,
  ]);
  db.setAuthorizer((action) => allowed.has(action) ? sqlite.SQLITE_OK : sqlite.SQLITE_DENY);

  database = db;
  return db;
}

export function queryReferenceSql(sql: string): {
  columns: string[];
  rows: Row[];
  rowCount: number;
  truncated: boolean;
  elapsedMs: number;
} {
  const value = sql.trim();
  if (!value) throw new SqlReadRejected("Write one SQL query.");

  const started = performance.now();
  try {
    const statement = openDatabase().prepare(value);
    const columns = statement.columns().map((column) => column.name);
    if (!columns.length) throw new SqlReadRejected("The query must return columns.");

    const rows: Row[] = [];
    let rowCount = 0;
    for (const source of statement.iterate() as Iterable<Record<string, unknown>>) {
      rowCount += 1;
      if (rows.length < 200) {
        rows.push(Object.fromEntries(Object.entries(source).map(([key, item]) => [key, typeof item === "bigint" ? Number(item) : item])) as Row);
      }
    }
    return {
      columns,
      rows,
      rowCount,
      truncated: rowCount > rows.length,
      elapsedMs: Math.round((performance.now() - started) * 10) / 10,
    };
  } catch (error) {
    if (error instanceof SqlReadRejected) throw error;
    throw new SqlReadRejected(error instanceof Error ? error.message : String(error));
  }
}

export function getReferenceStatus() {
  const result = queryReferenceSql(`
    SELECT
      (SELECT COUNT(*) FROM projects) AS projects,
      (SELECT COUNT(*) FROM works) AS works,
      (SELECT COUNT(*) FROM attributions WHERE confidence = 'accepted') AS acceptedAttributions,
      (SELECT COUNT(DISTINCT work_id) FROM findings) AS worksWithFindings,
      (SELECT COUNT(*) FROM findings) AS findings
  `);
  return result.rows[0]!;
}
