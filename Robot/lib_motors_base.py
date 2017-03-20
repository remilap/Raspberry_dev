#!/usr/bin/python

# Library: Basic Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_util


# Set variables for the GPIO motor pins
pinMotorRightForwards = 10
pinMotorRightBackwards = 9
pinMotorLeftForwards = 8
pinMotorLeftBackwards = 7

# Init this library
def Init():
	Trace("lib_motors_base.Init")
	# Set the GPIO modes
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	# Set the GPIO Pin mode
	for x in range(pinMotorLeftBackwards, pinMotorRightForwards+1):
		Trace("set pin " + str(x))
		GPIO.setup(x, GPIO.OUT)

		
# Turn Right motor off
def StopRightMotor():
	Trace("lib_motors_base.StopRightMotor")
	GPIO.output(pinMotorRightForwards, 0)
	GPIO.output(pinMotorRightBackwards, 0)

# Turn Left motor off
def StopLeftMotor():
	Trace("lib_motors_base.StopLeftMotor")
	GPIO.output(pinMotorLeftForwards, 0)
	GPIO.output(pinMotorLeftBackwards, 0)

# Turn all motors off
def StopMotors():
	Trace("lib_motors_base.StopMotors")
	StopRightMotor()
	StopLeftMotor()

# Turn the right motor forwards
def ForwardsRightMotor():
	Trace("lib_motors_base.ForwardsRightMotor")
	if debug == 0:
		GPIO.output(pinMotorRightForwards, 1)
	GPIO.output(pinMotorRightBackwards, 0)

# Turn the right motor backwards
def BackwardsRightMotor():
	Trace("lib_motors_base.BackwardsRightMotor")
	GPIO.output(pinMotorRightForwards, 0)
	if debug == 0:
		GPIO.output(pinMotorRightBackwards, 1)

# Turn the left motor forwards
def ForwardsLeftMotor():
	Trace("lib_motors_base.ForwardsLeftMotor")
	if debug == 0:
		GPIO.output(pinMotorLeftForwards, 1)
	GPIO.output(pinMotorLeftBackwards, 0)

# Turn the left motor backwards
def BackwardsLeftMotor():
	Trace("lib_motors_base.BackwardsLeftMotor")
	GPIO.output(pinMotorLeftForwards, 0)
	if debug == 0:
		GPIO.output(pinMotorLeftBackwards, 1)

# Turn both motors forwards
def Forwards():
	Trace("lib_motors_base.Forwards")
	ForwardsRightMotor()
	ForwardsLeftMotor()

# Turn both motors backwards
def Backwards():
	Trace("lib_motors_base.Backwards")
	BackwardsRightMotor()
	BackwardsLeftMotor()

# Turn left
def Left():
	Trace("lib_motors_base.Left")
	StopLeftMotor()
	ForwardsRightMotor()

# Turn left without moving forward
def LeftStay():
	Trace("lib_motors_base.LeftStay")
	BackwardsLeftMotor()
	ForwardsRightMotor()

# Turn right
def Right():
	Trace("lib_motors_base.Right")
	ForwardsLeftMotor()
	StopRightMotor()

# Turn right without moving forward
def RightStay():
	Trace("lib_motors_base.RightStay")
	ForwardsLeftMotor()
	BackwardsRightMotor()

# Ending the use of the library
def End():
	Trace("lib_motors_base.End")
	StopMotors()
	# Reset the GPIO pins (turn off motors too)
	GPIO.cleanup()

