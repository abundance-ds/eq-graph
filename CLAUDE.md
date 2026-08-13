# CLAUDE.md

This file captures only what cannot be inferred from the codebase itself.

## Rules for editing this file

Both developers and AI agents are expected to add entries as they encounter surprises.

- **Add an entry** when you encounter something unexpected: a build quirk, a non-obvious constraint, a dependency gotcha, or any behavior that would surprise the next agent or developer.
- **Add an entry** when a developer flags an anti-pattern produced by AI — describe the anti-pattern and the preferred alternative.
- **Do not** add codebase overviews, directory listings, or anything discoverable by reading the source.
- Keep entries concise: one line per lesson, grouped under a heading if a theme emerges.

## Known gotchas

- `Working Group` in the EuroQol CSV is multi-value joined with `", "`, but one of the groups is itself named `Dissemination, OA fee` — splitting on `", "` silently invents two groups for those 5 rows.
  Match against the closed vocabulary instead.
- Crossref cursor paging returns the **same** `next-cursor` token on every page, so consecutive page URLs are byte-identical.
  Behind any URL-keyed cache this replays page 2 forever (it silently inflated a 513-result sweep to "4000").
  Use `offset` paging for Crossref; Europe PMC's `cursorMark` does advance and is fine.
- Grant numbers are **not** globally unique across funders: Europe PMC `GRANT_ID:"2013010"` returns awards from the Norwegian South East Health Authority and a Chinese biofuel lab.
  Always confirm the matching grant's `agency` before treating a grant-id hit as evidence.
- Free-text searching a EuroQol project id only works for the 8-digit scheme.
  Suffix ids tokenize apart, and `-RA` collides with "RA" for rheumatoid arthritis — a search for `"100-RA"` returned a materials-chemistry paper on ZnO heterojunctions.
- OpenAlex is now **metered** and the free daily allowance is a fraction of a cent; a single funders query exhausted it.
  Do not assume it is a free bulk source.
- Anything whose output lands in git must iterate `set`s in sorted order.
  Python randomizes string hashing per process, so unsorted set iteration silently reordered exported evidence and rewrote ~540 tracked files on every identical rerun.
- Publishers 403 automated PDF fetches even for CC-licensed articles (Elsevier, BMJ, MDPI, Wiley all did).
  Treat 401/403 as terminal, not as a retryable failure.
- Europe PMC's `ACK_FUND:"EuroQol"` finds 626 works; the free-text phrase `"EuroQol Research Foundation"` finds 1147.
  The index only holds funding statements EPMC managed to parse, so never treat it as the full funder corpus.
- The grant id is printed in the article's acknowledgement text far more reliably than it is indexed.
  Harvesting OA full text and reading ids out of it (within ~300 chars of a EuroQol mention, else reused grant numbers produce false hits) is the highest-yield attribution route available without paid sources.
- OpenAIRE holds no EuroQol funder records (`funder=EuroQol` returns 0).
  Do not spend time on it for this corpus.
- A real desktop browser gets the same publisher URLs that answer 403 to `requests`, Elsevier/Wiley/MDPI/BMJ included.
  Two catches: Chrome opens a PDF in its viewer instead of saving it unless `plugins.always_open_pdf_externally` is set in the profile, and BMJ's `.full.pdf` needs the clearance cookie from a prior visit to the article landing page.
  Manual retrieval is a last resort, not a pipeline stage.
- Europe PMC's `fullTextXML` 404s for PMCIDs it lists, because the PMCID exists in the index while the OA full text does not.
  `pmc.ncbi.nlm.nih.gov/articles/<PMCID>/pdf/` usually serves the article those 404s hid.
- Unpaywall listing *no* location is not evidence an article is unobtainable.
  All 22 Creative-Commons works with an empty `oa_locations` were served by the publisher's own landing page, so `skip_reason` describes Unpaywall's coverage, not the article.
- A repository location with `url_for_pdf: null` is usually not a location without a file — the file is one fetch behind the landing page's `citation_pdf_url` meta tag (both Erasmus `pure.eur.nl` deposits resolved this way).
  Resolve landing pages only for works that would otherwise be skipped, or every settled work re-fetches one.
- Not every repository record has a file, though: figshare 29878841 is listed by Unpaywall as an OA location for `10.1016/j.jval.2025.07.009` while the record itself is metadata-only — zero files, licence *All Rights Reserved*.
  Check the figshare API (`api.figshare.com/v2/articles/<id>`) before treating such a hit as retrievable.
- A work with no DOI never reaches the Unpaywall path at all, so it is reported as having no free copy however open it is.
  169-RA's compendium was indexed only as an NCBI Bookshelf stub (`NBK589304`, no PDF) while being a fully open-access Springer book — `link.springer.com/content/pdf/10.1007/978-3-030-89289-0.pdf` serves all 115 pages to plain `curl`.
  For book-shaped records, search Crossref by title for the book DOI rather than trusting the work row.
