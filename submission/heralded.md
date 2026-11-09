# Heralded filter and tolerance for PARTROOT196-E (the fifth claim)

The heralded model, FILTER and Lemmas H.1-H.2 are restated from my own earlier public
submissions (for example 8467cc33-82d8-41df-9ad2-d7ac89987ae7 and
298e6cae-3ae1-4d71-9e3c-09ac0950eac2, file `heralded.md`); only the base algorithm, its caps and the tolerance constant are
new. Everything needed is restated here. Section references: "virtual k" is `virtual.md`,
"physical k" is `proof.md`, "E.k" is `envelope.md`.

## H.1 Error model of the fifth structured claim (exact text)

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

## H.2 Constants, caps and FILTER

Let `y = 10^128 - 184`, `D = y^2` and `epsilon_H = 1 - 1/D`. D is a fixed absolute integer with
256 decimal digits (`log2 D < 851`).

**Handed-over cap Q*.** Q* is the literal source cap of PARTROOT196, computed before the first
source request (physical 2, virtual 13): for `n < 2^512` (finite streaming tester)
`Q* = N (n + 10)`; for `n >= 2^512`, `Q* = Qcap = 4 n C0 + K`, which physical 2 computes before
LE. Virtual 13 and physical 10 prove that on EVERY execution branch the base requests at most
Q* copies (at most n batches of at most `4 C0` acquisitions plus at most K; the finite tester
uses at most `n + 10` copies per candidate), whatever the measurement outcomes, including every
failure, discard, retry, abort and bad-label branch.

**FILTER.** One source request of the base is served as follows. A classical counter h counts
copies handed over; if a request arrives with `h = Q*`, stop and output 0 (by the previous
paragraph this never happens). Otherwise acquire one raw copy into the source register of
physical 4 (the one additional counted register of n+1 wires) and read its herald bit f; if
`f = 1`, reset those n+1 wires to |0> without any other operation and acquire again; if `f = 0`,
increment h and hand the register to the caller, which continues exactly as physical 4 says
(three CNOTs per wire into the mapped source slots and release of the zero temporary), or, on
the finite branch, as the finite tester says. A classical raw counter r enforces the literal
raw cutoff `D Q*` on every branch: if the next raw acquisition would make r exceed `D Q*`, stop
and output 0. When copies carry no herald bit, FILTER hands every copy over (it is the identity
apart from the two counters).

**Global statement.** Every original source request of PARTROOT196 (finite tester copies; LE
supplier copies; root, 2-adic and optional `wd1` copies; copies used by failed, discarded or
partial attempts) is exactly one FILTER call, made at its original logical point. The base's
own counters and caps count handed-over copies; only r counts raw copies. The base never reads
a herald, so its control flow is that of the clean algorithm on the handed-over copies.

## H.3 Lemma H.1 (the raw cutoff never binds)

**Lemma H.1.** Under the heralded model with fraction epsilon_H, neither stop of FILTER is ever
executed: every FILTER call returns a well-formed copy and the base makes at most Q* calls.
*Proof.* The h-stop never fires because the base requests at most Q* copies on every branch
(H.2). Suppose the raw cutoff is reached while call j is served. Then `j <= Q*`, at most
`j - 1 <= Q* - 1` well-formed copies were handed over, exactly `D Q*` raw copies were acquired on
this branch (the run stops with `r = D Q*`), so at least `D Q* - (Q* - 1)` of them are malformed.
The promise for a branch with `D Q*` acquisitions allows at most
`floor((1 - 1/D) D Q*) = D Q* - Q*` malformed copies, a contradiction. ∎

## H.4 Lemma H.2 (clean law)

**Lemma H.2.** Under the heralded model, the sequence of copies handed over by FILTER, together
with every register, measurement outcome and the output of PARTROOT196, has the joint law of
the clean run, in which the base's source requests receive independent ideal copies rho_s
delivered one at a time on request.
*Proof.* A malformed register is reset without interacting with any register of the
algorithm, so whatever the adversary does on its private system and on malformed registers
acts on systems disjoint from the algorithm's, and the algorithm never reads the herald. Each
well-formed copy is, at delivery, a fresh rho_s in tensor product with every other system,
irrespective of the adversary's adaptive decisions about which later copies are malformed. The
algorithm's internal coins are drawn after delivery as in the clean run. By induction over the
handed-over index, the j-th handed-over copy is a fresh rho_s tensor-independent of everything
that precedes it. By Lemma H.1 the stops never change the run. ∎

