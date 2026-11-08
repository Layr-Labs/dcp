# OTP-LIMIT-BANK: one-time-pad label purification of F-LIMIT-BANK, tolerance 99/100 of coherent label steering (model X)

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), beta = 57739/50000 = 1.15478,
a = 2887/2500 = 1.1548 (a - beta = 1/50000) and eps0 = 99/100.

The single physical algorithm OTP-LIMIT-BANK below receives N in binary and Q source copies, which it acquires before
it generates any random bit. At most floor(eps0 Q) of the copies are malformed in the sense of model X (Section A);
all other copies are ideal copies of rho_s, each in tensor product with everything else. For every model-X adversary,
including the one that corrupts nothing, it outputs the entire s with probability at least 1 - 2^-8.

On EVERY execution branch, and for every adversary, it satisfies jointly

    T = O(n^130 2^(beta sqrt n)),   S_C = O(n),   S_Q = O(n^30 2^(beta sqrt n)),   Q = O(n^(7/2) 2^(beta sqrt n)).

Every branch here includes the OTP blocks, the SHUFFLE, wrong extracted labels, the FW stage (PREP included), supplier
and pool aborts, failed and retried merges, discarded copies, tag renumbering, initialization and final cleanup. Since
beta < a, the declared envelopes follow: T = O(n^130 2^(a sqrt n)), S_C = O(n), S_Q = O(n^30 2^(a sqrt n)) and
Q = O(n^(7/2) 2^(a sqrt n)).

All constants are absolute. The growth indices are 1/2, 0, 1/2 and 1/2 (Section 11). The fifth claim is the tolerance
99/100 under model X (Section 12).

Structure. OTP-LIMIT-BANK executes a fixed reference algorithm P' = OTP(P), without changing any of its quantum
operations, measurements, source requests or classical decisions.
- P is F-LIMIT. Its complete specification and proof are given after the marker line of virtual.md, which is
  byte-identical to the virtual.md of our F-LIMIT-BANK.
- Section B defines P' from P and proves it correct under model X. P' first acquires all copies and shuffles them in
  place. It then runs P, replacing each copy that P would acquire by a BLOCK of wo stored copies, purified into one
  copy-equivalent whose label is one-time padded. Its finite branch is the robust tester of Section B.5.
- Sections 2-11 are the counted-bank wrapper of OTP-LIMIT-BANK, run around P' instead of P.

"P Section x", "P (x.y)" and "P Lemma x" refer to virtual.md, and "Section x" refers to this file. The resource
statements inside virtual.md concern P in its own storage model, in which classical records are ordinary bits; they are
not claims of this file. Nor are virtual.md's header, which describes F-LIMIT-BANK, and its Section 16, whose tolerance 0
is P's under ideal copies; the tolerance claim of this file is 99/100 under model X (Sections A, B and 12). In Sections 2-11, "P step", "P's qubits", "P's records" and "P's measurements" refer to P',
the algorithm the wrapper runs. The wrapper changes only where data live:
- every classical record of P', except constant many O(n)-bit staged words, is kept in basis-state qubits, which are
  counted in S_Q and are read and written only at classically known addresses (Sections 3-6);
- P's qubits live in a fixed counted array of quantum slots, managed by an indexed free list (Section 4), and the store
  of P' lives in a fixed counted wire region.

Notation for P: r, ell, m, dl, kappa, K, C_i, Y and Qcap are as in P Sections 0, 8, 11 and 13; w = 2^28, q = 2^27,
RHO = 16385/8192, HI and c_F are as in P Sections 7 and 8; and PP = RHO^ell 2^m (P Section 14). The OTP parameters L,
wo, Q', h_o and nb are those of (B.1). C_P' is the number of core steps (P Section 2) of P' on a branch. All logarithms
are base 2. Constants c, c0, c1 are absolute.

## 1. Provenance

The OTP layer (Sections A and B). These parts are new here (ours):
- model X;
- the generic transformation OTP and its Theorem B.4: acquire-all, the in-place swap shuffle, the full Z/NZ block merge
  with its one-time-pad Lemma B.2, and the interface (i)-(iii);
- the robust finite branch B.5.

Its ingredients are prior work:
- Kuperberg's CNOT merge of two phase qubits (SIAM J. Comput. 35(1), 2005, arXiv:quant-ph/0302112; see also arXiv:1112.3333);
- spreading malformed copies by a uniform random assignment and padding a label with an exactly uniform clean
  label, the ideas of Lemma Pi (uniform slots) and Lemma U (exact uniformity) of our RLS (submission
  280a17e4-429b-4604-9301-c829332d45cd), there used in the adaptive malformed-copy model at index 1;
- Fisher-Yates shuffling and the bound C(b,w)/C(Q,w) <= (b/Q)^w, which are textbook.

Nothing in Sections A and B relies on RLS. The base inherits everything else:
- P and its proof are qzv's HPC-127 (submission 2aad498c-d5e9-4f64-a222-3b2f7f961738) with our FW stage (virtual.md);
- the wrapper is the text of our F-LIMIT-BANK (submission a9a7dcac-3918-44e8-84db-bda6b1dcebdd);
- the copy-use pattern transform -> LE -> coin that the interface names is HPC-127's, with AdamGagol's CS1
  (f1481815-9577-4990-abe3-7b79fa5d9284) inside it, as in our G4-124 (b48a1af4-3e6b-45d7-8cdb-a414739ddc21).

The storage construction is mpjunior92's. The construction of Sections 3-7 and the explicit-degree ledger of Section 9
are mpjunior92's idea, not ours. mpjunior92 applied them to HPC-127:
- HPC127-TAGBANK (6c0e2efd-41bd-4018-a24e-e386f3069c9b). It introduced the indexed free list and banked descriptors
  for an exponential coherent pool, the per-wire-event charge and the fixed spans (A, R, Wrow, H, B, e, D there; OWN,
  ROWS, WROW, HQ, LSPAN, EW, DRAW here) for HPC-127; it carries the tagged bank, exact renumbering and decoded
  classical-quantum invariant from IFCS1310-TAGBANK.
- HPC127-SHARP (73741b63-bfa1-4d24-b254-ca6fd0549221). The same construction with explicit polynomial degrees
  (n^4 control completion, n^16 wire events, n^100 per charged event, total power 132) in place of a pure envelope.
- Earlier rows by the same author that these build on: PSG21 (9fdfdb12-834d-441c-8bb1-717ab380abf3, a measured
  basis-state bank), LLV-GBANK (dc3ece2a-3068-487a-829f-29d5c9139f89, their first direct-wire bank), LLV-GBANKQ25
  (fbb8f36c-3904-4bf0-9ddf-e9f5d83657ae, direct-wire bank operations, classical forgetting and the complete counted
  prefix) and IFCS1310-TAGBANK (fc8aa038-cba6-42bf-a317-df1c36c956f7, lazy generation tags with exact renumbering).
