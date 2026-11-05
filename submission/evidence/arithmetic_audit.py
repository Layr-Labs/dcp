"""Finite exact properties for elementary three-product/reduction circuits."""
from pathlib import Path
import json,random

def product_unsigned(x,y,width):
    if width==1:return x&y
    m=width//2;mask=(1<<m)-1
    x0=x&mask;x1=x>>m;y0=y&mask;y1=y>>m
    z0=product_unsigned(x0,y0,m);z2=product_unsigned(x1,y1,m)
    aa=x1-x0;bb=y0-y1
    zd=product_unsigned(abs(aa),abs(bb),m)
    if (aa<0)!=(bb<0):zd=-zd
    return z0+((z0+z2+zd)<<m)+(z2<<(2*m))

def multiply(x,y):
    width=1<<max(0,(max(x.bit_length(),y.bit_length())-1).bit_length())
    return product_unsigned(x,y,width)

def reduce_value(u,N,v):
    n=(N-1).bit_length();W=v+n+2;mu=(1<<W)//N
    q=multiply(u,mu)>>W;r=u-multiply(q,N)
    assert 0<=r<2*N
    return r-N if r>=N else r

def translate(k,x,N,t,inverse=False):
    if x>=N:return x
    if inverse:
        kk=reduce_value(k,N,t+1)
        return x-kk if x>=kk else x+N-kk
    return reduce_value(x+k,N,t+1)

def main():
    products=0
    for x in range(256):
        for y in range(256):
            assert multiply(x,y)==x*y;products+=1
    rng=random.Random(121314)
    for width in [9,15,16,17,31,32,33,63,64,65,127,128,129,255,256,257,511,512,1024,2048]:
        for _ in range(20):
            x=rng.getrandbits(width);y=rng.getrandbits(width)
            assert multiply(x,y)==x*y;products+=1
    perms=0
    for N in range(2,34):
        n=(N-1).bit_length();t=n+2
        for k in range(1<<t):
            values=[]
            for x in range(1<<n):
                y=translate(k,x,N,t)
                assert y==((x+k)%N if x<N else x)
                assert translate(k,y,N,t,True)==x
                values.append(y);perms+=1
            assert sorted(values)==list(range(1<<n))
    grouped=0
    for t in range(1,10):
        for B in range(1,t+1):
            for x in range(1<<t):
                for j in range(t):
                    d=sum(((x>>k)&1)<<(B-j+k-1) for k in range(max(0,j-B+1),j))
                    scalar=sum(((x>>k)&1)*(1<<(B-(j-k+1))) for k in range(j) if j-k+1<=B)
                    assert d==scalar;grouped+=1
    assert 3**5<2**8
    out=dict(scope='Finite exact multiplication, inverse-permutation and grouped-phase properties; no asymptotic proof or device execution.',three_product_cases=products,source_basis_permutation_cases=perms,grouped_phase_exponents=grouped)
    Path(__file__).with_name('arithmetic_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
