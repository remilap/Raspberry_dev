#!/usr/bin/python

# Robotics - Keyboard control Driving and Turning

import time
import lib_util as util
import curses
from curses import wrapper
import lib_motors_evol as evol


def main(stdscr):
	# Clear screen
	stdscr.clear()
#	util.SetDebug(1)
	util.SetTrace(1)

	evol.Init()

	speed_r = 0
	speed_l = 0
	speed_max = evol.getMaxSpeed()
	speed_up = 1
	speed_turn = 0.25

	evol.StopMotors()
	running = True
	while running:
		stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r))
		c = stdscr.getkey()
#		stdscr.addstr(1, 0, "car=" + c + " " + str(ord(c)) + "         ")
		stdscr.addstr(1, 0, "UP=" + str(curses.KEY_UP) + "  " + c + "       ")
		if c == 'q':
			stdscr.addstr(1, 0, "Key pressed: q => EXIT")
			stdscr.refresh()
			running = False
			time.sleep(1)
		elif c == ' ':
			stdscr.addstr(1, 0, "Key pressed: space => BRAKE")
			speed_l = 0
			speed_r = 0
			evol.StopMotors()
		elif c == 'KEY_UP':
			stdscr.addstr(1, 0, "Key pressed: UP => SPEED UP")
			if speed_l + speed_up <= speed_max and speed_r + speed_up <= speed_max:
				speed_l += speed_up
				speed_r += speed_up
		elif c == 'KEY_DOWN':
			stdscr.addstr(1, 0, "Key pressed: DOWN => SPEED DOWN")
			if speed_l - speed_up >= -speed_max and speed_r - speed_up >= -speed_max:
				speed_l -= speed_up
				speed_r -= speed_up
		elif c == 'KEY_LEFT':
			stdscr.addstr(1, 0, "Key pressed: LEFT => TURN LEFT")
			if speed_l - speed_turn >= -speed_max and speed_r + speed_turn <= speed_max:
				speed_l -= speed_turn
				speed_r += speed_turn
		elif c == 'KEY_RIGHT':
			stdscr.addstr(1, 0, "Key pressed: RIGHT => TURN RIGHT")
			if speed_l + speed_turn <= speed_max and speed_r - speed_turn >= -speed_max:
				speed_l += speed_turn
				speed_r -= speed_turn

		evol.Move(speed_l, speed_r)

#evol.LeftStay()
#evol.RightStay()

	evol.StopMotors()

	evol.End()

wrapper(main)

