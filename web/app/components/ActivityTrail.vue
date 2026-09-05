<script setup lang="ts">
type Part = Record<string, any>;

const props = defineProps<{
  parts: Part[];
  thinking?: boolean;
}>();

type Step = {
  id: string;
  state: "running" | "done" | "failed";
  label: string;
  detail: string;
  query: string;
};

function tidy(value: unknown): string {
  const text = String(value ?? "").trim().replace(/\.$/, "");
  if (!text) return "Run tool";
  return text.charAt(0).toUpperCase() + text.slice(1);
}

function stepLabel(part: Part, input: Record<string, any>): string {
  if (part.type === "tool-show_visualization") {
    const mark = String(input.visualization?.mark ?? "data");
    return mark === "network" ? "Render relationship network" : `Render ${mark} chart`;
  }
  return tidy(input.purpose || "Run SQL query");
}

const steps = computed<Step[]>(() => props.parts.map((part, index) => {
  const input = part.input ?? {};
  const output = part.output;
  const stopped = part.state === "output-available" || part.state === "output-error";
  const failed = part.state === "output-error" || (stopped && output?.ok === false);
  const rows = Number(output?.rowCount ?? 0);

  return {
    id: part.toolCallId ?? `${part.type}-${index}`,
    state: failed ? "failed" : stopped ? "done" : "running",
    label: stepLabel(part, input),
    detail: failed
      ? String(output?.error ?? part.errorText ?? "Query failed")
      : stopped
        ? `${rows.toLocaleString("en")} ${rows === 1 ? "result" : "results"}${output?.truncated ? " · trimmed" : ""}`
        : "",
    query: part.type === "tool-query_sql" ? String(input.sql ?? "") : "",
  };
}));

const live = computed(() => steps.value.some((step) => step.state === "running") || Boolean(props.thinking));
const openedByHand = ref(false);
const open = computed(() => live.value || openedByHand.value);
const openedQueries = ref<Record<string, boolean>>({});

function toggleQuery(id: string) {
  openedQueries.value = { ...openedQueries.value, [id]: !openedQueries.value[id] };
}
</script>

<template>
  <div v-if="steps.length || thinking" :class="['activity', live && 'is-live']">
    <button v-if="!open" type="button" class="activity-summary" @click="openedByHand = true">
      <span aria-hidden="true">✓</span>
      {{ steps.length }} {{ steps.length === 1 ? "step" : "steps" }}
      <i aria-hidden="true">›</i>
    </button>

    <template v-else>
      <ul class="activity-list">
        <li v-for="step in steps" :key="step.id" :class="`is-${step.state}`">
          <span class="activity-mark" aria-hidden="true">
            <i v-if="step.state === 'running'" />
            <template v-else>{{ step.state === "done" ? "✓" : "!" }}</template>
          </span>
          <span class="activity-label">{{ step.label }}</span>
          <span v-if="step.detail" class="activity-detail">{{ step.detail }}</span>
          <button
            v-if="step.query"
            type="button"
            class="activity-query"
            :aria-expanded="Boolean(openedQueries[step.id])"
            @click="toggleQuery(step.id)"
          >SQL</button>
          <pre v-if="openedQueries[step.id]" class="activity-code">{{ step.query }}</pre>
        </li>

        <li v-if="thinking && !steps.some((step) => step.state === 'running')" class="is-running">
          <span class="activity-mark" aria-hidden="true"><i /></span>
          <span class="activity-label">Preparing answer</span>
        </li>
      </ul>

      <button v-if="!live" type="button" class="activity-hide" @click="openedByHand = false">Hide work</button>
    </template>
  </div>
</template>

<style scoped>
.activity {
  margin: .15rem 0 .45rem;
}
.activity-summary,
.activity-hide,
.activity-query {
  border: 0;
  background: none;
  font: inherit;
  cursor: pointer;
}
.activity-summary {
  min-height: 34px;
  padding: 0;
  display: inline-flex;
  align-items: center;
  gap: .42rem;
  color: var(--ink-3, #8e8e86);
  font-size: .78rem;
}
.activity-summary span { color: var(--accent, #007d6c); }
.activity-summary i { font-style: normal; font-size: 1rem; }
.activity-summary:hover { color: var(--ink-1, #1a1a17); }
.activity-list {
  margin: 0;
  padding: .15rem 0;
  list-style: none;
}
.activity-list li {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: .45rem;
  padding: .26rem 0;
  color: var(--ink-2, #5c5c56);
  font-size: .82rem;
  line-height: 1.45;
}
.activity-mark {
  width: 1rem;
  flex: none;
  color: var(--accent, #007d6c);
  text-align: center;
}
.activity-mark i {
  display: inline-block;
  width: 9px;
  height: 9px;
  border: 1.5px solid var(--hairline-strong, #cbc9c1);
  border-top-color: var(--accent, #007d6c);
  border-radius: 50%;
  animation: activity-spin .75s linear infinite;
}
.activity-list .is-failed .activity-mark,
.activity-list .is-failed .activity-label { color: #a23c2a; }
.activity-detail {
  margin-left: auto;
  color: var(--ink-3, #8e8e86);
  font: 400 .72rem var(--font-num, ui-monospace, monospace);
  font-variant-numeric: tabular-nums;
}
.activity-query {
  min-height: 24px;
  padding: 0 .15rem;
  color: var(--ink-3, #8e8e86);
  font: 500 .67rem var(--font-num, ui-monospace, monospace);
  letter-spacing: .04em;
}
.activity-query:hover { color: var(--accent, #007d6c); }
.activity-code {
  flex-basis: 100%;
  margin: .3rem 0 .15rem 1.45rem;
  padding: .65rem .75rem;
  overflow-x: auto;
  border-radius: 4px;
  background: var(--sunk, #f8f8f7);
  color: var(--ink-2, #5c5c56);
  font: 400 .7rem/1.55 var(--font-num, ui-monospace, monospace);
  white-space: pre-wrap;
}
.activity-hide {
  min-height: 28px;
  padding: 0;
  color: var(--ink-3, #8e8e86);
  font-size: .72rem;
}
.activity-hide:hover { color: var(--ink-1, #1a1a17); }
.activity-summary:focus-visible,
.activity-hide:focus-visible,
.activity-query:focus-visible {
  outline: 2px solid var(--accent, #007d6c);
  outline-offset: 2px;
}
@keyframes activity-spin { to { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) {
  .activity-mark i { animation: none; }
}
</style>
