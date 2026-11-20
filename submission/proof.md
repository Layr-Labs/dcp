# RQ-D64-Balanced: unequal widths and stronger online tolerance

## 0. Joint theorem and evidence

For every N>=2 and s in Z/NZ, put n=ceil(log2 N). The ONE explicit
all-n algorithm below recovers the full s under ModelM with unconditional
probability at least 1-2^-8>2/3. On EVERY execution branch its joint bounds are

 T=O(2^(n/130)*n^(2243/65)*(log2 n)^2), S_C=O(n^2) classical bits,
 S_Q=O(n) qubits, Q=O(n^65) acquired ORIGINAL source copies.

All outside constants are absolute, independent of N,s,outcomes and the
admissible strategy. Its guaranteed malformed fraction is
3333/(10000*n^(64)); the four exact growth indices are [1,0,0,0].
This is a strict asymptotic improvement of the same-model RQ-D64 resource
and tolerance guarantees. It does not lower the numerical time index.

The proof is jointly contained in three evidence files. This file gives
Sections 0-2 and 4-8; source.md gives Section 3, and resources.md gives
Sections 9-10. All section references refer to that combined document.
No theorem from a prior evaluation is assumed. The dispatcher uses an
explicit n=1 decoder, clean-forced exhaustive testing for 2<=n<128, the
original uniform tree for 128<=n<2^18, and unequal widths for n>=2^18.
The SAME fraction, success probability and resource objects apply to all.

The immediate reused source is our RQ-D64 submission
a8f6efa7-269a-4c1b-a0a4-38ddede4525c, immutable commit
8565dbba5da344ba5b700fd8d35462412878ea32, member submission/proof.md,
SHA-256 4f24d20e9d8e7dae11f87bfee919dc2826d83727d53b85e4c8d7250b1a3d9572.
Its earlier source is RQ-D32 by mpjunior92, submission
6a56e70e-a4f2-4ee2-b072-aa09b0313ddf, commit
fef98dde77c428f71c0140061f0d97e5551df37b, member submission/proof.md,
SHA-256 962f13d454cae5d8463abc3a1c8087456c4120ae56162dae53dcec827c73eb8e.
The extraction, verified-pair combiner, signed-incidence high-block law,
whole-attempt first-edit coupling, prefix concentration and cyclic score
search are reproduced with their hypotheses. New arguments balance the
64 widths, prove their exact all-input coverage and caps, enlarge the n=1
martingale experiment, and derive the rational polynomial time degree.
The supplied local improvement plan suggested width balancing and stronger
tolerance. We retain the conservative TWO logarithmic work factors rather
than assume its proposed address-cost refinement. No external plan or prior
acceptance is a mathematical premise. The ModelM text is unchanged.

The analytical couplings below retain all actual extraction, reset and
supplier/private feedback outcomes. Ideal continuations are Born-kernel
variables, never physical cloning or an unknown preparation inverse.
Actual outputs are not conditioned on being unedited: first-edit splices
and deterministic-prefix concentration account for altered acceptances,
failures and selective discarding.

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
calls were replaced, for epsilon(n)=3333/(10000*n^(64)). This is an input promise, not
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

Section 3, including the exact finite table and complete EXTRACT proof, is
in source.md. It is part of the same algorithm and joint evidence.

## 4. Fixed depth 64 and exact all-input width parameters

For the LARGE branch n>=128 put L=ceil(log2 n), tdepth=64, q0=(n+1)^64,
K=2^34*(n+70L+512), and Hroot=512K. Compute width capacities and H:

 * If 128<=n<2^18, H=ceil(n/65) and c_ell=H for ell=1,...,64.
 * If n>=2^18, m=ceil((n+4486L)/65), H=m-70L,
   and c_ell=m-2*(67-ell)*L for ell=1,...,64.

In both cases set stride=max(1,H-4), rbound=c_64+1, and exact caps

 A_ell=2^(12+3*(64-ell))*rbound^(64-ell)*K, ell=1,...,64,
 Qcap=2^204*rbound^64*K.

