# SEGMENT-RESET-CAP13: streaming pairing under a sample budget, T = O(n^32^((39999899241/28284200000)sqrt n)), Q = O(n^(3/2)2^((141421/100000)sqrt n)), S_Q = O(n)

## 0. Joint theorem and the exact segmented configuration

For every N>=2 and shift s moduloN putn=ceil(log2N). The SINGLE
SEGMENT-RESET-CAP13 algorithm below on independent ideal coset copies recovers
the entire secret with unconditional probability>=1-2^-8. EVERY branch,
including wrong labels, failed attempts, discarded/rejected acquisitions,
real range projections, support resets and aborts jointly obeys
 T=O(n³2^(t sqrt n)), S_C=O(2^(t sqrt n-13n^(1/4))),
 S_Q=O(n), Q=O(n^(3/2)2^(q sqrt n)),
 q=141421/100000,t=39999899241/28284200000.
Growth indices are1/2,1/2,0,1/2. Malformed fraction0 requires independent
ideal copies and asserts neither positive resilience nor impossibility.
Finite n<2^128 uses the separately proved exhaustive branch in13;
resource constants are absolute but may be enormous. At n1 logarithmic
envelopes usepositive n2 values. No practical quantum execution is claimed.

On main n>=2^128 compute exact integers
 r=ceil(sqrt n),m=ceil(qr),u=ceil(log2n),
 d0=100759/28284200000,base=ceil(d0r)+64,dl=base+2,
 Dwidth=floor(sqrt(128m))-1,Hlin=base+m-1,H=Hlin-Dwidth,
 L=floor(m/8),lift(k)=min(2,floor(2k/L)),
 lambda_i=min(base+i+lift(m-1-i),H) for0<=i<m,lambda_m=1,
 Kc=8192(m+10u+100),Kp=8192(u+100),gw=ceil(log2dl),
 b0=floor(log2n),Lblk=ceil(n/b0).
A public deterministic cycle list is built BEFORE access as follows:
starta=0; whilea<m putW=lambda_a, target=floor(W/4), remaining=m-a;
choosev=remaining ifremaining<=target+128, otherwisev=target;
append(a,v,sigma=ceil(log2v)+2), then seta+=v.
For each cycle at heightsa..a+v-1 set
 delta_j=(j+1)2^(j-v-sigma),M_(a+j)=(1-delta_j)2^lambda_(a+j).
There are at most128 cycles, allv>=128. At cycle boundaries a>0 a
binary merge first outputs the full power2^lambda_a with4-bit slack,
then a REAL measured index<M_a projection starts the next segment;
rejection rebuilds the entire subtree. The initial full tensor leaf is
likewise projected. Internal cycle binary steps have no reserved margin;
the final heightm uses full output2 with2-bit slack. ALL merges use
nonpower_mergeB for their ACTUAL input lengths. No free power reset,
state preparation or full-power-input assumption is made.

Budgets are allocated root-down in8. Actual delivered guards are
 D_R=2^156 dl2^m(R+u+16), C_R=4D_R.
These huge fixed coefficients are real counters, not omitted constants.
Block suppliers, staged coarse estimation, exact rational classical
scores and physical signed/two-adic block reconstruction are below.
Notation:dn=floor(log2N),N=2^a2 M withM odd,s1=s modM,s2 in[0,2^a2)
withs=s1+M*s2 modN,omega=exp(2pi i/N). All logarithms are base2.
Labels are nonnegative known integers; data basis encodings satisfy0<=u<N.
All roots, ceilings and schedule arithmetic use finite integer comparisons.

## 1. Actual sources and the support-reset contribution

The immediate full working source is the frozen SEGMENT-RESET artifact,
under its first genuine protected review at construction, then accepted
all five objects in406.30 seconds before this derivative was frozen. It supplies the
actual local support-reset schedule, constant2 uplift, <=128 cycles,
LOW cost coupling and2^156 actual guards, with the full physical block
decoder. Its actual HYBRID-BLOCK23 kernel source and working ancestry
are retained. Corrections must propagate; no predecessor verdict is a
premise. Actual canonical public identities must be verified and declared
if these working sources are registered before upload; none is invented.

Separately directly used is the actual frozen HYBRID-BLOCKCAP13 space
proof, whose first fresh protected review accepted all five claims in
254.12 seconds. It supplies the exact rational strict cap margin
128q>(67/5)^2 and explicitly charged growing plateau. Its same terminal
cap is originally supplied by the direct B64 source identified below,
with its historical CS1-C3 cap credit retained. This is not a claim of
independent cap invention or a new physical meaning for a prior verdict.

Direct published material retained is TAPER-SQRT2
7aaf9754-cafd-43f4-b072-f00b6490c1ce atfa84a323b64e99a5e6e7f13c6f363fe22dce44ab
for source/transforms/LE, radix/scan implementation, exact near-sqrt2
geometry, taper/high-field accounting and staged coarse estimator;
NONPOWER-CUBE c1f61c7d-e987-43fd-8fb3-faf19e7ebdae atf9df278591782804bdda7cc0406fe3bdbd458e85
for actual selected-interval/division maps and conditional binary moments;
NONPOWER-S58 b50e217c-3be6-4b1f-aeca-18948c12887e atd5daad9b9cb3ab32fb7fedbffa5bf9f3fa8f0d61
for weighted dyadic deficits, positive zeta and summed-loss proof; and
BLOCK64-SQRT2 8a59b2a0-202b-4702-8892-22cc1fc513bb at014da02ac3cd2390cb69189cd7515789028527b2
for unused-top-block uniformity, exact bounded scores and physical odd/2adic
block decoding. Exact used public proof/helper files were fetched, compared
where they were actual parent artifacts, and read; relevant provisional
incoming declarations were read through nextCursor null. Pending links
are not verified ancestry. Historical CSP40/BIFP1024 physical/allocation
and Kuperberg/CS1 credits remain retained through those actual sources.
B64's terminal cap/constant64 leaf augmentation IS directly used here,
with its stated historical CS1-C3 source credit retained. Its separate
old full-power-margin kernel is replaced by the actual segment schedule.

