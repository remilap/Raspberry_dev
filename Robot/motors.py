#!/usr/bin/python

# CamJam EduKit 3 - Robotics
# Worksheet 4 - Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time

# debug and trace modes
debug = 0
trace = 0

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorRightForwards = 10
pinMotorRightBackwards = 9
pinMotorLeftForwards = 8
pinMotorLeftBackwards = 7

# Set the GPIO Pin mode
for x in range(pinMotorLeftBackwards, pinMotorRightForwards+1):
	if trace == 1:
		print "set pin " + str(x)
	GPIO.setup(x, GPIO.OUT)

# Set debug mode
def SetDebug(m):
	debug = 1
	if m == 0:
		debug = 0

# Set trace mode
def SetTrace(t):
	trace = 1
	if t == 0:
		trace = 0
		
# Turn Right motor off
def StopRightMotor():
	if trace == 1:
		print "StopRightMotor"
	GPIO.output(pinMotorRightForwards, 0)
	GPIO.output(pinMotorRightBackwards, 0)

# Turn Left motor off
def StopLeftMotor():
	if trace == 1:
		print "StopLeftMotor"
	GPIO.output(pinMotorLeftForwards, 0)
	GPIO.output(pinMotorLeftBackwards, 0)

# Turn all motors off
def StopMotors():
	if trace == 1:
		print "StopMotors"
	StopRightMotor()
	StopLeftMotor()

# Turn the right motor forwards
def ForwardsRightMotor():
	if trace == 1:
		print "ForwardsRightMotor"
	if debug == 0:
		GPIO.output(pinMotorRightForwards, 1)
	GPIO.output(pinMotorRightBackwards, 0)

# Turn the right motor backwards
def BackwardsRightMotor():
	if trace == 1:
		print "BackwardsRightMotor"
	GPIO.output(pinMotorRightForwards, 0)
	if debug == 0:
		GPIO.output(pinMotorRightBackwards, 1)

# Turn the left motor forwards
def ForwardsLeftMotor():
	if trace == 1:
		print "ForwardsLeftMotor"
	if debug == 0:
		GPIO.output(pinMotorLeftForwards, 1)
	GPIO.output(pinMotorLeftBackwards, 0)

# Turn the left motor backwards
def BackwardsLeftMotor():
	if trace == 1:
		print "BackwardsLeftMotor"
	GPIO.output(pinMotorLeftForwards, 0)
	if debug == 0:
		GPIO.output(pinMotorLeftBackwards, 1)

# Turn both motors forwards
def Forwards():
	if trace == 1:
		print "Forwards"
	ForwardsRightMotor()
	ForwardsLeftMotor()

# Turn both motors backwards
def Backwards():
	if trace == 1:
		print "Backwards"
	BackwardsRightMotor()
	BackwardsLeftMotor()

# Turn left
def Left():
	if trace == 1:
		print "Left"
	StopLeftMotor()
	ForwardsRightMotor()

# Turn left without moving
def LeftStay():
	if trace == 1:
		print "LeftStay"
	BackwardsLeftMotor()
	ForwardsRightMotor()

# Turn right
def Right():
	if trace == 1:
		print "Right"
	ForwardsLeftMotor()
	StopRightMotor()

# Turn right without moving
def RightStay():
	if trace == 1:
		print "RightStay"
	ForwardsLeftMotor()
	BackwardsRightMotor()


