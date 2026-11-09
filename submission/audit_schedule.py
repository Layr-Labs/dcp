"""Exact actual geometry/capacity diagnostic; uniform proof is in proof.md."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
from math import isqrt
import json
q=F(141421,100000);d0=F(100759,28284200000);tc=q+d0
ceil=lambda x:-(-x.numerator//x.denominator)
assert q*d0+q*q/2==1 and 2*q>F(64,25) and d0*2**24>16
ns={2**e for e in [128,129,192,256,512,1024]}
for e in [128,129,192,256]:
 for off in [-1,1,17]:
  if 2**e+off>=2**128:ns.add(2**e+off)
for e in [64,96,128,256]:
 for off in [-1,0,1]:ns.add(((1<<e)+1)**2+off)
cases=0;cycles_total=0
with localcontext()as ctx:
 ctx.prec=800
 for n in sorted(ns):
  r=isqrt(n-1)+1;m=ceil(q*r);u=(n-1).bit_length();C=isqrt(u-1)+1+64
  base=ceil(d0*r)+C;dl=base+2;dw=isqrt(2*C*m)-1;Hlin=base+m-1;H=Hlin-dw;LL=m//8
  assert 64<=C<=u and base>=65536*u+64 and base>=4*dw+4*u+8
  assert dw>=C and dw<m//4 and 2*(dw+1)<LL and (m+1)*H<=4*n
  lam=lambda i:min(base+i+min(2,2*(m-1-i)//LL),H)
  out=[];aa=0
  while aa<m:
   W=lam(aa);vv=m-aa if m-aa<=W//4+128 else W//4;sig=(vv-1).bit_length()+2
   assert vv>=128 and W>=2*vv+2*sig+64*u
   out.append((aa,vv,W));aa+=vv
  assert aa==m and len(out)<=128;cycles_total+=len(out)
  loss=dw*(dw+1)//2;liftloss=2*LL-LL//2;JJ=len(out)-1
  cap=(m+1)*base+m*(m-1)//2-1+2*m-liftloss-4*JJ-loss
  assert loss<=C*m and cap>=n+m+63
  b0=(base-dw)//16-1024*u;g=b0-6;gw=(dl-1).bit_length();noise=(n**5-1).bit_length()
  assert b0*32>=base and g>=d0*r/64 and m+gw+b0<=H
  kc=8192*(m+10*u+100);cc=2**158*dl*(kc+u+16);cf=2**161*dl;YY=m+(cc-1).bit_length()
  Ns=ceil(F(YY+8*u+20,g))+1;lb=(n+b0-1)//b0
  assert Ns<2**26 and cf<=cc and kc*dl<=2**16*n
  assert Ns*cc+4*lb*cf<=2**210*n
  for bb in {1,2,b0//2,b0-1,b0}:
   dout=bb+noise
   assert dout<=H and cap-(dout-1)>=n-bb and 2*bb<=H-2048*u
  nn=D(n);ll=nn.ln()/D(2).ln();FF=D(tc.numerator)/D(tc.denominator)*nn.sqrt();zz=nn.sqrt().sqrt()*ll.sqrt().sqrt()
  assert D(C)<=ll.sqrt()+66
  assert D(m+dl)<=FF+ll.sqrt()+72 and D(H)<=FF+ll.sqrt()+71-D(8)*zz/5
  assert D(dw)>D(8)*zz/5-2;cases+=1
meta=json.loads(Path(__file__).with_name('submission.json').read_text())
assert meta['claims'][0]['structured']['bound']['nPower']=='5/2'
assert meta['claims'][0]['structured']['bound']['exponent'][1]==dict(coefficient='1',nPower='0',logPower='1/2')
assert meta['claims'][1]['structured']['bound']['exponent'][1]==dict(coefficient='-3/2',nPower='1/4',logPower='1/4')
assert meta['claims'][4]['structured']['expression']=='0'
print(json.dumps(dict(actual_sqrtlog_allowance_cases=cases,actual_cycle_instances=cycles_total,all_checks_passed=True,uniform_proof_and_fresh_review_required=True)))
