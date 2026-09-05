<script setup lang="ts">
const modelGroups = [
  {
    title: "Portfolio",
    entries: [
      ["Project", "title · abstract · investigator · working group · years · status"],
      ["Publication", "bibliographic metadata · funding · URLs · citations · editorial status"],
      ["Person", "names · ORCID · authorship · membership · project role"],
      ["Study", "primary family · purposes · execution state · result state"],
    ],
  },
  {
    title: "Study structure",
    entries: [
      ["StudyPart", "separable sample, data source, method, or state"],
      ["Design", "component · time · comparison · allocation"],
      ["Population + Sample", "population description · role · flow stage · size"],
      ["DataUse", "source · origin · level · purpose"],
      ["TaskDesign", "profiles · attributes · levels · blocks · randomisation"],
      ["Administration", "respondent · channel · setting · language · time point"],
      ["StudyFactor", "condition · comparator · determinant · modifier · stage"],
      ["StakeholderInvolvement", "group · activity · stage · role · influence"],
    ],
  },
  {
    title: "Scientific use",
    entries: [
      ["InstrumentUse", "instrument identity · context · function"],
      ["MethodUse", "method identity · context · function"],
      ["ProtocolUse", "protocol identity · context · function"],
      ["ModelUse", "model identity · context · function · analytic role"],
      ["SoftwareUse", "software identity · context · function"],
      ["ProductUse", "existing product examined, compared, or synthesised"],
      ["ScoringUse", "instrument responses linked to a scoring product"],
    ],
  },
  {
    title: "Evidence and control",
    entries: [
      ["Outcome", "family · source label"],
      ["Finding", "statement · selected value · unit · subgroup · comparator · uncertainty"],
      ["Interpretation", "source-reported meaning, separate from the finding"],
      ["Limitation", "source-reported limitation"],
      ["Product", "reusable output · type · dated state assertions"],
      ["Concept", "cross-cutting theme for discovery"],
      ["Gap", "unmapped value · unmodelled aspect · uncertain mapping · not reported"],
      ["SourceConflict", "contradictory source statements kept together"],
    ],
  },
];
</script>

