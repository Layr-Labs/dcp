# PSG-QSB: single-merge collimation with full-secret block decoding

## 0. Joint theorem and actual provenance

For every N>=2 and s in Z/NZ let n=ceil(log2 N), L=log2 n.
The ONE algorithm below recovers the entire s from independent ideal copies
with unconditional probability at least1-2^-8>2/3. On EVERY branch,
including failed attempts, rejected/discarded copies, wrong numerical
extraction, partial inputs and either cutoff, its joint representatives are

 T=O(2^((13/50)n)), S_C=O(n^2) classical bits,
 S_Q=O(n) qubits, Q=O(n^2) total acquired source copies.

All constants are absolute and independent of N,s,outcomes. These envelopes
apply for n>=2; the specified finite branch covers n=1. Their exact growth
indices are[1,0,0,0]. Guaranteed malformed fraction is0 in the independent
ideal-copy model. This is an exponential-time/quadratic-copy tradeoff, not
a smaller numerical time index, optimality result or cube-root algorithm.

Direct implementation/proof materials: this solver's PSG4-LIMIT submission
ae6bd13e-97a1-4009-8225-4b1b6bc3dea2 (hosted validating at drafting),
PSG5-LIMIT c07c0811-2485-4331-b055-d02391cb643c (first hosted execution
failed with exit2 and no mathematical verdict; exact local review valid),
and the original PSG5 source9f11a7a4-8d17-48f2-8658-892d3e378efa,
archive2e46e18cd6d60587394365bd89019196b002e15f. The eligible actual
ancestor PSG5-SHARP db0cc225-d7f0-475c-9b9d-21b3c15bac17 was directly
read and used in building those local materials. The inherited source
identities, collective extraction, verified-pair instrument, low-transcript
law and odd stride decoder are restated. Historical source credits include
PSR2,SLS,CS1,collective translations and held-out-block decoding. No source
verdict is a proof premise.

This candidate adapts this solver's unpublished local PSG-SB proof,
frozen intakeb88eccf4c6956f1984714a7df44f1ed506c5940135c749c1af120206838a256e.
Its real review was running when this follow-on draft was made. No prior
verdict is a premise. The immediate source's complete one-merge/modulus-route
construction is retained. The NEW operation is counted coherent threshold
search on the measured classical records, replacing classical grid sweeps.
 The block decoder replaces bit-by-bit parity extraction. This
prevents a large2-adic factor from forcing a nearly n-bit merge in the
small-odd-part case. The time is polynomial(n)2^(n/4), with the strict
13/50>1/4 gap absorbing the polynomial. Query/time interpolation already
exists in the literature; no first-ever tradeoff claim is made. The Remaud,
Schrottenloher,Tillich paper2206.14408 was read for comparison, and supplies
no algorithmic or proof subroutine used here.

## 1. Charged implementation conventions

All arithmetic is on explicit bit strings. A w-bit add, comparison, copy or
increment has O(w) Boolean gates using ripple carry, with O(w) scratch.
Reversibly compute a Boolean circuit, copy out its answer, then reverse it;
a permutation can be computed into a fresh register, swapped, and erased by
its inverse. NOT, CNOT and Toffoli suffice, and Toffoli has an exact constant
Clifford+T decomposition. Wire counters, generation, initialization, resets,
measurements and classical reads/writes are counted. Every indexed action
also pays O(log(S_C+S_Q+2)) bit operations. Gates are generated in streaming
order; no circuit description of exponential length is stored.

Only H, S, S-dagger and these exact reversible gates are used. In particular,
there is no arbitrary-N QFT circuit or approximate rotation to synthesize.
Fourier LABELS are inferred by nondestructive translation tests, with their
precision, tests and global error budget charged below. The source is used
only for fresh mixed copies; no purification, preparation inverse/control,
QRAM, hidden-shift oracle or subset-sum oracle is available or used.

Write N=2^a2 M with M odd, d=floor(log2 N), omega=exp(2 pi i/N),
s1=s mod M and s=s1+M s2 (mod N), 0<=s2<2^a2.

