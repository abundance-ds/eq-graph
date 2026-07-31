# Vendored agent skills

Nine skills from [neo4j-contrib/neo4j-skills](https://github.com/neo4j-contrib/neo4j-skills), MIT licensed — see [`LICENSE`](LICENSE).
They are committed rather than installed on demand, for three reasons.

`skills-lock.json` records the upstream repo but **no commit SHA**, so `npx skills experimental_install` resolves against whatever `main` says today.
It also cannot describe `neo4j-mcp-skill`, which is patched locally and therefore absent from the lock file entirely.
And skills are prompt content: a teammate resolving a newer revision gets different Cypher out of their agent, with nothing in the diff to explain why.
420 KB is a cheap price for that not happening.

`skills-lock.json` stays tracked as a provenance record and to keep `npx skills update` working — it is not the restore mechanism.

## The patch

`neo4j-mcp-skill/SKILL.md` has one deviation from upstream: its `description` contained `(neo4j/mcp): `, which makes the frontmatter invalid YAML, so `npx skills add` skipped the skill silently.
The colon is replaced with a dash.
Re-apply it if you ever refresh this skill from upstream.

## Updating

```sh
npx skills update -p                     # then re-apply the mcp patch and review the diff
```

Review what changed before committing — an upstream edit to a SKILL.md changes how the agents behave.

## Activation

`.claude/skills/` holds relative symlinks into this directory, and is tracked, so a fresh clone needs no setup on macOS or Linux.
Git on Windows does not create symlinks by default; there, reinstall with `npx skills add https://github.com/neo4j-contrib/neo4j-skills --skill <name> --copy`.
