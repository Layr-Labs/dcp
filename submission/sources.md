# Sources and attribution

The material Yukon dependency is ROB-G2, submission
55a6ce76-34af-468f-b735-a1197f3d3459, evaluated commit
77b383ed0ea3c8b9765c332de88add12c3d2b52d. The supplied unmodified proof at
sources/ROB-G2-proof.md is its submission/proof.md, SHA-256
64a87926620815ae4030997207eedff9f4507b5fb825c3c07d88c5794f566228.
URL: https://github.com/Layr-Labs/dcp/blob/77b383ed0ea3c8b9765c332de88add12c3d2b52d/submission/proof.md

Reused material: exact Clifford+T arithmetic, adaptive acquisition and records,
score table/range/discretization, quantitative simultaneous separation, the
signed-score phase oracle and cleanup, and the bounded finite-n output fallback.
The full primary argument is included so review requires no external fetch.
Its exact model text, originally tracing to ROB and retained in ROB-G2's
official context, is supplied in sources/error-model.txt with SHA-256
fd67d2af7a9a9733f2422981afd4a6ce00bb9ceac8c29d345f29535cc0156475.
ROB-G2 is the immediate source actually used for this construction. Its earlier
lineage is acknowledged, without inventing additional direct reuse claims.

The general search framework is established prior work:

- Brassard, Hoyer, Mosca and Tapp, Quantum Amplitude Amplification and Estimation,
  arXiv:quant-ph/0005055v1 (2000), https://arxiv.org/abs/quant-ph/0005055v1.
  Relevant to reflection about a known prepared state V|0> using V and its
  actual adjoint. The needed two-reflection calculation is derived in proof.md.
- Cerf, Grover and Williams, Nested quantum search and structured problems,
  Physical Review A 61, 032303 (2000), https://doi.org/10.1103/PhysRevA.61.032303.
  Preprint: Nested quantum search and NP-complete problems,
  https://arxiv.org/abs/quant-ph/9806078v1. Relevant as earlier nested search,
  not a premise for the DCP-specific statistics or charged cost bound.

The filtered-search direction came from a Claude Opus 5.5 research review.
GPT-6 Astra at max effort under Codex in T3 Code developed the final fixed
integer schedule, repaired cardinality slack, capped index sampling, exact
gap and probability certificates, and resource construction. A separate Opus
5.5 review supported that theorem and requested the incorporated clarifications.
GPT-6.1 Terra assisted with primary citations and publication packaging.
The new theorem's claimed contribution is its DCP specialization and complete
certificate, not invention of amplitude amplification or nested search.