- GordoAR's PSG2-QSTORE (2b2b0036-7bbc-4ce5-80a8-b8928f0ce120), on which that bank lineage builds: the direct stable
  wire map and the fixed-region maximum-address argument. Our Section 4 wire map and whole-prefix count descend from
  it.

We restate the construction completely, so that this file and virtual.md are self-contained. We keep mpjunior92's
constants so that the two can be compared line by line. Tags and free lists are standard programming techniques. No
earlier verdict on any submission is a premise here.

Ours, inherited from F-LIMIT-BANK, are:
- the reference algorithm P (F-LIMIT, specified and proved in full in virtual.md and not filed on its own), which
  replaces HPC-127's pairing stage by an instrument FW on w = 2^28 qubits. FW extends to w = 2^28 our sixteen-qubit
  instrument F16 (not filed), and both come from our own internal research sketch;
- the check in Section 2 that P supplies every property the construction uses;
- the lifecycle accounting for P's pool primitive FW (Sections 2 and 4);
- the exponents for P's parameters (Sections 8 and 10), where beta = 57739/50000 is an exact rational of P's
  schedule.

Prior board work on the same cell family. mpjunior92's PART7-189-TAGBANK (1e083775-5d0a-4070-bcdc-ded8ada75d3a),
PART31-190-TAGBANK (38897382-d7d7-44fe-8205-64ad028a41a5) and PART127-191-TAGBANK
(d444e283-4dcc-4836-a82b-bc1e6866e25b) use odd-pair cells with an all-equal remainder for odd group sizes, inside
the same banked storage. P is the even-size case at w = 2^28; we derived it independently, and its realization,
proof and schedule are our own.
mpjunior92's later rows PARTADAPT-193-TAGBANK (cfb1e549-2935-4d3f-a8b2-a01b125134ea, status failed in the
pipeline when checked) and PARTROOT196 (3315027c-4ec3-4352-80e5-f8f384e286f1, validating when checked) let the odd
group size grow with n and claim coefficients just above 2/sqrt 3; they are prior board work on the growing-size
case. We claim no priority over any of these rows.

Sibling. Our TRIAD-BANK (submission 9a129f0f-e377-466d-b45d-449843d2167e) applies the same construction to our
TRIAD-125 (submission f5b375dd-1e5c-4728-95dc-b855b2dc5827); mpjunior92's TRIAD185-TAGBANK
(74ff1ce3-b5ce-48f1-a153-640c223b8ab0) was the first application of this construction to TRIAD-125, and our
TRIAD-BANK followed. Our G4-BANK (not filed) applies it to our G4-124. Our F-LIMIT-BANK is G4-BANK's text with P = F-LIMIT, and Sections
2-13 here are F-LIMIT-BANK's text with P replaced by P'. The changes are: the facts of P' in Section 2; the OTP words
in Section 3; the store in Sections 4, 7, 8, 9 and 10; the exponent of Q in Sections 10 and 11; and Sections 12 and 13.
No step relies on F-LIMIT-BANK, TRIAD-BANK, G4-BANK, TRIAD-125 or G4-124, or on any of their verdicts.

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

Fix eps0 in [0, 1); this file uses eps0 = 99/100. Let a(eps0) be the least integer a >= 1 with eps0^a <= 1/2. Then
a(99/100) = 69, by the integer facts 2 * 99^69 < 100^69 and 100^68 < 2 * 99^68. On the main branch put

    L = ceil(log2 Qcap),  wo = a (L + 12),  Q' = wo Qcap,  h_o = ceil(log2(Q'(n+5))) + 12,  nb = 2 ceil(log2 Q') + 20.   (B.1)

Since K <= C_0, Qcap <= 5 n C_0, and log2 C_0 <= 2r - 1 (P (8.3)), we get L <= 3r, wo <= 69 (3r + 12) <= 208 r,
log2 Q' <= 3r and h_o, nb <= 7r. All are O(n)-bit integers. wo is the OTP block size (not FW's group size w = 2^28).

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
virtual label defined in (L1). In that run, the joint law of P's transcript (all of P's measurement outcomes, classical
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

