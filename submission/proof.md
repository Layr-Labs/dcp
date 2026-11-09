# CLEAN-40-LARGE: explicitly measured fine vectors at fractional sample depth

## 0. Joint theorem, exact bank configuration and error model

For everyN>=2 andsecret s moduloN,putn=ceil(log2N). The single
CLEAN-40-LARGE algorithm below,with independent ideal source copies,recovers
the entire secret with unconditional probability>=1-2^-8. Every branch
jointly obeys,with absolute constants,

    F(n)=n^(3/5)+(1/2)n^(2/5)-n^(1/5),
    T=O(n^(14/5)2^F(n)),
    S_C=O(n^(3/5)2^F(n)),S_Q=O(n),
    Q=O(n2^(n^(2/5))).

Indices3/5,3/5,0,2/5; malformed fraction0 requires independent ideal
copies and asserts no impossibility of positive robustness. Logarithmic
resource envelopes atn=1 usepositive n=2 values. Every raw copy in the
constant microbanks,padding,rejections and failed attempts is counted.
The finite exhaustive branch below n=2^48 is proved separately; its costs
are covered by absolute uniform outer constants,not a main-only claim.

For n>=2^48 compute exact parameters

    m=least positive integer withm^5>=n^2,u=ceil(log2n),
    kappa=ceil(log2m)+1,s0=kappa+1,
    base=ceil(n/(m+1)-m/2)+1,dl=base+s0,H=base+m-1,
    L=floor(m/(4s0)),lift(k)=min(s0,floor(k*s0/L)),
    lambda_i=base+i+lift(m-1-i) for i<m,lambda_m=d,
    d=1 for coarse roots,d=r for fine vector roots,
    Cc=64dl2^m,Cf=16dl2^m,Y=ceil(log2Cc),E=8u,
    htop=Y+E+12,P=htop+Y+8,Kc=32768(P+u+100),
    g_w=ceil(log2dl),b0=floor(H/2)-1024u,Lblk=ceil(n/b0),
    noise=ceil(log2(n^5)); each actual data block b uses r=b+noise.

The consumed-slot capQcap is defined in13 before access; Qbank=1024*Qcap.
For the main branch each reference source request in3..12 uses a fresh
microbank ofKraw=1024 raw copies: hold core workspace idle while they are
acquired,then draw10 fresh fair bits and select exactlyone uniformly.
Unchosen copies are reset/released. The main core never uses the wrapper's
selection or cleanup outcomes. After the core stops,pad with unused
microbanks until exactlyQcap microbanks have been acquired. Thus actual
Q=Qbank=1024Qcap is fixed byN,including all discarded and padding copies.
For n<2^48 use the whole-bank finite branch in13/18. The probabilistic
claims of3..12 describe the clean ideal-label reference;5 bounds label
errors,and18 proves the finite branch. All guards apply on every branch.

Integer roots use power comparisons/bisection; all arithmetic is finite
integer/rational arithmetic as8; no real
oracle is supplied. Notation:dn=floor(log2N),N=2^a2 M withM odd,s1=s modM,
s2 in[0,2^a2) withs=s1+M*s2 moduloN,omega=exp(2pi i/N). Logs are base2.
Labels are known nonnegative integers; data basis states|u> have0<=u<N.

## 1. Actual source material and changed fractional-depth profile

Immediate full clean large-block/one-batch/global-attempt template is
the frozen CLEAN-CUBE-LARGE private artifact. At this construction its
finite diagnostics passed, but its genuine review/publication are pending.
No accepted theorem or UUID is invented. Corrections must propagate;
if registered before this child's upload its exact canonical public ID,
files and relevant graph must be verified and formally declared.
It supplies the new clean sequential controller and complete charged
large-output/capacity/wide-grid/finite-vector compiler pipeline, fully
reproduced here. Historical published LARGE16 source
316d16c3-e6c7-4284-ab8d-05eff620cb4a at
5e378e99f91a59e6588b69a143b17db4938b0477 and clean QUDIT-CUBE
c64fcfa8-419c-4fa0-a4de-f0a4fddbbdd5 retain their precise feature credits
through that private construction. All3LARGE16 sourcefiles and2CUBE
sourcefiles were fetched/bytecompared and incoming5/2pendingrefs read;
pending is not accepted ancestry. No verdict is a mathematical premise.

