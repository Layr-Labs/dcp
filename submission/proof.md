# ODDPOLYCAP1-MARGIN50: physical block decoding and a deeper classical cap

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm ODDPOLYCAP1-MARGIN50 below receives N in binary and fresh
independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch
(every failure, discard and abort included) it satisfies jointly

    T=O(2^[(1375001/1000000)*sqrt(n)-n^(49/100)]),
    SC=O(2^[sqrt(n)-n^(49/100)]),
    SQ=O(n^(3/2)*2^[(1/2)sqrt(n)-8n^(49/100)]),
    Q=O(2^[(1375001/1000000)*sqrt(n)-n^(49/100)]).

All constants are absolute. These guarantees concern this ONE algorithm
jointly with full-secret success>=1-2^-8 under independent ideal copies.
Every failure,rejection,source call,gate,allocation,reset,compiler/history,
lookup and address cost is charged on EVERY branch. Every outside power
and rational exponent coefficient above is literal. Each chosen envelope
has exact growth index1/2; the malformed fraction expression is0,without
positive robustness or a robustness-impossibility assertion.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters for n>=2^32768, all by integer arithmetic:

 r=ceil(sqrt(n)), L=ceilLog2(n),
 k=least odd integer>=n,
 j0=floor(sqrt(k)), h=(k-1)/2, RHO=2+7/j0,
 U=least NONNEGATIVE integer with U^100>=n^49,
 m0=ceil((7/8)*r), m=m0+64*U, H=r-128*U,
 ell=dl=ceil((1/2)*r), w=floor(r/2)-8*U,
 kappa=ceilLog2(m)+1, Kc=8192*(2*r+L+30), K=Kc,
 Kp=8192*(L+100), b0=floorLog2(n), Lblk=ceil(n/b0).

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

Actual own working sources are fixed-odd STREAMFIXED13367, balanced
STREAMFIXED13229, and the polynomial-rank growing ODDPOLY1322876 working
proof with its drift annotation clarified. The new capped profile uses
actual fixed-odd STREAMFIXED13376CAP and STREAMFIXED13231CAP clipped
working proofs, plus my SWFC-13384, public16058efc-a4fe-4c81-a306-b2090e8f61c4,
canonicalc65add06467360b09fc9e5c250276bd010f30435, for clipped-width trees,
rounded capped-integral capacity and individually counted plateau tables.
Historical CW1310/CW1 cap credit is retained through that source. Its even
macro and old numeric profile are excluded. The actual public identities
of own working parents are supplied separately only when published.
Historical SPQ-1408/SPQ-14021/STRIAD, Kuperberg, CS1 and CYC1 physical
source credits remain. All actual geometry/caps/resources are rederived.
The actual immediate working source is ODDPOLYCAP86-FRACTIONAL,
with its complete polynomial-rank,physical block and U-margin proof.
This child reduces the actual classical cap coefficient from13/10 to1,
changes depth and (where specified)quantum width,and rederives the exact
clipped-capacity and every joint resource envelope. The complete direct
physical decoder remains ODDPOLYQ13BLOCK-EXPLICIT,PUBLIC
2d5b5341-1ba5-43a8-af8f-653f68a9433f,canonical
23e928d963f5cfc62585c4139bce92842e455332,adapting BLOCK64-SQRT2,
8a59b2a0-202b-4702-8892-22cc1fc513bb,canonical
014da02ac3cd2390cb69189cd7515789028527b2,proof9-12.
The quantum width is unchanged from the actual fractional parent;
this profile introduces no separate variable-width primitive.
The source below retains the original log-size
physical blocks and finite identity retry protocol,not a later one-trial
or enlarged-block draft. All actual public parents are declared separately.
Parent analytical coefficients
are called treecoef; operational b0 always means floorLog2(n).
Published identities are declared separately only when actually available.
No private working draft is assigned a fabricated public UUID.
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

IDEAL runs. The LABEL-IDEAL run executes this same physical ODDPOLYCAP1-MARGIN50
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
The helper's private-wire/gate bound T0=2^128*(k+1)^32*(ceilLog2(k)+1)^32
satisfies T0<=n^33 throughout the main branch. The counted classical compiled
circuit and generation cost are O(T0^2)<=O(n^66). Inputs' label-table updates
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

