"""Offline admission/producer boundaries; no provider, resolver or hosted judging."""
import copy
from contextlib import ExitStack
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from llm_verifier import pipeline
from llm_verifier.artifacts import intake_snapshot, implementation
from llm_verifier.config import load_config, select_evaluation
from llm_verifier.errors import VerifierError
from llm_verifier.files import snapshot, write_json
from llm_verifier.jsonutil import canonical, digest, sha

import dcp_admission as admission
from export_metrics import export, projection
from test_export_metrics import ROOT, bound, fixture, fixture_claims, term


def effective_for(mode="required", fields=None):
    effective = load_config(ROOT, "verifier.json", "submission")
    effective["config"], _ = admission.configure_mode(effective["config"],
        json.loads((ROOT / "benchmark.json").read_text()), mode)
    effective["evaluation"], effective["policy_instructions"] = select_evaluation(effective["config"])
    if fields is not None:
        effective["evaluation"]["fields"] = fields
    return effective


def files_for(claims=None):
    manifest = {"version": 1, "title": "Inert admission fixture", "claims":
                fixture_claims() if claims is None else claims, "experiments": []}
    return text_files({"submission.json": canonical(manifest).decode(), "proof.md": "Offline fixture only."})


def text_files(files):
    return {name: {"text": text, "sha256": sha(text.encode()), "size": len(text.encode())}
            for name, text in files.items()}


def legacy_config(effective):
    config = effective["config"]
    config["review_standard"] = admission.LEGACY_STANDARD
    policy = {"version": admission.LEGACY_STANDARD}
    config["policies"]["validity"] = policy
    config["supported_policies"]["validity"] = [{"selector": policy, "instructions": "Historical optional fixture."}]
    effective["evaluation"], effective["policy_instructions"] = select_evaluation(config)


