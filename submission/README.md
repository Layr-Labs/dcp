# FNS1: filtered robust DCP search

Start with proof.md. It specifies one complete algorithm for every modulus and
includes all error, work, memory and source accounting. sources/ROB-G2-proof.md
supplies the inherited acquisition, exact arithmetic, score construction and
small-n fallback; its unmodified bytes match the cited official source hash.

The guarantees are T=O(2^(n/2)n log^3(n+2)), S_C=O(n^2), S_Q=O(n), exactly
Q=2^33(n+4) and malformed fraction 3333/10000 under sources/error-model.txt.
The success lower bound exceeds 395079601/536870912>2/3. The indices remain
(1,0,0,0). This does not retain PFD-N1's exact n+1 cap or improve time index 1/2.
Constants are large; no practical speedup or crossover is measured.

From this submission directory, standard-library diagnostics are:

    python3 -B check.py
    python3 -B review/independent_check.py

Each process enforces a 45-second CPU limit and 512 MiB address-space limit.
check.py writes results.json. The independent script writes
review/independent_results.json. Recorded parent results are in
recorded-results.json. Review and parent scripts are independent implementations
of the finite checks; their exact and numerical scopes are distinguished in
review/REVIEW.md. These are not production circuit/source-count executions.

The explicit score phase oracles are constructed in proof.md and the inherited
source. The tests evaluate small Boolean phase oracles and exact Hadamard-layer
circuits, not the full large cosine table. The mathematical proofs supply the
uniform asymptotic guarantees. The review is evidence of an independent audit,
not a substitute for proving the claims or an assertion of hosted acceptance.

See sources.md for provenance and review/REPAIRS.md for the final clarifications.
