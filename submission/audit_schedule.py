from math import isqrt
from fractions import Fraction as F
import json
count=0
for lg in [32768,32769,33024,65536,131072]:
 for off in [-1,0,1]:
  n=(1<<lg)+off
  if n<1<<32768:continue
  r=isqrt(n)+(isqrt(n)**2<n);L=(n-1).bit_length();k=n+(n%2==0);dl=(r+1)//2
  b0=r//64;Kp=8192*(b0+L+100);Kc=8192*(2*r+L+30);Lblk=(n+b0-1)//b0
  assert b0>=F(r,128) and 1<=b0<n and Kp<=Kc
  assert Lblk<=129*r and 2*r+6+2*Lblk<=512*r<=3*n
  for R in [Kp,Kc]:
   normalized=4*(k+1)*r+3*R*dl
   assert normalized>=k*r+2*k+3*R*dl
   assert normalized<=2**18*r**3
  assert Kp>=288*(b0+L+32)
  assert 1-3*F(1,2**16)-3*F(1,2**18)-F(1,2**20)-F(1,2**29)-F(1,2**10)-F(1,2**125)>1-F(1,2**8)
  assert 512*F(1,2**25)==F(1,2**16) and 512*F(4,2**29)==F(1,2**18)
  count+=1
print(json.dumps(dict(diagnosticOnly=True,passed=True,roundedProfiles=count,additiveResidueAndDemand=True,wideScoreUnionChecked=True,mathematicalVerdictExternal=True)))

"""Exact rounded capacity checks for proposed deeper classical caps, no verdict."""
from math import isqrt
from fractions import Fraction as F
import json
counts={}
for name,beta,shift,source,lossbase,limit in [('CAP86',F(107,130),11008,None,64,323),('Q13CAP',F(67,80),1728,F(13,10),136,204)]:
 count=0;eta=F(13,10);d0=beta+F(1,2)-eta
 for lg in [32768,32769,33024,65536,131072]:
  for offset in [-1,0,1]:
   n=(1<<lg)+offset
   if n<1<<32768:continue
   L=(n-1).bit_length();r=isqrt(n)+(isqrt(n)**2<n);m0=(beta.numerator*r+beta.denominator-1)//beta.denominator;m=m0+256*L;dl=(r+1)//2;ell=dl if source is None else 13*r//10-m-16*L
   w=r//2-128*L;H=13*r//10-shift*L;kap=(m-1).bit_length()+1
   growing=min(m,max(0,H-dl+1));sums=growing*dl+growing*(growing-1)//2+(m-growing)*H
   capacity=ell*w+dl+sums-1-m*kap
   Bc=shift*L+1;A=256*L
   loss=lossbase*r*L+(F(r,2)if source is None else F(3*r,2))+1+d0*Bc*r+F(Bc*Bc,2)+A*Bc+m*(kap+1)
   gain=A*eta*r if source is None else A*F(4,5)*r
   guard=32 if source is None else 24
   assert r>2**guard*L and dl<H<dl+m and H>r and w>0 and dl>=kap+1 and m<r
   assert capacity>=n and loss<limit*r*L<gain
   assert F(Bc*Bc,2)+A*Bc<r*L
   address=2**20+16*r+4096*L
   log_alloc_upper=256+max(H+3*L,w+3*L,130*L,8*L)
   assert log_alloc_upper<=address<=17*r
   assert L*L<=r and r*r<=4*n and address*address<=2048*n
   Kc=8192*(2*r+L+30);Kp=8192*(L+100);b0=n.bit_length()-1;Lblk=(n+b0-1)//b0
   assert (2*r+6)*Kc+2*Lblk*Kp+Kp<=2**20*n
   count+=1
 counts[name]=count
print(json.dumps(dict(researchOnly=True,passed=True,roundedProfiles=counts,newCapLogMultipliers=[11008,1728],intendedClassicalPowers=[-11000,-1700],mathematicalVerdictExternal=True)))