## 2. Source identities and exact transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into
rho_s = (1/N) sum_x |psi_x><psi_x|, with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,       (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each copy is literally a convex mixture, with
uniform weights, of the product states phi_k(s) (x) chi_k. The whole algorithm
is a linear (adaptive) quantum instrument applied to independent copies. So
the joint law of all its classical outcomes equals the law obtained by first
drawing, for every copy, an independent uniform latent label k, and then
running on the product state phi_k(s) (x) chi_k. All probabilities below use
this model. Applying X to the control maps phi_k(s) to, up to a global phase,
the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each
is a permutation of all 2^n data encodings, extended by the identity on
encodings >= N. Each maps the copy exactly to rho_s' for a known transformed
secret s'. The latent-label model is then applied to rho_s' via (3.1), so the
latent label of a copy is the Fourier label of its TRANSFORMED data register,
which EXTRACT recovers.

(T1) Mult_alpha: u -> alpha u mod N, for a known alpha coprime to N. Since
x -> alpha x is a bijection of Z/NZ, the copy becomes exactly rho_(alpha s).
It is implemented with n controlled modular additions of the constants
alpha 2^v mod N into a clean register, a swap, and the inverse computation with
alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for a known c.
Since |1,x+s> becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This
takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N,
an addition, a comparison and a selector. It is the identity on encodings
>= N, uses O(n) Boolean gates, and is computed cleanly: compute, swap or XOR
the result out, then uncompute.

## 3. Finite-precision classical table and source-label extraction

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20
of cos(2 pi v/4096) and sin(2 pi v/4096).

- Bound pi within 2^-90 using Machin's formula pi = 16 atan(1/5) - 4 atan(1/239),
  summing the first 40 terms of each alternating arctangent series. This gives
  two-sided bounds; the tails are below 16 (1/5)^81/81 + 4 (1/239)^81/81 < 2^-91.
- The identity follows from tan(2 atan(1/5)) = 5/12, tan(4 atan(1/5)) = 120/119
  and tangent subtraction.
- At the angle 2 v p_mid/4096 < 7, where p_mid is the midpoint of the pi bounds,
  sum 80 Taylor terms. The remainder is <= 7^81/81! < 2^-170. The angle error
  is < 2^-89, and sin and cos are 1-Lipschitz.
- Round each value to denominator 2^20.

This is a fixed finite rational computation, charged once as an absolute
constant (not advice).

For x in [0,1) put tab_0(x) = Cos[floor(4096x)] and tab_1(x) = Sin[floor(4096x)],
and let cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                    (4.1)


EXTRACT uses Qcap fixed in Section 8. Put J_e=n+4,

    h=ceil(log2(2^16 Qcap (n+5))), F=2^21 h.

It runs RUN(F) below once, without verification, fallback or restart.
Conditional on the latent label k, the data register is unchanged by every
test. Afterward discard that register and keep its control qubit, applying X
when the positive phase convention is needed. The latent-label mixture makes
this procedure valid for the mixed source, without access to its purification.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k.
A TEST WITH SHIFT c (0 <= c < N) works as follows. Prepare an ancilla in |+>.
Apply Tr_((N - c) mod N) controlled by it, so the |1> branch gets eigenvalue
omega^(k c). Measure the ancilla in X (H then Z) or in Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi c k/N) or sin(2 pi c k/N). Conditioned on
k, chi_k and every spectator are unchanged and outcomes are independent. A test
at LEVEL j is the test with shift 2^j mod N. Each test costs one controlled
modular addition, O(n) core steps.

### Level-wise extraction RUN(F)

For each basis take F collective ROUNDS. In one round prepare J_e+1=n+5
ancillas in |+>, representing x=sum_(j=0)^J_e x_j2^j. Compute z=x modN
coherently, apply the register-controlled translation u<-u-z modN to the
data, and uncompute z and reduction scratch. This equals the product of
all individually controlled translations Tr_(-2^j). To compute the remainder,
x<2^(n+5)<64N since N>2^(n-1); six compare/conditional-subtract steps with
32N,16N,...,N suffice, keeping their six borrow flags for reversal.
All arithmetic has O(n) wires and O(n) exact reversible gates. On the
Fourier eigenstate chi_k the ancilla state is EXACTLY

    tensor_(j=0)^J_e (|0>+omega^(k2^j)|1>)/sqrt2,

while data and spectators are unchanged. Measure all ancillas in the chosen
X or Y basis, add each outcome to its own empirical counter, and reset the
ancillas before the next round. Conditional on k these outcomes are
independent across levels and rounds, with exactly the same means as the
separate tests. Thus each level still has F tests per basis and the same
concentration and unwrapping proof. No approximate QFT or rotation is used.

The n+5 counters each have O(log F) bits. Updating all of them costs
O(n log F) per round even with conservative ripple increments; their total
storage is O(n log F)<=O(n^2). Round-loop and gate-generation bookkeeping
are charged as well. Here log F=O(log n)=O(L), since h=O(log n)=O(n).
The quantum translation costs O(n) per round. Decoding and unwrapping add
O(n^2) core operations. Consequently a full call costs

    O(n h L+n^2 L) core operations,

with O(n) qubits, O(n^2) classical bits. The literal polynomial source
cap of Section8 gives h=O(log n), so this is O(n^2 L) per complete call.
All finite exceptions are absorbed by an absolute constant, using the
same fixed round counts. The source label error bound below is unchanged.

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
RUN(F(h)) uses 2F(h) collective rounds supplying 2(J_e+1)F(h)
individual outcomes, at the charged cost proved above.


Since e^-h <= 2^-h, the per-call probability of an incorrect label is at most
4(n+5)2^-h <= 1/(2^14 Qcap). The union bound for at most Qcap adaptive calls is
2^-14, including discarded copies. Couple to an ideal run which outputs the
true latent label on every call, ignoring EXTRACT's internal test outcomes.
No later choice uses those internal outcomes. This coupling preserves the
untouched-bit argument; one does not condition it on extraction succeeding.
Each call takes O(n h L+n^2 L)=O(n^2 L) core operations under the actual
polynomial source budget, O(n) qubits and O(n^2) classical bits. Store the n+5 six-bit
directions and their empirical counters explicitly. All loops have fixed bounds.

## 4. SINGLE(D,B): one merge and exact phase compression

