# PSG15: variable-width streaming sieve with a weighted work cutoff

## 0. Joint theorem and provenance

For every N>=2, s in Z/NZ, n=ceil(log2 N), L=log2 n, the single
CLEAN-input algorithm PSG15 below recovers the full secret with
unconditional probability at least1-2^-8>2/3 and jointly, on every branch,

 T=O(2^(n/(2L)-n/L^2)), S_C=O(n^2), S_Q=O(n), Q=O(2^(L^2)).

These displays apply for n>=2; the explicit n<256 finite branch covers
n=1 as well. All outside constants are absolute. Resource indices are
[1,0,0,0]. The sample guarantee is QUASIPOLYNOMIAL, not polynomial;
index0 includes this growth. Fractional tolerance is0 under the exact
independent-ideal-copy model. No positive robustness, optimality, practical
constant or cube-root time is claimed.

Immediate full algorithm/proof source is published PSG12,
cac3285d-da27-4010-a40c-b05d66c0c255, archive
38b7a3589059421b2a508ce6b7420700daed564e. PSG15 changes its maximum
number of positive profile stages from3 toceil(log2n)+4, replaces every
nominal-leaf/source/cap estimate consistently, and proves the new complete
envelopes. The bounded quantum primitive, compact persistent generator,
collective label extraction, stride decoder and original2-adic PARITY loop
are inherited. This proof retains the older fresh success bound1/3.
It does not use PSG14's stronger37/50 proof, robust record decoders,
local root isolation or adversarial error model, nor PSG13's majority wrapper.

The public LSIEVE note0d654368-a9b9-4e9e-8279-4e1b9d5d3d0a motivated
checking a different log-depth time/source/storage tradeoff. Its interval
sieve, large list storage and oblivious-corruption theorem are not used.
The chosen profile and every analytic estimate are reproduced below.
That note's actual publication status is disclosed without inventing a
source archive. The general parameter-tradeoff idea is not claimed as an
independent invention or a new literature-wide complexity class.

Immediate local material sources are PSG7 (commit d772839), for persistent
charged descriptors and its counter/cursor proof, and PSG8 (commit bd374e2),
for compact stage-local rows and separate full-precision pre/postprocessing.
They were unpublished local snapshots when this proof was written; no public
archive identity is invented. The earlier local PSG4 supplies the linear-base
Grover/stride configuration; PSG3 supplies collective label-test rounds;
PSG1 supplies bounded verified discovery and unused-block induction; and
PSW1/PSW2 supply variable-width, weighted-cutoff and truncated-base development.
All needed arguments are reproduced, and prior verdicts are not premises.

Directly consulted published sources include PSR2 submission
16bb6065-c3ca-45fb-b514-86106a310646, archive
7f835a08d1b109847a9b921c02b35361ed350bd0, for signed-label streaming, source
extraction, complete decoding and substantial adapted proof text; SLS
59facd77-4082-40d9-910e-9060c197e72a, archive
643c22bdf74a96b1e08a0eb56f562396c3084adc, for rank/pairing and polynomial-space
accounting context; and CS1 f1481815-9577-4990-abe3-7b79fa5d9284, archive
200ef0387acb280adcd272f4fbcdb805d1786bbe, for exact latent labels, source
transforms, untouched bits and full-modulus decoder material. The final
candidate replaces exhaustive ranking by the explicitly counted search below.

WTS1 submission50a9f13c-eda5-4239-a3c8-28ed83e8ce83, archive
9d8256a16cc1f29c7543af470f03ebc37f8bf0b4, supplies the held-out-block
characteristic lemma, stride rule, essential all-N restriction B>=a2 and
charged enlarged grid. Its vector-table sieve is not executed here.
The collective round was directly informed by the public note and then proof
of844c0fd2-9b1c-4e84-a37c-f402e109985f, archive
7c4b4ed099799e146213c1e3c43a50151482dc6b. That note credits the collective
translation identity in this solver's earlier CS1-C3A public note
05c80793-e172-437e-837c-4c10dd0c4929; its hosted execution failed, so no
mathematical verdict or published source archive is asserted for that entry.

CST-128 submissionf95bb4e2-3d08-4ca0-a34f-99841dca855a, archive
6b7500d549149709fb089338c116904f210b23d1, Section3, was directly consulted
for affine ripple-wire layout, regenerated reverse passes and fully charged
address accounting. Its O(n(log n)^2) test bound is already proved there,
not a new result claimed here. Its sequential shift search is not executed.