Thus A_64=4096K, A_ell=8rbound*A_(ell+1), and Qcap=8rbound*A_1.
The guards and error precision use THESE literal caps, not asymptotic ones.
Every level has a global actual attempt counter, including zero-width
returns. BEFORE each original acquisition, abort if Q=Qcap; otherwise
acquire and increment once. Every guard abort releases registers and
outputs 0. Thus Qactual<=Qcap on every branch. The integer formulas use
only known n, not advice or a depth depending on the instance.

Exact balanced-range inequalities. For n>=2^18 one has L<=n/8192.
At n=2^18 this holds. In a bin 2^(j-1)<n<=2^j, j>=19, its worst ratio
is j/(2^(j-1)+1), which decreases with j; 19/262145<1/8192.
Since m lies between (n+4486L)/65 and that number plus 1,

 c_1 >= (n-4094L)/65 > 0,
 H >= (n-64L)/65 >= n/66,   H <= n/65+1,
 rbound <= n/65+(4096/65)L+2 <= 3n/130+2 <= n/32.

The H lower bound uses 4224L<=n, implied by L<=n/8192.
The last inequality holds for n>=2^18. Capacities increase with ell.
Also sum_(ell=1)^64 (67-ell)=2208, and

 sum c_ell+H = 65m-4486L >= n.

In the uniform range sum c_ell+H=65H>=n,
rbound=H+1<=n/65+2<=n/32 for n>=128.
Every large-range H is positive and H<=n/65+1<=n-1<=d.

TREE64(D,B), 0<=B<D<=n, cancels B bits using the deterministic greedy rule

 b_ell=min(c_ell,max(0,B-sum_(j<ell)c_j)),
 p_ell=sum_(j<ell)b_j.

All requested B satisfy B<=n-H. Capacity coverage therefore proves
sum b_ell=B, 0<=b_ell<=c_ell and r_ell=b_ell+1<=rbound.
Also b_ell<=B<D, hence r_ell<=D<=n. Widths depend only on n,D,B, never
on a returned high label, source outcome, phase or supplier history.

NODE_0 means one accepted RAW supplier qubit/full label
from Sections6-7. For ell=1,...,64 a NODE_ell attempt does:
- Build r_ell=b_ell+1 complete fresh successful NODE_(ell-1) calls.
- Check its guard and increment its level counter; if it would exceed
  A_ell, abort. Already prepared lower inputs remain charged.
- At ROOT ell64 draw a fresh fair beta by H|0> measurement, unused by
  residue/pair selection. No lower node draws a measurement basis.
- If b_ell=0 return the one unmeasured child/full label, with beta at root.
  Otherwise run the verified-pair combiner at p=p_ell,b=b_ell.
- On FAIL discard/reset ALL current inputs (and root beta), and rebuild
  whole fresh lower calls. No successful subtree is reused after failure.
- On success return its unmeasured phase qubit and full signed label x,
  divisible numerically by2^(p_ell+b_ell).

The ROOT reports W=x/2^B with beta. The decoder immediately measures the
ROOT in that basis. All other returned qubits remain unmeasured until the
parent merge. All 64 level guards count even a zero-width return; their
counter increments have bounded constant-depth overhead.

Residue verification enforces every numerical divisibility on arbitrary
malformed states and incorrect labels. A retained root expression uses at
most product_ell r_ell<=(n+1)^64 distinct original labels with unit signed
incidences; failed lower calls do not enter it. Full words use
D+64ceil(log2(n+1))+128 bits, bounding temporary sums on every branch.
Always |W|<q0*2^(D-B). Phase semantics are asserted only for an all-honest
ideal kernel and correct previous decoder history. Edited output states
may be arbitrary, with bounded labels and one final sign outcome. No type
or edit information is supplied to the real controller.

### 4.1 Exact state preparation and verified-pair output

The inputs are phase qubits with full signed labels a_1,...,a_k divisible by
2^p, where k=b+1, with (p,b)=(p_ell,b_ell) at level ell, including the ROOT ell64. Their joint state is

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
Here k=b+1<=n, b<=c_64 and J0=2^ceil((b+1)/2). All residue arithmetic,
reflections, verification, the fixed list, streaming gate generation and
bookkeeping cost O(n^2 L) core work per iteration. The one full signed-label
update sums at most n labels of O(n) bits, also O(n^2 L), and is outside
the repeated oracle loop. Thus a complete attempt costs
O(n^2 L 2^ceil((b+1)/2)) core work and O(n) quantum scratch on every branch.
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

