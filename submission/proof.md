# OTP-FLQ080-YX-T2: one-time-pad label purification of FLQ080, tolerance 1 - 1/((16*10^126-1)(625*10^126-1)) of coherent label steering (model X), S_Q=O(n^(9/2) 2^((39999/50000) sqrt n)), Q=O(n^(7/2) 2^((39999/50000) sqrt n)), T=O(n^(9/2) 2^((82599/50000) sqrt n)), S_C=O(n 2^((82599/50000) sqrt n))

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), eT = 82599/50000, eP = 39999/50000,
aT = 413/250 = eT + 1/50000, aP = 4/5 = eP + 1/50000 and eps0 = 1 - 1/D, where D is the
integer (16*10^126 - 1)(625*10^126 - 1) = 10^256 - 641*10^126 + 1. (The letter D alone always means this integer;
"Section D" is the section of this file with that heading, and virtual.md uses a letter D only as a local variable
inside one proof of P.)

The single algorithm OTP-FLQ080-YX-T2 below receives N in binary and Q source copies, which it acquires before it
generates any random bit. At most floor(eps0 Q) of the copies are malformed in the sense of model X (Section A); all
other copies are ideal copies of rho_s, each in tensor product with everything else. For every model-X adversary,
including the one that corrupts nothing, it outputs the entire s with probability at least 1 - 2^-8.

On EVERY execution branch, and for every adversary, it satisfies jointly

    T = O(n^(13/2) 2^(eT sqrt n)),   S_C = O(n^3 2^(eT sqrt n)),   S_Q = O(n^(9/2) 2^(eP sqrt n)),   Q = O(n^(7/2) 2^(eP sqrt n)).

Every branch here includes the acquire-all store, the SHUFFLE, every OTP block, wrong extracted labels, the FW stage
(repeat-until-success included), supplier and pool aborts, failed and retried merges and discarded copies. Since
eP < eT, Section D sharpens these to the declared envelopes T = O(n^(9/2) 2^(eT sqrt n)), S_C = O(n 2^(eT sqrt n)),
S_Q = O(n^(9/2) 2^(eP sqrt n)) and Q = O(n^(7/2) 2^(eP sqrt n)).
All constants are absolute. The four growth indices are 1/2. The fifth claim is the tolerance 1 - 1/D under model X
(Section E).

Structure. OTP-FLQ080-YX-T2 is the algorithm P' = OTP(P) of Section B, with base P = FLQ080.
- P's complete specification and proof are given after the marker line of virtual.md; that text is our FLQ110 proof
  at new ratios, with the changes listed in P Section 1.
- Section A states model X. Section B defines P' from P and proves it correct under model X; its Theorem B.4 is
  generic. The finite branch of P' is the robust tester of Section B.5.
- Section C bounds the four resources of P' on every branch from P's allocation and cost bounds (P Section 14) and
  P's counting rule P (2.1). There is no storage wrapper: P' runs in P's storage model, with classical records in
  ordinary bits.

"P Section x", "P (x.y)" and "P Lemma x" refer to virtual.md, and "Section x" refers to this file. The resource,
success and tolerance statements inside virtual.md (its header and its Sections 0 and 13-16) concern P on ideal
copies; they are not claims of this file.

Notation for P: r, ell, m, dl, kappa, K, C_i, Y and Qcap are as in P Sections 0, 8, 11 and 13; w = 2^28,
RHO = 16385/8192 and HI are as in P Sections 7 and 8; and PP = RHO^ell 2^m (P Section 14). The OTP parameters L, wo,
Q', h_o and nb are those of (B.1). All logarithms are base 2.

