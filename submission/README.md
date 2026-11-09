# SPTS1: exact-one-third sampled-pivot search

Read proof.md and its included inherited construction at
sources/RQ-SPLIT-proof.md. The single all-N configuration has

    T=O(2^(n/2)n log^3(n+2)), SC=O(n^2), SQ=O(n),
    exactly Q=3*2^40(n+32), epsilon=1/3,
    unconditional full-secret success >=11/16.

Resources hold on every branch. The indices remain (1,0,0,0). The exact source
cap is RQ-SPLIT's, larger than FNS1's; it is not n+1. Constants are large and no
practical time or hardware claim is made. The raw-error model is preserved
byte-for-byte; no herald flags or restricted error support are introduced.

From this directory, run the capped standard-library replay:

    python3 -B replay_checks.py

It copies the supplied checkers to a temporary directory and compares their
mathematical outputs without changing the recorded receipts. The reference
platform is Linux/Python 3.12. Each process has a 45-second CPU and 512 MiB
address-space cap. These are finite exact/abstract checks, not production
source-count or full-score-circuit executions.

The proof specifies the full coherent oracle and its cleanup. The tests include
nested-state/inverse checks, uniform-acceptance and negative controls, constants,
and physically possible N=4 shadow fixtures. They do not replace the uniform
proof. The independent reviews in review/ describe exactly what was audited.
See review/repairs.md for editorial changes from the preserved reviewed draft.

No review implies hosted acceptance or promotion. See sources.md for provenance.
