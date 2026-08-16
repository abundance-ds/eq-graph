# Common paper-first ontology agent task

Version 2, frozen 2026-08-16 before the first run.

Develop or extend a paper-first ontology and extraction guide for EuroQol research.
Use `PURPOSE.md` and `USER_QUESTIONS.md` as the fixed requirements.

The paper is the main record.
You can use paper-local components when a paper has different samples, phases, tasks or analyses.
Keep components, method paths and relations subordinate to the paper record.
Do not use another structure as the primary record.

Your main task is to discover useful granularity.
Do not use one broad method label when a more specific distinction changes retrieval, comparison or interpretation.
Do not add detail only because it is present in a paper.
Decide which information needs a controlled term, repeatable value, relation or concise narrative.
Record important distinctions that you considered but rejected.

Apply the ontology to every assigned paper as you work.
Revise it when paper applications or user questions show that a distinction is missing, too broad, too fine or difficult to apply consistently.
Connect important decisions to the papers and user questions that support them.

Capture concise principal findings, author interpretation, implications, limitations and stated gaps.
Do not extract every numerical result or create a detailed claim-evidence representation.
Do not infer impact or a corpus-level gap from one paper.
State whether an interpretation, implication, limitation or gap is author-reported or is the extractor's scoped observation.

Do not reconstruct deterministic bibliographic or source metadata.
Instrument version and language, population, administration, protocol, methods and study interpretation remain semantic study information and are in scope.

Keep the result intelligible to a researcher.
Use clear Markdown and choose the structure that best communicates the work.
Do not use a fixed JSON schema.

Maintain the current ontology, applications, granularity decisions, rejected distinctions, unresolved cases and a short run note.

Work only from this lineage's current files and assigned inputs.
Do not inspect version-1 ontology work, another lineage, graph schemas, legacy extractions or files outside the supplied worktree.
Treat the supplied purpose, questions, task and papers as the complete research context.
