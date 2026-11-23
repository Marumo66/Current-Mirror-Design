# Phase 3 schematic files

The three ASC files are copies of the submitted `Draft1(2).asc`, split into separate setups for DC operating point, AC sweep and transient pulse analysis.

I kept the transistor connections, W/L values, bias sources and load capacitor the same. The input source, active analysis command and model include path are the parts that differ between the three files.

The original schematic had transient measurements over 20–100 µs, but the pulse simulation ends at 2.5 µs. I removed those old measurement directives from the repository copies.

I did not rerun the three split ASC files in LTspice after preparing them. The measurements in this phase come from the earlier LTspice sessions and are listed in `results/data/measurement_notes.md`.
