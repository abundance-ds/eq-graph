<script setup lang="ts">
import type { DemoResearchData } from "../../shared/types/demo";

useHead({
  title: "EQ-Graph — EuroQol Research Explorer",
  meta: [
    {
      name: "description",
      content: "Explore EuroQol studies, instruments, methods, populations, findings, and research gaps.",
    },
  ],
});

const { data, error } = await useFetch<DemoResearchData>("/api/story");

type ChatEntry = {
  source?: "skip" | "cta" | "story";
  returnY?: number;
};

const view = ref<"story" | "chat">("story");
const storyReturnY = ref(0);
const storyComponent = ref<{ restoreAt: (top: number) => void } | null>(null);

function setDocumentMode(chat: boolean) {
  if (!import.meta.client) return;
  document.documentElement.classList.toggle("is-chat-cockpit", chat);
  document.body.classList.toggle("is-chat-cockpit", chat);
}

async function enterChat(entry: ChatEntry = {}) {
  if (view.value === "chat") return;
  storyReturnY.value = entry.returnY ?? window.scrollY;
  view.value = "chat";
  setDocumentMode(true);
  history.replaceState(history.state, "", `${location.pathname}${location.search}#chat`);
  await nextTick();
  window.scrollTo(0, 0);
}

async function returnToStory() {
  if (view.value === "story") return;
  const chat = document.querySelector<HTMLElement>(".landing-v2-root .xp-root");
  if (chat) {
    chat.style.opacity = "0";
    chat.style.pointerEvents = "none";
  }
  view.value = "story";
  setDocumentMode(false);
  history.replaceState(history.state, "", `${location.pathname}${location.search}`);
  await nextTick();
  /* Closing goes home, not back to where you came in.  */
  storyComponent.value?.restoreAt(0);
}

onMounted(() => {
  if (location.hash === "#chat") enterChat({ source: "skip", returnY: 0 });
});

onBeforeUnmount(() => setDocumentMode(false));
</script>

<template>
  <main v-if="data" :class="['landing-v2-root', view === 'chat' && 'is-chat-mode']">
    <StoryHorizontal
      ref="storyComponent"
      :active="view === 'story'"
      @enter-chat="enterChat"
    />
    <EvidenceChat
      :data="data"
      :active="view === 'chat'"
      @return-story="returnToStory"
    />
  </main>

  <!-- The mark stays in the corner it occupies on every other screen rather than sitting in the middle of this one.  -->
  <main v-else class="load-state">
    <NuxtLink to="/" class="load-logo" aria-label="EuroQol home">
      <img src="/brand/euroqol-logo.svg" alt="EuroQol" width="300" height="49">
    </NuxtLink>
    <p v-if="error" class="load-error">The interface reference data did not load. Restart the application and try again.</p>
    <BrandLoader v-else label="Gathering the research" />
  </main>
</template>
