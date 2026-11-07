#!/usr/bin/env python3
"""Exact finite arithmetic diagnostics, each run <=768 MiB and <=60 CPU seconds."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,resource,time
P=Path(__file__).resolve().parent
cfg=json.loads((P/'protocol.json').read_text());lim=cfg['limits']
resource.setrlimit(resource.RLIMIT_AS,(lim['address_space_bytes'],)*2)
resource.setrlimit(resource.RLIMIT_CPU,(lim['cpu_seconds'],)*2)
from profile import *
start=time.process_time();counts={}
def count(k):counts[k]=counts.get(k,0)+1
# Independent direct capacity search and exact square telescope at all modest tops.
jumps={};guards=[]
for kind in ['critical-sqrt',*cfg['comparison_rules']]:
    prev=0;down=[]
    for B in range(2 if kind!='critical-sqrt' else 1,4097,2 if kind=='inherited-quarter' else 1):
        vs=profile(B,kind);c=sum(vs);u=base(B,kind)
        assert c<=B*B
        assert 2*c*drop(B,kind)>=B*B-u*u
        assert all(vs[i-1]==vs[i]-drop(vs[i],kind) for i in range(1,len(vs)))
        if c<prev:down.append([B,prev,c])
        prev=c;count('exact_top_capacity_checks')
    jumps[kind]=dict(count=len(down),first_examples=down[:8])
# The q/sigma assertion for every partial width at each nominal width <=512.
for v in range(1,513):
    for b in range(1,v+1):
        r=q(b)/sigma(b)
        assert r<=q(v)+2
        assert r*r<=1<<drop(v)
        count('all_partial_width_renewal_guards')
# Very large WIDTHS use logarithms/ratios only, never 2^(width).
for b in list(range(1,10001))+[2**j+d for j in range(16,129) for d in [-1,0,1]]:
    a,r,u,t=params(b)
    assert t<=b and F(1,1<<t)<=F(32*u,a)
    if t:assert 16*u*(1<<t)<=a
    assert (q(b)+2)**2<=1<<drop(b)
    if b>=16:assert q(b)+2<=2*b
    assert F(1,15*(b+1)+1)+F(1,2*(b+1)**2)<=F(1,2*(b+1))
    count('normalized_local_guards')
# Threshold proof certificates use only small exact rationals, not n=2^L.
gap=F(79,15625)
assert F(177,125)**2-2==gap
assert gap*16384>42 and gap>F(4,16384)
assert F(118,100)**2<F(177,125)
qgap=F(15,16)*F(731,500)**2-2
assert qgap==F(15415,4000000)
assert qgap*65536>42 and qgap>F(4,65536)
assert F(1,16)>F(1,100)
assert F(1,48)>F(1,1000)
assert F(177,250)**2>F(1,2)
assert 2*F(1,1024)+F(1,16384)+F(1,1048576)<F(1,256)
# True all-D maxima, plus explicitly labeled selected-D checks at larger n.
records=[]
for n in cfg['all_D_n']+cfg['selected_D_n']:
    for kind in ['critical-sqrt','critical-quarter','inherited-quarter']:
        B,vs=choose(n,kind)
        assert sum(vs)>=n
        assert all(sum(profile(t,kind))<n for t in range(1 if kind=='critical-sqrt' else 2,B,2 if kind=='inherited-quarter' else 1))
        allD=n in cfg['all_D_n']
        if allD:Ds=list(range(1,n+1))
        else:
            # Include all transitions between active levels and both adjacent D values.
            tails=[sum(vs[j:]) for j in range(len(vs))]
            Ds=sorted({1,2,n,n-1,*[min(n,max(1,t+d)) for t in tails for d in [-1,0,1,2]]})
        for D in Ds:
            ws=widths(vs,D);assert sum(ws)==D-1
            assert sum(0<b<v for b,v in zip(ws,vs))<=1
            e,v=budget(n,vs,D)
            # Square to avoid irrational half-integer powers in the telescope.
            bound=(8*B)**2*(1<<(B-base(B,kind)))
            assert e*e<=bound
            assert e*e<=(16*base(B,kind))**2*(1<<(B-base(B,kind)))
            assert e.numerator.bit_length()+e.denominator.bit_length()<64*(n+1)
            assert v.numerator.bit_length()+v.denominator.bit_length()<64*(n+1)
            count('all_or_selected_D_recurrences')
        c=caps(n,vs,Ds)
        assert c['q0']**2<=(6*B)**2*(1<<(B-base(B,kind)))
        assert c['k0']<=n
        assert c['Qcap'].bit_length()<64*(n+1) and c['Vcap'].bit_length()<64*(n+1)
        record=dict(n=n,kind=kind,B=B,U=base(B,kind),widths=vs,capacity=sum(vs),D_count=len(Ds),all_D=allD,
                    Qcap_bits=c['Qcap'].bit_length(),Vcap_bits=c['Vcap'].bit_length(),q0_bits=c['q0'].bit_length())
        if allD:
            record.update(Emax=exact_ratio(c['E']),Vmax=exact_ratio(c['V']),Qcap=str(c['Qcap']),Vcap=str(c['Vcap']))
        else:
            record['warning']='Selected-D maxima are not algorithm caps; only diagnostic word-length bounds.'
        records.append(record)
out=dict(status='PASS',scope=cfg['certificate_scope'],counts=counts,downward_capacity_jumps=jumps,
         recurrence_records=records,limits=lim,cpu_seconds=time.process_time()-start,
         hashes={s:sha256((P/s).read_bytes()).hexdigest() for s in ['profile.py','protocol.json','check_profiles.py']})
(P/'results/profiles.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['recurrence_records']},indent=2))