What changed from the previous version of this row. Only the tolerance constant: the integer D of this section,
B.2 and Section G is now (16*10^126 - 1)(625*10^126 - 1), and with it the block exponent a = D and the block
sizes wo = a(L + 12) and wf = a(2n + 15), which are multiples of a. Otherwise the algorithm, the error model, the
four resource bounds and every proof step are unchanged, because the proofs use the constant only through a = D
being a positive integer with (1 - 1/D)^D < 1/2 (B.2; this holds for every integer D >= 1), and through D < 2^851
where a width is needed (the estimate of log2 Q' in B.2). No step uses any other property of D.

Credit, not a premise. The previous version of this row is an earlier submission by the same solver,
92a5fbd7-6c38-4b6d-b705-0b82347a1eab. Every step of this file uses only the text of the files of this snapshot;
nothing depends on the content, the bytes or the verdict of any other submission.

Snapshot. This archive is kshitij-hash's public row 4df039ed-690f-4b24-9045-a71dd1035384 (OTP-FLQ080-9999) with the tolerance
constant eps0 = 1 - 1/D, D = (16*10^126 - 1)(625*10^126 - 1), in place of 9999/10000, and the block exponent
a = D in place of a(9999/10000) = 6932; the row is renamed OTP-FLQ080-YX-T2. The constant a enters only B.2 (wo = a(L + 12) <= 4 D r,
log2 Q' <= 3r), B.5 (wf = a(2n + 15)), Theorem B.4 and Section C (Q' <= 4 D r Qcap <= 20 D r n C_0,
Qf = N (n+10) D (2n+15)). Since D is an absolute integer and wo = O(sqrt n) either way, every resource envelope
is the predecessor's. eps0 enters only through eps0^a <= 1/2 (B.2) and the malformed-count promise. Section G gives
the tolerance integers. Every other sentence, except the two paragraphs before this one, is the predecessor's
text, in which "we" and "our" refer to
kshitij-hash; the next paragraph describes the predecessor and keeps its constants. No step relies on any verdict.

Predecessor (kshitij-hash's text, constants as there). OTP-FLQ080-9999 is our OTP-FLQ110 construction at eps0 = 9999/10000 over a new base point. It is our OTP-FLQ110 (public
submission 8195ab7d-f2d2-4c3e-8ca9-f79459f4f009) with eps0 = 9999/10000 as in our OTP-LIMIT-BANK-9999 (public
submission 9e80c58c-cb24-45d7-9347-a20d97826f75), and with base P = FLQ080 in place of FLQ110. FLQ080 is our FLQ110
(87dfc97f-0a57-45d1-8d66-78c23b73518d) run with
ell = ceil(1251 r/100000), m = ceil(39373 r/50000), dl = ceil(21613 r/25000), which gives pool exponent
eP = 39999/50000 and tree exponent eT = 82599/50000; its fact (8.5), capacity Lemma 8.1 and exponents are re-derived in
virtual.md (P Sections 1, 8, 14 and 15). Sections A and B.1-B.7 are the text of OTP-LIMIT-BANK-9999 (one phrase
added in Lemma B.2: LE's internal test outcomes feed no decision of the ideal run)
(a(eps0) = 6932, wo = 6932 (ceil(log2 Qcap) + 12) <= 20797 r, wf = 6932 (2n+15)). Section C is OTP-FLQ110's with
these constants and P's exponent constants (C.1). It uses of P only facts that hold at every point of the family:
label-first, Qcap = 4 n C_0 + K, deltaP and log2 C_0 <= 2r - 1. No step relies on any verdict.

Exact envelopes. This archive is the model X tolerance upgrade OTP-FLQ080-YX-T2 of kshitij-hash's OTP-FLQ080-9999 (see the
Snapshot paragraph), with the Section C bounds declared exactly instead
of the rounded envelopes 2^(aT sqrt n) and 2^(aP sqrt n): Section 0's final sentence, Section D, the title and the four
structured resource objects change, and the row is renamed OTP-FLQ080-YX-T2. Apart from the constants eps0 and a of the
Snapshot paragraph, the algorithm and every proof are unchanged.

## 1. Provenance

The OTP layer, Sections A and B.1-B.7, is the text of our OTP-LIMIT-BANK (submission
63be7cca-89b9-4ec3-a50b-7ca93edcc335), unchanged: model X; the generic transformation OTP with its Theorem B.4
(acquire-all, the in-place swap shuffle, the full Z/NZ block merge with its one-time-pad Lemma B.2, and the interface
(i)-(iii)); and the robust finite branch B.5. There OTP was applied to F-LIMIT inside a counted storage bank. Here it
is applied directly to FLQ080, with no bank, and Section C replaces that file's storage sections.

Ingredients of the OTP layer that are prior work, as credited there:
- Kuperberg's CNOT merge of two phase qubits (SIAM J. Comput. 35(1), 2005, arXiv:quant-ph/0302112);
- spreading malformed copies by a uniform random assignment, and padding a label with an exactly uniform clean
  label: the ideas of Lemma Pi (uniform slots) and Lemma U (exact uniformity) of our RLS (submission
  280a17e4-429b-4604-9301-c829332d45cd), there used in the adaptive malformed-copy model at index 1;
- the timing and adaptivity clauses of the error-model text, which follow our ROB-GD2
  (4b79ce01-6091-4584-a506-0bb627a249fa);
- Fisher-Yates shuffling and the bound C(b,w)/C(Q,w) <= (b/Q)^w, which are textbook.

The base P is FLQ080, our FLQ110 (submission 87dfc97f-0a57-45d1-8d66-78c23b73518d) at new ratios (P Section 1);
FLQ110 is our F-LIMIT with fewer recycling levels,
a deeper collimation tree and larger leaf tables, a trade first made by qzv's SPQ rows for SPC-127 and by our G4Q110
for G4-124. F-LIMIT is qzv's HPC-127 (2aad498c-d5e9-4f64-a222-3b2f7f961738) with our FW stage, with AdamGagol's CS1
(f1481815-9577-4990-abe3-7b79fa5d9284) inside it. P Section 1 gives the full lineage of P, including the prior board
work on its cell family.

New here: the composition, that is, the check that FLQ080 is a label-first base, and the resource accounting of
Section C. Section B uses these facts of P:
- P uses its copies only through transform -> LE -> coin: P Sections 3, 9, 10, 11, 12 and 13 are F-LIMIT's text
  unchanged, and P Section 5 (LE) differs from F-LIMIT's only in the algorithm's name, so the label-first check of
  OTP-LIMIT-BANK applies word for word; it is restated in B.1;
- P Section 13 gives Qcap = 4 n C_0 + K and the ideal-run failure terms 2^-10 (pool exhaustion), 2^-40 (FW-stage
  abort), 2^-40 (supplier abort), 2^-20 (decoder) and 2^-40 (2-adic miss), so deltaP = 2^-10 + 3 * 2^-40 + 2^-20;
- P (8.3) gives log2 C_0 <= 2r - 1.
No earlier verdict on any submission is a premise.

## A. Error model X

The error_model text of the fifth claim is the definition. Remarks on it (not part of the text):
- rho_s = Pi_s/N, since the psi_(x,s), x in Z/NZ, are an orthonormal basis of V_s.
- By the substitution of P (3.1), psi_(x,s) = N^(-1/2) sum_k omega^(-kx) phi_k(s) (x) chi_k, and this change of basis is
  unitary. So V_s = span{phi_k(s) (x) chi_k : k in Z/NZ}, with one vector per Fourier label k. A malformed copy is a copy
  whose labels are steered coherently and arbitrarily, while each label's coin phi_k(s) is exact. Every single psi_(x,s)
  has exactly uniform labels. So failures of the source's internal randomness x (a classical law on x) are a special case
  that changes nothing; the content of model X is coherent label steering.
- |+> (x) chi_0 = phi_0(t) (x) chi_0 lies in V_t for every t. Such copies pass every candidate test of the exhaustive
  tester of P Section 13, so model X breaks that tester; Section B.5 replaces it.
- If malformed copies C_1, ..., C_r each satisfy the support condition, their joint state w satisfies
  (Pi_s (x) ... (x) Pi_s) w (Pi_s (x) ... (x) Pi_s) = w, because the projectors act on different systems. The condition
  for C is preserved by every operation on other systems and by conditioning on their measurement outcomes (both
  commute with (Pi_s)_C). The same holds for "clean copy in tensor product with everything else".

## B. The OTP layer: P' = OTP(P)

### B.1 Interface

A LABEL-FIRST base is an algorithm A with a cap Qcap computed from N before its first acquisition, such that:
- (i) A makes at most Qcap acquisitions on every branch;
- (ii) each acquisition is followed at once by a transform, then by LE (P Section 5) on the data register, and A uses the
  copy in no other way. The transform is a unitary U on the copy register, chosen from A's past, with U V_t = V_(u(t)) for
  every t, for a known bijection u of Z/NZ. LE ends by resetting the data register. Afterwards A uses only the LE output
  k (classically) and the control qubit, the COIN;
- (iii) A's correctness is proved for its IDEAL run. There, each acquisition-transform-LE returns (k, coin), with k
  uniform on Z/NZ and independent of everything before it, and the coin exactly phi_k(u(s)), in tensor product with
  everything else. The actual run differs from the ideal run only through an LE coupling term.

P's main branch is label-first:
- copies are used only by the supplier of P Section 11 (Mult_(alpha_j), LE, accept iff k < 2^dn, X) and by the leaf
  qubits of P Section 12 (Shift_(sh_g), LE, X);
- Mult_alpha maps psi_(x,t) to psi_(alpha x, alpha t), and Shift_c maps psi_(x,t) to psi_(x, t-c), so U V_t = V_(u(t));
- the latent-label model of P Section 3 and the IDEAL run of P Section 5 are (iii);
- P Section 13 bounds the ideal-run failure, without its LE term, by deltaP = 2^-10 + 3 * 2^-40 + 2^-20, with
  Qcap = 4 n C_0 + K.

P's finite branch is not label-first; it is replaced (B.5).

### B.2 Parameters

Fix eps0 in [0, 1); this file uses eps0 = 1 - 1/D with D = (16*10^126 - 1)(625*10^126 - 1) = 10^256 - 641*10^126 + 1,
a positive integer (Section 0). Put a = D. Then
eps0^a = (1 - 1/D)^D < e^(-1) < 1/2, since 1 - x < e^(-x) for x > 0 (here x = 1/D), and a < 10^256 < 2^851. Only
eps0^a <= 1/2 and a < 2^851 are used below (a need not be the least such integer). On the main branch put

    L = ceil(log2 Qcap),  wo = a (L + 12),  Q' = wo Qcap,  h_o = ceil(log2(Q'(n+5))) + 12,  nb = 2 ceil(log2 Q') + 20.   (B.1)

Since K <= C_0, Qcap <= 5 n C_0, and log2 C_0 <= 2r - 1 (P (8.3)), we get L <= 3r and wo <= D (3r + 12) <= 4 D r,
so log2 wo <= 2 + log2 D + log2 r < 853 + log2 r, by D < 2^851.
Since log2 Q' = log2 wo + log2 Qcap <= 853 + log2 r + log2(5n) + 2r - 1 and r >= 2^20 on the main branch (n >= 2^40,
so 855 + 3 log2 r <= r), log2 Q' <= 3r, and h_o, nb <= 7r. All are O(n)-bit integers. wo is the OTP block size (not FW's group size w = 2^28).

