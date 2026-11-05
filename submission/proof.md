# QSR17: tensor leaves and direct adjacent-pair known-frequency roots

## Joint theorem, exact parameters and provenance

For every N>=2 and fixed s modulo N, n=ceil(log2 N), the SAME program
recovers the entire secret with unconditional probability>2/3 and has
these bounds on EVERY branch:

 T=O(n^(19/4)*(log2 n)*2^((5/4)sqrt(n)*sqrt(log2 n)+(25/16)sqrt(n)*(log2 n)^(-1/4))),
 S_C=O(n^(7/4)2^(n^(1/4))) bits, S_Q=O(n) qubits,
 Q=O(n^(5/4)*2^((1/4)sqrt(n)*sqrt(log2 n)+(5/4)sqrt(n)*(log2 n)^(-1/4))).

Resource representatives apply for n>=2, with n=1 fixed absolute
cost, storage and count. Outside constants are absolute. Growth indices are1/2,1/4,0,1/2.
The fifth law is0 under the canonical independent ideal-copy model.
No positive-corruption guarantee or maximum-tolerance impossibility is claimed.

This is a time/source/classical-memory tradeoff. Compared with polynomial-space
recomputation it uses larger classical tables to improve time/source envelopes.
Compared with the sqrt(n)-exponent table construction it has smaller classical
growth index but slower sqrt(n log n) time/source growth. No tight-cost,
practical, optimality, fastest-known or cube-root claim is made.

For n<1048576 use the exact exhaustive baseline: n+2 fresh controlled-
subtraction/X tests per candidate t<N, returning the first all-plus candidate
or zero. True t passes certainly; each false candidate passes with probability
2^(-(n+2)), so success>3/4 by a union bound. Q<=N(n+2), T=O(2^n n^4),
and spaces O(n^2). The fixed finite prefix fits the displayed envelopes
with absolute constants, including n^2<=1048576n for quantum space.
A source/time outside constant as large as2^1048580 is allowed, explicitly
not a practical performance assertion. Remaining descriptions use n>=1048576.

Set ell=ceil(log2 n), R=isqrt(isqrt(n-1))+1, L=2^R,
T0=isqrt(n*ell-1)+1, m=ceil(T0/R), t=mR,
v=ell+4, b0=t-R-v, D=ceil((n-1)/b0),
r=R, q=r*m^(D+1).
All roots and ceilings are INTEGER algorithms with counted schoolbook work.
R is exactly ceil(n^(1/4)); no real advice or irrational parameter is used.
Set f0=16n/(16n-1), A0=m*f0,
Mgrid=2^22(q+1), hstat=ceil(log2(Mgrid+1))+ceil(log2(n+7))+20,
Kstat=2^32hstat, C=(n+5)Kstat+n,
Qstar=C*32r*A0^D, Qcap=ceil(1024Qstar),
p=n+ceil(log2(Qcap+2))+40.
Set G=2^1000 n*m*R^5*2^t, E0=G, E_i=f0(mE_(i-1)+G),
Wstar=G+C*32*(E_D+G), B=ceil(1024Wstar).
Compute these rationals/integers EXACTLY before source acquisition.
Abort and output zero before a source acquisition would exceed Qcap
or a core bit/gate step would exceed B. After abort or completion, a
separate terminal G-core-step allowance clears/releases live tables and
qubits without acquiring sources; its own clock is charged in the same
way. Total core work is at most B+G<=2B. Initialization and cleanup count.

The collimation/reindexing context is Kuperberg arXiv:1112.3333v1 Sections4.2,
4.3 and4.6. Regev quant-ph/0406151v1 Section3 supplies polynomial-space
multi-input subset-merging context. Their results/verdicts are not premises:
QSR17 supplies its complete rank instrument, probabilities and counted circuits.
It carries locally archived PSR1 exact-stream enumeration and replaces
the earlier COL13 constant-weight leaves by ordinary tensor leaves. Neither
local artifact has a published endpoint; needed stream material is reproduced.
No novelty is asserted for tensor products or standard exact ranking.

