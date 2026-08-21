# Registry expansion audit

Decision: reject the 436-row candidate as direct registry input. Keep it as a
review queue.

The candidate covers all 261 recurring unresolved label pairs and passes its
mechanical checks. However, semantic review found unsafe identity merges. For
example, it maps a 25-item Australian EQ-HWB proxy version to the base EQ-HWB
identity, maps distinct dated United States value sets to one generic product,
maps Dutch respiratory bolt-on values to the standard Dutch EQ-5D-5L value
set, and maps software that is only based on EQ-VT to EQ-VT itself. These links
would create false aggregate results.

The release therefore uses the earlier reviewed registry and keeps other labels
unmapped. One confirmed duplicate was repaired: `method:dce-with-duration` was
merged into `method:dce-duration`, and `DCEd` is now an alias of the retained
identity. Final normalization maps 1,022 uses, leaves 3,457 unresolved, and has
no collision or unverified match.