The new construction replaces the one long late segment and early
kappa-margin levels by at most128 actual weighted-deficit segments. It
uses counted full-power OUTPUT resets and real range projections, not
full-power input assumptions or amplitude amplification. This lets the
leaf uplift be the constant2 and proves all capacity, support integrality,
cycle counts, moment-domain and batch-guard constants afresh. The huge
2^156 delivered coefficient pays a fixed bound for all reset/projection
geometric factors. It does not change the exponent or hide a source oracle.
The resulting time improves HYBRID-BLOCKCAP13's n^(10/3) by n^(1/3),
with its SAME other four complete objects. Relative to uncapped
SEGMENT-RESET, classical space improves and other four objects are
retained. Both comparisons concern full objects; indices are unchanged.
No priority, independence, optimum, QRAM, arbitrary rotation, extra oracle,
positive robustness or practical-speed claim is made.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates on indexed qubits are classically addressed through this charge; there is no
quantum-addressed memory and no QRAM. Toffoli has a fixed constant-size exact Clifford+T decomposition;
gate generation and execution are both charged. A source acquisition
costs n+1. Hence

    T <= (number of core steps) * (1 + ceil(log2(S_C+S_Q+2))) + (n+1) Q.          (2.1)

## 3. Source identities, the latent-label model and data transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into rho_s = (1/N) sum_x |psi_x><psi_x|,
with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,          (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each copy is a convex mixture, with uniform weights, of the
product states phi_k(s) (x) chi_k. The whole algorithm is a linear adaptive quantum instrument
on independent copies. So the joint law of all classical outcomes equals the law obtained by
first drawing, per copy, an independent uniform latent label k and then running on
phi_k(s) (x) chi_k. All probabilities below use this model. Applying X to the control maps
phi_k(s) to, up to a global phase, the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each is a permutation
of all 2^n data encodings, extended by the identity on encodings >= N, and maps the copy
exactly to rho_s' for a known s'. The latent label of a copy is the Fourier label of its
TRANSFORMED data register.

(T1) Mult_alpha: u -> alpha u mod N, for known alpha coprime to N. Since x -> alpha x is a
bijection of Z/NZ, the copy becomes exactly rho_(alpha s). It uses n controlled modular
additions of the constants alpha 2^v mod N into a clean register, a swap, and the inverse
computation with alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for known c. Since |1,x+s>
becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N, an addition, a
comparison and a selector. It is the identity on encodings >= N, uses O(n) Boolean gates, and
is computed cleanly: compute, swap or XOR out, uncompute.

## 4. Rational trigonometric table

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20 of
cos(2 pi v/4096) and sin(2 pi v/4096): bound pi within 2^-90 with Machin's formula
pi = 16 atan(1/5) - 4 atan(1/239), summing 40 terms of each alternating series (tails below
2^-91); at the angle 2 v p_mid/4096 < 7, with p_mid the midpoint of the pi bounds, sum 80 Taylor
terms (remainder <= 7^81/81! < 2^-170; angle error < 2^-89; sin and cos are 1-Lipschitz); round
to denominator 2^24. This is a fixed finite computation, an absolute constant, not advice.

For x in [0,1) put tab_0(x) = Cos[floor(4096x)], tab_1(x) = Sin[floor(4096x)], and let
cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                        (4.1)

## 5. Label extraction LE

Input: a data register holding chi_k for latent k, beside arbitrary spectators. Let Qcap be the
source cap of Section 13. Parameters: J_e = n + 4, h_e = ceil(log2(Qcap (n+5))) + 12,
F = 2^21 h_e.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k. A TEST AT LEVEL j
prepares an ancilla in |+>, applies Tr_((N - 2^j) mod N) controlled by it, so that the |1> branch
gets eigenvalue omega^(k 2^j), and measures the ancilla in X (H then Z) or Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi 2^j k/N) or sin(2 pi 2^j k/N). Conditioned on k, chi_k and every
spectator are unchanged and outcomes are independent. Each test costs O(n) core steps.

For each j = 0..J_e take F tests per basis, giving empirical means x_j and y_j.

Decoding a level. Pick the least dr in [0,64) maximizing x_j Cos[64 dr] + y_j Sin[64 dr]. If both
means are within 1/1024 of their expectations, each computed dot product differs from
cos(2 pi (2^j k/N - dr/64)) by at most 2/1024 + 2^-19 < 1/256. The nearest direction has true dot
>= cos(pi/64) >= 511/512. Any direction at circular distance >= 1/16 has dot <= cos(pi/8) <= 31/32.
The gap 15/512 exceeds 2/256, so alpha_j = dr/64 is within circular distance 1/16 of 2^j k/N.

Unwrapping. Set g_(J_e) = alpha_(J_e). For j = J_e - 1 down to 0, let g_j be whichever of g_(j+1)/2
and (g_(j+1)+1)/2 (mod 1) is circularly closer to alpha_j (ties: the first). If g_(j+1) is within
e < 1/16 of 2^(j+1) k/N, the correct preimage is within e/2 of 2^j k/N, hence within
1/16 + e/2 < 3/32 of alpha_j, while the other is more than 13/32 from alpha_j. So the choice is
correct and the error halves. Finally g_0 is within 2^-(n+8) < 1/(2N) of k/N, and LE outputs
floor(N g_0 + 1/2) mod N = k. On any input LE returns a value in [0,N) after its fixed number of
tests, and then resets the data register. It uses no Fourier transform, no lookup, and no rotation
other than H and S.

