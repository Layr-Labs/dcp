# Exact all-N recursion by retaining integer carries

Research-only first pass, 2026-11-06 UTC. This file is the only mutation by
this lane. No publication, reservation, checkout, monitor operation, or PSR2
READY inspection was performed.

**Result.** The V-extra-trials arbitrary-N reduction in `../astra-sieve.md`
is unnecessary. Keep the *integer* difference label at each Regev combination,
including its dyadic carry. Its final multiplier has an explicit characteristic
function bound from a never-inspected top bit. The already published CS1
free-frequency decoder then recovers the odd part of the secret; controlled
source shifts recover its 2-adic part. Original-copy cost is O(V poly(n)), with
the V from the prior dyadic solver, rather than O(V^2). Using actual modulus
depths tightens this to O(V); (1) uses a uniform n-only cap. This is an exact mixed-source
construction, apart from the explicitly budgeted classical-label errors of
`../label-extraction.md`. It requires no approximate coset-source conversion.

The unconditional, exhaustive-combination implementation below has, jointly,
for every N,s and with success greater than 2/3,

```
x = sqrt(n log2 n), n = ceil(log2 N), n >= 2:
T   = O(n^7 2^((3/2)x + (5/4)sqrt(n)))
S_C = O(n^2)
S_Q = O(n)
Q   = O(n^3 2^((1/2)x + (5/4)sqrt(n))).                 (A)
```

The four exact indices are `1/2, 0/1, 0/1, 1/2`. These are conservative
supported envelopes, not optimized polynomial factors. Section 9 gives the
fast-fiber contract with time exponent `x + (5/4)sqrt(n)`; Section 9.1
instantiates it using the completed QF48 sibling proof. Neither is a global time improvement over CS1's
`sqrt(2n)` exponential. The new contribution here is the explicit composition
removing the old arbitrary-N source penalty; the decoder, CRT idea, and
held-out-bit method are materially reused from CS1, not claimed as discoveries.

## 1. Inputs, parameters, and the exact source interface

All source copies are independent ideal mixed states from `rules.md`. No
purification, inverse preparation, coherent source control, hidden-function
oracle, QRAM, or subset-sum oracle is used. Logarithms are base two.

For n>=2 set

```
b = ceil(sqrt(n log2 n)), r = b+4,
D = ceil((n-1)/b), A = 16r/15, R = r^D,
K = 8192 (ceil(log2 R) + ceil(log2 n) + 30),
F = n K + 2n + 1,
C = ceil(3000 F A^D), q_label = ceil(log2(1000 C)).       (1)
```

All quantities are computed by finite integer/rational arithmetic. To compute
b, compare `2^(b^2)` with `n^n`; to compute the log ceilings, use integer bit
lengths and exact power-of-two tests. No real-arithmetic advice is used.
Parameters require polynomially many bit operations and O(n^2) space. Later
bounds show `log C=O(n)`. The algorithm has one global cap C on counted nodes,
as defined in Section 6. Attempting to exceed it aborts and outputs zero.

Use the channel E_(N,q_label) of `../label-extraction.md` on each acquired
original copy. The exact identity underlying that channel is

```
rho_s = (1/N) sum_k |phi_k(s)><phi_k(s)| tensor |chi_k><chi_k|,
phi_k(s) = (|0> + exp(2 pi i k s/N)|1>)/sqrt(2).
```

The ideal reference replaces the reported label by its latent k. Its retained
qubit is exactly the displayed one, k is uniform, and source copies are
independent. In the actual circuit the retained qubit is still exactly that
of its latent component, but the reported label can be wrong. The per-copy
classical-label/qubit error is at most `2^-q_label`, uniformly in the secret.
Section 7 compares complete capped executions, rather than conditioning on
all extractions having succeeded.

For a known unit alpha modulo N, no quantum multiplication is necessary:
classically relabel k as `l=alpha^(-1) k mod N`. Then l is uniform on Z_N and
the same qubit has phase `exp(2 pi i l alpha s/N)`. If P is the largest power
of two at most N, keep this qubit iff `l<P`. Acceptance is **exactly P/N>1/2**
(or 1 when N=P); conditional labels are exactly uniform on `[0,P)`.
This is rejection of a *Fourier label*, after exact spectral extraction.
It is not projection of the source address onto a dyadic window.

