#!/usr/bin/env python3
"""Finite exact check of the new no-pivot lower bound used in the comparison."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import sys,json,resource
resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(60,)*2)
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'replay'))
from score_schedules import schedule
count=0
for k in range(1,9):
 A=1<<k
 for z in range(1,A):
  for r in [12,20,64]:
   p,h,_=schedule(A,z+1,2,r)
   assert p>=F(3,4)
   assert h*h*z>=F(A,64)
   count+=1
first=None
for b in range(1,1001):
 q=b+b.bit_length()+4;u=(q+1).bit_length();t=max(0,(q//(16*u)).bit_length()-1)
 if t and first is None:first=b
assert first==275
out=dict(status='PASS',fixed_fiber_lower_bounds=count,first_b_with_nonzero_prescribed_pivot=first,limits=dict(address_space_bytes=512<<20,cpu_seconds=60),script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),scope='Finite checks of the analytical lower bound, not an enumeration of exponentially large arities or a measured compiled speedup.')
(HERE/'results'/'lower-bound.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
