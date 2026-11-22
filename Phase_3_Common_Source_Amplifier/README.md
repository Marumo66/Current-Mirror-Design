# Phase 3 — Common-Source Amplifier

I built this NMOS common-source stage with a PMOS active load in LTspice. I checked its DC operating point, AC response and transient response. This is a single-stage amplifier exercise, not a two-stage op-amp.

## Circuit

![Common-source amplifier schematic](screenshots/common_source_amplifier_schematic.png)

*LTspice capture. The blue analysis directives are commented out; the active transient command is `.tran 0 2.5u 0 20p`.*

- M1: NMOS, W = 10 µm, L = 1 µm
- M2: PMOS, W = 10 µm, L = 1 µm
- VDD = 1.5 V
- PMOS gate bias, VBP = 0.8 V
- NMOS input bias = 0.45 V for the DC and AC runs
- Load capacitor, CL = 1 pF
- Temperature = 27 °C
- Device model: generic 130-nm BSIM3 (`nMOSFET` and `pMOSFET`)

## Results

| Measurement | Result |
|---|---:|
| Output DC voltage | 1.03752 V |
| Quiescent supply current | 93.3611 µA |
| Static power from VDD | 140.04 µW |
| Low-frequency gain at 10 kHz | 32.21699 dB |
| −3 dB bandwidth | 9.332543 MHz |
| Unity-gain crossing (cursor, approximately 0 dB) | 144.54398 MHz |
| Output rising slew rate, 20–80% cursor interval | 69.7822 V/µs |
| Output falling slew rate, 80–20% cursor interval | 104.926 V/µs |

The slew-rate values are average slopes measured between two output-voltage cursor points during the transitions. They are not the peak value of the numerical derivative trace.

The three ASC files are separate analysis setups based on the supplied final schematic. They were not re-run after packaging; the recorded values come from the LTspice output logs and cursor readings documented in `results/data/measurement_notes.md`.

## Files

- `schematics/common_source_op_130nm.asc` — DC operating-point setup.
- `schematics/common_source_ac_130nm.asc` — AC sweep setup.
- `schematics/common_source_transient_130nm.asc` — pulse-response setup used for the slew-rate measurements.
- `results/data/measurements.csv` — summary of the recorded values.
- `results/data/measurement_notes.md` — measurement points, calculations and limitations.
- `screenshots/README.md` — note about screenshots.
- `models/README.md` — notes about the external model file.
- `simulation/README.md` — how to run the three analyses.

## Notes

The simulations were run in LTspice 26.0.2 on macOS using the supplied generic model. LTspice warned that the model specifies BSIM3 version 3.200 while the simulator reports support for version 3.3.0. It also warned that PD and PS are zero. The model was left unchanged. It is not a foundry-qualified PDK, so these results describe this simulation setup and should not be treated as silicon predictions.

The AC phase response was inspected in the Bode plot. No phase-margin value is claimed here: phase margin is a loop-stability metric and was not measured for this open-loop common-source stage.

The model file is not included because its redistribution terms have not been confirmed. See `models/README.md`.
