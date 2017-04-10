#!/usr/bin/python

# Robotics - Keyboard control Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_util
import lib_motors_evol
import curses
from curses import wrapper


#stdscr = curses.initscr()
#curses.noecho()
#curses.cbreak()
#stdscr.keypad(True)

def main(stdscr):
	# Clear screen
	stdscr.clear()
	lib_util.SetDebug(1)

	lib_motors_evol.Init()

	speed_r = 0
	speed_l = 0
	lib_motors_evol.StopMotors()
	running = True
	while running:
		stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r))
		c = stdscr.getkey()
		if c == ord('q'):
			stdscr.addstr(0, 1, "Key: q")
			running = False
		elif c == ord(' '):
			stdscr.addstr(0, 1, "Key: space")
			speed_l = 0
			speed_r = 0
			lib_motors_evol.StopMotors()
		elif c == curses.KEY_UP:
			stdscr.addstr(0, 1, "Key: UP")
			if speed_l < lib_motors_evol.speed_max:
				speed_l += 1
			if speed_r < lib_motors_evol.speed_max:
				speed_r += 1
		elif c == curses.KEY_DOWN:
			stdscr.addstr(0, 1, "Key: DOWN")
			if speed_l > -lib_motors_evol.speed_max:
				speed_l -= 1
			if speed_r > -lib_motors_evol.speed_max:
				speed_r -= 1
		elif c == curses.KEY_LEFT:
			stdscr.addstr(0, 1, "Key: LEFT")
			if speed_l > -lib_motors_evol.speed_max:
				speed_l -= 1
			if speed_r < lib_motors_evol.speed_max:
				speed_r += 1
		elif c == curses.KEY_RIGHT:
			stdscr.addstr(0, 1, "Key: RIGHT")
			if speed_l < lib_motors_evol.speed_max:
				speed_l += 1
			if speed_r > -lib_motors_evol.speed_max:
				speed_r -= 1
		lib_motors_evol.Move(speed_l, speed_r)

#lib_motors_evol.LeftStay()
#lib_motors_evol.RightStay()

	lib_motors_evol.StopMotors()

	lib_motors_evol.End()

#curses.nocbreak()
#stdscr.keypad(False)
#curses.echo()
#curses.endwin()

wrapper(main)

