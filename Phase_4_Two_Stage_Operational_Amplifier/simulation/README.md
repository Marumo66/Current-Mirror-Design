# Running the Phase 4 simulations

1. Place your permitted copy of `cmos130.lib` in `models/`.
2. Open the required `.asc` file from `schematics/` in LTspice.
3. Run the analysis enabled in that schematic.
4. Keep the folder layout unchanged so the relative model include resolves.

## DC operating point

Open `two_stage_opamp_dc_CC1P_RZ10K5.asc`. It uses a unity-gain feedback connection, VINP = 0.45 V, VDD = 1.5 V, CC = 1 pF, RZ = 10.5 kΩ and CL = 1 pF. The active analysis is `.op`.

## AC loop gain

Open `two_stage_opamp_ac_loopgain_CC1P_RZ10K5.asc`. A 0 V DC / 1 V AC test source is inserted in series with the feedback path. The measured return-ratio trace is `-V(out)/V(nfb)`. The active analysis is `.ac dec 100 1 1G`.

## Transient response

Open `two_stage_opamp_transient_500mV_CC1P_RZ10K5.asc`. It uses `PULSE(0.25 0.75 1u 1n 1n 1u 2u)` and `.tran 0 10u 0 1n`. Plot `V(out)` and `V(n003)`.

The three files are separate test setups. Do not overwrite one with another; keep the DC, AC and transient configurations separate.
