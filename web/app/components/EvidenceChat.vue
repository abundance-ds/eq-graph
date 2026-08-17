<script setup lang="ts">
import { Chat } from "@ai-sdk/vue";
import type { DemoResearchData } from "../../shared/types/demo";

const props = defineProps<{
  data: DemoResearchData;
  active?: boolean;
}>();

const emit = defineEmits<{ "return-story": [] }>();

type DataStatus = {
  ok: true;
  checkedAt: string;
  counts: {
    projects: number;
    works: number;
    acceptedAttributions: number;
    worksWithFindings: number;
    findings: number;
  };
};

type Segment =
  | { kind: "text"; key: string; text: string }
  | { kind: "widget"; key: string; widget: any }
  | { kind: "tools"; key: string; parts: any[] };

const chat = new Chat({});
const input = ref("");
const inputEl = ref<HTMLTextAreaElement | null>(null);
const threadEl = ref<HTMLElement | null>(null);
const chartSelections = reactive<Record<string, { label: string; value: number }>>({});
let graphRefreshTimer: ReturnType<typeof setInterval> | undefined;
let autoFollow = true;
let renderedWidgetCount = 0;
let widgetAnchor: HTMLElement | null = null;

const {
  data: graphStatus,
  status: graphRequestStatus,
  error: graphStatusError,
  refresh: refreshGraphStatus,
} = await useFetch<DataStatus>("/api/graph/status");

const busy = computed(() => chat.status === "submitted" || chat.status === "streaming");
const started = computed(() => chat.messages.length > 0);
const counts = computed(() => graphStatus.value?.counts ?? {
  projects: props.data.portfolio.projects,
  works: props.data.portfolio.works,
  acceptedAttributions: props.data.portfolio.acceptedLinks,
  worksWithFindings: 0,
  findings: props.data.portfolio.findings,
});

const EXAMPLES = [
  "Show the accepted publications for project 341-RA.",
  "Which instruments have the most extracted findings?",
  "Which countries have the most funded projects?",
  "What does the reference data report about ceiling effects?",
];

const OPEN = "<followups>";
const CLOSE = "</followups>";

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

function segments(message: any): Segment[] {
  const output: Segment[] = [];
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

const view = computed(() => chat.messages.map((message: any) => ({ message, list: segments(message) })));

function trailThinks(entry: { message: any; list: Segment[] }, index: number): boolean {
  if (!busy.value || entry.message.id !== view.value.at(-1)?.message.id) return false;
  if (index !== entry.list.length - 1) return false;
  const segment = entry.list[index];
  if (segment?.kind !== "tools") return false;
  return segment.parts.every((part: any) => part.state === "output-available" || part.state === "output-error");
}

const tailThinks = computed(() => {
  if (!busy.value) return false;
  const last = view.value.at(-1);
  if (!last || last.message.role === "user") return true;
  const tail = last.list.at(-1);
  return !tail || tail.kind === "widget";
});

function send(question?: string) {
  const value = (question ?? input.value).trim();
  if (!value || busy.value) return;
  autoFollow = true;
  widgetAnchor = null;
  input.value = "";
  autoGrow();
  chat.sendMessage({ text: value });
}

function onKeydown(event: KeyboardEvent) {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    send();
  }
}

function autoGrow() {
  nextTick(() => {
    if (!inputEl.value) return;
    inputEl.value.style.height = "auto";
    inputEl.value.style.height = `${Math.min(inputEl.value.scrollHeight, 120)}px`;
  });
}

function chartQuestions(label: string) {
  return [
    `Which funded projects are associated with ${label}?`,
    `Which publications are associated with ${label}?`,
    `Compare ${label} with the other results.`,
  ];
}

function chooseChart(key: string, value: { label: string; value: number }) {
  chartSelections[key] = value;
}

function keepLatestVisible() {
  const widgetCount = view.value.reduce(
    (total, entry) => total + entry.list.filter((segment) => segment.kind === "widget").length,
    0,
  );
  const hasNewWidget = widgetCount > renderedWidgetCount;
  renderedWidgetCount = widgetCount;

  nextTick(() => {
    const thread = threadEl.value;
    if (!thread) return;
    if (hasNewWidget) {
      const widgets = thread.querySelectorAll<HTMLElement>(".chat-widget-block");
      widgetAnchor = widgets[widgets.length - 1] ?? null;
      autoFollow = false;
    }
    if (widgetAnchor) {
      const delta = widgetAnchor.getBoundingClientRect().top - thread.getBoundingClientRect().top;
      thread.scrollTop += delta - 6;
      return;
    }
    if (autoFollow) thread.scrollTo({ top: thread.scrollHeight, behavior: busy.value ? "auto" : "smooth" });
  });
}

function onThreadScroll() {
  const thread = threadEl.value;
  if (!thread) return;
  if (widgetAnchor) return;
  autoFollow = thread.scrollHeight - thread.scrollTop - thread.clientHeight < 72;
}

function releaseWidgetAnchor() {
  widgetAnchor = null;
}

watch(
  () => chat.messages.map((message: any) => message.parts.map((part: any) => `${part.type}:${part.state ?? ""}:${part.text?.length ?? 0}`).join("|")).join("||"),
  keepLatestVisible,
);

