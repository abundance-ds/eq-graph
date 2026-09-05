import { requireAdmin } from "../../utils/adminAuth";
import { analyticsStore, parseAnalyticsRange } from "../../utils/analyticsStore";

export default defineEventHandler((event) => {
  requireAdmin(event);
  const query = getQuery(event);
  return analyticsStore().summary(parseAnalyticsRange(query.from, query.to));
});
