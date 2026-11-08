"""Exact boosted binary/quartic prefix capacities; finite diagnostic only."""
from fractions import Fraction as F
import json
P=8192
def G(J):
 z,t=divmod(J,P);return P*z*(z-1)//2+z*t

def ceildiv(a,b):return (a+b-1)//b

def sums(M,A,H,dl,k):
 if M<=A:return M*(dl-k)+M*(M-1)//2+dl-1
 J=M-A;sb=A*(dl-k-1)+A*(A-1)//2
 return sb+J*J+2*H*J+H-J*k-1-G(J)

def capacities(M,A,H,dl,k):
 out=[]
 for i in range(M):
  root=i==M-1
  if i<A:out.append(2*(dl+i)-1-k if root else dl+i-1-k)
  else:
   j=i-A;out.append(3*H+2*j-2*(j//P)-k if root else 2*H+1+2*j-2*(j//P)+(j+1)//P-k)
 return out

def prefix(B,Mmax,A,H,dl,k):
 lo,hi=1,Mmax
 while lo<hi:
  mid=(lo+hi)//2
  if sums(mid,A,H,dl,k)>=B:hi=mid
  else:lo=mid+1
 return lo
small=0
for H in [32,48,64]:
 for dl in [H//3,H//2,2*H//3]:
  A=H-dl
  for L in [1,2,4,8]:
   mm=A+L;k=(mm-1).bit_length()+3
   if dl<k+1:continue
   sb=A*(dl-k-1)+A*(A-1)//2
   assert sb>=2*H+2*L+1-k
   last=0
   for M in range(1,mm+1):
    cs=capacities(M,A,H,dl,k)
    assert min(cs)>=0 and sum(cs)==sums(M,A,H,dl,k)>last
    last=sum(cs)
   for B in range(1,last+1):
    M=prefix(B,mm,A,H,dl,k);cs=capacities(M,A,H,dl,k);remain=B
    alloc=[0]*M
    for i in range(M-1,-1,-1):alloc[i]=min(remain,cs[i]);remain-=alloc[i]
    assert remain==0
    assert all(alloc[i]==cs[i] for i in range(A,M))
    small+=1
q,d,h=map(F,['24999/50000', '17931/10000', '199989/100000']);a=h-d;ell=(q-a)/2
C=a*d+a*a/2+2*h*ell+ell*ell
assert C==F(40000561767,40000000000)>F(100001,100000)
assert q+d==F(57327,25000)
rs=set(range(2**24,2**24+5001))
for e in range(24,257):
 for off in [-1,0,1,17,9999]:
  if 2**e+off>=2**24:rs.add(2**e+off)
for r in rs:
 H=199989*r//100000;dl=ceildiv(17931*r,10000);target=ceildiv(24999*r,50000)
 A=H-dl;L=ceildiv(target-A,2);mm=A+L;height=A+2*L;k=(mm-1).bit_length()+3
 assert 8*A>=r and dl>=k+1 and L>=1
 assert target<=height<=target+1
 assert mm<=r and k<=r.bit_length()+5
 assert H>=k+2 and H+1+2*(L-1)<=2*H
 assert H-1-2*(L-1)-2*((L-1)//P)>=k and 2*(H-L//P)>r
 sb=A*(dl-k-1)+A*(A-1)//2
 assert sb>=2*H+2*L+1-k
 assert sums(mm,A,H,dl,k)>=r*r
 assert height<=q*r+2 and height+dl<=(q+d)*r+3
 assert H<=h*r
 assert F(7,10)*r>4*r.bit_length()+35
 assert 4*(mm+1)*H+2**13*(2*r+(r*r-1).bit_length()+30)<=8*((r-1)**2+1)
 Bs={1,r*r,(r*r)//2,sums(A,A,H,dl,k)}
 for j in [1,max(1,L//2),L]:
  s=sums(A+j,A,H,dl,k)
  Bs.update([s-1,s,s+1])
 for B in Bs:
  if not 1<=B<=r*r:continue
  M=prefix(B,mm,A,H,dl,k)
  assert sums(M,A,H,dl,k)>=B and (M==1 or sums(M-1,A,H,dl,k)<B)
  if M>A:
   J=M-A;allfour=J*J+2*H*J+H-J*k-1-G(J)
   assert B>=allfour
print(json.dumps({'small_greedy_cases':small,'main_schedule_cases':len(rs),'capacity_coefficient':str(C),'time_coefficient':str(q+d),'all_checks_passed':True}))


cap_cases=0
for r in sorted(rs):
 H=199989*r//100000;dl=ceildiv(17931*r,10000);target=ceildiv(24999*r,50000)
 A=H-dl;L=ceildiv(target-A,2);height=A+2*L
 for n in {r*r,(r-1)*(r-1)+1}:
  if n<2**48:continue
  u=(n-1).bit_length();Kc=8192*(2*r+u+30);Kp=8192*(u+100)
  cc=32*dl*(Kc+u+16);cf=32*dl*(Kp+u+16)
  Y=height+(cc-1).bit_length()
  assert Kp<=Kc<=3*8192*r
  assert Y<=2*r<=n and Y+6<=n and Kc//8192>=Y+u+30
  assert cc<=2**23*n and cf<=2**23*r*u
  qcoef=(Y+6)*cc+2*n*cf+Kp
  assert qcoef<=2**30*n*r*u
  assert height<=F(24999,50000)*r+2
  assert height+dl<=F(57327,25000)*r+3
  assert H<=F(199989,100000)*r
  cap_cases+=1
for M in range(1,129):
 pp=F(1,2*M)
 assert (1-pp)**(-M)<3
 partial=sum(pp**j for j in range(16))
 assert partial<1/(1-pp)
failure=3*(F(1,2**16)+F(1,2**12))+F(1,2**20)+F(1,2**30)+F(1,2**40)+F(1,2**10)
assert failure<F(1,2**8)
print(json.dumps({'variable_root_cap_cases':cap_cases,'retry_geometric_cases':128,'failure_sum':str(failure),'all_checks_passed':True}))


from decimal import Decimal as DD,localcontext
mixed_moments=0
with localcontext() as ctx:
 ctx.prec=180
 for LL in range(1,65):
  kk=max(6,(LL-1).bit_length()+3);pp=DD(4)/DD(2**kk)
  assert pp<=DD(1)/(2*LL) and pp<=DD(1)/10
  for mode in range(4):
   fs=[2 if mode==0 else 4 if mode==1 else (2 if (i+mode)%3==0 else 4) for i in range(LL)]
   prod=1
   for ff in fs:prod*=ff
   for ss in [DD(1)/32,DD(1)/16,DD(1)/8]:
    arg=ss/DD(prod);yy=arg
    for ii,ff in enumerate(fs,1):
     aa=ff*yy;arg*=ff
     assert aa<DD(1)/2
     yy=aa+(1-pp).ln()-(1-pp*aa.exp()).ln()
     assert yy<=(1+2*pp)**ii*arg
    assert yy<3*ss
    mixed_moments+=1
print(json.dumps({'mixed_arity_moment_cases':mixed_moments,'all_checks_passed':True}))


assert C-ell*ell/(2*P)>F(100001,100000)
closed=0;geom=0
for pp in sorted(set([1,2,3,7,1024,P])):
 for JJ in list(range(100))+[pp-1,pp,pp+1,2*pp-1,2*pp,2*pp+1,9*pp+3]:
  zz,tt=divmod(JJ,pp);gg=pp*zz*(zz-1)//2+zz*tt
  assert gg==sum(jj//pp for jj in range(JJ))
  assert 2*pp*gg<=JJ*(JJ-1)
  closed+=1
 for HH in [32,64,2048]:
  for dd in [1,HH//2,HH-1]:
   for LL in [1,min(HH,pp),min(HH,2*pp+7)]:
    widths=list(range(dd,HH))+[HH-jj//pp for jj in range(LL)]
    assert min(widths)>0 and sum(2**ww for ww in widths)<=(2*pp+1)*2**HH
    for jj in range(LL):
     lam=HH-jj//pp;aux=HH+1+2*jj;lp=HH-(jj+1)//pp
     assert 2*lam+aux-1==3*HH+2*jj-2*(jj//pp)
     assert 2*lam+aux-lp==2*HH+1+2*jj-2*(jj//pp)+(jj+1)//pp
    geom+=1
print(json.dumps({'plateau_floor_sum_cases':closed,'plateau_geometric_and_capacity_shapes':geom,'effective_C':str(C-ell*ell/(2*P)),'all_checks_passed':True}))
