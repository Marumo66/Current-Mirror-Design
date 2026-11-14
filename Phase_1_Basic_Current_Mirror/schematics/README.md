# LTspice schematics

These are the two schematic files used for the DC-sweep comparison:

- [Basic_Current_Mirror_Lambda002.asc](Basic_Current_Mirror_Lambda002.asc) — LAMBDA = 0.02
- [Basic_Current_Mirror_Lambda0.asc](Basic_Current_Mirror_Lambda0.asc) — LAMBDA = 0

Both files use the same circuit, bias values and transistor dimensions. Only the LAMBDA value changes.

The active analysis in these two schematics is:

```spice
.options logopinfo
.dc VSWEEP 0 1.8 0.01
```

The `.op` directive is commented out in the schematics. Operating-point runs are provided separately in [simulation/netlists](../simulation/netlists/).

The current-source value is written as `100u` in the repository copy. This is the SPICE suffix for 100 microamps and is equivalent to the `100µ` display in LTspice.
