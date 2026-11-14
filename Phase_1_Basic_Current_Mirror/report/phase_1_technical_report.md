# Phase 1 Technical Report — Basic NMOS Current Mirror

## Abstract

A two-transistor NMOS current mirror was simulated in LTspice using an illustrative Level-1 MOSFET model. The study examined the effect of channel-length modulation on output-current variation, current mismatch, and output resistance. A controlled comparison was performed by changing only the model parameter `LAMBDA` from 0.02 V⁻¹ to 0.

## Circuit and conditions

- Supply: 1.8 V
- Reference current: 100 µA
- M1 and M2: W = 10 µm, L = 1 µm
- Model: `NMOS(Level=1, VTO=0.7 V, KP=200 µA/V²)`
- Output-voltage sweep: 0 V to 1.8 V, 10 mV step
- Analyses: DC operating point and DC sweep

M1 is diode-connected. M1 and M2 share the same gate voltage. Both sources are grounded; the standard three-terminal NMOS symbol ties the body to the source for this study.

## Results

### Output-current measurements

| VOUT (V) | IOUT, λ=0.02 (µA) | IOUT, λ=0 (µA) |
|---:|---:|---:|
| 0.1 | 52.719635 | — |
| 0.2 | 85.569722 | — |
| 0.3 | 98.430275 | — |
| 0.5 | 98.994235 | 99.999997 |
| 1.0 | 99.974372 | 99.999997 |
| 1.8 | 101.542600 | 100.000000 |

The values are selected LTspice cursor readings transcribed from the user's simulator screenshots. The CSV contains selected samples, not the complete sweep dataset.

### Current mismatch

Mismatch is defined as `(IOUT - IREF) / IREF × 100%`. With λ=0.02, the mismatch at 1.8 V is +1.5426%. With λ=0, the sampled current remains 100 µA to the displayed precision at 0.5 V, 1.0 V, and 1.8 V.

### Operating point

For λ=0.02, the LTspice device operating-point table showed M1 `Gds=1.96 µS` and M2 `Gds=1.96 µS` to the displayed precision. M2 had `VDS=1.80 V`, `VDSAT=0.313 V`, `gm=0.649 mS`, and a rounded drain current of `1.02e-04 A`.

For λ=0, the table showed M1 and M2 drain currents of `1.00e-04 A`, `gm=0.632 mS`, and `Gds=0.00e+00 S` to the displayed precision. The operating-point listing gave `VREF=1.01623 V`.

### Output resistance

Using the λ=0.02 DC sweep samples at 0.5 V and 1.8 V:

`gout ≈ (101.542600 − 98.994235) µA / 1.3 V = 1.96028 µS`

`rout ≈ 1 / gout = 510.13 kΩ`

This agrees with `1/Gds ≈ 510.2 kΩ` from the operating-point table to the precision of the displayed measurements.

## Discussion

With λ=0.02, the saturation-region current depends on `VDS` in the Level-1 model. Because M1 and M2 have different drain-source voltages, their currents do not match exactly. With λ=0, the model's channel-length-modulation term is removed; the sampled saturation-region current becomes effectively independent of output voltage, and the reported `Gds` is zero to the displayed precision.

At low VOUT, M2 is not yet in saturation. The output current therefore rises with VOUT even when λ=0. This is why the comparison must distinguish the low-voltage region from the saturation region.

## Limitations

- The Level-1 model is intentionally simple and is not a foundry PDK.
- LTspice reported that the selected W/L dimensions were shorter/narrower than recommended for a Level-1 MOSFET. The simulation converged, but the warning must be retained as a limitation.
- The `λ=0` case is an idealized controlled experiment, not a claim that real MOSFETs have infinite output resistance.
- Cursor points and log values are recorded at the precision visible in LTspice. Raw log screenshots containing local usernames and file paths are not included.

## Conclusion

The controlled simulation demonstrates the first-order impact of channel-length modulation on a basic NMOS current mirror. With nonzero λ, output current varies with output voltage and the estimated output resistance is approximately 510 kΩ. With λ set to zero, the idealized model produces nearly constant saturation-region current and reports zero output conductance to the displayed precision. This establishes a baseline for the next phase: a cascode current mirror, which will be evaluated under the same model and bias conditions.
