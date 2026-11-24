# Taller final tree with a smaller source pool

This file replaces the PCROOT-1 main-branch schedule of virtual.md
Section 8 and its instantiations in the setup of base-bank.md Section 2.
Use the same profile in every capped pool or tree operation. The rest
of those procedures, the compiler and the logical decoder run exactly
as described in the attached source manuscripts at these parameters.

## 1. Exact parameter rule

At $n\ge2^{512}$ write $r=\lceil\sqrt n\rceil$ and
$L_n=\lceil\log_2n\rceil$. Use
$$
 \ell=\lceil127r/256\rceil,\qquad
 m=d_l=\lceil159r/256\rceil,\qquad
 \kappa=\lceil\log_2m\rceil+1.
$$
The root, ceilings and width calculations use only integer comparisons,
bit lengths and divisions. The same integer $k$, the least odd integer
at least $\lceil n^{1/3}\rceil$, and all quantities of the odd-cell
compiler of virtual.md Section 7 stay unchanged. Write $q$ for its
exact rational consumption-to-output ratio, with
$1<\log_2q\le1+7n^{-1/6}$. In particular $q>2$. Put
$$
 K=8192(2r+L_n+30),\qquad
 C_\ell=4096nK\,2^m d_l,\qquad
 C_i=\left\lceil\frac{q\ell C_{i+1}}{\ell-1}\right\rceil
 \quad(i=\ell-1,\ldots,0).
$$
Compute $Y=\lceil\log_2C_0\rceil$, $L_{\rm try}=Y+L_n+64$,
$u=\max(Y,m+d_l)+2$, and $U=2^u$. The initial ordinary controller
performs the rolling cap computation without storing its array,
using a constant number of $O(n)$-bit words and the same compiler
preprocessing as base-bank.md. After allocating its counted bank,
recompute and retain the schedule in that bank. This avoids any
extra ordinary memory. The actual source cap in the main proof is
still $C=4nC_0+K$ in logical requests.

For pool level $0\le i<\ell$ let $b^{\rm pool}_i$ be the largest integer
$b\ge0$ with $2^b 2(k+1)\ell\le C_i$. For the tree use phase-size
profile $\lambda_i=d_l+i$ for $0\le i<m$ and $\lambda_m=1$.
Its windows are
$$
 b^{\rm tree}_i=d_l+i-\kappa-1\quad(0\le i<m-1),\qquad
 b^{\rm tree}_{m-1}=2(d_l+m-1)-\kappa-1.
$$
For the desired $1\le B\le n$, allocate the actual bits in the same
greedy order as virtual.md Section 8. Use the pool widths in ascending
index and the tree widths in descending index, each at most that slot's
maximum and the number of bits still needed. Then form the prefix sums,
and use the unchanged tree and pool instruments. The cutoff only runs
the finite branch of the current main proof at $n<2^{512}$.

## 2. Cap identities and width conditions

Let $\rho=q\ell/(\ell-1)>2$. The ceiling recurrence gives
$$
 q^{\ell-i}C_\ell\le C_i,\qquad
 C_0\le \rho^\ell(C_\ell+1)\le8q^\ell C_\ell,\qquad
 \sum_{i=0}^\ell C_i\le2C_0.
$$
The middle inequality uses the geometric sum of ceiling errors
and $(1-1/\ell)^{-\ell}\le4$. From $n\le r^2$, $d_l\le r$ and
$K\le2^{15}r$ one obtains
$$
 Y\le \ell\log_2q+m+4\log_2 r+31 .
$$
At the stated cutoff $r\ge2^{256}$,
$127r/256\le\ell\le r/2$ and
$159r/256\le m=d_l\le5r/8$. These follow directly from the ceilings.
The identities $L_n\le2\log_2r+1$ and $\log_2 q<9/8$ imply
$Y\le2r$, $L_{\rm try}\le4r$ and $Y+1\le6\ell$. For example
$Y$ is at most $19r/16+4\log_2r+31$, which is below $2r-1$
at the cutoff and thereafter since the derivative of the linear
surplus after the logarithm stays positive. The estimate for
$K$ follows from $L_n+30\le2r$. Likewise $\ell^2<n$ because
$n>(r-1)^2>(r/2)^2$.

