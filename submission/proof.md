# WTS1: wide uninspected top blocks with a charged stride decoder

This document specifies the fixed algorithm WTS1 and its joint resource proof.
The argument is supplied for mathematical review; it is not a machine-checked
proof or a claim of a hosted verdict.

## 0. Joint theorem and comparison target

For every N >= 2, every secret s modulo N, and n = ceil(log2 N), WTS1 receives
N and independent ideal copies of the specified mixed coset state. It returns
the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY
execution branch, including rejection, merge failure, extraction error and
budget abort, its simultaneous resource guarantees are

    T   = O(n^(15/4) 2^(sqrt(2n))),
    S_C = O(n^2 2^(sqrt(2n) - 2(2n)^(1/4))),
    S_Q = O(n),
    Q   = O(n^(3/2) 2^(sqrt(2n) - (2n)^(1/4))).                 (0.1)

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

    n^(15/4) 2^(a sqrt n),   2^(a sqrt n - 2n^(1/4)),
    n,                       n^(3/2) 2^(a sqrt n - n^(1/4)).

Their exact growth indices are 1/2,1/2,0,1/2. The proof first establishes
(0.1), with actual sqrt(2n) exponent; its polynomial time gain never spends
a-sqrt(2). Relative to CS1-C3Q's n^4 log(n) time, the actual time ratio is
n^(-1/4)/log(n), tending to zero. This is a full bound improvement, not an
index improvement or a measured runtime claim.

## 1. Provenance and precise changes

Direct material participant sources, whose acceptance is not a premise:

* CS1 f1481815-9577-4990-abe3-7b79fa5d9284, commit
  200ef0387acb280adcd272f4fbcdb805d1786bbe, proof SHA256
  e1b698d021f72cc5fd17f0132a2c30ba213dc2c424e613087d711804f074b528.
  Its spectral source identity, extraction, exact linear rank merge,
  compressed labels, low-transcript argument, free-frequency decoder,
  two-adic shifts and finite exhaustive recovery are adapted below.
* Dadon TC 04669374-610b-497e-ae9b-c856335731ce, commit
  09655a3a4f490aa07f201a787ac2adfd2330edcb, proof SHA256
  2915c7e52df093034cf30e1a53f4f9f221132f2b5fb4232cfb69562e38ae3f31.
  Material reuse is exact unit relabelling, literal equality/lookup
  primitives, fixed block allowances and uncapped-reference cap coupling.
* CS1-C3 6e91de62-9a4f-4f08-bfa8-1beacca11e0f, commit
  f248f9f242c21046223007c9462332b9d738e0bb, proof SHA256
  c790bf765bcd1dd4cda653656ec9c79bc07520a051c29dcd7d2094fc57121a50.
  Its capacity-slack length cap and stronger storage comparison inform
  the cap choice. Our seed/cap parameters and trial-depth proof differ;
  they are established explicitly for this one configuration.

Private enlarged-leaf/controller research supplies the explicit census and
global-work cutoff. A private seed/cap integration derivation also informed
the square-root seed. These are acknowledged as research inputs rather
than independent published submissions. The new device is to collimate
B=d-L bits of d-bit labels, keep an entire independent uniform top block,
and pay the larger frequency grid while advancing by L-O(1) secret bits.
No repetition groups, rare-relation event, minimum Hamming-distance
assumption, QFT or heuristic intermediate-label distribution is used.

Historical primary sources are Kuperberg, arXiv:1112.3333v1, Algorithm4.1,
Proposition4.2, Corollary4.3 and Section4.6, and Kitaev,
arXiv:quant-ph/9511026v1, Section3, equations16-17, Lemmas9-10.
https://arxiv.org/pdf/1112.3333v1
https://arxiv.org/pdf/quant-ph/9511026v1
Kuperberg's Proposition4.2 assumes QRACM. Our literal scan circuit replaces
it. The paper's sqrt(2n) heuristic is not a premise. Kitaev's controlled
power interface is implemented here by known exact modular translations.
No external theorem's unspecified computational overhead is imported.

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

## 7. One global seed/cap schedule, with separate D and B

The main branch is n>=65536. Set, by exact integer arithmetic,

    t=sqrt(2n), mu=ceil(t)+4, u=floor(sqrt(mu)), sigma=2u,
    kappa=ceil(log2 mu)+1, ell=kappa+1+u.

