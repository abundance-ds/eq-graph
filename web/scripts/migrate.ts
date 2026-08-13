/**
 * Applies the Cypher migrations in graph/migrations, in file name order.
 *
 * The runner records each applied file on a :_Migration node. A file runs once.
 * Every statement uses IF NOT EXISTS, so a second run is still safe.
 *
 * Run: pnpm db:local:migrate
 */
import { readFileSync, readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import neo4j from "neo4j-driver";
import { localDatabaseConnection } from "./local-database";

const here = dirname(fileURLToPath(import.meta.url));
const migrationsDir = join(here, "..", "graph", "migrations");

const { uri, user, password } = localDatabaseConnection("The migration script");

/** Splits a file into statements. Removes the line comments first. */
function statements(sql: string): string[] {
  return sql
    .split("\n")
    .filter((line) => !line.trimStart().startsWith("//"))
    .join("\n")
    .split(";")
    .map((s) => s.trim())
    .filter((s) => s.length > 0);
}

async function main() {
  const driver = neo4j.driver(uri, neo4j.auth.basic(user, password));
  await driver.verifyConnectivity();

  const session = driver.session();
  try {
    await session.run(
      "CREATE CONSTRAINT migration_name_key IF NOT EXISTS " +
        "FOR (m:_Migration) REQUIRE m.name IS UNIQUE",
    );

    const applied = new Set(
      (await session.run("MATCH (m:_Migration) RETURN m.name AS name")).records.map(
        (r) => r.get("name") as string,
      ),
    );

    const files = readdirSync(migrationsDir)
      .filter((f) => f.endsWith(".cypher"))
      .sort();

    for (const file of files) {
      if (applied.has(file)) {
        console.log(`skip    ${file}`);
        continue;
      }
      const list = statements(readFileSync(join(migrationsDir, file), "utf8"));
      for (const stmt of list) {
        await session.run(stmt);
      }
      await session.run(
        "MERGE (m:_Migration {name: $name}) SET m.appliedAt = datetime()",
        { name: file },
      );
      console.log(`applied ${file}  (${list.length} statements)`);
    }
  } finally {
    await session.close();
    await driver.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
