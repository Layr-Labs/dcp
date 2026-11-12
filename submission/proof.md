# QLOG-P8: a fourth-scale profile and a smaller denominator correction

## 0. One selected program and theorem

For every integer N>=2 and secret s in Z/NZ let n=ceil(log2 N). For n>=2
put L=log2 n and define ANALYSIS scales

 F=sqrt(nL), G=sqrt(n)L^(-3/8), J=sqrt(n)L^(-7/16),
 P=sqrt(n)L^(-15/32), H=sqrt(n)L^(-1/2)log2 L.

The ONE integer program below outputs all of s with unconditional
probability at least 1-2^-8. Jointly on EVERY execution branch,

 T=O(2^((3/4)F+(3/4)G-(3/32)J+P/16)),
 S_C=O(n^2), S_Q=O(n),
 Q=O(2^((1/2)F-(3/2)G+(3/16)J-(3/32)P)).             (0.1)

All outside constants are absolute independent of N,s,outcomes. The
explicit finite branch below handles n=1. The four representative growth
indices are 1/2,0,0,1/2. Fractional malformed tolerance is zero under the
canonical clean model in Section 6. No positive robustness or impossibility
is asserted. H is an internal iterated-log accounting scale; it is NOT
encoded as a supported logPower. The four declared bounds contain only
supported exact rational powers of n and log2 n.

Direct material source: own published PSG4-QLOG submission
8870de8c-e8dd-4d03-82c7-57842e846e4f, evaluated commit
4f7e2b4f8dbcf19aa8dce588a8771a21297f42be. Its complete proof is included
UNMODIFIED as profile-source.md, SHA-256
6db1988013b27ef3ce4f266954ebac9c624bbf1989da272c4021ba78027bde09.
Its complete family-source.md is likewise unmodified, SHA-256
11f96191f1ab9c78f070472c4cb5e0552ec25381398ffc13b51d7f9c1b7c3fc7.
The exact published source bytes match official metric evidence. All direct
and historical credits in those files remain; prior validity or attribution
verdicts are not mathematical premises. All necessary circuits, probability
arguments and arbitrary-modulus full-secret recovery are supplied there.

The source's OLD selected numerical configuration is NOT executed. Its
source/extraction/C4096 verified-pair/unused-label/full-decoder primitives,
finite branch and literal-cap construction are executed with Section 1
below replacing its profile rule at EVERY use. The source's old selected
resource conclusions are replaced by Sections 3-5 here. No bank interpreter
is executed; the physical memory columns in (0.1) are the ordinary classical
and quantum storage of this program. This is a fourth-scale tradeoff within
the established square-root family, not a cube-root algorithm or optimality
claim. The stronger work representative is not claimed to be tight.

## 1. Complete actual integer profile and caps

For n<256 execute the included family-source.md Section 8 exhaustive test:
for candidates t=0,...,N-1 subtract t modulo N controlled by the source
first qubit, measure X, reject at a minus, accept after n+10 plus tests,
or output 0 if none. Its full Clifford+T circuit and proof are supplied.

For n>=256 compute public integers ell=ceil(log2 n), z=ceil(log2 ell),
and the following maximal nonnegative INTEGER roots:

 g^8 ell^3<=n^4, j^16 ell^7<=n^8,
 p_root^32 ell^15<=n^16, h^2 ell<=n z^2.

Each is found by finite binary search on [0,n] with fixed powers and exact
integer comparisons. All log ceilings of integer arguments are bit-length
operations with an exact power-of-two check. Fixed-power words have O(log n)
bits. There is no real arithmetic oracle. At EVERY positive trial R put

 u=min(R,max(1,floor(R/3)+2g-floor(j/4)+floor(p_root/8)+floor(h/2))). (1.1)

Since g>=j, the correction after floor(R/3) is nonnegative. Thus u>=R/8
for every positive R, and clipping defines 1<=u<=R on every trial.

Let delta(v) be the least d>=0 with 20*2^d>=21*(2v+6). Starting at R,
descend by v<-v-delta(v) retaining v>=u. Reverse the retained sequence
as v_1,...,v_m=R and write S=sum v_i. Choose the FIRST R with 2S>=n.
Sequential search is finite by R=ceil(n/2), since R itself is retained.
No monotonicity premise is used. Literal enumeration of all trials and
heights takes polynomial work in n; it is included in the resource ledger.

Run the complete source algorithm with THIS profile. For every requested
PS_TREE(D,B), greedily assign widths b_i<=2v_i from the root downward,
summing to B; use b_i+6 fresh child outputs at positive widths and return
the child directly at zero widths. Retain the exact bounded C4096 Grover
instrument and verified-pair compression, exact source transforms and
nondestructive label extraction, full signed label records, free-frequency
odd decoder and shifted 2-adic recovery. None is an unaccounted oracle.

Recompute q0=(2u+6)2^(R-u), hmax=1+floor(u/8), every odd decoder
frequency/stride/grid quantity, K=2^13(ceil(log2 nq)+ceil(log2 n)+30),
and the odd stage count Sodd, setting K=Sodd=0 when the odd part M=1.
The complete definitions of nq, exact CRT multiplier, stage bounds and
output rule are family-source.md Sections 6-8. Recompute literal budgets

 H0=Sodd K+2n,
 Qstar=6(2u+6)2^(R-u)H0+2n, Qcap=1024 Qstar,
 Wstar=3m 2^R H0, Wcap=1024 Wstar.

