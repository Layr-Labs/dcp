"""Real generic derivation preparation with synthetic accepted claim artifacts."""

from copy import deepcopy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

try:
    from llm_verifier import derivation
except ImportError:
    derivation = None
from llm_verifier import pipeline, structured_claims
from llm_verifier.artifacts import intake_snapshot
from llm_verifier.config import load_config, select_evaluation
from llm_verifier.errors import VerifierError
from llm_verifier.files import write_json
from llm_verifier.jsonutil import canonical, digest, sha
from llm_verifier.provider import HttpResponse, HttpTransport
from llm_verifier.simulation import ScriptedProvider
from score_derivation import SCORING_POLICY, RETAINED_VALIDITY, projection
from test_export_metrics import fixture_claims

ROOT = Path(__file__).resolve().parent


def uid(n):
    return f"00000000-0000-4000-8000-{n:012x}"


def descriptor(valid=True):
    def evidence(n):
        return {
            "result_id": uid(n),
            "evaluation_id": uid(n + 1),
            "policy_version_id": uid(n + 2),
            "source_ref": "b" * 40,
            "job_id": uid(n + 3),
            "commit_sha": "a" * 40,
        }

    return {
        "version": "yukon-retained-result-v1",
        "benchmark_id": uid(1),
        "submission_id": uid(2),
        "candidate_key": "digest:" + "b" * 64,
        "packet_id": uid(3),
        "score": evidence(10),
        "validity": {**evidence(20), "valid": valid},
        "destination": {
            "job_id": uid(30),
            "evaluation_id": uid(31),
            "packet_id": uid(32),
            "source_ref": "c" * 40,
        },
    }


def archive(root, id, name, file, value):
    raw = canonical(value) + b"\n"
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(file, raw)
    content = buffer.getvalue()
    root.mkdir(exist_ok=True)
    (root / (id + ".zip")).write_bytes(content)
    return {
        "repository": "synthetic/dcp",
        "run_id": "123",
        "run_attempt": "1",
        "artifact_id": id,
        "artifact_name": name,
        "archive_sha256": sha(content),
        "path": file,
        "file_sha256": sha(raw),
    }


