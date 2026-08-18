<script setup lang="ts">
import type { ChatTurn, ChatWidgetSpec } from "../types/chat";

useHead({
  title: "Chat lab — EQ-Graph",
  meta: [{ name: "robots", content: "noindex, nofollow" }],
});

type LabCase = {
  label: string;
  note: string;
  busy?: boolean;
  error?: string;
  followups?: string[];
  turns: ChatTurn[];
};

const question = (id: string, text: string): ChatTurn => ({
  id,
  role: "user",
  list: [{ kind: "text", key: `${id}-text`, text }],
});

const answer = (id: string, list: ChatTurn["list"]): ChatTurn => ({ id, role: "assistant", list });

const completedTool = (id: string, purpose: string, sql: string, rowCount: number) => ({
  type: "tool-query_sql",
  toolCallId: id,
  state: "output-available",
  input: { purpose, sql },
  output: { ok: true, rowCount, elapsedMs: 3.8, truncated: false },
});

const chartTurn = (key: string, prompt: string, text: string, widget: ChatWidgetSpec): ChatTurn[] => [
  question(`${key}-q`, prompt),
  answer(`${key}-a`, [
    {
      kind: "tools",
      key: `${key}-tool`,
      parts: [completedTool(`${key}-query`, `Answer ${prompt.toLowerCase()}`, "SELECT … FROM reference_data", widget.rowCount)],
    },
    { kind: "widget", key: `${key}-widget`, widget },
    { kind: "text", key: `${key}-text`, text },
  ]),
];

const CASES: Record<string, LabCase> = {
  empty: {
    label: "Empty",
    note: "First arrival and example questions",
    turns: [],
  },
  working: {
    label: "Working",
    note: "User question and live SQL activity",
    busy: true,
    turns: [
      question("working-q", "Which countries occur most often in the assessed studies?"),
      answer("working-a", [{
        kind: "tools",
        key: "working-tool",
        parts: [{
          type: "tool-query_sql",
          toolCallId: "working-query",
          state: "input-available",
          input: {
            purpose: "Count assessed studies by country.",
            sql: "SELECT country, COUNT(DISTINCT study_id) AS studies\nFROM study_countries\nGROUP BY country\nORDER BY studies DESC\nLIMIT 12",
          },
        }],
      }]),
    ],
  },
  answer: {
    label: "Answer",
    note: "Long prose, ordered evidence and links",
    followups: [
      "Which methods were used?",
      "Show the linked publications.",
      "Compare the project with other valuation studies.",
    ],
    turns: [
      question("answer-q", "What does project 2014030 contribute?"),
      answer("answer-a", [
        { kind: "tools", key: "answer-tool", parts: [completedTool("answer-query", "Find the project and accepted publications.", "SELECT … FROM projects LEFT JOIN project_publications", 1)] },
        {
          kind: "text",
          key: "answer-text",
          text: "Project **2014030** supported an exploratory German EQ-5D-5L valuation study. The assessed corpus contains one accepted publication link.\n\n1. The study used composite time trade-off.\n2. It tested changes to the valuation protocol.\n3. The evidence record includes the study methods, findings and limitations.\n\nThe evidence layer contains 209 assessed publications. It does not yet cover all EuroQol publications.",
        },
      ]),
    ],
  },
  bar: {
    label: "Bar",
    note: "Ranked categories and chart actions",
    followups: ["Show the projects in the United Kingdom.", "Compare the top three countries.", "Which publications report countries?"],
    turns: chartTurn(
      "bar",
      "Which countries occur most often in the assessed studies?",
      "The United Kingdom and the Netherlands lead the current assessed study records.",
      {
        mark: "bar",
        title: "Assessed studies by country",
        encoding: { x: "country", y: "studies" },
        options: { orientation: "horizontal", color: "#007d6c" },
        rows: [
          { country: "United Kingdom", studies: 26 }, { country: "Netherlands", studies: 25 },
          { country: "Australia", studies: 15 }, { country: "China", studies: 14 },
          { country: "Germany", studies: 12 }, { country: "Indonesia", studies: 11 },
          { country: "United States", studies: 11 }, { country: "Sweden", studies: 10 },
        ],
        rowCount: 8,
      },
    ),
  },
  line: {
    label: "Line",
    note: "Time series and compact prose",
    turns: chartTurn(
      "line",
      "How has the funded portfolio changed since 2018?",
      "Recorded projects rise through 2022 and then fall in the incomplete recent years.",
      {
        mark: "line",
        title: "Funded projects by start year",
        encoding: { x: "year", y: "projects" },
        options: { color: "#2a78d6" },
        rows: [
          { year: 2018, projects: 41 }, { year: 2019, projects: 49 }, { year: 2020, projects: 53 },
          { year: 2021, projects: 66 }, { year: 2022, projects: 72 }, { year: 2023, projects: 61 },
          { year: 2024, projects: 48 }, { year: 2025, projects: 31 },
        ],
        rowCount: 8,
      },
    ),
  },
  donut: {
    label: "Donut",
    note: "Composition with a responsive legend",
    turns: chartTurn(
      "donut",
      "Which instruments appear in extracted findings?",
      "EQ-5D-5L is the largest instrument group in the assessed evidence.",
      {
        mark: "donut",
        title: "Extracted findings by instrument",
        encoding: { x: "instrument", y: "findings" },
        options: { color: "#007d6c" },
        rows: [
          { instrument: "EQ-5D-5L", findings: 526 }, { instrument: "EQ VAS", findings: 451 },
          { instrument: "EQ-5D-3L", findings: 226 }, { instrument: "EQ-5D-Y-3L", findings: 188 },
          { instrument: "EQ-5D-Y-5L", findings: 80 },
        ],
        rowCount: 5,
      },
    ),
  },
  stat: {
    label: "Stat",
    note: "One answerable number with its scope",
    turns: chartTurn(
      "stat",
      "How many extracted findings are in the assessed evidence?",
      "The current evidence layer contains 871 extracted findings.",
      {
        mark: "stat",
        title: "Extracted findings",
        encoding: { value: "findings" },
        options: { unit: "findings", color: "#007d6c" },
        rows: [{ findings: 871 }],
        rowCount: 1,
      },
    ),
  },
  table: {
    label: "Table",
    note: "Dense records and horizontal overflow",
    turns: chartTurn(
      "table",
      "Show the accepted publications for project 2014030.",
      "One publication is linked to project 2014030 in the assessed corpus.",
      {
        mark: "table",
        title: "Accepted publications for 2014030",
        encoding: { columns: ["year", "title", "journal"] },
        rows: [
          { year: 2017, title: "Valuation of the EQ-5D-5L with composite time trade-off for the German population – an exploratory study", journal: "Health and Quality of Life Outcomes" },
        ],
        rowCount: 1,
      },
    ),
  },
  error: {
    label: "Error",
    note: "A failed query with a clear recovery path",
    error: "The answer could not be completed. Try the question again.",
    turns: [
      question("error-q", "Compare every finding with every project."),
      answer("error-a", [{
        kind: "tools",
        key: "error-tool",
        parts: [{
          type: "tool-query_sql",
          toolCallId: "error-query",
          state: "output-error",
          input: { purpose: "Compare findings and projects.", sql: "SELECT …" },
          output: { ok: false, error: "The query was too broad for one response." },
        }],
      }]),
    ],
  },
};