Established historical sources include Regev quant-ph/0406151 Section3,
Kuperberg1112.3333 Section4.6, Kitaev quant-ph/9511026, Grover
quant-ph/9605043, and Boyer-Brassard-Hoyer-Tapp quant-ph/9605034v1 Sections3-4.
The needed state, search, precision and circuit arguments are given below.
No oracle is free, and no cube-root-time, positive robustness, historical
invention or optimality claim is made.

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
are charged as well. Here log F=O(log n)=O(L), since h=O(L^2)=O(n).
The quantum translation costs O(n) per round. Decoding and unwrapping add
O(n^2) core operations. Consequently a full call costs

    O(n h L+n^2 L) core operations,

with O(n) qubits, O(n^2) classical bits. Since log2 Qcap=O(L^2) by Section9, h=O(L^2),
and L^2=O(n), this is O(n^2 L) for the complete profile.
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
profile budgets, O(n) qubits and O(n^2) classical bits. Store the n+5 six-bit
directions and their empirical counters explicitly. All loops have fixed bounds.

## 4. Work-balanced profile and bounded-search combiner

Main-branch parameters are computed once for n>=256. For a positive integer v,

 delta(v)=ceil(log2(3(2v+1)))=bit_length(3(2v+1)-1).

Compute ell=ceil(log2n)=bit_length(n-1), and mmax=ell+4.
Starting at a positive trial R, retain R and its next at most mmax-1
POSITIVE descendants under v<-v-delta(v). Stop at the limit or before a
nonpositive value. Reverse them into v_1,...,v_mstar=R, mstar<=mmax.
Choose the least positive R with2sum_i v_i>=n by sequential scan;
no monotonicity assumption is used. R<=ceil(n/2) suffices because the
profile contains R itself. Set u=max(1,floor(R/4)) only as an auxiliary
number for cost estimates and hmax, NOT as a profile truncation threshold.
Section9 proves every actual v_i>=u eventually. The finite main-branch
prefix uses the SAME profile rule and guarded circuits. Compute

    q0=(2R+1)^mmax

by counted integer arithmetic. Its logarithmic size, source precision,
frequency support and both budgets are all included below.

A PS_TREE(D,B) call,1<=D<=n,0<=B<D, has independent ideal leaves with
uniform known labels in[0,2^D). When B=0 return one leaf. Unless explicitly
stated otherwise (the odd-part decoder), calls use B=D-1. Otherwise allocate
actual widths b_mstar,...,b_1 greedily from the root down, b_i=min(2v_i,
B-already_allocated). Then sum_i b_i=B. Let r_i=b_i+1 and
p_i=sum_(j<i)b_j. Level0 returns a leaf. A zero-width level just returns
its child. For b_i>0, recursively build r_i fresh child outputs, then check
and add weight2^v_i to the global weighted-attempt counter before executing
the combiner below. If that would exceed Wcap, abort. On FAIL discard ALL
inputs and query scratch, and build fresh children before trying again.
No output label, including zero, is rejected inside the tree merely because
of its higher bits or value.

### 4.1 Exact state preparation and verified-pair output

The inputs are phase qubits with full signed labels a_1,...,a_k divisible by
2^p, where k=b+1, b=b_i, p=p_i. Their joint state is

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
### 4.2.1 Compact oracle with persistent charged descriptors

Here b=b_i<=2v_i<=2R and k=b+1<=2R+1. Keep all full signed a_j records
for the exact post-search output, but form c_j=(a_j/2^p) mod2^b once per
attempt. Store only b-bit low constants in rows padded to a power-of-two
stride between b+2 and2(b+2). All search accumulators and carry chains have
b+O(1) bits, and query/index strings have k bits. Full n-bit labels are never
fed through each Grover iteration or reduced modulo N/2^D at output.

