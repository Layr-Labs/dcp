# Complete reference program V only: LLV-GFL300

EVERY algorithm/implementation/resource assertion in the original body
below concerns the reference V. Its coarse classical n^3 allocation is
not the stronger physical n^3/log2n claim of LLV-GFL300C in proof.md.
The ENTIRE body is byte-identical to SHA-256 8867fd3c02c4220ec35844b8abf505318befb291259da60d0d4b03c707b4087f.
The current proof supplies its own actual compact classical backing;
no old JSON or historical verdict supplies a theorem premise.

--- BEGIN COMPLETE VIRTUAL SOURCE ---

# LLV-GFL300: full-log phase tables give cubic classical space

## 0. Joint theorem and literal configuration

For everyN>=2 ands inZ/NZ,n=ceil(log2N), this single LLV-GFL300
algorithm recovers the entire secret with unconditional probability
at least1-2^-8 from independent ideal copies. On EVERY branch jointly
 T=O(2^((1/2)sqrt nlog2n+(1/4)sqrt n+2sqrt n(log2n)^(-1/2))),S_C=O(n^3),
 S_Q=O(n),Q=O(2^((1/2)sqrt n)).
Outside constants are absolute. Indices are[1/2,0,0,1/2]. Guaranteed
fractional tolerance is zero under the independent-ideal-copy promise.
For n<2^4096 use the fixed finite branch. Otherwise compute
v=floor sqrt n,r=ceil sqrt n,ell=ceil log2n,lambda=ell,
P=ell^2,H_n=bit_length(n^P-1),
m=floor(P*(v-256ell)/(H_n+ell)),
kappa=ceil log2(m+2)+3,A_bar=ceil((n+m*kappa)/(m*lambda))+2,
center=ceil((m-1)/2),
fan_i=A_bar+i-center for0<=i<m.
Letfan_min=fan_0,fan_max=fan_(m-1),S(t)=t(t-1)/2.
All arithmetic is exact integer arithmetic. The powern^P hasO(ell^3) bits and usesO(logell) repeated
squarings, with charged polynomial work and workspace.

Notation. n=bit_length(N-1),dn=bit_length(N)-1, wherebit_length(x)
is the unique positivek with2^(k-1)<=x<2^k forx>=1. Computea2 by
repeated exact division by2 until the quotientM is odd. ThenN=2^a2 M
andomega=exp(2 pi i/N). For analysis only,s1=s modM and the unique
s2 in[0,2^a2) satisfies s=s1+M s2 modN. These unknowns are recovered
by the decoders, not supplied as secret-dependent input computations.
All logarithms below are base2 unless writtenln.





## 1. Provenance and the full-log table tradeoff

Actual direct full-proof source: my LLV-GBR200, SHA-256
74f2883577a0a8bd7d9e5c8e7ccf4a69f3e1a5fd8c90d96debdb79e5e09e4b7b.
It carries the generic variable-output phase instrument, centered fan-in
and AM-GM product/source ledger, deterministic per-level consumed-leaf
work, explicit quadratic primitive/decoder ledger, source-only LE,
fresh-child capped recursion and all-modulus decoders. Those arguments
are directly adapted, with all changed inequalities proved below.
Its upstream acknowledgments include LLV-GRF320, GPS-WQLOG,
corrected LLV-GPP375, LL5-RAMP, LLV-G125P256, LLV-G125,
GPS/BBHT, LLV-B125, LLV-125, LL6/LL5, MW4, LL4, LL-050,
LL-080, LL-150, CS1, PSieve and Kuperberg. Distinct direct precision sources are also credited: LLV-GRF320,
proof SHA-256060077647c623f8ca5678f5ff14ae54ce4d663c782e7ac508274953aa57331c9,
for the exact power-bit-length depth/source-budget parameterization;
and LLV-GQPL,29b36bcc-4073-4b5d-ac57-70ae0d822d58,
proof SHA-256d83da6450949ecb5db05220fc2c3d030174b0802be0c9b11cf5c8a6cf978062a,
for growing precisionell^2, uniformO(ell^3)-bit power computation and
exact near-power shortcuts. Those precision features are not carried
by the two-entry parent's conservative integer depth rule, so they
are declared separately. All changed source/time inequalities are
proved here; public mappings are in the final cited declaration.

