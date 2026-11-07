# Reproduce the F4 finite evidence

From the benchmark directory:

    python3 -B submission/checks/run.py --out .work/f4-diagnostics.json

Requires Python 3.11+ on Linux and the standard library. The runner copies
its four source files into temporary storage. Each diagnostic enforces at
most 768 MiB address space and 50 CPU seconds; the runner adds a 60-second
wall limit. No generated result is added to the submission archive.

Checks cover tuple recovery and cleanup, carries, planted moments, arities,
search constants, exact all-D profile caps at modest sizes and decoder
identities. The authored diagnostic scripts are byte-exact research copies.
The portable runner and review provenance were added during publication.

These finite checks do not execute the full quantum solver or certify the
asymptotic proof. The official experiment list is empty. Format admission,
independent mathematical review and hosted evaluation are distinct steps.