For0<=B<D<=n, a supplier returns fresh known uniform D-bit labels a and
phase qubits pq_a(th)=(|0>+exp(2pi i a th)|1>)/sqrt2, at at most two
original copies in expectation. Exact suppliers are specified in Sections6-7.
ForB=0 return one supplier qubit and its label W=a. Otherwise obtain
r=B+1 fresh supplier qubits. After building them, check and increment the
flat attempt counter of Section8. Use the combiner below with k=r,b=B,p=0.
On FAIL discard/reset the entire input collection and regenerate fresh
suppliers. On success its label x is divisible by2^B; return W=x/2^B and
the phase qubit pq_W(2^B th). No label, including zero, is rejected.

Set the uniform nominal factor q0=n+1 for all roots and decoder grids.
Every successful output uses at most n original suppliers, and its signed
integer label has magnitude less than(n+1)2^D. All full-label arithmetic
uses widthD+ceil(log2(n+1))+32=O(n), even on wrong numerical-label branches.
No symbolic incidence vector is stored. Supplier acceptance and every
retry acquisition are charged. The source cutoff prevents an infinite
rejection sequence on any actual branch.

### 4.1 Exact state preparation and verified-pair output

The inputs are phase qubits with full signed labels a_1,...,a_k divisible by
2^p, where k=b+1, b=B, p=0. Their joint state is

 2^(-k/2) sum_(y in{0,1}^k) exp(2pi i th A(y))|y>, A(y)=sum_j y_j a_j.

Set c_j=(a_j/2^p) mod2^b. Reversibly compute f(y)=sum_j y_j c_j mod2^b,
measure it to obtain e, and reset that measured register. The remaining
phase state has equal magnitudes on C_e={y:f(y)=e}.
Hold this original register untouched during discovery on SEPARATE query
registers. The discovery procedure below returns at most64 distinct,
classically verified members of C_e, using only c_j,e and fresh random bits.
It need not certify completeness. Sort the found strings and pair adjacent
ones, dropping an unpaired singleton. Reversibly compute on the original y
a success flag and a constant-size pair ID from equality tests with the
known list, then measure them. If y matches no pair, FAIL and discard.
Otherwise it is now an equal-magnitude superposition of exactly two known
strings y0,y1, with their original phases. Reset measured flags from their
known values. XOR y0 into y, choose a differing pivot, and use CNOTs from
that pivot to clear every other differing position. The surviving qubit has
label a'=A(y1)-A(y0), a FULL signed integer, not reduced modulo2^D or N.
Every successful branch is exactly this phase qubit, up to global phase,
regardless of whether discovery found the entire fiber.

The output is divisible by2^(p+b), since both selected strings have residue e.
It has a nonzero symbolic incidence vector in{-1,0,1} over distinct original
leaves: y0!=y1 differs in some child, child incidence vectors are nonzero,
and child leaf sets are disjoint. This induction starts at a single leaf.
Full labels are stored, but ALL choices of found strings and pairs, and
all success probabilities, factor through input residues modulo2^(p+b).
The unknown phase th is absent from this selection kernel. Computing a
full output label after selection does not add a selection rule on its high
bits. This distinction is used in the marginal argument of Section5.

### 4.2 Bounded discovery, exact Clifford+T circuits

Fix C=64. If k<=7, enumerate at most128 strings and retain the first64
solutions; this has constant enumeration length. If k>=8, use at most64
search blocks. Each block makes at most64 trials, stopping at its first
new verified solution, which is added to the list. Stop discovery after an
empty block or after64 found solutions. The list never contains a duplicate
or a false solution. On each trial:

 * Set J0=2^ceil(k/2), draw uniform j in[0,J0) with ceil(k/2) fair bits.
 * Prepare a fresh k-qubit query in |+>^k. Apply j Grover iterations for
   membership in C_e minus the found list. Measure its candidate string.
 * Verify its residue and novelty classically. Reset query registers before
   the next trial. The original phase-index register is not touched.

Membership is a COUNTED circuit. Controlled additions of the known b-bit
constants c_j compute f(z) in O(kb) gates; compare with e, exclude at most64
known strings with equality flags, apply Z on the computed flag, then
uncompute. This uses O(kb+64k) gates and O(k+b) scratch up to fixed constants.
Diffusion about |+>^k is H^k, a multi-controlled sign flip and H^k; a clean
Toffoli chain implements the sign flip in O(k) gates and scratch. Z=S^2.
All are exact Clifford+T. Known weights and strings are read by a classical
loop emitting gates; no quantum-addressed lookup, QRAM or stored circuit of
exponential length occurs. Gate generation, verification, fair bits, counters,
measurements, resets and all oracle work are charged.
There are at most4096 trials, each with fewer than J0 iterations.
Here k=B+1<=n, b<=n and J0=2^ceil((B+1)/2). All residue arithmetic,
reflections, verification, the fixed list, streaming gate generation and
bookkeeping cost O(n^2 L) core work per iteration. The one full signed-label
update sums at most n labels of O(n) bits, also O(n^2 L), and is outside
the repeated oracle loop. Thus a complete attempt costs
O(n^2 L 2^ceil((B+1)/2)) core work and O(n) quantum scratch on every branch.
The separate physical-address charge O(L) is applied in Section9. All
counter, random-bit, reset and projection costs are included.
The fixed-size found list needs O(n) classical bits. All these are
branchwise limits, independent of search success.

