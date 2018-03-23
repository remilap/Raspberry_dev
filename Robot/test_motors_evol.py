#!/usr/bin/python

# CamJam EduKit 3 - Robotics
# Worksheet 4 - Evolve Driving and Turning

#import RPi.GPIO as GPIO # Import the GPIO Library
import time
#import lib_motors_evol as evol
import robot_2wheels_class as robot
import lib_util as util


#evol.init()
util.setDebug(1)
util.setTrace(1)

robot1 = robot.Robot_2Wheels("r2d2")
robot1.stopRobot()
robot1.moveStraight(0, 1)
time.sleep(5.2)
robot1.stopRobot()
if False:
	time.sleep(1.5)
	robot1.turnRightForward()
	time.sleep(1.2)
	robot1.stopRobot()
	time.sleep(1.5)
	robot1.turnLeftForward()
	time.sleep(1.2)
	robot1.stopRobot()
	time.sleep(1.5)
#	robot1.leftStay()
	time.sleep(1.2)
	robot1.stopRobot()
	time.sleep(1.5)
#	robot1.rightStay()
	time.sleep(1.2)
	robot1.stopRobot()
	time.sleep(1.5)
#	robot1.backwards()
	time.sleep(1.2)
	robot1.stopRobot()


robot1.robotEnd()

