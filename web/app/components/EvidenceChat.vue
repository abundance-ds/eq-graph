<script setup lang="ts">
import { Chat } from "@ai-sdk/vue";
import type { UIMessage } from "ai";
import type { DemoResearchData } from "../../shared/types/demo";
import type { ChatSegment, ChatTurn } from "../types/chat";
import { analyticsViewId } from "../utils/analytics";
import {
  clearChatSessions,
  cloneMessages,
  readChatSessions,
  sessionTitle,
  writeChatSessions,
  type ChatSession,
} from "../utils/chatHistory";

const props = defineProps<{
  data: DemoResearchData;
  active?: boolean;
}>();

const emit = defineEmits<{
  "return-home": [];
  "return-story": [];
}>();

/* The server owns the curated examples, next to the data that must answer them. */
function buildQuestionPool(data: DemoResearchData): string[] {
  return [...new Set(data.questions.map((question) => question.trim()).filter(Boolean))];
}

const OPEN = "<followups>";
const CLOSE = "</followups>";
const requestProblem = ref("");
const lastQuestion = ref("");

const chat = new Chat({
  onFinish: ({ message, isAbort, isDisconnect, isError }) => {
    if (isAbort || isDisconnect || isError) return;
    if (!hasVisibleAnswer(message)) {
      requestProblem.value = "The research query finished without an answer. Try again.";
    }
  },
});
const sessions = ref<ChatSession[]>([]);
const currentSessionId = ref<string | null>(null);
const historyOpen = ref(false);
const historyNotice = ref("");

const busy = computed(() => chat.status === "submitted" || chat.status === "streaming");
const errorMessage = computed(() => requestProblem.value || chat.error?.message || "");
const canRetry = computed(() => !busy.value && Boolean(lastQuestion.value) && Boolean(errorMessage.value));

const dateFormatter = new Intl.DateTimeFormat(undefined, {
  dateStyle: "medium",
  timeStyle: "short",
});

function formatSessionDate(value: string): string {
  const date = new Date(value);
  return Number.isNaN(date.valueOf()) ? "Saved chat" : dateFormatter.format(date);
}

function createSessionId(): string {
  return crypto.randomUUID();
}

function persistCurrent(messages: UIMessage[] = chat.messages) {
  if (!import.meta.client || !currentSessionId.value || !messages.length) return;

  const now = new Date().toISOString();
  const existing = sessions.value.find((session) => session.id === currentSessionId.value);
  const savedMessages = cloneMessages(messages);
  const current: ChatSession = {
    id: currentSessionId.value,
    title: sessionTitle(savedMessages),
    createdAt: existing?.createdAt ?? now,
    updatedAt: now,
    messages: savedMessages,
  };
  const next = [current, ...sessions.value.filter((session) => session.id !== current.id)];
  const result = writeChatSessions(localStorage, next);

  if (result.saved) {
    sessions.value = result.sessions;
    historyNotice.value = "";
  } else {
    sessions.value = next;
    historyNotice.value = "This browser could not save the chat.";
  }
}

function openSession(session: ChatSession) {
  if (busy.value) return;
  persistCurrent();
  requestProblem.value = "";
  lastQuestion.value = "";
  chat.messages = cloneMessages(session.messages);
  currentSessionId.value = session.id;
  historyOpen.value = false;
}

function startNewChat() {
  if (busy.value) return;
  persistCurrent();
  requestProblem.value = "";
  lastQuestion.value = "";
  chat.messages = [];
  currentSessionId.value = null;
  historyOpen.value = false;
}

function clearHistory() {
  if (busy.value || !sessions.value.length) return;
  if (!window.confirm("Clear all saved chat history from this browser?")) return;
  if (!clearChatSessions(localStorage)) {
    historyNotice.value = "This browser could not clear the chat history.";
    return;
  }
  chat.messages = [];
  sessions.value = [];
  currentSessionId.value = null;
  historyOpen.value = false;
  historyNotice.value = "";
}

function trimPartialOpener(value: string): string {
  const max = Math.min(OPEN.length - 1, value.length);
  for (let size = max; size > 0; size -= 1) {
    if (OPEN.startsWith(value.slice(value.length - size))) return value.slice(0, value.length - size);
  }
  return value;
}

function splitFollowups(value: string): { body: string; followups: string[] } {
  const start = value.indexOf(OPEN);
  if (start === -1) return { body: trimPartialOpener(value), followups: [] };
  const rest = value.slice(start + OPEN.length);
  const end = rest.indexOf(CLOSE);
  const block = end === -1 ? rest : rest.slice(0, end);
  return {
    body: value.slice(0, start),
    followups: block.split("\n").map((line) => line.trim()).filter(Boolean),
  };
}

const followups = computed(() => {
  if (busy.value) return [];
  const last = chat.messages.at(-1);
  if (!last || last.role !== "assistant") return [];
  const text = last.parts
    .filter((part: any) => part.type === "text")
    .map((part: any) => part.text)
    .join("");
  return splitFollowups(text).followups.slice(0, 3);
});

function segments(message: any): ChatSegment[] {
  const output: ChatSegment[] = [];
  let tools: any[] | null = null;

  message.parts.forEach((part: any, index: number) => {
    const key = `${message.id}-${index}`;
    if (part.type === "text") {
      tools = null;
      const body = splitFollowups(part.text).body.trimEnd();
      if (body.trim()) output.push({ kind: "text", key, text: body });
      return;
    }
    if (typeof part.type === "string" && (part.type.startsWith("tool-") || part.type === "dynamic-tool")) {
      if (!tools) {
        tools = [];
        output.push({ kind: "tools", key, parts: tools });
      }
      tools.push(part);
      if (part.state === "output-available" && part.output?.ok && part.output?.widget) {
        tools = null;
        output.push({ kind: "widget", key: `${key}-widget`, widget: part.output.widget });
      }
    }
  });
  return output;
}

