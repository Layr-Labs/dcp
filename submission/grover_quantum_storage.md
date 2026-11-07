# PSG2-QSTORE: the clean Dense algorithm with a measured basis store

## 0. One physical algorithm and its joint theorem

For every integer N>=2 and every secret s in Z/NZ, put n=ceil(log2 N)
and L=log2 n when n>=2. PSG2-QSTORE is the single physical simulator
specified in Section1 and the complete transfer appendix. It returns the
whole secret with unconditional probability at least1-2^-8>2/3. Its
simultaneous resource bounds on EVERY execution branch are

    T=O(2^((177/250)sqrt(nL))),
    S_C=O(n), S_Q=O(n^2),
    Q=O(2^((177/250)sqrt(nL)
             -(5/32)sqrt(n/L)-(1/2)(nL)^(1/4))).       (Q0)

All outside constants are absolute and independent of N,s and outcomes.
The displayed T/Q representatives apply for n>=2; the same simulator
executes the explicit finite virtual branch for n=1 without dividing by L.
Their exact growth indices are1/2,0,0,1/2 in T,SC,SQ,Q order. Only time
has the numerical objective. These are proved upper bounds, not matching
runtime lower bounds or a claim of general novelty or a new best point.

The source consists of fresh independent ideal copies of

    rho_s=(1/N) sum_(x=0)^(N-1) |psi_(x,s)><psi_(x,s)|,
    |psi_(x,s)>=(|0,x>+|1,(x+s)mod N>)/sqrt(2).

The value x, purification, inverse preparation and coherent source control
are unavailable. Tolerance is0 in the exact clean model reproduced in
Section4. No positive malformed-copy or adaptive transfer is asserted.
Every copy costs n+1 and every attempted/discarded source copy is counted.

## 1. Complete selected physical algorithm

Let P be virtual Dense as completely specified in the six virtual proof
appendices in Section2. Its actual source guard is Qcap_dense with the
rational minimum; Qcap_old retains only its stated precision/analysis role.
Its weighted guard is Wcap. Its least feasible retained profile, dense
arity b+5, list2048, rank11 cyclic instrument, exact grouped G1, finite
branches, strided decoder and source extraction are exactly the complete
virtual instructions. No different nominal or displayed envelope replaces
an operational cap.

Run the following one physical interpreter, not P's original physical
classical allocation. All its exact bit/channel/counting details are in
[the complete transfer proof](grover_quantum_storage_transfer.md).

1. Read N on the counted classical input tape. Compute the public fixed
   region/subregion bases from n. Use the transfer's nine padded classical
   virtual regions, five linear quantum virtual regions and fixed finite
   bit-controller code. All original maps, counters, program, recursion
   frames, labels and metadata belong to those virtual regions.
2. Store virtual classical bit i in basis qubit2i. Store virtual quantum
   wire q at wire2(q+1)+1. Reserve wire1 as one fair-bit scratch qubit.
   Start paired prefix size h=2 and double it before a required slot would
   exceed it. Allocate/initialize every new prefix wire. Retain and count
   the whole prefix, including unused padding. The region capacities are
   public analytic bounds, and retries reuse fixed slots.
3. Execute P's finite bit-control program. Read a bank value by Z
   measurement at its decoded classical address. Write by reading its old
   value and applying X exactly when it differs from the new bit. Long
   arithmetic and program construction remain loops of these bit actions.
   Decode every actual instruction/tag/operand/marker field through the
   same measured interface. A fixed number of short classical words holds
   the decoded fields, finite control and head locations. There is no
   physical classical call stack or duplicate large record.
4. Execute every P quantum gate, measurement, reset, discard and fair bit
   through its exact mapped interface. Controlled Grover/G1 gates remain
   coherent on P's quantum data. No bank address is quantum coherent.
   For every virtual source request acquire exactly one physical source
   copy, move it to the mapped slot by counted SWAPs if needed, and release
   the now-zero temporary source wires. There is no source call in an
   inverse or in a bank initialization.
