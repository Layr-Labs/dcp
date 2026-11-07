# GPS3-E/H: heralded filter and heralded tolerance (companion to proof.md)

This file is part of the submission and is evidence for all five claims. It carries the whole
heralded section: the exact error model of the fifth claim, the filter FILTER, the literal
copy cap Q*, two lemmas, the success and resource theorem, and the tolerance integers.

## H.0 Reading rule

The algorithm is the unchanged GPS algorithm of proof.md (Sections 1-9), in which every source
acquisition is one call of FILTER (H.2). This covers the at most n+10 copies per candidate of
the finite branch n < 256 (proof.md Section 8, including n = 1) and, for n >= 256, every copy
acquired for a leaf of Section 6 or Section 7, every copy rejected by the acceptance test
k < 2^d, every copy of a discarded or failed attempt and of an aborted run. The acquisition
counter and its cap Qcap of proof.md Section 8, the per-candidate copies of the finite branch
and the EXTRACT parameter h = ceil(log2(2^16 Qcap (n+5))) of Section 3 all count copies HANDED
OVER by FILTER; only FILTER's counter r of H.2 counts raw copies. The algorithm reads only the
handed-over copies and never the herald, so its control flow is that of the unflagged
algorithm on the same copies. When copies carry no herald bit, FILTER is the identity and the
algorithm is exactly GPS3.

## H.1 Error model of the fifth structured claim (exact text)

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

Let x = 10^64 - 3 = 9999999999999999999999999999999999999999999999999999999999999997, D = x^4 and epsilon_H = 1 - 1/D. D is a fixed absolute integer
(2^850 < D < 2^851).

## H.2 FILTER and the literal copy cap Q*

**Q*.** Q*(N) is a hard cap on the number of source copies the algorithm hands over on every
branch, counting all retries, rejections, discards, failed attempts and aborts:

* n < 256 (including n = 1): Q* = N (n + 10). The finite branch of proof.md Section 8 uses at
  most n + 10 fresh copies for each of its at most N candidates t', so it acquires at most
  N (n + 10) copies on every branch; this is below the absolute constant 2^255 * 265.
* n >= 256: Q* = Qcap = 1024 (2 G H0 + 2n) of proof.md Section 8. The abort rule runs before
  every acquisition: if the acquisition would make the handed-over count exceed Qcap, the run
  aborts without acquiring; otherwise it acquires and increments the counter once. So at most
  Qcap copies are handed over on every branch, and Qcap = O(n^2 (log2 n) 2^R) (Section 9.2).

In both cases the algorithm never requests more than Q*(N) handed-over copies, on every
branch, and Q*(N) = O(E(n)) with E the envelope of proof.md Section 9.6.

**FILTER.** One source acquisition is served as follows: acquire one raw copy into the
(n+1)-qubit slot that proof.md reserves for a fresh copy and read its herald bit f; if f = 1,
reset that slot to |0> in place, without any other operation, and acquire again; otherwise hand
the register to the caller as the acquired copy. When copies carry no herald bit, FILTER is the
identity. A classical raw counter r, initialised to 0, enforces the literal cutoff D Q*(N) on
every branch: if the next raw acquisition would make r exceed D Q*(N), stop, release all
registers and output 0.

## H.3 Lemma H.1 (the cutoff never binds)

Under the heralded model with fraction epsilon_H, the cutoff D Q* is never reached while a
copy is awaited. Consequently every FILTER call completes, and every acquisition the algorithm
makes returns a handed-over copy.

*Proof.* Suppose the cutoff is reached while the algorithm awaits its handed-over copy number
j. By H.2 the algorithm requests at most Q* copies, so j <= Q*. Then j - 1 <= Q* - 1
well-formed copies were handed over, D Q* raw copies were acquired, and at least
D Q* - Q* + 1 of them are malformed. The promise on this branch, with Q = D Q* raw
acquisitions, allows at most floor((1 - 1/D) D Q*) = D Q* - Q* malformed copies, a
contradiction. The argument needs only that the algorithm never requests more than Q* copies,
which its finite-branch loop bounds and its abort rule guarantee. QED

## H.4 Lemma H.2 (clean law)

Under the heralded model, the joint law of every measurement outcome of GPS with FILTER and
of its output equals that of the clean problem: independent ideal copies rho_s, requested one
at a time and delivered fresh.

