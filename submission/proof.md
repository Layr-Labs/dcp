# PSG4-QLOG: quarter-step base with a denominator-scale correction

## 0. Selected theorem and provenance

For every integer N>=2 and secret s in Z/NZ, let n=ceil(log2 N). For
n>=2 write L=log2 n and define the analysis scales

 F=sqrt(nL), G=sqrt(n)L^(-3/8), J=sqrt(n)L^(-7/16),
 H=sqrt(n)L^(-1/2)log2 L.

The ONE integer program specified in Section 1 recovers the entire secret
with unconditional probability at least 1-2^-8. On EVERY execution branch,
including wrong-label outcomes, failed searches, discarded source copies,
cutoffs, classical preprocessing, address charges and cleanup, jointly

 T=O(2^((3/4)F+(3/4)G-J/12)), S_C=O(n^2), S_Q=O(n),
 Q=O(2^((1/2)F-(3/2)G+3J/16)).                       (0.1)

All outer constants are absolute, independent of N, s and outcomes. The
four exact representative growth indices are 1/2,0,0,1/2. Fractional error
tolerance is zero under the exact independent-ideal-copy model in Section 7.
The explicit finite branch covers n=1. H is an INTERNAL analytic scale;
it is never misencoded as a structured bound term. The selected bounds
in (0.1) contain only supported rational powers of n and log2 n.

This is a lower-order resource improvement within an established
square-root-growth sieve family, not a cube-root algorithm or optimality
claim. Its actual integer base changes, so every profile, decoder quantity,
precision and both literal resource caps are recomputed.

Two directly used public sources are declared:

* PSG4-SECOND-SCALE, submission 89ee2314-c0bd-464e-8da4-884c718cf012,
  evaluated commit f4ac88b213ea357aaf523ed97d317438ddb8d35f.
  Its complete proof is included BYTE-FOR-BYTE as family-source.md,
  SHA-256 11f96191f1ab9c78f070472c4cb5e0552ec25381398ffc13b51d7f9c1b7c3fc7.
  It supplies the complete C4096 instrument, exact source/extraction and
  quantum circuits, unused-label law, full all-modulus decoder, caps,
  probability proof, charged ledgers and integral capacity inequality.
* PSG4-LOGLOG-ENDPOINT, submission 08d74dc3-b542-4fc4-9727-72d7c913ddff,
  evaluated commit 3911bf322ec88a785b6f0405be7c30071475383f.
  Its proof.md supplies the integer denominator-scale correction and its
  root/capacity argument, adapted here with a new negative quarter J term.

The complete source's historical credits remain in family-source.md.
No prior acceptance or attribution verdict is used as a mathematical lemma.
Its selected numerical configuration is NOT executed here. The conventions,
circuits and probability arguments in its Sections 1-8 are executed with
Section 1 below replacing its profile-selection rule at EVERY use. Its
Sections 9 and 11's selected resource conclusions are replaced by this
proof's Sections 3-6, not silently combined with a different configuration.

## 1. Complete executed integer rule

For n<256 execute family-source.md Section 8's exact finite exhaustive
shift test, with n+10 fresh copies per candidate. For n>=256 compute

 ell=ceil(log2 n), z=ceil(log2 ell),
 g=max integer a>=0 with a^8 ell^3<=n^4,
 j=max integer a>=0 with a^16 ell^7<=n^8,
 h=max integer a>=0 with a^2 ell<=n z^2.

These are finite integer roots, found by binary search on [0,n], with
fixed integer powers and comparisons. Ceilings of logarithms of integers
use bit lengths and an exact power-of-two check. No real arithmetic oracle
is supplied. For EVERY positive integer trial R set

 u=min(R,max(1,floor(R/3)+2g-floor(j/4)+floor(11h/12))).       (1.1)

Since g>=j, the base correction is nonnegative. Thus u>=floor(R/3)
unless that floor is zero, when u>=1. This implies u>=R/8 for R>=1.
Clipping makes every trial meaningful with 1<=u<=R.

Set delta(v) to the least integer d>=0 with 20*2^d>=21*(2v+6).
Start at v=R and repeatedly subtract delta(v), retaining values v>=u.
Reverse the retained sequence to obtain v_1,...,v_m=R, and let S=sum_i v_i.
Choose the FIRST positive R for which 2S>=n, using sequential search.
This does not assume monotonicity of S or of the clipped rule. Since R
itself is retained, the search terminates by R=ceil(n/2). All its work is
polynomial in n, even by enumerating each trial and each height literally.

