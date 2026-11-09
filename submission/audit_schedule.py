"""Exact variable-width closed profiles; diagnostic only, not a proof verdict."""
from math import isqrt
from fractions import Fraction as F
import json
sigma=F('2/5');a=F('1356467/1000000');assert(a-F(1,10**6))**2>=2-sigma*sigma
count=0
for size in [328,330,656,1311,2622]:
 for offset in [-1,0,1]:
  x=(1<<size)+offset;n=x**100;U=x**49;L=(n-1).bit_length();r=isqrt(n)+(isqrt(n)**2<n)
  d=(sigma.numerator*r+sigma.denominator-1)//sigma.denominator;zarg=2*r*r-d*d;z=isqrt(zarg)+(isqrt(zarg)**2<zarg)
  m0=z-d;m=m0+64*U;ell=dl=d;w=d-1-8*U;k=n+(n%2==0);j=isqrt(k);kap=(m-1).bit_length()+1
  capacity=ell*w+m*dl+m*(m-1)//2+dl-1-m*kap
  loss=d*(1+8*U)+1+m*(kap+1)
  assert U**100==n**49 and (U-1)**100<n**49 and n>=1<<32768
  assert U>=L and r>2**20*U and m0>=0 and z>r
  assert F(67,100)*r<m<F(97,100)*r and 0<w<d<m<r and dl>=kap+1
  assert loss<11*r*U and capacity>=n and F(m+ell)+F(7*ell,j)<F(7,5)*r
  assert m+ell==z+64*U and m+dl==z+64*U and m+dl-w>F(6,10)*r
  assert 65*U*10**8<isqrt(n) and (256*L+192)*10**8<isqrt(n)
  assert F(3*8192*2*r*(k+1)*dl)>=16384*(k+1)*r*r
  count+=1
print(json.dumps(dict(diagnosticOnly=True,passed=True,closedProfiles=count,sigma=str(sigma),literalTimeClassicalSampleCoefficient=str(a),allFourSubleadingPowers='49/100',mathematicalVerdictExternal=True)))
