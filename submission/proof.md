# WTR1: wide top blocks with five-control ramped triple-cap trees

This document specifies the fixed algorithm WTR1 and its joint resource proof.
The argument is supplied for mathematical review; it is not a machine-checked
proof or a claim of a hosted verdict.

## 0. Joint theorem and comparison target

For every N >= 2, every secret s modulo N, and n = ceil(log2 N), WTR1 receives
N and independent ideal copies of the specified mixed coset state. It returns
the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY
execution branch, including rejection, merge failure, extraction error and
budget abort, its simultaneous resource guarantees are

    T   = O(n^(15/4) 2^(sqrt(2n))),
    S_C = O(n^2 2^(sqrt(2n) - 3(2n)^(1/4))),
    S_Q = O(n),
    Q   = O(n^(5/4) 2^(sqrt(2n) - (2n)^(1/4))).                 (0.1)

All outside constants are absolute. Asymptotic expressions involving log n are
understood for n >= 2; the explicit finite branch below includes n=1.
The supplied state is rho_s=N^(-1) sum_{x=0}^{N-1}|psi_{x,s}><psi_{x,s}|,
where |psi_{x,s}>=(|0,x>+|1,(x+s) mod N>)/sqrt 2. The value x and a
purification are unavailable. Write N=2^a2 M with M odd, d=floor(log2 N),
s1=s mod M and s=s1+M s2 mod N with 0<=s2<2^a2. Factoring out powers of
two is done by counting trailing zero bits; no factorization of M is needed.

Tolerance is zero, under exactly the published CS1 error-model text:

    Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The structured declarations retain CS1's exact rational a=u_333/v_333, where
(u_0,v_0)=(10,7), (u_{j+1},v_{j+1})=(3u_j+4v_j,2u_j+3v_j). Since
u_j^2-2v_j^2=2, a>sqrt(2). The envelopes, in T,C,Qubits,Samples order, are

    n^(15/4) 2^(a sqrt n),   2^(a sqrt n - 3n^(1/4)),
    n,                       n^(5/4) 2^(a sqrt n - n^(1/4)).

Their exact growth indices are 1/2,1/2,0,1/2. The proof first establishes
(0.1), with actual sqrt(2n) exponent; its polynomial time gain never spends
a-sqrt(2). Relative to CS1-C3Q's n^4 log(n) time, the actual time ratio is
n^(-1/4)/log(n), tending to zero. This is a full bound improvement, not an
index improvement or a measured runtime claim.

## 1. Provenance and precise changes

This is one new configuration. Direct material predecessor WTS1 is the exact
private source commit c0fa3c78636d0e0cb2f7ffe4e5093c2c74c03269, member
submission/proof.md, SHA256
bbc439d87a54bb4c145fd3549dd1c6fd25ee10f4890ef015e7a08a22bd2cddd7.
Its complete1091-line proof was read. The wide-top-block characteristic
function, CRT identity, enlarged grid, all-modulus stage-count bound, exact
high-confidence extractor and literal primitive/controller census are
adapted here. No prior verdict is a premise. It was submitted as50a9f13c-eda5-4239-a3c8-28ed83e8ce83 and was
validating at preparation. That actual UUID is declared when the source is
published; pending availability is not a claim of independence.

The other direct private predecessor is RBS2, exact commit
6bb755b709fc28c0f8f0e9cb2d50db2ddcaefbb5, member submission/proof.md,
SHA256 cd148b60eb0b574c42e0daeaaaae3e75f2be1e4868dd0afdb8616e8b851a4279.
Its ramped failure reserves, five-control leaves, shortened depth and
rounded triple cap replace the growing seed in WTS1. RBS2 descends from
unsubmitted RBS1 exact8685760ba9356c7c87a385aacc6891593cf61e95.
These are honest unpublished lineages, not fabricated published sources.

Underlying published material sources, all with member submission/proof.md:

* CS1 f1481815-9577-4990-abe3-7b79fa5d9284, evaluated commit
  200ef0387acb280adcd272f4fbcdb805d1786bbe, proof SHA256
  e1b698d021f72cc5fd17f0132a2c30ba213dc2c424e613087d711804f074b528.
  The same proof was read as b56c7ceb-de59-42da-9e3b-6ee96e4e4145,
  evaluated4bd1700e634c8b1f2ebcf6cc8126360622e08a1c.
  The latent-label identity, exact linear merge, decoder, two-adic shifts
  and finite branch are material. Both acquisition lineages are explicit.
* Dadon TC 04669374-610b-497e-ae9b-c856335731ce, evaluated commit
  09655a3a4f490aa07f201a787ac2adfd2330edcb, proof SHA256
  2915c7e52df093034cf30e1a53f4f9f221132f2b5fb4232cfb69562e38ae3f31.
  Exact unit relabelling, literal lookups, allowance-based controller and
  uncapped-reference coupling are material, as incorporated by WTS1.
* CS1-C3 6e91de62-9a4f-4f08-bfa8-1beacca11e0f, evaluated commit
  f248f9f242c21046223007c9462332b9d738e0bb, proof SHA256
  c790bf765bcd1dd4cda653656ec9c79bc07520a051c29dcd7d2094fc57121a50.
  Its enlarged-cap memory analysis motivated the intermediate RBS schedule.
* Triple-cap source13d9050e-950b-4eba-8097-d6c0b578536c, evaluated commit
  f37580741cd11a672b6f484e6d85082122ff6670, proof SHA256
  2cbb8a101c91060e0646c5c24becb8a5d51e9f630a03882d460ebb0c48164d06.
  Its three-square-root cap motivates our different rounded triple cap.
  The capacity, widths and joint costs are rederived for this configuration.

The integration does not stack incompatible old bounds. Section7 separates
label width D from the B collimated bits. Sections8-9 keep whole uniform top
blocks and charge their larger grid. Section11 supplies an explicit fixed
layout/census and a deterministic per-acquisition charge for EVERY failed
or partial subtree. Section12 couples the same algorithm to its uncapped
reference; Section13 establishes its joint resources. No rare event or
minimum-distance hypothesis is needed.

Primary papers browsed: Kuperberg arXiv:1112.3333v1, Algorithm4.1,
Proposition4.2, Corollary4.3 and Section4.6, and Kitaev
quant-ph/9511026v1, Section3 equations16-19 and Lemmas9-10.
https://arxiv.org/html/1112.3333v1
https://arxiv.org/pdf/quant-ph/9511026v1
Kuperberg's QRACM bound and heuristic sqrt(2n) estimate are not imported.
Kitaev's known controlled unitaries are implemented as counted exact modular
translations. The elementary proofs and all charged implementation costs
required here are given below.

## 2. Uniform primitive model

A raw step is a Boolean operation on at most three classical bits, a classical
bit read/write, an elementary Clifford+T gate, a measurement, a reset, or a
fresh-qubit initialization. All controller work, including construction of
addresses and gate descriptions, is included in raw steps. Each raw step has
at most three addressed operands; counting its own operation and the model's
address charges costs at most 1+3 ceil(log2(Mem+2)). There is no recursive
charge on this prescribed address tariff. A source acquisition separately
costs n+1. Section 11 includes that n+1 in its copy allowance.

The controller emits one gate at a time. It never stores a circuit of
exponential length and never assumes O(1) gate generation. Section 11 supplies
fixed raw allowances, including all descriptors, and a raw-work accumulator.
The subsequent factor 1+3 ceil(log2(Mem+2)) charges every included bit operation.

Here are elementary constructive bounds, deliberately with slack.
A w-bit copy, comparison, or addition/subtraction uses at most 64(w+1)
Boolean/read/write steps excluding address selection. Use the full-adder
relations t=a XOR b, sum=t XOR carry, carry'=(a AND b) OR (t AND carry),
and the corresponding borrow recurrence. Scans in both directions cover
carry computation, output and cleanup. Schoolbook multiplication and long
division on w-bit inputs use at most 2^12(w+1)^2 such steps and O(w) scratch.
Extended Euclid uses at most 2w+2 divisions: in every two nonterminal remainder
steps the larger remainder at least halves. Its coefficients have O(w) bits.

