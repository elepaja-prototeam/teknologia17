#!/usr/bin/python3


import serial
import sys


QUERY = bytes('A', '̈́utf-8')


def serial_init():
    port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
    return port


def serial_query(port):
    port.write(QUERY)
    #print("Sent query.")# Actually exists to give slave some time to respond
    ret = port.readline()
    return ret


def main():
    try:
        port = serial_init()
        while True:
            pdata = serial_query(port)
            print(pdata)
    except KeyboardInterrupt:
        sys.exit(0)
    sys.exit(-1)


if __name__ == '__main__':
    main()
