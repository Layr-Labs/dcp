# IFW-12-32 submission guide

This directory is the complete candidate for one algorithm and one parameter
configuration: **IFW-12-32**, the CW1 collimation skeleton with the
constant-width MERGE4I schedule of `proof.md` Section 7 at the fixed rationals
**(a, A, C) = (1/2, 3/2, 3/4)**, main branch n >= 4096 and finite branch
N <= 2^4095. All five claims in `submission.json` refer to this single
configuration and the same execution. There is exactly one algorithm; the
parameters w, lw, mu, kappa, Lam, l, nqmax are functions of n = ceil(log2 N)
alone, defined in `proof.md` Section 7.

## Files

- `submission.json` - the five declarations (T, S_C, S_Q, Q, tolerance).
- `proof.md` - the complete, self-contained proof. It is the direct source of
  every guarantee; no external fetch or private document is needed.
- `checks.md` - finite falsification checks: what was run, the observed
  results, measured resources, and honest scope limits.
- `checks.py` - the exact-integer test program for those checks (standard
  library only, deterministic, exits 0 on success).

## Claim-by-claim map into `proof.md`

- **Claim 0, total work T = O(n^(7/2) 2^((43/18) sqrt n)), index 1/2.**
  Section 0 states the joint theorem; the cost model and the address debit are
  Section 2 (equation 2.1); per-branch core steps are Lemma 11.2 (Section 11);
  the final multiplication by the address width and the envelope arithmetic,
  with the exact equal-rank coefficient 43/18 = 3/2 + 8/9, are Section 13 ("T")
  and Section 14.
- **Claim 1, classical space S_C = O(n^2 2^((3/4) sqrt n)), index 1/2.**
  Section 13 ("S_C"): depth-first stack bound with size fact S3, table sizes
  with 2^Lam = 2^(kappa+1) 2^w (S4), merge scratch of Sections 6.2/6.3, the
  decoder, LE scratch, counters. Fixed allocations, so the bound holds on every
  branch, including wrong-label branches.
- **Claim 2, quantum space S_Q = O(n), index 0.** Section 13 ("S_Q"): the
  depth-first stack of at most 4(mu+5) Lam <= 20n index qubits (S6), merge
  registers O(sqrt n), LE and transform scratch O(n), measurement at the root.
- **Claim 3, samples Q = O(n^2 2^((8/9) sqrt n)), index 1/2.** The finite
  branch cap N(n+10) and the main-branch acquisition down-counter Qcap = 1024
  Q* are in Section 11; Q* = O(n^2 4^mu) with 4^mu < 4*2^((8/9) sqrt n) (Lemma
  7.0(c), S3) is Section 13 ("Q"). Every discarded, rejected, failed or
  restarted acquisition is counted; the cap is enforced on every branch.
- **Claim 4, tolerance epsilon(n) = 0 (unscored).** Section 15, with the clean
  model already used throughout: every acquisition is an independent ideal
  coset state. The joint success probability 1 - 769/524288 >= 1 - 2^-8 > 2/3 is
  Section 12; the error budget is assembled from Lemma 5.1/5.2 (LE), Lemma 9.1
  (decoding), Markov on Lemma 11.1, and the LE/ABORT coupling of Section 5.6.

## How the joint theorem is proved, and where to challenge it

- Recovery of the full secret for every N >= 2 and every s: odd part by
  free-frequency decoding (Section 9), 2-adic part bit by bit (Section 10),
  finite branch below the threshold (Section 11). Non-power-of-two N is handled
  by d = floor(log2 N), the CRT units alpha_j, and the exact data transforms of
  Section 3.
- The latent-label model and the top-bit independence argument are Section 3
  and Section 8; the two-stage fiber moment bound of MERGE4I is Lemma 8.2, with
  the failure identity Lemma 6.3. Both are r-generic; the endpoint analysis
  2w - lw in {0,1} (so r = kappa+1 or kappa+2) is size fact S2 of Section 7.
- Hard cutoffs on every branch: acquisition down-counter (Qcap, Section 11),
  high-confidence LE counter (Section 5.5, Lemma 5.2), merge FAIL resets
  (Sections 6.2, 6.3). Wald's identity with the correct factor
  rt^m <= exp(m/(2(mu+4)-1)) <= e < 3 is Lemma 11.1.
- Precision: all tree, merge and decoder arithmetic is exact integer
  arithmetic; the only approximate object is the fixed 4096-entry rational
  trig table of Section 4 (error < 1/625), absorbed by Lemmas 5.1 and 9.1 with
  explicit constants.
- Charging: no QRAM (lookups are the explicit costed circuits of Section 6.1),
  no source inverse or coherent source control, no uncharged preparation; each
  core step pays its address (Section 2); each acquired copy costs n+1 and is
  counted in Q.

## Reproducing the finite checks

    cd submission && python3 checks.py

Expected output is printed at the end of `checks.md` with the observed exit
status, wall time and peak memory; the expected parameter values asserted
first were derived by hand from the definitions, independently of the program.

## Provenance

`proof.md` Section 1 records the exact textual and mathematical provenance:
the direct source IFCW23 (public submission
19391317-be51-44c1-af9f-7f3dfbf32d28), the IFC1/CW1/CS1/MW4/CS1-S3 chain with
submission identifiers, and the external references (Kuperberg
arXiv:1112.3333v1; Schroeppel-Shamir; Howgrave-Graham-Joux). New here is only
the schedule point (1/2, 3/2, 3/4) and its compiled numerics (Sections 0, 7,
the cost sentences of Lemma 11.2, 13, 14). No claim of a first method, of
novelty beyond this parameterization, or of any prior acceptance is made, and
no hosted acceptance is asserted by this package.
