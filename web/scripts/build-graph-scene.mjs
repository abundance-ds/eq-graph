#!/usr/bin/env node
/*
  Builds the static scene behind /graph.

  Reads the serving database, assembles the graph-shaped entities (people,
  projects, papers, products, instrument hubs), runs one seeded 3-D force layout
  per lens, and writes public/graph-scene.json.  The output is deterministic:
  same database, same bytes.

  Usage:  node scripts/build-graph-scene.mjs [--db server/data/serving.sqlite]
*/
import { DatabaseSync } from "node:sqlite";
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import {
  forceCenter, forceCollide, forceLink, forceManyBody, forceRadial,
  forceSimulation, forceX, forceY, forceZ,
} from "d3-force-3d";
import { parseWorkingGroups } from "../shared/utils/workingGroups.ts";

const here = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const dbFlag = args.indexOf("--db");
const dbPath = resolve(here, "..", dbFlag >= 0 ? args[dbFlag + 1] : "server/data/serving.sqlite");
const outPath = resolve(here, "..", "public/graph-scene.json");

const KIND = { person: 0, project: 1, paper: 2, product: 3, instrument: 4 };
const INSTRUMENT_MIN_PAPERS = 8;
const GROUPS = [
  "Valuation",
  "Descriptive Systems",
  "Populations and Health Systems",
  "Education and Outreach",
  "Youth",
  "EQ-HWB",
  "Dissemination, OA fee",
  "Others",
];

/* Deterministic pseudo-random source (LCG), shared by every simulation. */
function lcg(seed) {
  let s = seed >>> 0;
  return () => {
    s = (Math.imul(1664525, s) + 1013904223) >>> 0;
    return s / 4294967296;
  };
}

const db = new DatabaseSync(dbPath, { readOnly: true });
const rows = (sql) => db.prepare(sql).all();

/* ── entities ─────────────────────────────────────────────────────── */

const personRows = rows(`
  SELECT pe.person_id AS id, pe.display_name AS name,
    (SELECT COUNT(DISTINCT publication_id) FROM publication_authors pa
      WHERE pa.person_id=pe.person_id AND pa.resolution_status='ACCEPTED') AS papers,
    (SELECT COUNT(*) FROM project_people pp WHERE pp.person_id=pe.person_id) AS led,
    EXISTS(SELECT 1 FROM euroqol_memberships em WHERE em.person_id=pe.person_id) AS member
  FROM people pe
  WHERE pe.entity_kind='PERSON'
  ORDER BY pe.person_id
`).filter((r) => Number(r.papers) > 0 || Number(r.led) > 0);

const projectRows = rows(`
  SELECT project_id AS id, title, principal_investigator AS pi, working_group AS wg,
         start_year AS year, approved_budget_eur AS budget
  FROM projects ORDER BY project_id
`);

const paperRows = rows(`
  SELECT p.publication_id AS id, p.title, p.doi, p.publication_year AS year, p.journal,
         COALESCE(c.cited_by_count, 0) AS cites
  FROM publications p
  LEFT JOIN publication_citations c
    ON c.publication_id=p.publication_id AND c.match_status='EXACT'
  ORDER BY p.publication_id
`);

const productRows = rows(`
  SELECT rp.product_id AS id, rp.product AS name, rp.product_type AS type, s.publication_id AS paper
  FROM research_products rp JOIN studies s USING(study_id)
  ORDER BY rp.product_id
`);

const authorshipRows = rows(`
  SELECT DISTINCT pa.publication_id AS paper, pa.person_id AS person
  FROM publication_authors pa JOIN people pe USING(person_id)
  WHERE pa.resolution_status='ACCEPTED' AND pe.entity_kind='PERSON'
  ORDER BY pa.publication_id, pa.person_id
`);

const piRows = rows(`
  SELECT project_id AS project, person_id AS person FROM project_people
  WHERE role='PRINCIPAL_INVESTIGATOR' ORDER BY project_id, person_id
`);

const linkRows = rows(`
  SELECT project_id AS project, publication_id AS paper FROM project_publications
  ORDER BY project_id, publication_id
`);

const instrumentRows = rows(`
  SELECT DISTINCT s.publication_id AS paper, iu.instrument AS instrument
  FROM instrument_uses iu JOIN studies s USING(study_id)
  ORDER BY iu.instrument, s.publication_id
`);

/* ── node table ───────────────────────────────────────────────────── */

const nodes = [];
const index = new Map();
function addNode(node) {
  index.set(node.id, nodes.length);
  nodes.push(node);
}

