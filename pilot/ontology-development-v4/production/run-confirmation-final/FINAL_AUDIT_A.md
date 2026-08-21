# Final confirmation repair audit A

| Record | Verdict | Source evidence and repair check | Remaining defect |
|---|---|---|---|
| CNF-P001 | PASS | `corpus/1741-RA/doi_10.1007_s40273-025-01519-7.md:134,166,664-670`. `pu3` is now a `ProtocolUse` for the exact EQ-VT 2.1 label, and `td1` and `adm1` refer to it. `mod7` is now a candidate `ModelUse` for tobit modelling. The old `mu3` and `mu5` items and references are absent. | None. |
| CNF-P002 | PASS | `corpus/1487-RA/doi_10.1007_s11136-025-04145-0.md:94,107,165,218-222,319-359`. The record now has the two author-defined Studies. Study 1 contains the unconscious defense measure and result; Study 2 contains the conscious defense measure, Study-2-only analyses, and moderation result. Pooled findings are present under both Studies with explicit pooled scope. `g1` records the missing multi-Study finding relation, and `sc1` preserves the reported denominator conflict. | None. |
| CNF-P004 | PASS | `corpus/343-RA/doi_10.1186_s12955-024-02305-3.md:62-84,106-114,1461`. `iu1` now identifies the “Amharic version of EQ-5D-5L” and maps to the Amharic EQ-5D-5L registry entry. The three source conflicts remain intact. | None. |
| CNF-P006 | PASS | `corpus/445-RA/doi_10.1016_j.pecinn.2025.100421.md:105,109-119,127-129,392-398`. `part3` now represents exposure to the revised decision aid. It has the supported completed sample of 20 and the applicable empirical and non-comparative designs. `td1` and `adm1` now have `part3`; the EQ-5D-5L remains historical input to the decision aid, not a current administration. | None. |
| CNF-P009 | PASS | `corpus/348-PHD/doi_10.1007_s40273-025-01493-0.md:312,357-367,396-406,503-513,610-667,727`. PTO, cTTO, LT TTO, DCEd, and LOD are separate `MethodUse` items. The source defines LT-TTO as lag-time TTO, and the final registry mapping preserves that meaning. The vignette is now `td1`, not an instrument, and it no longer appears in outcome instrument lists. LSS is now two `ScoringUse` items for the applicable EQ instruments. The old `iu8` and `mu5` items are absent. | None. |
| CNF-P010 | PASS | `corpus/1598-RA/doi_10.1136_bmjopen-2025-102509.md:155-173,295-305,329`. `iu10` and `adm9` separately preserve the planned adult EQ-5D-5L use by children aged 12 years or older; caregiver use remains separate. The combined responsiveness method is split into exact labels “Glass’ Δ effect sizes” and “response means.” The generic exact label “regression techniques” remains on `mo2` with a null registry mapping, as required. `lim4.about` is now empty, and the planned sample records and qualitative-sample source conflict remain correct. | None. |

## Totals and readiness

- PASS: 6
- MINOR: 0
- MAJOR: 0

All requested repairs in these six records pass this focused source audit. No repaired field introduces an unsupported fact, and no checked repair caused a regression. These records are ready for the next production step.
