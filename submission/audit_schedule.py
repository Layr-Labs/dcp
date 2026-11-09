from math import isqrt
from fractions import Fraction as F
import json
count=0
for size in [328,330,656,1311,2622]:
 for off in [-1,0,1]:
  x=(1<<size)+off;n=x**100;U=x**49;r=isqrt(n)+(isqrt(n)**2<n);L=(n-1).bit_length()
  m=(107*r+129)//130+64*U;ell=dl=(r+1)//2;w=r//2-8*U;H=13*r//10-128*U;kap=(m-1).bit_length()+1
  growing=min(m,max(0,H-dl+1));su=growing*dl+growing*(growing-1)//2+(m-growing)*H
  cap=ell*w+dl+su-1-m*kap;A=64*U;Bc=128*U+1
  loss=4*r*U+F(r,2)+1+F(3,130)*Bc*r+F(Bc*Bc,2)+A*Bc+m*(kap+1)
  assert U>=L and r>2**20*U and 0<w<F(r,2)<m<r and dl<H<dl+m and H>r
  assert loss<12*r*U<A*F(13,10)*r and cap>=n
  assert 65*U*10**8<isqrt(n) and (256*L+192)*10**8<isqrt(n)
  assert F(1323077,1000000)-F(86,65)==F(1,13000000)
  assert m+ell+28<F(7,5)*r and L*L<=r
  count+=1
print(json.dumps(dict(diagnosticOnly=True,passed=True,closedProfiles=count,fullUniformProofRequired=True)))

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
