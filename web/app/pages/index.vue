<script setup lang="ts">
import type { DemoResearchData } from "../../shared/types/demo";
import { setAnalyticsScreen, syncAnalyticsStoryScreen } from "../utils/analytics";

useHead({
  title: "EQ-Graph — A knowledge graph of EuroQol-funded research",
  meta: [
    {
      name: "description",
      content: "A knowledge graph of EuroQol-funded research. Projects, publications, people, and findings, linked and ready to query.",
    },
    { property: "og:title", content: "EQ-Graph — A knowledge graph of EuroQol-funded research" },
    { property: "og:description", content: "Projects, publications, people, and findings, linked and ready to query." },
  ],
});

const { data, error } = await useFetch<DemoResearchData>("/api/story");

type ChatEntry = {
  source?: "skip" | "cta" | "story";
  returnY?: number;
  question?: string;
};

const view = ref<"story" | "chat">("story");
const storyReturnY = ref(0);
const storyComponent = ref<{
  goHome: () => void;
  restoreAt: (top: number) => Promise<void>;
} | null>(null);
const chatComponent = ref<{
  send: (question: string, options?: { newSession?: boolean; source?: "story" }) => void;
} | null>(null);

function setDocumentMode(chat: boolean) {
  if (!import.meta.client) return;
  document.documentElement.classList.toggle("is-chat-cockpit", chat);
  document.body.classList.toggle("is-chat-cockpit", chat);
}

async function enterChat(entry: ChatEntry = {}) {
  const chatUrl = `${location.pathname}${location.search}#chat`;
  if (location.hash !== "#chat") history.replaceState(history.state, "", chatUrl);
  if (view.value === "chat") return;
  storyReturnY.value = entry.returnY ?? window.scrollY;
  const activate = async () => {
    view.value = "chat";
    setDocumentMode(true);
    setAnalyticsScreen("chat");
    await nextTick();
    if (entry.question) {
      chatComponent.value?.send(entry.question, { newSession: entry.source === "story", source: "story" });
      await nextTick();
    }
    window.scrollTo(0, 0);
  };

  const transition = (document as Document & {
    startViewTransition?: (update: () => Promise<void>) => { finished: Promise<void> };
  }).startViewTransition;
  if (transition && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    await transition.call(document, activate).finished.catch(() => undefined);
  } else {
    await activate();
  }
}

async function returnToStory() {
  if (view.value === "story") return;
  const restore = async () => {
    view.value = "story";
    setDocumentMode(false);
    history.replaceState(history.state, "", `${location.pathname}${location.search}`);
    await nextTick();
    await storyComponent.value?.restoreAt(storyReturnY.value);
    syncAnalyticsStoryScreen();
  };
  const transition = (document as Document & {
    startViewTransition?: (update: () => Promise<void>) => { finished: Promise<void> };
  }).startViewTransition;
  if (transition && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    await transition.call(document, restore).finished.catch(() => undefined);
  } else {
    await restore();
  }
}

async function returnHome() {
  const restore = async () => {
    view.value = "story";
    setDocumentMode(false);
    history.replaceState(history.state, "", `${location.pathname}${location.search}`);
    await nextTick();
    storyComponent.value?.goHome();
    syncAnalyticsStoryScreen();
  };
  const transition = (document as Document & {
    startViewTransition?: (update: () => Promise<void>) => { finished: Promise<void> };
  }).startViewTransition;
  if (transition && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    await transition.call(document, restore).finished.catch(() => undefined);
  } else {
    await restore();
  }
}

function syncViewToHash() {
  /* /?ask=<question>#chat opens the chat and sends the question at once. */
  const asked = new URLSearchParams(location.search).get("ask");
  if (asked) {
    history.replaceState(history.state, "", `${location.pathname}#chat`);
    void enterChat({ source: "story", question: asked });
    return;
  }
  if (location.hash === "#chat") {
    void enterChat({ source: "skip" });
    return;
  }
  if (view.value === "chat") void returnToStory();
}

function resetRestoredLandingPage(event: PageTransitionEvent) {
  if (!event.persisted || location.hash === "#chat" || new URLSearchParams(location.search).has("ask")) return;
  window.scrollTo(0, 0);
  storyComponent.value?.goHome();
}

onMounted(() => {
  window.addEventListener("hashchange", syncViewToHash);
  window.addEventListener("pageshow", resetRestoredLandingPage);
  if (location.hash !== "#chat" && !new URLSearchParams(location.search).has("ask")) window.scrollTo(0, 0);
  syncViewToHash();
});

onBeforeUnmount(() => {
  window.removeEventListener("hashchange", syncViewToHash);
  window.removeEventListener("pageshow", resetRestoredLandingPage);
  setDocumentMode(false);
});
</script>

<template>
  <main v-if="data" :class="['landing-v2-root', view === 'chat' && 'is-chat-mode']">
    <StoryHorizontal
      ref="storyComponent"
      :active="view === 'story'"
      @enter-chat="enterChat"
    />
    <EvidenceChat
      ref="chatComponent"
      :data="data"
      :active="view === 'chat'"
      @return-home="returnHome"
      @return-story="returnToStory"
    />
  </main>

  <!-- The mark stays in the corner it occupies on every other screen rather than sitting in the middle of this one.  -->
  <main v-else class="load-state">
    <SiteHeader current="story" />
    <p v-if="error" class="load-error">The interface reference data did not load. Restart the application and try again.</p>
    <BrandLoader v-else label="Loading research data" />
  </main>
</template>