### B.3 The algorithm P'

Main branch (n >= 2^40). P' runs four steps.
1. ACQUIRE-ALL. Compute the parameters, which is deterministic. Acquire Q' copies, in order, into the store ST[0..Q'-1]
   of (n+1)-qubit registers. Before the last acquisition no random bit is generated, and no measurement is made whose
   outcome is not a fixed function of N.
2. SHUFFLE. For i = Q'-1 down to 1:
   - draw nb fair bits, each by H on a fresh |0> and a measurement, with value R;
   - put j = R mod (i+1);
   - SWAP the registers ST[i] and ST[j] in place (3(n+1) CNOTs).
   The classical state is i, R, j; no permutation is stored.
3. RUN P. Run P Sections 5-13 with one substitution. The v-th time P would acquire a copy, apply its transform U and run
   LE, P' runs BLOCK(v, U) instead: for t = 0, ..., wo-1 take c_t = ST[v wo + t], apply U, and run LE_o on its data
   register, obtaining kh_t. LE_o is P Section 5's LE with h_e replaced by h_o. Then:
   - if t = 0, the control of c_0 becomes the accumulator Acc, and K := kh_0;
   - if t >= 1, apply a CNOT from Acc to the control of c_t, and measure that control in the computational basis, with
     outcome sig_t. Reset and release it. Put K := K + kh_t mod N if sig_t = 0, and K := K - kh_t mod N if sig_t = 1.
   BLOCK hands (K, Acc) to P as LE's output and the copy's control. P continues unchanged: accept rule, X on the control,
   pools, tree, decoder.
