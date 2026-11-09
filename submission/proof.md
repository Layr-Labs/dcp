# ODDPOLY1322876: polynomial odd-token ranks with a balanced growing stream

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm ODDPOLY1322876 below receives N in binary and fresh
independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch
(every failure, discard and abort included) it satisfies jointly

    T = S_C = Q = O(2^[a*sqrt(n)-n^(49/100)]),
    S_Q = O(2^[sqrt(n)/2]),  a=330719/250000=1.322876.

All constants are absolute. These are branchwise bounds for this ONE
algorithm, jointly with full-secret success>=1-2^-8 and clean-copy
tolerance0. They include every failure, discard, allocated wire, circuit
history, lookup, gate-generation and address cost. Each selected envelope
has exact growth index1/2. The negative term is literal, not notation
for an unspecified smaller-order quantity. Sections14/15 derive it.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters for n>=2^32768, all by integer arithmetic:

 r=ceil(sqrt(n)), L=ceilLog2(n), z=ceil(sqrt(7*n)),
 k=least odd integer>=n,
 j0=floor(sqrt(k)), h=(k-1)/2, RHO=2+7/j0,
 m0=ceil((z-r)/2), m=m0+256*L,
 ell=ceil(r/2), dl=ceil(r/2), w=floor(r/2)-128*L,
 kappa=ceilLog2(m)+1, K=8192*(2*r+L+30).

Integer roots are computed by bounded binary search; no real-number oracle
is an instruction. The group size k is n when n is odd and n+1 otherwise;
n<=k<=2n. Its polynomial compiler and full history are charged explicitly.
The helper odd_partition.md proves the exact all-k instrument and its
polynomial contained-token/rank circuit. All known records here use counted
ordinary classical bits. All reserved quantum wires, including inactive
slots and the full reversible history, are counted.

## 1. Provenance and the new construction

The complete physical/source/linear-merge/full-secret decoder and bounded
READY/PENDING stopped-flow framework are adapted from my SWF-13377,
d3d5b073-2a02-4ffc-af9f-06225bca48fe, public9f297ca7481315f5a151e361d98433d105d284bf.
Its old FW cell/back arithmetic also informed the new explicit token rank
construction; its old even FW operation is not run. The all-odd-k weighted
cell family, product outputs, analytic yield inequality and general exact
dyadic token idea come from mpjunior92 PARTROOT196,
3315027c-4ec3-4352-80e5-f8f384e286f1, public34211deace09bfd907619767f8aa5fa30ba44114,
virtual.md7.1-7.2. The helper reproduces the needed all-k proof.
It REPLACES the generic exhaustive truth-function compiler by explicit
minority-pair and partial-permutation ranks, with polynomial compilation
and a fully counted reversible computation history. No basis-qubit known
record bank is used, and no generic growing compiler is hidden as a constant.

Actual own working sources are fixed-odd STREAMFIXED13367 and balanced
STREAMFIXED13229. Their actual public identifiers are supplied in the
separate dependency declaration only when public. This candidate changes
the actual macro compiler, growing k, integer geometry, caps/accounting and
all resource statements, and supplies complete proofs anew. Historical
SPQ-1408/SPQ-14021/STRIAD, Kuperberg, CS1 and CYC1 source credits remain
through the physical framework. The cap-only SWFC construction is not run.
No prior verdict, identity assertion or diagnostic is a mathematical premise.

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

IDEAL runs. The LABEL-IDEAL run executes this same physical ODDPOLY1322876
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

## 7. Polynomially compiled growing odd instrument and bounded stream

### 7.1. Exact public growing macro

A labeled qubit has table(t0,t1), difference Del=t1-t0 and the
uniform-magnitude phase state for the batch parameter th. Collimation to p
means Del=0 mod2^p. All live phase vectors use disjoint source-leaf sets
and are in product conditional on latent labels and the previous outcomes.
The helper proves the all-k ODD instrument, exact contained-token rank
circuit and conditional law: A yields(gamma,d)=(1,2), while J_j yields
(gamma,d)=(j,k-1), j=0,...,h-1. On every reached normalized macro,
E[d-RHO*gamma|past]<=0, since mu/p<=2+7/sqrt(k)<=2+7/j0=RHO.
The helper's private-wire/gate bound T0=2^128*(k+1)^64*(ceilLog2(k)+1)^64
satisfies T0<=n^65 throughout the main branch. The counted classical compiled
circuit and generation cost are O(T0^2)<=O(n^130). Inputs' label-table updates
are polynomial(n). Every macro permits Ltry=Y+L+64 exact identity trials,
then ABORTs if all are identity. A trial acquires no source copy and its
identity probability is below1/4 on arbitrary joint inputs. The helper
proves all-input channel and cleanup, as well as the product-state invariant.

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
The growing factor k and all handle records are charged explicitly; k<=2n.