Table log changes from1 toell, slope fromell to1, and a new literal
depth denominator H_n/P+1/ell, P=ell^2, controls the source product. This
raises classical degree2 to3 while lowering the positive time correction
from2sqrt n(log2n)^(1/4) to(1/4)sqrt n+2sqrt n(log2n)^(-1/2) at the same source/qubit/error
envelopes. The source and all costs are reproved for these actual tables
and arities; this is a resource tradeoff rather than parent dominance.
No earlier verdict or provisional attribution is a premise, and no
optimality, priority or practical speed is claimed.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates are classically addressed through this charge; there is no
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
to denominator 2^20. This is a fixed finite computation, an absolute constant, not advice.

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

IDEAL run. The ideal run is LLV-GFL300 in the latent-label model with every LE output replaced by the
latent k. Actual and ideal runs can be coupled to coincide unless some LE call returns a wrong
label, so every event's probability differs by at most 2^-10. Resource bounds are proved for every
ACTUAL branch directly, because they rest only on caps and fixed allocations.

## 6. Phase vectors, the linear merge and four-input enumeration

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

### 6.3 FIND: a fixed finite Grover search

LetP be a known classical predicate onU bits,M_dom=2^U,U>=1.
Definek_max=ceil(U/2),ell_max=2^k_max. FIND(P,J),J>=1, performs
at most8J trials. Each trial draws uniformj in[0,ell_max) with
k_max fair coins, preparesU fresh qubitsH^U|0^U>, appliesj Grover
iterations, measures theU bits, classically verifiesP, then resets
and releases all search scratch. Return the candidate only if verified
marked. If no trial succeeds, returnNONE.

The phase oracle computesP reversibly, appliesZ, and uncomputes.
Diffusion isH^U,X^U,a phase flip on all ones using a Toffoli ladder,
X^U,H^U. This is the usual uniform-state reflection up to a global
sign, irrelevant to measurement probabilities. It usesO(U) scratch
and exact Clifford+T gates. All predicate and gate generation is charged.

Lemma6.2. Every return is marked. With no marked string,FIND always
returnsNONE. Withr_mark>=1 marked strings, missed-solution probability
is at most2^-J. On EVERY branch, trial starts plus Grover iterations
number at most8J*ell_max, independent ofr_mark.

Proof. Verification excludes false positives. Each trial costs at most
1+j<=ell_max units, proving the deterministic count. If all strings
are marked each trial succeeds. Otherwise writer_mark/M_dom=sin²vartheta,
0<vartheta<pi/2. The two-reflection calculation gives marked probability
sin²((2j+1)vartheta) afterj iterations, up to a global sign. Averaging,

 P_avg=1/2-sin(4ell_max*vartheta)/
                    (4ell_max*sin(2vartheta)).        (6.3)

This follows by telescoping the cosine sum ofsin². For integer
1<=r_mark<=M_dom-1,r_mark*(M_dom-r_mark)>=M_dom-1>=M_dom/2.
Thus sin(2vartheta)>=sqrt(2/M_dom) and
ell_max*sin(2vartheta)>=sqrt2. ConsequentlyP_avg>1/4.
Trials use fresh coins and ancillas, so their conditional failure
probability is at most3/4. Across8J trials it is at most
(3/4)^(8J)<2^(-3J)<=2^-J. The algorithm never needsr_mark. QED.

### 6.4 MERGEF: variable arity and variable output length

