# Fractional metrics with retained validity

The optional DCP score-derivation profile preserves the active v6 validity policy,
original claim bytes and human review. It changes only scoring to
`dcp-time-growth-fraction-v3`, with `retained_result: yukon-retained-result-v1`.
The default main source and its v7 submission contract are not activated by this
migration.

The protected plan pins each selected original validity run, intake and accepted
claim artifact. Yukon independently supplies the current selected packet and
score/validity identities. Missing or changed evidence fails before the light
reviewer; it never starts an automatic full-review fallback. Baselines and jobs
explicitly requesting missing validity use the ordinary pinned v6 reviewer.
Rejected retained records need no provider call.

One `gpt-6-astra` reviewer at low effort has at most one request, 4,096 completion
tokens, 120 request seconds and 150 total review seconds. It extracts a fractional
tolerance and cites the accepted fifth claim. Deterministic checks preserve all
four structured resource bounds and the time score, require the identical error
model, and check count/fraction equivalence. Supported conversions are zero, full
sample tolerance, and `floor(c Q n^a (log2 n)^b)` to the corresponding capped
fraction. Positive Q-independent counts are explicitly unsupported; no sample
upper bound or corruption probability is substituted. Unsupported extraction
retains the original score and count metrics, so the fraction-configured frontier
omits it explicitly.

The new vector binds all five metrics to its derivation intake/result. Separate
`dcp_original` and `dcp_derivation` metadata preserve the original complete metric
objects, selected validity provenance, exact citations and derivation outcome.
Output echoes Yukon's issued `derived_from` and never emits a new `valid` field.
Simulation previews are unpublishable.

To prepare a profile, capture the full selected-submission snapshot and an
organizer artifact index with exact raw ZIP/file hashes. Supply an exact checkout
of the active v6 source; the generator verifies every tracked byte against the
specified Git tree. Run `tools/derivation_profile.py` with `--ordinary-source`,
`--source-ref`, `--snapshot`, `--artifact-index`, `--archive-root` and a new separate
`--out` directory. It verifies the plan before producing a source. Its default
ordinary verifier pin remains `204fdf8`; the separate derivation workflow pins
`da594aad`. Run both pins' required tests and `--check` on the generated source.
Refresh the full snapshot and plan after draining work, before an authorized
`scores:true, validity:unchanged` reorg. Activate the resulting source and publish
the matching fractional page configuration only after qualification.

Generic plan/route/hosted-transfer patterns follow the merged CircuitBreaker
adapter; DCP's domain checks, preserved resources and fraction conversion are
implemented here. Offline tests do not establish extraction quality or a live
mathematical verdict.
