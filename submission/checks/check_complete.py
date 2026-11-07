#!/usr/bin/env python3
"""Compare literal complete F certificates using only enumerated all-D maxima."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,resource
resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(60,)*2)
from profile import q,ceil_log,floor_log_ratio,hbound,params
P=Path(__file__).resolve().parent
r=json.loads((P/'results/profiles.json').read_text())
rows=[];by={}
for x in r['recurrence_records']:
    if not x['all_D']:continue
    n=x['n'];q0=1
    for b in x['widths']:q0*=q(b)
    fc=ceil_log(n+2)**2*(int(x['Vcap'])+n**3*int(x['Qcap'])+n**4*q0+n**6)
    by[n,x['kind']]=fc
for (n,kind),fc in sorted(by.items()):
    old=by[n,'inherited-quarter'];ratio=F(fc,old)
    rows.append(dict(n=n,kind=kind,F_floor_log2=fc.bit_length()-1,
                     F_ratio_floor_log2=floor_log_ratio(ratio),exact_comparison='less' if ratio<1 else 'equal' if ratio==1 else 'greater',
                     F=str(fc),ratio={'numerator':str(ratio.numerator),'denominator':str(ratio.denominator)}))
# Actual h has downward discontinuities, so monotone all-D work is not assumed.
down=[]
prev=hbound(1)
for b in range(2,10001):
    cur=hbound(b)
    if cur<prev:down.append(dict(b=b,t_b=params(b)[3],previous_t=params(b-1)[3]))
    prev=cur
out=dict(status='PASS',scope='Complete certificate F from Section 9, using true enumerated all-D caps. No realized runtime ratios.',
         rows=rows,local_h_downward_jumps=dict(count=len(down),first_examples=down[:8],pivot_changes=[d for d in down if d['t_b']!=d['previous_t']]),limits=dict(address_space_bytes=512<<20,cpu_seconds=60),
         hashes={s:sha256((P/s).read_bytes()).hexdigest() for s in ['check_complete.py','profile.py','results/profiles.json']})
(P/'results/complete.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],comparisons=[{k:r[k] for k in ['n','kind','F_floor_log2','F_ratio_floor_log2','exact_comparison']} for r in rows],local_h_downward_jumps=out['local_h_downward_jumps']),indent=2))
