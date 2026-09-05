import type { UIMessage } from "ai";

export const CHAT_HISTORY_KEY = "eq-graph.chat-history.v1";

const MAX_SESSIONS = 20;
const MAX_JSON_LENGTH = 2_000_000;

export type ChatSession = {
  id: string;
  title: string;
  createdAt: string;
  updatedAt: string;
  messages: UIMessage[];
};

export type ChatHistoryWrite = {
  saved: boolean;
  sessions: ChatSession[];
};

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value);
}

function isMessage(value: unknown): value is UIMessage {
  return isRecord(value)
    && typeof value.id === "string"
    && typeof value.role === "string"
    && Array.isArray(value.parts);
}

function isSession(value: unknown): value is ChatSession {
  return isRecord(value)
    && typeof value.id === "string"
    && typeof value.title === "string"
    && typeof value.createdAt === "string"
    && typeof value.updatedAt === "string"
    && Array.isArray(value.messages)
    && value.messages.every(isMessage);
}

function newestFirst(sessions: ChatSession[]): ChatSession[] {
  return [...sessions]
    .sort((left, right) => right.updatedAt.localeCompare(left.updatedAt))
    .slice(0, MAX_SESSIONS);
}

export function cloneMessages(messages: UIMessage[]): UIMessage[] {
  return JSON.parse(JSON.stringify(messages)) as UIMessage[];
}

export function sessionTitle(messages: UIMessage[]): string {
  const firstQuestion = messages.find((message) => message.role === "user");
  if (!firstQuestion) return "New chat";

  const text = firstQuestion.parts
    .filter((part): part is Extract<typeof part, { type: "text" }> => part.type === "text")
    .map((part) => part.text)
    .join(" ")
    .replace(/\s+/g, " ")
    .trim();

  if (!text) return "New chat";
  return text.length > 72 ? `${text.slice(0, 69).trimEnd()}…` : text;
}

export function readChatSessions(storage: Storage): ChatSession[] {
  try {
    const value = storage.getItem(CHAT_HISTORY_KEY);
    if (!value) return [];
    const parsed: unknown = JSON.parse(value);
    if (!Array.isArray(parsed)) return [];
    return newestFirst(parsed.filter(isSession));
  } catch {
    return [];
  }
}

export function writeChatSessions(storage: Storage, sessions: ChatSession[]): ChatHistoryWrite {
  const candidates = newestFirst(sessions);

  while (candidates.length > 1 && JSON.stringify(candidates).length > MAX_JSON_LENGTH) {
    candidates.pop();
  }

  while (candidates.length) {
    try {
      storage.setItem(CHAT_HISTORY_KEY, JSON.stringify(candidates));
      return { saved: true, sessions: candidates };
    } catch {
      if (candidates.length === 1) break;
      candidates.pop();
    }
  }

  return { saved: false, sessions: newestFirst(sessions) };
}

export function clearChatSessions(storage: Storage): boolean {
  try {
    storage.removeItem(CHAT_HISTORY_KEY);
    return true;
  } catch {
    return false;
  }
}
