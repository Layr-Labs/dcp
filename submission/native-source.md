# GPS-BLOCK-NATIVE: a streamed native pair instrument with linear classical storage

For every N>=2 and s modulo N, n=ceil(log2N), ONE uniform physical algorithm
recovers the ENTIRE secret with unconditional probability at least1-2^-8.
On EVERY branch, including discarded samples, failed attempts and all aborts,
its simultaneous bounds for n>=2 are

 T=O(n^(5/2)(log2n)^(3/2) 2^(a sqrt(n log2n))),
 SC=O(n), ENTIRE SQ=O(n^2), Q=O(2^(a sqrt(n log2n))),
 a=176777/250000, epsilon(n)=0.                            (0.1)

The four exact growth indices are1/2,0,0,1/2. The finite n=1 program has
bounded absolute costs. SQ includes ALL classical-data basis qubits, dense
padding/inactive cells, genuine work and raw source temporary wires. The
same input/source/cap rule and guarantee apply jointly to all five claims.
No positive robustness, maximal tolerance, free memory or cube-root time is
asserted. All constants are independent of N,s and measured outcomes.

## 0. Complete immediate program, directly used hybrid method and current change

The immediate program/controller source is GPS-BLOCK-BANK2,
b1e75c79-a495-4e24-9c48-a79ecfb8348d. Its complete main is copied unchanged
as controller-source.md, full SHA-256
0e11424104cd7fd4371f9a05676099a7b7133ecf4952c40c6ce2a9de17343950.
ALL FOUR of its complete mathematical helpers are copied unchanged:
previous-bank-source.md (full prior GPS-BLOCK-BANK main), gps-source.md
(full1113-line GPS-BLOCK proof), bank-interpreter-source.md (full generic
measured-bank proof), and stream-source.md (full STREAM method main).
Their full respective hashes are
b8a58ced5432baa998432d96450301265d17e83f0998e358895b409b881837f6,
3016a821fcc6ae313f0156326e1ca1f7de2f240c18d07bba70eb0db7859519f7,
26b64d6eb0471b0e73a66164c39c03d9a5954d9cad120a52729fdd50a2467298,
5ad693a64b57913c580fbec4798bf021fe9d505f3c2fa2421f4fcf080fd8affd.
No predecessor proof is omitted from this selected immediate archive.
Historical archive paths inside old method sources still describe their
own algorithms, not new mathematical premises here.

The additional directly selected physical feature is STREAM's hybrid active
word/native-bank implementation and full CQ mode-transfer method, not only
its pointer sweep. The original is b4039ae4-431b-4deb-8f66-e7d9df2ee633,
commit3e7a3d873fc24859d05fc7928996c372a1387c94; its exact complete main is the
stream-source.md already present. Its Sections2,4-6 supply active words,
measured coefficient/record access, native bit/gate generation and hybrid
channel reasoning. The old SPTS algorithm, compressed-preparation grammar,
log-three theorem and one-third noise promise are NOT the current program.
We derive the NEW complete GPS native ATTEMPT below. The prior BANK2 used
STREAM's pointer feature for a generic field-fetch kernel; the active
whole-attempt hybrid is a distinct directly used feature here and is
explicitly credited despite the carried source file.

The semantic algorithm remains EXACTLY GPS-BLOCK: all labels, private sign
laws, tree/Grover instrument, decoder, four literal caps and source schedule.
The physical change is a native COMPLETE pair ATTEMPT with a precomputed
basis-bank residue matrix and a constant number of active O(n)-bit words.
All repeated Grover/search/clock/verification work is native. Remaining
work uses the generic controller and is charged using the source's strong
superpolynomial gap between Qcap,q0 and2^R. It is NOT called polynomial-total
work, and a polynomial interpreter is NOT multiplied into the Grover loop.
All inherited algorithms, source proofs and methods retain their authorship.
No previous acceptance, diagnostic or provisional graph edge is a premise.

## 1. Exact source promise, full semantic program and finite branch

The fifth structured declaration uses EXACTLY the canonical text:

"Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies."

