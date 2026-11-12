# DCP challenge

Find and prove better algorithms for the Dihedral Coset Problem, aiming at total
work 2^{O(n^{1/3})}, where n = ceil(log₂ N). Read [rules.md](rules.md) for the
input, charged cost model and joint proof obligations. Participants edit only
`submission/`. The example retains its exhaustive-search proof and original
statements: O(N n⁴) work, O(n²) classical bits, O(n²) qubits, and at most N(n+2) samples
(hence O(2ⁿn)). Its new
structured declarations require a new review; historical acceptance is not
acceptance of the added fields.

The Pareto backend minimizes **one numeric time growth index**, sourced from
claim 0. All four resource claims, indices and evidence remain mandatory and
are reviewed atomically for one algorithm/configuration. The baseline time
score is `[1]`. Index zero includes polynomial and quasipolynomial guarantees;
equal indices do not imply equivalent full bounds. Sample complexity counts every source copy acquired, including discarded copies
and failed attempts; it is independent of peak quantum storage and is not a
numeric objective. Promotion remains manual.

The fifth claim is the guaranteed malformed-sample fraction expression and explicit
error model, reviewed jointly with the four resource bounds. It has no `score`
and adds no numeric objective. The baseline claims `0`, meaning that its proof
requires clean samples; it does not prove a maximum tolerance of zero. The full
expression/model and evidence are exported as `metrics.dcp_error_tolerance`,
with matching intake/dossier hashes. See [the expression contract](rules.md#error-tolerance-expression).

## Reviewed structured metrics

`export_metrics.py` reconstructs the shared-verifier dossier before producing
`metrics.dcp` version `dcp-bounds-v4`. The protected verifier configuration opts
into `structured_claims: "atomic-v1"`. Each resource claim declares a structured
object containing the fixed comparison context and an exact rational bound.
The reviewer must acknowledge the digest of **all** structured claim records,
including both memory claims, the sample claim and the tolerance claim. The exporter requires atomic acceptance and
matches each accepted statement, structured object, source hash and evidence.

The v4 envelope has exactly these fields:

```json
{
  "version": "dcp-bounds-v4",
  "comparator": "asymptotic-v1",
  "scope": "dcp-cyclic-group-order",
  "model": "dcp-uniform-clifford-t-bit-operations-v1",
  "notation": "big-o",
  "intake_sha256": "<64 lowercase hex>",
  "dossier_sha256": "<64 lowercase hex>",
  "resources": {
    "time": "<resource>",
    "classical_space": "<resource>",
    "quantum_space": "<resource>",
    "samples": "<resource>"
  }
}
```

Each resource has exactly `statement`, `bound`, `source_sha256`, and `evidence`.
`statement` is verbatim; `evidence` maps paths relative to the submission root
(such as `proof.md`) to snapshot SHA-256 hashes. The source digest covers the
claim index and complete source snapshot using the shared verifier's binding.
The dossier retains all four exact growth indices and original structured data.
The table's version/comparator/scope/model/notation must match the envelope.

The bound family is C·2^(Σ a·n^p·(log₂ n)^q)·n^r·(log₂ n)^s, with the exact keys,
limits and examples in [rules.md](rules.md#structured-reviewed-envelopes-dcp-bounds-v4).
`complexity_bounds.py` combines equal terms, folds 2^(a log₂ n) into n^a,
reduces rational strings and checks the exact growth index. Big-O ignores only
the outer C; unknown coefficients inside an exponent are never guessed.
No expression is extracted from prose, LaTeX, hints or scores.

In protected optional mode, if a valid reviewed claim has no supported
structured representation, the exporter emits **no `metrics.dcp`**. Instead `metrics.dcp_omission` contains the
target version, explicit per-resource reasons, intake/dossier hashes and all
four original statements, indices, evidence and any declared structured data.
The entire joint row is omitted from the structured frontier. Rejected,
unscored and validity-only results have no bound metrics. Simulations, stale or
mismatched review bindings and contradictory context/index data cannot publish.

Hashes and digest acknowledgments establish integrity, not reviewer identity
or mathematical truth. Accept dossiers only through the trusted organizer
workflow/artifact channel. Offline fixture reviews are scripted tests, not
proof certification.

## Required admission and the optional switch

Launch defaults to validity policy
`{"version":"dcp-joint-bounds-v7","structured_bounds":"required"}` with unchanged
`dcp-time-growth-v2` scoring. Every submission must declare supported time,
classical-space, quantum-space and sample bounds and matching exact rational indices,
plus the fifth unscored tolerance expression and error model. Its supported
`fractional-tolerance-v1` fractional guarantee participates in the full Pareto frontier, with
the original fractional expression preserved and no new numeric objective. See
[rules.md](rules.md#error-tolerance-expression) for syntax, comparison semantics,
and the requirement to match error models. Earlier v6 count dossiers retain their count grammar and original `reviewed-expression-v1` exports;
they are never reinterpreted as fractional guarantees. Earlier v5 tolerance dossiers retain
their original bounded-text admission contract.
This includes unscored, partial and validity-only submissions. The gate checks
format and index consistency; only the judge establishes the exact statements,
evidence and same-algorithm joint guarantees.

The protected organizer command `python configure_bounds.py --mode optional`
synchronizes `verifier.json` and `benchmark.json`; `--mode required` restores the
launch setting. It registers only the selected mode. Changing candidate data or
`YUKON_EVALUATION` cannot downgrade admission. Historical v2 review policies
remain optional according to their retained configuration, not today's default.

The Benchmark admission job checks the same immutable candidate SHA and verifier
pin as review, without provider credentials or accepted-result resolution.
Known missing/unsupported/malformed declarations succeed as a **format rejection**:
`valid:false`, `scores:null`, a clear reason and `metrics.dcp_admission`. A separate
`dcp-admission` artifact contains original bounded bytes, selected policy, exact
validator source hashes, verifier identity and the replayable receipt. These
hashes are provenance, not review authentication or mathematical acceptance.
The rejection uploads the sole `dcp-score` artifact and skips review. On Yukon,
a separate receipt-only job uses GitHub workload identity to bind that rejection
to the platform accepted-results protocol. It verifies the same admission
snapshot and immutable candidate, calls no judge, executes no candidate code,
and exports only the authenticated receipt, never an accepted-claims bundle or
mathematical dossier. The admission job itself remains credential-free. Supported
submissions proceed through the actual verifier and normal producer instead.
Configuration, I/O, pin and unexpected runtime faults fail without a score.
Validity-only requests omit scores; score-only invalid requests fail with
`score_only_claim_not_established` and cannot replace an earlier validity.

The official local manifest calls DCP preparation and finalization wrappers.
Preparation freezes the bytes checked by admission before creating intake;
review rechecks that exact intake before any provider. Finalization checks the
receipt/intake match and computes the validated projection before writing a
score. A format rejection produces no mathematical dossier. The exporter also
checks required format on retained intakes, even if unscored or invalid. Calling
the raw generic verifier CLI is not a DCP admission check.

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
.venv/bin/python dcp_admission.py preflight --root . --receipt .work/admission.json --score .work/admission-score.json
.venv/bin/python -m unittest -v
.venv/bin/python offline_fixtures.py --out .work/yukon-fixtures
.venv/bin/python admission_fixtures.py --out .work/admission-fixtures
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

The manifest's `setupCommand` creates `.yukon/work/admission.json` and, only for
`outcome:review`, `.yukon/work/intake.json`. A local phase driver must inspect that
outcome before executing/reviewing anything. Use `dcp_admission.py review-initial`
in place of generic initial review; this command can call the paid provider. The manifest's `benchmarkCommand`
uses `dcp_admission.py finalize` for either terminal branch. Direct trusted-dossier
projection remains `python export_metrics.py --dossier .yukon/dossier.json --out
.yukon/score.json`; it rechecks required admission and clears stale output on failure.

The original verifier `69032292f5c8a788d7524a9339fe1c7b79bf3e44` cannot execute
this opt-in contract. The exporter fails with `dcp_structured_verifier_required`
and clears stale output under that runtime; `check_legacy_runtime.py` tests this
against its exact original source. Keep both workflow and implementation pins
identical when upgrading. The metrics job consumes that same run's wheel and
dossier and retains the `dcp-score` artifact selection.

Push and PR checker CI does not run model review. The Benchmark workflow remains
dispatch-only; local checks do not perform hosted judging, import or rebind.
Hosted review uses one background request at high reasoning effort, with at most
32,768 output tokens and 1,200 seconds for the review. The token cap covers both
reasoning and final output. It does not automatically start another attempt after
a timeout. A timeout is an execution failure, not a
mathematical rejection; inspect the original run before authorizing another
review. These execution settings require fresh hosted qualification before launch.
The new required-mode validity identity changes acceptance semantics. Publishing
this source does not update an existing track or reclassify an accepted baseline.
Adoption uses the new immutable source and validity policy and needs fresh
baseline qualification; publishing source alone does not perform those steps.
Preserve the existing historical track, accepted baseline and evidence.

## Sample and error-tolerance columns

[complexity-tab.json](complexity-tab.json) configures Time, Classical memory,
Quantum memory, Number of Samples, and expression-only Fractional Error Tolerance,
with Time ascending. Preserve the page's default
chart `presentation.results.defaultView = {"mode":"record","objective":"time_growth"}`.
The tab is configured for `dcp-bounds-v4`; it must be activated only with a
source/policy and freshly reviewed results supplying `dcp-bounds-v4` resources and
a `reviewed-fraction-v1` tolerance sidecar. The fifth input claim uses
`dcp-fractional-error-tolerance-v1`, with fractions such as `1/100` or `1/n^2`
and no Q or floor brackets. The file is
a tab configuration, not a full page replacement. It requires the Yukon reviewed-expression
column support and `fractional-tolerance-v1`, in addition to the resource comparator.

Historical v4 sample-only dossiers retain their four resources without inferred
tolerance. Historical v3 dossiers continue to emit their original three-resource v3
metrics under their original required/optional policy. Missing sample claims
are never synthesized from time, memory, or prose. Existing v3 results do not
qualify for the four-column v4 table. No hosted policy, baseline, page or
participant history changes merely by editing this repository.

## Historical v2 evidence

Existing v2 records and their `[time, classical_space, quantum_space]` scores
remain historical and unchanged. The exporter retains their original branch;
it does not upgrade old prose into structured bounds. The frozen `yukon-producer-fixtures.json` also retains the earlier optional
producer snapshot. New required/optional admission fixtures are generated separately.
Old dossiers must be
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

## Score-only fractional metric migration

The optional [retained-validity scoring profile](docs/score-derivation.md) derives
fractional tolerance from authenticated original full claims while preserving
resource bounds, time scores and validity reviews. It prepares a separate source
with the active v6 input contract; this default source retains the v7 contract.
Plan preparation and offline previews do not activate a reorg or publish scores.