A Boolean circuit with g fan-in-two operations can be computed reversibly by
saving one bit per intermediate operation, copying its output and reversing
those g operations. AND uses Toffoli, XOR uses CNOT and negation uses X.
For a permutation f whose f and f^{-1} both have such circuits, compute f(x)
into a second register, swap, and XOR-compute f^{-1} to clear the old input.
For controlled modular addition, compute [x<N], x+c on w+1 bits,
[x+c<N], the unreduced sum minus N, and the two selectors (reduced versus
unreduced, followed by valid-and-enabled versus x). Each ripple has at most
five Boolean operations per position, each selector three, and the enable
flag two. Thus 128(w+1) Boolean operations is a conservative ceiling for
controlled addition of a known
constant modulo a known N, extended by identity for x>=N. The same description
with the negative constant supplies its inverse. Consequently this operation
has at most 2^16(w+1) elementary gates and 2^10(w+1) scratch qubits. Inputs are
retained during the compute-copy-uncompute steps; this is an actual bijection,
not irreversible erasure.

For completeness Toffoli is exact in Clifford+T: for bits a,b,c,
4abc=a+b+c-(a XOR b)-(a XOR c)-(b XOR c)+(a XOR b XOR c).
Compute the four displayed parities into clean ancillas, apply T to a,b,c
and the triple parity and T-dagger to the three pair parities, and uncompute.
The diagonal phase is (-1)^(abc). Conjugating c by H gives Toffoli. This uses
27 gates and four reusable ancillas. Thus the constant circuit bounds above
can be checked without a synthesis theorem or precision oracle.

An equality flag [x=e], x of l bits, uses X on the positions where e is zero,
a chain of l-1 Toffolis, CNOT to the flag, and reversal; at most 64(l+1)
elementary gates with O(l) scratch. A literal table lookup uses two such flag
circuits per row and CNOTs to the indicated output bits. It costs at most
E(128(l+1)+w) gates for E rows of w bits, with indices outside the table mapped
to zero. Its actual controller costs are included in Section 11.

## 3. Source identity and transformations

Let omega=exp(2 pi i/N), chi_k=N^(-1/2) sum_{x<N} omega^(kx)|x>, and
phi_k(s)=(|0>+omega^(-ks)|1>)/sqrt 2. Expansion of the specified mixed state gives

    rho_s = (1/N) sum_{k<N} |phi_k(s)><phi_k(s)| tensor |chi_k><chi_k|. (3.1)

Indeed off-diagonal labels have coefficient N^(-1)sum_x omega^((k-k')x)=0.
Therefore the actual mixed-state experiment has exactly the same law as
independent uniform latent k's followed by these product states. The latent
k is an analysis variable, never an extra input. Applying X to the control
turns phi_k(s) into q_k(s/N)=(|0>+omega^(ks)|1>)/sqrt 2 up to global phase.

Shift_c: conditionally on the source control being 1, replace data x by
x-c mod N. This is the exact permutation of Section 2, identity on encodings
>=N, and turns the source into rho_{s-c}. No controlled source preparation,
inverse source circuit, purification or knowledge of x is used.

Unit relabelling (TC Section 2). After extracting k, for a known unit alpha
modulo N compute k'=alpha^{-1}k mod N classically. Since k's phase equals
k' alpha s modulo N, the existing control qubit is q_{k'}(alpha s/N).
The label k' is uniform modulo N. This uses no quantum multiplication.

## 4. Rational trigonometric table

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20
of cos(2 pi v/4096) and sin(2 pi v/4096).

- Bound pi within 2^-90 using Machin's formula pi = 16 atan(1/5) - 4 atan(1/239),
  summing the first 40 terms of each alternating arctangent series. This gives
  two-sided bounds; the tails are below 16 (1/5)^81/81 + 4 (1/239)^81/81 < 2^-91.
- The identity follows from tan(2 atan(1/5)) = 5/12, tan(4 atan(1/5)) = 120/119
  and tangent subtraction.
- At the angle 2 v p_mid/4096 < 7, where p_mid is the midpoint of the pi bounds rounded to denominator 2^100,
  sum the first 80 terms of each sine/cosine series. Their remainders are
  bounded by 7^160/160! < 2^-170. The angle error
  is < 2^-89, and sin and cos are 1-Lipschitz.
- Round each value to denominator 2^20.

This is a fixed finite rational computation, charged once as an absolute
constant (not advice).

For x in [0,1) put tab_0(x) = Cos[floor(4096x)] and tab_1(x) = Sin[floor(4096x)],
and let cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                    (4.1)

## 5. High-confidence label extraction only

Set J_e=n+4, h=ceil(log2(Qcap(n+5)))+14 and F(y)=2^21 y for positive integer y, where the integer
Qcap is fixed by Section 11 before any acquisition. Every acquired copy is
processed by this same extraction, including copies later rejected.

Translation Tr_c|x>=|x+c mod N> has eigenvalue omega^(-kc) on chi_k.
A test of shift c prepares H|0>, controls Tr_{-c mod N} by that ancilla,
and measures it in X (H then Z) or Y (S-dagger,H then Z). Its sign has mean
cos(2 pi ck/N) or sin(2 pi ck/N). Conditioned on the latent k the data
and control spectator are unchanged, and the test outcomes are independent.
A level-j test uses c=2^j mod N, computed by classical modular doubling.
These are exact H/S/Toffoli circuits; no QFT or arbitrary rotation is invoked.

### 5.1 RUN(F): level-wise extraction

For each j = 0..J_e take F tests at level j per basis, giving empirical means
x_j and y_j. Then decode as follows.

Decoding each level. Pick the least dr in [0,64) maximizing
x_j Cos[64 dr] + y_j Sin[64 dr].
- If |x_j - cos| and |y_j - sin| are at most 1/1024, each computed dot product
  differs from cos(2 pi (2^j k/N - dr/64)) by at most 2/1024 + 2^-19 < 1/256.
- The nearest direction has true dot >= cos(pi/64) >= 511/512.
- Any direction at circular distance >= 1/16 has dot <= cos(pi/8) <= 31/32.
- The gap 15/512 exceeds 2/256. So alpha_j = dr/64 is within circular distance
  1/16 of 2^j k/N.

Unwrapping. Set g_(J_e) = alpha_(J_e). For j = J_e - 1 down to 0, let g_j be
whichever of g_(j+1)/2 and (g_(j+1)+1)/2 (mod 1) is circularly closer to alpha_j
(ties: the first).
- Suppose g_(j+1) is within e < 1/16 of 2^(j+1) k/N. The correct preimage is
  within e/2 of 2^j k/N, hence within 1/16 + e/2 < 3/32 of alpha_j.
- The other preimage is at least 1/2 - e/2 from 2^j k/N, hence more than 13/32
  from alpha_j.
- So the choice is correct and the error halves. Finally g_0 is within
  2^-(J_e)/16 = 2^-(n+8) < 1/(2N) of k/N.

RUN(F) outputs floor(N g_0 + 1/2) mod N, which then equals k. On any input it
returns a value in [0,N) after its fixed number of tests.

Concentration. For F independent +-1 variables, the centered log-moment
generating function has second derivative at most 1 (a tilted variance) and
vanishes with its first derivative at 0. Hence
Pr(|mean - E mean| > delta) <= 2 exp(-F delta^2/2). With delta = 1/1024 and
F = F(h) this is 2 exp(-h). So RUN(F(h)) returns a value other than k with
probability at most 4 (J_e + 1) e^(-h) = 4 (n+5) e^(-h), uniformly in k.
RUN(F(h)) uses 2(J_e+1)F(h) tests and O(n^2 h) quantum gates before
controller and address costs. Section 11 charges those costs explicitly.

We always run RUN(F(h)); there is no cheap estimate, randomized verifier,
fallback budget or test-dependent tree choice. After RUN the data is reset.
The returned label lies in [0,N) even on error. In at most Qcap calls, uniformly
under adaptive previous history, the chance of any erroneous label is at most

    4(n+5) Qcap exp(-h) <= 4(n+5) Qcap 2^(-h) <= 2^-12.       (5.1)

The ideal reference keeps the tests but replaces their decoded output by k.
It ignores all internal extraction outcomes when selecting tree structure.
The actual and ideal capped executions coincide until the first extraction
error, by coupling the same latent labels, tests and subsequent measurements.
The copy allowance in Section 11 charges exact circuit emission and classical
decoding. No expected extraction cost is used.

## 6. Phase vectors and the linear merge

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical
label table lab[0..2^lam). In the ideal run its state is
2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a global phase, for a fixed
real th. Labels are nonnegative integers. The vector is COLLIMATED TO p if all
lab[x] are congruent modulo 2^p.

STORAGE. A table collimated to p is stored as its common residue
c = lab[0] mod 2^p (one p-bit number) and the HIGH PARTS hi[x] = floor(lab[x]/2^p),
so lab[x] = c + 2^p hi[x]. Each high part is stored in a fixed field of w bits,
where w is any bound with lab[x] < 2^(p+w) for all x (Section 7 fixes w per
level). Every quantity used below is computed from (c, hi) exactly; lab[x] is
never written out in full except in LEAF, where p = 0 and hi = lab.

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x]
into a clean w-bit register, controlled by a lam-qubit index x. For each row
x0 = 0..E-1 it computes the flag [x = x0] with a Toffoli chain on O(lam)
scratch, applies CNOTs from the flag to the output bits where tab[x0] has a 1,
and uncomputes the chain. Indices outside [0,E) give output 0. The circuit is
its own inverse, has O(E (lam + w)) gates and O(lam + w) qubits, and is
generated by reading each table bit once.

