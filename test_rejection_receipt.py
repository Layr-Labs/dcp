"""Early rejection publishes an authenticated receipt, never claims or a dossier."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from llm_verifier.errors import VerifierError
from llm_verifier.files import write_json
from llm_verifier import pipeline
from dcp_admission import admission_receipt
from rejection_receipt import export_receipt
from test_dcp_admission import effective_for, files_for
from test_export_metrics import fixture_claims


class RejectionReceiptTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.path, self.out = self.root / "admission.json", self.root / "receipt.json"
        self.revision = "a" * 40
        self.context = {
            "version": 1, "api": "https://api-dev.yukon.org",
            "audience": "yukon:accepted-results:test", "submission_id": "submission",
            "benchmark_id": "benchmark", "challenge_id": None,
            "evaluation_id": "evaluation", "job_id": "job",
        }
        self.resolved = {
            "snapshot_id": "00000000-0000-4000-8000-000000000001",
            "consumer": {k: self.context[k] for k in
                         ("submission_id", "benchmark_id", "challenge_id", "evaluation_id", "job_id")},
        }
        claims = fixture_claims()
        claims[0].pop("structured")
        write_json(self.path, admission_receipt(effective_for(), files_for(claims), self.revision))

    def test_rejection_emits_only_authenticated_receipt_without_review(self):
        original = self.path.read_bytes()
        with patch("rejection_receipt.accepted.resolve", return_value=self.resolved) as resolve, patch.object(
                pipeline, "review", side_effect=AssertionError("judge called")):
            result = export_receipt(self.path, self.context, self.revision, self.out)
        resolve.assert_called_once_with(self.context, [])
        self.assertEqual(result, {"version": 1, "snapshot_id": self.resolved["snapshot_id"]})
        self.assertEqual(json.loads(self.out.read_text()), result)
        self.assertEqual(self.path.read_bytes(), original)
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["admission.json", "receipt.json"])

    def test_valid_candidate_and_wrong_revision_never_resolve(self):
        with patch("rejection_receipt.accepted.resolve") as resolve:
            with self.assertRaisesRegex(VerifierError, "dcp_candidate_revision"):
                export_receipt(self.path, self.context, "b" * 40, self.out)
            write_json(self.path, admission_receipt(effective_for(), files_for(), self.revision))
            with self.assertRaisesRegex(VerifierError, "dcp_format_rejection_required"):
                export_receipt(self.path, self.context, self.revision, self.out)
            resolve.assert_not_called()

    def test_failed_or_mismatched_resolution_clears_stale_output(self):
        wrong = copy.deepcopy(self.resolved)
        wrong["consumer"]["job_id"] = "another-job"
        for value in [wrong, {**self.resolved, "snapshot_id": "invalid"}]:
            self.out.write_text("stale")
            with patch("rejection_receipt.accepted.resolve", return_value=value):
                with self.assertRaises(VerifierError):
                    export_receipt(self.path, self.context, self.revision, self.out)
            self.assertFalse(self.out.exists())
        self.out.write_text("stale")
        with patch("rejection_receipt.accepted.resolve", side_effect=VerifierError("unavailable")):
            with self.assertRaisesRegex(VerifierError, "unavailable"):
                export_receipt(self.path, self.context, self.revision, self.out)
        self.assertFalse(self.out.exists())

    def test_tampered_admission_never_resolves(self):
        receipt = json.loads(self.path.read_text())
        receipt["diagnostic"]["code"] = "fabricated"
        write_json(self.path, receipt)
        with patch("rejection_receipt.accepted.resolve") as resolve:
            with self.assertRaisesRegex(VerifierError, "dcp_admission_receipt_mismatch"):
                export_receipt(self.path, self.context, self.revision, self.out)
            resolve.assert_not_called()
