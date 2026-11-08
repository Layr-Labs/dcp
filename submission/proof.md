# MICRO-L32: deeper block collimation with adaptive microbank protection

## 0. Joint theorem, exact bank configuration and error model

For every N>=2 and secret s moduloN put n=ceil(log2N). The single
MICRO-L32 algorithm below acquires exactly Qbank copies,computed
fromN alone. For every adversary of the error model below,including the
clean case,it recovers the entire secret with unconditional probability
at least2/3. On EVERY branch jointly,with absolute constants,

    T=O(n^19 log2n 2^(n/(32log2n))),
    S_C=O((n^17/log2n)2^(n/(32log2n))),
    S_Q=O(n), Q=O(n^34/log2n),
    epsilon(n)=(log2n)/(400000 n^34).

Logarithmic resource envelopes atn=1 usepositive n=2 values; the tolerance
itself is0 atn=1. Growth indices are1,1,0,0; tolerance is a fraction
among all acquired copies,not a per-copy probability or a count score.

Error model (exact adaptive specification): Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

For n>=2^128 compute exact parameters

    ell=RLOG(n),m=ceil(32ell),u=ceil(log2n),
    kappa=ceil(log2m)+1,s0=kappa+1,
    base=ceil(n/(m+1)-m/2)+1,dl=base+s0,H=base+m-1,
    L=floor(m/(4s0)),lift(k)=min(s0,floor(k*s0/L)),
    lambda_i=base+i+lift(m-1-i) for i<m,lambda_m=1,
    Kc=8192(m+10u+100),Kp=8192(u+100),g_w=ceil(log2dl),
    b0=floor(log2n),Lblk=ceil(n/b0).

The consumed-slot capQcap is defined in13 before access; Qbank=2048*Qcap.
For the main branch each reference source request in3..12 uses a fresh
microbank ofKraw=2048 raw copies: hold core workspace idle while they are
acquired,then draw11 fresh fair bits and select exactlyone uniformly.
Unchosen copies are reset/released. The main core never uses the wrapper's
selection or cleanup outcomes. After the core stops,pad with unused
microbanks until exactlyQcap microbanks have been acquired. Thus actual
Q=Qbank=2048Qcap is fixed byN,including all discarded and padding copies.
For n<2^128 use the whole-bank finite branch in13/18. The probabilistic
claims of3..12 describe the clean reference core;18 proves the adaptive
first-bad-selection coupling. Hard resource guards apply to every state.

RLOG and all arithmetic use the finite rational algorithms in8; no real
oracle is supplied. Notation:dn=floor(log2N),N=2^a2 M withM odd,s1=s modM,
s2 in[0,2^a2) withs=s1+M*s2 moduloN,omega=exp(2pi i/N). Logs are base2.
Labels are known nonnegative integers; data basis states|u> have0<=u<N.

## 1. Provenance and exact change

Direct physical/taper/block-decoder/microbank source: our MICRO-BLOCK-L16,
e49cbf0a-fc0c-41c5-b8fc-49fd4e968439,exact proof SHA-256
07611f5015dd94b02880e41836cd7915e3d9c3bd31ddc900f31f5352613ec866.
Every necessary source/extractor,merge,conditional moment,top-block score,
odd/two-adic decoder and adaptive first-bad proof is reproduced. Historical
bank-first credit to BANK-45L/R24 is retained through that source.
No prior verdict is a premise. The NEW depth isceil(32RLOG(n)),bank size2048
and supported fraction(log2n)/(400000n^34). Rounding,capacity,fields and
all full resource envelopes are independently rederived below.
The lower exponential coefficient1/32 costs more copies and a smaller
tolerance; this is a crossing tradeoff,not a new time-growth index or a
joint dominance claim. No primitive invention,priority,optimum,extra oracle,
QRAM,physical execution or practical-space assertion is claimed.

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

Main source wrapper MICROTAKE. Keep a countera of active/padding
microbanks,initially0. A reference acquisition in3..12 means:
(1) ifa=Qcap,ABORT before requesting any raw copy;
(2) pause every core gate/measurement and acquire exactly2048 raw copies
into distinct(n+1)-qubit registers,without any core/bank quantum operation,private
draw or measurement between deliveries; deterministic address bookkeeping
is allowed and charged;
(3) only after the last delivery,measure11 freshH|0> coins,forming uniform
J in0..2047; SWAP raw registerJ into an empty source working register
with3(n+1) CNOTs on classically known addresses;
(4) reset/release all unchosen registers,and incrementa. Return the chosen
copy to the core. All selection/cleanup outcomes are ignored by the core;
its own decoder coins remain fresh independent coins. The adversary may
see these outcomes before later deliveries,as its model permits.

The local acquisition/demand guards in9 count SELECTED MICROTAKE
deliveries,not the2048 raw acquisitions inside one call. Every raw copy
counts in actualQ. After core success orABORT,record its output,release
the core quantum state,and acquire/reset dummy microbanks untila=Qcap.
Dummy banks return no copy and their measurements never alter the output.
Thus actualQ=2048Qcap on every branch; all padding work/storage are charged.
At mostone microbank is allocated at a time,beside the reused core wires.
LE confidence usesQcap,because at mostQcap selected copies are extracted.

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

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O((log2n)^2) (Section 14),
this is O(n^2(log2n)^2) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL run. Execute this same MICRO-L32 algorithm but replace each LE
output by its latent labelk. Actual and ideal runs can be coupled until
the first incorrect label, whose probability is at most2^-10 by(5.1).
There are no additional ancilla-preparation trials. Every resource bound
is for actual branches, using fixed caps and allocations.

## 6. Phase vectors and the linear merge

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical label table
lab[0..2^lam). In the ideal run its state is 2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a
global phase, for a fixed real th. Labels are nonnegative integers. The vector is COLLIMATED TO p
if all lab[x] are congruent modulo 2^p.

STORAGE. For a vector collimated to p, store one p-bit number
c=lab[0] mod2^p and an array hi[x]=floor(lab[x]/2^p), so
lab[x]=c+2^p hi[x]. The notation lab denotes these logical integers,
not a second materialized array. Each hi entry has its public level
width w_i from9. At p=0,c=0 and hi=lab. For p>0 no full-label
array is written: all operations below use c and hi directly.
The common prefix is known classical data, contributing a common phase;
no unknown rotation or physical phase correction is performed.

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x] into a clean w-bit
register, controlled by a lam-qubit index x. For each row x0 it computes the flag [x = x0] with a
Toffoli chain on O(lam) scratch, applies CNOTs from the flag to the output bits where tab[x0] has a
1, and uncomputes the chain. Indices outside [0,E) give output 0. The circuit is its own inverse,
has O(E (lam + w)) gates and O(lam + w) qubits, and is generated by reading each table bit once.

