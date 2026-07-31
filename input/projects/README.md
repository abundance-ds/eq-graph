# Per-project directories

One directory per funded project,
generated from [`../Funded projects – Table for Download - EuroQol.csv`](../README.md) by [`../../scripts/split_projects.py`](../../scripts/split_projects.py).
1024 projects, matching the 1024 data rows one-to-one.

Regenerate with:

```sh
python3 scripts/split_projects.py
```

The script is idempotent — it rewrites a file only when its content changes,
so a rerun after a fresh CSV export touches just the rows that actually moved,
and warns about directories whose project no longer appears in the CSV (it never deletes them, because by then they may hold downloaded material).

## Directory name

The `Project Id` verbatim (`1489-RA`, `20190670`, `20180340R1`).
It is unique across the export and already filesystem-safe.
Ids come from two schemes and are *not* zero-padded, so directory listings sort lexically rather than chronologically — use `index.json` when order matters.

## Generated files

| File                   | Notes                                                                                                                                                                                                                                                                            |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project.json`         | The CSV row, normalized: integers parsed, `Working Group` split into a list, grant type derived from the id suffix, empty cells as `null`. Excludes the abstract.                                                                                                                |
| `abstract.txt`         | The `Abstract` cell verbatim, plus a trailing newline. **Absent for the 20 rows with an empty abstract** — check `has_abstract` in `project.json` rather than assuming the file exists.                                                                                          |
| `publications.json`    | Publications matched to this project by [the scraping pipeline](../../scripts/README.md), split into `accepted` / `review` / `weak` by evidence strength, each with its evidence trail and an `access` block saying whether a free copy exists. **Absent when nothing matched.** |
| `papers/`              | Downloaded open-access full texts, one file per publication, named by work id. Europe PMC JATS XML where available, otherwise an openly licensed PDF. Committed, since the repository is private.                                                                                |
| `papers/manifest.json` | Tracked in git: every accepted publication with its retrieval `status`, `method`, source URL, licence, byte count and SHA-256 — including the ones deliberately *not* downloaded, with the reason and a DOI landing page.                                                        |

Everything in `project.json` is derived from the CSV alone; nothing here has been enriched from external sources yet.
`pi_name_raw` is deliberately unparsed — the field mixes appended academic titles and multi-name rows,
and splitting it is part of the entity-resolution work, not of this export.

Identifiers and match evidence live in `publications.json`, so there is no separate `sources.json`.

Keep derived graph artefacts out of these directories — `input/` stays the immutable record of what was collected.

## index.json

A single machine-readable mirror of the whole portfolio: every project's metadata except the abstract, in CSV row order.
Convenient for filtering and for driving batch jobs without walking 1024 directories.
