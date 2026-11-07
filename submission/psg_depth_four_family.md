# Complete fixed-depth family proof for the selected PSG-D4 algorithm

## 0. Auxiliary family theorem and selected instance

This required appendix is used with psg_depth_four.md,
psg_depth_four_base.md and psg_depth_four_compiler.md. Every claim cites
all four proofs. The auxiliary uniform program below has a public integer
d>=2; the ONE declared PSG-D4 program fixes it to d=4 before any input
copy is acquired. The other depths are a mathematical lemma, not selected
configurations or alternative resource claims. For each fixed d the lemma is

    T=O_d(n^((d+5)/2) log2(n+2) 2^(n/(2d))),
    S_C=O_d(n^2), S_Q=O_d(n),
    Q=2^38 d C_d n^(d+1) exactly,
    epsilon_d(n)=1/(2^31 d C_d n^d),
    C_d=ceil(2*50^d/37^d), success>=1-2^-8,

for every N>=2, every secret, and every adversary in Section 2. Here
n=ceil(log2 N). All four costs concern the SAME execution. They hold on
every branch. The constants may depend on d; they do not depend on N,
the secret, the adversary or the outcomes. No assertion permits d to grow
with n under these bounds.

The new point d=4 has C_4=7 and

    T=O(n^(9/2) log2(n+2) 2^(n/8)),
    S_C=O(n^2), S_Q=O(n),
    Q=7*2^40 n^5, epsilon=1/(7*2^33 n^4).

The structural tradeoff is explicit. One more fixed level changes the
linear time exponent from 1/(2d) to 1/(2d+2), raises the outside time
power by 1/2, raises the source power by one, and lowers the tolerated
fraction power by one. Both space powers stay fixed. This is one family
proof, not a list of unrelated parameter substitutions.

Feasibility rests on five obligations. The same fresh-child law must hold
at d levels. Expected attempt multiplicity must be balanced by actual
integer gaps. The root count must fit deterministic record padding. The
decoder count must allow all d-dependent stages. The literal controller
must pay its R^2 work and all other work. Sections 3--10 prove these facts.
In particular the time power is (d+5)/2, not 3. The existing depth-two
literal-scan barrier is respected.

The finite threshold in this proof is deliberately large:

    n_d=2^(16d^2).

Below it the program executes an exact finite scan, with the SAME Q and
fraction. This is an executable branch, with no advice. It proves an
all-N result with finite d-dependent constants. It does not give a useful
small-N implementation. A smaller threshold is not needed for this theorem.
The main, base and compiler select exactly d=4 throughout. All arguments
needed by that instance are included in these four proofs. No review verdict
is a premise here.

The dependence on d is as follows. The explicit constants n_d,C_d,
Qroot,Proot,Wroot,Hmax and epsilon_d depend on d. So do the number of
frames/stages, signed width n+ceil(log2 q0)+4, the inequalities
n<=2dR and u>=n/(16d), the polynomial degree d+3 in the source allowance,
the exponential absorption constants, and the finite maximum F_d.
The primitive's 64-member bound, 37/50 fresh success, p0, K/n, eta,
128n contamination cap, table accuracy and final success target do not.
These are the exact points that would need new bounds in a separate
analysis with growing d. Such an analysis is outside this theorem.

## 1. Exact inputs and source credit

This proof adapts the following actual local files. Hashes are SHA-256.

| File | Hash |
|---|---|
| psg_depth_two_transfer.md | 2fb8ec6ce3d8d3d38e4c111908e392b7478b7e865db926b7858a196aa9533a07 |
| psg_depth_two.md | dde6a3e55dc20cf1b97d8409287b041e8bc70dbda8b6f29ce55f7254f9eb6ba8 |
| psg_depth_two_base.md | f58e64e83594a4258b40632973ca8e3fb9e042e3290b5441415894d1a961c268 |
| psg_depth_two_compiler.md | ec581df033589d913337deebc4bb2f2bdb57b2b364720999b85ed83c2a0f37ff |
| psg_depth_two_budget.md | 0c56248a73556be95d56a50da421ff8f8723b1b8e2e1530c25a9b90f6b64dbb4 |
| psg14c_streamed.md | e6d8a9d2910bce77ad26c54ee96b60f703bd5ed1f03c021c6ca2bec642242db2 |
| psg14c_streamed_base.md | bba18b26ef7260f1ec1a1c834baa9f545659bf1e887d8c81df8b5fb263562599 |
| psg14c_streamed_compiler.md | 4ff058eb9aa0f631126cd8443b691aa72d3d1ec7884dec06a5236542f71f79c1 |
| psg14c_streamed_budget.md | 2668b8f2c135c52a4911db4766a458f312b24a485e12d06d7cd7b5663b2ab854 |

The semantic inputs are the exact source/extraction, verified disjoint-pair
primitive, unused-block induction, odd arc decoder, multi-bit decoder,
record coupling and finite scan in the two base files. The compiler input
is the fixed-field ready-address/tape-head/marked-strip construction in
the compiler files, G.2--G.4. The new work here is the common fixed-depth
profile, the d-level moment/cap proof and their complete joint integration.
The source arguments needed for that integration are given below.

