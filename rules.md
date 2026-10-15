# DCP: proved time and memory bounds

## Problem and goal

For every integer N ≥ 2, the algorithm receives N in binary and fresh independent
copies of the mixed state below, for one fixed unknown s in Z/NZ:

$$
\rho_s=\frac1N\sum_{x=0}^{N-1}|\psi_{x,s}\rangle\langle\psi_{x,s}|,\qquad
|\psi_{x,s}\rangle=\frac{|0,x\rangle+|1,(x+s)\bmod N\rangle}{\sqrt2}.
$$

Set n = ceil(log₂ N). The value x, a purification, an inverse preparation circuit,
and coherent control of the source are unavailable. Output the entire s with
unconditional probability at least 2/3, for every N and s.

The research goal is total work 2^{O(n^{1/3})}. Here n is the residue bit length, not the
modulus. A time growth index of 1/3 alone does not establish this goal: for
example, 2^{n^{1/3} log₂ n} has that index but does not meet the stated bound.
The included exhaustive-search submission is a correctness/format baseline, not
a claim of research progress or the best known algorithm.

## Computation and resources

Use a uniform classical controller and a quantum circuit over Clifford+T, with
computational-basis measurement, fresh |0⟩ qubits, and the specified source.
Classically chosen gates may act on arbitrary indexed wires; no geometric
locality cost is imposed. Quantum-addressed memory access must be implemented
by counted gates. There is no additional QRAM, hidden-shift, or subset-sum oracle.

T is total sequential work, not depth, quantum work alone, or query count.
Count classical bit operations, circuit generation, gates, measurements,
initialization, preprocessing, memory access, precision/gate synthesis, and
all attempts including failures. A source copy costs n+1 work units. A classical
indexed access or classically addressed gate also pays for its address:
ceil(log₂(M+2)) bit operations, where M is the number of allocated bits and
qubits. Fixed-size logic is unit cost; arbitrary integers/real arithmetic are not.
All parallel work is summed. No instance-dependent advice, preloaded tables,
free postselection, or uncharged preparation is allowed.

S_C is peak allocated classical bits; S_Q is peak allocated qubits. Include
inputs, intermediate data, saved samples, lookup tables, ancillas and stored
circuit descriptions. State held by the inaccessible source is excluded.
All three bounds must hold jointly for one fully specified algorithm and
parameter choice, on every execution branch. An expected-time analysis needs
an explicit cutoff/restart argument establishing these bounds while retaining
success ≥ 2/3. Constants are independent of N, s, and sampled outcomes.

## Claims, full expressions, and numerical scores

Participants edit only `submission/`. In `submission.json`, the first three
claims, when scored, are structured claims for T, S_C, S_Q in that order.
Each `statement` must name the same algorithm/configuration, give the full
proved upper-bound expression, define every parameter/quantifier, and state
its exact numerical growth index. Reference the proof through `evidence`;
store a proof once and share its path between claims.

Preserve detail actually established: polynomial degrees, log factors,
coefficients, leading constants and validity thresholds when known. Use big-O
when that is all the proof gives; never manufacture finite-size constants.
Non-power expressions and sums are allowed. Define their meaning in the proof;
expressions are reviewed mathematical text, never executable code.

For an eventually positive representative envelope B(n), define the UI index

$$
g(B)=\limsup_{n\to\infty}
\frac{\log_2\!\left(\log_2\!\left(\max\{4,B(n)\}\right)\right)}
{\log_2 n}.
$$

For each resource, the claim must prove R(n) = O(B(n)) uniformly over instances
of bit length n, and prove the stated value of g(B). It need not prove a matching
lower bound on the algorithm's actual resource usage. For a bound containing
unspecified fixed constants, the index must have the same value for every
admissible choice of those constants. For example 2^{O(sqrt(n))} gives index
1/2 without choosing the hidden positive constant. Scores are nonnegative finite
**rational** indices, encoded as the verifier's canonical numerator/denominator
strings. If the index cannot be established as a finite rational, retain the
work as an unscored claim.

Examples (all logarithms base two):

| Proved envelope | UI index |
| --- | ---: |
| n², n¹⁰⁰, (log n)³ | 0 |
| n^{log n} | 0 |
| 2^{n^{1/3} log n} | 1/3 |
| 2^{c sqrt(n)} n^k, fixed c > 0 and k | 1/2 |
| 2^n | 1 |
| 2^{n²} | 2 |

Zero does **not** certify polynomial resources. Finite-prefix fitted slopes,
limits that discard troublesome subsequences, and guessed hidden constants are
not scores. Distinct bound expressions can share an index. Accepted statements
and exact rational scores are exported together in `metrics.dcp`; these full
statements are the record of what was proved.

All three resource claims must be accepted before a numerical vector is
published. The reviewer returns `scores: null` and accepts the framework's
snapshot-bound claim IDs; the shared verifier derives the numbers. Accept an
ID only after checking the entire statement, including its bound and index.
One proof may establish all three IDs. Do not combine configurations or accept
just the numeric part of a statement whose stronger expression is unsupported.

## Validity and comparison

A scored submission needs a complete algorithm, proof of full-secret recovery,
success bound, and joint resource analysis in this model. Heuristic distribution
assumptions, unproved lemmas, numerical experiments, or a reduction with an
unaccounted subroutine cannot establish a scored result. A relevant, correct,
explicitly scoped partial theorem may be valid with null scores. State unresolved
obligations; do not promote them into assumptions of a full DCP solution.
Citations must identify exact theorems/versions and explain applicability.
Provide the argument needed for review in the snapshot; the reviewer cannot
fetch external material.

Numerical Pareto order is a coarse UI summary. Scientific comparison and manual
promotion use the full proved bounds under this same scope and model. Establish
an asymptotic no-worse relation for each resource and a strict improvement in at
least one before declaring dominance. Unknown constants or incomparable bounds
may prevent this conclusion; never infer equivalence from equal indices or
invent a total order. Compare guarantees, not unknown optimal running times.
An equivalent rewrite or deliberately loosened prior claim is not new research
progress. Verify novelty against established results separately from validity.

The original motivation is Dan Boneh's DCP problem in
[the Yukon collection](https://app.notion.com/p/eigen-labs/Problem-statements-from-Cryptographers-for-Yukon-3f813c11c3e0800d9f2bf6c474d38a7e).
The scope and conventions above govern this challenge.