MERGEF(f,p,b,s_out) receivesf>=1 disjoint phase vectors, each
of lengthLtab=2^lambda, collimated through bitp. The output length
is2^s_out, withs_out in{1,lambda}. Input labels are
label_t[x]=c_t+2^p h_t[x],0<=c_t<2^p. Requireb>=0 and put

 U=f lambda,M_dom=2^U,mu=2^(U-b),Cp=2mu+1,
 ellCp=ceil log2(Cp+1),J=kappa+ellCp+8,
 2^(kappa+s_out)<=mu<=2^(kappa+lambda).             (6.4a)

Actual calls haveU<=O(n),kappa=O(logn),lambda=O(logn).
Cp may exceedM_dom whenb=0. NoCp<=M_dom orf>=4 assumption is
used. LetA_t[x]=h_t[x] mod2^b andcar=floor(sum_t c_t/2^p).
All routing uses only residues belowp+b. Forb=0 all residues and
car mod1 are0; skip the empty accumulator and sete=tau=0.

1. Otherwise initialize a b-bit accumulator tocar mod2^b. For each
   inputt, LOOKUP A_t[x_t] into reused scratch, add modulo2^b and
   uncompute the scratch. Measure the accumulator ase and clear it.
   Original indices hold the uniform-magnitude fiberS_e, sizeF>=1,
   with original phases. Settau=(e-car) mod2^b.
2. Start an empty CLASSICAL tuple listTl. For at mostCp+1 calls,
   stopping earlier at|Tl|=Cp, useFIND(P,J) on fresh U-bit ancillas:

     P(x_1,...,x_f)=[sum_t A_t[x_t]=tau mod2^b]
                     AND[(x_1,...,x_f) is not inTl].

   Append only verified marked tuples. OnNONE stop listing and
   proceed to rank projection. No FIND gate acts on original indices.
   On EVERY branch all trial starts plus Grover iterations total

         <=8J(Cp+1)2^ceil(U/2).                       (6.4)

   This bound remains valid forCp>M_dom; listing can then end after
   exhausting allF tuples and one empty-predicate call. No expected
   search-time argument or enumeration-time cutoff is used.
3. Reversibly scanTl for unique list rankr_idx and membership flagRf
   on original indices. MeasureRf; FAIL if zero.
4. Measurebl=floor(r_idx/2^s_out). FAIL if the complete block would
   exceed|Tl|, that is(bl+1)2^s_out>|Tl|.
5. LOOKUP the selected2^s_out tuples to XOR-clear original indices,
   reset flags/high rank bits, and return the lows_out bits with the
   corresponding full-label SUMS. Labels agree modulo2^(p+b).

On FAIL discard/reset all inputs and scratch; never reuse inputs.
Every successful output is an EXACT phase vector. FIND acts only
on a fresh tensor factor conditional on known tables,e andTl.
Rank/flag/block projections and injective tuple reindexing keep exactly
the original phases. This includes prematureNONE, f=1,s_out=1 andb=0.
The tuple list can have arbitrary verified order. Equal numerical labels
do not identify distinct tuple indices or their incidence sets.

All lookup is serial. Decode a search candidate into f lambda-bit
indices. Scan eachLtab-row residue array with reversible equality,
XOR the matching known value into reused scratch, add, uncompute.
ScanTl for exclusion, using distinctness andO(U) reused scratch.
ComputeP, applyZ and uncompute. Reflection, verification, copying,
measurement/reset, circuit generation and all address operations are
charged. Each unit costs FIXEDpoly(n)*(Ltab+Cp), hence
poly(n)*2^lambda because2^kappa is polynomial inn. No QRAM,
source acquisition or subtree construction is inside an oracle.
Search scratch isO(U+b), reused. Classical lists and arrays are
bounded explicitly inSection14; no full truth table is stored.

Lemma6.3. For any fixed tables and measured e, prematureNONE
while a solution remains has probability at most2^(-kappa-8).
Outside it,tl=|Tl|=min(F,Cp). Averaging over measured e,

 Pr[FAIL|tables]<=2^s_out/mu+
          sum_e(F_e-Cp)_+/M_dom+2^(-kappa-8).         (6.5)