function hasVisibleAnswer(message: UIMessage): boolean {
  return segments(message).some((segment) => segment.kind === "text" || segment.kind === "widget");
}

const turns = computed<ChatTurn[]>(() => chat.messages.map((message: any) => ({
  id: message.id,
  role: message.role,
  list: segments(message),
})));

type QuestionSource = "typed" | "sample" | "followup" | "story" | "retry";

async function send(question: string, options: { newSession?: boolean; source?: QuestionSource } = {}) {
  const value = question.trim();
  if (!value || busy.value) return;
  if (options.newSession) startNewChat();
  requestProblem.value = "";
  lastQuestion.value = value;
  currentSessionId.value ??= createSessionId();

  const response = chat.sendMessage({ text: value }, {
    body: { analytics: { viewId: analyticsViewId(), source: options.source ?? "typed" } },
  });
  await nextTick();
  persistCurrent();
  try {
    await response;
  } catch {
    // The chat object exposes the request error in the workbench.
  } finally {
    persistCurrent();
  }
}

async function retry() {
  if (busy.value || !lastQuestion.value) return;
  requestProblem.value = "";
  chat.clearError();
  const last = chat.messages.at(-1);
  try {
    if (last?.role === "assistant") {
      await chat.regenerate({ messageId: last.id, body: { analytics: { viewId: analyticsViewId(), source: "retry" } } });
    } else if (last?.role === "user") {
      await chat.sendMessage(
        { text: lastQuestion.value, messageId: last.id },
        { body: { analytics: { viewId: analyticsViewId(), source: "retry" } } },
      );
    } else {
      await chat.sendMessage(
        { text: lastQuestion.value },
        { body: { analytics: { viewId: analyticsViewId(), source: "retry" } } },
      );
    }
  } catch {
    // The workbench reads the SDK error.
  } finally {
    persistCurrent();
  }
}

/* Three at a time, dealt from the pool. "Other questions" advances the window
   and wraps, so it always gives you something and never dead-ends. */
const questionPool = computed(() => buildQuestionPool(props.data));
const dealt = ref(0);
const examples = computed(() => {
  const pool = questionPool.value;
  if (!pool.length) return [];
  return Array.from({ length: Math.min(3, pool.length) }, (_, index) => pool[(dealt.value + index) % pool.length]!);
});
function reshuffle() {
  dealt.value = (dealt.value + 3) % Math.max(1, questionPool.value.length);
}

function persistBeforeUnload() {
  persistCurrent();
}

onMounted(() => {
  sessions.value = readChatSessions(localStorage);
  const latest = sessions.value[0];
  if (latest) {
    currentSessionId.value = latest.id;
    chat.messages = cloneMessages(latest.messages);
  }
  window.addEventListener("beforeunload", persistBeforeUnload);
});

onBeforeUnmount(() => {
  persistCurrent();
  window.removeEventListener("beforeunload", persistBeforeUnload);
});

defineExpose({ send });

function sendFromWorkbench(question: string, source: "typed" | "sample" | "followup") {
  void send(question, { source });
}
</script>

<template>
  <ChatWorkbench
    id="chat"
    :active="active"
    :busy="busy"
    :error="errorMessage"
    :can-retry="canRetry"
    :examples="examples"
    :followups="followups"
    :turns="turns"
    :state-key="currentSessionId ?? 'new'"
    :can-reshuffle="questionPool.length > 3"
    @back="emit('return-story')"
    @home="emit('return-home')"
    @reshuffle="reshuffle"
    @send="sendFromWorkbench"
    @retry="retry"
  >
    <template #toolbar>
      <div class="chat-session-toolbar">
        <div class="chat-session-actions">
          <button
            type="button"
            class="chat-history-toggle"
            :aria-expanded="historyOpen"
            aria-controls="chat-history-panel"
            :disabled="busy"
            @click="historyOpen = !historyOpen"
          >
            History <span>{{ sessions.length }}</span>
          </button>
          <button
            type="button"
            class="chat-new-session"
            :disabled="busy || (!currentSessionId && !chat.messages.length)"
            @click="startNewChat"
          >New chat</button>
        </div>

        <section
          v-if="historyOpen"
          id="chat-history-panel"
          class="chat-history-panel"
          aria-label="Saved chat history"
        >
          <header>
            <div>
              <h2>Saved chats</h2>
              <p>Only on this browser</p>
            </div>
            <button type="button" aria-label="Close chat history" @click="historyOpen = false">×</button>
          </header>

          <ol v-if="sessions.length" class="chat-history-list">
            <li v-for="(session, index) in sessions" :key="session.id">
              <button
                type="button"
                :class="currentSessionId === session.id && 'is-current'"
                :aria-current="currentSessionId === session.id ? 'true' : undefined"
                :disabled="busy"
                @click="openSession(session)"
              >
                <span class="chat-history-index">{{ String(index + 1).padStart(2, "0") }}</span>
                <span class="chat-history-entry">
                  <strong>{{ session.title }}</strong>
                  <time :datetime="session.updatedAt">{{ formatSessionDate(session.updatedAt) }}</time>
                </span>
              </button>
            </li>
          </ol>
          <p v-else class="chat-history-empty">Your saved chats will appear here.</p>

          <footer>
            <p v-if="historyNotice" role="status">{{ historyNotice }}</p>
            <button type="button" :disabled="busy || !sessions.length" @click="clearHistory">Clear history</button>
          </footer>
        </section>
      </div>
    </template>
  </ChatWorkbench>
</template>
