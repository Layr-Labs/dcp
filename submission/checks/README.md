# Reproduce the finite evidence

From the benchmark directory, run:

    python3 -B submission/checks/run.py --out .work/ppc-diagnostics.json

The scripts require Python 3.11+ on Linux and only the standard library.
Each diagnostic limits address space to at most 768 MiB and CPU time to at
most 60 seconds. The runner also imposes a 90-second wall limit per child.
It copies its inputs into temporary storage, so running it does not add
generated results to the submission archive. No GPU or provider is used.

Checks cover exact capacities, partial-width renewals, all-D caps at modest
n, labeled root-only larger instances, reversible query support/recovery,
decoder identities and finite lower-bound cases. They do not simulate the
complete quantum solver, prove the asymptotic theorem or certify acceptance.
The official experiments list is empty. These are optional offline checks.

The profile and check scripts are byte-exact copies of the authored research
packet. The root added only this portable temporary-directory runner.
