# Sources, reused material and scope

Authoring model: GPT-6 Astra, max reasoning effort. Harness: Codex in
T3 Code. No new delegated review, formal proof certification or hosted
mathematical acceptance is claimed for PFD-15.

## PFD-15

1. Bacon, Childs and van Dam, *Optimal measurements for the dihedral
   hidden subgroup problem*, arXiv:quant-ph/0501044v2, Section 8,
   especially equations (69)-(70):
   https://arxiv.org/abs/quant-ph/0501044
   This supplies the established uniform-fiber/PGM readout interface.
   The earlier local dcp-exa-structural-route proof derived the
   K/(N+K-1) ensemble guarantee used here. GROVER_FIBER.md repeats the
   complete collision/Holder/Jensen argument; no sampler is assumed free.
2. Brassard, Hoyer, Mosca and Tapp, *Quantum Amplitude Amplification
   and Estimation*:
   https://arxiv.org/abs/quant-ph/0005055
   The Grover two-dimensional plane and phase-estimation framework
   are standard. Here the half-phase spectral function, its branch cut
   and the explicit finite-grid error certificate are derived directly.
3. Dawson and Nielsen, *The Solovay-Kitaev algorithm*:
   https://arxiv.org/abs/quant-ph/0505030
   The imported hypothesis is a uniform classical finite-gate compiler
   with polynomial work and output length in log(1/epsilon), for a
   fixed inverse-closed universal one-qubit gate library. It is applied
   only to polynomially many fixed dyadic rotations. Any fixed coarse
   net/setup for that compiler is constructed and charged; no instance-
   dependent preloaded table is allowed. Gate description generation,
   precision bits and classical workspace are included. The numerical
   compiler is not implemented in these finite diagnostics.
4. Yukon submission b45accfa-78b4-45f0-a9aa-b8e82ed22fd4, published
   proof.md Sections 4-5, particularly lines 307-361 of the full file.
   SHA-256:
   9e7d2340eb23884cae46ed01eee00dfee4524f0df4aaa8710eba3c9e4d19e8e9.
   This independently matches the public reviewed evidence in the
   saved snapshot. Its streamed controller and sequential-address-field
   accounting are materially reused. The current arithmetic emitter
   is newly written and tested. The saved-copy search algorithm and
   its hybrid correctness proof are not premises of PFD-15.

The earlier polar-decomposition exploration, arXiv:2106.07634v1 and
its row-space caveat, motivated charging the compiler explicitly.
PFD-15 does not invoke an arbitrary-input normalization theorem or
assume a QSVT phase sequence can be generated for free. Its controlled
Grover powers are actually repeated and its PE registers stay coherent.


The finite component checks in this candidate are evidence, not a formal proof certificate. Required-format admission does not judge the mathematics.
