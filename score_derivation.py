"""DCP metrics from separately reviewed, authenticated retained full claims.

The generic verifier authenticates original artifacts and the new derivation.
This adapter preserves resource bounds, the time score and corruption assumptions;
only an exactly equivalent supported count-to-fraction representation may change.
"""

from copy import deepcopy
from fractions import Fraction
import re

from llm_verifier.errors import VerifierError
from llm_verifier.jsonutil import digest
from llm_verifier.scoring import score_value

from complexity_bounds import CONTRACT, RESOURCES, reviewed_bound
from error_tolerance import COUNT_STANDARD, REVIEW_STANDARD, reviewed_tolerance
from tolerance_expression import (
    parse_exact_tolerance_monomial,
    parse_fractional_tolerance_expression,
)

VERSION = "dcp-score-derivation-v1"
SCORING_POLICY = {
    "version": "dcp-time-growth-fraction-v3",
    "retained_result": "yukon-retained-result-v1",
}
RETAINED_VALIDITY = {"version": COUNT_STANDARD, "structured_bounds": "required"}
VERIFIER_REVISION = "da594aad5166918d4dd7d71630e1e649521e1953"


def fraction_from_count(expression):
    """Exact supported rate representation; never substitute a sample upper bound."""
    c, q, n, log = parse_exact_tolerance_monomial(expression)
    if c == 0 or (q == 0 and n == 0 and log == 0 and c < 1):
        return "0"
    if q != 1:
        return None
    text = "(" + str(c) + ")"
    for symbol, power in (("n", n), ("L", log)):
        if power:
            text += "*" + symbol + "^{" + str(power) + "}"
    try:
        parse_fractional_tolerance_expression(text)
        return text
    except ValueError:
        # A normalized rational may exceed the grammar's per-token limit even
        # though its original factored form is supported. Preserve that form.
        text = re.sub(r"\\(?:left|right)(?![A-Za-z])", "", expression.strip(" \t\n"))
        if text.startswith(r"\lfloor") and text.endswith(r"\rfloor"):
            text = text[7:-7]
        text = text.replace("Q", "(1)")
        try:
            parse_fractional_tolerance_expression(text)
            return text
        except ValueError:
            return None


def _exact_fraction(expression):
    c, q, n, log = parse_exact_tolerance_monomial(expression, fractional=True)
    if c == 0:
        return (Fraction(0), Fraction(0), Fraction(0))
    if n == 0 and log == 0:
        c = min(c, Fraction(1))
    return c, n, log


def validate_fraction(original, target, *, standard):
    try:
        actual = _exact_fraction(target)
        if standard == REVIEW_STANDARD:
            expected = _exact_fraction(original)
        else:
            c, q, n, log = parse_exact_tolerance_monomial(original)
            if c == 0 or (q == 0 and n == 0 and log == 0 and c < 1):
                expected = (Fraction(0), Fraction(0), Fraction(0))
            elif q == 1:
                expected = (min(c, Fraction(1)) if n == 0 and log == 0 else c, n, log)
            else:
                expected = None
        if expected is None or actual != expected:
            raise VerifierError("dcp_derivation_fraction_not_equivalent")
    except (ValueError, TypeError) as exc:
        raise VerifierError("dcp_derivation_fraction") from exc
    return target


def original_metrics(material):
    """Reconstruct immutable v6/v7 structured claims without executing old code."""
    old, accepted, manifest = (
        material[k] for k in ("intake", "accepted_results", "manifest")
    )
    config = old["data"]["effective"]["config"]
    standard = config.get("review_standard")
    if (
        config.get("id") != "dcp"
        or standard not in (COUNT_STANDARD, REVIEW_STANDARD)
        or config.get("structured_claims") != "atomic-v1"
        or config.get("acceptance_policy", "atomic-claims-v1") != "atomic-claims-v1"
        or accepted.get("policy_id") != "atomic-claims-v1"
        or config["policies"]["validity"]
        != {"version": standard, "structured_bounds": "required"}
        or [o["name"] for o in config["objectives"]] != ["time_growth"]
        or [o["direction"] for o in config["objectives"]] != ["-"]
        or [o.get("score_source") for o in config["objectives"]] != [{"claim": 0}]
        or [o.get("score_minimum") for o in config["objectives"]]
        != [{"numerator": "0", "denominator": "1"}]
    ):
        raise VerifierError("dcp_derivation_original_contract")
    # The original full claims, including their structured objects, were accepted
    # atomically. Recheck domain syntax, without replaying an old implementation.
    from dcp_admission import validate_resource_claims

    validate_resource_claims(manifest, standard=standard)
    claims, files = manifest["claims"], old["data"]["files"]
    provenance = {
        "intake_sha256": old["sha256"],
        "dossier_sha256": accepted["source"]["dossier_sha256"],
    }

    def source(index):
        claim = claims[index]
        return {
            "statement": claim["statement"],
            "source_sha256": digest(
                {"source": {"claim": index}, "files": digest(files)}
            ),
            "evidence": {path: files[path]["sha256"] for path in claim["evidence"]},
        }

    resources = {
        name: {
            **source(i),
            "bound": reviewed_bound(
                claims[i]["structured"], claims[i]["score"], contract=CONTRACT
            ),
        }
        for i, name in enumerate(RESOURCES)
    }
    tolerance = reviewed_tolerance(manifest, standard=standard)
    metrics = {
        "dcp": {**CONTRACT, **provenance, "resources": resources},
        "dcp_error_tolerance": {
            "version": (
                "reviewed-fraction-v1"
                if standard == REVIEW_STANDARD
                else "reviewed-expression-v1"
            ),
            **tolerance,
            **source(4),
            **provenance,
        },
    }
    return [score_value(claims[0]["score"])], metrics, standard