This is the SIZE-BIASED fiber law of the counterfactual ideal measurement. Markov gives
Pr[|C_e|>64]<3/64. If discovery is complete, the failure mass of dropping
one singleton from each odd fiber, averaged over residue outcomes, is
#odd_fibers/2^k<=2^b/2^k=1/2, for every fixed weight list.
Combining large-fiber, discovery-miss and singleton events yields

 Pr[success]>=1-3/64-1/1024-1/2=463/1024>1/3.              (4.1)

Equation(4.1) is an average over independent fresh uniform weights and search
coins. It is NOT asserted conditional on arbitrary fixed child labels.
For fixed labels, successful output correctness and the low-bit kernel
statement of4.1 still hold unconditionally. Section5 establishes the counterfactual root law and transfers it by bounded edits; it never conditions actual attempts on being unmodified.

## 5. Large-branch counterfactual attempts and robust prefix scores

### 5.1 Ideal kernels, frequencies and an actual/ideal coupling

We prove the all-honest local kernel by induction on ell=0,...,64.
At ell0 an accepted RAW label is independent uniform on[0,2^D), and
its phase is the supplier phase when earlier decoding history is correct.
For ell>=1, assume independent fresh NODE_(ell-1) calls terminate a.s.
and supply quotients uniform modulo2^(D-p_ell), before their input
generation. Their next b_ell residues are independent uniform. The
verified-pair success lemma4.3 therefore gives success at least1/3
before fresh lower generation; zero width succeeds with certainty.
Complete fresh regeneration and the finite-depth induction imply a.s.
termination of the ideal uncapped NODE_ell.

For its quotient law condition ONLY on original leaf parts below
p_ell+b_ell, the finite retry/low-selection transcript and the selected
nonzero signed incidences. Each child involves disjoint original leaves.
Composing the parent's nonzero signed incidence with these disjoint child
incidences again yields a nonzero unit signed incidence. Write each leaf
as its fixed low part plus2^(p_ell+b_ell) times an independent uniform high
block. The quotient is a fixed carry plus a signed sum with at least one
unit coefficient, so it is uniform modulo2^(D-p_ell-b_ell). Failed calls
use disjoint fresh inputs and selections depend only on low parts; mixing
over finite successful transcripts preserves this law. Storing high labels
is not filtering them. Irrelevant full instrument records are marginalized
in this all-honest kernel calculation, not deleted from supplier feedback.
This establishes the induction and the ROOT case at total canceled width B.

These ideal success and numerical-label laws are PHASE INDEPENDENT. Each
honest input control and each paired compressed output has uniform index
magnitudes even if an earlier wrong secret estimate makes its physical
phase inconsistent with the reduced numerical label.4.1's selection kernel
uses only known residues and magnitudes. Consequently every level
ideal success lower bound hold after arbitrary previous decoder outcomes,
as required for cutoff probabilities. Frequency/score semantics below
are used conditional on preceding correct stages.

When the previous decoding history is correct, an ideal successful root
has phase pq_W(2^B th). The composed selected distinct binary strings give a
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
input construction was replaced, including a rejected replacement. Each
acquisition belongs to exactly one active attempt AT EACH of64 levels, so the number of edited attempts at EACH level
is at most the total replacements. ModelM and the exact cap give

In this LARGE branch n>=128, its actual budget and arity bound give

 Bbad<=3333Qactual/(10000n^64)<Qcap/(3n^64)
     <=2^204*(n/32)^64*K/(3n^64)=K/(3*2^116)<K/128.       (5.2)

Finite-input cases are proved separately in Section8. This is a literal
hard-cap inequality, not a substitution of an asymptotic sample envelope
for the actual acquired count in the model's fractional promise.

No edit/type information is available to the controller.

