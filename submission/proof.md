# STREAMFIXED13367: streaming pairing under a sample budget, T = O(2^((13367/10000) sqrt n)), Q = O(2^((13/10) sqrt n)), S_Q = O(2^((1/2) sqrt n))

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm STREAMFIXED13367 below receives N in binary and fresh
independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch
(every failure, discard and abort included) it satisfies jointly

    T = O(2^((13367/10000) sqrt n)),  S_C = O(2^((13367/10000) sqrt n)),  S_Q = O(2^((1/2) sqrt n)),  Q = O(2^((13/10) sqrt n)).

All constants are absolute. Each of the four envelopes has growth index exactly 1/2 (Section 15). The fifth claim is the clean-input
tolerance 0 (Section 16). The sharper main-branch bounds, from which these follow, are in Section 14. The envelope coefficients are fixed
exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^512:

    r=ceil(sqrt n), L=ceilLog2(n), k=10000000000000001, h=(k-1)/2,
    ell=ceil(463309*r/1000000), w=floor(499999*r/1000000),
    m=ceil(83669*r/100000), dl=ceil(r/2), kappa=ceilLog2(m)+1,
    RHO=20000001/10000000, K=8192*(2*r+L+30).

The odd group size k is FIXED, independent of n. The helper odd_partition.md
specifies the exact instrument, its finite circuit, all-input cleanup and
conditional yield law. All label records here are ordinary classical bits.
There are ell streaming levels, at most k-1 unknown qubits per key,
at most h READY qubits and one PENDING qubit per level, followed by the
collimation tree. Every allocated quantum wire, including unused slots,
is included in the quantum-memory theorem.

## 1. Provenance and mathematical scope

The actual starting framework is my SWF-13377, submission
 d3d5b073-2a02-4ffc-af9f-06225bca48fe, public commit
 9f297ca7481315f5a151e361d98433d105d284bf.
Its complete source extraction, transformations, measured linear merge,
READY/PENDING controller, stopped-flow correction and full-secret decoders
are reproduced and adapted below. Its immediate physical and development
sources SPQ-1408 (99b483c1-eed5-4398-8459-df749d65d390), SPQ-14021
(540fc9a7-7a06-4f13-b725-a95c612ba2d0) and STRIAD-13938
(863aff72-ac48-4706-adc1-5991c730884a) remain credited through this framework.

The replacement odd-partition family and exact dyadic token compiler come
from mpjunior92 PARTROOT196, submission3315027c-4ec3-4352-80e5-f8f384e286f1,
commit34211deace09bfd907619767f8aa5fa30ba44114, virtual.md Sections7.1-7.2.
The helper reproduces the full needed argument for our FIXED k. The source's
growing-k profile and basis-qubit record bank are not used. The earlier FW
macro in SWF is replaced; this is not a claim to have invented either macro.
Earlier sources include Kuperberg's merge, CS1, CYC1 and the SPQ/streaming
lineage explicitly credited by the actual sources. No prior acceptance,
artifact identity, diagnostic or attribution verdict is a mathematical premise.
All five claims concern the self-contained algorithm in these two proof files.
The new material is the fixed odd macro composition, its integer profile,
residue/cap proof and joint four-resource bounds with the smaller coefficient.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates on slot qubits are classically addressed through this charge; there is no
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

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(sqrt n) (Section 14),
this is O(n^(5/2)) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL runs. The LABEL-IDEAL run executes this same physical STREAMFIXED13367
algorithm, including capped identity trials, but replaces every LE output by its
latent k. Coupling to the actual run costs at most2^-10 by(5.1).
For the stopped-flow and decoder analyses also use a FULLY IDEAL run
that removes only the identity retry cap and uses the normalized
nonidentity ODD instrument. The helper proves the exact physical identity
channel and normalized law, so no extra operation is assumed free. It is coupled to the
LABEL-IDEAL run until the first identity retry abort, whose separate probability
is bounded in Section13. Below, ideal run means FULLY IDEAL unless
otherwise specified. All resource bounds concern actual branches and
follow directly from caps and fixed allocations.