The direct public source identified by these inputs is PSG14C, submission
30304a9e-15d5-4b58-9998-d5a4ccc1a67e, commit
398d8457f6c25e29a941403e4e75eccb290dda79. Its saved proof and JSON hashes are
2abeb473f0ea10cd5f7305cf58f8696dddd148967337a851183bfc55254ce0b6 and
626dd5115b1e5bf45f6fac74e659a902708ae1a580918daa1daa9b4b684b53d6.
The family was first derived from these local full reproductions. The
same S371 main/base/compiler were then compared with the saved publication
archive for submission 14a7bcaa-b4ea-47e6-8548-ab72eb5ac3c8, commit
49a5f9826710b4fefe536bd13279b74d41da555d. Their hashes are unchanged.
That public budget has hash b9afa4f8a5a8cfae9defb7a86fc302e5e615b485ad609d7292b6a14c38c4c6f4;
the listed local budget has exactly one additional final LF. D2 and the
bounded family remain local derivation inputs. No public identity is
invented for them. Section 12 retains inherited read chronology.

## 2. Exact adaptive model and allowed operations

The following model text is copied from the actual local source.

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

All arithmetic is on explicit bit strings. A bit read/write, gate, head
move, test, allocation, reset, random bit and acquisition is charged.
An indexed action pays O(log(S_C+S_Q+2)) additional bit work. Gates are
generated online. There is no source inverse, controlled source, source
purification, QRAM, state-copy operation or subset-sum oracle.

Use H and exact reversible NOT/CNOT/Toffoli circuits, plus S and S-dagger.
One phase-free Toffoli on a,b,c has the literal word

    H(c),CX(b,c),Tdag(c),CX(a,c),T(c),CX(b,c),Tdag(c),
    CX(a,c),T(b),T(c),H(c),CX(a,b),T(a),Tdag(b),CX(a,b).

The identity 4abc=a+b+c-(a XOR b)-(a XOR c)-(b XOR c)
+(a XOR b XOR c) checks its phase. Replace Tdag,S,Sdag,Z by 7,2,6,4
copies of T as needed. Ripple add/subtract/compare has a fixed number of
Boolean nodes per bit, O(w) gates and O(w) reusable carry scratch.
Compute a permutation into zero, swap and evaluate its inverse to clear
the old input. Quantum modular addition fixes encodings >=N; the inverse
adds the negative constant modulo N. Every helper clears on every input.
Classical product, restoring division and extended Euclid use polynomial
bit work and O(w^2) bits. These operations give total CRT and remainder
computations; only proven units are inverted.

## 3. One exact finite profile for all d

For n>=n_d let ell=ceil(log2 n). Start at R=ceil(n/(2d)). At each trial set

    c=ceil(log2(3(2R+1)))=bit_length(3(2R+1)-1),
    v_i=R-(d-i)c,  i=1,...,d,
    F=2 sum_i v_i=2dR-d(d-1)c.

Accept the first trial for which v_1>=ceil(R/2) and F>=n. Otherwise
increase R by one. This is exact integer search; no monotonicity of F
is assumed. Put q0=(2R+1)^d and u=floor(R/4).

Here are sufficient scalar bounds, valid for every d>=2 and n>=n_d:

    n>=16d^2(log2 n+3),
    d(ceil(log2 n))+9<=n/32,
    log2(193d)<=n/16, n/(2d)>=256.                 (F1)

For completeness, at n=n_d write m=16d^2. The first two follow from
2^m>=16d^2(m+3) and 2^m>=32(d(m+1)+9). The last two are weaker.
They hold at d=2. As d increases, each polynomial right side increases
by a factor at most 6, while 2^(16d^2) increases by at least 2^80.
The real differences increase for n>=n_d: their derivatives have the
forms 1-A/(n ln2), with A<=32d^2. Use ell<=log2 n+1. This proves (F1)
also between powers of two, without treating the ceiling as continuous.

Consider the trial

    Rtest=ceil(n/(2d))+ceil((d-1)(ell+2)/2).

It has Rtest<=n/(2d)+d ell<=9n/32<n/3 by (F1). Hence
3(2Rtest+1)<=4n, so its c<=ell+2. Its capacity is at least n.
Also Rtest>=n/(2d)>=8d(ell+2)>=2(d-1)c. Thus it meets the positive
width condition. The trial search terminates, with

    n/(2d)<=R<=Rtest<=n/(2d)+(d-1)(log2 n)/2+(3d+1)/2,
    2^R<=2^((3d+1)/2) n^((d-1)/2) 2^(n/(2d)),
    v_i>=R/2>=u>=R/8, n<=2dR<=16du,
    R<n/3, 2R+1<=n, q0<=n^d.                    (F2)

The strict scalar slack makes the last two integer statements valid.
The number of trials is O_d(log(n+2)); each uses polynomial bit work.

For every requested 1<=D<=n and 0<=B<D allocate widths from i=d down
to 1: b_i=min(2v_i,remaining), then subtract b_i from remaining. Since
F>=n>B, remaining ends at zero. Put r_i=b_i+1 and p_i=sum_(j<i)b_j.
A zero width returns its child; B=0 returns a leaf. Each positive level
uses the same primitive in Section 5 with k=r_i=b_i+1. Thus

    product_active r_i<=q0.

The returned full signed label is divisible by 2^B. Its quotient W
satisfies |W|<2^(D-B)q0. A returned phase has a nonzero incidence vector
in {-1,0,1} on disjoint original leaves. The program does not store that
vector. Numeric fields have w_s=n+ceil(log2 q0)+4=O_d(n) bits, also
after wrong numerical labels. No high label, zero label or odd W filter
is introduced. Greedy widths include every partial and zero-width case.

## 4. Exact source, table and label extraction

Write N=2^a M with M odd, D0=floor(log2 N), omega=exp(2pi i/N).
For chi_k=N^(-1/2)sum_x omega^(kx)|x> and
phi_k=(|0>+omega^(-ks)|1>)/sqrt2, direct character orthogonality gives

    rho_s=(1/N)sum_k |phi_k><phi_k| tensor |chi_k><chi_k|.

