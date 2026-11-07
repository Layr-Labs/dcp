# RQ-SPLIT: late sample splitting gives one-third tolerance with linear qubits

## 0. One joint theorem, parameters and provenance

For every N>=2 and s in Z/NZ, put n=ceil(log2 N). The ONE finite algorithm
below recovers the entire secret with unconditional probability at least
11/16>2/3 at the EXACT fraction epsilon=1/3 in ModelM. Every branch has

 T=O(2^(n/2) n^2 (log2 n)^2), S_C=O(n^2) classical bits,
 S_Q=O(n) qubits, Q=O(n) acquired ORIGINAL coset copies.

These are representatives for n>=2; the SAME protocol at n=1 has finite
cost absorbed in absolute constants. Their exact growth indices are
[1,0,0,0]. No practical constant factors or optimality are claimed.

The new construction partitions the source bank AFTER all deliveries.
A small uniform subset becomes actually measured classical shadow records;
the much larger complementary row bank is untouched during coarse search.
Its sampling fluctuations are controlled quantitatively, rather than
assuming each subset satisfies an exact one-third cap. All coarse pivot
histories/caches are therefore measured and stored CLASSICALLY. This
removes the quadratic QUANTUM histories of the cached one-third procedure,
while retaining a statistically adequate bank for the final antipodal test.
The deliberately large fixed copy multiplier is an actual counted constant.

Direct material sources read in full/relevant detail are:
- ROB-G2 55a6ce76-34af-468f-b735-a1197f3d3459, published commit
  77b383ed0ea3c8b9765c332de88add12c3d2b52d, proof SHA-256
  64a87926620815ae4030997207eedff9f4507b5fb825c3c07d88c5794f566228:
  the identical error-model string, packed binary phase words, controlled
  ripple arithmetic and explicit addressing/generation accounting.
- Cached one-third 493303b5-06f6-4ee0-9596-d8cae89c8bb4, commit
  d1d5a491f9b908ada5de2c7937fdf4732aede43d, proof SHA-256
  e659fd631482bac4d1977d0463d9951df6eaf8ec325e811c45e7646f71687074:
  cubic pair witnesses, canonical classes, fresh/exact-grid phase caches,
  contextual threshold counting, bounded mixed-Grover elimination, work
  gradient and the antipodal trit rule. Its coherent answer-copy/undo and
  same-bank disturbance argument are NOT used here. Its O(n^2) quantum
  history is replaced by classical measured history on separate shadows.
- This solver's published RQ-LIN e550a028-49f3-4b72-afeb-906d65ce40cf and
  Q-LIN8f43a18d-32dd-41c8-8898-7a8fa0e86cfc supply the reproduced source
  extraction/collective-round and counted source/circuit framework.
  Direct underlying materials are PSG-QSB70436d5e-40d4-489c-95e3-4cbc92c79cf0,
  PSG-SB1dd839ab-0ee6-4516-aa8d-89c390361d2a,
  PSG4-LIMITae6bd13e-97a1-4009-8225-4b1b6bc3dea2,
  PSG5-SHARPdb0cc225-d7f0-475c-9b9d-21b3c15bac17, and original PSG5
  9f11a7a4-8d17-48f2-8658-892d3e378efa, archive
  2e46e18cd6d60587394365bd89019196b002e15f. Historical source credits
  carry through, but every needed argument is reproduced.

Own B16/R15/FULL/CLOSE were unpublished local development, acknowledged
in the public note; they are not earlier public submission IDs. No prior
review is a mathematical premise. There is no first-ever exact-one-third,
linear-query or Grover-score claim. This proof establishes a different
joint storage/configuration guarantee through late bank splitting.

## 0.1 ModelM (exact comparator context)

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

The chosen fraction in this specification is epsilon(n)=1/3. Q below is
fixed before delivery, including branches that later abort. Clean input
is included. The source retains all its specified feedback from actual
label/probe/reset measurements during acquisition. Virtual outcomes used
in a causal proof below are withheld only in that analytical reordering;
no actual feedback is removed from the supplier model.

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

For cost notation set L=max(1,ceil(log2 n)). All exact parameter ceilings
are computed as written; for n>=2, L=Theta(log2 n).

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


EXTRACT uses Qcap=Q fixed in Section4. Put J_e=n+4,

    h=ceil(log2(2^64 Qcap (n+5))), F=2^21 h.

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
cap of Section4 gives h=O(log n), so this is O(n^2 L) per complete call.
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
4(n+5)2^-h <= 1/(2^62 Qcap). The union bound for at most Qcap adaptive HONEST calls is
2^-62, including discarded honest copies. In the analytical exact-label process preserve the COMPLETE actual probe,
position and reset transcript, sampled conditional on its honest latent k.
Only the reported honest numerical label is replaced by that k. The supplier
still uses every actual measurement outcome; none is erased from its feedback.
Until the first incorrect honest report this process agrees with the actual
execution. The total disagreement probability is at most2^-62. This is a
coupling, not conditioning on all labels being correct.

