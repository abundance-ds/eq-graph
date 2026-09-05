/*
  The WebGL stage behind /graph.

  A print-like drawing on the site's paper: ink hairlines for links, small
  colour-coded discs for nodes, atmospheric fading toward the paper for depth.
  Nodes morph between precomputed lens layouts from public/graph-scene.json.
  Interaction is a thin layer on top: screen-space picking, a focus target for
  the orbit camera, and an HTML label layer that follows the projected nodes.
*/
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { TrackballControls } from "three/addons/controls/TrackballControls.js";
import { LineSegments2 } from "three/addons/lines/LineSegments2.js";
import { LineSegmentsGeometry } from "three/addons/lines/LineSegmentsGeometry.js";
import { LineMaterial } from "three/addons/lines/LineMaterial.js";

export const KIND = { person: 0, project: 1, paper: 2, product: 3, instrument: 4 };

/* The story's chart series, pulled a step toward ink so they sit quietly on
   paper. Kind colours come first; communities and groups reuse the same set. */
export const HUES = ["#0f7a6b", "#2f6db5", "#a8720d", "#b5567f", "#5c4fb3", "#3d8f5f", "#c9633a", "#5f6b78"];
export const KIND_HUE = ["#0f7a6b", "#a8720d", "#2f6db5", "#b5567f", "#1a1a17"];
const NEUTRAL = "#9a9a92";
const HUB = "#1a1a17";
const PAPER = "#fcfcfb";
const INK = "#1a1a17";
const PENCIL = "#6b6b64";
const ACCENT = "#007d6c";

const CAMERA_DISTANCE = 430;
const TRANSITION_MS = 1500;
const FOCUS_MS = 950;
const DRIFT = 0.04;          // idle turn, radians per second
const IDLE_MS = 4500;

const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
const clamp01 = (v) => Math.min(1, Math.max(0, v));
const hex = (h) => new THREE.Color(h);

function instrumentFamily(name) {
  if (/^EQ-5D-Y/.test(name)) return 2;
  if (/^EQ-HWB/.test(name)) return 3;
  if (/^EQ VAS/.test(name)) return 4;
  if (/^EQ-5D-5L/.test(name)) return 0;
  if (/^EQ-5D-3L/.test(name) || /^EQ-5D$/.test(name)) return 1;
  return 7;
}

/* Colour of one node under one lens. */
export function nodeColour(node, lens, scene) {
  if (lens === "people") return node.k === KIND.person ? (node.c != null && node.c < 8 ? HUES[node.c] : NEUTRAL) : KIND_HUE[node.k];
  if (lens === "funding") {
    if (node.k === KIND.paper || node.k === KIND.project || node.k === KIND.person) {
      const g = node.g?.[0];
      return g == null ? NEUTRAL : HUES[g % HUES.length];
    }
    return KIND_HUE[node.k];
  }
  if (lens === "time") {
    if (node.k === KIND.instrument) return HUB;
    if (node.k === KIND.paper) {
      const first = node.i?.[0];
      return first == null ? NEUTRAL : HUES[instrumentFamily(scene.instruments[first])];
    }
    return KIND_HUE[node.k];
  }
  return KIND_HUE[node.k];
}

export function paletteFor(lens, scene) {
  if (lens === "people") return [...HUES.map((h, i) => ({ colour: h, label: scene.communities?.[i] || `Community ${i + 1}` })), { colour: NEUTRAL, label: "Smaller groups" }];
  if (lens === "funding") return scene.groups.map((g, i) => ({ colour: HUES[i % HUES.length], label: g }));
  if (lens === "time") return [
    { colour: HUES[0], label: "EQ-5D-5L" }, { colour: HUES[1], label: "EQ-5D-3L" }, { colour: HUES[2], label: "EQ-5D-Y" },
    { colour: HUES[3], label: "EQ-HWB" }, { colour: HUES[4], label: "EQ VAS" }, { colour: HUES[7], label: "Other instrument" },
    { colour: HUB, label: "Instrument" },
  ];
  return scene.kinds.map((k, i) => ({ colour: KIND_HUE[i], label: k === "person" ? "People" : `${k[0].toUpperCase()}${k.slice(1)}s` }));
}

/* Multiply blending with coverage: out = dst * (1 - a + a * colour).  Ink over
   ink darkens, order does not matter, and nothing can blow out on paper.
   Shaders output premultiplied colour for this to hold. */
const MULTIPLY_BLEND = {
  blending: THREE.CustomBlending,
  blendEquation: THREE.AddEquation,
  blendSrc: THREE.DstColorFactor,
  blendDst: THREE.OneMinusSrcAlphaFactor,
  blendSrcAlpha: THREE.ZeroFactor,
  blendDstAlpha: THREE.OneFactor,
};