Concentration. For F independent +-1 variables the centered log-moment generating function has
second derivative at most 1 and vanishes with its first derivative at 0. Hence
Pr(|mean - E mean| > delta) <= 2 exp(-F delta^2/2). With delta = 1/1024 and F = 2^21 h_e this is
2 exp(-h_e). So LE errs with probability at most 4(n+5) e^(-h_e), uniformly in k and in the adaptive
schedule. Over at most Qcap calls, the probability that ANY call returns a wrong label is at most

    4 (n+5) Qcap 2^(-h_e) <= 2^-10.                                                (5.1)

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(sqrt(n)) (Section 14),
this is O(n^(5/2)) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL run. Execute this same SEGMENT-RESET-CAP13 algorithm but replace each LE
output by its latent labelk. Actual and ideal runs can be coupled until
the first incorrect label, whose probability is at most2^-10 by(5.1).
There are no additional ancilla-preparation trials. Every resource bound
is for actual branches, using fixed caps and allocations.

## 6. Phase vectors and the linear merge

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical label table
lab[0..2^lam). In the ideal run its state is 2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a
global phase, for a fixed real th. Labels are nonnegative integers. The vector is COLLIMATED TO p
if all lab[x] are congruent modulo 2^p.

STORAGE. For a vector collimated to p, store one p-bit number
c=lab[0] mod2^p and an array hi[x]=floor(lab[x]/2^p), so
lab[x]=c+2^p hi[x]. The notation lab denotes these logical integers,
not a second materialized array. Each hi entry has its public level
width w_i from9. At p=0,c=0 and hi=lab. For p>0 no full-label
array is written: all operations below use c and hi directly.
The common prefix is known classical data, contributing a common phase;
no unknown rotation or physical phase correction is performed.

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x] into a clean w-bit
register, controlled by a lam-qubit index x. For each row x0 it computes the flag [x = x0] with a
Toffoli chain on O(lam) scratch, applies CNOTs from the flag to the output bits where tab[x0] has a
1, and uncomputes the chain. Indices outside [0,E) give output 0. The circuit is its own inverse,
has O(E (lam + w)) gates and O(lam + w) qubits, and is generated by reading each table bit once.

### 6.1a Stable digit-radix sorting and a merge join

For lam>=1, SORT(key,index) takes E=2^lam records with b-bit nonnegative keys
and lam-bit payload indices, initially in increasing payload order.
Store each record in a row padded to the next power-of-two bit stride;
this changes its size by at most a constant factor. Row/bit addresses
are then concatenations, not uncharged integer multiplications.
Put w_d=lam and B_d=2^w_d=E. The existing classical table
budget permits E counters; no array of size2^b is allocated.
If b=0 output the identity order. Otherwise for digits from least to
most significant, in chunks of w_d bits (pad the final chunk byzero):

- Zero B_d counters of lam+1 bits. Scan the records, extracting their
  current digit and incrementing that bucket's counter by fixed-width
  ripple arithmetic.
- Prefix-sum the counters to get bucket starts, each of lam+1 bits.
- Scan the input records in their current order, copy every bit of the
  record to the output at its bucket's next position, and increment that
  position. Swap the input/output arrays for the next pass.

Every pass is stable. Induction on processed digits gives final order
by(key,index), including repeated keys. A pass costs
O((E+B_d)(lam+b)) core bit steps, including counters, pointers,
prefix sums, digit extraction and every record bit copied. Sequential bit offsets are incremented with amortized linear total
bit updates per record; bucket positions are full lam+1-bit additions.
No word operation is charged as one step. Since B_d=E,

    SORT costs O(E(lam+b)(1+b/w_d)) core steps,
    and O(E(lam+b)+B_d(lam+1)) classical bits.           (6.1a)

All accesses are ordinary classical bit-array accesses, with the model's
address charge paid separately in14. No quantum lookup is added here.

To find partner runs, sort records(bb[y],y) and query records(t_x,x),
where t_x is the required key for x. Merge-scan their equal-key runs.
If a query key is smaller, assign its whole query run count0 and the
current data cursor as its insertion start. If a data key is smaller,
advance its whole data run. If equal, compute the data run's start and
length once and write them for every x in that query run. When the data
end, give remaining queries start=E,count=0. Each run/record is scanned
once, costing O(E(lam+b)) steps and linear record storage. The result
for each x is exactly its contiguous matching run in sorted data.

### 6.2 Actual arbitrary-length merge and counted support operations

Every binary merge in this configuration uses the complete explicitly
reproduced instrument nonpower_mergeB/C on its ACTUAL supported input
lengths and required output length. That includes full-power OUTPUT
resets; their inputs are still nonpower vectors. B defines all residue,
rank, arbitrary integer division, complete-interval selection, inverse
pair maps and finite padded-space reversible operations. Its exact
remainder formula, not a power-input shortcut, is used for every bound.
C charges radix sorting, scan lookups, one O(n²) rank division, all bit
arithmetic, table construction and scratch on arbitrary supported inputs.
The binary-incidence law D and cycle-local E bounds justify the stated
failure probabilities under the specific LOW conditioning F.