## 8. Deeper cap, rounded capacity and source guard

Use Dbar=3*Kc*(k+1)*2^m*dl,Dcap=2^16*n*Dbar,
Ccap=ceil(2^20*n*RHO^ell*Dbar),Y=ceilLog2(Ccap).
All integers/rational ceilings are exact; intermediate cutoff words have
O(r*log(n)) bits and their storage/arithmetic is charged. The helper counts
its full polynomial operands,circuit generation and reversible history.
Write sigma=1/2,beta=7/8,eta=1,d0=beta+sigma-eta=3/8,
Adepth=64U,Bc=128U+1. Put t=n^(49/100). Uniformly t<=U<t+1,
r<=sqrt(n)+1. The smooth ratio t/(log2(n)+1) increases above the main
cutoff and exceeds2 there,so U>=L+1. Also U/r<=2^-326,by U<=2t,
r>=sqrt(n) and n^(-1/100)<=2^-327.68. The increasing smooth ratios
n^(1/100) and sqrt(n)/(log2(n)+1) prove uniformly
 65U*10^8<floor(sqrt(n)),
 (256L+192)*10^8<floor(sqrt(n)).                       (8.0)
No monotonicity of rounded U/L is assumed. These imply
0<w<dl<m<r,ell<r,dl>=kappa+1,(99/100)r<H<r,dl<H<dl+m.
Actual maxima are pbmax_i=min(w,m+ell-i)=w for i<ell,
lam_i=min(dl+i,H) for i<m,lam_m=1,and
 tbmax_i=2lam_i-lam_(i+1)-kappa for i<m.
They are nonnegative and enforce b_i+lam_(i+1)-2lam_i<=-kappa.

Let f(tau)=min(sigma*r+tau,eta*r-Bc). Actual widths dominate f(i).
The increasing1-Lipschitz sum is at least its integral minusm.
Since beta+sigma>eta,the plateau starts before beta*r. With
m>=beta*r+Adepth,the exact capped triangle gives
 integral_0^m f>=r^2*(beta*sigma+beta^2/2-d0^2/2)
             +Adepth*eta*r-d0*Bc*r-Bc^2/2-Adepth*Bc.
The actual prefix obeys ell*w>=sigma^2*r^2-sigma*r*(8U+1).
The exact identity sigma^2+beta*sigma+beta^2/2-d0^2/2=1 makes
combined capacity ell*w+dl+sum_(i<m)lam_i-1-m*kappa at least
 r^2+64rU-Loss,where
 Loss=8sigma*rU+sigma*r+1+d0*Bc*r+Bc^2/2+Adepth*Bc+m*(kappa+1).
Because sigma+d0<1,U>=L+1,m<r,kappa+1<=L/2+4,
(sigma+d0)r+1<rU and m*(kappa+1)<rL<=rU.
Also Bc^2/2+Adepth*Bc<2^16U^2<rU. Thus
 Loss<(8sigma+128d0+3)rU<56rU<64rU.
Capacity therefore exceeds r^2>=n. Allocate every B<=n greedily to
prefix then root-down tree under these maxima,withtp_m=B. Every
key,merge and partition reads belowB. The cap changes actual sizes,
not the reproduced all-input product/disjoint-incidence law.

Set PP=RHO^ell*2^m. The growing-yield excess obeys
log2PP<=m+ell+28 because k>=n,ell<r,j0>=sqrt(k)/2.
Rounding gives m+ell,m+dl<=(11/8)r+64U+2. Hence
log2PP<1.4r and m+ell>(33/25)r uniformly by8.0.
Kc<=3*2^13r,dl<=r,k+1<=3n<=3r^2 imply
log2Ccap<=1.4r+6log2r+43<=2r-1;the smooth endpoint bound and increasing
.6r-6log2r-44 establish this uniformly. Hence Y<=2r<=n.

