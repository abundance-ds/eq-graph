# Production registry audit

## Scope and result

I checked the 20 production records against `REGISTRY.tsv`, `ONTOLOGY.md`, `VOCABULARY.tsv`, `CALIBRATION.tsv`, and the 20 source articles. The records contain 292 registry-eligible uses. Of these uses, 209 have no registry ID and 83 have a registry ID.

The main problem is the small, flat registry. Most null values are valid scientific objects, not extraction errors. The registry needs stable identities, aliases, and explicit family and version relations. It must not treat a language edition, respondent version, protocol adaptation, or experimental version as an alias for its base object.

| Null-use decision | Uses | Rule |
|---|---:|---|
| One identity: add a canonical or map an alias | 189 | One named instrument, method, model, protocol, or scoring product |
| Keep as one compound workflow | 8 | The source defines one procedure with ordered or integrated parts |
| Split or replace a compound item | 5 | The item combines methods that users can query separately |
| Hold as ambiguous | 3 | The label is not sufficient for a safe identity |
| Repair the entity type | 4 | The identity is valid, but the record uses the wrong use type |
| **Total** | **209** | |

The 209 null uses contain 196 distinct type-and-label pairs. Eleven exact duplicate-label groups account for 13 repeat uses: `EQ-TIPS-5L`, `EQ-TIPS-5L descriptive system`, `EQ-5D-Y-4L`, `WHOQOL-BREF`, `main-effects conditional logit model`, `Kruskal-Wallis test`, `standardized response mean (SRM)`, `standardized effect size (SES)`, `thematic content analysis`, `cognitive interviews`, and `algorithm derived from the crosswalk 3L value sets`.

## Non-null mappings

Of the 83 non-null mappings, 77 are safe at the stated identity level. Five are valid family matches but not exact identity matches. One maps an instrument component to the full instrument.

| Record and item | Current mapping | Decision |
|---|---|---|
| `CAL-B03/iu1` | experimental Australian proxy EQ-HWB-9 v1 -> `instrument:eq-hwb-s` | Add an exact experimental, language, and respondent-version child. Keep the EQ-HWB-S family relation. |
| `C50-P045/iu1` | Taiwan traditional-Chinese EQ-5D-5L -> `instrument:eq-5d-5l` | Add an exact language and jurisdiction child. |
| `R129-P049/pu1` | adapted translated EQ-VT -> `protocol:eq-vt` | Add a study adaptation child. Do not make the adapted protocol an alias for the standard protocol. |
| `R129-P129/iu1`, `iu8` | isiXhosa EQ-TIPS -> `instrument:eq-tips` | Add an isiXhosa South African child of EQ-TIPS-3L. The article states that the descriptive system has three response levels. |
| `R129-P106/iu3` | EQ-5D-5L anxiety/depression dimension -> `instrument:eq-5d-5l` | Repair. A dimension is not the complete instrument. Use the base instrument plus a component identity or a separate dimension field. |

The VAS mappings do not show a false match in this sample. In `R129-P106`, the article says that the VAS is included in EQ-5D-5L. In `R129-P129`, the article says that EQ-TIPS retained the EuroQol Visual Analogue Scale. These uses can map to `instrument:eq-vas`. A generic rating or valuation VAS must map to `method:vas`, or to another named instrument, unless the source gives this EQ evidence. `R129-P014` correctly separates a generic VAS method from EQ VAS.

## Required registry structure

Add these fields to the registry:

| Field | Purpose |
|---|---|
| `parent_registry_id` | Connect an exact identity to an instrument family, method family, protocol family, or product family. |
| `variant_kind` | Use controlled values such as `LEVEL_VERSION`, `LANGUAGE_EDITION`, `RESPONDENT_VERSION`, `PROTOCOL_VERSION`, `STUDY_ADAPTATION`, `EXPERIMENTAL_VERSION`, and `PRODUCT_VERSION`. |
| `language_code` | Identify a language edition. |
| `jurisdiction` | Identify a country or value-set jurisdiction when this is part of the identity. |
| `version` | Keep the stated version. |
| `source_identifier` | Keep a DOI, protocol ID, or other stable identifier. |
| `scope` | Use `GLOBAL` or a source record ID for a paper-specific procedure. |

Use typed relations. `EQ-5D-5L` is a level version of `EQ-5D`; it is not an alias. `cTTO` is a TTO method variant. EQ-VT 2.0, 2.1, and 2.6.1 are protocol versions. A value set is a scoring product for one instrument and jurisdiction. A translation or proxy form is a child identity. Add a component relation if dimension-level queries are required.

## Canonical additions and aliases

