"""Real verifier/producer tests with an offline HTTP boundary, never a live judge."""

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from llm_verifier import pipeline, structured_claims
from llm_verifier.artifacts import intake_snapshot, seal
from llm_verifier.config import load_config, select_evaluation
from llm_verifier.errors import VerifierError
from llm_verifier.files import write_json
from llm_verifier.jsonutil import canonical, digest
from llm_verifier.provider import HttpResponse, HttpTransport
from llm_verifier.simulation import ScriptedProvider

from complexity_bounds import CONTRACT, LEGACY_CONTRACT, RESOURCES, growth_index, normalize_bound, reviewed_bound
from export_metrics import export, projection

ROOT = Path(__file__).resolve().parent


def bound(*, exponent=(), n_power="0", log_power="0", coefficient="1"):
    return {"coefficient": coefficient, "exponent": list(exponent),
            "nPower": n_power, "logPower": log_power}


def term(a="1", p="1/3", q="1"):
    return {"coefficient": a, "nPower": p, "logPower": q}


def tolerance_claim(expression="0", error_model="All acquired samples are independent ideal coset states."):
    return {"statement": "Offline fixture only: the same algorithm has the stated malformed-sample count tolerance and joint resource bounds under the stated error model.",
            "evidence": ["proof.md"], "structured": {"version": "dcp-error-tolerance-v1",
            "expression": expression, "error_model": error_model}}


def fixture_claims():
    # Deliberately independent of the participant-editable baseline.
    statements = ("Offline fixture algorithm A: T(n) = O(2^{n^(1/3) log2 n}); index 1/3; joint bounds.",
                  "Offline fixture algorithm A: S_C(n) = O(n^100); index 0; joint bounds.",
                  "Offline fixture algorithm A: S_Q(n) = O(2^n); index 1; joint bounds.",
                  "Offline fixture algorithm A: Q(n) = O(n^3); index 0; joint bounds.")
    values = (("1", "3"), ("0", "1"), ("1", "1"), ("0", "1"))
    bounds = (bound(exponent=[term()]), bound(n_power="100"),
              bound(exponent=[term(p="1", q="0")]), bound(n_power="3"))
    return [{"statement": text, "score": {"numerator": n, "denominator": d},
             "evidence": ["proof.md"], "structured": {**CONTRACT, "bound": b}}
            for text, (n, d), b in zip(statements, values, bounds)] + [tolerance_claim()]


def fixture(*, unscored=False, invalid=False, fields=None, simulation=False,
            claims=None, ack="correct", configure=None, mode="optional"):
    effective = load_config(ROOT, "verifier.json", "submission")
    if mode == "optional":
        from dcp_admission import configure_mode
        effective["config"], _ = configure_mode(effective["config"],
            json.loads((ROOT / "benchmark.json").read_text()), "optional")
        effective["evaluation"], effective["policy_instructions"] = select_evaluation(effective["config"])
    if fields is not None:
        effective["evaluation"]["fields"] = fields
    if configure:
        configure(effective)
    claims = fixture_claims() if claims is None else claims
    if effective["config"]["review_standard"] in ("dcp-joint-bounds-v2", "dcp-joint-bounds-v3"):
        claims = copy.deepcopy(claims[:3])
        for claim in claims:
            if type(claim) is dict and "structured" in claim:
                claim["structured"]["version"] = LEGACY_CONTRACT["version"]
    if effective["config"]["review_standard"] == "dcp-joint-bounds-v4":
        claims = copy.deepcopy(claims[:4])
    if unscored:
        claims = ["Inert unscored lemma fixture."]
    with tempfile.TemporaryDirectory() as temporary:
        candidate = Path(temporary)
        (candidate / "proof.md").write_text("Inert offline fixture, not a mathematical proof.")
        write_json(candidate / "submission.json", {"version": 1, "title": "Offline fixture",
                   "claims": claims, "experiments": []})
        intake = intake_snapshot(effective, candidate)
    initial = pipeline.execute(intake)  # Empty plan: no Docker or candidate code.
    judgment = {"valid": not invalid, "scores": None, "reason": "Scripted offline test only",
                "evidence_refs": ["source:proof.md"],
                "review_standard": effective["config"]["review_standard"]}
    if ack is not None:
        judgment["structured_claims_sha256"] = (
            digest(structured_claims.records(intake["data"])) if ack == "correct" else ack)
    decision = {"kind": "judgment", "judgment": judgment, "requests": []}
    if simulation:
        first = pipeline.review(intake, initial, provider=ScriptedProvider(effective["config"]["provider"], decision))
    else:
        body = {"id": "fixture", "object": "chat.completion", "model": "fixture-model", "choices": [{
            "finish_reason": "stop", "message": {"role": "assistant", "content": json.dumps(decision)}}]}
        with patch.dict("os.environ", {"OPENAI_API_KEY": "fixture-not-a-key"}), patch.object(
                HttpTransport, "request", return_value=HttpResponse(200, canonical(body))):
            first = pipeline.review(intake, initial)
    return pipeline.dossier(intake, initial, first)


