# F4: four-entry recovered collimation

The proof below specifies one
algorithm for every modulus, including its source, precision, decoder,
retry rules and literal acquisition/work caps. It does not use a hosted
judgment as a premise. Section 11 points to the seed audit and material reuse.
The source-interface and decoder text is reproduced from the actual PPC
proof, SHA256 fabdda361727dba6378f546376c521fc91e94c3e803051f230df673b5590cfa4,
with its scope fix retained. The new integration is proved here.

## 0. Joint theorem and scope

For every integer N>=2 and fixed s in Z/NZ, set n=ceil(log2 N), L=log2 n.
From independent ideal DCP copies, F4 returns s with unconditional
probability at least 1-2^-8. On every branch, jointly,

    T = O(n^(11/4) L^(13/4) 2^((177/250)sqrt(nL))),
    S_C = O(n^2) bits,             S_Q = O(n) qubits,
    Q = O(n^(7/4) L^(3/4)
             2^((177/250)sqrt(nL)-(59/100)(nL)^(1/4))).       (T)

These representatives apply for n>=2; all 1<=n<256 use the exhaustive
finite branch in Section 7. Constants are independent of modulus, secret
and outcomes. The time and sample growth indices are 0.5; the two space
indices are 0. The verifier encodes these exactly as 1/2 and 0/1. Fractional
tolerance is 0 in the clean-copy model of Section 10. No bound with growth
index 0.49999, encoded 49999/100000, is proved.

For n>=256 the stronger, executed-profile guarantees are

    T = O(n B^(7/2) log2(B+2)^(-1/2) log2(n+2)^2 2^(B/2)),
    Qcap = O(n B^(3/2) 2^((B-U)/2)),  U=ceil(sqrt(B)).        (P)

The maximum width B is the first sequentially feasible trial of Section 5.
There is no monotonic-capacity assumption. At width b the algorithm uses
f(b) fresh FOUR-ENTRY child vectors. It measures one fixed index bit of
the FIRST floor(f/4) children, leaving q=2f-floor(f/4) index qubits. Here

    c=ceil(log2(b+1)),
    f(b)=min{f>=4:2f-floor(f/4)>=b+c+6},
    d4(b)=ceil(log2((f(b)+1)^2)).                            (0.1)

Every base vector uses TWO supplier leaves. The output length stays four
at all internal nodes. Section 9 proves, at the SAME square-root base,

    B_F4 <= B_PPC - B_PPC/(1000 log2 B_PPC)                 (G)

eventually, for the actual least-feasible profiles. It also proves a
vanishing ratio of their complete exact resource certificates and of their
uncapped ideal-label mean work. This is an executed arity/profile change,
independent of rational-envelope slack. We retain PPC's representative
coefficients in (T), so the declared vector is not a new strict improvement
over PPC's declared vector. No all-n ordering of their source caps is claimed.

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


## 2. Four-entry states, carry and the recovered instrument

### 2.1 Representation and fixed-position qubitization

A vector collimated to p bits has two index qubits and FOUR full nonnegative
integer labels A[0],...,A[3], all congruent modulo 2^p. Its state is

    (1/2) sum_(r=0)^3 exp(i theta A[r]) |r>.

The common residue need not be zero. At p=0 make the base from two fresh
supplier phase qubits with labels a,b, using table (0,a,b,a+b) and the
index convention |r>=|x_b,x_a>. This costs two independent original leaves.
Returned four-entry vectors need not be products of qubits.

For a width-b attempt, generate f=f(b) fresh child vectors at depth p.
For j=1,...,k=floor(f/4), in this fixed order and without inspecting high
label values, measure the high index bit. Retain its outcome eta_j and the
low bit, with table (A_j[2 eta_j], A_j[2 eta_j+1]). The outcome is a fair
bit. Reset the measured qubit; the chosen two rows remain a balanced qubit.
All other children retain their two qubits and four rows. Thus the combined
index x has exactly q=2f-k bits and 2^q equal-magnitude amplitudes. Charge
every measurement/reset and every child, including the discarded rows.

Every row is the sum of a distinct subset of its original supplier leaves.
Equivalently its analytical incidence is a distinct binary vector. Different
children have disjoint leaf sets. Tensoring the tables and selecting distinct
tuples preserve distinct binary incidences. Numerical label equality does
not identify two rows. Incidences are proof objects; the algorithm stores
only four full labels and a two-bit index per vector, not the leaf subsets.

Here is the exact carry-aware predicate. For every child, use its retained
table and set rho_j=A_j[0] mod 2^p, with rho_j=0 for p=0. All its rows have
this residue. Write A_j[r]=rho_j+2^p a_j[r] and compute classically

    rho=(sum_j rho_j) mod 2^p,
    Ccarry=floor((sum_j rho_j)/2^p),
    F_b(x)=(Ccarry+sum_j a_j[x_j]) mod 2^b.                      (2.1)

For p=0 this gives Ccarry=0. The full tuple label is
rho+2^p(Ccarry+sum_j a_j[x_j]), exactly. Computing F_b into a clean b-bit
register and measuring e retains the fiber F=F_b^-1(e), with probability
|F|/2^q. Its phases are the ORIGINAL full tuple phases. Reset the measured
register using e. Every resulting full label is congruent to rho+2^p e
modulo 2^(p+b). Subsequent steps keep the full nonnegative integers.

The controller computes rho_j,Ccarry and the b-bit entries of a_j once in
O(f w) core operations, where w is the fixed word width of Section 3.
Each quantum table lookup is an explicit scan of at most four rows, using
one/two index-bit equality controls and a controlled constant addition.
It costs O(b) per child, O(qb) altogether, with O(q+b) quantum scratch.
There is no QRAM or full-fiber table. The cost of computing carry is not
charged as a b-bit-only operation.