<template>
  <figure class="op">
    <div class="op-head">
      <div>
        <p class="op-kicker">Ontology 0.13</p>
        <h4>The semantic model</h4>
      </div>
      <ul class="op-legend" aria-label="Diagram legend">
        <li><i class="is-core" />Entity</li>
        <li><i class="is-registry" />Canonical registry</li>
        <li><i class="is-control" />Control or assertion</li>
      </ul>
    </div>

    <div class="op-canvas" tabindex="0" aria-label="Scrollable ontology diagram">
      <svg viewBox="0 0 1440 1040" role="img" aria-labelledby="ontology-title ontology-description">
        <title id="ontology-title">EQ-Graph ontology version 0.13</title>
        <desc id="ontology-description">
          A technical diagram of the project, publication, person, study, scientific-use,
          evidence, product, and quality-control entities in the EQ-Graph ontology.
        </desc>

        <defs>
          <marker id="op-arrow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M 0 0 L 8 4 L 0 8 z" />
          </marker>
        </defs>

        <g class="bands" aria-hidden="true">
          <rect x="0" y="0" width="1440" height="205" />
          <rect x="0" y="205" width="1440" height="235" />
          <rect x="0" y="440" width="1440" height="300" />
          <rect x="0" y="740" width="1440" height="300" />
          <line x1="0" y1="205" x2="1440" y2="205" />
          <line x1="0" y1="440" x2="1440" y2="440" />
          <line x1="0" y1="740" x2="1440" y2="740" />
          <text x="30" y="34">01 · PORTFOLIO</text>
          <text x="30" y="239">02 · STUDY STRUCTURE</text>
          <text x="30" y="474">03 · SCIENTIFIC ACTIVITY</text>
          <text x="30" y="774">04 · EVIDENCE, OUTPUTS + CONTROL</text>
        </g>

        <g class="relations">
          <path d="M280 118 H430" /><text x="316" y="105">direct output</text>
          <path d="M650 118 H800" /><text x="718" y="105">has</text>
          <path d="M1020 118 H1170" /><text x="1050" y="105">identifies</text>
          <path class="is-primary" d="M540 158 V235 H910 V275" /><text x="666" y="224">reports</text>

          <path d="M800 320 H655" /><text x="686" y="307">describes</text>
          <path d="M435 320 H290" /><text x="337" y="307">has</text>
          <path d="M1020 320 H1135" /><text x="1053" y="307">may have</text>
          <path d="M910 365 V374 H150 V385" /><text x="940" y="371">has · optionally part-scoped</text>
          <path d="M320 374 V385" /><path d="M505 374 V385" />
          <path d="M690 374 V385" /><path d="M910 374 V385" />
          <path d="M1125 374 V385" /><path d="M1300 374 V385" />

          <path class="is-primary" d="M910 365 V492 H195 V515" />
          <path class="is-primary" d="M410 492 V515" />
          <path class="is-primary" d="M625 492 V515" />
          <path class="is-primary" d="M840 492 V515" />
          <path class="is-primary" d="M1055 492 V515" />
          <path class="is-primary" d="M1270 492 V515" />
          <text x="925" y="481">records typed uses</text>

          <path d="M195 575 V625" /><path d="M410 575 V625" />
          <path d="M625 575 V625" /><path d="M840 575 V625" />
          <path d="M1055 575 V625" /><path d="M1270 575 V625" />
          <path d="M430 690 V600 H195 V575" /><text x="218" y="594">instrument responses</text>
          <path d="M500 690 V610 H1270 V625" /><text x="918" y="603">scoring product</text>

          <path class="is-primary" d="M910 365 V794 H190 V820" />
          <path class="is-primary" d="M897 794 V820" />
          <path class="is-primary" d="M1155 794 V820" />
          <path class="is-primary" d="M910 794 V925 H165 V940" />
          <path class="is-primary" d="M355 925 V940" />
          <path class="is-primary" d="M555 925 V940" />
          <path d="M300 863 H330" /><text x="300" y="850">has</text>
          <path d="M530 863 H560" /><text x="526" y="850">supports</text>
          <path d="M1035 863 H1055" /><text x="1028" y="850">has</text>
          <path d="M540 158 V185 H42 V914 H875 V920" /><text x="50" y="905">editorial status</text>
        </g>

        <g class="node core" transform="translate(60 70)">
          <rect width="220" height="88" /><text class="name" x="16" y="28">Project</text>
          <text class="field" x="16" y="53">project_id · years · status</text><text class="field" x="16" y="72">budget · working group</text>
        </g>
        <g class="node core" transform="translate(430 70)">
          <rect width="220" height="88" /><text class="name" x="16" y="28">Publication</text>
          <text class="field" x="16" y="53">DOI · title · journal · year</text><text class="field" x="16" y="72">funding · URLs · citations</text>
        </g>
        <g class="node core" transform="translate(800 70)">
          <rect width="220" height="88" /><text class="name" x="16" y="28">Authorship</text>
          <text class="field" x="16" y="53">order · corresponding · role</text><text class="field" x="16" y="72">affiliation · resolution</text>
        </g>
        <g class="node core" transform="translate(1170 70)">
          <rect width="220" height="88" /><text class="name" x="16" y="28">Person</text>
          <text class="field" x="16" y="53">names · ORCID · OpenAlex</text><text class="field" x="16" y="72">member · project role</text>
        </g>

        <g class="node core main" transform="translate(800 275)">
          <rect width="220" height="90" /><text class="name" x="16" y="29">Study</text>
          <text class="field" x="16" y="55">primary research family</text><text class="field" x="16" y="74">purpose · execution · result</text>
        </g>
        <g class="node" transform="translate(435 278)">
          <rect width="220" height="84" /><text class="name" x="16" y="28">Population</text>
          <text class="field" x="16" y="53">label · role · age</text><text class="field" x="16" y="71">inclusion description</text>
        </g>
        <g class="node" transform="translate(70 278)">
          <rect width="220" height="84" /><text class="name" x="16" y="28">Sample</text>
          <text class="field" x="16" y="53">stage · size · unit</text><text class="field" x="16" y="71">description</text>
        </g>
        <g class="node" transform="translate(1135 278)">
          <rect width="220" height="84" /><text class="name" x="16" y="28">StudyPart</text>
          <text class="field" x="16" y="53">separable component</text><text class="field" x="16" y="71">flat, optional structure</text>
        </g>
        <g class="node" transform="translate(70 385)"><rect width="160" height="48" /><text class="name small" x="14" y="29">Purpose</text></g>
        <g class="node" transform="translate(245 385)"><rect width="150" height="48" /><text class="name small" x="14" y="29">TaskDesign</text></g>
        <g class="node" transform="translate(420 385)"><rect width="170" height="48" /><text class="name small" x="14" y="29">StudyFactor</text></g>
        <g class="node" transform="translate(605 385)"><rect width="170" height="48" /><text class="name small" x="14" y="29">Administration</text></g>
        <g class="node" transform="translate(790 385)"><rect width="240" height="48" /><text class="name small" x="14" y="29">StakeholderInvolvement</text></g>
        <g class="node" transform="translate(1045 385)"><rect width="160" height="48" /><text class="name small" x="14" y="29">Design</text></g>
        <g class="node" transform="translate(1220 385)"><rect width="160" height="48" /><text class="name small" x="14" y="29">DataUse</text></g>

        <g class="node use" transform="translate(105 515)"><rect width="180" height="60" /><text class="name small" x="14" y="25">InstrumentUse</text><text class="field" x="14" y="45">context · function</text></g>
        <g class="node use" transform="translate(320 515)"><rect width="180" height="60" /><text class="name small" x="14" y="25">MethodUse</text><text class="field" x="14" y="45">context · function</text></g>
        <g class="node use" transform="translate(535 515)"><rect width="180" height="60" /><text class="name small" x="14" y="25">ProtocolUse</text><text class="field" x="14" y="45">context · function</text></g>
        <g class="node use" transform="translate(750 515)"><rect width="180" height="60" /><text class="name small" x="14" y="25">ModelUse</text><text class="field" x="14" y="45">function · analytic role</text></g>
        <g class="node use" transform="translate(965 515)"><rect width="180" height="60" /><text class="name small" x="14" y="25">SoftwareUse</text><text class="field" x="14" y="45">context · function</text></g>
        <g class="node use" transform="translate(1180 515)"><rect width="180" height="60" /><text class="name small" x="14" y="25">ProductUse</text><text class="field" x="14" y="45">context · function</text></g>

        <g class="node registry" transform="translate(105 625)"><rect width="180" height="55" /><text class="name small" x="14" y="33">Instrument</text></g>
        <g class="node registry" transform="translate(320 625)"><rect width="180" height="55" /><text class="name small" x="14" y="33">Method</text></g>
        <g class="node registry" transform="translate(535 625)"><rect width="180" height="55" /><text class="name small" x="14" y="33">Protocol</text></g>
        <g class="node registry" transform="translate(750 625)"><rect width="180" height="55" /><text class="name small" x="14" y="33">Model</text></g>
        <g class="node registry" transform="translate(965 625)"><rect width="180" height="55" /><text class="name small" x="14" y="33">Software</text></g>
        <g class="node registry" transform="translate(1180 625)"><rect width="180" height="55" /><text class="name small" x="14" y="33">Existing Product</text></g>
        <g class="node use" transform="translate(370 690)"><rect width="190" height="48" /><text class="name small" x="14" y="29">ScoringUse</text></g>

        <g class="node" transform="translate(80 820)"><rect width="220" height="86" /><text class="name" x="16" y="28">Outcome</text><text class="field" x="16" y="54">family · source label</text><text class="field" x="16" y="72">study or part scope</text></g>
        <g class="node" transform="translate(330 820)"><rect width="200" height="86" /><text class="name" x="16" y="28">Finding</text><text class="field" x="16" y="54">statement · value · unit</text><text class="field" x="16" y="72">subgroup · uncertainty</text></g>
        <g class="node" transform="translate(560 820)"><rect width="200" height="86" /><text class="name" x="16" y="28">Interpretation</text><text class="field" x="16" y="54">source-reported meaning</text><text class="field" x="16" y="72">kept separate</text></g>
        <g class="node" transform="translate(790 820)"><rect width="215" height="86" /><text class="name" x="16" y="28">Limitation</text><text class="field" x="16" y="54">source-reported statement</text><text class="field" x="16" y="72">study or item scope</text></g>
        <g class="node" transform="translate(1055 820)"><rect width="200" height="86" /><text class="name" x="16" y="28">Product</text><text class="field" x="16" y="54">label · product type</text><text class="field" x="16" y="72">reusable output</text></g>
        <g class="node control" transform="translate(1275 820)"><rect width="135" height="86" /><text class="name tiny" x="12" y="28">ProductState</text><text class="name tiny" x="12" y="45">Assertion</text><text class="field" x="12" y="68">state · date</text></g>

        <g class="node" transform="translate(80 940)"><rect width="170" height="55" /><text class="name small" x="14" y="33">Concept</text></g>
        <g class="node control" transform="translate(270 940)"><rect width="170" height="55" /><text class="name small" x="14" y="33">Gap</text></g>
        <g class="node control" transform="translate(460 940)"><rect width="190" height="55" /><text class="name small" x="14" y="33">SourceConflict</text></g>
        <g class="node control" transform="translate(760 920)"><rect width="230" height="75" /><text class="name small" x="14" y="29">PublicationStatus</text><text class="name small" x="14" y="48">Assertion</text><text class="field" x="14" y="66">status · date · notice</text></g>
        <g class="node control" transform="translate(1055 940)"><rect width="175" height="55" /><text class="name small" x="14" y="33">Provenance</text></g>
      </svg>
    </div>

    <figcaption>
      Solid lines show typed relations. Teal lines show the path from a publication
      to a study and its structured evidence. Every extracted item retains a source locator.
    </figcaption>

    <div class="op-index" aria-label="Ontology model index">
      <section v-for="group in modelGroups" :key="group.title">
        <h5>{{ group.title }}</h5>
        <dl>
          <div v-for="entry in group.entries" :key="entry[0]">
            <dt>{{ entry[0] }}</dt>
            <dd>{{ entry[1] }}</dd>
          </div>
        </dl>
      </section>
    </div>

    <div class="op-foot">
      <p><b>Information types:</b> controlled values · canonical registries · open source-faithful text · provenance</p>
      <p>
        <a href="https://github.com/abundance-ds/eq-graph/blob/main/pilot/ontology-development-v4/ONTOLOGY.md" target="_blank" rel="noopener noreferrer">Ontology reference</a>
        <span aria-hidden="true">·</span>
        <a href="https://github.com/abundance-ds/eq-graph/blob/main/pilot/ontology-development-v4/VOCABULARY.tsv" target="_blank" rel="noopener noreferrer">Controlled vocabulary</a>
      </p>
    </div>
  </figure>
