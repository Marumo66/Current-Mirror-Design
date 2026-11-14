# CMOS Current Mirror Design

An independent analog-circuit study using LTspice. The project starts with a basic two-transistor NMOS current mirror and examines how output voltage and channel-length modulation affect current matching and output resistance.

## Project status

- **Phase 1 — Basic NMOS current mirror:** initial simulations and analysis completed.
- **Phase 2 — Cascode current mirror:** planned.
- **Phase 3 — Architecture comparison and design trade-offs:** planned.

## Phase 1: scope

A matched NMOS pair was simulated with an illustrative Level-1 SPICE model. The reference branch used a 1.8 V supply and a 100 µA ideal current source. The output voltage was swept from 0 V to 1.8 V in 10 mV steps.

Two model settings were compared:

1. `LAMBDA=0.02 V^-1`: channel-length modulation enabled.
2. `LAMBDA=0`: channel-length modulation disabled in the idealized Level-1 model.

## Main results

- With `LAMBDA=0.02`, the measured output current at `VOUT=1.8 V` was **101.5426 µA**, or **+1.5426%** relative to the 100 µA reference.
- With `LAMBDA=0`, the measured saturation-region output current was essentially 100 µA at 0.5 V, 1.0 V, and 1.8 V.
- The finite-difference output resistance estimated from the `LAMBDA=0.02` sweep was approximately **510.13 kΩ**. This agrees with the inverse of the reported operating-point output conductance to the precision shown by LTspice.

The sampled cursor readings and operating-point values are recorded in `Phase_1_Basic_Current_Mirror/results/data/`. These are selected readings transcribed from LTspice screenshots, not the complete sweep dataset.

## Repository layout

- `Phase_1_Basic_Current_Mirror/models/` — illustrative Level-1 model cards.
- `Phase_1_Basic_Current_Mirror/simulation/netlists/` — operating-point and DC-sweep netlists for both lambda settings.
- `Phase_1_Basic_Current_Mirror/results/data/` — recorded cursor readings and operating-point data.
- `Phase_1_Basic_Current_Mirror/analysis/` — calculations and interpretation.
- `Phase_1_Basic_Current_Mirror/report/` — technical report.
- `scripts/` — script to regenerate the plot from the recorded CSV.

Native `.asc` schematics are not included in this initial upload because the final working files from the local LTspice session have not yet been added. The netlists provide the reproducible circuit description for now.

## Tools and limitations

- LTspice 26.0.2 for macOS
- Level-1 NMOS model with illustrative parameters
- Python 3 and Matplotlib for plotting

The Level-1 model is a simplified teaching model, not a foundry PDK. LTspice reported recommended-dimension warnings for the selected Level-1 MOSFET geometry. The results are therefore a model-based study, not silicon-accurate predictions for a specific process.

## Reproduce the recorded plot

Install Matplotlib and run:

```bash
python3 -m pip install matplotlib
python3 scripts/plot_results.py
```

The script plots the selected cursor readings; it does not regenerate the raw LTspice sweep.

## Data provenance

Numerical cursor readings and operating-point values were transcribed from LTspice screenshots supplied during the project. Raw screenshots containing local usernames or machine paths are not included.
