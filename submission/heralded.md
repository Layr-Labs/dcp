# RQ-D32-H: heralded filter and heralded tolerance (companion to proof.md)

This file is part of the submission and is evidence for all five claims. It carries the whole
heralded section: the exact error model of the fifth claim, the filter FILTER, the literal
copy caps Q*, two lemmas, the success and resource theorem, and the tolerance integers.

## H.0 Reading rule

The algorithm is the unchanged RQ-D32 algorithm of proof.md, in which every source
acquisition is one call of FILTER (H.2). This covers the 7 copies of n = 1, the copies of the
finite exhaustive protocol (2 <= n < 64), and, for n >= 64, every EXTRACT copy, every NODE_0
acquisition, every rejected, discarded or failed-attempt copy and every partially built
collection. All copy counters and guards of proof.md (Q, Qcap, the source guard, the n+8 tests
per candidate of the finite protocol) count copies HANDED OVER by FILTER; the level counters
count NODE attempts and are unaffected. The words "raw" and "RAW" in proof.md ("accepted RAW demand", "RAW supplier qubit")
mean handed-over copies before the base's own acceptance step; only FILTER's counter r of H.2
counts raw copies. The algorithm reads only the handed-over copies and never the herald, so
its control flow is that of the unflagged algorithm on the same copies. ModelM of proof.md
Section 0.1, its analysis (Section 5 onward) and the unflagged guarantee
epsilon_u(n) = 1/(8 n^32) with tolerance floor(Q/(8 n^32)) are proved there, verbatim, but
are NOT claimed here; the fifth claim is the heralded tolerance of H.6. Sentences of proof.md
that reason from epsilon_u (for example "epsilon(1) Q = 7/8 < 1, so no copy is replaced" in
Section 8) are statements about ModelM; under the heralded model the corresponding fact is
Lemma H.2. When copies carry no herald bit, FILTER is the identity and the algorithm is
exactly RQ-D32.

## H.1 Error model of the fifth structured claim (exact text)

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

Let x = 10^64 - 3 = 9999999999999999999999999999999999999999999999999999999999999997, D = x^4 and epsilon_H = 1 - 1/D. D is a fixed absolute integer
(log2 D < 851).

## H.2 FILTER and the literal copy cap Q*

**Q*.** Q*(n) is the hard cap on the number of source copies the algorithm acquires on every
branch, counting all retries, rejections, discards and failed attempts:

* n = 1: Q* = 7 (proof.md Section 8: exactly 7 originals);
* 2 <= n <= 63: Q* = 8 n^32. The finite protocol acquires at most n+8 copies per candidate t
  and has N <= 2^n candidates, so Qactual <= N(n+8) < 8 n^32 (proof.md Section 8);
* n >= 64: Q* = Qcap = 2^107 rbound^32 K with H = ceil(n/33), rbound = H+1,
  K = 2^32 (n + 36 ceil(log2 n) + 256) (proof.md Section 4). The source guard runs before
  every acquisition: at Qcap it aborts without another copy, otherwise it acquires and
  increments once, so Q <= Qcap on every branch.

In all three cases the algorithm never requests more than Q*(n) copies, on every branch. Also
Q*(n) <= C n^33 for an absolute constant C (proof.md Section 9: Qcap = O(n^33); for
n >= 64, rbound <= n/16 and n + 36 ceil(log2 n) + 256 <= 9n).

**FILTER.** One source acquisition is served as follows: acquire one raw copy into the
(n+1)-qubit acquisition slot of the base and read its herald bit f; if f = 1, reset that slot
to |0> in place, without any other operation, and acquire again; otherwise hand the register
to the caller as the copy. When copies carry no herald bit, FILTER is the identity. A
classical raw counter r enforces the literal cutoff D Q*(n) on every branch: if the next raw
acquisition would make r exceed D Q*(n), stop and output 0.

## H.3 Lemma H.1 (the cutoff never binds)

Under the heralded model with fraction epsilon_H, the cutoff D Q* is never reached while a
copy is awaited. Consequently every FILTER call completes, and every call the base makes
returns a handed-over copy.

*Proof.* Suppose the cutoff is reached while the base awaits its copy number j. By H.2 the
base requests at most Q* copies, so j <= Q*. Then j - 1 <= Q* - 1 well-formed copies were
handed over, D Q* raw copies were acquired, and at least D Q* - Q* + 1 of them are
malformed. The promise on this branch, with Q = D Q* raw acquisitions, gives at most
floor((1 - 1/D) D Q*) = D Q* - Q* malformed copies, a contradiction. The argument needs only
that the base never requests more than Q* copies, which its own hard caps guarantee. ∎

## H.4 Lemma H.2 (clean law)

Under the heralded model, the joint law of every measurement outcome of RQ-D32 with FILTER and
of its output equals that of the clean problem of ModelM: Q ideal copies rho_s, requested one at
a time and delivered fresh, with no replacement.

