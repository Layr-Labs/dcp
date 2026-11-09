# SEGMENT-VECTOR-LOGCAP: streaming pairing under a sample budget, T = O(n^3 2^((39999899241/28284200000)sqrt n)), Q = O(n2^((141421/100000)sqrt n)), S_Q = O(n)

## 0. Joint theorem and the exact segmented configuration

For every N>=2 and shift s moduloN putn=ceil(log2N). The SINGLE
SEGMENT-VECTOR-LOGCAP algorithm below on independent ideal coset copies recovers
the entire secret with unconditional probability>=1-2^-8. EVERY branch,
including wrong labels, failed attempts, discarded/rejected acquisitions,
real range projections, support resets and aborts jointly obeys
 T=O(n³2^(t sqrt n)), S_C=O(2^(t sqrt n-n^(1/4)sqrt(log2n))),
 S_Q=O(n), Q=O(n2^(q sqrt n)),
 q=141421/100000,t=39999899241/28284200000.
Growth indices are1/2,1/2,0,1/2. Malformed fraction0 requires independent
ideal copies and asserts neither positive resilience nor impossibility.
Finite n<2^128 uses the separately proved exhaustive branch in13;
resource constants are absolute but may be enormous. At n1 logarithmic
envelopes usepositive n2 values. No practical quantum execution is claimed.

On main n>=2^128 compute exact integers
 r=ceil(sqrt n),m=ceil(qr),u=ceil(log2n),
 d0=100759/28284200000,Cleaf=ceil(u/2)+64,base=ceil(d0r)+Cleaf,dl=base+2,
 Dwidth=floor(sqrt(2Cleaf*m))-1,Hlin=base+m-1,H=Hlin-Dwidth,
 L=floor(m/8),lift(k)=min(2,floor(2k/L)),
 lambda_i=min(base+i+lift(m-1-i),H) for0<=i<m,lambda_m=d,
 Kc=8192(m+10u+100),gw=ceil(log2dl),
 b0=floor((base-Dwidth)/16)-1024u,hstar=b0,g=hstar-6,
 E=8u,noise=ceil(log2(n^5)),Lblk=ceil(n/b0),
 Cf=2^161 dl2^m,A=4Lblk.
Finald=1 for coarse,d=rout=b+noise for each actual data block.
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
the final heightm uses full output2^d with2-bit slack. ALL merges use
nonpower_mergeB for their ACTUAL input lengths. No free power reset,
state preparation or full-power-input assumption is made.

Budgets are allocated root-down in8. Actual delivered guards are
 D_R=2^156 dl2^m(R+u+16), C_R=4D_R.
These huge fixed coefficients are real counters, not omitted constants.
Coarse batches use these delivered/raw guards. Fine VROOT uses the
single raw capCf (also a redundant delivered cap), rebuilding after FAIL.
Jumped coarse stages and full-vector physical signed/twoadic reconstruction
are specified below. All giant coefficients/stage constants are real.
Notation:dn=floor(log2N),N=2^a2 M withM odd,s1=s modM,s2 in[0,2^a2)
withs=s1+M*s2 modN,omega=exp(2pi i/N). All logarithms are base2.
Labels are nonnegative known integers; data basis encodings satisfy0<=u<N.
All roots, ceilings and schedule arithmetic use finite integer comparisons.

## 1. Actual sources and the jump/vector combination

Immediate complete working source is the actual frozen
SEGMENT-VECTOR-JUMP-CAP3443 artifact, FIRST genuine all-five acceptance
477.16 seconds, finalized0.5, registered2dbcafa0-3310-47e3-861b-4f24c66631d8.
Its canonical published files/graph must be verified and its actual ID
formally declared when publication is available before this upload.
It supplies actual physical coarse jumps, full fine-vector interfaces,
Cf2^161 raw fine caps, globalA,128-cycle LOW/cost/HGF proof and ledger.
Its verdict is not a mathematical premise; corrections must propagate.
The actual public earlier segmented/capped source is
f5fcc3b9-02e4-4457-a435-cca24ba517c6 at
db9bd0889bd4258e22bf7d03cb5dfcf00acca93b, all4 source files fetched/cmp,
graph5 provisional references read through nextCursor null. Historical
privateSEGCAP13 is not assigned an invented public identity.

