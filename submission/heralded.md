# SPTS1-H: sampled-pivot tournament search behind a heralded filter (the fifth claim)

## H.0 What this snapshot is

`proof.md` and `sources/RQ-SPLIT-proof.md` of this snapshot contain the complete specification and
proof of the algorithm SPTS1 (the other files beside them, `sources.md`, `checks/`, `review/`,
`README.md`, `replay_checks.py` and `replay-results.json`, are its supporting material). SPTS1
acquires exactly `Q0 = 3*2^40 (n+32)` copies, extracts a label and
keeps a one-qubit row from each, and recovers s with `T = O(2^(n/2) n log^3(n+2))`, `S_C = O(n^2)`,
`S_Q = O(n)` on every branch and success probability at least 11/16, for every adversary of its
adaptive malformed-copy model with fraction 1/3, including the adversary that corrupts nothing.
"SPTS k" below is Section k of `proof.md`; "RQ k" is Section k of `sources/RQ-SPLIT-proof.md`.

Credit (not a premise of any argument): SPTS1, its proofs and its accounting are the work of
0xplemonade (public submission 96a945cd-30b6-43f4-972f-e399bbd13a52); those files are included
here without change. Every step below uses only the text of the files of this snapshot. Nothing
depends on the content, the bytes or the verdict of any other submission.

New here: every acquisition of SPTS1 is served by FILTER (H.2), which resets flagged copies. The
heralded model, FILTER and Lemmas H.1-H.2 first appeared in my own earlier public submissions (for
example 8467cc33-82d8-41df-9ad2-d7ac89987ae7 and e5bdf4b7-42c1-4f49-bd92-418ce0613ca5; credit
only), and are written out in full below. The adaptation to SPTS1's acquisition loop and Theorem H.3 are new. This snapshot
uses SPTS1 only on well-formed copies, that is, with SPTS1's adversary that corrupts nothing. Its
fifth claim is the heralded tolerance below; SPTS1's own claim (1/3 in the adaptive model of
`sources/error-model.txt`) is not claimed here.

## H.1 Error model of the fifth structured claim (exact text)

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

## H.2 Constants and FILTER

Let `y = 10^128 - 184`, `D = y^2` and `epsilon_H = 1 - 1/D`. D is a fixed absolute integer with 256
decimal digits, so `D < 10^256 < 2^851`.