Run the FULL algorithm in family-source.md Sections 1-8 with this selected
profile and u. In particular, greedily allocate actual widths b_i<=2v_i,
from the root downward, summing to each requested B; use b_i+6 fresh
children at every positive width, with C4096 bounded Grover discovery,
verified pairs and exact phase compression. A zero width returns its child.
Depth-first evaluation discards every failed attempt's inputs. All source
transforms, signed labels and exact extraction circuits remain as specified.

Recompute, rather than import from another configuration,

 q0=(2u+6)*2^(R-u), hmax=1+floor(u/8),

and the complete source Section 6's h,stride,nq,odd stages Sodd and
K=2^13(ceil(log2 nq)+ceil(log2 n)+30). If M=1, set K=Sodd=0 as there.
Its complete CRT multiplier, frequency grids and 2-adic correction are used.
Use literal integer caps

 H0=Sodd*K+2n,
 Qstar=6(2u+6)*2^(R-u)*H0+2n, Qcap=1024 Qstar,
 Wstar=3m*2^R*H0, Wcap=1024 Wstar.

Check the acquisition counter before EVERY source copy, including rejected
Fourier labels; abort to output 0 before exceeding Qcap. Check and charge
weight 2^v_i before every complete level-i combiner attempt; abort before
exceeding Wcap. Child work before a parent abort remains charged. EXTRACT
uses this actual Qcap, with h_e=ceil(log2(2^16 Qcap(n+5))) and 2^21 h_e
collective rounds in each basis, as in complete source Section 3. No source
control, inverse preparation, purification, QRAM or extra oracle is used.

## 2. Full-secret correctness and literal cutoffs

Here the needed configuration-independent conclusions are made explicit;
their exact circuits and derivations are in the included complete source.
Its source identity is an exact convex decomposition of rho_s into a
uniform latent Fourier label and a product phase qubit/eigenstate. Exact
translations permit nondestructive label extraction with error at most
1/(2^14 Qcap) per acquisition. This is a coupling to an ideal run, not
conditioning the unused-label law on extraction succeeding.

At a positive width b, fresh low labels are independent uniform residues.
For k=b+6 children the size-biased measured subset fiber has mean <65.
The C4096 verified-list search and pairing succeed with probability at
least 3963/4096>20/21 before generating each fresh attempt's children.
Any selected pair is exactly correct even if discovery is incomplete.
All selection kernels depend only on cancelled low bits, not held-out
high blocks. At least one nonzero signed leaf incidence is a unit +/-1;
the untouched-block argument therefore gives uniform remaining quotients.
Distinct fresh calls use disjoint original leaves. For root label 2^B W,
W's parity is fair and its characteristic modulus is bounded by that of
one untouched uniform block. These are precisely the hypotheses of the
complete odd-part frequency decoder and shifted 2-adic parity recovery.
They hold for (1.1) because they do not depend on the choice of u.

For stages above the base, (21/20)(2v_i+6)<=2^delta(v_i).
Telescoping and the decreasing function (2v+6)2^-v for integer v>=1 give
expected source copies per root <=6q0. The expected sum of attempt
weights per root is <=3m*2^R. Failed ancestors are included: conditioning
on reaching a fresh attempt, its new child calls have the same uniform
conditional cost bounds; a geometric-sum recurrence does not require
attempt cost to be independent of success. Summing over the fixed odd
stages and fair-parity repeats gives expected acquisitions <=Qstar and
expected weight <=Wstar in the ideal uncapped process, including work
following a wrong odd-part decoder output.

The TWO real caps each lose at most 2^-10 in success by Markov's inequality
and coupling until the cap. They themselves give branchwise bounds,
not just expected resources. Decoder error is <=2^-20, and the at most
Qcap extraction calls have union-bound error <=2^-14. Thus unconditional
failure is at most 2^-10+2^-10+2^-14+2^-20<2^-8. When odd recovery is
correct, the complete source Section 7 proves every subsequent 2-adic
bit exactly. This recovers all of s for every N, including pure powers
of two and odd N. The finite n<256 branch has failure <2^-10.