## 2. Exact carry-retaining combination lemma

Fix a real theta and an integer m>=1. A level-c input is a qubit

```
(|0> + exp(2 pi i L theta)|1>)/sqrt(2),
```

with a known **signed integer** L divisible by `2^c`. Its residue modulo
`2^m`, divided by `2^c`, is uniform on `Z_(2^(m-c))`. Inputs to a call are
independent and come from disjoint source copies. Let
`1<=w<=min(b,m-1-c)` and use `r_w=w+4` such inputs.

On the tensor product compute and measure

```
f(z) = sum_j (L_j/2^c) z_j mod 2^w, z in {0,1}^(r_w).
```

In the measured fiber, pair consecutive members in lexicographic order.
Measure the pair index and reject an unpaired final member. For a retained
pair z0,z1, clear all but its branch bit by a reversible two-string map.
Store the **integer**, not reduced, output label

```
L' = sum_j (z1_j-z0_j) L_j.                              (2)
```

The output state has exactly phase `exp(2 pi i L' theta)`, and `2^(c+w)|L'`.
The pairing measurement is diagonal; all its probabilities depend only on
the measured fiber and its cardinalities, not on theta. At most one string
per fiber is rejected. Therefore success is at least
`1-2^w/2^(w+4)=15/16`, for **every** low-label assignment.

Conditioned on the low labels and selected pair, the high residues remain
independent uniform. At least one difference coefficient is +1 or -1, so
`L'/2^(c+w) mod 2^(m-c-w)` is uniform. Carries can correlate with these
residues; no independence of the integer carry is asserted or needed.
All selection, success, and retry decisions must inspect only the specified
low bits, never the retained high carry.

This operation is explicit in polynomial space. After measuring the residue,
scan all `2^(r_w)` bit strings classically. For every member of the fiber,
reversibly add its comparison with the quantum input to a rank accumulator.
Measure the paired rank, scan again for its two strings, and clear the rank
and input registers using the known pair. The scan stores only counters,
the r_w labels, two strings, and O(r_w) quantum scratch. This is the actual
implementation here, not a subset-sum query or uncharged classical list.

Depth-first recursion removes blocks of at most b bits until `c=m-1`.
Level zero supplies a uniform label in `[0,2^m)`. Failed calls discard all
their inputs and recurse afresh. A successful depth-d tree has a label

```
L = sum_(j in active leaves) epsilon_j l_j,
epsilon_j in {-1,0,1}, at most r^d leaves,
L = 2^(m-1) W, |W| < 2 r^d <= 2R.                       (3)
```

The nonzero coefficient vector is justified inductively: a selected pair
differs in at least one child branch, and children have disjoint leaf sets
and nonzero coefficient vectors. Thus cancellation between distinct children
cannot erase all leaf coefficients. Retry trees are discarded and are not
part of the retained linear combination. Their cost is still charged.

## 3. The held-out-bit lemma, including conditioning

Write every accepted leaf label as

```
l_j = u_j + 2^(m-1) tau_j, 0<=u_j<2^(m-1), tau_j in {0,1}.
```

Before any tree processing, all tau_j are independent fair bits, independent
of u_j. Define G to contain all u_j of all attempts, all residue/pair outcomes,
all low-bit selection/search coins, and all retry decisions. It excludes the
held-out tau_j, root X/Y measurements, and extractor transcripts. The ideal
extractor transcripts are unused and averaged out, not conditioned upon.

For fixed labels, every internal measurement is diagonal on distinct basis
strings with equal magnitude. Its law depends only on the low-bit fibers.
Adding `2^(m-1) tau_j` to a leaf changes none of those fibers at any level.
Consequently the joint law factorizes into the independent fair tau_j law
and a law of G depending only on the u_j and low-bit randomness. This proves
the claim also through arbitrarily many uncapped retries using fresh copies.
The global cap is dealt with later by coupling, not by conditioning on it.

Conditional on G, the returned integer multiplier has the form

```
W = c_G + sum_j epsilon_j tau_j,
c_G an integer, epsilon_j in {-1,0,1}, t=sum_j |epsilon_j|>=1.
```

For every real z,

```
| E[exp(2 pi i z W) | G] | = |cos(pi z)|^t <= |cos(pi z)|. (4)
Pr[W odd | G] = 1/2.                                    (5)
```

