import { createHmac, timingSafeEqual } from "node:crypto";

const COOKIE_NAME = "eq_admin";
const SESSION_SECONDS = 8 * 60 * 60;
type ServerEvent = NonNullable<Parameters<typeof useRuntimeConfig>[0]>;

function configuredToken(event: ServerEvent): string {
  const token = String(useRuntimeConfig(event).adminToken ?? "");
  if (token.length < 32) {
    throw createError({ statusCode: 503, statusMessage: "Admin access is not configured." });
  }
  return token;
}

function equal(left: string, right: string): boolean {
  const leftBuffer = Buffer.from(left);
  const rightBuffer = Buffer.from(right);
  return leftBuffer.length === rightBuffer.length && timingSafeEqual(leftBuffer, rightBuffer);
}

function signature(payload: string, token: string): string {
  return createHmac("sha256", token).update(payload).digest("base64url");
}

function validSession(value: string | undefined, token: string): boolean {
  if (!value) return false;
  const [payload, suppliedSignature] = value.split(".");
  if (!payload || !suppliedSignature || !equal(signature(payload, token), suppliedSignature)) return false;
  try {
    const session = JSON.parse(Buffer.from(payload, "base64url").toString("utf8")) as { expires?: number };
    return typeof session.expires === "number" && session.expires > Date.now();
  } catch {
    return false;
  }
}

function bearerToken(event: ServerEvent): string | undefined {
  const authorization = getRequestHeader(event, "authorization");
  return authorization?.startsWith("Bearer ") ? authorization.slice(7).trim() : undefined;
}

export function isAdminToken(event: ServerEvent, supplied: string): boolean {
  return equal(configuredToken(event), supplied);
}

export function requireAdmin(event: ServerEvent): void {
  const token = configuredToken(event);
  const bearer = bearerToken(event);
  const cookie = getCookie(event, COOKIE_NAME);
  if ((bearer && equal(token, bearer)) || validSession(cookie, token)) return;
  throw createError({ statusCode: 401, statusMessage: "Admin access is required." });
}

export function createAdminSession(event: ServerEvent): void {
  const token = configuredToken(event);
  const payload = Buffer.from(JSON.stringify({ expires: Date.now() + SESSION_SECONDS * 1_000 })).toString("base64url");
  setCookie(event, COOKIE_NAME, `${payload}.${signature(payload, token)}`, {
    httpOnly: true,
    secure: getRequestProtocol(event) === "https",
    sameSite: "strict",
    path: "/",
    maxAge: SESSION_SECONDS,
  });
}

export function clearAdminSession(event: ServerEvent): void {
  deleteCookie(event, COOKIE_NAME, { path: "/" });
}
