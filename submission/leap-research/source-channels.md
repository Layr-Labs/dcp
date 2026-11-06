# Source channels: exact identities and an exponential window obstruction

Research-only lane, 2026-11-07. No publication, submission, source reservation,
monitor operation, checkout, or prepared-candidate review is authorized here.
Only this file is owned. All statements below start with the inaccessible mixed
source in `rules.md`; they do not assume a purification or subgroup source.

**Main result.** The lower-dyadic-window channel, with failures discarded, can
require at least `(2^n-1)/3` acquired source copies for full-secret recovery.
Constant window acceptance does not imply constant useful-source yield.
Separately, a known secret residue allows deterministic quotient extraction;
tracing an unknown CRT factor generally destroys all coherence.

## 1. Conventions and the source operator

Write `T_s^(N)|x> = |x+s mod N>`, and order blocks by the source bit. Then

```
rho_s^(N) = (1/(2N)) [ I_N       T_-s^(N) ] .                 (1)
                     [ T_s^(N)  I_N       ]
```

This follows by expanding each mixed coset, so every subsequent channel applies
directly to the available density operator. Define

```
F_b|v> = b^(-1/2) sum_k exp(2 pi i k v/b)|k>.
R(theta) = |0><0| + exp(i theta)|1><1|.
rho_t^(a;theta) = (R(theta) tensor I) rho_t^(a)
                  (R(theta)^dagger tensor I).
```

Its lower-left block is `exp(i theta) T_t/(2a)`. Fourier transforms and phase
rotations in the identities below are mathematical channels. They are not
silently assumed to have exact Clifford+T implementations; see Section 7.

## 2. CRT projection: trace, measurement, and a repair impossibility

Hypotheses: supplied integers `a,b >= 2`, `gcd(a,b)=1`, `N=ab`.
The reversible CRT permutation maps `x` to `(u=x mod a,v=x mod b)`.
Put `t=s mod a`, `w=s mod b`. It maps the lower-left translation to
`T_t^(a) tensor T_w^(b)`.

**Tracing the b register.** Since `Tr(T_w^(b))=b` for `w=0` and zero otherwise,

```
Tr_b(CRT rho_s CRT^dagger) = rho_t^(a),      if w=0;
                          = I_(2a)/(2a),   if w!=0.           (2)
```

This is a deterministic channel with no postselection, but it is usually not a
factor source. The smallest nontrivial coprime factorization is `N=6=2*3`.
For `a=2,b=3`, both `s=1` and `s=2` become `I_4/4`, although their target
residues modulo 2 differ. Thus no further processing of this output alone can
recover the lost factor secret. Factoring N does not fix this channel.

**Fourier measuring the b register.** Each `k in Z_b` occurs with probability
exactly `1/b`, independently of s. Conditional on k, the retained state is

```
sigma_(t,w;k) = rho_t^(a; 2 pi k w/b).                        (3)
```

If `w` is known, applying `R(-2 pi k w/b)` corrects the phase. If only a promise
`w in W` is known, a single correction works precisely when `k w mod b` is
constant on W. For a subgroup promise `W=H`, the correctable labels are its
annihilator; their fraction is `1/|H|`. With no promise, `k=0` is the only
universally correctable label, accepted with probability `1/b`.

There is an exact arithmetic implementation when w is known that avoids
Fourier synthesis entirely: before discarding b, apply `T_-w^(b)` on that
register conditioned on source bit 1. This removes the b translation block
and leaves `rho_t^(a) tensor I_b/b`. Trace b with success 1. If correction
is performed after Fourier measurement instead, it is exactly a power of T
whenever `kw/b` is a multiple of `1/8`; arbitrary known angles still require
the implementation qualification in Section 7.

There is a stronger statement than failure of phase rotation. Fix any
`k!=0 mod b`. There is **no secret-independent, heralded CP success map** on
the retained state alone which outputs exactly `rho_t^(a)` and has strictly
positive success probability for every `t,w`. Indeed,

```
(1/b) sum_w sigma_(t,w;k) = I_(2a)/(2a)                       (4)
```

