# Invalidated round-one attempt

Status: invalidated before any lineage output was accepted or compared.

All three agents received the same frozen task and batch.
All source hashes, byte counts and paper-coverage checks passed.

The input-context audit found an unequal external input:

- Agent A opened `.agents/skills/neo4j-modeling-skill/SKILL.md` outside its supplied worktree.
- Agent A used its guidance about entity boundaries, explicit relations, intermediate records and relation direction.
- Agents B and C did not open or use the skill.

The skill supplied no EuroQol facts, but its modeling guidance could change the ontology representation.
The three outputs are therefore not a controlled comparison set.

The operator preserved all three files here and removed them from the lineage worktrees.
None was committed to a lineage branch.
Round one restarts for all lineages with fresh contexts and the same explicit instruction that this is not a Neo4j modeling task.
