/**
 * The result store.
 *
 * The run_cypher tool keeps each result set here under a short identifier. The
 * render tool then reads the rows by that identifier.
 *
 * This design matters. The model writes the chart encoding, and the model never
 * copies the data. That saves tokens, and it removes the transcription errors.
 *
 * The store is in memory, and one Nitro process owns it. This is correct for
 * development. Move it to Redis when the application runs on more than one
 * process.
 */
import type { CypherResult } from "./neo4j";

type Entry = { result: CypherResult; createdAt: number };

const store = new Map<string, Entry>();
const TTL_MS = 30 * 60 * 1000;
const MAX_ENTRIES = 200;

let counter = 0;

function evictOld() {
  const now = Date.now();
  for (const [id, entry] of store) {
    if (now - entry.createdAt > TTL_MS) store.delete(id);
  }
  while (store.size > MAX_ENTRIES) {
    const oldest = store.keys().next().value;
    if (oldest === undefined) break;
    store.delete(oldest);
  }
}

export function putResult(result: CypherResult): string {
  evictOld();
  counter += 1;
  const id = `r${counter}`;
  store.set(id, { result, createdAt: Date.now() });
  return id;
}

export function getResult(id: string): CypherResult | undefined {
  return store.get(id)?.result;
}
