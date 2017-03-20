#!/usr/bin/python

# CamJam EduKit 3 - Robotics
# Worksheet 4 - Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_motors_base


lib_motors_base.Init()

lib_motors_base.StopMotors()
lib_motors_base.Forwards()
time.sleep(0.2)
lib_motors_base.StopMotors()
time.sleep(0.5)
lib_motors_base.Left()
time.sleep(0.2)
lib_motors_base.StopMotors()
time.sleep(0.5)
lib_motors_base.Right()
time.sleep(0.2)
lib_motors_base.StopMotors()
time.sleep(0.5)
lib_motors_base.LeftStay()
time.sleep(0.2)
lib_motors_base.StopMotors()
time.sleep(0.5)
lib_motors_base.RightStay()
time.sleep(0.2)
lib_motors_base.StopMotors()
time.sleep(0.5)
lib_motors_base.Backwards()
time.sleep(0.2)
lib_motors_base.StopMotors()


lib_motors_base.End()

