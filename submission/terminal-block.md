# Terminal-block decoder and four-level clean solver

Execute BASE13's explicit Clifford+T leaf readout, positive-phase convention,
combiner, greedy positive widths and exact capped measurements from base13.md
with the profile and source overrides below. This evidence supersedes its old
odd/even decoder branching, fixed-depth parameters and both hard numeric
cutoffs. The combiner's induction requires only the stated independent
uniform binary-interval labels, distinct leaf ownership and decisions using
low blocks. With four levels it yields the same conditional unused-block
characteristic bound and residual uniformity with q0=(2R+1)^4.
The old adaptive wrapper is never used.

Every original-copy interface performs guarded fixed-width arithmetic even
on malformed branches. Reject any reported label outside its specified
range before interpreting its field. The fixed work and source counters
apply even after a wrong decoder output, so the same allocated fields
suffice on those branches. Implement every known shift by the counted
identity-extended modular permutation described in proof.md.

## Arbitrary moduli via two branches and exact source correction

Let d0=floor(log2 N), a=v2(N), and h=2R. In the main regime
R<d0, set B=d0-h and require capacity >= B. If a<B, use the
odd-part decoder with this actual h and B and the centered-label
and grid overrides below. The only
old condition involving u was the choice of hmax, and may
be replaced with h=2R: B>=a preserves the exact unit-CRT
identity, h determines the same likelihood grid and stride,
and all actual grid and record costs are poly(n)2^R. The
result, when successful, is s0=s mod M, with M=N/2^a.

If a>=B, first use unchanged truncation of uniform cyclic
Fourier labels to [0,2^d0) and cancel B low bits. The resulting
phase is exp(2pi i W s/M0), where M0=N/2^B is an integer in
[2^h,2^(h+1)). Do not use the odd CRT multiplier. Search
all t modulo M0 using independent X/Y records with score
Z cos(2pi Wt/M0-beta). Conditional on the low transcript,
W includes at least one independent uniform h-bit block and
has characteristic modulus at most D_A(y), A=2^h, by the
unchanged combiner analysis. For every wrong t, circular
|y|=||(s-t)/M0||>=1/M0>1/(2A). Some j in [0,h-1]
satisfies 2^j |y| in [1/4,1/2]: use j=0 if |y|>=1/4,
otherwise take the first j reaching 1/4. Its cosine factor
bounds D_A(y)<=1/sqrt(2). The true expected score is 1/2
and each wrong expected score is at most 1/(2sqrt(2)),
providing a constant separation without uniform W modulo M0.
The full unconditional K-record concentration follows from
independent ideal root calls and Hoeffding, with a union bound
over at most 2^(h+1) candidates. Constant-precision cosine
values and a strict-between threshold suffice. The output is
s0=s mod M0. This covers high 2-adic valuation and the
power-of-two modulus itself; no odd CRT inverse is needed.

In either branch write the known congruence as s=c modulo M0
(where M0=M in the first branch), and N=M0 2^D. On each fresh
source copy apply the exact controlled subtraction of c to
the data register, controlled by the row bit. It maps the
source to rho_(s-c). Then use the original cyclic Fourier
readout and reduce its exactly uniform ideal label modulo
2^D. Conditional on the reduced label, the ideal positive
row phase is exp(2pi i k ((s-c)/M0)/2^D); all original labels
with that reduction give the same row. Controlled subtraction is charged as an exact modular permutation. Use clip terminal width e=min(D,h)
and cancel D-e bits, decoding the next e low bits by coherent search of the
score on 2^e candidates. The unused-block property now gives
exact uniform W modulo 2^e, so false expected score is zero.
Appending the recovered bits to c multiplies M0 by 2^e
and reduces D by e. All loops have fixed lengths from N.
The worst D-e is at most d0-h, so the same capacity suffices.
Verify c belongs to [0,M0) after every stage; a wrong earlier
result can still be followed using the exact same capped
instructions, and its probability was already charged by
the first-error analysis.

For all n, the source correction is exact reversible modular
arithmetic, with the existing identity-extension convention.
The ideal root count target stays O(n) for each of the two
branches, since h=Theta(n), the number of direct decoded
blocks is O(1), and each score uses O(h+log n) roots.
The fixed parameters and joint work cap follow below.

## Main-branch direct scoring and finite fallback

