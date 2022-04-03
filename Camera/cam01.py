#!/usr/local/bin/python
#
# See https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
#

import sys
sys.path.insert(0, "/home/pi/Raspberry_dev/Camera")

from picamera import PiCamera, Color
from time import sleep, localtime, strftime
##import RPi.GPIO as GPIO


###Configure flash pin
##GPIO.setmode(GPIO.BCM)
##flash = GPIO.PWM(17,120)

camera = PiCamera()

camera.hflip = False
camera.vflip = False

name = 'image' + strftime("%Y_%m_%d_%H_%M_%S", localtime())

#print camera.resolution
#camera.resolution = (2592, 1944) # 720x480
#camera.resolution = (1296, 972)
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = strftime("%A %d %B %Y %H:%M:%S", localtime())
##flash.start(50)
sleep(2)
camera.capture(name + '_1.jpg')
camera.stop_preview()
camera.close()
##flash.stop()

