# QF48: bounded quantum fiber enumeration and exact phase compression

Research-only result, 2026-11-06 UTC. Owned file: this file only. No publication,
source lease, candidate mutation, checkout, queue restart, or PSR2 proof review.
Read `rules.md`, `COORDINATION.md`, and the later
`/Users/kaanm2/yukon-automining/dcp-COMPARATOR.md` instruction.

**Result.** The proposed square-root replacement for the exponential fiber scan
works as a *conditional phase-state primitive*. With `r=w+4`, `H=1024`, and 48
trials per search, its unconditional output probability, averaged over independent
uniform low labels, is at least **939/1024 > 7/8**. Every emitted state and its
label are exact, including when enumeration misses solutions. All branches cost
`O(2^(r/2) n^2 log(n+2))` charged work, `O(n^2)` classical bits and `O(n)` qubits.
It consumes exactly r supplied phase states per invocation and acquires **zero
additional DCP copies**. Input production is not free and is not established here.

This is not a complete all-N DCP solver, a full-secret recovery theorem, or a
global time lead over CS1. In particular, exact quotient-label uniformity needs
the hypotheses below; arbitrary-modulus interval labels cannot silently replace
cyclic quotient labels. The principal new ingredient relative to the proposed
classical scan is bounded search followed by **verified-set projection**, which
makes search misses erasures rather than errors.

## 1. Exact hypotheses and output contract

Let `n>=1`, `0<=w<=n`, `q=2^w`, `r=w+4`, and `D=2^r=16q`. A general phase input is

    |Phi_theta(b)> = tensor_{j=1}^r (|0> + exp(2 pi i theta b_j)|1>)/sqrt(2),

where theta is any fixed unknown real and the exact integers b_j, each with at
most n bits, are supplied classically. Write `a_j=b_j mod q`. Phase correctness
holds for every b and theta. The yield guarantee assumes that the a_j are
independent uniform elements of Z/qZ. Nothing assumes theta or the secret random.

For the **exact cyclic uniform-output contract**, additionally fix an integer
`M=qK<=2^n`, take `theta=s/M` for any fixed integer s, and assume the b_j are
independent uniform in `[0,M)`, independent of the primitive's fresh coins. Then

    b_j = a_j + q u_j,
    (a_1,...,a_r) uniform in (Z/qZ)^r,
    (u_1,...,u_r) uniform in (Z/KZ)^r and independent of all a_j.

For K=1 the quotient contract is the trivial one-element group. The supplied
quantum state, conditional on the exact labels, is the product above. No ability
to prepare it again, purify its origin, reflect about it, or coherently query its
source is supplied or used.

One invocation consumes its r input states and emits either FAIL or exactly one
qubit plus a known label `v in Z/KZ`. On success that qubit is exactly

    |phi_{s,K}(v)> = (|0> + exp(2 pi i s v/K)|1>)/sqrt(2),

up to a global phase. The label v is exactly uniform, even conditional on any
positive-probability **low-only selection transcript** defined in Section 6.
The operation emits one pair's qubit, not one independent qubit for each pair.

## 2. Fixed-cap search, including zero and all marked elements

For fixed low labels a, residue z, and a classical distinct list S, define

    f_a(x) = sum_j a_j x_j mod q,       x in {0,1}^r,
    P_S(x) = [f_a(x)=z] AND [x not in S].

This is a computed predicate, not an oracle supplied by the problem. Section 7
constructs and charges it. Set

    L = 2^ceil(r/2),    B = 48.

`Find(S)` makes at most B trials. In each trial:

1. Draw an exact uniform integer j in `[0,L)` by measuring `ceil(r/2)` fresh
   Hadamard coin qubits; this costs initialization, gates, measurements and bits.
2. On a separate clean r-qubit register prepare `|U>=H^r|0^r>`. Apply j copies of
   `(2|U><U|-I) O_S`, where `O_S|x>=(-1)^P_S(x)|x>`.
3. Measure x. Recompute P_S(x) classically. Return x only if this exact verification
   accepts. Otherwise reset/reuse the work register and start the next trial.