For n<1024 use the original finite-shadow BASE13 procedure from
Sections 3 and 8, with its original precision and actual count below
the new padding. For larger n use the parameters in coherent-search.md.
In each direct decoder obtain the fixed Kdir independent roots and
measure their row signs in uniformly chosen X or Y bases. Evaluate
the associated classical score term to error <=1/128, using a fixed
finite rational cosine table with known endpoint comparisons and
fixed denominator. Mean good score is 1/2 for the desired candidate
and at most 3/8 for all wrong candidates. With probability at least
1-2^-20 over all direct blocks and true prior prefixes, all averages
are within 1/32 of their exact expectations. This is Hoeffding with
2 exp(-Kdir/2048) per candidate and a finite union over stages and
at most 2^(h+1) candidates per stage. Consequently the threshold
7/16 separates true (at least 59/128) from false (at most 53/128).
It is implemented by the reversible predicate in coherent-search.md.

Use H0=2^20 n, Qstar=162 q0 H0 and Wstar=12*2^R H0,
with both actual caps set to 1024 times their respective budgets.
Use Qcap in the native Fourier label precision. The unchanged
low-bit combiner success analysis bounds the ideal uncapped
expected source and weighted work sums by Qstar and Wstar.
Uniform binary-interval leaves cost at most two raw inputs each
in expectation, and translated power-of-two residual leaves
cost one. Root outcomes and failures are charged; an abort
before a guarded request returns 0. The two cutoff errors
are each bounded by 1/1024 by Markov. Label readout contributes
at most 2^-14 by the full coupled analysis. The odd argument
from BASE13 controls concentration under true prior prefixes,
and failure of any decoder search contributes below 2^-24.
The clean full-secret success is therefore at least 2/3.
The raw cap is at most P=2^30 n^5 on every branch.

# Centered source labels and a smaller odd decoding grid

In the odd-part branch accept the centered binary interval
[-2^(d0-1),2^(d0-1)) as cyclic labels modulo N, with d0=floor(log2 N).
This means accepting either k<2^(d0-1) or k>=N-2^(d0-1), and storing
k-N in the second case. These intervals are disjoint. Each accepted
ideal label remains uniform on its centered interval and costs less
than two source copies in expectation, just as before. Subtracting N
from the stored integer changes no physical phase. Encode low bits
by the corresponding residues and keep full signed labels for sums.
The combiner uses exactly the same Boolean low residues and
has its original reduced-transcript law.

For a root with B=d0-h, write its selected leaf labels as
k_l=u_l+2^B tau_l with 0<=u_l<2^B and tau_l uniform on
[-A/2,A/2), A=2^h. Condition on the low transcript. The output
W=sum_l sigma_l(u_l/2^B+tau_l) has independent uniform high
blocks, sigma_l in {-1,0,1} with nonempty support of size <=q0.
Thus |E W|<=q0/2 and Var(W)<=q0 A^2/12. For the selected h=2R
and main n>=1024, A^2>=q0, using q0=(2R+1)^4 and R>=102.
It follows that E(W^2)<=q0 A^2/3 uniformly in the conditioning.
The uniform-block characteristic modulus and its far bound
are unchanged by centering.

In stage j use a common denominator
2^(j*stride+ceil(log2(A sqrt(q0)))+12), with sqrt(q0)=(2R+1)^2
computed exactly. The closest grid point to the true circular
parameter has |2^(j*stride) delta| <=1/(2^12 A sqrt(q0)).
The expected cosine at that point is at least
1-2 pi^2 (2^(j*stride) delta)^2 E(W^2)>999/1000
by 1-cos x<=x^2/2. Unlike a deterministic maximum-|W|
estimate this bound allows all frequency records to remain
stored and scored at their true values. There is no rejection
condition or truncation event that could bias the far scores.
For the true-prefix history, an interval contains a closest
grid point because its endpoints are on the grid.

Now the number of scored candidates at each stage is
O(A sqrt(q0)), including stage 0. The accepted score threshold
12/25 retains its near and far margins using the new strict
999/1000 bound and the same concentration and table accuracy.
Use the original K formula based on nq=2^(h-1)q0, but
add 16 inside its parentheses. This covers the new grid union
slack and still satisfies K<=2^15 n on the main range. The quantum search
uses O(q0^(1/4) 2^R) rather than O(q0^(1/2) 2^R) core iterations,
so the work envelope is
2^(n/10) n^(53/10) L^2 with unchanged storage, source and tolerance.
The negative integer labels use two’s-complement fields of
O(n) bits. Before multiplying or shifting, reduce coefficients
into the known positive modulus with ordinary signed arithmetic.