const truncate = (text, max) => {
  const t = String(text ?? "").replace(/\s+/g, " ").trim();
  return t.length > max ? `${t.slice(0, max - 1).trimEnd()}…` : t;
};
const norm = (value, max) => (max > 0 ? Math.log1p(value) / Math.log1p(max) : 0);

const maxPapers = Math.max(...personRows.map((r) => Number(r.papers)));
for (const r of personRows) {
  addNode({
    id: r.id, k: KIND.person, l: r.name,
    s: 0.18 + 0.82 * norm(Number(r.papers), maxPapers),
    papers: Number(r.papers), led: Number(r.led), member: Number(r.member) ? 1 : 0,
  });
}

const maxBudget = Math.max(...projectRows.map((r) => Number(r.budget) || 0));
for (const r of projectRows) {
  const groups = parseWorkingGroups(r.wg).map((g) => GROUPS.indexOf(g)).filter((g) => g >= 0);
  addNode({
    id: r.id, k: KIND.project, l: truncate(r.title, 96),
    s: 0.16 + 0.6 * norm(Number(r.budget) || 0, maxBudget),
    year: Number(r.year) || null, g: groups, pi: r.pi || "",
    budget: Number(r.budget) || null,
  });
}

const maxCites = Math.max(...paperRows.map((r) => Number(r.cites)));
for (const r of paperRows) {
  addNode({
    id: r.id, k: KIND.paper, l: truncate(r.title, 110),
    s: 0.16 + 0.84 * norm(Number(r.cites), maxCites),
    year: Number(r.year) || null, journal: truncate(r.journal, 60), cites: Number(r.cites),
    doi: r.doi || null,
  });
}

for (const r of productRows) {
  if (!index.has(r.paper)) continue;
  addNode({
    id: r.id, k: KIND.product, l: truncate(r.name, 90), s: 0.12,
    type: String(r.type || "").toLowerCase().replace(/_/g, " "), paper: r.paper,
  });
}

const instrumentPapers = new Map();
for (const r of instrumentRows) {
  if (!index.has(r.paper)) continue;
  if (!instrumentPapers.has(r.instrument)) instrumentPapers.set(r.instrument, []);
  instrumentPapers.get(r.instrument).push(r.paper);
}
const hubs = [...instrumentPapers]
  .filter(([, papers]) => papers.length >= INSTRUMENT_MIN_PAPERS)
  .sort((a, b) => b[1].length - a[1].length || a[0].localeCompare(b[0]));
const maxUses = hubs.length ? hubs[0][1].length : 1;
for (const [instrument, papers] of hubs) {
  addNode({
    id: `instrument:${instrument}`, k: KIND.instrument, l: instrument,
    s: 0.3 + 0.7 * norm(papers.length, maxUses), uses: papers.length,
  });
}

/* ── edge sets (node indices) ─────────────────────────────────────── */

const pair = (a, b) => [index.get(a), index.get(b)];
const edges = {
  authorship: authorshipRows.filter((r) => index.has(r.person) && index.has(r.paper)).map((r) => pair(r.paper, r.person)),
  pi: piRows.filter((r) => index.has(r.person) && index.has(r.project)).map((r) => pair(r.person, r.project)),
  link: linkRows.filter((r) => index.has(r.project) && index.has(r.paper)).map((r) => pair(r.project, r.paper)),
  product: nodes.filter((n) => n.k === KIND.product).map((n) => pair(n.id, n.paper)),
  instrument: hubs.flatMap(([instrument, papers]) => papers.map((p) => pair(p, `instrument:${instrument}`))),
  coauthor: [],
};

const authorsByPaper = new Map();
for (const [paper, person] of edges.authorship) {
  if (!authorsByPaper.has(paper)) authorsByPaper.set(paper, []);
  authorsByPaper.get(paper).push(person);
}
const coauthorWeight = new Map();
for (const authors of authorsByPaper.values()) {
  const sorted = [...authors].sort((a, b) => a - b);
  for (let i = 0; i < sorted.length; i++) {
    for (let j = i + 1; j < sorted.length; j++) {
      const key = sorted[i] * nodes.length + sorted[j];
      coauthorWeight.set(key, (coauthorWeight.get(key) || 0) + 1);
    }
  }
}
edges.coauthor = [...coauthorWeight]
  .map(([key, w]) => [Math.floor(key / nodes.length), key % nodes.length, w])
  .sort((a, b) => a[0] - b[0] || a[1] - b[1]);

