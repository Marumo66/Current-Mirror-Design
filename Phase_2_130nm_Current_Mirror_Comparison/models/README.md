# Device model

The schematics refer to an external file named cmos130.lib and use the model name nMOSFET.

The model used for the recorded runs is a generic 130-nm BSIM3 model. It is not a foundry-qualified PDK. Its SHA-256 hash in the supplied working copy was:

ac9aa8376dd3fb9cf7033e8791b9f76ae07bf2c809d2148e1a1662e5bb07b1c3

The model file is not redistributed in this repository because its redistribution terms have not been confirmed. Obtain the same model from its original source and place cmos130.lib in this models folder. The .asc files already refer to it as ../models/cmos130.lib relative to the schematics folder.

LTspice 26.0.2 reported that it supports BSIM3 version 3.3.0 while the model specifies 3.200. It also reported PD and PS warnings. The model was left unchanged; the version field was not edited to suppress the warning.