After B unsuccessful trials return NONE. NONE is **not** a certificate of an
empty marked set. There is no unbounded retry or time depending on an unknown
number of marked items.

Here is the search bound, proved for each fixed predicate. If it has
`0<t<D` marked inputs, write `sin(theta_g)^2=t/D`. In the orthonormal basis of
uniform marked/unmarked superpositions, the two reflections rotate the initial
amplitudes by `2 theta_g` each iteration. Thus success after j iterations is
`sin((2j+1)theta_g)^2`. Summing the geometric cosine series gives

    p_L(t) = 1/2 - sin(4 L theta_g)/(4 L sin(2 theta_g)).             (2.1)

For `1<=t<=D-1`,

    sin(2 theta_g) = 2 sqrt(t(D-t))/D
                  >= 2 sqrt(D-1)/D >= 1/sqrt(D).

Since `L>=sqrt(D)`, (2.1) gives `p_L(t)>=1/4`. This includes dense marked sets;
there is no small-t assumption. If t=D, the oracle only gives a global sign and
every measured candidate passes. If t=0, no candidate ever passes verification.
Both endpoint cases are treated directly, not by dividing by zero in (2.1).

Fresh trials give, on every fixed nonempty predicate,

    Pr[Find returns NONE] <= epsilon := (3/4)^48.                   (2.2)

After an adaptive success and exclusion-list update, condition on the entire
previous search transcript. The next marked set is then fixed, its new coins and
uniform register are fresh, and the same bound applies. No independence of the
successively shrinking marked sets is assumed. The two-dimensional search law
also shows uniformity among marked items conditional on success, although the
rest of this proof does not need that fact.

Provenance for the identity (2.1): Boyer, Brassard, Hoyer and Tapp,
*Tight bounds on quantum searching*, arXiv:quant-ph/9605034v1, Section 4,
Lemma 2, PDF page 3: https://arxiv.org/pdf/quant-ph/9605034 . The fixed dyadic
cap, exact endpoint treatment and adaptive enumeration argument here are stated
explicitly rather than invoking an expected-time search theorem.

## 3. The implemented instrument

First compute f_a into a clean w-bit register attached to the ORIGINAL r phase
qubits, measure that register to obtain z, and reset it from the known outcome.
This is exact reversible arithmetic plus computational-basis measurement. Put
`F_z={x:f_a(x)=z}` and `h=|F_z|`. For any observed z, h>0. Conditional on z the
original register is exactly

    |Psi_z> = (1/sqrt(h)) sum_{x in F_z} exp(2 pi i theta b.x)|x>.    (3.1)

Keep (3.1) untouched while all searches operate on independent known-uniform
registers. Start S empty and perform the following bounded enumeration:

    Repeat at most H+1 calls:
        y := Find(S).
        If y is NONE: stop enumeration with the current S.
        Append the verified y to S.
        If |S| = H+1: return FAIL and discard the original register.

Every member of S is distinct and lies in F_z. On the non-abort branch `|S|<=H`.
If `|S|<2`, return FAIL. Otherwise sort S lexicographically, obtaining
`x_0,...,x_(ell-1)`. Pair consecutive members

    (x_0,x_1), (x_2,x_3), ..., (x_(2 floor(ell/2)-2),x_(2 floor(ell/2)-1)).

If ell is odd, its last member is unpaired. Perform these exact operations:

1. Compute `[x in S]` reversibly on the ORIGINAL register and measure only that
   flag. On 0 return FAIL. On 1 reset the flag. The state is the equal-magnitude
   superposition on S with the original phases, not an approximation to (3.1).
2. Reversibly compute the pair identifier of x into a clean register, assigning
   identifier 0 to the leftover and positive identifiers to the pairs. Measure
   only this identifier. On 0 return FAIL. Do not measure which member of a pair
   is present. Equality-test scratch is uncomputed before this measurement.
