"""Exhaustive finite Boolean/reversible-arithmetic evidence for the DCP proof.
The circuit is materialized for diagnostics; the theorem uses its streamed loop
schedule. These tests do not establish the asymptotic theorem or an official score.
"""
from pathlib import Path
import json

ZERO, ONE = -1, -2

def ripple(a,b,w,cin=0):
    value,carry=0,cin
    for i in range(w):
        ai,bi=(a>>i)&1,(b>>i)&1
        p=ai^bi
        value|=(p^carry)<<i
        carry=(ai&bi)^(p&carry)
    return value,carry

class Circuit:
    def __init__(self,n):
        self.n=n; self.inputs=n+1; self.ops=[]; self.next=self.inputs
    def gate(self,kind,*args):
        out=self.next; self.next+=1; self.ops.append((kind,out,*args)); return out
    def inv(self,a):
        if a==ZERO:return ONE
        if a==ONE:return ZERO
        return self.gate('not',a)
    def xor(self,a,b):
        if a==b:return ZERO
        if a==ZERO:return b
        if b==ZERO:return a
        if a==ONE:return self.inv(b)
        if b==ONE:return self.inv(a)
        return self.gate('xor',a,b)
    def and_(self,a,b):
        if a==ZERO or b==ZERO:return ZERO
        if a==ONE:return b
        if b==ONE or a==b:return a
        return self.gate('and',a,b)
    def mux(self,k,a,b):return self.xor(b,self.and_(k,self.xor(a,b)))
    def add(self,a,b,carry=ZERO):
        out=[]
        for x,y in zip(a,b):
            p=self.xor(x,y)
            out.append(self.xor(p,carry))
            carry=self.xor(self.and_(x,y),self.and_(p,carry))
        return out,carry
    def sub(self,a,b):
        # Carry-in ONE is essential, including when the threshold is zero.
        return self.add(a,[self.inv(x) for x in b],ONE)
    def constant(self,value,w):return [ONE if (value>>i)&1 else ZERO for i in range(w)]
    def value(self,wire,v):return 0 if wire==ZERO else 1 if wire==ONE else v[wire]
    def oracle(self,x,control,target=0):
        v=[(x>>i)&1 for i in range(self.n)]+[control]+[0]*(self.next-self.inputs)
        def apply(op):
            kind,out,*args=op
            a=self.value(args[0],v)
            bit=1^a if kind=='not' else a^self.value(args[1],v) if kind=='xor' else a&self.value(args[1],v)
            v[out]^=bit
        for op in self.ops:apply(op)
        for i,out in enumerate(self.outputs):target^=self.value(out,v)<<i
        for op in reversed(self.ops):apply(op)
        assert not any(v[self.inputs:])
        assert v[:self.n]==[(x>>i)&1 for i in range(self.n)] and v[self.n]==control
        return target

def build(N,c,inverse):
    n=(N-1).bit_length(); w=n+2
    C=Circuit(n); x=list(range(n))+[ZERO]*(w-n); mod=C.constant(N,w); shift=C.constant(c,w)
    _,geN=C.sub(x,mod)
    active=C.and_(n,C.inv(geN))
    if inverse:
        diff,ge=C.sub(x,shift)
        alt,_=C.add(x,C.constant(N-c,w))
        raw=[C.mux(ge,a,b) for a,b in zip(diff,alt)]
    else:
        total,_=C.add(x,shift)
        reduced,ge=C.sub(total,mod)
        raw=[C.mux(ge,a,b) for a,b in zip(reduced,total)]
    C.outputs=[C.mux(active,raw[i],x[i]) for i in range(n)]
    assert len(C.ops)<100*w
    return C

def main():
    comparator_cases=0
    for w in range(2,9):
        mask=(1<<w)-1
        for x in range(1<<w):
            for threshold in range(1<<w):
                result,carry=ripple(x,mask^threshold,w,1)
                assert carry==int(x>=threshold)
                assert result==(x-threshold)&mask
                comparator_cases+=1
    old=ripple(0,0,4,0)[1]
    fixed=ripple(0,15,4,1)[1]
    assert old==0 and fixed==1
    basis_cases=0; max_ops=0; max_wires=0
    for N in range(2,34):
        n=(N-1).bit_length()
        for c in range(N):
            forward,inverse=build(N,c,False),build(N,c,True)
            max_ops=max(max_ops,len(forward.ops),len(inverse.ops))
            max_wires=max(max_wires,forward.next,inverse.next)
            for control in (0,1):
                image=[]
                for x in range(1<<n):
                    actual=forward.oracle(x,control)
                    expected=(x+c)%N if control and x<N else x
                    assert actual==expected
                    assert inverse.oracle(actual,control)==x
                    # Compute f into clean Y; swap; inverse-XOR clears old X.
                    assert inverse.oracle(actual,control,x)==0
                    image.append(actual); basis_cases+=1
                assert len(set(image))==1<<n
    phase_cases=0
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                rhs=a+b+c-(a^b)-(a^c)-(b^c)+(a^b^c)
                assert rhs==4*a*b*c
                phase_cases+=1
    result={'scope':'Finite exhaustive arithmetic evidence only; no official mathematical review.',
            'comparator_cases':comparator_cases,'controlled_permutation_basis_cases':basis_cases,
            'maximum_materialized_boolean_operations':max_ops,'maximum_materialized_wires':max_wires,
            'Toffoli_parity_phase_assignments':phase_cases,
            'zero_threshold_regression':{'old_carry':old,'required':1,'repaired_carry':fixed}}
    Path(__file__).with_name('arithmetic_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
