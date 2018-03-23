#!/usr/bin/python

# CamJam EduKit 3 - Robotics
# Worksheet 4 - Driving and Turning

#import RPi.GPIO as GPIO # Import the GPIO Library
import time
#import lib_motors_base as base
import motor_class as motor
import lib_util as util


#base.init()
util.setDebug(0)
util.setTrace(1)
util.traceCall()

wheel = motor.Motor("wheel", 8, 7)
wheel.basicMotorStop()
wheel.basicMotorForward()
time.sleep(0.2)
wheel.basicMotorStop()
time.sleep(0.5)
wheel.basicMotorBackward()
time.sleep(0.2)
wheel.basicMotorStop()
time.sleep(0.5)


wheel.motorEnd()