### 6.2 MERGE(X1, X2; p, b, lam')

Precondition: X1 and X2 are phase vectors from disjoint sets of copies, both of
length 2^lam, collimated to p, with index registers x and y and tables al and be.
Both are stored as in STORAGE: al[x] = cA + 2^p hA[x] and be[y] = cB + 2^p hB[y],
with 0 <= cA, cB < 2^p. Let car = floor((cA + cB)/2^p) in {0,1}.
Define residues aa[x] = hA[x] mod 2^b and bb[y] = hB[y] mod 2^b.
Then bits p..p+b-1 of al[x] + be[y] equal (aa[x] + bb[y] + car) mod 2^b.

1. LOOKUP aa into a fresh b-bit register Ru and bb into Rv. Add Ru + Rv + car
   (mod 2^b) cleanly into a fresh register Rz, and clear Ru and Rv by repeating
   both lookups. Measure Rz, obtaining e, and reset Rz from that known value.
2. Classical. Let S_e = {(x,y) : aa[x] + bb[y] + car = e mod 2^b} and sz = |S_e|.
   - Merge-sort the indices y by the key (bb[y], y) into order[]; pos[y] is the
     position of y.
   - For each x the partners y form one contiguous run of order[], namely the
     residue class cls[x] = (e - car - aa[x]) mod 2^b. Find its start lo[x] and
     length cnt[x] by binary search.
   - Put off[x] = sum_(x' < x) cnt[x'] and rank(x,y) = off[x] + pos[y] - lo[x].
     The rank is a bijection from S_e onto [0, sz).
   - If sz < 2^lam', declare FAIL.
3. Let R have 2 lam + 1 bits. LOOKUP pos into Rp and Dx[x] = (off[x] - lo[x]) mod 2^(2lam+1)
   into Rd. Add Rp + Rd (mod 2^(2lam+1)) cleanly into a fresh R, and clear Rp
   and Rd by repeating the lookups. On S_e, R = rank(x,y).
