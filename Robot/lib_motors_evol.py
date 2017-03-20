#!/usr/bin/python

# Library: Evolve Driving and Turning, using Motor Frequency

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_util
import lib_motors_base


# How many times to turn the pin on and off each second
Frequency = 20

# How long the pin stays on each cycle, as a percent (here, it's 30%)
DutyCycleLeft = 30
DutyCycleRight = 30

# Setting the duty cycle to 0 means the motors will not turn
Stop = 0


# Init this library
def Init():
        Trace("lib_motors_evol.Init")
	lib_motors_base.Init()

	# Set the GPIO to software PWM at 'Frequency' Hertz
	pwmMotorLeftForwards = GPIO.PWM(pinMotorLeftForwards, Frequency)
	pwmMotorLeftBackwards = GPIO.PWM(pinMotorLeftBackwards, Frequency)
	pwmMotorRightForwards = GPIO.PWM(pinMotorRightForwards, Frequency)
	pwmMotorRightBackwards = GPIO.PWM(pinMotorRightBackwards, Frequency)

	# Start the software PWM with a duty cycle of 0 (i.e. not moving)
	pwmMotorLeftForwards.start(Stop)
	pwmMotorLeftBackwards.start(Stop)
	pwmMotorRightForwards.start(Stop)
	pwmMotorRightBackwards.start(Stop)

# Turn left motor off
def StopLeftMotor():
        Trace("lib_motors_evol.StopLeftMotor")
	pwmMotorLeftForwards.ChangeDutyCycle(Stop)
	pwmMotorLeftBackwards.ChangeDutyCycle(Stop)

# Turn right motor off
def StopRightMotor():
        Trace("lib_motors_evol.StopRightMotor")
	pwmMotorRightForwards.ChangeDutyCycle(Stop)
	pwmMotorRightBackwards.ChangeDutyCycle(Stop)

# Turn left motor forwards
def LeftMotorForwards():
        Trace("lib_motors_evol.LeftMotorForwards")
	pwmMotorLeftForwards.ChangeDutyCycle(DutyCycleLeft)
	pwmMotorLeftBackwards.ChangeDutyCycle(Stop)

# Turn left motor backwards
def LeftMotorBackwards():
        Trace("lib_motors_evol.LeftMotorBackwards")
	pwmMotorLeftForwards.ChangeDutyCycle(Stop)
	pwmMotorLeftBackwards.ChangeDutyCycle(DutyCycleLeft)

# Turn right motor forwards
def RightMotorForwards():
        Trace("lib_motors_evol.RightMotorForwards")
	pwmMotorRightForwards.ChangeDutyCycle(DutyCycleRight)
	pwmMotorRightBackwards.ChangeDutyCycle(Stop)

# Turn right motor backwards
def RightMotorBackwards():
        Trace("lib_motors_evol.RightMotorBackwards")
	pwmMotorRightForwards.ChangeDutyCycle(Stop)
	pwmMotorRightBackwards.ChangeDutyCycle(DutyCycleRight)

# Turn all motors off
def StopMotors():
        Trace("lib_motors_evol.StopMotors")
	StopLeftMotor()
	StopRightMotor()

# Turn both motors forwards
def Forwards():
        Trace("lib_motors_evol.Forwards")
	LeftMotorForwards()
	RightMotorForwards()

# Turn both motors backwards
def Backwards():
        Trace("lib_motors_evol.Backwards")
	LeftMotorBackwards()
	RightMotorBackwards()

# Turn left
def Left():
        Trace("lib_motors_evol.Left")
	StopLeftMotor()
	RightMotorForwards()

# Turn left without moving forward
def LeftStay():
        Trace("lib_motors_evol.LeftStay")
	LeftMotorBackwards()
	RightMotorForwards()

# Turn Right
def Right():
        Trace("lib_motors_evol.Right")
	LeftMotorForwards()
	StopRightMotor()

# Turn Right without moving forward
def RightStay():
        Trace("lib_motors_evol.RightStay")
	LeftMotorForwards()
	RightMotorBackwards()

# Ending the use of the library
def End():
        Trace("lib_motors_evol.End")
	StopMotors()
	lib_motors_base.End()


