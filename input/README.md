# Input data

| Path | Content | Origin |
|---|---|---|
| `Funded projects – Table for Download - EuroQol.csv` | The EuroQol funded-projects export: 1,024 rows, one per grant. UTF-8, RFC 4180, every field quoted, no embedded newlines. The filename contains an en dash. | Downloaded on 2026-07-28 from [euroqol.org](https://euroqol.org/research-at-euroqol/our-research-portfolio/funded-projects-download/) |
| `projects/index.json` | Every project except its abstract, in CSV row order | `scripts/split_projects.py` |
| `projects/<Project Id>/project.json` | One CSV row, normalized: integers parsed, working groups as a list, grant type from the id suffix, empty cells as `null` | `scripts/split_projects.py` |
| `projects/<Project Id>/abstract.txt` | The abstract verbatim; absent for the 20 rows with an empty abstract | `scripts/split_projects.py` |

Regenerate the project directories with `python3 scripts/split_projects.py`. Nothing in `input/` is enriched from external sources. Downloaded full texts are not in the repository.

## Columns

| Column | Notes |
|---|---|
| `Project Id` | Unique. Suffix scheme (`1489-RA`) or eight-digit scheme (`20190670`; revision `20180340R1`). Two irregular ids: `215-2020RA`, `92-2020RA`. |
| `Title` | Always present. |
| `Abstract` | Median about 1,800 characters, up to about 12,000. Empty for 20 rows. |
| `Project PI / Applicant Name` | Always present; 344 distinct values; 8 rows hold more than one name. |
| `Working Group` | Multi-value, eight groups. Do not split on `", "`: the group *Dissemination, OA fee* contains a comma. Match the closed vocabulary in `web/shared/utils/workingGroups.ts`. |
| `Approved Budget (EUR)` | Integer euros. Total about 51.1 million; 21 rows are 0. |
| `Status` | `Completed` 711, `Ongoing` 312, `Closed` 1. |
| `Start Year` | 2012 to 2027; empty in 5 rows. |
| `End Year` | 2013 to 2030; empty in 190 rows. |

Grant-type suffixes and counts: RA 484, EO 48, VS 36, TVG 29, BT 23, PHD 21, SG 11, TR 7, EOI 6, PD 2, PCG 1; 354 ids carry no suffix (projects starting 2012 to 2022). Open-access fee awards carry `-EO` ids and *Dissemination, OA fee* in `Working Group`. Grant categories: [Guidelines for Applicants](https://euroqol.org/research-at-euroqol/funding/guidelines-for-applicants/).
