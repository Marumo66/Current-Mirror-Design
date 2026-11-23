# Phase 4 — Measurement notes

I read these values from the LTspice 26.0.2 screenshots and operating-point log saved on 22 November 2026. The circuit uses the same generic 130-nm BSIM3 model as the earlier phases.

## Design conditions

- VDD = 1.5 V
- CL = 1 pF
- CC = 1 pF
- RZ = 10.5 kΩ
- Temperature = 27 °C
- M1–M7: W = 10 µm, L = 1 µm
- Ideal DC bias sources: VTAIL = 0.31 V, VBN2 = 0.292 V

## DC operating point

- VINP = 0.45 V; the inverting input is connected to the output for unity-gain feedback.
- VOUT = 0.449782 V
- V(n1) = 1.14753 V
- V(n2) = 1.12147 V
- V(tail) = 0.15207 V
- I(VDD) = −18.2271 µA (supply-current magnitude = 18.2271 µA)
- Core static power from VDD = 1.5 V × 18.2271 µA = 27.34065 µW

The operating-point log showed that Direct Newton did not find the operating point at first. Gmin stepping then succeeded. The displayed operating point is the result after that convergence method.

VTAIL and VBN2 are external ideal bias sources. Their power is not included in the VDD-only core-power figure.

## AC loop-gain measurement

- AC sweep: 1 Hz to 1 GHz, 100 points/decade.
- Test source VTEST: 0 V DC and 1 V AC, inserted in series with the feedback path.
- Return-ratio expression: `-V(out)/V(nfb)`.
- At 1 Hz, the cursor read 79.578034 dB and −0.01564061° (the phase readout is in millidegrees in the LTspice cursor window).
- Near the 0 dB crossing, the cursor read 13.543947 MHz, +0.060451523 dB and −133.91447°.
- The corresponding approximate phase margin is 180° − 133.91447° = 46.08553°.

The unity-gain frequency and phase margin are cursor readings close to the 0 dB crossing. They are not interpolated exact crossing values.

## Transient response

The final transient source uses:

```text
PULSE(0.25 0.75 1u 1n 1n 1u 2u)
.tran 0 10u 0 1n
```

The input is plotted as `V(n003)` and the output as `V(out)`.

### Rising transition, 500 mV input step

- Cursor 1 = 1.0123105 µs / 349.56104 mV
- Cursor 2 = 1.0399619 µs / 649.40219 mV
- Δt = 27.651425 ns
- ΔV = 299.84115 mV
- 20–80% average output slope = 10.8436 V/µs

### Falling transition, 500 mV input step

- Cursor 1 = 2.0656116 µs / 650.07662 mV
- Cursor 2 = 2.1420038 µs / 350.10757 mV
- Δt = 76.392194 ns
- ΔV = −299.96905 mV
- 80–20% average output slope magnitude = 3.9267 V/µs

### Input step-amplitude check

The measured 20–80% rising slopes were:

| Input step | Rising slope |
|---:|---:|
| 200 mV | 8.42631 V/µs |
| 300 mV | 9.94791 V/µs |
| 400 mV | 10.548 V/µs |
| 500 mV | 10.8436 V/µs |

The rising slope was still increasing with the input step. I therefore report 10.8436 V/µs as the average slope measured for the 500 mV step, not as a proven asymptotic maximum slew rate.

The falling measurements for 200 mV and 500 mV input steps were 4.10908 V/µs and 3.9267 V/µs respectively.

All slew-rate values are average slopes over the selected 20–80% or 80–20% output transition interval, not instantaneous peak derivatives.

## Model and simulation limitations

LTspice reported that the model specifies BSIM3 version 3.200 while LTspice supports version 3.3.0. It also reported PD = 0 and PS = 0 warnings. I did not change the model to remove these warnings.

The model is generic and is not a foundry-qualified PDK. The measurements should not be treated as silicon predictions.
