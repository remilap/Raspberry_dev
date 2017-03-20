#!/usr/bin/python

# CamJam EduKit 3 - Robotics
# Worksheet 4 - Evolve Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_motors_evol


lib_motors_evol.Init()

lib_motors_evol.StopMotors()
lib_motors_evol.Forwards()
time.sleep(0.2)
lib_motors_evol.StopMotors()
time.sleep(0.5)
lib_motors_evol.Left()
time.sleep(0.2)
lib_motors_evol.StopMotors()
time.sleep(0.5)
lib_motors_evol.Right()
time.sleep(0.2)
lib_motors_evol.StopMotors()
time.sleep(0.5)
lib_motors_evol.LeftStay()
time.sleep(0.2)
lib_motors_evol.StopMotors()
time.sleep(0.5)
lib_motors_evol.RightStay()
time.sleep(0.2)
lib_motors_evol.StopMotors()
time.sleep(0.5)
lib_motors_evol.Backwards()
time.sleep(0.2)
lib_motors_evol.StopMotors()


lib_motors_evol.End()