### 4.3 Discovery probability and the measured-fiber moment

Suppose the measured fiber has at most64 members. At any search trial with
1<=m<=64 remaining solutions, let A=2^k and sin^2(gamma)=m/A. In the
normalized good/bad two-dimensional basis the marking reflection and
uniform-state reflection rotate by2gamma; therefore success after j
iterations is sin^2((2j+1)gamma). Summing the cosine geometric progression
for uniform j gives

 mean success=1/2-sin(4J0*gamma)/(4J0*sin(2gamma)).

For k>=8, m<=64<=A/2, hence sin(2gamma)>=sqrt(2/A) and J0>=sqrt A.
The mean is at least1/2-1/(4sqrt2)>1/4. A64-trial block consequently misses
while solutions remain with probability at most(3/4)^64<2^-16.
Over at most64 relevant blocks, premature stopping has probability at most
64*2^-16=1/1024. Once no solutions remain a block simply finds none;
no counting oracle is used. Small k is enumerated exactly up to the list cap.

Now suppose c_j are independent uniform residues in Z/2^b. The residue
measurement has the same probability law as e=f(Y) for an independent
uniform classical index Y. For each z!=Y, f(z)-f(Y) contains a coefficient
+1 or-1 of a uniform c_j and is uniform modulo2^b. Therefore

 E |C_(f(Y))|=1+(2^k-1)/2^b<3.

This is the SIZE-BIASED fiber law of the actual measurement. Markov gives
Pr[|C_e|>64]<3/64. If discovery is complete, the failure mass of dropping
one singleton from each odd fiber, averaged over residue outcomes, is
#odd_fibers/2^k<=2^b/2^k=1/2, for every fixed weight list.
Combining large-fiber, discovery-miss and singleton events yields

 Pr[success]>=1-3/64-1/1024-1/2=463/1024>1/3.              (4.1)

Equation(4.1) is an average over independent fresh uniform weights and search
coins. It is NOT asserted conditional on arbitrary fixed child labels.
For fixed labels, successful output correctness and the low-bit kernel
statement of4.1 still hold unconditionally. Section5 justifies complete fresh regeneration and the held-out root law.

## 5. Fresh attempts, signed root blocks and characteristic bound

Before every complete attempt, all r supplier labels are independent
uniform D-bit integers, conditional on external history before the fresh
suppliers. Their low B bits are therefore independent uniform weights.
Section4.3 gives fresh-call success>=1/3. Complete failures release every
input and restart, so attempts have geometric tail at most(2/3)^j.
SINGLE terminates almost surely in the ideal uncapped process. Its expected
attempt count is at most3 and its expected acquired copies at most6r.
ForB=0 these are zero merge attempts and at most two copies. No cost/success
independence within one attempt is assumed: reaching an attempt depends
on earlier attempts, then its conditional supplier cost is uniformly bounded.
Summing that geometric series gives the stated expectations.

Every accepted branch is the EXACT phase qubit of Section4.1 even when
discovery was incomplete. Its signed incidence vector z on the r original
supplier labels has entries in{-1,0,1}, not all zero, since the paired
binary index strings differ. Condition on the low-B parts, verified-search
choices/outcomes, residue, pair selection and retry history. These kernels
use only low-B parts and are phase independent, as proved in4.1-4.2.
Do not condition on irrelevant high EXTRACT records, full current labels
or later budget survival. Write a_l=u_l+2^B tau_l, where the tau_l remain
independent uniform in[0,A), A=2^h,h=D-B>=1. Then the full signed frequency
is W=c+sum_l z_l tau_l with fixed c. ForB=0,W is one uniform block directly.
Consequently for all real y,

 |E exp(2pi i yW)|<=D_A(y)=|(1/A)sum_(t=0)^(A-1)exp(2pi i yt)|,
 D_A(y)<=|cos(pi y)|,
 D_A(y)<=min(1,1/(2A||y||)) if||y||>0.                    (5.1)

Each unit coefficient contributes D_A and all other factors have modulus
at most1. Factoring the uniform block into fair binary digits gives
D_A(y)=product_(j=0)^(h-1)|cos(pi2^j y)|. The geometric sum and the sine
chord |sin(pi y)|>=2||y|| give the second displayed estimate. In particular
Pr(W odd)=1/2, though the new block decoder does not need to filter parity.
Also |W|<(n+1)2^h=q0*2^h. Fresh distinct SINGLE calls use independent
supplier sets; these conditional bounds hold uniformly over prior roots.

An additional bound is useful for exact-grid decoding:

 ||y||>=1/(2A) implies D_A(y)<=1/sqrt2.                    (5.2)

Indeed let x=||y|| in[2^(-h-1),1/2]. Repeatedly double x until it first
lies in[1/4,1/2]. This takes j<=h-1 steps (or j=0 if already there),
without an intervening wrap. The jth cosine factor has magnitude at most
cos(pi/4)=1/sqrt2, and all other factors are at most1. This also proves
the bound at both endpoints. Neither5.1 nor5.2 asserts a full integer
uniform law, or conditions on current high labels. The ideal process
marginalizes internal extraction records, and the real process is coupled
additively in Section8, not conditioned on all labels being correct.