Put g=1+ceil(log2(n+2)), so g=Theta(L) on the main branch. All quantum-wire
indices and classical addresses have O(g) bits by the polynomial allocation
bound of Section9. Allocate a fixed finite set of descriptor records for the
fixed finite collection of ripple, equality, Toffoli-decomposition and
Hadamard gate families. Each record has its gate type and at most three
binary wire-index fields, O(g) bits each. A record is classical controller
state, included in S_C. A gate invocation uses those already stored fields
DIRECTLY and pays the full O(g) address debit. The binary fields are not
copied to a fresh descriptor at every invocation. This is the model's
classically chosen indexed gate, not quantum-addressed memory or a word
arithmetic primitive. If the gate's encoded addresses are read in full at
invocation, their O(g) read work is included in that same O(g) invocation
allowance, rather than assumed free.

Every controlled addition is a fixed collection of ripple passes. In a
pass each quantum wire index is base+c*r for its bit position r and a fixed
integer c of bounded absolute size. The input-control index is fixed within
that row. Multi-controlled diffusion and the fixed equality tests also have
this form. Thus each gate family has persistent fields that advance or
retreat by a fixed constant as r advances; keep the finite families in
separate records, avoiding any per-gate copy of one whole record into
another. A finite-state pass identifier selects its family. Initializing a
pass's records costs O(g^2) core work conservatively. Fixed constants and
scratch-wire bases are computed once per pass, not per bit gate.

Counter lemma. Over m consecutive increments (or decrements) of an a-bit
binary field, the total number of changed bits and inspected carry bits is
O(m+a). Bit position j can carry at most floor(m/2^j)+1 times; summing this
geometric bound proves the assertion. An update by a fixed bounded constant
is a fixed number of unit updates and satisfies the same bound. The field
itself has a=O(g) bits. Its carry-scan cursor has O(log(g+2)) variable bits.
Place each field and its cursor segment in an aligned power-of-two region;
its high address bits remain stored throughout the pass, and only the
O(log(g+2)) low cursor bits vary when accessing a bit WITHIN the field.
The cursor moves, resets, bounds tests and finite-state transitions cost
O((log(g+2))^3) core operations per inspected carry bit conservatively, plus
O(g^2) initialization/termination per pass. This deliberately allows a
logarithmic factor for cursor-register arithmetic, another for forming its
low field addresses, and a third for the finite control/metadata loops;
these operate on O(log g)-bit indices. The stored high address parts are
reused, while EVERY indexed action still pays the separate full O(g) debit. Each of these actual bit reads
and writes ALSO pays its own full O(g) address debit. High fixed address
parts are never recounted as a free arbitrary-integer operation: they are
initialized and stored, and an indexed read/write uses the existing address
field with its full debit. This proves O((m+g)(log(g+2))^3+g^2) core generator
work for one pass and bounds every carry, including the all-ones boundary.

Use explicit marked iteration tapes for bit positions, initialized with
one marker per position and an end marker. A pass reads the marker at its
persistent cursor and stops at the end marker; it need not compare two
whole g-bit position integers for every elementary gate. Marker storage
is O(R) bits and its initialization/reset is counted. Cursor movement uses
the same counter lemma. The finitely many inverse passes use decrementing
fields and regenerate the same gates in reverse order. Coherent arithmetic
still keeps and uncomputes exactly the Boolean scratch described above.

For the membership circuit, enumerate the k input rows and b bit columns.
Pad the stored low-weight rows to a power-of-two stride between b+2 and
2(b+2); this is O(R^2) classical bits. The row cursor advances by that
power-of-two stride: increment its high row-index field by ONE and keep
the low stride bits zero, rather than performing stride many unit increments.
The bit cursor walks through the row. Their fields
are persistent as above. There are O(R) row passes, each of O(R) gates;
initialization of all row records costs O(R g^2), and bit/carry work costs
O(R^2 (log(g+2))^3). No table of gate descriptions, subsets or iterates is stored.
At most64 exclusion strings are handled the same way. Diffusion, projection,
verification and their row loops are bounded likewise. Since g=O(log n) and R>=sqrt(n/2),
Rg^2=O(R^2 (log(g+2))^3), with any finite exceptions in an absolute constant.
Thus one Grover iteration, including classical generation and control,
has O(R^2 (log(g+2))^3) core work and O(R^2) quantum elementary gates.
The outer Grover-iteration counter may conservatively take O(R) core work
per iteration, still covered by this bound. Its tests and bits are charged.

All quantum gates, indexed classical reads and descriptor-bit updates pay
O(g)=O(L) ADDITIONAL address work. We therefore bound total charged work by
O(L) times the above core count. This includes, rather than omits, reading
an already latched gate's binary indices. There is no fresh O(g)-bit COPY
per elementary gate; that is the implementation change. It is not a claim
that recomputing an arbitrary binary address is a constant-time operation.

