# GPS-BLOCK-BANK: signed multibit collimation with linear classical storage

For every N>=2 and s modulo N, n=ceil(log2N), ONE uniform physical algorithm
recovers the ENTIRE secret with unconditional probability at least1-2^-8.
Jointly on EVERY branch, including every failed/discarded attempt and abort,
its bounds for n>=2 are

 T=O(n^(5/2)(log2n)^(7/2) 2^(a sqrt(n log2n))),
 SC=O(n), SQ=O(n^2), Q=O(2^(a sqrt(n log2n))),
 a=176777/250000, epsilon(n)=0.                            (0.1)

The four growth indices are1/2,0,0,1/2. The finite n=1 program has bounded
absolute costs. SQ counts ALL allocated basis-bank qubits, coherent work,
padding, unused slots and raw temporary source wires. This is a physical
implementation tradeoff, not identification of virtual classical bits with
free quantum storage. All constants are independent of N,s and outcomes.

## 0. Exact material sources and present scope

The logical program V is EXACTLY GPS-BLOCK,
71412e04-4a62-4db8-a3be-ff505bef4cd8, published commit
7fa065113979996f7cfed57b92517bbe106ce614. Its COMPLETE self-contained1113-line
main is copied unchanged as gps-source.md, SHA-256
3016a821fcc6ae313f0156326e1ca1f7de2f240c18d07bba70eb0db7859519f7.
All its extraction, tree, conditional signed-leaf, decoder, four-cutoff,
finite-branch and branchwise resource arguments are included, not delegated
to a missing predecessor. Its GPS-HALF/GPS-VLE/GPS-C3/CS1/GPS3 and upstream
credits remain intact. No outside ancestor feature is separately imported.

The directly used physical method is the complete directly addressed
SPTS-JM-BANK main of057bc5a2-6358-428a-9cf6-85b9c45a478b, commit
231df65af68a16d2684fd9cc6613c4eeffa93868, copied unchanged as
bank-interpreter-source.md, SHA-256
26b64d6eb0471b0e73a66164c39c03d9a5954d9cad120a52729fdd50a2467298.
Its Sections2-4 prove the finite direct-address bit interpreter, counted
paired allocation, O(w^3) per-bit overhead and full-reference CQ method.
Those are re-established for V below. Its old SPTS algorithm, old log-six
time and one-third input theorem are NOT the current program or promise.
Historical helper/archive paths inside that exact source describe ITS
archive, not missing mathematical obligations here. This main supplies the
whole selected interpreter/layout/channel argument self-contained.

These two directly used features are distinct: the full current signed
sieve program and the directly addressed measured-bank method. Neither is
claimed newly invented or independently authored here. The contribution is
a concrete same-output physical implementation and its actual joint ledger.
Earlier review, publication, diagnostics and provisional graph references
are not mathematical premises or certificates of ancestry.

## 1. Exact input, unchanged logical algorithm and source guarantees

The fifth structured object uses EXACTLY the canonical clean-source text:

"Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies."

Thus every acquired original is an independent rho_s. No positive
corruption tolerance or claim of optimal tolerance is made. There is no
interactive supplier, purification access, source control or inverse.
Source-held copies not yet requested are excluded from accessible workspace
by the challenge rule. Independent ideal copies may equivalently be supplied
from a fixed product bank in passive order. Extra implementation readouts
never select a replacement source or become new feedback to a supplier.

For n<256, V is EXACTLY the source's bounded exhaustive shift-testing program,
including its n+10 tests, first-passing tie rule and abort/output convention.
For n>=256 use ALL source rules literally. Compute the least integer R>=2
with S(R)>=n-1, with Delta=2ceil(log2(4R)), m=floor((2R-2)/Delta)+1,
v_i=2R-1-(m-i)Delta, q0=product(v_i+1), G=2^m q0. Do not change widths,
profile, count constants or any actual cap to match a displayed envelope.