Every request receives one independent ideal rho_s, without purification,
source control or preparation inverse. Unread passive source-held copies
are excluded from accessible allocation by the challenge rule. There is no
interactive supplier reacting to implementation readouts. An arbitrary
reference may be retained for the channel argument; no reference access is
used. No conditional postselection or positive malformed promise is added.

Let V be the complete GPS-BLOCK semantic program in gps-source.md, with the
concrete BANK2 controller in controller-source.md as its generic physical
implementation. Before original acquisition choose the public branch:
if n<2^4096, execute THAT COMPLETE BANK2 program and return its output. This
includes its n<256 exhaustive branch, all other source cases, its literal
caps and exact independent-copy guarantee. It is not a different finite
solver. On this fixed finite prefix its extra log factor is bounded by an
absolute outside constant; its SCn,SQn^2,Q envelope and output guarantee are
unchanged. Only the large branch is specialized below.

For n>=2^4096 compute EXACTLY the original source profile and all parameters:

 Delta=2ceil(log2(4R)), m=floor((2R-2)/Delta)+1,
 R=least integer>=2 with S(R)>=n-1,
 v_i=2R-1-(m-i)Delta, q0=product_i(v_i+1), G=2^m q0.

Do not change the first-qualifying scan or round widths to improve a bound.
PS_TREE(D,B), p_i,b_i,r_i=b_i+1, signed/unsigned modes, odd-part h/step/pdec,
K,Smax,H0, all CRT multipliers, source EXTRACT/table/verification parameters,
2-adic recovery and final output are literally the source formulas.
The four actual cutoffs remain

 Qcap=1024(2G H0+2n), Wcap=1024(2m2^R H0),
 Cf=ceil(Qcap/ceil(sqrt n)), and root |W|<=nq0.             (1.1)

The weighted guard occurs AFTER the node's r_i inputs have been built,
but BEFORE its quantum ATTEMPT; all those child sources/work are counted.
A refused acquisition acquires no extra copy. Every failure/retry/abort
uses exactly V's release/output rule. No work or counter is restarted to
avoid a cap. The new matrix and native fields are deterministic work from
existing records, not extra source calls or a new probabilistic event.

The complete source proves, unconditionally, independent latent labels;
verified extraction coupling without conditioning on correct reports;
private signed-leaf untouched-high-part laws; the distribution-free
occupancy bound giving conditional combiner return>1/2; multibit Dirichlet
separation and an unguarded root tail; all four cutoff losses; and exact
2-adic parity conditional on the odd answer. Their total failure is

 2^-10+2^-10+2^-14+2^-19+2^-20+2^-20<2^-8.                (1.2)

All these proofs are included in gps-source.md Sections2-9. Neither passing
an extraction/frequency guard nor a later success is used to select a
conditional high-part law. Exact semantic channel transfer below preserves
this SAME theorem, including private unsigned/sign/EXTRACT erasure.

## 2. Exact bank pools, added matrix and native fields

Use the complete padded dyadic classical pool/typed finite controller and
compact genuine pool of controller-source.md. Its dimensions are computed
from actual public widths/templates and caps, including the public U-doubling
test before choosing the address width. Every field, return frame, handle,
private erased value, input, label, cap, prefix, arithmetic/table work,
decoder record and generator descriptor is counted. No Qcap-entry array or
execution-lifetime directory is allocated. B0=O(n^2),H0_pool=O(n).

Add ONE reusable current-node residue matrix: at most2R rows, each with at
most2R meaningful bits, stored in known dyadic padded classical-word slots.
Padding a row to the existing public O(n)-bit slot still costs at most
O(Rn)=O(n^2); the meaningful matrix is O(R^2)=O(n log n). Include row/base
metadata, source-input handles and all initialization/clearing padding.
There is never one such matrix per recursive level: while building children
all node quantum ATTEMPT work is inactive, and one shared matrix is reused
only after the current children are ready. Node input labels remain stored
for the later full signed output arithmetic; they are NOT discarded early.

