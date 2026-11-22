# Measurement notes

Values below were read from the LTspice 26.0.2 screenshots and output log supplied with the project.

## DC operating point

- VDD = 1.5 V
- VBP = 0.8 V
- VIN = 0.45 V
- VOUT = 1.03752 V
- Id(M1) = 93.3611 µA
- Id(M2) = −93.3611 µA (opposite SPICE reference direction)
- I(VDD) = −93.3611 µA (supply-current magnitude 93.3611 µA)
- Static power = 1.5 V × 93.3611 µA = 140.04165 µW

## AC analysis

- VIN DC offset = 0.45 V; AC amplitude = 1
- Sweep: 1 Hz to 1 GHz, 100 points/decade
- Gain at 10 kHz = 32.21699 dB
- Cursor at 9.332543 MHz read 29.216764 dB. This is about 3 dB below the 10 kHz gain (the cursor difference was 3.0002259 dB).
- Unity-gain cursor = 144.54398 MHz at +0.096279842 dB (96.279842 mdB), i.e. close to 0 dB.
- The complex transfer-function plot `V(vout)/V(n003)` was used to show magnitude and phase. No phase-margin result is claimed.

## Transient and slew rate

- VIN = `PULSE(0.35 0.55 1u 1n 1n 1u 2u)`
- Transient command = `.tran 0 2.5u 0 20p`
- Load capacitor = 1 pF
- Output falling: cursor 1 at 1.00256 µs / 1.1683505 V; cursor 2 at 1.01034 µs / 0.35220888 V. Delta t = 7.78 ns; delta V = −816.32158 mV; average falling slope magnitude = 104.926 V/µs.
- Output rising: cursor 1 at 2.00512 µs / 0.35169488 V; cursor 2 at 2.01682 µs / 1.1681467 V. Delta t = 11.7 ns; delta V = +816.45185 mV; average rising slope = 69.7822 V/µs.
- These are cursor-based average slopes over the selected transition interval, approximately 20–80% of the measured output swing. They are not the instantaneous peak of `d(V(vout))`.

## Model warnings

LTspice reported that it supports BSIM3 version 3.3.0 while the model specifies 3.200. It also reported PD = 0 and PS = 0 warnings. The model was not modified.
