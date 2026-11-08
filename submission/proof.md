# BLOCK-44: precision-weighted tapered storage at sample index4/9

## 0. Joint theorem and exact algorithm

For every N>=2 and shift s moduloN put n=ceil(log2N). On independent
ideal copies the single BLOCK-44 construction recovers the entire secret
with unconditional probability at least1-2^-8. Every execution branch,
including rejections, failed attempts, discards and aborts, jointly obeys

    F(n)=n^(5/9)+(1/2)n^(4/9)-n^(1/9),
    T=O(n^(31/9)2^F(n)), S_C=O(n^(5/9)2^F(n)),
    S_Q=O(n), Q=O(n^(14/9)2^(n^(4/9))).

Indices are 5/9,5/9,0,4/9; proved malformed fraction0 assumes
independent ideal copies and asserts no positive robustness or impossibility.
All constants are absolute. At n=1 logarithmic envelopes use positive n=2
values. For n<2^48 use the finite exhaustive branch in13, covered only by
outer constants. Otherwise compute exact integers

    m=least positive integer with m^9>=n^4,u=ceil(log2n),
    kappa=ceil(log2m)+1,s0=kappa+1,
    x=n/(m+1)-m/2,base=ceil(x)+1,dl=base+s0,H=base+m-1,
    L=floor(m/(4s0)),lift(k)=min(s0,floor(k*s0/L)),
    lambda_i=base+i+lift(m-1-i) for i<m,lambda_m=1,
    K=Kc=8192(m+10u+100),Kp=8192(u+100),g_w=ceil(log2dl),
    b0=floor(log2n),Lblk=ceil(n/b0).

The root uses integer power comparisons,base exact rational numerator
arithmetic. No real-root or floor-sum oracle is supplied. All parameters
precede acquisitions. Notation:dn=floor(log2N),N=2^a2 M withM odd,
s1=s modM,s2 in[0,2^a2) withs=s1+M*s2 modN,omega=exp(2pi i/N).
Logs are base2 unless noted; labels are known nonnegative integers and
basis states|u> have0<=u<N.

## 1. Provenance and exact change

The direct taper/physical/high-field source is my TAPER-SQRT2,proof SHA-256
c87f33c52f185d247fbbbe86770561e062e4f5ab4ad17a74a5c0f0c829fd2405.
Its public identifier is recorded in the companion declaration once published.
Every needed source/extractor, generic binary/radix/high-part instrument,
conditional moment, guard and full-secret decoder is reproduced.
The direct fractional-depth/profile-analysis source is my CSP-44,
e4bbd09c-946e-4a4b-83c5-3f97b5b618f2. The private TAPER-CUBE draft was a working template,
not a prior submission or certificate. No earlier verdict is a premise.

The actual leaf and width sequence now use the general taper with
base=ceil(n/(m+1)-m/2)+1. The leaf differs by at most two bits from the
old saturated profile, preserving time/copy/quantum envelopes. The peakH
lacks its retry-slack logarithm. A new capacity sum and precision-weighted
memory proof give classical n^(5/9) rather thann with the same exactF,
including its negative term. All dimensions/fields are independently checked.
Earlier credits include BIF-P1024,CSP-40,LQF-NEAR,LQF-D1,LQF-COMP,
LQF-RADIX,LQF-MGF,LQF-SK,QLC-14255,qzv's IFC1310,SPQ-1408,SWFC,
CW1310/CW1,SPC-127,HPC-127,SPC-138,CS1,Kuperberg as credited there.
No invention, optimum, priority, QRAM, coherent bank, extra oracle or
physical quantum execution is claimed.