## 3. Root estimates and direct capacity certificate

All assertions in this section are asymptotic inequalities with absolute
constants and an eventual threshold independent of N and s. Finite
exceptions still execute (1.1) and the literal caps; they enlarge only
outer resource constants. They do not change the algorithm or its uniform
correctness proof. Put x=sqrt(n), k=log2 L. As n tends to infinity,

 g=G+O(G/L+1), j=J+O(J/L+1),
 h=H+O(H/k+H/L+1)=H+O(x/sqrt(L)+1).                (3.1)

Indeed ell lies in [L,L+1], z lies in [k,k+2] eventually, and the exact
roots equal the floors of x ell^(-3/8), x ell^(-7/16), and x z/sqrt(ell).
For a fixed a>0, convexity gives 1-a/L<=(1+1/L)^(-a)<=1.
Floor errors are at most one. In particular all three scales are o(F).

The complete source's integral estimate applies to EVERY integer u:

 2S_u(R)>=(R^2-u^2)/D_R,  D_R<=log2 R+4.             (3.2)

For clarity it follows by assigning to each retained height v the interval
[max(u,v-delta(v)),v]. These contiguous intervals cover [u,R]. On each,
the integral of 2t is <=2v delta(v)<=2v D_R. Summing proves (3.2).
The bound delta(v)<=log2 R+4 holds for 1<=v<=R by its exact definition.

Consider the ANALYSIS trial Rtest=ceil(R0), where

 R0=(3/4)F+(3/4)G-(3/32)J+H,
 u0=R0/3+2G-J/4+11H/12
   =F/4+9G/4-9J/32+5H/4.

This is an analytic comparison trial, not an uncharged operation in the
program. Eventually Rtest is positive, less than F, and neither clipping
endpoint binds: u0/R0 tends to 1/3 and (3.1) has o(F) error.
The actual integer u at this trial satisfies u=u0+E where

 E=O(x/sqrt(L)+G/L+J/L+1).

Consequently E=o(F), and |2u0 E+E^2|=O(n)+o(n)=o(n k).
The ceiling's contribution to Rtest^2 is O(F+1)=o(n k).
Exact expansion gives

 R0^2-u0^2 = F^2/2+(7/8)F H -(9/2)G^2+(9/8)G J
             -(33/8)G H-(9/128)J^2+(33/64)J H-(9/16)H^2.       (3.3)

The F G and F J coefficients cancel EXACTLY. F H=n k. Every term in
(3.3) after (7/8)F H is o(n k): for example G^2/(n k)=L^(-3/4)/k,
G J/(n k)=L^(-13/16)/k, and H^2/(n k)=k/L all tend to zero.
The other ratios follow by multiplying these fixed powers; all tend to
zero as well. Thus with the actual rounded u,

 (Rtest^2-u^2)/n = L/2+(7/8)k+o(k),
 log2 Rtest+4 = L/2+k/2+O(1).                       (3.4)

There is a strictly positive (3/8)k surplus. Since k tends to infinity,
(3.4) and (3.2) prove 2S_u(Rtest)>=n eventually. The executed FIRST
feasible search therefore selects

 R<=ceil((3/4)F+(3/4)G-(3/32)J+H).                 (3.5)

This does not assume monotonicity of feasibility. Also each retained
height is <=R and their number <=R, so n<=2S<=2R^2 and R>=sqrt(n/2).
From (3.5), R=O(F). Because g,j,h=o(sqrt(n)) and R>=sqrt(n/2), clipping
is eventually inactive at the SELECTED R and u=R/3+o(R). These facts
justify all complete-source per-attempt and decoder estimates.

## 4. All acquired source copies, with the full supported bound

The complete source's deterministic caps give
Q<=Qcap<=2^38 n^3*2^(R-u) for the selected profile (an even coarser fixed
polynomial prefactor would suffice). Equivalently log2 Qcap<=R-u+O(L).
All constants are absolute. At the actual inactive-clipping base,

 R-u <= (2/3)R-2g+j/4-11h/12+2.

Insert (3.1) and (3.5). The coefficients are exact:

 R-u <= F/2-(3/2)G+(3/16)J-H/4
          +O(G/L+J/L+H/k+H/L+1).                   (4.1)

