#!/usr/bin/python


import serial


port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
data = raw_input()


port.write(data)
print(port.readline())