### 6.1a Stable digit-radix sorting and a merge join

For lam>=1, SORT(key,index) takes E=2^lam records with b-bit nonnegative keys
and lam-bit payload indices, initially in increasing payload order.
Store each record in a row padded to the next power-of-two bit stride;
this changes its size by at most a constant factor. Row/bit addresses
are then concatenations, not uncharged integer multiplications.
Put w_d=lam and B_d=2^w_d=E. The existing classical table
budget permits E counters; no array of size2^b is allocated.
If b=0 output the identity order. Otherwise for digits from least to
most significant, in chunks of w_d bits (pad the final chunk byzero):

- Zero B_d counters of lam+1 bits. Scan the records, extracting their
  current digit and incrementing that bucket's counter by fixed-width
  ripple arithmetic.
- Prefix-sum the counters to get bucket starts, each of lam+1 bits.
- Scan the input records in their current order, copy every bit of the
  record to the output at its bucket's next position, and increment that
  position. Swap the input/output arrays for the next pass.

Every pass is stable. Induction on processed digits gives final order
by(key,index), including repeated keys. A pass costs
O((E+B_d)(lam+b)) core bit steps, including counters, pointers,
prefix sums, digit extraction and every record bit copied. Sequential bit offsets are incremented with amortized linear total
bit updates per record; bucket positions are full lam+1-bit additions.
No word operation is charged as one step. Since B_d=E,

    SORT costs O(E(lam+b)(1+b/w_d)) core steps,
    and O(E(lam+b)+B_d(lam+1)) classical bits.           (6.1a)

All accesses are ordinary classical bit-array accesses, with the model's
address charge paid separately in14. No quantum lookup is added here.

To find partner runs, sort records(bb[y],y) and query records(t_x,x),
where t_x is the required key for x. Merge-scan their equal-key runs.
If a query key is smaller, assign its whole query run count0 and the
current data cursor as its insertion start. If a data key is smaller,
advance its whole data run. If equal, compute the data run's start and
length once and write them for every x in that query run. When the data
end, give remaining queries start=E,count=0. Each run/record is scanned
once, costing O(E(lam+b)) steps and linear record storage. The result
for each x is exactly its contiguous matching run in sorted data.

### 6.2 MERGE(X1, X2; p, b, lam'), for b >= 0

Precondition: X1 and X2 are phase vectors from disjoint sets of qubits, both of length 2^lam,
collimated to p, with index registers x,y. Their stored records are
(cA,hA),(cB,hB), with logical labels al[x]=cA+2^p hA[x],
be[y]=cB+2^p hB[y], 0<=cA,cB<2^p. Put
car=floor((cA+cB)/2^p),aa[x]=hA[x] mod2^b,bb[y]=hB[y] mod2^b.
These are computed directly from the stored fields. Bits p..p+b-1
of the logical sum equal(aa[x]+bb[y]+car) mod2^b. If b=0,
the residue registers are empty and e=0.

1. LOOKUP aa into a fresh b-bit register Ru and bb into Rv. Add Ru + Rv + car (mod 2^b) cleanly into
   a fresh Rz, and clear Ru and Rv by repeating both lookups. Measure Rz, obtaining e, and reset Rz.
2. Classical. Let S_e = {(x,y) : aa[x] + bb[y] + car = e mod 2^b} and sz = |S_e|.
   Use6.1a to sort records(bb[y],y), obtaining order[]; pos[y] is y's sorted position.
   Form t_x=(e-car-aa[x]) mod2^b. Sort records(t_x,x), then merge-join the query
   and data key runs as specified in6.1a. Write each matching run start lo[x] and
   length cnt[x], using insertion start/count0 for an absent class.
   Put off[x]=sum_(x'<x)cnt[x'] in increasing original x order, and
   rank(x,y)=off[x]+pos[y]-lo[x], a bijection from S_e onto[0,sz).
   If sz<2^lam', declare FAIL. Stable data sorting gives precisely the order
   (bb[y],y); therefore all counts and ranks on S_e and the subsequent instrument
   agree with the comparison-sort definition. Empty runs use their insertion start.

3. Let R have 2 lam + 1 bits. LOOKUP pos into Rp and Dx[x] = (off[x] - lo[x]) mod 2^(2lam+1) into Rd.
   Add Rp + Rd (mod 2^(2lam+1)) cleanly into a fresh R, and clear Rp and Rd by repeating the lookups.
   On S_e, R = rank(x,y).
