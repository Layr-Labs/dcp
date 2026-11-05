"""Reviewed fractional tolerance, with historical count contracts preserved."""
from llm_verifier.errors import VerifierError

CLAIM_INDEX = 4
REVIEW_STANDARD = "dcp-joint-bounds-v7"
COUNT_STANDARD = "dcp-joint-bounds-v6"
PREVIOUS_TOLERANCE_STANDARD = "dcp-joint-bounds-v5"
STRUCTURED_VERSION = "dcp-fractional-error-tolerance-v1"
METRICS_VERSION = "reviewed-fraction-v1"


def metrics_version(standard):
    return METRICS_VERSION if standard == REVIEW_STANDARD else "reviewed-expression-v1"


def tolerance_required(standard):
    return standard in (REVIEW_STANDARD, COUNT_STANDARD, PREVIOUS_TOLERANCE_STANDARD)


def reviewed_tolerance(manifest, *, standard=REVIEW_STANDARD):
    claims = manifest.get("claims") if type(manifest) is dict else None
    if type(claims) is not list or len(claims) <= CLAIM_INDEX or type(claims[CLAIM_INDEX]) is not dict:
        raise VerifierError("dcp_tolerance_claim_required")
    claim = claims[CLAIM_INDEX]
    if "score" in claim:
        raise VerifierError("dcp_tolerance_has_no_score")
    value = claim.get("structured")
    if type(value) is not dict or set(value) != {"version", "expression", "error_model"}:
        raise VerifierError("dcp_tolerance_expression_required")
    expected_version = STRUCTURED_VERSION if standard == REVIEW_STANDARD else "dcp-error-tolerance-v1"
    if value["version"] != expected_version:
        raise VerifierError("dcp_tolerance_contract")
    for key, maximum in (("expression", 2048), ("error_model", 4000)):
        text = value[key]
        if (type(text) is not str or not text.strip()
                or len(text.encode("utf-16-le")) // 2 > maximum
                or any(ord(c) < 32 and c not in "\n\t" for c in text)):
            raise VerifierError("dcp_tolerance_text")
    if standard in (REVIEW_STANDARD, COUNT_STANDARD):
        from tolerance_expression import parse_tolerance_expression, parse_fractional_tolerance_expression
        parse = parse_fractional_tolerance_expression if standard == REVIEW_STANDARD else parse_tolerance_expression
        try:
            parse(value["expression"])
        except ValueError:
            raise VerifierError("dcp_tolerance_comparison_expression") from None
    return {"expression": value["expression"], "context": value["error_model"]}
