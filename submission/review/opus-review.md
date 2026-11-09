# Independent review of SPTS1 (sampled-pivot tournament search, exact epsilon=1/3)

Reviewer: Claude Opus 5.5, acting as the review sub-agent, 2026-11-09. Review only: nothing was
submitted, posted, committed or installed, and no parent input was modified.

## Verdict: SUPPORTED, with editorial repairs

I found no material gap or counterexample in the claimed joint theorem:

    T=O(2^(n/2) n log^3(n+2)), S_C=O(n^2), S_Q=O(n), Q=3*2^40(n+32) exactly,
    epsilon=1/3 in the byte-identical adaptive model, full-secret success >=11/16

The theorem covers every N>=2, every secret and every adversary. It inherits RQ-SPLIT
Sections 1-6 and 8, and uses RQ-SPLIT Section 7 as the n<64 fallback. My acceptance is
conditional on those inherited sections being correct. I re-read the inherited arguments
that SPTS1 relies on (Sections 4-8), but I did not re-derive the source-label extraction
of RQ-SPLIT Section 3.

Each of the nine obligations in the brief checks out (Section 2 below). Five editorial
items (E1-E5) should be fixed before any submission. None of them changes a constant,
a bound or the algorithm.

## 1. Inputs and receipts

* All 14 files pinned in `review-inputs.json` match their SHA-256 values. This includes
  `PROOF.md` 0ac7a563…a512a and `sources/RQ-SPLIT-proof.md` 2952a6f5…a1ca80. The latter
  equals the pin in `sources/pins.json`.
* `sources/error-model.txt` appears verbatim, as a substring, inside RQ-SPLIT Section 0.1
  (ModelM).
* I ran `check_constants.py` and `terra/check.py` from copies in `review/replay/`, with a
  45 s CPU and 512 MiB cap. Both exited 0. Their JSON matches the original receipts,
  ignoring `cpu_seconds`. The originals were not touched.
* I did not open `peer-snapshot.json` or `peer-check.json`. Comparing against other
  submissions is outside this audit.

## 2. Obligation-by-obligation findings

### 2.1 True class survives a fresh sketch drawn after a wrong pivot (eq. 1)

Verified. Fix any records in E_score and any history up to the moment a wrong pivot p
is accepted. The list I and the threshold tau are then drawn from fresh coins, so their
law does not depend on p or on the history.

* **Which member means matter.** In a sketched comparison the candidate is fresh and the
  pivot is exact. E_score covers this role assignment, since RQ-SPLIT (A) gives an error
  of at most 1/1024 in every role.
  * If the true class is canonical first, it wins if, for both members u of p, the
    sampled mean(s,u) is at least tau.
  * If the true class is second, it wins if, for both members t of p, the sampled
    mean(t,s) is below tau, because min_u mean(t,u) <= mean(t,s).
  * So at most two member means matter. The proof's "four" is conservative.
* **Margin.** Every allowed threshold satisfies tau ∈ [-1/256, -1/256+(2^16-1)/2^23],
  which lies inside [-1/256, 1/256). The gap to ±1/64 is therefore at least 3/256 in the
  required direction, and the strict inequality "< tau" is covered.
* **Hoeffding bound.** Implemented scores lie in [-12/5, 12/5], an interval of width less
  than 6. With iid draws with replacement, the failure bound is
  exp(-2·ell·(3/256)^2/36) = exp(-ell/2^17) = e^(-a_sk) <= 2^-a_sk.
* **Union bound.** A sequential union over at most Hmax accepted pivots gives
  4·Hmax·2^-a_sk <= 2^-22, because 2^a_sk >= 2^24(Hmax+1). D1 rechecks this exactly.
* **What is not assumed.** The argument does not assume that an earlier sketch is
  independent of a later pivot. It also does not assume the true class stays a winner
  after it is visited.

### 2.2 Contextual pair counting (eq. 2)

Verified. Take distinct x and p in the current set S, and let c1 be the canonical first
of the two.

* "x beats p (x fresh)" and "p beats x (p fresh)" are the events {F_a >= tau} and
  {F_b < tau}. Both F_a and F_b are canonical max/min values of c1 against c2, built on
  the same list but with the fresh/exact roles swapped.
* For a fixed list, |F_a - F_b| <= epsilon_role. This holds because per-record
  differences survive multiset averaging, and max/min are 1-Lipschitz in sup-norm.
