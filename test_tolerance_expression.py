"""Exact symbolic admission, rounding, and policy compatibility."""
import unittest
from llm_verifier.config import select_evaluation
from dcp_admission import admission_receipt
from export_metrics import projection
from test_dcp_admission import effective_for, files_for
from test_export_metrics import fixture, fixture_claims
from tolerance_expression import parse_tolerance_expression as parse


class ToleranceExpressionTest(unittest.TestCase):
    def test_floor_and_fraction_aliases(self):
        forms = [r"\lfloor Q/n^2\rfloor", r"\left\lfloor\frac{2Q}{2n^{2}}\right\rfloor", r"Q n^{-2}"]
        expected = dict(kind="rate", coefficient="1", samplePower="1", nPower="-2", logPower="0")
        for expression in forms:
            self.assertEqual(parse(expression), expected)
        self.assertEqual(parse("(n^2/100)")["coefficient"], "1/100")
        self.assertEqual(parse("(n^2/100)")["nPower"], "2")
        self.assertEqual(parse("n^{2/100}")["nPower"], "1/50")

    def test_juxtaposed_denominators_and_explicit_operator_precedence(self):
        for c in ["2", "100"]:
            expected = parse(f"Q/({c}n^2)")
            for expression in [f"Q/{c}n^2", f"Q/{c} n^2", rf"\lfloor Q/{c}n^2\rfloor", rf"\frac{{Q}}{{{c}n^2}}"]:
                with self.subTest(expression=expression):
                    self.assertEqual(parse(expression), expected)
        self.assertEqual(parse(r"Q/n(\log_2 n)^2"), parse(r"Q/(n(\log_2 n)^2)"))
        self.assertEqual(parse("Q/2*n^2"), parse("Q"))
        self.assertEqual(parse("Q/2*n^{-2}/5"), parse("Q/(10n^2)"))
        self.assertEqual(parse("Q/2/5*n^{-2}"), parse("Q/(10n^2)"))
        self.assertEqual(parse(r"Q/n*(\log_2 n)^2")["logPower"], "2")

    def test_rounding_and_saturation(self):
        for expression in ["0", "1/2", "100/n"]:
            self.assertEqual(parse(expression)["kind"], "zero")
        self.assertEqual(parse(r"\lfloor 3/2\rfloor"), parse("1"))
        for expression in ["Q", "2Q", "Q*n"]:
            self.assertEqual(parse(expression)["kind"], "full")

    def test_unsupported_form_is_rejected_before_review_in_v6(self):
        for expression in ["Q+n", "Q^2", "Q^{1/2}", "Q/0", r"\log_2 n^2", r"\sqrt{Q}",
                           r"\def\a{Q}\a", "9"*65, "("*13+"Q"+")"*13, "\ufeffQ"]:
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    parse(expression)
                claims = fixture_claims()
                claims[4]["structured"]["expression"] = expression
                claims[4]["structured"]["version"] = "dcp-error-tolerance-v1"
                effective = effective_for()
                config = effective["config"]
                policy = {"version": "dcp-joint-bounds-v6", "structured_bounds": "required"}
                config["review_standard"] = policy["version"]
                config["policies"]["validity"] = policy
                config["supported_policies"]["validity"] = [{"selector": policy, "instructions": "Historical count grammar."}]
                effective["evaluation"], effective["policy_instructions"] = select_evaluation(config)
                receipt = admission_receipt(effective, files_for(claims))
                self.assertEqual(receipt["outcome"], "format_rejected")
                self.assertEqual(receipt["diagnostic"]["code"], "dcp_tolerance_comparison_expression")

    def test_v5_still_accepts_its_original_arbitrary_expression_contract(self):
        def prior(effective):
            config = effective["config"]
            config["review_standard"] = "dcp-joint-bounds-v5"
            policy = {"version": "dcp-joint-bounds-v5", "structured_bounds": "required"}
            config["policies"]["validity"] = policy
            config["supported_policies"]["validity"] = [{"selector": policy, "instructions": "Prior display-only expression policy."}]
            effective["evaluation"], effective["policy_instructions"] = select_evaluation(config)
        claims = fixture_claims()
        claims[4]["structured"]["expression"] = r"\sqrt{Q}"
        claims[4]["structured"]["version"] = "dcp-error-tolerance-v1"
        output = projection(fixture(claims=claims, mode="required", configure=prior))
        self.assertEqual(output["metrics"]["dcp_error_tolerance"]["expression"], r"\sqrt{Q}")
        self.assertEqual(output["scores"], [1/3])


if __name__ == "__main__":
    unittest.main()
