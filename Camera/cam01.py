#!/usr/local/bin/python
#
# See https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
#

import sys
sys.path.insert(0, "/home/pi/Raspberry_dev/Camera")

from picamera import PiCamera, Color
from time import sleep, localtime, strftime


camera = PiCamera()

camera.hflip = False
camera.vflip = False

name = 'image' + strftime("%Y_%m_%d_%H_%M_%S", localtime())

camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = strftime("%A %d %B %Y %H:%M:%S", localtime())
sleep(2)
camera.capture(name + '_1.jpg')
camera.stop_preview()