3. For the selected ordered pair (x,y), the state is exactly

       (exp(2 pi i theta b.x)|x> + exp(2 pi i theta b.y)|y>)/sqrt(2).

   Apply X gates translating x to 0, choose any pivot bit p with `(x XOR y)_p=1`,
   and apply CNOT(p,j) for each other 1-bit j of x XOR y. The basis states become
   `|0^r>` and `|e_p>`. Release the other, now-zero, qubits. The pivot qubit is

       (|0> + exp(2 pi i theta Delta)|1>)/sqrt(2),
       Delta = sum_j (y_j-x_j) b_j.                               (3.2)

Because x,y are in the measured fiber, q divides the integer Delta. The general
output is the signed integer frequency `W=Delta/q` and a phase with angle
`q theta W`. Under the cyclic hypothesis `M=qK, theta=s/M`, reduce W modulo K
and report v. This reduction leaves the phase unchanged exactly. One may compute
Delta modulo M in an n+1-bit accumulator and then shift right w bits; no large
integer division or Fourier transform is hidden here.

For every fixed a,z and search transcript yielding S, each selected pair has
unconditional probability `2/h` relative to (3.1). Hence

    Pr[emit | a,z,S] = 2 floor(|S|/2)/h.                          (3.3)

This proves **error-free output on incomplete enumeration**. Missing a solution
can change the selected pair and reduce retained mass; it cannot introduce a
wrong phase, a non-fiber member, or unequal pair amplitudes. All failed projection,
leftover, empty-list and large-list branches consume their inputs and are charged.

## 4. Uniform-label fiber and odd-leftover bounds

The measured z has probability h_z/D, independently of theta and the high labels.
For this classical probability calculation only, introduce an independent uniform
`X in {0,1}^r` and write `Z=f_A(X)`. This is a representation of the measurement
law, **not** a physical measurement of X or access to a source purification.

For x!=y the integer vector x-y has a coefficient +1 or -1. That coefficient is
a unit modulo q, so, fixing all other independent uniform low labels,

    Pr_A[f_A(x)=f_A(y)] = 1/q.

Pairwise collision counting is enough; no mutual independence of subset sums is
claimed. Consequently

    E_{A,Z}[h_Z] = (1/D) sum_{x,y} Pr_A[f_A(x)=f_A(y)]
                 = 1+(D-1)/q = 17-1/q <17.                     (4.1)

The expectation is for the size-biased *measured* fiber. Markov gives

    Pr[h_Z>H] <= E[h_Z]/H <17/1024.                             (4.2)

The slightly sharper divisor H+1 is available but unnecessary.

For EVERY fixed low-label vector, full lexicographic pairing leaves at most one
point in each odd fiber. It therefore loses at most

    (1/D) sum_z (h_z mod 2) <= q/D = 1/16.                     (4.3)

This counts all odd fibers, not just singleton fibers. In particular the ideal
full-enumeration pairing has yield at least 15/16 for every fixed a.

## 5. Adaptive stopping, unconditional yield, and the correct coupling

Fix a,z with `h<=H`. As long as the list is incomplete, each invocation of Find
is on a nonempty marked set. The conditional probability of a premature NONE is
at most epsilon by (2.2). There are at most h such calls before the entire fiber
has been discovered. A union bound over these conditional failure events gives

    Pr[S != F_z | a,z,h<=H] <= h epsilon <= H epsilon.            (5.1)

After all h elements are found, the next, empty-set call returns NONE with
certainty. This terminal call is not an enumeration error. For h=H it is call
H+1, so the prescribed cap is sufficient. For h>H, reaching H+1 verified members
causes an explicit abort; a premature NONE may instead leave a useful partial
set, whose exactness was already proved.

Let C denote the proof event that no premature NONE occurs on a fiber of size
at most H. C is not an event the implementation must certify. Couple to ideal
full enumeration using the same A,z, and use the same pair-measurement outcome
whenever C occurs. On `h<=H` and C, S=F_z and the actual and ideal instruments
agree exactly. Elsewhere the actual instrument may still emit a valid output;
ignoring that extra yield only weakens the lower bound.

