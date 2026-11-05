"""DCP representation boundary tests; no provider or hosted operations."""

from copy import deepcopy
import json
from pathlib import Path
import unittest

from llm_verifier.errors import VerifierError
from llm_verifier.config import select_evaluation
from llm_verifier import pipeline
from llm_verifier.jsonutil import digest
from score_derivation import (
    SCORING_POLICY,
    RETAINED_VALIDITY,
    fraction_from_count,
    validate_fraction,
    original_metrics,
    ordinary_projection,
    _project_verified,
)
from select_scoring_route import select_route
from test_export_metrics import fixture, fixture_claims

ROOT = Path(__file__).resolve().parent


def count_fixture(expression="0"):
    claims = fixture_claims()
    claims[4]["structured"].update(
        version="dcp-error-tolerance-v1", expression=expression
    )

    def configure(effective):
        config = effective["config"]
        config["review_standard"] = RETAINED_VALIDITY["version"]
        config["policies"]["validity"] = deepcopy(RETAINED_VALIDITY)
        config["supported_policies"]["validity"] = [
            {
                "selector": deepcopy(RETAINED_VALIDITY),
                "instructions": "Offline count fixture.",
            }
        ]
        effective["evaluation"], effective["policy_instructions"] = select_evaluation(
            config
        )

    record = fixture(claims=claims, mode="required", configure=configure)
    old = record["data"]["phases"][0]
    return record, {
        "intake": old,
        "accepted_results": pipeline.export_results(record),
        "manifest": old["data"]["manifest"],
    }


