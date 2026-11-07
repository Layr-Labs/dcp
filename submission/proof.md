# RQ-QSB: robust single-merge blocks with counted quantum score search

## 0. Joint theorem and actual materials

For every N>=2,s in Z/NZ put n=ceil(log2N). The ONE algorithm below,
under ModelM including the all-honest clean case, recovers the full s with
unconditional probability at least1-2^-8>2/3. On EVERY branch its joint
full representatives are

 T=O(2^((13/50)n)), S_C=O(n^2) classical bits,
 S_Q=O(n) qubits, Q=O(n^2) total acquired ORIGINAL source copies.

All outside constants are absolute and independent of N,s,outcomes and
the admissible online strategy. The declared malformed fraction is
1/(131072*n). The four exact indices are[1,0,0,0]. This is a faster-time,
higher-copy, lower-tolerance tradeoff than the linear-copy constant-noise
construction, not a smaller numerical growth index or optimality claim.
The SAME protocol handles all n>=1, with finite small costs absorbed by
absolute constants; there is no unproved noisy exhaustive branch.

Immediate directly used materials are this solver's PSG-QSB public
submission70436d5e-40d4-489c-95e3-4cbc92c79cf0, genuine local and hosted
reviews valid (manual promotion not observed), for the complete block
routes and counted threshold-search circuit; and local RQ-LIN, full
pipeline intakec25eba345b5d9eedec3d17d823f73a2151f71392d8d6c300dcf491d0a7062df1,
genuine local atomic review valid after an unchanged-input binding-error
retry, for ModelM and honest-only extraction coupling. The local clean
Q-LIN intake1b2fa3ba6b34b1a2acabbeb7a6492ce6bc49e5044fe27fdfa518778c147d5fdc
also informed the zero-merge case. The public source/interface ancestors
actually read are PSG-SB1dd839ab-0ee6-4516-aa8d-89c390361d2a,
PSG4-LIMITae6bd13e-97a1-4009-8225-4b1b6bc3dea2,
PSG5-SHARPdb0cc225-d7f0-475c-9b9d-21b3c15bac17 and originalPSG5
9f11a7a4-8d17-48f2-8658-892d3e378efa,archive2e46e18cd6d60587394365bd89019196b002e15f.
All needed arguments are restated; no source verdict is a premise.

The NEW argument compares every actual attempt to an all-honest analytic
counterfactual and bounds all attempt prefixes. Conditioning actual
returned roots on being unmodified would be unsound: an adversary may
spoil a later input after seeing earlier labels. The proof does not use
that conditioning. Each edited attempt changes bounded score/count
contributions, while the full counterfactual stream has the required
martingale laws. Counterfactual variables are analytical Born-kernel
variables, not an algorithmic state-cloning or preparation operation.

## 0.1 ModelM: unflagged online replacement, actual fractional budget

For fixed known N and fixed secret s, an online adversary chooses a
CLASSICAL replacement bit before each acquisition, using N,s,previous
classical transcript and an arbitrary private quantum workspace. It has
no access to the current fresh honest draw or future algorithm coins
before this decision. A non-replaced call supplies a fresh rho_s,
independent as a tensor factor of all prior algorithm/adversary systems.
A replaced call supplies an arbitrary density operator on the same(n+1)
input qubits, possibly entangled with its private workspace and other
replaced calls. All algorithm gates and measurements remain ideal.
The controller receives NO replacement bit, flag or side information.
Every acquired copy, including rejected or discarded ones, counts.

At termination let Q be the ACTUAL number acquired. An admissible strategy
must ensure, almost surely over the protocol, that at most floor(epsilon(n)Q)
calls were replaced, for epsilon(n)=1/(131072*n). This is an input promise, not
conditioning/postselecting an otherwise invalid strategy on later budget
fulfillment. The online decision precedes the current honest copy; a
source cannot inspect a fresh honest label and then retroactively declare
that copy replaced. No independence of replacement positions, replacement
states or private workspace is assumed. Clean input is the no-replacement
strategy. Every success and resource claim is uniform over N,s and ALL
admissible strategies, with probability over all protocol/source randomness.
The bounds include every branch permitted by this model, not only successes.

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
precision, tests and global error budget charged below. Honest calls supply
fresh mixed copies; replaced states are governed by ModelM. The controller
uses only acquisition, and no purification, preparation inverse/control,
QRAM, hidden-shift oracle or subset-sum oracle is available or used.

