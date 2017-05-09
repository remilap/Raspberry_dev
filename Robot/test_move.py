#!/usr/bin/python

# Robotics - Keyboard control Driving and Turning

import time
import lib_util
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

#	lib_motors_evol.Init()

	speed_r = 0
	speed_l = 0
	speed_max = 5
#	lib_motors_evol.StopMotors()
	running = True
	while running:
		stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r))
		c = stdscr.getkey()
#		stdscr.addstr(1, 0, "car=" + c + " " + str(ord(c)) + "         ")
		stdscr.addstr(1, 0, "UP=" + str(curses.KEY_UP) + "  " + c + "       ")
		if c == 'q':
			stdscr.addstr(1, 0, "Key: q")
			running = False
		elif c == ' ':
			stdscr.addstr(1, 0, "Key: space")
			speed_l = 0
			speed_r = 0
#			lib_motors_evol.StopMotors()
		elif c == 'KEY_UP':
			stdscr.addstr(1, 0, "Key: UP")
			if speed_l < speed_max:
				speed_l += 1
			if speed_r < speed_max:
				speed_r += 1
		elif c == 'KEY_DOWN':
			stdscr.addstr(1, 0, "Key: DOWN")
			if speed_l > -speed_max:
				speed_l -= 1
			if speed_r > -speed_max:
				speed_r -= 1
		elif c == 'KEY_LEFT':
			stdscr.addstr(1, 0, "Key: LEFT")
			if speed_l > -speed_max:
				speed_l -= 1
			if speed_r < speed_max:
				speed_r += 1
		elif c == 'KEY_RIGHT':
			stdscr.addstr(1, 0, "Key: RIGHT")
			if speed_l < speed_max:
				speed_l += 1
			if speed_r > -speed_max:
				speed_r -= 1
#		lib_motors_evol.Move(speed_l, speed_r)

#lib_motors_evol.LeftStay()
#lib_motors_evol.RightStay()

#	lib_motors_evol.StopMotors()

#	lib_motors_evol.End()

#curses.nocbreak()
#stdscr.keypad(False)
#curses.echo()
#curses.endwin()

wrapper(main)

