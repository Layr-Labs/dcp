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
claims are claims for T, S_C, S_Q in that order. Under the default required
mode, every submission must supply all three supported structured bounds and
exact nonnegative rational indices, including partial, unscored and validity-only
submissions. The protected optional mode permits the limited exceptions below.
Each `statement` must name the same algorithm/configuration, give the full
proved upper-bound expression, define every parameter/quantifier, and state
its exact numerical growth index. Reference the proof through `evidence`;
store a proof once and share its path between claims.

Preserve detail actually established: polynomial degrees, log factors,
coefficients, leading constants and validity thresholds when known. Use big-O
when that is all the proof gives; never manufacture finite-size constants.
Non-power expressions and sums are allowed. Define their meaning in the proof;
expressions are reviewed mathematical text, never executable code. Structured
declarations below are a separately reviewed representation of the same
guarantee, never an automatic interpretation of that text. In required mode,
the full guarantee must also have a supported structured representation.

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
strings. In optional mode only, work whose index cannot be established as a
finite rational may remain unscored. Required mode rejects incomplete declarations
before review; setting allow_unscored or selecting validity-only does not waive it.

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
and structured guarantees are exported in `metrics.dcp`
when supported; all original scores and declarations remain in the immutable
dossier. In optional mode, unsupported structured forms have an explicit
omission record retaining the statements, scores and evidence. In required
mode, missing or unsupported declarations cause format rejection before review. These full claims are the record of what
was proved.

Every declared claim must be established exactly as written before a numerical
vector is published. The reviewer returns `scores: null`; the shared verifier
derives a one-element numeric vector from the time claim only after atomic
acceptance. The three original resource claims and their indices remain mandatory
for every required-mode submission and every optional-mode scored result;
neither memory claim is an independent numeric objective.
One proof may establish all three statements. Do not combine
configurations, accept a subset, or accept just the numeric part of a statement
whose stronger expression is unsupported. Source hashes record provenance;
they are not acceptance selectors.

## Structured reviewed envelopes (dcp-bounds-v3)

The protected review standard is `dcp-joint-bounds-v3`; the validity selector is
`{"version":"dcp-joint-bounds-v3","structured_bounds":"required"}` at launch.
The scoring policy stays `dcp-time-growth-v2`. The verifier opts into
`structured_claims: "atomic-v1"`. The organizer may switch to optional mode using
`python configure_bounds.py --mode optional`, which synchronizes the verifier's
default and sole supported validity selector with the challenge manifest. Only
one mode may be registered. Participants cannot override it in submission data
or an evaluation selector. Returning to required uses the same command with
`--mode required`; either semantic change needs its corresponding policy identity.
Historical `dcp-joint-bounds-v2` intakes retain their original optional semantics.

Each of the first three claims must declare a `structured` object in required
mode, and may do so in optional mode, with exactly
`version`, `comparator`, `scope`, `model`, `notation`, and `bound`:

- `version`: `dcp-bounds-v3`; `comparator`: `asymptotic-v1`.
- `scope`: `dcp-cyclic-group-order`, meaning every N and s under the problem
  above, with n = ceil(log₂ N), not N itself.
- `model`: `dcp-uniform-clifford-t-bit-operations-v1`, meaning all the charged
  work, addressing, source, and peak-space conventions above.
- `notation`: `big-o`, because these claims prove R = O(B). An explicit outer
  constant is not a measured improvement when the guarantee is big-O.

The supported envelope family is

$$
B(n)=C\,2^{\sum_i a_i n^{p_i}(\log_2 n)^{q_i}}n^r(\log_2 n)^s.
$$

`bound` has exactly `coefficient` (C), `exponent` (a list of terms), `nPower`
(r) and `logPower` (s). Each term has exactly `coefficient` (a), `nPower` (p),
and `logPower` (q). All numbers are signed integer or p/q strings with positive
denominators, at most 256 decimal digits per integer. C must be positive. At
most 64 terms are supported. Each term requires p > 0 with rational q, or p = 0
with q > 0. Terms (p,q) = (0,1) fold into the outer nPower. Equal powers combine
and zero terms cancel using exact rational arithmetic. Big-O canonicalizes C to
1; this is a representative envelope, not a claim that its hidden constant is 1.
For example O(2^{sqrt(n)} n²) is declared as:

```json
{"coefficient":"1","exponent":[{"coefficient":"1","nPower":"1/2","logPower":"0"}],"nPower":"2","logPower":"0"}
```

The reviewer must explicitly establish that each structured object describes
its complete original statement and evidence for the same algorithm and joint
configuration. The review acknowledges the digest of all structured claim
records, including both memory claims. The producer verifies the dossier and
that acknowledgment before projecting, checks the exact g(B) against each
resource index, and performs only the declared rational normalization above.
No coefficients, exponents, scope or cost model may be supplied by inference
from prose, participant hints, or a numeric score. A hash provides provenance,
not reviewer authentication; the trusted organizer artifact channel is required.

An unknown inner coefficient, for example 2^{O(sqrt(n))}, is unsupported: do
not replace O() by 1. Required mode format-rejects it before paid review. In
optional mode only, such a claim can still be reviewed as mathematical text with
its exact index: omit its structured declaration, or retain a generically valid
unsupported object in reviewed data. The producer then emits
`metrics.dcp_omission` with an explicit reason and all three reviewed claims/evidence
instead of a `metrics.dcp` v3 row.
Mismatched review evidence, scope/model/notation, or a conflicting exact growth
index is rejected. A rejected, unscored, validity-only or simulated evaluation
cannot supply a frontier entry.

Official DCP admission checks only declared shape, supported domain and exact
index consistency; it does not establish mathematical truth. Expected format
errors produce a typed `DCP format rejection` with `valid:false`, `scores:null`
and `metrics.dcp_admission`, plus a separate replayable admission receipt. They
skip the verifier and do not create an LLM dossier. Validity-only requests omit
scores; score-only invalid requests fail closed rather than silently nulling an
old validity. Configuration, checkout, I/O or unexpected runtime faults remain
failed evaluations without a rejection score. Supported declarations proceed to
the actual joint mathematical review. Local preparation and finalization use
`dcp_admission.py`; the generic verifier CLI alone does not enforce DCP admission.
The exporter rechecks the exact retained intake under its original policy,
including unscored or invalid dossiers, before publishing a score.

Existing `dcp-bounds-v2` evidence and its three numeric objectives remain
historical; they are not converted or re-reviewed by this change. Missing or
unsupported structure excludes an entire joint-bound row from the structured
frontier, never an artificial zero or a tie.

## Validity and comparison

A scored submission needs a complete algorithm, proof of full-secret recovery,
success bound, and joint resource analysis in this model. Heuristic distribution
assumptions, unproved lemmas, numerical experiments, or a reduction with an
unaccounted subroutine cannot establish a scored result. A relevant, correct,
explicitly scoped partial theorem may be valid with null scores in a separate
optional-mode submission whose claims state that limited scope. Required mode
still demands all three supported resource claims on every submission; a partial
theorem without them is format-rejected before review. State unresolved obligations;
do not promote them into assumptions of a full DCP solution or use review
commentary to narrow an unsupported declared claim.
Citations must identify exact theorems/versions and explain applicability.
Provide the argument needed for review in the snapshot; the reviewer cannot
fetch external material.

The Pareto backend uses one minimizing time-growth objective. Its numerical
order is a coarse UI summary; equal-time and slower-time/lower-memory accepted
submissions still carry their independent evidence. The configured Complexity
frontier compares all three supported structured guarantees under exactly the
same version, scope, model and notation. Scientific comparison and manual
promotion use the full proved bounds. Establish
an asymptotic no-worse relation for each resource and a strict improvement in at
least one before declaring dominance. Unknown constants or incomparable bounds
may prevent this conclusion. Never infer equivalence from equal indices. The
versioned comparator orders only its supported exact envelope family; it does
not order arbitrary prose or resolve unknown constants. Compare guarantees,
not unknown optimal running times.
An equivalent rewrite or deliberately loosened prior claim is not new research
progress. Verify novelty against established results separately from validity.

The original motivation is Dan Boneh's DCP problem in
[the Yukon collection](https://app.notion.com/p/eigen-labs/Problem-statements-from-Cryptographers-for-Yukon-3f813c11c3e0800d9f2bf6c474d38a7e).
The scope and conventions above govern this challenge.