t is analytical notation; integer roots and comparisons compute all
parameters. TREE(D,B) receives independent positive leaf qubits with
labels uniform on [0,2^D), where 0<=B<D<=n. It collimates B bits; D is
not silently replaced by B+1. All trees share the same global parameters.

    Cap(m)=m(m+1)/2-sigma(sigma-1)/2+kappa+(m+1)u,
    m(B)=min{m>=sigma+1:Cap(m)>=B},
    lambda_i=ell+min(i,m-sigma) (0<=i<m), lambda_m=1.

Writing v=m-sigma, the capacities are i+u at growing levels i<v,
v+1+u at capped nonroot levels v<=i<=m-2, and
kappa+2v+1+2u at the root i=m-1. Their sum is Cap(m).
Allocate b_i from the root downward, b_i=min(capacity, remaining B), and
put p_0=0,p_(i+1)=p_i+b_i. Zero b_i is allowed in Section6.2.
Then p_m=B and direct substitution gives

    b_i+lambda_(i+1)-2lambda_i<=-kappa.                 (7.1)

Every merge has conditional failure<=2^-kappa on arbitrary tables.

Exact depth/seed bound. For z=m+u,

    Cap(m)=[z(z+1)-u(u-1)-sigma(sigma-1)]/2+kappa.

The trial m0=mu-u is >=2u+1: mu>=367, u>=19, and mu>=u^2>=3u+1.
Since u^2<=mu and mu-4=ceil(t)>=t,

    Cap(m0)=[mu(mu+1)-5u^2+3u]/2+kappa
            >=mu(mu-4)/2+3u/2+kappa>=n.

Thus, for every B<=n,

    m(B)+u<=m_*+u<=mu<t+5,     m_*=m(n).              (7.2)

Also u>=sqrt(mu)-1>=sqrt(t)-1, ell=Theta(n^(1/4)), m_*=O(sqrt n),
2^kappa is between 2mu and 4mu, and 2^(m_*+u)=O(2^t).
In particular 2^m_*=O(2^(t-(2n)^(1/4))). Since m<=mu and 2^kappa>=2mu,
the retry inflation (1-2^-kappa)^(-m) is less than3.

LEAF uses ell accepted source controls. Build its table by lab[0]=0 and
lab[x+2^j]=lab[x]+k_j for x<2^j, j=0,...,ell-1: one addition per new row.
VEC(0) returns LEAF. VEC(i+1) builds two fresh VEC(i), merges with
p_i,b_i,lambda_(i+1), and on FAIL discards both and repeats. Evaluation is
depth first. TREE(D,B) returns VEC(m), a one-qubit phase vector.

At level i a label is a sum of at most 2^i ell numbers below2^D. Use
g_ell=ceil(log2ell) and high-part width

    w_i=D+i+g_ell-p_i<3n.

These fixed widths remain valid on extraction-error branches, because
each decoded source label is reduced to the specified interval. The root
frequency is the exact known integer

    W=(lab[1]-lab[0])/2^B=hi[1]-hi[0],
    |W|<2^(D-B) q_B,       q_B=ell2^m.                (7.3)

Every returned root has exactly q_B distinct raw source controls; discarded
attempts do not belong to its incidence vectors. Put q=ell2^m_*; q_B<=q.

Width and stack. ell<=mu and lambda_i<=2mu in the main range; for example
u<=sqrt(mu), kappa+1<=log2mu+3, and sqrt(mu)+log2mu+3<=mu for mu>=367,
whose right-minus-left derivative is positive there. Every b_i<=4mu.
The retained index stack has <=2mu(mu+1)=O(n) qubits. The maximum table
log length over all trees is

    lambda_max=ell+m_*-sigma=kappa+1+m_*-u
      <=kappa+1+t+5-2u.

