#!/usr/bin/env python3
"""Finite exact carry/top-bit laws, supplier identities and decoder margins."""
import resource
resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(50,)*2)
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import gcd
from hashlib import sha256
import json,time,subprocess

P=Path(__file__).resolve().parents[1]
start=time.process_time();counts={}
def count(name):counts[name]=counts.get(name,0)+1

for N in range(2,513):
    n=(N-1).bit_length();d=N.bit_length()-1
    a=(N&-N).bit_length()-1;M=N>>a
    assert F(1<<d,N)>F(1,2)
    if M>1:
        assert d-1>=a
        for j in range(min(6,d+1)):
            alphaM=(1<<j)*pow(1<<(d-1-a),-1,M)%M
            alpha=alphaM if a==0 else alphaM+M*((1-alphaM)*pow(M,-1,1<<a)%(1<<a))
            assert gcd(alpha,N)==1
            assert alpha%M==alphaM and (a==0 or alpha%(1<<a)==1)
            for s in sorted({0,1,N//2,N-1}):
                for W in (-17,-3,-1,0,1,2,19):
                    assert ((1<<(d-1))*W*alpha*s)%N==((1<<j)*W*(s%M)*(1<<a))%N
                    count('odd_part_phase_identities')
    for s in sorted({0,1,N//2,N-1}):
        s1=s%M;s2=((s-s1)//M)%(1<<a)
        for g in range(a):
            low=s2% (1<<g);wd=a-g
            sh=(s1+M*low)%N
            rem=((s2-low)>>g)%(1<<wd)
            assert (s-sh)%N==(M*(1<<g)*rem)%N
            for W in (-7,-1,1,5):
                root=(1<<(wd-1))*W
                assert (root*((s-sh)%N))%N==(N//2)*(W*rem%2)
                count('two_adic_phase_identities')

# The two chosen rows have the same low residue. Their signed quotient keeps
# the carry, and the top bits remain fair without conditioning on full labels.
for low in product(range(2),repeat=4):
    values={r:sum(low[i] for i in range(4) if r>>i&1) for r in range(16)}
    for e in range(2):
        fiber=[r for r in range(16) if values[r]%2==e]
        if len(fiber)<4:continue
        C=fiber[:4]
        for eta in range(2):
            x,y=C[2*eta:2*eta+2]
            z=[((y>>i)&1)-((x>>i)&1) for i in range(4)]
            assert any(abs(t)==1 for t in z)
            carry=(values[y]-values[x])//2
            histogram={};real=imag=0
            for high in product(range(2),repeat=4):
                full=[low[i]+2*high[i] for i in range(4)]
                diff=sum(z[i]*full[i] for i in range(4))
                assert diff%2==0
                W=diff//2
                assert W==carry+sum(z[i]*high[i] for i in range(4))
                histogram[W%2]=histogram.get(W%2,0)+1
                rr,ii=((1,0),(0,1),(-1,0),(0,-1))[W%4]
                real+=rr;imag+=ii
            assert histogram=={0:8,1:8} or histogram=={1:8,0:8}
            # y=1/4: squared characteristic modulus <= cos(pi/4)^2=1/2.
            assert F(real*real+imag*imag,16*16)<=F(1,2)
            count('root_carry_parity_characteristic_laws')

assert F(511,512)-F(31,32)>2*F(1,256)
assert F(511,512)/2-F(37,40)/2>F(2,64)+F(2,625)
assert F(2,1024)+F(1,2**19)<F(1,256)
assert F(2,1024)+F(1,2**14)+F(1,2**20)<F(1,2**8)
assert F(1,2**10)<F(1,2**8)
for n in (1,2,255,256,1024):
    for Qcap in (1,17,2**100+7):
        target=2**16*Qcap*(n+5)
        h=(target-1).bit_length()
        assert F(4*(n+5),1<<h)<=F(1,2**14*Qcap)
        count('extraction_precision_guards')

out={'status':'PASS','timestamp':subprocess.check_output(['date','+%Y-%m-%d %H:%M:%S %Z (%z)'],text=True).strip(),
     'counts':counts,'cpu_seconds_used':time.process_time()-start,
     'limits':{'cpu_seconds':50,'address_space_bytes':512<<20},
     'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact finite modular identities and analytic-constant guards; not a DCP circuit simulation.'}
(P/'decoder-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
