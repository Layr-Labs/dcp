# GCAP-B: boosted growing plateaus with collective high-confidence labels

## Definition and inherited circuits

For every N>=2, s in Z/NZ, n=ceil(log2 N), use the full source algorithm
in cs1_base.md with the changes specified in this document. That included
file is the unmodified CS1 proof at submission f1481815-9577-4990-abe3-7b79fa5d9284,
commit 200ef0387acb280adcd272f4fbcdb805d1786bbe. Its original resource
theorem and original tree parameters are replaced here, not asserted for
this configuration. All its source identities, exact data transformations,
phase-vector definitions, MERGE circuit, lookup implementation, top-bit
argument, odd-part candidate-grid decoder and 2-adic recovery instructions
are retained. The original finite exhaustive branch is used for n<64.

On every branch the joint envelopes are

    T=O(n^4 2^E), S_C=O(n^2 2^F), S_Q=O(n), Q=O(n^(3/2)2^E),
    E=a sqrt(n)+(3/5)n^(1/4),
    F=a sqrt(n)-(5/4)n^(3/8)+(3/5)n^(1/4).

Here a=u_333/v_333 is the exact Pell rational in cs1_base.md Section 0.
All constants are absolute. Recovery succeeds with probability at least
1-2^-8, jointly with the four bounds, under independent ideal source
copies. Epsilon(n)=0 is the malformed-copy tolerance. No claim of a
maximum possible tolerance is made.

## 1. Boosted schedule with a sharper depth allowance

For B=D-1>=1 define by exact integer arithmetic

    mu=ceil(sqrt(2B))+1,
    r=ceil(sqrt(mu)/2), U=mu+r,
    s=min(mu-1,floor(mu^(3/4))),
    kappa=ceil(log2 U)+1, x=ceil(log2(kappa+1)), ell=kappa+1+x,
    C(z)=z(z+1)/2-s(s-1)/2+x(z+1)+kappa,
    m=min{z>=s+1:C(z)>=B}.

The integer r is the smallest nonnegative integer with 4r^2>=mu.
The floor defining s is the largest v with v^4<=mu^3. Each leaf has ell
qubits. The tree lengths are

    lam_i=kappa+1+x+min(i,m-s) (i<m), lam_m=1.

Write t=m-s. The available residue-window lengths are

    bmax_i=x+i                 (0<=i<t),
    bmax_i=x+t+1               (t<=i<m-1),
    bmax_(m-1)=kappa+2x+2t+1.

Greedily allocate windows from the root down to total exactly B, as in the
included source. The LEAF table is the sum table of its ell leaf labels.
VEC is evaluated depth first, with failed inputs discarded as before.

Since s^2<=mu^(3/2) and 2mu r>=mu^(3/2),
U(U+1)-s(s-1)>=mu^2>=2B. Thus m<=U and the definition exists.
The exact sum of all bmax_i is C(m), and direct substitution gives
bmax_i+lam_(i+1)-2lam_i=-kappa in all three regimes. The distribution-free
proof in cs1_base.md Lemma 6.1 therefore gives conditional failure at most
2^-kappa<=1/(2U)<=1/(2m). In particular the capped schedules require no
unproved randomness property of the tables.

### Leaf-count certificate

For every B, nq_D=2^m ell <=16*2^U. This removes the old log n factor in
source acquisitions rather than concealing it in an exponential coefficient.

For mu<256, U<=264, kappa<=10, x<=4 and ell<=15<16. Since m<=U the bound
holds directly. For mu>=256 we have r>=x: indeed U<=2mu,
kappa<=log2(mu)+3, so

    x<=log2(log2(mu)+4)+1<= (1/2)log2(mu)+1<=sqrt(mu)/2.

The first middle inequality holds for z=log2(mu)>=8 because
log2(z+4)<=z/2 there, as follows at z=8 and by differentiation. The last
holds at mu=256 and its right-minus-left derivative is positive thereafter.
Also kappa>=x(x-1)/2: kappa>=2^(x-1), and 2^(x-1)>=x(x-1)/2 for x>=1,
by direct small cases and induction. Consequently

    C(U-x)=U(U+1)/2-s(s-1)/2+kappa-x(x-1)/2>=B.

Since U-x>=mu>=s+1, m<=U-x. Moreover ell<=2^(x+1), because
2^x>=kappa+1 and x<=2^x. Hence nq_D<=2^(U+1). This proves the
uniform factor-16 certificate. It also proves x+m-s<=U-s for mu>=256;
the finitely many smaller mu affect only an absolute constant in storage.

