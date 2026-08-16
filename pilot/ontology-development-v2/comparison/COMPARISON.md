# Anonymous semantic granularity comparison

## Executive summary

The three candidates support a paper-first EuroQol research ontology. Each candidate can represent the paper, local study components, instrument roles, methods, products, findings, reuse, and uncertainty. Each candidate also supports the 40 supplied paper applications. The main differences concern the boundaries between related study families, the separation of evidence-provider roles, the structure of administration and preference tasks, the treatment of assessment classes, and the dimensions of product status.

The frozen probes show that all three candidates can make the main distinctions that the focused questions require. Some boundaries still create ambiguous broad matches. Candidate 1 combines some study families and combines intended population with decision context. It does not give product access a separate structured axis. Candidate 2 separates more study families and uses independent product-state axes, but its broad `methods study` tag and its use of a protocol tag for an operational infrastructure paper can widen retrieval. Candidate 3 adds an assessment-class layer, response-label provenance, and harmonization relations, but some combined family labels, a generic `tested` product state, and an inconsistent protocol treatment can widen retrieval.

The source checks also show that conflict capture is not exhaustive in any candidate. The candidates identify different conflicts in the same 40-paper corpus. A later harmonization process must therefore preserve source statements and extraction uncertainty as first-class records. It must not depend on a single narrative conflict list.

This comparison does not select a candidate and does not make a merged ontology proposal.

## Semantic crosswalk and boundary differences

### Crosswalk

| Semantic function | Candidate 1 | Candidate 2 | Candidate 3 | Material boundary difference |
|---|---|---|---|---|
| Paper record | `Paper` | paper record | paper record | No material difference. |
| Paper-local unit | `Study Component` | study component | paper component | All three prevent a multi-phase paper from receiving one undifferentiated status or method. |
| Conditions and arms | `Study Condition` | experimental arm and assigned factors | component and comparison conditions | Names differ. Each can separate samples, modes, tasks, and analysis conditions. |
| Study family | controlled `Study Family` | study-family tag | controlled study family | Candidate 2 separates health-state valuation from value-set development and translation from cultural adaptation. Candidates 1 and 3 combine valuation with value-set development. Candidate 1 also combines translation with cultural adaptation. |
| Protocol treatment | protocol/design family is available, with component status | `study protocol` is a family tag and component status is separate | core guidance treats protocol as execution status, but one application also uses `protocol or research infrastructure` as a family | The boundary affects retrieval of planned protocol work versus completed infrastructure work. |
| Evidence source | `Evidence Supplier` | `Evidence Supplier` and respondent | evidence provider or respondent | Candidate 2 names supplier and respondent separately. Candidates 1 and 3 can describe the same distinction through linked administration and provider records. |
| Referent | `Referent` | referent | referent | No material difference. All can separate the person who answers from the person whose health is described. |
| Intended use context | `Intended Population or Decision Context` | target population and decision context | target population and decision context | Candidate 1 puts two query axes in one concept. This can be ambiguous when both axes are present. |
| Instrument role | `Instrument Involvement` | instrument-use role | instrument involvement | All distinguish target, administered measure, comparator, source, scoring input, and product roles. |
| Instrument identity | family, version, variant, locale, language, form, and component detail | family, version, variant, language, locale, form, and role | family, version, configuration, language, locale, form, component, and role | Candidate 3 makes bolt-on and instrument configuration especially explicit. All can keep article language separate from instrument language. |
| Administration | `Administration Event` plus separate support | orthogonal bundle for perspective, contact, medium, support, setting, and platform | multi-axis administration record | Candidate 1 separates mode and support. Candidate 2 makes the full bundle explicit. Candidate 3 also uses several independent axes. |
| Preference task | `Valuation Task Use` plus specialized preference profiles | task form plus inferential purpose | elicitation task plus assessment class | Candidate 1 has separate profiles for valuation, distributional preference, instrument-structure preference, and preference architecture. Candidate 2 makes task form and inferential purpose explicit. Candidate 3 places the task under a broader assessment-class system. |
| Analysis purpose | `Method Use` and specialized method profiles | method path with purpose and inference type | analysis method with assessment target and purpose | All avoid a method-name-only record. |
| Assessment and property | measurement-property and related specialized profiles | measurement property, with content validity under the measurement-property family | assessment class first, then property or criterion | Candidate 3 distinguishes measurement property, instrument-development criterion, valuation or mapping performance, survey quality, and implementation outcome before it records the exact property. This reduces false equivalence between unlike assessments. |
| Outcome and scoring | outcome specification, derivation, and product provenance | score-construction path | score representation, scoring relation, and provenance | All can keep direct responses, utilities, mapped utilities, QALYs, and modeled results separate. Candidate 3 also records response-label semantics. |
| Comparison | comparison axes and conditions | comparison record | comparison plus harmonization or calibration relation | Candidate 3 gives harmonization and calibration a named relation. The other candidates express these through comparison and provenance. |
| Product type and role | product and product provenance | product kind and role | product kind and output role | No material difference for named outputs. |
| Product state | status, exact evidence, governance, derivation, and documented use or effect | development state, exact evidence state, governance, access, recommendation or use, and implementation | maturity, access, output role, and supporting evidence | Candidate 2 makes each state axis independent. Candidate 1 has several independent axes but no separate access axis. Candidate 3 has access, but its generic `tested` maturity value needs the supporting evidence record to show what was tested. |
| Findings and attribution | finding, author interpretation, implication, limitation, gap, documented use or effect, and extractor observation | principal finding, interpretation, limitation, implication, use, and extraction note | attributed finding, interpretation, limitation, implication, use, future work, and extraction note | All can prevent proposed impact from becoming observed impact. Candidate 1 makes analytic uncertainty and extraction uncertainty separate named records. |
| Reuse and dependency | evidence reuse and product provenance | reuse, overlap, and dependency | reuse, harmonization, overlap, and dependency | All can trace paper groups. Candidates 2 and 3 make overlap confidence or harmonization more explicit. |
| Uncertainty and source conflict | analytic uncertainty, extraction uncertainty, and source conflict | material uncertainty path and typed source conflict | uncertainty, limitation, and typed extraction issue | Each candidate keeps source conflict separate from author conclusion. Their application records identify different conflicts, so the extraction method remains material. |

