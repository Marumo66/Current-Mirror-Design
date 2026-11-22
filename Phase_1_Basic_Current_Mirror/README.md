# Phase 1 — Basic NMOS Current Mirror

I started with a two-transistor NMOS current mirror and simulated it in LTspice.

## LTspice source files

- [LAMBDA = 0 (.asc)](https://raw.githubusercontent.com/Marumo66/Current-Mirror-Design/main/Phase_1_Basic_Current_Mirror/schematics/Basic_Current_Mirror_Lambda0.asc)
- [LAMBDA = 0.02 (.asc)](https://raw.githubusercontent.com/Marumo66/Current-Mirror-Design/main/Phase_1_Basic_Current_Mirror/schematics/Basic_Current_Mirror_Lambda002.asc)

Both schematics contain their own Level-1 model directive, so no separate model file is needed for these two basic runs.

## Circuit settings

| Parameter | Value |
|---|---:|
| Supply voltage | 1.8 V |
| Reference current | 100 µA |
| M1 and M2 | W = 10 µm, L = 1 µm |
| Output-voltage sweep | 0–1.8 V, 0.01 V step |
| MOSFET model | Level 1 |

I ran the same circuit twice. The first run used LAMBDA = 0.02; the second used LAMBDA = 0.

## What I checked

- DC operating point of M1 and M2
- Output current as VOUT was swept
- Current mismatch relative to the 100 µA reference
- Output resistance from the DC sweep and the operating-point Gds value

The two LTspice files are in [schematics](schematics/). The measurements and calculations are in [experiment_notes.md](analysis/experiment_notes.md). The full write-up is in [phase_1_technical_report.md](report/phase_1_technical_report.md).

## Limitation

The Level-1 model is only used here to study the basic effect of channel-length modulation. It is not a foundry model. LTspice also showed dimension warnings for the selected W and L values.
