"""Prepare a protected v6-validity scoring profile without activating it.

The ordinary source is an exact organizer snapshot of the still-active v6
contract. New derivation files are overlaid separately; default main remains v7.
"""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
# Route validation runs before either verifier wheel is installed.
SCORING = {
    "version": "dcp-time-growth-fraction-v3",
    "retained_result": "yukon-retained-result-v1",
}
VALIDITY = {"version": "dcp-joint-bounds-v6", "structured_bounds": "required"}
VERIFIER_REVISION = "da594aad5166918d4dd7d71630e1e649521e1953"

PROFILE = "score-derivation-profile.json"
VERSION = "dcp-score-derivation-profile-v1"
ORDINARY_REVISION = "204fdf8fb640704da0a3972d97831de09bfb1c7a"
OVERLAY = (
    "score_derivation.py",
    "derivation.json",
    "select_scoring_route.py",
    "export_hosted_derivation.py",
    "derivation_hosted_helpers.py",
    "dcp_admission.py",
    "export_metrics.py",
    "error_tolerance.py",
    "tolerance_expression.py",
    "complexity_bounds.py",
    "test_export_metrics.py",
    "test_dcp_admission.py",
    "test_score_derivation.py",
    "test_derivation_integration.py",
    "tools/__init__.py",
    "tools/prepare_score_derivation_plan.py",
    "tools/derivation_profile.py",
    "tools/derivation-jobs.yml",
    ".github/workflows/score-derivation-tests.yml",
    "docs/score-derivation.md",
)


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_profile(root):
    root = Path(root)
    value = json.loads((root / PROFILE).read_text())
    required = {
        "derivation.json",
        "verifier.json",
        "rules.md",
        "reorg/ordinary-benchmark.yml",
        "reorg/score-derivation-plan.json",
        "reorg/score-derivation-report.json",
    }
    if (
        set(value)
        != {
            "version",
            "verifier_revision",
            "ordinary_verifier_revision",
            "ordinary_source_ref",
            "files",
            "retained_submission_ids",
            "ordinary_submission_ids",
            "excluded_submission_ids",
        }
        or value["version"] != VERSION
        or value["verifier_revision"] != VERIFIER_REVISION
        or value["ordinary_verifier_revision"] != ORDINARY_REVISION
        or set(value["files"]) != required
        or any(
            file_hash(root / name) != expected
            for name, expected in value["files"].items()
        )
    ):
        raise ValueError("invalid or changed DCP score-derivation profile")
    plan = json.loads((root / "reorg/score-derivation-plan.json").read_text())
    config = json.loads((root / "verifier.json").read_text())
    manifest = json.loads((root / "benchmark.json").read_text())
    if (
        config["policies"] != {"scoring": SCORING, "validity": VALIDITY}
        or config["review_standard"] != VALIDITY["version"]
        or manifest["tracks"][0]["paretoPolicies"] != config["policies"]
        or len(manifest["tracks"]) != 1
        or plan["config_sha256"] != value["files"]["derivation.json"]
        or not plan["entries"]
        or [entry["origin"]["submission_id"] for entry in plan["entries"]]
        != value["retained_submission_ids"]
    ):
        raise ValueError("DCP profile policy/plan mismatch")
    return value


def render_workflow(root):
    root = Path(root)
    ordinary = (root / "reorg/ordinary-benchmark.yml").read_text()
    header, jobs = ordinary.split("jobs:\n", 1)
    old = "    name: Check DCP bounds before paid review\n"
    if jobs.count(old) != 1 or ORDINARY_REVISION not in jobs:
        raise ValueError("unexpected ordinary DCP workflow")
    jobs = jobs.replace(
        old,
        old + "    needs: [route]\n    if: needs.route.outputs.route == 'ordinary'\n",
        1,
    )
    # The source tests run in CI. A materialized source keeps the complete old
    # v6 test corpus, plus the dedicated new-feature job at the derivation pin.
    return (
        header
        + "jobs:\n"
        + (root / "tools/derivation-jobs.yml")
        .read_text()
        .replace("@VERIFIER_REVISION@", VERIFIER_REVISION)
        + jobs
    )


def check(root):
    root = Path(root)
    read_profile(root)
    if (root / ".github/workflows/benchmark.yml").read_text() != render_workflow(root):
        raise ValueError("generated derivation workflow drift")


