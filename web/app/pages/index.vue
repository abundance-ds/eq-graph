<script setup lang="ts">
import { Chat } from "@ai-sdk/vue";

const chat = new Chat({});
const input = ref("");
const thread = ref<HTMLElement | null>(null);

const busy = computed(() => chat.status === "submitted" || chat.status === "streaming");

function send(question?: string) {
  const value = (question ?? input.value).trim();
  if (!value || busy.value) return;
  input.value = "";
  chat.sendMessage({ text: value });
}

function onKeydown(event: KeyboardEvent) {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    send();
  }
}

// --- The follow-up block ----------------------------------------------------
// The model writes the questions inside <followups>…</followups> at the end of
// the answer. We remove the block from the visible text, and we draw the
// questions as buttons.
//
// The text arrives one token at a time. A partial opening tag, for example
// "<follo", must never reach the screen. trimPartialOpener holds back any tail
// that could still become the opening tag.

const OPEN = "<followups>";
const CLOSE = "</followups>";

function trimPartialOpener(value: string): string {
  const max = Math.min(OPEN.length - 1, value.length);
  for (let n = max; n > 0; n--) {
    if (OPEN.startsWith(value.slice(value.length - n))) return value.slice(0, value.length - n);
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

/** The questions from the last assistant message, and only when it is finished. */
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

// --- The shape of one message ----------------------------------------------
// The parts arrive in one flat list: text, tool calls, more text. We group the
// neighbouring tool calls into one activity trail, and we keep the order. So
// the work of the agent stays where it happened, between the sentences, and
// not only at the end of the answer.

type Segment =
  | { kind: "text"; key: string; text: string }
  | { kind: "widget"; key: string; widget: any }
  | { kind: "tools"; key: string; parts: any[] };

function segments(message: any): Segment[] {
  const out: Segment[] = [];
  let bucket: any[] | null = null;

  message.parts.forEach((part: any, index: number) => {
    const key = `${message.id}-${index}`;

    if (part.type === "text") {
      bucket = null;
      const body = splitFollowups(part.text).body.trimEnd();
      if (body.trim()) out.push({ kind: "text", key, text: body });
      return;
    }

    // A chart that is ready leaves the trail and becomes a block of its own.
    if (part.type === "tool-render" && part.state === "output-available" && part.output?.ok) {
      bucket = null;
      out.push({ kind: "widget", key, widget: part.output.widget });
      return;
    }

    if (typeof part.type === "string" && (part.type.startsWith("tool-") || part.type === "dynamic-tool")) {
      if (!bucket) {
        bucket = [];
        out.push({ kind: "tools", key, parts: bucket });
      }
      bucket.push(part);
    }
  });

  return out;
}

/** Every message with its segments. The template reads this list only. */
const view = computed(() =>
  chat.messages.map((message: any) => ({ message, list: segments(message) })),
);

/**
 * True when the agent works and this trail holds the newest step. The trail
 * then adds a "Thinking" row, because the agent now decides what to do next.
 */
function trailThinks(entry: { message: any; list: Segment[] }, index: number): boolean {
  if (!busy.value || entry.message.id !== view.value.at(-1)?.message.id) return false;
  if (index !== entry.list.length - 1) return false;
  const segment = entry.list[index];
  if (segment?.kind !== "tools") return false;
  return segment.parts.every(
    (part: any) => part.state === "output-available" || part.state === "output-error",
  );
}

/**
 * True when the agent works but the newest thing on the screen is not a trail:
 * the question just left, or a chart just arrived. The page then shows one
 * trail of its own, so the wait is never silent.
 */
const tailThinks = computed(() => {
  if (!busy.value) return false;
  const last = view.value.at(-1);
  if (!last) return false;
  if (last.message.role === "user") return true;
  const tail = last.list.at(-1);
  return !tail || tail.kind === "widget";
});

const EXAMPLES = [
  "How many projects has each working group reviewed?",
  "Which countries have the most value sets, and which techniques did they use?",
  "Show the number of publications for each year since 2015.",
  "Who leads the most projects?",
];

watch(
  () => chat.messages.length + (chat.messages.at(-1)?.parts.length ?? 0),
  async () => {
    await nextTick();
    thread.value?.scrollTo({ top: thread.value.scrollHeight, behavior: "smooth" });
  },
);
</script>

<template>
  <main class="page">
    <header class="head">
      <h1>eq-graph</h1>
      <p>Ask a question about the EuroQol portfolio. The data is invented, and the shape is real.</p>
    </header>

    <div ref="thread" class="thread">
      <div v-if="chat.messages.length === 0" class="empty">
        <p>Try one of these:</p>
        <button v-for="q in EXAMPLES" :key="q" class="chip" @click="send(q)">{{ q }}</button>
      </div>

      <article
        v-for="entry in view"
        :key="entry.message.id"
        :class="['msg', `msg--${entry.message.role}`]"
      >
        <template v-for="(segment, i) in entry.list" :key="segment.key">
          <p v-if="segment.kind === 'text'" class="prose">{{ segment.text }}</p>

          <GraphWidget v-else-if="segment.kind === 'widget'" :spec="segment.widget" />

          <ActivityTrail v-else :parts="segment.parts" :thinking="trailThinks(entry, i)" />
        </template>
      </article>

      <ActivityTrail v-if="tailThinks" :parts="[]" thinking />

      <p v-if="chat.error" class="trace--warn">{{ chat.error.message }}</p>
    </div>

    <div v-if="followups.length" class="followups">
      <button v-for="q in followups" :key="q" class="chip" @click="send(q)">{{ q }}</button>
    </div>

    <form class="composer" @submit.prevent="send()">
      <textarea
        v-model="input"
        rows="1"
        placeholder="Ask about projects, people, publications or value sets…"
        @keydown="onKeydown"
      />
      <button type="submit" :disabled="busy || !input.trim()">
        {{ busy ? "…" : "Ask" }}
      </button>
    </form>
  </main>
</template>

<style scoped>
.page { max-width: 46rem; margin: 0 auto; height: 100%; display: flex; flex-direction: column; padding: 1.25rem 1.25rem 1rem; }
.head { padding-bottom: 0.9rem; border-bottom: 1px solid #e9e5dd; }
.head h1 { margin: 0; font-size: 1.05rem; letter-spacing: -0.01em; }
.head p { margin: 0.2rem 0 0; font-size: 0.8rem; color: #8a847a; }

.thread { flex: 1; overflow-y: auto; padding: 1.1rem 0; }
.empty { color: #8a847a; font-size: 0.85rem; }
.empty p { margin: 0 0 0.6rem; }

.msg { margin-bottom: 1.1rem; }
.msg--user .prose {
  background: #1c1a17; color: #faf8f4; display: inline-block;
  padding: 0.5rem 0.8rem; border-radius: 12px 12px 2px 12px; margin-left: auto;
}
.msg--user { display: flex; justify-content: flex-end; }
.prose { margin: 0 0 0.5rem; line-height: 1.6; font-size: 0.9rem; white-space: pre-wrap; }

.trace--warn { margin: 0.3rem 0; font-size: 0.75rem; color: #b4552d; font-family: ui-monospace, SFMono-Regular, monospace; }

.followups { display: flex; flex-wrap: wrap; gap: 0.4rem; padding-bottom: 0.6rem; }
.chip { display: block; margin-bottom: 0.35rem; text-align: left; background: #fff; border: 1px solid #e4e1da; border-radius: 999px; padding: 0.35rem 0.75rem; font: inherit; font-size: 0.78rem; color: #4a453e; cursor: pointer; }
.chip:hover { border-color: #b4552d; color: #b4552d; }
.followups .chip { margin-bottom: 0; }

.composer { display: flex; gap: 0.5rem; align-items: flex-end; border-top: 1px solid #e9e5dd; padding-top: 0.8rem; }
.composer textarea { flex: 1; resize: none; font: inherit; font-size: 0.9rem; padding: 0.6rem 0.75rem; border: 1px solid #e4e1da; border-radius: 10px; background: #fff; max-height: 8rem; }
.composer textarea:focus { outline: 2px solid #b4552d; outline-offset: -1px; border-color: transparent; }
.composer button { padding: 0.6rem 1.1rem; border-radius: 10px; border: none; background: #1c1a17; color: #faf8f4; font: inherit; font-size: 0.85rem; cursor: pointer; }
.composer button:disabled { opacity: 0.35; cursor: default; }
</style>
