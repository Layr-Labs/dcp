# HYBRID-TAPER23: streaming pairing under a sample budget, T = O(n^(10/3)log2(n)2^((39999899241/28284200000)sqrt n)), Q = O(n^(3/2)log2(n)2^((141421/100000)sqrt n)), S_Q = O(n)

## 0. Joint theorem and exact algorithm

For every integer N>=2 and s moduloN put n=ceil(log2N). The single
HYBRID-TAPER23 construction below, on independent ideal coset copies, recovers
the entire secret with unconditional probability at least1-2^-8. Every
execution branch, including all rejections, failures, discards and aborts,
jointly obeys

    T=O(n^(10/3)log2(n)2^((39999899241/28284200000)sqrt n)),
    S_C=O(sqrt(n)2^((39999899241/28284200000)sqrt n)), S_Q=O(n),
    Q=O(n^(3/2)log2(n)2^((141421/100000)sqrt n)).

All constants are absolute. At n=1 logarithmic resource envelopes use
their positive values at n=2. The indices are1/2,1/2,0,1/2 and proved
malformed fraction is0 under independent ideal copies. No positive
robustness or impossibility is claimed. On n<2^48 use the finite exhaustive
branch in13, covered only through outer constants. Otherwise compute

    r=ceil(sqrt n),q=141421/100000,m=ceil(q*r),u=ceil(log2n),
    kappa=ceil(log2m)+1,
    base=ceil((100759/28284200000)r),s0=ceil(2kappa/3)+2,
    dl=base+s0,H=base+m-1,L=floor(m/(4s0)),
    h0=ceil(2m/3)+24u,v=m-h0,sigma=ceil(log2v)+2,
    K=Kc=8192(m+10u+100),Kp=8192(u+100),g_w=ceil(log2dl).

The rational ceiling uses numerator arithmetic, r uses integer square root;
no irrational, fractional-power or logarithm oracle is supplied. Binary
input widths are lambda_i=base+i+lift(m-1-i) for i<m,
where lift(k)=min(s0,floor(k*s0/L)), and root widthlambda_m=1.
Early levels1..h0 use the power merge; at h0 actually measure the
index range for M0, and retry the whole early subtree on false. Late
local j=0..v-1 has EXACT support M_j=(1-delta_j)2^lambda_(h0+j),
 delta_j=(j+1)2^(j-v-sigma). The final root remains full2 on1qubit.
Root-down budgets, exact high-part storage, counted radix joins, variable
root guards and the complete signed near-parity decoder are given below.
Notation: dn=floor(log2N),N=2^a2 M with M odd,s1=s modM,
s2 in[0,2^a2) with s=s1+M*s2 modN,omega=exp(2pi i/N),
and all logs are base2 unless noted.
A label is a known nonnegative integer; data basis states are |u>,0<=u<N.

## 1. Actual material sources and the hybrid contribution

The immediate working template is the complete private HYBRID-TAPER
artifact undergoing its FIRST protected review at construction. It
supplies the explicit mixed power/non-power instrument, deferred accepted
bits/LOW ghost coupling, MGF multiplier16 and factor128 batch guards,
all reproduced below. If registered before this derivative is uploaded,
verify its actual canonical files/graph and formally declare its actual
ID. Corrections must propagate; no private verdict is a premise.
The present refinement changes the switch toceil(2m/3)+24u and uplift
toceil(2kappa/3)+2, proving all capacity/margin/envelope conditions again.

Immediate full staged-bootstrap/bit-decoder source is published TAPER-SQRT2,
7aaf9754-cafd-43f4-b072-f00b6490c1ce at
fa84a323b64e99a5e6e7f13c6f363fe22dce44ab. Its exact full proof was
fetched and byte-compared (SHA256c87f33c52f185d247fbbbe86770561e062e4f5ab4ad17a74a5c0f0c829fd2405),
all sections read, and BOTH current provisional incoming declarations
read through nextCursor:null. It supplies the complete physical source,
extractor, early full-power radix instrument, staged coarse estimator,
signed near-parity/two-adic bit decoders, field/taper accounting and
near-sqrt2 rational q/d0/t geometry, reproduced in full.
Its historical actual CSP40/BIFP1024 physical/high-field/allocation
credits and prior Kuperberg/CS1-derived methods remain retained. Pending
references are not certified ancestry and no prior verdict is a premise.

