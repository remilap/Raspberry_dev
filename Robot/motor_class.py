#!/usr/bin/python

import RPi.GPIO as GPIO # Import the GPIO Library
from datetime import datetime, timedelta
import lib_util as util

class Motor(object):
    "How to make a motor running"

    # instances number
    _nb_instances = 0
    # Forward/Backward
    _way = ['Forward', 'Backward']
    # pins number for the motor
    _pinForward = 10
    _pinBackward = 9
    # How many times to turn the pin on and off each second
    _frequency = 20
    # How long the pin stays on each cycle, as a percent (here, it's 30%)
    _dutyCycle = 3.0
    # Setting the duty cycle to 0 means the motors will not turn
    _stopCycle = 0
    # Maximum speed
    _maxSpeed = [30, 20]
    # Current speed
    _curSpeed = 0
    _curWay = 0
    # Current position
    _x = 0
    # Declare the PWM variables
    _pwmMotorForward = 0
    _pwmMotorBackward = 0

    #---
    # initialization of the class
    #---
    def __init__(self, *args):
        util.traceCall()
        if len(args) == 1 and isinstance(args[0], dict):
            self.__dict__ = args[0]
        elif len(args) == 3:
            name, pinF, pinB = args
            self.name = name
            self._pinForward = pinF
            self._pinBackward = pinB

        # Set the GPIO modes
        util.trace("set the GPIO mode and the pins " + str(self._pinForward) + " and " + str(self._pinBackward))
        if self._nb_instances == 0:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
        GPIO.setup(self._pinForward, GPIO.OUT)
        GPIO.setup(self._pinBackward, GPIO.OUT)

        # Set the GPIO to software PWM at 'Frequency' Hertz
        self._pwmMotorForward = GPIO.PWM(self._pinForward, self._frequency)
        self._pwmMotorBackward = GPIO.PWM(self._pinBackward, self._frequency)

        # Start the software PWM with a duty cycle of 0 (i.e. not moving)
        self._pwmMotorForward.start(self._stopCycle)
        self._pwmMotorBackward.start(self._stopCycle)

        # end of instance initialization
        self._nb_instances += 1


    #---
    # Retrieve the max speed
    #---
    def getMaxSpeed(self):
        util.traceCall()
        return self._maxSpeed[self._curWay]

    #---
    # Set the speed
    #---
    def setSpeed(self, v):
        util.traceCall()
        if v <= self.getMaxSpeed():
            if self._curSpeed != v:
                # apply the new speed
                self._curSpeed = v
                self.motorUpdate()
            else:
                util.trace("The speed was already " + v)
        else:
            util.trace("The speed must be lower than " + self.getMaxSpeed())

    #---
    # Retrieve the current speed
    #---
    def getSpeed(self):
        util.traceCall()
        return self._curSpeed

    #---
    # Set the way to go
    #---
    def setWay(self, way):
        util.traceCall()
        if way in self._way:
            if self._curWay != way:
                # apply the new way
                self._curWay = way
                self.motorStop()
                self.motorUpdate()
            else:
                util.trace("The way was already " + way)
        else:
            util.trace("The way must be in " + str(self._way))


    #---
    # Stop the Motor
    #---
    def motorStop(self):
        util.traceCall()
        if util.getDebug() > 0:
            return
        util.trace("_pwmMotorForward.ChangeDutyCycle to stop")
        util.trace("_pwmMotorBackward.ChangeDutyCycle to stop")
        self._pwmMotorForward.ChangeDutyCycle(self._stopCycle)
        self._pwmMotorBackward.ChangeDutyCycle(self._stopCycle)

    #---
    # Make the motor running with cycle
    #---
    def motorUpdate(self):
        util.traceCall()
        if util.getDebug() > 0:
            return
        if self._curWay == 0:
            # forward
            util.trace("_pwmMotorForward.ChangeDutyCycle to " + str(self._dutyCycle * self._curSpeed))
            util.trace("_pwmMotorBackward.ChangeDutyCycle to stop")
            self._pwmMotorForward.ChangeDutyCycle(self._dutyCycle * self._curSpeed)
            self._pwmMotorBackward.ChangeDutyCycle(self._stopCycle)
        else:
            # backward
            util.trace("_pwmMotorForward.ChangeDutyCycle to stop")
            util.trace("_pwmMotorBackward.ChangeDutyCycle to " + str(self._dutyCycle * self._curSpeed))
            self._pwmMotorForward.ChangeDutyCycle(self._stopCycle)
            self._pwmMotorBackward.ChangeDutyCycle(self._dutyCycle * self._curSpeed)

    #---
    # Stop the Motor (with basic method)
    #---
    def basicMotorStop(self):
        util.traceCall()
        if util.getDebug() > 0:
            return
        GPIO.output(self._pinForward, 0)
        GPIO.output(self._pinBackward, 0)

    #---
    # Start the motor in forward way (with basic method)
    #---
    def basicMotorForward(self):
        util.traceCall()
        if util.getDebug() > 0:
            return
        GPIO.output(self._pinForward, 1)
        GPIO.output(self._pinBackward, 0)

    #---
    # Start the motor in backward way (with basic method)
    #---
    def basicMotorBackward(self):
        util.traceCall()
        if util.getDebug() > 0:
            return
        GPIO.output(self._pinForward, 0)
        GPIO.output(self._pinBackward, 1)

    #---
    # Start the motor in one way (with basic method)
    #---
    def basicMotorStart(self, way):
        util.traceCall()
        if util.getDebug() > 0:
            return
        if way == self._way[1] or way == 1:
            self.basicMotorBackward()
        else:
            self.basicMotorForward()

    #---
    # End the class instance and cleanup the GPIO in case of latest instance
    #---
    def motorEnd(self):
        util.traceCall()
        self.motorStop()
        self._nb_instances -= 1
        if self._nb_instances == 0:
            # Reset the GPIO pins (turn off motors too)
            GPIO.cleanup()