Directly used finite uniform-label Dirichlet characteristic/SMALL-grid
argument is NONPOWER-ROBUST16 4c87713f-685c-42ee-b6f6-55429531212d
at35b4cdf3f8eba3f5a581701283cabf60aa8a64af, robust_decoderF, all4
exact public proof/helper files cmp and graph8 provisional references
inspected. This CLEAN algorithm runs no adaptive low-only verifier,
malformed-state controller, chains or positive-fraction claim. Its new
coarse jump schedule and proof below use that characteristic argument
with genuine physical CRT multipliers, finite grids and measured roots.

The directly used full-vector collision/PGM decoder and signed block
controller are CLEAN-CUBE-LARGE a6faf622-3a45-4b44-9e7c-1985e715d94c
at43e9d037666400fea9820d23c816f5e20fc45faf and NONPOWER-CUBE
c1f61c7d-e987-43fd-8fb3-faf19e7ebdae at
f9df278591782804bdda7cc0406fe3bdbd458e85; exact used public helpers/
proofs and graphs inspected. Its EVERY-secret finite measurement and
compiler arguments are reproduced in qudit_decoder.md, not imported
acceptances. Charged bitprecision accounting retains LARGE16
316d16c3-e6c7-4284-ab8d-05eff620cb4a at
5e378e99f91a59e6588b69a143b17db4938b0477, all3 actual used files
cmp/graph5 inspected. PGM literature is Bacon,Childs,vanDam
quant-ph/0501044v2 Sections4,5,8; constructive synthesis is Dawson,
Nielsen quant-ph/0505030v2 Sections2..4. The latter omits arithmetic
costs; extra certified bitprecision analysis comes from LARGE16.

Actual inherited material from the segmented parent separately retains
TAPER7aaf9754-cafd-43f4-b072-f00b6490c1ce physical/extraction/taper;
BLOCK648a59b2a0-202b-4702-8892-22cc1fc513bb cap/physical transforms
(with historical CS1-C3 cap credit); S58b50e217c-3be6-4b1f-aeca-18948c12887e
weighted deficits; C1 arbitrary-input maps/moments; and HYBRID-TAPER
d1c4694b-448e-4080-992c-1d319008606b LOW/cost coupling ingredients.
All actual source scopes and exact public files/graphs were inspected.
C1 maps operate at EVERY actual merge/reset, not only a late kernel.
No provisional path is certified ancestry, no graph-wide redundancy or
primitive independence is asserted. All actual material is declared.

The parent's coarse jumps and full-vector fine controller are retained,
not claimed new here. The NEW actual leaf allowance is Cleaf=ceil(u/2)+64
rather than a fixed2^22. It grows withlogn and changes every actualbase,
capwidth,support/window and block parameter. All capacity, cycle, field,
root/source/copy and charged plateau/work statements are rederived.
ActualDwidth²=O(sqrt(n)logn), so actual plateau SC isO(nlogn2^H),
not the oldO(n2^H). Initial allocations also carry that logarithm.
New fullT=n³2^(t sqrt n), SC=2^(t sqrt n-n^(1/4)sqrt(log2n)),
with SAME quantum/copy/clean objects as the immediate working parent.
Time/space cross versus that n^(5/2) parent. Versus publicf5 n³/time,
this retains time and improves both full space and copies. No scalar
index record, practical speed, optimum or primitive priority is claimed.

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

IDEAL run. Execute this same SEGMENT-VECTOR-LOGCAP algorithm but replace each LE
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
 Cleaf=ceil(u/2)+64,base=ceil(d0r)+Cleaf,dl=base+2,Hlin=base+m-1,
 Dwidth=floor(sqrt(2Cleaf*m))-1,H=Hlin-Dwidth.
For u>=128,128<=Cleaf=ceil(u/2)+64<=u. Letx=log2r>=64;
u<=2x+1<=r^(1/4), proved at64 with increasing power/log ratio.
Since m<3r/2,
 Dwidth<sqrt(3u r)<2r^(5/8),
 d0r>=16r^(5/8), since d0*2^24>16 andr>=2^64.
