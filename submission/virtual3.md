# Reference algorithm P for IFC-BANK-D, part 3: the fibered seven-input dissection merge MERGE7 and its failure bound

This file is part of the complete specification and proof of IFC-LIMIT-D, the reference algorithm P of proof.md; the
other parts are virtual.md and virtual2.md. "P Section x" and "P (x.y)" refer to virtual.md, and Sections 7.3, 8, 9, A
and B are in virtual2.md. Sections C and D are new in IFC-LIMIT-D (e-man07). MERGE7 is used only at the Phase M levels
of the schedule (P Section 8). In Sections C and D, L = 2^lam is the input length, w is the FIBER WIDTH of the merge and
b is the number of label bits that one MERGE7 collimates.

The structure follows MERGE4I (Section A), with TRIPLES (x1, x2, x3) in place of the pairs (x1, x2) and FOUR-TUPLES
(x4, ..., x7) in place of the pairs (x3, x4). The w-bit window W0 of each side is measured first. Then the next window
W1 of the seven-label sum is measured, and the measured class is listed by the dissection algorithm of Dinur,
Dunkelman, Keller and Shamir (CRYPTO 2012) for seven lists. That algorithm guesses the residue of the three-list sum on
2 lam bits, and for each guess it joins a stored class of triples with a streamed Schroeppel-Shamir four-list. Because
W0 is measured, only 2^(2 lam - w) guesses are needed, and the listing takes O(2^(4 lam - w)) steps up to polynomial
factors. The case w = 0 has empty W0. Every step is specified and proved below; no external result is a premise.

## C. MERGE7(X1, ..., X7; p, w, b, lam')

Precondition. X1, ..., X7 are phase vectors from pairwise disjoint sets of copies, each of length L = 2^lam and
collimated to p, with index registers x1, ..., x7. Write lab_t[x] = c_t + 2^p h_t[x] with 0 <= c_t < 2^p, as
collimation allows. Require:
- lam >= kappa + 2 (kappa as in P Section 0);
- 0 <= w <= 2 lam and lam' >= 1;
- b = 7 lam - lam' - kappa - w, and b' = b - w >= 2 lam.

Put a_t[x] = h_t[x] mod 2^b, and define the carries
- cA = floor((c_1 + c_2 + c_3)/2^p), cB = floor((c_4 + ... + c_7)/2^p),
- cq = floor(((c_1 + c_2 + c_3) mod 2^p + (c_4 + ... + c_7) mod 2^p)/2^p) in {0, 1},
- car = cA + cB + cq = floor((c_1 + ... + c_7)/2^p).

