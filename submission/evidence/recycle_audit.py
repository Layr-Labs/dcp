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

def capacity(ell):return ell+sum(6369*j//2500 for j in range(ell))
def parameters(n,m):
    lo,hi=1,m-1
    while lo<hi:
        mid=(lo+hi)//2
        if capacity(mid)>=m-1:hi=mid
        else:lo=mid+1
    ell=lo;lam=(1024*(n+1)-1).bit_length();final=(1<<62)*lam
    lengths=[(final*5847**t+1000**t-1)//1000**t for t in range(ell,-1,-1)]
    remaining=m-1-ell;widths=[]
    for i in range(ell):
        b=min(6369*(ell-i-1)//2500,remaining);widths.append(b);remaining-=b
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

def rsum_kernel(h,d):
    ts=r_terms(h);rev=[(2*h+3-i,v) for i,v in ts];target=4*h-2+d
    total=0
    for (a,aa),(b,bb),(c,cc),(e,ee) in product(ts,ts,rev,rev):
        rem=target-a-b-c-e
        if rem>=0:total+=aa*bb*cc*ee*comb(rem+15,15)
    return total

def derive_rsum_polynomials():
    # Exact integer polynomial expansion of3N, sofour factors scale81.
    from collections import defaultdict
    n=[(0,0,{3:3926,1:10000}),(0,1,{3:8222,2:-60000,1:40000}),
     (0,2,{3:-48222,2:120000,1:-60000,0:60000}),(0,3,{3:56074,2:-60000,1:20000}),
     (0,4,{3:-20000,1:-10000}),(1,0,{3:16074,2:-60000}),
     (1,1,{3:-48222,2:120000,1:-60000}),(1,2,{3:48222,2:-60000}),
     (1,3,{3:-16074,1:60000}),(2,1,{1:-60000}),(2,2,{1:60000,0:-60000})]
    nr=[(2-a,3-b,c) for a,b,c in n]
    def hp_mul(p,q):
        r=defaultdict(int)
        for a,c in p.items():
            for b,d in q.items():r[a+b]+=c*d
        return {a:c for a,c in r.items() if c}
    def groups_mul(p,q):
        r={}
        for (a,b),v in p.items():
            for (aa,bb),w in q.items():
                key=a+aa,b+bb
                if key not in r:r[key]=defaultdict(int)
                for j,c in hp_mul(v,w).items():r[key][j]+=c
        return {key:{j:c for j,c in v.items() if c} for key,v in r.items() if any(v.values())}
    b=groups_mul({(a,bb):v for a,bb,v in n},{(a,bb):v for a,bb,v in nr})
    g=groups_mul(b,b);raw=defaultdict(int)
    for (a,bb),coeff in g.items():
        if a>4:continue
        bp={(0,0):1}
        for j in range(15):
            temp=defaultdict(int)
            for (hp,dp),v in bp.items():
                temp[hp+1,dp]+=v*(4-a);temp[hp,dp+1]+=v;temp[hp,dp]+=v*(13-bb-j)
            bp={key:v for key,v in temp.items() if v}
        for (hp,dp),v in bp.items():
            for ep,c in coeff.items():raw[hp+ep,dp]+=v*c
    poly={key:F(v,81*factorial(15)) for key,v in raw.items() if v}
    zero=defaultdict(F)
    for (hp,dp),v in poly.items():
        if dp==0:zero[hp]+=v
    for hp,c in g.get((4,14),{}).items():zero[hp]+=F(c,81)
    return poly,{hp:v for hp,v in zero.items() if v}

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
        assert k0>=F(9,25)*h**7
        for d in range(h+1):
            actual=sum(sums[i]*sums[i+d] for i in range(len(sums)-d))
            assert actual==vsum_kernel(h,d)==vsum_poly(F(h),F(d))
            assert actual>=F(9,50)*h**7
            if d<h:
                coin=F(9*h**7,(25 if d==0 else 50)*actual)
                absolute=actual if d==0 else 2*actual
                assert 0<=coin<=1 and F(absolute,2*h**8)*coin==F(9,50*h)
            vsum_checks+=1
    # Bidegree(7,7) identity is certified at an 8x8 rational grid.
    table=json.loads(Path(__file__).with_name('vsum-bernstein.json').read_text())['rows']
    table=[[F(v) for v in row] for row in table]
    assert len(table)==8 and all(len(row)==8 for row in table)
    assert all(v>0 for row in table for v in row)
    for zi in range(8):
        for xi in range(8):
            z=F(zi);x=F(xi,7);h=z+2;d=h*x
            left=vsum_poly(h,d)-F(9,50)*h**7
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
            assert direct>=F(4642**2*h**7,4 if d==0 else 8)
            if h>=8:
                assert direct==(r_zero(h) if d==0 else r_poly(F(h),F(d)))
            coin=F(4642**2*h**7,(4 if d==0 else 8)*direct)
            absolute=direct if d==0 else 2*direct
            assert 0<=coin<=1 and F(absolute,2*4642**2*h**8)*coin==F(1,8*h)
            r_checks_new+=1
    rcert=json.loads(Path(__file__).with_name('vreject-bernstein.json').read_text())
    assert rcert['p']=='1/8' and rcert['segments']==4
    rows=[[[F(v) for v in row] for row in segment] for segment in rcert['rows']]
    assert len(rows)==4 and all(len(seg)==8 and all(len(row)==8 for row in seg) for seg in rows)
    assert all(v>0 for seg in rows for row in seg for v in row)
    assert min(v for seg in rows for row in seg for v in row)==F(5742665,144)
    for segment in range(4):
        for zi in range(8):
            for ui in range(8):
                z=F(zi);u=F(ui,7);h=z+8;d=h*(u+segment)/4
                left=r_poly(h,d)-F(4642**2,8)*h**7
                right=sum((z**k*rows[segment][k][j]*comb(7,j)*u**j*(1-u)**(7-j) for k in range(8) for j in range(8)),F(0))
                assert left==right
    zcoeff=[F(24158041501696),F(458083343793664,21),F(76159948669696,9),F(16451192619520,9),F(2136563057440,9),F(166800153808,9),F(7246625992,9),F(945920749,63)]
    assert all(v>0 for v in zcoeff)
    for z in range(8):
        h=z+8
        assert r_zero(h)-F(4642**2,4)*h**7==sum(v*z**i for i,v in enumerate(zcoeff))
    scert=json.loads(Path(__file__).with_name('rsum-certificate.json').read_text())
    assert scert['beta']=='1/5' and scert['shift']==16 and scert['degree']==15 and scert['segments']==1
    sp,sz=derive_rsum_polynomials()
    spjson={(t['h'],t['d']):F(t['coefficient']) for t in scert['polynomial']}
    szjson={t['h']:F(t['coefficient']) for t in scert['central']}
    assert sp==spjson and sz==szjson and len(sp)==len(scert['polynomial'])==126
    assert max(hp+dp for hp,dp in sp)==15
    def speval(h,d):return sum((v*h**hp*d**dp for (hp,dp),v in sp.items()),F(0))
    def szeval(h):return sum((v*h**hp for hp,v in sz.items()),F(0))
    rsum_checks=0
    for h in (2,4,8,16,32,64):
        sw=r_weights(h);tt=[0]*(4*h-1)
        for i,a in enumerate(sw):
            for j,b in enumerate(sw):tt[i+j]+=a*b
        assert sum(tt)==4642**2*h**8
        for d in range(h):
            actual=sum(tt[i]*tt[i+d] for i in range(len(tt)-d))
            assert actual==rsum_kernel(h,d)
            if h>=16:assert actual==(szeval(h) if d==0 else speval(F(h),F(d)))
            assert 5*actual>=4642**4*h**15*(2 if d==0 else 1)
            coin=F(4642**4*h**15*(2 if d==0 else 1),5*actual)
            absolute=actual if d==0 else 2*actual
            assert 0<=coin<=1 and F(absolute,2*4642**4*h**16)*coin==F(1,5*h)
            rsum_checks+=1
    srows=[[[F(v) for v in row] for row in segment] for segment in scert['rows']]
    assert len(srows)==1 and len(srows[0])==16 and all(len(row)==16 for row in srows[0])
    assert all(v>0 for row in srows[0] for v in row)
    scentral=[F(v) for v in scert['central_shift']]
    assert len(scentral)==16 and all(v>0 for v in scentral)
    for zi in range(16):
        for ui in range(16):
            z=F(zi);u=F(ui,15);h=z+16;d=h*u
            left=speval(h,d)-F(4642**4,5)*h**15
            right=sum((z**k*srows[0][k][j]*comb(15,j)*u**j*(1-u)**(15-j) for k in range(16) for j in range(16)),F(0))
            assert left==right
    for z in range(16):
        h=z+16
        assert szeval(h)-F(2*4642**4,5)*h**15==sum(v*z**i for i,v in enumerate(scentral))
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
                                for zr in range(p6+1):
                                    p7=zr//2
                                    coins=(p1-z1)+(p2-z2)+(p3-z3)+p4+(ur-zv)+p5+(p6-zr)+p7
                                    assert 8*coins<=7*(2*p1)
                                    max_outputs=d1+(p2-z2)+(p3-z3)+p4+(ur-zv-rv)+p5+(p6-zr)+p7
                                    assert max_outputs<=p1
                                    coin_cases+=1
    eps=F(1,1<<20);gamma=F(151,1260);theta=F(6661,40320)+F(1,1536)+(F(2679,10000)-F(1,4))/16+F(9,3200)+F(2321,2560000)+F(2321,6400000);q=F(5847,1000)
    assert theta==F(7,48)+gamma/32+F(2679,160000)+F(1,1536)+F(9,3200)+F(2321,2560000)+F(2321,6400000)
    assert q*theta>1
    assert q*(theta-eps)-1>F(1,8192)
    assert F(18081,40320)<F(1,2)
    parameter_cases=stages=0
    for n in list(range(17,2049))+[4096,16384,100000,1000000]:
        for m in (n-1,n):
            ell,final,lengths,widths=parameters(n,m)
            planned=4*(m-ell)*lengths[0]
            a=1024*planned*(n+3);msrc=8192*(a-1).bit_length()
            assert msrc>0 and F(4*(n+3),a**4)<F(1,1024*planned)
            assert capacity(ell)>=m-1>capacity(ell-1)
            assert 625000000*max(0,ell-2)**2<=490666801*n
            assert sum(widths)==m-1-ell and sum(lengths[:-1])<2*lengths[0]
            width=m
            for i,b in enumerate(widths):
                qp=q**(ell-i-1);k=1<<b;budget=final*qp
                assert k<=qp
                p1=F(lengths[i]-k,2)
                z1=(1-eps)*p1/2;v=(1-eps)*p1/4
                p2=(z1-k)/2;z2=(1-eps)*p2/2;p3=(z2-k)/2;z3=(1-eps)*p3/2;p4=(z3-k)/2;ur=(v-k)/2;zv=(1-eps)*ur/2;p5=(zv-k)/2;rv=(1-eps)*F(2321,10000)*ur;p6=(rv-k)/2;zr=(1-eps)*p6/2;p7=(zr-k)/2
                y=(1-eps)*(p1/4+p2/6+gamma*p3+p4/12+F(2679,10000)*ur+F(9,50)*p5+F(1,8)*p6+F(1,5)*p7)
                assert p1>=budget and p2>=budget/16 and p3>=budget/256 and ur>=budget/32 and p4>=budget/4096 and p5>=budget/512 and p6>=budget/512 and p7>=budget/4096
                assert y>=lengths[i+1]
                exponents=[eps*eps*p1/8,eps*eps*p1/4,eps*eps*p1/8,
                           eps*eps*p2/12,eps*eps*p2/4,eps*eps*gamma*p3/2,eps*eps*p3/4,eps*eps*p4/24,eps*eps*ur/8,eps*eps*ur/4,eps*eps*F(9,50)*p5/2,eps*eps*F(2321,10000)*ur/2,eps*eps*p6/16,eps*eps*p6/4,eps*eps*p7/10]
                assert all(z>=budget/(1<<58) for z in exponents)
                assert width-b>=2
                width-=b+1;stages+=1
            assert width==1;parameter_cases+=1
    partial=sum((F(2,(2*j+1)*3**(2*j+1)) for j in range(8)),F(0))
    assert partial>F(693147,1000000) and partial+F(9,4*17*3**17)<F(693148,1000000)
    x=(3-F(6369,2500))*F(693147,1000000)
    assert sum((x**j/factorial(j) for j in range(7)),F(0))>8/q
    x=(3-F(25477,10000))*F(693148,1000000)
    assert sum((x**j/factorial(j) for j in range(7)),F(0))+x**7/F(factorial(7))/(1-x/8)<8/q
    assert F(22151,25000)**2*F(6369,2500)>2
    assert F(22151,25000)*F(25477,10000)==F(564341027,250000000)
    assert F(17321,10000)**2>3
    out=dict(scope='Finite exact kernel/coin/quota and numerical density diagnostics; no asymptotic or device certification.',
             order8_correlation_checks=e_checks,order16_correlation_checks=fourth_checks,global_vsum_kernel_checks=vsum_checks,bernstein_identity_grid_points=64,elementary_source_error_schedules=parameter_cases,rejected_rescue_kernel_checks=r_checks_new,rejected_rescue_certificate_points=256,rsum_actual_kernel_checks=rsum_checks,rsum_coefficient_identity_terms=126,rsum_positive_identity_points=256,rsum_central_identity_points=16,polynomial_identity_points=16,rejected_difference_kernel_checks=r_checks,
             global_rejected_phase_density_checks=density_checks,maximum_numeric_density_error=maximum,
             branchwise_coin_and_output_cases=coin_cases,parameter_cases=parameter_cases,
             exact_fifteen_event_stage_checks=stages,exact_exponential_coefficient='564341027/250000000')
    Path(__file__).with_name('recycle_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
