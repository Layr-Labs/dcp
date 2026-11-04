"""Finite exact four-level/rejected-difference recycling diagnostics."""
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

def b_kernel(m,d):
    center=8*(m-1)+d
    return sum((-1)**j*comb(16,j)*(comb(center-j*m+15,15) if center-j*m>=0 else 0) for j in range(17))
def b_zero(m):
    return F(m*(2330931341*m**14+1122261140*m**12+810231422*m**10+649783420*m**8+547079533*m**6+474040840*m**4+422422704*m**2+454053600),6810804000)
V_SUCCESS=F(267949,1000000)

def qstate(f,n,s):return [1/2**.5,cmath.exp(2j*cmath.pi*f*s/n)/2**.5]
def difference(v,w,negative):
    out=[(2**.5)*v[0]*w[1],(2**.5)*v[1]*w[0]]
    if negative:out.reverse()
    return out

def capacity(ell):return ell+sum(51651*j//20000 for j in range(ell))
def parameters(n,m):
    lo,hi=1,m-1
    while lo<hi:
        mid=(lo+hi)//2
        if capacity(mid)>=m-1:hi=mid
        else:lo=mid+1
    ell=lo;lam=(1024*(n+1)-1).bit_length();final=(1<<68)*lam
    lengths=[(final*599**t+100**t-1)//100**t for t in range(ell,-1,-1)]
    remaining=m-1-ell;widths=[]
    for i in range(ell):
        b=min(51651*(ell-i-1)//20000,remaining);widths.append(b);remaining-=b
    assert remaining==0
    return ell,final,lengths,widths

def main():
    e_checks=r_checks=b_checks=0
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
        t8=[0]*(8*m-7)
        for i,x in enumerate(t4):
            for j,y in enumerate(t4):t8[i+j]+=x*y
        assert sum(t8)==m**8
        b0=sum(x*x for x in t8)
        assert b0==b_zero(m)>F(m**15,3)
        assert e_kernel(m,0)-e_kernel(m,1)==F(m**5+m**3+m,3)
        for distance in range(m//2+1):
            actual=sum(t8[i]*t8[i+distance] for i in range(len(t8)-distance))
            assert actual==b_kernel(m,distance)
            assert b0-actual<=distance**2*m**8*(e_kernel(m,0)-e_kernel(m,1))
            assert 2*actual>=b0
            probability=F(1) if distance==0 else F(b0,2*actual)
            weight=F(actual if distance==0 else 2*actual,2*m**16)*probability
            assert weight==F(b0,2*m**16)
            b_checks+=1
        assert F(b0,4*m**15)>=F(2330931341,27243216000)
        h=m//2
        w=[0]+[h-d for d in range(1,h)]+[2*h-d for d in range(h,2*h)]
        assert len(w)==2*h and sum(w)==h*h
        kept=[]
        for d in range(h):
            count=sum(w[i]*w[i+d] for i in range(len(w)-d))
            assert count==a_kernel(h,d)
            assert count>=V_SUCCESS*h**3
            abs_count=count if d==0 else 2*count
            probability=V_SUCCESS*F(2*h**3,count) if d==0 else V_SUCCESS*F(h**3,count)
            assert 0<=probability<=1
            kept.append(F(abs_count,h**4)*F(1,2)*probability)
            r_checks+=1
        assert all(p==V_SUCCESS/h for p in kept) and sum(kept)==V_SUCCESS
    assert F(1732051,1000000)**2>3 #exact sharp rational minimum certificate.
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
    for p1 in range(1,25):
        for z1 in range(p1+1):
            for rejected in range(p1-z1+1):
                p2=z1//2;ur=rejected//2;d1=p1-z1-rejected
                for z2 in range(p2+1):
                    p3=z2//2
                    for z3 in range(p3+1):
                        p4=z3//2
                        coins=(p1-z1)+(p2-z2)+(p3-z3)+p4+ur
                        assert 2*coins<=3*p1
                        max_outputs=d1+(p2-z2)+(p3-z3)+p4+ur
                        assert max_outputs<=p1
                        coin_cases+=1
    eps=F(1,1<<20);gamma=F(151,1260);delta=F(2330931341,27243216000)
    v=V_SUCCESS;q=F(599,100);z=1-eps
    theta=F(1,8)+F(1,48)+gamma/32+delta/128+v/16
    a=z/4+z*z/24+gamma*z**3/16+delta*z**4/64+v*z*z/8
    b=z/12+gamma*z*z/8+gamma*z/2+delta*z**3/32+delta*z*z/8+delta*z/2+v*z/2
    assert theta==F(72791093701609,435891456000000)
    assert a/2>theta-eps and a/2+b<1
    assert q*(theta-eps)-1>F(1,4096)
    parameter_cases=stages=0
    for n in list(range(17,2049))+[4096,16384,100000,1000000]:
        for m in (n-1,n):
            ell,final,lengths,widths=parameters(n,m)
            assert capacity(ell)>=m-1>capacity(ell-1)
            assert 10**12*max(0,ell-2)**2<=880017**2*n
            assert sum(widths)==m-1-ell and sum(lengths[:-1])<2*lengths[0]
            width=m
            for i,b in enumerate(widths):
                qp=q**(ell-i-1);k=1<<b;budget=final*qp
                assert k<=qp
                p1=F(lengths[i]-k,2)
                z1=(1-eps)*p1/2;primary_v=(1-eps)*p1/4
                p2=(z1-k)/2;z2=(1-eps)*p2/2;p3=(z2-k)/2
                z3=(1-eps)*p3/2;p4=(z3-k)/2;ur=(primary_v-k)/2
                y=(1-eps)*(p1/4+p2/6+gamma*p3+delta*p4+V_SUCCESS*ur)
                assert p1>=budget and p2>=budget/16 and p3>=budget/256 and p4>=budget/4096 and ur>=budget/32
                assert y>=lengths[i+1]
                exponents=[eps*eps*p1/8,eps*eps*p1/4,eps*eps*p1/8,
                           eps*eps*p2/12,eps*eps*p2/4,eps*eps*gamma*p3/2,eps*eps*p3/4,
                           eps*eps*delta*p4/2,eps*eps*V_SUCCESS*ur/2]
                assert all(z>=budget/(1<<60) for z in exponents)
                assert width-b>=2
                width-=b+1;stages+=1
            assert width==1;parameter_cases+=1
    partial=sum((F(2,(2*j+1)*3**(2*j+1)) for j in range(16)),F(0))
    ln_upper=partial+F(18,8*33*3**33)
    def exponential(x):
        low=sum((x**j/factorial(j) for j in range(40)),F(0))
        return low,low+x**40/factorial(40)/(1-x/41)
    r=F(51651,20000);upper=F(2582557,1000000);u=F(880017,1000000)
    assert exponential(r*ln_upper)[1]<q<exponential(upper*partial)[0]
    assert u*u*r>2 and u*upper==F(2272694063469,10**12)
    out=dict(scope='Finite exact kernel/coin/quota and numerical density diagnostics; no asymptotic or device certification.',
             order8_correlation_checks=e_checks,order16_correlation_checks=b_checks,rejected_difference_kernel_checks=r_checks,
             global_rejected_phase_density_checks=density_checks,maximum_numeric_density_error=maximum,
             branchwise_coin_and_output_cases=coin_cases,parameter_cases=parameter_cases,
             exact_nine_event_stage_checks=stages,exact_exponential_coefficient='2272694063469/1000000000000')
    Path(__file__).with_name('recycle_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