## 6. Odd-part recovery and a short-modulus exact-grid decoder

For the main n>=256 configuration put H=ceil(n/2) and use the SAME integer

 K=2^13*(n+ceil(log2 n)+40)

in every measurement stage. q0=n+1 is fixed before execution.
IfM=1 set s1=0 and skip odd recovery. ForM>=3 choose one of the following
TWO routes, depending only on the known modulus.

### 6.1 Large odd part: a2<=d-H

Use h=H,B=d-H>=a2,D=d,stride=H-4, and nq=2^(H-1)q0.
This route is the complete held-out-block stride decoder below. Every
PS_TREE(d,B) mentioned there means SINGLE(d,B). Its root supplier and
CRT transform are explicitly included.

The stages are j=0,...,J, where J is least nonnegative with
2^((J+1)*stride+2)>2M. Put Sodd=J+1. Because stride>=1, Sodd<=n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^(j*stride) (2^(B-a2))^(-1) (mod M). Then alpha_j is a
unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run EXTRACT to obtain k, and accept iff k < 2^d (otherwise discard the copy and
  acquire again);
- on acceptance, apply X to the control.

In the ideal run, accepted labels are i.i.d. uniform on [0, 2^d), each copy is
accepted with probability 2^d/N > 1/2, and the qubit is pq_k(alpha_j s), i.e. it
has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^B W th = W 2^(B-a2) alpha_j s / M = 2^(j*stride) W s1 / M   (mod 1),            (9.1)

because 2^(B-a2) alpha_j = 2^(j*stride) (mod M) and s = s1 (mod M). So a SINGLE(d,B) root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^(j*stride) W.

Measurement. For i = 1..K:
- run SINGLE(d,B);
- obtain a fair bit beta_i by measuring H|0>;
- measure the root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in {+1,-1}
  together with W_i and beta_i.

Ideally E[Z_i | f_i, beta_i] = cs_(beta_i)(f_i theta) with f_i = 2^(j*stride) W_i.

Candidates. Put P_j = j*stride + ceil(log2 nq) + 8, and identify an integer c with the
point zeta = c/2^(P_j) on the circle R/Z.
- Stage 0 uses every c in [0, 2^(P_0)).
- Stage j >= 1 uses every c whose point lies within circular distance
  rad_j = 2^-(j*stride+2) of the previous center z_(j-1). This is one or two explicit
  integer intervals.
- Both z_(j-1) (denominator 2^(P_(j-1))) and rad_j are multiples of 2^-(P_j),
  so the two arc endpoints are themselves candidates.
- There are at most 2^(ceil(log2 nq)+7) + 2 <= 2^(ceil(log2 nq)+8) candidates.

The candidate set is fixed by information available at the start of the stage.

Score. For each candidate, using exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

The trigonometric entries have exact denominator2^20. A candidate is
MARKED when its computed score is at least(481/1000)K, implemented by
comparing the signed integer2^20score to ceil(481*K*2^20/1000).
Use QSEARCH of Section6.4 on the one/two known candidate intervals, and
let z_j be its returned marked candidate divided by2^P_j. If QSEARCH
finds none within its fixed trials, abort and output0. Every returned
candidate is classically reverified. This searches the stated fixed grid;
it does not assume access to an uncharged maximum-finding oracle.

Lemma 6.1. Suppose theta is within circular distance rad_j of z_(j-1) (no
condition when j = 0). Then, in the ideal run, with probability at least
1 - (2^-20+2^-30)/n, theta is within circular distance 2^-(j*stride+stride+2) of z_j.

Proof. Let Fs_i be the sigma-field of everything up to and including root i
of the stage, and Gt_i the sigma-field of Section 5 for tree i. For a
candidate point zeta, let Delta = theta - zeta, taken as a circular
difference, and let xi_i = Z_i cs_(beta_i)(f_i zeta). Conditional on
Fs_(i-1), Gt_i and the held-out blocks of tree i (hence on W_i), averaging over the
fair basis bit gives

    E[xi_i | ...] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(..) sin(..)]
                  = (1/2) cos(2 pi f_i Delta).

By (4.1), the computed score differs from sum_i xi_i by at most K/625.

Near point. Let zeta0 be the candidate nearest theta. In stage 0 the
candidates cover the circle. In stage j >= 1 the candidate arc contains theta
and has candidate endpoints. Either way |Delta0| <= 2^-(P_j + 1). Since
|f_i| < 2^(j*stride) 2 nq,

    |f_i Delta0| < 2^(j*stride+1) nq 2^-(P_j + 1) <= 2^-8.

So E[xi_i | Fs_(i-1)] >= (1/2) cos(pi/128) for every realization.

Far points. Call zeta far if |Delta| >= 2^-(j*stride+stride+2). In stage 0 we always have
|Delta| <= 1/2. In stage j >= 1, both theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j*stride+1). Hence xx=2^(j*stride)|Delta| lies in[2^(-stride-2),1/2]
for each far candidate. Fresh trees are independent of Fs_(i-1), conditional
on its low transcript. Averaging the fair basis and the full signed root
frequency gives

 E[xi_i | Fs_(i-1)] <=(1/2)D_(2^h)(2^(j*stride)Delta).