Write N=2^a2 M with M odd, d=floor(log2 N), omega=exp(2 pi i/N),
s1=s mod M and s=s1+M s2 (mod N), 0<=s2<2^a2.

## 2. Source identities and exact transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into
rho_s = (1/N) sum_x |psi_x><psi_x|, with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,       (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each HONEST copy is literally a convex mixture, with
uniform weights, of the product states phi_k(s) (x) chi_k. For the complete adaptive instrument, one may draw a fresh uniform latent
label k whenever the source decision was HONEST, conditional on its prior
history, and apply that call to phi_k(s) (x) chi_k. Replaced-call states
and the private workspace remain unchanged in this representation; they
are not assumed independent or to have honest Fourier-label mixtures.
All source-frequency probability claims below use this honest-call model. Applying X to the control maps phi_k(s) to, up to a global phase,
the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact identities on an HONEST fresh copy are available before label extraction. Each
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

The numerical label correctness bounds in this section apply to HONEST
calls. On a replaced input the same fixed instrument is executed and
returns a label in[0,N), but no frequency or numerical correctness is
promised. Its work, registers and output range remain bounded on every
input state. All concentration/coupling statements below refer only to
honest calls, leaving replaced-call instruments unchanged.


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


EXTRACT uses Qcap fixed in Section8. Put J_e=n+4,

    h=ceil(log2(2^16 Qcap (n+5))), F=2^21 h.

It runs RUN(F) below once, without verification, fallback or restart.
Conditional on the latent label k, the data register is unchanged by every
test. Afterward discard that register and keep its control qubit, applying X
when the positive phase convention is needed. The honest latent-label mixture makes
this procedure valid for an honest mixed source, without access to its purification.

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
4(n+5)2^-h <= 1/(2^14 Qcap). The union bound for at most Qcap adaptive HONEST calls is
2^-14, including discarded honest copies. Couple to an ideal process which
outputs the true latent label on every HONEST call and retains the complete
replaced-call instrument, ignoring irrelevant honest internal test outcomes.
No later choice uses those internal outcomes. This coupling preserves the
untouched-bit argument; one does not condition it on extraction succeeding.
Each call takes O(n h L+n^2 L)=O(n^2 L) core operations under the actual
polynomial source budget, O(n) qubits and O(n^2) classical bits. Store the n+5 six-bit
directions and their empirical counters explicitly. All loops have fixed bounds.

## 4. Actual single-merge primitive and fixed protocol parameters

Compute for ALL n>=1

 H=ceil(n/2), stride=max(1,H-4), q0=n+1,
 K=2^28*(n+4ceil(log2n)+120), Hroot=16K,
 Tcap=128K, Qcap=512(n+1)K.

Bit lengths compute all ceilings exactly, including ceil(log2n)=0 at n=1.
The counters count EVERY original acquisition and EVERY primitive attempt,
INCLUDING B=0 calls. Source cutoff is checked before acquisition. The
attempt cutoff is checked after its fresh accepted inputs have been built,
but before a merge or B=0 return. Inputs already built are charged even
on an abort. EXTRACT uses this exact Qcap.

SINGLE(D,B),0<=B<D<=n, uses r=B+1 accepted suppliers (one ifB=0) from
the mode of Sections6-7. After building them, check/increment the global
attempt counter. Draw an independent fair basis beta by H|0> measurement,
kept with this attempt. IfB=0 return the supplier qubit, its label W and
beta. IfB>0 use the verified-pair combiner below with k=B+1,b=B,p=0.
On FAIL discard/reset ALL inputs and beta and regenerate whole suppliers;
on success return its qubit, the signed integer W=x/2^B, and beta.
The decoder measures every returned qubit in this attached basis immediately.
A fair beta on failed attempts is simply discarded. The coins used in
combining/searching are fresh after all input-source decisions, and beta
is not used to select pairs or the success flag.

Every numerical supplier label has D bits; every signed sum has fixed
width D+ceil(log2(n+1))+32. Verified pairs have equal numerical residue
modulo2^B, so W is an integer on all accepted branches, even malformed
ones. Always |W|<(n+1)2^(D-B). Phase correctness is asserted only for an
all-honest ideal attempt with the semantic source phase of its current
correct decoding history. On other attempts the output may be arbitrary,
but the classical label, bit outcome and every circuit remain bounded.
The primitive receives no replacement flags.

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

For an ALL-HONEST COUNTERFACTUAL attempt, c_j are independent uniform residues in Z/2^b. The residue
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
statement of4.1 still hold unconditionally. Section5 establishes the counterfactual root law and transfers it by bounded edits; it never conditions actual attempts on being unmodified.

## 5. Counterfactual attempts and robust prefix scores

### 5.1 Ideal kernels, frequencies and an actual/ideal coupling

For a complete all-honest input collection, fresh stored labels are
independent uniform D-bit integers. Their low B weights are uniform, so
4.3 gives ideal success probability at least1/3 before input generation.
ForB=0 success is1. These success probabilities are phase independent:
the input index has uniform magnitudes, success/projection kernels are
diagonal in its index, and searches use separate registers. The probability
statement remains true even after an earlier decoding error, when physical
honest phases may no longer match the stored reduced-label semantics.

When the previous decoding history is correct, an ideal successful root
has phase pq_W(2^B th). The selected distinct binary strings give a
nonzero signed incidence vector z_l in{-1,0,1}. Conditional on low-B
labels and selection transcript, original high blocks tau_l remain
independent uniform in[0,A), A=2^h,h=D-B. The output has
W=c+sum z_l tau_l. Therefore for every real y

 |E exp(2pi i yW)|<=D_A(y),
 D_A(y)=|(1/A)sum_(v=0)^(A-1)exp(2pi i yv)|
      =product_(j=0)^(h-1)|cos(pi2^j y)|,
 D_A(y)<=|cos(pi y)|,
 D_A(y)<=min(1,1/(2A||y||)) when||y||>0.                    (5.1)

The sine chord and geometric sum prove the last bound; the binary-factor
identity proves the first. If||y||>=1/(2A), double||y|| until first in
[1/4,1/2], taking at most h-1 doublings. One factor is at most1/sqrt2,
so D_A(y)<=1/sqrt2. ForB=0,W is a uniform h-bit supplier label directly
and all these estimates hold. No full signed-integer uniform law is claimed.
Selection and success kernels use only low bits and are phase independent;
current unused high labels and internal extraction records are marginalized,
not conditioned on. The attached beta is independent and unused by selection.

Define an actual attempt to be EDITED if ANY acquired copy during its
input construction was replaced, including a rejected replacement. An
acquisition belongs to only one attempt, so the number of edited attempts
is at most the total replacements. ModelM and the exact cap give

 Bbad<=Qcap/(131072n)=(n+1)K/(256n)<=K/128.                 (5.2)

No edit/type information is available to the controller.

Construct an analytical counterfactual for EVERY attempt, not just the
unedited ones. Reserve a complete fresh honest accepted supplier transcript
for each logical input slot: full latent label, stored D-bit label,
conditional phase state and irrelevant extraction records. Honest rejected
raw draws may be generated separately; their acceptance flag and conditional
rejected label are independent of the next reserved accepted label. The
online decision precedes the current honest draw. If the slot is filled
honestly, use its reserved honest transcript; if filled by a replacement,
leave the corresponding reserved honest input unobserved in the actual
run. The counterfactual complete attempt uses all reserved honest inputs
and an ideal Born measurement kernel. On an unedited attempt actual inputs
and circuit match this kernel exactly, so couple its classical success,
frequency,basis and outcome identically. On an edited attempt sample the
ideal kernel analytically, retaining the actual private workspace unchanged.

This is a coupling of classical transcript distributions conditional on
fixed N,s, not a physically executable second state or cloning operation.
The edit decision is fixed before the combiner/discovery/measurement coins.
Given the complete input labels, an unedited attempt has the product honest
phase input, unchanged by its data-only extraction tests. Its Born kernel
therefore remains ideal even conditional on its prior source-test records.
Edited attempts can depend on partial observed inputs, but this does not
alter the unconditional reserved-input and ideal-kernel law before the
attempt. Future ideal accepted inputs are fresh independent of prior
actual/private/counterfactual history. Replaced-call correlations affect
only actual edited kernels and the later online choices. These facts
justify the following martingales without assuming a selected good-root
subsequence is unbiased.

As in the honest-label coupling of Section3, clip an analytical adversary
after K/128 replacements and extend honestly after a halt/cap if needed.
Any promised actual run agrees before its first honest numerical-label
error or halt. The exact count in5.2 is all that is used; no ideal process
is conditioned on later budget fulfillment. Per-stage auxiliary ideal
streams may be extended with independent ideal kernels after that stage
ends, solely for the deterministic-prefix probability bounds below.

### 5.2 Prefix concentration and bounded edit transfer

Fix a measurement stage and a candidate grid determined BEFORE its
records. Conditional on correct earlier stages, let I_i be the ideal
success indicator of its ith primitive attempt, and xi_i its hypothetical
basis-weighted score term on that success, in[-1,1]. The attached basis
coin is fresh per attempt, even if the actual attempt fails. For a candidate
whose ideal conditional successful-root mean is at least a, the increment
I_i(xi_i-a) has nonnegative conditional drift; for a mean at most a it has
nonpositive drift. In either case its support, including0 on failure,
lies in the SAME interval[-1-a,1-a] of length2, for a in[-1,1].

The centered log-moment bound for an interval of length2 is t^2/2
(tilted variance at most1). With the appropriate sign, the drift only
improves the one-sided bound. At a prefix of t attempts, deviation at
least delta*K, delta=1/1024, has probability at most
exp(-delta^2 K^2/(2t)). Since t<=Tcap=128K, this is at mostexp(-K/2^28).
Union over ALL prefix lengths1,...,128K avoids any unproved stopping-time
independence. The number of candidate events in any actual stage is at
most2^(H+ceil(log2n)+10). Moreover

 log2(128K)<=42+ceil(log2n),

because n+4ceil(log2n)+120<=125n for n>=1. Their product union is bounded
by2^(H+2ceil(log2n)+52)exp(-K/2^28)<=2^-30/n for our actual K.
This is uniform over previous admissible histories and candidate sets.
No actual survival event or set of unedited attempts was conditioned on.

Let S_i be actual attempt success and xi'_i its actual record score term
when successful. On an unedited attempt these equal the ideal variables.
On any edited attempt, for fixed a in[-1,1],

 |S_i(xi'_i-a)-I_i(xi_i-a)|<=2,

since both values (including0 on failure) lie in[-1-a,1-a]. Thus at
completion of a stage's K ACTUAL successful records, the one-sided ideal
prefix concentration and at most Bbad edits give

 actual ideal-trig score >=aK-delta*K-2Bbad (lower-mean case),
 actual ideal-trig score <=aK+delta*K+2Bbad (upper-mean case).               (5.3)

This counts altered acceptance/failure decisions as well as corrupted
returned roots, and covers adversarial selective discarding. The actual
rational-table score differs by at mostK/625 for EVERY record, replaced
or not, by the uniform pointwise approximation. These bounds apply at the
random actual stage length because all prefixes were covered. If a cap
halts before K records, that is accounted separately in Section8.

## 6. Odd-part and exact-grid decoding with robust thresholds

For every n>=1 use the H,K,stride,q0 of Section4. Set M=1 case s1=0
without odd recovery. ForM>=3 choose one of the following two routes,
depending only on the known modulus.

### 6.1 Large odd part: a2<=d-H

Put h=H,B=d-H>=a2,D=d,nq=2^(H-1)q0. Every call below is the SINGLE
primitive of Section4; its returned beta is used to measure that root.

Put theta=s1/M. The stages are j=0,...,J, where J is least nonnegative with
2^((J+1)*stride+2)>2M. Put Sodd=J+1. Because stride>=1, Sodd<=n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^(j*stride) (2^(B-a2))^(-1) (mod M). Then alpha_j is a
unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run EXTRACT to obtain k, and accept iff k < 2^d (otherwise discard the copy and
  acquire again);
- on acceptance, apply X to the control.

For an all-honest counterfactual input collection, accepted labels are i.i.d. uniform on [0, 2^d), each copy is
accepted with probability 2^d/N > 1/2, and the qubit is pq_k(alpha_j s), i.e. it
has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^B W th = W 2^(B-a2) alpha_j s / M = 2^(j*stride) W s1 / M   (mod 1),            (9.1)

because 2^(B-a2) alpha_j = 2^(j*stride) (mod M) and s = s1 (mod M). So a SINGLE(d,B) root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^(j*stride) W.

Measurement. For i = 1..K:
- run SINGLE(d,B);
- use the independent beta_i attached to its successful attempt;
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
condition when j = 0). Then, in the actual promised ModelM run, with probability at least
1 - 2^-29/n, theta is within circular distance 2^-(j*stride+stride+2) of z_j.

Proof. Condition on previous correct stages and their full history. The
following means are for a SUCCESSFUL COUNTERFACTUAL ideal attempt i,
not the actual subsequence selected by adversarial decisions. Let Fprev
include all actual/private/counterfactual history before that attempt,
and Gt_i its low success/selection transcript. Conditional on ideal
success, Gt_i and held-out blocks (hence W_i), the fair attached basis gives

 E[xi_i | Fprev,I_i=1,Gt_i,W_i]=(1/2)cos(2pi f_i Delta),

where Delta=theta-zeta for its fixed candidate. Current high blocks are
marginalized when forming the successful-root mean. Every ACTUAL score
has table error at mostK/625; the transfer to its edited records is5.3.

Near point. Let zeta0 be the candidate nearest theta. In stage 0 the
candidates cover the circle. In stage j >= 1 the candidate arc contains theta
and has candidate endpoints. Either way |Delta0| <= 2^-(P_j + 1). Since
|f_i| < 2^(j*stride) 2 nq,

    |f_i Delta0| < 2^(j*stride+1) nq 2^-(P_j + 1) <= 2^-8.

Thus E[xi_i | Fprev,I_i=1]>=(1/2)cos(pi/128).

Far points. Call zeta far if |Delta| >= 2^-(j*stride+stride+2). In stage 0 we always have
|Delta| <= 1/2. In stage j >= 1, both theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j*stride+1). Hence xx=2^(j*stride)|Delta| lies in[2^(-stride-2),1/2]
for each far candidate. Counterfactual ideal inputs are fresh conditional on Fprev; ideal success
and low selection leave the held-out blocks untouched. Averaging those
blocks and the fair basis gives

 E[xi_i | Fprev,I_i=1] <=(1/2)D_(2^h)(2^(j*stride)Delta).