Published COL3,20dcb56f-cf80-4e95-8784-b2c66b9f6577, supplies carried aggregate,
unused-top-bit, all-moduli and cutoff arguments, reproduced here. Published
RLQGR2,8657ff0f-f4d3-4605-a583-a6d57d3205f4, supplies mixed-source eigenlabels;
published PG4,e40f2d5a-68c9-418b-b4e8-64a80305968e, supplied consulted gradient
kickback and one-initial-trace-error reuse. Their necessary helper arguments
and earlier Kitaev / Nam-Su-Maslov1803.04933v2 SectionII context are retained.
The ordinary mixed-eigenlabel gradient preparation differs from PG4's Fourier
circuit. No predecessor fast multiplication, robust score or Grover search
is used. No source inverse, purification, hiding oracle or free QRAM is supplied.

This directly carries the published MSRL5 regular stream/tree/control construction,
submission8fca011e-b320-4999-b898-be09e4130cf3 at candidate
db205d41db86bf1604f853ab8c08ee273978f237, whose relevant material is reproduced. MSR3,
5aafeb93-37d7-4b4c-bf75-44a2c84db4a8, supplies further consulted exact
stream/tree/bit-serial context. Their constant-weight leaves are replaced.
The root now keeps every known W for odd-part estimation and only waits for
odd W in two-adic parity. frequency-tools.md reproduces the local MSR4/MSR5
known-frequency estimator, without any predecessor verdict as a premise.
The source/work caps and precision are recomputed for this new instrument.
No private quantum counting, hashing, window, bucket dictionary or
approximately clean counter is used. Stream rank/unrank remains EXACT.

## Counted source and constant permutations

Put chi_k=N^(-1/2)sum_x exp(2pi i kx/N)|x> and
phi_(k,s)=(|0>+exp(-2pi i ks/N)|1>)/sqrt2. Expanding the source and summing
its uniform x cancels unequal Fourier labels, giving exactly
rho_s=(1/N)sum_k |phi_(k,s)><phi_(k,s)| tensor |chi_k><chi_k|.
label-tools.md gives counted nondemolition eigenlabel extraction with K=N,
d=n, planned count Qcap, H=ceil(log2(Qcap(n+5)+2))+20, and
whole-computation error<1/2048. Given k, source
control is unchanged. Apply X to obtain the positive phase qubit
q_k(s/N)=(|0>+exp(2pi i ks/N)|1>)/sqrt2 up to a global scalar. Reset/discard
data before the next acquisition. The ideal-label comparison is unconditional,
not conditioning an IID assertion on correct extraction.

A known unit alpha mod N applied as y->alpha*y mod N on source data gives
rho_(alpha*s), since x->alpha*x is a bijection. Extend by identity for y>=N.
Clean evaluation uses n controlled modular additions of alpha*2^i into a
zero accumulator, copies the product, and reverses; apply the permutation
in place by compute-swap-inverse using alpha^(-1). Each complete-domain
ripple comparison/add/select has O(n) gates and reused O(n) scratch, so this
costs O(n^2) gates and O(n) qubits, including invalid-domain guarding. Euclid,
constants and controller work are charged. The same construction at width p
implements odd constant permutations modulo2^p. Fixed Boolean gates have
exact constant-size Clifford+T decompositions. No source inverse is used.
The reference below uses true labels, ideal gradient and exact known phases;
the actual finite circuits are compared additively with both caps enforced.



## Uniform phase vectors, aggregate metadata and literal table access

For a fixed target width w<=n put Ftarget=2^(w-1). A phase vector of length L is
L^(-1/2)sum_(j=0)^(L-1) exp(2pi i F b_j theta)|j>,
with a known integer table b and irrelevant common global phase. It occupies
R index qubits, NOT L qubits. Store TWO O(n)-bit records per entry:
its phase label b_j and raw lower sum U_j. Incidences are NOT allocated.
In the proof only, entries correspond to DISTINCT binary strings x over
the original leaf controls a_i, satisfying
 sum_i a_i*x_i=F*b_j+c_global, U_j=sum_i(a_i mod Ftarget)*x_i.
The common integer c_global is independent of j. Incidence weights need
NOT agree. There is no popcount measurement or global incidence array.

### Direct tensor leaves

