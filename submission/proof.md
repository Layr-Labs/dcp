# PPC: critical-width partial-pivot collimation

The local, source and decoder arguments inherited from the unpublished PPSA
proof are reproduced below. Exact material sources and both-endpoint line
citations are recorded in sources.md; no prior verdict is a proof premise.

## 0. Joint theorem and scope

For every integer N>=2 and fixed secret s in Z/NZ, put n=ceil(log2 N),
L=log2 n. The single algorithm PPC is specified in Sections 1-7, including
its sequential integer profile search, square-root base, finite branch,
precision and two literal caps. From independent ideal DCP copies it returns
the entire secret with probability at least 1-2^-8>2/3. On EVERY branch,
including unsuccessful attempts, wrong labels and aborts, jointly

    T = O(n^(11/4) L^(13/4) 2^((177/250)sqrt(nL))),
    S_C = O(n^2) bits,                   S_Q = O(n) qubits,
    Q = O(n^(7/4) L^(3/4) 2^((177/250)sqrt(nL)-(59/100)(nL)^(1/4))).     (T)

These representatives are positive for n>=2. Every 1<=n<256 uses the
specified exhaustive branch, including n=1 where L=0.
Constants are independent of N,s and all outcomes. Exact growth indices are
[1/2,0,0,1/2]. The fifth claim is fraction 0 in the clean-copy model of
Section 10. No positive tolerance or index below 1/2 is claimed.

For n>=256 the actual maximum block width B is chosen anew using

    q(b)=b+ceil(log2(b+1))+4,
    d(b)=ceil(log2((q(b)+2)^2)),       U(B)=ceil(sqrt(B)).       (0.1)

Starting at trial B, descend by b<-b-d(b), retaining b>=U(B), and choose
least B with retained sum >=n. This changes the executed arities, depth and
child population. It is not merely a smaller displayed exponent coefficient
for the previous algorithm. Odd block widths are allowed.

For the n>=256 branch, the more informative exact-profile bounds are

    T = O(n B^(7/2) log2(B+2)^(-1/2) log2(n+2)^2 2^(B/2)),
    Qcap = O(n B^(3/2) 2^((B-U)/2)),                             (P)

with the exact rational caps of Section 7. For 1<=n<256, the exhaustive
branch uses at most N(n+10) source copies. Uniform all-D certificates are
proved, including a partial bottom width and arbitrarily many inactive levels.
The all-N decoder uses only its already proved one-bit frequency law.

There are three separate conclusions. The inherited pivot mechanism reduces
local mean search by a polynomial factor. The critical profile gives a genuine
stretched-exponential saving in ideal-root mean charged work against the
inherited profile at the SAME quarter base, even after paying for every level.
Changing the base to sqrt(B) then gives a leading time/sample tradeoff.
The literal source cap's leading coefficient rises from sqrt(3/10) for the
quarter-base family to 1/sqrt(2) for PPC. Section 9 proves these statements
without extrapolating the finite screen. There is no claim of a free joint
improvement over PPSA or PSG11, nor of a new literature-wide frontier.

## 1. Implementation conventions and exact source supply

An elementary reversible arithmetic operation means NOT, CNOT or Toffoli,
with Toffoli expanded into its fixed exact Clifford+T implementation.
Ripple addition/comparison on w bits takes O(w) such gates and O(w) scratch.
Compute/copy/uncompute gives clean predicates; compute/swap/inverse implements
a permutation, including a permutation controlled by another register.
Known constants are explicit classical bit strings. Registers, gate generation,
resets, fair random bits and addresses are paid. No QRAM or arithmetic oracle
is supplied. Gate descriptors are streamed, using binary counters. A
conservative O(ell^2) charged allowance per elementary operation includes
field construction and the full ell-bit address debit, where
ell=ceil(log2(S_C+S_Q+2)). There is no exponential stored circuit.

The following exact source construction is reproduced from CYG1 Sections
2-3. Its Qcap is the literal acquisition cap in Section 7 here. All later
selection ignores EXTRACT's internal outcomes, except its final label.