### Broad labels and false-combination risk

Candidate 1 uses a combined `valuation and value-set development` family. A family-only query can therefore return method work, task work, and completed value-set work together. Its task, product, and component records can resolve the difference, but the user must use them. Its combined `translation/cultural adaptation` family has the same effect. The Arabic translation paper and the Singapore English adaptation paper remain distinguishable through process and language records, but not through the broad family label alone.

Candidate 2 separates those valuation, value-set, translation, and adaptation families. Its `methods study` family is broad. Exact method paths resolve it, but a family-only query can combine work on very different methods. Its paper-level `mixed` status can help describe a paper with completed and planned components, but component status already carries the actionable distinction. The 40-paper set does not establish whether both status levels are necessary for retrieval.

Candidate 3 also combines valuation with value-set development. It combines qualitative concept work with content-validity work in one family and uses a broad `implementation or use study` family. Its assessment class and exact method records resolve many of these combinations. Its generic product maturity value `tested` can combine cognitive testing, psychometric testing, mock workflow testing, and other evidence unless the query also uses the evidence record.

### Fine distinctions and retrieval value

The fine distinctions in each candidate usually add retrieval value because they prevent a known false combination in the 40 applications.

- Separate task form and inferential purpose prevent standard DCE, DCE with duration, social-priority DCE, and descriptive-system preference work from becoming one method result.
- Separate respondent, referent, reporting perspective, target population, and decision context prevent adult valuation of a child's hypothetical health from becoming proxy reporting about an observed child.
- Separate instrument role prevents a survey topic, a comparator, a mapping source, and a produced instrument from becoming equivalent uses.
- Separate assessment class prevents psychometric validity evidence, mapping performance, survey quality control, and implementation feasibility from becoming one broad quality result.
- Separate product evidence, governance, access, recommendation, use, and implementation prevent a named output from receiving one broad completion label.
- Separate finding, interpretation, limitation, implication, documented use, and extractor inference prevent expected impact from becoming observed impact.

