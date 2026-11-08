# Independent review: filtered search with a fixed amplification schedule (PROOF.md)

Reviewer: Claude Opus 5.5, acting as the review sub-agent. Date: 2026-11-09.
Review only. Nothing outside `review/` was modified. Nothing was submitted, posted or installed.

## Verdict

**SUPPORTED, with minor repairable presentation gaps. Nothing blocks it.**

I re-derived the whole argument by hand: the interface, the filter, the cardinality bound, the
nested amplification, the success product and the resource accounting. I found no mathematical
error in the target theorem:

    T = O(2^(n/2) n log^3(n+2)),  S_C = O(n^2),  S_Q = O(n),  Q = 2^33(n+4) exactly,
    epsilon = 3333/10000 in the verbatim adaptive malformed-copy model,
    success >= min(49/64, 395079601/536870912) > 2/3 for every N >= 2, every s and every adversary,
    with bounded work on every branch.

The five items below (R1–R5) should be fixed in the text before submission. None changes a
constant or a bound. Two more items are scope or citation obligations (S1, S2), and one is
informational (I1).

## Frozen inputs

I checked all ten hashes in `review-inputs.json` against the files on disk, before and after this
review. All of them match, including `PROOF.md` 84e5509f…, `sources/ROB-G2-proof.md` 64a87926…
and `sources/error-model.txt` fd67d2af…. I did not touch any parent file. `check.py` was replayed
only from a copy in `review/replay/`, which also holds a copy of `sources/`.

## What I checked, item by item (brief §1–7)

### 1. Inherited event, under the same adversary — verified

* ROB-G2 Theorem 1 defines 𝒢₀ = {Σ_j D_j(s) > −δQ} ∩ ⋂_{t<N,t≠s} {Σ_j D_j(t) < δQ}. It has
  probability > 7/8 for every adversary of the model. The bound comes from Azuma–Hoeffding with
  width 2R plus a union bound over N events.
* On 𝒢₀ its proof gives the quantitative statements S(s) > Q·Lo and S(t) < Q·Hi for every valid
  t ≠ s, not just uniqueness of the mark. This is exactly (1), with θ = 6667/40000, provided
  Lo − θ > γ and θ − Hi > γ.
* I recomputed Lo and Hi from ROB-G2 §4.1/§6 with π < 22/7. η = 3π2^-24 + τ is increasing in π,
  so an upper bound on π is the safe direction. The results:
  * Lo − θ = 256318304059827/58720256000000000000 ≈ 4.365e-6
  * θ − Hi = 24376142481/5872025600000000 ≈ 4.151e-6

  These are the parent's values exactly. They exceed γ = 1/250000 by factors of 1.091 and 1.038,
  which is thin but exact.
* **Score range.** Hoeffding with width 2 needs z ∈ [−1, 1]. ROB-G2's Lemma B only states
  |Z̃| ≤ R = 1 + 2^-24. However, Lemma T proves |c_k| ≤ 2^25, so table[k] = c_k/2^25 ∈ [−1, 1]
  exactly, and the parent's citation of Lemma T is correct. I also evaluated c_k exactly at the
  extremes k ∈ {0, 1, 2^22, 2^23 ± 1, 2^23, 2^24 − 1}: |c_k| ≤ 2^25 = 33554432 every time.
* **Same adversary.** The acquisition phase is byte-identical to ROB-G2 §4.4, and every adversary
  decision happens before a delivery. So the adversary's information and the law of the records
  (Fact E, Lemma M) are unchanged, even if the adversary knows the new search stage. The filter's
  fair bits are drawn after the last delivery from fresh |0⟩ qubits. The model guarantees these
  are not entangled with the adversary's system, so the adversary never sees them.

### 2. Late sampling with replacement — verified

* Each trial uses ceil(log₂Q) bits and accepts a value < Q. Since 2^(ceil log₂ Q) < 2Q, each trial
  succeeds with probability > 1/2.
* With r = ceil(log₂(128L)) trials per index, a given index fails with probability ≤ 2^-r ≤ 1/(128L).
  A union bound over the L indices gives ≤ 1/128.
