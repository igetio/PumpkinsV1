PumpkinsV1
==========

Talking pumpkin code

Note that the audio playback is based off the adafruit tutorial at the link below:
http://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/overview

The only steps used were the install of the audio which can be done by doing the following:
1. Run these commands
 sudo apt-get install alsa-utils
 sudo apt-get install mpg321

2. Reboot

3. Run these commands
$ sudo modprobe snd_bcm2835
$ sudo amixer cset numid=3 1

Serial communication was based off the following:
http://blog.oscarliang.net/connect-raspberry-pi-and-arduino-usb-cable/

To run the code headless cd to the directory where you put the python script and runn the command below:
sudo nohup python talkingPumpkinsV1.py &