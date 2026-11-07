#!/usr/bin/env python3
"""Replay the exact unchanged decoder and held-out quotient diagnostics locally."""
import itertools,json,resource
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(60,)*2)
P=Path(__file__).resolve().parent
counts={}
def count(k,n=1):counts[k]=counts.get(k,0)+n
# Exact decoder circle-unwrapping, with deliberately biased coarse directions.
def circ(x):
 x=x%1
 return min(x,1-x)
for N in range(2,97):
 n=(N-1).bit_length();J=n+4
 for k in range(N):
  for bias in [-3,0,3]:
   alphas=[]
   for j in range(J+1):
    x=F((k*(1<<j))%N,N)
    nearest=(64*x+F(1,2)).__floor__()
    a=F((nearest+bias)%64,64)
    assert circ(a-x)<F(1,16)
    alphas.append(a)
   g=alphas[-1]
   for j in range(J-1,-1,-1):
    candidates=[g/2,(g+1)/2]
    g=min(candidates,key=lambda y:circ(y-alphas[j]))
   assert (N*g+F(1,2)).__floor__()%N==k
   count('exact_unwrapping_cases')
# CRT phase identity, including composites and signed W.
for N in range(3,97):
 M=N;a2=0
 while M%2==0:M//=2;a2+=1
 if M==1:continue
 d=N.bit_length()-1
 for j in range((M-1).bit_length()+1):
  residue=(pow(2,j,M)*pow(pow(2,d-1-a2,M),-1,M))%M
  alpha=next(x for x in range(N) if x%M==residue and x%(1<<a2)==1%(1<<a2))
  for s in range(N):
   for W in [-3,1,2]:
    assert (F((1<<(d-1))*W*alpha*s,N)-F((1<<j)*W*(s%M),M)).denominator==1
    count('exact_CRT_phase_cases')
# Full held-out block convolution for several signed incidence vectors.
for width in range(1,5):
 M=1<<width
 for zs in [(1,),(-1,), (1,-1),(1,0,-1),(1,1,-1)]:
  hist=[0]*M
  for hs in itertools.product(range(M),repeat=len(zs)):
   hist[sum(z*h for z,h in zip(zs,hs))%M]+=1
  assert len(set(hist))==1;count('held_out_quotient_laws')

out=dict(status='PASS',counts=counts,limits=dict(address_space_bytes=512<<20,cpu_seconds=60),script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),scope='Finite exact checks of unchanged CYG1/PPSA decoder and quotient laws; not all-N mathematical certification.')
(P/'results/decoder.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
