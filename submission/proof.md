# Critically sampled exhaustive shift testing

This is a correctness/format submission in the same family as the included
exhaustive baseline. It uses **one** algorithm and one parameter choice for the
four resource claims and the tolerance claim. It does not claim research
progress toward 2^{O(n^{1/3})}; it proves a total-work expression strictly
tighter than the baseline's O(N n⁴) while keeping the same coarse index.

## Setup, hypotheses, and model

- For every integer N ≥ 2 and every fixed unknown s in Z/NZ, the source supplies
  fresh independent copies of
  ρ_s = (1/N) Σ_{x=0}^{N−1} |ψ_{x,s}⟩⟨ψ_{x,s}|,
  |ψ_{x,s}⟩ = (|0,x⟩ + |1,(x+s) mod N⟩)/√2. Write n = ceil(log₂ N).
- The challenge model is used exactly (rules.md): a uniform classical
  controller, a Clifford+T quantum circuit, computational-basis measurement,
  fresh |0⟩ qubits, no advice, no postselection, no inverse preparation, no
  purification, no coherent source control. This is
  `dcp-uniform-clifford-t-bit-operations-v1`. Every acquired source copy costs
  n+1 work units, and every classically addressed access/gate additionally pays
  ceil(log₂(M+2)) bit operations for M allocated bits and qubits.
- These are hypotheses of scope and cost accounting, not of the algorithm's
  correctness. Success is unconditional over the source randomness and the
  algorithm's coins.

## The algorithm

Fix the measurement count k = n + 3 (a single parameter choice). For
t = 0, 1, …, N − 1:

1. Acquire k fresh independent copies of ρ_s.
2. Apply the controlled modular subtraction of t,
   U_t = Σ_y (|0⟩⟨0| ⊗ I + |1⟩⟨1| ⊗ |y − t mod N⟩⟨y|),
   to each copy; U_t sends ρ_s to ρ_{s−t}. It is a unitary because y ↦ y − t is
   a permutation of Z/NZ composed with a control (see "Implementing …").
3. Measure the control qubit of each of the k copies in the X basis; record
   m_t = (m_{t,1}, …, m_{t,k}) ∈ {0,1}^k, writing "+" for outcome 0.
4. Accept the candidate when m_{t,j} = "+" for **every** j = 1, …, k: output t and
   halt. (Acceptance requires all k control outcomes to be "+"; this is the exact
   event the correctness proof below charges.)

If no candidate is accepted, output the least t with the most "+" outcomes in
m_t. This fallback branch makes the algorithm total; under an ideal source the
correct candidate yields all k outcomes "+" (probability 1) and is therefore
accepted, so the fallback is reached with probability 0.

Only the first candidate (in increasing t) whose k outcomes are **all** "+" is
accepted; the scan stops there. The algorithm is fully specified by steps 1–4
and this fallback rule. Note that the correctness argument below uses exactly
this all-k acceptance event: an earlier wrong candidate is accepted only if all
k of its outcomes are "+".

## Correctness

**Per-copy marginal law.** After U_t and the X-basis measurement on the control,
a single copy whose component has offset x behaves as follows.

- If t = s then (x − t) mod N = x, and the copy is |+⟩|x⟩ with
  |+⟩ = (|0⟩+|1⟩)/√2, so the outcome is "+" with probability 1.
- If t ≠ s then (x − t) mod N ≠ x, so the two second-register kets |x⟩ and
  |(x − t) mod N⟩ are distinct computational-basis states and hence orthogonal.
  The joint state is (|0,x⟩ + |1,x′⟩)/√2 with x ≠ x′, an entangled state whose
  control marginal is I/2; measuring it in the X basis returns "+" with
  probability exactly 1/2.

This holds for every x; since the source is the uniform mixture over x and the
copies are independent, the k control outcomes are independent Bernoulli with
per-copy success probability p = 1 if t = s and p = 1/2 if t ≠ s.

**Acceptance bound.** The correct candidate t = s is accepted with probability 1.
For any t ≠ s with t earlier than s (so t < s), acceptance requires all k
recorded bits to be "+", an event of probability 2^(−k) = 2^(−(n+3)). The union
bound over the at most s ≤ N − 1 incorrect earlier candidates gives

  Pr[a wrong t is accepted before s] ≤ (N − 1)·2^(−(n+3)) ≤ (2^n − 1)·2^(−(n+3))
  = (1 − 2^(−n))/8 < 1/8, using k = n+3 and N ≤ 2^n.

Therefore the algorithm outputs the entire s with probability
> 1 − 1/8 = 7/8, in particular > 2/3, for every N ≥ 2 and every s. This is
unconditional; no postselection is assumed and the failure event is fully
charged. (A naïve k = n+2 gives only (1 − 2^(−n))/4 < 1/4 and succeeds with
probability > 3/4; the extra copy buys the uniform 7/8.)

## Implementing the controlled subtraction