The theorem covers every fixed eps0 < 1, with a(eps0) = ceil(1/log2(1/eps0)) for 0 < eps0 < 1; it is applied here with
eps0 = 99/100. It adds:
- Q'(n+1) store qubits;
- O(Q') transforms and LE_o calls;
- O(n) classical bits.

### B.8 Cost of P' in P's storage model

- Q = Q' = wo Qcap <= 208 r Qcap on every main branch.
- Qubits: P's, plus the store ST of Q'(n+1) qubits, the accumulator Acc and one fair-bit qubit.
- Core steps beyond P's: per copy, one SWAP pass (O(n)), U (O(n^2)), LE_o (O(n^2 h_o) = O(n^(5/2))) and one merge with
  an O(n)-bit addition; per SHUFFLE step, nb fair bits, one O(n)-bit division and one SWAP (O(n^2)). This is
  O(n^(5/2) Q') = O(n^6 PP).
- So P' has C_P' = O(n^6 PP + n^4 2^(m+dl)) + poly(n) = O(n^6 2^(beta sqrt n)) core steps on every main branch (P
  Section 14 and (P6)).

## 2. The reference algorithm P' and the facts used from it

Finite branch (n < 2^40). P' is the robust tester of Section B.5 (it replaces the exhaustive tester of P Section 13).
OTP-LIMIT-BANK runs it with ordinary storage: cand, the SHUFFLE words and the counters (O(n) bits), and Qf(n+1) + O(n)
qubits. It makes the same Qf acquisitions. There are finitely many such N, so this branch changes only absolute
constants.

Main branch (n >= 2^40). P' computes exactly the integers

    r = ceil(sqrt n), ell = ceil(2309r/4000), m = ceil(57747r/100000), dl = ceil(57731r/100000),
    kappa = ceil(log m) + 1, K = 2^13 (2r + ceil(log n) + 30), C_ell = 2^12 n K 2^m dl,
    C_i = ceil(16385 ell C_(i+1)/(8192(ell-1))) (i = ell-1..0),
    Y = least integer with 2^Y >= C_0,  Qcap = 4 n C_0 + K,

and L, wo, Q', h_o and nb of (B.1). It runs Section B.3: ACQUIRE-ALL, SHUFFLE, then P Sections 5-13 with BLOCK in
place of P's acquire-transform-LE. P Sections 5-13 comprise: label extraction (LE_o inside BLOCK); the FW stage, ell FWLEVELs of q(Y+1) rounds each; the bit
allocation of P Section 8 for each requested B; BATCH with its linear-merge tree; the free-frequency decoder; and the
2-adic part. Every ABORT outputs 0.

Completion of unspecified orders. P leaves three orders open:
- equal-key ties in its merge sorts;
- the order of LIVE after an FWLEVEL round;
- the order of OUTPUT.

OTP-LIMIT-BANK fixes them as follows:
- sorts are stable, with ties in current list order;
- after a round, LIVE lists, in scan order, the qubits a group returns to LIVE at the position of that group (for a
  pair cell its w - 2 returned qubits, in group order; for a matching cell or Ev its recycled qubit) and the
  ungrouped qubits at their own positions;
- OUTPUT is in order of production, so "the first C_(i+1)" of P Section 9 step 2 is defined.

These orders are functions of P's classical history only, never of slot numbers or bank addresses. Every lemma of P
that meets these orders holds for any order that is a function of the past:
- P Lemma 7.2 holds "For ANY labels, and conditional on everything before the level", and the live count
  S_end <= (w - 1)E of P Section 7.2 holds "whatever the labels and outcomes";
- the sigma-field G of P Lemma 10.1 contains all decisions of the controller;
- P Lemmas 6.1, 9.1, 9.2 and 11.1 are conditional on the past.

So this completion is an instance of P, and of P'.

Facts used. Sections 3-10 use only the following properties of P'.

(P1) Success. For every N, s and model-X adversary with fraction eps0, P' outputs s with probability at least
1 - 2^-10 - 2^-12 - 2^-20 on the finite branch and at least 1 - 2^-8 on the main branch (Section B.6). The main-branch
failure probability is at most the sum of:

    2^-20 (SHUFFLE) + 2^-12 (a block without clean copy, Lemma B.1) + 2^-10 (pool exhaustion, P Lemma 9.1)
    + 2^-40 (FW-stage abort, P Lemma 9.2) + 2^-40 (supplier abort) + 2^-20 (decoder, P Lemma 11.1)
    + 2^-40 (2-adic miss) + 2^-10 (LE_o coupling, B.6)  <  2^-8.

The five middle terms are the ideal-run terms of P Section 13 (deltaP), which hold for P' by Lemma B.2.

(P2) Word sizes and loops.
- Y <= 2r <= n (P (8.3)), and L, wo, Q', h_o, nb <= 2^(7r) have O(n) bits (B.2).
- Every label fits a 3n-bit field (P Sections 6 and 9).
- Every parameter above, every position pp_i and tp_i, and every loop limit has O(n) bits.
- Every loop has a length fixed by the parameters or is cut off by the caps on pool qubits and acquisitions
  (P Section 14). This holds on every branch, so every branch terminates.

(P3) Classical records. On every branch P's classical arrays are the following.
- The supplier's pool list, and in an FWLEVEL the lists LIVE and OUTPUT, the merge-sort scratch and the measured
  code of the current cell (w rows of 29 bits). Each has at most C_0 rows, since Cin = C_i <= C_0, LIVE never grows,
  and OUTPUT has at most Cin/2 rows: each FW appends gamma <= rho/2 good outputs while it removes rho qubits from
  LIVE, so |OUTPUT| <= (Cin - S_end)/2 by P (7.3) (P Section 7.2).
- In the tree: at most three retained tables per level, each of at most 2^(dl+m-1) rows. For the one active merge:
  the arrays aa, bb, order, pos, lo, cnt, off, Dx and the block inverse v -> (x_v, y_v), each of at most 2^(dl+m)
  rows (P Sections 6.2 and 14).
- The decoder's K records (Z_i, beta_i, W_i) and K residues (P Section 11).
- The OTP words of P' (v, t, K, kh_t, sig_t, and SHUFFLE's i, R, j): one array of 8 rows (Section B.3).
- LE's 2(J_e + 1) test counters and directions (P Section 5).
- The profiles over i of C_i, pbmax_i, pb_i, pp_i (ell rows) and of lam_i, tbmax_i, tb_i, tp_i (m+1 rows)
  (P Section 8), and the 4096-row table of P Section 4.
- O(1) scalars per loop level and per frame of the depth-first recursion, whose depth is m+1.

Each row of these arrays has at most 12n bits. Lists store a handle to their qubit; P calls it the "wire index", and
here it is a slot number (Section 4).

(P4) Qubits. At any time P holds at most:
- C_0 pool qubits (P Section 14);
- 2(m+1)(dl+m) <= 4r^2 <= 16n qubits of stacked index registers (P Section 14; m + 1 <= r and dl + m <= 2r);
- a fixed set of scratch registers: the current copy (n+1 qubits), the accumulator Acc and one fair-bit qubit; the transform, modular-addition and LE scratch of
  P Sections 3 and 5; the merge registers Ru, Rv, Rz, Rp, Rd, R and their Toffoli-chain scratch (P Section 6); the
  FW registers T, R and P, the PREP try qubits and the Boolean-evaluation scratch, at most c_F qubits in all, an
  absolute constant (P Section 7.1); and one coin qubit (P Section 11).

These are explicit ripple and Toffoli-chain circuits. Apart from FW's registers, (P4) lists fewer than 512 registers,
each of at most 4n qubits, so the scratch totals at most c0 n + c_F qubits with c0 <= 2^11 and c_F <= 2^90 <= n^3.
In addition P' holds the store ST of Q'(n+1) qubits (Section B.3). It is not one of the registers above: the wrapper
keeps it in a fixed wire region of its own (Section 4), not in slots.

(P5) Lifecycle. Every qubit of P' outside the store is created in one of two ways:
- by a store transfer, when BLOCK takes a register ST[p], whose n+1 qubits move into slots (Section 4);
- by allocation in |0>, as scratch of a transform, a modular addition, an LE test, a LOOKUP, a MERGE, an FW, a PREP try, a
  fair bit or a coin.

Store qubits are created by the acquisitions of ACQUIRE-ALL. SHUFFLE moves them only by SWAPs inside the store. A
transfer leaves the store wires in |0>, and the store is reset with the prefix at the end. Each such operation allocates at most c0 n qubits (at most c_F for an FW apart from its PREP tries, and at
  most 29 for a PREP try) and contains at least one P step.

Every P qubit ends by being measured and released, or reset and released, or released in a known basis state. In
three places P leaves the release implicit: the unused final-pool qubits after the K roots (P Section 9), the wd = 1
leaf qubits with kk != 1 (P Section 12), and R after a step-4 FAIL of MERGE (P Section 6.2). OTP-LIMIT-BANK completes P
there, and wherever else a release is implicit, by one rule: a qubit that P never touches again is reset and released
at that point (a trace-out, so the result is still an instance of P). In detail:
- BLOCK: LE_o resets the data register of each copy c_t, which is released. The control of c_0 becomes Acc. The control
  of c_t, t >= 1, is measured after its CNOT, then reset and released. Acc is handed to P as the copy's control. A fair-bit
  qubit is measured, reset and released.
- LE resets the data register of a copy. A rejected copy is released. An accepted copy's control becomes a pool qubit
  (P Sections 5, 11 and 12).
- An FW on pool qubits A_0, ..., A_(w-1) (P Section 7.1) first runs PREP: each try allocates j_N + 1 <= 29 fresh
  qubits, measures and resets the flag, and on failure measures, resets and releases the try qubits; on success they
  become R_N. It allocates T, P and the Boolean-evaluation scratch in |0>. Steps 1-4 return T, R, P and all scratch
  to |0> on every input (P Lemma 7.1(c)): steps 2-3 compute and uncompute cleanly, step 4 measures and resets P,
  every R_N and, for a matching cell, T, and for Ev returns T to |0> by H. They are then released. Step 5 depends
  on the recorded cell C:
  - for each pair {a, b} of C, a < b: A_b is brought to |1> by a CNOT, then to |0> by NOT, and released; A_a (a
    good output) stays;
  - if C has a block Bl = {c_0 < c_1 < ...} (a matching cell or Ev): after the CNOTs A_(c_0) -> A_(c_i) the qubits
    A_(c_i), i >= 1, are |0> and are released; A_(c_0) (the recycled output) stays;
  - the w - 2 qubits unconstrained by a pair cell stay, unchanged.
  P Lemma 7.1(c) states that step 5 leaves every released qubit in |0> on every input. So an FW, apart from its
  PREP tries, makes at most c_F + 2w wire events, an absolute constant, and each PREP try makes at most 58; an FW
  releases between 1 and w - 1 of its inputs, each in |0>, and keeps the others.
- At the end of an FWLEVEL, LIVE is measured, reset and released. BATCH step 2 measures and releases the unused
  outputs (P Sections 7.2 and 9).
- LEAF transfers dl pool qubits into an index register and allocates nothing.
- MERGE allocates its registers. It returns x and y to |0> (step 5) and releases them, keeps the low lam' bits of R as
  the output index register, and on FAIL resets and releases both inputs (P Section 6.2).
- A root is measured and released, and unused roots are released (P Sections 11 and 12). At an ABORT or at the end
  every remaining qubit is released.

(P6) Cost. On every main branch, P Section 14, (2.1) and Section B.8 give:
- C_P' = O(n^6 PP + n^4 2^(m+dl)) + poly(n) = O(n^6 2^(beta sqrt n));
- exactly Q' = wo Qcap <= 208 r Qcap acquisitions (B.2), with Qcap = 4 n C_0 + K (P Section 13);
- C_0 <= 8 RHO^ell C_ell (P (8.2));
- log PP <= beta r + HI + 1 and m + dl <= beta r + 2 (P Section 14).

P's declared envelopes are 2^((2887/2500) sqrt n) (P Sections 0 and 15). This file does not use them. It uses the
sharper main-branch bounds of P Section 14 listed above, which P proves with explicit polynomial factors and the
exact coefficient beta = 57739/50000, and which P Section 0 also states.

The pool primitive. The HPC-127 version of this construction differs from the present one only in P's pool primitive
(PAIR there, FW here, G4 in G4-BANK, TRIAD in TRIAD-BANK) and in the schedule constants. The construction uses the
pool primitive
only through (P4) and (P5): a bounded number of wire events per primitive, kept qubits transferred by handle, and
released qubits reset. By P Lemma 7.1(c), which holds for every input state, FW satisfies both. The number of inputs
an FW releases (between 1 and w - 1) is fixed by its recorded cell; the construction uses only the bound w - 1 on it,
since each release is one FREE_Q of a qubit that P releases. Sections 3-10 use P's yield lemmas
(P Lemmas 7.2 and 9.2) and Sections A and B only through (P1), and the schedules only through (P2), (P3) and (P6).

## 3. Fixed capacities of the bank

Put U = C_0 + 2^(dl+m) + 1 and

    OWN = 2^16 n^2 owners,  WROW = 2^16 n^2 bit cells per row,  ROWS = 2^24 n^4 U rows per owner,
    HQ = 2^20 n^2 U quantum slots.

An owner holds one logical array. The logical bit (o, i, j), with o < OWN, i < ROWS and j < WROW, has the address

    c = o ROWS WROW + i WROW + j  <  LSPAN = OWN ROWS WROW = 2^56 n^8 U.               (3.1)

Fit. Every array of (P3) has at most max(C_0, 2^(dl+m), K, 4096, ell, m+1, 2(J_e+1)) <= U <= ROWS rows. The
slot metadata of Section 4 has HQ rows, and HQ <= ROWS because ROWS/HQ = 16 n^2. Every row of P has at most
12n <= WROW bits. A slot number is below HQ < 2^n, so it has at most n bits.

Descriptors of P's qubits (Section 4) have one slot number per row:
- a pool qubit's slot number is a field of its row in the pool list, LIVE or OUTPUT;
- an index register of a phase vector has a descriptor array of at most dl + m rows in the same per-level family as
  its table;
- each of P's named scratch registers (P4) has its own descriptor array of at most c0 n + c_F <= U rows.

Fewer than 64 arrays are live per tree level and per FW level. The others are fewer than 65 + 520: fewer than 65
for the decoder, LE, the OTP words, profiles, table, slot metadata and frame arrays, and fewer than 520 scratch
descriptors (the registers of (P4) and of FW). So at most 64(m + 1) + 64 ell + 585 <= 512(m + ell + 2) <= OWN arrays are
live at once. Frames of
P's depth-first recursion and its loop counters are rows of fixed frame arrays indexed by depth; they are not
ordinary memory. Owners are reused through FREE_OWNER and ALLOC_OWNER (Section 5). These capacities are fixed before
P starts and do not depend on the branch.

## 4. Physical layout, and the quantum slot allocator

Each epoch has EW = (n+2)^20 tag bits. Every logical bit has one value bit and EW tag bits. The RAW span is

    DRAW = LSPAN (EW + 1) + (OWN + 8) EW + OWN + 2^20 n^4,                                (4.1)

laid out in RAW indices as follows:
- logical bit c < LSPAN: value at RAW index (EW+1)c, and tag bit t < EW at (EW+1)c + 1 + t;
- then OWN + 8 words of EW bits: the epoch ep(o) of each owner o, the global generation G, the backup word of
  Section 6, and six spare words;
- then OWN active flags;
- then 2^20 n^4 RAW scratch bits, which hold the owner bindings (which logical array an owner holds) and the fixed
  RAW state of the interpreter.

These ranges are disjoint and end below DRAW. RAW records carry no tags.

Physical wires:
- RAW index j is wire 2j;
- quantum slot k < HQ is wire 2k + 3;
- wire 1 is spare;
- qubit t <= n of store register ST[p], p < Q', is wire 2h + p(n+1) + t (the STORE region).

Let h be the least power of two with h >= max(DRAW, HQ + 2). On the main branch OTP-LIMIT-BANK first computes the
parameters with O(n) staging (Section 8). It then allocates wires 0, ..., 2h + Q'(n+1) - 1 in |0> once, and releases
them once at the very end, after the output is written. In between it allocates only an (n+1)-qubit acquisition
register, one at a time. Hence on every main branch

    S_Q <= 2h + Q'(n+1) + n + 1.                                                          (4.2)

Store wires are acted on only by the SWAPs of acquisitions, SHUFFLE and store transfers, at wire numbers computed
from p and t by staged arithmetic.

Bank wires are acted on only by computational-basis measurements and by X gates conditioned on classical bits.

Slot allocator. The bank holds the logical words head and virgin (O(n) bits each), the logical array NEXT of HQ rows,
and the descriptors of Section 3. Every P quantum register outside the store is a pool qubit or a register with its own descriptor
array, and its descriptor rows list its slot numbers, one per row. P's lists store slot numbers where P stores wire
indices. head = HQ means empty.
- ALLOC_Q: if head != HQ, put k := head and head := NEXT[k]; otherwise put k := virgin and virgin := virgin + 1.
  Return k.
- FREE_Q(k): reset wire 2k+3 (the reset core step, which records no outcome); then NEXT[k] := head and head := k.

Initially head := HQ and virgin := 0. NEXT[k] is read only after FREE_Q(k) has written it. No operation scans the
slots. Every head, NEXT and virgin access is a known-address word operation.

Invariant (I). The slots below virgin are partitioned into two sets:
- slots holding live P qubits, one slot per qubit, mapped injectively by the descriptors;
- slots on the free stack, which has no repetitions and whose slots are in |0>, in tensor product with everything.

Slots at or above virgin are untouched |0>. ALLOC_Q removes a free or untouched slot from those sets and gives it to
exactly one new P qubit. FREE_Q is called only when P releases that qubit, never when a handle is merely passed or
copied, and it returns the slot to |0>. A P qubit keeps its slot from allocation until release, and passing a
register passes its descriptor, never a copy of its qubits. So (I) is preserved. Gates read their operands' slot
numbers from the descriptors and act on the corresponding odd wires.

The pool is never full. By (P4), with the completion rule of (P5), at most C_0 + 16n + c0 n + c_F + 2 slots are live at
once. Since c0 <= 2^11 and c_F <= n^3 <= C_0 (C_0 >= 2^m with m >= 600000, P Sections 8 and 13),

    live  <=  2 C_0 + 2^11 n + 16n + 2  <  HQ,   because HQ = 2^20 n^2 U >= 2^20 n^2 C_0.

If virgin = HQ and the free stack were empty, all HQ slots would be live, a contradiction. So ALLOC_Q always
succeeds, and no abort or guard is added.

Wire events. Call every ALLOC_Q, FREE_Q and descriptor-row update a wire event. By (P5):
- allocations number at most (c0 n + c_F) C_P' + (n+1) Q' (store transfers included);
- releases number at most the allocations;
- each allocation or release updates at most c1 descriptor rows;
- moving a qubit between lists costs nothing extra: its slot number is a field of the list row, and P copies that row
  itself, in P steps already counted in C_P';
- only LEAF and MERGE step 6 move slot numbers into descriptor rows, at most c1 rows per moved qubit. LEAF moves dl
  qubits and builds 2^dl table rows, and MERGE step 6 moves lam' qubits and writes 2^lam' table rows, so each such
  move is charged to at least 2^dl or 2^lam' table rows, hence to at least one P step per moved qubit.

Hence a branch has at most

    c n (C_P' + Q')  =  O(n^16 (C_P' + Q' + HQ + 1))                                     (4.3)

wire events. The HQ slots are prepared once and cleared once, and are never scanned for an allocation, a gate, a
root, a request or a batch.

## 5. Bank operations

RAW_READ(j) measures wire 2j in the computational basis into one staged bit. RAW_WRITE(j, v) does RAW_READ(j) into a
staged bit z, applies X to wire 2j if z != v, and forgets z. The address j is always a classically known staged word;
no gate is ever controlled by a superposed address.

Epoch words ep(o), G and the backup are EW-bit RAW words. They are compared, copied and incremented bit-serially, with
one staged carry or equality bit and an O(log n)-bit bit counter. An epoch value is never held as an ordinary word.

- READ(o, i, j): compute c by (3.1), then compare the tag of c with ep(o) bit by bit. Return the stored value if they
  are equal, and 0 otherwise.
- WRITE(o, i, j, v): RAW_WRITE the value bit of c to v, then copy ep(o) into the tag of c bit by bit.
- ALLOC_OWNER: find an inactive owner o by scanning the OWN active flags. If G is all ones, run Section 6 first. Then
  G := G + 1, ep(o) := G, set o's active flag, and record its binding in RAW scratch.
- FREE_OWNER(o): clear o's active flag. No cell is cleared.

Initially every RAW bit is 0, so G = 0 and every tag is 0. Every active owner has an epoch >= 1.

Lemma 5.1 (lazy arrays). At all times every stored tag is at most G, and the epoch of an active owner exceeds every
tag that was stored in its cells before its activation. Consequently READ(o, i, j) returns the value of the last
WRITE to (o, i, j) during o's current activation, and 0 if there was none.

Proof. G does not decrease between renumberings. ALLOC_OWNER sets ep(o) = G + 1, which exceeds all stored tags
because they are at most G by induction. WRITE stores the tag ep(o) <= G. A cell (o, i, j) is written only through
owner o. If it was written during the current activation, its tag is ep(o), since every write in that activation
stores ep(o). Otherwise its tag was stored earlier, so it is 0 or a tag stored before the activation, and in both
cases it is smaller than ep(o). Section 6 preserves every decoded value and re-establishes both invariants. QED.

So the bank realizes zero-initialized arrays with O(1)-cost FREE and ALLOC: an exponential array is never cleared on
each free or retry. Where P only specifies fresh scratch, zero initialization is a valid fixed completion.

Words, loops and LOOKUP.
- An O(n)-bit field of a row is a run of logical bits. Word operations are bit-serial, with a staged carry.
- P's classical computations run as fixed bit-serial code whose operands are READ from and WRITTEN to the bank. These
  are the comparisons, additions, merge sorts and binary searches; table construction; the residue updates of the
  decoder; and parameter arithmetic, with schoolbook multiplication and division. Only constant many O(n)-bit words
  are staged at once.
- P's loop counters, recursion frames and profiles are bank rows. There is no ordinary call stack, no growing
  transcript and no stored circuit; the fixed program generates P's gates online.
- P's LOOKUP (P Section 6.1) remains its serial circuit. For each row x0 and output bit, the program READs that bit
  of tab[x0] and emits the CNOT from the flag if it is 1. A superposed P index is never used as a bank address.

## 6. Exact renumbering when G is full

OTP-LIMIT-BANK never assumes that G cannot wrap. If ALLOC_OWNER finds G all ones (a bit-serial test), P is paused, and the
following is done for o = 0, ..., OWN-1.
- If o is active: copy ep(o) into the backup word. For every cell (o, i, j), compute its decoded value against the
  backup, write that value and set the tag to o + 1, padded to EW bits. Finally set ep(o) := o + 1.
- If o is inactive: set all its values, all its tags and ep(o) to 0.

Then G := OWN, and the pending ALLOC_OWNER resumes.

Afterwards:
- every tag is at most OWN = G;
- an active owner's cells carry the tag o + 1 = ep(o) and decode to their previous values (unwritten cells decode to
  0, as before);
