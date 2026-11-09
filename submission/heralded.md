# Heralded filter and tolerance for RQ-D3 (the fifth claim)

This file belongs to the snapshot of public submission 8ecae89b-a9f8-43de-9ce3-e41ecb0ce9f7
(RQ-D3, by mpjunior92) described in the provenance paragraph of proof.md. The heralded model, FILTER
and Lemmas H.1-H.2 come from my own public submissions aeec33bc-0d38-43b1-a551-14a60353e05e and
b867bd2f-8997-459c-9aa6-930bdcb9bc07; everything needed is restated here. Section numbers refer
to proof.md unless prefixed H.

## H.1 Error model of the fifth structured claim (exact text)

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

The unflagged model ModelM of proof.md Section 0.1 is not the fifth claim. Its analysis in
proof.md Sections 0-10 is kept verbatim as proved text; this file uses from it only the clean
problem, the strategy of ModelM that replaces no copy (proof.md Section 0.1: "Clean input is the
no-replacement strategy"). The unflagged guarantee 1/(134217728*n^3) is proved there but is not
claimed.

## H.2 Constants and FILTER

Let y = 10^128 - 184, D = y^2 and epsilon_H = 1 - 1/D. D is a fixed absolute integer
(log2 D < 851). The literal sample cap of RQ-D3 is

    Q* = Qcap = 131072 (n+1)^3 K = 2^46 (n+1)^3 (n + 6 ceil(log2 n) + 180),   K = 2^29 (n + 6 ceil(log2 n) + 180)

(proof.md Section 4). It is the hard cap on acquired original source copies on every branch:
before EACH original source call the source counter is checked, and if it equals Qcap the run
aborts without acquiring another copy; otherwise the call is made and the counter is incremented
exactly once. Hence the base never requests more than Q* copies, whatever happens (retries,
rejections, discards, failed ROOT, MID and CHILD attempts, EXTRACT calls, wrong labels, malformed
copies). Since n + 6 ceil(log2 n) + 180 <= 187 n for n >= 1 we have Q* <= 2^54 (n+1)^4 = O(n^4).
The raw cutoff is D Q* = y^2 Q*.

**FILTER.** One source acquisition is served as follows: acquire one raw copy and read its
herald bit f; if f = 1, reset its n+1 qubits to |0> without any other operation and acquire
again; otherwise hand the register to the caller as the copy. When copies carry no herald bit,
FILTER is the identity. A classical raw counter r enforces the literal cutoff D Q* on every
branch: if the next raw acquisition would make r exceed D Q*, stop and output 0.

**Global statement.** Every original source acquisition of RQ-D3 is exactly one FILTER call:
the acquisitions of EXTRACT inside every supplier, the raw copies of the odd-route supplier
(including those whose extracted label is rejected, k >= 2^d, and are discarded), the
acquisitions of the root supplier of Section 6.3, the 2-adic suppliers of Section 7, the copies
used in every CHILD, MID and ROOT attempt including failed ones, and partially built
collections. The base's own counters (the source counter checked against Qcap, and the ROOT, MID
and CHILD counters, which count attempts) count the copies handed over by FILTER, never raw
copies; only r counts raw copies. The algorithm reads only the handed-over copies and never the
herald, so its control flow is that of the unflagged algorithm on the same copies. Statements of
proof.md about ModelM, replacements, Bbad or the unflagged fraction are about the unflagged
model and read as in the provenance paragraph; under the heralded model the source calls of the
base receive exactly the copies handed over by FILTER, at most Qcap of them, and the only abort
added by FILTER is the raw cutoff, which never binds (Lemma H.1).

## H.3 Lemma H.1 (the cutoff never binds)

