# Sources and provenance

## Material Yukon dependencies

RQ-SPLIT, submission 38d66dc0-bcf7-452a-ab86-edfc175c0db1, evaluated commit
192aca46e40deca146adf850db00f74544ac04bd. Its unmodified proof is supplied at
sources/RQ-SPLIT-proof.md, SHA-256
2952a6f52b94dfa9d0e03471b9e7611f185db198dbc9274639dbc03ce7d1ca80.
https://github.com/Layr-Labs/dcp/blob/192aca46e40deca146adf850db00f74544ac04bd/submission/proof.md

Reused: the exact adaptive model; raw-source extraction; post-delivery bank
split and its causal/count argument; cubic witnesses and phase-word arithmetic;
canonical class comparisons and role discrepancy; mixed-search sampler context;
untouched endpoint and finite-n fallback. All needed primary arguments are in
that included file. Hosted validity is not a mathematical premise.

FNS1, submission 9e0a54c5-ba96-42f9-877f-310ca9c478eb, evaluated commit
0ca6241b5770096e4a7f38e8c5204d4b4beeccd4. Its unmodified proof is supplied at
sources/FNS1-proof.md, SHA-256
8f8fa926b6779efdd12ce593c3d79e9cba9144c755ee664304fc1efaf5074e57.
https://github.com/Layr-Labs/dcp/blob/0ca6241b5770096e4a7f38e8c5204d4b4beeccd4/submission/proof.md

Adapted: private classical record sampling after acquisition, fixed-record
filter analysis, clean multiset-oracle accounting, and nested known-unitary
preparation/reflection. SPTS1 uses a new per-pivot sketch and recursive sampler,
not FNS1's fixed two-level iteration schedule. FNS1's ROB-G2 acquisition and
scalar score are not used here; the front end is RQ-SPLIT's.

The exact error-model bytes in sources/error-model.txt have SHA-256
fd67d2af7a9a9733f2422981afd4a6ce00bb9ceac8c29d345f29535cc0156475.
Earlier source lineage is acknowledged in the included primary proofs; no
additional direct reuse or verified attribution graph is inferred from it.

## Established search frameworks

- Brassard, Hoyer, Mosca and Tapp, Quantum Amplitude Amplification and Estimation,
  arXiv:quant-ph/0005055v1, https://arxiv.org/abs/quant-ph/0005055v1.
  Relevant to reflection about a known prepared state using its actual inverse.
- Boyer, Brassard, Hoyer and Tapp, Tight bounds on quantum searching,
  arXiv:quant-ph/9605034v1, https://arxiv.org/abs/quant-ph/9605034v1.
  Relevant to search with an unknown marked fraction and randomized clocks.
- Cerf, Grover and Williams, Nested quantum search and structured problems,
  Physical Review A 61, 032303 (2000), https://doi.org/10.1103/PhysRevA.61.032303.
  Preprint https://arxiv.org/abs/quant-ph/9806078v1 has the title Nested quantum
  search and NP-complete problems. Relevant as prior nested search.

The needed probability and cost inequalities are derived in proof.md or the
included primary source. These references are not unaccounted subroutine
oracles. No first-ever general search or exact-one-third claim is made.

## Work and review

GPT-6 Astra at max reasoning effort under Codex in T3 Code developed SPTS1,
the parent proof and the exact constant/physical-shadow fixtures. GPT-6.1 Terra
wrote independent finite abstract structure diagnostics and assisted with
publication preparation. Claude Opus 5.5 independently audited the new theorem;
GPT-6.1 Sol subsequently checked the inherited extraction and the complete
search/stopping/endpoint argument. Their reports and scope limits are included.
The reviews are corroborating evidence, not proof premises, formal proof-assistant
certificates, production quantum executions or hosted acceptance.
