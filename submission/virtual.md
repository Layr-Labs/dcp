# Uniform explicit-root-budget160 complete virtual module; corrected full-residue filter retained

# LG explicit-root-budget160 full virtual reference

# Complete LG32 reference P: VIRTUAL-ONLY resources and reduced histories

This module supplies the complete selected LG32-603 source, adapted from
public6f095593-51ce-4055-8c63-707c437940c8, immutablecommit
3a9525598f00107c4ade9b21389c1d3e2601eb56. The original full proof has
SHA256e54db374152f5034abdfd4b07e108073b59d0153628a91769c1559397557a940.
All its authors/method credits below remain. Its resource statements
concern the VIRTUAL reference allocation; proof.md gives the different
physical counted-basis implementation and its scored bounds.

The selected variable-arity integer schedule differs from the original LG32-603 schedule; every width-sensitive resource estimate is recounted below. The source/merge/listing/decoder instruments,
caps and finite branch are supplied completely. The changes here make
the reduced conditioning fields and fresh-attempt tower argument
explicit, fix unused public setup and a scope typo, and specify a
finite numerical completion. There is no byte-identity claim or prior
verdict premise. No physical helper transcript is a conditioning field.
The reduced-law/fresh-attempt proof method is directly adapted from
IFW1232-FILTERED db6af0c1-2762-4fd4-a5ea-d78910d65cb1; its constant-width
algorithm/profile is not selected. All resource guarantees in this
module are fully proved for this supplied completion, not imported.

# LG-LOGROOT160: low samples and counted smaller quantum exponent

## 0. One algorithm, envelopes and notation

For every N>=2 and s modulo N, let n=ceil(log2 N). The complete
single virtual algorithm below recovers the ENTIRE s with unconditional
probability at least1-2^-8 from independent ideal copies. On every
branch, including every failure, discard, guard, retry and abort,
 T=O(2^(n/(log2 n)^(7/8))),
 S_C=O(2^(n/(log2 n)^(15/8))),
 S_Q=O(2^(n/(log2 n)^(15/8))),
 Q=O(n^2*2^((1/3)*(log2 n)^(31/32))).
All coefficients are exact and outside constants absolute. These
are VIRTUAL workspaces; the physical proof replaces ordinary
classical storage by counted basis qubits and has ordinary S_C=O(n).
Virtual time/classical/quantum/sample indices are1,1,1,0.
The supported malformed fraction is0 under the independent-ideal-copy
model, without positive robustness or impossibility assertions.

Notation: dn=floor(log2 N), N=2^a2*M with M odd, s1=s mod M,
s=s1+M*s2 mod N with0<=s2<2^a2. omega=exp(2*pi*i/N).
Data registers have n qubits and labels are known nonnegative integers.
Log means log2. The symbols lambda and lam denote the same width.
Let ell=ceil(log2 n) by integer bit tests. For ell<2^20 run the
complete finite exhaustive tester13; compute main parameters only
when ell>=2^20. All roots/ceilings below are exact integer operations:
 a=floor(log2 ell),u=ceil((ell^31)^(1/32)),V=u,
 h=floor(31a/32)-5,f=2^h,Ybar=4ell,
 y=ceil(V/(4h)),w=ceil(n/((f-h)*y)),
 cbar=ell+6,q=f+ceil((f-1)*cbar/(w+1)),
 mu=q+y,kappa=ceil(log2 mu)+3,c0=kappa+1,lambda=w+c0,
 G=f-h-1,Hb=ceil((f-2h+4)*w/2),rstar=ceil(sqrt(n*h)).
Integer roots can be computed by finite binary search. The actual
low-sample profile, not a balanced sqrt(nh) profile, is selected.

Uniform explicit-range/root certificate. Put t=log2 n,
 alpha=31/32,x=ell^alpha. At ell>=2^20,a>=20,h>=14,
 x/128<=f<=x/32, x<=u<=9x/8 and u<=ell.
Indeed a<=log2 ell<a+1 and the two floor losses give
h>=alpha*log2 ell-alpha-6>alpha*log2 ell-7; the upper
bound is h<=alpha*log2 ell-5. Roots are exact integer roots
of ell^31, not quantum or real-valued setup or trial states.
The source primitive needs h>=3. Neither h>=32 nor h>=ell/3
is assumed. All inequalities below follow uniformly from
n>=2^(ell-1),ell>=2^20 by concrete boundary margins and
decreasing polynomial/exponential ratios.
As f-h>=f/2 and y<=u/(2h),
 f*y<=9*x²/(512h),w>32h*n/x²>=64*(ell+10)>=cbar-1.
Thus f<=q<=2f before kappa. It follows that
 mu<=u/16+u/(2h)<=u/8<=sqrt(n),c0<=cbar=ell+6,
 2^kappa<=16mu.
The upper rounded width gives
 w<=8h*n/(f*u)+1<=1024h*n/ell^(31/16)+1,
 f*w<=8h*n/u+f,
 f*lambda<=8h*n/u+f*(c0+1)<=n/16.
For the last inequality, h<=log2 ell,u>=ell^alpha give
8h/u<=8log2(ell)/ell^alpha<=160/2^19<1/1024;
f*(c0+1)<=ell*(ell+7)/32<=n/1024. Both ratios decrease
from the cutoff, leaving a margin stronger than n/16.
Consequently lambda>=3kappa+14,lambda>=h+3,L>=8f,
8*rstar<=n and Ybar=4ell<=rstar<=n. All full-label/tuple/
guess/target/arithmetic fields are O(n) bits; long arrays and
frames remain banked or recomputed.

The NEW public root budget is independent of the actual Y:
 Ybar=4ell,K=8192*(8Ybar+ell+30)=8192*(33ell+30).
Compute K before Ccap,Y; then15 proves actual Y<=Ybar directly.
This is not a fixed-point definition. The former rstar remains a
loose independent field bound; it no longer sets the root count.
The cumulative source guard13.5 and all original local guards,
filters and decoders are retained. LE is sized using the old-form
Qcap=n*Ccap+K with THIS selected K, which bounds actual Qglob.

## 1. Provenance and what is new

