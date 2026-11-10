# PSG10-F7: a fixed rational streaming-sieve configuration

## 1. Selected joint theorem

For every N>=2 and s in Z/NZ, set n=ceil(log2 N), L=log2 n for n>=2,
F=sqrt(nL), G=sqrt(n)L^(-7/16). Define the fixed rational constants

    q=1/10, c=51/20, f=49/51.

The single algorithm PSG10-F7, specified in Section 2, recovers the entire secret
with unconditional probability at least 1-2^-8>2/3 from independent ideal mixed
coset states. On EVERY execution branch, including failed attempts, incorrect
label extraction, discarded copies and aborts, it has the simultaneous bounds

    T=O(2^(c F+(3/4)G)), S_C=O(n^2), S_Q=O(n),
    Q=O(2^((1/10)F+(3/8)G)).                         (1)

Constants are absolute, independent of N,s and outcomes. n=1 belongs to the
explicit finite algorithm branch and is covered by the same big-O guarantee.
The four growth indices are exactly (1/2,0,0,1/2). Fractional tolerance is 0 in
Section 7's exact clean error model. No cube-root work or optimality is claimed.

## 2. Complete source, algorithm selection and exact parameters

`family-source.md` is the unmodified complete proof/program specification of
PSG4-THIRDBASE-REFINED, submission 53921d7e-f55c-4ca7-b9cd-5b6f1c2d88a0,
published commit 3335bc78b723613b2424a7fb2f693384537fda86. Its SHA-256 is
`da756264b856999eee099efbee811a04f8e6e754df5a243e25d2c8086535f008`.
It is included in full, not invoked as a prior verdict.
The same-round PSG49-F7 specialization proof is also retained byte-identically
as previous-core.md, from submission 567e39fd-a7be-4ed4-9e1c-97ea58b60e8f.
Its capacity and positive-gap proof method is materially used here, with the
new constants recomputed explicitly below. Its former selected q=49/100 is
not this configuration. Neither its verdict nor its selected bounds are
used to substitute for the calculation below. Its Section 11 gives the
general rational family, with its proof and all constituent algorithms in
Sections 1-8. PSG10-F7 is precisely that family at q=1/10 and alpha=7/16.
The source's selected third-base numerical theorem (Sections 0 and 9) describes
another configuration; it is not a claim of this snapshot. The following
selection resolves EVERY occurrence of the base threshold in the program and
its dependent quantities. No other algorithm or configuration is combined in (1).

For n<256 use exactly Section 8's exhaustive candidate tester: at most n+10
fresh copies per t, controlled subtraction of t, X-measurement, reject on the
first minus, output the first passing candidate or 0. Its error is <2^-10.
For n>=256, use Sections 1-8 with the sole profile change

    u(R)=max(1,floor(49 R/51)).

This is Section 11's rational-family rule in place of max(1,floor(R/3)).
Compute delta(v)=min{d>=0:20*2^d>=21*(2v+6)}. For each positive integer R in
ascending order, descend by v <- v-delta(v), retaining values >=u(R), and reverse
the retained values. Choose the FIRST R with twice their sum at least n. This
finite sequential search terminates by ceil(n/2), since the retained profile
contains R itself. No feasibility monotonicity is assumed.

For the chosen R write u=u(R), retained values v_1,...,v_mstar=R, and compute
q0=(2u+6)2^(R-u). For each PS_TREE(D,B), allocate widths greedily from the root
as in Section 4. Positive width b uses b+6 children; zero width returns its child.
Use the exact C4096 verified-pair combiner of Sections 4.1-4.3, including its
separate Grover-query registers, fixed-size list, every trial and retry.

Recompute ALL quantities from this actual u and profile: hmax=1+floor(u/8),
h=min(d-a2,hmax), B=d-h, stride=max(1,h-4), nq=2^(h-1)q0,
K=2^13(ceil(log2 nq)+ceil(log2 n)+30), Sodd and the CRT multipliers of Section 6.
If M=1 skip odd decoding with Sodd=K=0. Otherwise Section 6 determines the
finite grid and its full classical search. Use Section 7's controlled-shift
2-adic recovery with the same tree. Define exactly

    H0=Sodd K+2n,
    Qstar=6(2u+6)2^(R-u)H0+2n, Qcap=1024 Qstar,
    Wstar=3 mstar 2^R H0, Wcap=1024 Wstar.