Acquire r=R independently filtered uniform w-bit labels a_i and keep
their phase controls as the R-bit index. Their tensor product ALREADY is
L^(-1/2)sum_x exp(2pi i theta sum_i a_i*x_i)|x> over all R-bit strings.
Classically enumerate the L masks to write B[x]=sum_i a_i*x_i and
U[x]=sum_i(a_i mod Ftarget)*x_i with reused bit-serial scratch. Set F=1,
c_global=0 and release the source-label list after recording the table.
Every incidence is distinct; weights vary freely. There is no constant-
weight filter, combinatorial rank/unrank, Pascal table or leaf rejection.
The source-label filter succeeds with probability at least1/2, so leaf
source expectation is at most2R, with all failures counted. Tensor/table
construction, initialization and every generated index/bit are charged.
Only R source controls and O(n) reused source/arithmetic scratch are live.

## Multiway product ranking and a single-pass output table

Take m same-level vectors of length L with common F. Write their label tables
as B_i[j] and raw-low tables as U_i[j]. Their product
has t=mR quantum index bits and2^t equal-magnitude amplitudes. Coherently
compute sum_i B_i[x_i] mod2^b, b<=b0, with m literal L-row XOR lookup
networks and ripple additions. Each query compares its R-bit index with
each classical row, XORs the known value under equality, then erases the
equality scratch. Add to the residue and reverse the query before proceeding.
O(n) scratch is reused, not one quantum flag per row. All rows/gates/addresses
are generated and charged; this is NOT quantum-addressed RAM.

Measure the low-sum value y and reset its register using the known bits.
On the measured set S of product indices x, all magnitudes remain uniform.
Enumerate every CLASSICAL z in[0,2^t) using a t-bit counter, split it into
its m known R-bit components, read the child tables classically and compute
its residue. Count M=|S| in t+1 bits (M can equal2^t). Store no list of S.

The complete rank(x) is the number of valid z<x if x belongs to S, and zero
otherwise. Coherently compute validity with the same m lookup networks,
erase their data scratch, and retain one validity bit. Enumerate all z:
when its known residue is y, compare z to quantum x and conditionally
increment a t-bit rank accumulator. Copy under validity, reverse the entire
enumeration, and erase validity. The accumulator is at most2^t-1, since
at most that many strings are strictly below any x. Ripple increments and
comparisons have O(n) reusable quantum scratch. Reverse enumeration regenerates
classical decisions; no exponential history or gate stream is stored.

The complete inverse XOR function g(rank) enumerates valid classical z with
a t+1-bit classical count c; under equality of zero-extended quantum rank
with c, XOR that known product mask z into its target and erase equality
scratch. There is at most one match. Rank>=M has no match and returns zero.
Each function is a complete Boolean XOR unitary on ALL encodings. On the
measured S they are inverse because both enumerate the same numerical order.
Compute rank into a fresh t-bit register and XOR g(rank) into old x, erasing
old x on this measured support. No which-index information is discarded.

Measure the high t-R rank bits and retain low R. A partial last L-chunk
discards ALL m children and regenerates them. Globally BEFORE conditioning
on y the partial probability is
 sum_y(M_y modL)/2^t <=2^b(L-1)/2^t <=2^(-v)<=1/(16n).
This is uniform for every input table list; small individual buckets may
be entirely partial. No independent/uniform-current-label assumption is used.

For an accepted chunk, build its L output records by ONE MORE enumeration
of all valid classical product masks z, keeping their running rank c. When
c lies in the selected interval[chunk*L,(chunk+1)*L), compute and write row
c-chunk*L. The new record is
 B_new=(sum_i B_i[z_i]-y)/2^b,
 U_new=sum_i U_i[z_i].
Set F_new=F*2^b. Every quotient is exact. The invariant common offset becomes
c_global_new=sum_i c_global_i+F*y, independent of the retained rank. The
conceptual original incidence is the concatenation of child incidences,
still binary and distinct for every output row. No common-weight
property is needed or asserted. The per-row raw-low sum is computed only from lower
labels. Old tables/scratch are reset/released with counted work.

Crucially this is one2^t pass with L writes, NOT L separate inverse searches.
The coherent rank, inverse erasure, M counting and output construction use
a fixed number of2^t enumerations plus m literal L-row queries, each with
polynomial per-mask/row work. Only the child/output tables are exponential
in R; no2^t classical table is allocated.

For target w<=n apply D_w=ceil((w-1)/b0) regular levels, cancelling exactly
w-1 bits with a possibly shorter final remainder. When w=1 there are none.
Depth-first traversal retains at most m-1 R-qubit siblings per level.
A surviving vector uses exactly r*m^D_w original accepted base controls,
not counting discarded source copies. These original labels/incidences are
analysis objects, not an allocated global array. All failures regenerate
the whole affected group and are charged.