Each call takes O(n h L+n^2 L)=O(n^2 L) core operations under the actual
polynomial source budget, O(n) qubits and O(n^2) classical bits. Store the n+5 six-bit
directions and their empirical counters explicitly. All loops have fixed bounds.

## 4. Actual deliveries, a late random split and its count event

For ALL n>=1 compute the integers

 k=3*2^22*(n+32), Q=2^18*k=3*2^40*(n+32), Qcap=Q,
 m=Q-k, r=m/3, D=ceil(sqrt(16k)), R=r+D, g=m-R.

Ceil-square-root is isqrt followed by one exact comparison/increment.
There is no unknown constant or precomputed advice. In particular k,m,Q
are multiples of3. The large multipliers are actual finite parameters.
The algorithm acquires EXACTLY Q originals before any later abort is
possible. Apply EXTRACT to each with this Qcap and h of Section3, applyX
to its row as in the source convention, and measure/reset/release position
and extraction registers. Retain its row qubit and store the reported
W_j in[0,N). Every copy is kept: no range filter or retry. All probe and
reset outcomes remain actual supplier feedback before later deliveries.
There are Q retained one-qubit rows, not Q copies of the n-bit position.
The Q original count therefore remains deterministic on every branch.

After ALL deliveries choose a fresh uniform k-subset S of{1,...,Q}.
Implementation: initialize the classical array[1,...,Q]. For i=1,...,k
choose a uniform position in[i,Q], swap it with positioni, and use the
first k entries as S. Each uniform integer is sampled from the next
power-of-two interval and rejected if outside its target. It has success
probability at least1/2. HARD-cap this at J=ceil(log2 Q)+256 trials per
choice; on failure release all rows and output0. This adds probability
at most k*2^-J<=2^-256 and bounded polynomial work/storage. The ideal
uncapped sampler is used only for a coupling: its S is exactly uniform,
independent of every delivery, hidden type, latent label and private system.
The actual bounded sampler agrees until its abort. No source call occurs
inside this analytical extension, and Q remains the actual fixed count.
This does not condition a supplier on future fraction fulfillment.

For each j in S draw a NEW fair X/Y basis beta_j, measure the row sign
Z_j in{+1,-1}, store these bits and W_j classically, then release the row.
The remaining m rows are not touched by ANY coarse-search operation.
Classical random addresses to selected rows are charged; no quantum RAM
is used. Source labels for all Q positions remain classical for the endpoint.

Here is the exact count event. Let B<=Q/3 be actual malformed deliveries,
b their number in S, and B_ret=B-b. Conditional on the entire pre-split
history, including all hidden type bits, S is fresh uniform. Hypergeometric
indicator calculation gives

 E b=kB/Q, Var(b)=k(B/Q)(1-B/Q)(Q-k)/(Q-1)<=k/4.

For completeness, distinct draws without replacement have covariance
-p(1-p)/(Q-1), p=B/Q; summing the k variances and k(k-1) covariances gives
the displayed formula. Chebyshev yields the UNCONDITIONAL event E

 |b-kB/Q|<=D, with Pr(not E)<=k/(4D^2)<=1/64.             (E)

On E, both b<=k/3+D and B_ret<=m/3+D=R. The second follows from
B-b<=(1-k/Q)B+D<=m/3+D; it is not an independence assumption.
The hypergeometric variance and tail themselves hold for ANY total B; the
fraction promise is used only in these subsequent deterministic deductions.
Also k>=2^28, D<=4sqrt(k)+1, D<=k/1024,
m>2^17 k, D<=m/6, and g=2r-D>=m/2. For D<=k/1024 put
x=sqrt(k)>=2^14: x^2/1024>=16x>=4x+1. The remaining inequalities
follow directly from m/k=2^18-1. These cover n=1 as well.

### 4.1 Causal laws for selected honest labels and shadow measurements

We must not condition on a final malformed set to assert fresh good labels.
Two equivalent analytical reorderings will be used, with all failure events
combined only afterwards. Preselect S secretly before delivery; it does not
affect acquisition, so this has exactly the same law as drawing S afterwards.
For fixed S, move the row measurement of each selected copy to immediately
after ITS OWN complete label/position/reset instrument. Keep its fair coin
and row outcome virtual and WITHHOLD them from the supplier's controls.
All ACTUAL acquisition outcomes, including position/probe/reset outcomes,
still drive the original adaptive supplier exactly as before.

This is an equality of channel compositions, not a restriction of ModelM.
The moved instrument acts only on that delivered row and fresh coins.
Every later delivery/private operation/position instrument acts on disjoint
systems, with classical controls depending on actual acquisition outcomes
and private outcomes, not on the moved virtual row outcomes. Such local
instruments commute tensorwise even on entangled malformed rows. Commuting
one at a time, branchwise in the actual control histories, preserves the
joint law of type bits, all actual acquisition outcomes and final shadow
records. Private outcomes are retained analytically, never fed back to the
algorithm. The supplier has no post-delivery access to the moved row.

