#!/usr/bin/python

import picamera
from time import sleep, localtime, strftime
#import cd

#from contextlib import contextmanager
#import os
#
#@contextmanager
#def cd(newdir):
#    prevdir = os.getcwd()
#    os.chdir(os.path.expanduser(newdir))
#    try:
#        yield
#    finally:
#        os.chdir(prevdir)



camera = picamera.PiCamera()

#camera.hflip = True
#camera.vflip = True

name = 'image' + strftime("%Y_%m_%d_%H_%M_%S", localtime())

#with cd('/var/www/html/motion'):

camera.capture(name + '_1.jpg')
sleep(2)
camera.capture(name + '_1.jpg')

#raise Exception("Directory not found")


