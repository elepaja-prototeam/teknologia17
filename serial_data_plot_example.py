#!/usr/bin/python3


# imports, as in what libraries to use
import serial
import sys
import os
import time


# Constants
QUERY = bytes('A', 'utf-8')
FILEPATH = '/var/www/html/'
FILENAME = "dataplot.csv"
SERIALPATH = "/dev/serial0"
LENGTH = 10000
WILL_PLOT = True


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


def write_to_csv(row, file):
    try:
        file.write(row)
        file.flush()
        return 0
    except OSError:
        print("Error writing to file, check permissions and lsof")
        return -1


# function to read values for a specified time, from the serial port.
# Function saves the starting time into a variable, to check how much
# time has passed since last iteration. When the amount specified in
# the variable 'length' if filled, the loop ends and returns all of
# the values that were read while in the loop.
# Format for the values is [[time,value],[time,value]...[time,value]]
def read_values(port, length):
    begint = time.time()
    datal = []
    try:
        file = open(os.path.abspath(FILEPATH + FILENAME), 'w')
        file.write("Time,Temperature\n")
    except OSError:
        print("Writing to file not working, exiting read_values()")
    while time.time() - begint < length:
        appendl = []
        timestr = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        appendl.append(timestr)
        valread = float(serial_query(port, QUERY).rstrip())
        appendl.append(valread)
        row = str(appendl[0]) + "," + str(appendl[1]) + "\n"
        write_to_csv(row, file)
        #time.sleep(1)
        #datal.append(appendl)
    file.close()
    return datal


def main():
    port = serial_init()
    datal = read_values(port, LENGTH)
    #if WILL_PLOT:
    #    plot_to_csv(datal)
    sys.exit(0)


# If the program is run as a __main__ module, run main; otherwise
# complain about not being run as main.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        file.close()
        sys.exit(0)
else:
    print("This program has to be run as main!")
    file.close()
    sys.exit(-1)
