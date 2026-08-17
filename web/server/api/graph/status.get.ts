import { getReferenceStatus } from "../../utils/referenceSqlite";

export default defineEventHandler((event) => {
  setHeader(event, "Cache-Control", "no-store");
  return {
    ok: true as const,
    checkedAt: new Date().toISOString(),
    counts: getReferenceStatus(),
    source: "reference-sqlite" as const,
  };
});
