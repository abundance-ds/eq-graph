# Version 0.4 regression audit

The blind regression mapped all 60 studies but did not reproduce the reviewed
partition. Source checks found five wrong regression mappings and one wrong
review mapping.

| Study | Regression | Decision |
|---|---|---|
| G083 | `METHODS_RESEARCH` | Keep `HEALTH_ECONOMIC_EVALUATION`: the study compares dialysis costs, QALYs, and ICERs. |
| C004 | `HEALTH_OUTCOME_RESEARCH` | Keep `POPULATION_REFERENCE_DESCRIPTION`: population or reference data are a stated output. |
| C008 | `HEALTH_PREFERENCE_RESEARCH` | Accept: classify the planned Study, not the protocol Publication. |
| C012 | `MEASUREMENT_PROPERTY_EVALUATION` | Keep `INSTRUMENT_VERSION_DEVELOPMENT`: two new bolt-ons are principal outputs. |
| D006 | `METHODS_RESEARCH` | Keep `APPLIED_USE_RESEARCH`: PROM-supported readmission prediction and care support are primary. |
| D011 | `METHODS_RESEARCH` | Keep `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`: the paper classifies and applies 13 arguments. |

The regression's stability claim is rejected. Version 0.5 adds no family or
key. It makes the Study the classification unit and uses an ordered family
decision table.