- Publisher PDF routes that are not what the obvious URL suggests: BMC articles now redirect to `link.springer.com`, where the download button serves `/content/pdf/<doi>_reference.pdf` — the bare `<doi>.pdf` that `citation_pdf_url` advertises 404s.
  ScienceDirect challenges a direct `/pdfft` navigation every time, but the tokenised `pdfft?md5=…&pid=1-s2.0-<PII>-main.pdf` href *on the article page* is served;
  match that anchor on the article's own PII, since the page also links the PDFs of everything it cites.
- ISPOR society sites (`valueinhealthjournal.com/article/<PII>/pdf`) hand a browser the same Elsevier article that ScienceDirect guards behind Cloudflare, and never challenged.
  Prefer them for `j.jval.*`; VHRI has no such site.
- Driving Chrome over CDP needs two flags that fail silently or obscurely without it: Chrome 136+ **ignores `--remote-debugging-port` when `--user-data-dir` is the default profile** (the port simply never opens, and a second launch just prints "Opening in existing browser session"), and the WebSocket upgrade is rejected 403 without `--remote-allow-origins=*`.
  Use a throwaway profile dir carrying only `plugins.always_open_pdf_externally`;
  the open-access publishers that 403 scripts are checking for a browser, not for a login, so no cookies from the real profile are needed.
  6 of 7 such PDFs came down from a cold profile.
- CDP download events are **browser-wide**, not per-connection.
  Two fetch jobs against one Chrome will consume and delete each other's files: running a Sage and a ScienceDirect job together filed the Sage PDF under the ScienceDirect DOI, and the byte count looked entirely plausible.
  Drive one target at a time, and verify a downloaded PDF against its expected title before trusting it.
- Pandoc's JATS reader **discards the reference text at read time**: each `<ref>` survives only as `{"id": "CR1"}`, so the body gets an empty `<div id="refs">` and no template, Lua filter or `--citeproc` can put the bibliography back.
  `--citeproc` actively makes it worse — every entry renders as "n.d.-a" *and* the numeric markers in the body are rewritten to match, so `[4]` becomes `[(n.d.-d)]`.
  Read the reference list out of the XML instead, and leave citations as pandoc emits them without citeproc.
  Same class of loss, quieter: the abstract is filed under document metadata, and every Markdown writer drops it unless a `--template` asks for it, so a plain `pandoc -f jats -t gfm` silently loses the abstract *and* the title.
- Elsevier's *Value in Health* PDFs draw `−`, `<`, `>`, `≥` and `≤` from a Mathematical Pi symbol font whose glyphs carry no usable ToUnicode map, so **every** text extractor reads them as `2`, `,`, `.`, `$` and `#`.
  "Values ranged from −0.654" comes out as "from 20.654" and `P < .001` as `P , .001` — plausible, silent, and fatal to any number extracted downstream.
  All 7 PDFs held here are affected.
  The substitution is fixed per font, so repair it by font identity (`pdftohtml -xml` reports the font of every run) and never by context: a context rule cannot tell the corrupted `2` from the one in "20.5%".
  [`scripts/pdf_markdown.py`](scripts/pdf_markdown.py) carries the table.
- `pdftohtml -xml` emits a `<fontspec>` only on the page that first uses a font id, and later pages reuse those ids without redeclaring them.
  Building the font table per page therefore leaves most of the document with no resolvable font — which looks like "this PDF has no symbol fonts" rather than like a bug.
  Accumulate the table across pages.
- `pdftotext`'s de-hyphenation rejoins a word broken across lines by dropping the hyphen, which rewrites the instrument names this corpus is about: "EQ-" + "5D-5L" becomes `EQ5D-5L`.
  Whether a line-break hyphen was real is not decidable from the fragments ("evi-dence" is one word, "long-term" is two), so use the document as its own dictionary — whichever form occurs elsewhere in the paper wins — and keep the hyphen when neither does.
- Repository deposits staple a cover sheet in front of the PDF (White Rose and Erasmus both do), restating the citation and licence in the repository's house font.
  That font is what identifies it: the sheet shares no font family with the article, which a genuine first page always does.
- A replacement string passed to `re.sub`/`subn` is scanned for escapes, so substituting text harvested from a document explodes on the first `\c` (`re.PatternError`) and would silently expand a `\1`.
  Pass a callable — `subn(lambda _: block, …)` — whenever the replacement is data rather than a literal.
- Demoting headings by one to nest a document under its own title can push a level-6 heading to `#######`, which is not a heading in Markdown at all and renders as literal text — 27 of 220 papers hit this.
  Clamp at 6.
- `npx skills add <repo> --skill <name>` installs one skill at a time (the repo README only advertises the install-everything form), but it **skips a skill silently** when its `SKILL.md` frontmatter is invalid YAML — the warning scrolls past among unrelated ones and the exit code stays 0.
  `neo4j-mcp-skill` hits this, and is vendored here with the offending colon patched; see [`.agents/skills/README.md`](.agents/skills/README.md).
  `skills-lock.json` pins no commit SHA and does not list the patched skill, so it is a provenance record, not a restore mechanism — that is why the skills are committed.
