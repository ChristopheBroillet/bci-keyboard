# Brain Computer Interface Keyboard
This repository contains a project made at the University of Fribourg in the Spring Semester 2023, in the class **Multimodal User Interface**. It consists of using a brain computer interface (BCI) to write with a virtual keyboard displayed on the screen. This uses the technique of event related potential (ERP) emitted by the brain that is synchronized with a given pattern when the user looks at the flickering letter on the screen.

To try the framework, the user first needs to install the *PyMindAffect* library by following the official [tutorial](https://github.com/mindaffect/pymindaffectBCI), but using the source code provided in the *pymindaffectBCI* folder.

The hardware can be connected then with the getting started of the provider, for example [OpenBCI](https://docs.openbci.com/).
Different parameters for the acquisition, decoder, presentation and hub modules can be modified directly inside the *bci_experiment.py* file.
Finally the framework can be launched using the command `python3 bci_experiment.py`.