These imply Dwidth<m/4 andbase>=4Dwidth+4u+8; for the latter
4Dwidth<8r^(5/8),4u+8<=8r^(5/8). Moreover
2Cleaf*m>=(Cleaf+2)², sinceCleaf<=r^(1/4),m>=r andr>=2^64,
soDwidth>=Cleaf. Exact endpoint/power ratios increase thereafter.
Thus
 base>=65536u+64,base>=256u+1024,base>=32,
 dl<=2base,gw<=u<=base/4,
 hstar=b0=floor((base-Dwidth)/16)-1024u,
 base/32<=hstar<=base/16,g=hstar-6>=d0r/64,
 m+gw+b0<=H,H<=tr+1<=3r/2,(m+1)H<=4n.       (8.4),(8.7)
Compare d0*2^64 to65536*129+64 for thebasebound; its ratio
against2log2r+1 increases. Dwidth<=base/4 gives
hstar>=3base/64-1024u-1>=base/32 andbase-1-Dwidth>=base/2.
Noise<=5u,rout=b+noise<=H,2b<=H-2048u for every actualb<=b0;
ordinarycoarse/datafieldsm+gw+h<=H holdforh<=hstar.
For H useHlin<=tr+Cleaf+1 andDwidth>=Cleaf; this is a real
cancellation, not incorrectly treating2^Cleaf as an outside constant.
The product uses m+1<=3r/2 and
n>=(r-1)^2>=9r²/16. Thus all supported arrays have>=n² rows.

L=floor(m/8)>=4,lift increments0/1 andlift(k)<=k/2. The exact bound
 2(Dwidth+1)<L
holds at the endpoint and increasingly thereafter since m>=r and
Dwidth<2r^(5/8),so4r^(5/8)+2<floor(r/8). Hence lift(k)=0 for0<=k<=Dwidth+1. Capping lowers
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
subtract4 at each nonfinal reset; final maximum is2H-d-2. Each is
positive because lambda_prev>=base+2>4. WriteJ for the reset count,
 A=sum_(k=0)^(L-1)(2-floor(2k/L))<=m/4,
 B0=(m+1)base+m(m-1)/2-d,
 CapLoss=Dwidth(Dwidth+1)/2<=Cleaf*m.
Telescoping actual widths gives exactly
 Sum_i c_i=B0+2m-A-4J-CapLoss.
The actual Cleaf base augmentation and the rational identity give
 B0>=r²+(d0-q/2)r-d+Cleaf(m+1),
 Sum_i c_i>=r²+(d0+5q/4)r-4J-d+Cleaf
             >=n+m-d+64.                       (8.2)
The last usesm<qr+1,J<=127,Cleaf>=64 and
(d0+q/4)r>=4J+2 at the enormousmaincutoff and thereafter.
For coarse d1 this exceedsn. For actual data d=b+noise,
requiredB<=n-b leavesm-noise+64>=0. All maxima are positive
sincerout<=H and all nonrootlambda>=base+2>4.
Root-down allocation realizes exactly the required coarse/dataB bits within these maxima,
all reads belowB. Full-output resets use the arbitrary-input instrument;
no full-power INPUT identity is silently invoked. Internal moment
bounds are conditional on the LOW field, not complete high tables.

Set actual Dcap=2^156 dl2^m(Kc+u+16),Ccap=4Dcap,Y=ceilLog2Ccap.
Kc=8192(m+10u+100)<=2^14m,dl<=H and(m+1)H<=4n imply
 Kc*dl<=2^16n,Ccap<=2^175n2^m,
 Y<=m+u+176<=n/2,Kc/8192>=Y+u+30.             (8.1)
The last usesu>=128 and8u>=106. SetNsmax=ceil((Y+E+20)/g)+1, reserving coarse batches evenifM1.
SinceY<=m+u+176,m<1.5r,u+E+196<r/2,
Nsmax<=ceil(128/d0)+2<2^26<n. This fixed bound follows from
g>=d0r/64; every integer is sized before access.
Cf=2^161dl2^m<=Ccap sinceKc+u+16>=8.
ActualfineA=4Lblk=Theta(sqrt n),Qcap=Nsmax*Ccap+A*Cf.
All fields and confidence
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