In this enlarged analytical history the next clean delivery is still a fresh
rho_s tensor-independent of ALL earlier systems, so its latent Fourier label
is uniform conditional on the past and on its clean type. The next malformed
conditional row may be arbitrary, which our bounds allow. Future source
choices may depend on every actual position outcome; they do not inspect
that current fresh clean draw before choosing its type. No law is conditioned
on eventual E, correct labels, a fixed malformed subset or cap survival.

For complete clarity, in the analytical exact-label process retain all actual
probe/position/reset outcomes and supplier feedback. Force only the reported
clean label to its latent value. Clip its analytical supplier after Q/3
malformed choices, supplying fresh clean copies thereafter if necessary.
This clipping never changes a promised actual execution before its first
label error: its nondecreasing bad count cannot exceed its final cap Q/3.
It merely defines all counterfactual off-error branches without assuming a
promise for a changed protocol. Hidden type counts are analytical, not flags
provided to the controller. Every malformed instrument/private state before
disagreement is unchanged. Section3 bounds disagreement by2^-62. All ideal
probability estimates are unconditional for this clipped causal process and
transfer until the first error; there is no postselection on budget success. Good row
states conditional on their correct labels are pure pq_W(s/N); disjoint
future channels and shadow measurements cannot alter those pure rows.

For even N, read the latent label parities of the RETAINED clean calls in
acquisition order. For fixed hidden S each next such call was selected by
its position/type before its fresh label. These parities therefore form an
iid fair sequence, by induction on their pre-draw histories, despite adaptive
feedback about previous labels. Append fresh fair bits analytically if too
few retained clean calls occur. On E at least g occur, so its first g bits
are the actual first g retained clean parities. This is an unconditional
sequence statement; we never condition its binomial law on E or coarse success.

## 5. Cubic witnesses from the measured shadow bank

Put R_t(W)=cos(2pi Wt/N)X+sin(2pi Wt/N)Y, a Hermitian reflection.
The reflections here are analysis observables, never physical oracle calls.
For any t,u,W let A=(R_t-R_u)/2 and

 M_tu=(7A-2A^3)/5
     =[11(R_t-R_u)+R_(2t-u)-R_(2u-t)]/20.                 (W)

Indeed R_t R_u R_t=R_(2t-u), and expanding (R_t-R_u)^3 gives
3(R_t-R_u)-R_(2t-u)+R_(2u-t). Since ||A||<=1 and
f(x)=(7x-2x^3)/5 has f(-1)=-1,f(1)=1 and f'(x)>0 on[-1,1],
||M_tu||<=1. This is valid for EVERY reported W, including bad labels.

For a shadow record define the ideal score

 G_j(t,u)=Z_j/10*[11(cs_beta(W_j t/N)-cs_beta(W_j u/N))
                +cs_beta(W_j(2t-u)/N)-cs_beta(W_j(2u-t)/N)].               (S)

Conditional on W and the row's reduced state sigma, averaging the fresh fair
X/Y basis and its sign gives Tr(sigma M_tu). Each realized score has magnitude
at most2: the X or Y coefficient of a norm-one Pauli observable has magnitude
at most1, and (S) is twice that coefficient times Z. A malformed row, however
entangled, has conditional mean in[-1,1]. Freshness of beta after the label,
plus no-signalling for disjoint private operations, justifies this conditional
law. No replacement flag or independent-error assumption is used.

For a clean exact-label record and t=s, uniform W on the COMPLETE[0,N)
gives mean11/20 whenever u!=s and u is not antipodal to s. The complete
Fourier average of R_a on pq_W(s/N) is [a=s modN]. In (W), the only extra
negative coincidence would be2u-s=s modN, namely the antipodal case when N
is even. This explains the classes below. All other nonzero roots average0.

For a fixed false nonantipodal u, let B_i be the hidden type among the k
shadow positions in the causal order of Section4.1. The increment

 Y_i=G_i(s,u)-11/20+(31/20)B_i

has conditional mean>=0. Its support is within[-51/20,3], an interval
shorter than6. The conditional centered log-MGF is at most36t^2/8: its
tilted variance is at most36/4, integrate twice at zero. With negative t,
the mean sign gives the same bound for Y itself. Iterating and optimizing
therefore bounds Pr(sum Y_i<-a) by exp(-a^2/(18k)). At a=k/256 this is
exp(-k/(18*2^16)). Union over at most N true-oriented pairs is <2^-80,
because k/(18*2^16)>10(n+32), while N<=2^n and exp(-x)<=2^-x.
This tail is unconditional for each hidden S and hence for random S.

On E and outside this tail, the ideal average G(s,u) is at least

 11/20-(31/20)(1/3+1/1024)-1/256.

Section6's pointwise implemented-score error is at most1/1024, uniformly
in roles and records. Thus every true-oriented implemented average is
at least1/30-31/20480-1/256-1/1024 >1/64. Reverse orientations are below
-1/64. This simultaneously covers all member comparisons needed to separate
the true class. It is obtained by intersecting unconditional events, never
by claiming selected uncorrupted labels stay iid after conditioning on E.

