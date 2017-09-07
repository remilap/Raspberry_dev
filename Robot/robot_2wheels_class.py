#!/usr/bin/python

import motor_class as motor
from datetime import datetime, timedelta
import lib_util as util

class Robot_2Wheels(object):
    "How to move a robot with 2 wheels"

    # instances number
    _nb_instances = 0
    # the 2 wheels
    _wheel_left = 0
    _wheel_right = 0

    #---
    # initialization of the class
    #---
    def __init__(self, *args):
        util.traceCall()
        if len(args) == 1 and isinstance(args[0], dict):
            self.__dict__ = args[0]
        elif len(args) == 3:
            name = args
            self.name = name

        # Define the 2 wheels
        util.trace("Define the 2 wheels")
        self._wheel_left = motor.Motor("left_wheel", 8, 7)
        self._wheel_right = motor.Motor("right_wheel", 10, 9)

        # end of instance initialization
        self._nb_instances += 1


    #---
    # Stop the robot
    #---
    def stopRobot(self):
        util.traceCall()
        self._wheel_left.motorStop()
        self._wheel_right.motorStop()

    #---
    # Move straight
    #---
    def moveStraight(self, way, speed):
        util.traceCall()
        self._wheel_left.setWay(way)
        self._wheel_right.setWay(way)
        self._wheel_left.setSpeed(speed)
        self._wheel_right.setSpeed(speed)

    #---
    # Turn right forward
    #---
    def turnRightForward(self):
        util.traceCall()
        return self._curSpeed

    #---
    # Turn left forward
    #---
    def turnLeftForward(self):
        util.traceCall()
        return self._curSpeed

    #---
    # .
    #---
    def setWay(self, way):
        util.traceCall()


    #---
    # .
    #---
    def robotStop(self):
        util.traceCall()
        self._wheel_left.motorStop()
        self._wheel_right.motorStop()

    #---
    # End the class instance and cleanup the GPIO in case of latest instance
    #---
    def robotEnd(self):
        util.traceCall()
        self._wheel_left.motorEnd()
        self._wheel_right.motorEnd()
        self._nb_instances -= 1
        if self._nb_instances == 0:
            # nothing
            pass

