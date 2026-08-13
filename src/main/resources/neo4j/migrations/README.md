# Neo4j migrations

`Application.server()` runs every `V*.cypher` file in this directory against the database on startup,
in version order, recording what it applied in the database itself
(see `applyMigrations` in [`Neo4j.kt`](../../../kotlin/Neo4j.kt)).

Naming: `V{version}__{Description}.cypher`, version zero-padded (`V001`, `V002`, …), description words joined by underscores.
Never edit a migration that has been applied anywhere — add the next one instead.

The schema itself still lives in [`graph/schema.cypher`](../../../../../graph/schema.cypher) and is applied by hand.
The edition question that used to block moving it here is settled: migrations target Enterprise/Aura, which is what
both the deployed instance and the tests now connect to, and the whole file applies there unchanged —
all 48 constraints and 20 indexes, verified against Aura `5.27-aura`.

What is left is a placement decision rather than a compatibility one.
Moving it here makes the server apply it on startup and gives it a checksum,
after which it can never be edited — every schema change becomes a `V002`, `V003`, … instead.
Keeping it in `graph/` keeps it a single editable document at the cost of applying it by hand.

This file is here so the directory exists on the classpath while no migration does;
the scanner only looks at `.cypher`, so it is inert.
