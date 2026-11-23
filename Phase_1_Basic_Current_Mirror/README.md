# Phase 1 — Basic NMOS Current Mirror

I started with a two-transistor NMOS current mirror in LTspice. The main thing I wanted to check was how closely M2 follows the 100 µA reference current, and how much channel-length modulation changes the result.

## Circuit and setup

| Parameter | Value |
|---|---:|
| Supply voltage | 1.8 V |
| Reference current | 100 µA |
| M1 and M2 width | 10 µm |
| M1 and M2 length | 1 µm |
| Model threshold voltage | 0.7 V |
| KP | 200 µA/V² |
| LAMBDA | 0.02 and 0 |
| Output-voltage sweep | 0–1.8 V, 0.01 V step |

M1 is diode-connected, and its gate is connected to M2. Both sources and bulks are grounded. I ran the same circuit twice and changed only LAMBDA.

The model is a simple Level-1 NMOS model:

```spice
.model NM NMOS(Level=1 VTO=0.7 KP=200u LAMBDA=0.02)
```

## LTspice files

- [LAMBDA = 0](schematics/Basic_Current_Mirror_Lambda0.asc)
- [LAMBDA = 0.02](schematics/Basic_Current_Mirror_Lambda002.asc)

The separate operating-point and DC-sweep netlists are in [simulation/netlists](simulation/netlists/).

## Results

| VOUT | IOUT, LAMBDA = 0.02 | IOUT, LAMBDA = 0 |
|---:|---:|---:|
| 0.1 V | 52.719635 µA | — |
| 0.2 V | 85.569722 µA | — |
| 0.3 V | 98.430275 µA | — |
| 0.5 V | 98.994235 µA | 99.999997 µA |
| 1.0 V | 99.974372 µA | 99.999997 µA |
| 1.8 V | 101.542600 µA | 100.000000 µA |

These are selected readings from the LTspice plot cursors, not the full set of sweep points.

With LAMBDA = 0.02, the output current at 1.8 V was 101.5426 µA, which is 1.5426% above the reference current. With LAMBDA = 0, the three sampled saturation-region points stayed very close to 100 µA.

I also estimated the output resistance from the LAMBDA = 0.02 sweep. The result was about 510 kΩ, close to the inverse of M2's operating-point Gds shown in the LTspice log.

## What this shows

When LAMBDA is non-zero, the drain current changes with VDS. M1 and M2 have different drain-source voltages, so their currents do not match exactly. Setting LAMBDA to zero removes this dependence from the simple model, which is why the sampled output current stays almost constant.

At low VOUT, M2 is not in saturation and the output current drops below the reference current.

## Limitations

- The Level-1 model uses illustrative parameters and is not a foundry model.
- LTspice warned that the selected W and L were outside its recommended range for this model.
- The table contains selected cursor readings, not a full exported sweep dataset.
- The zero-LAMBDA result is an idealised model result. It does not mean a real MOSFET has infinite output resistance.

More calculations are in [experiment_notes.md](analysis/experiment_notes.md), and the longer write-up is in [phase_1_technical_report.md](report/phase_1_technical_report.md).