**Lemma H.1.** Under the heralded model with fraction epsilon_H, the cutoff D Q* is never
reached: every FILTER call that the base makes is completed, and the base makes at most Q*
of them.
*Proof.* By proof.md Section 4 the base checks its source counter, which counts handed-over
copies, before every source call and aborts without acquiring when it equals Qcap = Q*; so it
makes at most Q* FILTER calls on every branch, and call j <= Q* is made only after j - 1 copies
were handed over. Suppose the cutoff is reached while call j is being served. Then j <= Q*,
at most j - 1 <= Q* - 1 well-formed copies were handed over, exactly D Q* raw copies were
acquired (the run stops with r = D Q*), and at least D Q* - (Q* - 1) of them are malformed. The
promise of H.1 for a branch on which D Q* copies were acquired allows at most
floor((1 - 1/D) D Q*) = D Q* - Q* malformed copies, a contradiction. Hence the cutoff is not
reached, and every FILTER call returns a well-formed copy. ∎

## H.4 Lemma H.2 (clean law)

**Lemma H.2.** Under the heralded model, the sequence of copies handed over by FILTER, together
with every register, measurement outcome and the output of RQ-D3, has the joint law of the clean
run, in which the base's source calls receive independent ideal copies rho_s delivered one at a
time on request and nothing else.
*Proof.* A malformed register is reset without interacting with any register of the algorithm,
so what the adversary does on its private system and on malformed registers acts on systems
disjoint from the algorithm's, and the algorithm never reads the herald. Each well-formed copy
is, at delivery, a fresh rho_s in tensor product with every other system (earlier copies, the
adversary's system, the algorithm's registers), irrespective of the adversary's adaptive
decisions about which later copies are malformed. The algorithm's internal random choices (fair
bits, beta, search coins) are drawn after delivery as in the clean run. By induction over the
handed-over index j, the j-th handed-over copy is a fresh rho_s tensor-independent of everything
that precedes it, so the handed-over copies are distributed exactly as independent ideal copies
delivered on request. By Lemma H.1 the extra cutoff never changes the run. This is the clean
problem of ModelM (no replacements, Bbad = 0). ∎

The success proof of RQ-D3 for that problem is proof.md Sections 3-8 with the no-replacement
strategy: it needs only that the source calls deliver independent honest copies rho_s on request
(the latent-label model of Section 2 for honest calls, the honest-label union bound of
Section 3 over at most Qcap honest calls, the all-honest counterfactual kernels of Sections 4-5
with Bbad = 0, and the cap events of Section 8, which are bounds on actual events of the clean
run), and the probability bound of Section 8 holds for every strategy of ModelM, in particular
for the one that replaces nothing. Its other premise, the hard caps, is a property of the
algorithm, unchanged by FILTER.

## H.5 Theorem H.3 (success and resources)

**Theorem H.3.** Under the heralded model with fraction epsilon_H, for every N >= 2 and every s,
RQ-D3 with FILTER outputs the entire s with probability at least 1 - 2^-8 > 2/3, and on every
branch T = O(2^((13/100)n)), S_C = O(n^2), S_Q = O(n), at most Q* = Qcap = O(n^4) copies are
handed over and at most D Q* = O(n^4) raw copies are acquired.
*Proof.* Success: Lemma H.2 and proof.md Section 8, applied to the clean problem
(Pr[any failure] < 2^-8). Samples: handed-over copies are at most Q* = 2^46 (n+1)^3
(n+6 ceil(log2 n)+180) <= 2^54 (n+1)^4 by the base's source guard, and by the literal cutoff
at most D Q* <= 2^905 (n+1)^4 raw copies are acquired on every branch, an absolute constant
times n^4, the same polynomial order as the base's bound.