Thus a clean input is exactly a mixture with uniform latent label k.
Applying X gives the positive-phase control. The permutation x->alpha x
mod N, for a known unit alpha, maps rho_s to rho_(alpha s). It uses n
known controlled additions and the known inverse alpha^-1, O(n^2) gates
and O(n) quantum scratch. The controlled shift x->x-sh mod N on row 1
maps rho_s to rho_(s-sh), with O(n) gates. Both fix invalid data encodings.

Compute a 4096-entry rational sine/cosine table at denominator 2^20.
Machin's formula pi=16 atan(1/5)-4 atan(1/239), using 40 terms of each
alternating series, gives pi error <2^-90. The first 80 Taylor terms at
the resulting angles in [0,7] leave error <2^-170. Round to denominator
2^20. This fixed finite computation is charged. With
tab_beta(x) the table entry at floor(4096x),

    |tab_0(x)-cos(2pi x)|, |tab_1(x)-sin(2pi x)|<1/625.

Clamp every used value to [-1,1]. Clamping cannot increase these errors.

EXTRACT(P) uses J_e=n+4, h_e=ceil(log2(2^16 P(n+5))), F_e=2^21 h_e.
For each X/Y basis take F_e collective rounds. A round prepares n+5
Hadamard ancillas representing x=sum_j x_j2^j, computes z=x mod N,
applies the register-controlled translation u->u-z mod N, then clears
z and its helpers. Since x<64N, the remainder uses exactly six known
compare/subtract passes with 32N,16N,...,N and six reversible borrow flags.
It uses O(n) gates and O(n) quantum scratch. On chi_k its ancillas are
exactly tensor_j (|0>+omega^(k2^j)|1>)/sqrt2; chi_k is unchanged.
Measure in the chosen basis, update n+5 empirical counters, reset, repeat.

For each j choose the least r in [0,64) maximizing the rational dot
product of its empirical X/Y means with table direction r/64. If both
means are within 1/1024 of their true means, each dot error is <1/256.
The nearest direction has dot >=511/512; a direction at circular
distance >=1/16 has dot <=31/32. Thus the selected alpha_j is within
1/16 of 2^j k/N. Starting at g_(J_e)=alpha_(J_e), repeatedly select
the preimage g_(j+1)/2 or (g_(j+1)+1)/2 closer to alpha_j, ties first.
The correct preimage is within 3/32, the other beyond 13/32. Error
halves at each step. Output floor(N g_0+1/2) mod N, always in [0,N).
If all empirical bounds hold it equals k, since final error <1/(2N).

The bounded-variable exponential estimate gives per empirical mean
failure <=2exp(-F_e/(2*1024^2))=2e^(-h_e). Union over both bases
and n+5 levels gives label error <=4(n+5)2^(-h_e)<=1/(2^14 P),
uniformly in k. With at most P adaptive calls their total error is
<=2^-14. This is an additive coupling; no later low-bit law is
conditioned on successful extraction. Internal test outcomes are not
used by the algorithm after extraction. At main P=O_d(n^d) and finite
P=2^40n^4, h_e=O_d(log(n+2)). Retain the conservative complete charged
cost O_d(n^2 log2(n+2)^2) per call, O_d(n^2) classical bits, O(n) qubits.
It includes counters, all indexed work, decoding, transforms and resets.

## 5. The fixed verified disjoint-pair instrument

For a positive width b=b_i put k=b+1 and p=p_i. Fresh child controls
have phase labels a_j divisible by 2^p. Their joint index is the equal
magnitude state with phase A(y)=sum_j y_j a_j. Set
c_j=(a_j/2^p) mod 2^b. Compute f(y)=sum_j y_j c_j mod 2^b, measure e,
and reset its measured register. Hold this index throughout discovery.

Discovery uses separate fresh query registers. If k<=7 enumerate its
at most 128 strings and keep the first 64 valid strings. Otherwise use
at most 64 blocks of at most 64 trials. A trial draws j uniformly from
[0,J0), J0=2^ceil(k/2), prepares |+>^k, makes j Grover iterations for
f(z)=e excluding the found list, measures, classically verifies its
residue and novelty, and resets query work. A successful trial ends
that block and adds its new string. Stop after an empty block or 64
found strings. Every list element is distinct and verified.

Sort the list and pair adjacent strings, dropping a singleton. On the
held original index compute a success flag and constant-size pair ID.
Measure them. An unpaired outcome fails; discard all children and work,
then start with fresh children. Otherwise the state has exactly two
known equal-magnitude terms y0,y1. XOR y0, select a differing pivot,
and use CNOTs to clear the other differing positions. The output control
has full signed label A(y1)-A(y0), divisible by 2^(p+b). It has a
nonzero signed incidence vector because child leaves are disjoint and
y0!=y1. Discovery and selection use only the stated low residues.
They are independent of the held phase and inspect no high block.

Membership uses k controlled additions of b-bit known constants, an
equality comparison, at most 64 string exclusions, a sign, then the
literal inverse. Scratch is cleared after each addition and reused.
Diffusion uses H passes and a clean Toffoli chain. These circuits are
exact, with O(kb+64k) gates per oracle, O(k+b) live quantum helpers.
Section 9 gives the full online generation cost, including known-bit reads.

Here is the complete fresh-node success argument. For independent uniform
c_j modulo 2^b, fix the first b weights and let O be the support of
their odd subset counts. A uniform last weight translates O. Expected
odd support of the full counts is 2|O|-2|O|^2/2^b<=2^(b-1).
The measured fiber has size-biased mass. Complete pairing loses one
string per odd fiber, hence loses at most 1/4 on average.

