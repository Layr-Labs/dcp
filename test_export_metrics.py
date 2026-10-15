"""Tests of our metadata projection; no network, Docker, or mathematical judge."""

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from llm_verifier import pipeline
from llm_verifier.artifacts import intake_snapshot, seal
from llm_verifier.checks import score_gate
from llm_verifier.config import load_config
from llm_verifier.errors import VerifierError
from llm_verifier.files import write_json
from llm_verifier.jsonutil import canonical
from llm_verifier.provider import HttpResponse, HttpTransport
from llm_verifier.simulation import ScriptedProvider

from export_metrics import export, projection

ROOT = Path(__file__).resolve().parent


def fixture(*, accepted=3, invalid=False, fields=None, simulation=False, negative=False):
    effective = load_config(ROOT, "verifier.json", "submission")
    if fields is not None:
        effective["evaluation"]["fields"] = fields
    # Independent inert fixtures: participant submissions never determine test expectations.
    statements = ("Fixture: T(n) = O(2^{n^(1/3) log2 n}); index 1/3.",
                  "Fixture: S_C(n) = O(n^100); index 0.",
                  "Fixture: S_Q(n) = O(2^n); index 1.")
    values = (("1", "3"), ("0", "1"), ("1", "1"))
    claims = [{"statement": text, "score": {"numerator": n, "denominator": d},
               "evidence": ["proof.md"]} for text, (n, d) in zip(statements, values)]
    if negative:
        claims[0]["score"] = {"numerator": "-1", "denominator": "1"}
    with tempfile.TemporaryDirectory() as temporary:
        candidate = Path(temporary)
        (candidate / "proof.md").write_text("Inert fixture, not a mathematical proof.")
        write_json(candidate / "submission.json", {"version": 1, "title": "Fixture",
                   "claims": claims, "experiments": []})
        intake = intake_snapshot(effective, candidate)
    initial = pipeline.execute(intake)  # Empty execution plan: no Docker invocation.
    ids = [b["claim_id"] for b in score_gate(intake["data"], initial)["bindings"]]
    judgment = {"valid": not invalid, "scores": None, "reason": "Scripted test only",
                "accepted_claims": [] if invalid else ids[:accepted],
                "assumptions": [], "unresolved_obligations": [],
                "evidence_refs": ["source:proof.md"],
                "review_standard": effective["config"]["review_standard"]}
    decision = {"kind": "judgment", "judgment": judgment, "requests": []}
    if simulation:
        first = pipeline.review(intake, initial, provider=ScriptedProvider(effective["config"]["provider"], decision))
    else:
        # Mock the network boundary, never create a production bypass in the exporter.
        body = {"id": "fixture", "model": "fixture/model", "choices": [{
            "finish_reason": "stop", "message": {"role": "assistant", "content": json.dumps(decision)}}]}
        with patch.dict("os.environ", {"OPENROUTER_API_KEY": "fixture-not-a-key"}), patch.object(
                HttpTransport, "request", return_value=HttpResponse(200, canonical(body))):
            first = pipeline.review(intake, initial)
    return pipeline.dossier(intake, initial, first)


class MetricsTest(unittest.TestCase):
    def test_full_acceptance_preserves_exact_statements_and_scores(self):
        record = fixture()
        result = projection(record)
        self.assertEqual(result["scores"], [1/3, 0, 1])
        self.assertTrue(result["valid"])
        resources = result["metrics"]["dcp"]["resources"]
        claims = record["data"]["phases"][0]["data"]["manifest"]["claims"]
        self.assertEqual(resources["time"]["statement"], claims[0]["statement"])
        self.assertEqual(resources["classical_space"]["growth_index"], {"numerator": "0", "denominator": "1"})
        self.assertIn("proof.md", resources["quantum_space"]["evidence"])
        self.assertEqual(resources["time"]["growth_index"], {"numerator": "1", "denominator": "3"})

    def test_partial_or_invalid_result_cannot_export_accepted_bounds(self):
        for record in (fixture(accepted=1), fixture(accepted=2), fixture(invalid=True)):
            with self.subTest(valid=record["data"]["judgment"]["valid"]):
                result = projection(record)
                self.assertIsNone(result["scores"])
                self.assertNotIn("metrics", result)

    def test_reorg_field_selection_is_preserved(self):
        validity = projection(fixture(fields={"scores": False, "validity": True}))
        self.assertEqual(set(validity), {"valid", "reason"})
        scores = projection(fixture(fields={"scores": True, "validity": False}))
        self.assertEqual(set(scores), {"scores", "metrics"})

    def test_negative_growth_is_rejected_even_if_model_accepts(self):
        with self.assertRaisesRegex(VerifierError, "negative_growth_index"):
            projection(fixture(negative=True))

    def test_simulation_cannot_publish(self):
        with self.assertRaisesRegex(VerifierError, "simulation_cannot_publish"):
            projection(fixture(simulation=True))

    def test_resealed_metadata_cannot_replace_reviewed_statement(self):
        record = copy.deepcopy(fixture())
        record["data"]["phases"][0]["data"]["manifest"]["claims"][0]["statement"] = "T(n) = O(1)"
        record = seal(record["stage"], record["bindings"], record["data"], record["parents"])
        with self.assertRaises(VerifierError):
            projection(record)

    def test_failed_export_removes_stale_score(self):
        with tempfile.TemporaryDirectory() as temporary:
            source, output = Path(temporary)/"dossier.json", Path(temporary)/"score.json"
            write_json(source, fixture(simulation=True))
            output.write_text('{"valid":true,"scores":[0,0,0]}')
            with self.assertRaises(VerifierError):
                export(source, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
