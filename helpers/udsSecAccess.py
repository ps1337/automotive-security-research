#! /usr/bin/python3

from pyvit import can
from pyvit.hw import socketcan
from time import sleep
from math import ceil
from random import shuffle
import codecs

"""
Scans a vehicle for UDS services using Security Access
"""

#################
##  SETTINGS   ##
iface = "can0"
sleep_time = 0.01

#################


def init():
    global dev
    dev = socketcan.SocketCanDev(iface)
    dev.start()
    return dev


def tryBuildPacket(dataTuple):
    packet = None
    try:
        # convert id to hexvalue
        # convert data to list of bytes
        packet = can.Frame(
            arb_id=int(dataTuple[0], 16),
            data=list(bytearray.fromhex(dataTuple[1])))
    except ValueError as e:
        if "Arbitration ID out of range" in str(e):
            return False, None
        else:
            raise
    return True, packet


dev = init()

for x in range(255):
    for i in range(255):
        hexData = "0327" + hex(i).replace("0x", "") + "0" + hex(x).replace(
            "0x", "")
        while len(hexData) < 16:
            hexData += "0"

        retVal = tryBuildPacket(("714", hexData))
        packet_ok = retVal[0]
        packet = retVal[1]

        if packet_ok:
            print(packet)
            dev.send(packet)
            sleep(sleep_time)
        else:
            print("damaged packet")
