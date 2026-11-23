# Phase 3 — Measurement notes

I copied these readings from the LTspice operating-point log and cursor windows during the re-check on 22 November 2026.

## DC operating point

- VDD = 1.5 V
- VBP = 0.8 V
- VIN = 0.45 V
- VOUT = 1.03752 V
- Id(M1) = 93.3611 µA
- Id(M2) = −93.3611 µA (opposite SPICE reference direction)
- I(VDD) = −93.3611 µA (supply-current magnitude = 93.3611 µA)
- Static power = 1.5 V × 93.3611 µA = 140.04165 µW

## AC analysis

- VIN DC offset = 0.45 V; AC amplitude = 1
- Sweep: 1 Hz to 1 GHz, 100 points/decade
- Gain at 1 Hz = 30.373602 dB
- Gain at 10 kHz = 30.37358 dB
- Cursor reference near the low-frequency plateau: 31.622777 kHz, 30.37339 dB
- Cursor near the −3 dB point: 4.4668359 MHz, 27.32431 dB
- The two cursor readings differ by 3.0490705 dB. I therefore report the −3 dB bandwidth as an approximate cursor estimate of 4.47 MHz, not an interpolated exact crossing.
- Near-unity-gain cursor: 144.54398 MHz at +0.096279842 dB (96.279842 mdB). This is close to 0 dB, but it is not an exact zero crossing.
- The plotted signal was V(vout); the input source AC magnitude was 1. No phase-margin result is claimed.

## Transient response and slew rate

- VIN = `PULSE(0.35 0.55 1u 1n 1n 1u 2u)`
- Transient command = `.tran 0 2.5u 0 20p`
- Load capacitor = 1 pF

### Output falling transition

- Cursor 1 = 1.0025891 µs / 1.165109 V
- Cursor 2 = 1.01036 µs / 0.35033801 V
- Δt = 7.7708818 ns
- ΔV = −814.77098 mV
- Average falling slope magnitude = 104.849 V/µs

### Output rising transition

- Cursor 1 = 2.0051032 µs / 0.35047021 V
- Cursor 2 = 2.016668 µs / 1.1596267 V
- Δt = 11.576811 ns
- ΔV = +809.15652 mV
- Average rising slope = 69.8946 V/µs

The cursor points are approximately at the 20% and 80% levels of the observed output swing. These are average slopes over the selected intervals, not the instantaneous peak of `d(V(vout))`.

## Model warnings

LTspice reported that it supports BSIM3 version 3.3.0 while the model specifies 3.200. It also reported PD = 0 and PS = 0 warnings. I did not modify the model. It is a generic model, not a foundry-qualified PDK.