5. Check each virtual acquisition/weighted guard at its original point.
   Follow every original retry, failure, partial construction and abort
   branch, including output0 when P aborts. Extra physical simulator work
   is separately bounded and fully counted; it is not deleted from T or
   falsely charged to an old nominal guard.
6. When P has its final classical residue, stream it from the bank into
   the counted O(n)-bit physical output field. Then clear/release the
   prefix and short temporary fields. Return the saved residue. Both input
   and output storage are included in physical S_C.

Every memory, Boolean, pointer, carry, address, tag, loop, gate, measurement,
initialization, source move, inverse word, reset and failure action is
ordinary counted work. Fixed Clifford+T words implement all quantum gates;
no coherent memory lookup, QRAM, preloaded instance advice or hidden
compiler is supplied. The bank channels are defined on all inputs; the
simulation theorem uses the proved reachable CQ invariant and does not
assume unitary behavior on a superposed classical store.

## 2. Complete virtual source proofs and scope

The following six required appendices reproduce ALL actual Dense proof
content. Each has an explicit scope header: every copied allocation,
resource, controller and physical-implementation statement refers only
to virtual P. Its original SC=O(n^2),SQ=O(n) statement describes the
virtual storage being simulated. It is not this package's physical bound.
Local proof filenames alone are rebound; no source mathematical argument
is removed. The new physical resource conclusions are (Q0) and the
complete transfer proof.

| Current required proof | Full contents |
| --- | --- |
| [Virtual main](grover_quantum_storage_virtual.md) | Complete original algorithm, exact source transforms, source-label extraction, supplier, fresh-label law, both decoders, finite cases, success/guard and full resource proofs |
| [Virtual caps](grover_quantum_storage_virtual_caps.md) | Exact selected probability/source/cap binding, numerical roles and chronology |
| [Virtual oracle](grover_quantum_storage_virtual_oracle.md) | Complete exact grouped G1, retained history, allocator, gate constructor and integration |
| [Virtual compiler](grover_quantum_storage_virtual_compiler.md) | Complete bit-level helpers, stored instruction tape, forward/inverse interpreter, full RUN(F), remaining-work and inherited credits |
| [Virtual dense proof](grover_quantum_storage_virtual_dense.md) | Full cyclic instrument, first/second moments, bounded discovery, product/frequency, fresh conditional law, actual guard and every-branch cost |
| [Virtual rational bound](grover_quantum_storage_virtual_bound.md) | Complete strict283/400 profile certificate,177/250 envelopes, finite-prefix and exact source corrections |

These files are required proof content, not accepted-result or external
parent oracles. Their historical statements and source pins retain their
provenance meaning. Every direct/inherited source credit in the original
Dense package remains included. No old JSON is included as a current claim.

## 3. Correctness and all physical resources

Transfer Sections3--4 give the explicit fixed region map. Each of nine
classical regions has capacity C_t*2^(2ceil(log2(n+2))) for a fixed public
power-of-two constant. Fixed subranges use public analytic capacity bounds;
no maximum over runtime histories is computed. All addresses, metadata,
operand words, heads, constructor copies and stack frames use that same
map. Prefix bases never advance with a retry. The five quantum virtual
regions use fixed linear capacities. Thus the complete physical paired
prefix is O(n^2), including its unused padding and original quantum data.
Input, output and a constant number of O(log n)-bit physical address/control
words use O(n) classical bits. The finite simulator code is constant size.
This proves SC=O(n),SQ=O(n^2) jointly on all branches.

Transfer Section7 proves that the bank and live registers are a CQ mixture
over P's classical records. A measured bank read is nondisturbing on each
conditional live state, even with arbitrary references and correlations
with the stored labels. Writes, forgotten classical outcomes, original
quantum operations, reset/release channels and fresh independent source
deliveries reproduce P's reduced channel. No unknown state is copied.
The full output law is P's, with exactly its source-request sequence.
The complete virtual proofs therefore give full-secret probability at
least1-2^-8 and unchanged Qcap_dense and Q envelope, for every N,s.
No success or clean-label event is used to bound resources.

