# COVER7-186: seven-qubit weighted-cover recycling before linear-merge collimation

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), and let a0 = 6189/5000.
The single algorithm COVER7-186 below receives N in binary and fresh independent copies of
rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-7 > 2/3.
On EVERY execution branch (every failure, discard and abort included) it satisfies jointly

    T = O(2^(a0 sqrt n)),  S_C = O(2^(a0 sqrt n)),  S_Q = O(2^(a0 sqrt n)),  Q = O(2^(a0 sqrt n)).

All constants are absolute. Each of the four envelopes has growth index exactly 1/2
(Section 15). The fifth claim is the clean-input tolerance 0 (Section 16). The sharper
main-branch bounds, from which these follow, are in Section 14: T = O(n^6 2^(e sqrt n)),
S_C = O(n^3 2^(e sqrt n)), S_Q = O(n^2 2^(e sqrt n)) and Q = O(n^3 2^(e sqrt n)) with
e = 12377/10000 < a0. The envelope coefficient is a fixed exact rational; no hidden
constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with
  s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^60:

    r = ceil(sqrt n),   ell = ceil(757 r/2000),   m = ceil(448 r/625),   dl = ceil(5209 r/10000),
    kappa = ceil(log2 m) + 1.

So there are ell COVER7 LEVELS, a collimation tree of depth m, and leaf tables built from
dl qubits. Since r >= 2^30 these satisfy ell >= 2, dl >= kappa + 1, 2^kappa >= 2m.

## 1. Complete provenance and scope of the new construction

This complete source framework directly adapts kshitij-hash TRIAD-125,
actualf5b375dd-1e5c-4728-95dc-b855b2dc5827,archive
965917f88ec25ccab3d9ce78e07c717a1590a54f,originalproofSHA256
4802f6c40f92567f239d216c49e6e9e1370b8a3af1c62d6524cc84c901d23f8d.
The peer introduced its three-qubit overlapping projector instrument,
exact coin-erasure dilation,unchanged returned inputs and improved
poolyield. Those ideas motivate the NEWseven-qubit weighted cover7
below. The new fourcellfamilies,multiplicities,dyadicdilation,yield,
finite identitytrialcap and integerprofile are supplied inFULLhere;
they are not attributed to the peer's different instrument or verdict.
The source/LE/transforms/linearMERGE/fullmodulus decoders in2-6/11/12
are retained,with explicit newcaps/couplings asstated. Lowfield10 and
pool/tree9 are adapted for the newcells with their full proofs supplied.

The peer's contextual credits remain:qzvHPC-127 actual
2aad498c-d5e9-4f64-a222-3b2f7f961738,AdamGagolCS1 actual
f1481815-9577-4990-abe3-7b79fa5d9284,sparievPSieve actual
4256e671-97b0-4f84-82ce-12aeee17224e,and0xplemonadeCYC1 actual
7a4cecdc-7941-4027-8c95-8520de9fbcf3 as precedentforphase-independent
overlapping instruments. Kuperberg's SIAM J.Comput.35(1),2005,and
arXiv:1112.3333 are contextualreferences carried through the peer.
No missingpaper,priorverdict,novelty/priority or generalmeasurement-
optimality assertion supplies a premise. The finitecover was found by
an exploratory linearprogram and independently reconstructedexactly;
its complete identity,not the numericalsolver,proves its usehere.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates on pooled qubits are classically addressed through this charge; there is no
quantum-addressed memory and no QRAM. A source acquisition costs n+1. Hence

    T <= (number of core steps) * (1 + ceil(log2(S_C+S_Q+2))) + (n+1) Q.          (2.1)

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
to denominator 2^20. This is a fixed finite computation, an absolute constant, not advice.

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

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(sqrt n) (Section 14),
this is O(n^(5/2)) core steps per call, with O(n) quantum scratch and O(n) classical bits.

Probability-onlyidealruns. First replace everyLEoutputby its latent
label;coupling5.1 costsatmost2^-10. Thenremoveonlythe internal
identitytrialcaps ofCOVER7 (7.2);its rejectionterminates almostsurely
and couplingto the cappedlabelidealrun costsatmost2^-128 overthe
entirealgorithm. Keep every supplier,pool,tree andacquisitioncap.
All following probabilitylemmas refer to this analysisidealrun unless
stated otherwise. Every resourcebound concerns the ACTUALfinitecap
program,also onbadLE/identity-abort branches. No unboundedideal
resource or conditioning on favorablecap outcomes is used.