For ROOT-score/root-cap analysis construct a whole all-honest
counterfactual for EVERY root attempt, including all its variable-length lower NODE
retry subroutines. Run actual and ideal local transcripts identically up
to the FIRST replaced acquisition within that root attempt. Before it,
all local source inputs were honest; current phase registers are honest
functions of the shared latent labels and controller history, and source
extraction left their control phases unchanged. The replacement decision
is made BEFORE the current honest draw. At that point continue the ideal
local controller with a fresh honest source and fresh future Born kernels,
while the actual run receives the adversarial state and keeps its private
workspace. The ideal continuation always uses honest sources, ignoring
later adversarial choices. If no edit occurs, completed actual and ideal
kernels match exactly. If edited, the ideal local kernel still has its
ordinary all-honest distribution conditional on the shared honest prefix.

This causal splice preserves its unconditional all-honest law before the
attempt: every counterfactual source channel is honest and every ideal
controller transition has its original kernel. The first-edit stopping
decision merely selects where the two probability descriptions diverge;
it does not condition which honest future outcome occurs. It may depend
on earlier lower-NODE successes, failures, labels and ALL actual source
probe/position/reset feedback. That is why a
claim only about an unmodified-child subsequence would be insufficient.
For the guard event at EACH level ell, use a SEPARATE whole-NODE_ell
first-edit coupling by this same construction. A bad acquisition belongs
to one active local attempt at each level. Thus at most Bbad completed
attempts are edited at each of64 levels. The stopping decision can depend
on all previously observed lower successes/failures, labels, raw rejects
and actual extraction feedback, but not on the next fresh honest draw.
Each auxiliary splice retains the ACTUAL adversary, all private outcomes
and malformed-source instruments. Its honest continuation only defines
that local ideal kernel's ordinary distribution before its construction.
No joint independence among different level couplings is required.

These are analytical CLASSICAL Born-transcript couplings conditional on
fixed N,s and latent histories. No unknown state is physically cloned,
prepared twice or supplied to the algorithm. On a completed unedited
local attempt its conditional input/circuit kernel is exactly the ideal
one, so the classical outcomes can be coupled identically. On an edited
attempt complete its ideal continuation analytically while retaining
the actual quantum adversary and its outcomes. Fresh honest future
channels are tensor-independent of all previous real and auxiliary
histories. The current lower NODE circuit acts on fresh inputs, not on retained
parent siblings, until it returns. Parent siblings may be correlated with
arbitrary earlier malformed systems; local fresh honest tensor channels and
no-signalling preserve the required local kernel. No parent sibling is
queried by a lower retry.

Global guards are ignored ONLY in defining these analytic ideal local
kernels, which terminate a.s. Actual matching/edit transfer is applied
only to FULLY EXECUTED attempt prefixes: a source or lower-level cap interrupting
input construction is already a separate failure event. The additional
unexecuted collection at a guard is excluded from the status comparison
and included in source accounting. One can extend auxiliary ideal kernels
after an actual halt or stage end to define every deterministic prefix,
without conditioning on budget survival. No unedited aborted attempt is
falsely counted as matching a completed ideal output.

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

The centered log-moment bound for interval length2 is t^2/2, since
tilted variance is at most1. The appropriate drift sign only improves the
one-sided bound. At a prefix of length u<=Rcap=A_64=4096K,
a deviation delta*K, delta=1/1024, has probability at most
 exp(-delta^2*K^2/(2u))<=exp(-K/2^33).
Union over ALL deterministic prefixes avoids stopping-time or survival
independence. Write L=ceil(log2 n). A stage needs at most
2^(H+64L+80) candidate/near/far events: q0=(n+1)^64<=2^64*n^64,
and every odd grid has at most 2^(ceil(log2 nq)+8) points;
DIRECT has at most 2^(H+1). Also n+70L+512<=1024n for n>=128,
so K<=2^44*n and log2(4096K)<=56+L. The complete union is at most

 2^(H+65L+160)*exp(-K/2^33)<=2^-40/n.

Indeed K/2^33=2(n+70L+512), e^-x<=2^-x, and the exponent difference
2n-H+75L+864 is at least 40+L since H<=n. This bound is uniform
over earlier admissible histories and candidate sets. No actual survival
or set of unedited attempts is conditioned upon.

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

In the LARGE branch use the H,K,stride,q0 of Section4. Set M=1 case s1=0
without odd recovery. ForM>=3 choose one of the following two routes,
depending only on the known modulus.

### 6.1 Large odd part: a2<=d-H