The success proof of PARTROOT196 (virtual 13, union bound below `2^-7`, and physical 7 for the
physical realization) uses only that source requests deliver independent ideal copies on
request, plus the algorithm's own hard caps, which FILTER does not change.

## H.5 Theorem H.3 (success and resources under FILTER)

**Theorem H.3.** For every N >= 2 and s, PARTROOT196 with FILTER outputs the entire s with
probability at least `1 - 2^-7 > 2/3` in the clean problem and under every adversary of the
heralded model with fraction epsilon_H, and on every branch, counting all raw acquisitions,
herald reads, resets and counter steps, there is an absolute constant C_H with

    T, S_Q, Q <= C_H * 2^((2/sqrt3) sqrt n + 512 n^(7/16))   (all large n),     S_C = O(n).

*Proof.* Success: Lemma H.2 and virtual 13.

Samples. At most Q* copies are handed over and at most `D Q*` raw copies are acquired on every
branch. On the main branch physical 10 gives `Qcap <= C n^3 2^u`, so raw `Q <= D C n^3 2^u`: the
original bound times the absolute constant D.

Classical space. h and r have at most `bitlength(D Q*) <= 851 + bitlength(Q*)` bits. On the
main branch `log2 Qcap = O(sqrt n)` (virtual 14), so both are O(n)-bit words; physical 8 allows
constant-many current O(n)-bit ordinary words, so `S_C = O(n)` is unchanged. The herald is one
classical bit. The finite branch has `bitlength(Q*) <= n + bitlength(n + 10)`, also O(n).

Quantum space. Raw copies use only the source register already counted by physical 4; a
malformed register is reset in place before the next acquisition. No qubit is added, so the
S_Q bound of physical 8 is unchanged.

Work. Each raw copy costs the source charge n+1, one herald read, at most n+1 resets, and O(1)
increments/comparisons of O(n)-bit counters: O(n) core steps, each paying an address charge
of at most `ceil(log2(S_C + S_Q + 2)) = O(n)` (physical 9). So FILTER adds at most
`c1 n^2 D Q*` work. On the main branch this is at most `c1 D C n^5 2^u`; since
`u <= (2/sqrt3) sqrt n + 64 n^(7/16)` (virtual 8.8) and `5 log2 n <= 448 n^(7/16)`, it is at most
`c1 D C 2^((2/sqrt3) sqrt n + 512 n^(7/16))`. Adding the base's bound (virtual 15.1) gives the
common bound for T with an absolute constant. All lengths below `2^512` form a finite set with
finite caps (`N <= 2^n`, at most `D N (n+10)` raw copies), which changes only the constant.
FILTER's raw acquisitions are not attempts of the base and change none of its caps or failure
events. ∎

Then `envelope.md` Lemma E.3 and E.4 turn the common bound into `T, S_Q, Q = O(E(n))`.

## H.6 Tolerance integers and the fifth claim

Direct integer multiplication gives

    y - 1 = 10^128 - 185 = 5335141990128885426609730276678720277683416502358554958365713865 * 1453784502951732741565122088722888544641192403053171515669467 * 12893
    y + 1 = 10^128 - 183 = 719055566230248251667422218800112619090393319415209063256198417 * 577059380141468332193372098822704305647887763344885788274559561 * 241
    y     = 10^128 - 184 = 5075877125918923237102883636467494305708529717425087531949658494 * 9850514257858070894700972904055977636084650030052055871926891182 * 2

(the factors need not be prime; each has at most 64 digits). Hence the supported expression of
the fifth claim

    \frac{(y-1 factors)*(y+1 factors)}{(y factors)^2}

with the nine integers above equals `(y - 1)(y + 1)/y^2 = 1 - 1/y^2 = 1 - 1/D = epsilon_H`, a
constant in (0, 1), with normalized numerator and denominator of 256 digits. Lemma H.1 is the
only place epsilon_H is used: for every acquisition count `Q' = D Q*` it gives
`floor(epsilon_H Q') = D Q* - Q*`.

This guarantee covers detectable (heralded) malformed copies only. No tolerance of
undetectable corruption is claimed; the clean-problem guarantee (fraction 0 in the canonical
clean model) is also proved, by the same algorithm.
