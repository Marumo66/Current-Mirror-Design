# Phase 1 Results Summary

- Reference current: 100 µA.
- With `λ=0.02`, `IOUT(1.8 V)=101.542600 µA`; signed mismatch = +1.542600%.
- With `λ=0`, sampled saturation-region current is approximately 100 µA at 0.5 V, 1.0 V, and 1.8 V.
- Finite-difference output resistance with `λ=0.02`: approximately 510.13 kΩ.
- Operating-point `Gds` for `λ=0.02`: 1.96 µS, corresponding to approximately 510.2 kΩ.
- Operating-point `Gds` for `λ=0`: 0.00 S to the displayed precision in this idealized Level-1 model.

Interpretation: enabling channel-length modulation gives finite output conductance and output-voltage-dependent current in saturation. Setting `λ=0` removes this dependence from the simplified model, but does not represent a real MOSFET with all physical effects included.
