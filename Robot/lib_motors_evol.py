#!/usr/bin/python

# Library: Evolve Driving and Turning, using Motor Frequency

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_util
import lib_motors_base


# How many times to turn the pin on and off each second
Frequency = 20

# How long the pin stays on each cycle, as a percent (here, it's 30%)
DutyCycleLeft = 10
DutyCycleRight = 10

# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Maximum speed
speed_max = 10

# Current speed
my_speed = 0


# Init this library
def Init():
	global pwmMotorLeftForwards, pwmMotorLeftBackwards, pwmMotorRightForwards, pwmMotorRightBackwards

        lib_util.Trace("lib_motors_evol.Init")
	if lib_util.GetDebug() > 0:
		return
	lib_motors_base.Init()

	# Set the GPIO to software PWM at 'Frequency' Hertz
	pwmMotorLeftForwards = GPIO.PWM(lib_motors_base.pinMotorLeftForwards, Frequency)
	pwmMotorLeftBackwards = GPIO.PWM(lib_motors_base.pinMotorLeftBackwards, Frequency)
	pwmMotorRightForwards = GPIO.PWM(lib_motors_base.pinMotorRightForwards, Frequency)
	pwmMotorRightBackwards = GPIO.PWM(lib_motors_base.pinMotorRightBackwards, Frequency)

	# Start the software PWM with a duty cycle of 0 (i.e. not moving)
	pwmMotorLeftForwards.start(Stop)
	pwmMotorLeftBackwards.start(Stop)
	pwmMotorRightForwards.start(Stop)
	pwmMotorRightBackwards.start(Stop)

# Define the speed
def setSpeed(v):
	if v < -speed_max or v > speed_max:
		lib_util.Trace("The speed must be in range " + str(-speed_max) + ".." + str(speed_max))
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
def StopLeftMotor():
        lib_util.Trace("lib_motors_evol.StopLeftMotor")
	if lib_util.GetDebug() > 0:
		return
	pwmMotorLeftForwards.ChangeDutyCycle(Stop)
	pwmMotorLeftBackwards.ChangeDutyCycle(Stop)

# Turn right motor off
def StopRightMotor():
        lib_util.Trace("lib_motors_evol.StopRightMotor")
	if lib_util.GetDebug() > 0:
		return
	pwmMotorRightForwards.ChangeDutyCycle(Stop)
	pwmMotorRightBackwards.ChangeDutyCycle(Stop)

# Set left motor speed
def LeftMotorSpeed(speed_f, speed_b):
        lib_util.Trace("lib_motors_evol.LeftMotorSpeed with speed_f=" + str(speed_f) + " and speed_b=" + str(speed_b))
	if lib_util.GetDebug() > 0:
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
def StartLeftMotor(speed):
        lib_util.Trace("lib_motors_evol.StartLeftMotor with speed=" + str(speed))
	s = speed
	if speed == 0:
		LeftMotorSpeed(0, 0)
	elif speed > 0:
		if speed > speed_max:
			s = speed_max
		LeftMotorSpeed(s, 0)
	else:
		if speed < -speed_max:
			s = -speed_max
		LeftMotorSpeed(0, s)

# Turn left motor forwards
def LeftMotorForwards():
        lib_util.Trace("lib_motors_evol.LeftMotorForwards")
	StartLeftMotor(getAbsSpeed())

# Turn left motor backwards
def LeftMotorBackwards():
        lib_util.Trace("lib_motors_evol.LeftMotorBackwards")
	StartLeftMotor(-getAbsSpeed())

# Set right motor speed
def RightMotorSpeed(speed_f, speed_b):
        lib_util.Trace("lib_motors_evol.RightMotorSpeed with speed_f=" + str(speed_f) + " and speed_b=" + str(speed_b))
	if lib_util.GetDebug() > 0:
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
def StartRightMotor(speed):
	lib_util.Trace("lib_motors_evol.StartRightMotor with speed=" + str(speed))
	s = speed
	if speed == 0:
		RightMotorSpeed(0, 0)
	elif speed > 0:
		if speed > speed_max:
			s = speed_max
		RightMotorSpeed(s, 0)
	else:
		if speed < -speed_max:
			s = -speed_max
		RightMotorSpeed(0, s)

# Turn right motor forwards
def RightMotorForwards():
        lib_util.Trace("lib_motors_evol.RightMotorForwards")
	StartRightMotor(getAbsSpeed())

# Turn right motor backwards
def RightMotorBackwards():
        lib_util.Trace("lib_motors_evol.RightMotorBackwards")
	StartRightMotor(-getAbsSpeed())

# Turn all motors off
def StopMotors():
        lib_util.Trace("lib_motors_evol.StopMotors")
	StopLeftMotor()
	StopRightMotor()

# Turn both motors forwards
def Forwards():
        lib_util.Trace("lib_motors_evol.Forwards")
	LeftMotorForwards()
	RightMotorForwards()

# Turn both motors backwards
def Backwards():
        lib_util.Trace("lib_motors_evol.Backwards")
	LeftMotorBackwards()
	RightMotorBackwards()

# Move
def Move(speed_l, speed_r):
	lib_util.Trace("lib_motors_evol.Move with speed_l=" + str(speed_l) + " and speed_r=" + str(speed_r))
	StartLeftMotor(speed_l)
	StartRightMotor(speed_r)

# Turn left
def Left():
        lib_util.Trace("lib_motors_evol.Left")
	StopLeftMotor()
	RightMotorForwards()

# Turn left without moving forward
def LeftStay():
        lib_util.Trace("lib_motors_evol.LeftStay")
	LeftMotorBackwards()
	RightMotorForwards()

# Turn Right
def Right():
        lib_util.Trace("lib_motors_evol.Right")
	LeftMotorForwards()
	StopRightMotor()

# Turn Right without moving forward
def RightStay():
        lib_util.Trace("lib_motors_evol.RightStay")
	LeftMotorForwards()
	RightMotorBackwards()

# Ending the use of the library
def End():
        lib_util.Trace("lib_motors_evol.End")
	StopMotors()
	lib_motors_base.End()


