# Manual full-text download

The manual download queue handles articles that automated retrieval cannot reach.
See [docs/RESULTS.md](../docs/RESULTS.md) for the queue counts and dispositions, and [`data/fulltext-not-retrieved.csv`](../data/fulltext-not-retrieved.csv) for the register.

This file stays because the queue can reopen: the register marks records for reacquisition, and any new abstract-screen batch produces a new manual tail.

## File hand-off

Name each file `<record_id>.pdf` or `<record_id>.xml`, using the ID in the first column of the queue CSV.
Put it in `scale/protocol-2.0/fulltext-retrieval-v2/manual/`.
Do not convert or edit the file.
Provide the published article, not a supplement, abstract, or different version.

Import it:

```sh
.venv/bin/python pipeline/run_scale_fulltext_retrieval.py \
  --execute --retry --record-id <record_id>
```

The runner checks format, records a SHA-256, and accepts the file only when its first pages match the expected DOI, PMID, or bibliographic details.
Rerun the deterministic text preparation and paper-package build afterwards; both reuse completed work.

Not every queued record should be retrieved.
An operator scope screen removes records the abstract screen over-routed on an author or name link; see [archive/docs/results/SCOPE_SCREEN_RESULT.md](../archive/docs/results/SCOPE_SCREEN_RESULT.md).

## Publisher routes

Scripted HTTP does not work.
`curl` and `requests` were refused by every major publisher, Creative-Commons articles included.
Publishers check for a browser, not for a login.
The exceptions are small open-access platforms (PLOS, Wellcome Open Research, AFENET, CEJPH).

| Publisher | Route | Method |
|---|---|---|
| ScienceDirect | `/science/article/pii/<PII>/pdfft` | top-level navigation only; `fetch()` returns a challenge page |
| Ovid (Wolters Kluwer) | `/jnls/<journalSlug>/pdf/<doi>~x` | in-page `fetch`; the `~` suffix is required |
| Oxford | `/<jrnl>/article-pdf/<vol>/<iss>/<pg>/<internalId>/<name>.pdf` | navigation only; internal id from article page |
| Taylor & Francis | `/doi/pdf/<doi>?download=true` | in-page `fetch` |
| Springer | `/content/pdf/<doi>.pdf`, else `<doi>_reference.pdf` | in-page `fetch` |
| PLOS | `/article/file?id=<doi>&type=printable` | plain `curl` |
| Wellcome Open Research | `/articles/<vol>-<page>/v1/pdf` | plain `curl` |

Rate limiting is keyed to the cookie jar, not the IP.
ScienceDirect blocked after roughly 15 rapid downloads; a fresh incognito window resumed immediately from the same address.

Chrome blocks script-initiated downloads silently for any site not on the `automatic_downloads` allow list.
The page reports success and no file arrives.
Verify against the filesystem, never against the click.
