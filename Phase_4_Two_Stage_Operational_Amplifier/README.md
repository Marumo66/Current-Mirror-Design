# Phase 4 — Two-Stage CMOS Operational Amplifier

This phase develops a two-stage CMOS op-amp in LTspice using the generic 130-nm BSIM3 model used in the earlier phases.

## Circuit

- First stage: NMOS differential pair (M1, M2) with PMOS current-mirror active load (M3, M4).
- Tail current source: NMOS M5.
- Second stage: PMOS common-source device M6 with NMOS current-sink load M7.
- Compensation: Miller capacitor CC in series with nulling resistor RZ.
- Device dimensions: M1–M7 use W = 10 µm and L = 1 µm.

## Design conditions

| Parameter | Value |
|---|---:|
| Supply voltage | 1.5 V |
| Load capacitance, CL | 1 pF |
| Compensation capacitance, CC | 1 pF |
| Compensation resistance, RZ | 10.5 kΩ |
| Temperature | 27 °C |
| VINP common-mode level | 0.45 V |
| VTAIL bias | 0.31 V |
| VBN2 bias | 0.292 V |

The bias voltages are supplied by ideal voltage sources in this version. A transistor-level bias generator has not yet been implemented.

## Current measured results

| Measurement | Result |
|---|---:|
| Open-loop low-frequency gain | 79.58 dB |
| Unity-gain bandwidth (cursor estimate) | ≈ 13.54 MHz |
| Phase margin (cursor estimate) | ≈ 46.09° |
| Rising output slope, 500 mV step, 20–80% | 10.84 V/µs |
| Falling output slope, 500 mV step, 80–20% | 3.93 V/µs |
| Quiescent core power from VDD | 27.34 µW |

The AC values were obtained from the return-ratio trace `-V(out)/V(nfb)` with a 0 V DC / 1 V AC test source in series with the feedback path. The reported UGBW and phase margin are cursor-based values close to the 0 dB crossing.

The slew-rate values are average slopes over the selected output-voltage intervals. The rising slope continued to increase slightly as the input step was increased from 200 mV to 500 mV; therefore 10.84 V/µs is not claimed as a fully established asymptotic maximum. The static power is calculated from the current drawn from VDD only. Power drawn from the ideal bias sources is not included.

## LTspice files

- `schematics/two_stage_opamp_dc_CC1P_RZ10K5.asc` — closed-loop DC operating point.
- `schematics/two_stage_opamp_ac_loopgain_CC1P_RZ10K5.asc` — AC return-ratio test.
- `schematics/two_stage_opamp_transient_500mV_CC1P_RZ10K5.asc` — large-signal transient test.
- `simulation/README.md` — run instructions.
- `results/data/measurements.csv` — measurement table.
- `results/data/measurement_notes.md` — cursor readings and calculation details.
- `models/README.md` — external model instructions.

Place your separately obtained `cmos130.lib` in `models/` and keep the folder structure unchanged. The model itself is not included because redistribution permission has not been confirmed.

## Notes

The operating-point log showed that direct Newton iteration failed initially, but Gmin stepping successfully found an operating point. LTspice also reported a BSIM3 version warning (model version 3.200 versus simulator support 3.3.0) and PD/PS zero warnings. The generic model is not a foundry-qualified PDK, so these results describe this simulation setup and are not predictions for fabricated silicon.