RHO>2 and pbmax_i<=m+ell-i give RHO^i*2^pbmax_i<=RHO^ell*2^m.
The full stopped-flow residue is at most
 RHO^ell*((k-1)*ell*2^m+(1+RHO*h)/(RHO-1))
 <=RHO^ell*(k*r*2^m+2k)<=RHO^ell*Dbar.
Here RHO<3,ell<r,1+3h<=2k,andDbar>=24576*(k+1)r^2*2^m.
It also exceeds3Kc2^m dl. Every growing k+1 source/demand factor is
kept,including when the requested root count is reduced below Kc.

### 8.1. Root-dependent batches and global field guard

For a batch requesting R in{Kc,Kp}, put
 Dbar_R=3*R*(k+1)*2^m*dl, D_R=2^16*n*Dbar_R,
 C_R=ceil(2^20*n*RHO^ell*Dbar_R).
Write C_Kc,C_Kp for the corresponding values. The earlier Ccap,Dcap,Dbar
are exactly C_Kc,D_Kc,Dbar_Kc, and Y=ceilLog2(C_Kc) is global.
Kp<=Kc since2r>=70 throughout the main branch, so every C_R<=C_Kc.
All identity retries use the same global Ltry=Y+L+64.
A batch may have h unused top label bits,1<=h<=b0,with B+h<=n.
The geometry allocates its same legal removals for any B<=n,all belowB.

The stopped-flow residue is independent of how many roots are requested
and must still be paid. For R>=Kp>=8192 and dl>=r/2,
 Dbar_R>=12288*(k+1)*r*2^m>=k*r*2^m+2k.
It therefore pays the full residue derived in8. The unbounded expected
delivered demand for R roots is at most3R2^m dl<=Dbar_R. Both facts
hold simultaneously; Markov factors in9 include their sum. No old
fixed-K residue constant is silently reused for a smaller batch.

## 9. BATCH(supplier, B, R, h)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+h)). Here1<=h<=b0,B+h<=n,R in{Kc,Kp}. Output: R roots, or ABORT. A batch starts with empty slot tables and a counter of
source acquisitions; if an acquisition would exceed C_R, the batch ABORTs. At its end, slot qubits are measured and released.

TREE. VEC(0) = LEAF: request dl qubits by calling NEXT(ell) dl times, counting each in a counter D; if D would exceed D_R, ABORT. These qubits form
the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The
table has length 2^dl, is exactly the tensor product state in the ideal run, and is collimated to tp_0 because every difference is 0 mod 2^(tp_0).
VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until out != FAIL; return out. A root is VEC(m),
evaluated depth-first. Run it R times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. A batch has at most C_R source leaves, each label below
2^(B+h). All table entries are nonnegative sums over distinct leaves.
Thus every label is below2^(Y+n),which fits3n bits, and
 |W|<=2^h*C_R<=2^(Y+h).                              (9.2)
Global Y refers to C_Kc,not a new circularly defined batch threshold.

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a
batch ABORTs with probability at most 2^-16/n + 2^-18/n.

Proof. Work in the ideal run with exact labels and normalized ODD
outcomes. In the unbounded virtual tree every NEXT terminates almost surely.
The distribution-free merge failure bound gives conditional failure at
most2^-kappa. With tt=2^kappa/(2^kappa-1), a root's expected delivered
leaf demand is at most(2tt)^m dl, and tt^m<=e<3 by2^kappa>=2m.
For R roots, E[D_inf]<=Dbar_R. Thus Pr[D_inf>D_R]<=2^-16/n.

Stop this uncapped process when the batch finishes or its source acquisition
counter reaches C_R. All group counts are bounded, and A_ell<=D_inf. For complete rigor first
stop also after t acquisitions, apply the bounded stopped inequalities,
and then increase t. Nonnegative counters pass by monotone convergence;
no uncapped-work bound is asserted for the physical algorithm.
Iterating(7.6) and using the residue bound of8.1 gives E[A_0]<=2RHO^ellDbar_R.
The supplier accepts each acquisition with conditional probability at least1/2;
its bounded stopped sum therefore gives expected acquisitions at most
2E[A_0]<=4RHO^ellDbar_R. Markov against C_R yields at most2^-18/n.
The capped run agrees with this process until a cap triggers. Identity-cap aborts
are handled by a separate coupling in Section13, not by conditioning the
stopped argument on a favorable future identity-cap event. QED.