Transfer Sections5/8 count O(a^2) charged work for one virtual bit/head,
indexed-access or fixed-arity quantum action, including all operand-word
scans and full address fees, with a=O(log n). Source moves fit that
allowance times their n+1 original charge. Complete prefix initialization
and final output-first cleanup cost O(n^2a^2). Consequently

    T_physical=O((T_P+n^2)*log2(n+2)^2).

The complete virtual main/compiler/dense resource proofs establish the
stronger internal bound T_P=O(n^2 L log2(L+2)2^R), not merely its final
pure exponential. Transfer Section9 therefore proves

    T_physical=O(n^2 L^3 log2(L+2)2^R).

For L>=65536, the complete virtual rational proof gives
R<=ceil((283/400)sqrt(nL)) and3L<=(1/2000)sqrt(nL).
The new prefactor has logarithm at most2L+4log2 L<=3L. The exact gap
177/250-283/400=1/2000 absorbs it. The same capped algorithm/simulator
covers the remaining finite prefix with one absolute outside constant.
No new execution threshold or operational parameter is selected. This
proves the T bound in (Q0) while retaining its source corrections exactly.

The two exponential envelopes have growth index1/2 because the source
corrections are lower order than sqrt(nL); n and n^2 have index0.
The complete logarithmic limits are in the transfer and virtual bound.
The current JSON records those exact representatives for this one physical
algorithm, without combining different memory configurations.

## 4. Exact clean model and its limit

The fifth claim uses precisely this168-byte model string:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The fraction is0. Every copy is independent and ideal; the guarantee
includes every N>=2 and every secret. Source count includes all failed,
rejected, discarded and aborted attempts. The interpreter's fresh zero
bank qubits are counted physical qubits, not DCP copies. The full output
probability is unconditional.

Extra bank measurements could expose stored record bits to an adaptive
supplier that observes every actual outcome. This package proves no
transfer for such a supplier. No positive tolerance or impossibility of
greater tolerance follows from the clean theorem.

## 5. Direct sources and actual chronology

The complete virtual algorithm comes from Dense,
e2d3ffa5-7cea-4cf3-a9f8-9b9d75a2f75a, immutable commit
40bb93be85e7a9ed53244dbdd4157af7d170f68e. Its actual six proof members
and declaration were checked against the exact uploaded bytes and public
Git blobs. The local source was used before its later publication and
later public-byte check. Public compiler75234b55e8409a86bf1afc5e2ce989c69898fd54d9f49b2b0031cd1bcc2eb3ac
is the original local compiler8864034e983327b8a5d33d9297093779e3d877649dbb5d8dd4d2055a46495e8e
with exactly one terminal LF removed. This exact format identity changes
no instruction or proof. All source hashes and inherited credits are
reproduced in the transfer/virtual proofs. A public verdict is not a
mathematical premise or an ancestry certificate.

The coordinator proposed this direct Dense layout before the later
saved-list discovery of PSG21,9fdfdb12-834d-441c-8bb1-717ab380abf3,
commit05f0ab81b2cc641c7a917ed56dffb3204688e795. Its exact proof hash is
43e2ac8f392a5301733dbb393088588641b06c3345864d83002f123a6de3830f.
The coordinator then read Sections B--D; this author read the actual full
proof. PSG21 directly supplies prior generic measured-basis read/write,
CQ coupling, clean-model limitation and overhead methodology, all fully
reproduced here. Its parent.md was neither read nor adopted. Its parent
algorithm or theorem supplies no premise of this package.

PSG21 stores a key and flag for each live bit and scans those records.
This algorithm instead uses the proved fixed Dense regions and direct
indexed wire arithmetic, with no added per-cell keys/flags. It proves
its own O(n^2)-qubit capacity and O(log^2 n) overhead before using Dense's
strict internal margin. The generic simulation idea is not claimed new.
No broad novelty, frontier or new-best claim is made.

## 6. Complete current evidence

All five claims cite this physical main, the complete physical transfer
and all six complete virtual proof appendices. Required arguments are
inside this candidate. The current claims are only for PSG2-QSTORE's
physical implementation. Historical Dense/compiler assertions are scoped
to virtual P. No local audit, omitted research note, unavailable parent,
acceptance or review verdict replaces a construction or proof.
