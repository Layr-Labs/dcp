"""Finite exact three-level/rejected-difference recycling diagnostics."""
from fractions import Fraction as F
from math import comb,factorial
from itertools import product
import cmath,json
from pathlib import Path

def c(m,d):return F(2*m**3+m,3)-m*d*d+F(d**3-d,2)
def e_kernel(m,d):
    center=4*(m-1)+d
    return sum((-1)**j*comb(8,j)*(comb(center-j*m+7,7) if center-j*m>=0 else 0) for j in range(9))
def e_zero(m):return F(151*m**7+70*m**5+49*m**3+45*m,315)
def a_kernel(h,d):return F(2*h**3+h,3)-h*h*d+F(h*d*d+h*d,2)+F(d**3-d,6)

def qstate(f,n,s):return [1/2**.5,cmath.exp(2j*cmath.pi*f*s/n)/2**.5]
def difference(v,w,negative):
    out=[(2**.5)*v[0]*w[1],(2**.5)*v[1]*w[0]]
    if negative:out.reverse()
    return out

def capacity(ell):return ell+sum(259*j//100 for j in range(ell))
def parameters(n,m):
    lo,hi=1,m-1
    while lo<hi:
        mid=(lo+hi)//2
        if capacity(mid)>=m-1:hi=mid
        else:lo=mid+1
    ell=lo;lam=(1024*(n+1)-1).bit_length();final=(1<<60)*lam
    lengths=[(final*97**t+16**t-1)//16**t for t in range(ell,-1,-1)]
    remaining=m-1-ell;widths=[]
    for i in range(ell):
        b=min(259*(ell-i-1)//100,remaining);widths.append(b);remaining-=b
    assert remaining==0
    return ell,final,lengths,widths

def main():
    e_checks=r_checks=0
    for m in range(4,65,2):
        tri=[min(s+1,2*m-1-s) for s in range(2*m-1)]
        t4=[0]*(4*m-3)
        for i,x in enumerate(tri):
            for j,y in enumerate(tri):t4[i+j]+=x*y
        assert sum(t4)==m**4
        e0=sum(x*x for x in t4)
        assert e0==e_zero(m)
        assert e0>=F(151*m**7,315)>F(13*m**7,32)
        for d in range(m//2+1):
            actual=sum(t4[i]*t4[i+d] for i in range(len(t4)-d))
            assert actual==e_kernel(m,d)
            assert 2*actual>=e0
            assert e0-actual<=m**4*(c(m,0)-c(m,d))
            e_checks+=1
        assert F(e0,4*m**7)>=F(151,1260)
        h=m//2
        w=[0]+[h-d for d in range(1,h)]+[2*h-d for d in range(h,2*h)]
        assert len(w)==2*h and sum(w)==h*h
        kept=[]
        for d in range(h):
            count=sum(w[i]*w[i+d] for i in range(len(w)-d))
            assert count==a_kernel(h,d)
            assert count>=F(h**3,4)
            abs_count=count if d==0 else 2*count
            probability=F(h**3,2*count if d==0 else 4*count)
            assert 0<=probability<=1
            kept.append(F(abs_count,h**4)*F(1,2)*probability)
            r_checks+=1
        assert all(p==F(1,4*h) for p in kept) and sum(kept)==F(1,4)
    assert F(3)<F(49,16) #sqrt3<7/4, so the polynomial minimum exceeds1/4.
    density_checks=0;maximum=0.0
    m=4
    for n in (5,13):
        for secret in range(n):
            for x1,x2,x3,x4 in product(range(m),repeat=4):
                d1,d2=abs(x1-x2),abs(x3-x4)
                if not d1 or not d2:continue #the primaryR population excludes zero.
                v=difference(qstate(3+2*x1,n,secret),qstate(3+2*x2,n,secret),x1<x2)
                w=difference(qstate(11+2*x3,n,secret),qstate(11+2*x4,n,secret),x3<x4)
                got=difference(v,w,d1<d2);expected=qstate(2*abs(d1-d2),n,secret)
                for i,j in product((0,1),repeat=2):
                    error=abs(got[i]*got[j].conjugate()-expected[i]*expected[j].conjugate())
                    maximum=max(maximum,error);assert error<1e-12
                density_checks+=1
    coin_cases=0
    for p1 in range(1,33):
        for z1 in range(p1+1):
            for rejected in range(p1-z1+1):
                p2=z1//2;ur=rejected//2;d1=p1-z1-rejected
                for z2 in range(p2+1):
                    p3=z2//2
                    coins=(p1-z1)+(p2-z2)+p3+ur
                    assert 2*coins<=3*p1
                    max_outputs=d1+(p2-z2)+p3+ur
                    assert max_outputs<=p1
                    coin_cases+=1
    eps=F(1,1<<20);gamma=F(151,1260);theta=F(6661,40320);q=F(97,16)
    assert theta==F(7,48)+gamma/32+F(1,64)
    assert q*theta-1==F(997,645120)
    assert q*(theta-eps)-1>F(1,1024)
    assert F(18081,40320)<F(1,2)
    parameter_cases=stages=0
    for n in list(range(17,2049))+[4096,16384,100000,1000000]:
        for m in (n-1,n):
            ell,final,lengths,widths=parameters(n,m)
            assert capacity(ell)>=m-1>capacity(ell-1)
            assert 1000000*max(0,ell-2)**2<=772641*n
            assert sum(widths)==m-1-ell and sum(lengths[:-1])<2*lengths[0]
            width=m
            for i,b in enumerate(widths):
                qp=q**(ell-i-1);k=1<<b;budget=final*qp
                assert k<=qp
                p1=F(lengths[i]-k,2)
                z1=(1-eps)*p1/2;v=(1-eps)*p1/4
                p2=(z1-k)/2;z2=(1-eps)*p2/2;p3=(z2-k)/2;ur=(v-k)/2
                y=(1-eps)*(p1/4+p2/6+gamma*p3+ur/4)
                assert p1>=budget and p2>=budget/16 and p3>=budget/256 and ur>=budget/32
                assert y>=lengths[i+1]
                exponents=[eps*eps*p1/8,eps*eps*p1/4,eps*eps*p1/8,
                           eps*eps*p2/12,eps*eps*p2/4,eps*eps*gamma*p3/2,eps*eps*ur/8]
                assert all(z>=budget/(1<<56) for z in exponents)
                assert width-b>=2
                width-=b+1;stages+=1
            assert width==1;parameter_cases+=1
    partial=F(842,1215)
    assert partial>F(693,1000) and partial+F(1,6804)<F(347,500)
    x=F(41,100)*F(693,1000);assert 1+x+x*x/2>F(128,97)
    x=F(399,1000)*F(347,500);assert 1+x+x*x/(2*(1-x/3))<F(128,97)
    assert F(879,1000)**2*F(259,100)>2
    assert F(879,1000)*F(2601,1000)==F(2286279,1000000)
    out=dict(scope='Finite exact kernel/coin/quota and numerical density diagnostics; no asymptotic or device certification.',
             order8_correlation_checks=e_checks,rejected_difference_kernel_checks=r_checks,
             global_rejected_phase_density_checks=density_checks,maximum_numeric_density_error=maximum,
             branchwise_coin_and_output_cases=coin_cases,parameter_cases=parameter_cases,
             exact_seven_event_stage_checks=stages,exact_exponential_coefficient='2286279/1000000')
    Path(__file__).with_name('recycle_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