## 10. Unused-top-block independence and score discrimination

ForBATCH(B,R,h),write each accepted labelk_v=low_v+2^B tau_v,
0<=low_v<2^B,tau_v uniform inZ/2^h. LetG include all low_v,all actual ODD cell/token/identity outcomes,all merge
outcomes(e,bl),FAIL/retry/abort/qubit assignments and controller selection
history,but exclude root measurements,their fresh basis coins,unusedtau_v,
and LE internal coins/outcomes,which feed no ideal selection decision.
It is a coarse sigma-field,not the full computer record. Rejected source
history is independent of the subsequent uniform accepted value; every
fixed preceding rejected sequence has equal probability before each value
in its accepted interval. Direct modular suppliers are already uniform.

Every SLOT key,returned/recycled output decision,residue,sort,rank and
block partition inspects only label positions belowB. The actual weighted
ODD cell/token outcomes,including exact identity tokens,have a phase- and
label-independent law on every reached product of equatorial qubits,as
proved in the helper. Its disjoint output groups have injective0/1 leaf
incidence maps. Thus this claim applies to the actual growing ODD stream,
not only to a binary tree. Bits belowB of a sum depend only onlow_v. Stored prefixes and
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
Kp=8192(L+100),L>=log2n. This includes harmful ties. Phase perturbations
may depend onW; the uniform error bound suffices and no independence of
eta andW is asserted. Conditional completedG retains all unused top labels;
therefore integration bounds wrong-block AND completion. Aborts are charged
separately. Direct independent qubits satisfy the same argument.           (10.5)

## 11. Odd part: bootstrap followed by signed near-parity

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every coarse stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K=Kc=8192(2r+L+30), L=ceilLog2(n).                                              (11.0)

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

Measurement. Run BATCH(supplier,dn-1,Kc,h=1) for stage j. For each root i = 1..K obtain a fair bit beta_i by measuring H|0>, and measure the
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
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(2r+L+30) <= 2^-(Y+L+30), using Y<=2r. The failure
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

Ifwd>b runBATCH(supplier,B=wd-b,R=Kp,h=b); its root has phase
exp(2pi i Wrem/2^b),andW mod2^b is uniform by10. Ifwd=b useKp direct
supplier qubits,withW=kk and the same phase; no depth-zero tree is invoked.
Apply10.4 withJ=1 to choosea,and updates2low+=a2^g,g+=b. Release allroots.
There are at mostLblk blocks and at mostone direct batch. Conditional on
correctpast,s1 and ideal extraction,the phase error iszero,so10.5 bounds
each wrong block by2^-30/n. Allcorrectblocks yield s2low=s2 in[0,2^a2).
Output(s1+M*s2low) modN. Rules,sourcecaps and exact modular computations
remain defined on incorrecthistories and their resources are still bounded.

## 13. The complete algorithm and its success probability

Finite branch (n < 2^32768). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. All resources on this branch are bounded by an absolute constant.

Main branch (n>=2^32768). Compute a2,M,dn,J_full,Kc,Kp,b0,Lblk,
the complete schedule and root-dependent budgets before access. Use
C_Kc,C_Kp from8.1 and globalY=ceilLog2(C_Kc); precompute
 Qcap=(Y+6)*C_Kc+2*Lblk*C_Kp+Kp.
LE uses this actual global raw cap to set its confidence before any source
acquisition. Before running the stages,reserve the counted classical arena/compact
handle layout of14,then compile the public helper Boolean
structure ONCE and store its local wire indices. Each later trial maps
those indices to its known physical input handles/private-arena offsets,
with all classical bit/address and gate charges counted in14. Run11 then12. Every BATCH receives its actual R,h and its
own D_R,C_R. Any ABORT releases everything and outputs0. There are
at most Y+6 coarse batches,Lblk odd fine batches,Lblk two-adic batches,
and at most one direct final Kp-qubit block. Thus Q<=Qcap on EVERY
branch. Since Y+6<=n and Lblk<=n,there are at most3n batches.
All CRT/source transformations and scoring rules remain defined on bad
histories too. The helper compilation/indexing and every generated gate
are paid as in7/14,not assumed constant-size in n.

