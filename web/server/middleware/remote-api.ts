import { proxyRequest } from "h3";

const remoteOrigin = process.env.EQ_REMOTE_API_ORIGIN?.replace(/\/$/, "");

export default defineEventHandler((event) => {
  if (!import.meta.dev || !remoteOrigin || !event.path.startsWith("/api/")) return;

  const target = new URL(event.path, `${remoteOrigin}/`).toString();
  return proxyRequest(event, target, {
    filterHeaders: ["cookie", "authorization"],
  });
});
