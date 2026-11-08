# PFD-N1 evidence

`proof.md` is the self-contained all-N theorem and algorithm. `submission.json`
contains four joint resource claims and the unscored clean-copy tolerance
claim. `sources.md` records the supplied proposal and material reuse.

The circuit emitter is `walk.py`, built on PFD-15's unchanged `arithmetic.py`.
It streams the controlled two-reflection walk and its inverse. Only one
O(n)-gate arithmetic template is buffered at a time. The production PE
repetition count is specified by `parameters` and `power_schedule`; the
exponential circuit listing is not materialized.

Run the bounded checks with Python 3.11+ and no third-party Python packages:

```sh
python3 -B check_statistics.py
python3 -B check_walk.py
python3 -B check_sign_filter.py
python3 -B check_arithmetic.py
```

Each checker has a 45 CPU-second and 512 MiB address-space cap. The arithmetic
and controlled-walk columns use exact arithmetic. The full PE/sign/inverse
simulator and complete readout fixtures use floating-point complex arithmetic
on small grids, with explicit tolerances. They do not certify production
precision by extrapolation; the proof and rational tail checks do that.

The generic configuration includes N=2 and acquires exactly n+1 source copies
on every branch. The source shift is positive. It reports the source label
without a sign change; the final target shift label is negated.

The outer rotation compiler is the explicitly charged uniform synthesis
construction cited in the proof. A numerical Solovay-Kitaev compiler and the
production-size circuit are not executed by this diagnostic packet. The
finite programs are evidence for the constructive proof, not a physical
quantum backend or a free subset-sum oracle.
