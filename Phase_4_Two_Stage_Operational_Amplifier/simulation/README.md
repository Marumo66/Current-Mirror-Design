# Running the Phase 4 simulations

Before running the circuits, place a permitted copy of `cmos130.lib` in `models/`. See [models/README.md](../models/README.md). Keep the folder structure unchanged so the relative include path works.

Open the matching ASC file from `schematics/` in LTspice and run the analysis enabled in that file.

## DC operating point

Open `two_stage_opamp_dc_CC1P_RZ10K5.asc`. It uses a unity-gain feedback connection, VINP = 0.45 V, VDD = 1.5 V, CC = 1 pF, RZ = 10.5 kΩ and CL = 1 pF. The active analysis is `.op`.

## AC loop gain

Open `two_stage_opamp_ac_loopgain_CC1P_RZ10K5.asc`. A 0 V DC / 1 V AC test source is inserted in series with the feedback path. The return-ratio trace is `-V(out)/V(nfb)`. The active analysis is `.ac dec 100 1 1G`.

## Transient response

Open `two_stage_opamp_transient_500mV_CC1P_RZ10K5.asc`. It uses:

```spice
PULSE(0.25 0.75 1u 1n 1n 1u 2u)
.tran 0 10u 0 1n
```

Plot `V(out)` and `V(n003)`.

The three ASC files are separate test setups. Keep the DC, AC and transient configurations separate.
