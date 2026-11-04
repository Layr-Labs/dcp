"""Protected DCP admission; format checks do not establish mathematical truth.

The generic verifier remains generic. Official DCP entrypoints use this gate
before review, and the exporter rechecks the exact accepted intake snapshot.
"""

import argparse
from contextlib import contextmanager
from copy import deepcopy
from fractions import Fraction
import os
import re
from pathlib import Path
import sys
import tempfile

from llm_verifier import pipeline
from llm_verifier.artifacts import implementation, intake_snapshot, preflight_snapshot, verify_intake
from llm_verifier.config import load_config, resolve_submission, verify_effective
from llm_verifier.errors import VerifierError
from llm_verifier.files import (clear_output, distinct_paths, outside, read_json,
                                relative, snapshot, validate_files, write_json)
from llm_verifier.jsonutil import canonical, digest, loads, sha
from llm_verifier.judgment import yukon
from llm_verifier.scoring import score_value
from llm_verifier.workflow import checkout_revision

from complexity_bounds import RESOURCES, resource_contract, reviewed_bound

from error_tolerance import CLAIM_INDEX, REVIEW_STANDARD, COUNT_STANDARD, PREVIOUS_TOLERANCE_STANDARD, reviewed_tolerance, tolerance_required

SAMPLE_STANDARD = "dcp-joint-bounds-v4"
PREVIOUS_STANDARD = "dcp-joint-bounds-v3"
LEGACY_STANDARD = "dcp-joint-bounds-v2"
SCORING_POLICY = {"version": "dcp-time-growth-v2"}
VALIDATOR = "dcp-structured-bounds-admission-v3"
VERIFIER_REVISION = "204fdf8fb640704da0a3972d97831de09bfb1c7a"

# Only errors reached while parsing inert submission declarations can be format
# rejections. Configuration, I/O, hash/pin and unexpected runtime errors fail.
CANDIDATE_CODES = frozenset({
    "object_fields", "bounded_text_required", "claim_count",
    "unsupported_submission_version", "structured_claim_object_required",
    "structured_claim_byte_limit", "canonical_rational_required",
    "reduced_rational_required", "unrepresentable_score",
    "claim_evidence_required", "claim_evidence_file_missing",
    "duplicate_claim_evidence", "unsafe_path", "invalid_json",
    "duplicate_json_key", "nonfinite_json", "invalid_unicode",
    "invalid_json_key", "invalid_json_type", "json_complexity_limit",
    "json_byte_limit",
})
GLOBAL_CANDIDATE_CODES = frozenset({
    "missing_submission_manifest", "claim_count", "score_below_minimum",
    "terminal_requires_maximization",
})
BOUND_CODES = frozenset({
    "dcp_bound_keys", "dcp_bound_rational", "dcp_bound_normalized_size",
    "dcp_bound_positive_coefficient", "dcp_bound_terms",
    "dcp_bound_unsupported_power", "dcp_bound_contract",
    "dcp_bound_growth_index_mismatch",
})


class FormatRejection(VerifierError):
    """A known candidate format failure, never an LLM judgment."""

    def __init__(self, code, *, resource=None, path=()):
        super().__init__(code)
        self.resource = resource
        self.path = tuple(path)

    def diagnostic(self):
        return {"code": self.args[0], "path": list(self.path),
                **({"resource": self.resource} if self.resource else {})}


def admission_mode(effective):
    """Read only the exact protected validity selector; legacy absence is optional."""
    verify_effective(effective)
    config, evaluation = effective["config"], effective["evaluation"]
    if (config["id"] != "dcp" or config.get("structured_claims") != "atomic-v1"
            or config.get("acceptance_policy", "atomic-claims-v1") != "atomic-claims-v1"
            or config["policies"]["scoring"] != SCORING_POLICY
            or evaluation["policies"]["scoring"] != SCORING_POLICY):
        raise VerifierError("dcp_admission_policy")
    selected, default = evaluation["policies"]["validity"], config["policies"]["validity"]
    if selected != default:
        raise VerifierError("dcp_admission_policy_override")
    if config["review_standard"] == LEGACY_STANDARD:
        if default != {"version": LEGACY_STANDARD}:
            raise VerifierError("dcp_admission_policy")
        return "optional"
    if (config["review_standard"] not in (REVIEW_STANDARD, COUNT_STANDARD, PREVIOUS_TOLERANCE_STANDARD, SAMPLE_STANDARD, PREVIOUS_STANDARD) or type(default) is not dict
            or set(default) != {"version", "structured_bounds"}
            or default["version"] != config["review_standard"]
            or type(default["structured_bounds"]) is not str
            or default["structured_bounds"] not in ("required", "optional")
            or len(config["supported_policies"]["validity"]) != 1
            or config["supported_policies"]["validity"][0]["selector"] != default):
        raise VerifierError("dcp_admission_policy")
    return default["structured_bounds"]


