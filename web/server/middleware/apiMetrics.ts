import { recordAnalyticsSafely } from "../utils/analyticsStore";

const monitoredRoutes = new Set([
  "/api/story",
  "/api/graph",
  "/api/graph/status",
  "/api/chat",
]);

export default defineEventHandler((event) => {
  const route = getRequestURL(event).pathname;
  if (!monitoredRoutes.has(route)) return;

  const started = performance.now();
  event.node.res.once("finish", () => {
    recordAnalyticsSafely((store) => {
      store.recordApiRequest(
        route,
        event.node.req.method ?? "GET",
        event.node.res.statusCode,
        performance.now() - started,
      );
    });
  });
});
