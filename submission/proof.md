# PSG4-SECOND-SCALE-SEVEN: fixed q=1/3 two-scale configuration

## 0. Selected joint theorem and complete source

For every N>=2 and s in Z/NZ put n=ceil(log2 N), L=log2 n for n>=2,
F=sqrt(nL), G=sqrt(n)L^(-3/8), G2=sqrt(n)L^(-7/16). The ONE selected
program specified here recovers the entire s from independent ideal mixed
coset states, unconditionally with probability at least1-2^-8>2/3. On EVERY
execution branch, including failed/discarded work, wrong extracted labels,
both cutoffs, preprocessing, circuit generation, addressing and cleanup,

 T=O(2^((11/12)F+(3/4)G-(7/88)G2)), S_C=O(n^2), S_Q=O(n),
 Q=O(2^((1/3)F-(3/7)G+(1/2)G2)).                 (0.1)

All outside constants are absolute independent of N,s and outcomes. The
explicit n<256 branch includes n=1. Indices in time/classical/quantum/copies
order are1/2,0,0,1/2. The fractional guarantee is0 under the canonical clean
model in Section6. No cube-root time, optimality or resource lower bound.

The complete concrete source is PSG4-SECOND-SCALE, reproduced UNMODIFIED in
family-source.md, full SHA-256 11f96191f1ab9c78f070472c4cb5e0552ec25381398ffc13b51d7f9c1b7c3fc7.
Its publication identifier and source/use evidence accompany the eventual
note and declaration. The source supplies the entire C4096 program, source
extraction and verified-pair circuits, high-label laws, complete odd and
2-adic decoders, two literal caps and charged ledgers. Its Section11 proves
the fixed family used here. Its selected q=1/2 numerical theorem describes
another configuration; (0.1) binds ONLY the configuration below. Old verdicts
are not premises. Historical sources and credits remain in the supplied file.
The independent exact selected estimates in Sections3-4 resolve the constants.

## 1. One executed algorithm

The fixed rational parameters are

 q=1/3, c=11/12, f=7/11, alpha=3/8, alpha2=7/16, eta=3/4,
 lambda=54/77, kappa=7/44, mu=193/484.

For n<256 execute exactly the complete source Section8 finite candidate
tester with n+10 fresh tests per shift, controlled subtraction and X
measurement, first surviving shift or0. No analytical threshold is executed.
Otherwise compute ell_base=ceil(log2 n), g_base largest nonnegative integer
with g_base^8 ell_base^3<=n^4, and g2_base largest nonnegative integer with
g2_base^16 ell_base^7<=n^8. Fixed power comparison and binary search are
charged; no real root or logarithmic oracle is supplied. At each trial R>=1,

 u=min(R,max(1,floor(7R/11)
              +max(0,floor(54g_base/77)-floor(193g2_base/484))))).

Compute delta(v)=min d>=0 with20*2^d>=21(2v+6), descend from R by
v<-v-delta(v) retaining v>=u, then reverse the retained values. Use the FIRST
R with2S_u(R)>=n. Since the profile includes R, termination by ceil(n/2)
holds without any monotonicity assumption. The clipping defines every trial.
Since g_base>=g2_base and54/77>193/484, the inner difference is nonnegative
at every length. Also floor(7R/11)>=floor(R/3). Thus u>=floor(R/3)>=R/8
on the main feasible branch, preserving the per-attempt work bound.

Use source Sections1-8 with this sole profile substitution at EVERY use.
For each PS_TREE(D,B), greedily allocate widths from the root, no more than
2v_i per level, summing to B. Positive width b has b+6 children and the exact
verified-list cap4096 and bounded Grover attempts; zero width returns a child.
Recompute q0=(2u+6)2^(R-u), hmax=1+floor(u/8), odd-stage h,stride,nq,
K=2^13(ceil(log2 nq)+ceil(log2 n)+30), Sodd and all exact CRT values.
If no odd part, skip its decoder as in the source. Define

 H0=Sodd K+2n, Qstar=6(2u+6)2^(R-u)H0+2n,
 Qcap=1024 Qstar, Wstar=3mstar 2^R H0, Wcap=1024 Wstar.

