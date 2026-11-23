# Phase 1 — Results at a glance

The reference current was 100 µA. I compared the same two-transistor mirror with LAMBDA = 0.02 and LAMBDA = 0.

| Measurement | LAMBDA = 0.02 | LAMBDA = 0 |
|---|---:|---:|
| IOUT at 0.5 V | 98.994235 µA | 99.999997 µA |
| IOUT at 1.0 V | 99.974372 µA | 99.999997 µA |
| IOUT at 1.8 V | 101.542600 µA | 100.000000 µA |
| M2 Gds from operating-point log | 1.96 µS | 0.00 S (displayed precision) |

For LAMBDA = 0.02, the output current at 1.8 V is 1.5426% above the reference current.

Using the 0.5 V and 1.8 V readings, I estimated the output resistance as:

```text
g_out = (101.542600 - 98.994235) µA / (1.8 - 0.5) V
      = 1.96028 µS

r_out = 1 / g_out
      ≈ 510.13 kΩ
```

This is close to the value calculated from M2's operating-point Gds.

The values are selected LTspice readings, not a full sweep export. See [experiment_notes.md](analysis/experiment_notes.md) for the readings and calculations.