Some distinctions remain alternatives rather than established requirements. The applications do not show that paper-level `mixed` status adds a stable query result beyond component statuses. They also do not show whether an assessment-class parent must be explicit or can be derived from typed property and method records. These alternatives need later evaluation with the same paper applications.

### Terminology-only and representation-form differences

Several differences need only a terminology crosswalk. `Study Component`, study component, and paper component have the same paper-local function. `Evidence Supplier` and evidence provider are equivalent when the respondent relation is also present. `Instrument Involvement` and instrument-use role are equivalent. Outcome derivation, score-construction path, and scoring relation cover the same provenance function at this comparison level. Principal finding, finding summary, author interpretation, limitation, implication, documented use, and future-work records also have direct counterparts across the candidates.

The candidates differ in how they declare these facts. Candidate 1 often uses a controlled type plus a specialized structured profile. Candidate 2 often uses an explicit relation with orthogonal structured values. Candidate 3 labels each item as controlled, repeatable, relational, or narrative. These are not semantic differences when the value and relation have the same scope. They become material only when one form changes filtering. Examples include Candidate 1's combined intended-population or decision-context concept, Candidate 3's generic `tested` value, and any candidate application that leaves a conflict only in narrative text.

## Focused user-question findings

Legend: **P** = the candidate can answer precisely from its structured records and linked application text. **A** = the candidate can answer, but a boundary can make the result ambiguous without an additional narrative or filter. **N** = the candidate cannot answer from the proposed record.

| No. | Focused question, abbreviated | Candidate 1 | Candidate 2 | Candidate 3 | Comparison note |
|---:|---|:---:|:---:|:---:|---|
| 1 | Aim and contributions | P | P | P | All separate aim, contribution, and product or finding. |
| 2 | Concepts, frameworks, and topics | P | P | P | All retain structured topics plus narrative scope. |
| 3 | Instruments developed, adapted, used, scored, compared, or produced | P | P | P | Instrument-role records support the distinction. |
| 4 | Exact family, version, variant, and language | P | P | P | All retain these identity axes. |
| 5 | Phases, samples, tasks, analyses, and relations | P | P | P | Paper-local components and relations support the answer. |
| 6 | Supplier, referent, intended population, and decision context | A | P | P | Candidate 1 combines intended population with decision context. Its application text can resolve a case, but the controlled boundary does not keep the axes independent. |
| 7 | Geography, language, condition, age, care, and policy setting | P | P | P | All retain these scopes. |
| 8 | Selection, recruitment, exclusions, and stage counts | P | P | P | All support stage-specific population flow and source conflict. |
| 9 | Design and detailed domain method | P | P | P | All link methods to components and purposes. |
| 10 | Valuation task, protocol, and framing | P | P | P | The specialized task structures give exact answers. |
| 11 | Administration mode and perspective | P | P | P | All use multiple administration axes. |
| 12 | Statistical, scoring, mapping, psychometric, and qualitative method purpose | P | P | P | All connect method to purpose and inference. |
| 13 | Comparisons and material condition differences | P | P | P | All support typed comparison axes. |
| 14 | Products, stages, and remaining steps | P | P | P | Candidate 3 needs the supporting evidence record when `tested` is used. The application text supplies it. |
| 15 | Principal findings and interpretation | P | P | P | All keep summary findings separate from estimates and interpretation. |
| 16 | Limitations, uncertainty, conflicts, and transfer limits | P | P | P | The structures support the answer. Conflict detection differs by application, as Probe 13 shows. |
| 17 | Implications, actual use, and actual effect | P | P | P | All separate stated implication from documented use or effect. |
| 18 | Future work and gaps | P | P | P | All attribute future work to the paper. |
| 19 | Reused sample, data, protocol, value set, mapping, or model | P | P | P | All support reuse and provenance. |
| 20 | Combined cross-corpus filter | A | P | P | Candidate 1's combined intended-population or decision-context concept can require a second text check. Other filter axes are precise. |
| 21 | Method differences by study family | P | P | P | Each candidate can combine family, component, method, task, and purpose. |
| 22 | Corpus findings about a specified subject | P | P | P | All support subject, finding, comparison, and attribution. |
| 23 | Products and reported maturity | P | P | P | Candidate 1 cannot add access as an independent product filter. Candidate 3 needs evidence detail to interpret `tested`. Neither issue prevents the stated maturity answer. |
| 24 | Studied populations, places, languages, settings, and modes | P | P | P | All support these axes. |
| 25 | Independent versus reused evidence | P | P | P | All trace reuse. Candidates 2 and 3 state overlap confidence more explicitly. |
| 26 | Change over time | P | P | P | The semantic records can be combined with the supplied deterministic date layer. |
| 27 | Corpus-bounded absent or weak combinations | P | P | P | The answer must be derived from populated records and marked as corpus-bounded. |