### 7.3 Stopped flow including queued outputs

Use logical checking points between completed instruments and source or
demand acquisitions. Let A_i be arrivals from NEXT(i), d_j the net number
of inputs removed from level i by its j-th completed group, gamma_j its
number of produced good outputs, L_i the same-level inputs in its slots,
pending place and possible active item, and R_i the READY occupancy.
READY qubits are excluded from L_i. Then deterministically

    A_i=sum_j d_j+L_i, L_i<=(k-1)E_i+1,
    sum_j gamma_j=A_(i+1)+R_i, 0<=R_i<=h.                 (7.5)

Here d_j=2 for A cells and k-1 for J_j cells. the helper rate theorem imply E[d_j-RHO gamma_j|past]<=0 for the actual growing RHO=2+7/j0 specified in7.1 and Sections0/8.
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

Each group uses at most Ltry=O(sqrt(n)) trials of a polynomial(n)
gate circuit; every gate application and generation is charged. Its complete
classical table updates, slots and queues also cost polynomial(n). By
conservation the total stream work is at most poly(n)*(A_0+sum_iE_i+1).
The single clean helper workspace is reused: no completed macro leaves a
live computation history in a paused NEXT frame.

## 8. Exact geometry, capacity and residue budgets

Use Dbar=3*K*(k+1)*2^m*dl, Dcap=2^16*n*Dbar,
Ccap=ceil(2^20*n*RHO^ell*Dbar), Y=ceilLog2(Ccap).
RHO is an exact rational; exponentiation and ceilings use integer arithmetic.
Its intermediate numerator/denominator words have O(r*log(n)) bits, at most
polynomial(n), even though the represented cutoff is enormous. All setup
arithmetic and storage are charged. For later use set b0=sqrt(7)/2, an
ANALYTICAL constant, not an instruction. Integer roots and rounding give

 m+dl <=b0*sqrt(n)+256*L+3,
 m+ell <=b0*sqrt(n)+256*L+3.

Since k>=n and j0>=sqrt(k)/2,
 log2(RHO)<=1+7/j0,
 log2(RHO^ell*2^m)<=b0*sqrt(n)+256*L+31. (8.1)

Here ell<=r<=2sqrt(n) and7/j0<=14/sqrt(n), so their extra
product is at most28. This is a fixed exponent additive constant, not
a growing remainder. For n>=2^32768 the bound is below1.4r:
b0<1.323 and(256L+31)/r<.001 by the endpoint and monotonicity.
Also K<=3*2^13*r, dl<=r, n<=r^2 and k+1<=3n<=3r^2, so
 log2Ccap<=1.4r+6log2r+43<=2r-1.
The endpoint is r>=2^16384 and .6r-6log2r-44 increases thereafter.
Thus Y<=2r<=n and the same physical label-extraction/decoder sizes apply.

The actual streaming and tree maxima are
 pbmax_i=min(w,m+ell-i) (i<ell),
 lam_i=dl+i (i<m), lam_m=1,
 tbmax_i=dl+i-kappa-1 (i<m-1),
 tbmax_(m-1)=2*(dl+m-1)-kappa-1.
They enforce tbmax_i+lam_(i+1)-2lam_i<=-kappa at every level.
All maxima are nonnegative, since dl>=kappa+1. Moreover
0<w<r/2<m<r, ell<r and k<=2n on this branch. For example
z>=sqrt(7)*sqrt(n), z<=sqrt(7)*sqrt(n)+1, r<=sqrt(n)+1 and
256L/r<.001 give .82r<m<.824r. Thus pbmax_i=w exactly.
These inequalities hold at the stated cutoff and strengthen with n.

Here is a rounded capacity proof without an assumed real profile.
The exact tree capacity is
 m*dl+m^2/2+dl+m/2-1-m*(kappa+1).