The additional direct block-decoder method source is our BLOCK64-SQRT2
working proof,exact proof SHA-256
2e0bf017912fda46cb165eaea89ac82b2cf5bd81d7cc9cdf8c88b53b9c69bdb2.
Its eventual public identifier is recorded in the declaration once published.
Only its generalized unused-top-block instrument,uniform-residue scoring
and exact modular odd/two-adic block decoder are used here; its triangular
terminal cap is not used. The actual fractional taper remains as above.
The private preceding taper draft was a working template,not a previous
submission or verdict. New block accounting removes the logarithm from
both work and copies,with the same two workspace envelopes.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates on indexed qubits are classically addressed through this charge; there is no
quantum-addressed memory and no QRAM. A source acquisition costs n+1. Hence

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

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(n^(4/9)) (Section 14),
this is O(n^(22/9)) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL run. Execute this same BLOCK-44 algorithm but replace each LE
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

### 6.2 MERGE(X1, X2; p, b, lam'), for b >= 0

Precondition: X1 and X2 are phase vectors from disjoint sets of qubits, both of length 2^lam,
collimated to p, with index registers x,y. Their stored records are
(cA,hA),(cB,hB), with logical labels al[x]=cA+2^p hA[x],
be[y]=cB+2^p hB[y], 0<=cA,cB<2^p. Put
car=floor((cA+cB)/2^p),aa[x]=hA[x] mod2^b,bb[y]=hB[y] mod2^b.
These are computed directly from the stored fields. Bits p..p+b-1
of the logical sum equal(aa[x]+bb[y]+car) mod2^b. If b=0,
the residue registers are empty and e=0.

1. LOOKUP aa into a fresh b-bit register Ru and bb into Rv. Add Ru + Rv + car (mod 2^b) cleanly into
   a fresh Rz, and clear Ru and Rv by repeating both lookups. Measure Rz, obtaining e, and reset Rz.
2. Classical. Let S_e = {(x,y) : aa[x] + bb[y] + car = e mod 2^b} and sz = |S_e|.
   Use6.1a to sort records(bb[y],y), obtaining order[]; pos[y] is y's sorted position.
   Form t_x=(e-car-aa[x]) mod2^b. Sort records(t_x,x), then merge-join the query
   and data key runs as specified in6.1a. Write each matching run start lo[x] and
   length cnt[x], using insertion start/count0 for an absent class.
   Put off[x]=sum_(x'<x)cnt[x'] in increasing original x order, and
   rank(x,y)=off[x]+pos[y]-lo[x], a bijection from S_e onto[0,sz).
   If sz<2^lam', declare FAIL. Stable data sorting gives precisely the order
   (bb[y],y); therefore all counts and ranks on S_e and the subsequent instrument
   agree with the comparison-sort definition. Empty runs use their insertion start.

3. Let R have 2 lam + 1 bits. LOOKUP pos into Rp and Dx[x] = (off[x] - lo[x]) mod 2^(2lam+1) into Rd.
   Add Rp + Rd (mod 2^(2lam+1)) cleanly into a fresh R, and clear Rp and Rd by repeating the lookups.
   On S_e, R = rank(x,y).