def validate_resource_claims(manifest, *, standard=REVIEW_STANDARD):
    """Check complete supported declarations without modifying or proving them."""
    claims = manifest.get("claims") if type(manifest) is dict else None
    if type(claims) is not list:
        raise FormatRejection("dcp_joint_resource_claims_required", path=("claims",))
    normalized = {}
    resource_names, contract = resource_contract(standard)
    for index, resource in enumerate(resource_names):
        path = ("claims", index)
        if index >= len(claims) or type(claims[index]) is not dict:
            raise FormatRejection("dcp_resource_claim_required", resource=resource, path=path)
        claim = claims[index]
        if "structured" not in claim:
            raise FormatRejection("dcp_structured_bound_required", resource=resource,
                                  path=(*path, "structured"))
        score = claim.get("score")
        if type(score) is not dict:
            raise FormatRejection("dcp_resource_growth_required", resource=resource,
                                  path=(*path, "score"))
        try:
            score_value(score)
        except VerifierError as error:
            if error.args[0] not in CANDIDATE_CODES:
                raise
            raise FormatRejection(error.args[0], resource=resource,
                                  path=(*path, "score")) from None
        if Fraction(int(score["numerator"]), int(score["denominator"])) < 0:
            raise FormatRejection("dcp_resource_growth_required", resource=resource,
                                  path=(*path, "score"))
        try:
            normalized[resource] = reviewed_bound(claim["structured"], score, contract=contract)
        except VerifierError as error:
            if error.args[0] not in BOUND_CODES:
                raise
            raise FormatRejection(error.args[0], resource=resource,
                                  path=(*path, "structured")) from None
    if tolerance_required(standard):
        try:
            reviewed_tolerance(manifest, standard=standard)
        except VerifierError as error:
            raise FormatRejection(error.args[0], resource="error_tolerance", path=("claims", 4)) from None
    return normalized


def validate_intake(intake):
    """Also gates generic-library dossiers before any DCP score can publish."""
    data = verify_intake(intake)
    mode = admission_mode(data["effective"])
    if mode == "required":
        validate_resource_claims(data["manifest"], standard=data["effective"]["config"]["review_standard"])
    return mode


