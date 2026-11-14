# Basic NMOS Current Mirror — Experiment Notes

## 1. Circuit and model

The circuit uses two matched NMOS devices. M1 is diode-connected and establishes the common gate voltage. M2 uses the same gate voltage and provides the mirrored output current. The source and bulk terminals are at ground. An ideal 100 µA current source feeds the reference branch from a 1.8 V supply.

The model is a simplified Level-1 NMOS model:

```spice
.model NM NMOS(Level=1 VTO=0.7 KP=200u LAMBDA=0.02)
```

The controlled comparison changes only `LAMBDA` from `0.02` to `0`.

## 2. DC sweep measurements

The CSV file contains selected cursor readings transcribed from LTspice. These are sampled points from the sweep, not the complete 181-point sweep dataset.

| VOUT (V) | IOUT, λ=0.02 (µA) | IOUT, λ=0 (µA) |
|---:|---:|---:|
| 0.1 | 52.719635 | — |
| 0.2 | 85.569722 | — |
| 0.3 | 98.430275 | — |
| 0.5 | 98.994235 | 99.999997 |
| 1.0 | 99.974372 | 99.999997 |
| 1.8 | 101.542600 | 100.000000 |

The output current is read as `-I(VSWEEP)` because of LTspice's voltage-source current reference direction.

## 3. Current mismatch

The signed current mismatch is defined as:

[
	ext{Mismatch}(%)=rac{I_{OUT}-I_{REF}}{I_{REF}}	imes100%.
]

For `λ=0.02`, the measured mismatch is:

| VOUT (V) | Mismatch (%) |
|---:|---:|
| 0.1 | -47.280365 |
| 0.2 | -14.430278 |
| 0.3 | -1.569725 |
| 0.5 | -1.005765 |
| 1.0 | -0.025628 |
| 1.8 | +1.542600 |

For `λ=0`, the three sampled points at 0.5 V, 1.0 V, and 1.8 V are essentially 100 µA. This does not imply a constant current below the saturation region; at low output voltage M2 still enters the triode region.

## 4. Channel-length modulation interpretation

For the simplified saturation-region model:

[
I_Dapproxrac{1}{2}K_Prac{W}{L}V_{OV}^{2}(1+lambda V_{DS}).
]

With nonzero `λ`, current depends on `VDS`. Since M1 and M2 generally have different drain-source voltages, their drain currents do not match exactly. With `λ=0`, this particular model term is removed, so the saturation-region current becomes independent of `VDS` in the idealized model.

This is a model-controlled demonstration. Real devices have additional non-idealities not represented by this simple model.

## 5. Output resistance

Using the `λ=0.02` sweep readings at 0.5 V and 1.8 V:

[
 g_{out}approxrac{101.542600-98.994235}{1.8-0.5}
 =1.96028,mu S
]

[
 r_{out}approxrac{1}{g_{out}}approx510.13,kOmega.
]

The LTspice operating-point log reported `Gds = 1.96 µS` for M2, corresponding to approximately 510.2 kΩ. The agreement is within the precision of the displayed values.

For `λ=0`, LTspice reported `Gds = 0.00e+00 S` to the displayed precision. In the idealized Level-1 model this implies unbounded small-signal output resistance in saturation. It must not be interpreted as infinite output resistance in a real MOSFET.

## 6. Operating-point snapshot

### λ = 0.02

LTspice displayed, to the precision shown in its log:

- M1: `Id=1.00e-04 A`, `Vgs=1.01 V`, `Vds=1.01 V`, `Vdsat=0.313 V`, `gm=6.39e-04 S`, `gds=1.96e-06 S`.
- M2: `Id=1.02e-04 A` (rounded display), `Vgs=1.01 V`, `Vds=1.80 V`, `Vdsat=0.313 V`, `gm=6.49e-04 S`, `gds=1.96e-06 S`.

### λ = 0

LTspice displayed:

- `VREF=1.01623 V`.
- M1 and M2: `Id=1.00e-04 A`, `Vgs=1.02 V`, `Vds=1.02 V` and `1.80 V`, respectively, `Vdsat=0.316 V`, `gm=6.32e-04 S`, and `gds=0.00e+00 S`.

Values are transcribed from the visible LTspice output and retain its rounding.

## 7. Simulator warnings and limitations

LTspice reported that the selected MOSFET length and width were shorter/narrower than recommended for a Level-1 MOSFET. The simulations converged, but the warning and simplified model should be documented. These results are appropriate for learning the first-order behavior of the current mirror; they are not evidence of a foundry-qualified design.
