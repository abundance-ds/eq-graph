import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { createChatUsageLimiter } from "./chatUsage";

function temporaryState() {
  const directory = mkdtempSync(join(tmpdir(), "eq-chat-usage-"));
  return {
    path: join(directory, "usage.json"),
    remove: () => rmSync(directory, { recursive: true, force: true }),
  };
}

test("limits active requests without storing user data", () => {
  const state = temporaryState();
  try {
    const limiter = createChatUsageLimiter({
      statePath: state.path,
      concurrentLimit: 2,
    });
    const first = limiter.acquire();
    const second = limiter.acquire();
    assert.equal(first.allowed, true);
    assert.equal(second.allowed, true);

    const rejected = limiter.acquire();
    assert.equal(rejected.allowed, false);
    if (!rejected.allowed) assert.equal(rejected.reason, "concurrent");

    if (first.allowed) first.release();
    const next = limiter.acquire();
    assert.equal(next.allowed, true);
    if (second.allowed) second.release();
    if (next.allowed) next.release();

    const saved = JSON.parse(readFileSync(state.path, "utf8"));
    assert.deepEqual(Object.keys(saved).sort(), ["acceptedAt", "version"]);
    assert.equal(saved.acceptedAt.length, 3);
    assert.ok(saved.acceptedAt.every((value: unknown) => typeof value === "number"));
  } finally {
    state.remove();
  }
});

test("enforces rolling hour and day limits across restarts", () => {
  const state = temporaryState();
  let currentTime = Date.UTC(2026, 8, 2, 12);
  try {
    const options = {
      statePath: state.path,
      hourLimit: 2,
      dayLimit: 3,
      now: () => currentTime,
    };
    const limiter = createChatUsageLimiter(options);
    for (let index = 0; index < 2; index += 1) {
      const permit = limiter.acquire();
      assert.equal(permit.allowed, true);
      if (permit.allowed) permit.release();
    }

    const hourly = limiter.acquire();
    assert.equal(hourly.allowed, false);
    if (!hourly.allowed) assert.equal(hourly.reason, "hour");

    currentTime += 60 * 60 * 1_000 + 1;
    const third = limiter.acquire();
    assert.equal(third.allowed, true);
    if (third.allowed) third.release();

    const restarted = createChatUsageLimiter(options);
    const daily = restarted.acquire();
    assert.equal(daily.allowed, false);
    if (!daily.allowed) assert.equal(daily.reason, "day");

    currentTime += 24 * 60 * 60 * 1_000 + 1;
    const afterDay = restarted.acquire();
    assert.equal(afterDay.allowed, true);
    if (afterDay.allowed) afterDay.release();
  } finally {
    state.remove();
  }
});

test("rejects an unreadable state instead of resetting the budget", () => {
  const state = temporaryState();
  try {
    writeFileSync(state.path, "not json\n");
    const limiter = createChatUsageLimiter({ statePath: state.path });
    assert.throws(() => limiter.acquire());
  } finally {
    state.remove();
  }
});