Before EVERY original source acquisition check Qcap; before EVERY complete
combiner attempt check and add its weight 2^v_i to the Wcap counter. Abort
before exceeding either cap, release registers and output 0. Children of
an aborted parent remain counted. EXTRACT uses the newly recomputed Qcap,
h_e=ceil(log2(2^16 Qcap(n+5))) and 2^21 h_e collective rounds per basis,
exactly as in the complete source. All attempts, measurements, rejected
Fourier labels, wrong-label branches, address and initialization charges
are included. No inverse or coherent control of the original source,
purification, QRAM, hidden-shift oracle or subset-sum oracle is used.

## 2. Full-secret law and unconditional success

The exact configuration-independent arguments are included in full in
family-source.md Sections 1-8 and summarized in profile-source.md Section 2.
They apply for EVERY clipped u and feasible profile in (1.1): they depend
on fresh independent leaves, low-only selection and the exact delta bound,
not the old numerical base choice. The source is an exact mixture of a
uniform latent Fourier label with a product phase qubit/eigenstate.
EXTRACT changes no conditional eigenstate and has at most
1/(2^14 Qcap) label error per acquisition, with no conditioning of the
unused-label argument on all estimates succeeding.

At positive width b, the size-biased fiber from k=b+6 fresh independent
uniform low labels has mean <65. Bounded verified-list discovery and
pairing succeed with probability >=3963/4096>20/21 before each fresh
attempt. Every returned pair is exactly correct even if discovery is
incomplete. The selection kernel uses only cancelled low bits. The
nonzero +/-1 incidence on disjoint original leaves therefore leaves the
remaining block uniform, with fair root parity and the full characteristic
bound needed by the odd-part decoder. Full-secret recovery for arbitrary
N follows from that decoder and exact shifted 2-adic parity recovery,
not from a parity-only or power-of-two promise.

The source's reach-event/geometric recurrence and delta telescoping give
expected original acquisitions <=Qstar and expected total attempt weight
<=Wstar in the ideal uncapped process, including failed ancestors and work
after a wrong decoder outcome. This uses no independence between attempt
cost and success. The two literal caps each lose at most 2^-10 success by
Markov and coupling until the cap. At most Qcap extraction calls cost
<=2^-14, and the decoder error is <=2^-20. Thus failure is at most
2^-10+2^-10+2^-14+2^-20<2^-8. The finite branch has failure <2^-10.
The resources are branchwise caps, not expected-resource statements.

## 3. Exact root estimates and four-scale capacity

Write x=sqrt(n), k=log2 L. As n tends to infinity, ell lies in [L,L+1]
and z lies in [k,k+2]. Taking the floors of the exact positive roots gives

 g=G+O(G/L+1), j=J+O(J/L+1),
 p_root=P+O(P/L+1), h=H+O(x/sqrt(L)+1).              (3.1)

These estimates follow from convexity
1-a/L<=(1+1/L)^(-a)<=1 for each fixed a>0 and a floor error <=1.
All roots and H are o(sqrt(n)). Bounds here are eventual inequalities with
absolute constants. Every smaller n still executes the same finite capped
program and the same correctness theorem, enlarging only outside resource
constants; it does not require an uncharged infinite threshold test.

For every trial's clipped integer u the complete integral estimate is

 2S_u(R)>=(R^2-u^2)/D_R, D_R<=log2 R+4.              (3.2)

Indeed the intervals [max(u,v-delta(v)),v] for retained v cover [u,R];
the integral of 2t on each is <=2v delta(v)<=2vD_R. The exact delta
inequality bounds delta(v) by log2R+4 for 1<=v<=R. This gives (3.2)
without monotone feasibility or a random-profile approximation.

Consider the ANALYSIS trial ceil(R0) with

 R0=3F/4+3G/4-3J/32+3P/64+5H/8,
 u0=R0/3+2G-J/4+P/8+H/2
   =F/4+9G/4-9J/32+9P/64+17H/24.

Eventually R0 is positive, at most F, and u0/R0 tends to 1/3, so both
clipping endpoints are inactive at this trial. Root, floor and ceiling
errors give actual u=u0+E where

 E=O(x/sqrt(L)+G/L+J/L+P/L+1).

Thus E=o(F); the change to the capacity numerator from rounding is
O(n)+o(n)=o(nk), since F times x/sqrt(L) is n and all other products
are smaller. Exact expansion is

 R0^2-u0^2=F^2/2+(7/12)FH
  -(9/2)G^2+(9/8)GJ-(9/16)GP-(9/4)GH
  -(9/128)J^2+(9/128)JP+(9/32)JH
  -(9/512)P^2-(9/64)PH-H^2/9.                     (3.3)

