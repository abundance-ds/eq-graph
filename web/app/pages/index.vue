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
  /* Closing goes home, not back to where you came in.

     It used to restore the scroll position captured on entry, so arriving from
     the end of the story dropped the reader straight back into the last fold —
     and if that landed inside the handover zone, the chat opened again. Close
     is a way out of the explorer, so it goes to the top, which is the one place
     that is the same wherever you entered from. */
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

  <main v-else class="load-state">
    <img src="/brand/euroqol-logo.svg" alt="EuroQol" width="210" height="34">
    <p v-if="error">The interface reference data did not load. Restart the application and try again.</p>
    <p v-else>Preparing EuroQol research…</p>
  </main>
</template>
