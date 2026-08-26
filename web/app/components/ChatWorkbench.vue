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
  canReshuffle?: boolean;
}>(), {
  active: true,
  // Just "Back". 
  backLabel: "Back",
  busy: false,
  dataState: "ready",
  error: "",
  examples: () => [],
  followups: () => [],
  canReshuffle: false,
  stateKey: "",
  turns: () => [],
});

function goLanding(event: MouseEvent) {
  if (event.metaKey || event.ctrlKey || event.shiftKey || event.button !== 0) return;
  event.preventDefault();
  emit("back");
}

const emit = defineEmits<{
  send: [question: string];
  back: [];
  reshuffle: [];
}>();

const input = ref("");
const inputEl = ref<HTMLTextAreaElement | null>(null);
const threadEl = ref<HTMLElement | null>(null);
const chartSelections = reactive<Record<string, { label: string; value: number }[]>>({});
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

/* Comparison: selection IS the comparison.  */
const COMPARE_LIMIT = 2;

function chooseChart(key: string, value: { label: string; value: number }) {
  const picked = chartSelections[key] ?? [];
  const already = picked.findIndex((entry) => entry.label === value.label);

  if (already > -1) {
    // Clicking a picked row releases it. 
    chartSelections[key] = picked.filter((_, index) => index !== already);
    return;
  }

  const next = [...picked, value].slice(-COMPARE_LIMIT);
  chartSelections[key] = next;

  if (next.length === COMPARE_LIMIT) {
    send(`Compare ${next[0]!.label} and ${next[1]!.label}, measured the same way.`);
  }
}

function clearChart(key: string) {
  chartSelections[key] = [];
}

/* When an answer can be a graph.  */
function graphable(spec: any): { from: string; to: string } | null {
  const rows: Record<string, unknown>[] = spec?.rows ?? [];
  if (rows.length < 2) return null;
  const first = rows[0] ?? {};
  const valueKey = spec?.encoding?.value;

  const entityKeys = Object.keys(first).filter((key) => {
    if (key === valueKey) return false;
    const sample = rows.slice(0, 8).map((row) => row[key]);
    const looksNumeric = sample.every((v) => v !== null && v !== "" && !Number.isNaN(Number(v)));
    if (looksNumeric) return false;
    // A column where every row is the same value connects nothing.
    return new Set(sample.map(String)).size > 1;
  });

  if (entityKeys.length < 2) return null;
  return { from: entityKeys[0]!, to: entityKeys[1]! };
}