*Proof.* A malformed register is reset without interacting with any algorithm register, so it
is traced out; whatever the adversary does on its private system and on malformed registers
acts on systems disjoint from the algorithm's, and the algorithm reads neither the herald nor
r. Each well-formed copy is, at delivery, a fresh rho_s in tensor product with every other
system, irrespective of the adversary's adaptive decisions; the algorithm's own coins, search
registers and measurement bases are drawn after delivery as before. By induction over the
handed-over index j, the handed-over copies are distributed exactly as independent ideal
copies delivered on request, which is the clean problem analysed in proof.md Sections 2-8
(the latent-label model of Section 2 applies to each handed-over copy exactly as before). By
Lemma H.1 the extra cutoff never changes the run. QED

## H.5 Theorem H.3 (success and resources)

Under the heralded model with fraction epsilon_H, for every N >= 2 and every s in Z/NZ, GPS
with FILTER outputs the entire s with probability at least 1 - 2^-8 > 3/4, and on every
execution branch T = O(E(n)), S_C = O(n^2), S_Q = O(n), the number of copies handed over is at
most Q*(N) = O(E(n)), and the number of raw copies acquired is at most D Q*(N) = O(E(n)), with
E the envelope of proof.md Section 9.6.

*Proof.* *Success.* By Lemma H.2 the run is a run of the clean problem, for which proof.md
Section 8 proves failure at most 2^-8 (finite branch below 2^-10) jointly with the resource
accounting of Section 9.

*Copies.* By the literal cutoff at most D Q* raw copies are acquired on every branch, and
handed-over copies are at most Q* by H.2. Both are O(E(n)) by Section 9.6 with the absolute
constant D.

*Time.* Each raw copy costs the source charge n + 1, one herald read, a reset of n + 1 qubits
when malformed (O(n) operations), and an increment and comparison of r, which has
bitlength(D Q*) <= 851 + bitlength(Q*) = O(n) bits (Q* has O(n) bits on both branches: the
cap's binary length is O(R + log n) = O(n) by Section 9.2, and N (n + 10) < 2^(n + 9)). Every
indexed action pays the address charge O(log(S_C + S_Q + 2)) = O(log n) of proof.md Section
1, so a raw copy costs O(n log n). The extra work is therefore O(D Q* n log n), which is
O(n^3 (log2 n)^2 2^R) for n >= 256 and an absolute constant for n < 256; by proof.md Section
9.6 it is O(E(n)). The work of the algorithm on the handed-over copies is that of proof.md
Section 9.4, T = O(n^5 (log2 n)^2 2^R) = O(E(n)). proof.md has no literal work cap: its aborts
are the acquisition cap Qcap and the weighted-attempt cap Wcap, which count handed-over
copies and attempts, never operations, so FILTER's work, charged outside both counters,
changes no branch of the algorithm. Hence T = O(E(n)) on every branch.

*Space.* The classical space grows by the O(n) bits of r, one herald bit and the O(n)-bit
constant D Q*, so S_C = O(n^2); all counters and fields of proof.md keep their orders, and the
address charge stays O(log n). A malformed register arrives in the (n+1)-qubit slot that
proof.md already reserves for a fresh copy (counted in S_Q = O(n), Section 9.3) and is reset in
place before the next acquisition, so S_Q = O(n). All other steps run exactly as in proof.md on
the handed-over copies, so the four bounds and the envelopes of Section 9.6 hold jointly on
every branch. QED

## H.6 Fifth claim: tolerance integers

The fifth claim is epsilon_H = 1 - 1/x^4 under the heralded model of H.1. The displayed
integers t_i satisfy t_1 t_2 t_3 = x^2 + 1 exactly (direct integer multiplication; they need
not be prime):

    t_1 = 5909009547859618446014307935656485996455360061473289284034355157
    t_2 = 8461654968574415353741992088106541809421651544931744139485636465
    t_3 = 2

Each of x - 1, x, x + 1 and every t_i has at most 64 decimal digits. The supported expression

    9999999999999999999999999999999999999999999999999999999999999996*9999999999999999999999999999999999999999999999999999999999999998*5909009547859618446014307935656485996455360061473289284034355157*8461654968574415353741992088106541809421651544931744139485636465*2/9999999999999999999999999999999999999999999999999999999999999997^4

equals (x - 1)(x + 1)(x^2 + 1)/x^4 = (x^4 - 1)/x^4 = 1 - 1/x^4 = epsilon_H, a constant in
(0, 1), with normalized numerator and denominator of 256 digits. This guarantee covers
detectable (heralded) malformed copies only; no tolerance of undetectable corruption is claimed
in the fifth claim, and the clean-copy tolerance 0 of the source remains proved in proof.md but
is not claimed.