If h<=4, stride=1 and xx>=1/8, so the cos bound is at most cos(pi/8).
If h>=5, stride=h-4 and xx>=2^(-h+2); the block bound is at most
1/(2*2^h*2^(-h+2))=1/8<cos(pi/8). Thus the SAME old far-point score
upper bound (1/2)cos(pi/8) holds uniformly for every stage and modulus.
The larger frequency range is already included through nq=2^(h-1)q0.

Concentration. For each fixed candidate, sum_i (xi_i - E[xi_i | Fs_(i-1)]) is a
martingale whose increments lie in intervals of length 2. By Azuma-Hoeffding
it deviates by at least K/64 with probability at most
exp(-(K/64)^2/(2K)) = exp(-K/8192). Outside these events for zeta0 and every far
candidate,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625
                 >  (K/2) cos(pi/8)   + K/64 + K/625 >= score(far zeta),

because the explicit threshold satisfies

 (1/2)cos(pi/128)-1/64-1/625 >481/1000,
 (1/2)cos(pi/8)+1/64+1/625 <481/1000.

These inequalities can be checked with rational bounds: pi<22/7 and
cos x>=1-x^2/2 give the first; pi>157/50 and
cos x<=1-x^2/2+x^4/24 at x=157/400 give the second. The pi interval
is also supplied by Section3's explicit computation. Thus the nearest
candidate is marked and EVERY marked candidate is not far.
There are at most2^(ceil(log2nq)+9) concentration events. The same larger K
bounds their union by2^-20/n as before. Conditional on these events not
occurring, QSEARCH has a nonempty marked set and fails with probability
at most2^-30/n; any verified marked result is sufficiently close.
Their sum proves Lemma6.1 for the actual quantum search. QED.

For stage j+1 the hypothesis of Lemma 6.1 is the conclusion of stage j, since
2^-(j*stride+stride+2) = rad_(j+1). By induction, except for the summed per-stage errors, theta
lies within 2^-((J+1)*stride+2) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.


Stage-count and K audit. Here stride=H-4>=n/4 for n>=256.
The least stage count Sodd=J+1 is at most5 from its explicit defining
inequality and log2M<=n. Also ceil(log2nq)=H-1+ceil(log2(n+1))<=n+10,
so our common K is at least the original proof's
2^13*(ceil(log2nq)+ceil(log2n)+30). The displayed concentration and union
bounds therefore hold with this larger actual K. They give concentration-event error
at most2^-20/n, plus QSEARCH failure2^-30/n per stage. All candidate grids have at most O(n2^H) points and all
loop counts are fixed before outcomes. No odd factorization is needed.

### 6.2 Exact-grid decoder DIRECT(G,h)

This routine takes independent fresh roots pq_W(theta), where theta=t/G
for unknown t in{0,...,G-1}, A=2^h and G<=2A. Their W satisfy5.1-5.2,
uniformly conditional on previous independent root history. For each of K
roots choose a fair basis beta, measure X orY and record Z in{+1,-1},W,beta.
For every candidate j=0,...,G-1 compute the exact rational score

 score(j)=sum_i Z_i tab_(beta_i)(((W_i*j) modG)/G).

Mark a candidate when score(j)>=(481/1000)K using the same exact
integer comparison, and use QSEARCH over j=0,...,G-1. Return its verified
marked j or abort after its fixed trials. The coherent predicate streams
all K classical records with counted arithmetic, as Section6.4 specifies.
There is no quantum Fourier transform, approximate rotation or QRAM.

Proof. Let xi_i=Z_i cs_(beta_i)(W_i*j/G). Conditional on W_i and averaging
the fair basis, its mean is(1/2)cos(2pi W_i(theta-j/G)). For j=t the mean
is exactly1/2. For j!=t circular distance is at least1/G>=1/(2A), so5.2
gives conditional mean at most1/(2sqrt2), after marginalizing current W.
The approximation4.1 changes scores by at mostK/625. Azuma with deviations
K/64 gives each tail probability exp(-K/8192); it is derived by bounded
interval-length-two increments just as in6.1. Since

 (1-1/sqrt2)/2>2/64+2/625,

the true candidate has score/K at least1/2-1/64-1/625>481/1000.
Every wrong candidate has score/K at most1/(2sqrt2)+1/64+1/625<481/1000
(use1/sqrt2<=5/7 for a rational certificate). Outside the concentration
tails the ONLY marked candidate is the true one. There are at most
G+1<=2^(h+2)<=2^(H+2) relevant events. e^-x<=2^-x and our K bound their
union by2^(H+2-n-ceil(log2n)-40)<=2^-20/n.
On this event QSEARCH returns the true candidate except with failure
probability2^-30/n. The combined stage error is at most(2^-20+2^-30)/n,
conditional on previous correct stages, with no independence assumption.

### 6.3 Small odd part: a2>d-H and M>=3

