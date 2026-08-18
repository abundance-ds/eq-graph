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
  // Just "Back". The arrow already says the direction, and there is only one
  // place you can have come from — so naming it adds a word without adding
  // meaning. "Back to story" also named the route rather than the reader's
  // journey, which is how developer vocabulary leaks into an interface.
  backLabel: "Back",
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
    <!-- Two states, one shell.

         Before the first question the fold is centred: title, the counts under
         it, then the composer — the arrangement every assistant opens with,
         because with nothing to read yet the only thing worth putting in front
         of someone is the place they type.

         From the first question on it becomes an ordinary chat window: the
         title goes to the top bar, the thread takes the height, and the
         composer sits at the bottom where it stays. -->
    <div :class="['chat-shell', started ? 'is-conversation' : 'is-opening']">
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
          <!-- The opening fold's own title and counts. The header carries them
               once a conversation exists; before that they belong here, in the
               middle, directly above the composer as one centred group. -->
          <section v-if="!started" class="chat-empty">
            <h1 class="chat-opening-title">Research explorer</h1>
            <p class="chat-opening-counts">
              <template v-if="dataState === 'ready'">
                {{ counts.projects.toLocaleString('en') }} projects
                · {{ counts.works.toLocaleString('en') }} publications
                · {{ counts.findings.toLocaleString('en') }} findings
              </template>
              <template v-else-if="dataState === 'error'">Research data unavailable</template>
              <template v-else>Connecting to the research data</template>
            </p>
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
          <!-- An arrow, not the word "Ask". The placeholder already says what
               this does, and every assistant uses the same mark — so the arrow
               is read instantly and in any language. The accessible name stays
               a verb, because a screen reader gets no shape. -->
          <button
            type="submit"
            class="chat-send"
            :disabled="busy || !input.trim()"
            :aria-label="busy ? 'Working' : 'Send question'"
          >
            <span v-if="busy" class="chat-send-busy" aria-hidden="true" />
            <svg v-else viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
              <path d="M12 19V5M12 5l-6 6M12 5l6 6" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </button>
        </form>
      </div>

      <!-- Suggestions sit under the composer in the opening fold, so the eye
           lands on the place you type first and the examples read as help
           rather than as the main event. -->
      <section v-if="!started" class="chat-opening-examples" aria-label="Example questions">
        <p>Ask about funded research and its evidence, or try one of these:</p>
        <div class="chat-examples">
          <button v-for="question in examples" :key="question" type="button" :disabled="busy" @click="send(question)">
            {{ question }}
          </button>
        </div>
      </section>
    </div>
  </section>
</template>