For a uniform index Y let X=|f^-1(f(Y))|-1. For two distinct z!=Y the
rows z-Y have distinct nonempty supports. One coordinate in a support
difference and one in the other nonempty support give a determinant
+1 or -1 minor. The two linear forms are jointly uniform modulo 2^b.
Therefore E binom(X,2)=binom(2^k-1,2)/2^(2b)<2 and
Pr[fiber>64]<2/2016=1/1008.

If 1<=m<=64 solutions remain and k>=8, put sin^2 gamma=m/2^k.
The exact two-dimensional Grover rotation gives the uniform-j mean
1/2-sin(4J0 gamma)/(4J0 sin(2gamma))>1/4, because
sin(2gamma)>=sqrt(2/2^k) and J0>=sqrt(2^k). A block misses while a
solution remains with probability <=(3/4)^64<2^-16. Over 64 blocks
premature stop is <1/1024. The small branch is exact. Thus, before
fresh children are generated, the node succeeds with probability

    >=3/4-1/1008-1/1024>37/50.                    (F3)

This is not a success bound for an arbitrary fixed child list. A returned
pair is exact even when discovery is incomplete. Retries discard all inputs.

## 6. d-level law, local caps and exact record counts

Induct on the active levels of an ideal uncapped tree. A leaf has a uniform
numeric label modulo 2^D. If children cancel p bits, their returned
quotients are independent uniform residues modulo 2^(D-p), conditional
on external history before each fresh call. Equation (F3) gives a
conditional geometric tail and almost-sure termination at the next level.

Fix any finite successful low transcript through that level. It contains
leaf values only modulo 2^(p+b), all relevant residue/search/pair outcomes
and retry choices. Its probability kernel depends only on these low bits:
the held index has equal magnitudes and all queries are separate. Write
each used leaf as u_l+2^(p+b)H_l. Its uninspected H_l are independent
uniform blocks. The output quotient is c0+sum_l z_l H_l, where at least
one z_l=+1 or -1. Hence it is uniform modulo 2^(D-p-b). Sum over all
finite successful transcripts to close the induction. Fresh disjoint
calls give the next independent child law. Full high labels may be stored,
but are not conditioned on in this marginal proof. No cutoff or label-error
event is conditioned on. This induction works at every finite d.

For a root with h=D-B>=1, the same proof leaves independent uniform
tau_l in [0,2^h), with W=c0+sum z_l tau_l. For every real y,

    |E exp(2pi i yW)|<=D_(2^h)(y),
    D_A(y)<=|cos(pi y)|,
    D_A(y)<=min(1,1/(2A||y||)) for ||y||>0.        (F4)

The first bound uses one nonzero coefficient. Binary digits factor a
uniform block's characteristic function, giving the cosine bound. The
geometric sum and |sin(pi y)|>=2||y|| give the last bound. In particular
W mod 2^h is uniform. This does not assert a uniform signed integer W.

Let a0=50/37. An accepted odd leaf costs <2 source copies on average;
a direct 2-adic leaf costs one. Conditional geometric sums give

    E acquisitions<=2 a0^d product_active r_i<=C_d q0.

Attempt cost and success can depend on each other. Reaching a retry
depends only on preceding failures; its fresh child-generation expectation
has the same bound. This proves the displayed inequality without a false
cost/success independence assumption.

The expected number of level-i attempts in one root is at most

    a0 product_(active j>i)(a0 r_j)
      <=2 [3(2R+1)]^(d-i)<=2*2^((d-i)c).

Skipped levels only insert upper factors. Multiplying by 2^v_i and
summing gives expected weight <=2d*2^R. Select exactly

    Qroot=1024 C_d q0, Wroot=2048d*2^R,
    Proot=1024 C_d n^d, K=2^17n,
    Hmax=2048dK=2^28dn, Qtot=2^38d C_d n^(d+1).   (F5)

Before each source acquisition check Qroot. After building children,
before a positive attempt's query/array setup, check and charge its
weight against Wroot. A failed check ends only that root, with a neutral
score-0 record. Prior children and work remain charged. Local Markov
bounds on the uncapped clean reference process give loss <=1/1024
for each cap. EXTRACT(Qroot), including rejected leaves, adds <=2^-14.
The clean capped/uncapped outcome laws therefore couple with loss

    p0=2/1024+2^-14=33/16384.                     (F6)

This is an unconditional fresh-record bound. It includes its own retries,
neutral abort and numerical errors. Equal held magnitudes preserve the
numeric low-label/resource law also after wrong earlier decoder scalars;
correct phase identities are needed only on correct earlier estimates.

Every actual root starts from reset scratch. If it succeeds measure ONCE
in a fresh fair X/Y basis. Store its bounded frequency, basis and sign.
On abort store a neutral tag. Then acquire/discard until that record has
exactly Proot copies; use a separate padding counter, not Qroot. Reset
all nonrecord work. The fit Qroot<=Proot follows from q0<=n^d, on every
state. Later records/stages still run. After saving the final candidate,
consume Proot-copy dummy records to make exactly Hmax records, then return.

Section 7 proves that actual stages use fewer than Hmax records. Thus
every main branch has exactly Qtot copies. The finite branch of Section 8
pads directly to the SAME Qtot. With the stated epsilon_d,

    floor(epsilon_d(n) Qtot)=128n                    (F7)

for every n>=1. All rejected, aborted, root-padding, dummy and finite-padding
copies are included. This is not a per-copy noise probability.

## 7. Both exact decoders and the number of stages

Put hmax=1+floor(R/32). Compute a by trailing zero bits; M is odd.
There is no odd factorization. If M=1 set s1=0 and skip only odd stages.
Keep K positive. Otherwise put

    h=min(D0-a,hmax), B=D0-h>=a,
    stride=max(1,h-4), nq=2^(h-1)q0.