const route = useRoute();
const router = useRouter();
const keys = Object.keys(CASES);
const selectedKey = computed(() => {
  const value = String(route.query.case ?? "empty");
  return value in CASES ? value : "empty";
});
const selected = computed(() => CASES[selectedKey.value]!);

function select(key: string) {
  router.replace({ query: { ...route.query, case: key } });
}

function simulateSend() {
  select("working");
}
</script>

<template>
  <main class="chat-lab-page">
    <ChatWorkbench
      active
      back-label="Back to app"
      :busy="selected.busy"
      :counts="{ projects: 944, works: 174, findings: 178 }"
      data-state="ready"
      :error="selected.error"
      :examples="[
        'Show the accepted publications for project 341-RA.',
        'Which instruments have the most extracted findings?',
        'Which countries have the most funded projects?',
      ]"
      :followups="selected.followups"
      :state-key="selectedKey"
      :turns="selected.turns"
      @back="navigateTo('/#chat')"
      @send="simulateSend"
    >
      <template #toolbar>
        <nav class="lab-toolbar" aria-label="Chat test states">
          <span class="lab-title"><strong>Chat lab</strong><small>{{ selected.note }}</small></span>
          <div class="lab-cases" role="tablist" aria-label="Test state">
            <button
              v-for="key in keys"
              :key="key"
              type="button"
              role="tab"
              :aria-selected="selectedKey === key"
              :class="selectedKey === key && 'is-active'"
              @click="select(key)"
            >{{ CASES[key]!.label }}</button>
          </div>
        </nav>
      </template>
    </ChatWorkbench>
  </main>
</template>

<style scoped>
.chat-lab-page{height:100dvh; overflow:hidden; background:#fff;}
.lab-toolbar{
  width:100%;
  min-height:48px;
  padding:0 max(1rem, calc((100% - 50rem) / 2));
  display:flex;
  align-items:center;
  gap:1rem;
  flex:none;
  border-bottom:1px solid #d9d8d2;
  background:#f7f7f5;
  color:#5c5c56;
}
.lab-title{min-width:9rem; display:flex; align-items:baseline; gap:.55rem; white-space:nowrap;}
.lab-title strong{color:#1a1a17; font:600 .68rem var(--font-num); letter-spacing:.08em; text-transform:uppercase;}
.lab-title small{font-size:.72rem;}
.lab-cases{min-width:0; display:flex; gap:.1rem; overflow-x:auto; scrollbar-width:none;}
.lab-cases::-webkit-scrollbar{display:none;}
.lab-cases button{
  min-height:32px;
  padding:0 .58rem;
  flex:none;
  border:0;
  border-radius:5px;
  background:transparent;
  color:#74746d;
  font-size:.72rem;
  cursor:pointer;
}
.lab-cases button:hover{background:#ecece8; color:#1a1a17;}
.lab-cases button.is-active{background:#fff; color:#007d6c; box-shadow:inset 0 0 0 1px #cbc9c1;}
.lab-cases button:focus-visible{outline:2px solid #007d6c; outline-offset:-1px;}
@media (max-width:700px){
  .lab-toolbar{padding:0 1rem; gap:.65rem;}
  .lab-title{min-width:auto;}
  .lab-title small{display:none;}
  .lab-cases button{min-height:44px;}
}
</style>
