"""Joint sample evidence, historical contracts, and time-only scoring boundaries."""
import json
import unittest

from llm_verifier.config import select_evaluation
from llm_verifier.errors import VerifierError

from complexity_bounds import LEGACY_CONTRACT, LEGACY_RESOURCES, RESOURCES
from dcp_admission import FormatRejection
from export_metrics import projection
from test_export_metrics import ROOT, bound, fixture, fixture_claims


def previous_config(effective):
    config = effective["config"]
    config["review_standard"] = "dcp-joint-bounds-v3"
    policy = {"version": "dcp-joint-bounds-v3", "structured_bounds": "required"}
    config["policies"]["validity"] = policy
    config["supported_policies"]["validity"] = [{
        "selector": policy, "instructions": "Historical three-resource required policy fixture."}]
    effective["evaluation"], effective["policy_instructions"] = select_evaluation(config)


class SamplesTest(unittest.TestCase):
    def test_sample_changes_keep_time_score_and_bind_independent_evidence(self):
        results = []
        for power in ("2", "100"):
            claims = fixture_claims()
            claims[3]["statement"] = f"Offline fixture: the same algorithm acquires O(n^{power}) samples; index 0."
            claims[3]["structured"]["bound"] = bound(n_power=power)
            record = fixture(claims=claims, mode="required")
            result = projection(record)
            sample = result["metrics"]["dcp"]["resources"]["samples"]
            self.assertEqual(sample["statement"], claims[3]["statement"])
            self.assertEqual(sample["bound"], bound(n_power=power))
            self.assertEqual(sample["source_sha256"], record["data"]["accepted_structured_claims"][3]["source_sha256"])
            self.assertEqual(len(record["data"]["score_records"]), 1)
            results.append(result)
        self.assertEqual([result["scores"] for result in results], [[1/3], [1/3]])

    def test_unproved_sample_claim_suppresses_all_scores_and_metrics(self):
        claims = fixture_claims()
        claims[3]["statement"] = "Unsupported sample bound for this fixture algorithm."
        output = projection(fixture(claims=claims, mode="required", invalid=True))
        self.assertFalse(output["valid"])
        self.assertIsNone(output["scores"])
        self.assertNotIn("metrics", output)

    def test_missing_sample_claim_cannot_publish_even_in_optional_mode(self):
        with self.assertRaisesRegex(VerifierError, "dcp_joint_resource_claims_required"):
            projection(fixture(claims=fixture_claims()[:3]))
        claims = fixture_claims()
        claims[3].pop("structured")
        result = projection(fixture(claims=claims))
        self.assertEqual(result["metrics"]["dcp_omission"]["details"],
                         [{"resource": "samples", "reason": "missing_structured_bound"}])
        self.assertNotIn("dcp", result["metrics"])

    def test_v3_required_dossier_preserves_three_resources_and_requires_memory(self):
        output = projection(fixture(mode="required", configure=previous_config))
        self.assertEqual(output["metrics"]["dcp"]["version"], LEGACY_CONTRACT["version"])
        self.assertEqual(tuple(output["metrics"]["dcp"]["resources"]), LEGACY_RESOURCES)
        self.assertNotIn("samples", output["metrics"]["dcp"]["resources"])
        claims = fixture_claims()
        claims[2].pop("structured")
        with self.assertRaises(FormatRejection):
            projection(fixture(mode="required", claims=claims, configure=previous_config))

    def test_four_column_tab_matches_contract_and_keeps_time_sort(self):
        tab = json.loads((ROOT / "complexity-tab.json").read_text())
        output = projection(fixture(mode="required"))["metrics"]["dcp"]
        self.assertEqual(tuple(column["key"] for column in tab["columns"]), RESOURCES)
        self.assertEqual(tab["metricsVersion"], output["version"])
        self.assertEqual(tab["defaultSort"], {"by": "metric", "key": "time", "direction": "asc"})
        for key in ("scope", "model", "comparator", "notation"):
            self.assertEqual(tab[key], output[key])


if __name__ == "__main__":
    unittest.main()