Odd stage j starts at j=0. Compute the unit alpha_j by CRT with
alpha_j=1 mod 2^a and
alpha_j=2^(j stride)(2^(B-a))^-1 mod M. An odd leaf acquires a fresh
copy, applies Mult_alpha_j, runs EXTRACT(Qroot), accepts iff k<2^D0,
and applies X. In the ideal law acceptance is >1/2 and the accepted
numeric label is uniform in [0,2^D0). A PS_TREE(D0,B) root has exact
phase exp(2pi i f theta), f=2^(j stride)W, theta=s1/M, since
2^(B-a)alpha_j=2^(j stride) mod M. Take K isolated records.

Let P_j=j stride+ceil(log2 nq)+8. Stage zero scans every c in [0,2^P_j).
Later stages scan the one or two exact integer intervals within circular
radius 2^-(j stride+2) of the preceding center. Their endpoints are grid
points, since both denominators divide 2^P_j. Use the score

    sum_i Z_i clamp(tab_beta_i(((f_i c) mod 2^P_j)/2^P_j),-1,1),

with zero for neutral records. Keep the least maximizer z_j=c/2^P_j.
Enumerate integer intervals in increasing order with exact streamed
residue additions. Take the least positive Sodd with
2^(Sodd stride+2)>2M; run j=0,...,Sodd-1 and set
s1=floor(M z_(Sodd-1)+1/2) mod M.

Here is the full ideal arc argument. Fair basis/sign measurement makes
an exact trig score have mean (1/2)E cos(2pi f(theta-zeta)). The nearest
grid candidate exists also at arc endpoints. Since |f|<2^(j stride)2nq,
its phase error is <2^-8, and its mean is >=cos(pi/128)/2. A far candidate
has circular error >=2^-(j stride+stride+2). In the input arc its scaled
error x=2^(j stride)|theta-zeta| is in [2^(-stride-2),1/2]. For h<=4,
stride=1, so (F4) gives mean <=cos(pi/8)/2. For h>=5,
stride=h-4 and the geometric bound in (F4) gives <=1/16, which is smaller.
The common near/far gap is >0.0379. A selected nonfar point gives exactly
the input radius for the next stage. The final radius is <1/(2M), so
the stated circular rounding returns s mod M on good stage events.
Stage zero's full grid is used in every count; no later-arc count is
incorrectly applied to it.

For the 2-adic part start g=0,t0=0. While g<a put
wd=a-g, h=min(wd,hmax), sh=(s1+M t0) mod N. A leaf acquires a fresh
copy, applies Shift_sh, runs EXTRACT(Qroot), applies X and uses numeric
kk=k mod 2^wd. Take K records from PS_TREE(wd,wd-h). Scan every
r in [0,2^h) using score

    sum_i Z_i clamp(tab_beta_i(((W_i r) mod 2^h)/2^h),-1,1).

Keep the least maximizer, set t0<-t0+2^g r and g<-g+h, then continue.
If wd-h=0 the tree is one leaf. There is no odd-W filter or root reuse.
On a correct preceding prefix s-sh=M2^g rem mod N. The root phase is
exp(2pi i W rem/2^h); (F4)'s uniform quotient gives mean 1/2 at the true
r and zero at every wrong r. Induction recovers all bits. Without a
correct prefix no such phase identity is assumed, but all numeric words,
loop bounds and guards are unchanged. Save (s1+M t0) mod N in all cases.
If a=0 this decoder has no stages.

For the counts, R>=256 by (F1). If h=hmax, stride>=R/64, whence
Sodd<=64n/R+1<=128d+1. If h<hmax, log2 M<h+1 and the stride rule
gives Sodd<=8. The number of 2-adic blocks is
ceil(a/hmax)<=32n/R+1<=64d+1. Total stages <=192d+2<=193d<2048d.
Each uses K records, independent of all outcomes. Thus (F5)'s dummy
count is nonnegative, also if one part is absent.

Each odd grid has at most 2^(ceil(log2 nq)+8) candidates, including
stage zero; later grids have no more. With (F1),(F2),

    log2(candidate count)<=h+d ell+8<=R/32+d ell+9<=n/24<n/16.

The 2-adic grid is smaller. By (F1) all candidate-stage pairs together
are at most 2^(n/8). Candidate sets are fixed at stage start even when
their centers are random. All numerical widths are O_d(n).

## 8. Adaptive contamination, success and the finite branch

Reset by measurement and conditional X leaves pure zero scratch even
after reference entanglement. Retained classical history and the supplier's
conditional private state can be arbitrary. Condition on all previous
real and virtual classical history and the actual current stage inputs.
Couple a virtual clean capped record to the real one until its first
malformed delivery. Before it, both active states agree and deliveries
are fresh ideal products. After it, continue the virtual record with its
ideal conditional kernel and fresh analysis randomness. This is a coupling
of outcome laws; it is not an extra physical source or a state copy.

The pre-delivery decision rule makes this prefix coupling valid. Its full
virtual marginal is the fresh clean capped-record law. It never conditions
that law on actual noncontamination, cap survival or correct extraction.
Use actual stage inputs, not earlier virtual centers. Padding is included
and resets remove quantum carry-over before the next record.

Each bad copy contaminates at most one record. By (F7), at most 128n
records are contaminated globally, even if the adversary concentrates
them in one stage. For all candidates at once, actual/virtual average
score error is at most 2(128n)/K=1/512. No independence of corruption
events, malformed states or actual records is used.

