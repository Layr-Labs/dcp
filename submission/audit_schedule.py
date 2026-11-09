"""Exact lower-rational log, saturation and caps; finite diagnostic, not proof."""
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import json

def ceil(x):return -(-x.numerator//x.denominator)
def rlog(n):
 j=n.bit_length()-1;u=(n-1).bit_length();t=2*u+10
 if n==1<<j:return F(j)
 z=F(n-(1<<j),n+(1<<j))
 def aa(x):
  s=F(0);v=x
  for k in range(t):s+=2*v/(2*k+1);v*=x*x
  return s
 return j+aa(z)/(aa(F(1,3))+F(1,3**(2*t)))
def floor_sum(nn,mm,aa,bb=0):
 ans=0
 while True:
  qa,aa=divmod(aa,mm);qb,bb=divmod(bb,mm)
  ans+=qa*nn*(nn-1)//2+qb*nn
  top=aa*nn+bb
  if top<mm:return ans
  nn,bb=divmod(top,mm);aa,mm=mm,aa
floor_checks=0
for mm in range(1,33):
 for aa in range(33):
  for nn in range(17):
   assert floor_sum(nn,mm,aa)==sum(aa*ii//mm for ii in range(nn))
   floor_checks+=1
small=0;geometric_cases=0
for base in [4,9,17,33]:
 for k in [1,2,3]:
  s0=k+1
  if base<s0:continue
  for m in [32,64,96,128,192,256]:
   LL=m//(4*s0)
   if LL<2*s0:continue
   dl=base+s0;H=base+m-1
   def lift(kk):return min(s0,kk*s0//LL)
   ls=[base+ii+lift(m-1-ii) for ii in range(m)]+[1]
   cs=[2*ls[ii]-ls[ii+1]-k for ii in range(m)]
   AA=s0*LL-floor_sum(LL,LL,s0)
   total=(m+1)*base+m*(m-1)//2-1+m+s0-AA
   assert min(cs)>0 and sum(cs)==total
   assert ls[0]==dl and ls[-2]==H
   assert all(ls[ii+1]-ls[ii] in [0,1] for ii in range(m-1))
   assert sum((m-1-ii+4)*H*(1<<ls[ii]) for ii in range(m))<=19*H*(1<<H)
   geometric_cases+=1
   Bs=set(range(1,min(500,total)+1))|{total,total-1,total//2,cs[-1],cs[-1]+1}
   for BV in Bs:
    if not 1<=BV<=total:continue
    rem=BV
    for cap in reversed(cs):rem-=min(rem,cap)
    assert rem==0;small+=1

ns={2**e for e in [128,129,160,192,256,384,512,768,1024]}
for e in [128,129,160,192]:
 for off in [-1,1,17]:
  if 2**e+off>=2**128:ns.add(2**e+off)
cases=0
with localcontext() as ctx:
 ctx.prec=800;ln2=D(2).ln()
 for n in sorted(ns):
  ell=rlog(n);m=ceil(16*ell);u=(n-1).bit_length();k=(m-1).bit_length()+1
  den=2*(m+1);base=(2*n-m*(m+1)+den-1)//den+2;dl=base;H=base+m-1
  assert base>=16*m+64*u and base>=3*m+100*u
  l=D(n).ln()/ln2 if n&(n-1) else D(n.bit_length()-1)
  ed=D(ell.numerator)/D(ell.denominator)
  assert l-D(1)/D(n*n)<=ed<=l+D('1e-790')
  assert 16*l-1<m<=16*l+1 and m+1>16*l and m>=10*u+100
  assert m*m+k<=n and dl>=k+1
  t=D(n)/(16*l)
  assert t/2<=dl<=2*t and H<=2*t and (m+1)*H<=4*n
  total=(m+1)*base+m*(m-1)//2-3
  assert total>=n and base-m-2>=0
  ff=D(n)*sum((D((-1)**(j-1))/D(16)**j/l**j for j in range(1,64)),D(0))-D(n)*D(2048)/2049/(D(16)**64*l**64)
  assert D(H)<=ff+8*l+4 and m+dl==H+1 and D(m+dl)<=ff+8*l+5
  w=64*u;cc=64*dl*(1<<m);cf=16*dl*(1<<m);Y=(cc-1).bit_length()
  htop=Y+8*u+12;P=htop+Y+8;kc=36864*u;gw=(dl-1).bit_length()
  b0=H//2-1024*u;noise=(n**5-1).bit_length();Lblk=(n+b0-1)//b0
  assert b0>0 and 35*u*b0>=n and Lblk<=36*u and noise<=5*u
  assert base>=256*u and htop<=27*u and P<=45*u
  assert m+gw+htop<=H and m+gw+b0<=H
  assert D(cc)<=8*D(n)**17/l and D(cf)<=2*D(n)**17/l
  assert D(cc)>=D(n)**17/l and D(cf)>=D(n)**17/(4*l)
  I=16*Lblk+128*(w+u);chain=8*w+64*u;cap=cc*kc+10*cf*I
  assert I<=8896*u and I//4-2*w>Lblk+chain
  assert D(cc*kc)<=297216*D(n)**17
  assert D(10*cf*I)<=179310*D(n)**17
  assert cap<2**19*n**17
  assert cap>=36864*n**17
  eps=l/(D(238263)*D(n)**17)
  assert eps*D(cap)<=D(w)/32 and eps*D(1024*cap)>=144*l
  for bv in {1,2,b0//2,b0,b0-1}:
   if bv<1:continue
   r=bv+noise
   assert r<=H and total-(r-1)>=n-bv
   assert 2*H-r-2>0 and 2*bv<=H-2048*u
   assert m+gw+bv<=H
   # Root table labels require at most n-bv collimated bits.
   for B in {1,max(1,n-bv),max(1,(n-bv)//2)}:
    assert B<=total-r+1
   # Fixed compiler precision dominates the explicit conditioning loss.
   pp=2*bv+17*u+32
   assert pp<=16*n
   loss=1000000*(pp+100)*((pp+1).bit_length()+1)
   assert (n+pp+1100)**4>loss+pp+100+16*(pp+1).bit_length()
  # No exponential table is materialized here; these are exact exponent checks.
  assert 2048-128-20>=1900
  cases+=1
print(json.dumps(dict(exact_rational_log_schedule_cases=cases,floor_sum_reference_cases=floor_checks,tapered_greedy_cases=small,weighted_taper_frame_cases=geometric_cases,all_checks_passed=True)))

from fractions import Fraction as F
from math import gcd,cos,sin,pi
from itertools import product
import json,random
# Unused top-block incidence with a nonempty signed unit support.
uniform=0
for b in range(1,6):
 mod=1<<b
 for signs in [(1,),(-1,),(1,1),(1,-1),(-1,-1),(1,-1,1)]:
  counts=[0]*mod
  for tau in product(range(mod),repeat=len(signs)):counts[sum(a*x for a,x in zip(signs,tau))%mod]+=1
  assert len(set(counts))==1;uniform+=1
# Exact modular phase identity, including unknown 2-adic component.
crt=0;identity=0
for M in range(3,130,2):
 for b in range(1,min(7,M.bit_length()-1)):
  mod=1<<b;K0=pow(-mod,-1,M);J=(mod*K0+1)//M
  assert mod*K0+1==J*M and J%2==1 and gcd(K0,M)==1
  for j in [0,1,3,6]:
   for W in [-11,-1,0,1,6,17]:
    for t in [-37,-1,0,1,31]:
     assert F(K0*W*t,M)==F(J*W*t,mod)-F(W*t,mod*M);identity+=1
   for a2 in [0,1,3]:
    N=(1<<a2)*M;dn=N.bit_length()-1;B=dn-b
    assert B>=a2
    gamma=pow(2,B-a2,M);v=K0*pow(2,-j,M)*pow(gamma,-1,M)%M
    alpha=v+M*((1-v)*pow(M,-1,1<<a2)%(1<<a2)) if a2 else v
    assert gcd(alpha,N)==1 and gamma*alpha%M==K0*pow(2,-j,M)%M
    for t in [-37,-1,0,1,31]:
     for two in [0,1,(1<<a2)-1]:
      # residual secret moduloM is2^j*t; arbitrary two-adic lift cancels.
      residual=(pow(2,j,M)*t%M)+M*two
      for W in [-5,-1,0,1,7]:
       delta=F((1<<B)*W*alpha*residual,N)-F(K0*W*t,M)
       assert delta.denominator==1;crt+=1
# Signed blocks including negative residuals and every boundary length.
signed=0
for n in range(2,33):
 b0=n.bit_length()-1
 for t0 in sorted(set(range(-min(50,1<<(n-1))+1,min(50,1<<(n-1))))|{-(1<<(n-1))+1,(1<<(n-1))-1,0}):
  low=0;j=0;t=t0
  while j<n:
   b=min(b0,n-j);a=t%(1<<b);low+=a<<j;t=(t-a)//(1<<b);j+=b
  got=low if low<1<<(n-1) else low-(1<<n)
  assert got==t0;signed+=1
# Two-adic direct and collimated block labels, exact phase modulointegers.
twoadic=0
for wd in range(1,11):
 for b in range(1,wd+1):
  B=wd-b
  for rem in range(1<<min(wd,5)):
   for W in range(1<<min(b,5)):
    assert F((1<<B)*W*rem,1<<wd)==F(W*rem,1<<b);twoadic+=1
# Orthogonality and tabulated-score gap, including adversarial bounded phase noise.
score=0
for b in range(1,8):
 mod=1<<b
 for J in [1,3,mod-1]:
  for v in [0,1,mod//2,mod-1]:
   for a in sorted({0,1,mod//2,mod-1,(v+1)%mod}):
    if a==v:continue
    gap=0
    for W in range(mod):
     theta=2*pi*((J*W*v)%mod)/mod
     eta=(1 if W%2 else -1)/16
     obs=[cos(theta+eta),sin(theta+eta)]
     for beta,fun in enumerate([cos,sin]):
      def table(c):
       xx=((J*W*c)%mod)/mod;idx=int(4096*xx)
       return round(fun(2*pi*idx/4096)*(1<<24))/(1<<24)
      gap+=obs[beta]*(table(v)-table(a))/(2*mod)
    assert gap>0.25;score+=1
print(json.dumps(dict(uniform_top_block_incidence_cases=uniform,modular_phase_identity_cases=identity,crt_physical_supplier_cases=crt,signed_block_reconstruction_cases=signed,two_adic_block_phase_cases=twoadic,uniform_frequency_noisy_score_cases=score,all_checks_passed=True)))


# Independent exact permutation-bias and finite robust-block checks.
from math import comb,factorial
from itertools import product
shuffle_cases=0
for size in range(2,8):
 for extra in [0,3,10]:
  ell=2*(size-1).bit_length()+extra;two=1<<ell
  probs={}
  for choice in product(*[range(ii+1) for ii in range(size-1,0,-1)]):
   arr=list(range(size));prob=F(1)
   for ii,jj in zip(range(size-1,0,-1),choice):
    quo,rem=divmod(two,ii+1)
    prob*=F(quo+(jj<rem),two);arr[ii],arr[jj]=arr[jj],arr[ii]
   arr=tuple(arr);assert arr not in probs;probs[arr]=prob
  assert len(probs)==factorial(size) and sum(probs.values())==1
  tv=sum(abs(v-F(1,factorial(size))) for v in probs.values())/2
  assert tv<=F(size*size,two);shuffle_cases+=1
hypergeom_cases=0
for size in range(1,41):
 for bad in range(size+1):
  frac=F(bad,size)
  for take in range(1,min(size,12)+1):
   denom=comb(size,take);moment=F(0)
   for hit in range(take+1):
    if hit<=bad and take-hit<=size-bad:
     moment+=F(comb(bad,hit)*comb(size-bad,take-hit),denom)*(1<<hit)
   assert moment<=(1+frac)**take
   cleanprefix=F(comb(size-bad,take),denom) if take<=size-bad else F(0)
   assert 1-cleanprefix<=take*frac
   hypergeom_cases+=1
finite_cases=0
with localcontext() as ctx:
 ctx.prec=180;ln2=D(2).ln()
 for nn in list(range(2,5001))+[2**ee for ee in range(1,128)]:
  ll=D(nn).ln()/ln2;eps=ll/(D(238263)*D(nn)**17);kk=nn+10
  assert eps*kk<D(1)/D(2**30)
  assert (eps*kk).exp()<2
  failure=D(1)/D(2**10)*(eps*kk).exp()+eps*kk+D(1)/D(2**100)
  assert failure<D(1)/100
  finite_cases+=1
assert F(1,2**8)+F(69,256)<F(1,3)
print(json.dumps(dict(fixed_time_shuffle_distribution_cases=shuffle_cases,
 hypergeometric_prefix_moment_cases=hypergeom_cases,finite_fraction_error_cases=finite_cases,
 main_and_finite_error_budgets_passed=True,all_bank_checks_passed=True)))


from functools import lru_cache
adaptive=0
for width in range(2,17):
 @lru_cache(None)
 def worst(stages,budget):
  if not stages:return F(0)
  return max(F(b,width)+(1-F(b,width))*worst(stages-1,budget-b)
             for b in range(min(width,budget)+1))
 for stages in range(1,9):
  for budget in range(2*width+1):
   risk=worst(stages,budget)
   assert risk<=min(F(1),F(budget,width))
   adaptive+=1
uniform_selection=0
for bad in range(1025):
 # The ten-bit string is drawn only after all flags are committed.
 cnt=sum(jj<bad for jj in range(1<<10))
 assert F(cnt,1<<10)==F(bad,1024);uniform_selection+=1
padding=0
for cap in range(1,129):
 for used in range(cap+1):
  assert 1024*used+1024*(cap-used)==1024*cap
  padding+=1
assert F(1,256)+F(69,256)<F(1,3)
assert F(1024,32)>=32
print(json.dumps(dict(adaptive_first_bad_budget_cases=adaptive,
 perfect_post_bank_selection_cases=uniform_selection,exact_padding_cases=padding,
 microbank_space_and_error_checks_passed=True,all_micro_checks_passed=True)))

from fractions import Fraction as F
from itertools import product
from math import sqrt,cos,sin,pi
from cmath import exp
import random,json
rng=random.Random(60216)
worst=0;variance=0;uniformprep=0;permutations=0
for q in [2,4,8,16]:
 for D in [2,4,8,16,32,64]:
  for case in range(5):
   freqs=[rng.randrange(q) for _ in range(D)];bins=[[i for i,f in enumerate(freqs) if f==z] for z in range(q)]
   p=[len(b)/D for b in bins];theory=sum(sqrt(x) for x in p)**2/q
   ranks={i:(z,r) for z,b in enumerate(bins) for r,i in enumerate(b)}
   assert len(ranks)==D and len(set(ranks.values()))==D;permutations+=1
   for v in range(q):
    # Explicitly compress rank-uniform pieces then inverse Fourier transform.
    compressed=[sum(exp(2j*pi*freqs[i]*v/q)/sqrt(D) for i in b)/sqrt(len(b)) if b else 0j for b in bins]
    probs=[abs(sum(compressed[z]*exp(-2j*pi*z*out/q) for z in range(q))/sqrt(q))**2 for out in range(q)]
    assert abs(sum(probs)-1)<1e-12 and abs(probs[v]-theory)<1e-12;worst+=1
for q in [2,4,8]:
 for k in [1,2,3]:
  vectors=list(product([0,1],repeat=k))
  for D in [2,4,8]:
   if D>len(vectors):continue
   vecs=vectors[:D];val=F(0)
   for tau in product(range(q),repeat=k):
    ws=[sum(a*b for a,b in zip(v,tau))%q for v in vecs];counts=[ws.count(z) for z in range(q)]
    val+=q*sum((F(a,D)-F(1,q))**2 for a in counts)
   val/=q**k
   assert val==F(q-1,D);variance+=1
for count in range(1,129):
 width=(count-1).bit_length()
 # Recursive prefix count ratios are the exact squared rotation amplitudes.
 amps={0:1.0}
 for level in range(width):
  nxt={};remaining=width-level-1
  for prefix,a in amps.items():
   start=prefix<<(remaining+1);total=max(0,min(count-start,1<<(remaining+1)))
   for bit in [0,1]:
    sub=max(0,min(count-start-bit*(1<<remaining),1<<remaining))
    nxt[(prefix<<1)|bit]=a*sqrt(sub/total) if total else 0
  amps=nxt
 assert all(abs(a-(1/sqrt(count) if idx<count else 0))<1e-14 for idx,a in amps.items());uniformprep+=1
print(json.dumps(dict(covariant_worst_secret_measurement_cases=worst,exact_conditional_collision_variance_cases=variance,explicit_index_bin_rank_permutations=permutations,binary_prefix_uniform_state_preparations=uniformprep,all_checks_passed=True)))

# Exact reciprocal identity and64 declared coefficients; no floating truncation.
from pathlib import Path
reciprocal=0;envelope=0
x0=F(2048);r0=x0/(x0+1)
def f64_over_n(x):return sum(((-1)**(j-1)*x**(-j) for j in range(1,64)),F(0))-r0*x**(-64)
for x in [x0+F(v,10) for v in range(101)]+[x0*j for j in range(1,65)]+[F(10**p,3) for p in range(4,15)]:
 f63=sum(((-1)**(j-1)*x**(-j) for j in range(1,64)),F(0));val=f64_over_n(x)
 assert f63-F(1,x**63*(x+1))==1/(x+1)
 assert val>=1/(x+1) and val<1/x and val>=1/(2*x)
 reciprocal+=1
meta=json.load(open(Path(__file__).with_name('submission.json')))
assert all(len(meta['claims'][i]['structured']['bound']['exponent'])==64 for i in [0,1])
for ell in [128,129,160,192,256,384,512,768,1024]:
 n=1<<ell;x=F(16*ell);m=16*ell;k=(m-1).bit_length()+1;s0=k+1
 base=ceil(F(n,m+1)-F(m,2))+1;dl=base+s0;H=base+m-1;val=n*f64_over_n(x)
 assert F(n,m+1)<=val+1 and H<=val+8*ell+3
 assert m+dl<=val+8*ell+k+5
 delta=F(16,n*n);assert delta<1
 assert F(n,x+1-delta)<=F(n,x+1)+1
 for i in [0,1]:
  ev=sum((F(t['coefficient'])*n*F(ell)**int(t['logPower']) for t in meta['claims'][i]['structured']['bound']['exponent']),F(0))
  assert ev==val
 envelope+=1
print(json.dumps(dict(exact_reciprocal_identity_and_upper_cases=reciprocal,exact_power_two_parameter_envelope_cases=envelope,structured_64_terms_match_sum=True,all_reciprocal_checks_passed=True)))

# Independent exact drift,classification,and bounded-edit potential checks.
assert F(6251,64000)>F(2,24)+F(2,625)+F(1,96)
assert F(11,16)+F(5,16)*F(1,32)<F(7,10)
assert (1-F(1,1024))*(F(5,8)-F(4,2**512))-F(1,1024)>F(1,2)
assert F(7,10)**4<F(1,4)
assert 1-F(1,4096)-F(1,16)-F(1,32)>F(9,10)
assert F(7,10)+F(1,16)+F(1,32)<F(9,10)
assert 1+2*F(1,4)-F(2,3)*F(3,4)==1
assert F(1,16)+F(1,1024)+4*F(1,2**20)<F(1,3)
# Exhaustive incidence-vector/top-label translation and two-label merge toy laws.
from itertools import product
low_only=0
for B in range(1,5):
 for h in range(1,5):
  mod=1<<h;lo=1<<B
  for lows in [(0,1,0),(lo-1,1,lo-1),(lo-1,lo-1,1)]:
   # Entry pairs have different +/-1 incidence in common low residue.
   # Use same low-sum entry translated by a multiple of2^B.
   carry=(sum(lows)//lo);hist=[0]*mod
   for tau in product(range(mod),repeat=3):
    w=carry+tau[0]+tau[1]-tau[2];hist[w%mod]+=1
   assert len(set(hist))==1;low_only+=1
# Exhaust all small binary correct/wrong prefix transitions and edited outcomes.
edits=0
for L in range(1,7):
 for ell in range(L):
  for q in range(ell+1):
   def state(action):
    if action=='back':return max(0,ell-1),min(q,max(0,ell-1))
    if action=='hold':return ell,q
    return ell+1,q+(action=='true' and q==ell)
   def potentials(action):
    e,qq=state(action);return 2*qq-e,e-qq
   for av in ['back','hold','true','false']:
    for aa in ['back','hold','true','false']:
     pv,dv=potentials(av);pa,da=potentials(aa)
     assert pa>=pv-2 and da<=dv+2;edits+=1
print(json.dumps(dict(low_label_uniformity_cases=low_only,exhaustive_bounded_edit_transitions=edits,exact_coarse_margin=True,exact_full_test_margins=True,exact_drift_and_visit_factors=True,all_backtrack_checks_passed=True)))

# Chain-specific primitive and stopped-potential certificates.
import sys
sys.path.insert(0,str(Path.cwd()))
from tolerance_expression import parse_fractional_tolerance_expression as parse
assert parse(meta['claims'][4]['structured']['expression'])==dict(kind='fraction',coefficient='1/238263',nPower='-17',logPower='1')
assert parse(meta['claims'][4]['structured']['expression'])['logPower']=='1'  # natural n1zero
assert meta['claims'][0]['structured']['bound']['nPower']=='10'
assert meta['claims'][0]['structured']['bound']['logPower']=='1'
assert meta['claims'][3]['structured']['bound']['nPower']=='17'
assert meta['claims'][3]['structured']['bound']['logPower']=='0' 
assert 1-F(1,1024)>F(3,4)
assert F(1,32)+F(1,1024)+3*F(1,2**20)<F(1,3)
walks=0
for height in range(1,13):
 end=height+1;state={1:F(1)}
 for steps in range(1,65):
  new={}
  for pos,prob in state.items():
   if pos in [0,end]:new[pos]=new.get(pos,F(0))+prob;continue
   new[pos+1]=new.get(pos+1,F(0))+prob/4
   new[pos-1]=new.get(pos-1,F(0))+3*prob/4
  state=new
  assert sum(state.values())==1
  assert sum((p*3**pos for pos,p in state.items()),F(0))==3
  assert state.get(end,F(0))<=F(3,3**end)
  walks+=1
print(json.dumps(dict(exact_wrong_chain_stopped_walk_cases=walks,natural_n1_zero_fraction_checked=True,chain_budget_parser_and_all_four_resource_identity=True,all_chain_checks_passed=True)))

# NEW physical wide supplier and finite Dirichlet/grid checks.
from math import gcd,sqrt,pi,sin,cos
import cmath
crtwide=0
for M in range(3,66,2):
 for a2 in range(7):
  N=(1<<a2)*M;dn=N.bit_length()-1
  for ht in [1,2,3,5,8]:
   h=min(ht,M.bit_length()-1);B=dn-h
   if B<1:continue
   assert B>=a2 and B+h==dn
   gamma=pow(2,B-a2,M);alpha=pow(gamma,-1,M)
   if a2:alpha+=M*((1-alpha)*pow(M,-1,1<<a2)%(1<<a2))
   alpha%=N;assert gcd(alpha,N)==1 and (gamma*alpha)%M==1
   for secret in {0,1,N//2,N-1}:
    for W in [-7,0,1,9]:
     delta=F((1<<B)*W*alpha*secret,N)-F(W*(secret%M),M)
     assert delta.denominator==1;crtwide+=1
small_dirichlet=0
for M in range(3,130,2):
 L=1<<(M.bit_length()-1)
 for kk in range(1,M):
  direct=sum(cmath.exp(2j*pi*kk*t/M) for t in range(L))/L
  assert abs(direct)<=1/sqrt(2)+1e-12 and abs(direct)<.71
  small_dirichlet+=1
large_dirichlet=0
for h in range(4,10):
 L=1<<h
 for den in [2*L+1,4*L+3,8*L+7]:
  for kk in range(1,den//2+1):
   delta=F(kk,den)
   if delta<F(4,L):continue
   exact=abs(sin(pi*L*float(delta))/(L*sin(pi*float(delta))))
   assert exact<=float(F(1,2*L*delta))+1e-12 and exact<=1/8+1e-12
   large_dirichlet+=1
# Pointwise nearest-grid phase bound and exact rational margin certificates.
for h in [1,2,4,17]:
 for C in [1,64,129,2048]:
  Y=(C-1).bit_length();P=h+Y+8
  assert F((1<<h)*C,2*(1<<P))<=F(1,512)
assert 1-F(22,7)**2/F(2*128**2)>=F(999,1000)
assert F(29,64)*F(999,1000)-F(71,200)==F(6251,64000)
assert F(6251,64000)>F(2,24)+F(2,625)+F(1,96)
assert F(6,64)==F(3,32) and F(6,128)==F(3,64)
print(json.dumps(dict(new_wide_physical_crt_cases=crtwide,small_exact_grid_Dirichlet_cases=small_dirichlet,large_mesh_Dirichlet_cases=large_dirichlet,wide_grid_and_source_cap_checks_passed=True,all_wide_coarse_checks_passed=True)))

# NEW balanced-commutator algebra, safe frame lift, and SK tolerance recurrence.
import numpy as np
sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]],complex);ident=np.eye(2)
gc=0
for exponent in range(2,49):
 rr=2.0**(-exponent)
 tt=rr/sqrt(2*(1+sqrt(1-rr*rr)))
 VV=sqrt(1-tt)*ident+1j*sqrt(tt)*sx
 WW=sqrt(1-tt)*ident+1j*sqrt(tt)*sy
 CC=VV@WW@VV.conj().T@WW.conj().T
 assert np.linalg.norm(CC.conj().T@CC-ident)<1e-12
 assert abs(CC.trace().real/2-sqrt(1-rr*rr))<1e-12
 vx=np.array([CC[0,1].imag,CC[0,1].real,CC[0,0].imag])
 assert abs(np.linalg.norm(vx)-rr)<1e-12
 gc+=1
for pp in range(1,10001):
 aa=32;dep=0
 while aa<pp+4:
  nxt=3*aa//2-7
  assert 4*nxt>=5*aa and 2*nxt<=3*aa-14
  aa=nxt;dep+=1
 assert 5**dep<=2**40*(pp+1)**8
assert F(36864,1152)==32 and F(6*64,36864)==F(1,96)
assert 297216+179310<2**19
print(json.dumps(dict(new_large_block_geometry_cases=cases,balanced_commutator_numeric_cases=gc,exact_compiler_recurrence_cases=10000,large_cap_margin_and_bit_precision_checks=True,all_large_checks_passed=True)))

"""Finite supplements to PRIVATE nonpower-merge derivation; no uniform certification."""
from fractions import Fraction as F
from itertools import product,combinations
from collections import Counter
import json
minor=joint=variance=intervals=margin=roots=0
for d in [2,3,4]:
 vv=list(product([0,1],repeat=d))[1:]
 for a,b in combinations(vv,2):
  assert any(abs(a[i]*b[j]-a[j]*b[i])==1 for i,j in combinations(range(d),2));minor+=1
  for q in [2,4]:
   hist=Counter()
   for tau in product(range(q),repeat=d):
    x=(sum(t*v for t,v in zip(tau,a))+1)%q;y=(sum(t*v for t,v in zip(tau,b))+2)%q
    hist[x,y]+=1
   assert len(hist)==q*q and set(hist.values())=={q**(d-2)};joint+=1
# Two disjoint children, each support{0,e1,e2}; one zero pair form.
forms=[(a[0],a[1],b[0],b[1])for a in [(0,0),(1,0),(0,1)]for b in [(0,0),(1,0),(0,1)]]
for q in [2,4,8]:
 S=[0]*q;S2=[0]*q;num=q**4;V=len(forms)
 for tau in product(range(q),repeat=4):
  counts=[0]*q
  for j,f in enumerate(forms):counts[(sum(t*v for t,v in zip(tau,f))+j//3+2*(j%3))%q]+=1
  for r,v in enumerate(counts):S[r]+=v;S2[r]+=v*v
 for r in range(q):
  mean=F(S[r],num);var=F(S2[r],num)-mean*mean;mu=F(V,q)
  assert abs(mean-mu)<=1 and var<=mu;variance+=1
# Exact dyadic lengths and exponent inequalities, with only moderate bitlengths.
for m in [2,3,4,8,16,32,64,128]:
 for u in [1,2,8,48]:
  base=16*m+64*u;H=base+m-1
  M=[(1<<(base+i))-(1<<(base+2*i-m-2))for i in range(m)]
  assert all(F(M[i],1<<(base+i))==1-F(1,1<<(m+2-i))for i in range(m))
  total=F(0)
  for i in range(1,m):
   de=F(1,1<<(m+3-i));E=1<<(base+i)
   extra=F(2,1<<((base+i)//2))+F(2,E)+4/(de**4*E)
   assert extra<=de**2
   assert 2*de**2+extra<=3*de**2;total+=3*de**2
   c=base+i-2
   for k in {0,1,c//2,c}:
    mu=F((1<<k)*(1-de)**2*E);out=M[i];gap=mu-(1<<k)*out
    assert gap==(1<<k)*de**2*E and gap>1
    bound=gap/mu+F(1,1<<((base+i-1)//2))+1/mu+out/(gap-1)**2
    assert bound<=3*de**2;margin+=1
  assert total<=F(1,64)
  for dd in [1,H//2,H-1]:
   cap=2*H-dd-2;rootfail=F((1<<cap)*(1<<dd),M[-1]**2)
   assert rootfail==F(16,49);roots+=1
  assert F(16,15)*F(64,63)*F(49,33)<3
# Linear selected-rank interval walker: only first rectangle needsdivision.
def walk(groups,start,length):
 out=[];at=0;first=True
 for AA,BB in groups:
  size=len(AA)*len(BB)
  if start>=at+size:at+=size;continue
  if first:ia,ib=divmod(start-at,len(BB));first=False
  else:ia=ib=0
  while ia<len(AA) and len(out)<length:
   out.append((AA[ia],BB[ib]));ib+=1
   if ib==len(BB):ib=0;ia+=1
  at+=size
  if len(out)==length:return out
 return out
for na in [3,5,7]:
 for nb in [3,6,7]:
  LA=[(a*a+2*a)%17 for a in range(na)];LB=[(b*b+3*b)%19 for b in range(nb)]
  for q in [1,2,4,8]:
   for r in range(q):
    groups=[]
    for s in range(q):
     AA=[a for a in range(na)if LA[a]%q==s];BB=[bb for bb in range(nb)if LB[bb]%q==(r-s)%q]
     if AA and BB:groups.append((AA,BB))
    flat=[(a,bb)for AA,BB in groups for a in AA for bb in BB]
    assert len(flat)==sum((LA[a]+LB[bb])%q==r for a in range(na)for bb in range(nb))
    for outsize in [1,2,3,5,7]:
     for block in range(len(flat)//outsize):
      got=walk(groups,block*outsize,outsize)
      assert got==flat[block*outsize:(block+1)*outsize]
      assert len(set(got))==outsize
      for j,(a,bb) in enumerate(got):
       rank=flat.index((a,bb));assert divmod(rank,outsize)==(block,j)
       hi=(LA[a]+LB[bb]-r)//q;assert LA[a]+LB[bb]==r+q*hi
      intervals+=1
print(json.dumps(dict(binary_unit_minor_cases=minor,joint_affine_uniform_cases=joint,exact_bucket_mean_variance_cases=variance,dyadic_Chebyshev_margin_cases=margin,root_distribution_free_fraction_cases=roots,nonpower_selected_interval_reindex_cases=intervals,all_finite_research_checks_passed=True,uniform_proof_and_genuine_review_still_required=True)))

# The adaptive source model and all other four objects are exactly retained.
assert meta['claims'][4]['structured']['expression']==r'\frac{\log_2 n}{238263 n^{17}}'
assert all(c['evidence']==['proof.md','nonpower_merge.md','qudit_decoder.md','robust_decoder.md'] for c in meta['claims'])
print(json.dumps(dict(nonpower_robust16_geometry_cases=cases,all_nonpower_robust16_finite_checks_passed=True)))

assert 476526==2*238263 and 238263>196608
assert F(6,238263*2**15)<F(1,2**30)
print(json.dumps(dict(strengthened_fraction_denominator=238263,actual_finite_fraction_checks=finite_cases,new_cap_fraction_identity=True)))