- an inactive owner's cells carry the tag 0, below any later epoch.

So the invariants of Lemma 5.1 hold again. Since OWN + 2 < 2^EW, generations remain available, and repeated wraps are
handled in the same way.

During renumbering no P operation, source request or quantum operation occurs, and the old epoch is held only in the
RAW backup. The decoded record and every P qubit are unchanged, so no abort, failure, request or probability change is
introduced. One renumbering costs at most c n^22 DRAW charged steps.

Renumbering is eventually absent. The number of ALLOC_OWNER calls on a branch is at most the number of instructions
counted in (L1)-(L3) of Section 9, outside renumbering. By (P6) and (8.1) that number is at most 2^(c sqrt n). A
renumbering needs at least 2^EW - OWN - 1 generations since the start or since the last renumbering. Also
log(2^(c sqrt n)) = c sqrt n < (n+2)^20 - 1 for n >= c^2. So there is an absolute n1 such that no renumbering occurs
on any branch for n >= n1. For each of the finitely many lengths 2^40 <= n < n1 every branch is finite, because all
loops of P are bounded. So renumbering there changes only an absolute constant.

## 7. Correctness: the decoded classical-quantum invariant

An aligned point is any point between two P steps or acquisitions. Define a map pi from the physical state to P's
logical state at aligned points:
- decode the cells of every active owner through its epoch (Lemma 5.1);
- keep P's control position and bindings;
- map each slot that holds a live P qubit to that qubit, using the descriptors (injective by (I));
- map the wires of each store register ST[p] not yet transferred to ST[p] of P', qubit by qubit;
- trace out free slots, the |0> wires of transferred store registers, padding wires, tags, inactive owners, allocator fields and every other physical-only record.

