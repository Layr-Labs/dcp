"""Research-only exact contained-token construction, no quantum execution."""
from fractions import Fraction as F
from math import factorial,lcm
from collections import defaultdict
import json

def parameters(k):
 h=(k-1)//2;a=F(1,h*(h+1));weights=[(1-a*j*(k-j))*F(factorial(k-2*j),factorial(k-j))for j in range(h)]
 D=a.denominator
 for w in weights:D=lcm(D,w.denominator)
 bits=(D-1).bit_length()+2;M=1<<bits;scale=M//D;B=scale*D
 return a,weights,D,M,B

def data(x,k):
 one=[i for i in range(k)if x>>i&1];zero=[i for i in range(k)if not(x>>i&1)];return (one,zero)if len(one)<len(zero)else(zero,one)

def forward(x,r,k,par):
 a,weights,D,M,B=par
 if r>=B:return ('I',r-B)
 small,big=data(x,k);t=len(small);ca=int(B*a);cut=t*(k-t)*ca
 if r<cut:
  rank,c=divmod(r,ca);i,j=divmod(rank,k-t);u,v=sorted((small[i],big[j]));return ('A',((u,v),),c)
 assert t<(k-1)//2
 cj=int(B*weights[t]);rank,c=divmod(r-cut,cj);pairs=[];rest=big[:]
 for i,u in enumerate(small):
  rem=t-i-1;block=factorial(len(rest)-1)//factorial(len(rest)-1-rem);q,rank=divmod(rank,block);z=rest.pop(q);pairs.append(tuple(sorted((u,z))))
 assert rank==0
 return ('J',tuple(sorted(pairs)),c)

def inverse(x,token,k,par):
 a,weights,D,M,B=par
 if token[0]=='I':return B+token[1]
 kind,pairs,c=token;small,big=data(x,k);t=len(small);ca=int(B*a)
 if kind=='A':
  (u,v),=pairs
  if u not in small:u,v=v,u
  return (small.index(u)*(k-t)+big.index(v))*ca+c
 rank=0;partners={u:v for u,v in pairs}|{v:u for u,v in pairs};rest=big[:]
 for i,u in enumerate(small):
  q=rest.index(partners[u]);rem=t-i-1;block=factorial(len(rest)-1)//factorial(len(rest)-1-rem);rank+=q*block;rest.pop(q)
 return t*(k-t)*ca+rank*int(B*weights[t])+c

def contains(x,tok,k):
 if tok[0]=='I':return True
 kind,pairs,c=tok
 if any(((x>>i)^(x>>j))&1==0 for i,j in pairs):return False
 if kind=='A':return True
 used={i for p in pairs for i in p};rest=[i for i in range(k)if i not in used]
 return all((x>>i&1)==(x>>rest[0]&1)for i in rest)

checks=0;out=[]
for k in [3,5,7]:
 par=parameters(k);M=par[3];supports=defaultdict(set)
 for x in range(1<<k):
  tokens=[forward(x,r,k,par)for r in range(M)];assert len(set(tokens))==M
  for r,tok in enumerate(tokens):
   assert contains(x,tok,k) and inverse(x,tok,k,par)==r
   supports[tok].add(x);checks+=1
 for tok,s in supports.items():assert s=={x for x in range(1<<k)if contains(x,tok,k)}
 out.append(dict(k=k,D=par[2],coinSize=M,globalTokens=len(supports)))
print(json.dumps(dict(passed=True,rankInverseAndFullProjectorSupportChecks=checks,profiles=out,scope='finite research diagnostic; polynomial circuit proof not yet written or reviewed')))

from math import isqrt
from fractions import Fraction
leading=Fraction(330719,250000)
assert (leading-Fraction(3,10**7))**2>Fraction(7,4)
profiles=0
for logn in [32768,32769,33024,65536,131072]:
 for offset in [-1,0,1]:
  n=(1<<logn)+offset
  if n<(1<<32768):continue
  L=(n-1).bit_length();r=isqrt(n)+(isqrt(n)**2<n);z=isqrt(7*n)+(isqrt(7*n)**2<7*n)
  k=n+(n%2==0);j=isqrt(k);b=(k-1).bit_length()
  m0=(z-r+1)//2;m=m0+256*L;ell=dl=(r+1)//2;w=r//2-128*L;kap=(m-1).bit_length()+1
  K=8192*(2*r+L+30);T0=2**128*(k+1)**64*(b+1)**64
  capacity=ell*w+m*dl+m*(m-1)//2+dl-1-m*kap
  assert T0<=n**65 and k*ell<=n*n and k<=2*n and 0<2*w<r<2*m and m<r and dl>=kap+1
  assert capacity>=n and z>2*r and K<n
  assert Fraction(7*ell,j)<=28
  assert Fraction(m+ell)+Fraction(7*ell,j)<Fraction(7,5)*r
  assert Fraction(7,5)*r+6*r.bit_length()+43<=2*r-1
  assert 3*K*(k+1)*dl>k*r+2*k
  assert n>10**800 and (1024*L+128)*10**8<isqrt(n) and 130*L<isqrt(n)
  profiles+=1
print(json.dumps(dict(passed=True,mainClosedProfiles=profiles,linearGroupPolynomialCompiler=True,privateQuantumHistoryPolynomial65Counted=True,sourceYieldExcessBoundedByConstant28=True,sourceAndTreeBothCharged=True,scope='finite diagnostics; supplied uniform mathematical proofs required')))