Proof. At mostCp+1 FIND calls give union miss bound
(Cp+1)2^-J<=2^(-kappa-8), uniformly over all tables and preceding
lists. Without a miss allF tuples are found or the list reachesCp.
For anytl verified distinct tuples, flag failure is(F-tl)/F and
block rejection is(tl mod2^s_out)/F. This includesCp>F, f=1 and
b=0. Multiply byF/M_dom and sum over residues. Remainders total
at most2^b*2^s_out/M_dom=2^s_out/mu, and truncation gives the
displayed overflow term. Original phases never affect these structural
probabilities. No favorable-event conditioning is used. QED.

## 7. Leaf qubits

A LEAF QUBIT is a phase vector of length 2 with table (0, k), for its known label k: a positive qubit whose state in the ideal run is (|0> + exp(2 pi i k th)|1>)/sqrt 2, up to global phase, for a fixed real th. There is no pairing stage in this algorithm; leaf qubits go directly into leaf tables.

## 8. Growing-precision full-log profile and exact source budget

For Section0's literal parameters put
 Dbar=2K*lambda*fan_max*A_bar^m,Dcap=2^12nDbar,Ccap=2^13nDbar.
LetY be least with2^Y>=Ccap. For analysis only putL=log2n,x=sqrt n,
P=ell^2,Lhat=H_n/P,D=Lhat+1/ell.
ThenL<=Lhat<L+1/P andm=floor((v-256ell)/D).
Every formula uses integer bit lengths and rational ceilings; there is
no real-log oracle or uncounted parameter search. S(t)=t(t-1)/2 is the
exact sum ofi over0<=i<t, andcenter=ceil(S(m)/m)=ceil((m-1)/2).
All profile, prefix and cap computations have fixed polynomial work
and workspace. The powern^P is computed by repeated squaring
withO(ell^3)-bit integers, using polynomial work andO(n^2) space
or less. Caps haveO(sqrt n+logn) bits.

Uniformly atL>=4096, floors give
 m<=x/L, kappa<=L/2-log2L+6<=ell,2^kappa<16(m+2)=O(x/L).
A lower floor bound ism>=(x-delta)/D withdelta<=258L;
D<=2L,delta<=x/2 therefore give
 n/m<=xD+1032L^2
    <=x(L+1/ell+1/ell^2)+1032L^2.                   (8.1)
SinceL<=lambda<=L+1 and the actual ceiling gives
A_bar lambda<=n/m+kappa+3lambda, the exponential-to-polynomial
inequalities at4096 imply
 x/2<=A_bar<=x*(1+2/ell^2),
 fan_min=A_bar-center>=x/4>=4,
 fan_max=A_bar+(m-1-center)<=9x/8<=n,
 m(A_bar-1)<sum_i fan_i<=m A_bar.                    (8.2)
For example division of(8.1) bylambda=ell gives
A_bar<=x*L/ell+x/ell^2+x/ell^3+1032ell+4
     <=x*(1+2/ell^2).
The last inequality follows fromL<=ell and
x*(1-1/ell)/ell^2>=1032ell+4 at4096 and thereafter.
The lower bound follows fromA_bar>=n/(m lambda)>=xL/(L+1).
The relevant ratios improve thereafter. Also
lambda-kappa>=log2L-6>=6, hence lambda>=kappa+2.

Foru>=0,ln(1+u)<=u andln2>2/3 imply
log2(1+2/ell^2)<3/ell^2. The latter bound onln2 follows by
integrating the strictly convex1/t on[1,2], whose mean exceeds2/3.
Thus, withP=ell^2,
 log2A_bar<=L/2+3/ell^2
          <=(H_n+6)/(2P)<=D/2-1/(4ell).           (8.3a)