Actual late non-power instrument/conditional binary-incidence source is
NONPOWER-CUBE c1f61c7d-e987-43fd-8fb3-faf19e7ebdae at
f9df278591782804bdda7cc0406fe3bdbd458e85. ALL FOUR exact public files,
including nonpower_merge.md, were fetched/cmp verified, and its three
provisional incoming declarations read through nextCursor:null.
Only the explicit selected-interval instrument, binary moment law and
unused-bit method are used here, not its cube geometry, wide coarse
controller or vector PGM. Linearly weighted dyadic deficits come from
the actual frozen private NONPOWER-S58 artifact, undergoing its first
genuine review at construction. Its actual canonical files/graph must
be verified and formally declared if registered before this derivative.
All necessary arguments are included in nonpower_merge.md. Corrections
must propagate; no private/public acceptance is a mathematical premise.

The HYBRID combination is retained from the immediate private template: first h0=ceil(2m/3)+24u levels
use full powers and kappa margins; a REAL range projection starts late
non-power collimation, ending in the same full two-entry root. Reduced
upliftceil(2kappa/3)+2 preserves capacity and the same H, but reduces
2^dl by m^(1/3) compared with the old uplift. The crucial new proof
is a LOW-sigma-field ghost coupling and uniform exponential-moment
bound, replacing the old batch tail lemma rather than confusing a mean
with an exponentially small abort probability. This refinement uses factor8 caps relative to the original TAPER
(16 times smaller than the private hybrid template), with every changed
tail constant and global error budget explicitly rederived.

No one-wide-coarse-batch or large-vector decoder is run: their grid/cost
would not fit this near-sqrt2 time envelope. All operations below use
ordinary finite circuits; no QRAM, source purification, new oracle,
physical quantum runtime, primitive priority or optimality is asserted.

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

