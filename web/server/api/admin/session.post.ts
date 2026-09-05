import { createAdminSession, isAdminToken } from "../../utils/adminAuth";

export default defineEventHandler(async (event) => {
  const contentLength = Number(getRequestHeader(event, "content-length") ?? 0);
  if (contentLength > 1_024) {
    throw createError({ statusCode: 413, statusMessage: "The admin request is too large." });
  }
  const body = await readBody<{ token?: unknown }>(event);
  if (typeof body?.token !== "string" || !isAdminToken(event, body.token)) {
    throw createError({ statusCode: 401, statusMessage: "The admin token is not valid." });
  }
  createAdminSession(event);
  return { ok: true };
});
