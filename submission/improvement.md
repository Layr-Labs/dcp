# PCROOT-1 integration certificate and exact scope

This file connects the complete virtual algorithm in virtual.md, the exact
instrument in odd_partition.md, and the physical realization in proof.md.
Those files supply the underlying arguments, rather than relying on any
previous review decision. The direct material sources are PARTROOT196
(3315027c-4ec3-4352-80e5-f8f384e286f1) and ODDPOLY1322876
(e6fb060b-cab8-4a37-83aa-a98b50bde141). Their constructions are credited in
the files and dependency declaration. Their historical acceptance is not a
mathematical hypothesis here.

## 1. One algorithm and the change being proved

For every N>=2, n=ceil(log2 N), and unknown s in Z/NZ, use independent
copies of the stated mixed coset source. The only quantum primitives are
Clifford+T, computational-basis measurements, fresh zero qubits, and this
source. All indexing, bit operations, gate generation, source costs and
allocated memory are charged as in the protected rules. No source inverse,
coherent source control, preloaded circuit, or quantum memory oracle is used.

At n<2^512 use the finite exhaustive tester in virtual.md 13. Otherwise:

* k is the least odd integer at least the integer cube-root ceiling of n.
* z0 is the least integer with 3z0^2>=n; z=z0+16ceil(log2 n).
* ell=m=dl=z, kappa=ceil(log2 z)+1, and
  K=8192(2ceil(sqrt n)+ceil(log2 n)+30).
* Set C_ell=4096nK2^z z and recursively
  C_i=ceil(q ell C_(i+1)/(ell-1)), where q is the exact rational
  expected LIVE cost divided by expected GOOD output of the odd-cell
  instrument. Set Y=ceil(log2 C0), u=max(Y,2z)+2, U=2^u.
* Use the greedy bit windows, capped pools, capped identity retries,
  source cap 4nC0+K, and full-modulus decoder specified in virtual.md.
* Execute the polynomial rank/unrank circuit of odd_partition.md, compiled
  once into counted storage after physical bank allocation. Execute the
  entire classical virtual controller through proof.md's measured-basis
  bank; retain only a constant number of O(n)-bit ordinary working words.

The group-size choice, compiler and all caps are fixed as part of this one
algorithm. No resource claim uses a separately optimized configuration.

The change replaces exhaustive truth-function circuit generation with the
already known direct token-ranking construction, and permits increasing k
from the root parent's eighth-root rule to the cube-root rule. It is an
integration of credited techniques, not a claim to have invented either
technique. It improves the explicit subleading upper-bound allowance in
this proof from n^(7/16) to n^(1/3), with the same leading term
(2/sqrt3)sqrt n. It does not prove a lower bound on the predecessor's actual
runtime or a strict runtime separation. The selected rational structured
envelopes and numerical time index are unchanged.

## 2. Why substituting the compiler preserves the instrument

For odd k, h=(k-1)/2 and w=1/[h(h+1)], use A cells with a single unequal
pair and weight w, and J_j cells with j disjoint unequal pairs and an
all-equal remainder, with weight
w_j=(1-wj(k-j))(k-2j)!/(k-j)!, 0<=j<h.
For a basis string with minority size t, there are t(k-t) containing A
cells and, when t<h, exactly (k-t)!/(k-2t)! containing J_t cells.
These weighted multiplicities sum to one, including t=h and t=0.

The helper enumerates only tokens containing the current basis input:
A cells by a minority/majority pair, J cells by an injection of minority
positions into distinct majority positions. Canonical cell encodings are
independent of that input. Integer copy multiplicities and identity tokens
make exactly M tokens per basis input, with M a power of two. The two
reversible XOR functions are mutual rank/unrank inverses on this set.
After clearing the rank and measuring the token, each cell token has Kraus
operator Pi_cell/sqrt(M). Each identity token has I/sqrt(M). Conditional
on nonidentity, the cell Kraus weights are exactly the displayed w,w_j.
Thus the equality holds on arbitrary joint states with arbitrary
references, not merely on computational-basis inputs.

Only the arbitrary names/order of tokens differ from exhaustive compilation.
Group cleanup, output order and the canonical pivot remain those specified
in virtual.md. All remaining control decisions use the decoded cell and
low difference keys. For product equatorial phase inputs, every token's
probability depends only on the cell size; it is independent of all phases
and labels. This preserves the full product invariant and the low-field
factorization of virtual.md 10. Extra physical bank measurements are
marginalized by its decoded classical/quantum invariant; the argument
never conditions on high-label arithmetic traces.

## 3. Larger groups fit all probability and capacity estimates

The all-odd-k calculation in odd_partition.md 7.1 gives
2<q<=2+7/sqrt(k). Here n^(1/3)<=k<=2n^(1/3), hence
log2(q)<=1+7n^(-1/6). The fixed number of pool rounds contracts LIVE
to at most (k-1)2^c leftovers; concentration is uniform in all label
values and uses a union bound over every possible stopped prefix.