This is an exact identity: a fair Bernoulli bit contributes the factor
`exp(plus-or-minus pi i z) cos(pi z)`. It applies to the arbitrary-modulus
phase denominator theta just as it does to a dyadic denominator. It is the
specific distributional contract needed by CS1's decoder. Uniformity of W
on an integer interval is neither true in general nor assumed.

**Concrete carry error if omitted.** With N=5, labels 3 and 1, theta=s/5,
the even-parity two-qubit projection contains `|00>+exp(2 pi i 4s/5)|11>`.
Its difference label is the integer 4. Reducing it modulo the dyadic P=4
would label this as zero and predict |+>. For s=1 its actual trace distance
from |+> is `|sin(4pi/5)|=sin(pi/5)>0`. All operations in this example are
Clifford operations; this is not a Fourier-precision issue.

## 4. Odd part, with a fully specified decoder

Write `N=2^v M`, M odd, by removing trailing zero bits. No integer
factorization subroutine is needed. If M=1 skip this section. Otherwise put
`m=floor(log2 N)`, `B=m-1`; then `B>=v`, since M>=3.
The unknown target is `theta=s1/M`, `s1=s mod M`.

For each stage j=0,...,J, with

```
J = min{j>=0: 2^(j+3)>2M}, so J+1<=n,
```

compute the unit alpha_j modulo N determined by

```
alpha_j = 1 mod 2^v,
alpha_j = 2^j (2^(B-v))^(-1) mod M.                      (6)
```

Extended Euclid and CRT implement this with polynomial counted classical
work; for v=0 only the second congruence matters. A fresh accepted leaf is
the relabelled Fourier phase qubit of Section 1 with l<2^m. A tree root is

```
(|0> + exp(2 pi i 2^j W theta)|1>)/sqrt(2), |W|<2R,        (7)
```

because `2^B alpha_j s/N = 2^j s1/M mod 1`. CRT here selects a known unit;
there is **no CRT measurement, source conditioning, or CRT rejection loss**.

Acquire K independent roots per stage. Measure each in X or Y, chosen by an
independent fair bit beta_i, and record `(W_i,beta_i,Z_i)` where Z_i=+1 or -1.
Do not discard W=0 or even W. Every root is consumed by this decoder.

The following is the CS1 Section 9 decoder, with R in place of its leaf bound.
It is reproduced here to make this composition reviewable without source
upgrades or an external theorem.

Let `P_j=j+ceil(log2 R)+8`. Candidate c denotes `zeta=c/2^P_j` on the circle.
At j=0 enumerate all such c. At j>=1 enumerate the candidates within
`rad_j=2^(-j-2)` of the previous center z_(j-1). Endpoints are grid points;
the arc has one or two explicit integer intervals. At every stage the number
of candidates is at most `2^(ceil(log2 R)+8)`.

Use a fixed, uniformly generated rational table `tab_beta(x)` satisfying

```
|tab_0(x)-cos(2 pi x)| < 1/625,
|tab_1(x)-sin(2 pi x)| < 1/625.                            (8)
```

One fully counted construction is CS1 Section 4: approximate pi by the first
40 terms of each alternating series in `16 atan(1/5)-4 atan(1/239)`; tabulate
sin and cos at the 4096 grid points with Taylor polynomials through degree 80,
round to denominator 2^20, and use the lower grid point. The alternating
arctangent tail is below 2^-91; the Taylor remainder on [0,7] is at most
`7^81/81!<2^-170`; rounding and grid error total below `2pi/4096+2^-20<1/625`.
This is a fixed finite computation and O(1) table, not preloaded advice.
Rational arithmetic and all lookup addresses are charged.

Compute

```
score(c) = sum_i Z_i tab_(beta_i)(frac(2^j W_i c / 2^P_j)).
```

Return the least maximizing candidate as z_j. Stream the enumeration and
keep only K records, K running residues, and the best candidate. No table
of the O(R) candidates is allocated.

**Correctness.** If the candidate arc contains theta, the nearest candidate
zeta_0 has `|2^j W_i(theta-zeta_0)|<2^-8`. For the ideal score summand
`xi_i=Z_i cs_(beta_i)(2^j W_i zeta)`, averaging the random basis gives

```
E[xi_i | W_i] = (1/2) cos(2 pi 2^j W_i(theta-zeta)).
```