### 2.2 A known coarse-fiber query

For a qubitized child write a_j[x_j]=a_j[0]+delta_j x_j. Let
u=ceil(log2(q+2)) and choose t_* as the largest integer t>=0 with
16u 2^t<=k, or zero if there is none. Use t=t_* if all valuations
0,...,t_*-1 occur among the k differences modulo 2^b; otherwise use t=0.
For each valuation choose the first eligible child. The pivots are distinct
and t<=b. All choices here inspect only the current low block.

Prepare the q-t nonpivot bits by Hadamards. Into a t-bit accumulator
compute e-Ccarry minus all free-table contributions and minus the constant
a_j[0] of each pivot. For i=0,...,t-1, copy accumulator bit i to the
initially zero pivot bit of valuation i, then subtract delta_j controlled
by that pivot. Lower bits stay zero and the accumulator ends zero.
There is exactly one pivot assignment for each free assignment: the
lowest differing pivot has nonzero contribution at its valuation.

This is a known exact unitary U_query preparing the uniform state on

    S={y:F_b(y)=e mod 2^t},  A'=|S|=2^(q-t),  F subset S.   (2.2)

In particular S contains the ENTIRE measured fiber, regardless of pivot
availability. Reverse the additions and CNOTs for U_query^-1. The zero reflection
uses a Toffoli ladder, including scratch wires. U_query(2|0><0|-I)U_query^-1 reflects
about the known query state, never about an unknown source state. Discovery
costs O(qb) classical steps. Preparation, inverse and reflection cost
O(qt+q+b) core gates with O(q+b) scratch. The four-row scans remain constant
size even though the combined index space is exponential.

### 2.3 Extending an unknown coherent tuple

