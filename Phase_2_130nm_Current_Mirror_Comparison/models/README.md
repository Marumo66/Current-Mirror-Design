# Model file

The Phase 2 schematics use the model name `nMOSFET` from an external file called `cmos130.lib`.

The model used for the recorded runs is a generic 130-nm BSIM3 model. It is not a foundry-qualified PDK. The copy used for those runs had this SHA-256 hash:

```text
ac9aa8376dd3fb9cf7033e8791b9f76ae07bf2c809d2148e1a1662e5bb07b1c3
```

I have not included the model because I have not confirmed that it can be redistributed. Obtain it from its original source and place it in this folder as `cmos130.lib`. The schematics look for it at `../models/cmos130.lib`, relative to the schematics folder.

LTspice 26.0.2 reported a BSIM3 version warning: the model specifies 3.200, while the simulator reports support for 3.3.0. It also reported PD and PS warnings. I left the model unchanged.
