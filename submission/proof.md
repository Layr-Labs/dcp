# QUDIT-44: explicitly measured fine vectors at fractional sample depth

## 0. Joint theorem, exact bank configuration and error model

For everyN>=2 andsecret s moduloN,putn=ceil(log2N). The single
QUDIT-44 algorithm below,with independent ideal source copies,recovers
the entire secret with unconditional probability>=1-2^-8. Every branch
jointly obeys,with absolute constants,

    F(n)=n^(5/9)+(1/2)n^(4/9)-n^(1/9),
    T=O((n^(31/9)/log2n)2^F(n)),
    S_C=O(n^(5/9)2^F(n)),S_Q=O(n),
    Q=O((n^(14/9)/log2n)2^(n^(4/9))).

Indices5/9,5/9,0,4/9; malformed fraction0 requires independent ideal
copies and asserts no impossibility of positive robustness. Logarithmic
resource envelopes atn=1 usepositive n=2 values. Every raw copy in the
constant microbanks,padding,rejections and failed attempts is counted.
The finite exhaustive branch below n=2^48 is proved separately; its costs
are covered by absolute uniform outer constants,not a main-only claim.

For n>=2^48 compute exact parameters

    m=least positive integer withm^9>=n^4,u=ceil(log2n),
    kappa=ceil(log2m)+1,s0=kappa+1,
    base=ceil(n/(m+1)-m/2)+1,dl=base+s0,H=base+m-1,
    L=floor(m/(4s0)),lift(k)=min(s0,floor(k*s0/L)),
    lambda_i=base+i+lift(m-1-i) for i<m,lambda_m=d,
    d=1 for coarse roots,d=r for fine vector roots,
    Kc=8192(m+10u+100),Kp=8192(u+100),g_w=ceil(log2dl),
    b0=floor(log2n),Lblk=ceil(n/b0),E=4u,r=ceil(log2(n^5)).

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

## 1. Provenance and exact change

Direct new vector-measurement/capped-pipeline source: QUDIT-L16,
proof SHA-256 8ecb8b34668a54f077d1a8f23a91cb79bc0ce511f69405383cba2e3c94c717bf,
helper SHA-256 cce403a87549d6aebca189a7885230482f82ce894e4d29fc5e985b96741ba05d.
The registered source identifier is recorded in the formal dependency
once published; no publication or prior verdict is a mathematical premise.
It supplies the retained vector root,explicit bin/rank/Fourier decoder,
known-angle compilation,extra coarse precision and global retry cap.
All needed physical/extractor/merge/taper/source identities are reproduced.
Its historical MICRO/BANK and older block-decoder credits are retained.
The adaptive first-bad comparison and positive fraction are NOT used here.

Direct fractional geometry source: our published BLOCK-44,
6fa52d51-2814-44a1-8a95-cf7992108413,commit
8d9dbf6fef76aaf2159f4822c3bd97970d4da562,proof SHA-256
eceae899947b7c1efc735d0facbdf51a8575b6aa661d549a4e4f35086a71c024.
Its exact public file was downloaded and compared byte-for-byte; all3
attribution references were read (provisional is not verified ancestry).
It contributes exact integer-root geometry,capacity,precision-weighted
storage and the full F(n) with its negative term. All are rederived here
with rootwidthr. The new one-vector-per-block/global-retry accounting
saves a logarithm in T andQ while keeping both space envelopes. Source
credits to TAPER-SQRT2,BLOCK64 andCSP-44 remain through BLOCK-44.
No new error-resilience theorem is claimed by this clean configuration.

