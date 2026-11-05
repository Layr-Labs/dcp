"""Real offline DCP admission/producer outputs for Yukon parser qualification.

Review transport is scripted by the existing fixture helper. These are neither
live evaluations nor mathematical acceptance evidence. Each run gets a new dir.
"""
import argparse
import copy
import json
from pathlib import Path
import uuid
from unittest.mock import patch

from llm_verifier.artifacts import implementation
from llm_verifier.errors import VerifierError
from llm_verifier.jsonutil import sha

from dcp_admission import RESOURCES, admission_receipt, rejection_score
from export_metrics import projection
from test_dcp_admission import effective_for, files_for, legacy_config
from test_export_metrics import fixture, fixture_claims

ROOT = Path(__file__).resolve().parent


def generate(out):
    out.mkdir(parents=True, exist_ok=False)
    cases = []
    def save(name, value):
        (out / name).write_text(json.dumps(value, indent=2) + "\n")
    def rejected(name, claims, fields=None):
        receipt = admission_receipt(effective_for(fields=fields), files_for(claims))
        assert receipt["outcome"] == "format_rejected"
        save(name + "-receipt.json", receipt)
        case = {"id": name, "outcome": "format_rejected", "receiptPath": name + "-receipt.json"}
        try:
            case["output"] = rejection_score(receipt)
        except VerifierError as error:
            assert error.args[0] == "score_only_claim_not_established"
            case["error"] = error.args[0]
        cases.append(case)
    for i, resource in enumerate(RESOURCES):
        claims = fixture_claims()
        claims[i].pop("structured")
        rejected("required-missing-" + resource, claims)
    unknown = fixture_claims()
    unknown[0]["structured"]["bound"]["exponent"][0]["coefficient"] = "unknown"
    rejected("required-unknown-coefficient", unknown)
    rejected("required-partial", ["Offline partial theorem."])
    rejected("required-validity-only", ["Offline partial theorem."], {"scores": False, "validity": True})
    rejected("required-score-only", ["Offline partial theorem."], {"scores": True, "validity": False})
    ids = iter(uuid.UUID(int=i) for i in range(1, 100))
    with patch("time.time_ns", return_value=1793054400000000000), patch(
            "time.monotonic", return_value=1.0), patch("uuid.uuid4", side_effect=ids):
        def reviewed(name, **kwargs):
            dossier = fixture(**kwargs)
            receipt = admission_receipt(dossier["data"]["phases"][0]["data"]["effective"],
                                        dossier["data"]["phases"][0]["data"]["files"])
            assert receipt["outcome"] == "review"
            save(name + "-receipt.json", receipt)
            save(name + "-dossier.json", dossier)
            cases.append({"id": name, "outcome": "review", "output": projection(dossier),
                          "receiptPath": name + "-receipt.json", "dossierPath": name + "-dossier.json"})
        reviewed("required-supported", mode="required")
        reviewed("required-mathematical-rejection", mode="required", invalid=True)
        reviewed("optional-unknown-coefficient", claims=unknown)
        missing = fixture_claims()
        missing[2].pop("structured")
        reviewed("optional-missing-quantum", claims=missing)
        reviewed("optional-partial", unscored=True)
        reviewed("historical-v2-policy-optional", claims=missing, configure=legacy_config)
    sources = ["dcp_admission.py", "configure_bounds.py", "export_metrics.py", "complexity_bounds.py",
               "admission_fixtures.py", "test_dcp_admission.py", "test_export_metrics.py", "verifier.json",
               "benchmark.json", "rules.md", ".github/workflows/benchmark.yml"]
    result = {"kind": "offline-admission-and-scripted-review-fixtures-not-mathematical-acceptance",
              "verifierImplementation": implementation(),
              "producerSources": {name: sha((ROOT / name).read_bytes()) for name in sources}, "cases": cases}
    save("dcp-admission-fixtures.json", result)
    return out / "dcp-admission-fixtures.json"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    print(generate(parser.parse_args().out))
