# LLV-G125GPA: precision equal to arity sharpens the lower terms

## 0. Joint theorem and growing integer precision

For everyN>=2 ands inZ/NZ,n=ceil(log2N), the single LLV-G125GPA
algorithm below recovers the entire secret with unconditional probability
at least1-2^-8 from independent ideal copies. On EVERY branch jointly

 T=O(2^((1/8)sqrt nlog2n+(1/2)sqrt n+(5/8)n^(3/8)log2n+4n^(3/8))),
 S_C=O(2^((1/4)n^(3/8)log2n+(1/4)n^(1/4)log2n+7n^(1/4))),S_Q=O(n),
 Q=O(2^((1/2)sqrt n)).

All outside constants are absolute. Indices are[1/2,3/8,0,1/2].
Fractional tolerance is zero under the canonical independent-ideal-copy
promise. The finite exhaustive branch is n<2^4096. Otherwise compute
v=floor sqrt n,r=ceil sqrt n,ell=ceil log2n,a=ceil(n^(1/8)),
P_prec=a,B_src=floor(v/2)-a-100ell,
H_prec=ceil log2(a^P_prec),m=floor(P_prec*B_src/H_prec),
kappa=ceil log2(m+a)+3,lambda=ceil((n+m*kappa)/(m*(a-1))).
The aritya is the least integer whose eighth power reachesn,
computed by integer binary search; P_prec=a is an exact alias. H_prec=bit_length(a^P_prec-1).
All parameters use exact integer arithmetic from the known modulus.
Section8 gives a polynomial-cost implementation and optional exact
power-of-two shortcuts. There is no real-log oracle.

Notation. n=bit_length(N-1),dn=bit_length(N)-1, wherebit_length(x)
is the unique positivek with2^(k-1)<=x<2^k forx>=1. Computea2 by
repeated division by2 until the quotientM is odd;N=2^a2 M.
Putomega=exp(2 pi i/N). For analysis only,s1=s modM and the unique
s2 in[0,2^a2) satisfies s=s1+M s2 modN. These unknowns are recovered
by the decoders, not supplied as secret-dependent computations.
All logarithms below are base2 unless writtenln.

## 1. Provenance and precision equal to arity

Direct proof-text and framework source: my LLV-G125GP prototype,
proof SHA-256 5d9e367600722f95aaf44e2f2a298d17f1942046f97e2c380a347840051f88de.
Its final public mapping appears in the note/dependency declaration.
It supplies the complete fixed-schedule Grover-found classical fiber
list, exact rank/flag/block instrument, uniform miss bound, conditional
incidence and source-demand arguments, integer source/capacity budget,
binary finishing, source-only primitives, capped recursion, all-modulus
decoders and charged resource ledger. All upstream credits remain,
including GPS-WQLOG's Grover primitive. DS7's discarded enumeration
cutoff remains research context only. No previous judgment is a premise
or certified ancestry.

The actual logarithm precision is now P_prec=a, rather than a
sixteenth-root integer. This recomputes the literal depth and table
length and reduces the logarithm error to below1/a. Section14 also
retains more terms in the capacity expansion and uses the tighter
exact work identity (a+4)/2=(a-1)/2+5/2. Both displayed lower-order
time and classical-space envelopes improve eventually; the source,
qubit, leading growth indices and clean-copy promises are retained.
This is an upper-bound improvement, not optimality or practical timing.

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

IDEAL run. The ideal run is LLV-G125GPA in the latent-label model with every LE output replaced by the
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

### 6.4 MERGEA: a bounded Grover-found classical fiber list

This routine is used ONLY at full a-input levels: all input and output
log lengths equal the global lambda. Inputs are a disjoint phase
vectors of lengthLtab=2^lambda, collimated top, with full labels
label_t[x]=c_t+2^p h_t[x],0<=c_t<2^p. Set

 b=(a-1)lambda-kappa>=1,U=a lambda,M_dom=2^U,
 mu=M_dom/2^b=2^(lambda+kappa),Cp=2mu+1,
 ellCp=ceil log2(Cp+1),J=kappa+ellCp+8.

Section8 proveslambda>=kappa+2,a>=4,U=O(n),kappa=O(logn),
soCp<=2Ltab² andCp+1<=M_dom. LetA_t[x]=h_t[x] mod2^b and
car=floor(sum_t c_t/2^p). Only residues belowp+b are used.