In particular, the concentration denominator is at most
2^13 k^3 ell^2 <= 2^16 n^2, because ell^2<n and k^3<=8n.
The root schedule has C_i>=2^m and 2^m>=2^20 n^4. Thus virtual.md
7.6 and 9.2 retain the required exponentially small pool-yield failure.
This is the relevant concentration check for the changed group size;
one cannot keep the old k-dependent bounds without checking it.

The slot-size loss in virtual.md 8 is also rechecked: with r=ceil(sqrt n),
k<=2r^(2/3), and z<=r,
log2[4(k+1)z]<(5/3)log2 r+4. Together with kappa+1<=log2 r+3,
the negative window terms are at most r(3log2 r+20).
The added 16ceil(log2 n) in z gives surplus at least
r((93/2)ceil(log2 n)-23)>2r. The combined pool/tree capacity is
therefore at least r^2>=n at every main-branch length.

Identity retries have exact, input-independent probability R/M<1/4 of
leaving the state unchanged. Each macro has at most Ltry=Y+ceil(log2 n)+64
trials, there are at most 2nC0 macro starts, and total retry-cap error
is at most 2^-128. Trials consume no new source samples. Other failures
are the unchanged LE coupling, capped supplier and tree exhaustion, and
full-secret decoding events. Their explicit union bound in virtual.md 13
is below 2^-8 on the main branch; the finite branch errs by at most
2^-10. The common declared success 1-2^-7 is conservative.

## 4. Compilation, workspace and physical work

Let t=log2 n>=512, b=ceil(log2 k), W=8k^2(b+1), and
T0=2^128(k+1)^64(b+1)^64. The helper's fixed-loop schoolbook arithmetic,
full scans for data-dependent indices, explicit Boolean unrolling and
stored-history reversible conversion give at most T0 gates and T0 private
wires. They include both rank functions and clean uncomputation. The
stored circuit and its generation cost O(T0^2).

The inequalities W<=32n^(2/3)t<=n and
log2 T0<=(64/3)t+256+64log2 t<32t hold at t=512 and have increasing
slack. Therefore the coherent history fits n^32 wires and the generated
circuit and construction tape fit O(n^64) bits/work. This is not an
assertion of O(W) reversible history.

The preallocation pass computes exact k,D,q and rolling C_i using only
constant-many O(n)-bit words. Factorials, rational sums and denominator
lcm are streamed; their common denominators can be bounded by products
of O(k) factorials and h(h+1)2^k, hence O(k^2 log k) bits. The circuit
is generated only after the bank is initialized. Its arrays use fixed
owner roles and O(n^64) records, not one owner per generated gate.
Proof.md's R=2^128 n^64 U row capacity and H=2^96 n^64 U unknown-wire
capacity include this entire setup, private history, maps and padding.

The virtual cost is conservatively O(n^70 U). The counted interpreter
has ordinary S_C=O(n), full allocated S_Q=O(n^88 U), and eventual
T=O(n^160(n^70 U+n^88 U))=O(n^248 U). Epoch wrap is handled by an
exact finite renumbering on every branch; the proof shows it cannot occur
eventually, while finitely many exceptional lengths change only an
outside constant. Source acquisitions are one-for-one with virtual
requests, so Q<=4nC0+K. These are all-branch bounds, not expected costs.

## 5. The explicit improvement and admitted representation

The backward recurrence and new rate give
u<=(2/sqrt3)sqrt n+64n^(1/3). Absorbing n^248 and the smaller factors
using log2 n<=n^(1/3) yields jointly

    T, S_Q, Q <= C 2^[(2/sqrt3)sqrt n+512n^(1/3)],
    S_C <= C n,

for an absolute constant C, with any finite exceptions absorbed outside.
Let c=57735027/50000000, an exact rational with 3c^2>4, and put
epsilon=(3c^2-4)/(12c)>0. Then c-2/sqrt3>2epsilon and, for
n>=(512/epsilon)^6, 512n^(1/3)<=epsilon sqrt n. Consequently the
selected supported bound is O(2^(c sqrt n)) for T,S_Q,Q, jointly.
It has growth index 1/2; the linear classical envelope has index zero.
No irrational coefficient is put in a structured object.

The fifth declaration is the fractional guarantee 0 under the exact
independent ideal-copy model stated in the manifest. It is not a claim
that positive tolerance is impossible. All algorithms, including the
finite fallback, terminate with their fixed caps on every source outcome.

The proof does not establish 2^{O(n^(1/3))} total work, a smaller time
index, a new leading constant, global novelty, or frontier dominance.
It is an asymptotic construction with an enormous cutoff, not a practical
implementation. Local finite arithmetic diagnostics do not certify the
infinite theorem; hosted mathematical review remains necessary.
