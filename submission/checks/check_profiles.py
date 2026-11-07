#!/usr/bin/env python3
"""Literal exact all-D rational maxima; each diagnostic has a fixed CPU cap."""
import resource
resource.setrlimit(resource.RLIMIT_AS,(768<<20,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(50,)*2)
from pathlib import Path
from fractions import Fraction as F
from math import prod
from hashlib import sha256
import json,time,subprocess
from common import choose,widths,all_d,cert,flog,clog,local,arity,profile

P=Path(__file__).resolve().parents[1]
start=time.process_time()
rows=[]
for n in (256,512,1024,2048,4096,8192):
    results=[]
    for old in (True,False):
        B,seq=choose(n,old)
        assert sum(seq)>=n
        # Sequential choice examined every smaller trial, rather than assuming
        # monotonic capacity. Check the immediate previous trial as a guard.
        assert B==1 or sum(profile(B-1,old))<n
        r=all_d(n,seq,old)
        # Independently expand the inhomogeneous recurrence as a sum over
        # ancestor products, including the separate one- or TWO-copy base.
        for D in sorted({1,n//2,n-1,n}):
            terms=[local(n,b,old) for b in widths(D,seq) if b]
            e_expanded=F(1 if old else 2)*prod(factor for factor,add in terms)
            v_expanded=sum((add*prod(f for f,a in terms[i+1:])
                            for i,(factor,add) in enumerate(terms)),F(0))
            assert cert(n,D,seq,old)==(e_expanded,v_expanded)
        for D in range(1,n+1):
            bs=widths(D,seq)
            assert sum(bs)==D-1
            partial=[i for i,(b,v) in enumerate(zip(bs,seq)) if 0<b<v]
            assert len(partial)<=1
            if partial:assert all(bs[j]==seq[j] for j in range(partial[0]+1,len(seq)))
            e,v=cert(n,D,seq,old)
            assert e<=r['E'] and v<=r['V']
        if not old:
            assert cert(n,1,seq)==(F(2),F(0))
            assert r['q0']==2*prod(arity(b) for b in seq)
            # Every literal cap and rational word lies within the specified word.
            assert max(x.bit_length() for key in ('Qcap','Vcap','q0','K') for x in (r[key],))<1024*(n+1)
            for key in ('E','V'):
                assert max(r[key].numerator.bit_length(),r[key].denominator.bit_length())<1024*(n+1)
        r['B']=B;r['levels']=len(seq)
        results.append(r)
    old,new=results
    record={'n':n,'scope':'all D=1,...,n, exact rational maxima',
            'PPC_width':old['B'],'F4_width':new['B'],
            'PPC_levels':old['levels'],'F4_levels':new['levels'],
            'F4_E_argmax':new['E_argmax'],'F4_V_argmax':new['V_argmax'],
            'F4_Qcap_bits':new['Qcap'].bit_length(),'F4_Vcap_bits':new['Vcap'].bit_length(),
            'Qcap_ratio_floor_log2':flog(F(new['Qcap'],old['Qcap'])),
            'complete_certificate_ratio_floor_log2':flog(F(new['F'],old['F']))}
    # Exact values are retained, not rounded floating point estimates.
    record['F4_exact']={k:str(v) for k,v in new.items() if k in ('E','V','q0','K','Qcap','Vcap','F')}
    rows.append(record)

out={'status':'PASS','timestamp':subprocess.check_output(['date','+%Y-%m-%d %H:%M:%S %Z (%z)'],text=True).strip(),
     'rows':rows,'cpu_seconds_used':time.process_time()-start,
     'limits':{'cpu_seconds':50,'address_space_bytes':768<<20},
     'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'common_sha256':sha256((P/'checks/common.py').read_bytes()).hexdigest(),
     'scope':'Exact finite all-D caps, not an asymptotic fit, operation simulation or provider verdict.'}
(P/'profile-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'rows':[{k:v for k,v in r.items() if k!='F4_exact'} for r in rows]},indent=2))