1. Initialize a b-bit accumulator tocar mod2^b. For each inputt,
   LOOKUP A_t[x_t] into a reused b-bit temporary, add it modulo2^b,
   and uncompute the temporary. Measure the accumulator as e and
   clear it. The original indices now hold the uniform-magnitude
   fiberS_e of sizeF>=1, with their original phases. Settau=(e-car) mod2^b.
2. Start an empty CLASSICAL tuple listTl. For at mostCp+1 calls,
   stopping earlier when|Tl|=Cp, runFIND(P,J) on fresh U-bit ancillas:

       P(x_1,...,x_a)=[sum_t A_t[x_t]=tau mod2^b]
                     AND[(x_1,...,x_a) is not inTl].

   Append only verified returned tuples. OnNONE stop listing and
   proceed to rank projection; NONE is not automatic merge failure.
   No FIND gate acts on any original phase index. In particular,
   all search units on EVERY branch are bounded by

          8J(Cp+1)2^ceil(U/2).                       (6.4)

   No expected-search estimate or enumeration-time cutoff is used.
3. ScanTl to compute unique list rankR and membership flagRf on the
   ORIGINAL a index registers using reversible equality tests. The
   tuples are distinct by verified exclusion. MeasureRf; FAIL if zero.
4. Measurebl=floor(R/2^lambda). FAIL if(bl+1)2^lambda>|Tl|.
5. LOOKUP the selected2^lambda tuples to XOR-clear the original
   indices, reset flags/high rank bits, and return the lowlambda
   rank bits with their full-label SUMS. All output labels agree
   modulo2^(p+b).

On FAIL discard/reset all inputs and ancillas; inputs are not reused.
Successful output is always an EXACT phase vector: FIND acts on a
fresh tensor factor conditional on known tables,e and list; rank/block
projections and injective reindexing retain exactly the original phases.
This holds even after prematureNONE, since every collected tuple is
verified and distinct. List order need not be lexicographic.

Explicit cost. Decode theU-bit search candidate into a lambda-bit
index per table. Serial LOOKUP scans eachLtab-row classical array,
using reversible equality and XOR into a reused b-bit temporary.
Add into a modular accumulator. ScanTl for exclusion; distinctness
allows XOR of equality flags, using reusedO(U) scratch. Combine
the flags, applyZ and uncompute. Each oracle, reflection, trial setup,
verification, copying, measurement/reset and address action costs a
FIXED poly(n)*(Ltab+Cp) gates/bit operations. Since actual2^kappa
is polynomial inn, this ispoly(n)*2^lambda. No exponentially long
circuit description is stored; gates are generated serially and charged.
Search scratch isO(U+b)=O(a lambda)=O(n), reused per trial; no
source acquisition or subtree construction occurs inside an oracle.
Classical arrays, lists and schedules usepoly(n)*2^lambda bits.

Lemma6.3. For ANY fixed tables and measured e, prematureNONE while a
solution remains has probability at most2^(-kappa-8). Outside that
event,tl=|Tl|=min(F,Cp), and

 Pr[mergeFAIL | tables]
 <=2^-kappa+sum_e(F_e-Cp)_+/M_dom+2^(-kappa-8).        (6.5)

All structural laws depend only on residue arrays, index order and fresh
search outcomes/coins, not on higher label bits or original phases.

Proof. There are at mostCp+1 calls. Lemma6.2 andJ=kappa+ellCp+8
bound the union of nonempty-call misses by(Cp+1)2^-J<=2^(-kappa-8),
uniformly for all tables/e and preceding lists. Without such a miss,
listing stops atCp distinct solutions or after finding allF solutions.
For a list oftl distinct solutions, original-fiber flag failure is
(F-tl)/F and complete-block rejection contributes(tl mod2^lambda)/F,
independently of which tuples were selected. Add the uniform miss bound
pointwise; multiply byF/M_dom and sume. Block remainders total at
most2^b2^lambda/M_dom=2^-kappa, and truncation is the displayed sum.
No favorable-outcome conditioning or independent-table-entry assumption
is used. QED.


## 7. Leaf qubits

A LEAF QUBIT is a phase vector of length 2 with table (0, k), for its known label k: a positive qubit whose state in the ideal run is (|0> + exp(2 pi i k th)|1>)/sqrt 2, up to global phase, for a fixed real th. There is no pairing stage in this algorithm; leaf qubits go directly into leaf tables.

## 8. Exact budget with a growing-precision logarithm bound

