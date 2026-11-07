# RQ-LIN: counted quantum score search with linear original copies

## 0. Joint theorem and actual provenance

For every N>=2 and s in Z/NZ let n=ceil(log2 N). The ONE algorithm below
recovers the complete s under the explicit online replacement model below with
unconditional probability at least1-2^-8>2/3. On EVERY branch, including
rejected copies, failed search trials, numerical-label errors and the
literal acquisition abort, its joint representatives are

 T=O(n^6 2^((1/2)n)), S_C=O(n^2) classical bits,
 S_Q=O(n) qubits, Q=O(n) total acquired ORIGINAL source copies.

All outer constants are absolute, independent of N,s and outcomes. The
representatives apply for n>=2; the SAME specified algorithm has finite
cost at n=1, absorbed by absolute constants. The exact growth indices
are[1,0,0,0]. The guaranteed unflagged malformed fraction is1/32 in ModelM below,
including the required all-honest clean-input case.
This is an exponential-time, linear-copy tradeoff, not a smaller numerical
time index, source lower bound or optimality claim.

The immediate direct construction source is this solver's local clean
Q-LIN snapshot00574345b3c4d1c197f948ceec36573eb4dc6b90f8c62ebf1f7517a191c1c141,
whose genuine review was running when this draft was made. The changes
are the smaller exact source cap, robust score threshold, enlarged K and
full adaptive adversarial analysis. No prior verdict is a premise.

The direct source-interface and numerical extraction materials are the
complete proofs read from PSG4-LIMIT ae6bd13e-97a1-4009-8225-4b1b6bc3dea2,
PSG5-SHARP db0cc225-d7f0-475c-9b9d-21b3c15bac17 and original PSG5
9f11a7a4-8d17-48f2-8658-892d3e378efa, archive
2e46e18cd6d60587394365bd89019196b002e15f. Their historical upstream
source/translation credits are acknowledged; all needed arguments are
included. Immediate development sources are this solver's local PSG-SB
snapshot b88eccf4c6956f1984714a7df44f1ed506c5940135c749c1af120206838a256e
(real atomic local review valid) for exact-grid score separation, and local
PSG-QSB snapshot8725a059ad051d2cad2a4b059f7e23bc6f9cb9d8cca6ca4c560a4bca3f7d44e4
(real review pending at drafting) for counted coherent threshold search.
They had no public IDs when this draft was made. No verdict is a premise.

This is the ZERO-MERGE endpoint: take measured phase qubits directly from
source extraction, and perform one global score-threshold search over all
N secrets. No collimation tree, parity recovery or modulus split executes.
The Remaud,Schrottenloher,Tillich paper2206.14408 was read for comparison;
query/time tradeoffs and linear-query algorithms already exist. No
algorithmic or proof subroutine from that paper is invoked, and no
first-ever linear-query improvement is claimed.

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
calls were replaced, for epsilon(n)=1/32. This is an input promise, not
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


EXTRACT uses Qcap fixed in Section6. Put J_e=n+4,

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
cap of Section6 gives h=O(log n), so this is O(n^2 L) per complete call.
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

## 4. Accepted raw phase samples and exact-grid separation

Let d=floor(log2N), A=2^d and G=N. Then A<=G<2A. For every input n>=1
compute the integer

 K=2^25*(n+ceil(log2 n)+40), Qcap=67K/32.

ceil(log2n)=bit_length(n-1), including value0 at n=1. Initialize the
acquisition counter. Before any original copy that would exceed Qcap,
abort, release registers and output0. A supplier acquires a fresh raw
copy, runs EXTRACT with this EXACT Qcap, rejects and discards unless
k<2^d, and on acceptance appliesX to the control and releases the data.
Repeat until K accepted qubits have been obtained, measuring each immediately
in an independently fair X/Y basis beta_i and recording its outcome
Z_i in{+1,-1},label W_i=k and beta_i. Release its quantum registers before
the next supplier. Count every rejected and discarded original copy.

On an HONEST accepted copy in the exact-label process, W_i is uniform
in[0,A), the phase state is pq_(W_i)(s/N), and acceptance probability is
A/N>1/2 (or1 at N=A). The decision that this copy is honest preceded its
fresh draw. The controller filters only k<A and chooses an independent
fair basis after acceptance. For replaced accepted copies no phase law is
asserted: their stored W,beta,Z still lie in the fixed legal ranges.
They contribute one bounded score term each, and no flag identifies them.

