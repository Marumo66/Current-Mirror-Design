# Next: Compliance-voltage and operating-point checks

Phase 2 has been added in [Phase_2_130nm_Current_Mirror_Comparison](../Phase_2_130nm_Current_Mirror_Comparison/README.md). It compares the basic mirror with a self-biased cascode mirror using a generic 130-nm BSIM3 model.

The next checks are:

- Find the minimum output voltage at which the output current remains within 1% of the 100 µA reference.
- Compare transistor operating points at the same output voltage.
- Estimate small-signal output resistance from the operating-point gds value.

These checks have not been completed yet.