* Conditional on no failure, the indices are iid uniform on [Q] and independent of the records.
  The bits are fresh, and the geometric sum is the same for every accepted value.
* Every failure is in the output distribution: the algorithm outputs 0, with bounded work.
* Hoeffding over L iid draws from the fixed string gives exp(−2L²γ²/(4L)) = exp(−Lγ²/2) = e^-a.
  This uses 2/γ² = 1.25·10^11 exactly.
* Strictness is handled correctly: f(s) = 0 needs a deviation of ≥ γ, and f(t) = 1 needs a
  deviation of > γ.
* No copy is acquired after the draw.

### 3. Cardinality and Markov slack — verified

* The bound E H ≤ 1 + D·2^-a uses only linearity of expectation; candidates are not assumed
  independent.
* D·2^-a = 2^(n−a) ≤ 2^(b−12) = G/4096 because b ≥ n − a + 12. Then 1 + G/4096 ≤ G/2048 because
  G ≥ 4096.
* Markov gives P(H > G/64) ≤ 1/32, and P(f(s) = 0) ≤ 2^-a. Hence P(F) ≥ 31/32 − 2^-a.
* For n ≥ 20 we actually have a ≥ 28, so the parent's 2^-16 is just a weaker bound. G/64 is an
  integer.
* The parent's counterexample to the original cutoff (E H = t but P(H > t) = 1 − 1/t) is correct.
* I checked the integer premise D ≤ (G/4096)·2^a exactly for every n in [20, 20000].

### 4. Integer schedules and the amplitude bound — verified

I checked every inequality in §3 of PROOF.md:

* X = isqrt(2^m) with m = n − b ≥ 8, and q = 2⌊(X−1)/2⌋ + 1 ∈ {X, X−1}, so x − 2 < q ≤ x. Since
  x ≥ 16, q ≥ (7/8)x.
* h/D ≤ 1/16384, which gives z² ≤ 256/16383 < 1/63.
* sin z ≥ z(1 − z²/6), and z(1 − z²/6) is increasing on the relevant range.
* (129/128)² · 16383/16384 ≥ 1. Then α ≤ 129/8192 < 1/63, so arcsin α ≤ (64/63)α. This step needs
  (64/63)²(1 − 1/63²) > 1, which holds.
* 2j + 1 ∈ [3√G/2 − 5/2, 3√G/2 + 1]. This covers both the case where b is even and isqrt is exact,
  and the case where b is odd.
* The angle lies in [70499/55296, 4171/2688] ⊂ (5/4, 25/16]. Also 25/16 < π/2 because π > 25/8.
* The truncated alternating series bound for sin(5/4) has square
  245618323006225/272747603165184 ≈ 0.9005 > 7/8.
* I also checked every integer premise exactly for each n in [20, 20000]: q²G ≤ D ≤ (q+2)²G,
  64q²G ≥ 49D, both bounds on 2j+1, k ≥ 7 and j ≥ 48.

The operator word also checks out:

* V R₀ V† = 2|ψ⟩⟨ψ| − I with ψ = V|0⟩ holds for any unitary V. So the outer loop is standard
  amplitude amplification of the |s⟩ component, and the rest of ψ can be nonuniform.
* α > 0 on the whole range, since z < 1/√63.
* Sign errors in implementing R_u cancel exactly: V′ = (−1)^k V and V′† = (−1)^k V†. A sign error
  in R₀ only adds a global factor (−1)^j.
* O_v needs to mark only s, and on F, s passes the filter.
* The counts are k(2j+1) filter calls and j full-predicate calls, and (k(2j+1))² ≤ D.

**Independent simulation of the actual operator word** (part D of
`review/independent_check.py`):

* Method: the actual operators restricted to span{|s⟩, uniform(M∖s), uniform(unmarked)}, with V R₀ V†
  realised as 2|ψ⟩⟨ψ| − I. Matrix powers with the exact integers k and j. Decimal precision n/3 + 60
  digits.
* Coverage: every n in [20, 160], and h ∈ {1, 2, 3, …, G/128, G/64 − 1, G/64} plus a geometric grid.
  1746 cases in total.
* Result: minimum success 0.9723 (at n = 20) and about 0.994 for n ≥ 30. Norm error ≤ 1.5e-62.
* This does not use the closed form (5), so it is an independent cross-check of it.

