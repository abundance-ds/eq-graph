# Input data

Split into one directory per project under [`projects/`](projects/README.md),
which is where downloaded papers and per-project metadata will accumulate.

## `Funded projects – Table for Download - EuroQol.csv`

Export of the EuroQol Research Foundation's funded-projects portfolio,
downloaded from the public listing at <https://euroqol.org/research-at-euroqol/our-research-portfolio/funded-projects-download/> on 2026-07-28.

EuroQol funds research on the EQ-5D family of health-related quality-of-life instruments (and related measures such as EQ-HWB).
Each row is one grant awarded to an external applicant, as published by the foundation.
Note the filename contains an en dash (`–`), not a hyphen.

### Format

- UTF-8, one header row + **1024** data rows, RFC 4180-style with every field quoted.
- No embedded newlines in any field, so a line-oriented read is safe.

### Columns

| Column                        | Notes                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Project Id`                  | Unique across the file (no duplicates). Two coexisting schemes: a sequence number plus a programme suffix (`1489-RA`, `338-EO`), and a bare year-prefixed number (`20190670`, `2013010`, occasionally with a revision marker like `20180340R1`).                                                                                        |
| `Title`                       | Always present.                                                                                                                                                                                                                                                                                                                         |
| `Abstract`                    | Free text, typically structured (OBJECTIVE / METHODS / RESULTS / CONCLUSIONS). Median ~1.8 k characters, up to ~12 k. **Empty for 20 rows.**                                                                                                                                                                                            |
| `Project PI / Applicant Name` | Always present; 344 distinct values, so many PIs hold several grants. Formatting is inconsistent — titles are sometimes appended (`Marcel Jonker, PhD`), and 8 rows list more than one name.                                                                                                                                            |
| `Working Group`               | Comma-separated **multi-value** field, not a single category: 28 distinct combinations over the base groups *Valuation*, *Descriptive Systems*, *Populations and Health Systems*, *Education and Outreach*, *Youth*, *EQ-HWB*, plus the catch-alls *Others* and *Dissemination, OA fee*. Split on `, ` to get the ~8 underlying groups. |
| `Approved Budget (EUR)`       | Plain integer euros, no separators or currency symbol. Total ≈ **51.1 M EUR**, max 1 439 446, and **21 rows are 0**.                                                                                                                                                                                                                    |
| `Status`                      | `Completed` (711), `Ongoing` (312), `Closed` (1).                                                                                                                                                                                                                                                                                       |
| `Start Year`                  | 2012–2027; **empty in 5 rows**.                                                                                                                                                                                                                                                                                                         |
| `End Year`                    | 2013–2030; **empty in 190 rows** — mostly completed projects (189) rather than ongoing ones, so a blank end year does not mean "still running".                                                                                                                                                                                         |

### Grant-type suffixes in `Project Id`

The suffix is the **grant type** applied for.
EuroQol's Call for Proposals documents use the notation `XXXX-BT` / `XXXX-RA` when telling applicants which type to select,
and Appendix 3 of each call lists the full taxonomy (4 parent categories → sub-categories).
Mapping the suffixes onto that taxonomy:

| Suffix | n   | Grant type (Appendix 3 wording)                           | Parent category                    |
|--------|-----|-----------------------------------------------------------|------------------------------------|
| `RA`   | 484 | 1.1 Regular research project                              | Research grants                    |
| `EO`   | 48  | 3.1 Education and outreach project                        | Dissemination & knowledge transfer |
| `VS`   | 36  | 1.2 Valuation study                                       | Research grants                    |
| `TVG`  | 29  | 2.3 Travel grant                                          | Individual grants                  |
| `BT`   | 23  | 1.4 Bolt-on Toolbox validation                            | Research grants                    |
| `PHD`  | 21  | 2.1 PhD grant                                             | Individual grants                  |
| `SG`   | 11  | 1.3 Seed grants                                           | Research grants                    |
| `TR`   | 7   | 4.1 Tools and resources                                   | Implementation grants              |
| `EOI`  | 6   | 3.3 Expression of interest form for regional events       | Dissemination & knowledge transfer |
| `PD`   | 2   | 2.2 Postdoctoral grant (no longer offered)                | Individual grants                  |
| `PCG`  | 1   | 4.2 Program coordination grants (currently not available) | Implementation grants              |

Only `-RA` and `-BT` are stated verbatim in the call documents;
the rest are inferred by matching each suffix's projects against the taxonomy,
and the data agrees (`-TVG` are research visits, `-VS` are national value sets, `-TR` are translations/software/tooling, `-EOI` are regional meetings, `-BT` are bolt-on validation studies introduced with the 20th call).

Notes:

- **The 354 suffix-less ids are the older numbering scheme** (`20190670`, `2013010`), used for projects starting 2012–2022.
  Typed suffixes only appear from 2020 onward, so grant type is simply unavailable for the early portion of the portfolio.
  Two rows straddle the change with a `-2020RA` suffix.
- Grant types are not fixed across calls — each call states which are open,
  and `2.2 Postdoctoral` / `4.2 Program coordination` / `3.3 EOI` are currently marked unavailable, which is why their counts are tiny.
- `3.2 Open access fee reimbursement` has **no suffix of its own**: those awards carry `-EO` ids and are identifiable only by the `Dissemination, OA fee` value in `Working Group`.
- `Working Group` is the scientific working group(s) that reviewed the proposal, which is orthogonal to the grant type —
  e.g. a `-TVG` travel grant may sit under *Youth* or *Valuation*.

Sources: [Funded projects download](https://euroqol.org/research-at-euroqol/our-research-portfolio/funded-projects-download/) ·
[Guidelines for Applicants](https://euroqol.org/research-at-euroqol/funding/guidelines-for-applicants/) ·
[20th Joint Call for Proposals (PDF, incl. Appendix 3)](https://euroqol-domain.ams3.digitaloceanspaces.com/wp-content/uploads/2025/09/01170150/EuroQol-20th-RFP-with-appendices.pdf) ·
[21st Joint Call for Proposals (PDF)](https://euroqol-domain.ams3.digitaloceanspaces.com/wp-content/uploads/2026/02/16125721/EuroQol-21st-Joint-Call-for-Proposals-with-appendices.pdf)