There are at most4096 trials and O(2^v_i) iterations per trial. Initializing
low-weight rows, descriptors, marker tapes and full signed-label data for
one complete attempt costs at most O(n^3 L^2) core work, and all non-search
trial overhead fits that bound or the per-iteration allowance. Full signed
label updates, pair projection and final cleanup also fit this one-attempt
O(n^3 L^2) overhead. On this
eventually positive full profile v_i>=u=floor(R/4), R>=sqrt(n/2), so2^v_i eventually
exceeds every fixed polynomial in n. This covers the full-width
O(n^3 L^2) overhead relative to R^2 sqrt(L). Also
(log(g+2))^3=O(sqrt L). Hence a complete
attempt, including initialization and ALL indexed core operations, obeys

    O(R^2 sqrt(L)2^v_i) core work.

For the finite main-branch prefix the SAME generator and integer schedule
are used; an absolute outer constant covers it. The latched fields and
marker tapes add at most O(R^2) classical bits, and no quantum registers
beyond the O(n) scratch already counted. This statement is branchwise and
uses neither successful search nor a favorable carry pattern.

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
statement of4.1 still hold unconditionally. Section5 supplies the fresh
uniform weights needed at each recursively regenerated attempt.

## 5. Unused blocks, termination and the root frequency

Lemma U (joint induction). In the ideal uncapped process, every tree-level
call terminates almost surely. If it cancels p bits, its returned label
x/2^p mod2^(D-p) is uniform, conditional on any external past before the
fresh call. Distinct fresh child calls give independent such quotients.

Proof. The leaf statement is the exact uniform latent-label source law.
Assume the statement at the lower level. Before a new node attempt starts,
its freshly generated children have independent uniform quotients modulo
2^(D-p). Their residues c_j modulo the next2^b are thus independent uniform.
Equation(4.1) gives conditional success at least1/3 before child generation,
whatever the earlier external past. Every failure releases its inputs and
restarts with fresh children. The geometric bound proves almost-sure
termination and finite expected attempts at this level.

It remains to prove the output law that closes the induction. Fix any
finite successful selection transcript through this level, containing all
used leaf values modulo2^(p+b), search choices/outcomes, residue and pair
measurements, and retry choices. Its probability kernel is a function ONLY
of those low parts, by4.1 and4.2; quantum searches used separate registers.
Write each original leaf as k_l=u_l+2^(p+b)H_l, with H_l independent uniform
in Z/2^(D-p-b). The selected output has a symbolic signed incidence vector
z_l in{-1,0,1}, not allzero, determined by the low transcript. Consequently

 x/2^(p+b) mod2^(D-p-b)=c+sum_l z_l H_l mod2^(D-p-b).

Here c is an integer determined by the low parts. At least one z_l is a
unit +1 or-1, so the sum is uniform on that cyclic group. Marginalizing over
all finite successful low transcripts proves the output law. Fresh disjoint
leaf sets give the conditional independence for successive child calls.
This conditioning does NOT include irrelevant high-valued EXTRACT records
or all full labels stored by the controller; the ideal process marginalizes
those records and uses exact latent labels. It does not condition on the
event that all actual extractions were correct. The real/ideal comparison
later uses an additive error coupling. Computing/storing full labels does
not change that marginal law: decisions at this level use only the stated
low residues, and do not filter a zero or other high output value. QED.

There are at most mmax stages, every r_i<=2R+1, so

 q_D=product_i r_i<=(2R+1)^mmax=q0.

A returned tree has at most q_D nominal distinct leaves. Its label is2^B W
with |W|<2^(D-B)q0. Every stored label has O(n+log2q0)=O(n) bits,
also on numerical-error branches, since log2q0=O(L^2)=O(n).
No incidence vector or subset list is stored. The base consists of fresh
independent leaves, so Lemma U and its low-bit kernel argument apply.

For the root write h=D-B>=1 and each accepted leaf as
k_l=u_l+2^B tau_l, with independent uniform blocks tau_l in[0,2^h).
Condition on low parts u_l, residue/search/pair outcomes, retry choices and
independent previous roots. All these kernels use only bits below B and
are phase independent. Thus the tau_l remain independent uniform blocks.
Its nonzero signed incidence vector gives

 W=c+sum_(l in S+)tau_l-sum_(l in S-)tau_l, |S+|+|S-|>=1.

