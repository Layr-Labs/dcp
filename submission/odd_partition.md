# ODD-POLYRANK: exact weighted odd-cell instrument with a polynomial compiler

This helper supplies the full physical instrument used by proof.md. The
cell family and all-k yield proof are adapted from PARTROOT196, public
3315027c-4ec3-4352-80e5-f8f384e286f1, virtual.md7.1-7.2. The new contained-token
rank arithmetic replaces that source's generic exhaustive truth-function
compiler. The arithmetic cell/back idea in SWF-13377 Section7.1 informed
this construction; its old even FW instrument is not run. No source
verdict is a premise. The public group size k is specified by proof.md,
is odd and at least5, and grows with input length. Write h=(k-1)/2 and
w=1/[h(h+1)] LOCAL cell weight (not the main proof's key width).
Inputs are the k equatorial phase qubits with tables(t0^i,t1^i) for the
common parameter th; every input difference has the same low key modulo
2^(p+c). All-input channel/cleanup statements below also hold with arbitrary
reference systems and without an equatorial promise. Toffoli has an exact
constant-size Clifford+T decomposition; no rotation synthesis is used.

### 7.1. Complete uniform cell family,poststates and rate

A-cell:chooseoneunorderedoddpair,leaveotherk-2coordinatesfree,weightw.
Forj=0,...,h-1,J_j-cell:partitionallkcoordinates intoj unorderedoddpairs
andoneall-equalremaindergroupofsizek-2j. Itspercellweightandcountare
 w_j=(1-w*j*(k-j))*(k-2j)!/(k-j)!,
 N_j=k!/(2^j*j!*(k-2j)!).
CanonicalenumerationlistsA,J0,...,J_(h-1),thenlexicographicsortedpairlists;
the remainderis theircomplement. Thisnames eachcellonce. The formulas
are uniformfiniteinteger/rationalalgorithms givenpublick,notadvice.
Computefactorialproducts/rationalreductionsserially;donotstorethe
entirecellfamily or its truth-table history.

LetPi_cell projectontothecomputationalcell. IfxhasminorityHammingweight
t<=h,thereare t(k-t)containingAcells. A J_jcontainsxonlyifj=t orj=k-t;
forj<h onlyj=t<hispossible. Thereare (k-t)!/(k-2t)! suchJ_tcells:
matchthe tminoritybits todistinctmajoritybits,leavingequalbits.
For t<h,totalweightis
 w*t*(k-t)+[(k-t)!/(k-2t)!]*w_t=1.
At t=h,Jcellsareabsentandw*h(h+1)=1. Allweightsarenonnegative.
Therefore sum_cell w_cell Pi_cell=I onEVERYoneofthe2^k basisinputs
andalljointstates. The normalizedKrausoperatorsaresqrt(w_cell)Pi_cell.
This is an all-kidentity,not a finite LP/empiricaloptimalityclaim.

On productequatorialinputs,a cellwithLindependentbinarycomponents
hasprobabilityw_cell*2^(L-k),independentofphases,labels,secret,past.
Thus the typeprobabilitiesare
 P_A=choose(k,2)*w/2=k/(k+1),
 P_j=N_j*w_j*2^(j+1-k)=2^(1-k)*choose(k,j)*(1-w*j*(k-j)).
They sumto1 bycompleteness. This is the sameconditionaltypelaw at
EVERYreachedmacro,evenwhenlaterkeysdependonallpreviousoutcomes.

EveryconstrainedgroupGbecomesonephasequbit. Its canonicalpatternb
has smalleroddpairindex0/larger1,orall0foranequalgroup. Outputtable:
 (sum_(i inG)t_(b_i)^i,sum_(i inG)t_(1-b_i)^i).
Choose smallestwirev;CNOTv->i for everyotheri,thenXtoiifb_i xor b_v=1;
finallyXvifb_v=1. Everyothergroupwire becomeszero,andvindexalpha
selectsb xoralpha. This holds onEVERYstate supportedonthecell,
includingarbitraryreferences. Onproductphaseinputs,disjointconstraints
factor the projectionintoallgroupoutputs andunchangedfreeinputs,
inproductwith eachotheranduntouchedreferences. Nothingiscloned.

EachoddpairisGOOD:equalkeys makeDel_a-Del_b divisibleby2^(p+c).
The all-equalgroupRECYCLES atoldp,withdifferenceitsinputDelsum.
A givesoneGOOD andk-2unchanged inputs;J_j givesjGOOD andoneRECYCLED.
GOODleavesLIVE. NetLIVEcostCis2onA andk-1onJ_j;GOODcountGis1onA,
j onJ_j. Write p=E G=P_A+sum_j jP_j, mu=E C and q=mu/p.
These exact quantities describe the analysis; the controller uses RHO. G isnotBernoulli,andmay
dependonitsownC. For every odd k>=3,
 2<q<=2+7/sqrt(k),mu=(3k-1)/(k+1),p>=k/(k+1)>=3/4. (7.1)

Here is a proof ofthe uniformratebound. LetX~Bin(k,1/2),B=|X-k/2|,
T=min(X,k-X). The displayedP_j equalsPr[T=j]*(4B²-1)/(k²-1).
The j=h termis0,soitcanbe included. Independent centeredfairbits give
 E B²=k/4,E B4=(3k²-2k)/16:
expandthefourthpower,retainingthe kfourthpowers and6choose(k,2)
pairedsecondpowers;allodd/crosssingleterms vanish. Therefore
 sumP_j=1/(k+1),mu=(3k-1)/(k+1),
 p=3k/[2(k+1)]-E[4B³-B]/(k²-1),
 mu-2p=[2E(4B³-B)-(k-1)]/(k²-1).
Thisispositive:everyJoutcomehascostk-1>=2j+2 andtotalJmasspositive.
ByCauchy,E B³<=sqrt(E B² E B4)<=sqrt(3k³)/8. Hence
 0<mu-2p<=8E B³/(k²-1)<=sqrt3*k^(3/2)/(k²-1).
Usep>=3/4 andk²/(k²-1)<=9/8 toobtainq-2<7/sqrtk,proving7.1.
For the growing public k in proof.md set j0=floor(sqrt(k)) and
RHO=2+7/j0. Since j0>=sqrt(k)/2 for k>=4, the all-k theorem gives
mu/p<=2+7/sqrt(k)<=RHO and log2(RHO)<=1+7/j0.
The last inequality follows from ln(1+x)<=x and ln2>1/2.
Here k>=n, so 7/j0<=14*n^(-1/2). These are analytic
bounds; the controller computes only integer roots and the rational RHO.

Alloutputentriesaresums onDISJOINTleafsets. alpha->b xoralpha is
injectiveonitsgroup;differentcomponentsusedisjointgroups,andfree
inputskeepstate,tableandwireID. The product,disjointincidence and
fullpositive3n-bitlabelinvariants thuspersist for everypublick.


## 7.2. Polynomial contained-token ranks

Compute the reduced rational weights w and w_j, j=0,...,h-1. Let D be
the lcm of their denominators. Since each denominator divides
h(h+1)*(k-j)!/(k-2j)! <= k^(k+2), their product bounds D<=k^(k^2).
Set b=ceilLog2(k), coinbits=ceilLog2(D)+2, M=2^coinbits,
scale=floor(M/D) in{4,5,6,7}, B=scale*D, R=M-B<D<=M/4.
The positive integer c_A=B*w is the number of tokens per A-cell;
c_j=B*w_j is the number per J_j-cell (all are nonnegative integers).
All are computed by finite integer arithmetic, not an amplitude oracle.

A token has a unique fixed-width encoding as one of:
 I(u), 0<=u<R;
 A({a,b},v), sorted distinct pair a<b, 0<=v<c_A;
 J(P,v), P a canonical sorted list of j disjoint sorted pairs, j<h,
           with the equal-group being its complement, 0<=v<c_j.
An equivalent k-field partner array, a kind field, j and a copy field
encodes this injectively with O(k^2(b+1)) bits. Use fixed field widths,
zero padding and validity checks, so invalid strings are distinguished.
The token encoding depends only on the cell and v, never on input x.
A token CONTAINS x iff x lies in its cell; every identity token contains x.
The weighted identity in7.1 says every x has exactly B+R=M tokens.
We do not enumerate all cells or all truth-function input patterns.

Here is an explicit ordering and direct rank/unrank for those M tokens.
For basis x, form increasing lists U of minority positions, V of majority
positions, t=|U|<=h. Odd k eliminates ties. Put Acount=t*(k-t)*c_A.
For an injection U->[distinct elements of V], use lexicographic order
of the successive partner choices in the current increasing remaining V.
There are P(k-t,t)=(k-t)!/(k-2t)! injections. A basis input belongs to
J_j only for j=t<h. Its J token count is P(k-t,t)*c_t=B-Acount.
For t=h Acount=B, so that branch is absent. For t=0 the unique J_0
cell has the whole input as its equal group. These include the endpoints.

f(x,r), for 0<=r<M, returns its r-th contained token:
  if r>=B: return I(r-B)
  if r<Acount:
    (u,v)=divmod(r,c_A); (i,j)=divmod(u,k-t)
    return A(sort(U[i],V[j]),v)
  else:
    (u,v)=divmod(r-Acount,c_t)  # reached only when t<h and c_t>0
    remaining=V; pairs=[]
    for i=0,...,t-1:
      block=P(len(remaining)-1,t-i-1)
      (q,u)=divmod(u,block)
      append sort(U[i],remaining[q]) to pairs; remove remaining[q]
    return J(canonical_sort(pairs),v)

The inverse hfun(x,z) is0 on invalid token encodings or nonmembership.
On I(u) return B+u. On an A token find its unique endpoint in U, say
U[i], and its endpoint V[j]; return (i*(k-t)+j)*c_A+v. On a J token
verify j=t<h. For each U[i] find its partner in the encoded matching,
find its rank q in the current remaining V, and remove that partner.
Accumulate injectionrank +=q*P(len(remaining_before)-1,t-i-1).
Return Acount+injectionrank*c_t+v. All indexing/ranks are integer operations.
Mixed-radix blocks partition each remaining injection interval, so unrank
chooses exactly one injection and the accumulated rank recovers u. Every
matching containing x pairs each minority position to a distinct majority
position, uniquely; canonical sorting discards no information. Likewise
the A rank is a bijection on U x V. Thus hfun(x,f(x,r))=r for EVERY x,r,
and f lists each contained token exactly once. This proves the inverse
analytically, rather than relying on finitely enumerated examples.

## 7.3. Exact quantum realization on arbitrary joint inputs

Allocate coin register r and token register z in zero. Apply H to every
coin bit. Reversibly XOR f(x,r) into z, cleaning its computational scratch.
Reversibly XOR hfun(x,z) into r, cleaning that computational scratch.
The target r is not an input to hfun; the target z is not an input to f.
For an arbitrary purified joint input sum_x |x>|R_x>, the state is exactly

 sum_x |x>|R_x>|0>_r *(1/sqrt(M))*sum_(z contains x)|z>.

Measure/reset z and r. An identity token has Kraus I/sqrt(M); a copy
of a cell has Kraus Pi_cell/sqrt(M). Summing the copy tokens and
conditioning on nonidentity yields the exact weights c_cell/B=w_cell.
Identity probability R/M<1/4 is independent of the entire input/reference.
Each identity returns the input EXACTLY, including all reference systems.
After nonidentity perform the group CNOT/NOT cleanup in7.1. Every
released wire is zero on every input, and all private computational
scratch is clean. On product equatorial inputs, nonidentity token and
cell laws are independent of labels/phases, and the tensor-product,
disjoint-incidence and collimation conclusions in7.1 hold. No copy of
an unknown input is used as a second independent resource.

## 7.4. Explicit polynomial Boolean compilation and counted history

Put W=8*k^2*(b+1) and T0=2^128*(k+1)^64*(b+1)^64.
All integer operands above (factorials, denominator lcm, token counts,
partial permutation ranks, ID fields and constants) have at most W bits:
log2(k!)<=k*b, log2D<=k^2*b, coinbits<=k^2*b+3,
plus the k*O(b)-bit partner array. Bounds are public and are checked
before executing a word operation. There are only O(k) operand/list
words; a conservative O(k*W)-bit classical tape suffices.

For completeness a deliberately inefficient bounded Boolean program
implements this arithmetic as follows. Multiply by ordinary bitserial
schoolbook multiplication (<=O(W^2) bit operations), divide by W rounds
of shifted compare/subtract (O(W^2)), and compute gcd by at most2W
Euclidean divisions (O(W^3)). Compute factorial products serially; at
most k products per requested factorial and at most O(k^2) such requests
cover every weight, denominator and permutation block above. The lcm
uses at most k gcds. Scan the k input bits to count and select minority
positions; build U,V with stable bounded scans. Every selection of a
list entry by an unknown index is a scan over ALL k positions with an
equality flag and multiplexed word, and removal shifts every possible
position conditionally. Canonical matching sorting/validity uses at most
k^2 compare/exchanges, all on bounded fields. At most k rank/unrank
rounds use the bounded factorial/division programs. Zero divisors and
invalid inputs are assigned output0 by guards; real reachable f branches
have the positive divisors established above. All loops are run to their
public upper bounds with Boolean guards for inactive iterations.

These counts fit O(k^4*W^4) elementary Boolean tape operations. If an
address is data-dependent, replace the operation by a full scan of the
O(k*W)-bit tape and equality-controlled selection/write. This adds at
most O(k*W) overhead, avoiding any unknown-address memory instruction.
Public fixed-position accesses need no such replacement. With W=8k^2(b+1),
the resulting size is below 2^32*(k+1)^32*(b+1)^32; the generous powers
and constant cover all the displayed scans, guard operations, arithmetic
and their intermediate-bit copies. The exact algorithm is the specified
schoolbook/scan program with public bounds, not an oracle for a function.
Unrolling every bounded step yields a Boolean circuit; the constants and
wire addresses are generated by those public loops and charged too.

Convert this Boolean circuit to a clean reversible circuit by giving each
Boolean AND/XOR/NOT intermediate its own initially zero wire. AND uses
Toffoli; XOR uses CNOTs; negation uses NOT and a copy as appropriate.
Copy each result bit to the distinct output target and run the computation
in reverse, clearing every intermediate. Gate count and private wires are
at most a constant times the displayed Boolean size, hence below T0,
INCLUDING the two rank functions, coin/ID registers and their common
reuse. This explicitly counts the computation history; it does NOT claim
O(W) scratch by silently discarding intermediate quantum information.
The entire polynomial gate list can be stored in O(T0^2) ordinary
classical bits and generated in O(T0^2) classical bit work. This conservative
charge includes wire indices and constants, and is paid before use.
Table updates add O(k*n^2) bit work with O(k*n) current label bits.
Applying a generated gate also pays its address cost in proof.md. The
instrument uses no QRAM, exponential truth-table history, arbitrary
rotation or input-dependent uncharged advice.

For the public k in proof.md, with t=log2n>=32768,
 n<=k<=2n, log2(k+1)<=t+2, b+1<=t+3<=2t.
Therefore
 log2T0<=64t+320+64log2t<65t.
At t=32768 the last inequality has slack greater than30000; its slack
derivative is1-64/(t*ln2)>0 thereafter. Thus T0<=n^65 throughout
the main branch. All private history and gates have a fixed polynomial
bound, and the stored circuit/compilation costs at mostO(n^130).
This polynomial quantum workspace is counted in proof.md and is below
the declared exponential quantum envelope; it is NOT called linear.
No growing compiler exponential is hidden as an outside constant.

## 7.5. Finite identity retries

A reached macro runs at most Ltry=Y+ceilLog2(n)+64 trials. If all are
identity it ABORTs; otherwise it returns the first nonidentity output.
Trials acquire no source copies. The helper's exact identity-channel
statement couples this to the normalized instrument until the first
retry-cap failure, with conditional probability below4^-Ltry per start.
proof.md bounds the number of starts and all resource costs on EVERY
branch. The probability-only uncapped retry reference is never used
as a bound on actual runtime or actual workspace.