If h<=4, stride=1 and xx>=1/8, so the cos bound is at most cos(pi/8).
If h>=5, stride=h-4 and xx>=2^(-h+2); the block bound is at most
1/(2*2^h*2^(-h+2))=1/8<cos(pi/8). Thus the SAME old far-point score
upper bound (1/2)cos(pi/8) holds uniformly for every stage and modulus.
The larger frequency range is already included through nq=2^(h-1)q0.

Robust concentration and search. The near/far means just proved are
for the counterfactual ideal successful-root kernels. Apply5.3 at the
ACTUAL stage end, not a conditional good-record distribution. By5.2,
2Bbad/K<=2/128. With probability at least1-2^-30/n, all needed actual
scores simultaneously satisfy

 score(near)/K >=(1/2)cos(pi/128)-2/128-1/1024-1/625 >481/1000,
 score(far)/K <=(1/2)cos(pi/8)+2/128+1/1024+1/625 <481/1000.

These rationally certifiable inequalities use pi<22/7 for the first
quadratic cosine bound and pi>157/50 for the second quartic bound at
157/400, as in the clean construction. Hence a marked point exists and
ALL marks satisfy the required next-stage radius, even with adaptive edits.
The fully counted QSEARCH of6.4 fails at most2^-30/n on a nonempty set.
The combined conditional stage error is at most2^-29/n. QED.