*Proof.* A malformed register is reset without interacting with any algorithm register, so it
is traced out; whatever the adversary does on its private system and on malformed registers
acts on systems disjoint from the algorithm's, and the algorithm reads neither the herald nor
r. Each well-formed copy is, at delivery, a fresh rho_s in tensor product with every other
system, irrespective of the adversary's adaptive decisions; the algorithm's own coins and
bases are drawn after delivery as before. By induction over the handed-over index j, the
handed-over copies are distributed exactly as independent ideal copies delivered on request,
which is the clean problem, i.e. the no-replacement strategy of proof.md Section 0.1 ("Clean
input is the no-replacement strategy"). By Lemma H.1 the extra cutoff never changes the run. ∎

## H.5 Theorem H.3 (success and resources)

Under the heralded model with fraction epsilon_H, for every N >= 2 and every s, RQ-D32 with
FILTER outputs the entire s with probability at least 1 - 2^-8 > 2/3, and on every branch
T = O(2^(n/64)), S_C = O(n^2), S_Q = O(n), the number of copies handed over is at most Q* =
O(n^33), and the number of raw copies acquired is at most D Q* = O(n^33).

*Proof.* *Success.* By Lemma H.2 the run is a run of the clean problem. Every success proof of
proof.md (Section 8 for n = 1, for 2 <= n < 64 and for n >= 64, with Sections 3-7) was proved
for every admissible strategy of ModelM including the no-replacement strategy, and that is
the only case needed: with zero replacements the budget inequalities used there (for example
Bbad <= Qactual/(8 n^32) and at most K/128 edits per level) hold trivially, so the clean case
gives failure at most 2^-8.

*Copies.* By the literal cutoff at most D Q* raw copies are acquired on every branch, and
D Q* <= D C n^33 with D, C absolute constants. Handed-over copies are at most Q* by H.2.

*Time.* Each raw copy costs the base's source charge of O(n) (n+1 qubits), one herald read, a
reset of n+1 qubits when malformed (O(n) operations), and an increment and comparison of r.
Every indexed action pays the address charge A = O(log(S_C+S_Q+2)) = O(log(n+2)) of proof.md
Section 1, so a raw copy costs O(n log(n+2)). The counter r has bitlength(D Q*) <=
851 + 107 + 32 bitlength(rbound) + bitlength(K) = O(log n) bits. The extra work is
therefore O(D Q* n log(n+2)) = O(n^34 log(n+2)) with an absolute constant. Polynomial
growth is below exponential growth: n^34 log(n+2) / 2^(n/64) -> 0, so n^34 log(n+2) <= C' 2^(n/64)
for an absolute constant C' and all n >= 1. The base time on the handed-over copies is
T_base = O(poly(n) 2^(n/66)) = O(2^(n/64)) (proof.md Section 9), so
T <= T_base + extra = O(2^(n/64)); the exponent 1/64 and the growth index 1 are unchanged.
proof.md has no literal work or time cap that aborts: its aborts are the fixed trial and
iteration caps, the 32 level guards and the source guard, which count copies and attempts and
never operations. FILTER's work is charged outside every base counter and changes no branch of
the base, so no cap argument of proof.md is affected.

*Space.* The classical space grows by the O(log n) bits of r and one herald bit, so S_C = O(n^2);
all counters and fields of proof.md keep their orders. A malformed register arrives in the
(n+1)-qubit slot that the base already reserves for an acquired original (counted in S_Q =
O(n), proof.md Section 9) and is reset in place before the next acquisition. Even a separate
extra (n+1)-qubit slot would keep S_Q = O(n). All other steps run exactly as in proof.md on the
handed-over copies, so the four bounds hold jointly on every branch. ∎

## H.6 Fifth claim: tolerance integers

The fifth claim is epsilon_H = 1 - 1/x^4 under the heralded model of H.1. The displayed
integers t_i satisfy t_1 ... t_3 = x^2 + 1 exactly (direct integer multiplication; they need
not be prime):

    t_1 = 5909009547859618446014307935656485996455360061473289284034355157
    t_2 = 8461654968574415353741992088106541809421651544931744139485636465
    t_3 = 2

Each of x - 1, x, x + 1 and every t_i has at most 64 decimal digits. The supported expression

    9999999999999999999999999999999999999999999999999999999999999996*9999999999999999999999999999999999999999999999999999999999999998*5909009547859618446014307935656485996455360061473289284034355157*8461654968574415353741992088106541809421651544931744139485636465*2/9999999999999999999999999999999999999999999999999999999999999997^4

equals (x - 1)(x + 1)(x^2 + 1)/x^4 = (x^4 - 1)/x^4 = 1 - 1/x^4 = epsilon_H, a constant in
(0, 1), with normalized numerator and denominator of 256 digits. This guarantee covers
detectable (heralded) malformed copies only; no tolerance of undetectable corruption is
claimed in the fifth claim, and the unflagged guarantee floor(Q/(8 n^32)) of ModelM is proved
in proof.md but not claimed.