## 6. Phase caches and exact rational comparisons

Use fixed integers q=14,r_phi=26,b_cos=30 and
p=r_phi+4+ceil(log2 n). For each shadow label W compute by binary long division

 E_W=floor(2^(n+p) W/N).

It has n+p bits. Store it classically with W,beta,Z. For bit position ell of
a candidate t, 0<=ell<n, its p-bit sliding window

 c_(W,ell)=floor(E_W/2^(n-ell)) mod2^p
          =floor(2^p frac(2^ell W/N))

follows by nesting integer floors. Controlled on candidate bit t_ell add
this KNOWN constant into a p-qubit V modulo2^p. After n such additions,
copy V's top r_phi bits to a row phase-cache word a_W(t), then reverse all
additions and release V. The circular error of V/2^p from Wt/N is less
than n2^-p<=2^(-r_phi-4). Consequently a_W(t) differs from the exact word

 T_W(t)=floor(2^r_phi frac(Wt/N))

by at most ONE circular grid cell. A fresh candidate cache contains these
r_phi-bit words for all k shadow labels, coherently dependent on t.
For a KNOWN accepted pivot compute T_W(pivot) by exact modular multiplication
and fractional division CLASSICALLY, once, and retain its cache classically.
For even N an antipodal member's word is obtained by adding
2^(r_phi-1)*(W mod2), in either role. No extra approximation is introduced.

Generate a separate fixed cosine grid C_v,0<=v<2^q, at denominator2^b_cos
using Section3's Machin/Taylor recipe at angles2pi v/2^q. Round and clip to
[-1,1]. Its error is <=2^-b_cos; clipping cannot increase error to a value
already in[-1,1]. For a periodic r_phi-bit phase x, let I(x) interpolate
linearly between adjacent grid entries, including the wrap. This has range
[-1,1], slope magnitude at most2pi+2^(q+1-b_cos)<7, and pointwise error

 e_I<=2^-b_cos+pi^2/2^(2q+1).                              (I)

The interpolation bound follows by subtracting the affine interpolant on
an interval of length h: for |f''|<=4pi^2, the error is at most4pi^2 h^2/8.
Taylor's theorem or integrating the second derivative twice gives it.
For high index h and low remainder z of a phase word, the actual rational
is [C_h*(2^(r_phi-q)-z)+C_(h+1)*z]/2^(r_phi-q), with fixed denominator
2^(b_cos+r_phi-q). All widths in this interpolation are absolute constants.
Sine uses the same I with a quarter-period subtraction.

The implemented G replaces each trigonometric value of(S) by I at the
corresponding phase words, using modular affine combinations2a_t-a_u and
2a_u-a_t. In either fresh/exact role a member phase differs from its true
phase by less than two r_phi cells. An affine combination differs by less
than six. Thus uniformly over EVERY record, including arbitrary malformed
ones, the pointwise difference from(S) is at most

 (12/5)e_I+(196/5)2^-r_phi <1/1024.                        (A)

For example substitute pi<22/7 into(I) and check the rational inequality.
Actual score magnitudes are at most12/5<3 by the displayed coefficients
and the range of I. Scores have common denominator
10*2^(b_cos+r_phi-q), independent of n. Choose exactly
w=bit_length(k)+50 bits for each signed two's-complement accumulator.
Every accumulated numerator has absolute value at most24k*2^42<2^(w-1),
so no overflow occurs. Threshold numerators are smaller. These widths are
O(log k); all sums use that same fixed denominator. There is no threshold rounding:
comparison to tau*k is done by exact integer cross multiplication.

Exchanging the FRESH and EXACT-GRID roles changes each member phase by
at most one cell, each affine combination by at most three cells. The
interpolator slope bound gives per-record discrepancy below
(1/10)*7*(22+6)*2^-r_phi<20*2^-r_phi. Use the conservative bound

 epsilon_role=51*2^-r_phi.                                (D)

Averages, minima and maxima preserve this bound. It is deterministic for
EVERY shadow record string and pair of classes, not just correct labels.

### 6.1 Exact circuits and their streaming cost

An in-place p-bit constant addition modulo2^p is a known permutation.
Compute its ripple carries and sum in clean scratch with O(p) gates, then
use the inverse constant to clear the original input in the standard
compute/swap/inverse construction. Controlling every gate on one candidate
bit gives CNOT, Toffoli, or a triply controlled X. The latter uses a clean
ancilla: compute the AND of two controls, Toffoli with the third, undo the
AND. Hence it still has O(p) exact Clifford+T gates and O(p) clean scratch.
Constant and register additions/comparisons similarly use linear ripple
circuits and their reverses, as in Section1. No unknown-state inverse occurs.