for every t, by the geometric sum of a nontrivial character. If the success map
E obeyed `E(sigma_(t,w;k))=p_(t,w) rho_t`, then
`E(I/(2a))=((sum_w p_(t,w))/b) rho_t` for every t. The coefficient is positive
under the stated hypothesis. Distinct `rho_t` have trace one and different
translation blocks, so they are not proportional. This is a contradiction.
Even a uniformly successful probabilistic purifier is impossible in this
single-output setting. Additional source copies, side information about w, or
joint processing across copies are outside this impossibility theorem.

An exact small phase example uses `a=3,b=2,k=1`: secrets `s=1` and `s=4` have
the same target residue 1 and opposite relative phases. The discarded-factor
Fourier measurement is just H, so the issue is not Fourier approximation.

## 3. Noncoprime factor coordinates and the retained carry phase

For arbitrary supplied `N=ab`, use the bijection `x=u+a v` with
`0<=u<a`, `0<=v<b`. Write the integer representative `s=t+a w`, `0<=t<a`,
and `c_t(u)=floor((u+t)/a)`. Translation acts as

```
(u,v) -> (u+t mod a, v+w+c_t(u) mod b).
```

Fourier measuring v again gives uniform `k in Z_b`; its retained lower-left
unitary is

```
V_(t,w;k)|u> = exp(2 pi i k (w+c_t(u))/b)|u+t mod a>.         (5)
```

This is not an untwisted factor shift. There is a useful exact gauge identity:
with `D_k|u>=exp(2 pi i k u/(ab))|u>`,

```
D_k V_(t,w;k) D_k^dagger = exp(2 pi i k s/N) T_t^(a).         (6)
```

Proof: set `u'=u+t-a c_t(u)`. The combined exponent is
`k[(w+c)/b+(u'-u)/(ab)] = k s/N`. Thus the carry can be removed using a
known k-dependent gauge, but the remaining relative source-bit phase depends
on the *full secret*, not just t. Equation (6) is not a free source reduction.
For arbitrary phases D_k itself is an ideal identity requiring approximation
when implemented. For `k=0`, no gauge or phase correction is needed and the
conditional state is exactly `rho_t^(a)` with probability `1/b`.

Tracing v without Fourier measurement retains only entries with
`w+c_t(u)=0 mod b`. Equivalently its lower-left block is

```
(1/(2a)) sum_(u: w+c_t(u)=0 mod b) |u+t mod a><u|.            (7)
```

Consequently a generic noncoprime factor trace can leave a partial shift rather
than either a perfect factor source or total dephasing. Example `N=4,a=b=2,
s=1`: this block is `|1><0|/4`, not `T_1^(2)/4`.

## 4. A constructive quotient channel when a residue is already known

Hypotheses: supplied divisor `a|N`, `b=N/a`, and a **correct** known
`t in {0,...,a-1}` satisfying `s=t mod a`. No coprimality is required.

1. Apply `T_-t^(N)` to the address only when the source bit is 1.
2. Reversibly compute `x=u+a v` and measure/discard u.
3. Keep the source bit and v.

Step 1 produces `rho_(s-t)^(N)=rho_(a w)^(N)` exactly, where
`w=(s-t)/a in Z_b`. Translation by `a w` preserves u and shifts v by w.
The intermediate state factorizes as

```
(I_a/a) tensor rho_w^(b),                                   (8)
```

with the source bit grouped with v. Every remainder outcome has probability
`1/a`; every branch gives the same exact quotient source. Overall success is 1,
not `1/a`. A stream of independent inputs yields independent quotient sources.

If t is a guess, the exact same channel instead gives

```
E_t(rho_s^(N)) = rho_((s-t)/a)^(b),  if s=t mod a;
              = I_(2b)/(2b),         otherwise.             (9)
```

The remainder measurement removes all off-diagonal terms unless the remainder
is preserved. Its distribution is uniform in both cases, so it does **not**
herald whether the guess was right. A known divisor is not a known residue.
The smallest nontrivial example is `N=4,a=b=2,t=0,s=1`, giving `I_4/4`.

This is a genuine deterministic reduction after partial secret recovery, but
does not supply that partial recovery or improve the all-N time bound itself.

## 5. Lower windows: exact filter and exponential sample lower bound

