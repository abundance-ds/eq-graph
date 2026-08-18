# Graph model

> **Historical Neo4j pilot.** This file describes the closed Aura model used
> before ontology version 3. The current audited research graph uses the typed
> SQLite model described in
> [`../pilot/ontology-development-v3/production-calibration/DECISION.md`](../pilot/ontology-development-v3/production-calibration/DECISION.md).
> Aura does not drive the current application or research database.

The Neo4j model for stages 2 and 3.
Runnable DDL lives in [`graph/schema.cypher`](../graph/schema.cypher); this document explains *why* it is shaped that way.

The ontology pilot is loaded in Neo4j Aura. On 2026-08-05 it contains 20
projects, 174 works, 30 accepted attributions, 30 full texts, 20 extracted
studies, and 178 findings. It is a small real-data load that will grow.

The larger numbers below are from the stage-1 corpus as of 2026-07-31: 1,026
project directories, 5,475 work rows (318 accepted, 9 review, 5,148 weak), and
287 full texts (220 JATS XML and 67 PDF). They describe source data that is not
all in Aura yet.

## Questions the model must answer

Modelling starts from the queries, not the entities.
These are the ones that justify a graph rather than a table.

1. Which publications came out of project X, and how confident are we in each link?
2. How many EQ-5D-5L value sets has the portfolio funded, for which countries, using which elicitation technique?
3. Which funded studies measured responsiveness in oncology populations, and what did they find?
4. What is the pooled sample size behind the Youth working group's output, by country?
5. Which instruments were used as comparators alongside EQ-5D, and how has that changed over time?
6. Which projects studied a condition that no other project has studied?
7. Where do two projects study the same population with different instruments — i.e. what is directly comparable?
8. Which papers report ceiling effects, and in which populations were they observed?
9. Which countries are over- or under-represented as *study sites* versus as *researcher affiliations*?
10. Show me everything the portfolio knows about proxy reporting in children.
11. For a claim the agent just made, which paper, which section, which sentence?
12. What did the extractor see that does not fit the current schema?

Query 11 is the one that decides the architecture.
An agent that cannot cite a span is not deliverable to a funder.

## Three layers

The failure mode to design against is a single flat ontology that mixes what we know for certain with what an LLM read off a PDF.
The model is therefore split into three layers that differ in how they are allowed to change and how far they can be trusted.

| Layer | Content | Populated by | Schema changes | Trust |
| --- | --- | --- | --- | --- |
| **A — bibliographic spine** | Project, Work, Person, Organization, Country, attribution evidence | stage 1, deterministic | never, without a migration | high; every value traces to a source record |
| **B — study content** | Study, Sample, Instrument, Method, ValueSet, Finding | stage 2, LLM extraction | rarely, by promotion from layer C | medium; every value traces to a text span |
| **C — emergent vocabulary** | Concept, Term | stage 2, LLM extraction | continuously, in data | low until curated |

The layers share one graph and one query language.
The separation is a discipline about *writes*, not a partition of the data.

## Layer A — bibliographic spine

### Attribution is a node, not an edge

Of 5475 work rows, 5148 rest on `ack_pi_year` alone.
As `CLAUDE.md` records, 344 PIs hold 1024 grants, so name-and-date evidence identifies *a* paper by that PI and never *which grant* funded it.
That band is a review pool by construction.

If the agent can traverse `(:Project)-[:PRODUCED]->(:Work)` without seeing confidence, it will attribute papers to the wrong grant in front of EuroQol.
So the link is reified:

```cypher
(:Project)-[:CLAIMS]->(:Attribution {confidence, score, curated, sources})-[:OF_WORK]->(:Work)
(:Attribution)-[:SUPPORTED_BY]->(:Evidence {kind, detail, weight})
```

