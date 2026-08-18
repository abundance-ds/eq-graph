<script setup lang="ts">
import type {
  ChatDataCounts,
  ChatDataState,
  ChatTurn,
} from "../types/chat";

const props = withDefaults(defineProps<{
  active?: boolean;
  backLabel?: string;
  busy?: boolean;
  counts: ChatDataCounts;
  dataState?: ChatDataState;
  error?: string;
  examples?: string[];
  followups?: string[];
  stateKey?: string;
  turns?: ChatTurn[];
}>(), {
  active: true,
  backLabel: "Back to story",
  busy: false,
  dataState: "ready",
  error: "",
  examples: () => [],
  followups: () => [],
  stateKey: "",
  turns: () => [],
});

const emit = defineEmits<{
  send: [question: string];
  back: [];
}>();

const input = ref("");
const inputEl = ref<HTMLTextAreaElement | null>(null);
const threadEl = ref<HTMLElement | null>(null);
const chartSelections = reactive<Record<string, { label: string; value: number }>>({});
let autoFollow = true;
let renderedWidgetCount = 0;
let widgetAnchor: HTMLElement | null = null;

const titleId = useId();
const started = computed(() => props.turns.length > 0);

function trailThinks(entry: ChatTurn, index: number): boolean {
  if (!props.busy || entry.id !== props.turns.at(-1)?.id) return false;
  if (index !== entry.list.length - 1) return false;
  const segment = entry.list[index];
  if (segment?.kind !== "tools") return false;
  return segment.parts.every((part) => part.state === "output-available" || part.state === "output-error");
}

const tailThinks = computed(() => {
  if (!props.busy) return false;
  const last = props.turns.at(-1);
  if (!last || last.role === "user") return true;
  const tail = last.list.at(-1);
  return !tail || tail.kind === "widget";
});

function send(question?: string) {
  const value = (question ?? input.value).trim();
  if (!value || props.busy) return;
  autoFollow = true;
  widgetAnchor = null;
  input.value = "";
  autoGrow();
  emit("send", value);
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
    `Which studies are associated with ${label}?`,
    `What do the studies about ${label} find?`,
    `What limitations affect the evidence about ${label}?`,
  ];
}

function chooseChart(key: string, value: { label: string; value: number }) {
  chartSelections[key] = value;
}

function keepLatestVisible() {
  const widgetCount = props.turns.reduce(
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
    if (autoFollow) thread.scrollTo({ top: thread.scrollHeight, behavior: props.busy ? "auto" : "smooth" });
  });
}

function onThreadScroll() {
  const thread = threadEl.value;
  if (!thread || widgetAnchor) return;
  autoFollow = thread.scrollHeight - thread.scrollTop - thread.clientHeight < 72;
}

function releaseWidgetAnchor() {
  widgetAnchor = null;
}

const turnSignature = computed(() => props.turns.map((turn) =>
  `${turn.id}:${turn.list.map((segment) => {
    if (segment.kind === "text") return `${segment.kind}:${segment.text.length}`;
    if (segment.kind === "widget") return `${segment.kind}:${segment.key}:${segment.widget.rows.length}`;
    return `${segment.kind}:${segment.parts.map((part) => `${part.type}:${part.state ?? ""}`).join(",")}`;
  }).join("|")}`,
).join("||"));

watch(turnSignature, keepLatestVisible);
watch(
  () => props.stateKey,
  async () => {
    autoFollow = true;
    widgetAnchor = null;
    renderedWidgetCount = props.turns.reduce(
      (total, entry) => total + entry.list.filter((segment) => segment.kind === "widget").length,
      0,
    );
    Object.keys(chartSelections).forEach((key) => delete chartSelections[key]);
    await nextTick();
    threadEl.value?.scrollTo({ top: 0, behavior: "auto" });
  },
  { flush: "post" },
);
watch(() => props.followups.length, () => {
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
  renderedWidgetCount = props.turns.reduce(
    (total, entry) => total + entry.list.filter((segment) => segment.kind === "widget").length,
    0,
  );
  if (props.active) inputEl.value?.focus({ preventScroll: true });
});
</script>

<template>
  <section
    class="xp-root chat-root"
    :aria-labelledby="titleId"
    :aria-hidden="active ? undefined : 'true'"
    :inert="!active"
  >
    <div class="chat-shell">
      <slot name="toolbar" />

      <header class="chat-head">
        <div class="chat-head-main">
          <div class="chat-brand">
            <img src="/brand/euroqol-logo.svg" alt="EuroQol" width="116" height="19">
            <span aria-hidden="true" />
            <strong :id="titleId">Research explorer</strong>
          </div>
          <button type="button" class="chat-back" @click="emit('back')">
            <span aria-hidden="true">←</span> {{ backLabel }}
          </button>
        </div>

        <div
          :class="['chat-data-state', dataState === 'ready' && 'is-ready', dataState === 'error' && 'is-error']"
          aria-live="polite"
        >
          <i aria-hidden="true" />
          <template v-if="dataState === 'ready'">
            <strong>EuroQol research</strong>
            <span>{{ counts.studies.toLocaleString('en') }} studies</span>
            <span>{{ counts.works.toLocaleString('en') }} publications</span>
            <span>{{ counts.findings.toLocaleString('en') }} findings</span>
          </template>
          <strong v-else-if="dataState === 'error'">Research data unavailable</strong>
          <strong v-else>Connecting to the research data</strong>
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
            <h1>Ask about EuroQol research.</h1>
            <p>Try one of these:</p>
            <div class="chat-examples">
              <button v-for="question in examples" :key="question" type="button" :disabled="busy" @click="send(question)">
                {{ question }}
              </button>
            </div>
          </section>

          <article v-for="entry in turns" :key="entry.id" :class="['chat-turn', `is-${entry.role}`]">
            <div v-if="entry.role === 'user'" class="chat-user-message">
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
          <p v-if="error" class="chat-error" role="alert">{{ error }}</p>
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