Put D=d,B=d-H<a2,h=H,A=2^H,G=N/2^B. Here2^B dividesN, and
2^d<=N<2^(d+1) gives A<=G<2A. The root supplier acquires a fresh raw
source copy, runs EXTRACT, rejects unless k<2^d, and appliesX to the
control on acceptance. Accepted labels are independent uniform d-bit
integers and each supplier costs at most two copies in expectation.
SINGLE(d,B) has phase exp(2pi i2^B W s/N)=exp(2pi i W s/G).
Run DIRECT(G,H) to get t=s modG and set s1=t modM. Since M dividesG,
this gives s modM. The routine uses exactly one stage; no costly
almost-n-bit merge is inserted to cancel a large2-adic factor.

### 6.4 QSEARCH: fixed-loop counted quantum score threshold search

The candidate set is a known ordered list of Dcand integers: a complete
DIRECT interval, or the one/two explicit binary-grid intervals of6.1.
Let p=ceil(log2Dcand), Tpad=2^p. A p-bit ordinal u<Dcand maps reversibly
to its candidate by comparison with the first interval length and addition
of the appropriate known endpoint. Invalid padded indices are unmarked.
IfDcand=1 evaluate its predicate classically and return it if marked,
otherwise fail. Every actual main-stage set has at least two points.

There is a COUNTED exact phase predicate for valid candidates with score
at least(481/1000)K. The records (W_i,beta_i,Z_i) are classical constants
fixed BEFORE this search. Stream all K records in a classical gate-generation
loop. For each, reversibly compute its argument W_i*c mod2^P or W_i*j modG
using ripple modular arithmetic. The fields have O(n) bits; repeated
controlled addition implements multiplication in O(poly(n)) gates with
O(n) scratch. Compute floor4096residue/G (or its binary-grid counterpart)
by explicit arithmetic: the quotient has at most12 bits, so12 comparisons
and conditional subtractions of known multiples ofG suffice. Scan the
fixed4096-row rational trigonometric table with equality flags to obtain
the signed20-bit entry, apply the known sign Z_i, add it to an
O(log K+20)-bit signed score accumulator, and uncompute all per-record
scratch. The known basis beta_i selects Cos orSin. All table constants,
record reads, wire indices and gate generation are charged.
After the last record compare the score to ceil(481*K*2^20/1000), combine
with validity and phase flip; reverse the entire score computation.
This is an exact Clifford+T circuit with polynomial(n) work per query and
O(n) scratch. Streaming known records is not quantum-addressed memory;
no QRAM, free arithmetic or preexisting search oracle is used.

Perform exactly at most Ntrial=256*(ceil(log2 n)+40) trials, stopping at
the first classically verified marked result. In a trial a fair classical
bit chooses direct uniform measurement or random-length Grover:
prepare H^p|0>; in the direct branch measure its ordinal; in the Grover
branch choose j uniformly in[0,J), J=2^ceil(p/2), perform j iterations
of the counted predicate and the exact reflection about H^p|0>, then
measure. Check validity and recompute its score classically before accepting.
Reject/uncompute/reset between trials. If none succeeds, abort/output0.
The reflection uses H gates, an exact reversible all-zero test and Z.
All trial loops and j ranges are fixed, even if no marked candidate exists.

Success bound when the marked set is nonempty. If f is its fraction in
the padded Tpad and f<=1/2, then J>=sqrt(Tpad), f>=1/Tpad and
Jsin(2theta)>=1 for theta=arcsin(sqrt f). The random-iteration identity
of4.3 gives mean Grover success at least1/4. If f>=1/2 the direct half
alone succeeds with probability at least1/4. Thus each mixed trial
succeeds with probability at least1/8 in all cases, including f=1.
Trials on fresh query registers are independent for the fixed records.
Failure probability is at most(7/8)^Ntrial<=exp(-Ntrial/8)
<=2^(-Ntrial/8)<=2^-30/n. On a good concentration transcript every
returned mark is near (odd route) or exactly true (DIRECT), as proved.

The work is polynomial(n)Ntrial*2^ceil(p/2), including every failed query,
verification, reset and address charge. Because Dcand<=O(n2^H), this is
O(poly(n)2^(H/2)). Candidate registers, score, comparison, multiplication
and diffusion scratch use O(n) qubits. All phase-bearing roots have already
been measured and released before QSEARCH; only their classical records
remain. Even arbitrary wrong-label records respect these fixed resource
limits and the maximum trial count.

## 7. Two-adic recovery in blocks

Ifa2=0 set s2=0 and skip. Otherwise, conditional on correct s1, write
s=s1+M s2 modN,0<=s2<2^a2. Begin g=0,s2low=0. At a stage put
wd=a2-g,h=min(wd,H),D=wd,B=wd-h. Let
sh=s1+M s2low modN,rem=(s2-s2low)/2^g in Z/2^wd. A supplier acquires
a fresh copy, applies Shift_sh, runs EXTRACT, appliesX to the control,
and uses kk=k mod2^wd as label. Since2^wd dividesN, kk is uniform in
[0,2^wd), and the qubit's phase is exp(2pi i kk rem/2^wd).
SINGLE(wd,wd-h) gives phase exp(2pi i W rem/2^h), with the law of5.1-5.2.
Run DIRECT(2^h,h) and let t be its answer. Update
s2low<-s2low+2^g*t and g<-g+h. Continue until g=a2, then set s2=s2low.
At most ceil(a2/H)<=3 stages are used. A correct stage appends exactly the
next h low bits. IfM=1, s1=0 is already known and this same procedure
recovers the entire secret without odd recovery. No odd-W filtering or
single-bit retry remains. Every root, even a zero frequency, is counted.
The final answer is(s1+M s2) modN.