`Evidence.kind` is a closed vocabulary — the seven kinds the matcher currently emits:
`grant_id_structured`, `grant_id_acknowledged`, `grant_id_fulltext`, `title_exact`, `title_strong`, `title_fuzzy`, `ack_pi_year`.
Adding a kind is a schema change, deliberately.

Every agent query defaults to `confidence = 'accepted'`.
The review and weak bands are reachable only through an explicit parameter that forces the answer to be labelled as provisional.
This is enforced in the query templates (below), not left to the agent's discretion.

### Affiliation belongs to the authorship, not the person

Author records currently carry `full_name`, `last_name`, `orcid` and **nothing else** — layer A has no `Organization` or `Country` yet.
Affiliations exist in the 220 JATS `<aff>` elements already on disk and are the cheapest missing piece to add.

A person's affiliation changes between papers, so it cannot hang off `:Person`:

```cypher
(:Person)-[:AUTHORED]->(:Authorship {position, isFirst, isLast, isCorresponding})-[:OF_WORK]->(:Work)
(:Authorship)-[:AT_ORGANIZATION]->(:Organization)-[:LOCATED_IN]->(:Country)
```

Contributor roles go on the authorship as `creditRoles`, following the [CRediT](https://credit.niso.org/) taxonomy — JATS already carries them, so they cost nothing to capture.

31 269 author mentions resolve to far fewer people, and most have no ORCID.
`Person.personId` is the ORCID where present and a normalised-name key otherwise, with `resolved` recording which.
Unresolved duplicates are retired with `[:MERGED_INTO]` rather than destructively, so a bad merge can be undone — the same lifecycle as layer C.

### Country means three different things

Modelling `Country` once and distinguishing by edge is the whole point of using a graph here:

```cypher
(:Organization)-[:LOCATED_IN]->(:Country)   // where the researchers are
(:Sample)-[:RECRUITED_IN]->(:Country)       // where the data came from
(:ValueSet)-[:VALUES_FOR]->(:Country)       // whose preferences were elicited
```

Conflating these answers query 9 with nonsense.
The second and third only exist in full text; only the first is derivable from metadata.

## Layer B — extracted study content

### Findings are n-ary

"EQ-5D-5L showed a 42% ceiling effect in Dutch elderly in study X" is not a binary edge.
Reifying it is what makes portfolio-level aggregation possible at all — queries 3, 5 and 8 are unanswerable without it.

```cypher
(:Finding {metric, value, ciLow, ciHigh, n, pValue, direction, statement})
  -[:ABOUT_INSTRUMENT]->(:Instrument)
  -[:IN_SAMPLE]->(:Sample)
  -[:MEASURES_PROPERTY]->(:Property)      // COSMIN
  -[:USED_METHOD]->(:Method)
  -[:REPORTED_IN]->(:Work)
  -[:EXTRACTED_FROM {quote}]->(:Chunk)
```

`EXTRACTED_FROM` points at the same `:Chunk` nodes the vector index runs over, so provenance and retrieval share one substrate rather than duplicating the text.
A finding that spans sections gets several `EXTRACTED_FROM` edges.

This edge is what makes the promised per-field accuracy assessment against the 50 hand-coded papers computable, and what lets the agent quote rather than assert.

### Value sets get their own structure

National value sets are the portfolio's highest-value output and deserve to be queryable to the coefficient:

```cypher
(:Study)-[:PRODUCED_VALUE_SET]->(:ValueSet {year, technique, nRespondents})
(:ValueSet)-[:FOR_INSTRUMENT]->(:Instrument)
(:ValueSet)-[:VALUES_FOR]->(:Country)
(:ValueSet)-[:HAS_COEFFICIENT]->(:Coefficient {dimension, level, value, se})
```

### Instrument use carries its own attributes

Mode, language and role (index measure versus comparator) are properties of *this study's use* of the instrument, not of the instrument:

```cypher
(:Study)-[:ADMINISTERED]->(:InstrumentUse {role, mode, language})-[:OF_INSTRUMENT]->(:Instrument)
```

`Instrument` itself is curated and closed for the EQ family (`EQ-5D-3L`, `EQ-5D-5L`, `EQ-5D-Y-3L`, `EQ-5D-Y-5L`, `EQ-HWB`, `EQ-HWB-S`, `EQ-VAS`, bolt-ons) and open for comparators, flagged by `isEuroQol`.

## Layer C — emergent vocabulary

### Closed labels, open vocabulary

This is the answer to "meta ontology or emergent ontology".
Both, but split along a specific seam: **let the vocabulary grow in the data, never in the label set.**

If the extractor mints labels and relationship types freely, then indexes, constraints and every generated Cypher query drift underneath the application, and no agent can reliably introspect what exists.
So everything novel lands as data:

```cypher
(:Concept {conceptId, prefLabel, definition, scheme, kind, status, support, embedding})
(:Term {text, normalized})-[:DENOTES]->(:Concept)
(:Concept)-[:BROADER]->(:Concept)
(:Concept)-[:MERGED_INTO]->(:Concept)                     // internal dedup
(:Concept)-[:EXACT_MATCH|CLOSE_MATCH]->(:Concept)         // external alignment
(:Chunk)-[:MENTIONS {count}]->(:Concept)
```

Deduplication and alignment are separate acts and get separate types.
`MERGED_INTO` retires a duplicate candidate; `EXACT_MATCH` and `CLOSE_MATCH` are `skos:exactMatch` and `skos:closeMatch`, pointing at a MeSH or Cochrane concept.
An LLM-proposed alignment to MeSH is rarely exact, and recording an approximate one as identity would poison the `BROADER*` rollups the whole design leans on.

`status` runs `candidate → promoted → merged`.
A candidate accumulates `support` as more papers mention it.
Promotion is a human decision that attaches a curated secondary label — `:Condition`, `:Method`, `:Property` — expressed as a label implication so the graph type enforces it:

```cypher
(cond:Condition => :Concept)
```

That keeps both properties of the design: labels stay curated, and label-based traversal still works for everything promoted.
Query 12 is just `MATCH (c:Concept {status:'candidate'}) RETURN c ORDER BY c.support DESC`.

### Graft onto existing vocabularies, do not author one

There is no reason to hand-build a research-domain ontology.

| Domain | Use | Instead of |
| --- | --- | --- |
| Works | DOI / PMID / PMCID | local identifiers |
| People | ORCID | name strings |
| Organizations | ROR | affiliation text |
| Countries | ISO 3166-1 alpha-2, UN M49 regions | free text |
| Clinical area, topic | **MeSH** | a bespoke condition taxonomy |
| Measurement properties | **COSMIN** | ad-hoc property names |
| Instruments, valuation technique, working group, grant type | hand-curated closed lists | anything emergent |

MeSH is the significant one.
Europe PMC already returns MeSH headings per PMID, so a maintained hierarchical ontology of the research domain arrives attached to the corpus at no cost, and `BROADER*` traversal gives the agent rollups ("all cancer studies") for free.
Only the genuinely EuroQol-local vocabularies are worth curating by hand, and they are all small and closed.

## Vocabulary alignment

The table above lists identifier *systems*.
This section states what the classes themselves mean in published vocabularies, which is a different question and matters for two reasons: the web app should emit JSON-LD the outside world can read, and alignment is free evidence that a reification is not idiosyncratic.

The governing rule is that we **model to the domain and project to schema.org at the API edge**, never the reverse.
schema.org is a web-publishing vocabulary with no way to express a measurement property, an elicitation technique or a value-set coefficient.
Modelling to it would discard exactly the distinctions that make questions 2, 3 and 8 answerable.

### Layer A

| Class | schema.org | Research-domain |
| --- | --- | --- |
| `Project` | `schema:ResearchProject`, `schema:MonetaryGrant` | `vivo:Grant` |
| `Work` | `schema:ScholarlyArticle` | `fabio:JournalArticle`, `dcterms:*` |
| `Journal` | `schema:Periodical` | `fabio:Journal` |
| `Person` | `schema:Person` | `foaf:Person` |
| `Organization` | `schema:Organization` | `org:FormalOrganization` |
| `Country` | `schema:Country` | — |
| `Authorship` | `schema:Role` | `vivo:Authorship` |
| `Attribution` | — | `prov:Attribution` |
| `Evidence` | — | partly `prov:hadRole`; mostly local |
| `FullText`, `Chunk` | `schema:MediaObject` | `prov:Entity` |
| `Extraction` | — | `prov:Activity` |

Three alignments are exact rather than approximate, which is worth knowing because each one independently validates a reification:

- `Authorship` is schema.org's `Role` pattern, and VIVO arrived at a class literally named `vivo:Authorship` for the same reason — affiliation belongs to the person-work pairing, not the person.
- `Attribution` is PROV-O's qualified-relation pattern node for node. `prov:qualifiedAttribution` → `prov:Attribution` exists precisely to hang confidence and justification off an otherwise binary link.
- `Concept` and `Term` are SKOS and SKOS-XL, below.

PROV also supplies the vocabulary for recording that an LLM produced something: `:Extraction` is a `prov:Activity`, layer-B nodes reach it via `[:GENERATED_BY]` (`prov:wasGeneratedBy`), and `[:EXTRACTED_FROM]` is `prov:wasDerivedFrom`.
That is worth having for the accuracy assessment on its own terms, export or no export — a bad prompt version has to be traceable to exactly the nodes it produced.

### Layer B

Standards thin out here, and the gaps matter more than the matches.

The best available fit is **Cochrane's PICO ontology and Linked Data Vocabulary** — roughly 400 000 terms already cross-linked to MeSH, SNOMED-CT, MedDRA, RxNorm and ATC.
PICO maps onto the extraction targets closely enough to be worth adopting rather than paralleling:

| Our class | PICO / other |
| --- | --- |
| `Sample` | PICO Population |
| `InstrumentUse {role:'index'}` | PICO Intervention |
| `InstrumentUse {role:'comparator'}` | PICO Comparison |
| `Finding` → `Property` | PICO Outcome |
| `Study` | `obi:investigation` |
| `Method` (statistical) | STATO |

What has no standard:

- **COSMIN is a taxonomy, not an ontology** — no IRIs, no machine-readable release. `:Property` codes are local, with the COSMIN term as the label.
- **Value sets and coefficients have no published ontology at all.** Entirely local, which is unsurprising: they are also the portfolio's most distinctive output.
- **LOINC for instruments is unverified.** LOINC has patient-reported-outcome panel infrastructure (`89196-0`, `72355-1`), but whether an EQ-5D-specific panel code exists was not confirmed. Search LOINC directly before designing around it.

### Layer C

SKOS, essentially unchanged: `skos:Concept`, `skos:prefLabel`, `skos:definition`, `skos:inScheme`, `skos:broader`, `skos:exactMatch`, `skos:closeMatch`, and `skosxl:Label` for `:Term`.

### Where the alignment lives

Two mechanisms, deliberately not merged.
Class-level alignment is design-time and static, so it goes in the catalog subgraph where it costs nothing at query time and the agent can read it during progressive disclosure:

```cypher
(:_Vocabulary {prefix, namespace, title})
(:_VocabularyTerm {curie})-[:IN_VOCABULARY]->(:_Vocabulary)
(:_NodeType)-[:ALIGNS_WITH {relation}]->(:_VocabularyTerm)
(:_RelType)-[:ALIGNS_WITH {relation}]->(:_VocabularyTerm)
```

Instance-level alignment is data and grows with the corpus: the `EXACT_MATCH` and `CLOSE_MATCH` edges between `:Concept` nodes.

We do **not** run the graph as RDF.
Neosemantics can round-trip it if that is ever needed, but a property graph carrying alignment metadata gives the interoperability without giving up the reified n-ary modelling that motivated choosing a graph at all.

## Presenting the graph

Some of the audience will see the graph rendered, not queried, and will not know Cypher.
That constrains presentation, not the schema — and the two are kept apart on purpose.

Relationship types stay `SCREAMING_SNAKE_CASE` and labels stay `PascalCase`, because the graph's other primary consumer is an LLM writing Cypher, and every sample in the vendored skills and in any model's training data uses those conventions.
A miscased relationship type does not raise an error in Neo4j; it returns **zero rows**, and the agent reports "no results" with full confidence.
That failure is silent and permanent, whereas readability is solved once, elsewhere:

```cypher
(:_RelType {
  name:                'PRODUCED_VALUE_SET',
  displayLabel:        'produced value set',
  displayLabelInverse: 'was produced by',
  description:         'A study that elicited a national value set.'
})
(:_NodeType {
  name:              'InstrumentUse',
  displayName:       'instrument use',
  displayNamePlural: 'instrument uses'
})
```

A display layer is needed regardless of casing — `ValueSet` and `InstrumentUse` are no more self-explanatory as captions than `PRODUCED_VALUE_SET` is — so putting it in the catalog costs nothing extra and buys three things a naming convention cannot:

- **Direction-aware phrasing.** The same edge reads *"project claims work"* one way and *"work claimed by project"* the other.
- **Renaming never breaks a query.** Wording can be iterated with EuroQol during the demo without a migration.
- **Translation stays possible.** EuroQol is not an English-only organisation.

One rendering rule follows from the reifications.
`Attribution`, `Authorship`, `InstrumentUse` and `Finding` exist because a binary edge could not carry the fact;
in a diagram they should be drawn as the labelled node with their surrounding edges left unlabelled.
`Project —— [Attribution: accepted, 0.9] —— Work` reads better than three labelled hops, and it puts confidence where a non-technical viewer will actually see it, which is the single most important thing to be visible in a EuroQol demonstration.

## Semantic search

Vector indexes earn their place for three specific jobs, not as a general retrieval layer.

**1. Entry point, not the index.**
Vector search finds anchor nodes; the answer comes from traversing outward.
Embed section-aware chunks of the 287 full texts — JATS gives real `<sec>` boundaries, so chunk on those rather than character windows — plus the 1026 project abstracts and the work titles and abstracts.
All of them are `:Chunk` nodes under one vector index, filterable by `sectionType` and `source`, keeping embeddings off the business nodes.

**2. Concept resolution during ingestion.**
Query the concept vector index before minting a new candidate.
This is the underrated use: it is what stops the emergent layer fragmenting into forty spellings of "ceiling effect".
It is also the one deliberate deviation from the "embeddings only on `:Chunk`" rule — `Concept.embedding` sits on the business node because the embedding *is* the resolution key, and there are only thousands of them.

**3. Natural-language query onto graph anchors.**
The same concept index maps a user's phrasing onto the concept the graph actually stores.

Pair all of this with Lucene full-text indexes on titles, DOIs and grant ids.
Exact-identifier lookup through a vector index is a common and embarrassing failure.

The corpus is small — order 15 000 chunks — so index size and embedding cost are not constraints.

## How the agent sees the graph

### Progressive disclosure through a catalog subgraph

The agent does not get a schema dump.
The database carries its own description, generated from `apoc.meta.stats` plus hand-written prose, under `_`-prefixed labels the application filters out of the domain schema:

```cypher
(:_NodeType {name, displayName, displayNamePlural, description, count, keyProperties, exampleCypher})
  -[:HAS_PROPERTY]->(:_PropertyDef {name, type, cardinality, sampleValues})
(:_NodeType)-[:CONNECTS_VIA]->(:_RelType {name, displayLabel, displayLabelInverse, description, count})
```

The same nodes carry the display captions and the vocabulary alignment, so one catalog serves the agent, the visualisation and the JSON-LD export.

First call: read the catalog.
Then drill into only the region the question touches.
Because it is derived from the live database it cannot go stale, and it costs one round trip instead of a permanent context tax.

### Query templates before free Cypher

`(:_QueryTemplate {name, question, cypher, params})` holds parameterised Cypher for the questions listed at the top of this document.
The agent matches a question to a template first and writes free Cypher only when nothing fits.
This is where the confidence default is enforced, and it is what makes the demo reproducible.

### Guardrails

- Read-only database user for the application; writes only from the pipeline.
- Query timeout and a server-side result cap.
- `confidence = 'accepted'` unless explicitly overridden, and the override changes the wording of the answer.

## Open questions

- **Study versus Work cardinality.** One paper may report several studies and one study may span several papers. Modelled as many-to-many; whether the extractor can reliably identify a study across papers is untested.
- **Embedding model and dimension.** `graph/schema.cypher` uses 1024 as a placeholder. It must match whatever model the pipeline uses; changing it means dropping and rebuilding the index.
- **Recruitment setting** is currently a property on `:Sample`. It is a promotion candidate if it turns out to be queried on its own.
- **Journal identity** uses the name string, since ISSN was not collected in stage 1.
- **Coefficient granularity.** Storing every value-set coefficient as a node is defensible for the ~36 valuation studies but should be reviewed once the real count is known.
- **Aura version.** `GRAPH TYPE` is a preview feature (2026.02+). `graph/schema.cypher` is the GA-safe form; `graph/graph-type.cypher` is the equivalent declaration for when it reaches GA.

## Node reference

| Label | Key | Layer | Notes |
| --- | --- | --- | --- |
| `Project` | `projectId` | A | one per funded grant |
| `WorkingGroup` | `name` | A | 8 closed values |
| `GrantType` | `code` | A | 11 suffixes, 4 parent categories |
| `GrantCategory` | `name` | A | from Appendix 3 of the call documents |
| `Work` | `workId` | A | `doi:…`, falling back to `pmid:…` / `pmcid:…` |
| `Journal` | `name` | A | no ISSN collected |
| `Person` | `personId` | A | ORCID where present |
| `Authorship` | `authorshipId` | A | intermediate; carries position and affiliation |
| `Organization` | `rorId` | A | not yet populated |
| `Country` | `iso2` | A/B | meaning carried by the edge |
| `Attribution` | `attributionId` | A | reified project→work link |
| `Evidence` | `evidenceId` | A | closed `kind` vocabulary |
| `FullText` | `sha256` | A | mirrors `manifest.json` |
| `Chunk` | `chunkId` | A | the only node carrying passage embeddings |
| `Study` | `studyId` | B | |
| `Sample` | `sampleId` | B | |
| `Instrument` | `instrumentId` | B | closed for EQ family, open for comparators |
| `InstrumentUse` | `instrumentUseId` | B | intermediate; role, mode, language |
| `Method` | `methodId` | B | also `:Concept` |
| `Property` | `code` | B | COSMIN; also `:Concept` |
| `Condition` | `code` | B | MeSH; also `:Concept` |
| `ValueSet` | `valueSetId` | B | |
| `Coefficient` | `coefficientId` | B | |
| `Finding` | `findingId` | B | n-ary; the reason the graph exists |
| `Extraction` | `extractionId` | B | `prov:Activity`; one per pipeline run |
| `Concept` | `conceptId` | C | candidate → promoted → merged |
| `Term` | `normalized` | C | surface forms |
| `_NodeType`, `_RelType`, `_PropertyDef`, `_QueryTemplate` | `name` | meta | the agent's self-description, plus display captions |
| `_Vocabulary` | `prefix` | meta | published vocabularies the model aligns to |
| `_VocabularyTerm` | `curie` | meta | the aligned class or property |
