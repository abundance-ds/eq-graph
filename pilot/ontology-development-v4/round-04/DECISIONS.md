# Round 4 decisions

- Keep the current records, keys, and controlled values.
- Correct S058 to `METHODS_RESEARCH`.
- Correct C011 to `HEALTH_PREFERENCE_RESEARCH`.
- Keep S084 as `METHODS_RESEARCH`.
- Keep C004 as `POPULATION_REFERENCE_DESCRIPTION`.
- Map D005 and D013 to `METHODS_RESEARCH`.
- Do not add method evaluation or implementation functions. Use
  `CURRENT_STUDY_OBJECT` with the method's scientific function.
- Use `ECONOMIC_OR_BURDEN` for readmission or other reported resource use.
- A later unit check changes C008 to `HEALTH_PREFERENCE_RESEARCH`: the family
  classifies the planned Study, while protocol form is a Publication fact.
- Version 0.5 adds an ordered family decision table. It adds no record, key,
  or controlled value.
- The blind version-0.5 application matched 59 of 60 source-adjudicated
  families and found no new structure or gap.
- Do not add a paper-specific rule for C011. Freeze the structure as a
  production-calibration candidate and review primary-family close calls before
  aggregate use.
