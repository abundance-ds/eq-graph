/**
 * The Neo4j connection and the read guards.
 *
 * Community Edition has no roles, so the application cannot use a read-only
 * database account. These guards do that work instead:
 *
 *   1. Every query runs in a read transaction. The server refuses a write.
 *   2. The runner inspects the EXPLAIN plan and rejects a write operator.
 *      A plan is reliable. A regular expression on the query text is not,
 *      because it loses against comments, string literals and Unicode.
 *   3. A procedure runs only if the allowlist holds its name.
 *   4. One statement for each call.
 *   5. A transaction timeout and a row cap.
 */
import neo4j, { type Driver, type Record as Neo4jRecord } from "neo4j-driver";

let driver: Driver | undefined;

export function getDriver(): Driver {
  if (!driver) {
    const config = useRuntimeConfig();
    driver = neo4j.driver(
      config.neo4jUri,
      neo4j.auth.basic(config.neo4jUser, config.neo4jPassword),
      { disableLosslessIntegers: true },
    );
  }
  return driver;
}

/** An operator that changes the database. The plan must hold none of these. */
const WRITE_OPERATOR = /^(Create|Merge|Delete|DetachDelete|Set|Remove|Foreach|LoadCSV)/;

/** The procedures that a query may call. */
const PROCEDURE_ALLOWLIST = new Set([
  "db.index.fulltext.queryNodes",
  "db.index.fulltext.queryRelationships",
]);

export class CypherRejected extends Error {}

/** Removes the comments, then counts the statements. */
function countStatements(cypher: string): number {
  const withoutComments = cypher
    .replace(/\/\*[\s\S]*?\*\//g, " ")
    .split("\n")
    .map((line) => line.replace(/\/\/.*$/, ""))
    .join("\n");
  return withoutComments.split(";").filter((s) => s.trim().length > 0).length;
}

type PlanNode = {
  operatorType: string;
  arguments?: Record<string, unknown>;
  children?: PlanNode[];
};

function walkPlan(plan: PlanNode, visit: (node: PlanNode) => void) {
  visit(plan);
  for (const child of plan.children ?? []) walkPlan(child, visit);
}

/** Converts a driver value into a value that JSON accepts. */
function toPlain(value: unknown): unknown {
  if (value === null || value === undefined) return null;
  if (neo4j.isInt(value)) return (value as any).toNumber();
  if (Array.isArray(value)) return value.map(toPlain);
  if (neo4j.types.Node.prototype.isPrototypeOf(value as object)) {
    const node = value as any;
    return { _labels: node.labels, ...mapValues(node.properties) };
  }
  if (neo4j.types.Relationship.prototype.isPrototypeOf(value as object)) {
    const rel = value as any;
    return { _type: rel.type, ...mapValues(rel.properties) };
  }
  if (
    neo4j.isDate(value) ||
    neo4j.isDateTime(value) ||
    neo4j.isLocalDateTime(value) ||
    neo4j.isDuration(value)
  ) {
    return value.toString();
  }
  if (typeof value === "object") return mapValues(value as Record<string, unknown>);
  return value;
}

function mapValues(input: Record<string, unknown>): Record<string, unknown> {
  const output: Record<string, unknown> = {};
  for (const [key, value] of Object.entries(input)) output[key] = toPlain(value);
  return output;
}

export type CypherResult = {
  columns: string[];
  rows: Record<string, unknown>[];
  rowCount: number;
  truncated: boolean;
  elapsedMs: number;
  warnings: string[];
};

/**
 * Checks a query, then runs it in a read transaction.
 * Throws CypherRejected when a guard refuses the query.
 */
export async function runReadCypher(
  cypher: string,
  params: Record<string, unknown> = {},
): Promise<CypherResult> {
  const config = useRuntimeConfig();
  const rowCap = Number(config.cypherRowCap);
  const timeout = Number(config.cypherTimeoutMs);

  if (countStatements(cypher) > 1) {
    throw new CypherRejected("Send one statement for each call.");
  }

  const session = getDriver().session({ defaultAccessMode: neo4j.session.READ });
  const warnings: string[] = [];
  const startedAt = Date.now();

  try {
    // Step 1. Plan the query, and read the plan. EXPLAIN executes nothing.
    const explained = await session.run(`EXPLAIN ${cypher}`, params);
    const plan = explained.summary.plan as unknown as PlanNode | undefined;
    if (!plan) throw new CypherRejected("Neo4j returned no plan for this query.");

    walkPlan(plan, (node) => {
      if (WRITE_OPERATOR.test(node.operatorType)) {
        throw new CypherRejected(
          `This query writes to the database (${node.operatorType}). Only a read is allowed.`,
        );
      }
      if (node.operatorType === "ProcedureCall") {
        const signature = String(node.arguments?.["Details"] ?? "");
        const name = signature.match(/([\w.]+)\s*\(/)?.[1] ?? signature;
        if (!PROCEDURE_ALLOWLIST.has(name)) {
          throw new CypherRejected(`The procedure ${name} is not allowed.`);
        }
      }
      if (node.operatorType.startsWith("CartesianProduct")) {
        warnings.push(
          "The plan has a cartesian product. Add a relationship between the patterns.",
        );
      }
    });

    // Step 2. Run the query in a read transaction, with a timeout.
    const result = await session.executeRead(
      (tx) => tx.run(cypher, params),
      { timeout },
    );

    const columns = result.records[0]?.keys.map(String) ?? [];
    const truncated = result.records.length > rowCap;
    const kept: Neo4jRecord[] = truncated
      ? result.records.slice(0, rowCap)
      : result.records;

    return {
      columns,
      rows: kept.map((record) => mapValues(record.toObject())),
      rowCount: result.records.length,
      truncated,
      elapsedMs: Date.now() - startedAt,
      warnings,
    };
  } finally {
    await session.close();
  }
}