The classical generator maintains a fixed number of current wire/address
counters. Binary increment/decrement has amortized constant bit flips;
initializing a descriptor takes O(log n)<=O(p) per p-bit adder. It emits
one instruction per fixed carry stage, changing persistent descriptors
instead of serializing an exponential circuit. Reading the p-bit window
costs O(p) bit reads; constructing its ripple stage list costs O(p) core
operations. EVERY indexed read/write, generated instruction and quantum
gate additionally pays A_addr=ceil(log2(S_C+S_Q+2))=O(L). There is no
unit-cost classical word arithmetic hidden here.

An I lookup scans all2^q known grid entries with equality tests, writes
its fixed-width numerator, performs the fixed-width interpolation, then
uncomputes. Its core cost is an absolute constant for q=14. Adding its
signed contribution to an O(log k)-bit score register costs O(log k) core
operations. Across all k labels a fresh cache costs O(k n p)=O(n^2 L)
core instructions; a comparison to one cached pivot costs O(k log k)
core instructions plus O(n) for class order/equality. All accumulators and
per-record scratch are reused/uncomputed. Classical pivot-cache generation
costs O(k n^2 L) conservatively before address charges, only once per
accepted pivot. Its storage is k*r_phi classical bits, not quantum qubits.

## 7. Coarse classes with measured classical pivot histories

Classes are singletons for odd N and antipodal pairs{a,a+N/2} for even N.
Their canonical representatives are respectively[0,N) and[0,N/2). Let M_cls
be that number. For distinct classes put the smaller representative first.
For their current fresh/exact phase-role assignment define

 F(first,second)=max_(t in first) min_(u in second) average_j Gtilde_j(t,u).

At a pivot threshold tau the canonical FIRST wins iff F>=tau; the SECOND
wins otherwise. This defines one direction for every comparison even when
arbitrary false classes have no intrinsic max/min winner. It uses at most
four signed integer average comparisons. This canonical convention matters:
we do not silently assume that max/min in the reverse order is its negative.

On E, correct labels and Section5's sign event, the true class wins against
EVERY other class in either role whenever |tau|<=1/256. If true is first,
its actual member s has score>1/64 against all other members, so F>1/64.
If true is second, each false first member loses to member s, so F<-1/64.
These statements include all possible fresh/exact encoding choices.

Start with all valid representatives. Keep a CLASSICAL list of accepted
pivots, their thresholds and their exact phase caches. A candidate is a
contender iff it is valid, equals no old pivot, and beats every old pivot
using that old pivot's threshold and exact cache, with the candidate FRESH.
Thus a selected pivot is removed. A true pivot, once selected, leaves no
contender on the good sign event; until selected the true class survives.

### 7.1 Fresh threshold and contextual pair counting

AFTER a pivot has been sampled and measured, draw a new independent 16-bit
integer J_p and set tau_p=-1/256+J_p/2^23. Its threshold was not used during
its own sampling. It is used only in later membership tests against it.
Every threshold lies in[-1/256,1/256). One may imagine independent thresholds
assigned to potential pivots but not revealed until selection; no exponentially
large threshold list is actually allocated. Current contenders depend only
on thresholds of old, already removed pivots, so unused ones remain fresh.

For any two distinct current contenders x,p, consider the canonical scores
when x is fresh/p exact and when p is fresh/x exact. Their difference is
at most epsilon_role from(D), for every record string. For the common
uniform threshold grid, the difference between its two cutoff probabilities
is at most

 nu=128*epsilon_role+2^-16=59/2^19<1/1024.                  (C)

Indeed a length-epsilon_role interval contains at most epsilon_role*2^23+1
grid points, out of2^16. Depending on which class is canonical first, the
two ordered win probabilities therefore sum to at most1+nu: one is the
cutoff probability, the other its complementary cutoff with the perturbed
role score. This accounts for contextual comparisons; a fixed tournament
is not assumed.

For a uniform pivot in a contender set S, averaging its NEW threshold and
pair-counting unordered pairs gives

 E[|S_after_accept| | S] <=(1+nu)(|S|-1)/2 <=3|S|/4.       (P)

Old membership constraints remain; new ones can only remove additional
contenders. The estimate is valid for every record string and previous
history, not just strings satisfying the true-class sign event.

### 7.2 Bounded mixed-Grover sampler

Use n candidate qubits, padded to Tpad=2^n; invalid class representatives
are unmarked. The contender predicate is an explicit exact Boolean circuit:
compute the shared k-word fresh phase cache of Section6, compare to each old
CLASSICAL cached pivot by scanning all k records into at most four score
accumulators, compare to its exact tau_p*k, and retain one win flag. Include
validity and inequality to all old representatives. Flip phase on the AND
of flags, then reverse every flag computation and the fresh cache. All
ancillas return to0. An old cache is read classically in fixed order and its
bits generate known gates; no quantum-addressed lookup or source-bank read
occurs. The cosine table is likewise read by the explicit equality scan.

There are at most H=64(n+1)+1280 old-pivot slots. Win flags use O(H) qubits;
cache/score scratch is reused. The retained source rows are not operands
of this circuit, its inverse, diffusion, or any verification operation.