OTP-LIMIT-BANK has no randomness of its own. Its staged decisions and every RAW_READ outcome are fixed functions of N and
of the outcomes of P's own measurements so far: by induction over steps, the basis content z of all bank wires and
staged bits is such a function, and a RAW_READ returns a bit of z. So at each aligned point the physical state is

    sum_z p_z |z><z| (x) rho_z,

where rho_z is a state of the mapped P qubits and of any reference system, possibly entangled and correlated with z,
and p_z is the probability of P's outcome history behind z. We show that pi(Phi_phys(X)) = Phi_P(pi(X)) for each step,
where Phi_P is P's channel for that step and Phi_phys is OTP-LIMIT-BANK's.

- Bank steps. On a state of this form, RAW_READ leaves the state unchanged and reveals a bit of z. RAW_WRITE maps z to
  a known z'. By Lemma 5.1 and Section 6, READ, WRITE, ALLOC_OWNER, FREE_OWNER and renumbering change the decoded
  record exactly as P's classical read, write, allocation or forgetting would. A forgotten staged bit mixes the
  conditional states rho_z as P's own forgetting does. By linearity this holds for arbitrary rho_z and references.
- Quantum steps. P's gate, measurement or reset on at most three qubits is applied to the slots holding those qubits.
  The classical controls of P's classically controlled gates are READ from the bank. LOOKUP is P's serial circuit,
  with table bits read from the bank. So, conditional on z, the action on rho_z is P's.
  In particular FW's PREP tries and steps 1-5 are applied gate by gate on the slots of A_0, ..., A_(w-1) and of its
  ancillas. By P Lemma 7.1(c), which holds for every input state, the instrument of P is realized on the mapped
  qubits whatever the correlations, and its measured cell code is recorded in the bank.