The logical program has the source's verified translation-label EXTRACT,
private signing, depth-first PS_TREE(D,B), explicit fixed-schedule Grover
pair instrument and above-half conditional return. The odd part uses the
signed multiple-untouched-bit decoder when h>=8, otherwise its specified
unsigned small-mode decoder. The 2-adic part uses the same shifted sources
and fair-parity measurement. All CRT arithmetic, tables, exact Clifford+T
words, searches, measurements, finite loops and streaming candidate grids
are the source's. No new phase or preparation oracle is substituted.

In particular the four hard cutoffs are unchanged: original acquisition
Qcap=1024(2G H0+2n), weighted attempts Wcap=1024(2m2^R H0), high-confidence
fallback Cf=ceil(Qcap/ceil(sqrt n)), and root frequency |W|<=nq0. H0,Smax,K
are EXACT source formulas. The weighted guard occurs AFTER its children
have been built; those acquisitions/work remain counted. A refused source
call acquires no additional original. All source aborts release and output0.
No physical interpreter step restarts V or resets a logical counter.

The complete source proves the following simultaneous facts, with its own
actual instructions and private-record exclusions:

* Exact source decomposition gives independent uniform latent Fourier labels;
  extraction coupling costs at most2^-14+2^-20 without conditioning on a
  numerical label being correct or on future cap survival.
* Routing inspects low residues, not the separately discarded unsigned label,
  sign or extraction-private transcript. The untouched signed high parts
  keep the proved conditional product laws in the unguarded ideal process.
  The deterministic occupancy inequality gives attempt success>1/2.
* Untouched high parts give the stated Dirichlet characteristic bound and
  signed root tail2exp(-n^2/8). The frequency guard is omitted in that ideal
  proof and coupled separately, never used to postselect that law.
* Root demand is O(n), all four actual caps bound EVERY execution branch,
  and full-secret failure is at most
  2^-10+2^-10+2^-14+2^-19+2^-20+2^-20<2^-8. The finite branch also qualifies.
* All retained labels, fields, counters, frames, exact arithmetic, instruction
  generation and decoder records use O(n^2) classical bits; all retained
  source-phase qubits plus shared scratch use O(n) genuine qubits.

These are supplied proved mathematics in gps-source.md Sections2-9, not
assertions extracted from an old score. Section9.4 establishes a useful
more precise CORE ledger BEFORE multiplying by the global address fee:

 A_V=O(n^(5/2)(log2n)^(1/2)2^R)                           (1.1)

for the number of expanded Boolean bit actions, actual elementary gates,
measurements, source fees, generation and loop/counter actions. Its terms
are O(R^2 Wcap), O(nmQcap), O(n^2 log n Qcap), streamed decoder work and
O(n^6) public preprocessing, exactly as proved there. It explicitly includes
generation and failures. It is not quantum work alone. The old full charged
T_V multiplies (1.1) by O(log n); we will instead pay OUR complete physical
cost per such core action, without dropping either address/generation cost.

The source also proves Q<=Qcap=O(n^-8 2^R), in particular O(2^R), and
2^R=O(2^(a sqrt(n log2n))) with EXACT rational a in (0.1). Its explicit
large threshold n>=2^16777216 and all finite smaller input lengths are
part of that uniform theorem. None of its lower-order factors is silently
absorbed as a constant on an unbounded range.

## 2. Constructive fixed pools for this program

Use the exact finite widths from V and fixed chosen Boolean ripple/
schoolbook templates to assign its classical fields padded bit ranges.
These are arrays with public capacities, NOT an array indexed by Qcap.
The source stores only a bounded current tree and decoder stage even though
Qcap is exponential. Define the static families in the following order:

1. Input N, group decomposition, current secrets/interval endpoints and all
   public profile/cap words; the m widths/offsets and generator constants.
2. At most n+1 current/retained sibling label slots. Each label has width
   n+ceil(log2q0)+O(1), with the fixed sign/guard padding from source4.3.
   Labels are reused after a node consumes/discards its inputs.