Lemma5.1. With A=2^h, for every real y, conditional on that low transcript,

 |E exp(2pi i yW)|<=D_A(y)=|(1/A)sum_(t=0)^(A-1)exp(2pi i yt)|,
 D_A(y)<=|cos(pi y)|,
 D_A(y)<=min(1,1/(2A*||y||)) when ||y||>0,                (5.2)
 Pr[W odd]=1/2.                                         (5.3)

Proof. Each independent block contributes D_A(y); at least one is present
and all factors are at most1. Writing a uniform block as its independent
fair binary digits factors its characteristic modulus into
product_(j=0)^(h-1)|cos(pi2^j y)|, giving the first bound. The geometric sum
has modulus |sin(pi A y)|/(A|sin(pi y)|). For circular distance x=||y||
in(0,1/2], the sine chord gives |sin(pi y)|>=2x, proving the second bound.
At y=1/2 the fair lowest bit makes the characteristic function zero, so
parity is fair. This is about the full signed integer W, not a claim that
its full integer distribution is uniform. Irrelevant high EXTRACT records
and future budget survival are marginalized, not conditioned on. QED.

## 6. Odd-part recovery by free-frequency decoding

If M=1, put s1=0, K=0, Sodd=0 and skip this section. Otherwise M >= 3, so N >= 3 * 2^a2
and d - 1 >= a2. Put theta=s1/M in[0,1). Define

 hmax=1+floor(u/8), h=min(d-a2,hmax), B=d-h>=a2,
 stride=max(1,h-4), D=d, nq=2^(h-1)q0,

and

    K = 2^13 (ceil(log2 nq) + ceil(log2 n) + 30).

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

because 2^(B-a2) alpha_j = 2^(j*stride) (mod M) and s = s1 (mod M). So a PS_TREE(d,B) root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^(j*stride) W.

Measurement. For i = 1..K:
- run PS_TREE(d,B);
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

Enumerate the candidates in increasing order, keeping the K residues
(f_i c) mod 2^(P_j) and updating each with one addition per step, and keep a
running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have
fixed lengths, and the decoder returns a candidate on every branch.

Lemma 6.1. Suppose theta is within circular distance rad_j of z_(j-1) (no
condition when j = 0). Then, in the ideal run, with probability at least
1 - 2^-20/n, theta is within circular distance 2^-(j*stride+stride+2) of z_j.

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

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the
maximizer is not far. There are at most 2^(ceil(log2 nq)+9) events, and since
e^-x <= 2^-x, exp(-K/8192) <= 2^-(ceil(log2 nq) + ceil(log2 n) + 30). The failure
probability is therefore at most 2^(9-30)/n <= 2^-20/n. QED.

For stage j+1 the hypothesis of Lemma 6.1 is the conclusion of stage j, since
2^-(j*stride+stride+2) = rad_(j+1). By induction, with probability at least 1 - 2^-20, theta
lies within 2^-((J+1)*stride+2) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.


Stage-count bound. The chosen hmax is Theta(R) as R grows, since
u=floor(R/4). If h=hmax, stride=Theta(R), so Sodd=O(1+log M/R).
If h<hmax, then h=d-a2=floor(log2 M), hence log2 M<h+1. For h>=5,
h/(h-4)<=5; for h<=4, stride=1. Thus Sodd=O(1) in this case.
In all cases Sodd=O(1+n/R), K=O(log nq+log n)=O(R+L^2)=O(R),
because h<=hmax=O(R), log2q0=O(L^2), and L^2=O(sqrt n)=O(R). Consequently Sodd*K+2n=O(n), with absolute constants.
These are bounds for the fixed stage counts before execution, not favorable
outcome counts. No factorization of the odd M is needed.

## 7. 2-adic recovery

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for
a unique s2 in [0, 2^a2). The bits of s2 are found at levels g = 0..a2-1. Let
s2low be the known low g bits. Put sh_g = s1 + M s2low (mod N), wd = a2 - g, and
rem = (s2 - s2low)/2^g in Z/2^wd. Then s - sh_g = M 2^g rem (mod N).

