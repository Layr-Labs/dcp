"""Exact perfect-power main-profile diagnostics; not a proof or quantum run."""
from math import isqrt
from fractions import Fraction as F
import json
count=0
a=F(1336661,1000000)
assert (a-F(1,2)-F(9,10**7))**2>F(7,10)
for size in [328,330,656,1311,2622]:
 for offset in [-1,0,1]:
  z=(1<<size)+offset;n=z**100;U=z**49
  assert U**100==n**49 and (U-1)**100<n**49
  L=(n-1).bit_length();r=isqrt(n)+(isqrt(n)**2<n);t0=(7*r*r+9)//10;m0=isqrt(t0)+(isqrt(t0)**2<t0)
  k=n+(n%2==0);j=isqrt(k);m=m0+64*U;ell=13*r//10-m-8*U;dl=(r+1)//2;w=r//2-8*U;kap=(m-1).bit_length()+1
  capacity=ell*w+m*dl+m*(m-1)//2+dl-1-m*kap
  loss=12*r*U+F(3*r,2)+1+m*(kap+1)
  assert n>=1<<32768 and U>=L and r>2**20*U and 64*U<F(r,1000)
  assert 0<2*w<r<2*m and m<F(84,100)*r and F(45,100)*r<ell<r and dl>=kap+1
  assert loss<15*r*U and F(256,5)*r*U>loss and capacity>=n
  assert m+ell==13*r//10-8*U and F(m+ell)+F(7*ell,j)<=F(13,10)*r-8*U+28
  assert 65*U*10**8<isqrt(n) and (256*L+128)*10**8<isqrt(n)
  assert 7*U>=65*L and F(13,10)*r-8*U+28+6*r.bit_length()+43<=2*r-1
  count+=1
print(json.dumps(dict(diagnosticOnly=True,passed=True,exactPerfectPowerProfiles=count,allFourLiteralSubleadingPowers='49/100',mathematicalVerdictExternal=True)))
