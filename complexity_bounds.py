"""Exact validation of explicit reviewed bounds; never parse claim prose.

The wire contract is shared with Yukon's asymptotic-v1 comparator. This module
normalizes only declared rational data and derives its coarse growth index.
Mathematical validity and the link to the algorithm remain review obligations.
"""

from fractions import Fraction
import re

from llm_verifier.errors import VerifierError

LEGACY_CONTRACT = {
    "version": "dcp-bounds-v3",
    "comparator": "asymptotic-v1",
    "scope": "dcp-cyclic-group-order",
    "model": "dcp-uniform-clifford-t-bit-operations-v1",
    "notation": "big-o",
}
CONTRACT = {**LEGACY_CONTRACT, "version": "dcp-bounds-v4"}
LEGACY_RESOURCES = ("time", "classical_space", "quantum_space")
RESOURCES = (*LEGACY_RESOURCES, "samples")


def resource_contract(review_standard):
    if review_standard in ("dcp-joint-bounds-v4", "dcp-joint-bounds-v5", "dcp-joint-bounds-v6"):
        return RESOURCES, CONTRACT
    if review_standard in ("dcp-joint-bounds-v2", "dcp-joint-bounds-v3"):
        return LEGACY_RESOURCES, LEGACY_CONTRACT
    raise VerifierError("dcp_bound_contract")


MAX_DIGITS = 256
MAX_TERMS = 64


def exact_keys(value, expected):
    if type(value) is not dict or set(value) != set(expected):
        raise VerifierError("dcp_bound_keys")


def rational(value):
    if type(value) is not str or len(value) > MAX_DIGITS * 2 + 2:
        raise VerifierError("dcp_bound_rational")
    match = re.fullmatch(r"(-?[0-9]+)(?:/([0-9]+))?", value)
    if (not match or len(match[1].lstrip("-")) > MAX_DIGITS
            or len(match[2] or "1") > MAX_DIGITS or int(match[2] or "1") == 0):
        raise VerifierError("dcp_bound_rational")
    return Fraction(int(match[1]), int(match[2] or "1"))


def rational_text(value):
    # Bound conversion before str(): malicious coprime denominators can create
    # an intermediate larger than Python's integer-to-decimal safety limit.
    if value.numerator.bit_length() > 851 or value.denominator.bit_length() > 851:
        raise VerifierError("dcp_bound_normalized_size")
    if (len(str(abs(value.numerator))) > MAX_DIGITS
            or len(str(value.denominator)) > MAX_DIGITS):
        raise VerifierError("dcp_bound_normalized_size")
    return str(value)


def normalize_bound(value):
    exact_keys(value, ("coefficient", "exponent", "nPower", "logPower"))
    if rational(value["coefficient"]) <= 0:
        raise VerifierError("dcp_bound_positive_coefficient")
    n_power, log_power = rational(value["nPower"]), rational(value["logPower"])
    if type(value["exponent"]) is not list or len(value["exponent"]) > MAX_TERMS:
        raise VerifierError("dcp_bound_terms")
    terms = {}
    for term in value["exponent"]:
        exact_keys(term, ("coefficient", "nPower", "logPower"))
        a, p, q = (rational(term[key]) for key in ("coefficient", "nPower", "logPower"))
        if p < 0 or (p == 0 and q <= 0):
            raise VerifierError("dcp_bound_unsupported_power")
        if (p, q) == (0, 1):
            n_power += a
        else:
            terms[p, q] = terms.get((p, q), Fraction(0)) + a
    return {
        # All DCP guarantees are O(B): outer constants do not distinguish bounds.
        "coefficient": "1",
        "exponent": [
            {"coefficient": rational_text(a), "nPower": rational_text(p),
             "logPower": rational_text(q)}
            for (p, q), a in sorted(terms.items(), reverse=True) if a
        ],
        "nPower": rational_text(n_power),
        "logPower": rational_text(log_power),
    }


def growth_index(bound):
    """g(B), including cancellation and envelopes tending to zero."""
    growth = [(rational(t["nPower"]), rational(t["logPower"]),
               rational(t["coefficient"])) for t in bound["exponent"]]
    n_power = rational(bound["nPower"])
    if n_power:
        growth.append((Fraction(0), Fraction(1), n_power))
    if growth:
        p, _q, a = max(growth)
        if a > 0:
            return p
    return Fraction(0)


def reviewed_bound(structured, score, *, contract=CONTRACT):
    exact_keys(structured, (*contract, "bound"))
    if any(structured[key] != value for key, value in contract.items()):
        raise VerifierError("dcp_bound_contract")
    normalized = normalize_bound(structured["bound"])
    if (type(score) is not dict or set(score) != {"numerator", "denominator"}
            or growth_index(normalized) != Fraction(
                int(score["numerator"]), int(score["denominator"]))):
        raise VerifierError("dcp_bound_growth_index_mismatch")
    return normalized
