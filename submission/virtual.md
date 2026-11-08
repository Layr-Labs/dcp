# PARTROOT197-Q1: uniform growing odd-partition recycling before linear-merge collimation

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), and let a0 = 141421357/100000000.
The single algorithm PARTROOT197-Q1 below receives N in binary and fresh independent copies of
rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-7 > 2/3.
On EVERY execution branch (every failure, discard and abort included) it satisfies jointly

    T = O(2^(a0 sqrt n)),  S_C = O(2^(a0 sqrt n)),  S_Q = O(2^(sqrt n)),  Q = O(2^(sqrt n)).

All constants are absolute. Each of the four envelopes has growth index exactly 1/2
(Section 15). The fifth claim is the clean-input tolerance 0 (Section 16). The explicit T/ordinarySC bound is C*2^[sqrt2*sqrt n+512ceil(n^(7/16))].
The quantumspace and samples separately obey O(2^sqrt n). The full
physical ledger is in proof.md. The growing compiler and all subleading
exponents are paid explicitly before deriving these exact envelopes.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with
  s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^512:

    r = ceil(sqrt n),   L=ceilLogn,M7=ceil(n^(7/16)),s0=r-32M7,m0=min{j:2j²>=2n-s0²}, m=dl=m0+16L,ell=s0-m,
    kappa = ceil(log2 m) + 1.

So there are ell PARTADAPT LEVELS, a collimation tree of depth m, and leaf tables built from
dl qubits. Since r >= 2^256 these satisfy ell >= 2, dl >= kappa + 1, 2^kappa >= 2m.

## 1. Completeprovenanceandscope

The source/LE/transforms/linearMERGE/fullmodulusdecoders adaptkshitij-hash
TRIAD125 actualf5b375dd-1e5c-4728-95dc-b855b2dc5827,archive
965917f88ec25ccab3d9ce78e07c717a1590a54f. Its overlap/coin-erasure/
unchangedreturnsarecredited. SeparatelyconsultedG4 actual
b48a1af4-3e6b-45d7-8cdb-a414739ddc21,archive
0cca4a7452d2b18eea6c3ba24ac8123ce7fa2886,inspiredmultipleoutputs and
random-consumptionproof. Public185/188virtualframework/profile/gap,
186finiteidentitycap/uniformprefix,189partitionand190analyticodd-family
workingproofsremainmaterial,aspreciselyspecifiedinproof.md5. Private
191/193/194suppliedgrowingcompiler/moment/profileworkingtext;addactual
linksafterpublication,no privateUUIDs/verdictpremises. Currentordinary-
array/quantumpoolimplementationisinproof.md0-4,includingallinitialized
qubits,classicalrecords,allocation/source/address/cleanupcosts.

The indexedallocator adapts6c0e2efd-41bd-4018-a24e-e386f3069c9b with
HEREordinaryclassicalmetadataandarederivedledger. Reduced-field/
reached-attemptcostmethodusesdb6af0c1-2762-4fd4-a5ea-d78910d65cb1.
Correlated-record/arbitrary-referencechannelproofprinciplewasconsulted
infbb8f36c-3904-4bf0-9ddf-e9f5d83657ae;itsmeasuredbasisbank/profile/
resourcecomparatorisnotexecutedhere. No generationtags/basisbank/epoch
repair isselectedfromfc8. The largeclassicaltablesAREordinaryS_C.

Contextfrompeer:qzvHPC1272aad498c-d5e9-4f64-a222-3b2f7f961738,
AdamGagolCS1f1481815-9577-4990-abe3-7b79fa5d9284,sparievPSieve
4256e671-97b0-4f84-82ce-12aeee17224e,0xplemonadeCYC1
7a4cecdc-7941-4027-8c95-8520de9fbcf3;KuperbergSIAMJ.Comput35(1),2005/
arXiv:1112.3333arecontextcarriedthroughthepeer. Allneededproofsare
suppliedhere;noabsentpaper,LPobjective,oldverdict,priority or general
optimalityclaimprovesany step. Timeindexremains1/2,notcube-rootwork.

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
identitytrialcaps ofPARTADAPT (7.2);its rejectionterminates almostsurely
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

## 7. PARTADAPT: uniform growing odd-partition instrument