const POINT_VERTEX = /* glsl */ `
  attribute float size;
  attribute float state;
  attribute float presence;
  attribute vec3 color;
  uniform float uPixelRatio;
  uniform float uScale;
  uniform float uNear;
  uniform float uFar;
  varying vec3 vColor;
  varying float vAlpha;
  varying float vState;
  varying float vFog;
  void main() {
    vec4 mv = modelViewMatrix * vec4(position, 1.0);
    float depth = max(-mv.z, 1.0);
    float lit = step(1.5, state);
    vFog = smoothstep(uNear, uFar, depth) * 0.82;
    /* Nodes that drift past the camera thin out instead of filling the screen. */
    float near = smoothstep(uNear * 0.22, uNear * 0.62, depth);
    float px = (1.9 + size * 8.5) * (1.0 + 0.4 * lit) * uScale * (430.0 / depth) * uPixelRatio;
    gl_PointSize = clamp(px, 1.3 * uPixelRatio, 28.0 * uPixelRatio);
    gl_Position = projectionMatrix * mv;
    vColor = color;
    vState = state;
    vAlpha = presence * near;
  }
`;

const POINT_FRAGMENT = /* glsl */ `
  uniform vec3 uPaper;
  uniform vec3 uInk;
  varying vec3 vColor;
  varying float vAlpha;
  varying float vState;
  varying float vFog;
  void main() {
    vec2 c = gl_PointCoord - 0.5;
    float d = length(c) * 2.0;
    if (d > 1.0) discard;
    float muted = step(0.5, vState) * step(vState, 1.5);
    float lit = step(1.5, vState);
    /* A colour disc with a paper knockout rim, so markers sit above the lines.
       A selected node gets an ink rim instead. */
    float disc = 1.0 - smoothstep(0.66, 0.80, d);
    float edge = 1.0 - smoothstep(0.88, 1.0, d);
    vec3 col = mix(vColor, uPaper, vFog);
    col = mix(col, vec3(0.86, 0.86, 0.84), muted * 0.9);
    vec3 rim = mix(uPaper, uInk, lit);
    vec3 rgb = mix(rim, col, disc);
    float a = edge * vAlpha * mix(1.0, 0.55, muted);
    gl_FragColor = vec4(rgb * a, a);
  }
`;

const LINE_VERTEX = /* glsl */ `
  attribute float estate;
  attribute float eweight;
  attribute float epresence;
  uniform float uNear;
  uniform float uFar;
  uniform float uFade;
  varying float vAlpha;
  varying float vFog;
  void main() {
    vec4 mv = modelViewMatrix * vec4(position, 1.0);
    float depth = max(-mv.z, 1.0);
    vFog = smoothstep(uNear, uFar, depth) * 0.85;
    float near = smoothstep(uNear * 0.22, uNear * 0.62, depth);
    float muted = step(0.5, estate) * step(estate, 1.5);
    float base = 0.035 + 0.17 * eweight;
    float a = mix(base, 0.012, muted);
    vAlpha = clamp(a * near * uFade * epresence, 0.0, 1.0);
    gl_Position = projectionMatrix * mv;
  }
`;

const LINE_FRAGMENT = /* glsl */ `
  uniform vec3 uPaper;
  uniform vec3 uPencil;
  varying float vAlpha;
  varying float vFog;
  void main() {
    vec3 col = mix(uPencil, uPaper, vFog);
    gl_FragColor = vec4(col * vAlpha, vAlpha);
  }
`;

/**
 * @param {HTMLElement} container
 * @param {object} scene  parsed graph-scene.json
 * @param {object} options
 *   quality: "full" | "lite"
 *   onHover(index|null), onSelect(index|null), onLens(key), onSettle()
 */
