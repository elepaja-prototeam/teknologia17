#!/usr/bin/python3


# imports, as in what libraries to use
import serial
import sys
import os
import time
import logging


# Constants
QUERY = bytes('A', 'utf-8')
OUTPATH = '/var/www/html/'
FILENAME = "dataplot.csv"
SERIALPATH = "/dev/serial0"
LOGNAME = "demoserial.log"
LOGLVL = logging.DEBUG
WILL_PLOT = True





def main():
    try:
        logging.basicConfig(filename=LOGNAME,level=LOGLVL)
        logging.info('Logging library succesfully set up')
    except OSError:
        print('The program has no rights to open a logging file!')
        sys.exit(-1)
