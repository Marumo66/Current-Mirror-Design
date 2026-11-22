# Running the analyses

Open the matching `.asc` file in LTspice 26.0.2. Put the external `cmos130.lib` file in `models/` as described in `models/README.md`. The include path in the schematics is relative to the `schematics/` folder.

- `common_source_op_130nm.asc`: runs `.op` with VIN = 0.45 V.
- `common_source_ac_130nm.asc`: runs `.ac dec 100 1 1G` with VIN DC offset = 0.45 V and AC amplitude = 1.
- `common_source_transient_130nm.asc`: runs `.tran 0 2.5u 0 20p` with `PULSE(0.35 0.55 1u 1n 1n 1u 2u)`.

The three files use the same circuit topology and device dimensions. Only the input source and active analysis directive differ.
