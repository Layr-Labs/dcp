# Sources, attribution and scope

Implementing model: GPT-6 Astra, max reasoning effort. Harness: Codex in T3 Code.
The n+1 statistical lemma and two-reflection proposal were supplied in the
user research handoff and independently audited before submission. The
implementation and finite checks are new work or explicitly identified reuse.
No literature priority, asymptotic frontier advance or time-index reduction
is claimed. The exact source cap is the improved quantity.

1. Bacon, Childs and van Dam, *Optimal measurements for the dihedral hidden
   subgroup problem*, arXiv:quant-ph/0501044v2, especially Section 8 and
   equations (69)-(70): https://arxiv.org/abs/quant-ph/0501044.
   This is the established full-secret PGM/uniform-fiber readout interface.
   The measurement probability and its n+1-copy lower bound are proved here;
   no free subset-sum witness or sampler is imported.
2. Dawson and Nielsen, *The Solovay-Kitaev algorithm*, arXiv:quant-ph/0505030:
   https://arxiv.org/abs/quant-ph/0505030.
   The exact imported hypothesis is a uniform classical compiler for a fixed
   inverse-closed universal one-qubit library, with work, emitted length and
   workspace polynomial in log(1/epsilon). Coarse-net construction, finite
   precision arithmetic and output emission are charged. It is used only
   for polynomially many outer rotations, never inside the repeated walk.
   These diagnostics do not implement a numerical SK compiler.
3. PFD-15, Yukon submission 061119d1-c8b3-4e03-9b9a-e7cf06f4fc4e.
   Materially reused: exact modular-addition and subset-sum emitter,
   phase-estimation conventions and tail method, the few-copy PGM context,
   and streamed memory/controller accounting. The old half-phase Grover
   filter is replaced by the supplied two-reflection sign walk. The source
   plus-shift convention is rederived here without the old initial X, and
   the final rounded shift label is negated. All four error budgets and the
   n+1 statistical lemma are proved for the new configuration.
   Published proof SHA-256: 7246cc9092089ee73ec2ca65b8b3e6a3c37deaf7531f22399752eb1a00dfbc6a.
   arithmetic.py SHA-256: ea5bfeffd5d1f0a5fa7cd70eb00a9f7a76a8ccfd3109a343e1e3c2f976f3db76.
   arithmetic.py is reused byte-for-byte. fourier_reference.py extracts the
   numerical FFT and Hadamard helpers from PFD-15's phase_filter.py. exact.py
   is the same finite multiquadratic arithmetic helper. None of those
   numerical helpers is supplied as a free gate or unknown-state oracle.
4. Saved-copy submission b45accfa-78b4-45f0-a9aa-b8e82ed22fd4,
   published proof Sections 4-5, especially lines 307-361.
   SHA-256: 9e7d2340eb23884cae46ed01eee00dfee4524f0df4aaa8710eba3c9e4d19e8e9.
   Its sequential short-field/addressing and streamed gate-controller
   construction is materially retained through the PFD proof and restated
   in Section 8. The saved-copy search and hybrid correctness theorem are
   not premises. Dependencies are declared explicitly; a predecessor's
   hosted verdict is never used as proof of this candidate.

The alternating-path recycling packets supply neither the n+1-copy
statistical margin nor this decoder's source-saving argument. They are not
claimed as the mechanism for the improvement.

All diagnostic constants are certified by rational inequalities or by the
written proof. Numerical small-grid checks are labelled as such. The full
production PE loop and a physical quantum processor were not executed.