For the main branch n>=2^512,let t be the leastintegerwitht^8>=n,
and k the leastoddinteger>=t. Compute t byintegerbinarysearch,then
h=(k-1)/2,w=1/[h(h+1)]. Thusk>=n^(1/8),k<=2n^(1/8),k>=3.
No realroot/logoracle is aninstruction. Allmacroparametersarepublic.
A labeledqubit hastable(t0,t1),Del=t1-t0. Conditionalonlatentlabels
andpastoutcomes,the pool consists of its recorded equatorialphase
qubits inproductwithallother source/pool/reference registers,by3/5.
One macro takesk qubits with equalkeysDel mod2^(p+c),collimatedtop.

### 7.1. Complete uniform cell family,poststates and rate

A-cell:chooseoneunorderedoddpair,leaveotherk-2coordinatesfree,weightw.
Forj=0,...,h-1,J_j-cell:partitionallkcoordinates intoj unorderedoddpairs
andoneall-equalremaindergroupofsizek-2j. Itspercellweightandcountare
 w_j=(1-w*j*(k-j))*(k-2j)!/(k-j)!,
 N_j=k!/(2^j*j!*(k-2j)!).
CanonicalenumerationlistsA,J0,...,J_(h-1),thenlexicographicsortedpairlists;
the remainderis theircomplement. Thisnames eachcellonce. The formulas
are uniformfiniteinteger/rationalalgorithms givenpublick,notadvice.
Computefactorialproducts/rationalreductionsserially;donotstorethe
entirecellfamily or its truth-table history.

LetPi_cell projectontothecomputationalcell. IfxhasminorityHammingweight
t<=h,thereare t(k-t)containingAcells. A J_jcontainsxonlyifj=t orj=k-t;
forj<h onlyj=t<hispossible. Thereare (k-t)!/(k-2t)! suchJ_tcells:
matchthe tminoritybits todistinctmajoritybits,leavingequalbits.
For t<h,totalweightis
 w*t*(k-t)+[(k-t)!/(k-2t)!]*w_t=1.
At t=h,Jcellsareabsentandw*h(h+1)=1. Allweightsarenonnegative.
Therefore sum_cell w_cell Pi_cell=I onEVERYoneofthe2^k basisinputs
andalljointstates. The normalizedKrausoperatorsaresqrt(w_cell)Pi_cell.
This is an all-kidentity,not a finite LP/empiricaloptimalityclaim.

On productequatorialinputs,a cellwithLindependentbinarycomponents
hasprobabilityw_cell*2^(L-k),independentofphases,labels,secret,past.
Thus the typeprobabilitiesare
 P_A=choose(k,2)*w/2=k/(k+1),
 P_j=N_j*w_j*2^(j+1-k)=2^(1-k)*choose(k,j)*(1-w*j*(k-j)).
They sumto1 bycompleteness. This is the sameconditionaltypelaw at
EVERYreachedmacro,evenwhenlaterkeysdependonallpreviousoutcomes.

EveryconstrainedgroupGbecomesonephasequbit. Its canonicalpatternb
has smalleroddpairindex0/larger1,orall0foranequalgroup. Outputtable:
 (sum_(i inG)t_(b_i)^i,sum_(i inG)t_(1-b_i)^i).
Choose smallestwirev;CNOTv->i for everyotheri,thenXtoiifb_i xor b_v=1;
finallyXvifb_v=1. Everyothergroupwire becomeszero,andvindexalpha
selectsb xoralpha. This holds onEVERYstate supportedonthecell,
includingarbitraryreferences. Onproductphaseinputs,disjointconstraints
factor the projectionintoallgroupoutputs andunchangedfreeinputs,
inproductwith eachotheranduntouchedreferences. Nothingiscloned.

EachoddpairisGOOD:equalkeys makeDel_a-Del_b divisibleby2^(p+c).
The all-equalgroupRECYCLES atoldp,withdifferenceitsinputDelsum.
A givesoneGOOD andk-2unchanged inputs;J_j givesjGOOD andoneRECYCLED.
GOODleavesLIVE. NetLIVEcostCis2onA andk-1onJ_j;GOODcountGis1onA,
j onJ_j. Compute p=E G=P_A+sum_j jP_j,mu=E C andq=mu/p bythe
exactfiniteformulasBEFORE computing sourceC_i. These are input-dependent
rationals,notfixedconstants or a logoracle. G isnotBernoulli,andmay
dependonitsownC. Uniformlyforourpublick,
 2<q<=2+7/sqrt(k),mu=(3k-1)/(k+1),p>=k/(k+1)>=3/4. (7.1)