const graphOpen = reactive<Record<string, boolean>>({});

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
    <!-- Two states, one shell.  -->
    <div :class="['chat-shell', started ? 'is-conversation' : 'is-opening']">
      <slot name="toolbar" />

      <!-- The mark is pinned to the page, not carried inside the centred header, so it lands on the same pixel here as on the story and the About page.  -->
      <!-- `href="/"` reloaded the whole application to reach a screen that is already mounted behind this one.  -->
      <a class="chat-logo" href="/" aria-label="EuroQol home"
         @click="goLanding">
        <img src="/brand/euroqol-logo.svg" alt="EuroQol" width="300" height="49">
      </a>

      <!-- Close, not Back.  -->
      <button type="button" class="chat-close" @click="emit('back')" aria-label="Close the research explorer">
        <span aria-hidden="true">×</span>
      </button>

      <header class="chat-head">
        <div class="chat-head-main">
          <div class="chat-brand">
            <strong :id="titleId">Research explorer</strong>
          </div>

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
          <!-- The opening fold's own title and counts.  -->
          <section v-if="!started" class="chat-empty">
            <!-- Two tones in one line: the noun carries, the qualifier recedes.  -->
            <h1 class="chat-opening-title">Research <span>explorer</span></h1>

            <!-- Three small KPIs, not a sentence.  -->
            <dl v-if="dataState === 'ready'" class="chat-kpis">
              <div>
                <dt>{{ counts.projects.toLocaleString('en') }}</dt>
                <dd>projects</dd>
              </div>
              <div>
                <dt>{{ counts.works.toLocaleString('en') }}</dt>
                <dd>publications</dd>
              </div>
              <div>
                <dt>{{ counts.findings.toLocaleString('en') }}</dt>
                <dd>findings</dd>
              </div>
            </dl>
            <p v-else class="chat-opening-counts">
              {{ dataState === 'error' ? 'Research data unavailable' : 'Connecting to the research data' }}
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
                    :selected="(chartSelections[segment.key] ?? []).map((entry) => entry.label)"
                    reference
                    @select="chooseChart(segment.key, $event)"
                  />
                  <p class="chat-chart-hint">Click a bar to ask about it. Click a second to compare the two.</p>

                  <!-- Offered, never forced.  -->
                  <template v-if="graphable(segment.widget)">
                    <button
                      type="button"
                      class="chat-asgraph"
                      :aria-expanded="Boolean(graphOpen[segment.key])"
                      @click="graphOpen[segment.key] = !graphOpen[segment.key]"
                    >
                      <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true">
                        <circle cx="5" cy="6" r="2.2" fill="none" stroke="currentColor" stroke-width="1.7" />
                        <circle cx="5" cy="18" r="2.2" fill="none" stroke="currentColor" stroke-width="1.7" />
                        <circle cx="19" cy="12" r="2.2" fill="none" stroke="currentColor" stroke-width="1.7" />
                        <path d="M7 7l10 4M7 17l10-4" stroke="currentColor" stroke-width="1.7" fill="none" />
                      </svg>
                      {{ graphOpen[segment.key] ? "Hide the graph" : "View as graph" }}
                    </button>
                    <ChatGraph
                      v-if="graphOpen[segment.key]"
                      :spec="segment.widget"
                      :from="graphable(segment.widget)!.from"
                      :to="graphable(segment.widget)!.to"
                      @ask="send"
                    />
                  </template>

                  <!-- One picked: what you can ask about it.  -->
                  <div v-if="(chartSelections[segment.key] ?? []).length === 1" class="chat-chart-actions">
                    <span>Ask about <strong>{{ chartSelections[segment.key]![0]!.label }}</strong></span>
                    <button
                      v-for="question in chartQuestions(chartSelections[segment.key]![0]!.label)"
                      :key="question"
                      type="button"
                      :disabled="busy"
                      @click="send(question)"
                    >{{ question }}</button>
                  </div>

                  <div v-else-if="(chartSelections[segment.key] ?? []).length > 1" class="chat-chart-compare">
                    <span>Comparing</span>
                    <button
                      v-for="entry in chartSelections[segment.key]"
                      :key="entry.label"
                      type="button"
                      class="chat-chip-picked"
                      :aria-label="`Remove ${entry.label}`"
                      @click="chooseChart(segment.key, entry)"
                    >{{ entry.label }} <span aria-hidden="true">×</span></button>
                    <button type="button" class="chat-chip-clear" @click="clearChart(segment.key)">Clear</button>
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
          <!-- An arrow, not the word "Ask".  -->
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

      <!-- Suggestions sit under the composer in the opening fold, so the eye lands on the place you type first and the examples read as help rather than as the main event. -->
      <!-- Suggestions carry a magnifier, so they read as questions you can run rather than as tags.  -->
      <section v-if="!started" class="chat-opening-examples" aria-label="Example questions">
        <div class="chat-examples">
          <button v-for="question in examples" :key="question" type="button" :disabled="busy" @click="send(question)">
            <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true">
              <circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="1.8" />
              <path d="M16 16l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
            </svg>
            {{ question }}
          </button>
          <!-- Plain text, not another chip.  -->
          <button
            v-if="canReshuffle"
            type="button"
            class="chat-reshuffle"
            @click="emit('reshuffle')"
          >
            Other questions
            <svg viewBox="0 0 24 24" width="13" height="13" aria-hidden="true">
              <path d="M4 12a8 8 0 0 1 13.7-5.6M20 12a8 8 0 0 1-13.7 5.6" fill="none"
                    stroke="currentColor" stroke-width="1.9" stroke-linecap="round" />
              <path d="M17.5 3.5v3.2h-3.2M6.5 20.5v-3.2h3.2" fill="none"
                    stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </button>
        </div>
      </section>
    </div>
  </section>
</template>
