<script setup lang="ts">
import type { DemoResearchData } from "../../shared/types/demo";

useHead({
  title: "About EQ-Graph",
  meta: [{
    name: "description",
    content: "About EQ-Graph, its research method, ontology, team, and contact details.",
  }],
});

const { data } = await useFetch<DemoResearchData>("/api/story");
const portfolio = computed(() => data.value?.portfolio);
const n = (value: unknown) => Number(value ?? 0).toLocaleString("en");

const repo = "https://github.com/abundance-ds/eq-graph";
const email = "paul@abundanceds.com";
</script>

<template>
  <main class="about">
    <SiteHeader current="about" />

    <section class="about-hero">
      <h1>About this project</h1>
      <div class="about-intro">
        <div>
          <p class="about-lead">
            <strong>EQ-Graph</strong> is a research knowledge graph of EuroQol-funded projects.
            It connects projects and researchers to the instruments, methods, and findings
            reported in the associated publications.
          </p>
        </div>
        <div>
          <p>
            The aim is to map EuroQol's research portfolio and make it easier to explore,
            query, and study as one connected body of evidence.
          </p>
          <p>
            The public data release and code are openly available.
            <a href="/data">Download the data</a> or
            <a :href="repo" target="_blank" rel="noopener noreferrer">view the research repository</a>.
          </p>
        </div>
        <div>
          <p>
            The project was conducted by Paul Schneider, Anuja Kulkarni, and Kazik Pogoda,
            supported by EuroQol seed grant 2582-SG.
          </p>
          <p>
            Contact: <a :href="`mailto:${email}`">{{ email }}</a>
          </p>
        </div>
      </div>

      <p v-if="portfolio" class="about-release">
        <span>Beta research release</span>
        <b>{{ n(portfolio.projects) }}</b> funded projects
        <i aria-hidden="true">·</i>
        <b>{{ n(portfolio.works) }}</b> included publications
        <i aria-hidden="true">·</i>
        <b>{{ n(portfolio.studies) }}</b> studies
        <i aria-hidden="true">·</i>
        ontology 0.13
      </p>
    </section>

    <section id="methods" class="about-methods">
      <div class="about-section-head">
        <div>
          <p class="about-section-label">Methods Summary</p>
          <p class="about-section-note">
            For more details, see
            <a :href="repo" target="_blank" rel="noopener noreferrer">research repository</a>.
          </p>
        </div>
        <h2>From funded projects to structured research evidence</h2>
      </div>
      <div class="about-method-copy">
        <p>
          First, we took the public list of EuroQol-funded projects. We extracted the
          principal investigators, removed duplicates, and matched them to public author
          profiles on OpenAlex and ORCID where possible.
        </p>
        <p>
          We then searched OpenAlex, ORCID, and PubMed for publications linked to those
          investigators or to EuroQol funding. After removing duplicates, 28,600 records
          remained. Of these, 18,348 journal articles and reviews with an abstract entered
          screening.
        </p>
        <p>
          An AI screen of the 18,348 abstracts routed 1,679 papers to full-text assessment.
          We retrieved 1,607 full texts; 72 were not retrieved. Full-text assessment confirmed
          EuroQol support or a funded-project origin for 797 papers, which were processed and
          included in the knowledge graph.
        </p>
        <p class="about-method-note">
          Note on AI use: the human authors planned and designed this study, reviewed its
          outputs, and take full responsibility for it. Large parts of the implementation,
          from screening to data extraction, were carried out by AI agents.
        </p>
      </div>

      <section id="ontology" class="about-ontology" aria-labelledby="ontology-heading">
        <div class="about-subhead">
          <p>Ontology</p>
          <h3 id="ontology-heading">What the graph can represent</h3>
        </div>
        <OntologyPlate />
      </section>

      <section class="about-development" aria-labelledby="development-heading">
        <div class="about-subhead">
          <p>Ontology development</p>
          <h3 id="development-heading">Bottom-up ontology creation</h3>
        </div>
        <div class="about-development-copy">
          <p>
            We did not assume an ontology of EuroQol research in advance (top-down). Instead,
            we used AI agents to let one emerge from the papers (bottom-up).
          </p>
          <p>
            Several AI agents independently reviewed different samples of publications and
            mapped them against candidate meta-research questions. Each agent proposed
            ontological structures, which we reviewed and then tested on unseen papers.
          </p>
          <p>
            The ontology was refined over several rounds until it remained stable. In total,
            four 15-paper development rounds and two 20-publication calibration batches
            produced version 0.13.
          </p>
        </div>
        <p class="about-method-link">
          <a :href="`${repo}/blob/main/docs/METHOD.md`" target="_blank" rel="noopener noreferrer">
            Read the full research method
          </a>
          <span aria-hidden="true">↗</span>
        </p>
      </section>
    </section>

    <section id="contact" class="about-contact">
      <div class="about-section-head">
        <p class="about-section-label">Contact</p>
        <h2>Corrections and contributions are welcome.</h2>
      </div>
      <div class="about-contact-copy">
        <p>
          Both humans and AI make mistakes. Please contact us if you spot an error, or if we
          missed a paper from a EuroQol-funded project.
        </p>
        <div class="about-actions">
          <a class="about-action-primary" :href="`mailto:${email}`">Email the project team</a>
          <a href="/data">Download the data</a>
          <a :href="repo" target="_blank" rel="noopener noreferrer">Research repository</a>
        </div>
      </div>
    </section>
  </main>
