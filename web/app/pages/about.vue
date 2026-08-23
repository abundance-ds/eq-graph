<script setup lang="ts">
/**
 * What this is, how it was built, and what it cannot do yet.
 *
 * Skeleton. The method is still moving, so the page states the counts it can
 * verify from the live API and marks everything provisional as provisional
 * rather than writing a finished-sounding claim we would have to walk back.
 */
import type { DemoResearchData } from "../../shared/types/demo";

useHead({
  title: "About EQ-Graph",
  meta: [{ name: "description",
           content: "How the EuroQol research knowledge graph is built, and what it can and cannot answer yet." }],
});

const { data } = await useFetch<DemoResearchData>("/api/story");
const p = computed(() => (data.value as any)?.portfolio ?? {});
const n = (v: unknown) => Number(v ?? 0).toLocaleString("en");

// The share of the portfolio that has actually been read. This is the number
// the page is organised around, so it is derived here rather than written down.
const readShare = computed(() => {
  const done = Number(p.value.linkedProjects ?? 0);
  const all = Number(p.value.projects ?? 0);
  return all ? Math.round((done / all) * 100) : 0;
});

const stages = [
  { n: "01", name: "Assemble the corpus",
    body: "EuroQol's public project database lists the funded projects. Publications are matched to them from the funding acknowledgement in the paper itself.",
    state: "running" },
  { n: "02", name: "Agree what to extract",
    body: "A schema of entities and relationships: study, instrument, population, method, country, value set. It is expanded when a paper carries something the categories do not hold.",
    state: "moving" },
  { n: "03", name: "Read the full text",
    body: "A model reads each paper and returns structured fields against that schema, each one carrying the sentence it came from.",
    state: "running" },
  { n: "04", name: "Check it by hand",
    body: "A person reads a sample and codes it independently, then the two are compared field by field. A pilot of 40 papers has been through this.",
    state: "pilot" },
  { n: "05", name: "Make it answerable",
    body: "The graph behind a page you can read and a question you can ask in plain English, with the source paper attached to every answer.",
    state: "running" },
];

// Stated plainly, because a method that hides its edges is harder to trust than
// one that names them.
const limits = [
  { head: "Most of the portfolio is unread",
    body: "Papers have been matched and read for a minority of funded projects. Everything counted on this site describes that subset, not the whole portfolio." },
  { head: "It starts in 2012",
    body: "The project records available to us begin there. Earlier funded work exists and is not represented, so nothing here should be read as the full history." },
  { head: "The instrument list is not canonical",
    body: "Instrument names come from the papers as written, so the same version can appear under more than one spelling. Counts by instrument are indicative." },
  { head: "Concepts are too sparse to use",
    body: "The concept field was extracted but the values are spread too thin across studies to support any claim, so it is not shown anywhere on the site." },
  { head: "Funding is what defines the corpus",
    body: "A paper counts if EuroQol funded any part of the work behind it: the study, the data, or a researcher's time. That is read from the funding statement, which not every paper carries." },
];
</script>

<template>
  <main class="ab">
    <!-- The mark sits top left, where it sits on every other screen. Back goes
         under it, because a way out belongs below the thing it returns to. -->
    <header class="ab-top">
      <img class="ab-logo" src="/brand/euroqol-logo.svg" alt="EuroQol" width="300" height="49">
      <NuxtLink to="/" class="ab-back">← Back</NuxtLink>
    </header>

    <section class="ab-hero">
      <p class="ab-eyebrow">EQ-Graph, a EuroQol seed grant</p>
      <!-- No span of years in the headline: the records we hold start in 2012,
           and the page says so lower down. -->
      <h1>
        A thousand funded projects, written down in a form
        you can ask questions of.
      </h1>
      <p class="ab-lede">
        EuroQol has funded more than a thousand projects. What those projects found
        sits inside individual papers, one PDF at a time, which means nobody can
        answer a question about the portfolio without reading it again. This reads
        the papers and records what is in them as structured facts, so the portfolio
        can be queried instead of re-read.
      </p>
    </section>

    <!-- The counts are live, not written into the page, so this section cannot
         drift away from what the database actually holds. -->
    <section class="ab-counts" aria-label="What is in the graph today">
      <div><b>{{ n(p.projects) }}</b><span>projects funded</span></div>
      <div><b>{{ n(p.studies) }}</b><span>studies read in full</span></div>
      <div><b>{{ n(p.findings) }}</b><span>findings extracted</span></div>
      <div><b>{{ n(p.countries) }}</b><span>countries</span></div>
      <div><b>{{ n(p.authors) }}</b><span>researchers</span></div>
      <div><b>{{ n(p.valueSets) }}</b><span>value sets</span></div>
    </section>
    <p class="ab-caveat">
      Read so far: <b>{{ n(p.linkedProjects) }}</b> of <b>{{ n(p.projects) }}</b> funded
      projects, about {{ readShare }} per cent. This is a working system on a growing
      corpus, not a finished index.
    </p>

    <section class="ab-block">
      <h2>How it is built</h2>
      <ol class="ab-stages">
        <li v-for="s in stages" :key="s.n">
          <span class="ab-num">{{ s.n }}</span>
          <div>
            <h3>{{ s.name }} <em :data-state="s.state">{{ s.state }}</em></h3>
            <p>{{ s.body }}</p>
          </div>
        </li>
      </ol>
    </section>

    <!-- Given the same weight as the method, on purpose. -->
    <section class="ab-block ab-limits">
      <h2>What it cannot tell you yet</h2>
      <dl>
        <div v-for="l in limits" :key="l.head">
          <dt>{{ l.head }}</dt>
          <dd>{{ l.body }}</dd>
        </div>
      </dl>
    </section>

    <section class="ab-block">
      <h2>Who</h2>
      <p class="ab-who">
        Built by <a href="https://shoulde.rs" rel="noreferrer">Shoulders</a>, an independent
        group making AI tools for researchers, under a EuroQol seed grant. Principal
        investigator Paul Schneider, who is not a member of the EuroQol Group. The code
        is open source, and every number on this site is traceable to the paper it
        came from.
      </p>
      <p class="ab-draft">
        This page is a draft. The method is still being worked out, and it will be
        rewritten as the corpus and the schema settle.
      </p>
    </section>
  </main>
