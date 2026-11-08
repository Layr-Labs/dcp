# Repairs following the independent review

The original reviewed draft remains at reviewed-draft.md with SHA-256
84e5509f85b6959f1762828a2239c90be46b4498b30fc97430a42deba9c77528.
The manifest records the actual bytes; this listed hash is checked during
packaging. REVIEW.md refers to that draft. The final proof.md incorporates:

- R1: E is defined as the record-measurable event satisfying the gap condition;
  the compensator event G_0 implies E and need not be record-measurable.
- R2: the list-index loop, multiplicities, w_f, C_f_star, Theta_f, signed range,
  per-record scratch cleanup and full reverse loop are explicit in Section 4.
- R3: the score range follows from |c_k|<=2^25 in Lemma T, not Lemma B's looser R.
- R4: floor-square-root and iteration rounding inequalities are derived for
  both parities of the relevant exponents.
- R5: the success chain is conditioned in order on E, successful generation,
  F and readout. Main-branch output has no classical recheck.
- S2: general amplitude amplification and prior nested search are cited, with
  novelty scoped to the application and certificate.
- I1: L>Q below n=695 is stated explicitly. No practical speedup is claimed.

S1 concerns the separate snapshot comparison, not the theorem: 91 valid rows
in the saved comparison's context had nonconstant vanishing tolerances and
were excluded from its constant-fraction comparison. The public note reports
that exclusion. No source proof or algorithm parameter was changed by these
repairs. The final copy includes explicit index derivations and claim formatting.