## Direct adjacent-pair roots and a shifted-binomial law

After D_w regular levels, ONE length-L vector has F=Ftarget and a common
c_global. Measure its high R-1 index bits, obtaining j uniformly, and keep
the low bit. This selects the ADJACENT numerical rows2j and2j+1, with no
raw-key measurement, extra product vector or singleton rejection. Both
rows always exist because L is an even power of two. The pair identifier
has uniform probability2/L independent of all stored phases. ONLY AFTER
that measurement inspect the full two B records and set
 W=B[2j+1]-B[2j].
The retained qubit is EXACTLY q_1(W*Ftarget*theta) up to global phase.
Release the other index qubits/tables with counted reset/clearing work.
Each vector uses q'=r*m^D_w<=q/m conceptual source controls; |W|<=2q'
by the invariant and0<=a_i<2Ftarget. The public q remains a convenient
conservative bound, with |W|<=2q, and no q-bit incidence string is stored.

For the proof write a_i=ell_i+Ftarget*T_i, where ell_i<Ftarget and the
T_i are independent fair bits. All leaf indices and regular low-key/rank/
chunk choices ignore T: before w-1 cancellation, each top contribution
is divisible by the next prescribed residue modulus. Computational
partition probabilities depend only on uniform magnitudes. The direct
pair choice is purely numerical and likewise ignores full B records.
Thus T_i remain independent fair bits conditional on LOWER choices and
pair identifier, NOT on the entire high-label transcript.

The two distinct binary incidences have difference c=y-x in{-1,0,1},
nonzero, with d>=1 nonzeros and n_minus negative ones. Common residue
modulo Ftarget implies eta=(sum_i ell_i*c_i)/Ftarget is an INTEGER.
There is no requirement eta=0 or sum_i c_i=0. Exactly
 W=eta+sum_i T_i*c_i = kappa+Bin(d,1/2), kappa=eta-n_minus in Z.
Consequently
 E exp(2pi i W delta)=exp(2pi i(kappa+d/2)delta)*cos(pi delta)^d.
For circular |delta|<=1/2, cos(pi delta)>=0; its REAL part is at most
cos(pi delta) for EVERY d>=1 and EVERY integer kappa. At delta=0 it is1.
The estimator needs this upper population gap, not a centered or
nonnegative characteristic function. frequency-tools.md reproduces the
complete shifted-binomial gap, bounded-score concentration and decoding.
The law includes odd d and unequal incidence weights.

In odd-part mode keep EVERY W including zero and nonunits; the root
accepts certainly. Conditional on observed W the relative phase is the
same exact q_1(W*Ftarget*theta), so forgetting other data does not dephase.
In two-adic parity mode only, keep odd W. A nonempty signed sum of fair
bits has fair parity for any integer eta, hence acceptance is EXACTLY1/2.
Any such odd W gives the required(-1)^bit phase; no sign flip or
literal-W=+/-1 restriction is imposed. Retries regenerate ONE vector.

## All-moduli source supply and full-secret recovery

Compute N=2^a M with M odd by trailing zeros; do not factor M.
If M>1, put d=floor(log2N), F=2^(d-1), f=F/2^a, a unit modulo M.
For j=0,...,n+4 choose a CRT unit alpha_j congruent to2^j mod M and1
mod2^a (use2^j mod N if a=0). This is counted Euclid/CRT arithmetic.
Transform each NEW source's data by alpha_j, extract its uniform N-label k,
and retain only k<2^d. Success is at least1/2 and retained labels are IID
uniform d-bit integers. Charge every rejected source. After X its control
is q_k(alpha_j*s/N). Run the root in odd-part mode with w=d.
Its result is q_1(W*2^j*vartheta), with W known and
vartheta=f*(s mod M)/M modulo1.

For each j collect Kstat such root outputs, choose a fresh fair X/Y basis
for each measurement, record (W,basis,outcome) classically and release the
qubit. frequency-tools.md proves a uniform population gap on the finite
Mgrid grid, Hoeffding concentration with this ACTUAL hstat, rational
half-angle unwrapping and final rounding. With failure<1/1024 simultaneously
over all n+5 stages it recovers f*(s mod M), then its inverse yields
r_secret=s mod M. All trigonometry is counted finite classical rational
work. At M=1 set r_secret=0 and skip this odd-part procedure.