All padded input widths in this main configuration are>=base>=2u+1,
so actual input supports have at leastn² rows. This absorbs the ONE
O(n²) division cost per merge intoO(n(E+E')) core steps foractual
input/output rows. It is not an uncharged division per array row.
All indices and high fields are O(n) bits; actual rank/lookup fields
are O(sqrt n), since lambda_i<=H=Theta(sqrt n). Table initialization,
conditional arithmetic, clearing and addressing are included. Nonpower
supports and projections have no free state-preparation interface.

## 7. Direct phase-qubit supplier and quantum allocation

NEXT(0) simply requests the next accepted phase qubit from the batch
supplier. There are no other NEXT levels, slots, READY or PENDING queues.
The source and Section5 establish that, conditional on latent labels and
past outcomes, every delivered qubit is the two-entry phase vector(0,k)
in tensor product with all other live registers, on a fresh source-leaf set.
The supplier's acquisition counter includes rejected labels and failed tests.
All source/data scratch is reused. Each supplied control qubit is transferred
into a free location in the current leaf index register by counted SWAPs.

Use a fixed array of O(n) quantum working wires: two stacked tree-index
registers per level, global O(n) modular/LE scratch, O(n) merge lookup
scratch, and K=O(sqrt(n)) root qubits. Section14 gives its uniform size bound.
A classically addressed free-handle stack or equivalent known recursive
wire layout permits reuse with O(n)-bit bookkeeping per allocation, within
the charged ledger. No exponential register bank is allocated. Classical
tables are looked up by the explicit Section6 scan circuits, not QRAM.

## 8. Exact capped cycle schedule and capacity

Use the exact parameters of0. Write x=log2r>=64,l=log2n. Then
 qd0+q²/2=1,t=q+d0<3/2,qr<=m<qr+1,
 base=ceil(d0r)+64,dl=base+2,Hlin=base+m-1,
 Dwidth=floor(sqrt(128m))-1,H=Hlin-Dwidth.
Endpoint/monotonicity gives Dwidth>=64,Dwidth<=14sqrt r<m/4,
 base>=256u+1024,base>=4Dwidth+4u+8,base>=32,
 dl<=2base,gw<=base/4,b0<=u<=base/4,
 m+gw+b0<=H,H<=tr+1<=3r/2,(m+1)H<=4n.          (8.4),(8.7)
For base>=256u+1024 compare d0*2^64 with256*129+1024.
For the second lower bound compare d0r with56sqrt r+4(2x+1)+8
at r2^64; the linear ratios to square-root/log terms increase thereafter.
For the field inequality, Dwidth<=base/4 andbase>=4 give
base-1-Dwidth>=base/2>=gw+b0. The product uses m+1<=3r/2 and
n>=(r-1)^2>=9r²/16. Thus all supported arrays have>=n² rows.

L=floor(m/8)>=4,lift increments0/1 andlift(k)<=k/2. The exact bound
 2(Dwidth+1)<L
holds at the endpoint and increasingly thereafter since m>=r and
Dwidth<=14sqrt r. Hence lift(k)=0 for0<=k<=Dwidth+1. Capping lowers
just the lastDwidth input widths by1,2,...,Dwidth; lambda_0=dl and
lambda_(m-1)=H. All actual widths are nondecreasing with increments0/1,
 lambda_i<=dl+i,
 lambda_i<=H-max(ceil(k/2)-Dwidth,0),k=m-1-i.    (8.5)
There is a growing plateau and its storage is explicitly charged in14.

Public cycles use ACTUAL W=lambda_a in0, not the uncapped width. Every
nonfinal cycle hasv=floor(W/4)>=128 and leaves remaining>128, so the
final one also hasv>=128. Alwaysv<=W/4+128,sigma<=u+2 and
 W-2v>=W/2-256>=128u+256>=2sigma+64u.          (8.6)
All M_i are exact integers and at least7/8 padded length; widths may
have zero increments and the loss proof uses onlyE>=2^W.

Number of cycles with the plateau. If consecutive start heights are
both before m-Dwidth, their widths obeyWnext>=W+v-2>=6W/5 as in the
uncapped case. The plateau hasDwidth heights and every regular
v=floor(W/4)>=floor(base/4)>Dwidth by8.7. A cycle START on the plateau
has remaining<=Dwidth<floor(W/4), so it is FINAL under the lookahead
rule. Thus at mostONE nonfinal transition can end on the plateau;
all other nonfinal transitions have the factor6/5 growth. If there
were129 cycles, at least127 such growth steps would give
 Wlast/Wfirst>=(6/5)^127>2^20,
contradictingWlast<=H<2r,Wfirst>=d0r and2/d0<2^20. Therefore
there are at most128 cycles and127 nonfinal reset heights even here.
All projections are real measured operations with whole-subtree retries.

For every nonroot binary level use maximum2lambda_prev-lambda_next,
subtract4 at each nonfinal reset; final maximum is2H-1-2. Each is
positive because lambda_prev>=base+2>4. WriteJ for the reset count,
 A=sum_(k=0)^(L-1)(2-floor(2k/L))<=m/4,
 B0=(m+1)base+m(m-1)/2-1,
 CapLoss=Dwidth(Dwidth+1)/2<=64m.
Telescoping actual widths gives exactly
 Sum_i c_i=B0+2m-A-4J-CapLoss.
The constant64 base augmentation and the rational identity give
 B0>=r²+(d0-q/2)r-1+64(m+1),
 Sum_i c_i>=r²+(d0+5q/4)r-4J-1+64>=r²>=n.     (8.2)
Root-down allocation realizes exactlyB<=n bits within these maxima,
all reads belowB. Full-output resets use the arbitrary-input instrument;
no full-power INPUT identity is silently invoked. Internal moment
bounds are conditional on the LOW field, not complete high tables.

Set actual Dcap=2^156 dl2^m(Kc+u+16),Ccap=4Dcap,Y=ceilLog2Ccap.
Kc=8192(m+10u+100)<=2^14m,dl<=H and(m+1)H<=4n imply
 Kc*dl<=2^16n,Ccap<=2^175n2^m,
 Y<=m+u+176<=n/2,Kc/8192>=Y+u+30.             (8.1)
The last usesu>=128 and8u>=106. AlsoKp<=Kc. All fields and confidence
parameters are sized from these REAL huge caps before acquisitions.
The helper's moment product uses at most128 cycles and is unchanged.

## 9. BATCH(supplier, B, R, h=1)

Input is an actual supplier of positive one-qubit states with known
labelk and phaseexp(2pi i k th), fixedth; in the ideal run accepted
labels are iid uniform on[0,2^(B+h)),1<=h<=b0,1<=B,B+h<=n.
For1<=R<=Kc set actualdeliveredD_R=2^156 dl2^m(R+u+16),
actualsourceC_R=4D_R BEFORE access. Abort before an acquisition or
delivery would exceed its respective counter. Reuse the same framepool.
Compute all public cycles,M_i,windows,tp_i and high-field widths first.

FULLLEAF uses dl actual accepted qubits with source entries(0,k), guarded
before EVERY request. It forms the full tensor table by exact subset sums.
LEAF repeatedly buildsFULLLEAF and actually measures index<M_0; false
resets/releases the WHOLE leaf before rebuilding. True retains precisely
M_0 equal-magnitude entries and their absolute high fields/prefix.
Fori>0, CORE(i) repeatedly builds TWO fresh VEC(i-1) inputs and runs
nonpower_mergeB with the assigned window and actual input lengths.
Its output is M_i at internal cycle levels, full2^lambda_i at a reset
height, and full2 at heightm. FAIL resets both inputs before retrying.
VEC(i)=CORE(i) except at nonfinal reset heights, where it repeatedly
builds a fresh completeCORE(i), actually measures index<M_i for the
new cycle, and on false resets/rebuilds the WHOLE subtree. VEC(0)=LEAF.
No projection retry reuses a previously rejected vector. Every comparison,
measurement, cleanup and table construction is counted. All binary
merges, even full-power OUTPUT resets, use the arbitrary-input B maps.

RunVEC(m) R times, retaining one-qubit roots and their known frequencies;
no root measurement feeds this batch schedule. Every source/counter guard
applies inside all recursion and real projections. At completion release
all temporary index/high-field frames. There are no coherent bank/QRAM,
free nonpower input or unchecked full-power support resets.

Field widths. SetD_src=B+h. A leveli logical label sums at mostdl2^i
canonical source labels, even with real projections/resets, since each
successful binary tree combines disjoint child coordinate sets. Store
one tp_i-bit prefixc and absolute high entries of exactly
 w_i=D_src+i+gw-tp_i>=1 bits.
Each update hasw_next=w_i+1-b_i,so carries and truncation are exact.
This invariant also holds on wrong-label branches because accepted stored
source values still lie in[0,2^D_src); finite maps preserve exact sums.
No overflow abort reads unused high fields. SinceD_src<=n,m+gw<=Y,
 w_i<=n+Y<=3n.
At the root computeW=hi[1]-hi[0]=(lab[1]-lab[0])/2^B. Its state is
 (|0>+exp(2pi i2^B W th)|1>)/sqrt2.              (9.1)
Each logical value uses at mostC_R accepted labels, hence
 |W|<=2^h C_R<=2^h Ccap<=2^(Y+h).              (9.2)

Lemma9.1. In the ideal-label reference each batch aborts with probability
at most(2^-16+2^-12)/n, uniformly on prior history and its public supplier.
Proof: nonpower_mergeE bounds local weighted losses, full-output resets
and final root; F/G prove a LOW field coupling including all child costs
and all real same-height projections. H derivesK<=2^154 and the full
momentEexp(D_root/(2^156 dl2^m))<=exp(1/4). Its I proves actual delivered
and source guard tails2^-16/n and2^-12/n with the stated coefficients.
No expected-cost Markov bound replaces those exponentially small tails.
The coupling is analytical, not a new oracle or independence assertion
about actual cost/success. Actual branches obey deterministic caps after
wrong labels as well; success transfers by5's first-extraction-error
comparison, not by conditioning on a future clean-label event.

## 10. Unused-top-block independence and score discrimination

ForBATCH(B,R,h),write each accepted labelk_v=low_v+2^B tau_v,
0<=low_v<2^B,tau_v uniform inZ/2^h. LetG include all low_v,all merge
outcomes(e,bl),FAIL/retry/abort/qubit assignments and controller selection
history,but exclude root measurements,their fresh basis coins,unusedtau_v,
and LE internal coins/outcomes,which feed no ideal selection decision.
It is a coarse sigma-field,not the full computer record. Rejected source
history is independent of the subsequent uniform accepted value; every
fixed preceding rejected sequence has equal probability before each value
in its accepted interval. Direct modular suppliers are already uniform.

Every real cycle-start index-range predicate is independent of labels.
Every residue,sort,rank and block partition inspects only logical positions
belowB. Bits belowB of a sum depend only onlow_v. Stored prefixes and
exposed residue windows end belowB. nonpower_mergeB.1 for every actual merge makes the conditional law
of merge outcomes a function of these low bits and earlier outcomes only.
Induction factorizes the joint law as

    law(tau) law(low) law(outcomes,controller | low).

Thus conditional onG and randomness outside the batch,thetau_v remain
independent uniformZ/2^h. A table entry is the sum of leaves with a0/1
incidence vector. Distinct indices have distinct vectors: it holds for a
leaf(0,k_v),LEAF concatenates disjoint coordinates,and MERGE injectively
reindexes pairs on disjoint coordinates. The two root entries therefore
have different incidence vectors,so

    W=cst+sum_(v inSp)tau_v-sum_(v inSm)tau_v,       (10.1)

with disjointG-measurable sets,nonempty union,and integralG-measurablecst.
Every nonzero coefficient is+1 or-1. Holding all but one suchtau fixed
proves W mod2^h is uniform. Leaves of distinct roots are disjoint,so the
root frequencies are independent conditional onG. Forh=1 this also gives

    |E exp(2pi i phi W)|=|cos(pi phi)|^hd<=|cos(pi phi)|,
    Pr(W odd |G)=1/2,                              (10.2),(10.3)

wherehd=|Sp|+|Sm|>=1,as used by the unchanged coarse bootstrap.

Block score lemma. Letb=h or let a direct supplier give uniformW mod2^b.
Suppose independent roots have physical phase

    2pi J W v/2^b+eta, J odd, |eta|<1/16,

wherev is the desired residue. Independently for each root choose a fair
basisbeta in{0,1},measureX orY,obtainZ in{+1,-1}. Y isS^dagger thenH
then computational measurement. For everya in[0,2^b),compute

    S(a)=sum_roots Z*tab_beta((J W a mod2^b)/2^b),   (10.4)

using Section4's fixed rational table. Choose the smallest maximizinga.
All scores are exact rational sums of known table entries. In noiseless
exact-trig scoring the mean true score is1/2,and the mean false score is
(1/2)E cos(2pi JW(v-a)/2^b)=0,by uniformW and oddJ. The angle perturbation
changes each expectation by at most1/16; table error adds at most1/625.
Thus true-minus-false expected score exceeds1/4. Each table value has
absolute value<=1+1/625,so each score difference lies in[-3,3]. Independent
root scores obey Hoeffding:

    Pr(S(a)>=S(v) |completedG)<=exp(-Kp/288).

Here the interval width6 gives exp(-2Kp*(1/4)^2/36). Union over at most
2^b<=n false candidates yields n exp(-Kp/288)<=2^-30/n,using
Kp=8192(u+100),u>=log2n. This includes harmful ties. Phase perturbations
may depend onW; the uniform error bound suffices and no independence of
eta andW is asserted. Conditional completedG retains all unused top labels;
therefore integration bounds wrong-block AND completion. Aborts are charged
separately. Direct independent qubits satisfy the same argument.           (10.5)

## 11. Odd part: bootstrap followed by signed near-parity

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every coarse stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (m + 10u + 100), u=ceil(log2n).                                              (11.0)

Put J_full=min{j>=0:2^(j+3)>2M} and J0=min(J_full,Y+5).
Run the following coarse stages j=0,...,J0, each with Kc roots.
There are at most Y+6 stages, and at most log2 M stages.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. To supply one leaf qubit, repeat until accepted: acquire a fresh
copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard), and on acceptance apply X to the
control. The batch's acquisition cap applies. In the ideal run accepted labels are i.i.d. uniform on [0, 2^dn), and each copy
is accepted with probability 2^dn/N > 1/2. The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(dn-1) W th = W 2^(dn-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),           (11.1)

so a root is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known frequency f = 2^j W.

Measurement. Run BATCH(supplier,dn-1,Kc) for stage j. For each root i = 1..K obtain a fair bit beta_i by measuring H|0>, and measure the
root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in {+1,-1} with W_i and beta_i. Given W_i and beta_i,
E Z_i = cs_(beta_i)(f_i theta) with f_i = 2^j W_i.

Candidates. Put P_j = j + Y + 8 and identify an integer c with the point zeta = c/2^(P_j) on R/Z. Stage 0 uses every c in
[0, 2^(P_0)). Stage j >= 1 uses every c within circular distance rad_j = 2^-(j+2) of the previous center z_(j-1); both
z_(j-1) and rad_j are multiples of 2^-(P_j), so the arc endpoints are candidates. There are at most 2^(Y+8) candidates.

Score. For each candidate, with exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

Enumerate candidates in increasing order, keeping the K residues (f_i c) mod 2^(P_j), updating each with one addition per
step, and keep a running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have fixed lengths.

Lemma 11.1. Suppose theta is within circular distance rad_j of z_(j-1) (no condition when j = 0). In the ideal run,
conditional on BATCH not aborting, with probability at least 1 - 2^-20/n, theta is within circular distance 2^-(j+3) of z_j.

Proof. Condition on the past of the stage and on G. For a candidate point zeta let Delta = theta - zeta as a circular
difference, and xi_i = Z_i cs_(beta_i)(f_i zeta). Given G, the roots use disjoint leaves and independent coins, and their
measurements are on separate qubits, so xi_1, ..., xi_K are independent with values in [-1,1]. Averaging over beta_i,

    E[xi_i | G, W_i] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(2 pi f_i theta) sin(2 pi f_i zeta)] = (1/2) cos(2 pi f_i Delta).