### 9.3 Fine VROOT, a full-vector output and its actual cap

VROOT(supplier,B,h,d=rout) uses EXACTLY the same FULLLEAF/LEAF/CORE/
VEC recursion and public cycles asBATCH, with the root output FULL2^d
rather than2 and with windows greedily allocated from8.2. All internal
resets and real same-height projections are unchanged. Before EACH raw
source request, ifCf calls have already been made returnmissing and reset
all work. Use the sameCf as a redundant delivered guard. No source or
postselection is free and no rejected child is reused. The successful
root is the equal-magnitude phase vector on2^d known labels; form known
W_a=hi[a]-hi[0]. Its physical phase is2pi2^B W_a th,up to global phase.
For all actual outcomes |W_a|<=2^h Cf. Actual root fields are at most
h+m+gw<=H andd<=H; the same finite maps/guards apply afterwrongLE.

The final-stage loss bound inhelperE.3 holds for ANY full2^d output
withwindowb<=2H-d-2, not justd1: q(2^d-1)/(AB)<=16/49.
All128-cycle thresholds, LOW/cost coupling and slope products inhelperH
therefore hold with the same constants for these actual data dimensions.
By Jensen on H.2, E D_root<=2^154dl2^m. The accepted-uniform value
is independent of its rejected supplier waiting history (helperF);
waiting mean<=2 per accepted coordinate. Summing fresh requests, with
monotone convergence for positive truncated costs, gives Eraw<=2^155dl2^m.
This permits cost/success correlations and needs no independent ghost
success variable. At rawCf=2^161dl2^m, Markov gives
 Pr(missing | ANY past fixed root parameters)<=1/64.       (9.3)
All incomplete branches are capped; every rebuild requires fresh sources.
The distribution conditional completion preserves all unused high bits,
since every structural choice/cap reads onlyLOW and counters. No future
label-correctness event is used for this reference law.

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

For a completed fine root withh=b,d=rout, ANY two distinct output
indices have a nonzero incidence difference with some coefficient+/-1.
Consequently W_a-W_c is uniform modulo2^b conditionalG, without joint
independence of the entire vector. qudit_decoder.md constructs the actual
finite Clifford+T measurement for the KNOWN labels,oddJ and phasevector
 2^(-rout/2) sum_a exp(2pi i J W_a v/2^b+i eta_a)|a>,
 |eta_a|<=1/(16n^4),rout=b+ceilLog2(n^5).
It recovers EVERYv with error<=2/n^4 averaged over the conditional unused
top bits, including all synthesis error. Completion/caps depend onlyG,
so this bounds wrong AND completion. Direct final twoadic vectors have
the same pairwise-uniform subset law. There is no Kp-vote data decoder.

## 11. Jumped physical coarse estimation and signed odd vectors

IfM1 sets1=0 andskipodd. Otherwiseθ=s1/M. ReserveNsmax coarse batches
as8 evenwhenfewer areused; this is a source CAP, not a promise to acquire
unused copies. Set h=min(hstar,floorLog2M),B=dn-h. B>=a2 andB>=1:
ifh=floorLogM<hstar thena2=dn-h is enormous onmain; otherwiseh<=hstar
=O(sqrt n)<dn. Source acceptsk<2^dn withprobability>1/2 andexactuniform
acceptedinterval[0,2^dn)=[0,2^(B+h)). For stage indexj compute CRT unit
alpha_j=1 mod2^a2, (2^(B-a2))alpha_j=2^j modM. These are units;
Mult_alpha_j,LE,accept interval,X supplies the physical phase
 exp(2pi i2^B W alpha_j s/N)=exp(2pi i2^j W s1/M).
No unknown rotation is synthesized. Each coarse stage runs the actual
Kc-root BATCH with its Dcap/Ccap guards, then fair independentX/Y root
measurements and exact rational scores of4, all temporarywork reset.

Characteristic lemma. ConditionalG and completion,10.1 gives at least
one independentuniformtau in[0,2^h). The finite geometric sum implies
 |E exp(2pi iΔ W)|<=min(1,1/(2*2^h dist(Δ,Z)))           (11.1)