def materialize(root, ordinary, output, snapshot, artifact_index, archives, source_ref):
    from llm_verifier.config import load_config
    from llm_verifier.files import write_json
    from tools.prepare_score_derivation_plan import build
    import subprocess

    root, ordinary, output = (Path(p).resolve() for p in (root, ordinary, output))
    if (
        output.exists()
        or not output.parent.is_dir()
        or output.is_relative_to(root)
        or root.is_relative_to(output)
    ):
        raise ValueError("profile output must be a new separate directory")
    if not __import__("re").fullmatch(r"[0-9a-f]{40}", source_ref):
        raise ValueError("immutable ordinary source ref required")
    # Verify the supplied ordinary snapshot against the immutable Git tree in
    # the organizer checkout; never trust a directory label or manifest alone.
    tree = subprocess.run(
        ["git", "ls-tree", "-rz", "--full-tree", source_ref],
        cwd=root,
        check=True,
        capture_output=True,
    ).stdout
    expected = {}
    modes = {}
    for row in tree.split(b"\0"):
        if not row:
            continue
        meta, name = row.split(b"\t", 1)
        mode, kind, oid = meta.decode().split()
        name = name.decode()
        if mode not in ("100644", "100755") or kind != "blob":
            raise ValueError("ordinary snapshot contains unsupported file type")
        data = subprocess.run(
            ["git", "cat-file", "blob", oid], cwd=root, check=True, capture_output=True
        ).stdout
        expected[name] = data
        modes[name] = int(mode, 8) & 0o777
        path = ordinary / name
        if path.is_symlink() or not path.is_file() or path.read_bytes() != data:
            raise ValueError("ordinary source bytes mismatch: " + name)
    actual = {str(p.relative_to(ordinary)) for p in ordinary.rglob("*") if p.is_file()}
    if actual != set(expected):
        raise ValueError("ordinary source inventory mismatch")
    config = json.loads(expected["verifier.json"])
    if (
        config["policies"]["validity"] != VALIDITY
        or config["review_standard"] != VALIDITY["version"]
    ):
        raise ValueError("ordinary source must retain the active v6 validity contract")
    plan, report = build(
        snapshot, artifact_index, (root / "derivation.json").read_bytes(), archives
    )
    with tempfile.TemporaryDirectory(dir=output.parent) as temp:
        staging = Path(temp) / "source"
        # Construct from the already verified immutable Git bytes, so a local
        # snapshot change or directory symlink cannot enter the staged source.
        staging.mkdir()
        for name, data in expected.items():
            target = staging / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            target.chmod(modes[name])
        for name in OVERLAY:
            target = staging / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / name, target)
        old_selector = deepcopy(config["policies"]["scoring"])
        original = [
            p
            for p in config["supported_policies"]["scoring"]
            if p["selector"] == old_selector
        ]
        if len(original) != 1 or original[0]["selector"] == SCORING:
            raise ValueError("ambiguous ordinary scoring policy")
        config["policies"]["scoring"] = deepcopy(SCORING)
        config["supported_policies"]["scoring"].append(
            {**deepcopy(original[0]), "selector": deepcopy(SCORING)}
        )
        write_json(staging / "verifier.json", config)
        manifest = json.loads(expected["benchmark.json"])
        if len(manifest["tracks"]) != 1:
            raise ValueError("one track required")
        manifest["tracks"][0]["paretoPolicies"] = deepcopy(config["policies"])
        write_json(staging / "benchmark.json", manifest)
        (staging / "reorg").mkdir(exist_ok=True)
        (staging / "reorg/ordinary-benchmark.yml").write_bytes(
            expected[".github/workflows/benchmark.yml"]
        )
        write_json(staging / "reorg/score-derivation-plan.json", plan)
        write_json(staging / "reorg/score-derivation-report.json", report)
        names = (
            "derivation.json",
            "verifier.json",
            "rules.md",
            "reorg/ordinary-benchmark.yml",
            "reorg/score-derivation-plan.json",
            "reorg/score-derivation-report.json",
        )
        profile = {
            "version": VERSION,
            "verifier_revision": VERIFIER_REVISION,
            "ordinary_verifier_revision": ORDINARY_REVISION,
            "ordinary_source_ref": source_ref,
            "files": {name: file_hash(staging / name) for name in names},
            "retained_submission_ids": [
                e["origin"]["submission_id"] for e in plan["entries"]
            ],
            "ordinary_submission_ids": report["ordinary_submission_ids"],
            "excluded_submission_ids": report["excluded_submission_ids"],
        }
        write_json(staging / PROFILE, profile)
        (staging / ".github/workflows/benchmark.yml").write_text(
            render_workflow(staging)
        )
        # Add a notice rather than rewrite the original validity rules.
        with (staging / "README.md").open("a") as f:
            f.write(
                "\n## Retained-validity fractional metrics\n\nThis source keeps the v6 count-based input and validity contract. Scoring exports equivalent fractions for the table. Historical jobs use authenticated score derivation; see [the profile guide](docs/score-derivation.md). No new v7 validity policy is activated.\n"
            )
        load_config(staging, "verifier.json", "submission")
        check(staging)
        staging.rename(output)
    return profile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    for name in (
        "ordinary-source",
        "source-ref",
        "snapshot",
        "artifact-index",
        "archive-root",
        "out",
    ):
        parser.add_argument("--" + name)
    args = parser.parse_args()
    if args.check:
        check(ROOT)
        return
    if any(
        getattr(args, n.replace("-", "_")) is None
        for n in (
            "ordinary-source",
            "source-ref",
            "snapshot",
            "artifact-index",
            "archive-root",
            "out",
        )
    ):
        parser.error("all materialization inputs are required")
    materialize(
        ROOT,
        args.ordinary_source,
        args.out,
        json.loads(Path(args.snapshot).read_text()),
        json.loads(Path(args.artifact_index).read_text()),
        args.archive_root,
        args.source_ref,
    )


if __name__ == "__main__":
    main()