For a triple x = (x1, x2, x3) put A(x) = (cA + a_1 + a_2 + a_3) mod 2^b. For a four-tuple y = (x4, ..., x7) put
By(y) = (cB + a_4 + a_5 + a_6 + a_7) mod 2^b. Put mX = L^3/2^w, mY = L^4/2^w, mu7 = 2^(lam' + kappa),
Cp = 8 mu7 + 1 and Cq = 2 L + 1. A TUPLE is a pair (x, y) of a triple and a four-tuple.

Window identity. For a tuple let S = lab_1[x1] + ... + lab_7[x7]. Then floor(S/2^p) = car + h_1 + ... + h_7, as
0 <= (c_1 + ... + c_7) mod 2^p < 2^p and car = cA + cB + cq. Hence bits p..p+b-1 of S are
(A(x) + By(y) + cq) mod 2^b.                                                                                   (C.1)

Residue classes (functions of the input tables only).
- For g in [0, 2^(2 lam)), T3(g) is the list of the triples x with A(x) mod 2^(2 lam) = g, in lexicographic order,
  cut to its first Cq entries.
- For h in [0, 2^lam), P45(h) is the list of the pairs (x4, x5) with (a_4 + a_5) mod 2^lam = h, in lexicographic
  order, cut to its first Cq entries. P67(h) is defined in the same way from the pairs (x6, x7) with
  (cB + a_6 + a_7) mod 2^lam = h.
- A triple, a (4,5)-pair or a (6,7)-pair is DROPPED if it is not in the list of its own class. A tuple is KEPT if
  none of its triple, its pair (x4, x5) and its pair (x6, x7) is dropped.

1. LOOKUP h_t mod 2^w (t = 1, 2, 3), add them and cA modulo 2^w cleanly into a fresh w-qubit register Rz, clear the
   lookups by repeating them, measure Rz (outcome v) and reset it. Do the same on x4, ..., x7 with cB (outcome v2).
   Let the fibers X_v = {triples with A(x) mod 2^w = v} and Y_v2 = {four-tuples with By(y) mod 2^w = v2}. If w = 0
   this step measures nothing: v = v2 = 0, X_0 has all L^3 triples and Y_0 all L^4 four-tuples.
2. LOOKUP h_t mod 2^b (t = 1..7), add them and car modulo 2^b cleanly into a fresh b-qubit register Rw, clear the
   lookups, CNOT bits w..b-1 of Rw into a fresh b'-qubit register Ru, and uncompute Rw. By (C.1), Ru holds bits
   p+w..p+b-1 of S. Measure Ru (outcome v') and reset it. On X_v x Y_v2, bits p..p+w-1 of S are (v + v2 + cq) mod 2^w
   by (C.1). So put E = ((v + v2 + cq) mod 2^w) + 2^w v' and T = (E - cq) mod 2^b. Let Z be the set of tuples of
   X_v x Y_v2 with (A(x) + By(y)) mod 2^b = T, that is, with bits p..p+b-1 of S equal to E. Put sz = |Z|, and let Zk
   be the set of kept tuples of Z.
3. Listing (classical). Stably sort the x3 by a_3 mod 2^(2 lam), and the x5 and the x7 by a_5 mod 2^lam and
   a_7 mod 2^lam. Start with an empty list Tl and a read counter rd = 0. For the 2^(2 lam - w) values g in
   [0, 2^(2 lam)) with g mod 2^w = v, in increasing order:
   (a) Build T3(g). For (x1, x2) in lexicographic order, find by binary search the run of the x3 with
       a_3 mod 2^(2 lam) = (g - cA - a_1 - a_2) mod 2^(2 lam), which lists them in increasing x3. Append the triple
       for each x3 of the run, stopping as soon as Cq triples are listed. This is the lexicographic order, so the list
       is T3(g). Store with each triple its key A(x), and stably sort the list by A.
   (b) Put t4 = (T - g) mod 2^(2 lam). For h = 0, 1, ..., 2^lam - 1 in order:
       - build P45(h) as in (a): for x4 in increasing order, take the run of the x5 with
         a_5 mod 2^lam = (h - a_4) mod 2^lam, stopping at Cq pairs;
       - build P67(h2) likewise with h2 = (t4 - h) mod 2^lam;
       - stably sort P45(h) by (a_4 + a_5) mod 2^(2 lam);
       - for each (x6, x7) of P67(h2) in order, find by binary search the run of P45(h) with
         (a_4 + a_5) mod 2^(2 lam) = (t4 - cB - a_6 - a_7) mod 2^(2 lam);
       - for each (x4, x5) of that run in order, increase rd by one, and if rd > 2 mY declare FAIL. Otherwise find
         by binary search the run of T3(g) with A = (T - By(x4, ..., x7)) mod 2^b, and append to Tl the tuple of
         each triple of that run, in order.
   Stop the listing as soon as |Tl| = Cp. Let tl = |Tl|.
   Claim C.1. The entries of Tl are distinct elements of Zk. Every four-tuple counted in rd is a kept-pair
   four-tuple of Y_v2, counted once. If step 3 does not FAIL, tl = min(|Zk|, Cp).
   Proof.
   - Membership. Let a tuple be appended at (g, h). Its triple lies in T3(g), so A mod 2^(2 lam) = g, and it is not
     dropped. Its pair (x4, x5) lies in P45(h) and its pair (x6, x7) in P67(h2), so neither is dropped. Its key
     condition gives A + By = T modulo 2^b. As g = v and T = v + v2 modulo 2^w, also By = v2 modulo 2^w. So the
     tuple is in X_v x Y_v2 and in Z, hence in Zk.
   - Reads. A four-tuple read at (g, h) has By = t4 modulo 2^(2 lam), and h is the class of its pair (x4, x5). So
     g = (T - By) mod 2^(2 lam) and h are fixed by the four-tuple. At that (g, h) it is read at most once: each list
     has distinct entries, and the four-tuple is reached only from its own (x6, x7) entry and its own (x4, x5) entry
     in that entry's run. Its two pairs are in their lists, so they are kept, and By = v2 modulo 2^w as above, so it
     is in Y_v2. Since every tuple is appended only after the read of its four-tuple, and once from that read for
     its own triple, the entries of Tl are distinct.
   - Completeness. Let a tuple of Zk be given, with triple class g and (4,5)-class h. Then g mod 2^w = A mod 2^w = v.
     As b >= 2 lam, By mod 2^(2 lam) = (T - g) mod 2^(2 lam) = t4 at this g, so the (6,7)-class of the tuple is
     (t4 - h) mod 2^lam = h2. Its three parts are not dropped, so (x6, x7) is in P67(h2), (x4, x5) is in the run of
     P45(h) searched for it, and the triple is in the run of T3(g) searched for (x4, x5). So the tuple is appended
     unless the listing stopped or failed before. Hence, without FAIL: if the listing does not stop, Tl lists Zk and
     tl = |Zk| <= Cp; if it stops, tl = Cp <= |Zk|.
   QED. In particular, if |Y_v2| <= 2 mY then rd <= |Y_v2| <= 2 mY and step 3 does not FAIL.
4-7. (These are MERGE4I's steps 5-8, Section A, with seven index registers.)
   (4) R has ceil(log2(Cp + 1)) bits and Rf one qubit, both 0. For each row rho of Tl, compute
       [(x1, ..., x7) = Tl[rho]] with a Toffoli chain on O(lam) scratch, CNOT it into Rf and onto the bits of R where
       rho has a 1, and uncompute. Rows are distinct, so R = rho and Rf = 1 on the tuples of Tl, and R = Rf = 0
       elsewhere. Measure Rf; if Rf = 0 declare FAIL.
   (5) Measure bl = floor(R/2^lam'); if (bl + 1) 2^lam' > tl declare FAIL.
   (6) For y in [0, 2^lam'), LOOKUP y -> Tl[bl 2^lam' + y] on the low lam' bits of R, XORing into x1, ..., x7, which
       become |0>; reset them, Rf and the high bits of R from known values.
   (7) Output the low lam' bits of R as the index register, with lab[y] the sum of the seven input labels of
       Tl[bl 2^lam' + y], stored in full (P Section 6). Every such tuple is in Z, so by (C.1) every lab[y] is
       congruent to c' = c_1 + ... + c_7 - car 2^p + 2^p E modulo 2^(p+b).

On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers and arrays
have fixed sizes, set by L, w, b, lam' and kappa.

Correctness (ideal run). Before step 1 the state is the product of the inputs: equal magnitudes over the L^7 tuples,
with phases 2 pi (sum of the seven labels) th. Steps 1, 2, 4 and 5 compute functions of the tuple into clean
registers and measure them, and step 3 acts on nothing in this state. So after step 5 the state is the
equal-magnitude superposition over the 2^lam' tuples of block bl of Tl, with their original phases, and step 6 maps
each to its y bijectively. The output is a phase vector with table lab, collimated to p + b, since every label is
congruent to c' modulo 2^(p+b).

Lemma C.2 (failure bound for fixed tables). For ANY input tables collimated to p:
- the laws of the measurements of steps 1, 2, 4 and 5 depend only on label bits below p + b;
- (v, v2) has probability |X_v| |Y_v2|/L^7;
- given (v, v2) with |Y_v2| <= 2 mY,

    Pr[FAIL | v, v2] = sum_(v') [ (sz - tl) + (tl mod 2^lam') ] / (|X_v| |Y_v2|),

  with sz = sz(v, v2, v') and tl = tl(v, v2, v'). Moreover sz - tl <= (sz - |Zk|) + (sz - Cp)_+.

Proof. Each measurement is a computational-basis measurement of a function of the tuple on an equal-magnitude
superposition, so its law is a ratio of counts, independent of phases. All sets and lists above are functions of the
a_t, that is, of label bits below p + b. Step 1's two measurements act on disjoint registers, so (v, v2) has
probability |X_v| |Y_v2|/L^7. Given (v, v2), v' has probability sz/(|X_v| |Y_v2|). If |Y_v2| <= 2 mY, step 3 does not
FAIL (Claim C.1). Given v', the state is equal-magnitude on Z, and Rf = 1 exactly on the tl tuples of Tl, which lie in Z;
so Rf = 0 has probability (sz - tl)/sz. Given Rf = 1, R is uniform on [0, tl), and step 5 fails with probability
(tl mod 2^lam')/tl. Multiplying and summing over v' gives the identity. By Claim C.1, if |Zk| <= Cp then
sz - tl = sz - |Zk|, and otherwise sz - tl = sz - Cp. QED.

Cost on every branch.
- Steps 1 and 2: 28 lookup passes of L rows with O(lam + b)-bit fields, and O(b)-bit additions.
- Step 3: three sorts of L rows. For each of the 2^(2 lam - w) values g: L^2 binary searches, at most Cq appends and
  a sort of at most Cq rows for T3(g). For each (g, h): 2L binary searches and at most 2 Cq appends for P45(h) and
  P67(h2), a sort of at most Cq rows, and at most Cq binary searches into P45(h). In all this is
  O(2^(2 lam - w) L^2) = O(L^4/2^w) searches and appends.
- Reads: the counter rd caps them at 2 mY = 2 L^4/2^w, each followed by one binary search into T3(g); appends to Tl
  number at most Cp. So step 3 is O((L^4/2^w) lam) comparisons and moves of O(lam + b)-bit keys, whatever the labels.
- Steps 4-7: one pass of tl <= Cp rows with O(lam) control bits, one lookup pass of 2^lam' rows, and 2^lam' additions
  of 3n-bit labels.

Total: O((L^4/2^w) lam (lam + b) + Cp lam + 2^lam' (lam + n)) core steps. Quantum scratch is O(lam + b) qubits beyond
the seven index registers: the lookup registers, Rz, Rw, Ru, R, Rf and Toffoli-chain scratch, fewer than 32 registers.
Classical scratch is the three sort orders (L rows each); T3(g), P45(h) and P67(h2) (at most Cq rows each, with
O(lam + b)-bit keys); Tl (at most Cp rows of 7 lam bits); the block table (2^lam' rows); and O(1) counters. That is at
most 3 L + 3 Cq + Cp + 2^lam' rows of fixed size, freed at the end of the merge.

## D. Failure bound for MERGE7 on pool-output leaves

Lemma D.1. In the ideal run, consider a MERGE7 attempt at Phase M level k of a batch, with p its start position,
lam = Lam, w = w_k, lam' = Lam (or 1 at the root) and b = 7 Lam - lam' - kappa - w_k (P Section 8). Let Hp be the
sigma-field defined as in Lemma B.1, with the seven inputs of the attempt in place of four: it is generated by
everything that happened before its step 1 that a controller decision can read, except the label bits at positions
>= p of the leaves of its seven inputs. So Hp contains:
- the bits below p of those labels;
- the FW and PREP outcomes;
- the merge, MERGE4I and MERGE7 outcomes, with their counts, runs and lists;
- the coins and the controller decisions of all earlier steps;
- everything on other copies.
As in Lemma B.1, Hp does not contain LE's internal coins and test outcomes on the copies of these leaves, nor the
root outcomes of the current batch. Then

    Pr[FAIL | Hp] <= 9 * 2^(-lam) + 2^(-kappa - lam') + 2^(-kappa) < 2^(2 - kappa).

Proof. LEAVES are as in Lemma B.1: a leaf qubit of the supplier, with label k_j uniform on [0, 2^(B+1)), or a phantom
qubit of Lemma 9.1, with label 2^(pp_ell) u_j and u_j uniform. By the incidence paragraph of P Section 10:
- every table entry of the seven inputs is the sum of the labels over a 0/1 incidence set of leaves;
- distinct entries of one table have distinct incidence sets;
- the seven inputs use pairwise disjoint sets of leaves.
Let Lv be the set of leaves of the seven inputs. For j in Lv write k_j = lo_j + 2^p g_j + 2^(p+w) g'_j + 2^(p+b) u_j
with 0 <= lo_j < 2^p, 0 <= g_j < 2^w and 0 <= g'_j < 2^b'. This is possible as p + b <= B (P Section 8). Since
p >= pp_ell, the digits g_j and g'_j are uniform and independent of each other and of lo_j, also for phantoms.

Factorization. This is the factorization paragraph of Lemma B.1 word for word, with three substitutions:
- "the seven inputs" in place of "the four inputs";
- Lemma C.2 next to Lemma A.1 among the lemmas whose laws, keys, residues, sort keys, counts, ranks, lists and block
  choices read only label bits below p;
- the merges, MERGE4Is and MERGE7s at lower levels (p' + b' <= p) among the earlier steps.
Every earlier step that involves a leaf of Lv lies in the subtree of the attempt or in the FW stage below it, so it
reads only label bits below p. Bits below p of a sum of leaf labels depend only on the lo_j. Hence, conditional on Hp,
the pairs (g_j, g'_j) (j in Lv) are i.i.d. uniform on [0, 2^w) x [0, 2^b'). Let Hp' be generated by Hp and the g_j
(j in Lv); conditional on Hp', the g'_j are i.i.d. uniform.

Residues. An entry x of input t has label sum_(j in I_t(x)) k_j. So
h_t[x] = f_t(x) + sum_(j in I_t(x)) (g_j + 2^w g'_j) modulo 2^b, with f_t(x) = floor((sum_(j in I_t(x)) lo_j)/2^p),
which is Hp-measurable. For a triple, a pair, a four-tuple or a tuple e, write I(e) for the disjoint union of the
incidence sets of its parts. Then the residue modulo 2^s (s <= b) of the sum of its a_t, with the constant cA or cB
where it occurs, is (f(e) + sum_(j in I(e)) z_j) mod 2^s, with f(e) Hp-measurable and z_j = g_j + 2^w g'_j uniform on
[0, 2^b) given Hp. Its bits w..b-1, given Hp', are (f'(e) + sum_(j in I(e)) g'_j) mod 2^b', with f'(e)
Hp'-measurable.

Distinct triples (pairs, four-tuples, tuples) have distinct incidence sets: their parts come from tables on disjoint
leaves, and distinct entries of one table have distinct incidence sets. So at most one of each kind has an empty
incidence set. The pairwise-independence paragraph of Lemma B.1 applies:
- with H = Hp and the z_j mod 2^s, or with H = Hp, s = w and the g_j;
- with H = Hp' and the g'_j.
So for a count S of the elements of an H-measurable family with nonempty incidence sets and a fixed residue,
Var[S | H] <= E[S | H].

Bad fibers. Call (v, v2) BAD if |X_v| > 2 mX or |Y_v2| > 2 mY, and GOOD otherwise; this is Hp'-measurable. Fix v and
let S count the triples with nonempty incidence set and A mod 2^w = v. Then E[S | Hp] <= L^3/2^w = mX, and
|X_v| <= S + 1. If |X_v| > 2 mX, then D = S - E[S | Hp] >= mX >= 1, and |X_v| <= D + mX + 1 <= 3 D <= 3 D^2/mX. So
E[ |X_v| [|X_v| > 2 mX] | Hp ] <= 3, and the same holds for Y_v2 with mY. As sum_v2 |Y_v2| = L^4 and
sum_v |X_v| = L^3, the probability of a BAD (v, v2) is at most

    sum_v |X_v| [|X_v| > 2 mX]/L^3 + sum_v2 |Y_v2| [|Y_v2| > 2 mY]/L^4,

with expectation at most 3 * 2^w/L^3 + 3 * 2^w/L^4 <= 6 * 2^(2 lam)/L^3 = 6 * 2^(-lam), as w <= 2 lam.

Lost tuples. For GOOD (v, v2), Lemma C.2 applies. The sets Z(v, v2, v') over all outcomes partition the L^7 tuples,
so the sum over all GOOD outcomes of (sz - |Zk|) is at most the number of tuples that are not kept. Fix g and let S_g
count the triples with nonempty incidence set and class g. Then E[S_g | Hp] <= L^3/2^(2 lam) = L. The class has at most
S_g + 1 triples, so at most (S_g + 1 - Cq)_+ = (S_g - 2L)_+ of them are dropped. If S_g > 2L, then
D = S_g - E[S_g | Hp] > L and S_g - 2L < D <= D^2/L. So E[(S_g - 2L)_+ | Hp] <= Var[S_g | Hp]/L <= 1, and the expected
number of dropped triples is at most 2^(2 lam). In the same way (classes modulo 2^lam, E <= L^2/2^lam = L per class,
the same cap Cq = 2L + 1), the expected numbers of dropped (4,5)-pairs and of dropped (6,7)-pairs are at most 2^lam
each. A dropped triple lies in L^4 tuples and a dropped pair in L^5. So the expected lost contribution is at most

    (2^(2 lam) L^4 + 2 * 2^lam L^5)/L^7 = 3 * 2^(-lam).

Overflow. Fix a GOOD (v, v2) and fix v'. Let S' count the tuples of X_v x Y_v2 with nonempty incidence set whose bits
w..b-1 of A + By + cq equal v'. Given Hp', X_v and Y_v2 are fixed, and E[S' | Hp'] <= |X_v| |Y_v2|/2^b' <=
4 mX mY/2^b' = 4 L^7/2^(2w + b') = 4 mu7, as 2w + b' = w + b = 7 lam - lam' - kappa. Also sz <= S' + 1 and
Cp = 8 mu7 + 1, so (sz - Cp)_+ <= (S' - 8 mu7)_+. If S' > 8 mu7, then D' = S' - E[S' | Hp'] > 4 mu7 and
S' - 8 mu7 < D' <= D'^2/(4 mu7); so E[(sz - Cp)_+ | Hp'] <= Var[S' | Hp']/(4 mu7) <= 1. There are at most 2^(2w + b')
triples (v, v2, v'), so after the weights |X_v| |Y_v2|/L^7 of Lemma C.2 cancel the denominators, the overflow
contribution is at most 2^(2w + b')/L^7 = 2^(-kappa - lam').

Block. The terms (tl mod 2^lam') contribute less than 2^(2w + b') 2^lam'/L^7 = 2^(-kappa).

Summing. By Lemma C.2,

    Pr[FAIL | tables] <= Pr[BAD] + sum_(GOOD (v, v2)) sum_(v') [ (sz - |Zk|) + (sz - Cp)_+ + (tl mod 2^lam') ]/L^7.

Taking E[. | Hp], and E[. | Hp'] first for the overflow term, gives at most
6 * 2^(-lam) + 3 * 2^(-lam) + 2^(-kappa - lam') + 2^(-kappa). As lam >= kappa + 2 and lam' >= 1, this is at most
(9/4 + 1/2 + 1) 2^(-kappa) < 2^(2 - kappa). QED.

The bound conditions on no outcome of the attempt itself. It holds for every attempt, retries included, since a retry
uses fresh pool qubits whose leaves are not in any earlier attempt's input. It is used in P Lemma 9.1 exactly as
Lemma B.1 is, with seven inputs per attempt.
