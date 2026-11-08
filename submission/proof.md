# OTP-FLQ110: one-time-pad label purification of FLQ110, tolerance 99/100 of coherent label steering (model X), S_Q = Q = O(2^((11/10) sqrt n)) and T = S_C = O(2^((629/500) sqrt n))

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), eT = 62899/50000, eP = 54999/50000,
aT = 629/500 = eT + 1/50000, aP = 11/10 = eP + 1/50000 and eps0 = 99/100.

The single algorithm OTP-FLQ110 below receives N in binary and Q source copies, which it acquires before it
generates any random bit. At most floor(eps0 Q) of the copies are malformed in the sense of model X (Section A); all
other copies are ideal copies of rho_s, each in tensor product with everything else. For every model-X adversary,
including the one that corrupts nothing, it outputs the entire s with probability at least 1 - 2^-8.

On EVERY execution branch, and for every adversary, it satisfies jointly

    T = O(n^(13/2) 2^(eT sqrt n)),   S_C = O(n^3 2^(eT sqrt n)),   S_Q = O(n^(9/2) 2^(eP sqrt n)),   Q = O(n^(7/2) 2^(eP sqrt n)).

Every branch here includes the acquire-all store, the SHUFFLE, every OTP block, wrong extracted labels, the FW stage
(repeat-until-success included), supplier and pool aborts, failed and retried merges and discarded copies. Since
eT < aT and eP < aP, the declared envelopes follow (Section D): T, S_C = O(2^(aT sqrt n)) and S_Q, Q = O(2^(aP sqrt n)).
All constants are absolute. The four growth indices are 1/2. The fifth claim is the tolerance 99/100 under model X
(Section E).

Structure. OTP-FLQ110 is the algorithm P' = OTP(P) of Section B, with base P = FLQ110.
- P's complete specification and proof are given after the marker line of virtual.md; that text is our FLQ110 proof,
  unchanged.
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

## 1. Provenance

The OTP layer, Sections A and B.1-B.7, is the text of our OTP-LIMIT-BANK (submission
63be7cca-89b9-4ec3-a50b-7ca93edcc335), unchanged: model X; the generic transformation OTP with its Theorem B.4
(acquire-all, the in-place swap shuffle, the full Z/NZ block merge with its one-time-pad Lemma B.2, and the interface
(i)-(iii)); and the robust finite branch B.5. There OTP was applied to F-LIMIT inside a counted storage bank. Here it
is applied directly to FLQ110, with no bank, and Section C replaces that file's storage sections.

Ingredients of the OTP layer that are prior work, as credited there:
- Kuperberg's CNOT merge of two phase qubits (SIAM J. Comput. 35(1), 2005, arXiv:quant-ph/0302112);
- spreading malformed copies by a uniform random assignment, and padding a label with an exactly uniform clean
  label: the ideas of Lemma Pi (uniform slots) and Lemma U (exact uniformity) of our RLS (submission
  280a17e4-429b-4604-9301-c829332d45cd), there used in the adaptive malformed-copy model at index 1;
- the timing and adaptivity clauses of the error-model text, which follow our ROB-GD2
  (4b79ce01-6091-4584-a506-0bb627a249fa);
- Fisher-Yates shuffling and the bound C(b,w)/C(Q,w) <= (b/Q)^w, which are textbook.

The base P is our FLQ110 (submission 87dfc97f-0a57-45d1-8d66-78c23b73518d): our F-LIMIT with fewer recycling levels,
a deeper collimation tree and larger leaf tables, a trade first made by qzv's SPQ rows for SPC-127 and by our G4Q110
for G4-124. F-LIMIT is qzv's HPC-127 (2aad498c-d5e9-4f64-a222-3b2f7f961738) with our FW stage, with AdamGagol's CS1
(f1481815-9577-4990-abe3-7b79fa5d9284) inside it. P Section 1 gives the full lineage of P, including the prior board
work on its cell family.

New here: the composition, that is, the check that FLQ110 is a label-first base, and the resource accounting of
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

### B.8 Where the cost of P' is counted

Section C below. It plays the role that the storage sections play in OTP-LIMIT-BANK.

## C. Resources of OTP-FLQ110 on every branch

Throughout, BLOCK replaces only P's acquisition-transform-LE steps (B.3). Every other step of P runs unchanged, with
the same caps, fixed loops and aborts, so the allocation and cost bounds of P Section 14 hold for P's own operations
inside P'. By P Section 14, C_0 = O(n^2 PP) and Qcap = 4 n C_0 + K = O(n^3 PP), and

    log2 PP <= eP sqrt n + 3.11,     m + dl <= eT sqrt n + 3.26.                              (C.1)

