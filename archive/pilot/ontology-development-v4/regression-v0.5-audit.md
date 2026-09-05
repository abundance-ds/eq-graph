# Version 0.5 regression audit

The blind run mapped all 60 studies without a new record, key, controlled
value, or gap. It matched 59 of 60 source-adjudicated primary families.

The only difference is C011. The regression used `METHODS_RESEARCH`; the prior
source review used `HEALTH_PREFERENCE_RESEARCH` because empirical self/other
and adult/child preference differences are the main results and no method is
selected. Both readings are plausible from normal paper reporting.

Decision:

- keep the source-adjudicated C011 mapping;
- do not add a paper-specific boundary rule;
- accept version 0.5 as the structural candidate for production calibration;
- treat primary family as a high-impact governed classification; and
- measure unseen-paper agreement before trusted aggregate loading.

This is a 59/60 classification result, not a claim that complete extraction is
98.3% accurate. The regression tested family, first purpose, and main design
and data axes. It did not source-audit every extracted fact.