Here is a proof ofthe uniformratebound. LetX~Bin(k,1/2),B=|X-k/2|,
T=min(X,k-X). The displayedP_j equalsPr[T=j]*(4B²-1)/(k²-1).
The j=h termis0,soitcanbe included. Independent centeredfairbits give
 E B²=k/4,E B4=(3k²-2k)/16:
expandthefourthpower,retainingthe kfourthpowers and6choose(k,2)
pairedsecondpowers;allodd/crosssingleterms vanish. Therefore
 sumP_j=1/(k+1),mu=(3k-1)/(k+1),
 p=3k/[2(k+1)]-E[4B³-B]/(k²-1),
 mu-2p=[2E(4B³-B)-(k-1)]/(k²-1).
Thisispositive:everyJoutcomehascostk-1>=2j+2 andtotalJmasspositive.
ByCauchy,E B³<=sqrt(E B² E B4)<=sqrt(3k³)/8. Hence
 0<mu-2p<=8E B³/(k²-1)<=sqrt3*k^(3/2)/(k²-1).
Usep>=3/4 andk²/(k²-1)<=9/8 toobtainq-2<7/sqrtk,proving7.1.
Asln(1+x)<=x and2ln2>1,log2q-1<=q-2. For n>=2^512,k>=n^(1/8),
 1<log2q<=1+7n^(-1/16)<1+10^-8,                  (7.2)
since7*10^8<2^32. These inequalitiesare analyticproofs;the controller
computesonlyexactinteger/rationalq,notrealmoments/logarithms.

Alloutputentriesaresums onDISJOINTleafsets. alpha->b xoralpha is
injectiveonitsgroup;differentcomponentsusedisjointgroups,andfree
inputskeepstate,tableandwireID. The product,disjointincidence and
fullpositive3n-bitlabelinvariants thuspersist for everypublick.

### 7.2. Uniform exact dyadic dilation with its full growing cost

LetL=h(h+1). Eachreduceddenominatorofw_j divides
 L*(k-j)!/(k-2j)!<=k^(k+2). IncludingtheAdenominatorL,theirlcmD
satisfies D<=k^(k²):the productexponentis(k+2)h+2<=k².
ComputeD seriallybyEuclid/lcm. Put b_k=ceilLogk,
 coinbits=ceilLogD+2<=k²b_k+3,M=2^coinbits,
 scale=floor(M/D) in{4,5,6,7},R=M-scaleD<D<=M/4.
GiveeachcellscaleD*w_cell distincttokens,aninteger;addRidentitytokens.
Everybasisinputbelongs toscaleD+R=Mtokens by7.1. Orderallnonidentity
bycanonicalcell/copyorder,thenidentity. Thereare<=2k^(k+1)cells:
choose(k,2)<=k²,and eachN_j<=k!<=k^k,withfewerthank Jtypes.
Sincew_cell<=1,totaloutcomeIDs<4M k^(k+1),so
 outcomebits<=2k²b_k+8.
Thesearecomputedparameterbounds,not an exponentiallylargeadvicearray.

Preparecoinbitsqubitsr andoutcomebitsqubitsz inzero;applyHadamardsto
allr. f(x,r) isther-thcontainedtoken,r=0,...,M-1;XORfintoz.
h(x,z) isz'srankamongcontainedtokens,or0oninvalidpairs;XORh into r,
clearingr. UncomputeBoolean scratch,measure/resetz. Identityleaves
allinputsunchanged;otherwiseperformthe groupcleanup7.1. Decode the
measuredID bycanonicalenumeration/range-arithmetic,not a QRAMlookup.

For arbitraryjointinputsum_x|x>|R_x>,beforemeasuringzthestateis
 sum_x|x>|R_x>|0>_r (1/sqrtM)sum_(z containsx)|z>.
Rankbijectionproves this exactlyonallbasisinputs andthusallreferences.
TokenKrausisPi_cell/sqrtM,orI/sqrtMforidentity. Identityprobability
R/M<1/4 isinput-independent;conditionalonnonidentity,the aggregated
percellweightisscaleD*w_cell/(scaleD)=w_cell. Everyprivate/released
wireisclean onallinputs,without anequatorial/product assumption.