Sections 2-6.2 and 10-12 follow the framework of CS1 (f1481815-9577-4990-abe3-7b79fa5d9284) as adapted in my submissions HPC-127 (2aad498c-d5e9-4f64-a222-3b2f7f961738), LL-150 (2db348f1-6660-48c8-8e10-b056131f6baa) and PM4-146 (2c82753c-68eb-449e-85b0-5b21e7c37eba). Sections 6.3, 8 and 10.1 follow my GP16-191 (72b6a06d-acd3-4f7c-a2a9-7e9dadbd3031), and its measurement steps and overflow count follow my WD11-210 (438efd04-e4d1-4b4a-bb03-de909e42ab7e). Searching for fiber members by Grover on separate registers appeared first in GPS3 (05a58278-80b6-40ff-9e8b-dcec501b4b10) and MWG (76d06063-f670-4712-8f30-d52b4c665084), with lookup in classical tables and O(n) qubits. Tree heights and the overflow argument follow MW4 (e93f341a-7965-4a93-b5c4-7b0f7a799c37). Measuring a window before listing a four-input fiber was published first by IFC1 (1294d17f-2acf-4e10-9996-6b4375388f49). Dissection is from Dinur, Dunkelman, Keller and Shamir, CRYPTO 2012, and collimation from G. Kuperberg, arXiv:1112.3333. These citations are context; every step used is proved below.

New here is a uniform variable-arity extension, not an invocation
of a theorem restricted to h=3,4,5. Sections6.3 and10.2 below prove
the complete instruments and a uniform all-height failure bound with
larger explicit capacities. Section8 supplies a new integer schedule
whose windows may saturate at zero; no all-positive-window capacity
argument is inherited. The original source and contextual credits
above identify the actual methods used, not a prior verdict premise.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates are classically addressed through this charge; there is no
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

Cost per call: exactly2(J_e+1)F fixed tests, with O(n^2*h_e)
core steps. Use the ACTUAL profile-independent cap certificate:
Ccap>=K, Qcap=n*Ccap+K<=(n+1)*Ccap and Y=ceil(log2 Ccap)<=n.
Hence log2 Qcap<=Y+log2(n+1)=O(n), h_e=O(n), and the
per-call cost is O(n^3), with O(n) quantum scratch and O(n)
classical bits. This is a fixed polynomial on every branch.
No log2 Qcap=O(sqrt(n)) estimate is used for growing arity.
The polynomial charging in14 includes these actual LE loops;
their outcome law and error bound5.1 are unchanged.

IDEAL reduced run. Use the latent-label product decomposition3.1.
For each query, conditional on its freshly drawn k, LE acts only on
the data factor and fresh test ancillas; the positive control qubit
is a product spectator and is unchanged. Replace LE's returned label
by k in the mathematical ideal process and marginalize all its internal
test, unwrapping and reset records. Only the returned label can affect
subsequent source-level instructions. LE has a fixed call length and
no additional outcome-dependent source request. This ideal label is
an ANALYSIS variable, not a physically assumed source oracle.

Couple actual and ideal executions with common fresh k, original
coins and the same quantum instruments until the first wrong LE label.
At a matched call the data tests do not act on the control factor;
if the label is correct the reduced subsequent operation is identical.
The uniform per-call bound5.1 and the deterministic Qcap therefore
bound divergence by2^-10, without conditioning the ideal law on the
event that all actual extractions were correct. Such conditioning
would bias k and is not used. All actual-branch resource bounds still
follow directly from the fixed loops, allocations and caps.

### 5.7 Explicit reduced fields and random-stopped leaf selection

Treat an accepted supplier delivery as a superstep. In the odd case,
a raw uniform k is accepted iff k<2^(B+1). Summing over every rejected
prefix gives a uniform accepted k on[0,2^(B+1)), independent of the
rejection count: every accepted value has the same geometric-prefix
weight. In the2-adic case k mod2^(B+1) is exactly uniform because
2^(B+1) divides N; its discarded quotient may be marginalized. These
facts hold after the FULL past before each fresh delivery, including
known transformation/shift parameters and outcomes on earlier copies.
Fresh ideal copies keep this property even on a wrong earlier decode.

At an input boundary collimated to p, the retained coarse field Sigma_p
contains: low p bits of accepted leaves in the current construction;
source/delivery counts; all lower-prefix merge outcomes, listing coins,
Grover readouts, lists/tuple incidences, retries, returns and active
leaf identities used by that construction. The full past OUTSIDE the
fresh parent attempt may also be fixed. It does NOT contain unused
higher-label values, full high-part table writes/arithmetic, internal
LE records, discarded numerical/helper bit-read transcripts or gate
emission timing not used by logical selection. Full labels are stored
and later used, but that is not a disclosure into this coarse field.
In particular Sigma_p is not the complete actual input transcript.

Here is the factorization proof for random, stopped inputs. At a fixed
finite cylinder of the accepted-leaf tape, write k_j=l_j+2^p h_j.
Initially its law factors as uniform high blocks times the law of l.
Each lower construction step has prefix p'+b'<=p. Its deterministic
selection/list/branch data use only those prefix bits. Lemmas6.1/6.6
show its quantum outcome kernel is a ratio of low-prefix counts,
independent of the untouched high blocks and secret-dependent phases.
The listing Grover circuit acts on separate fresh registers with an
oracle determined only by those low-prefix constants. Full-label sums
are bookkeeping writes; they do not select tuples using unused bits.
Thus multiplication by each step kernel preserves the product law.
The next touched leaf identity and the stopping decision are likewise
functions of that retained trace. Induction proves the factorization
on every finite cylinder, not merely a fixed successful tree shape.

Summing over cylinders selecting the same finite live leaf sets and
then taking monotone limits proves the same identity at random return
and retry boundaries. Actual caps give finite traces; the uncapped
process used for expectations is handled by the countable-cylinder
limit, and its finite expected termination is proved by height below.
Failed inputs are discarded and never reused, so no failed ancestor
can have exposed higher bits of a retained leaf. Retained siblings
outside a fresh attempt have disjoint leaf sets and may be included in
its full start-past. Conditional on Sigma_p and the l_j, the remaining
high coordinates of the selected leaves are still independent uniform.
The selected incidence vectors themselves are Sigma_p-measurable.

At a current merge reveal its next b bits c_j by
 k_j=l_j+2^p c_j+2^(p+b)u_j.
