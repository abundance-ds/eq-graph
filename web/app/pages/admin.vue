<script setup lang="ts">
useHead({
  title: "EQ-Graph activity",
  meta: [{ name: "robots", content: "noindex,nofollow,noarchive" }],
});

type Summary = {
  totals: {
    pageViews: number;
    activeMs: number;
    messagesSent: number;
    responsesReceived: number;
    chatErrors: number;
    chatAborts: number;
    responseP50Ms: number;
    responseP95Ms: number;
    apiRequests: number;
  };
  pages: Array<{ path: string; views: number; averageActiveMs: number; averageScrollPct: number; maximumScrollPct: number }>;
  screens: Array<{ screen: string; views: number; activeMs: number }>;
  devices: Array<{ device: string; views: number }>;
  api: Array<{ route: string; requests: number; errors: number; averageDurationMs: number }>;
};

type ChatRow = {
  turnId: string;
  startedAt: number;
  source: string;
  question: string | null;
  answer: string | null;
  status: string;
  durationMs: number | null;
  modelSteps: number;
  toolCalls: number;
  chartType: string | null;
  errorType: string | null;
};

type Health = {
  release: string;
  uptimeSeconds: number;
  model: string;
  usage: { hour: number; day: number; active: number; limits: { hour: number; day: number; active: number } };
  analytics: { pageViews: number; chatTurns: number; apiRequests: number; lastChat: unknown; lastApiError: unknown };
};

const status = ref<"loading" | "locked" | "ready" | "error">("loading");
const problem = ref("");
const token = ref("");
const summary = ref<Summary | null>(null);
const chats = ref<ChatRow[]>([]);
const health = ref<Health | null>(null);

function dateValue(offsetDays: number): string {
  const date = new Date();
  date.setDate(date.getDate() + offsetDays);
  return date.toISOString().slice(0, 10);
}

const from = ref(dateValue(-6));
const through = ref(dateValue(0));

function queryString(): string {
  const end = new Date(`${through.value}T00:00:00Z`);
  end.setUTCDate(end.getUTCDate() + 1);
  return new URLSearchParams({
    from: `${from.value}T00:00:00Z`,
    to: end.toISOString(),
  }).toString();
}

const exportUrl = computed(() => `/api/admin/export?${queryString()}`);

function duration(value: number): string {
  if (!value) return "0s";
  if (value < 1_000) return `${Math.round(value)}ms`;
  const seconds = Math.round(value / 1_000);
  if (seconds < 60) return `${seconds}s`;
  const minutes = Math.floor(seconds / 60);
  return `${minutes}m ${seconds % 60}s`;
}

function moment(value: number): string {
  return new Intl.DateTimeFormat(undefined, { dateStyle: "medium", timeStyle: "short" }).format(value);
}

const screenLabels: Record<string, string> = {
  landing: "Landing",
  "story-01": "Research community",
  "story-02": "Research programmes",
  "story-03": "Research over time",
  "story-04": "Citation reach",
  "story-05": "Measure use",
  "story-end": "Story end",
  chat: "Chat",
  about: "About",
};
const screenOrder = Object.keys(screenLabels);
const orderedScreens = computed(() => [...(summary.value?.screens ?? [])]
  .sort((left, right) => screenOrder.indexOf(left.screen) - screenOrder.indexOf(right.screen)));
const maximumScreenViews = computed(() => Math.max(1, ...orderedScreens.value.map((entry) => entry.views)));

async function load() {
  problem.value = "";
  try {
    const query = queryString();
    const [nextSummary, nextChats, nextHealth] = await Promise.all([
      $fetch<Summary>(`/api/admin/summary?${query}`),
      $fetch<{ chats: ChatRow[] }>(`/api/admin/chats?${query}&limit=100`),
      $fetch<Health>("/api/admin/health"),
    ]);
    summary.value = nextSummary;
    chats.value = nextChats.chats;
    health.value = nextHealth;
    status.value = "ready";
  } catch (error: any) {
    if (error?.statusCode === 401 || error?.response?.status === 401) {
      status.value = "locked";
      return;
    }
    problem.value = "The activity data could not be loaded.";
    status.value = "error";
  }
}

