# Phase 1 Report — Basic NMOS Current Mirror

## Aim

I wanted to see how well a simple NMOS current mirror copies a 100 µA reference current, and how the result changes when channel-length modulation is included in the MOSFET model.

## Circuit and simulation setup

I used two matched NMOS transistors in LTspice. M1 was diode-connected, and its gate was connected to the gate of M2. Both sources and bulks were grounded.

| Parameter | Value |
|---|---:|
| Supply voltage | 1.8 V |
| Reference current | 100 µA |
| Width of M1 and M2 | 10 µm |
| Length of M1 and M2 | 1 µm |
| Model threshold voltage | 0.7 V |
| KP | 200 µA/V² |
| LAMBDA | 0.02 and 0 |
| DC sweep | 0 to 1.8 V, step 0.01 V |

I first ran the circuit with LAMBDA = 0.02. I then copied the circuit and changed only LAMBDA to zero.

The model is a simple Level-1 model:

```spice
.model NM NMOS(Level=1 VTO=0.7 KP=200u LAMBDA=0.02)
```

## Results

### Output current

The table shows selected cursor readings from the LTspice sweep. It does not contain every simulation point.

| VOUT (V) | IOUT, LAMBDA = 0.02 (µA) | IOUT, LAMBDA = 0 (µA) |
|---:|---:|---:|
| 0.1 | 52.719635 | — |
| 0.2 | 85.569722 | — |
| 0.3 | 98.430275 | — |
| 0.5 | 98.994235 | 99.999997 |
| 1.0 | 99.974372 | 99.999997 |
| 1.8 | 101.542600 | 100.000000 |

With LAMBDA = 0.02, the output current at 1.8 V was 101.5426 µA. Relative to the 100 µA reference, the mismatch was +1.5426%.

With LAMBDA = 0, the three measured saturation-region points were essentially 100 µA.

At low output voltage, the output transistor is not in saturation, so the output current is lower. This is visible in the readings at 0.1 V and 0.2 V.

### Channel-length modulation

In the simplified Level-1 saturation model, the drain current is approximately:

```text
ID = 0.5 * KP * (W/L) * VOV^2 * (1 + LAMBDA * VDS)
```

When LAMBDA is 0.02, the current depends on VDS. M1 and M2 do not have the same VDS, so the output current is not exactly equal to the reference current.

When LAMBDA is set to zero, this term disappears from the model. In the saturation region, the output current stays close to 100 µA in the measured points.

### Output resistance

I estimated the output conductance using two points from the LAMBDA = 0.02 sweep:

```text
g_out = (101.542600 - 98.994235) µA / (1.8 - 0.5) V
      = 1.96028 µS

r_out = 1 / g_out
      = approximately 510.13 kΩ
```

The LTspice operating-point log showed Gds = 1.96 µS for M2. This corresponds to about 510.2 kΩ and agrees with the estimate from the sweep.

For LAMBDA = 0, LTspice displayed Gds as zero to the shown precision. This is the result of the idealized model setting, not a claim that a real MOSFET has infinite output resistance.

## Limitations

- The Level-1 MOSFET model uses illustrative parameters and is not a foundry PDK.
- LTspice warned that the selected W and L dimensions were outside its recommended range for this model.
- The current readings are selected points copied from LTspice cursor screenshots, not the full sweep dataset.
- The operating-point values are rounded to the precision shown by LTspice.

## Conclusion

The simulation showed the expected first-order effect of channel-length modulation. With LAMBDA = 0.02, the output current changed with output voltage and the estimated output resistance was about 510 kΩ. With LAMBDA = 0, the output current was almost constant in the measured saturation-region points.

This basic circuit will be the reference for the next part of the project, where I will build and test a cascode current mirror.
