import { z } from "zod";
import {
  recordAnalyticsSafely,
  type AnalyticsScreen,
  type DeviceClass,
} from "../utils/analyticsStore";

const screen = z.enum([
  "landing",
  "story-01",
  "story-02",
  "story-03",
  "story-04",
  "story-05",
  "story-end",
  "chat",
  "about",
]);
const viewId = z.string().uuid();
const payload = z.discriminatedUnion("type", [
  z.object({
    type: z.literal("view"),
    viewId,
    path: z.enum(["/", "/about"]),
    screen,
    device: z.enum(["mobile", "tablet", "desktop"]),
  }).strict(),
  z.object({
    type: z.literal("engagement"),
    viewId,
    screen,
    activeMs: z.number().int().min(0).max(60_000),
    maxScroll: z.number().int().min(0).max(100),
    maxStoryStep: z.number().int().min(0).max(5),
  }).strict(),
]);

export default defineEventHandler(async (event) => {
  const contentLength = Number(getRequestHeader(event, "content-length") ?? 0);
  if (contentLength > 4_096) {
    throw createError({ statusCode: 413, statusMessage: "The analytics event is too large." });
  }

  const origin = getRequestHeader(event, "origin");
  if (origin && origin !== getRequestURL(event).origin) {
    throw createError({ statusCode: 403, statusMessage: "The analytics origin is not allowed." });
  }

  const result = payload.safeParse(await readBody(event));
  if (!result.success) {
    throw createError({ statusCode: 400, statusMessage: "The analytics event is invalid." });
  }

  recordAnalyticsSafely((store) => {
    if (result.data.type === "view") {
      store.recordPageView({
        viewId: result.data.viewId,
        path: result.data.path,
        screen: result.data.screen as AnalyticsScreen,
        device: result.data.device as DeviceClass,
      });
      return;
    }
    store.recordEngagement({
      viewId: result.data.viewId,
      screen: result.data.screen as AnalyticsScreen,
      activeMs: result.data.activeMs,
      maxScroll: result.data.maxScroll,
      maxStoryStep: result.data.maxStoryStep,
    });
  });

  setResponseStatus(event, 204);
  return null;
});
