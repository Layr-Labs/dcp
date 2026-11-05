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

def capacity(ell):return ell+sum(51001*j//20000 for j in range(ell))
def parameters(n,m):
    lo,hi=1,m-1
    while lo<hi:
        mid=(lo+hi)//2
        if capacity(mid)>=m-1:hi=mid
        else:lo=mid+1
    ell=lo;lam=(1024*(n+1)-1).bit_length();final=(1<<62)*lam
    lengths=[(((2*final+t)*435891456000000**t-final*3**t*74427789362209**t)+74427789362209**t-1)//74427789362209**t for t in range(ell,-1,-1)]
    remaining=m-1-ell;widths=[]
    for i in range(ell):
        b=min(51001*(ell-i-1)//20000,remaining);widths.append(b);remaining-=b
    assert remaining==0
    return ell,final,lengths,widths

def r_weights(h):
    w=[0]+[h-d for d in range(1,h)]+[2*h-d for d in range(h,2*h)]
    jj=[sum(w[i]*w[i+d] for i in range(2*h-d)) for d in range(2*h)]
    return [10000*jj[0]-5358*h**3]+[20000*jj[d]-(5358*h**3 if d<h else 0) for d in range(1,2*h)]

def r_terms(h):
    if h<8:
        sw=r_weights(h);n={}
        for j,c in enumerate(sw):
            for k in range(5):n[j+k]=n.get(j+k,0)+c*(-1)**k*comb(4,k)
        return [(i,v) for i,v in n.items() if v]
    coeff=[(0,0,F(2*h*(1963*h*h+5000),3)),
      (0,1,F(2*h*(4111*h*h-30000*h+20000),3)),
      (0,2,-2*(8037*h**3-20000*h*h+10000*h-10000)),
      (0,3,F(2*h*(28037*h*h-30000*h+10000),3)),
      (0,4,-F(10000*h*(2*h*h+1),3)),
      (1,0,2*h*h*(2679*h-10000)),
      (1,1,-2*h*(8037*h*h-20000*h+10000)),
      (1,2,2*h*h*(8037*h-10000)),
      (1,3,-2*h*(2679*h*h-10000)),(2,1,-20000*h),(2,2,20000*(h-1))]
    assert all(F(c).denominator==1 for a,b,c in coeff)
    return [(a*h+b,int(c)) for a,b,c in coeff]

def r_kernel(h,d):
    ts=r_terms(h);rev=[(2*h+3-i,c) for i,c in ts];target=2*h-1+d
    total=0
    for (i,c),(j,v) in product(ts,rev):
        rem=target-i-j
        if rem>=0:total+=c*v*comb(rem+7,7)
    return total

def r_poly(h,d):
    # Each tuple is (dPower,hPower,coefficient), exactly Section11.6.
    terms=[(7,0,F(5000000,63)),(6,1,F(10000000,9)),
    (5,2,-F(40000000,3)),(5,1,F(10000000,3)),(5,0,-F(10000000,9)),
    (4,3,-F(63395000,3)),(4,2,F(100000000,3)),(4,1,-F(50000000,9)),
    (3,4,F(682220000,9)),(3,3,-F(526790000,3)),(3,2,F(100000000,9)),
    (3,1,-F(50000000,3)),(3,0,F(35000000,9)),
    (2,5,-F(20740000,3)),(2,4,F(200000000,3)),(2,3,-F(36605000,3)),(2,1,-F(80000000,9)),
    (1,6,-F(415413476,9)),(1,5,F(107160000)),(1,4,-F(1278520000,9)),
    (1,3,-F(73210000,3)),(1,2,-F(160000000,3)),(1,1,F(40000000,3)),(1,0,-F(20000000,7)),
    (0,7,F(1285304332,63)),(0,6,-F(80740000,3)),(0,5,F(578890000,9)),
    (0,3,F(280000000,9)),(0,2,-F(80000000,3)),(0,1,F(40000000,7))]
    return sum((c*d**dp*h**hp for dp,hp,c in terms),F(0))

def r_zero(h):
    return F(4*h,63)*(321326083*h**6-561295000*h**5+1013057500*h**4
      -418705000*h**3+490000000*h*h-595000000*h+90000000)

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
        assert F(f0,4*m**15)>=F(2330931341,27243216000)
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
    def vsum_kernel(h,d):
        terms=[(1,h-1),(2,-h),(h,h),(h+1,-h),(2*h+1,1)]
        rev=[(2*h+1-e,c) for e,c in terms]
        target=4*h-2+d
        val=0
        for (a,aa),(b,bb),(c,cc),(e,ee) in product(terms,terms,rev,rev):
            remaining=target-a-b-c-e
            if remaining>=0:val+=aa*bb*cc*ee*comb(remaining+7,7)
        return val
    def vsum_poly(h,d):
        central=F(227,630)*h**7+F(2,15)*h**6+F(41,90)*h**5+F(7,45)*h**3-F(2,15)*h**2+F(1,35)*h
        return (F(1,1680)*d**7+h*d**6/120
          +d**5*(-F(3,40)*h*h+h/40-F(1,120))
          +d**4*(-h**3/9+F(5,24)*h*h-h/72)
          +d**3*(h**4/2-h**3+F(7,24)*h*h-h/8+F(7,240))
          +d*d*(-F(13,30)*h**5+F(2,3)*h**4-F(7,18)*h**3+h*h/8-F(11,180)*h)
          +d*(-h**4/2-F(13,60)*h*h+h/10-F(3,140))+central)
    vsum_checks=0
    for h in range(2,66,2):
        weights=[0]+[h-d for d in range(1,h)]+[2*h-d for d in range(h,2*h)]
        sums=[0]*(4*h-1)
        for i,x in enumerate(weights):
            for j,y in enumerate(weights):sums[i+j]+=x*y
        assert sum(sums)==h**4
        k0=sum(v*v for v in sums)
        assert k0>=F(227,630)*h**7
        for d in range(h+1):
            actual=sum(sums[i]*sums[i+d] for i in range(len(sums)-d))
            assert actual==vsum_kernel(h,d)==vsum_poly(F(h),F(d))
            assert actual>=F(227,1260)*h**7
            if d<h:
                coin=F(227*h**7,(630 if d==0 else 1260)*actual)
                absolute=actual if d==0 else 2*actual
                assert 0<=coin<=1 and F(absolute,2*h**8)*coin==F(227,1260*h)
            vsum_checks+=1
    # Bidegree(7,7) identity is certified at an 8x8 rational grid.
    table=json.loads(Path(__file__).with_name('vsum-bernstein.json').read_text())['rows']
    table=[[F(v) for v in row] for row in table]
    assert len(table)==8 and all(len(row)==8 for row in table)
    assert all(v>0 for row in table for v in row)
    for zi in range(8):
        for xi in range(8):
            z=F(zi);x=F(xi,7);h=z+2;d=h*x
            left=vsum_poly(h,d)-F(227,1260)*h**7
            right=sum((z**k*table[k][j]*comb(7,j)*x**j*(1-x)**(7-j) for k in range(8) for j in range(8)),F(0))
            assert left==right
    r_checks_new=0
    for h in (2,4,8,16,32,64,128):
        sw=r_weights(h)
        assert min(sw)>=0 and sum(sw)==4642*h**4
        ns=r_terms(h);expanded={}
        for i,v in enumerate(sw):
            for k in range(5):expanded[i+k]=expanded.get(i+k,0)+v*(-1)**k*comb(4,k)
        assert {i:v for i,v in expanded.items() if v}==dict(ns)
        for d in range(h):
            direct=sum(sw[i]*sw[i+d] for i in range(2*h-d))
            assert direct==r_kernel(h,d)
            assert direct>=F(13,100)*4642**2*h**7*(2 if d==0 else 1)
            if h>=8:
                assert direct==(r_zero(h) if d==0 else r_poly(F(h),F(d)))
            coin=F(13*4642**2*h**7,(50 if d==0 else 100)*direct)
            absolute=direct if d==0 else 2*direct
            assert 0<=coin<=1 and F(absolute,2*4642**2*h**8)*coin==F(13,100*h)
            r_checks_new+=1
    rcert=json.loads(Path(__file__).with_name('vreject-bernstein.json').read_text())
    assert rcert['p']=='13/100' and rcert['segments']==5
    rows=[[[F(v) for v in row] for row in segment] for segment in rcert['rows']]
    intervals=[[F(v) for v in interval] for interval in rcert['intervals']]
    assert len(rows)==5 and all(len(seg)==8 and all(len(row)==8 for row in seg) for seg in rows)
    assert intervals[0][0]==0 and intervals[-1][1]==1
    assert all(a<b for a,b in intervals) and all(intervals[i][1]==intervals[i+1][0] for i in range(4))
    assert all(v>0 for seg in rows for row in seg for v in row)
    for segment,(start,end) in enumerate(intervals):
        for zi in range(8):
            for ui in range(8):
                z=F(zi);u=F(ui,7);h=z+8;d=h*(start+(end-start)*u)
                left=r_poly(h,d)-F(13*4642**2,100)*h**7
                right=sum((z**k*rows[segment][k][j]*comb(7,j)*u**j*(1-u)**(7-j) for k in range(8) for j in range(8)),F(0))
                assert left==right
    zcoeff=[F(v) for v in rcert['central_shift']]
    assert len(zcoeff)==8 and all(v>0 for v in zcoeff)
    for z in range(8):
        h=z+8
        assert r_zero(h)-F(13*4642**2,50)*h**7==sum(v*z**i for i,v in enumerate(zcoeff))
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
                        for zv in range(ur+1):
                            p5=zv//2
                            for rv in range(ur-zv+1):
                                p6=rv//2
                                coins=(p1-z1)+(p2-z2)+(p3-z3)+p4+(ur-zv)+p5+p6
                                assert 8*coins<=7*(2*p1)
                                max_outputs=d1+(p2-z2)+(p3-z3)+p4+(ur-zv-rv)+p5+p6
                                assert max_outputs<=p1
                                coin_cases+=1
    gamma=F(151,1260);gamma4=F(2330931341,27243216000)
    beta5=F(227,1260);beta6=F(13,100);p0=F(2679,10000);eta=F(2321,10000)
    theta=F(1,8)+F(1,48)+gamma/32+gamma4/128+p0/16+beta5/64+eta*beta6/32
    q=1/theta
    assert theta==F(74427789362209,435891456000000) and 5<q<6
    # Exact linear propagation of all thirteen additive events.
    add=lambda *vs:tuple(sum(xs) for xs in zip(*vs))
    scale=lambda v,a:tuple(a*x for x in v)
    mk=(F(0),F(-1),F(0));mg=(F(0),F(0),F(-1))
    pair=lambda v:scale(add(v,mk),F(1,2))
    count=lambda v,p:add(scale(v,p),mg)
    v1=(F(1,2),F(-1,2),F(0));d1=count(v1,F(1,4));z1=count(v1,F(1,2));vv=count(v1,F(1,4))
    v2=pair(z1);d2=count(v2,F(1,6));z2=count(v2,F(1,2));v3=pair(z2);d3=count(v3,gamma);z3=count(v3,F(1,2))
    v4=pair(z3);d4=count(v4,gamma4);vr=pair(vv);dv=count(vr,p0);zv=count(vr,F(1,2));rv=count(vr,eta)
    v5=pair(zv);d5=count(v5,beta5);v6=pair(rv);d6=count(v6,beta6)
    linear=add(d1,d2,d3,d4,dv,d5,d6)
    assert linear[0]==theta and -linear[1]<F(3,4) and -linear[2]<16
    assert 3**32>=32**2*2**32
    assert 36*128**2<2**20
    parameter_cases=stages=0
    for n in list(range(17,2049))+[4096,16384,100000,1000000]:
        for m in (n-1,n):
            ell,final,lengths,widths=parameters(n,m)
            planned=4*(m-ell)*lengths[0]
            a=1024*planned*(n+3);msrc=8192*(a-1).bit_length()
            assert msrc>0 and F(4*(n+3),a**4)<F(1,1024*planned)
            assert capacity(ell)>=m-1>capacity(ell-1)
            assert 1000000000000*max(0,ell-2)**2<=885607**2*n
            assert sum(widths)==m-1-ell and sum(lengths[:-1])<2*lengths[0]
            assert lengths[-1]==final and final%128==0
            width=m
            for i,b in enumerate(widths):
                t=ell-i;k=1<<b;ii=lengths[i]
                assert k*74427789362209**(t-1)<=435891456000000**(t-1)
                slack=final*3**(t-1)//128
                p1=F(ii-k,2);d1=p1/4-slack;z1=p1/2-slack;v=p1/4-slack
                p2=(z1-k)/2;d2=p2/6-slack;z2=p2/2-slack
                p3=(z2-k)/2;d3=gamma*p3-slack;z3=p3/2-slack
                p4=(z3-k)/2;d4=gamma4*p4-slack
                ur=(v-k)/2;dv=p0*ur-slack;zv=ur/2-slack;rv=eta*ur-slack
                p5=(zv-k)/2;d5=beta5*p5-slack;p6=(rv-k)/2;d6=beta6*p6-slack
                y=d1+d2+d3+d4+dv+d5+d6
                assert y>=theta*ii-F(3,4)*k-16*slack
                assert y>=lengths[i+1]
                assert F(slack*slack,ii)>=F(final,2**20)
                assert F(lengths[i],1)>=q*lengths[i+1]
                assert width-b>=2
                width-=b+1;stages+=1
            assert width==1;parameter_cases+=1
    partial=sum((F(2,(2*j+1)*3**(2*j+1)) for j in range(8)),F(0))
    assert partial>F(693147,1000000) and partial+F(9,4*17*3**17)<F(693148,1000000)
    x=(3-F(51001,20000))*F(693147,1000000)
    assert sum((x**j/factorial(j) for j in range(7)),F(0))>8/q
    x=(3-F(127503,50000))*F(693148,1000000)
    assert sum((x**j/factorial(j) for j in range(7)),F(0))+x**7/F(factorial(7))/(1-x/8)<8/q
    assert F(885607,1000000)**2*F(51001,20000)>2
    assert F(885607,1000000)*F(127503,50000)==F(112917549321,50000000000)
    assert F(17321,10000)**2>3
    out=dict(scope='Finite exact kernel/coin/quota and numerical density diagnostics; no asymptotic or device certification.',
             order8_correlation_checks=e_checks,order16_correlation_checks=fourth_checks,global_vsum_kernel_checks=vsum_checks,bernstein_identity_grid_points=64,elementary_source_error_schedules=parameter_cases,rejected_rescue_kernel_checks=r_checks_new,rejected_rescue_certificate_points=320,polynomial_identity_points=16,rejected_difference_kernel_checks=r_checks,
             global_rejected_phase_density_checks=density_checks,maximum_numeric_density_error=maximum,
             branchwise_coin_and_output_cases=coin_cases,parameter_cases=parameter_cases,
             exact_additive_thirteen_event_stage_checks=stages,exact_exponential_coefficient='112917549321/50000000000')
    Path(__file__).with_name('recycle_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
