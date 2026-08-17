# Relational ontology pilot

Status: the ten-study pilot and the full JATS metadata audit pass. The schema
also supports the completed 20-paper broader test.

## Purpose

- Test whether the ontology supports useful EuroQol questions.
- Keep exact domain facts as direct, typed records.
- Keep flexible concepts for discovery, without replacing exact facts.
- Load publication metadata from JATS XML without AI reconstruction.
- Test a relational implementation before any full-corpus run.

## Scope

- Ten scientific studies in the semantic pilot.
- One rejected funding-link boundary case.
- Eleven JATS XML files in the pilot database.
- All 220 repository JATS XML files in the deterministic metadata audit.
- This schema implements ontology v1 for the pilot. It is not a frozen
  production database contract.

## Run

```sh
python3 audit_jats.py
python3 build_pilot.py
python3 test_queries.py
```

The scripts use the Python standard library. `build_pilot.py` recreates
`ontology-pilot.sqlite` after it verifies the input hashes.

## Result

- The metadata audit has no parse failures and no nondeterministic output.
- The database build has no foreign-key errors.
- All 15 competency-query tests pass.
- Exact study types, instruments, methods, models, products, outcomes,
  findings, limitations, and concepts remain queryable.
- A verified funded paper with no EQ instrument is included.
- The unverified funding-link case is excluded from funded counts.

See `METADATA_AUDIT.md` and `QUERY_EVALUATION.md` for evidence.
