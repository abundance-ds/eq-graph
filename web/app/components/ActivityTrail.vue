<script setup lang="ts">
/**
 * The working card.
 *
 * It shows how the answer was reached, while it is being reached — steps named
 * in the reader's language, each carrying the real count it produced. A step
 * that is finished is struck through and goes quiet. Once the answer has
 * landed the whole card folds to a single line, and one click opens it again.
 *
 * This replaces a trail that printed the raw SQL and a stopwatch. Those answer
 * "what did the program do?". A researcher is asking "how do you know?", and
 * that is a different question with a different vocabulary. The query is still
 * reachable — one click, per step — because hiding it entirely would trade one
 * kind of opacity for another. It just no longer opens itself uninvited.
 *
 * The component reads the tool parts of one message and holds no chat state,
 * so it also works when the page draws an old answer again.
 */
import { computed, ref } from "vue";

type Part = Record<string, any>;

const props = defineProps<{
  /** The tool parts, in the order the agent made them. */
  parts: Part[];
  /** True when the agent works, and this card is the newest one. */
  thinking?: boolean;
}>();

type Step = {
  id: string;
  state: "running" | "done" | "failed";
  label: string;
  detail: string;
  query: string;
};

/** Sentence case, no trailing full stop — these read as step names, not prose. */
function tidy(text: string): string {
  const trimmed = text.trim().replace(/\.$/, "");
  if (!trimmed) return "";
  return trimmed.charAt(0).toUpperCase() + trimmed.slice(1);
}

const steps = computed<Step[]>(() => {
  const list: Step[] = [];

  // The question is read before anything else can happen, so this step is
  // true by construction rather than invented.
  if (props.parts.length || props.thinking) {
    list.push({ id: "read", state: "done", label: "Read the question", detail: "", query: "" });
  }

  props.parts.forEach((part, index) => {
    const input = part.input ?? {};
    const output = part.output;
    const stopped = part.state === "output-available" || part.state === "output-error";
    const failed = part.state === "output-error" || (stopped && output?.ok === false);

    // The agent writes a plain-language purpose for every query it runs. That
    // sentence IS the step name — it is what a person would say they were
    // doing. Falling back only when the model gives us nothing.
    const label = tidy(input.purpose ?? "") || (stopped ? "Searched the reference data" : "Searching the reference data");

    let detail = "";
    if (failed) {
      detail = output?.error ?? part.errorText ?? "This step failed";
    } else if (stopped) {
      const rows = output?.rowCount ?? 0;
      detail = `${rows.toLocaleString("en")} ${rows === 1 ? "result" : "results"}`;
      if (output?.truncated) detail += ", trimmed";
    }

    list.push({
      id: part.toolCallId ?? `${part.type}-${index}`,
      state: failed ? "failed" : stopped ? "done" : "running",
      label,
      detail,
      query: part.type === "tool-query_sql" ? (input.sql ?? "") : "",
    });
  });

  return list;
});

const done = computed(() => steps.value.filter((step) => step.state === "done").length);
const total = computed(() => steps.value.length);
const live = computed(() => steps.value.some((step) => step.state === "running") || Boolean(props.thinking));
const failed = computed(() => steps.value.some((step) => step.state === "failed"));

/* The card folds itself once the work is over.

   Note the denominator can grow while the agent runs: it decides how many
   queries to make as it goes, so there is no plan to count against. Showing a
   fixed total would be a nicer number and a false one. */
const openedByHand = ref(false);
const open = computed(() => live.value || openedByHand.value);

const progress = computed(() => (total.value ? Math.round((done.value / total.value) * 100) : 0));

const openedQueries = ref<Record<string, boolean>>({});
function toggleQuery(id: string) {
  openedQueries.value = { ...openedQueries.value, [id]: !openedQueries.value[id] };
}
</script>

<template>
  <div v-if="total || thinking" :class="['card', live && 'card--live', failed && 'card--failed']">
    <!-- Folded: the one line the card becomes once the answer has landed. -->
    <button
      v-if="!open"
      type="button"
      class="folded"
      @click="openedByHand = true"
    >
      <span class="chev" aria-hidden="true">›</span>
      {{ total }} {{ total === 1 ? "step" : "steps" }} · how this was worked out
    </button>

    <template v-else>
      <div class="head">
        <span class="title">
          <span class="bars" aria-hidden="true"><i /><i /><i /></span>
          Reading the graph
        </span>
        <span :class="['status', live && 'status--live']">
          <i aria-hidden="true" />
          {{ live ? "Working" : failed ? "Finished with a problem" : "Done" }}
        </span>
        <button
          v-if="!live"
          type="button"
          class="fold"
          @click="openedByHand = false"
        >Hide</button>
      </div>

      <div class="meter" aria-hidden="true"><i :style="{ width: `${progress}%` }" /></div>

      <p class="count">
        <span>{{ done }} of {{ total }} {{ total === 1 ? "step" : "steps" }}</span>
      </p>

      <ul class="steps">
        <li v-for="step in steps" :key="step.id" :class="['step', `is-${step.state}`]">
          <span class="tick" aria-hidden="true">
            <template v-if="step.state === 'done'">✓</template>
            <template v-else-if="step.state === 'failed'">!</template>
            <template v-else><i class="spin" /></template>
          </span>
          <span class="label">{{ step.label }}</span>
          <span v-if="step.detail" class="detail">{{ step.detail }}</span>
          <button
            v-if="step.query"
            type="button"
            class="peek"
            :aria-expanded="Boolean(openedQueries[step.id])"
            @click="toggleQuery(step.id)"
          >{{ openedQueries[step.id] ? "hide query" : "query" }}</button>
          <pre v-if="openedQueries[step.id]" class="code">{{ step.query }}</pre>
        </li>

        <!-- Between two queries the agent decides what to check next. -->
        <li v-if="thinking && !steps.some((s) => s.state === 'running')" class="step is-running">
          <span class="tick" aria-hidden="true"><i class="spin" /></span>
          <span class="label">Deciding what to check next</span>
        </li>
      </ul>
    </template>
  </div>
