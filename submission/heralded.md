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
  K = 2^13 rbound (proof.md Section 8).

**FILTER.** Every source acquisition requested anywhere in the algorithm is served as
follows. Acquire one raw copy and read its herald bit f. If f = 1, reset its n+1 qubits to
|0> without any other operation and acquire again. If f = 0, hand the register to the
requesting step. A classical raw-acquisition counter enforces the literal cutoff Qraw = D Q*
on every branch: if the next raw acquisition would exceed Qraw, stop, release everything and
output 0. Q* still bounds the number of well-formed copies handed to the algorithm; it does
not bound raw acquisitions under the heralded model, which are bounded by Qraw instead.

## H.3 Lemma H.1 (the cutoff never binds)

Under the heralded model with fraction epsilon_H, the Qraw cutoff is never reached before the
algorithm itself stops.

Proof. On either branch the clean algorithm never requests more than Q* copies. Suppose the
raw cutoff is reached while the algorithm still awaits a requested copy, so R <= Q* - 1
well-formed copies have been handed over. Then Q = Qraw = D Q* raw copies were acquired and
Q - R >= D Q* - Q* + 1 of them are malformed. The promise gives at most
floor(epsilon_H Q) = floor((1 - 1/D) D Q*) = D Q* - Q*, a contradiction. QED.

## H.4 Lemma H.2 (clean law)

Under the heralded model, the joint law of every measurement outcome of the algorithm and of
its output equals that of the clean run.

Proof. A malformed register is reset without interacting with any algorithm register, so it is
traced out; whatever the adversary does on its private system and on malformed registers acts
on systems disjoint from the algorithm's. Each well-formed copy is, at delivery, a fresh rho_s
in tensor product with every other system, irrespective of the adversary's adaptive decisions.
By induction over requests, the sequence of handed-over copies is distributed exactly as
independent ideal copies supplied on request, which is the clean problem, and by Lemma H.1 the
extra cutoff never changes the run. QED.

## H.5 Theorem H.3 (success and resources)

Under the heralded model with fraction epsilon_H, for every N >= 2 and every s, the algorithm
with FILTER outputs s with probability at least 1 - 2^-8 > 2/3, and on every branch, counting
every raw acquisition, T = O(2^((1/64) n)), S_C = O(n^2), S_Q = O(n) and
Q <= D Q* = O(n^33); hence the four declared envelopes hold jointly.

Proof. Success: Lemma H.2 and the success proof of proof.md. Resources: by the literal cutoff
at most D Q* raw copies are acquired on every branch, with D an absolute constant, so
Q = O(Q*) = O(n^33). Each raw copy costs n+1, one herald read and, if malformed, a reset of
n+1 qubits, O(n) core steps at the address charge of the computation model, plus an increment
and comparison of the counter. The extra work is O(D Q* n^2) = O(n^35), below the base's
O(2^((1/64)n)) bound for every n >= 64 and an absolute constant on the finite branch; it is
absorbed by an absolute constant. The counter adds O(log2 Qraw) = O(n) classical bits. A
malformed register arrives in the (n+1)-qubit slot that the base already reserves for an
acquired original (counted in S_Q = O(n)) and is reset in place before the next acquisition.
All other steps run exactly as in proof.md on the handed-over copies, so the four bounds hold
jointly on every branch. QED.

## H.6 Fifth claim: tolerance integers

The fifth claim is epsilon_H = 1 - 1/x^4 under the heralded model of H.1. The displayed
integers t_i satisfy t_1 t_2 t_3 = x^2 + 1 exactly (direct integer multiplication; they need
not be prime):

    t_1 = 9999999999999999999999999999999999999999999999999999999999999996
    t_2 = 9999999999999999999999999999999999999999999999999999999999999998
    t_3 = 5909009547859618446014307935656485996455360061473289284034355157
    t_4 = 8461654968574415353741992088106541809421651544931744139485636465
    t_5 = 2

Each of x - 1, x, x + 1 and every t_i has at most 64 decimal digits. The supported expression

    9999999999999999999999999999999999999999999999999999999999999996*9999999999999999999999999999999999999999999999999999999999999998*5909009547859618446014307935656485996455360061473289284034355157*8461654968574415353741992088106541809421651544931744139485636465*2/9999999999999999999999999999999999999999999999999999999999999997^4

equals (x - 1)(x + 1)(x^2 + 1)/x^4 = (x^4 - 1)/x^4 = 1 - 1/x^4 = epsilon_H, a constant in
(0, 1), with normalized numerator and denominator of 256 digits.

## H.6.1 The identity t_1 t_2 t_3 = x^2 + 1, checked without long multiplication

