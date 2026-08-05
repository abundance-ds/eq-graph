<script setup lang="ts">
/**
 * The activity trail.
 *
 * It shows what the agent does, in the flow of the answer, and not only at the
 * end. One row for each tool call, on a vertical rail. The row that runs now
 * carries a live dot, a moving label and a counter. A finished row becomes
 * quiet. A failed row becomes red and keeps its message.
 *
 * The component reads the tool parts of one message. It holds no state of the
 * chat, so it also works when the page draws an old answer again.
 */
import { computed, onBeforeUnmount, ref, watch } from "vue";

type Part = Record<string, any>;

const props = defineProps<{
  /** The tool parts, in the order the agent made them. */
  parts: Part[];
  /** True when the agent works, and this trail is the newest one. */
  thinking?: boolean;
}>();

/** The label for each tool, while it runs and after it stops. */
const VERBS: Record<string, [string, string]> = {
  "tool-search_graph": ["Looking for names", "Looked for names"],
  "tool-run_cypher": ["Querying the graph", "Read the graph"],
  "tool-render": ["Drawing the chart", "Drew the chart"],
};

type Step = {
  id: string;
  state: "running" | "done" | "failed";
  label: string;
  detail: string;
  cypher: string;
};

const steps = computed<Step[]>(() =>
  props.parts.map((part, index) => {
    const [running, finished] = VERBS[part.type] ?? ["Working", "Done"];
    const input = part.input ?? {};
    const output = part.output;
    const stopped = part.state === "output-available" || part.state === "output-error";
    const failed = part.state === "output-error" || (stopped && output?.ok === false);

    let detail = "";
    if (failed) {
      detail = output?.error ?? part.errorText ?? "The tool failed.";
    } else if (stopped) {
      if (part.type === "tool-run_cypher") {
        detail = `${output?.rowCount ?? 0} rows in ${output?.elapsedMs ?? 0} ms`;
        if (output?.truncated) detail += " (cut)";
      } else if (part.type === "tool-search_graph") {
        detail = `${output?.hits?.length ?? 0} matches`;
      } else if (part.type === "tool-render") {
        detail = output?.widget?.title ?? "";
      }
    } else {
      if (part.type === "tool-run_cypher") detail = input.purpose ?? "Writing the query…";
      else if (part.type === "tool-search_graph") detail = input.query ? `“${input.query}”` : "";
      else if (part.type === "tool-render") detail = input.title ?? "";
    }

    return {
      id: part.toolCallId ?? `${part.type}-${index}`,
      state: failed ? "failed" : stopped ? "done" : "running",
      label: stopped ? finished : running,
      detail,
      cypher: part.type === "tool-run_cypher" ? (input.cypher ?? "") : "",
    };
  }),
);

const active = computed(() => steps.value.find((step) => step.state === "running") ?? null);
const live = computed(() => Boolean(active.value) || Boolean(props.thinking));

// --- The counter for the row that runs now --------------------------------
// The parts carry no time stamp, so the trail takes the time when the row
// first becomes the active one.

const startedAt = ref(0);
const now = ref(0);
let ticker: ReturnType<typeof setInterval> | undefined;

function stopTicker() {
  if (ticker) clearInterval(ticker);
  ticker = undefined;
}

watch(
  () => [active.value?.id ?? null, props.thinking] as const,
  ([id, thinks]) => {
    if (!id && !thinks) {
      startedAt.value = 0;
      stopTicker();
      return;
    }
    startedAt.value = Date.now();
    now.value = startedAt.value;
    stopTicker();
    ticker = setInterval(() => {
      now.value = Date.now();
    }, 90);
  },
  { immediate: true },
);

onBeforeUnmount(stopTicker);

const elapsed = computed(() => {
  if (!startedAt.value) return "";
  const seconds = (now.value - startedAt.value) / 1000;
  return seconds < 0.4 ? "" : `${seconds.toFixed(1)}s`;
});

// --- The query text --------------------------------------------------------
// While the agent writes the query, the trail shows it. After the query runs,
// the trail hides it, and one click opens it again.

const opened = ref<Record<string, boolean>>({});

function toggle(id: string) {
  opened.value = { ...opened.value, [id]: !opened.value[id] };
}

function showsCypher(step: Step): boolean {
  if (!step.cypher) return false;
  return step.state === "running" || Boolean(opened.value[step.id]);
}
</script>

