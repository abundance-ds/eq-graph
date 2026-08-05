# Protocol

> **Summary only.** The governing research method and current counts are in
> [`protocol-2.0.md`](protocol-2.0.md). Use
> [`docs/METHOD_SIMPLE.md`](docs/METHOD_SIMPLE.md) for the short method and
> [`docs/PROVENANCE.md`](docs/PROVENANCE.md) for the evidence trail.
> The project is paused after the complete scale screen and before scale full-text
> retrieval. See [`PAUSE_2026-08-05.md`](scale/protocol-2.0/PAUSE_2026-08-05.md).

## Aim

Identify EuroQol-funded publications, verify project links, and extract graph-ready data.

## Workflow

```text
1. People → 2. Publications → 3. Metadata screen → 4. Full-text verification → 5. Data extraction
```

## Phase 1 — People

| Step | Input | Action | Output | Result |
|---|---|---|---|---|
| 1. Projects | [EuroQol download](https://euroqol.org/research-at-euroqol/our-research-portfolio/funded-projects-download/) | Save all rows; key = `Project Id` | [`funded-projects-canonical.csv`](data/funded-projects-canonical.csv) | 1,024 projects |
| 2. Members | [EuroQol members](https://euroqol.org/about-us/our-members/current-members/) | Save name, affiliation, member ID and URL | [`00_euroqol_members.csv`](artefacts/00_euroqol_members.csv) | 125 unique members |
| 3. Project leaders | Project CSV | Normalise names; merge documented aliases | [`01_authors.csv`](artefacts/01_authors.csv); [alias decisions](data/person-name-overrides.csv) | 297 unique leaders |
| 4. Merge people | Leaders + members | Merge by normalised name and aliases | [`01_people.csv`](artefacts/01_people.csv) | 316 people; 106 both |
| 5. Resolve profiles | Merged people | Match in OpenAlex using name, EQ work, affiliation and ORCID; reuse prior results | [`02_author_ids.json`](artefacts/02_author_ids.json) | 282 reused; 34 queried; 286 OpenAlex IDs; 263 ORCIDs |
| 6. Review | Resolution results | Flag missing, ambiguous or suspicious profiles | [`02_review.csv`](artefacts/02_review.csv) | 45 flagged |

Google Scholar is not used. Unresolved people remain in the table.
