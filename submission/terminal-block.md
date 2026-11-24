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

Let d0=floor(log2 N), a=v2(N), and h=R. In the main regime
R<d0, set B=d0-h and require capacity >= B. If a<B, use the
original odd-part decoder with this actual h and B. The only
old condition involving u was the choice of hmax, and may
be replaced with h=R: B>=a preserves the exact unit-CRT
identity, h determines the same likelihood grid and stride,
and all actual grid and record costs are poly(n)2^R. The
result, when successful, is s0=s mod M, with M=N/2^a.

If a>=B, first use unchanged truncation of uniform cyclic
Fourier labels to [0,2^d0) and cancel B low bits. The resulting
phase is exp(2pi i W s/M0), where M0=N/2^B is an integer in
[2^h,2^(h+1)). Do not use the odd CRT multiplier. Enumerate
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
and cancel D-e bits, decoding the next e low bits by direct
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

## Uniform profile, score, and deterministic cutoffs

Use n>=1024 for the main branch, with original finite shadow
decoder below 1024. For trial R keep at most four positive values
of the same delta recurrence. Select least R with
2 sum_i v_i+R>=n, by sequential search. For D0=ceil(log2 n)+3
the test R'=ceil((n+12D0)/9) is at most n and
R'-3D0>=n/9-(5/3)D0>0 on the main range. The four-value
capacity plus R' is at least 9R'-12D0>=n. Therefore
R>=n/9 and R<=R', and the selected four values all satisfy
v_i>=R-3D0>=R/4, using n/36>=D0 for n>=1024. As before
q0=(2R+1)^4<=n^4. Now 2^R=O(n^(4/3) 2^(n/9)).
The selected h=R is strictly less than floor(log2 N) on this
range by the test upper bound. The cancellation requirement
never exceeds floor(log2 N)-R. Power-of-two residual blocks
of size at most R are decoded after at most nine such blocks.

For each direct scoring block choose Kdir=8192(R+ceil(log2 n)+32).
The high-valuation first block has at most 2^(R+1) candidates and
all smaller residual blocks at most 2^R. True score expectation
is 1/2. The false expectation is at most 1/(2sqrt(2))<3/8
in both cases. Evaluate each term to absolute error <=1/128
and bound the exact empirical deviation by 1/32. The resulting
true score is >=59/128 and false is <=53/128, so choose
threshold 7/16 and return the least candidate passing it,
or zero. Hoeffding gives per-candidate failure <=
2 exp(-Kdir/2048); the union over all candidates and <=10
direct stages is below 2^-20. A direct arithmetic table with
fixed rational entries can achieve the required term accuracy
on every transcript. Projection to a residual modulus, the
sift test, and the candidate-dependent phase computing
arguments all run with explicitly bounded integer indices.

For the odd branch h=R, stride=R-4>=R/2 and Sodd<=2n/R+1<=19.
Its K is unchanged except for using the actual nq=2^(R-1)q0.
It satisfies K<=8192(R+5ceil(log2 n)+32)<=2^15 n on this
range; the same coarse upper bound covers Kdir. The total
root count is at most H0=2^20 n, covering at most 19 odd
stages and 10 direct stages, where the cases are disjoint
except for the residual power-of-two direct stages.

Use Qstar=162 q0 H0, Wstar=12*2^R H0; permit at most
1024 times each, guarding before each actual source request
or weighted attempt. The raw sift costs at most two copies
in expectation per ideal accepted leaf, and power-of-two
reduced leaves need only one, even on wrong-prefix paths
for the analysis of the cost. Root retries still obey the
same induction, so Markov bounds each cutoff failure by
1/1024, and the extraction failure with the actual Qcap
is <=2^-14. Combined decoder errors stay below 2^-19
by a first-wrong-block union bound. This gives clean
success >=2/3 and a padding cap P=2^39 n^5 because
1024*162*2^20<2^38, and the finite-shadow prefix is
within this same budget. The wrapper executes J=64 ceil(n^(1/10)) with epsilon=L/(16 P) and the shared verification reserve in proof.md.

The inherited odd-stage score loop supplies a conservative unaddressed
work bound O(n^4 q0 2^h) and stores only the running best, current grid
point and K records. With h=R it is no longer exponentially lower than
the combiner. Charge O(n^8 L 2^R) for this loop across O(1) stages.
Direct comparisons need only poly(n) work per candidate, and the
explicit schoolbook per-record residue calculation, O(n) records
and O(1) stages give O(n^3 L 2^R). Source preprocessing and abort
work remains polynomial. It follows that the joint
time representative after the tenth-root bank multiplier is
2^(n/9) n^(283/30) L. Classical and quantum space and the n^(51/10)
sample envelope are the stated polynomial bounds from the bank workspaces and cap.
This deliberately charges the odd decoding term even on moduli
where it is skipped.