The near candidate's conditional expectation is at least
`(1/2)cos(pi/128)`. For a candidate at circular distance at least
`2^(-j-3)`, both points are in the same candidate arc (or on the full circle
at j=0), so `2^j |theta-zeta| in [1/8,1/2]`. Equation (4), followed by
averaging G, bounds its expectation by `(1/2)cos(pi/8)`. This step uses the
held-out-bit proof, not any numerical distribution test.

For each fixed candidate, independent-root bounded-variable concentration
gives a deviation of K/64 with probability at most `exp(-K/8192)`. The same
bound follows by conditional Hoeffding if the previous-stage history is
fixed. Summands lie in [-1,1], and the computed/ideal score difference is
at most K/625. The strict separation is

```
(1/2)(cos(pi/128)-cos(pi/8)) > 2/64 + 2/625.
```

A union bound over the near and all far candidates, at most
`2^(ceil(log2 R)+9)` events, gives stage failure at most `2^-20/n` with K
from (1). Therefore, with probability at least `1-2^-20`, all stages give
`dist(theta,z_j)<2^(-j-3)`. This is exactly the next arc hypothesis.
Finally `dist(theta,z_J)<1/(2M)`; rounding `M z_J` modulo M gives s1.

## 5. Full-secret recovery, including the 2-adic part

After obtaining s1, write `s=s1+M s2 mod N`, `s2 in Z_(2^v)`.
If g low bits a of s2 are known, transform each **fresh original** source
copy by subtracting `s1+M a` from its address on branch 1. This is an exact
controlled modular permutation, producing the mixed source with shift
`M 2^g t`, where `t=(s2-a)/2^g in Z_(2^(v-g))`, provided s1 and a are right.

Extract its Fourier label k over the original N and set
`l=k mod 2^(v-g)`. Since this power of two divides N, l is exactly uniform
on that dyadic modulus. The retained phase is exactly

```
exp(2 pi i l t/2^(v-g)).                                 (9)
```

Run the same recursion to remove `v-g-1` bits. Its integer output has
phase `exp(pi i W t)`. With probability exactly 1/2, W is odd; retain those
roots and measure X to read the next bit exactly. A zero-depth tree covers
`v-g=1`. Repeat for all v bits. Output `s1+M s2 mod N`.

No guess of s1 is tried in a separate sieve run. Its decoder returns one
answer with the proved error probability. Incorrect s1 histories can give
arbitrary answers, but all loops and memory remain capped on those histories.
For N a power of two this section alone applies, with s1=0 and M=1.
For N=2 use the following specified finite branch: test candidates 0 then 1,
using eleven fresh copies per candidate; controlled-subtract the candidate and
measure the first qubit in X. Accept only if all eleven outcomes are +. The
correct candidate always passes, and a wrong one passes with probability
2^-11. Output zero if neither passes. Resources are absolute constants.

## 6. Source, retry, and all-branch node accounting

A counted node is either one **original acquisition attempt** (including a
rejected Fourier label) or one combination attempt (including a failed pair).
Do not double-count a retry as a separate node; it starts a new combination
attempt and new children. The source cap is implied by the global node cap C.
Stop before starting a node that would exceed C. An aborted branch outputs
zero and releases all allocated registers. Parameter and decoder loops have
fixed bounds independent of success.

In an ideal uncapped recursion, let a_i be the expected counted nodes until
one level-i output. A level-zero accepted leaf costs at most 2 expected
acquisitions; in the 2-adic part it costs one. For a combination call,
success is at least 15/16, independently of phases, and fresh attempts have
the same distribution. With `A=16r/15`,

```
a_0<=2,
a_i <= A a_(i-1) + 16/15,
a_i <= (2+1/(r-1)) A^i <= 3 A^i.                        (10)
```

The last geometric-series bound also covers smaller final blocks, whose
arity is at most r. The odd part uses at most nK roots. The 2-adic part
uses a mean of two roots per bit by (5). Each depth is at most D. Hence
the expected total node count of the whole ideal uncapped solver is at most

```
3 (nK+2n) A^D < 3 F A^D.
```

Markov gives cap probability at most 1/1000. This accounts for **all**
label rejections, failed fibers, failed odd-multiplier tests, and retries.
It does not replace a worst-case bound by an expected one: the algorithm's
actual branchwise node bound is the explicit integer C.