For a fixed stage candidate the virtual centered increments have
conditional interval width 2. Their conditional exponential moment is
<=exp(lambda^2/2): convexity reduces to the two endpoints, and the
tilted variance is <=1. Iterate this conditional bound and optimize lambda.
At t=1/512 the two-sided deviation bound is

    2exp(-Kt^2/2)=2exp(-n/4)<2^(1-n/4).

The mean error caused by (F6) and the rational table is <=2p0+1/625.
Combining mean, concentration and contamination gives per-side error

    eta=2p0+1/625+1/512+1/512
       =48817/5120000<0.009535.

Twice this error is smaller than both the odd gap 0.0379 and the 2-adic
gap 1/2. Conditional stage-start union bounds and induction on good
earlier arcs/prefixes recover the entire secret. Section 7's total pair
count makes the main failure <2^(1-n/8)<=2^-8 for all n>=n_d.

For n<n_d do not compute a main profile. Make mF=2^20(n+16) one-copy
shadow records. Each uses one untransformed raw input, EXTRACT with the
distinct old precision P_old=2^40n^4, X, one fresh fair X/Y basis and
one sign measurement. Reset between records. Scan every t in [0,N),
with exact residue kt mod N and the same clamped rational score. Keep
the least maximizer, SAVE it, pad to Qtot, then return it.

The acquisition fit is mF<=2^25n<=Qtot for every n>=1. The true ideal
score mean is 1/2 and every wrong mean is zero by character orthogonality.
Numerical labels change a mean by <=2^-13; the table by <1/625. Thus
virtual conditional means are >3/8 at the true t and <1/8 otherwise.
At t_deviation=1/16, martingale union over N<=2^n gives

    failure<=2^(n+1)exp(-mF/512)
            <=2^(n+1-2048(n+16))<2^-20.

Outside that event virtual averages are >=5/16 and <=3/16 respectively.
Contamination changes them by at most 2(128n)/mF<1/4096. The true
maximizer remains unique. Padding cannot alter the saved output.
This proof is valid for every n, so it applies throughout the enlarged
finite branch. It includes n=1,N=2. Both branches therefore have
unconditional success >=1-2^-8 under exactly the model in Section 2.

## 9. Literal online compiler, including short rows and failed work

The selected controller is the source G.2--G.4 ready-address construction,
with the following complete fixed-depth substitutions. Pad each DATA row
to a power-of-two stride. An address is base+(row<<shift)+bit; no two
variable address words are multiplied. Allocate only the one active
residue array, labels, found list, reusable scratch and fixed-type fields.
The simultaneous bounds in Section 10 give

    A=ceil(log2(M_alloc+2))=O_d(log2(n+2)).

Keep a fixed number of ready operand-address words on fixed work tapes.
A gate names those fields and pays A for each fixed-arity operand use.
Every address construction, copy, bit change, known-bit read, test and
physical head move is also charged and receives the same A debit.
There is no instruction/address copy assumed free. The finite program
does not store a gate-description tape.

At a full scan's start, set up each ready pointer in O(A) raw bit actions.
For a unit increment/decrement let a physical head walk the carry bits
and return to the low marker. From any initial value, across m successive
steps bit h changes at most floor(m/2^h)+1 times. Summing gives
O(m+A) bit/head work, including the returns and wrap marker. Fixed
power-of-two strides have the same proof. A marked strip controls bit
passes; its traversal, endpoint tests and rewind use O(m+1) raw work.
Inverse passes reverse these same scans. Thus a fixed number of complete
m-bit ripple/copy/compare scans costs O(m+A) raw work, also for short
or empty scans. No worst-case constant delay per individual gate is used.

Build the global w_s-bit signed-label strip once during polynomial setup.
After a positive attempt passes its weighted guard, build its b/k/counter
strips with O((b+k+1)A) raw work. They are reused throughout that attempt.
Do not place an endpoint by an n-cell walk inside a short row. By (F2),
A=O_d(u)=O_d(v_i), n<=2dR and v_i>=R/2.

Form each b-bit residue row by setting a ready child-label address once,
adding p once and reading its indexed bit slice. Two's-complement signed
bits give the correct residue for negative divisible labels. This costs
O(k(b+A)) raw work, with no full n-bit seek per residue bit.
Each oracle uses k complete controlled b-bit row additions and their
inverses, an e comparison, at most 64 complete k-bit string exclusions,
marking and flag cleanup. Each actual known bit is read, including zero
bits that select identity slots. Cleared O(b) carry scratch is reused
per row; no kb-node quantum history is retained. Therefore its raw work is

    O(k(b+A)+b+A+64(k+A))=O_d(v_i^2).

Diffusion's H passes and clean forward/reverse Toffoli chain cost
O(k+A). The j draw/decrement/full limit test has width ceil(k/2)<=v_i+1
and costs O(v_i+A), even if performed after every iteration. At most
4096 trials each have fewer than 2^(v_i+1) iterations. All exact finite
Clifford+T expansions are included. The complete discovery raw cost is
O_d(v_i^2 2^v_i), uniformly in random j, list contents and input states.

One-off work uses these same complete scans: initial f(y), its measurement
and reset, fresh query preparation, query measurements/resets, classical
residue/novelty verification, sorting the fixed list, original-index pair
flags and their resets, pivot selection, XOR and affine clearing. All
failed searches and failed projections execute bounded prefixes of these
words and then paid cleanup. The full signed output uses O(k) scans of
w_s=O_d(n) bits, hence O_d(nk)=O_d(R^2) raw work. Negative and zero labels
execute the same words. Array/list/strip clearing and release fit these
scans. A weighted check costs O_d(R+A) raw work and is included. A failed
weighted check allocates no parent query/array; prior children stay charged.

