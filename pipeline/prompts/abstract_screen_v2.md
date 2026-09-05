# Funded-project publication screen

Assess one publication from the supplied evidence only. This is a high-recall
screen for full-text verification, not the final funding decision.

The graph covers publications that EuroQol supported or that clearly came from a
funded EuroQol project. At this stage, decide whether the publication has credible
support evidence or a concrete link to a supplied project. Do not decide final
inclusion.

Return one JSON object. The decision is only a routing action:

```json
{"decision":"RETRIEVE_FULL_TEXT|EXCLUDE","project_ids":["project ID"],"reason":"35 words or fewer"}
```

Use these rules:

- Use `RETRIEVE_FULL_TEXT` when there is a credible EuroQol support signal or a
  concrete, plausible link to a supplied funded project. This does not mean that
  the paper is eligible.
- An exact OpenAlex EuroQol funder signal or a EuroQol award string can justify
  retrieval unless the record is an obvious namesake or metadata error.
- A project link normally needs compatible dates and personnel plus a distinctive
  match in objective, instrument, method, population, dataset, protocol, or
  research product. Without a personnel match, retrieve only when the objective,
  dataset, protocol, or product match is unusually specific.
- A linked EuroQol person alone is not sufficient. A broad shared topic or method
  alone is not sufficient. Do not turn either into a project link.
- Being about, developing, valuing, validating, or using a EuroQol instrument is
  not sufficient without support evidence or a concrete funded-project link.
- Use `EXCLUDE` when neither support evidence nor a concrete project link is
  plausible from the supplied information.
- For `RETRIEVE_FULL_TEXT`, return only plausible IDs from the supplied project
  list. Return all plausible IDs, but do not add weak topic-only matches. For
  `EXCLUDE`, return an empty list.
- A project with a known start year after the publication year cannot match.
- Keep the reason factual and concise.

EuroQol supports many kinds of research. Do not infer support from subject matter
alone.