Since `(3/4)^8=6561/65536 < 1/8`,

    H epsilon = 1024 (3/4)^48 < 2^10 2^-18 = 1/256.

Combining (4.2), (4.3), and (5.1), with no postselection,

    Pr[emit] >= 1 - 1/16 - 17/1024 - 1/256
             = 939/1024 > 7/8.                                (5.2)

The search-miss constant does not need an exponentially small error budget in
a recursive caller: it is a yield loss, not an incorrect-state probability.
This does not waive the caller's need for branchwise attempt/source cutoffs.

The average-over-labels qualification is essential. For example, if all a_j=0
and D>H, the sole fiber has size D; this implementation will usually abort at
H+1 discoveries. No pointwise-in-a 7/8 yield is claimed.

## 6. Exact unused-label and independent-output laws

The selection transcript tau consists of the low labels a, measured z, every
search coin and search outcome, the discovered list and its ordering, the
membership outcome, and the measured pair identifier. It excludes the supplied
higher labels u, the computed output v, and later measurements of the output
phase qubit. Only a,z and classical search history control search predicates and
all choices of pairings.

Conditional on a, the z law depends only on fiber counts. The separate-register
search law depends only on a,z,S. Finally membership and pair outcomes depend
only on cardinalities as in (3.3). Thus the complete likelihood of any tau is
independent of u and theta. In particular, under the cyclic hypothesis,

    Law(U | tau) = Uniform((Z/KZ)^r).                            (6.1)

This statement is true on partial-discovery success branches as well as complete
ones. It is not inferred from a simulation or from an exponentially unlikely
condition that enumeration found everything.

On any successful tau, the selected distinct x,y are fixed. Put `d_j=y_j-x_j`.
At least one d_j is +1 or -1, and

    v = c(a,x,y) + sum_j d_j u_j mod K,
    c(a,x,y) = (sum_j d_j a_j)/q,                               (6.2)

where c is an integer. Hold all u except one with coefficient +1 or -1 fixed.
The remaining map to v is a bijection of Z/KZ. Hence v is uniform conditional on
tau, and the successful output's classical-quantum law is exactly

    (1/K) sum_{v in Z/KZ} |v><v| tensor |phi_{s,K}(v)><phi_{s,K}(v)|. (6.3)

For independent input batches and fresh internal randomness, invocations have
product output laws. Conditional on any pattern of successes and their low-only
transcripts, the emitted labels are independent uniforms, and, given those
labels, their qubits are the product of the stated phase states. Taking the first
success in a fixed finite number of independent attempts preserves (6.3).
More generally the same induction works for a caller that supplies batches
independent in the required conditional sense and whose retention/retry decisions
use only the specified selection histories. Stopping on a high-label property,
reusing inputs, overlapping batches, or conditioning on already revealed full
input labels is not covered by this independence assertion.

For fixed w, the success probability itself is independent of K and s: the full
selection process uses only the low-label vector and the specified fresh trials.

For an arbitrary real theta and independently uniform integer interval inputs
`b_j in [0,qK)`, (6.1) still holds, but the **integer** W in (3.2) has the exact
signed-sum law `c+sum d_j U_j`, not generally a uniform interval law. For instance
a pair whose difference is `e_1-e_2` gives `U_1-U_2`, with probability
`(K-|t|)/K^2` at integers `-(K-1)<=t<=K-1`. Its residue modulo K is uniform.
Replacing W by W mod K in its phase is valid only when `qK theta` is an integer.
This is an explicit obstruction to extending the cyclic contract to arbitrary N
by simply reinterpreting high labels; it is not an obstruction to the exact
general phase operation or the unused-high-label statement (6.1).

If input labels come from a fallible extractor, analyze an ideal exact-label
process and couple the actual whole process to it with a separately proved error
budget. Conditioning the actual process on "all labels happened to be correct"
can bias labels and is not a proof of (6.1). Likewise, on approximate input states,
the failure-inclusive instrument is a CPTP map and contracts trace distance;
normalizing on success can amplify error. No approximate-state error or imperfect
label error is silently included in the exact contract here.