## 7. Exact gates, finite label error, and joint success

Combine source extraction, classical relabelling, diagonal fiber measurement,
rank scans, two-string compression, X/Y measurements, and controlled source
subtraction. All quantum operations are NOT/CNOT/Toffoli/H/S and basis
measurements. Toffoli has a constant-size exact Clifford+T decomposition,
given explicitly in `../label-extraction.md`. No generic-angle quantum
rotation, quantum Fourier transform, or gate-synthesis oracle is invoked.
The trigonometric table in the decoder is entirely classical.

The cap holds even for wrong extracted labels. In the ideal-source reference,
each fresh input after a known controlled shift is again an ideal coset,
whether that shift was the right guess or a wrong guess. Relabelling and
all later operations are channels. The label-extraction hybrid bound on at
most C fresh calls is therefore

```
C 2^-q_label <= 1/1000.                                 (11)
```

Until this hybrid diverges, every label used in the classical recursion is
the latent correct label. No conditioning on the extractor-success event
is used to infer uniform high bits.

The ideal uncapped decoder fails with probability at most 2^-20; given its
correct odd-part answer, all ideal 2-adic measurements are exact. Capping
changes success by at most 1/1000 and label extraction by at most 1/1000.
Thus the single actual capped algorithm has unconditional success at least

```
1 - 2^-20 - 1/1000 - 1/1000 > 2/3                        (12)
```

for every N,s, jointly with its branchwise bounds.

## 8. Charged resources and rational supported envelopes

Pending phase qubits: at most O(rD)=O(n) under depth-first recursion. Full
signed integer labels have `O(n+D log r)=O(n)` bits by (3). Their total
classical storage is O(n^2). One active rank scan, controlled modular
subtraction, or label extraction needs O(n) quantum scratch, reused between
calls. Hence S_Q=O(n).

Each stage stores K records and residues of O(n) bits; here
`K=O(D log r+log n)=O(sqrt(n log n))=O(n)`. They fit in O(n^2) bits and are
discarded after the stage. Table generation, Euclid/CRT, counters, and
parameter arithmetic fit in O(n^2) classical bits. Stream all circuit
descriptions. S_C=O(n^2), so every classical indexed access, gate address,
and generated wire index pays O(log n) bit operations. These charges are
included below, not treated as unit-cost RAM.

An exhaustive combination scans at most `2^(b+4)` strings with O(n^2)
bit/gate arithmetic per string and address/generation charges. The source
extractor has charged work `O(n^2(q_label+log n)log(n+q_label+2))`; since
`q_label=O(n)`, this is `O(n^3 log n)`. Classical relabelling, subtraction,
bookkeeping, and modular inverses are polynomial. A conservative charged
bound per counted node is `O(2^b n^4)`.

The decoder evaluates O(R) candidates at each of at most n stages, with K
records per candidate. Exact modular products on O(n)-bit rationals and
all addresses cost O(n^3) per record as a conservative bound. Its total
work is `O(n K R n^3)`, bounded by `O(C n^3)` because R<=A^D. Fixed
setup is polynomial and absorbed by the same bound. Therefore

```
Q <= C,
T = O(C 2^b n^4), S_C=O(n^2), S_Q=O(n).                 (13)
```

The old dyadic solver defined `V=ceil(100 n^2 A^D)`, with depth computed
from the actual lower dyadic modulus. Using that actual depth in (1),
`K=O(n)` and thus `C=O(V)`. A uniform n-only bound uses D from (1), which
differs by at most one from that actual depth; alternatively keep the
actual depth throughout the odd part and use the at-most-one larger dyadic
part. In either convention this is `O(V poly(n))`, and for non-dyadic N
the 2-adic depth is no larger than the odd-part depth, giving O(V) directly.
This is the removed V-factor in original copies; no acceptance probability
was silently set to one.

For explicit envelopes put `L=log2 n`, `x=sqrt(nL)` and n>=16. Since
`b<=x+1`, `r<=x+5`, one has `A<=2x`, and `D<=n/x+1`. Therefore

```
log2 A^D
 <= (n/x+1)(1+L/2+(log2 L)/2)
 <= x/2 + (5/4)sqrt(n) + L + 1.                         (14)
```