/* Per-node facets derived from the edges: instruments used by a paper, and
   the working groups reached through PI roles or accepted project links. */
const instrumentIndexOf = new Map(hubs.map(([name], i) => [name, i]));
for (const [paper, hub] of edges.instrument) {
  const node = nodes[paper];
  const hubIndex = instrumentIndexOf.get(nodes[hub].l);
  (node.i ||= []).push(hubIndex);
}
for (const [person, project] of edges.pi) {
  const node = nodes[person];
  for (const g of nodes[project].g) if (!(node.g ||= []).includes(g)) node.g.push(g);
}
for (const [project, paper] of edges.link) {
  const node = nodes[paper];
  for (const g of nodes[project].g) if (!(node.g ||= []).includes(g)) node.g.push(g);
}
for (const node of nodes) {
  if (node.g) node.g.sort((a, b) => a - b);
  if (node.i) node.i.sort((a, b) => a - b);
}
const coauthorCount = new Map();
for (const [a, b] of edges.coauthor) {
  coauthorCount.set(a, (coauthorCount.get(a) || 0) + 1);
  coauthorCount.set(b, (coauthorCount.get(b) || 0) + 1);
}
for (const node of nodes) if (node.k === KIND.person) node.coauthors = coauthorCount.get(index.get(node.id)) || 0;

/* ── communities on the co-author graph (modularity local moves) ──── */

function communities(personIndices, links, maxGroups) {
  const ids = personIndices;
  const neighbours = new Map(ids.map((id) => [id, new Map()]));
  const degree = new Map(ids.map((id) => [id, 0]));
  let total = 0;
  for (const [a, b, w] of links) {
    neighbours.get(a).set(b, (neighbours.get(a).get(b) || 0) + w);
    neighbours.get(b).set(a, (neighbours.get(b).get(a) || 0) + w);
    degree.set(a, degree.get(a) + w);
    degree.set(b, degree.get(b) + w);
    total += w * 2;
  }
  const community = new Map(ids.map((id) => [id, id]));
  const totals = new Map(ids.map((id) => [id, degree.get(id)]));
  const order = [...ids].sort((a, b) => degree.get(b) - degree.get(a) || a - b);
  const resolution = 0.8;
  for (let pass = 0; pass < 40; pass++) {
    let moved = 0;
    for (const id of order) {
      const own = community.get(id);
      const byGroup = new Map();
      for (const [other, w] of neighbours.get(id)) {
        const g = community.get(other);
        byGroup.set(g, (byGroup.get(g) || 0) + w);
      }
      const k = degree.get(id);
      totals.set(own, totals.get(own) - k);
      let best = own;
      let bestGain = (byGroup.get(own) || 0) - (resolution * totals.get(own) * k) / total;
      for (const [g, inward] of byGroup) {
        const gain = inward - (resolution * totals.get(g) * k) / total;
        if (gain > bestGain + 1e-9 || (Math.abs(gain - bestGain) < 1e-9 && g < best)) {
          best = g;
          bestGain = gain;
        }
      }
      community.set(id, best);
      totals.set(best, (totals.get(best) || 0) + k);
      if (best !== own) moved += 1;
    }
    if (!moved) break;
  }
  const sizes = new Map();
  for (const g of community.values()) sizes.set(g, (sizes.get(g) || 0) + 1);
  const ranked = [...sizes].sort((a, b) => b[1] - a[1] || a[0] - b[0]).map(([g]) => g);
  const rank = new Map(ranked.map((g, i) => [g, Math.min(i, maxGroups)]));
  return new Map(ids.map((id) => [id, rank.get(community.get(id))]));
}

const personIndices = nodes.map((n, i) => (n.k === KIND.person ? i : -1)).filter((i) => i >= 0);
const communityOf = communities(personIndices, edges.coauthor, 8);
for (const i of personIndices) nodes[i].c = communityOf.get(i);
const communityLabels = Array.from({ length: 8 }, (_, c) => {
  const members = personIndices.filter((i) => nodes[i].c === c).sort((a, b) => nodes[b].papers - nodes[a].papers || a - b);
  const surname = (i) => nodes[i].l.trim().split(/\s+/).pop();
  return members.slice(0, 2).map(surname).join(" · ");
});

/* ── layouts ──────────────────────────────────────────────────────── */

/* Every lens is rescaled so its 90th-percentile radius lands here; the camera never has to move between lenses. */
const TARGET_RADIUS = 150;
const isolatedRadius = (present) => Math.cbrt(present.length) * 11 + 60;