- There is no embedded Neo4j to test against, because [`graph/schema.cypher`](graph/schema.cypher) needs Enterprise (`IS NODE KEY`, existence and property-type constraints) and no embedded Enterprise database is publicly obtainable any more.
  `org.neo4j.test:neo4j-harness-enterprise` on Maven Central stops at 3.5.0-beta03 (2018);
  Neo4j's support KB points at `com.neo4j.test:neo4j-harness-enterprise` instead, which is customer-only — and `maven.neo4j.com`, `artifacts.neo4j.com` and `repo.neo4j.com` now all resolve to nothing, so that repository cannot be reached at all.
  The remaining options are the `neo4j:<version>-enterprise` Docker image (`NEO4J_ACCEPT_LICENSE_AGREEMENT=yes`, which the operations manual pairs with "use ... without a proper commercial license ... is prohibited") or a real instance.
  `TestNeo4j` therefore connects to whatever `NEO4J_URI` / `NEO4J_USER` / `NEO4J_PASSWORD` point at, exactly as `application.yaml` does — tests do not run without those set.
- Tests share the developer's live database, so anything destructive in test scaffolding is live ammunition.
  `TestNeo4j.cleanDatabase()` (`MATCH (n) DETACH DELETE n`) was harmless against the old embedded instance and was removed rather than re-aimed at Aura.
- The Aura instance reports `5.27-aura` / Cypher 5, not a calendar version.
  `graph/schema.cypher` applies to it whole — all 48 constraints and 20 indexes, `vector.quantization.type: 'SCALAR'` included — but the 2026.x features its comments hold in reserve (the `SEARCH` clause, filterable vector metadata via `WITH [...]`, and `GRAPH TYPE` in [`graph/graph-type.cypher`](graph/graph-type.cypher)) are not available there yet.
  Check `dbms.components()` before assuming a Cypher feature exists.
- `kotlin-test-junit5` still pins `junit-platform-launcher` at 1.10.1, while the rest of JUnit here is 6.x.
  Nothing else requests the launcher, so there is no version conflict for Gradle to resolve and it silently stays four majors behind, failing the whole test task with `TestEngine with ID 'junit-jupiter' failed to discover tests` — the actual cause, `OutputDirectoryCreator not available … unaligned versions`, is two `Caused by` levels down and invisible without `--stacktrace`.
  The `junit-bom` platform plus a versionless `testRuntimeOnly` launcher in [`build.gradle.kts`](build.gradle.kts) keeps the two aligned as either side moves.
- Ktor 3.4.1 stopped sending `Accept-Charset` ([KTOR-5616](https://youtrack.jetbrains.com/issue/KTOR-5616)) and 3.5.0 deprecated the header ([KTOR-9355](https://youtrack.jetbrains.com/issue/KTOR-9355)).
  ContentNegotiation derived the *response* charset from it, so `call.respond` now emits a bare `application/json` where it used to emit `application/json; charset=UTF-8` — a wire-visible change to our own API that no changelog entry mentions.
  `respondStreaming` in [`HttpResponses.kt`](src/main/kotlin/HttpResponses.kt) still sets the charset by hand, so the streaming and non-streaming endpoints now disagree on the header.
- The backend under `src/` is derived from [xemantic-neo4j-demo](https://github.com/xemantic/xemantic-neo4j-demo) (Apache-2.0), so its files keep the upstream copyright headers even though this repository has no root `LICENSE`.
  The Kotlin sources sit flat under `src/main/kotlin` while declaring `package rs.shoulde.eqgraph` — that mismatch is the upstream convention, not an oversight.

## Anti-patterns to avoid

- Do not attribute a paper to a specific grant on PI-name evidence alone.
  344 PIs hold 1024 grants, so name matching cannot tell which of a PI's grants a paper belongs to;
  it yields a review pool, not an attribution.
- Do not treat the ledger's `query` as a record of where a file came from.
  It is the settle key — the whole candidate list — so reading provenance out of it rewrote hand-recorded source URLs with a pipe-joined string.
  For anything already on disk, `manifest.json` is the only provenance record, and `fulltext.py` reads it back.
- Do not add content to this file that is already discoverable by reading the source or build scripts — that inflates context without adding signal, reducing AI agent task success rates (see [arxiv 2602.11988](https://arxiv.org/abs/2602.11988)).
- Do not hard-wrap Markdown at a column limit.
  Break lines **semantically** instead — after a sentence, or at a major clause boundary — and let the line run as long as the thought does.
  Our IDEs soft-wrap for display, so a column limit buys nothing and costs plenty: reflowing one word rewrites a whole paragraph, so diffs stop showing which sentence actually changed.
  This file and the root `README.md` follow the rule; the READMEs under `input/` and `scripts/` do not yet, so rewrap a paragraph there when you are editing it anyway rather than as a separate sweep.
