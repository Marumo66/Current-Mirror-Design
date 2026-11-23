# CMOS Analog Circuit Studies

This is where I keep my LTspice work on a few CMOS analog circuits. I started with a basic current mirror, compared it with a cascode version, then moved on to a common-source amplifier and a two-stage CMOS op-amp.

For each circuit, I keep the schematic, simulation setup, measurements and notes. Some parts are more complete than others, so I have listed the main limitations instead of treating every result as a final design.

## What is in the repository?

| Part | Circuit | What I looked at |
|---|---|---|
| [Phase 1](Phase_1_Basic_Current_Mirror/README.md) | Basic NMOS current mirror | Channel-length modulation, current mismatch and output resistance |
| [Phase 2](Phase_2_130nm_Current_Mirror_Comparison/README.md) | Basic and self-biased cascode current mirrors | Output-current variation and an output-resistance estimate |
| [Phase 3](Phase_3_Common_Source_Amplifier/README.md) | NMOS common-source stage with PMOS active load | DC operating point, AC gain and transient response |
| [Phase 4](Phase_4_Two_Stage_Operational_Amplifier/README.md) | Two-stage CMOS op-amp | DC operating point, loop gain, phase margin, bandwidth and slew-rate measurements |

## A few results

These are the values I recorded from the LTspice runs. They are tied to the circuits and model files used here.

- **Phase 1:** with LAMBDA = 0.02, the output current was 101.5426 µA at VOUT = 1.8 V, compared with a 100 µA reference. The output-resistance estimate was about 510 kΩ.
- **Phase 2:** over the 0.5–1.5 V measurement interval, the measured current variation was 7.03% for the basic mirror and 0.96% for the cascode mirror.
- **Phase 3:** the common-source stage had about 30.37 dB gain at 10 kHz and a cursor-based −3 dB bandwidth estimate of about 4.47 MHz.
- **Phase 4:** the two-stage op-amp had about 79.58 dB low-frequency return-ratio gain, 13.54 MHz cursor-based unity-gain bandwidth and 46.09° cursor-based phase margin.

The details and measurement conditions are in the README for each phase and in its `results/data/` folder.

## How the project is organised

Each phase has its own folder. The usual layout is:

- `schematics/` — LTspice schematic files (`.asc`).
- `simulation/` — netlists, measurement directives and run notes.
- `models/` — model cards or instructions for obtaining an external model.
- `results/data/` — measured values and calculations.
- `results/figures/` and `screenshots/` — plots and LTspice screenshots.
- `analysis/` and `report/` — working notes and longer write-ups.

Not every phase uses every folder.

## Running the circuits

I used LTspice 26.0.2 on macOS for the runs documented here.

1. Clone or download this repository.
2. Open the `.asc` file for the circuit you want to run.
3. Follow the instructions in that phase's `simulation/README.md` or `models/README.md`.
4. Keep the folder structure unchanged where the schematic uses a relative model path.

The Phase 1 schematics include their own simple Level-1 models. Phases 2–4 refer to a generic 130-nm BSIM3 model named `cmos130.lib`. I have not included that file because I have not confirmed that it can be redistributed. You will need to obtain it from its original source before running those schematics.

To redraw the Phase 1 comparison plot from the saved cursor readings, install Matplotlib and run:

```bash
python3 -m pip install matplotlib
python3 scripts/plot_results.py
```

This script only plots the readings already saved in the CSV. It does not run LTspice or recreate the original sweep.

## Things to keep in mind

- The Level-1 model in Phase 1 uses illustrative parameters. It is not tied to a fabrication process.
- The 130-nm BSIM3 model used in Phases 2–4 is a generic model, not a foundry-qualified PDK.
- LTspice reported BSIM3 version and PD/PS warnings for the generic model. I left the model unchanged.
- Some results are taken from selected cursor readings or measurement logs rather than a complete exported dataset. The relevant notes say which ones.
- The output-resistance values in Phase 2 are estimates from DC sweep endpoints, not small-signal values calculated from operating-point Gds.
- The Phase 4 bias voltages still come from ideal voltage sources. A transistor-level bias generator has not been built yet.
- These results are useful for comparing the circuits in the stated simulation setup. They are not predictions of fabricated-chip performance.

## Files worth opening first

- [Phase 1 — basic current mirror](Phase_1_Basic_Current_Mirror/README.md)
- [Phase 2 — current mirror comparison](Phase_2_130nm_Current_Mirror_Comparison/README.md)
- [Phase 3 — common-source amplifier](Phase_3_Common_Source_Amplifier/README.md)
- [Phase 4 — two-stage CMOS op-amp](Phase_4_Two_Stage_Operational_Amplifier/README.md)
