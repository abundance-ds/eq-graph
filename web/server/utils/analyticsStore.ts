import { chmodSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { randomUUID } from "node:crypto";
import { DatabaseSync } from "node:sqlite";

const DAY_MS = 24 * 60 * 60 * 1_000;
const CONTENT_RETENTION_MS = 30 * DAY_MS;
const METADATA_RETENTION_MS = 90 * DAY_MS;

export type DeviceClass = "mobile" | "tablet" | "desktop";
export type AnalyticsScreen =
  | "landing"
  | "story-01"
  | "story-02"
  | "story-03"
  | "story-04"
  | "story-05"
  | "story-end"
  | "chat"
  | "about";
export type ChatSource = "typed" | "sample" | "followup" | "story" | "retry";
export type ChatStatus = "started" | "success" | "error" | "aborted";

type PageViewInput = {
  viewId: string;
  path: "/" | "/about";
  screen: AnalyticsScreen;
  device: DeviceClass;
};

type EngagementInput = {
  viewId: string;
  screen: AnalyticsScreen;
  activeMs: number;
  maxScroll: number;
  maxStoryStep: number;
};

export type ChatStartInput = {
  viewId?: string;
  source: ChatSource;
  question: string;
  model: string;
};

export type ChatFinishInput = {
  status: Exclude<ChatStatus, "started">;
  answer?: string;
  durationMs: number;
  modelSteps?: number;
  toolCalls?: number;
  chartType?: string;
  errorType?: string;
};

type StoreOptions = {
  now?: () => number;
};

export type AnalyticsRange = { from: number; to: number };

function text(value: unknown, limit: number): string {
  return String(value ?? "").trim().slice(0, limit);
}

function number(value: unknown): number {
  return typeof value === "number" ? value : Number(value ?? 0);
}

function percentile(values: number[], fraction: number): number {
  if (!values.length) return 0;
  const sorted = [...values].sort((left, right) => left - right);
  return Math.round(sorted[Math.min(sorted.length - 1, Math.floor((sorted.length - 1) * fraction))]!);
}

export function createAnalyticsStore(path: string, { now = Date.now }: StoreOptions = {}) {
  mkdirSync(dirname(path), { recursive: true, mode: 0o700 });
  const database = new DatabaseSync(path);
  chmodSync(path, 0o600);
  database.exec("PRAGMA journal_mode = WAL");
  database.exec("PRAGMA synchronous = NORMAL");
  database.exec("PRAGMA busy_timeout = 5000");
  database.exec("PRAGMA foreign_keys = ON");
  database.exec(`
    CREATE TABLE IF NOT EXISTS page_views (
      view_id TEXT PRIMARY KEY,
      path TEXT NOT NULL,
      device_class TEXT NOT NULL,
      started_at INTEGER NOT NULL,
      last_seen_at INTEGER NOT NULL,
      active_ms INTEGER NOT NULL DEFAULT 0,
      max_scroll_pct INTEGER NOT NULL DEFAULT 0,
      max_story_step INTEGER NOT NULL DEFAULT 0
    ) STRICT;
    CREATE INDEX IF NOT EXISTS page_views_started_at ON page_views(started_at);

    CREATE TABLE IF NOT EXISTS screen_time (
      view_id TEXT NOT NULL REFERENCES page_views(view_id) ON DELETE CASCADE,
      screen TEXT NOT NULL,
      active_ms INTEGER NOT NULL DEFAULT 0,
      PRIMARY KEY (view_id, screen)
    ) STRICT;
    CREATE INDEX IF NOT EXISTS screen_time_screen ON screen_time(screen);

    CREATE TABLE IF NOT EXISTS api_requests (
      request_id INTEGER PRIMARY KEY,
      occurred_at INTEGER NOT NULL,
      route TEXT NOT NULL,
      method TEXT NOT NULL,
      status INTEGER NOT NULL,
      duration_ms INTEGER NOT NULL
    ) STRICT;
    CREATE INDEX IF NOT EXISTS api_requests_occurred_at ON api_requests(occurred_at);

    CREATE TABLE IF NOT EXISTS chat_turns (
      turn_id TEXT PRIMARY KEY,
      view_id TEXT,
      started_at INTEGER NOT NULL,
      completed_at INTEGER,
      source TEXT NOT NULL,
      question TEXT,
      answer TEXT,
      status TEXT NOT NULL,
      duration_ms INTEGER,
      model TEXT NOT NULL,
      model_steps INTEGER NOT NULL DEFAULT 0,
      tool_calls INTEGER NOT NULL DEFAULT 0,
      chart_type TEXT,
      error_type TEXT
    ) STRICT;
    CREATE INDEX IF NOT EXISTS chat_turns_started_at ON chat_turns(started_at);
  `);

  let lastCleanup = 0;

  function cleanup(): void {
    const currentTime = now();
    if (currentTime - lastCleanup < 6 * 60 * 60 * 1_000) return;
    lastCleanup = currentTime;
    database.prepare("UPDATE chat_turns SET question=NULL, answer=NULL WHERE started_at < ?").run(currentTime - CONTENT_RETENTION_MS);
    database.prepare("DELETE FROM chat_turns WHERE started_at < ?").run(currentTime - METADATA_RETENTION_MS);
    database.prepare("DELETE FROM api_requests WHERE occurred_at < ?").run(currentTime - METADATA_RETENTION_MS);
    database.prepare("DELETE FROM page_views WHERE started_at < ?").run(currentTime - METADATA_RETENTION_MS);
  }

  function recordPageView(input: PageViewInput): void {
    cleanup();
    const currentTime = now();
    database.prepare(`
      INSERT INTO page_views(view_id,path,device_class,started_at,last_seen_at)
      VALUES(?,?,?,?,?)
      ON CONFLICT(view_id) DO NOTHING
    `).run(input.viewId, input.path, input.device, currentTime, currentTime);
    database.prepare(`
      INSERT INTO screen_time(view_id,screen,active_ms) VALUES(?,?,0)
      ON CONFLICT(view_id,screen) DO NOTHING
    `).run(input.viewId, input.screen);
  }

  function recordEngagement(input: EngagementInput): void {
    cleanup();
    const activeMs = Math.max(0, Math.min(60_000, Math.round(input.activeMs)));
    const maxScroll = Math.max(0, Math.min(100, Math.round(input.maxScroll)));
    const maxStoryStep = Math.max(0, Math.min(5, Math.round(input.maxStoryStep)));
    database.prepare(`
      UPDATE page_views
      SET last_seen_at=?, active_ms=active_ms+?,
          max_scroll_pct=MAX(max_scroll_pct,?),
          max_story_step=MAX(max_story_step,?)
      WHERE view_id=?
    `).run(now(), activeMs, maxScroll, maxStoryStep, input.viewId);
    database.prepare(`
      INSERT INTO screen_time(view_id,screen,active_ms) VALUES(?,?,?)
      ON CONFLICT(view_id,screen) DO UPDATE SET active_ms=active_ms+excluded.active_ms
    `).run(input.viewId, input.screen, activeMs);
  }

  function recordApiRequest(route: string, method: string, status: number, durationMs: number): void {
    cleanup();
    database.prepare(`
      INSERT INTO api_requests(occurred_at,route,method,status,duration_ms)
      VALUES(?,?,?,?,?)
    `).run(now(), text(route, 80), text(method, 12), Math.round(status), Math.max(0, Math.round(durationMs)));
  }

  function startChat(input: ChatStartInput): string {
    cleanup();
    const turnId = randomUUID();
    database.prepare(`
      INSERT INTO chat_turns(turn_id,view_id,started_at,source,question,status,model)
      VALUES(?,?,?,?,?,'started',?)
    `).run(
      turnId,
      input.viewId ? text(input.viewId, 64) : null,
      now(),
      input.source,
      text(input.question, 2_000),
      text(input.model, 80),
    );
    return turnId;
  }

  function finishChat(turnId: string, input: ChatFinishInput): void {
    database.prepare(`
      UPDATE chat_turns
      SET completed_at=?, answer=?, status=?, duration_ms=?, model_steps=?,
          tool_calls=?, chart_type=?, error_type=?
      WHERE turn_id=? AND status='started'
    `).run(
      now(),
      input.answer ? text(input.answer, 4_000) : null,
      input.status,
      Math.max(0, Math.round(input.durationMs)),
      Math.max(0, Math.round(input.modelSteps ?? 0)),
      Math.max(0, Math.round(input.toolCalls ?? 0)),
      input.chartType ? text(input.chartType, 40) : null,
      input.errorType ? text(input.errorType, 80) : null,
      turnId,
    );
  }

  function summary(range: AnalyticsRange) {
    cleanup();
    const parameters = [range.from, range.to];
    const pages = database.prepare(`
      SELECT path, COUNT(*) AS views,
             ROUND(AVG(active_ms)) AS average_active_ms,
             ROUND(AVG(max_scroll_pct)) AS average_scroll_pct,
             MAX(max_scroll_pct) AS maximum_scroll_pct
      FROM page_views WHERE started_at>=? AND started_at<?
      GROUP BY path ORDER BY views DESC, path
    `).all(...parameters).map((row) => ({
      path: String(row.path), views: number(row.views),
      averageActiveMs: number(row.average_active_ms),
      averageScrollPct: number(row.average_scroll_pct),
      maximumScrollPct: number(row.maximum_scroll_pct),
    }));
    const screens = database.prepare(`
      SELECT screen, COUNT(*) AS views, SUM(screen_time.active_ms) AS active_ms
      FROM screen_time
      JOIN page_views USING(view_id)
      WHERE page_views.started_at>=? AND page_views.started_at<?
      GROUP BY screen ORDER BY views DESC, screen
    `).all(...parameters).map((row) => ({
      screen: String(row.screen), views: number(row.views), activeMs: number(row.active_ms),
    }));
    const devices = database.prepare(`
      SELECT device_class, COUNT(*) AS views
      FROM page_views WHERE started_at>=? AND started_at<?
      GROUP BY device_class ORDER BY views DESC
    `).all(...parameters).map((row) => ({ device: String(row.device_class), views: number(row.views) }));
    const api = database.prepare(`
      SELECT route, COUNT(*) AS requests,
             SUM(CASE WHEN status>=400 THEN 1 ELSE 0 END) AS errors,
             ROUND(AVG(duration_ms)) AS average_duration_ms
      FROM api_requests WHERE occurred_at>=? AND occurred_at<?
      GROUP BY route ORDER BY requests DESC, route
    `).all(...parameters).map((row) => ({
      route: String(row.route), requests: number(row.requests), errors: number(row.errors),
      averageDurationMs: number(row.average_duration_ms),
    }));
    const chatRows = database.prepare(`
      SELECT status,duration_ms FROM chat_turns WHERE started_at>=? AND started_at<?
    `).all(...parameters);
    const durations = chatRows
      .filter((row) => row.status === "success")
      .map((row) => number(row.duration_ms))
      .filter((value) => value > 0);
    const viewTotals = database.prepare(`
      SELECT COUNT(*) AS views, COALESCE(SUM(active_ms),0) AS active_ms
      FROM page_views WHERE started_at>=? AND started_at<?
    `).get(...parameters)!;
    const successful = chatRows.filter((row) => row.status === "success").length;
    return {
      range,
      totals: {
        pageViews: number(viewTotals.views),
        activeMs: number(viewTotals.active_ms),
        messagesSent: chatRows.length,
        responsesReceived: successful,
        chatErrors: chatRows.filter((row) => row.status === "error").length,
        chatAborts: chatRows.filter((row) => row.status === "aborted").length,
        responseP50Ms: percentile(durations, 0.5),
        responseP95Ms: percentile(durations, 0.95),
        apiRequests: api.reduce((sum, row) => sum + row.requests, 0),
      },
      pages,
      screens,
      devices,
      api,
    };
  }

  function chats(range: AnalyticsRange, limit = 100) {
    cleanup();
    return database.prepare(`
      SELECT turn_id,started_at,completed_at,source,question,answer,status,
             duration_ms,model,model_steps,tool_calls,chart_type,error_type
      FROM chat_turns WHERE started_at>=? AND started_at<?
      ORDER BY started_at DESC LIMIT ?
    `).all(range.from, range.to, Math.max(1, Math.min(500, Math.round(limit)))).map((row) => ({
      turnId: String(row.turn_id),
      startedAt: number(row.started_at),
      completedAt: row.completed_at == null ? null : number(row.completed_at),
      source: String(row.source),
      question: row.question == null ? null : String(row.question),
      answer: row.answer == null ? null : String(row.answer),
      status: String(row.status),
      durationMs: row.duration_ms == null ? null : number(row.duration_ms),
      model: String(row.model),
      modelSteps: number(row.model_steps),
      toolCalls: number(row.tool_calls),
      chartType: row.chart_type == null ? null : String(row.chart_type),
      errorType: row.error_type == null ? null : String(row.error_type),
    }));
  }

  function health() {
    cleanup();
    const lastChat = database.prepare(`
      SELECT started_at,status,duration_ms,error_type FROM chat_turns ORDER BY started_at DESC LIMIT 1
    `).get();
    const lastApiError = database.prepare(`
      SELECT occurred_at,route,status FROM api_requests WHERE status>=400 ORDER BY occurred_at DESC LIMIT 1
    `).get();
    return {
      ok: true,
      pageViews: number(database.prepare("SELECT COUNT(*) AS count FROM page_views").get()!.count),
      chatTurns: number(database.prepare("SELECT COUNT(*) AS count FROM chat_turns").get()!.count),
      apiRequests: number(database.prepare("SELECT COUNT(*) AS count FROM api_requests").get()!.count),
      lastChat: lastChat ?? null,
      lastApiError: lastApiError ?? null,
    };
  }

  function exportRows(range: AnalyticsRange) {
    cleanup();
    const pageViews = database.prepare("SELECT * FROM page_views WHERE started_at>=? AND started_at<? ORDER BY started_at").all(range.from, range.to);
    const screenTime = database.prepare(`
      SELECT screen_time.* FROM screen_time JOIN page_views USING(view_id)
      WHERE page_views.started_at>=? AND page_views.started_at<? ORDER BY page_views.started_at,screen
    `).all(range.from, range.to);
    const apiRequests = database.prepare("SELECT * FROM api_requests WHERE occurred_at>=? AND occurred_at<? ORDER BY occurred_at").all(range.from, range.to);
    const chatTurns = database.prepare("SELECT * FROM chat_turns WHERE started_at>=? AND started_at<? ORDER BY started_at").all(range.from, range.to);
    return { pageViews, screenTime, apiRequests, chatTurns };
  }

  function close(): void {
    database.close();
  }

  return { recordPageView, recordEngagement, recordApiRequest, startChat, finishChat, summary, chats, health, exportRows, close };
}

let singleton: ReturnType<typeof createAnalyticsStore> | undefined;
let warned = false;

export function analyticsStore() {
  singleton ??= createAnalyticsStore(
    process.env.NUXT_ANALYTICS_DATABASE_PATH || resolve(process.cwd(), ".data/analytics.sqlite"),
  );
  return singleton;
}

export function recordAnalyticsSafely(action: (store: ReturnType<typeof createAnalyticsStore>) => void): void {
  try {
    action(analyticsStore());
  } catch (error) {
    if (!warned) {
      warned = true;
      console.error("[analytics] Usage data could not be recorded.", error);
    }
  }
}

export function parseAnalyticsRange(from: unknown, to: unknown, currentTime = Date.now()): AnalyticsRange {
  const parsedTo = typeof to === "string" && to ? Date.parse(to) : currentTime;
  const parsedFrom = typeof from === "string" && from ? Date.parse(from) : parsedTo - 7 * DAY_MS;
  if (!Number.isFinite(parsedFrom) || !Number.isFinite(parsedTo) || parsedFrom >= parsedTo) {
    throw createError({ statusCode: 400, statusMessage: "Use a valid date range." });
  }
  if (parsedTo - parsedFrom > 366 * DAY_MS) {
    throw createError({ statusCode: 400, statusMessage: "The date range cannot exceed 366 days." });
  }
  return { from: parsedFrom, to: parsedTo };
}
