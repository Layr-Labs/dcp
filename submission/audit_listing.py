"""Compare bounded implicit pair-fiber listing with brute-force tuples.
Small finite classical diagnostic; not a quantum simulation or proof premise.
"""
from heapq import heappush,heappop
from itertools import product
from random import Random
import json
rng=Random(748193)

def stream_pairs(fiber,reverse=False):
 # Independently group by first coordinate and sort its restricted second run.
 rows={}
 for key,a,b in fiber:rows.setdefault(a,[]).append((key,b))
 heap=[]
 for a,values in rows.items():
  values.sort(reverse=reverse)
  key,b=values[0];heappush(heap,((-key if reverse else key),a,0,b))
 while heap:
  signed,a,j,b=heappop(heap);yield (-signed if reverse else signed),a,b
  j+=1
  if j<len(rows[a]):
   key,b=rows[a][j];heappush(heap,((-key if reverse else key),a,j,b))

def listed(X,Y,rp,target,Cp):
 out=[]
 for g in range(4):
  tg=target+g*2**rp
  sx=iter(stream_pairs(X));sy=iter(stream_pairs(Y,True))
  hx=next(sx,None);hy=next(sy,None)
  while hx is not None and hy is not None:
   z=hx[0]+hy[0]
   if z<tg:hx=next(sx,None);continue
   if z>tg:hy=next(sy,None);continue
   ky=hy[0];buf=[]
   while hy is not None and hy[0]==ky:
    if len(buf)<Cp:buf.append(hy)
    hy=next(sy,None)
   kx=hx[0]
   while hx is not None and hx[0]==kx:
    for eta in buf:
     out.append((hx[1],hx[2],eta[1],eta[2]))
     if len(out)==Cp:return out
    hx=next(sx,None)
 return out

cases=0;cut=0;overflows=0;small=0
for L,r,rp in [(4,0,2),(8,0,3),(16,0,4),(4,1,2),(8,2,3),(16,3,4)]:
 for trial in range(40):
  # The planted low-label case exercises ties and overflowing fibers.
  labs=[[j%(2**r) for j in range(L)] for _ in range(4)] if trial==0 else [[rng.randrange(2**(r+rp)) for _ in range(L)] for _ in range(4)]
  rho=[[v%2**r for v in row] for row in labs];sg=[[v//2**r for v in row] for row in labs]
  for _ in range(8):
   v,v2,tg=[rng.randrange(2**z) for z in [r,r,rp]]
   cAB,cCD=rng.randrange(2),rng.randrange(2)
   X=[(sg[0][a]+sg[1][b]+(rho[0][a]+rho[1][b]+cAB)//2**r,a,b) for a,b in product(range(L),repeat=2) if (rho[0][a]+rho[1][b]+cAB)%2**r==v]
   Y=[(sg[2][a]+sg[3][b]+(rho[2][a]+rho[3][b]+cCD)//2**r,a,b) for a,b in product(range(L),repeat=2) if (rho[2][a]+rho[3][b]+cCD)%2**r==v2]
   for Cp in [1,3,17,65]:
    got=listed(X,Y,rp,tg,Cp)
    expected={(x[1],x[2],y[1],y[2]) for x,y in product(X,Y) if (x[0]+y[0])%2**rp==tg}
    assert len(set(got))==len(got)==min(Cp,len(expected))
    assert set(got)<=expected
    if len(expected)<=Cp:assert set(got)==expected;small+=1
    else:overflows+=1
    cases+=1
  # An all-zero pair fiber exceeds the deterministic first-stage cap.
  mX=L*L//2**r
  zero_pair_fiber=[(a,b) for a,b in product(range(L),repeat=2)]
  assert (len(zero_pair_fiber)>2*mX if r>1 else len(zero_pair_fiber)<=2*mX)
  if r>1:cut+=1
window_cases=0;zero_windows=0
for _ in range(5000):
 p0=rng.randrange(1,9);r0=rng.randrange(0,5);r1=rng.randrange(1,6);b=r0+r1
 constants=[rng.randrange(2**p0) for _ in range(4)]
 high=[rng.randrange(2**(b+3)) for _ in range(4)]
 labels=[c+2**p0*h for c,h in zip(constants,high)]
 ca=(constants[0]+constants[1])//2**p0;cc=(constants[2]+constants[3])//2**p0
 cl=((constants[0]+constants[1])%2**p0+(constants[2]+constants[3])%2**p0)//2**p0
 low=[v%2**r0 for v in high];sg=[(v//2**r0)%2**r1 for v in high]
 vx=(low[0]+low[1]+ca)%2**r0;vy=(low[2]+low[3]+cc)%2**r0
 gx=(low[0]+low[1]+ca)//2**r0;gy=(low[2]+low[3]+cc)//2**r0
 kx=sg[0]+sg[1]+gx;ky=sg[2]+sg[3]+gy
 val=sum(labels)//2**p0
 assert val==(vx+vy+cl)+2**r0*(kx+ky)+2**b*sum(v//2**b for v in high)
 assert val%2**r0==(vx+vy+cl)%2**r0
 assert (val//2**r0)%2**r1==(kx+ky+(vx+vy+cl)//2**r0)%2**r1
 window_cases+=1;zero_windows+=(r0==0)
print(json.dumps({'window_identity_cases':window_cases,'zero_window_identity_cases':zero_windows,'listing_cases':cases,'small_complete_fibers':small,'overflow_cases':overflows,'planted_pair_cut_checks':cut,'all_checks_passed':True}))