## 7. Counted implementation and all-branch resources

All bounds below are for this isolated primitive, including storage of its r
supplied n-bit labels and original phase qubits. H=1024 and B=48 are fixed
universal constants. Use ordinary uniformly generated X, CNOT, Toffoli, H and Z
circuits; Toffoli has a fixed exact Clifford+T decomposition. No variable-angle
gate, real arithmetic or synthesis precision occurs.

**Addition and equality.** A controlled addition of a classical w-bit constant
modulo 2^w uses O(w) gates and O(w) clean scratch. One explicit construction
computes the ripple carries `c_(i+1)=majority(y_i,a_i control,c_i)` into scratch,
XORs the sum bits into a second register, and uncomputes the carries. The majority
is the XOR of the three pairwise ANDs, hence has a constant-size Toffoli circuit.
Erase the old accumulator by the analogous inverse subtraction circuit using
the new accumulator, then swap the registers. Addition and its inverse are
permutations, and all carry scratch returns to zero. Equality to a fixed r-bit
string uses an AND chain with negative controls, O(r) gates and O(r) reusable
scratch. These constructions also give their classical bit-operation bounds.

**Predicate.** Compute f_a with r controlled additions into a w-bit accumulator;
test equality to z. Compute membership in S by scanning its at most H+1 classical
entries, computing each equality flag, toggling one membership bit, and
uncomputing the flag. Since list members are distinct, XOR equals OR here.
Apply a phase flip controlled by equality-to-z and nonmembership, then uncompute
everything. The gate cost is

    O(r(w+1) + (H+1)(r+1)),

with O(r+w) scratch. All classical constants are read and all gate descriptions
generated as they are used. There is no quantum-addressed table access. The
diffusion reflection is H^r, a phase on zero implemented by an AND chain, then
H^r again, with O(r) gates and O(r) scratch.

**Projection and compression.** Membership in the final S uses the same scan.
The pair-identifier circuit scans all entries and XORs the known identifier
conditioned on equality, uncomputing scratch on each entry; identifier width is
at most 10 bits. It has O(H(r+1)) gates. Classical sorting costs O(H^2(r+1)) bit
operations even with simple insertion sort. Pair compression uses O(r) gates.
The output frequency uses r n-bit signed additions/modular additions and, for
the cyclic version, a shift; its classical cost is O(rn) bit operations before
addressing. A signed unreduced frequency needs only O(n+log(r+1)) bits.

**Caps and streaming.** There are at most `B(H+1)=49200` search trials and at most
`B(H+1)(L-1)` Grover iterations on every branch. This includes all empty-set
trials, premature failures, large fibers, unsuccessful verifications, and aborts.
Counters up to L use O(r) bits. The loop decrement/control cost O(r) per iteration
is covered by the displayed gate-generation budget. Every trial's initialization,
coin production, measurement and reset is charged. The proof transcript need not
be retained: only S, current counters and outcomes are stored. Stream one gate
description at a time rather than allocating a circuit of exponential length.

Peak classical allocation is

    O(rn + (H+1)r + n + r) = O(n^2),

including input labels, lists, counters, sorting scratch and gate descriptions.
Peak quantum allocation, including the held original phase register, the search
register, sum/carry registers and equality/diffusion scratch, is `O(r+w)=O(n)`.
The address charge with this isolated allocation is `O(log(n+2))`. Bitwise
generation of wire indices, classical accesses and classically addressed gates
are all included in the resulting full-work bound

    T_prim = O(( B(H+1)L [r(w+1)+(H+1)(r+1)]
                 + H^2(r+1) + rn ) log(n+2))
           = O(2^(r/2) n^2 log(n+2)).                           (7.1)

If embedded in an algorithm retaining A bits/qubits of unrelated storage, replace
this address factor by `ceil(log2(A+O(n^2)+2))`; one cannot reuse the polynomial-
space address factor while simultaneously keeping an exponential table.

