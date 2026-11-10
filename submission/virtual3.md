# Reference algorithm P for IFC-BANK-D, part 3: the seven-input dissection merge MERGE7 and its failure bound

This file is part of the complete specification and proof of IFC-LIMIT-D, the reference algorithm P of proof.md; the
other parts are virtual.md and virtual2.md. "P Section x" and "P (x.y)" refer to virtual.md, and Sections 7.3, 8, 9, A
and B are in virtual2.md. Sections C and D are new in IFC-LIMIT-D (e-man07). MERGE7 is used only at the Phase M levels
of the schedule (P Section 8). In Sections C and D, L = 2^lam is the input length, and b is the number of label bits
that one MERGE7 collimates.

The listing in step 2 is the dissection algorithm of Dinur, Dunkelman, Keller and Shamir (CRYPTO 2012) for seven
lists: it guesses the residue of a three-list sum on 2 lam bits, and for each guess it joins a stored three-list class
with a streamed Schroeppel-Shamir four-list. Here it lists one measured class of a seven-input collimation, in time
O(L^4) up to polynomial factors and with O(L) stored rows. Every step is specified and proved below; no external result is a premise.

## C. MERGE7(X1, ..., X7; p, b, lam')

Precondition. X1, ..., X7 are phase vectors from pairwise disjoint sets of copies, each of length L = 2^lam and
collimated to p, with index registers x1, ..., x7. Write lab_t[x] = c_t + 2^p h_t[x] with 0 <= c_t < 2^p, as
collimation allows. Require lam >= kappa + 2 (kappa as in P Section 0), lam' >= 1 and b = 7 lam - lam' - kappa >= 2 lam.
Put a_t[x] = h_t[x] mod 2^b, car = floor((c_1 + ... + c_7)/2^p), mu7 = 2^(lam' + kappa), Cp = 8 mu7 + 1 and
Cq = 2 L + 1. A TUPLE is (x1, ..., x7) in [0, L)^7.

Window identity. For a tuple with S = lab_1[x1] + ... + lab_7[x7], S = (c_1 + ... + c_7) + 2^p (h_1 + ... + h_7) and
0 <= (c_1 + ... + c_7) mod 2^p < 2^p, so floor(S/2^p) = car + h_1 + ... + h_7. Hence bits p..p+b-1 of S are
(car + a_1 + ... + a_7) mod 2^b.                                                                              (C.1)

Residue classes (functions of the input tables only). For g in [0, 2^(2 lam)) let T3(g) be the list of the triples
(x1, x2, x3) with (a_1 + a_2 + a_3) mod 2^(2 lam) = g, in lexicographic order and cut to its first Cq entries. For h
in [0, 2^lam) let P45(h) be the list of the pairs (x4, x5) with (a_4 + a_5) mod 2^lam = h, in lexicographic order and
cut to its first Cq entries, and define P67(h) from (x6, x7) in the same way. A triple, a (4,5)-pair or a (6,7)-pair
is DROPPED if it is not in the list of its own class. A tuple is KEPT if none of its triple (x1, x2, x3), its pair
(x4, x5) and its pair (x6, x7) is dropped.

1. LOOKUP h_t mod 2^b into fresh registers (t = 1..7), add them and car modulo 2^b cleanly into a fresh b-qubit
   register Rw, clear the seven lookup registers by repeating the lookups, measure Rw (outcome v') and reset it. By
   (C.1) v' is bits p..p+b-1 of S. Put T = (v' - car) mod 2^b and Z = {tuples with (a_1 + ... + a_7) mod 2^b = T},
   sz = |Z|, and let Zk be the set of kept tuples of Z.
2. Listing (classical). Stably sort the x3 by a_3 mod 2^(2 lam), and the x5 and the x7 by a_5 mod 2^lam and
   a_7 mod 2^lam. Start with an empty list Tl. For g = 0, 1, ..., 2^(2 lam) - 1 in order:
   (a) Build T3(g): for (x1, x2) in lexicographic order, find by binary search the run of the x3 with
       a_3 = (g - a_1 - a_2) mod 2^(2 lam), which lists them in increasing x3, and append (x1, x2, x3) for each x3 of
       the run, stopping as soon as Cq triples are listed. This is the lexicographic order, so the list is T3(g).
       Store with each triple its key A = (a_1 + a_2 + a_3) mod 2^b, and stably sort the list by A.
   (b) Put t4 = (T - g) mod 2^(2 lam). For h = 0, 1, ..., 2^lam - 1 in order: build P45(h) as in (a) (for x4 in
       increasing order, the run of the x5 with a_5 = (h - a_4) mod 2^lam, stopping at Cq pairs), and P67(h2) with
       h2 = (t4 - h) mod 2^lam likewise; stably sort P45(h) by (a_4 + a_5) mod 2^(2 lam). For each (x6, x7) of
       P67(h2) in order, find by binary search the run of P45(h) with (a_4 + a_5) mod 2^(2 lam) =
       (t4 - a_6 - a_7) mod 2^(2 lam); for each (x4, x5) of that run in order, find by binary search the run of T3(g)
       with A = (T - a_4 - a_5 - a_6 - a_7) mod 2^b, and append to Tl the tuple (x1, ..., x7) for each triple
       (x1, x2, x3) of that run in order.
   Stop the listing as soon as |Tl| = Cp. Let tl = |Tl|.
   Claim C.1. The entries of Tl are distinct elements of Zk, and tl = min(|Zk|, Cp).
   Proof. Let a tuple be appended at (g, h). Its triple lies in T3(g), so (a_1 + a_2 + a_3) mod 2^(2 lam) = g and the
   triple is not dropped. Its pair (x4, x5) lies in P45(h), so it has class h and is not dropped. Its pair (x6, x7)
   lies in P67(h2), so it has class h2 and is not dropped. Its key condition gives
   (a_1 + a_2 + a_3) + (a_4 + a_5 + a_6 + a_7) = T modulo 2^b, so the tuple is in Z; hence it is in Zk. The pair
   (g, h) is fixed by the tuple (g is the class of its triple, h that of its pair (x4, x5)). At that (g, h) the
   tuple is appended at most once: each list has distinct entries, and a tuple is appended only from its own
   (x6, x7) entry, its own (x4, x5) entry in that entry's run, and its own triple in the run found for that pair.
   So the entries are distinct. Conversely let a tuple of Zk be given, with triple class g and (4,5)-class h. Since
   b >= 2 lam, (a_4 + a_5 + a_6 + a_7) mod 2^(2 lam) = (T - g) mod 2^(2 lam) = t4 at this g, so the (6,7)-class of
   the tuple is (t4 - h) mod 2^lam = h2. Its three parts are not dropped, so (x6, x7) is in P67(h2), (x4, x5) is in
   the run of P45(h) searched for (x6, x7), and the triple is in the run of T3(g) searched for (x4, x5). So the tuple
   is appended unless the listing stopped before. Hence if the listing does not stop, Tl lists Zk, and tl = |Zk| <= Cp
   (if |Zk| = Cp the listing stops at the last append, with the same Tl). If it stops, then tl = Cp, and
   |Zk| >= Cp because the entries of Tl are distinct elements of Zk. QED.
   Nothing before the measurement of v' depends on a label bit at a position >= p: step 1 is the first step, and
   its measurement law is fixed by Lemma C.2 below.
3-6. (These are MERGE4I's steps 5-8, Section A, with seven index registers.) (3) R has ceil(log2(Cp + 1)) bits and
   Rf one qubit, both 0. For each row rho of Tl compute [(x1, ..., x7) = Tl[rho]] with a Toffoli chain on O(lam)
   scratch, CNOT it into Rf and onto the bits of R where rho has a 1, and uncompute. Rows are distinct, so R = rho
   and Rf = 1 on the tuples of Tl, and R = Rf = 0 elsewhere. Measure Rf; if Rf = 0 declare FAIL. (4) Measure
   bl = floor(R/2^lam'); if (bl + 1) 2^lam' > tl declare FAIL. (5) For y in [0, 2^lam'), LOOKUP y -> Tl[bl 2^lam' + y]
   on the low lam' bits of R, XORing into x1, ..., x7, which become |0>; reset them, Rf and the high bits of R from
   known values. (6) Output the low lam' bits of R as the index register, with lab[y] the sum of the seven input
   labels of Tl[bl 2^lam' + y], stored in full (P Section 6). Every such tuple is in Z, so by (C.1) every lab[y] is
   congruent to c' = c_1 + ... + c_7 - car 2^p + 2^p v' modulo 2^(p+b).

On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers and arrays
have fixed sizes, set by L, b, lam' and kappa.

Correctness (ideal run). Before step 1 the state is the product of the inputs: equal magnitudes over the L^7 tuples,
with phases 2 pi (sum of the seven labels) th. Steps 1, 3 and 4 compute functions of the tuple into clean registers
and measure them; step 2 acts on nothing in this state. After step 4 the state is therefore the equal-magnitude
superposition over the 2^lam' tuples of block bl of Tl, with their original phases, and step 5 maps each to its y
bijectively. The output is a phase vector with table lab, collimated to p + b, since every label is congruent to c'
modulo 2^(p+b).

Lemma C.2 (failure identity). For ANY input tables collimated to p, the laws of the measurements of steps 1, 3 and 4
depend only on label bits below p + b, and with sz = sz(v') and tl = tl(v'),

    Pr[FAIL] = sum_(v') [ (sz - tl) + (tl mod 2^lam') ] / L^7.

Moreover sz - tl <= (sz - |Zk|) + (sz - Cp)_+, and the terms (tl mod 2^lam') sum to less than 2^(b + lam')/L^7 = 2^(-kappa).

Proof. Each measurement is a computational-basis measurement of a function of the tuple on an equal-magnitude
superposition, so its law is a ratio of counts, independent of phases. The outcome v' has probability sz/L^7, and Z,
Zk, Tl and tl are functions of the a_t, that is, of label bits below p + b. Given v', the state is equal-magnitude on
Z, and Rf = 1 exactly on the tl tuples of Tl, which lie in Z by Claim C.1; so Rf = 0 has probability (sz - tl)/sz.
Given Rf = 1, R is uniform on [0, tl), and step 4 fails with probability (tl mod 2^lam')/tl. Multiplying and summing
gives the identity. By Claim C.1, if |Zk| <= Cp then sz - tl = sz - |Zk|, and otherwise sz - tl = sz - Cp. There are
2^b values v', and tl mod 2^lam' < 2^lam'. QED.

Cost on every branch. Step 1: 14 lookup passes of L rows with O(lam + b)-bit fields and O(b)-bit additions. Step 2:
three sorts of L rows. For each g: L^2 binary searches and at most Cq appends for T3(g), and a sort of at most Cq rows.
For each (g, h): 2L binary searches and at most 2 Cq appends for P45(h) and P67(h2), a sort of at most Cq rows, and at
most Cq binary searches into P45(h). Over all g and h this is O(2^(2 lam) (L^2 + 2^lam L)) = O(L^4) searches and
appends. Each (x4, x5) read in a run, together with the current (x6, x7), is a four-tuple (x4, x5, x6, x7) whose
four-sum is congruent to t4 modulo 2^(2 lam), and the pair (g, h) is then fixed by t4 = (T - g) mod 2^(2 lam) and the
(4,5)-class h. So each four-tuple is read at most once in the whole listing: there are at most L^4 such reads, each
followed by one binary search into T3(g). Appends to Tl number at most Cp. So step 2 is O(L^4 lam) comparisons and
moves of O(lam + b)-bit keys, whatever the labels. Steps 3-6: one pass of tl <= Cp rows with O(lam) control bits, one
lookup pass of 2^lam' rows, and 2^lam' additions of 3n-bit labels. Total O(L^4 lam (lam + b) + Cp lam + 2^lam' (lam + n))
core steps. Quantum scratch: O(lam + b) qubits beyond the seven index registers (the seven lookup registers, Rw, R, Rf
and Toffoli-chain scratch, fewer than 32 registers). Classical scratch: the three sort orders (L rows each), T3(g),
P45(h) and P67(h2) (at most Cq rows each, with O(lam + b)-bit keys), Tl (at most Cp rows of 7 lam bits) and the block
table (2^lam' rows), so at most 3 L + 3 Cq + Cp + 2^lam' rows of fixed size, freed at the end of the merge.

## D. Failure bound for MERGE7 on pool-output leaves

Lemma D.1. In the ideal run, consider a MERGE7 attempt at Phase M level k of a batch, with p its start position,
lam = Lam, lam' = Lam (or 1 at the root) and b = 7 Lam - lam' - kappa (P Section 8). Let Hp be the sigma-field defined
as in Lemma B.1 with the seven inputs of the attempt in place of four: generated by everything that happened before
its step 1 that a controller decision can read, except the label bits at positions >= p of the leaves of its seven
inputs. (So Hp contains the bits below p of those labels; the FW and PREP outcomes; the merge, MERGE4I and MERGE7
outcomes with their counts, runs and lists; the coins and the controller decisions of all earlier steps; and
everything on other copies. As in Lemma B.1 it does not contain LE's internal coins and test outcomes on the copies of
these leaves, nor root outcomes of the current batch.) Then

    Pr[FAIL | Hp] <= 3 * 2^(-lam) + 2^(-kappa - lam') + 2^(-kappa) < 2^(2 - kappa).

Proof. LEAVES are as in Lemma B.1: a leaf qubit of the supplier with label k_j uniform on [0, 2^(B+1)), or a phantom
qubit of Lemma 9.1 with label 2^(pp_ell) u_j and u_j uniform. By the incidence paragraph of P Section 10, every table
entry of the seven inputs is the sum of the labels over a 0/1 incidence set of leaves, distinct entries of one table
have distinct incidence sets, and the seven inputs use pairwise disjoint sets of leaves. Let Lv be the set of leaves
of the seven inputs. For j in Lv write k_j = lo_j + 2^p z_j + 2^(p+b) u_j with 0 <= lo_j < 2^p and 0 <= z_j < 2^b. This
is possible as p + b <= B (P Section 8), and since p >= pp_ell the digits z_j are uniform and independent of each
other and of lo_j, also for phantoms.

Factorization. This is the factorization paragraph of Lemma B.1, word for word, with "the seven inputs" in place of
"the four inputs", with Lemma C.2 next to Lemma A.1 among the lemmas whose laws, keys, residues, sort keys, counts,
ranks, lists and block choices read only label bits below p, and with the merges, MERGE4Is and MERGE7s at lower levels
(p' + b' <= p) among the earlier steps. Every earlier step that involves a leaf of Lv lies in the subtree of the
attempt or in the FW stage below it, so it reads only label bits below p, and bits below p of a sum of leaf labels
depend only on the lo_j. Hence, conditional on Hp, the z_j (j in Lv) are i.i.d. uniform on [0, 2^b).

Residues. An entry x of input t has label sum_(j in I_t(x)) k_j, so
a_t[x] = (f_t(x) + sum_(j in I_t(x)) z_j) mod 2^b with f_t(x) = floor((sum_(j in I_t(x)) lo_j)/2^p), which is
Hp-measurable. For a triple, a pair or a tuple e, the residue of its sum of a_t modulo 2^s, for s <= b, is
(f(e) + sum_(j in I(e)) z_j) mod 2^s, where I(e) is the disjoint union of the incidence sets of its parts and f(e) is
Hp-measurable. Distinct triples (pairs, tuples) have distinct incidence sets, since the parts come from tables on
disjoint leaves and distinct entries of one table have distinct incidence sets; so at most one triple (one pair of
each kind, one tuple) has an empty incidence set. The pairwise-independence paragraph of Lemma B.1 applies with
H = Hp and the z_j mod 2^s: for a count S of the elements with nonempty incidence set and a fixed residue,
Var[S | Hp] <= E[S | Hp].

Lost tuples. By Lemma C.2, sz - tl <= (sz - |Zk|) + (sz - Cp)_+. The sets Z(v') over the 2^b outcomes v' partition the
L^7 tuples, so sum_(v') (sz - |Zk|) is the number of tuples that are not kept, whatever v' is. Fix g and let S_g count
the triples with nonempty incidence set and class g. Then E[S_g | Hp] <= L^3/2^(2 lam) = L. The class has at most
S_g + 1 triples, so at most (S_g + 1 - Cq)_+ = (S_g - 2L)_+ of them are dropped. If S_g > 2L then
D = S_g - E[S_g | Hp] > L and S_g - 2L < D <= D^2/L. So E[(S_g - 2L)_+ | Hp] <= Var[S_g | Hp]/L <= 1, and the expected
number of dropped triples is at most 2^(2 lam). In the same way, with classes modulo 2^lam, E <= L^2/2^lam = L per
class and the same cap Cq = 2L + 1, the expected numbers of dropped (4,5)-pairs and of dropped (6,7)-pairs are at most
2^lam each. A dropped triple lies in L^4 tuples and a dropped pair in L^5. So

    E[ sum_(v') (sz - |Zk|) | Hp ] / L^7 <= (2^(2 lam) L^4 + 2 * 2^lam L^5)/L^7 = 3 * 2^(-lam).

Overflow. Fix v' and let S' count the tuples with nonempty incidence set and (a_1 + ... + a_7) mod 2^b = T. Then
E[S' | Hp] <= L^7/2^b = mu7, sz <= S' + 1 and Cp = 8 mu7 + 1, so (sz - Cp)_+ <= (S' - 8 mu7)_+. If S' > 8 mu7 then
D' = S' - E[S' | Hp] > 7 mu7 and S' - 8 mu7 < D' <= D'^2/(7 mu7), so E[(sz - Cp)_+ | Hp] <= Var[S' | Hp]/(7 mu7) <= 1.
Summing over the 2^b outcomes gives at most 2^b/L^7 = 2^(-kappa - lam') after division by L^7.

Summing. Take E[. | Hp] of the identity of Lemma C.2. The lost, overflow and block terms are at most 3 * 2^(-lam),
2^(-kappa - lam') and 2^(-kappa). As lam >= kappa + 2 and lam' >= 1, the total is at most
(3/4 + 1/2 + 1) 2^(-kappa) < 2^(2 - kappa). QED.

The bound conditions on no outcome of the attempt itself: the only measurement before the listing is that of v', and
the listing reads it only through the count identity of Lemma C.2. It holds for every attempt, retries included, since
a retry uses fresh pool qubits whose leaves are not in any earlier attempt's input. It is used in P Lemma 9.1 exactly
as Lemma B.1 is, with seven inputs per attempt.
