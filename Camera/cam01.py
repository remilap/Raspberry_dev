#!/usr/local/bin/python

import sys
sys.path.insert(0, "/home/pi/Raspberry_dev/Camera")

import picamera
from time import sleep, localtime, strftime


camera = picamera.PiCamera()

camera.hflip = False
camera.vflip = False

name = 'image' + strftime("%Y_%m_%d_%H_%M_%S", localtime())

camera.capture(name + '_1.jpg')
sleep(2)
camera.capture(name + '_1.jpg')