## 6. Phase vectors and the linear merge

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical label table
lab[0..2^lam). In the ideal run its state is 2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a
global phase, for a fixed real th. Labels are nonnegative integers. The vector is COLLIMATED TO p
if all lab[x] are congruent modulo 2^p. Labels are stored in full, in fixed fields of 3n bits, which
suffices by Section 9 (label bound).

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x] into a clean w-bit
register, controlled by a lam-qubit index x. For each row x0 it computes the flag [x = x0] with a
Toffoli chain on O(lam) scratch, applies CNOTs from the flag to the output bits where tab[x0] has a
1, and uncomputes the chain. Indices outside [0,E) give output 0. The circuit is its own inverse,
has O(E (lam + w)) gates and O(lam + w) qubits, and is generated by reading each table bit once.

### 6.2 MERGE(X1, X2; p, b, lam'), for b >= 0

Precondition: X1 and X2 are phase vectors from disjoint sets of qubits, both of length 2^lam,
collimated to p, with index registers x, y and tables al, be. Let cA = al[0] mod 2^p,
cB = be[0] mod 2^p, car = floor((cA + cB)/2^p), aa[x] = floor(al[x]/2^p) mod 2^b and
bb[y] = floor(be[y]/2^p) mod 2^b. Then bits p..p+b-1 of al[x] + be[y] equal (aa[x] + bb[y] + car)
mod 2^b. (If b = 0 the residue registers below are empty and e = 0.)

1. LOOKUP aa into a fresh b-bit register Ru and bb into Rv. Add Ru + Rv + car (mod 2^b) cleanly into
   a fresh Rz, and clear Ru and Rv by repeating both lookups. Measure Rz, obtaining e, and reset Rz.
2. Classical. Let S_e = {(x,y) : aa[x] + bb[y] + car = e mod 2^b} and sz = |S_e|. Merge-sort the
   indices y by key (bb[y], y) into order[]; pos[y] is the position of y. For each x the partners y
   form one contiguous run of order[], the class (e - car - aa[x]) mod 2^b; find its start lo[x] and
   length cnt[x] by binary search. Put off[x] = sum_(x' < x) cnt[x'] and
   rank(x,y) = off[x] + pos[y] - lo[x], a bijection from S_e onto [0, sz). If sz < 2^lam', declare FAIL.
3. Let R have 2 lam + 1 bits. LOOKUP pos into Rp and Dx[x] = (off[x] - lo[x]) mod 2^(2lam+1) into Rd.
   Add Rp + Rd (mod 2^(2lam+1)) cleanly into a fresh R, and clear Rp and Rd by repeating the lookups.
   On S_e, R = rank(x,y).
