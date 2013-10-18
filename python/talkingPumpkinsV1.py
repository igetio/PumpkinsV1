#!/usr/bin/env python

from time import sleep
import os
import serial 

# delay after each chain
rstDelay = 20 
#set up serial with arduino
ser = serial.Serial('/dev/ttyACM0', 9600) 
# the loop for new input
while 1 : 
 print "Listening"
 input = ser.readline()
 print input
 # if else statements to deal with which dialogue chain to play
 if input == '0\r\n':
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/0-d1-p3.mp3')
  ser.write('10000')
  os.system('mpg321 -g 100 ../audio/0-d2-p1.mp3')
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/0-d3-p3.mp3')
  ser.write('00001')
  os.system('mpg321 -g 100 ../audio/0-d4-p5.mp3')
  ser.write('10000')
  os.system('mpg321 -g 100 ../audio/0-d5-p1.mp3')
  ser.write('00001')
  os.system('mpg321 -g 100 ../audio/0-d6-p5.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 elif input == '1\r\n':
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/1-d1-p3.mp3')
  ser.write('01000')
  os.system('mpg321 -g 100 ../audio/1-d2-p2.mp3')
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/1-d3-p3.mp3')
  ser.write('01000')
  os.system('mpg321 -g 100 ../audio/1-d4-p2.mp3')
  ser.write('10000')
  os.system('mpg321 -g 100 ../audio/1-d5-p1.mp3')
  ser.write('01100')
  os.system('mpg321 -g 100 ../audio/1-d6-p23.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 elif input == '2\r\n':
  ser.write('11111')
  os.system('mpg321 -g 100 ../audio/2-d1-pA.mp3')
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/2-d2-p3.mp3')
  ser.write('00010')
  os.system('mpg321 -g 100 ../audio/2-d3-p4.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 elif input == '3\r\n':
  ser.write('00001')
  os.system('mpg321 -g 100 ../audio/3-d1-p5.mp3')
  ser.write('01000')
  os.system('mpg321 -g 100 ../audio/3-d2-p2.mp3')
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/3-d3-p3.mp3')
  ser.write('01000')
  os.system('mpg321 -g 100 ../audio/3-d4-p2.mp3')
  ser.write('00001')
  os.system('mpg321 -g 100 ../audio/3-d5-p5.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 elif input == '4\r\n':
  ser.write('00010')
  os.system('mpg321 -g 100 ../audio/4-d1-p4.mp3')
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/4-d2-p3.mp3')
  ser.write('00010')
  os.system('mpg321 -g 100 ../audio/4-d3-p4.mp3')
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/4-d4-p3.mp3')
  ser.write('00010')
  os.system('mpg321 -g 100 ../audio/4-d5-p4.mp3')
  ser.write('00100')
  os.system('mpg321 -g 100 ../audio/4-d6-p3.mp3')
  ser.write('00000')
  sleep(rstDelay)
  ser.write('99999')

 print "Done with Playback"
