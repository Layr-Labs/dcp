"""Generate reproducible cross-language fixtures through the real offline producer."""

import argparse
import hashlib
import json
from pathlib import Path
import uuid
from unittest.mock import patch

from llm_verifier.artifacts import implementation

from complexity_bounds import CONTRACT, normalize_bound
from export_metrics import projection
from test_export_metrics import bound, fixture, term, tolerance_claim


def claims_for(p, classical, quantum, samples="2"):
    n, d = p.split("/") if "/" in p else (p, "1")
    data = (("time", f"O(2^(n^({p})))", bound(exponent=[term(p=p, q="0")]), n, d),
            ("classical bits", f"O(n^{classical})", bound(n_power=classical), "0", "1"),
            ("qubits", f"O(n^{quantum})", bound(n_power=quantum), "0", "1"),
            ("samples", f"O(n^{samples})", bound(n_power=samples), "0", "1"))
    return [{"statement": f"Offline fixture only: algorithm A uses {expr} {name}; all four bounds hold jointly. Index {numerator}/{denominator}.",
             "score": {"numerator": numerator, "denominator": denominator},
             "evidence": ["proof.md"], "structured": {**CONTRACT, "bound": raw}}
            for name, expr, raw, numerator, denominator in data] + [tolerance_claim()]


def normalization_claims():
    claims = claims_for("1/2", "3", "2")
    claims[0]["statement"] = ("Offline fixture only: algorithm A has joint total work "
        "O(2^((1/2)*sqrt(n)*log2(n) - (1/3)*sqrt(log2(n))) * n^3 * (log2(n))^(2/3)); index 1/2.")
    claims[0]["structured"]["bound"] = bound(n_power="1", log_power="2/3", exponent=[
        term("2/4", "1/2", "1"), term("-1/3", "0", "1/2"), term("2", "0", "1")])
    return claims


def generate(out):
    out.mkdir(parents=True, exist_ok=True)
    cases = []
    # Independently selected orders: the balanced row wins no individual column.
    specifications = (("fast", "1/2", "4", "4"),
                      ("same-time-less-memory", "1/2", "3", "4"),
                      ("exact-tie", "1/2", "3", "4"),
                      ("slower-less-memory", "3/4", "2", "4"),
                      ("classical-best", "3/4", "1", "5"),
                      ("quantum-best", "3/4", "5", "1"),
                      ("balanced-no-column-win", "2/3", "3", "3"),
                      ("dominated", "1", "100", "100"))
    ids = iter(uuid.UUID(int=i) for i in range(1, 100))
    with patch("time.time_ns", return_value=1793054400000000000), patch(
            "time.monotonic", return_value=1.0), patch("uuid.uuid4", side_effect=ids):
        def add(name, **kwargs):
            dossier = fixture(**kwargs)
            output = projection(dossier)
            path = f"{name}-dossier.json"
            (out / path).write_text(json.dumps(dossier, indent=2) + "\n")
            cases.append({"id": name, "output": output, "dossierPath": path})

        for name, p, classical, quantum in specifications:
            add(name, claims=claims_for(p, classical, quantum,
                samples="3" if name == "balanced-no-column-win" else "2"))
        raw = claims_for("1/2", "3", "4")
        for claim in raw[:4]:
            claim.pop("structured")
        add("unstructured", claims=raw)
        unknown = claims_for("1/2", "3", "4")
        unknown[0]["structured"]["bound"]["exponent"][0]["coefficient"] = "unknown"
        add("unknown-exponent-coefficient", claims=unknown)
        add("rejected", claims=claims_for("1/2", "3", "4"), invalid=True)
        add("unscored", unscored=True)
        normalized_claims = normalization_claims()
        normalized_dossier = fixture(claims=normalized_claims)
        normalized_output = projection(normalized_dossier)
        (out / "normalization-dossier.json").write_text(json.dumps(normalized_dossier, indent=2) + "\n")
    root = Path(__file__).parent
    cases.append({"id": "historical-v2", "output": json.loads(
        (root / "tests/fixtures/historical-v2-score.json").read_text()),
        "dossierPath": "historical-v2-dossier.json"})
    raw_bounds = [
        bound(coefficient="99", exponent=[term("2/4", "1/2", "0")]),
        bound(n_power="-1", exponent=[term("3", "0", "1")]),
        bound(exponent=[term("1/2", "1/2", "-3/2"), term("1/2", "1/2", "-3/2"),
                        term("2", "1", "0"), term("-2", "1", "0")]),
        bound(exponent=[term("1", "0", "2")]),
        bound(exponent=[term("-1", "1", "0")], log_power="2/3"),
    ]
    result = {
        "kind": "offline-producer-fixtures-not-mathematical-acceptance",
        "contract": CONTRACT,
        "verifierImplementation": implementation(),
        "producerSources": {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
                            for p in ("export_metrics.py", "complexity_bounds.py", "verifier.json", "rules.md")},
        "cases": cases,
        "normalizationProjection": {"inputClaims": normalized_claims,
                                    "output": normalized_output,
                                    "dossierPath": "normalization-dossier.json"},
        "expectedEligibleIds": [row[0] for row in specifications],
        "expectedFrontierIds": ["same-time-less-memory", "exact-tie", "slower-less-memory",
                                "classical-best", "quantum-best", "balanced-no-column-win"],
        "expectedBestKeys": {"same-time-less-memory": ["time", "samples"], "exact-tie": ["time", "samples"],
                             "slower-less-memory": ["samples"], "classical-best": ["classical_space", "samples"],
                             "quantum-best": ["quantum_space", "samples"], "balanced-no-column-win": []},
        "normalizationCases": [{"input": b, "expected": normalize_bound(b)} for b in raw_bounds],
    }
    (out / "historical-v2-dossier.json").write_bytes((root / "tests/fixtures/historical-v2-dossier.json").read_bytes())
    target = out / "yukon-producer-fixtures.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    return target


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    print(generate(parser.parse_args().out))