An attempt draws a fair coin. One branch measures a uniform candidate
immediately. The other chooses a uniform integer j0 in[0,B), with B a
power of two, and applies j0 standard Grover iterations to H^n|0>, then
measures. Verify the measured candidate with the SAME fresh-role contender
predicate evaluated classically; accept only a verified mark. The reflection
is H^n, an exact all-zero test/phase flip, and H^n, with linear Toffoli-chain
scratch. All clocks, fair bits, verification, generation and resets count.
Fresh query work is prepared independently after each failed attempt.

If the marked fraction f>=1/2 the direct half alone succeeds with probability
at least1/4. If0<f<=1/2 and B>=4/sqrt(f), then for theta=arcsin(sqrt f),
B sin(2theta)>=1 and the mean random-clock success is

 (1/B)sum_(j=0)^(B-1)sin^2((2j+1)theta)
 =1/2-sin(4Btheta)/(4B sin(2theta))>=1/4.

The mixed success is therefore at least1/8. Conditional on acceptance the
pivot is EXACTLY uniform over the marked contenders: Grover amplitudes
are equal on every marked basis state for each fixed clock, and mixing
clocks/direct trials preserves that uniform conditional law. If there are
no marks no pivot is accepted. Failure leaves the contender list unchanged.

Each attempt measures and releases its entire candidate/query workspace.
On acceptance copy the CLASSICAL representative to the pivot list, draw its
fresh threshold, and generate/store its exact phase cache classically.
No coherent quantum history is retained. This is legitimate because the
predicate reads only the measured shadow records; conditional on those
records the untouched retained bank is independent of fresh coarse qubits
and coins. Measuring/forgetting coarse helpers does not act on that bank.
This is precisely the storage benefit of splitting; no known-undo or gentle
measurement lemma about a reused source bank is invoked.

### 7.3 Literal schedule and coarse failure

For ell=0,...,n make64 attempts with B_ell=2^(ceil(ell/2)+2), then make1280
further attempts with B_n. Store the last accepted pivot. If none was
accepted use representative0. These are hard limits, even on arbitrary
wrong-label records. With rho=31/32, (P) and sampler success imply

 E[|S_next| | S] <=rho|S|+(1-rho)2^(n-ell).

For |S|>=2^(n-ell) the sampler succeeds with probability>=1/8, and an
acceptance reduces expected size by at least a quarter. Below that size,
nonincrease suffices for the displayed additive estimate. Since
rho^64<1/4, induction over levels gives E|S_after_level_n|<=2: if the
previous bound is twice the preceding threshold, it is four times the
new threshold, and the recurrence after64 steps is <=7/4 of the new
threshold, hence<=2. The initial bound is |S|<=2^n.

In the final1280 attempts, EVERY nonempty set has the success guarantee,
so E|S_final|<=2rho^1280<2^-39. The last inequality follows from
rho^32<=exp(-1)<1/2. Consequently Pr(S_final nonempty)<2^-39 for every
fixed shadow record string. On the true-class sign event the true class
survives until selected and then ends all acceptances. If the last accepted
pivot is not true, the true class is still a contender. Coarse-class failure
outside the already stated sign/count/label exceptions is therefore <2^-39.

The total Grover clock budget is at most
64 sum_(ell=0)^n B_ell+1280B_n <=1536B_n=O(2^(n/2)),
since the paired geometric sum is at most4B_n. This is a worst-branch count,
not expected work or an uncharged powered oracle. There are at most H=O(n)
pivots/attempt histories, all stored classically. No acquisition occurs here.

## 8. Untouched retained bank, counted phases and the endpoint

For odd N the correct coarse singleton is already the entire secret.
For even N let its representative be t. When the class is correct, s is
either t or t+N/2. On a correctly labelled clean retained row, correcting
by phase -2pi W_j*t/N makes its X sign + for both secrets when W_j is even,
and makes the X sign deterministic + or - according to the true direction
when W_j is odd. Thus even W gives a neutral trit; odd W gives the direction
of its measured X sign. Arbitrary malformed rows give arbitrary trits, but
each can contribute at most one false direction. This remains true for
correlated rows and adaptive private processing.

### 8.1 An ordinary work gradient, with no free rotations

Choose a power G=2^g_aux with G>=2^80(Q+1), using
 g_aux=ceil(log2(2^80(Q+1))).
The work state is the POSITIVE-exponent Fourier state
 gamma=G^-1/2 sum_(x<G)exp(2pi i x/G)|x>.
It is generated using only initialized ancillas, not an original source call.
In each of80 capped attempts prepare g_aux fair computational bits by H
and measurement, use their computational basis state as a register, and
discard that random value from all future use. Its reduced state is I/G,
diagonal with the uniform ensemble of positive-exponent Fourier chi_u.
Use the Section3 data-label instrument for known modulus G, with
h_aux=ceil(log2(2^124(g_aux+5))) and its prescribed F, to estimate u.
The same nondemolition proof applies to each eigenvector: per-attempt error
is at most4(g_aux+5)2^-h_aux<=2^-122. No coset row is required for these
controlled translations on an ordinary generated data register.