| Type | Add these canonical groups | Alias and identity rule |
|---|---|---|
| Instrument | EQ-TIPS-5L; EQ-5D-Y-4L; experimental EQ-HWB-9; EQ-5D-3L proxy v1; FACIT-COST v2; HINT-8; HUI, HUI2, HUI3; SF-6Dv1; QWB-SA; WEMWBS; FACT-G; PROMIS-16; SF-36 general-health item; mRS; Barthel-10; ZBI-22; WHOQOL-BREF; ASQ Parent Report Form; FLACC | Add exact language and respondent-version children for Indonesian FACIT-COST v2, isiXhosa EQ-TIPS-3L, Taiwan Chinese EQ-5D-5L, and Australian proxy EQ-HWB-9. Keep local questionnaires as source-scoped identities. |
| Method | Sampling families; cognitive and qualitative methods; evidence-review methods; descriptive methods; chi-square; ANOVA; t-test variants; Mann-Whitney; Kruskal-Wallis; Wilcoxon signed-rank; Pearson; Spearman; ICC; Gwet AC and AC2; Lin CCC; Bland-Altman; Cronbach alpha; McDonald omega; PCA; parallel analysis; PCHC; SRM; SES; probability of superiority; MID; Shannon indexes | Merge spelling and case aliases only when the statistical identity is the same. Keep paired, Welch, and generic t-tests separate. Keep Gwet AC and AC2 separate unless the article identifies the coefficient. |
| Model | Conditional logit; OLS; GLS; Tobit; Tobit-GLS; hybrid-model family and selected censored hybrid variant; ordinal logit; censored linear regression; linear regression; multiple linear regression; multinomial logistic regression; EFA; QALY model | Use model-family parents. Keep estimation restrictions and selected model variants as child identities or record properties. |
| Protocol | PRISMA; COSMIN risk-of-bias checklist; COREQ; PROSPERO record; EQ-VT 2.0; EQ-5D-Y translation protocol | Keep named local study protocols source-scoped. `common standardized protocol` remains unmapped until it has a name or sufficient definition. |
| Scoring product | Country- and instrument-specific EQ value sets; van Hout 5L-to-3L crosswalk; EQ-5D-Y US scoring algorithm; level-sum score | Key value sets by instrument, jurisdiction, edition, publication year, and source DOI. Do not use country-column text as the canonical label. |

Material product merges from the articles:

- `R129-P028/su1` and `R129-P117/su1` are the Indonesian EQ-5D-5L value set by Purba et al., DOI `10.1007/s40273-017-0538-9`.
- `R129-P064/su2` and `R129-P106/sc1` are the Canadian EQ-5D-5L value set.
- `R129-P110/su1` and `su2` use the same 2024 Trinidad and Tobago EQ-5D-5L value set, DOI `10.1186/s12955-024-02266-7`. They are two applications, not two products.
- `R129-P127/su1` and `su2` are two applications of the van Hout crosswalk, DOI `10.1016/j.jval.2012.02.008`.
- `R129-P129/su1` and `su2`, plus `R129-P064/mu1`, refer to level-sum scoring. The source-label variants are aliases of one scoring identity.
- `R129-P001/su1` is the Dutch EQ-5D-5L tariff by Versteegh et al., DOI `10.1016/j.jval.2016.01.003`.

## Compounds and type repairs

Keep these eight items as one workflow or one method identity: the database-plus-citation search and dual-screening workflow in `C50-P028`; the specified cluster bootstrap in `C50-P032`; integrated inductive and deductive thematic analysis in `CAL-B03`; the descriptive-statistics bundle in `R129-P014`; the researcher-and-advisor consultation in `R129-P018`; the 5L/3L relative-efficiency ratio in `R129-P064`; and the street, house, and birthday household-selection procedure in `R129-P110`.

Split or replace these five items:

- `C50-P045/mu4`: split the four quality controls when the source identifies each control.
- `R129-P038/mo2`: split the dimension-, construct-, and instrument-level models.
- `R129-P049/mu4`: remove the compound method item and retain the separate univariate and multivariable censored models.
- `R129-P110/mu4`: split Welch's t-test and ANOVA.
- `R129-P129/mu2`: split response distributions, ceiling/floor effects, and missingness analysis.

Hold `R129-P001/mu2` (`non-parametric method`), `R129-P001/mu3` (`direct method`), and `R129-P014/pr1` (`common standardized protocol`) as unmapped until the label has enough source context.

Repair four item types: move `CAL-B12/mu3` CFA to `ModelUse`; move `R129-P064/mu1` level-sum score to `ScoringUse`; move `R129-P090/mu7` better-than-dead to a concept or task condition; and merge or move `R129-P129/mu6` VAS regression into its existing `ModelUse` record.

## Normalization workflow

1. Keep `source_label` unchanged in every record.
2. Match exact registry IDs first. Apply aliases only after entity type and variant checks.
3. If only the family matches, create or queue an exact child. Do not force the base ID.
4. Split queryable compounds. Keep true integrated workflows as one source-scoped identity and store their normalized family.
5. Send unresolved labels to `UNMAPPED_VALUE` with the proposed type and reason.
6. Let a second strong model review only proposed new global identities, cross-record merges, and type changes. This review must use the source locator.
7. Add accepted identities to the registry. Revalidate records. Report remaining nulls and any one-to-many alias collision.

## Sample-stage decision

**ACCEPT `PLANNED_TARGET`.** Use it only for a count that the protocol explicitly intends to recruit, enroll, complete, or analyze before that stage occurs. A power-analysis minimum is not a planned target unless the protocol adopts it as its operational target. Never convert a planned count to `COMPLETED` or `ANALYZED`.