Counter and space. The raw counter r has at most bitlength(D Q*) <= 851 + 54 +
4 bitlength(n+1) = O(log n) bits, so one counter step costs O(log n) bit operations; the herald
is one classical bit. The classical space grows by these O(log n) bits and S_C = O(n^2) is
unchanged (the base's own bound is O(n^2), proof.md Section 9). Each raw copy is acquired into the
(n+1)-qubit slot that the base reserves for the copy being acquired, which proof.md Section 9
already counts in S_Q = O(n); a malformed register is reset in place before the next acquisition,
so no register outlives its FILTER call. Even an implementation holding one extra (n+1)-qubit slot
would add only n + 1 qubits, so S_Q = O(n).

Work. Let A = O(log(S_C+S_Q+2)) = O(log n) be the base's address charge (proof.md Section 1).
Each raw copy costs the source charge n+1, one herald read, for a malformed copy a reset of n+1
qubits (O(n) operations, each paying A), and an increment and comparison of r (O(log n) bit
operations, each paying A). Hence each raw copy costs O(n log(n+2)) beyond what the base charges
for handed-over copies, and the extra work of FILTER over all raw copies is

    O(D Q* n log(n+2)) = O(n^5 log(n+2)),

the absolute constant being D 2^54 times the constants of one raw copy. For n >= 1,
log2(n+2) <= 2n, so n^5 log2(n+2) <= 2 n^6, and 2 n^6 <= c0 2^((13/100)n) with the absolute
constant c0 = max over m >= 1 of 2 m^6 2^(-(13/100) m) < 5 * 10^8 (the maximum of a sequence that
tends to 0, attained near m = 67). Thus the extra work is O(2^((13/100)n)) with an absolute
constant and no polynomial factor, and it is added to the base's O(2^((13/100)n)) of proof.md
Section 9 (T = O(poly(n) 2^(n/8)) = O(2^((13/100)n)), where 13/100 - 1/8 = 1/200 > 0 absorbs
every polynomial prefactor): their sum is O(2^((13/100)n)), so claim 0's bound and its exact
growth index 1 are unchanged.

Caps. The four literal caps of proof.md Section 8 are the ROOT, MID, CHILD and source counters;
none is a cap on work and no abort depends on the work done. FILTER's raw acquisitions and resets are
not attempts, and the source counter counts handed-over copies only, so the cap events and their
probability bounds are those of the clean run (Lemma H.2); FILTER's work is charged outside all four
counters, namely in the bound above. No argument about the caps needs adjusting.

All other steps run exactly as in proof.md on the at most Q* handed-over copies, so the four
bounds and envelopes of proof.md Sections 0 and 9 hold jointly on every branch. ∎

## H.6 Tolerance integers and the fifth claim

Direct integer multiplication gives (the factors need not be prime; each has at most 64 digits)

    y - 1 = 10^128 - 185 = 5335141990128885426609730276678720277683416502358554958365713865 * 1453784502951732741565122088722888544641192403053171515669467 * 12893
    y + 1 = 10^128 - 183 = 719055566230248251667422218800112619090393319415209063256198417 * 577059380141468332193372098822704305647887763344885788274559561 * 241
    y     = 10^128 - 184 = 5075877125918923237102883636467494305708529717425087531949658494 * 9850514257858070894700972904055977636084650030052055871926891182 * 2

Hence the supported expression

    \frac{5335141990128885426609730276678720277683416502358554958365713865*1453784502951732741565122088722888544641192403053171515669467*12893*719055566230248251667422218800112619090393319415209063256198417*577059380141468332193372098822704305647887763344885788274559561*241}{(5075877125918923237102883636467494305708529717425087531949658494*9850514257858070894700972904055977636084650030052055871926891182*2)^2}

equals (y - 1)(y + 1)/y^2 = (y^2 - 1)/y^2 = 1 - 1/y^2 = 1 - 1/D, the claimed fraction, a constant in (0, 1),
with normalized numerator and denominator of 256 digits. Here y = 10^128 - 184 and D = y^2 < 10^256,
so log2 D < 851 and every bound above that uses log2 D < 851 or D < 2^851 is unchanged.
This guarantee covers
detectable (heralded) malformed copies only; no tolerance of undetectable corruption is
claimed in the fifth claim, and the unflagged guarantee of ModelM is proved in proof.md but
not claimed.