By (4.1) the computed score differs from sum_i xi_i by at most K/625.

Near point. The candidate zeta0 nearest theta has |Delta0| <= 2^-(P_j + 1). By (9.2), |f_i| <= 2^(j+Y+1), so
|f_i Delta0| <= 2^-8 and E[xi_i | G] >= (1/2) cos(pi/128).

Far points. Call zeta far if |Delta| >= 2^-(j+3). In stage 0, |Delta| <= 1/2. In stage j >= 1, theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j+1). So xx = 2^j |Delta| is in [1/8, 1/2]. By the incidence law (10.1) and characteristic bound (10.2) with phi = 2^j Delta,

    E[xi_i | G] = (1/2) Re E[exp(2 pi i 2^j Delta W_i) | G] <= (1/2) cos(pi xx) <= (1/2) cos(pi/8).

Concentration. By Hoeffding each fixed candidate's sum deviates from its conditional mean by at least K/64 with probability
at most exp(-K/8192). Outside these events,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625 > (K/2) cos(pi/8) + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the maximizer is not far. There are at most 2^(Y+8)
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(m+10u+100) <= 2^-(Y+u+30), using8.1. The failure
probability is at most 2^(8-30)/n <= 2^-20/n. QED.

The hypothesis for stage j+1 is the conclusion of stage j. There are at
most n stages, so all coarse conclusions hold except with probability
2^-20 (apart from batch aborts counted separately). If J0=J_full,
round M z_J0 to the nearest integer modulo M, obtaining s1 as before,
and skip the fine stages. The error is strictly below1/(2M).