class MetricsTest(unittest.TestCase):
    def test_joint_acceptance_one_score_preserves_all_reviewed_resources(self):
        record = fixture()
        result = projection(record)
        self.assertEqual(result["scores"], [1/3])
        self.assertTrue(result["valid"])
        metrics = result["metrics"]["dcp"]
        for k, v in CONTRACT.items():
            self.assertEqual(metrics[k], v)
        self.assertEqual(len(record["data"]["score_records"]), 1)
        self.assertEqual(len(record["data"]["accepted_structured_claims"]), 5)
        for i, resource in enumerate(RESOURCES):
            r = metrics["resources"][resource]
            accepted = record["data"]["accepted_structured_claims"][i]
            self.assertEqual(r["statement"], accepted["statement"])
            self.assertEqual(r["source_sha256"], accepted["source_sha256"])
            self.assertEqual(r["evidence"], accepted["evidence"])
            self.assertEqual(set(r), {"statement", "bound", "source_sha256", "evidence"})
        self.assertEqual(metrics["resources"]["time"]["source_sha256"], record["data"]["score_records"][0]["source_sha256"])

    def test_all_resources_explicitly_in_review_payload(self):
        record = fixture()
        messages, schema, _ = pipeline.review_material(*record["data"]["phases"][:2])
        evidence = json.loads(messages[1]["content"].split("\n", 1)[1])
        self.assertEqual(len(evidence["structured_claims"]), 5)
        self.assertEqual(evidence["structured_claims"], record["data"]["accepted_structured_claims"])
        self.assertIn("structured_claims_sha256", canonical(schema).decode())
        self.assertIn("same algorithm", messages[0]["content"])

    def test_unscored_invalid_and_memory_rejection_have_no_metrics(self):
        for record in (fixture(unscored=True), fixture(invalid=True)):
            result = projection(record)
            self.assertIsNone(result["scores"])
            self.assertNotIn("metrics", result)
        claims = fixture_claims()
        claims[2]["statement"] = "False fixture: same algorithm uses no qubits."
        result = projection(fixture(claims=claims, invalid=True))
        self.assertIsNone(result["scores"])
        self.assertNotIn("metrics", result)

    def test_reorg_field_selection_is_preserved(self):
        validity = projection(fixture(fields={"scores": False, "validity": True}))
        self.assertEqual(set(validity), {"valid", "reason"})
        scores = projection(fixture(fields={"scores": True, "validity": False}))
        self.assertEqual(set(scores), {"scores", "metrics"})

    def test_explicit_acknowledgment_required_even_with_valid_true(self):
        for ack in (None, "0" * 64):
            with self.subTest(ack=ack), self.assertRaises(VerifierError):
                fixture(ack=ack)

    def test_runtime_without_reviewed_structure_support_fails_closed(self):
        record = fixture()
        with patch.object(pipeline, "accepted_structured_claims", None):
            with self.assertRaisesRegex(VerifierError, "dcp_structured_verifier_required"):
                projection(record)

    def test_simulation_cannot_publish(self):
        with self.assertRaisesRegex(VerifierError, "simulation_cannot_publish"):
            projection(fixture(simulation=True))

    def test_resealed_statement_bound_evidence_or_accepted_record_cannot_publish(self):
        original = fixture()
        for field in ("statement", "bound", "evidence", "accepted"):
            record = copy.deepcopy(original)
            claim = record["data"]["phases"][0]["data"]["manifest"]["claims"][0]
            if field == "statement":
                claim["statement"] = "T(n)=O(1)"
            elif field == "bound":
                claim["structured"]["bound"] = bound()
            elif field == "evidence":
                claim["evidence"] = []
            else:
                record["data"]["accepted_structured_claims"].pop()
            record = seal(record["stage"], record["bindings"], record["data"], record["parents"])
            with self.subTest(field=field), self.assertRaises(VerifierError):
                projection(record)

    def test_missing_memory_claims_never_allow_time_only_claim_acceptance(self):
        with self.assertRaisesRegex(VerifierError, "dcp_joint_resource_claims_required"):
            projection(fixture(claims=fixture_claims()[:1]))

    def test_unstructured_claims_are_retained_but_explicitly_omitted(self):
        claims = fixture_claims()
        for c in claims[:4]:
            c.pop("structured")
        result = projection(fixture(claims=claims))
        self.assertEqual(result["scores"], [1/3])
        self.assertNotIn("dcp", result["metrics"])
        omitted = result["metrics"]["dcp_omission"]
        self.assertEqual(len(omitted["details"]), 4)
        for i, resource in enumerate(RESOURCES):
            self.assertEqual(omitted["resources"][resource]["statement"], claims[i]["statement"])
            self.assertEqual(omitted["resources"][resource]["growth_index"], claims[i]["score"])
            self.assertIn("proof.md", omitted["resources"][resource]["evidence"])

    def test_unknown_exponent_coefficients_and_unsupported_shapes_are_not_inferred(self):
        for unsupported in (bound(exponent=[term(a="O(1)")]), {"latex": "2^{sqrt(n)}"},
                            bound(exponent=[term(p="-1")]), bound(coefficient="0")):
            claims = fixture_claims()
            claims[0]["structured"]["bound"] = unsupported
            result = projection(fixture(claims=claims))
            self.assertNotIn("dcp", result["metrics"])
            self.assertEqual(len(result["metrics"]["dcp_omission"]["resources"]), 4)

    def test_scope_model_notation_and_index_mismatch_are_rejected(self):
        for key in CONTRACT:
            claims = fixture_claims()
            claims[1]["structured"][key] = "wrong"
            with self.subTest(key=key), self.assertRaisesRegex(VerifierError, "dcp_bound_contract"):
                projection(fixture(claims=claims))
        claims = fixture_claims()
        claims[1]["score"] = {"numerator": "1", "denominator": "2"}
        with self.assertRaisesRegex(VerifierError, "dcp_bound_growth_index_mismatch"):
            projection(fixture(claims=claims))

    def test_negative_memory_index_is_rejected_despite_not_being_objective(self):
        claims = fixture_claims()
        claims[1]["score"] = {"numerator": "-1", "denominator": "1"}
        with self.assertRaisesRegex(VerifierError, "dcp_resource_growth_required"):
            projection(fixture(claims=claims))

    def test_equal_and_slower_time_with_lower_memory_both_export(self):
        results = []
        for p, memory in (("1/3", "100"), ("1/3", "50"), ("1/2", "2")):
            claims = fixture_claims()
            claims[0]["structured"]["bound"] = bound(exponent=[term(p=p)])
            n, d = p.split("/")
            claims[0]["score"] = {"numerator": n, "denominator": d}
            claims[0]["statement"] = f"Offline fixture: same joint algorithm has time O(2^(n^({p}) log2 n))."
            claims[1]["structured"]["bound"] = bound(n_power=memory)
            claims[1]["statement"] = f"Offline fixture: same joint algorithm uses O(n^{memory}) classical bits."
            results.append(projection(fixture(claims=claims)))
        self.assertEqual([r["scores"] for r in results], [[1/3], [1/3], [1/2]])
        self.assertTrue(all("dcp" in r["metrics"] for r in results))

    def test_actual_projection_normalizes_known_coefficients_and_log_factors(self):
        from offline_fixtures import normalization_claims
        result = projection(fixture(claims=normalization_claims()))
        time = result["metrics"]["dcp"]["resources"]["time"]
        self.assertEqual(time["bound"], bound(n_power="3", log_power="2/3", exponent=[
            term("1/2", "1/2", "1"), term("-1/3", "0", "1/2")]))
        self.assertEqual(result["scores"], [1/2])

    def test_failed_export_removes_stale_score(self):
        with tempfile.TemporaryDirectory() as temporary:
            source, output = Path(temporary)/"dossier.json", Path(temporary)/"score.json"
            write_json(source, fixture(simulation=True))
            output.write_text('{"valid":true,"scores":[0]}')
            with self.assertRaises(VerifierError):
                export(source, output)
            self.assertFalse(output.exists())