Reject even estimates, measuring/resetting/releasing that attempt's register.
For an odd estimate u, compute u^-1 modulo G classically and apply the known
permutation x->u*x mod G. On correct estimation it maps chi_u to gamma.
Explicitly, add u*x into a clean g_aux-bit register using bit-controlled
constant additions, swap, then subtract u^-1 times the new first register
from the second. It becomes0 for EVERY basis input. Each sequence has
O(g_aux^2) exact gates/O(g_aux) scratch; precomputed doubling constants use
O(g_aux^2) CLASSICAL bits. Extended Euclid and their generation are polynomial
in g_aux. This is a complete known unitary word, with no source inverse.

Fresh latent u is uniform each attempt, so all-even failure has probability
2^-80. Any estimation error over80 attempts has probability at most
80*2^-122<2^-115. On the complementary event the accepted state is exactly
gamma; if none accepts output0 after releasing work. Thus the whole flagged
preparation is within trace distance2^-80+2^-115 of ideal success with gamma.
This is an unconditional state comparison, not postselection as an oracle.
Preparation is independent of the retained bank, even though it follows a
classical coarse answer; it uses only Q and fresh random ancillas. The unused
basis seed is charged then discarded. Supplier operations after the last
delivery act on a disjoint private system and cannot signal a change in the
algorithm's reduced state; their private outcomes are averaged, not supplied
to future algorithm controls. The same local-channel argument justifies the
I/G ensemble analysis when those unused random outcomes are public.

Translation by c has eigenvalue exp(-2pi i c/G) on this POSITIVE-exponent
gamma. For each retained reported W compute
c_j=round(G W_j*t/N) mod G by exact classical arithmetic. Controlled on its
row being1 add c_j to gamma. This applies a phase approximating
-2pi W_j*t/N and leaves gamma unchanged. All these additions are exact
Clifford+T; the only approximation is the classical integer rounding.
For arbitrary joint row states, telescoping the controlled-unitary norm
errors gives output-probability error at most16Q/G<=2^-76, conservatively.
Indeed each phase discrepancy is at most pi/G, hence its unitary norm error
at most pi/G; purify the bank, telescope at most Q operations, and use the
pure-state trace-distance bound and contraction. The constant16 exceeds
all these factors. No irrational gate or uncharged Fourier preparation is used.

### 8.2 Trit rule with a split-dependent threshold

Measure X on the corrected retained rows. Ignore even reported W; for odd W
increment the direction named by its sign. If a direction count exceeds R,
return it; if neither exceeds R use a fresh fair bit. If both exceed R choose
the first (this can happen only off the promised count event or other errors).
Use the representative t or t+N/2 as the corresponding full answer. All loops
and count registers have fixed finite limits. The threshold R is computed
from Q,k, not an unknown malformed count.

On E, correctly labelled clean retained rows supply no false trit and
malformed rows supply at most B_ret<=R false trits. There are at least
g=m-R retained clean calls. Section4.1's first g iid fair latent parities
therefore imply that the correct count dominates X_g~Bin(g,1/2) on E,
without conditioning its binomial law on E or on the coarse answer.

Here is a quantitative elementary bound that covers every n. If
 a_h=binom(2h,h)/4^h,
then a_h<=1/sqrt(h+1) by induction: a_(h+1)/a_h=(2h+1)/(2h+2), and
(2h+1)^2(h+2)<=4(h+1)^3. Odd binomial maxima are no larger than the
preceding even one, so every atom of Bin(g,1/2) is at most2/sqrt(g+1).
Symmetry gives Pr(X_g>g/2)>=1/2 minus half the largest atom. Since
R-g/2=3D/2, moving the cutoff removes at most2D+1 additional atoms. Thus

 Pr(X_g>R)>=1/2-(4D+4)/sqrt(g)
           >=1/2-17/256=111/256>27/64,                   (B)

using D<=4sqrt(k)+1, sqrt(g)>=2^8 sqrt(k), and sqrt(k)>=8.
Indeed (4D+4)/sqrt(g)<=(16sqrt(k)+8)/(256sqrt(k))<=17/256.

In the ideal endpoint with a correct class and the good count/label events,
false counts cannot exceed R. If X_g>R the answer is correct; otherwise it
is at least a fair guess. The unconditioned binomial bound therefore gives
success at least1/2+(1/2)*(27/64)=91/128 before exceptional-event losses.
To make the lack of conditioning explicit, let A denote the joint good
count/class/label event. The conditional guarantee bounds the actual success
indicator's expectation below by E[(1/2+1_(X_g>R)/2)1_A], which is at least
1/2+Pr(X_g>R)/2-Pr(not A). The binomial variable is the unconditional
analytically extended sequence; no success-conditioned distribution is used.