No focused question receives **N**. This does not mean that every answer is a single-field lookup. The questions about methods, products, implications, and gaps require joins across component, role, status, and attribution records.

## Frozen retrieval and comparison probes

### Probe 1: DCE with duration

The focal applications are `10.1016/j.jval.2024.05.016` and `10.1177/0272989x251325828`. All three candidates retrieve them as DCE-with-duration work and distinguish them from standard DCE, cTTO, PTO, and EQ VAS work. Candidate 1 uses a valuation-task profile and valuation-model purpose. Candidate 2 uses task form plus inferential purpose. Candidate 3 uses elicitation task plus assessment class. The applications preserve the split or triplet duration design and its anchoring purpose. No focal miss or false match was found. The practical effect is that a standard-DCE paper does not enter the result only because it contains `DCE`.

### Probe 2: Unsupervised online versus supervised face-to-face cTTO

All three candidates retrieve `10.1007/s11136-020-02712-1`. They distinguish online unsupervised administration from interviewer-supported face-to-face administration, including contact medium, support, setting, platform, and recruitment differences. Candidate 1 uses administration event plus support. Candidate 2 uses an orthogonal administration bundle. Candidate 3 uses a multi-axis administration record. All avoid a direct causal statement based on mode alone. A source check found an abstract range with a lower bound of 0.600 and a main-results lower bound of 0.446. Candidate 3 records this conflict. Candidates 1 and 2 report the abstract range without the conflict. The practical effect is that mode retrieval is precise, but the exact range is ambiguous in two applications.

### Probe 3: Translation and language adaptation

All three candidates retrieve `10.1186/s41687-025-00985-z` and `10.1186/s12955-024-02290-7`. They keep article language, instrument language, and study country separate. The first application records translation from UK English to Modern Standard Arabic for use in Egypt, with forward translation, back translation, cognitive interviews, and a transfer limit for use in other Arabic-speaking countries. The second records intralingual adaptation from UK English to Singapore English, local expert review, cognitive debriefing, and separate content-validity work. Candidate 2 and Candidate 3 separate translation from cultural adaptation at the family level. Candidate 1 needs the process filter because its family label combines them. The practical effect is that a search for translation alone can be broad in Candidate 1, while all three can still give a precise paper explanation.

### Probe 4: Adult, proxy, caregiver, and other-person evidence

All three candidates distinguish the three focal cases. In `10.1007/s40273-022-01216-9`, adults value hypothetical health for a 10-year-old child; this is not proxy reporting about an observed child. In `10.1007/s11136-025-04150-3`, experts advise on future proxy use; this is not observed proxy administration. In `10.1186/s12955-022-01996-w`, caregivers use proxy version 1 to rate a child, and children complete independent self-report records. Candidate 1 can represent the roles but combines intended population with decision context. Candidates 2 and 3 keep these axes independent. No false conversion from valuation to proxy report was found. The practical effect is that the evidence provider, referent, perspective, and intended use remain distinct.

### Probe 5: Instrument roles

All three candidates distinguish instrument roles in the applications. For example, one paper can use EQ-5D as the target of valuation and as an administered measure, while an older version or crosswalk is a comparator or scoring input. The EQ-HWB development application treats its framework, codebook, target instrument, and produced output as different roles. The dialysis mapping application treats SF-12 as a mapping source, EQ-5D-3L utilities as mapped outputs, directly collected EQ-5D-5L as observed evidence, and SF-6D as a comparator. Papers that list survey topics do not become administration records. No role-level miss was found. The practical effect is that an instrument mention does not imply administration, production, or scoring.