### 1.1 Source identities and exact transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into
rho_s = (1/N) sum_x |psi_x><psi_x|, with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,       (S1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (S1) each copy is literally a convex mixture, with
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
secret s'. The latent-label model is then applied to rho_s' via (S1), so the
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

For either transform, compute the flag [u<N], control the complete
permutation on that flag, then recompute membership on the output to
clear it. Membership is invariant under each permutation, so this gives
the claimed identity extension and clean scratch. The two comparisons
add O(n) gates and O(n) scratch.

Modular addition of a known constant in [0,N) is a ripple comparison with N,
an addition, a comparison and a selector. It is the identity on encodings
>= N, uses O(n) Boolean gates, and is computed cleanly: compute, swap or XOR
the result out, then uncompute.

### 1.2 Finite-precision classical table and source-label extraction

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20
of cos(2 pi v/4096) and sin(2 pi v/4096).

- Bound pi within 2^-90 using Machin's formula pi = 16 atan(1/5) - 4 atan(1/239),
  summing the first 40 terms of each alternating arctangent series. This gives
  two-sided bounds; the tails are below 16 (1/5)^81/81 + 4 (1/239)^81/81 < 2^-91.
- The identity follows from tan(2 atan(1/5)) = 5/12, tan(4 atan(1/5)) = 120/119
  and tangent subtraction.
- At the angle 2 v p_mid/4096 < 7, where p_mid is the midpoint of the pi bounds,
  evaluate the degree-80 Taylor polynomials. Their remainders are <= 7^81/81! < 2^-170. The angle error
  is < 2^-89, and sin and cos are 1-Lipschitz.
- Round each value to the nearest multiple of 2^-20.

This is a fixed finite rational computation, charged once as an absolute
constant (not advice).

For x in [0,1) put tab_0(x) = Cos[floor(4096x)] and tab_1(x) = Sin[floor(4096x)],
and let cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                    (S2)


EXTRACT uses Qcap fixed in Section 7. Put J_e=n+4,

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

### 1.3 Level-wise extraction RUN(F)

For each j = 0..J_e take F tests at level j per basis, giving empirical means
x_j and y_j. Then decode as follows.

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
RUN(F(h)) uses 2 (J_e + 1) F(h) tests, that is O(n^2 h) core steps.


Since e^-h <= 2^-h, the per-call probability of an incorrect label is at most
4(n+5)2^-h <= 1/(2^14 Qcap). The union bound for at most Qcap adaptive calls is
2^-14, including discarded copies. Couple to an ideal run which outputs the
true latent label on every call, ignoring EXTRACT's internal test outcomes.
No later choice uses those internal outcomes. This coupling preserves the
untouched-bit argument; one does not condition it on extraction succeeding.
Each call takes O(n^2 h+n^2) core operations, O(n) qubits and O(n^2) classical
bits. For unwrapping store the n+5 six-bit directions; handle one empirical
mean at a time with binary counters. All loops have their stated fixed bounds.


## 2. The local recovered instrument

At a positive level, the input qubits have full signed labels A_j divisible
by 2^p and phases exp(i theta A_j). For b new cancellation bits set
c_j=(A_j/2^p) mod 2^b, compute f(X)=sum c_j X_j mod 2^b and measure e.
The retained register is the uniform-magnitude phase state on F=f^-1(e).
Its Born weight is |F|/2^q. In the following local proof a_j denotes c_j
when used in modular arithmetic, and A(x)=sum A_j x_j denotes the full
signed label. The output is labelled A(v)-A(u), never a reduced residue.


### 2.1 Preparing the query on a coarse fiber

Let q known labels a_j in Z/(2^b) be given. Define f(x)=sum_j a_j x_j mod 2^b.
The retained unknown input has support F={x:f(x)=e}, of size m>=1. For a clean
input its amplitudes are exp(i theta A(x))/sqrt(m), where A uses the full
signed labels and theta is unknown. No preparation or inverse preparation of
this input is available.

Suppose there is a distinct pivot p_i of valuation i for each 0<=i<t<=b.
Choose the first such index in input order. Put r=e mod 2^t and let the other
q-t positions be free bits w. In a t-bit accumulator compute

    z = r - sum_(j free) a_j w_j mod 2^t.

For i=0,...,t-1, copy accumulator bit i to the initially zero pivot bit p_i
and subtract a_(p_i) controlled by that pivot bit. Lower accumulator bits
stay zero at every step; the final accumulator is zero. The lowest differing
pivot proves that exactly one pivot assignment completes each w. Therefore

    S={y:f(y)=r mod 2^t},   |S|=2^(q-t),   F subset S.

Every operation described is a reversible controlled addition or CNOT on the
whole ambient space. Reversing their order and signs gives the inverse.
Hadamards on the free bits followed by this computation prepare
|S>=|S|^(-1/2) sum_(y in S)|y>. Denote this known unitary by U. Scratch is
zero at its end. Reflection about |S> is U(2|0><0|-I)U^-1, including the
scratch registers in the zero reflection. This is reflection about a newly
prepared query, with no reflection about the unknown retained phase state.

Pivot discovery costs O(qb) classical bit operations. Reversible preparation
and its inverse cost O(qt+q) elementary exact gates and O(q+t) qubits. A
controlled constant addition on t bits uses a ripple carry/borrow circuit
with O(t) NOT/CNOT/Toffoli gates and clean scratch. The zero reflection uses
an O(q+t) Toffoli ladder. Thus the statement does not assume a rank oracle,
QRAM, or a supplied subset-sum table. No extra source copies are acquired.

### 2.2 The recovered search remains exact

Write A'=|S|. Given retained X in F, mark a query Y iff Y in F and Y!=X.
There are m-1 marked elements for every basis value of X. Starting at |S>,
after j Grover iterations the query has amplitude g_j/sqrt(A') on each
marked element and h_j/sqrt(A') on each unmarked element, where g_j,h_j
are independent of X. This follows either from the two-dimensional rotation
or the exact recurrence, with z=m-1,

    g_0=h_0=1,
    g_(j+1)=(1-2z/A')g_j + 2(1-z/A')h_j,
    h_(j+1)=-2z/A' g_j + (1-2z/A')h_j.

Verify the marked flag. On success, coherently sort X,Y, measure the unordered
pair, and retain its orientation bit. For endpoints u<v the Kraus map is
(g_j/sqrt(A'))(|0><u|+|1><v|). On the promised phase input it gives the balanced
qubit with phase difference theta(A(v)-A(u)). Compute that full signed
difference, including all carry bits. Measuring only low differences would
not suffice.

On failure, measure membership Y in F. If true, failed marking implies Y=X;
CNOT X into Y clears Y without measuring X. If false, Y lies in the same set
S\F for every X. Its query vector factors from X and may be measured/reset.
Every failure Kraus operator on the retained F register is a scalar times
I_F. This remains true with an arbitrary reference system. Thus repeated
trials use the same children and exact failure recovery, not an independence
assumption about a disturbed batch. All flags and arithmetic scratch clear.

Selection of pivots uses only low b bits. The query preparation, marked
oracle, trial schedule and measured pair depend only on those bits and fresh
randomness. The untouched-label induction in Section 4 below applies without exposing
any high bit. Section 1 and the outer decoder supply its leaf interface.

### 2.3 Two early trials at each scale suffice

Let z=m-1. At dyadic scale J choose j uniformly in {0,...,J-1}. For
0<z<A', put sin^2(gamma)=z/A'. The success probability is exactly

    p_J=1/2-sin(4J gamma)/(4J sin(2 gamma)).

Use two recovered trials at each scale 1,2,...,J_max/2, and R trials at
J_max=2^ceil(log2(A')/2). Count H=sum(j+1), including final verification.
Every branch has H<(R+2)J_max. If z>0 the terminal scale has p_J>1/4, so
failure is at most (3/4)^R. If z=0 the entire cap is exhausted.

For sparse fibers z<A'/2, let J_* be the first dyadic scale at least
2/sin(2 gamma), if it occurs before or at J_max. Then
J_*<=2sqrt(2A'/z), and all later scales have p_J>=3/8. The probability of
reaching d further scales is at most r^d, with r=(5/8)^2=25/64 and 2r<1.
The cost before J_* is below 2J_*. The later nonterminal cost is at most
2J_*/(1-2r). The terminal contribution is at most (8/3)J_*; these bounds
may harmlessly overlap. Hence

    E H <= [2+2/(1-25/32)+8/3]J_* < 40sqrt(A'/z).

If the first qualifying scale exceeds J_max, all early trials cost below
2J_max and terminal expected cost is at most 4J_max. Since
J_max<2/sin(2 gamma)<=sqrt(2A'/z), the same bound follows.

Dense fibers need their own bound. Put eta=pi/2-gamma in (0,pi/4]. Now
p_J=1/2+sin(4J eta)/(4J sin(2eta)). For J=1 it is at least 1/2. If its
correction is negative, J>=2 and eta>pi/(4J). Monotonicity of sine on
[0,pi/2] and its chord on [0,pi/4] give

    4J sin(2eta) >= 4J sin(pi/(2J)) >= 4sqrt(2).

Thus p_J>1/2-1/(4sqrt(2))>5/16. Two-trial scale failure is at most
r=(11/16)^2, with 2r=121/128<1. Summing scales and bounding the terminal
expected trials gives

    E H <= 2/(1-121/128)+16/5 <40 <=40sqrt(A'/z).

These estimates do not require independence between trial work and success.
Fresh j is independent of reaching its trial; exact recovery supplies the
same success law conditional on all prior failures.

### 2.4 A proved local asymptotic saving, including rare missing pivots

For b>=1 set

    q=b+ceil(log2(b+1))+4,
    R=8ceil(log2(b+1))+4,
    u=ceil(log2(q+2)).

Let t_* be the largest integer t>=0 such that 16u*2^t<=q, or zero if
none exists. It is always at most b. Use t=t_* if all its pivots exist,
and t=0 otherwise. This rule is chosen for proof, not claimed to be the
finite optimal cap found by the GPU. In particular,

    2^(-t_*/2) <= sqrt(32u/q).

Suppose the q low labels are independent uniform modulo 2^b and the full
fiber is measured with its true Born weight m/2^q. A valuation-i pivot
occurs with probability 2^(-i-1) per label. If t_*>0, union bound gives

    delta=Pr(a pivot is missing)
          <=t_* exp(-q/2^t_*) <=u exp(-16u) <=u(q+2)^(-16).

When t_*=0 the missing-pivot event is empty. This bound is unconditional
over the labels; pivot availability and full fiber size are NOT independent.

For completeness, the unconditioned planted variable Z=m-1 has
lambda=E Z=(2^q-1)/2^b and Var Z=lambda(1-2^-b). Plant a uniform X and
write the other strings as X xor z; sign changes preserve uniform labels.
Every nonzero binary z has uniform subset sum, and any two distinct such
rows have a determinant +/-1 minor, proving pairwise independence. Thus
Pr(Z=0)<=1/(1+lambda) by Cauchy-Schwarz and
Pr(Z<lambda/2)<=4/lambda by Chebyshev.

Write A=2^q and define the pointwise allowance

    B(Z)=40sqrt(A/Z)                       if Z>0,
         (R+2)sqrt(2A)                    if Z=0.

The moment split just proved gives

    E B <=40sqrt(2A/lambda)+160sqrt(A)/lambda
                                  +(R+2)sqrt(2A)/(1+lambda)
         <=256*2^ceil(b/2).

Indeed lambda>=15(b+1); the first two terms are bounded by 80sqrt(2^b)
and 80sqrt(2^b)/sqrt(b+1). With a=ceil(log2(b+1)), the third is at most
4sqrt(2)(a+1)sqrt(2^b)/sqrt(b+1). Use (a+1)/sqrt(b+1)<=3. Their sum is
less than 256sqrt(2^b). This also charges singleton exhaustion.

On the pivot event the pointwise bound scales by 2^(-t_*/2). On its
complement use the original deterministic cap. Without conditioning the
fiber moments on pivot success, this proves

    E H_pre <= 256*2^ceil(b/2)*2^(-t_*/2)
                    +(R+2)*2^ceil(q/2)*u(q+2)^(-16)
            = O(2^(b/2) sqrt(log2(b+2)/b)).

The attempt still succeeds with probability at least
1-1/(1+lambda)-(3/4)^R >=1-1/[2(b+1)]. The query support contains every
original full-fiber member, so preparation loses no retained input mass.

This is an improved local upper bound, not a matching lower bound or a
pointwise dominance assertion over the unconditioned algorithm.


## 3. Literal finite local budgets and implementation

For an actual width b>=1 define, using integer bit lengths only,

    c=ceil(log2(b+1)), q=b+c+4, r=8c+4, u_b=ceil(log2(q+2)),
    t_b=max({t>=0:16 u_b 2^t<=q} union {0}),
    sigma_b=1-1/[2(b+1)].

Test for all t_b pivot valuations; use them all if present, otherwise use
no pivots. The local terminal scale is 2^ceil((q-t)/2). There are exactly
two trials at each earlier dyadic scale and r trials at the terminal one,
stopping on success. This defines every small width without enumeration
or an asymptotic exception. A singleton exhausts its cap and is discarded.

Here is a RATIONAL expected-H certificate, including missing pivots:

    h_b=256*2^(ceil(b/2)-floor(t_b/2))
        + I[t_b>0]*(r+2)*2^ceil(q/2)*u_b/(q+2)^16.             (3.1)

Section 2 proves EH<=h_b and success probability >=sigma_b>=3/4. Replacing t_b/2 by floor(t_b/2) in Section 2.4's bound costs at most
sqrt(2); relative to 2^((b-t_b)/2), both roundings together cost at most 2. In particular

    h_b=O(2^(b/2)*sqrt(log2(b+2)/(b+1)))                       (3.2)

uniformly for b>=1. For the rare term, divide by the displayed expression:
2^ceil(q/2)<=8*sqrt((b+1)2^b), r=O(log(b+2)), u_b=O(log(b+2)),
and q>=b. The resulting ratio is O((log(b+2))^(3/2)/(b+1)^15),
which is bounded and tends to zero. The main term follows from
2^-t_b<=32u_b/q. No conditional fiber-moment estimate is used.

Set the deterministic bookkeeping word allowance w=64(n+1). Section 8
bounds full labels, search counters and both global counters by w bits.
For a width-b attempt define two ticket weights

    s_b=q*(w+b+1)+w,       z_b=q*(b+1)+w.                     (3.3)

Before initial residue measurement, debit 2s_b work tickets or abort.
This reserves both setup and final output/disposal. Before preparing each
trial debit z_b, then before EACH Grover iteration debit z_b. The first
debit covers preparation, choosing j, verification, recovery and reset.
A trial costs j+1 such debits, so the charged total is exactly
2s_b+z_b H. A started ticket's finite macro finishes before the next debit.
One global integer counter counts their weighted sum, not the worst-case
cost of a complete trial, scale or attempt. Counter comparison/addition is
included in the w summands. Aborting inside a search discards the live
state; no favorable conditioned-state claim is made on that branch.

The low predicate computes sum c_j Y_j, compares to e and compares Y to
quantum X, then uncomputes everything. It takes O(qb+q) exact gates.
The prepared-query reflection costs O(qt+q+b). Flags are uncomputed;
on a failed equality branch CNOTs clear Y=X, and on an outside branch
Y factors and is measured/reset. Sorting X,Y reversibly retains an
orientation bit and the two ordered endpoints. Measuring the ordered pair
leaves the exact phase qubit; a reversible map from (X,Y) to (u,v,bit)
has an explicit inverse by swapping iff bit=1. Endpoints and residue records
are then classical. Computing A(v)-A(u) costs O(qw), including carries.
These costs fit (3.3) with one universal constant times ell^2. Fair bits
choose uniform j below a power of two with no rejection overhead.

The deterministic local cap is H<(r+2)2^ceil(q/2), even on wrong labels.
It is only used for termination and word length. Expected local ticket
cost has certificate

    a_b=2s_b+z_b*h_b.                                        (3.4)

Source/child work is excluded here and included in the global recurrences.

## 4. Fresh blocks, phase correctness and termination

An ideal leaf has known label uniform on [0,2^D), phase exp(i theta label),
and is independent of other fresh calls. Fix any deterministic nonnegative
width sequence with total at most D-1. At each node build q(b) fresh child
outputs. If its bounded attempt fails, discard all children and restart.
Distinct child calls use disjoint fresh source streams. Zero-width levels
return their child without an attempt.

We prove termination, the exact phase and uniformity of the WHOLE untouched
quotient together by induction. Leaves satisfy all three assertions. Assuming
them below a node, the q next-block residues are iid uniform. Section 2
therefore gives unconditional fresh-attempt success >=sigma_b>0, given the
external history before building the children. Its child costs have finite
means by induction and its local cost is bounded. Fresh restarts imply
almost-sure geometric termination and finite means. This reasoning requires
no independence between one attempt's cost and its success.

Fix any finite successful low transcript, including preceding failures,
child selections, low leaf values modulo 2^(p+b), pivot choices, search coins,
residues, recovery records and unordered edges. Probabilities of these records
depend only on those low values. On a flat phase fiber every edge's probability
is the sum of its two diagonal input weights; its phase causes no interference
between the orthogonal orientations. Failed records have the scalar-identity
maps from Section 2. The selected full output is a signed sum of successful
leaves with coefficients in {-1,0,1} and at least one nonzero coefficient.
This follows inductively because u!=v selects a nonzero child coefficient,
and disjoint child leaf sets prevent its cancellation by another child.

More formally, a flat q-qubit input with arbitrary phases yields residue e
with probability m/2^q, where m=|f^{-1}(e)|. Conditional on e and j, an edge
has probability 2|g_j|^2/(m A'), while each diagonal or specified outside
failure record has probability |h_j|^2/A'. These depend only on low labels.
Thus a finite selection transcript tau has kernel P(tau|low,high)=k_tau(low).
Bayes gives P(high|low,tau)=P(high|low) for every positive-probability
transcript, including failed attempts. Unused extraction outcomes and future
budget survival are not in this conditioning.

Write each such original leaf as low_l+2^(p+b) H_l. Conditional on the low
transcript the H_l remain independent uniform modulo 2^(D-p-b). The parent
quotient equals carry+sum_l z_l H_l modulo that whole group. One z_l is +/-1;
conditioning on all other H_l proves uniformity. Averaging over the countable
finite terminating transcripts proves the unconditional law. Disjoint fresh
streams give independence across subsequent calls. Full-label storage does
not make those unused values selection inputs. Neither future budget survival
nor accurate numerical extraction is included in this conditioning.

For a root cancelling D-1 bits, its full signed quotient W satisfies, given
the low transcript,

    W=carry+sum_l z_l tau_l,      tau_l iid fair bits,
    |E exp(2 pi i y W)| <= |cos(pi y)|,     Pr(W odd)=1/2.       (4.1)

The product of characteristic factors proves the inequality. This does not
say W is uniform as a signed integer. The full signed label is 2^(D-1)W.
No phase tensorization of the free pivot bits is used anywhere.

## 5. Fixed critical profile and exact all-D recurrences

For n>=256, and each trial integer B=1,2,...,n, put

    U=ceil(sqrt(B)),  d(v)=ceil(log2((q(v)+2)^2)).

Both are integer computations: U=isqrt(B-1)+1; ceil(log2 x) is the bit
length of x-1. Start at v=B, retain it, and replace v by v-d(v), stopping
before a value below U would be retained. Reverse the result to
v_1<...<v_m=B. Choose the LEAST B for which C(B)=sum_i v_i>=n.
Search sequentially. No binary search or capacity monotonicity is assumed.
The search terminates by B=n since the top value alone supplies n bits.
Always C(B)<=B^2, so B>=sqrt(n). This finite rule is the actual algorithm,
including below any large analytic threshold used later.

For TREE_D, 1<=D<=n, allocate D-1 cancellation bits greedily from the root
down: b_i=min(v_i,remaining), then subtract b_i from remaining. There is at
most one partial positive width; all positive ancestors above it are full.
Skip leading zero levels. At every positive width use EXACTLY Sections 2-3.
Return full signed labels. Define the nominal successful-leaf bound

    q0=product_i q(v_i),          k0=ceil(log2 q0).

A successful tree uses at most q0 successful leaves, even if its discarded
attempts used more. The absolute value of any intermediate full label is
less than q0*2^D, and the final signed quotient satisfies |W|<2q0. These
bounds also hold after incorrect numerical labels, since each supplier
returns a D-bit encoding. A failed or discarded leaf is never added to a
later successful full label.

For EACH D=1,...,n compute exact rational certificates starting e=1,v=0,
processing actual widths bottom up. For b_i=0 do nothing; otherwise put

    e <- q(b_i)*e/sigma_(b_i),
    v <- [q(b_i)*v+a_(b_i)]/sigma_(b_i).                      (5.1)

Retain Emax=max_D e_D and Vmax=max_D v_D. This is a literal maximum over
all D, including e_1=1,v_1=0. Do not replace Vmax by v_n: t_b and h_b have
ceiling discontinuities. Only one D's working recurrence is stored at once.

If p_i is true fresh-attempt success probability, ideal expectations obey

    E_i=q_i E_(i-1)/p_i,
    V_i=[q_i V_(i-1)+E(local tickets)]/p_i.                  (5.2)

First-attempt unconditional cost plus (1-p_i) times an independent fresh
future proves this renewal identity. A child's cost may correlate with its
label; the attempt's cost may correlate with success. Neither correlation
invalidates (5.2). Section 4 supplies the fresh iid uniform low labels and
p_i>=sigma_(b_i), and Section 3 supplies E(local tickets)<=a_(b_i).
Therefore (5.1) upper-bounds the uncapped ideal means, not realized branches.

For a separately specified comparison configuration PPC-Q, replace U(B)
by max(2,floor(B/4)), and start trial B at 2. All other instructions,
recurrences and caps are identical. PPC in claims (T) always uses sqrt(B).
PPC-Q is an auxiliary complete configuration, never combined with PPC's
sample bound to make a mixed claim. Sections 8-9 state its own joint bounds.

## 6. Full-secret recovery for non-power-of-two and power-of-two N

Compute a2=v_2(N), the number of trailing zero bits of N, and write
N=2^a2 M with M odd. Put d=floor(log2 N), so 2^d<=N<2^(d+1).
The target s1 is the representative of s mod M in [0,M), with s1=0
when M=1. The algorithm's estimated s1 has the same range on every
branch. The symbol s2 denotes (s-s1)/M modulo 2^a2 only when that
odd-part estimate is correct; operational bit recovery uses only the
estimated s1, the accumulated bit string s2low and the shifts below.

The following decoder is reproduced from CYG1 Sections 6-7 with TREE_D,
q0 and the new source precision cap substituted. Only the law (4.1), the
full frequency bound |W|<2q0 and the leaf interface are required. In particular
it does not use the old classical-list combiner or its survival constants.

### 6.1 Odd-part recovery by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so N >= 3 * 2^a2
and d - 1 >= a2. Put theta = s1/M in [0,1). Every stage uses D = d,
nq = q0 and

    K = 2^13 (ceil(log2 nq) + ceil(log2 n) + 30).

The stages are j = 0, 1, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. By
minimality, J + 1 <= log2 M <= n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^j (2^(d-1-a2))^(-1) (mod M). Then alpha_j is a
unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run EXTRACT to obtain k, and accept iff k < 2^d (otherwise discard the copy and
  acquire again);
- on acceptance, apply X to the control.

In the ideal run, accepted labels are i.i.d. uniform on [0, 2^d), each copy is
accepted with probability 2^d/N > 1/2, and the qubit is pq_k(alpha_j s), i.e. it
has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(d-1) W th = W 2^(d-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),            (D1)

because 2^(d-1-a2) alpha_j = 2^j (mod M) and s = s1 (mod M). So a TREE_d root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^j W.

Measurement. For i = 1..K:
- run TREE_d;
- obtain a fair bit beta_i by measuring H|0>;
- measure the root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in {+1,-1}
  together with W_i and beta_i.

Ideally E[Z_i | f_i, beta_i] = cs_(beta_i)(f_i theta) with f_i = 2^j W_i.

Candidates. Put P_j = j + ceil(log2 nq) + 8, and identify an integer c with the
point zeta = c/2^(P_j) on the circle R/Z.
- Stage 0 uses every c in [0, 2^(P_0)).
- Stage j >= 1 uses every c whose point lies within circular distance
  rad_j = 2^-(j+2) of the previous center z_(j-1). This is one or two explicit
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
1 - 2^-20/n, theta is within circular distance 2^-(j+3) of z_j.

Proof. Let Fs_i be the sigma-field of everything up to and including root i
of the stage, and Gt_i the sigma-field of Section 4 for tree i. For a
candidate point zeta, let Delta = theta - zeta, taken as a circular
difference, and let xi_i = Z_i cs_(beta_i)(f_i zeta). Conditional on
Fs_(i-1), Gt_i and the top bits of tree i (hence on W_i), averaging over the
fair basis bit gives

    E[xi_i | ...] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(..) sin(..)]
                  = (1/2) cos(2 pi f_i Delta).

By (S2), the computed score differs from sum_i xi_i by at most K/625.

Near point. Let zeta0 be the candidate nearest theta. In stage 0 the
candidates cover the circle. In stage j >= 1 the candidate arc contains theta
and has candidate endpoints. Either way |Delta0| <= 2^-(P_j + 1). Since
|f_i| < 2^j 2 nq,

    |f_i Delta0| < 2^(j+1) nq 2^-(P_j + 1) <= 2^-8.

So E[xi_i | Fs_(i-1)] >= (1/2) cos(pi/128) for every realization.

Far points. Call zeta far if |Delta| >= 2^-(j+3). In stage 0 we always have
|Delta| <= 1/2. In stage j >= 1, both theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j+1). Hence xx = 2^j |Delta| lies in [1/8, 1/2] for
every far zeta. Tree i uses copies independent of Fs_(i-1). By Section 4, its
top bits are fair and independent given Fs_(i-1) and Gt_i. So by (4.1) with
phi = 2^j Delta, and since a real part is at most the modulus,

    E[xi_i | Fs_(i-1)] = E[ (1/2) Re E[exp(2 pi i 2^j Delta W_i) | Fs_(i-1), Gt_i] | Fs_(i-1) ]
                       <= (1/2) cos(pi xx) <= (1/2) cos(pi/8).

Concentration. For each fixed candidate, sum_i (xi_i - E[xi_i | Fs_(i-1)]) is a
martingale whose increments lie in intervals of length 2. By Azuma-Hoeffding
it deviates by at least K/64 with probability at most
exp(-(K/64)^2/(2K)) = exp(-K/8192). Outside these events for zeta0 and every far
candidate,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625
                 >  (K/2) cos(pi/8)   + K/64 + K/625 >= score(far zeta),

because cos(pi/128)>511/512 and cos(pi/8)<37/40, and
(1/2)(511/512-37/40)>2/64+2/625. The first bound follows from
cos x>=1-x^2/2 and pi<22/7; the second from
cos(pi/8)=sqrt(2+sqrt2)/2, sqrt2<99/70 and (2+99/70)/4<(37/40)^2.
So the
maximizer is not far. There are at most 2^(ceil(log2 nq)+9) events, and since
e^-x <= 2^-x, exp(-K/8192) <= 2^-(ceil(log2 nq) + ceil(log2 n) + 30). The failure
probability is therefore at most 2^(9-30)/n <= 2^-20/n. QED.

For stage j+1 the hypothesis of Lemma 6.1 is the conclusion of stage j, since
2^-(j+3) = rad_(j+1). By induction, with probability at least 1 - 2^-20, theta
lies within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.


### 6.2 Two-adic recovery

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
- If wd >= 2: run TREE_wd (D = wd). If W is even, discard and repeat. If W is
  odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

By (4.1), each attempt succeeds with probability exactly 1/2, even if s1 was
wrong. Set bit g of s2. In the ideal run with s1 correct, every bit is correct.
Output (s1 + M s2) mod N.



On branches where an earlier estimate is wrong, the symbol rem need
not denote a residue satisfying the displayed phase identity. The controller
still performs exactly the stated shifts, label reductions and parity tests.
Conditioned on full latent Fourier labels, every leaf remains a balanced
phase qubit; its recorded reduced label is uniform. The local selection and
recovery probabilities depend only on label residues and amplitude magnitudes,
not on these possibly incorrect phases. Thus the resource renewal and fair
recorded-parity law remain valid on these branches, without asserting that
their measured bit is correct. Correctness is used only conditional on the
preceding decoded bits being correct, as in the union bound below.


## 7. Joint acquisition/work caps and success

For n<256 use exhaustive testing: for t=0,...,N-1 test up to n+10 fresh
copies, subtracting t from the data register on control 1 and measuring the
control in X. Reject at the first minus; output the first passing t. If none
passes output 0. The true s always passes. Each test of a wrong t has plus
probability 1/2, so wrong output probability is less than 2^-10. Every branch
uses at most N(n+10) copies, O(n) qubits, O(n^2) bits and O(N n^4) work.
Controlled modular subtraction is extended by identity outside [0,N), as
in Section 1. This fixed finite prefix is included by absolute constants.

For n>=256 compute Sections 3 and 5 BEFORE acquiring any copy. Set

    K=2^13*(k0+ceil(log2 n)+30),       H0=nK+2n,
    Qstar=2 Emax H0+2n,              Vstar=Vmax H0,
    Qcap=ceil(1024 Qstar),           Vcap=ceil(1024 Vstar).      (7.1)

All numbers are exact integers/rationals. No real-number oracle, approximate
parameter choice or infinite search is used. Set Q and V counters to zero.
Check/increment Q BEFORE every source acquisition, including rejected labels
and unsuccessful attempts. Check/increment V BEFORE each ticket from Section
3; this counts actual executed search units. On a rejected guard discard
all workspace and output 0. If Vstar=0 then Vcap=0 and no positive-width
attempt can start; for the main branch some widths are positive, so Vstar>0.

Use Qcap for EXTRACT precision. Run Section 6 for the odd part, then the
two-adic part, then return (s1+M s2) mod N. Every source transform, decoder
and two-adic loop runs as specified even after an incorrect earlier estimate.

In the uncapped ideal process, accepted odd leaves cost <2 source copies in
expectation, by the uniform-label rejection rule. This factor multiplies
leaf expectations by renewal at a rejected source call; independence between
a returned label and the cost of all future tree decisions is unnecessary.
There are at most nK odd roots. Each two-adic bit uses an expected two fresh
roots by fair untouched parity, or two direct copies when D=1. Cost may
correlate with parity; the same renewal identity applies. Thus physical
source expectation is <=Qstar and ticket expectation <=Vstar, uniformly
given previous decoder outputs. All uncapped ideal loops terminate almost
surely with finite means. Transforming a wrong intermediate secret changes
phases but preserves the required flatness and uniform-label resource law.

The capped ideal process differs from the uncapped one only when a future
actual acquisition or ticket would take its counter above its cap. Markov
bounds each such event by 1/1024. Precharged setup/output macros are part of
the uncapped ticket sum as well. Charges for unfinished children remain
counted when the global guard aborts. A reserved trial ticket permits its finite
verification/reset after any completed iterations. An abort may instead
discard it immediately; its cleanup is polynomial, with no new search.

The actual capped process has at most Qcap numerical extraction calls.
Section 1 gives a label-error union bound 2^-14, even adaptively and including
rejected copies. Couple to the ideal process until the first disagreement.
Do NOT condition the ideal law on extraction success or cap survival.
The ideal odd decoder fails with probability <=2^-20; given its success,
all ideal two-adic bits are exact. Therefore the actual failure probability
is at most

    2^-10+2^-10+2^-14+2^-20 < 2^-8.                           (7.2)

No independence between these error events is asserted. This proves the
same unconditional full-secret guarantee for EVERY modulus and secret.

## 8. Profile analysis, implementation and branchwise bounds

All asymptotic assertions below are uniform in D, input modulus, secret and
outcomes. A finite set of small B or n changes only absolute outer constants.
Write l_B=log2(B+2) and ell=ceil(log2(S_C+S_Q+2)).

### 8.1 Renewal bound for every partial width

For every b>=1, q(b)/(2b+1)<=2. At b=1 equality holds; at b>=2 use
ceil(log2(b+1))<=b. Since q is nondecreasing, for 1<=b<=v,

    q(b)/sigma_b = q(b)+q(b)/(2b+1) <=q(v)+2<=2^(d(v)/2).    (8.1)

An inactive factor is 1 and obeys the same upper bound. Consecutive nominal
levels satisfy v_(i-1)=v_i-d(v_i), so

    sum_(j=i+1)^m d(v_j)=B-v_i.                              (8.2)

Products of ancestor renewal factors are at most 2^((B-v_i)/2), even after
inserting inactive levels. The bottom factor is at most q(v_1)+2<=8v_1. The function
x 2^(-x/2) is decreasing for x>=3, so v_1>=U gives, with one absolute
constant also covering U<3,

    Emax=O(U 2^((B-U)/2)),     q0=O(U 2^((B-U)/2)),
    k0=O(B), K=O(B), H0=O(nB).                              (8.3)

These apply to tiny partial b at a large nominal v. The q0 inequality uses
q(v)<=q(v)+2 and the same telescope; it is not a survival assumption.

### 8.2 Actual ticket sum at the critical decrement

Uniformly in 1<=b<=v, Section 3 implies

    h_b <= C 2^(v/2) sqrt(log2(v+2)/(v+1)).                   (8.4)

For b>=v/2 this follows by comparability. For b<v/2 the exponential gap
absorbs the bounded factor sqrt(log2(b+2)/(b+1)). Since q(b)<=6b and
w=64(n+1), s_b=O(nv), z_b=O(v^2+n). Consequently

 a_b 2^(-v/2) <= C[(v^2+n)sqrt(log2(v+2)/(v+1))
                                        +nv 2^(-v/2)].     (8.5)

This keeps the full n-bit counters; it does not pretend that all operations
have v-bit precision. Also 1/sigma_b<=4/3. Expanding (5.1) and using (8.1)
and (8.2) gives Vmax at most C 2^(B/2) times the sum of the right side of
(8.5) over all nominal levels. The critical ancestor factor is at most one,
not at most one half. Every level is paid.

For PPC, v>=sqrt(B), and d(v)>=2log2 v>=log2 B. Thus the levels are
separated by at least log2 B; m<=1+B/log2 B. Summing an increasing function
and comparing the decreasing function x^(-1/2) with its integral gives

    sum v^(3/2) <= C B^(5/2)/l_B,
    sum v^(-1/2) <= B^(-1/4)+2sqrt(B)/log2 B
                       =O(sqrt(B)/l_B).                     (8.6)

For example, for a decreasing f and ordered points separated by h, all
but the smallest point contribute at most h^(-1) times the integral of f
over the preceding h-intervals. This proves the second inequality with
no density assumption. Multiplying by sqrt(l_B) and using n<=B^2 bounds
the first part of (8.5) by O(B^(5/2)/sqrt(l_B)). The setup part is at most
C nB^2 2^(-sqrt(B)/2), which fits the same bound. Therefore

    Vmax=O(B^(5/2) l_B^(-1/2) 2^(B/2)),
    Vcap=O(n B^(7/2) l_B^(-1/2) 2^(B/2)).                   (8.7)

For PPC-Q, eventually U>=B/8>=sqrt(B); the identical argument applies.
Together with (8.3), Qcap=O(nBU 2^((B-U)/2)) for each configuration with
its OWN B and U. For PPC, U=Theta(sqrt(B)), giving nB^(3/2) as the prefactor;
for PPC-Q, U=Theta(B), giving nB^2. These bounds are for the literal numbers in Section 7.
Their implementation as guards, not the expectation argument alone, gives
the branchwise bounds.

### 8.3 Capacity, ceilings and an explicit supported coefficient

Set dmax=d(B), since d is nondecreasing. For each retained v, the interval
[max(U,v-d(v)),v] has length at most dmax and height at most v. These
intervals partition [U,B] apart from endpoints. Therefore

    C(B)>= (B^2-U^2)/(2 dmax).                              (8.8)

For B>=16, q(B)+2<=2B, hence dmax<=2log2 B+3. For PPC,
U^2<=B+2sqrt(B)+1<=4B. To give an exact rational supported envelope, test

    Btest=ceil((177/125)sqrt(nL)).

For L>=16384, Btest<=n and Btest<=2sqrt(nL); thus
2dmax<=2L+2log2 L+10. Also Btest^2>=(31329/15625)nL.
The exact gap 31329/15625-2=79/15625 satisfies

    (79/15625)*16384 > 2*14+14,
    79/15625 > 4/16384.                                    (8.9)

The derivative of (79/15625)L-2log2 L-14 is positive thereafter, since
ln 2>1/2. Consequently Btest^2-4Btest>=2n(L+log2 L+5), and (8.8) proves
C(Btest)>=n. Least-feasible selection, without any monotonicity hypothesis,
now gives

    B<=ceil((177/125)sqrt(nL)).                              (8.10)

Only the proof uses Btest. The algorithm uses ordinary integer search.
It never allocates an integer with 2^(16384) bits to establish a threshold.
The finite n-prefix below the analytic threshold has finite exact caps and
positive representatives in (T), so its maximum resource/envelope ratios
are absolute constants. This is an asymptotic bound, not a finite hardware
estimate.

Since f(x)=(x-sqrt(x))/2 is increasing with derivative at most 1/2 for
x>=1, (8.10) and U>=sqrt(B) imply

 (B-U)/2 <=(177/250)sqrt(nL)
                   -(sqrt(177/125)/2)(nL)^(1/4)+1/2
           <=(177/250)sqrt(nL)-(59/100)(nL)^(1/4)+1/2.        (8.11)

The final inequality is exact: (118/100)^2<177/125. This is a square-root
base saving in the source exponent. It does not make PPC use fewer samples
than a quarter-base profile.

For PPC-Q, U=floor(B/4) eventually, so U^2<=B^2/16. The same rectangle
argument with Btest=ceil((731/500)sqrt(nL)) gives C(Btest)>=n for
L>=65536: the rational gap (15/16)(731/500)^2-2=15415/4000000 obeys
its threshold inequality gap*L>2log2 L+10 and positive derivative.
Thus PPC-Q separately has

 T=O(n^(11/4)L^(13/4)2^((731/1000)sqrt(nL))),
 S_C=O(n^2), S_Q=O(n),
 Q=O(n^2 L 2^((2193/4000)sqrt(nL))).                         (Q)

The quarter profile's changed exact behavior is sharper than these deliberately
coarse envelopes; the research gain is proved in Section 9, not credited to
another rational rounding of the same leading constant.

### 8.4 Space, finite words and rational preprocessing

Depth-first evaluation keeps at most 1+sum_i(q(b_i)-1)<=1+6(D-1)
phase qubits. One active query, pivot/ripple/sorting scratch, source registers
and transforms add O(n) qubits. Thus S_Q=O(n), with all scratch included.
There are O(n) live signed labels, each of O(n+log q0)=O(n) bits.
The controller, score records and exact arithmetic therefore use O(n^2)
classical bits; no exponentially long circuit or lookup table is stored.

Here are coarse finite bounds justifying the fixed word w=64(n+1), also
on wrong-label branches. For n>=256, B<=n, q0<=6B 2^(B/2) and
Emax<=8B 2^(B/2); hence k0<=n and Emax<2^n. All local widths satisfy
b<=n, q(b)<=n+ceil(log2(n+1))+4<=2n. Formula (3.1) implies h_b<2^n:
the main term has log <=8+ceil(n/2), and the rare term has log at most
ceil(q/2)+log2((8ceil(log2(n+1))+6)ceil(log2(2n+2))), which remains below
n-1 for n>=256. Both ticket weights are <2^(n/2), so a_b<2^(2n).
An ancestor product is <=Emax<2^n; m<=n, giving Vmax<2^(4n).
K<=2^13(n+ceil(log2 n)+30) and H0=nK+2n<2^n. Thus Qcap<2^(3n),
Vcap<2^(6n). Label, frequency, trial and counter integers are all below
2^w in absolute value. These coarse bounds are used only for storage and
finite implementations, not for the asymptotic resource certificates.

Exact recurrence denominators divide a product of (2b_i+1)(q(b_i)+2)^16,
with powers of two that cancel or have O(n) bits. This follows by induction
from (3.1) and (5.1); q_i and 2b_i+2 are integers. Moreover

 sum_i log2(q(b_i)+2) <= log2(q(v_1)+2)+(B-v_1)/2 =O(B).

Also log2(2b_i+1)<=log2(q(b_i)+2)+1. Denominators, numerators and their
reduced cross products have O(n) bits. Iterate over D without storing all
profiles or all recurrence tables. Schoolbook rational arithmetic, sequential
B search, Euclid/CRT, maxima and budget generation take O(n^6) charged
operations and O(n^2) bits. Any temporary product is still O(n) bits.

EXTRACT uses h=O(B+log n)=O(n). Its directions and counters fit O(n^2)
classical bits. The decoder stores K=O(B) full-frequency records of O(n)
bits, also O(n^2). Trigonometric constants are generated once by the explicit
finite procedure, not given as advice. With these allocations ell=O(log(n+2)).

### 8.5 All charged work, source and decoder included

Every local search unit and setup/output/counter macro costs O(ell^2) times
its actual ticket debit by Section 3. The total is O(ell^2 Vcap), plus a
polynomial abort guard and disposal. Skip inactive levels; a depth-first
call or return is charged to a child production or an attempt, apart from
O(m) unfinished frames at abort. These fit the setup/acquisition allowances.

Each physical source call, transformation and EXTRACT costs O(n^3 ell^2),
including its n+1 source debit. Therefore source work is O(n^3 ell^2 Qcap).
Decoder scanning costs at most O(n^4 ell^2 q0), including n stages,
K=O(B)<=O(n) records and full signed-frequency arithmetic. Compared with
the main allowance in (8.7), these are polynomials times 2^(-U/2).
Since U>=sqrt(B)>=n^(1/4), that factor beats every fixed polynomial.
Preprocessing O(n^6) and final cleanup are absorbed as well. This proves (P),
on every actual branch, including wrong earlier estimates and wrong labels.

By sqrt(n)<=B=O(sqrt(nL)), log(B+2)=Theta(L). Substituting (8.10) into
(P) gives n*(nL)^(7/4)*L^(-1/2)*L^2=n^(11/4)L^(13/4).
Using U=Theta(sqrt(B)), its sample prefactor is nB^(3/2)=O(n^(7/4)L^(3/4)).
Substituting (8.11) into Qcap therefore proves exactly (T). For both time and samples,
the dominant logarithm is a positive multiple of sqrt(n log2 n), so the
specified limsup index is 1/2; the lower-order fourth-root term does not
change it. Both polynomial-space envelopes have index 0. The same proof
with PPC-Q's B,U gives its separate bounds (Q).

## 9. What actually improves and what is a parameter tradeoff

The lower bounds here apply only to the explicitly specified search
processes and configurations. They are not general DCP lower bounds.

### 9.1 Smooth capacity comparison despite integer discontinuities

All limits in this section are analytic, not fitted to finite outputs.
Consider a descending profile with d(v)=2log2 v+O(1) uniformly, and either
U(B)=alpha B+O(1), 0<alpha<1 fixed, or U(B)=ceil(sqrt(B)). Its capacity is

 C(B)=(B^2-U(B)^2)/(4log2 B)+O(B^2/(log2 B)^2+B).            (9.1)

Here is a Riemann comparison proof which includes the ceiling jumps.
Sandwich d(v) between 2log2 v+c_- and 2log2 v+c_+ for fixed constants.
For x sufficiently large, f_c(x)=x/(2log2 x+c) is increasing and has
derivative O(1/log x). On [v-d(v),v], the difference between d(v)f_c(v)
and the integral of f_c is O(d(v)^2/log v)=O(log v). Summing costs O(B),
since d(v)=Theta(log v). A truncated bottom interval and the omitted top
endpoint also cost O(B). Lower rectangles using c_+ and upper rectangles
using c_- thus sandwich capacity between these smooth integrals plus O(B).

Differentiating x^2/(4log2 x) shows

 integral_U^B f_c(x) dx = B^2/(4log2 B)-U^2/(4log2 U)
                                  +O(B^2/(log2 B)^2).

The error integral of O(x/(log x)^2) has this bound: on x<=sqrt(B) use
a crude O(B) bound, and on each interval [B/2^(j+1),B/2^j] above sqrt(B)
sum its geometric squared length divided by (log B)^2. For the square-root
cutoff U^2/log U=O(B/log B); for a linear cutoff replace log U by log B
with error O(B^2/log^2 B). This proves (9.1). The same reasoning applies
to the inherited even-width profile with

 d_old(v)=2ceil(log2(3(v+1))), U_old(B)=2max(1,floor(B/8)),

restricted to even top B. It also applies to the half-geometric proposal,
whose decrement is exactly d(v)+2. Parity and ceiling jumps remain within
the uniform constant errors; no smoothness of the actual capacity is assumed.

For least feasible sequential choice, (9.1) implies

 B_sqrt/sqrt(nL) ->sqrt(2),
 B_quarter/sqrt(nL) ->sqrt(32/15),
 B_old/sqrt(nL) ->sqrt(32/15).                               (9.2)

Indeed a trial B=c sqrt(nL) has log B=L/2+o(L), so C(B)/n tends to
c^2/2 in the square-root case and 15c^2/32 in the quarter case. Testing
any fixed larger c gives a feasible top; the uniform capacity upper bound
excludes every smaller c. The even-top restriction adds at most two to a
test and does not change either conclusion. Uniformity also shows that the
chosen capacity C(B)=n(1+o(1)). This argument controls isolated downward
jumps and minimal-capacity selection, not only a favorable subsequence.

### 9.2 A same-base separation stronger than the level penalty

Now compare PPC-Q to PPSA's inherited even-width profile, using the SAME
pivot local instrument, extraction, one-bit decoder and actual-ticket rules.
For all sufficiently large retained v,

 d(v)<=2log2 v+3/2,      d_old(v)>=2log2 v+3.                 (9.3)

The first follows from (q(v)+2)/v->1 and ceil(x)<=x+1; the second from
2log2 3>3. Put I_c(B)=integral_(B/4)^B x/(2log2 x+c) dx.
The rectangle proof above strengthens to

 C_critical(B)>=I_(3/2)(B),    C_old(B)<=I_3(B)+O(B).          (9.4)

The first is exact for all sufficiently large B, since the critical bottom
floor lies below B/4 and each integral rectangle fits beneath its retained
height. The old cutoff differs from B/4 by O(1), absorbed by O(B).

Integrating just over [B/2,B], for log2 B>=3,

 I_(3/2)(B)-I_3(B)
  >=(3/2) integral_(B/2)^B x dx /(3log2 B)^2
   =B^2/(16(log2 B)^2).                                    (9.5)

Let B'=floor(B-B/(100log2 B)). Differentiating I_(3/2), its derivative
is f_(3/2)(B)-(1/4)f_(3/2)(B/4)<=B/log2 B. Monotonicity of x/log2 x
for large x bounds the loss on [B',B] by

 I_(3/2)(B)-I_(3/2)(B')
       <=B^2/(100(log2 B)^2)+B/log2 B.

The positive gap in (9.5) dominates this loss and every O(B) error.
Thus C_critical(B')>=C_old(B) eventually. Apply this at the actual least
feasible old top B_old; since C_old(B_old)>=n, B' is a feasible critical
trial. No monotonicity is used in concluding

 B_quarter <= B_old-B_old/(100log2 B_old)                    (9.6)

for all sufficiently large n. The critical profile may pay m=O(B/log B)
in its work bound; the root exponential saved by (9.6) is
2^(-Omega(sqrt(n/L))), which beats every polynomial in n.

The half-geometric proposal has d_geo(v)=d(v)+2>=2log2 v+2.
Replacing I_3 by I_2 in this argument gives an integral gap at least
B^2/(48(log2 B)^2). A shrink of B/(1000log2 B) leaves a positive gap.
Thus the critical quarter profile also has top at most
B_geo-B_geo/(1000log2 B_geo) eventually, with each profile chosen by its
own sequential minimal-capacity search. The geometric profile has no level
penalty, but this stretched-exponential root saving still dominates the
critical profile's polynomial level count. This justifies choosing critical
among the two proposed rules without asserting global optimality.

For a precise complete certificate comparison, let

 F(n)=ceil(log2(n+2))^2
           *(Vcap+n^3 Qcap+n^4 q0+n^6).                    (9.7)

Use each configuration's OWN caps and q0. The unchanged implementation
costs O(F) on every branch. Section 8 bounds F_critical by a polynomial
in n times 2^(B_quarter/2). For the inherited profile, TREE_n's root has
full width B_old once n is large, since B_old=O(sqrt(nL))<n-1.
Its positive root term in v_n contains h_(B_old)>=2^(B_old/2)/sqrt(q(B_old))
by the main term of (3.1) and t_b<=log2 q(b). Therefore F_old is at least
2^(B_old/2) divided by a fixed polynomial in n. Equations (9.6)-(9.7) prove

             F_critical/F_old ->0.                         (9.8)

This compares two complete, explicit, differently parameterized resource
certificates. It includes acquisition, full precision, decoding and setup.
It is neither a ratio of realized branch costs nor a source-dominance claim.

There is also a full ideal-label EXPECTATION comparison, not just two upper
bounds. To supply the needed lower bound, on any nonsingleton measured fiber
write z=|F|-1 and A'=2^(q-t). A trial with j Grover steps succeeds with
probability <=4(j+1)^2 z/A'. Stopping before total query units exceed h,
a union bound gives success probability <=4h^2 z/A'. The complete bounded
schedule succeeds with probability at least 3/4 on a nonsingleton. With
h=(1/4)sqrt(A'/z), this gives E[H|labels,fiber]>=sqrt(A'/z)/8.
One may formally define h as a real cutoff on the integer debit sum.

Uniformly t<=log2 q, so A'>=2^q/q. The unconditional planted moment gives
Pr(0<z<=2lambda)>=1/2-1/(1+lambda)>=1/2-1/31, and
2^q/lambda>2^b. Hence even WITH pivots

             E H =Omega(2^(b/2)/sqrt(q(b))).                (9.9)

No moments were conditioned on pivot availability. Root work includes H,
so PPSA's full uncapped ideal-label algorithm has mean work at least
2^(B_old/2)/poly(n). For every large N it must construct such a root:
if its odd part is nontrivial, the first odd stage uses D=d>=n-1;
otherwise the first two-adic stage uses D=n. Either has full top width.
PPC-Q's full ideal-label expected work, with all physical supplier work at
its stipulated precision charged, is at most poly(n)2^(B_quarter/2) by
Sections 5-8. Therefore its mean/old-mean ratio tends to zero, uniformly in
modulus and secret. This ideal-label comparison replaces extraction outputs
by their true latent labels while charging their actual routines. It does
NOT assert a ratio for the two noisy, capped physical algorithms; those
algorithms separately retain the unconditional success and branchwise bounds.

For the ORIGINAL no-pivot instrument the same argument has A'=2^q and
gives Omega(2^(b/2)), versus the inherited pivot upper bound
O(2^(b/2)sqrt(log(b+2)/(b+1))). That local mechanism gain is prior PPSA
work, fully credited, rather than claimed as this profile integration's invention.

### 9.3 The base change is a genuine sample tradeoff

The leading logarithms of the literal caps, not just coarse displayed bounds,
can be identified. Along an active full segment, for either critical or old
profile, log2(q(v)/sigma_v)=d(v)/2+O(1). Summing the O(1)'s costs
O(m)=O(B/log B); a partial bottom adds O(log B). For D=n, the unallocated
capacity is C(B)-(n-1)=o(n) by (9.1)-(9.2). Were the bottom active nominal
width separated from U by epsilon B in the linear-base case, or at least
epsilon B in the square-root case, the omitted interval would already have
Omega(B^2/log B)=Omega(n) capacity by the same rectangle argument. Hence
the bottom active nominal width is U+o(B) or o(B), respectively.
Consequently, using e_n for the lower bound and (8.3) for the upper bound,

    log2 Emax=(B-U)/2+o(B),
    log2 Qcap=(B-U)/2+o(B).                                 (9.10)

The inherited upper bound follows from its telescope as well; the extra
renewal margin can only change O(m) in this leading-order statement.
Similarly the positive full-root h term and the upper ticket bound give
log2 Vcap=B/2+O(log n). Source, decoder and preprocessing are smaller by
2^(-U/2) up to polynomials, so log2 F=B/2+O(log n). Thus

                 log2 F/sqrt(nL)     log2 Qcap/sqrt(nL)
 PPC                 1/sqrt(2)             1/sqrt(2)
 PPC-Q               sqrt(8/15)            sqrt(3/10)
 inherited PPSA      sqrt(8/15)            sqrt(3/10).        (9.11)

These are limits of specified complete certificates and caps. They are not
matching lower bounds on the capped physical algorithm's resource use.
Equation (9.6) distinguishes critical and inherited profiles below their
shared leading coefficient. The main PPC base change makes the time
certificate smaller in its leading exponent but makes the acquisition CAP
larger in its leading exponent. Finite screens showing sample increases for
the denser quarter profile are consistent with this, but are not promoted
to an all-n source ordering between the two quarter profiles.

Any fixed rational c>1/sqrt(2) can replace 177/250 after an appropriate
analytic threshold proof. That freedom is coefficient slack, not another
mechanism gain. The square-root base is not claimed optimal. A logarithmic
base would require an explicit sufficiently large coefficient to pay source,
decoder and setup polynomials; this draft uses sqrt(B) to settle those costs
without importing grouped sums, batched extraction or a stride decoder.

## 10. Clean-input claim, comparisons and research status

The fifth claim uses exactly this error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Fraction epsilon(n)=0 permits zero malformed acquisitions. For every N,s,
Sections 7-8 prove the same success and all four resources jointly under
that promise. This does not prove that positive tolerance is impossible.

The frozen comparison snapshot has 125 records, refreshed by the parent at
2026-11-07 01:20 UTC. Narrow selected records and their hashes are archived.
PSG11's exact proof states time 2^((187/256)sqrt(nL)), samples
2^((561/1024)sqrt(nL)), quadratic classical bits and linear qubits. The
main PPC guarantee has a smaller time coefficient and a larger sample
coefficient, so neither guarantee dominates the other. PPSA is likewise a
time/sample tradeoff against PPC. The analytic same-base result (9.8) is a
comparison to the inherited PPSA configuration and certificates; PSG11 uses
a different local instrument, compiler and decoder and is not substituted
into that theorem.

GPS2, PSG2-GBGR, PSG3, PSG17 and PSG21 are recorded as recent public context,
with their current immutable commits. No proof or theorem from them is
imported. In particular, this draft has not audited GPS2's coefficient
proof or PSG2-GBGR's grouped-sum/compiler proof. A formal ordering of their
displayed coefficients is not used to claim a newly established public
frontier victory or algorithmic separation. Their hosted validity status
is metadata, never a premise. The source and decoder proof here is the
conservative reproduced CYG1/PPSA implementation.

The proof has a complete all-N algorithm and literal resource caps; it is
still an unsubmitted research draft requiring independent mathematical
review. Finite diagnostics check exact rational recurrences, capacities,
partial-width guards, phase identities and provenance. They are neither a
proof of the asymptotic limits nor acceptance. The pinned verifier is used
only for deterministic format admission. No provider judgment is requested.

The specific advances are an all-D critical-profile integration, a complete
square-root-base tradeoff with explicit supported envelopes, and a proved
stretched-exponential full-certificate and ideal-label-mean separation for
the changed critical schedule at a fixed quarter base. The resource index
remains 1/2. The public leading constants in (T) are conservative rational
representatives; the algorithmic distinction is the profile rule and the
comparisons in Section 9. No finite-output trend establishes index .498.