The following costbound is UNIFORMINn,not a fixed-macroconstant.
SetF=8k²(b_k+1). Itbounds bothf/hinputbitcounts,targetbitcounts,
currentmatching/counterwordlengthsandconstant-manyarithmeticoperands.
CompileeachBooleanfunctiononeoutputbitatatime:enumerateinputpatterns,
computeNOT/Toffoliequalityflag,copybit,uncomputeflag. Targetisnever
itsownfunctioninput. AtmostF2^Fterms eachwithO(F)gatesgive<=2^(2F)
elementarygates;<=8Fprivateancillas suffice,withreusableflagchains.
Toffolihas the exactClifford+T completionof2.

Evaluateeachclassicaltruthfunctionvaluebygrowingcanonicalmatchinglists,
cell-membershiptests,andtokenranges/ranks,usingO(F)currentbits.
Atmost2^Finputpatterns and2^Ftokens perpattern,and a conservative
F^16 schoolbookarithmetic/enumerationoverhead,fit2^(16F)coresteps
forF>=128. This paysfactorial/denominator/reduction/membership/rank,
measurementIDdecoding,groupcleanup/fulltablesumsandgateemission.
Multiplyingbyn payscompleteO(n)-bit known-wire/operandstaging:
 oneactualtrialcosts<=C*n*2^(16F)coresteps.          (7.3)
Onlyconstant-manyF-bitcurrentwords,packedmatchingindices andO(n)
currentwords coexist. No storedtruth-table/history,QRAM,unknown-address
memory,arbitraryrotationoracle or input-specificadviceisused.
Computingk,D,q andpublicparametersnaivelycostsO(n16)bitsteps and
O(n)ordinarybits:atmostpolynomialink,F integerproducts/Euclidsteps
onF-bitwords,withk,F<=n and a conservativefixeddegree16 allowance.
Allthissetupisexplicitlycharged in14,notassumedfree.

For log2n>=512,k<=2n^(1/8),b_k<=log2n/8+2,so
 F<=8n^(1/4)log2n,8F<=n,
 16F<=128n^(1/4)log2n<=sqrt(n)/10^9.              (7.4)
For thelastinequality,t2^(-t/4)decreasesfort=log2n>=512;at512the
ratio128*512/2^128=2^-112<10^-9. The samecomparisonproves8F<=n.
Thus2^(16F)<=2^(sqrt n/10^9). This growingcompilerfactoris carried
explicitlyinto14/15,neverhiddenas an outsideconstant. Hugecutoffsand
circuitsmake thisasymptotic,not a practicalperformanceclaim.

Eachmacrotriesuntilnonidentity,atmostLtry=Y+ceilLogn+64trials,then
ABORTbatchifallidentity. The probability-onlyanalysisrunremovesjust
theseidentitycaps,keepingallothers. Rejectionterminatesalmostsurely
andhasnormalizedlaw7.1. Perlevel<=Cin/2successfulcallsplusonefailed
callis<=Cin forCin>=2;sumCi<=2C0andatmostnbatches give<=2nC0calls.
Totalcouplingfailure<=2nC0*4^-Ltry<=2^-128. No trialacquires a copy.
AllresourceboundsarefortheACTUALfinitecap,evenonabort/badlabels/
nonproductinputs. Unboundedidealwork isnot a resourceargument.

### 7.3. Uniform PARTLEVEL and random-stopped yield

PARTLEVEL(pool,Cin,p,c),E=2^c:repeatEXACTLY(k+1)(Y+1)/2rounds. SortLIVE
byDel mod2^(p+c),tiesbyoriginallogicalorder;cut eachkeyrunintoconsecutive
k-tuples,leaving<=k-1inputsperkey. Applycappedmacroingrouporder;ABORT
stopsbatch. AppendGOODpivots toOUTPUTinincreasingpivotorder;append
RECYCLEDpivots tonextLIVEthenfreeunchangedinputs byoriginalorder.
Ungroupedinputs stayLIVE. Finallyreset/releaseLIVE. OUTPUTiscollimated
top+c,LIVEoldp;controllerreadsonlylowkeys/outcomes,notroot/highbits.

