"""Small state-vector simulation of the explicit Grover phase filter.

Uses floating-point complex arithmetic. Production correctness uses the
analytic tail bound in GROVER_FIBER.md, not numerical extrapolation.
"""
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


def grover_filter(population, size, grid, initial, inverse=False, wrong_sign=False):
    p = population / size
    c, s = 1-2*p, 2*math.sqrt(p*(1-p))
    if wrong_sign: c, s = -c, -s
    vectors = [[], []]
    a, b = initial
    for j in range(grid):
        vectors[0].append(a/math.sqrt(grid)); vectors[1].append(b/math.sqrt(grid))
        a, b = c*a+s*b, -s*a+c*b
    vectors = [fourier(v, -1) for v in vectors]
    for j in range(grid):
        phase = 1j*cmath.exp(-1j*math.pi*j/grid)
        if inverse: phase = phase.conjugate()
        for v in vectors: v[j] *= phase
    vectors = [fourier(v, 1) for v in vectors]
    cj, sj = 1.0, 0.0
    for j in range(grid):
        a, b = vectors[0][j], vectors[1][j]
        vectors[0][j], vectors[1][j] = cj*a-sj*b, sj*a+cj*b
        cj, sj = cj*c-sj*s, sj*c+cj*s
    return [hadamards(v) for v in vectors]


def estimation_probability(alpha, grid, j):
    distance = (alpha-j/grid+.5) % 1 - .5
    if abs(distance) < 1e-14: return 1.0
    return (math.sin(math.pi*grid*distance)/(grid*math.sin(math.pi*distance)))**2


def spectral_error(population, size, grid):
    theta = math.asin(math.sqrt(population/size))
    angles = [theta/math.pi, 1-theta/math.pi]
    total = 0.0
    for alpha in angles:
        wanted = 1j*cmath.exp(-1j*math.pi*alpha)
        total += sum(estimation_probability(alpha, grid, j)
                     * abs(1j*cmath.exp(-1j*math.pi*j/grid)-wanted)**2
                     for j in range(grid))/2
    return total
