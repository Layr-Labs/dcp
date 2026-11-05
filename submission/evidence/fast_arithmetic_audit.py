"""Finite adaptive-product diagnostics; no timing, asymptotic or device claim."""
import json,math,random
from functools import lru_cache
from pathlib import Path
calls=0;radices=set()

@lru_cache(None)
def matrix(k):
    count=2*k-1;D=math.factorial(count-1);M=[]
    for j in range(count):
        poly=[1];den=1
        for h in range(count):
            if h==j:continue
            out=[0]*(len(poly)+1)
            for i,c in enumerate(poly):out[i]-=h*c;out[i+1]+=c
            poly=out;den*=j-h
        assert D%den==0
        M.append([c*(D//den) for c in poly])
    return D,M


def product(a,b,width):
    global calls
    calls+=1
    assert abs(a).bit_length()<=width and abs(b).bit_length()<=width
    sign=-1 if (a<0)!=(b<0) else 1
    a,b=abs(a),abs(b)
    if width<=65536:return sign*a*b
    L=width.bit_length()-1;u=math.isqrt(L);k=1<<u;radices.add(k)
    s=(width+k-1)//k;B=1<<s;mask=B-1
    child=s+k*(u+1)+1
    assert child*k<=2*width and child<width
    av=[(a>>(i*s))&mask for i in range(k)]
    bv=[(b>>(i*s))&mask for i in range(k)]
    D,M=matrix(k);values=[]
    for j in range(2*k-1):
        aa=bb=0
        for i in reversed(range(k)):aa=aa*j+av[i];bb=bb*j+bv[i]
        values.append(product(aa,bb,child))
    coeff=[]
    for i in range(2*k-1):
        v=sum(M[j][i]*values[j] for j in range(2*k-1))
        assert v%D==0
        coeff.append(v//D)
    assert min(coeff)>=0
    out=0
    for c in reversed(coeff):out=(out<<s)+c
    return sign*out

rng=random.Random(5573);products=basis=width_cases=0
for k in (16,32,64):
    D,M=matrix(k)
    for j in range(2*k-1):
        for h in range(2*k-1):
            acc=0
            for c in reversed(M[j]):acc=acc*h+c
            assert acc==(D if j==h else 0)
            basis+=1
for width in (1,32,65536,65537,65538,262144,1048576):
    for _ in range(2):
        a,b=rng.getrandbits(width),rng.getrandbits(width)
        assert product(a,b,width)==a*b
        assert product(-a,b,width)==-a*b
        products+=2
# Force the first actual radix-32 branch with a sparse but full-width operand.
width=1<<25;a=(1<<(width-1))+rng.getrandbits(1024);b=3
assert product(a,b,width)==a*b
products+=1
for width in list(range(65537,80000,17))+[10**6,10**9,1<<25,1<<64,1<<100,1<<256,1<<4096]:
    L=width.bit_length()-1;u=math.isqrt(L);k=1<<u
    child=(width+k-1)//k+k*(u+1)+1
    assert k*k*(u+1)+2*k<=width
    assert child*k<=2*width and child<width
    gain=math.sqrt(math.log2(width))-math.sqrt(math.log2(child))
    assert gain>=0.2
    width_cases+=1
out=dict(scope='Finite exact product and width diagnostics only; no performance, asymptotic or quantum execution claim.',
         lagrange_basis_evaluations=basis,declared_width_signed_products=products,
         recursive_calls=calls,actual_recursion_radices=sorted(radices),
         universal_width_contraction_diagnostics=width_cases,
         largest_declared_product_width=1<<25,
         large_width_note='The radix32 branch used a full-width sparse operand times3; no random dense 33-million-bit product was tested.')
Path(__file__).with_name('fast_arithmetic_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
