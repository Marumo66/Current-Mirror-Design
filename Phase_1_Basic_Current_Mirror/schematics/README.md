# Native LTspice schematics

The final native `.asc` files from the local LTspice 26.0.2 session are not included in this initial upload. An earlier generated draft was not independently verified in the user's LTspice environment and is intentionally excluded.

The four `.cir` netlists in `../simulation/netlists/` provide the circuit topology and model settings needed to reproduce the analyses.

Recommended native schematic files to add after final local verification:
- `Basic_Current_Mirror_lambda0p02.asc` — measured baseline (`LAMBDA=0.02`)
- `Basic_Current_Mirror_lambda0.asc` — controlled comparison (`LAMBDA=0`)

Before committing, open each file in LTspice, verify the topology, run the corresponding analysis, and make sure the model and sweep settings match the recorded data.