<template>
  <div :class="['trail', live && 'trail--live']">
    <div v-for="step in steps" :key="step.id" :class="['step', `step--${step.state}`]">
      <span class="dot" />

      <div class="body">
        <p class="line">
          <span :class="['label', step.state === 'running' && 'label--live']">{{ step.label }}</span>
          <span v-if="step.detail" class="detail">{{ step.detail }}</span>
          <span v-if="step.state === 'running' && elapsed" class="clock">{{ elapsed }}</span>
          <button
            v-if="step.cypher && step.state !== 'running'"
            class="peek"
            type="button"
            @click="toggle(step.id)"
          >
            {{ opened[step.id] ? "hide query" : "query" }}
          </button>
        </p>

        <pre v-if="showsCypher(step)" class="code">{{ step.cypher }}</pre>
      </div>
    </div>

    <!-- Between two tools the agent decides what to do next. -->
    <div v-if="props.thinking" class="step step--running">
      <span class="dot" />
      <div class="body">
        <p class="line">
          <span class="label label--live">Thinking</span>
          <span class="dots"><i /><i /><i /></span>
          <span v-if="elapsed" class="clock">{{ elapsed }}</span>
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.trail {
  position: relative;
  margin: 0.35rem 0 0.7rem;
  padding-left: 0.95rem;
}
.trail::before {
  content: "";
  position: absolute;
  left: 3px;
  top: 0.45rem;
  bottom: 0.45rem;
  width: 1px;
  background: #e4e1da;
}
.trail--live::before {
  background: linear-gradient(180deg, #e4e1da 0%, #e0b7a4 55%, #e4e1da 100%);
  background-size: 100% 220%;
  animation: flow 2.2s linear infinite;
}
@keyframes flow {
  from { background-position: 0 -120%; }
  to { background-position: 0 120%; }
}

.step {
  position: relative;
  padding: 0.16rem 0;
}
.body {
  min-width: 0;
}

.dot {
  position: absolute;
  left: -0.95rem;
  top: 0.5rem;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #cfc9bf;
  box-shadow: 0 0 0 3px #faf8f4;
}
.step--running .dot {
  background: #b4552d;
  animation: halo 1.5s ease-out infinite;
}
.step--failed .dot {
  background: #faf8f4;
  border: 1.5px solid #b4552d;
}
@keyframes halo {
  0% { box-shadow: 0 0 0 3px #faf8f4, 0 0 0 3px rgba(180, 85, 45, 0.45); }
  70% { box-shadow: 0 0 0 3px #faf8f4, 0 0 0 9px rgba(180, 85, 45, 0); }
  100% { box-shadow: 0 0 0 3px #faf8f4, 0 0 0 9px rgba(180, 85, 45, 0); }
}

.line {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.45rem;
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.5;
}
.label {
  color: #6f6a62;
  font-weight: 500;
}
.step--done .label { color: #a09a90; }
.step--failed .label { color: #b4552d; }

/* The moving label marks the step that runs now. */
.label--live {
  background: linear-gradient(90deg, #a09a90 0%, #1c1a17 45%, #a09a90 90%);
  background-size: 220% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: sweep 1.6s linear infinite;
}
@keyframes sweep {
  from { background-position: 120% 0; }
  to { background-position: -120% 0; }
}

.detail {
  color: #a09a90;
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 0.7rem;
  overflow-wrap: anywhere;
}
.step--failed .detail { color: #c07a58; }

.clock {
  color: #c3bcb1;
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 0.68rem;
  font-variant-numeric: tabular-nums;
}

.peek {
  border: none;
  background: none;
  padding: 0;
  font: inherit;
  font-size: 0.68rem;
  color: #c3bcb1;
  text-decoration: underline;
  text-underline-offset: 2px;
  cursor: pointer;
}
.peek:hover { color: #b4552d; }

.dots {
  display: inline-flex;
  gap: 3px;
  align-self: center;
}
.dots i {
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: #b4552d;
  animation: bob 1.1s ease-in-out infinite;
}
.dots i:nth-child(2) { animation-delay: 0.15s; }
.dots i:nth-child(3) { animation-delay: 0.3s; }
@keyframes bob {
  0%, 100% { opacity: 0.25; transform: translateY(0); }
  50% { opacity: 1; transform: translateY(-2px); }
}

.code {
  margin: 0.3rem 0 0.35rem;
  padding: 0.5rem 0.6rem;
  background: #f4f1ea;
  border-left: 2px solid #e0d9cc;
  border-radius: 0 6px 6px 0;
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 0.68rem;
  line-height: 1.55;
  color: #6f6a62;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  max-height: 11rem;
  overflow: auto;
}

@media (prefers-reduced-motion: reduce) {
  .trail--live::before,
  .step--running .dot,
  .label--live,
  .dots i {
    animation: none;
  }
  .label--live { color: #1c1a17; -webkit-text-fill-color: #1c1a17; }
}
</style>