Here `1/sqrt L<=1/2`, `log2 L<= (3/2)sqrt L`, and `log2 L<=L` for L>=4.
The middle inequality can be verified by maximizing `log2 L/sqrt L`;
its maximum is `2/(e ln 2)<3/2`. Since F=O(n^2),

```
C=O(n^3 2^(x/2+(5/4)sqrt n)),
2^b=O(2^x).
```

Substitution in (13) gives (A). The algorithm remains as specified for
2<=n<16, with finite costs covered by absolute outer constants; it does not
switch to an asymptotically exponential search.

The exact rational `bound` components, in T,S_C,S_Q,Q order, are:

```json
[
  {"coefficient":"1","exponent":[{"coefficient":"3/2","nPower":"1/2","logPower":"1/2"},{"coefficient":"5/4","nPower":"1/2","logPower":"0"}],"nPower":"7","logPower":"0"},
  {"coefficient":"1","exponent":[],"nPower":"2","logPower":"0"},
  {"coefficient":"1","exponent":[],"nPower":"1","logPower":"0"},
  {"coefficient":"1","exponent":[{"coefficient":"1/2","nPower":"1/2","logPower":"1/2"},{"coefficient":"5/4","nPower":"1/2","logPower":"0"}],"nPower":"3","logPower":"0"}
]
```

Common metadata, if centrally integrated later: version `dcp-bounds-v4`,
comparator `asymptotic-v1`, scope `dcp-cyclic-group-order`, model
`dcp-uniform-clifford-t-bit-operations-v1`, notation `big-o`.
The fifth expression is `0`. To match the actual CS1 context exactly its
error-model text would be:

> Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Positive tolerance is not claimed. These are research artifacts, not a
submission, acceptance, or publication instruction.

## 9. Conditional fast-fiber replacement: exact obligations

Replace only the combination implementation, not the all-N argument. The
following contract is sufficient and must be proved by that primitive's owner:

1. For w+4 independent inputs with independent uniform low w-bit labels,
   per-attempt success is at least 7/8, averaging its explicit bounded search
   coins and diagonal measurements. Every successful output is a genuine
   two-string compression with the **exact integer** difference (2).
2. Every selection, rejection, search predicate, search stopping decision,
   projection, and compression outcome depends on low labels and search
   randomness only. Its conditional law does not inspect held-out high bits
   or depend on unknown phase. Quantum search must be on a separate explicit
   register, with counted reversible predicates and no source inversion.
3. On every branch it costs `G(n,w)`, uses O(n) extra qubits and O(n^2)
   classical bits, and produces no unchecked phase error on success.

The exact proof above then applies with `A=8r/7`, the same R,K,F,
`C=ceil(3000 F A^D)`, and the same extraction budget. The recurrence (10)
uses 8/7 instead of 16/15; its `3 A^i` bound still holds. Success need only
be uniform for the fresh independent input distribution; it need not be
7/8 for every fixed low-label instance. The held-out-bit factorization is
what prevents that average guarantee from being spoiled by retries.

If, additionally, the fully charged branchwise bound is
`G(n,w)=O(2^(w/2) n^4)`, then

```
T   = O(n^7 2^(x+(5/4)sqrt n)),
S_C = O(n^2), S_Q=O(n),
Q   = O(n^3 2^((1/2)x+(5/4)sqrt n)).                     (15)
```

Indeed `8r/7<=2x` for n>=16, so (14) remains valid. The conditional structured
T bound is the first bound in Section 8 with `3/2` replaced by `1`; the
other three bounds and indices are unchanged. If the primitive establishes
only `poly(n)` without a degree, retain (13) with G explicitly; do **not**
promote (15) to a supported unconditional envelope on that weaker premise.

This composition never requires the output integer multiplier to equal 1,
nor retries a full solve until a guessed controlled shift is close. Those
are the two potential exponential sample penalties avoided here.

### 9.1 Late-arriving QF48 instantiation

At 19:09 UTC the completed sibling `quantum-fiber.md` became available and
was read. Its Sections 3--7 prove precisely the additional properties above:
general real-theta integer-difference correctness, verified-set projection
even on incomplete enumeration, low-only transcript likelihood, average yield
939/1024>7/8, and charged work `O(2^((w+4)/2) n^2 log(n+2))`.