## 6. Phase vectors and the linear merge

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical label table
lab[0..2^lam). In the ideal run its state is 2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a
global phase, for a fixed real th. Labels are nonnegative integers. The vector is COLLIMATED TO p
if all lab[x] are congruent modulo 2^p. Labels are stored in full, in fixed fields of 3n bits, which
suffices by Section 9 (label bound).

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x] into a clean w-bit
register, controlled by a lam-qubit index x. For each row x0 it computes the flag [x = x0] with a
Toffoli chain on O(lam) scratch, applies CNOTs from the flag to the output bits where tab[x0] has a
1, and uncomputes the chain. Indices outside [0,E) give output 0. The circuit is its own inverse,
has O(E (lam + w)) gates and O(lam + w) qubits, and is generated by reading each table bit once.

### 6.2 MERGE(X1, X2; p, b, lam'), for b >= 0

Precondition: X1 and X2 are phase vectors from disjoint sets of qubits, both of length 2^lam,
collimated to p, with index registers x, y and tables al, be. Let cA = al[0] mod 2^p,
cB = be[0] mod 2^p, car = floor((cA + cB)/2^p), aa[x] = floor(al[x]/2^p) mod 2^b and
bb[y] = floor(be[y]/2^p) mod 2^b. Then bits p..p+b-1 of al[x] + be[y] equal (aa[x] + bb[y] + car)
mod 2^b. (If b = 0 the residue registers below are empty and e = 0.)

1. LOOKUP aa into a fresh b-bit register Ru and bb into Rv. Add Ru + Rv + car (mod 2^b) cleanly into
   a fresh Rz, and clear Ru and Rv by repeating both lookups. Measure Rz, obtaining e, and reset Rz.
2. Classical. Let S_e = {(x,y) : aa[x] + bb[y] + car = e mod 2^b} and sz = |S_e|. Merge-sort the
   indices y by key (bb[y], y) into order[]; pos[y] is the position of y. For each x the partners y
   form one contiguous run of order[], the class (e - car - aa[x]) mod 2^b; find its start lo[x] and
   length cnt[x] by binary search. Put off[x] = sum_(x' < x) cnt[x'] and
   rank(x,y) = off[x] + pos[y] - lo[x], a bijection from S_e onto [0, sz). If sz < 2^lam', declare FAIL.
3. Let R have 2 lam + 1 bits. LOOKUP pos into Rp and Dx[x] = (off[x] - lo[x]) mod 2^(2lam+1) into Rd.
   Add Rp + Rd (mod 2^(2lam+1)) cleanly into a fresh R, and clear Rp and Rd by repeating the lookups.
   On S_e, R = rank(x,y).