Leaf qubit for level g:
- acquire a copy and apply Shift_(sh_g), which makes the secret s - sh_g;
- run EXTRACT to obtain k, and apply X to the control.

Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with
kk = k mod 2^wd. Since 2^wd divides N and k is uniform on Z/NZ, kk is uniform on
[0, 2^wd). Use kk as the label.

- If wd = 1: if kk = 1, measure X; the outcome is + iff rem is even. If kk = 0,
  discard and repeat.
- If wd >= 2: run PS_TREE(wd,wd-1). If W is even, discard and repeat. If W is
  odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

By (5.3), each attempt succeeds with probability exactly 1/2, even if s1 was
wrong. Set bit g of s2. In the ideal run with s1 correct, every bit is correct.
Output (s1 + M s2) mod N.


## 8. Complete algorithm, two cutoffs and success

For n<256 use exhaustive shift testing. For t=0,...,N-1 use at most n+10
fresh copies, subtract t modulo N controlled by the first qubit, and measure
that qubit in X. Reject t at the first minus and output the first candidate
passing every test, or0 if none. The true t=s always passes; each wrong
candidate passes a fresh test with probability1/2. Thus wrong output has
probability<(N-1)2^(-n-10)<2^-10. It uses at most N(n+10) copies,
O(n) qubits and O(n^2) classical bits. All charged work is O(Nn^4).
The fixed finite prefix is absorbed in the stated asymptotic bounds.

For n>=256 compute the profile of Section4, all decoder parameters and K.
Define integer budgets

    H0=Sodd*K+2n,
    Qstar=2*3^mmax*q0*H0+2n, Qcap=1024Qstar,
    Wstar=3*mstar*2^R*H0, Wcap=1024Wstar.

The fixed H0 overbounds Sodd*K+2a2 for every modulus; when M=1, Sodd=K=0.
Initialize the acquisition counter and the weighted-attempt counter to zero.
Before any acquisition that would exceed Qcap, abort, release all registers
and output0. Before a combiner attempt, after building its inputs, check
whether adding its nominal weight2^v_i would exceed Wcap; if so abort
likewise, otherwise add it and execute the complete attempt. EXTRACT uses
this fixed Qcap. Run the odd-part decoder followed by the2-adic procedure,
then output(s1+M*s2) mod N. No circuit execution is hidden in either counter.

Expected source bound. In the ideal uncapped run each accepted leaf costs
at most two source copies. By Lemma U and(4.1), before each attempt generates fresh children it
succeeds with probability at least1/3. Thus, uniformly over previous history,
E_i<=3r_i E_(i-1). Zero-width shortcuts only reduce this bound.
There are at most mmax nonzero stages, so directly

 E_root<=2 product_i(3r_i)<=2*3^mmax product_i r_i<=2*3^mmax*q0.

No independence of attempt cost and success is required. The event of
reaching an attempt depends on earlier attempts; its fresh child calls
have the same uniform conditional cost bound. Summing their geometric
upper bound, with failure at most2/3 before each fresh attempt, gives the
displayed recurrence. Conditioning on fixed child labels is not used. Odd-part decoding uses at
most Sodd*K roots; each of at most n2-adic bits needs two roots in expectation
by parity fairness, or two direct copies when wd=1. Thus ideal expected
acquisitions are at most Qstar, irrespective of earlier decoder outcomes.

Expected weighted-attempt bound. For a root call, the expected number of
leveli attempts is at most 3 product_(j>i)(3r_j). The same conditional
geometric-sum argument proves this by induction, including attempts in
failed ancestors. Telescoping the profile gives

 product_(j>i)(3r_j)<=2^(R-v_i).

Hence the expected sum of weights at that level is at most
3*2^(R-v_i)*2^v_i=3*2^R, and at most3*mstar*2^R over all levels.
Zero-width shortcuts contribute zero. Summing over all roots, with the
same conditional argument for odd-W repeats, bounds ideal expected total
weighted attempts by Wstar.

Apply Markov separately to source count and weighted attempts in this
ideal uncapped process. Each cutoff changes it only on an event of
probability at most1/1024. In particular, a work cutoff before the next
attempt implies the uncapped weighted total would exceed Wcap; children
already built are already charged. There is no assumption that caps and
decoder events are independent. The odd-part error is at most2^-20, and
conditional on its correctness the2-adic measurements make no error.
On the actual capped run the probability of any EXTRACT label error is
at most2^-14 by Section3. Couple the actual and ideal processes until
a label error or cutoff. Total failure is at most

    2^-10+2^-10+2^-14+2^-20 < 2^-8.