The primitive acquires no source copies and consumes r supplied phase qubits
even on failure. If supplied-input generators cost T_in,j and Q_in,j on a branch,
the attempt must charge `sum_j T_in,j + T_prim` and `sum_j Q_in,j` (including the
specified `(n+1) Q` source charge). Input-production scratch and retained siblings
must also be included by the caller. No all-N source-generation bound or complete
DCP sample envelope is claimed by writing `Q_prim=0`.

## 8. Exact supported local envelopes and scope of the gain

For every w<=n, (7.1) gives the supported *local* envelope

    B_T(n)=2^(n/2) n^2 log2 n,  B_C(n)=n^2, B_Qubits(n)=n,

for n>=2; the finite n=1 case is covered by the outside O constant. Their indices
are respectively `1`, `0`, `0`. Zero new source acquisitions can be bounded by
the representative envelope 1 (index 0), but this is not a complete-solver Q claim.

More usefully, if an external configuration proves
`w(n)<=c sqrt(n log2 n)+O(1)` for a specified positive rational c, then

    B_T(n)=2^((c/2) n^(1/2)(log2 n)^(1/2)) n^2 log2 n.            (8.1)

Its index is exactly 1/2, with c/2 retained, and the supported `bound` fields are

    coefficient: "1"
    exponent: [{coefficient: c/2, nPower: "1/2", logPower: "1/2"}]
    nPower: "2"
    logPower: "1"

Here c/2 is to be encoded as its reduced rational string, not as an unspecified
inner constant. Classical and quantum fields have empty exponent lists and
nPower "2" and "1", respectively. These are a parameterized local handoff,
not `dcp-bounds-v4` claims with the full-DCP scope or a submission package.

The factor `2^r` of an explicit exhaustive fiber scan has genuinely become
`2^(r/2)` with the same O(n^2)/O(n) local space orders. This does not halve a
whole solver's exponent: its number of recursive children, failures, discarded
source copies, extraction, arbitrary-modulus transformations and decoder work
still have to be charged. A `2^(c sqrt(n log n))` full-time envelope with fixed
c>0 would remain asymptotically slower than CS1's fixed-coefficient sqrt(n)
time envelope, regardless of equal coarse index 1/2.

## 9. Live comparison and provenance

Read-only `yukon submissions --all --json` refreshes at
`2026-11-06T19:02:54.974603+00:00` and `2026-11-06T19:04:40.945254+00:00`
returned 15 valid published rows. Exact rational comparison used the existing
`compare`, `context`, and `full_frontier` functions loaded without invoking
`refresh()` from `/Users/kaanm2/yukon-automining/dcp-sender-refresh.py`.
No queue/state snapshot was written by these reads. They combine like exponent
terms, include outside n powers as log-time terms, preserve inner coefficients,
match tolerance contexts, discard equal vectors by earliest time/ID, and ignore
only outside Big-O constants. `currentBestScore` was not used.

The six nondominated published IDs at the first refresh were:

    04669374-610b-497e-ae9b-c856335731ce
    59facd77-4082-40d9-910e-9060c197e72a
    f95bb4e2-3d08-4ca0-a34f-99841dca855a
    613ca17b-835c-4180-98af-b08f0c06c5bc
    d0c6b9b9-d80e-4bd7-95e1-e6267b61f2f0
    15f1d1c3-0ec1-45a3-92ea-f99fcefaef49

Newest published CS1 is `15f1d1c3-0ec1-45a3-92ea-f99fcefaef49`, published
`2026-11-06T19:00:54.173+00:00`, evaluated commit
`93a79cadf4c3270174860053caa4dd0530a63f27`, evidence `proof.md` SHA256
`2615b7a4802d9b8e3b529a2d8711c2652c92f13fdaf57b51f57b9f165e02a4c6`.
Its live exact envelope vector is

    T = n^4 (log2 n)^2 2^(a sqrt(n)),
    C = 2^(a sqrt(n) - 2 n^(1/4)),
    Qubits = n,
    Sources = n^(3/2) (log2 n) 2^(a sqrt(n)),
    tolerance = 0,

