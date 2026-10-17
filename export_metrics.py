"""Project accepted DCP statements from a trusted shared-verifier dossier.

This adds metadata only. Mathematical review and phase validation remain in
llm-verifier. A dossier must arrive through the organizer's artifact channel;
content hashes alone do not authenticate a reviewer.
"""

import argparse
from pathlib import Path

from llm_verifier import pipeline
from llm_verifier.artifacts import verify_envelope
from llm_verifier.errors import VerifierError
from llm_verifier.files import clear_output, read_json, write_json
from llm_verifier.jsonutil import canonical

RESOURCES = ("time", "classical_space", "quantum_space")


def projection(record):
    data = verify_envelope(record, "dossier")
    phases = data["phases"]
    if len(phases) not in (3, 5):
        raise VerifierError("dcp_dossier_phases")
    rebuilt = pipeline.dossier(*phases)
    if canonical(rebuilt) != canonical(record):
        raise VerifierError("dcp_dossier_mismatch")
    if record["simulation"]:
        raise VerifierError("simulation_cannot_publish_score")
    intake = phases[0]
    config = intake["data"]["effective"]["config"]
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
