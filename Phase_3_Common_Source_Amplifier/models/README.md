# Device model

The schematics include `../models/cmos130.lib` and use the model names `nMOSFET` and `pMOSFET`.

The model used for the recorded runs is a generic 130-nm BSIM3 model. It is not a foundry-qualified PDK. The SHA-256 hash of the supplied model file was:

`ac9aa8376dd3fb9cf7033e8791b9f76ae07bf2c809d2148e1a1662e5bb07b1c3`

The model is not included because its redistribution terms have not been confirmed. Obtain it from its original source and place it in this folder as `cmos130.lib`.

LTspice 26.0.2 reported a BSIM3 version warning (model specifies 3.200) and warnings that PD and PS are zero. The model was not edited to hide these warnings.
