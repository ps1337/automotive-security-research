#!/usr/bin/python3

"""
Simple test for received packets
"""

from pyvit.hw import socketcan

dev = socketcan.SocketCanDev("vcan0")
dev.start()

packets = []
a = dev.recv()

print(a)