4. Measure bl = floor(R / 2^lam'). If (bl+1) 2^lam' > sz, declare FAIL.
5. Classical. For v in [0, 2^lam'), find the unique (x_v, y_v) with rank bl 2^lam' + v, in one scan
   over x with running offsets. Apply LOOKUP v -> (x_v, y_v) on the low lam' bits of R, XORing into the
   registers x and y, which become |0>. Reset the high bits of R from their known value bl.
6. Output the low lam' bits of R as the index register, with table lab[v] = al[x_v] + be[y_v].

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

Cost. Write L = 2^lam, L' = 2^lam'. With lam, b = O(sqrt n): nine lookup passes of O(L + L') rows with
O(sqrt n)-bit fields; O(L lam) comparisons of O(sqrt n)-bit keys; O(L) binary searches; O(L') additions
of 3n-bit labels. In total O(n (L + L')) core steps. Quantum scratch is O(sqrt n) beyond the index
registers. Classical scratch is O((L + L') n) bits.

## 7. COVER7: exact seven-qubit overlapping-cell recycling

A labeled qubit has table(t0,t1) and phase differenceDel=t1-t0.
It is collimated top ifDel is divisibleby2^p. Maintain the same
pool product invariant as the peer:conditionalon latentlabels and
past outcomes,every pool qubit is its recorded equal-magnitude phase
qubit,in tensorproduct with all other pool/source/reference registers.
Leafqubits satisfythis by3/5. The instrument below preserves it.

### 7.1. A complete rational cover and its exact instruments

On seven computational bits x,choose G subset{1,...,7} ofsizeg and
patternb in{0,1}^G,identifying b with1-b. A cell is
 S(G,b)={x:x_G=b or x_G=1-b},with other coordinates free.
Pi_(G,b) projects onto this cell. Use the following four families;
k is the numberofones in a canonicalpattern,and w is PER-CELLweight:

 type(g,k)  numberofcells  weightw   good?
 (2,1)          21         17/210    yes
 (4,0)          35          1/35     no
 (6,1)          42          1/70     no
 (7,2)          21          2/105    no.

For(2,1),thetwo oppositepatterns identifyone cell perpair. For the
other types,k<g/2,so choosing thek onepositions uniquely selects a
pattern/complementcell. These are fixed finite families,not advice
or an input-dependent search. The proposed normalized instrument
has one Krausoperator sqrt(w)*Pi_cell percell.

Completeness is an exact finiteidentity. By permutation/complement
symmetry,it suffices to count cellscontaining an input ofHammingweight
t=0,1,2,3. In the displayed familyorder,the counts are
 t=0:(0,35,0,0), t=1:(6,15,6,0),
 t=2:(10,5,2,1), t=3:(12,1,0,0).
Multiplication by the integerweights(17,6,3,4) gives210 in EACHrow.
Thus sum_cell w Pi_cell=I on ALLseven-bitinputs,not only a promise.
The countformula is choose(t,k)choose(7-t,g-k) plus its complementary
term when2k!=g;at2k=g count onlyonce. This also directly checks all
128basisinputs without a statistical assertion.

For a product of equatorial phasequbits,eachbasisamplitude has
modulus2^(-7/2). Cellsize is2^(8-g),so that cell's outcomeprobability
is w*2^(1-g),independentof everyphase,label,secret andpast. Summing
within types gives EXACTprobabilities
 p_good=17/20, p_(4,0)=1/8,p_(6,1)=3/160,p_(7,2)=1/160.
They sumto1. Projecting theg selected qubits onto b or1-b leaves
one two-term phasequbit;the other7-g qubits retain EXACTLY their
inputstates and identities,in product with theoutput and untouched
reference. Its outputtable is
 (sum_(j inG)t_(b_j)^j, sum_(j inG)t_(1-b_j)^j).
Choose a knownpivotv inG. For eachotherj inG,applyCNOT v->j and
thenXifb_j xor b_v=1;thenapplyXto v ifb_v=1. All otherg-1 groupwires
becomezero;v is theindexalpha selectingpatternb then1-b. This clean-
wire conclusion holds for EVERYstate supportedon thecell,including
arbitrary entangled references. No unknown state is cloned.

For equalkeysDel mod2^(p+c),thegood(2,1) signs balance,so its
outputdifference is divisibleby2^(p+c). All recycledtypes preserve
oldp:their difference is a signed sum of theinputDel values. Every
outputentry is a sum of entries from disjoint inputtables. The maps
alpha->b xor alpha on selected disjointleafcoordinates are injective;
unmergedqubits retain their disjointleafsets. Thus the product and
incidence invariants used in9/10 persist. Everylabel remains a full
positive sum of at mostC0 initial labels,not a truncated signedword.

### 7.2. Exact Clifford+T realization with finite identity rejection

The rational weights do NOTrequire a non-Clifford rotation oracle.
Give each individualcell respectively17,6,3,4 distincttokens. There
are21*17+35*6+42*3+21*4=777tokens. Add46globalidentitytokens. The
full outcomeIDj has823possibilities and10qubits suffice. Eachbasisx
belongs to exactly210nonidentitytokens plus46identitytokens=256.
Order all777nonidentitytokens first,then the46identitytokens.

Initialize an8-qubitcoinr and10-qubitj tozero. ApplyH to everycoin
bit. The fixed finite Booleanfunction f(x,r) is ther-th containedtoken
in that order,forr=0,...,255. XORf intoj. Let h(x,j) be the rankofj
among tokens containingx (arbitraryfixed0 oninvalidpairs). XORh into
r,clearingit tozero. Uncompute all Boolean scratch,thenmeasurej and
reset its knownbits. On a nonidentitytokenapplythe preceding group
cleanup;on an identitytokenleave all seveninputs unchanged.

Both f andh are complete Booleanfunctions on15 and17inputbits.
A uniform finitebitcode implements each by looping over its fixed
classicalinputpatterns,computing a controlled equalityflag with a
NOT/Toffolichain,copying the relevantoutputbit,thenuncomputing the
flag. f targetsj;h targetsr and doesnot user as aninput. Thereare
at most10*2^15 and8*2^17 outputpatternterms,respectively. At most
5*17+1 elementaryNOT/CNOT/Toffoliactions perterm gives fewerthan2^32
gates,with atmost32 reusable scratchqubits. Fixedclassicalcounters
have atmost17bits. Code generates these gates online,without a
stored truth-table history,unknown reads or quantum-addressedRAM.
Classical truthfunction evaluation/gateemission also has a fixedfinite
constant-template bound:atmost2^17 patterns,10outputbits,and a serial823token
scan with fixed7/10-bit arithmetic perpattern are covered by2^64
templateactions pertrial. AllowingfullO(n)-bit operand/known-wire
staging,a conservative2^64*n coresteps pertrial covers both
evaluation andemission. No growing classicaltruth table is allocated.
Toffoli has the exact finiteClifford+T completion of2.

For arbitrary jointinput sum_x |x>|R_x>,the unitary beforemeasuringj
is EXACTLY
 sum_x |x>|R_x>|0>_r (1/16)sum_(j containsx)|j>.
Hence eachnonidentitytoken's Krausoperator isPi_cell/16;eachidentity
token's isI/16. Coin andscratch arezero on everybranch. This proves
the entire instrument with arbitraryreferences bylinearity. The total
identitychannel has probability46/256=23/128<1/4 on EVERYinputstate.
Conditionedon a nonidentitytoken,the aggregatedpercell weights are
17/210,6/210,3/210,4/210,exactly7.1. Releasedgroupwires areclean.

A macrotries this finite instrument until a nonidentitytoken,atmost
 Ltry=Y+ceilLogn+64
trials. If all areidentity,ABORT thebatch and releaseits pool. This
is an ACTUALfinitecap,not unbounded repeat-until-success work. Y and
Ltry arepublic beforeLE. Coupling to an analysisrun with unbounded
identityrejection costs atmost2^-128 in totalfailure:perlevelthere
are atmostCin/2 nonidentitymacros plusone finalfailedcall,atmostCin
calls sinceCin>=2. Section8 givessum_i Ci<=2C0 andthereare<=nbatches,
so atmost2nC0calls. WithC0<=2^Y,the unionbound is
 2nC0*(23/128)^Ltry <=2^(1+ceilLogn+Y-2Ltry)<=2^-128.
Unboundedidentityrejection terminates almostsurely and has normalized
instrument7.1. It is used only in probabilityanalysis. Everyresource
bound is for the ACTUALfinite-trial program,even on aborts/badLEinputs.
No trial acquires a sourcecopy. Ltry=O(sqrt n),and all returned input
identities,reset/discard channels and cleanup work count.

### 7.3. COVERLEVEL and an all-label yield certificate

COVERLEVEL(pool,Cin,p,c) takesCin labeledqubits collimatedtop. Put
E=2^c. KeepLIVE andOUTPUT arrays. Repeat EXACTLY3(Y+1) rounds:
sortLIVEbyDel mod2^(p+c),with originallogicalties;cut each equalkeyrun
into consecutivegroups ofseven. At mostsixqubits perkey areungrouped.
Run the cappedmacro7.2 on eachgroup in scanorder. Goodoutputs append
toOUTPUT;all recycledoutputs and unmergedqubits go to the nextLIVE.
Within eachgroup append a recycledpivot first if present,thenunmerged
inputs in their originalgrouporder;goodoutputs appendin processingorder.
If a macroABORTs,ABORT thebatch. Afterthefixedrounds,reset/releaseLIVE.
COVERLEVEL outputqubits are collimatedtop+c;LIVE retainedoldp.

For yieldonly,work in the analysisidealrun5 withoutidentitycaps.
Each macroreducesLIVEby a costC in{2,3,5,6},with goodindicatorG in{0,1}.
It preservesproductstates and has the fixedconditionaltypelaw7.1 given
EVERYpast andalllabels. Thus pairs(G,C) form an i.i.d.sequence at all
reachedmacros,with
 p=E G=17/20, mu=E C=353/160, mu/p=353/136.
Extend it afterstopping by independentphantomtypes for this probability
argument only. The whole sequence is i.i.d.;no actualalgorithm uses
those phantomtypes or obtains freephysicalwork from them.

A round onLlivequbits leavesu<=6E ungrouped. Everygroupreturnsatmost
fiveLIVE,so Lnew<=(5L+2u)/7<=(5L+12E)/7. Consequently
 L_j-6E<=(5/7)^j(Cin-6E).
Since(5/7)^3<1/2 andCin<=2^Y,after3(Y+1)rounds L_end<=6E by
integrality. TotalroundLIVEvisits are atmost(7/2)Cin+6rounds*E.
For actualmacrocountA,the deterministic identityis
 sum_(j<=A) C_j=Cin-L_end.
AssumeE<=Cin/(64ell),ell>=2. ThenA>=(Cin-6E)/6>=Cin/7 andA<=Cin/2.

Seteta=1/(64ell). Hoeffding forG in[0,1] andC in[2,6] gives,for each
fixedprefix j,lowerGdeviation<=exp(-2eta²j),upperCdeviation
<=exp(-eta²j/8). Unionover ALLprefixesceil(Cin/7)<=j<=Cin/2 gives
 failure<=2Cin*exp(-Cin/(2^18ell²)).
This uniformprefix event covers the randomA without conditioningonit.
Outsideit,the numberSofgoodoutputs satisfies
 S>=(p-eta)A >=[(p-eta)/(mu+eta)]*(Cin-6E).
As1/p+1/mu<2,the ratio(p-eta)/(mu+eta)>=(p/mu)(1-2eta).
Using6E/Cin<=6/(64ell),weconclude
 S>=(136/353)(1-1/(8ell))Cin
  >=136(ell-1)Cin/(353ell).                              (7.2)
No independence between goodindicator and its ownremovalcost is used.

At allmainlengths8,Cin>=2^m,m>=r/2,ell<=r,Y<=2r. Thusln(2Cin)<=3r.
The inequalityr/2>=20+3log2r implies2^(r/2)>=2^20r³,so
 ln(2Cin)<=3Cin/(2^20ell²).
Thereforethe precedingfailure is atmost
 exp(-Cin/(2^20ell²)).                                 (7.3)
Both cutoffinequalities hold atr=2^30 and their continuousmargins
increase. This is a uniform all-label certificate,not a simulation
or an empirical independence assumption.

Cost. The source's fixed7-qubit macro has constant<2^32 quantumgates and
a conservative2^64*n totalcoresteps pertrial,includingknown-wire
staging andgateemission,
atmostLtry=O(sqrt n)trials,andO(n) fulltable additions/record work.
ThusO(n^(3/2)) coresteps permacro is a conservative allowance.
Sorting a round costsO(L n logCin). The totalLIVEvisit bound and
E<=Cin/(64ell),rounds=3(Y+1)<=18ell give atmost6Cin visits perlevel.
Hence onelevelcostsO(n^(3/2)Cin),withconstantcurrentmacroancillas
beyondthepool. These costs count actualfinitecap failures too.

## 8. Exact schedule,capacities and bit allocation

DefineC_ell=2^12*n*K*2^m*dl,withKfrom11.0,and backwardsi
 C_i=ceil(353ell*C_(i+1)/(136(ell-1))).
Letq=353/136 andrho=q*ell/(ell-1)>=q>2. Then
 Ci>=q^(ell-i)C_ell>=q^(ell-i)2^m,                 (8.1)
 C0<=rho^ell(C_ell+1)<=2rho^ell C_ell<=8q^ell C_ell. (8.2)
Indeed the accumulatedceil errors sumto atmostrho^ell since
rho>=2,and(1-1/ell)^(-ell)<=4 for allell>=2. PutY=ceilLogC0.
EveryCOVERLEVELuses3(Y+1)rounds andLtry=Y+ceilLogn+64 per macro.

Here are exact rational logarithmbrackets,not a realarithmeticoracle:
 172/125<log2(353/136)<13761/10000.
They followfrom the fixed integerinequalities
 353^125>2^172*136^125,
 353^10000<2^13761*136^10000.
For completeness eachis verified bythis fixedfiniteinteger procedure:
 pow(b,e):out=1;whilee>0:if e odd:out=out*b; b=b*b;e=floor(e/2);returnout.
The two comparisons useonly integer multiplication and powersoftwo.
Their exponents are constants independentofN,n,s;no runtimeoracle,
advice or absent infiniteprecision calculation is assumed.

Puta=757/2000,b=448/625,d=5209/10000,cL=172/125,cU=13761/10000.
The selectedell=ceil(ar),m=ceil(br),dl=ceil(dr) give
 p=cU*a+b=24753077/20000000,
 g=b+d=12377/10000,p<g<5/4.
From8.2,K<=3*2^13r,dl<=r,n<=r² andceilrounding,
 log2C0<=p*r+4log2r+33.
The constantincludes3 from8.2,cU+1 fromthetwo ceilings,and
12+13+log2(3) fromC_ell;theirsumis<33. Forr>=2^30,
3r/4>4log2r+34 and thismargin increases. Hence
 Y<=2r<n,2^Y<=2C0.                                      (8.3)
At allsuchr,ell,m,dl<=r,ell>=2,m>=r/2,
dl>=kappa+1 and2^kappa>=2m. Linear/logarithmic cutoffmargins
prove these inequalities uniformly. Also2^m>=64ell,so all pool
slotmaxima below are nonnegative. InparticularY+1<=6ell and
Ltry<=4r. No instructionuses a negative window or an unboundedloop.

Poolslot i:pbmax_i is the largestintegerb>=0 with2^b*64ell<=Ci.
Tree:lam_i=dl+i for0<=i<=m-1,lam_m=1;
 tbmax_i=dl+i-kappa-1 for0<=i<=m-2,
 tbmax_(m-1)=2(dl+m-1)-kappa-1.
For everyb_i<=tbmax_i,
 b_i+lam_(i+1)-2lam_i<=-kappa.                         (8.4)
The treewindows are nonnegative bydl>=kappa+1.

Lemma8.1. The totalpool/tree bitcapacity isatleastr²>=n onALLmain
lengthsn>=2^60.
Proof. Maximality gives2^(pbmax_i)*128ell>Ci. Thusby8.1,
 pbmax_i>cL(ell-i)+m-log2(128ell).
The poolsumisatleast(cL/2)ell²+ell*m-elllog2(128ell).
The exacttreesumis m*dl+m²/2+dl+m/2-1-m(kappa+1).
Droppingonlydl+m/2-1>=0,thepositivequadraticcoefficient is
 (86/125)(757/2000)²+(757/2000)(448/625)
 +(448/625)(5209/10000)+(448/625)²/2
 =250038867/250000000=1+delta,
 delta=38867/250000000>0.
Allnegative termsareatmostr(2log2r+10)<=r(2log2r+16),because
ell,m<=r andkappa+1<=log2r+3. Atr=2^30,delta*r>100000>76.
Thereafterdelta*r-2log2r-16 increases,since itsderivative
isdelta-2/(r ln2)>=delta-4/r>0. Thisproves the all-main claim,
including allceil/floorroundings,without a finite-test premise.QED.

AllocateexactlyBbits for1<=B<=n greedily:firstpb_0,...,pb_(ell-1)
withpb_i=min(pbmax_i,bitsremaining),thentb_(m-1),...,tb_0likewise.
Lemma8.1 exhaustsB. Putpp_0=0,pp_(i+1)=pp_i+pb_i;
tp_0=pp_ell,tp_(i+1)=tp_i+tb_i,so tp_m=B. Everykey/residue/rank
partitionusesonlybitsbelowB,asrequiredin10.

## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known
label k, where in the ideal run the labels are independent and uniform on [0, 2^(B+1)). Output: K measured-ready
roots, or ABORT. A leaf qubit is a labeled qubit with table (0, k).

1. POOL. Obtain C_0 leaf qubits (qubits held in the quantum pool, labels in a classical list). The supplier may
   ABORT.
2. COVER7 STAGE. For i = 0, ..., ell-1 run COVERLEVEL(pool, C_i, pp_i, pb_i). If it yields fewer than C_(i+1)
   qubits, ABORT; otherwise keep the first C_(i+1) and measure and release the rest. By the invariants the final
   pool qubits are collimated to pp_ell, and E_i = 2^(pb_i) <= C_i/(64 ell) by definition of pbmax_i, while
   3(Y+1) rounds and the internal trialcap are used as7 specifies.
3. TREE. VEC(0) = LEAF: take the next dl qubits of the final pool (ABORT if fewer remain). Their qubits form the
   index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and
   lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The table has length 2^dl, is exactly the tensor product state in
   the ideal run, and is collimated to tp_0 because every difference is 0 mod 2^(tp_0).
   VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until
   out != FAIL; return out. A root is VEC(m), evaluated depth-first. Run it K times, or ABORT if the pool runs out.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once and all pool qubits are distinct, so every label in
the batch is a sum of at most C_0 leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n
bits by Y <= n, and

    |W| <= 2 C_0 <= 2^(Y+1).                                                        (9.2)

Lemma 9.1 (no pool exhaustion). Conditional on any final-pool contents, in the ideal run the pool runs out before K
roots finish with probability at most 2^-10/n.

Proof. Extendthepoolbyphantomqubits withDel0 for analysisonly.
LetA_i beauniformupperboundon expectedpoolconsumptionofVEC(i),given
anyremainingcontents andthepast. A0=dl. Eachreachedparentattempt
makes2childcalls withconditionalexpectedcost<=2A_i. ParentMERGEfails
withconditionalprobability<=delta=2^-kappa,uniformlyoveritsinputs.
HencePr[attemptjreached]<=delta^(j-1),andtheconditionalcosttower
sums toA_(i+1)<=2A_i/(1-delta). ThisdoesNOTconditiononthe same
attempt's success or assume itscostindependentofsuccess.
Withtt=1/(1-delta),A_m<=(2tt)^m dl. Since2^kappa>=2m,
tt^m<=exp(m/(2m-1))<=e<3. Kroots consumeatmost3K2^m dl in
expectation. MarkovagainstC_ell=2^12nK2^m dl givesfailure<=2^-10/n.
Thephantom andactualpoolruns coincideuntil exhaustion.QED.

Lemma9.2(poolstage). In the analysisidealrun,the poolstageabort
probability isatmostell*exp(-2^m/(2^20ell²)).
Proof. At eachreachedlevel,E_i<=Ci/(64ell),Ci>=2^m. Yieldinequality(7.2)in7.3
gives at least136(ell-1)Ci/(353ell)>=C_(i+1)goodoutputs exceptwith
probability7.3. Unionoverelllevels proves theclaim. Identitycapfailures
are separatelycoupled by7.2;no newsourcecopy is used.QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all COVER7 cell/token and identity outcomes; all merge outcomes (e, bl); and all decisions of the controller in
that batch (sort orders, groupings into seven, trimming, FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels,
and of a difference modulo 2^(p+c) with p+c <= B, depend only on the low_j, since multiples of 2^B do not change them.
COVER7 cell/token outcomes have phase/label-independent probabilities
by7.1/7.2,including everyidentitytrial. The pool product invariant
makes these the same conditionalprobabilities at everyreachedmacro.
Recycled/mergedtableentries remain sums of selected entries ondisjoint
leaves;unmergedqubits are unchanged. Their laterkeys readonlybitsbelowB.
 By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); in COVER7 a groupedcomponent uses theinjective mapalpha->b xor alpha
onitsselecteddisjointcoordinates,andunmergedqubitskeeptheirtables; a LEAF table concatenates disjoint coordinates; and a
merge re-indexes injectively pairs on disjoint coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

## 11. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (2r + ceil(log2 n) + 30).                                              (11.0)

The stages are j = 0, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. Then J + 1 <= log2 M.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. Make at most 4 C_0 acquisitions, stopping at C_0 accepted
qubits: acquire a fresh copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard) and on
acceptance apply X to the control. If 4 C_0 acquisitions do not give C_0 accepted qubits, ABORT. In the ideal run accepted
labels are i.i.d. uniform on [0, 2^dn), each copy is accepted with probability 2^dn/N > 1/2, so by Hoeffding the abort has
probability at most exp(-C_0/2). The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(dn-1) W th = W 2^(dn-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),           (11.1)

so a root is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known frequency f = 2^j W.

Measurement. Run BATCH for stage j. For each root i = 1..K obtain a fair bit beta_i by measuring H|0>, and measure the
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
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(2r + ceil(log2 n) + 30) <= 2^-(Y + ceil(log2 n) + 30), using Y <= 2r. The failure
probability is at most 2^(8-30)/n <= 2^-20/n. QED.

The hypothesis for stage j+1 is the conclusion of stage j, since 2^-(j+3) = rad_(j+1). By induction, with probability at least
1 - 2^-20, theta is within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M.

## 12. 2-adic part: s2 bit by bit

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for a unique s2 in [0, 2^a2). Find its bits at levels
g = 0..a2-1. Let s2low be the known low g bits, sh_g = s1 + M s2low (mod N), wd = a2 - g, and rem = (s2 - s2low)/2^g in Z/2^wd, so
s - sh_g = M 2^g rem (mod N).

A leaf qubit for level g: acquire a copy, apply Shift_(sh_g), which makes the secret s - sh_g; run LE to obtain k; apply X to the
control. Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with kk = k mod 2^wd. Since 2^wd divides N and k
is uniform on Z/NZ, kk is uniform on [0, 2^wd). Use kk as the label.

- If wd = 1: make up to K leaf qubits, stopping at the first with kk = 1; measure it in X. The outcome is + iff rem is even. If
  none has kk = 1, set the bit to 0.
- If wd >= 2: run BATCH with B = wd - 1 and C_0 leaf qubits. Take the first root with W odd, and measure it in X. By (9.1) it is
  (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2, which gives rem mod 2 exactly. Release the other roots. If no root
  has W odd, set the bit to 0.

By (10.3), and independence of distinct roots given G, each such level misses with probability at most 2^-K, even if s1 was wrong.
Set bit g of s2. In the ideal run with s1 correct and no miss, every bit is correct. Output (s1 + M s2) mod N.

## 13. The complete algorithm and its success probability

Finite branch (n < 2^60). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and
reject cand at the first minus outcome. Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For
cand != s the two data branches are orthogonal, so each outcome is uniform. A union bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^60). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = 4 n C_0 + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2
= log2 N <= n, there are at most n batches, each using at most 4 C_0 acquisitions, plus at most K per wd = 1 level, of which there is
at most one. So Q <= Qcap on every branch, without any counter being needed. LE is sized by this Qcap, which is computed before h_e.

Success. Pool exhaustion in the analysisidealrun has totalprobability
<=2^-10 by9.1. Poolstageyieldfailure isatmost
 n*ell*exp(-2^m/(2^20ell²)).
Atr>=2^30,wehaven<=r²,ell<=r,m>=r/2 and
 r/2>=20+6log2r.
The latterholds at thecutoff and increases,derivative
1/2-6/(r ln2)>0. Thus2^m/(2^20ell²)>=r4,andthe totalyieldfailure
isatmostr³exp(-r4)<2^-40. Supplierabortisatmost
nexp(-C0/2)<=r²exp(-r4)<2^-40,sinceC0>=2^m.
Decodererror<=2^-20 and2-adicmiss<=n2^-K<=2^-40 asbefore.
LEcouplingcosts<=2^-10 andthe finiteidentitytrialcap coupling
costs<=2^-128 by7.2. TheirSUMis
 2^-10+2^-40+2^-40+2^-20+2^-40+2^-10+2^-128<2^-8<2^-7.
The finiteprefix tester has error<=2^-10. These are unconditional
additivecouplings,notconditioning onluckylabels or cointrialsuccess.
All actualloops stillhave finitecaps for resourceaccounting.

## 14. Resources on every main-branch execution

Throughout, K = O(sqrt n), dl, m, ell = O(sqrt n), C_ell = O(n^2 2^m) and, writing PP = (353/136)^ell 2^m, C_0 = O(n^2 PP) by (8.2). Also
sum_i C_i <= 2 C_0, since C_i >= (353/136) C_(i+1) >= 2C_(i+1). All fixed loops, caps and aborts below hold on every branch.

Q. Q <= Qcap = O(n^3 PP).

S_Q. The pool holds at most C_0 qubits. A COVER7 trial adds constant coin/outcome/Boolean scratch;all private and releasedwires are clean by7.2,even onbadinputs. The depth-first stack holds at
most two index registers per level, at most 2 (m+1)(dl+m) = O(n) qubits. A merge adds O(sqrt n) qubits. LE and transforms use O(n), reset
between uses. So S_Q = O(C_0 + n) = O(n^2 PP).

S_C. Pool tables and sort scratch use O(n C_0) bits. Depth-first tables: at most three tables per level, each of 2^(lam_i) fields of
3n bits, plus merge scratch O((L + L') n). Since lam_i <= dl + m - 1 and these geometric sizes sum, this is O(n 2^(dl+m)). The decoder stores
K triples and K residues of O(n) bits. LE uses O(n) bits. So S_C = O(n^3 PP + n 2^(dl+m)). These are fixed allocations.

Core steps, per batch.
- Acquisitions: at most 4 C_0, each O(n^2) for Mult plus O(n^(5/2)) for LE (log2 Qcap = O(sqrt n) by (8.3), so h_e = O(sqrt n)): O(n^(5/2) C_0).
- COVER7stage: eachlevelhas3(Y+1)<=18ell rounds,E_i<=Ci/(64ell),
  andatmost6Ci totalLIVEvisits by7.3. Fixedmacrotrials cost<2^32quantumgates and2^64*n totalcoresteps
  each,includingfinitegateemission;Ltry<=4r=O(sqrt n),soO(n^(3/2))coresteps permacro also
  covers itsfulltable additions. Everymacrocallis finitelycapped.
  Perlevelcorework isO(Ci*n*logCi)=O(n^(3/2)Ci),includingidentity
  capfailures. SummingCi<=2C0 givesO(n^(3/2)C0)coresteps.
- Tree: there are at most C_ell/dl LEAF calls at O(n 2^dl) each. A merge producing level i+1 consumes 2^(i+1) dl pool qubits that no other merge at that level uses,
  since inputs of a failed merge are discarded. So there are at most C_ell/(2^(i+1) dl) of them, each O(n 2^(dl+i)) by Section 6. Each level thus costs
  O(n C_ell 2^dl/dl), and all m+1 levels cost O(m n C_ell 2^dl/dl) = O(n C_ell 2^dl) = O(n^3 2^(m+dl)).
- Decoder per stage: at most 2^(Y+8) candidates, K residues each, O(n) bits per addition: O(K n 2^Y) = O(n^(3/2) C_0).

Over at most n batches, plus poly(n) setup (parameters, CRT, Mult constants, the table of Section 4, shift values, initial residues), core steps total
O(n^(7/2) C_0 + n^4 2^(m+dl)) + poly(n). Every loop is either fixed-length or consumes pool qubits or acquisitions, so every branch terminates.

T. By (8.3), log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T = O(n^4 C_0 + n^(9/2) 2^(m+dl) + n Q) = O(n^6 PP + n^(9/2) 2^(m+dl)).

Exponents. The exactnewratios give
 log2PP<=p*r+cU+1,p=24753077/20000000<g=12377/10000,
 m+dl<=g*r+2.
Withr<=sqrt n+1,both are<=g*sqrt n+4. ThusjointlyonEVERYactualbranch,
 T=O(n6*2^(g*sqrt n)),S_C=O(n3*2^(g*sqrt n)),
 S_Q=O(n2*2^(g*sqrt n)),Q=O(n3*2^(g*sqrt n)).
These are derivedfortheactualfinite-trial program,not the unbounded
probability-onlyidealrun. Allcaps/failures/cleanup remainincluded.

## 15. Exact growth indices and selected envelopes

ChooseEXACTa0=6189/5000. It hasgap a0-g=1/10000>0.
For everyfixeddegreej,n^j2^(-sqrt n/10000) isbounded sinceits
logarithmjlog2n-sqrt n/10000 tends tominusinfinity. Thusallfour
virtualresources areO(2^(a0sqrt n));finiteexceptionsaffect only
absoluteoutsideconstants. The physicalbank'sfixedpolynomials fit
thissamegap,but itsordinaryclassicalbound is separatelylinear.
ForB(n)=2^(a0sqrt n),log2log2B=(1/2)log2n+log2a0,so its upper-
envelopeindexisexactly1/2. No matchingalgorithm lowerbound isclaimed.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Limitations

The new sevenqubitinstrument and itscompletefinite implementation
are specific tothisconstantcellcover. No claimofgeneralmeasurement
optimality,priority or absenceofpriorweightedcovers is made. The
finite LP was a discoverytool,not amathematicalacceptancecriterion.
The source stillhastimeindex1/2,notcube-root totalwork. The large
cutoff andoutsideconstants are unoptimized andnotpractical claims.
Only independentideal copies are guaranteed. Every neededsource,
cover,yield,capacity,coupling,decoder andresourceproof is supplied.