Because p+b<=B, c_j are independent uniform modulo2^b under this
reduced law, across the pairwise disjoint input leaf sets. Revealing
one input block first leaves every disjoint block uniform. No claim
of independence of entries WITHIN one phase table is made or needed.
The same proof at p=B leaves the top bits tau_j independent fair,
even after the batch's low-bit stopping and nonabort events. It excludes
full root W values and root measurement outcomes from that coarse
batch field, since neither controls construction within the batch.

## 6. Phase vectors, the linear merge and multi-input merges

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical label table
lab[0..2^lam). In the ideal run its state is 2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a
global phase, for a fixed real th. Labels are nonnegative integers. The vector is COLLIMATED TO p
if all lab[x] are congruent modulo 2^p. Labels are stored in full, in fixed fields of 3n bits, which
suffices by Section 9 (label bound).

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x] into a clean w-bit
register, controlled by a lam-qubit index x. For each row x0 it computes the flag [x = x0] with a
Toffoli chain on O(f*lam) scratch, applies CNOTs from the flag to the output bits where tab[x0] has a
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

Cost. Write L=2^lam,L'=2^lam'. Here lambda,b<=O(n).
Nine serial lookup passes have O(n)-bit fields; stable sorting takes
O(L*lambda) comparisons of O(n)-bit keys; binary searches and L'
3n-bit additions give O(n^2*(L+L')) core actions. Quantum scratch
beyond the original index registers is O(n). These are bounds for
the complete bit circuits, without a coherent RAM primitive.

### 6.3 MERGEG(X1, ..., Xf; p, b, lam', kap, r), for f = 2^h, arbitrary integer h >= 3

Precondition: X1..Xf are phase vectors on pairwise disjoint qubits, all of length L = 2^lam >= max(64,8*f), collimated to p, with index registers x1..xf and tables lab_t. Also lam >= 3 kap + 14, lam' <= lam + 1, 0 <= r <= (h - 1) lam, and b = f lam - lam' - kap - r, so b >= h lam. Put G = 2^h-h-1, g = G lam - r, and

    mu = 2^(f lam - b - r) = 2^(lam' + kap),   Cp = 2^(kap + 2) mu,   Cap = 2^(kap + h + 7) L,   D = 2^(kap + h + 9).

Let bb be whichever of lam' + 2 kap + 4 and lam' + 2 kap + 5 makes am = g - bb even, and M = 2^am. Since g >= 2 lam, am >= kap + 8. Let c_t = lab_t[0] mod 2^p, h_t[x] = floor(lab_t[x]/2^p), a_t[x] = h_t[x] mod 2^b and car = floor((c_1 + ... + c_f)/2^p). Bits p..p+b-1 of a tuple's label sum are res(x1,...,xf) = (a_1[x1] + ... + a_f[xf] + car) mod 2^b. Its WINDOW is win = (a_1[x1] + ... + a_(f/2)[x_(f/2)]) mod 2^r.

The tree. Arrange the tables as the leaves of a perfect binary tree of height h. A node v of level j has 2^j tables below it. For a tuple u let s_v(u) be the sum of its a_t over the tables below v, mod 2^b.

Targets. Fix tau in [0, 2^b) and c in [0, 2^r), and let z be a g-bit integer. Z determines a target T_v mod 2^(j lam) for each node v of level j >= 1, top-down. The root has T = tau mod 2^(h lam). A node v of level j >= 2 with children vl, vr takes T_vl, of (j - 1) lam bits, directly from fresh bits of z, and T_vr = (T_v - T_vl) mod 2^((j - 1) lam). At the root only, the low r bits of T_vl are c, and the other bits come from z. The number of bits used is the sum over j >= 2 of 2^(h - j) (j - 1) lam, minus r, which is exactly g.

TREE(z), a fixed Boolean circuit. Each node of level j >= 1 computes a LIST of Cap slots, each a valid bit, a tuple of indices, and its sum mod 2^b. A level-0 node has one slot per table entry. A node v of level j with child lists A, B and target T_v does this:
1. Give each valid slot of A the key s mod 2^(j lam), and each valid slot of B the key (T_v - s) mod 2^(j lam), with one bit recording its side.
2. Sort all these slots by (invalid bit, key) with a Batcher odd-even merge sorting network.
3. For each position q and each d in [1, D], form an output slot, valid if positions q and q + d are valid, have equal keys and have opposite sides, holding the two parts' indices and the sum of their sums.
4. Sort the output slots with valid ones first, again by a Batcher network, and keep the first Cap.

Root-only full-residue pass (step5). After the root has kept its Cap
low-target slots, for EACH fixed slot compute a fresh Boolean flag
 root_record_valid = valid AND [sum = tau modulo2^b].
The full b-bit equality is computed, not merely equality modulo2^(h*lam).
Preserve the original valid bit and sum; the new flag is an output of
the fixed Boolean circuit. Nonroot lists and all Cap truncations stay
as specified above. In a reversible evaluation the equality/AND work
uses fresh ancillas and is uncomputed with TREE; no unknown data bit
is irreversibly overwritten. A ROOT RECORD means ONLY a slot with
root_record_valid=1. Thus ROOT RECORDS are a filtered subset of the
root list, including when a measured guess is unmarked.

MARK(z) is the OR of those root_record_valid flags. This is exactly
the predicate valid AND full-b-bit sum=tau, aggregated over root slots.
The extra root pass takes O(Cap*n) bit gates/ancillas for b=O(n).
It is included with all comparison flags and original unknown wires.
There are f-1 TREE nodes. Each pre-sort/output list has length at most
4*Cap*D=O(f^2*2^(2kap)*L). Round networks to powers of two.
Their address length is O(n), and each full record has O(n) bits;
sorting uses O(length*n^2) comparisons of O(n) gates each.
Thus TREE has O(f^3*2^(2kap)*L*n^3) Boolean actions and at most
that many fresh reversible AND ancillas, with an absolute constant
independent of h. Its description is emitted by uniform finite loops.
Only z is unknown; the source tables are fixed classical constants.
No array of all guesses, coherent RAM or source inverse is used.

Lemma 6.3 (records). A root record of TREE(z) is a tuple with res = e and win = c for tau = (e - car) mod 2^b, whose left-child sums are the left targets given by z. So each tuple is a root record for at most one z, and at most once. Conversely, let u have res = e and win = c. It has a unique z(u), namely its left-child sums. If in TREE(z(u)) no node's list of tuples meeting all targets below and at that node exceeds Cap, and no node has more than D slots with one key, then u is a root record.

Proof. For the first part, every kept slot meets its node's target by construction, the root's left child gives win = c, and the filter gives res = e. Left-child sums mod 2^((j-1) lam) equal the left targets, so z is determined, and a pair is formed at most once. For the converse, res = e gives s_root(u) = tau mod 2^(h lam), since h lam <= b. By induction down the tree, every subtuple of u meets its target. By induction up the tree, each subtuple is in its node's list: its two parts have equal keys, the group holds at most D slots so they lie within distance D after sorting, and the valid outputs are at most Cap, so all are kept. QED.

For clarity, root filtering occurs AFTER the same low-target Cap
truncation. It removes no true-fiber tuple already retained: every
such tuple has sum=tau modulo2^b and passes its flag. Under the
capacity hypotheses of Lemma6.3 it is retained before filtering and
therefore remains a ROOT RECORD. Conversely every appended flag-one
tuple has res=e and win=c. Unmarked guesses append nothing, so Tl
is always a set of distinct members of S. The lost-tuple and Cap
bounds of Lemmas6.6/10.2 therefore apply to this explicitly completed
procedure. This test reads only the consumed label bits below p+b;
it reveals no unused high block and needs no additional source call.

The merge.

1. LOOKUP each a_t into a fresh b-bit register, add these and car (mod 2^b) cleanly into a fresh register Rz, and clear the f registers by repeating the lookups. Measure Rz, obtaining e, and reset Rz from that known value. In the same way compute win into a fresh r-bit register by lookups, measure it, obtaining c, and reset it. Let S be the set of tuples with res = e and win = c, and sz = |S|. Put tau = (e - car) mod 2^b.
2. Listing, on fresh qubits and coins that do not touch the input registers. Draw alpha uniform and odd in [0, 2^g), by measuring H|0> g - 1 times. Start with an empty list Tl. For each block value B0 in [0, 2^bb):
   (a) Prepare am qubits in uniform superposition over v. Put z(v) = alpha^(-1) (B0 2^am + v) mod 2^g, computed cleanly by additions of constants.
   (b) Apply t = floor(pt 2^(am/2)/4) GROVER ITERATIONS, where pt <= pi is a rational within 2^(-am-8) of pi, from Machin's formula as in Section 4. An iteration computes z(v), TREE and MARK reversibly, applying each AND as a Toffoli onto a fresh ancilla; applies Z (that is S S) to the MARK bit; uncomputes; applies H to all am qubits; flips the sign of |0...0> by a Toffoli chain; and applies H to all am qubits again.
   (c) Measure v and evaluate the complete TREE(z(v)) classically.
       Scan ALL Cap root slots in their fixed logical order. Append a
       tuple to Tl IF AND ONLY IF root_record_valid=1, explicitly
       testing valid and the full b-bit sum=tau equality. Before each
       actual append, if the new size would exceed Cp declare FAIL.
       A measured unmarked guess has no passing flags and appends
       NOTHING. Never append an unfiltered low-target root slot.
   Every part of this has a fixed length.
3. Let R have ceil(log2(Cp + 1)) bits, with a one-qubit flag Rf. Both start at 0. For each row rho of Tl compute the flag [(x1,...,xf) = Tl[rho]] with a Toffoli chain on O(f*lam) scratch, CNOT it into Rf and CNOT it onto the bits of R where rho has a 1, and uncompute the chain. Since rows are distinct, on Tl R = rho and Rf = 1, and elsewhere R = Rf = 0. Measure Rf. If Rf = 0 declare FAIL. Let tl = |Tl|.
4. Measure bl = floor(R / 2^lam'). If (bl + 1) 2^lam' > tl declare FAIL.
5. For v in [0, 2^lam'), LOOKUP v -> Tl[bl 2^lam' + v] on the low lam' bits of R, XORing into x1..xf, which become |0>. Reset those registers, Rf and the high bits of R from their known values.
6. Output the low lam' bits of R as the index register, with table lab[v] the sum of the f input labels of Tl[bl 2^lam' + v].

On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers have fixed widths.

Correctness (ideal run). Before step 1 the state is the product of the inputs: equal magnitudes over all L^f tuples, with phases 2 pi (sum of labels) th. Step 2 acts on separate registers, so it does not disturb them. By Lemma 6.3, Tl is a set of distinct members of S. Steps 1, 3 and 4 compute functions of the tuple into clean registers and measure them. So after step 4 the state is the equal-magnitude superposition over the 2^lam' tuples of block bl, with their original phases. Step 5 maps each to its v bijectively. The output is thus a phase vector with table lab, and every label has the same residue modulo 2^(p+b), since all tuples in the block have res = e. So it is collimated to p+b.

Lemma 6.4 (Grover). If exactly one v in the block is marked, the measurement in step 2(c) returns it with probability at least 1 - 5/M.

Proof. Put s = 2^(-am/2) <= 1/16 and th0 = arcsin s, so s <= th0 <= s + s^3. The iterations act in the plane of the marked state and the uniform state as usual, and the marked amplitude after t iterations is sin((2 t + 1) th0). Here t <= pi/(4 s) < t + 1.01, so this angle is within 2 th0 of pi/2. So the probability is at least cos^2(2 th0) >= 1 - 4 th0^2 >= 1 - 5 s^2. QED.

Lemma 6.5 (blocks). For distinct z, z' in [0, 2^g), the top bb bits of alpha z mod 2^g and alpha z' mod 2^g agree with probability at most 2^(1 - bb) over alpha.

Proof. Write z - z' = 2^i m with m odd and i < g. Then alpha (z - z') mod 2^g is uniform on the 2^(g - i - 1) odd multiples of 2^i. Agreement forces its circular absolute value below 2^am, which holds for at most 2^(am - i) of them. The ratio is 2^(1 + am - g) = 2^(1 - bb). QED.

Lemma 6.6 (failure bound). For ANY input tables collimated to p, the measurement laws and every decision depend only on the a_t, car and independent coins, that is on label bits below p+b. With sums over all outcome pairs (e, c), and with lost(e, c) the number of members of S missing from Tl,

    Pr[FAIL] <= 2^(-kap) + sum_(sz > Cp) sz/L^f + E sum_(sz <= Cp) lost(e, c)/L^f.

Proof. Each input-register measurement is a computational-basis measurement of a function of the tuple on an equal-magnitude superposition, so its law is a ratio of counts, independent of phases. Outcomes (e, c) have probability sz/L^f. If sz <= Cp, step 2 does not FAIL, Rf = 0 has conditional probability lost/sz, and given Rf = 1, R is uniform on [0, tl), so step 4 fails with probability (tl mod 2^lam')/tl. Multiplying and summing over the 2^(b + r) outcome pairs, this last term contributes at most 2^(b + r) (2^lam' - 1)/L^f < 2^(-kap). QED.

Cost. There are2^bb blocks and O(2^(am/2)) TREE evaluations
per block. Their number is O(2^kap*L^((G+1)/2)*2^(-r/2)),
uniformly in h. Complete listing costs
 O(f^3*2^(3kap)*L^((G+3)/2)*2^(-r/2)*n^3).
All other serial passes over L,Cp and output rows fit this allowance:
f*lambda<=n and Cp<=2^(2kap+3)*L. The listing quantum scratch,
including original inputs and every reversible AND ancilla, is
 O(f^3*2^(2kap)*L*n^3+f*lambda).
Classical scratch, including Tl and current TREE, fits the same
bound. Constants here are absolute, not constants depending on h.

## 7. Leaf qubits

A LEAF QUBIT is a phase vector of length 2 with table (0, k), for its known label k: a positive qubit whose state in the ideal run is (|0> + exp(2 pi i k th)|1>)/sqrt 2, up to global phase, for a fixed real th. There is no pairing stage in this algorithm; leaf qubits go directly into leaf tables.

## 8. The schedule

Every input exponent lambda_i=lambda. The public level profile is
 Phase A: 0<=i<q, f_i=2, r_i=0;
 Phase T: i=q+j, 0<=j<y, f_i=f,
 r_i=max(0,(G+3)*w-2*Hb-2*(q+h*j)).
Let N0=1,N_(i+1)=f_i*N_i, a_i=log2 N_i and Nmax=N_mu.
Then a_i=i in Phase A and a_(q+j)=q+h*j. Direct substitution gives
 binary: lambda<=c0+Hb+a_i;
 multi-input: (G+3)*lambda-r_i<=(G+3)*c0+2*Hb+2*a_i. (8.0)
This remains true when r_i=0. Since2Hb>=(f-2h+4)w and
G+3=f-h+2, we have r_i<=(h-2)w<=(h-1)lambda.

For nonroot levels put tbmax_i=(f_i-1)*lambda-kappa-r_i.
Root capacity is rootcap_i=f_i*lambda-1-kappa-r_i, which is
tbmax_i+lambda-1. Binary capacity is w+1. Every multi-input
capacity is at least(f-1)w-r_i>=(f-h)w. Thus the y multi-input
levels alone provide more than n consumed bits.

For m levels define Sum(m)=sum_(i<m-1)tbmax_i+rootcap_(m-1).
The increment Sum(m+1)-Sum(m)=(f_m-1)lambda-kappa-r_m>0.
For any batch width1<=B<=n select minimal m with Sum(m)>=B,
then assign its root min(rootcap,B) bits and proceed backwards,
at each nonroot taking min(tbmax,remaining). Set tp0=0 and
tp_(i+1)=tp_i+tb_i. These public arrays are banked or recomputed.
All label bits read are below tp_m=B.

Every multi-input level is full. If any exists, m>=q+1 and
Sum(m)-B<Sum(m)-Sum(m-1)<=(f-1)lambda.
The actual q=f+ceil((f-1)*cbar/(w+1)) binary levels satisfy
 q*(w+1)>=f*(w+1)+(f-1)*cbar>=(f-1)*lambda,
because cbar=ell+6>=c0. Since w>=cbar-1, also f<=q<=2f.
There is no circular parameter choice: cbar is computed from ell,
and w,y are chosen before q,kappa,lambda. The certificate for c0
uses q<=2f, so all conclusions hold simultaneously.
Hence backward allocation never shortens a multi-input level.
MERGEG's exact b=f*lambda-lambda'-kappa-r precondition holds,
including at the root lambda'=1; it implies b>=h*lambda.
Also lambda>=3kappa+14,L>=8f. Lemma10.2 applies uniformly.
Binary MERGE failure remains at most2^-kappa for any input tables.
No positivity of the multi-input windows is needed or asserted.

For all-branch caps put
 K=8192*(8*Ybar+ell+30),Dbar=3*K*Nmax*lambda,
 Dcap=4096*n*Dbar,Ccap=8192*n*Dbar,Y=ceil(log2 Ccap).
The ACTUAL quota has h*y<=u/4+h and q<=2f<=u/16,
so log2 Nmax<=5u/16+h. The public K<=2^19ell,lambda<=n
certificate15 proves directly Y=ceil(log2 Ccap)<=4ell=Ybar.
It does NOT assume Y<=V=u. Thus Y<=Ybar<=rstar<=n and
all decoder grid/K-tail bounds are valid before LE. Every
original source/delivery/cap guard keeps its order. The new
cumulative batched guard13.5 counts all underlying requests.
Also2^Y<=2Ccap, so all decoder grid and K-tail bounds are valid
before LE. Every original source/delivery/cap guard keeps its order.

## 9. BATCH(supplier, B)

Input: a supplier of leaf qubits, where in the ideal run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch has a counter of source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs.

TREE. VEC(0) = LEAF: request lam leaf qubits from the supplier, counting each in a counter D; if D would exceed Dcap, ABORT. These qubits form the index register, bit j = qubit j. With labels k_j, build lab[0] = 0 and lab[x + 2^j] = lab[x] + k_j for x < 2^j. The table has length 2^lam, is exactly the tensor product state in the ideal run, and is collimated to tp_0 = 0.

VEC(i), 1 <= i <= m: repeat: build f_(i-1) inputs, each by VEC(i-1); put out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i) if f_(i-1) = 2, and otherwise out = MERGEG(X1, ..., X_(f_(i-1)); tp_(i-1), tb_(i-1), lam_i, kappa, r_(i-1)); until out != FAIL; return out. A root is VEC(m), evaluated depth-first. Run it K times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a batch ABORTs with probability at most 2^-12/n + 2^-11/n.

Proof. Consider the uncapped ideal process. Fix the FULL past just
before a fresh parent attempt starts constructing ALL f_i inputs.
By5.7 and Lemma10.2, after averaging their fresh construction the
attempt fails with probability at most ep=2^(2-kappa), uniformly in
that start-past. This is not a claim conditional on its full newly
computed input labels. By height induction its input-delivery cost
X has conditional mean at most f_i*V_i. Its own cost and success may
be correlated; no independence between them is asserted.

Let Reach_j be the event that attempt j is entered. It is measurable
at its start, and successive conditional failure bounds imply
 Pr(Reach_j)<=ep^(j-1).
By the tower property and monotone convergence,
 E[sum_j 1_Reach_j X_j]
 =sum_j E[1_Reach_j E[X_j|start-past_j]]
 <=f_i*V_i*sum_j ep^(j-1)=f_i*V_i/(1-ep).
The leaf base is V_0=lam delivered qubits. This also inductively proves
finite expected returns and almost-sure termination at each height.
With tt=1/(1-ep),2^(kappa-2)>=2mu gives
 tt^mu<=exp(mu*ep/(1-ep))<=e<3.
Thus V_m<=3N_m*lam and E[D_inf]<=3K*Nmax*lam=Dbar.
Markov against Dcap gives2^-12/n as claimed.

Each fresh supplier delivery has conditional expected acquisition cost
at most2, by its at-least1/2 acceptance probability after the full
request past. Its request indicator is measurable before that delivery;
a second tower/Fubini sum gives E[total acquisitions]<=2E[D_inf].
This argument does not assume its cost independent of the returned
label or of future tree success. Markov against Ccap gives at most
2^-12/n<=2^-11/n. The actual run matches this uncapped process until
its original acquisition or delivery cap triggers, so the two abort
bounds apply without changing a cap or instrument. QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the REDUCED Sigma_B field of5.7: all low_B
accepted-leaf bits, source counts, low-prefix merge/list/Grover outcomes,
listing coins, tuple incidences, retries, returns and abort decisions.
It excludes unused top bits/full high-label arithmetic records, LE
internal outcomes, full root W values, physical/helper bit transcripts
and root measurements. Although full labels are stored, their unused
high parts are not conditioned on. No batch construction decision
reads a root measurement or full root frequency.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, enumeration, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels
depend only on the low_j, since multiples of 2^B do not change them.
By Lemmas 6.1 and 6.6 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs or tuples on disjoint
coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

### 10.1 The failure bound for MERGEG

Lemma 10.2. In the ideal reduced run, a MERGEG attempt at level i
with f=f_i,h=log2(f),p=tp_i,b=tb_i,lam=lam_i and lam'=lam_(i+1),
conditioned on the permitted Sigma_p construction history of5.7,
has Pr[FAIL]<=2^(2-kappa). In particular this bound holds after
averaging a fresh parent attempt's input construction given its full
start-past; it does not condition on all newly constructed high labels.

Proof. Let Lv be the leaves of its f inputs, a union of pairwise
disjoint sets. Write k_j=l_j+2^p c_j+2^(p+b)u_j. By the finite-trace
and stopped-selection factorization5.7, conditional on Sigma_p and
all l_j, the c_j are independent uniform on[0,2^b). The input incidence
vectors are fixed under that conditioning and use disjoint leaf sets.
All lower merge selection kernels read prefix at most p; unused full
label computations and LE/helper records have been marginalized.
These count kernels require equal index magnitudes, not a shared phase identity on an erroneous earlier decode. Wrong shifts can change phases but not these low-prefix outcome probabilities. Correct decoding phases are invoked only on the correct prior-decoder event. This supplies the precise factorization used in the following counts.

Uniform differences. Each table entry has a 0/1 incidence vector over leaves, and its residue is a known constant plus the sum of c_j over that vector, modulo 2^b. A tuple of entries from several inputs has incidence equal to the disjoint union, and distinct tuples have distinct incidence vectors, by the argument of Section 10. So:

    (U) for two distinct tuples from the same tables, the difference of their residue sums is uniform mod 2^b, because some c_j has coefficient +1 or -1.

Overflow of S. Write an f-tuple as (A, A'), with A from the first k = f/2 tables and A' from the others, and let s(A), s(A') be its two residue sums. Let Z = sum_(e,c) sz^2/L^f, which is 1/L^f times the number of ordered pairs of tuples with the same outcome. There are four kinds of pair:
- Equal tuples: L^f pairs, contributing 1.
- Both parts differ: the same outcome needs the first parts to agree mod 2^r and then the second parts' difference to equal a value fixed by the first parts mod 2^b. By (U) and independence of the parts this has probability at most 2^-(b + r), contributing at most L^f 2^-(b + r) = mu.
- Same first part: by (U) the probability is 2^-b. At most L^(2f - k) pairs contribute at most L^k 2^-b = mu 2^r L^-k.
- Same second part: res equal needs the first parts to agree mod 2^b, probability 2^-b, contributing the same.

Since r <= (h - 1) lam <= (k - 1) lam, each of the last two is at most mu/L. So E Z <= 1 + mu + 2 mu/L <= 3 mu. Since sum_(sz > Cp) sz/L^f <= Z/Cp and Cp = 2^(kappa + 2) mu,

    E sum_(sz > Cp) sz/L^f <= (3/4) 2^(-kappa).                                     (10.4)

Lost tuples. Sum over tuples u, with its outcome (e, c): sum_(e,c) lost/L^f is the sum over u of [u is missing from Tl]/L^f. If u is missing, then by Lemmas 6.3 and 6.4 one of three things happened.

(i) A list or key group overflowed in TREE(z(u)). Fix u. For a node v of level j and l >= 0, let X_j(l) bound, over any shift d, the expected number of subtuples w != u_v below v that meet every target of z(u) at proper descendants of v, and have s_v(w) = s_v(u) + d mod 2^l. Level 0 gives X_0(l) <= L 2^-l by (U). At level j, w = (wl, wr). Either wl equals u's part, or wr does, or both differ, and then the parts are independent. So

    X_j(l) <= (2 + X_(j-1)((j - 1) lam)) X_(j-1)(l).

Let A0=1, A_j=A_(j-1)*(A_(j-1)+2/L). The same induction
gives X_j(l)<=A_j*L*2^(j*lambda-l) for every j<=h.
Here A_j>=1 and natural logarithms obey
 ln A_j<=2*ln A_(j-1)+2/L.
Iterating yields ln A_j<=2*(2^j-1)/L<=2f/L<=1/4,
so ALL A_j<2, uniformly for arbitrary h. This replaces the old
height-five numerical check. Including the distinguished tuple,
each node's expected list length is at most3L, and its true-tuple
key group at most6. The recurrence used independent disjoint child
leaf sets and (U), not independence of entries within one table.
Union over f-1 nodes with the actual enlarged Cap,D gives
 (f-1)*(3L/Cap+6/D)
 <(3/128+6/512)*2^-kappa.



(ii) Another marked guess lies in u's block. By Lemma 6.3 it comes from some w in S with z(w) != z(u). By Lemma 6.5, summing over u, this contributes at most Z 2^(1 - bb), with expectation at most 3 mu 2^(1 - bb) <= (6/16) 2^(-kappa), since 2^bb >= 2^(kappa + 4) mu.

(iii) u's guess is alone and marked in its block, and Grover misses it: probability at most 5/M <= (5/64) 2^(-kappa), by Lemma 6.4.

Failure. By Lemma 6.6 and (10.4), Pr[FAIL] <= (1 + 3/4 + (3/128 + 6/512) + 6/16 + 5/64) 2^(-kappa) <= 2^(2 - kappa). QED.

## 11. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (8 rstar + ell + 30).                                              (11.0)

The stages are j = 0, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. Then J + 1 <= log2 M.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. To supply one leaf qubit, repeat until accepted: acquire a fresh
copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard), and on acceptance apply X to the
control. The batch's acquisition cap applies. In the ideal run accepted labels are i.i.d. uniform on [0, 2^dn), and each copy
is accepted with probability 2^dn/N > 1/2. The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

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

Concentration. By the two-sided Hoeffding bound each fixed candidate's sum deviates from its conditional mean by at least K/64 with probability
at most 2 exp(-K/8192). Outside these events,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625 > (K/2) cos(pi/8) + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the maximizer is not far. There are at most 2^(Y+8)
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(8 Ybar + ell + 30) <= 2^-(Y + ceil(log2 n) + 30), using Y<=Ybar and ell>=ceil(log2 n). The failure
probability is at most 2^(9-30)/n <= 2^-20/n. QED.

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
- If wd >= 2: run BATCH with B = wd - 1, with this supplier. Take the first root with W odd, and measure it in X. By (9.1) it is
  (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2, which gives rem mod 2 exactly. Release the other roots. If no root
  has W odd, set the bit to 0.

By (10.3), and independence of distinct roots given G, each such level misses with probability at most 2^-K, even if s1 was wrong.
Set bit g of s2. In the ideal run with s1 correct and no miss, every bit is correct. Output (s1 + M s2) mod N.

## 13. The complete algorithm and its success probability

Finite branch (ell < 2^20). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome. Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
All resources on this branch are bounded by an absolute constant.

Main branch (ell >= 2^20). Compute a2, M, dn, K, the schedule, Y, and all allocations; define unused J=0 if M=1, otherwise J as Section11; put

    Qcap = n Ccap + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2 = log2 N <= n, there are at most n batches, each using at most Ccap acquisitions, plus at most K for the single wd = 1 level. So Q <= Qcap on every branch. LE is sized by this Qcap, which is computed before h_e.

Success. Include the additional cumulative-guard failure2^-12 proved in13.5. In the ideal run the other failure events are: a batch ABORT, at most n (2^-12 + 2^-11)/n = 2^-12 + 2^-11 (Lemma 9.1); a decoder error, at most 2^-20 (Lemma 11.1); and a 2-adic miss, at most n 2^-K <= 2^-40. Adding the LE coupling (5.1):

    Pr[output = s] >= 1 - 2*2^-12 - 2^-11 - 2^-20 - 2^-40 - 2^-10 >= 1 - 2^-8 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings; there is no conditioning on favorable labels or outcomes.

## 13.5. One cumulative acquisition guard for the actual algorithm

Initialize one known integer Aglob=0 before Section11; never reset it
between batches. At every UNDERLYING source acquisition performed by
a batch supplier, after all original pre-request guards and before
the acquisition/LE, abort the whole algorithm if Aglob+1>Ccap;
otherwise increment Aglob and perform that original acquisition.
Count every rejected, discarded, failed, partial or retried supplier
request, not merely accepted deliveries. The separate wd=1 path
keeps its original capK and is outside Aglob. All original per-batch
Ccap and Dcap guards, ordering, extraction instruments, filters,
listing gates and decoders remain exactly as supplied. Keep the OLD
Qcap=n*Ccap+K for LE accuracy sizing: it is still an upper bound.
The actual all-branch total is instead Q<=Qglob=Ccap+K.

Proof of the extra abort budget. First consider the old ideal process
with all its local caps but without this added cumulative guard.
There are at most n adaptively entered batch slots. Conditional on
ANY history just before an entered batch, Lemma9.1's fresh-attempt
height/tower proof gives E[batch source acquisitions|start]<=2Dbar:
the unbounded ideal construction has that mean, and local guards
stop its coupled prefix. Fresh future source coordinates remain
independent; the supplier shift, B and prior decoder outcome may
be adaptive, but the at-least1/2 supplier acceptance and uniform
merge bounds hold for each such history and secret. Do not condition
on the batch's own newly generated full labels or successful outcome.
Put zero cost in unentered slots. Iterated expectation then gives
 E[all batched acquisitions]<=2*n*Dbar,
without assuming batch costs or successes independent. Couple the
new process to this old process until its added guard fires. That
event requires the old batched count to exceed Ccap, so Markov gives
 Pr[extra global abort]<=2*n*Dbar/Ccap=2^-12.
This argument also covers paths stopped by an earlier local abort.
Add this budget to the original failure union, not as a success
conditioning event. With the original LE coupling still sized by
Qcap, total failure is at most
 2*2^-12+2^-11+2^-20+2^-40+2^-10<2^-8.
No source or merge success probability is multiplied by a favorable
conditioning assumption. The new guard depends only on counters,
which are admitted low-history stopping data; it does not inspect
current high labels, LE outcomes or physical helper transcripts.

Aglob has O(log(Ccap+2))=O(n) bits (here actuallyO(ell)). Its known
integer compare/increment takes O(n) charged bit work per request,
within a fixed polynomial factor of the existing n+1 source charge.
Store the long-lived known field as a counted basis record or one
of constant-many O(n)-bit staged words. Its initialization, access,
address debit and cleanup are charged. All original full allocation
and time envelopes absorb this fixed polynomial overhead. Nothing
is added to the source interface and no acquisition is hidden.

## 14. Complete all-branch resources

All current numerical fields have O(n) bits, f<=ell/32,
mu<=sqrt(n),K=O(sqrt(nh)+ell),2^kappa<=16mu.
Every multiplicative factor in this paragraph outside an explicitly
displayed exponential is bounded by a fixed polynomial in n with
absolute degree and coefficient, uniformly over the actual arity.
Qcap=n*Ccap+K is deterministic and
 log2(Qcap+2)=log2 Nmax+O(log n).
Depth-first retained child tables use at most f*mu families; a current
TREE has O(f^3*2^(2kappa)*L*n^3) actions and unknown AND scratch.
Original phase indices, source/LE scratch and K retained roots are
polynomial. Both full virtual workspaces are poly(n)*2^w.
No all-guess array, leaf-tree-sized cache or candidate grid is stored.

Every attempted level i+1 merge consumes N_(i+1)*lambda delivered
qubits, including discarded inputs of failed attempts. Its count is
at mostDcap/(N_(i+1)*lambda). By the supplied window identity8.0,
its full primitive cost is at most
 poly(n)*2^(Hb+((G+3)/2)*c0)*N_i.
Sum all at mostmu levels and n batches. Include LE's actual O(n³)
fixed loops per acquisition, source moves, binary merges, leaves,
the streamed2^Y decoder grid and full virtual address debit O(n).
The complete result, uniformly on all capped/aborted branches, is
 T_P<=poly(n)*Nmax*2^(Hb+((G+3)/2)*c0).
The target-offset factor remains explicit; it is not a polynomial.
It has logarithm O(f*ell), lower order in the exact limits below.

## 15. Explicit-range root budget and near-quadratic acquisitions

Put t=log2 n,alpha=31/32,x=ell^alpha. The actual q<=2f,
rounded quota and root give logN=q+h*y<=5u/16+h.
The PUBLIC Ybar=4ell sets K=8192*(33ell+30)<=2^19ell.
No actual Y is used to choose K. Also lambda<=n, so
 Ccap=24576*n*K*lambda*Nmax<=2^34*ell*n²*Nmax.
Consequently Y=ceil(log2 Ccap)<=4ell=Ybar at every main
length: u<=ell,h<=log2 ell imply
 log2 Ccap<=2ell+5u/16+h+log2 ell+34<4ell.
Check the cutoff and monotonic logarithm/linear ratios.
This direct proof closes the root-count/label-range certificate
WITHOUT reusing the false old rstar-sized K inequality.

The decoder union bound11 now uses
 exp(-K/8192)<=2^-(8Ybar+ell+30)<=2^-(Y+ell+30).
The old finite grid has at most2^(Y+8) candidate events, so its
same error budget remains valid. Also K>=8192ell implies
n*2^-K<=2^-40. The fresh-attempt tower9 holds for any fixed
positive selected root count K; Dbar=3K*Nmax*lambda and both
local caps use this SAME K. The cumulative guard13.5 then adds
abort probability at most2^-12, retaining total failure<2^-8.
The original LE sizing Qcap=n*Ccap+K with the new K remains
conservative for actual Qglob=Ccap+K. No earlier source instrument,
root filter, local guard order or numeric accuracy budget is omitted.

For queries Qglob<=2Ccap, giving
 log2(Qglob+2)<=2t+5u/16+h+log2 ell+40.
Concavity of z^alpha,0<alpha<1, gives ell^alpha-t^alpha<=1;
u<=ell^alpha+1. Thus
 (1/3)*t^alpha-(5/16)*u>=ell^alpha/48-31/48.
This positive gap pays h+log2 ell+40 uniformly. For a=floorLogell,
h<=a,log2 ell<a+1, a sufficient integer condition is
 u>=48*(h+a+41)+32.
At a=20 the lower x>=2^19 has ample margin over96a+2000.
As a increases,2^(31a/32) grows by a factor greater than3/2
(since2^63>3^32), whereas96a+2000 grows by a factor below3/2.
This proves the condition for ALL main lengths, with no sampled
feasibility premise. Therefore EXACTLY
 Q=O(n²*2^((1/3)*(log2 n)^(31/32))).
The coefficient1/3 and outside polynomial power2 are exact.
This is n^(2+o(1)), NOT a claim Q=O(n²). All unsuccessful,
rejected,discarded,partial,retry and aborted requests count.
The explicit cap-factor accounting144 and fresh-attempt source
completion147 are used only for their declared methods; their
literal profiles, old K values and review verdicts are not premises.

For time,0 yields Hb<=4h*n/u+f/2+1. Complete14 retains
logN=O(ell^alpha), target offsetsO(ell^alpha*log ell), all caps
and polynomial factors. Hence
 log2(T_P+2)=O(n*log ell/ell^alpha+ell^alpha*log ell+ell).
The full physical compiler, global-counter work, initialization and
prefix/pool logarithms fit this order. As alpha-7/8=3/32>0,
 log2(T+2)/(n/t^(7/8))->0.
For full allocation O(n^88*2^w),
 log2(S_Q+2)=O(n*log ell/ell^(31/16)+ell).
Since31/16-15/8=1/16>0, its ratio to n/t^(15/8) tends to0.
These vanishing ratios prove EXACT coefficient1 time/quantum
envelopes with finite outside constants; neither is asserted with
outside constant1 from the very first main length. Every inactive/
padded owner,row,tag,description,basis/source and unknown comparison/
AND wire counts. Physical ordinary staging remainsO(n).
Virtual indices1,1,1,0; physical indices1,0,1,0. No scalar-score
improvement, matching lower bound, positive robustness or optimality
is asserted. Fixed finite tester/epoch exceptions affect constants.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope and limitations

This actual asymmetric variable-arity profile trades higher work for
fewer samples and a smaller quantum index. Physical ordinary classical
space is linear, time index1, quantum index1 and sample index0.
No optimality, lower bound, priority or practical-speed assertion is
made. The ell>=2^20 cutoff and outside constants are unoptimized.
All contextual author/method credits remain. The complete source,
capacity/probability/cost and both decoder arguments are supplied.
Physical helper transcripts are marginalized, never held-out-bit
conditioning fields. Only independent ideal copies are covered.