Put h=H,B=d-H>=a2,D=d,nq=2^(H-1)q0. Every call below is the TREE64
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

because 2^(B-a2) alpha_j = 2^(j*stride) (mod M) and s = s1 (mod M). So a TREE64(d,B) root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^(j*stride) W.

Measurement. For i = 1..K:
- run TREE64(d,B);
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
1 - 2^-39/n, theta is within circular distance 2^-(j*stride+stride+2) of z_j.

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
2Bbad/K<=2/128. With probability at least1-2^-40/n, all needed actual
scores simultaneously satisfy

 score(near)/K >=(1/2)cos(pi/128)-2/128-1/1024-1/625 >481/1000,
 score(far)/K <=(1/2)cos(pi/8)+2/128+1/1024+1/625 <481/1000.

These rationally certifiable inequalities use pi<22/7 for the first
quadratic cosine bound and pi>157/50 for the second quartic bound at
157/400, as in the clean construction. Hence a marked point exists and
ALL marks satisfy the required next-stage radius, even with adaptive edits.
The fully counted QSEARCH of6.4 fails at most2^-40/n on a nonempty set.
The combined conditional stage error is at most2^-39/n. QED.

For stage j+1 the hypothesis of Lemma 6.1 is the conclusion of stage j, since
2^-(j*stride+stride+2) = rad_(j+1). By induction, except for the summed per-stage errors, theta
lies within 2^-((J+1)*stride+2) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.


Stage-count bound. Section 8 proves at most 391 stages in the uniform
range and 199 in the balanced range, both below the literal ceiling 512.
Every grid has at mostO(n^64 2^H) points because q0=(n+1)^64. The prefix
and search bounds are uniform for all n>=1; no odd factorization is needed.

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
prefix event of probability2^-40/n,

 score(true)/K>=1/2-2/128-1/1024-1/625>481/1000,
 score(wrong)/K<=17/48+2/128+1/1024+1/625<481/1000.

Here1/(2sqrt2)<=17/48 is the rational certificate289>288.
Therefore only the correct candidate is marked. QSEARCH adds failure
probability2^-40/n; total conditional stage error is at most2^-39/n.
The argument is for all actual records with bounded edits, not a claim
that their honest-looking subset is independent or unselected.

### 6.3 Small odd part: a2>d-H and M>=3

Put D=d,B=d-H<a2,h=H,A=2^H,G=N/2^B. Here2^B dividesN, and
2^d<=N<2^(d+1) gives A<=G<2A. The root supplier acquires a fresh raw
source copy, runs EXTRACT, rejects unless k<2^d, and appliesX to the
control on acceptance. On honest calls the accepted labels are fresh
uniform d-bit integers. An ideal successful counterfactual TREE64(d,B)
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
<=2^(-Ntrial/8)<=2^-40/n. On a good concentration transcript every
returned mark is near (odd route) or exactly true (DIRECT), as proved by the robust prefix/edit estimates.

The work is polynomial(n)Ntrial*2^ceil(p/2), including every failed query,
verification, reset and address charge. Because Dcand<=O(n^64 2^H), this is
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
An ideal successful counterfactual TREE64(wd,wd-h) gives phase
exp(2pi i W rem/2^h), with5.1; the actual edited records are handled by5.3.
Run DIRECT(2^h,h) and let t be its answer. Update
s2low<-s2low+2^g*t and g<-g+h. Continue until g=a2, then set s2=s2low.
At most ceil(a2/H)<=66 stages are used (<=65 in the uniform range). A correct stage appends exactly the
next h low bits. IfM=1, s1=0 is already known and this same procedure
recovers the entire secret without odd recovery. No odd-W filtering or
single-bit retry remains. Every root, even a zero frequency, is counted.
The final answer is(s1+M s2) modN.

## 8. Full algorithm, 65 literal caps and probability

The all-n dispatcher is explicit. If n=1 then N=2. Acquire exactly
Q1=2^31 original copies. On each apply a Hadamard to its DATA register
and measure that bit k in Z, then measure its control in X. Record a
score V=0 when k=0, and V equal to the observed X sign when k=1.
Reset/release each copy after these measurements. Sum the signed scores
and output0 if their sum is positive,1 if negative, and0 on a tie.
This uses exact Hadamards and fixed classical counters; it does not know s.

