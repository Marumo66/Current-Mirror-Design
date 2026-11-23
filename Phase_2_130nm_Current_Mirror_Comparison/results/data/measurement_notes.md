# Phase 2 — Measurement notes

I copied these values from the LTspice 26.0.2 SPICE Output Log screenshots saved with this project. The log reports current in amperes; I have written the values below in microamperes to make them easier to read.

## Basic current mirror

- `.meas DC IOUT_05 FIND -I(VSWEEP) AT=0.5` → 100.427823782 µA
- `.meas DC IOUT_10 FIND -I(VSWEEP) AT=1.0` → 104.217455373 µA
- `.meas DC IOUT_15 FIND -I(VSWEEP) AT=1.5` → 107.461441075 µA
- `.meas DC IOUT_MIN MIN -I(VSWEEP) FROM=0.5 TO=1.5` → 100.427823782 µA
- `.meas DC IOUT_MAX MAX -I(VSWEEP) FROM=0.5 TO=1.5` → 107.461441075 µA

## Cascode current mirror

- `.meas DC IOUT_05 FIND -I(V2) AT=0.5` → 99.0781554719 µA
- `.meas DC IOUT_10 FIND -I(V2) AT=1.0` → 99.9996773317 µA
- `.meas DC IOUT_15 FIND -I(V2) AT=1.5` → 100.038356322 µA
- `.meas DC IOUT_MIN MIN -I(V2) FROM=0.5 TO=1.5` → 99.0781554719 µA
- `.meas DC IOUT_MAX MAX -I(V2) FROM=0.5 TO=1.5` → 100.038356322 µA

## Conditions and warnings

- LTspice: 26.0.2 for macOS
- Temperature: 27 °C
- Reference current: 100 µA
- Supply voltage: 1.5 V
- DC sweep: 0–1.5 V in 5 mV steps
- Comparison interval: 0.5–1.5 V

Both runs reported a BSIM3 version warning (LTspice reports support for 3.3.0; the model specifies 3.200) and warnings that PD and PS are zero and less than W. I did not change the model.