def ordinary_projection(output, *, config):
    """Representation-only export after a fresh ordinary v6/v7 review."""
    if config["policies"]["scoring"] != SCORING_POLICY or output.get("scores") is None:
        return output
    result = deepcopy(output)
    metrics = result.get("metrics", {})
    tolerance = metrics.get("dcp_error_tolerance")
    if not tolerance:
        raise VerifierError("dcp_derivation_ordinary_tolerance")
    if tolerance["version"] == "reviewed-fraction-v1":
        return result
    if tolerance["version"] != "reviewed-expression-v1":
        raise VerifierError("dcp_derivation_ordinary_version")
    fraction = fraction_from_count(tolerance["expression"])
    metrics["dcp_original"] = deepcopy(
        {"dcp": metrics["dcp"], "dcp_error_tolerance": tolerance}
    )
    metrics["dcp_representation"] = {
        "version": VERSION,
        "method": "exact-count-to-fraction",
        "status": "derived" if fraction is not None else "unsupported",
    }
    if fraction is not None:
        metrics["dcp_error_tolerance"] = {
            **tolerance,
            "version": "reviewed-fraction-v1",
            "expression": fraction,
        }
    return result


def _project_verified(result, material):
    data = result["data"]
    intake, decision = data["intake"], data["decision"]
    evaluation = intake["data"]["evaluation"]
    retained = evaluation["retained_result"]
    if evaluation["policies"]["scoring"] != SCORING_POLICY:
        raise VerifierError("dcp_derivation_scoring_policy")
    metadata = {
        "version": VERSION,
        "status": decision["status"],
        "reason": decision["reason"],
        "intake_sha256": intake["sha256"],
        "dossier_sha256": result["sha256"],
        "retained_result": deepcopy(retained),
        "source_refs": deepcopy(decision["source_refs"]),
    }
    output = {
        "scores": None,
        "derived_from": deepcopy(retained),
        "metrics": {"dcp_derivation": metadata},
    }
    if not retained["validity"]["valid"]:
        if decision["status"] != "not_applicable" or decision["payload"] is not None:
            raise VerifierError("dcp_derivation_invalid_source")
        return output
    scores, original, standard = original_metrics(material)
    old, accepted = material["intake"], material["accepted_results"]
    if (
        evaluation["policies"]["validity"]
        != old["data"]["effective"]["evaluation"]["policies"]["validity"]
    ):
        raise VerifierError("dcp_derivation_changed_validity")
    metadata["original"] = {
        "intake_sha256": old["sha256"],
        "dossier_sha256": accepted["source"]["dossier_sha256"],
        "review_sha256": accepted["source"]["review_sha256"],
        "accepted_results_sha256": accepted["sha256"],
    }
    output["scores"] = scores
    output["metrics"]["dcp_original"] = deepcopy(original)
    output["metrics"].update(deepcopy(original))
    if decision["status"] == "unsupported" and decision["payload"] is None:
        # Preserve the original score/count metrics. The fraction-configured
        # frontier explicitly omits this incompatible representation.
        return output
    if (
        decision["status"] != "derived"
        or type(decision["payload"]) is not dict
        or set(decision["payload"]) != {"fraction"}
    ):
        raise VerifierError("dcp_derivation_payload")
    if not any(ref["source"] == "claim:4" for ref in decision["source_refs"]):
        raise VerifierError("dcp_derivation_tolerance_citation")
    fraction = validate_fraction(
        original["dcp_error_tolerance"]["expression"],
        decision["payload"]["fraction"],
        standard=standard,
    )
    shared = {"intake_sha256": intake["sha256"], "dossier_sha256": result["sha256"]}
    # The five-column vector is bound to this representation review. Its
    # original full claims and validity provenance remain separately retained.
    output["metrics"]["dcp"].update(shared)
    for value in output["metrics"]["dcp"]["resources"].values():
        value["source_sha256"] = digest(
            {
                "original_source_sha256": value["source_sha256"],
                "derivation_sha256": result["sha256"],
            }
        )
    tolerance = output["metrics"]["dcp_error_tolerance"]
    tolerance.update(shared)
    tolerance.update(
        version="reviewed-fraction-v1",
        expression=fraction,
        source_sha256=digest(
            {
                "original_source_sha256": tolerance["source_sha256"],
                "derivation_sha256": result["sha256"],
            }
        ),
    )
    return output


def projection(result, *, expected_intake=None, preview=False):
    from llm_verifier.derivation import source_material, verify_derivation

    data = verify_derivation(result, expected_intake=expected_intake)
    if result["simulation"] and not preview:
        raise VerifierError("simulation_cannot_publish_score")
    output = _project_verified(result, source_material(data["intake"]))
    return (
        {
            "publishable": False,
            "simulation": result["simulation"],
            "score_preview": output,
        }
        if preview
        else output
    )