For any set `I subset Z_N` of size L, let `P_I` project the address into I,
identically on both source-bit branches. The success probability is exactly
`p=L/N`. Conditioned on success, the diagonal blocks are `I_I/(2L)` and the
lower-left block is

```
A_s/(2L),  A_s = sum_(x in I: x+s mod N in I) |x+s mod N><x|. (10)
```

Write `K_s=|I intersect (I-s)|`. The successful state can be expanded as
`(1/(2L)) sum_x |eta_x><eta_x|`, where
`eta_x=1_I(x)|0,x>+1_I(x+s)|1,x+s>`. There are `K_s` coherent two-entry
vectors and `2(L-K_s)` singleton vectors. Their supports are disjoint.
Hence it is a mixture of the normalized coherent pairs with total weight
`K_s/L` and incoherent singletons with total weight `1-K_s/L`. Acceptance
does not mean both endpoints passed. The successful state has rank
`2L-K_s`; an L-point DCP state has rank L. Equality of rank requires
`I+s=I`, although identifying the resulting permutation with a particular
cyclic L-point shift can require more conditions.

Let `omega=I_(2L)/(2L)`. The K_s nonzero singular values of A_s equal one, so

```
D(sigma_s,omega) := (1/2)||sigma_s-omega||_1 = K_s/(2L).      (11)
```

For `I={0,...,L-1}`, `L<=N`, and integer `0<=s<N`,

```
K_s = max(0,L-s) + max(0,L-(N-s)).                          (12)
```

If one ideally Fourier measures the retained L-point address, its label k is
uniform and its source-bit lower-left entry is `c_s(k)/2`, where

```
c_s(k) = [ max(0,L-s) exp(2 pi i k s/L)
         + max(0,L-(N-s)) exp(2 pi i k(s-N)/L) ]/L.           (13)
```

In particular, a random choice of label does not restore unit visibility.

**The dyadic-window lower bound.** Let `L=2^m`, `m>=1`, `N=2L-1` and
`I={0,...,L-1}`. Then `n=m+1`, and consider secrets `s_0=L-1`, `s_1=L`.
Their retained lower-left operators are respectively
`A_0=|L-1><0|` and `A_1=|0><L-1|`. Their difference has two singular values
equal to one, giving exactly

```
p = L/N > 1/2;
D(sigma_(s_0),sigma_(s_1)) = 1/L.                           (14)
```

Define the full acquisition channel C to output the successful state and a
success flag, or a fixed erasure state and a failure flag; all quantum systems
from failed filters are discarded. The failure probability is secret
independent. Orthogonality of the two flag sectors therefore gives

```
D(C(rho_(s_0)), C(rho_(s_1))) = p/L = 1/N.                  (15)
```

For q independent acquired copies the product-state telescoping inequality
and trace-norm contractivity give distinguishability at most `q/N`, even
after arbitrary joint processing. An adaptive procedure with an all-branch
cap q is also covered: pre-supply q independent channel outputs, simulate its
adaptive consumption, and discard unused ones. Recovering the complete secret
with probability >=2/3 for each of these two secrets would distinguish their
equiprobable hypotheses with probability >=2/3. For two states, any binary
decision has average success at most `(1+D)/2`: this follows by maximizing
`Tr(E(rho_0-rho_1))` over `0<=E<=I`. Consequently

```
q >= N/3 = (2^n-1)/3.                                      (16)
```

This charges **acquired** source copies, including failed filters; the source
work alone is at least `(n+1)(2^n-1)/3`. The obstruction holds even if all
post-channel computation is free. It is a lower bound on this precisely
specified preprocessing pipeline, not on general DCP algorithms. Keeping the
failed quantum state, using unfiltered copies, changing the filter, or using
secret-dependent windows is outside the theorem. It rules out treating a
constant-acceptance lower dyadic projection as a perfect smaller DCP source.

Known translations of a fixed window do not help: `rho_s` commutes with every
unconditional address translation, so translating the window and translating
the output coordinates back gives the same state for every translation.
Retaining that random translation supplies only an independent classical label.

## 6. Upper dyadic padding and random shifts

