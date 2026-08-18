<script setup lang="ts">
import { Chat } from "@ai-sdk/vue";
import type { DemoResearchData } from "../../shared/types/demo";
import type { ChatSegment, ChatTurn } from "../types/chat";

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
    studies: number;
    works: number;
    acceptedAttributions: number;
    worksWithFindings: number;
    findings: number;
  };
};

/* Suggested questions, built from the reference data rather than written by
   hand. A hardcoded list goes stale the moment the data moves, and worse, it
   can offer a question the data cannot answer — which is the fastest way to
   lose someone's trust on their first click.

   Every question below names something that is actually in the graph: a real
   project, a real instrument, a real working group. Three are shown at a time
   and "Other questions" deals the next three, so the pool is a way to browse
   what is here rather than a fixed menu. */
function buildQuestionPool(data: DemoResearchData): string[] {
  const pool: string[] = [];
  const pick = <T,>(list: T[] | undefined, n: number): T[] => (list ?? []).slice(0, n);

  // Questions that hold whatever the data contains.
  pool.push(
    "Which countries have the most funded projects?",
    "Which instruments have the most extracted findings?",
    "Which journals published this work?",
    "Which conditions have been studied?",
    "Where were these studies run?",
  );

  // Questions naming real records, so a click lands on something that exists.
  for (const project of pick(data.projects, 2)) {
    if (project?.id) pool.push(`Show the accepted publications for project ${project.id}.`);
  }
  for (const instrument of pick(data.instruments?.filter((entry) => entry.isEuroQol), 3)) {
    if (instrument?.name) pool.push(`Where has ${instrument.name} been used?`);
  }
  for (const group of pick(data.workingGroups, 2)) {
    if (group?.name) pool.push(`What has the ${group.name} working group produced?`);
  }
  const metrics = [...new Set((data.findings ?? []).map((finding) => finding.metric).filter(Boolean))];
  for (const metric of metrics.slice(0, 2)) {
    pool.push(`What does the evidence say about ${String(metric).replace(/_/g, " ")}?`);
  }

  return pool;
}

const OPEN = "<followups>";
const CLOSE = "</followups>";
const chat = new Chat({});
let graphRefreshTimer: ReturnType<typeof setInterval> | undefined;

const {
  data: graphStatus,
  error: graphStatusError,
  refresh: refreshGraphStatus,
} = await useFetch<DataStatus>("/api/graph/status");

const busy = computed(() => chat.status === "submitted" || chat.status === "streaming");
const counts = computed(() => graphStatus.value?.counts ?? {
  projects: props.data.portfolio.projects,
  studies: props.data.portfolio.studies,
  works: props.data.portfolio.works,
  findings: props.data.portfolio.findings,
});
const dataState = computed(() => graphStatusError.value
  ? "error" as const
  : graphStatus.value?.ok
    ? "ready" as const
    : "loading" as const);

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

const turns = computed<ChatTurn[]>(() => chat.messages.map((message: any) => ({
  id: message.id,
  role: message.role,
  list: segments(message),
})));

function send(question: string) {
  chat.sendMessage({ text: question });
}

onMounted(() => {
  graphRefreshTimer = setInterval(() => refreshGraphStatus(), 60_000);
});

onBeforeUnmount(() => {
  if (graphRefreshTimer) clearInterval(graphRefreshTimer);
});

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
</script>

<template>
  <ChatWorkbench
    id="chat"
    :active="active"
    :busy="busy"
    :counts="counts"
    :data-state="dataState"
    :error="chat.error?.message"
    :examples="examples"
    :followups="followups"
    :turns="turns"
    :can-reshuffle="questionPool.length > 3"
    @back="emit('return-story')"
    @reshuffle="reshuffle"
    @send="send"
  />
</template>
