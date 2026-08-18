import { existsSync } from "node:fs";
import { resolve } from "node:path";
import { DatabaseSync, constants as sqlite } from "node:sqlite";

export class SqlReadRejected extends Error {}

type SqlRow = Record<string, string | number | null>;

let database: DatabaseSync | undefined;

function databasePath(): string {
  const configured = process.env.NUXT_SERVING_DATABASE_PATH;
  const candidates = [
    configured,
    resolve(process.cwd(), "server/data/serving.sqlite"),
    resolve(process.cwd(), "data/serving.sqlite"),
    resolve(process.cwd(), ".output/server/data/serving.sqlite"),
  ].filter((value): value is string => Boolean(value));
  const path = candidates.find(existsSync);
  if (!path) {
    throw new Error("The EQ-Graph serving database is not available.");
  }
  return path;
}

function openDatabase(): DatabaseSync {
  if (database) return database;

  const db = new DatabaseSync(databasePath(), { readOnly: true });
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

function normalizeRow(source: Record<string, unknown>): SqlRow {
  return Object.fromEntries(
    Object.entries(source).map(([key, value]) => [key, typeof value === "bigint" ? Number(value) : value]),
  ) as SqlRow;
}

export function queryServingRows<T extends SqlRow = SqlRow>(sql: string): T[] {
  const statement = openDatabase().prepare(sql);
  return [...statement.iterate()].map((row) => normalizeRow(row as Record<string, unknown>) as T);
}

export function queryServingSql(sql: string): {
  columns: string[];
  rows: SqlRow[];
  rowCount: number;
  truncated: boolean;
  elapsedMs: number;
} {
  const value = sql.trim();
  if (!value) throw new SqlReadRejected("Write one SQL query.");
  if (!/^(SELECT|WITH)\b/i.test(value)) throw new SqlReadRejected("Use one SELECT or WITH query.");

  const started = performance.now();
  try {
    const statement = openDatabase().prepare(value);
    const columns = statement.columns().map((column) => column.name);
    if (!columns.length) throw new SqlReadRejected("The query must return columns.");

    const rows: SqlRow[] = [];
    let rowCount = 0;
    for (const source of statement.iterate() as Iterable<Record<string, unknown>>) {
      rowCount += 1;
      if (rows.length < 200) rows.push(normalizeRow(source));
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

export function getServingStatus() {
  return queryServingRows(`
    SELECT
      (SELECT COUNT(*) FROM projects) AS projects,
      (SELECT COUNT(*) FROM publications) AS works,
      (SELECT COUNT(*) FROM studies) AS studies,
      (SELECT COUNT(*) FROM project_publications) AS acceptedAttributions,
      (SELECT COUNT(DISTINCT publication_id) FROM findings) AS worksWithFindings,
      (SELECT COUNT(*) FROM findings) AS findings
  `)[0]!;
}
