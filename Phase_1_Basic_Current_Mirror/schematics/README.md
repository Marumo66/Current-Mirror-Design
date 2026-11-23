# Phase 1 schematic files

These are the two schematics I used for the DC-sweep comparison:

- [Basic_Current_Mirror_Lambda002.asc](Basic_Current_Mirror_Lambda002.asc) — LAMBDA = 0.02
- [Basic_Current_Mirror_Lambda0.asc](Basic_Current_Mirror_Lambda0.asc) — LAMBDA = 0

The circuit, bias values and transistor dimensions are the same in both files. Only LAMBDA changes.

The active analysis is:

```spice
.options logopinfo
.dc VSWEEP 0 1.8 0.01
```

The `.op` directive is commented out in these schematics. Separate operating-point netlists are in [simulation/netlists](../simulation/netlists/).

The current source is written as `100u`, which is the SPICE suffix for 100 microamps.