The actual fraction promise and exact cap imply that the TOTAL number of
replaced acquisitions is at most Qcap/32=67K/1024. Thus the number b of
replaced ACCEPTED records is also at most67K/1024. K is divisible by1024.
This uses the exact literal protocol cap, not an asymptotic sample
representative. Section6 proves the fractional guarantee jointly from
this actual-input promise and the score drift analysis below.

For probability analysis, clip an ideal adversary after67K/1024 replacements
and extend with fresh honest calls after the cap if needed to complete K
records. Before any honest numerical extraction error the promised actual
process cannot exceed this count, so it agrees with the clipped process
until a cutoff or completion. No replacement flag is supplied to the real
controller. The analytical extension avoids conditioning score laws on
budget survival; its uncapped honest draws remain fresh. Replaced-call
instruments and their private entanglement are unchanged before clipping.

For every real y the uniform label's characteristic modulus is

 D_A(y)=|(1/A)sum_(w=0)^(A-1)exp(2pi i yw)|
       =product_(j=0)^(d-1)|cos(pi2^j y)|.

If||y||>=1/(2A), then D_A(y)<=1/sqrt2. Indeed starting at
x=||y|| in[2^(-d-1),1/2], double until first reaching[1/4,1/2].
This takes j<=d-1 steps, without a wrap before that threshold. The jth
cosine factor is at mostcos(pi/4), and the others at most1.
This works for every N, including powers of two and odd N.

For j=0,...,N-1 define the explicit score

 score(j)=sum_(i=1)^K Z_i tab_(beta_i)(((W_i*j) modN)/N).

The true integer secret is an EXACT candidate. Put theta=s/N and
xi_i(j)=Z_i cs_(beta_i)(W_i*j/N), always in[-1,1], including replaced
records. For an honest accepted record, conditioning on the past and its
honest type, and marginalizing the current internal extraction outcomes,
W is uniform[0,A) and beta is fair. Thus its conditional mean mu_j is
constant: mu_s=1/2 and mu_j<=1/(2sqrt2) for j!=s, by the characteristic
bound above. The choice of its type was made before that honest draw.

Here is the adaptive-position justification in detail. Between accepted
records there may be arbitrary rejected honest/replaced calls, depending
on the earlier transcript. At the next honest accepted call, conditioning
on its true acceptance flag k<A leaves a uniform k within[0,A), regardless
of that prior history. Mixing over which future call is the next accepted
honest call preserves this conditional law. No current high label or
current internal extraction record is included in this conditioning.
Those records do not select the copy beyond its stated acceptance flag;
the later adversarial choices affect only later calls. A mathematical
filtration may reveal current type/acceptance before the conditional
accepted label,basis and outcome. Equivalently average over that type:
with B_i the hidden replacement indicator,

 X_i(j)=(1-B_i)(xi_i(j)-mu_j)

has conditional mean0 given previous accepted-record history. Its support,
including the zero increment on a replacement, lies in an interval of
length2. This is a martingale difference even for adaptive correlated
replacement positions and states; no fixed independent good-position set
is assumed. The hidden B_i is for proof only, not available to the algorithm.

The centered log-moment bound for interval length2 is at most t^2/2:
its tilted variance is at most1, and its value and first derivative vanish
at zero. Iterating the conditional bound and optimizing t gives
Pr(sum X_i>=a) and Pr(sum X_i<=-a) at most exp(-a^2/(2K)). Taking
a=K/4096 gives exp(-K/2^25). Union over the true lower tail and all wrong
upper tails (at mostN+1<=2^(n+1)) is at most2^-20/n for our actual K.

For the b<=67K/1024 replaced accepted records, every xi lies in[-1,1].
The trigonometric approximation changes ANY computed score by at mostK/625,
even for replaced records, since its pointwise bound is uniform. Therefore
outside those martingale tails,

 score(s)/K >=1/2-(3/2)(b/K)-1/4096-1/625
             >=1/2-201/2048-1/4096-1/625 >2/5,
 score(j)/K <=c+(1-c)(b/K)+1/4096+1/625
             <=17/48+(31/48)*(67/1024)+1/4096+1/625 <2/5 (j!=s).

