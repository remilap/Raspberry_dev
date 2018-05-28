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
#	util.setDebug(1)
#	util.setTrace(1)
	util.setTraceOutput(1)

	evol.init()

	k_pres = "Key pressed: "
	speed_r = 0
	speed_l = 0
	speed_max = evol.getMaxSpeed()
	speed_up = 1
	speed_turn = 0.25

	evol.stopMotors()
	running = True
	while running:
		stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
		c = stdscr.getkey()
		stdscr.addstr(1, 0, " " * 50)
		if c == 'q':
			stdscr.addstr(1, 0, k_pres + "q => EXIT")
			running = False
			time.sleep(1)
		elif c == ' ':
			stdscr.addstr(1, 0, k_pres + "space => BRAKE")
			speed_l = 0
			speed_r = 0
			evol.stopMotors()
		elif c == 'KEY_UP':
			stdscr.addstr(1, 0, k_pres + "UP => SPEED UP")
			if speed_l + speed_up <= speed_max and speed_r + speed_up <= speed_max:
				speed_l += speed_up
				speed_r += speed_up
		elif c == 'KEY_DOWN':
			stdscr.addstr(1, 0, k_pres + "DOWN => SPEED DOWN")
			if speed_l - speed_up >= -speed_max and speed_r - speed_up >= -speed_max:
				speed_l -= speed_up
				speed_r -= speed_up
		elif c == 'KEY_LEFT':
			stdscr.addstr(1, 0, k_pres + "LEFT => TURN LEFT")
			if speed_l > speed_turn:
				speed_l -= speed_turn
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
				stdscr.refresh()
				evol.move(speed_l, speed_r)
				time.sleep(0.5)
				speed_l += speed_turn
			if speed_l < -speed_turn:
				speed_l += speed_turn
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
				stdscr.refresh()
				evol.move(speed_l, speed_r)
				time.sleep(0.5)
				speed_l -= speed_turn
		elif c == 'KEY_RIGHT':
			stdscr.addstr(1, 0, k_pres + "RIGHT => TURN RIGHT")
			if speed_r > speed_turn:
				speed_r -= speed_turn
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
				stdscr.refresh()
				evol.move(speed_l, speed_r)
				time.sleep(0.5)
				speed_r += speed_turn
			if speed_r < -speed_turn:
				speed_r += speed_turn
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
				stdscr.refresh()
				evol.move(speed_l, speed_r)
				time.sleep(0.5)
				speed_r -= speed_turn

		stdscr.refresh()
		evol.move(speed_l, speed_r)

#evol.leftStay()
#evol.rightStay()

	evol.stopMotors()

	evol.end()

wrapper(main)

