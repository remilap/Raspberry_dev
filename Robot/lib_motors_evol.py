#!/usr/bin/python

# Library: Evolve Driving and Turning, using Motor Frequency

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_util as util
import lib_motors_base as base


# How many times to turn the pin on and off each second
Frequency = 20

# How long the pin stays on each cycle, as a percent (here, it's 30%)
DutyCycleLeft = 3.1
DutyCycleRight = 3.0

# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Maximum speed
speed_max = 30

# Current speed
my_speed = 0


# Init this library
def init():
        util.trace("lib_motors_evol.init")
	base.init()

	# Declare the PWM variables
	global pwmMotorLeftForwards
	global pwmMotorLeftBackwards
	global pwmMotorRightForwards
	global pwmMotorRightBackwards

	# Set the GPIO to software PWM at 'Frequency' Hertz
	pwmMotorLeftForwards = GPIO.PWM(base.pinMotorLeftForwards, Frequency)
	pwmMotorLeftBackwards = GPIO.PWM(base.pinMotorLeftBackwards, Frequency)
	pwmMotorRightForwards = GPIO.PWM(base.pinMotorRightForwards, Frequency)
	pwmMotorRightBackwards = GPIO.PWM(base.pinMotorRightBackwards, Frequency)

	# Start the software PWM with a duty cycle of 0 (i.e. not moving)
	pwmMotorLeftForwards.start(Stop)
	pwmMotorLeftBackwards.start(Stop)
	pwmMotorRightForwards.start(Stop)
	pwmMotorRightBackwards.start(Stop)

# Retrieve the max speed
def getMaxSpeed():
	return speed_max

# Define the speed
def setSpeed(v):
	if v < -speed_max or v > speed_max:
		util.trace("The speed must be in range " + str(-speed_max) + ".." + str(speed_max))
	else:
		my_speed = v

# Retrieve the current speed
def getSpeed():
	return my_speed

# Retrieve the current speed in absolute value
def getAbsSpeed():
	if my_speed >= 0:
		return my_speed
	return -my_speed

# Turn left motor off
def stopLeftMotor():
        util.trace("lib_motors_evol.stopLeftMotor")
	if util.getDebug() > 0:
		return
	pwmMotorLeftForwards.ChangeDutyCycle(Stop)
	pwmMotorLeftBackwards.ChangeDutyCycle(Stop)

# Turn right motor off
def stopRightMotor():
        util.trace("lib_motors_evol.stopRightMotor")
	if util.getDebug() > 0:
		return
	pwmMotorRightForwards.ChangeDutyCycle(Stop)
	pwmMotorRightBackwards.ChangeDutyCycle(Stop)

# Set left motor speed
def leftMotorSpeed(speed_f, speed_b):
        util.trace("lib_motors_evol.leftMotorSpeed with speed_f=" + str(speed_f) + " and speed_b=" + str(speed_b))
	if util.getDebug() > 0:
		return
	if 1 <= speed_f <= speed_max:
		pwmMotorLeftForwards.ChangeDutyCycle(DutyCycleLeft * speed_f)
	else:
		pwmMotorLeftForwards.ChangeDutyCycle(Stop)
	if 1 <= speed_b <= speed_max:
		pwmMotorLeftBackwards.ChangeDutyCycle(DutyCycleLeft * speed_b)
	else:
		pwmMotorLeftBackwards.ChangeDutyCycle(Stop)

# Turn left motor on
def startLeftMotor(speed):
        util.trace("lib_motors_evol.startLeftMotor with speed=" + str(speed))
	s = speed
	if speed == 0:
		leftMotorSpeed(0, 0)
	elif speed > 0:
		if speed > speed_max:
			s = speed_max
		leftMotorSpeed(s, 0)
	else:
		if speed < -speed_max:
			s = -speed_max
		leftMotorSpeed(0, s)

# Turn left motor forwards
def leftMotorForwards():
        util.trace("lib_motors_evol.leftMotorForwards")
	startLeftMotor(getAbsSpeed())

# Turn left motor backwards
def leftMotorBackwards():
        util.trace("lib_motors_evol.leftMotorBackwards")
	startLeftMotor(-getAbsSpeed())

# Set right motor speed
def rightMotorSpeed(speed_f, speed_b):
        util.trace("lib_motors_evol.rightMotorSpeed with speed_f=" + str(speed_f) + " and speed_b=" + str(speed_b))
	if util.getDebug() > 0:
		return
	if 1 <= speed_f <= speed_max:
		pwmMotorRightForwards.ChangeDutyCycle(DutyCycleLeft * speed_f)
	else:
		pwmMotorRightForwards.ChangeDutyCycle(Stop)
	if 1 <= speed_b <= speed_max:
		pwmMotorRightBackwards.ChangeDutyCycle(DutyCycleLeft * speed_b)
	else:
		pwmMotorRightBackwards.ChangeDutyCycle(Stop)

# Turn right motor on
def startRightMotor(speed):
	util.trace("lib_motors_evol.startRightMotor with speed=" + str(speed))
	s = speed
	if speed == 0:
		rightMotorSpeed(0, 0)
	elif speed > 0:
		if speed > speed_max:
			s = speed_max
		rightMotorSpeed(s, 0)
	else:
		if speed < -speed_max:
			s = -speed_max
		rightMotorSpeed(0, s)

# Turn right motor forwards
def rightMotorForwards():
        util.trace("lib_motors_evol.rightMotorForwards")
	startRightMotor(getAbsSpeed())

# Turn right motor backwards
def rightMotorBackwards():
        util.trace("lib_motors_evol.rightMotorBackwards")
	startRightMotor(-getAbsSpeed())

# Turn all motors off
def stopMotors():
        util.trace("lib_motors_evol.stopMotors")
	stopLeftMotor()
	stopRightMotor()

# Turn both motors forwards
def forwards():
        util.trace("lib_motors_evol.forwards")
	leftMotorForwards()
	rightMotorForwards()

# Turn both motors backwards
def backwards():
        util.trace("lib_motors_evol.backwards")
	leftMotorBackwards()
	rightMotorBackwards()

# Move
def move(speed_l, speed_r):
	util.trace("lib_motors_evol.move with speed_l=" + str(speed_l) + " and speed_r=" + str(speed_r))
	startLeftMotor(speed_l)
	startRightMotor(speed_r)

# Turn left
def left():
        util.trace("lib_motors_evol.left")
	stopLeftMotor()
	rightMotorForwards()

# Turn left without moving forward
def leftStay():
        util.trace("lib_motors_evol.leftStay")
	leftMotorBackwards()
	rightMotorForwards()

# Turn Right
def right():
        util.trace("lib_motors_evol.right")
	leftMotorForwards()
	stopRightMotor()

# Turn Right without moving forward
def rightStay():
        util.trace("lib_motors_evol.rightStay")
	leftMotorForwards()
	rightMotorBackwards()

# Ending the use of the library
def end():
        util.trace("lib_motors_evol.end")
	stopMotors()
	base.end()


