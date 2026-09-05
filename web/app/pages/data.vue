<script setup lang="ts">
useHead({
  title: "EQ-Graph data",
  meta: [{
    name: "description",
    content: "Download the EQ-Graph research database as SQLite, CSV tables, or analysis-ready files.",
  }],
});

const release = "beta-2026-08-29";
const repo = "https://github.com/abundance-ds/eq-graph";
const raw = `${repo}/raw/main/release/${release}`;
const blob = `${repo}/blob/main/release/${release}`;
const tree = `${repo}/tree/main/release/${release}`;

const files = [
  {
    label: "SQLite database",
    note: "47 tables in one file.",
    meta: "43 MB",
    href: `${raw}/eq-graph-${release}.sqlite`,
  },
  {
    label: "CSV tables",
    note: "One CSV per table, plus codebook, vocabulary, and ontology.",
    meta: "5 MB zip",
    href: `${raw}/eq-graph-${release}-tables.zip`,
  },
  {
    label: "Analysis files",
    note: "Twelve joined CSVs, ready for R, Python, or Stata.",
    meta: "folder",
    href: `${tree}/analysis`,
  },
  {
    label: "Codebook",
    note: "Tables, columns, joins, and counting rules.",
    meta: "read",
    href: `${blob}/CODEBOOK.md`,
  },
];
</script>

<template>
  <main class="data">
    <SiteHeader current="data" />

    <section class="data-hero">
      <h1>Download the data</h1>
      <p class="data-lead">
        1,024 projects | 797 publications | CC BY 4.0 Licence<br>
        <code style="font-size:0.75em;">Release: {{ release }}</code>
      </p>
    </section>

    <ul class="data-files">
      <li v-for="file in files" :key="file.href">
        <a :href="file.href" target="_blank" rel="noopener noreferrer">
          <span class="data-file-label">{{ file.label }}</span>
          <span class="data-file-note">{{ file.note }}</span>
          <span class="data-file-meta">{{ file.meta }}</span>
        </a>
      </li>
    </ul>

    <p class="data-foot">
      <a :href="`${repo}/blob/main/CITATION.cff`" target="_blank" rel="noopener noreferrer">Cite</a>
      <i aria-hidden="true">·</i>
      <a :href="`${repo}/blob/main/docs/DATA_RELEASE.md`" target="_blank" rel="noopener noreferrer">Release record</a>
      <i aria-hidden="true">·</i>
      <a :href="`${repo}/tree/main/release`" target="_blank" rel="noopener noreferrer">All releases</a>
      <i aria-hidden="true">·</i>
      <a :href="`${repo}/blob/main/release/LICENSE.md`" target="_blank" rel="noopener noreferrer">Licence</a>
      <i aria-hidden="true">·</i>
      <a :href="repo" target="_blank" rel="noopener noreferrer">Code</a>
    </p>
  </main>
</template>

<style scoped>
.data{
  --ink-1:#1a1a17; --ink-2:#5c5c56; --ink-3:#8e8e86;
  --hairline:#e2e2dc; --paper:#fcfcfb; --teal:#007d6c;
  --gut:clamp(1.5rem,4vw,3rem); --pad:3rem;
  max-width:min(860px,100% - var(--gut) * 2); margin:0 auto; padding:0 0 8rem;
  color:var(--ink-1); font:16px/1.68 var(--font-body,'Instrument Sans',sans-serif);
}
.data-hero{padding-top:10.5rem;}
.data-eyebrow{
  margin:0; color:var(--ink-3); font:500 .72rem/1 var(--font-num,monospace);
  letter-spacing:.075em; text-transform:uppercase;
}
.data-hero h1{
  margin:1.25rem 0 1.6rem; max-width:14ch;
  font:500 clamp(3rem,7vw,5.7rem)/.94 var(--font-display,sans-serif); letter-spacing:-.052em;
}
.data-lead{margin:0; max-width:52ch; color:var(--ink-2); font-size:1.08rem;}
.data a{color:var(--ink-1); text-decoration:none;}
.data a:hover{color:var(--teal);}
.data a:focus-visible{outline:2px solid var(--teal); outline-offset:3px; border-radius:2px;}

.data-files{list-style:none; margin:2.5rem 0 0; padding:0; border-top:1px solid var(--ink-1);}
.data-files li{border-bottom:1px solid var(--hairline);}
.data-files a{
  display:grid; grid-template-columns:minmax(12rem,1fr) 2fr auto; gap:.4rem 2rem; align-items:baseline;
  padding:1.2rem 0;
}
.data-file-label{font-weight:500; font-size:1.05rem;}
.data-file-note{color:var(--ink-2); font-size:.95rem;}
.data-file-meta{
  color:var(--ink-3); font:400 .78rem/1.5 var(--font-num,monospace);
  font-variant-numeric:tabular-nums; white-space:nowrap; text-align:right;
}
.data-files a:hover .data-file-meta{color:var(--teal);}

.data-foot{
  display:flex; flex-wrap:wrap; gap:.45rem .62rem; margin:2.2rem 0 0;
  color:var(--ink-2); font:400 .8rem/1.5 var(--font-num,monospace);
}
.data-foot i{color:#b9b9b1; font-style:normal;}

@media (max-width:900px){.data{--pad:1.5rem;}}
@media (max-width:640px){
  .data{padding-bottom:5rem;}.data-hero{padding-top:8.5rem;}
  .data-files a{grid-template-columns:1fr auto; gap:.3rem 1rem;}
  .data-file-note{grid-column:1 / -1;}
}
</style>