## 2. Collective high-confidence label extraction

This section REPLACES all of cs1_base.md Section 5, including its cheap
estimate, random verification and fallback cap. It uses the collective
translation construction from submission 844c0fd2-9b1c-4e84-a37c-f402e109985f,
but simply performs high-confidence level tests on every source copy.
No approximate Fourier transform, rotation synthesis or verification
fallback is used.

Set J_e=n+4 and h=ceil(log2(Qcap(n+5)))+20. Define F(h)=2^21 h,
using the same exact fixed trigonometric table as cs1_base.md Section 4.
For each of F(h) X rounds and F(h) Y rounds:

1. Prepare J_e+1=n+5 ancillas in |+>, viewed as the integer
   c=sum_(j=0)^J_e c_j 2^j.
2. Apply |c>|u> -> |c>|u-c mod N> for u<N, and the identity on u>=N,
   without changing c and with all arithmetic scratch cleared.
3. Measure each ancilla in the selected X or Y basis.

Circuit for step 2: copy c into an n+5-bit scratch register. Since
N>2^(n-1), c<2^(n+5)<64N. Reduce it modulo N by the six fixed
compare/conditional-subtract operations for 2^i N, i=5,...,0, retaining
the six quotient flags. On the valid data encodings, subtract the residue
modulo N, controlled on the valid-range flag. A register-valued ripple
subtract, conditional N add-back and uncomputation implement this in O(n)
Boolean/reversible gates and O(n) scratch. It is a permutation on valid
data and the identity on invalid data; the valid-range flag is cleared
because subtraction preserves the range. Reverse the reduction using its
flags and erase the copied c. The input register c is never changed.
All operations use NOT/CNOT/Toffoli, whose Clifford+T compilation is exact.

On chi_k, translations have eigenvalue omega^(kc), so the ancillas end in
exactly the product of (|0>+omega^(k 2^j)|1>)/sqrt2 for all j.
The data chi_k and spectators are unchanged. Conditional on the latent k,
all level outcomes and all rounds have precisely the independent-test law
used in cs1_base.md Section 5.1.

Decode the empirical X/Y means with the 64-direction table and the exact
halving/unwrapping routine of that section. Return the resulting integer
floor(Ng_0+1/2) mod N and reset the data register. The proof in that section
gives per-call error <=4(n+5)e^-h for every k. A union bound over at most
Qcap calls bounds any label error by 4(n+5)Qcap e^-h<=2^-18.
The ideal latent-label run and the actual run couple unless this event
occurs; no event depending on the label-test transcript is used elsewhere.

Every round costs O(n) core operations. Its accumulation counters have
O(log h)=O(log n) bits each. Total testing and counter cost is at most
O(n h log n)=O(n^(3/2)log n)=O(n^2), because h=O(sqrt n).
The exact unwrapping can be implemented conservatively with O(n)-bit
arithmetic at each of O(n) levels, costing O(n^2). The final rational
multiplication/rounding also costs O(n^2) by schoolbook arithmetic. Thus
this replacement LE has O(n^2) core work on EVERY call and O(n) quantum
scratch. Its classical counters and scratch are polynomial and are
included in the storage bound below.

## 3. Complete algorithm, cap and success

At B=n compute U*,kappa* above and

    NQ*=16*2^U*,
    K*=2^13(ceil(log2 NQ*)+ceil(log2 n)+30),
    Q*=6 NQ*(n K*+2a2)+2a2, Qcap=1024 Q*.

All are explicit integers. The odd-part decoder uses its original actual
nq_D and K in the grid and score; K<=K*. There are at most n stages.
When the odd part is 1, skip that decoder entirely. The 2-adic source
shifts and all decoder decisions are unchanged. Abort, release everything,
and return 0 before acquiring copy Qcap+1. All label calls use Section 2.

The retry multiplier obeys rt^m<=e<3 by the same inequality
m/(2^kappa-1)<=m/(2m-1)<=1. Each accepted leaf qubit uses at most 2
copies in expectation, so a successful tree uses at most 6 nq_D<=6 NQ*
copies in expectation. An odd W occurs with probability 1/2 in the 2-adic
part. Hence the ideal uncapped acquisition expectation is at most Q*.
Markov bounds source-cap failure by 2^-10.

