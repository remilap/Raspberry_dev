#!/usr/bin/python

# CamJam EduKit 3 - Robotics
# Worksheet 4 - Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_motors_base as base


base.Init()

base.StopMotors()
base.Forwards()
time.sleep(0.2)
base.StopMotors()
time.sleep(0.5)
base.Left()
time.sleep(0.2)
base.StopMotors()
time.sleep(0.5)
base.Right()
time.sleep(0.2)
base.StopMotors()
time.sleep(0.5)
base.LeftStay()
time.sleep(0.2)
base.StopMotors()
time.sleep(0.5)
base.RightStay()
time.sleep(0.2)
base.StopMotors()
time.sleep(0.5)
base.Backwards()
time.sleep(0.2)
base.StopMotors()


base.End()

