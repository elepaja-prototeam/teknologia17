#!/usr/bin/python3


# imports, as in what libraries to use
import serial
import sys
import os
import time


# Constants
QUERY = 'A'
FILEPATH = '/var/www/html/'
FILENAME = dataplot.csv
SERIALPATH = "/dev/serial0"


# serial_init initializes serial with the correct device, specified in the constant SERIALPATH
# baudrate of 9600 is a commonly used speed for the serial connection, and should be safe to
# use, even when the wires connecting the two ports are not of the highest quality.
def serial_init():
    port = serial.Serial(SERIALPATH, baudrate=9600, timeout=3.0)
    return port


# serial_query queries the specific port with the query value given in the value query
def serial_query(port, query):
    port.write(query)
    ret = port.readline()
    return ret


# writes the data collected from serial into a .csv file, to be read into an external
# plotting program, eg. a javascript based interactive website
def plot_to_csv(datal):
    try: # try opening the file and write values into it
        filename = os.path.abspath(FILEPATH + FILENAME)
        file = open(filename, 'w')
        file.write("time,value")
        for i in datal:
            row = str(i[0]) + "," + str(i[1]) + "\n"
            file.write(row)
        file.close()
    except OSError:
        print("Error writing to file, check permissions and lsof")


# function to read values for a specified time, from the serial port.
# Function saves the starting time into a variable, to check how much
# time has passed since last iteration. When the amount specified in
# the variable 'length' if filled, the loop ends and returns all of
# the values that were read while in the loop.
# Format for the values is [[time,value],[time,value]...[time,value]]
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


# If the program is run as a __main__ module, run main; otherwise
# complain about not being run as main.
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)
else:
    print("This program has to be run as main!")
    sys.exit(-1)
