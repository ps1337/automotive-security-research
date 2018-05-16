#! /usr/bin/python3

from time import sleep
from math import ceil
from random import shuffle
import codecs
import sys

# This script converts the desired displayed speed for a
# Model 8 (2010) speedometer to a CAN payload

# @author pschmied

###############
#   SETTINGS  #
# calculation value and index in packet
firstFineTuningCalc = (0.5, 4)
secondFineTuningCalc = (0.01, 5)
firstByteCalc = (67, 6)
secondByteCalc = (4.1, 7)
calcVals = [
    firstByteCalc, secondByteCalc, firstFineTuningCalc, secondFineTuningCalc
]

###############


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