function layout({ key, nodeFilter, edgeSets, seed, ticks, configure }) {
  const present = nodes.map((n, i) => (nodeFilter(n, i) ? i : -1)).filter((i) => i >= 0);
  const presentSet = new Set(present);
  const random = lcg(seed);
  const simNodes = present.map((i) => {
    const t1 = random() * Math.PI * 2;
    const t2 = Math.acos(2 * random() - 1);
    const r = 40 + random() * 40;
    return {
      i, size: nodes[i].s, kind: nodes[i].k, degree: 0,
      x: r * Math.sin(t2) * Math.cos(t1), y: r * Math.sin(t2) * Math.sin(t1), z: r * Math.cos(t2),
    };
  });
  const byIndex = new Map(simNodes.map((n) => [n.i, n]));
  const links = [];
  for (const set of edgeSets) {
    for (const e of edges[set]) {
      if (!presentSet.has(e[0]) || !presentSet.has(e[1])) continue;
      links.push({ source: byIndex.get(e[0]), target: byIndex.get(e[1]), set, w: e[2] || 1 });
      byIndex.get(e[0]).degree += 1;
      byIndex.get(e[1]).degree += 1;
    }
  }
  const sim = forceSimulation(simNodes, 3).randomSource(random).stop();
  configure(sim, simNodes, links, isolatedRadius(present));
  for (let t = 0; t < ticks; t++) sim.tick();

  /* Recentre and scale to a common radius so lenses share a camera. */
  let cx = 0, cy = 0, cz = 0;
  for (const n of simNodes) { cx += n.x; cy += n.y; cz += n.z; }
  cx /= simNodes.length; cy /= simNodes.length; cz /= simNodes.length;
  const radii = simNodes.map((n) => Math.hypot(n.x - cx, n.y - cy, n.z - cz)).sort((a, b) => a - b);
  const scale = TARGET_RADIUS / Math.max(1, radii[Math.floor(radii.length * 0.9)]);
  const pos = new Float32Array(nodes.length * 3);
  const positioned = new Uint8Array(nodes.length);
  for (const n of simNodes) {
    pos[n.i * 3] = (n.x - cx) * scale; pos[n.i * 3 + 1] = (n.y - cy) * scale; pos[n.i * 3 + 2] = (n.z - cz) * scale;
    positioned[n.i] = 1;
  }
  return { key, present, pos, positioned, links: links.length, centre: [cx, cy, cz], scale };
}

const everything = layout({
  key: "everything",
  nodeFilter: () => true,
  edgeSets: ["authorship", "pi", "link", "product", "instrument"],
  seed: 11, ticks: 360,
  configure(sim, simNodes, links, shell) {
    const distance = { authorship: 13, pi: 15, link: 15, product: 7, instrument: 24 };
    sim
      .force("link", forceLink(links).distance((l) => distance[l.set]).strength((l) => (l.set === "instrument" ? 0.25 : l.set === "product" ? 0.9 : 0.6)))
      .force("charge", forceManyBody().strength((n) => -(5 + 26 * n.size)).theta(0.9).distanceMax(150))
      .force("shell", forceRadial((n) => (n.degree ? 0 : shell)).strength((n) => (n.degree ? 0.03 : 0.7)))
      .force("center", forceCenter(0, 0, 0));
  },
});

const people = layout({
  key: "people",
  nodeFilter: (n) => n.k === KIND.person && n.papers > 0,
  edgeSets: ["coauthor"],
  seed: 23, ticks: 420,
  configure(sim, simNodes, links, shell) {
    sim
      .force("link", forceLink(links).distance((l) => 28 / Math.sqrt(l.w)).strength((l) => Math.min(1, 0.25 + l.w * 0.12)))
      .force("charge", forceManyBody().strength((n) => -(6 + 22 * n.size)).theta(0.9).distanceMax(160))
      .force("shell", forceRadial((n) => (n.degree ? 0 : shell)).strength((n) => (n.degree ? 0.03 : 0.7)))
      .force("center", forceCenter(0, 0, 0));
  },
});