For n>=2^4096 use Section0 and

 Dbar=2^a K lambda*a^m,Dcap=2^12 nDbar,Ccap=2^13 nDbar.

LetY be least with2^Y>=Ccap. PutL=log2n,x=sqrt n,t=n^(1/8),
s_prec=t,andh_log=H_prec/P_prec for analysis only. Then
x=t^4,L>=4096,x-1<=v<=x,r<=x+1,t<=a<=t+1,
s_prec<=P_prec<=s_prec+1,L<=ell<=L+1, and

 log2a<=h_log<log2a+1/P_prec,
 L/8<=h_log<=L/8+2/t+1/s_prec<=L/4.

Here ln(1+1/t)<=1/t and1/ln2<2 bound the rounded root logarithm.
Define delta=2a+200ell+2h_log+2=O(t+L). The floor rules give

 (x-delta)/(2h_log)<=m<=x/(2h_log).

AtL>=4096,t>=2^512; as in the explicit exponential-to-polynomial
threshold comparisons,delta<=x/2 andt>=3L. Hencem>=x/(4h_log)>=1,
m+a<=r andkappa<=ell. The exact capacity ceiling yields

 h_log*t^3<=lambda<=8h_log*t^3+2ell/t+1<=3L*t^3<=x<=r,
 lambda>=(a-2)kappa+1.

The lower bound(L/8)t^3 exceeds2t(L+1)+1, proving the last
inequality. Thus all primitive lengths, binary widths and search
registers obey their required polynomial dimension bounds.

Uniform integer implementation. Compute a^P_prec by binary exponentiation
andH_prec=bit_length(a^P_prec-1). The largest intermediate integer has
O(P_prec loga)=O(n^(1/8)logn) bits; there areO(logP_prec)=O(logn)
schoolbook multiplications. This is fixed polynomial work and classical
memory in input lengthn, fully charged before source acquisition. It
requires no approximate logarithm or uncounted arithmetic oracle.

Optional exact shortcuts. Putj=bit_length(a)-1. Ifa=2^j,
H_prec=j*a. Ifa=2^j+1 andj>=2,H_prec=j*a+2. To prove the
second formula, writeu=2^j>=4. Integrating1/v on[1,1+1/u]
gives1<(u+1)ln(1+1/u)<1+1/u<=5/4. Also ln2<1 and
ln2>2/3: integrate1/v+1/(3-v)>4/3 on[1,3/2), with equality
only at the endpoint. Thus ln2<(u+1)ln(1+1/u)<2ln2,
so 2^(j*a+1)<a^a<2^(j*a+2). The ceiling logarithm is j*a+2.
Otherwise ordinary binary exponentiation computes the same exact
integer. These shortcuts use no approximate logarithm oracle.

Letcfull=(a-1)lambda-kappa. By the ACTUAL table ceiling,

 m*cfull>=n exactly.                                 (8.1)

For1<=B_req<=n takeu=floor(B_req/cfull)<=m full a-input levels,
widthcfull and output loglambda. Allocate the remainder amonga-1
binary finishing levels, a-2 of maximumlambda-kappa and one of maximum
2lambda-kappa-1, greedily from the last level down. Their total
a lambda-(a-1)kappa-1>=cfull. The actual height ish_tree=u+a-1
(denotedh locally in TREE); prefix sums end atB_req. No a-input
width is trimmed; all binary widths meet the failure inequality.

For source arithmetic,K<=2^15r andlambda<=r imply
log2(nCcap+K)<=m log2a+a+6L+50. The EXACT depth rule gives

 mH_prec<=P_prec*B_src,
 log2(nCcap+K)<=mH_prec/P_prec+a+6L+50
               <=B_src+a+6L+50<=floor(v/2)<=sqrt n/2.  (8.2)

ThusQcap<=2^((1/2)sqrt n) on EVERY main input. In particular
Y<=2r<=n,2^Y<=2Ccap. All caps have polynomial bit lengths. The
finite exhaustive branch changes only absolute outside constants.


## 9. BATCH(supplier, B)

Input: a supplier of leaf qubits, where in the ideal run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch has a counter of source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs.

TREE. VEC(0)=LEAF obtains lambda independent supplier qubits,
counting each before request againstDcap, and constructs their subset
label table. VEC(i+1) repeatedly builds f_i fresh VEC(i) outputs on
disjoint source copies, then usesMERGEA(p_i,b_i,lambda_(i+1),kappa)
whenf_i=a, otherwise the binaryMERGE. On FAIL all inputs are discarded
and the next trial obtains fresh children. A root isVEC(h), evaluated
depth first, and a batch requestsK roots.