Otherwise J_full>Y+5. Since j=Y+5 does not satisfy the defining strict
inequality, M>=2^(Y+7). Put the known integer

    chat=floor(M z_J0+1/2) mod M,
    R0=M2^(-Y-8)+1/2.

On correct coarse conclusions the circular error of z_J0 is at most
2^(-Y-8). Therefore a unique signed lift t0 congruent to s1-chat
modulo M satisfies |t0|<=R0. Also R0>=1, R0/M<=2^(-Y-7)<1/2.
Indeed rounding adds at most1/2, and M>=2^(Y+7) bounds that term
by M2^(-Y-8). This is a mathematical bound, not a measurement of t0.
It also proves |t0|<M/2, including rounding and circular wraparound.

Fine blocks. Initialize low=0,j=0. Whilej<n putb=min(b0,n-j),B=dn-b.
The large-M branch has M>=2^(Y+7),dn-a2=floor(log2M)>=Y+7 andY>=m>=b0,
so B>=a2+1. Compute gamma=2^(B-a2) modM and K0=(-2^b)^(-1) modM
as the representative in[1,M). Both are units becauseM is odd. Define

    J=(2^b K0+1)/M.

This is an integer,1<=J<=2^b,andJ is odd because its numerator andM
are odd. Compute by extended Euclid and CRT a unitalpha moduloN with
alpha=1 mod2^a2 and gamma*alpha=K0*2^(-j) modM.
Setcj=(chat+low) modM. On each fresh copy applyShift_cj thenMult_alpha,
runLE,accept iffk<2^dn,and applyX to the control. Accepted labels are
uniform on[0,2^dn)=[0,2^(B+b)),acceptance>1/2; every rejection counts.
RunBATCH(supplier,B,Kp,h=b). On a correct past,t_j=(t0-low)/2^j is integral.
The exact transformed root phase is

    exp(2pi i 2^B W alpha(s-cj)/N)
      =exp(2pi i K0 Wt_j/M)
      =exp(2pi i J Wt_j/2^b) exp(-2pi i Wt_j/(2^b M)). (11.2)