The finite branch meets that bound as well. This proves unconditional
full-secret success at least1-2^-8. All trials, failures and aborts remain
in the resource counts; nothing is postselected free of charge.

## 9. Complete log-depth resource estimates

### Exact finite profile and an asymptotic certificate

The actual positive values are distinct integers at most R, so their
number is at most R and sum at most R^2. Hence n<=2sum<=2R^2 and
R>=sqrt(n/2), valid on every main-branch length regardless of the limit.
Also n<=2mmax R, so R>=n/(2mmax). The scan always terminates byceil(n/2).
All parameters and guards are finite exact integers, uniformly computable.

For the sufficient range L>=32, abbreviate m=mmax, so L+4<=m<=L+5.
The inequality2^L>=4(L+6)^3 holds at32 and thereafter: the logarithmic
ratio has derivative ln2-3/(L+6)>0. Test

 Rtest=ceil(n/(2m))+ceil((m-1)(ell+5)/2).

Since ell<=L+1, the two ceiling overheads are at most
(L+4)(L+6)/2+2<=L^2. Thus Rtest<=n/(2m)+L^2<=n.
Every decrement is at most ell+5. All m test values stay positive, since
the last is at least n/(2m)-(m-1)(ell+5)/2>0 by the displayed cubic bound.
Their twice-sum is at least2mRtest-m(m-1)(ell+5)>=n. Thus the ACTUAL
minimizing integer R obeys

 R<=n/(2m)+L^2<=n/(2(L+4))+L^2, R=Theta(n/L).

For the actual profile, each of its first m potential values is at least
R-(m-1)(L+5)>=R-(L+5)^2. Since R>=n/[2(L+5)] and
n>=4(L+6)^3, this is at least R/2>0. Therefore all m values exist
and v_i>=R/2>=u in this sufficient range. The same algorithm is used
below it; finite main-branch lengths only enlarge an absolute outside
constant. No new exhaustive branch, table or advice is inserted to make
an asymptotic inequality true.

For later source accounting the same bounds give
2R+1<=n/m+2L^2+1<=2n/m<=2n/L eventually (indeed the cubic bound suffices).
All rounding and integer-cap effects are counted rather than discarded.

### Decoder and exact source envelope

The nominal logarithm is log2q0=mmax log2(2R+1)=O(L^2), since R<=ceil(n/2)
and mmax<=L+5. For L>=8 it is at most(L+5)(L+1)<=2L^2.
Also L^2<=4sqrt(n) in this range, by its decreasing ratio to2^(L/2),
so L^2=O(R) follows from R>=sqrt(n/2) without a profile asymptotic assumption. Source precision has h_extract=O(log Qcap+L)=O(L^2),
so each collective EXTRACT retains its O(n^2L) core bound: its explicit
O(n h_extract L+n^2L) cost fits because L^2=O(n).

For the odd decoder hmax=Theta(R), log2nq=O(R+L^2), and L^2=O(R)
by R>=sqrt(n/2). Thus K=O(R), Sodd=O(1+n/R), and
H0=Sodd*K+2n=O(n), uniformly over every modulus, including the M=1 skip
and odd-part-limited h. The later2-adic parity tests still have expected
two roots per bit; all these costs are in the actual Qstar and Wstar.

The fixed source cap gives

 Q<=1024(2*3^mmax q0 H0+2n).

For L>=32, 2R+1<=2n/L, so for an absolute constant C this is at most
 C n (6n/L)^mmax+C n.
Let log mean log2 in the next estimate. Since log6<3, mmax<=L+5,
and L-log L+3 is positive for this range,

 log[n(6n/L)^mmax]
 <=L+(L+5)(L-log L+3)
 =L^2-L log L+9L-5log L+15
 <=L^2 for L>=1024.

The last step uses log L>=10. Thus Q=O(2^(L^2)) with EXACT coefficient1
of L^2, not an unspecified constant inside an exponential. The bound
includes all rejected leaves, repeated roots, discarded trees and aborts.
The finite prefix is bounded by explicit guarded parameter formulas and
can be absorbed in one absolute constant. The n<256 exhaustive procedure
is the actual stated finite branch, with its source cost included likewise.
No fractional-noise promise is manufactured from this source envelope.