Root. VEC(h) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma9.1 (no abort). In the ideal run a batch aborts with
probability at most2^-11/n.

Proof. Lemma10.2 below bounds each a-input trial's failure,
averaged over its untouched current residues, byeta=2^(1-kappa).
Binary failure is at most2^-kappa<=eta. Sinceeta<=1/[4(m+a)]
and heighth<=m+a-1, Bernoulli's inequality gives(1-eta)^h>=3/4.
These success bounds apply conditional on history BEFORE building
the fresh children of each trial: all their future copies are disjoint.
They are not assertions conditional on full numeric current input tables.
The restricted low-routing conditioning in Lemma10.2 includes child
construction decisions and costs; averaging it proves the stated trial
bound. Failed trials never reuse inputs.

Inductively, if E_i bounds expected delivered leaf-qubit demand of
VEC(i) uniformly over histories before its fresh-copy call, then
E_0=lambda and E_(i+1)<=f_i E_i/(1-eta). Indeed trial j is
started with probability at mosteta^(j-1), and its conditional expected
child demand is at mostf_i E_i. Summing the nonnegative trial costs
proves the recurrence without conditioning on a trial's success.
Thus E_h<=lambda * a^u*2^(a-1)/(1-eta)^h<=2^a lambda * a^m,
and K roots have expected demand at mostDbar.

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

### 10.1 Conditional overflow bound for an a-input level

Lemma10.2. Every ideal a-input trial fails with probability at most
2^-kappa+2^(-lambda-kappa)+2^(-kappa-8)
<2^(1-kappa), conditional on its low-routing
history before revealing its current residue fields.

Proof. Let Lv be the surviving leaves of its a disjoint child inputs,
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
The binary and Grover-list structural-law statements show that measured residues,
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
so E[S|Fs]<=Ltab^a/2^b=mu_a=2^(lambda+kappa). For distinct nonempty sets
I,I', choose j in their symmetric difference (swap the sets if needed
so j in I'\I) and an i in I. With all other g fixed, the map from
(g_i,g_j) to the two residues has matrix[[1,0],[1,1]] if i in I',
and identity otherwise. It is invertible over Z/2^b. The indicators
are pairwise independent, hence Var(S|Fs)<=E[S|Fs]<=mu_a.

Since sz_e<=S+1 and Cp=2mu_a+1, overflow is at most(S-2mu_a)_+.
When S>2mu_a one has S-E S>mu_a and
S-2mu_a<=S-E S<=(S-E S)^2/mu_a. Thus expected overflow is
at mostVar(S)/mu_a<=1. Summing over the2^b possible e and dividing
byLtab^a bounds the expected discarded mass by2^b/Ltab^a=2^(-lambda-kappa).
Lemma6.3 adds remainder failure2^-kappa and the uniform
missed-solution term. Since lambda>=1, their sum with the overflow
is less than2^(1-kappa). This proves the bound
on each fresh trial after averaging Fs, without fixing full high labels
or the actually measured e. QED.

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

## 14. Every-branch resources and the eighth-leading time term

The literal source budget and caps are UNCHANGED fromSection8, so
Q<=nCcap+K<=2^((1/2)sqrt n) on every main branch. Section9's demand
proof uses the SAMEeta=2^(1-kappa), established for the new instrument
inSection10.1. No extra source copies are used by ancillary searches.

Quantum. Retained siblings and finishing/current phase registers use
O(m*a*lambda+a lambda)=O(n), by the exact capacity ceiling as before.
Each search usesU=a lambda<=O(n) additional qubits, withO(U+b)
reused oracle/reflection scratch. Rank/projection and source transforms
also fitO(n). No trial's ancillas survive to another trial. Hence
S_Q=O(n), including every search-miss and source-abort branch.

Classical. Retained full-label tables, residue arrays, bounded tuple
lists, search schedules, source/counter fields, decoder records and
extraction scratch fitpoly(n)*2^lambda bits. Growing-precision integer
preprocessing uses only polynomial space and is included. No complete
recursion tree, oracle truth table or exponential circuit description is
stored. All addresses and generation work are charged.

LetL=log2n,x=sqrt n,t=n^(1/8). HereP_prec=a>=t, so
Section8 givesh_log<=L/8+3/t. Withdelta=O(t+L),

 n/m<=2h_log*x+4h_log*delta
     <=(1/4)t^4 L+6t^3+O(Lt+L^2).                 (14.1)