Enforce BOTH literal counters as in Section 8: abort before acquiring a copy
which exceeds Qcap, or before executing a combiner whose added weight 2^v_i
would exceed Wcap (children are already accounted). Extraction confidence is
h_e=ceil(log2(2^16 Qcap(n+5))), F_e=2^21 h_e; run the fixed collective EXTRACT
of Section 3, with exact translations, Clifford+T gates and constant rational
tables. Discard its position register and keep the phase control.
The root frequency and phase convention, odd decoder and 2-adic output follow
Sections 5-7. No sampled x, source control, inverse preparation, purification,
quantum-addressed table or subset-sum oracle is supplied. Only actual fresh
mixed source copies are acquired. All loops, caps and gate generators are the
source's explicit finite integer algorithms. Neither real F,G nor an asymptotic
threshold is evaluated by the physical controller.

## 3. Applicability of the full correctness proof

Here is why changing u changes none of the required probabilistic hypotheses.
The exact latent-label decomposition in Section 2 of the source identifies an
independent uniform hidden Fourier label for each fresh mixed copy. Section 3's
translation-test instrument reads that label without disturbing the phase coin,
except with probability <=1/(2^14 Qcap) per acquired copy; its coupling loss for
all acquisitions is <=2^-14. These are uniform bounds and use our recomputed cap.

The combiner chooses and projects a verified adjacent pair in the measured
low-residue fiber. It never changes the full signed output label or filters its
high bits. Section 4.3 bounds its average advancing probability by
3963/4096>20/21 for every positive width, independently of the base fraction.
The bounded discovery uses counted arithmetic circuits on separate registers;
its incomplete discovery only reduces acceptance. The original phase register
is untouched until its exact pair projection and affine compression.

Section 5's unused-block induction depends only on those low-residue selection
kernels, disjoint fresh leaves, and a nonzero signed incidence coefficient. It
therefore applies to the new profile. Its high blocks stay uniform, and the
integer root frequency retains the stated characteristic-function bounds and
fair parity. Full-label records are marginalized in that proof, not improperly
conditioned on. The source decoder of Section 6 and shifted parity procedure of
Section 7 consequently recover the entire s, for arbitrary N, with odd error
<=2^-20; there is no factorization promise on the odd part of N.

For each retained interval above the base,
(21/20)r_i <= 2^delta(v_i), so telescoping bounds the expected source cost of
a root by 6(2u+6)2^(R-u). The corresponding expected sum of combiner weights is
<=3 mstar 2^R. The reach-event argument of Section 8 counts failed ancestors
and does not assume that an attempt's cost is independent of its success.
It bounds total uncapped expectations by our Qstar and Wstar. Each cutoff
therefore costs at most 2^-10 in success by Markov. The same reasoning applies
uniformly after earlier decoder outcomes, including wrong ones.

The actual capped law is coupled to the ideal uncapped law until a label error
or cutoff. Their unconditional total failure is at most

    2^-10 + 2^-10 + 2^-14 + 2^-20 < 2^-8.

The finite branch's failure is <2^-10. This proves the probability in (1),
without postselection and on all moduli. The bounds on every branch below
also cover executions after a wrong extracted label; finite caps remain literal.

## 4. Capacity certificate for these fixed rationals

Exact identities, verified by integer arithmetic, are

    c=q/2+1/(4q), f=(1-2q^2)/(1+2q^2),
    c(1-f)=1/10, (1-f^2)c^2=1/2.                 (2)

For sufficiently large R, u=floor(fR)<=fR and the retained decrement intervals
cover [u,R]. With D_R=max delta(v)<=log2 R+4, integration (the decreasing-step
profile argument in source Sections 9 and 11) gives

    2 S_u(R) >= (R^2-u^2)/D_R >= (1-f^2)R^2/D_R. (3)

Let Rtest=ceil(cF+G/2). Eventually Rtest<=4F since c=51/20<4 and
G/F=L^(-15/16) tends to 0; rounding adds at most 1/F to the ratio. Thus
D_Rtest<=L/2+(log2 L)/2+6. Expanding its numerator with (2) gives

    (1-f^2) Rtest^2 >= nL/2 + (10/51)n L^(1/16).     (4)

An explicit certificate for the comparison of (4) to nD_Rtest starts at
L0=2^160. There L0^(1/16)=1024, and

    (10/51)*1024 - 80 - 6 = 5854/51 > 0.

For H(L)=(10/51)L^(1/16)-(log2 L)/2-6,

    L H'(L)=(10/(16*51))L^(1/16)-1/(2 ln2)>0

for L>=L0, using ln2>1/2 and L^(1/16)>=1024. Hence H stays positive.
The eventual inequality Rtest<=4F follows from its displayed ratio and
rounding; taking the maximum of its fixed threshold and L0 suffices. No
special algorithm branch or preloaded table uses this analytical threshold.
Thus Rtest is eventually feasible, and the literal first-feasible search obeys

    R <= cF+G/2+1.                                  (5)