* So for a fixed list, the two probabilities over tau sum to 1 plus the number of grid
  points in a half-open interval of length at most epsilon_role, divided by 2^16. That
  count is at most 7, and 7/2^16 <= nu = 59/2^19.
* The sum is then averaged over the list. This is valid because (I, tau) has one law
  whichever element is the pivot.
* Ties are exact integer comparisons and fall into the half-open interval.
* No fixed tournament and no independence between candidates is used. Linearity over
  ordered pairs gives E|S'| <= (1+nu)(|S|-1)/2 <= (3/4)|S| for every record string and
  every past.

D2 rebuilds RQ-SPLIT's Section 6 word and score arithmetic and checks this. It
enumerates all 2^16 thresholds for 42 random pairs with a shared sketch: the total count
never exceeded 2^16 + 7, and it was exactly 2^16 in every case seen.

### 2.3 Frozen-prefix recursion V_j, bad-size events, bound (5)

Verified.

* **Uniform amplitude on P_j.** With psi = V_(j-1)|0>, we have
  V_j|0> = (2|psi><psi| - I) O_(P_j) psi. If psi has the same amplitude alpha on
  P_(j-1) ⊇ P_j, the marked amplitude becomes alpha(3 - 4|P_j|alpha^2) and is again the
  same everywhere on P_j.
  * This uniformity holds on every history, not only good-size ones; see E3. Good-size
    is needed only for the magnitude bound (5) and for positivity.
* **Frozen prefixes.** The proof states P_j = S_(128j) and makes it immutable. Later
  constraints only shrink S_r, which is a subset of P_j.
* **Markov bound.** Markov applied to the ideal chain's E|S_r| <= D rho^r gives (4). In
  exact arithmetic the sum is about 4.2e-13 < 2^-18.
* **Amplitude-loss sum.** It equals (4/3)Σe_j + (A_K^2 - 1)/(6D) <= 17/24576.
* **D1 recursion check.** D1 runs the worst admissible good-size recursion, with |P_j|
  at its largest allowed value, using rational bounds rounded downward. This covers every
  n in 64..300 and n = 512, 1024. The worst ratio alpha_j·sqrt(D)/A_j found is
  0.999466 > 1023/1024.
* **No cardinality oracle.** The algorithm never uses |P_j|. Only the analysis does.

### 2.4 Prepared-state mixed-Grover sampler

Verified. Let psi = V_j|0>. The operator V_j R0 V_j^† O_(S_r) equals
(2|psi><psi| - I)·O on the span of psi_M and psi_U.

* **Success probability.** It is sin^2((2t+1)θ) with sin^2θ = p = h·alpha_j^2. The
  unmarked part does not need to be uniform.
* **Uniform acceptance.** The marked component stays proportional to psi_M, which is
  uniform on S_r. So for each fixed clock, and on the direct branch, acceptance is
  uniform on S_r. Attempts use fresh work and coins, so conditioning on earlier failures
  or on the successful clock does not change this.
* **Explicit inverse.** V_j^† = V_(j-1)^† O V_(j-1) R0 V_(j-1)^†.
* **Global phases.** Sign conventions for -R0 only add global phases.
* **Bcap is large enough.** Bcap_j·A_j >= 16·root > 4·(1024/1023)·sqrt(D), so the first
  qualifying scale B0 is at most Bcap_j. D1 checks the squared inequality exactly.

D3 is a scaled state-vector simulation. Amplitudes on P_j were equal in every case
(asserted). A uniformity test over 22,195 acceptances used the randomized rank PIT and
gave chi^2 = 9.73 on 9 degrees of freedom.

### 2.5 Hitting time and coupling (eqs. 6-7)

Verified.

* **Per-seek bound.** Let B0 be the first dyadic scale with B0 >= 4/sqrt(p). Then the
  expected B-sum per seek is at most 16·B0 + 16·B0/(1 - 2(7/8)^16) <= 48·B0 < 384/sqrt(p).
  The proof's 512 is valid.
  * Holding B at Bcap only removes doubling, so the bound still holds.
  * A_j/sqrt(p) <= (1024/1023)·sqrt(D/h), so the expected token cost of a seek is at
    most 1024·sqrt(D/h), whatever the stage.
