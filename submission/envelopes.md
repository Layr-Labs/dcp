# envelopes.md: supported classical-space and sample envelopes E_b

This file is part of the proof of the CS1-WINDOW-P-MIN-E configuration in
proof.md and uses only its proved raw bounds and Section 14 inequality (14.1).
It replaces the declared memory/sample envelope 2^(b sqrt n) of the source
public submission 61a4271c-b434-409b-b475-f19aa0b78380 by a smaller envelope E_b with the same leading term.

## E1. Definition

Let b = C/D be the exact rational of proof.md Section 14 and beta =
sqrt(2+4/P^2) - sqrt(2)/P with P = u_333. By (14.1), delta_b = b - beta > 0.
Let

    K = 10^256 - 1  (256 nines),   J = 10^58 - 1  (58 nines),
    d_i = 10^256 - i for i = 1, ..., 28  (so d_1 = K > ... > d_28 > 0),
    k_i = K for i = 1, ..., 27,  k_28 = J  (so 1 <= k_i <= K),

and for integers n >= 2, with L = log2 n >= 1,

    E_b(n) = 2^( b sqrt(n) - sum_(i=1..28) k_i n^(1/2) L^(-1/d_i) ).

The structured objects of claims 1 and 3 list E_b exactly: outer
coefficient 1, outer nPower 0, outer logPower 0, the exponent term
(coefficient b, nPower 1/2, logPower 0), and for i = 1, ..., 28 the term
(coefficient -k_i, nPower 1/2, logPower -1/d_i).

## E2. Lemma (absorption)

For every fixed real p >= 0, n^p 2^(beta sqrt(n)) = O(E_b(n)).

Proof. For n >= 2,

    log2( n^p 2^(beta sqrt n) / E_b(n) )
      = -delta_b sqrt(n) + sqrt(n) sum_i k_i L^(-1/d_i) + p log2 n.

Every 1/d_i >= 1/K, every k_i <= K and L >= 1, so k_i L^(-1/d_i) <= K L^(-1/K).
Let L_0 = (56 K/delta_b)^K. For L >= L_0, L^(1/K) >= 56K/delta_b and so
sqrt(n) sum_i k_i L^(-1/d_i) <= 28 K L^(-1/K) sqrt(n) <= (delta_b/2) sqrt(n).
The logarithm is then at most -(delta_b/2) sqrt(n) + p log2 n -> -infinity.
Hence the ratio tends to 0, is bounded for large n, and finitely many smaller
n contribute a finite maximum. QED. The threshold is astronomically large;
only its existence is used. All constants are independent of N, s and
outcomes.

## E3. Application

proof.md Sections 0, 13 and 14 prove S_C = O(n^20 2^(beta sqrt n)) and
Q = O(n^20 2^(beta sqrt n)) on every execution branch, and Sections 11.1
and 13 extend both to the heralded model of the fifth claim with the fixed
absolute D. Lemma E2 with p = 20 gives S_C = O(E_b) and Q = O(E_b) on every
branch, jointly with the unchanged time envelope E, S_Q = O(n), and recovery
probability at least 1 - 2^-8.

## E4. Growth index

Each sqrt(n) L^(-1/d_i) is o(sqrt n), so log2 E_b(n) = (b + o(1)) sqrt(n) and
log2 log2 E_b(n) = (1/2) log2 n + log2 b + o(1). The exact growth index is 1/2.

E_b is a comparator-ordered restatement of the same raw bounds; it adds no
algorithmic content. Its leading coefficient b is unchanged.
