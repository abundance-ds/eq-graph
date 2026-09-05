# Funding evidence audit for papers with no EQ instrument

## Decision rule

All verified EuroQol-supported outputs belong in the research portfolio, including outputs that do not use an EQ instrument.

For a paper with no reported EQ instrument, accept the project-publication link only when one of these conditions is true:

1. The article states that EuroQol supported this work, study, or its data.
2. An authoritative EuroQol project record lists the paper as an output.

Record the exact support type. Examples are study funding, data-collection funding, researcher support, travel support, and publication support. Do not convert all support into `study funded by EuroQol`.

Folder placement, author overlap, topic similarity, or a competing-interest statement that an author received a grant is not enough. Keep these links as candidates until review.

## Checked examples

The section names in this table refer to the local full-text corpus, which is not tracked in Git.

| Paper | Actual EQ instrument use | Evidence and support type | Decision |
|---|---|---|---|
| Peripheral nerve-block use, project `1483-TVG` | None | The article's Disclosures section states that EuroQol funded this work through a travel grant. | Accept as direct support. Record `travel grant`. |
| Cultural values and self-reported health, project `2015150` | None | The article's Acknowledgements section states that EuroQol funded this study. | Accept as direct study support. |
| QID-12 development, project `429-RA` | No EQ responses or scores in the reported analysis; an input dataset has an EQ-5D-Y-5L evaluation label | The article's Funding section states that EuroQol supported the data collections. | Accept as direct data-collection support. |
| Chichewa PedsQL adaptation, project `20190200` | EQ-5D-Y results are mentioned as work reported elsewhere; the PedsQL data came from the same Chichewa study programme | The article's Funding section states that LGN received EuroQol funding under project `20190200`. The canonical project title and abstract cover the same Chichewa sample and name PedsQL as a study instrument. | Accept as a project-supported secondary output. Record the article wording as `researcher/project funding`, not as an unsupported claim that EuroQol funded every part of the study. |
| Vision-impairment economic burden, project candidates `341-RA` and `357-RA` | None | The Funding section names the Trinidad and Tobago Ministry of Health and Fight for Sight. A separate competing-interest statement lists EuroQol grants received by one author. | Do not accept from article evidence. Require an authoritative project-output record. |

Two independent agents reviewed the source text and agreed on these decisions. They also found one useful false candidate: the FACIT-COST paper under `1644-RA` does use EQ-HWB and EQ-5D-5L, although its title does not show this.

The current generated `publications.json` files classify the vision-impairment paper as accepted under `341-RA` and `357-RA`. That classification fails the new evidence rule. Do not use it for funded-output counts until the discovery output is regenerated or an authoritative project-output record confirms the link.

## Required portfolio fields

- project ID;
- publication ID;
- link status: candidate, accepted, rejected, or superseded;
- evidence class: direct article statement or authoritative project-output record;
- exact support type;
- evidence source and location;
- review note, reviewer, and date.

Only accepted links enter funded-output counts.