### Probe 6: Graves' disease measurement properties

All three candidates retrieve `10.1186/s12955-023-02177-z` and keep ceiling effects, convergent validity, test-retest reliability, and responsiveness separate. They preserve different results for worsening and improvement instead of assigning one validity label. Candidate 1 also records an effect-size label issue. Candidate 3 states that the stability anchor procedure is not fully described. The source states that the stable group had self-reported unchanged health between baseline and one month, but it does not give a full administration description for that item. Candidate 3's note is therefore a procedural caution, not a contradiction of the reported anchor. The practical effect is that support for one property does not become support for all properties.

### Probe 7: Mapping to QALYs and cost-effectiveness

All three candidates retrieve `10.1007/s10198-018-0987-x`. They trace direct EQ-5D-5L responses and scoring, three direct mappings and two response mappings from SF-12 to EQ-5D-3L utility, SF-6D derivation, then QALYs and ICERs in two Markov models. They keep observed utility, mapped utility, modeled QALY, and modeled decision result separate. No focal miss was found. The practical effect is that a mapped utility does not become a directly observed EQ-5D response and an ICER does not become an instrument score.

### Probe 8: Full valuation method trace

For `10.1007/s40258-021-00639-3`, all three candidates record the EQ-VT 2.1 protocol, interviewer-administered computer-assisted personal interviews, ten cTTO states, seven duration-free DCE pairs, blocked health-state designs, and selection of a heteroscedastic censored hybrid model to create the Danish value set. For `10.1016/j.jval.2025.01.003`, they record EQ-VT, interviewer-administered face-to-face or online interviews in Arabic or English, ten cTTO states, seven standard DCE pairs, and a hybrid Tobit model censored at -1.0 with a heteroskedasticity correction for the UAE value set. Candidate 1 expresses this through valuation task and model profiles. Candidate 2 uses protocol, task, design, mode, and inferential purpose. Candidate 3 uses task, administration, assessment, and product provenance. No focal miss was found. The practical effect is that model purpose and task design remain linked to the correct value-set product.

### Probe 9: Planned, operational, and completed products

All three candidates distinguish the focal outputs when component and product status are used. `10.1136/bmjopen-2025-100897` is a planned two-wave DCE protocol. It contains wave-1 survey materials, design, an analysis plan, and pilot evidence, but it does not report the planned main findings. `10.1007/s11136-025-03983-2` describes operational EQ-DAPHNIE infrastructure with a completed pilot and two completed country rounds, plus planned expansion. `10.1186/s12955-024-02266-7` reports a completed and selected national value set. Candidate 1 keeps the infrastructure paper out of a broad protocol family and uses component status. Candidates 2 and 3 also apply a protocol label to the infrastructure application, which can create a broad protocol match unless status and product filters are used. Candidates 2 and 3 record restricted EQ-DAPHNIE data access. Candidate 1 has no separate product-access axis. The practical effect is that one broad completion label is insufficient.

### Probe 10: Principal finding and author attribution

All three candidates retrieve a concise principal finding, author interpretation, limitation, and future work for `10.1007/s11136-025-04074-y` and `10.1007/s11136-025-03996-x`. The first application describes EQ-DAPHNIE quality controls, country variation, threshold decisions, and future method work without returning every country estimate. The second describes a co-designed P-PROM ROCK prototype, its resources and mock optimization, its limitations, and the planned Phase 3 pilot and evaluation. It does not claim routine clinical implementation or an observed clinical effect. No focal miss was found. The practical effect is that retrieval returns an attributed research summary rather than an estimate dump.

### Probe 11: Implication, documented use, and extractor inference

All three candidates provide separate records for author-reported implications, documented use or effect, and extractor inference. Candidate 1 names `Author Implication`, `Documented Use/Effect`, and `Extractor Observation`. Candidates 2 and 3 use equivalent attributed layers. The P-PROM ROCK paper illustrates the distinction: the authors propose and prepare a program for routine care, but the paper reports co-design and mock optimization, not routine implementation or patient effect. No false observed impact was found after the status filters were applied. The practical effect is that expected or proposed benefit is not presented as an observed effect.