The unknown two-adic component cancels sinceB>=a2; equality uses the
CRT relation and s-cj=2^j t_j modM. The final small phase is a physical
consequence of modular source transforms,not a synthesized rotation.
Measure and score by10.4 with thisJ,b; let the chosen residuebea.
Updatelow+=a2^j,j+=b. These rules also specify every incorrect history.

On a correct past |t_j|<=R0. The invariant follows fromR0>=1 and
|(t_j-(t_j mod2^b))/2^b|<=(|t_j|+2^b-1)/2^b<=R0,includingnegativeintegers.
By9.2,|W|<=2^(Y+b),so the phase perturbation in11.2 has magnitude at most

    2pi 2^Y R0/M<=2pi/128<1/16,

usingpi<4 andR0/M<=2^(-Y-7). Lemma10.5 bounds each wrong completed
block by2^-30/n. After at mostLblk=ceil(n/b0) correct blocks,low=t0 mod2^n.
Recover the signed n-bit integer t=low iflow<2^(n-1),otherwise low-2^n.
Since|t0|<M/2<=2^(n-1),this equals t0. Output s1=(chat+t) modM.
Coarse failure,extraction errors and aborts retain their separate budgets.

## 12. Two-adic part by blocks

Ifa2=0 puts2=0. Otherwise initializeg=0,s2low=0. Whileg<a2,
putwd=a2-g,b=min(b0,wd),sh=(s1+M*s2low) modN. On a correct past
rem=(s2-s2low)/2^g is integral modulo2^wd. A supplier acquires a copy,
appliesShift_sh,runsLE,appliesX,and useslabelkk=k mod2^wd. Ideallykk
is uniform on[0,2^wd) because2^wd dividesN,and its phase is
exp(2pi i kk rem/2^wd). No rejection is needed.

Ifwd>b runBATCH(supplier,B=wd-b,Kp,h=b); its root has phase
exp(2pi i Wrem/2^b),andW mod2^b is uniform by10. Ifwd=b useKp direct
supplier qubits,withW=kk and the same phase; no depth-zero tree is invoked.
Apply10.4 withJ=1 to choosea,and updates2low+=a2^g,g+=b. Release allroots.
There are at mostLblk blocks and at mostone direct batch. Conditional on
correctpast,s1 and ideal extraction,the phase error iszero,so10.5 bounds
each wrong block by2^-30/n. Allcorrectblocks yield s2low=s2 in[0,2^a2).
Output(s1+M*s2low) modN. Rules,sourcecaps and exact modular computations
remain defined on incorrecthistories and their resources are still bounded.

## 13. The complete algorithm and its success probability

Finite branch (n < 2^128). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. This branch acquires at most N(n+10) copies. Its resources are bounded by an absolute constant over this finite range; the exact main-branch cap below is not asserted here.

Main branch (n >= 2^128). Compute a2,M,dn,J_full,Kc,Kp,the
schedule,Dcap,Ccap,Y before access, where Dcap,Ccap denote the Kc caps
from8. For a batch with R roots use D_R,C_R as in9. Put

    Cp=2^158 dl2^m(Kp+u+16),
    Qcap=(Y+6)Ccap+2Lblk*Cp+Kp, Lblk=ceil(n/b0).

Size LE with this Qcap before any source acquisition. Run11 then12.
Any ABORT releases everything and outputs0. There are at mostY+6
coarse batches, Lblk odd fine batches, and Lblk two-adic batches; the
final direct two-adic block uses at mostKp copies. Thus Q<=Qcap on EVERY branch.
There are at most3n batches sinceY+6<=n throughout the main range.
Compute all CRT constants with ordinary polynomial-time integer routines.

Success. Lemma9.1 holds uniformly for each R, and its proved sharper
estimates9.3/9.4 give abort probability at most(2^-16+2^-12)/n
per batch. Over3n batches this is at most3(2^-16+2^-12).
Add coarse decoding2^-20, all odd/two-adic wrong blocks2^-29 and global LE coupling2^-10. Their sum is less than
2^-8. Correct preceding stages suffice in every conditional error bound;
a union bound on the first error proves unconditional full-secret success.
The finite branch has error at most2^-10 as before. Resources below
bound actual branches even when a prior estimate or extracted label errs.

## 14. All-branch resources

Every counter, array and retry is capped. With l=log2n, Section8 gives
m,Kc,dl,H=Theta(sqrt n),Kp=Theta(l),Y+6=O(sqrt n),Lblk=O(n/l),
Ccap=O(n2^m),Cf=O(sqrt(n)l2^m). Coarse batches acquire
O(n^(3/2)2^m) copies and all fine/two-adic batches acquire
O(n^(3/2)2^m). Thus on every execution branch

    Q<=Qcap=O(n^(3/2)2^m).                         (14.0)

