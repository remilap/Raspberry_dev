#!/usr/bin/python

# Library: Line Detection

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_util


# Init this library
def Init():
	# Set the GPIO modes
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	# Set variables for the GPIO motor pins
	pinLineFollower = 25

	# Set pin 25 as an input so its value can be read
	GPIO.setup(pinLineFollower, GPIO.IN)


# Get detector status
def IsOverBlack():
	# If the sensor is Low (=0), it's above the black line
	if GPIO.input(pinLineFollower) == 0:
		Trace("The sensor is seeing a black surface")
		return True
	# If not (else), print the following
	else:
		Trace("The sensor is seeing a white surface")
		return False