AroundwithLliveinputsandu<=(k-1)Eleftovers returns<=k-2LIVEpergroup:
 Lnew<=((k-2)L+2u)/k<=((k-2)L+2(k-1)E)/k.
HenceL_j-(k-1)E<=(1-2/k)^j(Cin-(k-1)E).
Since(1-2/k)^((k+1)/2)<=exp(-(k+1)/k)<1/2 andCin<=2^Y,
fixedroundsand integralitygiveLend<=(k-1)E. TotalLIVEvisits are
 <=kCin/2+(k-1)roundsE.

In theprobability-onlyanalysisidealrun5,reached(G,C)pairs have the same
conditionaljointlaw7.1givenALLpastandalllabels. Extendafterstoppingby
independentphantomtypes forproofonly;chainrulegivesthei.i.d.sequence.
Noactualphantomdraws/workoccur. For actualmacrocountA,
 sum_(i<=A)C_i=Cin-Lend.
WithE<=Cin/[2(k+1)ell],ell>=2,
 A>=(Cin-(k-1)E)/(k-1)>=Cin/[2(k+1)],A<=Cin/2.

Puteta=1/(64ell). HoeffdingforG in[0,(k-3)/2]andC in[2,k-1]gives
lowerG/upperCdeviationatmostexp[-2eta²z/(k-3)²]each(theGboundisstronger).
UnionoverALLprefixesceil(Cin/[2(k+1)])<=z<=Cin/2 givesfailure
 <=2Cin exp[-Cin/(64²(k-3)²(k+1)ell²)]
 <=2Cin exp[-Cin/(2^13k³ell²)].
Thiscoversthe randomAwithoutconditioningonit. Outsideit,
 S>=(p-eta)A>=[(p-eta)/(mu+eta)]*(Cin-(k-1)E).
Since1/p+1/mu<2,theratiois>=(p/mu)(1-2eta). Relativeproductloss
is<=2eta+(k-1)/[2(k+1)ell]<17/(32ell)<1/ell. Therefore
 S>=(ell-1)Cin/(qell).                              (7.5)
GisnotBernoulli,norisitassumedindependentofC orlaterkeys.

Atallmainlengths8,k<=2n^(1/8),ell²<=n,sodenominator2^13k³ell²<=2^16n².
AlsoCin>=2^m,ln(2Cin)<=3r,andm>=20+4log2n by8. Thus
ln(2Cin)<=3Cin/(2^18n²),andtheprecedingfailureisatmost
 exp[-Cin/(2^18n²)].                               (7.6)
Indeed2^m>=2^20n³alreadygivesRHS>=12n>=3r. Thisuniformall-label
certificateincludesallgrowing-kconstants,not finitecaseextrapolation.

Cost. Y+1<=6ell givesrounds<=3(k+1)ell. WithourEslot,totalLIVEvisits
 <=[k/2+3(k-1)/2]Cin<2(k+1)Cin.
SortingcostsO(LnlogCin),logCin=O(sqrt n),k<=2n^(1/8). FiniteLtry=O(sqrt n)
trials costO(n^(3/2)2^(sqrt n/10^9))permacro by7.3/7.4,includingall
canonicaltablework. SoonelevelcostsO(n^(5/2)Ci*2^(sqrt n/10^9))
conservatively,evenonactualcapfailures,with<=8F<=nprivateancillas.
The input-dependentcompilerfactor staysin the resourceledger14.

## 8. Root schedule with an explicit negative sample margin

For n>=2^512 compute r=ceil(sqrt n),L=ceilLogn,M7=ceil(n^(7/16))
by exact integer roots (M7 is the least integer with M7^16>=n^7).
Put s0=r-32M7, m0=min{j>=0:2j²>=2n-s0²},
 m=dl=m0+16L,ell=s0-m,kappa=ceilLogm+1.
Compute k,D,q,F by7, K=8192(2r+L+30),C_ell=4096nK2^m dl,
 Ci=ceil(qell*C_(i+1)/(ell-1)),Y=ceilLogC0,Ltry=Y+L+64.
All are exact finite integer/rational computations. The analytical
allocation parameter u=max(Y,2m)+2 is also public; no bank is used.
Classical arrays store the complete schedule as ordinary counted bits.

As before rho=qell/(ell-1)>2 gives
 Ci>=q^(ell-i)C_ell>=q^(ell-i)2^m,                 (8.1)
 C0<=8q^ell C_ell, sumCi<=2C0.                   (8.2)