* **Band bound.** Four contraction steps followed by Markov give survival in a band of
  at most 2·rho^4 = 81/128. Cardinality never increases. So the expected number of steps
  per band is at most 4/(1 - 81/128) < 16, and Σ_a 16·2^(-a/2) < 64.
* **Stopping time.** "First bad-size event" is a stopping time at step starts, because
  B_j is fixed when pivot 128j is accepted. Bound (6) is applied only on histories
  before that time, so nothing is conditioned on future survival.
* **Coupling.** Because acceptance is structurally uniform, the actual pivot process
  has exactly the ideal chain's law up to any stop (budget, index abort, Hmax). It is
  not merely coupled until the first bad-size event; this is stronger than the proof
  claims (see E3).
* **Markov on the budget.** Total expected charge is at most 2^16·sqrt(D), and
  Budget >= 2^28·sqrt(D), so Markov gives 2^-12. A refused debit is counted in full.
* **Bad-size paths.** These are already charged to (4). Their actual work is still
  bounded by the deterministic budget.

D3 (scaled) gave a mean of 634 tokens to visit, against a scaled analytic bound of
2^16·sqrt(D) = 4.2e6.

### 2.6 Token budget and work outside it

Verified.

* **Debit before work.** B·A_j is debited before any query work. B is a power of two,
  so the debit is a shift of A_j, costing O(n) bit operations, which is at most U(n).
* **Per-attempt cost.** An attempt costs O(U·B·A_j) because:
  * C(V_j) <= 3·C(V_(j-1)) + O((j+1)U) solves to O(3^j U), since Σ(j+1)/3^j converges;
  * O_(S_r) and the classical verification each cost O(r·U) <= O(128(j+1)U) = O(3^j U).
* **Per-constraint cost.** Each constraint costs ell·O(n·p) gates times an O(log n)
  address charge, which is O(n log^3 n) = U(n), with ell = O(log n). There is no hidden
  per-gate n-bit counter.
* **Work outside the budget:**

  | Item | Bound |
  |---|---|
  | Pivot caches | at most Hmax |
  | Full-bank champion | at most Hmax - 1 classical comparisons, O(k·n^2) each before log factors |
  | Index rejection | capped |
  | Acquisition and endpoint | inherited, polynomial |

  All of these are deterministic polynomials, at most O(n^4 polylog n), which is far
  below 2^(n/2).

### 2.7 Saved-pivot champion

Verified.

* **The true class wins the tournament.** On E_score the true class wins every
  full-bank comparison at tau = 0 in either role and in either canonical order. So once
  it is champion it stays champion, and as a challenger it beats any champion. Cycles
  among the false classes do not matter.
* **Visiting is enough.** The champion step reduces correctness to visiting the true
  class. This is exactly what (9) bounds.
* **The retained bank is untouched.** The champion uses only the classical shadow bank.
* **Tests.** D3 had 275 runs where the last pivot was wrong but the champion was
  correct. It never had a run where the true class was visited and the champion was
  wrong. The supplied N=4 fixture shows a physical sketch error.

### 2.8 Endpoint law, single acquisition, n<64, error model

Verified.

* **No second acquisition.** Coarse search acts only on classical shadows plus fresh
  coins and work. No second bank is acquired.
* **Coarse failure bound.** The bounds in Pr(coarse failure ∧ G_source) <= delta_coarse
  hold for every fixed record string in E_score.
* **Endpoint argument.** The endpoint argument is RQ-SPLIT's
  E[(1/2 + 1{X_g>R}/2)·1_A] >= 1/2 + Pr(X_g>R)/2 - Pr(¬A), with an unconditioned binomial
  law.
  * On a correct class, the correct-direction count depends only on the retained clean
    odd-W labels, not on which representative t is chosen. So correlation between the
    shadows and the coarse output does not enter.
* **Losses.** Total loss is below 3/128, giving success >= 0.6950 > 11/16.
* **n<64.** RQ-SPLIT Section 7 runs on the same records, with the same k and Q.
* **Error model.** The error-model text is identical to RQ-SPLIT's.

### 2.9 History oracle and memory

Verified.

* **Antisymmetry.** With each member's word fixed, the implemented score satisfies
  G(t,u) = -G(u,t) exactly, because the four interpolated terms swap with sign. So when
  the pivot is canonical first, the "negative transpose, recompute max/min, complement"
  route equals the direct definition.
  * D2 checked this: 560 antisymmetry checks and 42 matrix-route checks.