</template>

<style scoped>
.ab{
  --measure:64ch;
  max-width:min(1080px, 100% - 3rem);
  margin:0 auto; padding:0 0 6rem;
  color:var(--ink-1,#1a1a17);
  font:15px/1.6 var(--font-body,'Instrument Sans',sans-serif);
}
.ab-top{
  display:flex; flex-direction:column; align-items:flex-start; gap:1.15rem;
  padding:1.55rem 0 3.5rem;
}
.ab-logo{height:27px; width:auto;}
.ab-back{
  color:var(--ink-1,#1a1a17); text-decoration:none;
  font-size:.95rem; font-weight:600;
  padding:.35rem .1rem;
}
.ab-back:hover{color:var(--accent,#007d6c);}
.ab-back:focus-visible{outline:2px solid var(--accent,#007d6c); outline-offset:3px; border-radius:3px;}

.ab-eyebrow{
  margin:0 0 1.4rem; color:var(--ink-3,#8e8e86);
  font:500 .82rem/1 var(--font-num,monospace);
  letter-spacing:.02em;
}
.ab-hero h1{
  margin:0 0 1.6rem; max-width:22ch;
  font:500 clamp(2.1rem, 5.2vw, 3.4rem)/1.08 var(--font-display,sans-serif);
  letter-spacing:-.03em;
}
.ab-lede{margin:0; max-width:var(--measure); font-size:1.05rem; color:var(--ink-2,#5c5c56);}

/* One rule under the headline figures. They are the page's evidence, so they
   sit above the prose rather than inside it. */
.ab-counts{
  display:grid; gap:1.6rem 1.2rem; margin:4rem 0 1rem;
  grid-template-columns:repeat(auto-fit, minmax(140px, 1fr));
  padding-top:1.6rem; border-top:1px solid var(--hairline,#e5e4df);
}
.ab-counts div{display:flex; flex-direction:column; gap:.2rem;}
.ab-counts b{
  font:500 1.9rem/1 var(--font-num,monospace);
  letter-spacing:-.02em; font-variant-numeric:tabular-nums;
}
.ab-counts span{color:var(--ink-3,#8e8e86); font-size:.84rem;}
.ab-caveat{
  margin:0; max-width:var(--measure);
  color:var(--ink-2,#5c5c56); font-size:.9rem;
}
.ab-caveat b{font-family:var(--font-num,monospace); font-weight:500;}

.ab-block{margin-top:4.5rem;}
.ab-block h2{
  margin:0 0 1.8rem; padding-bottom:.9rem;
  border-bottom:1px solid var(--hairline,#e5e4df);
  font:500 1.28rem/1.2 var(--font-display,sans-serif); letter-spacing:-.02em;
}

/* Numbered because these really are ordered: a paper cannot be read before it
   has been found. */
.ab-stages{list-style:none; margin:0; padding:0; display:grid; gap:1.9rem;}
.ab-stages li{display:grid; grid-template-columns:3.2rem 1fr; align-items:start;}
.ab-num{
  color:var(--ink-4,#b9b9b1);
  font:500 .82rem/1.7 var(--font-num,monospace); font-variant-numeric:tabular-nums;
}
.ab-stages h3{
  margin:0 0 .3rem;
  display:flex; align-items:baseline; flex-wrap:wrap; gap:.6rem;
  font:500 1rem/1.5 var(--font-body,sans-serif);
}
.ab-stages h3 em{
  font:500 .72rem/1 var(--font-num,monospace);
  letter-spacing:.01em; font-style:normal;
  padding:.24rem .45rem; border-radius:3px;
  color:var(--ink-3,#8e8e86); background:var(--sunk-2,#efefec);
}
.ab-stages h3 em[data-state="pilot"],
.ab-stages h3 em[data-state="moving"]{color:#8a6d1f; background:#f6efdc;}
.ab-stages p{margin:0; max-width:var(--measure); color:var(--ink-2,#5c5c56);}

.ab-limits dl{margin:0; display:grid; gap:1.5rem;}
.ab-limits div{
  padding-left:1rem;
  border-left:2px solid var(--hairline-strong,#cbc9c1);
}
.ab-limits dt{margin-bottom:.25rem; font-weight:500;}
.ab-limits dd{margin:0; max-width:var(--measure); color:var(--ink-2,#5c5c56);}

.ab-who{margin:0; max-width:var(--measure); color:var(--ink-2,#5c5c56);}
.ab-who a{color:var(--accent,#007d6c);}
.ab-draft{
  margin:1.6rem 0 0; max-width:var(--measure);
  color:var(--ink-3,#8e8e86); font-size:.88rem;
}

@media (max-width:640px){
  .ab-stages li{grid-template-columns:2.4rem 1fr;}
  .ab-counts{gap:1.3rem 1rem;}
}
</style>