For the last step3/ell^2<=1/(4ell) sinceell>=12.
Hence m log2A_bar<=mD/2<=(v-256ell)/2. AM-GM gives
 product_(i<m)fan_i<=(sum_i fan_i/m)^m<=A_bar^m.    (8.3)
This covers every prefix, as allfan_i>=1. No real-log oracle or
powerofA_bar for a precision bound is used in the algorithm.

Full leveli usesf=fan_i,b_i=(fan_i-1)lambda-kappa,s_out=lambda,
with positivewidthb_i andmu=2^(lambda+kappa). Exact prefix capacity is
 C(t)=lambda*(t*(A_bar-center-1)+t(t-1)/2)-t*kappa.
The ceiling and(8.2) give
 C(m)>=m(A_bar-2)lambda-m*kappa>=n.                (8.4)
For1<=B_req<=n find largestu<=m withC(u)<=B_req by integer
binary search. PutR=B_req-C(u), then useu full levels and ONE call
 k=ceil((R+kappa+1)/lambda),f=k,b=R,s_out=1.
Ifu<m thenR<b_u,1<=k<=fan_u-1<=fan_max. Ifu=m then
B_req=C(m)=n,R=0,k=1 becauselambda>=kappa+2. In every case
kappa+1<=k lambda-R<=kappa+lambda, satisfying(6.4a).
The final output is a qubit, total removed width exactlyB_req, and
heightu+1<=m+1. The prefix search is uniform polynomial bit work;
no approximate numerical width choice or binary finishing stage.

Simultaneous frame and quantum use obeys
 lambda*sum_i fan_i<=m A_bar lambda<=n+m*kappa+3m lambda=O(n),
andfan_max lambda=O(xL)<=n. WithK<=2^15r andlambda<=r,
 log2(nCcap+K)<=m log2A_bar+log2fan_max+6L+60
 <=m*(H_n+6)/(2P)+7ell+60
 <=(v-256ell)/2+7ell+60<=v/2<=sqrt n/2.             (8.5)
This is the literal main source cap, including all polynomial factors.
AlsoY<=2r<=n,2^Y<=2Ccap. The finite branch changes outside constants.

## 9. BATCH(supplier, B)

Input: a supplier of leaf qubits, where in the ideal run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch has a counter of source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs.

Use Section8 allocation with B_req=B.

TREE. VEC(0)=LEAF obtains lambda independent supplier qubits,
counting each request againstDcap, and builds their subset-label table.
VEC(i+1) obtains the prescribed number of fresh VEC(i) children on
disjoint copies and applies MERGEF with the public level parameters.
At full leveli these arefan_i,p_i=C(i),b_i=(fan_i-1)lambda-kappa,
s_out=lambda. At the last level they arek,p=C(u),b=R,s_out=1.
On FAIL discard all inputs and build fresh children. A root isVEC(h),
evaluated depth first; a batch requestsK roots. Children are completely
built before the current tuple list is allocated. Child lists were
released after their output tables were formed; only one merge keeps
a current list at a time. Prefix allocation is fixed by publicN,B.

Root. VEC(h) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma9.1 (no abort). In the ideal run a batch aborts with
probability at most2^-11/n.

Proof. Lemma10.2 below bounds each actual MERGEF trial's failure,
averaged over its untouched current residues, byeta=2^(1-kappa).
Sinceeta<=1/[4(m+2)]
and heighth<=m+1, Bernoulli's inequality gives(1-eta)^h>=3/4.
These success bounds apply conditional on history BEFORE building
the fresh children of each trial: all their future copies are disjoint.
They are not assertions conditional on full numeric current input tables.
The restricted low-routing conditioning in Lemma10.2 includes child
construction decisions and costs; averaging it proves the stated trial
bound. Failed trials never reuse inputs.