### Both peak storage bounds

A depth-first tree retains sum_i(r_i-1)+1=B+1<=n phase qubits as siblings
and current outputs. Query, arithmetic and source-extraction scratch add
O(n) reusable qubits. Thus S_Q=O(n), even at aborts. The nominal leaf count
is not materialized. A full signed label needs O(n+log2q0)=O(n) bits;
O(n) retained labels require O(n^2) bits. Even a conservative allocation
of mmax=O(L) budget snapshots of O(R+L^2+L) bits is O(nL+L^3)<=O(n^2).
The profile, compact low-weight rows, descriptor fields, fixed64-member
found list, numeric scratch and K=O(R)<=O(n) decoder records fit O(n^2).
All numerical-label branches use the same bounded representations.
Every indexed classical access and classically addressed gate retains its
full O(log n)=O(L) address debit. There is no exponential table or QRAM.

### Charged time and absorption with a negative correction

In the sufficient range, v_i>=u and R>=sqrt(n/2), so the inherited compact
persistent generator gives O(R^2 sqrt(L)2^v_i) core work per complete
attempt. Its separately counted full-label and setup polynomial is covered
because every v_i=Omega(n/L) eventually. The SAME finite generator/profile
handles the remaining fixed main-branch prefix. Weighted guards then give
all combiner core work O(R^2 sqrt(L)Wcap), with
Wcap=O(n mmax2^R). After full address charges this is bounded by
O(n^3 L^3 2^R), a conservative polynomial-times-exponential internal bound.
No controller, inverse pass, reset or address formation is omitted.

Put E(n)=n/(2L)-n/L^2. The profile certificate gives, for L>=32,

 E(n)-R >= n(L-4)/[L^2(L+4)]-L^2
         >= n/(2L^2)-L^2.

This positive gap eventually dominates every fixed aL+b log2L, because
2^L/L^2 grows faster than every polynomial in L. For completeness,
L^d/2^L tends to zero for each fixed d: its ratio at consecutive integer
L tends to1/2, and fractional parts change a bounded factor. Hence all
polynomial prefactors in the INTERNAL combiner bound are absorbed, giving
T_comb=O(2^E). This is an asymptotic estimate for charged costs already
counted, not a free-operation assumption or a change of algorithm.

All source extraction/acquisition work is at most
O(n^2 L^2 2^(L^2)), also smaller than2^E eventually because E~n/(2L)
and L^2=o(n/L). The actual decoder grids cost poly(n)q0*2^h per stage,
with h<=1+R/32, log2q0=O(L^2) and at most O(n) stages. Their total
is poly(n)2^(R/32+O(L^2)), lower than2^E since R=Theta(n/L) and
L^2=o(R). This counts the enlarged grid and every numerical score and
memory access. Preprocessing, rational precision, caps and cleanup are
polynomial or included in these explicit budgets. Finite main-prefix
exceptions and the n<256 branch enlarge one absolute outside constant;
the guarded finite circuits give a uniform bound independent of N,s and
outcomes within that fixed prefix.

Thus jointly on EVERY execution branch,

 T=O(2^(n/(2L)-n/L^2)), S_C=O(n^2), S_Q=O(n), Q=O(2^(L^2)).

### Exact growth indices

The declared time envelope has log2B_T=n/(2L)-n/L^2
=(n/(2L))(1-2/L). Its iterated logarithm divided by L tends to1.
For copies log2B_Q=L^2, so log2log2B_Q/L=2log2L/L tends to0.
The two polynomial spaces also have index0. Therefore the exact resource
indices are[1,0,0,0], while copies are QUASIPOLYNOMIAL rather than
polynomial. The supported structures contain the two exact rational time
terms and the exact L^2 copy term, with no coefficient guessed from a
heuristic or inner big-O. Only time contributes numeric score[1].

## 10. Error tolerance and limits

The fractional tolerance is epsilon(n)=0 under the exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

All N>=2 and s meet the success and resource guarantees above under this
promise. No positive tolerance or impossibility of greater tolerance is
asserted. The result is a rigorous implementation/accounting tradeoff of
known sieve ideas, not a new exponent breakthrough. Hosted mathematical
acceptance, if obtained, remains fallible review rather than formal proof.
