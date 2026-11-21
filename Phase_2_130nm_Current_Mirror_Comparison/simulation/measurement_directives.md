# LTspice measurement directives

The Basic schematic uses VSWEEP as the swept output-voltage source:

.meas DC IOUT_05 FIND -I(VSWEEP) AT=0.5
.meas DC IOUT_10 FIND -I(VSWEEP) AT=1.0
.meas DC IOUT_15 FIND -I(VSWEEP) AT=1.5
.meas DC IOUT_MIN MIN -I(VSWEEP) FROM=0.5 TO=1.5
.meas DC IOUT_MAX MAX -I(VSWEEP) FROM=0.5 TO=1.5

The Cascode schematic uses V2 as the swept output-voltage source:

.meas DC IOUT_05 FIND -I(V2) AT=0.5
.meas DC IOUT_10 FIND -I(V2) AT=1.0
.meas DC IOUT_15 FIND -I(V2) AT=1.5
.meas DC IOUT_MIN MIN -I(V2) FROM=0.5 TO=1.5
.meas DC IOUT_MAX MAX -I(V2) FROM=0.5 TO=1.5

The leading minus sign makes the output current positive for the chosen voltage-source orientation.
