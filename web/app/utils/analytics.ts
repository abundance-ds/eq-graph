import type { Router } from "vue-router";

export type AnalyticsScreen =
  | "landing"
  | "story-01"
  | "story-02"
  | "story-03"
  | "story-04"
  | "story-05"
  | "story-end"
  | "chat"
  | "about";

type AnalyticsState = {
  viewId: string;
  path: "/" | "/about";
  screen: AnalyticsScreen;
  maxScroll: number;
  maxStoryStep: number;
  activeSince: number;
  visible: boolean;
  enabled: boolean;
};

let state: AnalyticsState | undefined;
let interval: ReturnType<typeof setInterval> | undefined;
let storyObserver: MutationObserver | undefined;

function deviceClass(): "mobile" | "tablet" | "desktop" {
  if (window.innerWidth < 640) return "mobile";
  if (window.innerWidth < 1024) return "tablet";
  return "desktop";
}

function send(payload: object, beacon = false): void {
  const body = JSON.stringify(payload);
  if (beacon && navigator.sendBeacon) {
    navigator.sendBeacon("/api/analytics", new Blob([body], { type: "application/json" }));
    return;
  }
  void fetch("/api/analytics", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body,
    keepalive: true,
  }).catch(() => undefined);
}

function routeScreen(path: string, hash: string): AnalyticsScreen | null {
  if (path === "/about") return "about";
  if (path === "/") return hash === "#chat" ? "chat" : "landing";
  return null;
}

function begin(path: "/" | "/about", screen: AnalyticsScreen): void {
  state = {
    viewId: crypto.randomUUID(),
    path,
    screen,
    maxScroll: 0,
    maxStoryStep: 0,
    activeSince: performance.now(),
    visible: document.visibilityState === "visible",
    enabled: true,
  };
  send({ type: "view", viewId: state.viewId, path, screen, device: deviceClass() });
}

function activeDelta(): number {
  if (!state?.visible) return 0;
  const current = performance.now();
  const delta = Math.max(0, Math.min(60_000, Math.round(current - state.activeSince)));
  state.activeSince = current;
  return delta;
}

export function flushAnalytics(beacon = false): void {
  if (!state?.enabled) return;
  send({
    type: "engagement",
    viewId: state.viewId,
    screen: state.screen,
    activeMs: activeDelta(),
    maxScroll: state.maxScroll,
    maxStoryStep: state.maxStoryStep,
  }, beacon);
}

export function setAnalyticsScreen(screen: AnalyticsScreen, storyStep = 0): void {
  if (!state?.enabled) return;
  state.maxStoryStep = Math.max(state.maxStoryStep, storyStep);
  if (state.screen === screen) return;
  flushAnalytics();
  state.screen = screen;
  state.activeSince = performance.now();
}

export function analyticsViewId(): string | undefined {
  return state?.enabled ? state.viewId : undefined;
}

export function syncAnalyticsStoryScreen(): void {
  const root = document.querySelector<HTMLElement>(".sh-root");
  const phase = root?.dataset.storyPhase;
  const beat = Math.max(1, Math.min(5, Math.round(Number(root?.dataset.storyBeat ?? 1))));
  if (phase === "intro") setAnalyticsScreen("landing");
  else if (phase === "end") setAnalyticsScreen("story-end", 5);
  else if (phase === "step") {
    setAnalyticsScreen(`story-${String(beat).padStart(2, "0")}` as AnalyticsScreen, beat);
  }
}

function observeStory(): void {
  storyObserver?.disconnect();
  storyObserver = undefined;
  const root = document.querySelector<HTMLElement>(".sh-root");
  if (!root) return;
  storyObserver = new MutationObserver(syncAnalyticsStoryScreen);
  storyObserver.observe(root, {
    attributes: true,
    attributeFilter: ["data-story-phase", "data-story-beat"],
  });
  syncAnalyticsStoryScreen();
}

export function initialiseAnalytics(router: Router): () => void {
  const route = router.currentRoute.value;
  const initial = routeScreen(route.path, route.hash);
  if (initial) begin(route.path as "/" | "/about", initial);

  const removeRouteHook = router.afterEach((to, from) => {
    const next = routeScreen(to.path, to.hash);
    if (!next) {
      flushAnalytics(true);
      state = undefined;
      return;
    }
    if (!state || to.path !== from.path) {
      flushAnalytics(true);
      begin(to.path as "/" | "/about", next);
      requestAnimationFrame(observeStory);
      return;
    }
    setAnalyticsScreen(next);
  });

  const onScroll = () => {
    if (!state) return;
    const available = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    state.maxScroll = Math.max(state.maxScroll, Math.min(100, Math.round(window.scrollY / available * 100)));
  };
  const onVisibility = () => {
    if (!state) return;
    if (document.visibilityState === "hidden") {
      flushAnalytics(true);
      state.visible = false;
    } else {
      state.visible = true;
      state.activeSince = performance.now();
    }
  };
  const onPageHide = () => {
    flushAnalytics(true);
    if (state) state.visible = false;
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  document.addEventListener("visibilitychange", onVisibility);
  window.addEventListener("pagehide", onPageHide);
  observeStory();
  interval = setInterval(() => flushAnalytics(), 15_000);

  return () => {
    flushAnalytics(true);
    removeRouteHook();
    if (interval) clearInterval(interval);
    interval = undefined;
    storyObserver?.disconnect();
    storyObserver = undefined;
    window.removeEventListener("scroll", onScroll);
    document.removeEventListener("visibilitychange", onVisibility);
    window.removeEventListener("pagehide", onPageHide);
  };
}
