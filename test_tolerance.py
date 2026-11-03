"""Tolerance is a jointly reviewed expression, never a score or guessed bound."""
import unittest

from llm_verifier.config import select_evaluation
from llm_verifier.errors import VerifierError
from dcp_admission import admission_receipt, validate_intake
from export_metrics import projection
from test_dcp_admission import effective_for, files_for
from test_export_metrics import fixture, fixture_claims


class ToleranceTest(unittest.TestCase):
    def test_exact_expression_context_and_provenance_without_scalar(self):
        for expression in ("0", r"\lfloor Q/n^2\rfloor", r"\lfloor Q/100\rfloor"):
            claims = fixture_claims()
            claims[4]["structured"].update(expression=expression, error_model="Explicit inert test error model.")
            record = fixture(claims=claims, mode="required")
            result = projection(record)
            tolerance = result["metrics"]["dcp_error_tolerance"]
            self.assertEqual(tolerance["expression"], expression)
            self.assertEqual(tolerance["context"], claims[4]["structured"]["error_model"])
            self.assertEqual(tolerance["statement"], claims[4]["statement"])
            self.assertEqual(tolerance["source_sha256"], record["data"]["accepted_structured_claims"][4]["source_sha256"])
            self.assertEqual(tolerance["intake_sha256"], result["metrics"]["dcp"]["intake_sha256"])
            self.assertEqual(tolerance["dossier_sha256"], result["metrics"]["dcp"]["dossier_sha256"])
            self.assertEqual(result["scores"], [1/3])
            self.assertEqual(len(record["data"]["score_records"]), 1)
            self.assertNotIn("score", tolerance)
            self.assertNotIn("error_tolerance", result["metrics"]["dcp"]["resources"])

    def test_required_missing_or_malformed_tolerance_rejects_before_review(self):
        missing = fixture_claims()[:4]
        variants = [missing]
        for field, value in (("expression", ""), ("expression", "n" * 2049),
                             ("error_model", ""), ("version", "other")):
            claims = fixture_claims()
            claims[4]["structured"][field] = value
            variants.append(claims)
        with_score = fixture_claims()
        with_score[4]["score"] = {"numerator": "0", "denominator": "1"}
        variants.append(with_score)
        no_structure = fixture_claims()
        no_structure[4].pop("structured")
        variants.append(no_structure)
        for claims in variants:
            receipt = admission_receipt(effective_for(), files_for(claims))
            self.assertEqual(receipt["outcome"], "format_rejected")
            self.assertEqual(receipt["diagnostic"]["resource"], "error_tolerance")

    def test_optional_scored_result_still_needs_tolerance_evidence(self):
        with self.assertRaisesRegex(VerifierError, "dcp_tolerance_claim_required"):
            projection(fixture(claims=fixture_claims()[:4]))
        self.assertIsNone(projection(fixture(unscored=True))["scores"])

    def test_unproved_tolerance_invalidates_joint_result(self):
        result = projection(fixture(invalid=True, mode="required"))
        self.assertFalse(result["valid"])
        self.assertIsNone(result["scores"])
        self.assertNotIn("metrics", result)

    def test_prior_four_resource_policy_does_not_invent_tolerance(self):
        def prior(effective):
            config = effective["config"]
            config["review_standard"] = "dcp-joint-bounds-v4"
            policy = {"version": "dcp-joint-bounds-v4", "structured_bounds": "required"}
            config["policies"]["validity"] = policy
            config["supported_policies"]["validity"] = [{"selector": policy, "instructions": "Prior sample-only required policy."}]
            effective["evaluation"], effective["policy_instructions"] = select_evaluation(config)
        record = fixture(mode="required", configure=prior)
        result = projection(record)
        self.assertEqual(len(result["metrics"]["dcp"]["resources"]), 4)
        self.assertNotIn("dcp_error_tolerance", result["metrics"])
        self.assertEqual(validate_intake(record["data"]["phases"][0]), "required")


if __name__ == "__main__":
    unittest.main()