Here c=1/(2sqrt2)<=17/48, since17^2=289>288. The last inequalities are
exact rational comparisons; the bounds are respectively0.400011328125 and
less than0.398268. Thus the fixed threshold marks EXACTLY the secret
uniformly for every permitted adversary, not just clean records.
Scores have exact denominator2^20; mark by comparing signed integer units
to ceil(2*K*2^20/5). No uncharged likelihood normalization is assumed.

## 5. Fixed-loop counted quantum threshold search

Use an n-qubit ordinal register with Tpad=2^n basis states. Valid
ordinals j<N are candidate secrets; padded ordinals are unmarked.
Prepare the uniform query state H^n|0>. The source samples and phase
qubits are already measured and all source workspace reset, so only their
CLASSICAL records remain. No further source call occurs during search.
Conditional on those records, fresh query registers are independent of
any private adversarial workspace; classical correlation with that workspace
does not alter the fixed predicate or its trial-success calculation.

A score phase predicate is explicitly implemented as follows. In a classical
gate-generation loop over i=1,...,K, stream the known n-bit W_i and known
beta_i,Z_i. Reversibly compute (W_i*j) modN using O(n)-bit modular
arithmetic, for example repeated controlled addition and reversal, with
O(poly(n)) gates and O(n) scratch. Compute floor4096residue/N into12 bits
with12 comparisons/conditional subtractions of known multiples ofN.
Scan the fixed4096-entry Cos orSin table with equality flags, obtain
its signed20-bit value, apply the known sign Z_i, add it to a signed
O(log K+20)-bit score accumulator, and uncompute per-record scratch.
After the Kth contribution compare to ceil(2*K*2^20/5), combine
with j<N and phase flip, then reverse the score computation completely.
All records, constants, wire addresses, table scans, multiplication,
comparisons and gate generation are charged on EACH query. This is not
quantum-addressed memory: every classical record is scanned in fixed order.
No QRAM or uncharged score oracle is used. The circuit is exact Clifford+T
with O(n) quantum scratch and polynomial(n) charged work per predicate.

Perform at most Nt=256*(ceil(log2n)+40) independent trials. A fair bit
chooses direct uniform measurement or random-length Grover. In the latter
choose j0 uniform in[0,J), J=2^ceil(n/2), perform j0 iterations of the
counted predicate and exact reflection about H^n|0>, and measure the
candidate. The direct branch measures its uniform ordinal immediately.
Verify validity and the score classically, accepting the first verified
mark. Reset/discard query registers between failures. If no mark is found
within Nt trials, output0. The reflection is H gates, a reversible all-zero
test and Z, with exact Toffoli decomposition. All fair bits, measurements,
verification, reset and generation are charged. The loop limits are fixed
even if wrong-label records give no marked candidate.

When at least one mark exists, let f be its fraction in Tpad. If f<=1/2,
J>=sqrt(Tpad), f>=1/Tpad, and for theta0=arcsin(sqrt f),
Jsin(2theta0)>=1. The mean random-length Grover success is

 (1/J)sum_(j0=0)^(J-1)sin^2((2j0+1)theta0)
 =1/2-sin(4Jtheta0)/(4Jsin(2theta0))>=1/4.

If f>=1/2 the direct half alone succeeds with probability at least1/4,
including f=1 where the formula's denominator vanishes. Thus the mixed
trial always succeeds with probability at least1/8. For fixed records,
independent fresh queries miss in every trial with probability at most
(7/8)^Nt<=exp(-Nt/8)<=2^(-Nt/8)<=2^-30/n. On Section4's concentration
event the only verified mark is s. Every returned mark is checked using
the same explicit rational predicate; no maximum-finding oracle or
assumed successful postselection appears.

## 6. Complete success and EVERY-BRANCH resources

The algorithm is exactly Sections4-5, for ALL N>=2, including n=1,
under ModelM. It has the literal acquisition cap Qcap=67K/32 and no
merge or flat attempt counter. If the exact-label process reaches this
cap without K accepted records, it has seen at least
(67/32-67/1024)K=2077K/1024 honest acquisitions. In particular, the
first Mgood=259K/128=2072K/1024 honest calls have occurred, yet fewer
than K could have accepted. These counts are integers since K is
divisible by1024. The honest sequence is fresh independent rho_s,
despite online adaptive interleaving, with acceptance probability A/N>=1/2.
Its expected accepted count among Mgood calls is at least259K/256;
falling below K requires deviation at least3K/256. The Bernoulli
interval-length-one log-moment bound gives probability at most

 exp(-2*(3K/256)^2/(259K/128))=exp(-9K/66304)
 <=exp(-K/8192)<=2^-30/n.