The capacity ceiling giveslambda<=(n/m+kappa)/(a-1)+1.
Use1/(a-1)<=1/(t-1)=1/t+1/t^2+O(1/t^3) to obtain

 lambda<=(1/4)t^3 L+(1/4)t^2 L+6t^2+o(t^2).

For example the remainingtL,L,L^2/t andt terms are allo(t^2).
Fixed polynomial storage factors addO(logn)=o(t^2) to the
exponent. The positive unit gap7-6 proves

 S_C=O(2^((1/4)n^(3/8)log2n+(1/4)n^(1/4)log2n+7n^(1/4))).

Time. Equation(6.4) bounds ALL searches in one attempt. Including the
charged serial lookup/list-exclusion cost per unit, each a-input attempt uses

 poly(n)*2^(((a+4)/2)lambda)

charged gates/bit operations on EVERY branch. The factor2^lambda
for serial table lookup and list exclusion is INCLUDED: no unit-cost
oracle, QRAM or uncharged circuit-generation assumption is used.
IndeedCp=poly(n)*2^lambda, so the fixed call count contributes one
2^lambda factor and serial lookup/list exclusion another. All2^kappa
factors,J,U and parameter arithmetic are polynomial inn.

Charge each level-(i+1) attempt to at leasta^(i+1)lambda distinct
delivered leaves. Summing the uniform geometrica^-i count, accounting
for all failed children, pending frames, a-1 finishing binary levels,
leaf tables, source/extraction, decoders, addresses, gate generation,
initialization, measurement, resets and abort cleanup gives, for fixedC,k,

 T<=C n^k 2^a a^m 2^(((a+4)/2)lambda).              (14.2)

The ENTIRE2^(a-1) binary-finishing leaf factor is inDbar. Partial
frames add only polynomial bookkeeping; prior work is charged to
consumed acquisitions/leaves, never to expected-only success.

For time retain the tighter exact identity

 ((a+4)/2)lambda=((a-1)/2)lambda+(5/2)lambda
 <=(1/2)(n/m+kappa+a-1)+(5/2)lambda.

By(14.1),half ofn/m is at most(1/8)xL+3t^3+o(t^3).
The classical estimate gives(5/2)lambda<=(5/8)t^3 L+o(t^3),
since t^2L=o(t^3). Also kappa+a=o(t^3). Hence

 ((a+4)/2)lambda<=(1/8)xL+(5/8)t^3 L+3t^3+o(t^3).

The source prefactorm log2a+a<=x/2, and any fixed polynomial
work addsO(logn)=o(t^3). Taking logs in(14.2),

 log2(T/C)<=(1/8)xL+(1/2)x+(5/8)t^3 L+3t^3+o(t^3).

The explicit unit gap4-3 absorbs the remainder beyond a fixed
threshold. Earlier main inputs are finite and have literal finite
caps; they change only the absolute outside constant. Jointly,

 T=O(2^((1/8)sqrt nlog2n+(1/2)sqrt n+(5/8)n^(3/8)log2n+4n^(3/8))),
 S_C=O(2^((1/4)n^(3/8)log2n+(1/4)n^(1/4)log2n+7n^(1/4))),S_Q=O(n),
 Q=O(2^((1/2)sqrt n)).

All bounds hold on every branch, with unconditional full-secret success.


## 15. Exact growth indices and comparison

Time is led by(1/8)sqrt nlog2n, so its exact growth index is1/2.
Classical space is led by(1/4)n^(3/8)log2n, giving exact index3/8.
Sources have index1/2 and linear quantum space index0. The exact
structured objects match these expressions; only time scores[1/2].

The parent's2n^(7/16) time correction exceeds the present
(5/8)n^(3/8)log2n+4n^(3/8) eventually by an unbounded amount.
Its3n^(5/16) space correction similarly exceeds the present
(1/4)n^(1/4)log2n+7n^(1/4). Thus both envelope ratios tend to
zero. All other envelopes and the error model are identical. This
is an upper resource-bound improvement, without optimality or
practical timing claims.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope

Variable arity gives a classical-space growth index3/8 with time
index1/2, source coefficient1/2 and linear quantum workspace. Time
is slower than fixed-arity sqrt n exponentials; classical workspace
is larger than the polynomial-space GPS family. No optimality,
positive robustness, practical performance or priority is claimed.
