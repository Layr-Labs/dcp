"""Numerical FFT/Hadamard reference, inherited from PFD-15. Not a free circuit oracle."""
import cmath
import math

def fourier(values, sign):
    size = len(values)
    assert size and size & (size-1) == 0 and sign in (-1, 1)
    out = list(values)
    j = 0
    for i in range(1, size):
        bit = size >> 1
        while j & bit:
            j ^= bit; bit >>= 1
        j ^= bit
        if i < j: out[i], out[j] = out[j], out[i]
    length = 2
    while length <= size:
        step = cmath.exp(sign * 2j * math.pi / length)
        for start in range(0, size, length):
            w = 1+0j
            for k in range(length//2):
                a, b = out[start+k], w*out[start+k+length//2]
                out[start+k], out[start+k+length//2] = a+b, a-b
                w *= step
        length *= 2
    scale = math.sqrt(size)
    return [v/scale for v in out]


def hadamards(values):
    out = list(values); step = 1
    while step < len(out):
        for start in range(0, len(out), 2*step):
            for j in range(step):
                a, b = out[start+j], out[start+j+step]
                out[start+j], out[start+j+step] = a+b, a-b
        step *= 2
    return [v/math.sqrt(len(out)) for v in out]