Success. Each batch's source/demand abort probability is bounded by
(2^-16+2^-18)/n uniformly for R=Kc orKp,by8.1/9.
Across3n batches the total is at most3*(2^-16+2^-18).
Coarse decoding adds2^-20,and the first wrong odd/two-adic fine blocks
add at most2^-29 by the conditional score lemma and at most2n blocks.
LE coupling adds2^-10. The exact identity channel gives a coupling to
the normalized reference without conditioning on future success. Across
at most3n*(C_Kc+1) started macros,the all-identity probability is at most
 3n*(C_Kc+1)*4^-(Y+L+64)<=3*2^-127<2^-125.
The sum3*(2^-16+2^-18)+2^-20+2^-29+2^-10+2^-125 is below2^-8.
On the complement of these first-error events,Sections11/12 recover
the entire secret. The finite branch has error at most2^-10 as before.
Every actual branch terminates under its finite source/demand/retry caps.

## 14. Every allocation,compiler bit and charged execution branch

PP=RHO^ell*2^m. Root-dependent batches in8.1/13 have
 C_R<=C*R*n^(5/2)*PP,D_R<=C*R*n^(5/2)*2^m,
with rounding+1 absorbed since PP>=1. Both k+1 and dl factors are kept.
Because(Y+6)Kc=O(n),b0>=L/2,Kp=O(L),andLblk=O(n/L),the exact global
raw cap gives Q<=Qcap=O(n^(7/2)*PP),including every rejected acquisition.
The total delivered cap likewise is O(n^(7/2)*2^m).

Reserve the complete power-of-two-rounded quantum arena for
16kell2^w+2(m+1)(dl+m)+2^32n+T0+4096 wires. This counts every inactive
slot,source/merge/index/controller scratch,completed Kc roots and private
helper/history wire. Kp<=Kc,so blocks require no larger allocation.
Input/READY/PENDING/SWAP ownership is exactly7.2;the helper uncomputes
its whole history before returning,so paused NEXT frames do not retain
an unfinished computation. One clean private workspace is reused.
Since k<=2n,ell<r<=2sqrt(n),T0<=n^33,the complete allocation obeys
 SQ<=C*(n^(3/2)*2^w+n^33).
Here w<=(1/2)r-8U,r<=sqrt(n)+1,U>=n^(49/100),so the first term is
O(n^(3/2)*2^[(1/2)sqrt(n)-8n^(49/100)]). The polynomial term
fits too:its ratio is n^(63/2)*2^[-(1/2)sqrt(n)+8n^(49/100)],
which tends to zero and is bounded because49/100<1/2.
Thus precisely SQ=O(n^(3/2)*2^[(1/2)sqrt(n)-8n^(49/100)]).
No inactive/private wire is discarded by this sharper retained-trim count.

Reserve a fixed ordinary CLASSICAL arena
 MC=2^128*(n^3*2^H+n^3*2^w+T0^2+n^8) bits before source access.
The entire arena,including unused padding and all compiler regions,is
counted. Its compiler/parameter part persists across batches;only stage
regions are cleared between batches. Input N and the finite controller
add O(n) bits,also included below. Every RAM array uses power-of-two
record strides and aligned blocks. Labels have3n payload bits;known
handles/pointers use A=2^20+16r+4096L bits,rounded to a power-of-two
stride at most2A. This is an actual representation choice,not a free
word-arithmetic convention. Local circuit indices retain O(log T0) fields.
The phase/lookup arrays need O(n^(3/2)*2^H) used bits and source records
O(n^3*2^w);fixed padding,all pointer registers,all score/CRT/counter
scratch and the compiled list/history fit MC. The fixed factor2^128
covers the finitely many structures;the polynomial term n^8 covers
ordinary noncompiler arithmetic,and the compiler uses O(T0^2) bits.