The sum of delivered-demand caps has the same envelope, including every
rejected label, failed input and abort. The quantum stack has at most two
retained index registers per level, each<=H;8.4 gives(m+1)H<=4n.
Leaf, source/data, modular/LE, lookup/controller scratch and Kc root qubits
add O(n). All wires are reset/reused. Therefore S_Q=O(n), with no QRAM.

Classical space. Put k=m-1-i. Remaining precision satisfies
R_i=B-tp_i<= (m-i+1)H=(k+2)H since each nonroot capacity is belowH
and the root below2H. Thus actual high fields obey
w_i=R_i+h+i+g_w<=(k+3)H, usingm+g_w+b0<=H. Radix buckets, records,
ranks/orders and inverse maps need O(H) bits per row. Output length
is at most2E_i with field at mostw_i+1. Equation8.5 gives
 E_i<=2^H2^(-max(ceil(k/2)-Dwidth,0)).
All retained siblings,output and scratch frames are therefore bounded by
 H2^H sum_(k>=0)(k+4)2^(-max(ceil(k/2)-Dwidth,0))
 <=16(Dwidth+5)^2 H2^H.
Splitk<=2Dwidth from the rest. The first sum is(2Dwidth+1)(Dwidth+4).
Pairingk=2(Dwidth+j)-1,2(Dwidth+j),j>=1, gives remaining4Dwidth+15.
The total2Dwidth²+13Dwidth+19 is<=16(Dwidth+5)². SinceDwidth²=O(m)
andH=Theta(sqrt n),S_C=O(n2^H), including the growing plateau.
Prefixes,source/LE,controller,small roots and classical score scratch
add polynomial space absorbed by this bound. No storage oracle is used.

Work. Each leaf costs O(n2^dl) core steps and consumesdl delivered
qubits. A merge producing heighti consumes2^i dl disjoint canonical
delivered qubits not reused by another attempt there, and costs
O(n2^(dl+i+1)). A partial leaf at abort is charged fully. Each actual cycle-start range
projection at heighta has costO(n2^lambda_a) per trial and consumes a
fresh entire subtree withdl2^a canonical coordinates. There are at most
128 projection heights, including the leaf; failed predicates rebuild
and every request is guarded. These add at most128 additional terms
to the same source-based level ledger, soO(m+128)=O(m) levels overall.
All nonpower input supports have at leastn² rows by8.7; thus the ONE
O(n²) division per merge is absorbed at EVERY actual level, including
near-leaf ones. No such operation is silently charged as constant.
All m levels
cost O(nD_R2^dl(m+1)/dl) per batch, with(m+1)/dl=O(1) by8.
Using14.0 gives O(n^(5/2)2^(m+dl)) core tree steps. Address width
is O(H+logn)=O(sqrt n), so total tree work is

    O(n³2^(m+dl)).                                (14.1)

Extraction confidence has logQcap=O(sqrt n), so source/extraction costs
O(n^(5/2)) core per copy and O(n^(9/2)2^m) total with addresses.
Coarse scoring over O(sqrt n) stages costs O(Kc*n*2^Y*sqrt n)
=O(n³2^m) core steps. Fine block votes, signed updates, parity and CRT,
source charges(n+1)Q, gates, resets and parameter work are also included.
Each block enumerates2^b<=n candidates withKp=O(logn) roots,
using exact rational sums and polynomially many bit operations. There
are at most2Lblk such blocks. This total is polynomial in n, with only
polynomial additional classical scratch and no additional quantum
primitive. It is absorbed by14.1, not omitted.
All polynomial terms with exponentm are absorbed by14.1 because
 dl>=d0*sqrt(n) for the fixed positive constant d0: exp(c sqrt n)
dominates every polynomial for c>0, with a finite uniform outer constant.
This is not an expected-cost estimate. Initializing compressed frames
across at most3n batches, including addresses, costs
O(nH²(Dwidth+5)^2 2^H)=O(n^(5/2)2^H), below14.1 since n^(5/2)<=n³ and H<m+dl.
Thus14.1 bounds every actual branch, including previous errors.

## 15. Exact complete envelopes for the capped segmented configuration

For the literal q,t of8 andr<=sqrt n+1,
 m<qr+1,base<d0r+65,m+dl<tr+68<=t sqrt n+70,
 m<=q sqrt n+3,Hlin<=t sqrt n+67.
Section14's actualO(n³2^(m+dl)) work and source/quantum ledgers give
 T=O(n³2^(t sqrt n)),Q=O(n^(3/2)2^(q sqrt n)),S_Q=O(n).
AlsoDwidth>=sqrt(128m)-2>=sqrt(128q)n^(1/4)-2
>(67/5)n^(1/4)-2 because128q=18101888/100000>4489/25.
ConsequentlyH<=t sqrt n-(67/5)n^(1/4)+69 andactualspaceO(n2^H)
is covered by
 S_C=O(2^(t sqrt n-13n^(1/4))),
since the quotient n2^(-(2/5)n^(1/4)) is bounded on positive integers
and tends to zero. This explicitly absorbs the plateau's polynomial
factor using a strict subleading margin. The structured coefficient-13
is literal, not an optimality claim or a growth-index-only comparison.

Relative to actualHYBRID-BLOCKCAP13's n^(10/3) time this improves by
n^(1/3), with the other FOUR full objects identical. Relative to
uncappedSEGMENT-RESET, classical space improves while others retain
the same complete objects. Relative to publishedB64, time improves
n^(1/2) and classical space2^(5n^(1/4)); quantum space,copies,clean
fraction are retained. All are joint same-configuration, every-branch
bounds. The finite n<2^128 exhaustive branch affects only uniform
absolute outer constants, with positive n2 log conventions atn1.
Large constants and cutoff preclude any claim of practical execution.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope

This exact tapered profile has time coefficient close to sqrt(2), with
resource tradeoffs against other algorithms. Constants and the finite cutoff
may be large. No optimum, practical runtime, positive robustness or physical
quantum execution is claimed.