External material measurement source: Bacon,Childs andvanDam,Optimal
measurements for the dihedral hidden subgroup problem,quant-ph/0501044v2,
https://arxiv.org/abs/quant-ph/0501044 ,Sections4,5,8 (covariant PGM and
frequency-bin state compression). We rederive this finite-vector success
bound and explicitly enumerate all bins; no subset-sum oracle is supplied.
External compilation source: Dawson andNielsen,The Solovay-Kitaev algorithm,
quant-ph/0505030v2,https://arxiv.org/abs/quant-ph/0505030 ,Sections2..4.
Its constructive fixed-gate compilation theorem is used with charged
precision and circuit generation in qudit_decoder.md. Neither PGM nor
gate synthesis is claimed as a new primitive or an independent invention.

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

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(n^(4/9)) (Section 14),
this is O(n^(22/9)) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL run. Execute this same QUDIT-44 algorithm but replace each LE
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
lam=Theta(n^(5/9)),0<=b<=2lam and w_d=lam.
There are at most two stable digit passes. Equation6.1a and the
merge join cost O(E(lam+b))=O(n^(5/9)E) core steps.
The E counters each have lam+1 bits, so the bucket arrays occupy
O(E lam) bits, absorbed by O(nE) since lam=O(n). All explicit quantum lookups have
O(n^(5/9)) gates per row; ranks and the inverse lists use O(n^(5/9))-bit
fields. Each high field is at most3n bits (9). High-part preprocessing and
selected-output arithmetic cost O(n(E+E')) steps; the prefix/carry
update costs O(n) once per merge. No repeated full prefixes are expanded.
Thus total work remains O(n(E+E')) core steps and quantum scratch
O(n^(5/9))<=O(n). The actual classical arrays use their high-field widths
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

Let a=n^(4/9),t=n^(5/9),l=log2n in analysis only. Integer root
comparisons givea<=m<a+1. Put x=n/(m+1)-m/2,base=ceil(x)+1,
s0=kappa+1,dl=base+s0,H=base+m-1,L=floor(m/(4s0)).
At n>=2^48,a>=8,a/t<=1/8,kappa<=log2a+3=(4/9)l+3.
Alsoa>=8((4/9)l+4)² at48 and the exponential/polynomial ratio increases,
so m>=8s0²,L>=2s0>0,L<=m-1 ands0<=m-1. We have

    base>=t/(1+2/a)-a+1>=t/2>=s0,
    base>=4,dl<=2base,g_w<=base-1,m+g_w<=H,
    H=ceil(x)+m<=n/(m+1)+m/2+1<=2t,
    m+1<=2a,(m+1)H<=4n.                            (8.4)

All endpoint inequalities have slack at2^48 and improve thereafter.
Thus m=Theta(n^(4/9)),base,dl,H=Theta(n^(5/9)).
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

For fine outputwidthd=r,replace rootcapacity2H-1-kappa by2H-r-kappa.
Total capacity decreases byr-1<=5u-1,while the available slack3m/4+s0
exceeds5u at l48 and thereafter,usingm>=a and a/(l+1) increasing.
Thus everyB<=n still fits. Coarse roots used=1. We have1<=r<=5u<H.

At l>=48,a>=10u+100,soKc=8192(m+10u+100)<=2^14m,
Kc*dl<=2^16n. PutCt=65536dl2^m,Y=ceil(log2Ct),E=4u. Since dl<=H<=2t<n,

    m<=Y<=m+u+16<=n/2,
    Kc/8192=m+10u+100>=Y+u+30.                  (8.1)

All dimensions/caps precede access. ForY<=n/2,usem<=2a<=n/4,
u+16<=n/4 at48 and thereafter. In analysis,Y+E+6=Theta(a).

For block fields also use b0=floor(log2n),Lblk=ceil(n/b0).
Herebase>=4u andbase>=32 atn=2^48 and thereafter:base>=t/2 and
t/2 grows exponentially faster than4u. Since dl<=2base,
g_w<=ceil(log2(2base))<=base/4 andb0<=u<=base/4.
Thus m+g_w+b0<=m+base/2<=H,as required for theh-unused-bit fields.

## 9. BATCH(supplier, B, R, h=1)

Input: a supplier of leaf qubits with known labels,whose ideal accepted
values are independent uniform[0,2^(B+h)),1<=h<=b0,1<=B,B+h<=n.
VROOT(supplier,B,h,d) builds ONE root of outputwidthd in{1,r}. Allocate
nonroot lambda_i as8,lambda_m=d,and budgets under the changed root
capacity. Start with all quantum workzero. Count selected source calls;
if callCt+1 would be needed,stop,reset all work and returnmissing.
Rejected suppliers and failed merges count. Completion returns the
root index and its high-part table; it is immediately decoded/measured,
then ALL work is reset before any new root call. No earlier source or
quantum root persists between calls. Source parameters are fixed within
a root; retry of a missing fine root keeps those same parameters.

BATCH(supplier,B,R,h=1) for COARSE stages callsVROOT with d=1 R times.
A completed root is immediately measured in a fresh fairX/Y basis,
recording(W,beta,Z); a missing root contributes scorezero. Reset all
quantum work between roots. Stage parameters stay fixed until allR
classical records exist,then scores and the centre are updated.
For cost bounds only putD_R=C_R=R*Ct; there is no separate demand guard.
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
evaluated depth-first. At its final MERGE use lambda_m=d. VROOT returns this one index after at mostCt selected calls.

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
accepted values below2^(B+h). Also each actual root uses at mostCt
source calls. Consequently

    |W_a|<=2^h Ct<=2^(Y+h).                        (9.2)

Since2^(m+g_w)<2dl2^m<=Ct,m+g_w<=Y. All high fields obey
w_i<=D_src+m+g_w<=n+Y<=3n; wrong-label branches obey these dimensions
because accepted stored labels still belong to the same finite ranges.
The common prefix cancels in every W_a. No full logical label table is
reconstructed. For a fine root the2^r<=2n^5 high rows are explicitly stored.

Coarse decoding usesh=1; block decoding usesh=b. No root-cost bound depends onh.

Lemma9.1 (clean capped-root law). In the ideal-label reference process,
each root is missing with probabilitydelta<=6/65536<1/8192. The cap
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
calls<=6dl2^m. Markov bounds cap failure by6/65536. Almost-sure finite
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

wherehd=|Sp|+|Sm|>=1,as used by the unchanged coarse bootstrap.

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

Direct final-block lemma. One final two-adic block withwd=b instead uses
Kp independent uniformW=kk and single qubits of exact phase2pi Wv/2^b.
Fresh fair basisbeta andoutcomeZ scoreeverya<2^b by
sum Z*tab_beta(Wa/2^b). Exact-trig mean true1/2,false0,table error<1/625;
true-false mean>1/4,pair range[-3,3]. Hoeffding gives wrong candidate
probability<=exp(-Kp/288). Union over at mostn candidates gives2^-30/n.
Pick the smallest maximizing residue,including all harmful ties.
All direct qubits are measured/reset immediately.                      (10.5)

## 11. Odd part: bootstrap followed by signed near-parity

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every coarse stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (m + 10u + 100), u=ceil(log2n).                                              (11.0)

Put J_full=min{j>=0:2^(j+3)>2M} and J0=min(J_full,Y+5+E).
Run the following coarse stages j=0,...,J0, each with Kc roots.
There are at most Y+6+E stages, and at most log2 M stages.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. To supply one leaf qubit, repeat until accepted: acquire a fresh
copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard), and on acceptance apply X to the
control. The individual root's acquisition cap applies. In the ideal run accepted labels are i.i.d. uniform on [0, 2^dn), and each copy
is accepted with probability 2^dn/N > 1/2. The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(dn-1) W th = W 2^(dn-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),           (11.1)

so a root is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known frequency f = 2^j W.

Measurement. Run BATCH(supplier,dn-1,Kc) for stage j,with IMMEDIATE root measurement and complete quantum reset between roots as9. Its classical records have missing scorezero. For a complete clean reference record,
E Z_i = cs_(beta_i)(f_i theta) with f_i = 2^j W_i.

Candidates. Put P_j = j + Y + 8 and identify an integer c with the point zeta = c/2^(P_j) on R/Z. Stage 0 uses every c in
[0, 2^(P_0)). Stage j >= 1 uses every c within circular distance rad_j = 2^-(j+2) of the previous center z_(j-1); both
z_(j-1) and rad_j are multiples of 2^-(P_j), so the arc endpoints are candidates. There are at most 2^(Y+8) candidates.

Score. For each candidate, with exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

Enumerate candidates in increasing order, keeping the K residues (f_i c) mod 2^(P_j), updating each with one addition per
step, and keep a running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have fixed lengths.

Lemma11.1. On a correct past each clean reference coarse stage chooses
a centre within2^-(j+3) oftheta,except probability2^-20/n.
Proof. Root records are independent fresh clean capped roots for fixed
stage parameters. Exactscorexi=Z*cs_beta(f*zeta) oncomplete roots andzero
onmissing lies in[-1,1]. Fresh basis averaging gives
(1/2)cos(2pi f(theta-zeta)). Nearest grid point error<=2^-(P_j+1),
|f|<=2^(j+Y+1),so its mean>=(1-delta)(1/2)cos(pi/128).
For a far candidate,correctpast and the arc give2^j|theta-zeta| in[1/8,1/2].
The conditional completed characteristic bound10.2 gives mean
<=(1/2)cos(pi/8). Thus reference near-far gap>379/10000-delta/2.
The rational checks cos(pi/128)>=1-(22/7)^2/(2*128²),
cos(pi/8)<923881/1000000 andsqrt2<141422/100000 establish this margin.
Hoeffding bounds each score's deviationKc/64 by2exp(-Kc/8192).
Table error costsKc/625 per candidate. The exact inequality
379/10000>2/64+2/625+1/16384 leaves a strict gap. Union over at most
2^(Y+8) candidates gives2^(Y+9)exp(-Kc/8192)<=2^-20/n by8.1.
Missing probability is included in means,not union bounded across roots.
All laws here are unconditional ideal-label clean reference laws;5
bounds disagreement with the physical extraction process. QED.

The hypothesis for stage j+1 is the conclusion of stage j. There are at
most n stages, so all coarse conclusions hold except with probability
2^-20. If J0=J_full,
round M z_J0 to the nearest integer modulo M, obtaining s1 as before,
and skip the fine stages. The error is strictly below1/(2M).

Otherwise J_full>Y+5+E. Since j=Y+5+E does not satisfy the defining strict
inequality, M>=2^(Y+7+E). Put the known integer

    chat=floor(M z_J0+1/2) mod M,
    R0=M2^(-Y-8-E)+1/2.

On correct coarse conclusions the circular error of z_J0 is at most
2^(-Y-8-E). Therefore a unique signed lift t0 congruent to s1-chat
modulo M satisfies |t0|<=R0. Also R0>=1, R0/M<=2^(-Y-7-E)<1/2.
Indeed rounding adds at most1/2, and M>=2^(Y+7+E) bounds that term
by M2^(-Y-8-E). This is a mathematical bound, not a measurement of t0.
It also proves |t0|<M/2, including rounding and circular wraparound.

Fine blocks. Initialize low=0,j=0. Whilej<n putb=min(b0,n-j),B=dn-b.
The large-M branch has M>=2^(Y+7+E),dn-a2=floor(log2M)>=Y+7+E andY>=m>=b0,
so B>=a2+1. Compute gamma=2^(B-a2) modM and K0=(-2^b)^(-1) modM
as the representative in[1,M). Both are units becauseM is odd. Define

    J=(2^b K0+1)/M.

This is an integer,1<=J<=2^b,andJ is odd because its numerator andM
are odd. Compute by extended Euclid and CRT a unitalpha moduloN with
alpha=1 mod2^a2 and gamma*alpha=K0*2^(-j) modM.
Setcj=(chat+low) modM. On each fresh copy applyShift_cj thenMult_alpha,
runLE,accept iffk<2^dn,and applyX to the control. Accepted labels are
uniform on[0,2^dn)=[0,2^(B+b)),acceptance>1/2; every rejection counts.
Request one completedVROOT(supplier,B,h=b,d=r),retrying missing roots under the global fine attempt cap13. On a correct past,t_j=(t0-low)/2^j is integral.
For each output indexa,the exact transformed root phase(relative to index0) is

    exp(2pi i 2^B W_a alpha(s-cj)/N)
      =exp(2pi i K0 W_a t_j/M)
      =exp(2pi i J W_a t_j/2^b) exp(-2pi i W_a t_j/(2^b M)). (11.2)

The unknown two-adic component cancels sinceB>=a2; equality uses the
CRT relation and s-cj=2^j t_j modM. The final small phase is a physical
consequence of modular source transforms,not a synthesized rotation.
Apply the vector measurement in qudit_decoder.md with thisJ,b; let its outputbea. Reset all root and measurement work before anotherVROOT.
Updatelow+=a2^j,j+=b. These rules also specify every incorrect history.

On a correct past |t_j|<=R0. The invariant follows fromR0>=1 and
|(t_j-(t_j mod2^b))/2^b|<=(|t_j|+2^b-1)/2^b<=R0,includingnegativeintegers.
By9.2,|W_a|<=2^(Y+b),so the phase perturbation in11.2 has magnitude at most

    2pi 2^Y R0/M<=2pi*2^-E/128<1/(16n^4),

usingpi<4,E=4u>=4log2n andR0/M<=2^(-Y-7-E). The vector lemma10 bounds each wrong completed
block by2/n^4. After at mostLblk=ceil(n/b0) correct blocks,low=t0 mod2^n.
Recover the signed n-bit integer t=low iflow<2^(n-1),otherwise low-2^n.
Since|t0|<M/2<=2^(n-1),this equals t0. Output s1=(chat+t) modM.
Coarse failure,good-label errors and global attempt-cap exhaustion retain separate budgets.

## 12. Two-adic part by blocks

Ifa2=0 puts2=0. Otherwise initializeg=0,s2low=0. Whileg<a2,
putwd=a2-g,b=min(b0,wd),sh=(s1+M*s2low) modN. On a correct past
rem=(s2-s2low)/2^g is integral modulo2^wd. A supplier acquires a copy,
appliesShift_sh,runsLE,appliesX,and useslabelkk=k mod2^wd. Ideallykk
is uniform on[0,2^wd) because2^wd dividesN,and its phase is
exp(2pi i kk rem/2^wd). No rejection is needed.

Ifwd>b requestone completedVROOT(supplier,B=wd-b,h=b,d=r),retrying
missing attempts under13. Each vector entry phase is2pi W_a rem/2^b.
Apply qudit_decoder.md withJ=1 to choosea. Ifwd=b use the direct final
single-qubit block lemma10.5,withW=kk andKp qubits. In both cases reset
all quantum work,update s2low+=a2^g,g+=b. There are at mostLblk blocks
andone direct block. On correctpast the vector phase perturbation iszero,
so each vector block fails with probability<=2/n^4. Correct blocks yield
s2low=s2. Output(s1+M*s2low) modN. Every incorrect history still has
specified finite dimensions,labels,measurements and modular updates.

## 13. Actual complete algorithm and reference-core error budget

Finite branch(n<2^48). Putk=n+10,Qcap=N*k,Qbank=1024*Qcap. Prefetch and
shuffle as18. For EVERY candidatec=0..N-1,use its predetermined block ofk
consecutive bank slots,applyShift_c,measure the control inX,and record
whether all outcomes wereplus. Test every block in full; no early stop,
skipped candidate or adaptively shifted block boundary is used. Output the
first candidate whose block was allplus,or0 ifnone. Unused bank slots are
reset/released without conditioning the output on their measurements.
Section18 proves robustness of this branch uniformly,not a clean-only premise.

Main branch(n>=2^48). Compute all parameters,a2,M,dn,J_full,Ct,Y,E,r
before access. Set the GLOBAL fine-vector attempt capA=4Lblk and

    Qcap=Ct*(Kc*(Y+6+E)+A)+Kp,Qbank=1024Qcap.

SizeLE confidence withQcap. Run11 then12 with MICROTAKE. At mostY+6+E
coarse stages each run exactlyKc capped1-qubit roots. Each fine block
requestsone completedr-qubit root,retrying missing attempts with identical
current supplier parameters. Every fine VROOT started increments ONE
global attempt counter; before attemptA+1 ABORT with output0. This is
shared across odd andtwo-adic vector blocks,not a cap per block. Every
completed vector is measured and all work reset before the next attempt.
There are at most2Lblk desired completed vector roots andat mostone
Kp-qubit direct final block. Thus the displayedQcap bounds selected calls
on EVERY branch. On success/ABORT record output,reset work,pad exactQcap
microbanks and return. Every raw,unused andpadding copy is counted.

Clean reference analysis. First use an ideal-label clean reference.
The actual clean physical reference agrees with it until the first clean
LE error,whose probability is at most2^-10 by5.1. This is an unconditional
first-error comparison,not conditioning a whole run on extraction success.
Each fine attempt is missing with conditional
probability<=delta<1/8192. If the total desired completions are not reached
inA attempts,at leastA/2 aremissing. Extend with analytical ghost attempts
if the actual schedule stops earlier. For any specifiedk missing positions,
iterated conditional expectation gives probability<=delta^k. Union over
at most2^A subsets gives

    Pr(global fine cap abort)<=(4delta)^(A/2)<=2^(-11A/2)<=2^-22.

Parameters may change between completed blocks; the missing bound is
uniform given any prior history. Conditional completion retains the
unused-top laws,so vector failure<=2/n^4 per block,even if missing roots
were retried. All vector errors total<=4/n^3<2^-20 on this main range.
Direct block errors<=2^-30/n. Coarse errors<=2^-20 globally; all clean
LE errors<=2^-10. Sum,including the fine attempt cap,is below2^-8.
This proves actual main failure<2^-8 under the independent-ideal-copy
promise. No law is conditioned on all physical label extractions succeeding.

## 14. Resource bounds on every branch

Every root and enumeration loop is capped. Letl=log2n,a=n^(4/9),
t=n^(5/9). We have m,Kc,Y+E+6=Theta(a),Kp=Theta(l),dl,H=Theta(t),
Ct=Theta(t2^m). Coarse roots numberO(a²),fine attemptsO(n/l).
Since a²/(n/l)=l/n^(1/9)<=2 at l>=48 (the ratio decreases
thereafter,its logarithmic derivative is1/l-ln2/9<0),
all root calls numberO(n/l). Therefore,including every rejection,
failed/capped attempt,direct source andpadding,

    Qcap=O((n^(14/9)/l)2^m).                      (14.0)

Quantum workspace. At mosttwo retained core indices per level,each<=H,
useO(n) qubits by8.4. Leaf,source/data,modular/LE,lookup/controller scratch
andone active root addO(n),with wires reset/reused. Each MICROTAKE holds only
1024 raw(n+1)-qubit copies and10 coin qubits(also reusable). Hence the main
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

Work. A leaf costsO(n2^dl) core steps anddl accepted qubits.
At heighti,a merge attempt costsO(n2^(dl+i+1)) and consumes2^(i+1)dl
canonical leaves not reused by another attempt at that level. A partial
leaf at cap is charged fully. Summing overlevels gives
O(nQcap2^dl(m+1)/dl) core tree steps on EVERY branch,where
(m+1)/dl=O(a/t). Multiply by address widthO(H+logQcap)=O(t) to obtain

    T_tree=O((n³/l)2^(m+dl)).                    (14.1)

Indeed n*(n*t/l)*a/t*t=n²at/l=n³/l. Confidence has
logQcap=O(m+l)=O(a); each selected extraction costsO(n²a) core steps.
All extraction/source/controller work has only a polynomial factor times
2^m,and is absorbed by14.1 because dl=Theta(t) grows faster thanlogn.
Coarse scoring usesO((Y+E)Kc*n*2^Y) core steps. Since2^Y<=2Ct and
Y+E,Kc=O(a),this is polynomial inn times2^m,also absorbed.
There areO(n/l) root calls; initializing compressed frames costs
O((n/l)H²2^H),bounded by14.1 becauseH=m+dl-s0-1.
CRT/parity,signed updates,fixed loops,resets andall source charges count.

qudit_decoder.md's explicitly enumerated polynomial-size tables,gate
synthesis,finite precision andcircuits cost fixed polynomial work/classical
bits percall andO(logn) qubits. They are absorbed by14.1,H2^H andO(n),
with every address charged and no oracle. The main1024-copy microbanks
and exact10-bit choices costO(nQcap) core steps and polynomial bookkeeping;
address widthO(t) still leaves these absorbed by14.1. Idle core wires
count throughout prefetch. All raw unused/padding copies are counted,
and all caps,synthesis precision and dimensions apply after earlier errors.

## 15. Exact uniform envelopes

Put F(n)=n^(5/9)+(1/2)n^(4/9)-n^(1/9),a=n^(4/9),t=n^(5/9),l=log2n.
Since m+1>=a+1 and1/(1+x)<=1-x+x² forx>=0,

    n/(m+1)<=t-n^(1/9)+n^(-1/3)<=t-n^(1/9)+1,
    H<=n/(m+1)+m/2+1<=F(n)+3,
    m+dl=H+kappa+2<=F(n)+(4/9)l+8, m<=a+1.

The remainder power-1/3 is nonpositive. Substitute into14 withH<=2t.
All ceiling and slack factors are explicit in the complete joint envelopes

    T=O((n^(31/9)/log2n)2^F(n)), S_C=O(n^(5/9)2^F(n)),
    S_Q=O(n), Q=O((n^(14/9)/log2n)2^(n^(4/9))).

Time/classical indices are5/9,copy index4/9,quantum0. The exact negative
term is retained. Finite n<2^48 exhaustive inputs change only uniform outer
constants,never main-only guards. At n=1 logarithmic envelopes usepositive n=2 values.

For the finite branch,actualprefetched bank quantum allocation is at most
1024N(n+10)(n+1)+O(n). For fixedC0=2^48 andn<C0,an absolute bound
C_f*n withC_f=2^20*2^C0*(C0+100)^2 suffices. Fixed-range work,copies
andclassical bits have absolute outside constants too. The success
proof is separately supplied in18 and is not absorbed into a constant.

## 16. Error tolerance

The fifth claim is epsilon(n)=0 under the exact clean-input context in
submission.json. It promises independent ideal coset copies throughout.
All four worst-case bounds and success above are joint under that promise.
Zero asserts no positive resilience or impossibility result.

## 17. Scope

This clean configuration has time/classical growth index5/9 andcopy4/9,
with a retained negative exponent correction and lower logarithmic work/
copy factors. It does not meet the challenge's stronger2^O(n^(1/3)) goal,
claim a new PGM,an optimum,physical execution or small outer constants.
Its uniform finite prefix and all source/lookup/synthesis costs are counted.

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