class FractionDerivationTest(unittest.TestCase):
    def test_exact_rates_and_zero(self):
        for count, fraction in [
            ("0", "0"),
            ("Q", "1"),
            ("2Q", "1"),
            ("Q/100", "1/100"),
            (r"\lfloor Q/n^2\rfloor", "1/n^2"),
            ("3Q/(2nL^2)", "3/(2nL^2)"),
        ]:
            with self.subTest(count=count):
                self.assertEqual(
                    validate_fraction(count, fraction, standard="dcp-joint-bounds-v6"),
                    fraction,
                )
                self.assertIsNotNone(fraction_from_count(count))

    def test_positive_counts_without_q_are_not_rates(self):
        for count in ["1", "100", "n^2", "L"]:
            self.assertIsNone(fraction_from_count(count))
            with self.assertRaises(VerifierError):
                validate_fraction(count, "1/n", standard="dcp-joint-bounds-v6")

    def test_cannot_strengthen_weaken_or_round_away_guarantees(self):
        for count, target in [
            ("0", "1/n^2"),
            ("Q/n^2", "0"),
            ("Q/n^2", "1/n"),
            ("Q/100", "1/10"),
            ("Q/100", "1/1000"),
        ]:
            with self.assertRaises(VerifierError):
                validate_fraction(count, target, standard="dcp-joint-bounds-v6")

    def test_eventual_full_tolerance_does_not_authorize_finite_parameter_strengthening(
        self,
    ):
        # Both expressions compare as eventually full, but 1 would strengthen
        # the first law before its cap is reached. Extraction preserves the law.
        validate_fraction("Q*n/100", "n/100", standard="dcp-joint-bounds-v6")
        with self.assertRaises(VerifierError):
            validate_fraction("Q*n/100", "1", standard="dcp-joint-bounds-v6")
        self.assertIsNone(fraction_from_count("100/n^2"))

    def test_supported_factored_coefficient_survives_rendering(self):
        count = "1234567890123456789012345^{8}*Q/n"
        target = fraction_from_count(count)
        self.assertIsNotNone(target)
        validate_fraction(count, target, standard="dcp-joint-bounds-v6")

    def test_fraction_payload_cannot_contain_count_syntax(self):
        for target in ["Q/Q", r"\lfloor 1/n^2\rfloor", "0.01", "n+1", "-1"]:
            with self.assertRaises(VerifierError):
                validate_fraction("Q/100", target, standard="dcp-joint-bounds-v6")

    def test_reconstructs_original_metric_bytes_and_time(self):
        from export_metrics import projection

        record, material = count_fixture("Q/100")
        score, metrics, standard = original_metrics(material)
        original = projection(record)
        self.assertEqual(score, original["scores"])
        self.assertEqual(metrics, original["metrics"])
        self.assertEqual(standard, "dcp-joint-bounds-v6")

    def test_ordinary_profile_maps_counts_only_after_acceptance(self):
        from export_metrics import projection

        record, _ = count_fixture("Q/100")
        old = projection(record)
        before = deepcopy(old)
        mapped = ordinary_projection(
            old, config={"policies": {"scoring": SCORING_POLICY}}
        )
        self.assertEqual(old, before)
        self.assertEqual(mapped["scores"], old["scores"])
        self.assertEqual(mapped["metrics"]["dcp_original"], old["metrics"])
        self.assertEqual(
            mapped["metrics"]["dcp_error_tolerance"]["context"],
            old["metrics"]["dcp_error_tolerance"]["context"],
        )
        self.assertEqual(
            mapped["metrics"]["dcp_error_tolerance"]["version"], "reviewed-fraction-v1"
        )

    def test_unsupported_ordinary_count_remains_explicitly_count_based(self):
        from export_metrics import projection

        record, _ = count_fixture("n^2")
        old = projection(record)
        output = ordinary_projection(
            old, config={"policies": {"scoring": SCORING_POLICY}}
        )
        self.assertEqual(
            output["metrics"]["dcp_error_tolerance"],
            old["metrics"]["dcp_error_tolerance"],
        )
        self.assertEqual(
            output["metrics"]["dcp_representation"]["status"], "unsupported"
        )

    def test_default_scoring_does_not_convert_historical_exports(self):
        from export_metrics import projection

        record, _ = count_fixture("Q/100")
        old = projection(record)
        self.assertIs(
            ordinary_projection(
                old, config={"policies": {"scoring": {"version": "dcp-time-growth-v2"}}}
            ),
            old,
        )

    def test_wrong_original_contract_is_rejected(self):
        _, material = count_fixture()
        for key, value in [
            ("id", "other"),
            ("acceptance_policy", "exploratory-v1"),
            ("structured_claims", None),
        ]:
            altered = deepcopy(material)
            altered["intake"]["data"]["effective"]["config"][key] = value
            with self.assertRaises(VerifierError):
                original_metrics(altered)

    def test_profile_and_adapter_constants_match(self):
        from tools.derivation_profile import SCORING, VALIDITY, VERIFIER_REVISION
        from score_derivation import VERIFIER_REVISION as pin

        self.assertEqual(SCORING, SCORING_POLICY)
        self.assertEqual(VALIDITY, RETAINED_VALIDITY)
        self.assertEqual(pin, VERIFIER_REVISION)


class RouteTest(unittest.TestCase):
    def evaluation(self, **changes):
        value = {
            "fields": {"scores": True, "validity": False},
            "policies": {"scoring": SCORING_POLICY, "validity": RETAINED_VALIDITY},
            "retained_result": {"version": "yukon-retained-result-v1"},
        }
        value.update(changes)
        return value

    def test_retained_score_only_has_its_own_route(self):
        self.assertEqual(select_route(json.dumps(self.evaluation())), "derive")

    def test_no_descriptor_never_falls_back_to_paid_review(self):
        value = self.evaluation()
        value.pop("retained_result")
        with self.assertRaises(ValueError):
            select_route(json.dumps(value))

    def test_explicit_missing_validity_uses_ordinary_route(self):
        value = self.evaluation(fields={"scores": True, "validity": True})
        value.pop("retained_result")
        self.assertEqual(select_route(json.dumps(value)), "ordinary")

    def test_descriptor_cannot_accompany_new_validity(self):
        with self.assertRaises(ValueError):
            select_route(
                json.dumps(self.evaluation(fields={"scores": True, "validity": True}))
            )

    def test_invalid_json_or_flags_fail_closed(self):
        for raw in [
            '{"fields":{},"fields":{}}',
            "null",
            '{"x":NaN}',
            json.dumps(self.evaluation(fields={"scores": 1, "validity": False})),
        ]:
            with self.assertRaises(ValueError):
                select_route(raw)


if __name__ == "__main__":
    unittest.main()
