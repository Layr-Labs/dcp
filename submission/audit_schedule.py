"""Exact balanced perfect-power schedule diagnostics; no proof verdict."""
from math import isqrt
from fractions import Fraction as F
import json
count=0;a=F(330719,250000)
assert (a-F(3,10**7))**2>F(7,4)
for size in [328,330,656,1311,2622]:
 for offset in [-1,0,1]:
  x=(1<<size)+offset;n=x**100;U=x**49
  assert U**100==n**49 and (U-1)**100<n**49
  L=(n-1).bit_length();r=isqrt(n)+(isqrt(n)**2<n);z=isqrt(7*n)+(isqrt(7*n)**2<7*n);m0=(z-r+1)//2
  k=n+(n%2==0);j=isqrt(k);m=m0+64*U;ell=dl=(r+1)//2;w=r//2-8*U;kap=(m-1).bit_length()+1
  capacity=ell*w+m*dl+m*(m-1)//2+dl-1-m*kap
  loss=4*r*U+F(r,2)+1+m*(kap+1)
  assert n>=1<<32768 and U>=L and r>2**20*U and (64*U+31)*1000<r
  assert F(82,100)*r<m<F(824,1000)*r and 0<2*w<r and ell<r and dl>=kap+1
  assert loss<7*r*U and 64*r*U>loss and capacity>=n
  assert F(m+ell)+F(7*ell,j)<F(7,5)*r
  assert 65*U*10**8<isqrt(n) and (256*L+192)*10**8<isqrt(n) and 7*U>=65*L
  count+=1
print(json.dumps(dict(diagnosticOnly=True,passed=True,exactBalancedPerfectPowerProfiles=count,allFourLiteralSubleadingPowers='49/100',mathematicalVerdictExternal=True)))
