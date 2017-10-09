#!/usr/bin/python3


import serial
import sys


def main():
    port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
    data = bytes(input(), 'utf-8')
    port.write(data)
    print(port.readline())


if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(-1)
    except:
        sys.exit(-100)
