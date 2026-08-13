# Reproduce current pilot

```sh
python pipeline/pilot_2_0.py sources
python pipeline/pilot_2_0.py profile-input
python pipeline/run_codex_eval.py profile-verification

python pipeline/pilot_2_0.py pubmed-v2
python pipeline/pilot_2_0.py pubmed-v2-profile-input
python pipeline/run_codex_eval.py pubmed-v2-profile-verification

python pipeline/pilot_2_0.py aggregate
python pipeline/resolve_eligibility.py
python pipeline/enrich_abstracts.py
python pipeline/person_funnel.py
python pipeline/validate_screening_corpus.py

python pipeline/prepare_screening_pilot.py --version v3 --prompt-version v3 --batches 3 --sample random
python pipeline/run_screening_pilot.py --version v3
python pipeline/evaluate_screening.py --version v3

python pipeline/prepare_screening_pilot.py --version v3-boundary --prompt-version v3 --batches 1 --sample boundary
python pipeline/run_screening_pilot.py --version v3-boundary
python pipeline/evaluate_screening.py --version v3-boundary

python pipeline/prepare_screening_pilot.py --version final --prompt-version v3 --sample full
python pipeline/run_screening_pilot.py --version final
python pipeline/validate_screening_results.py

python pipeline/retrieve_fulltexts.py
python pipeline/prepare_fulltext_assessment.py --output-version v1-sample --sample 12
python pipeline/run_fulltext_assessment.py --version v1-sample
python pipeline/prepare_fulltext_assessment.py --output-version v1-final --sample 0
python pipeline/run_fulltext_assessment.py --version v1-final

python pipeline/prepare_funding_audit.py
python pipeline/run_funding_audit.py
python pipeline/validate_fulltext_assessment.py
python pipeline/prepare_project_assessment_v2.py --version v3
python pipeline/run_project_assessment_v2.py --version v3
python pipeline/evaluate_project_candidate_audit.py
python pipeline/validate_pilot_2_0.py

python pipeline/prepare_scale_inputs.py
# Load OPENALEX_API_KEY before the next command when profiles are missing.
python pipeline/retrieve_scale_profiles.py
python pipeline/prepare_scale_inputs.py
python pipeline/prepare_profile_qa.py
python pipeline/run_profile_qa.py
python pipeline/evaluate_profile_qa.py
python pipeline/prepare_scale_discovery.py
python pipeline/retrieve_scale_identifier_sources.py
python pipeline/prepare_scale_source_union.py
python pipeline/validate_scale_source_union.py
python pipeline/enrich_scale_abstracts.py
python pipeline/validate_scale_abstract_enrichment.py
python pipeline/prepare_scale_screening.py --version v1 --validation
python pipeline/run_screening_pilot.py --version v1 --screen-dir scale/protocol-2.0/screening-v1-validation --workers 2
python pipeline/evaluate_screening.py --version v1 --screen-dir scale/protocol-2.0/screening-v1-validation
python pipeline/prepare_scale_screening.py --version v1
# Resume the complete production screen after the recorded 60-record check.
python pipeline/run_screening_pilot.py --version v1 --screen-dir scale/protocol-2.0/screening-v1 --workers 2 --resume
python pipeline/collect_scale_screening.py
python pipeline/prepare_scale_exclusion_audit.py --version v1 --seed 20260805
# A blinded reviewer submits all five exclusion-audit batches before evaluation.
python pipeline/evaluate_scale_exclusion_audit.py --version v1
# Audit v2 uses only fresh exclusions from the 6,000-record checkpoint.
python pipeline/prepare_scale_exclusion_audit.py --version v2 --seed 2026080502
# A fresh blinded reviewer submits all five v2 batches before evaluation.
python pipeline/evaluate_scale_exclusion_audit.py --version v2
python pipeline/evaluate_funding_metadata_route.py
```

- Existing network responses are reused from `raw/`.
- Abstracts are source text; never AI-generated.
- Preparation commands stop if their versioned output exists. This protects frozen
  selections and prompts. Use a new version name for a new run.
- The full-text retrieval command is safe to resume and uses saved per-record attempts.
- `paper-assessment.csv` marks unavailable full texts as
  `not_assessed_fulltext_unavailable`.
- Scale-up includes only profiles with a binary `accept` decision. All other profiles
  remain outside the author route.
- OpenAlex funding metadata is a discovery signal and needs full-text confirmation.
- Scale PubMed discovery uses exact accepted ORCID IDs. It does not use author names.
- Scale screening inputs contain the full stored abstract text. They are not truncated.
- Historical failed attempts remain under `audit/` and `screening-v2/`.
- Pause state on 2026-08-05: the scale screen is complete. Do not run scale full-text
  retrieval until the independent human check and held identity queue are resolved.
- Restart from `scale/protocol-2.0/PAUSE_2026-08-05.md`.