The ceiling errors sum to <=rho^ell and (1-1/ell)^(-ell)<=4.
Since K<=3*2^13r,n<=r²,dl<=r, we have
 log2C0<=ell*log2q+m+4log2r+30.                  (8.3)
The constant is 3+12+13+log2(3)<30.

Here M7<=r/2^31 at ALL main lengths: M7<=n^(7/16)+1,
r>=sqrt n and n^(-1/16)+1/sqrt n<=2^-31 at n>=2^512.
Thus (1-2^-26)r<=s0<r. From n>(r-1)², m0>=r/2
for r>=8. Also 2n-s0²<(1+2^-24)r², so m0<=71r/100+1.
Since16L+1<=r/100 at the cutoff with increasing margin,
 r/2<=m<=18r/25<3r/4, r/4<=ell<r/2.             (8.4)
In particular all are positive, <=r-1<sqrt n,ell²<n,
dl>=kappa+1,2^kappa>=2m. Both m>=20+4log2n and
m>=20+8log2r+4 hold at r>=2^256 and improve thereafter.
They give 2^m>=2^20 n^4 and2^m>=2(k+1)ell.         (8.6)

By7's uniform log2q<=1+7n^(-1/16),8.3 implies
 Y<=s0+7r*n^(-1/16)+4log2r+31
   <=r-25M7+4log2r+38<=r-20M7.                 (8.5)
We used r*n^(-1/16)<=M7+1 and4log2r+38<=5M7;
the latter holds at the cutoff and improves with n. Consequently
Y<=2r,Ltry<=4r,Y+1<=r+1<=6ell. These prove all original
round/trial/growth/window conditions, without uncapped rejection.
The negative M7 margin will pay every sample/quantum polynomial.

For time/table analysis, s0>=sqrt n-32M7>0 gives
 2m0<=sqrt(4n-2s0²)+2<=sqrt2*sqrt n+46M7+2,
using sqrt(x+y)<=sqrt x+y/(2sqrt x) and64/sqrt2<46.
Since Y<=r<2m, u=2m+2, and L<=M7, we obtain
 u<=sqrt2*sqrt n+80M7.                            (8.8)
The growing compiler satisfies16F<=128n^(1/4)log2n<=128M7.
Thus u+16F<=sqrt2*sqrt n+208M7.                   (8.9)
No input-dependent factor is an outside constant.

Poolslot i:pbmax_i is the largestintegerb>=0 with
 2^b*2(k+1)ell<=Ci.
Tree:lam_i=dl+i for0<=i<=m-1,lam_m=1;
 tbmax_i=dl+i-kappa-1 for0<=i<=m-2,
 tbmax_(m-1)=2(dl+m-1)-kappa-1.
Foreveryb_i<=tbmax_i,
 b_i+lam_(i+1)-2lam_i<=-kappa.                      (8.7)
The treewindowsarenonnegativebydl>=kappa+1.

Lemma8.1. Totalpool/treebitcapacityisatleastr²>=n atALLmainlengths.
Proof. Maximalitygives2^(pbmax_i)*4(k+1)ell>Ci,so8.1andlog2q>1give
 pbmax_i>(ell-i)+m-log2[4(k+1)ell].
The poolsumis>=ell²/2+ell*m-elllog2[4(k+1)ell]. The exacttreesumis
 m*dl+m²/2+dl+m/2-1-m(kappa+1).
Dropdl+m/2-1>=0. Because dl=m and ell+m=s0, the positive
quadratic sum is s0²/2+m². By the exact m0 definition and m0>=r/2,
 s0²/2+m²>=n+32m0L>=n+16rL.
As k<=2r^(1/4),ell,m<=r, all negative slot/window terms are
<=r(3log2r+20)<=r(3L/2+23). The surplus is therefore
>=r(29L/2-23)>2r at L>=512. Capacity>=n+2r>=r²,
including every ceiling, floor and growing slotfactor at all main
lengths. No sampled-case extrapolation establishes this lemma. QED.

