# Phase 1 — Basic NMOS Current Mirror

This phase establishes a two-transistor NMOS current mirror as the baseline circuit for later architecture comparisons.

## Circuit conditions

- Supply voltage: 1.8 V
- Reference current: 100 µA
- M1 and M2: W = 10 µm, L = 1 µm
- Output-voltage sweep: 0 V to 1.8 V, 10 mV step
- Model: illustrative Level-1 NMOS

Two controlled model cases were simulated:
- `LAMBDA=0.02`
- `LAMBDA=0`

## Work completed

1. DC operating-point analysis.
2. DC output-voltage sweep.
3. Comparison of output-current characteristics.
4. Current-mismatch calculation.
5. Output-resistance estimation from the sweep and operating-point data.

See `analysis/experiment_notes.md` and `report/phase_1_technical_report.md` for details.

## Important limitation

LTspice issued recommended-dimension warnings for the chosen Level-1 MOSFET geometry. These simulations are intended to illustrate first-order behavior, not to represent a foundry-qualified design.