For stage j+1 the hypothesis of Lemma 6.1 is the conclusion of stage j, since
2^-(j*stride+stride+2) = rad_(j+1). By induction, except for the summed per-stage errors, theta
lies within 2^-((J+1)*stride+2) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.


Stage-count audit. With stride=max(1,H-4), for n>=16 stride>=n/4
and the explicit J inequality gives Sodd<=5. For1<=n<=15 direct integer
substitution in H and the J inequality gives Sodd<=9 (the largest is n=10,
H=5,stride1). This finite check can also be made by15 constant iterations
in parameter preparation; it is not advice or a different input branch.
No odd factorization is needed. Every grid has at mostO(n2^H) points and
the per-stage prefix/search error bound is uniform for all n>=1.

### 6.2 Exact-grid decoder DIRECT(G,h)

This routine uses the returned-root records described above, whose ideal
successful counterparts are pq_W(theta), where theta=t/G
for unknown t in{0,...,G-1}, A=2^h and G<=2A. The ideal W satisfy5.1,
uniformly conditional on counterfactual attempt history and ideal success. For each of K
roots use its attached fair beta and measure X orY and record Z in{+1,-1},W,beta.
For every candidate j=0,...,G-1 compute the exact rational score

 score(j)=sum_i Z_i tab_(beta_i)(((W_i*j) modG)/G).

