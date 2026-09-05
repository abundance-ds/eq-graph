<script setup lang="ts">
import type { ChatTurn } from "../types/chat";
import { submitChatOnEnter } from "../utils/chatComposer";

const props = withDefaults(defineProps<{
  active?: boolean;
  busy?: boolean;
  error?: string;
  examples?: string[];
  followups?: string[];
  stateKey?: string;
  turns?: ChatTurn[];
  canReshuffle?: boolean;
  canRetry?: boolean;
}>(), {
  active: true,
  busy: false,
  error: "",
  examples: () => [],
  followups: () => [],
  canReshuffle: false,
  canRetry: false,
  stateKey: "",
  turns: () => [],
});

const emit = defineEmits<{
  send: [question: string, source: "typed" | "sample" | "followup"];
  back: [];
  home: [];
  reshuffle: [];
  retry: [];
}>();

function goSection(to: "home" | "story" | "explore") {
  if (to === "home") emit("home");
  if (to === "story") emit("home");
}

const input = ref("");
const inputEl = ref<HTMLTextAreaElement | null>(null);
const threadEl = ref<HTMLElement | null>(null);
let autoFollow = true;
let renderedWidgetCount = 0;
let widgetAnchor: HTMLElement | null = null;

const started = computed(() => props.turns.length > 0);
const showKnowledgeTrace = computed(() => (
  props.busy && started.value && props.turns.at(-1)?.role === "user"
));

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

function send(question?: string, source: "typed" | "sample" | "followup" = "typed") {
  const value = (question ?? input.value).trim();
  if (!value || props.busy) return;
  autoFollow = true;
  widgetAnchor = null;
  input.value = "";
  autoGrow();
  emit("send", value, source);
}

function onComposerKeydown(event: KeyboardEvent) {
  submitChatOnEnter(event, () => send());
}

function autoGrow() {
  nextTick(() => {
    if (!inputEl.value) return;
    inputEl.value.style.height = "auto";
    inputEl.value.style.height = `${Math.min(inputEl.value.scrollHeight, 120)}px`;
  });
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
    aria-label="Ask about the research"
    :aria-hidden="active ? undefined : 'true'"
    :inert="!active"
  >
    <!-- Two states, one shell.  -->
    <div :class="['chat-shell', started ? 'is-conversation' : 'is-opening']">
      <slot name="toolbar" />
      <SiteHeader current="explore" :on-go="goSection" />

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
          <section v-if="!started" class="chat-empty">
            <h1 class="chat-opening-title" style="font-size: 2.5rem; padding-bottom:8px; min-width: 100% !important;;">What do you want to investigate?</h1>
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
                  <GraphWidget :spec="segment.widget" />
                </div>
              </template>
            </div>
          </article>

          <div
            v-if="showKnowledgeTrace"
            class="chat-knowledge-trace"
            role="status"
            aria-label="Searching projects, publications, and findings"
          >
            <span><i />Projects</span><b /><span><i />Publications</span><b /><span><i />Findings</span>
          </div>
          <ActivityTrail v-if="tailThinks && !showKnowledgeTrace" :parts="[]" thinking />
          <div v-if="error" class="chat-request-state is-error" role="alert">
            <span>{{ error }}</span>
            <button v-if="canRetry" type="button" @click="emit('retry')">Try again</button>
          </div>
        </div>
      </div>

      <div class="chat-dock">
        <div v-if="followups.length" class="chat-followups" aria-label="Follow-up questions">
          <button v-for="question in followups" :key="question" type="button" :disabled="busy" @click="send(question, 'followup')">
            {{ question }}
          </button>
        </div>

        <form class="chat-composer" @submit.prevent="send()">
          <textarea
            ref="inputEl"
            v-model="input"
            rows="1"
            placeholder="Ask a research question…"
            aria-label="Ask a research question"
            @input="autoGrow"
            @keydown="onComposerKeydown"
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

      <section v-if="!started" class="chat-opening-examples" aria-label="Example questions">
        <div class="chat-examples">
          <button v-for="question in examples" :key="question" type="button" :disabled="busy" @click="send(question, 'sample')">
            <span>{{ question }}</span><i aria-hidden="true">→</i>
          </button>
          <!-- Plain text, not another chip.  -->
          <button
            v-if="canReshuffle"
            type="button"
            class="chat-reshuffle"
            @click="emit('reshuffle')"
          >
            More questions
          </button>
        </div>
      </section>
    </div>
  </section>
</template>
