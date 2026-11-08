"""Exact sparse reference for emitted X/CNOT/Toffoli/Z/CZ/H circuits."""
from fractions import Fraction as F
from exact import Exact


def boolean_code(gates):
    out=[]
    for op,*w in gates:
        assert len(set(w))==len(w)
        if op in ('Z','CZ'):out.append((sum(1<<x for x in w),0,True))
        else:
            assert op in ('X','CX','CCX')
            out.append((sum(1<<x for x in w[:-1]),1<<w[-1],False))
    return out


def apply_boolean(state,code):
    out={}
    for basis,amp in state.items():
        sign=1
        for controls,target,phase in code:
            if basis&controls==controls:
                if phase:sign=-sign
                else:basis^=target
        out[basis]=out.get(basis,Exact())+amp*sign
    return {b:a for b,a in out.items() if a}


def hadamard(state,wire):
    out={};mask=1<<wire;scale=Exact.sqrt(F(1,2))
    for basis,amp in state.items():
        low=basis&~mask;high=low|mask
        out[low]=out.get(low,Exact())+amp*scale
        out[high]=out.get(high,Exact())+amp*scale*(-1 if basis&mask else 1)
    return {b:a for b,a in out.items() if a}


def compile_parts(gates):
    parts=[];pending=[]
    for gate in gates:
        if gate[0]=='H':
            if pending:parts.append(('B',boolean_code(pending)));pending=[]
            parts.append(('H',gate[1]))
        else:pending.append(gate)
    if pending:parts.append(('B',boolean_code(pending)))
    return parts


def apply(state,parts):
    for kind,value in parts:
        state=hadamard(state,value) if kind=='H' else apply_boolean(state,value)
    return state