3. The m capped depth-first frames, each with its source O(n)-bit parameter,
   return/loop/child-slot fields; one shared current search description.
4. The exact EXTRACT stage arrays, verifier windows and its reused arithmetic
   fields. There are O(n) levels/windows of O(n) or smaller bit widths.
5. The K decoder records (known frequencies, signs/bases and running residues),
   streamed current/best candidates, and n modular constants of O(n) bits.
6. Common finite-table/rational/schoolbook work, allocation/handle metadata,
   source-private/sign erasure fields, and all source bit-level generation,
   operand and loop scratch. No circuit tree or candidate list is expanded.

Each dimension is computed from the actual formulas and chosen finite
bit-circuit templates, and its offset is the prefix sum of those dimensions.
Here O(n)-width notation records the PROVED bound, not an unspecified
runtime allocator: use the actual integer bit widths of the source's caps,
q0, n+40+T_V, frequencies and fixed templates. All carry/product scratch is
obtained from the finite chosen ripple/schoolbook template for that width.
Reserve maximal stage widths and reuse common fields at their specified
release points. For example the source proves K<=2^15 n on its main branch,
log2q0=O(n), P_j=O(n), and m<=2n; these give fixed polynomial capacities on
incorrect-label and abort paths too. Its finite branch uses its own fields.

This sum is O(n^2), by the source9.3 list and the elementary dimensions above.
All handles/padding count. A map for O(n) genuine slots uses O(n log n) bank
bits and fits the same bound; no directory for every bit or every lifetime
is added. A field has an address in this one fixed pool, not a heap object
whose descriptions accumulate with time. Recursion contexts and long loop
counters remain pool data. Program code is a fixed finite controller; its
opcodes are not an exponentially unrolled instruction tape.

For genuine quantum work reserve the source's retained-sibling ranges by
level, of total at most sum_i b_i+1<=n+1, plus the ONE current source-phase
output. Reserve its shared maxima for search/Boolean arithmetic/extraction/
transforms and clean ancillas, using the actual chosen linear-size templates.
A parent holds only its retained phase siblings while a child runs; it does
not hold a separate full scratch pool. Released roles are reused, as source9.3
specifies. The resulting fixed pool is O(n), with all inactive helpers counted.

Let B be the next power of two above the actual classical capacity sum and
H the next power of two above this complete genuine quantum pool. Thus
B=O(n^2),H=O(n). Their exact dimensions and offsets are computable without
instance advice or an unknown threshold. Before acquisition a bounded number
of O(n)-bit physical words can stream the public integer profile/cap/layout
calculation; it need not store an m-entry classical array. Schoolbook
arithmetic and sequential scans use O(n) temporary classical bits here.
This public setup is polynomial work, paid separately. The fixed finite
trigonometric recipe is computed, not supplied as preloaded data.

Map virtual classical bit i to physical wire2i, 0<=i<B, and genuine wire j
to2j+1, 0<=j<H. Reserve the ENTIRE prefix through2max(B,H)+3, including all
unused pairings and padding. One current raw source request additionally
uses n+1 temporary wires. The full physical allocation is O(n^2). There is
no sparse set of enormous wire indices or uncounted quantum classical data.

Put w=ceil(log2(4B+4H+4n+32))=O(log(n+2)). The finite kernel stores only the
input/output O(n) bits, a fixed number of w-bit address/operand fields,
its finite opcode, and O(w^2) bounded staging/layout scratch. All long source
words, return contexts, caches and mutable generation descriptors stay in
the basis bank. Since log^2(n+2)=O(n), physical classical space is O(n).

## 3. Direct bit interpreter with actual addressing and generation cost

Expand V's specified arithmetic/control into finite Boolean bit actions,
indexed reads/writes, exact elementary Clifford+T gates, measurements,
coins, source calls and finite branches. The source's CORE ledger (1.1)
counts this expansion, including instruction/operand generation. A bulk
multiply, comparison, whole field or subroutine is NOT one virtual step.
The opcode set and number of operands per opcode are fixed and finite.
The current frame/descriptor has a known bank address. Loop and call/return
values are fetched from its bounded banked frame, never a classical stack.