After the full A debit, every paid attempt on every branch has cost

    O_d(R^2 log2(n+2) 2^v_i).                       (F8)

This bound includes full setup, known-bit scans, ready operands, inverses,
random-loop control, signed output and cleanup. All parent query/strip
buffers are created after children and released before new children.
Thus recursion does not keep an extra query array at each active depth.
The profile's d frames have only ordinary bounded metadata and child labels.

The all-state weighted guard in (F5) gives at most
O_d(R^2 log2(n+2)2^R) combiner work per actual root, including children
in failed ancestors. Summing over <2048dK=O_d(n) actual roots and using
(F2) proves

    T_comb=O_d(nR^2 log2(n+2)2^R)
          =O_d(n^((d+5)/2) log2(n+2)2^(n/(2d))).  (F9)

The R^2 scan factor is retained. No n^3 outside prefactor is substituted
at depth two or any other depth.

## 10. All remaining work, hard bounds and simultaneous storage

Source transforms, EXTRACT, source/work guards, counters, reset and the
raw n+1 cost retain the conservative O_d(n^2 log2(n+2)^2) allowance per
source event. There are exactly Qtot=O_d(n^(d+1)) acquisitions. Thus
even charging this full allowance to all padding gives polynomial
O_d(n^(d+3) log2(n+2)^2) work. Padding in fact runs only acquire/discard,
reset and counters. These costs are charged before absorption in (F9).

Depth-first recursion, zero-width returns, full-label metadata and partial
stack release have polynomial_d(n) work per source/attempt event. Source
events already have a polynomial total. Every paid positive attempt has
weight >=2^u; hence all roots have at most O_d(n2^(R-u)) such attempts.
Since u>=R/8>=n/(16d), any fixed polynomial_d(n) times this count fits
(F9): divide by 2^R and bound polynomial_d(n)2^(-n/(16d)). One failed
source or weighted check ends only that root, with d-frame cleanup.
There are O_d(n) such final propagation events. Executed children and
last partial calls are never removed from the charged count.

The odd full grid has O(q0 2^h) points; the 2-adic grid has 2^h points.
Each score uses K=O(n) stored bounded records and O_d(n)-bit exact
products, remainders, table reads, clamps, additions and least-tie tests.
Streamed interval setup and residue updates have polynomial_d(n) work
per candidate. Since h<=1+R/32 and there are O_d(1) stages, their total
is polynomial_d(n)2^(R/32). The positive 31R/32 gap to (F9) absorbs
every fixed polynomial. Table construction, CRT, profile search, layout,
precision setup, initialization and every loop-strip/head allocation are
charged polynomial computations. These statements require fixed d.

There is an explicit bound on all d-dependent absorption constants.
For any integer p>=0 and a>0, the maximum of x^p exp(-ax) for x>=1
is finite, bounded by max(1,(p/(ae))^p). Apply it to each polynomial
term with a=ln2/(16d), 31ln2/(64d), or ln2/(2d), as appropriate.
The polynomial degrees and coefficients come from the fixed bit loops
above, the rational integer C_d and the exact d-level bounds. Thus no
unstated dependence on N is placed in a constant.

On n<n_d, the finite scan explicitly enumerates N candidates, makes mF
fixed-length EXTRACT calls, and pads to Qtot. Its loop lengths depend
only on N,d. All measurements are finite-bit measurements, and all data
are bounded strings. Taking the maximum primitive step count over the
finite set 2<=N<=2^(n_d) therefore gives a finite computable bound F_d.
It is a bound on actual fixed program loops, independent of states and
outcomes. The time representative in Section 0 is positive for every
n>=1, so multiplying by max(1,F_d) covers this whole branch. No stored
solution, infinite search, validity threshold or nonuniform advice occurs.

For storage, a depth-first tree with active widths b_i has at most
1+sum_i(r_i-1)=B+1<=n held/current sibling phase qubits. Original-index,
separate query, reused row carry, extraction, transform and one padding
slot add O(n) qubits. Parent queries do not remain live during child
generation. There is no general quantum divider or quantum-addressed table.
The collective quantum remainder has only the six O(n)-scratch passes.
So S_Q=O_d(n) simultaneously on every branch.

The corresponding O(n) signed labels each have O_d(n) bits. The one
active k-by-b residue DATA array, found list, K-record bank, streamed
candidate residues, ordinary exact arithmetic, d frames, counters, strips,
head locations and the fixed number of ready operand fields use O_d(n^2)
classical bits. Record banks are reused between stages. No exponential
candidate table, symbolic incidence tree, gate list or O(R^2)-entry
address/instruction tape is stored. Polynomial source counts need only
O_d(log(n+2)) counter bits; the weighted counter has O_d(R+log(n+2)).
Thus A=O_d(log(n+2)) as used in Section 9, without circular extra storage.
The finite branch has mF=O(n) records and the same O(n^2),O(n) peaks.

Malformed states, incorrect labels, wrong earlier scalars, all local
aborts, failed pair projections, empty search blocks and dirty resets
are covered by the total bounded templates and before-action guards.
Final odd outputs are reduced modulo M, each 2-adic update appends an
h-bit residue, and the final output is always (s1+M t0) mod N. The finite
output is always a t in [0,N). A local failure supplies a neutral record;
it never causes a whole-run abort or skips final padding. This closes
the joint branchwise time, space and exact-count theorem in Section 0.

## 11. Exact selected d=4 interface

