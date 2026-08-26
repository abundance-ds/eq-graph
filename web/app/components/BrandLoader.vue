<script setup lang="ts">
/**
 * What the page shows while it has nothing to show.
 *
 * The story is made of particles that gather into a shape and come apart
 * again, so waiting for it is drawn the same way: a ring of the same grain, in
 * the same two colours, settling one after another. A borrowed spinner would
 * have been the only thing on the site that came from somewhere else.
 *
 * It is deliberately quiet. This is a wait, not an event.
 */
withDefaults(defineProps<{ label?: string }>(), {
  label: "Gathering the research",
});

// Ten is enough to read as a ring at this size without the dots touching.
const dots = Array.from({ length: 10 }, (_, i) => i);
</script>

<template>
  <div class="bl" role="status" :aria-label="label">
    <div class="bl-ring" aria-hidden="true">
      <i v-for="i in dots" :key="i" :style="{ '--i': i }" />
    </div>
    <p class="bl-label">{{ label }}</p>
  </div>
</template>

<style scoped>
.bl {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.6rem;
}

.bl-ring {
  position: relative;
  width: 58px;
  height: 58px;
}

/* Each dot is placed by rotating it out to the rim, so the ring is one
   transform per dot rather than ten hand-written positions. */
.bl-ring i {
  position: absolute;
  inset: 0;
  margin: auto;
  width: 4.5px;
  height: 4.5px;
  border-radius: 50%;
  background: var(--dot-teal, #007d6c);
  transform: rotate(calc(var(--i) * 36deg)) translateY(-24px);
  animation: bl-settle 1.5s ease-in-out infinite;
  /* Negative delays start the cycle already in progress, so the ring is
     mid-rotation on the first frame instead of switching on all at once. */
  animation-delay: calc(var(--i) * -0.15s);
}

/* Two of them carry the second colour, the way the charts do. */
.bl-ring i:nth-child(4),
.bl-ring i:nth-child(9) { background: var(--dot-yellow, #b88016); }

@keyframes bl-settle {
  0%, 100% { opacity: 0.16; scale: 0.55; }
  38%      { opacity: 1;    scale: 1; }
}

.bl-label {
  margin: 0;
  color: var(--ink-3, #8e8e86);
  font: 500 0.92rem var(--font-body, "Instrument Sans", sans-serif);
  letter-spacing: 0.01em;
}

/* Movement is the whole point of this element, so with motion turned down it
   holds still and states itself rather than disappearing. */
@media (prefers-reduced-motion: reduce) {
  .bl-ring i { animation: none; opacity: 0.55; scale: 1; }
}
</style>