### 5. Resources on every branch — verified at the stated orders

**Time.**
* Filter calls: k(2j+1) ≤ √D. Each call does L record steps. Each step is O(np + w) gates plus
  the shift-and-mask constant extraction, each charged A = O(log n). So C_f = O(n log³ n).
* Full predicate: j·C_v = O(√G · n² log² n). By (8), √G ≤ 64 + 4√D/(n+2)², so this term is
  O(√D log² n). I checked 2^(4d) ≥ (n+2)⁴ exactly.
* Reflections: O(√D · n log n).
* Index generation: O(L · r · log Q) = polylog(n).
* Acquisition: O(n³ log² n), which is o(2^(n/2) n log³ n).
* Fallback (n < 20): constant work.
* Total: T = O(2^(n/2) n log³ n) on every branch. Every loop length depends only on (n, N), and
  index generation is capped.

**Classical space.**
* Records: Q(n + p + 4) = O(n²) bits.
* Indices: L·ceil(log₂Q) = O(log² n) bits.
* Table: 27·2^24 bits, a constant.
* Loop counters (k, j, l, i): O(n) bits. Reverse streaming reuses the reverse generator that
  ROB-G2 §4.7 step 4 already uses.

**Quantum space.** n search qubits, plus the O(log n) accumulator/comparator, plus the shared O(n)
pool. The nesting has fixed depth and holds no stored states. Total O(n).

**Accumulator width for the multiset.** With w_f = bitlength(L) + 29:
* |U*| ≤ L(2^26 + 1) < 2^(w_f − 1).
* |Θ_f + 1| < 2^(w_f − 1).

I checked both exactly for n ∈ [20, 2000] ∪ {10⁴, 10⁶} (part C).

**Samples.** Exactly Q copies on every branch. The fallback reuses the same records.

**Fallback.** ROB-G2 Theorem 2 applies to the same records and gives success ≥ 49/64 for n < 20.
Its loops are bounded: at most 3 repetitions.

### 6. Diagnostics and comparison scope — confirmed as stated

* `check.py` replayed from my copy in `review/replay/`. It exits 0, and its `results.json` is
  identical to the parent's apart from `python` and `cpu_seconds`.
* The checker's circuits are small Boolean-oracle circuits, not emitted score circuits. They do not
  replay the source count, and they are not a frontier verification. PROOF.md and README.md both
  say so correctly.
* PFD-N1's n+1 cap is not preserved, and the text says so.
* See S1 for a comparison caveat that README.md does not mention.

### 7. Uniformity, noise model and implementation — no gap

* All parameters are integers computable from n in poly(n) bit operations. There is no real
  arithmetic, and the only rotations are exact Clifford+T.
* The noise model is verbatim, and its hash matches.
* The only implementation detail left unstated is R2 below, and that is a specification gap, not
  a correctness gap.

## Findings

**R1 (minor, PROOF.md §1 interface and §5, "The event G_0 … supplies …").** 𝒢₀ is defined using
the compensators m_j(t) = E[Z̃_j(t) | H_{j−1}]. These depend on the adversary's private outcomes,
so 𝒢₀ is not a function of the record string alone. §2 nevertheless conditions on "any record
string in E".

*Repair:* define E := {record string r : (1) holds for r}. This event is record-measurable, and
E ⊇ 𝒢₀, so P(E) ≥ P(𝒢₀) > 7/8. Every later step uses only property (1) of r together with the
fair bits, which are independent of (records, adversary). The proof is otherwise unchanged.

**R2 (minor, PROOF.md §4, "the same explicit signed-score comparator … applies").** The filter
oracle O_f is described only by reference to ROB-G2 §4.7, "for both list lengths". The text should
spell out the substitutions:
* loop over l = 1..L, using record I_l (with multiplicity);
* n₀, n₁ counted over the multiset;
* C*_f = 6667·2^25·L + 40000(2^25 + 1)(n₀ − n₁) and Θ_f = ⌊C*_f/40000⌋, computed classically once
  per run;
* w_f = bitlength(L) + 29;
* the step-(e) and step-4 reversals iterate l = L..1.