watch(() => followups.value.length, () => {
  if (autoFollow) keepLatestVisible();
});

watch(
  () => props.active,
  async (active) => {
    if (!active) return;
    await nextTick();
    inputEl.value?.focus({ preventScroll: true });
  },
);

onMounted(() => {
  graphRefreshTimer = setInterval(() => refreshGraphStatus(), 60_000);
  if (props.active) inputEl.value?.focus({ preventScroll: true });
});

onBeforeUnmount(() => {
  if (graphRefreshTimer) clearInterval(graphRefreshTimer);
});
</script>

<template>
  <section
    class="xp-root chat-root"
    aria-labelledby="chat-title"
    :aria-hidden="active ? undefined : 'true'"
    :inert="!active"
  >
    <div class="chat-shell">
      <header class="chat-head">
        <div class="chat-head-main">
          <div class="chat-brand">
            <img src="/brand/euroqol-logo.svg" alt="EuroQol" width="116" height="19">
            <span aria-hidden="true" />
            <strong id="chat-title">Research explorer</strong>
          </div>
          <button type="button" class="chat-back" @click="emit('return-story')">
            <span aria-hidden="true">←</span> Back to story
          </button>
        </div>

        <div
          :class="['chat-data-state', graphStatus?.ok && 'is-ready', graphStatusError && 'is-error']"
          aria-live="polite"
        >
          <i aria-hidden="true" />
          <template v-if="graphStatus?.ok">
            <strong>Reference data</strong>
            <span>{{ counts.projects.toLocaleString('en') }} projects</span>
            <span>{{ counts.works.toLocaleString('en') }} publications</span>
            <span>{{ counts.findings.toLocaleString('en') }} findings</span>
          </template>
          <template v-else-if="graphStatusError">
            <strong>Research data unavailable</strong>
          </template>
          <template v-else>
            <strong>{{ graphRequestStatus === 'pending' ? 'Connecting to the research data' : 'Preparing the research data' }}</strong>
          </template>
        </div>
      </header>

      <div
        ref="threadEl"
        class="chat-thread"
        aria-live="polite"
        aria-relevant="additions text"
        @scroll.passive="onThreadScroll"
        @wheel.passive="releaseWidgetAnchor"
        @touchstart.passive="releaseWidgetAnchor"
        @pointerdown="releaseWidgetAnchor"
        @keydown="releaseWidgetAnchor"
      >
        <div class="chat-thread-inner">
          <section v-if="!started" class="chat-empty" aria-label="Example questions">
            <h1>Ask about funded research and its evidence.</h1>
            <p>Try one of these:</p>
            <div class="chat-examples">
              <button v-for="question in EXAMPLES" :key="question" type="button" :disabled="busy" @click="send(question)">
                {{ question }}
              </button>
            </div>
          </section>

          <article v-for="entry in view" :key="entry.message.id" :class="['chat-turn', `is-${entry.message.role}`]">
            <div v-if="entry.message.role === 'user'" class="chat-user-message">
              {{ entry.list.filter((item) => item.kind === 'text').map((item: any) => item.text).join('') }}
            </div>

            <div v-else class="chat-assistant-message">
              <template v-for="(segment, index) in entry.list" :key="segment.key">
                <ChatAnswer v-if="segment.kind === 'text'" :text="segment.text" />

                <ActivityTrail
                  v-else-if="segment.kind === 'tools'"
                  :parts="segment.parts"
                  :thinking="trailThinks(entry, index)"
                />

                <div v-else class="chat-widget-block">
                  <GraphWidget
                    :spec="segment.widget"
                    reference
                    @select="chooseChart(segment.key, $event)"
                  />
                  <div v-if="chartSelections[segment.key]" class="chat-chart-actions">
                    <span>Ask about <strong>{{ chartSelections[segment.key]!.label }}</strong></span>
                    <button
                      v-for="question in chartQuestions(chartSelections[segment.key]!.label)"
                      :key="question"
                      type="button"
                      :disabled="busy"
                      @click="send(question)"
                    >{{ question }}</button>
                  </div>
                </div>
              </template>
            </div>
          </article>

          <ActivityTrail v-if="tailThinks" :parts="[]" thinking />
          <p v-if="chat.error" class="chat-error" role="alert">{{ chat.error.message }}</p>
        </div>
      </div>

      <div class="chat-dock">
        <div v-if="followups.length" class="chat-followups" aria-label="Follow-up questions">
          <span>Continue</span>
          <button v-for="question in followups" :key="question" type="button" :disabled="busy" @click="send(question)">
            {{ question }}
          </button>
        </div>

        <form class="chat-composer" @submit.prevent="send()">
          <textarea
            ref="inputEl"
            v-model="input"
            rows="1"
            placeholder="Ask about the evidence…"
            aria-label="Ask about the evidence"
            @input="autoGrow"
            @keydown="onKeydown"
          />
          <button type="submit" :disabled="busy || !input.trim()">
            {{ busy ? "Working…" : "Ask" }}
          </button>
        </form>
      </div>
    </div>
  </section>
</template>
