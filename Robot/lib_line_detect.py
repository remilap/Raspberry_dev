#!/usr/bin/python

# Library: Line Detection

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_util as util


# Set variables for the GPIO motor pins
pinLineFollower = 25


# Init this library
def init():
	# Set the GPIO modes
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	# Set pin 25 as an input so its value can be read
	GPIO.setup(pinLineFollower, GPIO.IN)


# Get detector status
def isOverBlack():
	# If the sensor is Low (=0), it's above the black line
	if GPIO.input(pinLineFollower) == 0:
		util.trace("The sensor is seeing a black surface")
		return True
	# If not (else), print the following
	else:
		util.trace("The sensor is seeing a white surface")
		return False