fornonintegralΔ; atintegers use1. All other factors have magnitude<=1,
andtheknowncarry contributes onlyunitphase. Use|sinπΔ|>=2dist(Δ,Z).
This is an actual finite distribution identity, not a continuous oracle.

SMALLodd: floorLogM<hstar. Run ONE stagej0 and score EVERYa/M,
0<=a<M, bysum Z tab_beta((Wa modM)/M). True exact-trig mean1/2;
falsemean<=1/(2sqrt2)<71/200, because2^h<=M<2^(h+1) and
1/[2^h sin(π/2^(h+1))]<=1/sqrt2 for h>=1. The latter follows
sinx/x>=2sqrt2/π on0<x<=π/4. Choose the smallest maximizinga and
returns1=a; noodd finecontroller isrun. All M candidates fit2^(hstar+1).

LARGEodd: h=hstar,g=hstar-6. PutJfull=min{J>=0:2^(J+3)>2M},
Pneed=min(Jfull,Y+E+20),Ns=ceil(Pneed/g)<=Nsmax. Stagek=0..Ns-1
hasj=kg andgridP_j=j+Y+h+8. Initially enumerate everyc/2^P_j in[0,1).
Later enumerate onlythecirculararc ofradius2^-(j+2) aboutpreviouscenter.
All arc endpoints/previouscenters are exactgridpoints. Enumerate increasing
integers inone/two modular intervals, keeping scoremaximum andsmallesttie.
There are atmost2^(Y+h+8) actualcandidates, not2^P_j forlaterstages.
MaintainKc knownresiduesmod2^P_j byaddition at eachc; addresses and exact
rational arithmetic arecharged. Score(c)=sum_i Z_i tab_beta_i((2^jW_i c
mod2^P_j)/2^P_j). Choosecenterz_k atsmallestmaximum.

Inductively afterstagek, circularerror<=2^(-(k+1)g-3) exceptprobability
2^-20/n. For the firststage no arccondition; laterpreviouserror<=2^(-j-3)
putsθ insidethearc ofradius2^(-j-2). Anearestgridpoint hasphaseerror
|2^jWΔ|<=2^(j+Y+h)*2^(-P_j-1)=2^-9, sotrue/nearmean>=
(1/2)cos(π/256)>49/100. For afarpoint atdistance>=2^(-j-g-3),
xx=2^j|Δ| liesin[8/2^h,1/2];11.1 boundscharacteristicby1/16,
sofarmean<=1/32. Thus allfarpoints lose with a fixedlargegap.

For BOTHgrids, conditioned onG, roots have disjointleafsets andindependent
measurementcoins. Scoresliein[-1,1] beforetableerror. Hoeffdingdeviation
1/24 fails withprobability<=2exp(-Kc/1152) percandidate. Tableerror<=1/625
perrecord isexplicit. SMALLgap>=1/2-71/200>2/24+2/625;
LARGEgap>=49/100-1/32 islarger. Sincehstar<=m,Y<=m+u+176,
2^(Y+hstar+9)*exp(-Kc/1152)<=2^-20/n:
Kc/1152=(64/9)(m+10u+100)>7m+70u+700, while
(Y+hstar+9)ln2+(u+20)ln2<2m+2u+205.
This union includesharmfulties. IntegrateG; batchaborts have theirseparate
HGFbounds and first-LEcoupling ischargedseparately. No futurecleanlabel
event conditions thesecore laws. Thus atmostNsmax<=n stages contribute
coarse-scorefailure<=2^-20. Eachacceptedjump gainsg=Theta(sqrt n),
soNsmax is a FIXED enormousconstant, not O(sqrt n).

IfPneed=Jfull, roundMz_last tothenearestinteger moduloM. Error<1/(2M)
givesexacts1,skipfineodd. OtherwiseJfull>Pneed=Y+E+20 implies
M>=2^(Y+E+22). Putchat=round(Mz_last) modM and
 R0=M2^(-Y-E-23)+1/2.
ThenR0>=1,true signedt0 congruents1-chat has|t0|<=R0,
R0/M<=2^(-Y-E-22)<1/2. DefineJtarget=min{J>=0:2^J>=4R0};
2^Jtarget<8R0<=M2^(-Y-E-19), soJtarget<floorLog2M.

