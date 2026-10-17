# DCP challenge

Find and prove better algorithms for the Dihedral Coset Problem, aiming at total
work 2^{O(n^{1/3})}, where n = ceil(log₂ N). Read [rules.md](rules.md) for the
input, cost model, proof obligations and comparison policy. Participants edit
only `submission/`; its example gives a self-contained exhaustive-search proof
with bounds O(N n⁴) work, O(n²) classical bits and O(n²) qubits.

The UI vector minimizes three **growth indices**: time, classical space and
quantum space. The example declares [1, 0, 0]. Indices are coarse: zero includes
both polynomial and quasipolynomial bounds. Full reviewed statements, exact
rational indices, source hashes and evidence hashes are retained in `metrics.dcp`.
Scientific comparisons use those statements; promotion is manual. No automatic
general symbolic comparator is included.

## Shared verifier and the one extension

This uses `Layr-Labs/llm-verifier` at
`69032292f5c8a788d7524a9339fe1c7b79bf3e44`, following its
[`llm-verifier-challenge` skill](https://github.com/Layr-Labs/llm-verifier/blob/69032292f5c8a788d7524a9339fe1c7b79bf3e44/skills/llm-verifier-challenge/SKILL.md).
It supplies intake, review, score binding, phase validation and hosted execution.

That revision does not export arbitrary Yukon metrics. `export_metrics.py` adds
only the accepted statements from the immutable dossier, after rerunning the
shared dossier validator. It makes no model calls and evaluates no expressions.
Rejected, unscored, and validity-only results receive no bound metrics.
The `dcp-bounds-v2` metric records `source_sha256` for each resource; the
shared verifier accepts all original claims together, without ID selectors.
Simulations cannot publish. Its tests use mocked HTTP responses and independent
inert fixtures; they neither call a model nor certify mathematical correctness.

The generated Actions caller has one extra export job. It consumes the shared
wheel and dossier from the same workflow run, then uploads `dcp-score`, the
artifact selected by `benchmark.json`. The upstream `benchmark-score` and
`verifier-dossier` remain separate audit artifacts. As with the shared verifier,
trust comes from the organizer's workflow/artifact channel, not hashes alone.

## Local validation and hosted qualification

With access to the verifier repository and Python 3.11+:

```sh
python3 -m venv .venv
.venv/bin/pip install 'git+https://github.com/Layr-Labs/llm-verifier.git@69032292f5c8a788d7524a9339fe1c7b79bf3e44'
.venv/bin/llm-verifier check --root .
.venv/bin/python -m unittest -v
```

The reviewer is `gpt-6-astra` with high reasoning effort through OpenAI.
Each evaluation permits at most two provider requests and 360 review seconds.
Static checks and export tests do not qualify the model or the baseline proof.
Before launch, configure `OPENAI_API_KEY` in the challenge repository,
provide reusable-workflow access and, if necessary, `VERIFIER_CHECKOUT_TOKEN`
for the pinned verifier repository. Run the workflow on the baseline and on an
incorrect claim; inspect the dossier and require expert review before promotion.
Live qualification results are recorded separately from these setup instructions.

The hosted workflow orchestrates the phases. Local `yukon run` does not do that;
use the shared verifier's documented phase commands for local reviews, then:

```sh
.venv/bin/python export_metrics.py --dossier .yukon/dossier.json --out .yukon/score.json
```

`llm-verifier github` regenerates the caller and manifest. On an upgrade,
preserve the extra metrics job and the manifest's `dcp-score` artifact selection,
then rerun checks. No custom checker, copied runner, proof-parser language or
additional dependency is needed here.