My part C confirms the widths. This is a specification gap, not an error.

**R3 (minor, PROOF.md §5, "the table range in its Lemma T ensures …").** Add one line saying that
|c_k| ≤ 2^25 gives |Z̃| ≤ 1, which is sharper than ROB-G2's own Lemma B (|Z̃| ≤ R). A reader
checking against Lemma B would otherwise see a width of 2R, not 2, in the Hoeffding step.

**R4 (minor, PROOF.md §3, "x−2<=q<=x").** The text should state the derivation: q ∈ {X, X−1}
with X = isqrt(2^m) > x − 1. It should also state the analogous derivation for 2j+1 from isqrt(G)
when b is odd. Both are correct (part B), but the text only asserts them.

**R5 (minor, PROOF.md §1 and §3).** Say explicitly that the measured output t̂ is returned without
a classical recheck, and that the 7/8 readout factor is conditional on (r, list) ∈ E ∩ F. Then
state the product (6) as an explicit iterated conditioning. The arithmetic is correct as written:
395079601/536870912 ≈ 0.7359.

**S1 (scope, README.md "Current comparison").** `compare.py` skipped 91 same-context valid rows.
All 91 have vanishing tolerances, for example 1/(8n) and log n/(224n³). README.md reports only
"34 comparable rows". Because their tolerances go to 0, these rows cannot be equal or better than
a constant 3333/10000, so the "no blocker" statement is unaffected. README.md should still say
they were excluded and why.

I did not re-verify the comparator, the server frontier or exhaustiveness. The snapshot hash
matches `comparison.json`.

**S2 (novelty and citation obligation, PROOF.md §6).** The search lemma is a nested
amplitude-amplification scheme: a cheap randomized prefilter inside an outer search with the
expensive predicate. It should cite at least the following, and should frame its novelty as the
DCP application, the fixed-schedule rational certificate and the adaptive-model compatibility,
not as a new search primitive:
* Brassard–Høyer–Mosca–Tapp, "Quantum amplitude amplification and estimation" (2002), for
  reflection about V|0⟩;
* Cerf–Grover–Williams, "Nested quantum search and structured problems", PRA 61 (2000).

Not a mathematical gap.

**I1 (informational, constants).** L = 1.25·10^11·(4⌈log₂(n+2)⌉ + 8) exceeds Q = 2^33(n+4) for
every n < 695 (part E). Below that size the "filter" reads more records, with repetition, than the
full test does. This is harmless for the asymptotic theorem, but any intuitive or practical
"cheap filter" wording would be false in that range. PROOF.md already disclaims a practical
crossover, so this is fine as is.

## Exact scope of my verification

* **Proved by hand (analytic):** PROOF.md §§1–5 in full, against ROB-G2 §§2, 4.1–4.7, 5, 6.1–6.3
  and 7 as copied in `sources/`. I did not re-audit ROB-G2's own Lemmas P, C, K, M, A, T and
  Theorem 1 from scratch. I read them, checked that the parent's use of them matches their exact
  statements, and spot-checked their constants (the gap and the table extremes).
* **Exact rational and integer diagnostics** (`review/independent_check.py`, written
  independently, standard library only, 6.6 CPU s; results in
  `review/independent_results.json`):
  * gap constants;
  * table extremes;
  * the uniform rational chain and the success product;
  * all schedule premises for n ∈ [20, 20000];
  * multiset accumulator/comparator widths and sampler bounds for n ∈ [20, 2000] ∪ {10⁴, 10⁶};
  * the L-versus-Q crossover.
* **High-precision numeric diagnostic:** the reduced-space simulation of the actual operator word
  for n ∈ [20, 160]. These are floating-point Decimal results, so they are diagnostics, not
  certificates.
* **Replay:** the parent's `check.py`, from the copy in `review/replay/` (outputs in
  `review/replay/results.json` and `review/replay/replay-stdout.txt`). It passes, with results
  identical to the parent's.
* **Not done:** no production score circuit was emitted or simulated; there was no source-count
  replay and no hardware or proof-assistant check. I did not re-verify the comparator or the
  frontier, and did no literature or novelty search beyond S2.
