import { getServingStatus } from "../../utils/servingSqlite";

export default defineEventHandler((event) => {
  setHeader(event, "Cache-Control", "no-store");
  return {
    ok: true as const,
    checkedAt: new Date().toISOString(),
    counts: getServingStatus(),
    source: "serving-sqlite" as const,
  };
});