Mark a candidate when score(j)>=(481/1000)K using the same exact
integer comparison, and use QSEARCH over j=0,...,G-1. Return its verified
marked j or abort after its fixed trials. The coherent predicate streams
all K classical records with counted arithmetic, as Section6.4 specifies.
There is no quantum Fourier transform, approximate rotation or QRAM.

Proof. For a counterfactual ideal successful root and fair attached
basis, the mean term is(1/2)cos(2pi W(theta-j/G)). At the exact true
candidate it is1/2. For every wrong candidate, spacing at least1/G>=1/(2A)
and5.1 give mean at most1/(2sqrt2). By5.3 and5.2, outside a per-stage
prefix event of probability2^-30/n,

 score(true)/K>=1/2-2/128-1/1024-1/625>481/1000,
 score(wrong)/K<=17/48+2/128+1/1024+1/625<481/1000.

Here1/(2sqrt2)<=17/48 is the rational certificate289>288.
Therefore only the correct candidate is marked. QSEARCH adds failure
probability2^-30/n; total conditional stage error is at most2^-29/n.
The argument is for all actual records with bounded edits, not a claim
that their honest-looking subset is independent or unselected.

### 6.3 Small odd part: a2>d-H and M>=3

Put D=d,B=d-H<a2,h=H,A=2^H,G=N/2^B. Here2^B dividesN, and
2^d<=N<2^(d+1) gives A<=G<2A. The root supplier acquires a fresh raw
source copy, runs EXTRACT, rejects unless k<2^d, and appliesX to the
control on acceptance. On honest calls the accepted labels are fresh
uniform d-bit integers. An ideal successful counterfactual SINGLE(d,B)
has phase exp(2pi i2^B W s/N)=exp(2pi i W s/G).
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
returned mark is near (odd route) or exactly true (DIRECT), as proved by the robust prefix/edit estimates.

