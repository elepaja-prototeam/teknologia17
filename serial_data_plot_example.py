#!/usr/bin/python3


import serial
import sys
import os
import time


QUERY = 'A'
FILEPATH = '/var/www/html/'
FILENAME = dataplot.csv
SERIALPATH = "/dev/serial0"


# serial_init initializes serial with the correct device, specified in the constant SERIALPATH
def serial_init():
    port = serial.Serial(SERIALPATH, baudrate=9600, timeout=3.0)
    return port


# serial_query queries the specific port with the query value given in the value query
def serial_query(port, query):
    port.write(query)
    ret = port.readline()
    return ret


def plot_to_csv(datal):
    try:
        filename = os.path.abspath(FILEPATH + FILENAME)
        file = open(filename, 'w')
        file.write("time,value")
        for i in datal:
            row = str(i[0]) + "," + str(i[1]) + "\n"
            file.write(row)
        file.close()
    except OSError:
        print("Error writing to file, check permissions and lsof")


def read_values(port, length):
    begint = time.time()
    datal = []
    while time.time() - begint < length:
        appendl = []
        appendl.append(time.time())
        valread = serial_query(port).rstrip()
        appendl.append(valread)
        datal.append(datal)
    return datal


if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)