Add one shared compact genuine input area for at most2R phase qubits and
shared native SEARCH/residue/pair-comparison/carry/AND helpers. A parent
keeps only its ordinary phase siblings while children are built; it does
not retain a private full native scratch pool. The source sibling count is
sum b_i+1<=n+1. All added work is O(n), including unused roles, and source
raw/extraction/transform roles remain counted. Thus total B=O(n^2),H=O(n)
after next-power-of-two rounding of the actual finite capacity sums.

Map classical bit i to even wire2i and genuine slot j to odd wire2j+1.
Reserve the ENTIRE paired prefix through2max(B,H)+3, all inactive pairings,
and one raw original n+1 temporary register. Quantum space is O(n^2), not
the O(n) smaller genuinely coherent part. Every actual operand pays the full
combined-memory address fee O(w), w=O(log(n+2)). All bases/offsets/padding
and public setup are paid; no sparse huge physical wire index is used.

The generic mode retains its physical O(n) input/output and O(w^2) short
staging. The native mode additionally reserves a FIXED NUMBER of words for:
current level/widths/row bases; e; x0,x1; measured query y; delta/pivot;
ONE current b_i-bit coefficient row; u/trial and random-j/iteration counters;
and a fixed number of gate-role/carry/bit pointers and flags. Numeric local
words have O(R)<=O(n) bits. Even allowing a constant number of full n-bit
controller words remains O(n), and ALL inactive native fields count.
The residue matrix, full label lists and long recursion stack stay banked;
there is no resident R^2 coefficient array or classical stack.

## 3. Strong source gap pays every generic phase and mode transfer

We use the source's STRONG estimate, not only its displayed loose Q bound:

 For EVERY fixed A>0, q0=O(n^-A 2^R),
                        Qcap=O(n^-A 2^R).               (3.1)

Proof from the included actual profile. Source9.4 proves
G<=8R2^(R-m/5), m=Theta(R/log R), R>=sqrt(n-1)/2 and R=O(sqrt(n log n)).
Consequently m/log n tends to infinity, so2^(-m/5) beats every fixed power
of n. Multiplication by R,H0=O(n) and fixed constants is absorbed by choosing
a slightly larger fixed power in this fact. Since q0<=G and Qcap is (1.1),
(3.1) follows; the additive2n is absorbed because R/log n tends to infinity.
For a CHOSEN fixed A all constants are absolute independent of input/outcome.
This is an actual cap/profile inequality on every branch, not an expectation
or an assumption about a typical sieve. All finite exceptions are bounded.

The following work is GENERIC, with its complete BANK2 bit interpreter:
public source/profile/layout initialization; acquisition/transforms/EXTRACT;
leaf signing and its private erasure; building/returning children; full signed
label arithmetic; frame/global-cap bookkeeping; native entry/exit; coefficient
matrix preparation/clearing and genuine slot moves; full decoder/root-frequency
processing; and complete output-first cleanup. NO repeated inner SEARCH,
residue oracle, trial clock, verification or pair instrument action below
is left in that generic list.

There are at most Qcap actual acquisitions. At a fixed level, supplied child
outputs descend from disjoint nonempty source sets, including failed attempts.
Hence at most Qcap inputs are delivered there; an actual/refused node attempt
has at least two such inputs. Summing over m<=2n levels bounds node events
by O(nQcap)+poly(n), even on wrong-label or abort histories. Pass-through
levels add only polynomial bookkeeping per delivered input. This is the
source9.4 operational disjointness argument, independent of ideal statistics.

Preparing a current matrix needs only polynomial work per node: read its
r_i full O(n)-bit labels and compute EXACT rho_j=(a_j/2^p_i) mod2^b_i, then
write those b_i bits and role metadata. The divisibility invariant holds for
reported labels on every branch by the verified residue equality in V.
Two's-complement bit extraction implements the same signed quotient/modulus;
ordinary full-word arithmetic may instead be used. Source label widths and
all intermediate fields remain O(n). Matrix clearing, entry/exit and moving
O(R) phase wires/handles are also fixed-polynomial node work. No full n-bit
label is reread for each Grover iteration.

