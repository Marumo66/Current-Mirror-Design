# Phase 2 — 130-nm Current Mirror Comparison

In this part I compared a basic NMOS current mirror with a four-transistor self-biased cascode current mirror in LTspice. I wanted to see how much the cascode version reduces the change in output current as VOUT increases.

## Circuit and simulation setup

Both circuits use the same generic 130-nm BSIM3 model, 1.5 V supply, 100 µA reference current and 10 µm / 1 µm NMOS dimensions. I swept the output voltage from 0 V to 1.5 V in 5 mV steps. The comparison below uses the 0.5–1.5 V interval.

| Parameter | Basic mirror | Cascode mirror |
|---|---:|---:|
| Supply voltage | 1.5 V | 1.5 V |
| Reference current | 100 µA | 100 µA |
| NMOS dimensions | W = 10 µm, L = 1 µm | W = 10 µm, L = 1 µm (each device) |
| Temperature | 27 °C | 27 °C |
| Output-voltage sweep | 0–1.5 V, 5 mV step | 0–1.5 V, 5 mV step |
| Model | Generic 130-nm BSIM3 | Generic 130-nm BSIM3 |

## LTspice files

- [Basic current mirror](schematics/basic_current_mirror_130nm.asc)
- [Self-biased cascode current mirror](schematics/cascode_current_mirror_130nm.asc)

Both schematics refer to `../models/cmos130.lib`. The model file is not included because I have not confirmed its redistribution terms. See [models/README.md](models/README.md) before running the circuits.

## Results

| Measurement | Basic | Cascode |
|---|---:|---:|
| IOUT at 0.5 V | 100.4278 µA | 99.0782 µA |
| IOUT at 1.0 V | 104.2175 µA | 99.9997 µA |
| IOUT at 1.5 V | 107.4614 µA | 100.0384 µA |
| Current variation, 0.5–1.5 V | 7.0336% | 0.9602% |
| Maximum absolute current error in this interval | 7.4614% | 0.9218% |
| Interval output-resistance estimate | 142.17 kΩ | 1.04145 MΩ |

Over this measurement interval, the cascode circuit reduced the measured current variation by about 86.35%. The interval output-resistance estimate was about 7.33 times the basic mirror's estimate.

I calculated current variation as `(Imax - Imin) / IREF`. The output-resistance estimate is `(1.5 V - 0.5 V) / (IOUT at 1.5 V - IOUT at 0.5 V)`.

These resistance values come from the DC sweep endpoints. They are not small-signal output resistance values calculated from operating-point Gds.

## Files and measurements

- `results/data/selected_dc_measurements.csv` — three measured output-current points for each circuit.
- `results/data/derived_metrics.csv` — calculations from the LTspice MIN and MAX measurements.
- `results/data/measurement_notes.md` — values copied from the LTspice output logs and the conditions used.
- `results/figures/selected_dc_points.svg` — plot of the selected points, not a full sweep export.
- `simulation/measurement_directives.md` — the `.meas` commands used in the schematics.

## Notes and limitations

The values were copied from LTspice 26.0.2 output logs. The schematics and readings are from the LTspice files and screenshots; I did not rerun the simulations in this build environment.

LTspice reported that it supports BSIM3 version 3.3.0 while the model specifies version 3.200. It also reported PD and PS warnings because those values are zero. I left the model unchanged.

The model is generic, not a foundry-qualified PDK. The results show how these two circuits compare with this model and setup; they should not be treated as predictions for silicon.