GivenBwith1<=B<=n,allocateexactlyBbits greedily:firstpb_0,...,pb_(ell-1)
withpb_i=min(pbmax_i,bitsremaining),thentb_(m-1),...,tb_0likewise.
Lemma8.1exhaustsB. Putpp_0=0,pp_(i+1)=pp_i+pb_i;
tp_0=pp_ell,tp_(i+1)=tp_i+tb_i,so tp_m=B. Everykey/residue/rank
partitionreadsonlypositionsbelowB,asrequiredfor10.

## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known
label k, where in the ideal run the labels are independent and uniform on [0, 2^(B+1)). Output: K measured-ready
roots, or ABORT. A leaf qubit is a labeled qubit with table (0, k).

1. POOL. Obtain C_0 leaf qubits (qubits held in the quantum pool, labels in a classical list). The supplier may
   ABORT.
2. PARTADAPT STAGE. Fori=0,...,ell-1 runPARTLEVEL(pool,C_i,pp_i,pb_i)
   withthepublick and(k+1)(Y+1)/2rounds. IffewerthanC_(i+1)GOODqubits
   result,ABORT;otherwisekeepfirstC_(i+1),measure/releasetherest.
   The finalpooliscollimatedtopp_ell andE_i=2^pb_i<=Ci/[2(k+1)ell]
   by8. ThefiniteidentitytrialcapLtry isexactly7.2.
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

Lemma9.2(poolstage). In the analysisidealrun,thepoolstageabort
probabilityis<=ell*exp[-2^m/(2^18n²)]. At eachreachedlevel,
E_i<=Ci/[2(k+1)ell],Ci>=2^m. Yield7.5 gives(ell-1)Ci/(qell)>=C_(i+1)
exceptwithprobability7.6. Unionoverell proves theclaim. Finiteidentity
capfailuresareseparatelycoupledby7.2;no newcopy isacquired.QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all PARTADAPT cell/token and identity outcomes; all merge outcomes (e, bl); and all decisions of the controller in
that batch (sort orders, groupings into publick-tuples, trimming, FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Here controller decisions means only the listed abstract selection,
termination and order decisions. G excludes full high-label table values,
arithmetic bit traces and emitted-gate-description data; the proof
marginalizes these records rather than conditioning on them.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels,
and of a difference modulo 2^(p+c) with p+c <= B, depend only on the low_j, since multiples of 2^B do not change them.
PARTADAPT cell/token outcomes have phase/label-independent probabilities
by7.1/7.2,including everyidentitytrial. The pool product invariant
makes these the same conditionalprobabilities at everyreachedmacro.
Recycled/mergedtableentries remain sums of selected entries ondisjoint
leaves;unmergedqubits are unchanged. Their laterkeys readonlybitsbelowB.
 By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); in PARTADAPT a groupedcomponent uses theinjective mapalpha->b xor alpha
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

## 13. Completealgorithm and unconditional success

Finitebranch(n<2^512):foreachcand=0,...,N-1,useup ton+10freshcopies;
applyShift_cand,measurecontrolinX,andrejectcandatfirstminus. Output
firstunrejectedcand,or0. Truecandhasallplus;wrongcandhasindependent
fairoutcomes becauseits twodatabranches areorthogonal. Unionbound
N2^(-(n+10))<=2^-10. OrdinaryworkspaceremainsO(n);allbranchcostsare
finite,andthisfiniteprefix affects onlyabsoluteoutsideconstants.

Mainbranch:computea2,M,dn,J,K,k,D,q,F,the exactschedule/Yandallocations;
putQcap=4nC0+K BEFORELE. Run11then12. AnyABORTreleasesallandoutputs0.
SinceJ+1+a2<=log2N<=n,thereareatmostnbatches,each<=4C0acquisitions,
plus<=Kfortheuniqueoptionalwd1level. ThusQ<=Qcap onEVERYbranch.
Dynamiccompilation andidentitytrialsacquirenocopies. Everyloopis
finite/fixed orconsumespool/sourcecapacity,includingallbadlabelbranches.

In theanalysisidealrun,pool exhaustiontotal<=2^-10by9.1. Yieldabort
<=n*ell*exp[-2^m/(2^18n²)]<=n²exp(-4n²)<2^-40 by8.6andn>=2^512.
Supplierabort<=nexp(-C0/2)<2^-40 sinceC0>=2^m>=2^20n4.
The elementaryn²exp(-4n²)bounddecreasesforn>=1;alreadyatn16it is
<2^-40usingexp(1)>2. Decodererror<=2^-20,2-adicmiss<=n2^-K<=2^-40.
AddLEcoupling<=2^-10 andfiniteidentitycapcoupling<=2^-128. TheSUMis
 2^-10+2^-40+2^-40+2^-20+2^-40+2^-10+2^-128<2^-8<2^-7.