- Allocation and release. ALLOC_Q supplies a slot in |0> in tensor product with everything (by (I)), which is P's
  fresh qubit. FREE_Q applies reset, that is trace-out followed by |0>, to a qubit that P has just released, and pi
  forgets that qubit in both cases.
- Sources and the store. Each of the Q' acquisitions of ACQUIRE-ALL delivers a fresh copy into the (n+1)-qubit
  acquisition register. Its qubits are SWAPped, with three CNOTs per qubit, into the wires of ST[p], and the register,
  now |0>, is released. SHUFFLE's SWAPs act on store wires at addresses computed from i and j. A store transfer takes
  n+1 slots by ALLOC_Q and SWAPs ST[p] into them, leaving the store wires |0>. SWAP is exact, so the mapped qubits hold
  exactly what P' holds. Prefix zeros and metadata are not source copies.

By induction from P's initial state (input N, all scratch zero), the reduced logical state of OTP-LIMIT-BANK equals
P's at every aligned point, on every branch: extraction errors, returned and recycled FW outputs, failed merges, partial
children, rejected copies and aborts included. Its source-request sequence and its output law equal P''s.

The identity pi(Phi_phys(X)) = Phi_P'(pi(X)) holds for arbitrary states and references. So it holds with the
adversary's system as a reference, under every model-X adversary. Model X's timing clause is met: before the last
acquisition, the only outcomes are RAW_READs of bank wires, which are fixed functions of N. So by (P1)
OTP-LIMIT-BANK outputs s with probability at least 1 - 2^-8, for every N, s and adversary.