This common global cap is used for actual allocation, not a B-dependent
shortcut. Its exponential reduction is 2u>=2(2n)^(1/4)-2.

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
    L=min(d-a2,1+floor(u/8)), B=d-L>=a2,
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
stride=max(1,L-4)>=L/5. If L=1+floor(u/8), then L>=u/8 and
Sodd<=ceil(n/stride)<=40n/u+1. If L=d-a2=floor(log2M), then
log2M<L+1 and Sodd<=ceil(log2M/stride)<=11. One of these cases always
holds (including equality). Hence Sodd=O(1+n/u)=O(n^(3/4)) for every
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
           <=8mu+32log2(n+1)+256 <64mu=R.                 (11.1)

The first line follows from Section 7; K is defined below and
ceil(log2 q)=m_*+ceil(log2 ell). Here L<=1+u/8<=mu/8+1 and Sodd<=n; adding L to K leaves
K<=2^16mu. For h use Q* below, Rroots<=2^18nmu, ell<=mu and m_*<=mu. For the third line use the two terms
of M0 and ceil(log2 x)<log2 x+1. For the last line substitute the formulas
below: they are sums of fewer than sixteen terms, whose exponential factors are 2^(m_*+ell), Lmax, q and2^L, with
combined exponent sizes below4mu; their polynomial degrees are at most 6
and, after substituting H=64(n+1), R=64mu and mu<2sqrt(n),
their numerical constants are below2^160. (The largest isolated setup
coefficient after the Wcap factor is2^146; the other fixed formulas are
smaller.) These give the stated looser
8mu+32log2(n+1)+256 bound. Finally log2(n+1)<=sqrt(n)/8 for n>=65536
(the ratio decreases there), mu>=sqrt(2n), and 256<mu. This proves the last
strict inequality with substantial slack. There is no circular resource
assumption: the displayed integer formulas determine all widths first.

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

### 11.4 Global caps and the fully specified controller

Define the integer

    Wtree=10 F_merge (m_*+1) 2^(m_*+ell),
    W*=c_set+3c_init+Q* c_copy
          +Rroots(Wtree+c_root)+2n c_root+n c_dec,
    Wcap=1024 W*.

Set the RAW allowance accumulator A=c_set+3c_init, reserving all deterministic
inter-stage work, initialization and cleanup. Set acquisition counter C=0.
Before every copy, leaf, merge, root, or decoder block, calculate/read its
fixed allowance and test A+allowance<=Wcap. Before every copy also test
C+1<=Qcap. If either test fails, do not execute the block or acquire that
copy; run the reserved cleanup and output 0. Otherwise increment the counters
and execute the block. For trees use their own c_merge(i); the common Wtree
is used only in W*. The check/update cost is included in each allowed block,
and the last denied check is covered by c_init. No individual-gate work
counter, with an extra R-bit addition per gate, is installed.

Setup computes the integer caps and reserves c_set before acquisitions.
All n schedules may be stored in the polynomial memory region. Inter-stage
operations depending on measurement results consume their reserved portion
of c_set when they occur; they are performed at most n times. On all branches,
no table width or loop allowance depends on whether label extraction was
correct. A returning source-block label is always reduced to its specified
range. Thus counters cannot overflow their fixed fields, and

    Q<=Qcap,    raw work including acquisition debit <=Wcap.       (11.2)

There is no overshooting block: the check is before the action, and cleanup
was reserved. With the allocated memory above, total CHARGED work is at most
(1+3ceil(log2(Mclass+Pwire+2))) Wcap. Charging the n+1 source debit again by
this factor is an overestimate, not an omission.

Finite branch n<65536. For cand=0,...,N-1 in order, acquire at most n+10 fresh
copies, apply Shift_cand, and measure the control in X. Reject cand at its
first minus; return the first cand with all pluses, or 0 if none. For cand=s
all outcomes are plus; for cand!=s, tracing orthogonal data branches gives a
uniform sign. Hence error <=N2^(-n-10)<=2^-10. This branch uses at most
N(n+10) copies, O(N(n+10)n log(n+2)^2) charged work with the simple generated
shift circuits, O(n) classical bits, and O(n) qubits. It is finite as a set of
input lengths, so it changes only the absolute asymptotic constants in (0.1).
It is not presented as a practical finite-size improvement. n=1 is included.

## 12. Uncapped expectations and unconditional success

Let U be the ideal reference with exact latent labels and with NO source or
work caps. For bounding allowances U follows the same block definitions and
can keep unbounded mathematical counters; their implementation is needed only
in the capped actual algorithm. Internal extraction tests remain real tests,
but their results do not alter U's structural choices.