Thisisunconditional,notconditionedonfavorablelabels/caps/outcomes.
Thefinitebrancherroris<=2^-10. Allresourcesbelowrefer toACTUALfinitecaps.

## 14. Actual uniform resource ledger

All main parameters are O(sqrt n),F<=n,sumCi<=2C0. Pool SQ=C0,
source indices<=16n²,current scratch<=2^20n16 andmacroprivate<=8F<=n.
The whole physical quantum allocation is exactly the H_Q prefix
specified in proof.md, plus n+1 incoming source wires, including
all inactive qubits. Q<=4nC0+K. Since2^Y<=2C0 and C0<=2^Y,
 Q=O(n*2^Y), SQ=O(2^Y+n16).
Ordinary classical arrays/metadata/source-depth tables fit
O(n³*(2^Y+2^(2m))+n16), including full initialization and frames.
Every bit access pays its full known address cost; unknown-index
LOOKUP remains the explicit linear-row circuit of6.

Core work per batch comprises O(n^(5/2)C0) source/LE/transforms,
O(n^(5/2)C0*2^(16F)) partition stages with their actual finite
identitycaps/visits, O(n³2^(m+dl)) tree work and O(Kn2^Y)
decoder work. There are<=n batches. Polynomial O(n16) parameter
and schedule/denominator arithmetic and canonical/gate generation
bitloops are counted, not advice. Thus conservative fully addressed
 T_P=O(n20*2^(u+16F)), SCvirtual=O(n³2^u).         (14.1)
All source transfers and cleanup count. The ordinary-array physical
driver proves T,SC<=C*n32*2^(u+16F) on every branch.
By8.9 and log2n<=M7, this implies
 T,SC<=C*2^[sqrt2*sqrt n+512M7].                  (14.2)
The compiler16F, parameter work, ordinary long arrays, inactive
quantum prefix and full addresses have all been charged explicitly.

## 15. Exact selected rational envelope and sample/quantum margin

Put c=141421357/100000000. Exact integer squaring gives c²>2.
Let epsilon=(c²-2)/(4c)>0; then
 c-sqrt2=(c²-2)/(c+sqrt2)>2epsilon.
M7<=n^(7/16)+1. Once n is sufficiently large, 512M7<=epsilon*sqrt n;
for example n>=(1024/epsilon)^16 and n>=(1024/epsilon)^2 suffice.
Equation14.2 therefore gives T,SC=O(2^(c sqrt n)).
The algorithm uses the actual root schedule, independent of the
selected rational c; the growing compiler was already paid in14.

For quantumspace/samples,8.5 and r<=sqrt n+1 give
 Y<=sqrt n-19M7.
Since M7 grows faster than every fixed multiple of log2n,
 n^j2^(-19M7) is bounded for every fixed j. Thus Q=O(2^sqrt n)
and the FULL initialized prefix H_Q+n+1=O(2^sqrt n), including
its additive polynomial scratch. Every earlier fixed length has
finite deterministic caps, so only the outside constants change.
One actual configuration establishes all four bounds jointly.
All four selected exponential envelopes have index1/2; clean0
requires independent idealcopies. No lowerbound, priority or
positive-robustness/impossibility claim is made.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scopeandlimitations

Thegrowingmacrois a uniformfinitebitprogram withhugeexplicitcutoff,
not a practicalhardwareclaim. Its compiler andancillasdependonn and
arechargedexplicitly. Exactrationalcoefficientsandallfourboundsapply
tooneconfiguration;clean0promises idealindependentinputs only. Still
index1/2,notcube-roottotalwork. No priority,generalmeasurementoptimality,
matchinglowerbound or claimtodominatetradeoffswithsmallquantumspace.

Working provenance update: private195 supplied the ordinary-array/fixed-pool
channel and ledger; private196 supplied integer-root/slack/subleading
proof presentation. Current new actual Q1 schedule differs from both.
Neither unreviewed work nor predecessor acceptance proves this program.
Add actual direct material links only after publication inspection.
