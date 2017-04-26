#!/usr/bin/python

# CamJam EduKit 3 - Robotics
# Worksheet 4 - Evolve Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_motors_evol as evol


evol.Init()

evol.StopMotors()
evol.Forwards()
time.sleep(5.2)
evol.StopMotors()
if False:
	time.sleep(1.5)
	evol.Left()
	time.sleep(1.2)
	evol.StopMotors()
	time.sleep(1.5)
	evol.Right()
	time.sleep(1.2)
	evol.StopMotors()
	time.sleep(1.5)
	evol.LeftStay()
	time.sleep(1.2)
	evol.StopMotors()
	time.sleep(1.5)
	evol.RightStay()
	time.sleep(1.2)
	evol.StopMotors()
	time.sleep(1.5)
	evol.Backwards()
	time.sleep(1.2)
	evol.StopMotors()


evol.End()

