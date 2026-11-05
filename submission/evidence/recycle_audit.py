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

def qstate(f,n,s):return [1/2**.5,cmath.exp(2j*cmath.pi*f*s/n)/2**.5]
def difference(v,w,negative):
    out=[(2**.5)*v[0]*w[1],(2**.5)*v[1]*w[0]]
    if negative:out.reverse()
    return out

def capacity(ell):return ell+sum(1033*j//400 for j in range(ell))
def parameters(n,m):
    lo,hi=1,m-1
    while lo<hi:
        mid=(lo+hi)//2
        if capacity(mid)>=m-1:hi=mid
        else:lo=mid+1
    ell=lo;lam=(1024*(n+1)-1).bit_length();final=(1<<62)*lam
    lengths=[(final*599**t+100**t-1)//100**t for t in range(ell,-1,-1)]
    remaining=m-1-ell;widths=[]
    for i in range(ell):
        b=min(1033*(ell-i-1)//400,remaining);widths.append(b);remaining-=b
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
            assert F(count,h**3)>=F(2679,10000)
            abs_count=count if d==0 else 2*count
            probability=F(5358*h**3 if d==0 else 2679*h**3,10000*count)
            assert 0<=probability<=1
            kept.append(F(abs_count,h**4)*F(1,2)*probability)
            r_checks+=1
        assert all(p==F(2679,10000*h) for p in kept) and sum(kept)==F(2679,10000)
    fourth_checks=0
    for m in range(4,33,2):
        counts=[1]
        for _ in range(8):
            updated=[0]*(len(counts)+m-1)
            for i,v in enumerate(counts):
                for j in range(m):updated[i+j]+=v
            counts=updated
        assert sum(counts)==m**8
        center=8*(m-1)
        f0=sum(v*v for v in counts)
        assert F(f0,4*m**15)>F(1,12)
        for d in range(m//2+1):
            actual=sum(counts[i]*counts[i+d] for i in range(len(counts)-d))
            formula=sum((-1)**j*comb(16,j)*(comb(center+d-j*m+15,15) if center+d-j*m>=0 else 0) for j in range(17))
            assert actual==formula and 2*actual>=f0
            if d<m//2:
                abs_count=actual if d==0 else 2*actual
                coin=F(1) if d==0 else F(f0,2*actual)
                assert F(abs_count,2*m**16)*coin==F(f0,2*m**16)
            fourth_checks+=1
    # Exact degree-15 polynomial identity: sixteen distinct H values suffice.
    central={15:F(2386873693184,212837625),13:F(57402368,42525),11:F(51803008,212625),9:F(14540608,297675),7:F(2186132,212625),5:F(1041848,467775),3:F(1066724,2149875),1:F(2,15)}
    halfdiff={15:F(2021749533234257,217945728000),13:F(1066650359,1555200),11:F(837883421,15552000),9:-F(138861587,76204800),7:-F(86478337,31104000),5:-F(9170783,8553600),3:-F(46135813,137592000),1:-F(7,60)}
    assert central[15]/2**15>F(1,3) and all(v>0 for v in central.values())
    assert halfdiff[15]>9000 and sum(-v for v in halfdiff.values() if v<0)<7
    def kernel(m,d):
        center=8*(m-1)+d
        return sum((-1)**j*comb(16,j)*(comb(center-j*m+15,15) if center-j*m>=0 else 0) for j in range(17))
    for h in range(1,17):
        assert kernel(2*h,0)==sum(v*h**k for k,v in central.items())
        assert 2*kernel(2*h,h)-kernel(2*h,0)==sum(v*h**k for k,v in halfdiff.items())
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
    eps=F(1,1<<20);gamma=F(151,1260);theta=F(6661,40320)+F(1,1536)+(F(2679,10000)-F(1,4))/16;q=F(599,100)
    assert theta==F(7,48)+gamma/32+F(2679,160000)+F(1,1536)
    assert q*theta>1
    assert q*(theta-eps)-1>F(1,8192)
    assert F(18081,40320)<F(1,2)
    parameter_cases=stages=0
    for n in list(range(17,2049))+[4096,16384,100000,1000000]:
        for m in (n-1,n):
            ell,final,lengths,widths=parameters(n,m)
            assert capacity(ell)>=m-1>capacity(ell-1)
            assert 400000000*max(0,ell-2)**2<=309795201*n
            assert sum(widths)==m-1-ell and sum(lengths[:-1])<2*lengths[0]
            width=m
            for i,b in enumerate(widths):
                qp=q**(ell-i-1);k=1<<b;budget=final*qp
                assert k<=qp
                p1=F(lengths[i]-k,2)
                z1=(1-eps)*p1/2;v=(1-eps)*p1/4
                p2=(z1-k)/2;z2=(1-eps)*p2/2;p3=(z2-k)/2;z3=(1-eps)*p3/2;p4=(z3-k)/2;ur=(v-k)/2
                y=(1-eps)*(p1/4+p2/6+gamma*p3+p4/12+F(2679,10000)*ur)
                assert p1>=budget and p2>=budget/16 and p3>=budget/256 and ur>=budget/32 and p4>=budget/4096
                assert y>=lengths[i+1]
                exponents=[eps*eps*p1/8,eps*eps*p1/4,eps*eps*p1/8,
                           eps*eps*p2/12,eps*eps*p2/4,eps*eps*gamma*p3/2,eps*eps*p3/4,eps*eps*p4/24,eps*eps*ur/8]
                assert all(z>=budget/(1<<58) for z in exponents)
                assert width-b>=2
                width-=b+1;stages+=1
            assert width==1;parameter_cases+=1
    partial=sum((F(2,(2*j+1)*3**(2*j+1)) for j in range(8)),F(0))
    assert partial>F(693147,1000000) and partial+F(9,4*17*3**17)<F(693148,1000000)
    x=(3-F(1033,400))*F(693147,1000000)
    assert sum((x**j/factorial(j) for j in range(7)),F(0))>8/q
    x=(3-F(12913,5000))*F(693148,1000000)
    assert sum((x**j/factorial(j) for j in range(7)),F(0))+x**7/F(factorial(7))/(1-x/8)<8/q
    assert F(17601,20000)**2*F(1033,400)>2
    assert F(17601,20000)*F(12913,5000)==F(227281713,100000000)
    assert F(17321,10000)**2>3
    out=dict(scope='Finite exact kernel/coin/quota and numerical density diagnostics; no asymptotic or device certification.',
             order8_correlation_checks=e_checks,order16_correlation_checks=fourth_checks,polynomial_identity_points=16,rejected_difference_kernel_checks=r_checks,
             global_rejected_phase_density_checks=density_checks,maximum_numeric_density_error=maximum,
             branchwise_coin_and_output_cases=coin_cases,parameter_cases=parameter_cases,
             exact_nine_event_stage_checks=stages,exact_exponential_coefficient='227281713/100000000')
    Path(__file__).with_name('recycle_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