async function openAdmin(supplied = token.value) {
  if (!supplied.trim()) return;
  problem.value = "";
  status.value = "loading";
  try {
    await $fetch("/api/admin/session", { method: "POST", body: { token: supplied.trim() } });
    token.value = "";
    await load();
  } catch {
    problem.value = "The admin token is not valid.";
    status.value = "locked";
  }
}

async function logout() {
  await $fetch("/api/admin/session", { method: "DELETE" }).catch(() => undefined);
  summary.value = null;
  chats.value = [];
  health.value = null;
  status.value = "locked";
}

onMounted(async () => {
  const fragment = decodeURIComponent(location.hash.slice(1).replace(/^token=/, ""));
  if (location.hash) history.replaceState(history.state, "", `${location.pathname}${location.search}`);
  if (fragment) await openAdmin(fragment);
  else await load();
});
</script>

<template>
  <main class="admin-root">
    <div class="admin-grid" aria-hidden="true"><i v-for="index in 12" :key="index" /></div>
    <header class="admin-header">
      <a href="/" class="admin-wordmark">EQ<span>–</span>GRAPH</a>
      <div v-if="status === 'ready'" class="admin-header-actions">
        <a :href="exportUrl">Export</a>
        <button type="button" @click="logout">Lock</button>
      </div>
    </header>

    <section v-if="status === 'loading'" class="admin-gate" aria-live="polite">
      <p>Loading activity…</p>
    </section>

    <section v-else-if="status === 'locked'" class="admin-gate">
      <div>
        <h1>Admin access</h1>
        <p>Open the private admin link or enter the token.</p>
        <form @submit.prevent="openAdmin()">
          <input v-model="token" type="password" autocomplete="current-password" aria-label="Admin token" />
          <button type="submit">Open activity</button>
        </form>
        <p v-if="problem" class="admin-error" role="alert">{{ problem }}</p>
      </div>
    </section>

    <section v-else-if="status === 'error'" class="admin-gate">
      <div>
        <h1>Activity unavailable</h1>
        <p>{{ problem }}</p>
        <button type="button" @click="load">Try again</button>
      </div>
    </section>

    <div v-else-if="summary && health" class="admin-content">
      <section class="admin-intro">
        <div>
          <h1>EQ-Graph activity</h1>
          <p>Unlinked product use, chat outcomes, and service state.</p>
        </div>
        <form class="admin-range" @submit.prevent="load">
          <label>From <input v-model="from" type="date" /></label>
          <label>Through <input v-model="through" type="date" /></label>
          <button type="submit">Update</button>
        </form>
      </section>

      <section class="admin-totals" aria-label="Activity totals">
        <div><strong>{{ summary.totals.pageViews.toLocaleString() }}</strong><span>Page views</span></div>
        <div><strong>{{ duration(summary.totals.activeMs) }}</strong><span>Visible time</span></div>
        <div><strong>{{ summary.totals.messagesSent.toLocaleString() }}</strong><span>Questions</span></div>
        <div><strong>{{ summary.totals.responsesReceived.toLocaleString() }}</strong><span>Answers</span></div>
        <div><strong>{{ duration(summary.totals.responseP50Ms) }}</strong><span>Median answer</span></div>
      </section>

      <div class="admin-main-grid">
        <section class="admin-section admin-reach">
          <header><h2>Story reach</h2><p>Views and visible time by screen</p></header>
          <ol>
            <li v-for="entry in orderedScreens" :key="entry.screen">
              <span>{{ screenLabels[entry.screen] ?? entry.screen }}</span>
              <i><b :style="{ width: `${entry.views / maximumScreenViews * 100}%` }" /></i>
              <strong>{{ entry.views }}</strong>
              <small>{{ duration(entry.activeMs) }}</small>
            </li>
          </ol>
        </section>

        <section class="admin-section admin-state">
          <header><h2>Service state</h2><p>Current process and global limits</p></header>
          <dl>
            <div><dt>Release</dt><dd>{{ health.release }}</dd></div>
            <div><dt>Model</dt><dd>{{ health.model }}</dd></div>
            <div><dt>Uptime</dt><dd>{{ duration(health.uptimeSeconds * 1_000) }}</dd></div>
            <div><dt>Questions this hour</dt><dd>{{ health.usage.hour }} / {{ health.usage.limits.hour }}</dd></div>
            <div><dt>Questions in 24 hours</dt><dd>{{ health.usage.day }} / {{ health.usage.limits.day }}</dd></div>
            <div><dt>Active now</dt><dd>{{ health.usage.active }} / {{ health.usage.limits.active }}</dd></div>
          </dl>
        </section>
      </div>

      <div class="admin-main-grid">
        <section class="admin-section">
          <header><h2>Pages</h2><p>Reach, attention, and scroll depth</p></header>
          <div class="admin-table-wrap">
            <table>
              <thead><tr><th>Page</th><th>Views</th><th>Average time</th><th>Average scroll</th></tr></thead>
              <tbody><tr v-for="page in summary.pages" :key="page.path">
                <td>{{ page.path }}</td><td>{{ page.views }}</td><td>{{ duration(page.averageActiveMs) }}</td><td>{{ page.averageScrollPct }}%</td>
              </tr></tbody>
            </table>
          </div>
          <ul class="admin-devices" aria-label="Views by device class">
            <li v-for="device in summary.devices" :key="device.device">
              <span>{{ device.device }}</span><strong>{{ device.views }}</strong>
            </li>
          </ul>
        </section>

        <section class="admin-section">
          <header><h2>API requests</h2><p>Volume, errors, and response time</p></header>
          <div class="admin-table-wrap">
            <table>
              <thead><tr><th>Route</th><th>Requests</th><th>Errors</th><th>Average</th></tr></thead>
              <tbody><tr v-for="route in summary.api" :key="route.route">
                <td>{{ route.route }}</td><td>{{ route.requests }}</td><td>{{ route.errors }}</td><td>{{ duration(route.averageDurationMs) }}</td>
              </tr></tbody>
            </table>
          </div>
        </section>
      </div>

      <section class="admin-section admin-chats">
        <header>
          <div><h2>Recent questions and answers</h2><p>Final visible answers only; tool traces are not stored</p></div>
          <p>{{ summary.totals.chatErrors }} errors · {{ summary.totals.chatAborts }} stopped</p>
        </header>
        <ol v-if="chats.length">
          <li v-for="chat in chats" :key="chat.turnId">
            <div class="admin-chat-meta">
              <time>{{ moment(chat.startedAt) }}</time>
              <span>{{ chat.source }}</span>
              <span :class="`is-${chat.status}`">{{ chat.status }}</span>
              <span>{{ duration(chat.durationMs ?? 0) }}</span>
              <span>{{ chat.modelSteps }} model steps</span>
            </div>
            <p class="admin-question">{{ chat.question ?? "Question text expired" }}</p>
            <p v-if="chat.answer" class="admin-answer">{{ chat.answer }}</p>
            <p v-else-if="chat.errorType" class="admin-answer is-error">{{ chat.errorType }}</p>
          </li>
        </ol>
        <p v-else class="admin-empty">No chat requests in this period.</p>
      </section>
    </div>
  </main>
