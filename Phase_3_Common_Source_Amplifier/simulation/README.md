# Running the Phase 3 analyses

Open the matching ASC file in LTspice 26.0.2. Before running it, put the external `cmos130.lib` file in `models/`, as described in [models/README.md](../models/README.md). Keep the folder layout unchanged because the schematics use a relative include path.

- `common_source_op_130nm.asc`: DC operating point, `.op`, with VIN = 0.45 V.
- `common_source_ac_130nm.asc`: AC sweep, `.ac dec 100 1 1G`, with VIN DC offset = 0.45 V and AC amplitude = 1.
- `common_source_transient_130nm.asc`: transient run, `.tran 0 2.5u 0 20p`, with `PULSE(0.35 0.55 1u 1n 1n 1u 2u)`.

All three files use the same circuit topology and device dimensions. The input source and active analysis directive change between files.