Also n<=2S_u(R)<=2R^2, so R>=sqrt(n/2). Since f>1/3,
u(R)>=max(1,floor(R/3)); in particular u>=R/8 on the main branch. For large R,
u>=fR/2 and all retained heights are Theta(R) up to constants. Decrements are
Theta(log R), whence mstar=O(R/log R)=O(R/L). The fixed positive f gives
hmax=Theta(R). Source Section 6's stage count is therefore O(1+n/R), K=O(R),
and H0=O(n). All constants here depend only on the displayed absolute rationals.

## 5. Every-branch resources and positive absorption gaps

The exact branchwise ledger of source Sections 4.2, 8-9 now yields

    Q <= Qcap = O(n(2u+6)2^(R-u)),
    T = O(n^(5/2)L^(5/2)2^R),
    S_C=O(n^2), S_Q=O(n).                            (6)

For clarity its applicability is checked explicitly. Each complete combiner
costs O(R^2 L2^v_i) core operations; the used inequality n<=128v_i^2 remains
valid because u>=R/8. Wcap=O(nR2^R/L), so all combiner core work is
O(nR^3 2^R)=O(n^(5/2)L^(3/2)2^R). Collective extraction costs O(n^2 L)
core operations per raw copy. Its total is a polynomial times 2^(R-u), below
that combiner envelope since u=Omega(R). The decoder's full grid, not a free
oracle, costs at most polynomial(n)2^(R-7u/8), also below it. Preprocessing,
cleanup, both counters, gate generation and initialization remain charged.
Classical indexed access and classically addressed gates pay their separate
O(L) fee because allocated bits plus qubits are O(n^2). Adding source charge
(n+1)Q proves the T ledger in (6). All after-abort work is bounded by those
same fixed allocation and instruction limits.

Depth-first storage retains at most B+5m_active+1<=6n+1 phase qubits, plus
O(n) extraction/arithmetic/query scratch, hence O(n) qubits. O(n)-bit signed
labels for O(n) live coins occupy O(n^2) classical bits. Frames, bounded lists,
profile, budgets, fixed-size tables and decoder frequencies all fit O(n^2).
EXTRACT's precision is O(R+log n)=O(n) bits because Qcap is the recomputed
finite budget above. Nothing stores a circuit of exponential size.

Now (5) gives R<=cF+G/2+1. The gap between (3/4)G and G/2 is G/4.
Since G/log2 n=sqrt(n)/(log2 n)^(23/16) tends to infinity, G/4 absorbs every
fixed polynomial factor in T's ledger. Thus T=O(2^(cF+(3/4)G)).
For copies, u>=fR-1 eventually, so

    R-u <= (1-f)R+1
         <= (1/10)F + (1/51)G + O(1).

The exact positive gap is

    3/8-1/51=145/408>0.

It absorbs the source prefactor in (6), proving
Q=O(2^((1/10)F+(3/8)G)). This retains the positive lower-order terms rather
than replacing them by an unsupported hidden exponent constant. Every smaller
n is a finite prefix with bounded resource maxima and positive envelopes;
its inclusion enlarges only the absolute multiplicative constants in (1).

## 6. Growth indices, comparison and scope

The selected structured time has exponent terms (c,1/2,1/2) and
(3/4,1/2,-7/16); samples have (1/10,1/2,1/2) and (3/8,1/2,-7/16).
There are no outside polynomial or logarithmic factors after the proved
positive-gap absorption. F dominates G, so for both exponential envelopes
log2 log2 B = (1/2)log2 n+(1/2)log2 log2 n+O(1). Dividing by log2 n proves
index 1/2. For n^2 and n the index is zero directly from its definition.

Compared with the source's selected q=1/2 program, the new work coefficient
51/20 is larger and the sample coefficient 1/10 is smaller. Compared with the
published q=1/3 family reference, samples have coefficient 1/10 instead of
1/3, and work has coefficient 51/20 instead of 11/12. These are distinct
tradeoff vectors with identical polynomial spaces; neither dominates the
other. The decrease in the sample coefficient is 70 percent for this
polynomial-memory reference comparison. It is not a 70 percent finite-size
sample measurement, nor a claim that we have the globally smallest samples:
other slower algorithms use O(n) copies. The retained lower-order power is
-7/16, with both correction coefficients included in the declarations.
This is a specialization of the existing rational family, not a new DCP
index, practical speed claim, optimality theorem or claim of literature novelty.

## 7. Exact fifth-claim model and fraction

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The fraction expression is exactly 0. Under this promise each acquired copy
is a fresh independent rho_s of the challenge, including copies discarded or
acquired in failed attempts. Sections 2-5 establish success and all resources
jointly for this same configuration. No positive tolerance is asserted.
