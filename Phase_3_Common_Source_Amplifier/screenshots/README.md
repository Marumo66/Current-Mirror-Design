# Phase 3 screenshots

- `common_source_amplifier_schematic.png` is a screenshot taken directly from LTspice.
- `phase3_dc_operating_point.png` shows the DC operating-point log.
- `phase3_ac_response.png` shows the gain and phase response.
- `phase3_transient_response.png` shows the input pulse and inverted output waveform.

In the schematic screenshot, the blue `.op`, `.ac` and older `.tran` directives are commented out. The active transient command is `.tran 0 2.5u 0 20p`. The separate ASC files in `../schematics/` are used for the DC, AC and transient runs.
