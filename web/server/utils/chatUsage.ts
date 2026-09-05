import { mkdirSync, readFileSync, renameSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";

const HOUR_MS = 60 * 60 * 1_000;
const DAY_MS = 24 * HOUR_MS;

type UsageState = {
  version: 1;
  acceptedAt: number[];
};

type LimitReason = "hour" | "day" | "concurrent";

export type ChatUsagePermit = {
  allowed: true;
  release: () => void;
} | {
  allowed: false;
  reason: LimitReason;
  statusCode: 429 | 503;
  retryAfterSeconds: number;
  message: string;
};

type ChatUsageOptions = {
  statePath: string;
  hourLimit?: number;
  dayLimit?: number;
  concurrentLimit?: number;
  now?: () => number;
};

function retryMessage(reason: Exclude<LimitReason, "concurrent">, seconds: number): string {
  const minutes = Math.max(1, Math.ceil(seconds / 60));
  const period = reason === "hour" ? "hourly" : "daily";
  return `The beta has reached its ${period} usage limit. Try again in about ${minutes} minute${minutes === 1 ? "" : "s"}.`;
}

export function createChatUsageLimiter({
  statePath,
  hourLimit = 100,
  dayLimit = 500,
  concurrentLimit = 8,
  now = Date.now,
}: ChatUsageOptions) {
  let acceptedAt: number[] | undefined;
  let active = 0;

  function load(currentTime: number): number[] {
    if (acceptedAt) return acceptedAt;
    try {
      const state = JSON.parse(readFileSync(statePath, "utf8")) as Partial<UsageState>;
      if (state.version !== 1 || !Array.isArray(state.acceptedAt)) {
        throw new Error("The chat usage state has an invalid format.");
      }
      acceptedAt = state.acceptedAt
        .filter((value) => Number.isFinite(value) && value > currentTime - DAY_MS && value <= currentTime)
        .sort((left, right) => left - right);
    } catch (error) {
      const code = (error as NodeJS.ErrnoException).code;
      if (code !== "ENOENT") throw error;
      acceptedAt = [];
    }
    return acceptedAt;
  }

  function save(): void {
    const directory = dirname(statePath);
    mkdirSync(directory, { recursive: true, mode: 0o700 });
    const temporaryPath = `${statePath}.${process.pid}.tmp`;
    const state: UsageState = { version: 1, acceptedAt: acceptedAt ?? [] };
    writeFileSync(temporaryPath, `${JSON.stringify(state)}\n`, { mode: 0o600 });
    renameSync(temporaryPath, statePath);
  }

  function acquire(): ChatUsagePermit {
    const currentTime = now();
    const timestamps = load(currentTime).filter((value) => value > currentTime - DAY_MS);
    acceptedAt = timestamps;

    if (active >= concurrentLimit) {
      return {
        allowed: false,
        reason: "concurrent",
        statusCode: 503,
        retryAfterSeconds: 15,
        message: "The beta is busy. Try again in a moment.",
      };
    }

    if (timestamps.length >= dayLimit) {
      const retryAfterSeconds = Math.max(1, Math.ceil((timestamps[timestamps.length - dayLimit]! + DAY_MS - currentTime) / 1_000));
      return {
        allowed: false,
        reason: "day",
        statusCode: 429,
        retryAfterSeconds,
        message: retryMessage("day", retryAfterSeconds),
      };
    }

    const hourStart = currentTime - HOUR_MS;
    const hourly = timestamps.filter((value) => value > hourStart);
    if (hourly.length >= hourLimit) {
      const retryAfterSeconds = Math.max(1, Math.ceil((hourly[hourly.length - hourLimit]! + HOUR_MS - currentTime) / 1_000));
      return {
        allowed: false,
        reason: "hour",
        statusCode: 429,
        retryAfterSeconds,
        message: retryMessage("hour", retryAfterSeconds),
      };
    }

    timestamps.push(currentTime);
    active += 1;
    try {
      save();
    } catch (error) {
      timestamps.pop();
      active -= 1;
      throw error;
    }

    let released = false;
    return {
      allowed: true,
      release() {
        if (released) return;
        released = true;
        active = Math.max(0, active - 1);
      },
    };
  }

  function snapshot() {
    const currentTime = now();
    const timestamps = load(currentTime).filter((value) => value > currentTime - DAY_MS);
    acceptedAt = timestamps;
    return {
      hour: timestamps.filter((value) => value > currentTime - HOUR_MS).length,
      day: timestamps.length,
      active,
      limits: { hour: hourLimit, day: dayLimit, active: concurrentLimit },
    };
  }

  return { acquire, snapshot };
}

const statePath = process.env.NUXT_CHAT_USAGE_PATH || resolve(process.cwd(), ".data/chat-usage.json");

export const chatUsage = createChatUsageLimiter({ statePath });
