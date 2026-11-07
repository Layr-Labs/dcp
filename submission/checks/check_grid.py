#!/usr/bin/env python3
"""Exact finite root-certificate comparisons; integer log bins are certified, not floats."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,resource,time
P=Path(__file__).resolve().parent
cfg=json.loads((P/'protocol.json').read_text());lim=cfg['limits']
resource.setrlimit(resource.RLIMIT_AS,(lim['address_space_bytes'],)*2)
resource.setrlimit(resource.RLIMIT_CPU,(lim['cpu_seconds'],)*2)
from profile import *
def binding(x):
    def h(i):return sha256(i.to_bytes((i.bit_length()+7)//8,'big')).hexdigest()
    return dict(numerator_bits=x.numerator.bit_length(),denominator_bits=x.denominator.bit_length(),
                numerator_sha256=h(x.numerator),denominator_sha256=h(x.denominator),floor_log2=floor_log_ratio(x))
rows=[];start=time.process_time()
for n in cfg['exact_profile_grid_n']:
    vals={}
    for kind in ['inherited-quarter','half-geometric-quarter','critical-quarter','critical-sqrt']:
        B,vs=choose(n,kind);e,v=budget(n,vs,n);vals[kind]=(e,v)
        row=dict(n=n,kind=kind,B=B,U=base(B,kind),levels=len(vs),capacity=sum(vs),
                 E_n=binding(e),V_n=binding(v),scope='D=n only; not Emax/Vmax or global caps')
        if kind!='inherited-quarter':
            er=e/vals['inherited-quarter'][0];vr=v/vals['inherited-quarter'][1]
            row.update(E_ratio_to_inherited=binding(er),V_ratio_to_inherited=binding(vr),
                       exact_E_comparison='less' if er<1 else 'equal' if er==1 else 'greater',
                       exact_V_comparison='less' if vr<1 else 'equal' if vr==1 else 'greater')
        rows.append(row)
        print(n,kind,B,row['E_n']['floor_log2'],row['V_n']['floor_log2'],flush=True)
out=dict(status='PASS',rows=rows,limits=lim,cpu_seconds=time.process_time()-start,
         meaning='Each floor_log2 k means exactly 2^k <= rational < 2^(k+1). Ratios and orderings use exact rational arithmetic. No fitted exponent or asymptotic inference.',
         hashes={f:sha256((P/f).read_bytes()).hexdigest() for f in ['check_grid.py','profile.py','protocol.json']})
(P/'results/grid.json').write_text(json.dumps(out,indent=2)+'\n')