4. Measure bl = floor(R / 2^lam'). If (bl+1) 2^lam' > sz, declare FAIL.
5. Classical. For v in [0, 2^lam'), find the unique (x_v, y_v) with rank bl 2^lam' + v, in one scan
   over x with running offsets. Apply LOOKUP v -> (x_v, y_v) on the low lam' bits of R, XORing into the
   registers x and y, which become |0>. Reset the high bits of R from their known value bl.
6. Output the low lam' bits of R as the index register, with table lab[v] = al[x_v] + be[y_v].

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

Cost. Write L = 2^lam, L' = 2^lam'. With lam, b = O(sqrt n): nine lookup passes of O(L + L') rows with
O(sqrt n)-bit fields; O(L lam) comparisons of O(sqrt n)-bit keys; O(L) binary searches; O(L') additions
of 3n-bit labels. In total O(n (L + L')) core steps. Quantum scratch is O(sqrt n) beyond the index
registers. Classical scratch is O((L + L') n) bits.

## 7. Fixed odd-partition instrument in a streaming controller

A labeled qubit has table(t0,t1), difference Del=t1-t0 and the equal-amplitude
phase state for the batch parameter th. Collimation to p means Del=0 mod2^p.
Conditional on the latent labels and all past outcomes, all live qubits are
product phase vectors on disjoint source-leaf sets, in tensor product with
the tree. The instrument ODD and its exact capped physical implementation
are proved in odd_partition.md. Its normalized nonidentity law gives
A: (gamma,d)=(1,2), or J_j: (gamma,d)=(j,k-1), j=0,...,h-1.
It returns k-2 unchanged inputs on A, one RECYCLED input on J_j,
and gamma GOOD outputs. Each GOOD has the difference of equal-key inputs.
For every reached macro E[d-RHO*gamma|past]<=0, since the helper proves
mu/p<=2+7/sqrt(k)<2+7*10^-8<RHO. In particular 2gamma<=d always.
Use the helper's EXACT dyadic circuit, not the previous FW/PREP circuit.
It has fixed F0=8*k^2*(ceilLog2(k)+1), Gamma=2^(16F0), at most8F0
private wires, and at most C*n*Gamma core steps per trial. Every macro
allows Ltry=Y+L+64 identity trials and otherwise ABORTs. No trial acquires
a source copy. The identity probability is below1/4 on every joint input.

### 7.2 READY, PENDING and bounded slots

At each level i<ell allocate SLOT_i with E_i=2^pb_i keys and k-1 places
per key; READY_i with at most h good output qubits; and PENDING_i with
at most one recycled same-level input. Initially all are empty. The key is

    key_i(item)=floor((Del mod2^(pp_i+pb_i))/2^pp_i).

NEXT(0) requests a leaf from the supplier. NEXT(i+1) executes at level i:

    if READY_i nonempty: remove and return its first qubit
    item = remove PENDING_i if nonempty, else NEXT(i)
    loop:
        key=key_i(item)
        if SLOT_i[key] has fewer than k-1 qubits:
            append item there; item=NEXT(i); continue
        group=(SLOT_i[key] in arrival order, item)
        clear SLOT_i[key]
        run the capped ODD macro on the ordered group
        if all identity trials fail: ABORT the whole algorithm
        if A cell:
            put the k-2 untouched inputs back into SLOT_i[key]
            append the single good output to READY_i
        if J_j cell with j>=1:
            append all good outputs, ordered by increasing pair endpoint,
                to READY_i
            put the single recycled output into PENDING_i
        if J_0:
            item=the recycled output; continue
        remove and return the first READY_i qubit

Before a new group can be formed, READY_i has been drained and PENDING_i
has been removed. Thus at most one group's outputs are ever in READY_i;
its size is at most h. A returned untouched input has the original key key,
so k-2 such inputs fit in the cleared slot. A recycled sum may change key:
it is deliberately deferred in PENDING_i, never inserted blindly into a
possibly full slot. A J_0 sum is reprocessed by the loop with its new key.
A frame waiting on a lower-level NEXT stored its active input first.

Same-key inputs have equal differences mod2^(pp_i+pb_i), so every good
pair difference is collimated to pp_(i+1). Recycled sums remain collimated
to pp_i. Returned inputs are unchanged. All key and grouping decisions
read only low bits below the prescribed positions. By the helper product-state theorem, good
outputs, returned inputs and recycled outputs are product phase vectors
on disjoint source-leaf sets. Their separate queues preserve this property.

The streaming data allocation is at most (k-1)sum_iE_i+O(k ell), with
additional source/data, tree and ODD scratch counted in Section14. Use a
fixed slot array and an indexed classical free-handle stack. Each handle
has O(n) bits; allocation/release requires one push/pop and O(n) core work,
not a linear search. Queue and slot bookkeeping also costs O(n) per qubit.
The constant factor k is absolute and is charged, not taken to be one.

### 7.3 Stopped flow including queued outputs

Use logical checking points between completed instruments and source or
demand acquisitions. Let A_i be arrivals from NEXT(i), d_j the net number
of inputs removed from level i by its j-th completed group, gamma_j its
number of produced good outputs, L_i the same-level inputs in its slots,
pending place and possible active item, and R_i the READY occupancy.
READY qubits are excluded from L_i. Then deterministically

    A_i=sum_j d_j+L_i, L_i<=(k-1)E_i+1,
    sum_j gamma_j=A_(i+1)+R_i, 0<=R_i<=h.                 (7.5)

Here d_j=2 for A cells and k-1 for J_j cells. the helper rate theorem imply E[d_j-RHO gamma_j|past]<=0 for RHO=20000001/10000000.
The ideal reference run removes only the finite identity retry cap; its
normalized nonidentity law is the helper law. Section13 bounds the coupling. At any
bounded stopping point optional stopping yields

    E[A_i] <= RHO E[A_(i+1)]+(k-1)E_i+1+RHO h.           (7.6)

No uniform-key or independence-of-recycled-label assumption is used.
Also 2gamma_j<=d_j on every branch. Hence
2A_(i+1)<=sum_j d_j<=A_i and sum_iA_i<=2A_0. Every completed group
has d_j>=2, so at most A_0 groups complete across all levels. At most
one additional group can start and abort in identity retry. The finite source cap
therefore bounds all stopping times used in(7.6).

Without caps each NEXT terminates almost surely: if inputs continue,
finite slots force further groups; each group has a positive constant
chance of producing a good output, independent of the past. A pending
or READY qubit never blocks progress. The bounded-stop argument below,
not an assumed expected-time execution, supplies the resource theorem.

Each group uses at most Ltry=O(sqrt n) trials, each costing at most
C*n*Gamma core steps including generation of every elementary gate.
Initialization and occupancy records cost O(poly(n)*sum_i E_i). Thus
all stream work is bounded by C*Gamma*n^4*(A_0+sum_i E_i+1).
All constants involving k and Gamma are fixed and charged.

## 8. Schedule, capacity and explicit residue budget

Write RHO=20000001/10000000 and cbar=10000001/10000000.
Since ln2>1/2 and ln(1+x)<x, log2RHO<1+10^-7=cbar.
Set Dbar=3*K*2^m*dl, Dcap=2^16*n*Dbar,
Ccap=ceil(2^20*n*RHO^ell*Dbar), Y=ceilLog2(Ccap).
Rational powers, ceilings and binary lengths are computed exactly, using
O(r+log n) bits with fixed absolute word-length factors; k and F0 are fixed absolute constants. For r>=2^256,
K<=3*2^13*r, dl<=r, n<=r^2, whence

 log2 Ccap <=(12999990463309/10000000000000)*r+4log2r+41 <=2r-1.

The coefficient is exactly beta+cbar*alpha, with beta=83669/100000,
alpha=463309/1000000. Rounding m and ell adds less than3. The remaining
constant41 exceeds log2(2*2^20*3*3*2^13)+3. The last inequality holds at
2^256 and stays true since .7r-4log2r-42 is increasing there. Thus Y<=2r<=n.
Use

    pbmax_i=min(w,m+ell-i),
    lam_i=dl+i for i<m, lam_m=1,
    tbmax_i=dl+i-kappa-1 for i<m-1,
    tbmax_(m-1)=2(dl+m-1)-kappa-1.

Every tree capacity gives b_i+lam_(i+1)-2lam_i<=-kappa. (8.2)
Since RHO>2,

    RHO^i 2^pbmax_i <= RHO^ell 2^m.                      (8.3)

Here w<m, so pbmax_i=w exactly. Put delta=1/2, omega_0=499999/1000000.
The exact rational leading capacity is

 alpha*omega_0+beta*delta+beta^2/2
   =1000024114741/1000000000000 >1+1/50000.

The exact tree capacity is m*dl+m^2/2+dl+m/2-1-m*(kappa+1).
Pool capacity ell*w >=alpha*omega_0*r^2-alpha*r (since w>=omega_0*r-1).
All losses are bounded by r*(log2r+4): m<=.837r, kappa+1<=log2r+3,
and the positive terms may be discarded. For r>=2^256,
50000*(log2r+4)<r, as holds at the endpoint and the ratio r/(log2r+4)
is increasing. Thus total capacity exceeds r^2>=n. Every maximum is
nonnegative since dl>=kappa+1. These are uniform inequalities, not samples.

Allocate exactly B<=n bits greedily to pb_0,...,pb_(ell-1), then
tb_(m-1),...,tb_0, each capped by its maximum. Put pp_0=0,
pp_(i+1)=pp_i+pb_i,tp_0=pp_ell,tp_(i+1)=tp_i+tb_i. Then tp_m=B;
all key/merge readings are strictly belowB.

For the additional stopped-flow residues in(7.6), (8.3) and RHO>2 give

    sum_(i<ell)RHO^i[(k-1)E_i+1+RHO h]
      <=RHO^ell[(k-1)ell2^m+(1+RHO h)/(RHO-1)]
      <=RHO^ell[(k-1)ell2^m+1+3h]
      <=RHO^ell Dbar.                                    (8.4)

Indeed k=10000000000000001<=16r,ell<r/2,1+3h<=2k<=32r, so the bracket is at
most40r²2^m. In contrast K>=2^14r and dl>=r/2 yield
Dbar>=24576r²2^m. This supplies the residue budget uniformly, including
the READY correction; it is not omitted as a lower-order heuristic.

## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch starts with empty slot tables and a counter of
source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs. At its end, slot qubits are measured and released.

TREE. VEC(0) = LEAF: request dl qubits by calling NEXT(ell) dl times, counting each in a counter D; if D would exceed Dcap, ABORT. These qubits form
the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The
table has length 2^dl, is exactly the tensor product state in the ideal run, and is collimated to tp_0 because every difference is 0 mod 2^(tp_0).
VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until out != FAIL; return out. A root is VEC(m),
evaluated depth-first. Run it K times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap
leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a
batch ABORTs with probability at most 2^-16/n + 2^-18/n.

Proof. Work in the ideal run with exact labels and normalized ODD
outcomes. In the unbounded virtual tree every NEXT terminates almost surely.
The distribution-free merge failure bound gives conditional failure at
most2^-kappa. With tt=2^kappa/(2^kappa-1), a root's expected delivered
leaf demand is at most(2tt)^m dl, and tt^m<=e<3 by2^kappa>=2m.
For K roots, E[D_inf]<=Dbar. Thus Pr[D_inf>Dcap]<=2^-16/n.

Stop this uncapped process when the batch finishes or its source acquisition
counter reaches Ccap. All group counts are bounded, and A_ell<=D_inf. For complete rigor first
stop also after t acquisitions, apply the bounded stopped inequalities,
and then increase t. Nonnegative counters pass by monotone convergence;
no uncapped-work bound is asserted for the physical algorithm.
Iterating(7.6) and using(8.4) gives E[A_0]<=2RHO^ellDbar.
The supplier accepts each acquisition with conditional probability at least1/2;
its bounded stopped sum therefore gives expected acquisitions at most
2E[A_0]<=4RHO^ellDbar. Markov against Ccap yields at most2^-18/n.
The capped run agrees with this process until a cap triggers. Identity-cap aborts
are handled by a separate coupling in Section13, not by conditioning the
stopped argument on a favorable future identity-cap event. QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all ODD cell/junk outcomes; all merge outcomes (e, bl); and all decisions of the controller in
that batch (slot stores and matches, FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every slot key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels,
and of a difference modulo 2^(pp_i+pb_i) with pp_i+pb_i <= B, depend only on the low_j, since multiples of 2^B do not change them.
ODD outcomes have the phase- and label-independent law in the helper conditional outcome law, including their junk values. The identity/nonidentity token law is independent of labels. By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); in ODD each returned or combined output has an injective incidence map on disjoint input sets (Section 7.1); a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs on disjoint
coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

## 11. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (2r + ceil(log2 n) + 30).                                              (11.0)

The stages are j = 0, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. Then J + 1 <= log2 M.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. To supply one leaf qubit, repeat until accepted: acquire a fresh
copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard), and on acceptance apply X to the
control. The batch's acquisition cap applies. In the ideal run accepted labels are i.i.d. uniform on [0, 2^dn), and each copy
is accepted with probability 2^dn/N > 1/2. The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(dn-1) W th = W 2^(dn-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),           (11.1)

so a root is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known frequency f = 2^j W.

Measurement. Run BATCH for stage j. For each root i = 1..K obtain a fair bit beta_i by measuring H|0>, and measure the
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
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(2r + ceil(log2 n) + 30) <= 2^-(Y + ceil(log2 n) + 30), using Y <= 2r. The failure
probability is at most 2^(8-30)/n <= 2^-20/n. QED.

The hypothesis for stage j+1 is the conclusion of stage j, since 2^-(j+3) = rad_(j+1). By induction, with probability at least
1 - 2^-20, theta is within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M.

## 12. 2-adic part: s2 bit by bit

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for a unique s2 in [0, 2^a2). Find its bits at levels
g = 0..a2-1. Let s2low be the known low g bits, sh_g = s1 + M s2low (mod N), wd = a2 - g, and rem = (s2 - s2low)/2^g in Z/2^wd, so
s - sh_g = M 2^g rem (mod N).

A leaf qubit for level g: acquire a copy, apply Shift_(sh_g), which makes the secret s - sh_g; run LE to obtain k; apply X to the
control. Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with kk = k mod 2^wd. Since 2^wd divides N and k
is uniform on Z/NZ, kk is uniform on [0, 2^wd). Use kk as the label.

- If wd = 1: make up to K leaf qubits, stopping at the first with kk = 1; measure it in X. The outcome is + iff rem is even. If
  none has kk = 1, set the bit to 0.
- If wd >= 2: run BATCH with B = wd - 1, with this supplier. Take the first root with W odd, and measure it in X. By (9.1) it is
  (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2, which gives rem mod 2 exactly. Release the other roots. If no root
  has W odd, set the bit to 0.

By (10.3), and independence of distinct roots given G, each such level misses with probability at most 2^-K, even if s1 was wrong.
Set bit g of s2. In the ideal run with s1 correct and no miss, every bit is correct. Output (s1 + M s2) mod N.

## 13. The complete algorithm and its success probability

Finite branch (n < 2^512). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^512). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = n Ccap + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2 = log2 N <= n, there are at most n batches,
each using at most Ccap acquisitions, plus at most K for the single wd = 1 level. So Q <= Qcap on every branch. LE is sized by this Qcap, which is computed before h_e.

Success. Batch source/demand cap failures total at most2^-16+2^-18,
odd decoding at most2^-20, parity misses n*2^-K<=2^-40, and LE coupling
at most2^-10. To compare the physical macro with the normalized reference,
use the exact identity channel in the helper: every identity outcome returns
the entire input, including arbitrary references, unchanged. At most
n*(Ccap+1) macros start: completed macros remove at least2 inputs, the
conservation inequalities sum_i A_i<=2A_0 bound their total by A_0 per
batch, and there can be only one aborting macro. Each start has conditional
all-identity probability <4^-Ltry. Consequently the coupling failure is

 n*(Ccap+1)*4^-(Y+L+64) <=2^-127,

using Ccap<=2^Y, n<=2^L and Ccap>=1. No conditioning on all future
successes occurs. Total failure2^-16+2^-18+2^-20+2^-40+2^-10+2^-127
is below2^-8. The finite branch fails with probability at most2^-10.
All source, demand, identity and decoding loops are finite on EVERY branch.

## 14. Fully charged resources on every main-branch execution

Put PP=RHO^ell*2^m. Dcap=O(n^2*2^m), Ccap=O(n^2*PP),
Qcap=n*Ccap+K. Constants involving the fixed k and Gamma are absolute.
No labels or known records are encoded as basis-qubit memory.

Q <=Qcap=O(n^3*PP), including all rejected acquisitions and aborts.

Quantum allocation: reserve a power-of-two arena large enough for
16*k*ell*2^w+2*(m+1)*(dl+m)+16*n+8*F0+4096 qubits, and count the
ENTIRE arena. SLOT has k-1 places per key, READY at most h per level,
PENDING one, and an active call uses only its owned handle. A returned
GOOD is removed from READY, SWAPped into its tree-leaf coordinate, and
the resulting zero slot is released. No two records own the same unknown
wire. Known integer handles use an ordinary indexed classical free stack:
allocation/free is push/pop, never a search or quantum lookup. The tree
is depth-first and holds at most two index registers per level. LE/source
and merge scratch fit O(n). The helper needs at most8F0 private wires.
Thus S_Q=O(k*ell*2^w+n+F0), counting all inactive reserved wires.

Classical allocation: label tables have 3n-bit fields. Streaming slots,
queues, ownership stacks and counters cost O(poly(n)*k*ell*2^w).
Depth-first tree and merge scratch cost O(poly(n)*2^(m+dl)). Their
geometrically growing table sizes sum to this bound even on failed merges.
Decoder triples/residues and source extraction use polynomial memory.
The serial exact compiler stores only O(F0+n) current bits, not its truth
table, emitted-gate history or a growing collection of constants. Since
m+dl-w>.83*r, all slot/ownership records fit the larger tree envelope.
Initialization of every allocated classical bit and reset of every quantum
wire are charged. Conservatively S_C<=C*Gamma*n^128*2^(m+dl).

Time: each acquisition costs polynomial(n), including LE, transforms and
classical arithmetic. At most Ccap occur per batch. Each macro costs at
most C*n*Gamma*Ltry, and conservation bounds completed macros by Ccap
plus one abort. A merge at level i consumes 2^(i+1)*dl delivered leaves
not reused by another merge at that level, including failures. There are
at most Dcap/(2^(i+1)*dl) such merges, each O(n*2^(dl+i)) steps; summing
levels gives O(n*Dcap*2^dl). Each decoder enumerates at most2^(Y+8)
candidates and K residues, costing O(K*n*2^Y). At most n batches occur.
Setup computes exact rational/integer parameters, CRT and trigonometric
constants. Each integer has O(n+F0) bits, and all fixed-k compiler work is
paid by Gamma. All addresses have O(n+F0) bits, and their bit cost from
Section2 is charged. A generous simultaneous bound is

 T<=C*Gamma*n^128*(PP+2^(m+dl)),
 S_C<=C*Gamma*n^128*2^(m+dl),
 S_Q<=C*Gamma*n^128*2^w,
 Q<=C*Gamma*n^128*PP.

The deliberately loose polynomial128 exceeds the costs just itemized;
no exponential enumeration other than the paid fixed compiler, acquisition
stream, explicit tree tables and decoder loop occurs. Every loop terminates
under the fixed caps, regardless of labels, failures or nonproduct states.

## 15. Uniform envelopes and indices

Exact rounding gives, with r<=sqrt(n)+1,
 m+dl <=(133669/100000)*sqrt(n)+4,
 log2(PP) <=(12999990463309/10000000000000)*sqrt(n)+4,
 w <=(499999/1000000)*sqrt(n)+1.
The positive gaps to the declared exponents are respectively1/100000,
1/1000000 and9536691/10000000000000 for time/SC, SQ and samples.
For every fixed positive c and integer d, n^d*2^(-c*sqrt(n)) is bounded
on n>=1: writing x=sqrt(n), its logarithm is 2d*ln(x)-c*ln(2)*x,
whose derivative is eventually negative. Thus every displayed polynomial
is absorbed by its strict fixed gap, simultaneously. Gamma is FIXED and
is an outside constant, however enormous. The finite branch n<2^512
also contributes an absolute constant because it is a finite set of n.
These establish precisely the four pure-exponential envelopes in Section0.
For every c>0, log2(log2(2^(c*sqrt(n))))/log2(n) tends to1/2.
Thus each chosen envelope has exact growth index1/2, not an optimality claim.

## 16. Fractional error tolerance

The fifth claim is epsilon(n)=0: every acquired copy is an independent
ideal coset state. All four bounds and full-secret success >=1-2^-8 hold
jointly under this promise. No positive malformed-copy fraction is asserted,
and zero is not an impossibility statement about other algorithms/models.

## 17. Limitations

The fixed odd group size, generic truth-function compiler and finite cutoff
are astronomical. This is an asymptotic proof, not a practical speed claim.
It has time growth index1/2, not a cube-root algorithm or an optimal profile.
The bound concerns exactly this one fully specified clean-input stream.