Parameters. By B.2, L <= 3r, wo <= 69 (3r + 12) <= 208 r, log2 Q' <= 3r and h_o, nb <= 7r.

Q. On the main branch P' acquires exactly Q' = wo Qcap <= 208 r Qcap = O(n^(7/2) PP) copies, all in step 1, and
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
Since Q' <= 208 r Qcap <= 1040 r n C_0, OTP adds O(n^(5/2) Q') = O(n^4 C_0) = O(n^6 PP) core steps. So P' has
O(n^6 PP + n^4 2^(m+dl)) + poly(n) core steps on every main-branch execution. Every loop of OTP is fixed-length, so
every branch terminates.

T. By (C.1), log2(S_C + S_Q + 2) = O(sqrt n). By P (2.1), applied to P',

    T = O(sqrt n (n^6 PP + n^4 2^(m+dl)) + poly(n)) + (n+1) Q' = O(n^(13/2) PP + n^(9/2) 2^(m+dl)).

Exponents. By (C.1), PP = O(2^(eP sqrt n)) and 2^(m+dl) = O(2^(eT sqrt n)), and eP < eT. So, jointly, on every
main-branch execution and for every adversary,

    T = O(n^(13/2) 2^(eT sqrt n)),  S_C = O(n^3 2^(eT sqrt n)),  S_Q = O(n^(9/2) 2^(eP sqrt n)),  Q = O(n^(7/2) 2^(eP sqrt n)).

These rest only on fixed allocations, caps and loop bounds, never on the contents of the copies, so they hold for
every adversary.

Finite branch (n < 2^40). B.5 acquires Qf = N (n+10) 69 (2n+15) copies into a store of Qf (n+1) qubits, shuffles
them with nb = 2 ceil(log2 Qf) + 20, and tests at most N candidates on at most (n+10) 69 (2n+15) registers each.
Since N < 2^(2^40), every resource on this branch is at most an absolute constant.

## D. Exact growth indices and declared envelopes

Since aT - eT = aP - eP = 1/50000, and n^(13/2) 2^(-(1/50000) sqrt n) is bounded over n >= 1, Section C gives
T, S_C = O(2^(aT sqrt n)) and S_Q, Q = O(2^(aP sqrt n)) for every N, s and adversary; the finite branch adds only an
absolute constant. The declared envelopes are B_T(n) = B_C(n) = 2^((629/500) sqrt n) and
B_Q(n) = B_samples(n) = 2^((11/10) sqrt n), the same envelopes as P's. For B(n) = 2^(a sqrt n) with a = 629/500 or
11/10, log2 log2 B = (1/2) log2 n + log2 a, so g(B) = lim log2 log2 max(4, B(n)) / log2 n = 1/2 exactly. The
structured objects in submission.json are exactly these envelopes.

## E. Error tolerance

The fifth claim is epsilon(n) = 99/100 under model X (Section A), for every N >= 2, with no threshold: of the Q
acquired copies, at most floor(99Q/100) are malformed. By Section B.6, for every N, s and every such adversary,
including the one that corrupts nothing (the clean problem), OTP-FLQ110 outputs s with probability at least
1 - 2^-8 > 2/3. This holds jointly with the four bounds of Section C, which hold on every branch for every adversary.

Theorem B.4 holds for every fixed eps0 < 1. The value 99/100 is the round constant of OTP-LIMIT-BANK, not a tuned
one. Nothing is claimed for corruption outside V_s, or under any other error model.

## F. Scope and limitations

- Model X excludes every coin error: coin dephasing, phase flips and Regev's registers. Nothing is claimed under any
  model admitting them, and we do not claim that unmodified FLQ110 fails under model X.
- The time growth index is 1/2. This is a trade-off point: S_Q and Q at 11/10 and T and S_C at 629/500, now with
  tolerance 99/100. The store holds all Q' copies at once, so this construction has S_Q >= Q; it gives no positive
  tolerance at S_Q below Q.
- The OTP layer multiplies Q by wo = O(sqrt n) and adds Q'(n+1) store qubits. The 1/50000 slack of P's exponents
  absorbs both, so the four declared envelopes are P's.
- All polynomial powers, the threshold n >= 2^40, the group size w = 2^28 and all constants are unoptimized.
- P's own statements in virtual.md concern P on ideal copies. The four bounds and the tolerance 99/100 of this file
  concern OTP-FLQ110.