For specificity a generous full physical bound for ALL generic work is

 T_gen<=C n^20(Qcap+q0+1).                               (3.2)

Here is a degree ledger, not an unspecified unbounded overhead. Source full
label/controller work is O(nmQcap); EXTRACT/source work is O(n^2 log n Qcap);
decoder work is O(n^3 K q0+n^3 K), K=O(n); public work is O(n^6). Each mode
transfer/matrix/handle event uses at most polynomial schoolbook work on
O(n^2) bounded fields; even O(n^6) core actions per node is a conservative
upper bound. BANK2's O(w^2) charged overhead is at most O(n^2). Node count
is O(nQcap)+poly(n); bounded public scans/layout and final clearing are at
most the same polynomial degree. These terms are all bounded by (3.2),
with enormous spare degree. The finite typed-kernel/field setup is charged
here too. No table exponentially larger than the source's actual q0-grid
is iterated or stored; the decoder grid is STREAMED exactly as in V.

Choose fixed A=64 in (3.1). Then

 T_gen=O(n^-44 2^R+n^20)
      =O(n^(5/2)(log n)^(3/2)2^R).                       (3.3)

The n^20 term is
absorbed because R/log n tends to infinity. Constants may depend on the
fixed A and finite implementation, never on n,N,s or outcomes. This uses
an explicit superpolynomial GAP below2^R. It does NOT call these phases
polynomial-total work, hide an arbitrary polynomial in a tight time bound,
or apply a generic polynomial interpreter to each dominant Grover gate.

## 4. Native entry, exact residue rows and every repeated operation

At a level-i node with b_i>=1, r_i=b_i+1, build children and execute the
ORIGINAL Wcap guard/debit in generic mode. Only if admitted, prepare the
matrix rho_j above. Give the current genuine phase inputs a compact shared
role range by paid SWAPs with zero slots and update direct handles. All
arbitrary correlations move with them; this is not a reconstruction of
phase states. Current labels remain banked. Load the bounded local words
and bases, clearing their old bank shadow copies when moved to native mode.
On exit encode new semantic fields back, then clear native duplicates.
The active-value decoding is made precise in Section6.

The native region implements the COMPLETE original ATTEMPT, not just an oracle:

1. Reversibly form res(x)=sum_j x_j rho_j modulo2^b_i on the actual UNKNOWN
   phase-input qubits, measure the b_i-bit result e and clear that accumulator
   by XOR with e as V does. No source-phase qubit is read as classical data.
2. Run EXACT source SEARCH(f_e), then SEARCH(f_(e,x0)), with f_e(y) the clean
   residue equality and f_(e,x0) additionally excluding x0. The fixed schedule
   is u=0,...,ceil(r_i/2), twenty trials each, uniform j in[0,2^u), prepare
   H^r_i, j actual Grover iterations, measure y, classically verify the SAME
   predicate and reset every trial register. All clocks/coins/counters are
   native active words; there is no generic callback per iteration or trial.
3. On two verified distinct fiber members, coherently compute the pair indicator
   on the original phase-input register, measure it and uncompute its scratch.
   On outcome1 XOR x0, choose the same first differing pivot and emit the CNOT
   compression. The nonpivot roles are zero on that support and are released.
   All FAIL cases reset/discard ALL node inputs/work exactly as V, then return
   to generic mode to build fresh children under the original guards.

On success keep its unknown pivot phase qubit, move it to the original
caller-output role by a paid SWAP, and do the full signed label difference
A(x1)-A(x0) in generic mode. Its full O(n)-bit source labels are used HERE,
not inside repeated residue predicates. Keep the needed x0,x1 until that
calculation, then apply the same private releases. Clear the entire matrix,
all extra staged copies/metadata and unused compact phase roles before
reuse. These per-node mode costs are (3.2). No original source call occurs
inside a SEARCH/oracle/inverse or other known gate word.