Fineodd: setlow0,j0. Whilej<Jtarget chooseb=min(b0,Jtarget-j),
rout=b+noise,B=dn-b>=a2+1. Computegamma=2^(B-a2) modM,
K0=(-2^b)^(-1) modM,J=(2^bK0+1)/M (odd), andCRTunit alpha with
alpha1mod2^a2,gammaalpha=K0*2^(-j) modM. ApplyShift_(chat+low modM),
Mult_alpha,LE,acceptk<2^dn,X. Run ONE Cf-cappedVROOT,h=b,d=rout.
Missingretries onlyunder13globalattemptcap. Oncorrectpast t_j=(t0-low)/2^j
is integral,|t_j|<=R0 bysignedquotientinduction; itsrelativephase is
 exp(2pi iK0W_a t_j/M)=exp(2pi iJ W_a t_j/2^b)
                            *exp(-2pi iW_a t_j/(2^bM)).
This follows by CRT/cancelingtwoadicphase, not synthesizedcorrection.
Since|W_a|<=2^bCf,Cf<=Ccap<=2^Y, perturbation<=2πCfR0/M
<2^(-E-19)<1/(16n^4). Applytheactual10/quditdecoder measurement,
appenditsb-bitresult,low+=a2^j,j+=b. AfterJtargetcorrectbits choose
unique signedrepresentativeoflowmod2^Jtarget in[-R0,R0],elseoutput0;
uniquenessuses2^Jtarget>=4R0. Returns1=(chat+t0) modM. Allwronghistories
stilldefineunits,finiteintervals/guards/dimensionswithoutacorrectnessclaim.

## 12. Sequential twoadic blocks, including direct zero-precision vectors

After s1, write s=s1+M*s2 moduloN. Setj=0,low=0. Whilej<a2 put
wd=a2-j,b=min(b0,wd),rout=b+noise. Shift_(s1+M*low),LE,X yields
uniform k moduloN; kk=k mod2^wd is uniform[0,2^wd) with phase
exp(2pi i kk*remaining/2^wd) on correct past. For B=wd-b>=1 use
ordinary known-label VROOT with h=b,d=rout,raw capCf. Retry missing under13.
Its exact phase is2pi W_a*remaining/2^b and qudit_decoder.md usesJ=1.
For B=0 acquire rout independent DIRECT source phase qubits with uniform
kk modulo2^b. Their product is the equal-amplitude vector on2^rout subset
indices, with known labels their subset sums. A difference of distinct
subsets has a coefficient+1 or-1, so each pair difference is uniform
modulo2^b. Use the SAME finite vector decoder withJ=1. This attempt
completes surely and uses rout<=Cf selected calls; no invalid B=0 tree
or Kp-vote subroutine is requested. It counts as one global attempt.
After completion append a: low+=a2^j,j+=b. Reset ALL work after each
attempt. On correct past the vector has no phase perturbation and each
completed block error<=2/n^4. Correct blocks give low=s2. Return
(s1+M*low) modN. Incorrect prefixes still define the same finite
physical instruments, dimensions and guards, without a correctness claim.

## 13. Actual complete algorithm and unconditional success

Finite branch (n < 2^128). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. This branch acquires at most N(n+10) copies. Its resources are bounded by an absolute constant over this finite range; the exact main-branch cap below is not asserted here.

Mainn>=2^128: compute allparameters/cycles/slotsbeforeaccess,
 Qcap=Nsmax*Ccap+A*Cf,A=4Lblk.
SizeLEconfidencebyQcap. Run11coarse/odd then12twoadic. Eachfineattempt,
includingdirectB0, increments ONEsharedcounter BEFOREaccess; abortbefore
attemptA+1. Everycoarsebatch hasitsDcap/Ccap; fineVROOT hasCf. Resetall
work aftereachattempt/abort. Every rawrejection,failedprojection/merge,
partialconstruction anddiscardedsource iscounted; Q<=Qcap always.
There is no microbank wrapper or positivecorruption claim inthisclean
algorithm. Skippedcoarse/finecomponents do not acquiretheirreservedslots.