The streaming capacity is ell*w>=r^2/4-64rL-r/2, since
ell>=r/2 and w>=r/2-128L-1>0. For the base m0,
 m0*dl+m0^2/2 >=z^2/8-r^2/8.
Indeed dl>=r/2 and m0+r/2>=z/2; expand the square.
Adding the stream leading term gives z^2/8+r^2/8>=n.
Increasing m0 by256L adds at least256rL to m*dl+m^2/2,
because dl+m0>=z/2>r on this branch. All losses, including
64rL+r/2, m*(kappa+1), the isolated1 and discarded rounding terms,
are below70rL: m<r,kappa+1<=log2r+3<=L/2+4, L>=32768.
Thus actual total capacity is greater than n. No test grid is a premise.
Allocate exactly B<=n bits greedily to pb_0,...,pb_(ell-1), then
root-down tb_(m-1),...,tb_0, capped by these maxima. Define pp,tp as
in the stream/tree, so tp_m=B and all key/merge readings are belowB.

For the stopped-flow residue, RHO>2 and pbmax_i<=m+ell-i give
 RHO^i*2^pbmax_i<=RHO^ell*2^m.
Consequently
 sum_(i<ell) RHO^i*((k-1)*E_i+1+RHO*h)
 <=RHO^ell*((k-1)*ell*2^m+(1+RHO*h)/(RHO-1))
 <=RHO^ell*((k-1)*ell*2^m+1+3h)
 <=RHO^ell*(k*r*2^m+2*k) <=RHO^ell*Dbar. (8.2)
Here RHO<3, ell<r and1+3h<=2k. The inflated public budget
Dbar=3*K*(k+1)*dl*2^m is at least24576*(k+1)*r^2*2^m,
so it pays this whole growing slot/READY residue. It also exceeds the
unbounded-tree expected demand3*K*2^m*dl. This extra polynomial factor
is included in source, demand, memory and time accounting, not suppressed.

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

Finite branch (n < 2^32768). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^32768). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

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

## 14. All branchwise resources, including the polynomial compiler

Let PP=RHO^ell*2^m. Dcap=O(n^3*2^m), Ccap=O(n^3*PP),
Qcap=n*Ccap+K, so Q<=C*n^4*PP including all rejections and aborts.
All constants here are absolute and no factor involving growing k is
hidden as a constant. k<=2n and the helper T0<=n^65 are used explicitly.

Quantum allocation. Reserve the whole power-of-two-rounded arena for
16*k*ell*2^w+2*(m+1)*(dl+m)+2^32*n+T0+4096 wires; count every wire,
including inactive slots. SLOT/READY/PENDING/active handle ownership is
as in7.2. Transfer a returned good output by SWAP into its tree coordinate
and release the resulting zero slot. No two records own one unknown wire.
The helper computes/copies/uncomputes each rank function and measures/resets
its token register before returning, so its entire private history is clean
and one global workspace suffices across all levels and trials. Paused
NEXT frames hold phase-state handles, not unfinished compiler circuits.
The K completed root qubits are reserved as well: K<=24576r<n on
this branch. Depth-first tree indices cost O(n), as do source/LE and
merge scratch; the generous fixed2^32*n allowance includes all of them.
Since k*ell<=2*n^(3/2)<=n^2 and T0<=n^65, the full allocation satisfies
 S_Q<=C*(n^2*2^w+n^65).
With w<=r/2-128L and r<=sqrt(n)+1,
 n^2*2^w<=2^(sqrt(n)/2+1/2)*n^(-126).
Also n^65=O(2^(sqrt(n)/2)): the ratio65*log2(n)/sqrt(n) is
already below1/2 at the main cutoff and decreases thereafter. Therefore S_Q=O(2^(sqrt(n)/2)) uniformly.
All ordinary known records remain classical; no basis-bank wrapper is used.

Classical allocation. Every label has3n bits. Stream slot/queue/free-stack
records use poly(n)*2^w bits, including every indexed handle. The depth-first
tree holds at most three tables per level; their geometrically increasing
sizes sum to O(poly(n)*2^(m+dl)), including the active merge lookup/sort
scratch. The compiled helper gate list and classical generation history
cost O(T0^2)<=O(n^130) bits and are counted, not assumed free. All integer
parameter words, actual rational-cap numerator/denominator arithmetic,
source/LE counters, CRT, decoder triples and residues cost polynomial(n).
Since m+dl-w>.8r on the main branch, these fit the tree envelope. Initializing
all allocations and resetting every private wire are charged.

