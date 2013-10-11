#!/usr/bin/env python

from time import sleep
import os
import serial 

rstDelay = 20
ser = serial.Serial('/dev/ttyACM0', 9600) 
while 1 :
 print "start loop"
 input = ser.readline()
 print input
 if input == '0\r\n':
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/0-d1-p3.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 elif input == '1\r\n':
  ser.write('01000')
  os.system('mpg321 ../audio/1-d1-p2.mp3')
  ser.write('00000')
  ser.write('00001')
  os.system('mpg321 ../audio/1-d2-p5.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 elif input == '2\r\n':
  ser.write('10000')
  os.system('mpg321 ../audio/0-p1.mp3')
  ser.write('00100')
  os.system('mpg321 ../audio/0-p3.mp3')
  ser.write('01000')
  os.system('mpg321 ../audio/0-p2.mp3')
  ser.write('00001')
  os.system('mpg321 ../audio/0-p5.mp3')
  ser.write('00010')
  os.system('mpg321 ../audio/0-p4.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 elif input == '3\r\n':
  ser.write('00001')
  os.system('mpg321 ../audio/0-p5.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 elif input == '4\r\n':
  ser.write('00010')
  os.system('mpg321 ../audio/4-d1-p4.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 print "Loop"
