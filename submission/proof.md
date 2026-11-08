# LQF-SK: streaming pairing under a sample budget, T = O(n^5 log2(n) 2^F(n)), Q = O(n^3 2^((1/4) sqrt(n)/log2(n))), S_Q = O(n)

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm LQF-SK below receives N in binary and fresh
independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch
(every failure, discard and abort included) it satisfies jointly

    T = O(n^5 log2(n) 2^F(n)),  S_C = O(n^(3/2) 2^F(n)),  S_Q = O(n),  Q = O(n^3 2^((1/4) sqrt(n)/log2(n))).

For n=1 only, evaluate every displayed logarithmic resource envelope
at n=2; this finite positive extension leaves its asymptotic structured
form unchanged. Here F(n)=4sqrt(n)log2(n)+(1/8)sqrt(n)/log2(n).
All constants are absolute. Time, classical space and samples have growth index1/2; the quantum envelope n has index0 (Section15). The fifth claim is the clean-input
tolerance 0 (Section 16). The sharper main-branch bounds, from which these follow, are in Section 14. The envelope coefficients are fixed
exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters for n>=2^48 are computed exactly; ell is rational
and the remaining parameters are integers:

    r=ceil(sqrt n), ell=RLOG(n) from8.0, m=ceil(r/(4ell)),
    kappa=ceil(log2m)+1, dl=ceil((n+1+m*kappa-m(m-1)/2)/(m+1)), H=dl+m-1,
    u=ceil(log2n), K=2^13(m+10u+100).

There is no recycling stage or table-width cap. The binary tree has widths
lambda_i=dl+i for0<=i<m and lambda_m=1. Its depth becomes smaller
as its initial leaf width grows. All table lookups are implemented scans.

## 1. Provenance and exact change

The direct source is my QLC-14255, submission
3ca00587-2350-4943-8f32-ff05b08b024a, candidate
bf11874b13c807b6ce65a2130298063108be892e. The exact source transforms,
translation-test label extractor, general binary merge, direct supplier,
full-secret decoder and deterministic stopping framework are reproduced.
Their earlier framework ancestry includes SPQ-1408,SPQ-14021,STRIAD,SWF,
SWFC,CW1310/CW1,SPC-127,HPC-127,SPC-138,CS1 and Kuperberg, as credited
by those proofs. No earlier verdict is a correctness premise.

The new configuration replaces fixed square-root coefficients with a
logarithmically growing initial width and a reciprocal-logarithmic depth.
An exact minimal-width formula saturates the available binary capacity.
The root count is fixed from the actual depth and log n, with the new
concentration margin proved explicitly, reducing unnecessary log factors.
A rational log approximation avoids the extra4sqrt(n) term introduced
by rounding log2n to its ceiling. The intermediate LQF-4F and LQF-4R drafts were used
as a development template; it is not a mathematical premise.
Section8 gives an exact rational logarithm routine and elementary capacity argument, Section14 charges
operations on the wider labels and all live quantum registers, and
Section15 derives supported log-power resource envelopes. This is a
sample/time/classical-space tradeoff, not a new merge instrument or growth
class. No four-input merge, QRAM, recycling bank or additional oracle is used.

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

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(sqrt n) (Section 14),
this is O(n^(5/2)) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL run. Execute this same LQF-SK algorithm but replace each LE
output by its latent labelk. Actual and ideal runs can be coupled until
the first incorrect label, whose probability is at most2^-10 by(5.1).
There are no additional ancilla-preparation trials. Every resource bound
is for actual branches, using fixed caps and allocations.

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

