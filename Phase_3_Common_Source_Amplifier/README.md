# Phase 3 — Common-Source Amplifier

After the current-mirror comparison, I built a common-source stage with an NMOS input transistor and a PMOS active load. I checked its DC operating point, AC response and transient response in LTspice.

This is a single-stage amplifier. It is separate from the two-stage op-amp in Phase 4.

## Circuit and setup

![Common-source amplifier schematic](screenshots/common_source_amplifier_schematic.png)

- M1: NMOS, W = 10 µm, L = 1 µm
- M2: PMOS, W = 10 µm, L = 1 µm
- VDD = 1.5 V
- PMOS gate bias, VBP = 0.8 V
- NMOS input bias = 0.45 V for DC and AC analyses
- Load capacitor, CL = 1 pF
- Temperature = 27 °C
- Model: generic 130-nm BSIM3 (`nMOSFET` and `pMOSFET`)

## Results

| Measurement | Result |
|---|---:|
| Output DC voltage | 1.03752 V |
| Quiescent supply current | 93.3611 µA |
| Static power from VDD | 140.04 µW |
| Gain at 10 kHz | 30.37358 dB |
| −3 dB bandwidth (cursor estimate) | ≈ 4.47 MHz |
| Near-unity-gain point | 144.54398 MHz |
| Output rising slew rate | 69.8946 V/µs |
| Output falling slew rate | 104.849 V/µs |

The bandwidth estimate comes from a cursor reading at 4.4668359 MHz and 27.32431 dB, about 3.05 dB below the low-frequency gain. The near-unity-gain cursor reading was +0.0963 dB, so I have not called it an exact 0 dB crossing.

The slew rates are average slopes between cursor points over the 20–80% and 80–20% parts of the output transition. They are not peak values of the numerical derivative.

## LTspice files

- [DC operating-point schematic](schematics/common_source_op_130nm.asc)
- [AC analysis schematic](schematics/common_source_ac_130nm.asc)
- [Transient analysis schematic](schematics/common_source_transient_130nm.asc)

The three files use the same circuit topology and device dimensions. They have different input sources and active analysis directives. See [simulation/README.md](simulation/README.md) for run details.

Keep the folder structure and place a separately obtained `cmos130.lib` file in `models/`. The schematics refer to it using `../models/cmos130.lib`. I have not included the model because I have not confirmed its redistribution terms. See [models/README.md](models/README.md).

## Screenshots and data

- [DC operating point](screenshots/phase3_dc_operating_point.png)
- [AC response](screenshots/phase3_ac_response.png)
- [Transient response](screenshots/phase3_transient_response.png)
- [Measured values](results/data/measurements.csv)
- [Cursor readings and calculations](results/data/measurement_notes.md)

## Notes and limitations

The ASC files were split into separate DC, AC and transient setups from the submitted schematic. The topology, device dimensions, bias sources and load capacitor were kept the same. The split files were not run again in LTspice after they were prepared; the recorded values come from the LTspice sessions described in the measurement notes.

LTspice reported a BSIM3 version warning (the model specifies 3.200) and PD = 0 / PS = 0 warnings. I left the model unchanged. It is a generic model, not a foundry-qualified PDK, so these results describe this simulation setup rather than a fabricated device.

I did not report phase margin for this stage. It is an open-loop common-source amplifier, and phase margin was not measured here.