Inductively, letE_i bound expected delivered leaf-qubit demand of
VEC(i), uniformly over histories before its fresh-copy call. E_0=lambda.
For any fixed full or final arityq_i, fresh trials give
E_(i+1)<=q_i E_i/(1-eta). Trialj starts with probability at most
eta^(j-1); its conditional expected child demand is at mostq_i E_i.
This sums nonnegative trial costs, without conditioning on success.
Thus, for the actual prefix and final arityk,

 E_h<=lambda*k*product_(i<u)fan_i/(1-eta)^h
     <=2lambda*fan_max*A_bar^m.

For the last inequality use(8.3), allfan_i>=1,k<=fan_max and
(1-eta)^h>=3/4. The expected demand ofK roots is at mostDbar.

Each accepted leaf costs at most two acquisitions in conditional
expectation. Summing over successive leaf calls, whose occurrence is
determined before each call, gives expected acquisitions at most2Dbar.
Markov againstDcap andCcap gives2^-12/n each. The real capped
process agrees until one cap fails; a union bound gives2^-11/n.
Both counters include copies from failed/discarded subtrees. QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all merge outcomes (e, Rf, bl); all search fair coins, ancilla probe outcomes,
collected tuple lists and fixed search-schedule histories; and all decisions of the controller in
that batch (FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels
depend only on the low_j, since multiples of 2^B do not change them.
The fresh search ancilla laws depend only on residue arrays belowB;
their coins are independent of the held-out top bits. By Lemmas6.1 and6.3 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs or a-tuples on disjoint
coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

### 10.1 Conditional overflow bound for a generic MERGEF call

Lemma10.2. Every actual MERGEF trial, including the final
f=1,b=0 possibility, fails with probability less thaneta=2^(1-kappa),
conditional on lower-routing history before its current residue fields.
Heref,b,s_out are the public parameters of that call andmu=2^(f lambda-b).

Proof. Let Lv be the surviving leaves of its f disjoint child inputs,
p=p_i,b=b_i,Ltab=2^lambda. Decompose k_j=l_j+2^p g_j+2^(p+b)t_j, with l_j the low
p bits and g_j the next b bits. Let Fs contain these low parts l_j,
child routing outcomes (including child search coins, ancilla probes and
tuple lists), discarded-attempt records and costs, independent
outside-copy information and previous root outcomes. EXCLUDE full stored
input labels above p, all current g_j,t_j, and LE's private records.
The cost records here mean structural source/leaf/search-schedule counts,
not full-label arithmetic traces or generated circuit descriptions. Those
fixed-width operations are charged in the worst-case work bound and are
not used for routing.
All earlier routing within the child inputs reads positions below p.
The generic Grover-list structural law shows that measured residues,
projections and rank blocks depend only on such low bits, index order and fresh
search coins. These coins are independent of the current unrevealed leaf fields.
Induction therefore leaves the g_j independent uniform modulo2^b given
Fs. The fact that high labels are physically stored does not authorize
conditioning on them. No extraction-error or cap-survival conditioning
is used in this ideal argument.

Given Fs, each tuple has a fixed incidence set I of distinct leaves
and a fixed carry floor(sum_(j in I)l_j/2^p). Different tuples have
different incidence sets, as leaf tables have all distinct bit strings,
children have disjoint coordinates and every merge reindexes injectively.
At most one tuple has an empty set. Fix a residue e and let S count
nonempty tuples whose sum has that residue. Each nonempty sum is uniform,
so E[S|Fs]<=Ltab^f/2^b=mu=2^(f lambda-b). For distinct nonempty sets
I,I', choose j in their symmetric difference (swap the sets if needed
so j in I'\I) and an i in I. With all other g fixed, the map from
(g_i,g_j) to the two residues has matrix[[1,0],[1,1]] if i in I',
and identity otherwise. It is invertible over Z/2^b. The indicators
are pairwise independent, hence Var(S|Fs)<=E[S|Fs]<=mu.

Since sz_e<=S+1 and Cp=2mu+1, overflow is at most(S-2mu)_+.
When S>2mu one has S-E S>mu and
S-2mu<=S-E S<=(S-E S)^2/mu. Thus expected overflow is
at mostVar(S)/mu<=1. Summing over the2^b possible e and dividing
byLtab^f bounds the expected discarded mass by2^b/Ltab^f=1/mu.
Lemma6.3 adds remainder failure2^s_out/mu and the uniform
missed-solution term. Since2^(kappa+s_out)<=mu ands_out>=1,
the total is at most2^-kappa+2^(-kappa-1)+2^(-kappa-8)<eta.
The pairwise argument uses only distinct nonempty incidence sets, so
it holds forf=1. Forb=0 the ring has one element, indicators are
constant and the same inequalities hold; no inversion on random
high fields is required to infer a nontrivial distribution. QED.

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
at most 2exp(-K/8192) by the two-sided form. Outside these events,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625 > (K/2) cos(pi/8) + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the maximizer is not far. There are at most 2^(Y+8)
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(2r + ceil(log2 n) + 30) <= 2^-(Y + ceil(log2 n) + 30), using Y <= 2r. The failure
probability is at most 2^(9-30)/n <= 2^-20/n. QED.

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

Finite branch (n < 2^4096). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome. Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^4096). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = n Ccap + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2 = log2 N <= n, there are at most n batches, each using at most Ccap acquisitions, plus at most K for the single wd = 1 level. So Q <= Qcap on every branch. LE is sized by this Qcap, which is computed before h_e.