Cost. Write E=2^lam,E'=2^lam'. Here lam,b=O(r ell),
r²=O(n). Explicit lookups have O(r ell) gates per row. Merge-sort
uses O(E log E) comparisons of O(r ell)-bit keys, costing
O(n ell²E). Binary searches and rank arithmetic obey the same bound;
preprocessing and selected3n-bit labels add O(n(E+E')) steps.
Thus O(n ell²(E+E')) core steps and O(n(E+E')) classical bits suffice.
Quantum scratch is O(r ell)<=O(n) beyond input index registers.
These costs include table preprocessing and generation of every lookup.

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
scratch, and K=O(sqrt(n)/log2(n)) root qubits. Section14 gives its uniform size bound.
A classically addressed free-handle stack or equivalent known recursive
wire layout permits reuse with O(n)-bit bookkeeping per allocation, within
the charged ledger. No exponential register bank is allocated. Classical
tables are looked up by the explicit Section6 scan circuits, not QRAM.

## 8. Rational-logarithmic depth, exact capacity and budgets

### 8.0 RLOG(n): an explicit rational lower approximation

Put j=floor(log2n),u=ceil(log2n),t=2u+10, and
z=(n-2^j)/(n+2^j), so0<=z<1/3. Define exact rationals

    A(x)=2 sum_(v=0)^(t-1) x^(2v+1)/(2v+1),
    delta=3^(-2t),
    RLOG(n)=j+A(z)/(A(1/3)+delta).

For0<=x<=1/3, the power-series identity
ln((1+x)/(1-x))=2sum_(v>=0)x^(2v+1)/(2v+1)
follows by integrating the uniformly convergent geometric series on
[0,1/3]. The omitted tail is at most
2x^(2t+1)/((2t+1)(1-x²))<=3^(-2t)=delta.
Thus Az<=ln(n/2^j)<=Az+delta and A2<=ln2<=A2+delta,
where Az=A(z),A2=A(1/3)>=2/3. Also Az<=ln2<1. Consequently

    j+Az/(A2+delta)<=log2n<=j+(Az+delta)/A2,
    0<=log2n-RLOG(n)<=4delta<=1/n².                  (8.0)

The last inequality uses delta<=2^(-2t)<=2^(-4u-20)<=2^-20/n^4.
All powers, sums and quotients here are rational and computed exactly.
There are O(log n) terms with O((log n)²)-bit common denominators;
ordinary schoolbook rational arithmetic costs poly(log n) core steps
and poly(log n) classical bits. That memory is O(n) and the work is
polynomial in n, with absolute constants. No real-number or logarithm
oracle is supplied. In the main range1<=ell=RLOG(n)<=log2n<=r.

Set Dbar=3Kdl2^m,Dcap=2^12nDbar,Ccap=2^13nDbar,
Y=ceil(log2Ccap). All are fixed before acquisitions.
Throughout the main range, r>=4u(10u+100), so m>=10u+100
and K<=2^14m. To check the first inequality, use u<=2log2r+1;
the corresponding continuous inequality holds at2^24 and its
left-minus-right derivative is positive thereafter.
Also m<=r/(4ell)+1<=r/4+1 and kappa<=log2r+2.
The capacity bounds below show dl<=5r ell,H<=5r ell.
Since m<=r/(2ell) and r²<=2n on this range,

    Kdl<=5*2^14n,
    Ccap<=15*2^27n²2^m,
    Y<=m+2u+32<=r/4+4log2r+35<=r/2<=2r-1.          (8.1)

Hence Y<=2r<=n and2^Y<=2Ccap; counters and full label fields
have the sizes used below. Crucially the root count was fixed using
m,u, not the later Y, yet it satisfies

    K/2^13=m+10u+100>=Y+u+30.                         (8.1a)

That inequality will replace the predecessor's looser2r-based root
count in the concentration proof. It does not assume an oracle or solve
a circular definition. All integers are computed directly.

Put lambda_i=dl+i for0<=i<m,lambda_m=1 and
bmax_i=2lambda_i-lambda_(i+1)-kappa. The exact capacity is

    Sum(m)=(m+1)dl+m(m-1)/2-1-m*kappa.                    (8.2)

The prescribed dl is the SMALLEST INTEGER with Sum(m)>=n;
indeed n<=Sum(m)<=n+m by the ceiling definition. All maxima are
nonnegative: m<=r/2,r²<=2n,kappa<=n/2 imply m²+kappa<=n,
so n+1-kappa-m(m-1)/2>0 and the numerator definingdl exceeds
(m+1)kappa. Thus dl>=kappa+1. These inequalities hold throughout
the main range, including its endpoint.

For later estimates, r>=8ell: ell<=log2n<=2log2r and
16log2r<=r for r>=2^24. Also r²<=2n follows from
n>=(r-1)²+1 on this range. Thus m+1<=r/(2ell), while
m>=r/(4ell). The ceiling formula gives

    n/(m+1)-m/2<=dl<=n/(m+1)+kappa-m/2+2.              (8.3)

As n>=r²/2 and m<=r/(2ell), this shows dl>=r ell/2.
Also dl<=4r ell+kappa+2 and H<=5r ell by the elementary
main-range inequalities already used. Hence dl=Theta(r ell),
which will justify the per-level work sum; no fixed coefficient is
substituted into an exponent without the rounding proof below.

For B<=n allocate exactlyB bits b_i greedily from root to leaves,
bounded by bmax_i. Put tp_0=0,tp_(i+1)=tp_i+b_i. Then tp_m=B, all residue reads are belowB,
and b_i+lambda_(i+1)-2lambda_i<=-kappa. The binary merge lemma
bounds each attempt's failure by2^-kappa for arbitrary input tables,
including zero-width windows and partial budgets. All allocations and
counter caps are fixed before source access.


## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch starts with a zeroed counter of
source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs. At its end, unused tree/index scratch is reset and released.

TREE. VEC(0) = LEAF: request dl qubits by calling NEXT(0) dl times, counting each in a counter D; if D would exceed Dcap, ABORT. These qubits form
the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The
table has length 2^dl, is exactly the tensor product state in the ideal run, and is collimated to tp_0=0.
VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until out != FAIL; return out. A root is VEC(m),
evaluated depth-first. Run it K times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap
leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a
batch ABORTs with probability at most 2^-12/n + 2^-11/n.

Proof. In the ideal run each merge has conditional failure probability
at most2^-kappa for arbitrary input tables. With tt=2^kappa/(2^kappa-1),
a root's expected leaf demand is at most(2tt)^m dl. Because2^kappa>=2m,
tt^m<=exp(m/(2m-1))<=e<3. Thus E[D_inf]<=Dbar for K roots and the
demand-cap failure probability is at most2^-12/n.

Stop the uncapped process when it finishes or the acquisition counter
reachesCcap. The number of accepted delivered qubits is at mostD_inf;
there is no intervening stream. Conditional acceptance probability of each
acquisition is at least1/2. Bounded stopping of its accepted-count sum
therefore gives expected acquisitions at most2E[D_inf]<=2Dbar.
Markov against Ccap gives at most2^-12/n, hence certainly at most2^-11/n.
The real process agrees until a source or demand cap triggers. All these
arguments concern bounded stopped sums, not an unbounded-runtime assumption.
QED.

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
By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs on disjoint
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

    K = 2^13 (m + 10u + 100), u=ceil(log2n).                                              (11.0)

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
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(m+10u+100) <= 2^-(Y+u+30), using8.1a. The failure
probability is at most 2^(8-30)/n <= 2^-20/n. QED.

The hypothesis for stage j+1 is the conclusion of stage j, since 2^-(j+3) = rad_(j+1). By induction, with probability at least
1 - 2^-20, theta is within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M.

The chosen K>=u+40 also gives n2^-K<=2^-40, as used for parity misses.

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

Finite branch (n < 2^48). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. This branch acquires at most N(n+10) copies. Its resources are bounded by an absolute constant over this finite range; the exact main-branch cap below is not asserted here.

Main branch (n >= 2^48). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = n Ccap + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2 = log2 N <= n, there are at most n batches,
each using at most Ccap acquisitions, plus at most K for the single wd = 1 level. So Q <= Qcap on every branch. LE is sized by this Qcap, which is computed before h_e.

Success. The failure budgets are batch aborts2^-12+2^-11,
odd decoding2^-20, parity missesn2^-K<=2^-40, and label-extraction
coupling2^-10. Their total is less than2^-8. There is no FW or PREP
subroutine or additional corresponding error. The finite branch has
failure at most2^-10. Thus entire-secret recovery succeeds with probability
at least1-2^-8 for everyN,s. Resources below are direct all-branch bounds,
not conditioned on this success event.

## 14. Resource bounds on every branch

All counters, arrays and retries are capped as specified. Here
K=Theta(r/ell),dl=Theta(r ell),m=Theta(r/ell),r²=Theta(n).
Hence Dcap,Ccap=O(n²2^m), and at mostn batches give

    Q<=nCcap+K=O(n³2^m).

Quantum space. A depth-first traversal retains at most two index
registers per level, each of width at mostH. Since

    m+1<=r/(4ell)+2, H<=5r ell,
    (m+1)H<=5r²/4+10r ell<=45n,

using ell<=r and r²<=4n, their peak is O(n). A leaf's dl wires
are included in this bound. Modular operations, the physical source/data
register, LE and implemented lookup scratch are O(n), and K roots use
O(r). Wires are reused after measured failures. Hence S_Q=O(n) on
actual branches, not just in the ideal run. There is no coherent bank.

Classical space. Allocate framei with its prescribed widthlambda_i,
not every frame at widthH. Its tables and merge scratch have
O(n2^lambda_i) bits; an output of widthlambda_i+1 changes this
only by a factor2. There is at most a constant number of such tables
per level. Since widths increase byone below the root,

    sum_(0<=i<m)2^(dl+i)<2^(H+1).

Thus all retained siblings, active inputs, selected outputs and even
fixed per-level scratch allocations together fit O(n2^H) bits.
The root output has width1. Parameter, rational-log, decoder, free-wire
and counter storage is polynomial in n and is absorbed by this bound
on the main range. Full3n-bit labels and every retained frame count.
Hence S_C=O(n2^H); the geometric sum is specific to these uncapped
increasing widths and is not assumed for a plateau of equal-width frames.

Work. A LEAF costs O(n2^dl) core steps and there are at most
Dcap/dl calls. A merge at input heighti consumes2^(i+1)dl delivered
leaves which no other attempt at that height uses; failed inputs are
discarded. Each attempt costs O(n ell²2^(dl+i+1)) by6. Since
(m+1)/dl=O(1/ell²), summing all levels and LEAF calls costs
O(nDcap2^dl)=O(n³2^(m+dl)) core steps per batch.

By8.1,logQcap=m+O(log n)=O(r/ell). Indeed ell=Theta(log n)
and(log n)²=O(r). Label extraction and source transforms therefore
cost O(n²r/ell) core steps per acquisition. Acquisitions cost
O(n^(9/2)2^m/ell) per batch. The decoder costs O(Kn2^Y), hence
O(n^(7/2)2^m/ell) core steps per stage.

Across at mostn batches, and charging O(r ell) address bits per
core step since log(S_C+S_Q+2)=O(H+log n)=O(r ell), total work is

    T=O(n^(9/2)ell2^(m+dl)+n^6 2^m+n^5 2^m).

Source charges(n+1)Q, parameter/CRT and rational-log computation,
gate generation, all resets and fixed-array initialization fit these
bounds or a smaller polynomial-times2^H term. Since2^dl grows faster
than every polynomial, the latter terms are absorbed. Thus

    T=O(n^(9/2)ell2^(m+dl)).                         (14.1)

This is an actual all-branch bound, not an expected-runtime statement.
Each loop is fixed or consumes a capped acquisition/delivered leaf;
every branch terminates. Wrong LE labels do not evade allocations or caps.

## 15. Uniform envelopes and exact indices

Let l=log2n>=1 and define

    F(n)=4sqrt(n)l+(1/8)sqrt(n)/l.

By8.0, l-1/n²<=ell<=l and ell>=l/2. Thus
1/ell<=1/l+2/(n²l²), giving

    m<=sqrt(n)/(4l)+3, kappa<=l/2+3.

Also m>=r/(4ell) and r>=sqrt n give

    n/(m+1)<=n/m<=4ell*n/r<=4sqrt(n)l.

By8.3,

    m+dl<=n/(m+1)+m/2+kappa+2
          <=F(n)+l/2+7,
    H<=F(n)+l/2+6.

Substitute into14. Absolute factors2^7,2^6 and2^3 are outer
constants, so jointly

    T=O(n^5log2(n) 2^F(n)), S_C=O(n^(3/2)2^F(n)),
    S_Q=O(n), Q=O(n³ 2^((1/4)sqrt(n)/log2(n))).

These inequalities apply on the main branch. Any polynomial setup cost
of RLOG is absorbed in the stated work and classical envelopes. Its
poly(log n) scratch is O(n), including after increasing an absolute
constant over any bounded initial range. The finite n<2^48 branch
contributes finite constants too. Thus everyN,s is covered.

The multiple exponent terms and polynomial factors are all part of the
declared structured envelopes. For T andS_C the dominant exponent is
4sqrt(n)log2(n); for samples it is(1/4)sqrt(n)/log2(n). Double
logarithms divided bylog2n tend to1/2. The linear quantum envelope
has index0. Thus indices are[1/2,1/2,0,1/2] and score[1/2].

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope and limitations

This is a source/time/classical-space tradeoff with O(n) accessible qubits,
not a cube-root algorithm or global optimum. Classical memory grows with sqrt(n)log(n) in its exponent, while the
sample envelope has sqrt(n)/log(n) in its exponent. Their indices remain1/2. The finite cutoff and absolute constants
may be large. Zero fractional tolerance means independent ideal copies;
it is neither a positive robustness claim nor an impossibility theorem.
All statements concern the one specified configuration.
