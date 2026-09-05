import { requireAdmin } from "../../utils/adminAuth";
import { analyticsStore, parseAnalyticsRange } from "../../utils/analyticsStore";

export default defineEventHandler((event) => {
  requireAdmin(event);
  const query = getQuery(event);
  const limit = Math.max(1, Math.min(500, Number(query.limit ?? 100)));
  const range = parseAnalyticsRange(query.from, query.to);
  return {
    range,
    chats: analyticsStore().chats(range, limit),
  };
});