The tree has $2^\kappa\ge2m$ and $d_l\ge\kappa+1$, so every
window is nonnegative. Any admitted window $b$ at child level $i$
satisfies $b+\lambda_{i+1}-2\lambda_i\le-\kappa$ required by
the merge failure lemma. Also $m\ge20+8\log_2 r+4$ and
$2^m\ge2(k+1)\ell$. Both hold at $r=2^{256}$ with increasing
margin, using $k\le2n^{1/3}\le2r^{2/3}$ and the lower linear
bound for $m$. It follows that $C_i\ge2^m\ge2^{20}n^4$,
and every pool width is defined. The bank bound
$u+512+100L_n<n$ still holds from $u\le2r+2$,
$n>(r-1)^2$, and $L_n\le2\log_2r+1$. The bank uses
$C_0\le 2^Y\le U/4$ and $d_l+m\le u-2$, independently
of whether $\ell=m$.

## 3. Capacity for all cancellation bits

Maximality and the cap lower bound imply
$$
 b^{\rm pool}_i>
 \log_2 C_i-\log_2(4(k+1)\ell)
 \ \ge\ \ell-i+m-\log_2(4(k+1)\ell).
$$
The sum over pool levels is therefore at least
$\ell^2/2+\ell m-\ell\log_2(4(k+1)\ell)$.
Summing the exact tree windows gives
$m d_l+m^2/2+d_l+m/2-1-m(\kappa+1)$.
Discard the nonnegative term $d_l+m/2-1$.
The remaining positive pool-and-tree terms satisfy
$$
 \frac{(\ell+m)^2}{2}+m d_l
 \ \ge\ \frac{66179}{65536}\,r^2
 =\left(1+\frac{643}{65536}\right)r^2 .
$$
The two subtractions are bounded by $r(3\log_2r+20)$:
$\log_2(4(k+1)\ell)<(5/3)\log_2r+4$ and
$\kappa+1\le\log_2r+3$, with $\ell,m\le r$.
At $r=2^{256}$,
$(643/65536)r>3\log_2r+20$, and the difference grows
thereafter. Hence the sum of usable windows is at least $r^2\ge n$.
The greedy rule always reaches exactly $B$ and only reads low bits
below the allocated cut, as required by the unchanged incidence and
top-bit argument.

## 4. Preserved correctness and separate asymptotic bounds

The pool yield and identity caps depend on the inequalities
$2^b 2(k+1)\ell\le C_i$, $\ell^2\le n$, $Y+1\le6\ell$,
$Y\le2r$ and $C_i\ge2^m$, now proved above. The original
Hoeffding calculation, conditional stopped yield, and total
number of batches therefore give their original error
bounds. The exact final-pool cap is the one needed by
virtual.md Lemma 9.1, $4096nK2^m d_l$, and $2^\kappa\ge2m$.
The pool-exhaustion bound and the full-modulus stage proof
thus remain valid. No argument requires $\ell=m$ beyond the
overridden old capacity comparison. The hard raw source and
program nontermination guards remain actual, including on
inaccurate labels.

As $n$ grows, the displayed bound on $Y$ gives
$$
 Y\le (143/128)\sqrt n+O(n^{1/3}),\qquad
 m+d_l\le(159/128)\sqrt n+O(1),\qquad
 u\le(159/128)\sqrt n+O(n^{1/3}).
$$
For the first, $\ell+m=143r/128+O(1)$,
$7\ell n^{-1/6}=O(n^{1/3})$, and
$\log r=O(n^{1/3})$. The next two follow from the integer
schedule and the strict leading gaps.

The resource counting in virtual.md Section 14 continues
to hold with $U=2^u$ and $m,d_l$ as above:
pool processing is polynomial times $\sum C_i=O(C_0)$.
The tree work is $O(n C_\ell2^{d_l})=
O(n^3 2^{m+d_l})$ by the distinct-descendant charge, and
the number of stages is at most $n$. Table capacities,
stored compiler history and measured bank and controller
overhead remain bounded by fixed polynomials times $U$.
All derived bank dimensions are computed with the new $u$
and $U$. Setup and control keep a constant number of
$O(n)$-bit current words. The paired source wrapper's raw
label bank is counted, with only $O(n)$ ordinary staging.

Logical acquisitions use the tighter separate cap
$4nC_0+K=O(n\,2^Y)$, even when $u$ is larger.
For the paired wrapper the gap decreases with length, and its
lower odd probability decreases as well, and the hard repetition
cap satisfies $2P=O(n2^{3r/512})$. So branchwise
source use is $O(n^2 2^{Y+3r/512})$. Counting one additional bank
of $O(wn)$ qubits and every extra source operation changes the
paired storage and work to a polynomial times the bigger of
$2^u$ and $2^{Y+3r/512}$. In both cases $159/128$ is the larger
leading coefficient. The source leading coefficient is $575/512$.
The positive gaps to $5/4$ and $9/8$ absorb the respective
subleading terms.
