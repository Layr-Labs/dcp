"""Finite PG4 diagnostics, not asymptotic proof or quantum device execution."""
import cmath, json, math, random
from pathlib import Path
K=16;POINTS=31;D=math.factorial(30)
M=[]
for j in range(POINTS):
    poly=[1];den=1
    for h in range(POINTS):
        if h==j:continue
        out=[0]*(len(poly)+1)
        for i,c in enumerate(poly):out[i]-=h*c;out[i+1]+=c
        poly=out;den*=j-h
    assert D%den==0
    M.append([c*(D//den) for c in poly])
for j in range(31):
    for h in range(31):
        acc=0
        for c in reversed(M[j]):acc=acc*h+c
        assert acc==(D if j==h else 0)
calls=0

def fastprod(a,b):
    global calls
    calls+=1
    sign=-1 if (a<0)!=(b<0) else 1
    a,b=abs(a),abs(b);size=max(a.bit_length(),b.bit_length())
    if size<=4096:return sign*a*b
    width=(size+15)//16;base=1<<width
    av=[(a>>(i*width))&(base-1) for i in range(16)]
    bv=[(b>>(i*width))&(base-1) for i in range(16)]
    values=[]
    for point in range(31):
        aa=bb=0
        for i in reversed(range(16)):aa=aa*point+av[i];bb=bb*point+bv[i]
        assert max(aa.bit_length(),bb.bit_length())<=width+80
        values.append(fastprod(aa,bb))
    cs=[]
    for i in range(31):
        value=sum(M[j][i]*values[j] for j in range(31))
        assert value%D==0
        cs.append(value//D)
    assert min(cs)>=0
    result=0
    for c in reversed(cs):result=result*base+c
    return sign*result


def rectangular(a,b,width):
    base=1<<width;mask=base-1
    assert b<base
    products=[]
    while a:
        products.append(fastprod(a&mask,b));a>>=width
    if not products:return 0
    digits=[products[0]&mask];carry=0
    for i in range(1,len(products)):
        value=(products[i]&mask)+(products[i-1]>>width)+carry
        digits.append(value&mask);carry=value>>width
        assert carry in (0,1)
    last=(products[-1]>>width)+carry
    assert last<=base
    out=last
    for d in reversed(digits):out=out*base+d
    return out


def apply_recursive_qft(v,start,width):
    if width==0:return v
    if width==1:
        w=v[:]
        for z in range(len(v)):
            if not z>>start&1:
                other=z|(1<<start)
                w[z]=(v[z]+v[other])/math.sqrt(2)
                w[other]=(v[z]-v[other])/math.sqrt(2)
        return w
    low=width//2;high=width-low
    v=apply_recursive_qft(v,start+low,high)
    for z in range(len(v)):
        a=(z>>start)&((1<<low)-1)
        c=(z>>(start+low))&((1<<high)-1)
        v[z]*=cmath.exp(2j*math.pi*a*c/(1<<width))
    v=apply_recursive_qft(v,start,low)
    out=[0j]*len(v);mask=((1<<width)-1)<<start
    for z in range(len(v)):
        d=(z>>start)&((1<<low)-1);c=(z>>(start+low))&((1<<high)-1)
        out[(z&~mask)|((c+(d<<high))<<start)]=v[z]
    return out

rng=random.Random(4417);products=rectangles=reciprocals=qft_columns=0
for bits in [0,1,60,4096,4097,8192,16384,65536]:
    for _ in range(3):
        a,b=rng.getrandbits(bits),rng.getrandbits(bits)
        assert fastprod(a,b)==a*b
        assert fastprod(-a,b)==-a*b
        products+=2
for n in [1,8,64,256,1024,4096]:
    for width in [1,3,7,16,64,128,256]:
        for _ in range(3):
            a=rng.getrandbits(n);b=rng.getrandbits(width)
            assert rectangular(a,b,width)==a*b
            rectangles+=1
for modulus in range(2,32):
    n=(modulus-1).bit_length()
    for extra in range(5):
        t=n+extra;reciprocal=(1<<t)//modulus
        for k in range(1<<t):
            q0=(k*reciprocal)>>t
            assert 0<=k//modulus-q0<=1
            r=k-q0*modulus
            assert 0<=r<2*modulus
            if r>=modulus:r-=modulus
            assert r==k%modulus
            reciprocals+=1
maximum=0.0
for bits in range(1,7):
    size=1<<bits
    for x in range(size):
        v=[0j]*size;v[x]=1
        v=apply_recursive_qft(v,0,bits)
        for z in range(size):
            error=abs(v[z]-cmath.exp(2j*math.pi*x*z/size)/math.sqrt(size))
            maximum=max(maximum,error);assert error<1e-12
        qft_columns+=1
assert 31<32
for r in range(1,33):
    probability=sum(math.comb(4*r,j) for j in range(r))/(1<<(4*r))
    assert probability<=math.exp(-r/4)
out=dict(scope='Finite diagnostics only; not asymptotic proof, hosted judgment or quantum execution.',
         lagrange_basis_evaluations=31**2,signed_16way_products=products,
         recursive_multiplication_calls=calls,rectangular_products=rectangles,
         exact_reciprocal_reduction_cases=reciprocals,recursive_qft_columns=qft_columns,
         maximum_numeric_qft_amplitude_error=maximum,binomial_cap_tail_checks=32)
Path(__file__).with_name('fast_arithmetic_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
