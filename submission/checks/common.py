"""Exact F4 parameters and certificates. No asymptotic-width exponentiation."""
from fractions import Fraction as F
from math import isqrt
from functools import lru_cache

def clog(x):
    assert x >= 1
    return (x - 1).bit_length()

def arity(b):
    assert b >= 1
    target = b + clog(b + 1) + 6
    return min(4 * max(1, (target - 2*r + 6)//7) + r for r in range(4))

def parameters(b):
    f = arity(b)
    k = f//4
    q = 2*f-k
    c = clog(b+1)
    u = clog(q+2)
    t = max(0, (k//(16*u)).bit_length()-1)
    return f, k, q, c, u, t

def decrement(b, old=False):
    v = b + clog(b+1) + 6 if old else arity(b) + 1
    return clog(v*v)

def profile(B, old=False):
    U = isqrt(B-1)+1
    v = B
    seq = []
    while v >= U:
        seq.append(v)
        v -= decrement(v, old)
    return tuple(reversed(seq))

def choose(n, old=False):
    for B in range(1, n+1):
        seq = profile(B, old)
        if sum(seq) >= n:
            return B, seq
    raise AssertionError('The top width n must be feasible')

def widths(D, seq):
    remaining = D-1
    bs = []
    for v in reversed(seq):
        b = min(remaining, v)
        bs.append(b)
        remaining -= b
    assert remaining == 0
    return tuple(reversed(bs))

@lru_cache(maxsize=32768)
def local(n, b, old=False):
    assert 1 <= b <= 100000, 'Only bounded exact diagnostics may exponentiate'
    if old:
        q = b + clog(b+1) + 4
        f = q
        c = clog(b+1)
        u = clog(q+2)
        t = max(0, (q//(16*u)).bit_length()-1)
        R = 8*c+4
        h = F(256 * (1 << ((b+1)//2-t//2)))
        if t:
            h += F((R+2)*(1 << ((q+1)//2))*u, (q+2)**16)
        sigma = F(2*b+1, 2*b+2)
        w = 64*(n+1)
    else:
        f,k,q,c,u,t = parameters(b)
        R = 8*c+16
        h = F(512 * (1 << ((b+1)//2-t//2)))
        if t:
            h += F(3*(R+2)*(1 << ((q+1)//2))*u, (q+2)**16)
        sigma = F(8*b+7, 8*b+8)
        w = 1024*(n+1)
    s = q*(w+b+1)+w
    z = q*(b+1)+w
    return F(f, 1)/sigma, (2*s+z*h)/sigma

def cert(n, D, seq, old=False):
    e = F(1 if old else 2)
    v = F(0)
    for b in widths(D, seq):
        if b:
            factor, add = local(n, b, old)
            e *= factor
            v = factor*v+add
    return e, v

def all_d(n, seq, old=False):
    em = F(0)
    vm = F(0)
    ed = vd = 0
    for D in range(1, n+1):
        e,v = cert(n,D,seq,old)
        if e > em:
            em,ed = e,D
        if v > vm:
            vm,vd = v,D
    q0 = 1 if old else 2
    for b in seq:
        q0 *= b+clog(b+1)+4 if old else arity(b)
    K = 8192*(clog(q0)+clog(n)+30)
    H0 = n*K+2*n
    qs = 2*em*H0+2*n
    vs = vm*H0
    qc = (1024*qs.numerator+qs.denominator-1)//qs.denominator
    vc = (1024*vs.numerator+vs.denominator-1)//vs.denominator
    work = clog(n+2)**2*(vc+n**3*qc+n**4*q0+n**6)
    return dict(E=em,V=vm,E_argmax=ed,V_argmax=vd,q0=q0,K=K,Qcap=qc,Vcap=vc,F=work)

def flog(x):
    x = F(x)
    assert x > 0
    k = x.numerator.bit_length()-x.denominator.bit_length()
    if k >= 0:
        if x.numerator < x.denominator << k:
            k -= 1
    elif x.numerator << (-k) < x.denominator:
        k -= 1
    return k
