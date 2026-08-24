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
    },
  { n: "02", name: "Agree what to extract",
    body: "A schema of entities and relationships: study, instrument, population, method, country, value set. It is expanded when a paper carries something the categories do not hold.",
    },
  { n: "03", name: "Read the full text",
    body: "A model reads each paper and returns structured fields against that schema, each one carrying the sentence it came from.",
    },
  { n: "04", name: "Check it by hand",
    body: "A person reads a sample and codes it independently, then the two are compared field by field. A pilot of 40 papers has been through this.",
    },
  { n: "05", name: "Make it answerable",
    body: "The graph behind a page you can read and a question you can ask in plain English, with the source paper attached to every answer." },
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
    <!-- Pinned to the viewport, not to the reading column, so it lands on the
         same pixel as the home page. Inside the centred column it drifted to
         wherever that column began, which is why it looked like it had moved. -->
    <header class="ab-top">
      <!-- The mark is the way home, which is where a reader already looks for
           it. A separate Back button said the same thing twice. -->
      <NuxtLink to="/" aria-label="EuroQol home">
        <img class="ab-logo" src="/brand/euroqol-logo.svg" alt="EuroQol" width="300" height="49">
      </NuxtLink>
    </header>
    <SiteNav current="about" />

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
            <h3>{{ s.name }}</h3>
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
/* Hierarchy comes from space and size, not from rules and chips.

   The earlier version fenced every section with a hairline, put each limitation
   in a bordered box and tagged each stage with a coloured pill. That is the look
   of a template being filled in. Here the only horizontal rule is under the
   headline; everything else is separated by how far apart it sits. */
.ab{
  --measure:62ch;
  --gut:clamp(1.5rem, 4vw, 3rem);
  max-width:min(1140px, 100% - var(--gut) * 2);
  margin:0 auto; padding:0 0 9rem;
  color:var(--ink-1,#1a1a17);
  font:16px/1.68 var(--font-body,'Instrument Sans',sans-serif);
}

/* Pinned to the page, so it lands where the home page puts it. */
.ab-top{ position:absolute; left:var(--gut); top:1.55rem; z-index:5; }
.ab-top a{ display:block; }
/* The nav is positioned against --pad on the story, so this page has to hand it
   the same value or the two would not line up between screens. */
.ab{ --pad:var(--gut); }
.ab-logo{ height:27px; width:auto; display:block; }
@media (max-width:900px){ .ab-top{ left:var(--gut); } .ab-logo{ height:22px; } }

.ab-hero{ padding-top:10rem; }
.ab-eyebrow{
  margin:0 0 1.5rem; color:var(--ink-3,#8e8e86);
  font:400 .95rem/1 var(--font-body,sans-serif);
}
.ab-hero h1{
  margin:0 0 2rem; max-width:19ch;
  font:500 clamp(2.4rem, 6vw, 4.1rem)/1.04 var(--font-display,sans-serif);
  letter-spacing:-.035em;
}
.ab-lede{
  margin:0; max-width:var(--measure);
  font-size:1.18rem; line-height:1.62; color:var(--ink-2,#5c5c56);
}

/* The one rule on the page, because these numbers are the evidence and the
   line is what makes them a set rather than a sentence. */
.ab-counts{
  display:grid; gap:2.2rem 1.5rem; margin:6rem 0 1.4rem;
  grid-template-columns:repeat(auto-fit, minmax(150px, 1fr));
  padding-top:2rem; border-top:1px solid var(--hairline,#e8e8e4);
}
.ab-counts div{ display:flex; flex-direction:column; gap:.3rem; }
.ab-counts b{
  font:400 2.3rem/1 var(--font-body,sans-serif);
  letter-spacing:-.03em; font-variant-numeric:tabular-nums;
}
.ab-counts span{ color:var(--ink-3,#8e8e86); font-size:.9rem; }
.ab-caveat{ margin:0; max-width:var(--measure); color:var(--ink-2,#5c5c56); }
.ab-caveat b{ font-weight:500; color:var(--ink-1,#1a1a17); }

.ab-block{ margin-top:7rem; }
.ab-block h2{
  margin:0 0 3rem; max-width:var(--measure);
  font:500 clamp(1.5rem, 2.6vw, 2rem)/1.18 var(--font-display,sans-serif);
  letter-spacing:-.025em;
}

/* Numbered because they really are a sequence: a paper cannot be read before
   it has been found. The number is quiet — it orders, it does not announce. */
.ab-stages{ list-style:none; margin:0; padding:0; display:grid; gap:3.2rem; }
.ab-stages li{ display:grid; grid-template-columns:3.5rem 1fr; align-items:baseline; }
.ab-num{
  color:var(--ink-4,#b9b9b1);
  font:400 .9rem/1.6 var(--font-body,sans-serif); font-variant-numeric:tabular-nums;
}
.ab-stages h3{
  margin:0 0 .5rem;
  font:500 1.1rem/1.4 var(--font-body,sans-serif); letter-spacing:-.01em;
}
.ab-stages p{ margin:0; max-width:var(--measure); color:var(--ink-2,#5c5c56); }

/* No boxes. Each limitation is a small headline and a paragraph, set like the
   stages above, because it carries the same weight as the method. */
.ab-limits dl{ margin:0; display:grid; gap:2.6rem; }
.ab-limits dt{ margin-bottom:.5rem; font-weight:500; font-size:1.1rem; letter-spacing:-.01em; }
.ab-limits dd{ margin:0; max-width:var(--measure); color:var(--ink-2,#5c5c56); }

.ab-who{ margin:0; max-width:var(--measure); font-size:1.06rem; color:var(--ink-2,#5c5c56); }
.ab-who a{ color:var(--ink-1,#1a1a17); text-decoration:underline; text-underline-offset:3px; text-decoration-thickness:1px; }
.ab-who a:hover{ color:var(--accent,#007d6c); }
.ab-draft{ margin:2.4rem 0 0; max-width:var(--measure); color:var(--ink-4,#b9b9b1); font-size:.95rem; }

@media (max-width:640px){
  .ab-hero{ padding-top:9rem; }
  .ab-stages li{ grid-template-columns:2.6rem 1fr; }
  .ab-block{ margin-top:5rem; }
}
</style>