### Probe 12: Reuse and extension

All three candidates trace the Trinidad and Tobago group and the EQ-DAPHNIE group. In the Trinidad and Tobago group, the applications separate the primary EQ-VT sample and value-set product, reused EQ-VT data with a new independent DCE-with-duration sample, reused DCE-with-duration data with an independent cTTO benchmark, and later pooled or rescored analyses. In the EQ-DAPHNIE group, they separate the infrastructure paper, the quality-control paper that reuses pilot and main-study data, and the paper that reuses an eight-country subset. Candidates 2 and 3 make overlap confidence or harmonization more explicit. Candidate 1 expresses the same lineage through reuse and provenance. No group-level miss was found. The practical effect is that a new analysis does not become independent evidence merely because it appears in a new paper.

### Probe 13: Conflicts, unclear procedures, and transfer limits

All three candidates have a suitable source-conflict and extraction-uncertainty structure, but their populated applications find different issues.

- Candidates 1 and 2 record the Trinidad and Tobago value-set conflict between 236 and 275 negative health-state values. Candidate 3 does not record it.
- Candidates 2 and 3 record the EQ-DAPHNIE review count conflict between 889 reported records and component counts of 496 plus 397, which total 893. Candidate 1 does not record it.
- Candidate 3 records the DIF reference or focal-group conflict and the online cTTO range conflict. Candidates 1 and 2 do not record them.
- Candidate 3 records the Graves stability-anchor procedure as unclear. The source gives a self-reported unchanged-health anchor, so the remaining issue is the exact administration procedure, not the existence of an anchor.
- All candidates retain transfer limits for language, country, population, mode, and reused evidence when the application states them.

The practical effect is that no application set provides exhaustive conflict capture. The final system must retain the exact competing source statements and the extractor's uncertainty separately from the authors' conclusions.

### Probe 14: Corpus-bounded gap

The applications support this derived gap: none of the 40 papers reports observed administration of an EQ-5D-Y-family instrument with proxy perspective 2. The proxy psychometric paper uses proxy version 1. Another application states that version 1 is available but does not provide an observed version-2 count. The implementation workflow paper concerns planned future proxy handling rather than observed version-2 administration. Candidates 2 and 3 state this gap explicitly. Candidate 1 provides the role and perspective records from which it can be derived, but it does not state the gap in its corpus summary. The practical effect is a precise corpus audit. The result must not be presented as an absence from all EuroQol research.

## Candidate-specific strengths and failure modes

### Candidate 1

Strengths:

- It gives detailed profiles to valuation tasks, preference architecture, distributional preference, instrument-structure preference, valuation models, survey quality, cost burden, measurement properties, and implementation.
- It makes analytic uncertainty and extraction uncertainty separate.
- It has explicit finding, interpretation, implication, documented-use, and extractor-observation layers.
- It uses several independent product-state dimensions and does not force all products onto one maturity ladder.
- Its infrastructure application keeps completed operations separate from a protocol family.

Failure modes:

- Combined valuation or value-set and translation or adaptation families can widen family-only retrieval.
- The combined intended-population or decision-context concept can make a joint context query ambiguous.
- Product access is not a separate structured dimension. Restricted access in the EQ-DAPHNIE source is therefore not available as a direct product filter.
- Its applications do not record the EQ-DAPHNIE review-count conflict, the DIF reference or focal-group conflict, or the online cTTO range conflict.

### Candidate 2

Strengths:

- It separates health-state valuation from value-set development, translation from cultural adaptation, population-health work from norm work, and target population from decision context.
- Its administration bundle uses independent perspective, contact, medium, support, setting, and platform axes.
- It separates preference task form from inferential purpose.
- Its product records use independent development, evidence, governance, access, recommendation or use, and implementation axes.
- It has explicit source-conflict types and clear reuse or overlap records.

Failure modes:

- The `methods study` family remains broad and depends on exact method-path filters.
- Paper-level `mixed` status can duplicate information in component statuses and can hide which component is complete.
- The infrastructure application also receives a protocol tag. A protocol-family query can therefore return an operational resource unless it also uses component or product status.
- Its applications do not record the DIF reference or focal-group conflict or the online cTTO range conflict.