Enforce BOTH literal acquisition and weighted-attempt cutoffs, aborting
before a copy or attempt would exceed its cap, with children already counted.
Recompute extraction confidence h_e=ceil(log2(2^16 Qcap(n+5))) and
F_e=2^21 h_e; execute the complete source EXTRACT translation-test instrument.
Follow the actual free-frequency odd decoder and shifted parity 2-adic
recovery, all failed ancestors and cleanup included. The preparation inverse,
a known purification, sampled position or Fourier label, quantum-addressed
memory and subset-sum oracle are not supplied. All full integer labels,
measurements, explicit gates, exact tables, classical searches, circuit
compilation and counters are the complete finite algorithms in the source.

## 2. Full-secret correctness and all-branch caps

Source Section2 gives independent uniform latent labels for fresh mixed
states. Its nondestructive collective extraction in Section3 applies at
our recomputed cap, coupling the complete computation to correct labels
except with probability<=2^-14. It does not measure away the phase coin.
The exact adjacent-pair projection and affine compression of Section4 give
the output phase law for each verified pair. Incomplete bounded discovery
only reduces success, and the measured-fiber estimate gives advancing
probability>=3963/4096>20/21 uniformly in the retained widths.

Selection uses canceled low blocks only. The disjoint-leaf signed-incidence
argument in Section5 leaves a coefficient +/-1 at an untouched leaf, hence
uniform unused blocks after marginalizing full records. These facts apply
to this profile and establish both the odd free-frequency decoder and the
conditional shifted parity recovery of the entire secret for every modulus.
They require no monotone capacity or independence of cost and acceptance.

The source telescoping and reach-event accounting apply for every clipped
u, with (21/20)r_i<=2^delta(v_i). They give uncapped expected raw copies
<=Qstar and expected total attempt weight<=Wstar, including failed ancestors
and later work following an incorrect decoder outcome. The two ACTUAL caps
therefore lose at most2^-10 each. Decoder error is<=2^-20, and extraction
coupling costs<=2^-14. The total unconditional failure is at most

 2^-10+2^-10+2^-14+2^-20<2^-8.

The exhaustive finite branch has error<2^-10 by the complete source tester
analysis. Literal finite caps and uniform allocation still apply after a
wrong label; resource bounds do not condition on successful execution.

## 3. Independent exact selected capacity and source analysis

Let x=sqrt(n). For L>=4096, x>=16L^2 and

 G(1-3/(8L))-1<=g_base<=G,
 G2(1-7/(16L))-1<=g2_base<=G2.

These follow from ell_base in[L,L+1], convexity and integer root floors.
The decrement interval integral in the complete source gives
2S_u(R)>=(R^2-u^2)/D_R, D_R<=log2 R+4.
Consider the ANALYSIS trial Rtest=ceil((11/12)F+(3/4)G-(7/44)G2).
Its ideal unrounded base is u0=(7/12)F+(33/28)G-G2/2.
Exact rational expansion gives

 R0^2-u0^2=F^2/2+(7/24)FG2-(81/98)G^2
                         +(579/616)GG2-(435/1936)G2^2. (3.1)

The F*G term cancels. For L>=4096, Rtest<=F eventually (indeed the
positive correction .75L^(-7/8)+1/F is smaller than1/12), and0<u0/x<=sqrt L.
All upper-base integer errors at the trial are bounded by x*e where

 e<=(7/11+193/484+1)/(16L^2)
          +(193/484)*(7/16)*L^(-23/16)
   <=(1/2)L^(-23/16).

Here the negative floor in g2 is controlled using its LOWER root bound;
the positive g term uses g<=G. Any upper clipping only lowers u. The inner
maximum is eventually inactive, and the lower maximum is inactive here.
Thus after division by n, the losses in (3.1), plus2(u0/x)e+e^2, are bounded
by6L^(-3/4). Since7/24>1/8, the same weaker sufficient estimate is

 (Rtest^2-u^2)/n>=L/2+L^(1/16)/16 eventually.

For L>=2^256 its surplus over L/2+(log2 L)/2+4 is positive: at that point
it is4096-128-4=3964 and its derivative multiplied by L is
L^(1/16)/256-1/(2ln2)>0 thereafter. Therefore the trial is feasible and

 R<=ceil((11/12)F+(3/4)G-(7/44)G2).               (3.2)