The middle inequality follows from9*8192>66304. One may pre-sample
an infinite honest sequence: an online replacement decision cannot inspect
or skip its next fresh draw. Rejected honest labels and private bad-copy
correlations do not change that law. The clipped/extended process of
Section4 supplies this bound without conditioning on actual cap survival.

At mostQcap HONEST EXTRACT calls can err; their conditional uniform
per-call bound gives aggregate error2^-14. Couple honest labels to their
exact latent values until the first such error. On replaced inputs keep
the actual bounded extraction/measurement instrument unchanged. Clipping
after67K/1024 replacements agrees with any promised actual execution before
an honest-label error or halt, since Q<=67K/32 and its actual fraction is<=1/32.
Therefore the actual algorithm has total failure at most

 2^-14+2^-30/n+2^-20/n+2^-30/n<2^-8.

The terms are honest extraction, source-cap, robust score and bounded
quantum search, respectively. Their union needs no independence assumption.
This proof is uniform over all admissible online strategies. It uses the
actual fractional promise at every replaced/discarded acquisition, rather
than a statement merely about accepted records or per-copy independent
noise probability. Clean input is included as the zero-replacement case.
Qcap=O(n), so the total original-copy bound holds on every branch.

Source transforms, extraction and construction of K records cost polynomial(n)
work, including every rejected copy. A threshold query has polynomial(n)
work by its counted arithmetic/scan circuit. Each trial has fewer than
2^ceil(n/2) iterations and there are O(log n) trials asymptotically, with
fixed finite counts at n=1. The physical address charge is O(log n) for
polynomial workspaces and is included. All initialization, preparation,
verification, uncomputation, measurements, releases and generation are counted.
Therefore on EVERY branch

 T=O(n^3 L^3 2^(n/2))=O(n^6 2^((1/2)n)).

For completeness, each streamed record uses O(n^2 L) core bookkeeping
and reversible arithmetic; K=O(n) records give O(n^3 L) core per query.
The separate address charge gives O(n^3 L^2) work per query and O(L)
trials give O(n^3 L^3 2^(n/2)). Classical verification and source work
are smaller. For n>=2,L<=n, giving the declared n^6 prefactor.
The finitely many small n, including1, enlarge only absolute constants.
No unspecified exponential coefficient is inferred or hidden.

The K=O(n) measured records have O(n) bits each, so classical space is
O(n^2), including all label counters, global caps and the fixed rational
table. Source/data and extraction workspaces use O(n) qubits; those are
released before the n-bit search register plus O(n) arithmetic/diffusion
scratch is used. Thus S_Q=O(n). The score accumulator has only
O(log n+1) bits. Even arbitrary wrong numerical-label records respect
all fixed widths, the acquisition cap and query loop bounds. There is
no exponentially stored circuit or hidden classical advice.

The exact time-envelope growth index is1, and the three polynomial
resource envelopes have index0. Only time contributes numeric score[1].
These are full representatives of this ONE algorithm, not optimality
claims or lower bounds. It trades slower time than the quadratic-copy
block algorithm for a smaller, linear original-copy envelope.

## 7. Guaranteed malformed fraction and quantifiers

The exact guaranteed expression is epsilon(n)=1/32. ModelM of0.1 specifies
unflagged ONLINE replacements, fresh independent honest states, the timing
of the replacement decision, arbitrary correlated private replacement
states, and the almost-sure budget among ACTUAL acquired originals.
For every N>=2,s and every such adversary, the ONE algorithm has all four
joint every-branch resource envelopes and unconditional success>=1-2^-8.
No replacement positions, labels or flags are given to the controller.
The proof allows a growing linear number of replaced inputs; it is not a
zero-malformed-copy promise in disguise. All-honest copies are a special
case, so the challenge's clean problem is also solved. No claim is made
for retroactive/offline selection that biases honest labels, for source
gate faults, or for any larger fraction. Different error-model contexts
must be compared with their actual assumptions, not silently identified.