4. At the end (or at an ABORT), release the store.

P makes at most Qcap requests (P Section 13), so v < Qcap always. BLOCK's classical state is v, t, K, kh_t and sig_t.
All randomness of P' (SHUFFLE, FW tickets and registers, P's coins beta_i, measurement outcomes) arises after step 1.

### B.4 Sampling and purification

Fix N, s and a model-X adversary with fraction eps0. Let B be the set of malformed acquisition positions, and Pm the
SHUFFLE permutation (ST[p] holds the copy acquired at position Pm(p)). E is the event that for every v < Qcap the block
{Pm(v wo + t) : t < wo} meets the complement of B.

Lemma B.1 (sampling).
(a) Pm is within total variation 2^-20 of a uniform permutation that is independent of B, the copies and the adversary.
(b) If Pm is uniform and independent of B, then Pr[not E] <= Qcap eps0^wo <= 2^-12.

Proof. (a) By step 1 and model X, B and the copies depend only on N, s, the algorithm's description and the adversary's
system. The fair bits come later, from fresh qubits in tensor product with every copy, so they are exactly fair and
independent of all of this. With R uniform on [0, 2^nb), each value of j = R mod (i+1) has floor or ceiling of
2^nb/(i+1) preimages, so the law of j is within total variation (i+1)/2^nb of uniform on [0, i]. Swap-based
Fisher-Yates with exactly uniform j gives a uniform permutation. Coupling the j's one by one, the total variation is at
most sum_(i=1)^(Q'-1) (i+1)/2^nb <= Q'^2/2^nb <= 2^-20.
(b) Block v is a uniform wo-subset, independent of B, and |B| <= eps0 Q'. So
Pr[block in B] = prod_(t<wo) (|B| - t)/(Q' - t) <= eps0^wo = (eps0^a)^(L+12) <= 2^-(L+12) <= 2^-12/Qcap. Take a union
bound over the Qcap blocks. QED.

Lemma B.2 (purification). Condition on B and on a Pm in E. Consider the run in which each LE_o output is replaced by the
virtual label defined in (L1). In that run, the joint law of P's transcript (all of P's measurement outcomes other than LE's internal test outcomes,
which feed no decision in the ideal run, classical
decisions and output) equals its law in P's IDEAL run. Moreover, conditional on any prefix of that transcript, and on
all OTP-internal records, the state of P's registers equals the ideal-run state given the prefix, and it is in tensor
product with the adversary's system, the store and those records.

Proof. (L1) Exact coin.
- LE_o acts on the data register only by ancilla-controlled translations Tr_c, which are diagonal in the chi basis
  (Tr_c chi_k = omega^(-kc) chi_k). It then measures the ancillas and resets the data register. So a complete chi-basis
  measurement of the data register inserted just before LE_o changes neither the joint law of all outcomes nor the
  state of any other system: the tests commute with chi-dephasing, and the final trace absorbs it. Its outcome is the
  virtual label k_t.
- Given k_t, the data register is chi_(k_t), so P Section 5 applies verbatim: LE_o returns k_t except with probability
  at most 4(n+5) 2^(-h_o).
- Let c_t be malformed. By model X and remark A, the joint state just before U is supported on V_s (x) (rest), so after
  U it is supported on V_(s') (x) (rest), where s' = u(s). Every vector there is sum_k phi_k(s') (x) chi_k (x) |e_k>,
  with |e_k> on all other systems, and projecting the data on chi_k leaves phi_k(s') (x) chi_k (x) |e_k>. So given
  k_t = k, the coin is the pure state phi_k(s'), in tensor product with every other system. The law of k_t is arbitrary.
- Let c_t be clean. It is rho_s in tensor product with everything (remark A), U gives rho_(s'), and by P (3.1) k_t is
  uniform and independent of everything else, with coin phi_(k_t)(s').

(L2) Merge. phi_K (x) phi_k = (|00> + omega^(-ks')|01> + omega^(-Ks')|10> + omega^(-(K+k)s')|11>)/2. After a CNOT from
the first qubit to the second, the outcome sig = 0 leaves phi_(K+k)(s') and sig = 1 leaves phi_(K-k)(s'), each exactly,
with probability exactly 1/2. This does not depend on K, k, s' or anything else. So, given its virtual labels and
signs, BLOCK ends with Acc = phi_K(s'), where K = k_0 + sum_(t>=1) (-1)^(sig_t) k_t mod N, a pure state.

(L3) One-time pad.
- The virtual-label measurements of a block act on data registers, which nothing else in the block touches. So they
  commute with the CNOTs and the coin measurements, and may be taken first.
- On E, let t* be the first clean position of the block. k_(t*) is uniform and independent of the past, of the other
  labels of the block (whose joint law is arbitrary) and, by (L2), of the signs.
- Given all of these, K = +-k_(t*) + c mod N, where the sign and c are fixed. This is a bijective function of k_(t*), so
  K is uniform on Z/NZ.
- So, conditional on the whole past (P's transcript, the adversary and all earlier OTP records), BLOCK returns K uniform
  and independent of that past, with Acc exactly phi_K(s') in tensor product with everything else. This is the ideal
  return of (iii). The block's other labels, its signs and its LE_o outcomes are records that P never reads.

(L4) Induction over P's steps.
- P's own steps act only on P's registers and fresh ancillas. By the induction hypothesis these are in the ideal-run
  state given the transcript prefix, in tensor product with the rest. So their outcome laws are the ideal ones and do
  not depend on the OTP records or on the adversary.
- A BLOCK step is an ideal return by (L3).
- So the conditional law of each next transcript entry, given the prefix and all hidden records, is the ideal one given
  the prefix. Averaging over the hidden records proves the lemma. QED.

Redefined sigma-fields. P's proofs condition on sigma-fields of P's transcript: G in P Lemma 10.1, "the past of the
stage" in P Lemma 11.1, and "everything before" in P Lemmas 6.1, 7.2 and 9.1. For P' these are generated by P's
transcript alone:
- the block labels K are P's leaf labels;
- every BLOCK internal is excluded: individual labels and LE_o outcomes, the signs sig_t, the SHUFFLE bits, B and Pm.
This is how P Lemma 10.1 already excludes "LE's internal coins and outcomes, which in the ideal run feed no decision".
"Independent randomness outside the batch" means P's transcript outside the batch. By Lemma B.2, every statement of P
about the law of its ideal run holds for P', conditional on B and Pm in E. This includes the five ideal-run failure
bounds of P Section 13.

### B.5 Robust finite branch (n < 2^40)

Put wf = a(2n + 15) and Qf = N(n+10) wf. ACQUIRE-ALL Qf copies into the store, and SHUFFLE with
nb = 2 ceil(log2 Qf) + 20. Candidate cand = 0, ..., N-1 owns the (n+10) wf registers ST[cand (n+10) wf + i],
i < (n+10) wf. Apply Shift_cand to each in turn and measure its control in X; reject cand at the first minus, leaving its
remaining registers unused. Output the first cand not rejected, or 0.

Lemma B.3. For every N >= 2 with n < 2^40, every s and every model-X adversary with fraction eps0, this outputs s with
probability at least 1 - 2^-10 - 2^-12 - 2^-20.

Proof.
- s is never rejected. Shift_s maps V_s onto V_0 = |+> (x) span{|x>}. So every copy, clean (rho_0 = |+><+| (x) I/N)
  or malformed (joint state supported on |+> (x) C^N (x) rest), has its control exactly |+>.
- For cand != s, a clean copy becomes rho_(s - cand). Its control is I/2, since the off-diagonal term
  (1/N) sum_x <x|x + s - cand> is 0. The copy is in tensor product with everything, so its outcome is a fair bit,
  independent of all other outcomes.
- Cut each candidate's registers into n+10 runs of wf consecutive registers. There are N(n+10) <= 2^(2n+3) runs, since
  N <= 2^n and n + 10 <= 2^(n+3). By Lemma B.1, with wf in place of wo, the probability that some run holds no clean
  copy is at most 2^(2n+3) eps0^wf + 2^-20 <= 2^-12 + 2^-20, because eps0^wf <= 2^-(2n+15).
- Otherwise every wrong cand meets at least n+10 clean copies before it can survive, and it survives only if all of
  them show plus: probability at most 2^-(n+10).
- The output is wrong only if some cand < s survives: probability at most N 2^-(n+10) <= 2^-10. QED.

### B.6 Success of P'

On the main branch, for every N, s and adversary, the failure probability is at most the sum of:
- the SHUFFLE total variation, 2^-20, and Pr[not E] <= 2^-12 (Lemma B.1);
- P's ideal-run failure on E, at most deltaP (Lemma B.2);
- the LE_o coupling, at most 4(n+5) Q' 2^(-h_o) <= 2^-10. On E the actual run equals the virtual-label run unless some
  LE_o call errs, and LE_o's bound holds given any virtual label.
The total is 2^-20 + 2^-12 + deltaP + 2^-10 < 2^-8. On the finite branch the failure probability is at most
2^-10 + 2^-12 + 2^-20 < 2^-8 (Lemma B.3).

### B.7 The generic theorem

Theorem B.4. Let A be any label-first base with ideal failure probability deltaA, let eps0 < 1 be fixed, and let OTP(A)
be B.3 with A in place of P, sized by A's Qcap. Under model X with fraction eps0, OTP(A) fails with probability at most
deltaA + 2^-10 + 2^-12 + 2^-20, for every N, s and adversary. It makes exactly Q' = a(eps0) (ceil(log2 Qcap) + 12) Qcap
acquisitions, all before any random bit.

Proof. B.1-B.4 and B.6 use only (i)-(iii). QED.

The theorem covers every fixed eps0 < 1, with a(eps0) = ceil(1/log2(1/eps0)) for 0 < eps0 < 1; its proof uses a(eps0) only through eps0^a(eps0) <= 1/2, so any integer a >= 1
with eps0^a <= 1/2 may replace it. It is applied here with eps0 = 1 - 1/D and a = D (B.2). It adds:
- Q'(n+1) store qubits;
- O(Q') transforms and LE_o calls;
- O(n) classical bits.

### B.8 Where the cost of P' is counted

Section C below. It plays the role that the storage sections play in OTP-LIMIT-BANK.

## C. Resources of OTP-FLQ080-YX-T2 on every branch

Throughout, BLOCK replaces only P's acquisition-transform-LE steps (B.3). Every other step of P runs unchanged, with
the same caps, fixed loops and aborts, so the allocation and cost bounds of P Section 14 hold for P's own operations
inside P'. By P Section 14, C_0 = O(n^2 PP) and Qcap = 4 n C_0 + K = O(n^3 PP), and

    log2 PP <= eP sqrt n + 2.81,     m + dl <= eT sqrt n + 3.66.                              (C.1)

Parameters. By B.2, L <= 3r, wo <= D (3r + 12) <= 4 D r, log2 Q' <= 3r and h_o, nb <= 7r.

Q. On the main branch P' acquires exactly Q' = wo Qcap <= 4 D r Qcap = O(n^(7/2) PP) copies, all in step 1, and
none later.

S_Q. At any moment P' holds at most:
- the store, Q'(n+1) qubits, allocated in step 1 and released in step 4;
- one fair-bit qubit (SHUFFLE), and during a BLOCK the ancillas of LE_o, O(n) qubits reset after each call
  (P Section 5 with h_o = O(sqrt n));
- P's own qubits other than its acquired copies: the pool, whose qubits are the accumulators Acc and so lie in the
  store (counted again here), the FW ancillas and repeat-until-success registers, the depth-first index registers,
  merge registers and transform workspace. By P Section 14 these are at most S_Q(P) = O(n^2 PP).
So S_Q <= Q'(n+1) + O(n^2 PP + n) = O(n^(9/2) PP).

S_C. P's classical records are those of P Section 14, O(n^3 PP + n 2^(dl+m)) bits in fixed allocations. The pool
label tables now hold the block labels K, each an O(n)-bit word as before. OTP adds O(n) bits: the parameters of
(B.1), SHUFFLE's i, R and j, and BLOCK's v, t, K, kh_t and sig_t (B.3). No permutation, per-copy record or
block-internal record is stored. So S_C = O(n^3 PP + n 2^(dl+m)).

Core steps. P's own core steps number at most O(n^(7/2) C_0 + n^4 2^(m+dl)) + poly(n) (P Section 14), a count that
already includes, per acquisition, O(n^2) for the transform and O(n^(5/2)) for LE. OTP adds:
- SHUFFLE: Q' - 1 rounds. Each has nb fair bits (O(r)), one division of an nb-bit integer by an integer of at most
  3r bits (O(r^2) = O(n)) and one SWAP of two (n+1)-qubit registers (3(n+1) CNOTs). Total O(n Q').
- BLOCKs: at most Qcap of them (P Section 13). Each has wo transforms U (O(n^2) each, as in P), wo calls of LE_o
  (O(n^2 h_o) = O(n^(5/2)) each, P Section 5 with h_o <= 7r), wo - 1 CNOTs with their measurements and resets, and
  wo O(n)-bit additions or subtractions mod N. Total O(n^(5/2) wo Qcap) = O(n^(5/2) Q').
- The parameters (B.1) cost poly(n), and releasing the store costs O(n Q').
Since Q' <= 4 D r Qcap <= 20 D r n C_0, OTP adds O(n^(5/2) Q') = O(n^4 C_0) = O(n^6 PP) core steps. So P' has
O(n^6 PP + n^4 2^(m+dl)) + poly(n) core steps on every main-branch execution. Every loop of OTP is fixed-length, so
every branch terminates.

T. By (C.1), log2(S_C + S_Q + 2) = O(sqrt n). By P (2.1), applied to P',

    T = O(sqrt n (n^6 PP + n^4 2^(m+dl)) + poly(n)) + (n+1) Q' = O(n^(13/2) PP + n^(9/2) 2^(m+dl)).

Exponents. By (C.1), PP = O(2^(eP sqrt n)) and 2^(m+dl) = O(2^(eT sqrt n)), and eP < eT. So, jointly, on every
main-branch execution and for every adversary,

    T = O(n^(13/2) 2^(eT sqrt n)),  S_C = O(n^3 2^(eT sqrt n)),  S_Q = O(n^(9/2) 2^(eP sqrt n)),  Q = O(n^(7/2) 2^(eP sqrt n)).

These rest only on fixed allocations, caps and loop bounds, never on the contents of the copies, so they hold for
every adversary.

Finite branch (n < 2^40). B.5 acquires Qf = N (n+10) D (2n+15) copies into a store of Qf (n+1) qubits, shuffles
them with nb = 2 ceil(log2 Qf) + 20, and tests at most N candidates on at most (n+10) D (2n+15) registers each.
Since N < 2^(2^40), every resource on this branch is at most an absolute constant.

## D. Exact growth indices and declared envelopes

Section C gives, on every main-branch execution and for every adversary, T = O(n^(13/2) PP + n^(9/2) 2^(m+dl)),
S_C = O(n^3 PP + n 2^(dl+m)), S_Q = O(n^(9/2) PP) and Q = O(n^(7/2) PP), and (C.1) gives PP = O(2^(eP sqrt n)) and
2^(m+dl) = O(2^(eT sqrt n)). Since eT - eP = 213/250 > 0, n^2 2^(-(eT - eP) sqrt n) is bounded over n >= 1, so
n^(13/2) PP = O(n^(9/2) 2^(eT sqrt n)) and n^3 PP = O(n 2^(eT sqrt n)). Hence, for every N, s and adversary,

    T = O(n^(9/2) 2^(eT sqrt n)),  S_C = O(n 2^(eT sqrt n)),  S_Q = O(n^(9/2) 2^(eP sqrt n)),  Q = O(n^(7/2) 2^(eP sqrt n));

the finite branch adds only an absolute constant. The declared envelopes are B_T(n) = n^(9/2) 2^((82599/50000) sqrt n),
B_C(n) = n 2^((82599/50000) sqrt n), B_Q(n) = n^(9/2) 2^((39999/50000) sqrt n) and B_samples(n) = n^(7/2) 2^((39999/50000) sqrt n), each strictly
below the predecessor's 2^((413/250) sqrt n), 2^((413/250) sqrt n), 2^((4/5) sqrt n), 2^((4/5) sqrt n). For B(n) = n^beta 2^(a sqrt n)
with a > 0, log2 log2 B = (1/2) log2 n + log2 a + o(1), so g(B) = 1/2 exactly. The structured objects in submission.json are
exactly these envelopes.

## E. Error tolerance

The fifth claim is epsilon(n) = 1 - 1/D with D = (16*10^126 - 1)(625*10^126 - 1) = 10^256 - 641*10^126 + 1
under model X (Section A), for every N >= 2, with no threshold: of the Q
acquired copies, at most floor((1 - 1/D) Q) are malformed. By Section B.6, for every N, s and every such adversary,
including the one that corrupts nothing (the clean problem), OTP-FLQ080-YX-T2 outputs s with probability at least
1 - 2^-8 > 2/3. This holds jointly with the four bounds of Section C, which hold on every branch for every adversary.

Theorem B.4 holds for every fixed eps0 < 1. The value 1 - 1/D is written with the factorizations of Section G; the predecessor row used 9999/10000. Nothing is claimed for corruption outside V_s, or under any other error model.

## F. Scope and limitations

- Model X excludes every coin error: coin dephasing, phase flips and Regev's registers. Nothing is claimed under any
  model admitting them, and we do not claim that unmodified FLQ080 fails under model X.
- The time growth index is 1/2. This is a trade-off point: S_Q and Q at 4/5 and T and S_C at 413/250, now with
  tolerance 1 - 1/D. The store holds all Q' copies at once, so this construction has S_Q >= Q; it gives no positive
  tolerance at S_Q below Q.
- The OTP layer multiplies Q by wo = O(sqrt n) and adds Q'(n+1) store qubits. The 1/50000 slack of P's exponents
  absorbs both, so the four declared envelopes are P's.
- All polynomial powers, the threshold n >= 2^40, the group size w = 2^28 and all constants are unoptimized.
- P's own statements in virtual.md concern P on ideal copies. The four bounds and the tolerance 1 - 1/D of this file
  concern OTP-FLQ080-YX-T2.

## G. Tolerance constant of this snapshot

Recall D = (16*10^126 - 1)(625*10^126 - 1) (Section 0). Direct integer multiplication (checked with exact
integer arithmetic) gives the first three lines below; the fourth is the decimal form of 10^63 (64 digits).

    16*10^126 - 1  = 4329632813347406305223297584667745034303743116654997715999733453 * 3695463493041522429397493437973995985916922777904245876619237883
    625*10^126 - 1 = 8333333333333333333333333333333333333333333333333333333333333333 * 454542699741213689614002339379761334779789213398706674505003 * 165001
    10^130 - 641   = 2189251513709577192973000802960123783290116879858557832979634351 * 858746507556703404750738054330397864679429 * 5319114725318138222421821
    10^63          = 1000000000000000000000000000000000000000000000000000000000000000

(the factors need not be prime; each has at most 64 digits). Since 16*625 = 10^4 and 16 + 625 = 641,
D = 10^256 - 641*10^126 + 1, so D - 1 = 10^126 (10^130 - 641). Hence the supported expression of the fifth claim,
with numerator the square of 10^63 times the three factors of 10^130 - 641 and denominator the two factors of
16*10^126 - 1 times the three factors of 625*10^126 - 1 (the nine integers above), equals
10^126 (10^130 - 641)/D = (D - 1)/D = 1 - 1/D = eps0, a constant in (0, 1). D - 1 and D are coprime, so the
normalized numerator and denominator are D - 1 and D, each of 256 digits. Since D > 10^4 (indeed D > 10^255),
eps0 > 9999/10000.
