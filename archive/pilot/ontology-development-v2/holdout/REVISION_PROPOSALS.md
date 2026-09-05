# Revision proposals after holdout review

## Required revisions

None are justified by the ten holdout applications. No paper required a missing relation, an `other` family, or misuse of an existing controlled term. Two retrieval risks and two wording risks justify clarification only.

## Useful clarifications that do not change the ontology

### Clarify preference-scale mapping versus instrument mapping

- **Exact problem:** The family name **Mapping or scoring** can retrieve a DCE-to-cTTO scale transformation together with source-instrument-to-target-instrument mappings. A family-only result can therefore imply the wrong input and output.
- **Holdout evidence:** In `10.1007/s40273-022-01210-1`, mixed-logit DCE disutilities are transformed to the cTTO utility scale. No source PROM is mapped to a target PROM, and no QALY or cost-effectiveness result is calculated.
- **Question or probe consequence:** This affects focused question 21 and frozen probes 7 and 8. It can falsely match the paper to a mapped-utility economic evaluation.
- **Smallest change:** Add one sentence to the Mapping or scoring boundary. State that valuation-scale anchoring or transformation must retain its task-to-scale path, and that it must not be retrieved as instrument mapping or economic use unless those separate outputs exist.
- **Development concept changed or extended:** This clarifies the controlled study-family boundary and the existing valuation scale-construction and score-path guidance. It adds no concept.
- **Backward check:** Check prior applications that have both Value-set development and Mapping or scoring. Confirm the exact source, target, and output and remove any implied QALY or instrument mapping.
- **Complexity and consistency cost:** Low. The clarification reduces extraction variation but requires exact source-to-target paths in family-level queries.

### Clarify exact targets for response-process evidence

- **Exact problem:** The measurement-property list does not name recall-period interpretation, reporting-perspective adherence, or other response-process behavior. The open exact-target rule can represent them, but an extractor can incorrectly force them into content-validity comprehensibility or omit a stable retrieval phrase.
- **Holdout evidence:** `10.1007/s11136-026-04230-y` studies how dementia proxies use a seven-day recall period and how they combine two reporting perspectives. It does not develop a concept framework and does not present the work as a standard content-validity assessment. Cognitive interviews in `10.1186/s41687-024-00761-5` provide related response-process evidence during language work.
- **Question or probe consequence:** This affects focused questions 2, 9, and 12 and frozen probes 4 and 6. Queries for recall or perspective behavior can become wording-sensitive.
- **Smallest change:** State that the supported property list is not exhaustive. Give `response-process behavior`, `recall-period interpretation`, and `instruction or perspective adherence` as examples of exact assessment targets. Do not require a new property category and do not equate them automatically with content validity.
- **Development concept changed or extended:** This clarifies the Measurement-property study profile and the common method-use exact-target field.
- **Backward check:** Check prior think-aloud, cognitive-interview, and proxy-method applications for forced content-validity labels. Keep paper-local author terms where needed.
- **Complexity and consistency cost:** Low to moderate. The examples improve retrieval, but extractors must still avoid treating each response behavior as a new controlled property.

### Define proxy perspective labels in plain semantic terms

- **Exact problem:** `proxy perspective 1` and `proxy perspective 2` are stable labels only when the form convention is known. Papers also use terms such as proxy-person, proxy-patient, observed view, and inferred patient view. A number alone can be unclear across instrument families.
- **Holdout evidence:** `10.1007/s40271-025-00787-x` states an EQ-5D proxy form and perspective. `10.1007/s11136-026-04230-y` reports observed and inferred response behavior but does not state a numbered requested form. `10.1186/s41687-025-00928-8` and `10.1007/s11136-026-04223-x` do not report the requested perspective.
- **Question or probe consequence:** This affects focused questions 4, 6, and 11 and frozen probe 4. It can cause a false equivalence between requested perspective and the perspective that a respondent actually used.
- **Smallest change:** Add plain-language definitions for the two controlled proxy perspectives. Require the extractor to keep exact form identity, author wording, requested perspective, and observed response behavior separate. If the source gives none, keep `not reported`.
- **Development concept changed or extended:** This clarifies Reporting perspective and the proxy-evidence instructions. It adds no relation.
- **Backward check:** Check prior proxy applications for perspective values inferred only from a form number or from respondent behavior.
- **Complexity and consistency cost:** Low. The added wording increases clarity and prevents unsupported normalization.

