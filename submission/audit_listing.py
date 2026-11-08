"""Compare bounded implicit pair-fiber listing with brute-force tuples.
Small finite classical diagnostic; not a quantum simulation or proof premise.
"""
from heapq import heappush,heappop
from itertools import product
from random import Random
import json
rng=Random(748193)

def stream_pairs(fiber,reverse=False):
 # Independently group by first coordinate and sort its restricted second run.
 rows={}
 for key,a,b in fiber:rows.setdefault(a,[]).append((key,b))
 heap=[]
 for a,values in rows.items():
  values.sort(reverse=reverse)
  key,b=values[0];heappush(heap,((-key if reverse else key),a,0,b))
 while heap:
  signed,a,j,b=heappop(heap);yield (-signed if reverse else signed),a,b
  j+=1
  if j<len(rows[a]):
   key,b=rows[a][j];heappush(heap,((-key if reverse else key),a,j,b))

def listed(X,Y,rp,target,Cp):
 out=[]
 for g in range(4):
  tg=target+g*2**rp
  sx=iter(stream_pairs(X));sy=iter(stream_pairs(Y,True))
  hx=next(sx,None);hy=next(sy,None)
  while hx is not None and hy is not None:
   z=hx[0]+hy[0]
   if z<tg:hx=next(sx,None);continue
   if z>tg:hy=next(sy,None);continue
   ky=hy[0];buf=[]
   while hy is not None and hy[0]==ky:
    if len(buf)<Cp:buf.append(hy)
    hy=next(sy,None)
   kx=hx[0]
   while hx is not None and hx[0]==kx:
    for eta in buf:
     out.append((hx[1],hx[2],eta[1],eta[2]))
     if len(out)==Cp:return out
    hx=next(sx,None)
 return out

