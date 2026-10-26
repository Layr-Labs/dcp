"""Project accepted DCP statements from a trusted shared-verifier dossier.

This adds metadata only. Mathematical review and phase validation remain in
llm-verifier. A dossier must arrive through the organizer's artifact channel;
content hashes alone do not authenticate a reviewer.
"""

import argparse
from fractions import Fraction
from pathlib import Path

from llm_verifier import pipeline
from llm_verifier.artifacts import verify_envelope
from llm_verifier.errors import VerifierError
from llm_verifier.files import clear_output, read_json, write_json
from llm_verifier.jsonutil import canonical, digest

from complexity_bounds import CONTRACT, reviewed_bound

RESOURCES = ("time", "classical_space", "quantum_space")


def historical_projection(record, data, intake, config):
    """Unchanged v2 projection, replayed with its original verifier runtime."""
    expected = [r + "_growth" for r in RESOURCES]
    if (config["id"] != "dcp" or config["review_standard"] != "dcp-joint-bounds-v1"
            or [o["name"] for o in config["objectives"]] != expected
            or [o.get("score_source") for o in config["objectives"]]
            != [{"claim": i} for i in range(3)]
            or [o.get("score_minimum") for o in config["objectives"]]
            != [{"numerator": "0", "denominator": "1"}] * 3):
        raise VerifierError("dcp_objective_contract")
    result = dict(data["yukon_projection"])
    if result.get("scores") is not None:
        claims = intake["data"]["manifest"]["claims"]
        files = intake["data"]["files"]
        result["metrics"] = {"dcp": {
            "version": "dcp-bounds-v2",
            "format": "reviewed-mathematical-text",
            "intake_sha256": intake["sha256"],
            "dossier_sha256": record["sha256"],
            "resources": {resource: {
                "statement": claims[i]["statement"],
                "growth_index": claims[i]["score"],
                "source_sha256": data["score_records"][i]["source_sha256"],
                "evidence": {p: files[p]["sha256"] for p in claims[i]["evidence"]},
            } for i, resource in enumerate(RESOURCES)},
        }}
    return result


def structured_projection(record, data, intake, config):
    if (config["id"] != "dcp" or config["review_standard"] != "dcp-joint-bounds-v2"
            or config.get("structured_claims") != "atomic-v1"
            or config.get("acceptance_policy", "atomic-claims-v1") != "atomic-claims-v1"
            or [o["name"] for o in config["objectives"]] != ["time_growth"]
            or [o["direction"] for o in config["objectives"]] != ["-"]
            or [o.get("score_source") for o in config["objectives"]] != [{"claim": 0}]
            or [o.get("score_minimum") for o in config["objectives"]]
            != [{"numerator": "0", "denominator": "1"}]):
        raise VerifierError("dcp_objective_contract")
    result = dict(data["yukon_projection"])
    if result.get("scores") is None:
        return result
    if not data["judgment"]["valid"] or len(result["scores"]) != 1:
        raise VerifierError("dcp_atomic_acceptance_required")
    claims, files = intake["data"]["manifest"]["claims"], intake["data"]["files"]
    if len(claims) < 3 or any(type(c) is not dict for c in claims[:3]):
        raise VerifierError("dcp_joint_resource_claims_required")
    accepted = {r["claim"]: r for r in pipeline.accepted_structured_claims(record)}
    resources, retained, omitted = {}, {}, []
    for i, resource in enumerate(RESOURCES):
        claim = claims[i]
        score = claim.get("score")
        if (type(score) is not dict or set(score) != {"numerator", "denominator"}
                or Fraction(int(score["numerator"]), int(score["denominator"])) < 0):
            raise VerifierError("dcp_resource_growth_required")
        provenance = {
            "statement": claim["statement"],
            "source_sha256": digest({"source": {"claim": i}, "files": digest(files)}),
            "evidence": {p: files[p]["sha256"] for p in claim["evidence"]},
        }
        retained[resource] = {**provenance, "growth_index": score}
        if "structured" not in claim:
            omitted.append({"resource": resource, "reason": "missing_structured_bound"})
            continue
        expected = {"claim": i, "structured": claim["structured"], **provenance}
        if accepted.get(i) != expected:
            raise VerifierError("dcp_structured_review_binding")
        retained[resource]["structured"] = claim["structured"]
        try:
            bound = reviewed_bound(claim["structured"], score)
        except VerifierError as error:
            # A disagreement in scope/model/notation or the exact index is not
            # an unsupported expression: it contradicts the accepted contract.
            if str(error) in {"dcp_bound_contract", "dcp_bound_growth_index_mismatch"}:
                raise
            omitted.append({"resource": resource, "reason": str(error)})
            continue
        resources[resource] = {**provenance, "bound": bound}
    provenance = {"intake_sha256": intake["sha256"], "dossier_sha256": record["sha256"]}
    if omitted:
        # Preserve the reviewed joint claims without a usable v3 envelope.
        result["metrics"] = {"dcp_omission": {
            "version": CONTRACT["version"], "reason": "unsupported_structured_bounds",
            "details": omitted, **provenance, "resources": retained,
        }}
    else:
        result["metrics"] = {"dcp": {**CONTRACT, **provenance, "resources": resources}}
    return result


def projection(record):
    data = verify_envelope(record, "dossier")
    phases = data["phases"]
    if len(phases) not in (3, 5):
        raise VerifierError("dcp_dossier_phases")
    intake = phases[0]
    config = intake["data"]["effective"]["config"]
    if (config.get("structured_claims") == "atomic-v1"
            and not callable(getattr(pipeline, "accepted_structured_claims", None))):
        raise VerifierError("dcp_structured_verifier_required")
    options = ({"finalized_at_ns": data["finalized_at_ns"]}
               if "finalized_at_ns" in data else {})
    rebuilt = pipeline.dossier(*phases, **options)
    if canonical(rebuilt) != canonical(record):
        raise VerifierError("dcp_dossier_mismatch")
    if record["simulation"]:
        raise VerifierError("simulation_cannot_publish_score")
    if config["review_standard"] == "dcp-joint-bounds-v1":
        return historical_projection(record, data, intake, config)
    return structured_projection(record, data, intake, config)


def export(dossier_path, output):
    if Path(dossier_path).absolute() == Path(output).absolute():
        raise VerifierError("distinct_output_paths_required")
    clear_output(output)
    write_json(output, projection(read_json(dossier_path)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dossier", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    export(args.dossier, args.out)