@contextmanager
def frozen_candidate(files):
    # Snapshot exactly once from the candidate. Subsequent library preflight and
    # intake read an organizer-owned private copy, closing a local re-read race.
    with tempfile.TemporaryDirectory(prefix="dcp-admission-") as temporary:
        root = Path(temporary)
        for name, record in files.items():
            path = root / relative(name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(record["text"].encode("utf-8"))
        yield root


def _candidate_failure(error, *, standard=REVIEW_STANDARD):
    code = error.args[0]
    if code in GLOBAL_CANDIDATE_CODES or (
            code in CANDIDATE_CODES and error.path[:1] == ("submission.json",)):
        path = tuple(error.path)
        resource = None
        if len(path) >= 3 and path[:2] == ("submission.json", "claims"):
            index = path[2]
            if type(index) is int and 0 <= index < len(RESOURCES):
                resource = RESOURCES[index]
            elif index == CLAIM_INDEX and tolerance_required(standard):
                resource = "error_tolerance"
        return FormatRejection(code, resource=resource, path=path)
    return None


def preflight_files(effective, files):
    """Return a typed decision bound to original bytes; no network or provider."""
    mode = admission_mode(effective)
    validate_files(files, effective["config"]["limits"], empty=True)
    if not files and mode == "required":
        return mode, None, FormatRejection("missing_submission_manifest")
    failure, prepared = None, None
    with frozen_candidate(files) as root:
        try:
            prepared = preflight_snapshot(effective, root)
        except VerifierError as error:
            failure = _candidate_failure(error, standard=effective["config"]["review_standard"]) if mode == "required" else None
            if failure is None:
                raise
        if failure is None and mode == "required":
            try:
                validate_resource_claims(prepared["manifest"], standard=effective["config"]["review_standard"])
            except FormatRejection as error:
                failure = error
    if prepared is not None and canonical(prepared["files"]) != canonical(files):
        raise VerifierError("dcp_admission_snapshot_mismatch")
    return mode, prepared, failure


def validator_identity():
    root = Path(__file__).resolve().parent
    sources = {name: sha((root / name).read_bytes())
               for name in ("dcp_admission.py", "complexity_bounds.py", "error_tolerance.py", "tolerance_expression.py")}
    return {"version": VALIDATOR, "sources": sources, "source_sha256": digest(sources),
            "verifier_revision": VERIFIER_REVISION, "verifier_implementation": implementation()}


def admission_receipt(effective, files, revision="local-unasserted"):
    if type(revision) is not str or (revision != "local-unasserted" and not re.fullmatch(r"[0-9a-f]{40}", revision)):
        raise VerifierError("dcp_candidate_revision")
    mode, _prepared, failure = preflight_files(effective, files)
    result = {"version": VALIDATOR, "kind": "format-admission-not-mathematical-review",
              "outcome": "format_rejected" if failure else "review",
              "mode": mode, "validator": validator_identity(),
              "candidate_revision": revision,
              "validity_policy": effective["evaluation"]["policies"]["validity"],
              "config_sha256": digest(effective), "submission_sha256": digest(files),
              "snapshot": {"effective": effective, "files": files},
              "diagnostic": failure.diagnostic() if failure else None}
    result["sha256"] = digest(result)
    return result


def rejection_score(receipt):
    """Ordinary masked invalid output; deliberately no fake model dossier."""
    verify_receipt(receipt)
    if receipt["outcome"] != "format_rejected":
        raise VerifierError("dcp_format_rejection_required")
    d = receipt["diagnostic"]
    reason = "DCP format rejection [" + d["code"] + "]"
    if d.get("resource"):
        reason += " for " + d["resource"]
    resource_names, _ = resource_contract(receipt["snapshot"]["effective"]["config"]["review_standard"])
    reason += "; complete supported " + "/".join(resource_names) + " bounds are required"
    if tolerance_required(receipt["snapshot"]["effective"]["config"]["review_standard"]):
        reason += ", plus a reviewed error-tolerance expression and error model"
    # Preserve score-only fail-closed semantics from the generic verifier.
    result = yukon({"valid": False, "scores": None, "reason": reason},
                   receipt["snapshot"]["effective"]["evaluation"])
    result["metrics"] = {"dcp_admission": {
        "version": VALIDATOR, "kind": receipt["kind"], "outcome": "format_rejected",
        "receipt_sha256": receipt["sha256"], "candidate_revision": receipt["candidate_revision"],
        "validity_policy": receipt["validity_policy"], "config_sha256": receipt["config_sha256"],
        "submission_sha256": receipt["submission_sha256"], "diagnostic": receipt["diagnostic"],
        "validator_source_sha256": receipt["validator"]["source_sha256"],
        "verifier_revision": receipt["validator"]["verifier_revision"],
        "verifier_content_sha256": receipt["validator"]["verifier_implementation"]["content_sha256"]}}
    return result


def verify_receipt(receipt):
    if type(receipt) is not dict or set(receipt) != {
            "version", "kind", "outcome", "mode", "validator", "candidate_revision",
            "validity_policy", "config_sha256", "submission_sha256", "snapshot",
            "diagnostic", "sha256"}:
        raise VerifierError("dcp_admission_receipt")
    snap = receipt["snapshot"]
    if type(snap) is not dict or set(snap) != {"effective", "files"}:
        raise VerifierError("dcp_admission_receipt")
    rebuilt = admission_receipt(snap["effective"], snap["files"], receipt["candidate_revision"])
    if canonical(receipt) != canonical(rebuilt):
        raise VerifierError("dcp_admission_receipt_mismatch")
    return receipt


def prepare_intake(effective, files, *, context=None, accepted_results_context=None):
    _mode, _prepared, failure = preflight_files(effective, files)
    if failure:
        raise failure
    with frozen_candidate(files) as root:
        intake = intake_snapshot(effective, root, context,
                                 accepted_results_context=accepted_results_context)
    if canonical(intake["data"]["files"]) != canonical(files):
        raise VerifierError("dcp_admission_snapshot_mismatch")
    validate_intake(intake)
    return intake


def finalize(receipt_path, intake_path, initial_path, review_path, dossier_path, score_path):
    """The official local score entrypoint never publishes generic intermediate scores."""
    distinct_paths([receipt_path, intake_path, initial_path, review_path], [dossier_path, score_path])
    clear_output(score_path)
    clear_output(dossier_path)
    receipt = verify_receipt(read_json(receipt_path))
    if receipt["outcome"] == "format_rejected":
        write_json(score_path, rejection_score(receipt))
        return
    intake = read_json(intake_path)
    validate_intake(intake)
    for key in ("effective", "files"):
        if canonical(intake["data"][key]) != canonical(receipt["snapshot"][key]):
            raise VerifierError("dcp_admission_snapshot_mismatch")
    record = pipeline.dossier(intake, read_json(initial_path), read_json(review_path))
    from export_metrics import projection
    result = projection(record)
    write_json(dossier_path, record)
    write_json(score_path, result)


def configure_mode(config, benchmark, mode):
    """One organizer setting, synchronized across protected policy copies."""
    if mode not in ("required", "optional") or type(mode) is not str:
        raise VerifierError("dcp_admission_policy")
    config, benchmark = deepcopy(config), deepcopy(benchmark)
    policy = {"version": REVIEW_STANDARD, "structured_bounds": mode}
    config["review_standard"] = REVIEW_STANDARD
    config["policies"]["validity"] = policy
    requirement = ("Every submission, including partial/unscored or validity-only work, must contain "
                   "all four supported structured resource bounds (time, classical space, quantum space, "
                   "and samples) with exact nonnegative indices, plus a fifth reviewed error-tolerance "
                   "expression and error model with no numeric score. "
                   "Missing, malformed or unsupported declarations are format rejection, not unscored acceptance. "
                   if mode == "required" else
                   "The four resource structures are optional; scored results still require the fifth "
                   "error-tolerance expression and model without a score. Unsupported or absent resource forms receive an "
                   "explicit omission record after review. Separately scoped partial theorems may remain unscored. ")
    config["supported_policies"]["validity"] = [{"selector": policy, "instructions":
        "Apply rules.md to unconditional full-secret correctness and jointly charged worst-case resources. "
        + requirement + "Format admission does not prove a claim: establish all exact statements and declared "
        "structured objects for the same algorithm/configuration, domain, model and evidence. Never infer "
        "coefficients or normalization from prose or hints. Reject mathematical mismatches. "
        "The tolerance expression must use the fractional-tolerance-v1 fraction family in rules.md, with no Q or floor brackets; "
        "establish recovery with at most that fraction of malformed samples under the stated model, never a numeric tolerance score."}]
    if len(benchmark["tracks"]) != 1 or benchmark["tracks"][0]["name"] != "main":
        raise VerifierError("dcp_manifest_contract")
    benchmark["tracks"][0]["paretoPolicies"]["validity"] = policy
    return config, benchmark


def _protected_outputs(root, candidate, outputs):
    protected = [root / name for name in ("verifier.json", "benchmark.json", "rules.md",
                 "dcp_admission.py", "configure_bounds.py", "complexity_bounds.py", "error_tolerance.py", "tolerance_expression.py", "export_metrics.py")]
    for output in outputs:
        outside(output, candidate)
    distinct_paths(protected, outputs)
    for output in outputs:
        clear_output(output)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("preflight", "intake"):
        p = sub.add_parser(command)
        p.add_argument("--root", default=".")
        p.add_argument("--submission", default="submission")
        p.add_argument("--evaluation", default=os.environ.get("YUKON_EVALUATION"))
        p.add_argument("--candidate-revision")
        p.add_argument("--receipt", required=True)
        p.add_argument("--score", required=True)
        p.add_argument("--github-output")
        if command == "intake":
            p.add_argument("--out", required=True)
            p.add_argument("--accepted-results-context", default=os.environ.get("YUKON_ACCEPTED_RESULTS"))
    p = sub.add_parser("review-initial")
    p.add_argument("--intake", required=True)
    p.add_argument("--initial", required=True)
    p.add_argument("--out", required=True)
    p = sub.add_parser("finalize")
    for name in ("receipt", "intake", "initial", "initial-review", "dossier", "score"):
        p.add_argument("--" + name, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "finalize":
            finalize(args.receipt, args.intake, args.initial, args.initial_review, args.dossier, args.score)
            return 0
        if args.command == "review-initial":
            distinct_paths([args.intake, args.initial], [args.out])
            clear_output(args.out)
            intake = read_json(args.intake)
            validate_intake(intake)  # Before constructing any provider client.
            write_json(args.out, pipeline.review(intake, read_json(args.initial)))
            return 0
        root = Path(args.root)
        candidate = root / relative(args.submission)
        outputs = [args.receipt, args.score] + ([args.out] if args.command == "intake" else [])
        _protected_outputs(root, candidate, outputs)
        submission = resolve_submission(root, "verifier.json", args.submission)
        if submission != args.submission:
            raise VerifierError("dcp_submission_selector_unsupported")
        effective = load_config(root, "verifier.json", submission,
                                loads(args.evaluation) if args.evaluation else None)
        admission_mode(effective)  # Config faults are not candidate rejection.
        if args.candidate_revision:
            checkout_revision(root, args.candidate_revision)
        files = snapshot(candidate, effective["config"]["limits"])
        receipt = admission_receipt(effective, files, args.candidate_revision or "local-unasserted")
        write_json(args.receipt, receipt)
        if receipt["outcome"] == "format_rejected":
            write_json(args.score, rejection_score(receipt))
        elif args.command == "intake":
            accepted = loads(args.accepted_results_context) if args.accepted_results_context else None
            write_json(args.out, prepare_intake(effective, files, accepted_results_context=accepted))
        if args.github_output:
            with open(args.github_output, "a", encoding="utf-8") as stream:
                stream.write("outcome=" + receipt["outcome"] + "\n")
        print(canonical({k: receipt[k] for k in ("outcome", "mode", "diagnostic", "sha256")}).decode())
        return 0
    except VerifierError as error:
        print("DCP admission error: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
