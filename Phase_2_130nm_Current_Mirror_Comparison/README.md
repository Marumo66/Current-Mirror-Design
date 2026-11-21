# Phase 2 — 130-nm Current Mirror Comparison

This phase compares a basic NMOS current mirror with a self-biased cascode current mirror in LTspice.

Both circuits use the same generic 130-nm BSIM3 model, 1.5 V supply, 100 µA reference current and 10 µm / 1 µm MOSFET dimensions. The output voltage is swept from 0 V to 1.5 V in 5 mV steps. The measurements below cover 0.5 V to 1.5 V.

## Files

- schematics/basic_current_mirror_130nm.asc — basic two-transistor current mirror.
- schematics/cascode_current_mirror_130nm.asc — four-transistor self-biased cascode current mirror.
- results/data/selected_dc_measurements.csv — the three voltage points read from the LTspice measurement logs.
- results/data/derived_metrics.csv — calculations based on the LTspice MIN and MAX measurements over 0.5–1.5 V.
- results/data/measurement_notes.md — measurement values, conditions and model warnings.
- results/figures/selected_dc_points.svg — plot of the three measured points. It does not represent a full sweep export.
- models/README.md — model file requirements and notes.
- simulation/measurement_directives.md — the .meas directives used in the schematics.

## Simulation setup

| Parameter | Basic | Cascode |
|---|---:|---:|
| Supply voltage | 1.5 V | 1.5 V |
| Reference current | 100 µA | 100 µA |
| NMOS dimensions | W = 10 µm, L = 1 µm | W = 10 µm, L = 1 µm (each device) |
| Temperature | 27 °C | 27 °C |
| Output-voltage sweep | 0–1.5 V, 5 mV step | 0–1.5 V, 5 mV step |
| Device model | generic 130-nm BSIM3 | generic 130-nm BSIM3 |

## Results

| Measurement | Basic | Cascode |
|---|---:|---:|
| IOUT at 0.5 V | 100.4278 µA | 99.0782 µA |
| IOUT at 1.0 V | 104.2175 µA | 99.9997 µA |
| IOUT at 1.5 V | 107.4614 µA | 100.0384 µA |
| Current variation, 0.5–1.5 V | 7.0336% | 0.9602% |
| Maximum absolute current error in this interval | 7.4614% | 0.9218% |
| Interval output-resistance estimate | 142.17 kΩ | 1.04145 MΩ |

The measured current variation is 86.35% lower with the cascode circuit. The interval output-resistance estimate is 7.33 times the basic-circuit estimate (about a 632.5% increase).

## How the calculations were made

Current variation is calculated as (Imax - Imin) / IREF over the 0.5–1.5 V interval. Maximum absolute current error is calculated from the measured minimum and maximum currents relative to the 100 µA reference. The interval output resistance is estimated from (1.5 V - 0.5 V) / (IOUT at 1.5 V - IOUT at 0.5 V).

The output-resistance values are interval estimates from the DC sweep. They are not small-signal output resistance values taken from an operating-point gds measurement.

## Notes and limitations

The measurements were copied from LTspice 26.0.2 output logs. The schematics and measurement values are from the submitted LTspice files and screenshots; the simulations were not rerun in this build environment.

LTspice reported that it supports BSIM3 version 3.3.0 while the supplied model specifies version 3.200. It also reported zero drain/source junction perimeters (PD and PS). The model file was not modified to suppress these warnings. The model is a generic technology model, not a foundry-qualified PDK. Results should be read as a comparison within this model and setup, not as silicon performance predictions.

The model file is not included because its redistribution licence has not been confirmed. See models/README.md before running the schematics.