The ACTUAL tariff in rules is ceilLog2(M+2),where M counts all allocated
classical bits and quantum wires. The arena formula,T0<=n^33,H<=1.3r,
w<=r/2 and the explicit quantum arena give
 ceilLog2(M+2)<=256+max(H+3L,w+3L,66L,8L)<=A=O(r).
All transients and inputs are covered by the fixed padding factor and
O(n) term. Thus classical indexed operations and classically selected
gates each pay O(r),not an assumed constant. Uniformly L^2<=r and
r^2=O(n):the first follows from the increasing smooth ratio
sqrt(n)/(log2(n)+1)^2 and its huge endpoint value.

A fixed-field scan is implemented with live counted pointer/cursor
registers. A scan of b consecutive bits uses O(b+A) cursor-bit changes
by amortized binary increments,plus b indexed reads/writes. Address
construction/copy uses O(A) bit operations. Charging each indexed step
and each address bit operation by O(A) gives O((b+A)A) work,including
setup. Aligned power-of-two strides construct an arbitrary row address
by concatenation/shifts,not repeated large multiplication. Copying any
O(r)-bit field or computing a known handle therefore costs O(r^2)=O(n).
No arbitrary integer operation is unit cost. Unknown quantum indexing
inside the helper/merge remains its explicit counted full scan.

Every phase-vector label is stored in3n bits. At most three tables per
retained level,including EVERY plateau level,coexist with O(n2^H)
lookup/sort scratch. Since m=O(sqrt(n)),these take O(n^(3/2)*2^H)
classical bits. Stream slot/queue/ownership/free-handle records use at most
O(n^3*2^w) bits. The full compiled gate list,generation history and current
operands use O(T0^2)<=O(n^66) bits;all other parameter/CRT/score/counter
scratch is polynomial and fits that budget. Thus simultaneously
 SC<=C*(n^3*2^H+n^3*2^w+n^66).                   (14.1)
The larger n^3 table factor counts ALL reserved classical padding,not
only used records. No geometric sum replaces repeated plateau levels.

The public circuit is compiled ONCE;generation/list/history initialization
with all addresses fits O(n^68),kept separate from trial work. On each
trial a stored local wire index has O(L) bits. It selects one of the k
known input handles or a fixed private-arena offset. Power-of-two record
strides and the scan construction above map/read/update that O(r)-bit
handle with O(r^2)=O(n) work,including gate application and its tariff.
Thus at most T0<=n^33 gates cost O(n^34) per trial. Private reset and
measured-cell/label bookkeeping fit this generous bound as well. There
is no new QRAM primitive or uncharged full-word read.
At most O(n^(7/2)PP) macros start across all batches,including aborts;
conservation7bounds them by arrivals plus3n. Ltry=O(sqrt(n)) finite
trials per macro therefore give
 O(n^38*PP) total trial/gate/mapping work.             (14.2)
No exponential number of calls multiplies standalone compiler generation.