Additional directly read published exact2/5-root geometry source is
QUDIT-40,4729ec52-0365-45f7-9397-258a50835e3f,commit
9e1713467fd4abcc17974ebbc5e7413cad0b3cee. Its exact full proof and
helper were fetched/byte-compared and both incoming pending declarations
read through nextCursor:null. Its Section8 exactm^5>=n² and15 full
F=n3/5+.5n2/5−n1/5 profile are rederived with the new large-root
capacity/fields, one coarse batch and caps. The old logarithmic blocks,
staged bootstrap and per-root constants are not run.

The specialized PGM source is Bacon,Childs,vanDam quant-ph/0501044v2
Sections4,5,8. Balanced commutator synthesis is Dawson,Nielsen
quant-ph/0505030v2 Sections2..4; that paper omits numerical arithmetic
costs. The additional finiteprecision bitcost lemma is reproduced from
LARGE16, and its main2^48 preconditions checked here. Primitive priority,
physical execution, optimality or source independence are not claimed.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger/T/T^dagger gate; a computational-basis
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
(2) pause every core gate/measurement and acquire exactly1024 raw copies
into distinct(n+1)-qubit registers,without ANY algorithm operation,private
draw or measurement between these deliveries;
(3) only after the last delivery,measure10 freshH|0> coins,forming uniform
J in0..1023; SWAP raw registerJ into an empty source working register
with3(n+1) CNOTs on classically known addresses;
(4) reset/release all unchosen registers,and incrementa. Return the chosen
copy to the core. All selection/cleanup outcomes are ignored by the core;
its own decoder coins remain fresh independent coins. The adversary may
see these outcomes before later deliveries,as its model permits.