The held-out-bit argument of P Section 10, the coupling of P Section 5 and Lemmas B.1-B.3 are statements about the
logical law of P', which pi preserves. The extra RAW_READ outcomes are functions of P's outcome history, so conditioning on them adds nothing.

## 8. Classical and quantum space

S_C. OTP-LIMIT-BANK's ordinary classical storage consists of:
- the input N and the output, n bits each;
- constant many staged words of O(n) bits each (a RAW index or wire number, an owner, row and bit index, a slot
  number, an operand of a word operation);
- O(1) staged bits, and O(log n)-bit counters of the bit-serial loops;
- the finite control of the fixed program.

A wire number needs at most log(2h + Q'(n+1)) + 1 bits, which is at most 2r + 30 log n + 122 <= n by (8.2) below.

Before the prefix exists, the parameters are computed by streaming:
- C_0 by the recurrence from C_ell, with one current word of at most Y + 1 <= 2r + 1 bits and the counter i;
- then U, DRAW, HQ, h and the OTP parameters of (B.1), each of O(n) bits.

Once the prefix exists, the profiles are recomputed into the bank. The finite branch uses O(n) bits. So S_C = O(n) on
every branch.

S_Q. Bounds from P. By P Sections 8, 11 and 14, K <= 3 * 2^13 r, dl <= r and r^2 <= (sqrt n + 1)^2 <= 4n. Hence
C_ell <= 3 * 2^27 n^2 2^m and C_0 <= 8 RHO^ell C_ell <= 3 * 2^30 n^2 PP. Since r <= sqrt n + 1 and
beta + HI + 1 < 4, log PP <= beta sqrt n + 4. Likewise m + dl <= beta sqrt n + beta + 2 < beta sqrt n + 4.

Hence

    C_0 <= 3 * 2^34 n^2 2^(beta sqrt n),   U <= 2^36 n^2 2^(beta sqrt n).                 (8.1)

Bounds on the layout. These follow from (8.1) and EW + 1 <= 2^21 n^20 (n >= 2):
- HQ = 2^20 n^2 U <= 2^56 n^4 2^(beta sqrt n);
- LSPAN = 2^56 n^8 U <= 2^92 n^10 2^(beta sqrt n);
- DRAW <= 2^114 n^30 2^(beta sqrt n), since the terms after LSPAN (EW+1) in (4.1) are O(n^22).

By (4.2),

    S_Q <= 2h + Q'(n+1) + n + 1 <= 5 DRAW + n + 1 <= 2^117 n^30 2^(beta sqrt n),         (8.2)

This uses HQ + 2 <= LSPAN <= DRAW, so that h < 2 DRAW. It also uses
Q'(n+1) <= 208 r * 5 n C_0 * 2n <= 2^12 n^3 C_0 <= LSPAN, by (B.2) and r <= n.

This counts every physical wire: bank values, tags, epochs, flags, RAW scratch, every slot (live, free or never used),
the padding up to 2h, the whole store (acquire-all) and the acquisition register. It is a fixed span, the same on every
branch. The finite branch uses Qf(n+1) + O(n) qubits, an absolute constant. So S_Q = O(n^30 2^(beta sqrt n)).

## 9. Explicit polynomial ledger

Every core step of OTP-LIMIT-BANK pays its address fee ADDR = ceil(log(S_C + S_Q + 2)), and ADDR <= n by (8.2). An
instruction is one of the following:
(i) a logical READ or WRITE;
(ii) a RAW_READ or RAW_WRITE;
(iii) a bit operation on staged words;
(iv) one gate, measurement or reset of P on mapped slots;
(v) an ALLOC_Q or FREE_Q, or a descriptor field update;
(vi) an ALLOC_OWNER or FREE_OWNER;
(vii) one acquisition, with its SWAP into the store; or one store transfer (n+1 ALLOC_Q with descriptor updates and
      the SWAP into the slots).

(L1) Control completion: at most c n^4 instructions per P step.
- A P step touches at most three classical bits or three qubits.
- Locating a classical bit takes the owner of its array (a field of the current frame row) and its row and bit index
  (O(n)-bit words held by P). Forming (3.1) and the RAW index (EW+1)c takes O(n^2) staged bit operations.
- Locating a qubit takes one slot number from a descriptor field, or, for a store qubit, the O(n^2) staged bit
  operations of 2h + p(n+1) + t.
- Bookkeeping. P is a fixed program with s0 statements, s0 an absolute constant. Let D <= c(m+2) bound the
  iterations and calls open at once (bounded static nesting, recursion depth m+1). Every innermost body consists of
  P steps, so every opened iteration or call runs at least one P step. Charge each control event to the first P step
  of the innermost context containing it. The events are: counter update and test, frame push or pop, the at most s0
  allocate/free statements of a body (ALLOC_OWNER and FREE_OWNER, instruction (vi); slot operations are wire events,
  counted in (4.3)), and the at most s0 loop-exit tests of a body. A P step is the first step of at most D contexts,
  each charged at most 2 s0 + 2 events of at most 13n instructions. So bookkeeping is at most c' n^2 instructions per
  P step.

(L2) Cost per instruction: at most c n^24 charged bit operations, which is at most n^100 for n >= n1, where we also
take the threshold n1 of Section 6 to be at least c.
- (i): 2EW + 1 <= 2^22 n^20 RAW accesses (EW tag bits, EW epoch bits and the value bit). Each access is one core step
  plus ADDR, plus an O(n)-bit increment of a RAW index, which is O(n) staged bit operations with their fees; so each
  access costs O(n^2). Add O(n^2) staged bit operations of address arithmetic, each of cost at most c n. At most
  c n^22.
- (ii), (iii) and (iv): at most c n.
- (v): three O(n)-bit fields (head, NEXT[k] and virgin), or one descriptor row (a slot number of at most n bits), so
  O(n) logical READs and WRITEs, plus one reset. At most c n^23.
- (vi): a scan of OWN flags (OWN RAW accesses, c n^4), the all-ones test, the increment and the copy of G (at most
  5 EW RAW accesses), and a binding of O(n^2) RAW bits. At most c n^22, plus Section 6 if it is triggered.
- (vii): the source cost n+1, then 3(n+1) CNOTs with fees, and n+1 ALLOC_Q with descriptor updates. At most c n^24.

The bounds n^4 and n^100 are the degrees used by mpjunior92. The items above show that they hold with room.

(L3) Wire events. By (4.3) there are O(n^16 (C_P' + Q' + HQ + 1)) of them, each of cost at most n^100 by (L2).

(L4) Prefix. HQ + 2 <= LSPAN <= DRAW, so h < 2 DRAW, and Q'(n+1) <= DRAW (Section 8). Allocating wires
0, ..., 2h + Q'(n+1) - 1 in |0>, writing head := HQ, and at the end resetting and releasing them costs at most
c n (2h + Q'(n+1)) <= c n DRAW. The streamed parameter computation and the profiles cost poly(n), which is
included in the next display.

Total. Take n >= n1, so that no renumbering occurs (Section 6), and any branch. The charged work is at most the sum
of four terms:
- c n^4 C_P' instructions from (L1), each of cost at most n^100;
- O(n^16 (C_P' + Q' + HQ + 1)) wire events, each of cost at most n^100 (L3);
- Q' acquisitions and at most Q' store transfers, each of cost at most n^100;
- c n DRAW for the prefix, plus poly(n) for the parameters (L4).

Allowing (L1) a second factor n^4 of slack, so that n^4 * n^4 * n^100 <= n^120,

    T <= c n^120 (C_P' + Q' + HQ + 1) + c n^100 DRAW.                                      (9.1)

The derivation above gives c n^28 per P step and c n^24 per wire event, far below these degrees. For 2^40 <= n < n1,
and on the finite branch, the work is bounded on every branch, so these lengths change only the constant.

## 10. Time and samples

T. Substitute (P6), (8.1) and Section 8 into (9.1):
- C_P' = O(n^6 2^(beta sqrt n)) (Section B.8) gives degree 126;
- Q' = wo Qcap = O(n^(7/2) 2^(beta sqrt n)) gives degree 123 + 1/2;
- HQ = O(n^4 2^(beta sqrt n)) gives degree 124;
- DRAW = O(n^30 2^(beta sqrt n)) gives degree 130.

So

    T = O(n^130 2^(beta sqrt n)),   hence   T = O(n^130 2^((2887/2500) sqrt n)).

The power 130 is the largest of these four degrees. The coefficient beta = 57739/50000 is exact. On the tree side,
m + dl <= beta r + 2 follows from P's integer schedule (57747/100000 + 57731/100000 = 57739/50000). On the pool side,
log PP <= beta r + HI + 1 uses P's bracket log2 RHO < HI, which P proves from the series of ln 2, and the exact
inequality HI (2309/4000) + 57747/100000 < beta (P (8.5)). Initialization, ACQUIRE-ALL, SHUFFLE, every BLOCK, every failed or
recycled branch, every abort, all bank, descriptor, slot and store work, the source moves and the output-first cleanup
are included.

Q. OTP-LIMIT-BANK makes exactly the Q' acquisitions of ACQUIRE-ALL and none other (Section 7). They include every copy
of every block, of every rejected copy-equivalent, of every FW-stage, supplier and pool abort and of every discarded
merge input (P Section 13), and every store register left unused. By (B.2), r <= 2 sqrt n and (8.1),

    Q = Q' = wo Qcap <= 416 sqrt n (3 * 2^36 n^3 2^(beta sqrt n) + K) = O(n^(7/2) 2^((2887/2500) sqrt n)).

The finite branch uses Qf = N(n+10) 69 (2n+15) copies, a constant over its finitely many N. Bank zeros, tags, slot
bookkeeping, SWAPs and renumbering are charged as work and storage, never as copies.

## 11. Growth indices

For fixed c > 0 and fixed a >= 0, log(n^a 2^(c sqrt n)) = c sqrt n + a log n. Then
log log max(4, n^a 2^(c sqrt n)) = (1/2) log n + log c + o(1), and the index g = 1/2 exactly. This holds for each of
the declared envelopes of T (a = 130, c = 2887/2500), S_Q (a = 30, c = 2887/2500) and Q (a = 7/2, c = 2887/2500).
For S_C = O(n),
log log max(4, n) = log log n, so g = 0. The indices are those of the proved upper envelopes; no lower bound is
claimed. The structured objects in submission.json are exactly these four envelopes.

## 12. Error tolerance

The fifth claim is epsilon(n) = 99/100 under model X (Section A), for every N >= 2, with no threshold: of the Q
acquired copies, at most floor(99Q/100) are malformed. By Section B.6 and Section 7, for every N, s and every such
adversary, including the one that corrupts nothing (the clean problem), OTP-LIMIT-BANK outputs s with probability at
least 1 - 2^-8 > 2/3. This holds jointly with the four bounds above. Those bounds hold on every branch for every
adversary, because they rest only on caps and fixed allocations, never on the contents of the copies.

Theorem B.4 holds for every fixed eps0 < 1. The value 99/100 is a round constant, not a tuned one. Nothing is claimed
for corruption outside V_s, or under any other error model.

## 13. Scope and limitations

- Model X excludes every coin error: coin dephasing, phase flips and Regev's registers. Nothing is claimed under any
  model admitting them, and we do not claim that unmodified P fails under model X. Its scope is coherent label steering
  with an exact coset relation, which contains the |+> (x) chi_0 attack on the exhaustive baseline (Section A).
- The OTP layer multiplies Q by wo = O(sqrt n) (n-power 3 -> 7/2) and adds Q'(n+1) store qubits. S_Q keeps its
  power 30 because the bank prefix dominates. Theorem B.4 applies to other label-first bases, and a stronger base
  gives a stronger row.
- The time growth index is 1/2, as for P and the earlier versions of this construction. The research goal
  2^(O(n^(1/3))) is not reached. Against our TRIAD-BANK (156/125 on T and S_Q) and the HPC-127 version with explicit
  degrees (4950737/3900250, about 1.26934), the declared coefficient is 2887/2500 = 1.1548 on T, S_Q and Q, with
  polynomial powers 130, 30 and 7/2 and S_C = O(n). As motivation only (not claimed or used): the pool constant of this rule tends to 2/sqrt 3 = 1.15470 as w grows.
- The memory construction is not ours (Section 1), and the cell family has prior odd-size versions on the board
  (Section 1). What this file adds is its application to F-LIMIT and the check that P's FW-based pool exposes the
  interface it needs.
- S_Q is 2^(Theta(sqrt n)), because classical records are moved into counted qubits. This is not an improvement over
  algorithms with O(n) or 2^(o(sqrt n)) qubits.
- All polynomial powers, the threshold n >= 2^40, the group size w = 2^28, FW's gate and scratch constant c_F and
  the tag width (n+2)^20 are unoptimized.
- P's own statements in virtual.md (its header and its Sections 0, 14, 15 and 16) concern P's storage model, in which S_C is exponential.
  The four bounds and the tolerance 99/100 of this file concern OTP-LIMIT-BANK.