Success. In the ideal run the failure events are: a batch ABORT, at most n*2^-11/n=2^-11 (Lemma9.1); a decoder error, at most 2^-20 (Lemma 11.1); and a 2-adic miss, at most n 2^-K <= 2^-40. Adding the LE coupling (5.1):

    Pr[output = s] >= 1 - 2^-11 - 2^-20 - 2^-40 - 2^-10 >= 1 - 2^-8 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings; there is no conditioning on favorable labels or outcomes.

## 14. Cubic classical space and weighted branchwise work

Section8 provesQcap=nCcap+K<=2^(x/2),x=sqrt n. FIND acquires
no source copies. The generic instrument, fresh-child recursion and
Dbar preserve all batch-abort and full-secret bounds ofSections9-13.

Quantum. Pending vector siblings useO(lambda*sum_i fan_i)=O(n)
qubits. A finish or search requiresO(fan_max lambda)=O(xL)<=O(n)
reusable scratch. Source/LE, rank/projection and abort cleanup fitO(n).
Every search releases scratch before the next, including failed trials.

Classical. lambda=ell gives2^lambda=O(n). There are
O(sum_i fan_i+fan_max)=O(n) retained full-label tables, each
O(n*2^lambda)=O(n^2) bits, givingO(n^3). Only the current merge
keeps its tuple list:Cp=2^(lambda+kappa+1)+1=O(n^(3/2)/L),
U=O(xL), soCp*U=O(n^2). Current input/sort/residue arrays need
O(fan_max*n*2^lambda)=O(n^(5/2)). The complete primitive/decoder
ledger carried by the direct source remainsO(n^2): counters, caps,
labels and arithmetic haveO(n)-bit fields, LE usesO(n) scratch,
K=O(sqrt n) decoder records haveO(n) bits, and candidates and
circuit instructions are streamed with reused arithmetic scratch.
The stack, profile andO(ell^3)-bit power/precision arithmetic fit
O(n^2), with no full tree, truth table or
exponential circuit. JointlyS_C=O(n^3) on EVERY actual branch.