Atmost2Lblk desired finecompletions. Eachfreshattempt conditionalpast
completes>=63/64 by9.3; directB0completessurely. ConditionalHoeffding/
iteratedexponentialmoments boundfailuretocomplete byA=4Lblk attempts
byexp(-Lblk/8)<2^-20, sinceLblk=Theta(sqrt n) andmaincutoff.
Correct-pastcompletedPGMblocks haveerror<=2/n4, sounionover<=2Lblk<=n
contributes<2^-20. Coarse-scoreerrors<=2^-20. AtmostNsmax<=n coarse
batchaborts contribute<=2^-16+2^-12 by9.1. ActualLEfirsterror<=2^-10
by5,withoutconditioningtheentirerunoncorrectLE. Totalfailure
 <=2^-16+2^-12+2^-10+3*2^-20<2^-8.
Finitebranch hasitsseparate2^-10 proof. Fullentiresecret isreturned
unconditionally; incorrecthistories stillobeyallfinitebranchcaps.

## 14. All-branch charged resources for actual jumps/vectors

Allguards/scratch arefiniteandfixedbeforeaccess. Geometrygives
m,dl,H,Kc=Theta(sqrt n),Nsmax=O(1),b0=Theta(sqrt n),Lblk=O(sqrt n).
Ccap=O(n2^m),Cf=O(sqrt n2^m),A=O(sqrt n), hence
 Q<=Qcap=O(n2^m).                            (14.0)
Allrawrejected,failed,discardedandpartialcallsarecounted. Atmosttwo
retainedindicesperheight,each<=H,with(m+1)H<=4n; plusallsource/LE,
lookup/arithmeticandactualrout-vector/decoderwires givesSQ=O(n).
NoexponentialcoherentbankorQRAMisallocated. Temporarywiresreset/reuse.

Atreverseheightk, remainingprecisionR_i<=(k+2)H; everyordinarycoarse/
datafieldw_i=R_i+h+i+gw<=(k+3)H usesactualm+gw+h<=H.
Rank/residue/inverse/scratchfieldsareO(H)bitsperrow; fullrootd<=H.
Actualcap/taper boundE_i<=2^H2^(-max(ceil(k/2)-Dwidth,0)) gives
 H2^H sum_(k>=0)(k+4)2^(-max(ceil(k/2)-Dwidth,0))
 <=16(Dwidth+5)^2H2^H=O(n logn2^H).
Plateauandtailareexplicitlychargedasintheactualparentschedule8.
Source/prefix/score/parameterrecordsarepolynomial. Actualdecoder
O(2^(2b)n128)bitsareO(2^H/n1920) since2b<=H-2048u.
No hiddenlargeh2^H physicalfieldortableexists.

LeaftrialcostO(n2^dl); mergeatheighti costsO(n2^(dl+i+1)) andconsumes
2^idl canonicalfreshcoordinatesnotreusedatthatheight. OneO(n²)rank
divisionisabsorbedbyactualinputrows>=n². Eachof<=128realcycle-start
projectionsconsumesitswholefreshsubtreeandcostsO(n2^lambda_a); these
fitthesamelevelcharging. Rawcapsboundallconsumedcoordinates,including
partialleavesandwronghistories. Totalcoretreework
 O(n Qcap 2^dl(m+1)/dl)=O(n²2^(m+dl)),
because(m+1)/dl=O(1). ActualaddressesO(H+logQcap)=O(sqrt n) give
 T_tree=O(n^(5/2)2^(m+dl)).                 (14.1)
InitializationoverO(Nsmax+A)=O(sqrt n) root/framecalls costs
O(sqrt n H²(Dwidth+5)^2 2^H)=O(n²logn2^H), below14.1
since logn<=sqrt n and H<m+dl. The extra growing logarithm is charged.
Everyplateau/siblingbitanditsaddressiscounted, notonlypreloadedtables.

Coarsegridsscanatmost2^(Y+hstar+8) candidatesperstage, withNsmaxO1,
KcO(sqrt n) exactinteger/rationalrecords. j<=Y+E+20=O(sqrt n), all
phase/residueaddressesO(sqrt n). Allscore/table/circuitgenerationand
finitebitoperationscostpoly(n)2^(Y+hstar). SinceY<=m+u+176,
hstar<=base/16 anddl=base+2, thepositive gapdl-hstar>=15base/16
isTheta(sqrt n) withfixedpositivecoefficientd0. ItabsorbsANYfixed
polynomialscorefactorinto14.1. Thereisno2^jhiddenenumerationfactor:
laterarcscontainonlytheexplicitboundednumberofcandidates,eveniftheir
integergridindicesneedO(sqrt n)bits. SMALLgridissmallerstill.