### Candidate 3

Strengths:

- It places assessment class before the exact property or criterion. This separates measurement properties, instrument-development criteria, valuation or mapping performance, survey quality, and implementation outcomes.
- It makes instrument configuration explicit for bolt-ons and variants.
- It records response-label semantics as part of mapping and scoring provenance.
- It gives harmonization and calibration named relations.
- It records product access and detects source conflicts that the other applications do not record.

Failure modes:

- Combined valuation or value-set, qualitative concept or content-validity, and implementation or use families can widen family-only retrieval.
- The generic `tested` product-maturity value is ambiguous without the linked evidence record.
- Its core guidance treats protocol as execution status, but the infrastructure application also uses protocol as a family. This internal boundary inconsistency can create false protocol matches.
- Its applications do not record the Trinidad and Tobago negative-value count conflict.
- Its Graves anchor note can be read too broadly. The source gives the unchanged-health anchor but not the full item administration procedure.

## Requirements and unresolved alternatives for later harmonization

### Requirements that all three candidates support

A later harmonization process must preserve these capabilities:

1. Keep the paper as the main research object, with paper-local components for phases, samples, tasks, analyses, and products.
2. Give each component its own execution status and relations to other components.
3. Keep evidence provider, respondent, referent, reporting perspective, target population, and decision context separate.
4. Keep instrument family, version, variant, configuration, language, locale, form, component, and role separate.
5. Represent administration with independent mode, contact, support, platform, setting, recruitment, and order axes when the source supplies them.
6. Keep preference-task form, inferential purpose, protocol, framing, health-state design, anchor, and time treatment separate.
7. Link each analysis method to its component, input, purpose, assessment target, inference type, and output.
8. Keep assessment class, exact property or criterion, subtype, target, direction, level, and result separate.
9. Preserve direct response, score, utility, mapped utility, QALY, modeled estimate, and decision result as different outcome types with complete provenance.
10. Record product kind, output role, exact supporting evidence, governance, access, recommendation, documented use, implementation, version, and time as independent facts.
11. Keep principal finding, estimate, author interpretation, author limitation, author implication, documented use or effect, future work, and extractor inference separate.
12. Trace sample, data, protocol, design, value set, mapping function, model, and product reuse, including overlap and dependency.
13. Keep analytic uncertainty, extraction uncertainty, source conflict, unclear procedure, and transfer limit separate. Preserve each competing source statement.
14. Mark derived gaps as corpus-bounded and keep them separate from author-reported gaps.

### Alternatives that remain unresolved in the 40-paper set

- Whether valuation and value-set development need separate study-family values or one family plus task and product filters.
- Whether translation and cultural adaptation need separate family values or one family plus explicit process stages.
- Whether protocol is a study family, an execution status, a product kind, or more than one of these with strict role rules.
- Whether paper-level `mixed` status is stored or derived from component statuses.
- Whether assessment class is an explicit parent concept or a derived group of exact properties and method purposes.
- Whether product maturity uses a controlled state list or is derived from independent evidence, governance, access, use, and implementation axes.
- Whether overlap confidence is controlled, narrative, or computed from the evidence lineage.
- How much review-level search and screening context belongs in the paper ontology instead of a linked evidence-synthesis layer.
- How a system validates conflict capture. The application records show that a schema can support conflict without ensuring that extraction finds every conflict.

The corpus also leaves several evidence alternatives open. It contains no observed proxy-perspective-2 administration in the selected papers, no completed results for the planned PTO work, no full uncertainty propagation across every mapping-to-decision chain, and limited observed routine implementation effects. These are corpus limits, not ontology conclusions.

## Source checks and limitations

The focused source checks used only the supplied local article files. They checked details that could change the probe result or distinguish candidate failure modes.