### Clarify the evidence level of a documented effect

- **Exact problem:** A qualitative report that staff changed care behavior can be called a documented effect, but that phrase can also suggest a measured participant outcome. The present rule requires evidence but does not give an example of this difference.
- **Holdout evidence:** In `10.1007/s40271-025-00787-x`, staff reported that collection changed some care approaches. The pilot did not measure a resident-health effect or a scaled service effect.
- **Question or probe consequence:** This affects focused question 17 and frozen probe 11. A loose application can overstate implementation impact.
- **Smallest change:** Add an example that distinguishes a staff-reported practice response, an observed workflow change, and a measured participant or service outcome. Require the exact evidence provider and outcome level with each effect.
- **Development concept changed or extended:** This clarifies Documented effect and the implementation profile.
- **Backward check:** Check prior implementation applications for effects that are only expectations, recommendations, or participant reports.
- **Complexity and consistency cost:** Low. The clarification adds no field and makes impact claims more consistent.

## Rejected ideas

### Add a separate short-form product kind

- **Exact problem considered:** `10.1007/s11136-026-04223-x` produces QID-12, which is more specific than the broad product kind `instrument or version`.
- **Question or probe consequence:** A separate kind could make focused questions 14 and 23 more direct.
- **Reason rejected:** Product identity, item count, form, and development fact already identify a short form. One paper detail does not justify another controlled product kind.
- **Development concept that would change:** Product kinds.
- **Backward check if reconsidered:** All abbreviated, long, youth, adult, and proxy forms.
- **Complexity and consistency cost:** Moderate. It would create overlap between form attributes and product kinds.

### Add a separate family for proxy response-process studies

- **Exact problem considered:** `10.1007/s11136-026-04230-y` does not have a named controlled property for its qualitative response-behavior target.
- **Question or probe consequence:** A family could simplify focused question 2 and frozen probe 4.
- **Reason rejected:** The paper naturally fits Measurement-property study with an exact target and qualitative methods. A new family would classify a method and reporter type as a purpose and would overlap with content validity and survey methods.
- **Development concept that would change:** Controlled study families.
- **Backward check if reconsidered:** All cognitive-interview, proxy, content-validity, and survey-process papers.
- **Complexity and consistency cost:** High. Family assignment would become unstable.

### Add a `routine data` study family

- **Exact problem considered:** `10.3390/cancers16111952` reuses routine PROM data but is not an implementation study.
- **Question or probe consequence:** A family could appear useful for focused questions 9, 17, and 24.
- **Reason rejected:** Routine collection is an evidence-source and setting fact. The paper purpose is responsiveness assessment. A new family would mix provenance with purpose and create false implementation matches.
- **Development concept that would change:** Controlled study families and evidence-source representation.
- **Backward check if reconsidered:** All secondary analyses of clinical, registry, or routine PROM data.
- **Complexity and consistency cost:** High. It would duplicate existing execution, reuse, setting, and purpose fields.

### Treat each pooled estimate as a value-set or data product

- **Exact problem considered:** `10.1186/s12955-025-02421-8` produces pooled utility and EQ VAS estimates that can be used in economic work.
- **Question or probe consequence:** Product retrieval for focused question 23 could include these outputs.
- **Reason rejected:** The estimates are synthesis outcomes. They are not a scoring algorithm for all instrument profiles and are not a named data resource. Calling them a value set would be wrong.
- **Development concept that would change:** Product kinds and outcome-to-product boundary.
- **Backward check if reconsidered:** All evidence syntheses and modeled estimates.
- **Complexity and consistency cost:** High. It would inflate ordinary findings into products.

### Add a representativeness flag

- **Exact problem considered:** Several papers describe quota samples, underrepresented groups, or narrow sites.
- **Question or probe consequence:** A flag could simplify focused questions 8, 16, 20, and 24.
- **Reason rejected:** The candidate already preserves frame, recruitment, quotas, exclusions, flow, and transfer limits. One flag would remove the reasons and denominators that users need.
- **Development concept that would change:** Evidence and population context.
- **Backward check if reconsidered:** All primary and review samples.
- **Complexity and consistency cost:** High because a subjective binary value would replace structured evidence.

## Proposal-stage conclusion

The holdout evidence supports the frozen ontology without a required structural revision. The proposed wording clarifications address extraction consistency and false-match risk. They do not change the ten applications or add a controlled term.