For analysis multiply every recorded score by the true sign (-1)^s,
calling it X_i. On a fresh honest rho_s, its independent fair Fourier
label is0 or1. The control's sign at k=1 is exactly(-1)^s, so X_i is
Bernoulli(1/2). On any replacement X_i belongs to{-1,0,1}, including
private-state correlations. Let b_i be the analytical replacement bit,
chosen BEFORE the current fresh draw as ModelM requires, and let
M_j=sum_(i<=j,b_i=0)(X_i-1/2). Given the full past and the chosen current
type, its increment has mean0 and support in[-1/2,1/2]: at a replacement
it is exactly0, and otherwise the fresh honest label is fair. Hence the
interval-length-one exponential martingale inequality gives
Pr[M_Q1<=-Q1/20000]<=exp(-2*(Q1/20000)^2/Q1)
                     =exp(-Q1/(2*10^8))<2^-8.
Indeed Q1/(2*10^8)>8 and e>2. The fractional promise gives
B=sum b_i<=floor(3333Q1/10000) almost surely. Pointwise,

 sum_i X_i >=(Q1-B)/2+M_Q1-B
             =Q1/2-3B/2+M_Q1>=Q1/20000+M_Q1,

because 1/2-(3/2)*(3333/10000)=1/20000 exactly.

An erroneous output (including an unfavorable tie) requires sum X_i<=0,
so failure is below2^-8. This is uniform over both secrets and all online
admissible strategies; no bad positions or honest subset are conditioned
on. The actual protocol acquires exactly Q1 copies on every n=1 branch.
Its constant costs fit the declared all-n bounds by absolute constants.
Unlike the parent finite dispatcher, this branch proves positive malformed
sample tolerance directly.

If 2<=n<128, perform the following finite exhaustive protocol. For each
t=0,...,N-1, acquire at most n+8 fresh originals, applying the known
Shift_t of Section2 and measuring the control in X. Reject t at the first
minus; output the first candidate passing all n+8 tests, or0 if none does.
Every branch has Qactual<=N(n+8)<=2^n(n+8)<n^64.
For the strict inequality, n+8<n^4 for every n>=2. If2<=n<=60,
2^n<=n^n<=n^60; if61<=n<=127,2^n<=2^127<61^60<=n^60.
Multiplication proves the bound without advice.
Consequently epsilon(n)*Qactual<1, and any admissible strategy again
makes NO replacements almost surely. The deterministic copy ceiling
prevents a malicious state from manufacturing later budget through extra
queries; no invalid strategy is conditioned onto a favorable event.
For a clean copy Shift_t changes the secret to s-t. If t=s the control
is|+> and always passes. If t!=s its X mean is zero: a nonzero cyclic
translation has trace0, or directly each off-diagonal overlap between
x and x+s-t vanishes. Thus a false test passes with probability1/2,
uniformly conditional on all previous outcomes, using a fresh ideal copy.
A false candidate passes its n+8 tests with probability2^-(n+8).
Union over at most N-1 false candidates gives wrong output probability
<(N/2^n)*2^-8<=2^-8. The true candidate always passes if reached.
This branch uses the explicitly defined controlled translation, never a
Fourier/hidden-shift oracle, and is a PROVED zero-malformed consequence
of the fractional promise for these finite lengths.

For n>=128 run Sections 4,6,7 with their literal caps and chosen H.
In the uniform range H=ceil(n/65). If H<=4 then n<=260, giving at most
260 odd stages. Otherwise n<=65H and stride=H-4, so at most
n/(H-4)+1<=326 odd stages. At most ceil(n/H)<=65 dyadic blocks
give a total of at most 391. In the balanced range H>=n/66>=8,
stride=H-4>=H/2. Thus at most n/stride+1<=133 odd stages and
ceil(n/H)<=66 dyadic blocks give at most 199 stages. Both ranges are
covered by the unchanged ceiling of 512 stages and Hroot=512K roots.
The alternative DIRECT odd route is one stage.
Every query search has its fixed trial/iteration caps. Any of the64 NODE
guards or the source guard aborts by releasing registers and outputting0.
The actual fractional budget gives at mostK/128 edits at each level.