### 12.1 Conditional expected counts

Let f=(1-2^-kappa)^(-1). Every merge attempt, conditional on all already
constructed inputs and prior history, succeeds with probability >=1/f.
Thus the chance of reaching its j-th attempt is at most (1-1/f)^(j-1) and
the expected attempts per invocation are <=f. This holds without independence
of the attempt's cost and its success event.

For each block type count all occurrences in a returning subtree. Conditional
on any history at the start of a child invocation, its expected count has the
same uniform upper bound (fresh sources, the distribution-free merge bound).
Sum over attempts reached, using that uniform bound before constructing each
child. Induction gives, in a returning level-m tree,

    expected leaves <=2^m f^m <3*2^m,
    expected merge attempts producing level j, 1<=j<=m,
                    <=2^(m-j) f^(m-j+1) <3*2^(m-j).        (12.1)

Indeed f^m<=exp(m/(2^kappa-1))<=exp(m/(2m-1))<3 for m>=2.
These estimates do NOT require Wald independence between a subtree cost and
the subsequent merge outcome. The conditional tail-sum argument supplies
exactly the uniform upper bounds used here.

Each accepted odd-part qubit uses at most two acquisitions in expectation;
each two-adic qubit uses one. Thus a tree uses at most 6 ell 2^m<=6q expected
acquisitions. For child level i, its table length is <=2^(ell+i), and its
output length <=2^(ell+i+1), including the one-qubit root. By (12.1), the
expected sum of row counts L+L' for that merge level is at most

    3*2^(m-i-1) * 3*2^(ell+i) <=6*2^(m+ell).

Leaves add at most 3*2^(m+ell). Summing all m levels gives at most
(6m+3)2^(m+ell) <=10(m+1)2^(m+ell). This proves the common Wtree bound
on the expected leaf/merge allowance per returning tree, for every B<=n.

There are exactly Sodd K odd-stage roots. For each two-adic bit with wd>=2,
conditional on any previous history, fresh W is odd with probability 1/2,
so expected trees are <=2. The parity retry may correlate with tree cost;
apply the same uniform conditional tail-sum argument, not conditioning on
odd W, to give expected cost <=2 times the per-tree upper bound. For wd=1,
expected copies and root blocks are two. Rroots=Sodd K+2n and the extra 2n terms
are safe overcounts. Therefore

    E_U[acquisitions]<=Q*,   E_U[total reserved allowance]<=W*.       (12.2)

All attempts and all rejections are included. Positive lower bounds on each
local success probability imply termination almost surely; (12.2) also
implies that the uncapped total allowance is finite almost surely.

### 12.2 Coupling the caps and labels

Sections 8-10 prove ideal uncapped full recovery with error at most 2^-20.
In particular all high-bit independence and decoder concentration arguments
are carried out in U, with no conditioning on future budget survival.
By Markov's inequality, the chance in U that total acquisitions exceed Qcap
is at most 2^-10, and that total allowance exceeds Wcap is at most 2^-10.
The ideal capped process agrees with U until the first denied block, so its
failure probability is at most the sum of these two probabilities and 2^-20.
No independence between the two cap events or between a cap and the secret
recovery event is required.

Section 5 couples the actual capped process to the ideal capped process with
additional failure probability at most 2^-12. In this comparison the internal
tests are kept and only incorrect decoded labels can break the coupling;
counting them before the first disagreement gives the uniform adaptive union
bound. On every actual branch resources are bounded directly by Section 11,
even after a disagreement. Consequently

    Pr[output=s] >=1-2^-20-2^-10-2^-10-2^-12 >1-2^-8>2/3.    (12.3)

The finite branch has error <=2^-10. Thus the theorem is unconditional for
every N and s, and the all-branch resource guarantee has the same parameters.

## 13. Joint resource expressions

All estimates here are for n>=65536; the explicit exhaustive finite branch
changes absolute constants only. Put t=sqrt(2n). Section7 proves

    mu,m_*=O(sqrt n), u,ell=Theta(n^(1/4)),2^kappa=O(sqrt n),
    m_*+u<=mu<t+5, q=O(n^(1/4)2^(t-(2n)^(1/4))).

