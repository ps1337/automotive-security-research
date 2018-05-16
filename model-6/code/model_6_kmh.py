#! /usr/bin/python3

from math import ceil
import sys

# This script converts the desired displayed speed for a
# Model 6 (2007) speedometer to a CAN payload

# @author pschmied

########################################
############## SETTINGS ################
# calculation value and index in payload
fineTuningCalc = (0.25, 2)
firstByteCalc = (31.5, 4)
secondByteCalc = (1.83, 5)

calcVals = [firstByteCalc,
            secondByteCalc,
            fineTuningCalc]
########################################


def setChar(string, char, idx):
    """
    Set the character at index ``idx`` of the string ``string``
    to the character ``char``.
    """
    stringList = list(string)
    stringList[idx] = char.upper()
    return "".join(stringList)


def kmhToData(kmh):
    """
    This converts the desired displayed speed, which is stored in
    ``kmh`` as integer, to a CAN payload.
    """

    data = "0" * 16

    for calcVal in calcVals:
        while kmh >= calcVal[0]:
            currentVal = int(data[calcVal[1]], 16)
            if currentVal == 15:
                newVal = "F"
                # check if its possible to increment the previous value
                if calcVal == secondByteCalc:
                    # set current value to 0 and increment previous value
                    newVal = "0"
                    currentValPrevious = int(data[firstByteCalc[1]], 16)
                    newValPrevious = hex(currentValPrevious + 1).split("0x")[1]
                    data = setChar(data, newValPrevious, firstByteCalc[1])
            else:
                newVal = hex(currentVal + 1).split("0x")[1]
            data = setChar(data, newVal, calcVal[1])
            kmh -= calcVal[0]

    print(data)


kmh = int(sys.argv[1])
kmhToData(kmh)
