# LST-H-T2: the linear-memory streamed shift tester behind a heralded filter (the fifth claim)

## H.0 What this snapshot is

`proof.md` is a byte-identical copy of the proof file of public submission
198a7f6f-0326-439d-a338-e9d66fa2d3eb (LST, by mpjunior92): the streamed cutoff shift tester with
k = n+4 tests per candidate and the global cap 48N, with `T = O(N n log2(n+2))`, `S_C = O(n)`,
`S_Q = O(n)`, `Q <= 48N` on every branch and success probability above 5/6 from ideal copies. The
algorithm, its success proof and its bit-level accounting are theirs and are used unchanged.
"LST k" below means the section of `proof.md` with that heading.

New here: every acquisition of LST is served by FILTER (H.2), which discards flagged copies. The
heralded model, FILTER and Lemmas H.1-H.2 are restated from my own earlier public submissions (for
example 8467cc33-82d8-41df-9ad2-d7ac89987ae7 and e5bdf4b7-42c1-4f49-bd92-418ce0613ca5, file
`heralded.md`). The adaptation to LST's single sample register, the O(n)-bit raw down-counter and
the proof that the filter keeps all four of LST's envelopes (Theorem H.3) are new. The fifth claim
of `proof.md` (tolerance 0 in the clean model) is LST's own and is not this snapshot's claim.

**What changed from the previous version.** Only the tolerance constant: D is now
`(16*10^126 - 1)(625*10^126 - 1)` (H.2, H.6). The algorithm, the error model, the four resource
bounds and every proof step are unchanged, because the proofs use D only as a positive integer
(and `D < 2^851` where a width is needed: the constant `48 D` still has at most 857 bits). Credit,
not a premise: the previous version is my own earlier submission
91357338-275b-4c5e-ab48-d1755536724e. Every step below uses only the
text of the files of this snapshot; nothing depends on the content, the bytes or the verdict of any
other submission.

## H.1 Error model of the fifth structured claim (exact text)

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

## H.2 Constants and FILTER

Let `A = 16*10^126 - 1`, `B = 625*10^126 - 1`, `D = A B` and `epsilon_H = 1 - 1/D`. D is a fixed absolute
positive integer with 256 decimal digits (H.6), so `D < 10^256 < 2^851`.

**Handed-over cap.** LST keeps a classical counter c, initially 0. Before each acquisition it
outputs 0 and halts if `c = 48N`; otherwise it acquires one copy and increments c (LST
"Algorithm"). So on every branch LST requests at most `Q* = 48N` copies.

**Raw counter.** Before the first acquisition compute `R0 = 48 D N` by a fixed sequence of O(1)
shift-and-add passes over the O(n)-bit number N with the absolute constant `48 D` (at most 857
bits), and store it in a binary down-counter r of `n + 857` bits. This costs O(n) bit operations
with absolute constants (the multiplier has a fixed number of bits), each paying the address
charge.

**FILTER.** Each execution of LST's step "acquire one fresh source copy" is replaced by the loop

1. If `r = 0`, output 0 and halt.
2. Decrement r by one (a ripple borrow over its `n + 857` bits; the test `r = 0` in step 1 is a
   scan of the same bits).
3. Acquire one raw copy into LST's sample wires (the `n+1` wires LST uses for every test) and read
   its herald bit f into one classical bit.
4. If `f = 1`: dispose of all `n+1` sample wires exactly as LST disposes of a tested sample (no
   other operation touches them), and go to step 1.
5. If `f = 0`: hand the copy to LST, which increments c and continues with its controlled
   subtraction `f_t`, the X measurement and the disposal, unchanged.

When copies carry no herald bit, FILTER hands every copy over (step 4 never occurs). LST never
reads a herald, a flagged register or r; its control flow is that of the clean algorithm on the
handed-over copies. LST's counter c counts handed-over copies; only r counts raw copies.

## H.3 Lemma H.1 (the raw cutoff never binds)

**Lemma H.1.** Under the heralded model with fraction epsilon_H, step 1 of FILTER never halts the
run: every FILTER call returns a well-formed copy.

*Proof.* Suppose step 1 halts while some request is being served. Then exactly `48 D N` raw copies
were acquired on this branch. The request being served is at most LST's `48N`-th (LST halts before
requesting a copy when `c = 48N`), and it has not been satisfied, so at most `48N - 1` raw copies
were well-formed. Hence at least `48 D N - 48N + 1` of the `Q = 48 D N` acquired copies are
malformed. The promise allows at most `floor((1 - 1/D) 48 D N) = 48 D N - 48N` malformed copies on
this branch, a contradiction. QED

## H.4 Lemma H.2 (clean law)

**Lemma H.2.** Under the heralded model, the sequence of copies handed over by FILTER, together
with every register, measurement outcome and the output of LST, has the joint law of the clean
run, in which LST's requests receive independent ideal copies rho_s delivered one at a time.