- `doi_10.1186_s12955-023-02177-z.md`: Graves properties and the self-reported unchanged-health stability anchor.
- `doi_10.1007_s11136-025-04003-z.md`: the DIF reference or focal-group conflict.
- `doi_10.1007_s11136-020-02688-y.md`: the review count of 889 versus 496 plus 397.
- `doi_10.1186_s12955-024-02266-7.md`: the Trinidad and Tobago negative-value count of 236 versus 275 and value-set status.
- `doi_10.1007_s11136-020-02712-1.md`: online versus face-to-face administration and the range conflict.
- `doi_10.1016_j.jval.2024.05.016.md` and `doi_10.1177_0272989x251325828.md`: DCE-with-duration task design and anchoring.
- `doi_10.1007_s40258-021-00639-3.md` and `doi_10.1016_j.jval.2025.01.003.md`: valuation protocol, task design, administration, model selection, and model purpose.
- `doi_10.1186_s41687-025-00985-z.md` and `doi_10.1186_s12955-024-02290-7.md`: translation versus intralingual adaptation, instrument language, country, process, and transfer limits.
- `doi_10.1186_s12955-022-01996-w.md`: proxy version 1, independent self-report, respondent, referent, and perspective.
- `doi_10.1007_s10198-018-0987-x.md`: direct and mapped utilities, QALYs, and ICERs.
- `doi_10.1136_bmjopen-2025-100897.md`: planned waves, available wave-1 materials, pilot evidence, and absent main findings.
- `doi_10.1007_s11136-025-03983-2.md`: completed EQ-DAPHNIE rounds, future expansion, and restricted data access.
- `doi_10.1007_s11136-025-04074-y.md`: quality-control procedures, thresholds, country variation, and future work.
- `doi_10.1007_s11136-025-03996-x.md`: co-designed prototype, mock optimization, and planned Phase 3 evaluation.

These checks did not re-extract every fact from all 40 articles. The comparison uses the complete candidate applications for the full corpus view and uses the local articles only for the focused checks above. No Internet source, external ontology source, database guidance, Git history, or holdout material was used.

## Run note

### Inputs read in full

- `AGENTS.md`
- `TASK.md`
- `context/PURPOSE.md`
- `context/USER_QUESTIONS.md`
- `context/PROTOCOL.md`
- `context/PROBES.md`
- `candidates/candidate-1.md`
- `candidates/candidate-2.md`
- `candidates/candidate-3.md`
- `batches/batch-01.tsv`
- `batches/batch-02.tsv`
- `batches/batch-03.tsv`
- `batches/batch-04.tsv`

### Local article inputs used for focused checks

- `corpus/333-RA/doi_10.1186_s12955-023-02177-z.md`
- `corpus/1811-RA/doi_10.1007_s11136-025-04003-z.md`
- `corpus/2016170/doi_10.1007_s11136-020-02688-y.md`
- `corpus/341-RA/doi_10.1186_s12955-024-02266-7.md`
- `corpus/2016470/doi_10.1007_s11136-020-02712-1.md`
- `corpus/341-RA/doi_10.1016_j.jval.2024.05.016.md`
- `corpus/341-RA/doi_10.1177_0272989x251325828.md`
- `corpus/20170400/doi_10.1007_s40258-021-00639-3.md`
- `corpus/1465-VS/doi_10.1016_j.jval.2025.01.003.md`
- `corpus/1492-RA/doi_10.1186_s41687-025-00985-z.md`
- `corpus/364-RA/doi_10.1186_s12955-024-02290-7.md`
- `corpus/20180140/doi_10.1186_s12955-022-01996-w.md`
- `corpus/20170450/doi_10.1007_s10198-018-0987-x.md`
- `corpus/1850-RA/doi_10.1136_bmjopen-2025-100897.md`
- `corpus/367-RA/doi_10.1007_s11136-025-03983-2.md`
- `corpus/367-RA/doi_10.1007_s11136-025-04074-y.md`
- `corpus/330-PHD/doi_10.1007_s11136-025-03996-x.md`

The article checks used targeted local text searches. They did not read unrelated corpus files.

### Mechanical issues

The first terminal rendering of Candidate 1 and Candidate 3 was clipped by the output limit. Each file was then read again in smaller line ranges through its end. Two broad article-search outputs were also clipped. The affected checks were repeated with narrower patterns and smaller source groups. No required candidate or context input remained partially read. The output directory was empty before this report was created. This run wrote only `output/anonymous-granularity-comparison.md` and made no commit.
