The CSV file contains 20 projects to ingest into the knowledge graph for testing the initial emergent ontology

## Markdown full texts

Every paper in these 20 project directories has been converted to Markdown, next to its source:

    input/projects/<project id>/papers/<work id>.md

30 documents in all — the 20 the CSV names, plus the 10 other papers those directories hold.
23 come from JATS XML through pandoc, 7 from PDF through poppler; the `fulltext_format` column says which for the CSV's own row, and each file's front matter carries `source_format` along with the SHA-256 of the file it was made from.

Regenerate with:

```sh
python3 scripts/to_markdown.py --beside <project ids…>
```

`--beside` is what puts the output next to the sources rather than under [`corpus/`](../../corpus/README.md), which is where the rest of the converted full texts live.
Note that this is the one place derived files sit under `input/`, against the rule stated in the [root README](../../README.md#repository-map); the pilot wants each project's Markdown in the project's own directory.

The PDF-derived documents are the thinner ones, and the CSV's `fulltext_format` column identifies them.
A publisher PDF has no structural markup at all, so they carry no author list, keywords or affiliations, their reference lists are not reassembled, and their tables arrive as loose lines in reading order rather than as tables.
Where a project holds both formats, the XML-derived file is the better source.