In particular (2/3)(-3/32)+1/4=3/16 and
(2/3)-11/12=-1/4. Each error term in (4.1), as well as O(L) from the cap,
is o(H): (G/L)/H=L^(-7/8)/k, (J/L)/H=L^(-15/16)/k,
(H/k)/H=1/k, and L/H tends to zero. Hence eventually

 log2 Qcap <= F/2-(3/2)G+(3/16)J-H/8.

Dropping ONLY this proved negative remainder establishes exactly the
supported Q representative in (0.1). No positive logarithmic, polynomial
or smaller-scale term is discarded. This is the total number of original
source acquisitions, not surviving leaves, roots or quantum storage.

## 5. All charged work and both spaces

Since u>=R/8 and n<=2R^2, the complete source's exact bounded combiner
cost is O(R^2 L*2^v_i) core work per entire attempt, not oracle queries
alone. The actual Wcap, the profile m=O(R/L), and the full decoder bound
H0=O(n) give all combiner core work O(nR^3*2^R). Source extraction costs
O(n^2 L) per acquired copy; its total is smaller because u=Theta(R).
The exact odd decoder enumerates its full frequency grid with cost
poly(n)*2^(R-7u/8), also smaller. Integer roots, sequential profile search,
CRT, arithmetic tables and all cap bookkeeping use polynomial work.

Every address is charged under total allocated storage O(n^2), adding
O(L) to the core ledger. Streaming generation, initialization, measurements,
failed Grover trials, rejected labels and resets are included. Thus the
same every-branch bound as the complete framework, now at the new R, is

 T=O(n^(5/2)L^(5/2)*2^R).

Using (3.5), the logarithm of this envelope is at most

 (3/4)F+(3/4)G-(3/32)J+H+O(L+log2 L).

Since H/J=(log2 L)L^(-1/16) tends to zero and (L+log2 L)/J also tends
to zero, their sum is eventually at most J/96. The identity
3/32-1/96=1/12 proves the EXACT selected time bound in (0.1).
All coefficients inside the declared exponential are explicit rationals;
unknown constants occur only in the outer big-O and in paid lower-order
errors with the stated strict margins.

Depth-first live phase qubits number at most B+5m_active+1<=6n+1;
all complete-source modular/extraction/search scratch is O(n). Thus
S_Q=O(n). Full signed labels, decoder frequencies, recursion frames,
precision/cap words, the constant-4096 found list and extraction counters
are O(n^2) classical bits as derived in family-source.md Section 9.
The extra public roots g,j,h,ell,z have O(log n) bits and fixed-power
binary-search intermediates have O(log n) bits. They preserve S_C=O(n^2).
All statements hold even following wrong labels or an abort. Every finite
n not covered by the eventual estimates still has finite literal caps,
so taking the maximum over that finite set enlarges only outer constants.

## 6. Exact indices and comparison of guarantees

For both exponential representatives, log2 B is a fixed positive leading
multiple of F plus lower scales G,J=o(F). Therefore
log2 log2 max(4,B)=(1/2)log2 n+(1/2)log2 L+O(1), giving index 1/2.
The polynomial space representatives n^2,n have index zero. All four
claims refer to ONE selected program, not different family members.

The published SECOND-SCALE representatives are
T_old=2^(3F/4+3G/4-J/24), Q_old=2^(F/2-3G/2+J/2).
Our selected time ratio is 2^(-J/24), and source ratio 2^(-5J/16),
both tending to zero. Spaces and the canonical tolerance model agree.
Thus the declared full vector strictly improves those published guarantees.
No matching lower bound on old actual costs, literature priority, global
optimality, practical speedup or automatic promotion is claimed.
Against LOGLOG-ENDPOINT's sample representative without a positive J term,
this row trades more samples for less declared work; it does not dominate
that endpoint. Equation (1.1) is a changed actual rule, not a renaming of
one earlier algorithm's fields. The finite exact derivation is (3.3)-(3.5),
not an input-dependent substitution into a fixed-parameter family theorem.

## 7. Fractional error tolerance

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

For every N and s, with malformed fraction zero, the complete program
succeeds with unconditional probability at least 1-2^-8 and all four
branchwise resource bounds jointly. No positive corruption tolerance or
impossibility of positive tolerance is asserted. There is no new numeric
objective for this fifth expression. It does not use Q's upper bound to
manufacture a fraction.