class AdmissionTest(unittest.TestCase):
    def rejection(self, claims, fields=None):
        effective, files = effective_for(fields=fields), files_for(claims)
        original = copy.deepcopy((effective, files))
        with patch.object(admission, "intake_snapshot", side_effect=AssertionError("resolver/intake reached")), patch.object(
                pipeline, "review", side_effect=AssertionError("provider reached")):
            receipt = admission.admission_receipt(effective, files)
            self.assertEqual(receipt["outcome"], "format_rejected")
            score = admission.rejection_score(receipt)
            with self.assertRaises(admission.FormatRejection):
                admission.prepare_intake(effective, files, accepted_results_context={"must_not_resolve": True})
        self.assertEqual((effective, files), original)
        self.assertFalse(score["valid"])
        self.assertTrue(score["reason"].startswith("DCP format rejection ["))
        self.assertEqual(set(score["metrics"]), {"dcp_admission"})
        self.assertEqual(score["metrics"]["dcp_admission"]["receipt_sha256"], receipt["sha256"])
        self.assertNotIn("stage", receipt)
        return receipt, score

    def test_actual_baseline_passes_all_three_without_mutation(self):
        effective = effective_for()
        files = snapshot(ROOT / "submission", effective["config"]["limits"])
        original = copy.deepcopy(files)
        receipt = admission.admission_receipt(effective, files)
        self.assertEqual(receipt["outcome"], "review")
        intake = admission.prepare_intake(effective, files)
        self.assertEqual(intake["data"]["files"], original)
        self.assertEqual(admission.validate_intake(intake), "required")
        with self.assertRaisesRegex(VerifierError, "dcp_format_rejection_required"):
            admission.rejection_score(receipt)

    def test_missing_each_resource_structure_is_rejected_before_review(self):
        for index in range(3):
            claims = fixture_claims()
            claims[index].pop("structured")
            with self.subTest(index=index):
                receipt, score = self.rejection(claims)
                self.assertEqual(receipt["diagnostic"]["resource"], admission.RESOURCES[index])
                self.assertIsNone(score["scores"])

    def test_missing_joint_claims_partial_and_unscored_cannot_bypass(self):
        for claims in ([], fixture_claims()[:1], fixture_claims()[:2], ["A partial theorem."],
                       fixture_claims()[:1] + ["Memory unproved.", "Memory unproved."]):
            with self.subTest(claims=str(claims)[:50]):
                self.rejection(claims)

    def test_unsupported_and_malformed_bounds_reject_each_resource(self):
        bad = [None, [], {}, {"hint": "normalize my prose"},
               {"bound": bound()},
               {**fixture_claims()[0]["structured"], "bound": {"latex": "O(2^sqrt(n))"}},
               {**fixture_claims()[0]["structured"], "bound": bound(exponent=[term(a="unknown")])},
               {**fixture_claims()[0]["structured"], "bound": bound(coefficient="0")},
               {**fixture_claims()[0]["structured"], "bound": bound(n_power="1/0")},
               {**fixture_claims()[0]["structured"], "bound": bound(exponent=[term(p="-1")])}]
        for index in range(3):
            for malformed in bad:
                claims = fixture_claims()
                claims[index]["structured"] = malformed
                with self.subTest(index=index, malformed=malformed):
                    self.rejection(claims)

    def test_domain_and_exact_index_mismatch_reject(self):
        for key in ("scope", "model", "version", "notation", "comparator"):
            claims = fixture_claims()
            claims[1]["structured"][key] = "other"
            self.rejection(claims)
        for index in range(3):
            claims = fixture_claims()
            claims[index]["score"] = {"numerator": "3", "denominator": "2"}
            self.rejection(claims)

    def test_missing_malformed_or_negative_resource_indices_reject(self):
        for index in range(3):
            for score in (None, {}, {"numerator": "-1", "denominator": "1"},
                          {"numerator": "1", "denominator": "0"}, "positive_infinity"):
                claims = fixture_claims()
                if score is None:
                    claims[index].pop("score")
                else:
                    claims[index]["score"] = score
                with self.subTest(index=index, score=score):
                    self.rejection(claims)

    def test_manifest_syntax_and_missing_evidence_are_format_errors(self):
        for files in ({}, text_files({"proof.md": "only proof"}),
                      text_files({"submission.json": "{"}),
                      text_files({"submission.json": '{"a":1,"a":2}'})):
            receipt = admission.admission_receipt(effective_for(), files)
            self.assertEqual(receipt["outcome"], "format_rejected")
        claims = fixture_claims()
        claims[2]["evidence"] = ["missing.md"]
        self.rejection(claims)

    def test_masks_both_validity_only_and_score_only(self):
        claims = fixture_claims()
        claims[2].pop("structured")
        _, score = self.rejection(claims, {"scores": False, "validity": True})
        self.assertEqual(set(score), {"valid", "reason", "metrics"})
        receipt = admission.admission_receipt(effective_for(fields={"scores": True, "validity": False}), files_for(claims))
        with self.assertRaisesRegex(VerifierError, "score_only_claim_not_established"):
            admission.rejection_score(receipt)
        self.rejection(["Partial theorem."], {"scores": False, "validity": True})

    def test_optional_preserves_omission_and_unscored_legacy_absence(self):
        claims = fixture_claims()
        claims[2].pop("structured")
        for configure in (None, legacy_config):
            effective = effective_for("optional")
            if configure:
                configure(effective)
            self.assertEqual(admission.admission_receipt(effective, files_for(claims))["outcome"], "review")
            result = projection(fixture(claims=claims, configure=configure))
            self.assertTrue(result["valid"])
            self.assertIn("dcp_omission", result["metrics"])
            self.assertIsNone(projection(fixture(unscored=True, configure=configure))["scores"])

    def test_config_cannot_register_or_select_downgrade(self):
        required, optional = effective_for(), effective_for("optional")
        for selected in (False, True):
            effective = copy.deepcopy(required)
            effective["config"]["supported_policies"]["validity"].append(optional["config"]["supported_policies"]["validity"][0])
            if selected:
                effective["evaluation"]["policies"]["validity"] = optional["config"]["policies"]["validity"]
            effective["evaluation"], effective["policy_instructions"] = select_evaluation(effective["config"], effective["evaluation"])
            with self.assertRaisesRegex(VerifierError, "dcp_admission_policy"):
                admission.admission_receipt(effective, files_for())
        for value in (None, True, "REQUIRED", "ignored"):
            effective = copy.deepcopy(required)
            effective["config"]["policies"]["validity"]["structured_bounds"] = value
            with self.assertRaises(VerifierError):
                admission.admission_receipt(effective, files_for())
        effective = copy.deepcopy(required)
        effective["config"]["policies"]["validity"].pop("structured_bounds")
        with self.assertRaises(VerifierError):
            admission.admission_receipt(effective, files_for())

    def test_unexpected_verifier_io_and_integrity_errors_remain_errors(self):
        for code in ("unsafe_or_missing_file", "unsafe_submission_tree", "verifier_revision_mismatch",
                     "source_hash_mismatch", "policy_binding", "new_unclassified_error"):
            with patch.object(admission, "preflight_snapshot", side_effect=VerifierError(code)):
                with self.subTest(code=code), self.assertRaisesRegex(VerifierError, code):
                    admission.admission_receipt(effective_for(), files_for())
        files = files_for()
        files["proof.md"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(VerifierError, "source_hash_mismatch"):
            admission.admission_receipt(effective_for(), files)

    def test_receipt_replays_and_binds_exact_sources_verifier_policy_and_snapshot(self):
        claims = fixture_claims()
        claims[2].pop("structured")
        receipt, _ = self.rejection(claims)
        self.assertEqual(admission.verify_receipt(receipt), receipt)
        self.assertEqual(receipt["validator"]["verifier_implementation"], implementation())
        self.assertEqual(receipt["validator"]["sources"]["dcp_admission.py"], sha((ROOT / "dcp_admission.py").read_bytes()))
        for key, replacement in (("outcome", "review"), ("mode", "optional"), ("diagnostic", None),
                                 ("submission_sha256", "0" * 64)):
            changed = copy.deepcopy(receipt)
            changed[key] = replacement
            changed["sha256"] = digest({k: v for k, v in changed.items() if k != "sha256"})
            with self.assertRaisesRegex(VerifierError, "dcp_admission_receipt_mismatch"):
                admission.verify_receipt(changed)
        with patch.object(admission, "implementation", return_value={"changed": True}):
            with self.assertRaisesRegex(VerifierError, "dcp_admission_receipt_mismatch"):
                admission.verify_receipt(receipt)
        with self.assertRaisesRegex(VerifierError, "dcp_candidate_revision"):
            admission.admission_receipt(effective_for(), files_for(), "main")

    def test_exporter_closes_generic_intake_bypass_even_invalid_unscored_or_masked(self):
        cases = [{"claims": ["Partial theorem."]}, {"unscored": True},
                 {"claims": fixture_claims()[:1]}, {"unscored": True, "invalid": True},
                 {"unscored": True, "fields": {"scores": False, "validity": True}}]
        claims = fixture_claims()
        claims[2].pop("structured")
        cases += [{"claims": claims}, {"claims": claims, "invalid": True}]
        for kwargs in cases:
            record = fixture(mode="required", **kwargs)  # Generic library deliberately has no DCP hook.
            with self.subTest(kwargs=kwargs), self.assertRaises(admission.FormatRejection):
                projection(record)
        valid = projection(fixture(mode="required"))
        self.assertTrue(valid["valid"])
        self.assertIn("dcp", valid["metrics"])
        self.assertFalse(projection(fixture(mode="required", invalid=True))["valid"])

    def test_local_review_revalidates_before_provider(self):
        intake = fixture(mode="required", unscored=True)["data"]["phases"][0]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_json(root / "intake.json", intake)
            (root / "out.json").write_text("stale")
            with patch.object(pipeline, "review", side_effect=AssertionError("provider reached")):
                result = admission.main(["review-initial", "--intake", str(root / "intake.json"),
                    "--initial", str(root / "not-read.json"), "--out", str(root / "out.json")])
            self.assertEqual(result, 2)
            self.assertFalse((root / "out.json").exists())

    def test_prepared_intake_uses_only_frozen_checked_bytes(self):
        effective, files = effective_for(), files_for()
        original = copy.deepcopy(files)
        real = admission.intake_snapshot
        def intercept(config, root, *args, **kwargs):
            self.assertEqual(snapshot(root, config["config"]["limits"]), original)
            return real(config, root, *args, **kwargs)
        with patch.object(admission, "intake_snapshot", side_effect=intercept):
            intake = admission.prepare_intake(effective, files)
        self.assertEqual(intake["data"]["files"], original)

    def test_local_finalize_format_rejection_has_no_dossier_and_never_reads_model_phases(self):
        claims = fixture_claims()
        claims[1].pop("structured")
        receipt = admission.admission_receipt(effective_for(), files_for(claims))
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_json(root / "receipt.json", receipt)
            with patch.object(pipeline, "dossier", side_effect=AssertionError("fake dossier")):
                admission.finalize(root / "receipt.json", root / "missing-intake", root / "missing-initial",
                    root / "missing-review", root / "dossier.json", root / "score.json")
            self.assertFalse((root / "dossier.json").exists())
            self.assertFalse(json.loads((root / "score.json").read_text())["valid"])

    def test_local_finalize_exports_only_validated_projection_and_clears_on_failure(self):
        record = fixture(mode="required")
        intake, initial, review = record["data"]["phases"]
        receipt = admission.admission_receipt(intake["data"]["effective"], intake["data"]["files"])
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, value in (("receipt", receipt), ("intake", intake), ("initial", initial), ("review", review)):
                write_json(root / (name + ".json"), value)
            args = [root / (name + ".json") for name in ("receipt", "intake", "initial", "review", "dossier", "score")]
            admission.finalize(*args)
            self.assertEqual(json.loads((root / "score.json").read_text())["metrics"]["dcp"]["resources"],
                             projection(record)["metrics"]["dcp"]["resources"])
            with patch("export_metrics.projection", side_effect=VerifierError("failed_projection")):
                with self.assertRaisesRegex(VerifierError, "failed_projection"):
                    admission.finalize(*args)
            self.assertFalse((root / "score.json").exists())
            self.assertFalse((root / "dossier.json").exists())
            changed = fixture(mode="required", claims=fixture_claims()[:1])["data"]["phases"][0]
            write_json(root / "intake.json", changed)
            with self.assertRaises(admission.FormatRejection):
                admission.finalize(*args)
            self.assertFalse((root / "score.json").exists())

    def test_organizer_toggle_updates_all_policy_copies_and_only_one_supported_mode(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ("verifier.json", "benchmark.json"):
                (root / name).write_bytes((ROOT / name).read_bytes())
            for mode in ("optional", "required"):
                subprocess.run([sys.executable, str(ROOT / "configure_bounds.py"), "--root", str(root), "--mode", mode], check=True, capture_output=True)
                config = json.loads((root / "verifier.json").read_text())
                benchmark = json.loads((root / "benchmark.json").read_text())
                policy = {"version": "dcp-joint-bounds-v3", "structured_bounds": mode}
                self.assertEqual(config["policies"]["validity"], policy)
                self.assertEqual(benchmark["tracks"][0]["paretoPolicies"]["validity"], policy)
                self.assertEqual([p["selector"] for p in config["supported_policies"]["validity"]], [policy])

    def test_cli_rejection_success_infra_and_score_only_failure_clear_stale_outputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ("verifier.json", "benchmark.json", "rules.md"):
                (root / name).write_bytes((ROOT / name).read_bytes())
            candidate = root / "submission"
            candidate.mkdir()
            claims = fixture_claims()
            claims[1].pop("structured")
            for name, record in files_for(claims).items():
                (candidate / name).write_text(record["text"])
            args = ["intake", "--root", str(root), "--out", str(root / "intake.json"),
                    "--receipt", str(root / "receipt.json"), "--score", str(root / "score.json"),
                    "--github-output", str(root / "github-output")]
            with patch.object(admission, "intake_snapshot", side_effect=AssertionError("intake reached")):
                self.assertEqual(admission.main(args), 0)
            self.assertFalse(json.loads((root / "score.json").read_text())["valid"])
            self.assertFalse((root / "intake.json").exists())
            self.assertEqual((root / "github-output").read_text(), "outcome=format_rejected\n")
            evaluation = effective_for(fields={"scores": True, "validity": False})["evaluation"]
            self.assertEqual(admission.main(args + ["--evaluation", json.dumps(evaluation)]), 2)
            self.assertFalse((root / "score.json").exists())
            (root / "score.json").write_text("stale")
            with patch.object(admission, "snapshot", side_effect=VerifierError("unsafe_or_missing_directory")):
                self.assertEqual(admission.main(args), 2)
            self.assertFalse((root / "score.json").exists())
            self.assertFalse((root / "receipt.json").exists())


if __name__ == "__main__":
    unittest.main()