The measured windows never exceed bit B-1. The low-label/top-bit
factorization, characteristic-function bound and odd-W probability in
cs1_base.md Section 8 therefore hold with these new schedules. They
establish exactly the decoder hypotheses in Sections 9--10 of that source.
The ideal odd-part error is at most 2^-20; conditional on its success,
the 2-adic part is exact. Coupling actual to ideal labels and adding the
cap event gives

    Pr[output=s]>=1-2^-20-2^-10-2^-18>1-2^-8.

The finite exhaustive branch has error <=2^-10. No conditioning on a
favorable label, cap or tree outcome is part of the success claim.

## 4. Uniform every-branch resources

Put z=sqrt(2n). For any B<=n, mu<=z+2 and
r<=sqrt(mu)/2+1. Thus U<=z+sqrt(z)/2+4. In particular, for
H=z+(1/2)sqrt(z), NQ*=O(2^H), kappa*=O(log n), and K*=O(sqrt n).
Therefore Qcap=O(n^(3/2)2^H) on every branch.

Transforms and the new LE cost O(n^2) core work per acquisition. A leaf
table has O(2^(kappa+x)) entries; its work per acquired leaf qubit is
O(n 2^(kappa+x)/ell)=O(n^(3/2)), since 2^x/ell<=2.
A level-i merge costs O(n(2^lam+2^lam')) and its inputs contain at least
2^(i+1)ell acquisitions. Its charge per acquisition is O(n^(3/2)).
At most O(sqrt n) such levels charge a given acquisition, because a failed
merge discards all its inputs. Total merge charge is O(n^2) per copy.
The decoder's fixed loops cost O(n^(5/2)NQ*) core steps, which is smaller
than O(n^2)Qcap. Polynomial setup is absorbed by the exponential. Hence

    core work=O(n^(7/2)2^H).

The depth-first stack still has O(n) qubits, plus O(n) collective-round
ancillas and arithmetic scratch reused on each call. All label high parts
have O(n) bits. The stacked tables use at most
O(n^(3/2)2^(kappa+x+m-s)) bits, with smaller merge scratch and polynomial
decoder/LE records. By the leaf-count certificate, x+m-s<=U-s+O(1)
uniformly, and 2^kappa=O(sqrt n). Thus

    S_C=O(n^2 max_(B<=n) 2^(U(B)-s(B)))+poly(n).

Since s>=mu^(3/4)-1,
U-s<=mu+(1/2)sqrt(mu)-mu^(3/4)+2. The function
f(v)=v+(1/2)sqrt(v)-v^(3/4) is increasing for v>=1, since its derivative
is at least 1/4. Evaluating it at z+2 and bounding the square root gives

    U-s<=z+(1/2)sqrt(z)-z^(3/4)+5.

Consequently

    S_C=O(n^2 2^(sqrt(2n)-(2n)^(3/8)+(1/2)(2n)^(1/4))).

These envelopes dominate polynomial scratch eventually; the finite
initial range only changes the outside constant. The address charge is
O(sqrt n), so total charged work is O(n^4 2^H), including (n+1)Qcap
source cost and uniform gate generation, arithmetic and measurements.

Finally a>sqrt2, 3/5>(1/2)2^(1/4), and 5/4<2^(3/8).
Termwise comparison gives exactly E,F in the introductory theorem.
Every exponential envelope has log2 B=a sqrt n+o(sqrt n), hence index
1/2, while n has index 0. All structured representations preserve these
exact coefficients and the polynomial prefactors; no inner big-O is
replaced by an invented coefficient.

## 5. Provenance and comparison

CS1 is the material source of the included circuits and recovery proof.
The growing plateau and mixed-power analysis are developed from GCAP.
The extra-leaf length x and its added x(m+1) capacity term are the leaf
boost used in CS1-LBQ, submission 603d96b1-a332-49a9-90ca-ef5cb6b8a5f2;
only that part is reused, not its QPE estimate. The collective translation
is from submission 844c0fd2-9b1c-4e84-a37c-f402e109985f; the present
algorithm uses it for direct high-confidence extraction rather than that
source's verified cheap estimate/fallback combination. Its public note
credits an earlier collective-phase-estimation construction; no additional
code was fetched from that indirect source. All inherited arguments used
here are reproduced in this proof snapshot.

Compared with GCAP, this configuration halves the explicitly retained
n^(1/4) overhead coefficient, removes a logarithm from source acquisitions
by leaf boosting, and removes both logarithms from total work by combining
that boost with collective label tests. The n^(3/8) memory saving remains.
It is a rigorous time/space tradeoff at index 1/2, not the 1/3 research goal.