export function createGraphScene(container, scene, options = {}) {
  const N = scene.nodes.length;
  const lite = options.quality === "lite";
  const reducedMotion = typeof matchMedia === "function" && matchMedia("(prefers-reduced-motion: reduce)").matches;
  const lensByKey = new Map(scene.lenses.map((l) => [l.key, l]));

  /* ── renderer ─────────────────────────────────────────────────── */
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "high-performance" });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, lite ? 1.5 : 2));
  renderer.setClearColor(new THREE.Color(PAPER), 1);
  renderer.domElement.className = "gx-canvas";
  container.appendChild(renderer.domElement);

  const labelLayer = document.createElement("div");
  labelLayer.className = "gx-labels";
  container.appendChild(labelLayer);

  const three = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(42, 1, 1, 4000);
  camera.position.set(0, 40, CAMERA_DISTANCE);

  /* Two cameras' worth of manners on one camera. The free lenses tumble
     without a pole, keep momentum after a flick, and turn slowly when left
     alone; the instrument lens has a year axis to read, so it stays upright
     and only swings inside a window. */
  const orbit = new OrbitControls(camera, renderer.domElement);
  orbit.enableDamping = true;
  orbit.dampingFactor = 0.055;
  orbit.rotateSpeed = 0.55;
  orbit.zoomSpeed = 0.7;
  orbit.panSpeed = 0.6;
  orbit.minDistance = 40;
  orbit.maxDistance = 1100;
  orbit.autoRotate = !reducedMotion;
  orbit.autoRotateSpeed = 0.22;
  orbit.enabled = false;
  const tumble = new TrackballControls(camera, renderer.domElement);
  tumble.rotateSpeed = 1.5;
  tumble.zoomSpeed = 0.13;
  tumble.panSpeed = 0.09;
  tumble.dynamicDampingFactor = 0.08;
  tumble.minDistance = 40;
  tumble.maxDistance = 1100;
  tumble.target = orbit.target;
  let controls = tumble;
  let orbitLimitsPending = false;
  function useControls(next) {
    if (controls === next) return;
    controls.enabled = false;
    next.enabled = true;
    controls = next;
  }
  function setOrbitLimits(on) {
    orbit.minAzimuthAngle = on ? -1.05 : -Infinity;
    orbit.maxAzimuthAngle = on ? 1.05 : Infinity;
    orbit.minPolarAngle = on ? 0.7 : 0;
    orbit.maxPolarAngle = on ? 2.3 : Math.PI;
  }

  /* ── buffers ──────────────────────────────────────────────────── */
  const cur = new Float32Array(N * 3);
  const from = new Float32Array(N * 3);
  const to = new Float32Array(N * 3);
  const presenceCur = new Float32Array(N);
  const presenceFrom = new Float32Array(N);
  const presenceTo = new Float32Array(N);
  const colourCur = new Float32Array(N * 3);
  const colourFrom = new Float32Array(N * 3);
  const colourTo = new Float32Array(N * 3);
  const sizes = new Float32Array(N);
  const state = new Float32Array(N);
  const stagger = new Float32Array(N);
  const order = new Uint32Array(N);
  const depthOf = new Float32Array(N);
  for (let i = 0; i < N; i++) {
    sizes[i] = scene.nodes[i].s;
    stagger[i] = ((i * 2654435761) >>> 0) / 4294967296 * 0.18;
    order[i] = i;
  }

  const pointGeometry = new THREE.BufferGeometry();
  pointGeometry.setAttribute("position", new THREE.BufferAttribute(cur, 3));
  pointGeometry.setAttribute("color", new THREE.BufferAttribute(colourCur, 3));
  pointGeometry.setAttribute("size", new THREE.BufferAttribute(sizes, 1));
  pointGeometry.setAttribute("state", new THREE.BufferAttribute(state, 1));
  pointGeometry.setAttribute("presence", new THREE.BufferAttribute(presenceCur, 1));
  pointGeometry.setIndex(new THREE.BufferAttribute(order, 1));
  pointGeometry.boundingSphere = new THREE.Sphere(new THREE.Vector3(), 1200);
  const pointUniforms = {
    uPixelRatio: { value: renderer.getPixelRatio() },
    uScale: { value: 1 },
    uNear: { value: CAMERA_DISTANCE * 0.55 },
    uFar: { value: CAMERA_DISTANCE * 1.9 },
    uPaper: { value: hex(PAPER) },
    uInk: { value: hex(INK) },
  };
  const pointMaterial = new THREE.ShaderMaterial({
    uniforms: pointUniforms, vertexShader: POINT_VERTEX, fragmentShader: POINT_FRAGMENT,
    transparent: true, depthWrite: false, depthTest: true,
    blending: THREE.NormalBlending, premultipliedAlpha: true,
  });
  const points = new THREE.Points(pointGeometry, pointMaterial);
  points.frustumCulled = false;
  points.renderOrder = 2;
  three.add(points);

  const lineUniforms = {
    uNear: pointUniforms.uNear, uFar: pointUniforms.uFar, uFade: { value: 1 },
    uPaper: pointUniforms.uPaper, uPencil: { value: hex(PENCIL) },
  };
  const lineMaterial = new THREE.ShaderMaterial({
    uniforms: lineUniforms, vertexShader: LINE_VERTEX, fragmentShader: LINE_FRAGMENT,
    transparent: true, depthWrite: false, depthTest: true, ...MULTIPLY_BLEND,
  });
  let lines = null;
  let edgeList = [];        // [[a, b, w]] for the active lens
  let edgeState = null;     // Float32Array(E * 2)
  let edgePresence = null;  // Float32Array(E * 2)
  let linePositions = null; // Float32Array(E * 6)
  const adjacency = new Map(); // node index -> Set(neighbour index) for the active lens

  /* Highlighted links are redrawn as real-width strokes in the accent colour. */
  const litMaterial = new LineMaterial({
    color: new THREE.Color(ACCENT), linewidth: 1.5, transparent: true, opacity: 0.9,
    depthTest: true, depthWrite: false, worldUnits: false,
  });
  let litLines = null;
  let litEdges = [];

  /* Hub edges (every paper to EQ-5D-5L) converge on one spot; draw them faint so
     the core stays readable. */
  const EDGE_WEIGHT = { instrument: 0.2, authorship: 0.5, product: 0.4, pi: 0.8, link: 1, coauthor: 1 };

  function buildEdges(lens) {
    if (lines) { three.remove(lines); lines.geometry.dispose(); }
    const minWeight = lite && lens.key === "people" ? 2 : 1;
    edgeList = [];
    const edgeSet = [];
    for (const set of lens.edges) {
      for (const e of scene.edges[set]) {
        if ((e[2] || 1) < minWeight) continue;
        edgeList.push(e);
        edgeSet.push(set);
      }
    }
    const E = edgeList.length;
    linePositions = new Float32Array(E * 6);
    edgeState = new Float32Array(E * 2);
    edgePresence = new Float32Array(E * 2);
    const weights = new Float32Array(E * 2);
    let maxW = 1;
    for (const e of edgeList) if ((e[2] || 1) > maxW) maxW = e[2];
    adjacency.clear();
    for (let i = 0; i < E; i++) {
      const [a, b, w] = edgeList[i];
      const wn = Math.sqrt((w || 1) / maxW) * (EDGE_WEIGHT[edgeSet[i]] ?? 1);
      weights[i * 2] = wn; weights[i * 2 + 1] = wn;
      if (!adjacency.has(a)) adjacency.set(a, new Set());
      if (!adjacency.has(b)) adjacency.set(b, new Set());
      adjacency.get(a).add(b);
      adjacency.get(b).add(a);
    }
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute("position", new THREE.BufferAttribute(linePositions, 3));
    geometry.setAttribute("estate", new THREE.BufferAttribute(edgeState, 1));
    geometry.setAttribute("eweight", new THREE.BufferAttribute(weights, 1));
    geometry.setAttribute("epresence", new THREE.BufferAttribute(edgePresence, 1));
    geometry.boundingSphere = new THREE.Sphere(new THREE.Vector3(), 1200);
    lines = new THREE.LineSegments(geometry, lineMaterial);
    lines.frustumCulled = false;
    lines.renderOrder = 1;
    three.add(lines);
    syncLines();
    applyState();
    buildAxis(lens);
  }

  function syncLines() {
    if (!lines) return;
    const E = edgeList.length;
    for (let i = 0; i < E; i++) {
      const [a, b] = edgeList[i];
      const o = i * 6;
      linePositions[o] = cur[a * 3]; linePositions[o + 1] = cur[a * 3 + 1]; linePositions[o + 2] = cur[a * 3 + 2];
      linePositions[o + 3] = cur[b * 3]; linePositions[o + 4] = cur[b * 3 + 1]; linePositions[o + 5] = cur[b * 3 + 2];
      const p = Math.min(presenceCur[a], presenceCur[b]);
      edgePresence[i * 2] = p; edgePresence[i * 2 + 1] = p;
    }
    lines.geometry.attributes.position.needsUpdate = true;
    lines.geometry.attributes.epresence.needsUpdate = true;
    syncLitLines();
  }

  function rebuildLitLines() {
    if (litLines) { three.remove(litLines); litLines.geometry.dispose(); litLines = null; }
    litEdges = [];
    const focus = selected ?? hovered;
    if (focus == null) return;
    for (const e of edgeList) if (e[0] === focus || e[1] === focus) litEdges.push(e);
    if (!litEdges.length) return;
    const geometry = new LineSegmentsGeometry();
    geometry.setPositions(litPositions());
    litLines = new LineSegments2(geometry, litMaterial);
    litLines.frustumCulled = false;
    litLines.renderOrder = 3;
    three.add(litLines);
  }

  function litPositions() {
    const out = new Float32Array(litEdges.length * 6);
    for (let i = 0; i < litEdges.length; i++) {
      const [a, b] = litEdges[i];
      const o = i * 6;
      out[o] = cur[a * 3]; out[o + 1] = cur[a * 3 + 1]; out[o + 2] = cur[a * 3 + 2];
      out[o + 3] = cur[b * 3]; out[o + 4] = cur[b * 3 + 1]; out[o + 5] = cur[b * 3 + 2];
    }
    return out;
  }

  function syncLitLines() {
    if (!litLines) return;
    litLines.geometry.setPositions(litPositions());
  }

  /* ── interaction state ────────────────────────────────────────── */
  let activeLens = null;
  let selected = null;
  let hovered = null;
  let filter = null; // (node, index) => boolean
  let transition = null; // { start, swapDone }
  let focusMove = null;  // { start, fromTarget, toTarget, fromPos, toPos }
  let lastInteraction = performance.now();
  let destroyed = false;
  let firstFrame = true;

  const passes = (i) => !filter || filter(scene.nodes[i], i);

  function applyState() {
    const neighbours = selected != null ? adjacency.get(selected) : null;
    const hoverNeighbours = hovered != null ? adjacency.get(hovered) : null;
    for (let i = 0; i < N; i++) {
      let s = 0;
      if (selected != null) {
        s = i === selected || (neighbours && neighbours.has(i)) ? 2 : 1;
      } else if (filter) {
        s = passes(i) ? 0 : 1;
      }
      if (hovered != null && (i === hovered || (hoverNeighbours && hoverNeighbours.has(i)))) s = 2;
      state[i] = s;
    }
    pointGeometry.attributes.state.needsUpdate = true;
    if (lines) {
      for (let i = 0; i < edgeList.length; i++) {
        const [a, b] = edgeList[i];
        let s = 0;
        if (selected != null) s = a === selected || b === selected ? 2 : 1;
        else if (filter) s = passes(a) && passes(b) ? 0 : 1;
        if (hovered != null && (a === hovered || b === hovered)) s = 2;
        edgeState[i * 2] = s; edgeState[i * 2 + 1] = s;
      }
      lines.geometry.attributes.estate.needsUpdate = true;
    }
    rebuildLitLines();
  }

  /* ── lenses ───────────────────────────────────────────────────── */
  function setLens(key, { instant = false } = {}) {
    const lens = lensByKey.get(key);
    if (!lens || lens === activeLens) return;
    const previous = activeLens;
    activeLens = lens;
    const presentSet = new Set(lens.present);
    from.set(cur);
    presenceFrom.set(presenceCur);
    colourFrom.set(colourCur);
    for (let i = 0; i < N; i++) {
      to[i * 3] = lens.pos[i * 3]; to[i * 3 + 1] = lens.pos[i * 3 + 1]; to[i * 3 + 2] = lens.pos[i * 3 + 2];
      presenceTo[i] = presentSet.has(i) ? 1 : 0;
      const c = hex(nodeColour(scene.nodes[i], key, scene));
      colourTo[i * 3] = c.r; colourTo[i * 3 + 1] = c.g; colourTo[i * 3 + 2] = c.b;
    }
    pointUniforms.uScale.value = key === "people" ? 0.92 : key === "time" ? 1.08 : 1;
    if (!previous) {
      /* First reveal: drift in from an expanded shell. */
      for (let i = 0; i < N * 3; i++) from[i] = to[i] * 1.6;
      presenceFrom.fill(0);
      colourFrom.set(colourTo);
    }
    if (selected != null && !presentSet.has(selected)) select(null);
    if (instant || reducedMotion) {
      cur.set(to); presenceCur.set(presenceTo); colourCur.set(colourTo);
      buildEdges(lens);
      pointGeometry.attributes.position.needsUpdate = true;
      pointGeometry.attributes.presence.needsUpdate = true;
      pointGeometry.attributes.color.needsUpdate = true;
      transition = null;
      lineUniforms.uFade.value = 1;
    } else {
      transition = { start: performance.now(), swapDone: !previous };
      if (!previous) buildEdges(lens);
    }
    if (key === "time") {
      /* The limits wait for the camera to arrive, or the orbit would snap it into the window mid-flight. */
      setOrbitLimits(false);
      orbitLimitsPending = true;
      useControls(orbit);
      const xs = (lens.axis?.ticks || []).map((t) => t.x);
      const lo = xs.length ? Math.min(...xs) : -150;
      const hi = xs.length ? Math.max(...xs) : 150;
      /* Aim past the midpoint: most papers sit in the last decade. */
      homeTarget = new THREE.Vector3(lo + (hi - lo) * 0.6, 0, 0);
      homeDistance = fitWidth((hi - lo) / 2);
      aimCamera(0.05, 0.22);
    } else {
      orbitLimitsPending = false;
      homeTarget = new THREE.Vector3();
      homeDistance = CAMERA_DISTANCE;
      useControls(tumble);
    }
    options.onLens?.(key);
  }

  function stepTransition(now) {
    if (!transition) return;
    const t = clamp01((now - transition.start) / TRANSITION_MS);
    if (!transition.swapDone) {
      lineUniforms.uFade.value = 1 - clamp01(t / 0.22);
      if (t >= 0.22) { buildEdges(activeLens); transition.swapDone = true; }
    } else {
      lineUniforms.uFade.value = clamp01((t - 0.36) / 0.64);
    }
    for (let i = 0; i < N; i++) {
      const e = ease(clamp01((t - stagger[i]) / (1 - 0.18)));
      const o = i * 3;
      cur[o] = from[o] + (to[o] - from[o]) * e;
      cur[o + 1] = from[o + 1] + (to[o + 1] - from[o + 1]) * e;
      cur[o + 2] = from[o + 2] + (to[o + 2] - from[o + 2]) * e;
      presenceCur[i] = presenceFrom[i] + (presenceTo[i] - presenceFrom[i]) * e;
      colourCur[o] = colourFrom[o] + (colourTo[o] - colourFrom[o]) * e;
      colourCur[o + 1] = colourFrom[o + 1] + (colourTo[o + 1] - colourFrom[o + 1]) * e;
      colourCur[o + 2] = colourFrom[o + 2] + (colourTo[o + 2] - colourFrom[o + 2]) * e;
    }
    pointGeometry.attributes.position.needsUpdate = true;
    pointGeometry.attributes.presence.needsUpdate = true;
    pointGeometry.attributes.color.needsUpdate = true;
    syncLines();
    if (t >= 1) { transition = null; lineUniforms.uFade.value = 1; options.onSettle?.(); }
  }

  /* Painter's order: far nodes first, so near markers knock out what is behind. */
  const lastCamera = new THREE.Matrix4();
  function sortNodes(force) {
    camera.updateMatrixWorld();
    if (!force && lastCamera.equals(camera.matrixWorld)) return;
    lastCamera.copy(camera.matrixWorld);
    const e = camera.matrixWorldInverse.elements;
    for (let i = 0; i < N; i++) {
      const o = i * 3;
      depthOf[i] = e[2] * cur[o] + e[6] * cur[o + 1] + e[10] * cur[o + 2] + e[14];
    }
    const idx = Array.from(order);
    idx.sort((a, b) => depthOf[a] - depthOf[b]);
    order.set(idx);
    pointGeometry.index.needsUpdate = true;
  }

  /* ── camera ───────────────────────────────────────────────────── */
  const tmpTarget = new THREE.Vector3();
  const tmpPos = new THREE.Vector3();

  const UP = new THREE.Vector3(0, 1, 0);
  /* Where "Reset view" goes: the origin, or the middle of the year axis. */
  let homeTarget = new THREE.Vector3();
  let homeDistance = CAMERA_DISTANCE;

  function moveCamera(toTarget, toPos, toUp) {
    focusMove = {
      start: performance.now(),
      fromTarget: controls.target.clone(), toTarget,
      fromPos: camera.position.clone(), toPos,
      fromUp: camera.up.clone(), toUp: toUp || camera.up.clone(),
    };
  }

  function aimCamera(azimuth, elevation) {
    const dir = new THREE.Vector3(
      Math.sin(azimuth) * Math.cos(elevation), Math.sin(elevation), Math.cos(azimuth) * Math.cos(elevation),
    );
    moveCamera(homeTarget.clone(), homeTarget.clone().add(dir.multiplyScalar(homeDistance)), UP.clone());
  }

  /* The distance at which a horizontal span fills most of the viewport. */
  function fitWidth(halfSpan) {
    const halfView = Math.tan((camera.fov * Math.PI) / 360) * camera.aspect;
    return Math.min(700, Math.max(200, (halfSpan * 1.4) / halfView));
  }

  function focusOn(index) {
    const target = new THREE.Vector3(cur[index * 3], cur[index * 3 + 1], cur[index * 3 + 2]);
    const offset = camera.position.clone().sub(controls.target);
    const distance = Math.min(Math.max(offset.length(), 120), 210);
    offset.setLength(distance);
    moveCamera(target, target.clone().add(offset));
  }

  function stepFocus(now) {
    if (!focusMove) return;
    const t = ease(clamp01((now - focusMove.start) / (reducedMotion ? 1 : FOCUS_MS)));
    tmpTarget.lerpVectors(focusMove.fromTarget, focusMove.toTarget, t);
    tmpPos.lerpVectors(focusMove.fromPos, focusMove.toPos, t);
    controls.target.copy(tmpTarget);
    camera.position.copy(tmpPos);
    camera.up.lerpVectors(focusMove.fromUp, focusMove.toUp, t).normalize();
    if (t >= 1) {
      focusMove = null;
      if (orbitLimitsPending) { orbitLimitsPending = false; setOrbitLimits(true); }
    }
  }

  /* ── picking ──────────────────────────────────────────────────── */
  const pointer = { x: -1, y: -1, dirty: false, inside: false };
  const projected = new THREE.Vector3();
  let width = 1;
  let height = 1;

  function screenSize(index, depth) {
    return (1.9 + sizes[index] * 8.5) * pointUniforms.uScale.value * (430 / Math.max(depth, 1));
  }

  function pick(px, py) {
    let best = null;
    let bestScore = Infinity;
    camera.updateMatrixWorld();
    for (let i = 0; i < N; i++) {
      if (presenceCur[i] < 0.5) continue;
      projected.set(cur[i * 3], cur[i * 3 + 1], cur[i * 3 + 2]).project(camera);
      if (projected.z > 1 || projected.z < -1) continue;
      const sx = (projected.x + 1) * 0.5 * width;
      const sy = (1 - projected.y) * 0.5 * height;
      const dx = sx - px;
      const dy = sy - py;
      const d2 = dx * dx + dy * dy;
      const depth = camera.position.distanceTo(tmpPos.set(cur[i * 3], cur[i * 3 + 1], cur[i * 3 + 2]));
      const radius = Math.max(7, screenSize(i, depth) * 0.5 + 4);
      if (d2 > radius * radius) continue;
      const score = d2 / (radius * radius);
      if (score < bestScore) { bestScore = score; best = i; }
    }
    return best;
  }

  function setHovered(index) {
    if (index === hovered) return;
    hovered = index;
    renderer.domElement.style.cursor = index != null ? "pointer" : "";
    applyState();
    options.onHover?.(index);
  }

  function select(index, { silent = false, move = true } = {}) {
    if (index === selected) return;
    selected = index;
    applyState();
    if (index != null && move) focusOn(index);
    if (!silent) options.onSelect?.(index);
  }

  /* ── labels ───────────────────────────────────────────────────── */
  const labelPool = [];
  const labelSlots = new Map(); // node index -> element
  function labelElement() {
    const el = labelPool.pop() || document.createElement("span");
    el.className = "gx-label";
    labelLayer.appendChild(el);
    return el;
  }

  /* Axis marks (the time lens's years) live in world space like any node. */
  let axisMarks = [];
  function buildAxis(lens) {
    for (const mark of axisMarks) mark.el.remove();
    axisMarks = (lens.axis?.ticks || []).map((tick) => {
      const el = document.createElement("span");
      el.className = "gx-label is-axis";
      el.textContent = tick.label;
      labelLayer.appendChild(el);
      return { el, x: tick.x, y: lens.axis.y, z: 0 };
    });
  }
  function stepAxis() {
    for (const mark of axisMarks) {
      projected.set(mark.x, mark.y, mark.z).project(camera);
      const visible = projected.z <= 1;
      mark.el.style.opacity = visible ? "1" : "0";
      if (!visible) continue;
      const sx = (projected.x + 1) * 0.5 * width;
      const sy = (1 - projected.y) * 0.5 * height;
      mark.el.style.transform = `translate(${(sx - 14).toFixed(1)}px, ${sy.toFixed(1)}px)`;
    }
  }

  let persistentLabels = [];
  function refreshPersistentLabels() {
    if (!activeLens) return;
    const budget = lite ? 9 : 18;
    persistentLabels = [...activeLens.present]
      .filter((i) => scene.nodes[i].k !== KIND.product)
      .sort((a, b) => sizes[b] - sizes[a])
      .slice(0, budget);
  }

  const smooth = (a, b, x) => { const t = clamp01((x - a) / (b - a)); return t * t * (3 - 2 * t); };
  const labelBoxes = [];
  function stepLabels() {
    const wanted = new Map(); // index -> priority
    for (const i of persistentLabels) wanted.set(i, 1 + sizes[i]);
    if (selected != null) {
      wanted.set(selected, 10);
      const n = adjacency.get(selected);
      if (n) [...n].sort((a, b) => sizes[b] - sizes[a]).slice(0, 12).forEach((i) => wanted.set(i, 4 + sizes[i]));
    }
    if (hovered != null) wanted.set(hovered, 9);
    const ranked = [...wanted].sort((a, b) => b[1] - a[1]);
    labelBoxes.length = 0;
    const keep = new Set();
    camera.updateMatrixWorld();
    for (const [i, priority] of ranked) {
      if (presenceCur[i] < 0.6) continue;
      if (filter && !passes(i) && i !== selected && i !== hovered) continue;
      if (selected != null && state[i] < 1.5) continue;
      projected.set(cur[i * 3], cur[i * 3 + 1], cur[i * 3 + 2]).project(camera);
      if (projected.z > 1) continue;
      const sx = (projected.x + 1) * 0.5 * width;
      const sy = (1 - projected.y) * 0.5 * height;
      if (sx < -40 || sx > width + 40 || sy < 0 || sy > height) continue;
      const depth = camera.position.distanceTo(tmpPos.set(cur[i * 3], cur[i * 3 + 1], cur[i * 3 + 2]));
      const r = screenSize(i, depth) * 0.5;
      const text = scene.nodes[i].l;
      const w = Math.min(text.length, 44) * 6.4 + 8;
      const box = { x: sx + r + 6, y: sy - 8, w, h: 16 };
      let overlap = false;
      for (const other of labelBoxes) {
        if (box.x < other.x + other.w && box.x + box.w > other.x && box.y < other.y + other.h && box.y + box.h > other.y) { overlap = true; break; }
      }
      if (overlap && priority < 9) continue;
      labelBoxes.push(box);
      keep.add(i);
      let el = labelSlots.get(i);
      if (!el) {
        el = labelElement();
        el.textContent = text.length > 44 ? `${text.slice(0, 43)}…` : text;
        labelSlots.set(i, el);
      }
      const near = 1 - smooth(pointUniforms.uNear.value, pointUniforms.uFar.value, depth);
      const emphasis = state[i] > 1.5 ? 1 : 0.45 + 0.55 * near;
      el.style.transform = `translate(${(sx + r + 6).toFixed(1)}px, ${(sy - 8).toFixed(1)}px)`;
      el.style.opacity = (0.35 + 0.65 * emphasis).toFixed(2);
      el.classList.toggle("is-lit", state[i] > 1.5);
      el.classList.toggle("is-hub", scene.nodes[i].k === KIND.instrument);
    }
    for (const [i, el] of labelSlots) {
      if (keep.has(i)) continue;
      el.remove();
      labelPool.push(el);
      labelSlots.delete(i);
    }
  }

  /* ── events ───────────────────────────────────────────────────── */
  const canvas = renderer.domElement;
  let downAt = null;
  function onPointerMove(ev) {
    const rect = canvas.getBoundingClientRect();
    pointer.x = ev.clientX - rect.left;
    pointer.y = ev.clientY - rect.top;
    pointer.dirty = true;
    pointer.inside = true;
    lastInteraction = performance.now();
  }
  function onPointerLeave() { pointer.inside = false; setHovered(null); }
  function onPointerDown(ev) { downAt = { x: ev.clientX, y: ev.clientY, t: performance.now() }; lastInteraction = performance.now(); }
  function onPointerUp(ev) {
    lastInteraction = performance.now();
    if (!downAt) return;
    const moved = Math.hypot(ev.clientX - downAt.x, ev.clientY - downAt.y);
    const quick = performance.now() - downAt.t < 450;
    downAt = null;
    if (moved > 5 || !quick) return;
    const rect = canvas.getBoundingClientRect();
    select(pick(ev.clientX - rect.left, ev.clientY - rect.top));
  }
  function onWheel() { lastInteraction = performance.now(); }
  canvas.addEventListener("pointermove", onPointerMove);
  canvas.addEventListener("pointerleave", onPointerLeave);
  canvas.addEventListener("pointerdown", onPointerDown);
  canvas.addEventListener("pointerup", onPointerUp);
  canvas.addEventListener("wheel", onWheel, { passive: true });

  function resize() {
    width = container.clientWidth || 1;
    height = container.clientHeight || 1;
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    pointUniforms.uPixelRatio.value = renderer.getPixelRatio();
    litMaterial.resolution.set(width * renderer.getPixelRatio(), height * renderer.getPixelRatio());
    tumble.handleResize();
  }
  const observer = new ResizeObserver(resize);
  observer.observe(container);
  resize();

  /* ── frame loop ───────────────────────────────────────────────── */
  let raf = 0;
  let lastLabelStep = 0;
  let lastFrame = 0;
  function frame(now) {
    if (destroyed) return;
    raf = requestAnimationFrame(frame);
    const dt = Math.min(0.05, (now - lastFrame) / 1000);
    lastFrame = now;
    stepTransition(now);
    stepFocus(now);
    const drifting = !reducedMotion && !focusMove && now - lastInteraction > IDLE_MS;
    if (controls === orbit) {
      orbit.autoRotate = drifting;
      /* Inside the azimuth window the idle drift swings back and forth. */
      const azimuth = orbit.getAzimuthalAngle();
      if (azimuth > 0.6) orbit.autoRotateSpeed = -Math.abs(orbit.autoRotateSpeed);
      else if (azimuth < -0.6) orbit.autoRotateSpeed = Math.abs(orbit.autoRotateSpeed);
    } else if (drifting) {
      /* A slow turn about whatever is currently up, so a tumbled view keeps its tilt. */
      tmpPos.copy(camera.position).sub(controls.target).applyAxisAngle(camera.up, DRIFT * dt).add(controls.target);
      camera.position.copy(tmpPos);
    }
    controls.update();
    const distance = camera.position.distanceTo(controls.target);
    pointUniforms.uNear.value = distance * 0.5;
    pointUniforms.uFar.value = distance * 2.1;
    sortNodes(Boolean(transition));
    if (pointer.dirty && pointer.inside && !transition) {
      pointer.dirty = false;
      setHovered(pick(pointer.x, pointer.y));
    }
    if (now - lastLabelStep > 33 || transition || focusMove) { stepLabels(); stepAxis(); lastLabelStep = now; }
    renderer.render(three, camera);
    if (firstFrame) { firstFrame = false; container.classList.add("is-ready"); }
  }
  raf = requestAnimationFrame(frame);

  return {
    setLens(key, opts) { setLens(key, opts); refreshPersistentLabels(); },
    select(index, opts) { select(index, opts); },
    setFilter(fn) { filter = fn; applyState(); },
    hover(index) { setHovered(index); },
    lens: () => activeLens?.key ?? null,
    selected: () => selected,
    neighbours: (index) => [...(adjacency.get(index) || [])],
    edgeCount: () => edgeList.length,
    resetView() {
      select(null);
      const offset = camera.position.clone().sub(controls.target).setLength(homeDistance);
      moveCamera(homeTarget.clone(), homeTarget.clone().add(offset), UP.clone());
    },
    destroy() {
      destroyed = true;
      cancelAnimationFrame(raf);
      observer.disconnect();
      canvas.removeEventListener("pointermove", onPointerMove);
      canvas.removeEventListener("pointerleave", onPointerLeave);
      canvas.removeEventListener("pointerdown", onPointerDown);
      canvas.removeEventListener("pointerup", onPointerUp);
      canvas.removeEventListener("wheel", onWheel);
      orbit.dispose();
      tumble.dispose();
      pointGeometry.dispose();
      pointMaterial.dispose();
      lineMaterial.dispose();
      litMaterial.dispose();
      lines?.geometry.dispose();
      litLines?.geometry.dispose();
      renderer.dispose();
      canvas.remove();
      labelLayer.remove();
    },
  };
}