Embed the N-point address as `{0,...,N-1}` in `Z_M`, `M>=N`, and keep the source
bit. For `0<=s<N`, there are `N-s` nonwrapping pairs of integer difference s
and s wrapping pairs of integer difference `s-N`.

Twirl by a uniform unconditional translation `T_r^(M)` and forget r. The exact
result is

```
Twirl_M(Embed rho_s^(N))
  = (1-s/N) rho_s^(M) + (s/N) rho_(s-N mod M)^(M).            (17)
```

Proof: twirling each `|y><x|` gives `T_(y-x)^(M)/M`; diagonal blocks become
`I_M/(2M)`. The two differences above give (17). This is a mixture of *two
different shifts per copy*, not a fixed-secret DCP_M source. If r is retained,
the state is a known translate of the original embedded state; undoing it
recovers the original, not an improved source. Randomizing x modulo N before
embedding leaves the mixed source invariant.

Fourier measuring the M-point address, with or without the forgotten twirl,
gives uniform k and the qubit

```
tau_(s,k) = (1/2)[ 1           conjugate(c_s(k)) ],
                  [ c_s(k)    1                 ]
c_s(k) = exp(2 pi i k s/M)
         [1-s/N + (s/N) exp(-2 pi i k N/M)].                 (18)
|c_s(k)|^2 = 1 - 4s(N-s)/N^2 * sin^2(pi k N/M).
det(tau_(s,k)) = s(N-s)/N^2 * sin^2(pi k N/M).               (19)
```

For any `0<s<N`, the qubit is pure iff `M` divides `kN`. Exactly
`d=gcd(M,N)` labels satisfy this, so universal pure-label postselection has
probability `d/M`. Those labels are `k=jM/d` and their phases are
`exp(2 pi i j s/d)`; they reveal only `s mod d`. For odd N and dyadic M,
only k=0 is pure and it contains no secret information. Rank cannot be fixed
by any phase rotation, whether the phase is known or unknown.

The smallest nontrivial non-dyadic padding example is `N=3,M=4,s=1,k=2`:
`c=-1/3`, with qubit eigenvalues `2/3,1/3` rather than `1,0`.
An exact complete-erasure example with nearest upper dyadic M is
`N=6,M=8,s=3,k=2`, where the two phases are `-i,+i` and `tau=I_2/2`.
The former example uses an exactly implementable four-point Fourier transform.
These are state identities, not empirical diagnostics.

Equation (17) is also not a proof that *all* padded noisy samples are useless:
their bias may encode s. A solver exploiting that bias must be analyzed as a
noisy, secret-dependent ensemble, not fed silently into a perfect-phase sieve.

## 7. Charged implementation and exact scope of the resource claims

The quotient channel (8), CRT permutation, interval membership filter and
padding isometry require only reversible integer arithmetic, comparisons and
computational-basis measurements. Supplied factors are inputs; no uncharged
factorization is assumed. Check divisibility/coprimality using counted binary
arithmetic. The quotient channel includes verification of the supplied divisor,
but cannot verify the secret-residue promise without extra work.

A conservative uniform implementation envelope per source copy is

```
T = O(n^4), S_C = O(n^3), S_Q = O(n^3), Q = 1,               (20)
```

for `a,b<=N`, and for padding/window registers of at most `n+1` bits.
All four envelope growth indices are exactly `0/1`. These are channel bounds,
not a full-secret solver or a submission. They deliberately allow workspace
larger than the stated PSR2 quantum bound and claim no dominance over it.

Here is an explicit sufficient circuit-accounting argument. Schoolbook
division, multiplication, modular subtraction, comparisons and extended Euclid
have binary Boolean circuits/generators of size bounded by O(n^3) at these
lengths; division alone can be made by O(n) stages of O(n)-bit subtraction and
selection. Use a reversible gate for each Boolean operation, saving intermediate
bits, copy the result, and reverse the computation. This uses O(n^3) bits/qubits
and gates. A bijective coordinate change is implemented by computing its
forward map into clean space and clearing the input with its inverse; both maps
are explicit bounded-length arithmetic. Each elementary reversible gate has a
fixed exact Clifford+T decomposition. Generating wire indices and executing
addressed operations costs O(log n) per gate when total allocation is O(n^3).
Keeping the circuit description costs O(n^3 log n) bits if stored, so instead
generate the regular arithmetic circuit gate by gate using O(n^3) controller
space. Reverse schedules have explicit loop indices and do not need a saved
gate list. Thus O(n^3 log n) total work is safely bounded by O(n^4), including
initialization, generation, addresses, measurements and the n+1 source charge.
All loops and memory allocations are fixed by n; no stochastic branch exceeds
these bounds. Failed windows consume the source copy and the same envelope.