where the exact rational a is

    8441478004666748666153322414015794961054342923175177808658686557734489303162152388494751245868147491831446292476962720233203201073933816582585276436077865535199430405176591394221939485167179701583924490203278327423413823406808776174974568608124494762509770/
    5969026340336944451114480739433819709407468170415945417713771714885974444504222882421291476798989652766383498455240579454394404150586732509003361709530480614304768144606668970442415970951831495263198155709406532002051594173677103082229495028847707209502393.

The exact fifth error-model context is:

> Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The newly published source Section 6 was read through the GitHub connector at
https://github.com/Layr-Labs/dcp/blob/93a79cadf4c3270174860053caa4dd0530a63f27/submission/proof.md
(requested lines 327-424). It supplies the existing general collimation context,
equal-magnitude measurement principle and explicit charged table-lookup model;
it does not establish the bounded Grover primitive here.

The user-pinned earlier CS1 source was separately read with `git show` in the
existing `/Users/kaanm2/yukon-automining/dcp-l2` repository, without a fetch or
checkout. Its commit is `200ef0387acb280adcd272f4fbcdb805d1786bbe`; the actual
`submission/proof.md` bytes hashed to
`e1b698d021f72cc5fd17f0132a2c30ba213dc2c424e613087d711804f074b528`.
Published identity: `f1481815-9577-4990-abe3-7b79fa5d9284`.

`3988996f-c9ac-41f2-8e30-1472a94502a4` was valid/published but absent from the
computed frontier, as required by the SLS dominance correction. Protected
`16bb6065-c3ca-45fb-b514-86106a310646` remained validating on the second refresh;
its proof was not opened or re-reviewed. Nothing in this local theorem is a claim
to replace it or to advance the full published resource vector.

**Final refresh superseding those status counts:** at
`2026-11-06T19:09:54.769817+00:00` there were 18 valid published rows. The exact
frontier IDs became `f95bb4e2-3d08-4ca0-a34f-99841dca855a`,
`613ca17b-835c-4180-98af-b08f0c06c5bc`, `d0c6b9b9-d80e-4bd7-95e1-e6267b61f2f0`,
`15f1d1c3-0ec1-45a3-92ea-f99fcefaef49`, `16bb6065-c3ca-45fb-b514-86106a310646`,
and `6c59d152-b326-4817-a244-31a15b3cd9d8`. PSR2 published at
`2026-11-06T19:07:20.866+00:00`; this is a live-metrics observation, not a proof
review. `row_comparison(SLS,398)` returned exactly `[-1,0,0,-1,0]`.

A final time-only exact comparison at `2026-11-06T19:10:23.055740+00:00` still
selected the CS1 time envelope; the earlier `f1481815` row and newer `15f1d1c3`
have the same time envelope, while the newer full vector improves classical
memory. The new rival `6c59d152` (evaluated commit
`e74e74baffd61fd9f4a0b57b075591ed96994aa5`, published
`2026-11-06T19:09:25.876+00:00`) has the exact same clean error-model text and
zero tolerance, with normalized vector

    T = n^4 2^((1553/736) sqrt(n)),
    C = n^(3/2) (log2 n)^(-1) 2^((23/32) sqrt(n)),
    Qubits = n,
    Sources = n^(1570/529) (log2 n)^(1024/529) 2^((32/23) sqrt(n)).

Its time coefficient 1553/736 is larger than the exact CS1 coefficient a; its
appearance does not change the full-time target. Its source theorem was also
read at the pinned commit through the GitHub connector (lines 1-65). No full
vector gain is being claimed for this local primitive.

Instruction-input SHA256s recorded at the final write boundary:

    rules.md: 7be4f5f1137aea419a481bf31482bebc5a8f8cbb15dd2296872fce6dbad7a469
    COORDINATION.md: 8fac6920633297f3e8a664bc7f88b80c75b15829a886941299d90604a1902bb8
    dcp-COMPARATOR.md: 547cb55ea5c06cce8a603404dff1727a8b11cd72a2b0d63f0e7cabfa6bb09dfb

