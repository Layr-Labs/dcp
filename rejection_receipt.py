"""Bind a hosted format rejection to Yukon's authenticated receipt, without review."""
import argparse
import os
import re
from llm_verifier import accepted
from llm_verifier.errors import VerifierError
from llm_verifier.files import clear_output, read_json, write_json
from llm_verifier.jsonutil import canonical, loads
from llm_verifier.prior import consumer_key
from dcp_admission import preflight_files, verify_receipt


def export_receipt(receipt_path, context, revision, output):
    clear_output(output)
    receipt = verify_receipt(read_json(receipt_path))
    if (not re.fullmatch(r"[0-9a-f]{40}", revision)
            or receipt["candidate_revision"] != revision):
        raise VerifierError("dcp_candidate_revision")
    if receipt["outcome"] != "format_rejected":
        raise VerifierError("dcp_format_rejection_required")
    identity = accepted.context_identity(context)
    snap = receipt["snapshot"]
    _, prepared, _ = preflight_files(snap["effective"], snap["files"])
    # Only a generically valid manifest can supply prior references. Candidate
    # text is never evaluated or used to select a network endpoint.
    requested = prepared["manifest"].get("prior_results", []) if prepared else []
    resolved = accepted.resolve(context, requested)
    if canonical(consumer_key(resolved.get("consumer"))) != canonical(consumer_key(identity)):
        raise VerifierError("prior_consumer_binding")
    snapshot_id = resolved.get("snapshot_id")
    if type(snapshot_id) is not str or not re.fullmatch(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", snapshot_id):
        raise VerifierError("prior_snapshot_identity")
    result = {"version": 1, "snapshot_id": snapshot_id}
    write_json(output, result)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--admission", required=True)
    parser.add_argument("--candidate-revision", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    export_receipt(args.admission, loads(os.environ["YUKON_ACCEPTED_RESULTS"], 16384),
                   args.candidate_revision, args.out)
