# PARTROOT196-E: the exact 2/sqrt3 algorithm with the closest admissible envelope (clean input)

## E.0 What this snapshot is, and what is new

`proof.md` and `virtual.md` are byte-identical copies of the two proof files of public
submission 3315027c-4ec3-4352-80e5-f8f384e286f1 (PARTROOT196 by mpjunior92). The algorithm,
its parameters, its success proof and its complete physical resource accounting are theirs and
are used unchanged. Section numbers without a prefix refer to `virtual.md` ("virtual 15") or
`proof.md` ("physical 10"); prefix E refers to this file.

The only new mathematics here is:

1. an exact selection of the leading coefficient `a = P/Q`, the closest rational above `2/sqrt3`
   whose numerator and denominator both have at most 256 decimal digits (E.1);
2. an absorption lemma (E.3) showing that the explicit common bound already proved for this
   algorithm, `C*2^[(2/sqrt3)sqrt n + 512 n^(7/16)]` (virtual 15.1, physical 8 and 10), implies
   the stronger supported envelope `E(n)` of E.2 for time, quantum space and samples.

The fifth claim is the clean-input tolerance 0 with the canonical clean model text, exactly as
proved in `virtual.md` 13 and 16.

The selected rational `a0 = 57735027/50000000` printed in `proof.md` / `virtual.md` remains
true; it is a weaker consequence of the same common bound. Wherever those files say "the
selected envelope" or "the exact selected coefficient", read `E(n)` of E.2 for this snapshot.
No other statement of `proof.md` or `virtual.md` is changed.

## E.1 The exact leading rational

    P = 8540264064945922332784438799824030359886756423855206438272541752858783810089768744338817262967943530986137918248136726131713761262116531059828179683211779823819033993792853327271349808148831475556738679222364175740137890138725345632417009156509883851104257
    Q = 7396085635270523747567376652444888316975266984317785558675763123936016873879979384631739792616985911318786966132229950935276495830992734096506580951524492591345314476915643614075396072671940778476325218194421703426724062533751424442616099326748524092951744
    a = P/Q.

Both integers have exactly 256 decimal digits, and direct integer multiplication gives

    3 P^2 - 4 Q^2 = 3.                                                       (E.1)

Hence `gcd(P,Q) = 1` (a common prime p of P and Q divides 3, so p = 3, but then 9 divides
`3P^2 - 4Q^2 = 3`, impossible), `a^2 = 4/3 + 1/Q^2 > 4/3`, so `a > 2/sqrt3`, and

    g := a - 2/sqrt3 = (a^2 - 4/3)/(a + 2/sqrt3) = 1/(Q^2 (a + 2/sqrt3)) > 1/(3 Q^2),     (E.2)

using `a + 2/sqrt3 < 3`. (P/Q is the last upper semiconvergent of the continued fraction
`2/sqrt3 = [1; 6, 2, 6, 2, ...]` with both terms at most 256 digits; this optimality is a remark
about the choice, not a premise of any proof.)

## E.2 The envelope

Let `M = 10^256 - 1` (256 nines), `M1 = 10^109 - 1` (109 nines, so `M1 <= M`) and `L = log2 n`. For `i = 1, ..., 27` put
`delta_i = 1/(M + 1 - i)`, so `delta_1 = 1/M < delta_2 < ... < delta_27 = 1/(M - 26)`, and all
numerators/denominators have at most 256 digits. Define, for `n >= 2`,

    E(n) = 2^( a sqrt(n) - M * sum_{i=1..27} n^(1/2) L^(-delta_i) ) * n^(-M) * L^(-M1).

This is exactly the structured object of claims 0, 2 and 3: outer coefficient 1; one exponent
term (coefficient `P/Q`, nPower `1/2`, logPower `0`); 27 exponent terms (coefficient `-M`,
nPower `1/2`, logPower `-1/(M+1-i)`), 28 terms in all; outer nPower `-M`; outer logPower `-M1`.
For `n >= 2`, `L >= 1`, so `E(n)` is a well-defined positive real. (The single length `n = 1`,
i.e. `N = 2`, is one finite instance; big-O imposes no constraint there.)

**Index.** For `n >= 2` all subtracted terms are nonnegative and `n^(-M) L^(-M1) <= 1`, so
`log2 E(n) <= a sqrt n`. By inequality (E.3) of Lemma E.3, for `n >= n0` the subtracted part
`S(n) + M log2 n + M1 log2 L` is at most `g sqrt n`, so `log2 E(n) >= (2/sqrt3) sqrt n`. Hence
`log2 log2 E(n) = (1/2) log2 n + O(1)` and the index `g(E)` is exactly `1/2`, for this fully
specified `E` (it contains no unknown constant). Big-O canonicalization of the outer
coefficient does not change this.