</template>

<style scoped>
.admin-root {
  --paper: #fcfcfb;
  --ink: #1a1a17;
  --muted: #71716a;
  --faint: #9b9b93;
  --line: #dcdbd5;
  --sunk: #f3f3f0;
  --accent: #007d6c;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  background: var(--paper);
  color: var(--ink);
  font-family: "Instrument Sans", sans-serif;
}
.admin-grid { position: fixed; inset: 0; z-index: 0; display: grid; grid-template-columns: repeat(12, 1fr); pointer-events: none; }
.admin-grid i { border-left: 1px solid rgba(26, 26, 23, .035); }
.admin-grid i:last-child { border-right: 1px solid rgba(26, 26, 23, .035); }
.admin-header {
  height: 4.8rem;
  padding: 0 clamp(1.2rem, 3.35vw, 3rem);
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--line);
  background: rgba(252, 252, 251, .94);
}
.admin-wordmark { color: var(--ink); font-weight: 600; letter-spacing: -.045em; text-decoration: none; }
.admin-wordmark span { margin: 0 .08em; color: var(--accent); }
.admin-header-actions { display: flex; align-items: center; gap: 1.2rem; }
.admin-header-actions a, .admin-header-actions button {
  border: 0; background: none; color: var(--muted); font: 500 .78rem/1 inherit; text-decoration: none; cursor: pointer;
}
.admin-header-actions a:hover, .admin-header-actions button:hover { color: var(--accent); }
.admin-content { width: min(1180px, calc(100% - 2.4rem)); margin: 0 auto; position: relative; z-index: 1; }
.admin-intro { min-height: 12rem; display: flex; align-items: flex-end; justify-content: space-between; gap: 2rem; padding: 3.5rem 0 2rem; }
.admin-intro h1 { margin: 0; max-width: 12ch; font-size: clamp(2.3rem, 5vw, 4.8rem); font-weight: 500; line-height: .96; letter-spacing: -.06em; }
.admin-intro p { margin: 1rem 0 0; color: var(--muted); font-size: .9rem; }
.admin-range { display: flex; align-items: flex-end; gap: .8rem; }
.admin-range label { display: grid; gap: .3rem; color: var(--muted); font-size: .68rem; }
.admin-range input { width: 100%; min-width: 0; min-height: 38px; box-sizing: border-box; padding: .4rem .55rem; border: 1px solid var(--line); background: var(--paper); color: var(--ink); font: 400 .72rem "IBM Plex Mono", monospace; }
.admin-range button, .admin-gate button { min-height: 38px; padding: .5rem .8rem; border: 1px solid var(--ink); background: var(--ink); color: var(--paper); font: 500 .75rem inherit; cursor: pointer; }
.admin-totals { display: grid; grid-template-columns: repeat(5, 1fr); border-block: 1px solid var(--ink); }
.admin-totals div { min-height: 6.7rem; padding: 1.15rem 1rem 1rem 0; display: flex; flex-direction: column; justify-content: space-between; border-right: 1px solid var(--line); }
.admin-totals div:not(:first-child) { padding-left: 1rem; }
.admin-totals div:last-child { border-right: 0; }
.admin-totals strong { font: 500 clamp(1.75rem, 3vw, 2.7rem)/1 "IBM Plex Mono", monospace; letter-spacing: -.06em; }
.admin-totals span { color: var(--muted); font-size: .72rem; }
.admin-main-grid { display: grid; grid-template-columns: minmax(0, 1.55fr) minmax(18rem, .8fr); gap: clamp(2rem, 5vw, 5rem); }
.admin-section { min-width: 0; padding: 2.6rem 0 3rem; border-bottom: 1px solid var(--line); }
.admin-section > header { min-height: 3rem; display: flex; justify-content: space-between; gap: 1rem; margin-bottom: 1.3rem; }
.admin-section h2 { margin: 0; font-size: 1rem; font-weight: 600; letter-spacing: -.02em; }
.admin-section header p { margin: .25rem 0 0; color: var(--muted); font-size: .7rem; }
.admin-reach ol, .admin-chats ol { margin: 0; padding: 0; list-style: none; }
.admin-reach li { min-height: 2.6rem; display: grid; grid-template-columns: minmax(8.7rem, 1.2fr) minmax(6rem, 2fr) 2.5rem 4rem; align-items: center; gap: .75rem; border-top: 1px solid var(--line); }
.admin-reach li > span { font-size: .78rem; }
.admin-reach li > i { height: 3px; display: block; background: var(--sunk); }
.admin-reach li > i b { height: 100%; display: block; background: var(--accent); }
.admin-reach li > strong, .admin-reach li > small { font-family: "IBM Plex Mono", monospace; font-weight: 400; text-align: right; }
.admin-reach li > strong { font-size: .75rem; }
.admin-reach li > small { color: var(--muted); font-size: .65rem; }
.admin-state dl { margin: 0; }
.admin-state dl div { min-height: 2.6rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; border-top: 1px solid var(--line); }
.admin-state dt { color: var(--muted); font-size: .72rem; }
.admin-state dd { margin: 0; max-width: 55%; overflow: hidden; font: 400 .68rem "IBM Plex Mono", monospace; text-overflow: ellipsis; white-space: nowrap; }
.admin-table-wrap { overflow-x: auto; }
.admin-section table { width: 100%; border-collapse: collapse; font-size: .73rem; }
.admin-section th, .admin-section td { padding: .65rem .5rem .65rem 0; border-top: 1px solid var(--line); text-align: left; white-space: nowrap; }
.admin-section th { color: var(--muted); font-weight: 400; }
.admin-section td:not(:first-child) { font-family: "IBM Plex Mono", monospace; font-size: .68rem; }
.admin-devices { margin: 1rem 0 0; padding: 0; display: flex; flex-wrap: wrap; gap: .55rem 1.2rem; list-style: none; }
.admin-devices li { display: flex; gap: .45rem; color: var(--muted); font-size: .68rem; text-transform: capitalize; }
.admin-devices strong { color: var(--ink); font: 400 .68rem "IBM Plex Mono", monospace; }
.admin-chats { padding-bottom: 5rem; }
.admin-chats > header > p { text-align: right; }
.admin-chats li { padding: 1.4rem 0 1.6rem; border-top: 1px solid var(--line); }
.admin-chat-meta { display: flex; flex-wrap: wrap; gap: .5rem 1rem; color: var(--muted); font: 400 .62rem "IBM Plex Mono", monospace; }
.admin-chat-meta span.is-success { color: var(--accent); }
.admin-chat-meta span.is-error { color: #a23c2a; }
.admin-question { margin: .8rem 0 .45rem; max-width: 70ch; font-size: .92rem; font-weight: 600; line-height: 1.45; }
.admin-answer { margin: 0; max-width: 85ch; color: #454540; font-size: .82rem; line-height: 1.55; white-space: pre-line; }
.admin-answer.is-error, .admin-error { color: #a23c2a; }
.admin-empty { padding: 2rem 0; border-top: 1px solid var(--line); color: var(--muted); }
.admin-gate { min-height: calc(100vh - 4.8rem); position: relative; z-index: 1; display: grid; place-items: center; padding: 2rem; }
.admin-gate > div { width: min(30rem, 100%); }
.admin-gate h1 { margin: 0; font-size: clamp(2.4rem, 6vw, 4rem); font-weight: 500; letter-spacing: -.055em; }
.admin-gate p { color: var(--muted); }
.admin-gate form { margin-top: 1.5rem; display: flex; }
.admin-gate input { min-width: 0; flex: 1; padding: .65rem; border: 1px solid var(--line); background: var(--paper); }
.admin-gate button { flex: none; }
button:focus-visible, a:focus-visible, input:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }

@media (max-width: 760px) {
  .admin-header { padding-inline: 1rem; }
  .admin-content { width: calc(100% - 2rem); }
  .admin-intro { align-items: flex-start; flex-direction: column; padding-top: 2.4rem; }
  .admin-range { width: 100%; display: grid; grid-template-columns: 1fr 1fr; }
  .admin-range button { grid-column: 1 / -1; }
  .admin-totals { grid-template-columns: 1fr 1fr; }
  .admin-totals div { min-height: 5.5rem; border-bottom: 1px solid var(--line); }
  .admin-totals div:nth-child(2n) { border-right: 0; }
  .admin-totals div:last-child { grid-column: 1 / -1; }
  .admin-main-grid { grid-template-columns: 1fr; gap: 0; }
  .admin-reach li { grid-template-columns: minmax(0, 1.3fr) minmax(2rem, 1fr) 1.5rem 2.7rem; gap: .45rem; }
  .admin-section > header > p { max-width: 45%; text-align: right; }
  .admin-header-actions { gap: .7rem; }
}
</style>
