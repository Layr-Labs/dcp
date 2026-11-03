"""Bounded sample-tolerance-v1 monomial grammar; mirrors the Yukon consumer.

This validates symbolic counts without executing TeX, guessing constants, or
computing a score. The consumer orders min(Q, floor(c Q^q n^a log_2(n)^b)).
"""
import re
from fractions import Fraction as F

ZERO, ONE = F(0), F(1)


def _checked(value):
    if len(str(abs(value.numerator))) > 256 or len(str(value.denominator)) > 256:
        raise ValueError("rational limit")
    return value


def _unit(c=ONE):
    return [c, ZERO, ZERO, ZERO]


def _product(a, b, divide=False):
    sign = -1 if divide else 1
    return [_checked(a[0] / b[0] if divide else a[0] * b[0]),
            *[_checked(x + sign*y) for x, y in zip(a[1:], b[1:])]]


class _Parser:
    def __init__(self, expression):
        if type(expression) is not str or len(expression) > 2048 or re.search(r"[\x00-\x08\x0b-\x1f]", expression):
            raise ValueError("expression limit")
        source = re.sub(r"\\(?:left|right)(?![A-Za-z])", "", expression.strip(" \t\n"))
        if source.startswith(r"\lfloor") and source.endswith(r"\rfloor"):
            source = source[7:-7]
        source = re.sub(r"\\log_(?:2|\{2\})[ \t\n]*(?:\{n\}|\(n\)|n(?![A-Za-z0-9^]))(?!\^)", "L", source)
        source = re.sub(r"\\(?:cdot|times)(?![A-Za-z])", "*", source)
        source = re.sub(r"\\[,!; ]", "", source)
        source = re.sub(r"[ \t\n]", "", source)
        self.tokens = re.findall(r"\\frac|\d+|[QnL{}()*/^+-]", source, re.ASCII)
        if ("".join(self.tokens) != source or not self.tokens or len(self.tokens) > 128
                or any(t.isdigit() and len(t) > 64 for t in self.tokens)):
            raise ValueError("token limit")
        self.at, self.depth = 0, 0

    def peek(self, offset=0):
        return self.tokens[self.at+offset] if self.at+offset < len(self.tokens) else None

    def take(self):
        token = self.peek()
        if token is None:
            raise ValueError("missing token")
        self.at += 1
        return token

    def group(self):
        opening = self.take()
        self.depth += 1
        if opening not in ("{", "(") or self.depth > 12:
            raise ValueError("group limit")
        value = self.expression()
        if self.take() != ("}" if opening == "{" else ")"):
            raise ValueError("unclosed group")
        self.depth -= 1
        return value

    def exponent(self, allow_fraction=False):
        opening = self.peek()
        if opening in ("{", "("):
            self.take()
            self.depth += 1
            if self.depth > 12:
                raise ValueError("group limit")
            value = self.exponent(True)
            if self.take() != ("}" if opening == "{" else ")"):
                raise ValueError("unclosed exponent")
            self.depth -= 1
            return value
        if not allow_fraction and self.peek() == "-":
            raise ValueError("group the exponent")
        sign = -1 if self.peek() == "-" else 1
        if sign == -1:
            self.take()
        if self.peek() == r"\frac":
            self.take()
            a, b = self.group(), self.group()
            if any(a[1:] + b[1:]):
                raise ValueError("non-rational exponent")
            return _checked(sign * a[0] / b[0])
        numerator = self.take()
        if not numerator.isascii() or not numerator.isdigit() or (not allow_fraction and len(numerator) != 1):
            raise ValueError("non-rational exponent")
        denominator = "1"
        if (allow_fraction and self.peek() == "/" and (self.peek(1) or "").isdigit()
                and self.peek(2) in ("}", ")")):
            self.take()
            denominator = self.take()
        return _checked(F(sign*int(numerator), int(denominator)))

    def factor(self):
        token = self.peek()
        if token in ("{", "("):
            value = self.group()
        elif token == r"\frac":
            self.take()
            value = _product(self.group(), self.group(), True)
        elif token and token.isascii() and token.isdigit():
            self.take()
            value = _unit(F(int(token)))
        elif token in ("Q", "n", "L"):
            self.take()
            value = _unit()
            value[{"Q": 1, "n": 2, "L": 3}[token]] = ONE
        else:
            raise ValueError("unsupported atom")
        if self.peek() == "^":
            self.take()
            power = self.exponent()
            if value[0] != ONE:
                if (power.denominator != 1 or abs(power) > 16
                        or (value[0] == ZERO and power <= ZERO)):
                    raise ValueError("unsupported coefficient power")
                value[0] = _checked(value[0] ** int(power))
            value = [value[0], *[_checked(x*power) for x in value[1:]]]
        return value

    def implicit_product(self):
        value = self.factor()
        while self.peek() not in (None, "}", ")", "*", "/"):
            value = _product(value, self.factor())
        return value

    def expression(self):
        # Juxtaposition binds before left-associative explicit * and /.
        value = self.implicit_product()
        while self.peek() in ("*", "/"):
            divide = self.take() == "/"
            value = _product(value, self.implicit_product(), divide)
        return value

    def read(self):
        value = self.expression()
        if self.at != len(self.tokens) or value[1] not in (ZERO, ONE):
            raise ValueError("unsupported sample power")
        return value


def parse_tolerance_expression(expression):
    """Return a canonical symbolic form or raise ValueError; never rewrite input."""
    try:
        c, q, n, log = _Parser(expression).read()
        power = (n > 0)-(n < 0) or (log > 0)-(log < 0)
        if c == 0 or (q == 0 and power < 0):
            kind, (c, q, n, log) = "zero", _unit(ZERO)
        elif q == 1 and (power > 0 or (power == 0 and c >= 1)):
            kind, (c, q, n, log) = "full", [ONE, ONE, ZERO, ZERO]
        elif q == 0 and power == 0:
            c = F(c.numerator // c.denominator)
            kind = "zero" if c == 0 else "constant"
        else:
            kind = "count" if q == 0 else "rate"
        return dict(kind=kind, coefficient=str(c), samplePower=str(q), nPower=str(n), logPower=str(log))
    except (ValueError, ZeroDivisionError, OverflowError, RecursionError) as error:
        raise ValueError("sample-tolerance-v1: unsupported count expression") from error