## 8. Complete algorithm, literal caps and unconditional success

For n<256 use exhaustive testing: for t=0,...,N-1 acquire at most n+10
fresh copies, subtract t controlled by the first qubit, measure X and
reject on first minus. Output the first candidate passing all tests or0.
The true s always passes; each wrong candidate passes independently with
probability1/2 per fresh test. Wrong output probability is below
(N-1)2^(-n-10)<2^-10. Work O(Nn^4),copies at mostN(n+10),qubitsO(n),
classical bitsO(n^2). This fixed finite prefix fits all stated asymptotic
bounds by absolute outside constants.

For n>=256 compute H,K and set the deterministic maximum root count
Hroot=8K. Section6.1 needs at most5 stages and Section7 at most3; the
alternative6.3 needs only one initial stage. Define integers

 Qstar=6(n+1)Hroot,Qcap=1024Qstar,
 Wstar=3Hroot,Wcap=1024Wstar.

The acquisition counter counts every original source copy, including
rejections, failures and discarded states. Before exceeding Qcap abort,
release all registers and output0. The flat attempt counter counts every
complete positive-B merge. Check it AFTER building its fresh inputs but
BEFORE executing the merge; abort likewise if its next increment exceeds
Wcap, otherwise increment and perform the whole attempt. B=0 roots have
no merge attempt. EXTRACT uses exactly this fixed Qcap. Run Section6's
chosen route and Section7, then output their combined answer.

In the ideal uncapped process, uniformly over earlier history each root
uses at most6(n+1) expected acquisitions and three expected attempts by
Section5. Thus totals have expectations at mostQstar,Wstar. No independence
of an attempt's cost and success is assumed; the fresh-call conditional
geometric sums prove the bounds. Markov bounds each cap event by2^-10.
A work abort before the next attempt means the uncapped total WOULD exceed
Wcap; already built inputs are already charged. At most eight measurement
stages have per-stage concentration-plus-search error(2^-20+2^-30)/n.
For n>=256,8*(2^-20+2^-30)/n<2^-20, so their combined
conditional error is at most2^-20. Label extraction is coupled to exact
latent labels until first error, with error probability at most2^-14 over
the literal Qcap by Section3. Do not condition the ideal unused-block law
on all numerical extractions being correct. The union bound gives total
failure at most2^-10+2^-10+2^-14+2^-20<2^-8. This includes either abort.
The finite branch also meets that guarantee. No successful subtree,
measurement or accepted result is postselected free of charge.

## 9. Every-branch charged resources and exact indices

All positive cancellations have B<=n-H, as in Sections6-7. The flat Wcap
is O(n), and4.2 bounds total merge work by
O(poly(n)2^((n-H+1)/2))=O(poly(n)2^(n/4)). The root search, verification,
projection, full labels, generation, failed attempts and partly built
input collections are all counted. Literal Qcap=O(n^2) bounds all original
acquisitions and their polynomial extraction/transform work.

Each decoder stage's predicate is the explicit streamed-score circuit
of6.4, not an uncharged score oracle. At mostNtrial=O(log n) searches run,
each with fewer than2^ceil(p/2) counted iterations and polynomial work
per iteration. Dcand<=O(n2^H) implies p<=H+O(log n). Since H=ceil(n/2),
the TOTAL decoder work across at most eight stages is
O(poly(n)2^(n/4)). Classical record construction, interval endpoints,
verification, resets, initialization and the fixed rational table are
included. Physical addresses pay O(log n), still within the polynomial.
Thus on every branch, including all search failures and either cutoff,

 T=O(poly(n)2^(n/4))=O(2^((13/50)n)),

because13/50-1/4=1/100>0 and log2poly(n)=O(log n)=o(n).

Input labels and K classical measurement records use O(n^2) bits; every
stage releases old records. Merge/query/extraction workspaces use O(n)
qubits. During decoding the phase roots are already released, and QSEARCH
uses p=O(n) candidate bits plus O(n) arithmetic/diffusion scratch. Therefore
S_C=O(n^2),S_Q=O(n) jointly with the same Q=O(n^2) source cap. All
wrong-label branches respect the fixed widths. The finite branch enlarges
only absolute outside constants.

The exact index of the submitted pure time envelope is1, and all three
polynomial resource envelopes have index0. Only time contributes numeric
score[1]. The quantum threshold search strictly improves the immediate
single-merge construction's time coefficient while retaining its complete
space, copy and clean-success guarantees; no numerical-index, optimality
or cube-root breakthrough is claimed.

## 10. Malformed copies

The guaranteed fractional expression is epsilon(n)=0. Every acquired copy
is an independent ideal coset state. No positive unflagged corruption,
heralded erasure tolerance or impossibility of greater tolerance is asserted.
Under this promise all four every-branch bounds and the unconditional
full-secret probability are joint guarantees proved above.