cases=0;cut=0;overflows=0;small=0
for L,r,rp in [(4,1,2),(8,2,3),(16,3,4)]:
 for trial in range(40):
  # The planted low-label case exercises ties and overflowing fibers.
  labs=[[j%(2**r) for j in range(L)] for _ in range(4)] if trial==0 else [[rng.randrange(2**(r+rp)) for _ in range(L)] for _ in range(4)]
  rho=[[v%2**r for v in row] for row in labs];sg=[[v//2**r for v in row] for row in labs]
  for _ in range(8):
   v,v2,tg=[rng.randrange(2**z) for z in [r,r,rp]]
   cAB,cCD=rng.randrange(2),rng.randrange(2)
   X=[(sg[0][a]+sg[1][b]+(rho[0][a]+rho[1][b]+cAB)//2**r,a,b) for a,b in product(range(L),repeat=2) if (rho[0][a]+rho[1][b]+cAB)%2**r==v]
   Y=[(sg[2][a]+sg[3][b]+(rho[2][a]+rho[3][b]+cCD)//2**r,a,b) for a,b in product(range(L),repeat=2) if (rho[2][a]+rho[3][b]+cCD)%2**r==v2]
   for Cp in [1,3,17,65]:
    got=listed(X,Y,rp,tg,Cp)
    expected={(x[1],x[2],y[1],y[2]) for x,y in product(X,Y) if (x[0]+y[0])%2**rp==tg}
    assert len(set(got))==len(got)==min(Cp,len(expected))
    assert set(got)<=expected
    if len(expected)<=Cp:assert set(got)==expected;small+=1
    else:overflows+=1
    cases+=1
  # An all-zero pair fiber exceeds the deterministic first-stage cap.
  mX=L*L//2**r
  zero_pair_fiber=[(a,b) for a,b in product(range(L),repeat=2)]
  assert len(zero_pair_fiber)>2*mX if r>1 else len(zero_pair_fiber)==2*mX
  if r>1:cut+=1
window_cases=0
for _ in range(5000):
 p0=rng.randrange(1,9);r0=rng.randrange(1,5);r1=rng.randrange(1,6);b=r0+r1
 constants=[rng.randrange(2**p0) for _ in range(4)]
 high=[rng.randrange(2**(b+3)) for _ in range(4)]
 labels=[c+2**p0*h for c,h in zip(constants,high)]
 ca=(constants[0]+constants[1])//2**p0;cc=(constants[2]+constants[3])//2**p0
 cl=((constants[0]+constants[1])%2**p0+(constants[2]+constants[3])%2**p0)//2**p0
 low=[v%2**r0 for v in high];sg=[(v//2**r0)%2**r1 for v in high]
 vx=(low[0]+low[1]+ca)%2**r0;vy=(low[2]+low[3]+cc)%2**r0
 gx=(low[0]+low[1]+ca)//2**r0;gy=(low[2]+low[3]+cc)//2**r0
 kx=sg[0]+sg[1]+gx;ky=sg[2]+sg[3]+gy
 val=sum(labels)//2**p0
 assert val==(vx+vy+cl)+2**r0*(kx+ky)+2**b*sum(v//2**b for v in high)
 assert val%2**r0==(vx+vy+cl)%2**r0
 assert (val//2**r0)%2**r1==(kx+ky+(vx+vy+cl)//2**r0)%2**r1
 window_cases+=1
print(json.dumps({'window_identity_cases':window_cases,'listing_cases':cases,'small_complete_fibers':small,'overflow_cases':overflows,'planted_pair_cut_checks':cut,'all_checks_passed':True}))


"""Exact modular identities, signed residual induction, and CRT supplier checks."""
from math import gcd
from fractions import Fraction
cases=0
for M in range(3,130,2):
 K0=(M-1)//2
 assert gcd(K0,M)==1
 for a2 in range(5):
  N=M<<a2; dn=N.bit_length()-1; B=dn-1
  assert B>=a2
  gamma=pow(2,B-a2,M)
  for c in (0,1,M//2,M-1):
   for t in range(-min(8,(M-1)//2),min(8,(M-1)//2)+1):
    s=(c+t)%M
    low=0
    for j in range(8):
     assert (t-low)%(1<<j)==0
     tj=(t-low)//(1<<j)
     cj=(c+low)%M
     alphaM=K0*pow(2,-j,M)*pow(gamma,-1,M)%M
     alpha=next(alphaM+k*M for k in range(1<<a2) if (alphaM+k*M)%(1<<a2)==1%(1<<a2))
     assert gcd(alpha,N)==1
     for W in (-7,-1,0,1,2,7):
      # Exact root phase modulo one including the 2-adic part of any full s.
      for z in (0, max(0,(1<<a2)-1)):
       fulls=s+M*z
       assert ((1<<B)*W*alpha*(fulls-cj)-((N//M)*K0*W*tj))%N==0
      # exp(2pi i K0 W tj/M)=(-1)^(W tj) exp(-pi i W tj/M).
      assert (Fraction(K0*W*tj,M)-Fraction(W*tj,2)+Fraction(W*tj,2*M)).denominator==1
     low+=(tj%2)<<j
     assert abs((t-low)//(1<<(j+1)))<=max(1,abs(t))
     cases+=1
    signed=low if low<128 else low-256
    assert signed==t and (c+signed)%M==s
print('exact near-parity supplier/signed-bit cases',cases)
# Bootstrap radius and nonwrapping signed n-bit reconstruction.
for Y in range(2,12):
 for M in ((1<<(Y+7))+1,(1<<(Y+8))-1,(1<<(Y+12))+3):
  R=Fraction(M,1<<(Y+8))+Fraction(1,2)
  assert R>=1 and R/M<=Fraction(1,1<<(Y+7))
  assert (1<<(Y+1))*R/M<=Fraction(1,64)
  for n in range(M.bit_length(),M.bit_length()+3):
   assert R<Fraction(1<<(n-1))
print('bootstrap radius, phase slack, signed-range cases passed')


rounding_cases=0
for YY in range(2,10):
 for MM in ((1<<(YY+7))+1,(1<<(YY+7))+3,(1<<(YY+10))-1):
  NN=MM.bit_length()
  RR=Fraction(MM,1<<(YY+8))+Fraction(1,2)
  for ss in {0,1,MM//2,MM-2,MM-1}:
   for eps in (Fraction(-1,1<<(YY+8)),Fraction(0),Fraction(1,1<<(YY+8))):
    zz=(Fraction(ss,MM)+eps)%1
    xx=MM*zz+Fraction(1,2)
    cc=(xx.numerator//xx.denominator)%MM
    tt=(ss-cc)%MM
    if tt>MM//2:tt-=MM
    assert abs(tt)<=RR and abs(tt)<Fraction(MM,2)
    ll=0
    for jj in range(NN):
     tj=(tt-ll)//(1<<jj)
     assert abs(tj)<=RR
     assert Fraction((1<<(YY+1))*abs(tj),MM)<=Fraction(1,64)
     ll+=(tj%2)<<jj
    assert (ll if ll<1<<(NN-1) else ll-(1<<NN))==tt
    assert (cc+tt)%MM==ss
    rounding_cases+=1
print('exact circular bootstrap/rounding and signed-stage cases',rounding_cases)

def audit_cost_filtration():
 """Finite data-flow diagnostic: child/ghost costs ignore unused parent windows."""
 from fractions import Fraction
 from random import Random
 rr=Random(9017364);pdom=Fraction(3,4);cases=0;changed=0
 def one_attempt(labels,flat,aux):
  aa=[0,labels[0],labels[1],labels[0]+labels[1]]
  bb=[0,labels[2],labels[3],labels[2]+labels[3]]
  fibres=[[] for _ in range(4)]
  for x in range(4):
   for y in range(4):fibres[(aa[x]+bb[y])%4].append((x,y))
  q=Fraction(sum(len(f)%4 for f in fibres),16)
  assert q<=pdom
  x,y=flat%4,flat//4;e=(aa[x]+bb[y])%4;f=fibres[e]
  rk=f.index((x,y));start=(rk//4)*4
  fail=start+4>len(f)
  uu=q*aux if fail else q+(1-q)*aux
  assert (uu<=q)==fail and (uu>pdom)<= (not fail)
  chosen=() if fail else tuple((u|(v<<2),aa[u]+bb[v]) for u,v in f[start:start+4])
  return fail,uu,chosen
 def call(records,variant,seed):
  flip=Random(seed+variant*1000003);actual=None
  for tt,(base,flat,aux) in enumerate(records):
   lab=base if not variant else [(x%4)+4*flip.randrange(16) for x in base]
   fail,uu,chosen=one_attempt(lab,flat,aux)
   if actual is None and not fail:actual=(tt,chosen)
   if uu>pdom:
    assert actual is not None
    fingerprint=(actual[0],tuple((mask,val%4) for mask,val in actual[1]))
    return 4*(actual[0]+1),4*(tt+1),fingerprint,actual[1]
  raise AssertionError('finite deterministic toy guard reached')
 for seed in range(96):
  for child in range(4):
   records=[([rr.randrange(64) for _ in range(4)],rr.randrange(16),Fraction(rr.randrange(1,258),258)) for _ in range(256)]
   base=call(records,0,seed*11+child)
   assert base[0]<=base[1]
   for variant in range(1,17):
    new=call(records,variant,seed*11+child)
    assert new[:3]==base[:3]
    changed+=new[3]!=base[3];cases+=1
 assert changed>0
 print('unused-window child/ghost-cost invariance cases',cases,'changed high-label outputs',changed)
audit_cost_filtration()

# Actual descending-width window shapes at small sizes.
desc=0
for HH,jj in [(3,0),(4,0),(5,0),(6,1)]:
 lam=HH-jj;aux=HH+1+2*jj;r0=2*lam-aux;LL=2**lam
 for lp in [1,lam-1]:
  kk=2;r1=2*aux-lp-kk;cap=8*2**(lp+kk)+1
  assert r0>=1 and r1>=1 and aux<=2*lam
  for trial in range(4):
   vv=0;vv2=0
   lo=[[rng.randrange(2**r0) for _ in range(LL)] for _ in range(4)]
   hi=[[rng.randrange(2**r1) for _ in range(LL)] for _ in range(4)]
   XX=[(hi[0][aa]+hi[1][bb]+(lo[0][aa]+lo[1][bb])//2**r0,aa,bb) for aa,bb in product(range(LL),repeat=2) if (lo[0][aa]+lo[1][bb])%2**r0==vv]
   YY=[(hi[2][aa]+hi[3][bb]+(lo[2][aa]+lo[3][bb])//2**r0,aa,bb) for aa,bb in product(range(LL),repeat=2) if (lo[2][aa]+lo[3][bb])%2**r0==vv2]
   if not XX or not YY:continue
   target=(XX[0][0]+YY[0][0])%2**r1
   expected={(xx[1],xx[2],yy[1],yy[2]) for xx,yy in product(XX,YY) if (xx[0]+yy[0])%2**r1==target}
   got=listed(XX,YY,r1,target,cap)
   assert len(set(got))==len(got)==min(cap,len(expected)) and set(got)<=expected
   desc+=1
print('descending-width listing shapes',desc,'passed')
