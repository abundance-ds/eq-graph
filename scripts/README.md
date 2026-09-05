# Scripts

Build, validation, enrichment, analysis, and deployment scripts for the research database and public release.

## Release build

Build the private typed database, the public serving database, and check it.
Run from the repository root. `load_research_v2.py` lives under `pilot/ontology-development-v4/production/`.

```sh
python3 scripts/prepare_fulltext_release.py
python3 scripts/extend_person_resolution.py \
  --base-directory scale/protocol-2.0/fulltext-release-v1/person-base \
  --manifest scale/protocol-2.0/fulltext-release-v1/MANIFEST.tsv \
  --openalex scale/protocol-2.0/fulltext-release-v1/openalex-publications.jsonl \
  --output-directory scale/protocol-2.0/fulltext-release-v1/person-resolution
python3 pilot/ontology-development-v4/production/load_research_v2.py \
  --run scale/protocol-2.0/fulltext-release-v1 \
  --manifest scale/protocol-2.0/fulltext-release-v1/MANIFEST.tsv \
  --registry scale/protocol-2.0/fulltext-release-v1/REGISTRY.tsv \
  --aliases scale/protocol-2.0/fulltext-release-v1/REGISTRY_ALIASES.tsv \
  --vocabulary scale/protocol-2.0/fulltext-release-v1/VOCABULARY.tsv \
  --projects data/funded-projects-canonical.csv \
  --project-links scale/protocol-2.0/fulltext-release-v1/PROJECT_LINKS.tsv \
  --persons scale/protocol-2.0/fulltext-release-v1/person-resolution/PERSONS.tsv \
  --person-names scale/protocol-2.0/fulltext-release-v1/person-resolution/PERSON_NAMES.tsv \
  --person-identifiers scale/protocol-2.0/fulltext-release-v1/person-resolution/PERSON_IDENTIFIERS.tsv \
  --project-persons scale/protocol-2.0/fulltext-release-v1/person-resolution/PROJECT_PERSONS.tsv \
  --publication-authors scale/protocol-2.0/fulltext-release-v1/person-resolution/PUBLICATION_AUTHORS.tsv \
  --openalex-publications scale/protocol-2.0/fulltext-release-v1/openalex-publications.jsonl \
  --output scale/protocol-2.0/fulltext-release-v1/research.sqlite \
  --expect-studies 798 \
  --expect-items 54002
python3 scripts/build_serving_database_v2.py \
  --source scale/protocol-2.0/fulltext-release-v1/research.sqlite \
  --output web/server/data/serving.sqlite
python3 scripts/check_serving_database_v2.py \
  --expect-projects 1024 \
  --expect-publications 797 \
  --expect-pdf-publications 345 \
  --expect-project-leaders 297 \
  --expect-members 125 \
  --expect-leaders-and-members 106 \
  web/server/data/serving.sqlite
```

## Create a public data release

Use a new `beta-YYYY-MM-DD` name for each release. Never change a frozen release
directory.

1. Start from a clean working tree. Set the release name and confirm that its
   output directory does not exist.

   ```sh
   git status --short
   release_name=beta-YYYY-MM-DD
   release_dir="release/$release_name"
   test ! -e "$release_dir"
   ```

2. Run the release build and database check above. Review the check output and
   confirm the expected counts. The check rejects private tables, local paths,
   and other internal source references.

3. Build the website graph scene from the checked database. Then export the
   public files into the new directory.

   ```sh
   pnpm --dir web build:graph
   python3 scripts/export_public_release.py \
     --release "$release_name" \
     --output "$release_dir"
   ```

4. Confirm that the release database is identical to the checked serving
   database. Confirm all generated checksums.

   ```sh
   cmp web/server/data/serving.sqlite \
     "$release_dir/eq-graph-$release_name.sqlite"
   (cd "$release_dir" && shasum -a 256 -c SHA256SUMS)
   ```

5. Review the public files for personal data, financial data, internal
   communication, credentials, private paths, and full text. Public-source
   research metadata can contain names, affiliations, email addresses, and
   approved project budgets. Record each decision in the release record.

6. Update all release references. Use this search to find the current version
   and tag before editing:

   ```sh
   rg -n 'beta-[0-9]{4}-[0-9]{2}-[0-9]{2}|data-beta-' \
     README.md CITATION.cff docs web/app/pages/data.vue \
     pilot/ontology-development-v4/ONTOLOGY.md
   ```

   Update:

   - `README.md`: version, counts, filenames, and links.
   - `CITATION.cff`: version and release date.
   - `docs/DATA_RELEASE.md`: version, tag, counts, validation, sizes, hashes,
     and privacy decisions.
   - `docs/RESULTS.md` and `docs/HISTORY.md`: current release and dated record.
   - `web/app/pages/data.vue`: version and displayed file sizes.
   - `pilot/ontology-development-v4/ONTOLOGY.md`: release name only if this
     ontology version governs the new release.
   - `scripts/export_public_release.py`: `ZIP_TIME` when the release date
     changes.

