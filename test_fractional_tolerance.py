"""Fractional guarantees keep positive rates and never reinterpret count dossiers."""
import unittest

from llm_verifier.config import select_evaluation
from dcp_admission import admission_receipt
from export_metrics import projection
from test_dcp_admission import effective_for, files_for
from test_export_metrics import fixture, fixture_claims
from tolerance_expression import parse_fractional_tolerance_expression as parse


class FractionalToleranceTest(unittest.TestCase):
    def test_fractions_are_not_floored(self):
        for expression, coefficient, n_power in [("1/2", "1/2", "0"), ("1/n^2", "1", "-2"), ("100/n", "100", "-1")]:
            self.assertEqual(parse(expression), dict(kind="fraction", coefficient=coefficient, nPower=n_power, logPower="0"))
        self.assertEqual(parse("0")["kind"], "zero")
        for expression in ["1", "2", "n", "L", "n/L"]:
            self.assertEqual(parse(expression), parse("1"))

    def test_aliases_and_denominator_precedence(self):
        forms = ["1/2n^2", "1/(2n^2)", r"\frac{1}{2n^2}", "(1/2)n^{-2}"]
        for expression in forms:
            self.assertEqual(parse(expression), parse("1/(2n^2)"))
        self.assertEqual(parse("1/2*n^2"), parse("1"))
        self.assertEqual(parse(r"1/n(\log_2 n)^2"), parse("1/(nL^2)"))
        self.assertEqual(parse("n^{1/2}/n")["nPower"], "-1/2")

    def test_count_or_unsupported_notation_is_rejected_before_review(self):
        for expression in ["Q", "Q/n^2", "1/Q", "Q/Q", "0Q", r"\lfloor 1/n^2\rfloor",
                           r"\left\lfloor 1/2\right\rfloor", "n+1", "-1", "0.01", "1/0", "n^-2",
                           r"\log_2 n^2", "9"*65, "("*13+"n"+")"*13]:
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    parse(expression)
                claims = fixture_claims()
                claims[4]["structured"]["expression"] = expression
                receipt = admission_receipt(effective_for(), files_for(claims))
                self.assertEqual(receipt["outcome"], "format_rejected")
                self.assertEqual(receipt["diagnostic"]["code"], "dcp_tolerance_comparison_expression")

    def test_fraction_contract_is_distinct_even_for_zero(self):
        claims = fixture_claims()
        claims[4]["structured"]["version"] = "dcp-error-tolerance-v1"
        receipt = admission_receipt(effective_for(), files_for(claims))
        self.assertEqual(receipt["diagnostic"]["code"], "dcp_tolerance_contract")

    def test_v6_count_dossier_exports_original_expression_and_version(self):
        def prior(effective):
            config = effective["config"]
            policy = {"version": "dcp-joint-bounds-v6", "structured_bounds": "required"}
            config["review_standard"] = policy["version"]
            config["policies"]["validity"] = policy
            config["supported_policies"]["validity"] = [{"selector": policy, "instructions": "Historical count grammar."}]
            effective["evaluation"], effective["policy_instructions"] = select_evaluation(config)
        for expression in ["1/2", r"\lfloor Q/n^2\rfloor", "n^2"]:
            claims = fixture_claims()
            claims[4]["structured"].update(version="dcp-error-tolerance-v1", expression=expression)
            output = projection(fixture(claims=claims, mode="required", configure=prior))
            self.assertEqual(output["metrics"]["dcp_error_tolerance"]["version"], "reviewed-expression-v1")
            self.assertEqual(output["metrics"]["dcp_error_tolerance"]["expression"], expression)
            self.assertEqual(output["scores"], [1/3])


if __name__ == "__main__":
    unittest.main()