If a>0 prepare the one counted gradient below before the two-adic loop;
otherwise it is omitted. Write s=r_secret+M*t_secret, t_secret modulo2^a.
At level ell=0,...,a-1, given its correct previous low bits t_low, put
s0=r_secret+M*t_low. A new untransformed source has phase q_k(s/N).
The gradient subtracts the known k*s0/N phase. The ideal phase is
q_(k mod2^w)(t'/2^w), w=a-ell, t'=(t_secret-t_low)/2^ell.
The reduced labels are independent uniform w-bit integers because2^w
divides N. Run the root in parity mode. Its phase is(-1)^(W*t');
odd W makes the X outcome the next bit EXACTLY in the ideal reference.
Repeat and output r_secret+M*t_secret, the entire secret.

At most C=(n+5)Kstat+n completed generator calls occur. Correct odd-part
estimation and earlier parity bits imply correctness by induction.
If earlier estimates are wrong the qubits are still balanced and source
labels uniform, so all cost/retry bounds remain valid. Correctness is not
a premise in the source/work cutoff expectations.

## Counted approximate gradient and error transfer

gradient-tools.md supplies one actual approximate gamma_p from ordinary fresh
zero qubits, controlled modular translations, measurements and at most n+20
attempts. It acquires no DCP copies. Its trace-distance/abort allowance is
<1/1024, charged ONCE to all subsequent uses, not independently per reuse.
Ideal gamma is unchanged under translation, including on superpositions.
The source label k and known s0 are CLASSICAL, so compute
z=k*s0 mod N and c=floor(2^p*z/N) entirely classically by counted schoolbook
arithmetic. Controlled SUBTRACTION of c from gamma implements
exp(-2pi i c/2^p) on the source control. The exact reference correction is
exp(-2pi i k*s0/N); per use norm error<8/2^p. There are at most Qcap uses,
so telescoping quantum channels gives total error<=8Qcap*2^(-p)<1/1024.
All computations, constant loads, additions, inverse work and precision are
counted; no arbitrary rotations or phase oracle is free. Preparing gamma
before two-adic recovery may abort, but all acquired source copies still
count toward Q. Its ordinary preparation register is not part of source Q.

Actual source-label extraction uses planned count Qcap in label-tools.md.
Its whole-computation error<1/2048<1/1024 compares to true labels on the
UNCONDITIONAL exact ensemble. It remains uniform over adaptive CRT choices
and known estimates because every new source copy is independent and its
transformed Fourier label is uniform. Do not condition on correct labels
or absence of caps to claim uniform phases. Work/source caps enforce all
actual branch bounds even when labels/gradient/estimates are wrong.



## Counted work, reference expectations and literal hard cutoffs

A tensor leaf needs at most2r source acquisitions in expectation,
including its label filters. Regular nodes have uniform retry factor f0,
so EQ_0<=2r and EQ_i<=A0*EQ_(i-1). The direct root takes ONE completed
vector, with no odd-part rejection and parity success1/2. Thus at most
C desired roots cost at most4Cr*A0^D in expectation; the conservative
Qstar=C*32r*A0^D covers this uniformly. Markov bounds source-cap abort
by1/1024, with the actual guard stopping BEFORE Qcap on every branch.
This is a new source plan; the old extra factor m is removed, not free.

A CORE step is a fixed-size classical Boolean bit read/write/operation,
head move, circuit gate, measurement/reset, source acquisition or bit of
circuit/address generation, excluding only the monitor's own work.
No word, table query, whole enumeration pass or controller is free.
Use the explicit streamed operand generator in circuit-tools.md, with
constant-many a_addr-bit workwords and no retained circuit history.
A fixed-arity logical bit/gate and its complete own-address generation
cost at most2^100a_addr^5 raw CORE steps, each still paying full allocated-
memory price externally. Here a_addr<=10001+3x+R<=512n^(1/4)<=512R.
For each CLASSICALLY enumerated z<2^t, the m ordinary indexed child
reads, O(n)-bit subset/target sums and output-record work need O(mn+t)
logical positions. Quantum rank comparison/increment and inverse-g
controlled XOR add O(t). Since t=mR<=mn, complete generated work per z
is at most2^200 n*m*R^5, retaining a_addr^5<=2^45R^5 directly.
A fixed number of forward/reverse/count/inverse/output passes costs at
most2^250 n*m*R^5*2^t CORE steps, with every gate/loop/address field.

Coherent validity uses a FIXED number of m literal L-row scans per node,
computed once and later erased, outside the classical z enumeration.
Their O(mL(n+R)+mn+t) logical gates yield at most2^250 n*m*R^5*L
raw steps, absorbed by the corresponding2^t allowance. No quantum query
is inserted inside every classical mask iteration. All retained metadata
rows are written in ONE pass, with exact scratch reset and no2^t list.

The leaf/source/gradient/basic helpers may retain their older slower
bit-serial implementation:2^200n^12L+2^80n^8 core work is a loose
bound including tensor-leaf output enumeration, source filters,
initialization, the direct pair readout and terminal live-table clearing.
Since t-R>=H/2>=96x, t>=192x and n*m*R^5>=n, this and the fixed stream passes
are less than G/2 for the ACTUAL allowance G=2^1000n*m*R^5*2^t.
There is no weight-chunk leaf retry; all source filters are included.
No previous padding workload is assumed or hidden. Fixed Boolean gates
have exact constant-size Clifford+T decompositions; no arbitrary rotation,
preparation inverse, uncharged oracle or free word operation is supplied.

Uniform conditional expectations justify E0=G, E_i=f0(mE_(i-1)+G).
The exact recurrence is
 E_D=G*((16nm+1)A0^D-16n)/(16n(m-1)+1)<=2G A0^D.
The whole classical grid/unwrapping work is at most E_D, as shown below.
Including initial gradient and all root trials is safely bounded by
Wstar=G+C32(E_D+G).
The B-step clock then has abort probability<=1/1024 by Markov in the
uncapped reference. Fresh trial costs may correlate with success; the
bound needs only uniform conditional mean and success bounds before each
new trial, not independent full tables or a favorable success-conditioned cost.

Costs remain uniform after earlier estimation errors. All supplied qubits
are balanced in magnitude, and tensor-leaf/chunk/rank operations select and permute
computational amplitudes without phase-dependent interference. Even if
assigned labels no longer match the intended phase semantics, every vector
still has uniform magnitudes; initial target labels remain uniform and the
direct pair has the same shifted-binomial unused-top-bit law. Thus correctness of earlier
estimates is not a condition in the cutoff expectations. Wrong labels and
the actual approximate gradient are handled by unconditional finite-channel
comparison, while the syntactic caps bound every actual branch.

circuit-tools.md supplies the new complete streamed n*m*R^5 per-mask ledger
and the old-helper/cleanup absorption. controller-tools.md supplies the
fully charged O(n^(5/4)*sqrt(x)) overhead for each raw core event,
including the monitor's own addresses and direct source cost.

## Uniform original parameters with explicit two-term bounds

Write x=log2n,a=n^(1/4),H=sqrt(nx),V=sqrt(n/x),J=sqrt(n)x^(-1/4)
for ANALYSIS only. Every following inequality holds for EVERY n>=2^20,
not only powers of two. Runtime uses the exact integer roots above.
We have a>=32,R in[a,a+1],ell<=x+1 and
 H<=T0<=H+V/2+1, H<=t<T0+R<=H+V/2+R+1.
The ratios x^(1/4)/a and (a+2)x^(1/4)/a^2 decrease for x>=20.
Since V/J=x^(-1/4)<=1/2, a+2<=17a/16, and at20 x^(1/4)<3,
 (V/2+R+1)/J<=1/4+51/512<1/2.
Thus t<=H+J/2. Also H>=192x: at20,2^20>=192^2*20, and2^x/x
increases. We have H<=n/20, x<=sqrt(n), and log2n<=n^(1/4).

Since R+v<=a+x+6,
 (R+v)/t<=1/128+13/1920=7/480<1/64.
Here a/H=1/(a sqrt(x))<=1/128 and (x+6)/H<=13/1920.
Therefore b0>=63t/64,D<=64n/(63t)+1<=n,tD<=2n.
Moreover r<=3R<4a and r>=R>=a, while m>=H/(a+1)>=64.

The ceiling in m and ell gives
 log2m<=x/4+(1/2)log2x+1/x+4/(a sqrt(x)).
Using log2x<=x/4 and the small rounding terms<=x/8 proves log2m<=x/2.
The full logarithm is positive, so n/t<=n/H yields
 (n/t)log2m<=H/4+(1/2)V log2x+V/x+4a/x.
Divide the excess by J. Its three terms are at most9/8,1/40,1/64.
For the first, put y=x^(1/4):2log2y/y<=3ln(y)/y<=3/e<9/8;
ln2>=2/3 and e>8/3 follow from elementary integral/series bounds.
The other two use x>=20,a>=32,x^(3/4)>=8.

With e0=(R+v)/t<1/64 use1/(1-e0)<=1+2e0.
The cancellation-denominator correction is at most
2n(R+v)log2m/t^2<=R+v<=a+x+6.
Also2log2m+log2r<=5x/4+2.
Thus log2q<=log2r+(n/b0+2)log2m is at most H/4 plus
 (9/8+1/40+1/64)J + a+(9/4)x+8.
Now a/J=x^(1/4)/a<=3/32. The ratio ((9/4)x+8)/J decreases after20,
where it is at most159/1024. The displayed coefficients sum to less than2.
Consequently
 q<=2^(H/4+2J), t<=H+J/2.
No far analytic threshold or hidden exponential O coefficient is used.

As J/H=x^(-3/4)<=1/8, log2q<=H/2. The unused legacy bound2^t>=4(q+1) remains true, but direct pairing
needs no matching/support inequality. Also log2(q+1)<n/4. All metadata fit their
O(n)-bit fields. Also hstat<=log2q+x+52<=H, so C<=2^35nH.
Bernoulli gives (16n/(16n-1))^D<=2 and A0^D<=2m^D.
The exact source cap satisfies Qstar<=64Cq/m<=64Cq and
Qcap<=2^17Cq. Thus log2Qcap<=H/2+2x+100<n-41, so p<=2n.
The source-label precision Hlabel and all controller clocks have O(n) bits;
p>=n+log2Qcap+40 gives8Qcap*2^(-p)<1/1024.

## Sharper envelopes within this fixed QSR17 configuration

The preceding two-term bounds are convenient coarse width/precision
checks for QSR17. The following sharpens those intermediate analysis
inequalities within the SAME QSR17 runtime parameters, generator and caps.
The work guard differs from QSR13 as explicitly explained below.

The finite positive sums sum_(j=0)^7 1/j! and
2sum_(j=0)^3 1/((2j+1)3^(2j+1)) prove respectively
e>2718/1000 and ln2>693/1000. The latter is the first four positive terms
of the integrated geometric series for ln((1+u)/(1-u)) at u=1/3.
Exact rational multiplication gives2/(e ln2)<17/16.
Since ln(y)/y has its maximum at e, the first leading excess above is
 (1/2)log2(x)/x^(1/4)=2log2(y)/y<=17/16, y=x^(1/4).
The other two leading excesses still cost1/40 and1/64 in units of J.

A sharper bound log2m<=3x/8+1/10 follows from log2x<=x/4 and
1/x+4/(a sqrt(x))<=1/20+1/32<1/10.
Consequently the cancellation-denominator correction is at most
(3/4+1/(5x))(R+v)<=(19/25)(R+v).
The final2log2m+log2r term is at most x+11/5. Their sum is at most
 (19/25)a+(44/25)x+169/25.
The ratio x^(1/4)/a decreases for x>=20, and20^(1/4)<17/8, so a/J<=17/256.
The other ratio to J decreases as well and its endpoint is at most
((44*20+169)/25)*(17/8)/1024=17833/204800.
Therefore the COMPLETE q excess divided by J is at most
 17/16+1/40+1/64+323/6400+17833/204800 <5/4.
This includes every ceiling, residue-width and final-tree-depth term:
 q<=2^(H/4+(5/4)J).

For t, both ratios in
(t-H)/J<=(1/2)x^(-1/4)+(a+2)x^(1/4)/a^2
decrease after20. The exact integer inequalities
20*19^4>40^4 and17^4>20*8^4 imply
(1/2)x^(-1/4)<=19/80 and the second term<=289/4096.
Since19/80+289/4096<5/16,
 t<=H+(5/16)J.
Every inequality is uniform for EVERY integer n>=2^20. The coarse
root/field/label/gradient/controller bounds above remain valid. These are
proved tighter bounds, not an altered performance measurement or a reused
mathematical verdict.

## Whole classical-estimator cost and simultaneous resources

The finite-grid helper bounds all n+5 stages by
(n+5)2^150n^12q core steps. Since E_D>=Gm^D and q=r*m^(D+1),
their ratio to E_D is at most2^154n^13*r*m/G.
Here r*m<=3t<=n and G=2^1000n*m*R^5*2^t, so this is at most
2^(-846)n^13*2^(-t)<1, using t>=H>=192x. Thus the FULL grid evaluation,
record work, exact trigonometry and unwrapping fit E_D, not a free step.
All node, gradient, estimator and root work is included in Wstar.

The expectation recurrence and A0^D<=2m^D give
Wstar<=1000CGq/(r*m). Here r=R, R<=33a/32, a=n^(1/4), so G/(r*m)=2^1000*n*R^4*2^t
=O(n^2*2^t). Also m>=H/(a+1)>=(32/33)*a*sqrt(x). Since C=O(nH),
 B=O(n^(7/2)*sqrt(x)*2^((5/4)H+(25/16)J)),
 Q=O(n^(5/4)*2^(H/4+(5/4)J)).
controller-tools.md charges O(n^(5/4)*sqrt(x)) per core event, including
the monitor's own addresses and source acquisition. Initialization, public exact parameter
generation O(n^16) and terminal G cleanup are charged.
All live-table clearing costs polynomial times L and fits G since t>=H;
cleanup acquires no sources and uses a separate counted clock. Their polynomial
or polynomial-times-L costs fit this SAME exponential envelope. Hence
 T=O(n^(19/4)*x*2^((5/4)H+(25/16)J)).
Every coefficient is an explicit supported rational.

The depth-first stack holds O(m(D+1))=O(n/R) tables of L O(n)-bit records.
Since R>=n^(1/4),R<=n^(1/4)+1, its classical peak is
 S_C=O(n^(7/4)*2^(n^(1/4))).
All classical arithmetic/control buffers are O(n^2); the Kstat records
have O(nH) bits. They fit: sqrt(x)<=a gives nH<=n^(7/4), and
2^(n^(1/4))>=n^(1/4) lets the SAME envelope contain n^2.
The statistical grid is streamed, with no q-sized score array.
Quantum sibling indices use O(tD+t)=O(n) qubits. Exact stream-rank
comparisons, rank accumulators, leaf/sum scratch, source data and the
p<=2n gradient each use O(n), a constant number live. No emitted history,
incidence tree, QRAM, private count/window or coherent median is allocated.

The four source-label/gradient/phase-rounding/statistical allowances and
two Markov cutoffs total at most6/1024. Every comparison is unconditional
and all reference costs include retries; no source IID is conditioned on
correct labels, estimates or surviving caps. Correct parity follows after
correct odd-part recovery. Thus full-secret success>=1-6/1024>2/3, jointly
with all four every-branch resource bounds. Syntactic caps bound erroneous
actual outcomes too. The n<2^20 finite baseline has success>3/4 and its
explicit outside constants, with n=1 fixed separately.

## Joint improvement, changed circuits and exact scope

Relative to local QSR15 the source/tree schedule R,m,t,D is retained,
but tensor leaves REPLACE constant-weight rank leaves, and direct adjacent
pairs REPLACE the extra raw-key product root. The estimator is generalized
to shifted binomial laws with d>=1; its finite grid is four times larger.
The fifth-degree generator bound and ACTUAL G=2^1000*n*m*R^5*2^t are also
proved here. Qcap,p,Wstar,B and clocks are recomputed for THIS program.
Neither old root acceptance nor any earlier verdict is a premise.

Complete spaces and canonical error model agree with QSR15. Its old/new
time ratio is n^(3/4), and its source ratio is n^(1/4)*sqrt(x), both tending
to infinity. This is a strict joint time/source improvement without a
space/model tradeoff. No practical crossover, fastest-known, optimality
or cube-root claim is made. All finite n<2^20 behavior remains explicit.
Published QSR11 supplies the materially adapted schoolbook generator and
known-frequency score/concentration/unwrapping context; the fifth-degree
bound, unbalanced shifted law, tensor leaves and direct root are proved
here. Published QSR14 supplies the carried exact stream/controller and
all-size quarter-width context; its old root and leaf circuits are replaced.
The earlier published MSR3/MSRL5 constant-weight construction is not used;
their exact stream/tree/bit-serial context remains materially carried.