The work is polynomial(n)Ntrial*2^ceil(p/2), including every failed query,
verification, reset and address charge. Because Dcand<=O(n2^H), this is
O(poly(n)2^(H/2)). Candidate registers, score, comparison, multiplication
and diffusion scratch use O(n) qubits. All phase-bearing roots have already
been measured and released before QSEARCH; only their classical records
remain. No source call occurs during QSEARCH, and fresh query registers
are independent of private adversarial workspace conditional on those records.
Even arbitrary wrong-label records respect these fixed resource
limits and the maximum trial count.

## 7. Two-adic recovery in blocks

Ifa2=0 set s2=0 and skip. Otherwise, conditional on correct s1, write
s=s1+M s2 modN,0<=s2<2^a2. Begin g=0,s2low=0. At a stage put
wd=a2-g,h=min(wd,H),D=wd,B=wd-h. Let
sh=s1+M s2low modN,rem=(s2-s2low)/2^g in Z/2^wd. A supplier acquires
a fresh copy, applies Shift_sh, runs EXTRACT, appliesX to the control,
and uses kk=k mod2^wd as label. On honest calls, since2^wd dividesN, kk
is uniform in[0,2^wd), and the qubit's phase is exp(2pi i kk rem/2^wd).
An ideal successful counterfactual SINGLE(wd,wd-h) gives phase
exp(2pi i W rem/2^h), with5.1; the actual edited records are handled by5.3.
Run DIRECT(2^h,h) and let t be its answer. Update
s2low<-s2low+2^g*t and g<-g+h. Continue until g=a2, then set s2=s2low.
At most ceil(a2/H)<=2 stages are used. A correct stage appends exactly the
next h low bits. IfM=1, s1=0 is already known and this same procedure
recovers the entire secret without odd recovery. No odd-W filtering or
single-bit retry remains. Every root, even a zero frequency, is counted.
The final answer is(s1+M s2) modN.