/* Working-group anchors sit on a ring so programmes read as regions. */
const groupAnchor = GROUPS.map((_, g) => {
  const a = (g / GROUPS.length) * Math.PI * 2;
  return { x: Math.cos(a) * 60, y: Math.sin(a) * 60, z: ((g % 2) - 0.5) * 30 };
});
const funding = layout({
  key: "funding",
  nodeFilter: (n) => n.k === KIND.project || n.k === KIND.paper || (n.k === KIND.person && n.led > 0),
  edgeSets: ["pi", "link"],
  seed: 37, ticks: 380,
  configure(sim, simNodes, links, shell) {
    const anchor = (n) => {
      const g = nodes[n.i].g?.[0];
      return g == null ? null : groupAnchor[g];
    };
    sim
      .force("link", forceLink(links).distance((l) => (l.set === "pi" ? 12 : 14)).strength(0.7))
      .force("charge", forceManyBody().strength((n) => -(6 + 20 * n.size)).theta(0.9).distanceMax(160))
      .force("x", forceX((n) => anchor(n)?.x ?? 0).strength((n) => (anchor(n) ? 0.1 : 0)))
      .force("y", forceY((n) => anchor(n)?.y ?? 0).strength((n) => (anchor(n) ? 0.1 : 0)))
      .force("z", forceZ((n) => anchor(n)?.z ?? 0).strength((n) => (anchor(n) ? 0.1 : 0)))
      .force("shell", forceRadial((n) => (n.degree ? 0 : shell)).strength((n) => (n.degree ? 0.01 : 0.6)))
      .force("center", forceCenter(0, 0, 0));
  },
});

/* A timeline reads sideways: wide year spacing and firm centring in y and z
   make the ribbon broader than it is tall, so the axis spans the screen. */
const yearX = (year) => (year - 2016) * 20;
const time = layout({
  key: "time",
  nodeFilter: (n) => n.k === KIND.paper || n.k === KIND.instrument,
  edgeSets: ["instrument"],
  seed: 53, ticks: 340,
  configure(sim, simNodes, links) {
    const hubYear = new Map();
    for (const l of links) {
      const hub = l.target.kind === KIND.instrument ? l.target : l.source;
      const paper = hub === l.target ? l.source : l.target;
      const y = nodes[paper.i].year;
      if (!y) continue;
      const acc = hubYear.get(hub.i) || { sum: 0, n: 0 };
      acc.sum += y; acc.n += 1;
      hubYear.set(hub.i, acc);
    }
    const targetX = (n) => {
      if (n.kind === KIND.paper) return yearX(nodes[n.i].year || 2016);
      const acc = hubYear.get(n.i);
      return acc ? yearX(acc.sum / acc.n) : 0;
    };
    sim
      .force("link", forceLink(links).distance(20).strength(0.18))
      .force("charge", forceManyBody().strength((n) => -(6 + 30 * n.size)).theta(0.9).distanceMax(120))
      .force("x", forceX(targetX).strength((n) => (n.kind === KIND.paper ? 0.9 : 0.5)))
      .force("y", forceY(0).strength(0.07))
      .force("z", forceZ(0).strength(0.12))
      .force("collide", forceCollide((n) => 1.6 + 3 * n.size).strength(0.6).iterations(1));
  },
});

/* ── serialise ────────────────────────────────────────────────────── */

const round = (v) => Math.round(v * 10) / 10;
function lensPositions(lens) {
  const out = new Array(nodes.length * 3);
  for (let i = 0; i < nodes.length; i++) {
    if (lens.positioned[i]) {
      out[i * 3] = round(lens.pos[i * 3]);
      out[i * 3 + 1] = round(lens.pos[i * 3 + 1]);
      out[i * 3 + 2] = round(lens.pos[i * 3 + 2]);
    } else {
      /* Absent nodes fly outward along their base position and fade. */
      out[i * 3] = round(everything.pos[i * 3] * 1.9);
      out[i * 3 + 1] = round(everything.pos[i * 3 + 1] * 1.9);
      out[i * 3 + 2] = round(everything.pos[i * 3 + 2] * 1.9);
    }
  }
  return out;
}

/* Year marks for the time lens, in the lens's own (recentred, rescaled) space. */
function timeAxis(l) {
  const years = [2005, 2010, 2015, 2020, 2025];
  const ys = l.present.map((i) => l.pos[i * 3 + 1]).sort((a, b) => a - b);
  const low = ys[Math.floor(ys.length * 0.04)];
  return {
    y: round(low - 12),
    ticks: years.map((year) => ({ label: String(year), x: round((yearX(year) - l.centre[0]) * l.scale) })),
  };
}