To instantiate it here, at level c pass **b_j=L_j/2^c** and real phase
parameter `2^c theta`; retain its general signed integer output, multiplied
back by `2^(c+w)`. Do not invoke its narrower cyclic-pure-state output
contract. Its low residues are independent uniform by Section 2, while its
search and projection use only those residues. Section 3 of this note then
proves the required held-out-leaf-bit law across all levels. Negative integer
labels are handled by their nonnegative low residues in the predicate and
signed classical arithmetic for the output; the argument and gate count do
not change. Their bit width is O(n), as proved above.

Thus (15) is a joint **compositional research corollary** of the proved QF48
primitive and Sections 1--8 here, with A=8r/7 and the explicit C in Section 9.
The primitive's input-production obligation is discharged by this construction;
the all-N construction's fast-combination obligation is discharged by QF48.
Every acquired copy, failed attempt, address charge and label-error hybrid is
still accounted for by the same C. No heuristic subset-sum distribution or
source upgrade is introduced by the composition. This is not a hosted verdict
or permission to publish. The exhaustive implementation (A) remains an
independent fallback theorem not using the sibling primitive.

## 10. Source-channel obstruction respected

Sibling `source-channels.md` Section 5 proves: for N=2L-1, dyadic L, the
fixed address-window filter `[0,L)` with failures erased has output trace
distance exactly 1/N per acquisition for secrets L-1 and L. Every q-copy
full-secret algorithm using only that fixed filtered stream needs q>=N/3.
Constant acceptance L/N does not make that stream a good dyadic source.

The present algorithm is outside that obstruction for a precise reason:
it never applies the address-window filter. It performs modular-translation
label extraction on the entire original copy, retains the exact original-N
phase, and rejects a classical **label** only. The actual integer carry is
kept. CRT is arithmetic on units, and source shifts act before fresh label
extraction. No discarded CRT register is assumed to be coherently erased.
The sibling's obstruction is not a general all-N impossibility theorem.

## 11. Provenance, comparator refresh, and status

Material reuse:

* `../astra-sieve.md`, Sections 1,2,5,6: lexicographic fiber pairing, depth-first
  recursion, exact-gate rank scan and label extraction interface. Its
  approximate source projection and V-trial wrapper are **not** used.
* `../label-extraction.md`: exact mixed-state spectral identity, bounded
  modular-translation decoder and its explicit charged implementation.
* Published CS1, source commit `200ef0387acb280adcd272f4fbcdb805d1786bbe`,
  `submission/proof.md`, SHA-256
  `e1b698d021f72cc5fd17f0132a2c30ba213dc2c424e613087d711804f074b528`:
  Sections 4,8,9,10 supply respectively the classical trig table,
  held-out-bit characteristic bound, free-frequency decoder, and source-shift
  2-adic recovery. Read from that exact git object. The decoder and identities
  are reproduced above, so no verdict or unexplained citation is a premise.
* Regev, *A Subexponential Time Algorithm for the Dihedral Hidden Subgroup
  Problem with Polynomial Space*, arXiv:quant-ph/0406151v1, Section 3,
  https://arxiv.org/abs/quant-ph/0406151v1: historical subset-fiber recursion.
  Read primary PDF during this pass. Its simplifying dyadic assumption and
  hidden-function reductions do not supply an all-N source reduction here.

Read-only live publication refreshes used `yukon submissions --all --json`
directly, not the sender script (which writes queue state). At
`2026-11-06T19:02:40.299767Z` there were 15 valid published rows; at
`2026-11-06T19:04:24.701379Z` there were 16. Comparisons combined exact
rational exponent terms and included outside n powers as log terms. The
smallest full time was still the CS1 envelope
`n^4 (log2 n)^2 2^(a sqrt n)`, a=u_333/v_333>sqrt(2), unchanged in the new
rows. The older CS1 row was `f1481815-9577-4990-abe3-7b79fa5d9284`.
New row `15f1d1c3-0ec1-45a3-92ea-f99fcefaef49`, published at 19:00:54.173Z,
had the same T,Q,S_Q and classical exponent `a sqrt n - 2 n^(1/4)`;
`6e91de62-9a4f-4f08-bfa8-1beacca11e0f`, published at 19:03:25.588Z, had
the same complete vector as that new row, so the earlier equal-vector row
wins. The latter's source commit `f248f9f242c21046223007c9462332b9d738e0bb`
was not available in the local object store (`fatal: bad object`); its proof
was not silently substituted for the verified original CS1 source.