7. Run the repository and website checks.

   ```sh
   python3 -m pytest
   pnpm --dir web test
   pnpm --dir web exec nuxi typecheck
   pnpm --dir web build
   git diff --check
   ```

   Start the local website and run the story-number check in a second terminal:

   ```sh
   pnpm --dir web dev:local
   node web/scripts/check-story-numbers.mjs
   ```

8. Review the complete diff. Commit the release, then create the annotated tag
   named in `docs/DATA_RELEASE.md`.

   ```sh
   git status --short
   git diff --stat
   git tag -a "data-$release_name" -m "Frozen data release $release_name"
   git push origin main
   git push origin "data-$release_name"
   ```

9. After publication, test every download on the website Data page and compare
   its downloaded checksums with `SHA256SUMS`.

## Deploy the web application

The production URL is `https://eq-graph.abundanceds.com`. The legacy
`https://eq-graph.shoulde.rs` URL redirects to it.

Deploy from a reviewed, committed revision. The release identifier contains
the current Git revision, but the deployment script does not check for local
changes.

For an ordinary application change, run:

```sh
pnpm --dir web test
pnpm --dir web exec nuxi typecheck
pnpm --dir web build
./scripts/deploy_web.sh
```

If the serving database changed, build and check it first. Then run
`pnpm --dir web build:graph` before `pnpm --dir web build`.

The script uses the `chat-host` SSH alias by default. Set
`EQ_GRAPH_DEPLOY_HOST` to use a different SSH target. It uploads a timestamped
release to `/home/ubuntu/eq-graph-web/releases`, changes the `current` symlink,
restarts `eq-graph-web`, and checks the production API and page. Persistent
secrets and usage data stay in `/home/ubuntu/eq-graph-web/shared`.

An ordinary deployment does not require an AWS, DNS, Caddy, or systemd change.

## Co-authorship network

Build the data package from the release database, then render the standalone interactive view:

```sh
python3 scripts/build_coauthorship_analysis.py \
  --database scale/protocol-2.0/fulltext-release-v1/research.sqlite \
  --output-directory scale/protocol-2.0/fulltext-release-v1/coauthorship

python3 scripts/render_coauthorship_network.py \
  --network-json scale/protocol-2.0/fulltext-release-v1/coauthorship/network.json \
  --output scale/protocol-2.0/fulltext-release-v1/coauthorship/coauthorship-network.html
```

## Scripts

| Script | Purpose |
|---|---|
| `prepare_fulltext_release.py` | Prepare completed full-text results for the typed database loader |
| `extend_person_resolution.py` | Extend reviewed person files with authors from a new manifest |
| `build_serving_database.py` | V1 public database builder; exports `SCHEMA`, `COUNTRY_PATTERNS`, and `countries_from` used by v2 |
| `build_serving_database_v2.py` | Build the public serving database from the typed research database |
| `check_serving_database_v2.py` | Check a typed public serving database |
| `export_public_release.py` | Export the public database as an open-data release |
| `enrich_openalex_publications.py` | Fetch DOI-matched OpenAlex citation and authorship data |
| `enrich_prepared_metadata_openalex.py` | Add exact OpenAlex metadata to prepared publication records |
| `build_person_resolution.py` | Build canonical people and identity links |
| `build_combined_release_inputs.py` | Combine frozen JATS inputs with a validated expansion tranche |
| `build_pdf_project_links.py` | Build audited project links for the local PDF tranche |
| `repair_prepared_jats_authors.py` | Create a build manifest with corrected JATS author metadata |
| `build_coauthorship_analysis.py` | Build external co-authorship files from resolved authors |
| `render_coauthorship_network.py` | Render a standalone co-authorship network HTML |
| `split_projects.py` | Split the funded-projects CSV into one directory per project |
| `to_markdown.py` | Convert harvested full texts to Markdown; also imported by `pipeline/prepare_scale_fulltexts.py` (its standalone `corpus/` output is no longer used) |
| `pdf_markdown.py` | Repair known PDF font maps and convert to Markdown |
| `hash_tree.py` | Write a deterministic SHA-256 manifest for a directory tree |
| `deploy_web.sh` | Deploy the web application |