"""Exact finite checks of unused-block frequency and physical CRT identities."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import gcd
import json
counts=dict(uniformIncidence=0,independentRootPairs=0,oddPhysicalCRT=0,signedReconstruction=0,twoAdicPhysical=0)
for h in range(1,5):
 q=1<<h
 for coeff in product([-1,0,1],repeat=3):
  if not any(coeff):continue
  hist=Counter(sum(a*b for a,b in zip(coeff,tau))%q for tau in product(range(q),repeat=3))
  assert len(hist)==q and len(set(hist.values()))==1;counts['uniformIncidence']+=1
for h in range(1,4):
 q=1<<h
 for c0,c1 in product(product([-1,1],repeat=2),repeat=2):
  hist=Counter(((c0[0]*t[0]+c0[1]*t[1])%q,(c1[0]*t[2]+c1[1]*t[3])%q)for t in product(range(q),repeat=4))
  assert len(hist)==q*q and len(set(hist.values()))==1;counts['independentRootPairs']+=1
for M in [257,509,1021,4093]:
 Y=1;R0=F(M,1<<(Y+8))+F(1,2);assert R0>=1 and R0/M<=F(1,1<<(Y+7))
 for a2 in range(4):
  N=(1<<a2)*M;dn=N.bit_length()-1;n=(N-1).bit_length()
  for b in range(1,5):
   B=dn-b;assert B>=a2+1;gamma=pow(2,B-a2,M);K0=pow(-(1<<b),-1,M);J=((1<<b)*K0+1)//M
   assert ((1<<b)*K0+1)%M==0 and J%2==1 and 1<=J<=1<<b
   for j in range(7):
    am=K0*pow(1<<j,-1,M)*pow(gamma,-1,M)%M;mod2=1<<a2
    alpha=am if mod2==1 else am+M*((1-am)*pow(M,-1,mod2)%mod2)
    assert gcd(alpha,N)==1 and (gamma*alpha-K0*pow(1<<j,-1,M))%M==0 and alpha%mod2==1%mod2
    for tj in range(-int(R0),int(R0)+1):
     cj=37%M;s1=(cj+(1<<j)*tj)%M;s=s1+M*((j+1)%mod2)
     for W in [-1<<(Y+b),-3,-1,0,1,3,1<<(Y+b)]:
      phase=F((1<<B)*W*alpha*(s-cj),N);target=F(K0*W*tj,M);model=F(J*W*tj,1<<b)-F(W*tj,(1<<b)*M)
      assert (phase-target).denominator==1 and target==model
      assert 8*abs(F(W*tj,(1<<b)*M))<=F(1,16)
      counts['oddPhysicalCRT']+=1
  for t0 in range(-int(R0),int(R0)+1):
   low=j=0
   while j<n:
    b=min(3,n-j);tj=(t0-low)//(1<<j);assert (t0-low)%(1<<j)==0 and abs(tj)<=R0
    residue=tj%(1<<b);low+=residue*(1<<j);j+=b
   got=low if low<(1<<(n-1))else low-(1<<n);assert got==t0;counts['signedReconstruction']+=1
  for s2 in range(1<<a2):
   for g in range(a2):
    wd=a2-g;b=min(3,wd);B=wd-b;low=s2%(1<<g);rem=(s2-low)//(1<<g);s1=37%M;s=s1+M*s2;sh=(s1+M*low)%N
    for W in [-3,-1,0,1,3]:
     assert (F((1<<B)*W*(s-sh),N)-F(W*rem,1<<b)).denominator==1;counts['twoAdicPhysical']+=1
assert F(1,2)-2*F(1,16)-2*F(1,625)>F(1,4)
assert 2+2*F(1,625)<3 and F(8192,288)>2 and F(8192*100,288)>30
failure=3*(F(1,2**16)+F(1,2**18))+F(1,2**20)+F(1,2**29)+F(1,2**10)+F(1,2**125);assert failure<F(1,2**8)
print(json.dumps(dict(diagnosticOnly=True,passed=True,counts=counts,rationalFailureBudget=str(failure),mathematicalVerdictExternal=True)))

from fractions import Fraction as F
from math import factorial,lcm,isqrt
import json
profiles=0;containing=0
for k in range(5,130,2):
 h=(k-1)//2;b=(k-1).bit_length();r=isqrt(k);w=F(1,h*(h+1));weights=[(1-w*j*(k-j))*F(factorial(k-2*j),factorial(k-j))for j in range(h)]
 D=lcm(w.denominator,*(x.denominator for x in weights));pad=4*r+64;coin=(D-1).bit_length()+pad;M=1<<coin;B=(M//D)*D;R=M-B;ca=B*w
 assert ca.denominator==1 and F(R,M)<F(1,1<<pad)
 W=8*k*k*(b+1);assert coin+k*(b+1)+3*b+10<=W
 for t in range(h+1):
  ac=t*(k-t)*ca;jc=F(0)if t==h else F(factorial(k-t),factorial(k-2*t))*B*weights[t]
  assert ac+jc+R==M
  for wt in [w]+weights:assert (B*wt).denominator==1 and F(B*wt,B)==wt
  containing+=1
 profiles+=1
for lg in [32768,32769,33024,65536]:
 n=1<<lg;r=isqrt(n);L=(n-1).bit_length();assert -2*r+L-61<-125
print(json.dumps(dict(diagnosticOnly=True,passed=True,oddSizes=profiles,minorityContainingMassIdentities=containing,newCoinRegistersCounted=True,mathematicalVerdictExternal=True)))