Retain a tuple Xtuple=(x_0,...,x_(a-1)) of distinct elements of F, for a=1,2,3.
Here x_0 carries the original phase; a is an endpoint count, not a label.
Prepare a fresh query Y on S. Mark Y iff Y in F and Y differs from ALL
entries of Xtuple. Every basis tuple has z=m-a marked queries, where m=|F|.
After j Grover iterations every marked amplitude is g_j/sqrt(A'), and
every unmarked amplitude is h_j/sqrt(A'). The coefficients are independent
of Xtuple and obey

    g_0=h_0=1,
    g_(j+1)=(1-2z/A')g_j+2(1-z/A')h_j,
    h_(j+1)=-2z/A' g_j+(1-2z/A')h_j.                       (2.3)

On success keep Y quantum. The successful Kraus map is a scalar times
the isometry J_a |Xtuple>=(m-a)^(-1/2) sum_(y in F minus Xtuple)|Xtuple,y>.
On failed marking, measure ONLY membership Y in F. If false, every
outside value y in S minus F has amplitude h_j/sqrt(A') independent of Xtuple.
Measure/reset Y. Each such outcome is that scalar times identity on Xtuple.
If true, compute the unique position ell for which Y=Xtuple_ell. Measure ell,
NOT the endpoint value. Uncompute comparison scratch while Xtuple,Y remain,
then XOR the classically selected Xtuple_ell into Y. The resulting Kraus map
is again h_j/sqrt(A') times identity on the ENTIRE tuple. Erase ell's
measured encoding using its classical value. These statements hold on
arbitrary superpositions and with arbitrary reference systems.

Thus failed trials recover the old tuple exactly. Trials use fresh coins
on that same tuple; a successful trial adds an endpoint. If any extension
exhausts its finite schedule, discard the entire tuple and all children.
There are no additional source acquisitions inside an extension. All inputs
to a failed node are charged by the recursive supplier recurrence.

### 2.4 Four-endpoint extraction and old-index cleanup

Starting from a flat phase fiber, three successful extensions give

    (m)_4^(-1/2) sum_(distinct x_0,x_1,x_2,x_3 in F)
           exp(i theta A(x_0)) |x_0,x_1,x_2,x_3>,           (2.4)

where (m)_4=m(m-1)(m-2)(m-3) and A(x) is the full tuple label.
For a distinct ordered tuple compute its sorted list S4=(c_0<c_1<c_2<c_3),
the rank r of x_0, and the permutation pi of x_1,x_2,x_3 relative to the
sorted list S4 with c_r removed. pi has exactly six valid three-bit codes.
The inverse map is x_0=c_r and x_1,x_2,x_3 the indicated permutation of
the other three entries. This is a bijection on the valid domain.

An explicit clean implementation first computes (S4,r,pi) in new registers
while retaining Xtuple. It then computes this inverse and XORs its four q-bit
outputs into Xtuple, clearing ALL old endpoint registers. Reverse the temporary
inverse scratch computation, controlled only by (S4,r,pi). A fixed sorting
network and comparison gates implement encoding in O(q) core steps;
decoding scans four entries with constant-size selectors in O(q) steps.
Temporary comparison flags are uncomputed. Arbitrary padded inputs can
have any fixed total Boolean extension, since compute/XOR/uncompute remains
reversible and only the distinct-tuple subspace is used. This construction
does not keep a hidden copy of x_0 or of the old tuple.

Measure S4 and pi, keep r, and reset the measured registers. For each fixed
S4,pi the output is exactly

    (1/2) sum_(r=0)^3 exp(i theta A(c_r)) |r>.              (2.5)

Compute and store all four full labels A(c_r), using O(fw) core steps.
No whole-fiber rank is computed. The measured set is sorted by index, not
by high numerical labels. pi is independent of r and any reference: on an
arbitrary input the conditional extension-and-sort Kraus map is

    K_(S4,pi)=[(m-1)(m-2)(m-3)]^(-1/2)
                       sum_(r=0)^3 |r><c_r|.              (2.6)

It is the same for every pi. Summing the six pi outcomes gives coefficient
binom(m-1,3)^(-1/2) for the uniform-four-subset instrument. Its squared
Kraus maps sum to identity on F. On a flat input S4 is uniform among the
four-subsets of F; all record probabilities are phase independent.

Up to four q-bit endpoints are simultaneously live. The encoding, inverse
and query scratch add only a CONSTANT number of q-bit blocks. The quantum
cost is O(4q+b), with that constant paid. For variable output length h it
would be O(hq), so this proof uses h=4 throughout.

### 2.5 Bounded dyadic search, including dense fibers

Use two recovered trials at each dyadic scale J=1,2,4,...,Jmax/2 and R
trials at Jmax=2^ceil((q-t)/2), stopping at the first success. A trial
chooses j uniformly from 0,...,J-1 by fair bits. Its work units are j+1,
including verification and recovery. Every extension has
H<(R+2)Jmax. For z>0 its failure probability is at most (3/4)^R and

    E H <=40 sqrt(A'/z).                                  (2.7)

Here is a proof, to fix the schedule constant rather than import a query
oracle. For 0<z<A', sin^2 gamma=z/A' and the averaged success probability is
p_J=1/2-sin(4J gamma)/(4J sin(2gamma)). At Jmax, Jmax sin(2gamma)>=sqrt(2),
so p_J>1/4. For z=A' every trial succeeds; in the tuple setting z<A'.
For z<A'/2 let J_* be the first dyadic scale >=2/sin(2gamma). If it occurs,
J_*<=2sqrt(2A'/z) and all subsequent p_J>=3/8. Two-trial scale failure is
at most 25/64. Summing earlier work, geometric later work and terminal
expected work gives [2+2/(1-25/32)+8/3]J_*<40sqrt(A'/z).
If J_* exceeds Jmax, the cost is at most 6Jmax<6sqrt(2A'/z).
For z>=A'/2 put eta=pi/2-gamma. At J=1 success is >=1/2. A negative
correction at any later J requires eta>pi/(4J); hence
4J sin(2eta)>=4J sin(pi/(2J))>=4sqrt(2), so p_J>5/16.
Two-trial scale failure is at most121/256. The bound
2/(1-121/128)+16/5<40 proves (2.7). For z=0 use the deterministic cap.
Exact recovery makes these bounds conditional on any preceding failures;
no independence between work and success is assumed.

## 3. Fresh-block bounds and literal rational local budgets

### 3.1 Planted moments under the right filtration

Condition on original supplier leaves modulo 2^p, the subtrees' selections
and retries through depth p, independent history BEFORE generating these
children, and the fixed-position qubitization outcomes. Do not condition
on completed child tables, next-block pivot events, attempts' cost, EXTRACT
internal records, or future cap survival. Section 4 proves this filtration
is legitimate simultaneously with termination. The fresh b-bit blocks of
the original leaves are then independent uniform modulo M=2^b.

Fix a planted tuple X, uniform among all A=2^q tuples independently of the
fresh blocks. Tuple incidences z_x are distinct binary vectors. For Y!=X,
z_Y-z_X has a unit coefficient. For distinct Y,W!=X the two difference
rows modulo 2 are nonzero and distinct, hence independent over F_2. They
have an odd 2-by-2 minor, which is invertible modulo 2^b. In fact coordinate
signs are fixed by X, so a nonzero such minor is +/-1. Known low-part carries
only add constants. Therefore F_b(Y)-F_b(X) is uniform, and two such
differences are jointly uniform. Collision indicators are pairwise independent.

Writing Z=|F|-1 for the fiber containing X, the measured fiber has exactly
this size-biased planted law. For every such low transcript,

    lambda=(A-1)/M,  E Z=lambda, Var Z=lambda(1-1/M).        (3.1)

These claims concern original leaf blocks, not independence of the four
correlated rows of a child table. The least-arity rule gives
b+c+6<=q<=b+c+7, so lambda>=63(b+1). It also gives f<=5b: at f=5b,
q>=35b/4>=b+c+6, using c<=b and b>=1. f is nondecreasing. The exact
constant-time arity formula is

    f=min_(r=0,1,2,3) [4 max(1,ceil((b+c+6-2r)/7))+r].     (3.2)

It follows from f=4a+r =>q=7a+2r and avoids huge-width linear loops.

The k qubitized differences have disjoint original leaf sets. Each is a
nonzero signed binary difference, so after fixing the low transcript and
qubitization outcomes its next block is uniform. The k differences are
independent. For t_*>0 the missing-pivot probability is therefore

    delta<=t_* exp(-k/2^t_*)<=u exp(-16u)<=u(q+2)^(-16).     (3.3)

For t_*=0 the missing event is empty. The definitions give t_*<=b and
2^-t_*<=32u/k, also when t_*=0. Since k=Theta(b), this is the desired
logarithmic-over-linear reduction. These are unconditional over the fresh
blocks. No fiber-moment formula is conditioned on pivot availability.

### 3.2 Survival and a rational expected-work certificate

Set R=8c+16. Since (3/4)^8<1/8, each extension of a fiber with m>=4 fails
with probability <1/[64(b+1)^3]. For lambda>=126,

    Pr(m<4)<=lambda/(lambda-2)^2<=2/lambda,
    Pr(Z<lambda/2)<=4/lambda.

The three extensions thus fail in total with probability at most

    2/[63(b+1)]+3/[64(b+1)^3] < 1/[8(b+1)].                (3.4)

The last inequality follows by multiplying by b+1 and using b+1>=2:
2/63+3/256<1/8. Set sigma_b=(8b+7)/(8b+8). This includes too-small
fibers, which exhaust at most three finite search caps. Repeated trials
preserve state exactly; a successful bounded node gives exactly (2.5).

For work define a pointwise allowance, with no pivots yet,

    B(Z)=120 sqrt(3A/lambda)       if Z>=lambda/2,
         3(R+2)sqrt(2A)           otherwise.               (3.5)

On the high event every m-a>=lambda/3, a=1,2,3, so (2.7) bounds the
total conditional mean by B(Z). On the low event use all three caps.
Reaching an extension can only decrease this total bound. By (3.1),

    E B <=120 sqrt(3A/lambda)+12(R+2)sqrt(2A)/lambda
         <512 sqrt(M).                                    (3.6)

For explicit constants, A/lambda<=2M and lambda>=63(b+1). Also
(c+3)^2<=9(b+1): on each c-block the smallest b+1 is 2^(c-1)+1;
the inequality holds at c=1 and its difference increases by
9*2^(c-1)-(2c+7)>=0. Since R+2=8c+18<=8(c+3), the two terms in (3.6)
are bounded by 120sqrt(6) sqrt(M)<300sqrt(M) and
(576/sqrt(63))sqrt(M)<73sqrt(M), respectively. The stated 512 leaves
explicit slack. This split charges low-fiber exhaustion, not only m>=4.

On pivot success the pointwise allowance scales by 2^(-t_*/2). On pivot
failure use the original deterministic three-cap bound and (3.3).
E[B 1_pivot]<=E B, so no independence is needed. A rational certificate is

    h_b=512*2^(ceil(b/2)-floor(t_*/2))
        +1_[t_*>0]*3(R+2)*2^ceil(q/2)*u/(q+2)^16.          (3.7)

It upper-bounds E H_total for an entire width-b attempt. All powers in
(3.7) are integer powers. Uniformly for b>=1,

    h_b=O(2^(b/2) sqrt(log2(b+2)/(b+1))).                  (3.8)

For the main term use 2^-t_*<=32u/k and k=Theta(b). For the rare term
use q<=b+c+7, so 2^ceil(q/2)<=32sqrt((b+1)2^b). Dividing that term by
the right side of (3.8) gives O(log(b+2)^(3/2)/(b+1)^15). The two integer
roundings in the main term cost at most a factor two. Small b are included.

### 3.3 Charged macros and counters

Use the deterministic word width w=1024(n+1); Section 8 bounds every full
label, counter and rational temporary. Define

    s_b=q(w+b+1)+w,  z_b=q(b+1)+w,
    a_b=2s_b+z_b h_b.                                    (3.9)

Before residue setup debit 2s_b work tickets or abort. This reserves setup,
qubitization, carry construction, all final four-label computations,
tuple encoding/cleanup and disposal, up to a fixed universal multiplier.
Before each trial debit z_b, and before EACH Grover iteration debit z_b.
A trial has exactly j+1 such debits. Its first debit reserves uniform-query
preparation, random j, final verification, failed-position measurement,
recovery and reset. Choosing fresh j uses at most O(q) fair bits. Three
extensions together have actual ticket total 2s_b+z_b H_total.

Every macro fits its ticket weight times one universal constant in core
operations: predicates and reflections cost O(qb+q); comparisons against
up to three coherent endpoints cost O(q); four-endpoint encoding and
inverse cost O(q); carry, table setup and full output sums cost O(qw).
Counter compare/add costs O(w) and is included. Section 1's O(ell^2)
address/generation allowance converts core steps to charged sequential work.
The weights are accounting units, not a claim of one physical gate per ticket.
The V cap checks their ACTUAL sum. Reserved finite macros finish before
the next debit. At a failed guard, discard the live state and output 0;
aborting inside an extension claims no retained phase state.

Base-table construction and the final root measurement/difference use
O(w) per base/root and are charged in the physical-source allowance in
Section 8, not silently omitted from total work. V counts only positive
node attempts. Source supply and child work are separate in Section 5.
Every local branch has H_total<3(R+2)2^ceil(q/2), even on incorrect labels.

## 4. Low-transcript induction, termination and the root law

Fix deterministic widths totaling at most D-1. A supplier leaf has an
independent uniform D-bit label and its balanced phase qubit. The ideal
process replaces numerical extraction by the true latent label and ignores
EXTRACT's internal records. The actual process will be coupled to this one.
Nonroot calls return four-entry vectors. Inactive widths simply return
their child. Each positive node builds f(b) fresh children; on local failure
it discards all children and restarts from fresh independent suppliers.

We prove simultaneously, by level, finite mean termination and the following
invariant. Returned rows have distinct binary incidences, full
labels with a common low-p residue, and flat amplitudes with their original
phases. For every finite selection transcript hist at that depth the kernel
obeys

    P(hist | all leaf labels)=K_hist(labels mod 2^p).         (4.0)

The transcript contains discarded-attempt low labels, child selections,
qubitization outcomes, pivot choices, e, all Grover coins and failure
records, S4 and pi. It omits unused numerical high labels and EXTRACT test
records. Conditioning on "everything the controller knows" would be wrong.
Full labels may be computed and stored; their high values feed no selection
branch. Fixed-width arithmetic runtime is not a high-label-dependent choice.

The base has no selections, two independent leaves and the stated four
incidences. Assume the invariant and finite mean termination for children.
Before a fresh node attempt its successful child selection laws depend
only on original low-p bits. Conditional on these low transcripts, higher
blocks of every used leaf remain independent uniform. Fixed-position
qubitization has probability 1/2 per outcome, independently of phases and
labels, so it preserves this factorization. Section 3 applies at this
point. Average it over the low transcripts to get fresh-attempt success
at least sigma_b>0, uniformly given independent PREVIOUS history.

All child means are finite by induction and local work is bounded. Attempts
at this node use disjoint fresh source streams with fixed parameters.
Their unconditional pairs (cost, success) are identically distributed and
independent across attempts. They need not have independent coordinates.
Geometric fresh retries therefore terminate almost surely with finite mean.

For the new invariant, residue probabilities are m/2^q. Each recovered
failure record is scalar identity by (2.3). Successful extension probability
depends only on m,a,j,A'; the three successful isometries lead to (2.4).
Every fixed S4,pi has probability independent of phases, by (2.6). Thus the
new finite transcript kernel depends only on leaf values modulo 2^(p+b).
The carry in (2.1) uses no higher bits. Explicitly, fix a finite transcript
hist, including its used leaf positions, and write these D-bit leaf labels
as lo+2^(p+b)hi. Each conditional record probability is

    P(hist_i | hist_<i,lo,hi)=k_i(hist_i;hist_<i,lo).

The factors are the fair qubitization/coin probabilities, m/2^q, the scalar
failure norms, extension success norms and the probabilities in (2.6).
All their indices, supports and amplitudes are functions of lo. Thus the
product K_hist(lo) contains no hi. Whenever the conditioning event has
positive probability, Bayes gives

    P(hi=h | lo=l,hist)=P(hi=h | lo=l),

the original product-uniform law on the untouched blocks. Include every
preceding failed attempt in hist; the same factorization applies. Average
over the countably many finite terminating transcripts, whose probabilities
sum to one. This never conditions on completed tables, success-biased cost,
correct extraction, or future cap survival.

The selected rows are distinct tuples on disjoint child leaf sets, so their
incidences stay distinct binary vectors. Their labels are congruent by
(2.1), and (2.5) preserves all four phases, completing the invariant. There
is no assertion that all four entries, or their high parts, are independent.

At the root, after cancelling D-1 bits, measure its FIXED high index bit.
For result eta retain rows 2eta and 2eta+1, reset that measured bit and keep
the low bit. Return the full signed difference
x=A[2eta+1]-A[2eta]=2^(D-1)W. This final outcome is fair and its kernel
uses no label bits. The selected difference has incidence coefficients
z_l in {-1,0,1}, with at least one unit coefficient. Conditional on the
low transcript, write original labels l_l+2^(D-1)tau_l. Then

    W=carry+sum_l z_l tau_l,  tau_l independent fair bits,
    |E exp(2 pi i yW)|<=|cos(pi y)|,  Pr(W odd)=1/2.        (4.1)

The carry is an INTEGER because the two rows share the entire low residue.
Each unit coefficient supplies a cosine factor and every other factor has
modulus at most one. This is a signed-integer characteristic law, not a
claim that W itself is uniformly distributed. It is exactly what Section 6
needs. Root conversion at D=1 is also defined on the two-leaf base; the
two-adic decoder instead uses its stated direct one-leaf shortcut there.

## 5. Fixed profiles, exact all-D maxima and renewal

For n>=256 sequentially try B=1,2,...,n. Set U=isqrt(B-1)+1. Starting at B,
retain v while v>=U, then replace v by v-d4(v). Reverse the retained list
to v_1<...<v_m=B. Choose the FIRST trial with sum v_i>=n. It exists by B=n,
and sum v_i<=B^2 gives B>=sqrt(n). No binary search is used.

For TREE_D, 1<=D<=n, allocate D-1 cancellation bits greedily from the root
down: b_i=min(v_i,remaining); subtract it and continue. There is at most
one partial positive width; all its ancestors are full. Skip zero widths.
The base is always the two-leaf vector. A returned root then undergoes
Section 4's fixed-bit conversion. Define the NOMINAL successful-leaf bound

    q0=2 product_i f(v_i),  k0=ceil(log2 q0).               (5.1)

Discarded attempts never contribute to a returned label, although all
their source copies are charged. Every full nonnegative label is <q0 2^D;
the root difference has |W|<2q0. These finite bounds also hold on wrong-label
branches because each supplier returns a D-bit encoding.

For EACH D=1,...,n start e=2,v=0. Process its actual positive widths bottom
up using the EXACT rational recurrence

    e <- f(b)e/sigma_b,
    v <- [f(b)v+a_b]/sigma_b.                              (5.2)

Set Emax=max_D e_D, Vmax=max_D v_D. These are literal all-D maxima,
including e_1=2,v_1=0. Keep only one D's working recurrence at a time.
Vmax is not replaced by v_n because (3.7) has ceiling discontinuities.

If one fresh node attempt has actual success probability p_i, renewal gives

    E_i=f_i E_(i-1)/p_i,
    V_i=[f_i V_(i-1)+E(local tickets)]/p_i.                 (5.3)

The proof is first-attempt cost plus (1-p_i) times an independent fresh
future. It does not condition that cost on success. Child cost can correlate
with its returned label. Section 4 gives p_i>=sigma_b after averaging over
fresh children; Section 3 gives E(local tickets)<=a_b under the correct
filtration. Thus (5.2) bounds uncapped ideal means, including failed tuples,
all regenerated children, and TWO leaves at every base.

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

## 8. Joint charged resources and exact word bounds

All asymptotic constants below are uniform in D,N,s and outcomes. Put
l_B=log2(B+2) and ell=ceil(log2(S_C+S_Q+2)).

### 8.1 Ancestor products and all partial widths

For b>=1, f(b)<=5b gives

    f(b)/sigma_b=f(b)+f(b)/(8b+7)<f(b)+1.

Monotonicity of f therefore gives, for 1<=b<=v,

    f(b)/sigma_b<=f(v)+1<=2^(d4(v)/2).                     (8.1)

An inactive factor is 1 and satisfies the same inequality. Adjacent nominal
levels obey v_(i-1)=v_i-d4(v_i), so

    sum_(j>i)d4(v_j)=B-v_i.                               (8.2)

The ancestor product above nominal level i is at most 2^((B-v_i)/2),
regardless of partial or inactive widths below it. The bottom factor is
at most f(v_1)+1<=6v_1. Including the base factor TWO, and using that
x2^(-x/2) decreases for x>=3, yields

    Emax,q0=O(U 2^((B-U)/2)),
    k0,K=O(B), H0=O(nB).                                 (8.3)

The finitely many U<3 are absorbed in the absolute constant. This also
bounds the zero-positive-width case; it is not an argument only for D=n.

### 8.2 Total ticket bound

Uniformly for 1<=b<=v, (3.8) implies
h_b<=C 2^(v/2) sqrt(log2(v+2)/(v+1)). If b>=v/2 this follows by
comparability; otherwise the exponential gap absorbs the bounded low-b
factor. Since q=O(b), s_b=O(nv) and z_b=O(v^2+n),

 a_b 2^(-v/2)<=C[(v^2+n)sqrt(log2(v+2)/(v+1))
                                      +nv 2^(-v/2)].      (8.4)

Expand (5.2), use 1/sigma_b<=16/15 and (8.1)-(8.2), and sum over ALL
nominal levels. Every level is charged. Since d4(v)=2log2 v+O(1) and
v>=sqrt(B), eventual level separation is at least (log2 B)/2. Consequently

    sum v^(3/2)=O(B^(5/2)/l_B),
    sum v^(-1/2)=O(sqrt(B)/l_B).                           (8.5)

The first uses at most O(B/log B) levels. For the second, a decreasing
function at separated ordered points, except the lowest point, is at most
the integral over the preceding intervals divided by their separation.
This gives O(B^-1/4+sqrt(B)/log B), as required. Using n<=B^2, (8.4)
sums to O(B^(5/2)/sqrt(l_B)); its setup term is at most
O(n B^2 2^(-sqrt(B)/2)). It follows that

    Vmax=O(B^(5/2) l_B^(-1/2)2^(B/2)),
    Vcap=O(n B^(7/2) l_B^(-1/2)2^(B/2)),
    Qcap=O(n B^(3/2)2^((B-U)/2)).                         (8.6)

These bound the literal caps in Section 7. The guards, rather than a mean
bound alone, make them hold on every realized branch.

### 8.3 Explicit rational supported envelopes

d4 is nondecreasing. The intervals [max(U,v-d4(v)),v] cover [U,B]. Each
has length at most d4(B) and height at most v, so

    C4(B)=sum v >= (B^2-U^2)/(2d4(B)).                     (8.7)

For B>=64, f(B)+1<=2B: use f<=4q/7 and q<=B+ceil(log2(B+1))+7, or
the even coarser c<=B. Thus d4(B)<=2log2 B+3. Also U^2<=4B. Take
Btest=ceil((177/125)sqrt(nL)). For L>=16384, Btest<=n and Btest<=2sqrt(nL),
so 2d4(Btest)<=2L+2log2 L+10 and
Btest^2>=(31329/15625)nL. The rational gap is 79/15625. It obeys

    (79/15625)*16384 > 2*14+14,
    79/15625 > 4/16384.                                  (8.8)

The derivative of (79/15625)L-2log2 L-14 is positive thereafter, using
ln 2>1/2. Hence Btest^2-4Btest>=2n(L+log2 L+5): here
4Btest/n<=4 eventually, already at this threshold. Equations (8.7)-(8.8)
make Btest feasible, proving

    B<=ceil((177/125)sqrt(nL)).                            (8.9)

This is an analytic threshold proof. The algorithm never instantiates an
integer of 2^16384 bits merely to check it. Below that threshold there are
finitely many n, each with finite caps and a positive representative in
(T), so an absolute outer constant covers the finite prefix.

The increasing function (x-sqrt(x))/2 has derivative at most 1/2 for x>=1.
Using U>=sqrt(B), (8.9), and (118/100)^2<177/125 gives

    (B-U)/2 <= (177/250)sqrt(nL)
                    -(59/100)(nL)^(1/4)+1/2.              (8.10)

This is a sample-cap saving from the square-root base, not a new index.
The representative rational coefficients are retained from PPC deliberately.

### 8.4 Space, finite arithmetic and preprocessing

Depth-first evaluation retains at most two index qubits per finished child
and at most 1+sum(f(b_i)-1) unfinished sibling slots. Since f(b)<=5b and
sum b_i<=D-1, these require O(n) qubits. The active local operation can
hold all FOUR q-bit endpoints, the old-index cleanup workspace and predicate
scratch, still O(n). A source data register, control, extraction ancilla,
reversible transforms and arithmetic add O(n) qubits. S_Q=O(n).

Each live child stores at most four full labels of O(n) bits. All other
data are the q-bit endpoints, qubitization outcomes, low table entries,
profile, arithmetic words and decoder records. Their total is O(n^2)
classical bits. Neither an exponential incidence vector nor an exponential
circuit description is allocated. Gate descriptors are streamed.

For a concrete width justification, n>=256 and B<=n give
q0,Emax<=12B 2^(B/2)<2^n, so k0<=n. All actual b<=n and q<=2n.
Equation (3.7) gives h_b<2^(2n): the main exponent is at most n/2+10,
and the rare term is bounded even after discarding its denominator by
3(8ceil(log2(n+1))+18)ceil(log2(2n+2))2^n<2^(2n-1).
With w=1024(n+1), s_b,z_b<2^n and a_b<2^(4n). An ancestor product is
<2^n and there are at most n levels, giving Vmax<2^(6n).
K=2^13(k0+ceil(log2 n)+30), H0=nK+2n<2^n, so
Qcap<2^(3n), Vcap<2^(8n). Full labels, decoder frequencies, shifts,
search counters and extraction counters are well within w bits.

Rational certificate denominators divide

    product_(positive i) (8b_i+7)(q(b_i)+2)^16.             (8.11)

No large denominator is hidden by a floating-point log. Since
q(b)+2<=2(f(b)+1) and 8b+7<=16(f(b)+1),
the log of each factor is <=20+17log2(f(b)+1). Also

    sum_i log2(f(b_i)+1)
       <=log2(f(v_1)+1)+(B-v_1)/2 <=4n

for n>=256; inserting inactive nominal levels only increases this bound.
There are at most n levels, so the denominator has fewer than 89n+1 bits.
Value bounds above give numerator lengths below 100n+32. Rational
comparison cross-products are below 201n+64 bits. Thus w covers all
numerators, denominators, unreduced recurrence terms and cross-products;
use wider temporary multiples up to w and reduce after every step.
All exact recurrences, sequential B search, Euclid/CRT, maxima and cap
generation use O(n^6) charged work with schoolbook arithmetic. Iterate over
D rather than storing n full recurrences. Memory is O(n^2).

EXTRACT's precision parameter is h=O(B+log n)=O(n); it stores n+5 six-bit
directions and a few O(n)-bit counters. The decoder stores K=O(B) records
of O(n) bits. Its fixed trigonometric table is generated, not advice.
Therefore ell=O(log(n+2)), consistently with Section 1.

### 8.5 Source, decoder, base and root costs

All positive-node macros use O(ell^2 Vcap) charged work. The physical
source transform, EXTRACT, acquisition debit, base table construction and
associated frame operations cost O(n^3 ell^2) per physical copy. Every base
costs TWO such copies. The O(w) root-bit measurement and signed difference
cost is bounded by the same allowance: each constructed root consumes at
least one distinct physical copy. This covers rejected parity roots too.

Decoder scanning takes O(n^4 ell^2 q0), using at most n stages, K=O(B)
records and full signed-frequency arithmetic. Preprocessing takes O(n^6)
charged work. Cleanup of unfinished frames and an abort is polynomial.
Consequently a complete branchwise resource certificate is

    Cert4(n)=ceil(log2(n+2))^2
               [Vcap+n^3 Qcap+n^4 q0+n^6].               (8.12)

Total work is O(Cert4(n)). Since U>=sqrt(B)>=n^(1/4), source and decoder
terms in (8.12) have a factor 2^(-U/2) relative to 2^(B/2), beating every
polynomial overhead. Substitution of (8.6) gives (P). Finally
B=O(sqrt(nL)), log(B+2)=Theta(L), and (8.9)-(8.10) give exactly (T):
n B^(7/2)L^(-1/2)L^2=O(n^(11/4)L^(13/4)) and
nB^(3/2)=O(n^(7/4)L^(3/4)). All these bounds hold on wrong-label,
wrong-earlier-estimate, failure and abort branches because the actual
integer guards and fixed widths do not require correctness.

The dominant logarithm of both exponential representatives is a positive
multiple of sqrt(n log2 n), so their defined limsup growth index is 0.5.
The negative fourth-root sample term does not change it. Polynomial space
has index 0. An exponent coefficient or a finite fit is not a growth index.

## 9. A genuine same-base profile gain, without finite-fit extrapolation

PPC here means the ACTUAL submitted critical-profile square-root-base
algorithm, not PPSA or the older quarter-base configuration. Write
qP(v)=v+ceil(log2(v+1))+4 and dP(v)=ceil(log2((qP(v)+2)^2)).
Its capacity CP and F4's capacity C4 use the same U(B)=ceil(sqrt(B)).

### 9.1 Uniform smooth comparison despite nonmonotone capacities

For any profile with d(v)=2log2 v+O(1), uniformly for large B,

    C(B)=(B^2-U(B)^2)/(4log2 B)
                         +O(B^2/(log2 B)^2+B).            (9.1)

To prove this, bound d between 2log2 v+c_- and 2log2 v+c_+.
The functions f_c(x)=x/(2log2 x+c) are increasing for large x, with
derivative O(1/log x). On a descent interval [v-d(v),v], replacing its
integral by d(v)f_c(v) has error O(log v). There are O(B/log B)
intervals, so the aggregate error is O(B). The final truncated interval
and endpoint contribute O(B) too. Thus capacity lies between the two
smooth integrals from U to B with O(B) errors. Differentiating
x^2/(4log2 x) bounds each integral by its endpoint expression plus
O(B^2/log^2 B). For the error integral split below sqrt(B), then into
dyadic intervals above it. Since U=ceil(sqrt(B)), its lower endpoint term
is O(B/log B). This proves (9.1) with uniform errors, regardless of
ceiling jumps or downward capacity jumps.

For the first feasible trial it follows that

    B_PPC/sqrt(nL) ->sqrt(2),
    B_F4/sqrt(nL)  ->sqrt(2).                              (9.2)

Indeed C(c sqrt(nL))/n ->c^2/2 uniformly on compact positive c-ranges.
Every fixed c>sqrt(2) supplies a feasible integer trial, and the uniform
upper bound excludes every c<sqrt(2). No monotonicity is used.

The arity gives f(v)+1=(4/7)v+O(log v). More explicitly, eventually
f(v)+1<=(7/12)v, since 4/7<7/12 and the remaining term is O(log v).
Using ceil(x)<=x+1 and 2401/5184<1/2 gives

    d4(v)<=2log2 v-1/2,   dP(v)>=2log2 v.                 (9.3)

For example v>=4096 suffices for the first inequality: c<=v/128 there,
f+1<=4(v+c+7)/7+1<=4v/7+v/224+5<=(7/12)v. The bound on c follows
on each dyadic interval from 13<=4096/128 and preservation on doubling.

Define I_c(B)=integral_(sqrt(B))^B x/(2log2 x+c) dx.
The rectangle proof yields

    C4(B)>=I_(-1/2)(B)-O(B),
    CP(B)<=I_0(B)+O(B).                                   (9.4)

Here is the rectangle step explicitly. For F4, increasing f_(-1/2)
and (9.3) give

 integral_(v-d4(v))^v f_(-1/2)(x) dx
       <=d4(v) f_(-1/2)(v)<=v.

Summing covers [U,B]. For PPC, v<=dP(v)f_0(v); replacing that upper
rectangle by its integral loses O(log v), because f_0'=O(1/log v) and
dP(v)=O(log v). There are O(B/log B) intervals, so the total error is O(B).
The bottom overhang and replacing ceil(sqrt(B)) by sqrt(B) also cost O(B).
All retained v eventually exceed the fixed threshold in (9.3). On [B/2,B],

 I_(-1/2)(B)-I_0(B)
  >=(1/2) integral_(B/2)^B x dx/[4(log2 B)^2]
   =3B^2/[64(log2 B)^2].                                 (9.5)

Let B'=floor(B-B/(1000log2 B)). The derivative of I_(-1/2) is
f_(-1/2)(B)-f_(-1/2)(sqrt(B))/(2sqrt(B))<=B/log2 B eventually.
Monotonicity of x/log2 x bounds the lost integral by
B^2/[1000(log2 B)^2]+B/log2 B. Equation (9.5) dominates that loss
and both O(B) errors. Hence C4(B')>=CP(B) for all sufficiently large B.
Apply it to the actual least feasible B_PPC. Since CP(B_PPC)>=n,
B' is a feasible F4 trial. Sequential minimality proves (G), including
integer floors and every sufficiently large n, not just a subsequence.

### 9.2 What this proves about work, and what it does not

Use each algorithm's OWN literal caps, q0, source precision and profile in
the complete certificate (8.12), with CertPPC defined by the identical formula
from PPC Section 9.2. Both are polynomial times 2^(B/2) from above.
For PPC, TREE_n has full root width B_PPC eventually, and its positive
root certificate contains h_B>=2^(B/2)/sqrt(qP(B)). Thus
CertPPC>=2^(B_PPC/2)/poly(n). Equation (G) proves

    Cert4/CertPPC <=poly(n) 2^(-B_PPC/(2000log2 B_PPC)) ->0.       (9.6)

This comparison includes source extraction, decoder, all-D maxima and
preprocessing. It compares complete executed-parameter certificates, not
realized worst-branch costs. It is not inferred from the unchanged coarse
envelopes (T), which deliberately conceal this lower-order saving.

There is also a comparison of complete UNCAPPED ideal-label mean work.
For PPC's recovered pair search, on a nonsingleton fiber with z=m-1,
a trial of j iterations succeeds with probability at most 4(j+1)^2 z/A'.
Stopping at total query units h, sum the conditional bounds over trials;
sum(j+1)^2<=h^2, so success by h is at most 4h^2 z/A'. The full bounded
schedule succeeds with probability at least 3/4. Taking
h=(1/4)sqrt(A'/z) yields E H>=sqrt(A'/z)/8, with real h interpreted by
the integer cutoff. Uniformly A'>=2^qP/qP. Under PPC's planted moments,
Pr(0<Z<=2lambda)>=1/2-1/(1+lambda)>0 by Markov and the second-moment
singleton bound. Hence E H=Omega(2^(b/2)/sqrt(qP(b))). This averages
unconditionally and does not assume independence of pivots and fiber size.
These lower bounds concern only PPC's specified uncapped ideal-label
process. They are not general DCP lower bounds.

For all large moduli PPC must construct a root with full top width:
its first odd stage has D=floor(log2 N)>=n-1 if the odd part is nontrivial,
otherwise the first two-adic stage has D=n. These exceed B_PPC+1 eventually.
That root alone supplies mean work at least 2^(B_PPC/2)/poly(n).
F4's uncapped ideal-label total mean, charging its actual source routines
at the stipulated finite precision, is at most poly(n)2^(B_F4/2) by the
renewal analysis. Therefore the ratio tends to zero uniformly over N,s.
"Ideal-label" replaces extraction outputs by the true labels while still
charging extraction work; it is not a comparison between the two capped
noisy physical runs.

The leading limit remains 1/sqrt(2) for B/2 divided by sqrt(nL), so this
gain does not lower the growth index below 0.5. All fixed rational leading
coefficients above that limit can also be obtained for PPC by changing an
analytic threshold. Tightening such a coefficient alone is envelope slack,
not this algorithmic gain. Nor does (9.6) prove that F4's literal source cap
is smaller for every n. The finite source comparisons are reported with
their scope, separately from this analytic theorem.

## 10. Clean-input tolerance and status

The fifth claim uses exactly the following error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

epsilon(n)=0 permits zero malformed acquisitions. Sections 7-8 establish
unconditional success and all four branchwise bounds jointly under that
promise. Nothing here proves positive tolerance impossible.

The independent review and publication changes are documented in sources.md.
Bounded exact diagnostics check the finite identities and the
literal rational certificates, not a compiled quantum circuit or an all-N
theorem by enumeration. The proof above supplies the all-N argument.
Its supported representatives match PPC; no public frontier claim follows
from them. It does not assert an algorithm with growth index 0.49999 or a
hardness result excluding one.

## 11. Provenance

Exact source versions, reuse and unpublished inputs are recorded in sources.md.