For (A), the log-time difference from CS1 contains the positive leading term
`(3/2)sqrt(n log2 n)`; for conditional (15) it contains `sqrt(n log2 n)`.
Both dominate any fixed-coefficient sqrt(n) term, including CS1's exact a.
Thus this work does **not** achieve the primary strict fastest-time goal.
It supplies the requested exact all-N composition and a sample/polyspace
tradeoff route. No frontier membership claim is made. The stated PSR2
benchmark is context only and its READY proof was not inspected.

Input hashes recorded during this pass:

```
rules.md: 7be4f5f1137aea419a481bf31482bebc5a8f8cbb15dd2296872fce6dbad7a469
COORDINATION.md (19:04 read): 8fac6920633297f3e8a664bc7f88b80c75b15829a886941299d90604a1902bb8
../astra-sieve.md: fec805a997cddd476041b06fda0c9c51e7f5e7036aa6490ca3ef8dcec2907ad6
../label-extraction.md: dcf1d5c07aa20e136e0ca852b249c6b9b20f9ef970776b162e22981860ee1222
source-channels.md: d70ca04cacaceaaf470ff44b1360f72281bd95944d7b5597c5f21cffee5a885f
/Users/kaanm2/yukon-automining/dcp-COMPARATOR.md: 547cb55ea5c06cce8a603404dff1727a8b11cd72a2b0d63f0e7cabfa6bb09dfb
```

## 12. Required remote Wolfram evidence

One narrow WolframContext call asked for rational simplification and finite
enumeration syntax; no factual search result from it was used as a premise.
The connected remote `mcp__wolfram__WolframLanguageEvaluator` then evaluated
the following complete stateless job, timeConstraint=15 seconds:

```wl
With[{h=2 t+1}, {
 FullSimplify[Cos[2 Pi h (a+1/2)]+Cos[2 Pi h a],
   Element[t,Integers]&&Element[a,Reals]],
 FullSimplify[Sin[2 Pi h (a+1/2)]+Sin[2 Pi h a],
   Element[t,Integers]&&Element[a,Reals]],
 FullSimplify[1/2 Cos[Pi/100]-1/32 > 3/8],
 Limit[(Sqrt[n Log[2,n]]-Sqrt[2 n])/Sqrt[n],n->Infinity],
 FullSimplify[Abs[Exp[2 Pi I*4/5]-1]/2]
}]
```

Raw returned text:

```
Infinity::indet: -- Message text not found -- (-Infinity + Infinity)
General::messages: Messages were generated which may indicate errors.
Out[1]= {0, 0, True, Infinity, Root[5 - 20*#1^2 + 16*#1^4 & , 3, 0]}
```

The first two entries check the odd-frequency half-turn identity considered
during derivation. The third was a score-margin check for an alternative
odd-frequency list decoder, which was not needed in the final composition.
The fourth reports a limiting divergence, but emitted an indeterminate-form
message; the actual comparison above uses the elementary exact expression
`sqrt(log2 n)-sqrt(2) -> Infinity` and is not inferred from this warning.
The final algebraic root is the positive distance `sin(pi/5)` in Section 3.
These checks do not prove quantum conditioning, independence, success, or
all-branch complexity. Those arguments are supplied in Sections 2--8.

Final read-only live refresh: `2026-11-06T19:09:46.624315Z`, 18 valid published
rows. PSR2 `16bb6065-c3ca-45fb-b514-86106a310646` was now valid/published at
`19:07:20.866Z`; only its public metrics were read, not its proof. New row
`6c59d152-b326-4817-a244-31a15b3cd9d8` at `19:09:25.876Z` had time
`n^4 2^((1553/736)sqrt n)`, slower than CS1's coefficient a. Thus the fastest
full-time conclusion is unchanged. QF48 bytes used in Section 9.1 have SHA256
`287bfb6eb98a8d2043ba9f13012f2f8fdc169314778477863ceba57c2cc8e8ec`.

Handoff: the carry-retaining lemma, exhaustive construction, and the QF48
composition are ready for central mathematical assessment. The all-N input
obligations are explicitly discharged; the two constituent research proofs
must travel together for the fast envelope. No publication action or additional
review/delegation is requested here.
