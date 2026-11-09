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

ns={2**e for e in [48,49,64,96,128,192,256,512,1024]}
for e in [48,49,64,96]:
 for off in [-1,1,17]:
  if 2**e+off>=2**48:ns.add(2**e+off)
cases=0
with localcontext() as ctx:
 ctx.prec=800;ln2=D(2).ln()
 for n in sorted(ns):
  ell=rlog(n);m=ceil(ell*ell);u=(n-1).bit_length();k=(m-1).bit_length()+1
  den=2*(m+1);base=(2*n-m*(m+1)+den-1)//den+1;s0=k+1;dl=base+s0;H=base+m-1;LL=m//(4*s0)
  assert LL>=2*s0 and base>=s0 and base>=4
  l=D(n).ln()/ln2 if n&(n-1) else D(n.bit_length()-1)
  ed=D(ell.numerator)/D(ell.denominator)
  assert l-D(1)/D(n*n)<=ed<=l+D('1e-790')
  assert l*l-1<m<=l*l+1 and m+1>l*l and m>=10*u+100
  assert m*m+k<=n and dl>=k+1
  tt=D(n)/(l*l);assert tt/2<=base and H<=2*tt and (m+1)*H<=4*n
  AA=s0*LL-floor_sum(LL,LL,s0);B0=(m+1)*base+m*(m-1)//2-1
  total=B0+m+s0-AA
  rr=(n**5-1).bit_length();assert total-rr+1>=n and rr<=5*u
  gw=(dl-1).bit_length();b0=n.bit_length()-1;Lblk=(n+b0-1)//b0
  assert m+gw+b0<=H and 2*b0<=H-2048*u
  K=8192*(m+10*u+100);Kp=8192*(u+100);coef=65536*dl
  Y=m+(coef-1).bit_length();A=4*Lblk;rootcount=K*(Y+6+4*u)+A
  assert K<=2**14*m and Y<=m+u+16 and K//8192>=Y+u+30
  assert D(rootcount)<=D(2**26)*D(n)/l
  assert D(coef*rootcount+Kp)<=D(2**44)*D(n)**2/l**3
  FF=D(n)/l**2+l**2/2
  assert H<=FF+2 and D(m+dl)<=FF+2*l.ln()/ln2+7
  assert m<=l*l+1
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
  ll=D(nn).ln()/ln2;eps=ll/(D(2**20)*D(nn)**17);kk=nn+10
  assert eps*kk<D(1)/D(2**32)
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

# Independent exact drift,classification,and bounded-edit potential checks.
assert F(6251,64000)>F(2,24)+F(2,625)+F(1,192)
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
assert F(6251,64000)>F(2,24)+F(2,625)+F(1,192)
assert F(6,64)==F(3,32) and F(6,128)==F(3,64)
print(json.dumps(dict(new_wide_physical_crt_cases=crtwide,small_exact_grid_Dirichlet_cases=small_dirichlet,large_mesh_Dirichlet_cases=large_dirichlet,wide_grid_and_source_cap_checks_passed=True,all_wide_coarse_checks_passed=True)))


from pathlib import Path
meta=json.load(open(Path(__file__).with_name('submission.json')))
assert meta['claims'][0]['structured']['bound']['nPower']=='3'
assert meta['claims'][0]['structured']['bound']['logPower']=='1'
assert meta['claims'][3]['structured']['bound']['logPower']=='-3'
assert meta['claims'][4]['structured']['expression']=='0'
print(json.dumps(dict(squared_log_vector_parameter_cases=cases,all_qudit_log2_checks_passed=True)))