The lower bound R>=sqrt(n/2) and G=o(R) make clipping inactive eventually,
u=(7/11)R+o(R), mstar=O(R/L), hmax=Theta(R), H0=O(n), K=O(R).
Every analytic exception remains a finite length of the SAME capped
program; it changes only absolute outside constants, not correctness.

For acquisition prefactors the complete source's universal estimate applies:
Qcap<=2^38 n^3 2^(R-u), log2 Qcap<=R-u+4L for L>=38.
Using the correct signs in the floor/root bounds and (3.2),

 R-u <= (4/11)R-(54/77)g_base+(193/484)g2_base+2
     <= F/3-(3/7)G+(15/44)G2+(81/308)G/L+4.

The latter conservative constant covers all ceiling/floor errors. Since
G/L=o(G2), L=o(G2), eventually the last two terms, together with4L,
are at most G2/24. The resulting coefficient15/44+1/24=101/264<1/2
leaves a positive strict margin to the claimed source exponent (0.1).
This is an every-branch acquisition cap, not an expected successful cost.
No positive smaller-scale term is dropped or hidden inside an exponent.

## 4. Charged work, both spaces and strict margins

All retained v_i>=u>=R/8, n<=2R^2, so source Section4.2's per-attempt
O(R^2 L2^v_i) core gate bound applies. The weighted cap and H0=O(n) give
Wcap=O(nR2^R/L), hence total combiner core work O(nR^3 2^R).
Extraction costs O(n^2 L) per acquired copy; with Qcap=poly(n)2^(R-u)
it is lower than this bound since u=Theta(R). The FULL classical decoder
grid costs poly(n)2^(R-7u/8), also lower. Preprocessing is polynomial.
All resets, abort checks, arithmetic, program generation and source fees
(n+1)Q are charged. Including O(L) FULL addressing gives

 T=O(n^(5/2)L^(5/2)2^R).

Since (5/2)L+(5/2)log2 L+1=o(G2), eventually it is<=7G2/176.
Equation (3.2) therefore yields the stronger INTERNAL time
T<=C2^((11/12)F+(3/4)G-(21/176)G2).
The claimed -7G2/88=-14G2/176 leaves a positive7G2/176 gap.
That gap could separately pay any fixed polynomial physical interpreter;
none is executed in the present virtual configuration.

The exact depth-first occupancy bound B+5m_active+1<=6n+1 and O(n)
extraction/combiner scratch give O(n) live qubits. O(n)-bit full signed
labels for O(n) coins, frames and counters, bounded4096 solution lists,
parameter roots, all decoder records and arithmetic use O(n^2) classical
bits. Precision/cap words have O(R+log n)=O(n) bits. The fixed integer root
powers and their intermediate values require only O(log n)-bit words.
No exponentially large circuit description or lookup table is stored.
Every finite n has a finite uniform capped implementation and all four
asymptotic bounds jointly extend with absolute outside constants.

## 5. Exact indices and comparisons

G2=o(G), G=o(F). Thus both exponential resource representatives have index
1/2 and both polynomial ones index0. These are indices of proved envelopes,
not matching runtime lower bounds. Against PSG4-ELASTIC-SEVEN's reported
T2^((11/12)F+G), Q2^(F/3-G/4), both new representatives improve:
time ratio2^(-G/4-7G2/88), copies ratio2^(-5G/28+G2/2) tend to0.
That comparison does not make PSG4-ELASTIC-SEVEN an algorithmic source:
the complete concrete family and all executed routines here come from
PSG4-SECOND-SCALE. It is only a numerical comparator; this proof explicitly
includes the comparison so its scope is inspectable. No tightness or
per-instance runtime dominance claim is made. There is no promotion claim.

## 6. Error tolerance and limitations

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The guaranteed fraction is exactly0 for the same program and joint bounds.
No positive robustness or impossibility of robustness is asserted. The
q=1/3 parameter controls a SOURCE coefficient of sqrt(nL); the time growth
index stays1/2. The analytic expressions never become real-number oracles.
This is a fixed finite companion to the locally reviewed q=1/2 two-scale
configuration, not an input-dependent parameter selection or an infinite
limit exchange. Its selected claims require their own native/hosted review.
