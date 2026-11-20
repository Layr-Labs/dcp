# RQ-D64-Balanced resource and tolerance proof

This supplies Sections 9-10 of the joint proof with proof.md and source.md.

## 9. Every-branch resources and exact indices

Put L=max(1,ceil(log2 n)). Depth is the fixed integer 64. For n>=128,
K=O(n), rbound=O(n), A_ell=O(n^(65-ell)), and Qcap=O(n^65).
Every stored word has O(n) bits; source/attempt counters and loop indices
have O(log n) bits unless they store candidates, labels or products.
In particular q0=(n+1)^64 has O(log n) bits and grid numerators P_j
have O(n) bits. The unequal widths and m are exact O(log n)-bit integers
computed once by counted arithmetic. They introduce no large stored table.

Implementation. Exact multiplication of O(n)-bit fields uses O(n^2)
ripple gates by shift-and-add. Division/remainder by a known O(n)-bit
modulus uses O(n^2) gates, one compare/subtract per dividend bit; reversal
retains O(n) borrow/control flags. The fixed 4096-row table scan costs
O(n) gates per argument and O(n) scratch. A K-term score costs
O(K*n^2)=O(n^3) core operations including reversible computation, record
reads and O(n)-bit scores. Circuit generation, bit-string operations,
initialization, measurement and reset are charged. Every addressed action
adds O(L) because allocated memory is O(n^2). We retain the conservative
core O(L) factor in NODE and EXTRACT, so their addressed bound has L^2.

Source work. Source.md proves O(n^2 L) core work per EXTRACT; a preceding
modular multiplier costs O(n^2). With addresses this is O(n^2 L^2).
All Qcap=O(n^65) original acquisitions, rejects, discards and transforms
therefore contribute O(n^67 L^2). The source cost n+1 is included.

Node work. At each ell, at most A_ell complete attempts execute, including
all failed trials. Section 4.2 costs O(n^2 L^2 2^ceil((b+1)/2)) after
addresses, and 2^ceil((b+1)/2)<=2*2^(b/2). Any partly constructed
parent inputs are charged to executed lower attempts or originals;
guards, stack cleanup and zero-width returns have polynomial cost.
For n>=2^18, b_ell<=c_ell=m-2(67-ell)L, hence level ell costs at most

 O(n^(67-ell)*L^2*2^(c_ell/2))
 =O(L^2*2^(m/2)*(n/2^L)^(67-ell))
 =O(L^2*2^(m/2)).

There are only 64 levels. This charges every executed node at its own
width; multiplying the worst width by the bottom-level attempt count
would lose the improvement. No expected runtime or successful-only
accounting is used.

Grid work. Each of at most 512 stages has Dcand=O(n^64*2^H) candidates,
hence padded square-root range O(n^32*2^(H/2)). Each search has O(L)
fixed trials, and each score predicate, diffusion, ordinal mapping and
classical reverification costs O(n^3 L) after addresses. Thus all grid
work is O(n^35 L^2 2^(H/2)). In the balanced range H=m-70L, so this is

 O(L^2*2^(m/2)*(n/2^L)^35)=O(L^2*2^(m/2)).

No source calls occur during grid searches. Euclid, CRT, table generation
and protocol initialization add only polynomial work within these bounds.

Since m<=(n+4486L)/65+1 and L<log2 n+1,

 2^(m/2)<=sqrt(2)*2^(n/130)*2^((2243/65)L)
          =O(2^(n/130)*n^(2243/65)).

The source term is absorbed without changing the exponential coefficient:
its ratio to 2^(n/130)*n^(2243/65)*L^2 is
n^(2112/65)*2^(-n/130). For a=2112/65 and c=(ln 2)/130,
x^a*exp(-cx) has finite maximum (a/(ce))^a for x>0, by differentiation.
Thus on EVERY balanced-range branch the full work is

 T=O(n^67 L^2+L^2*2^(m/2))
  =O(2^(n/130)*n^(2243/65)*(log2 n)^2).

For 128<=n<2^18 the exact original uniform tree/caps remain in force.
Its charged ledger is O(n^67 L^2+n^66 L^2*2^(H/2)
+n^35 L^2*2^(H/2)). Its ratio to the declared positive representative
has a finite maximum over this explicitly fixed finite set of lengths,
all N,s, source states and branches: the branchwise ledger depends only
on n. This maximum is an absolute outside constant. This finite range
does NOT use exhaustive search or assume zero noise; Sections 4-8 prove
its same online noisy success guarantee with the unchanged tree caps.

For n=1 the explicit decoder acquires Q1=2^31 copies and uses fixed
counters, finite constant work and constant storage. For 2<=n<128 the
proved zero-malformed exhaustive branch has Qactual<n^64, O(n) space
and work bounded only by known n. Its finite envelope ratios likewise
fit absolute constants. The representative is understood for n>=2;
the all-n protocol has separately specified finite costs at n=1.
No instance-dependent advice or unknown finite-input theorem is used.

Space on EVERY branch. Suspended siblings at level ell number at most
r_ell-1=b_ell; the current leaf adds one. Their total is B+1<=n+1.
Current merge/source/query/reversible scratch adds O(n), so S_Q=O(n).
All 64 frames include zero-width returns. Each full signed label has
D+64ceil(log2(n+1))+128=O(n) bits; O(n) stack labels occupy O(n^2)
classical bits. The K=O(n) decoder records each occupy O(n) bits.
The computed trig table is fixed finite size. Conservative
256n+4096+4ceil(log2K)-bit arithmetic fields cover source/level counters,
candidate products and signed scores. Thus S_C=O(n^2). Finite dispatcher
branches have the same asymptotic spaces with absolute constants.

The source guard gives Q=O(n^65) including every failed or unfinished
attempt, rejected copy and discarded input. The finite branches acquire
Q1 or fewer than n^64 originals. Analytical couplings and probability
transcripts are not physical algorithm storage or source calls.

Exact indices. For B_T=2^(n/130)*n^(2243/65)*(log2 n)^2,
log2 B_T=n/130+(2243/65)log2 n+2log2log2 n. Its further logarithm
divided by log2 n tends to 1. For n^2,n,n^65 the same limit is 0.
The exact resource indices are [1,0,0,0]; tolerance is unscored.

Against RQ-D64's jointly proved representative, the time ratio is
n^(-2047/65), tending to 0, while both memories and samples retain
their bounds and the identical ModelM. Tolerance improves by 3333/2500.
It also supports the plan's coarser O(2^(n/130)*n^35*log2 n) bound,
since its ratio to that representative is n^(-32/65)*log2 n -> 0.
We declare the more precise rational degree and conservative log square.
This is asymptotic guarantee dominance; unknown outside constants give
no practical speedup ratio. Numerical time index stays 1. The challenge
target 2^{O(n^(1/3))} remains unachieved and no optimality is claimed.

## 10. Fractional guarantee and exact scope

The declared expression is epsilon(n)=3333/(10000*n^(64)). ModelM means
online unflagged replacements chosen before each current honest draw;
fresh tensor-independent honest rho_s; arbitrary correlated replacement
states and private workspace; and almost surely at most
floor(epsilon(n)*Qactual) replaced ORIGINAL acquisitions at termination,
including all rejects and discards. Sections 3-8 prove unconditional
full-secret success at least 1-2^-8 for every N,s and admissible strategy,
jointly with all four EVERY-branch resource bounds above. Clean input is
included. No independent-position assumption, replacement flag or
postselection on an unedited subset or later budget fulfillment is used.
No larger fraction, different corruption model or numerical tolerance
score is asserted.
