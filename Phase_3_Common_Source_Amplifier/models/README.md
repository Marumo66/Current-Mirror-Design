# Model file

The schematics in this folder use the model names `nMOSFET` and `pMOSFET` from an external file named `cmos130.lib`.

The model used for the recorded runs is a generic 130-nm BSIM3 model. It is not a foundry-qualified PDK. The copy used for those runs had this SHA-256 hash:

```text
ac9aa8376dd3fb9cf7033e8791b9f76ae07bf2c809d2148e1a1662e5bb07b1c3
```

I have not included the model because I have not confirmed its redistribution terms. Obtain it from its original source and place it in this folder as `cmos130.lib`.

LTspice 26.0.2 reported a BSIM3 version warning (the model specifies 3.200) and PD / PS warnings. I left the model unchanged.