</template>

<style scoped>
.op{--op-bg:#f1f1ed;--op-paper:#fafaf8;--op-ink:#1a1a17;--op-muted:#6f6f68;--op-rule:#c9c9c1;--op-teal:#007d6c;--op-yellow:#b88016;margin:0;color:var(--op-ink);background:var(--op-bg);border-top:1px solid var(--op-ink);border-bottom:1px solid var(--op-rule)}
.op-head{display:flex;align-items:flex-end;justify-content:space-between;gap:2rem;padding:1.5rem 1.6rem 1.35rem;border-bottom:1px solid var(--op-rule)}
.op-kicker{margin:0 0 .45rem;color:var(--op-teal);font:500 .7rem/1.2 var(--font-num,monospace);letter-spacing:.08em;text-transform:uppercase}
.op-head h4{margin:0;font:500 clamp(1.25rem,2vw,1.65rem)/1.1 var(--font-display,sans-serif);letter-spacing:-.025em}
.op-legend{list-style:none;display:flex;flex-wrap:wrap;gap:.7rem 1.2rem;margin:0;padding:0;color:var(--op-muted);font-size:.76rem}
.op-legend li{display:flex;align-items:center;gap:.42rem;white-space:nowrap}.op-legend i{display:block;width:.8rem;height:.6rem;border:1px solid var(--op-ink);background:var(--op-paper)}
.op-legend i.is-registry{border-color:var(--op-teal);background:#edf7f4}.op-legend i.is-control{border-color:var(--op-yellow);background:#faf4e8}
.op-canvas{overflow-x:auto;overscroll-behavior-inline:contain;scrollbar-color:var(--op-rule) transparent}.op-canvas:focus-visible{outline:2px solid var(--op-teal);outline-offset:-2px}
.op svg{display:block;width:100%;min-width:940px;height:auto;background:var(--op-bg)}
.bands rect{fill:transparent}.bands rect:nth-child(even){fill:rgba(255,255,255,.18)}.bands line{stroke:var(--op-rule);stroke-width:1}.bands text{fill:#81817a;font:500 11px var(--font-num,monospace);letter-spacing:1.4px}
.relations path{fill:none;stroke:#9a9a92;stroke-width:1.15;marker-end:url(#op-arrow)}.relations path.is-primary{stroke:var(--op-teal);stroke-width:1.55}.relations text{fill:#777770;font:400 10px var(--font-num,monospace);letter-spacing:.2px;paint-order:stroke;stroke:var(--op-bg);stroke-width:5px}.relations marker path{fill:#9a9a92;stroke:none}
.node rect{fill:var(--op-paper);stroke:#aaa9a2;stroke-width:1;rx:2}.node.core rect{stroke:var(--op-ink)}.node.main rect{fill:#eef7f5;stroke:var(--op-teal);stroke-width:1.4}.node.use rect{fill:#f8f8f5;stroke:#8f8f88}.node.registry rect{fill:#edf7f4;stroke:var(--op-teal)}.node.control rect{fill:#faf4e8;stroke:var(--op-yellow)}
.node .name{fill:var(--op-ink);font:500 16px var(--font-body,sans-serif);letter-spacing:-.2px}.node .name.small{font-size:14px}.node .name.tiny{font-size:12px}.node .field{fill:#73736c;font:400 10px var(--font-num,monospace)}
.op figcaption{padding:1rem 1.6rem 1.1rem;border-top:1px solid var(--op-rule);color:var(--op-muted);font-size:.82rem;line-height:1.5}
.op-index{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--op-rule)}.op-index section{padding:1.55rem 1.35rem 1.8rem;border-right:1px solid var(--op-rule)}.op-index section:last-child{border-right:0}.op-index h5{margin:0 0 1.25rem;color:var(--op-muted);font:500 .68rem/1 var(--font-num,monospace);letter-spacing:.08em;text-transform:uppercase}.op-index dl,.op-index dd{margin:0}.op-index dl{display:grid;gap:1rem}.op-index dt{margin:0 0 .18rem;font:500 .84rem/1.3 var(--font-body,sans-serif)}.op-index dd{color:var(--op-muted);font:400 .68rem/1.5 var(--font-num,monospace)}
.op-foot{display:flex;justify-content:space-between;gap:2rem;padding:1.15rem 1.35rem;border-top:1px solid var(--op-rule);color:var(--op-muted);font-size:.75rem;line-height:1.5}.op-foot p{margin:0}.op-foot b{color:var(--op-ink);font-weight:500}.op-foot a{color:var(--op-ink);text-underline-offset:3px;text-decoration-thickness:1px}.op-foot a:hover{color:var(--op-teal)}
@media (max-width:900px){.op-head{align-items:flex-start;flex-direction:column;gap:1.1rem}.op-index{grid-template-columns:repeat(2,1fr)}.op-index section:nth-child(2){border-right:0}.op-index section:nth-child(-n+2){border-bottom:1px solid var(--op-rule)}.op-foot{flex-direction:column;gap:.7rem}}
@media (max-width:560px){.op-head,.op figcaption{padding-left:1rem;padding-right:1rem}.op svg{min-width:820px}.op-index{grid-template-columns:1fr}.op-index section,.op-index section:nth-child(2){border-right:0;border-bottom:1px solid var(--op-rule)}.op-index section:last-child{border-bottom:0}.op-foot{padding:1rem}}
</style>