The local per-root guards in9 count SELECTED MICROTAKE
deliveries,not the1024 raw acquisitions inside one call. Every raw copy
counts in actualQ. After core success orABORT,record its output,release
the core quantum state,and acquire/reset dummy microbanks untila=Qcap.
Dummy banks return no copy and their measurements never alter the output.
Thus actualQ=1024Qcap on every branch; all padding work/storage are charged.
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

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(n^(2/5)) (Section 14),
this is O(n^(12/5)) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL run. Execute this same CLEAN-40-LARGE algorithm but replace each LE
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
lam=Theta(n^(3/5)),0<=b<=2lam and w_d=lam.
There are at most two stable digit passes. Equation6.1a and the
merge join cost O(E(lam+b))=O(n^(3/5)E) core steps.
The E counters each have lam+1 bits, so the bucket arrays occupy
O(E lam) bits, absorbed by O(nE) since lam=O(n). All explicit quantum lookups have
O(n^(3/5)) gates per row; ranks and the inverse lists use O(n^(3/5))-bit
fields. Each high field is at most3n bits (9). High-part preprocessing and
selected-output arithmetic cost O(n(E+E')) steps; the prefix/carry
update costs O(n) once per merge. No repeated full prefixes are expanded.
Thus total work remains O(n(E+E')) core steps and quantum scratch
O(n^(3/5))<=O(n). The actual classical arrays use their high-field widths
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

## 8. Exact fractional-root taper and capacity

Let a=n^(2/5),t=n^(3/5),l=log2n in analysis only. Integer root
comparisons givea<=m<a+1. Put x=n/(m+1)-m/2,base=ceil(x)+1,
s0=kappa+1,dl=base+s0,H=base+m-1,L=floor(m/(4s0)).
At n>=2^48,a>=8,a/t<=1/8,kappa<=log2a+3=(2/5)l+3.
Alsoa>=8((2/5)l+4)² at48 and the exponential/polynomial ratio increases,
so m>=8s0²,L>=2s0>0,L<=m-1 ands0<=m-1. We have

    base>=t/(1+2/a)-a+1>=t/2>=s0,
    base>=4,dl<=2base,g_w<=base-1,m+g_w<=H,
    H=ceil(x)+m<=n/(m+1)+m/2+1<=2t,
    m+1<=2a,(m+1)H<=4n.                            (8.4)

All endpoint inequalities have slack at2^48 and improve thereafter.
Thus m=Theta(n^(2/5)),base,dl,H=Theta(n^(3/5)).
Let lift(k)=min(s0,floor(k*s0/L)). It has increments0 or1 andlift(k)<=k/2.
Input widths lambda_i=base+i+lift(m-1-i) grow by0 or1,start atdl,end atH,
and satisfy lambda_i<=H-ceil(k/2),k=m-1-i. Nonroot capacities
2lambda_i-lambda_(i+1)-kappa are at leastbase>0; root2H-1-kappa is positive.
Define B0=(m+1)base+m(m-1)/2-1 and
A=sum_(k=0)^(L-1)(s0-floor(k*s0/L))<=s0L<=m/4.
The uplifts sum to m*s0-A, so exact root/nonroot telescoping gives

    Sum=2lambda_0+sum_(1<=i<m)lambda_i-1-m*kappa
       =B0+m+s0-A.                                (8.2)

Since base>=n/(m+1)-m/2+1,B0>=n andSum>=n+3m/4+s0>=n.
For B<=n allocateb_i root-down under these maxima,settingtp_0=0,
tp_(i+1)=tp_i+b_i,tp_m=B. All residue reads lie belowB and
b_i+lambda_(i+1)-2lambda_i<=-kappa. Binary failure is at most2^-kappa
conditional on ENTIRE built inputs/history,including partial/zero windows.

For each ACTUAL data block b set noise=ceil(log2(n^5)),r=b+noise.
The root maximum drops from2H-1-kappa to2H-r-kappa, losing
b+noise-1. But its required precision B<=n-b: odd B=dn-b,
twoadic B=wd-b. Hence b cancels exactly, leaving total slack at least
3m/4+s0-noise+1>0. Since noise<=5u andm>=a>=10u+100, this
holds throughout the main range. Every nonroot dimension/failure bound
is unchanged; r<=H implies rootmaximum2H-r-kappa>0.

Put Cc=64dl2^m,Cf=16dl2^m,Y=ceil(log2Cc),E=8u,
htop=Y+E+12,P=htop+Y+8,Kc=32768(P+u+100),
b0=floor(H/2)-1024u,Lblk=ceil(n/b0),noise=ceil(log2(n^5)).
At l>=48, a=n^(2/5)>=2^16, m<=a+1 and a>=10u+100.
We have H>=t/2, t=n^(3/5), H<=2t, gw<=u,
Y<=m+u+6, htop<=m+9u+18<=2m, P<=2m+10u+32<=3m.
Also m<=n/4 gives htop<=n/2, so B=dn-h>=1 for ordinary
coarse h<=htop. The extra condition h<=floor(log2M) gives B>=a2.
Since t/a=n^(1/5)>=2^(48/5)>512, m+gw+htop<=4a+3<=t/2<=H.
Similarly m+gw<=2a+1<=H/2, so m+gw+b0<=H.

The b0 lower bound is b0>=t/4-1024u-1>=t/5, using
 t>=20(1024u+1).
This holds at l=48 and the ratio2^(3l/5)/(l+1) increases thereafter.
Thus b0>0 and a<=Lblk<=5a+1<=6a: the lower bound follows
b0<=H/2<=t. For each data r=b+noise<=H and2b<=H-2048u.
At an odd data call b<=Jtarget<floor(log2M), so B=dn-b>=a2+1,
including shortened final blocks. These are operational legality bounds,
not an assumption that b0 itself is smaller than log2M.

All caps, precisions and loop dimensions are computed before access.
In particular Kc/8192=4(P+u+100) and Kc<=2^17m. No earlier
logarithmic-block field proof or staged coarse confidence is reused.

## 9. BATCH(supplier, B, R, h=1)

Input: a supplier of leaf qubits with known labels,whose ideal accepted
values are independent uniform[0,2^(B+h)),1<=h,1<=B,B+h<=n.
VROOT(supplier,B,h,d) builds ONE root of outputwidthd in{1,r}. Allocate
nonroot lambda_i as8,lambda_m=d,and budgets under the changed root
capacity. Start with all quantum workzero. Count selected source calls;
Set Croot=Cc for coarse and Croot=Cf for data.
If callCroot+1 would be needed,stop,reset all work and returnmissing.
Rejected suppliers and failed merges count. Completion returns the
root index and its high-part table; it is immediately decoded/measured,
then ALL work is reset before any new root call. No earlier source or
quantum root persists between calls. Source parameters are fixed within
a root; retry of a missing fine root keeps those same parameters.

BATCH(supplier,B,R,h) for the ONE COARSE batch callsVROOT with d=1 R times.
A completed root is immediately measured in a fresh fairX/Y basis,
recording(W,beta,Z); a missing root contributes scorezero. Reset all
quantum work between roots. All parameters stay fixed until allR
classical records exist,then scores and the centre are updated.
For cost bounds only putD_R=C_R=R*Cc; there is no separate demand guard.
Fine vector attempts and direct final blocks are specified in11/12/13.

Each frame allocates its actual2^lambda_i rows and actual output length,
not2^H rows at every level. Changing the index widths does not change the
canonical source footprint: a level-i logical label is still the sum of at
mostdl2^i accepted source labels. Therefore the exact high-part field and
carry formulas below apply with these actual row counts as well.

TREE. VEC(0) = LEAF: for each of dl wires request the next accepted qubit by NEXT(0),subject to the per-root selected-call cap above. Increment the delivered count on acceptance. These qubits form
the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j.
At p=0 write only this hi table, of width w_0=D_src+g_w per row; c=0. The logical
table has length 2^dl, is exactly the tensor product state in the ideal run, and is collimated to tp_0=0.
VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until out != FAIL; return out. A root is VEC(m),
evaluated depth-first. At its final MERGE use lambda_m=d. VROOT returns this one index after at mostCroot selected calls.

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

Root. At p=B store common prefixc and highpartshi[a] for0<=a<2^d.
PutW_a=hi[a]-hi[0],soW_0=0. The ideal state,up to global phase,is

    2^(-d/2) sum_a exp(2pi i 2^B W_a th)|a>.       (9.1)

For d=1 coarse notationW meansW_1. Each label sums at mostdl2^m
accepted values below2^(B+h). Also each actual root uses at mostCroot
source calls. Consequently

    |W_a|<=2^h Croot<=2^(Y+h).                        (9.2)

Since2^(m+g_w)<2dl2^m<=Cc,m+g_w<=Y. All high fields obey
w_i<=D_src+m+g_w<=n+Y<=3n; wrong-label branches obey these dimensions
because accepted stored labels still belong to the same finite ranges.
The common prefix cancels in every W_a. No full logical label table is
reconstructed. For a fine root the2^r<2^(b+1)n^5 high rows are explicitly stored;
the full exponential decoder charge is bounded in14/qudit_decoder5.

Coarse decoding uses its actualwideh<=htop; block decoding usesh=b. No root-cost bound depends onh.

Lemma9.1 (clean capped-root law). In the ideal-label reference process,
each coarse root is missing with probability<=3/32 and each fine
root with probability<=3/8. The cap
uses only selected counts and low-bit structural decisions; conditional
completion retains the unused-top-bit laws in10.
Proof. In the uncapped clean process p=2^-kappa<=1/(2m). Conditional
on the ENTIRE built input/history every merge fails with probability<=p.
After children are built,represent the failure event by an independent
uniformU and actual failure thresholdq<=p. Add analytical ghost retries
wheneverU<=p; U>p forces success. Parent coins are independent of upper
child costs. Induction dominates delivered demand byZ_0=dl and
Z_i=sum_(j=1)^G(Z_(i-1,j,1)+Z_(i-1,j,2)),whereG is independent geometric
success1-p. Hence E Z_m=dl2^m(1-p)^(-m)<=3dl2^m: use
-m log(1-p)<=mp/(1-p)<=1 for m>=2. Supplier rejection is independent
of its accepted uniform value,and acceptance>=1/2,so expected selected
calls<=6dl2^m. Markov bounds cap failure by6/64=3/32 for coarse and6/16=3/8 for fine. Almost-sure finite
geometric constructions justify the uncapped comparison. Capping earlier
cannot increase this expectation. Root caps read no unused top bits.
This is only a statement about clean reference roots,not actual roots
conditioned on adaptive flags. All actual branches terminate at the cap.

## 10. Unused-top-block independence and score discrimination

ForBATCH(B,R,h),write each accepted labelk_v=low_v+2^B tau_v,
0<=low_v<2^B,tau_v uniform inZ/2^h. LetG include all low_v,all merge
outcomes(e,bl),FAIL/retry/root-cap/qubit assignments and controller selection
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

Thus within a clean reference root,conditional on its G,thetau_v remain
independent uniformZ/2^h. A table entry is the sum of leaves with a0/1
incidence vector. Distinct indices have distinct vectors: it holds for a
leaf(0,k_v),LEAF concatenates disjoint coordinates,and MERGE injectively
reindexes pairs on disjoint coordinates. The two root entries therefore
have different incidence vectors,so

    W=cst+sum_(v inSp)tau_v-sum_(v inSm)tau_v,       (10.1)

with disjointG-measurable sets,nonempty union,and integralG-measurablecst.
Every nonzero coefficient is+1 or-1. Holding all but one suchtau fixed
proves W mod2^h is uniform. Clean reference roots use disjoint fresh sources and have identical marginal laws for fixed stage parameters. Completion reads onlyG and preserves these unused-top-bit identities. Forh=1 this also gives

    |E exp(2pi i phi W)|=|cos(pi phi)|^hd<=|cos(pi phi)|,
    Pr(W odd |G)=1/2,                              (10.2),(10.3)

wherehd=|Sp|+|Sm|>=1,while the wide characteristic bound used here is proved in robust_decoderF.

Fine-vector lemma. For a completed root with d=r,putq=2^b,h=b.
For any distinct output indicesa,c,their incidence-vector difference is
nonzero and has a coefficient+1 or-1 on some unused top labeltau_v.
ThereforeW_a-W_c is uniform moduloq conditional on the complete
structural transcriptG. No independence of the full frequency vector is
asserted. qudit_decoder.md constructs a finite Clifford+T measurement
for the known vector(W_a),oddJ and phasevector

    2^(-r/2) sum_a exp(2pi i J W_a v/q+i eta_a)|a>,
    |eta_a|<=1/(16n^4).

It outputs the truev with error at most2/n^4 averaged over the conditional
unused top bits,for EVERYv andG,including all gate-synthesis error. This
law holds conditional completion because caps/retry read onlyG.

For B=0 twoadic data use Section12's direct product of r qubits.
Distinct subset indices give the same pairwise-uniform frequency law.
There is no Kp-vote final block in this algorithm.

## 11. ONE wide coarse batch and sequential signed odd blocks

Run robust_decoder.md F with its stated fixed Cc,Y,E,htop,P,Kc.
M=1 returns0. SMALL returns exacts1. LARGE returnschat,R0; define
Jtarget=min{J>=0:2^J>=4R0}. By its definition4R0<=2^Jtarget<8R0; sinceR0/M<=2^(-Y-E-7),
2^Jtarget<8R0<=M2^(-Y-E-4), proving Jtarget<log2M-Y-E-4.
Set low=0,j=0; whilej<Jtarget choose b=min(b0,Jtarget-j),r=b+noise.
Each root attempt has precision B=dn-b, capCf and the following supplier.
Compute gamma=2^(B-a2) modM,K0=(-2^b)^(-1) modM,
J=(2^bK0+1)/M (an odd integer), and CRT unit alpha with
alpha=1 mod2^a2, gamma*alpha=K0*2^(-j) modM.
Apply Shift_(chat+low modM),Mult_alpha,LE, accept iff k<2^dn,
then X. Accepted labels are uniform[0,2^dn), acceptance>1/2,
and the physical root phase(relative to entry0), on correct past, is
 exp(2pi i K0 W_a t_j/M)
 =exp(2pi i J W_a t_j/2^b) exp(-2pi i W_a t_j/(2^bM)),
where t_j=(t0-low)/2^j. This follows by multiplying out the CRT
relation and canceling the twoadic phase using B>=a2+1.
Since R0>=1, signed quotient induction gives |t_j|<=R0 on correct
past. The known source footprint gives |W_a|<=2^bCf, so the extra
phase magnitude<=2pi Cf R0/M<2^-E<1/(16n^4).

Retry missing roots with these SAME current supplier/block parameters,
subject to the ONE global attempt cap13. A completed root is measured
by qudit_decoder.md for this odd J,b. Reset all work after each attempt.
On completion append its measured residue a: low+=a2^j,j+=b.
Conditional completion the every-secret block error is<=2/n^4 on
correct past. After Jtarget bits choose the unique signed representative
of low modulo2^Jtarget in[-R0,R0], else output0. Uniqueness follows
2^Jtarget>=4R0. Correct blocks recover t0 and s1=(chat+t0) modM.
All incorrect histories still have finite specified labels/dimensions,
unit alpha and the same guards; no verifier or backtracking is used.

## 12. Sequential twoadic blocks, including direct zero-precision vectors

After s1, write s=s1+M*s2 moduloN. Setj=0,low=0. Whilej<a2 put
wd=a2-j,b=min(b0,wd),r=b+noise. Shift_(s1+M*low),LE,X yields
uniform k moduloN; kk=k mod2^wd is uniform[0,2^wd) with phase
exp(2pi i kk*remaining/2^wd) on correct past. For B=wd-b>=1 use
ordinary known-label VROOT with h=b,d=r,capCf. Retry missing under13.
Its exact phase is2pi W_a*remaining/2^b and qudit_decoder.md usesJ=1.
For B=0 acquire r independent DIRECT source phase qubits with uniform
kk modulo2^b. Their product is the equal-amplitude vector on2^r subset
indices, with known labels their subset sums. A difference of distinct
subsets has a coefficient+1 or-1, so each pair difference is uniform
modulo2^b. Use the SAME finite vector decoder withJ=1. This attempt
completes surely and uses r<=Cf selected calls; no invalid B=0 tree
or Kp-vote subroutine is requested. It counts as one global attempt.
After completion append a: low+=a2^j,j+=b. Reset ALL work after each
attempt. On correct past the vector has no phase perturbation and each
completed block error<=2/n^4. Correct blocks give low=s2. Return
(s1+M*low) modN. Incorrect prefixes still define the same finite
physical instruments, dimensions and guards, without a correctness claim.

## 13. Actual complete algorithm and reference-core error budget

Finite branch(n<2^48). Putk=n+10,Qcap=N*k,Qbank=1024*Qcap. Prefetch and
shuffle as18. For EVERY candidatec=0..N-1,use its predetermined block ofk
consecutive bank slots,applyShift_c,measure the control inX,and record
whether all outcomes wereplus. Test every block in full; no early stop,
skipped candidate or adaptively shifted block boundary is used. Output the
first candidate whose block was allplus,or0 ifnone. Unused bank slots are
reset/released without conditioning the output on their measurements.
Section18 proves this finite branch uniformly for everyN,s under the
independent-ideal-copy promise.

Main branch(n>=2^48). Compute all N-dependent parameters first.
Set A=4Lblk and Qcap=Cc*Kc+Cf*A,Qbank=1024Qcap. Size LE confidence
with this Qcap. Run the ONE coarse batch then11/12 sequential data.
Every data attempt, including a direct B=0 vector, increments ONE shared
counter before access; before attemptA+1 ABORT0. Missing roots retry
only within this global bound. There are <=2Lblk desired completions.
After success/abort reset all work and pad exactly Qcap microbanks.
Selected rejections, failed/capped attempts and all1024 raw copies per
bank, including discards and padding, count. Actual Qbank is fixed byN.
The coarse batch is reserved in the cap even if its odd part is skipped.

Ideal-label clean reference: each fine attempt has conditional completion
probability>=5/8 on EVERY finite prior history, by9; direct vectors
complete surely. Extend with ghost Bernoulli5/8 attempts if needed.
Failure to finish <=2Lblk desired blocks in4Lblk attempts therefore has
probability<=exp(-Lblk/8)<2^-20, since Lblk>=a>=2^16.
This follows also from the conditional Hoeffding exponential moment;
it does not assume independent actual completion indicators. Each
correct-past completed vector has error<=2/n^4, so the first-block-error
union over <=2Lblk<=12a blocks is <=24a/n^4<2^-20.
The ONE coarse error is<=2^-20 in the ideal-label reference. Actual
clean execution agrees until the first LE error, charged once by5.1
as<=2^-10. No entire run is conditioned on correct labels. Total main
failure<=2^-10+3*2^-20<2^-8. The separate finite branch is proved in18.

## 14. Complete charged resource ledger on every branch

Put a=n^(2/5),t=n^(3/5),l=log2n. Proof8 gives m=Theta(a),
dl,H=Theta(t), Lblk<=6a and Kc<=2^17m. Thus
 Qcap=CcKc+CfA=O(t*a*2^m)=O(n2^m).
For example dl*m<=4n implies CcKc<=2^25n2^m; the fine term
16dl2^m*4Lblk<=768n2^m, so Qcap<=2^30n2^m is a loose
uniform main-range numerical upper bound. Actual Qbank=1024Qcap
includes every rejection, failed/capped root, discard, direct vector and
padding. All loops and cutoffs are fixed finite dimensions before access.

Quantum. Depth-first core indices use <=two H-sized frames per level,
and (m+1)H<=4n. Root/lookup/AND scratch uses O(H+r+b)=O(n),
source/LE/modular arithmetic O(n); compiler arithmetic is all classical.
Each microbank has1024(n+1) qubits and10 coin qubits, with the core
idle and retained wires counted. No bank source or discarded wire is
omitted. Total accessible quantum peak is O(n), also on wrong histories.

Classical. Ordinary coarse/data fields satisfy m+gw+h<=H by8. Thus
at level i, k=m-1-i, remaining precision R_i<=(k+2)H and
stored high width w_i=R_i+h+i+gw<=(k+3)H. The actual length taper
lambda_i<=H-ceil(k/2) gives
 H2^H sum_(k>=0)(k+4)2^(-ceil(k/2))=19H2^H.
This covers every retained sibling, high field, radix bucket, rank/inverse
map, output and scratch frame. Rootwidth r<=H and its h+m+gw<=H
fields fit the same bound. Source, prefix, parameter and score records
are polynomial. The explicit data decoder costs O(2^(2b)n^128) bits,
which is O(2^H/n^1920) since2b<=H-2048u. No unknown high-label
or uncounted quantum lookup table is supplied. Peak SC=O(H2^H).

Work. Each leaf costs O(n2^dl) core steps and dl delivered qubits.
At height i, each merge costs O(n2^(dl+i+1)) and consumes2^(i+1)dl
fresh canonical delivered coordinates not reused at that height. A partial
leaf at cap is charged fully. Summation over all capped roots gives
 O(nQcap2^dl(m+1)/dl)
core work; actual addresses have width O(H+logQcap)=O(t).
Since (m+1)/dl=O(a/t), total addressed tree work is
 T_tree=O(n²*a*2^(m+dl)).                         (14.1)
Initializing O(a) compressed frame pools costs O(a H²2^H), including
bit-address costs once, below14.1 as H=m+dl-s0-1 and H<=2t.
The declared time includes this initialization, not just arithmetic on
already populated tables. No expected-work statement replaces these caps.

Every actual fine vector, including B=0, costs O(2^(2b)n^128) work
and bits by qudit_decoder.md5, including table preprocessing, sparse
inverse/forward scans, controlled prefix preparations, finiteprecision
synthesis, circuit generation, addresses, execution and cleanup. Over
O(a)<=O(n) calls this is O(2^H/n^1900), absorbed by14.1 and H2^H.
All targets are known integer-count/dyadic matrices; no free rotation,
QRAM, subset-sum oracle or preloaded instance advice is used.

Coarse P<=2m+10u+32, with O(m) records each of O(m+u) bits.
Stream all2^P candidates, including exact modular scores/trig-table
lookups, keeping only current score and the smallest maximum. A crude
O(n^50 2^(2m)) addressed work and polynomial classical storage bound
covers this enumeration. It is below14.1 because dl>=3m+100u:
dl>=t/2>=256a, m<=a+1, u<=a/10, and a>=2^16 prove this
last inequality already at the main cutoff and increasingly thereafter.
There is no exponential quantum candidate array or score oracle.

Confidence has logQcap=O(m+l)=O(a). Every source/extraction costs
O(n²a) core work, hence only polynomial(n)*2^m over Qcap calls,
absorbed by14.1 since dl grows faster than m andlogn. Euclid/CRT,
signed updates, guard/counter arithmetic, all measured/erased wires,
source charges(n+1)Q, selection, routing and exact padding have the same
absorption. All actual operations remain capped after incorrect labels,
wrong prefixes or arbitrary measurement outcomes. Idle core wires count
throughout source delivery. Therefore14.1,SC=O(H2^H),SQ=O(n)
and Q=O(n2^m) hold JOINTLY on EVERY branch of this single algorithm.

## 15. Exact fractional-depth complete uniform envelopes

Put a=n^(2/5),t=n^(3/5),F=t+.5a-n^(1/5),l=log2n.
The exactm=ceil(a) rule and finite reciprocal inequality give
 n/(m+1)<=n/(a+1)<=t-n^(1/5)+n^(-1/5)
                              <=t-n^(1/5)+1,
 H<=n/(m+1)+m/2+1<=F+3,
 m+dl=H+kappa+2<=F+(2/5)l+8,m<=a+1.
The inequality1/(1+x)<=1-x+x² for x>=0 proves the reciprocal
bound, including all ceiling errors. Substitute14's complete addressed
work O(n²*a2^(m+dl)) andH<=2t:
 T=O(n^(14/5)2^F),SC=O(n^(3/5)2^F),SQ=O(n),
 Q=O(n2^(n^(2/5))).
Every outer power and all three signed exponent monomials occur in the
structured declarations. Time/classical indices3/5,copy2/5,quantum0
hold jointly for this sameconfiguration. Source2^m<=2*2^a is separately
charged. Finite n<2^48 costs are bounded with absolute uniform constants;
its correctness is independently proved in18. At n1 resource envelopes
usepositive n2 values. Finite bankallocation1024N(n+10)(n+1)+O(n)
is <=C_f*n for fixedC0=2^48, e.g. C_f=2^20*2^C0*(C0+100)^2.
Other finite costs are counted with absolute constants, not omitted.

## 16. Error tolerance

The fifth claim is epsilon(n)=0 under the exact clean-input context in
submission.json. It promises independent ideal coset copies throughout.
All four worst-case bounds and success above are joint under that promise.
Zero asserts no positive resilience or impossibility result.

## 17. Scope

This is a clean-source joint upper-bound construction with a lower
polynomial time/copy prefactor than the published2/5-depth vector source.
It does not meet2^O(n^(1/3)) time, assert an optimum/lower bound,
practical constants, physical execution, or a new primitive. All finite
and incorrect-history branches and actual bit/gate/source costs count.

## 18. Finite-input correctness and clean source wrapper

Below n=2^48 prefetch exactlyQbank=1024N(n+10) ideal copies and shuffle
bythe finite-bit modulo Fisher-Yates algorithm: withz=ceil(log2Qbank),
ell_s=2z+u+100,fori=Qbank-1 down1 drawell_s fairH-measurement bits,
formR,swap wholecopyregistersi andR mod(i+1). Every swap is3(n+1)
CNOTs on charged known addresses. There is no rejection loop. Since all
copies are identical independentrho_s,everyfixed permutation leaves the
bank's joint stateexactlyrho_s^tensorQbank. A mixture ofpermutations also
leaves itunchanged,so no distributional approximation error is needed.
The shuffle is retained only to fully specify the inherited finite branch;
it costs time/space and confers no additional clean-input promise.

For EVERYcandidatec=0..N-1,its predetermined block ofk=n+10 copies is
tested in full:applyShift_c thenmeasure thecontrolX. Ifc=s,allk outcomes
areplus with certainty. Ifc!=s,orthogonal data branches give an unbiased
X outcome,and independent copies make allplus probability2^-k. Union over
at mostN falsecandidates givesN2^-k<=2^-10. Outputthefirst allplus
candidate (or0 ifnone); a true allplus block always exists. Thus full-secret
finite failure<=2^-10<2^-8. No earlystop or adaptiveblockboundary occurs.
Everyremainingbankcopy is reset/released,with source countunchanged.

On the main branch every bank's raw copies are ideal products. Freshuniform
post-bank selection simplyreturnsanother idealproduct; unchosen cleanup
and padding do not affect the core. Everyselectedcopy and all raw copies
are charged. Analyze the ideal-label reference,then couple toactualLE
until its first incorrect extraction. Bound5.1 charges that eventonce,
without conditioning the reference on correctLE. The main pipeline13
therefore proves fullsecret success>=1-2^-8 uniformly. These clean-input
arguments use neither a hidden malformed flag nor a positive-noise claim.