The following probability estimates use the auxiliary exact-honest-label
process with at mostK/128 clipped edits. They control actual cap events
before the FIRST honest numerical-label error; that separate error is
added afterwards. At the ROOT cap A_64=4096K, before all requested512K records are obtained,
actual successes are below512K. Its auxiliary ideal count is below513K,
hence below A_64/4=1024K. For any lower level ell, the maximum successful
outputs requested is rbound(A_(ell+1)+1), including an unfinished extra parent
collection. At its attempt cap A_ell=8rbound*A_(ell+1), the auxiliary ideal
count is at most rbound(A_(ell+1)+1)+Bbad<2rbound*A_(ell+1)=A_ell/4.
The strict inequality follows from A_(ell+1)>=4096K, K>=1, rbound>=1.
These count comparisons apply only to fully executed attempts; a guard
interrupting fresh construction is separately included in its cap event.

For EACH level the auxiliary conditional success mean is at least1/3,
even after wrong earlier guesses. Use ideal kernels throughout the actual GLOBAL level stream; extend
successes to1 only after the entire run halts or terminates. At A_ell attempts, fewer than
A_ell/4 successes deviate below the mean by at least A_ell/12. The
interval-length-one martingale inequality therefore gives

 Pr[level-ell cap]<=exp(-2*(A_ell/12)^2/A_ell)
                  =exp(-A_ell/72)<=2^-40/n.              (C1)

For the last step A_ell>=4096K>=4096*2^34*n, and
A_ell/72>=64n>=40+ceil(log2n); use e^-x<=2^-x and n>=1.
All64 level cap events have this uniform bound; no independence is claimed.

For the source guard, accepted RAW demand is at most rbound(A_1+1).
Since Qcap=8rbound*A_1 and Qcap>16rbound, this is <3Qcap/16. At Qcap originals,
at least Qcap/2 calls were honest because Bbad<=K/128. Their conditional
acceptance probability is at least1/2 on the odd threshold route or1 on
the dyadic route, even after wrong earlier estimates. Among the first
Qcap/2 honest calls the mean accepted count is at least Qcap/4. Source
abort allows fewer than3Qcap/16 total accepted inputs, hence also fewer
than that many honest acceptances, a gap at least Qcap/16. Thus

 Pr[source cap]<=exp(-2*(Qcap/16)^2/(Qcap/2))
                =exp(-Qcap/64)<=2^-40/n.                (C2)

The last estimate follows from Qcap>=8rbound*A_1>=16384K. Analytical honest
call streams may be extended freshly after actual halt to define this
fixed prefix. Their unconditional drift bound uses the type decision BEFORE
the fresh draw, never iid labels conditioned on a final honest set.
Every partially built extra input collection is included in rbound(A_1+1).

These65 estimates bound actual pre-honest-error cap events through the
separate auxiliary kernels; honest numerical errors are added below.
No edited positions, random local costs or survival events are assumed
independent. Completed unedited attempts match ideal completions; guard-
interrupted unexecuted kernels are not falsely included as matches.
The source guard BEFORE acquisition ensures the exact literal Qcap.

Up to Qcap honest EXTRACT calls have aggregate error2^-14. The auxiliary
honest-label forcing retains all actual probe/position/reset outcomes,
private workspaces and supplier feedback. Clipping afterK/128 edits agrees
with all promised real prefixes before first honest error or halt. No
honest law is conditioned on label success or future fractional compliance.
At most512 stages each have prefix-score error2^-40/n and query-search
error2^-40/n. Induct on preceding correct stages and union all losses:

 Pr[any failure]<=2^-14+(1024+65)*2^-40/n
                 =2^-14+1089*2^-40/n<2^-8.               (C3)

This proves the large-branch failure bound for n>=128. The two finite
branches proved above have failure at most2^-8 as well. Thus the SAME
complete protocol has success at least1-2^-8 for EVERY n>=1, including
the clean no-replacement case.
All originals, source rejects, failed nodes and partially constructed
collections count. No subtree, projection or edited status is postselected.

Sections 9-10 (joint branchwise resources, growth indices and tolerance)
are in resources.md and are part of this complete proof.