Time. At full leveli the generic MERGEF costs at most
poly(n)*2^(fan_i lambda/2+2lambda), charging all2^kappa factors,
serial lookup/list exclusion, verification, circuit/address generation,
arithmetic, measurements and reset. LetP_i=product_(0<=j<=i)fan_j.
Each STARTED attempt at the SAME level consumes at leastlambda*P_i
delivered leaves disjoint from those of the other attempts. No failed
input is reused. Henceattempts_i<=Qcap/(lambda*P_i).
Aborted calls that have not completed children pay no merge search;
construction and cleanup charge to consumed copies and at mostm+1
pending frames. Summing levels, full work is up to a fixed polynomial
 max_(0<=i<m)2^(x/2+fan_i lambda/2-sum_(j<=i)log2fan_j). (14.1)
This is deterministic on every branch. Source/LE, leaves, arithmetic,
unfinished frames, generation and cleanup addpoly(n)*Qcap or a
polynomial multiple of the same bound, with no free lookup/QRAM.

Uniformly the literal formulas imply
 m=x/L*(1+O(1/L^2))+O(L),lambda=L+O(1),
 A_bar=x*(1+O(1/L)),fan_min=x*(1+O(1/L)),
 center=m/2+O(1),m lambda=x+O(x/L)+O(L^2).
In particularlog2fan_min=L/2+O(1/L). For EVERYi<m,
 fan_i lambda/2-sum_(j<=i)log2fan_j
 <=A_bar lambda/2-m lambda/4
     +i*(lambda/2-log2fan_min)+O(L)
 <=A_bar lambda/2-x/4+O(x/L)+O(L^2).              (14.2)
The i coefficient isO(1),i=O(x/L), so this is uniform over the
entire profile. A_bar lambda<=n/m+kappa+3lambda and(8.1) give
 n/m<=xL+O(x/L)+O(L^2).
Consequently for an absoluteC,
 log2(T/C)<=xL/2+x/4+O(x/L)+O(L^2)
          <=xL/2+x/4+2xL^(-1/2)
eventually, uniformly over integer input lengths. Indeedx/L andL^2
are both o(xL^(-1/2)). This eventual positive gap absorbs EVERY
fixed polynomial work/addressing cost and level count. No unspecified
polynomial factor is left outside the pure three-term envelope.

Finishes. Foru<m every started tail consumes at leastlambda*k times
the preceding fan-in product in leaves. Forlambda>=3 the function
k lambda/2-log2k increases at every positive integerk, because its
next difference is>=lambda/2-1>0. Withk<=fan_u its work per leaf
is at most the full-slot exponent(14.1) at indexu. Foru=m,R=0,k=1;
all such final work costs at mostpoly(n)*Qcap. Failed and discarded
finishes count. Each earlier main length has finite literal counters;
the finite prefix changes only absolute outside constants. Jointly,
 T=O(2^((1/2)sqrt nlog2n+(1/4)sqrt n+2sqrt n(log2n)^(-1/2))), S_C=O(n^3),
 S_Q=O(n),Q=O(2^((1/2)sqrt n)), full-secret success at least1-2^-8.

## 15. Exact growth indices and comparison

Time2^((1/2)sqrt nlog2n+(1/4)sqrt n+2sqrt n(log2n)^(-1/2)) has exact growth index1/2;
classicaln^3 and quantumn have index0. Source2^((1/2)sqrt n)
has index1/2. All structured objects match; only time scores[1/2].
Against LLV-GBR200 the same source/qubit/error envelopes are retained,
classical degree rises2 to3, and the positive time correction falls
from2sqrt n(log2n)^(1/4) to(1/4)sqrt n+2sqrt n(log2n)^(-1/2). Against the earlier period-six
pure-time configuration, space degree is smaller and time is larger.
These are algorithmic tradeoffs, not four-resource dominance claims.
No priority, optimality, practical speed or cube-root growth is claimed.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope

Variable arity gives polynomial classical space with growth index0 and time
index1/2, source coefficient1/2 and linear quantum workspace. Time
is slower than fixed-arity sqrt n exponentials; classical workspace
has a larger declared polynomial degree than the GPS n^2 family. No optimality,
positive robustness, practical performance or priority is claimed.