**Handed-over cap.** SPTS1 acquires exactly `Q0 = 3*2^40 (n+32)` copies, in a fixed loop
`j = 1, ..., Q0` that runs before any later abort is possible (SPTS 1, RQ 4: "The algorithm
acquires EXACTLY Q originals"). No other step acquires a copy (SPTS 8, RQ 9). Each acquired copy
enters the raw input register of `n+1` wires, on which EXTRACT acts (RQ 3-4).

**Raw counter.** Before the first acquisition compute `R0 = D Q0` and store it in a binary
down-counter r. Since `Q0 < 2^42 (n+32)`, r has at most `893 + ceil(log2(n+32))` bits. Computing R0
is a fixed sequence of shift-and-add passes with the absolute constant `3*2^40 D`.

**FILTER.** In iteration j of SPTS1's acquisition loop, the step "acquire one original" is
replaced by

1. If `r = 0`: release every retained row and all scratch, output 0 and halt.
2. Decrement r by one.
3. Acquire one raw copy into the raw input register and read its herald bit f.
4. If `f = 1`: reset the `n+1` wires of the raw input register to |0>, with no other operation on
   them, and go to step 1.
5. If `f = 0`: continue iteration j exactly as SPTS1 prescribes (EXTRACT, X on the row,
   measurement, reset and release of the position and extraction registers, storage of W_j).

When copies carry no herald bit, FILTER hands every copy over. SPTS1 never reads a herald, a
flagged register or r. The deliveries it processes are the handed-over copies, exactly Q0 of them
unless step 1 halts the run.

## H.3 Lemma H.1 (the raw cutoff never binds)

**Lemma H.1.** Under the heralded model with fraction epsilon_H, step 1 of FILTER never halts the
run: all Q0 iterations receive a well-formed copy.

*Proof.* Suppose step 1 halts in iteration j <= Q0. Then exactly `D Q0` raw copies were acquired on
this branch, and iteration j has not received a well-formed copy, so at most `Q0 - 1` of them were
well-formed. Hence at least `D Q0 - Q0 + 1` of the `Q = D Q0` acquired copies are malformed. The
promise allows at most `floor((1 - 1/D) D Q0) = D Q0 - Q0`, a contradiction. QED

## H.4 Lemma H.2 (clean law)

**Lemma H.2.** Under the heralded model, the Q0 copies handed over by FILTER, together with every
register, measurement outcome and the output of SPTS1, have the joint law of SPTS1's run on Q0
independent ideal copies rho_s, that is, of its run against the adversary that corrupts nothing.

*Proof.* A flagged register is reset without interacting with any other register of the
algorithm, and no later operation depends on r, on f or on the number of flagged copies. So
whatever the adversary does on its private system and on flagged registers acts on systems
disjoint from those that determine SPTS1's transcript. Each well-formed copy is, at its delivery,
a fresh rho_s in tensor product with every other system, whatever the adversary's adaptive
decisions. By induction over the handed-over index, the j-th handed-over copy is a fresh rho_s in
tensor product with everything that precedes it. A clean copy of SPTS1's own model
(`sources/error-model.txt`) is the same object: a fresh rho_s in tensor product with everything
else. By Lemma H.1 the halt of step 1 never changes the run. QED

SPTS1's theorem holds for every adversary of its model, including the one that corrupts nothing
(SPTS 0 and its fifth claim: "including the clean strategy"). So SPTS1 with FILTER outputs s with
probability at least 11/16.

## H.5 Theorem H.3 (success and resources)

**Theorem H.3.** For every N >= 2 and every s, SPTS1 with FILTER outputs the entire s with
probability at least 11/16 > 2/3 in the clean problem and under every adversary of the heralded
model with fraction epsilon_H. On every execution branch, counting every raw acquisition, herald
read, reset and counter step,

    T = O(2^(n/2) n log^3(n+2)),   S_C = O(n^2),   S_Q = O(n),   Q <= D Q0 = O(n).

*Proof.* Success: Lemmas H.1 and H.2.

Samples. r starts at `D Q0` and is decremented once per raw acquisition, and step 1 halts at zero.
So `Q <= D Q0 = 3*2^40 D (n+32)` on every branch, whatever the heralds and outcomes are. D is an
absolute constant, so `Q = O(n)`.

Classical space. FILTER adds r, at most `893 + ceil(log2(n+32))` bits, and one herald bit to
SPTS1's `O(n^2)` bits (SPTS 8).

Quantum space. Raw copies occupy only the raw input register, which SPTS1 already counts ("the
current raw input", SPTS 8 and its third claim), and a flagged copy is reset before the next
acquisition. FILTER allocates no qubit, so `S_Q = O(n)` as in SPTS1.

Work. Allocated memory is `O(n^2)`, so the address charge is `O(log(n+2))`. One pass of FILTER is
a zero test and a ripple decrement of r (`O(log(n+2))` bit operations), one acquisition (source
charge `n+1`), one herald read and at most `n+1` resets: `O(n log(n+2))` work. There are at most
`D Q0 = O(n)` passes, and computing R0 costs `O(log^2(n+2))`. So FILTER adds `O(n^2 log(n+2))` work.
If step 1 halts, releasing at most Q0 rows costs `O(n log(n+2))`. SPTS1's own work on the
handed-over copies is `O(2^(n/2) n log^3(n+2))` on every branch (SPTS 8), and
`n^2 log(n+2) = O(2^(n/2) n)`. QED

The supported envelopes are therefore SPTS1's: `2^(n/2) n (log2 n)^3`, `n^2`, `n` and `n`, with growth
indices 1, 0, 0, 0 (SPTS 8).

## H.6 Tolerance integers and the fifth claim

Direct integer multiplication (also checked in Wolfram Language) gives

    y - 1 = 10^128 - 185 = 5335141990128885426609730276678720277683416502358554958365713865 * 1453784502951732741565122088722888544641192403053171515669467 * 12893
    y + 1 = 10^128 - 183 = 719055566230248251667422218800112619090393319415209063256198417 * 577059380141468332193372098822704305647887763344885788274559561 * 241
    y     = 10^128 - 184 = 5075877125918923237102883636467494305708529717425087531949658494 * 9850514257858070894700972904055977636084650030052055871926891182 * 2

(the factors need not be prime; each has at most 64 digits). Hence the supported expression of the
fifth claim, with numerator the six factors of y - 1 and y + 1 and denominator the square of the
product of the three factors of y, equals `(y - 1)(y + 1)/y^2 = 1 - 1/y^2 = 1 - 1/D = epsilon_H`, a
constant in (0, 1) with normalized numerator and denominator of 256 digits. epsilon_H is used only
in Lemma H.1, through `floor(epsilon_H D Q0) = D Q0 - Q0`.

**Fifth claim.** Under the heralded malformed-copy model of H.1 with fraction
`epsilon_H = 1 - 1/(10^128 - 184)^2`: for every N >= 2 and s and every such adversary, SPTS1 with
FILTER recovers the entire s with probability at least 11/16, jointly with the four resource
bounds of Theorem H.3. This covers detectable (heralded) malformed copies only. Tolerance of
undetectable corruption (SPTS1's own 1/3 in its adaptive model) is 0xplemonade's result for SPTS1
without the filter and is not claimed for this snapshot. The clean problem is solved by the same
algorithm with the same bounds.
