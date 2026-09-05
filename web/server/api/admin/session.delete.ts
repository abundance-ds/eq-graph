import { clearAdminSession, requireAdmin } from "../../utils/adminAuth";

export default defineEventHandler((event) => {
  requireAdmin(event);
  clearAdminSession(event);
  return { ok: true };
});