For a tree merge at level i,all quantum lookup/rank/inverse fields have
O(r) bits. There are O((2^lam+2^lam')r) quantum gates;each known physical
index is constructed/copied/applied with O(r^2) charged work. Sorting
and binary-search steps have O(r)-bit keys/indices,with O(E r)
comparisons/searches each O(r^2),whereE=2^(dl+i). Full3n-bit label
additions/reads are sequential scans costing O(nr) per row. Aligned
strides and maintained cursors include all address formation. Hence a
merge costs O(n*r*2^(dl+i)),not merely a unit-cost lookup.
Completed attempts consume2^(i+1)dl disjoint delivered leaves,including
failures. Summing levels underD_R gives O(n*r*D_R*2^dl),since m/dl=O(1).
An aborting partial path adds at most O(n*r*2^(m+dl)),already within
that budget becauseD_R>=2^m. Summing actual R-dependent delivered caps
over all batches gives O(n^(7/2)*2^m). Total tree work is therefore
 O(n^5*2^(m+dl)).                                    (14.3)
Every partial/failed path,gate-generation pass and address is counted.

LE/transforms/source costs,coarse scores and fine modular residue scoring
are at most O(n^8*PP),including addresses:LE uses O(n*sqrt(n)) tests per
copy,each O(n) core and O(n) address charge;Qcap=O(n^(7/2)PP).
Coarse scoring has O(sqrt(n)) stages with Kc=O(sqrt(n)) and at most2^(Y+8)
candidates,2^Y<=2C_Kc=O(n^3PP). Fine stages enumerate at most2^b<=n
candidates withKp=O(L),and their remaining work is polynomial(n).
Initializing/clearing all plateau arrays over3n batches costs at most
O(n^(9/2)*2^H);stream regions similarly cost O(n^(9/2)*2^w). These fit
O(n^8PP):for this balanced profile log2PP>=m+ell>1.32r while H<=r;
the present profile is balanced,so the first strict exponential gap suffices. The stream's
leading exponent1/2 is smaller than the source exponent. These arguments
pay ALL array initialization rather than assuming it free.
Every integer/cap/CRT operation fits the separately charged polynomial
initialization budget. Every loop is fixed-length or consumes arrivals or
leaves under a finite cap. Altogether every branch obeys
 T<=C*(n^38*PP+n^5*2^(m+dl)+n^68),
 Q<=C*n^(7/2)*PP.                                    (14.4)

## 15. Four literal fractional envelopes for the actual cap coefficient1

Write a=1375001/1000000,a0=11/8,t=n^(49/100). Then a-a0=1/1000000.
Section8 gives log2PP<=a0*r+64U+30 and m+dl<=a0*r+64U+2.
The exact8.0 inequalities imply
 65U+256L+192<2*10^-8*sqrt(n)<(a-a0)*sqrt(n).
Since r-sqrt(n)<=1 and U>=t,the full14.4 time/copy ledger gives
 T=Q=O(2^[a*sqrt(n)-n^(49/100)]).
This pays n38PP,n5*2^(m+dl),n^(7/2)PP and the declared negative
unit fractional margin. Standalone n68 fits by its smaller leading
coefficient and a bounded-ratio argument;it is not a free compiler.
The actual padded classical cap is H=r-128U,so
 n^3*2^H<=C*2^[sqrt(n)-n^(49/100)],
because127U>=3L. Stream term n^3*2^w has leading coefficient
1/2<1;compiler n66 is polynomial. Both ratios to the stated SC
bound tend to zero and are bounded. Therefore precisely
 SC=O(2^[sqrt(n)-n^(49/100)]).
Section14 gives SQ=O(n^(3/2)*2^[(1/2)sqrt(n)-8n^(49/100)]),
counting every inactive slot,controller/source/tree/lookup scratch and
private wire. All four guarantees apply to the same actual configuration
and every branch,including aborted or incorrect histories.
The finite exhaustive branch n<2^32768 changes only absolute constants.
Each positive envelope has log2 equal to c*sqrt(n)-d*n^(49/100)
plus at mostp*log2n,withc>0. Its logarithm divided bylog2n tends to1/2.
These are exact indices of the chosen upper envelopes,not lower bounds,
optimality claims or a practical quantum runtime assertion.

## 16. Fractional tolerance and limitations

The fifth expression is epsilon(n)=0 under independent ideal copies.
All four branchwise costs and full-secret success>=1-2^-8 hold jointly.
No positive malformed fraction or robustness impossibility is asserted.
This is an asymptotic proof with huge cutoffs,not a practical quantum
runtime,cube-root result or global optimum. The complete two proof files
supply all mathematical premises;previous verdicts,diagnostics and public
artifact-identity assertions are not premises. This new configuration
requires its OWN genuine protected atomic review before publication.

## 17. Actual compiler and proof scope

The actual compiler is the explicitly counted T0=2^128*(k+1)^32*
(ceilLog2(k)+1)^32<=n^33 helper7.4. Its full Boolean program,constant
reversible conversion,history and circuit generation are reproduced.
All capacity and resource claims for the changed fractional clipped
schedule are proved above,not inferred from a source verdict. This
new configuration needs its own genuine protected joint review.