</template>

<style scoped>
.card {
  margin: 0.35rem 0 0.6rem;
  border: 1px solid var(--hairline, #e4e1da);
  border-radius: 10px;
  background: var(--surface, #fff);
  overflow: hidden;
}
.card--failed { border-color: #e0c3b6; }

/* --- folded ------------------------------------------------------------- */
.folded {
  width: 100%;
  min-height: 40px;
  padding: 0.5rem 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  border: 0;
  background: none;
  font: inherit;
  font-size: 0.82rem;
  color: var(--ink-3, #8b857c);
  text-align: left;
  cursor: pointer;
}
.folded:hover { color: var(--ink-1, #1c1a17); }
.chev { font-size: 1rem; line-height: 1; }

/* --- head --------------------------------------------------------------- */
.head {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.6rem 0.75rem 0.5rem;
}
.title {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--ink-1, #1c1a17);
}
.bars { display: inline-flex; align-items: flex-end; gap: 2px; height: 12px; }
.bars i {
  width: 3px;
  border-radius: 1px;
  background: var(--accent, #007d6c);
}
.bars i:nth-child(1) { height: 6px; }
.bars i:nth-child(2) { height: 12px; }
.bars i:nth-child(3) { height: 9px; }
.card--live .bars i { animation: bob 1.1s ease-in-out infinite; }
.card--live .bars i:nth-child(2) { animation-delay: 0.14s; }
.card--live .bars i:nth-child(3) { animation-delay: 0.28s; }
@keyframes bob {
  0%, 100% { transform: scaleY(0.7); }
  50% { transform: scaleY(1); }
}

.status {
  margin-left: auto;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.78rem;
  color: var(--ink-3, #8b857c);
}
/* The one dot that earns its place: it reports live state, which nothing
   else on the card says. */
.status i {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--hairline-strong, #cfc9bf);
}
.status--live i {
  background: var(--accent, #007d6c);
  animation: pulse 1.5s ease-out infinite;
}
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(0, 125, 108, 0.35); }
  70% { box-shadow: 0 0 0 7px rgba(0, 125, 108, 0); }
  100% { box-shadow: 0 0 0 7px rgba(0, 125, 108, 0); }
}

.fold {
  border: 0;
  background: none;
  min-height: 28px;
  padding: 0 0.2rem;
  font: inherit;
  font-size: 0.76rem;
  color: var(--ink-3, #8b857c);
  text-decoration: underline;
  text-underline-offset: 2px;
  cursor: pointer;
}
.fold:hover { color: var(--ink-1, #1c1a17); }

/* --- progress ----------------------------------------------------------- */
.meter {
  height: 2px;
  background: var(--hairline, #e4e1da);
}
.meter i {
  display: block;
  height: 100%;
  background: var(--accent, #007d6c);
  transition: width 0.45s cubic-bezier(0.16, 1, 0.3, 1);
}

.count {
  margin: 0;
  padding: 0.5rem 0.75rem 0.15rem;
  font-size: 0.76rem;
  color: var(--ink-3, #8b857c);
}

/* --- steps -------------------------------------------------------------- */
.steps {
  margin: 0;
  padding: 0 0.75rem 0.7rem;
  list-style: none;
}
.step {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.5rem;
  padding: 0.22rem 0;
  font-size: 0.84rem;
  line-height: 1.5;
}
.tick {
  width: 1rem;
  flex: none;
  text-align: center;
  font-size: 0.78rem;
  color: var(--accent, #007d6c);
}
.is-failed .tick { color: #b4552d; }
.label { color: var(--ink-1, #1c1a17); }

/* Done steps are struck through and fade back — the card should read as a
   list that is emptying itself, not as a growing log. */
.is-done .label {
  color: var(--ink-3, #8b857c);
  text-decoration: line-through;
  text-decoration-thickness: 1px;
}
.is-done .detail { color: var(--ink-4, #b4ada2); text-decoration: line-through; }
.is-failed .label { color: #b4552d; }

.detail {
  margin-left: auto;
  color: var(--ink-3, #8b857c);
  font-family: var(--font-num, ui-monospace, SFMono-Regular, monospace);
  font-size: 0.76rem;
  font-variant-numeric: tabular-nums;
}

.spin {
  display: inline-block;
  width: 10px;
  height: 10px;
  border: 1.5px solid var(--hairline-strong, #cfc9bf);
  border-top-color: var(--accent, #007d6c);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

.peek {
  border: 0;
  background: none;
  min-height: 24px;
  padding: 0 0.2rem;
  font: inherit;
  font-size: 0.72rem;
  color: var(--ink-4, #b4ada2);
  text-decoration: underline;
  text-underline-offset: 2px;
  cursor: pointer;
}
.peek:hover { color: var(--accent, #007d6c); }

.code {
  flex-basis: 100%;
  margin: 0.3rem 0 0.2rem;
  padding: 0.5rem 0.6rem;
  background: var(--sunk, #f4f1ea);
  border-radius: 6px;
  font-family: var(--font-num, ui-monospace, SFMono-Regular, monospace);
  font-size: 0.72rem;
  line-height: 1.5;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  color: var(--ink-2, #6f6a62);
}

@media (prefers-reduced-motion: reduce) {
  .bars i, .status--live i, .spin { animation: none; }
  .meter i { transition: none; }
}
</style>