For repeated rejection with acceptance p, R fixed attempts use exactly R source
copies and O(R n^4) work, with failure probability `(1-p)^R`. A demand for K
accepted outputs must specify an acquisition cutoff and a separate binomial
tail bound; expected `K/p` acquisitions is not an all-branch bound. No rejection
loop is asserted here without a cutoff.

General F_b, D_k and R(theta) in Sections 2, 3 and 6 are stated as exact
mathematical identities, **not included in (20)**. In a physical realization
outside exactly synthesizable cases, construct a Clifford+T approximation and
charge its entire generator, gates, precision and scratch. If a unitary U is
replaced by V with operator norm error <=eta, then for any density matrix
`||U rho U^dagger - V rho V^dagger||_1 <=2 eta`; measurement and discarding
cannot increase this error for the unnormalized instrument output. Across R
calls the trace-distance error is at most `R eta` by a hybrid argument. For a
conditional branch of probability p, renormalization can amplify the trace-
distance error to at most `2 eta/p` when the approximate branch has nonzero
probability. Therefore rare-outcome exact formulas cannot justify an uncharged
fixed-precision implementation. No resource claim depending on a generic
Fourier synthesis theorem is made in this note. The quotient construction and
window lower bound do not need any Fourier transform at all.

The small examples are independently realizable: F_2=H, and F_4 uses H,
controlled-S and a swap. Controlled-S is exact from T gates and CNOT using
`2xy=x+y-(x xor y)` in the phase exponent. Thus the `N=3,M=4` mixed-qubit
counterexample does not rely on an unavailable exact gate.

## 8. Handoff status and provenance

Proved: (1)--(19), the explicit obstruction (16), and the scoped arithmetic
channel envelope (20). No heuristic assumption, numerical experiment or source
purification enters their proofs. No finite diagnostic is used as a substitute
for proof. Novelty against the literature has not been established; these are
self-contained derivations, not a claim that the channel facts are new.

No all-N faster solver is obtained. The new useful obstruction is exponential
source loss in one constant-acceptance dyadic-window pipeline. A correct known
residue enables deterministic quotient extraction, but obtaining that residue
remains an explicit obligation. The global-time benchmark and PSR2 target from
the assignment are context only, not invoked as theorems or re-reviewed.

For any later handoff, central sender must integrate a complete solver with
exact rational supported resource envelopes and a joint all-N, all-s success
proof. Equation (20) alone is not such a handoff and does not authorize a send.
The only exact rational indices asserted here are the four `0/1` channel
envelope indices; (16) is a lower bound, not a submitted upper envelope.

Read-first source provenance (SHA-256, before writing this file):

```
rules.md
7be4f5f1137aea419a481bf31482bebc5a8f8cbb15dd2296872fce6dbad7a469
submission/leap-research/COORDINATION.md
4be27627b2ba52fcbfe80c8f3dc07d08e6c9a9c77ca6e337c237735e8e61dd93
```

Consistency diagnostic: 82 finite matrix checks passed for (6), (14) and (17),
using `(a,b)=(2,2),(2,3),(3,2),(3,3)`, windows `L=2,4,8`, and padded pairs
`(N,M)=(3,4),(5,8),(6,8)`, over all relevant s and k. They are not proof
premises; no diagnostic files or changes outside this owned note were needed.

No external result is needed for the proofs: only expansion of the mixed state,
finite character sums, explicitly described reversible Boolean arithmetic,
singular values of partial permutations, and the binary-decision trace-norm
inequality proved above. This file is the lane's research report; the shared
coordination contract and other lanes' files remain untouched.
