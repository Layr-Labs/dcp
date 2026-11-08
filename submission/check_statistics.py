"""Exact moments, parity restriction, interval certificates and all small ensembles."""
from collections import Counter
from fractions import Fraction as F
import itertools,json,math,resource
from walk import parameters


def interval_root(k, scale=1 << 48):
    v=math.isqrt(k*scale*scale)
    return F(v,scale),F(v+1,scale)


def main():
    resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20));resource.setrlimit(resource.RLIMIT_CPU,(45,45))
    lo2,hi2=interval_root(2);lo3,hi3=interval_root(3)
    c_lo=3*(1+lo2)/4-hi3;c_hi=3*(1+hi2)/4-lo3
    lower=(1+lo2+4*lo3)**2/128;upper=(1+hi2+4*hi3)**2/128
    assert c_lo>0 and lower>F(87,128) and upper<F(11,16)
    assert (14-9*hi2)/5>0
    # The factorization proves all k; these certify the exceptional small cases.
    from exact import Exact
    r2,r3=Exact.sqrt(2),Exact.sqrt(3)
    a=r2-F(1,2);b=(r2-1)*F(1,4);c=(1+r2)*F(3,4)-r3
    for k in (0,2,3,4):assert Exact.sqrt(k)==a*k-b*k*k-c*(k%2)
    for k in (1,5,6,7,8):
        rootlo,_=interval_root(k)
        assert rootlo >= (hi2-F(1,2))*k - ((lo2-1)/4)*k*k - c_lo*(k%2)
    assert 9*(lo2-1)/4 > hi2-F(1,2)
    rows=[];total_lists=base_lists=0
    for N in range(2,9):
        n=(N-1).bit_length();m=n+1;K=1<<m;H=1<<n;lam=F(H,N)
        sx2=ss=ss2=odd=0
        for labels in itertools.product(range(N),repeat=n):
            sums=[0]
            for a0 in labels:sums += [(v+a0)%N for v in sums]
            xi=[sums.count(t) for t in range(N)]
            assert sum(xi)==H
            conditional_odd=sum((xi[t]+xi[(t-A)%N])%2 for t,A in itertools.product(range(N),repeat=2))
            assert 2*conditional_odd<=N*N
            sx2+=sum(x*x for x in xi);base_lists+=1
            for A in range(N):
                eta=[xi[t]+xi[(t-A)%N] for t in range(N)]
                ss+=sum(eta);ss2+=sum(x*x for x in eta);odd+=sum(x%2 for x in eta)
        assert F(sx2,N**(n+1))==lam*lam+lam-lam/N
        assert F(ss,N**(m+1))==2*lam
        assert F(ss2,N**(m+1))==4*lam*lam+2*lam-2*lam/N
        assert F(odd,N**(m+1))<=F(1,2)
        scale=1<<32;sum_lower=0;profiles=Counter()
        for labels in itertools.product(range(N),repeat=m):
            sums=[0]
            for a0 in labels:sums += [(v+a0)%N for v in sums]
            profile=tuple(sorted(Counter(sums).values()));profiles[profile]+=1
        for profile,freq in profiles.items():
            root_sum=sum(math.isqrt(x*scale*scale) for x in profile)
            sum_lower+=freq*root_sum*root_sum
        bound=F(sum_lower,N**m*N*K*scale*scale)
        assert bound>=upper
        total_lists+=N**m
        rows.append({'N':N,'m':m,'label_lists':N**m,'ideal_success_certified_lower':str(bound),
                     'mean_odd_occupancy':str(F(odd,N**(m+1)))})
    filter_square=F(4,(1<<23)-1)
    assert filter_square<F(1,512**2)
    for n in range(1,1025):
        for N in (1<<n,(1<<(n-1))+1):
            p=parameters(N);m=p['m'];M=1<<p['q_lab']
            assert M>=2048*m*N and F(1,M//(2*N)-1)<=F(1,512*m)
            assert 2*p['p']>=m+52
            assert 2*((1<<p['p'])-1)>0
    assert lower-F(1,128)>F(43,64)>F(2,3)
    print(json.dumps({'passed':True,'complete_label_lists':total_lists,'conditional_base_histograms':base_lists,
                      'ensembles':rows,'Cstar_interval':[str(lower),str(upper)],
                      'implemented_success_lower':str(lower-F(1,128)),
                      'rational_success_claim':'43/64','walk_error_squared_upper':str(filter_square),
                      'parameter_bit_lengths':1024,'scope':'Exact rational certificates; no production-size PE simulation.'},indent=2))


if __name__=='__main__':main()