On n-bit strings define f_t(y) = (y − t) mod N for y < N and f_t(y) = y for
y ≥ N. This is a permutation of the n-bit register; its inverse is conditional
addition of t modulo N on the same valid range, which makes the extension a
unitary even when N is not a power of two.

Comparisons and addition/subtraction with carry are Boolean circuits of O(n)
gates and O(n) temporary wires: each comparison and each arithmetic operation is
a single bit scan retaining the carry/borrow. Comparing with N and with t, and
selecting between y − t and y + N − t, is a fixed number of such operations on
n+1 bits; an n-bit result is kept and the valid modular result is below N.

Reversible evaluation retains each gate's value in a fresh bit, XORs the result
into a target register, then reverses all gates to clear intermediates. NOT,
CNOT and Toffoli realise these steps, and Toffoli has an exact constant-size
Clifford+T decomposition. For a permutation, compute f_t into a zero register,
swap registers, and XOR f_t^{−1} of the new first register into the old input,
clearing that old input. The identity on control 0 and f_t on control 1 gives
the required controlled permutation, and the same control drives the inverse
computation. The X-basis measurement is a Hadamard followed by a
computational-basis measurement.

## Charged cost of one candidate test

- The emitted circuit has O(n) gates and O(n) ancillas; fixed-size logic is unit
  cost. Each gate's wire index is classically addressed, so the gate description
  costs O(1) bit operations per gate plus ceil(log₂(M+2)) = O(log n) per address,
  with M = O(n²) allocated bits and qubits. Writing and interpreting the O(n)-gate
  description is O(n log n).
- Acquiring and initialising the k = n+3 fresh copies costs k(n+1) = O(n²) work
  units (source) and initialises O(n) qubits per copy.
- The classical generator holds the at-most-(n+1)-bit constants N and t and a
  binary counter of O(log n) bits, and its temporary-wire budget is O(n²).

Hence one candidate test is O(n² log n) bit operations — the O(n²) emitted gates
each pay a classically-addressed-gate charge of ceil(log₂(M+2)) = O(log n) for
M = O(n²) allocated bits and qubits — and O(n²) allocated classical bits, with
O(n²) qubits and no stored exponential circuit or lookup table. (The tighter
working-qubit count is O(n); the conservative O(n²) covers all copies, ancillas
and the generator's scratch.)

## Joint costs and indices

All k copies are discarded before the next candidate and the workspace is reused,
so the single algorithm obeys these uniform worst-case bounds:

- T(N,s) = O(N n² log n) bit operations (at most N tests, O(n² log n) each).
- S_C(N,s) = O(n²) classical bits (generator registers and circuit description).
- S_Q(N,s) = O(n²) qubits (conservative; working registers are O(n) per copy).
- Q(N,s) ≤ N(n+3) = O(2^n n) fresh copies, counting every test, failed copies
  and discarded copies.

All hidden constants are absolute; enlarging them covers the finitely many small
bit lengths. These are upper bounds, not tight resource estimates.

**Indices.** With g(B) = limsup_{n→∞} log₂(log₂ max{4,B(n)}) / log₂ n from
rules.md:

- B_T(n) = 2^n n² log₂ n: log₂ B_T(n) = n + 2 log₂ n + log₂ log₂ n, so
  g(B_T) = 1.
- B_C(n) = B_Q(n) = n²: log₂ B(n) = 2 log₂ n, so g(B_C) = g(B_Q) = 0.
- B_samples(n) = 2^n n: log₂ B_samples(n) = n + log₂ n, so g(B_samples) = 1.

Fixed multiplicative constants do not change any limit. The four resource
indices are [1, 0, 0, 1]; only time is a numeric objective, so the published
score vector is [1]. The tighter N-dependent time O(N n² log n) and sample
N(n+3) expressions remain in the claim statements, and Q is independent of how
little quantum workspace is retained, per rules.md.

## Fractional error tolerance

The correctness argument and all four bounds above assume that every acquired
copy is an independent ideal coset state ρ_s. Under that promise the same
algorithm and parameter choice (k = n+3, one pass, worst-case time O(N n² log n),
classical and quantum workspace O(n²), at most N(n+3) copies) recovers the whole
s with probability > 7/8 > 2/3 for every N and s.

We therefore declare the guaranteed malformed-sample fraction ε(n) = 0. No
malformed copy is admitted by the proof: replacing an ideal copy by a random
bit/value drives the per-copy "+" probability under the correct candidate from 1
to at most 1/2, which the union-bound argument does not control. This states the
clean-input guarantee; it does not prove that the algorithm's maximum tolerable
fraction is zero, and no positive tolerance is claimed or scored.

The error model: the compared quantity is the fraction of malformed copies among
the Q acquired copies; every non-ideal copy is treated as arbitrary (adversarial)
unless ideal, and Q counts every acquired copy including discarded and
failed-attempt copies. Zero means exactly the clean-input guarantee above.