4. Measure bl = floor(R / 2^lam'). If (bl+1) 2^lam' > sz, declare FAIL.
5. Classical. Produce all pairs (x_v,y_v),v=0..2^lam'-1 jointly. Scan original x in increasing
   order with off/cnt while the target rank bl*2^lam'+v increases. Advance past each empty or
   completed x interval once; for its containing interval put y_v=order[lo[x_v]+target-off[x_v]].
   This is one shared scan, not a full scan for each output row. Apply LOOKUP v->(x_v,y_v) on
   the low lam' bits of R, XORing into x,y, which become|0>. Reset R's high bits from known bl.
6. Output R's low lam' bits. Its logical labels are al[x_v]+be[y_v], but store
   only the shared prefix and high parts: for each selected row put
   sv=hA[x_v]+hB[y_v]+car and hi'[v]=floor(sv/2^b), and once put
   c'=((cA+cB) mod2^p)+2^p e. Then 0<=c'<2^(p+b) and

       c'+2^(p+b)hi'[v]=al[x_v]+be[y_v].

   The shared prefix is written once, not once per output row. No full
   logical label array is formed. An input high field of w_i bits needs
   w_i+1 temporary bits for sv and w_(i+1)=w_i+1-b bits for output.

On FAIL, both inputs are reset and released and never reused.

Correctness (ideal run). Before step 1 the state is X1 (x) X2: equal magnitudes over all pairs (x,y),
with phases 2 pi (al[x] + be[y]) th. Steps 1 and 3 compute functions of (x,y) into clean registers and
measure them. So after step 4 the state is the equal-magnitude superposition over the 2^lam' pairs of
block bl, with their original phases. Step 5 maps (x_v, y_v) to v bijectively. The output is a phase
vector with table lab, and every label is congruent to cA + cB + 2^p ((e - car) mod 2^b) modulo
2^(p+b), so it is collimated to p+b.

Lemma 6.1 (distribution-free failure). For ANY input tables collimated to p, the measurement law in
steps 1 and 4 depends only on aa, bb and car (label bits below p+b), and Pr[FAIL] <= 2^(b + lam' - 2 lam).

Proof. Each measurement is a computational-basis measurement of a function of (x,y) on an
equal-magnitude superposition, so its outcome probabilities are ratios of counts, independent of the
phases. Outcome e has probability sz_e / 2^(2lam). Given e, the measured rank is uniform on [0, sz_e).
So FAIL has conditional probability rem_e / sz_e with rem_e = sz_e mod 2^lam' (this also covers
sz_e < 2^lam'). Hence Pr[FAIL] = sum_e rem_e / 2^(2lam) <= 2^b (2^lam' - 1) / 2^(2lam). QED.

Cost. Write E=2^lam,E'=2^lam'. In this configuration
lam=Theta(n^(5/9)),0<=b<=2lam and w_d=lam.
There are at most two stable digit passes. Equation6.1a and the
merge join cost O(E(lam+b))=O(n^(5/9)E) core steps.
The E counters each have lam+1 bits, so the bucket arrays occupy
O(E lam) bits, absorbed by O(nE) since lam=O(n). All explicit quantum lookups have
O(n^(5/9)) gates per row; ranks and the inverse lists use O(n^(5/9))-bit
fields. Each high field is at most3n bits (9). High-part preprocessing and
selected-output arithmetic cost O(n(E+E')) steps; the prefix/carry
update costs O(n) once per merge. No repeated full prefixes are expanded.
Thus total work remains O(n(E+E')) core steps and quantum scratch
O(n^(5/9))<=O(n). The actual classical arrays use their high-field widths
and O(lam+b)-bit indices/keys, counted precisely in14; the coarse
O(n(E+E')) storage upper bound is not used for the final space claim.
Every digit, counter bit, pointer, record copy and table initialization
is included. There is no free word sort or quantum-addressed memory.

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
scratch, and K=O(n^(4/9)) root qubits. Section14 gives its uniform size bound.
A classically addressed free-handle stack or equivalent known recursive
wire layout permits reuse with O(n)-bit bookkeeping per allocation, within
the charged ledger. No exponential register bank is allocated. Classical
tables are looked up by the explicit Section6 scan circuits, not QRAM.

## 8. Exact fractional-root taper and capacity

Let a=n^(4/9),t=n^(5/9),l=log2n in analysis only. Integer root
comparisons givea<=m<a+1. Put x=n/(m+1)-m/2,base=ceil(x)+1,
s0=kappa+1,dl=base+s0,H=base+m-1,L=floor(m/(4s0)).
At n>=2^48,a>=8,a/t<=1/8,kappa<=log2a+3=(4/9)l+3.
Alsoa>=8((4/9)l+4)² at48 and the exponential/polynomial ratio increases,
so m>=8s0²,L>=2s0>0,L<=m-1 ands0<=m-1. We have

    base>=t/(1+2/a)-a+1>=t/2>=s0,
    base>=4,dl<=2base,g_w<=base-1,m+g_w<=H,
    H=ceil(x)+m<=n/(m+1)+m/2+1<=2t,
    m+1<=2a,(m+1)H<=4n.                            (8.4)

All endpoint inequalities have slack at2^48 and improve thereafter.
Thus m=Theta(n^(4/9)),base,dl,H=Theta(n^(5/9)).
Let lift(k)=min(s0,floor(k*s0/L)). It has increments0 or1 andlift(k)<=k/2.
Input widths lambda_i=base+i+lift(m-1-i) grow by0 or1,start atdl,end atH,
and satisfy lambda_i<=H-ceil(k/2),k=m-1-i. Nonroot capacities
2lambda_i-lambda_(i+1)-kappa are at leastbase>0; root2H-1-kappa is positive.
Define B0=(m+1)base+m(m-1)/2-1 and
A=sum_(k=0)^(L-1)(s0-floor(k*s0/L))<=s0L<=m/4.
The uplifts sum to m*s0-A, so exact root/nonroot telescoping gives

    Sum=2lambda_0+sum_(1<=i<m)lambda_i-1-m*kappa
       =B0+m+s0-A.                                (8.2)

Since base>=n/(m+1)-m/2+1,B0>=n andSum>=n+3m/4+s0>=n.
For B<=n allocateb_i root-down under these maxima,settingtp_0=0,
tp_(i+1)=tp_i+b_i,tp_m=B. All residue reads lie belowB and
b_i+lambda_(i+1)-2lambda_i<=-kappa. Binary failure is at most2^-kappa
conditional on ENTIRE built inputs/history,including partial/zero windows.

At l>=48,a>=10u+100,u=ceil(log2n):2^((4/9)l)>=10l+110 holds at48
and its ratio increases. Therefore Kc=8192(m+10u+100)<=2^14m,
Kc*dl<=2^16n bydl<=H and8.4. WithDcap=8dl2^m(Kc+u+16),Ccap=4Dcap,
Y=ceil(log2Ccap),all computed before access,

    Ccap<=64Kc dl2^m<=2^22n2^m,
    Y<=m+u+23<=n/2,
    Kc/8192=m+10u+100>=Y+u+30.                       (8.1)

Usem<=2a<=n/4 andu+23<=n/4 at48 and thereafter forY<=n/2.
No field/concentration parameter is defined circularly.

For block fields also use b0=floor(log2n),Lblk=ceil(n/b0).
Herebase>=4u andbase>=32 atn=2^48 and thereafter:base>=t/2 and
t/2 grows exponentially faster than4u. Since dl<=2base,
g_w<=ceil(log2(2base))<=base/4 andb0<=u<=base/4.
Thus m+g_w+b0<=m+base/2<=H,as required for theh-unused-bit fields.

## 9. BATCH(supplier, B, R, h=1)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+h)). Here1<=h<=b0 and1<=B,B+h<=n. Output: R roots, or ABORT. Here 1<=R<=Kc is a requested root count. Compute D_R=8dl2^m(R+u+16), C_R=4D_R before access. A batch starts with a zeroed counter of
source acquisitions; if an acquisition would exceed C_R, the batch ABORTs. Also initialize delivered counter D=0. Before acquisition compute D_src=B+h, the budget tp_i and all w_i. At its end, unused tree/index scratch and high-part tables are reset or released; the next batch reuses the frame pool.

Each frame allocates its actual2^lambda_i rows and actual output length,
not2^H rows at every level. Changing the index widths does not change the
canonical source footprint: a level-i logical label is still the sum of at
mostdl2^i accepted source labels. Therefore the exact high-part field and
carry formulas below apply with these actual row counts as well.

TREE. VEC(0) = LEAF: for each of dl wires, first check D<D_R; otherwise ABORT before calling NEXT. Request the next accepted qubit by NEXT(0), then increment D. Thus D never exceeds D_R. These qubits form
the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j.
At p=0 write only this hi table, of width w_0=D_src+g_w per row; c=0. The logical
table has length 2^dl, is exactly the tensor product state in the ideal run, and is collimated to tp_0=0.
VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until out != FAIL; return out. A root is VEC(m),
evaluated depth-first. Run it R times.

Field widths. Put D_src=B+h and g_w=ceil(log2dl). A level-i logical
label is a sum of at most dl2^i source labels below2^D_src, by disjoint
canonical footprints. It is below2^(D_src+i+g_w). Thus store its high parts
in exactly

    w_i=D_src+i+g_w-tp_i >=1

bits per row, and one tp_i-bit common prefix. These dimensions are fixed
before acquisitions. At a merge w_(i+1)=w_i+1-b_i, so the w_i+1-bit
sum sv fits and its right shift fits the output field without truncation.
The same integer bound holds on actual wrong-label branches: accepted
stored source values still lie in[0,2^D_src), and the logical sum invariant
is maintained exactly. No high-value overflow check or abort is needed.

Root. At p=B the stored pair is(c,hi[0],hi[1]). Compute

    W=hi[1]-hi[0]=(lab[1]-lab[0])/2^B.

The common prefix cancels; no full labels need reconstruction. Its ideal
state is, up to global phase,

    (|0>+exp(2 pi i 2^B W th)|1>)/sqrt2.                (9.1)

The earlier global bound remains true for logical values: each is a sum
of at most C_R source labels below2^(B+h), hence is below2^(Y+n+1).
Only the high fields and one prefix are stored. Since
2^(m+g_w)<2dl2^m<=C_R, we have m+g_w<=Y. Thus
w_i<=D_src+m+g_w<=n+Y<=3n on the main range. In particular

    |W|<=2^h C_R<=2^h Ccap<=2^(Y+h),                              (9.2)

Coarse decoding usesh=1; block decoding usesh=b. No root-cost bound depends onh.

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a
batch ABORTs with probability at most 2^-12/n + 2^-11/n.

Proof. Work in the ideal run and put p=2^-kappa<=1/(2m),
so p<=1/10 on the main range. Lemma6.1 bounds the failure probability
of every merge by p CONDITIONAL ON ITS ENTIRE BUILT INPUTS AND HISTORY.
This property is stronger than an unconditional small failure rate.

Analytical domination. After each pair of child constructions, let q<=p
be the actual conditional failure probability of that attempt. Its outcome
can be represented in the probability analysis using a fresh independent
uniform U: failure iff U<=q, with additional independent randomness
choosing the particular outcome conditional on failure/success. The event
U<=p dominates actual failure and is independent of the just-built child
costs. This is an analytical coupling, not an extra computational oracle
or a change of the quantum circuit. If the actual attempt succeeds while
U<=p, add ghost attempts in the upper process. Use independent coins at
all potential call-tree nodes. Induction on height then dominates actual
delivered demand by the following independent upper process:

    Z_0=dl,
    Z_i=sum_(j=1)^G (Z_(i-1,j,1)+Z_(i-1,j,2)),
    Pr(G=g)=(1-p)p^(g-1),g>=1,

where all child Z copies and each G are independent. The parent coin is
fresh after child construction; no independence of actual cost and actual
failure is asserted. Since U>p forces actual success, the actual number of parent attempts
is at most the first index with U>p. That index uses only parent coins
and is independent of every upper child cost. This domination is uniform conditional on all history
before the root call. Fixed depth and finite geometric G also establish
almost-sure finiteness of the uncapped process used only for this analysis.

Exponential moment. Define M_i(s)=E exp(s Z_i/(2^i dl)) and
y_i(s)=ln M_i(s). For0<=s<=1/8, y_0(s)=s. Put
c_i=(1+2p)^i<=exp(2*p*i)<=e<3 for i<=m. With
a=2y_(i-1)(s/2), the geometric sum gives

    y_i(s)=f_p(a),
    f_p(a)=a+ln(1-p)-ln(1-p exp(a)).

Inductively a<=c_(i-1)s<=3/8<1/2. On0<=a<=1/2,
exp(a)<5/3 and p<=1/10 imply

    f'_p(a)=1/(1-p exp(a))<=1/(1-5p/3)<=1+2p.

The last inequality follows from p/3-10p²/3>=0. Since f_p(0)=0,
y_i(s)<=c_i s. Denominators are positive throughout, so every moment
used exists. In particular an actual root has, conditional on its prior
history, E exp(D_root/(8*2^m dl))<=exp(3/8).
For R roots the tower property therefore gives

    E exp(D_inf/(8*2^m dl))<=exp(3R/8).

Independence of actual root costs is unnecessary. Markov applied to this
exponential moment, with the stated D_R, yields

    Pr(D_inf>D_R)<=exp(-5R/8-u-16)
                    <=2^(-u-16)<=2^-16/n.             (9.3)

Acquisitions. In the ideal supplier each potential acquisition produces
an accepted qubit with conditional probability at least1/2. Extend its
potential acceptance indicators after any stopping time as needed for the
analysis. If A is their sum over C_R=4D_R acquisitions, iterated
conditional expectation gives E[3^-A]<=(2/3)^C_R. A source-cap abort
before demand abort/completion entails A<=D_R. Hence

    Pr(source-cap abort before demand abort)
       <=3^D_R(2/3)^(4D_R)=(16/27)^D_R
       <=2^(-D_R/2)<=2^(-u-12)<=2^-12/n.             (9.4)

Here(16/27)^2<1/2 and D_R>=2(u+12). The actual capped run agrees
with the uncapped process until a cap triggers. Equations9.3/9.4 are
stronger than the lemma's stated2^-12/n+2^-11/n bound. These are
probability estimates for success only; every actual branch, including
wrong-label branches, obeys the deterministic caps directly. QED.

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

Every residue,sort,rank and block partition inspects only logical positions
belowB. Bits belowB of a sum depend only onlow_v. Stored prefixes and
exposed residue windows end belowB. Lemma6.1 makes the conditional law
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
z_(j-1), so |Delta| <= 2^-(j+1). So xx = 2^j |Delta| is in [1/8, 1/2]. By Lemma 10.1 and (10.2) with phi = 2^j Delta,

    E[xi_i | G] = (1/2) Re E[exp(2 pi i 2^j Delta W_i) | G] <= (1/2) cos(pi xx) <= (1/2) cos(pi/8).

Concentration. By Hoeffding each fixed candidate's sum deviates from its conditional mean by at least K/64 with probability
at most exp(-K/8192). Outside these events,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625 > (K/2) cos(pi/8) + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the maximizer is not far. There are at most 2^(Y+8)
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(m+10u+100) <= 2^-(Y+u+30), using8.1a. The failure
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

Finite branch (n < 2^48). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. This branch acquires at most N(n+10) copies. Its resources are bounded by an absolute constant over this finite range; the exact main-branch cap below is not asserted here.

Main branch (n >= 2^48). Compute a2,M,dn,J_full,Kc,Kp,the
schedule,Dcap,Ccap,Y before access, where Dcap,Ccap denote the Kc caps
from8. For a batch with R roots use D_R,C_R as in9. Put

    Cp=32dl2^m(Kp+u+16),
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

Every counter,array and retry is capped. Withl=log2n,
m,Kc,Y+6=Theta(n^(4/9)),dl,H=Theta(n^(5/9)),Kp=Theta(l),
Ccap=O(n2^m),Cf=O(n^(5/9)l2^m). Coarse batches acquire
O(n^(13/9)2^m) copies and all fine/two-adic blocks acquire
O(n^(14/9)2^m),which dominates since4/9<1/2. Thus

    Q<=Qcap=O(n^(14/9)2^m).                       (14.0)

There are at mostLblk=O(n/log2n) fine blocks per part;
each still usesKp=Theta(log2n) roots. Hence the displayed aggregate
copy bound has no logarithm,while its per-batch Cf retains one.

The sum of delivered-demand caps has the same envelope,including every
rejection,failure,discard and abort. Two retained indices per level,each<=H,
useO(n) qubits by(m+1)H<=4n. Leaf,source/data,modular/LE,lookup/controller
scratch andKc roots addO(n); wires are reused. HenceS_Q=O(n),with no QRAM.

Classical space. Put k=m-1-i. Remaining precision satisfies
R_i=B-tp_i<= (m-i+1)H=(k+2)H since each nonroot capacity is belowH
and the root below2H. Thus actual high fields obey
w_i=R_i+h+i+g_w<=(k+3)H, usingm+g_w+b0<=H. Radix buckets, records,
ranks/orders and inverse maps need O(H) bits per row. Output length
is at most2E_i with field at mostw_i+1. Equation8.5 gives

    E_i=2^lambda_i<=2^H*2^(-ceil(k/2)).

Every retained sibling, field, output and scratch frame is bounded by a
constant times

    H2^H sum_(k>=0)(k+4)2^(-ceil(k/2))=19H2^H.

The sum follows by pairing k=2j-1,2j and using sum2^-j=1,
sumj2^-j=2 for j>=1. No n-dependent plateau is hidden in a constant.
Prefixes, small roots, source/LE, controller, decoder and parameter records
add polynomial space absorbed by H2^H. Hence S_C=O(H2^H), without
any storage or lookup oracle.

Work. A leaf costsO(n2^dl) core and consumesdl delivered qubits.
At heighti a merge attempt consumes2^(i+1)dl disjoint canonical qubits not
reused by another attempt there,and costsO(n2^(dl+i+1)),since lambda_i<=dl+i.
A partial leaf at abort is charged fully. All levels cost
O(nD_R2^dl(m+1)/dl) per batch,where(m+1)/dl=O(n^(-1/9)).
Using14.0 givesO(n^(22/9)2^(m+dl)) core tree work. Address width
O(H+logn)=O(n^(5/9)) yields

    T_tree=O(n³2^(m+dl)).                          (14.1)

LogQcap=O(n^(4/9)),so source/extraction usesO(n^(22/9)) core per copy,
orO(n^(41/9)2^m) total with addresses. Coarse scoring acrossO(m) stages
costsO(Kc*n*2^Y*m)=O(n^(26/9)2^m) core. Fine votes,parity,signed/CRT
updates,source charges(n+1)Q,gates,resets and parameters are also charged.
Every polynomial term with exponentm is absorbed by14.1 because dl=Theta(n^(5/9)).
Initializing all compressed frames over3n batches,with addresses,costs
O(nH²2^H)=O(n^(19/9)2^H),below14.1. Every branch,even after earlier
errors,is bounded; each loop is fixed or consumes a capped qubit.

## 15. Exact uniform envelopes

Put F(n)=n^(5/9)+(1/2)n^(4/9)-n^(1/9),a=n^(4/9),t=n^(5/9),l=log2n.
Since m+1>=a+1 and1/(1+x)<=1-x+x² forx>=0,

    n/(m+1)<=t-n^(1/9)+n^(-1/3)<=t-n^(1/9)+1,
    H<=n/(m+1)+m/2+1<=F(n)+3,
    m+dl=H+kappa+2<=F(n)+(4/9)l+8, m<=a+1.

The remainder power-1/3 is nonpositive. Substitute into14 withH<=2t.
All ceiling and slack factors are explicit in the complete joint envelopes

    T=O(n^(31/9)2^F(n)), S_C=O(n^(5/9)2^F(n)),
    S_Q=O(n), Q=O(n^(14/9)2^(n^(4/9))).

Time/classical indices are5/9,copy index4/9,quantum0. The exact negative
term is retained. Finite n<2^48 exhaustive inputs change only uniform outer
constants,never main-only guards. At n=1 logarithmic envelopes usepositive n=2 values.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope

This is a lower-copy/time/classical-space tradeoff with linear quantum
workspace,not a better time index than1/2. Constants and the finite cutoff
can be large. No optimum,practical runtime,positive robustness or physical
quantum execution is claimed.
