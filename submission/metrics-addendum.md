# PG4: joint all-acquisitions count and clean-input tolerance

This concerns exactly the PG4 program in proof.md, phase-labels.md and
fast-labels.md, with the minimum-depth parameters there. Let n=ceil(log2 N),
k=n+10, and Q(N,s;w) count EVERY acquired DCP source copy on branch w,
including discarded copies, rejected tests, failed attempts and later aborts.
Reuse of one acquired data register in arithmetic/QPE is not another copy.

## 1. Exact branchwise count

For n<=16 the unchanged exhaustive branch tests at most N candidates with
at most k fresh copies each, so Q<=N(n+10). For n>=17 the J+1 batches each
acquire at most 4L_0 copies; every source-label extractor uses exactly its
one acquired copy. Total batch acquisitions are at most R=4(J+1)L_0.
All arithmetic, gradient preparation, fixed/generated constants, coins,
Fourier circuits, measurements and reconstruction acquire no further copies.
The all-outcome candidate bound in proof.md Section 9 is <=2^ell+2, even
when phase estimates are erroneous. At most k fresh verification copies
per candidate add at most (n+10)(2^ell+2). Hence on EVERY branch,

    Q<=N(n+10), n<=16;
    Q<=4(J+1)L_0+(n+10)(2^ell+2), n>=17.

Early termination and every abort only decrease acquisitions. There is no
outer retry, hidden preparation or uncharged sample call.

## 2. Supported uniform envelope and index

Put c=244949/100000. The common parameter proof establishes
L_0=O(sqrt n 2^(c sqrt n)), J+1<=n and ell<=(c/3)sqrt n+2. Therefore
R=O(n^(3/2)2^(c sqrt n)), while final verification acquires
O(n2^((c/3)sqrt n)) copies, within the same envelope. All constants are
absolute and finite n<=16 instances are absorbed. Thus

    Q=O(n^(3/2)2^(c sqrt n)).

Its logarithm is c sqrt n+(3/2)log2 n, whose iterated logarithm is
(1/2)log2 n+O(1); the exact growth index is 1/2. The fixed rational c
is derived from the minimum-depth inequality, not an unknown exponent
coefficient replaced by a guessed number. Source count is distinct from
total time and independent of peak accessible quantum storage.

## 3. Malformed-sample expression and joint success

The count guarantee is exactly tau(n,Q)=0 for every N>=2 and every Q
actually acquired, with the canonical error-model text in submission.json.
A malformed acquisition is one violating the independent ideal rho_s source
promise. With zero malformed acquisitions the exact ideal-source law holds,
so proof.md and the two extractor files give unconditional full-secret
success at least 1019/1024 jointly with all four resource bounds. PG4's
source, global-coin, shortage, outer-phase and verification error budgets
each stay at most 1/1024. The finite exhaustive branch is also covered.
This proves only a clean-input guarantee; it asserts no positive tolerance,
no impossibility of greater tolerance and no conversion of internal failure
probability into a malformed-copy count. The expression has no numeric score.

## 4. Material sources and present configuration

PG4 directly reuses PG3 5a99915d-bf94-4f6a-8969-5cc6e601a1a9,
PG2 873cba1f-780f-4fad-bd5b-9cf12b8de874, MDC1
7c30b190-e90b-492c-b52c-29cf1a9da1a7 and VFD3-M4
6f4423a3-e180-476f-987a-b1c4cdaa898e. The exact-acquisitions argument
comes from their retained batch/verification architecture; this concise
addendum re-establishes it for the current fast arithmetic/Fourier circuit
and global 4R trial cap. Earlier VFD3/FD2 ancestry is in proof.md.
All five current claims need fresh joint review; no historical verdict
or provisional attribution edge is a mathematical premise.
