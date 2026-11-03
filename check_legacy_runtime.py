"""Offline compatibility test: the original pinned verifier must fail closed for structured bounds."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from test_export_metrics import fixture

ROOT = Path(__file__).resolve().parent


def check(legacy_src):
    environment = {**os.environ, "PYTHONPATH": str(legacy_src.resolve())}
    identity = subprocess.run(
        [sys.executable, "-c", "import json; from llm_verifier.artifacts import implementation; print(json.dumps(implementation()))"],
        env=environment, capture_output=True, text=True, check=True)
    historical = json.loads((ROOT / "tests/fixtures/historical-v2-dossier.json").read_text())
    expected = historical["data"]["phases"][0]["data"]["implementation"]
    assert json.loads(identity.stdout) == expected, "Provide the exact original verifier 6903229 source"
    static = subprocess.run([sys.executable, "-m", "llm_verifier", "check", "--root", str(ROOT)],
                            env=environment, capture_output=True, text=True)
    assert static.returncode != 0, "Old verifier unexpectedly accepted the new config"
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        dossier, score = root / "dossier.json", root / "score.json"
        dossier.write_text(json.dumps(fixture()))
        score.write_text('{"valid":true,"scores":[0],"metrics":{"dcp":{"version":"dcp-bounds-v4"}}}')
        result = subprocess.run([sys.executable, str(ROOT / "export_metrics.py"),
                                 "--dossier", str(dossier), "--out", str(score)],
                                env=environment, capture_output=True, text=True)
        assert result.returncode != 0 and "dcp_structured_verifier_required" in result.stderr, result.stderr
        assert not score.exists(), "Unsupported runtime left a publishable stale score"
    print("PASS: exact pinned verifier rejects current config and export; stale score removed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--legacy-src", type=Path, required=True)
    check(parser.parse_args().legacy_src)
