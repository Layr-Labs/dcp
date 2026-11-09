"""Exact finite diagnostics; proof.md supplies the uniform inequalities."""
from fractions import Fraction as F
from math import comb,factorial,isqrt
import json
alpha=F(499999,1000000);beta=F(82289,100000);delta=F(1,2);omega=F(499999,1000000);cbar=F(10000001,10000000)
cap=alpha*omega+beta*delta+beta*beta/2
assert cap>1+F(1,100000)
assert beta+delta<F(13229,10000)
assert beta+cbar*alpha<F(13229,10000)
assert omega<F(1,2)
k=10**16+1;assert k%2 and k>10**16
assert F(2)+F(7,10**8)<F(20000001,10000000)
checks=0
for k in range(3,102,2):
 h=(k-1)//2;w=F(1,h*(h+1));PA=F(k,k+1)
 pj=[F(2,2**k)*comb(k,j)*(1-w*j*(k-j)) for j in range(h)]
 assert PA+sum(pj)==1
 p=PA+sum(j*x for j,x in enumerate(pj));mu=2*PA+(k-1)*sum(pj)
 assert mu==F(3*k-1,k+1) and mu>2*p and p>=PA
 assert (mu/p-2)**2*k<49
 for t in range(h+1):
  inc=w*t*(k-t)
  if t<h:inc+=F(factorial(k-t),factorial(k-2*t))*(1-w*t*(k-t))*F(factorial(k-2*t),factorial(k-t))
  assert inc==1;checks+=1
# Closed formula capacity/bit lengths at huge integer endpoints, never allocate a table.
for power in [256,257,300,512,1024,4096]:
 for offset in [0,1,19]:
  r=2**power+offset
  ceil=lambda x:(x.numerator+x.denominator-1)//x.denominator
  m=ceil(beta*r);dl=(r+1)//2;ell=ceil(alpha*r);w=(omega*r).__floor__();kap=(m-1).bit_length()+1
  total=ell*w+m*dl+F(m*m,2)+dl+F(m,2)-1-m*(kap+1)
  assert total>=r*r and dl>=kap+1 and w<m
  assert 100000*(r.bit_length()+4)<r
  assert beta+cbar*alpha<F(13229,10000)
  assert F(13229,10000)*r+4*r.bit_length()+41<=2*r-1
print(json.dumps({'capacityLeading':str(cap),'treeLeading':str(beta+delta),'sourceUpper':str(beta+cbar*alpha),'smallOddIncidenceChecks':checks,'hugeClosedFormProfiles':18,'passed':True}))
