"""Small exact multiquadratic field with i, for finite circuit diagnostics."""
from fractions import Fraction as F
from math import gcd


class Exact:
    def __init__(self, value=0, terms=None):
        self.t = {k: F(v) for k, v in (terms or {(1, 0): value}).items() if v}

    def __add__(self, other):
        other = other if isinstance(other, Exact) else Exact(other)
        out = dict(self.t)
        for k, v in other.t.items():
            out[k] = out.get(k, F(0)) + v
        return Exact(terms=out)

    __radd__ = __add__

    def __neg__(self):
        return Exact(terms={k: -v for k, v in self.t.items()})

    def __sub__(self, other):
        return self + -other if isinstance(other, Exact) else self + Exact(-other)

    def __mul__(self, other):
        other = other if isinstance(other, Exact) else Exact(other)
        out = {}
        for (a, i), v in self.t.items():
            for (b, j), w in other.t.items():
                g = gcd(a, b)
                key = (a * b // (g * g), (i + j) % 2)
                out[key] = out.get(key, F(0)) + v * w * g * (-1 if i + j == 2 else 1)
        return Exact(terms=out)

    __rmul__ = __mul__

    def __eq__(self, other):
        other = other if isinstance(other, Exact) else Exact(other)
        return self.t == other.t

    def __bool__(self):
        return bool(self.t)

    def conjugate(self):
        return Exact(terms={(d, i): v * (-1 if i else 1) for (d, i), v in self.t.items()})

    def squared(self):
        return self.conjugate() * self

    def data(self):
        return [dict(radicand=d, imaginary=bool(i), coefficient=str(v))
                for (d, i), v in sorted(self.t.items())]

    @staticmethod
    def sqrt(value):
        value = F(value)
        assert value >= 0
        if not value:
            return Exact()
        n = value.numerator * value.denominator
        factor, outside, inside = 2, 1, 1
        while factor * factor <= n:
            power = 0
            while n % factor == 0:
                n //= factor
                power += 1
            outside *= factor ** (power // 2)
            if power % 2:
                inside *= factor
            factor += 1
        inside *= n
        return Exact(terms={(inside, 0): F(outside, value.denominator)})

    @staticmethod
    def phase8(power):
        z = Exact(terms={(2, 0): F(1, 2), (2, 1): F(1, 2)})
        out = Exact(1)
        for _ in range(power % 8):
            out = out * z
        return out
