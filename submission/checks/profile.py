"""Exact profile/certificate definitions. Import without writing bytecode."""
from fractions import Fraction as F
from math import isqrt

def ceil_log(x):
    assert x >= 1
    return (x-1).bit_length()

def q(b):
    assert b >= 1
    return b+b.bit_length()+4

def sigma(b):
    return F(2*b+1,2*b+2)

def drop(b, kind='critical-sqrt'):
    if kind == 'inherited-quarter':
        return 2*ceil_log(3*(b+1))
    return ceil_log((q(b)+2)**2)+(2 if kind == 'half-geometric-quarter' else 0)

def base(B,kind):
    if kind == 'critical-sqrt':
        return isqrt(B-1)+1
    if kind == 'inherited-quarter':
        return 2*max(1,B//8)
    return max(2,B//4)

def profile(B,kind='critical-sqrt'):
    u=base(B,kind)
    bs=[]
    while B>=u:
        bs.append(B)
        B-=drop(B,kind)
    return bs[::-1]

def choose(n,kind='critical-sqrt'):
    # Do not assume capacity is monotone or use a float to choose a starting point.
    step=2 if kind=='inherited-quarter' else 1
    start=1 if kind=='critical-sqrt' else 2
    for B in range(start,n+step,step):
        bs=profile(B,kind)
        if sum(bs)>=n:
            return B,bs
    raise AssertionError('finite sequential search')

def widths(nominal,D):
    rest=D-1
    bs=[]
    for v in reversed(nominal):
        b=min(v,rest)
        bs.append(b)
        rest-=b
    assert rest==0
    return bs[::-1]

def params(b):
    c=b.bit_length();a=q(b);r=8*c+4;u=ceil_log(a+2)
    t=max(0,(a//(16*u)).bit_length()-1)
    return a,r,u,t

def hbound(b):
    a,r,u,t=params(b)
    return F(256*(1<<((b+1)//2-t//2)))+(F((r+2)*(1<<((a+1)//2))*u,(a+2)**16) if t else 0)

def budget(n,nominal,D):
    e=F(1);v=F(0);w=64*(n+1)
    for b in widths(nominal,D):
        if not b:continue
        a=q(b);s=a*(w+b+1)+w;z=a*(b+1)+w
        e=a*e/sigma(b)
        v=(a*v+2*s+z*hbound(b))/sigma(b)
    return e,v

def caps(n,nominal,Ds):
    em=F(1);vm=F(0);q0=1
    for v in nominal:q0*=q(v)
    for D in Ds:
        e,v=budget(n,nominal,D)
        em=max(em,e);vm=max(vm,v)
    k0=ceil_log(q0);K=8192*(k0+ceil_log(n)+30);H0=n*K+2*n
    qc=(1024*(2*em*H0+2*n)).__ceil__();vc=(1024*vm*H0).__ceil__()
    return dict(E=em,V=vm,q0=q0,k0=k0,K=K,H0=H0,Qcap=qc,Vcap=vc)

def exact_ratio(x):
    return {'numerator':str(x.numerator),'denominator':str(x.denominator)}

def floor_log_ratio(x):
    assert x>0
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if e>=0:
        if x.numerator<(x.denominator<<e):e-=1
    elif (x.numerator<<(-e))<x.denominator:e-=1
    return e
