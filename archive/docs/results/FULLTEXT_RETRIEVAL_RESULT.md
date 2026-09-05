# Full-text retrieval result

## Counts

| | records |
|---|---|
| routed to retrieval by the abstract screen | 1,679 |
| **verified full text** | **1,607** — 885 XML, 722 PDF |
| not retrieved, disposition recorded | 72 |
| unfinished | 0 |

Verified means that the file belongs to the expected publication. It does not
mean that the publication is eligible for the graph. Full-text assessment must
still confirm EuroQol support or an accepted funded-project link.

## How the 1,607 were obtained

Two passes, in order.

**Automated, 2026-08-24.** A resumable runner reused audited local sources, then
tried Europe PMC JATS, indexed open-access PDFs, OpenAlex, and Unpaywall. It
verified 1,153 records — 885 XML and 268 PDF — and referred 526 to manual
retrieval. Code checked each file against its DOI, PMID, or bibliographic
identity; Luna reviewed only eight unclear first-page cases.

**Manual, 2026-08-25 to 2026-08-26.** An operator worked the 526 through a
Ruhr-Universität Bochum entitlement in their own browser, and a colleague
contributed two files. This added 454 records. The routes are per publisher and
none generalises; they are written down in
[`MANUAL_FULLTEXT_DOWNLOAD.md`](../../../pipeline/MANUAL_FULLTEXT_DOWNLOAD.md). Every manual file
passed the same identity check as the automated pass, which rejected six
misfiled PDFs.

An operator scope screen removed a further 36 records from the queue instead of
retrieving them; see [`SCOPE_SCREEN_RESULT.md`](SCOPE_SCREEN_RESULT.md).

## The 72 not retrieved

Each is registered with a disposition in
[`../data/fulltext-not-retrieved.csv`](../../../data/fulltext-not-retrieved.csv),
one row per record with `record_id`, `year`, `doi`, `title`, `disposition`,
`revisit`, and `basis`. The dispositions are:

| disposition | records | meaning | revisit |
|---|---|---|---|
| `outside_scope` | 36 | Removed by the operator scope screen. | no |
| `not_accessible` | 20 | The publication exists and has a publisher route, but no entitlement served it. | yes |
| `not_found` | 12 | No DOI and no retrievable full text located. | yes |
| `supplement_only` | 2 | The record is a supplementary file, not a publication. Crossref type `component`. | no |
| `abstract_only` | 1 | The record is a conference poster abstract. No full text exists. | no |
| `duplicate` | 1 | A second record for a publication already verified under another id. | no |

`revisit = yes` marks the 32 records that are potentially relevant and merely
unobtained. They are the reacquisition list. Nothing downstream waits on them:
full-text assessment proceeds on the 1,607.

A disposition is not an eligibility decision. `outside_scope` is the only code
that asserts anything about the content, and it is an operator screen, not the
full-text gate.

## Reversing a disposition

No file was discarded, so every row is reversible. Delete the row from the
register, put the file in `manual/<record_id>.pdf` or `.xml`, and rerun:

```sh
.venv/bin/python pipeline/run_scale_fulltext_retrieval.py \
  --execute --retry --record-id <record_id>
```

Then rerun the deterministic text preparation and paper-package build. Both
reuse completed work. See [`FULLTEXT_PREPARATION_RESULT.md`](FULLTEXT_PREPARATION_RESULT.md).

## Run location and hashes

The run is in `scale/protocol-2.0/fulltext-retrieval-v2/`, which git ignores.
The register above is the tracked record of its unfinished tail.

- queue SHA-256 `4628d6e86486d6b540a26dfe766bb071aade8c7e9d1943bba642ee1f91c009bf`
- result SHA-256 `950162a7dbbe8fe37fbf3bf4ea4a878782060ab479cbcdb51f9f1a7c07c6cfb4`

```sh
python3 pipeline/run_scale_fulltext_retrieval.py --execute --workers 6
```