For each residue word, j is a CLASSICAL outer row loop. READ the b_i stored
coefficient bits from the known row into ONE reused native word, or stream
them, and emit the full controlled constant-add template. Query y_j (or
phase input x_j) remains an actual QUANTUM control. The controller visits
EVERY row and emits its entire original controlled word, even when that
coherent control is inactive. It NEVER measures a candidate bit to select
a bank address. The matrix is unchanged during the attempt, so reverse
row order and actual reverse ripple words are its exact uncompute.
Additional basis READ outcomes are deterministic conditional on existing
classical labels and therefore cannot disclose a coherent query value.

Residue equalities and exclusions, diffusion Toffoli ladders, pair-pattern
comparisons, XOR/CNOT compression and source measurements use the exact
finite Clifford+T templates of gps-source.md. Controls remain coherent;
no arbitrary phase synthesis, classical simulation of an unknown qubit,
source inverse/control or supplied purification is used. All gate controls,
clean AND/carry helpers and their reverses are counted, including failure
branches. The field generator emits the SAME actual words on ANY genuine
work state, not only on an ideal successful source-label component.

## 5. Native per-attempt work and deterministic weighted bound

Write L=max(1,ceil(log2n)). The dense allocation gives w=O(L), and source
capacity gives R>=sqrt(n-1)/2, R=O(sqrt(n log n)), r_i,b_i<=2R. Thus
w^3=O(R), R=O(n), n=O(R^2). These are uniform asymptotic inequalities with
absolute constants; on n>=2^4096 they have direct exponential-versus-power
slack (n>=2^(L-1)). Remaining finite exceptions change an outside constant,
not a source parameter or event. No unbounded factor is hidden.

At row entry, all metadata is bounded short addresses, public widths and
local indices, not full signed labels. Even allowing O(w^3) CORE setup per
row for addresses/handles and short-field decoding is sufficient. Each
b_i-bit coefficient READ/copy and controlled ripple template uses persistent
regular native role pointers: O(b_i+w) actual bit/gate-generation/carry
and sentinel actions per row, including control/AND words and reverse walks.
One current coefficient row fits SC=O(R), not R^2. Every emitted bit action,
READ/WRITE, instruction and gate pays its FULL O(w) address fee.

Consequently a complete residue oracle or its inverse, including all row
setup, costs at most

 C r_i(b_i+w+w^3)w + C(r_i+w)w
                      =O(R^2 L).                        (5.1)

The equality uses r_i<=2R and w^3=O(R). This includes, rather than discards,
all per-row address products/loads and actual instructions. Diffusion,
canonical equality/exclusion and classical measured-query verification have
the same bound, with reused role pools and complete uncompute. No descriptor
word is fetched from a generic interpreter per emitted ripple gate.

Native counter/trial work also fits: j has at most R bits; its bounded
compare/decrement and all fair coins, u/trial changes and register reset
cost O(R) or at most O(n) core actions per iteration/trial. Since n=O(R^2),
these fit (5.1), including all addressing. They are NOT left as generic
long-word operations inside the loop. Measurement of the original residue,
pair projection and compression use at most the same O(R^2L) allowance.
There is no hidden O(n r_i) full-label scan per Grover iteration.

The exact fixed source schedule performs fewer than80w_i Grover iterations
across the two searches, w_i=2^ceil(r_i/2), and O(r_i)<=O(w_i) trials. Therefore
EVERY complete native attempt, returning or failing on arbitrary input,
has physical charged work

 cost(ATTEMPT_i)<=C R^2 L w_i.                            (5.2)

All admitted attempts have the ORIGINAL pre-debited sum w_i<=Wcap. Hence
on EVERY execution branch

 T_native<=C R^2 L Wcap
          =O(n R^3 2^R)
          =O(n^(5/2)(log n)^(3/2)2^R).                  (5.3)

We used the actual source estimate Wcap=O(nR/(log n)2^R). Markov/expected
success arguments are NOT used to bound actual work; they appear only in
V's unchanged cutoff-failure proof. A final refused attempt's already-built
children and generic cleanup are separately counted in (3.2). No interrupt
of an unknown quantum state or free failed attempt is assumed.

## 6. Full-reference hybrid CQ equality and private erasure