4. Measure bl = floor(R / 2^lam'), the bits of R above the low lam'. If
   (bl+1) 2^lam' > sz, declare FAIL.
5. Classical. For v in [0, 2^lam'), find the unique (x_v, y_v) with rank
   bl 2^lam' + v, in one scan over x with running offsets. Apply LOOKUP
   v -> (x_v, y_v) on the low lam' bits of R, XORing into the registers x and y,
   which become |0>. Reset the high bits of R from their known value bl.
6. Output the low lam' bits of R as the index register, with table
   lab[v] = al[x_v] + be[y_v], stored as in STORAGE with p+b in place of p:
   put sv = hA[x_v] + hB[y_v] + car, which is congruent to e modulo 2^b. Then
   lab[v] = (cA + cB - car 2^p + 2^p e) + 2^(p+b) floor(sv/2^b). The first term
   c' = cA + cB - car 2^p + 2^p e lies in [0, 2^(p+b)) and does not depend on v.
   So the stored output is the common residue c' and the high parts
   hi'[v] = floor(sv/2^b).

On FAIL, both inputs are reset and released and never reused. All registers
have fixed widths, so memory is allocated deterministically.

Correctness (ideal run). Before step 1 the state is X1 (x) X2: equal
magnitudes over all pairs (x,y), with phases 2 pi (al[x] + be[y]) th. Steps 1
and 3 compute functions of (x,y) into clean registers and measure them. So
after step 4 the state is the equal-magnitude superposition over the 2^lam'
pairs of block bl, with their original phases. Step 5 maps (x_v, y_v) to v
bijectively. The output is therefore a phase vector with table lab. Every
label is congruent to cA + cB + 2^p ((e - car) mod 2^b) modulo 2^(p+b), so the
output is collimated to p+b.

Lemma 6.1 (distribution-free failure). For ANY input tables collimated to p,
the measurement law in steps 1 and 4 depends only on aa, bb and car (that is,
on label bits below p+b), and Pr[FAIL] <= 2^(b + lam' - 2 lam).

Proof. Each measurement is a computational-basis measurement of a function of
(x,y) on an equal-magnitude superposition. Its outcome probabilities are
therefore ratios of counts, independent of the phases. The outcome e has
probability sz_e / 2^(2lam). Given e, the measured rank is uniform on [0, sz_e).
So FAIL has conditional probability rem_e / sz_e, where rem_e = sz_e mod 2^lam'
(this also covers sz_e < 2^lam'). Hence
Pr[FAIL] = sum_e rem_e / 2^(2lam) <= 2^b (2^lam' - 1) / 2^(2lam). QED.

Cost interface. Put L=2^lam and L'=2^lam'. There are eight passes over
L-row lookup tables and one over the L'-row inverse block table. All quantum
lookup field widths are at most a constant times lam+b+lam'; high labels of
O(n) bits are added classically, never loaded quantumly. Section 11 proves
the explicit raw allowance F_merge(L+L'), where F_merge=O(n), including
sorting, searches, address formation, gate descriptors and budget updates.
This allowance applies also on FAIL or after a wrong label extraction.

## 7. Ramped triple-cap tree with separate D and B

The main branch is n>=65536. Define exact global integers

    u_*=ceil(sqrt(2n)), v_*=floor(sqrt(u_*)), mu=u_*+4, ell=5.

A star denotes the schedule at B=n below. TREE(D,B) takes ideal independent
phase controls with labels uniform[0,2^D), where 0<=B<D<=n. For B=0 it
returns one accepted control directly, with two labels0,k, frequency W=k
and q_B=1. There is no merge or five-control leaf on that special branch.
For B>=1 define the exact B-dependent schedule

    u=ceil(sqrt(2B)), v=floor(sqrt(u)), m=u-v+4,
    sigma=min(m-1,3floor(sqrt(m))), t=m-sigma, h_t=ceil(log2m),
    kappa_i=3+min(i,h_t), delta_i=min(max(i-1,0),v)  (0<=i<m),
    lambda_i=min(i,t)+kappa_i+2+delta_i             (0<=i<m),
    lambda_m=1, bmax_i=2lambda_i-lambda_(i+1)-kappa_i.

All schedules depend on B, not D or label values. Set lambda_max to the
EXACT maximum of all lambda_i over 1<=B<=n and0<=i<=m(B), together with1.
Setup enumerates at most n schedules of at most mu+1 entries. This avoids
assuming that the rounded triple-cap table maximum occurs at B=n.

Feasibility. u>=2, m>=5, and m>=v+2, because u>=v^2 gives
u+2-2v>0. Hence delta_(m-1)=v and 1<=sigma<m, t>=1.
Consecutive kappa and delta increments Dk_i,Dd_i are0 or1. For i<m-1,

    bmax_i=i+1-Dk_i+delta_i-Dd_i       if i<t,
    bmax_i=t+2-Dk_i+delta_i-Dd_i       if i>=t.

At i=0 it is0; at i>=1 these are nonnegative. The root capacity is
2t+kappa_(m-1)+3+2v>0. Telescoping, including that root, gives

    C=sum_i bmax_i
     =m(m+3)/2-sigma(sigma-1)/2+4+vm-v(v+3)/2
     =u^2/2+11u/2+18-v^2-3v-sigma(sigma-1)/2.             (7.1)

Here lambda_0=5 and sum delta_i=vm-v(v+3)/2. Since sigma<=3sqrt(m),
sigma(sigma-1)<=9m. Substitution of m=u-v+4 yields

    C>=u^2/2+u-v^2+3v/2>=u^2/2>=B.                       (7.2)

Allocate b_i greedily from root downward, b_i=min(bmax_i, remaining B),
then set p_0=0,p_(i+1)=p_i+b_i. Thus0<=b_i<=bmax_i, p_m=B and
p_i+b_i<=B. Section6 applies also to b_i=0. Its conditional failure
bound is at most pFail_i=2^(-kappa_i) for ANY input tables.

The sum of pFail_i is at most1/4+1/8=3/8: sum the geometric part from
kappa_i=3+i and bound the plateau by m2^(-3-h_t)<=1/8.
Each pFail_i<=1/8. Hence

    product_i(1-pFail_i)^(-1)<=exp((8/7)(3/8))=exp(3/7)<2.  (7.3)

The last strict inequality follows termwise from exp(x)<=1/(1-x) for
0<=x<1, giving exp(3/7)<=7/4. No assumed bucket distribution is used.

LEAF takes exactly5 accepted controls and constructs its32-entry table
by lab[0]=0, lab[x+2^j]=lab[x]+k_j for j=0,...,4,x<2^j.
VEC(0)=LEAF. VEC(i+1) builds two fresh VEC(i), runs MERGE with
p_i,b_i,lambda_(i+1), and on FAIL discards both and repeats. TREE(D,B)
returns VEC(m). Evaluation is depth first; each failed input is consumed.
The returning root uses q_B=5*2^m distinct accepted controls; discarded
copies are extra and are counted by the caps, not hidden in q_B.

Each level-i table label is a sum of at most5*2^i integers below2^D.
Its high-part field therefore has fixed positive width

    w_i=D+i+3-p_i<3n.                                    (7.4)

In particular D is NOT replaced by B+1. Widths remain valid after extraction
errors because the returned labels are reduced to their specified interval.
The returned two labels agree modulo2^B and their exact frequency is

    W=(lab[1]-lab[0])/2^B=hi[1]-hi[0],
    |W|<2^(D-B)q_B.                                      (7.5)

Every index has a distinct raw-control incidence vector: subsets at a leaf,
concatenation on disjoint child supports at a merge, and injective reindexing.
This proves the only incidence fact needed by Section8.

Depth and lengths. The map u-floor(sqrt(u)) is nondecreasing on integers,
so m(B),v(B),q_B are nondecreasing. All are bounded by their stars at B=n;
put q=5*2^m_*. Directly from the rounding inequalities,

    m+v=u+4<=mu,
    m<=sqrt(2B)-(2B)^(1/4)+6.                            (7.6)

For i<m,2^kappa_i<16m. Therefore

    2^lambda_i<=64m2^v2^i,
    2^lambda_(i+1)<=8*2^lambda_i.                        (7.7)

The root is shorter. Every lambda_i<=2mu and b_i<=4mu in the main range.
Indeed lambda_i<=u+h_t+9<=mu+log2mu+10<=2mu for mu>=367; the final
inequality holds at367 and its right-minus-left derivative is positive.
Also sum_i lambda_i<=2mu(mu+1)=O(n), sufficient for the depth-first stack.

Triple-cap memory bound. The maximum nonroot width of a B-tree obeys
lambda_i<=u-sigma+h_t+9. Since sqrt(m)>=sqrt(u)-1 and m>=5,

    sigma>=3sqrt(m)-3>=3sqrt(u)-6,
    u-sigma<=sqrt(2B)-3(2B)^(1/4)+7.                      (7.8)

For the minimum's second entry use3floor(sqrt(m))>=3sqrt(m)-3;
for its first use m+2-3sqrt(m)=(sqrt(m)-1)(sqrt(m)-2)>=0.
For all B<=n,n>=64 the right side of(7.8) is at most its expression at n:
x^2-3x is convex for x=(2B)^(1/4), and the left endpoint x=2^(1/4)
has negative value whereas x=(2n)^(1/4)>3 has positive value. This handles
the rounded small-B cases without a false monotonicity assertion. Since
h_t<=h_t*=ceil(log2m_*), the actual enumerated allocation satisfies

    lambda_max<=sqrt(2n)-3(2n)^(1/4)+h_t*+16.              (7.9)

These estimates and all source/work bounds concern this single new schedule.

## 8. Entire uninspected top blocks remain uniform

For TREE(D,B), let Rtop=2^(D-B). Each accepted label has decomposition
k_j=low_j+2^B tau_j, with independent low_j uniform[0,2^B) and
tau_j uniform[0,Rtop). Let Gt contain all low_j, including discarded
attempts, all merge residue/block outcomes, and structural retry and
copy-use decisions. It excludes extraction tests, full high labels, W,
final root measurements and all budget decisions. In the ideal uncapped
process decoded labels are replaced by their latent values and internal
extraction outcomes feed no structural choice. Rejection counts are
independent of accepted labels and may be conditioned on separately.

Lemma8.1. Conditional on Gt and the past before this fresh tree, the tau_j
of the returning root remain independent uniform[0,Rtop).

Proof. Every bucket, rank, sort key, block partition and structural choice
uses only label bits below B, since p_i+b_i<=B. Adding multiples of2^B
does not change these bits. Lemma6.1 makes every merge measurement law a
function only of these low bits and the previous outcomes; it is independent
of the phases. Thus the joint law factorizes as law(tau)*law(low)*
law(structural outcomes|low), inductively through fresh-copy retries.
Extraction tests are averaged out, not conditioned on. Full high labels
are computed but do not change the fixed structural algorithm in this
uncapped reference. No runtime or budget survival event is conditioned on.
This proves the conditional factorization for every prior history. QED.

Distinct index entries at a node have distinct raw-copy incidence vectors:
true for subsets at leaves, preserved by concatenation on disjoint child
copies and by the merge's bijective reindexing. For the two root entries
their difference therefore has hd>=1 nonzero coordinates, each +1 or-1.
The known collimation ensures their low-label difference is divisible by
2^B. Hence

    W=cst+sum_(j in Sp)tau_j-sum_(j in Sm)tau_j,
    cst integer and Gt-measurable, |Sp|+|Sm|=hd>=1.

For any real phi define

    D_R(phi)=|(1/R)sum_(z=0..R-1)exp(2pi i phi z)|.

Independence gives, for R=Rtop,

    |E[exp(2pi i phi W)|Gt,past]|=D_R(phi)^hd<=D_R(phi).   (8.1)

R is a power of two>=2. Its binary expansion factorizes the characteristic
function into fair-bit factors, so D_R(phi)<=|cos(pi phi)|. If phi has
circular distance x in (0,1/2] from an integer, the geometric-sum identity
and sin(pi x)>=2x give

    D_R(phi)=|sin(pi R phi)/(R sin(pi phi))|
             <=min(1,1/(2R x)).                          (8.2)

To justify sin(pi x)>=2x, sine is concave on[0,pi/2] and lies above its
endpoint chord. Finally R is even, D_R(1/2)=0, so

    Pr[W odd|Gt,past]=1/2.                               (8.3)

No uniformly random intermediate table, favorable root pair, unusually
large incidence distance or postselection assumption enters these bounds.

## 9. Odd part with a wide-top-block stride decoder

If M=1 skip this part and put s1=0. Otherwise M>=3. Let

    d=floor(log2N)=a2+floor(log2M),
    L=min(d-a2,1+floor(v_*/8)), B=d-L>=a2,
    stride=max(1,L-4), theta=s1/M,
    K=2^13(ceil(log2q)+L+ceil(log2n)+30).

Here L>=1, B<d and q is the global bound from Section7. Let J be the least
nonnegative integer such that 2^((J+1)stride+2)>2M. Use Sodd=J+1 stages.
Sodd<=n: stride>=1 and 2^(n+2)>2M. All parameters are computed exactly
in setup; for M=1 define L=1, stride=1 and Sodd=0 in the cap formulas.

At stage j=0,...,J put A_j=j*stride. Compute the CRT unit alpha_j with
alpha_j=1 mod2^a2 and
alpha_j=2^A_j*(2^(B-a2))^(-1) modM. It exists because M is odd and B>=a2.
Acquire a copy, extract k0, set k=alpha_j^(-1)k0 modN classically and accept
iff k<2^d; on acceptance apply X to the control. Ideal accepted k are
independent uniform[0,2^d), with acceptance2^d/N>1/2 (equal1 at powers of2).
The phase is exp(2pi i k alpha_j s/N). For every integer W,

    2^B W alpha_j s/N =2^A_j W s1/M mod1.               (9.1)

Indeed 2^B/N=2^(B-a2)/M and the chosen unit reduces the numerator modulo M.
Run TREE(d,B). Its root has phase exp(2pi i f theta), f=2^A_j W,
with known |W|<2^L q. At each stage obtain K fresh roots, independently
choose X or Y by a measured H|0> coin beta_i, and record W_i,beta_i and
the measurement sign Z_i. Conditional on W_i,beta_i the ideal mean is
cos(2pi f_i theta) or sin(2pi f_i theta), respectively.

Grid and arc. Set P_j=A_j+ceil(log2q)+L+8. Stage0 uses every point
zeta=c/2^P_j on the circle. Later stages use every grid point within
circular distance rad_j=2^(-A_j-2) of the previous center. The previous
center and both arc endpoints are points of this finer grid. Split a
wraparound arc into at most two explicit integer intervals. Each stage
has at most V=2^(ceil(log2q)+L+8) candidates: stage0 has exactly V;
later arcs have at most2^(ceil(log2q)+L+7)+2<=V.

All arithmetic widths used here are fixed in advance. If J>=1, its
minimality gives J*stride+2<=log2(2M)<=n+1, so A_j<=n-1; if J=0,
A_0=0. Hence P_j<=n+ceil(log2q)+L+8<3n in the main range, by Section7.

The factor2^L in the grid is essential and is charged below. Score each
candidate by sum_i Z_i tab_beta_i((f_i c mod2^P_j)/2^P_j). Maintain the K
running modular residues and increment them by f_i between successive
candidates. Keep the least maximizing c and call its point z_j.

Lemma9.1. Given theta within rad_j of the preceding center (no condition
at j=0), with probability>=1-2^-20/n the output has circular error
<2^(-A_j-stride-2).

Proof. The candidate set is fixed at the start of the stage. For each fixed
candidate put Delta=theta-zeta and xi_i=Z_i cs_beta_i(f_i zeta). Conditional
on the preceding root history, this tree's low transcript and its top
blocks (hence W_i), averaging over the fresh fair basis coin gives
E[xi_i|...]=(1/2)cos(2pi f_i Delta). Scores differ from sums of xi_i by
at mostK/625, by Section4.

The nearest candidate zeta0 has |Delta0|<=2^(-P_j-1). Thus
|f_i Delta0|<2^A_j2^Lq2^(-P_j-1)<=2^-9<2^-8, so conditional drift is
at least(1/2)cos(pi/128) for every realization.

For a far candidate |Delta|>=2^(-A_j-stride-2), let
xx=2^A_j|Delta|. At stage0, xx<=1/2 by circular distance. At later
stages theta and zeta are both within rad_j of the previous center, hence
xx<=1/2 as well. Also xx>=2^(-stride-2).
If L<=4, stride=1 and xx>=1/8; (8.1) gives characteristic modulus
<=cos(pi xx)<=cos(pi/8). If L>=5, stride=L-4, so2^L xx>=4 and
(8.2) gives modulus<=1/8<cos(pi/8). Fresh source blocks are independent
of the prior history and Lemma8.1 holds conditionally on that history.
Taking real parts and averaging its low transcript proves conditional
far drift<= (1/2)cos(pi/8), with no favorable-history exception.

For each candidate, xi_i-E[xi_i|past] is a martingale increment supported
in an interval of length2. The conditional log-moment proof of Section5
therefore gives one-sided probability<=exp(-v^2/(2K)) for total deviation v.
At v=K/64 this is exp(-K/8192). Outside the near-point downward and each
far-point upward event,

    score(near)>=(K/2)cos(pi/128)-K/64-K/625
                >(K/2)cos(pi/8)+K/64+K/625>=score(far),

The score margin is positive by an exact rational certificate: pi<22/7,
cos(pi/128)>=1-(22/(7*128))^2/2, and cos(pi/8)<37/40. The latter
follows from cos(pi/8)^2=(2+sqrt(2))/4 and sqrt(2)<569/400,
whose square certificate is569^2>2*400^2. Therefore the margin is
at least 1454743/501760000>0 after subtracting2/64+2/625.
The pi bound is also obtainable from Section4's rational Machin bounds.
There are at most2^(ceil(log2q)+L+9) events. The specified K and
e^-x<=2^-x give total probability<=2^-21/n<=2^-20/n. Thus the maximizing
point is not far. QED.

The output radius2^(-A_j-stride-2) equals rad_(j+1). By induction and
Sodd<=n, all stages succeed with probability>=1-2^-20. The final radius
is2^(-(J+1)stride-2)<1/(2M), so floor(Mz_J+1/2) modM equals s1.

Stage-count saving for arbitrary M. For every L>=1,
stride=max(1,L-4)>=L/5. If L=1+floor(v_*/8), then L>=v_*/8 and
Sodd<=ceil(n/stride)<=40n/v_*+1. If L=d-a2=floor(log2M), then
log2M<L+1 and Sodd<=ceil(log2M/stride)<=11. One of these cases always
holds (including equality). Hence Sodd=O(1+n/v_*)=O(n^(3/4)) for every
odd part, including tiny M. Consequently Sodd*K=O(n^(5/4)).

## 10. 2-adic part: s2 bit by bit

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for
a unique s2 in [0, 2^a2). The bits of s2 are found at levels g = 0..a2-1. Let
s2low be the known low g bits. Put sh_g = s1 + M s2low (mod N), wd = a2 - g, and
rem = (s2 - s2low)/2^g in Z/2^wd. Then s - sh_g = M 2^g rem (mod N).

Leaf qubit for level g:
- acquire a copy and apply Shift_(sh_g), which makes the secret s - sh_g;
- run LE to obtain k, and apply X to the control.

Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with
kk = k mod 2^wd. Since 2^wd divides N and k is uniform on Z/NZ, kk is uniform on
[0, 2^wd). Use kk as the label.

- If wd = 1: if kk = 1, measure X; the outcome is + iff rem is even. If kk = 0,
  discard and repeat.
- If wd >= 2: run TREE(wd,wd-1). If W is even, discard and repeat. If W is
  odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

By (8.3), each attempt has odd W with probability exactly 1/2, even if s1
was wrong. The parity interpretation of its measurement needs the inductive
correctness hypothesis; the bounded expected retry count does not. Set bit g of s2. In the ideal run with s1 correct, every bit is correct.
Output (s1 + M s2) mod N.

## 11. Explicit allocation, block allowances and caps

This section is part of the algorithm, not merely an asymptotic accounting
convention. All parameters below are exact integers, computed before the first
main-branch source copy. ceil(log2 x) means the least integer b with 2^b>=x.

### 11.1 Fixed sizes and addressing

Set

    H=64(n+1), R=64mu, Pwire=2^16(n+1),
    Dwire=ceil(log2(Pwire+1)),
    Lmax=2^lambda_max,
    M0=2^20 H(mu+1)Lmax + 2^20 H^3,
    Mclass=2^ceil(log2 M0).

Reserve Mclass classical bits and Pwire quantum wire positions. Initialize
classical memory by a sequential scan; initialize/reset quantum positions when
first used, charging this to initialization. Pwire is an upper allocation
bound, not the number of source states held. Use the same positions again
after a reset. Below, `Dwire` denotes descriptor width and is distinct from
the tree's label range D.

High-label fields have a power-of-two stride at least H and less than 2H.
Index/residue/rank/key fields have such a stride for R. Different named arrays
occupy disjoint aligned regions; each array has a power-of-two row count.
The number of arrays per level is at most 64. A simple fixed layout, in depth
order, reserves two input-label tables, an output-label table and 32 small-field
arrays per level, all at the common maximum row count Lmax. Padding and unused
regions cost at most a further factor four. This is below
2^12 H(mu+1)Lmax. Source scratch, all n schedules, decoder records and running
residues, constants, and controller scratch fit in 2^12 H^3 bits: there are at
most n(mu+1) schedule entries of O(R) bits, and K<=2^16mu records with O(H)
bits each. Thus even this deliberately wasteful fixed allocation is below
Mclass. It has the required asymptotic space bound; no compressed allocation
is needed for the theorem.

The retained index registers total at most 2mu(mu+1) qubits. At most one
merge, or one source's data/extraction computation, is active beside them.
The former has fewer than 2^18 mu ancilla/index bits (the generic
reversible arithmetic scratch is included) and the latter at most
2^11(n+2)+ell+10. Since mu<=n/64 at these input lengths, these, and a constant number of root/coin qubits, are below
Pwire for n>=65536. Consequently a physical wire name has Dwire=O(log n)
bits, even though classical memory has an exponential number of bits.

All table indices, rank fields, classical pointers, work/source counters and
allowances use at most R bits. All high labels and ordinary arithmetic inputs
use at most H bits; products of them use at most 2H bits. Here is a coarse
check on the explicit sizes, including the constants in this section:

    lambda_max<=2mu, ell<=mu, log2 H<=log2 n+7,
    K<=2^16mu, h<=3mu,
    log2(Mclass+Pwire+2)<=2mu+4log2(n+1)+64,
    log2(2 Wcap+2 Qcap+largest block allowance+2)
           <=8mu+32log2(n+1)+512 <64mu=R.                 (11.1)

The first line follows from Section7. Since q=5*2^m_*,
ceil(log2q)=m_*+3. Also L<=1+v_*/8<=1+mu/8 and
ceil(log2n)<=sqrt(n)/8<=mu/8 for n>=65536. Consequently the literal K is
below2^16mu. Thus Rroots<=2^18nmu and the displayed Qcap satisfies
Qcap<=2^35 n mu2^m_*. It follows directly that
h<=m_*+3log2(n+1)+52<=3mu. The Mclass bound follows from its two explicit
summands and lambda_max<=2mu.

For the last width bound, use R<H, Dwire+1<H and E<=3H^2.
Every term in Wdet is bounded by a constant times (n+1)^8 with exponential
part among2^(m_*+v_*),2^lambda_max,q2^L. These have exponents below4mu.
All displayed numerical factors, including Wcap=2Wdet, are below2^220:
for example Qcap<=2^31 qH^2, c_copy<=2^60H^5, Grow<=2^7H^2 2^v_*,
and F_merge<=2^46H^2; c_set=2^100H^6 is smaller than the same common
ceiling after H=64(n+1). Fewer than sixteen such terms occur. This gives
log2(2Wcap+2Qcap+largest block allowance+2)
<=8mu+32log2(n+1)+512<64mu=R.
Indeed32log2(n+1)<=4sqrt(n), mu>=sqrt(2n), and512<2mu in this range,
so even14mu is a larger upper bound. There is no circular resource
assumption: all displayed integer formulas determine the widths first.

For a random field access form base+(row << strideLog)+fieldOffset by copying
and addition of at most R bits. Never multiply row by a general stride. For a
field scan copy this starting pointer ONCE, then increment through the padded
power-of-two field. Ripple increment has fewer than 2v+R bit flips over v
successive increments, including an initial pointer copy. Detect the field
end by the carry out of the field-offset suffix, rather than a full pointer
comparison at each bit. Thus access to a w-bit field, where w is R or H,
costs at most 2^8(w+R+1) raw steps, including the reads/writes and pointer
arithmetic. An addition, comparison or copy of at most four such fields costs
at most 2^11(w+R+1) raw steps. R<H, so high-field work is O(H) and small-field
work O(R). The model's additional address debit is not part of this raw count;
it is applied to EVERY one of these steps afterwards.

Gate emitter: use a fixed finite template for each elementary gate, equality
chain and ripple operation. A gate location is a wire-region base plus one
loop position (or two such bounded additions), with type and at most three
wire names. For each of at most three operands: copy the register base, copy the
loop offset, add, and copy to the emitted descriptor (12 word operations
in total). Type emission, choosing forward/reverse template positions,
and updating the at most four nested position counters take at most 16
more copies/additions/comparisons. The resulting total is below 32
Dwire-bit word operations, including the loop-position update;
64 raw steps per operand bit gives at most 2^11(Dwire+1) steps. A lookup
also tests the relevant table bit or row-index bit. Its address is formed
by the aligned rule, with no multiplication. Even charging a fresh R-bit
address construction to EVERY emitted gate gives at most

    2^18 R raw steps per elementary gate,

because Dwire+1<=R and fewer than four additional small-field operations
suffice. This deliberately conservative bound includes descriptor writing
and any such bit fetch, as well as the executed gate/measurement/reset.
The physical wire descriptors themselves use O(log n) work; the broader
O(R) allowance also pays for surrounding table-address control. Each loop
position is at most a physical register width and fits in Dwire bits; the
exponential row index is changed at most once per row. No R-bit multiply
or O(n)-bit gate generator is assumed. Actual table scans may be cheaper.

### 11.2 A literal merge/leaf allowance

Define

    E=H+R^2+R(Dwire+1),  F_merge=2^44 E,
    c_leaf=F_merge 2^ell,
    c_merge(i)=F_merge(2^lambda_i+2^lambda_{i+1})  (0<=i<m).

E=O(n), since H=O(n), R=O(sqrt n), Dwire=O(log n). The 2^44 constant follows
from the following primitive census, with enough slack for loop control and
counter updates; it is not an unspecified big-O coefficient.

* A small-field operation above costs at most 2^13 R. Bottom-up stable
  mergesort of L records has at most lambda rounds, at most 2L comparisons
  and 2L record copies per round, with at most four small-field operations
  per comparison/copy (including cursor/index maintenance). Its cost is at
  most 2^17 L R^2. Store the key (bb[y],y) in the record, so a comparison does
  not chase a table pointer for each key bit.
* For each x, lower and upper bound binary searches use at most
  2(lambda+1) iterations. An iteration has at most eight small-field
  operations (midpoint, record address/read/compare, interval update and
  loop test), costing at most 2^17 L R^2. Forming aa,bb,order,pos,lo,cnt,
  off,Dx and the selected inverse block uses at most 32 scans with at most
  sixteen small-field operations per visited input/output row. This is
  below 2^23 R(L+L'). The inverse enumeration advances x at most L times
  and emits at most L' entries; it never enumerates L^2 pairs.
* Computing c', adding two high fields, shifting/copying their quotient
  into the output, and clearing/initializing table/scratch fields uses
  at most 64 high/small-field operations per input/output row. This is
  below 2^24 H(L+L'). It also includes per-row setup and any unused padded
  bits. LEAF's doubling construction requires fewer than 2^ell such
  row operations plus at most ell pointer setups; the same allowance
  F_merge 2^ell covers it.
* Each quantum lookup has at most 2^9 R gates per row by Section 2,
  since all its index/data widths are below R. The nine passes use at
  most 2^13 R(L+L') gates. A fixed number (at most sixteen) of reversible
  additions, copies and cleanup circuits of width below R, each bounded
  by 2^16(R+1) gates as in Section 2, plus measurements/resets, costs
  less than 2^22 R. Since L+L'>=4, the combined count is less than
  2^22 R(L+L'). At 2^18 R raw steps per generated/executed gate this
  contributes less than 2^40 R^2(L+L').

These four entries sum to less than 2^42(H+R^2+R(Dwire+1))(L+L').
Budget read/add/compare, recursion-stack operations and every per-block
initialization use at most 2^20 R additional raw steps. The remaining factor
four in F_merge covers these and an unsuccessful budget check reserved below.
This census uses explicitly described bounded-width operations; the allowance
is valid on arbitrary labels and either merge outcome. It does not divide the
leaf-table cost by the reduced number of source copies.

### 11.3 The remaining allowances

Use the following fixed integer parameters (even if the odd part is skipped):

    K=2^13(ceil(log2 q)+L+ceil(log2 n)+30),
    V=2^(ceil(log2 q)+L+8),
    Rroots=Sodd K+2n,
    Q*=6 q Rroots+2n,  Qcap=1024 Q*,
    h=ceil(log2(Qcap(n+5)))+14.

Sodd K is the exact number of odd-part root records. Section9 computes
L and Sodd before any source acquisition, including the M=1 convention;
2n upper bounds the expected two-adic tree count. The +2n in Q* covers the
width-one case separately. In particular no O(1) or O(n) root count is used.

The remaining RAW allowances are

    c_copy=2^60 H^3(h+1)(Dwire+1),
    c_root=2^40 H^2(Dwire+1),
    c_dec=2^40(H^2 K + H K V),
    c_set=2^100 H^6,
    c_init=2^30 Mclass.

A copy block includes source acquisition n+1, a known controlled shift if
needed, label extraction, classical unit relabelling, label acceptance test,
control X, data reset/discard, and copy-budget update. Here is an upper count
showing that c_copy is conservative without relying on a predecessor's unit-
cost generation convention. There are 2(n+5)2^21 h tests, each with at most
2^17(n+2) gates. At most 2^18 R raw work per gate as above gives at most
2^58 (n+5)(n+2) h R raw work. Because R<=H and n+5,n+2<=H/16 in the main
branch, this is below 2^50 H^3 h, within c_copy. Keeping the outcome counts
and the 64 candidate direction scores at every extraction level, performing
dyadic unwrapping and rounding, and relabelling need fewer than 2^20 H^3(h+1)
raw steps by the field/arithmetic bounds. Modular doubling constants can be
computed once in setup. Thus no cheap verifier is needed. This intentionally
loose copy allowance is harmless with the reduced source count.

A root block measures its root, computes the difference W, records a basis
coin and outcome or tests parity, and advances its retry/record counter.
It involves fewer than 32 H-bit operations, plus a constant number of gates
and a work-budget update. It is bounded by c_root. For wd=1 a raw qubit is
handled as a root block after its copy block, including a rejected even label.

A decoder stage visits at most V candidates, keeps K running modular residues,
and uses one table evaluation and score addition per record/candidate. The
running residue is advanced by an addition, not recomputed by multiplication
at every candidate. Split a wraparound arc into at most two integer intervals;
initialize their starting residues with at most two multiplications per record.
Each residue has at most P_j<3n bits and each score O(log K)+22 bits. Even
including aligned record addressing, at most 128 H-bit field operations
per candidate/record and sixteen schoolbook products per record suffice.
This is below c_dec by Section 2 and 11.1. The fixed trigonometric lookup has
4096 entries, so even a full classical scan of that constant table changes
only a finite factor less than 2^20; this is included in 2^40.

c_set reserves ALL setup, deterministic inter-stage work and final output:
integer roots/logarithms, at most n schedules, at most n CRT/Euclid
computations, constants, source shifts, initial/final rounding and the
fixed rational trigonometric table. To see an explicit polynomial ceiling,
compute integer square roots by binary search in at most H iterations, each
using at most sixteen products/comparisons of H-bit numbers; compute each
of at most n schedules in at most mu+1 iterations. Euclid is at most 2H+2
long divisions per invocation. All these computations use fewer than
2^20 H^2 calls to schoolbook/field operations of raw cost at most 2^20 H^3,
including pointer formation. Their total is below 2^40 H^5<c_set. The constant
trigonometric table can be evaluated with exact rationals: 80 series terms
with operands of at most 2^16 bits suffice: round the Machin midpoint to
denominator 2^100, so each angle is dyadic with at most 112 denominator bits;
use the common Taylor denominator 2^(112*160) 160!, whose bit length is
below 2^15, rather than multiplying 80 separate rational denominators.
The Machin sums use powers up to 81 and the product of the 40 odd
denominators; those operands are smaller. Schoolbook arithmetic
with at most 2^24 operations fits this same allowance when n>=65536.
No uncharged transcendental oracle is used.

c_init covers a full clear/initialize/release scan of Mclass bits, quantum
reset with emission and the final unsuccessful budget check. At most
256(Mclass+R) raw classical scan steps suffice by the pointer rule, and
Pwire*2^18 R gate/emission work is less than c_init/2 using the H^3 term of
Mclass. Three such reservations below cover initialization, normal/abort
cleanup, and extra check/control slack. Initialization of subsequently used
regions is also included in leaf/merge allowances, so double counting is safe.

### 11.4 Deterministic aggregate charge and explicit caps

Define exact integers, using the starred B=n parameters from Section7,

    Grow=8+64(m_*)^2 2^(v_*),
    Wdet=c_set+3c_init+Qcap(c_copy+c_root+F_merge Grow)+Sodd c_dec,
    Wcap=2Wdet.                                           (11.2)

These are literal finite integer formulas, not unspecified big-O constants.
Here is an EVERY-PREFIX accounting proof, valid on arbitrary classical
labels, including wrong-label, failed, rejected and partially built branches.
A completed LEAF bill is32F_merge, supported by5 distinct accepted
acquisitions; charging less than8F_merge to each covers it. A merge attempt
at level i+1 has row allowance F_merge(L_i+L_(i+1)). By(7.7),

    L_i+L_(i+1)<=576m2^v2^i.

Its completed inputs contain at least5*2^(i+1) distinct supporting accepted
acquisitions, so less than64F_merge m2^v per supporting acquisition pays
that FULL attempted-merge bill. At a fixed level no acquisition supports
two attempted merges: inputs are consumed once, even on failure. An
acquisition supports at most m levels. Thus all completed and currently
reserved leaf/merge bills in any prefix with C acquisitions total at most

    F_merge[8+64(m_*)^2 2^(v_*)] C.                        (11.3)

A partial subtree has only a subset of these bills. Interrupted acquisitions
cannot support a leaf until its5 controls have actually been acquired.
For B=0 a direct control uses no leaf/merge bill. The width-one two-adic
case is also a copy/root block. No source is reused across roots. Therefore
the number of root blocks is at most C, including rejected parity roots.
There are at most Sodd decoder stages and exactly one reserved setup/cleanup
allocation. Copy bills are at most C c_copy. Applying(11.3) to ANY prefix
with C<=Qcap gives total billed raw allowance<=Wdet.

The controller is fully specified as follows. Set raw-allowance accumulator
A=c_set+3c_init, acquisition counter C=0. Before every copy test C+1<=Qcap.
Before every copy, leaf, merge, root or decoder block compute/read its fixed
allowance and test A+allowance<=Wcap. If a test fails, execute no such block
and acquire no such copy; run the reserved cleanup and output0. Otherwise
increase the counters and execute the block. Gate generation is streamed;
there is no per-gate R-bit work counter. The checks and updates are included
in their block allowances, and the last denied check is covered by c_init.

A work-budget denial before a source denial cannot occur: include the proposed
block in the prefix; when its source count remains<=Qcap its full allowance
is covered by(11.3) and Wdet<Wcap. Setup and at most n inter-stage/final
computations use their reserved c_set portions. All n schedules and the
lambda_max enumeration fit that setup allowance. No actual time or label
content is used as a hidden stopping criterion. The work cap is retained as
an explicit all-branch safeguard, not an expected-runtime substitution.
Thus on every actual branch, even after a label error,

    Q<=Qcap, raw work including acquisition debit<=Wcap.     (11.4)

Widths are fixed by the integer formulas before acquisitions, so no counter
or table overflows. Charged work is at most
(1+3ceil(log2(Mclass+Pwire+2)))Wcap. Applying that factor also to the included
n+1 source debit is a safe overestimate.

Finite branch n<65536. For cand=0,...,N-1 acquire at most n+10 independent
copies, apply Shift_cand, measure the control in X, and reject cand at its
first minus. Return the first cand with all pluses, or0. For cand=s all
outcomes are plus. For cand!=s the two data branches are orthogonal, so the
sign is fair and error<=N2^(-n-10)<=2^-10. All loops are cut off; copies
<=N(n+10), charged work O(N(n+10)n log(n+2)^2), classical bits O(n), qubits
O(n). This fixed finite set of bit lengths, including n=1, changes only
absolute asymptotic constants; no practical small-instance speed is claimed.

## 12. Uncapped reference, acquisitions and unconditional success

Let U use exact latent labels, retain the same extraction tests but replace
the decoded label by its latent value, and omit source/work caps. Internal
test outcomes and elapsed work feed no structural choice. All conditional
top-block/decoder arguments in Sections8-10 are in U, without conditioning
on future cap survival.

For a returning B>=1 tree, let A_i bound expected acquisitions for VEC(i),
uniformly over all earlier history. A_0<=10 because each of5 odd accepted
controls needs at most2 acquisitions (two-adic controls need1). Conditional
on obtained input tables a level-i merge failure is<=pFail_i. A reached
attempt's two child invocations each have the same uniform conditional
expected-cost bound before they start. The conditional tail-sum argument
therefore gives

    A_(i+1)<=2A_i/(1-pFail_i),
    A_m<=10*2^m product_i(1-pFail_i)^(-1)<20*2^m=4q_B<=6q. (12.1)

No independence between an attempt's cost and its success is assumed.
The B=0 direct root costs at most2 acquisitions, also<=6q. Positive success
probabilities and these finite expected bounds give almost-sure termination
of every uncapped tree.

There are exactly Sodd K odd roots. For wd>=2, a fresh root's oddness is1/2
conditional on all prior history by(8.3). The per-tree expected cost bound
(12.1) is uniform before each attempt; applying the tail-sum argument again
gives at most2 times that bound per two-adic bit. This remains true after an
erroneous earlier decode: the construction laws depend on low labels, not
phases. The parity interpretation only needs earlier correctness when
proving recovery. The wd=1 direct rule costs2 copies in expectation.
Consequently the exact Q* from Section11 satisfies

    E_U[ALL acquired copies]<=6q(Sodd K+2n)+2n=Q*.           (12.2)

This counts all rejected labels, discarded inputs, restarted subtrees and
parity roots. Markov gives Pr_U[Q>Qcap]<=2^-10. On Q<=Qcap, the deterministic
prefix billing proof(11.3) ensures no work denial. Thus the ideal capped
process coincides with U unless its source cap is reached; no separate
work-tail event or extra Markov loss is needed.

Sections8-9 give uncapped odd-part error<=2^-20 for every N,s, including
small M; the ideal two-adic recovery is exact after the correct s1.
Section5 couples the actual capped process with the ideal capped process,
with disagreement probability<=2^-12. The adaptive union bound counts at
most Qcap extractions before the first disagreement, not on a conditioned
successful-extraction event. All actual resources remain bounded directly
by Section11 even on a disagreement. Adding the three losses yields

    Pr[output=s]>=1-2^-20-2^-10-2^-12>1-2^-8>2/3.            (12.3)

The finite branch has error<=2^-10. No cap, favorable frequency, large
incidence distance or label-extraction verdict is postselected.

## 13. Joint resources of this exact configuration

All estimates are for n>=65536; the finite branch changes absolute constants.
Put t0=sqrt(2n). The exact starred schedule has

    mu,m_*=O(sqrt n), v_*=Theta(n^(1/4)), m_*+v_*=u_*+4<t0+5,
    q=5*2^m_*=O(2^(t0-(2n)^(1/4))), h=O(sqrt n).

Section9 uses L<=1+v_*/8, K=O(sqrt n), and Sodd=O(n^(3/4)) uniformly
for every odd M, with Sodd=0 for M=1. Thus Rroots=Sodd K+2n=O(n^(5/4)),
including all expected two-adic retries, and the literal all-branch cap is

    Q<=Qcap=1024(6qRroots+2n)
            =O(n^(5/4)2^(t0-(2n)^(1/4))).                  (13.1)

This uses constant five-control leaves, not the n^(1/4)-control WTS1 seed.

The fixed classical allocation and(7.9), with2^h_t*<2m_*, give

    Mclass=O(n mu2^lambda_max+n^3)
          =O(n^2 2^(t0-3(2n)^(1/4))+n^3)
          =O(n^2 2^(t0-3(2n)^(1/4))).                     (13.2)

The polynomial term is eventually dominated. All schedules, pointers,
counters, classical labels, root records, controller and cleanup scratch
are included. Pwire=2^16(n+1) gives S_Q=O(n), including retained siblings,
source data, extraction scratch and merge registers on abort branches.
The address tariff is O(sqrt n) from this ACTUAL common allocation.

F_merge=O(n). The deterministic row charge in Wdet contributes

    F_merge Grow Qcap
        =O(n^2 2^v_* Qcap)
        =O(n^(13/4)2^(m_*+v_*))=O(n^(13/4)2^t0).          (13.3)

Every other term in that SAME explicit Wdet is smaller:

* c_copy Qcap=O(n^(19/4)log n 2^m_*) plus a polynomial, because
  c_copy=O(n^3(h+1)log n)=O(n^(7/2)log n). Its ratio to(13.3) is
  O(n^(3/2)log n 2^(-v_*)).
* c_root Qcap=O(n^(13/4)log n 2^m_*) plus a polynomial.
* V=O(q2^L), so Sodd c_dec=O(n^(13/4)+n^(9/4)q2^L).
  Its exponential term is smaller than(13.3), since L<=1+v_*/8 and
  2^(L-v_*)<=2^(1-7v_*/8).
* c_init=O(n^2 2^(t0-3(2n)^(1/4)))+poly(n); c_set and all cap/parameter
  calculations are polynomial and have already been reserved.

For every fixed c,d>0, n^c2^(-d n^(1/4))->0 by taking logarithms. This
absorbs all displayed polynomial/log factors using the actual fourth-root
gaps, without spending any slack in a-sqrt2. Therefore
Wcap=2Wdet=O(n^(13/4)2^t0) on every execution branch. Multiplying every raw
step by the prescribed O(sqrt n) address charge, including all controller
emission, gives

    T=O(n^(15/4)2^(sqrt(2n))).                             (13.4)

This is one generalized tree/kernel/decoder/controller configuration, not
a selection of bounds from different algorithms. Failed attempts and every
acquisition are bounded before the unconditional success claim is invoked.

## 14. Exact structured envelopes, indices and comparisons

Retain precisely the CS1 Pell rational a=u_333/v_333 from Section0.
It is explicitly computed there and has a>sqrt2. Equations(13.1)-(13.4)
therefore support the four same-configuration declarations

    B_T=n^(15/4)2^(a sqrt n), B_C=2^(a sqrt n-3n^(1/4)),
    B_Q=n, B_samples=n^(5/4)2^(a sqrt n-n^(1/4)).

For C, the extra n^2 factor is absorbed by the strict quarter-power gap:

    n^2 2^(sqrt(2n)-3(2n)^(1/4))/2^(a sqrt n-3n^(1/4))
       <=2^(2log2n-3(2^(1/4)-1)n^(1/4))=O(1).

Indeed2^(1/4)-1>189/1000 since(1189/1000)^4<2, and the negative fourth-root
term eventually dominates2log2n. The sample enclosure uses
(2n)^(1/4)>=n^(1/4), retaining the exact outside power5/4. No unknown
exponent coefficient or polynomial saving from a-sqrt2 is invented.
For each exponential envelope, log2B=a sqrt n+O(n^(1/4)+log n), so its
exact growth index is1/2. The linear qubit envelope has index0.

Comparison normalizes exact rational log-envelope terms under identical
clean error-model text. Against the WTS1 source configuration, time and
qubits are identical, C gains2^(-n^(1/4)), and the sample ratio is n^(-1/4).
Against RBS2, C and qubits are identical, time and samples each gain
n^(-1/4). Against HSR1's n^4/log2n time and n^(3/2)/log2n samples, both
ratios are log2n/n^(1/4)->0 while C also improves. These compare the exact
reported configurations without implying that a private or pending source
has already been published or accepted. The time gain over HSR1 is the
same polynomial-time gain already introduced by WTS1, not another time
exponent improvement beyond WTS1.

A live full-frontier comparison is still required at publication. Lower-memory
or different-tolerance algorithms can remain incomparable. Exact equal
vectors use earliest submission time then ID; sorting and coarse index ties
never create a gain. No below1/2 index, cube-root algorithm, or optimality
is asserted.

## 15. Tolerance, limitations and proof status

For the SAME WTR1 algorithm and parameters, epsilon(n)=0 for every N>=2:
every acquired copy must be an independent ideal coset state. Section 12
establishes unconditional success together with all four branchwise resource
bounds under precisely this promise. No behavior under malformed copies,
positive robustness, or impossibility of positive tolerance is asserted.

The argument is analytical and includes the uncapped/capped distinction,
conditional expected counts, explicit controller allowances, exact finite
branch and full-secret arbitrary-modulus decoder. It is not an executable
quantum simulator or a formal proof-assistant certificate. The block census
and its implementation conventions are part of the claim and must be retained
if the owner changes the layout, generator, schedule, or cap. Merely preserving
the asymptotic schedule while replacing these counted primitives is insufficient.

Exact symbolic and finite schedule checks support arithmetic diagnostics only. They do not certify adaptive top-bit
independence, source accessibility, quantum correctness or the success coupling.
The large absolute allowances and the finite exhaustive branch make no useful
small-instance runtime promise. This is an analytical polynomial-factor improvement to a resource
envelope, not a measurement of a realized hardware speedup.

The complete argument is supplied for independent mathematical review.
Hosted acceptance, if obtained, is fallible review rather than formal proof.