Time. There are at most Ccap acquisitions per batch. LE, transforms and
known-label arithmetic cost polynomial(n) per call. At most Ccap completed
macros and one aborting macro occur per batch; Ltry=O(sqrt(n)) trials per
macro use a fully generated circuit of at most T0<=n^65 gates plus O(k*n^2)
classical table work. Circuit generation/list storage is O(T0^2)<=O(n^130)
and is paid. Classical data-dependent access in the helper is an explicit
full scan, not an unknown-address primitive; the main known-index handle
stack and every gate pay the address charge of Section2.

A merge at level i consumes2^(i+1)*dl delivered leaves not reused by another
merge at that level, including failures. There are at most
Dcap/(2^(i+1)*dl) such merges, each O(n*2^(dl+i)) work; summing levels
costs O(n*Dcap*2^dl). The decoder enumerates at most2^(Y+8) candidates
with K residues and O(n)-bit arithmetic, costing O(K*n*2^Y) per stage.
At most n batches occur. Setup, every rational/integer operation, loop
administration and gate emission is polynomial(n); all address lengths
are O(n). No uncapped expected work is used as an actual resource bound.

The explicit costs above are bounded simultaneously and conservatively by
 T<=C*n^256*(PP+2^(m+dl)),
 S_C<=C*n^256*2^(m+dl), Q<=C*n^256*PP.
Degree256 exceeds the itemized polynomial costs after T0<=n^65,
including the inflated Dbar factor(k+1), n^130 circuit generation and
the address/retry/batch costs. Every loop
is fixed-length, bounded by a source/demand cap, or consumes inputs under
conservation. Thus every branch terminates, including bad labels, all
failed merges, repeated J_0 outcomes and an all-identity abort. Quantum
space uses the sharper allocated-arena estimate above, not an assumed
outside-constant circuit size.

## 15. Exact joint envelopes and indices

Let b0=sqrt(7)/2 and a=330719/250000. Exact rational squaring gives
 (a-3/10^7)^2-7/4=11765049/10^14>0,
so a-b0>3/10^7. The coefficient b0 is only used in analysis; all actual
parameters are the stated integer-root expressions.
By8.1 and14, each of T,S_C,Q is at most an absolute constant times
 2^[b0*sqrt(n)+1024*L+128].
The generous1024L includes256L from the actual geometry, the degree256
resource factors and all fixed rounding/cap factors. For n>=2^32768,
 (1024*L+128)/sqrt(n)<10^-8, n^(-1/100)<10^-8.
For the first use L<=log2n+1 and the endpoint inequality
(1024*32769+128)*10^8<2^16384; its ratio decreases thereafter by
differentiation. For the second use10^8<2^327. Thus
 1024L+128+n^(49/100)<2*10^-8*sqrt(n)
 <(a-b0)*sqrt(n).
This proves EXACTLY T=S_C=Q=O(2^[a*sqrt(n)-n^(49/100)]).
Section14 gives S_Q=O(2^[sqrt(n)/2]) with no outside polynomial.
The exhaustive finite branch n<2^32768 contributes absolute constants
over a finite set of bit lengths, so the four bounds extend to every N>=2.
No growing macro cost is hidden in that finite-branch argument.

For the first envelope,
 log2(log2(2^[a*sqrt(n)-n^(49/100)]))
 = (1/2)log2n+log2(a-n^(-1/100)),
whose ratio to log2n tends to1/2. The quantum envelope has the same index
by the elementary pure-square-root calculation. These are indices of the
chosen guaranteed envelopes, not lower bounds on optimal DCP complexity.

## 16. Fractional tolerance and limitations

The fifth expression is epsilon(n)=0 under the independent ideal-copy
promise. All four costs and full-secret success>=1-2^-8 hold jointly.
No positive malformed-copy tolerance or robustness impossibility is asserted.
The huge finite cutoff, public group sizes and circuit budgets make this
an asymptotic proof, not a practical quantum runtime. It remains index1/2,
not a cube-root algorithm or a global optimality theorem. Every argument
needed by the original claims is contained in this proof and the helper;
no historical verdict, artifact authentication or diagnostic is a premise.
