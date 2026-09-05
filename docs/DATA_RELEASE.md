# Data release

Release: `beta-2026-08-29`
Ontology: `0.13`
Git tag: `data-beta-2026-08-29`

Later data changes go into a new release; these files do not change.

## Contents

| Content | Count |
|---|---:|
| Funded projects | 1,024 |
| Included publications | 797 |
| Studies | 798 |
| Typed evidence items | 54,002 |
| Confirmed project-publication links | 642 |
| Findings | 5,845 |
| Limitations | 3,666 |
| Research products | 489 |
| People | 1,909 |
| Publication authorships | 4,919 |
| Unresolved authorships | 90 |

OpenAlex matched 791 publications exactly; the 2026-08-27 snapshot holds 42,727 citations.
Six publications keep a manual Google Scholar route.

## Validation

- SQLite integrity: pass for both databases.
- Foreign-key and release checks: pass.
- Public scientific uses without a canonical identity: zero.
- Aggregate test: 54 pass, 36 partial, 6 fail, 4 not testable ([result](../pilot/ontology-development-v4/aggregate-validity-v5/RESULT.md)).
- Repeated paper-ontology defect: none.

## Public-data boundary

The release retains public-source research metadata needed for attribution and
analysis. This metadata includes researcher names, identifiers, affiliations,
publication contact addresses, EuroQol membership records, project leaders, and
published approved project budgets.

The release excludes article full text, local file paths, source locators,
reference lists, possible project links, audit reasoning, credentials, and
internal communication. `scripts/check_serving_database_v2.py` checks the
database for private tables and internal source references before export.

## Release artefacts

| Database | Release copy | Bytes | SHA-256 |
|---|---|---:|---|
| Complete research database | private, outside Git | 86,376,448 | `31c3d88f48eb6a3637c3a687f250907fa3fa3e7b1138abe6ef054fb093cbfe6d` |
| Public serving database | [`release/beta-2026-08-29/eq-graph-beta-2026-08-29.sqlite`](../release/beta-2026-08-29/eq-graph-beta-2026-08-29.sqlite) | 43,044,864 | `262d00e067471c171eb4ec0b7503258d1c33e32f1ccecaf59df020025382a502` |

The private database adds source locators, reference lists, possible project links, and audit material.

## Download

Files: [`release/beta-2026-08-29/`](../release/beta-2026-08-29/) and [eq-graph.abundanceds.com/data](https://eq-graph.abundanceds.com/data).

| File | Bytes | Contents |
|---|---:|---|
| `eq-graph-beta-2026-08-29.sqlite` | 43,044,864 | The public database |
| `eq-graph-beta-2026-08-29-tables.zip` | 5,338,556 | One CSV per table, codebook, vocabulary, ontology, licence |
| `analysis/*.csv` | 12 files | Joined, analysis-ready files |
| `CODEBOOK.md` | | Tables, columns, identifiers, joins, counting rules |
| `SHA256SUMS` | | Hashes of every file |

`scripts/export_public_release.py` generates every file deterministically.
Licence: [`release/LICENSE.md`](../release/LICENSE.md). Citation: [`CITATION.cff`](../CITATION.cff).
