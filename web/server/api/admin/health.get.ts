import { basename } from "node:path";
import { realpathSync } from "node:fs";
import { requireAdmin } from "../../utils/adminAuth";
import { analyticsStore } from "../../utils/analyticsStore";
import { chatUsage } from "../../utils/chatUsage";
import { getServingStatus } from "../../utils/servingSqlite";

export default defineEventHandler((event) => {
  requireAdmin(event);
  return {
    ok: true,
    checkedAt: new Date().toISOString(),
    release: basename(realpathSync(process.cwd())),
    uptimeSeconds: Math.round(process.uptime()),
    model: useRuntimeConfig(event).agentModel,
    usage: chatUsage.snapshot(),
    data: getServingStatus(),
    analytics: analyticsStore().health(),
  };
});