This subsection exists so that the identity above can be confirmed by inspection and by short
exact arithmetic, with no multi-precision multiplication of the 64-digit factors.

**(a) Exact closed forms.** With x = 10^64 - 3,

    x^2 + 1 = (10^64 - 3)^2 + 1 = 10^128 - 6*10^64 + 9 + 1 = 10^128 - 6*10^64 + 10,

a 129-digit number whose decimal expansion has the block form

    1 [63 nines] 4 [63 zeros] 1 0

that is, digit 1 at position 128 (0-indexed), then 63 nines, then the digit 4 at position 64,
then 63 zeros, then the digits 1 and 0 at positions 1 and 0. Equivalently, in base 10^64 it is
the three-limb number (1, 10^64 - 6, 10): the top limb is 1, the middle limb is 10^64 - 6
(which is 63 nines followed by a 4), and the low limb is 10. Direct subtraction confirms
10^128 - 6*10^64 + 10 has exactly this shape, since 6*10^64 = 5*10^64 + 10^64 and the borrow
propagates one limb.

**(b) The product, limb by limb.** Write t_1 = a, t_2 = b. The claimed identity is
2ab = x^2 + 1, i.e. ab = (x^2 + 1)/2 = 5*10^127 - 3*10^64 + 5. Both a and b are odd, so ab is
odd and 2ab is even, consistent with x^2 + 1 being even. Splitting a and b into base-10^32
limbs, a = a_1 10^32 + a_0 and b = b_1 10^32 + b_0, the product has limbs

    ab = a_1 b_1 10^64 + (a_1 b_0 + a_0 b_1) 10^32 + a_0 b_0,

and each of a_1 b_1, a_1 b_0 + a_0 b_1, a_0 b_0 is a product of at most 32-digit integers, so
each is computable exactly by hand or by any 64-bit-safe routine. Carrying the low limb into
the middle and the middle into the high limb reproduces 5*10^127 - 3*10^64 + 5.

**(c) Congruence checks that pin the identity.** The following exact congruences hold and each
is a check on a small modulus, so none requires the full product:

* mod 2: 2ab = 0 and x^2 + 1 = 0, since x is odd.
* mod 5: 2ab = 0 and x^2 + 1 = 9 + 1 = 10 = 0 (mod 5), since x = -3 (mod 5) and 9 + 1 = 10.
* mod 10^27: 2ab = 10 and x^2 + 1 = 10. This is the check the board's rejection of the
  earlier submission b67e27c3 asserted to fail; it does not fail. Both sides are congruent to
  10 modulo 10^27, because x^2 + 1 = 10^128 - 6*10^64 + 10 is congruent to 10 modulo 10^27
  (the terms 10^128 and 6*10^64 both vanish mod 10^27), and 2 t_1 t_2 = 10^128 - 6*10^64 + 10
  by (a) and (b), so it too is congruent to 10.
* mod 10^64: 2ab = 10 and x^2 + 1 = 10, by the same argument with 10^128 vanishing.
* mod 10^64 - 1: x^2 + 1 = 1 - 6 + 10 = 5 and 2ab = 5, consistent with ab = (x^2+1)/2.

**(d) Self-contained verification recipe.** Any reviewer can confirm the identity in one line
of exact integer arithmetic, with no floating point:

    x = 10**64 - 3
    assert 2 * t_1 * t_2 == x*x + 1
    assert (x*x + 1) == 10**128 - 6*10**64 + 10
    assert (2 * t_1 * t_2) % 10**27 == (x*x + 1) % 10**27 == 10

All three assertions hold. The submission's build script
(tools/build_h6b.py) executes exactly these assertions before writing any file, so the
identity is machine-checked at build time as well.

**(e) Consequence.** Because t_1 t_2 t_3 = x^2 + 1 with t_3 = 2, the expression 9999999999999999999999999999999999999999999999999999999999999996*9999999999999999999999999999999999999999999999999999999999999998*5909009547859618446014307935656485996455360061473289284034355157*8461654968574415353741992088106541809421651544931744139485636465*2/9999999999999999999999999999999999999999999999999999999999999997^4 equals
(x - 1)(x + 1)(x^2 + 1)/x^4 = (x^4 - 1)/x^4 = 1 - 1/x^4 exactly, as a rational number, with
normalized numerator x^4 - 1 and denominator x^4, each of 256 decimal digits. This is the
fraction epsilon_H of the fifth claim.

This guarantee covers detectable (heralded) malformed copies only; no tolerance of
undetectable corruption is claimed in the fifth claim, and the unflagged guarantee
floor(Q/(8 n^32)) of ModelM is proved in proof.md but not claimed.