Section9 gives L<=1+u/8,K=O(sqrt n),Sodd=O(n^(3/4)), so
Rroots=O(n^(5/4)) including all two-adic retries. Thus the explicit cap is

    ALLQ<=1024(6q Rroots+2n)
        =O(n^(3/2)2^(t-(2n)^(1/4))).

The allocated classical layout is

    Mclass=O(n mu2^lambda_max+n^3)
          =O(n^2 2^(m_*+u-2u)+n^3)
          =O(n^2 2^(t-2(2n)^(1/4))).

The polynomial region is eventually dominated. Quantum allocation is
Pwire=2^16(n+1), so S_Q=O(n). All source/data/scratch, live siblings,
descriptors, schedules, tables and counters are included. Address width
is O(sqrt n) even with the larger odd-decoder grid.

F_merge=O(n) and Wtree=O(n(m_*+1)2^(m_*+ell))=O(n^2 2^t).
Multiplying by Rroots gives O(n^(13/4)2^t) RAW table work. Other terms
in the literal W* are lower order:

* Q*c_copy=O(n^5 log(n) 2^(t-(2n)^(1/4))) plus a polynomial.
* V=2^(ceil(log2q)+L+8)=O(n^(1/4)2^(t-7u/8)); even the n-stage
  overestimate n*c_dec=O(n^(11/4)2^(t-7u/8))+poly(n) is smaller.
* c_init=O(n^2 2^(t-2(2n)^(1/4)))+poly(n).
* c_set, root allowances and inter-stage work are polynomial.

For every fixed c and positive d, n^c exp(-d n^(1/4)) tends to0,
because its logarithm is c log n-d n^(1/4). This justifies each suppression
using actual fourth-root gaps, not a-sqrt(2). Consequently
Wcap=1024W*=O(n^(13/4)2^t) on every branch. Multiplying by the prescribed
O(sqrt n) address tariff gives

    T=O(n^(15/4)2^(sqrt(2n))).

The entire source, table, decoder and cap analysis concerns this SAME
configuration; replacing Sodd by n would lose the polynomial time gain.
All failed/rejected/restarted costs enter the conditional expected block
counts first and the explicit all-branch cutoff second.

## 14. Structured envelopes, indices and exact comparison

Use precisely the same rational a=u_333/v_333 as the source CS1. Its Pell
invariant proves a>sqrt(2). Time enclosure only replaces sqrt(2n) by
a sqrt n. Space enclosure uses

    n^2 2^(sqrt(2n)-2(2n)^(1/4)) /2^(a sqrt n-2n^(1/4))
      <=2^(2log2n-2(2^(1/4)-1)n^(1/4)),

which is bounded. Sample enclosure uses the positive difference
(2^(1/4)-1)n^(1/4). Its outside power remains3/2. No polynomial time
saving is manufactured from the rational a-sqrt(2) gap.

For bounds with positive leading c sqrt n and any fixed outside powers,
log2 B=c sqrt n+O(n^(1/4)+log n), so
log2(log2(max(2,B)))/log2n tends to1/2. The three exponential resource
indices are exactly1/2. For the qubit envelope n the index is0.

Exact comparison folds outside n^r into r log2n and retains exponent
coefficients. Relative to CS1-C3Q32076cd3-77d5-4058-813d-7e66be4714f8's
n^4 log2n 2^(a sqrt n), WTS1's log2 time ratio is
-(1/4)log2n-log2(log2n), tending to minus infinity. Relative to any
n^4 2^(a sqrt n) envelope it is-(1/4)log2n. These are genuine full-time
improvements conditional on this proof's mathematical correctness; equal
indices, sorting or currentBestScore cannot establish them. The declared
C,S_Q,Q,tolerance envelopes also match the privately reported RBS1 vector,
but its reserved source is not a proof premise or a claim of publication.
Newest published vectors must be checked again when choosing a submission.

Lower-memory algorithms may remain incomparable. WTS1 establishes neither
time index below1/2, 2^{O(n^(1/3))}, nor optimality of its bound. An equal
full vector would be a duplicate under earliest submission time/ID.

## 15. Tolerance, limitations and proof status

For the SAME WTS1 algorithm and parameters, epsilon(n)=0 for every N>=2:
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
