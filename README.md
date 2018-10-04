# Automotive Security Research

![Alt text](/.res/logo.png?raw=true "Hax")

This repository contains reverse engineering results and resources for a few specific car models.

## Index

- [helpers](helpers): Contains two simple Python PoCs that demonstrate how to read CAN data and how to scan a CAN bus for UDS security access.
- [keys](keys): Contains ECU keys extracted from manufacturer software using IDA. You can guess the manufacturers by reading the file names.
- [misc](misc): You can find the partial CAN matrix of various cars and CAN protocol information in there
- [model 6](model-6): Contains all data of a very specific car I gathered by reverse engineering. You can find code to set the displayed speed on the speedometer via the CAN bus there. Also, there are various CAN dumps and a wiring diagram which are useful for further analysis.
- [model-8](model 8): Same as above but for a different model of the same manufacturer.

