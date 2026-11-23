# Phase 4 — Two-Stage CMOS Operational Amplifier

For this part I put together a two-stage CMOS op-amp in LTspice. The first stage is an NMOS differential pair with a PMOS current-mirror active load. The second stage is a PMOS common-source device with an NMOS current-sink load. I added a Miller compensation capacitor and a series resistor.

## Circuit

- M1 and M2: NMOS differential pair
- M3 and M4: PMOS current-mirror active load
- M5: NMOS tail current source
- M6: PMOS common-source second stage
- M7: NMOS current-sink load
- CC and RZ: Miller compensation network

All seven MOSFETs currently use W = 10 µm and L = 1 µm.

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

The VTAIL and VBN2 voltages are supplied by ideal voltage sources for now. I have not built a transistor-level bias generator yet.

## Current measurements

| Measurement | Result |
|---|---:|
| Low-frequency return-ratio gain | 79.58 dB |
| Unity-gain bandwidth (cursor estimate) | ≈ 13.54 MHz |
| Phase margin (cursor estimate) | ≈ 46.09° |
| Rising output slope, 500 mV step, 20–80% | 10.84 V/µs |
| Falling output slope, 500 mV step, 80–20% | 3.93 V/µs |
| Quiescent core power from VDD | 27.34 µW |

For the AC test I inserted a 0 V DC / 1 V AC test source in series with the feedback path and plotted `-V(out)/V(nfb)`. The UGBW and phase margin above are cursor readings near the 0 dB crossing, not interpolated exact values.

The slew-rate values are average slopes over the selected output-voltage intervals. The rising slope continued to increase as I raised the input step from 200 mV to 500 mV, so 10.84 V/µs is the result for the 500 mV step, not a proven maximum slew rate.

The power figure includes current drawn from VDD only. It does not include power from the ideal bias sources.

## LTspice files

- [DC operating-point schematic](schematics/two_stage_opamp_dc_CC1P_RZ10K5.asc)
- [AC loop-gain schematic](schematics/two_stage_opamp_ac_loopgain_CC1P_RZ10K5.asc)
- [Transient schematic](schematics/two_stage_opamp_transient_500mV_CC1P_RZ10K5.asc)
- [Run instructions](simulation/README.md)

Keep the folder structure unchanged and place a separately obtained `cmos130.lib` in `models/`. The schematics refer to it with a relative path. I have not included the model because I have not confirmed that it can be redistributed. See [models/README.md](models/README.md).

## Measurement notes and limitations

The individual cursor readings and calculations are in [measurement_notes.md](results/data/measurement_notes.md). The current screenshots are in [screenshots/](screenshots/).

The operating-point log showed that Direct Newton did not find the operating point at first, but Gmin stepping succeeded. LTspice also reported a BSIM3 version warning (model version 3.200 versus simulator support for 3.3.0) and PD/PS zero warnings. I left the model unchanged.

The model is a generic 130-nm BSIM3 model, not a foundry-qualified PDK. These results describe this LTspice setup and should not be treated as predictions for a fabricated chip.
