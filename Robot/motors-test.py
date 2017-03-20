#!/usr/bin/python

# CamJam EduKit 3 - Robotics
# Worksheet 4 - Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import motors



motors.StopMotors()
motors.Forwards()
time.sleep(0.2)
motors.StopMotors()
time.sleep(0.5)
motors.Left()
time.sleep(0.2)
motors.StopMotors()
time.sleep(0.5)
motors.Right()
time.sleep(0.2)
motors.StopMotors()
time.sleep(0.5)
motors.LeftStay()
time.sleep(0.2)
motors.StopMotors()
time.sleep(0.5)
motors.RightStay()
time.sleep(0.2)
motors.StopMotors()
time.sleep(0.5)
motors.Backwards()
time.sleep(0.2)
motors.StopMotors()


# Reset the GPIO pins (turn off motors too)
GPIO.cleanup()