At each aligned semantic time include unread passive originals U and an
arbitrary inaccessible reference R_ref. The actual joint state is a CQ
mixture over bank record c and bounded generic/native classical fields z,
with conditional rho_(c,z) on mapped genuine roles,U,R_ref. Decode banked
inactive fields and native ACTIVE words to the semantic values; relabel
odd/compact slots and forget deterministic staged/derived copies. The result
is EXACTLY the GPS-BLOCK semantic state. No tensor-independence of these
conditional states, correct reported labels or successful search is assumed.

Initialization has the same input, zeros and originals. Bank READ copies an
already-classical value and leaves conditional rho unchanged. WRITE/reset/
forgetting mixes conditional states exactly as logical classical erasure.
Entry moves active values from bank fields to native words and zeroes the
shadow; exit copies back and zeroes duplicates. They do not retain a previous
logical value after its semantic overwrite. The matrix is a deterministic
function of already-classical labels, read only at known outer indices; all
its extra copies are cleared at attempt release. Its reads are independent
of coherent x/y conditional on the existing classical record, including
inverse, failure and arbitrary-work-state branches.

Section4 emits the SAME genuine gate words, measurements and classical
predicate results as V. Source, phase-role and output SWAPs are register
relabeling with all correlations. Reset/discard is measurement, conditional
X and forgetting, exactly trace-and-zero with an arbitrary reference. Induct
over generic bit steps, native microsteps and entry/exit: the decoded state
and instruments agree on every actual history. No label-correct, pair-pass,
frequency-guard or source-success event is postselected for this invariant.

Source unsigned k/sign and EXTRACT-private records are erased at the same
logical points by the unchanged generic leaf program; no native copy of
them is created as extra routing data. Kernel/matrix/readout/clock transcripts
are never new routing inputs, source feedback or random coins. Thus private
signed-high-part and low-residue routing laws are used exactly in their
original unconditional theorem, not reproved after conditioning on extra
readouts. The fixed passive source cannot react to those implementation
copies. This does not assert an interactive-source or positive-noise result.

The final classical output law is consequently EXACTLY V's for every N,s.
All original statistical/cap/extraction/frequency/decoder failures remain
(1.2), with ZERO added loss. The all-N finite BANK2 fallback has that same
law too. One original source is acquired per logical request and none during
native work, so the same literal Qcap/finite acquisition rules transfer.

## 7. Actual simultaneous resources and exact declared objects

Combining (3.2)-(3.3) and (5.3), paid fixed allocation/setup/cleanup and the
original exact profile bound2^R=O(2^(a sqrt(n log2n))) proves (0.1) for the
main branch. For n<2^4096 the complete BANK2 fallback has only one extra
factor log2n in time, bounded on this FIXED finite prefix. No unbounded
polynomial or logarithm is absorbed by that argument. All original sources,
failed work, bad reports, native/generic mode transitions, inactive fields
and complete output-first release count on every branch.

Classical space is O(n) for generic input/output/short staging and the fixed
number of native O(R) or O(n)-bit active words/pointers, with all inactive
reservations. Quantum space is the FULL dense paired prefix O(B+H)=O(n^2),
including the entire matrix and all padded bank cells, compact phase inputs,
source retained siblings, shared genuine work and raw n+1 originals. Source
held unread copies are excluded only under the explicit challenge convention.
The smaller virtual classical/coherent pair is not the actual declared pair.

Every original acquisition, rejection and failed subtree is in Qcap, so
Q=O(2^(a sqrt(n log2n))). Extra basis reads, zeros, matrix preparation and
all SWAPs are not original copies. The guaranteed fraction is EXACTLY0 under
the literal canonical independent-ideal-copy model; no positive robustness
or impossibility is inferred. Full-secret success is at least1-2^-8 jointly
with these four actual resource bounds, including clean finite inputs.

Logarithms of the time/sample envelopes are a sqrt(n log2n)+O(log n), so
their exact growth index is1/2. Both polynomial storage envelopes have
index0. Only the time index is the numeric score; all five structured
objects concern this SAME actual configuration and complete proof.
