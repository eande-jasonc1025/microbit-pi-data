#!/usr/bin/env python
import time
import serial
from datetime import datetime
from csv import writer
import http.server

ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while True:
    x=ser.readline()
    if x:
        dt = datetime.now()
        datestamp = str(dt)[:16]
        ###jwc o temp, light = x.decode().split(':')
        ###jwc 23-0310-1120 y id, te, li, co = x.decode().split(',')
        ###jwc n id, te, li, co, m1, m2, m3, m4 = x.decode().split('|')

        ###jwc o newData = [datestamp,temp,light]
        ###jwc 23-0310-1120 y newData = [datestamp, id, te, li, co]
        ###jwc n newData = [datestamp, id, te, li, co, m1, m2, m3, m4]
        newData = [datestamp, x]

        print(newData)
        with open('test.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(newData)
            f_object.close()