4. Measure bl = floor(R / 2^lam'). If (bl+1) 2^lam' > sz, declare FAIL.
5. Classical. Produce all pairs (x_v,y_v),v=0..2^lam'-1 jointly. Scan original x in increasing
   order with off/cnt while the target rank bl*2^lam'+v increases. Advance past each empty or
   completed x interval once; for its containing interval put y_v=order[lo[x_v]+target-off[x_v]].
   This is one shared scan, not a full scan for each output row. Apply LOOKUP v->(x_v,y_v) on
   the low lam' bits of R, XORing into x,y, which become|0>. Reset R's high bits from known bl.
6. Output R's low lam' bits. Its logical labels are al[x_v]+be[y_v], but store
   only the shared prefix and high parts: for each selected row put
   sv=hA[x_v]+hB[y_v]+car and hi'[v]=floor(sv/2^b), and once put
   c'=((cA+cB) mod2^p)+2^p e. Then 0<=c'<2^(p+b) and

       c'+2^(p+b)hi'[v]=al[x_v]+be[y_v].

   The shared prefix is written once, not once per output row. No full
   logical label array is formed. An input high field of w_i bits needs
   w_i+1 temporary bits for sv and w_(i+1)=w_i+1-b bits for output.

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

Cost. Write E=2^lam,E'=2^lam'. In this configuration
lam=Theta((n/log2n)),0<=b<=2lam and w_d=lam.
There are at most two stable digit passes. Equation6.1a and the
merge join cost O(E(lam+b))=O((n/log2n)E) core steps.
The E counters each have lam+1 bits, so the bucket arrays occupy
O(E lam) bits, absorbed by O(nE) since lam=O(n). All explicit quantum lookups have
O((n/log2n)) gates per row; ranks and the inverse lists use O((n/log2n))-bit
fields. Each high field is at most3n bits (9). High-part preprocessing and
selected-output arithmetic cost O(n(E+E')) steps; the prefix/carry
update costs O(n) once per merge. No repeated full prefixes are expanded.
Thus total work remains O(n(E+E')) core steps and quantum scratch
O((n/log2n))<=O(n). The actual classical arrays use their high-field widths
and O(lam+b)-bit indices/keys, counted precisely in14; the coarse
O(n(E+E')) storage upper bound is not used for the final space claim.
Every digit, counter bit, pointer, record copy and table initialization
is included. There is no free word sort or quantum-addressed memory.

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
scratch, and K=O((log n)²) root qubits. Section14 gives its uniform size bound.
A classically addressed free-handle stack or equivalent known recursive
wire layout permits reuse with O(n)-bit bookkeeping per allocation, within
the charged ledger. No exponential register bank is allocated. Classical
tables are looked up by the explicit Section6 scan circuits, not QRAM.

## 8. Exact logarithmic depth and tapered capacity

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
oracle is supplied. In the main range1<=ell=RLOG(n)<=log2n.

For n>=2^128 let l=log2n in analysis,ell=RLOG(n),m=ceil(32ell),
kappa=ceil(log2m)+1,s0=kappa+1,base=ceil(n/(m+1)-m/2)+1,
dl=base+s0,H=base+m-1,L=floor(m/(4s0)). Exact arithmetic gives

    32l-1<m<=32l+1,m+1>32l,m>=10u+100,
    kappa<=log2l+8,s0<=log2l+9,m>=8s0².             (8.0a)

At l=128,32l-1>8(log2l+9)²; its linear-to-squared-log ratio increases.
Also m²+kappa<=n,m<=n/4 by endpoint exponential/polynomial comparison.
Put t=n/(32l). We have t>=16(32l+1),t>=16(kappa+3) at128 with
increasing exponential/polynomial ratios. Therefore

    base>=t/(1+2/(32l))-(32l+1)/2>=t/2>=s0>=4,
    dl<=2base,g_w+1<=base,m+g_w<=H,
    H<=n/(m+1)+m/2+1<=2t,
    (m+1)H<=(32l+2)2t<=4n.                         (8.4)

Hence dl,H=Theta(n/l),m=Theta(l),L>=2s0,L<=m-1.
The fixed finite range is handled separately; no main guard applies there.

For k>=0 let lift(k)=min(s0,floor(k*s0/L)). Since L>=2s0 it has
increments0 or1 and lift(k)<=k/2. Therefore the actual input widths
lambda_i=base+i+lift(m-1-i) grow by0 or1, start atdl, end atH, and

    lambda_i<=H-ceil(k/2),k=m-1-i.                  (8.5)

Every nonroot capacity2lambda_i-lambda_(i+1)-kappa is at leastbase>0;
the root capacity2H-1-kappa is positive. Put

    B0=(m+1)base+m(m-1)/2-1,
    A=sum_(k=0)^(L-1)(s0-floor(k*s0/L))<=s0L<=m/4.

The sum of uplifts is m*s0-A. Exact root/nonroot telescoping gives

    Sum=2lambda_0+sum_(1<=i<m)lambda_i-1-m*kappa
       =B0+m+s0-A.                                (8.2)

Since base>=n/(m+1)-m/2+1, we have B0>=n, soSum>=n+3m/4+s0>=n.
For B<=n greedily allocate b_i root-down under these maxima, setting
 tp_0=0,tp_(i+1)=tp_i+b_i,tp_m=B. All residue reads lie belowB and
b_i+lambda_(i+1)-2lambda_i<=-kappa. Each binary attempt fails with
probability at most2^-kappa conditional on ENTIRE built inputs/history,
including partial and zero windows.

Put Kc=8192(m+10u+100),Kp=8192(u+100),
Dcap=8dl2^m(Kc+u+16),Ccap=4Dcap,Y=ceil(log2Ccap).
By8.0a Kc<=2^14m,Kc*dl<=2^16n,and therefore

    Ccap<=64Kc dl2^m<=2^22n2^m,
    Y<=m+u+23<=n/2,
    Kc/8192=m+10u+100>=Y+u+30.                      (8.1)

Here m<=n/4,u+23<=n/4 hold at128 and thereafter. All dimensions and
caps precede access; concentration and field sizes are not circular.

For block fields put b0=floor(log2n),Lblk=ceil(n/b0).
We havebase>=4u,base>=32 at the stated main cutoff and thereafter:
base>=t/2 and the exponential-to-logarithmic ratio increases.
Since dl<=2base,g_w<=ceil(log2(2base))<=base/4,b0<=u<=base/4.
Thusm+g_w+b0<=m+base/2<=H. AlsoY>=m>=b0.                  (8.6)

## 9. BATCH(supplier, B, R, h=1)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+h)). Here1<=h<=b0 and1<=B,B+h<=n. Output: R roots, or ABORT. Here 1<=R<=Kc is a requested root count. Compute D_R=8dl2^m(R+u+16), C_R=4D_R before access. A batch starts with a zeroed counter of
source acquisitions; if an acquisition would exceed C_R, the batch ABORTs. Also initialize delivered counter D=0. Before acquisition compute D_src=B+h, the budget tp_i and all w_i. At its end, unused tree/index scratch and high-part tables are reset or released; the next batch reuses the frame pool.

Each frame allocates its actual2^lambda_i rows and actual output length,
not2^H rows at every level. Changing the index widths does not change the
canonical source footprint: a level-i logical label is still the sum of at
mostdl2^i accepted source labels. Therefore the exact high-part field and
carry formulas below apply with these actual row counts as well.

TREE. VEC(0) = LEAF: for each of dl wires, first check D<D_R; otherwise ABORT before calling NEXT. Request the next accepted qubit by NEXT(0), then increment D. Thus D never exceeds D_R. These qubits form
the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j.
At p=0 write only this hi table, of width w_0=D_src+g_w per row; c=0. The logical
table has length 2^dl, is exactly the tensor product state in the ideal run, and is collimated to tp_0=0.
VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until out != FAIL; return out. A root is VEC(m),
evaluated depth-first. Run it R times.

Field widths. Put D_src=B+h and g_w=ceil(log2dl). A level-i logical
label is a sum of at most dl2^i source labels below2^D_src, by disjoint
canonical footprints. It is below2^(D_src+i+g_w). Thus store its high parts
in exactly

    w_i=D_src+i+g_w-tp_i >=1

bits per row, and one tp_i-bit common prefix. These dimensions are fixed
before acquisitions. At a merge w_(i+1)=w_i+1-b_i, so the w_i+1-bit
sum sv fits and its right shift fits the output field without truncation.
The same integer bound holds on actual wrong-label branches: accepted
stored source values still lie in[0,2^D_src), and the logical sum invariant
is maintained exactly. No high-value overflow check or abort is needed.

Root. At p=B the stored pair is(c,hi[0],hi[1]). Compute

    W=hi[1]-hi[0]=(lab[1]-lab[0])/2^B.

The common prefix cancels; no full labels need reconstruction. Its ideal
state is, up to global phase,

    (|0>+exp(2 pi i 2^B W th)|1>)/sqrt2.                (9.1)

The earlier global bound remains true for logical values: each is a sum
of at most C_R source labels below2^(B+h), hence is below2^(Y+n+1).
Only the high fields and one prefix are stored. Since
2^(m+g_w)<2dl2^m<=C_R, we have m+g_w<=Y. Thus
w_i<=D_src+m+g_w<=n+Y<=3n on the main range. In particular

    |W|<=2^h C_R<=2^h Ccap<=2^(Y+h),                              (9.2)

Coarse decoding usesh=1; block decoding usesh=b. No root-cost bound depends onh.

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a
batch ABORTs with probability at most 2^-12/n + 2^-11/n.

Proof. Work in the ideal run and put p=2^-kappa<=1/(2m),
so p<=1/10 on the main range. Lemma6.1 bounds the failure probability
of every merge by p CONDITIONAL ON ITS ENTIRE BUILT INPUTS AND HISTORY.
This property is stronger than an unconditional small failure rate.

Analytical domination. After each pair of child constructions, let q<=p
be the actual conditional failure probability of that attempt. Its outcome
can be represented in the probability analysis using a fresh independent
uniform U: failure iff U<=q, with additional independent randomness
choosing the particular outcome conditional on failure/success. The event
U<=p dominates actual failure and is independent of the just-built child
costs. This is an analytical coupling, not an extra computational oracle
or a change of the quantum circuit. If the actual attempt succeeds while
U<=p, add ghost attempts in the upper process. Use independent coins at
all potential call-tree nodes. Induction on height then dominates actual
delivered demand by the following independent upper process:

    Z_0=dl,
    Z_i=sum_(j=1)^G (Z_(i-1,j,1)+Z_(i-1,j,2)),
    Pr(G=g)=(1-p)p^(g-1),g>=1,

where all child Z copies and each G are independent. The parent coin is
fresh after child construction; no independence of actual cost and actual
failure is asserted. Since U>p forces actual success, the actual number of parent attempts
is at most the first index with U>p. That index uses only parent coins
and is independent of every upper child cost. This domination is uniform conditional on all history
before the root call. Fixed depth and finite geometric G also establish
almost-sure finiteness of the uncapped process used only for this analysis.

Exponential moment. Define M_i(s)=E exp(s Z_i/(2^i dl)) and
y_i(s)=ln M_i(s). For0<=s<=1/8, y_0(s)=s. Put
c_i=(1+2p)^i<=exp(2*p*i)<=e<3 for i<=m. With
a=2y_(i-1)(s/2), the geometric sum gives

    y_i(s)=f_p(a),
    f_p(a)=a+ln(1-p)-ln(1-p exp(a)).

Inductively a<=c_(i-1)s<=3/8<1/2. On0<=a<=1/2,
exp(a)<5/3 and p<=1/10 imply

    f'_p(a)=1/(1-p exp(a))<=1/(1-5p/3)<=1+2p.

The last inequality follows from p/3-10p²/3>=0. Since f_p(0)=0,
y_i(s)<=c_i s. Denominators are positive throughout, so every moment
used exists. In particular an actual root has, conditional on its prior
history, E exp(D_root/(8*2^m dl))<=exp(3/8).
For R roots the tower property therefore gives

    E exp(D_inf/(8*2^m dl))<=exp(3R/8).

Independence of actual root costs is unnecessary. Markov applied to this
exponential moment, with the stated D_R, yields

    Pr(D_inf>D_R)<=exp(-5R/8-u-16)
                    <=2^(-u-16)<=2^-16/n.             (9.3)

Acquisitions. In the ideal supplier each potential acquisition produces
an accepted qubit with conditional probability at least1/2. Extend its
potential acceptance indicators after any stopping time as needed for the
analysis. If A is their sum over C_R=4D_R acquisitions, iterated
conditional expectation gives E[3^-A]<=(2/3)^C_R. A source-cap abort
before demand abort/completion entails A<=D_R. Hence

    Pr(source-cap abort before demand abort)
       <=3^D_R(2/3)^(4D_R)=(16/27)^D_R
       <=2^(-D_R/2)<=2^(-u-12)<=2^-12/n.             (9.4)

Here(16/27)^2<1/2 and D_R>=2(u+12). The actual capped run agrees
with the uncapped process until a cap triggers. Equations9.3/9.4 are
stronger than the lemma's stated2^-12/n+2^-11/n bound. These are
probability estimates for success only; every actual branch, including
wrong-label branches, obeys the deterministic caps directly. QED.

## 10. Unused-top-block independence and score discrimination

ForBATCH(B,R,h),write each accepted labelk_v=low_v+2^B tau_v,
0<=low_v<2^B,tau_v uniform inZ/2^h. LetG include all low_v,all merge
outcomes(e,bl),FAIL/retry/abort/qubit assignments and controller selection
history,but exclude root measurements,their fresh basis coins,unusedtau_v,
and LE internal coins/outcomes,which feed no ideal selection decision.
It is a coarse sigma-field,not the full computer record. Rejected source
history is independent of the subsequent uniform accepted value; every
fixed preceding rejected sequence has equal probability before each value
in its accepted interval. Direct modular suppliers are already uniform.

Every residue,sort,rank and block partition inspects only logical positions
belowB. Bits belowB of a sum depend only onlow_v. Stored prefixes and
exposed residue windows end belowB. Lemma6.1 makes the conditional law
of merge outcomes a function of these low bits and earlier outcomes only.
Induction factorizes the joint law as

    law(tau) law(low) law(outcomes,controller | low).

Thus conditional onG and randomness outside the batch,thetau_v remain
independent uniformZ/2^h. A table entry is the sum of leaves with a0/1
incidence vector. Distinct indices have distinct vectors: it holds for a
leaf(0,k_v),LEAF concatenates disjoint coordinates,and MERGE injectively
reindexes pairs on disjoint coordinates. The two root entries therefore
have different incidence vectors,so

    W=cst+sum_(v inSp)tau_v-sum_(v inSm)tau_v,       (10.1)

with disjointG-measurable sets,nonempty union,and integralG-measurablecst.
Every nonzero coefficient is+1 or-1. Holding all but one suchtau fixed
proves W mod2^h is uniform. Leaves of distinct roots are disjoint,so the
root frequencies are independent conditional onG. Forh=1 this also gives

    |E exp(2pi i phi W)|=|cos(pi phi)|^hd<=|cos(pi phi)|,
    Pr(W odd |G)=1/2,                              (10.2),(10.3)

wherehd=|Sp|+|Sm|>=1,as used by the unchanged coarse bootstrap.

Block score lemma. Letb=h or let a direct supplier give uniformW mod2^b.
Suppose independent roots have physical phase

    2pi J W v/2^b+eta, J odd, |eta|<1/16,

wherev is the desired residue. Independently for each root choose a fair
basisbeta in{0,1},measureX orY,obtainZ in{+1,-1}. Y isS^dagger thenH
then computational measurement. For everya in[0,2^b),compute

    S(a)=sum_roots Z*tab_beta((J W a mod2^b)/2^b),   (10.4)

using Section4's fixed rational table. Choose the smallest maximizinga.
All scores are exact rational sums of known table entries. In noiseless
exact-trig scoring the mean true score is1/2,and the mean false score is
(1/2)E cos(2pi JW(v-a)/2^b)=0,by uniformW and oddJ. The angle perturbation
changes each expectation by at most1/16; table error adds at most1/625.
Thus true-minus-false expected score exceeds1/4. Each table value has
absolute value<=1+1/625,so each score difference lies in[-3,3]. Independent
root scores obey Hoeffding:

    Pr(S(a)>=S(v) |completedG)<=exp(-Kp/288).

Here the interval width6 gives exp(-2Kp*(1/4)^2/36). Union over at most
2^b<=n false candidates yields n exp(-Kp/288)<=2^-30/n,using
Kp=8192(u+100),u>=log2n. This includes harmful ties. Phase perturbations
may depend onW; the uniform error bound suffices and no independence of
eta andW is asserted. Conditional completedG retains all unused top labels;
therefore integration bounds wrong-block AND completion. Aborts are charged
separately. Direct independent qubits satisfy the same argument.           (10.5)

## 11. Odd part: bootstrap followed by signed near-parity

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every coarse stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (m + 10u + 100), u=ceil(log2n).                                              (11.0)

Put J_full=min{j>=0:2^(j+3)>2M} and J0=min(J_full,Y+5).
Run the following coarse stages j=0,...,J0, each with Kc roots.
There are at most Y+6 stages, and at most log2 M stages.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. To supply one leaf qubit, repeat until accepted: acquire a fresh
copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard), and on acceptance apply X to the
control. The batch's acquisition cap applies. In the ideal run accepted labels are i.i.d. uniform on [0, 2^dn), and each copy
is accepted with probability 2^dn/N > 1/2. The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(dn-1) W th = W 2^(dn-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),           (11.1)

so a root is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known frequency f = 2^j W.

Measurement. Run BATCH(supplier,dn-1,Kc) for stage j. For each root i = 1..K obtain a fair bit beta_i by measuring H|0>, and measure the
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

The hypothesis for stage j+1 is the conclusion of stage j. There are at
most n stages, so all coarse conclusions hold except with probability
2^-20 (apart from batch aborts counted separately). If J0=J_full,
round M z_J0 to the nearest integer modulo M, obtaining s1 as before,
and skip the fine stages. The error is strictly below1/(2M).

Otherwise J_full>Y+5. Since j=Y+5 does not satisfy the defining strict
inequality, M>=2^(Y+7). Put the known integer

    chat=floor(M z_J0+1/2) mod M,
    R0=M2^(-Y-8)+1/2.

On correct coarse conclusions the circular error of z_J0 is at most
2^(-Y-8). Therefore a unique signed lift t0 congruent to s1-chat
modulo M satisfies |t0|<=R0. Also R0>=1, R0/M<=2^(-Y-7)<1/2.
Indeed rounding adds at most1/2, and M>=2^(Y+7) bounds that term
by M2^(-Y-8). This is a mathematical bound, not a measurement of t0.
It also proves |t0|<M/2, including rounding and circular wraparound.

Fine blocks. Initialize low=0,j=0. Whilej<n putb=min(b0,n-j),B=dn-b.
The large-M branch has M>=2^(Y+7),dn-a2=floor(log2M)>=Y+7 andY>=m>=b0,
so B>=a2+1. Compute gamma=2^(B-a2) modM and K0=(-2^b)^(-1) modM
as the representative in[1,M). Both are units becauseM is odd. Define

    J=(2^b K0+1)/M.

This is an integer,1<=J<=2^b,andJ is odd because its numerator andM
are odd. Compute by extended Euclid and CRT a unitalpha moduloN with
alpha=1 mod2^a2 and gamma*alpha=K0*2^(-j) modM.
Setcj=(chat+low) modM. On each fresh copy applyShift_cj thenMult_alpha,
runLE,accept iffk<2^dn,and applyX to the control. Accepted labels are
uniform on[0,2^dn)=[0,2^(B+b)),acceptance>1/2; every rejection counts.
RunBATCH(supplier,B,Kp,h=b). On a correct past,t_j=(t0-low)/2^j is integral.
The exact transformed root phase is

    exp(2pi i 2^B W alpha(s-cj)/N)
      =exp(2pi i K0 Wt_j/M)
      =exp(2pi i J Wt_j/2^b) exp(-2pi i Wt_j/(2^b M)). (11.2)

The unknown two-adic component cancels sinceB>=a2; equality uses the
CRT relation and s-cj=2^j t_j modM. The final small phase is a physical
consequence of modular source transforms,not a synthesized rotation.
Measure and score by10.4 with thisJ,b; let the chosen residuebea.
Updatelow+=a2^j,j+=b. These rules also specify every incorrect history.

On a correct past |t_j|<=R0. The invariant follows fromR0>=1 and
|(t_j-(t_j mod2^b))/2^b|<=(|t_j|+2^b-1)/2^b<=R0,includingnegativeintegers.
By9.2,|W|<=2^(Y+b),so the phase perturbation in11.2 has magnitude at most

    2pi 2^Y R0/M<=2pi/128<1/16,

usingpi<4 andR0/M<=2^(-Y-7). Lemma10.5 bounds each wrong completed
block by2^-30/n. After at mostLblk=ceil(n/b0) correct blocks,low=t0 mod2^n.
Recover the signed n-bit integer t=low iflow<2^(n-1),otherwise low-2^n.
Since|t0|<M/2<=2^(n-1),this equals t0. Output s1=(chat+t) modM.
Coarse failure,extraction errors and aborts retain their separate budgets.

## 12. Two-adic part by blocks

Ifa2=0 puts2=0. Otherwise initializeg=0,s2low=0. Whileg<a2,
putwd=a2-g,b=min(b0,wd),sh=(s1+M*s2low) modN. On a correct past
rem=(s2-s2low)/2^g is integral modulo2^wd. A supplier acquires a copy,
appliesShift_sh,runsLE,appliesX,and useslabelkk=k mod2^wd. Ideallykk
is uniform on[0,2^wd) because2^wd dividesN,and its phase is
exp(2pi i kk rem/2^wd). No rejection is needed.

Ifwd>b runBATCH(supplier,B=wd-b,Kp,h=b); its root has phase
exp(2pi i Wrem/2^b),andW mod2^b is uniform by10. Ifwd=b useKp direct
supplier qubits,withW=kk and the same phase; no depth-zero tree is invoked.
Apply10.4 withJ=1 to choosea,and updates2low+=a2^g,g+=b. Release allroots.
There are at mostLblk blocks and at mostone direct batch. Conditional on
correctpast,s1 and ideal extraction,the phase error iszero,so10.5 bounds
each wrong block by2^-30/n. Allcorrectblocks yield s2low=s2 in[0,2^a2).
Output(s1+M*s2low) modN. Rules,sourcecaps and exact modular computations
remain defined on incorrecthistories and their resources are still bounded.

## 13. Actual complete algorithm and reference-core error budget

Finite branch(n<2^128). Putk=n+10,Qcap=N*k,Qbank=2048*Qcap. Prefetch and
shuffle as18. For EVERY candidatec=0..N-1,use its predetermined block ofk
consecutive bank slots,applyShift_c,measure the control inX,and record
whether all outcomes wereplus. Test every block in full; no early stop,
skipped candidate or adaptively shifted block boundary is used. Output the
first candidate whose block was allplus,or0 ifnone. Unused bank slots are
reset/released without conditioning the output on their measurements.
Section18 proves robustness of this branch uniformly,not a clean-only premise.

Main branch(n>=2^128). Compute all parameters,a2,M,dn,J_full,
Dcap,Ccap,Y before access,withD_R,C_R from9. Put

    Cp=32dl2^m(Kp+u+16),
    Qcap=(Y+6)Ccap+2Lblk*Cp+Kp,Qbank=2048*Qcap.

SizeLE confidence withQcap,initialize the wrapper counter,and run11 then12
with MICROTAKE in place of reference acquisitions. On success orABORT,
record the output(0 forABORT),release the core quantum system,finish
the required dummy microbanks,and only then return the recorded output. There are at mostY+6 coarse batches,
Lblk odd blocks,Lblk two-adic blocks and at mostone direct final block.
Thus at mostQcap selected deliveries occur on EVERY branch; there are at most3n
batches. All CRT constants use ordinary polynomial-time integer routines.
Every unchosen microbank copy is counted inQbank and reset/released
within its call. Padding copies are also counted and cannot alter output.

Reference-core analysis. In the analytical reference program,each source
request receives a fresh independent idealrho_s and wrapper outcomes are
ignored by the core. Lemma9.1 and9.3/9.4 give abort probability at most
(2^-16+2^-12)/n per batch. Over3n it is at most3(2^-16+2^-12).
Addcoarse2^-20,all odd/two-adic wrong blocks2^-29,and globalLE2^-10.
The sum is below2^-8. Union on the first error gives the clean reference
full-secret guarantee. Section18 compares the actual adaptive process to
this reference by first bad selection; conditioning on all selected copies
being clean is NOT assumed to preserve the unconditional reference law.

## 14. Resource bounds on every branch

Every counter, array and retry is capped. With l=log2n, Section8 gives
m,Kc,Kp,Y+6=Theta(l),dl,H=Theta(n/l),Ccap,Cf=O(n2^m).
All coarse batches cost O(nl2^m) acquisitions and all fine/two-adic
batches cost O((n²/l)2^m), which dominates. Hence, on every branch,

    consumed_slots<=Qcap=O((n²/l)2^m).                              (14.0)

There are at mostLblk=O(n/log2n) fine blocks per part,each with
Kp=Theta(log2n) roots; the old bit-stage logarithm is therefore absent
from the displayed aggregate bound,while the per-batch Cf is unchanged.

The sum of delivered-demand caps has the same envelope, including all
rejections, failures, discards and aborts.

Quantum workspace. At mosttwo retained core indices per level,each<=H,
useO(n) qubits by8.4. Leaf,source/data,modular/LE,lookup/controller scratch
andKc roots addO(n),with wires reset/reused. Each MICROTAKE holds only
2048 raw(n+1)-qubit copies and11 coin qubits(also reusable). Hence the main
total peak isO(n),including EVERY microbank register and core wire.
The finite whole-bank branch is explicitly handled by uniform outer
constants in15/18; no main-only space bound is asserted there.

Classical space. Put k=m-1-i. Remaining precision satisfies
R_i=B-tp_i<= (m-i+1)H=(k+2)H since each nonroot capacity is belowH
and the root below2H. Thus actual high fields obey
w_i=R_i+h+i+g_w<=(k+3)H, usingm+g_w+b0<=H. Radix buckets, records,
ranks/orders and inverse maps need O(H) bits per row. Output length
is at most2E_i with field at mostw_i+1. Equation8.5 gives

    E_i=2^lambda_i<=2^H*2^(-ceil(k/2)).

Every retained sibling, field, output and scratch frame is bounded by a
constant times

    H2^H sum_(k>=0)(k+4)2^(-ceil(k/2))=19H2^H.

The sum follows by pairing k=2j-1,2j and using sum2^-j=1,
sumj2^-j=2 for j>=1. No n-dependent plateau is hidden in a constant.
Prefixes, small roots, source/LE, controller, decoder and parameter records
add polynomial space absorbed by H2^H. Hence S_C=O(H2^H), without
any storage or lookup oracle.

Work. A leaf costs O(n2^dl) core steps and consumesdl delivered qubits.
At heighti a merge attempt consumes2^(i+1)dl canonical delivered qubits
not reused by another attempt there and costs O(n2^(dl+i+1)). A partial
leaf at abort is charged fully. All levels cost O(nD_R2^dl(m+1)/dl)
per batch, with(m+1)/dl=O(l²/n). Summing14.0 gives
O(n²l2^(m+dl)) core tree steps; address width O(H+logn)=O(n/l)
gives the complete tree bound

    T_tree=O(n³2^(m+dl)).                          (14.1)

Confidence has logQcap=O(l). Source/extraction costs O(n²l) core per
acquisition, and all charged source/extraction work is O(n^5 2^m).
Coarse scoring across O(l) stages costs O(Kc*n*2^Y*l)=O(n²l²2^m)
core steps. Fine votes, parity, CRT/signed updates, gates, resets,
parameter computation and source charges(n+1)Q count as well. All
polynomial terms with exponentm are absorbed by14.1 since dl=Theta(n/l)
grows faster than log n. Initializing all compressed frames over3n batches
costs O(nH²2^H), bounded by14.1 usingH<=2n/(32l),H=m+dl-s0-1.
Thus14.1 counts every branch, even after earlier errors.

Wrapper overhead. Actual fresh acquisitions equal2048Qcap=O(n^34/l).
Acquisition,selection,routing,reset and padding useO(nQcap) additional core
steps up to fixed factors,and polynomial classical bookkeeping. Address
width isO(H+logQcap)=O(n/l),so all this charged polynomial work is absorbed
by n^19 l2^(n/(32l)); classical wrapper records are absorbed by the declared
exponential classical envelope. Idle core wires are counted throughout
prefetch. Uniform selection uses exactly11 bits,no rejection loop.
All branch bounds hold even after bad states or incorrect labels destroy
the probabilistic reference-core statements. No source/bank operation is free.

## 15. Exact uniform envelopes and indices

Let l=log2n. Since m+1>32l,m<=32l+1,kappa<=log2l+8,

    H<=n/(32l)+m/2+1<=n/(32l)+16l+2,
    m+dl=H+kappa+2<=n/(32l)+16l+log2l+12,
    m<=32l+1.

Insert into14 withH=O(n/l). Factor2^(16l)=n^16 and2^(log2l)=l.
Every ceiling/slack power is explicit in the complete joint guarantees

    T=O(n^19log2n 2^(n/(32log2n))),
    S_C=O((n^17/log2n)2^(n/(32log2n))),
    S_Q=O(n),Q=O(n^34/log2n).

Time/classical indices are1;copy and quantum indices0.
The fixed finite branch and positiven=2 convention atn=1 affect only
uniform absolute outer constants,not any success guarantee.

For clarity,the finite branch quantum allocation is at most
2048N(n+10)(n+1)+O(n) circuit scratch. With fixedC0=2^128 andn<C0,
this is bounded by a fixed absolute constant timesn,for example by
C_f*n with C_f=2^20*2^C0*(C0+100)^2. The same finite-range argument
covers its work,copies and classical storage. This constant can be enormous;
the theorem is an asymptotic uniform bound,not a practical-space claim.
The finite SUCCESS guarantee still requires and receives its separate
positive-fraction proof in18; it is not absorbed into an outer constant.

## 16. Guaranteed malformed fraction

The exact guaranteed fraction is epsilon(n)=(log2n)/(400000 n^34),including
epsilon(1)=0,under the full adaptive error model in0. Forn>=2,log2n<=n
shows0<epsilon(n)<1. Section18 proves
whole-secret recovery>=2/3 jointly with all four worst-case envelopes.
It is not a per-copy corruption probability,an expected count,or a claim
of optimal robustness. The guaranteed budget permits at least20 malformed
copies at every main-branch input size,as quantified below. No growing
malformed-count guarantee is claimed for the asymptotic main branch.

## 17. Scope

This algorithm trades time/classical growth index1 for polynomial copies
and linear main quantum workspace with constant-size microbanks and a nonzero
supported fraction,with the finite-range uniform constants just described.
It does not claim a better time index than1/2,small outside constants,an optimum,
practical runtime or physical quantum execution. Constants and the finite
cutoff can be large. All branch and error statements refer to this one
banked configuration.

## 18. Conditional microbanks, first-bad coupling and finite-bank proof

Finite-bank lemma. In the finite branch,before the last delivery the algorithm makes no
measurement,private draw,source transform or abort decision. Record each
adversary clean/malformed decision in an analytical hidden classical
register. Inductively,conditional on the decision trajectory,the delivered
operator factors as a tensor product ofrho_s on its clean slots with a
positive operator on all malformed slots and the adversary system.
A private adversary instrument acts only on the latter; a malformed
delivery transfers part of that operator,and a clean delivery appends a
fresh productrho_s by the model. Countably many private outcomes preserve
this form upon summation. After acquisition,trace out the adversary and
condition on the flags: the input is a mixture over fixedBad sets with
|Bad|<=floor(epsilon Qbank),independent ideal factors on all other slots,
and an arbitrary joint malformed state. Prove bounds for each such component
and integrate. This reproduces the cited bank-first argument; it assumes
no independence among malformed copies. Later local processing of the
adversary cannot signal into the algorithm or change its marginal output.

Finite shuffle. Setz=ceil(log2Qbank),ell_s=2z+u+100. Fori=Qbank-1 down1,
generate exactlyell_s fresh fairH-measurement bits after acquisition,
form integerR,putj=R mod(i+1),and swap whole bank registersi,j.
Modulo uses finite ordinary bit arithmetic. Each swap costs3(n+1) CNOTs;
all addressed gates,coin gates/measurements,resets and integer operations
are charged. No rejection loop or quantum memory oracle is supplied.
For anm-element range,the modulo distribution of a uniformell_s-bit
integer is within TV m/2^ell_s of uniform. Couple each step to an ideal
uniform Fisher-Yates step; the total permutation TV is at most

    delta<=Qbank²/2^ell_s<=2^(-u-100).

The ideal order is uniform independent of the bank. Every subsequent
quantum/classical computation contracts this classical TV distance,so
delta is added ONCE to any total failure event. The new coins are drawn
only after all copies arrive; they cannot affect any adversarial source
decision. No later fresh acquisition occurs. Only the finite branch uses this whole-bank shuffle; all its dimensions
are finite with charged outside constants. The main branch instead uses
exact11-bit microbank selection. Every loop has a fixed finite bound.

Main cap and fraction. Letl=log2n>=128. We have
u<=l+1,m<=33l,Kc<=2^14*33l,Y+6<=34l.
Also dl<=n/(32l):use dl<=n/(m+1)-m/2+s0+2 and
m/2>=s0+2,which follows from16l-1/2>=log2l+11.
The fixedKp+u+16<=8193l+827409<14700l and2^m<=2n^32 imply
Cp<=29400n^33<=58800n^33. As beforeb0>=127l/128,n>=256l yield
Lblk<=(65/64)n/l. RetainCcap<=2^22n^33. Because
n>=34*2^22*l² at128 and its ratio increases,

    (Y+6)Ccap<=n^34/l,
    2LblkCp<=119438n^34/l,Kp<=n^34/l,
    Qcap<=2^17 n^34/l.                             (18.1)

All are explicit weakened upper bounds. With epsilon=l/(400000n^34),
epsilon Qcap<=2^17/400000.

Main conditional-bank lemma. Before each active microbank,hold all core
quantum wires idle. Condition analytically on the full classical past and
on no earlier selected copy being malformed. At the start,core workspace
and adversary/unused-malformed systems factor conditional on that past.
This holds initially. For the induction,all previously returned copies
were clean products; core operations act only on that product workspace.
Unchosen malformed registers are acted on only by the wrapper's local
reset/release operations. Conditional on their public outcomes these
local operations preserve the tensor factorization. Public outcomes may
influence future adversarial decisions,but do not entangle the two factors.

During the next2048 deliveries the algorithm performs no core/bank quantum operation or measurement; deterministic
address bookkeeping is allowed and charged. Recording
the hidden clean/malformed flags gives,as in the finite-bank lemma,a
mixture of fixed currentBad sets,ideal productrho_s on the other registers,
and an arbitrary joint malformed/adversary state,independent of core
workspace on the no-earlier-bad history. Private instruments during
delivery act only on the adversary/malformed factor. This also covers
malformed copies entangled with one another. These flags are analytical
records,never an oracle available to the algorithm.

After ALL deliveries,the11 fresh fair coins are independent of these
flags,states and workspace. Ifb_i copies in this bank were malformed,
Pr(selected malformed |preselection record)=b_i/2048. If the selected
copy is clean,it is exactlyrho_s in tensor product with the core and all
other systems. Swapping it into the working register and resetting the
unchosen bank cannot alter this product. Subsequent core computation
preserves the induction on no earlier bad selection. The selection and
cleanup outcomes are not used as decoder coins or data.

First-bad bound. There are exactlyQcap banks including padding. LetA_i
denote that banki is active and no earlier selected copy was malformed.
It is fixed before the current selection coins. Ifb_i is the bad count
in banki,conditional expectation and the preceding lemma give

    Pr(any selected bad)
      <=sum_i E[1_(A_i) b_i/2048]
      <=E[sum_all_banks b_i]/2048
      <=epsilon Qcap.                             (18.2)

The last inequality uses the pathwise global model budget
sum b_i<=floor(epsilon*2048Qcap). Padding copies contribute to that
budget and to actualQ,even though none is returned. No independence
between banks or corruption decisions is asserted. The adversary may
use all earlier measurement outcomes and arbitrary private processing;
the current selection coins are drawn only after its current deliveries.

Reference comparison. Construct an analytical hybrid that returns an
independent idealrho_s at every reference core request,carrying wrapper
records and adversary systems as auxiliary environment. Core decoding
does not read wrapper outcomes and its own coins stay independent,so
its marginal is precisely the clean reference core of13. Until the first
selected malformed copy,the conditional-bank lemma makes actual and
hybrid returned states and all core operations identical. Unchosen-bank
operations are local to the auxiliary factor. Thus the two processes
can differ in output only on the first-bad event; equivalently,track a
classical first-bad flag in their unnormalised state induction and charge
its total trace at most18.2. This is a comparison proof,not physical
cloning,measurement of Bad,or conditioning the entire adaptive run on
all selections being clean. In particular,that conditioning could bias
past outcomes and is not used.

Consequently the actual main error is at most

    2^-8+epsilon Qcap<=2^-8+2^17/400000<1/3.

There is no approximate-permutation error on the main branch. On success
orABORT,padding and cleanup leave the recorded classical output unchanged.

The guarantee is nonvacuous. Fromm>32l-1,dl>=n/(64l),Kp>=8192l,
Lblk>=n/l we obtainCp>=2048n^33,Qcap>=4096n^34/l. Therefore

    epsilon Qbank=epsilon*2048*Qcap>=2^23/400000>20.

The model permits at least20 malformed raw copies at every main input.
The asymptotic allowed count is bounded by a constant; no growing-count
claim is made. Every unused and padding copy is included in actualQ.

Finite branch. Putk=n+10. A fixed candidate block under the ideal shuffle
is a sizek sample without replacement from the fixedBad set. LetI_j mark
bad positions andB_c=sum I_j. For every chosenh positions,
Pr(allh bad)=(|Bad|)_h/(Qbank)_h<=(|Bad|/Qbank)^h<=epsilon^h.
Expanding product(1+I_j) gives

    E2^B_c<=sum_h binom(k,h)epsilon^h=(1+epsilon)^k.

Forc!=s,a clean shifted copy has unbiased X control because its two data
branches are orthogonal. Conditional on the bad pattern,clean copies
factor independently and arbitrary entangled malformed-copy measurement
effects are bounded by the identity. The probability allk outcomes are
plus is therefore at most2^(-(k-B_c)),without assuming independent bad
outcomes. Union overN candidates givesfalse acceptance probability
<=N2^-k(1+epsilon)^k<=2^-10 exp(epsilon k)<=2^-9.
Forc=s every clean test isplus,so rejection of the true candidate requires
at leastone bad copy in its fixed block,with probability<=epsilon k.
Atn>=2,use log2n<=n,k<=6n to getepsilon k<=6/(400000 n^32)<2^-32;
atn=1 it iszero. Thus exp(epsilon k)<2. Adddelta once: finite total
failure<=2^-9+2^-32+2^-100<1/100. Testing EVERY fixed block in full
is essential to this argument; no adaptive early-stop layout is used.
All finite bank/copy/workspace costs are bounded by absolute outer
constants over the fixed finite integer range,as stated in0 and15.

The two branches prove the uniform positive fraction and all resource
claims for everyN and secret and every adversary of0.