*Proof.* A flagged register is disposed of without interacting with any other register of the
algorithm, and the algorithm's later operations do not depend on r, on f or on the number of
flagged copies. So whatever the adversary does on its private system and on flagged registers acts
on systems disjoint from those that determine LST's transcript. Each well-formed copy is, at its
delivery, a fresh rho_s in tensor product with every other system, whatever the adversary's
adaptive decisions about which copies to flag. By induction over the handed-over index, the j-th
handed-over copy is a fresh rho_s in tensor product with everything that precedes it. By Lemma H.1
the halt of step 1 never changes the run. QED

LST's success proof (LST "Success with a hard sample cap") uses only that its requests deliver
independent ideal copies, together with its own cap 48N, which FILTER does not change.

## H.5 Theorem H.3 (success and resources)

**Theorem H.3.** For every N >= 2 and every s, LST with FILTER outputs the entire s with
probability above 5/6 > 2/3 in the clean problem and under every adversary of the heralded model
with fraction epsilon_H. On every execution branch, counting every raw acquisition, herald read,
disposal and counter step,

    T = O(N n log2(n+2)),   S_C = O(n),   S_Q = O(n),   Q <= 48 D N = O(N).

*Proof.* Success: Lemmas H.1 and H.2 with LST's success bound.

Samples. r starts at `48 D N` and is decremented once per raw acquisition, and step 1 halts at
zero, so `Q <= 48 D N` on every branch, whatever the heralds and outcomes are. D is an absolute
constant and `N <= 2^n`, so `Q = O(2^n)`.

Classical space. Beyond LST's O(n) bits, FILTER stores r (`n + 857` bits), the herald bit and
O(log(n+2))-bit scan indices. So `S_C = O(n)`.

Quantum space. Raw copies occupy only LST's sample wires, which are disposed of before the next
acquisition. FILTER allocates no qubit. So `S_Q = O(n)`, as in LST.

Work. By the two bounds just proved, the allocated memory is O(n), so the address charge is
`O(log(n+2))`, as in LST "Streaming generation and bit-operation addresses". One pass of the
FILTER loop performs: a zero scan and a ripple decrement of r, O(n) bit operations; one
acquisition, source charge `n+1`; one herald read; and, for a flagged copy, the disposal of `n+1`
wires. That is O(n) addressed operations, hence `O(n log2(n+2))` work per raw copy, the same order
as LST's own per-test bound. There are at most `48 D N` passes. The initial computation of R0 is
`O(n log2(n+2))`. LST's own work is `O(N n log2(n+2))` on every branch (LST "Joint envelopes"),
because it makes at most 48N requests and N candidate steps, which FILTER does not change. So

    T <= c0 (48 D N) n log2(n+2) + c1 N n log2(n+2) = O(N n log2(n+2)),

with absolute constants, because D is absolute. QED

The supported envelopes are therefore LST's: `B_T = 2^n n log2 n`, `B_C = B_Q = n` and
`B_samples = 2^n`, with growth indices 1, 0, 0, 1 (LST "Joint envelopes, indices, and error model").
As there, the single length n = 1 is one finite computation covered by an absolute constant.

## H.6 Tolerance integers and the fifth claim

Direct integer multiplication (checked with exact integer arithmetic) gives the first three lines
below; the fourth is the decimal form of `10^63` (64 digits).

    A = 16*10^126 - 1  = 4329632813347406305223297584667745034303743116654997715999733453 * 3695463493041522429397493437973995985916922777904245876619237883
    B = 625*10^126 - 1 = 8333333333333333333333333333333333333333333333333333333333333333 * 454542699741213689614002339379761334779789213398706674505003 * 165001
    C = 10^130 - 641   = 2189251513709577192973000802960123783290116879858557832979634351 * 858746507556703404750738054330397864679429 * 5319114725318138222421821
    Z = 10^63          = 1000000000000000000000000000000000000000000000000000000000000000

(the factors need not be prime; each has at most 64 digits). Since `16*625 = 10^4` and
`16 + 625 = 641`, `D = A B = 10^256 - 641*10^126 + 1`, so `D - 1 = 10^126 C = Z^2 C`. Hence the supported
expression of the fifth claim, with numerator `Z^2` times the three factors of C and denominator the
two factors of A times the three factors of B (nine displayed integers), equals
`Z^2 C/(A B) = (D - 1)/D = 1 - 1/D = epsilon_H`, a constant in (0, 1). `D - 1` and `D` are coprime, so the
normalized numerator and denominator are `D - 1` and `D`, each of 256 digits. epsilon_H is used only
in Lemma H.1, through `floor(epsilon_H * 48 D N) = 48 D N - 48N`.

**Fifth claim.** Under the heralded malformed-copy model of H.1 with fraction
`epsilon_H = 1 - 1/D`, `D = (16*10^126 - 1)(625*10^126 - 1)`:
for every N >= 2 and s and every such adversary, LST with
FILTER recovers the entire s with probability above 5/6, jointly with the four resource bounds of
Theorem H.3. This covers detectable (heralded) malformed copies only; no tolerance of undetectable
corruption is claimed. The clean problem (no herald, all copies ideal) is solved by the same
algorithm with the same bounds.