READ(i): measure known wire2i into a staged physical classical bit.
WRITE(i,b): READ(i), X on2i iff its old value differs from b, then forget
unneeded staged values. Boolean bit logic reads its fixed number of operands,
performs the same Boolean action and writes its destination. No unmeasured
quantum query or coherent control is treated as a classical bank bit.
An original coherent control remains a quantum control on mapped odd wires.
Known genuine address j maps to2j+1; data address i maps to2i.

For each instruction fetch its fixed number of at-most-w-bit descriptor
fields by separate READs. A known field/base product can be computed ONCE
in O(w^2) core bit actions. For each of its w bits, ordinary w-bit pointer
arithmetic, address construction, instruction emission and staging cleanup
cost O(w) core actions. Thus a full field costs O(w^2) core actions. The
fixed number of fields, finite opcode logic, branch/return steps and actual
virtual bit action fit the same bound. This includes any descriptor of an
original GENERATED gate: that descriptor has been stored/fetched, not
provided as an instruction oracle. No full-bank scan is needed or claimed.

EVERY physical indexed bit action, field READ/WRITE, generated instruction
and actual quantum gate ALSO pays its full O(w) address fee. Thus each
expanded virtual core action costs at most C w^3 PHYSICAL charged work,
including the kernel's own construction of all addresses and inverse words.
There is no free word access and no recursive invocation of a bank
interpreter to implement the kernel's short physical address arithmetic.
The kernel is a fixed finite loop acting on its bounded physical fields;
its own bit actions/addresses are precisely the O(w^3) just charged.

Emit the original actual Clifford+T word on its mapped odd roles. Boolean
controlled operations are decomposed into their actual finite exact words,
not an inverse or controlled version of an unknown source. Original
measurements and coins write their same outcomes to their bank destinations.
Reset/discard is measurement, conditional X to zero, and forgetting: the
exact trace-and-zero channel with arbitrary references. Source-private
EXTRACT outcomes, unsigned labels/signs and their extra fetched copies are
forgotten at the SAME logical points; kernel transcripts are not fed into
routing, later randomness, source choices or the decoder.

At a V source request acquire EXACTLY ONE original raw n+1-qubit register.
SWAP its entire state into V's designated zeroed odd slots, using three
CNOTs per qubit, and release the now-zero temporary wires. All correlations
move with the register. The O(nw^3) physical work fits the same factor
applied to V's original n+1 core source fee. A move, zero, bank measurement
or reset is not another original sample. Calls, retries and all four hard
guards remain at EXACTLY V's logical points. There is no additional source
call inside a known gate word or its actual adjoint.

After V produces its result, copy the ENTIRE secret to counted physical
classical output FIRST. Then clear/reset/release every basis cell, odd pool,
temporary source role, padding and staged copy. Initialization and release
can stream all cells with the same known-address kernel in
O((B+H+n+1)w^3) charged work. Private data is not retained as a hidden
transcript, and no lifetime-indexed history accumulates with execution time.

## 4. Full channel identity, including private-sign erasure

At aligned logical times, include fixed unread product originals U and an
arbitrary inaccessible reference R. The actual state has the CQ form

 sum_(c,z) p(c,z)|z><z|_kernel tensor |c><c|_basis-bank
                      tensor rho_(c,z)_(genuine,U,R).      (4.1)

Here c is V's genuine classical record and z is only bounded fetched copies/
finite functions of its fields. Conditional rho can depend on every record;
no state independence is asserted by this invariant. Forget duplicate
kernel values and relabel odd slots: the result is EXACTLY V's full state.