</template>

<style scoped>
.about{
  --ink-1:#1a1a17; --ink-2:#5c5c56; --ink-3:#8e8e86;
  --hairline:#e2e2dc; --paper:#fcfcfb; --teal:#007d6c;
  --gut:clamp(1.5rem,4vw,3rem); --measure:65ch;
  max-width:min(1140px,100% - var(--gut) * 2); margin:0 auto; padding:0 0 8rem;
  color:var(--ink-1); font:16px/1.68 var(--font-body,'Instrument Sans',sans-serif);
}
.about{--pad:3rem;}
.about-hero{padding-top:10.5rem;}
.about-section-label,.about-subhead>p:first-child{
  margin:0; color:var(--ink-3); font:500 .72rem/1 var(--font-num,monospace);
  letter-spacing:.075em; text-transform:uppercase;
}
.about-hero h1{
  margin:1.25rem 0 3.25rem; max-width:14ch;
  font:500 clamp(3rem,7vw,5.7rem)/.94 var(--font-display,sans-serif); letter-spacing:-.052em;
}
.about-intro{display:grid; grid-template-columns:repeat(3,1fr); gap:2.4rem; padding-top:1.7rem; border-top:1px solid var(--ink-1);}
.about-intro p{margin:0; color:var(--ink-2); font-size:1rem; line-height:1.66;}
.about-intro p+p{margin-top:.75rem;}
.about-intro .about-lead{color:var(--ink-1); font-size:1.08rem;}
.about a{color:var(--ink-1); text-decoration-thickness:1px; text-underline-offset:3px;}.about a:hover{color:var(--teal);}
.about-release{
  display:flex; align-items:center; flex-wrap:wrap; gap:.45rem .62rem;
  margin:3.1rem 0 0; padding:1rem 0; border-top:1px solid var(--hairline); border-bottom:1px solid var(--hairline);
  color:var(--ink-2); font:400 .8rem/1.5 var(--font-num,monospace); font-variant-numeric:tabular-nums;
}
.about-release span{margin-right:.7rem; color:var(--teal); font-weight:500; text-transform:uppercase; letter-spacing:.05em;}
.about-release b{color:var(--ink-1); font-weight:500;}.about-release i{color:#b9b9b1; font-style:normal;}

.about-methods{margin-top:8.5rem;}
.about-section-head{display:grid; grid-template-columns:1fr 2fr; gap:2rem; align-items:start;}
.about-section-head h2{margin:-.2rem 0 0; max-width:21ch; font:500 clamp(2rem,4.2vw,3.45rem)/1.02 var(--font-display,sans-serif); letter-spacing:-.043em;}
.about-section-note{margin:1rem 0 0; max-width:24ch; color:var(--ink-3); font-size:.86rem; line-height:1.5;}
.about-section-note a{color:var(--ink-2);}
/* Column flow: readers take the left column top to bottom, then the right. */
.about-method-copy{
  display:grid; grid-template-columns:1fr 1fr; grid-template-rows:auto auto; grid-auto-flow:column;
  gap:2.4rem; margin:3.8rem 0 0 33.333%; padding-left:.65rem; max-width:760px;
}
.about-method-copy p{margin:0; color:var(--ink-2);}
.about-method-copy .about-method-note{align-self:end; padding-top:1rem; border-top:1px solid var(--hairline); color:var(--ink-3); font-size:.9rem; line-height:1.55;}
.about-ontology{margin:8.5rem calc(50% - 50vw) 0; padding:6.5rem max(var(--gut),calc(50vw - 570px)) 7rem; background:#ededeb;}
.about-subhead{display:grid; grid-template-columns:1fr 2fr; gap:1rem 2rem; align-items:start; margin-bottom:3.25rem;}
.about-subhead h3{margin:-.25rem 0 0; max-width:24ch; font:500 clamp(1.7rem,3vw,2.5rem)/1.05 var(--font-display,sans-serif); letter-spacing:-.035em;}
.about-development{margin-top:8rem;}
.about-development-copy{display:grid; grid-template-columns:repeat(3,1fr); gap:2.4rem; padding-top:1.5rem; border-top:1px solid var(--ink-1);}
.about-development-copy p{margin:0; color:var(--ink-2);}.about-development-copy p:first-child{color:var(--ink-1);}
.about-method-link{margin:2.5rem 0 0; display:flex; gap:.45rem; align-items:center; font-weight:500;}.about-method-link span{color:var(--teal);}

.about-contact{display:grid; grid-template-columns:1fr 2fr; gap:2rem; margin-top:9rem; padding-top:3rem; border-top:1px solid var(--ink-1);}
.about-contact .about-section-head{display:block;}.about-contact .about-section-head h2{margin:1.2rem 0 0; font-size:clamp(1.8rem,3vw,2.5rem);}
.about-contact-copy{max-width:620px;}.about-contact-copy>p{margin:0; color:var(--ink-2); font-size:1.07rem;}
.about-actions{display:flex; align-items:center; flex-wrap:wrap; gap:1rem 1.6rem; margin-top:2rem;}.about-actions a{font-weight:500;}
.about-actions .about-action-primary{display:inline-flex; align-items:center; min-height:44px; padding:.72rem 1.2rem; color:#fff; background:var(--teal); border:1px solid var(--teal); border-radius:999px; text-decoration:none;}
.about-actions .about-action-primary:hover{color:#fff; background:#086f62; border-color:#086f62;}.about a:focus-visible{outline:2px solid var(--teal); outline-offset:3px; border-radius:2px;}

@media (max-width:900px){
  .about{--pad:1.5rem;}
  .about-intro,.about-development-copy{grid-template-columns:1fr; max-width:var(--measure);}
  .about-section-head,.about-subhead,.about-contact{grid-template-columns:1fr;}
  .about-section-note{max-width:var(--measure);}
  .about-method-copy{margin-left:0; padding-left:0; max-width:var(--measure);}
}
@media (max-width:640px){
  .about{padding-bottom:5rem;}.about-hero{padding-top:8.5rem;}.about-hero h1{margin-bottom:2.4rem;}
  .about-methods,.about-ontology,.about-development{margin-top:6rem;}.about-ontology{padding-top:4.5rem; padding-bottom:5rem;}
  .about-method-copy{grid-template-columns:1fr; grid-template-rows:none; grid-auto-flow:row; gap:1.4rem;}.about-contact{margin-top:6rem;}
}
@media (max-width:520px){
  .about-release{align-items:flex-start;}.about-release span{flex-basis:100%; margin:0 0 .35rem;}
}
</style>
