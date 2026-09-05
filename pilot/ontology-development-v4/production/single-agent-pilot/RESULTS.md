# Single-agent full-text pilot

- Papers: 20
- Final decisions: 9 include, 11 exclude
- Differences from the reviewed two-agent baseline: 0 eligibility decisions and 0 project links
- Saved records: 20; failed records: 0
- Included records: 9 studies and 506 typed items
- Registry extensions used during validation: 97

One Opus call assessed each full text and extracted an eligible paper. Claude
received only native `submit` and `reject` tools. `submit` validated the complete
record, returned specific errors when necessary, resolved known scientific
identities, and accepted explicit additions for genuinely new identities.

The authoritative run is `native-opus-clean-check-01`. An earlier run under
`native-opus-smoke-01` used a prepared prompt that predated the native-tool
cleanup. It is diagnostic output only and must not enter the database.

The single-agent workflow reproduced all reviewed eligibility and project-link
decisions. It can replace the second general source-review call. Code validation
inside `submit` remains mandatory.