class BoundsTest(unittest.TestCase):
    def test_exact_cancellation_log_fold_and_big_o_constants(self):
        raw = bound(coefficient="037/003", n_power="-1", log_power="2/4", exponent=[
            term("2/4", "1/2", "-3/2"), term("1/2", "1/2", "-3/2"),
            term("2", "1", "0"), term("-2", "1", "0"), term("3", "0", "1")])
        expected = bound(n_power="2", log_power="1/2", exponent=[term("1", "1/2", "-3/2")])
        self.assertEqual(normalize_bound(raw), expected)
        self.assertEqual(str(growth_index(expected)), "1/2")
        self.assertEqual(normalize_bound(bound(exponent=[term("3", "0", "1")])), bound(n_power="3"))

    def test_zero_index_quasipolynomial_and_decaying_envelopes(self):
        for raw in (bound(n_power="100"), bound(exponent=[term("1", "0", "2")]),
                    bound(exponent=[term("-1", "1", "0")], n_power="100")):
            self.assertEqual(growth_index(normalize_bound(raw)), 0)

    def test_strict_rational_syntax_size_and_term_limits(self):
        for value in ("0.5", "+1", "1e4", "1/0", "1/-2", " 1", "1" * 257, 1, True):
            with self.subTest(value=str(value)[:20]), self.assertRaises(VerifierError):
                normalize_bound(bound(n_power=value))
        with self.assertRaises(VerifierError):
            normalize_bound(bound(exponent=[term()] * 65))
        with self.assertRaises(VerifierError):
            normalize_bound({**bound(), "hint": "trust me"})

    def test_complete_contract_and_exact_index(self):
        value = {**CONTRACT, "bound": bound(exponent=[term("1/2", "1/2", "0")])}
        self.assertEqual(reviewed_bound(value, {"numerator": "1", "denominator": "2"})["exponent"][0]["coefficient"], "1/2")


if __name__ == "__main__":
    unittest.main()