The declared main program fixes d=4, C_d=7 and n_d=2^256. Its only actual
parameters are the following:

    d=4, n_4=2^256, C_4=7, q0=(2R+1)^4,
    Qroot=7168q0, Wroot=8192*2^R,
    K=2^17n, Proot=7168n^4, Hmax=8192K=2^30n,
    Qtot=7*2^40n^5=7696581394432n^5 exactly,
    epsilon(n)=1/(7*2^33n^4)=1/(60129542144n^4).

The root precision is P_label=Qroot. The finite precision remains the
distinct P_label_old=2^40n^4. The finite branch is n<2^256; the main
branch is n>=2^256. The profile is the constant-gap four-level profile
of Section 3, with v_i=R-(4-i)c. Actual odd stages are at most 513 and
actual 2-adic stages at most 257, for a common bound 770<8192. Thus
all active records fit Hmax and all root acquisitions fit Proot.
The source count is exact, including all padding, and epsilon Q=128n.
Constants in the instantiated theorem are absolute. Its four growth
indices are 1,0,0,0. The family proof's other d values are not executed.

## 12. Inherited source record

The following record comes from the exact depth-two/S371 inputs. Statements
about direct consultation concern their original authors. This task newly
reads the local reproduced texts; it does not claim all original archives
were read. Historical private aliases remain distinct from public copies.

PSG14C corrects PSG14 submission 720fb0a6-7a00-40c8-bb92-3c0649aa5755,
commit 51400781cedeb3fc1cdebdfacb697314a75f5286. The corrected positive K
for M=1 is retained here. PSG13 supplies reset/virtual-transcript and
two-basis finite shadow methods. PSG12 local ce0de50 supplies the
three-level Grover sieve, source-cap design, compact implementation and
all-modulus stride geometry, inherited from PSG9. ROB-G submission
a5c17989-ca3a-49c1-8cea-49d37de89a27, public
1e7300e39bdc1d352dbb895601723712f51d3b62 supplies the exact model text
and shadow/martingale motivation. Its compressed-feature search and
constant 33/100 fraction are not used here.

CYG1 note 70564803-3637-426f-9587-e1333aa07b39 supplies the parity-support
disjoint-pair mass and two-row factorial-moment fiber tail. Its reported
upstream source is CYC1. The inherited record claims no direct CYC1 archive
read. Neither the cyclic instrument nor its seven-moment theorem is used.
The primitive here is exactly the 64-member disjoint-pair instrument.

Historical local sources are PSG7 d772839 for persistent descriptors and
counter/cursor accounting, PSG8 bd374e2 for compact rows and separated
precision, PSG4 for the linear-base Grover/stride setup, PSG3 for collective
label rounds, PSG1 for bounded verified discovery and unused-block induction,
and PSW1/PSW2 for variable widths, weighted cutoff and truncated-base work.
No public archive identity is asserted for these local snapshots.

The inherited public sources are PSR2 submission
16bb6065-c3ca-45fb-b514-86106a310646, archive
7f835a08d1b109847a9b921c02b35361ed350bd0, for signed streaming, extraction,
decoding and substantial adapted proof text; SLS
59facd77-4082-40d9-910e-9060c197e72a, archive
643c22bdf74a96b1e08a0eb56f562396c3084adc, for pairing and space context;
CS1 f1481815-9577-4990-abe3-7b79fa5d9284, archive
200ef0387acb280adcd272f4fbcdb805d1786bbe, for latent labels, transforms,
untouched bits and full-modulus decoders; WTS1
50a9f13c-eda5-4239-a3c8-28ed83e8ce83, archive
9d8256a16cc1f29c7543af470f03ebc37f8bf0b4, for the held-out-block lemma,
stride, restriction B>=a and enlarged grid. WTS1's vector table is not used.

Collective rounds were informed by 844c0fd2-9b1c-4e84-a37c-f402e109985f,
archive 7c4b4ed099799e146213c1e3c43a50151482dc6b. That source credits
the earlier CS1-C3A note 05c80793-e172-437e-837c-4c10dd0c4929; its failed
hosted execution is not a mathematical verdict or archive premise.
CST-128 f95bb4e2-3d08-4ca0-a34f-99841dca855a, archive
6b7500d549149709fb089338c116904f210b23d1, Section 3, supplies affine
ripple layouts, regenerated inverse passes and charged addresses.

The actual local compiler chain is psg14c_compiler_transfer.md,
0524ec65f682efc625237ad074d71430cfdfdf60d6e80cc1ecb6167b82e61224;
grover_stride_compiler.md,
4c5bcd59c95fa2c10be21ab610cdfe76f6b8d2d31300582b97417a7f5b7e896f;
psg13_compiler_transfer.md,
bcc4156e5aba2b6c7ec9e687c204aec97bbf903b16c72bca1c2c3dd71dc4c699;
psg13_verified_compiler.md,
948a1d348359f808d7a5e726262f8bd8adb3315447c1027d6e5706f620cfce4a;
and critical_third_cache_generator_l2.md,
eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3,
for the ready-address/tape-head/marked-loop method. The local budget input
psg14c_record_budget.md has hash
41021054aeed39ebeb552fc13dfce9717245f3c3cedbb9761ee2236c835cdca3.
Literal helpers also descend from psg13_verified_base.md,
d68deac7104659ab598837f07791e16e077018740ff9cec24962bc6335f95ecd.

Historical references are Regev quant-ph/0406151 Section 3,
Kuperberg 1112.3333 Section 4.6, Kitaev quant-ph/9511026, Grover
quant-ph/9605043, and Boyer-Brassard-Hoyer-Tapp quant-ph/9605034v1
Sections 3--4. The required identities, search estimate and charged
implementation are proved above. No acceptance/rejection result,
optimality claim, maximal-fraction claim or invention claim is a premise.