## 8. Full algorithm, literal limits and unconditional probability

For ALL N>=2 use Sections4,6,7, including n=1. There is no noisy finite
exhaustive branch. H=ceil(n/2)<=d holds for all input moduli (at n=1,N=2,
d=1; for n>=2,d>=n-1>=ceil(n/2)). At most nine odd stages or one alternate
initial stage, plus at most two2-adic stages, give at most11<=16 stages.
Thus at mostHroot=16K successful records are ever requested. The branch
choice, K,source/attempt limits and candidate sizes are computed before use.
All counter aborts release registers and output0. Every accepted root uses
the basis attached to its attempt. Every decoder search has the fixed
trial/iteration limits of6.4 regardless of marks or bad records.

Work-cap probability in the honest-label coupling. At a primitive-attempt
abort, Tcap=128K attempts have executed while fewer than16K actual roots
have returned. At mostBbad<=K/128 attempts were edited, so the corresponding
ideal success count is less than17K<32K. Each ideal I_i has conditional
mean at least1/3, even if an earlier secret estimate was wrong, by the
phase-independent success-kernel argument in5.1. Extend I_i=1 after a
halt for this count bound if needed. The interval-length-one martingale
bound at128K gives

 Pr[sum I_i<32K]<=exp(-2*(32K/3)^2/(128K))
                =exp(-16K/9)<=2^-30/n.                  (8.1)

The check is after input building; the additional partly built attempt is
already covered by the source count and its accepted-input bound below.
No cost/success independence within a potentially edited attempt is assumed.

Source-cap probability. At most n(128K+1)<=129nK<144nK accepted supplier
qubits can be built before the attempt cap or completion. This includes
all failed attempts, B=0 attempts and one unexecuted partly built input
collection. At Qcap, at least512(n+1)K-K/128>=384nK raw acquisitions
were honest. Conditional on the prior history, every honest raw acceptance
probability is at least1/2: odd suppliers threshold a uniform latent label,
and the2-adic suppliers accept directly. This holds even after wrong past
secret estimates, since shifted/unit-transformed honest sources still have
uniform labels. If the source cap aborts, among the first384nK honest
calls at most144nK could have accepted. Their conditional mean is at
least192nK. The Bernoulli interval-length-one bound, valid with these
adaptive acceptance probabilities, gives

 Pr[source abort]<=exp(-2*(48nK)^2/(384nK))
                  =exp(-12nK)<=2^-30/n.                 (8.2)

