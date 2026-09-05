export const SQL_SCHEMA = `
metadata(key, value)
projects(project_id, title, abstract, principal_investigator, working_group,
         start_year, end_year, status, approved_budget_eur)
publications(publication_id, title, doi, pmid, pmcid, publication_year,
             publication_date, journal, publisher, volume, issue, article_number,
             article_type, language, keywords, funding_statement, abstract,
             canonical_url, licence_url, open_access, assessment_disposition,
             euroqol_connection, euroqol_support, support_scope, full_text_format)
studies(study_id, publication_id, label, study_ordinal, execution_status, source_status)
project_publications(project_id, publication_id)
people(person_id, display_name, family_name, given_names, orcid, openalex_id,
       entity_kind, identity_status)
person_names(person_id, name, name_type)
person_identifiers(person_id, scheme, value)
euroqol_memberships(person_id, member_id, affiliation, profile_url,
                     observed_date, status)
project_people(project_id, person_id, role)
publication_authors(publication_id, person_id, author_name, author_order,
                    corresponding, orcid, resolution_method, resolution_status)
coauthor_edges(source_id, source, target_id, target, weight)
author_affiliations(publication_id, person_id, affiliation)
publication_citations(publication_id, source, source_work_id, cited_by_count,
                      retrieved_at, source_updated_at, match_status)
publication_citation_years(publication_id, source, year, cited_by_count)
study_types(study_id, study_type, status)
research_purposes(study_id, purpose)
study_parts(part_id, study_id, label)
design_axes(design_id, study_id, part_id, axis, value)
populations(study_id, population, role, geography, size, details_json)
samples(sample_id, study_id, label, sample_size, role, geography, details_json)
study_countries(study_id, country)
concepts(study_id, concept)
outcomes(outcome_id, study_id, outcome)
findings(finding_id, study_id, publication_id, statement, outcome, details_json)
limitations(limitation_id, study_id, publication_id, statement, impact, scope, details_json)
research_products(product_id, study_id, product, product_type, status, details_json)
dataset_uses(dataset_use_id, study_id, dataset, role, details_json)
source_conflicts(conflict_id, study_id, statement, details_json)
registry_entities(registry_id, entity_type, canonical_label, parent_registry_id,
                  applies_to_registry_id, variant_kind, language_code,
                  jurisdiction, version, respondent_form, source_identifier,
                  scope)
scientific_uses(use_id, study_id, part_id, use_type, source_label,
                canonical_label, registry_id, context, function, analytic_role,
                details_json)
scoring_uses(scoring_use_id, study_id, part_id, source_label, registry_id,
             context, instrument_use_id, product_id, details_json)
administrations(administration_id, study_id, part_id, respondent, perspective,
                completion, assistance, channel, setting, instrument_language,
                interview_language, recall_period, time_point)
administration_targets(administration_id, target_use_id)
task_designs(task_id, study_id, part_id, label, duration, alternatives,
             task_count, block, task_order, randomization_unit, stopping_rule,
             profiles_json, attributes_json, levels_json, targets_json)
study_factors(factor_id, study_id, part_id, label, role, levels_json)
stakeholder_involvements(involvement_id, study_id, part_id, stakeholder_group,
                         activity, stage, role, influence)
outcome_details(outcome_id, study_id, family, label, instrument_use_ids_json)
finding_values(finding_id, ordinal, reported_value, unit, denominator, time,
               subgroup, comparator, direction, uncertainty)
interpretations(interpretation_id, study_id, publication_id, statement,
                finding_ids_json)
product_states(state_id, product_id, axis, exact_state, assertion_date, asserted_by)
extraction_gaps(gap_id, study_id, state, affected_type, affected_key,
                importance, proposed_resolution)
`.trim();