Initialization copies classical input and starts the same zero pools and
original source. READ projectors reveal a value already classical in c,
leaving conditional rho unchanged; a duplicate is forgotten when released.
WRITE and irreversible overwrite mix conditional states exactly as logical
classical forgetting does. Boolean logic and field decoding then preserve
the invariant. Mapped gates, measurements, coins, guards and return contexts
have the SAME instruments/probabilities as V. A source SWAP is only register
relabeling and reset has the exact reference-safe identity above. Induction
establishes (4.1) on every history, without any ideal-label, cap-survival,
high-part or decoder-success postselection.

For GPS-BLOCK the private exclusions matter. Original unsigned k and sign
sigma are overwritten after making signed a, and extraction-private records
are not routing data. Kernel copies may be used ONLY to implement V's own
specified update, and all extra copies are forgotten at that update's
release. No readout log, address trajectory or kernel transcript becomes a
new routing input. Thus logical low-residue routing and private erasure are
unchanged; a full-label-dependent implementation detail cannot introduce an
extra selection of leaves or alter the ideal untouched-high-part proof.
One can simply apply V's COMPLETE unconditional theorem to the identical
logical channel, instead of reproving a conditional law after new readouts.
The passive independent source cannot react to these extra deterministic
record copies. No stronger interactive-supplier statement is selected.

The final output distribution is EXACTLY V's for every N,s. All source label,
private signed-fiber, root tail, fallback/acquisition/weight/frequency-cutoff
and decoder events are already counted in that theorem, with ZERO additional
failure loss. This transfers success at least1-2^-8 including the full finite
branch. It does not add a positive malformed fraction or condition success
on a favorable acquired subset.

## 5. Actual every-branch resources, exact envelopes and indices

The physical allocation is SC=O(n)+O(w^2)=O(n) bits and ENTIRE
SQ=O(B+H+n+1)=O(n^2) qubits, including inactive/padded cells, all genuinely
coherent roles and current raw source wires. Virtual SCn^2,SQn are not the
actual declared pair. All combined-memory address fees are O(w)=O(log(n+2)).

Using the CORE count (1.1), not only quantum gates or an uncharged word count,

 T_phys<=C w^3(A_V+B+H+n+1)+poly(n)
       =O(n^(5/2)(log2n)^(7/2)2^R)+poly(n)
       =O(n^(5/2)(log2n)^(7/2)2^(a sqrt(n log2n))).        (5.1)

The additional poly(n) is the paid public layout computation and fixed
control initialization. Every fixed polynomial is absorbed by the displayed
positive subexponential for all sufficiently large n; finite remaining
lengths have bounded explicit caps and contribute one absolute constant.
The exponent coefficient a is the source's proved exact rational, unchanged.
Its explicit threshold and uniform finite-prefix argument are included.
No inner unknown big-O coefficient or unbounded logarithm is guessed away.

All four source cutoffs remain literal logical guards, not an attempt to
charge physical kernel work for free. (5.1) bounds that work, ALL source
moves, original preparation, descriptor fetches, failed searches, private
coins, repeated instructions, refusal and complete cleanup on EVERY branch.
The ideal expectations in V's proof are used only for cutoff failure, never
as an actual-branch work bound here. Runtime is sequential work, not depth.

Exactly ONE original register is acquired for each V request, so its literal
Qcap and finite-branch acquisition rules transfer unchanged. In particular
Q=O(2^(a sqrt(n log2n))). Discarded copies and every unsuccessful tree/search
are included. No bank initialization or extra READ creates original samples.
The canonical independent-ideal-source promise and exact fraction0 transfer
by output-channel equality. The same all-N physical algorithm has ALL FIVE
guarantees jointly.

For time and samples, log2 of either representative is
a sqrt(n log2n)+O(log n), hence their exact growth index is1/2. The two
polynomial space representatives have index0. The supported declarations
are EXACTLY (0.1), with no claimed numeric objective for Q or fraction.
This is not a cube-root algorithm, a maximal tolerance result, a free-memory
simulation or an inference across different error-model contexts.
