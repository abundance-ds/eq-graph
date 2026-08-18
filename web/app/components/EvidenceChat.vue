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
    works: number;
    acceptedAttributions: number;
    worksWithFindings: number;
    findings: number;
  };
};

const EXAMPLES = [
  "Show the accepted publications for project 2014030.",
  "Which instruments have the most extracted findings?",
  "Which countries occur most often in the assessed studies?",
  "What does the evidence report about ceiling effects?",
];

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
</script>

<template>
  <ChatWorkbench
    id="chat"
    :active="active"
    :busy="busy"
    :counts="counts"
    :data-state="dataState"
    :error="chat.error?.message"
    :examples="EXAMPLES"
    :followups="followups"
    :turns="turns"
    @back="emit('return-story')"
    @send="send"
  />
</template>
