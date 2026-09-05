import { requireAdmin } from "../../utils/adminAuth";
import { analyticsStore, parseAnalyticsRange } from "../../utils/analyticsStore";

export default defineEventHandler((event) => {
  requireAdmin(event);
  const query = getQuery(event);
  const range = parseAnalyticsRange(query.from, query.to);
  const rows = analyticsStore().exportRows(range);
  const lines = [
    ...rows.pageViews.map((row) => ({ type: "page_view", ...row })),
    ...rows.screenTime.map((row) => ({ type: "screen_time", ...row })),
    ...rows.apiRequests.map((row) => ({ type: "api_request", ...row })),
    ...rows.chatTurns.map((row) => ({ type: "chat_turn", ...row })),
  ].map((row) => JSON.stringify(row)).join("\n");
  const day = new Date(range.from).toISOString().slice(0, 10);
  setResponseHeaders(event, {
    "Content-Type": "application/x-ndjson; charset=utf-8",
    "Content-Disposition": `attachment; filename="eq-graph-analytics-${day}.jsonl"`,
  });
  return `${lines}${lines ? "\n" : ""}`;
});
