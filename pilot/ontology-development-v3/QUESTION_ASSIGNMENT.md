# Controlled competency-question assignment

Seed: `20260816`

Algorithm: parse positive questions Q1–Q100. Exclude B1–B20. Use `random.Random(20260816)`; shuffle Q1–Q100 once; assign first 25 to `shared`; split next 75 into consecutive 25-question private blocks A, B, C. Keep shuffled order. No topic rebalancing.

Negative-question exclusion: B1–B20 are excluded from the main assignment and are not in `questions.tsv`.

Counts: 100 rows; shared=25, A=25, B=25, C=25. Each agent receives 50 questions (25 shared + 25 private). Private sets are pairwise disjoint.

## Agent A (50, ordered)

Shared: Q47, Q54, Q74, Q57, Q44, Q81, Q22, Q20, Q87, Q78, Q62, Q11, Q51, Q33, Q77, Q99, Q1, Q31, Q12, Q59, Q58, Q18, Q7, Q30, Q80

Private: Q25, Q66, Q82, Q13, Q28, Q88, Q55, Q43, Q86, Q10, Q32, Q9, Q69, Q73, Q65, Q50, Q76, Q4, Q84, Q35, Q79, Q89, Q94, Q16, Q24

## Agent B (50, ordered)

Shared: Q47, Q54, Q74, Q57, Q44, Q81, Q22, Q20, Q87, Q78, Q62, Q11, Q51, Q33, Q77, Q99, Q1, Q31, Q12, Q59, Q58, Q18, Q7, Q30, Q80

Private: Q56, Q70, Q72, Q64, Q14, Q34, Q67, Q83, Q93, Q39, Q95, Q71, Q68, Q27, Q6, Q41, Q21, Q5, Q40, Q36, Q3, Q90, Q15, Q53, Q100

## Agent C (50, ordered)

Shared: Q47, Q54, Q74, Q57, Q44, Q81, Q22, Q20, Q87, Q78, Q62, Q11, Q51, Q33, Q77, Q99, Q1, Q31, Q12, Q59, Q58, Q18, Q7, Q30, Q80

Private: Q38, Q98, Q23, Q49, Q17, Q29, Q8, Q26, Q91, Q96, Q42, Q63, Q46, Q85, Q19, Q52, Q92, Q48, Q2, Q37, Q60, Q97, Q45, Q61, Q75

## Validation

Validation is performed after file creation by an independent script.

SHA-256 of the repository copy of `questions.tsv`: `d5b5322f002c8f7dc1b4ff68874652510c880f0c4b7fe65da314bd1d2960ef7f`