IDEAL run. Execute this same HYBRID-TAPER23 algorithm but replace each LE
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
lam=Theta(sqrt(n)),0<=b<=2lam and w_d=lam.
There are at most two stable digit passes. Equation6.1a and the
merge join cost O(E(lam+b))=O(sqrt(n)E) core steps.
The E counters each have lam+1 bits, so the bucket arrays occupy
O(E lam) bits, absorbed by O(nE) since lam=O(n). All explicit quantum lookups have
O(sqrt(n)) gates per row; ranks and the inverse lists use O(sqrt(n))-bit
fields. Each high field is at most3n bits (9). High-part preprocessing and
selected-output arithmetic cost O(n(E+E')) steps; the prefix/carry
update costs O(n) once per merge. No repeated full prefixes are expanded.
Thus total work remains O(n(E+E')) core steps and quantum scratch
O(sqrt(n))<=O(n). The actual classical arrays use their high-field widths
and O(lam+b)-bit indices/keys, counted precisely in14; the coarse
O(n(E+E')) storage upper bound is not used for the final space claim.
Every digit, counter bit, pointer, record copy and table initialization
is included. There is no free word sort or quantum-addressed memory.

The EARLY full-power instrument6.2 is unchanged. LATE levels instead
run the arbitrary-integer-output MERGE fully specified in included
nonpower_merge.md B/C, with exact M_j and final2. Its A/D/E/G/H/I
prove transition support, conditional moments, HIGH-bit preservation,
cost-measurable coupling and new batch tails. These are part of this
same algorithm, not a call to an unprovided oracle or prior theorem.

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

## 8. Exact hybrid tapered staircase, capacity and late-stage margins

Set q=141421/100000,d0=100759/28284200000,
t=1/q+q/2=39999899241/28284200000. Compute
 r=ceil(sqrt n),m=ceil(qr),kappa=ceilLog2(m)+1,
 base=ceil(d0*r),s0=ceil(2kappa/3)+2,dl=base+s0,H=base+m-1,
 L=floor(m/(4s0)),lift(k)=min(s0,floor(ks0/L)),
 lambda_i=base+i+lift(m-1-i),0<=i<m,lambda_m=1,
 h0=ceil(2m/3)+24u,v=m-h0,sigma=ceilLog2(v)+2.
Everything uses finite integers/rationals, including integer square root
and bit_length. For n>=2^48,qr<=m<qr+1,kappa<=log2r+3 and
s0<=kappa+1<=log2r+4 (kappa>=8 here). Thus the old endpoint
inequalities r>=8(log2r+4)^2 and d0*r>=log2r+4 hold at2^24 and
increasingly thereafter. They imply
 m>=8s0²,L>=2s0,L<=m-1,base>=kappa+1>=s0,
 dl<=2base,gw=ceilLog2dl<=base-1,m+gw<=H,
 H<=t*r+1<=3r/2,m+1<=3r/2,(m+1)H<=4n.          (8.4)
The last follows r>=4,n>=(r-1)^2>=9r²/16. In particular
m,dl,H=Theta(sqrt n), with fixed positive d0, and all guards precede
access. Lift increments0/1, equals s0 at k=m-1 and0 at k0, and
lift(k)<=k/2. Hence consecutive lambda_i grow0/1,
 lambda_0=dl,lambda_(m-1)=H,
 lambda_i<=dl+i,lambda_i<=H-ceil(k/2),k=m-1-i.   (8.5)

For merge i=1..h0 use window maximum
 2lambda_(i-1)-lambda_i-kappa;
for h0<i<m use maximum2lambda_(i-1)-lambda_i;
for the final root use maximum2H-1-2. All are positive: earlymaximum
>=dl-1-kappa>=s0, late>=lambda_prev-1, and H>2.
Put A=sum_(k=0)^(L-1)(s0-floor(ks0/L))<=s0L<=m/4 and
B0=(m+1)base+m(m-1)/2-1. Exact telescoping gives
 Sum=B0+m*s0+s0-A-kappa*h0-2.
Since s0>=2kappa/3+2 and h0<=2m/3+1+24u,
 Sum>=B0+7m/4-kappa(24u+1)+s0-2.
The identity q*d0+q²/2=1 and base>=d0r,m>=qr imply
 B0>=r²+(d0-q/2)r-1,
 Sum>=r²+(d0+5q/4)r+s0-kappa(24u+1)-3>=r²>=n.   (8.2)
For the penultimate inequality write x=log2r>=24. We have
kappa<=x+3,u<=2x+1 and d0+5q/4>1. At x24,
2^x>=(x+3)(48x+25)+3, and the ratio of2^x to this positive quadratic
increases: ln2-1/(x+3)-48/(48x+25)>0. Thus
r>=kappa(24u+1)+3 throughout the main range, proving the inequality.
Allocate exactlyB<=n bits root-down within the positive maxima, so all
reads end belowB.
No full-high-table small-failure bound is asserted for late levels.

For j0..v-1 define the late support
 delta_j=(j+1)2^(j-v-sigma),
 M_j=2^lambda_(h0+j)-(j+1)2^(lambda_(h0+j)+j-v-sigma).
The final root is full2. Here v>=128,2^sigma>=4v,delta_j<=1/8.
Let W=lambda_h0. Endpoint/monotonicity with m>=r,u<=2log2r+1
gives m>=288u+12 on the main range. Hence
 h0=ceil(2m/3)+24u<=3m/4<m,v>=m/4>=128.
Also sigma<=u+2 and
 W-2v>=base+3h0-2m>=base+72u>=2sigma+64u.
The last uses72u>=66u+4 foru>=1. Therefore
 W>=2v+2sigma+64u,                               (8.6)
so every M_j is an EXACT positive integer and at least7/8 its padded
length. The projected transition and late conditional moment/coupling/
MGF lemmas are fully proved in nonpower_merge.md. Late input widths
are>=W>=2u+1, hence their supported input arrays have>=n² rows, absorbing the
ONE O(n²) division/multiplication cost per coherent late merge. This
array bound is NOT asserted for early leaves with tiny positive base;
early power merges use6.2 and no arbitrary division.

Kc=8192(m+10u+100)<=2^14m, Kc*dl<=2^16n, and Kp=8192(u+100).
Set Dcap=64dl2^m(Kc+u+16),Ccap=4Dcap,Y=ceilLog2Ccap.
Then Ccap<=512Kc dl2^m<=2^25n2^m, hence
 Y<=m+u+26<=n/2,
 Kc/8192=m+10u+100>=Y+u+30.                    (8.1)
The first uses m<=3r/2<=n/4,u+26<=n/4 at the endpoint and later.
The second uses10u+100>=2u+56. This recomputes the changed frequency
and concentration fields without circularity. Factor8 changed caps
are actual finite guards, not a success-only analysis adjustment.

## 9. BATCH(supplier, B, R)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+1)). Output: R roots, or ABORT. Here 1<=R<=Kc is a requested root count. Compute D_R=64dl2^m(R+u+16), C_R=4D_R before access. A batch starts with a zeroed counter of
source acquisitions; if an acquisition would exceed C_R, the batch ABORTs. Also initialize delivered counter D=0. Before acquisition compute D_src=B+1, the budget tp_i and all w_i. At its end, unused tree/index scratch and high-part tables are reset or released; the next batch reuses the frame pool.

Each frame allocates its actual2^lambda_i rows and actual output length,
not2^H rows at every level. Tapering the index widths does not change the
canonical source footprint: a level-i logical label is still the sum of at
mostdl2^i accepted source labels. Therefore the exact high-part field and
carry formulas below apply with these actual row counts as well.

TREE. EARLY(0)=LEAF acquires dl accepted phase qubits by NEXT(0).
Before each NEXT call check D<D_R, otherwise ABORT; increment D on
delivery. The initial full tensor table uses source entries(0,k), exact
absolute subset sums, prefix0 and public widthD_src+gw. EARLY(i),
1<=i<=h0, repeatedly builds TWO fresh EARLY(i-1) inputs and applies
power MERGE6.2 at its assigned window, output2^lambda_i; FAIL resets
both and retries. Every source/counter guard applies inside recursion.

START repeatedly builds a fresh complete EARLY(h0), computes the
predicate index<M_0, measures it and clears comparator scratch. False
resets/releases the WHOLE built index/table and repeats fresh. True
retains the equal-magnitude phase vector on the first M_0 indices and
its ABSOLUTE high table/common prefix; padded indices have zero ideal
amplitude. This is a real counted range measurement, not free non-power
preparation. Its exact retention1-delta_0 is label/phase independent.

VEC(h0)=START. For h0<i<m, repeatedly build two fresh VEC(i-1)
inputs and run nonpower_mergeB with outputM_(i-h0), precision tp_(i-1)
and assigned window. Final VEC(m) similarly has output EXACT2. FAIL
resets both children before fresh retries. The stored fields/carries
below are unchanged; all rank/division/inverse maps are explicitly
finite on the whole padded space. Run VEC(m) R times, retaining only
its one-qubit root and knownW until BATCH returns. No root measurement
feeds the batch schedule. R<=Kc=O(sqrt n) retained roots count in14.

Field widths. Put D_src=B+1 and g_w=ceil(log2dl). A level-i logical
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
of at most C_R source labels below2^(B+1), hence is below2^(Y+n+1).
Only the high fields and one prefix are stored. Since
2^(m+g_w)<2dl2^m<=C_R, we have m+g_w<=Y. Thus
w_i<=D_src+m+g_w<=n+1+Y<=3n on the main range. In particular

    |W|<=2C_R<=2Ccap<=2^(Y+1),                              (9.2)

as required by both decoder phases.

Lemma9.1 (NEW hybrid no-abort law). In the ideal-label reference
process each batch aborts with probability at most(2^-16+2^-12)/n.

Proof. Included nonpower_mergeG constructs the LOW-sigma-field
geometric upper coupling, accounting for early power levels, the real
transition projection, late non-power moments and the final root. Its
H proves Eexp(D_root/(64dl2^m))<=exp(1/4), uniformly given any
history before this root, using Kproduct<16. Its I combines the R-root
tower bound with ACTUAL D_R64dl2^m(R+u+16), C_R4D_R, giving
 Pr(delivered-demand abort)<2^-16/n,
 Pr(source abort before delivered-demand abort)<=2^-12/n.   (9.3),(9.4)
The coarse field includes built child COSTS but excludes the current
unused label window. This is not a claim of small failure conditional on
full high tables, nor an assumption of cost/success independence. All
coupling variables are analytical and are never gates/source oracles.
All proofs and finite instruments are reproduced in the helper. Earlier
batch MGFs are not imported as a theorem. Actual branches obey the hard
caps even after incorrect labels; actual success is compared until the
first LE error by5.1, not conditioned on a future clean-label event.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all merge outcomes (e, bl); and all decisions of the controller in
that batch (FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no selection decision. It excludes full saved labels and any records exposing accepted leaves' top bits. Source rejection history is independent of the accepted values: for iid uniform labels, every fixed preceding rejected-value sequence has the same probability followed by each value in the accepted power-of-two interval. Thus the accepted values remain uniform and independent of that history. Direct modular suppliers already give uniform labels. G is a coarse sigma-field, not the full physical computer record.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits belowB of a sum of leaf labels depend only on the low_j, since multiples of2^B do not change them.
The stored prefix contains only bits below tp_i and a b_i-bit
residue of hi exposes exactly logical positions tp_i..tp_i+b_i-1,
all belowB. Compression therefore does not expose a new top bit.
By Lemma6.1 for early powers and nonpower_mergeB.1 for late
merges, each outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low).
The transition index predicate is label independent, and the new complete
rank blocks and caps also inspect only low labels. Thus they preserve
the same factorization, including aborted histories. QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs on disjoint
coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

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

Fine stages j=0,...,n-1. Initialize low=0. At stage j let
cj=(chat+low) mod M, K0=(M-1)/2 and gamma=2^(dn-1-a2) mod M.
Compute by extended Euclid and CRT a unit alpha_j modulo N such that

    alpha_j=1 mod2^a2,
    gamma alpha_j=K0 2^(-j) mod M.

These inverses exist: M is odd and gcd(K0,M)=1. Apply Shift_cj
and then Mult_alpha_j to each fresh copy, run LE, accept k<2^dn,
and apply X to the control. The actual batch cap counts every rejected
copy. The ideal accepted labels are independent uniform on[0,2^dn),
with conditional acceptance probability2^dn/N>1/2.
Run BATCH(this supplier,dn-1,Kp), using its smaller local caps.

For analysis on a correct past, t_j=(t0-low)/2^j is an integer.
The exact modular transform gives root phase

    exp(2pi i 2^(dn-1)W alpha_j(s-cj)/N)
       =exp(2pi i K0 W t_j/M)
       =(-1)^(W t_j) exp(-pi i W t_j/M).                (11.2)

The first equality modulo one uses dn-1>=a2 and
s-cj=2^j t_j mod M; the unknown two-adic component cancels.
No gate implements the final small angle: it is the resulting physical
phase of the exact modular supplier and collimation instrument.

Measure every root in X, obtaining Z_i in{+1,-1}. Define V_i=Z_i
if its known W_i is odd, and V_i=0 otherwise. Set b_j=0 if
sum_i V_i>=0 and b_j=1 otherwise; update low+=b_j2^j.
The rule is specified even on an incorrect past or tie.

Lemma11.2. Conditional on a correct past and successful bootstrap,
each fine bit is incorrect with probability at most2^-30/n, apart from
batch aborts and label-extraction error already charged globally.

Proof. Induction gives |t_j|<=R0: after a correct bit
 t_(j+1)=(t_j-(t_j mod2))/2 has absolute value at most(|t_j|+1)/2.
This applies to negative integers too, with residues0,1. Since R0>=1,
the claimed interval is invariant. Every completed root satisfies
|W_i|<=2Ccap<=2^(Y+1), so |W_i t_j/M|<=1/64. Consequently
cos(pi W_i t_j/M)>=3/4, using pi<4 and cos x>=1-x²/2.
Condition on the batch coarse sigma-field G of10, together with the
correct preceding stages. Top bits remain independent across roots,
and Pr(W_i odd|G)=1/2. By equation(11.2), the independent variables
(-1)^t_j V_i in[-1,1] have means at least3/8 each.
Hoeffding thus bounds a wrong sign, including a harmful tie, by

    exp(-9Kp/128)<=exp(-Kp/16)<=2^(-u-30)<=2^-30/n.

The completion/abort decision is G-measurable: every delivery, retry,
source rejection and cap guard depends only on the coarse controller
history included in10. On each completed G, the deterministic frequency
bound applies and top-bit independence remains as stated in10. Thus the
bound holds conditional on every such G, and integration bounds the event
of an incorrect bit together with batch completion. Aborted histories are
charged separately; no independence of root costs and cap success is used. QED.

After n correct fine bits, low=t0 mod2^n. Since |t0|<=R0<M/2
and M<=N<=2^n, recover its unique signed n-bit value by
 t=low if low<2^(n-1), else t=low-2^n.
Output s1=(chat+t) mod M. This completes the odd secret, including
negative residuals, circular boundary cases and unknown two-adic parts.
The total fine-bit failure probability is at most2^-30.

## 12. 2-adic part: s2 bit by bit

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for a unique s2 in [0, 2^a2). Find its bits at levels
g = 0..a2-1. Let s2low be the known low g bits, sh_g = s1 + M s2low (mod N), wd = a2 - g, and rem = (s2 - s2low)/2^g in Z/2^wd, so
s - sh_g = M 2^g rem (mod N).

A leaf qubit for level g: acquire a copy, apply Shift_(sh_g), which makes the secret s - sh_g; run LE to obtain k; apply X to the
control. Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with kk = k mod 2^wd. Since 2^wd divides N and k
is uniform on Z/NZ, kk is uniform on [0, 2^wd). Use kk as the label.

- If wd = 1: make up to Kp leaf qubits, stopping at the first with kk = 1; measure it in X. The outcome is + iff rem is even. If
  none has kk = 1, set the bit to 0.
- If wd >= 2: run BATCH(this supplier,wd-1,Kp). Take the first root with W odd, and measure it in X. By (9.1) it is
  (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2, which gives rem mod 2 exactly. Release the other roots. If no root
  has W odd, set the bit to 0.

By (10.3), and independence of distinct roots given G, each such level misses with probability at most 2^-Kp, even if s1 was wrong.
Set bit g of s2. In the ideal run with s1 correct and no miss, every bit is correct. Output (s1 + M s2) mod N.

## 13. The complete algorithm and its success probability

Finite branch (n < 2^48). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. This branch acquires at most N(n+10) copies. Its resources are bounded by an absolute constant over this finite range; the exact main-branch cap below is not asserted here.

Main branch (n >= 2^48). Compute a2,M,dn,J_full,Kc,Kp,the
schedule,Dcap,Ccap,Y before access, where Dcap,Ccap denote the Kc caps
from8. For a batch with R roots use D_R,C_R as in9. Put

    Cp=256dl2^m(Kp+u+16),
    Qcap=(Y+6)Ccap+2nCp+Kp.

Size LE with this Qcap before any source acquisition. Run11 then12.
Any ABORT releases everything and outputs0. There are at mostY+6
coarse batches, n odd fine batches, and n two-adic batches; the direct
wd=1 step uses at mostKp copies. Thus Q<=Qcap on EVERY branch.
There are at most3n batches sinceY+6<=n throughout the main range.
Compute all CRT constants with ordinary polynomial-time integer routines.

Success. The NEW Lemma9.1 gives batch abort<=(2^-16+2^-12)/n uniformly
for each R. Over<=3n batches this totals<=3(2^-16+2^-12).
Add coarse decoding2^-20, fine votes2^-30, two-adic misses
n2^-Kp<=2^-40 and global LE coupling2^-10. Their sum is less than
2^-8. Correct preceding stages suffice in every conditional error bound;
a union bound on the first error proves unconditional full-secret success.
The finite branch has error at most2^-10 as before. Resources below
bound actual branches even when a prior estimate or extracted label errs.

## 14. All-branch resources

Every counter, array and retry is capped. With l=log2n, Section8 gives
m,Kc,dl,H=Theta(sqrt n),Kp=Theta(l),Y+6=O(sqrt n),
Ccap=O(n2^m),Cf=O(sqrt(n)l2^m). Coarse batches acquire
O(n^(3/2)2^m) copies and all fine/two-adic batches acquire
O(n^(3/2)l2^m). Thus on every execution branch

    Q<=Qcap=O(n^(3/2)l2^m).                         (14.0)

The sum of delivered-demand caps has the same envelope, including every
rejected label, failed input and abort. The quantum stack has at most two
retained index registers per level, each<=H;8.4 gives(m+1)H<=4n.
Leaf, source/data, modular/LE, lookup/controller scratch and Kc root qubits
add O(n). All wires are reset/reused. Therefore S_Q=O(n), with no QRAM.

Classical space. Put k=m-1-i. Remaining precision satisfies
R_i=B-tp_i<= (m-i+1)H=(k+2)H since each nonroot capacity is belowH
and the root below2H. Thus actual high fields obey
w_i=R_i+1+i+g_w<=(k+3)H, usingm+g_w<=H. Radix buckets, records,
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

Work. Each leaf costs O(n2^dl) core steps and consumesdl delivered
qubits. At heighti a merge attempt consumes2^(i+1)dl disjoint canonical
delivered qubits not reused by another attempt there, and costs
O(n2^(dl+i+1)). A partial leaf at abort is charged fully. Transition projections cost
O(n2^lambda_h0) per trial, with dl2^h0 fresh successful canonical
coordinates consumed each time; failed projections reset and rebuild.
They add only one such level to the same source-based sum. Late
rank/division O(n²) costs are absorbed only for their large inputs, as8.6
proves; no early n²-per-row arithmetic is silently omitted. All m levels
cost O(nD_R2^dl(m+1)/dl) per batch, with(m+1)/dl=O(1) by8.
Using14.0 gives O(n^(5/2)l2^(m+dl)) core tree steps. Address width
is O(H+logn)=O(sqrt n), so total tree work is

    O(n³l2^(m+dl)).                                (14.1)

Extraction confidence has logQcap=O(sqrt n), so source/extraction costs
O(n^(5/2)) core per copy and O(n^(9/2)l2^m) total with addresses.
Coarse scoring over O(sqrt n) stages costs O(Kc*n*2^Y*sqrt n)
=O(n³2^m) core steps. Fine votes, signed updates, parity and CRT,
source charges(n+1)Q, gates, resets and parameter work are also included.
All polynomial terms with exponentm are absorbed by14.1 because
 dl>=d0*sqrt(n) for the fixed positive constant d0: exp(c sqrt n)
dominates every polynomial for c>0, with a finite uniform outer constant.
This is not an expected-cost estimate. Initializing compressed frames
across at most3n batches, including addresses, costs
O(nH²2^H)=O(n²2^H), below14.1 since l<=n and H<m+dl.
Thus14.1 bounds every actual branch, including previous errors.

## 15. Exact uniform envelopes for the reduced uplift

With exact q,t in8, r<=sqrt n+1, H<=t*sqrt n+3 and
kappa<=log2r+3<=l/2+4. Actual uplift satisfies
 s0=ceil(2kappa/3)+2<=2kappa/3+3<=l/3+17/3.
Consequently
 m+dl=H+s0+1<=t*sqrt n+l/3+10,
 m<=q*sqrt n+3,s0=O(l),l=log2n.
Insert these bounds into14's fully charged n³l2^(m+dl) tree bound:
 T=O(n^(10/3)log2(n)2^(t sqrt n)),
 SC=O(sqrt(n)2^(t sqrt n)),SQ=O(n),
 Q=O(n^(3/2)log2(n)2^(q sqrt n)).
The time exponent coefficient39999899241/28284200000 and copy
coefficient141421/100000 remain literal structured rationals. All
outer powers and logarithms are declared, with indices1/2,1/2,0,1/2.
Compared to TAPER's full time n^(7/2)logn2^(t sqrt n), the ratio is
n^(-1/6), while other FOUR objects including clean fraction0 are
identical. This is a full bound improvement, not an improved scalar
index or an optimality/physical-speed claim. The separately proved
finite prefix n<2^48 changes only absolute uniform resource constants;
at n1 logarithmic resource envelopes usepositive n2 values.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope

This exact tapered profile has time coefficient close to sqrt(2), with
resource tradeoffs against other algorithms. Constants and the finite cutoff
may be large. No optimum, practical runtime, positive robustness or physical
quantum execution is claimed.
