import assert from "node:assert/strict";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { createAnalyticsStore } from "./analyticsStore";

const DAY_MS = 24 * 60 * 60 * 1_000;

function temporaryStore(now: () => number) {
  const directory = mkdtempSync(join(tmpdir(), "eq-analytics-"));
  const store = createAnalyticsStore(join(directory, "analytics.sqlite"), { now });
  return {
    store,
    remove: () => {
      store.close();
      rmSync(directory, { recursive: true, force: true });
    },
  };
}

test("records unlinked page, screen, API, and chat activity", () => {
  let currentTime = Date.UTC(2026, 8, 2, 12);
  const temporary = temporaryStore(() => currentTime);
  const viewId = "a8cc4a75-fe5f-4fce-ad0f-9754ad2c4e12";
  try {
    temporary.store.recordPageView({ viewId, path: "/", screen: "landing", device: "desktop" });
    temporary.store.recordEngagement({ viewId, screen: "story-01", activeMs: 12_400, maxScroll: 61, maxStoryStep: 1 });
    temporary.store.recordEngagement({ viewId, screen: "chat", activeMs: 3_400, maxScroll: 88, maxStoryStep: 5 });
    temporary.store.recordApiRequest("/api/chat", "POST", 200, 1_470);
    temporary.store.recordApiRequest("/api/graph", "GET", 500, 40);

    const successful = temporary.store.startChat({ viewId, source: "sample", question: "Which topics grew?", model: "test-model" });
    temporary.store.finishChat(successful, {
      status: "success",
      answer: "Measurement research grew.",
      durationMs: 1_800,
      modelSteps: 3,
      toolCalls: 2,
      chartType: "bar",
    });
    currentTime += 1_000;
    const failed = temporary.store.startChat({ source: "typed", question: "A second question", model: "test-model" });
    temporary.store.finishChat(failed, { status: "error", durationMs: 9_000, errorType: "ProviderError" });

    const range = { from: currentTime - DAY_MS, to: currentTime + DAY_MS };
    const summary = temporary.store.summary(range);
    assert.deepEqual(summary.totals, {
      pageViews: 1,
      activeMs: 15_800,
      messagesSent: 2,
      responsesReceived: 1,
      chatErrors: 1,
      chatAborts: 0,
      responseP50Ms: 1_800,
      responseP95Ms: 1_800,
      apiRequests: 2,
    });
    assert.deepEqual(summary.pages, [{
      path: "/",
      views: 1,
      averageActiveMs: 15_800,
      averageScrollPct: 88,
      maximumScrollPct: 88,
    }]);
    assert.deepEqual(summary.devices, [{ device: "desktop", views: 1 }]);
    assert.equal(summary.screens.find((row) => row.screen === "story-01")?.activeMs, 12_400);
    assert.equal(summary.screens.find((row) => row.screen === "chat")?.activeMs, 3_400);
    assert.equal(summary.api.find((row) => row.route === "/api/graph")?.errors, 1);

    const chats = temporary.store.chats(range);
    assert.equal(chats.length, 2);
    assert.equal(chats[0]?.status, "error");
    assert.equal(chats[1]?.answer, "Measurement research grew.");
    const exported = temporary.store.exportRows(range);
    assert.equal(exported.pageViews.length, 1);
    assert.equal(exported.screenTime.length, 3);
    assert.equal(exported.apiRequests.length, 2);
    assert.equal(exported.chatTurns.length, 2);
  } finally {
    temporary.remove();
  }
});

test("removes chat text after 30 days and usage rows after 90 days", () => {
  let currentTime = Date.UTC(2026, 0, 1);
  const temporary = temporaryStore(() => currentTime);
  try {
    const turnId = temporary.store.startChat({ source: "typed", question: "Retained question", model: "test-model" });
    temporary.store.finishChat(turnId, { status: "success", answer: "Retained answer", durationMs: 500 });

    currentTime += 31 * DAY_MS;
    const afterContentExpiry = temporary.store.chats({ from: 0, to: currentTime + 1 });
    assert.equal(afterContentExpiry[0]?.question, null);
    assert.equal(afterContentExpiry[0]?.answer, null);

    currentTime += 60 * DAY_MS;
    assert.equal(temporary.store.chats({ from: 0, to: currentTime + 1 }).length, 0);
  } finally {
    temporary.remove();
  }
});