All THREE cross terms FG,FJ,FP cancel EXACTLY. FH=nk. Every remaining
quadratic term is o(nk). For example G^2/(nk)=L^(-3/4)/k,
P^2/(nk)=L^(-15/16)/k and H^2/(nk)=k/L tend to zero; mixed terms
are bounded by the corresponding sums of squares. Consequently at this
rounded trial,

 (Rtest^2-u^2)/n=L/2+(7/12)k+o(k),
 log2Rtest+4=L/2+k/2+O(1).

Their surplus is k/12+o(k)-O(1), eventually strictly positive. Equation
(3.2) proves the trial feasible, so the ACTUAL first-feasible search obeys

 R<=ceil(3F/4+3G/4-3J/32+3P/64+5H/8).              (3.4)

No input-dependent substitution into a fixed-parameter theorem is used.
Since n<=2S<=2R^2, also R>=sqrt(n/2). Hence R=O(F), and (3.1) implies
clipping is eventually inactive at the selected R, with u=R/3+o(R).
These are exactly the hypotheses needed by the general source ledgers.

## 4. All original copies with the full signed P term

The actual acquisition cap is bounded by a fixed polynomial times
2^(R-u), so log2Qcap<=R-u+O(L). This counts every original source request,
including discarded labels and failed attempts. At the selected base,

 R-u<=(2/3)R-2g+j/4-p_root/8-h/2+3.

Using (3.1) and (3.4), the exact coefficients give

 R-u<=F/2-3G/2+3J/16-3P/32-H/12
          +O(G/L+J/L+P/L+H/k+H/L+1).               (4.1)

In particular (2/3)(3/64)-1/8=-3/32 and
(2/3)(5/8)-1/2=-1/12. All error terms and the cap's O(L) logarithm
are o(H): their ratios are negative powers of L divided by k, 1/k,
1/L, or L/H, respectively. Therefore eventually

 log2Qcap<=F/2-3G/2+3J/16-3P/32-H/24.

Dropping ONLY this strictly negative internal remainder proves exactly
the selected Q representative in (0.1). Its full negative P coefficient
is established, not inferred from a sample-growth score. No positive
error, polynomial fee or unsupported iterated-log term is discarded.

## 5. Every charged operation, spaces, indices and comparison

The complete source's exact per-attempt circuit/generator bound remains
O(R^2 L 2^v_i) core work because u>=R/8 and n<=2R^2. Its two actual
caps, m=O(R/L) and full decoder root count H0=O(n) give combiner core
work O(nR^3 2^R). Exact label extraction costs O(n^2 L) per acquisition;
its total is smaller by the exponential gap u=Theta(R). The complete
frequency grid costs poly(n)2^(R-7u/8), likewise smaller. All integer
roots, sequential profile search, fixed rational tables and CRT are
polynomial preprocessing. Add the full O(L) address fee under O(n^2)
allocated storage, initialization, measurements, resets and cleanup:

 T=O(n^(5/2)L^(5/2)2^R).

Combining with (3.4), log2 of this envelope is at most

 3F/4+3G/4-3J/32+3P/64+5H/8+O(L+log2 L).

Since H/P=(log2L)L^(-1/32)->0 and (L+log2L)/P->0, the combined
positive remainder is eventually at most P/64. The identity
3/64+1/64=1/16 proves the EXACT supported time bound (0.1).
Unknown constants occur outside the exponential and in terms explicitly
paid by these strict margins, never as guessed inner coefficients.

Depth-first live phase-qubit occupancy is <=B+5m_active+1<=6n+1;
all source/extraction/search arithmetic scratch is O(n). Thus S_Q=O(n).
Full signed labels, frames, source counters, decoder records and the
constant-4096 found list use O(n^2) classical bits by the included complete
ledger. The new p_root and its fixed-power binary-search scratch use
O(log n) extra bits, preserving S_C=O(n^2). These allocations are bounded
after wrong labels and on aborts as well. Every finite exception has
finite literal caps and affects only an absolute outside constant.

The log of each exponential representative has a positive leading
multiple of F; G,J,P=o(F). Thus log2log2max(4,B)=(1/2)log2n+
(1/2)log2L+O(1), so its exact growth index is 1/2. Both polynomial
space representatives have index zero. All four concern this ONE rule.

Compared with the published QLOG parent, which reports time
2^(3F/4+3G/4-J/12) and copies2^(F/2-3G/2+3J/16), the ratios are

 time: 2^(-J/96+P/16), samples: 2^(-3P/32).

Both tend to zero, because J/P=L^(1/32)->infinity and P->infinity.
The two spaces and exact clean model agree. This is strict improvement
of the reported joint upper-bound vector. It does not assert the old
bounds were tight or incapable of refinement. The actual program changes
both denominator correction and a fourth integer-root term; it is not
merely relabeling the previous manifest. At finite sizes the actual work
height can decrease while the source parameter increases; no finite
sample or elapsed-runtime superiority is asserted. The full supported
asymptotic guarantees, not finite fitted slopes, are proved above.

## 6. Fractional error tolerance

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The guaranteed fraction is zero for every N and s, with unconditional
full-secret success >=1-2^-8 and all four resource bounds jointly for
this one configuration. No positive tolerance or impossibility of positive
tolerance is asserted. The fifth expression has no numeric score.
