#!/usr/bin/python

# Library: Basic Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_util as util


# Set variables for the GPIO motor pins
pinMotorRightForwards = 10
pinMotorRightBackwards = 9
pinMotorLeftForwards = 8
pinMotorLeftBackwards = 7

# Init this library
def init():
	util.trace("lib_motors_base.Init")
	# Set the GPIO modes
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	# Set the GPIO Pin mode
	for x in range(pinMotorLeftBackwards, pinMotorRightForwards+1):
		util.trace("set pin " + str(x))
		GPIO.setup(x, GPIO.OUT)

		
# Turn Right motor off
def stopRightMotor():
	util.trace("lib_motors_base.stopRightMotor")
	GPIO.output(pinMotorRightForwards, 0)
	GPIO.output(pinMotorRightBackwards, 0)

# Turn Left motor off
def stopLeftMotor():
	util.trace("lib_motors_base.stopLeftMotor")
	GPIO.output(pinMotorLeftForwards, 0)
	GPIO.output(pinMotorLeftBackwards, 0)

# Turn all motors off
def stopMotors():
	util.trace("lib_motors_base.stopMotors")
	stopRightMotor()
	stopLeftMotor()

# Turn the right motor forwards
def forwardsRightMotor():
	util.trace("lib_motors_base.forwardsRightMotor")
	if util.getDebug == 0:
		GPIO.output(pinMotorRightForwards, 1)
	GPIO.output(pinMotorRightBackwards, 0)

# Turn the right motor backwards
def backwardsRightMotor():
	util.trace("lib_motors_base.backwardsRightMotor")
	GPIO.output(pinMotorRightForwards, 0)
	if util.getDebug == 0:
		GPIO.output(pinMotorRightBackwards, 1)

# Turn the left motor forwards
def forwardsLeftMotor():
	util.trace("lib_motors_base.forwardsLeftMotor")
	if util.getDebug == 0:
		GPIO.output(pinMotorLeftForwards, 1)
	GPIO.output(pinMotorLeftBackwards, 0)

# Turn the left motor backwards
def backwardsLeftMotor():
	util.trace("lib_motors_base.backwardsLeftMotor")
	GPIO.output(pinMotorLeftForwards, 0)
	if util.getDebug == 0:
		GPIO.output(pinMotorLeftBackwards, 1)

# Turn both motors forwards
def forwards():
	util.trace("lib_motors_base.forwards")
	forwardsRightMotor()
	forwardsLeftMotor()

# Turn both motors backwards
def backwards():
	util.trace("lib_motors_base.backwards")
	backwardsRightMotor()
	backwardsLeftMotor()

# Turn left
def left():
	util.trace("lib_motors_base.left")
	stopLeftMotor()
	forwardsRightMotor()

# Turn left without moving forward
def leftStay():
	util.trace("lib_motors_base.leftStay")
	backwardsLeftMotor()
	forwardsRightMotor()

# Turn right
def right():
	util.trace("lib_motors_base.right")
	forwardsLeftMotor()
	stopRightMotor()

# Turn right without moving forward
def rightStay():
	util.trace("lib_motors_base.rightStay")
	forwardsLeftMotor()
	backwardsRightMotor()

# Ending the use of the library
def end():
	util.trace("lib_motors_base.end")
	stopMotors()
	# Reset the GPIO pins (turn off motors too)
	GPIO.cleanup()