* **Error bounds.** Fresh windows are within one cell of the exact words (560 checks),
  and the role discrepancy is at most epsilon_role (800 records; worst observed 0.34 of
  the bound).
* **Memory:**

  | Resource | Bound |
  |---|---|
  | Flags | O(Hmax) = O(n) |
  | Accumulators | width bitlength(ell)+50, enough since the per-record numerator is at most 24·2^42 |
  | Recursion stack | O(K log n) |
  | Indices | O(n log^2 n) |
  | Pivots | O(n^2) |
  | Pivot words | O(n log n) |

  So S_C = O(n^2) and S_Q = O(n).

## 3. Editorial items (repairable, non-blocking)

* **E1, Section 1.** "After every delivery, choose the bounded uniform k_shadow-subset"
  should read "after ALL Q deliveries", as in RQ-SPLIT Section 4.
  * Read literally, it suggests choosing the split per delivery. That would change the
    supplier feedback and the Section 4.1 causal argument. The intended meaning is clear
    from the inheritance, but the sentence should be fixed.
* **E2, Section 5.** State that B is reset to 1 at the start of every new pivot seek.
  * The derivation of (6) assumes this ("charged sum of B below B0 <= 16·B0").
  * If B carried over from the previous seek, then at a stage change, where alpha grows
    about 3x, the inherited B could exceed the new B0. Bound (6) would then need a
    separate argument.
* **E3, Sections 4 and 6.** Equal amplitudes on P_j, and hence uniform acceptance, hold
  on EVERY history by nestedness. Good-size is needed only for (5), that is, for
  positivity and the cost bound. Saying so makes the coupling exact up to the stop, not
  just until the first bad-size event. This only strengthens the proof.
* **E4, Section 3.1.** At most two member means are needed (Section 2.1 above). Four is
  a valid but loose count.
* **E5, Sections 5 and 6.** After the set is exhausted, the actual controller keeps
  burning tokens until a debit is refused. The proof should say explicitly that the
  coarse phase always ends by Hmax, index abort or refusal, and that a refusal after
  exhaustion is not a failure, because exhaustion implies the true class was visited
  on the good events.

## 4. Independent diagnostics (review/diag/)

These were written by me and run with ulimit -t 45, -v 512 MiB, `python3 -I -B`,
and numpy pinned to one thread. They are finite checks and do not replace the proof.

* **`d1_constants.py` → `d1_results.json`.** Exact arithmetic over n = 64..1024 plus
  1500, 2048, 4096 and 8191.
  * Checks: K is maximal, K >= n/9, n - 32K < -64, the (1) union bound, the r_idx cap,
    Bcap against 4/sqrt(p_min), the worst good-size recursion (n up to 300, plus 512 and
    1024), nu, the sum in (4), the constants in (6)/(7)/Markov, delta_coarse, and the
    final success bound.
  * Status: passed.
* **`d2_scores.py` → `d2_results.json`.** A replica of the RQ-SPLIT Section 6 phase-word
  and score arithmetic. The cosine grid values come from rounded doubles, which does not
  affect the structural checks.
  * Checks: fresh words within one cell, exact antisymmetry, role discrepancy, the
    transpose route, and the full 2^16 pair count.
  * Status: passed.
* **`d3_controller.py` → `d3_results.json`.** A scaled abstract controller: D = 2^12,
  64n replaced by 2, Cblock = 5, K = 3. It does not use DCP records or production
  constants.
  * It runs 2,259 instances and checks sampler uniformity, the recursion amplitudes,
    token use against the analytic bound, and champion wiring.
  * Visiting failures (1.5%) come from the scaled Hmax and the deliberate 1e-3
    true-removal rate, not from the controller logic.

## 5. Precise scope

**Checked:**
* All of PROOF.md, against RQ-SPLIT Sections 0.1 and 4-9.
* All nine brief obligations.
* All numeric constants, exactly.
* Both supplied checkers, replayed.

**Not checked:**
* The internal correctness of RQ-SPLIT Sections 2-3, which I treated as inherited.
* FNS1, beyond its sketch interface.
* The peer snapshot or comparison.
* Any production circuit, gate count or physical source run.
* A formal proof-assistant certificate.

Finite diagnostics are corroboration only. This review does not authorize submission.