The complete losses are at most

 subset abort2^-256 + count event1/64 + clean labels2^-62
 + shadow signs2^-80 + coarse elimination2^-39
 + gradient preparation2^-80+2^-115 + endpoint phase error2^-76 <3/128.

For odd N the endpoint is unnecessary, and this same conservative bound
still applies. Hence unconditional full-secret success on every N>=2 is
strictly above91/128-3/128=11/16>2/3. All actual supplier feedback and
private correlations were retained. There is no expected-resource promise,
fixed-position reduction, bank-reuse disturbance assumption or fraction
postselection. The guarantee includes the no-malformed-copy clean case.

## 9. Joint EVERY-BRANCH resources and exact envelopes

Every loop above is bounded BEFORE its execution: Q acquisitions, the subset
rejection trial cap,80 gradient attempts, H coarse attempts and their literal
Grover clocks. Every original produces one retained row before the split;
no helper or inverse acquires a source copy. Thus Q=3*2^40(n+32)=O(n)
on EVERY branch, including all aborts. The fractional promise is exactly
floor(Q/3)=Q/3 and is applied to those originals, never to a selected bank.

Peak quantum storage during acquisition is Q row qubits plus one n-bit
position and O(n) reused extraction scratch. During coarse search it is m
untouched row qubits, n query qubits, k*r_phi fresh phase-cache qubits,
O(H) membership flags and O(n) reusable arithmetic/diffusion scratch.
All are O(n); Q,k,H have fixed linear envelopes and r_phi is a constant.
Exact pivot caches and candidate/clock histories are CLASSICAL. Gradient
preparation adds O(log n) work qubits and later reuses them. Source data,
failed query registers and measured rows are actually reset/released. Thus
S_Q=O(n) on every branch, even malformed numerical branches.

Classical labels use Q*n=O(n^2) bits; shadow packed words and signs use
O(k(n+p))=O(n^2). The subset array uses O(Q log Q)=O(n log n), and old
phase caches H*k*r_phi=O(n^2), together with H n-bit representatives,
thresholds, bounded counters, fixed tables and reused arithmetic scratch.
All are simultaneously O(n^2). Full expanded quantum circuits, symbolic
source incidence trees and exponential lookup tables in n are not stored.
The tables have fixed, publicly specified finite sizes. Accordingly
A_addr=ceil(log2(S_C+S_Q+2))=O(L), with L=max(1,ceil(log2 n)).

Acquisition uses O(n^2 L) core work per complete extraction from Section3,
with the new h=O(L); its address cost gives O(n^2 L^2) per copy and
O(n^3 L^2) total, including all Q originals and their n+1 input cost.
The bounded subset shuffle uses O(n L^3) charged work conservatively,
smaller than that source envelope. Computing shadow packed words by binary
long division costs O(k n^2 L^2)=O(n^3 L^2) conservatively.

For a contender-predicate call, the shared fresh cache costs O(k n p)
core operations. All H cached-pivot constraints cost O(H k log k+H n)
core operations, since fixed-width interpolation is constant and signed
accumulators have O(log k) bits. With k,H=O(n),p=O(L), this is O(n^2 L)
core instructions/generation steps. EACH indexed bit/gate/descriptor access
pays its O(L) debit, so a query and its complete cleanup cost O(n^2 L^2).
Diffusion costs O(n L). The entire hard Grover budget is O(2^(n/2)), giving
O(2^(n/2)n^2 L^2), including every failed attempt, query reset and verification.

At most H pivots have their exact caches generated, with O(k n^2 L)
core work per pivot before addresses, totaling O(n^4 L^2) charged work.
Endpoint phase numerators and source-label arithmetic are O(n^3 L^2)
conservatively; work-gradient preparation is polynomial in log n, with
its explicit80 cap. Initialization, cleanup and threshold generation are
polynomial and fit these envelopes. These polynomial terms are absorbed
by the declared time: n^2=O(2^(n/2)), as follows for n>=16 by induction in
steps of two from16,17; a finite prefix changes only an absolute constant.
Therefore n^4 L^2=O(2^(n/2)n^2 L^2) as well.

For n>=2, L<=1+log2 n<=2log2 n. Hence the full joint EVERY-BRANCH time
representative is exactly O(2^(n/2)n^2(log2 n)^2). All constants are
absolute, independent of N,s,supplier and outcomes. The SAME finite protocol
at n=1 has bounded costs and the proven success bound; no unreviewed noisy
finite branch or advice is substituted. The logarithm of the time envelope
is n/2+2log2 n+2log2 log2 n, whose exact growth index is1. Each of n^2,n,n
has index0. Only time contributes numeric score[1]; the exact1/3 fraction
is a separate jointly proved guarantee in the identical ModelM context.

This establishes the complete structured resource objects for one algorithm
and parameter rule. No comparison in this proof changes that configuration.
The method trades very large absolute source/sample constants for keeping
the final quantum bank independent of coarse quantum search history. It is
not a claim of optimal constants, a general contamination ceiling, or an
unavailable state-preparation oracle.
