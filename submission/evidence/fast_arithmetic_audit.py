from fractions import Fraction as F
import json, random
from pathlib import Path

calls=0

def toom(a,b):
    global calls
    calls+=1
    sign=-1 if (a<0)!=(b<0) else 1
    a,b=abs(a),abs(b)
    n=max(a.bit_length(),b.bit_length())
    if n<=32:return sign*(a*b)
    k=(n+2)//3;B=1<<k
    a0,a1,a2=a%B,(a//B)%B,a//(B*B)
    b0,b1,b2=b%B,(b//B)%B,b//(B*B)
    c0=toom(a0,b0);c4=toom(a2,b2)
    v1=toom(a0+a1+a2,b0+b1+b2)
    vn=toom(a0-a1+a2,b0-b1+b2)
    v2=toom(a0+2*a1+4*a2,b0+2*b1+4*b2)
    assert (v1-vn)%2==0 and (v1+vn)%2==0
    u=(v1-vn)//2
    c2=(v1+vn)//2-c0-c4
    assert (v2-c0-16*c4)%2==0
    w=(v2-c0-16*c4)//2
    assert (w-u-2*c2)%3==0
    c3=(w-u-2*c2)//3;c1=u-c3
    assert min(c0,c1,c2,c3,c4)>=0
    return sign*(c0+B*c1+B**2*c2+B**3*c3+B**4*c4)

rng=random.Random(31337);product_cases=division_cases=permutation_cases=0
for bits in [0,1,2,16,31,32,33,64,127,128,255,256,512,1024,2048,4096]:
    vals=[0,1,(1<<bits)-1]+[rng.getrandbits(bits) for _ in range(12)]
    for i,a in enumerate(vals):
        b=vals[-1-i]
        for sa,sb in [(1,1),(-1,1),(1,-1),(-1,-1)]:
            assert toom(sa*a,sb*b)==sa*a*sb*b
            product_cases+=1
for t in range(1,11):
    for n in range(1,t+1):
        for modulus in sorted({max(2,1<<(n-1)),(1<<n)-1,1<<n}):
            if modulus<2:continue
            m=modulus.bit_length()-1
            for integer in range(1<<t):
                remainder=integer
                for j in reversed(range(max(0,t-m))):
                    threshold=modulus<<j
                    assert remainder<2*threshold
                    if remainder>=threshold:remainder-=threshold
                assert remainder==integer%modulus
                division_cases+=1
                if t<=7:
                    for x in sorted({0,modulus//2,modulus-1,modulus,min((1<<n)-1,modulus+1)}):
                        if x>=1<<n:continue
                        y=(x+remainder)%modulus if x<modulus else x
                        back=(y-remainder)%modulus if y<modulus else y
                        assert back==x
                        permutation_cases+=1
assert 5**2<3**3
out=dict(scope='Finite exact diagnostics, not a proof of asymptotics or quantum execution.',
         signed_toom3_product_cases=product_cases,recursive_calls=calls,
         restoring_division_cases=division_cases,variable_shift_inverse_cases=permutation_cases,
         toom3_rational_exponent_comparison=True)
Path(__file__).with_name('fast_arithmetic_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
