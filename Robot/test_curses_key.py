#!/usr/bin/python

# Keyboard control Driving and Turning

import time
import lib_util as util
import curses
from curses import wrapper


def main(stdscr):
	# Clear screen
	stdscr.clear()
	util.setDebug(1)
	util.setTraceOutput(1)

	k_pres = "Key pressed: "
	speed_r = 0
	speed_l = 0
	speed_max = 5
	speed_up = 1
	speed_turn = 0.25

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
				time.sleep(0.5)
				speed_l += speed_turn
			if speed_l < -speed_turn:
				speed_l += speed_turn
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
				stdscr.refresh()
				time.sleep(0.5)
				speed_l -= speed_turn
		elif c == 'KEY_RIGHT':
			stdscr.addstr(1, 0, k_pres + "RIGHT => TURN RIGHT")
			if speed_r > speed_turn:
				speed_r -= speed_turn
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
				stdscr.refresh()
				time.sleep(0.5)
				speed_r += speed_turn
			if speed_r < -speed_turn:
				speed_r += speed_turn
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
				stdscr.refresh()
				time.sleep(0.5)
				speed_r -= speed_turn

		stdscr.refresh()

	util.closeTrace()


wrapper(main)

