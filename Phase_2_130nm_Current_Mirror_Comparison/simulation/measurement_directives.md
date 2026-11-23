# Phase 2 measurement directives

These are the `.meas` commands used in the two schematics.

## Basic current mirror

The swept output-voltage source is named `VSWEEP`:

```spice
.meas DC IOUT_05 FIND -I(VSWEEP) AT=0.5
.meas DC IOUT_10 FIND -I(VSWEEP) AT=1.0
.meas DC IOUT_15 FIND -I(VSWEEP) AT=1.5
.meas DC IOUT_MIN MIN -I(VSWEEP) FROM=0.5 TO=1.5
.meas DC IOUT_MAX MAX -I(VSWEEP) FROM=0.5 TO=1.5
```

## Cascode current mirror

The swept output-voltage source is named `V2`:

```spice
.meas DC IOUT_05 FIND -I(V2) AT=0.5
.meas DC IOUT_10 FIND -I(V2) AT=1.0
.meas DC IOUT_15 FIND -I(V2) AT=1.5
.meas DC IOUT_MIN MIN -I(V2) FROM=0.5 TO=1.5
.meas DC IOUT_MAX MAX -I(V2) FROM=0.5 TO=1.5
```

The minus sign makes the reported output current positive for the voltage-source orientation used in these schematics.
