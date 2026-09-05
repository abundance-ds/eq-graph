import { requireAdmin } from "../utils/adminAuth";

export default defineEventHandler((event) => {
  const path = getRequestURL(event).pathname;
  if (!path.startsWith("/api/admin/")) return;

  setResponseHeader(event, "Cache-Control", "no-store");
  setResponseHeader(event, "X-Robots-Tag", "noindex, nofollow, noarchive");
  if (path === "/api/admin/session" && event.node.req.method === "POST") return;
  requireAdmin(event);
});