const lenses = [
  { key: "people", label: "People", edges: ["coauthor"], layout: people },
  { key: "time", label: "Instruments", edges: ["instrument"], layout: time },
  { key: "funding", label: "Funding", edges: ["pi", "link"], layout: funding },
  { key: "everything", label: "Everything", edges: ["authorship", "pi", "link", "product", "instrument"], layout: everything },
].map(({ layout: l, ...lens }) => ({
  ...lens,
  count: l.present.length,
  links: l.links,
  present: l.present,
  pos: lensPositions(l),
  ...(l.key === "time" ? { axis: timeAxis(l) } : {}),
}));

const scene = {
  version: 1,
  groups: GROUPS,
  instruments: hubs.map(([name]) => name),
  communities: communityLabels,
  kinds: ["person", "project", "paper", "product", "instrument"],
  nodes,
  edges,
  lenses,
};

mkdirSync(dirname(outPath), { recursive: true });
writeFileSync(outPath, JSON.stringify(scene));

const kb = Math.round(Buffer.byteLength(JSON.stringify(scene)) / 1024);
console.log(`scene.json: ${nodes.length} nodes, ${kb} KB`);
for (const lens of lenses) console.log(`  ${lens.key.padEnd(11)} ${lens.count} nodes, ${lens.links} links`);

/* ── teaser: one co-author community, as drawn on the landing page ──
   A small real excerpt of the people lens, so the invitation to the graph
   shows the graph itself and not an illustration of one. */
function teaserFor(c, limit, extra) {
  const peopleLens = lenses.find((l) => l.key === "people");
  const inLens = new Set(peopleLens.present);
  const core = personIndices
    .filter((i) => (c == null || nodes[i].c === c) && inLens.has(i))
    .sort((a, b) => nodes[b].s - nodes[a].s || a - b)
    .slice(0, limit);
  const coreSet = new Set(core);
  const touches = new Map();
  for (const [a, b] of edges.coauthor) {
    if (coreSet.has(a) && !coreSet.has(b)) touches.set(b, (touches.get(b) || 0) + 1);
    if (coreSet.has(b) && !coreSet.has(a)) touches.set(a, (touches.get(a) || 0) + 1);
  }
  const rim = [...touches]
    .filter(([i, n]) => n >= 2 && inLens.has(i))
    .sort((a, b) => b[1] - a[1] || nodes[b[0]].s - nodes[a[0]].s || a[0] - b[0])
    .slice(0, extra)
    .map(([i]) => i);
  const chosen = [...core, ...rim];
  const local = new Map(chosen.map((i, n) => [i, n]));
  /* Each node keeps its four strongest ties; the rest of the mesh is noise at this size. */
  const perNode = new Map(chosen.map((i) => [i, []]));
  for (const [a, b, w] of edges.coauthor) {
    if (!local.has(a) || !local.has(b)) continue;
    perNode.get(a).push([b, w]);
    perNode.get(b).push([a, w]);
  }
  const kept = new Set();
  for (const [i, list] of perNode) {
    list.sort((x, y) => y[1] - x[1] || x[0] - y[0]);
    for (const [j] of list.slice(0, 4)) kept.add(i < j ? `${i}:${j}` : `${j}:${i}`);
  }
  const pos = peopleLens.pos;
  const centre = [0, 1, 2].map((d) => chosen.reduce((sum, i) => sum + pos[i * 3 + d], 0) / chosen.length);
  return {
    nodes: chosen.map((i) => ({
      p: [0, 1, 2].map((d) => round(pos[i * 3 + d] - centre[d])),
      s: round(nodes[i].s),
      c: nodes[i].c ?? null,
    })),
    links: [...kept].sort().map((key) => key.split(":").map((v) => local.get(Number(v)))),
  };
}
const teaserCommunity = process.env.TEASER_COMMUNITY === "all" ? null : Number(process.env.TEASER_COMMUNITY ?? 0);
const teaser = teaserFor(teaserCommunity, 64, 16);
writeFileSync(resolve(here, "..", "app/lib/graphTeaser.json"), JSON.stringify(teaser));
console.log(`teaser: community ${teaserCommunity ?? "all"}, ${teaser.nodes.length} nodes, ${teaser.links.length} links`);
if (process.env.TEASER_VARIANTS) {
  for (const variant of [0, 1, 2, null]) {
    const t = teaserFor(variant, 64, 16);
    writeFileSync(resolve(process.env.TEASER_VARIANTS, `teaser-${variant ?? "all"}.json`), JSON.stringify(t));
    console.log(`  variant ${variant ?? "all"}: ${t.nodes.length} nodes, ${t.links.length} links`);
  }
}