@unittest.skipIf(
    derivation is None, "separate pinned derivation CI requires the new verifier"
)
class DerivationIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.candidate = self.root / "submission"
        self.candidate.mkdir()
        self.selected = descriptor()
        claims = fixture_claims()
        claims[4]["structured"].update(
            version="dcp-error-tolerance-v1", expression="Q/100"
        )
        claims[4][
            "statement"
        ] = "The same algorithm tolerates floor(Q/100) malformed samples under the stated error model."
        write_json(
            self.candidate / "submission.json",
            {
                "version": 1,
                "title": "Synthetic derivation test",
                "claims": claims,
                "experiments": [],
            },
        )
        (self.candidate / "proof.md").write_text(
            "Synthetic source evidence; no mathematical acceptance."
        )
        effective = load_config(ROOT, "verifier.json", "submission")
        config = effective["config"]
        config["policies"]["scoring"] = {"version": "dcp-time-growth-v2"}
        config["review_standard"] = RETAINED_VALIDITY["version"]
        config["policies"]["validity"] = deepcopy(RETAINED_VALIDITY)
        config["supported_policies"]["validity"] = [
            {
                "selector": deepcopy(RETAINED_VALIDITY),
                "instructions": "Synthetic v6 fixture.",
            }
        ]
        effective["evaluation"], effective["policy_instructions"] = select_evaluation(
            config
        )
        context = {
            "kind": "github-actions",
            "candidate_revision": "a" * 40,
            "run_id": "123:1",
        }
        old = intake_snapshot(effective, self.candidate, context)
        initial = pipeline.execute(old)
        decision = {
            "kind": "judgment",
            "requests": [],
            "judgment": {
                "valid": True,
                "scores": None,
                "reason": "Synthetic fixture only",
                "evidence_refs": ["source:proof.md"],
                "review_standard": RETAINED_VALIDITY["version"],
                "structured_claims_sha256": digest(
                    structured_claims.records(old["data"])
                ),
            },
        }
        response = {
            "id": "fixture",
            "object": "chat.completion",
            "model": "fixture-model",
            "choices": [
                {
                    "finish_reason": "stop",
                    "message": {"role": "assistant", "content": json.dumps(decision)},
                }
            ],
        }
        with patch.dict(
            "os.environ", {"OPENAI_API_KEY": "fixture-not-a-key"}
        ), patch.object(
            HttpTransport,
            "request",
            return_value=HttpResponse(200, canonical(response)),
        ):
            review = pipeline.review(old, initial)
        self.dossier = pipeline.dossier(old, initial, review)
        bundle = pipeline.export_results(self.dossier)
        self.archives = self.root / "archives"
        refs = {
            "intake": archive(self.archives, "101", "llmv-intake", "intake.json", old),
            "accepted_results": archive(
                self.archives,
                "102",
                "verifier-accepted-results",
                "accepted-results.json",
                bundle,
            ),
        }
        raw = (ROOT / "derivation.json").read_bytes()
        (self.root / "derivation.json").write_bytes(raw)
        self.plan = {
            "version": "score-derivation-plan-v1",
            "config_sha256": sha(raw),
            "entries": [
                {
                    "origin": {
                        k: v for k, v in self.selected.items() if k != "destination"
                    },
                    "action": "derive",
                    "reason": "Synthetic representation test.",
                    "source_files_sha256": old["bindings"]["submission"],
                    "artifacts": refs,
                }
            ],
        }
        write_json(self.root / "reorg/score-derivation-plan.json", self.plan)
        self.evaluation = {
            "policies": {"scoring": SCORING_POLICY, "validity": RETAINED_VALIDITY},
            "fields": {"scores": True, "validity": False},
            "retained_result": self.selected,
        }
        self.context = {
            "kind": "github-actions",
            "candidate_revision": "d" * 40,
            "verifier_revision": "e" * 40,
            "run_id": "200:1",
            "repository": "synthetic/dcp",
            "score_path": ".yukon/score.json",
        }

    def intake(self):
        return derivation.prepare(
            self.root,
            "derivation.json",
            "submission",
            self.evaluation,
            self.context,
            self.archives,
        )

    def result(
        self, *, status="derived", fraction="1/100", claim="claim:4", mocked_http=False
    ):
        intake = self.intake()
        text = derivation.sources(intake)[claim]
        script = {
            "status": status,
            "payload": {"fraction": fraction} if status == "derived" else None,
            "reason": "Synthetic representation outcome.",
            "source_refs": [
                {
                    "source": claim,
                    "sha256": sha(text.encode()),
                    "start_line": 1,
                    "end_line": len(text.split("\n")),
                    "quote": text,
                }
            ],
        }
        if mocked_http:
            response = {
                "id": "fixture",
                "object": "chat.completion",
                "model": "fixture-model",
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {"role": "assistant", "content": json.dumps(script)},
                    }
                ],
            }
            with patch.dict(
                "os.environ", {"OPENAI_API_KEY": "fixture-not-a-key"}
            ), patch.object(
                HttpTransport,
                "request",
                return_value=HttpResponse(200, canonical(response)),
            ):
                return derivation.review(intake)
        return derivation.review(
            intake,
            provider=ScriptedProvider(intake["data"]["config"]["provider"], script),
        )

    def test_preserves_originals_and_publishes_no_new_validity(self):
        result = self.result()
        output = projection(result, preview=True)["score_preview"]
        from export_metrics import projection as ordinary

        old = ordinary(self.dossier)
        self.assertNotIn("valid", output)
        self.assertEqual(output["scores"], old["scores"])
        self.assertEqual(output["derived_from"], self.selected)
        self.assertEqual(output["metrics"]["dcp_original"], old["metrics"])
        target = output["metrics"]["dcp_error_tolerance"]
        self.assertEqual(target["expression"], "1/100")
        self.assertEqual(
            target["context"], old["metrics"]["dcp_error_tolerance"]["context"]
        )
        self.assertEqual(
            target["intake_sha256"], output["metrics"]["dcp"]["intake_sha256"]
        )
        self.assertEqual(
            target["dossier_sha256"], output["metrics"]["dcp"]["dossier_sha256"]
        )
        for key, value in old["metrics"]["dcp"]["resources"].items():
            new = output["metrics"]["dcp"]["resources"][key]
            self.assertEqual(
                {k: v for k, v in new.items() if k != "source_sha256"},
                {k: v for k, v in value.items() if k != "source_sha256"},
            )
        with self.assertRaises(VerifierError):
            projection(result)

    def test_stronger_fraction_fails_even_if_reviewer_proposes_it(self):
        with self.assertRaises(VerifierError):
            projection(self.result(fraction="1/10"), preview=True)

    def test_missing_tolerance_citation_fails(self):
        with self.assertRaises(VerifierError):
            projection(self.result(claim="claim:0"), preview=True)

    def test_changed_candidate_fails_before_review(self):
        (self.candidate / "proof.md").write_text("changed")
        with self.assertRaises(VerifierError):
            self.intake()

    def test_stale_selected_packet_fails_before_review(self):
        self.evaluation["retained_result"]["packet_id"] = uid(999)
        with self.assertRaises(VerifierError):
            self.intake()

    def test_changed_archive_fails_before_review(self):
        (self.archives / "101.zip").write_bytes(b"not the original archive")
        with self.assertRaises(VerifierError):
            self.intake()

    def test_unsupported_keeps_original_scores_and_count_metrics(self):
        output = projection(self.result(status="unsupported"), preview=True)[
            "score_preview"
        ]
        self.assertEqual(
            output["metrics"]["dcp_error_tolerance"]["version"],
            "reviewed-expression-v1",
        )
        self.assertEqual(
            output["metrics"]["dcp_error_tolerance"]["expression"], "Q/100"
        )
        self.assertEqual(output["scores"], [1 / 3])
        self.assertNotIn("valid", output)

    def test_rejected_origin_does_not_call_provider(self):
        self.selected["validity"]["valid"] = False
        self.plan["entries"][0].update(action="not_applicable", artifacts=None)
        self.plan["entries"][0]["origin"] = deepcopy(
            {k: v for k, v in self.selected.items() if k != "destination"}
        )
        write_json(self.root / "reorg/score-derivation-plan.json", self.plan)
        with patch.object(
            HttpTransport,
            "request",
            side_effect=AssertionError("must not call provider"),
        ):
            result = derivation.review(self.intake())
        output = projection(result, preview=True)["score_preview"]
        self.assertIsNone(output["scores"])
        self.assertNotIn("valid", output)

    def test_extra_payload_fields_are_rejected(self):
        config = derivation.normalize_config(
            json.loads((ROOT / "derivation.json").read_text())
        )
        from llm_verifier.derivation_schema import compile_schema, validate_value

        with self.assertRaises(VerifierError):
            validate_value(
                compile_schema(config["payload_schema"]),
                {"fraction": "1/100", "error_model": "stronger"},
            )

    def hosted_case(self, *, simulation=False):
        from tools.derivation_profile import (
            VERSION,
            VERIFIER_REVISION,
            ORDINARY_REVISION,
            file_hash,
        )

        self.context.update(verifier_revision=VERIFIER_REVISION)
        result = self.result(mocked_http=not simulation)
        intake = result["data"]["intake"]
        config = {
            "review_standard": RETAINED_VALIDITY["version"],
            "policies": {"scoring": SCORING_POLICY, "validity": RETAINED_VALIDITY},
        }
        write_json(self.root / "verifier.json", config)
        write_json(
            self.root / "benchmark.json",
            {"tracks": [{"paretoPolicies": config["policies"]}]},
        )
        (self.root / "rules.md").write_text("Synthetic protected rules fixture.")
        (self.root / "reorg/ordinary-benchmark.yml").write_text(
            "Synthetic ordinary workflow fixture."
        )
        write_json(self.root / "reorg/score-derivation-report.json", {})
        names = (
            "derivation.json",
            "verifier.json",
            "rules.md",
            "reorg/ordinary-benchmark.yml",
            "reorg/score-derivation-plan.json",
            "reorg/score-derivation-report.json",
        )
        write_json(
            self.root / "score-derivation-profile.json",
            {
                "version": VERSION,
                "verifier_revision": VERIFIER_REVISION,
                "ordinary_verifier_revision": ORDINARY_REVISION,
                "ordinary_source_ref": "b" * 40,
                "files": {name: file_hash(self.root / name) for name in names},
                "retained_submission_ids": [uid(2)],
                "ordinary_submission_ids": [],
                "excluded_submission_ids": [],
            },
        )
        directory = self.root / "delivery"
        directory.mkdir()
        paths = [
            directory / "fixture.whl",
            directory / "intake.json",
            directory / "derivation.json",
        ]
        paths[0].write_bytes(b"Inert wheel fixture; never installed or executed.")
        write_json(paths[1], intake)
        write_json(paths[2], result)
        descriptors = [
            {
                "id": str(201 + i),
                "name": name,
                "sha256": str(i + 1) * 64,
                "run_id": "200",
                "run_attempt": "1",
            }
            for i, name in enumerate(
                (
                    "llmv-derivation-package",
                    "llmv-derivation-intake",
                    "verifier-score-derivation",
                )
            )
        ]
        receipt = {
            "version": 1,
            "run_id": "200",
            "delivery_attempt": "2",
            "artifacts": [
                {
                    "artifact": descriptor,
                    "path": dest,
                    "files": {path.name: file_hash(path)},
                }
                for descriptor, dest, path in zip(
                    descriptors, ("wheel", "intake", "derivation"), paths
                )
            ],
        }
        write_json(directory / "receipt.json", receipt)
        env = {
            "GITHUB_RUN_ID": "200",
            "GITHUB_RUN_ATTEMPT": "2",
            "GITHUB_SHA": "d" * 40,
            "GITHUB_REPOSITORY": "synthetic/dcp",
            "LLMV_REVIEW_RUN_ID": "200",
            "LLMV_REVIEW_RUN_ATTEMPT": "1",
            "LLMV_EXPECTED_INTAKE": intake["sha256"],
        }
        env.update(
            {
                key: json.dumps(value)
                for key, value in zip(
                    (
                        "LLMV_PACKAGE_ARTIFACT",
                        "LLMV_INTAKE_ARTIFACT",
                        "LLMV_DERIVATION_ARTIFACT",
                    ),
                    descriptors,
                )
            }
        )
        args = (
            paths[1],
            paths[2],
            paths[0],
            directory / "score.json",
            directory / "lineage.json",
            directory / "receipt.json",
        )
        return args, env, receipt

    def test_hosted_delivery_preserves_review_attempt_on_consumer_rerun(self):
        from export_hosted_derivation import export

        args, env, _ = self.hosted_case()
        export(*args, env=env, root=self.root)
        score = json.loads(args[3].read_text())
        lineage = json.loads(args[4].read_text())
        self.assertNotIn("valid", score)
        self.assertEqual(score["derived_from"], self.selected)
        self.assertEqual(lineage["review_attempt"], "1")
        self.assertEqual(lineage["delivery_attempt"], "2")

    def test_hosted_wrong_run_or_head_leaves_no_output(self):
        from export_hosted_derivation import export

        args, env, _ = self.hosted_case()
        for key, value in (
            ("GITHUB_SHA", "f" * 40),
            ("GITHUB_RUN_ID", "999"),
            ("LLMV_REVIEW_RUN_ATTEMPT", "3"),
        ):
            args[3].write_text("stale")
            args[4].write_text("stale")
            with self.assertRaises(VerifierError):
                export(*args, env={**env, key: value}, root=self.root)
            self.assertFalse(args[3].exists())
            self.assertFalse(args[4].exists())

    def test_hosted_altered_transfer_receipt_or_simulation_cannot_publish(self):
        from export_hosted_derivation import export

        args, env, receipt = self.hosted_case(simulation=True)
        with self.assertRaisesRegex(VerifierError, "simulation"):
            export(*args, env=env, root=self.root)
        self.assertFalse(args[3].exists())
        receipt["artifacts"][1]["files"]["intake.json"] = "0" * 64
        write_json(args[5], receipt)
        with self.assertRaisesRegex(VerifierError, "transfer_receipt"):
            export(*args, env=env, root=self.root)
        self.assertFalse(args[3].exists())
        self.assertFalse(args[4].exists())


if __name__ == "__main__":
    unittest.main()