Honest numerical-label errors have total coupled probability at most2^-14
by Section3 with this exact source cap. Only honest calls are replaced by
their latent labels in the analysis; every malformed-call instrument is
kept. Analytical clipping afterK/128 bad acquisitions and honest extension
agree with every promised actual prefix before first honest error or halt.
This avoids conditioning the ideal processes on extraction success, budget
fulfillment or cap survival.

Each completed stage has prefix-score failure at most2^-30/n and counted
query-search failure at most2^-30/n. Inducting on previous correct stages
and union over at most16 stages, then adding8.1,8.2 and label error, gives

 Pr[any failure]<=2^-14+34*2^-30/n<2^-8 for every n>=1.

Every count includes discarded and rejected copies and either abort. The
promise is the ACTUAL acquired-copy fraction, not a count only among outputs.
No successful projection, subtree or noise pattern is postselected free.

## 9. Every-branch resources and exact indices

All positive cancellations have B<=n-H; every input collection has r<=n.
The cap of128K=O(n) attempts, including B=0 and failures, and4.2 give total
merge work O(poly(n)2^((n-H+1)/2))=O(poly(n)2^(n/4)). Partly built inputs
are charged through the literal source cap and their bounded arithmetic.
Every score query is the explicit full-record scan of6.4, with polynomial
work and O(n) scratch. Candidate counts are O(n2^H), so its bounded quantum
searches across at most16 stages cost O(poly(n)2^(H/2))=O(poly(n)2^(n/4)).
All random bits, source transforms, extraction, verification, resets,
initialization, fixed rational table and circuit generation are included.
Physical addresses cost O(log n) asymptotically for the polynomial spaces,
with finite constants at n=1. The source cap is O(n^2), so total source
processing is polynomial(n). Therefore on EVERY branch

 T=O(poly(n)2^(n/4))=O(2^((13/50)n)),

using13/50-1/4=1/100>0. All n=1 costs are finite absolute constants.

The labels for at most n inputs and K=O(n) fixed measurement records have
O(n) bits each, giving O(n^2) classical bits. Fixed all-n field widths can
be8n+128+ceil(log2K), covering candidate numerators, frequencies, carry
flags, counters and rational scores without overflow; this is O(n).
Source/extraction and merge/query scratch are O(n) qubits. After root
measurement only classical records remain; threshold search uses an O(n)
ordinal and O(n) arithmetic/score/diffusion workspace. Private adversarial
workspace is external input-source memory, not an algorithm register.
All wrong-label and arbitrary-state branches respect these fixed limits.
Thus S_C=O(n^2),S_Q=O(n),Q=O(n^2) jointly with the time representative.

The exact time-envelope growth index is1 and all three polynomial resource
indices are0. Only time contributes numeric score[1]. The tolerance is a
positive inverse-bit-length fraction under the SAME ModelM context as the
constant-tolerance linear-copy construction. Its faster time and larger
copy bound are a genuine tradeoff, not automatic full-vector domination.
No sub-half-index, optimality or offline-corruption result is claimed.

## 10. Fractional guarantee and scope

The exact expression is epsilon(n)=1/(131072*n). The error-model text is
ModelM: online unflagged replacement chosen before the current honest draw,
fresh tensor-independent honest rho_s, arbitrary correlated private replaced
states, and an almost-sure budget among ACTUAL acquired originals.
Every N,s and admissible strategy has the full-secret probability and
all four every-branch bounds jointly. There are no replacement flags.
The all-honest clean-input problem is included. The proof does not assume
independent bad positions and does not condition actual good outputs on
being unedited. It makes no guarantee for a different/offline corruption
model or a larger fraction.