Material inputs to this result are the candidate in COORDINATION.md, the explicit
BBHT random-iteration identity, and the standard collimation/unused-label principle
present in the cited CS1 source. The new work is the complete bounded-list
instrument, exactness with incomplete lists, adaptive failure proof, conditional
cyclic uniform-output law, and full primitive accounting. No CS1 source extractor
or full-secret decoder is adopted as an unproved black box in this theorem.

## 10. Remote Wolfram check: code, assumptions and output

Used the already connected `mcp__wolfram__WolframLanguageEvaluator`, stateless,
`timeConstraint:20`. One prior narrow WolframContext request returned no useful
search result; it was not a proof input. No local engine, installation or license
operation was attempted.

Exact code:

```wl
Clear[dd, tt, ww];
<|"UnionMissExact" -> 1024 (3/4)^48,
  "UnionMissLT1over256" -> (1024 (3/4)^48 < 1/256),
  "YieldLower" -> (1 - 1/16 - 17/1024 - 1/256),
  "MarginOver7over8" -> (1 - 1/16 - 17/1024 - 1/256 - 7/8),
  "FiberMean" -> FullSimplify[1 + (2^(ww + 4) - 1)/2^ww,
    Assumptions -> Element[ww, Integers] && ww >= 0],
  "GroverCapSuffices" -> FullSimplify[
    dd/(2 Sqrt[tt (dd - tt)]) <= Sqrt[dd],
    Assumptions -> Element[{dd, tt}, Integers] &&
      dd >= 2 && 1 <= tt <= dd - 1]|>
```

Raw textual result:

```text
Out[1]= <|"UnionMissExact" -> 79766443076872509863361/77371252455336267181195264, "UnionMissLT1over256" -> True, "YieldLower" -> 939/1024, "MarginOver7over8" -> 43/1024, "FiberMean" -> 17 - 2^(-ww), "GroverCapSuffices" -> True|>
```

All constants in this check are exact rationals. The assumptions are integer
`ww>=0`, integer `dd>=2`, and integer `1<=tt<=dd-1`. The result checks arithmetic
and an elementary search-cap inequality only. It does not prove the quantum
conditioning, independence, all-N source access, or full-secret recovery; those
first two assertions are proved in Sections 3-6, and the latter two remain outside
this primitive's scope.

A second stateless remote evaluator job, also with `timeConstraint:20`, checked
all low-label assignments for the finite cases w=0,1,2. Exact code:

```wl
Table[Module[{q = 2^ww, rr = ww + 4, xs, av, hs, meanH, maxOdd},
  xs = Tuples[{0, 1}, rr];
  av = Tuples[Range[0, q - 1], rr];
  hs = (Values[Counts[Mod[xs.#, q]]] &) /@ av;
  meanH = Total[(Total[#^2] &) /@ hs]/(Length[av] 2^rr);
  maxOdd = Max[(Total[Mod[#, 2]] &) /@ hs]/2^rr;
  {ww, Length[av], meanH, 17 - 2^-ww, maxOdd, maxOdd <= 1/16}],
  {ww, 0, 2}]
```

Raw output (columns: w, number of low-label vectors, measured-fiber mean,
predicted mean, maximum odd leftover mass, bound check):

```text
Out[1]= {{0, 1, 16, 16, 0, True}, {1, 32, 33/2, 33/2, 0, True}, {2, 4096, 67/4, 67/4, 0, True}}
```

These are exhaustive finite arithmetic checks over the stated integer sets.
The zero odd masses in these small cases are not extrapolated; the general proof
uses only the bound 1/16. They provide no substitute for the quantum-state proof.

## 11. Handoff boundary

The proven primitive is ready for a caller's resource recurrence. To obtain a
complete DCP theorem the caller must supply exact-label ideal input production
with an actual-source coupling, compatible arbitrary-N label laws, a full-secret
decoder, branchwise global cutoffs and a joint resource proof. In particular,
do not condition away source-label errors, treat a signed interval frequency as
a cyclic uniform label without its period hypothesis, or call a polynomial-space
sqrt(n log n) tradeoff a CS1 full-time improvement.
