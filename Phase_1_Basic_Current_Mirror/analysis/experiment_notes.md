# Basic NMOS Current Mirror — Experiment Notes

## 1. Circuit

The circuit has two matched NMOS transistors.

- M1 is diode-connected: its drain and gate are tied together.
- M2 uses the same gate voltage as M1.
- Both sources and bulks are connected to ground.
- A 100 µA ideal current source feeds the reference branch from a 1.8 V supply.
- VSWEEP sets the voltage at the drain of M2.

The model used for the first run was:

```spice
.model NM NMOS(Level=1 VTO=0.7 KP=200u LAMBDA=0.02)
```

For the second run, only LAMBDA was changed from 0.02 to 0.

## 2. DC sweep readings

The following values were read from the LTspice plot cursors. They are selected points from the sweep, not the full 181-point dataset.

| VOUT (V) | IOUT, LAMBDA = 0.02 (µA) | IOUT, LAMBDA = 0 (µA) |
|---:|---:|---:|
| 0.1 | 52.719635 | — |
| 0.2 | 85.569722 | — |
| 0.3 | 98.430275 | — |
| 0.5 | 98.994235 | 99.999997 |
| 1.0 | 99.974372 | 99.999997 |
| 1.8 | 101.542600 | 100.000000 |

I plotted `-I(VSWEEP)` as the output current. LTspice reports current through a voltage source using its own reference direction, so the minus sign gives the current delivered by the mirror to the output node.

## 3. Current mismatch

I calculated the signed mismatch relative to the 100 µA reference current using:

```text
Mismatch (%) = (IOUT - IREF) / IREF * 100
```

For LAMBDA = 0.02:

| VOUT (V) | Mismatch (%) |
|---:|---:|
| 0.1 | -47.280365 |
| 0.2 | -14.430278 |
| 0.3 | -1.569725 |
| 0.5 | -1.005765 |
| 1.0 | -0.025628 |
| 1.8 | +1.542600 |

At low VOUT, M2 is not in saturation, so its current is well below the reference current. The 0.5 V, 1.0 V and 1.8 V points are in the saturation region for this setup.

With LAMBDA = 0, the three sampled saturation-region currents are essentially 100 µA.

## 4. Channel-length modulation

For the simplified Level-1 model, the saturation-region drain current can be written approximately as:

```text
ID = 0.5 * KP * (W/L) * VOV^2 * (1 + LAMBDA * VDS)
```

Here, VOV is the overdrive voltage (VGS - VTH).

When LAMBDA is non-zero, ID changes with VDS. M1 and M2 have different drain-source voltages, so their currents do not match exactly. When I set LAMBDA to zero, this dependence is removed from the simplified model. The output current then stays close to 100 µA at the sampled saturation-region points.

This comparison only shows the effect of this one model parameter. It does not include all non-ideal effects found in real MOSFETs.

## 5. Output resistance

I estimated the output conductance from the LAMBDA = 0.02 sweep using the readings at 0.5 V and 1.8 V:

```text
g_out = (101.542600 - 98.994235) µA / (1.8 - 0.5) V
      = 1.96028 µS

r_out = 1 / g_out
      = approximately 510.13 kΩ
```

The LTspice operating-point log showed Gds = 1.96 µS for M2. Its inverse is approximately 510.2 kΩ, which agrees with the estimate from the sweep to the precision displayed in the log.

For LAMBDA = 0, LTspice displayed Gds as 0.00e+00 S. In this idealized Level-1 model, that means the small-signal output resistance is unbounded in saturation. It should not be taken as the output resistance of a real transistor.

## 6. Operating-point readings

The values below are transcribed from the LTspice device operating-point table. Some values are rounded by LTspice.

### LAMBDA = 0.02

| Parameter | M1 | M2 |
|---|---:|---:|
| Id | 1.00e-04 A | 1.02e-04 A |
| Vgs | 1.01 V | 1.01 V |
| Vds | 1.01 V | 1.80 V |
| Vbs | 0.00 V | 0.00 V |
| Vth | 0.70 V | 0.70 V |
| Vdsat | 0.313 V | 0.313 V |
| Gm | 6.39e-04 S | 6.49e-04 S |
| Gds | 1.96e-06 S | 1.96e-06 S |

### LAMBDA = 0

The node listing showed VREF = 1.01623 V.

| Parameter | M1 | M2 |
|---|---:|---:|
| Id | 1.00e-04 A | 1.00e-04 A |
| Vgs | 1.02 V | 1.02 V |
| Vds | 1.02 V | 1.80 V |
| Vbs | 0.00 V | 0.00 V |
| Vth | 0.70 V | 0.70 V |
| Vdsat | 0.316 V | 0.316 V |
| Gm | 6.32e-04 S | 6.32e-04 S |
| Gds | 0.00e+00 S | 0.00e+00 S |

## 7. LTspice warning

LTspice reported that the selected transistor length and width were shorter/narrower than recommended for a Level-1 MOSFET. The operating-point calculation and DC sweep converged, but this warning is a limitation of the setup. The model parameters are illustrative and are not taken from a foundry PDK.