Actualquditmeasurementsincludingtablepreprocessing,knownintegercount
matrices,sparseinverse/forwardscans,controlledprefixpreparations,finite
precisionandbalancedcommutatorsynthesis,classicalarithmetic/circuit
generation,addresses,gatesandcleanupcostO(2^(2b)n128)perattempt.
AcrossO(sqrt n) attempts thisisO(2^H/n1900), absorbedby14.1andthe
actualspacebound. Source/extractionconfidencehaslogQcapO(sqrt n),
sochargedsource/LEworkispoly(n)2^m, absorbedbyexp(dl)'sfixedpositive
sqrtgap. ExactEuclid/CRT,signedupdates,sourcecharges(n+1)Q,routing,
allmeasured/resetwires,guards/parametersandpadding(ifany)countaswell.
AllstatementsareonEVERYbranch,includingwronglabels/prefixes/aborts,
notexpectationsorconditionedruntimes. Nooracles/unknownrotationsarefree.

## 15. Exact growing-allowance envelopes and actual tradeoff

Letl=log2n,u=ceil(l),Cleaf=ceil(u/2)+64. Then
 l/2<=Cleaf<=l/2+66, r<=sqrt n+1,
 m<qr+1,base<d0r+Cleaf+1,
 m+dl<tr+Cleaf+4<=t sqrt n+l/2+72,
 Hlin<=t sqrt n+Cleaf+3<=t sqrt n+l/2+69,
 m<=q sqrt n+3.
The actual14 chargedtreework remainsO(n^(5/2)2^(m+dl)); now
2^Cleaf is NOT a constant butO(n^(1/2)). Hence precisely
 T=O(n³2^(t sqrt n)),Q=O(n2^(q sqrt n)),S_Q=O(n).
The initializationlogfactor isalready charged in14; no n-dependent
allowance or cost has been hidden in an outside constant.

Since2Cleaf*m>=l*q*sqrt n andq>121/100,
 Dwidth>=sqrt(q)n^(1/4)sqrtl-2>(11/10)n^(1/4)sqrtl-2.
Putz=n^(1/4)sqrtl. ThusH<=t sqrt n+l/2+71-(11/10)z.
Actualplateau SC=O(nlogn2^H), withDwidth²=O(sqrt(n)logn),
is covered by
 S_C=O(2^(t sqrt n-n^(1/4)sqrt(log2n))).
Indeed the ratio is bounded by a fixed constant times
n^(3/2)logn2^(-z/10), which tendszero and isbounded over positive
integer n>=2. This follows becausez/logn=n^(1/4)/sqrtlogn tendsinfinity;
the finite remaining sizes havepositiveenvelopes anduniformconstants.
The exact structured second monomial has coefficient-1,nPower1/4,
logPower1/2; outerclassicalpowers are0. No unsupported change to
leadingt or omission of the new plateau logarithm is used.

Versus the immediate working jump parent, time worsensby n^(1/2),
space improvesby2^(-n^(1/4)sqrtlogn+3443n^(1/4)) tendingzero,
with the SAME other THREE fullobjects quantum,copies,clean fraction.
Versus publicf5's n³time/negative3443quarter/Qn1.5 object, time,
quantum andfraction agree,space andcopies strictlyimprove.
This is afull time-space tradeoff, not an index record or a claim
of practical performance/optimality/primitive priority. The growing
square-root-log saving eventually beats every FIXED quartercoefficient.
Maincutoff stays2^128; the finite prefix keeps13's separate all-secret
proof. Its full costs are covered by fixed outside constants, not its
correctness. At n1 logarithmic resource convention usespositive n2.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope

This exact tapered profile has time coefficient close to sqrt(2), with
resource tradeoffs against other algorithms. Constants and the finite cutoff
may be large. No optimum, practical runtime, positive robustness or physical
quantum execution is claimed.