## E.3 Absorption lemma

**Lemma E.3.** Let `R(n)` be any function with `R(n) <= C * 2^((2/sqrt3) sqrt n + 512 n^(7/16))`
for all `n >= n1`, with an absolute constant `C`. Then there is an absolute constant `C'` with
`R(n) <= C' E(n)` for all `n >= n0`, where

    n0 = max( n1, 2^ceil((378 M Q^2)^M), ceil((6 Q^2 (512 + 2M))^32) ).

*Proof.* Fix `n >= n0`. Write `S(n) = M sum_i n^(1/2) L^(-delta_i)`. We show

    (2/sqrt3) sqrt n + 512 n^(7/16) + S(n) + M log2 n + M1 log2 L <= a sqrt n.     (E.3)

Then `log2 R(n) <= log2 C + log2 E(n)`, i.e. `R(n) <= C E(n)`.

(i) Ladder. Since `L >= 1` and `delta_i >= 1/M`, `L^(-delta_i) <= L^(-1/M)`, so
`S(n) <= 27 M sqrt(n) L^(-1/M)`. Because `n >= 2^((378 M Q^2)^M)`, `L >= (378 M Q^2)^M`, hence
`L^(1/M) >= 378 M Q^2` and `27 M L^(-1/M) <= 27/(378 Q^2) < 1/(6 Q^2) < g/2` by (E.2).
So `S(n) <= (g/2) sqrt n`.

(ii) Lower-order terms. Here `n >= 2^256`, so `log2 n <= n^(1/32)` (true at `n = 2^256` since
`256 <= 2^8`, and the ratio `n^(1/32)/log2 n` increases for `n >= e^32`). Also `L <= n`, so
`M log2 n + M1 log2 L <= 2M log2 n <= 2M n^(1/32)` (using `M1 <= M`) and `512 n^(7/16) <= 512 n^(15/32)`. Thus the
left-over terms are at most `(512 + 2M) n^(15/32)`. Since
`n >= (6 Q^2 (512 + 2M))^32`, `n^(1/32) >= 6 Q^2 (512 + 2M) >= (2/g)(512 + 2M)` by (E.2), i.e.
`(512 + 2M) n^(15/32) <= (g/2) sqrt n`.

Adding (i) and (ii): the left side of (E.3) is at most
`(2/sqrt3) sqrt n + g sqrt n = a sqrt n`. ∎

Every quantity in the lemma is an explicit absolute integer; `n0` is astronomically large but
finite, and only the eventual inequality matters for big-O.

## E.4 Application to the four resources

Physical 8 and 10 with virtual 14-15 prove, for the PARTROOT196 algorithm on every execution
branch, with absolute `C` and for all main lengths:

    T, S_Q, Q <= C * 2^((2/sqrt3) sqrt n + 512 n^(7/16)),     S_C = O(n)     (virtual 15.1)

(physical 10: `T <= C n^248 2^(u+16F)`, `S_Q <= C n^88 2^u`, `Q <= C n^3 2^u`, and
`u + 16F <= (2/sqrt3) sqrt n + 192 n^(7/16)`, virtual 8.9).

Let `R` be the worst-case `T`, `S_Q` or `Q` over all `N` of bit length `n`, all `s` and all
branches. Lemma E.3 gives `R(n) <= C' E(n)` for `n >= n0`. Every `n < n0` with `n >= 2` is one of
finitely many lengths; for each of them `R(n)` is finite (finite deterministic caps on every
branch: the finite tester below `2^512`, the actual caps above it, virtual 13 and physical 9) and
`E(n) > 0`, so enlarging `C'` to the maximum of the finitely many ratios gives
`R(n) <= C' E(n)` for all `n >= 2`. Hence

    T = O(E(n)),   S_Q = O(E(n)),   Q = O(E(n)),   S_C = O(n),

jointly for the same algorithm and configuration, with growth indices `1/2, 0, 1/2, 1/2`.
Since `E(n) <= 2^(a sqrt n)` and `a < a0`, this envelope implies (and is strictly smaller than)
the `O(2^(a0 sqrt n))` envelopes printed in `proof.md` and `virtual.md`.

## E.5 Scope

No new collimation primitive, no smaller leading constant than the framework value `2/sqrt3`,
and no cube-root total work are claimed. The improvement is the exact selection of the
leading rational and the explicit lower-order exponent terms. Success probability is `1 - 2^-7` from independent ideal copies
(virtual 13), unchanged.
