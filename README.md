# DCP challenge

Find and prove better algorithms for the Dihedral Coset Problem, aiming at total
work 2^{O(n^{1/3})}, where n = ceil(log₂ N). Read [rules.md](rules.md) for the
input, charged cost model and joint proof obligations. Participants edit only
`submission/`. The example retains its exhaustive-search proof and original
statements: O(N n⁴) work, O(n²) classical bits and O(n²) qubits. Its new
structured declarations require a new review; historical acceptance is not
acceptance of the added fields.

The Pareto backend minimizes **one numeric time growth index**, sourced from
claim 0. All three resource claims, indices and evidence remain mandatory and
are reviewed atomically for one algorithm/configuration. The baseline time
score is `[1]`. Index zero includes polynomial and quasipolynomial guarantees;
equal indices do not imply equivalent full bounds. Promotion remains manual.

## Reviewed structured metrics

`export_metrics.py` reconstructs the shared-verifier dossier before producing
`metrics.dcp` version `dcp-bounds-v3`. The protected verifier configuration opts
into `structured_claims: "atomic-v1"`. Each resource claim declares a structured
object containing the fixed comparison context and an exact rational bound.
The reviewer must acknowledge the digest of **all** structured claim records,
including both memory claims. The exporter requires atomic acceptance and
matches each accepted statement, structured object, source hash and evidence.

The v3 envelope has exactly these fields:

```json
{
  "version": "dcp-bounds-v3",
  "comparator": "asymptotic-v1",
  "scope": "dcp-cyclic-group-order",
  "model": "dcp-uniform-clifford-t-bit-operations-v1",
  "notation": "big-o",
  "intake_sha256": "<64 lowercase hex>",
  "dossier_sha256": "<64 lowercase hex>",
  "resources": {
    "time": "<resource>",
    "classical_space": "<resource>",
    "quantum_space": "<resource>"
  }
}
```

Each resource has exactly `statement`, `bound`, `source_sha256`, and `evidence`.
`statement` is verbatim; `evidence` maps paths relative to the submission root
(such as `proof.md`) to snapshot SHA-256 hashes. The source digest covers the
claim index and complete source snapshot using the shared verifier's binding.
The dossier retains all three exact growth indices and original structured data.
The table's version/comparator/scope/model/notation must match the envelope.

The bound family is C·2^(Σ a·n^p·(log₂ n)^q)·n^r·(log₂ n)^s, with the exact keys,
limits and examples in [rules.md](rules.md#structured-reviewed-envelopes-dcp-bounds-v3).
`complexity_bounds.py` combines equal terms, folds 2^(a log₂ n) into n^a,
reduces rational strings and checks the exact growth index. Big-O ignores only
the outer C; unknown coefficients inside an exponent are never guessed.
No expression is extracted from prose, LaTeX, hints or scores.

If a valid reviewed claim has no supported structured representation, the
exporter emits **no `metrics.dcp`**. Instead `metrics.dcp_omission` contains the
target version, explicit per-resource reasons, intake/dossier hashes and all
three original statements, indices, evidence and any declared structured data.
The entire joint row is omitted from the structured frontier. Rejected,
unscored and validity-only results have no bound metrics. Simulations, stale or
mismatched review bindings and contradictory context/index data cannot publish.

Hashes and digest acknowledgments establish integrity, not reviewer identity
or mathematical truth. Accept dossiers only through the trusted organizer
workflow/artifact channel. Offline fixture reviews are scripted tests, not
proof certification.

## Pinned verifier and local validation

This challenge pins `Layr-Labs/llm-verifier` at
`204fdf8fb640704da0a3972d97831de09bfb1c7a` ([dependency PR #21](https://github.com/Layr-Labs/llm-verifier/pull/21)).
Its structured-claim review binding is used by both workflow callers and the
same-run verifier wheel consumed by the exporter. Participants and solver
launchers should use the [same-revision solver guide](https://github.com/Layr-Labs/llm-verifier/blob/204fdf8fb640704da0a3972d97831de09bfb1c7a/docs/solving.md).

With access to the verifier repository and Python 3.11+:

```sh
python3 -m venv .venv
.venv/bin/pip install 'git+https://github.com/Layr-Labs/llm-verifier.git@204fdf8fb640704da0a3972d97831de09bfb1c7a'
.venv/bin/llm-verifier check --root .
.venv/bin/python -m unittest -v
.venv/bin/python offline_fixtures.py --out .work/yukon-fixtures
.venv/bin/python check_legacy_runtime.py --legacy-src /absolute/path/to/verifier-6903229/src
```

For development against the identical verifier source, set `PYTHONPATH` to its
`src` directory and use `python -m llm_verifier` and `python` for these commands.

The tests use the actual intake, review, dossier and export implementation with
only the HTTP transport replaced by an inert response. They run no model,
Docker experiment or hosted evaluation. `offline_fixtures.py` creates actual
producer outputs and their complete dossiers for cross-language Yukon tests,
including equal-time and slower-time/lower-memory cases, ties, rejection and
unsupported forms. These are explicitly **offline fixtures**, not live data.

After local phase execution, run the actual producer with:

```sh
python export_metrics.py --dossier .yukon/dossier.json --out .yukon/score.json
```

The original verifier `69032292f5c8a788d7524a9339fe1c7b79bf3e44` cannot execute
this opt-in contract. The exporter fails with `dcp_structured_verifier_required`
and clears stale output under that runtime; `check_legacy_runtime.py` tests this
against its exact original source. Keep both workflow and implementation pins
identical when upgrading. The metrics job consumes that same run's wheel and
dossier and retains the `dcp-score` artifact selection.

Push and PR checker CI does not run model review. The Benchmark workflow remains
dispatch-only; local checks do not perform hosted judging, import or rebind.
The existing three-objective track requires a separately authorized replacement;
its mode/objective list cannot be changed by reorg. Fresh review of the new
structured baseline is required before it can populate the v3 frontier.

## Historical v2 evidence

Existing v2 records and their `[time, classical_space, quantum_space]` scores
remain historical and unchanged. The exporter retains their original branch;
it does not upgrade old prose into structured bounds. Old dossiers must be
replayed using their exact original verifier implementation, whose identity is
part of intake validation. The frozen historical test dossier and score under
`tests/fixtures/` were produced by the original DCP producer with verifier
`69032292f5c8a788d7524a9339fe1c7b79bf3e44`, with mocked HTTP and inert claims.
To check preservation with that source:

```sh
PYTHONPATH=/absolute/path/to/verifier-6903229/src python export_metrics.py \
  --dossier tests/fixtures/historical-v2-dossier.json \
  --out .work/historical-v2-replayed.json
python -c 'import json; from pathlib import Path; assert json.loads(Path(".work/historical-v2-replayed.json").read_text()) == json.loads(Path("tests/fixtures/historical-v2-score.json").read_text())'
```
